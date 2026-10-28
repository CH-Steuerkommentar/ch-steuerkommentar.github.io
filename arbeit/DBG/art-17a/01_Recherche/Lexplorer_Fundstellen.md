# Lexplorer-Fundstellen zu Art. 17a DBG

Stand: 28.10.2026. Quelle: Lexplorer Tax (mcp-tax.lexplorer.ch). Wörtliche Zitate sind aus dem gelesenen Text kopiert.

**Suchzähler Lexplorer (search_chunks_*): 2 von höchstens 4.**
1. search_chunks_keyword, query «Mitarbeiterbeteiligungen echte unechte», filter_kanton BE, limit 8. Ergebnis: 1 Treffer (Art. 20a StG BE, nur Gesetz).
2. search_chunks_keyword, query «Mitarbeiteraktien», filter_kanton BE, filter_category 02-verwaltungspraxis, limit 8. Ergebnis: 3 Treffer (TaxInfo BE).

Alles andere wurde **navigierend** erreicht: nav_list_documents, nav_find, get_document_slice, get_chunk_content. nav_find-Muster waren «Mitarbeiterbeteiligung» (ohne Kanton und SG) sowie «Mitarbeiter» (LU, BE, AG, BS). Lexplorer wurde nicht für Rechtsprechung verwendet.

---

## Praxis

### P1. ESTV-KS Nr. 37 (Version 30.10.2020), Hauptdokument: nur Kennung
- Navigationsweg: nav_list_documents(source_id 5798ae15-307d-4518-821c-326012116e9a, «ESTV Kreisschreiben DBG»)
- Kennung: doc_id 03addb87-fb11-42d6-8443-7fdb1b08ceaf
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/03addb87-fb11-42d6-8443-7fdb1b08ceaf
- Der Text wurde in Open Case Law gelesen (estv_ks_dbst_ks_2020_1_037_d_de); siehe Verwaltungspraxis.md, Ziff. 1.

### P2. KS 37, Anhang I «Übersicht über Mitarbeiterbeteiligungen»
- Navigationsweg: wie P1 → get_document_slice (slice 0, vollständig)
- Kennung: doc_id f1133ebf-b909-4c12-8957-784594359a49
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/f1133ebf-b909-4c12-8957-784594359a49
- Fundstelle: Schaubild (Kopf «Anhang I zum Kreisschreiben Nr. 37 vom 22. Juli 2013»)
- Tragender Inhalt: Die Spalte «Phantom-Aktien/-Optionen SARs, etc.» hat den Zeitpunkt «Realisation (Zufluss des geldwerten Vorteils)». Die Spalte «Anwartschaften auf MA-Aktien» hat den Zeitpunkt «Realisation (d.h. Umwandlung in MA-Aktien)». Ob die Anwartschaften unter «echte» oder «unechte» stehen, ist aus der Textextraktion nicht eindeutig. Am PDF prüfen.

### P3. ESTV-KS Nr. 37A vom 4.5.2018 (Arbeitgeberin)
- Navigationsweg: wie P1 → get_document_slice (slices 0–1, slice_size 12000)
- Kennung: doc_id 5f831ad9-13db-4989-8493-dd9167882802
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/5f831ad9-13db-4989-8493-dd9167882802
- Fundstelle Ziff. 1, S. 3:
> «Für Einzelheiten und die Definition der verschiedenen Begriffe wird auf die Ausführungen im erwähnten Kreisschreiben verwiesen, welche vorliegend in analoger Weise zur Anwendung gelangen.»
- Fundstelle Ziff. 3.2.1, S. 5:
> «Im Konzernverhältnis beziehen sich die Mitarbeiterbeteiligungsmodelle häufig auf Aktien einer an der Börse kotierten Konzerngesellschaft (nahestehende Gesellschaft) der eigentlichen (d.h. zivilrechtlichen) Arbeitgeberin.»
- Fundstelle Ziff. 5.1, S. 7:
> «Bis zur vereinbarten Auslieferung der Aktien an die berechtigten Mitarbeitenden im Zeitpunkt des Ablaufs der Vestingperiode liegt somit eine Anwartschaft vor.»

