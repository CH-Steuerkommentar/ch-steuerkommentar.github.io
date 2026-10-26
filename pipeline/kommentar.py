"""Liest eine Kommentierung im kanonischen Markdown-Format (siehe docs/FORMAT.md) und prüft sie.

    python3 pipeline/kommentar.py kommentare/DBG/art-26.md        # prüfen, Kennzahlen ausgeben

Andere Skripte (md2site, md2docx, pruefung) verwenden `lesen()`.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

VERZEICHNISSE = ("literaturverzeichnis", "materialienverzeichnis", "abkürzungsverzeichnis",
                 "entscheidverzeichnis")


class FormatFehler(Exception):
    pass


@dataclass
class Block:
    art: str                  # titel_norm | ueberschrift | randnote | absatz | liste | verzeichnis_eintrag | zwischentitel
    text: str = ""
    ebene: int = 0            # Überschriften: 1–4
    label: str | None = None  # Randnoten
    nummer: int | None = None
    verzeichnis: bool = False
    zeilen: list[str] = field(default_factory=list)


@dataclass
class Kommentar:
    meta: dict
    normtext: list[str]
    bloecke: list[Block]
    labels: dict[str, int]
    fussnoten: list[str]

    @property
    def randnoten(self) -> list[Block]:
        return [b for b in self.bloecke if b.art == "randnote"]


def fussnoten_finden(text: str) -> list[tuple[int, int, str]]:
    """Findet ^[…] mit ausgeglichenen eckigen Klammern. Gibt (start, ende, inhalt) zurück."""
    erg, i = [], 0
    while True:
        s = text.find("^[", i)
        if s < 0:
            return erg
        tiefe, j = 0, s + 1
        while j < len(text):
            if text[j] == "[":
                tiefe += 1
            elif text[j] == "]":
                tiefe -= 1
                if tiefe == 0:
                    break
            j += 1
        if tiefe != 0:
            raise FormatFehler(f"Fussnote nicht geschlossen: {text[s:s + 80]!r}")
        erg.append((s, j + 1, text[s + 2:j]))
        i = j + 1


def _frontmatter(roh: str) -> tuple[dict, str]:
    if not roh.startswith("---"):
        raise FormatFehler("Frontmatter fehlt (Datei muss mit --- beginnen)")
    ende = roh.find("\n---", 3)
    meta = {}
    for zeile in roh[3:ende].strip().splitlines():
        if not zeile.strip() or zeile.lstrip().startswith("#"):
            continue
        k, _, v = zeile.partition(":")
        v = v.split(" #")[0].strip().strip('"').strip("'")
        meta[k.strip()] = v
    for pflicht in ("erlass", "artikel", "stand"):
        if pflicht not in meta:
            raise FormatFehler(f"Frontmatter: «{pflicht}» fehlt")
    return meta, roh[ende + 4:]


RN = re.compile(r"^\{rn(?::([\w-]+))?\}\s*")


def lesen(pfad: Path | str) -> Kommentar:
    roh = Path(pfad).read_text(encoding="utf-8")
    meta, rumpf = _frontmatter(roh)
    absaetze = re.split(r"\n\s*\n", rumpf.strip())
    normtext, bloecke, labels = [], [], {}
    im_verzeichnis = False
    n = 0
    for a in absaetze:
        a = a.strip("\n")
        if not a.strip():
            continue
        zeilen = a.splitlines()
        if all(z.startswith(">") for z in zeilen):
            if bloecke:
                raise FormatFehler("Normtext (>-Zeilen) nur am Anfang, vor der ersten Überschrift")
            normtext += [z[1:].strip() for z in zeilen if z[1:].strip()]
            continue
        m = re.match(r"^(#{1,4})\s+(.+)$", zeilen[0])
        if m and len(zeilen) == 1:
            ebene, titel = len(m.group(1)), m.group(2).strip()
            if ebene == 1:
                im_verzeichnis = titel.lower() in VERZEICHNISSE
            if im_verzeichnis and ebene > 1:
                bloecke.append(Block("zwischentitel", titel, verzeichnis=True))
            else:
                bloecke.append(Block("ueberschrift", titel, ebene=ebene, verzeichnis=im_verzeichnis))
            continue
        if m:
            raise FormatFehler(f"Nach einer Überschrift muss eine Leerzeile folgen: {zeilen[0]!r}")
        if all(z.startswith("- ") for z in zeilen):
            art = "verzeichnis_eintrag" if im_verzeichnis else "liste"
            for z in zeilen:
                bloecke.append(Block(art, z[2:].strip(), verzeichnis=im_verzeichnis))
            continue
        # Randnote oder Absatz; Listenzeilen direkt nach dem Text gehören zur Randnote
        text_zeilen, liste = [], []
        for z in zeilen:
            (liste if z.startswith("- ") else text_zeilen).append(z[2:].strip() if z.startswith("- ") else z)
        text = " ".join(t.strip() for t in text_zeilen)
        rm = RN.match(text)
        if rm:
            n += 1
            label = rm.group(1)
            if label:
                if label in labels:
                    raise FormatFehler(f"Label doppelt: {label}")
                labels[label] = n
            bloecke.append(Block("randnote", text[rm.end():], label=label, nummer=n, zeilen=liste))
        else:
            bloecke.append(Block("absatz", text, zeilen=liste, verzeichnis=im_verzeichnis))
    # Fussnoten und Querverweise prüfen
    fussnoten = []
    for b in bloecke:
        for teil in [b.text] + b.zeilen:
            for _, _, inhalt in fussnoten_finden(teil):
                fussnoten.append(inhalt)
            for ref in re.findall(r"\{\{N:([\w-]+)\}\}", teil):
                if ref not in labels:
                    raise FormatFehler(f"Querverweis auf unbekanntes Label: {ref}")
    return Kommentar(meta, normtext, bloecke, labels, fussnoten)


VERBOTEN = re.compile(
    r"\bu\.\s?e\.|unseres erachtens|hier vertretenen|vorzugswürdig|richtigerweise|\bzu ?recht\b|"
    r"zutreffend|überzeug|verfehlt|sachgerecht|wünschenswert|\bdürfte\b|wohl kaum|\bwir\b|\bunser",
    re.IGNORECASE)


def pruefen(k: Kommentar) -> list[str]:
    befunde = []
    for b in k.bloecke:
        if b.art == "randnote":
            fett = re.findall(r"\*\*[^*]+\*\*", re.sub(r"\^\[.*?\]", "", b.text))
            if len(fett) != 1:
                befunde.append(f"N. {b.nummer}: {len(fett)} fette Stichwörter (verlangt: genau eines)")
            if "==" in b.text:
                befunde.append(f"N. {b.nummer}: gelbe Markierung (==) gefunden")
        if b.art in ("absatz", "liste") and not b.verzeichnis:
            befunde.append(f"Text ohne Randnote (jeder Absatz im Kommentartext beginnt mit {{rn}}): {b.text[:60]!r}")
        for teil in [b.text] + b.zeilen:
            ohne_fn = teil
            for s, e, inh in reversed(fussnoten_finden(teil)):
                if not inh.rstrip().endswith((".", ".»", ".)")):
                    befunde.append(f"Fussnote ohne Schlusspunkt: {inh[:60]!r}")
                ohne_fn = ohne_fn[:s] + ohne_fn[e:]
            for m in VERBOTEN.finditer(ohne_fn):
                if b.art != "verzeichnis_eintrag":
                    befunde.append(f"Wertende Wendung «{m.group(0)}»: {ohne_fn[max(0, m.start()-50):m.end()+30]!r}")
            if "—" in teil:
                befunde.append(f"Geviertstrich «—» statt «–»: {teil[:60]!r}")
            if "ß" in teil:
                befunde.append(f"«ß» statt «ss»: {teil[:60]!r}")
    if not k.bloecke or k.bloecke[0].art != "ueberschrift" or k.bloecke[0].text.lower() != "übersicht":
        befunde.append("Erstes Kapitel muss «# Übersicht» heissen")
    if not k.normtext:
        befunde.append("Normtext fehlt")
    return befunde


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    fehler = 0
    for p in sys.argv[1:]:
        try:
            k = lesen(p)
        except FormatFehler as e:
            print(f"{p}: FORMATFEHLER – {e}")
            fehler += 1
            continue
        bef = pruefen(k)
        print(f"{p}: {len(k.randnoten)} Randnoten, {len(k.fussnoten)} Fussnoten, {len(bef)} Befunde")
        for b in bef:
            print("  -", b)
        fehler += bool(bef)
    sys.exit(1 if fehler else 0)


if __name__ == "__main__":
    main()
