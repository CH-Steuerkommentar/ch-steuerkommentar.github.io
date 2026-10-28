# Prüfbericht Art. 7 StG (Entstehung der Abgabeforderung)

Lauf: Claude-Cloud, unbeaufsichtigt, 28.10.2026. Skill `steuerkommentar-selbstaendig` (Fassung im Repository) mit den Abweichungen der Aufgabenbeschreibung (keine Karteikarten, «Verhältnis zu anderen Erlassen» statt «Harmonisierung», keine Word-Fassung, kein `stand.py setze`).

## Ergebnis

- Ausgabe: `kommentare/StG/art-7.md`, 31 Randnoten, 76 Fussnoten; `pipeline/kommentar.py`: 0 Befunde. `md2site.py --pruefen`: nur wegen Reservierungsstatus «in_arbeit» zurückgehalten (wird mit der Freigabe «geprueft» aufgehoben).
- Entscheidregister: 28 Entscheide (BGer/BGE 8, BVGer 15, SRK 3, Bundesrat 2, kantonal 0) plus Nachtrag BGer 9C_232/2026 (aus der Fundstellenprüfung).
- Lehre: ILE-Literatur 2 Fundstellen (Oesterhelt/Tschan, Seminar 2025; Oesterhelt/Opel, FStR 2023, Rechtsprechung 2023/2); Onlinekommentar.ch: keine Kommentierung zum StG oder zu verwandten Normen vorhanden (`onlinekommentar.py liste`: nur DBG 10, 11, 174 und StHG 13–14a), daher 0 OK-Fundstellen.
- Lexplorer-Suchen: 11 (Budget 25), alle durch den Hilfsagenten Praxis/ILE.

## Entscheide im unbeaufsichtigten Lauf

1. **Lexplorer-Lesesperre.** Lexplorer meldete ab 07:52 UTC «Tageslimite für das Lesen und Navigieren erreicht (2000 Aufrufe)». Chunks konnten nicht gelesen werden. Entscheid: ILE-Literatur nur dort verwendet, wo ein früherer Lauf (Art. 5 StG, `arbeit/StG/art-5/01_Recherche/Lexplorer_ILE.md`) den Chunk vollständig gelesen und den Wortlaut aufgezeichnet hat; die Fundstellenprüfung hat diese Stellen gegen die Aufzeichnung bestätigt («bestätigt (Aufzeichnung)»). Neue Treffer (u.a. IFF-Schriftenreihe 2021 «La créance fiscale», IFF-SR 2025 § 4 KER zur Nettobetrachtung bei der Emissionsabgabe, Seminar 2022) wurden nicht verwendet; sie sind in `01_Recherche/Lexplorer_Fundstellen.md`, Teil B.2, für eine Nachführung vorgemerkt. Foliennummern «69 f.» bei Oesterhelt/Tschan nicht am Original nachgeprüft.
2. **Verwaltungspraxis** über Open Case Law (`get_practice`) im Volltext gelesen; Lexplorer Tax nur Trefferliste.
3. **OCR-Materialien** vor 1999 zitiert mit Zusatz «(Text nach der OCR-Fassung)», wie in den früheren StG-Kommentierungen; Seitenzahlen nach Formel Anfangsseite + Dokumentseite − 1.
4. **Begründung zu lit. f (Kapitalband)** in der Botschaft Aktienrecht 2016 nicht gefunden; der Text stützt lit. f nur auf Gesetz, Art. 9 Abs. 3 StG, ESTV-Checkliste und Lehre und verweist auf die Botschaft nur zur Nettobetrachtung bei DBG/VStG.
5. **VPB 61.64 E. 6a** (Verzugszins erst ab Mahnung nach damaligem Art. 29 StG) nicht verwendet, weil das Änderungsdatum von Art. 29 StG nicht belegt werden konnte.
6. **Querschnittskapitel «Rechtsfolgen des Entstehungszeitpunkts»** mit vier Unterüberschriften, teils unter drei Randnoten (bewusst, vier selbständige Rechtsfolgen; Gliederungsnotiz).
7. **Datumsformat im Fliesstext** numerisch belassen (wie in den bestehenden StG-Kommentierungen Art. 1–6), obwohl die Zitierrichtlinie im Fliesstext ausgeschriebene Monate vorsieht; Einheitlichkeit der StG-Reihe vorgezogen. Ebenso Form des Literaturverzeichnisses und der Kurzzitate wie bei Art. 5 StG.

## Fundstellenprüfung (Schritt 8)

