"""Führt die bereinigten Arbeitspakete (daten/ile-literatur/ergebnis/paket_*.json) zum Katalog zusammen.

Entfernt Dubletten über Paketgrenzen (gleicher erster Nachname, gleiche Titelwörter, gleiches Jahr),
vereinigt Artikel, Nennungen und Fundorte und schreibt
  daten/ile-literatur/katalog.json        (Liste der Werke, Grundlage für md2site)
  daten/ile-literatur/artikel/<ERLASS>/art-<N>.json  (je Bestimmung die Werke, für Skill und Website)
  daten/ile-literatur/nach_artikel.md     (Übersicht je Bestimmung zur Durchsicht durch PH)
"""
from __future__ import annotations

import collections
import json
import re
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent / "daten" / "ile-literatur"
ERLASSE = ["DBG", "StHG", "VStG", "MWSTG", "StG"]


def schluessel(z: str) -> str:
    name = re.match(r"[A-Za-zÄÖÜäöüßéèêàâçëïôûñ'’\-]+", z)
    teile = z.split(",", 2)
    titel = teile[1] if len(teile) > 1 else ""
    woerter = re.findall(r"[a-zäöüéèàç]{4,}", titel.lower())[:4]
    jahr = re.findall(r"\b(?:19|20)\d\d\b", z)
    return f"{name.group(0).lower() if name else ''}|{' '.join(woerter)}|{jahr[0] if jahr else ''}"


def art_sort(a: str):
    erlass, nr = a.split(" ", 1)
    m = re.match(r"(\d+)([a-z]*)", nr)
    return (ERLASSE.index(erlass) if erlass in ERLASSE else 9, int(m.group(1)) if m else 0, m.group(2) if m else nr)


def main() -> None:
    werke: dict[str, dict] = {}
    for datei in sorted((WURZEL / "ergebnis").glob("*.json")):
        for e in json.loads(datei.read_text(encoding="utf-8")):
            k = schluessel(e["zitat"])
            w = werke.get(k)
            if w is None:
                werke[k] = {"zitat": e["zitat"], "jahr": e.get("jahr"), "ile": bool(e.get("ile")),
                            "url": e.get("url", ""),
                            "artikel": list(dict.fromkeys(e.get("artikel", []))),
                            "nennungen": e.get("nennungen", 1), "fundorte": list(e.get("fundorte", []))}
                continue
            if len(e["zitat"]) > len(w["zitat"]):
                w["zitat"] = e["zitat"]
            w["ile"] |= bool(e.get("ile"))
            w["url"] = w["url"] or e.get("url", "")
            w["artikel"] = list(dict.fromkeys(w["artikel"] + e.get("artikel", [])))
            w["nennungen"] += e.get("nennungen", 1)
            for f in e.get("fundorte", []):
                if f not in w["fundorte"] and len(w["fundorte"]) < 12:
                    w["fundorte"].append(f)
    liste = sorted(werke.values(), key=lambda w: w["zitat"].lower())
    for i, w in enumerate(liste, 1):
        w["artikel"].sort(key=art_sort)
        w["id"] = f"L{i:05d}"
    (WURZEL / "katalog.json").write_text(json.dumps(liste, ensure_ascii=False, indent=1), encoding="utf-8")

    je = collections.defaultdict(list)
    for w in liste:
        for a in w["artikel"]:
            je[a].append(w)
    ordner = WURZEL / "artikel"
    if ordner.exists():
        for alt in ordner.glob("*/art-*.json"):
            alt.unlink()
    for a, ws in je.items():
        erlass, nr = a.split(" ", 1)
        ziel = ordner / erlass / f"art-{nr}.json"
        ziel.parent.mkdir(parents=True, exist_ok=True)
        ws = sorted(ws, key=lambda w: (not w["ile"], -w["nennungen"], w["zitat"].lower()))
        ziel.write_text(json.dumps([{k: w[k] for k in ("id", "zitat", "jahr", "ile", "url", "nennungen")} for w in ws],
                                   ensure_ascii=False, indent=1), encoding="utf-8")
    zeilen = ["# ILE-Literaturkatalog nach Bestimmung", "",
              f"{len(liste)} Werke, davon {sum(1 for w in liste if w['artikel'])} mit Artikelzuordnung; "
              f"{len(je)} Bestimmungen. ILE-Werke mit (ILE) markiert; im Abschnitt «Weiterführende Literatur» erscheint ein Werk nur, "
              "wenn die Kommentierung es nicht schon zitiert.", ""]
    for a in sorted(je, key=art_sort):
        zeilen.append(f"## Art. {a.split(' ', 1)[1]} {a.split(' ', 1)[0]} ({len(je[a])})")
        zeilen.append("")
        for w in sorted(je[a], key=lambda w: (-w["nennungen"], w["zitat"].lower())):
            zeilen.append(f"- {w['zitat']}{' (ILE)' if w['ile'] else ''} · {w['nennungen']}×")
        zeilen.append("")
    (WURZEL / "nach_artikel.md").write_text("\n".join(zeilen), encoding="utf-8")
    print(f"{len(liste)} Werke, {len(je)} Bestimmungen")


if __name__ == "__main__":
    main()
