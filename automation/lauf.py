"""Automatischer Lauf über die API (GitHub Actions, täglich). Bezahlt aus dem API-Guthaben
der Console; Claude Code mit API-Key wäre nicht abgedeckt, das Agent SDK schon.

Ablauf eines Laufs:
1. Fertige Batches abholen (Karteikarten, Fundstellenprüfungen), Register bauen.
2. Vorrat sichern: Hat die Warteschlange weniger als VORRAT Artikel «bereit», Entscheide für die
   nächsten Artikel laden und einen Karteikarten-Batch einreichen; bis WARTEN_MIN Minuten warten.
3. Schreiben, solange Zeit und Budget reichen: Artikel reservieren (pipeline/reservierung.py),
   Skill steuerkommentar-selbstaendig über das Agent SDK ausführen, Fundstellen per Batch prüfen,
   Befunde vom Agent beheben lassen, als «geprueft» freigeben und pushen (dann veröffentlicht die
   Website ihn).

Budget: höchstens MONATSBUDGET_USD je Kalendermonat (eigene Zählung in data/kosten.json) und
BUDGET_JE_ARTIKEL_USD je Artikel. Unabhängig davon stoppt die Console bei ihrem Ausgabenlimit oder
wenn das Guthaben verbraucht ist; der Lauf bricht dann ab und versucht es am nächsten Tag wieder.

Einstellungen über Umgebungsvariablen (im Workflow gesetzt): siehe EINSTELLUNGEN unten.
"""
from __future__ import annotations

import asyncio
import datetime as dt
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "pipeline"))
from config import ARBEIT, BATCHES, BATCH_PREISE, DATA, QUEUE, lade_json, schreibe_json  # noqa: E402
from reservierung import freigeben, git, reservieren  # noqa: E402

E = os.environ.get
EINSTELLUNGEN = {
    "MONATSBUDGET_USD": float(E("MONATSBUDGET_USD", "95")),
    "BUDGET_JE_ARTIKEL_USD": float(E("BUDGET_JE_ARTIKEL_USD", "15")),
    "BUDGET_KORREKTUR_USD": float(E("BUDGET_KORREKTUR_USD", "4")),
    "MODELL_SCHREIBEN": E("MODELL_SCHREIBEN", "claude-opus-5-5"),
    "MAX_ARTIKEL": int(E("MAX_ARTIKEL", "3")),            # je Lauf
    "VORRAT": int(E("VORRAT", "3")),                     # Artikel «bereit», die vorgehalten werden
    "NEUE_ARTIKEL_JE_LAUF": int(E("NEUE_ARTIKEL_JE_LAUF", "6")),
    "BATCH_BUDGET_USD": float(E("BATCH_BUDGET_USD", "10")),
    "WARTEN_MIN": int(E("WARTEN_MIN", "75")),            # Warten auf Batches
    "LAUFZEIT_MIN": int(E("LAUFZEIT_MIN", "300")),       # danach kein neuer Artikel mehr
    "WER": E("WER", "github-actions"),
}
START = time.time()
KOSTEN = DATA / "kosten.json"


def log(*a):
    print(f"[{dt.datetime.now().strftime('%H:%M:%S')}]", *a, flush=True)


def py(*args, pruefen=True) -> subprocess.CompletedProcess:
    r = subprocess.run([sys.executable, *args], cwd=ROOT, text=True, capture_output=True)
    if r.stdout.strip():
        log(r.stdout.strip()[-2000:])
    if r.returncode != 0:
        log("FEHLER", " ".join(args), r.stderr.strip()[-2000:])
        if pruefen:
            raise RuntimeError(r.stderr[-500:])
    return r


def minuten() -> float:
    return (time.time() - START) / 60


# ---------- Budget ----------

def monat() -> str:
    return dt.date.today().strftime("%Y-%m")


