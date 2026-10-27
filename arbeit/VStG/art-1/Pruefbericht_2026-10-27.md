# Prüfbericht Art. 1 VStG – 27.10.2026 (Claude-Cloud, unbeaufsichtigter Lauf)

## Entscheide im unbeaufsichtigten Lauf
- Reserviert: VStG/art-1 (reservierung.py); der vorangehende Lauf vom 27.10. war wegen Nutzungslimit abgebrochen, Arbeitsstand lag nicht vor, Neubeginn. Kein stand.py, keine Word-Fassung (Vorgabe).
- Register und Problemkarte selbst erstellt. Cache: 59 Entscheide, davon 50 einschlägig (48 Einträge), 9 Fehltreffer (LIA = Tessiner Handwerksgesetz, LIP = Genfer Schulgesetz, ErgStG). Nachträge: BGE 125 II 348, BGE 136 II 525, BGE 141 II 447, BGer 9C_317/2024. Klassen A 15, B 8, C 29.
- Art. 1 VStG wird vom Bundesgericht fast nur als Einstiegsformel zitiert; die Gliederung folgt daher dem Wortlaut (Abs. 1: Zweck, Steuerobjekte, Meldung; Abs. 2: Zweiphasigkeit/Rückerstattung, Bund oder Kanton).
- Übersicht ohne «Harmonisierung», stattdessen «Verhältnis zu den direkten Steuern» und «Verhältnis zu den Doppelbesteuerungsabkommen» (Aufgabe und Skill).
- Onlinekommentar.ch: keine OK-Kommentierung zum VStG und keine verwandte Norm vorhanden (`onlinekommentar.py liste`: nur DBG 10, 11, 174; StHG 13, 14, 14a, Vorb. 13–14a); keine OK-Fundstelle.
- Botschaft VStG 1963 nur als OCR-Fassung (search_botschaft); BBl-Seiten aus PDF-Seite + 952 abgeleitet und an zwei Zitaten in BGE 113 Ib 128 (S. 955, 978) geeicht; im Text als «OCR-Fassung» gekennzeichnet.
- Kantonale Gerichte (Entscheidsuche): einziger Entscheid mit Aussage zur Norm KGer VD FI.2025.0036 (Abs. 2, Rückleistung); übrige nur Einstiegsformel.
- ILE-Literatur: WP 20 (2024) nicht verwendet (Autorenangabe im Chunk fehlt). Lehrbuch Hongler/Lorenz übergangen.
- Lexplorer-Suchen: 9 von 25.

## Fundstellenprüfung (Schritt 8, zwei Hilfsagenten, alle 63 Fussnoten)
- Teil 1 (FN 1–31): 4 Korrekturen umgesetzt – Botschaft S. 954 und 957 (statt 954 f.); 2C_85/2015 E. 2.2–2.4 und Deklarationspflicht nach BGer und ESTV; Halbsatz «daher rührt der Name der Steuer» ersetzt; Scherrer-Wiedergabe präzisiert und als Rezension gekennzeichnet. Präzisierungen: NFA Ziff. II 12; BGE 113 Ib 128 E. 2d zu «Bund, Kantone und Gemeinden»; Botschafts-Bezug BGE 113 Ib 128 zugeordnet (nicht BGE 125 II 348).
- Teil 2 (FN 32–63, Verzeichnisse, Normtext): 5 Korrekturen umgesetzt – FN zu Art. 4 (2C_597/2016 nur lit. b); 2C_470/2018 zur Steuerumgehung verschoben; 2C_85/2015 mit «vgl. auch»; Zuständigkeit Art. 30 neu mit 2C_1030/2013 E. 2.3 (2C_699/2009 mit «vgl.»); 2C_42/2014 E. 3.1 statt E. 2. Risi im Text namentlich genannt; Heftnummern FStR ergänzt; Art. 20a VStG mit BG vom 28.9.2018 (AS 2019 433). Normtext bestätigt. ESTV-Links nicht prüfbar.
- Ergebnislisten: Fundstellenliste_Teil1.md, Fundstellenliste_Teil2.md.

## Schlussprüfung (Schritt 9)
- Neutralität: keine eigene Wertung; Lehrmeinungen in indirekter Rede (Scherrer, Teuscher, Risi, Oesterhelt/Opel). pipeline/kommentar.py: 22 Randnoten, 63 Fussnoten, 0 Befunde.
- Offen ausgewiesen: keine Rechtsprechung zur Fassung von Abs. 1 seit 2019; Verhältnis Sicherungs-/Fiskalzweck in der Lehre.
- md2site.py --pruefen: zurückgehalten nur wegen Status «in_arbeit» (setzt das Steuerskript beim Freigeben).
