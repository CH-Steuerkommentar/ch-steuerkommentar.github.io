"""Fundstellenprüfung per Batch API: prüft jede Fussnote, die einen Bundesgerichtsentscheid
zitiert, gegen die zitierte Erwägung im Volltext. Eine eigene Modellinstanz ohne Kenntnis
der Entstehung urteilt: stützt die Erwägung die Aussage, und stimmt die Erwägungsnummer?

    python3 pipeline/pruefung.py vorbereiten kommentare/DBG/art-26.md
    python3 pipeline/karteikarten.py einreichen        # reicht auch Prüf-Batches ein
    python3 pipeline/karteikarten.py status
    python3 pipeline/pruefung.py abholen

Ergebnis: arbeit/<Erlass>/<art>/Fundstellenliste_<Datum>.md. Fussnoten ohne Bundesgerichts-
entscheid (Lehre, Praxis, kantonale Gerichte, Materialien) stehen dort als «im Skill prüfen».
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import ARBEIT, BATCHES, ENTSCHEIDE, MODELL_PRUEFUNG, art_slug, lade_json, schreibe_json  # noqa: E402
from kommentar import fussnoten_finden, lesen  # noqa: E402

RE_BGE = re.compile(r"BGE\s+(\d{2,3})\s+([IVX]+[a-z]?)\s+(\d+)(?:\s*,?\s*E\.\s*([\d.]+(?:\s*f{1,2}\.)?))?")
RE_BGER = re.compile(r"(?:BGer\s+|Urteil(?:e)?\s+(?:des\s+Bundesgerichts\s+)?)?(\d[A-Z]{1,2})[_.](\d{1,4})/(\d{4})"
                     r"(?:[^;]*?E\.\s*([\d.]+(?:\s*f{1,2}\.)?))?")

SYSTEM = """Du prüfst Fussnoten eines Rechtskommentars gegen die Quelle. Du erhältst eine Aussage aus dem Kommentar, die Fundstelle aus der Fussnote und den Text der zitierten Erwägung eines Bundesgerichtsentscheids (oder, wenn sie sich nicht abgrenzen liess, einen grösseren Ausschnitt).

