"""Register: baut aus den Karteikarten je Artikel das Entscheidregister, eine Problemkarte
(nach Sachfragen verdichtet) und die Karteikarten zum Lesen. Das ist der Ausgangspunkt
für den Skill `steuerkommentar-selbstaendig`.

    python3 pipeline/register.py DBG/art-26
    python3 pipeline/register.py --alle          # alle Artikel mit Status «karten»

Ergebnis in arbeit/<Erlass>/<art>/01_Recherche/:
- Entscheidregister.md   eine Zeile je Entscheid (Klasse, Sachfrage, Kernaussage, E., Ergebnis, Fassung)
- Problemkarte.md        Sachfragen mit Zahl der A/B-Entscheide und Leitentscheiden
- Karteikarten.md        A- und B-Karten ausführlich, mit wörtlichem Kurzzitat und Link
- register.json          dasselbe maschinenlesbar
"""
from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import ARBEIT, DATA, INVENTAR, KARTEN, QUEUE, lade_json, schreibe_json  # noqa: E402

ZITATE = DATA / "zitate"


def ref(karte: dict) -> str:
    bge = (karte.get("bge") or "").strip()
    gn = (karte.get("geschaeftsnummer") or "").strip()
    teile = [t for t in (bge, f"BGer {gn}" if gn and not gn.startswith("BGE") else gn) if t]
    return " = ".join(dict.fromkeys(teile)) or ", ".join(karte.get("_referenz", []))


def zelle(s) -> str:
    return (s or "").replace("|", "/").replace("\n", " ").strip()


def bauen(qid: str, queue: dict) -> dict:
    erlass, slug = qid.split("/")
    nummer = queue["artikel"][qid]["nummer"].lower()
    norm_key = f"{erlass}/{nummer}"
    z = lade_json(ZITATE / erlass / f"{slug}.json", {"entscheide": []})
    zeilen, fehlend, fehltreffer = [], [], []
    gesehen = set()
    for eintrag in z["entscheide"]:
        did = eintrag["id"]
        if not did:
            fehlend.append(eintrag["referenz"][0])
            continue
        karte = lade_json(KARTEN / f"{did}.json")
        if karte is None:
            fehlend.append(", ".join(eintrag["referenz"]))
            continue
        norm = next((n for n in karte.get("normen", []) if n.get("norm", "").lower() == norm_key.lower()), None)
        if norm is None:
            norm = {"relevant": True, "klasse": "C", "kernaussage": "Norm erkannt, auf der Karte nicht erfasst.",
                    "norm": norm_key}
        if not norm.get("relevant", True):
            fehltreffer.append(ref(karte))
            continue
        # BGE und zugehöriges BGer-Urteil zusammenführen
        schluessel = (karte.get("geschaeftsnummer") or did).split(",")[0].strip()
        if schluessel in gesehen:
            continue
        gesehen.add(schluessel)
        zeilen.append({
            "entscheid": ref(karte), "datum": karte.get("datum"), "fuenf": bool(karte.get("besetzung_fuenf")),
            "normstelle": norm.get("normstelle", ""), "sachfrage": norm.get("sachfrage", ""),
            "kernaussage": norm.get("kernaussage", ""), "erwaegung": norm.get("erwaegung", ""),
            "ergebnis": norm.get("ergebnis", "") or karte.get("ausgang", ""), "klasse": norm.get("klasse", "C"),
            "fassung": norm.get("fassung", ""), "zitat": norm.get("zitat", ""),
            "zitat_wortlaut_geprueft": karte.get("_zitat_geprueft", {}).get(norm.get("norm", norm_key)),
            "lehre": norm.get("lehre", []), "praxis": norm.get("praxis", []),
            "url": karte.get("_url"), "entscheid_id": did, "gegenstand": karte.get("gegenstand", ""),
        })
    reihenfolge = {"A": 0, "B": 1, "C": 2}
    zeilen.sort(key=lambda r: (reihenfolge.get(r["klasse"], 3), r["datum"] or ""))
    return {"artikel": qid, "zeilen": zeilen, "fehlend": fehlend, "fehltreffer": fehltreffer,
            "suchtreffer": z.get("suchtreffer"), "abfrage": z.get("abfrage")}


def normtext(qid: str) -> tuple[str, str]:
    erlass, slug = qid.split("/")
    inv = lade_json(INVENTAR / f"{erlass}.json", {"artikel": []})
    for a in inv["artikel"]:
        if "art-" + a["nummer"].lower() == slug:
            return a["sachueberschrift"], a["normtext"]
    return "", ""


