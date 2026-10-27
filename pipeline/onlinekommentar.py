"""Kommentierungen von Onlinekommentar.ch (OK) zu den fünf Steuererlassen finden und als Text ablegen.
Öffentliche API, kein Schlüssel nötig.

    python3 pipeline/onlinekommentar.py liste                 # alle OK-Kommentierungen zu DBG, StHG, VStG, MWSTG, StG
    python3 pipeline/onlinekommentar.py holen DBG 10          # Text mit Randnoten und Fussnoten nach
                                                              # arbeit/DBG/art-10/01_Recherche/OK_DBG_art-10.md, Zitiervorschlag
    python3 pipeline/onlinekommentar.py holen DBG 10 --nach DBG/art-26   # Ablage beim Artikel, der gerade kommentiert wird
"""
from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import ARBEIT, USER_AGENT, art_slug  # noqa: E402

API = "https://onlinekommentar.ch/api/commentaries"
ERLASSE = {
    "Federal Act on Direct Federal Tax": "DBG",
    "Tax Harmonisation Act": "StHG",
    "Withholding Tax Act": "VStG",
    "Value Added Tax Act": "MWSTG",
    "Stamp Duties Act": "StG",
}
KOPF = {"User-Agent": USER_AGENT, "Accept": "application/json"}


def alle() -> list[dict]:
    """Alle deutschen OK-Kommentierungen zu den fünf Erlassen."""
    aus, seite = [], 1
    while True:
        r = requests.get(API, params={"language": "de", "page": seite}, headers=KOPF, timeout=60)
        r.raise_for_status()
        d = r.json()
        for x in d.get("data", []):
            akt = (x.get("legislative_act") or {}).get("title", "")
            kurz = ERLASSE.get(akt) or next((k for k in ERLASSE.values() if x.get("title", "").endswith(" " + k)), None)
            if kurz:
                x["erlass"] = kurz
                aus.append(x)
        if seite >= d.get("meta", {}).get("last_page", seite):
            return aus
        seite += 1


def text(content: str) -> str:
    """HTML der Kommentierung in lesbaren Text: Randnoten als «N. 12», Fussnoten als [Fn. …]."""
    t = re.sub(r'<footnote data-content="(.*?)">.*?</footnote>', lambda m: f" [Fn.: {html.unescape(m.group(1))}]", content, flags=re.S)
    t = re.sub(r'<span class="paragraph-nr">(\d+)</span>', r"N. \1 ", t)
    t = re.sub(r"<h(\d)[^>]*>", lambda m: "\n\n" + "#" * int(m.group(1)) + " ", t)
    t = re.sub(r"</(p|h\d|li)>", "\n", t)
    t = re.sub(r"<li[^>]*>", "- ", t)
    t = re.sub(r"<[^>]+>", "", t)
    return re.sub(r"\n{3,}", "\n\n", html.unescape(t)).strip()


def holen(erlass: str, nummer: str, nach: str | None) -> Path | None:
    titel = f"Art. {nummer} {erlass}"
    treffer = [x for x in alle() if x["erlass"].lower() == erlass.lower() and x.get("title", "").strip() == titel]
    if not treffer:
        print(f"Keine OK-Kommentierung zu {titel}.")
        return None
    meta = requests.get(treffer[0]["link"], headers=KOPF, timeout=60).json()
    meta = meta.get("data", meta)
    ziel_art = nach or f"{erlass}/{art_slug(nummer)}"
    e, slug = ziel_art.split("/")
    ziel = ARBEIT / e / slug / "01_Recherche" / f"OK_{erlass}_{art_slug(nummer)}.md"
    ziel.parent.mkdir(parents=True, exist_ok=True)
    autoren = "/".join(a["name"] for a in meta.get("authors", []))
    kopf = (f"# OK, {titel}\n\n- Autor:innen: {autoren}\n- Stand (date): {meta.get('date')}\n"
            f"- Zitiervorschlag kurz: {meta.get('suggested_citation_short')}\n"
            f"- Zitiervorschlag lang: {meta.get('suggested_citation_long')}\n- Link: {meta.get('html_link')}\n\n")
    ziel.write_text(kopf + text(meta.get("content", "")) + "\n", encoding="utf-8")
    print(f"{titel}: {autoren}, Stand {meta.get('date')} → {ziel}")
    print(f"Kurzzitat: {meta.get('suggested_citation_short')}")
    return ziel


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("liste")
    h = sub.add_parser("holen")
    h.add_argument("erlass")
    h.add_argument("nummer")
    h.add_argument("--nach", help="Artikel-ID, in deren 01_Recherche abgelegt wird")
    a = ap.parse_args()
    if a.cmd == "liste":
        for x in sorted(alle(), key=lambda x: (x["erlass"], x.get("title", ""))):
            print(f"{x['erlass']}\t{x.get('title')}\t{'/'.join(au['name'] for au in x.get('authors', []))}\t{x.get('date')}\t{x.get('html_link')}")
    else:
        holen(a.erlass, a.nummer, a.nach)


if __name__ == "__main__":
    main()
