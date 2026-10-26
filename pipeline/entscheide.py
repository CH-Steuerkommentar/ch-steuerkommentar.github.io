"""Entscheide: sucht für jeden Artikel die Entscheide des Bundesgerichts, die ihn zitieren,
lädt deren Volltexte (einmal je Entscheid, im Cache) und hält fest, welche Normen der
fünf Erlasse jeder Entscheid zitiert. Kein Sprachmodell, keine Kosten.

    python3 pipeline/entscheide.py DBG/art-26            # ein Artikel
    python3 pipeline/entscheide.py DBG                   # alle offenen Artikel des DBG
    python3 pipeline/entscheide.py --naechste 20         # die nächsten 20 offenen Artikel der Queue

Quelle: entscheidsuche.ch (BGer und BGE). Ergebnis:
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


def artikel_bearbeiten(qid: str, queue: dict, nachtragen: list[str]) -> int:
    erlass, slug = qid.split("/")
    nummer = queue["artikel"][qid]["nummer"]
    abk = ERLASSE[erlass]["abk"] + ERLASSE[erlass]["abk_mehrdeutig"]
    abfrage = f"\"Art. {nummer}\" AND ({' OR '.join(abk)})"
    hits = es_suche(abfrage)
    gefunden = []
    for hit in hits:
        e = entscheid_laden(hit)
        schluessel = f"{erlass}/{nummer.lower()}"
        if schluessel in e["normen"]:
            gefunden.append({
                "id": e["id"], "referenz": e["referenz"], "datum": e["datum"],
                "bge": "CH_BGE" in e["hierarchie"], "ausschnitte": e["normen"][schluessel][:3],
            })
    for ref in nachtragen:
        gefunden.append({"id": None, "referenz": [ref], "datum": None, "bge": ref.startswith("BGE"),
                         "ausschnitte": [], "nachgetragen": True})
    gefunden.sort(key=lambda x: (x["datum"] or "9999"))
    schreibe_json(ZITATE / erlass / f"{slug}.json", {"artikel": qid, "abfrage": abfrage,
                                                     "suchtreffer": len(hits), "entscheide": gefunden})
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
    ap.add_argument("--nachtragen", nargs="*", default=[],
                    help="Referenzen, die die Gegenprobe gefunden hat (z.B. 2C_123/2020), nur mit einem Artikel")
    a = ap.parse_args()
    queue = lade_json(QUEUE)
    if queue is None:
        sys.exit("Zuerst pipeline/inventar.py ausführen.")
    ids = auswahl(a, queue)
    for i, qid in enumerate(ids, 1):
        n = artikel_bearbeiten(qid, queue, a.nachtragen if len(ids) == 1 else [])
        print(f"[{i}/{len(ids)}] {qid}: {n} Entscheide")
        schreibe_json(QUEUE, queue)
    print(f"Entscheide im Cache: {len(list(ENTSCHEIDE.glob('*.json')))}")


if __name__ == "__main__":
    main()
