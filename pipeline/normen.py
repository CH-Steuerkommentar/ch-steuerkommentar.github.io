"""Erkennt in einem Entscheidtext die zitierten Artikel der fünf Erlasse.

Die Erkennung ist bewusst grosszügig: Sie soll keinen Entscheid übersehen. Fehltreffer
(etwa «StG» für ein kantonales Steuergesetz) sortiert die Karteikarte aus.
"""
from __future__ import annotations

import re

from config import ERLASSE

ABK_ZU_ERLASS = {}
for _key, _e in ERLASSE.items():
    for _a in _e["abk"] + _e["abk_mehrdeutig"]:
        ABK_ZU_ERLASS[_a] = _key

_ZUSATZ = r"(?:\s?(?:bis|ter|quater|quinquies|sexies|septies|octies|novies|decies)|[a-z](?:bis|ter|quater)?)?(?![a-z])"
_GLIED = (r"(?:\s*(?:Abs|al|cpv|Ziff|ch|lit|let|lett|Bst|Satz|phrase|par|Unterabs|n)\s?\.?\s*[0-9a-z]+(?:bis|ter)?\.?"
          r"(?:\s*(?:à|–|-|bis|und|et)\s*[0-9a-z]{1,3}\b\.?)?)")
_NR = r"\d{1,3}" + _ZUSATZ
_KETTE = rf"(?:\s*(?:und|et|e|bzw\.|sowie|resp\.|,|–|-)\s*(?:(?:Art|art)\.\s*)?{_NR}{_GLIED}{{0,4}})"
_ABK = "|".join(sorted(map(re.escape, ABK_ZU_ERLASS), key=len, reverse=True))

MUSTER = re.compile(
    rf"(?P<alt>\ba)?(?:Art|art|Artikel|article|articolo)s?\.?\s*(?P<nr>{_NR})(?P<glied>{_GLIED}{{0,4}})"
    rf"(?P<kette>{_KETTE}{{0,4}})\s*(?:\(\s*)?(?P<abk>{_ABK})\b"
)
_NR_IN_KETTE = re.compile(rf"(?<![\w.])({_NR})(?=\s*(?:{_GLIED}|\s|,|und|et|e|bzw|sowie|resp|–|-|$))")
_BEREICH = re.compile(r"^\s*[–-]\s*(?:(?:Art|art)\.\s*)?(\d{1,3})")


def norm_nr(nr: str) -> str:
    return re.sub(r"\s+", "", nr).lower()


def zitierte_normen(text: str) -> dict[tuple[str, str], list[str]]:
    """Gibt {(Erlass, Nummer): [Kontextausschnitte]} zurück."""
    treffer: dict[tuple[str, str], list[str]] = {}
    for m in MUSTER.finditer(text):
        erlass = ABK_ZU_ERLASS[m.group("abk")]
        nummern = [norm_nr(m.group("nr"))]
        kette = m.group("kette") or ""
        b = _BEREICH.match(kette)
        if b:  # «Art. 26–33 DBG»: nur der erste Artikel zählt als Zitat; der Bereich wird vermerkt
            pass
        else:
            for n in _NR_IN_KETTE.findall(kette):
                nummern.append(norm_nr(n))
        anfang, ende = max(0, m.start() - 220), min(len(text), m.end() + 220)
        ausschnitt = text[anfang:ende].replace("\n", " ")
        if m.group("alt"):
            ausschnitt = "[frühere Fassung] " + ausschnitt
        for n in nummern:
            liste = treffer.setdefault((erlass, n), [])
            if len(liste) < 6:
                liste.append(ausschnitt)
    return treffer


if __name__ == "__main__":
    probe = (
        "gemäss Art. 26 Abs. 1 lit. c DBG sowie Art. 9 Abs. 1 StHG; vgl. art. 26 al. 1 let. a LIFD "
        "und Art. 37a DBG, ferner Art. 26-33 DBG, aArt. 26 DBG, Art. 205bbis DBG, Art. 4 und 5 VStG, "
        "Art. 21 Abs. 1 Ziff. 2 MWSTG, § 31 StG ZH, Art. 5 StG"
    )
    for k, v in zitierte_normen(probe).items():
        print(k, "|", v[0][:60])
