# Art. 17d DBG – ILE-Literatur und Verwaltungspraxis (Lexplorer Tax)

Stand: 28.10.2026, ca. 07:15 UTC. Quelle: Lexplorer Tax (Kategorie «08-institut-fuer-law-und-economics», filter_kanton «CH») und lokale Quelltexte der Vorarbeit. Keine Websuche, keine Rechtsprechung über Lexplorer.

## 0. Status: Lesesperre, Auswertung unvollständig

- **Blocker:** Beim ersten Leseaufruf meldete Lexplorer Tax für alle Lese- und Navigationswerkzeuge (get_chunk_content, get_document_slice, nav_*): «Tageslimite für das Lesen und Navigieren erreicht (2000 Aufrufe, Fair Use). Ab 00:00 UTC wieder verfügbar.» Die Suchwerkzeuge funktionieren weiter. Sie liefern aber nur eine Vorschau von etwa 300 Zeichen je Treffer.
- **Folge:** An diesem Tag wurde **kein Chunk neu ganz gelesen**. Das gilt auch für die Chunks aus der Vorarbeit (Peyer/Schreiber/Walt, Oesterhelt/Truffer, Oesterhelt/Gammeter, Brozzo/Stocker, Allemann/Bloch-Riemer). Für den Anhang II von KS 37, den Anhang IV und die kantonalen Weisungen gilt dasselbe.
- **Was trotzdem verwendbar ist:**
  1. Wörtliche Zitate, die frühere Agenten **ganz gelesen** und in den Vorarbeit-Dateien festgehalten haben (art-17b, art-17c). Sie sind unten mit «[Vorarbeit, heute nicht neu gelesen]» markiert.
  2. Der Wortlaut von KS 37 Ziff. 7, den ich in der lokalen Datei `art-17b/01_Recherche/quellen/KS37_ESTV_2020.txt` ganz gelesen habe (S. 11–18).
  3. Die Botschaft BBl 2005 575, die ich in der lokalen Datei `art-17b/01_Recherche/quellen/Botschaft_BBl_2005_575.txt` gelesen habe (nur für Sachfrage 7, Entstehungsgeschichte).
- **Neue Treffer** aus den heutigen Suchen sind als «Kandidat, Lesen ausstehend» aufgeführt. Belegt sind dafür nur Titel, Abschnitt, IDs und URL, keine Aussagen. Die Vorschautexte sind als solche gekennzeichnet und nicht zitierfähig.
- **Fortsetzung:** Nach 00:00 UTC (29.10.2026, 01:00 MEZ) die Leseliste in Ziff. 4 abarbeiten. Dafür sind keine weiteren Suchen nötig.

## 1. Suchprotokoll

Zähler: **8 Suchen (search_chunks_*) von höchstens 14.** Alle mit search_chunks_hybrid, filter_kanton «CH», filter_category «08-institut-fuer-law-und-economics». Leseaufrufe: 6 Versuche (5 × get_chunk_content, 1 × get_document_slice), alle durch die Tageslimite abgewiesen.

| Nr. | Werkzeug | Abfrage | Sachfrage | Treffer |
|---|---|---|---|---|
| 1 | hybrid, limit 10 | «Mitarbeiteroptionen Vestingperiode Zuzug Wegzug anteilsmässige Besteuerung Arbeitstage Art. 17d DBG Ende des Arbeitsverhältnisses beschleunigtes Vesting good leaver» | 1 | 10 (Brozzo/Stocker 2024 ×2; Seminar Unternehmensbesteuerung 2023 «internationale Vesting-Periode»; FStR 2002/3 «Zeitpunkt der Besteuerung von Mitarbeiteroptionen»; Risi/Schmid FStR 2005/3 Ziff. 6.4; sonst schon bekannt) |
| 2 | hybrid, limit 10 | «Arbeitstage oder Kalendertage Ferien Abwesenheiten Drittstaatentage Berechnung Schweizer Anteil Mitarbeiterbeteiligung Vestingperiode Progressionsvorbehalt Import» | 2 | 10 (nur Grenzgänger/Homeoffice/Nichtrückkehrtage; Seminar 2015 «Internationale Mitarbeiterentsendung»; nichts unmittelbar zu Art. 17d) |
| 3 | hybrid, limit 10 | «Quellensteuer Art. 97a DBG 11,5 Prozent Arbeitgeber Schuldner Art. 100 Abs. 1 lit. d DBG ausländische Konzerngesellschaft Mitarbeiteroptionen nach Wegzug ausgeübt» | 4 | 10 (Allemann/Bloch-Riemer 2021 ×5; Brozzo/Stocker 2024; neu: FStR 2025 «Steuerliche Behandlung von Mitarbeiterbeteiligungen auf Seiten des Arbeitgebers», Exemple 2; Seminar 2022 «C-Level Hires») |
| 4 | hybrid, limit 10 | «OECD-Musterkommentar Art. 15 Ziff. 12.14 Mitarbeiteroptionen Aufteilung Besteuerungsrecht Tätigkeitsstaat Doppelbesteuerung Verständigungsverfahren Grenzgänger Art. 15a DBA Deutschland» | 5 | 10 (FStR 2002/3 «Vorschläge der OECD …»; Niederbacher-Puchegger/Risi FStR 2005/1 ×4; FStR 2012/2 Arbeitgeberbegriff; FStR 2025 Rechtsprechung 2025-2, nur Materialienliste) |
| 5 | hybrid, limit 10, filter_source_id FStR (fdd29b9d-…) | «Rechtsprechung 2025 Bundesgericht Mitarbeiteroptionen Vestingperiode Wohnsitz im Ausland anteilsmässige Besteuerung Art. 17d DBG OECD-Musterkommentar Bemerkungen» | 5 (9C_13/2025) | 10 (nur Inhaltsverzeichnisse und Materialienlisten der Rechtsprechung 2023/1, 2025/1, 2025-2, 2025/4; **kein Treffer zu 9C_13/2025**) |
| 6 | hybrid, limit 8 | «interkantonaler Wohnsitzwechsel während Vestingperiode Mitarbeiteroptionen Besteuerung Wohnsitzkanton Ende Steuerperiode keine pro rata Aufteilung zwischen Kantonen» | 6 | 8 (nur Oesterhelt/Truffer 2020, Folie «Interkantonale Aspekte»; sonst Vorsorge und juristische Personen; **keine pro-rata-Lehre**) |
| 7 | hybrid, limit 8 | «Rundschreiben ESTV 2003 Vesting-Klauseln Mitarbeiteroptionen Besteuerung beim Vesting internationale Ausscheidung Bericht gemischte Arbeitsgruppe Anteil Schweiz» | 7 | 8 (FStR 2002/3 «Zeitpunkt der Besteuerung von Mitarbeiteroptionen» ×3; Risi FStR 2002/3 Bericht der gemischten Arbeitsgruppe ×2) |
| 8 | hybrid, limit 10 | «Anwartschaften RSU Zuzug in die Schweiz anteilsmässige Besteuerung gesetzliche Grundlage Mitarbeiterbeteiligungsverordnung Art. 7 MBV Bonus in Aktien Auslandstätigkeit Wortlaut gesperrte Mitarbeiteroptionen» | 3 | 10 (Risi/Schmid FStR 2005/3 Ziff. 6.2 RSU, Ziff. 6.4 Beispiel; Oesterhelt/Truffer 2020 «Gesetzliche Grundlagen»; Seminar 2023 Arbeitgebersicht) |
Verbleibendes Budget: 6 Suchen (bewusst offen gelassen; die Fortsetzung braucht nur Lesezugriffe).

