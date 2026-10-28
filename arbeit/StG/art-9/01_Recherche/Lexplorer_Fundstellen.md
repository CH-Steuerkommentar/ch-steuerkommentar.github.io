# Art. 9 StG – Besondere Fälle: Fundstellen Verwaltungspraxis und ILE-Lehre (Lexplorer / Open Case Law)

Arbeitsdatei, Stand 28.10.2026. Hilfsagent Praxis/ILE. Keine Rechtsprechung recherchiert, keine Websuche.

## 0. Methode, Vorarbeiten, Grenzen

- **Vorarbeiten wiederverwendet (vor jeder Suche geprüft):** art-8/01_Recherche/Lexplorer_Fundstellen.md (Suchen 9 und 10 zu lit. d und lit. e; KS 5a- und KS 32a-Register; Kapitalband 2.8), art-6/01_Recherche/Lexplorer_Fundstellen.md (§ 1 N 6–10, N 190–193, N 217–219; Hinny FStR 2001/4), art-5/01_Recherche/Lexplorer_Fundstellen.md und Lexplorer_ILE.md (KS 5a Ziff. 2.4.1 Chunk 9170fcb7; KS 32a Ziff. 4.2.4 b; Checkliste Mitteilung-020; Seminar 2025 Folien 69 f.), art-5/01_Recherche/Materialien.md Ziff. 7 (Art. 12 StV), art-7/01_Recherche/Lexplorer_Fundstellen.md (Kapitalband; KS 29c). Zitate aus Vorarbeiten sind als «Vorlauf» gekennzeichnet; alle tragenden Stellen unten wurden heute erneut am Volltext gelesen, ausser wo «Vorlauf» steht.
- **Verwaltungspraxis:** Open Case Law (`get_practice`): KS 5a (365 209 Zeichen, in Datei ausgelagert) – sämtliche Fundstellen «Artikel 9» (Grep) samt Kontext gelesen: Ziff. 2.4.1, 3.2.1, 3.2.2.4 (DBG-Sperrfrist, zum Vergleich), 3.2.6, 4.2.1.5, 4.2.4 (ganz), 4.2.5 (ganz), Anhang Nr. 2 (ganz), Nr. 3 (ganz), Nr. 8 (Abschnitt Emissionsabgabe). KS 5 vom 1.6.2004 (aufgehoben; 356 679 Zeichen) – Grep «Artikel 9», Ziff. 2.4.1, 3.2.6, 4.4.1.3, Anhang Nr. 2 gelesen. Lexplorer, Kategorie 02-verwaltungspraxis: KS 5a durch `nav_list_chunks` (Chunk-IDs), KS 32a Chunk 8b50916c, «Geltende Steuern» Chunk 46727844, Quellenliste «ESTV Medien und News» (`nav_list_documents`, kein Dokument «Eidgenössische Stempelabgaben» vorhanden).
- **ILE-Literatur:** filter_kanton CH, filter_category 08-institut-fuer-law-und-economics. Treffer aus «ILE-HSG — Lehrbuch Steuerrecht» (e_chunks 44703, 44704, 44705) übergangen. Oesterhelt/Tschan, Verrechnungssteuer und Stempelabgaben (IFF-Schriftenreihe, Pfad `doc_0127_128_…` = **Bd. 128**, 2025): § 1 Teile I–V und XII–XIX sowie § 7 durch `nav_list_chunks` vollständig gesichtet (Inhaltsverzeichnis § 1 I–XIX, alle Kapitelüberschriften § 7); § 4 N 68–72 und Abschn. 5 gelesen.
- **Rechtsstatus:** KS 5a, KS 32a, KS 29c, Checkliste Mitteilung-020 «in Kraft». KS 5 vom 1.6.2004 aufgehoben (frühere Praxis). «Geltende Steuern» und «Das schweizerische Steuersystem»: Lexplorer-Status «Materialien» (Informationsschriften). Keine künftigen Fassungen oder Entwürfe verwendet.

## 1. Suchprotokoll

### 1.1 Lexplorer (13 von höchstens 15 Suchen)

| Nr. | Werkzeug | Kategorie | Abfrage | Treffer | verwendet |
|---|---|---|---|---|---|
| 1 | search_chunks_keyword | 08-ILE | Art. 9 Abs. 1 lit. e StG | 10 | 29858 (§ 1 N 190–193, CV); 49055 (Aebi/Brozzo, Seminar 2025 Stiftungen); übrige (FStR 2025/1, 2015/2, 2019/4, 2026, Debt push down) nicht einschlägig |
| 2 | search_chunks_hybrid | 08-ILE | Einzelunternehmen Kollektivgesellschaft Sacheinlagegründung Aktiengesellschaft Emissionsabgabe nur auf Nennwert Veräusserung Beteiligungsrechte innert fünf Jahren nachträgliche Abrechnung Emissionsabgabe Mehrwert | 10 | keiner (53405, 53568, 64016, 53391, 51428, MWST-Seminar 2023: ohne lit. e) |
| 3 | search_chunks_keyword | 08-ILE | Umwandlung Personenunternehmung Emissionsabgabe | 3 | 1717 (FStR 2001/1, Entstehung); 11326 → Navigation FStR 2022/1 (Oesterhelt/Schreiber; Ziff. 6.2/6.3 gelesen: keine EA-Aussage) |
| 4 | search_chunks_hybrid | 08-ILE | Genossenschaft Emissionsabgabe Einzahlungen auf das Genossenschaftskapital Rückzahlungen während des gleichen Geschäftsjahres Art. 9 Abs. 2 StG Genossenschaftsanteile Austritt | 8 | keiner (Lehrbuch übergangen) |
| 5 | search_chunks_keyword | 02-Verwaltungspraxis | Genossenschaftskapital Emissionsabgabe | 0 | – |
| 6 | search_chunks_hybrid | 02-Verwaltungspraxis | Emissionsabgabe Genossenschaft Genossenschaftsanteile Einzahlungen Rückzahlungen Geschäftsjahr Abrechnung Formular | 8 | 46727844 («Geltende Steuern», ohne Art.-9-Aussage); sonst SSK KS 28 (Vermögenssteuer), Merkblätter VSt – nicht einschlägig |
| 7 | search_chunks_keyword | 08-ILE | Genussscheine Emissionsabgabe | 2 | keiner (nur Lehrbuch, übergangen) |
| 8 | search_chunks_hybrid | 08-ILE | Privatisierung Anstalt des öffentlichen Rechts Umwandlung in Aktiengesellschaft Emissionsabgabe Dotationskapital Nennwert; Verein Sportclub Umwandlung Aktiengesellschaft Emissionsabgabe | 8 | 2998 → Navigation 2999 (Schmid/Lehmann FStR 2002/4); 48395 (Vorlauf, nur KER) |
| 9 | search_chunks_hybrid | 08-ILE | Revision Stempelgesetz 1991/1993 ermässigter Abgabesatz Emissionsabgabe Fusion fusionsähnlicher Zusammenschluss bisheriger Art. 9 StG ersetzt durch Ausnahme Art. 6 Abs. 1 lit. abis | 8 | 53397 (Seminar 2023, Stiftung); 1717 (bereits); zu lit. a–c nichts |
| 10 | search_chunks_keyword | 08-ILE | Sperrfristverletzung Emissionsabgabe Nennwert | 0 | – |
| 11 | search_chunks_hybrid | 08-ILE | Art. 9 Abs. 1 lit. e StG Veräusserungssperrfrist fünf Jahre Emissionsabgabe nachträglich auf Mehrwert Verkehrswert anteilsmässig Personengesellschaft Stiftung Verein Bestand fünf Jahre | 0 | – |
| 12 | search_chunks_hybrid | 08-ILE | Emissionsabgabe nur auf dem Nennwert Veräusserungssperrfrist fünf Jahre Personengesellschaft | 10 | 51431 (Seminar 2024, CV); 49111 (Bieri/Risi, Seminar 2025, L-QIF) |
| 13 | search_chunks_hybrid | 02-Verwaltungspraxis | unentgeltlich ausgegebene Genussscheine 3 Franken je Genussschein Emissionsabgabe | 8 | nur Bekanntes (KS 32a 4.2.4 b; 4.2.3 b betrifft VSt); MB S-027.289.1 (VSt, Gratisaktien), ohne Genussschein-EA |

