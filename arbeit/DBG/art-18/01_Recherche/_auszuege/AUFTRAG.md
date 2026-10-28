# Auftrag: Triage Entscheidregister Art. 18 DBG

Norm: Art. 18 DBG (Bundesgesetz über die direkte Bundessteuer, SR 642.11), «Grundsatz» der selbständigen Erwerbstätigkeit, geltende Fassung (Abs. 2 seit 1.1.2009, UStR II):
1 Steuerbar sind alle Einkünfte aus einem Handels-, Industrie-, Gewerbe-, Land- und Forstwirtschaftsbetrieb, aus einem freien Beruf sowie aus jeder anderen selbständigen Erwerbstätigkeit.
2 Zu den Einkünften aus selbstständiger Erwerbstätigkeit zählen auch alle Kapitalgewinne aus Veräusserung, Verwertung oder buchmässiger Aufwertung von Geschäftsvermögen. Der Veräusserung gleichgestellt ist die Überführung von Geschäftsvermögen in das Privatvermögen oder in ausländische Betriebe oder Betriebsstätten. Als Geschäftsvermögen gelten alle Vermögenswerte, die ganz oder vorwiegend der selbstständigen Erwerbstätigkeit dienen; Gleiches gilt für Beteiligungen von mindestens 20 Prozent am Grund- oder Stammkapital einer Kapitalgesellschaft oder Genossenschaft, sofern der Eigentümer sie im Zeitpunkt des Erwerbs zum Geschäftsvermögen erklärt. Artikel 18b bleibt vorbehalten.
3 Für Steuerpflichtige, die eine ordnungsgemässe Buchhaltung führen, gilt Artikel 58 sinngemäss.
4 Die Gewinne aus der Veräusserung von land- und forstwirtschaftlichen Grundstücken werden den steuerbaren Einkünften nur bis zur Höhe der Anlagekosten zugerechnet.
(Bis 31.12.2008 lautete Abs. 2 Satz 3: «Als Geschäftsvermögen gelten alle Vermögenswerte, die ganz oder vorwiegend der selbständigen Erwerbstätigkeit dienen.» ohne Beteiligungserklärung und ohne Vorbehalt Art. 18b.)

## Material
Die Datei `teilN.md` (dein Teil) enthält je Entscheid: Zitierstring (`zitat_de`, verbindlich), Cache-Datei (JSON mit Feld `text` = Volltext), Datum, Sprache, Textanfang (meist Regeste bzw. Rubrum) und bis zu 5 Textstellen, an denen Art. 18 DBG zitiert wird, sowie die weiteren zitierten Normen.

## Vorgehen
1. Für jeden Entscheid: Fehltreffer erkennen (z.B. Art. 18 eines anderen Erlasses, Normkette ohne Bezug) → Klasse C oder «Fehltreffer».
2. Klasse bestimmen: **A** tragend – die Erwägung legt Art. 18 DBG aus oder entscheidet eine Sachfrage daraus (Begriff selbständige Erwerbstätigkeit, Liegenschaften-/Wertschriftenhandel, Geschäftsvermögen/Präponderanz, Privatentnahme, Abs. 3/4 usw.); **B** Anwendung – Subsumtion nach bekannten Grundsätzen, Kasuistik; **C** Erwähnung (Normkette, Sachverhalt, Prozessgeschichte, AHV-Fall nur mit Verweis).
3. A-Entscheide an der einschlägigen Erwägung im Cache-Text lesen (nicht ganz! mit Python gezielt die Erwägung suchen, z.B. `python3 -c "import json;t=json.load(open(F))['text'];i=t.find('2.3');print(t[i:i+3000])"`); B über Textanfang und Stellen; C nur zählen.
4. Bei AHV-Entscheiden (H_, 9C_, BGE … V …): Diese betreffen oft Art. 17 AHVV, der auf Art. 18 Abs. 2 DBG verweist (Kapitalgewinne/Geschäftsvermögen in der AHV). Klasse A nur, wenn das Gericht Begriffe von Art. 18 DBG selbst auslegt (z.B. Geschäftsvermögen, Präponderanz, Liegenschaftenhandel).
5. Steuerperiode bzw. Fassung notieren (vor/nach 1.1.2009 bei Abs. 2 Satz 3).

