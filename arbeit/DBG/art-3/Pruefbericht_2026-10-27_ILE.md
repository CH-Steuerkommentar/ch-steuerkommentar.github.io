# Prüfbericht Art. 3 DBG – Einbau der ILE-Literatur (27.10.2026)

Unbeaufsichtigter Lauf. Status unverändert («geprueft»), keine Reservierung. Nur `kommentare/DBG/art-3.md` und `arbeit/DBG/art-3/` geändert.

## Recherche
- **Lexplorer-Suchen:** 9 (`search_chunks_hybrid`, Kanton CH, Kategorie `08-institut-fuer-law-und-economics`, limit 8–10); Budget 25. Lesen mit `get_chunk_content`, `get_document_slice` und `nav_list_chunks` (nicht gezählt).
- Lehrbuch Hongler/Lorenz («ILE-HSG — Lehrbuch Steuerrecht») erschien einmal als Treffer (Suche 6) und wurde übergangen.
- Ablage aller verwendeten Treffer: `01_Recherche/Lexplorer_Fundstellen.md`.
- Ohne einschlägigen Treffer und deshalb ohne Einbau: Ausblick (Individualbesteuerung und Wohnsitz von Ehegatten), Harmonisierung (über Abs. 4 hinaus), Übersicht/Regelungsgegenstand, Steuerdomizilentscheid und Vorentscheid (N. vorentscheid).

## Eingebaut
Sechs ILE-Werke, 33 Fussnoten mit neuen ILE-Fundstellen (38 Zitatstellen):

| Werk | Zitatstellen |
|---|---|
| Oesterhelt/Opel, FStR 2025, Rechtsprechung 2025-2, Ziff. 5.3 | 5 |
| Oesterhelt/Opel, FStR 2024, Rechtsprechung 2024/3, Ziff. 3.3 | 5 |
| Seiler, IFF-Schriftenreihe 2023, Internationales Steuerrecht der Schweiz, § 4 und § 10 | 14 |
| Mauchle, IFF-Schriftenreihe 2021, Die Verteilung von Erwerbseinkünften im interkantonalen Steuerrecht, Rz. 39 f. | 2 |
| Brülisauer, FStR 2024, Sitz versus Verwaltung im interkantonalen und im internationalen Verhältnis, Ziff. 4.1.3.1 | 4 |
| Oesterhelt, FStR 2021, Aus der Rechtsprechung im Jahr 2020/2021 (Teil 1), Ziff. 4.3 | 8 |

- Bestätigend (gl.M./vgl.) in bestehenden Fussnoten nach den Entscheiden: entstehung, dba, beweis-wegzug (2), beweis-indizien, beweis-mitwirkung-steuerhoheit, wohnsitz-zgb, wohnsitz-elemente (2), wohnsitz-lebensmittelpunkt (2), familienort, international-familie, gesetzlicher-wohnsitz, aufenthalt-begriff, aufenthalt-unterbrechung, aufenthalt-umfang, sonderzweck-grundsatz, sonderzweck-stationaer, sonderzweck-zaehlung, heimatort-wirkung, heimatort-kantone, veranlagungsort.
- Meinungsstand in indirekter Rede in bestehenden Randnoten: wohnsitz-lebensmittelpunkt (Minderheit zum alternierenden Wohnsitz, a.M.), international-familie (Oesterhelt/Opel zur gesonderten Wohnsitzbestimmung), sonderzweck-grundsatz (Oesterhelt zur analogen Anwendung auf die Staatssteuer, a.M. zur Begründung), sonderzweck-zaehlung (Oesterhelt zur Lehranstalt).
- **Neue Randnoten (3)**, je mit eigenem Meinungsstand der Lehre:
  - `wohnsitz-jahresfrist` – Faustregel von einem Jahr; Kritik von Oesterhelt/Opel an BGer 9C_714/2023 E. 6.4 (a.M.).
  - `remanence-fiktiv` – fiktiver statt gesetzlicher Wohnsitz (Oesterhelt/Opel, a.M.); BGer 9C_714/2023 ohne Rückgriff auf Art. 24 ZGB; offen gelassen; spätere Bestätigung der Fortdauer in BGer 9C_448/2025 E. 5.2. Querverweis aus `gesetzlicher-wohnsitz` ergänzt.
  - `aufenthalt-lehre` – Meinungsstand zur vorübergehenden Unterbrechung und zur Anrechnung von Abwesenheitstagen (Seiler; Oesterhelt).
- Neu zitierter Entscheid: BGer 9C_714/2023 vom 4.2.2025 (Fünferbesetzung; Staats- und Gemeindesteuern BE), Gegenstand der Besprechung FStR 2025, Ziff. 5; am Original (Open Case Law) geprüft, E. 6.1, 6.2, 6.4.
- Literaturverzeichnis ergänzt (6 Einträge); bestehender Eintrag De Vries Reilingh unverändert. Kopf `stand: 2026-10-27`.
- Bestehender Text sonst nicht umgeschrieben; einzige Änderung an bestehendem Wortlaut: Querverweis «zur Kritik N. …» in `gesetzlicher-wohnsitz`.

## Fundstellenprüfung (getrennter Arbeitsschritt)
Kein Werkzeug für einen eigenen Hilfsagenten verfügbar; die Prüfung erfolgte als getrennter Durchgang: alle 33 Fussnoten mit ILE-Fundstellen wurden per Skript aus der Datei gezogen und jede Zitatstelle erneut am Chunk (`get_chunk_content`) auf Autor:innen, Fundort, Ziffer und Tragfähigkeit geprüft.

| Ergebnis | Zahl | Hinweis |
|---|---|---|
| bestätigt | 37 | Autor:innen laut Chunk-Angabe; Ziffern: FStR-Besprechungen nach Abschnittsnummer (3.3, 4.3, 5.3, 4.1.3.1 laut Überschrift im Dokument), Seiler nach Randnoten (N. 13, 14, 15, 22, 24, 29; «N. 16 ff.» für die unnummeriert extrahierten Absätze nach N. 16), Mauchle Rz. 39 f. |
| korrigiert | 1 | Fn. zu `heimatort-wirkung`: gl.M. von Oesterhelt/Opel auf die Zuständigkeit des Heimatkantons für den Ehegatten beschränkt (die Besprechung sagt nichts zum Wahlrecht nach Art. 5 Abs. 3 VNPA). |
| zusätzlich präzisiert | 2 | `aufenthalt-lehre`: «hat das Bundesgericht nicht ausdrücklich entschieden» als Aussage von Oesterhelt umformuliert; `remanence-fiktiv`: «für unzutreffend» (Wertungswort, von kommentar.py gemeldet) durch «lehnen … ab» ersetzt. |
| gestrichen | 0 | |

Hinweise: Der Titel bei Mauchle ist im Lexplorer-Pfad gekürzt («… unter Berücksichti…»); zitiert wird der Haupttitel. Den Sammelband von Seiler weist Lexplorer als «Schriftenreihe (2023)» mit Pfad «122_Internationales_Steuerrecht_der_Schweiz» aus; Herausgeberschaft dort nicht angegeben.

## Prüfung Format und Neutralität
`python3 pipeline/kommentar.py kommentare/DBG/art-3.md`: 42 Randnoten, 130 Fussnoten, 0 Befunde. `python3 pipeline/md2site.py --pruefen`: keine Meldung zu Art. 3 DBG.
