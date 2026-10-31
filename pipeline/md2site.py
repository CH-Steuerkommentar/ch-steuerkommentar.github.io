"""Website-Inhalte erzeugen: wandelt jede Kommentierung in kommentare/ in eine Seite der
Website um und baut die Übersichtsseiten je Erlass und die Startseite neu.

    python3 pipeline/md2site.py             # alles neu erzeugen
    python3 pipeline/md2site.py --pruefen   # nur Format und Neutralität prüfen, nichts schreiben

Eine Kommentierung mit Befunden aus der Formatprüfung wird nicht veröffentlicht.
"""
from __future__ import annotations

import argparse
from datetime import date
import html
import datetime as dt
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import (ausgenommen, ERLASSE, INVENTAR, KOMMENTARE, KOMMENTARE_FR, QUEUE, SITE_DOCS, WERK, WERK_FR,  # noqa: E402
                    WERK_KURZ, WERK_KURZ_FR, art_slug, art_sortkey, lade_json)  # noqa: E402
from kommentar import FormatFehler, fussnoten_finden, lesen, pruefen  # noqa: E402

# Nur Kommentierungen mit diesem Status kommen auf die Website (Entwürfe und laufende Arbeit nicht).
VEROEFFENTLICHEN = {"geprueft", "veroeffentlicht"}

ROEMISCH = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV",
            "XVI", "XVII", "XVIII", "XIX", "XX"]


def nummer(ebene: int, zaehler: list[int]) -> str:
    n = zaehler[ebene - 1]
    if ebene == 1:
        return ROEMISCH[n - 1] + "."
    if ebene == 2:
        return chr(ord("A") + n - 1) + "."
    if ebene == 3:
        return f"{n}."
    return chr(ord("a") + n - 1) + "."


def datum_ch(iso: str) -> str:
    try:
        d = dt.date.fromisoformat(iso)
        return f"{d.day}.{d.month}.{d.year}"
    except ValueError:
        return iso


def yaml_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def order(nummer_art: str) -> int:
    k = art_sortkey(nummer_art)
    return k[0] * 100 + (k[1] if isinstance(k[1], int) else 99)


OCL = "https://mcp.opencaselaw.ch/entscheid/"

# Texte der Website in beiden Sprachen
T = {
    "de": {
        "banner": "Mit KI erstellt und am Volltext der Quellen geprüft. Stand: {stand}. Keine Rechtsberatung.",
        "zitat": "{werk}, Art. {art} {abk} N. [Randnote] (Stand {stand})",
        "zitat_label": "Zitiervorschlag:", "kopieren": "Kopieren", "kopiert": "Kopiert",
        "beschreibung": "Beitrag zu Art. {art} {abk}",
        "randnote": "Randnote",
    },
    "fr": {
        "banner": "Rédigé par une IA et vérifié sur le texte intégral des sources. État : {stand}. Ne constitue pas un conseil juridique.",
        "zitat": "{werk}, art. {art} {abk} N [note marginale] (état au {stand})",
        "zitat_label": "Proposition de citation :", "kopieren": "Copier", "kopiert": "Copié",
        "beschreibung": "Contribution à l'art. {art} {abk}",
        "randnote": "Note marginale",
    },
}


def abk(erlass: str, lang: str) -> str:
    return ERLASSE[erlass]["kurz_fr"] if lang == "fr" else erlass


def erlass_name(erlass: str, lang: str) -> str:
    return ERLASSE[erlass]["name_fr"] if lang == "fr" else ERLASSE[erlass]["name"]


def beitragsverweise(text: str) -> str:
    """Eigenverweise auf Beiträge umbenennen; Titel zitierter Werke bleiben erhalten."""
    text = re.sub(r"\bdie Kommentierung(?= zu Art\.)", "den Beitrag", text)
    text = re.sub(r"\bdie Kommentierungen(?= zu Art\.)", "die Beiträge", text)
    text = re.sub(
        r"\ble commentaire de (l[’']art\.\s*\d+[a-z]*(?:,\s*al\.\s*\d+)?[,]?\s+(?:LIFD|LHID|LIA|LTVA|LT)\b)",
        r"la contribution relative à \1", text)
    return re.sub(
        r"\bles commentaires des (art\.\s*\d+[a-z]*(?:\s+et\s+\d+[a-z]*)?\s+(?:LIFD|LHID|LIA|LTVA|LT)\b)",
        r"les contributions relatives aux \1", text)


_BGE = re.compile(r"\b(?:BGE|ATF)\s+(\d{2,3})\s+(Ia|Ib|IV|V|III|II|I)\s+(\d{1,4})\b")
_BGER = re.compile(r"(?<![\w/.])(\d{1,2}[A-Z]{1,2}[_.]\d{1,5}/\d{4})\b")


def _link(text: str, url: str) -> str:
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'


