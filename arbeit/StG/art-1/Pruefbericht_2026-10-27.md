# Prüfbericht Art. 1 StG – 27.10.2026 (Claude-Cloud, unbeaufsichtigter Lauf)

## Entscheide im unbeaufsichtigten Lauf
- Reserviert: StG/art-1 (reservierung.py). Kein stand.py, keine Word-Fassung (Vorgabe).
- Register und Problemkarte selbst erstellt (keine Karteikarten). Cache: 35 Entscheide, davon 20 einschlägig (16 Einträge nach Zusammenführung BGE/BGer), 15 Fehltreffer (kantonale «StG»/«LT»). Gegenprobe Open Case Law: 1 Nachtrag (2C_976/2014, C). Register: 17 Einträge (A 8, B 8, C 1) plus 3 gelesene BVGer-Entscheide.
- Kantonale Gerichte: Entscheidsuche ohne einschlägigen Treffer; der Text erwähnt das nicht eigens (keine kantonale Sachfrage).
- Übersicht ohne «Harmonisierung», stattdessen «Verhältnis zu anderen Erlassen» (kantonale Abgaben/Art. 134 BV; MWST; Liechtenstein), gemäss Aufgabe und Skill.
- Botschaft 1972 und Bericht/Stellungnahme 1991: Scans bei amtsdruckschriften.bar.admin.ch nicht erreichbar (Verbindung zurückgesetzt). Botschaft 1972 nur nach OCR-Snippets (search_botschaft) und nach Seitenangaben des Bundesgerichts zitiert (S. 1289, 1297, 1307); 1991 nach Ziffern statt Seiten.
- AS-Fundstelle StG 1917: «AS 1918 59» übernommen aus BGE 149 II 462, E. 2.2.1; Prüfagent schlug «AS 34 59; BS 6 101» vor (aus BBl 1949 OCR bzw. Fedlex Art. 53 StG). Beibehalten, weil vom Bundesgericht so zitiert; für die Nachführung vermerkt.
- Inkrafttreten StG 1973: BGE 149 II 462 (StG 1917 «bis zum 1. Januar 1975») und BGE 151 II 545 (StG 1973 «entrée en vigueur le 1er juillet 1974») widersprechen sich; der Text nennt deshalb kein Datum, nur AS 1974 11.
- Normtext: Fedlex führt für Art. 1 keine eigene Sachüberschrift (Gliederungstitel «I. Gegenstand des Gesetzes»); Normtext-Kopf daher «Art. 1», Titel im Kopf der Datei.
- Ausblick: Schicksal von Entwurf 2 der pa.Iv. 09.503 nach 2021 in den zugelassenen Quellen nicht festgestellt; Text auf Belegtes beschränkt und mit Fedlex-Stand (Art. 1 seit 2020 unverändert) abgeschlossen.
- Lexplorer-Suchen: 10 von 25 (alle ILE-Literatur); Verwaltungspraxis navigiert (KS 33) bzw. über Open Case Law (KS 12).

## Fundstellenprüfung (Schritt 8, zwei Hilfsagenten, vollständig)
- Teil 1 (Entscheide, 35 Fussnoten): alle Zitierstrings bestätigt. Behoben: Seitenangabe Botschaft 1972 (FF statt BBl) → BBl S. 1297 über 2C_638/2020; 2C_488/2017 abgeschwächt («spricht dafür») und auf lit. b beschränkt; BGE 151 II 545: Entgeltlichkeit E. 9.3–9.5 als Hauptbegründung, Umsatzbegriff als Bestätigung, E. 10.1.1–10.3; 2C_579/2009 als Rechtslage vor 1.3.2012 formuliert; Liechtenstein-Satz geteilt (ZAV/KS 33 bzw. BVGer); Rechtsverkehrssteuer-Randnote nach Fundstellen getrennt; Barprämie-Definition der ESTV-Praxis zugeordnet; 2A.569/2003 E. 2.4 f.; 2C_381/2009 auf Umsatzabgabe beschränkt.
- Teil 2 (Materialien, Erlasse, Praxis, Lehre): Normtext bestätigt. Behoben: Bericht 1991 (Kommission des Nationalrates, Ziff. 3 für die parlamentarische Initiative; Kurzzitat «Bericht Kommission NR 1991»); Signal gl.M. Athanas/Bürgy auf die Einordnung als Rechtsverkehrssteuer beschränkt; Oesterhelt/Tschan N. 44 zum Grundsatz verschoben; Seiten BBl 2020 8721 (S. 8753 f.) und BBl 2020 9427 (S. 9434 f., 9438); Erstnennung KAG und FINIG mit SR; KS 33 Ziff. 1.2 und 1.4; Art. 3 StG gegenüber Art. 134 BV präzisiert. Nicht prüfbar: ESTV-URL KS 33 (Werkzeuge).

## Schlussprüfung (Schritt 9)
- Neutralität: keine eigene Wertung; pipeline/kommentar.py: 22 Randnoten, 58 Fussnoten, 0 Befunde.
- Kürzung: zwei unbelegte bzw. den Wortlaut wiederholende Sätze gestrichen (Umsatzabgabe «ohne Rücksicht auf Inländer/Ausländer»; Abs. 2 «erweitert den Kreis nicht»); Satz zu Geldmarktpapieren (Art. 14 StG) gestrichen.
- Aufbau: Überschriften lit. a–c mit 2–3 Randnoten folgen dem Wortlaut (Gliederungsnotiz).
- Offen ausgewiesen: Token (keine höchstrichterliche Rechtsprechung); Zulässigkeit der ESTV-Befreiung des Brandschutzanteils (vom BGer offengelassen); BVGer A-5128/2024 als angefochten gekennzeichnet.
- md2site.py --pruefen: zurückgehalten nur wegen Status «in_arbeit» (setzt das Steuerskript beim Freigeben).