Nicht gezählt (Navigation/Lesen): `nav_list_chunks` (KS 5a e163e163…; § 1 I–V 28f448bc…; § 1 XII–XIX a61a9b0c…; § 7 93b8e513…; FStR 2022/1 c20a722f…; FStR 2002/4 471627c4…), `nav_list_documents` (ESTV Medien und News), `get_document_slice` (FStR 2001/1, Slices 0 und 75, Autorensuche erfolglos), `get_chunk_content` für alle unten genannten Chunks.

### 1.2 Open Case Law (nicht auf das Lexplorer-Budget angerechnet)

| Nr. | Abfrage (search_practice) | Filter | Treffer |
|---|---|---|---|
| OCL 1 | Genossenschaftskapital Einzahlungen Rückzahlungen Geschäftsjahr Emissionsabgabe | ESTV | 0 |
| OCL 2 | "Artikel 9 Absatz 1 Buchstabe e" OR "Art. 9 Abs. 1 Bst. e StG" OR "Art. 9 Abs. 1 lit. e StG" | ESTV | KS 5 (2004), KS 5a |
| OCL 3 | Genossenschaftsanteile Emissionsabgabe | estv_ks | KS 32a, KS 5, KS 5a (keine Genossenschafts-Bemessungsregel) |
| OCL 4 | Genussscheine unentgeltlich "drei Franken" OR "3 Franken" | ESTV | KS 32a (Ziff. 4.2.4 b); MWST-Branchen-Info 03 (nicht einschlägig) |

`get_practice`: estv_ks_dbst_ks_2022_1_005a_dvs_de (KS 5a), estv_ks_dbst_ks_2004_1_005_dvs_de (KS 5, aufgehoben).

---

## 2. Fundstellen – Verwaltungspraxis

### V.1 ESTV, Kreisschreiben Nr. 5a vom 1. Februar 2022, «Umstrukturierungen» (Direkte Bundessteuer, Verrechnungssteuer und Stempelabgaben), 1-005a-DVS-2022-d

- Link: PDF https://www.estv.admin.ch/dam/de/sd-web/BmJ1WWSC79gq/dbst-ks-2022-1-005a-dvs-de.pdf (OCL doc_id estv_ks_dbst_ks_2022_1_005a_dvs_de); Lexplorer-Dokument https://mcp-tax.lexplorer.ch/s/doc/e163e163-e38f-4631-85a6-455c20a8c29a (Status «in Kraft»).

**V.1.1 Ziff. 2.4.1 (Rechtliche Grundlagen, Emissionsabgabe)** – Chunk 9170fcb7-2a44-4cf5-afa2-fa5d338547b9 – https://mcp-tax.lexplorer.ch/s/doc/e163e163-e38f-4631-85a6-455c20a8c29a?chunk=9170fcb7-2a44-4cf5-afa2-fa5d338547b9 (Wortlaut heute im OCL-Volltext gelesen)
- «Artikel 9 Absatz 1 Buchstabe e StG bestimmt, dass die Emissionsabgabe bei der Begründung oder Erhöhung von Beteiligungsrechten im Rahmen von Fusionen, Spaltungen oder Umwandlungen von andern Rechtsträgern als Kapitalgesellschaften und Genossenschaften auf ein Prozent des Nennwerts beschränkt wird. Die Reduktion der Bemessungsgrundlage für die Emissionsabgabe bei Fusionen, Spaltungen oder Umwandlungen wird jedoch nur dann gewährt, wenn der bisherige Rechtsträger während mindestens fünf Jahren bestand. Im Weiteren wird über den Mehrwert nachträglich abgerechnet, soweit während den der Umstrukturierung nachfolgenden fünf Jahren die Beteiligungsrechte veräussert werden.»
- Unmittelbar davor (Abgrenzung lit. abis): «Gemäss Artikel 6 Absatz 1 Buchstabe abis … sind von der Emissionsabgabe ausgenommen Beteiligungsrechte, die in Durchführung von Beschlüssen über Fusionen oder diesen wirtschaftlich gleichkommenden Zusammenschlüssen, Umwandlungen und Spaltungen von Aktiengesellschaften, Kommanditaktiengesellschaften, Gesellschaften mit beschränkter Haftung oder Genossenschaften begründet oder erhöht werden.»
- Normstelle: Abs. 1 lit. e (Anwendungsbereich, Bestand, Nachbesteuerung); Abgrenzung zu Art. 6 Abs. 1 lit. abis.

**V.1.2 Ziff. 3.2.1 (Übertragung eines Betriebes oder Teilbetriebes auf eine juristische Person, Tatbestände)** – im Lexplorer-Chunk-Verzeichnis nicht eindeutig zuordenbar; Fundort PDF S. 21 (OCL-Volltext)
- «Unter die Übertragung eines Betriebes oder Teilbetriebes auf eine juristische Person fallen insbesondere folgende Umstrukturierungstatbestände im steuerlichen Sinn: • Zusammenschluss mit einer juristischen Person; • Umwandlung einer Personenunternehmung in eine Kapitalgesellschaft oder Genossenschaft; • Umwandlung der schweizerischen Betriebsstätte einer ausländischen Personengesellschaft in eine Kapitalgesellschaft. Die Übertragung kann zivilrechtlich auf folgende Weise erfolgen: • Sacheinlage; • Verkauf; • Fusion (nur für Kollektiv- und Kommanditgesellschaften; Art. 3-22 FusG); • Umwandlung (nur für Kollektiv- und Kommanditgesellschaften; Art. 53-68 FusG); • Vermögensübertragung (Art. 69-77 FusG).»
- «Die Umwandlung eines Einzelunternehmens in eine Kapitalgesellschaft erfolgt zivilrechtlich entweder durch Sacheinlage in eine neugegründete Kapitalgesellschaft oder durch die im FusG geregelte Vermögensübertragung (allenfalls kombiniert mit einem Verkauf) auf eine bereits bestehende Kapitalgesellschaft (Art. 69-77 FusG).»
- Normstelle: Abs. 1 lit. e (Rechtsträger «Einzelunternehmen, Handelsgesellschaften ohne juristische Persönlichkeit»; zivilrechtliche Wege).

