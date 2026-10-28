# Prüfbericht Art. 4 StHG – 28.10.2026

Unbeaufsichtigter Lauf (Claude-Cloud, geplante Aufgabe). Skill: steuerkommentar-selbstaendig (Fassung im Repository). Ergebnis: kommentare/StHG/art-4.md, 37 Randnoten, 106 Fussnoten; `pipeline/kommentar.py` ohne Befund; `md2site.py --pruefen` ohne Befund (zurückgehalten nur wegen Status «in_arbeit» bis zur Freigabe).

## Ablauf
1. Norm erfasst (Fedlex). Die Fedlex-Konsolidierung vom 1.1.2025 zeigt die Änderungen des Telearbeitsgesetzes (in Kraft 1.1.2025) noch nicht; der Normtext folgt deshalb den vorgreifenden Konsolidierungen 2028/2029 (Art. 4 dort unverändert), Kopf «Fassung vom 1.1.2025».
2. Entscheid-Cache `pipeline/entscheide.py StHG/art-4`: 72 Kandidaten; Triage durch zwei Hilfsagenten (medium), Gegenprobe durch einen dritten (Open Case Law, Entscheidsuche, find_leading_cases): 16 Nachträge (v.a. Sammelzitate «Art. 3 und 4 StHG» und ausgeschriebener Erlasstitel, die die Phrasensuche nicht erfasst). Register 84 Einträge (A 19, B 25, C 39), 2 Fehltreffer. Problemkarte, Gliederungsnotiz.
3. Recherche durch drei Hilfsagenten (high): Materialien (Fedlex, Open Case Law), kantonale Gerichte (Entscheidsuche) und Praxis (Open Case Law, kantonale Gesetze über get_law, Lexplorer Tax), Lehre (ILE-Literatur, Onlinekommentar).
4. Text in der Hauptsitzung; Kürzungs- und Neutralitätsdurchgang.
5. Fundstellenprüfung: drei Hilfsagenten (high), alle 110 Fussnoten der Erstfassung einzeln, dazu beide Verzeichnisse (Fundstellenliste_Teil1–3.md): 141 bestätigt (davon 28 «bestätigt (Vorprüfung)»), 29 korrigiert, 0 nicht belegbar. Alle Korrekturen übernommen.
6. Schlussprüfung: zwei Hilfsagenten (medium) nach den Prüfpunkten von `pruefung` (Schlusspruefung_TeilA.md, _TeilB.md); Befunde in der Hauptsitzung behoben, soweit unten nicht anders vermerkt.

## Entscheide im unbeaufsichtigten Lauf (vermerkt)
- **Lexplorer-Tageslimite:** Lexplorer Tax meldete bereits beim ersten Lese- oder Navigationsaufruf die Tageslimite (2000 Aufrufe, Sperre bis 00:00 UTC; der Lauf fand um 07–09 UTC statt). Suchen waren möglich, lieferten aber nur Vorschauen ohne Autorenangabe. Entscheid: Nicht 15 Stunden warten, sondern (a) Lehre nur aus Fundstellen verwenden, die in früheren Läufen (Art. 4, 5, 6 DBG, Art. 3 StHG) vollständig gelesen und geprüft wurden (Recherche_Lehre.md, Kategorie A); (b) neue Treffer (Kategorie B/C, z.B. FStR 2023/2 zu Immobiliengesellschaften, Reich/Waldburger FStR 2003 zu BGer 2P.289/2000, Schwab N. 584) nicht verwenden; (c) kantonale Steuerbücher und SSK-Kreisschreiben, die nur als Vorschau vorlagen, nicht zitieren; kantonale Praxis stattdessen über kantonale Gesetzestexte (Open Case Law get_law) und KS 45 ESTV (Open Case Law). Die 28 Lehre-Fundstellen «bestätigt (Vorprüfung)» sollten bei der nächsten Nachführung am Chunk nachgelesen werden; die Nachleseliste steht in 01_Recherche/Recherche_Lehre.md und Lexplorer_Fundstellen.md.
- **Lexplorer-Suchen:** 17 (Lehre 9, Praxis 8; Budget 25).
- **Steuerbücher/SSK:** Mangels lesbarer Steuerbücher enthält der Text keine Mehrheitslinie der kantonalen Verwaltungspraxis; die Kantone werden über ihre Gesetze und Gerichte dargestellt.
- **Kantonale Erlassdaten:** Für StG/VS, StG/SG, StG/ZH, StG/LU, LIPP/GE und StG/SH war das Erlassdatum in keinem verwendeten Tool belegt; zitiert mit systematischer Nummer ohne Datum (wie in StHG/art-3). StG/BE und LI/VD mit Datum.
- **Botschaft 1983:** nur OCR-Ausschnitte; S. 87, 156, 289 und 317 über die Seitenposition im Scan.
- **Kurzzitate der Lehre:** wie im Projekt mit Fundort, Titel und Ziffer/Randnote; Seitenzahlen ohne Lexplorer nicht ermittelbar. Mauchle wie in den übrigen Kommentierungen mit «Rz.».

