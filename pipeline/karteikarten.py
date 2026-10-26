"""Karteikarten: lässt jeden Entscheid einmal über die Batch API auswerten (Sonnet oder Haiku,
50 % Rabatt) und legt je Entscheid eine Karteikarte als JSON ab. Die Karte hält für jede
zitierte Norm der fünf Erlasse fest: Klasse (A/B/C), Sachfrage, Kernaussage, Erwägung,
Ergebnis, Fassung und ein wörtliches Kurzzitat als Anker für die Fundstellenprüfung.

    python3 pipeline/karteikarten.py vorbereiten [DBG/art-26 ...] [--budget 40]
    python3 pipeline/karteikarten.py einreichen
    python3 pipeline/karteikarten.py status
    python3 pipeline/karteikarten.py abholen

`vorbereiten` ohne Artikel nimmt alle Artikel mit Status «entscheide» (nach Priorität) und
füllt den Batch, bis das Budget in USD erreicht ist. Braucht ANTHROPIC_API_KEY (Key aus der
Console-Organisation, die mit dem Max-Abo verknüpft ist).
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import (BATCH_PREISE, BATCHES, DATA, ENTSCHEIDE, ERLASSE, KARTEN, MODELL_KARTEN,  # noqa: E402
                    QUEUE, lade_json, schreibe_json)

ZITATE = DATA / "zitate"
MAX_ZEICHEN = 140_000          # längere Entscheide werden gekürzt (Rubrum und Sachverhalt zuerst)
MAX_JE_BATCH = 5_000

SYSTEM = """Du wertest einen Entscheid des Schweizerischen Bundesgerichts für einen wissenschaftlichen Kommentar zum Bundessteuerrecht aus. Kommentiert werden fünf Bundesgesetze: DBG (frz./ital. LIFD), StHG (LHID/LAID), VStG (LIA/LIP), MWSTG (LTVA/LIVA) und das Bundesgesetz über die Stempelabgaben, hier «StG» (frz. LT, ital. LTB).

Du erhältst die Metadaten, eine Liste der Artikel dieser Gesetze, die eine automatische Erkennung im Text gefunden hat, und den Volltext. Rufe das Werkzeug `karteikarte` genau einmal auf.