Drei Hilfsagenten (Fn 1–21, 22–40, 41–69; Stand vor der Bereinigung), Listen `Fundstellenliste_2026-10-28_TeilA.md`, `_TeilB.md`, `_TeilC.md`. Keine Fundstelle «nicht belegbar». Umgesetzt:
- korrigiert: 2C_995/2011 E. 3 statt E. 2 (Ausgabe/Erneuerung; E. 2 zum anwendbaren Recht in die Folgefussnote); 2C_115/2007 E. 7.1–7.3; Eröffnung/Frist Vernehmlassung (Bericht S. 1, Fedlex-Verfahren statt S. 7); 2A.149/2006 E. 2.1 f.; VPB 61.64 E. 2d; KS 5a Ziff. 4.4.1.4; BGE 149 II 462 E. 3.4.1; Botschaft Aktienrecht 1983 S. 946 und 797 getrennt.
- Textprobleme behoben: Begründung lit. abis nach der Botschaft (Entstehung mit Erfüllung der Einlagepflicht); VPB 69.60 nur Umwandlung eines Vereins, damalige Fälligkeitsregel; Art. 9 Abs. 1 lit. e StG (1 % des Nennwerts, andere Rechtsträger als Kapitalgesellschaften und Genossenschaften); KS 37A nur Konzerngesellschaft; Botschaft 1972 «einzige Änderung» als Aussage der Botschaft; «Sachen und Rechte» (Art. 8 Abs. 3 StG); KS 32a Frist als Voraussetzung des Freibetrags; Nettobetrachtung als Zusammenhang statt «entspricht»; Satz «nicht an den wirtschaftlichen Mittelzufluss» (unbelegt) ersetzt durch BGE 115 Ib 233 E. 2 (Verkehrssteuer); A-6828/2017 «im Ergebnis teilweise aufgehoben … (ohne Aussage zu Art. 7 StG)»; BVGer-Formeln zum Erlasszeitpunkt ohne angedeutete Abweichung.
- ergänzt: Fussnoten zu Art. 6 Abs. 1 lit. ater StG (mit EMBAG-Erstnennung), Art. 12 Abs. 2bis StV, Art. 10 Abs. 1bis StV, 2C_299/2021 E. 3.2 (analoge Anwendung von Art. 53 Abs. 2 StG), KS 32a Ziff. 3.3.2 b) (Ausbuchung im Folgejahr), BGer 9C_232/2026 E. 4.1 (Handwechsel, Bemessung), Ausblick um die geplante Fälligkeit bei Zuschüssen und Handwechsel (Bericht S. 8) und Art. 11 lit. a VE.
- Nicht übernommen: Seitenzahl FStR für Oesterhelt/Opel (nicht ermittelbar wegen Lesesperre); Zusammenlegen gleichlautender Fussnoten Fn 8/9 (eine Dublette in N. entstehung entfernt).

## Schlussprüfung (Schritt 9)

Hilfsagent (Sprache, Zitierweise, Aufbau), 17 Befunde. Behoben: Erstnennung FINIG im Text, OR-Erstnennung an die erste Stelle verschoben, lit. d «Ausgabe oder Erhöhung» in der Übersicht, Querverweise statt Wiederholung (N. formell/deklaratorisch, Fälligkeit bei lit. a), mehrdeutige «lit. c»/«lit. e» präzisiert, Bezug auf Art. 120 Abs. 2 OR klargestellt, Querverweis Art. 5 StG beim Dividendenverzicht verschoben, Rang beim Handwechsel («Bundesgericht, soweit ersichtlich»), «in der Praxis» → KS 37A, unbestimmte Bezüge («solche Einlagen», «30 Tage danach»), doppelte Fussnote in N. entstehung, Wiederholung der 2A.618-Aussage in N. gegenstand durch Querverweis ersetzt.
Nicht übernommen: Datumsformat und Literaturform (siehe Entscheid 7); angeblicher Widerspruch Verrechnung/Ausbuchung (KS 32a Ziff. 3.3.2 b enthält beide Regeln: Verrechnungsbeschluss bis zur GV, Ausbuchung spätestens im Folgejahr; beide verifiziert).
Neutralitätsdurchgang: `pipeline/kommentar.py` ohne Befund; keine eigenen Wertungen.

## Für die Nachführung

- Lexplorer-Chunks aus Teil B.2 von `Lexplorer_Fundstellen.md` lesen (insbesondere IFF-SR 2021 «La créance fiscale» zu lit. a, IFF-SR 2025 § 4 N 56 ff. zur Nettobetrachtung, Seminar 2022 zu Art. 7 Abs. 1 lit. f) und einarbeiten.
- Ergebnis der Vernehmlassung 2026 und allfällige Botschaft verfolgen (lit. a/c, Fälligkeit Art. 11).
- OCR-Stellen am Scan prüfen (Materialien.md, offene Punkte).