## Befunde der Fundstellenprüfung und Erledigung (Auszug)
- Pinpoints korrigiert: 2C_689/2018 (E. 4.4), 9C_349/2025 (E. 6.2.3 f.), 9C_70/2023 (E. 7.1 f.), 2C_735/2017 (E. 3), 2C_713/2019 (E. 4.3, 5.2, 6), 2C_202/2014 (E. 2.2), 2C_436/2011 (E. 2.3), 9C_131/2025 (E. 2.2.3–2.2.6), 2C_1046/2015 (E. 2.1 und 2.3), BGE 137 II 246 (E. 7 f. ergänzt), Botschaft Telearbeit (Ziff. 4.1 und 7.2 ergänzt).
- Aussagen angepasst: 2C_708/2012 (seit 2006 tätig, drei Kunden); 2C_198/2015 betrifft eine Kollektivgesellschaft; BGE 149 I 125 kommunale Minimal-Grundstücksteuer; 9C_10/2023 (nur «nicht offensichtlich unrichtig»); 2P.289/2000 (juristische Person, Entscheid nach dem Doppelbesteuerungsverbot, Art. 4/21 StHG noch nicht angewandt); 2C_215/2009 (DBA FL); Kurzaufenthalter «grundsätzlich»; Weiterleitung der Steuererklärung «nicht umgehend»; Seeleute (Flaggenerfordernis Praxis, Betreiber-Erfordernis neu); ESTV «Ersuchen» statt «Weisung»; Margraf/Schreiber als Hinweis, nicht als Kritik; Seiler zur Rechtsgrundlage mit «vgl.»; Schwab nur N. 568–572.
- Zusätze: «Beschwerde abgewiesen: BGer 2C_960/2016» bei KGer VD FI.2015.0035; 9C_131/2025 als Beleg für «Nebensteuerdomizil»; BGE 148 II 285 als Gegenakzent zu 2P.2/2003 («vgl. aber»); 2C_309/2014 als Parallelurteil zu BGE 141 II 318 gestrichen; Aufhebungserlass zu Art. 72w StHG (AS 2021 673).

## Befunde der Schlussprüfung und Erledigung
- Inhalt/Widersprüche: Art. 3 und 4 StHG «nur die Steuerpflicht gegenüber den Kantonen» (nicht «nur interkantonal»); Art. 4b Abs. 2 StHG als gesetzliche Grundlage der interkantonalen Ausscheidung ergänzt; «keine beschränkte Steuerpflicht aufgrund eines Geschäftsbetriebs»; Belegenheitsprinzip als Rechtsprechung kenntlich gemacht; doppelte Zitierung 2C_980/2017 und VGer ZH SB.2016.00037 sowie Doppelung der Arbeitstage-Regel (KS 45 Ziff. 3.2.2) beseitigt; Luzerner Handelstatbestand am Gesetz geprüft (§ 9 Abs. 1 lit. c StG/LU aufgehoben auf 1.1.2020) und neutral formuliert; Erläuternder Bericht 2013 nicht mehr als Beleg für die Praxis bis 2017.
- Rang: «nach dem Bundesgericht», «nach Hongler», «nach Mauchle», «nach der Praxis der ESTV» ergänzt; OK-Grieder/Hongler zu Art. 11 DBG als deren Hinweis wiedergegeben.
- Zitierweise: DBG-Erstnennung an die erste Stelle verschoben; Fussnoten chronologisch geordnet (Fn. zu 2C_980/2017, 2C_215/2009, 2C_436/2011); «Telearbeitsgesetz» eingeführt; Datumsformat im Fliesstext.
- Aufbau: Überschriften «Telearbeit» und «Vermittlung» (je zwei Randnoten) mit den Nachbarüberschriften zusammengelegt; «Grundsatz» unter Abs. 1 in «Anwendungsbereich und Verfahren» umbenannt.
- Nicht übernommen: Ausschreiben von «StRK BE» und «consid.» bei Waadtländer Entscheiden (Projektstil, vgl. StHG/art-3); «Bst.» in Botschaftszitaten (Originalgliederung der Botschaft); «Folien zum …» bei Seminareinträgen und Lexplorer-Links auf Dokumentebene (Projektstil); Erlassdaten kantonaler Gesetze (nicht belegt, siehe oben); Art. 38 Abs. 2 StHG als zusätzlicher Beleg zur Quellensteuerzuständigkeit (im Lauf nicht am Original geprüft).

## Offene Fragen, die der Text als offen ausweist
Rechtsnatur kantonaler Ausscheidungsregeln; Schwelle, ab der die Beteiligung an einer Immobiliengesellschaft ein Nutzungsrecht begründet (BGer 9C_674/2025 hängig); keine Rechtsprechung zu lit. abis, b, c und g.

## Zahlen
Randnoten 37; Fussnoten 106; Entscheide im Register 84 (A 19; 16 nachgetragen); im Text zitiert 51 verschiedene BGE/BGer; ILE-Fundstellen 28 (18 Werke); OK-Fundstellen 2 (Art. 11 DBG, Art. 13 StHG; zu Art. 4 StHG gibt es keine OK-Kommentierung); Lexplorer-Suchen 17 (Budget 25).