def entscheid_links(text: str) -> str:
    """BGE- und BGer-Zitate in Fussnoten auf den Entscheid bei Open Case Law verlinken (neuer Tab).
    Bestehende Links (Markdown oder HTML) bleiben unverändert."""
    teile = re.split(r"(\[[^\]]*\]\([^)]*\)|<a\b[^>]*>.*?</a>)", text)
    aus = []
    for i, t in enumerate(teile):
        if i % 2:
            aus.append(t)
            continue
        t = _BGE.sub(lambda m: _link(m.group(0), OCL + "bge_" + f"{m.group(1)} {m.group(2)} {m.group(3)}".replace(" ", "%20")), t)
        t = re.sub(r"(<a\b[^>]*>.*?</a>)|" + _BGER.pattern,
                   lambda m: m.group(1) or _link(m.group(2), OCL + "bger_" + m.group(2).replace("/", "_")), t)
        aus.append(t)
    return "".join(aus)


class Umwandler:
    def __init__(self, k, lang: str = "de"):
        self.k = k
        self.lang = lang
        self.fn: list[str] = []

    def inline(self, text: str) -> str:
        text = beitragsverweise(text)
        # Fussnoten durch [^n] ersetzen (von hinten, damit Positionen stimmen)
        teile, pos = [], 0
        for s, e, inhalt in fussnoten_finden(text):
            teile.append(text[pos:s])
            self.fn.append(entscheid_links(self.querverweise(inhalt)))
            teile.append(f"[^{len(self.fn)}]")
            pos = e
        teile.append(text[pos:])
        return self.querverweise("".join(teile))

    def querverweise(self, text: str) -> str:
        return re.sub(r"\{\{N:([\w-]+)\}\}", lambda m: f"[{self.k.labels[m.group(1)]}](#n{self.k.labels[m.group(1)]})", text)

    def seite(self, pfad_quelle: Path) -> str:
        k, m = self.k, self.k.meta
        tx = T[self.lang]
        erlass, art = m["erlass"], m["artikel"]
        ab = abk(erlass, self.lang)
        titel = m.get("titel", "")
        stand = datum_ch(m["stand"])
        aus = []
        aus.append("---")
        aus.append(f"title: {yaml_str(f'Art. {art} {ab}')}")
        aus.append(f"description: {yaml_str((tx['beschreibung'].format(art=art, abk=ab) + ' – ' + titel).strip(' –'))}")
        aus.append("sidebar:")
        aus.append(f"  label: {yaml_str(f'Art. {art} – {titel}' if titel else f'Art. {art}')}")
        aus.append(f"  order: {order(art)}")
        aus.append("banner:")
        aus.append(f"  content: {yaml_str(tx['banner'].format(stand=stand))}")
        aus.append(f"lastUpdated: {m['stand']}")
        aus.append("---\n")
        zitat = tx["zitat"].format(werk=WERK_KURZ_FR if self.lang == "fr" else WERK_KURZ, art=art, abk=ab, stand=stand)
        aus.append(f'<aside class="zitiervorschlag"><span><strong>{tx["zitat_label"]}</strong> <span class="zitat">{zitat}</span>'
                   + f'</span><button type="button" class="kopieren" data-text="{html.escape(zitat, quote=True)}" '
                   f'data-label="{tx["kopieren"]}" data-ok="{tx["kopiert"]}">{tx["kopieren"]}</button></aside>\n')
        # Normtext
        aus.append('<div class="normtext">\n')
        for i, z in enumerate(k.normtext):
            z = z.replace("**", "")
            if i == 0:
                aus.append(f"**{z}**\n")
                continue
            mz = re.match(r"^(\d+[a-z]*(?:bis|ter)?)\s+(.*)$", z)
            if mz:
                aus.append(f'<sup>{mz.group(1)}</sup> {mz.group(2)}\n')
            elif re.match(r"^[a-z]+\.\s", z) or re.match(r"^\d+\.\s", z):
                aus.append(f'<span class="norm-bst">{z}</span>\n')
            else:
                aus.append(z + "\n")
        aus.append("</div>\n")
        # Text
        zaehler = [0, 0, 0, 0]
        hinweis_gesetzt = False
        for b in k.bloecke:
            if b.art == "ueberschrift":
                if b.verzeichnis and b.ebene == 1:
                    if not hinweis_gesetzt:
                        aus.append(fehler_melden(erlass, art, self.lang))
                        aus.append(ile_hinweis(k, self.lang))
                        hinweis_gesetzt = True
                    aus.append(f"## {b.text}\n")
                    continue
                zaehler[b.ebene - 1] += 1
                for j in range(b.ebene, 4):
                    zaehler[j] = 0
                aus.append(f"{'#' * (b.ebene + 1)} {nummer(b.ebene, zaehler)} {self.inline(b.text)}\n")
            elif b.art == "zwischentitel":
                aus.append(f"### {b.text}\n")
            elif b.art == "randnote":
                n = b.nummer
                aus.append(f'<span class="rn" id="n{n}" data-pagefind-ignore><a href="#n{n}" aria-label="{tx['randnote']} {n}">{n}</a></span> '
                           f"{self.inline(b.text)}")
                if b.zeilen:
                    aus.append("\n" + "\n".join(f"- {self.inline(z)}" for z in b.zeilen))
                aus.append("\n")
            elif b.art in ("liste", "verzeichnis_eintrag"):
                aus.append(f"- {self.inline(b.text)}")
            elif b.art == "absatz":
                aus.append(self.inline(b.text) + "\n")
                if b.zeilen:
                    aus.append("\n".join(f"- {self.inline(z)}" for z in b.zeilen) + "\n")
        if not hinweis_gesetzt:
            aus.append(fehler_melden(erlass, art, self.lang))
            aus.append(ile_hinweis(k, self.lang))
        aus.append(weiterfuehrende_literatur(k, self.lang))
        text = "\n".join(aus)
        text = re.sub(r"(\n- [^\n]*)\n(?=[^-\n])", r"\1\n\n", text)
        text += "\n\n" + "\n".join(f"[^{i}]: {inh}" for i, inh in enumerate(self.fn, 1)) + "\n"
        return text


