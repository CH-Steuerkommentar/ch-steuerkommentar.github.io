# Lexplorer-Fundstellen zu Art. 17c DBG

Stand: 28.10.2026. Quelle: Lexplorer Tax (Praxis: mcp-tax.lexplorer.ch; ILE: app.lexplorer.ch). Lexplorer nicht für Rechtsprechung verwendet. Budget dieses Auftrags: höchstens 12 Suchen (search_chunks_*, find_leading_cases); Lesen und Navigieren (get_chunk_content, get_document_slice, nav_*) zählt nicht.

## Suchprotokoll

| Nr. | Werkzeug | Abfrage | Kanton / Kategorie | Treffer |
|---|---|---|---|---|
| 1 | search_chunks_hybrid (limit 10) | «Phantom Stocks Stock Appreciation Rights unechte Mitarbeiterbeteiligung Besteuerung im Zeitpunkt des Zuflusses Auszahlung Art. 17c DBG Zuflussprinzip Forderungserwerb» | CH / 08-institut-fuer-law-und-economics | 10 |
| 2 | search_chunks_hybrid (limit 10) | «Co-Investment Management-Beteiligung Private Equity Sweet Equity Exit unechte Mitarbeiterbeteiligung Erwerbseinkommen statt steuerfreier Kapitalgewinn umfassende Eigentümerrechte» | CH / 08-ile | 10 |
| 3 | search_chunks_hybrid (limit 10) | «Wahlrecht Abgeltung in bar oder in Aktien cash settled Restricted Stock Units Barausgleich Qualifikation echte oder unechte Mitarbeiterbeteiligung Anwartschaft Bargeldabfindung» | CH / 08-ile | 10 |
| 4 | search_chunks_hybrid (limit 8) | «Dividendenäquivalente Dividend Equivalents Zahlungen auf Phantom Stocks oder RSU während Vestingperiode Lohn oder Vermögensertrag Besteuerung» | CH / 08-ile | 8 (keiner einschlägig) |
| 5 | search_chunks_hybrid (limit 8) | «Rückzahlung Bonus Clawback Malus Verfall Mitarbeiterbeteiligung bereits besteuertes Erwerbseinkommen Gewinnungskosten negatives Einkommen Rückforderung Lohn» | CH / 08-ile | 8 (keiner zu unechten) |
| 6 | search_chunks_hybrid (limit 10) | «unechte Mitarbeiterbeteiligungen Phantom Stocks Wegzug ins Ausland Quellensteuer Art. 97a DBG nur gesperrte Mitarbeiteroptionen keine gesetzliche Grundlage anteilsmässige Besteuerung Art. 17d» | CH / 08-ile | 10 |
| 7 | search_chunks_hybrid (limit 8) | «Rentensatz Art. 37 DBG Kapitalabfindung für wiederkehrende Leistungen mehrjährige Mitarbeiterbeteiligung Phantom Auszahlung Progression Satzbestimmung» | CH / 08-ile | 8 (keiner einschlägig; 2 Lehrbuch-Treffer übergangen) |
| 8 | search_chunks_keyword (limit 10) | «Phantom» | CH / 08-ile | 10 |
| 9 | search_chunks_hybrid (limit 10) | «Zufluss von Einkommen fester Rechtsanspruch Erwerb einer Forderung oder Auszahlung aufgeschobener Bonus deferred compensation Vestingbedingung Besteuerungszeitpunkt Lohn» | CH / 08-ile | 10 (1 Lehrbuch-Treffer übergangen) |

Für die Verwaltungspraxis (Block P) wurde **keine** Suche verwendet; alles navigierend (nav_find, nav_list_chunks, get_document_slice, get_chunk_content). Verwendete nav_find-Muster: «exportierten Mitarbeiterbeteiligungen» (ZH, 0 Treffer), «collaborateur» (GE: 2; VD: 0), «Mitarbeiter» (ZG: 0; BL: 1), «Mitarbeiterbeteiligungen» (TG: 3).

