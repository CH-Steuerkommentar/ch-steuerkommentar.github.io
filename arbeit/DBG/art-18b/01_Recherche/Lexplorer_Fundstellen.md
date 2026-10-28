# Lexplorer-Fundstellen zu Art. 18b DBG

Stand: 28.10.2026. Quelle: Lexplorer Tax (mcp-tax.lexplorer.ch). Wörtliche Zitate sind aus dem gelesenen Text kopiert. Lexplorer wurde nicht für Rechtsprechung verwendet.

> Hinweis (28.10.2026): Diese Datei bestand beim Schreiben bereits (von einem parallelen Hilfsagenten angelegt) und wurde durch diesen Abschnitt ersetzt. Der frühere Inhalt ist nicht mehr vorhanden. Die Lexplorer-Treffer der ILE-Literatur stehen mit Abfragen und Chunk-IDs in `ILE_Literatur.md` und sind hier nachzutragen.

## Verwaltungspraxis

**Suchzähler Lexplorer (search_chunks_*): 6 von höchstens 6.** Navigation (nav_find, nav_list_sources, nav_list_documents) und Lesen (get_document_slice, get_chunk_content) sind nicht mitgezählt.

### Suchprotokoll

| Nr. | Werkzeug | Kanton / Filter | Abfrage | Ergebnis |
|---|---|---|---|---|
| 1 | search_chunks_keyword, limit 10 | ZH, Kategorie 02-verwaltungspraxis | «Teilbesteuerung Geschäftsvermögen» | 0 Treffer |
| 2 | search_chunks_hybrid, limit 10 | ZH | «Teilbesteuerung Einkünfte aus Beteiligungen im Geschäftsvermögen 50 Prozent Spartenrechnung § 18b StG» | PI 173/2025 (Chunks § 18b und § 20); sonst StG § 18 und StRG-Entscheide (nicht ausgewertet, Rechtsprechung ausgeschlossen); kein Steuerbuch-Treffer |
| 3 | search_chunks_hybrid, limit 8 | SG, Kategorie 02-verwaltungspraxis | «Teilbesteuerung qualifizierte Beteiligungen Geschäftsvermögen Spartenrechnung Veräusserungsgewinn Haltedauer» | nichts Einschlägiges (StB 139 Nr. 1, StB 031 Nr. 2/3, StB 234 Nr. 1 usw.) |
| 4 | search_chunks_keyword, limit 8 | AG | «Teilbesteuerung Beteiligungen Geschäftsvermögen» | 0 Treffer |
| 5 | search_chunks_keyword, limit 8 | BS | «Teilbesteuerung Beteiligungen Geschäftsvermögen» | § 19b StG BS (Chunk 7d2fb6dd…); Wegleitung 2026 (Formularbeispiele, nicht einschlägig) |
| 6 | search_chunks_hybrid, limit 8 | CH, Quelle SSK-Kreisschreiben (dd71a4af-2915-4cd8-ba66-291f69a7e6a8) | «Teilbesteuerung Beteiligungen Geschäftsvermögen interkantonale Steuerausscheidung qualifizierte Beteiligung» | SSK-KS 32 (drei Chunks); SSK-KS 23 und 34 (nicht einschlägig) |

**Navigierend (ohne Suche):** nav_find «Teilbesteuerung» (ZH, CH), «Teilbesteuer» (BE, LU, SG, AG, BL, BS), «18b» (ZH), «ZStB 18» (ZH), «Beteiligung» (ZH, SG, AG, BS, CH), «Geschäftsvermögen» (SG), «StB 032», «StB 033» (SG); nav_list_sources AG und BS (02-verwaltungspraxis); nav_list_documents AG-Quelle f653e769-dd49-4c8f-954d-41f91d1d3303.

### Treffer

**L1. ESTV-KS Nr. 23a (CH)**
- Werkzeug: nav_find «Teilbesteuerung» (CH) → get_document_slice
- Kennung: dc4ca501-c9e7-43ed-b86b-d2fe09d36c95; Status «in Kraft seit 01.01.2020»
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/dc4ca501-c9e7-43ed-b86b-d2fe09d36c95
- Inhalt in Open Case Law (get_practice) vollständig gelesen; Auswertung in Verwaltungspraxis.md A1.