ILE_DATEN = Path(__file__).resolve().parent.parent / "site" / "src" / "data" / "ile.json"
KATALOG = Path(__file__).resolve().parent.parent / "daten" / "ile-literatur" / "katalog.json"
_katalog: dict[str, list[str]] | None = None


def _werkschluessel(zitat: str) -> tuple[str, str]:
    """Erster Nachname und erstes längeres Titelwort, klein geschrieben (für den Abgleich mit dem Literaturverzeichnis)."""
    teile = [t.strip() for t in zitat.split(",")]
    name = re.findall(r"[A-Za-zÄÖÜäöüßéèêàâçëïôûñ'’\-]+", teile[0])
    titel = teile[1] if len(teile) > 1 else ""
    wort = next((w for w in re.findall(r"[A-Za-zÄÖÜäöüßéèêàâç\-]{6,}", titel)), "")
    return (name[0].lower() if name else "", wort.lower())


def katalog_je_artikel() -> dict[str, list[dict]]:
    """ILE-Literaturkatalog je Bestimmung («DBG 18» -> Werke), ILE-Werke zuerst."""
    global _katalog
    if _katalog is None:
        _katalog = {}
        for e in lade_json(KATALOG, []):
            for a in e.get("artikel", []):
                _katalog.setdefault(a, []).append(e)
        for ws in _katalog.values():
            ws.sort(key=lambda e: (not e.get("ile"), e["zitat"].lower()))
    return _katalog


def _literatur_zeile(e: dict) -> str:
    z = html.escape(e["zitat"], quote=False)
    if e.get("ile") and e.get("url"):
        return f'- <a href="{html.escape(e["url"])}" target="_blank" rel="noopener">{z}</a> <span class="ile-marke">ILE</span>'
    if e.get("ile"):
        return f'- {z} <span class="ile-marke">ILE</span>'
    return f"- {z}"


def weiterfuehrende_literatur(k, lang: str = "de") -> str:
    """Schlussabschnitt: Werke aus dem ILE-Literaturkatalog zu diesem Artikel, die nicht schon zitiert sind."""
    werke = katalog_je_artikel().get(f"{k.meta['erlass']} {k.meta['artikel']}", [])
    if not werke:
        return ""
    zitiert = " ".join(b.text for b in k.bloecke).lower()
    neu = []
    for e in werke:
        name, wort = _werkschluessel(e["zitat"])
        if name and name in zitiert and (not wort or wort in zitiert):
            continue
        if e.get("url") and e["url"].lower() in zitiert:
            continue
        neu.append(e)
    if not neu:
        return ""
    if lang == "fr":
        titel = "Bibliographie complémentaire"
        satz = ("Autres publications pertinentes pour cette disposition, tirées des publications de l'ILE-HSG et de leurs "
                "bibliographies, non citées ci-dessus.")
    else:
        titel = "Weiterführende Literatur"
        satz = ("Weitere einschlägige Publikationen zu dieser Bestimmung aus den Publikationen des ILE-HSG und deren "
                "Literaturverzeichnissen und Fussnoten, die oben nicht zitiert sind.")
    return (f"\n## {titel}\n\n<p class=\"weiterfuehrend-hinweis\">{satz}</p>\n\n"
            + "\n".join(_literatur_zeile(e) for e in neu) + "\n")


def literatur_seite(erlass: str, nummer: str, sachueberschrift: str, lang: str = "de") -> str:
    """Seite für einen noch nicht kommentierten Artikel: nur die Literatur aus dem ILE-Katalog."""
    werke = katalog_je_artikel().get(f"{erlass} {nummer}", [])
    ab = abk(erlass, lang)
    if lang == "fr":
        hinweis = ("Aucune contribution n'est encore disponible pour cet article. En attendant, voici les publications pertinentes tirées des "
                   "publications de l'ILE-HSG et de leurs bibliographies.")
        titel = "Bibliographie"
    else:
        hinweis = ("Zu diesem Artikel liegt noch kein Beitrag vor. Bis dahin finden Sie hier die einschlägige Literatur aus "
                   "den Publikationen des ILE-HSG und deren Literaturverzeichnissen.")
        titel = "Literatur"
    zeilen = ["---", f"title: {yaml_str(f'Art. {nummer} {ab}')}",
              f"description: {yaml_str(f'{titel} – Art. {nummer} {ab}' + (f' – {sachueberschrift}' if sachueberschrift else ''))}",
              "sidebar:", f"  label: {yaml_str(f'Art. {nummer} – {sachueberschrift}' if sachueberschrift else f'Art. {nummer}')}",
              f"  order: {order(nummer)}", "  attrs:", "    class: nur-literatur", "---\n",
              f'<p class="weiterfuehrend-hinweis">{hinweis}</p>\n', f"## {titel}\n"]
    zeilen += [_literatur_zeile(e) for e in werke]
    zeilen.append(fehler_melden(erlass, nummer, lang))
    return "\n".join(zeilen) + "\n"


