# Prüfbericht Art. 6 DBG – 27.10.2026

Unbeaufsichtigter Lauf (Claude-Cloud, geplante Aufgabe). Skill `steuerkommentar-selbstaendig` in der Fassung des Repositorys; Abweichungen gemäss Aufgabe (keine Karteikarten, kein `stand.py setze`, keine Word-Fassung).

## Umfang

- 40 Randnoten, 121 Fussnoten.
- Entscheidregister: 104 Cache-Entscheide (A 28, B 38, C 36, X 2; Parallelfassungen BGE/BGer einzeln gezählt) plus 4 Nachträge (2C_110/2018, 2C_646/2021, 2C_839/2009, BGE 150 II 244).
- Kantonale Gerichte (Entscheidsuche): rund 25 Entscheide ausgewertet, 17 im Text zitiert.
- Verwaltungspraxis: KS 22a ESTV, KS 1 SSK.
- Lehre: 19 Einträge im Literaturverzeichnis (ILE-Literatur: FStR, IFF-Schriftenreihe, ILE-Seminarunterlagen). Hongler/Lorenz nicht zitiert.
- Onlinekommentar.ch: keine Kommentierung zu Art. 6 DBG und zu den verwandten Normen (Art. 3, 4, 5, 7, 52 DBG; StHG-Parallelnorm existiert nicht). Die vorhandenen OK-Kommentierungen (Art. 10, 11, 174 DBG; Art. 13–14a StHG) betreffen Art. 6 DBG nicht; daher keine OK-Fundstelle.
- Lexplorer-Suchen: 16 von 25 (4 Verwaltungspraxis, 12 ILE-Literatur); in der Fundstellenprüfung keine Suchen.

## Entscheide im unbeaufsichtigten Lauf

- Gliederung nach Absätzen und Sätzen von Abs. 3 (Muster OK-Grieder/Hongler Art. 10 DBG). Überschriften «Umfang der beschränkten Steuerpflicht» und «Vorbehalt der DBA (Satz 4)» mit je 2 Randnoten unter der Schwelle von drei Randnoten belassen, weil sie einen eigenen Gesetzesbestandteil kommentieren; «Unilaterale Freistellung» und «Beweislast» in die benachbarten Abschnitte eingegliedert.
- Progressionsvorbehalt, Mindestsatz und Verlegung der Abzüge bei Ehegatten nur mit Querverweis auf die Kommentierung zu Art. 7 DBG (keine Doppelung).
- Kantonale Praxen nur, soweit sie im Volltext gelesen wurden; die von der Recherche als aufgehoben markierten Entscheide (AppGer BS VD.2022.49 vom 5.11.2023; VGer ZH SB.2014.00063; VGer BE 100.2021.115) nicht verwendet.
- SSK-Kreisschreiben im Materialienverzeichnis unter eigener Rubrik «Schweizerische Steuerkonferenz» (Hausgebrauch des Projekts: Kreisschreiben im Materialienverzeichnis).

## Fundstellenprüfung (Schritt 8)

Drei Hilfsagenten (effort high), je ein Hauptteil, ohne Kenntnis der Entstehung: Fundstellenliste_Teil1.md (112 Fundstellen: 103 bestätigt, 9 korrigiert), Teil2.md (64: 46 bestätigt, 17 korrigiert, 1 nicht belegbar), Teil3.md (76: 67 bestätigt, 9 korrigiert). Alle Befunde behoben:
- falsche Erwägungen berichtigt (u.a. 2C_436/2011 E. 2.2; 2C_465/2021 E. 3.5, 3.7, 3.9 f.; 2C_404/2017 E. 3.2.1, 3.3.3; BGE 151 II 154 E. 4.1 f., 4.4.1 f.; 2C_1154/2013 E. 3.5; 2C_111/2022 E. 4.1 f.);
- BGE 140 II 248 E. 4 existiert nicht → BGer 2C_164/2013 E. 4 (nicht publ.); Beweislast auf BGE 140 II 248 E. 3.5 gestützt statt BGE 139 II 78 E. 3.1;
- unveröffentlichte Erwägungen von 2C_585/2012 als «nicht publ. in BGE 140 II 157» gekennzeichnet;
- Aussagen enger gefasst, wo der Text über die Quelle hinausging (2P.340/2005 beiläufig; VGer ZH SB.2020.00044 hypothetisch; 2C_18/2014 E. 4.3.3; 2C_646/2021 nur DBA CH-DE; SVGer AG E. 5; Art. 190 BV in 2C_585/2012 E. 4; Brülisauer zu Art. 52 DBG und zur direkten Methode; 2A.328/2002 Rückweisung);
- nicht belegbare Fundstelle (Brülisauer/Seiler, Fall 2 Frage 2, zur Mitwirkung) gestrichen; Satz zur FZA-Begründung nach Brülisauer/Seiler gestrichen;
- Titel KS 1 SSK nach dem Original berichtigt.

## Schlussprüfung (Schritt 9)

- `python3 pipeline/kommentar.py kommentare/DBG/art-6.md`: 0 Befunde (Format und Neutralität).
- `python3 pipeline/md2site.py --pruefen`: Art. 6 nur wegen Status «in_arbeit» zurückgehalten (Status setzt die Freigabe).
- Sprache und Begriffe durchgesehen: Präzisierungen in N. «mindestens» (Mindestbemessungsgrundlage), «bundesbedienstete» (Bezug auf Art. 3 Abs. 5 DBG), «bundesbedienstete-kantone» (Höchstsatz Art. 36 DBG); Beleg 2C_604/2011 E. 3.2 für die Beschränkung auf das Erwerbseinkommen ergänzt (am Cache-Text geprüft).
- Als offen ausgewiesen: kantonaler Gestaltungsspielraum; «schweizerisches Unternehmen» bei Beteiligung an ausländischen Personengesellschaften; Vortrag nach Satz 2 für die Bemessungsgrundlage; FZA bei Gebietsfremden; Umfang nach Abs. 4.

## Hinweise für die Nachführung

- Der Lexplorer-Chunk 2aa25deb (Oesterhelt/Opel § 7 N. 33–38) existiert nicht mehr; die Prüfer lasen die Stelle über `get_document_slice`. Randnoten N. 33/34 in § 7 und N. 12 in § 6 sind im Text nicht gedruckt und erschlossen.
- Literaturverzeichnis Mauchle: Untertitel des Werks in Lexplorer nicht lesbar; Kurztitel wie in den übrigen Kommentierungen des Projekts.
