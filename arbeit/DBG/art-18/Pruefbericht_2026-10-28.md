# Prüfbericht Art. 18 DBG (28.10.2026)

Unbeaufsichtigter Lauf (Claude-Cloud, geplante Aufgabe). Ergebnis: 95 Randnoten, 348 Fussnoten; `pipeline/kommentar.py` ohne Befund; `md2site.py --pruefen` hält die Datei nur wegen des Status «in_arbeit» zurück (Status setzt das Freigabeskript).

## Entscheide dieses Laufs (ohne Rückfrage)

- Keine Karteikarten. Register und Problemkarte selbst erstellt: Cache `pipeline/entscheide.py DBG/art-18` (429 Entscheide; Suchtreffer 625), Triage durch sechs Hilfsagenten nach Zeitraum (A 84, B 231, C 114, X 0). `find_leading_cases` (40 Treffer): alle BGer/BGE im Cache.
- Umfang über dem Plan der kleineren OK-Kommentierungen, begründet in der Gliederungsnotiz (Fülle der Rechtsprechung).
- Zitierstrings: alle 216 BGE/BGer-Zitate per Skript gegen `zitat_de` des Caches geprüft (keine Abweichung). Datumsform wie im Repository nach `citation_string_de` («vom 22. April 2005»).
- Materialien vor 1999 (BBl 1983 III 1, BBl 1999 I 4) nur als OCR-Ausschnitte erreichbar; zitiert nur, was durch Rechtsprechung gestützt ist (BGE 125 II 113 E. 5c, BGE 126 II 473, BGer 2A.272/2003); Botschaft 1999 nach Ziffer statt Seite zitiert.
- Gescheiterte Vorlage 16.031 (Abs. 4): Nichteintreten mit BGer 2C_199/2017 E. 2.3 f. belegt; Daten der Ratsbeschlüsse nicht erreichbar (Curia Vista ausserhalb der zulässigen Quellen).
- Ausblick Individualbesteuerung: Ergebnis der Abstimmung vom 8.3.2026 und Inkraftsetzung nicht an einer zulässigen Quelle gelesen (andere Kommentierungen des Repositorys nennen eine Medienmitteilung vom 19.8.2026, die hier nicht geprüft werden konnte). Text deshalb auf Gesetz (Ziff. II Abs. 3) und Abstimmungsdatum beschränkt.
- Stocker/Schmid (Schriftenreihe Bd. 122): Herausgeber:innen des Werks in Lexplorer nicht ausgewiesen; Eintrag ohne Hrsg. Teuscher: Autorname nur aus dem Dokumentpfad, am Titelblatt nachprüfen. Engstler: Jahr 2025 nach Impressum (Lexplorer führt 2026).

## Lexplorer

Lexplorer Tax: 16 Suchen (alle ILE-Literatur, Budget 25 eingehalten); Verwaltungspraxis und Fundstellenprüfung nur navigierend. Lexplorer nicht für Rechtsprechung. Keine Websuche. Onlinekommentar: Art. 10 DBG, Art. 13 und 14 StHG geholt; zitiert Art. 10 DBG und Art. 14 StHG.

## Fundstellenprüfung (Schritt 8)

Fünf Hilfsagenten je Hauptteil, jede Fussnote einzeln am Original (Cache-Volltexte, Open Case Law, Entscheidsuche, Kreisschreiben über Open Case Law, Steuerbücher und ILE-Literatur über Lexplorer Tax), dazu ein sechster Agent für alle ILE-Fundstellen am Original. Rund 64 Korrekturen umgesetzt, u.a.: zahlreiche E.-Nummern; Fachkenntnisse nur von Mitgesellschaftern zugerechnet (2C_553/2019, 2C_1048/2013); 2C_468/2009 (Arzt, altes Recht) richtiggestellt; 2C_282/2022 (Rückstellung für Bewirtschaftungskosten); Zwei-Drittel-Aussage als geschützte Würdigung der Vorinstanz; Zürcher Praxis (BStRK, VGer) präzisiert; SB.2022.00082 als Vorinstanz von 9C_416/2023; Autor:innenreihenfolge Hongler/Weder/Graf und Stocker/Schmid; Auswertung Hongler/Weder/Graf betrifft alle Handelsarten; Ziffern Engstler, Teuscher, Klöti-Weber, Stadelmann/Kocher. Nicht belegbares gestrichen oder abgeschwächt (Liquidationskosten nur «können abziehbar bleiben»; Verwaltungsrat-Bezug bei 9C_725/2022). Einzelheiten: `Fundstellenliste_2026-10-28.md`.

## Schlussprüfung (Schritt 9)

Hilfsagent nach den Prüfpunkten von `pruefung` (52 Befunde, `Schlusspruefung_Befunde_2026-10-28.md`). Umgesetzt: Widersprüche (Verpachtung altes/neues Recht, Bindung an Zuordnung, Soll-/Ist-Methode, BGBB-Unterstellung), Wiederholungen durch Querverweise ersetzt, unbestimmte Bezüge, Zuschreibung von Lehrmeinungen an Autor:innen statt «die Lehre», Reihenfolge der Belege in 14 Fussnoten, Erlass-Erstnennungen (ESTV, Änderungserlasse mit Datum, BdBSt-Aufhebung), Art. 18a Abs. 3 («Gesuch»), Sprache. Nicht übernommen (Hausgebrauch des Repositorys): Daten im Fliesstext in Ziffern, Apostroph «'», Abkürzungen kantonaler Gerichte, kantonale Materialien ohne URL; Medienmitteilung zur Individualbesteuerung (nicht geprüft, siehe oben). Neutralitätsdurchgang: `kommentar.py` ohne Treffer; offene Fragen als offen ausgewiesen.

## Offene Punkte für eine Nachführung

- Abstimmungsergebnis und Inkrafttreten der Individualbesteuerung belegen.
- Herausgeber:innen Internationales Steuerrecht der Schweiz (Bd. 122) und Autorname Teuscher (Bd. 120) am Titelblatt.
- Datum von BGer 2C_866/2016 (Cache: 6. Juni 2017; Obrist nennt 6. Juli 2017).