**L2. ESTV-KS Nr. 23 (CH)**
- Werkzeug: nav_find «Teilbesteuerung» (CH) → get_document_slice
- Kennung: 6bc9d39e-50cc-4d95-99ef-fc766736af6b; Status «in Kraft für Steuerperioden 2009 bis 2019»
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/6bc9d39e-50cc-4d95-99ef-fc766736af6b
- Auswertung Verwaltungspraxis.md A2. (Weitere Treffer derselben nav_find-Abfrage: KS 22a, 4fb7ee28-726c-4b2f-9de7-cc167f148a7d; KS 22, 215e442e-8223-4f1e-9c46-7b2a3d2bcb4f.)

**L3. SSK-Kreisschreiben 32 vom 1.7.2009 (CH)**
- Werkzeug: Suche 6 → get_document_slice (Slice 0, 20 000 Zeichen = S. 1–6)
- Kennung: 081ca9a6-a7b3-4192-b4c3-8904ba6ed815 (Chunk zu Art. 18b: 0c57fcf3-2ba4-4697-9208-4721ef49c1c6)
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/081ca9a6-a7b3-4192-b4c3-8904ba6ed815
- Tragender Satz (Ziff. 1.5.1, S. 2): «Den Kantonen dürfte es im Übrigen grundsätzlich freigestellt sein, ob sie – bei Beteiligungen im Geschäftsvermögen – die analoge Regelung von Art. 18b DBG übernehmen oder ob sie die Einkünfte aus qualifizierten Beteiligungen (einschliesslich Gewinne aus der Veräusserung solcher Beteiligungsrechte) ohne Anrechnung von damit zusammenhängenden Aufwendungen mildern wollen.» Ziff. 3.4.1 (S. 5 f.): Aufrechnung der Bemessungsreduktion der «Sparte Beteiligungen» im ersten Schritt, Korrektur im Zuweisungskanton im zweiten Schritt.

**L4. BE TaxInfo «Teilbesteuerungsverfahren» (BE)**
- Werkzeug: nav_find «Teilbesteuer» (BE) → get_document_slice
- Kennung: 64805312-323c-455b-ad70-97c562133237; Status «in Kraft»; Fassung vom 6.8.2026; Original https://www.taxinfo.sv.fin.be.ch/taxinfo/09d79854-aeeb-4f74-ab35-86d95b7f72ac
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/64805312-323c-455b-ad70-97c562133237
- Tragender Satz (Ziff. 1.3): «Netto-Ergebnisse (Erträge abzüglich anteiliger Finanzierungs- und Verwaltungsaufwand) aus qualifizierenden Beteiligungen im Geschäftsvermögen sind in folgendem Umfang steuerbar: Kantons- und Gemeindesteuer 50 % steuerbar (Art. 21b StG) Direkte Bundessteuer 70 % steuerbar (Art. 18b DBG)». «Die reduzierte Besteuerung (Spartenrechnung) wird auf Antrag der steuerpflichtigen Person gewährt.»

**L5. Luzerner Steuerbuch Bd. 1 «Teilbesteuerung der Einkünfte aus qualifizierten Beteiligungen» (LU)**
- Werkzeug: nav_find «Teilbesteuer» (LU) → get_document_slice
- Kennung: 5018e163-510e-48e2-8ca5-37c6fa42e891; Stand 01.01.2024; Original https://steuerbuch.lu.ch/band1/einkommenssteuer/teilbesteuerung_der_einkuenfte_aus_qualifizierten_beteiligungen
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/5018e163-510e-48e2-8ca5-37c6fa42e891
- Tragender Satz: «Die Milderung der wirtschaftlichen Doppelbelastung bei Einkünften aus qualifizierten Beteiligungen erfolgt grundsätzlich analog zur direkten Bundessteuer nach dem Teilbesteuerungsverfahren auf der Bemessungsgrundlage.» Tabelle ab 2020: Staats-/Gemeindesteuern PV 60 %, GV 50 %; DBG PV 70 %, GV 70 %. «Einkünfte von Genossenschaften ohne Grundkapital und Anteilsscheine berechtigen nicht für die Teilbesteuerung (vgl. BGE 2C_812/2018 vom 20.8.2019).» (Zitat des Steuerbuchs, nicht über Lexplorer geprüft.)

