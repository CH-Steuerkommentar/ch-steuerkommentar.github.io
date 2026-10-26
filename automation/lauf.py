"""Automatischer Lauf über die API (GitHub Actions, stündlich gestartet, nie zwei Läufe gleichzeitig).
Bezahlt aus dem API-Guthaben der Console; Claude Code mit API-Key wäre nicht abgedeckt, das Agent SDK schon.

Ein Lauf kommentiert Artikel um Artikel, solange Tages- und Monatsbudget und die Laufzeit reichen:
nächsten Artikel reservieren, Bundesgerichtsentscheide in den Cache laden (Open Case Law, ohne API-Kosten),
Skill steuerkommentar-selbstaendig über das Agent SDK (Opus 5.5, hohe Stufe) samt Fundstellenprüfung mit
Hilfsagenten, Artikel als «geprueft» freigeben (dann veröffentlicht die Website ihn), nächster Artikel.
Keine Karteikarten, keine Batches.

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
from config import BATCHES, BATCH_PREISE, DATA, QUEUE, lade_json, schreibe_json  # noqa: E402
from reservierung import freigeben, reservieren  # noqa: E402

E = os.environ.get
EINSTELLUNGEN = {
    "TAGESBUDGET_USD": float(E("TAGESBUDGET_USD", "100")),
    "MONATSBUDGET_USD": float(E("MONATSBUDGET_USD", "100")),
    "MIN_REST_USD": float(E("MIN_REST_USD", "5")),          # darunter kein neuer Artikel mehr an diesem Tag
    "MODELL_SCHREIBEN": E("MODELL_SCHREIBEN", "claude-opus-5-5"),
    "EFFORT": E("EFFORT", "high"),
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
- Es gibt keine Karteikarten und kein vorbereitetes Register: Schritt 2 «Ohne Vorarbeit», Register und Problemkarte selbst
  in arbeit/{erlass}/{slug}/01_Recherche/ ablegen. Die Bundesgerichtsentscheide, die die Norm zitieren, liegen bereits
  im Cache data/entscheide/ (JSON mit referenz, zitat_de, normen, text); `python3 pipeline/entscheide.py {erlass}/{slug}`
  hat sie aus Open Case Law geladen.
- Fokus Rechtsprechung des Bundesgerichts (BGE, BGer): Sie trägt die Kommentierung. Quelle ist der Cache und Open Case Law
  (MCP-Server «open-case-law»; Zitierstrings nur mit `cite` bzw. aus zitat_de). Erlasse: data/inventar/ und Fedlex (WebFetch);
  Materialien nur, soweit die Übersicht (Entstehungsgeschichte, Harmonisierung) sie braucht.
- Kantonale Gerichte: ausschliesslich Entscheidsuche (POST https://entscheidsuche.ch/_search.php mit Filter `hierarchy`,
  Volltexte unter https://entscheidsuche.ch/docs/…). Verwaltungspraxis (ESTV-Kreisschreiben, MWST-Infos u.a.):
  Open Case Law (search_practice, get_practice); SSK-Kreisschreiben und kantonale Praxis über Fedlex/ESTV/SSK-Seiten per WebFetch,
  wenn die Adresse bekannt ist.
- Nicht recherchieren: Lehre (Schrifttum) und allgemeine Websuche (kein WebSearch). Lehre erscheint nur, wenn ein Entscheid sie
  selbst anführt, und dann als dessen Aussage mit dem Entscheid als Fundstelle. Der Abschnitt des Skills zur Lehre entfällt;
  das Fehlen nicht im Text erwähnen.
  Lexplorer ist nicht verfügbar.
- Schritt 8: Fundstellenprüfung vollständig mit Hilfsagenten (keine Batches).
- Schreibe nach kommentare/{erlass}/{slug}.md; `python3 pipeline/kommentar.py kommentare/{erlass}/{slug}.md` muss ohne Befund durchlaufen.
- Kein `stand.py setze`, kein git, keine Word-Fassung. Status und Veröffentlichung übernimmt das Steuerskript.
- Achte auf Kosten: Volltexte an der einschlägigen Erwägung lesen, nicht ganz; Hilfsagenten gezielt.
Ende: drei bis fünf Sätze Zusammenfassung."""


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