**V.1.3 Ziff. 3.2.6 (Emissionsabgabe bei Übertragung auf eine juristische Person)** – PDF S. 26 (OCL-Volltext)
- «Nach Artikel 9 Absatz 1 Buchstabe e StG beträgt die Emissionsabgabe bei der Begründung von Beteiligungsrechten im Rahmen einer Umwandlung einer Personenunternehmung in eine Kapitalgesellschaft oder Genossenschaft, vorbehältlich des Freibetrages nach Artikel 6 Absatz 1 Buchstabe h StG, 1 Prozent des Nennwerts. Die übertragenen offenen und stillen Reserven sind von der Steuer ausgenommen. Die Reduktion der Bemessungsgrundlage für die Emissionsabgabe bei Fusionen, Spaltungen oder Umwandlungen wird jedoch nur dann gewährt, wenn der bisherige Rechtsträger während mindestens fünf Jahren bestand. Im Weiteren ist über den Mehrwert nachträglich anteilsmässig abzurechnen, soweit während den der Umstrukturierung nachfolgenden fünf Jahren Beteiligungsrechte veräussert werden.»
- «Der Übergang des Eigentums an den Beteiligungsrechten durch Erbgang, Schenkung oder andere unentgeltliche Rechtsgeschäfte, einschliesslich steuerneutraler Umstrukturierungen, stellt keine Sperrfristverletzung dar. Dies gilt auch für entgeltliche Übertragungen, sofern der Preis das übertragene Eigenkapital nicht übersteigt.»
- Normstelle: Abs. 1 lit. e (Bemessung Nennwert, lit. h, Reserven, anteilige Nachabrechnung, Veräusserungsbegriff).

**V.1.4 Ziff. 3.2.2.4 (Veräusserungssperrfrist DBG – nur zum Vergleich, keine EA-Aussage)** – PDF S. 24 f.
- «Die Veräusserungssperrfrist beginnt am Tag der Eigentumsübertragung. Bei der Umwandlung einer Personenunternehmung in eine juristische Person beginnt die Veräusserungssperrfrist mit der Anmeldung beim Handelsregisteramt, sofern und soweit für die zivilrechtlich massgebende Abwicklung ein Eintrag im Handelsregister nötig ist. Eine rückwirkende Umwandlung ist für den Beginn der Veräusserungssperrfrist wirkungslos.»
- «Schon der Verkauf eines einzigen Beteiligungs- oder Mitgliedschaftsrechtes stellt eine Verletzung der Veräusserungssperrfrist dar und führt zu einer anteiligen Nachbesteuerung der übertragenen stillen Reserven. … Die Veräusserungssperrfrist ist verobjektiviert.»
- Normstelle: Abs. 1 lit. e Satz 2 (Fristbeginn, Veräusserung) – nur Analogie; KS 5a überträgt diese Regeln in Ziff. 3.2.6 nicht ausdrücklich auf die Emissionsabgabe.

**V.1.5 Ziff. 4.2.1.5 (Umwandlung einer juristischen Person in eine andere juristische Person im Allgemeinen, Emissionsabgabe)** – PDF S. 52 f.
- «Bei einer Umwandlung durch den Wechsel der Rechtsform (Rechtsformwechsel; direkte Umwandlung) werden keine neuen Beteiligungsrechte begründet oder erhöht. Die Emissionsabgabe ist somit nicht betroffen.»
- «Nach Artikel 9 Absatz 1 Buchstabe e StG ist die Emissionsabgabe bei der Begründung oder Erhöhung von Beteiligungsrechten im Rahmen einer Umwandlung eines Vereins, einer Stiftung oder eines Unternehmens des öffentlichen Rechts in eine Kapitalgesellschaft oder Genossenschaft, vorbehältlich des Freibetrages nach Artikel 6 Absatz 1 Buchstabe h StG, auf ein Prozent des Nennwerts beschränkt. Die übertragenen offenen und stillen Reserven sind von der Steuer ausgenommen. …»
- Normstelle: Abs. 1 lit. e (Verein, Stiftung, Unternehmen des öffentlichen Rechts).

**V.1.6 Ziff. 4.2.4.1 und 4.2.4.5 (Umwandlung eines Vereins, einer Stiftung oder einer übrigen juristischen Person in eine Kapitalgesellschaft oder Genossenschaft)** – Ende 4.2.4.5 in Chunk 4df96489-29e9-4f1c-be7b-a778ab7ad3ef – https://mcp-tax.lexplorer.ch/s/doc/e163e163-e38f-4631-85a6-455c20a8c29a?chunk=4df96489-29e9-4f1c-be7b-a778ab7ad3ef (heute gelesen); Anfang im OCL-Volltext (PDF S. 56 f.)
- 4.2.4.1: «Nur die Umwandlung eines im Handelsregister eingetragenen Vereins ist zivilrechtlich durch einen Rechtsformwechsel möglich (Art. 54 Abs. 5 FusG). Alle übrigen Vereine, Stiftungen oder übrigen juristische Personen können nur indirekt, d.h. übertragend, in eine Kapitalgesellschaft oder Genossenschaft umgewandelt werden.»
- 4.2.4.5: «Nach Artikel 9 Absatz 1 Buchstabe e StG ist die Emissionsabgabe bei der Begründung oder Erhöhung von Beteiligungsrechten im Rahmen einer Umwandlung eines Vereins oder einer Stiftung in eine Kapitalgesellschaft oder Genossenschaft, vorbehältlich des Freibetrages nach Artikel 6 Absatz 1 Buchstabe h StG, auf ein Prozent des Nennwerts beschränkt. Die übertragenen offenen und stillen Reserven sind von der Steuer ausgenommen. Diese Reduktion der Bemessungsgrundlage für die Emissionsabgabe wird jedoch nur dann gewährt, wenn der bisherige Rechtsträger während mindestens fünf Jahren bestand. Im Weiteren ist über den Mehrwert nachträglich anteilsmässig abzurechnen, soweit während den der Umwandlung nachfolgenden fünf Jahren Beteiligungsrechte veräussert werden.»
- Normstelle: Abs. 1 lit. e (Verein, Stiftung; Befund: Überschrift 4.2.4 nennt auch «übrige juristische Person», Ziff. 4.2.4.5 nur Verein und Stiftung).

**V.1.7 Ziff. 4.2.5.1 und 4.2.5.4 (Umwandlung eines Instituts des öffentlichen Rechts)** – Chunk 4df96489-29e9-4f1c-be7b-a778ab7ad3ef (wie oben, heute gelesen)
- 4.2.5.1: «Als Institute des öffentlichen Rechts, die eine direkte Umwandlung (Rechtsformwechsel) vornehmen können (Art. 99-101 FusG), gelten die im Handelsregister eingetragenen, organisatorisch verselbständigten Einrichtungen des öffentlichen Rechts des Bundes, der Kantone und der Gemeinden, unabhängig, ob sie als juristische Person ausgestaltet sind oder nicht (Art. 2 Bst. d FusG).»
- 4.2.5.4: «Nach Artikel 9 Absatz 1 Buchstabe e StG ist die Emissionsabgabe bei der Begründung oder Erhöhung von Beteiligungsrechten im Rahmen einer Umwandlung eines Unternehmens des öffentlichen Rechts in eine Kapitalgesellschaft oder Genossenschaft, vorbehältlich des Freibetrages nach Artikel 6 Absatz 1 Buchstabe h StG, auf ein Prozent des Nennwerts beschränkt. Die übertragenen offenen und stillen Reserven sind von der Steuer ausgenommen. …»
- Normstelle: Abs. 1 lit. e (Unternehmen des öffentlichen Rechts).

