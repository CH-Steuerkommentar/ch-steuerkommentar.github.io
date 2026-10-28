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
from config import ausgenommen, ERLASSE, INVENTAR, KOMMENTARE, QUEUE, SITE_DOCS, WERK, WERK_KURZ, art_slug, art_sortkey, lade_json  # noqa: E402
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
_BGE = re.compile(r"\bBGE\s+(\d{2,3})\s+(Ia|Ib|IV|V|III|II|I)\s+(\d{1,4})\b")
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
    def __init__(self, k):
        self.k = k
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
        erlass, art = m["erlass"], m["artikel"]
        titel = m.get("titel", "")
        stand = datum_ch(m["stand"])
        aus = []
        aus.append("---")
        aus.append(f"title: {yaml_str(f'Art. {art} {erlass}')}")
        aus.append(f"description: {yaml_str(f'Kommentierung zu Art. {art} {erlass} – {titel}'.strip(' –'))}")
        aus.append("sidebar:")
        aus.append(f"  label: {yaml_str(f'Art. {art} – {titel}' if titel else f'Art. {art}')}")
        aus.append(f"  order: {order(art)}")
        aus.append("banner:")
        aus.append(f"  content: {yaml_str(f'Mit KI erstellt und am Volltext der Quellen geprüft. Stand: {stand}. Keine Rechtsberatung.')}")
        aus.append(f"lastUpdated: {m['stand']}")
        aus.append("---\n")
        zitat = f"{WERK_KURZ}, Art. {art} {erlass} N. [Randnote] (Stand {stand})"
        aus.append(f'<aside class="zitiervorschlag"><span><strong>Zitiervorschlag:</strong> <span class="zitat">{zitat}</span>'
                   + (f' · {m["fassung"]}' if m.get("fassung") else "")
                   + f'</span><button type="button" class="kopieren" data-text="{html.escape(zitat, quote=True)}">Kopieren</button></aside>\n')
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
                        aus.append(ile_hinweis(k))
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
                aus.append(f'<span class="rn" id="n{n}"><a href="#n{n}" aria-label="Randnote {n}">{n}</a></span> '
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
            aus.append(ile_hinweis(k))
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


def ile_hinweis(k) -> str:
    """Kasten unter der Kommentierung: wie viele FStR-Beiträge und Seminarunterlagen sie stützen, mit Links."""
    d = ile_daten()
    if not d:
        return ""
    eintraege, in_lit = [], False
    for b in k.bloecke:
        if b.art == "ueberschrift" and b.verzeichnis and b.ebene == 1:
            in_lit = b.text.strip().lower().startswith("literatur")
        elif in_lit and b.art == "verzeichnis_eintrag":
            eintraege.append(b.text)
    fstr = sum(1 for e in eintraege if re.search(r"\bFStR\s+\d{4}", e))
    sem = sum(1 for e in eintraege if "Seminarunterlage" in e)
    if fstr or sem:
        teile = []
        if fstr:
            teile.append(f"{fstr} {'Beitrag' if fstr == 1 else 'Beiträge'} aus dem Forum für Steuerrecht (FStR)")
        if sem:
            teile.append(f"{sem} {'Unterlage' if sem == 1 else 'Unterlagen'} der St.Galler Seminare")
        satz = ("Diese Kommentierung stützt sich auf " + " und ".join(teile)
                + ". Das FStR ist die Fachzeitschrift des ILE-HSG; die St.Galler Seminare greifen aktuelle Fragen der Praxis auf.")
    else:
        satz = ("Das Forum für Steuerrecht (FStR) ist die Fachzeitschrift des ILE-HSG zum Schweizer und internationalen "
                "Steuerrecht; die St.Galler Seminare greifen aktuelle Fragen der Praxis auf.")
    knoepfe = [f'<a class="ile-knopf" href="{d["fstr"]["url"]}" target="_blank" rel="noopener">FStR abonnieren</a>']
    for s in d["naechste"]:
        knoepfe.append(f'<a class="ile-knopf zweit" href="{s["url"]}" target="_blank" rel="noopener">'
                       f'{html.escape(s["kurz"])} · {html.escape(s["datum"])}</a>')
    if not d["naechste"]:
        knoepfe.append(f'<a class="ile-knopf zweit" href="{d["seminare_url"]}" target="_blank" rel="noopener">Seminare</a>')
    return ('\n<aside class="ile-hinweis" aria-label="Vertiefung beim ILE-HSG">'
            '<p class="ile-hinweis-titel">Vertiefung beim ILE-HSG</p>'
            f'<p>{html.escape(satz)}</p><p class="ile-knoepfe">{"".join(knoepfe)}</p></aside>\n')


def erlass_seite(erlass: str, kommentiert: dict[str, dict]) -> str:
    inv = lade_json(INVENTAR / f"{erlass}.json", {"artikel": [], "fassung_vom": "", "quelle": ""})
    e = ERLASSE[erlass]
    zeilen = ["---", f"title: {yaml_str(erlass)}",
              f"description: {yaml_str(e['name'])}", "sidebar:", "  label: Übersicht", "  order: 0", "---\n",
              f"{e['name']} (SR {e['sr']}), Fassung vom {datum_ch(inv.get('fassung_vom', ''))} "
              f"([Fedlex](https://www.fedlex.admin.ch/eli/cc/{e['eli'].split('/eli/cc/')[1]}/de)).\n",
              f"{len(kommentiert)} von {sum(1 for a in inv['artikel'] if not a['aufgehoben'] and not ausgenommen(erlass, a['nummer']))} "
              "geltenden Artikeln kommentiert. Übergangsbestimmungen sowie Referendum und Inkrafttreten werden nicht kommentiert.\n",
              "| Artikel | Sachüberschrift | Stand |", "|---|---|---|"]
    for a in inv["artikel"]:
        if a["aufgehoben"]:
            continue
        slug = art_slug(a["nummer"])
        if ausgenommen(erlass, a["nummer"]) and slug not in kommentiert:
            zeilen.append(f"| Art. {a['nummer']} | {a['sachueberschrift']} | nicht kommentiert |")
            continue
        if slug in kommentiert:
            zeilen.append(f"| [Art. {a['nummer']}](./{slug}/) | {a['sachueberschrift']} | {datum_ch(kommentiert[slug]['stand'])} |")
        else:
            zeilen.append(f"| Art. {a['nummer']} | {a['sachueberschrift']} | – |")
    return "\n".join(zeilen) + "\n"


def startseite(stand: dict[str, int]) -> str:
    gesamt_k = sum(stand.values())
    queue = lade_json(QUEUE, {"artikel": {}})
    gesamt = sum(1 for v in queue["artikel"].values() if v["status"] not in ("aufgehoben", "ausgenommen"))
    ueber = "Über den " + WERK.replace("Offener ", "Offenen ", 1)
    zeilen = ["---", f"title: {yaml_str(WERK)}",
              "description: Offener Online-Kommentar zum Steuerrecht des Bundes (DBG, StHG, VStG, MWSTG, StG)",
              "template: splash", "---\n",
              '<div class="start">',
              f'<section class="start-band"><p class="start-titel">{html.escape(WERK)}</p></section>',
              '<section class="start-intro"><p>Kommentierungen zum Bundesgesetz über die direkte Bundessteuer, zum '
              'Steuerharmonisierungsgesetz, zum Verrechnungssteuergesetz, zum Mehrwertsteuergesetz und zum '
              'Stempelabgabengesetz – frei zugänglich, neutral, jede Fundstelle am Volltext geprüft.</p>'
              f'<a class="start-link" href="./ueber/">{html.escape(ueber)}</a></section>',
              '<h2 class="start-zwischentitel">Erlasse</h2>',
              '<nav class="erlass-raster" aria-label="Erlasse">']
    for key, e in ERLASSE.items():
        n = stand.get(key, 0)
        zeilen.append(f'<a class="erlass-knopf" href="./{key.lower()}/"><strong>{key}</strong>'
                      f'<span>{html.escape(e["name"])}</span><small>{n} Artikel kommentiert</small></a>')
    zeilen.append("</nav>")
    d = ile_daten()
    if d:
        sem = "".join(f'<li><a href="{s["url"]}" target="_blank" rel="noopener">{html.escape(s["titel"])}</a>'
                      f'<small>{html.escape(s["datum"])}, {html.escape(s["ort"])}</small></li>' for s in d["naechste"])
        zeilen.append('<h2 class="start-zwischentitel">Vom ILE-HSG</h2>')
        zeilen.append('<div class="start-ile">'
                      f'<section class="start-ile-karte"><strong>{html.escape(d["fstr"]["titel"])}</strong>'
                      f'<p>{html.escape(d["fstr"]["text"])} Viele Kommentierungen stützen sich auf seine Beiträge.</p>'
                      f'<a class="ile-knopf" href="{d["fstr"]["url"]}" target="_blank" rel="noopener">FStR abonnieren</a></section>'
                      '<section class="start-ile-karte"><strong>St.Galler Seminare</strong>'
                      '<p>Die nächsten Seminare des Instituts:</p>'
                      f'<ul>{sem}</ul>' if sem else '<section class="start-ile-karte"><strong>St.Galler Seminare</strong><p>Seminare zum internationalen Steuerrecht und zur Unternehmensbesteuerung.</p>')
        zeilen[-1] += (f'<a class="ile-knopf" href="{d["seminare_url"]}" target="_blank" rel="noopener">Alle Seminare</a></section>'
                       f'<section class="start-ile-karte"><strong>{html.escape(d["weiterbildung"]["titel"])}</strong>'
                       f'<p>{html.escape(d["weiterbildung"]["text"])}</p>'
                       f'<a class="ile-knopf" href="{d["weiterbildung"]["url"]}" target="_blank" rel="noopener">Zur Weiterbildung</a></section>'
                       '</div>')
    zeilen.append('<h2 class="start-zwischentitel">So entsteht der Kommentar</h2>')
    zeilen.append('<ol class="start-schritte">'
                  '<li><strong>Rechtsprechung</strong><span>Alle Entscheide des Bundesgerichts, die die Norm zitieren, '
                  'werden gesammelt, eingeordnet und an der einschlägigen Erwägung gelesen.</span></li>'
                  '<li><strong>Praxis und Lehre</strong><span>Dazu kommen kantonale Gerichte, die Verwaltungspraxis, '
                  'die Literatur des ILE-HSG und Onlinekommentar.ch.</span></li>'
                  '<li><strong>Neutraler Text</strong><span>Der Text gibt wieder, was Gerichte, Verwaltung und Lehre sagen, '
                  'und wertet nicht selbst.</span></li>'
                  '<li><strong>Prüfung</strong><span>Eine eigene Prüfinstanz kontrolliert jede Fussnote am Volltext der Quelle.</span></li>'
                  '</ol>')
    zeilen.append('<p class="start-mehr"><a class="start-link" href="./ueber/">Mehr zur Arbeitsweise</a></p>')
    zeilen.append(f'<div class="start-zahl"><span class="start-zahl-text">Kommentierte Artikel</span>'
                  f'<span class="start-zahl-wert">{gesamt_k}</span>'
                  f'<span class="start-zahl-text">von {gesamt or "–"} geltenden Artikeln</span></div>')
    zeilen.append("</div>\n")
    return "\n".join(zeilen)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pruefen", action="store_true")
    a = ap.parse_args()
    dateien = sorted(KOMMENTARE.glob("*/art-*.md"))
    queue_status = lade_json(QUEUE, {"artikel": {}})["artikel"]
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
            print(f"zurückgehalten (Status «{st}»): {qid}")
            continue
        (abgelehnt if bef else ok).append((p, bef) if bef else (p, k))
    for p, bef in abgelehnt:
        print(f"NICHT veröffentlicht: {p.relative_to(KOMMENTARE)}")
        for b in bef[:10]:
            print("   -", b)
    if a.pruefen:
        print(f"{len(ok)} bereit, {len(abgelehnt)} mit Befunden")
        sys.exit(1 if abgelehnt else 0)
    stand: dict[str, int] = {}
    kommentiert: dict[str, dict[str, dict]] = {e: {} for e in ERLASSE}
    for key in ERLASSE:
        ziel = SITE_DOCS / key.lower()
        if ziel.exists():
            shutil.rmtree(ziel)
        ziel.mkdir(parents=True)
    for p, k in ok:
        erlass = k.meta["erlass"]
        slug = art_slug(k.meta["artikel"])
        (SITE_DOCS / erlass.lower() / f"{slug}.md").write_text(Umwandler(k).seite(p), encoding="utf-8")
        kommentiert[erlass][slug] = k.meta
        stand[erlass] = stand.get(erlass, 0) + 1
    for key in ERLASSE:
        (SITE_DOCS / key.lower() / "index.md").write_text(erlass_seite(key, kommentiert[key]), encoding="utf-8")
    (SITE_DOCS / "index.md").write_text(startseite(stand), encoding="utf-8")
    print(f"{len(ok)} Kommentierungen veröffentlicht, {len(abgelehnt)} zurückgehalten.")


if __name__ == "__main__":
    main()