def batch_kosten_monat() -> float:
    summe = 0.0
    for p in BATCHES.glob(f"{dt.date.today().strftime('%Y%m')}*/batch.json"):
        m = lade_json(p, {})
        if "tokens_in" in m:
            pr = BATCH_PREISE.get(m.get("modell"), BATCH_PREISE["claude-sonnet-5-5"])
            summe += (m["tokens_in"] * pr["in"] + m["tokens_out"] * pr["out"]) / 1e6
        else:
            summe += m.get("kosten_geschaetzt_usd", 0) if m.get("status") in ("eingereicht", "abgeholt") else 0
    return summe


def agent_kosten_monat() -> float:
    return lade_json(KOSTEN, {}).get(monat(), {}).get("agent_usd", 0.0)


def kosten_buchen(usd: float, qid: str) -> None:
    k = lade_json(KOSTEN, {})
    m = k.setdefault(monat(), {"agent_usd": 0.0, "artikel": {}})
    m["agent_usd"] = round(m["agent_usd"] + usd, 4)
    m["artikel"][qid] = round(m["artikel"].get(qid, 0) + usd, 4)
    schreibe_json(KOSTEN, k)


def budget_rest() -> float:
    return EINSTELLUNGEN["MONATSBUDGET_USD"] - agent_kosten_monat() - batch_kosten_monat()


class GuthabenAufgebraucht(Exception):
    pass


# ---------- Git ----------

def sichern(nachricht: str, pfade: list[str]) -> None:
    """Committet die angegebenen Pfade (falls geändert) und pusht, mit Rebase bei Konflikt."""
    vorhanden = [p for p in pfade if (ROOT / p).exists()]
    if not vorhanden:
        return
    git("add", *vorhanden)
    if git("diff", "--cached", "--quiet", pruefen=False).returncode == 0:
        return
    git("commit", "-q", "-m", nachricht)
    for versuch in range(6):
        r = git("pull", "--rebase", "--autostash", "origin", "main", pruefen=False)
        if r.returncode != 0:
            git("rebase", "--abort", pruefen=False)
            log("Rebase-Konflikt beim Sichern:", r.stderr[-300:])
            raise RuntimeError("Rebase-Konflikt")
        if git("push", "origin", "HEAD:main", pruefen=False).returncode == 0:
            return
        time.sleep(3 + versuch * 3)
    raise RuntimeError("Push fehlgeschlagen")


DATENPFADE = ["data/karten", "data/zitate", "data/batches", "data/queue.json", "data/kosten.json", "arbeit"]


# ---------- Phasen ----------

def batches_abholen() -> None:
    meta = [lade_json(p, {}) for p in BATCHES.glob("*/batch.json")]
    if any(m.get("status") == "eingereicht" for m in meta):
        py("pipeline/karteikarten.py", "abholen", pruefen=False)
        py("pipeline/pruefung.py", "abholen", pruefen=False)
    py("pipeline/register.py", "--alle", pruefen=False)
    sichern("Batches abgeholt, Register nachgeführt", DATENPFADE)


def bereit_zahl() -> int:
    return sum(1 for v in lade_json(QUEUE)["artikel"].values() if v["status"] == "bereit")


def warten_auf_batches(art: str, max_min: int) -> bool:
    """Wartet, bis alle eingereichten Batches der Art fertig sind. True, wenn fertig."""
    import anthropic
    c = anthropic.Anthropic()
    ende = time.time() + max_min * 60
    while time.time() < ende:
        offen = 0
        for p in BATCHES.glob("*/batch.json"):
            m = lade_json(p, {})
            if m.get("status") == "eingereicht" and m.get("art") == art:
                if c.messages.batches.retrieve(m["batch_id"]).processing_status != "ended":
                    offen += 1
        if not offen:
            return True
        log(f"warte auf {offen} {art}-Batch(es) …")
        time.sleep(120)
    return False


