# Format einer Kommentierung

Jede Kommentierung ist eine Markdown-Datei unter `kommentare/<Erlass>/art-<Nummer>.md`, z.B. `kommentare/DBG/art-26.md`, `kommentare/StHG/art-7a.md`. Sie ist die einzige Quelle: Website und Word-Fassung werden daraus erzeugt. Ein vollständiges Beispiel steht in `docs/beispiel-format.md`.

## Kopf

```yaml
---
erlass: DBG                    # DBG, StHG, VStG, MWSTG oder StG (wie in pipeline/config.py)
artikel: "26"                  # wie in Fedlex: "26", "37a", "205bbis"
titel: Berufskosten            # Sachüberschrift für die Website
stand: 2026-10-26              # Stand der Bearbeitung (ISO-Datum)
fassung: Fassung vom 2.9.2026  # kommentierte Fassung (optional)
---
```

## Text

| Zeile | Bedeutung |
|---|---|
| `> **Art. 26 Berufskosten**` | Normtext, erste Zeile (Artikel und Sachüberschrift) |
| `> 1 Als Berufskosten …` | Absatz des Normtexts mit Absatzziffer |
| `> a. die notwendigen …` | Buchstabe |
| `# Übersicht` | Gliederungsebene I. (Nummern setzt das Skript; keine Nummern schreiben) |
| `## …`, `### …`, `#### …` | Ebenen A., 1., a. |
| `{rn:label} **Stichwort.** Text …` | Randnote mit Label (Absatz beginnt mit der Marke); `{rn}` ohne Label, wenn nichts darauf verweist |
| `N. {{N:label}}` | Querverweis auf eine Randnote |
| `…Text.^[Fussnotentext.]` | Fussnote (eckige Klammern im Fussnotentext sind erlaubt) |
| `- Punkt` direkt unter einer Randnote | Aufzählung innerhalb der Randnote |
| `# Literaturverzeichnis`, `# Materialienverzeichnis` | Verzeichnisse (ohne Nummer); darin `## Bund` als Zwischentitel und `- Eintrag.` je Eintrag |
| `**fett**`, `*kursiv*` | Hervorhebung |

Regeln, die `pipeline/kommentar.py` prüft (eine Kommentierung mit Befunden wird nicht veröffentlicht):

- Erstes Kapitel `# Übersicht`; Normtext vorhanden.
- Jeder Textabsatz ausserhalb der Verzeichnisse ist eine Randnote.
- Pro Randnote genau ein fettes Stichwort.
- Jede Fussnote endet mit Punkt; jedes Label ist eindeutig; jeder Querverweis zeigt auf ein Label.
- Keine wertenden Wendungen (U.E., «zu Recht», «überzeugend», «dürfte» …), kein `==`, kein «—», kein «ß».

Leerzeilen trennen Absätze. Eine Randnote steht in einem Absatz (Zeilenumbrüche innerhalb sind erlaubt).

## Word-Fassung

`python3 pipeline/md2docx.py kommentare/DBG/art-26.md` erzeugt das Markup des OK-Builders und, wenn das Plugin «OK-Steuerkommentar» installiert ist, die Word-Datei in der OK-Vorlage. Aufzählungen in Randnoten erscheinen in Word im Fliesstext mit Halbgeviertstrichen.