**V.1.8 Ziff. 4.2.6.7 (Umwandlung einer Kapitalgesellschaft oder Genossenschaft in eine Personenunternehmung)** – Chunk 4df96489 (heute gelesen): «Nicht betroffene Steuer • Emissionsabgabe.» – Normstelle: Abs. 1 lit. e (Gegenrichtung nicht erfasst).

**V.1.9 Anhang Nr. 2 «Umwandlung einer Personenunternehmung in eine Kapitalgesellschaft; Sperrfristverletzung (Ziff. 3.2)»** – Anhang S. 4–9 (OCL-Volltext, ganz gelesen)
- Sachverhalt: «Das Einzelunternehmen A. Müller soll durch Sacheinlagegründung in eine GmbH umgewandelt werden.» Eröffnungsbilanz: Stammkapital 100, KER 100 (je «übertragenes steuerliches Eigenkapital»), unversteuerte stille Reserven 500. «Drei Jahre nach der Umwandlung verkauft A. Müller 60 Prozent seiner Stammeinlage», Varianten a) 660 an Dritten, b) 340 an Dritten, c) 120 an Sohn, d) 130 an Sohn.
- Emissionsabgabe: «Im Weiteren ist über den Mehrwert nachträglich anteilsmässig abzurechnen, soweit während den der Umwandlung nachfolgenden fünf Jahren Beteiligungsrechte veräussert werden und der Verkehrswert den Freibetrag (Art. 6 Abs. 1 Bst. h StG) übersteigt. Berechnung Sperrfristverletzung gemäss Beispiel a): Stammkapital 100 / 60% der übertragenen offenen Reserven von 100 60 / 60% der übertragenen stillen Reserven von 500 300 / 460 Nach Abzug des Freibetrags von 1'000 ist keine Emissionsabgabe geschuldet.»
- Normstelle: Abs. 1 lit. e Satz 2 (Berechnung des Mehrwerts, Quote, Verhältnis zu lit. h).

**V.1.10 Anhang Nr. 3 «Umwandlung einer Personenunternehmung in eine Kapitalgesellschaft; Vorjahresverluste (Ziff. 3.2)»** – Anhang S. 9 f. (ganz gelesen)
- Sachverhalt: «Die Kollektivgesellschaft A&B soll in eine Aktiengesellschaft umgewandelt werden.» Aktienkapital nach Umwandlung 100, stille Reserven 500.
- Emissionsabgabe: gleichlautend mit Nr. 2 (Satz bis «… der Verkehrswert den Freibetrag (Art. 6 Abs. 1 Bst. h StG) übersteigt.»), ohne Berechnung.
- Normstelle: Abs. 1 lit. e (Handelsgesellschaft ohne juristische Persönlichkeit).

**V.1.11 Anhang Nr. 8 «Umwandlung eines Instituts des öffentlichen Rechts in eine Kapitalgesellschaft oder in eine Genossenschaft; Rechtsformwechsel (Ziff. 4.2.5)»** – Anhang S. 23 (Abschnitt Emissionsabgabe gelesen)
- Sachverhalt: «Schlussbilanz einer Kantonalbank vor der Umwandlung in eine AG», Dotationskapital 2'000.
- «Der Nennwert der im Zuge der Umwandlung begründeten Beteiligungsrechte beträgt 2'000. Von diesem Betrag kann der noch nicht beanspruchte Freibetrag (Art. 6 Abs. 1 Bst. h StG) in Abzug gebracht werden.»
- Normstelle: Abs. 1 lit. e (Rechtsformwechsel eines öffentlich-rechtlichen Unternehmens; lit. h).

### V.2 ESTV, Kreisschreiben Nr. 5 vom 1. Juni 2004, «Umstrukturierungen» (aufgehoben; frühere Praxis)

- PDF https://www.estv.admin.ch/dam/de/sd-web/m8L5i9gMslCi/dbst-ks-2004-1-005-dvs-de.pdf (OCL doc_id estv_ks_dbst_ks_2004_1_005_dvs_de)
- Ziff. 2.4.1: «Das FusG führt eine neue Regelung in Artikel 9 Absatz 1 Buchstabe e StG ein, wonach die Emissionsabgabe bei der Begründung oder Erhöhung von Beteiligungsrechten im Rahmen von Fusionen, Spaltungen oder Umwandlungen von andern Rechtsträgern als Kapitalgesellschaften und Genossenschaften auf ein Prozent des Nennwerts beschränkt wird.»
- Ziff. 3.2.6: «… 1 Prozent des Nennwerts. Die übertragenen stillen Reserven sind von der Steuer ausgenommen.» (ohne Vorbehalt lit. h und ohne «offenen» Reserven – Unterschied zu KS 5a)
- Anhang Nr. 2: «… soweit während den der Umwandlung nachfolgenden fünf Jahren Beteiligungsrechte veräussert werden und der Verkehrswert die Freigrenze (Art. 6 Abs. 1 Bst. h StG) übersteigt.» (Begriff «Freigrenze»; keine Berechnung)
- Ziff. 4.4.1.3 (Ausgliederung, nicht lit. e): «… ist die Emissionsabgabe anteilsmässig auf dem Verkehrswert des übertragenen Aktivenüberschusses (Aktienkapital, offene Reserven und Gewinnvortrag sowie stille Reserven inkl. Goodwill), vorbehältlich einer allfälligen Freigrenze nach Artikel 6 Absatz 1 Buchstabe h StG, geschuldet. Die Abgabeforderung wird 30 Tage nach Verletzung der Sperrfrist zur Zahlung fällig.» – Normstelle: lit. e Satz 2 nur als Analogie (Verkehrswertbegriff, Fälligkeit); seit KS 5a für die Ausgliederung aufgegeben (Oesterhelt/Tschan, § 1 N 7 f., unten L.3).

### V.3 ESTV, Kreisschreiben Nr. 32a vom 20. Januar 2025, «Sanierung von Kapitalgesellschaften und Genossenschaften» (Direkte Bundessteuer, Verrechnungssteuer und Stempelabgaben)