Treffer aus «ILE-HSG — Lehrbuch Steuerrecht» (source_slug ile-lehrbuch-steuerrecht): in Suche 7 (chunks 23735cab-…, c92ac7cf-…) und Suche 9 (chunk 93e557cd-…) – nicht gelesen, nicht verwendet.

---

## P. Verwaltungspraxis (navigierend erreicht)

lexplorer_url wie vom Werkzeug ausgegeben.

**P1. ESTV KS 37 (Version 30.10.2020), Hauptdokument** – Text aus lokaler Datei `art-17b/01_Recherche/quellen/KS37_ESTV_2020.txt`; Lexplorer doc 03addb87-fb11-42d6-8443-7fdb1b08ceaf, https://mcp-tax.lexplorer.ch/s/doc/03addb87-fb11-42d6-8443-7fdb1b08ceaf (Kennung aus Vorarbeit). Ziff. 2.3.2–2.3.2.3 (S. 5), 2.5 (S. 6), 6 (S. 11), 7.1 (S. 11 f.), 7.3.1–7.3.4 (S. 14–18), 8.1.1 (S. 18 f.), 8.1.3.2 (S. 20), 8.2 (S. 20).

**P2. KS 37 Anhang II «Fallbeispiele»** – doc ccf1675a-1432-4f0e-ae05-2d94dc4a8624, https://mcp-tax.lexplorer.ch/s/doc/ccf1675a-1432-4f0e-ae05-2d94dc4a8624. get_document_slice (1 Slice, vollständig). Nur Optionen; kein Beispiel zu unechten Beteiligungen.

**P3. KS 37 Anhang III «Musterbescheinigungen»** – doc 97c864dc-7181-46f6-8a56-8ce72fb2790e. nav_list_chunks (13 Chunks): Sachverhalte I–IV (Aktien, Optionen, RSU); kein Muster zu unechten Beteiligungen.

**P4. KS 37 Anhang IV «Fallbeispiele zur Quellenbesteuerung»** – doc a0f3aafe-2be8-4ed7-9e05-c8ce3c325bad, https://mcp-tax.lexplorer.ch/s/doc/a0f3aafe-2be8-4ed7-9e05-c8ce3c325bad. get_document_slice (1 Slice, vollständig). Tragend S. 1: «Der internationale Ansässigkeitswechsel zwischen Abgabe und Ausübung der Mitarbeiterbeteiligung löst die Besteuerung gemäss Artikel 97a DBG aus.»

**P5. KS 37 Anhang V «Elektronische Musterbescheinigungen», Ziff. V «Unechte Mitarbeiterbeteiligungen (Beispiel: Phantom Shares)»** – doc 96c03c16-4ede-49e4-a919-35c780d7f6e9; chunk b10314e1-57c8-4386-8b7e-d90b8d05c66a, https://mcp-tax.lexplorer.ch/s/doc/96c03c16-4ede-49e4-a919-35c780d7f6e9?chunk=b10314e1-57c8-4386-8b7e-d90b8d05c66a. Tragend: «Phantom Shares nicht in Aktien umgewandelt, sondern mit einer Geldleistung abgegolten werden, deren Höhe dem Verkehrswert zugrundeliegender Aktien entspricht». Dazu Ziff. IV (RSU, Zuzug): chunk a565ec39-3069-408e-8a1e-e26eed6b3f16, https://mcp-tax.lexplorer.ch/s/doc/96c03c16-4ede-49e4-a919-35c780d7f6e9?chunk=a565ec39-3069-408e-8a1e-e26eed6b3f16.

**P6. KS 37 Anhang I «Übersicht»** – doc f1133ebf-b909-4c12-8957-784594359a49, https://mcp-tax.lexplorer.ch/s/doc/f1133ebf-b909-4c12-8957-784594359a49 (Vorarbeit; nicht neu gelesen). «Phantom-Aktien/-Optionen, SARs, etc.»: «Realisation (Zufluss des geldwerten Vorteils)».

