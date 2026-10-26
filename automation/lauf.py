"""Automatischer Lauf über die API (GitHub Actions, stündlich gestartet, nie zwei Läufe gleichzeitig).
Bezahlt aus dem API-Guthaben der Console; Claude Code mit API-Key wäre nicht abgedeckt, das Agent SDK schon.

Ein Lauf:
1. Fertige Batches abholen: Karteikarten → Register; Fundstellenprüfungen → Korrektur durch den Agent
   und Freigabe als «geprueft» (dann veröffentlicht die Website den Artikel).
2. Vorrat sichern: Sind weniger als VORRAT Artikel «bereit», Entscheide laden und einen
   Karteikarten-Batch einreichen (Sonnet, Batch-Preis); bis WARTEN_MIN Minuten auf das Ergebnis warten.
3. Schreiben, solange Tages- und Monatsbudget reichen: Artikel reservieren, Skill
   steuerkommentar-selbstaendig über das Agent SDK (Opus 5.5, hohe Stufe), Fundstellen-Batch einreichen,
   Artikel als «geschrieben» freigeben. Die Prüfung schliesst der nächste Schritt 1 ab.

Budget: TAGESBUDGET_USD je Kalendertag, MONATSBUDGET_USD je Monat (Zählung in data/kosten/).
Unabhängig davon stoppt die Console bei ihrem Ausgabenlimit oder wenn das Guthaben aufgebraucht ist.
API-Preise hängen nicht von der Tageszeit ab.
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
from reservierung import freigeben, lokale_queue_aenderungen, queue_uebernehmen, reservieren  # noqa: E402

E = os.environ.get
EINSTELLUNGEN = {
    "TAGESBUDGET_USD": float(E("TAGESBUDGET_USD", "30")),
    "MONATSBUDGET_USD": float(E("MONATSBUDGET_USD", "100")),
    "BUDGET_JE_ARTIKEL_USD": float(E("BUDGET_JE_ARTIKEL_USD", "15")),
    "BUDGET_KORREKTUR_USD": float(E("BUDGET_KORREKTUR_USD", "4")),
    "MIN_REST_USD": float(E("MIN_REST_USD", "5")),          # darunter kein neuer Artikel mehr an diesem Tag
    "MODELL_SCHREIBEN": E("MODELL_SCHREIBEN", "claude-opus-5-5"),
    "EFFORT": E("EFFORT", "high"),
    "VORRAT": int(E("VORRAT", "3")),
    "NEUE_ARTIKEL_JE_LAUF": int(E("NEUE_ARTIKEL_JE_LAUF", "6")),
    "BATCH_BUDGET_USD": float(E("BATCH_BUDGET_USD", "8")),
    "WARTEN_MIN": int(E("WARTEN_MIN", "60")),
    "LAUFZEIT_MIN": int(E("LAUFZEIT_MIN", "280")),           # danach kein neuer Artikel mehr in diesem Lauf
    "WER": E("WER", "github-actions"),
}
START = time.time()
KOSTEN_DIR = DATA / "kosten"
LAUF_ID = E("GITHUB_RUN_ID", dt.datetime.now().strftime("%H%M%S"))


def log(*a):
    print(f"[{dt.datetime.now().strftime('%H:%M:%S')}]", *a, flush=True)


def py(*args, pruefen=False) -> subprocess.CompletedProcess:
    r = subprocess.run([sys.executable, *args], cwd=ROOT, text=True, capture_output=True)
    if r.stdout.strip():
        log(r.stdout.strip()[-1500:])
    if r.returncode != 0:
        log("FEHLER", " ".join(args), r.stderr.strip()[-1500:])
        if pruefen:
            raise RuntimeError(r.stderr[-500:])
    return r


def minuten() -> float:
    return (time.time() - START) / 60


class GuthabenAufgebraucht(Exception):
    pass


# ---------- Kosten und Budget ----------

def heute() -> str:
    return dt.date.today().isoformat()


def kosten_datei() -> Path:
    return KOSTEN_DIR / heute() / f"{EINSTELLUNGEN['WER']}-{LAUF_ID}.json"


def kosten_buchen(usd: float, qid: str, art: str) -> None:
    p = kosten_datei()
    k = lade_json(p, {"agent_usd": 0.0, "posten": []})
    k["agent_usd"] = round(k["agent_usd"] + usd, 4)
    k["posten"].append({"artikel": qid, "art": art, "usd": round(usd, 4), "zeit": dt.datetime.now().isoformat(timespec="seconds")})
    schreibe_json(p, k)


def agent_kosten(praefix: str) -> float:
    return sum(lade_json(p, {}).get("agent_usd", 0.0) for p in KOSTEN_DIR.glob(f"{praefix}*/*.json"))


def batch_kosten(praefix: str) -> float:
    summe = 0.0
    for p in BATCHES.glob(f"{praefix.replace('-', '')}*/batch.json"):
        m = lade_json(p, {})
        if "tokens_in" in m:
            pr = BATCH_PREISE.get(m.get("modell"), BATCH_PREISE["claude-sonnet-5-5"])
            summe += (m["tokens_in"] * pr["in"] + m["tokens_out"] * pr["out"]) / 1e6
        elif m.get("status") == "eingereicht":
            summe += m.get("kosten_geschaetzt_usd", 0)
    return summe


def tagesrest() -> float:
    d = heute()
    return EINSTELLUNGEN["TAGESBUDGET_USD"] - agent_kosten(d) - batch_kosten(d)


def monatsrest() -> float:
    m = heute()[:7]
    return EINSTELLUNGEN["MONATSBUDGET_USD"] - agent_kosten(m) - batch_kosten(m)


def rest() -> float:
    return min(tagesrest(), monatsrest())


# ---------- Agent ----------

AUFTRAG = """Führe den Skill steuerkommentar-selbstaendig für Art. {nummer} {erlass} aus (Projekt: {root}).

