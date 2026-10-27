# Prüfbericht Art. 12 DBG – 27.10.2026 (Claude-Cloud, unbeaufsichtigter Lauf)

## Grundlagen und Entscheide im Lauf
- Reservierung `DBG/art-12` über `pipeline/reservierung.py` (claude-cloud). Skill `steuerkommentar-selbstaendig` (Fassung im Repository) mit den Abweichungen der Aufgabe: keine Karteikarten, keine Lehrrecherche, keine Websuche, keine Word-Fassung, kein `stand.py setze`.
- Entscheid-Cache mit `pipeline/entscheide.py DBG/art-12` geladen (20 Einträge = 18 Entscheide). Gegenprobe durch Hilfsagenten (Open Case Law, Entscheidsuche, ca. 3'650 Kandidaten im Volltext geprüft): 3 neue Entscheide (2A.780/2006, 9C_679/2009, 9C_611/2022). Register: 21 Entscheide (A 4 / B 11 / C 6).
- Kantonale Gerichte nur über Entscheidsuche (rund 35 Entscheide ausgewertet); Verwaltungspraxis über Open Case Law (ESTV-KS) und Lexplorer Tax.
- Lexplorer: 1 Suchaufruf (vom Server abgewiesen, Monatskontingent 500/500 erschöpft); alle Steuerbuch-Fundstellen über Navigation und Lesen.
- Materialien: Botschaft 1983 (nur OCR-Text, gekennzeichnet), BBl 2003 1288, BBl 2006 8795 (am PDF geprüft), BBl 2025 2033 (PDF: Art. 12 nur durch Ersatz von Ausdrücken betroffen).

## Entscheide, die Claude selbst getroffen hat
- Vorgängernorm: Art. 10 BdBSt laut Botschaft (S. 159, OCR); die Vermutung des Registeragenten (Art. 12 Abs. 1 BdBSt) nicht übernommen.
- Drei Überschriften mit weniger als drei Randnoten beibehalten (Begründung in der Gliederungsnotiz).
- Satz zur Begründung neuer eingetragener Partnerschaften gestrichen (Art. 35 PartG regelt nur die Umwandlung; Aussage nicht belegt); ersetzt durch die Umwandlung nach Art. 35 PartG.
- EGMR-Urteil in 9C_679/2009 nur mit Datum angeführt (Parteibezeichnung im Entscheid nicht verlässlich verifizierbar).
- 9C_42/2024 für E. 4 als BGE 151 II 435 zitiert (Pinpoints mit `cite` verifiziert); E. 1.2 (Legitimation) als BGer-Urteil belassen.

## Fundstellenprüfung (Hilfsagenten, Fundstellenliste_2026-10-27.md)
Drei Prüfagenten, alle 108 Fussnoten und das Materialienverzeichnis an der Quelle. Befunde: 32 zu korrigieren, 1 nicht belegt (Fn. 77). Alle umgesetzt, u.a.:
- Pinpoints: CJ GE ATA/63/2020 consid. 4e; KG GR KSK 19 4 E. 4.3; CDAP VD FI.2019.0141 consid. 3a–b, 4d–e; 2C_377/2017 E. 3.3.2; OGer ZH NQ120027 E. II.2.1; CDAP VD FI.2009.0059 consid. 3d, FI.2013.0070 consid. 3c–4a; 2C_476/2021 E. 1.2.3, 2.4 f.; 2C_117/2017 E. 5.1–5.8 und 6; 2C_838/2018 E. 3.3–3.5; StRK BE 100 18 45 / 200 18 40.
- Inhalt: 2C_838/2018 (Ergebnis richtiggestellt: Einleitung auch für die Erbschaftssteuer nicht willkürlich); 2C_117/2017 (Rechtsmissbrauch verneint, Haftung aufgehoben); Art. 579 ZGB-Satz neu gefasst (Frage nicht beantwortet); 5P.134/2002 (nicht Willkürprüfung, Frage des öffentlichen Rechts offen); 2C_1058/2018 (Sachverhalt präzisiert); 2A.275/2002 (Abschreibungsentscheid, Tod vor dem Rekurs); StG SO (Fristbeginn am Folgetag); 2C_259/2021 (Urteilsunfähigkeit «nicht festgestellt»); Art. 37b Abs. 2 DBG als gesetzliche Grundlage; Billigkeitsgründe kantonal belegt; Haftung «mit ganzem Vermögen» nur als Aussage des VGer ZH; Art. 149a SchKG als Verjährung; Datum CDAP VD FI.2018.0116 (11.10.2019); ZStB 172.1 als Praxis zu den Staats- und Gemeindesteuern; VGer LU nur zur Luzerner Erbschaftssteuer; Art. 52 AHVG als Schadenersatzpflicht; Notwendige Streitgenossenschaft (ZH, SZ, TG) zusammen mit selbständigem Handeln dargestellt; Harmonisierung: Spannung zwischen 2C_986/2017 E. 8 und Willkürprüfung neutral formuliert; StHG Art. 56 Abs. 4 f. ergänzt; Art. 13 Abs. 4 DBG ergänzt; Art. 205h Abs. 1 nDBG ergänzt.

## Schlussprüfung
- Sprache, Zitierweise, Rang der Aussagen, Querverweise in der Hauptsitzung durchgesehen; Wiederholungen (SZ-Entscheid) und eine zu weit gehende Verallgemeinerung («kantonale Gerichte … überwiegend») behoben.
- Neutralität: keine eigenen Wertungen; wertende Wendungen der Gerichte («überzeugen», «sachgerecht») nicht übernommen.
- `pipeline/kommentar.py kommentare/DBG/art-12.md`: 38 Randnoten, 108 Fussnoten, 0 Befunde.
- `pipeline/md2site.py --pruefen`: nur Zurückhaltung wegen Status «in_arbeit» (Reservierung); entfällt mit der Freigabe.
- Offen ausgewiesen: Akteneinsicht provisorischer Erben; Haftung ausschlagender Erben mit Vorempfängen; Art. 579 ZGB; Bemessung des Erbteils und Beweislast; keine Rechtsprechung zu Abs. 2 und 3.
