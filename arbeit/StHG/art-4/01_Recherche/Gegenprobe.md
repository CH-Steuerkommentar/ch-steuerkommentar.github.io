# Gegenprobe Entscheidregister Art. 4 StHG

Stand: 28. Oktober 2026. Abgleich gegen `cache_liste.txt` (72 Einträge). Werkzeuge: Open Case Law (search_decisions, find_leading_cases, find_relevant_erwaegung, get_erwaegung, get_decision) und Entscheidsuche (search). Keine Lexplorer-Werkzeuge. Zitierstrings ausschliesslich aus `citation_string_de` übernommen.

## 1. Trefferzahlen je Suchweg

### 1.1 Open Case Law, search_decisions (fields compact; has_more bei allen Phrasenabfragen = false)

| Abfrage | court bger | court bge | davon neu (nicht im Cache) |
|---|---|---|---|
| "Art. 4 StHG" | 8 | 2 | 0 |
| "Art. 4 Abs. 1 StHG" | 29 | 4 | 0 |
| "4 Abs. 1 StHG" | 26 | – | 0 |
| "Art. 4 Abs. 2 StHG" | 13 | 3 | 0 |
| "Art. 4 Abs. 2 lit. a StHG" | 4 | – | 0 |
| "Art. 4 Abs. 2 lit. e StHG" | 2 | – | 0 |
| "Art. 4 Abs. 2 lit. b/c/d/f/g StHG" (je einzeln) | 0 | – | 0 |
| "art. 4 LHID" | 4 | 0 | 1 (2C_198/2015) |
| "art. 4 al. 1 LHID" | 14 | 4 | 3 (2C_198/2015, 2C_28/2015, BGE 141 I 235) |
| "4 al. 1 LHID" | 12 | – | 2 (2C_28/2015, 2C_198/2015) |
| "art. 4 al. 2 LHID" | 8 | 1 | 1 (2C_198/2015) |
| "art. 4 al. 2 let. a LHID" | 3 | – | 0 |
| "art. 4 al. 2 let. e LHID" | 1 | – | 0 |
| "art. 4 al. 2 let. b/c/d LHID" (je einzeln) | 0 | – | 0 |
| "art. 4 LAID" | 2 | 0 | 0 |
| "art. 4 cpv. 1 LAID" / "art. 4 cpv. 2 LAID" | 2 / 2 | – | 0 |
| "Art. 3 und 4 StHG" | 5 | – | 5 (2C_73/2018, 2C_415/2019, 2C_416/2019, 2C_897/2018, 2C_398/2021) |
| "art. 3 et 4 LHID" | 2 | – | 2 (2C_28/2015, 2C_330/2021) |

Verworfen: OR-verknüpfte Phrasenabfragen in Open Case Law (854 bis 1036 Treffer; die Engine löst die Phrasen dort auf, Ergebnis unbrauchbar) sowie "4 al. 2 let" LHID und "4 Abs. 2 lit" StHG ohne Artikelbindung (Ergebnislisten übergross, gleiche Ursache).

### 1.2 Entscheidsuche, search (next_cursor jeweils null, ausser Nähe-Suche)

