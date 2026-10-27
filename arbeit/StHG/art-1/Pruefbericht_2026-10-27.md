# Prüfbericht Art. 1 StHG – 27.10.2026

## Entscheide im unbeaufsichtigten Lauf
- Reservierung durch das Steuerskript (`reservierung.py`, claude-cloud). Kein `stand.py setze`, keine Word-Fassung, Git nur über `reservierung.py freigeben` (Vorgabe der Aufgabe).
- Entscheid-Cache: `entscheide.py StHG/art-1` → 177 Kandidaten (547 Suchtreffer). Vortriage per Mustersuche: 12 Kandidaten ohne Zitierung von Art. 1 StHG ausgeschieden; 165 Entscheide durch drei Hilfsagenten (effort medium) am Volltext triagiert, Erwägungsnummern am Volltext bestimmt. Nachtrag BGE 150 II 346 (Kognitionsformel, nicht von der Phrasensuche erfasst). Gegenprobe `find_leading_cases` (30): keine weiteren BGer/BGE.
- Kantonale Gerichte über Entscheidsuche (Phrasensuche «Art. 1 Abs. 2 StHG», «art. 1 al. 2 LHID», «Art. 1 Abs. 3 Satz 2 StHG»): VGer GR A 2016 53, VGer BE 100.2017.191, Cour de justice GE ATA/920/2014 verwendet.
- Verwaltungspraxis: Zu Art. 1 StHG fanden sich in Open Case Law und Lexplorer Tax (Keyword «Art. 1 Abs. 3 StHG») keine einschlägigen Kreisschreiben von ESTV oder SSK und keine Steuerbuchstellen; der Text enthält deshalb keine Randnote zur Praxis und keine Aussage über deren Fehlen.
- Lehre: ILE-Literatur (9 Lexplorer-Suchen von 25) und Onlinekommentar.ch (keine OK-Kommentierung zu Art. 1 StHG; verwandt: Vorb. zu Art. 13–14a, Art. 13, Art. 14 StHG von Grieder/Hongler). Hongler/Lorenz nicht zitiert.
- Botschaft 1983: Volltext nur als OCR-Snippets in Open Case Law; amtliche PDF (amtsdruckschriften.bar.admin.ch) nicht erreichbar. Seitenangaben der OCR-Indizes nicht gesichert → Zitat nach «Übersicht», «Ziff. 13» und «Erläuterungen zu Art. 1 E-StHG», ohne Seitenzahl.
- Rostetter Rz 760: Randziffer aus dem Querverweis «hiernach Rz 761» (Fn. 1295) erschlossen (Absatz vor Rz 761).

## Fundstellenprüfung (Schritt 8, zwei Hilfsagenten, alle Fundstellen)
- Fundstellenliste_Teil1.md (Fn. 1–43, 73 Fundstellen): 64 bestätigt, 8 korrigiert, 1 nicht belegbar. Erledigt: BGE 116 Ia 264 als «vgl. … (zu Art. 83 BVG)»; Satz «deklaratorisch» aus N. verfassung auf Bezug beschränkt und nach N. vorbehalt verwiesen; Botschaft-Fn. ohne Pinpoint, Ziff. 13; Rostetter Rz 760 f. bzw. 760; BGE 148 II 121 Sachverhalt (Wechsel der Fondsleitung) und E. 6.1 ergänzt, Gegensatz gestrichen, «spätere Urteile» → «ein späteres Urteil»; 2C_68/2016: Erbschaftssteuer vom BGer als indirekt bezeichnet, nur Lehrkontroverse offen; GE ATA/920/2014 E. 9 f.; BGE 123 II 588 (nicht belegbar für Gleichstellung mit Kanton) ersetzt durch BGE 141 I 235 E. 5.2, BGE 123 II 588 auf kantonalrechtliche Gemeindeautonomie (E. 1a) beschränkt; Fassung 1.1.2028 ergänzt.
- Fundstellenliste_Teil2.md (Fn. 44–91, 77 Fundstellen): 71 bestätigt, 6 korrigiert. Erledigt: N. vorbehalt umformuliert (Bezug; Art. 3/129 Abs. 2 BV nur 9C_195/2025); 2C_616/2016 → Art. 189 Abs. 1 lit. a BV; VGer GR E. 4d statt 4b für «insbesondere»; BGE 130 II 202 E. 3.2 statt 5.3; 2C_815/2021 E. 4.1 f.; 2C_827/2015 E. 2.3.2 f.; «seit August 2015»; Hinny «vgl.» statt «gl.M.».

## Schlussprüfung (Schritt 9)
- pipeline/kommentar.py: 32 Randnoten, 92 Fussnoten, 0 Befunde (Format und Neutralität); zusätzliche grep-Suche nach wertenden Wendungen ohne Treffer.
- Neutralität: Satz «Die Formel geht über den Wortlaut hinaus» (eigene Wertung) ersetzt durch Beschreibung des Unterschieds; «nicht einheitlich» ersetzt durch «zwei Ansätze»; unbelegtes «wie häufig» gestrichen; unbestimmter Bezug «da diese» präzisiert.
- Sprache: doppeltes «damit» im Ausblick bereinigt.
- md2site.py --pruefen: zurückgehalten nur wegen Status «in_arbeit» (setzt das Steuerskript bei Freigabe).
- Offen ausgewiesen: Massstab für «keine Regelung» (BGE 130 II 202 vs. 2C_458/2012); Erstreckung der Kognitionsformel auf Spielräume innerhalb bestehender Regelungen ohne Begründung; Grenze sehr hoher Vermögenssteuer-Freibeträge (BGer nicht entschieden); Rechtsnatur der Erbschaftssteuer in der Lehre.
