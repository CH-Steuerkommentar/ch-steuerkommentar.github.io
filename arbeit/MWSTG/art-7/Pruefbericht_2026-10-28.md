# Prüfbericht Art. 7 MWSTG (28.10.2026, Claude-Cloud, unbeaufsichtigter Lauf)

## Umfang
48 Randnoten, 141 Fussnoten. Entscheidregister: 28 BGer-Entscheide zum Ort der Lieferung (A 6, B 7, C 15; Cache 5 einschlägig, 23 nachgetragen über Open Case Law/Entscheidsuche), BVGer/SRK rund 30 Einträge (BVGer_kantonal.md), kantonale Gerichte: keine einschlägigen Entscheide. Lexplorer-Suchen: 13 (Budget 25; alle durch den ILE-Hilfsagenten; Praxis navigiert, 0 Suchen). ILE-Fundstellen im Text: 9 Werke (Handbuch MWSTG, Bodemann FStR 2020 und 2022, Baumgartner FStR 2026, Cochardt WP 2023-18, Jöhri WP 2026-31, Seminarfolien Müller/Schluckebier 2024, Blum/Messmer 2020, Denzler/Frey 2026, Paris/Schluckebier 2018, Antonini/Studer 2025). Onlinekommentar.ch: 0 (keine OK-Kommentierung zum MWSTG; `onlinekommentar.py liste` nur DBG/StHG).

## Entscheide dieses Laufs
- Repository: Lokaler Klon hatte divergierenden `main` (alte, nicht auf origin vorhandene Commits); ein Hard-Reset wurde vom Sicherheitsfilter verweigert. Der alte Klon wurde unverändert umbenannt (/home/claude/ch-steuerkommentar.github.io.alt-*), danach frisch geklont.
- Auftrag nannte Art. 12 MWSTV 1994 als Vorgängernorm; richtig ist Art. 11 MWSTV 1994 (Art. 12 = Ort der Dienstleistung). Art. 13 MWSTG 2009 (Gruppenbesteuerung) und Art. 7 aMWSTG (Dienstleistungsbegriff) als Fehltreffer behandelt.
- Übersicht mit «Verhältnis zur Einfuhrsteuer» und «Verhältnis zum Recht der Europäischen Union» statt «Harmonisierung».
- Liechtensteinische Entscheide (Art. 13 MWSTG/FL ≈ Art. 13 aMWSTG) gekennzeichnet zitiert.
- Rechenzeitlimit: Die erste Fundstellenprüfung brach um ca. 07:00 UTC wegen des Nutzungslimits ab (Teil 2 fertig); Teile 1, 3 und 4 nach Reset um 12:00 UTC neu gestartet und vollständig durchgeführt.
- Projektweite Konventionen beibehalten wie in art-1 bis art-6 (nicht geändert, obwohl Schlussprüfung sie anmerkt): Datum in Fussnoten T.M.JJJJ; Handbuch MWSTG mit Rz. wo im OCR sichtbar, sonst mit Teil/Ziff. (Randziffern im Lexplorer-OCR teils nicht ausgewiesen – am gedruckten Werk nachtragen); FStR-Beiträge mit Ziff. statt Seiten (Seiten im Lexplorer-Text nicht verlässlich); ESTV-Publikationen als Sammeleintrag «abrufbar über Lexplorer Tax»; SRK-Zitierform wie art-6; Botschaft MWSTG 2021 ohne «ff.».
- 100’000 mit typografischem Apostroph (Prüfskill).

## Fundstellenprüfung (Schritt 8)
Vier Hilfsagenten, jede Fussnote einzeln (Fundstellenliste_Teil1–4.md; Stand der Prüfung: 146 Fussnoten vor Korrektur). Ergebnis: Teil 1 (Fn. 1–35) 33 bestätigt, 2 korrigiert; Teil 2 (Fn. 36–70) 6 korrigiert, übrige bestätigt; Teil 3 (Fn. 71–105) 29 bestätigt, 5 korrigiert, 1 nicht belegbar; Teil 4 (Fn. 106–146 und Verzeichnisse) 39 bestätigt, 2 korrigiert. Alle Korrekturen übernommen, u.a.: A-4388/2014 nur Art. 3 lit. d Ziff. 2; «bestätigt durch» bei 2C_709/2017 und 2C_321/2017 ersetzt (BGer prüfte die Frage nicht; bei A-4783/2015 E. 9.2.1.3 Eventualbegründung offengelassen, BGer E. 7.5); 2C_195/2007 E. 2.1; 2A.519/1998 betrifft Einfuhrsteuer auf Gebrauchsentgelt (Text umgeschrieben); A-1526/2006 E. 3.3 nur Ermessenseinschätzung; 2C_1079/2016 E. 3.2–3.4 und A-2675/2016 E. 5.2.2–5.3.1; 2C_561/2009 E. 2.1 f.; Fassung 2009 von Abs. 2 nach AS 2009 5206; 2C_470/2007 (nicht belegbare Regel ersetzt durch Fallbeschreibung, E. 3.6 f.); Bodemann-Stellen «wiedergegeben bei» statt «gl.M.»; 2C_266/2019 E. 4.3 auf Art. 3 Abs. 1 MWSTV a.F. bezogen, Art. 27 verneint (E. 4.4 ff., 5.2); BGE 148 II 233 E. 5.5.3 Vertrauensschutz präzisiert; Art. 79a-Massnahmen ergänzt; Erl. Bericht VE-MWSTV 2016 S. 2 f.; Divergenz der BVGer-Urteile zur Kommission offen ausgewiesen.

## Schlussprüfung (Schritt 9)
Zwei Hilfsagenten nach den Prüfpunkten von `pruefung` (Schlusspruefung_Befunde_A.md: A01–A51; Schlusspruefung_Befunde_B.md: B01–B28). Behoben: A01–A08, A11–A13, A15–A35, A37–A48 (teils sinngemäss), B01 («dürften» entfernt), B02 (Daten im Fliesstext ausgeschrieben, auch A10 im Fliesstext), B03–B20, B24–B28. Gliederung bereinigt: Überschriften unter der Schwelle zusammengelegt (Abs. 1 «Grundsatz», Abhol-/Beförderungslieferung; Abs. 2 ohne Unterüberschriften; Abs. 3 «Grundsatz»); «Abgrenzungsfragen» umbenannt in «Verhältnis zur Plattformbesteuerung»; Satz zur Gesetzmässigkeit von Art. 4 MWSTV gestrichen (A45, implizite Wertung). Nicht umgesetzt (Projektkonvention, s. oben): A09, A14, A28, A36, A49, A50, B21–B23; A10 in Fussnoten.
`pipeline/kommentar.py`: 0 Befunde; `md2site.py --pruefen`: nur Zurückhaltung wegen Status «in_arbeit» (wird beim Freigeben gesetzt).

## Für die Nachführung
- Handbuch-Randziffern, wo nur Teil/Ziff. zitiert, am gedruckten Werk ergänzen.
- Hängige Vorlage VE-MWSTG 2025 (Art. 7 Abs. 4): Botschaft abwarten.
- Lexplorer_Fundstellen.md: Rz. 280 liegt in Chunk 8cf86e67-ea54-4b62-a2a7-1d3b7815e68b (nicht cbc77bf0-…).