### P4. ZH: ZStB Nr. 17a.1, Merkblatt vom 6.1.2025
- Navigationsweg: Kennung aus arbeit/DBG/art-17/01_Recherche/Lexplorer_Fundstellen.md (B3; Zürcher Steuerbuch doc cb70f7eb-5a94-4b36-aeba-10652145b7cc) → get_chunk_content (vollständig)
- Kennung: chunk_id b83b037a-d2d4-4e3d-aba7-6615bad4cfb8
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/cb70f7eb-5a94-4b36-aeba-10652145b7cc?chunk=b83b037a-d2d4-4e3d-aba7-6615bad4cfb8
- Fundstelle lit. B.I.1:
> «Als Mitarbeiteraktien im Sinne dieses Merkblatts gelten Aktien der arbeitgebenden Gesellschaft oder einer Gruppengesellschaft (nachfolgend «Arbeitgeber» genannt), die diese aufgrund vergangener, aktueller oder zukünftiger Arbeitsverhältnisse an Mitarbeitende überträgt.»
> «Werden die Beteiligungsrechte den Mitarbeitenden nicht durch den Arbeitgeber, sondern durch eine natürliche Person (z.B. aus dem Eigenbestand eines Aktionärs) abgegeben, handelt es sich zwar nicht um Mitarbeiterbeteiligungen nach Artikel 17a DBG im engeren Sinne.»
> «Instrumente, mit welchen sich der Arbeitgeber verpflichtet, den Mitarbeitenden in einem späteren Zeitpunkt – in der Regel bei Erfüllung bestimmter subjektiver oder objektiver Bedingungen – Mitarbeiteraktien einzuräumen, stellen blosse Anwartschaften auf den Erwerb von Mitarbeiteraktien dar […] (z.B. Restricted Stock Units).»
- Fundstelle lit. B.I.2:
> «Gesperrte Mitarbeiteraktien sind Mitarbeiteraktien, die mit vertraglichen Klauseln belastet sind, welche im Arbeitsverhältnis begründet sind und ihren Wert mindern.»

### P5. SG: StB 30 Nr. 2 «Steuerliche Behandlung von Mitarbeiterbeteiligungen» (Stand 1.1.2025)
- Navigationsweg: nav_find(«Mitarbeiterbeteiligung», filter_kanton SG) → get_document_slice (slices 0–1, vollständig)
- Kennung: doc_id 563bc34e-b2c3-4dd4-b945-5bc6585fa5cf
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/563bc34e-b2c3-4dd4-b945-5bc6585fa5cf
- Fundstelle Ziff. 1.2, S. 1–2:
> «Mitarbeiterbeteiligungen sind Beteiligungen, die auf ein ehemaliges, aktuelles oder künftiges Arbeitsverhältnis mit dem Arbeitgeber zurückzuführen sind.»
> «Die Mitarbeiteraktien sind von Gratisaktien (vgl. StB 33 Nr. 1) abzugrenzen. Mitarbeiteraktien werden auf der Grundlage eines Arbeitsverhältnisses ausgegeben, wohingegen Gratisaktien zulasten der Reserven der Gesellschaft liberiert und aufgrund der Aktionärseigenschaft an Personen abgegeben werden […].»
> «Unechte Mitarbeiterbeteiligungen berechtigen hingegen nicht zu einem Anspruch auf eine Beteiligung am Eigenkapital des Arbeitgebers, sondern stellen Anwartschaften auf blosse Bargeldabfindungen dar (Art. 30 Abs. 3 StG).»
- Fundstelle Ziff. 5, S. 5:
> «Bei einer Nachfolgelösung oder einer strategischen Beteiligung wird unterschieden, ob die Kaufpreisberechnung mittels Formelwert transparent gemacht wird oder nicht.»
> «Ob eine Nachfolgeregelung oder strategische Beteiligung vorliegt, wird im Einzelfall beurteilt.»

### P6. LU: Steuerbuch Bd. 1 «Mitarbeiteraktien und Mitarbeiteroptionen» (Einkommenssteuer, Stand 1.1.2024)
- Navigationsweg: nav_find(«Mitarbeiter», filter_kanton LU) → get_document_slice (vollständig)
- Kennung: doc_id 954c9fcd-8547-4dd1-8587-631847aad25a
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/954c9fcd-8547-4dd1-8587-631847aad25a
> «Die Besteuerung von Mitarbeiteraktien und -optionen richtet sich nach dem entsprechenden Kreisschreiben Nr. 37 der EStV vom 30. Oktober 2020 betreffend Besteuerung von Mitarbeiterbeteiligungen.»