**P7. ZH: ZStB Nr. 17a.1, Merkblatt vom 6.1.2025, lit. A, D, E** – doc cb70f7eb-5a94-4b36-aeba-10652145b7cc, chunk b83b037a-d2d4-4e3d-aba7-6615bad4cfb8, https://mcp-tax.lexplorer.ch/s/doc/cb70f7eb-5a94-4b36-aeba-10652145b7cc?chunk=b83b037a-d2d4-4e3d-aba7-6615bad4cfb8. Tragend (D.I.1): «Der gesamte geldwerte Vorteil nach Abzug allfälliger Gestehungskosten unterliegt als Erwerbseinkommen der Einkommenssteuer.»

**P8. ZH: ZStB Nr. 100.1, Merkblatt vom 15.12.2020 (gültig ab 1.1.2021), Quellenbesteuerung exportierter Mitarbeiterbeteiligungen gemäss § 100 StG** – chunk 85de6577-e02a-4806-bc7d-762a193ac1bf (über nav_list_chunks des Zürcher Steuerbuchs gefunden), https://mcp-tax.lexplorer.ch/s/doc/cb70f7eb-5a94-4b36-aeba-10652145b7cc?chunk=85de6577-e02a-4806-bc7d-762a193ac1bf. Tragend (lit. A): «… oder unechte Mitarbeiterbeteiligungen (Phantom-Aktien/-Optionen, SAR usw.) während der Zeit zugeteilt erhielten oder teilweise verdienten, in der sie in der Schweiz ansässig waren, und die diese Mitarbeiterbeteiligungen erst nach dem Wegzug ins Ausland realisieren.»

**P9. SG: StB 30 Nr. 2 (Stand 1.1.2025), Ziff. 1.2, 2, 3** – doc 563bc34e-b2c3-4dd4-b945-5bc6585fa5cf, https://mcp-tax.lexplorer.ch/s/doc/563bc34e-b2c3-4dd4-b945-5bc6585fa5cf (Slice 0 gelesen). Tragend (Ziff. 2): «Unechte Mitarbeiterbeteiligungen (z.B. Phantom Shares) | Zufluss des geldwerten Vorteils (Art. 30ter Abs. 1 StG) | Geldwerter Vorteil (Art. 30ter Abs. 1 StG)».

**P10. SZ: Merkblatt «Besteuerung von Mitarbeiterbeteiligungen» vom 18.11.2025, N 2, 4, 30–34, 38** – doc 8755573e-cb4d-49c8-b826-ce3f5ba2b760, https://mcp-tax.lexplorer.ch/s/doc/8755573e-cb4d-49c8-b826-ce3f5ba2b760 (vollständig). Tragend (N 38): «Alle übrigen Mitarbeiterbeteiligungen sind im Wertschriften- und Guthabenverzeichnis ohne Steuerwert (pro memoria) aufzuführen».

**P11. LU: Steuerbuch Bd. 1, «Mitarbeiterbeteiligungen» (Vermögenssteuer, Stand 1.1.2024), Ziff. 3** – doc ba5b4aee-4e12-49a5-b3a5-37b4c2da0145, https://mcp-tax.lexplorer.ch/s/doc/ba5b4aee-4e12-49a5-b3a5-37b4c2da0145 (Vorarbeit art-17a). Tragend: «Unechte Mitarbeiterbeteiligungen unterliegen nicht der Vermögenssteuer, da sie keine definitiv erworbenen Vermögenswerte darstellen.» Einkommenssteuer: doc 954c9fcd-8547-4dd1-8587-631847aad25a (nur Verweis auf KS 37).

**P12. BE: TaxInfo «Mitarbeiterbeteiligungen» (Fassung 27.1.2022)** – chunk 21316eec-9113-4c97-a6e8-241a03bca668, https://mcp-tax.lexplorer.ch/s/doc/28edeed9-27cf-4444-bb20-95a75a525785?chunk=21316eec-9113-4c97-a6e8-241a03bca668 (neu gelesen). Keine Aussage zu unechten Beteiligungen.

