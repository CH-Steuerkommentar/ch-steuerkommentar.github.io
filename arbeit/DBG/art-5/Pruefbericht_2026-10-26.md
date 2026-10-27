# Prüfbericht zu Art. 5 DBG – 26.10.2026

Unbeaufsichtigter Lauf (API, Steuerskript). Kein `stand.py setze`, kein git, keine Word-Fassung.

## Ergebnis

- `kommentare/DBG/art-5.md`: 42 Randnoten, 89 Fussnoten; `python3 pipeline/kommentar.py` ohne Befund.
- `python3 pipeline/md2site.py --pruefen`: 0 Befunde; Art. 5 wird nur wegen des Status «in_arbeit» zurückgehalten (Status setzt das Steuerskript).
- Register: 40 Bundesgerichtsentscheide (31 aus dem Cache, 9 nachgetragen; 5 A, rund 28 B, 6 C/Erwähnung); kantonale Gerichte: 13 Entscheide verwendet (Kantonal_Praxis.md); ESTV-Praxis: KS 45, KS 37, KS 41.
- Fundstellenprüfung vollständig durch drei Hilfsagenten (Fundstellenliste_2026-10-26.md mit Teillisten); alle Befunde behoben.

## Entscheide und Annahmen im unbeaufsichtigten Lauf

1. Schritt 2 «Ohne Vorarbeit»: Grundlage war der Cache (684 Kandidaten, 34 Treffer = 31 Entscheide). Gegenprobe mit eigenem Regex-Scan der 684 Kandidaten (DE/FR/IT, mit Absatz/Buchstabe): identische Menge. Die Volltextsuche von Open Case Law mit Absatzvarianten lieferte über 400 unscharfe Treffer (überwiegend Art. 5 anderer Erlasse) und wurde nicht ausgewertet. Nachgetragen über Entscheidsuche zu Art. 91–97 DBG und Stichwörtern zu lit. b–f/Abs. 2.
2. Die Rechtsprechung des Bundesgerichts betrifft fast nur lit. a und lit. e; zu lit. abis, b (Auslegung), c, d und f sowie Abs. 2 weist der Text das Fehlen höchstrichterlicher Rechtsprechung aus und stützt sich auf Wortlaut, Materialien, kantonale Entscheide und ESTV-Praxis.
3. Materialien: Botschaft 1983 nur im OCR-Text von Open Case Law geprüft (Bundesarchiv-PDF nicht abrufbar, Zeitüberschreitung); Botschaft Telearbeit (BBl 2024 650) im Fedlex-HTML mit Ziffern zitiert (keine Seitenzahlen in BBl ab 2022); Botschaft Mitarbeiterbeteiligungen mit gedruckten Seitenzahlen. Frühere Fassungen von lit. b und f am Fedlex-PDF (Stand 1.1.2017) und Fedlex-HTML (1.1.2023/1.1.2024) geprüft. Fedlex-Fassungen bis 1.1.2029 enthalten keine weitere Änderung von Art. 5; kein Ausblick-Kapitel.
4. Gliederung: Kapitel je Absatz; lit. d und e in einer Überschrift zusammengelegt (lit. d allein unter drei Randnoten); Querschnittsfragen (Abkommensrecht, Beginn/Ende, Ehegatten) unter «Grundsatz».
5. Musterkommentierung Art. 11 DBG (Grieder/Hongler) für Stil und Aufbau gelesen; die Schwesterkommentierung Art. 4 DBG des Projekts diente als Formatvorbild (Zitierweise kantonaler Gerichte, Erstnennungen). Wertende Stellen nicht übernommen.
6. Lexplorer nicht verfügbar; 0 Lexplorer-Suchen. Keine Websuche, keine Lehrrecherche. Lehre erscheint nur als von Entscheiden wiedergegebene Aussage (BGE 137 II 246 E. 7; 2C_215/2009 E. 2.1; 2P.188/2005 E. 3.2).
7. KS 30 ESTV nur als von BGE 152 II 98 wiedergegebene Praxis zitiert. KS 45 in der Fassung vom 12.6.2019 (Korpusstand Oktober 2023, ohne Regelung zu lit. abis). SSK-Kreisschreiben und kantonale Steuerbücher nicht eingesehen (keine gesicherte Adresse). ESTV-Merkblätter zu Künstlern, Verwaltungsräten, Hypothekarzinsen, Vorsorgeleistungen und internationalem Verkehr nicht im Korpus von Open Case Law.
8. Nicht verwendet, obwohl recherchiert: TAPI GE A/4451/2022 (Sachverhalt trägt die Aussage nicht), AG RV.2003.50053 und ZH SB.1999.00057 (altes kantonales Recht), ZH SB.2020.00106 (Abkommensrecht), ZH QS.2015.8 (kein Bezug auf Abs. 2), VD FI.2025.0005 (zusätzlich zu FI.2021.0035 nicht nötig).
9. Die Gleichsetzung VGer ZH SB.2007.00078 / BGer 2C_258/2008 / BGE 137 II 246 als dasselbe Verfahren wurde im Text vermieden; zitiert ist nur das Nichteintreten von 2C_258/2008 auf den Entscheid SB.2007.00078 (Vermerk im kantonalen Entscheid und Gegenstand von 2C_258/2008).

## Schlussprüfung (Prüfpunkte des Skills `pruefung`, in der Hauptsitzung)

| Prüfpunkt | Befund | Erledigung |
|---|---|---|
| Neutralität | «unzutreffend» (Wiedergabe von 2A.23/2007) von kommentar.py gemeldet | «verwarf es» |
| Rang der Aussagen | kantonale Aussagen teils ohne Gericht im Satz; ESTV-Praxis | Gericht bzw. «nach der Praxis der ESTV» jeweils im Satz |
| Unbelegte Sätze | «Das DBG ist seit 1.1.1995 in Kraft» ohne Beleg; Satz zur Veranlagung selbständig Erwerbender zu allgemein | gestrichen bzw. als Beispiel formuliert |
| Zitierweise | Erstnennungen DBG, StHG, BdBSt, KS 45, KS 37, KS 41; Gesetzesänderungen mit AS | ergänzt |
| Querverweise | alle Labels aufgelöst (kommentar.py) | – |
| Wiederholungen | Quellensteuer-Hinweise in Übersicht und lit. a | Übersicht nur Grundsatz, Einzelheiten bei den Buchstaben |
| Fremdsprachige Zitate | keine wörtlichen fremdsprachigen Zitate im Text | – |

## Offene Fragen, die der Text als offen ausweist

- Ob Art. 5 DBG über die Quellensteuertatbestände der Art. 91 ff. DBG hinausreicht (BGE 137 II 246 E. 7 offengelassen).
- Beweislast für den Zufluss eines Bonus nach dem Wegzug (BGer 9C_663/2022 E. 6.1.2 offengelassen; KGer BL: Steuerpflichtiger).
- Lücke zwischen lit. d und e (nur VGer BE entschieden).
- Keine höchstrichterliche Rechtsprechung zu lit. abis, zur Auslegung von lit. b, c und f sowie zu Abs. 2.