## Einheitliche Sachfragen (bitte diese Bezeichnungen verwenden; Neues mit eigenem Namen)
- S1 Begriff selbständige Erwerbstätigkeit (Kriterien, Gesamtbild, Gewinnabsicht)
- S2 Abgrenzung unselbständig/selbständig
- S3 Liebhaberei / Hobby (fehlende Gewinnabsicht, Verluste)
- S4 Liegenschaftenhandel (quasi-gewerbsmässig, Kriterien)
- S5 Wertschriftenhandel (gewerbsmässig, KS 36, Safe-haven)
- S6 Handel mit anderen Vermögenswerten (Darlehen, Kunst, Krypto, Beteiligungen)
- S7 Beginn/Ende der selbständigen Erwerbstätigkeit; Aufgabe, Liquidation, Verpachtung
- S8 Geschäftsvermögen: Präponderanzmethode, Zuordnung, gemischt genutzte Vermögenswerte
- S9 Beteiligungen als (gewillkürtes) Geschäftsvermögen, 20-%-Erklärung
- S10 Kapitalgewinne: Veräusserung, Verwertung, buchmässige Aufwertung
- S11 Privatentnahme / Überführung ins Privatvermögen (Entnahme, Realisation, Bewertung)
- S12 Überführung ins Ausland / Betriebsstätte
- S13 Abs. 3: ordnungsgemässe Buchhaltung, Massgeblichkeit, Art. 58 sinngemäss
- S14 Abs. 4: land- und forstwirtschaftliche Grundstücke (Begriff, Anlagekosten, wiedereingebrachte Abschreibungen)
- S15 Personengesellschaften (Kollektiv-/Kommanditgesellschaft, einfache Gesellschaft)
- S16 Ermittlung des Einkommens / Ermessensveranlagung / Beweislast
- S17 Verhältnis zur AHV (Art. 17 AHVV, Beitragspflicht)
- S18 Verfahren, Nachsteuer, Hinterziehung (nur wenn Art. 18 inhaltlich behandelt)
- S19 Erbengemeinschaft, Erbteilung, Unternehmensnachfolge
- S20 Sonstiges (bitte benennen)

## Ausgabe
Schreibe `register_teilN.md` in `arbeit/DBG/art-18/01_Recherche/` mit:
1. Tabelle, eine Zeile je Entscheid (alle Entscheide deines Teils, auch C):
| Entscheid | Datum | Normstelle | Sachfrage | Kernaussage (ein Satz) | E. | Ergebnis | Klasse | Steuerperiode/Fassung |
Entscheid exakt wie der Zitierstring in der Datei (z.B. «BGer 2C_1001/2018 vom 30. Januar 2020», «BGE 125 II 113»). BGE und zugehöriges BGer-Urteil, falls beide vorhanden, vermerken.
2. Danach Abschnitt «A-Entscheide: tragende Sätze»: je A-Entscheid die tragende(n) Formel(n) als wörtliches Kurzzitat (max. 3 Zeilen, aus dem Cache-Text kopiert, mit genauer E.-Nummer) und Sachverhaltskern in einem Halbsatz.
3. Zum Schluss: Zahl A/B/C/Fehltreffer, und Auffälligkeiten (Praxisänderungen, offen gelassene Fragen mit E.-Nummer, oft zitierte Leitentscheide, die im Cache fehlen, z.B. ältere BGE).

Regeln: Nur aus dem Cache-Text; nichts aus dem Gedächtnis; Zitierstrings nur aus `zitat_de`. Keine Lexplorer-Suchen (Budget 0), keine Websuche. Gib als Endantwort nur eine kurze Bestätigung mit den Zahlen A/B/C und den 5 wichtigsten A-Entscheiden zurück (die Details stehen in der Datei).
