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
        "beschreibung": "Kommentierung zu Art. {art} {abk}",
        "randnote": "Randnote",
    },
    "fr": {
        "banner": "Rédigé par une IA et vérifié sur le texte intégral des sources. État : {stand}. Ne constitue pas un conseil juridique.",
        "zitat": "{werk}, art. {art} {abk} N [note marginale] (état au {stand})",
        "zitat_label": "Proposition de citation :", "kopieren": "Copier", "kopiert": "Copié",
        "beschreibung": "Commentaire de l'art. {art} {abk}",
        "randnote": "Note marginale",
    },
}


def abk(erlass: str, lang: str) -> str:
    return ERLASSE[erlass]["kurz_fr"] if lang == "fr" else erlass


def erlass_name(erlass: str, lang: str) -> str:
    return ERLASSE[erlass]["name_fr"] if lang == "fr" else ERLASSE[erlass]["name"]
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
        text = "\n".join(aus)
        text = re.sub(r"(\n- [^\n]*)\n(?=[^-\n])", r"\1\n\n", text)
        text += "\n\n" + "\n".join(f"[^{i}]: {inh}" for i, inh in enumerate(self.fn, 1)) + "\n"
        return text


ILE_DATEN = Path(__file__).resolve().parent.parent / "site" / "src" / "data" / "ile.json"


def ile_daten() -> dict:
    d = lade_json(ILE_DATEN, {})
    heute = date.today().isoformat()
    d["naechste"] = [s for s in d.get("seminare", []) if s.get("bis", "") >= heute][:2]
    return d


def fehler_melden(erlass: str, art: str, lang: str = "de") -> str:
    """Kleiner Hinweis am Ende des Kommentartexts: Fehler per E-Mail melden (Betreff vorausgefüllt)."""
    from urllib.parse import quote
    if lang == "fr":
        betreff = f"[ILE-StK] Signalement art. {art} {abk(erlass, lang)}"
        text = "Vous avez trouvé une erreur ? "
        link = "Signalez-la-nous"
    else:
        betreff = f"[ILE-StK] Hinweis Art. {art} {erlass}"
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
            satz = (f"Ce commentaire s'appuie sur {n} publication{'s' if n > 1 else ''} de l'ILE-HSG{klammer}. "
                    "La FStR est la revue spécialisée de l'ILE-HSG ; les séminaires de Saint-Gall traitent des questions "
                    "actuelles de la pratique.")
        else:
            satz = ("Le Forum für Steuerrecht (FStR) est la revue spécialisée de l'ILE-HSG en droit fiscal suisse et "
                    "international ; les séminaires de Saint-Gall traitent des questions actuelles de la pratique.")
    else:
        titel, abo, sem_knopf = "Vertiefung beim ILE-HSG", "FStR abonnieren", "Seminare"
        if n:
            satz = (f"Diese Kommentierung stützt sich auf {n} {'Publikation' if n == 1 else 'Publikationen'} des ILE-HSG{klammer}. "
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


def erlass_seite(erlass: str, kommentiert: dict[str, dict], lang: str = "de", deutsch: dict[str, dict] | None = None) -> str:
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
                f"{len(kommentiert)} articles commentés en français et {len(deutsch)} en allemand, sur {gesamt} articles en vigueur. "
                "Les dispositions finales et transitoires ainsi que celles relatives au référendum et à l'entrée en vigueur ne sont pas commentées.\n",
                "| Article | Titre | État |", "|---|---|---|"]
        label, nicht = "Aperçu", "non commenté"
    else:
        ab = erlass
        kopf = [f"{e['name']} (SR {e['sr']}), Fassung vom {datum_ch(inv.get('fassung_vom', ''))} "
                f"([Fedlex](https://www.fedlex.admin.ch/eli/cc/{eli}/de)).\n",
                f"{len(kommentiert)} von {gesamt} geltenden Artikeln kommentiert. Schluss- und Übergangsbestimmungen sowie "
                "Referendum und Inkrafttreten werden nicht kommentiert.\n",
                "| Artikel | Sachüberschrift | Stand |", "|---|---|---|"]
        label, nicht = "Übersicht", "nicht kommentiert"
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
        else:
            zeilen.append(f"| {artikel_nr} | {a['sachueberschrift']} | – |")
    return "\n".join(zeilen) + "\n"