Treffer aus «ILE-HSG — Lehrbuch Steuerrecht» (source_slug ile-lehrbuch-steuerrecht): keine vorgekommen.

---

## 2. A. ILE-Literatur je Sachfrage

### Sachfrage 1: Referenzperiode (Erwerb bis Vesting), Austritt, beschleunigtes Vesting

**Verwendbar (Vorarbeit):** Keine ILE-Fundstelle, die das Ende der Referenzperiode bei Austritt, good/bad leaver oder beschleunigtem Vesting für Art. 17d DBG behandelt. Zu einem beschleunigten Vesting gibt es nur eine Stelle zu Aktien mit Sperrfrist (Oesterhelt/Truffer 2020, Folie 27 «acclerated [sic] Vesting aufgrund eines Exits»; art-17b ILE 4.2). Sie betrifft Art. 17b Abs. 2 und nicht Art. 17d.

**Kandidaten, Lesen ausstehend:**
- Stocker/Brozzo, Seminar Einkommenssteuer, Vorsorge und Sozialversicherungen 2024, «Verwaltungsratshonorare und Abgangsentschädigungen», Folie «Steuern und Sozialabgaben bei Mitarbeiteroptionen nach Wegzug» (Ausgangslage). Chunk ccf5bcc2-26c5-4247-93e6-cc7d8428be9c, doc fb5c4aa5-bbbe-47e6-9d08-21a3b13c9da8, https://app.lexplorer.ch/suche?e_chunks=51316&e_sys=ile. Vorschau (nicht zitierfähig): «Anna hatte bis 30. Juni 2022 Wohnsitz in Zürich und w…». Referent:innen nach Vorarbeit art-17: Raoul Stocker, Hanna Brozzo (Bär & Karrer); am Chunk-Ende prüfen.
- Dieselben, Folie «Steuerliche Behandlung von Mitarbeiteroptionen bei internationaler Tätigkeit – Variante 5: Lösungshinweise». Chunk f60abd82-de6c-4651-8c37-fdbdfaa0c939, https://app.lexplorer.ch/suche?e_chunks=51317&e_sys=ile. Die Folgefolien (Varianten 1–4) über nav_list_chunks des doc fb5c4aa5 suchen.
- St.Galler Seminar zur Unternehmensbesteuerung 2023, «Mitarbeiterbeteiligungspläne aus Sicht der Arbeitgeberin bzw. im Konzern», Folie «Verrechnung von Mitarbeiteraktien bei internationaler Vesting-Periode». Chunk 7a93985f-a880-467c-9436-376ff9a038db, doc 0f830659-3e56-4e4b-a618-2509cf93d958, https://app.lexplorer.ch/suche?e_chunks=53579&e_sys=ile. Nach Vorarbeit art-17b ist das wohl Bertschinger/Risi (Arbeitgebersicht, KS 37A). Für Art. 17d voraussichtlich nur am Rand (Weiterbelastung).

### Sachfrage 2: Zählweise (Arbeitstage/Kalendertage, Ferien, Drittstaatentage)

**Verwendbar (Vorarbeit):** Keine ILE-Fundstelle zur Zählweise nach Art. 17d DBG beziehungsweise Art. 7/8 MBV. Allemann/Bloch-Riemer 2021 (unten Sachfrage 4) verweisen nur allgemein auf die Vestingperiode.