def ile_daten() -> dict:
    d = lade_json(ILE_DATEN, {})
    heute = date.today().isoformat()
    d["naechste"] = [s for s in d.get("seminare", []) if s.get("bis", "") >= heute][:2]
    return d


def fehler_melden(erlass: str, art: str, lang: str = "de") -> str:
    """Kleiner Hinweis am Ende des Kommentartexts: Fehler per E-Mail melden (Betreff vorausgefüllt)."""
    from urllib.parse import quote
    if lang == "fr":
        betreff = f"[StE] Signalement art. {art} {abk(erlass, lang)}"
        text = "Vous avez trouvé une erreur ? "
        link = "Signalez-la-nous"
    else:
        betreff = f"[StE] Hinweis Art. {art} {erlass}"
        text = "Fehler gefunden? "
        link = "Hinweis an das ILE-HSG senden"
    return (f'\n<p class="fehler-melden">{text}<a href="mailto:sekretariat-ile@unisg.ch?subject={quote(betreff)}">'
            f'{link}</a></p>\n')


def ile_hinweis(k, lang: str = "de") -> str:
    """Kasten unter der Kommentierung: wie viele Publikationen des ILE-HSG sie stützen, mit Links."""
    d = ile_daten()
    if not d:
        return ""
    eintraege, in_lit = [], False
    for b in k.bloecke:
        if b.art == "ueberschrift" and b.verzeichnis and b.ebene == 1:
            in_lit = b.text.strip().lower().startswith(("literatur", "bibliographie"))
        elif in_lit and b.art == "verzeichnis_eintrag":
            eintraege.append(b.text)
    # Publikationen des ILE-HSG im Literaturverzeichnis zählen (alle Arten, nicht nur FStR)
    ARTEN = [  # (Muster, deutsch, französisch)
        (r"\bFStR\s+\d{4}", "Forum für Steuerrecht", "Forum für Steuerrecht"),
        (r"Schriftenreihe Finanzwissenschaft|IFF-Schriftenreihe|IFF-Forum|Schriftenreihe IFF|Handbuch zum Mehrwertsteuergesetz", "Schriftenreihe Finanzwissenschaft und Finanzrecht", "Schriftenreihe Finanzwissenschaft und Finanzrecht"),  # Reihe des IFF, Vorgänger des ILE
        (r"Working Paper", "ILE Working Papers", "ILE Working Papers"),  # z.B. «ILE Working Paper 2024-19», «ILE-HSG Working Paper No. 2026-31»
        (r"Seminarunterlage|support de séminaire|Steuerseminar|Seminar\b", "St.Galler Seminare", "séminaires de Saint-Gall"),
    ]
    n, arten = 0, []
    for e in eintraege:
        treffer = next((a for a in ARTEN if re.search(a[0], e)), None)
        if treffer is None and "e_sys=ile" in e:
            # übrige Werke aus der ILE-Sammlung in Lexplorer sind Bände der Schriftenreihe Finanzwissenschaft und Finanzrecht
            # (das Lehrbuch Hongler/Lorenz wird nicht zitiert)
            treffer = ARTEN[1]
        if treffer is None:
            continue
        n += 1
        name = treffer[2] if lang == "fr" else treffer[1]
        if name and name not in arten:
            arten.append(name)
    arten.sort(key=lambda a: [x[2] if lang == "fr" else x[1] for x in ARTEN].index(a))
    klammer = f" ({', '.join(arten)})" if arten else ""
    if lang == "fr":
        titel, abo, sem_knopf = "Approfondir avec l'ILE-HSG", "S'abonner à la FStR", "Séminaires"
        if n:
            satz = (f"Cette contribution s'appuie sur {n} publication{'s' if n > 1 else ''} de l'ILE-HSG{klammer}. "
                    "La FStR est la revue spécialisée de l'ILE-HSG ; les séminaires de Saint-Gall traitent des questions "
                    "actuelles de la pratique.")
        else:
            satz = ("Le Forum für Steuerrecht (FStR) est la revue spécialisée de l'ILE-HSG en droit fiscal suisse et "
                    "international ; les séminaires de Saint-Gall traitent des questions actuelles de la pratique.")
    else:
        titel, abo, sem_knopf = "Vertiefung beim ILE-HSG", "FStR abonnieren", "Seminare"
        if n:
            satz = (f"Dieser Beitrag stützt sich auf {n} {'Publikation' if n == 1 else 'Publikationen'} des ILE-HSG{klammer}. "
                    "Das FStR ist die Fachzeitschrift des ILE-HSG; die St.Galler Seminare greifen aktuelle Fragen der Praxis auf.")
        else:
            satz = ("Das Forum für Steuerrecht (FStR) ist die Fachzeitschrift des ILE-HSG zum Schweizer und internationalen "
                    "Steuerrecht; die St.Galler Seminare greifen aktuelle Fragen der Praxis auf.")
    knoepfe = [f'<a class="ile-knopf" href="{d["fstr"]["url"]}" target="_blank" rel="noopener">{abo}</a>']
    for s in d["naechste"]:
        datum = s.get("datum_fr", s["datum"]) if lang == "fr" else s["datum"]
        knoepfe.append(f'<a class="ile-knopf zweit" href="{s["url"]}" target="_blank" rel="noopener">'
                       f'{html.escape(s["kurz"])} · {html.escape(datum)}</a>')
    if not d["naechste"]:
        knoepfe.append(f'<a class="ile-knopf zweit" href="{d["seminare_url"]}" target="_blank" rel="noopener">{sem_knopf}</a>')
    return (f'\n<aside class="ile-hinweis" aria-label="{titel}">'
            f'<p class="ile-hinweis-titel">{titel}</p>'
            f'<p>{html.escape(satz)}</p><p class="ile-knoepfe">{"".join(knoepfe)}</p></aside>\n')