| Abfrage | hierarchy | Treffer | davon neu |
|---|---|---|---|
| "Art. 4 StHG" OR "Art. 4 Abs. 1 StHG" OR "Art. 4 Abs. 2 StHG" | CH_BGer | 31 | 0 |
| "art. 4 LHID" OR "art. 4 al. 1/2 LHID" OR "art. 4 LAID" OR "art. 4 cpv. 1/2 LAID" | CH_BGer | 13 | 0 |
| alle DE/FR/IT-Phrasen wie oben | CH_BGE | 7 | 0 |
| "Art. 4 Abs. 2 lit" AND StHG | CH_BGer | 11 | 0 (4 Fehltreffer: DBA, AHVG) |
| ("art. 4 al. 2 let" OR "art. 4 al. 1 let") AND LHID | CH_BGer | 12 | 2 (2C_140/2016, 2C_436/2016) |
| Langform FR ("4 [al. …] de la loi fédérale du 14 décembre 1990 sur l'harmonisation") | CH_BGer + CH_BGE | 9 | 3 (2C_28/2015, BGE 141 I 235, 2C_436/2016) |
| Langform DE ("Art. 4 [Abs. …] des Bundesgesetzes vom 14. Dezember 1990 über die Harmonisierung") | CH_BGer + CH_BGE | 3 | 3 (2C_340/2022, BGE 149 I 125, BGE 150 II 244) |
| Sammelzitate ("Art. 3 und 4 StHG", "Art. 3 f. StHG", "art. 3 et 4 LHID", "Art. 1, 3 und 4 StHG" u.a.) | CH_BGer + CH_BGE | 11 | 9 (2C_28/2015, BGE 141 I 235, 2C_330/2021, 2C_1025/2016, 2C_897/2018, 2C_73/2018, 2C_415/2019, 2C_416/2019, BGE 148 II 285, 2C_398/2021; BGE 125 I 458 bekannt) |
| "Art. 4 und 21 StHG", "art. 4 et 21 LHID", "Art. 4 und 35 StHG" u.a. | CH_BGer + CH_BGE | 5 | 0 |
| Nähe-Suche "Art. 4 StHG"~4 | CH_BGer + CH_BGE | 301 | 0 (erste 100 geprüft: durchwegs "Abs. 4" anderer StHG-Artikel; nicht weiter geblättert) |

### 1.3 find_leading_cases (law_code StHG, article 4)

- court bger: 36 Entscheide, alle im Cache.
- court bge: 5 Entscheide, alle im Cache.

### 1.4 Thematische Ergänzung (seit 2001, nur BGer/BGE)

- Open Case Law: "Liegenschaftenhändler Spezialsteuerdomizil interkantonal Doppelbesteuerung" (207+), "commerçant d'immeubles double imposition intercantonale rattachement économique" (212+), "Betriebsstätte selbständige Erwerbstätigkeit interkantonale Doppelbesteuerung … StHG" (206+), "établissement stable activité indépendante double imposition intercantonale LHID" (227+); je die ersten 50 Treffer gegen den Cache und die Phrasenergebnisse abgeglichen.
- Pinpoint-Abgleich (find_relevant_erwaegung) bei BGE 139 II 373, 2C_375/2010, 2C_152/2019, 2C_1039/2020, 2C_350/2018, 2C_401/2020: keine Zitierung von Art. 4 StHG; einschlägige Normzitate betreffen Art. 21 StHG (juristische Personen) oder nur die Kollisionsregeln zu Art. 127 Abs. 3 BV.
- Ergebnis: 0 neue Entscheide. Die Liegenschaftenhändler- und Betriebsstättenpraxis ab 2001 zitiert Art. 4 StHG in der Regel nicht oder ist bereits im Cache (z.B. 2C_18/2014, 2C_708/2012, 2C_689/2018, 2C_1046/2015).

### 1.5 Aussortierte Fehltreffer

- Art. 4 Abs. 2 lit. a DBA/OECD-MA bzw. CDI-F: 2C_452/2012, 2P.340/2005, 2C_128/2016, 2C_924/2014; 9C_496/2023 enthält zusätzlich OECD-MA (bereits im Cache).
- Art. 4 Abs. 2 lit. b AHVG: 9C_241/2019. Art. 4 al. 1 let. e LApEl: 2C_495/2017. Art. 4 al. 1 let. a der Genfer Quellensteuerverordnung: 9C_632/2024.
- "chapitre 4" bzw. andere Absätze der LHID: H_99/2001, 2C_494/2016, 2C_648/2007, BGE 134 II 207.
- Art. 4 BV: BGE 125 I 65, BGE 124 I 145.
- Art. 21 StHG ohne Art. 4: 2C_401/2020, 2C_1039/2020.

