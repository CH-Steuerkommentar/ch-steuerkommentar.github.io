"""Entscheide: sucht für jeden Artikel die Entscheide des Bundesgerichts, die ihn zitieren,
lädt deren Volltexte (einmal je Entscheid, im Cache) und hält fest, welche Normen der
fünf Erlasse jeder Entscheid zitiert. Kein Sprachmodell, keine Kosten.

    python3 pipeline/entscheide.py DBG/art-26            # ein Artikel
    python3 pipeline/entscheide.py DBG                   # alle offenen Artikel des DBG
    python3 pipeline/entscheide.py --naechste 20         # die nächsten 20 offenen Artikel der Queue

Quelle: Open Case Law (BGE und BGer, Standard; Suchwege nach Anhang A.1 des Skills); mit --quelle
entscheidsuche wie früher entscheidsuche.ch. Kantonale Entscheide holt der Skill beim Schreiben über
Entscheidsuche. Ergebnis:
- data/entscheide/<id>.json   Metadaten, Volltext, zitierte Normen
- data/zitate/<Erlass>/<art>.json  Entscheide, die den Artikel zitieren, mit Ausschnitten
- data/queue.json             Zahl der Entscheide je Artikel (= Priorität)

Grenze: entscheidsuche.ch findet nicht jeden Entscheid, den Open Case Law führt. Die
Gegenprobe macht der Skill beim Schreiben (Liste, ohne Volltexte); was fehlt, kommt über
`--nachtragen` in den nächsten Lauf.
"""
from __future__ import annotations

import argparse
import html as htmlmod
import re
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import DATA, ENTSCHEIDE, ERLASSE, QUEUE, USER_AGENT, art_sortkey, lade_json, schreibe_json  # noqa: E402
from normen import zitierte_normen  # noqa: E402

SUCHE = "https://entscheidsuche.ch/_search.php"
ZITATE = DATA / "zitate"
HIERARCHIEN = ["CH_BGer", "CH_BGE"]
S = requests.Session()
S.headers["User-Agent"] = USER_AGENT


def es_suche(abfrage: str) -> list[dict]:
    """Alle Treffer (ohne Volltext) für eine query_string-Abfrage in BGer und BGE."""
    treffer, nach = [], None
    while True:
        body = {
            "size": 500, "track_total_hits": True,
            "sort": [{"date": "asc"}, {"id": "asc"}],
            "query": {"bool": {"must": [{"query_string": {"query": abfrage, "default_operator": "AND"}}],
                               "filter": [{"terms": {"hierarchy": HIERARCHIEN}}]}},
            "_source": {"excludes": ["attachment.content"]},
        }
        if nach:
            body["search_after"] = nach
        r = S.post(SUCHE, json=body, timeout=120)
        r.raise_for_status()
        hits = r.json()["hits"]["hits"]
        treffer += hits
        if len(hits) < 500:
            return treffer
        nach = hits[-1]["sort"]
        time.sleep(0.3)


def html_zu_text(h: str) -> str:
    h = re.sub(r"(?is)<(script|style).*?</\1>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</h\d>|</tr>", "\n", h)
    t = htmlmod.unescape(re.sub(r"<[^>]+>", " ", h)).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t).strip()


def entscheid_laden(hit: dict) -> dict:
    src = hit["_source"]
    did = src["id"]
    pfad = ENTSCHEIDE / f"{did}.json"
    e = lade_json(pfad)
    if e is not None:
        return e
    url = src.get("attachment", {}).get("content_url")
    text = ""
    if url:
        r = S.get(url, timeout=120)
        r.raise_for_status()
        roh = r.content.decode("utf-8", errors="replace")
        text = html_zu_text(roh) if "<" in roh[:2000] else roh
        time.sleep(0.2)
    normen = zitierte_normen(text)
    e = {
        "id": did,
        "referenz": src.get("reference", []),
        "datum": src.get("date"),
        "hierarchie": src.get("hierarchy", []),
        "sprache": src.get("language") or src.get("attachment", {}).get("language"),
        "titel": (src.get("title") or {}).get("de"),
        "url": url,
        "text": text,
        "normen": {f"{k[0]}/{k[1]}": v for k, v in normen.items()},
    }
    schreibe_json(pfad, e)
    return e