def erlass_seite(erlass: str, kommentiert: dict[str, dict], lang: str = "de", deutsch: dict[str, dict] | None = None,
                 literatur: set[str] | None = None) -> str:
    """Übersicht je Erlass. `kommentiert`: Kommentierungen in dieser Sprache; `deutsch` (nur fr): deutsche Kommentierungen,
    die noch nicht übersetzt sind und auf der französischen Seite deutsch angezeigt werden."""
    inv = lade_json(INVENTAR / f"{erlass}.json", {"artikel": [], "fassung_vom": "", "quelle": ""})
    e = ERLASSE[erlass]
    deutsch = deutsch or {}
    gesamt = sum(1 for a in inv["artikel"] if not a["aufgehoben"] and not ausgenommen(erlass, a["nummer"]))
    eli = e["eli"].split("/eli/cc/")[1]
    if lang == "fr":
        ab = e["kurz_fr"]
        kopf = [f"{e['name_fr']} (RS {e['sr']}), version du {datum_ch(inv.get('fassung_vom', ''))} "
                f"([Fedlex](https://www.fedlex.admin.ch/eli/cc/{eli}/fr)).\n",
                f"{len(kommentiert)} articles traités en français et {len(deutsch)} en allemand, sur {gesamt} articles en vigueur. "
                "Les dispositions finales et transitoires ainsi que celles relatives au référendum et à l'entrée en vigueur ne sont pas traitées.\n",
                "| Article | Titre | État |", "|---|---|---|"]
        label, nicht, nur_lit = "Aperçu", "non traité", "bibliographie"
    else:
        ab = erlass
        kopf = [f"{e['name']} (SR {e['sr']}), Fassung vom {datum_ch(inv.get('fassung_vom', ''))} "
                f"([Fedlex](https://www.fedlex.admin.ch/eli/cc/{eli}/de)).\n",
                f"{len(kommentiert)} von {gesamt} geltenden Artikeln bearbeitet. Schluss- und Übergangsbestimmungen sowie "
                "Referendum und Inkrafttreten werden nicht bearbeitet.\n",
                "| Artikel | Sachüberschrift | Stand |", "|---|---|---|"]
        label, nicht, nur_lit = "Übersicht", "nicht bearbeitet", "Literatur"
    zeilen = ["---", f"title: {yaml_str(ab)}", f"description: {yaml_str(erlass_name(erlass, lang))}",
              "sidebar:", f"  label: {label}", "  order: 0", "prev: false", "---\n"] + kopf
    for a in sorted(inv["artikel"], key=lambda a: art_sortkey(a["nummer"])):
        if a["aufgehoben"]:
            continue
        slug = art_slug(a["nummer"])
        artikel_nr = f'<span class="artikel-nummer">Art. {html.escape(a["nummer"])}</span>'
        if slug in kommentiert:
            titel = kommentiert[slug].get("titel") or a["sachueberschrift"]
            zeilen.append(f"| [{artikel_nr}](./{slug}/) | {titel} | {datum_ch(kommentiert[slug]['stand'])} |")
        elif slug in deutsch:
            zeilen.append(f"| [{artikel_nr}](./{slug}/) | {a['sachueberschrift']} | en allemand, {datum_ch(deutsch[slug]['stand'])} |")
        elif ausgenommen(erlass, a["nummer"]):
            zeilen.append(f"| {artikel_nr} | {a['sachueberschrift']} | {nicht} |")
        elif literatur and slug in literatur:
            zeilen.append(f"| [{artikel_nr}](./{slug}/) | {a['sachueberschrift']} | {nur_lit} |")
        else:
            zeilen.append(f"| {artikel_nr} | {a['sachueberschrift']} | – |")
    return "\n".join(zeilen) + "\n"