**Negativbefund Suche Nr. 2:** Die Treffer betreffen Nichtrückkehrtage nach Art. 15a DBA-D und Homeoffice/Grenzgänger. Sie betreffen nicht die Mitarbeiterbeteiligung (Seminar 2024 «Grenzgänger und Homeoffice», doc 3e260ccc-8b96-4ab8-ab3e-c141120b1556; Internationales Steuerseminar 2025 «Erfahrungen aus Verständigungsverfahren», doc ebe3df5f-1f6c-4ebf-9d5b-33021df25ebf; Internationales Steuerseminar 2015 «Internationale Mitarbeiterentsendung», chunk ade0b4a8-0783-495f-ba4c-f411ca310343, https://app.lexplorer.ch/suche?e_chunks=63175&e_sys=ile). Diese Fundstellen allenfalls für Art. 15a DBA-D lesen (Sachfrage 4).

Die Praxis zur Zählweise steht in KS 37 Ziff. 7.1 (siehe 3.1).

### Sachfrage 3: Anwendungsbereich (nur gesperrte Optionen; Ausdehnung durch MBV/KS 37)

**Verwendbar (Vorarbeit):**

(a) **Oesterhelt/Gammeter, FStR 2024 (Heft 4), «Das Formelwertprinzip bei Mitarbeiteraktien. Darstellung anhand der Praxis im Kanton Zürich», Ziff. 11.6** [Vorarbeit art-17c F.2, damals über get_document_slice Slice 9 gelesen; heute nicht neu gelesen]
- Chunk-ID 27617312-3b9d-4265-acc1-bd769efedb1f (Lexplorer-Chunk 60); doc_id fb1b2dda-d30d-4c1d-9bed-e363bc738452
- Autoren: Stefan Oesterhelt (Homburger AG), Thomas Gammeter (Leiter Abteilung Wertschriften, KStA ZH)
- lexplorer_url: https://app.lexplorer.ch/suche?e_id=592&e_sys=ile (Dokument; eine Chunk-URL ist für diese Stelle nicht ausgegeben worden)
- Zitat: «Das Besteuerungsrecht für Erwerbseinkommen steht hingegen gemäss Art. 15 Abs. 1 OECD-MA dem Tätigkeitsstaat zu. Dies gilt auch für Mitarbeiterbeteiligungen.» / «Unabhängig vom Besteuerungsrecht stellt sich zudem die Frage, ob die Schweiz überhaupt eine rechtliche Grundlage hat, um den nach dem Wegzug erzielten Übergewinn zu besteuern. Während für Mitarbeiteroptionen in Art. 97a DBG eine entsprechende Bestimmung besteht, fehlt eine solche Regelung für Mitarbeiteraktien. Eine eindeutige Praxis der Steuerbehörden zu dieser Frage hat sich noch nicht herausgebildet.»
- Einordnung: **weiterführend.** Die Stelle betrifft den Übergewinn auf Aktien nach Wegzug. Sie belegt, dass die Autoren Art. 97a DBG wortlautgemäss nur auf Mitarbeiteroptionen beziehen. Zu RSU und unechten Beteiligungen äussern sie sich nicht. Gammeter ist Praxisvertreter (KStA ZH).
- Kurzzitat: Oesterhelt/Gammeter, FStR 2024, Das Formelwertprinzip bei Mitarbeiteraktien, Ziff. 11.6.

(b) **Oesterhelt/Truffer, St.Galler Seminar zur Einkommenssteuer 2020, «Mitarbeiterbeteiligung», Folie «Interkantonale Aspekte»** [Vorarbeit art-17c F.1, damals über get_chunk_content gelesen; heute nicht neu gelesen]
- Chunk-ID d4d4fb91-3255-4685-9e4f-eb717cd00853; doc_id d51d1cd9-28c6-40c5-a671-0cbd63539415
- Referent:innen: Stefan Oesterhelt (Homburger), Ildiko Truffer (KStA ZH)
- lexplorer_url: https://app.lexplorer.ch/suche?e_chunks=56676&e_sys=ile
- Zitat: «Falls Wohnsitz im Ausland: keine Rechtsgrundlage für Quellenbesteuerung, da Art. 97a DBG nur auf Mitarbeiteroptionen i.S.v. Art. 17b Abs. 3 DBG anwendbar ist. (Aber evtl. Kapitalgewinnbesteuerung im Ausland).»
- Einordnung: **weiterführend.** Die Folie betrifft den Übergewinn bei Aktien. Sie enthält aber dieselbe Wortlautlesung von Art. 97a wie (a). Für RSU und unechte Beteiligungen sagt sie nichts. Sie steht in Spannung zu KS 37 Ziff. 7.3, Art. 7/8 MBV und ZStB 100.1 (siehe 3.1, 3.4).
- Kurzzitat: Oesterhelt/Truffer, ILE-Seminar Einkommenssteuer 2020, Mitarbeiterbeteiligung, Folie «Interkantonale Aspekte».

(c) **Peyer/Schreiber/Walt, Internationales Steuerseminar 2024, «Aktuelles aus Verständigungsverfahren Deutschland, Österreich, Liechtenstein und Schweiz», Folie «MA-Beteiligungen – Nationales Steuerrecht»** [Vorarbeit art-17b 5.5 und art-17c F.3; heute nicht neu gelesen]
- Chunk-ID 56ca079c-8a59-468f-bf7c-33f08a066890; doc_id 5c0ecafe-99c5-4798-b2d0-9dd22adf29fb
- Referent:innen: Basil Peyer, Susanne Schreiber, Martina Walt
- lexplorer_url: https://app.lexplorer.ch/suche?e_chunks=50258&e_sys=ile
- Zitat: «Besteuerungszeitpunkt: Art. 97d DBG: anteilsmässige Besteuerung bei gesperrten MA-Optionen, Art. 17d DBG» / «Praxis, KS 37 MA-Beteiligungen, Ziff. 3.4.3.: […] keine Aussage zu internationalen Konstellationen bei echten MA-Beteiligungen mit Übergewinnbesteuerung»
- Einordnung: **bestätigend** für den Wortlaut, nämlich anteilsmässige Besteuerung bei gesperrten Optionen. Die Folie zitiert «Art. 97d» falsch; gemeint ist wohl Art. 97a. Sie stellt zudem fest, dass KS 37 für den Übergewinn bei Aktien im internationalen Verhältnis keine Aussage macht.
- Kurzzitat: Peyer/Schreiber/Walt, ILE Internationales Steuerseminar 2024, Aktuelles aus Verständigungsverfahren Deutschland, Österreich, Liechtenstein und Schweiz, Folie «MA-Beteiligungen – Nationales Steuerrecht».

**Befund:** Keine ILE-Fundstelle, die die Ausdehnung von Art. 17d DBG auf RSU/Anwartschaften oder unechte Beteiligungen durch Art. 7/8 MBV und KS 37 ausdrücklich prüft, bejaht oder verneint (ebenso Vorarbeit art-17c F.5). Zum Bonus in Aktien für eine Auslandstätigkeit: kein ILE-Treffer. Die Praxis dazu steht in KS 37 Ziff. 7.2.1 und 7.3.3 (siehe 3.1).

**Kandidaten, Lesen ausstehend:**
- Risi/Schmid, FStR 2005 (Heft 3), «Besteuerung von Mitarbeiterbeteiligungen – Gesetzesentwurf im Parlament». Gelesen werden sollen Ziff. 6.4 «Internationale Steuerausscheidung vor allem bei mehreren Arbeitsverhältnissen» (chunk 100490ab-e489-44c8-9252-232acc2cc642, https://app.lexplorer.ch/suche?e_chunks=8686&e_sys=ile) und das Beispiel (chunk f1a5b791-980c-4573-8177-94bf99f477c6, https://app.lexplorer.ch/suche?e_chunks=8687&e_sys=ile; Vorschau: «Eine in Grossbritannien ansässige Person hat am 1. Juli 2003 Optionen mit einer Vestingperiode von 3 Jahren …»). doc 53e71ab8-7ab3-426d-99b6-15c23a9e2665. Die Stelle betrifft den Entwurf. Zur RSU-Frage (Ziff. 6.2) siehe Vorarbeit art-17b 1.5.
- Oesterhelt/Truffer 2020, Folie «Gesetzliche Grundlagen zur Besteuerung von Mitarbeiterbeteiligungen» (chunk dedea00a-3970-4ecb-9b9a-e9e01ce1237a, https://app.lexplorer.ch/suche?e_chunks=56660&e_sys=ile). Voraussichtlich nur eine Aufzählung der Rechtsgrundlagen.

### Sachfrage 4: Import/Export/Reimport, Progressionsvorbehalt, Quellensteuer Art. 97a, Arbeitgeberhaftung Art. 100 Abs. 1 lit. d, Grenzgänger, VR

**Verwendbar (Vorarbeit):**

**Allemann/Bloch-Riemer, Internationales Steuerseminar 2021, «Arbeitgeber in der Haftung – Quellensteuern und Sozialversicherungen im internationalen Verhältnis», Folie «Mitarbeiterbeteiligungsprogramme, Bonuspläne, Abgangsentschädigungen und Entlassungen nach 58. Geburtstag»** [Vorarbeit art-17c F.4; heute nicht neu gelesen]
- Chunk-ID c637de6e-34b7-4fff-b804-ab558ed20ae4; doc_id 3ac15de8-f2da-48cd-8270-57de8500f5c0
- Referent:innen (Chunk-Ende): Patrick Allemann, Ruth Bloch-Riemer
- lexplorer_url: https://app.lexplorer.ch/suche?e_chunks=58607&e_sys=ile
- Zitat (Tabelle): «Steuerpflicht | Art. 84 Abs. 2 lit. a DBG | Art. 97a Abs. 1 DBG» – «International im Verhältnis zur Vestingperiode in der Schweiz, grundsätzlich Besteuerung mit restlichem Einkommen | KS 45 Ziff. 3.2.2 und Ziff. 5.2»
- Einordnung: **weiterführend.** Die Folie verweist auf das KS 45 ESTV, das in der Vorarbeit nicht ausgewertet wurde. Sie bestätigt die Anknüpfung an die Vestingperiode.
- Kurzzitat: Allemann/Bloch-Riemer, ILE Internationales Steuerseminar 2021, Arbeitgeber in der Haftung, Folie «Mitarbeiterbeteiligungsprogramme, Bonuspläne, Abgangsentschädigungen und Entlassungen nach 58. Geburtstag».

**Kandidaten, Lesen ausstehend (für Art. 97a/100 Abs. 1 lit. d am ergiebigsten):**
- Allemann/Bloch-Riemer 2021, Folie «Schuldner der Steuerbaren Leistung – Schweizer Arbeitgeber als Schuldner» (chunk bd1da586-b4cf-4b37-a018-e9dbad34b07d, https://app.lexplorer.ch/suche?e_chunks=58602&e_sys=ile) und Folie «Schuldner der steuerbaren Leistung bei der Quellensteuer (DBG)» (chunk 497fd81d-874b-45b0-b509-6ef69a3115a4, https://app.lexplorer.ch/suche?e_chunks=58601&e_sys=ile; Vorschau: «Keine Legaldefinition, nur Pflichten auf…»).
- FStR 2025, «Steuerliche Behandlung von Mitarbeiterbeteiligungen auf Seiten des Arbeitgebers», Abschnitt «Exercice d'options et imposition à la source en cas d'expatriation», Exemple 2 (chunk b6732f35-3b4d-49b6-a483-72767fe5b2dc, doc 65957644-9a5b-4dfc-975d-2a79f6648ac5, https://app.lexplorer.ch/suche?e_chunks=41314&e_sys=ile). Vorschau: «A reçoit 100 options selon les modalités décrites dans l'exemple 1. Le 1er janvier 2023, A déménage à l'étran…». Autor:innen am Chunk-Ende feststellen. **Wahrscheinlich die ergiebigste neue Fundstelle zu Art. 97a/100 Abs. 1 lit. d.**
- Stocker/Brozzo 2024, siehe Sachfrage 1 (Optionen nach Wegzug; Steuern und Sozialabgaben).
- St.Galler Seminar zur Unternehmensbesteuerung 2022, «C-Level Hires – Quellensteuern und Sozialversicherungen im internationalen Verhältnis», Folie «Quellensteuer: Zentrale Aspekte aus Schweizer Sicht» (chunk b650e98f-6311-4aa0-a512-9be46971e8da, doc 5edc2a4f-859d-43f9-89b9-fd2c705c31c3, https://app.lexplorer.ch/suche?e_chunks=55147&e_sys=ile).

### Sachfrage 5: DBA/OECD-MK Ziff. 12.14 zu Art. 15, Doppelbesteuerung, Verständigungsverfahren, 9C_13/2025

**Verwendbar (Vorarbeit):** Oesterhelt/Gammeter, FStR 2024, Ziff. 11.6, erster Satz (siehe Sachfrage 3 lit. a): Besteuerungsrecht nach Art. 15 Abs. 1 OECD-MA beim Tätigkeitsstaat, «auch für Mitarbeiterbeteiligungen». Peyer/Schreiber/Walt 2024 (Verständigungsverfahren), siehe Sachfrage 3 lit. c.

**9C_13/2025:** Wie in der Vorarbeit art-17b (Suchen I4, I14) kein ILE-Treffer. Suche Nr. 5 (auf die FStR beschränkt) traf nur Inhaltsverzeichnisse und Materialienlisten:
- FStR 2025, Rechtsprechung 2025-2 (Oesterhelt/Opel), doc 92ba09fe-6240-40f5-b624-8bd7fb30a572. Die Materialienliste nennt den OECD-MK (chunk 0edd9bf0-1e5d-4e88-b347-fbe7b23ffe4a, https://app.lexplorer.ch/suche?e_chunks=14644&e_sys=ile) und das SSK KS 1 vom 30.6.2010 (chunk c95bbba4-…, https://app.lexplorer.ch/suche?e_chunks=14645&e_sys=ile). Das Inhaltsverzeichnis steht in chunk e3f99ab9-6d23-40ee-9aa0-82515c1a77ef (https://app.lexplorer.ch/suche?e_chunks=14565&e_sys=ile). **Lesen:** Ob eine Besprechung von 9C_13/2025 darin steht, ist offen.
- FStR 2025, Rechtsprechung 2025/4, doc f1ed9b62-9922-4e8b-ad23-1fab619e4353 (Materialien: WBK «unbeschränkte Steuerpflicht»; chunk e03ea08b-37d3-46c2-9de8-aa681858e250, https://app.lexplorer.ch/suche?e_chunks=45345&e_sys=ile). Das Inhaltsverzeichnis lesen.
- FStR 2023/1, Rechtsprechung im Steuerrecht 2023/1, doc 82247d36-873a-40e2-b4a2-2a03d9a190b5. Die Materialienliste nennt KS 37 (chunk d85947de-554f-46a4-8d17-58659765ba76, https://app.lexplorer.ch/suche?e_chunks=12857&e_sys=ile), was auf eine Besprechung zu Mitarbeiterbeteiligungen hindeutet. Das Inhaltsverzeichnis lesen.

**Kandidaten OECD (historisch/weiterführend), Lesen ausstehend:**
- FStR 2002/3, «Vorschläge der OECD zur Vermeidung der internationalen Doppelbesteuerung auf Mitarbeiteroptionen», Ziff. 4.2 «Besteuerung als Erwerbseinkommen» (chunk 8a126594-a4e0-4c5e-822d-4b81629c1a62, doc 10ecde5b-db3e-43f4-9462-07514ba50a56, https://app.lexplorer.ch/suche?e_chunks=2805&e_sys=ile). Das ist der OECD-Entwurf, auf den die Botschaft verweist.
- Niederbacher-Puchegger/Risi, FStR 2005 (Heft 1), «Mitarbeiteroptionen und Verrechnungspreis-Aspekte von Optionsprogrammen», doc 0da9c2e0-495d-49b8-950c-ea06643fa42e: «Besteuerungsrecht gemäß Artikel 15 OECD-MA» (chunk db34664a-1795-425f-bfeb-b76ffb01b71c, https://app.lexplorer.ch/suche?e_chunks=8519&e_sys=ile), Ziff. 4.1 OECD-Bericht «Cross-Border Income Tax Issues …» (chunk af4db2d4-76ac-4fe3-9efe-61a147c5293f, https://app.lexplorer.ch/suche?e_chunks=8515&e_sys=ile) und chunk 4ef57451-c991-4ddc-9fa6-db7c2f4e808c (https://app.lexplorer.ch/suche?e_chunks=8526&e_sys=ile). Autor:innen laut Chunk-Ende von Ziff. 6: Ingrid Niederbacher-Puchegger, Andreas Risi (Suchtreffer 9b04a6cd).

### Sachfrage 6: Interkantonale Verhältnisse (Wohnsitzwechsel in der Schweiz während des Vesting)

**Befund (Suche Nr. 6): keine ILE-Lehre zu einer interkantonalen pro-rata-Aufteilung nach Vestingperiode.** Einziger einschlägiger Treffer ist Oesterhelt/Truffer 2020, Folie «Interkantonale Aspekte» (chunk d4d4fb91-…, https://app.lexplorer.ch/suche?e_chunks=56676&e_sys=ile). Ihre Vorschau (heute im Suchresultat gelesen, nicht der ganze Chunk) lautet: «Besteuerung des "Übergewinns" durch den Wohnsitzkanton am Ende der Steuerperiode in welchem die Veräußerung erfolgt.» Die Folie betrifft den Übergewinn auf Aktien, nicht Optionen. Für die Optionsausübung geht sie nach der Vorschau von der Grundregel aus (Wohnsitzkanton am Ende der Steuerperiode). Am ganzen Chunk prüfen, bevor die Stelle für Optionen herangezogen wird.

### Sachfrage 7: Altes Recht vor 2013 (Entstehungsgeschichte)

**Materialien (lokal gelesen, Botschaft vom 17.11.2004, BBl 2005 575; Datei `art-17b/01_Recherche/quellen/Botschaft_BBl_2005_575.txt`):**
- S. 576 (Übersicht): Es ist sicherzustellen, «dass die schweizerischen Unternehmen die anteilsmässigen Steuern auf den geldwerten Vorteilen abliefern, die der Dauer der in der Schweiz ausgeübten Tätigkeit des oder der Mitarbeitenden (gemessen an der gesamten Zeitspanne zwischen der Zuteilung der Option und dem Entstehen des Ausübungsrechts) entspricht.»
- Ziff. 1.3.5 «Die erweiterte Quellenbesteuerung»: «In Anlehnung an eine OECD-Empfehlung (vgl. Ziff. 1.4.3) gilt der geldwerte Vorteil aus der Optionsausübung als Arbeitseinkommen, das in der Zeit zwischen der Zuteilung und dem unwiderruflichen Erwerb des Ausübungsrechts verdient worden ist.» / «Wenn der Mitarbeiter die Optionen später im Staate C ausübt, steht diesem das Besteuerungsrecht nicht zu, da es sich nicht um Einkommen aus einer Arbeitstätigkeit auf seinem Gebiet handelt.»
- Zu Art. 17d (S. 596 f.): «Mit diesem Artikel wird die Grundlage für das anteilsmässige Besteuerungsrecht der Schweiz gelegt. Das Arbeitseinkommen unterliegt auch dann der Steuerpflicht, wenn der geldwerte Vorteil im Ausland realisiert wird.» Beispiel: Sperre fünf Jahre, zwei Jahre im Land A, drei Jahre in der Schweiz, Ausübung im siebten Jahr im Land B: «Nach diesem Artikel kann die Schweiz Dreifünftel – also 30 – und Land A Zweifünftel der geldwerten Leistung besteuern.» Zur alten Praxis: «Damit gibt die Schweiz ihre bisherige, unbefriedigende Praxis auf. Nach dieser Praxis musste ein Mitarbeiter, der im Ausland nicht bewertbare Optionen erhalten und diese Optionen nach einem Zuzug in die Schweiz ausgeübt hat, seinen mit der Ausübung erzielten geldwerten Vorteil voll versteuern.»
- Zu Art. 97a (S. 597): «Eine Wegzugbesteuerung würde hier keinen Sinn machen. Zum einen kennt das DBG die Wegzugbesteuerung nicht, zum andern hat der Mitarbeiter beim Wegzug nichts realisiert.» Satz 11,5 %, «da ohnehin die meisten Kaderleute bei der Besteuerung in der Schweiz diesem Satz unterliegen».
- Zu Art. 100 Abs. 1 lit. d (S. 597): «Wesentlich ist, dass das schweizerische Unternehmen zur Steuerschuldnerin wird, auch wenn sie dem ehemaligen Arbeitnehmer den geldwerten Vorteil selber nicht direkt ausrichtet. Sie wird sich entweder bei der ausländischen Mutter- oder Gruppengesellschaft schadlos halten oder die Steuer beim inzwischen im Ausland wohnhaften Mitarbeiter einfordern müssen.»
- StHG (S. 598): «Artikel 97a Absatz 2 DBG darf daher nicht in Artikel 35 Absatz 1 Buchstabe i StHG übernommen werden, da es sich um eine tarifarische Vorschrift handelt.» Achtung: Die Konkordanz der Botschaft nennt «Art. 7d» als StHG-Parallele zu Art. 17d DBG. Geltendes Recht ist Art. 7f StHG. Vor einem Zitat prüfen.
- Hinweis: Das Beispiel der Botschaft verweist noch auf die «Freistellung nach Artikel 17b Absatz 3», die später gestrichen wurde (Vorarbeit art-17b ILE 8.2).

**ILE (Vorarbeit, heute nicht neu gelesen):** Risi, FStR 2002 (Heft 3), Bericht der gemischten Arbeitsgruppe, doc 098d9241-b114-47e9-84ab-a4295a913c7e, https://app.lexplorer.ch/suche?e_id=110&e_sys=ile: «Einzig bei den Optionen ergibt sich eine grundlegende Änderung: Die Arbeitsgruppe hat sich für die grundsätzliche Besteuerung von Mitarbeiteroptionen im Zeitpunkt des Vestings entschieden.» (zitiert nach art-17a ILE_Literatur.md Z. 161). Ablauf der Gesetzgebung: Gesetzgebungs-Agenda FStR 2006/3, 2010/4, 2011/2 (Vorarbeit art-17b ILE 8.2).

**Kandidaten, Lesen ausstehend:** FStR 2002/3, «Zeitpunkt der Besteuerung von Mitarbeiteroptionen» (doc bcb05a17-7ff8-410e-a3d9-891597f8647a): «Empfehlung zur Besteuerung bei Vesting durch gemischte Arbeitsgruppe» (chunk 4585df42-cce8-4a26-aeae-510d7c8ddf0b, https://app.lexplorer.ch/suche?e_chunks=2989&e_sys=ile), «Steuerliche Vorteile beim Vesting» (chunk 25208a5d-f859-409c-b1a0-e04b96cab429, https://app.lexplorer.ch/suche?e_chunks=2990&e_sys=ile) und «Steuerliche Auslegung von Zuteilungs- und Vesting-Zeiten» (StRK II ZH; chunk f0831991-0328-48ef-8f39-713d186e3ea0, https://app.lexplorer.ch/suche?e_chunks=2941&e_sys=ile). Risi, FStR 2002/3, «Neuregelung …» (chunk df0c69b2-3352-4d6d-a2a1-a4662d80db50, https://app.lexplorer.ch/suche?e_chunks=30600&e_sys=ile). Das Rundschreiben ESTV vom 6.5.2003 (Vesting-Klauseln) ist laut Vorarbeit art-17a durch KS 37 aufgehoben. Eine ILE-Besprechung dazu fand sich nicht.

---

## 3. B. Verwaltungspraxis

### 3.1 ESTV KS 37 vom 30.10.2020, Ziff. 7 (lokal ganz gelesen, S. 11–18)
Lexplorer doc 03addb87-fb11-42d6-8443-7fdb1b08ceaf, https://mcp-tax.lexplorer.ch/s/doc/03addb87-fb11-42d6-8443-7fdb1b08ceaf (Kennung aus Vorarbeit art-17c). Text aus `art-17b/01_Recherche/quellen/KS37_ESTV_2020.txt`.

- **Ziff. 7.1, S. 11 (Anwendungsbereich):** «Die anteilsmässige Besteuerung, welche in den Artikeln 17d DBG sowie 7 und 8 MBV festgehalten wird, ist auf zwei Sachverhalte anwendbar. […] Bei diesen Mitarbeiterbeteiligungen handelt es sich in der Regel um Mitarbeiteroptionen, Anwartschaften auf Mitarbeiteraktien oder um unechte Mitarbeiterbeteiligungen.»
- **Ziff. 7.1, S. 11 f. (Referenzperiode, DBA):** «Die Besteuerung ist vielmehr aufgrund der Arbeitstage auf die Länder zu verteilen, in denen der Mitarbeitende seit der Zuteilung der Mitarbeiterbeteiligung bis zum Entstehen des Ausübungsrechts ansässig war (Art. 7 und 8 MBV). Keine Rolle spielt dabei, ob ein anderes Land den geldwerten Vorteil anteilsmässig besteuert oder nicht. Vielmehr ist entscheidend, welches Land das anteilige Besteuerungsrecht für das Einkommen aus der zugrundeliegenden Erwerbstätigkeit besitzt.»
- **Ziff. 7.1 (Mehrfachwechsel, Art. 9 MBV):** «… wenn ein Mitarbeitender aus dem Ausland in die Schweiz zuzieht, für kurze Zeit hier ansässig ist und noch vor dem Vesting wieder wegzieht oder umgekehrt.» Örtliche Zuständigkeit nach Art. 107 und 105 DBG; die Quellensteuer wird «jeweils bloss auf dem schweizerischen Anteil» abgerechnet.
- **Ziff. 7.1, S. 12 (Zählweise):** «Als Arbeitstage im Sinne von Artikel 7 und 8 MBV gilt der Zeitraum, in welchem zwischen einem Mitarbeitenden und seinem Arbeitgeber ein Arbeitsvertragsverhältnis besteht. Die in diese Zeitspanne fallenden Ferien, Wochenenden, gesetzlichen Feiertage und sonstigen Abwesenheiten (Reisetage, Krankheit, Militärdienst, Mutterschaftsurlaub etc.) werden dabei nicht in Abzug gebracht.» Vorbehalt der DBA, «so etwa Art. 15a DBA Deutschland über die Besteuerung von Grenzgängern».
- **Ziff. 7.2.1, S. 12 (Aktien, Bonus):** «Eine anteilsmässige Besteuerung ist ausgeschlossen, da Mitarbeiteraktien mit ihrer Abgabe erworben werden. Vorbehalten bleiben Fälle, in welchen die Mitarbeiteraktien als Entschädigung für eine im Ausland erbrachte Arbeitsleistung (Bonus) abgegeben werden.» Tabelle Ziff. 7.2.2, S. 13: «anteilsmässige Besteuerung von Mitarbeiterbeteiligungen, die als Bonus abgegeben werden (sinngemäss Art. 17d DBG)».
- **Ziff. 7.3.2.1, S. 14 (Import mit Ansässigkeitswechsel):** «… wird – unter Progressionsvorbehalt – nur anteilsmässig besteuert, sofern zwischen dem Zeitpunkt der Abgabe und der Realisation der Mitarbeiterbeteiligung ein Ansässigkeitswechsel erfolgt ist. Der in der Schweiz steuerbare geldwerte Vorteil berechnet sich dabei wie folgt (Art. 17d DBG): Gesamthaft erhaltener geldwerter Vorteil x Anzahl Arbeitstage in der Schweiz innerhalb der Vestingperiode / Anzahl Tage der Vestingperiode». Veranlagung im ordentlichen oder im Quellensteuerverfahren; Verweis auf die Fallbeispiele 1 und 3 in Anhang II.
- **Ziff. 7.3.2.2, S. 14 f. (Import ohne Ansässigkeitswechsel):** anteilsmässig «nach dem Verhältnis der Arbeitsverträge (Arbeitstage) Schweiz / Ausland innerhalb der Vestingperiode (sinngemässe Anwendung von Art. 17d DBG)». «Die Arbeitstage Schweiz sind um allfällige Drittstaattage zu kürzen.» Quellensteuerverfahren; Vorbehalt Art. 15a DBA-D.
- **Ziff. 7.3.3, S. 15 (Export):** Bei Mitarbeiterbeteiligungen, die schon bei der Abgabe besteuert wurden, ist der Export «steuerlich unbeachtlich. Vorbehalten bleiben diejenigen Fälle, in welchen die Mitarbeiterbeteiligungen als Bonus für die in der Schweiz erbrachte Leistung ausgerichtet werden». «Die Besteuerung hat in jedem Fall über das Quellensteuerverfahren zu erfolgen».
- **Ziff. 7.3.3.1, S. 15 (Export mit Ansässigkeitswechsel, Art. 97a):** «Die Steuer (Anteil direkte Bundessteuer) beträgt 11,5 Prozent des in der Schweiz steuerbaren geldwerten Vorteils (Art. 97a Abs. 2 DBG). Die anfallenden Steuern sind als Quellensteuer – diese wird auch als erweiterte Quellensteuer bezeichnet – durch den (ehemaligen) schweizerischen Arbeitgeber abzuführen. Diese Verpflichtung gilt insbesondere auch dann, wenn der geldwerte Vorteil von einer ausländischen Konzerngesellschaft ausgerichtet wird.» Ausnahme: Bei fortbestehender Anstellung beim gleichen Leistungsschuldner oder Tätigkeit als VR gelten Art. 91, 97 und 93 DBG; «Eine Ausscheidung gemäss Artikel 17d DBG hat dabei zu unterbleiben (vgl. Art. 13 Abs. 1 und Art. 14 Abs. 1 MBV).»
- **Ziff. 7.3.3.2, S. 15 f. (Export ohne Ansässigkeitswechsel):** Bei unverändertem Arbeitsverhältnis in der Schweiz sind «einzig allfällige Drittstaattage (d.h. Arbeitstage ausserhalb der Schweiz) von der Besteuerung auszuscheiden». Bei einem Arbeitgeberwechsel ins Ausland innerhalb der Vestingperiode wird anteilsmässig besteuert, auch für Art. 93 DBG («Tage des Verwaltungsratsmandats»). Verweis auf Fallbeispiel 5 in Anhang II.
- **Ziff. 7.3.4, S. 16–18 (Tabelle):** Wohnsitz Schweiz (Art. 83): «Eine anteilsmässige Besteuerung (Art. 17d DBG) kann nur dann erfolgen, wenn die steuerpflichtige Person nicht während der ganzen Zeitspanne für ihr Einkommen in der Schweiz steuerpflichtig war.» Wohnsitz Ausland, Art. 91/97: «Die Besteuerung erfolgt nach Art. 84 DBG, wobei eine anteilsmässige Besteuerung gemäss Art. 17d DBG ausgeschlossen ist (vgl. Art. 13 Abs. 1 MBV).» Art. 93: «… wobei eine anteilsmässige Besteuerung gemäss Art. 17d DBG (Art. 14 Abs. 1 MBV) ausgeschlossen ist.» Fn. 3: «Im Falle eines Wegzugs aus der Schweiz ist somit eine Besteuerung durch die Schweiz dennoch nicht ausgeschlossen.»
- **Einordnung:** (1) Wortlautspannung zum Gesetz: Art. 17d DBG knüpft an «steuerrechtlichen Wohnsitz oder Aufenthalt» an, KS 37 und Art. 7/8 MBV an «Arbeitstage» mit Arbeitsvertragsverhältnis. (2) Die Ausdehnung auf Anwartschaften, unechte Beteiligungen und Aktien als Bonus beruht auf MBV und KS. (3) Fälle ohne Ansässigkeitswechsel löst das KS in «sinngemässer Anwendung» von Art. 17d. Eine gesetzliche Grundlage dafür nennt das KS nicht. Neutral darzustellen.

### 3.2 KS 37 Anhang II «Fallbeispiele» (Stand 22.7.2013)
doc ccf1675a-1432-4f0e-ae05-2d94dc4a8624, https://mcp-tax.lexplorer.ch/s/doc/ccf1675a-1432-4f0e-ae05-2d94dc4a8624. **Heute nicht lesbar (Lesesperre).** Aus der Vorarbeit (art-17b Verwaltungspraxis 2.2 und art-17c 3.2, dort ganz gelesen) ist verfügbar:
- **Fallbeispiel 1 a), S. 1:** «Die Mitarbeiteroptionen werden im Zeitpunkt ihrer Ausübung besteuert, weil sie weder frei verfügbar noch börsenkotiert sind.» (Rechtserwerb nach fünfjähriger Sperrfrist, Ausübung im siebten Jahr.)
- **Fallbeispiel 1 b), S. 1:** «X hat die Mitarbeiteroptionen während den ersten fünf Jahren verdient. Weil X während dieser Zeitdauer nur drei Jahre in der Schweiz gearbeitet hat, besteuert die Schweiz den geldwerten Vorteil gemäss Artikel 17d DBG nur anteilsmässig im Umfang von 3/5».
- **Fallbeispiel 3, S. 3:** «Zu beachten ist, dass die Arbeitgeberin in Ziffer 5 des Lohnausweises den gesamten geldwerten Vorteil von 90'000 Franken einfliessen lassen muss.»
- Nach KS 37 Ziff. 7.3.2.1 betreffen die Fallbeispiele 1 und 3 den Import mit Ansässigkeitswechsel, nach Ziff. 7.3.3.2 das Fallbeispiel 5 den Export ohne Ansässigkeitswechsel (Arbeitgeberwechsel ins Ausland).
- Gesamtbefund der Vorarbeit: Die Fallbeispiele 1–7 betreffen nur Mitarbeiteroptionen (Art. 17d, 97a DBG: Import, Export, Reimport). Sie enthalten kein Beispiel zu unechten Beteiligungen oder RSU.
- **Offen:** Die Fallbeispiele 2, 4, 6 und 7 (Sachverhalt, Lösung, Seite, Kernsatz) und die Seitenzahl von Fallbeispiel 5 wurden in der Vorarbeit nicht wörtlich festgehalten. Nach 00:00 UTC mit get_document_slice (1 Slice, ca. 16 000 Byte; slice_size 20000) nachholen.

### 3.3 KS 37 Anhang IV «Fallbeispiele zur Quellenbesteuerung» (Stand 22.7.2013)
doc a0f3aafe-2be8-4ed7-9e05-c8ce3c325bad, https://mcp-tax.lexplorer.ch/s/doc/a0f3aafe-2be8-4ed7-9e05-c8ce3c325bad. Heute nicht lesbar. Aus der Vorarbeit (art-17c, dort ganz gelesen), S. 1:
- «Der internationale Ansässigkeitswechsel zwischen Abgabe und Ausübung der Mitarbeiterbeteiligung löst die Besteuerung gemäss Artikel 97a DBG aus. […] Auf die Ermittlung des steuerbaren Einkommens hat der internationale Ansässigkeitswechsel nur insoweit Auswirkungen, als dieser innerhalb der Vestingperiode erfolgt (Art. 17d DBG).»
- Ausnahme: keine Besteuerung nach Art. 97a, «wenn innerhalb des Zeitraums zwischen Abgabe und Ausübung der Mitarbeiterbeteiligung unverändert das Vertragsverhältnis zum Leistungsschuldner mit Sitz in der Schweiz weiterbesteht.»
- Einordnung: Ein Wechsel nach dem Vesting und vor der Ausübung löst die Quellensteuer nach Art. 97a aus, ändert aber den Schweizer Anteil nicht. **Offen:** die einzelnen Fallgruppen (Art. 91, 93, 97) mit Seitenzahl.

### 3.4 Zürich: ZStB Nr. 100.1, Merkblatt über die Quellenbesteuerung von geldwerten Vorteilen aus exportierten Mitarbeiterbeteiligungen gemäss § 100 StG vom 15.12.2020 (gültig ab 1.1.2021)
Chunk 85de6577-e02a-4806-bc7d-762a193ac1bf (Zürcher Steuerbuch, doc cb70f7eb-5a94-4b36-aeba-10652145b7cc), https://mcp-tax.lexplorer.ch/s/doc/cb70f7eb-5a94-4b36-aeba-10652145b7cc?chunk=85de6577-e02a-4806-bc7d-762a193ac1bf. [Vorarbeit art-17c 5.2, dort ganz gelesen; heute nicht neu gelesen]
- Lit. A: «Der Quellensteuer gemäss § 100 des Steuergesetzes (StG; LS 631.1) unterliegen Personen, die gesperrte oder nicht börsenkotierte Mitarbeiteroptionen, Anwartschaften auf Mitarbeiteraktien oder unechte Mitarbeiterbeteiligungen (Phantom-Aktien/-Optionen, SAR usw.) während der Zeit zugeteilt erhielten oder teilweise verdienten, in der sie in der Schweiz ansässig waren, und die diese Mitarbeiterbeteiligungen erst nach dem Wegzug ins Ausland realisieren.» Ausnahme bei fortbestehender Anstellung beim Leistungsschuldner (§§ 94, 96 StG).
- Lit. B: «Steuerbar ist der gesamte geldwerte Vorteil.» Anteilsmässig «im Verhältnis der der in der Schweiz verbrachten Zeitspanne zur gesamten Vestingperiode, besteuert (§ 17d StG)».
- Lit. C: «Die Quellensteuer beträgt total 31,5 % des geldwerten Vorteils.»
- Lit. D: Fälligkeit «im Zeitpunkt der Realisierung»; die Bescheinigung nach Art. 8 MBV ist beizulegen.
- Ergänzend ZStB Nr. 17a.1 (Merkblatt vom 6.1.2025), lit. B.I.7.2 (Import von Anwartschaften), chunk b83b037a-d2d4-4e3d-aba7-6615bad4cfb8, https://mcp-tax.lexplorer.ch/s/doc/cb70f7eb-5a94-4b36-aeba-10652145b7cc?chunk=b83b037a-d2d4-4e3d-aba7-6615bad4cfb8 [Vorarbeit art-17c 5.1]: «Sind die importierten Anwartschaften mit subjektiven Bedingungen behaftet, wonach die Mitarbeitenden die Anwartschaft erst verdienen bzw. abverdienen müssen, wird nur derjenige Anteil des erzielten geldwerten Vorteils – unter Progressionsvorbehalt – als Erwerbseinkommen besteuert, welcher auf die Arbeitstätigkeit in der Schweiz zurückzuführen ist bzw. in der Schweiz verdient wurde (§ 17d StG und Art. 17d DBG).» Formel nach Arbeitstagen.
- Einordnung: Lit. B übernimmt im Kernsatz den Gesetzeswortlaut («in der Schweiz verbrachten Zeitspanne»). Lit. A und B.I.7.2 dehnen die Regel auf Anwartschaften und unechte Beteiligungen aus; B.I.7.2 rechnet nach Arbeitstagen.

### 3.5 Waadt: ACI VD, Directive 21565 (Stand 01.2026)
doc 632fe8c1-8114-49c2-9b7e-81bdb36c677b, https://mcp-tax.lexplorer.ch/s/doc/632fe8c1-8114-49c2-9b7e-81bdb36c677b. [Vorarbeit art-17c 5.10, dort ganz gelesen; heute nicht neu gelesen]
- Titel: «Directive concernant l'imposition à la source des avantages appréciables en argent provenant de participations de collaborateur « gagnées » en Suisse, mais réalisées lorsque le bénéficiaire n'est ni domicilié ni en séjour en Suisse».
- Ch. I: erfasst «options de collaborateur bloquées ou non cotées en bourse», «expectatives sur des actions de collaborateur (restricted stock units (RSUs), etc.)» sowie «phantom stocks, - stock appreciation rights (SARs), etc.»
- Ch. IV: Aufteilung nach Arbeitstagen in der Vestingperiode; «Lorsqu'il n'y a pas de période de vesting, il faut considérer que les dates d'octroi et de vesting se confondent.»
- Ch. V: Barème nach «articles 97a, al. 2 LIFD et 144a, al. 2 LI»; «impôt fédéral direct : 11.5 %», «impôt cantonal et communal : 20 %», insgesamt «31.5% de la prestation brute».
- **Offen:** die wörtliche Formel und die Bestimmungen zu den Arbeitstagen aus Ch. IV, sobald die Lesesperre aufgehoben ist.

### 3.6 Genf: Information fiscale 2/2016 vom 1.7.2016
doc 6faa02c2-6c22-447f-a872-57b673d84e99, https://mcp-tax.lexplorer.ch/s/doc/6faa02c2-6c22-447f-a872-57b673d84e99. [Vorarbeit art-17c 5.9, dort ganz gelesen]
- Ziff. 2.1: Bescheinigung «lors de la réalisation du revenu provenant de participations de collaborateur (options/expectatives sur actions ou sur espèces), y compris en cas de départ du collaborateur à l'étranger» und «chaque année, tant que le collaborateur est titulaire de participations de collaborateur au 31 décembre».
- Einordnung: Das Dokument regelt nur Bescheinigungen; die Wegzugsfälle werden einbezogen. Zur Berechnung des Anteils ist in der Vorarbeit nichts festgehalten.

### 3.7 St. Gallen: StB 30 Nr. 2 (Stand 1.1.2025)
doc 563bc34e-b2c3-4dd4-b945-5bc6585fa5cf, https://mcp-tax.lexplorer.ch/s/doc/563bc34e-b2c3-4dd4-b945-5bc6585fa5cf. In der Vorarbeit wurde nur Slice 0 (S. 1–3) gelesen. Dort steht nichts zu Zuzug, Wegzug oder anteilsmässiger Besteuerung. **Offen:** die übrigen Slices lesen und Ziffer und Kernsatz zu Art. 30quater StG SG (Parallele zu Art. 17d) und zur Quellensteuer festhalten.

### 3.8 Basel-Landschaft: Steuerbuch BL Bd. 1, 24 Nr. 4
doc 6ea8e8d3-1db4-4673-af94-f10aba05a432, https://mcp-tax.lexplorer.ch/s/doc/6ea8e8d3-1db4-4673-af94-f10aba05a432. [Vorarbeit art-17c 5.7, dort ganz gelesen, aber Ziff. 4 nur sinngemäss festgehalten]
- Ziff. 4 (international): Die anteilsmässige Besteuerung ist nur für «gesperrten (oder nicht börsenkotierten) Mitarbeiteroptionen» formuliert. Die Quellensteuer gilt für Personen ohne Wohnsitz im Zuflusszeitpunkt allgemein. **Offen:** der wörtliche Kernsatz.

### 3.9 Weitere Kantone (Vorarbeit art-17c)
- SZ: Merkblatt vom 18.11.2025, N 30–32, doc 8755573e-cb4d-49c8-b826-ce3f5ba2b760, https://mcp-tax.lexplorer.ch/s/doc/8755573e-cb4d-49c8-b826-ce3f5ba2b760. Anteilsmässige Besteuerung nur für «gesperrte Mitarbeiteroption[en]» formuliert.
- TG: StP 120a Nr. 1, doc 98f00095-17df-41b8-a9f1-c16ebc23df31, https://mcp-tax.lexplorer.ch/s/doc/98f00095-17df-41b8-a9f1-c16ebc23df31: «Die Steuer beträgt 24.5% des geldwerten Vorteils, der Staats- und Gemeindesteueranteil beträgt dabei 13%»; formuliert für «gesperrten Mitarbeiteroptionen (§ 19 Abs. 3 StG)».
- ZG: nur Verweis auf KS 37 (doc 399c5404-d2ba-405d-8f44-c00a51403f2f). BE: TaxInfo ohne Aussage zu Art. 17d (chunk 21316eec-9113-4c97-a6e8-241a03bca668). BS: nur § 18b StG, keine Praxis (Vorarbeit art-17b). Wegen der Lesesperre war heute kein nav_find möglich.

---

## 4. Leseliste für die Fortsetzung (nach 00:00 UTC; nur Lese- und Navigationswerkzeuge, keine Suche nötig)

1. get_document_slice ccf1675a-1432-4f0e-ae05-2d94dc4a8624 (Anhang II, Fallbeispiele 1–7 mit Seite und Kernsatz).
2. get_document_slice a0f3aafe-2be8-4ed7-9e05-c8ce3c325bad (Anhang IV, Fallgruppen).
3. get_chunk_content b6732f35-3b4d-49b6-a483-72767fe5b2dc (FStR 2025, Arbeitgeber, Exemple 2 Wegzug) und die benachbarten Chunks über nav_list_chunks 65957644-….
4. get_chunk_content ccf5bcc2-… und f60abd82-… (Stocker/Brozzo 2024), dazu Varianten 1–4 über nav_list_chunks fb5c4aa5-….
5. get_chunk_content bd1da586-…, 497fd81d-… (Allemann/Bloch-Riemer, Schuldner) und c637de6e-… (erneut lesen).
6. get_chunk_content 56ca079c-… (Peyer/Schreiber/Walt), d4d4fb91-… (Oesterhelt/Truffer) und 27617312-… (Oesterhelt/Gammeter 11.6) zur Verifikation.
7. get_chunk_content e3f99ab9-… (Inhaltsverzeichnis Rechtsprechung 2025-2), dazu die Inhaltsverzeichnisse von Rechtsprechung 2025/4 (doc f1ed9b62-…) und 2023/1 (doc 82247d36-…), um eine Besprechung von 9C_13/2025 zu finden.
8. get_chunk_content 100490ab-… und f1a5b791-… (Risi/Schmid 2005 Ziff. 6.4), 8a126594-… (OECD 2002), db34664a-… (Niederbacher-Puchegger/Risi 2005).
9. get_chunk_content 4585df42-…, 25208a5d-…, f0831991-… (FStR 2002/3, altes Recht; nur soweit für die Entstehungsgeschichte nötig).
10. Kantone: VD 632fe8c1-… Ch. IV wörtlich; SG 563bc34e-… Slices 1 ff.; BL 6ea8e8d3-… Ziff. 4 wörtlich; nav_find für BS, ZG und BE «Mitarbeiter».

## 5. Literaturverzeichnis (nur verwendbare, in der Vorarbeit ganz gelesene ILE-Texte)

- Allemann Patrick/Bloch-Riemer Ruth, Arbeitgeber in der Haftung – Quellensteuern und Sozialversicherungen im internationalen Verhältnis, Internationales Steuerseminar 2021, St. Gallen 2021 [https://app.lexplorer.ch/suche?e_chunks=58607&e_sys=ile]
- Oesterhelt Stefan/Gammeter Thomas, Das Formelwertprinzip bei Mitarbeiteraktien – Darstellung anhand der Praxis im Kanton Zürich, FStR 2024 [https://app.lexplorer.ch/suche?e_id=592&e_sys=ile]
- Oesterhelt Stefan/Truffer Ildiko, Mitarbeiterbeteiligung, St.Galler Seminar zur Einkommenssteuer 2020, St. Gallen 2020 [https://app.lexplorer.ch/suche?e_id=1623&e_sys=ile]
- Peyer Basil/Schreiber Susanne/Walt Martina, Aktuelles aus Verständigungsverfahren Deutschland, Österreich, Liechtenstein und Schweiz, Internationales Steuerseminar 2024, St. Gallen 2024 [https://app.lexplorer.ch/suche?e_chunks=50258&e_sys=ile]
- (historisch, Vorarbeit) Risi Andreas, Besteuerung von Mitarbeiterbeteiligungen – der Bericht der gemischten Arbeitsgruppe, FStR 2002 [https://app.lexplorer.ch/suche?e_id=110&e_sys=ile]

Materialien: Botschaft zum Bundesgesetz über die Besteuerung von Mitarbeiterbeteiligungen vom 17.11.2004, BBl 2005 575 (S. 576, 596–598).
