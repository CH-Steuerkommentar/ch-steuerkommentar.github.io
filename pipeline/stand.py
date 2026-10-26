"""Stand des Projekts und Steuerung der Warteschlange.

    python3 pipeline/stand.py                          # Übersicht je Erlass und Status, Kosten der Batches
    python3 pipeline/stand.py naechster [--anzahl 5]   # nächste Artikel zum Schreiben (Status «bereit»)
    python3 pipeline/stand.py setze DBG/art-26 geschrieben [--notiz "…"]

Status eines Artikels, in dieser Reihenfolge:
  offen → entscheide → karten → bereit → in_arbeit → geschrieben → geprueft → veroeffentlicht
  (aufgehoben: nicht zu kommentieren)
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import BATCHES, BATCH_PREISE, ERLASSE, QUEUE, lade_json, schreibe_json  # noqa: E402

STATUS = ["offen", "entscheide", "karten", "bereit", "in_arbeit", "geschrieben", "geprueft", "veroeffentlicht",
          "aufgehoben"]


def uebersicht(_a) -> None:
    q = lade_json(QUEUE)
    print(f"{'Erlass':7}" + "".join(f"{s[:10]:>11}" for s in STATUS))
    for e in ERLASSE:
        c = Counter(v["status"] for v in q["artikel"].values() if v["erlass"] == e)
        print(f"{e:7}" + "".join(f"{c.get(s, 0):>11}" for s in STATUS))
    c = Counter(v["status"] for v in q["artikel"].values())
    print(f"{'Total':7}" + "".join(f"{c.get(s, 0):>11}" for s in STATUS))
    kosten, monat = 0.0, dt.date.today().strftime("%Y%m")
    kosten_monat = 0.0
    for p in BATCHES.glob("*/batch.json"):
        m = lade_json(p)
        if "tokens_in" in m:
            pr = BATCH_PREISE.get(m["modell"], BATCH_PREISE["claude-sonnet-5-5"])
            k = (m["tokens_in"] * pr["in"] + m["tokens_out"] * pr["out"]) / 1e6
            kosten += k
            if p.parent.name.startswith(monat):
                kosten_monat += k
    print(f"\nBatch-Kosten (aus Token-Zählung, ohne Cache-Rabatt geschätzt): total {kosten:.2f} USD, "
          f"dieser Monat {kosten_monat:.2f} USD")


def naechster(a) -> None:
    q = lade_json(QUEUE)["artikel"]
    bereit = [(k, v) for k, v in q.items() if v["status"] == "bereit"]
    bereit.sort(key=lambda kv: -(kv[1]["prioritaet"] or 0))
    if not bereit:
        print("Kein Artikel bereit. Zuerst entscheide.py, karteikarten.py und register.py laufen lassen.")
        return
    for k, v in bereit[: a.anzahl]:
        print(f"{k}\t{v['entscheide']} Entscheide\t{v['sachueberschrift']}")


def setze(a) -> None:
    if a.status not in STATUS:
        sys.exit(f"Unbekannter Status. Erlaubt: {', '.join(STATUS)}")
    q = lade_json(QUEUE)
    if a.artikel not in q["artikel"]:
        sys.exit(f"Unbekannter Artikel: {a.artikel}")
    q["artikel"][a.artikel]["status"] = a.status
    if a.notiz:
        q["artikel"][a.artikel]["notiz"] = a.notiz
    q["artikel"][a.artikel]["geaendert"] = dt.date.today().isoformat()
    schreibe_json(QUEUE, q)
    print(f"{a.artikel}: {a.status}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    n = sub.add_parser("naechster")
    n.add_argument("--anzahl", type=int, default=5)
    s = sub.add_parser("setze")
    s.add_argument("artikel")
    s.add_argument("status")
    s.add_argument("--notiz", default="")
    a = ap.parse_args()
    {"naechster": naechster, "setze": setze}.get(a.cmd, uebersicht)(a)


if __name__ == "__main__":
    main()