- PDF https://www.estv.admin.ch/dam/de/sd-web/NkHH-TkCqMnq/dbst-ks-2025-1-032a-dvs-de.pdf (OCL estv_ks_dbst_ks_2025_1_032a_dvs_de); Ziff. 4.2.4 b) Chunk 8b50916c-d9c2-4c38-b1c6-171458c71f9c – https://mcp-tax.lexplorer.ch/s/doc/c5dfca80-98f2-47a1-a63b-a8660c765a93?chunk=8b50916c-d9c2-4c38-b1c6-171458c71f9c (heute ganz gelesen, Status «in Kraft»)
- «Bei der Ausgabe von Sanierungsgenussscheinen handelt es sich um eine Begründung von Beteiligungsrechten im Sinn von Artikel 5 Absatz 1 Buchstabe a Strich 4 StG, die der Emissionsabgabe unterliegt.»
- «Die Emission von Sanierungsgenussscheinen ist als unentgeltlich zu bezeichnen, wenn sie nicht auf einer mit dem Forderungsverzicht verbundenen Verpflichtung der Gesellschaft beruht. Unter diesen Umständen qualifiziert der Forderungsverzicht als eigenständige Leistung, die rechtlich nicht als Gegenleistung für den Erhalt des Sanierungsgenussscheins bezeichnet werden kann. In diesem Fall beträgt die Emissionsabgabe, gestützt auf Artikel 9 Absatz 1 Buchstabe d StG, drei Franken je Titel.»
- «Als entgeltlich erweist sich die Ausgabe von Sanierungsgenussscheinen, wenn darauf zu schliessen ist, dass die involvierten Parteien, das heisst Gläubiger und Schuldner, den Forderungsverzicht und die Emission der Genussscheine als Einheit betrachten. Darauf ist insbesondere zu schliessen, wenn die Anzahl ausgegebener Scheine sich am Umfang der geleisteten Forderungsverzichte orientiert.»
- «Liegt eine entgeltliche Ausgabe von Genussscheinen vor, muss der Gesamtbetrag der geleisteten Forderungsverzichte als Zufluss im Sinn von Artikel 8 Absatz 1 Buchstabe a StG bezeichnet werden; die Emissionsabgabe ist folglich auf diesem Betrag zu berechnen; vorbehalten bleibt der Freibetrag gemäss Artikel 6 Absatz 1 Buchstabe k StG.»
- Normstelle: Abs. 1 lit. d (Begriff «unentgeltlich»; Abgrenzung zu Art. 8 Abs. 1 lit. a).

### V.4 ESTV, Mitteilung-020-DVS-2024-d vom 18. September 2024, Checkliste für Spezialfälle (PDF vom 16. Mai 2025) – Wortlaut Vorlauf (art-7, art-8)

- PDF https://www.estv.admin.ch/dam/de/sd-web/2hqENQZfloRj/estv-mitteilung-020-dvs-checkliste-de.pdf (OCL estv_ks_estv_mitteilung_020_dvs_checkliste_de); Lexplorer-Chunk 90d43197-c66f-423c-aef2-5781a90ed51c – https://mcp-tax.lexplorer.ch/s/doc/cc089a32-3c79-4649-bb8b-801e60de6539?chunk=90d43197-c66f-423c-aef2-5781a90ed51c
- Abschnitt «Kapitalband»: «Beurteilung der KER am Ende des Kapitalbandes (Nettoprinzip) inkl. Nachweis des Betrages» – «Hinweis der Deklaration der Emissionsabgabe auf dem Nettozufluss mit Formular 3»
- Normstelle: Abs. 3 (Nettozufluss; Deklaration Formular 3).

### V.5 ESTV, Kreisschreiben Nr. 29c vom 23. Dezember 2022, «Kapitaleinlageprinzip» – Wortlaut Vorlauf (art-7)

- PDF https://www.estv.admin.ch/dam/de/sd-web/h36nmhxQYuz5/dbst-ks-2022-1-029c-dvs-de.pdf; Lexplorer https://mcp-tax.lexplorer.ch/s/doc/2822de22-4ad4-4636-9199-db732d79a79d
- Ziff. 3.1: «Soweit die Einlagen und Aufgelder, die während eines Kapitalbands nach den Artikeln 653s ff. OR geleistet werden, die Rückzahlungen von Reserven im Rahmen dieses Kapitalbands übersteigen, werden diese den KER bzw. Ausland-KER gutgeschrieben (Nettobetrachtung gemäss Artikel 20 Absatz 8 DBG bzw. Artikel 5 Absatz 1septies VStG).»
- Befund (Vorlauf, Grep): KS 29c enthält keine Aussage zur Emissionsabgabe (bestätigt durch Oesterhelt/Tschan, § 4 N 72, unten L.6). Normstelle: Abs. 3 (nur Parallele VSt/DBG).

### V.6 Verordnung über die Stempelabgaben (StV, SR 641.101), Art. 12 – Wortlaut Vorlauf (art-5/Materialien Ziff. 7, Fedlex Stand 1.9.2023)

- Abs. 1bis: «Die Genossenschaft hat die Abgabe aufgrund der Abrechnung nach amtlichem Formular innert 30 Tagen nach Geschäftsabschluss unaufgefordert der ESTV zu entrichten.» – Normstelle: Abs. 2 (Jahresabrechnung). Verordnungsrecht, keine Verwaltungspraxis; hier nur als verfahrensrechtlicher Rahmen.

### V.7 ESTV-Informationsschriften (Lexplorer-Status «Materialien»)

- «Dossier Steuerinformationen: Geltende Steuern», Juni 2026, Ziff. 2.2.3.1 – Chunk 46727844-5c39-456f-a5df-011226eb63fd – https://mcp-tax.lexplorer.ch/s/doc/aa95c20d-5592-42af-8c01-a0b0d59a7f61?chunk=46727844-5c39-456f-a5df-011226eb63fd (heute ganz gelesen): «Von der Emissionsabgabe ausgenommen sind insbesondere die Begründung oder Erhöhung von Beteiligungsrechten im Zusammenhang mit Fusionen, Umwandlungen oder Spaltungen von Kapitalgesellschaften oder Genossenschaften …» – Befund: keine Aussage zu Art. 9 (weder lit. d, lit. e, Abs. 2 noch Abs. 3); Verweis auf den Artikel «Eidgenössische Stempelabgaben» im Dossier Steuerinformationen, der in Lexplorer nicht vorhanden ist.
- «Das schweizerische Steuersystem», Juni 2025, Ziff. 8.2.3.1 – Chunk 180aff51-887b-4b4a-90a2-dc18885f0562 (Vorlauf art-8): ebenfalls ohne Art.-9-Aussage.

---

## 3. Fundstellen – ILE-Lehre

**L.1 Oesterhelt/Tschan, Verrechnungssteuer und Stempelabgaben – Fallbeispiele zu aktuellen Entwicklungen, IFF-Schriftenreihe Bd. 128, 2025, § 1 Umstrukturierungen, XV «Umstrukturierung von Stiftungen», N 217–220**
- Chunk fc8607df-0fd6-4a80-8acd-67858a35ac11 – https://app.lexplorer.ch/suche?e_chunks=29871&e_sys=ile (heute gelesen); Autor:innen: Stefan Oesterhelt, David Tschan
- Sachverhalt: «Die Stiftung X. will ihren Restaurationsbetrieb künftig über eine Betriebsgesellschaft (X. AG) führen. Die Stiftung legt ihren Betrieb daher als Sacheinlage in die X. AG ein.» (Fn. 75: «ILE 2023, Folien 68 f.»)
- «217 Die Einlage des Restaurationsbetriebs durch die Anteilsinhaberin (Stiftung X.) in die X. AG stellt einen emissionsabgabepflichtigen Zuschuss i. S. v. Art. 5 Abs. 2 lit. a StG dar.» – «218 … Da es sich bei der Stiftung nicht um eine Kapitalgesellschaft oder Genossenschaft handelt, kann der Ausnahmetatbestand gemäss Art. 6 Abs. 1 Bst. abis StG nicht angewendet werden.» – «219 Soweit die Stiftung seit mehr als fünf Jahren besteht, kann aber Art. 9 Abs. 1 lit. e StG angewendet werden. Die Emissionsabgabe ist in diesem Fall nur auf dem Nennwert geschuldet. Es ist aber eine Veräusserungssperrfrist von fünf Jahren zu beachten.» – «220 Im Umfang des eingelegten Aktivenüberschusses können bei der übernehmenden X. AG KER gebildet werden.»
- Kurzzitat: Oesterhelt/Tschan, § 1 Umstrukturierungen, N. 217 ff.
- Normstelle: Abs. 1 lit. e (Stiftung; Ausgliederung eines Betriebs; Abgrenzung lit. abis; Bestand; Sperrfrist).