### P7. LU: Steuerbuch Bd. 1 «Mitarbeiterbeteiligungen» (Vermögenssteuer, Stand 1.1.2024)
- Navigationsweg: wie P6
- Kennung: doc_id ba5b4aee-4e12-49a5-b3a5-37b4c2da0145
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/ba5b4aee-4e12-49a5-b3a5-37b4c2da0145
- Fundstelle Ziff. 1 und 3:
> «Anwartschaften auf den Erwerb von Mitarbeiteraktien unterliegen nicht der Vermögenssteuer, da sie keine definitiv erworbenen Vermögenswerte darstellen.»
> «Unechte Mitarbeiterbeteiligungen unterliegen nicht der Vermögenssteuer, da sie keine definitiv erworbenen Vermögenswerte darstellen.»

### P8. BE: TaxInfo «Mitarbeiterbeteiligungen» (Fassung vom 27.01.2022)
- Weg: **Suche Nr. 2** (search_chunks_keyword «Mitarbeiteraktien», BE, 02-verwaltungspraxis) → get_chunk_content
- Kennung: chunk_id 21316eec-9113-4c97-a6e8-241a03bca668 (doc 28edeed9-27cf-4444-bb20-95a75a525785)
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/28edeed9-27cf-4444-bb20-95a75a525785?chunk=21316eec-9113-4c97-a6e8-241a03bca668
> «Als Mitarbeiteraktien gelten Beteiligungspapiere des Arbeitgebers oder einer Konzerngesellschaft (Aktien, Genussscheine, Partizipationsscheine, Genossenschaftsanteile, Beteiligungen anderer Art). Dabei wird unterschieden zwischen freien Mitarbeiteraktien, Mitarbeiteraktien mit Sperrfrist und Anwartschaften auf Mitarbeiteraktien.»

### P9. BE: TaxInfo «Exkurs: Nicht börsenkotierte Mitarbeiteraktien» (Fassung vom 27.01.2022)
- Weg: Suche Nr. 2 → get_chunk_content
- Kennung: chunk_id 59719798-e155-4063-8c5a-89a1b545f050
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/28edeed9-27cf-4444-bb20-95a75a525785?chunk=59719798-e155-4063-8c5a-89a1b545f050
> «Gemäss Praxis der Steuerverwaltung des Kantons Bern wird die Anwendung dieser «5-Jahresregelung» nur dann geprüft, wenn im Erwerbszeitpunkt unsicher ist, ob ein ermittelter Formelwert als Verkehrswert von nicht börsenkotierten Mitarbeiteraktien gelten kann (typischerweise bei Start-up-Unternehmen).»

### P10. SZ: Merkblatt «Besteuerung von Mitarbeiterbeteiligungen» vom 18.11.2025
- Navigationsweg: nav_find(«Mitarbeiterbeteiligung», ohne Kanton) → get_document_slice (slices 0–2, vollständig)
- Kennung: doc_id 8755573e-cb4d-49c8-b826-ce3f5ba2b760
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/8755573e-cb4d-49c8-b826-ce3f5ba2b760
- Fundstelle Rz 26, S. 7:
> «Mitarbeiteraktien haben ihre Ursache in einem Arbeitsverhältnis. Sie setzen demnach einen kausalen Zusammenhang zwischen Arbeitsverhältnis und Erwerb voraus. Demgegenüber wird bei einem Erwerb von 100 % der Aktien – auch in Form eines von Anfang an geplanten gestaffelten Erwerbs – ohne eine Rückgabeverpflichtung bei Beendigung des Arbeitsverhältnisses von einer sog. Nachfolgeregelung ausgegangen.»
- Fundstelle Fn. 20, S. 7:
> «Der Mitarbeitende hat bis zum Vesting lediglich eine einkommenssteuerlich unbeachtliche Anwartschaft auf die Mitarbeiteroption.»
- Fundstelle Rz 33, S. 8: Die Bescheinigungspflicht gilt auch für Optionen, die «von einer in- oder ausländischen Muttergesellschaft oder einer anderen Konzerngesellschaft abgegeben und/oder verwaltet werden».