START = {
    "de": {
        "intro": "Kommentierungen zum Bundesgesetz über die direkte Bundessteuer, zum Steuerharmonisierungsgesetz, zum "
                 "Verrechnungssteuergesetz, zum Mehrwertsteuergesetz und zum Stempelabgabengesetz – frei zugänglich "
                 "und neutral, vollständig von KI verfasst und ohne menschliche Durchsicht veröffentlicht; jede Fundstelle "
                 "hat die KI am Volltext geprüft.",
        "ueber": "Über den ILE-HSG Steuerrechtskommentar", "erlasse": "Erlasse", "n_kommentiert": "{n} Artikel kommentiert",
        "ile": "Vom ILE-HSG", "fstr_zusatz": " Die Kommentierungen stützen sich auf seine Beiträge.",
        "abo": "FStR abonnieren", "sem_titel": "St.Galler Seminare", "sem_naechste": "Die nächsten Seminare des Instituts:",
        "sem_alle": "Alle Seminare", "tax_knopf": "Zum Fachbereich",
        "so": "So entsteht der Kommentar",
        "schritte": [("Rechtsprechung", "Alle Entscheide des Bundesgerichts, die die Norm zitieren, werden gesammelt, "
                      "eingeordnet und an der einschlägigen Erwägung gelesen."),
                     ("Praxis und Lehre", "Dazu kommen kantonale Gerichte, die Verwaltungspraxis, die Literatur des ILE-HSG "
                      "und Onlinekommentar.ch."),
                     ("Neutraler Text", "Der Text gibt wieder, was Gerichte, Verwaltung und Lehre sagen, und wertet nicht selbst."),
                     ("Prüfung", "Eine eigene Prüfinstanz kontrolliert jede Fussnote am Volltext der Quelle.")],
        "mehr": "Mehr zur Arbeitsweise", "zahl": "Kommentierte Artikel", "von": "von {g} geltenden Artikeln",
    },
    "fr": {
        "intro": "Commentaires de la loi sur l'impôt fédéral direct, de la loi sur l'harmonisation des impôts directs, de la loi "
                 "sur l'impôt anticipé, de la loi sur la TVA et de la loi sur les droits de timbre – en libre accès et neutres, "
                 "entièrement rédigés par une IA et publiés sans relecture humaine ; chaque référence a été vérifiée "
                 "par l'IA sur le texte intégral. Traduits de la version allemande.",
        "ueber": "À propos du Commentaire de droit fiscal ILE-HSG", "erlasse": "Lois", "n_kommentiert": "{n} articles commentés",
        "ile": "L'ILE-HSG", "fstr_zusatz": " De nombreux commentaires s'appuient sur ses contributions.",
        "abo": "S'abonner à la FStR", "sem_titel": "Séminaires de Saint-Gall", "sem_naechste": "Les prochains séminaires de l'institut :",
        "sem_alle": "Tous les séminaires", "tax_knopf": "Vers le domaine",
        "so": "Comment le commentaire est rédigé",
        "schritte": [("Jurisprudence", "Tous les arrêts du Tribunal fédéral qui citent la disposition sont réunis, classés et "
                      "lus au considérant pertinent."),
                     ("Pratique et doctrine", "S'y ajoutent les tribunaux cantonaux, la pratique administrative, la littérature "
                      "de l'ILE-HSG et Onlinekommentar.ch."),
                     ("Texte neutre", "Le texte rapporte ce que disent les tribunaux, l'administration et la doctrine, sans "
                      "porter d'appréciation propre."),
                     ("Contrôle", "Une instance de contrôle distincte vérifie chaque note de bas de page sur le texte intégral "
                      "de la source.")],
        "mehr": "En savoir plus sur la méthode", "zahl": "Articles commentés", "von": "sur {g} articles en vigueur",
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
              f'<section class="start-intro"><p>{html.escape(s["intro"])}</p>'
              f'<a class="start-link" href="./ueber/">{html.escape(s["ueber"])}</a></section>',
              f'<h2 class="start-zwischentitel">{s["erlasse"]}</h2>',
              '<nav class="erlass-raster" aria-label="Erlasse">']
    for key in ERLASSE:
        n = stand_gesamt.get(key, 0)
        zeilen.append(f'<a class="erlass-knopf" href="./{key.lower()}/"><strong>{abk(key, lang)}</strong>'
                      f'<span>{html.escape(erlass_name(key, lang))}</span><small>{s["n_kommentiert"].format(n=n)}</small></a>')
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
        zeilen.append(f'<h2 class="start-zwischentitel">{s["ile"]}</h2>')
        zeilen.append('<div class="start-ile">'
                      f'<section class="start-ile-karte"><strong>{html.escape(d["fstr"]["titel"])}</strong>'
                      f'<p>{html.escape(fstr_text)}{s["fstr_zusatz"]}</p>'
                      f'<a class="ile-knopf" href="{d["fstr"]["url"]}" target="_blank" rel="noopener">{s["abo"]}</a></section>'
                      f'<section class="start-ile-karte"><strong>{s["sem_titel"]}</strong>'
                      + (f'<p>{s["sem_naechste"]}</p><ul>{sem}</ul>' if sem else "")
                      + f'<a class="ile-knopf" href="{d["seminare_url"]}" target="_blank" rel="noopener">{s["sem_alle"]}</a></section>'
                      f'<section class="start-ile-karte"><strong>{html.escape(d["tax"]["titel"])}</strong>'
                      f'<p>{html.escape(tax_text)}</p>'
                      f'<a class="ile-knopf" href="{d["tax"]["url"]}" target="_blank" rel="noopener">{s["tax_knopf"]}</a></section>'
                      '</div>')
    zeilen.append(f'<h2 class="start-zwischentitel">{s["so"]}</h2>')
    zeilen.append('<ol class="start-schritte">' + "".join(f"<li><strong>{a}</strong><span>{b}</span></li>" for a, b in s["schritte"]) + "</ol>")
    zeilen.append(f'<p class="start-mehr"><a class="start-link" href="./ueber/">{s["mehr"]}</a></p>')
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
        (SITE_DOCS / key.lower() / "index.md").write_text(erlass_seite(key, kommentiert[key]), encoding="utf-8")
        nur_de = {s: m for s, m in kommentiert[key].items() if s not in kommentiert_fr[key]}
        (SITE_DOCS / "fr" / key.lower() / "index.md").write_text(
            erlass_seite(key, kommentiert_fr[key], "fr", nur_de), encoding="utf-8")
    (SITE_DOCS / "index.md").write_text(startseite(stand), encoding="utf-8")
    (SITE_DOCS / "fr" / "index.md").write_text(startseite(stand_fr, "fr", stand), encoding="utf-8")
    print(f"{len(ok)} Kommentierungen veröffentlicht, {len(ok_fr)} auf Französisch, {len(abgelehnt) + len(abgelehnt_fr)} zurückgehalten.")


if __name__ == "__main__":
    main()
