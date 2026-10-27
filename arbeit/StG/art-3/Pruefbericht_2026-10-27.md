# Prüfbericht Art. 3 StG – 27.10.2026 (Claude-Cloud, unbeaufsichtigter Lauf)

## Entscheide im unbeaufsichtigten Lauf
- Reserviert: StG/art-3 (reservierung.py). Kein stand.py, keine Word-Fassung (Vorgabe).
- Register und Problemkarte selbst erstellt (Hilfsagent Register, effort medium). Cache (entscheide.py): 13 Treffer, davon 1 einschlägig (BGE 128 II 46), 12 Fehltreffer (kantonale «StG»/«LT»). Gegenprobe Open Case Law und Entscheidsuche: Vorgängernorm ist Art. 2 StG 1917; Register 18 Einträge (11 A, 1 B, 6 C), überwiegend alte BGE (1919–1951).
- Kantonale Gerichte (nur Entscheidsuche): 4 Entscheide TI CDT, VGer ZH VB.2001.00171, VGer GE A/4034/2008 (bestätigt durch 2C_579/2009). Keine Entscheide aus VD, FR, NE, JU, BE.
- Verwaltungspraxis: kein ESTV-Kreisschreiben zu Art. 3 StG; KS 33 Ziff. 1.7.4 verwendet. ESTV-Entscheid vom 4.8.1989 und Kreisschreiben des Bundesrates vom 20.2.1918 nur über die Tessiner Urteile belegt; Text nennt das Kreisschreiben nur als Bezugnahme der CDT.
- Onlinekommentar.ch: keine Kommentierung zum StG oder zu einer verwandten Norm vorhanden (onlinekommentar.py liste) – 0 OK-Fundstellen.
- Übersicht ohne «Harmonisierung», stattdessen «Verhältnis zu anderen Erlassen» (Art. 134 BV, kantonale Handänderungssteuern).
- Materialien: OCR-Text über search_botschaft; Seitenzählung (Dokumentseite → BBl-Seite) vom Prüfagenten bestätigt (1972: n+1277; 1999: Seite 19 = 7940). Fedlex-Webseiten nicht direkt abrufbar (SPA).
- Titel des BG vom 8.10.1999 nicht belegbar → neutral umformuliert («im Zuge der Anpassung der Gesetzgebung an die neue Bundesverfassung»).
- Lexplorer-Suchen: 10 von 25 (3 Hilfsagent Kantone/Praxis, 7 ILE-Literatur Hauptsitzung); ILE-Literatur zu Art. 3 StG spärlich: Regli 2021, Schwab 2019, Dahinden FStR 2004.
- Schwab 2019: Lexplorer führt deutschen Werktitel, Kapitel französisch; Werktitel wie in Lexplorer übernommen (für Nachführung vermerkt).

## Fundstellenprüfung (Schritt 8, zwei Hilfsagenten, vollständig)
- Teil 1 (alle 28 Fussnoten mit BGer/BGE): alle Zitierstrings bestätigt; korrigiert: BGE 71 I 204 Pinpoints (E. 5a/5d für «Natur der Urkunde», im Konjunktiv umformuliert; E. 1 für Anleihensobligationen und Steuercharakter; Sachverhalt C/E. 3 für Klageweg); Rechtsweg seit VDG 1928 statt «OG 1943»; Einleitung der Kasuistik («die der Ausschluss erfasst»); Pinpoints 66 I 92 (E. 3, 5 f.), 70 I 56 (E. 2), 46 I 53 (S. 56), 2C_579/2009 (E. 5.1 f., 5.1 und 5.3); Serienschuldbriefe als Lehre, auf die das BGer verweist; Zinsen: kantonales Recht.
- Teil 2 (übrige): korrigiert Gliederungstitel (Einleitung, III.), CDT TI 80.2002.99 E. 7.1 f., Zuordnung ESTV-Auffassung in CDT TI 80.1997.144, CDT TI 80.2002.54 E. 7.6.2–7.6.4, Dahinden Ziff. 4.4–4.6 mit Ergebnis der Autorin, Datum Botschaft 1999 (11.8.1999), Art. 41bis Abs. 2 aBV. Alle übrigen bestätigt.

## Schlussprüfung (Schritt 9)
- pipeline/kommentar.py: 21 Randnoten, 56 Fussnoten, 0 Befunde (ein «dürfte» im Neutralitätsdurchgang umformuliert).
- Erstnennungen ergänzt (FusG). Querverweise geprüft (Labels vorhanden).
- Offen ausgewiesen: subjektive Befreiungen (nur kantonal entschieden); Serientitel nach Aufhebung der Emissionsabgabe auf Obligationen; Immobiliengesellschaften im Verhältnis zu Art. 3 StG; Rechtsweg unter dem BGG; Abs. 2 ohne Rechtsprechung; kantonale Abgaben auf Prämienrechnungen.
- md2site.py --pruefen: zurückgehalten nur wegen Status «in_arbeit» (setzt das Steuerskript beim Freigeben).