def ocl_varianten(ref: str) -> list[str]:
    """Schreibweisen einer Referenz, unter denen Open Case Law den Entscheid findet."""
    import re
    ref = ref.strip()
    if ref.upper().startswith("BGE"):
        return [re.sub(r"\s+", " ", ref)]
    m = re.match(r"^(\d[A-Z]{1,2})[-_.](\d+)[/-](\d{4})$", ref)
    if not m:
        return [ref]
    k, n, j = m.groups()
    return [f"{k}_{n}/{j}", f"{k}.{n}/{j}"]


_ocl = None


def ocl_client():
    global _ocl
    if _ocl is None:
        from ocl import OCL
        _ocl = OCL()
    return _ocl


def ocl_entscheid_laden(decision_id: str, gericht: str) -> dict | None:
    """Lädt einen Entscheid aus Open Case Law in den Cache (Volltext, Normen, Zitierstring)."""
    import re
    sicher = lambda x: re.sub(r"[^\w.-]+", "_", x)  # noqa: E731
    alias = ENTSCHEIDE / "_verweise" / f"{sicher(decision_id)}.json"   # Verweis Referenz -> Cache-Datei
    if alias.exists():
        ziel = lade_json(alias, {}).get("datei")
        e = lade_json(ENTSCHEIDE / ziel) if ziel else None
        if e is not None:
            return e
    d = ocl_client().entscheid(decision_id, volltext=True)
    if not d:
        return None
    pfad = ENTSCHEIDE / f"ocl_{sicher(d.get('decision_id') or decision_id)}.json"
    if pfad.exists():
        schreibe_json(alias, {"datei": pfad.name})
        return lade_json(pfad)
    text = d.get("full_text") or ""
    # Open Case Law bricht Zeilen innerhalb von Absätzen um; Absätze sind durch Leerzeilen getrennt.
    # Auf eine Zeile je Absatz bringen, damit Erwägungsnummern am Zeilenanfang stehen.
    text = re.sub(r"[ \t]*\n[ \t]*(?!\n)", " ", text.replace("\r", ""))
    text = re.sub(r"\n\s*\n+", "\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text).replace(" )", ")").replace("( ", "(")
    normen = zitierte_normen(text + "\n" + "; ".join(d.get("statutes") or []))
    referenz = [d.get("citation_string_de") or d.get("docket_number_2") or decision_id]
    e = {
        "id": pfad.stem,
        "quelle": "opencaselaw",
        "ocl_id": d.get("decision_id") or decision_id,
        "referenz": referenz,
        "geschaeftsnummer": d.get("docket_number_2") or d.get("docket_number"),
        "datum": d.get("decision_date"),
        "hierarchie": ["CH_BGE"] if (d.get("court") == "bge" or gericht == "bge") else ["CH_BGer"],
        "sprache": d.get("language"),
        "titel": d.get("regeste") or d.get("title"),
        "url": d.get("canonical_url"),
        "zitat_de": d.get("citation_string_de"),
        "zitat_fr": d.get("citation_string_fr"),
        "text": text,
        "normen": {f"{k[0]}/{k[1]}": v for k, v in normen.items()},
    }
    schreibe_json(pfad, e)
    schreibe_json(alias, {"datei": pfad.name})
    return e


def artikel_bearbeiten(qid: str, queue: dict, nachtragen: list[str], quelle: str = "ocl") -> int:
    erlass, slug = qid.split("/")
    nummer = queue["artikel"][qid]["nummer"]
    abk = ERLASSE[erlass]["abk"] + ERLASSE[erlass]["abk_mehrdeutig"]
    schluessel = f"{erlass}/{nummer.lower()}"
    gefunden, gesehen, suchtreffer = [], set(), 0
    if quelle == "ocl":
        # Kandidaten präzise über Entscheidsuche (Phrasensuche, BGer und BGE); geladen werden die Entscheide
        # aus Open Case Law (Volltext, bereinigte Normen, offizielle Zitierstrings). Nur wenn ein Entscheid
        # dort fehlt, dient der Volltext von Entscheidsuche als Ersatz.
        abfrage = f"\"Art. {nummer}\" AND ({' OR '.join(abk)})"
        hits = es_suche(abfrage)
        suchtreffer = len(hits)
        refs = [(h["_source"].get("reference") or [None])[0] for h in hits]
        refs += list(nachtragen)
        for hit, ref in zip(hits + [None] * len(nachtragen), refs):
            e = None
            if ref:
                for kandidat in ocl_varianten(ref):
                    try:
                        e = ocl_entscheid_laden(kandidat, "bge" if kandidat.startswith("BGE") else "bger")
                    except Exception:  # noqa: BLE001
                        e = None
                    if e:
                        break
            if e is None and hit is not None:
                e = entscheid_laden(hit)
            if not e or schluessel not in e["normen"] or e["id"] in gesehen:
                continue
            gesehen.add(e["id"])
            gefunden.append({"id": e["id"], "referenz": e["referenz"], "datum": e["datum"],
                             "bge": "CH_BGE" in e["hierarchie"], "ausschnitte": e["normen"][schluessel][:3]})
        abfrage += " (Kandidaten: Entscheidsuche; Entscheide: Open Case Law)"
    else:
        abfrage = f"\"Art. {nummer}\" AND ({' OR '.join(abk)})"
        hits = es_suche(abfrage)
        suchtreffer = len(hits)
        for hit in hits:
            e = entscheid_laden(hit)
            if schluessel in e["normen"]:
                gefunden.append({"id": e["id"], "referenz": e["referenz"], "datum": e["datum"],
                                 "bge": "CH_BGE" in e["hierarchie"], "ausschnitte": e["normen"][schluessel][:3]})
        for ref in nachtragen:
            gefunden.append({"id": None, "referenz": [ref], "datum": None, "bge": ref.startswith("BGE"),
                             "ausschnitte": [], "nachgetragen": True})
    gefunden.sort(key=lambda x: (x["datum"] or "9999"))
    schreibe_json(ZITATE / erlass / f"{slug}.json", {"artikel": qid, "abfrage": abfrage, "quelle": quelle,
                                                     "suchtreffer": suchtreffer, "entscheide": gefunden})
    q = queue["artikel"][qid]
    q["entscheide"] = len(gefunden)
    q["prioritaet"] = len(gefunden)
    if q["status"] == "offen":
        q["status"] = "entscheide"
    return len(gefunden)


def auswahl(args, queue) -> list[str]:
    alle = queue["artikel"]
    if args.naechste:
        offen = [k for k, v in alle.items() if v["status"] == "offen"]
        offen.sort(key=lambda k: (k.split("/")[0], art_sortkey(alle[k]["nummer"])))
        return offen[: args.naechste]
    ids = []
    for z in args.ziele:
        if "/" in z:
            ids.append(z)
        else:
            ids += [k for k, v in alle.items() if v["erlass"] == z and v["status"] in ("offen", "entscheide")]
    return ids


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ziele", nargs="*", help="Erlass (z.B. DBG) oder Artikel (z.B. DBG/art-26)")
    ap.add_argument("--naechste", type=int, default=0)
    ap.add_argument("--quelle", choices=["ocl", "entscheidsuche"], default="ocl",
                    help="Bundesgericht über Open Case Law (Standard) oder entscheidsuche.ch")
    ap.add_argument("--nachtragen", nargs="*", default=[],
                    help="Referenzen, die die Gegenprobe gefunden hat (z.B. 2C_123/2020), nur mit einem Artikel")
    a = ap.parse_args()
    queue = lade_json(QUEUE)
    if queue is None:
        sys.exit("Zuerst pipeline/inventar.py ausführen.")
    ids = auswahl(a, queue)
    for i, qid in enumerate(ids, 1):
        n = artikel_bearbeiten(qid, queue, a.nachtragen if len(ids) == 1 else [], a.quelle)
        print(f"[{i}/{len(ids)}] {qid}: {n} Entscheide")
        schreibe_json(QUEUE, queue)
    print(f"Entscheide im Cache: {len(list(ENTSCHEIDE.glob('*.json')))}")


if __name__ == "__main__":
    main()
