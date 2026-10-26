"""Übernimmt eine bestehende Kommentierung aus Word (OK-Vorlage, gebaut mit dem OK-Builder)
in das Markdown-Format von docs/FORMAT.md.

    python3 pipeline/docx2md.py Art_9_DBG_Kommentierung.docx --erlass DBG --artikel 9 [--stand 2026-10-21]

Ergebnis: kommentare/<Erlass>/art-<N>.md. Danach mit pipeline/kommentar.py prüfen.
Querverweise («N. 15») bleiben Text; Randnoten erhalten die Labels n1, n2, …
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import INVENTAR, KOMMENTARE, art_slug, lade_json  # noqa: E402

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
VERZ = {"literaturverzeichnis", "materialienverzeichnis", "abkürzungsverzeichnis", "entscheidverzeichnis"}


def run_text(r, fussnoten: dict[str, str]) -> str:
    teile = []
    for el in r:
        if el.tag == W + "t":
            teile.append(el.text or "")
        elif el.tag == W + "tab":
            teile.append(" ")
        elif el.tag in (W + "br", W + "cr"):
            teile.append(" ")
        elif el.tag == W + "footnoteReference":
            teile.append(f"^[{fussnoten.get(el.get(W + 'id'), '')}]")
    text = "".join(teile)
    rpr = r.find(W + "rPr")
    if rpr is not None and "^[" not in text and text.strip():
        fett = rpr.find(W + "b") is not None and rpr.find(W + "b").get(W + "val") not in ("0", "false")
        kursiv = rpr.find(W + "i") is not None and rpr.find(W + "i").get(W + "val") not in ("0", "false")
        if fett or kursiv:
            m = re.match(r"^(\s*)(.*?)(\s*)$", text, re.S)
            zeichen = "**" if fett else "*"
            text = f"{m.group(1)}{zeichen}{m.group(2)}{zeichen}{m.group(3)}"
    return text


def absatz_text(p, fussnoten) -> str:
    text = "".join(run_text(r, fussnoten) for r in p.iter(W + "r"))
    text = re.sub(r"\*\*(\s*)\*\*", r"\1", text)     # aneinanderstossende Fettungen zusammenführen
    return re.sub(r"[ \t]+", " ", text).strip()


def stil(p) -> str:
    ps = p.find(W + "pPr/" + W + "pStyle")
    return ps.get(W + "val") if ps is not None else ""


def nur_fett(p) -> bool:
    runs = [r for r in p.iter(W + "r") if "".join(t.text or "" for t in r.iter(W + "t")).strip()]
    return bool(runs) and all(r.find(W + "rPr/" + W + "b") is not None for r in runs)


def lesen_fussnoten(z: zipfile.ZipFile) -> dict[str, str]:
    if "word/footnotes.xml" not in z.namelist():
        return {}
    root = ET.fromstring(z.read("word/footnotes.xml"))
    erg = {}
    for fn in root.findall(W + "footnote"):
        fid = fn.get(W + "id")
        if fn.get(W + "type") in ("separator", "continuationSeparator"):
            continue
        teile = [absatz_text(p, {}) for p in fn.iter(W + "p")]
        erg[fid] = " ".join(t for t in teile if t).strip()
    return erg


def ebene(stilname: str, stile: dict[str, str]) -> int | None:
    name = stile.get(stilname, stilname).lower()
    m = re.search(r"(?:heading|überschrift)\s*(\d)", name)
    return int(m.group(1)) if m else None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx")
    ap.add_argument("--erlass", required=True)
    ap.add_argument("--artikel", required=True)
    ap.add_argument("--stand")
    ap.add_argument("--titel")
    a = ap.parse_args()

    z = zipfile.ZipFile(a.docx)
    fussnoten = lesen_fussnoten(z)
    stile = {}
    if "word/styles.xml" in z.namelist():
        for s in ET.fromstring(z.read("word/styles.xml")).findall(W + "style"):
            n = s.find(W + "name")
            stile[s.get(W + "styleId")] = n.get(W + "val") if n is not None else s.get(W + "styleId")
    body = ET.fromstring(z.read("word/document.xml")).find(W + "body")

    norm, aus = [], []
    titel_gesehen = text_begonnen = im_verz = False
    n = 0
    for p in body.iter(W + "p"):
        if stil(p).lower().startswith(("toc", "verzeichnis")) or stile.get(stil(p), "").lower().startswith(("toc", "verzeichnis 1", "inhaltsverzeichnis")):
            continue
        t = absatz_text(p, fussnoten)
        if not t or t.strip("*") == "Inhaltsverzeichnis":
            continue
        e = ebene(stil(p), stile)
        if e == 1 and not titel_gesehen:
            titel_gesehen = True
            continue
        if e and e >= 2:
            text_begonnen = True
            ueb = re.sub(r"^\*\*(.*)\*\*$", r"\1", t)
            im_verz = ueb.lower() in VERZ
            aus.append("#" * (e - 1) + " " + ueb)
            continue
        if not text_begonnen:
            norm.append(re.sub(r"\*\*", "", t))
            continue
        if im_verz:
            if nur_fett(p) and len(t) < 60:
                aus.append("## " + t.strip("*"))
            else:
                aus.append("- " + t)
            continue
        m = re.match(r"^#(\d+)#\s*", t)
        if m:
            n += 1
            aus.append(f"{{rn:n{n}}} " + t[m.end():])
        else:
            aus.append(f"{{rn:n{n + 1}}} " + t)
            n += 1

    sach = a.titel
    if not sach:
        inv = lade_json(INVENTAR / f"{a.erlass}.json", {"artikel": []})
        sach = next((x["sachueberschrift"] for x in inv["artikel"] if x["nummer"].lower() == a.artikel.lower()), "")
        if norm:
            m = re.match(rf"^Art\.\s*{re.escape(a.artikel)}\s+(.*)$", norm[0])
            if m:
                sach = m.group(1)
    stand = a.stand or (re.search(r"(\d{4}-\d{2}-\d{2})", Path(a.docx).name) or [None, ""])[1]
    kopf = ["---", f"erlass: {a.erlass}", f'artikel: "{a.artikel}"', f"titel: {sach}", f"stand: {stand}", "---", ""]
    normzeilen = []
    for i, z_ in enumerate(norm):
        normzeilen.append("> " + (f"**{z_}**" if i == 0 else z_))
    # Verzeichniseinträge und Listenzeilen ohne Leerzeile dazwischen, alles andere mit
    blocks, puffer = [], []
    for zeile in aus:
        if zeile.startswith("- "):
            puffer.append(zeile)
            continue
        if puffer:
            blocks.append("\n".join(puffer))
            puffer = []
        blocks.append(zeile)
    if puffer:
        blocks.append("\n".join(puffer))
    ziel = KOMMENTARE / a.erlass / f"{art_slug(a.artikel)}.md"
    ziel.parent.mkdir(parents=True, exist_ok=True)
    ziel.write_text("\n".join(kopf) + "\n".join(normzeilen) + "\n\n" + "\n\n".join(blocks) + "\n", encoding="utf-8")
    print(f"{ziel}: {n} Randnoten, {len(fussnoten)} Fussnoten")


if __name__ == "__main__":
    main()