**L.2 Oesterhelt/Tschan, a.a.O. (Bd. 128), § 1 Umstrukturierungen, XII.7 «Einlage einer niederländischen CV», Sachverhalt und N 190–193**
- Chunks 5f112ea9-44de-49ec-8df9-c1c8538dd860 – https://app.lexplorer.ch/suche?e_chunks=29857&e_sys=ile und 6ac1095c-3fa6-4c5d-bd2a-7d5c6dfe6cd0 – https://app.lexplorer.ch/suche?e_chunks=29858&e_sys=ile (beide heute gelesen); Autor:innen: Stefan Oesterhelt, David Tschan
- Sachverhalt: «X hält 100 % an der holländischen X. CV (Commanditaire Vennotschap; dies entspricht einer direktsteuerlich intransparenten Kommanditgesellschaft) und bringt diese im Rahmen einer Sacheinlagegründung (gegen AK/KER) in die schweizerische Y. AG ein.» (Fn. 65: «ILE 2024, Folien 53 ff.»)
- «190 Die X. CV ist zivilrechtlich als Kommanditgesellschaft (und damit als Personengesellschaft) ausgestaltet. 191 Die Anwendung des Ausnahmetatbestandes von Art. 6 Abs. 1 lit. abis StG ist auf die Umstrukturierung von Kapitalgesellschaften und Genossenschaften beschränkt. Es fehlt am für die Quasifusion erforderlichen Austausch von Beteiligungsrechten.» – «193 Hingegen kann bei einem Bestehen der X. CV von mindestens fünf Jahren der Spezialfall nach Art. 9 Abs. 1 lit. e StG geltend gemacht werden. Diesbezüglich ist eine Veräusserungssperrfrist von fünf Jahren zu berücksichtigen.»
- Kurzzitat: Oesterhelt/Tschan, § 1 Umstrukturierungen, N. 190–193.
- Normstelle: Abs. 1 lit. e (ausländische Personengesellschaft; Einbringung der Anteile; Bestand; Sperrfrist).

**L.3 Oesterhelt/Tschan, a.a.O. (Bd. 128), § 1 Umstrukturierungen, I «Emissionsabgabe bei Verletzung von Sperrfristen», N 7–10**
- Chunk 5e215081-cbe6-416e-a52c-b22ff76d4ce8 – https://app.lexplorer.ch/suche?e_chunks=29785&e_sys=ile (heute gelesen); Autor:innen: Stefan Oesterhelt, David Tschan
- «7 Art. 6 Abs. 1 lit. abis StG enthält aber weder eine Bestimmung über eine Sperrfrist noch einen Verweis auf die Sperrfrist von Art. 61 Abs. 2 DBG. Somit besteht keine gesetzliche Grundlage für die Erhebung der Emissionsabgabe bei Verletzung der Sperrfrist von Art. 61 Abs. 2 DBG.» – «8 Die ESTV hält daher in Ziff. 4.4.1.4 KS 5a seit dem 1. Februar 2022 fest, dass mit Bezug auf die Emissionsabgabe bei einer Ausgliederung keine Veräusserungssperrfrist gilt.»
- Kurzzitat: Oesterhelt/Tschan, § 1 Umstrukturierungen, N. 7 f.
- Normstelle: Abs. 1 lit. e Satz 2 (Kontrast: einzige gesetzliche Emissionsabgabe-Sperrfrist bei Umstrukturierungen).

**L.4 Oesterhelt/Tschan, a.a.O. (Bd. 128), § 1 Umstrukturierungen, VI–XI, N 134–136 (Spaltung; lit. h)** – Wortlaut Vorlauf (art-6, art-8, dort heute gelesen)
- Chunk 3b93e218-4df1-420a-a2ee-9a043212e71c – https://app.lexplorer.ch/suche?e_chunks=29746&e_sys=ile; Autor:innen: Stefan Oesterhelt, David Tschan
- «136 Dies hat aber zur Folge, dass der Freibetrag von Art. 6 Abs. 1 lit. h StG für künftige Kapitalerhöhungen nicht mehr geltend gemacht werden kann.»
- Kurzzitat: Oesterhelt/Tschan, § 1 Umstrukturierungen, N. 136.
- Normstelle: Abs. 1 lit. e i.V.m. lit. h («noch nicht beanspruchter» Freibetrag) – nur mittelbar (betrifft lit. abis).

**L.5 Oesterhelt/Tschan, St. Galler Seminar zur Unternehmensbesteuerung 2023, «Aktuelle Entwicklungen Verrechnungssteuer und Stempelabgaben», Folie «Umstrukturierung von Stiftungen: Beurteilung» (Folien 68 f. gemäss § 1 Fn. 75)**
- Chunk 57d93931-194f-41b2-a29d-dc654f364004 – https://app.lexplorer.ch/suche?e_chunks=53397&e_sys=ile (heute gelesen); Referent:innen: Stefan Oesterhelt, David Tschan
- «Soweit die Stiftung seit mehr als fünf Jahren besteht, kann Art. 9 Abs. 1 Bst. e StG angewendet werden. Die Emissionsabgabe ist in diesem Fall nur auf dem Nennwert geschuldet (Veräußerungssperrfrist von fünf Jahren)»
- Kurzzitat: Oesterhelt/Tschan, Seminar 2023, Folien 68 f.
- Normstelle: Abs. 1 lit. e (Stiftung).

**L.6 Oesterhelt/Tschan, St. Galler Seminar zur Unternehmensbesteuerung 2024, «Aktuelle Entwicklungen Verrechnungssteuer und Stempelabgaben», Folie 55 «Qualifikation als Quasifusion?»**
- Chunk 7f09b463-0004-46dd-84e9-f266d6d3810e – https://app.lexplorer.ch/suche?e_chunks=51431&e_sys=ile (heute gelesen); Referent:innen: Stefan Oesterhelt, David Tschan
- «Hingegen kann bei einem Bestehen der X. CV von mindestens fünf Jahren das Privileg von Art. 9 Abs. 1 lit. e StG (Einlage einer Personengesellschaft qualifiziert praxisgemäß als besonderer Fall) geltend gemacht werden. Somit wird die Emissionsabgabe nur auf dem Nennwert erhoben (wobei eine Veräußerungssperrfrist von fünf Jahren zu beachten ist).»
- Kurzzitat: Oesterhelt/Tschan, Seminar 2024, Folie 55.
- Normstelle: Abs. 1 lit. e (Einlage einer [ausländischen] Personengesellschaft; «praxisgemäss»).