def schreiben(reg: dict) -> Path:
    qid = reg["artikel"]
    erlass, slug = qid.split("/")
    ordner = ARBEIT / erlass / slug / "01_Recherche"
    ordner.mkdir(parents=True, exist_ok=True)
    schreibe_json(ordner / "register.json", reg)
    z = reg["zeilen"]
    n = {k: sum(1 for r in z if r["klasse"] == k) for k in "ABC"}
    titel, norm = normtext(qid)
    kopf = (f"# Entscheidregister {qid}\n\n{titel}\n\n```\n{norm}\n```\n\n"
            f"Quelle: entscheidsuche.ch, Abfrage `{reg['abfrage']}` ({reg['suchtreffer']} Suchtreffer). "
            f"{len(z)} Entscheide: {n['A']} A, {n['B']} B, {n['C']} C. "
            f"Fehltreffer ausgeschieden: {len(reg['fehltreffer'])}. Ohne Karte: {len(reg['fehlend'])}.\n\n"
            "Die Gegenprobe über Open Case Law steht noch aus (Skill, Schritt 2).\n\n")
    tab = ["| Entscheid | Datum | 5er | Normstelle | Sachfrage | Kernaussage | E. | Ergebnis | Kl. | Fassung |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for r in z:
        tab.append("| " + " | ".join(zelle(x) for x in (
            r["entscheid"], r["datum"], "ja" if r["fuenf"] else "", r["normstelle"], r["sachfrage"],
            r["kernaussage"], r["erwaegung"], r["ergebnis"], r["klasse"], r["fassung"])) + " |")
    rest = ""
    if reg["fehlend"]:
        rest += "\n\n## Ohne Karte\n\n" + "\n".join(f"- {x}" for x in reg["fehlend"])
    if reg["fehltreffer"]:
        rest += "\n\n## Fehltreffer (nicht diese Norm)\n\n" + "\n".join(f"- {x}" for x in reg["fehltreffer"])
    (ordner / "Entscheidregister.md").write_text(kopf + "\n".join(tab) + rest + "\n", encoding="utf-8")

    # Problemkarte
    gruppen = defaultdict(list)
    for r in z:
        if r["klasse"] in "AB":
            gruppen[r["sachfrage"] or "(ohne Sachfrage)"].append(r)
    pk = [f"# Problemkarte {qid}\n", "Sachfragen nach Zahl der A-Entscheide. Gleiche Fragen mit "
          "abweichender Bezeichnung beim Gliedern zusammenlegen.\n",
          "| Sachfrage | A | B | Leitentscheide (A, älteste zuerst) | Normstellen |", "|---|---|---|---|---|"]
    for sf, rs in sorted(gruppen.items(), key=lambda kv: (-sum(r["klasse"] == "A" for r in kv[1]), -len(kv[1]))):
        a = [r for r in rs if r["klasse"] == "A"]
        leit = "; ".join(f"{r['entscheid']} {r['erwaegung']}".strip() for r in sorted(a, key=lambda r: r["datum"] or "")[:4])
        stellen = ", ".join(sorted({r["normstelle"] for r in rs if r["normstelle"]}))
        pk.append(f"| {zelle(sf)} | {len(a)} | {len(rs) - len(a)} | {zelle(leit)} | {zelle(stellen)} |")
    (ordner / "Problemkarte.md").write_text("\n".join(pk) + "\n", encoding="utf-8")

    # Karteikarten zum Lesen
    kk = [f"# Karteikarten {qid}\n", "Maschinell erstellt aus dem Volltext (Batch). «Zitat geprüft» heisst: "
          "das Kurzzitat steht wörtlich im Entscheid. Ob die Erwägungsnummer stimmt und die Aussage trägt, "
          "prüft die Fundstellenprüfung.\n"]
    for r in z:
        if r["klasse"] not in "AB":
            continue
        geprueft = {True: "ja", False: "**nein – vor Verwendung am Volltext prüfen**", None: "–"}[r["zitat_wortlaut_geprueft"]]
        kk.append(f"## {r['entscheid']} ({r['datum']}) – {r['klasse']}\n")
        kk.append(f"- Sachfrage: {r['sachfrage']}\n- Normstelle: {r['normstelle']}\n- Gegenstand: {r['gegenstand']}\n"
                  f"- Kernaussage: {r['kernaussage']}\n- Erwägung: {r['erwaegung']}\n- Ergebnis: {r['ergebnis']}\n"
                  f"- Fassung: {r['fassung'] or '–'}\n- Zitat: «{zelle(r['zitat'])}» (Zitat geprüft: {geprueft})")
        if r["lehre"]:
            kk.append(f"- Lehre im Entscheid: {'; '.join(r['lehre'])}")
        if r["praxis"]:
            kk.append(f"- Praxis im Entscheid: {'; '.join(r['praxis'])}")
        kk.append(f"- Volltext: {r['url']} (Cache: data/entscheide/{r['entscheid_id']}.json)\n")
    (ordner / "Karteikarten.md").write_text("\n".join(kk) + "\n", encoding="utf-8")
    return ordner


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("artikel", nargs="*")
    ap.add_argument("--alle", action="store_true")
    a = ap.parse_args()
    queue = lade_json(QUEUE)
    ids = a.artikel or ([k for k, v in queue["artikel"].items() if v["status"] == "karten"] if a.alle else [])
    if not ids:
        sys.exit("Artikel angeben oder --alle.")
    for qid in ids:
        reg = bauen(qid, queue)
        ordner = schreiben(reg)
        if queue["artikel"][qid]["status"] in ("karten", "entscheide") and not reg["fehlend"]:
            queue["artikel"][qid]["status"] = "bereit"
        print(f"{qid}: {len(reg['zeilen'])} Entscheide im Register, {len(reg['fehlend'])} ohne Karte → {ordner}")
    schreibe_json(QUEUE, queue)


if __name__ == "__main__":
    main()