**P13. BL: Steuerbuch Bd. 1, 24 Nr. 4 (30.4.2012/31.12.2016/08.08.2025), Ziff. 1.1, 2.3, 3, 4** – doc 6ea8e8d3-1db4-4673-af94-f10aba05a432, https://mcp-tax.lexplorer.ch/s/doc/6ea8e8d3-1db4-4673-af94-f10aba05a432 (vollständig). Tragend (Ziff. 3): «Geldwerte Vorteile aus «unechten» Mitarbeiterbeteiligungen (Anwartschaften auf blosse Bargeldabfindungen, rein rechnerisch an Aktienkurse gekoppelte Zahlungen, sog. «Phantom Stock Units») sind im Zeitpunkt ihres jeweiligen Zuflusses steuerbar.»

**P14. ZG: Zuger Steuerbuch, «Mitarbeiterbeteiligungen» (geändert 4.11.2025)** – doc 399c5404-d2ba-405d-8f44-c00a51403f2f, chunk c1f7a75b-6aae-4601-95ba-8e39f295edec (Vorarbeit art-17b). Nur Verweis auf KS 37.

**P15. GE: «Tableau récapitulatif …»** – doc 0ee6131f-6eaa-4672-a1d1-5685a970533c, https://mcp-tax.lexplorer.ch/s/doc/0ee6131f-6eaa-4672-a1d1-5685a970533c (vollständig; nichts zu unechten). **GE: Information fiscale 2/2016 vom 1.7.2016** – doc 6faa02c2-6c22-447f-a872-57b673d84e99, https://mcp-tax.lexplorer.ch/s/doc/6faa02c2-6c22-447f-a872-57b673d84e99 (vollständig). Tragend (Ziff. 2.1): «lors de la réalisation du revenu provenant de participations de collaborateur (options/expectatives sur actions ou sur espèces), y compris en cas de départ du collaborateur à l'étranger».

**P16. VD: Directive 21565 (01.2026)** – doc 632fe8c1-8114-49c2-9b7e-81bdb36c677b, https://mcp-tax.lexplorer.ch/s/doc/632fe8c1-8114-49c2-9b7e-81bdb36c677b (vollständig). Tragend (ch. IV): «b) Pour les participations improprement dites : à l'indemnité versée en espèce.» Ch. I: «Participations improprement dites […] - phantom stocks, - stock appreciation rights (SARs), etc.»

**P17. TG: StP 120a Nr. 1** – doc 98f00095-17df-41b8-a9f1-c16ebc23df31, https://mcp-tax.lexplorer.ch/s/doc/98f00095-17df-41b8-a9f1-c16ebc23df31; **StP 19 Nr. 3** – doc 538a627a-3b35-4bac-b437-081e308b4998, https://mcp-tax.lexplorer.ch/s/doc/538a627a-3b35-4bac-b437-081e308b4998; **StP 46 Nr. 3** – doc af69d293-011a-40fd-81ac-6f6a50700a42, https://mcp-tax.lexplorer.ch/s/doc/af69d293-011a-40fd-81ac-6f6a50700a42 (alle vollständig). Unechte Beteiligungen nicht ausdrücklich genannt; StP 46 Nr. 3: «Anwartschaften auf Mitarbeiterbeteiligungen unterliegen dagegen der Vermögenssteuer nicht.»

**P18. MBV im Lexplorer** – doc 28f816dc-1c9f-4fb8-8da2-217b3c58df0e (nicht gelesen; Text über Fedlex).

---

## L. ILE-Literatur (verwendete Treffer)

Auswertung in `ILE_Literatur.md`. lexplorer_url wie vom Werkzeug ausgegeben (ausser wo als abgeleitet gekennzeichnet).