**L.7 Aebi/Brozzo, St. Galler Seminar zur Besteuerung von personenbezogenen Unternehmen 2025, «Familien- und Unternehmensstiftungen», Folie «Lösungsvorschlag» (Buchwertübertragungen durch Familienstiftungen; Foliennummer im Chunk nicht ausgewiesen)**
- Chunk 4986046d-7b07-49d2-ab02-0ef55cee2e83 – https://app.lexplorer.ch/suche?e_chunks=49055&e_sys=ile (heute gelesen); Referent:innen: Lukas Aebi, Hanna Brozzo
- «Anwendbarkeit Art. 61 Abs. 1 lit. d DBG / Art. 24 Abs. 3 lit. d StHG auf Stiftungen? … Bezüglich Emissionsabgabe u.E. Art. 9 lit. e StG anwendbar» – «Ergo: Steuerneutrale Übertragung der Beteiligung durch Familienstiftung möglich.»
- Kurzzitat: Aebi/Brozzo, Seminar personenbezogene Unternehmen 2025, Folie «Lösungsvorschlag» (Familienstiftungen).
- Normstelle: Abs. 1 lit. e (Stiftung; Beteiligungsausgliederung; eigene Auffassung «u.E.»).

**L.8 Bieri/Risi, St. Galler Seminar zur Besteuerung von personenbezogenen Unternehmen 2025, «Vermögensverwaltung mittels Personenunternehmen und Fondsstrukturen», Folie «Einbringung L-QIF in Personal Holding» (Foliennummer im Chunk nicht ausgewiesen)**
- Chunk 951131ea-56a4-4c09-b1aa-dff1a1e5095a – https://app.lexplorer.ch/suche?e_chunks=49111&e_sys=ile (heute gelesen); Referent:innen: Daniel Bieri, Andreas Risi
- «Einbringung des L-QIF in die Hans im Glück GmbH löst die Emissionsabgabe aus (Spezialfall nach Art. 9 Abs. 1 lit. e StG prüfen!)»
- Kurzzitat: Bieri/Risi, Seminar personenbezogene Unternehmen 2025, Folie «Einbringung L-QIF in Personal Holding».
- Normstelle: Abs. 1 lit. e (KmGK als Rechtsträger? – offen).

**L.9 Schmid/Lehmann, «Privatisierung von Banken aus steuerlicher Sicht», FStR 2002 Heft 4, Ziff. 4.2.1 «Emissionsabgabe»**
- Chunk 6a593fcb-6540-43cd-95f4-33208a72f2d3 – https://app.lexplorer.ch/suche?e_chunks=2999&e_sys=ile (heute gelesen); Autor:innen: Christoph Lehmann, Peter Schmid
- «Die entscheidende Frage, nämlich ob der Ausnahmeartikel nach Art. 6 Abs. 1 lit. abis StG auch die Umwandlung einer Anstalt in eine Aktiengesellschaft erfasse, wurde vom Bundesgericht mit Urteil vom 3.10.1996 im Fall der Walliser Kantonalbank bereits abschlägig beantwortet: Eine solche Umwandlung ist emissionsabgabepflichtig.»
- «Leider übernimmt die Eidg. Steuerverwaltung diese Ansicht nicht. Trotz Fehlens einer eigentlichen Vermögensübertragung zwischen verschiedenen Rechtssubjekten ist für die Berechnung der Abgabe aus Sicht der Eidg. Steuerverwaltung auf den inneren Wert abzustellen … Für die emissionsabgaberechtliche Bewertung einer Bank wird der Unternehmenswert im Regelfall so berechnet, dass der Verkehrswert dem um einen Goodwill-Zuschlag von 10 % erhöhten, zu Verkehrswerten ermittelten Aktivenüberschuss gleichgestellt wird.»
- «Es ist zu hoffen, dass das Fusionsgesetz diese Frage lösen wird. Nach den Beschlüssen des Ständerates (21.3.2001) und der nationalrätlichen WAK (3.7.2001) soll jedenfalls das Stempelgesetz durch einen Art. 9 Abs. 1 lit. e in dem Sinne ergänzt werden, dass unter anderem bei Umwandlungen von Unternehmen des öffentlichen Rechts lediglich auf dem Nennwert abzurechnen ist (allerdings unter Vorbehalt einer fünfjährigen Sperrfrist).»
- Kurzzitat: Schmid/Lehmann, FStR 2002, Ziff. 4.2.1.
- Normstelle: Abs. 1 lit. e (Entstehung; Rechtslage vor 2004; Unternehmen des öffentlichen Rechts). Urteil (BGer 3.10.1996, Walliser Kantonalbank) nur als Hinweis aus dem Lehrtext, nicht geprüft.

**L.10 [Autor:in im Lexplorer-Chunk nicht ausgewiesen], «Steuerrechtliche Aspekte des Fusionsgesetzes», FStR 2001 Heft 1, Ziff. 6.1 «Emissionsabgabe»**
- Chunk 5096d7b4-fd78-40b7-abc9-5238389d6e5e – https://app.lexplorer.ch/suche?e_chunks=1717&e_sys=ile (heute gelesen; Autorenzeile fehlt im Chunk, auch Dokumentanfang/-ende ohne Angabe – vor Zitierung am Original ergänzen)
- «Die Arbeitsgruppe Steuern bei Umstrukturierungen hat bei den bis anhin nicht privilegierten Umstrukturierungen von Personengesellschaften, Vereinen, Stiftungen und Unternehmen des öffentlichen Rechts vorgeschlagen, die Emissionsabgabe nicht auf dem Verkehrswert, sondern lediglich auf dem Nennwert der bei der Umstrukturierung neu geschaffenen Beteiligungsrechte zu erheben. Der Bundesrat ist diesem Kompromissvorschlag nicht gefolgt, weil er zum einen grössere Steuerausfälle zur Folge hätte und sich zum andern nicht mit dem Postulat vereinbaren liesse, wonach Umstrukturierungen bei der Emissionsabgabe nur begünstigt werden sollten, wenn die betreffenden Unternehmen die Abgabe bereits entrichtet haben. Auch wäre die vorgeschlagene Entlastung unter dem Aspekt der Rechtsgleichheit problematisch, weil sie zu einer Privilegierung der im Zug der Privatisierung öffentlicher Anstalten neu gegründeten Kapitalgesellschaften führen würde. Schliesslich wird hinsichtlich der Umwandlung von Personenunternehmen in Kapitalgesellschaften auf die kürzlich statuierte Freigrenze von 250'000 Franken hingewiesen.» (Fn. 127: Botschaft zum FusG, 4379)
- Normstelle: Abs. 1 lit. e (Entstehung; Bundesrat gegen, Parlament für die Nennwertlösung).

