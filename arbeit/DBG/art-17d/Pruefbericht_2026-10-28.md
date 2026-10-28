# Prüfbericht Art. 17d DBG (unbeaufsichtigter Lauf, Claude-Cloud, 28.10.2026)

## Entscheide dieses Laufs (ohne Rückfrage)
- Keine Karteikarten; Register, Problemkarte und Gliederungsnotiz selbst erstellt (01_Recherche/).
- Entscheid-Cache (`pipeline/entscheide.py`): nur 9C_86/2021. Die Phrasensuche hatte 9C_13/2025 (französisch «art. 17d LIFD») nicht erfasst; nachgetragen mit `--nachtragen 9C_13/2025 2C_397/2015 2C_285/2019`. Register: A = 1 (9C_13/2025), B = 2, C = 1; kein BGE.
- Kantonale Gerichte über Entscheidsuche (Hilfsagent, 15 Suchen): 6 einschlägige Entscheide. Das Urteil der Cour de justice GE ATA/1365/2024 ist in Entscheidsuche nicht indexiert; sein Inhalt wird nur nach der Wiedergabe in BGer 9C_13/2025 dargestellt.
- Onlinekommentar.ch: keine Kommentierung zu Art. 17a–17d DBG, Art. 7c–7f StHG oder Art. 97a DBG (Liste: DBG 10, 11, 174; StHG 13, 14, 14a, Vorb. 13–14a); keine verwandte Norm; OK nicht zitiert.
- Lexplorer Tax: Lese- und Navigationsaufrufe am 28.10.2026 wegen der Tageslimite (2000 Aufrufe, Fair Use) gesperrt. Daher nur ILE- und Praxisstellen verwendet, die in der Vorarbeit zu Art. 17a–17c DBG (gleicher Tag) ganz gelesen und wörtlich festgehalten wurden (Oesterhelt/Gammeter Ziff. 11.6, Oesterhelt/Truffer Folie «Interkantonale Aspekte», Peyer/Schreiber/Walt; KS 37 Anhang II und IV; ZStB 100.1 und 17a.1; ACI VD 21565). Neue Suchtreffer (Stocker/Brozzo 2024, FStR 2025 Exemple 2, Allemann/Bloch-Riemer 2021 Folien zum Schuldner) nicht gelesen und nicht verwendet; Leseliste in 01_Recherche/ILE_und_Praxis.md Ziff. 4 für eine Nachführung.
- Gestrichen, weil heute nicht am Original prüfbar: Hinweis auf die Merkblätter SZ und TG (nur für gesperrte Optionen formuliert); Satz zur redaktionellen Änderung gegenüber Art. 17d E-DBG (BBl 2005 603).
- Botschaft: Seitenmarken der Textfassung stehen am Seitenende (Prüfagent mit search_botschaft für S. 594 und 597 bestätigt).
- Künftige Fassungen: Art. 17d und 97a DBG am 1.1.2029 unverändert (Fedlex); kein Ausblick-Kapitel.
- Gliederung nach Tatbestandsmerkmalen (Norm ohne Absätze), dann Rechtsfolge (mit Art. 97a DBG), Abgrenzungsfragen (DBA, AHV), Verfahren. Muster: OK-Grieder/Hongler, Art. 11 DBG; Kommentierung Art. 17c DBG.
- Offen ausgewiesen: gesetzliche Grundlage der Ausdehnung auf Anwartschaften und unechte Beteiligungen; Ende des Vesting bei Austritt (TAPI vs. CJ GE; BGer Tatfrage); Anknüpfung der MBV an Arbeitstage statt Ansässigkeit.

## Lexplorer
- Suchen: 8 (Recherche-Agent) + 0 (Fundstellenprüfung) = 8 von 25.

## Fundstellenprüfung (Schritt 8)
- Zwei Hilfsagenten, alle 70 Fussnoten der ersten Fassung und die Verzeichnisse einzeln geprüft (Fundstellenliste_2026-10-28.md); keine «nicht belegbar».
- Korrigiert: Fn. 12 (Bedingung KS 37 Ziff. 10), 21 (consid. 12 und 16; Gleichbehandlung nicht streitig), 27 (Drittstaattage je nach Quellensteuerart), 28 (KS Ziff. 2.4, 7.3.2.1), 32 («aufhielt»; Anhang II nur vgl.), 34 und 68 (9C_86/2021 prüfte Aufteilung nicht, E. 5.3; Wegzug während der Vestingperiode), 37 (Rüge «Verletzung» des KS), 38 (Begründung der CJ GE ergänzt, E. 5), 44/45 (Drittstaattage nur ohne Ansässigkeitswechsel; TAPI gibt KS nur wieder), 46, 47 («Verfügungssperre»), 52, 53, 58, 64, 65 (VGer bestätigte Ausscheidung des Rekursgerichts).
- Textbefunde behoben: Sachverhalt N. austritt (Optionen im September 2020 realisiert) mit Beleg; Harmonisierung «bis auf den Verweis»; N. rsu letzter Satz belegt; N. ohne-wechsel an KS 37 Ziff. 7.1 gebunden; N. quellensteuer auf gesperrte Optionen präzisiert; «Leitfall» ersetzt; Überschrift «Bemessung» ohne Progressionsvorbehalt; Schlusssatz N. austritt-offen ohne Wertung.
- Nicht übernommen: Angleichung des Kurzzitats Oesterhelt/Truffer an den Seminartitel (Kurzzitat wie in den Kommentierungen zu Art. 17a–17c DBG).

## Schlussprüfung (Schritt 9)
- Ganzer Text in der Hauptsitzung gelesen (Sprache, Rang der Aussagen, Querverweise, Wiederholungen). Behoben: Doppelnennung Zürich/Waadt (N. harmonisierung); Zuständigkeit nach Art. 8 Abs. 1 und 3 MBV präzisiert (N. bescheinigung); Querverweis in N. austritt-offen umgestellt; ungenutzter Materialieneintrag E-DBG gestrichen.
- Neutralitäts-grep ohne Treffer; `pipeline/kommentar.py`: 25 Randnoten, 73 Fussnoten, 0 Befunde.
- `md2site.py --pruefen`: Artikel nur wegen Status «in_arbeit» zurückgehalten (wird mit der Freigabe «geprueft» gesetzt).
