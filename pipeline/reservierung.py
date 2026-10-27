"""Reservierung: verhindert, dass zwei Läufe (GitHub Actions, Claude-Cloud, Laptop) denselben
Artikel gleichzeitig bearbeiten.

Prinzip: Wer einen Artikel bearbeiten will, setzt dessen Status in data/queue.json auf
«in_arbeit», committet das und pusht. Git nimmt von zwei gleichzeitigen Pushes nur einen an;
der andere wird abgelehnt, holt den neuen Stand und nimmt den nächsten freien Artikel.
Eine Reservierung, die älter als RESERVIERUNG_STUNDEN ist, gilt als verwaist (Lauf abgestürzt)
und darf neu vergeben werden.

    python3 pipeline/reservierung.py reservieren --wer github-actions [--status bereit] [--status offen] [--erlass VStG]
        → gibt die reservierte Artikel-ID aus (z.B. DBG/art-26) oder nichts
    python3 pipeline/reservierung.py freigeben DBG/art-26 zurueck   # Status wie vor der Reservierung
    python3 pipeline/reservierung.py freigeben DBG/art-26 geprueft [--notiz "…"] [--dateien kommentare/DBG/art-26.md arbeit/DBG/art-26]
    python3 pipeline/reservierung.py liste            # laufende Reservierungen

Voraussetzung: sauberes Git-Arbeitsverzeichnis mit Push-Recht auf origin/main.
"""
from __future__ import annotations

import argparse
import datetime as dt
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import QUEUE, ROOT, art_sortkey, lade_json, schreibe_json  # noqa: E402

RESERVIERUNG_STUNDEN = 12
VERSUCHE = 8
ZWEIG = "main"


def git(*args, pruefen=True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True, check=pruefen)


def jetzt() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def verwaist(eintrag: dict) -> bool:
    seit = eintrag.get("seit")
    if not seit:
        return True
    try:
        return jetzt() - dt.datetime.fromisoformat(seit) > dt.timedelta(hours=RESERVIERUNG_STUNDEN)
    except ValueError:
        return True


def _sichern_kopie(dateien: list[str]) -> Path:
    import shutil
    import tempfile
    tmp = Path(tempfile.mkdtemp(prefix="res-"))
    for d in dateien:
        quelle = ROOT / d
        if quelle.is_dir():
            shutil.copytree(quelle, tmp / d, dirs_exist_ok=True)
        elif quelle.exists():
            (tmp / d).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(quelle, tmp / d)
    return tmp


def _zurueckkopieren(tmp: Path) -> None:
    import shutil
    for quelle in tmp.rglob("*"):
        if quelle.is_file():
            ziel = ROOT / quelle.relative_to(tmp)
            ziel.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(quelle, ziel)


def aendern_und_pushen(aenderung, nachricht: str, dateien: list[str] | None = None):
    """Holt den neuesten Stand von origin/main, wendet `aenderung(queue)` an und pusht – zusammen mit
    `dateien` (eigene Dateien dieses Laufs, z.B. die Kommentierung). Bei Konflikt: neu versuchen.
    `aenderung` gibt einen Wert zurück; None bedeutet «nichts zu tun» (kein Commit).

    Robust für parallele Läufe: Die eigenen Dateien werden vor dem Abgleich kopiert und danach
    zurückgelegt; der Arbeitsbaum wird hart auf origin/main gesetzt. Andere lokale Änderungen
    gehen dabei verloren, deshalb immer alle eigenen Dateien in `dateien` angeben."""
    dateien = [d for d in (dateien or []) if (ROOT / d).exists()]
    tmp = _sichern_kopie(dateien)
    queue_pfad = str(QUEUE.relative_to(ROOT))
    for versuch in range(VERSUCHE):
        git("fetch", "-q", "origin", ZWEIG)
        git("reset", "-q", "--hard", f"origin/{ZWEIG}")
        _zurueckkopieren(tmp)
        queue = lade_json(QUEUE)
        ergebnis = aenderung(queue)
        if ergebnis is None:
            return None
        schreibe_json(QUEUE, queue)
        git("add", queue_pfad, *dateien)
        if git("diff", "--cached", "--quiet", pruefen=False).returncode == 0:
            return ergebnis
        git("commit", "-q", "-m", nachricht)
        if git("push", "-q", "origin", f"HEAD:{ZWEIG}", pruefen=False).returncode == 0:
            return ergebnis
        time.sleep(2 + versuch * 3)   # jemand war schneller: neuer Stand, neuer Versuch
    raise RuntimeError(f"Push nach {VERSUCHE} Versuchen nicht möglich: {nachricht}")