## 2. Nachträge

Besetzung: Abteilung nach den Metadaten; Spruchkörper (Richterinnen und Richter) nicht einzeln geprüft. Fassung: Alle Nachträge betreffen Steuerperioden vor Einfügung von Art. 4 Abs. 2 lit. abis StHG (Telearbeit); massgebend ist die jeweils für die Steuerperiode geltende Fassung von Art. 4 StHG, deren Abs. 1 und Abs. 2 lit. a unverändert wiedergegeben werden.

| Entscheid | Datum | Besetzung | Normstelle | Sachfrage | Kernaussage | E. | Ergebnis | Klasse | Fassung |
|---|---|---|---|---|---|---|---|---|---|
| BGE 141 I 235 | 19.06.2015 | II. öffentlich-rechtliche Abteilung | Art. 3 und 4 StHG (art. 3 et 4 LHID) | Interkommunale Zuteilung des Erwerbseinkommens (GE, Arbeitsgemeinde vs. Wohngemeinde) | Art. 3 und 4 StHG regeln nur die interkantonale, nicht die interkommunale Steuerpflicht; die Kantone sind bei der Abgrenzung der Gemeindesteuerhoheiten unter Vorbehalt von Rechtsgleichheit und Willkürverbot frei. | E. 6.3 (auch E. 5.2) | Abweisung der Rüge der Verletzung von Art. 49 Abs. 1 BV | A | Fassung vor lit. abis (GE, Steuerperioden vor 2010) |
| BGer 2C_28/2015 vom 19. Juni 2015 | 19.06.2015 | II. öffentlich-rechtliche Abteilung | art. 3 et 4 LHID | wie BGE 141 I 235 (Ausgangsurteil) | wie BGE 141 I 235. | E. 6.3 (auch E. 5.2) | wie BGE 141 I 235 | A | wie oben |
| BGer 2C_897/2018 vom 25. Oktober 2018 | 25.10.2018 | II. öffentlich-rechtliche Abteilung | Art. 3 und 4 StHG | Beschwerdelegitimation einer Urner Einwohnergemeinde im Streit um das Steuerdomizil einer natürlichen Person | Die Voraussetzungen der persönlichen und wirtschaftlichen Zugehörigkeit ergeben sich für die harmonisierten Steuern abschliessend aus Art. 3 und 4 StHG; Kantone und Gemeinden haben keinen Gestaltungsspielraum. | E. 2.2.2 | Nichteintreten (keine Legitimation der Gemeinde) | A | Fassung vor lit. abis |
| BGer 2C_330/2021 vom 3. August 2021 | 03.08.2021 | II. öffentlich-rechtliche Abteilung | art. 3 et 4 LHID | Interkommunales Hauptsteuerdomizil (VS) | Verweist das kantonale Recht für den interkommunalen Domizilstreit auf Art. 3 und 4 StHG, gelten diese als autonomes kantonales Recht (Prüfung nur auf Willkür). | E. 5.2 | Prüfung auf Willkür beschränkt | B | Fassung vor lit. abis |
| BGE 148 II 285 | 23.12.2021 | II. öffentlich-rechtliche Abteilung | Art. 3 und 4 StHG | Wohnsitz bei Patchwork-Familie; leitender Angestellter (LU) | Die harmonisierte Regelung der subjektiven Steuerpflicht in Art. 3 und 4 StHG soll die Aufspaltung der Besteuerung auf zwei Kantone vermeiden; deshalb wird die Figur des leitenden Angestellten nicht ausgedehnt. | E. 3.6.2 | Abweisung | B | Fassung vor lit. abis |
| BGer 2C_398/2021 vom 23. Dezember 2021 | 23.12.2021 | II. öffentlich-rechtliche Abteilung | Art. 3 und 4 StHG | wie BGE 148 II 285 (Ausgangsurteil) | wie BGE 148 II 285. | E. 3.6.2 | wie BGE 148 II 285 | B | wie oben |
| BGE 149 I 125 | 20.03.2023 | II. öffentlich-rechtliche Abteilung | Art. 4 Abs. 1 StHG | Walliser Minimal-Grundstücksteuer für Nichtwohnsässige (Art. 181 Abs. 2 StG/VS) | Auch nichtwohnsässige Grundeigentümer sind aufgrund wirtschaftlicher Zugehörigkeit (Art. 4 Abs. 1 StHG) der Einkommens- und Vermögenssteuer unterworfen; die Ansässigkeit taugt deshalb nicht als Abgrenzungskriterium für eine Minimalsteuer. | E. 5.3.4 | Gutheissung (Verstoss gegen Art. 8 Abs. 1 BV) | B | Fassung vor lit. abis |
| BGer 2C_340/2022 vom 20. März 2023 | 20.03.2023 | II. öffentlich-rechtliche Abteilung | Art. 4 Abs. 1 StHG | wie BGE 149 I 125 (Ausgangsurteil) | wie BGE 149 I 125. | E. 5.3.4 | wie BGE 149 I 125 | B | wie oben |
| BGE 150 II 244 | 29.02.2024 | III. öffentlich-rechtliche Abteilung | Art. 3 Abs. 1 und Art. 4 Abs. 1 StHG | Veranlagungszuständigkeit DBG (Art. 108 DBG), Wohnsitz eines Bundesangestellten im Ausland | Anders als bei der direkten Bundessteuer (Einheit des Veranlagungsorts) unterstehen Steuerpflichtige bei den kantonalen Steuern regelmässig mehreren Steuerhoheiten (z.B. unbeschränkt am Wohnsitz, beschränkt kraft Grundbesitz nach Art. 4 Abs. 1 StHG). | E. 4.3.3 | Nichtigkeit des kantonalen Feststellungsentscheids | B | Fassung vor lit. abis (Steuerperiode 2017). Hinweis: Das Ausgangsurteil BGer 9C_496/2023 vom 29. Februar 2024 steht im Cache, die BGE-Fundstelle fehlt dort. |
| BGer 2C_198/2015 vom 11. September 2015 | 11.09.2015 | II. öffentlich-rechtliche Abteilung | Art. 4 Abs. 1 StHG (art. 4 al. 1 LHID; art. 4 LHID) | Interkantonale Doppelbesteuerung GE/JU; Kommanditärin bzw. Teilhaberin einer Personengesellschaft ohne Arbeitsleistung | Wiedergabe von Art. 4 Abs. 1 StHG (Steuerpflicht kraft Unternehmen im Kanton); Gewinnanteil und Kapitalzinsen sind nur im Sitzkanton der Gesellschaft steuerbar, der Wohnsitzkanton darf ohne persönliche Arbeit keinen Lohnanteil besteuern. | E. 5.1 (Normzitat), E. 6.4 (Ergebnis) | Gutheissung gegenüber JU | C | Fassung vor lit. abis (Steuerperiode 2007) |
| BGer 2C_140/2016 vom 30. Mai 2017 | 30.05.2017 | II. öffentlich-rechtliche Abteilung | Art. 4 Abs. 2 lit. a StHG | Quellensteuer einer in Frankreich wohnhaften Erwerbstätigen (VD), Steuerperioden 2010 bis 2012 | Beschränkte Steuerpflicht für das Erwerbseinkommen (Verweis auf Art. 4 Abs. 2 lit. a StHG neben Art. 5 Abs. 1 lit. a und Art. 6 Abs. 2 DBG). | E. 4.1 | Quellensteuerpflicht bestätigt | C | Fassung vor lit. abis |
| BGer 2C_436/2016 vom 21. Dezember 2016 | 21.12.2016 | II. öffentlich-rechtliche Abteilung | Art. 4 Abs. 2 lit. a StHG | Steuerpflicht kraft wirtschaftlicher Zugehörigkeit für Erwerbstätigkeit im Kanton GE, ICC/IFD 2011 | Gleiche Rechtsfrage im DBG und im harmonisierten Recht (Verweis auf Art. 4 Abs. 2 lit. a StHG), daher gemeinsamer Entscheid. | E. 1 | – (nur Normzitat in der Eintretenserwägung) | C | Fassung vor lit. abis (Steuerperiode 2011) |
| BGer 2C_73/2018 vom 3. Juni 2019 | 03.06.2019 | II. öffentlich-rechtliche Abteilung | Art. 3 und 4 StHG | Steuerwohnsitz einer natürlichen Person (SG) | Die persönliche Zugehörigkeit ist eine bundesrechtlich harmonisierte Rechtsfrage (Verweis auf Art. 3 und 4 StHG); massgebend sind die Kollisionsnormen zu Art. 127 Abs. 3 BV. | E. 3 | – (Art. 4 nur mitzitiert) | C | Fassung vor lit. abis |
| BGer 2C_415/2019 vom 20. Dezember 2019 | 20.12.2019 | II. öffentlich-rechtliche Abteilung | Art. 3 und 4 StHG | Steuerwohnsitz der Ehefrau (LU), Steuerperioden 2009 und 2010 | wie 2C_73/2018. | E. 5 | – (Art. 4 nur mitzitiert) | C | Fassung vor lit. abis |
| BGer 2C_416/2019 vom 20. Dezember 2019 | 20.12.2019 | II. öffentlich-rechtliche Abteilung | Art. 3 und 4 StHG | Steuerwohnsitz des Ehemanns (LU/VAE), Steuerperioden 2009 und 2010 | wie 2C_73/2018, mit interkantonalem und internationalem Bezug. | E. 5 | – (Art. 4 nur mitzitiert) | C | Fassung vor lit. abis |
| BGer 2C_1025/2016 vom 14. November 2016 | 14.11.2016 | II. öffentlich-rechtliche Abteilung | Art. 3 f. StHG | Untersuchungspflicht und Feststellungsentscheid bei bestrittener Steuerhoheit (BE) | Die behördliche Untersuchungspflicht erstreckt sich auch auf die subjektive Steuerpflicht (Art. 3 f. StHG); bei bestrittener interkantonaler Steuerhoheit ist vorab ein Feststellungsentscheid zu erlassen. | E. 3.2 | Abweisung | C | Fassung vor lit. abis |