def vorrat_sichern() -> None:
    if bereit_zahl() >= EINSTELLUNGEN["VORRAT"]:
        return
    if budget_rest() < EINSTELLUNGEN["BATCH_BUDGET_USD"]:
        log("Budget reicht nicht für neue Karteikarten.")
        return
    q = lade_json(QUEUE)["artikel"]
    if not any(v["status"] == "entscheide" for v in q.values()):
        py("pipeline/entscheide.py", "--naechste", str(EINSTELLUNGEN["NEUE_ARTIKEL_JE_LAUF"]), pruefen=False)
    r = py("pipeline/karteikarten.py", "vorbereiten", "--budget", str(EINSTELLUNGEN["BATCH_BUDGET_USD"]), pruefen=False)
    if "Nichts vorzubereiten" not in r.stdout:
        einreichen = py("pipeline/karteikarten.py", "einreichen", pruefen=False)
        if einreichen.returncode != 0 and "credit balance" in einreichen.stderr.lower():
            raise GuthabenAufgebraucht()
    sichern("Karteikarten-Batch eingereicht", DATENPFADE)
    if warten_auf_batches("karten", EINSTELLUNGEN["WARTEN_MIN"]):
        batches_abholen()


AUFTRAG = """Führe den Skill steuerkommentar-selbstaendig für Art. {nummer} {erlass} aus (Projekt: {root}).

Rahmen dieses Laufs:
- Unbeaufsichtigter Lauf über die API: keine Rückfragen; vernünftige Entscheide treffen und im Prüfbericht vermerken.
- Register, Problemkarte und Karteikarten liegen in arbeit/{erlass}/{slug}/01_Recherche/. Volltexte im Cache data/entscheide/.
- Lexplorer ist nicht verfügbar. Rechtsprechung: Open Case Law (MCP-Server «open-case-law») und Entscheidsuche
  (POST https://entscheidsuche.ch/_search.php, Volltexte unter https://entscheidsuche.ch/docs/…). Erlasse: data/inventar/ und Fedlex (WebFetch).
  Praxis und Lehre: Open Case Law (search_practice, search_scholarship) und Websuche.
- Schritt 8: Fussnoten mit BGE/BGer-Entscheiden prüft nach dir ein eigener Batch. Du prüfst mit einem Hilfsagenten nur die übrigen Fundstellen.
- Schreibe nach kommentare/{erlass}/{slug}.md; `python3 pipeline/kommentar.py kommentare/{erlass}/{slug}.md` muss ohne Befund durchlaufen.
- Kein `stand.py setze`, kein git, keine Word-Fassung. Status und Veröffentlichung übernimmt das Steuerskript.
- Achte auf Kosten: Volltexte nur, wo die Karteikarte nicht reicht; Hilfsagenten sparsam.
Ende: drei bis fünf Sätze Zusammenfassung."""

KORREKTUR = """Im Projekt {root} liegt die Kommentierung kommentare/{erlass}/{slug}.md und die Fundstellenliste {liste}.
Behebe jede Zeile mit Ergebnis «teilweise», «erwaegung_falsch» oder «nicht_belegt»: Erwägung korrigieren, Aussage an die Quelle anpassen
oder Aussage samt Fussnote streichen (Volltexte im Cache data/entscheide/ oder über Open Case Law). Nichts Neues hinzufügen.
Danach `python3 pipeline/kommentar.py kommentare/{erlass}/{slug}.md` ohne Befund. Halte die Korrekturen im Prüfbericht
arbeit/{erlass}/{slug}/Pruefbericht_{datum}.md fest. Kein git, kein stand.py. Ende: ein Satz, wie viele Fussnoten du geändert hast."""