Rahmen dieses Laufs:
- Unbeaufsichtigter Lauf über die API: keine Rückfragen; vernünftige Entscheide treffen und im Prüfbericht vermerken.
- Register, Problemkarte und Karteikarten liegen in arbeit/{erlass}/{slug}/01_Recherche/. Volltexte im Cache data/entscheide/.
- Lexplorer ist nicht verfügbar. Rechtsprechung: Entscheidsuche (POST https://entscheidsuche.ch/_search.php, Volltexte unter
  https://entscheidsuche.ch/docs/…) und Open Case Law (MCP-Server «open-case-law»). Erlasse: data/inventar/ und Fedlex (WebFetch).
  Praxis und Lehre: Open Case Law (search_practice, search_scholarship) und Websuche.
- Schritt 8: Fussnoten mit BGE/BGer-Entscheiden prüft nach dir ein eigener Batch. Du prüfst mit einem Hilfsagenten nur die übrigen Fundstellen.
- Schreibe nach kommentare/{erlass}/{slug}.md; `python3 pipeline/kommentar.py kommentare/{erlass}/{slug}.md` muss ohne Befund durchlaufen.
- Kein `stand.py setze`, kein git, keine Word-Fassung. Status und Veröffentlichung übernimmt das Steuerskript.
- Achte auf Kosten: Volltexte nur, wo die Karteikarte nicht reicht; Hilfsagenten sparsam.
Ende: drei bis fünf Sätze Zusammenfassung."""

KORREKTUR = """Im Projekt {root} liegt die Kommentierung kommentare/{erlass}/{slug}.md und die Fundstellenliste {liste}.
Behebe jede Zeile mit Ergebnis «teilweise», «erwaegung_falsch» oder «nicht_belegt»: Erwägung korrigieren, Aussage an die Quelle anpassen
oder Aussage samt Fussnote streichen (Volltexte im Cache data/entscheide/, über Entscheidsuche oder Open Case Law). Nichts Neues hinzufügen.
Danach `python3 pipeline/kommentar.py kommentare/{erlass}/{slug}.md` ohne Befund. Halte die Korrekturen im Prüfbericht
arbeit/{erlass}/{slug}/Pruefbericht_{datum}.md fest. Kein git, kein stand.py. Ende: ein Satz, wie viele Fussnoten du geändert hast."""


async def _agent(prompt: str, budget: float) -> tuple[float, str, str]:
    from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query
    optionen = ClaudeAgentOptions(
        cwd=str(ROOT),
        model=EINSTELLUNGEN["MODELL_SCHREIBEN"],
        effort=EINSTELLUNGEN["EFFORT"],
        setting_sources=["project"],
        skills=["steuerkommentar-selbstaendig"],
        permission_mode="bypassPermissions",
        max_budget_usd=budget,
        mcp_servers={"open-case-law": {"type": "http", "url": "https://mcp.opencaselaw.ch/mcp"}},
    )
    kosten, ergebnis, art = 0.0, "", ""
    async for m in query(prompt=prompt, options=optionen):
        if isinstance(m, ResultMessage):
            kosten = m.total_cost_usd or 0.0
            ergebnis = (m.result or "")[-1500:]
            art = m.subtype
            if "credit balance" in (ergebnis + str(m.errors or "")).lower():
                raise GuthabenAufgebraucht(ergebnis)
    return kosten, ergebnis, art


def agent(prompt: str, budget: float, qid: str, art: str) -> tuple[float, str, str]:
    try:
        kosten, text, typ = asyncio.run(_agent(prompt, budget))
    except GuthabenAufgebraucht:
        raise
    except Exception as fehler:  # noqa: BLE001
        if "credit" in str(fehler).lower() or "billing" in str(fehler).lower():
            raise GuthabenAufgebraucht(str(fehler))
        raise
    kosten_buchen(kosten, qid, art)
    log(f"{qid}: {art} fertig ({typ}), {kosten:.2f} USD. {text[-300:]}")
    return kosten, text, typ


def kommentar_ok(pfad: Path) -> bool:
    return pfad.exists() and py("pipeline/kommentar.py", str(pfad.relative_to(ROOT))).returncode == 0


def pfade_artikel(erlass: str, slug: str) -> list[str]:
    return [f"kommentare/{erlass}/{slug}.md", f"arbeit/{erlass}/{slug}", str(kosten_datei().relative_to(ROOT))]


# ---------- Schritte ----------

def offene_batches() -> dict[str, dict]:
    return {p.parent.name: lade_json(p, {}) for p in BATCHES.glob("*/batch.json")
            if lade_json(p, {}).get("status") == "eingereicht"}


def beendete_batches(namen: list[str]) -> set[str]:
    if not namen:
        return set()
    import anthropic
    c = anthropic.Anthropic()
    fertig = set()
    for n in namen:
        m = lade_json(BATCHES / n / "batch.json", {})
        try:
            if c.messages.batches.retrieve(m["batch_id"]).processing_status == "ended":
                fertig.add(n)
        except Exception as fehler:  # noqa: BLE001
            log(f"Batch {n}: Status nicht abrufbar ({fehler})")
    return fertig


def karteikarten_abholen() -> None:
    karten = [n for n, m in offene_batches().items() if m.get("art") == "karten"]
    if not beendete_batches(karten):
        return
    py("pipeline/karteikarten.py", "abholen")
    py("pipeline/register.py", "--alle")
    aenderungen = lokale_queue_aenderungen()
    queue_uebernehmen(aenderungen, "Karteikarten abgeholt, Register nachgeführt",
                      ["data/karten", "data/zitate", "data/batches", "arbeit"])


def pruefungen_abschliessen() -> None:
    """Artikel «geschrieben», deren Fundstellen-Batch fertig ist: abholen, korrigieren, freigeben."""
    q = lade_json(QUEUE)["artikel"]
    kandidaten = {v.get("pruefung_batch") for v in q.values() if v["status"] == "geschrieben" and v.get("pruefung_batch")}
    fertig = beendete_batches(sorted(k for k in kandidaten if k))
    while fertig and rest() >= EINSTELLUNGEN["BUDGET_KORREKTUR_USD"]:
        qid = reservieren(EINSTELLUNGEN["WER"], ["geschrieben"], lambda _q, v: v.get("pruefung_batch") in fertig)
        if not qid:
            return
        erlass, slug = qid.split("/")
        batch = lade_json(QUEUE)["artikel"][qid]["pruefung_batch"]
        fertig.discard(batch)
        py("pipeline/pruefung.py", "abholen", "--nur", batch)
        listen = sorted((ARBEIT / erlass / slug).glob("Fundstellenliste_*.md"))
        datei = ROOT / "kommentare" / erlass / f"{slug}.md"
        pfade = pfade_artikel(erlass, slug) + [f"data/batches/{batch}"]
        try:
            if listen:
                agent(KORREKTUR.format(root=ROOT, erlass=erlass, slug=slug, liste=listen[-1].relative_to(ROOT),
                                       datum=heute()), min(EINSTELLUNGEN["BUDGET_KORREKTUR_USD"], rest()), qid, "korrektur")
        except GuthabenAufgebraucht:
            freigeben(qid, "geschrieben", "Korrektur abgebrochen: Guthaben", pfade, EINSTELLUNGEN["WER"])
            raise
        except Exception as fehler:  # noqa: BLE001
            freigeben(qid, "geschrieben", f"Korrektur-Fehler: {str(fehler)[:100]}", pfade, EINSTELLUNGEN["WER"])
            continue
        if kommentar_ok(datei):
            freigeben(qid, "geprueft", f"automatisch geprüft ({heute()})", pfade, EINSTELLUNGEN["WER"],
                      {"pruefung_batch": None})
            log(f"{qid}: geprüft und freigegeben → wird veröffentlicht")
        else:
            freigeben(qid, "fehler", "Nach Korrektur Format- oder Neutralitätsbefunde", pfade, EINSTELLUNGEN["WER"])


def vorrat_sichern() -> None:
    q = lade_json(QUEUE)["artikel"]
    if sum(1 for v in q.values() if v["status"] == "bereit") >= EINSTELLUNGEN["VORRAT"]:
        return
    if any(m.get("art") == "karten" for m in offene_batches().values()):
        return  # ein Batch läuft schon
    if rest() < EINSTELLUNGEN["BATCH_BUDGET_USD"]:
        log("Budget reicht heute nicht für neue Karteikarten.")
        return
    if not any(v["status"] in ("entscheide", "karten") for v in q.values()):
        py("pipeline/entscheide.py", "--naechste", str(EINSTELLUNGEN["NEUE_ARTIKEL_JE_LAUF"]))
    r = py("pipeline/karteikarten.py", "vorbereiten", "--budget", str(EINSTELLUNGEN["BATCH_BUDGET_USD"]))
    if "Batch " in r.stdout:
        name = r.stdout.split("Batch ", 1)[1].split(":", 1)[0].strip()
        e = py("pipeline/karteikarten.py", "einreichen", "--nur", name)
        if e.returncode != 0 and "credit" in e.stderr.lower():
            raise GuthabenAufgebraucht()
    queue_uebernehmen(lokale_queue_aenderungen(), "Entscheide geladen, Karteikarten-Batch eingereicht",
                      ["data/zitate", "data/batches"])
    ende = time.time() + EINSTELLUNGEN["WARTEN_MIN"] * 60
    while time.time() < ende:
        karten = [n for n, m in offene_batches().items() if m.get("art") == "karten"]
        if not karten or beendete_batches(karten) == set(karten):
            karteikarten_abholen()
            return
        log("warte auf Karteikarten-Batch …")
        time.sleep(120)


def artikel_schreiben(qid: str) -> None:
    erlass, slug = qid.split("/")
    nummer = lade_json(QUEUE)["artikel"][qid]["nummer"]
    datei = ROOT / "kommentare" / erlass / f"{slug}.md"
    budget = min(EINSTELLUNGEN["BUDGET_JE_ARTIKEL_USD"], rest())
    log(f"Schreibe {qid} (Budget {budget:.2f} USD, {EINSTELLUNGEN['MODELL_SCHREIBEN']}, Effort {EINSTELLUNGEN['EFFORT']}) …")
    pfade = pfade_artikel(erlass, slug)
    try:
        kosten, _, typ = agent(AUFTRAG.format(nummer=nummer, erlass=erlass, slug=slug, root=ROOT), budget, qid, "schreiben")
    except GuthabenAufgebraucht:
        freigeben(qid, "bereit", "Abbruch: API-Guthaben aufgebraucht", pfade, EINSTELLUNGEN["WER"])
        raise
    except Exception as fehler:  # noqa: BLE001
        freigeben(qid, "bereit", f"Abbruch: {str(fehler)[:120]}", pfade, EINSTELLUNGEN["WER"])
        log(f"{qid}: Fehler im Agent-Lauf: {fehler}")
        return
    if not kommentar_ok(datei):
        versuche = lade_json(QUEUE)["artikel"][qid].get("versuche", 0) + 1
        freigeben(qid, "fehler" if versuche >= 2 else "bereit",
                  f"Lauf {versuche} ohne gültige Kommentierung ({typ}, {kosten:.2f} USD)", pfade,
                  EINSTELLUNGEN["WER"], {"versuche": versuche})
        return
    # Fundstellen per Batch prüfen lassen; die Korrektur folgt im nächsten Schritt 1
    r = py("pipeline/pruefung.py", "vorbereiten", str(datei.relative_to(ROOT)), "--name", LAUF_ID)
    name = next((z.split("=", 1)[1] for z in r.stdout.splitlines() if z.startswith("BATCH=")), None)
    meta = lade_json(BATCHES / name / "batch.json", {}) if name else {}
    if name and meta.get("anfragen", 0) > 0:
        e = py("pipeline/karteikarten.py", "einreichen", "--nur", name)
        if e.returncode != 0:
            freigeben(qid, "geschrieben", "Prüf-Batch nicht eingereicht", pfade + [f"data/batches/{name}"], EINSTELLUNGEN["WER"])
            if "credit" in e.stderr.lower():
                raise GuthabenAufgebraucht()
            return
        freigeben(qid, "geschrieben", f"Entwurf ({kosten:.2f} USD), Fundstellenprüfung läuft",
                  pfade + [f"data/batches/{name}"], EINSTELLUNGEN["WER"], {"pruefung_batch": name})
    else:
        freigeben(qid, "geprueft", f"automatisch ({heute()}); keine BGer-Fundstellen für den Batch", pfade,
                  EINSTELLUNGEN["WER"])


def main() -> None:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        log("ANTHROPIC_API_KEY fehlt (Repository-Secret). Lauf beendet.")
        return
    log("Einstellungen:", json.dumps(EINSTELLUNGEN))
    log(f"Heute übrig: {tagesrest():.2f} USD, diesen Monat: {monatsrest():.2f} USD")
    py("pipeline/karteikarten.py", "fehler")   # Fehlermeldungen früherer Batches ins Protokoll
    try:
        karteikarten_abholen()
        pruefungen_abschliessen()
        vorrat_sichern()
        while True:
            pruefungen_abschliessen()
            if minuten() > EINSTELLUNGEN["LAUFZEIT_MIN"]:
                log("Laufzeit erreicht; der nächste stündliche Lauf macht weiter.")
                break
            if rest() < EINSTELLUNGEN["MIN_REST_USD"]:
                log(f"Tages- oder Monatsbudget erreicht (heute {tagesrest():.2f}, Monat {monatsrest():.2f} USD übrig).")
                break
            qid = reservieren(EINSTELLUNGEN["WER"], ["bereit"])
            if not qid:
                log("Kein Artikel «bereit»; der nächste Lauf bereitet neue vor.")
                break
            artikel_schreiben(qid)
    except GuthabenAufgebraucht:
        log("API-Guthaben aufgebraucht oder Ausgabenlimit der Console erreicht. Nächster Versuch im nächsten Lauf.")
    log(f"Fertig nach {minuten():.0f} Minuten. Heute übrig: {tagesrest():.2f} USD, Monat: {monatsrest():.2f} USD")


if __name__ == "__main__":
    main()