Regeln:
1. Arbeite nur mit dem Text des Entscheids. Nichts ergänzen, was dort nicht steht; keine Fundstellen erfinden.
2. Für jeden erkannten Artikel einen Eintrag in `normen`. Ergänze Artikel der fünf Gesetze, die die Erkennung übersehen hat und die der Entscheid in den Erwägungen anwendet oder auslegt. Fasst der Entscheid mehrere Absätze eines Artikels getrennt, genügt ein Eintrag je Artikel mit der wichtigsten Normstelle; weitere Normstellen in `normstelle` nennen.
3. `relevant` ist false, wenn der Treffer nicht das Bundesgesetz meint (z.B. «StG» für ein kantonales Steuergesetz, «LT» in anderem Sinn) oder die Norm nur in einer Aufzählung ohne Bezug steht. Dann genügen `norm`, `relevant` und ein Satz in `kernaussage`.
4. Klasse: A = die Erwägung legt die Norm aus oder entscheidet eine Rechtsfrage daraus (Rechtssatz); B = Anwendung bekannter Grundsätze auf den Fall (Subsumtion, Kasuistik); C = blosse Erwähnung (Normkette, Sachverhalt, Prozessgeschichte, Kosten).
5. `kernaussage`: bei A der Rechtssatz abstrakt in ein bis zwei Sätzen («Fahrkosten sind nur in der Höhe der Kosten des öffentlichen Verkehrs abziehbar, wenn …»), bei B das Ergebnis im Fall mit dem entscheidenden Umstand, bei C ein kurzer Satz. Eigene Worte, deutsch, neutral, keine Wertung.
6. `erwaegung`: die Erwägung, die die Aussage trägt, so genau wie möglich («E. 3.2.1»). Nicht raten: Wenn sich die Nummer nicht feststellen lässt, leer lassen.
7. `zitat`: ein wörtlicher Ausschnitt von 8 bis 40 Wörtern aus genau dieser Erwägung, der die Kernaussage trägt, in der Originalsprache, Zeichen für Zeichen aus dem Text kopiert. Bei C leer lassen.
8. `sachfrage`: kurzes Stichwort der Rechtsfrage, so allgemein, dass gleiche Fragen in anderen Entscheiden gleich heissen («Fahrkosten: Mehrkosten des Privatfahrzeugs», «Weiterbildungskosten: Abgrenzung zu Ausbildung»).
9. `fassung`: Steuerperiode oder Zeitraum, falls der Entscheid eine frühere Fassung der Norm anwendet («Steuerperiode 2014; Fassung vor FABI»), sonst leer.
10. `bge`: nur ausfüllen, wenn der Text selbst die amtliche Publikation angibt (z.B. «BGE 148 II 285»). `besetzung_fuenf`: true, wenn fünf Richterinnen oder Richter mitwirken.
11. `lehre` und `praxis`: Fundstellen von Literatur und Verwaltungspraxis (Kreisschreiben, MWST-Info, Merkblätter), die der Entscheid in derselben Erwägung zur Norm zitiert, wörtlich wie im Entscheid; höchstens fünf je Liste.
"""

WERKZEUG = {
    "name": "karteikarte",
    "description": "Karteikarte zu einem Bundesgerichtsentscheid ablegen.",
    "input_schema": {
        "type": "object",
        "properties": {
            "geschaeftsnummer": {"type": "string"},
            "bge": {"type": "string"},
            "datum": {"type": "string", "description": "TT.MM.JJJJ"},
            "besetzung_fuenf": {"type": "boolean"},
            "gegenstand": {"type": "string", "description": "Steuer, Steuerperiode, Streitfrage in einem Satz"},
            "regeste": {"type": "string", "description": "Kern des Entscheids in höchstens zwei Sätzen, eigene Worte"},
            "ausgang": {"type": "string", "description": "z.B. Beschwerde abgewiesen / gutgeheissen / Rückweisung"},
            "normen": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "norm": {"type": "string", "description": "Erlass/Artikel, z.B. DBG/26, StHG/9, MWSTG/21"},
                        "normstelle": {"type": "string", "description": "z.B. Abs. 1 lit. c"},
                        "relevant": {"type": "boolean"},
                        "klasse": {"type": "string", "enum": ["A", "B", "C"]},
                        "sachfrage": {"type": "string"},
                        "kernaussage": {"type": "string"},
                        "erwaegung": {"type": "string"},
                        "ergebnis": {"type": "string"},
                        "fassung": {"type": "string"},
                        "zitat": {"type": "string"},
                        "lehre": {"type": "array", "items": {"type": "string"}},
                        "praxis": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["norm", "relevant", "klasse", "kernaussage"],
                },
            },
        },
        "required": ["geschaeftsnummer", "datum", "gegenstand", "normen"],
    },
}


def cid(entscheid_id: str) -> str:
    return "k" + hashlib.sha1(entscheid_id.encode()).hexdigest()[:24]


def anfrage(e: dict) -> dict:
    erkannt = []
    for norm, ausschnitte in sorted(e["normen"].items()):
        erlass = norm.split("/")[0]
        if erlass in ERLASSE:
            erkannt.append(f"- {norm}: «…{ausschnitte[0][150:320].strip()}…»")
    text = e["text"]
    if len(text) > MAX_ZEICHEN:
        text = text[:MAX_ZEICHEN] + "\n[… gekürzt …]"
    inhalt = (
        f"Referenz: {', '.join(e['referenz'])}\nDatum: {e['datum']}\nGericht: {e.get('titel') or ''}\n"
        f"Sprache: {e.get('sprache') or ''}\n\nErkannte Artikel:\n" + ("\n".join(erkannt) or "- keine") +
        f"\n\nVolltext:\n<entscheid>\n{text}\n</entscheid>"
    )
    return {
        "custom_id": cid(e["id"]),
        "params": {
            "model": MODELL_KARTEN,
            "max_tokens": 6000,
            "system": [{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}],
            "tools": [WERKZEUG],
            "tool_choice": {"type": "tool", "name": "karteikarte"},
            "messages": [{"role": "user", "content": inhalt}],
        },
    }


def schaetzung(anfragen: list[dict], modell: str) -> float:
    preis = BATCH_PREISE.get(modell, BATCH_PREISE["claude-sonnet-5-5"])
    tok_in = sum(len(a["params"]["messages"][0]["content"]) / 3.0 for a in anfragen) + 1500 * len(anfragen)
    tok_out = 700 * len(anfragen)
    return (tok_in * preis["in"] + tok_out * preis["out"]) / 1e6


def vorbereiten(args) -> None:
    queue = lade_json(QUEUE)
    if args.artikel:
        artikel = args.artikel
    else:
        artikel = [k for k, v in queue["artikel"].items() if v["status"] == "entscheide"]
        artikel.sort(key=lambda k: -(queue["artikel"][k]["prioritaet"] or 0))
    offen_ids = {p.stem for p in KARTEN.glob("*.json")}
    laufend = set()
    for b in BATCHES.glob("*/zuordnung.json"):
        meta = lade_json(b.parent / "batch.json", {})
        if meta.get("status") != "abgeholt":
            laufend |= set(lade_json(b, {}).values())
    anfragen, zuordnung, artikel_im_batch, summe = [], {}, [], 0.0
    for qid in artikel:
        erlass, slug = qid.split("/")
        z = lade_json(ZITATE / erlass / f"{slug}.json")
        if z is None:
            print(f"{qid}: zuerst entscheide.py ausführen")
            continue
        neu = []
        for eintrag in z["entscheide"]:
            did = eintrag["id"]
            if not did or did in offen_ids or did in laufend or did in zuordnung.values():
                continue
            e = lade_json(ENTSCHEIDE / f"{did}.json")
            if e and e["text"]:
                neu.append(anfrage(e))
                zuordnung[neu[-1]["custom_id"]] = did
        kosten = schaetzung(neu, MODELL_KARTEN)
        if args.budget and summe + kosten > args.budget and anfragen:
            break
        anfragen += neu
        summe += kosten
        artikel_im_batch.append(qid)
        if len(anfragen) >= MAX_JE_BATCH:
            break
    if not anfragen:
        print("Nichts vorzubereiten: alle Entscheide dieser Artikel haben schon eine Karte.")
        return
    name = dt.datetime.now().strftime("%Y%m%d-%H%M%S") + "-karten"
    ordner = BATCHES / name
    ordner.mkdir(parents=True)
    with open(ordner / "anfragen.jsonl", "w", encoding="utf-8") as f:
        for a in anfragen:
            f.write(json.dumps(a, ensure_ascii=False) + "\n")
    schreibe_json(ordner / "zuordnung.json", zuordnung)
    schreibe_json(ordner / "batch.json", {"art": "karten", "modell": MODELL_KARTEN, "status": "vorbereitet",
                                          "artikel": artikel_im_batch, "anfragen": len(anfragen),
                                          "kosten_geschaetzt_usd": round(summe, 2)})
    print(f"Batch {name}: {len(anfragen)} Entscheide aus {len(artikel_im_batch)} Artikeln, "
          f"geschätzt {summe:.2f} USD ({MODELL_KARTEN}, Batch-Preis). Einreichen mit: karteikarten.py einreichen")


def client():
    import anthropic
    return anthropic.Anthropic()


def einreichen(args) -> None:
    c = client()
    for meta_pfad in sorted(BATCHES.glob("*/batch.json")):
        if getattr(args, "nur", None) and meta_pfad.parent.name != args.nur:
            continue
        meta = lade_json(meta_pfad)
        if meta["status"] != "vorbereitet":
            continue
        anfragen = [json.loads(z) for z in (meta_pfad.parent / "anfragen.jsonl").read_text(encoding="utf-8").splitlines()]
        # Vorprüfung ohne Kosten: Token-Zählung mit den Parametern der ersten Anfrage. Ein Fehler in Modellname
        # oder Parametern fällt so sofort auf, statt dass der ganze Batch scheitert.
        probe = {k: v for k, v in anfragen[0]["params"].items() if k in ("model", "system", "tools", "tool_choice", "messages")}
        try:
            c.messages.count_tokens(**probe)
        except Exception as fehler:  # noqa: BLE001
            print(f"{meta_pfad.parent.name}: Vorprüfung fehlgeschlagen, nicht eingereicht: {fehler}")
            meta.update({"status": "abgelehnt", "fehler": str(fehler)[:2000]})
            schreibe_json(meta_pfad, meta)
            raise SystemExit(2)
        b = c.messages.batches.create(requests=anfragen)
        meta.update({"status": "eingereicht", "batch_id": b.id, "eingereicht": dt.datetime.now().isoformat()})
        schreibe_json(meta_pfad, meta)
        print(f"{meta_pfad.parent.name}: eingereicht als {b.id}")


def status(args) -> None:
    c = None
    for meta_pfad in sorted(BATCHES.glob("*/batch.json")):
        meta = lade_json(meta_pfad)
        zeile = f"{meta_pfad.parent.name} [{meta.get('art')}] {meta['status']}, {meta['anfragen']} Anfragen"
        if meta["status"] == "eingereicht":
            c = c or client()
            b = c.messages.batches.retrieve(meta["batch_id"])
            rc = b.request_counts
            zeile += (f" – {b.processing_status}: {rc.succeeded} fertig, {rc.processing} in Arbeit, "
                      f"{rc.errored} Fehler")
        print(zeile)


def abholen(args) -> None:
    c = client()
    queue = lade_json(QUEUE)
    for meta_pfad in sorted(BATCHES.glob("*/batch.json")):
        meta = lade_json(meta_pfad)
        if meta["status"] != "eingereicht" or meta.get("art") != "karten":
            continue
        b = c.messages.batches.retrieve(meta["batch_id"])
        if b.processing_status != "ended":
            print(f"{meta_pfad.parent.name}: noch in Arbeit")
            continue
        zuordnung = lade_json(meta_pfad.parent / "zuordnung.json")
        ok = fehler = 0
        tokens_in = tokens_out = 0
        fehlerliste = []
        for r in c.messages.batches.results(meta["batch_id"]):
            did = zuordnung.get(r.custom_id)
            if r.result.type != "succeeded":
                fehler += 1
                fehlerliste.append(did)
                if len(meta.setdefault("fehlerbeispiele", [])) < 3:
                    meta["fehlerbeispiele"].append(str(getattr(r.result, "error", r.result))[:1500])
                    print(f"Fehler bei {did}: {meta['fehlerbeispiele'][-1]}")
                continue
            msg = r.result.message
            tokens_in += (msg.usage.input_tokens or 0) + (msg.usage.cache_read_input_tokens or 0)
            tokens_out += msg.usage.output_tokens or 0
            karte = next((blk.input for blk in msg.content if blk.type == "tool_use"), None)
            if karte is None:
                fehler += 1
                fehlerliste.append(did)
                continue
            e = lade_json(ENTSCHEIDE / f"{did}.json")
            karte["_entscheid_id"] = did
            karte["_url"] = e.get("url") if e else None
            karte["_referenz"] = e.get("referenz") if e else []
            karte["_modell"] = msg.model
            karte["_erstellt"] = dt.date.today().isoformat()
            karte["_zitat_geprueft"] = zitate_pruefen(karte, e["text"] if e else "")
            schreibe_json(KARTEN / f"{did}.json", karte)
            ok += 1
        meta.update({"status": "abgeholt", "ok": ok, "fehler": fehler, "fehlerliste": fehlerliste,
                     "tokens_in": tokens_in, "tokens_out": tokens_out})
        schreibe_json(meta_pfad, meta)
        print(f"{meta_pfad.parent.name}: {ok} Karten, {fehler} Fehler (erneut mit «vorbereiten»)")
    # Status der Artikel nachführen
    vorhanden = {p.stem for p in KARTEN.glob("*.json")}
    for qid, v in queue["artikel"].items():
        if v["status"] != "entscheide":
            continue
        erlass, slug = qid.split("/")
        z = lade_json(ZITATE / erlass / f"{slug}.json")
        if not z:
            continue
        ids = [x["id"] for x in z["entscheide"] if x["id"]]
        v["karten_fertig"] = sum(1 for i in ids if i in vorhanden)
        if ids and v["karten_fertig"] == len(ids):
            v["status"] = "karten"
    schreibe_json(QUEUE, queue)


def fehler_zeigen(args) -> None:
    """Zeigt die Fehlermeldungen abgeholter Batches mit Fehlern (erste drei je Batch)."""
    c = client()
    for meta_pfad in sorted(BATCHES.glob("*/batch.json")):
        meta = lade_json(meta_pfad)
        if not meta.get("fehler") or meta.get("fehlerbeispiele") or "batch_id" not in meta:
            continue
        beispiele = []
        for r in c.messages.batches.results(meta["batch_id"]):
            if r.result.type != "succeeded":
                beispiele.append(str(getattr(r.result, "error", r.result))[:1500])
                if len(beispiele) >= 3:
                    break
        meta["fehlerbeispiele"] = beispiele
        schreibe_json(meta_pfad, meta)
        for b in beispiele:
            print(f"{meta_pfad.parent.name}: {b}")


def zitate_pruefen(karte: dict, text: str) -> dict:
    """Prüft maschinell, ob jedes Kurzzitat wörtlich im Entscheid steht (Leerraum normalisiert)."""
    import re

    def norm(s):
        return re.sub(r"\s+", " ", s.replace("«", '"').replace("»", '"')).strip().lower()
    t = norm(text)
    erg = {}
    for n in karte.get("normen", []):
        z = n.get("zitat") or ""
        if z:
            erg[n["norm"]] = norm(z) in t
    return erg


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("vorbereiten")
    v.add_argument("artikel", nargs="*")
    v.add_argument("--budget", type=float, default=40.0, help="Obergrenze in USD (geschätzt) je Batch")
    e = sub.add_parser("einreichen")
    e.add_argument("--nur", help="nur diesen Batch-Ordner einreichen")
    sub.add_parser("status")
    sub.add_parser("abholen")
    sub.add_parser("fehler")
    a = ap.parse_args()
    {"vorbereiten": vorbereiten, "einreichen": einreichen, "status": status, "abholen": abholen,
     "fehler": fehler_zeigen}[a.cmd](a)


if __name__ == "__main__":
    main()
