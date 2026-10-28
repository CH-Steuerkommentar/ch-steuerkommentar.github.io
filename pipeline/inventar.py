"""Inventar: holt die geltende Fassung jedes Erlasses von Fedlex und legt je Artikel
Nummer, Sachüberschrift, Normtext und Status (aufgehoben oder nicht) ab.

    python3 pipeline/inventar.py                 # alle fünf Erlasse
    python3 pipeline/inventar.py DBG StHG        # nur diese
    python3 pipeline/inventar.py --stichtag 2027-01-01

Ergebnis: data/inventar/<Erlass>.json und neue Einträge in data/queue.json.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys

import requests
from bs4 import BeautifulSoup

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from config import ausgenommen, ERLASSE, INVENTAR, QUEUE, USER_AGENT, art_slug, art_sortkey, lade_json, schreibe_json  # noqa: E402

SPARQL = "https://fedlex.data.admin.ch/sparqlendpoint"

ABFRAGE = """
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT ?d ?url WHERE {
  ?cons jolux:isMemberOf <%(eli)s> ;
        jolux:dateApplicability ?d ;
        jolux:isRealizedBy ?expr .
  ?expr jolux:language <http://publications.europa.eu/resource/authority/language/DEU> ;
        jolux:isEmbodiedBy ?m .
  ?m jolux:userFormat <https://fedlex.data.admin.ch/vocabulary/user-format/html> ;
     jolux:isExemplifiedBy ?url .
  FILTER(?d <= "%(stichtag)s"^^xsd:date)
} ORDER BY DESC(?d) LIMIT 1
"""


def aktuelle_fassung(eli: str, stichtag: str) -> tuple[str, str]:
    r = requests.post(SPARQL, data={"query": ABFRAGE % {"eli": eli, "stichtag": stichtag}},
                      headers={"Accept": "application/sparql-results+json", "User-Agent": USER_AGENT}, timeout=120)
    r.raise_for_status()
    b = r.json()["results"]["bindings"]
    if not b:
        raise RuntimeError(f"Keine Fassung für {eli} gefunden")
    return b[0]["d"]["value"], b[0]["url"]["value"]


def text(el) -> str:
    t = el.get_text(" ", strip=True)
    t = t.replace("\xa0", " ")
    return re.sub(r"\s+", " ", t).strip()


def parse(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    # Fussnoten-Hinweise aus dem Normtext entfernen
    artikel = []
    letzte_ueberschrift = ""
    for el in soup.find_all(["h1", "h2", "h3", "h4", "h5", "article"]):
        if el.name != "article":
            for sup in el.find_all("sup"):
                sup.decompose()
            u = text(el)
            u = re.sub(r"^\d+[a-z]*\.\s*(Titel|Kapitel|Abschnitt|Teil)\s*:\s*", "", u)
            u = re.sub(r"^[a-z]\.\s+", "", u)
            letzte_ueberschrift = u
            continue
        aid = el.get("id", "")
        if not aid.startswith("art_"):
            continue
        kopf = el.find("h6")
        if kopf is None:
            continue
        for sup in kopf.find_all("sup"):
            sup.decompose()
        # Nummer aus der ID: art_37_a -> 37a, art_205_b_bis -> 205bbis, art_43_48 -> 43–48
        teile = aid[4:].split("_")
        if len(teile) >= 2 and teile[1].isdigit():
            nr_roh = f"{teile[0]}–{teile[1]}"
        else:
            nr_roh = "".join(teile)
        # Sachüberschrift: Kopfzeile ohne «Art. N» (<b>) und ohne den Zusatzbuchstaben (<i>)
        for tag in kopf.find_all(["b", "i"]):
            tag.decompose()
        sach = text(kopf).replace("Art.", "").strip(" ;:")
        # Fedlex setzt einzelne Nummernzusätze (z. B. 205d) als unformatierten Text.
        # Nur den zur Artikelnummer gehörenden, freistehenden Zusatz entfernen.
        zusatz = re.search(r"[a-z]+$", nr_roh)
        if zusatz:
            sach = re.sub(rf"^{re.escape(zusatz.group())}(?:\s+|$)", "", sach)
        koerper = el.find("div", class_="collapseable")
        absaetze, fussnoten = [], []
        if koerper is not None:
            fn = koerper.find("div", class_="footnotes")
            if fn is not None:
                fussnoten = [text(p) for p in fn.find_all("p")]
                fn.decompose()
            for sup in koerper.find_all("sup"):
                if sup.find("a"):
                    sup.decompose()
            for p in koerper.find_all(["p", "dt", "dd"]):
                if p.name == "dt":
                    continue
                t = text(p)
                if p.name == "dd":
                    dt_el = p.find_previous_sibling("dt")
                    t = (text(dt_el) + " " + t) if dt_el is not None else t
                if t:
                    absaetze.append(t)
        normtext = "\n".join(absaetze)
        aufgehoben = (not normtext.strip(" .…")) or bool(re.fullmatch(r"(…\s*)+", normtext.strip())) \
            or normtext.strip().lower().startswith("aufgehoben")
        bereich = bool(re.search(r"\d[–-]\d", nr_roh)) or aid.count("_") >= 2 and re.fullmatch(r"art_\d+_\d+", aid)
        if not sach:
            # Erlasse ohne Sachüberschriften (z. B. VStG): Randtitel der übergeordneten Gliederung unterhalb des Kapitels
            stufen = []
            for sec in el.find_parents("section"):
                sid = sec.get("id", "")
                if "lvl_" not in sid.split("/")[-1]:
                    break
                kopf_g = sec.find("div", class_="heading", recursive=False) or sec.find(class_="heading")
                if kopf_g is not None:
                    kopf_g = BeautifulSoup(str(kopf_g), "html.parser")
                    for sup in kopf_g.find_all("sup"):
                        sup.decompose()
                    g = re.sub(r"^(\d+\s*[a-z]{0,6}|[A-Z]|[IVX]+|[a-z])\s*\.\s*", "", text(kopf_g)).strip()
                    if g:
                        stufen.insert(0, g)
            if stufen:
                sach = stufen[0] + (": " + ", ".join(stufen[1:]) if len(stufen) > 1 else "")
        artikel.append({
            "id": aid,
            "nummer": nr_roh,
            "sachueberschrift": sach or letzte_ueberschrift,
            "sachueberschrift_quelle": "artikel" if sach else "gliederung",
            "normtext": normtext,
            "fussnoten_fedlex": fussnoten,
            "aufgehoben": bool(aufgehoben or bereich),
        })
    return artikel


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("erlasse", nargs="*", default=list(ERLASSE))
    ap.add_argument("--stichtag", default=dt.date.today().isoformat())
    a = ap.parse_args()

    queue = lade_json(QUEUE, {"artikel": {}})
    for key in a.erlasse:
        e = ERLASSE[key]
        datum, url = aktuelle_fassung(e["eli"], a.stichtag)
        html = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=180).content.decode("utf-8")
        arts = parse(html)
        arts.sort(key=lambda x: art_sortkey(x["nummer"]))
        schreibe_json(INVENTAR / f"{key}.json", {
            "erlass": key, "name": e["name"], "sr": e["sr"], "fassung_vom": datum, "quelle": url,
            "abgerufen": dt.date.today().isoformat(), "artikel": arts,
        })
        neu = 0
        for art in arts:
            qid = f"{key}/{art_slug(art['nummer'])}"
            eintrag = queue["artikel"].get(qid)
            if eintrag is None:
                queue["artikel"][qid] = {
                    "erlass": key, "nummer": art["nummer"], "sachueberschrift": art["sachueberschrift"],
                    "status": "aufgehoben" if art["aufgehoben"] else ("ausgenommen" if ausgenommen(key, art["nummer"]) else "offen"),
                    "entscheide": None, "karten_fertig": 0, "prioritaet": None, "notiz": "",
                }
                neu += 1
            else:
                eintrag["sachueberschrift"] = art["sachueberschrift"]
                if art["aufgehoben"] and eintrag["status"] == "offen":
                    eintrag["status"] = "aufgehoben"
                elif ausgenommen(key, art["nummer"]) and eintrag["status"] in ("offen", "entscheide", "karten", "bereit"):
                    eintrag["status"] = "ausgenommen"
        aktiv = sum(1 for x in arts if not x["aufgehoben"])
        print(f"{key}: Fassung vom {datum}, {len(arts)} Artikel ({aktiv} in Kraft), {neu} neu in der Queue")
    schreibe_json(QUEUE, queue)


if __name__ == "__main__":
    main()
