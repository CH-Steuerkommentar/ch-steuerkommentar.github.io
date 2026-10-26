# Prüfbericht Art. 2 DBG (26.10.2026, Claude-Cloud, unbeaufsichtigter Lauf)

## Entscheide des Laufs
- Keine Karteikarten; Register, Problemkarte und Gliederungsnotiz selbst erstellt (01_Recherche/).
- Entscheid-Cache: pipeline/entscheide.py (39 Treffer), ergänzt mit `--nachtragen` aus der Open-Case-Law-Volltextsuche; die Normenerkennung der Pipeline übersieht Ketten wie «Art. 2, Art. 104 ff. und Art. 160 DBG» (z.B. 2C_843/2016) – manuell per Regex nachgeprüft und ins Register aufgenommen.
- Lehre nicht recherchiert; Lehre nur als Aussage von BGE 142 II 182 (Vallender/Cavelti) und BGE 141 I 161 E. 3.4.2 (Meinungsstand zu Rulings). Kein Literaturverzeichnis.
- Verwaltungspraxis: Open Case Law `search_practice` (2 Suchen) ohne einschlägiges ESTV-Dokument zu Art. 2; Lexplorer Tax nicht benutzt (0 Suchen), da Art. 2 DBG keine kantonale Steuerbuchpraxis hat; ESTV-Praxis (Interventionslimite Eigenmietwert, Rundschreiben) nur, soweit Gerichte sie wiedergeben.
- Überschneidung mit der Kommentierung zu Art. 1 DBG (Kanton als Gläubiger): bewusst hier ausführlich (Art. 2 ist der Sitz der Frage), mit Querverweis.
- Muster OK-Grieder/Hongler Art. 11 DBG nicht im Volltext geladen (keine Websuche); Aufbau nach Anhang M.
- Keine Word-Fassung; kein stand.py setze (Status über reservierung.py).

## Schlussprüfung (Prüfpunkte pruefung)
- Rechtschreibung/Grammatik: Satz «die Obergerichte der Kantone Bern …» korrigiert; sonst ohne Befund.
- Zitierrichtlinie: Erstnennungen DBG, BV, StHG, BdBSt, BVV 3 mit Titel, Datum, SR; Fussnoten mit Punkt; Datumsformat; ohne Befund.
- Rang der Aussagen: BGer, kantonale Gerichte, BVGer und Praxis je kenntlich; aufgehobenes BVGer-Urteil gekennzeichnet.
- Neutralität: kommentar.py ohne Befund; eigene Schlussfolgerungen («Kanton kann nicht verzichten …», «zweistufige Aufsicht», «meist») gestrichen oder umformuliert; Überschrift «Gleichbehandlung im Unrecht» neutral ersetzt.
- Offene Fragen ausgewiesen: Folgen der Bezeichnung der Eidgenossenschaft in der Betreibung (ZH/BE vs. GE); Steuerabkommen nach 2C_603/2012; Eingriffsbefugnis der ESTV in kantonale Rulings (VGer GL offengelassen); kantonale Verfahrensfragen ohne BGer-Rechtsprechung.
- Querverweise: N. {{N:nichtigkeit}} geprüft.
- Format: kommentar.py 32 Randnoten, 69 Fussnoten, 0 Befunde; md2site --pruefen hält nur wegen Status «in_arbeit» (Reservierung) zurück.