### Tragender Inhalt der A-Entscheide

**BGE 141 I 235 (= BGer 2C_28/2015 vom 19. Juni 2015)**
- E. 5.2: Die Gemeinden sind an das StHG gebunden, soweit ihnen das kantonale Recht Steuerkompetenzen einräumt; zu diesen Bestimmungen gehören Art. 3 StHG (persönliche Zugehörigkeit) und Art. 4 StHG (wirtschaftliche Zugehörigkeit natürlicher Personen).
- E. 6.3: Nach ihrem Wortlaut betreffen Art. 3 und 4 StHG die interkantonale, nicht die interkommunale Steuerpflicht. Wegen Art. 3 BV und weil Art. 127 Abs. 3 BV nur das interkantonale Verhältnis erfasst, ist ihre Tragweite nicht extensiv und contra legem auf die Abgrenzung der Gemeindesteuerhoheiten auszudehnen. Die Kantone sind deshalb frei, die Steuerkompetenzen ihrer Gemeinden zu begrenzen, unter Vorbehalt von Rechtsgleichheit und Willkürverbot. Die Genfer Zuteilung eines Teils des Erwerbseinkommens an die Arbeitsgemeinde verletzt Art. 4 StHG deshalb nicht.

**BGer 2C_897/2018 vom 25. Oktober 2018**
- E. 2.2.2: Für die harmonisierten Steuern ergeben sich die Voraussetzungen der persönlichen und der wirtschaftlichen Zugehörigkeit abschliessend aus Art. 3 und 4 StHG. Kantonen und Gemeinden verbleibt kein Gestaltungsspielraum, denn Zugehörigkeit sowie unbeschränkte und beschränkte Steuerpflicht müssen schweizweit einheitlich gehandhabt werden, sonst drohen Nicht- oder Doppelbesteuerungen. Die Aussage trägt die Verneinung der Gemeindeautonomie und damit der Beschwerdelegitimation der Einwohnergemeinde. Die Einordnung als A ist knapp, weil Art. 4 nur zusammen mit Art. 3 StHG genannt wird. Je nach Massstab ist auch B vertretbar.