### P11. Negativbefunde und nur Gefundenes
- nav_find «Mitarbeiter» für AG, BS und BE: 0 Treffer. BE war nur über die Suchen erreichbar (P8, P9).
- Gefunden, nicht gelesen: MBV im Lexplorer (doc 28f816dc-1c9f-4fb8-8da2-217b3c58df0e; gelesen über Fedlex); NW «Bewertung von Mitarbeiterbeteiligungen» (2192cd80-1c0b-45ae-ad39-8fbcf0ab37a8); NW Vermögensbesteuerung (9ddbe75f-3e19-4bc6-b859-a15f6847a134); SH «Mitarbeiterbeteiligungen 18.1» (39e412f2-37a5-4e64-a612-cdb3cbe62520); TG StP 120a Nr. 1 (98f00095-17df-41b8-a9f1-c16ebc23df31); ESTV-Mitteilung 029-S-2026 (Umsatzabgabe; dd13b4ec-0f37-4380-9849-beb770b7201f); Art. 20a StG BE (chunk 2557a71b-0ce8-4915-9b82-ec95c4b53fb5, Suche Nr. 1, nur Vorschau).
- ILE-Literatur, nur über nav_find gefunden, für die Literaturrecherche: FStR 2002/1 (fa2e4f69-…), FStR 2002/3 (098d9241-…), FStR 2005/3 «Gesetzesentwurf im Parlament» (53e71ab8-…), FStR 2023/1 (b692106b-…), FStR 2025 (65957644-…), St.Galler Seminar Einkommenssteuer 2020 «Mitarbeiterbeteiligung» (d51d1cd9-…), Seminar Unternehmensbesteuerung 2023 (0f830659-…), Internationales Steuerseminar 2019 (c78ae5b0-…).

## ILE-Literatur (Art. 17a DBG)

Ausführlich in `ILE_Literatur.md` (gleicher Ordner; 11 Lexplorer-Suchen, Stand 28.10.2026). Kurzübersicht der verwendbaren Fundstellen:
- Oesterhelt/Gammeter, FStR 2024, Ziff. 3.1–3.5 (Begriff, Mitarbeiter/VR, Kausalität, Investoren-/Gründeraktien, Abgabe durch Aktionär), Ziff. 2.1 f. (Phantom Stocks/SAR unecht), Ziff. 10 (Co-Investments unecht), Ziff. 11.5 (importierte Aktien) – https://app.lexplorer.ch/suche?e_id=592&e_sys=ile
- Oesterhelt, FStR 2021, Rechtsprechung 2019/2020 (Teil 2), Ziff. 5.3 (2C_1057/2018; Erwerb vom Aktionär, qualifizierte Beteiligung) – https://app.lexplorer.ch/suche?e_id=267&e_sys=ile
- Oesterhelt/Opel, FStR 2025, Rechtsprechung 2025-1, Ziff. 1.3, S. 46–48 (9C_168/2023; RSU/PSU-Aktien als Naturallohn) – https://app.lexplorer.ch/suche?e_id=599&e_sys=ile
- Risi/Schmid, FStR 2005, Ziff. 4, 6.1, 6.2 (Entwurf; SR 31.5.2005; RSU als Zero Strike Options) – https://app.lexplorer.ch/suche?e_id=318&e_sys=ile
- Seminare: Buchmann/Schreiber 2019; Oesterhelt/Truffer 2020; Meister 2020; Risi/Bertschinger 2023; Bucher/Marbach 2022; Oesterhelt/Tschan 2025; Fenners/Oesterhelt 2025.
- Kein ILE-Treffer zu 2C_705/2017, 2C_285/2019, 9C_41/2024, 9C_13/2025, «BGE 151 II 545».
- Nachtrag: Risi, FStR 2002, Ziff. 4.3 (Bericht der gemischten Arbeitsgruppe: Unterscheidung echt/unecht, «Art. 17a» des AG-Vorschlags) – https://app.lexplorer.ch/suche?e_id=110&e_sys=ile (über nav_find, ohne Suche).
