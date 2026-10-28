# Prüfbericht Art. 18b DBG – 28.10.2026

Unbeaufsichtigter Lauf (API). Skill steuerkommentar-selbstaendig mit den Vorgaben des Auftrags: keine Karteikarten, Register und Problemkarte selbst erstellt (Schritt 2 «Ohne Vorarbeit», Cache aus pipeline/entscheide.py); kein `stand.py setze`, kein git, keine Word-Fassung.

## Umfang
- 26 Randnoten, 75 Fussnoten.
- Entscheidregister: 22 Bundesgerichtsentscheide (A 3, B 6, C 13), davon 6 gegenüber dem Cache (14) über Open Case Law/Entscheidsuche nachgetragen; kein BGer-Entscheid zur Fassung ab 2020. 31 verwertbare kantonale Entscheide (Entscheidsuche).
- Verwaltungspraxis: KS 23 und 23a ESTV (Kern), KS 5a, 27, 39 ESTV; KS 32 SSK; BE TaxInfo, Luzerner Steuerbuch, Steuerbuch BL, § 19b StG/BS.
- Lehre: 6 ILE-Werke im Literaturverzeichnis (FStR-Gesetzgebungs-Agenda 2006/3, 2006/4, 2007/2; Kocher/Stadelmann FStR 2016; Locher FStR 2020; Fenners/Schreiber Seminar 2024). Kein ILE-Beitrag behandelt Art. 18b DBG systematisch. Onlinekommentar.ch: keine Kommentierung zu Art. 18, 18b, 20 DBG oder Art. 7/8 StHG (Liste vom 28.10.2026).
- Lexplorer-Suchen: 20 (ILE 14, Verwaltungspraxis 6; Budget 25). Lexplorer nicht für Rechtsprechung, Lehrbuch Hongler/Lorenz nicht verwendet.

## Entscheide im unbeaufsichtigten Lauf
- Kostenrahmen: Muster Grieder/Hongler nicht erneut im Volltext gelesen; Aufbau nach Art. 18a DBG dieses Werks (gleicher Skill) und Anhang M.
- Fundstellenprüfung (Schritt 8) mit einem Hilfsagenten (Modell sonnet, effort high) über alle 76 Fussnoten (105 Fundstellen), nicht stichprobenweise. Kantonale Entscheide überwiegend an den wörtlichen Auszügen in Kantonale_Entscheide.md geprüft (aus den Volltexten erhoben), im Volltext nachgelesen: VGer SG, StG SO, TC VD; KS 23a Ziff. 2.3.2 am ESTV-PDF.
- Schlussprüfung (Schritt 9) in der Hauptsitzung statt durch Hilfsagenten (Kosten).
- Lexplorer_Fundstellen.md: Abschnitt «ILE-Literatur» wurde beim parallelen Schreiben zweier Agenten überschrieben und aus ILE_Literatur.md wiederhergestellt.
- Parlamentarische Beratungen (Amtliches Bulletin UStR II, STAF) mit den verfügbaren Werkzeugen nicht zugänglich; Entstehungsgeschichte stützt sich auf Botschaften, Erlasstexte und FStR-Gesetzgebungs-Agenda.

## A. Fundstellenprüfung (Fundstellenliste_2026-10-28.md)
Ergebnis: 103 bestätigt, 2 korrigiert, 0 nicht belegbar; 1 Korrektur im Literaturverzeichnis; 10 Teildeckungen. Erledigt:
- KS 23a Ziff. 2.3.2: Abgrenzung privat/geschäftlich und Zuteilung des Finanzierungsaufwands getrennt dargestellt.
- VGer SG B 2022/202: Aufhebung des Vorinstanzentscheids auf Beschwerde des Steueramts, geldwerter Vorteil (statt «Veranlagung»).
- Bucher (Titel in Lexplorer abgeschnitten, nicht verifizierbar): Satz und Verzeichniseintrag gestrichen. Die Fussnotennummern der Fundstellenliste ab Fn. 7 liegen deshalb um eins höher als in der Endfassung.
- StRG ZH DB.2024.79: als beiläufige Erwägung gekennzeichnet.
- TAPI GE A/132/2025: «damals auf 50 Prozent».
- 9C_454/2023: Begründung (Rechtskraft nur des Dispositivs) ergänzt; 9C_54/2025 vorangestellt.
- 9C_526/2013 als «vgl. auch … (Nichteintreten)».
- 2C_750/2013, 9E_1/2023: «zu Beteiligungen im Privatvermögen».
- Gegenstand: «ergänzt Art. 18 DBG» gestrichen; Ansässigkeit aus dem Wortlaut, KS 27 (ausländische Personengesellschaften) und Kocher/Stadelmann (Einzelstimme) getrennt.
- KS 32 SSK: «voraussichtlich zulässig» (Original: «dürfte»).
- Veräusserungsgewinne: Art. 16 Abs. 3 DBG für den Gegensatz zum Privatvermögen.
- Fenners/Schreiber: «ausländische Personengesellschaften».

## B. Schlussprüfung (Schritt 9)
- 2C_787/2012: Erwägung am Cache-Text auf E. 3.4 korrigiert; Satz zur Qualifikation als selbständiges Erwerbseinkommen ohne Beleg gestrichen.
- 9C_54/2025 «Zudienen»: E. 6.2 f. statt 6.3; 9C_270/2021: E. 3.4, 4.3 und 4.4.
- Gerichtsbezeichnung CDT TI («Kammer für Steuerrecht des Tessiner Appellationsgerichts»).
- Neutralität: `pipeline/kommentar.py` ohne Befund; Wertungen Dritter (Locher, Kocher/Stadelmann, OGer NW) als deren Auffassung bzw. mit Gegenüberstellung zum Wortlaut wiedergegeben.
- `pipeline/md2site.py --pruefen`: 0 Befunde; Kommentierung nur wegen Status «in_arbeit» zurückgehalten (Status setzt das Steuerskript).

## Als offen ausgewiesen
Gewillkürtes Geschäftsvermögen bei Erbgang; Quote und Zeitpunkt ohne BGer-Rechtsprechung; Teilveräusserungen (KS 23a vs. Steuerbuch BL); 30-%-Realisation bei Übertragung von Aktiven; Verlustbehandlung; Anrechnung der Vorbesitzdauer bei Umstrukturierungen; abweichender Entscheid OGer NW.