START = {
    "de": {
        "leitsatz": "Rechtsprechung, Verwaltungspraxis und Lehre – bei der jeweiligen Norm.",
        "intro": "Die St. Galler Steuerrechtsenzyklopädie ist ein frei zugängliches Nachschlagewerk zum Schweizer Steuerrecht. "
                 "Zu den bearbeiteten Gesetzesartikeln gibt sie wieder, was Gerichte, Steuerbehörden und die ausgewertete "
                 "Literatur sagen. Das Werk wird schrittweise erweitert.",
        "angebote_titel": "Was die Enzyklopädie bietet",
        "angebote": [
            ("Orientierung entlang des Gesetzes", "Die Inhalte sind nach Gesetzesartikeln geordnet. Begriffe und Rechtsfragen "
             "werden im Zusammenhang mit der jeweiligen Bestimmung erläutert."),
            ("Im Original ausgewertete Quellen", "Die Darstellung stützt sich auf Rechtsprechung, Verwaltungspraxis und "
             "Publikationen des ILE-HSG, die im Volltext ausgewertet und an der betreffenden Stelle in den Fussnoten zitiert werden."),
            ("Weiterführende Literatur", "Am Ende der Beiträge werden zusätzliche Veröffentlichungen aufgeführt, die anhand "
             "ihrer Titel dem Thema zugeordnet wurden. Ihre Inhalte wurden für den Beitrag nicht ausgewertet."),
            ("Aktuelle Inhalte", "Jeder Beitrag weist seinen aktuellen Bearbeitungsstand aus. Die Inhalte werden laufend "
             "automatisiert aktualisiert, sodass neue Entwicklungen zeitnah berücksichtigt und der Stand der Bearbeitung "
             "transparent nachvollziehbar bleibt."),
        ],
        "zielgruppe": "Die Enzyklopädie richtet sich an Fachpersonen in Beratung, Verwaltung, Justiz und Unternehmen sowie "
                      "an Forschende und Studierende. Sie unterstützt den Einstieg in ein Thema ebenso wie die gezielte "
                      "Recherche zu einer einzelnen Bestimmung.",
        "hinweis_titel": "Hinweis zur Erstellung",
        "hinweis": "Die Inhalte werden mit künstlicher Intelligenz erstellt und automatisiert geprüft. Vor der Veröffentlichung "
                   "findet keine menschliche Durchsicht statt. Fehler und Lücken sind möglich. Massgebend bleiben die "
                   "Originalquellen und die aktuelle Rechtslage.",
        "ueber": "Über die St. Galler Steuerrechtsenzyklopädie", "erlasse": "Erlasse", "n_bearbeitet": "{n} Artikel bearbeitet",
        "ile": "Vom ILE-HSG", "fstr_zusatz": " Die Beiträge stützen sich auf die Publikationen des ILE-HSG. Abonnenten des FStR haben über die Plattform Lexplorer Zugriff auf diese Publikationen.",
        "abo": "FStR abonnieren", "sem_titel": "St.Galler Seminare", "sem_naechste": "Die nächsten Seminare des Instituts:",
        "sem_alle": "Alle Seminare", "tax_knopf": "Zum Fachbereich",
        "mehr": "Mehr zur Arbeitsweise", "zahl": "Bearbeitete Artikel", "von": "von {g} geltenden Artikeln",
    },
    "fr": {
        "leitsatz": "Jurisprudence, pratique administrative et doctrine – à la disposition concernée.",
        "intro": "L'Encyclopédie de droit fiscal de Saint-Gall est un ouvrage de référence en libre accès consacré au droit "
                 "fiscal suisse. Pour les articles de loi traités, elle rapporte ce que disent les tribunaux, les autorités "
                 "fiscales et la littérature analysée. L'ouvrage est progressivement enrichi.",
        "angebote_titel": "Ce que propose l'Encyclopédie",
        "angebote": [
            ("Une orientation fondée sur la loi", "Les contenus sont organisés par article de loi. Les notions et questions "
             "juridiques sont présentées dans le contexte de la disposition concernée."),
            ("Des sources analysées dans leur texte intégral", "La présentation repose sur la jurisprudence, la pratique "
             "administrative et les publications de l'ILE-HSG, analysées dans leur texte intégral et citées en note de bas "
             "de page à l'endroit concerné."),
            ("Une bibliographie complémentaire", "Des publications supplémentaires figurent à la fin des contributions. "
             "Elles sont rattachées au sujet sur la base de leur titre ; leur contenu n'a pas été analysé pour la contribution."),
            ("Des contenus actualisés", "Chaque contribution indique son état de traitement actuel. Les contenus sont "
             "actualisés automatiquement en continu afin de tenir compte rapidement des nouvelles évolutions et de rendre "
             "l'état du traitement transparent."),
        ],
        "zielgruppe": "L'Encyclopédie s'adresse aux professionnels du conseil, des administrations, de la justice et des "
                      "entreprises, ainsi qu'aux chercheurs et aux étudiants. Elle facilite aussi bien la découverte d'un "
                      "sujet que la recherche ciblée sur une disposition particulière.",
        "hinweis_titel": "Élaboration des contenus",
        "hinweis": "Les contenus sont rédigés à l'aide de l'intelligence artificielle et vérifiés automatiquement. Ils sont "
                   "publiés sans relecture humaine. Des erreurs et des lacunes restent possibles. Les sources originales et "
                   "le droit en vigueur demeurent déterminants. La version française est une traduction de la version allemande.",
        "ueber": "À propos de l'Encyclopédie de droit fiscal de Saint-Gall", "erlasse": "Lois", "n_bearbeitet": "{n} articles traités",
        "ile": "L'ILE-HSG", "fstr_zusatz": " Les contributions s'appuient sur les publications de l'ILE-HSG. Les abonnés de la FStR ont accès à ces publications sur la plateforme Lexplorer.",
        "abo": "S'abonner à la FStR", "sem_titel": "Séminaires de Saint-Gall", "sem_naechste": "Les prochains séminaires de l'institut :",
        "sem_alle": "Tous les séminaires", "tax_knopf": "Vers le domaine",
        "mehr": "En savoir plus sur la méthode", "zahl": "Articles traités", "von": "sur {g} articles en vigueur",
    },
}