async def agent(prompt: str, budget: float) -> tuple[float, str, str]:
    from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query
    optionen = ClaudeAgentOptions(
        cwd=str(ROOT),
        model=EINSTELLUNGEN["MODELL_SCHREIBEN"],
        setting_sources=["project"],
        skills=["steuerkommentar-selbstaendig"],
        permission_mode="bypassPermissions",
        max_budget_usd=budget,
        effort="high",
        mcp_servers={"open-case-law": {"type": "http", "url": "https://mcp.opencaselaw.ch/mcp"}},
    )
    kosten, ergebnis, art = 0.0, "", ""
    async for m in query(prompt=prompt, options=optionen):
        if isinstance(m, ResultMessage):
            kosten = m.total_cost_usd or 0.0
            ergebnis = (m.result or "")[-1500:]
            art = m.subtype
            if m.api_error_status in (400, 402) or "credit balance" in (ergebnis + str(m.errors or "")).lower():
                raise GuthabenAufgebraucht(ergebnis)
    return kosten, ergebnis, art


def kommentar_ok(pfad: Path) -> bool:
    return pfad.exists() and py("pipeline/kommentar.py", str(pfad.relative_to(ROOT)), pruefen=False).returncode == 0


def artikel_schreiben(qid: str) -> None:
    erlass, slug = qid.split("/")
    nummer = lade_json(QUEUE)["artikel"][qid]["nummer"]
    datei = ROOT / "kommentare" / erlass / f"{slug}.md"
    pfade = [str(datei.relative_to(ROOT)), f"arbeit/{erlass}/{slug}", "data/kosten.json"]
    log(f"Schreibe {qid} (Budget {EINSTELLUNGEN['BUDGET_JE_ARTIKEL_USD']} USD) …")
    try:
        kosten, text, art = asyncio.run(agent(
            AUFTRAG.format(nummer=nummer, erlass=erlass, slug=slug, root=ROOT), EINSTELLUNGEN["BUDGET_JE_ARTIKEL_USD"]))
    except GuthabenAufgebraucht:
        freigeben(qid, "bereit", "Abbruch: API-Guthaben aufgebraucht", [], EINSTELLUNGEN["WER"])
        raise
    except Exception as fehler:  # noqa: BLE001
        if "credit" in str(fehler).lower():
            freigeben(qid, "bereit", "Abbruch: API-Guthaben aufgebraucht", [], EINSTELLUNGEN["WER"])
            raise GuthabenAufgebraucht(str(fehler))
        freigeben(qid, "bereit", f"Abbruch: {str(fehler)[:120]}", [], EINSTELLUNGEN["WER"])
        log(f"{qid}: Fehler im Agent-Lauf: {fehler}")
        return
    kosten_buchen(kosten, qid)
    log(f"{qid}: Agent fertig ({art}), {kosten:.2f} USD. {text[-400:]}")
    if not kommentar_ok(datei):
        versuche = lade_json(QUEUE)["artikel"][qid].get("versuche", 0) + 1
        status = "fehler" if versuche >= 2 else "bereit"
        freigeben(qid, status, f"Lauf {versuche} ohne gültige Kommentierung ({art}, {kosten:.2f} USD)", pfade,
                  EINSTELLUNGEN["WER"], {"versuche": versuche})
        return
    # Zwischenstand sichern, Artikel bleibt reserviert
    sichern(f"{qid}: Entwurf ({kosten:.2f} USD)", pfade)
    # Fundstellenprüfung per Batch
    py("pipeline/pruefung.py", "vorbereiten", str(datei.relative_to(ROOT)), pruefen=False)
    py("pipeline/karteikarten.py", "einreichen", pruefen=False)
    if not warten_auf_batches("pruefung", 45):
        freigeben(qid, "geschrieben", "Fundstellenprüfung (Batch) noch offen", pfade + ["data/batches"], EINSTELLUNGEN["WER"])
        return
    py("pipeline/pruefung.py", "abholen", pruefen=False)
    listen = sorted((ARBEIT / erlass / slug).glob("Fundstellenliste_*.md"))
    if listen:
        k2, text2, _ = asyncio.run(agent(KORREKTUR.format(
            root=ROOT, erlass=erlass, slug=slug, liste=listen[-1].relative_to(ROOT), datum=dt.date.today().isoformat()),
            EINSTELLUNGEN["BUDGET_KORREKTUR_USD"]))
        kosten_buchen(k2, qid)
        log(f"{qid}: Korrektur {k2:.2f} USD. {text2[-300:]}")
    if kommentar_ok(datei):
        freigeben(qid, "geprueft", f"automatisch ({EINSTELLUNGEN['WER']}, {dt.date.today().isoformat()})",
                  pfade + ["data/batches"], EINSTELLUNGEN["WER"])
        log(f"{qid}: geprüft und freigegeben → wird veröffentlicht")
    else:
        freigeben(qid, "geschrieben", "Korrektur ohne gültiges Ergebnis", pfade + ["data/batches"], EINSTELLUNGEN["WER"])


