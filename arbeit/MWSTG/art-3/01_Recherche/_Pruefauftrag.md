# Auftrag Fundstellenprüfung Art. 3 MWSTG (28.10.2026)

Du prüfst Fundstellen einer veröffentlichungsreifen Kommentierung zu Art. 3 MWSTG (Datei kommentare/MWSTG/art-3.md; nummerierte Fussnoten mit dem jeweils vorangehenden Text in arbeit/MWSTG/art-3/01_Recherche/Fussnoten_nummeriert.md). Du kennst die Entstehung nicht und prüfst unabhängig. Prüfe JEDE Fussnote deines Bereichs einzeln (keine Stichprobe): Stimmt die Fundstelle (Erwägung, Seite, Ziffer, Randziffer), und stützt sie die Aussage im Text davor? Stimmt der Zitierstring?

Werkzeuge und Regeln:
- Bundesgericht: zuerst Cache data/entscheide/*.json (Feld text, zitat_de; Dateiname z.B. ocl_bger_2C_585_2017.json, ocl_bge_141_II_182.json; mit Python/grep im Text suchen), sonst Open Case Law get_erwaegung / get_decision / cite. Zitierstrings nur aus zitat_de/citation_string_de/cite.
- BVGer: Open Case Law (get_erwaegung, search_decisions court bvger, cite). Kantonale Entscheide: Entscheidsuche (search, fetch_document). Lexplorer nie für Rechtsprechung.
- Materialien (Botschaften BBl 2008 6885, BBl 2015 2615, BBl 2021 2363; Vorentwürfe/Erläuternde Berichte 2007, 2020, 2025; AS 2009 5203, AS 2017 3575, AS 2024 438): Open Case Law search_botschaft / get_materialien, Fedlex; Hilfsablage arbeit/MWSTG/art-3/01_Recherche/Materialien.md (dort wörtliche Zitate mit Seitenzahlen; bei Zweifel an der Quelle selbst prüfen).
- ESTV-Praxis und ILE-Literatur (Frey/Honauer/Probst/Rohner, Handbuch MWSTG; Bodemann; Cagienard; Fröhlich; Robinson; Jöhri; Baumgartner; Denzler/Frey): Chunk-IDs in arbeit/MWSTG/art-3/01_Recherche/Lexplorer_Fundstellen.md; lesen mit Lexplorer Tax get_chunk_content (zählt nicht als Suche) bzw. nav_list_chunks/get_document_slice. KEINE Lexplorer-Suchen (search_*), Budget 0. Handbuch-Randziffern stehen im Chunk-Text als Zahl am Absatzanfang; prüfe die Rz.-Nummer genau.
- Gesetze/Verordnung: Fedlex (SR 641.20, 641.201, 631.0).
- Keine Websuche.

Ausgabe: Schreibe die Datei, die dir genannt wird, als Tabelle: | Fn. | Fundstelle | Ergebnis (bestätigt / korrigiert / nicht belegbar) | Hinweis (bei korrigiert: die richtige Fundstelle bzw. die nötige Textänderung; bei nicht belegbar: was fehlt) |. Am Ende Zahl je Ergebnis. Antworte zum Schluss mit einer knappen Liste NUR der Fussnoten, die korrigiert oder nicht belegbar sind, mit konkretem Korrekturvorschlag (genaue E./Seite/Rz. oder Umformulierung des Satzes).