def startseite(stand: dict[str, int], lang: str = "de", stand_gesamt: dict[str, int] | None = None) -> str:
    s = START[lang]
    werk = WERK_FR if lang == "fr" else WERK
    stand_gesamt = stand_gesamt or stand
    gesamt_k = sum(stand_gesamt.values())
    queue = lade_json(QUEUE, {"artikel": {}})
    gesamt = sum(1 for v in queue["artikel"].values() if v["status"] not in ("aufgehoben", "ausgenommen"))
    zeilen = ["---", f"title: {yaml_str(werk)}",
              f"description: {yaml_str(s['intro'][:150])}",
              "template: splash", "---\n",
              '<div class="start">',
              f'<section class="start-band"><p class="start-titel">{html.escape(werk)}</p></section>',
              f'<section class="start-intro"><p class="start-leitsatz">{html.escape(s["leitsatz"])}</p>'
              f'<p>{html.escape(s["intro"])}</p>'
              f'<a class="start-link" href="./ueber/">{html.escape(s["ueber"])}</a></section>',
              f'<h2 class="start-zwischentitel">{html.escape(s["angebote_titel"])}</h2>',
              '<ul class="start-angebote">' + ''.join(
                  f'<li><strong>{html.escape(titel)}:</strong> {html.escape(text)}</li>'
                  for titel, text in s["angebote"]) + '</ul>',
              f'<p class="start-zielgruppe">{html.escape(s["zielgruppe"])}</p>',
              f'<h2 class="start-zwischentitel">{html.escape(s["hinweis_titel"])}</h2>',
              f'<p class="start-hinweis">{html.escape(s["hinweis"])}</p>',
              f'<p class="start-mehr"><a class="start-link" href="./ueber/">{s["mehr"]}</a></p>',
              f'<h2 class="start-zwischentitel">{s["erlasse"]}</h2>',
              '<nav class="erlass-raster" aria-label="Erlasse">']
    for key in ERLASSE:
        n = stand_gesamt.get(key, 0)
        zeilen.append(f'<a class="erlass-knopf" href="./{key.lower()}/"><strong>{abk(key, lang)}</strong>'
                      f'<span>{html.escape(erlass_name(key, lang))}</span><small>{s["n_bearbeitet"].format(n=n)}</small></a>')
    zeilen.append("</nav>")
    d = ile_daten()
    if d:
        sem = ""
        for x in d["naechste"]:
            datum = x.get("datum_fr", x["datum"]) if lang == "fr" else x["datum"]
            sem += (f'<li><a href="{x["url"]}" target="_blank" rel="noopener">{html.escape(x["titel"])}</a>'
                    f'<small>{html.escape(datum)}, {html.escape(x["ort"])}</small></li>')
        fstr_text = d["fstr"].get("text_fr", d["fstr"]["text"]) if lang == "fr" else d["fstr"]["text"]
        tax_text = d["tax"].get("text_fr", d["tax"]["text"]) if lang == "fr" else d["tax"]["text"]
        tax_titel = "ILE-HSG Steuerrecht" if lang == "de" else d["tax"]["titel"]
        zeilen.append(f'<h2 class="start-zwischentitel">{s["ile"]}</h2>')
        zeilen.append('<div class="start-ile">'
                      f'<section class="start-ile-karte"><strong>{html.escape(d["fstr"]["titel"])}</strong>'
                      f'<p>{html.escape(fstr_text)}{s["fstr_zusatz"]}</p>'
                      f'<a class="ile-knopf" href="{d["fstr"]["url"]}" target="_blank" rel="noopener">{s["abo"]}</a></section>'
                      f'<section class="start-ile-karte"><strong>{s["sem_titel"]}</strong>'
                      + (f'<p>{s["sem_naechste"]}</p><ul>{sem}</ul>' if sem else "")
                      + f'<a class="ile-knopf" href="{d["seminare_url"]}" target="_blank" rel="noopener">{s["sem_alle"]}</a></section>'
                      f'<section class="start-ile-karte"><strong>{html.escape(tax_titel)}</strong>'
                      f'<p>{html.escape(tax_text)}</p>'
                      '<div class="start-ile-knoepfe">'
                      f'<a class="ile-knopf" href="{d["tax"]["url"]}" target="_blank" rel="noopener">{s["tax_knopf"]}</a>'
                      f'<a class="ile-knopf" href="{d["newsletter_url"]}" target="_blank" rel="noopener">Newsletter</a>'
                      '</div></section>'
                      '</div>')
    zeilen.append(f'<div class="start-zahl"><span class="start-zahl-text">{s["zahl"]}</span>'
                  f'<span class="start-zahl-wert">{gesamt_k}</span>'
                  f'<span class="start-zahl-text">{s["von"].format(g=gesamt or "–")}</span></div>')
    zeilen.append("</div>\n")
    return "\n".join(zeilen)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pruefen", action="store_true")
    a = ap.parse_args()
    queue_status = lade_json(QUEUE, {"artikel": {}})["artikel"]

    def sammeln(dateien):
        ok, abgelehnt = [], []
        for p in dateien:
            try:
                k = lesen(p)
            except FormatFehler as e:
                abgelehnt.append((p, [f"Formatfehler: {e}"]))
                continue
            bef = pruefen(k)
            qid = f"{k.meta['erlass']}/{art_slug(k.meta['artikel'])}"
            st = queue_status.get(qid, {}).get("status")
            if not bef and st not in VEROEFFENTLICHEN:
                print(f"zurückgehalten (Status «{st}»): {p}")
                continue
            (abgelehnt if bef else ok).append((p, bef) if bef else (p, k))
        return ok, abgelehnt

    ok, abgelehnt = sammeln(sorted(KOMMENTARE.glob("*/art-*.md")))
    ok_fr, abgelehnt_fr = sammeln(sorted(KOMMENTARE_FR.glob("*/art-*.md")))
    for p, bef in abgelehnt + abgelehnt_fr:
        print(f"NICHT veröffentlicht: {p}")
        for b in bef[:10]:
            print("   -", b)
    if a.pruefen:
        print(f"{len(ok)} bereit (de), {len(ok_fr)} bereit (fr), {len(abgelehnt) + len(abgelehnt_fr)} mit Befunden")
        sys.exit(1 if abgelehnt or abgelehnt_fr else 0)

    def schreiben(liste, lang):
        basis = SITE_DOCS / "fr" if lang == "fr" else SITE_DOCS
        stand: dict[str, int] = {}
        kommentiert: dict[str, dict[str, dict]] = {e: {} for e in ERLASSE}
        for key in ERLASSE:
            ziel = basis / key.lower()
            if ziel.exists():
                shutil.rmtree(ziel)
            ziel.mkdir(parents=True)
        for p, k in liste:
            erlass = k.meta["erlass"]
            slug = art_slug(k.meta["artikel"])
            (basis / erlass.lower() / f"{slug}.md").write_text(Umwandler(k, lang).seite(p), encoding="utf-8")
            kommentiert[erlass][slug] = k.meta
            stand[erlass] = stand.get(erlass, 0) + 1
        return stand, kommentiert

    stand, kommentiert = schreiben(ok, "de")
    # Französisch nur, wenn die deutsche Fassung veröffentlicht ist
    ok_fr = [(p, k) for p, k in ok_fr if art_slug(k.meta["artikel"]) in kommentiert.get(k.meta["erlass"], {})]
    stand_fr, kommentiert_fr = schreiben(ok_fr, "fr")
    for key in ERLASSE:
        # noch nicht kommentierte Artikel mit Literatur aus dem ILE-Katalog: eigene Literaturseite
        inv = lade_json(INVENTAR / f"{key}.json", {"artikel": []})
        literatur: set[str] = set()
        for a in inv["artikel"]:
            slug = art_slug(a["nummer"])
            if a["aufgehoben"] or ausgenommen(key, a["nummer"]) or slug in kommentiert[key]:
                continue
            if katalog_je_artikel().get(f"{key} {a['nummer']}"):
                literatur.add(slug)
                (SITE_DOCS / key.lower() / f"{slug}.md").write_text(
                    literatur_seite(key, a["nummer"], a["sachueberschrift"]), encoding="utf-8")
                (SITE_DOCS / "fr" / key.lower() / f"{slug}.md").write_text(
                    literatur_seite(key, a["nummer"], a["sachueberschrift"], "fr"), encoding="utf-8")
        (SITE_DOCS / key.lower() / "index.md").write_text(erlass_seite(key, kommentiert[key], literatur=literatur),
                                                         encoding="utf-8")
        nur_de = {s: m for s, m in kommentiert[key].items() if s not in kommentiert_fr[key]}
        (SITE_DOCS / "fr" / key.lower() / "index.md").write_text(
            erlass_seite(key, kommentiert_fr[key], "fr", nur_de, literatur), encoding="utf-8")
    (SITE_DOCS / "index.md").write_text(startseite(stand), encoding="utf-8")
    (SITE_DOCS / "fr" / "index.md").write_text(startseite(stand_fr, "fr", stand), encoding="utf-8")
    print(f"{len(ok)} Kommentierungen veröffentlicht, {len(ok_fr)} auf Französisch, {len(abgelehnt) + len(abgelehnt_fr)} zurückgehalten.")


if __name__ == "__main__":
    main()
