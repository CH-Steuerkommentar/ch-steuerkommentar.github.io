# Prüfbericht Art. 17 DBG (28.10.2026)

Unbeaufsichtigter Lauf (Claude-Cloud, geplante Aufgabe). Ergebnis: 55 Randnoten, 188 Fussnoten; `pipeline/kommentar.py` ohne Befund. `md2site.py --pruefen`: Artikel nur wegen Status «in_arbeit» zurückgehalten (Freigabe setzt «geprueft»).

## Entscheide dieses Laufs (ohne Rückfrage)

- Keine Karteikarten; Register und Problemkarte selbst erstellt. Cache `pipeline/entscheide.py DBG/art-17`: 139 Entscheide (405 Kandidaten); Triage durch drei Hilfsagenten nach Zeitraum; Gegenprobe über Open Case Law (`find_leading_cases` DBG/LIFD 17, Volltextsuchen) und Entscheidsuche: 8 Nachträge (u.a. BGer 2C_974/2019, 2C_292/2007, 9C_216/2023). Zusätzlich zitiert: BGer 2C_1057/2018 (über `cite`/`get_erwaegung`), BGE 121 I 259, BGer 2C_879/2021, BGer 2C_989/2019 (Zitierstrings aus `citation_string_de` bzw. `zitat_de`). Register: 147 Zeilen (A 44, B 23, C 79; Parallelfassungen doppelt).
- Onlinekommentar.ch: Zu Art. 17 DBG und zu den verwandten Normen (Art. 16, 17a–17d, 23, 38 DBG; Art. 7, 7c–7f, 11 StHG) besteht keine OK-Kommentierung (`onlinekommentar.py liste`); keine OK-Fundstelle.
- Lehre nur ILE-Literatur (Lexplorer Tax, Kategorie 08); Lehrbuch Hongler/Lorenz übergangen. Seminarunterlagen als solche bezeichnet.
- Abs. 1bis: Die Botschaft BBl 2011 2607 enthält keine Erläuterung; die parlamentarische Herkunft wurde nicht weiter belegt (kein Zugang zum Amtlichen Bulletin über die zugelassenen Werkzeuge) und im Text nicht behauptet. BGer 2C_879/2021 (SNF-Stipendium) äussert sich nicht zu Abs. 1bis; der Text weist Abs. 1bis als höchstrichterlich nicht behandelt aus.
- Ausblick entfällt: Art. 17 DBG ist in den Fedlex-Fassungen 1.1.2027 und 1.1.2029 unverändert; eine Änderung durch die Individualbesteuerung wurde nicht gefunden.
- Datumsform der BGer-Zitate nach `citation_string_de` («vom 7. April 2020»), kantonale Entscheide numerisch (wie Art. 16 DBG).
- Mitarbeiterbeteiligungen: nur Rechtslage bis 2012 und Abgrenzung; Einzelheiten zu Art. 17a–17d DBG.
- Lohn vs. verdeckte Gewinnausschüttung nur als Hinweis (Art. 20/58 DBG).

## Lexplorer

12 Suchen (search_chunks_hybrid, ILE-Literatur; davon 1 Vorabsuche im Hauptlauf), 0 Suchen für Verwaltungspraxis (navigiert). Lexplorer nicht für Rechtsprechung verwendet. Keine Websuche.

## Fundstellenprüfung (Schritt 8)

Vier Hilfsagenten, alle 186 Fussnoten der ersten Fassung einzeln (Fundstellenliste_2026-10-28.md): 136 bestätigt, 50 korrigiert, 0 nicht belegbar. Alle Korrekturen eingearbeitet, u.a.: E.-Nummern (2C_929/2019, 2C_331/2017, 9C_237/2023, 2C_316/2020, BGE 149 II 454, 2C_809/2013, 2C_319/2012), Sachverhalte (2C_353/2022, 2A.706/2004, 9C_463/2025, 9C_421/2025, 2C_731/2017, 2C_616/2016), Vorinstanzen als solche bezeichnet (VGer ZH SB.2021.00079, SB.2014.00021, StRG ZH DB.2011.208, TC VD FI.2022.0012), VGer ZG A 2019 5 gestrichen (durch BGer 2C_316/2020 teilweise aufgehoben), sinnverkehrte Wiedergabe TC VD FI.2022.0067 consid. 6c berichtigt, obiter dictum in 2C_316/2020 gekennzeichnet, KS-1-Kriterien als nicht buchstabengetreu anzuwendende Weisung, Zuschreibungen an Lehre/Seminarunterlagen präzisiert. Nach der Prüfung eingefügte Fussnoten (2C_879/2021, 2C_989/2019, BPG) an Cache bzw. `cite` geprüft. Alle BGE/BGer-Zitierstrings per Skript gegen `zitat_de` bzw. `citation_string_de` geprüft.

Hinweise für die Recherchenotizen: Kantonale_Entscheide.md gibt TC VD FI.2022.0067 consid. 6c ungenau wieder und vermerkt zu VGer ZH SB.2014.00021 «nicht eingetreten» (richtig: BGer 2C_592/2014 abgewiesen, soweit eingetreten); VGer SZ II 2019 61 ist durch BGer 2C_989/2019 bestätigt.

## Schlussprüfung (Schritt 9)

Hilfsagent nach den Prüfpunkten von `pruefung` (54 Befunde). Eingearbeitet: Erstnennungen (BPG, Berufskostenverordnung; MBV-Abkürzung entfernt), Auflösung «ILE-HSG», Kurzzitate mit Titel (Meister, von Streng/Vuilleumier), Reihenfolge der Belege (BGE vor BGer, chronologisch, kantonal, Praxis, Lehre), Kasuistikliste chronologisch, eigene Gesamtwertung «überwiegend restriktiv» und eigene Feststellung zum Zufluss gestrichen, Hinweis auf die Verwaltungszugehörigkeit von Gammeter in die Fussnote, Widerspruch «objektive Kriterien / Parteiabsicht» aufgelöst, Doppelschilderung 2C_538/2009 durch Querverweis ersetzt, Rentensatz-Satz zu N. «Kapitalabfindung für wiederkehrende Leistungen» verschoben, Berner Praxis zur Abgrenzung in N. «Unselbständige Erwerbstätigkeit», Grammatik (Cour de justice, Mitarbeiterbeteiligungen, KS 42 Ziff. 4.5), Gesetzesbegriff «anderer geldwerter Vorteil», Titel im Kopf vereinheitlicht. Nicht übernommen: KS 4 ohne Link (keine bestätigte URL). Neutralitätsdurchgang: `kommentar.py` ohne Treffer.

## Offene Punkte für eine spätere Nachführung

- Parlamentarische Materialien zu Abs. 1bis (Geschäft 11.023).
- Wortlaut AS 1991 1184 und Seiten der Botschaft 1983 am Scan (nur OCR geprüft).
- Individualbesteuerung und künftige Fassung von Art. 38 Abs. 2 DBG (Verweisnorm von Abs. 2).