**L6. Steuerbuch Basel-Landschaft Bd. 1, 24 Nr. 8 «Teilbesteuerung der Einkünfte aus qualifizierten Beteiligungen» (BL)**
- Werkzeug: nav_find «Teilbesteuer» (BL) → get_document_slice (Slices 0 und 1, vollständig)
- Kennung: 9035b91b-cbc0-49a3-b38d-ec8797a90515; Nr. 1-024-08; Stände 30.9.2011/31.12.2016/12.05.2026; Original https://kanton.baselland.ch/finanz-und-kirchendirektion/steuerverwaltung-steuerbuch/band-1/einkommen/downloads-1/band1_024_08.pdf
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/9035b91b-cbc0-49a3-b38d-ec8797a90515
- Tragende Sätze: Ziff. 2.2.3 (S. 3): «Damit eine Teilbesteuerung beansprucht werden kann, muss gesamthaft eine Beteiligungsquote von 10 % veräussert werden.» Ziff. 2.2.3 «Mindesthaltedauer und Mindestveräusserungsquote» (S. 3 f.): «Zudem müssen alle veräusserten Beteiligungen zusammen die oben (siehe Ziff. 2.2.3) skizzierte 10 % Beteiligungsquote erreichen (sog. Mindestveräusserungsquote).» «Im Rahmen von Umstrukturierungen wird die bisherige Haltedauer auf die übernehmende Gesellschaft übertragen, sofern eine steuerneutrale Umstrukturierung vorliegt.» Ziff. 2.3.2 (S. 4): direkter Beteiligungsaufwand inkl. «nicht rückforderbare ausländische Quellensteuern». Ziff. 2.3.4 (S. 5): «Der Verwaltungsaufwand wird grundsätzlich pauschal im Umfang von 5 % des Spartenergebnisses (Bruttogewinn abzüglich direkter Beteiligungsaufwand) ermittelt.» Ziff. 3 (S. 7): DBG ab 2020 70 %.
- Hinweis: Der kantonale GV-Satz ist im gelesenen Text nicht beziffert; Beispiel Ziff. 2.3.5.1 rechnet mit 60 von 100.

**L7. § 19b StG BS (Gesetz über die direkten Steuern, BS 640.100) (BS)**
- Werkzeug: Suche 5 → get_chunk_content
- Kennung: Chunk 7d2fb6dd-b5aa-4a14-882f-5e35f6ed809d (Dok. 8165032d-ede9-4f8e-816f-969bffc6e838); Status «in Kraft seit 01.01.2026»
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/8165032d-ede9-4f8e-816f-969bffc6e838?chunk=7d2fb6dd-b5aa-4a14-882f-5e35f6ed809d
- Tragender Satz: «… sind nach Abzug des zurechenbaren Aufwandes im Umfang von 80 Prozent steuerbar, wenn diese Beteiligungsrechte mindestens 10 Prozent des Grund- oder Stammkapitals einer Kapitalgesellschaft oder Genossenschaft darstellen.» (Gesetzgebung, nicht Verwaltungspraxis; ein BS-Merkblatt zur Teilbesteuerung wurde nicht gefunden.)

**L8. ZH: PI 173/2025 «Anpassung der Dividendenbesteuerung bei qualifizierten Beteiligungen» (Materialien)**
- Werkzeug: Suche 2 → get_chunk_content
- Kennung: Chunk 918b8213-7217-4742-b388-fd124fac938f (Dok. fbfdb241-79e2-4287-b15c-072ad47b3674); «Materialien, 26.05.2025»
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/fbfdb241-79e2-4287-b15c-072ad47b3674?chunk=918b8213-7217-4742-b388-fd124fac938f
- Tragender Satz (Synopse § 18b StG ZH): «… sind nach Abzug des zurechenbaren Aufwands im Umfang von 50 70 Prozent steuerbar …» (geltend 50, beantragt 70).

**L9. ZH: Kantonsrat, Teilprotokoll 30.6.2025, KR-Nr. 173/2025 (Materialien)**
- Werkzeug: nav_find «Beteiligung» (ZH) → get_document_slice (Slices 0 und 7)
- Kennung: 60774792-acee-4178-ba34-737342da8604
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/60774792-acee-4178-ba34-737342da8604
- Tragende Sätze: «Wer mehr als 10 Prozent einer Firma besitzt, … versteuert nur die Hälfte dieser Einnahmen» (Votum Berger, S. 1). «Für die vorläufige Unterstützung der parlamentarischen Initiative KR-Nr. 173/2025 stimmen 58 Ratsmitglieder. Damit ist das Quorum von 60 Stimmen nicht erreicht. Die Initiative ist abgelehnt.» (S. 8)