def artikel_schreiben(qid: str) -> None:
    erlass, slug = qid.split("/")
    nummer = lade_json(QUEUE)["artikel"][qid]["nummer"]
    datei = ROOT / "kommentare" / erlass / f"{slug}.md"
    pfade = pfade_artikel(erlass, slug)
    py("pipeline/entscheide.py", qid)   # Entscheide in den Cache (Open Case Law), ohne API-Kosten
    budget = rest()   # kein Limit je Artikel, nur das verbleibende Monatsbudget
    log(f"Schreibe {qid} (Budget {budget:.2f} USD, {EINSTELLUNGEN['MODELL_SCHREIBEN']}, Effort {EINSTELLUNGEN['EFFORT']}) …")
    try:
        kosten, _, typ = agent(AUFTRAG.format(nummer=nummer, erlass=erlass, slug=slug, root=ROOT), budget, qid, "schreiben")
    except GuthabenAufgebraucht:
        freigeben(qid, "zurueck", "Abbruch: API-Guthaben aufgebraucht", pfade, EINSTELLUNGEN["WER"])
        raise
    except Exception as fehler:  # noqa: BLE001
        freigeben(qid, "zurueck", f"Abbruch: {str(fehler)[:120]}", pfade, EINSTELLUNGEN["WER"])
        log(f"{qid}: Fehler im Agent-Lauf: {fehler}")
        return
    if not kommentar_ok(datei):
        versuche = lade_json(QUEUE)["artikel"][qid].get("versuche", 0) + 1
        freigeben(qid, "fehler" if versuche >= 2 else "zurueck",
                  f"Lauf {versuche} ohne gültige Kommentierung ({typ}, {kosten:.2f} USD)", pfade,
                  EINSTELLUNGEN["WER"], {"versuche": versuche})
        return
    freigeben(qid, "geprueft", f"GitHub Actions, {heute()} ({kosten:.2f} USD)", pfade, EINSTELLUNGEN["WER"])
    log(f"{qid}: fertig und freigegeben → wird veröffentlicht")
    website_bauen()


def website_bauen() -> None:
    """Pushes mit GITHUB_TOKEN lösen keinen Workflow aus; workflow_dispatch schon."""
    if os.environ.get("GITHUB_ACTIONS"):
        r = subprocess.run(["gh", "workflow", "run", "website.yml", "--ref", "main"], cwd=ROOT, text=True, capture_output=True)
        log("Website-Build gestartet" if r.returncode == 0 else f"Website-Build nicht gestartet: {r.stderr.strip()[:200]}")


def main() -> None:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        log("ANTHROPIC_API_KEY fehlt (Repository-Secret). Lauf beendet.")
        return
    log("Einstellungen:", json.dumps(EINSTELLUNGEN))
    log(f"Heute übrig: {tagesrest():.2f} USD, diesen Monat: {monatsrest():.2f} USD")
    try:
        while True:
            if minuten() > EINSTELLUNGEN["LAUFZEIT_MIN"]:
                log("Laufzeit erreicht; der nächste stündliche Lauf macht weiter.")
                break
            if rest() < EINSTELLUNGEN["MIN_REST_USD"]:
                log(f"Tages- oder Monatsbudget erreicht (heute {tagesrest():.2f}, Monat {monatsrest():.2f} USD übrig).")
                break
            qid = reservieren(EINSTELLUNGEN["WER"], ["bereit", "karten", "entscheide", "offen"])
            if not qid:
                log("Kein Artikel mehr offen.")
                break
            artikel_schreiben(qid)
    except GuthabenAufgebraucht:
        log("API-Guthaben aufgebraucht oder Ausgabenlimit der Console erreicht. Nächster Versuch im nächsten Lauf.")
    log(f"Fertig nach {minuten():.0f} Minuten. Heute übrig: {tagesrest():.2f} USD, Monat: {monatsrest():.2f} USD")


if __name__ == "__main__":
    main()