**L.11 Oesterhelt/Tschan, a.a.O. (Bd. 128), § 4 KER, Abschn. 4 «Nettobetrachtung bei Emissionsabgabe», N 68–72, und Abschn. 5**
- Chunks ee9997e0-fa60-404e-8b62-aabf8f572df9 – https://app.lexplorer.ch/suche?e_chunks=30315&e_sys=ile und d2c70ea0-6945-4a9b-aedc-3ddf7ef4a91a – https://app.lexplorer.ch/suche?e_chunks=30317&e_sys=ile (beide heute gelesen); Autor:innen: Stefan Oesterhelt, David Tschan (am Chunk-Ende verifiziert)
- «68 Zuflüsse im Rahmen eines Kapitalbands unterliegen gemäss Art. 5 Abs. 1 lit. a StG der Emissionsabgabe. Art. 9 Abs. 3 StG in der seit 1. Januar 2023 geltenden Fassung hält fest, dass auf den Beträgen, die einer Gesellschaft im Rahmen eines Kapitalbands nach Art. 653s ff. OR zufliessen, die Emissionsabgabe nur soweit erhoben wird, als diese Zuflüsse die Rückzahlungen im Rahmen dieses Kapitalbands übersteigen. Mit anderen Worten gilt das Nettoprinzip gemäss Art. 9 Abs. 3 StG auch für die Emissionsabgabe.»
- «69 Mit Bezug auf die Emissionsabgabe spielt es keine Rolle, ob die Rückzahlungen im Rahmen des Kapitalbands aus übrigen Reserven über die zweite Handelslinie erfolgt sind oder nicht. Mit anderen Worten ist das Nettoprinzip mit Bezug auf Art. 9 Abs. 3 StG - im Gegensatz zu Art. 5 Abs. 1septies VStG - auch für Rückkäufe ausserhalb der zweiten Handelslinie sowie für Rückzahlungen von KER anwendbar.»
- «70 Auf den diesbezüglichen zusätzlichen KER nach Ziff. 3.1 KS 29c ist keine Emissionsabgabe geschuldet, d. h. die Modifizierungen des Nettoprinzips für die Bildung von zusätzlichen KER haben keine Auswirkung auf die Emissionsabgabe: hier bleibt es bei der strengen Nettobetrachtung.»
- «71 … Diese Bestimmung [Art. 7 Abs. 1 lit. f StG] ist eine direkte Folge des in Art. 9 Abs. 3 StG enthaltenen Nettoprinzips, da die Höhe der Emissionsabgabe erst am Ende des Kapitalbands feststeht.» – «72 Das KS 29c der ESTV enthält in Bezug auf die Emissionsabgabefolgen des Kapitalbands keine Ausführungen …»
- Fn. 23: «Dies ist ein gewisser Nachteil des Kapitalbands, da z. B. Einlagen im Jahr 1 des Kapitalbands erst am Ende des Kapitalbands im Jahr 5 … als KER zurückbezahlt werden können. … Dies ist kommerziell gegen die Emissionsabgabe-Ersparnis aufgrund des Kapitalbands abzuwägen.»
- Abschn. 5: «Im konkreten Fall kommt es zu Einlagen in Höhe von CHF 600 Mio. und zu Rückzahlungen von CHF 500 Mio. … Die Emissionsabgabe ist nach dem strengen Nettoprinzip auf CHF 100 Mio. zu entrichten.»
- Kurzzitat: Oesterhelt/Tschan, § 4 KER, N. 68–72.
- Normstelle: Abs. 3.

**L.12 Oesterhelt/Tschan, St. Galler Seminar zur Unternehmensbesteuerung 2025, «Aktuelle Entwicklungen Verrechnungssteuer und Stempelabgaben», Folie 70 («Kapitalband und Zuschüsse bei der X. AG»)**
- Chunk e6455063-0ff2-4413-a6fc-4fc87729cd07 – https://app.lexplorer.ch/suche?e_chunks=48393&e_sys=ile (heute gelesen); Referent:innen: Stefan Oesterhelt, David Tschan
- «Gemäss Art. 653v OR führt der Beschluss der Generalversammlung zur Kapitalerhöhung oder –herabsetzung während der Dauer eines Kapitalbandes zu dessen Beendigung. Im Gegensatz hat ein allfälliger Beschluss eines Zuschusses während der Dauer eines Kapitalbandes keinen Einfluss und führt daher nicht zu dessen Beendigung. Der Zuschuss von CHF 30 Mio. unterliegt daher nach Art. 7 Abs. 1 Bst. e StG im Zeitpunkt des Zuschusses der Emissionsabgabe; die KER können analog dazu umgehend (nach Vorliegen der entsprechenden Jahresrechnung) bestätigt werden. Die Nettobetrachtung nach Art. 7 Abs. 1 Bst. f StG sowie nach Art. 5 Abs. 1septies VStG kommt nicht zur Anwendung.»
- Kurzzitat: Oesterhelt/Tschan, Seminar 2025, Folie 70.
- Normstelle: Abs. 3 (sachlicher Umfang: Zuschüsse ausserhalb der Nettobetrachtung).

**L.13 Oesterhelt/Tschan, St. Galler Seminar zur Unternehmensbesteuerung 2022, Folie 10 (Nettobetrachtung bei der Emissionsabgabe)** – Wortlaut Vorlauf (art-8, dort heute gelesen)
- Chunk b8ff96f0-7052-4626-ad97-b91daef2efdc – https://app.lexplorer.ch/suche?e_chunks=54972&e_sys=ile; Referent:innen: Stefan Oesterhelt, David Tschan
- «Eigenkapital zu Beginn des Kapitalbandes: 300'000 / Eigenkapital am Ende des Kapitalbandes: 305'000 / Nettozunahme: 5'000 (bei der Emissionsabgabe erfolgt die Beurteilung unabhängig der Börsenkotierung)»
- Kurzzitat: Oesterhelt/Tschan, Seminar 2022, Folie 10.
- Normstelle: Abs. 3 (Berechnungsbeispiel).

**L.14 Oesterhelt/Tschan, St. Galler Seminar zur Unternehmensbesteuerung 2025, Folie 74 (direkte Umwandlung übriger juristischer Personen)** – Vorlauf (art-8)
- Chunk 600d0652-ba7a-4de9-94ae-07e71b77e9e8 – https://app.lexplorer.ch/suche?e_chunks=48395&e_sys=ile: nur KER («Gemäss Ziffer 4.2.4.4 KS 5a sowie Ziffer 6.3.3 KS 29c können bei einer direkten Umwandlung von übrigen jur[istischen Personen] …»), keine Emissionsabgabe-Aussage; nicht verwendet.

**Gelesen, ohne Art.-9-Aussage (nicht verwendet):** Oesterhelt/Schreiber, «Das neue Kreisschreiben betreffend Umstrukturierungen», FStR 2022/1, Ziff. 6.2 (Chunk 5cc3fb8e, e_chunks=11363; nur Einkommenssteuer bei Umwandlung von Vereinen/Stiftungen) und 6.3 (Chunk 46a60a65, e_chunks=11365; nur Art. 61a DBG/KER); Inhaltsverzeichnis (Chunk 373167a3) ohne eigenen Abschnitt zu Art. 9 StG. Hinny, FStR 2001/4, Ziff. 4 (Chunk 197d1753, e_chunks=2308; Merkblatt ESTV vom 23.5.2001 zu lit. abis, keine Aussage zu Art. 9). Oesterhelt/Tschan, Seminar 2023 (Chunk 350af3fe, e_chunks=53405; Kauf AG, Art. 5 Abs. 1 lit. a, kein lit. e). Oesterhelt/Tschan, § 7 Emissionsabgabe (Bd. 128): Kapitel I–V (Aktienliberierung/Ausgliederung, Kauf durch Muttergesellschaft, Compensatory Capital Increase, Grossmutterzuschuss, teilweise steuerneutrale Umstrukturierungen) – keine Stelle zu Genussscheinen, Genossenschaften, Kapitalband oder Art. 9 Abs. 1 lit. e.

---

## 4. Zählerstand

- Lexplorer-Suchen: **13 von 15** (search_chunks_hybrid 8, search_chunks_keyword 5; davon Kategorie 08-ILE 10, Kategorie 02-Verwaltungspraxis 3).
- Open Case Law: 4 × search_practice, 2 × get_practice.
- Lesezugriffe Lexplorer (get_chunk_content, nav_list_chunks, nav_list_documents, get_document_slice): ca. 25, nicht gezählt.