**L10. ZH: Antwort RR 233/2025 vom 29.10.2025 (Materialien)**
- Werkzeug: nav_find «Teilbesteuerung» (ZH) → get_document_slice
- Kennung: b64643d1-047a-477f-b029-56d9aa5527ee
- lexplorer_url: https://mcp-tax.lexplorer.ch/s/doc/b64643d1-047a-477f-b029-56d9aa5527ee
- Tragende Angaben (S. 2): Bruttoerträge aus qualifizierten Beteiligungen, Steuerperiode 2020 «Total 9 450 1 878 048 423», 2021 «Total 10 500 2 433 991 768», 2022 «Total 11 094 2 728 623 774»; «Für die Steuerperioden 2023 und 2024 sind noch keine aussagekräftigen Zahlen verfügbar.»

### Ohne Treffer
- **ZH Steuerbuch (ZStB):** kein Eintrag zur Teilbesteuerung im Geschäftsvermögen (nav_find und Suchen 1–2). Gefundene ZStB-Titel mit «Beteiligung»: ZStB 17a.1 (Mitarbeiterbeteiligungen), ZStB 20.3 (persönliche Holdinggesellschaften), ZStB 72.2 (Merkblatt Beteiligungen, juristische Personen); nicht einschlägig.
- **SG Steuerbuch:** kein Eintrag (nav_find, Suche 3).
- **AG Merkblätter & Richtlinien:** kein Eintrag (nav_list_documents mit 31+ Dokumenten, Suche 4).
- **BS Steuerbuch:** nur Merkblatt «Beteiligungsgesellschaften / Beteiligungsabzug» (2b145211-bb1f-40eb-9860-e2b16de4a32c), nicht einschlägig.

## ILE-Literatur (wiederhergestellt aus ILE_Literatur.md, 28.10.2026)

Der ursprüngliche Abschnitt des ILE-Agenten wurde beim parallelen Schreiben überschrieben. Die vollständigen Angaben (Abfrage Nr., Werkzeug, Kanton CH, Kategorie 08-institut-fuer-law-und-economics, Chunk-ID, Autor:innen, Ziffer, tragender Satz, lexplorer_url) stehen in ILE_Literatur.md. Verwendet in der Kommentierung:
- Baumgartner/Stocker/Zigerlig, FStR 2006, Gesetzgebungs-Agenda 2006/3 und 2006/4, Ziff. 1.1 – Chunks eea90476-8da9-4887-a6a5-a9856f2449d4, 88f04e68-1da9-4a0f-a2ca-a72ea63aaa0d – https://app.lexplorer.ch/suche?e_chunks=9164&e_sys=ile; …e_chunks=9366…
- Baumgartner/Stocker/Zigerlig, FStR 2007, Gesetzgebungs-Agenda 2007/2, Ziff. 1.1 – Chunk 48832223-5c3d-4f68-90d5-2d4a84630d80 – https://app.lexplorer.ch/suche?e_chunks=30716&e_sys=ile
- Bucher, Schriftenreihe Finanzwissenschaft und Finanzrecht Bd. 123, N 805 – Chunk a5002afb-c4f1-40de-b949-38e255abb536 – https://app.lexplorer.ch/suche?e_chunks=23457&e_sys=ile
- Fenners/Schreiber, ILE-Seminar 2024 – Chunk ad613f0f-44bd-452f-81fc-2e3ea1a0b2c4 – https://app.lexplorer.ch/suche?e_chunks=51228&e_sys=ile
- Kocher/Stadelmann, FStR 2016, Ziff. 2.2.4.7 – https://app.lexplorer.ch/suche?e_chunks=4186&e_sys=ile
- Locher, FStR 2020, Ziff. 4.3.3 – https://app.lexplorer.ch/suche?e_chunks=6987&e_sys=ile
Suchen gesamt: ILE 14 + Verwaltungspraxis 6 = 20 (Budget 25).