| Nr. | Suche | Fundstelle | doc_id | Chunk-ID(s) | lexplorer_url | Abschnitt |
|---|---|---|---|---|---|---|
| L1 | Vorarbeit; Navigation | Oesterhelt/Gammeter, Das Formelwertprinzip bei Mitarbeiteraktien, FStR 2024/4, Ziff. 2.1, 2.2 (Fn. 11, 12), 3.1, 10, 11.6 | fb1b2dda-d30d-4c1d-9bed-e363bc738452 | ff07732d-577a-4f7a-ac0e-9ec800a53abb; ef1a6e1d-69ea-4b73-a811-1f4095c3dbd8; 5ad883da-3ac9-4f8c-a913-a74a9884920c; 051e3cf5-4005-48c6-bf2e-fe44ed28fead; 27617312-3b9d-4265-acc1-bd769efedb1f; 17a30200-edbd-4f85-b17d-f951b119f7ca (versprengter Satz) | https://app.lexplorer.ch/suche?e_chunks=13889&e_sys=ile; https://app.lexplorer.ch/suche?e_chunks=13887&e_sys=ile; https://app.lexplorer.ch/suche?e_chunks=13895&e_sys=ile; https://app.lexplorer.ch/suche?e_chunks=14021&e_sys=ile; Dokument https://app.lexplorer.ch/suche?e_id=592&e_sys=ile | A.1, B.1, F.2 |
| L2 | 9 | Oesterhelt/Opel, Rechtsprechung 2024/1, FStR 2024/1, Ziff. 2.2–2.3 (BGer 16.8.2023, Bonus), S. 56–57 | c8ae20f7-114b-4b55-a83d-ca6769e84f1b | 3df8e1b5-f3a7-4181-84cd-d7263cac4be5; 0c072188-9b81-4b30-9fd4-17c3a089f054; d9307ec2-6a0a-451b-ae5f-e5e8a7571039; 81465b3b-1fdc-4b50-92a9-4979f7d68818 | https://app.lexplorer.ch/suche?e_chunks=13681&e_sys=ile; https://app.lexplorer.ch/suche?e_chunks=13682&e_sys=ile; Dokument https://app.lexplorer.ch/suche?e_id=577&e_sys=ile | A.2 |
| L3 | 1, 8 (Doc); Navigation | Oesterhelt/Truffer, ILE-Seminar Einkommenssteuer 2020, Mitarbeiterbeteiligung, Folien «Grundsätze der Vermögenssteuer», «Interkantonale Aspekte» | d51d1cd9-28c6-40c5-a671-0cbd63539415 | b40e5c3a-6433-4372-b557-3a321a847985; d4d4fb91-3255-4685-9e4f-eb717cd00853 | https://app.lexplorer.ch/suche?e_chunks=56692&e_sys=ile; https://app.lexplorer.ch/suche?e_chunks=56676&e_sys=ile | A.3, F.1 |
| L4 | 8 | Niederbacher-Puchegger/Risi, Mitarbeiteroptionen und Verrechnungspreis-Aspekte, FStR 2005/1, Ziff. 3.4 | 0da9c2e0-495d-49b8-950c-ea06643fa42e | e6a9cf09-90ee-4577-b1fe-3d41fe7146c7 | https://app.lexplorer.ch/suche?e_chunks=8513&e_sys=ile | A.4 |
| L5 | 8 | Bertschinger, Die handels- und steuerrechtliche Behandlung von Mitarbeiterbeteiligungen bei der Arbeitgeberin, FStR 2023/1, Ziff. 4 | b692106b-9910-48d1-bb3b-c7deab52cc1e | 03ce6009-29d5-44cb-84f4-95211ec7f0da | https://app.lexplorer.ch/suche?e_chunks=12540&e_sys=ile | A.5 |
| L6 | Vorarbeit; Navigation | Oesterhelt/Fenners, ILE-Seminar personenbezogene Unternehmen 2025, Besteuerung von Mitarbeiteraktien, Folien «Co-Investment» | 5a293fd8-1a40-4de4-b41f-99ce4351ce88 | dec50b69-23ac-4095-869e-4784a8e2becb; 172bbe68-5029-4533-9e08-08caa58a22b7 | https://app.lexplorer.ch/suche?e_chunks=48826&e_sys=ile; Dokument https://app.lexplorer.ch/suche?e_id=1458&e_sys=ile | B.2 |
| L7 | 2 | Poltera/Seematter, ILE-Seminar Unternehmensbesteuerung 2016, Kauf und Verkauf von Unternehmen, Folien 12–15 | 9e0a5620-a916-4600-a406-7b12016c4ea4 | 1051b8c4-3663-447e-a5ec-6c5ca0e0751f; c8805447-1bfb-4de4-baee-b92c73559f4e | https://app.lexplorer.ch/suche?e_chunks=62887&e_sys=ile; https://app.lexplorer.ch/suche?e_chunks=62885&e_sys=ile; Dokument https://app.lexplorer.ch/suche?e_id=1754&e_sys=ile | B.3 |
| L8 | 1, 3, 8 | Buchmann/Schreiber, ILE Internationales Steuerseminar 2019, Folie 8 und Definition | c78ae5b0-c517-4830-b8bd-c5465e9fcbe2 | 481c8259-c5d3-436b-ae04-ca9cb6adfdd0; 6be2af06-4fe7-45f5-ac55-a3c7597b2059 | https://app.lexplorer.ch/suche?e_chunks=56418&e_sys=ile; https://app.lexplorer.ch/suche?e_chunks=56416&e_sys=ile | B.4 |
| L9 | 1, 2 | Bucher/Marbach, ILE Internationales Steuerseminar 2022, MIP | 79fa60e0-3bc9-4ffa-af5c-b62d9ecfbdd0 | a3835c45-b359-4609-96d1-bff5689613f9 | https://app.lexplorer.ch/suche?e_chunks=53989&e_sys=ile | B.5 |
| L10 | Vorarbeit (nicht neu gelesen) | Oesterhelt/Opel, Rechtsprechung 2025-1, FStR 2025/1, Ziff. 1.3 (9C_168/2023) | dc394ef9-3a50-47c8-be97-f3c2c4846ab1 | dc734c25-0dba-4199-80e2-f49483a929ff | https://app.lexplorer.ch/suche?e_chunks=14438&e_sys=ile | C.1 |
| L11 | 3 | Mühlemann, Tax Accounting für anteilsbasierte Vergütungen, FStR 2013/3, Ziff. 1.2 | 80936eaf-e13c-48a4-97a0-25bb28d9a528 | 7efc6dab-4816-462d-a815-aa37e2540d48 | https://app.lexplorer.ch/suche?e_chunks=18002&e_sys=ile | C.2 |
| L12 | 6 | Peyer/Schreiber/Walt, ILE Internationales Steuerseminar 2024, Verständigungsverfahren, Folie «MA-Beteiligungen» | 5c0ecafe-99c5-4798-b2d0-9dd22adf29fb | 56ca079c-8a59-468f-bf7c-33f08a066890 | https://app.lexplorer.ch/suche?e_chunks=50258&e_sys=ile | F.3 |
| L13 | 6 | Allemann/Bloch-Riemer, ILE Internationales Steuerseminar 2021, Arbeitgeber in der Haftung | 3ac15de8-f2da-48cd-8270-57de8500f5c0 | c637de6e-34b7-4fff-b804-ab558ed20ae4 | https://app.lexplorer.ch/suche?e_chunks=58607&e_sys=ile | F.4 |
| L14 | Vorarbeit (nicht neu gelesen) | Risi, Bericht der gemischten Arbeitsgruppe, FStR 2002/3, Ziff. 4.3 Fn. 39 | 098d9241-b114-47e9-84ab-a4295a913c7e | – (Slice-Lektüre) | https://app.lexplorer.ch/suche?e_id=110&e_sys=ile | G.1 |

Gefunden, nicht verwendet: Jaeger (Rezension), FStR 2002/1, chunk 22e88400-a298-4c52-a4bf-b317e18c8a94; Brozzo/Stocker 2024, chunks fb05fbf7-5d3b-4149-925c-b9c98cdc4ec0, ccf5bcc2-26c5-4247-93e6-cc7d8428be9c; Stocker/Wolfensberger 2025, chunk 23f1920e-8f3e-4557-8e4d-c7bcb5d066f1; Oesterhelt/Truffer 2020, chunk 798748fa-2bcd-40bd-b989-93513871f55d (Milestone Payments); Bucher/Marbach 2022, chunk 9dc3abdd-d90f-4826-b1d1-aebea5d7f06a (Transaktionsbonus, nur Vorschau).

---

**Zahl der Lexplorer-Suchen in diesem Auftrag: 9** (8 × search_chunks_hybrid, 1 × search_chunks_keyword; 0 × find_leading_cases). Davon 0 für die Verwaltungspraxis, 9 für die ILE-Literatur.