def offene_pruefungen_abschliessen() -> None:
    """Artikel im Status «geschrieben», deren Prüf-Batch inzwischen fertig ist, korrigieren und freigeben."""
    q = lade_json(QUEUE)["artikel"]
    for qid, v in q.items():
        if v["status"] != "geschrieben" or budget_rest() < EINSTELLUNGEN["BUDGET_KORREKTUR_USD"]:
            continue
        erlass, slug = qid.split("/")
        listen = sorted((ARBEIT / erlass / slug).glob("Fundstellenliste_*.md"))
        if not listen:
            continue
        if reservieren(EINSTELLUNGEN["WER"], ["geschrieben"]) != qid:
            continue
        datei = ROOT / "kommentare" / erlass / f"{slug}.md"
        k2, _, _ = asyncio.run(agent(KORREKTUR.format(root=ROOT, erlass=erlass, slug=slug, liste=listen[-1].relative_to(ROOT),
                                                    datum=dt.date.today().isoformat()), EINSTELLUNGEN["BUDGET_KORREKTUR_USD"]))
        kosten_buchen(k2, qid)
        pfade = [str(datei.relative_to(ROOT)), f"arbeit/{erlass}/{slug}", "data/kosten.json"]
        freigeben(qid, "geprueft" if kommentar_ok(datei) else "geschrieben", "Prüfung nachträglich abgeschlossen", pfade,
                  EINSTELLUNGEN["WER"])


def main() -> None:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        log("ANTHROPIC_API_KEY fehlt (Repository-Secret). Lauf beendet.")
        return
    log("Einstellungen:", json.dumps(EINSTELLUNGEN))
    log(f"Budget diesen Monat: {budget_rest():.2f} USD übrig")
    try:
        batches_abholen()
        offene_pruefungen_abschliessen()
        vorrat_sichern()
        geschrieben = 0
        while geschrieben < EINSTELLUNGEN["MAX_ARTIKEL"]:
            if minuten() > EINSTELLUNGEN["LAUFZEIT_MIN"]:
                log("Laufzeit erreicht.")
                break
            if budget_rest() < EINSTELLUNGEN["BUDGET_JE_ARTIKEL_USD"]:
                log(f"Monatsbudget erreicht ({budget_rest():.2f} USD übrig). Nächster Versuch im neuen Monat.")
                break
            qid = reservieren(EINSTELLUNGEN["WER"], ["bereit"])
            if not qid:
                log("Kein Artikel «bereit».")
                break
            artikel_schreiben(qid)
            geschrieben += 1
    except GuthabenAufgebraucht:
        log("API-Guthaben aufgebraucht oder Ausgabenlimit erreicht. Der nächste Lauf versucht es erneut.")
    finally:
        try:
            sichern("Lauf beendet: Kosten und Daten", DATENPFADE)
        except Exception as e:  # noqa: BLE001
            log("Sichern am Ende fehlgeschlagen:", e)
    log(f"Fertig nach {minuten():.0f} Minuten. Budget übrig: {budget_rest():.2f} USD")


if __name__ == "__main__":
    main()