## 3. find_leading_cases (Art. 4 StHG)

Die Pinpoint-Erwägung war in den Ergebnissen nicht enthalten (`pinpoint` leer). Die Pinpoints der Ränge im Cache wurden hier nicht neu erhoben.

### court bge

| Rang | Zitierstring | Zitate aus Art.-4-Entscheiden (gesamt) | Pinpoint |
|---|---|---|---|
| 1 | BGE 134 I 303 | 17 (559) | nicht geliefert |
| 2 | BGE 142 II 182 | 8 (624) | nicht geliefert |
| 3 | BGE 141 II 318 | 4 (46) | nicht geliefert |
| 4 | BGE 137 II 246 | 1 (35) | nicht geliefert |
| 5 | BGE 150 II 40 | 0 (44) | nicht geliefert |

### court bger

| Rang | Zitierstring | Zitate aus Art.-4-Entscheiden (gesamt) |
|---|---|---|
| 1 | BGer 2C_708/2012 vom 21. Dezember 2012 | 8 (95) |
| 2 | BGer 2P.2/2003 vom 7. Januar 2004 | 6 (58) |
| 3 | BGer 2C_1046/2015 vom 10. August 2016 | 6 (13) |
| 4 | BGer 2C_615/2021 vom 23. September 2022 | 4 (17) |
| 5 | BGer 2C_263/2018 vom 11. Februar 2019 | 3 (64) |
| 6 | BGer 2C_689/2018 vom 20. Juni 2019 | 3 (30) |
| 7 | BGer 2C_76/2015 vom 24. Mai 2016 | 2 (19) |
| 8 | BGer 2C_215/2009 vom 1. Oktober 2009 | 2 (9) |
| 9 | BGer 9C_608/2022 vom 13. November 2023 | 1 (43) |
| 10 | BGer 2C_18/2014 vom 15. Januar 2015 | 1 (28) |
| 11 | BGer 2C_952/2020 vom 6. Oktober 2021 | 1 (21) |
| 12 | BGer 2C_510/2017 vom 16. September 2019 | 1 (17) |
| 13 | BGer 2C_1011/2012 vom 5. Mai 2014 | 1 (13) |
| 14 | BGer 2C_309/2014 vom 16. Juli 2015 | 1 (9) |
| 15 | BGer 9C_349/2025 vom 18. Dezember 2025 | 1 (4) |
| 16 | BGer 2C_662/2010 vom 25. März 2011 | 1 (2) |
| 17 | BGer 9C_472/2024 vom 15. September 2025 | 1 (2) |
| 18–36 | 2C_794/2015, 9C_496/2023, 2C_684/2019, 2C_939/2019, 2C_712/2015, 2C_199/2011, 2C_171/2019, 9C_315/2023, 2C_511/2017, 2A.23/2007, 2A.54/2003, 2C_133/2018, 2C_646/2021, 2C_713/2019, 9C_131/2025, 2C_202/2014, 9C_10/2023, 2C_644/2018, 9C_538/2025 | je 0 |

Alle 41 Leitentscheide (36 BGer, 5 BGE) sind bereits im Cache. Keiner der Nachträge erscheint in der Rangliste, weil die Nachträge Art. 4 StHG nur in Sammelzitaten ("Art. 3 und 4"), in der Langform des Erlasstitels oder als lit.-Zitat ohne Kurztitel anführen.