Rufe das Werkzeug `befund` genau einmal auf.
- `ergebnis`: «bestätigt», wenn die Erwägung die Aussage trägt; «teilweise», wenn sie nur einen Teil trägt oder die Aussage weiter geht; «erwaegung_falsch», wenn die Aussage im Entscheid steht, aber in einer anderen Erwägung; «nicht_belegt», wenn der Entscheid die Aussage nicht trägt.
- `richtige_erwaegung`: bei «erwaegung_falsch» die richtige Erwägung, sonst leer.
- `begruendung`: ein bis zwei Sätze; bei «teilweise» und «nicht_belegt», was fehlt oder abweicht.
- Prüfe streng und nur am gegebenen Text. Eine Aussage über die Lehre oder Praxis wird durch einen Entscheid nur bestätigt, wenn der Entscheid sie selbst wiedergibt."""

WERKZEUG = {
    "name": "befund",
    "description": "Prüfergebnis zu einer Fundstelle ablegen.",
    "input_schema": {"type": "object", "properties": {
        "ergebnis": {"type": "string", "enum": ["bestätigt", "teilweise", "erwaegung_falsch", "nicht_belegt"]},
        "richtige_erwaegung": {"type": "string"},
        "begruendung": {"type": "string"},
    }, "required": ["ergebnis", "begruendung"]},
}


def cache_index() -> dict[str, str]:
    """Referenz (BGE 148 II 285 / 2C_123/2020) -> Entscheid-ID im Cache."""
    idx = {}
    for p in ENTSCHEIDE.glob("*.json"):
        e = lade_json(p)
        for r in e.get("referenz", []):
            idx[normref(r)] = e["id"]
        m = re.search(r"(\d[A-Z]{1,2})[_.-](\d{1,4})[-/](\d{4})", e["id"])
        if m:
            idx[f"{m.group(1)}_{m.group(2)}/{m.group(3)}"] = e["id"]
        m = re.search(r"BGE-(\d+)-([IVX]+)-(\d+)", e["id"])
        if m:
            idx[f"BGE {m.group(1)} {m.group(2)} {m.group(3)}"] = e["id"]
    return idx


def normref(r: str) -> str:
    r = r.replace("-", "_", 1) if re.match(r"^\d[A-Z]{1,2}-", r) else r
    r = re.sub(r"^(\d[A-Z]{1,2})[_.](\d+)[/-](\d{4})$", r"\1_\2/\3", r.strip())
    return re.sub(r"\s+", " ", r)


def erwaegung(text: str, e_nr: str | None) -> tuple[str, bool]:
    """Schneidet die Erwägung aus dem Volltext. Gibt (Ausschnitt, genau_gefunden) zurück."""
    start = 0
    for marke in ("Erwägungen", "Erwägung:", "Considérant", "Considerando", "Diritto", "Droit:", "Aus den Erwägungen"):
        i = text.find(marke)
        if i >= 0:
            start = i
            break
    rumpf = text[start:]
    if e_nr:
        nr = re.sub(r"\s*f{1,2}\.$", "", e_nr.strip()).rstrip(".")
        teile = nr.split(".")
        for laenge in range(len(teile), 0, -1):
            kand = ".".join(teile[:laenge])
            m = re.search(rf"(?m)^\s*{re.escape(kand)}\.?\s+\S", rumpf)
            if m:
                rest = rumpf[m.start():]
                # Ende: nächste Erwägung gleicher oder höherer Ebene
                tief = len(kand.split("."))
                muster = []
                for k in range(tief, 0, -1):
                    basis = kand.split(".")[:k]
                    basis[-1] = str(int(basis[-1]) + 1) if basis[-1].isdigit() else basis[-1]
                    muster.append(re.escape(".".join(basis)))
                ende = re.search(rf"(?m)^\s*(?:{'|'.join(muster)})\.?\s+\S", rest[10:])
                aus = rest[: (ende.start() + 10) if ende else 12000]
                return aus[:12000], laenge == len(teile)
    return rumpf[:30000], False


def aussage_vor(text: str, pos: int) -> str:
    vor = re.sub(r"\^\[.*?\]", "", text[:pos])
    saetze = re.split(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ«])", vor.strip())
    return " ".join(saetze[-2:])[-700:]


def vorbereiten(args) -> None:
    k = lesen(args.datei)
    idx = cache_index()
    anfragen, zuordnung, liste = [], {}, []
    fn_nr = 0
    for b in k.bloecke:
        for teil in [b.text] + b.zeilen:
            for s, e, inhalt in fussnoten_finden(teil):
                fn_nr += 1
                aussage = aussage_vor(teil, s)
                treffer = []
                for m in RE_BGE.finditer(inhalt):
                    treffer.append((f"BGE {m.group(1)} {m.group(2)} {m.group(3)}", m.group(4)))
                for m in RE_BGER.finditer(inhalt):
                    treffer.append((f"{m.group(1)}_{m.group(2)}/{m.group(3)}", m.group(4)))
                if not treffer:
                    liste.append({"fn": fn_nr, "randnote": b.nummer, "fundstelle": inhalt, "ergebnis": "im Skill prüfen"})
                    continue
                rest = RE_BGER.sub("", RE_BGE.sub("", inhalt))
                rest = re.sub(r"vom\s+\d{1,2}\.\d{1,2}\.\d{4}|E\.\s*[\d.]+|\b(?:vgl|so|ferner|bestätigt in|BGer)\b\.?", "", rest)
                if len(re.findall(r"[A-Za-zÄÖÜäöü]", rest)) >= 4:
                    liste.append({"fn": fn_nr, "randnote": b.nummer, "fundstelle": rest.strip(" ;,."),
                                  "ergebnis": "übrige Fundstellen der Fussnote im Skill prüfen"})
                for ref, e_nr in treffer:
                    did = idx.get(normref(ref))
                    if not did:
                        liste.append({"fn": fn_nr, "randnote": b.nummer, "fundstelle": ref, "ergebnis": "nicht im Cache – im Skill prüfen"})
                        continue
                    ent = lade_json(ENTSCHEIDE / f"{did}.json")
                    aus, genau = erwaegung(ent["text"], e_nr)
                    cid = f"f{fn_nr}_{len(anfragen)}"
                    zuordnung[cid] = {"fn": fn_nr, "randnote": b.nummer, "fundstelle": f"{ref}" + (f", E. {e_nr}" if e_nr else ""),
                                      "aussage": aussage, "erwaegung_genau": genau, "entscheid": did}
                    anfragen.append({"custom_id": cid, "params": {
                        "model": MODELL_PRUEFUNG, "max_tokens": 800,
                        "system": [{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}],
                        "tools": [WERKZEUG], "tool_choice": {"type": "tool", "name": "befund"},
                        "messages": [{"role": "user", "content":
                                      f"Aussage im Kommentar (N. {b.nummer}):\n{aussage}\n\nFundstelle: {ref}"
                                      + (f", E. {e_nr}" if e_nr else ", ohne Erwägungsangabe") +
                                      f"\n\n{'Text der Erwägung' if genau else 'Ausschnitt (Erwägung nicht genau abgrenzbar)'}:"
                                      f"\n<quelle>\n{aus}\n</quelle>"}]}})
    erlass, slug = k.meta["erlass"], art_slug(k.meta["artikel"])
    name = dt.datetime.now().strftime("%Y%m%d-%H%M%S") + "-pruefung"
    ordner = BATCHES / name
    ordner.mkdir(parents=True)
    with open(ordner / "anfragen.jsonl", "w", encoding="utf-8") as f:
        for a in anfragen:
            f.write(json.dumps(a, ensure_ascii=False) + "\n")
    schreibe_json(ordner / "zuordnung.json", zuordnung)
    schreibe_json(ordner / "batch.json", {"art": "pruefung", "modell": MODELL_PRUEFUNG, "status": "vorbereitet",
                                          "artikel": [f"{erlass}/{slug}"], "anfragen": len(anfragen),
                                          "ohne_batch": liste, "fussnoten": fn_nr})
    print(f"{fn_nr} Fussnoten: {len(anfragen)} Entscheid-Fundstellen im Batch {name}, "
          f"{len(liste)} für die Prüfung im Skill.")


def abholen(args) -> None:
    import anthropic
    c = anthropic.Anthropic()
    for meta_pfad in sorted(BATCHES.glob("*/batch.json")):
        meta = lade_json(meta_pfad)
        if meta.get("art") != "pruefung" or meta["status"] != "eingereicht":
            continue
        b = c.messages.batches.retrieve(meta["batch_id"])
        if b.processing_status != "ended":
            print(f"{meta_pfad.parent.name}: noch in Arbeit")
            continue
        zuordnung = lade_json(meta_pfad.parent / "zuordnung.json")
        zeilen = list(meta["ohne_batch"])
        for r in c.messages.batches.results(meta["batch_id"]):
            z = dict(zuordnung[r.custom_id])
            if r.result.type == "succeeded":
                bef = next((blk.input for blk in r.result.message.content if blk.type == "tool_use"), {})
                z.update(bef)
            else:
                z["ergebnis"] = "Fehler im Batch – im Skill prüfen"
            zeilen.append(z)
        zeilen.sort(key=lambda z: z["fn"])
        erlass, slug = meta["artikel"][0].split("/")
        ziel = ARBEIT / erlass / slug / f"Fundstellenliste_{dt.date.today().isoformat()}.md"
        ziel.parent.mkdir(parents=True, exist_ok=True)
        aus = [f"# Fundstellenliste {meta['artikel'][0]}\n",
               "Entscheid-Fundstellen per Batch geprüft (eigene Modellinstanz, Erwägung im Volltext). "
               "«im Skill prüfen»: Lehre, Praxis, kantonale Entscheide und Materialien.\n",
               "| Fn. | N. | Fundstelle | Ergebnis | richtige E. | Hinweis |", "|---|---|---|---|---|---|"]
        for z in zeilen:
            hinweis = (z.get("begruendung") or "")
            if z.get("erwaegung_genau") is False:
                hinweis = "(E. nicht genau abgrenzbar) " + hinweis
            aus.append(f"| {z['fn']} | {z.get('randnote') or ''} | {z['fundstelle'][:120].replace('|', '/')} | "
                       f"{z.get('ergebnis', '')} | {z.get('richtige_erwaegung') or ''} | {hinweis.replace('|', '/')} |")
        ziel.write_text("\n".join(aus) + "\n", encoding="utf-8")
        meta["status"] = "abgeholt"
        schreibe_json(meta_pfad, meta)
        n_prob = sum(1 for z in zeilen if z.get("ergebnis") in ("teilweise", "erwaegung_falsch", "nicht_belegt"))
        print(f"{ziel}: {len(zeilen)} Zeilen, {n_prob} zu beheben")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("vorbereiten")
    v.add_argument("datei")
    sub.add_parser("abholen")
    a = ap.parse_args()
    {"vorbereiten": vorbereiten, "abholen": abholen}[a.cmd](a)


if __name__ == "__main__":
    main()