def queue_uebernehmen(felder_je_artikel: dict[str, dict], nachricht: str, dateien: list[str],
                      geschuetzt=("in_arbeit", "geschrieben", "geprueft", "veroeffentlicht", "fehler")) -> None:
    """Überträgt Feldänderungen an Artikeln (z.B. aus register.py) auf den neuesten Stand, ohne die
    Arbeit paralleler Läufe zu überschreiben: Der Status geschützter Artikel bleibt unverändert."""
    def aenderung(queue):
        for qid, felder in felder_je_artikel.items():
            v = queue["artikel"].get(qid)
            if v is None:
                continue
            for k, w in felder.items():
                if k == "status" and v["status"] in geschuetzt:
                    continue
                v[k] = w
        return True
    aendern_und_pushen(aenderung, nachricht, dateien)


def lokale_queue_aenderungen() -> dict[str, dict]:
    """Unterschiede der lokalen data/queue.json zur Fassung in HEAD, je Artikel und Feld."""
    import json
    r = git("show", f"HEAD:{QUEUE.relative_to(ROOT)}", pruefen=False)
    alt = json.loads(r.stdout)["artikel"] if r.returncode == 0 else {}
    neu = lade_json(QUEUE)["artikel"]
    diff = {}
    for qid, v in neu.items():
        a = alt.get(qid, {})
        d = {k: w for k, w in v.items() if a.get(k) != w}
        if d:
            diff[qid] = d
    return diff


def reservieren(wer: str, status_reihenfolge: list[str], bedingung=None) -> str | None:
    def aenderung(queue):
        artikel = queue["artikel"]
        kandidaten = []
        for rang, st in enumerate(status_reihenfolge):
            for qid, v in artikel.items():
                if v["status"] == st and (bedingung is None or bedingung(qid, v)):
                    kandidaten.append((rang, -(v.get("prioritaet") or 0), v["erlass"], art_sortkey(v["nummer"]), qid))
        # verwaiste Reservierungen zuerst wieder freigeben
        for qid, v in artikel.items():
            if v["status"] == "in_arbeit" and verwaist(v):
                v["status"] = v.get("status_vorher") or "offen"
                v["notiz"] = f"Reservierung von {v.get('bearbeiter')} verfallen"
                if v["status"] in status_reihenfolge:
                    kandidaten.append((status_reihenfolge.index(v["status"]), -(v.get("prioritaet") or 0), v["erlass"], art_sortkey(v["nummer"]), qid))
        if not kandidaten:
            return None
        kandidaten.sort()
        qid = kandidaten[0][-1]
        v = artikel[qid]
        v["status_vorher"] = v["status"]
        v["status"] = "in_arbeit"
        v["bearbeiter"] = wer
        v["seit"] = jetzt().isoformat(timespec="seconds")
        return qid

    return aendern_und_pushen(aenderung, f"Reserviert für {wer}")


def freigeben(qid: str, status: str, notiz: str = "", dateien: list[str] | None = None, wer: str = "",
              felder: dict | None = None) -> None:
    def aenderung(queue):
        v = queue["artikel"][qid]
        if v["status"] == "in_arbeit" and wer and v.get("bearbeiter") not in (wer, None):
            raise RuntimeError(f"{qid} ist von {v.get('bearbeiter')} reserviert, nicht von {wer}")
        v["status"] = (v.get("status_vorher") or "offen") if status == "zurueck" else status
        v["notiz"] = notiz
        v.update(felder or {})
        v["geaendert"] = jetzt().date().isoformat()
        v.pop("seit", None)
        if status != "in_arbeit":
            v.pop("bearbeiter", None)
        return qid

    aendern_und_pushen(aenderung, f"{qid}: {status}" + (f" ({notiz})" if notiz else ""), dateien)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("reservieren")
    r.add_argument("--wer", required=True)
    r.add_argument("--status", action="append", help="zulässige Ausgangsstatus in Vorzugsreihenfolge (Standard: bereit)")
    r.add_argument("--erlass", action="append", help="nur Artikel dieser Erlasse (z.B. --erlass VStG --erlass StG)")
    f = sub.add_parser("freigeben")
    f.add_argument("artikel")
    f.add_argument("status")
    f.add_argument("--notiz", default="")
    f.add_argument("--wer", default="")
    f.add_argument("--dateien", nargs="*", default=[])
    sub.add_parser("liste")
    a = ap.parse_args()
    if a.cmd == "reservieren":
        erlasse = {e.lower() for e in (a.erlass or [])}
        bedingung = (lambda _q, v: v["erlass"].lower() in erlasse) if erlasse else None
        qid = reservieren(a.wer, a.status or ["bereit"], bedingung)
        if qid:
            print(qid)
    elif a.cmd == "freigeben":
        freigeben(a.artikel, a.status, a.notiz, a.dateien, a.wer)
        print(f"{a.artikel}: {a.status}")
    else:
        for qid, v in lade_json(QUEUE)["artikel"].items():
            if v["status"] == "in_arbeit":
                print(f"{qid}\t{v.get('bearbeiter')}\tseit {v.get('seit')}\t{'verwaist' if verwaist(v) else ''}")


if __name__ == "__main__":
    main()
