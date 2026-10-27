# Entscheidregister Art. 8 DBG (SR 642.11) – Beginn und Ende der Steuerpflicht

Stand: 26. Oktober 2026 (Lauf Claude-Cloud, ohne Karteikarten). Werkzeuge: `pipeline/entscheide.py DBG/art-8` (Kandidaten über Entscheidsuche, Volltexte aus Open Case Law), Open Case Law (OCL) `get_erwaegung`, `find_relevant_erwaegung`, `find_leading_cases`, Entscheidsuche (ES). Lexplorer nicht verwendet.
Zitierstrings: aus OCL (`zitat_de` der Pipeline bzw. `citation_string_de`). Erwägungen der A-Entscheide an der Stelle gelesen (lokaler Volltext oder `get_erwaegung`).

## Suchwege und Trefferzahlen

| # | Weg | Abfrage | Treffer | Bemerkung |
|---|---|---|---|---|
| 1 | Pipeline (ES-Phrasensuche, CH_BGer/CH_BGE) | `"Art. 8" AND (DBG OR LIFD)` | 806 Kandidaten → 25 Einträge (21 Entscheide; 4 BGE mit BGer-Dublette) | Volltext auf Zitat von Art. 8 DBG geprüft |
| 2 | ES CH_BGer/CH_BGE (Gegenprobe) | `"Art. 8 DBG" OR "art. 8 LIFD" OR "Art. 8 Abs. 1/2 DBG" OR "art. 8 al. 1/2 LIFD"` | 21 (CH) | alle im Register |
| 3 | ES CH_BGer/CH_BGE (Gegenprobe) | `"art. 8 cpv." LIFD`, `"Art. 8 Abs. 1 und 2 DBG"`, `"Art. 9 WStB"`, `"Art. 8/9 BdBSt"` mit Steuerpflicht | 7 | alle im Register |
| 4 | OCL `search_decisions` bger, Phrasen-OR | wie 2 | 1139 | Rauschen (Tokenisierung), nicht ausgewertet |
| 5 | OCL `find_leading_cases` DBG 8 | – | 24 (davon 15 BGer/BGE) | alle BGer/BGE im Register |
| 6 | OCL `get_article_history` 642.11/8 | – | 15 | alle BGer/BGE im Register |

Nachtrag ausserhalb der Phrasentreffer (zitiert Art. 8 DBG nicht, aber für Sachfrage 3 tragend): BGE 150 II 244, E. 5.6.5 (Präzisierung zur Wohnsitzverlegung).

## Register

| Entscheid | Datum | Besetzung | Normstelle | Sachfrage | Kernaussage (ein Satz) | E. | Ergebnis | Klasse | Fassung |
|---|---|---|---|---|---|---|---|---|---|
| BGE 138 II 300 (= BGer 2C_614/2011 vom 4. Mai 2012) | 4.5.2012 | 3 | Abs. 2 | Wegzug ins Ausland | Der einmal begründete Wohnsitz besteht bis zum Erwerb eines neuen fort (Art. 24 Abs. 1 ZGB analog); die Wohnsitzverlegung hat der Steuerpflichtige darzulegen; «Weltenbummler». | 3.1–3.6 | Beschwerde ESTV gutgeheissen | A | geltend |
| BGE 141 II 318 (= BGer 2C_309/2014 vom 16. Juli 2015) | 16.7.2015 | 5 | Abs. 2 | Tod, Ehegatten | Der Tod eines Ehegatten beendet bundessteuerlich die gemeinsame Steuerpflicht beider Gatten für alle Faktoren, auch eine Liegenschaft im anderen Kanton. | 2.2.2, 2.3.4 | gutgeheissen | B | geltend |
| BGE 149 II 34 (= BGer 2C_977/2020 vom 6. Mai 2022) | 6.5.2022 | 3 | Abs. 1 und 2 | Wegzug; neue beschränkte Steuerpflicht; Art. 40 Abs. 3 | Mit dem Wegzug endet die unbeschränkte Steuerpflicht; eine später in derselben Periode aufgenommene Grenzgängertätigkeit begründet eine neue beschränkte Steuerpflicht, für die nur ihr Zeitraum auf zwölf Monate umgerechnet wird. | 6.1–6.3 | abgewiesen | A | geltend |
| BGE 152 II 98 (= BGer 9C_416/2024 vom 14. August 2025) | 14.8.2025 | 5 | Abs. 1 und 2 (i.V.m. Art. 40 Abs. 3) | Wechsel beschränkt → unbeschränkt | Beim Wechsel von wirtschaftlicher zu persönlicher Zugehörigkeit ist die Steuerperiode aufzuteilen; die beschränkte Steuerpflicht wird wegen ihres subsidiären Charakters von der unbeschränkten «absorbiert», es gibt Beginn und Ende auch beim Wechsel der Art. | 7.3, 7.5, 9.3 | gutgeheissen | A | geltend |
| BGer 2A.388/1998 vom 3. Mai 2000 | 3.5.2000 | 3 | Abs. 2 | Wegzug, Freizügigkeitsleistung | Unbeschränkte Steuerpflicht endet mit Tod oder Wegzug; für den Wegzug ins Ausland ist der neue Wohnsitz massgebend, nicht die Abmeldung; Zeitpunkt entscheidet über Steuerhoheit für Kapitalleistung. | 2a, 5a–c | Rückweisung | A | geltend |
| BGer 2A.443/2001 vom 16. Mai 2002 | 16.5.2002 | 3 | Abs. 2 | Wegzug | Abmeldung und Verlassen sind nicht entscheidend; massgebend ist, ob ein neuer Wohnsitz begründet wurde. | 6.1, 6.2 | Rückweisung | B | Pränumerando (Bemessung) |
| BGer 2A.780/2006 vom 31. Oktober 2007 | 31.10.2007 | 3 | Abs. 2 | Tod (altes Bemessungsrecht) | Die Zwischenveranlagung bei Vermögensanfall von Todes wegen folgt daraus, dass die Steuerpflicht des Verstorbenen mit dem Tod endet. | 3.1 | gutgeheissen | C | Pränumerando (überholt) |
| BGer 2C_382/2008 vom 12. November 2008 | 12.11.2008 | 3 | allg. (Zeitpunkt) | Tag des Endes | Wer zu Beginn eines Tages die Voraussetzungen erfüllt, bleibt für den ganzen Tag steuerpflichtig; Tod oder Wohnsitzwechsel im Lauf des Tages beenden die Pflicht erst nach Ablauf dieses Tages (Kirchensteuer, mit Hinweis auf DBG-Lehre). | 4.2 | abgewiesen | B | geltend |
| BGer 2C_355/2010 vom 7. Dezember 2010 | 7.12.2010 | 3 | Abs. 2 | Wegzug, «Weltenbummler» | Abmeldung ohne neuen Wohnsitz beendet die Steuerpflicht nicht. | 3.2, 4.1 | abgewiesen | B | geltend |
| BGer 2C_604/2011 vom 9. Mai 2012 | 9.5.2012 | 3 | Abs. 2 | Ende der unbeschränkten, Fortbestand beschränkter Steuerpflicht | Die unbeschränkte Steuerpflicht endet am Tag des Wegzugs; danach nur noch beschränkte Steuerpflicht; ein Bonus für die Arbeit vor dem Wegzug ist nach Art. 5 Abs. 1 lit. a DBG steuerbar. | 3.1, 5.1, 5.2 | teilweise gutgeheissen | B | geltend |
| BGer 2C_855/2014 vom 11. September 2015 | 11.9.2015 | 3 | Abs. 1 und 2 | Harmonisierung; Wegzug | § 13 StG SO entspricht Art. 8 Abs. 1 und 2 DBG; Rechtsprechung zum DBG übertragbar; rémanence. | 4.1, 4.2 | – | B | geltend |
| BGer 2C_1107/2014 vom 14. September 2015 | 14.9.2015 | 3 | Abs. 1 und 2 | Harmonisierung; Wegzug | Art. 10 StG NW entspricht Art. 8 Abs. 1 und 2 DBG; rémanence. | 4.1, 4.2 | – | B | geltend |
| BGer 2C_873/2014 vom 8. November 2015 | 8.11.2015 | 3 | Abs. 1 und 2 | Harmonisierung; Wegzug | § 10 StG ZH entspricht Art. 8 Abs. 1 und 2 DBG; rémanence. | 3.1, 3.2 | – | B | geltend |
| BGer 2C_498/2016 vom 3. Juni 2016 | 3.6.2016 | 3 | Abs. 2 | Tod, Solidarhaftung | Die Steuerpflicht endet am Todestag; ab dann haftet der überlebende Ehegatte nur noch für seinen Anteil; Aufteilungsverfügung nötig. | 6 | abgewiesen | B | geltend |
| BGer 2C_377/2017 vom 4. Oktober 2017 | 4.10.2017 | 3 | Abs. 2 | Tod, Erben | Steuerpflicht endet mit dem Tod; Erben treten ein (Art. 12 DBG); kein Schutz durch öffentliches Inventar für Steuerforderungen. | 1.3, 2 | abgewiesen | B | geltend |
| BGer 2C_133/2018 vom 21. Februar 2018 | 21.2.2018 | 3 | Abs. 1 | Beginn durch Grundstückerwerb | Beschränkte Steuerpflicht beginnt mit dem Eigentumserwerb (Verfügungsgeschäft), nicht mit Beurkundung oder Besitzantritt; keine Karenzfrist; Beginn der wirtschaftlichen Zugehörigkeit ist bundesrechtliche Frage. | 2.2.2–2.2.4 | abgewiesen | A | geltend |
| BGer 2C_1036/2017 vom 10. März 2019 | 10.3.2019 | 3 | Abs. 1 und 2 | Harmonisierung; Beweislast Wegzug | § 10/11 StG TG entsprechen Art. 8 Abs. 1 und 2 DBG; Wohnsitzverlegung ist von der steuerpflichtigen Person darzulegen. | 2.1–2.3 | – | B | geltend |
| BGer 2C_114/2018 vom 18. Juli 2019 | 18.7.2019 | 3 | Abs. 2 | Wegzug (Dubai) | Für eine Wohnsitzverlegung (Art. 8 Abs. 2 DBG) genügt das Lösen der Verbindungen nicht; der Steuerpflichtige bleibt steuerpflichtig, bis er nachweisbar einen neuen Wohnsitz begründet. | 3.1.2, 3.1.3, 5 | abgewiesen | A | geltend |
| BGer 2C_186/2020 vom 28. Dezember 2020 | 28.12.2020 | 3 | Abs. 2 | Ende des Aufenthalts | Mit dem Verlassen der Schweiz endete der steuerrechtliche Aufenthalt im Sinne von Art. 8 Abs. 2 DBG; keine ganzjährige Steuerpflicht. | 5.1 | teilweise gutgeheissen | A | geltend |
| BGer 9C_54/2026 vom 9. Juni 2026 | 9.6.2026 | 3 | Abs. 2 | Tod, Parteifähigkeit Erben | Erben sind kraft Art. 560 ZGB und Art. 8 Abs. 2 DBG zur Beschwerde legitimiert. | 1.2 | – | C | geltend |
| BGer 9C_448/2025 vom 9. September 2026 | 9.9.2026 | 3 | Abs. 2 | Wegzug; Harmonisierung | Steuerpflicht endet am Tag des Wegzugs; rémanence bis zum neuen Wohnsitz; StHG enthält keine mit Art. 8 Abs. 2 DBG vergleichbare Bestimmung (Art. 8 Abs. 5 LI VD entspricht ihr). | 5.2, 8 | abgewiesen | A | geltend |

Zählung: 21 Entscheide (ohne BGer-Dubletten der BGE); A = 8, B = 11, C = 2.

## Kantonale Entscheide (Entscheidsuche; Auswertung Hilfsagent, Volltexte)

| Entscheid | Sachfrage | E. | Kernaussage |
|---|---|---|---|
| StRK BE 100 2023 21 vom 18.6.2024 | Beginn, Zuzug | 3.5, 3.7 | Beginn an dem Tag, an dem sich die Wohnsitzkriterien verwirklichen; nicht Grenzübertritt oder Anmeldung. |
| StRG ZH DB.2025.90 vom 31.3.2026 | Beginn; Wechsel | 1a/bb, 3b | Beginn am ersten Tag der Wohnsitznahme bzw. des Aufenthalts; nach 9C_416/2024 zwei Veranlagungen. |
| VGer ZH SB.2019.00094 vom 8.1.2020 | Aufenthalt | 2.4.1 | Aufenthalt: Steuerpflicht pro rata für die Zeit des Aufenthalts; Unterbrüche zählen mit; vom BGer (2C_186/2020) teilweise korrigiert. |
| VGer AG WBE.2023.189 vom 29.5.2024 | Grundstückerwerb | II/4.2 | Beginn mit Grundbucheintrag; gestützt auf 2C_133/2018. |
| StRG ZH ST.2016.82 vom 28.6.2017 | Erwerb/Verkauf Liegenschaft | 2 | Erwerb und Verkauf durch im Ausland Wohnhafte begründen bzw. beenden unterjährige beschränkte Steuerpflicht. |
| TAPI GE A/615/2021 vom 1.11.2021 | Wegfall | 10 | Ende der wirtschaftlichen Zugehörigkeit mit Grundbucheintrag des Verkaufs. |
| StRG ZH DB.2011.247 vom 27.1.2012 | Wegzug, Kapitalleistung | 1b, 3g, 6a | Abmeldung nur Indiz; Kapitalleistung vor Wegzug fällig → ordentliche Besteuerung. |
| VGer ZH SR.2015.00021 vom 11.5.2016 | Wegzug | 3.2.2 | Ohne Nachweis neuer Wohnsitz besteht Domizil fort. |
| VGer ZH SB.2017.00045 vom 18.4.2018 | Wegzug Ehegatte | 4.3.1 | Arbeitsort im Ausland ohne regelmässige Rückkehr begründet noch keinen ausländischen Wohnsitz. |
| KGer BL 810 15 71 vom 30.9.2015 | Wegzug | 6.2 | Hotelaufenthalte am Arbeitsort begründen keinen Wohnsitz. |
| CDT TI 80.2007.25 vom 26.2.2008; 80.2015.25 vom 3.3.2016; 80.2019.281 vom 5.10.2020; 80.2009.81 vom 21.4.2010 | Wegzug, Ehegatten | 1.2; 3.2; 2.3; 3.2 | Abmeldung ohne Wirkung; Steuer geschuldet bis zum Nachweis eines neuen Wohnsitzes. |
| TC NE CDP.2010.228 vom 27.6.2011 | Wegzug | 3c | Abmeldung blosses Indiz. |
| CDAP VD FI.2010.0061 vom 16.12.2010; FI.2016.0067 vom 3.10.2016; FI.2024.0126 vom 3.7.2025 | Wegzug, Beweis | 2b; 4c; 4d | rémanence; nach akzeptiertem Wegzug trägt der Fisk Beweislast für Rückkehr; Pflichtige beweisen Ende und Datum. |
| CJ GE ATA/397/2015 vom 28.4.2015 | Begriff «Wegzug» | 4 | «départ de Suisse» umfasst Ende des Aufenthalts und Wohnsitzverlegung. |
| TAPI GE A/1633/2023 vom 27.5.2024 | Wegzug, Vermögen | 7 | Vermögen am Wegzugstag festgestellt. |
| StG SO SGSTA.2017.44 vom 23.10.2017; VGer TG VG.2015.144 vom 2.12.2015 | Wegzug, Auslandeinsätze | 3.2; 2.3 | Massgebend ist Begründung eines neuen Wohnsitzes, nicht Dauer im Ausland. |
| StRG ZH DB.2012.191 vom 4.12.2012 | Rückkehr | 4d | Nach Entlassung aus der Steuerpflicht muss die Behörde die Rückverlegung beweisen. |
| VGer GR A 07 56 vom 4.3.2008 (PVG 2008 Nr. 14) | Tod Ehegatte | 3 | Tod: Ende der gemeinsamen, Beginn neuer Steuerpflicht des Überlebenden. |
| SVG AG 3-BB.2023.9 vom 19.12.2024 | Tod, Erben | 4.2.1 | Steuerpflicht des Erblassers endet; Erben einzeln zu veranlagen. |
| StG SO SGSTA.2010.54 vom 11.4.2011 | Tod | 2 | Mit dem Tod enden Rechtspersönlichkeit und subjektive Steuerpflicht. |
| StG BL 049/2008 vom 27.6.2008; KGer BL 810 08 359 vom 17.6.2009 | Konkurs | 3e; 4.1 | Konkurs ist kein Beginn/Ende der Steuerpflicht; abschliessender Katalog. |
| CDAP VD FI.2022.0151 vom 1.6.2023; FI.2023.0121 vom 8.7.2024 (aufgehoben durch 9C_416/2024) | Wechsel | 5c; 8b | Einheitsmethode; überholt durch BGE 152 II 98. |
| StRG ZH DB.2017.109 vom 18.4.2018 | Wegzug mit Liegenschaft | 3b/bb, 4b | Zürcher Praxis: ungeteilte Periode bei fortbestehender beschränkter Steuerpflicht. |
| VGer ZH SB.2004.00054 vom 20.10.2004 | Wechsel (kantonal, altes Recht) | 3.3.1 | Ende der unbeschränkten bei fortbestehender beschränkter Steuerpflicht gilt als Beendigung. |
| StRG ZH DB.2019.31 vom 28.1.2020 | Liquidation | 5c | interkantonal, für Art. 8 nur am Rand. |

## Nachtrag 27.10.2026 (ILE-Lauf)

| Entscheid | Datum | Besetzung | Normstelle | Sachfrage | Kernaussage (ein Satz) | E. | Ergebnis | Klasse | Fassung |
|---|---|---|---|---|---|---|---|---|---|
| BGE 149 II 177 (= BGer 9C_689/2022 vom 12. April 2023) | 12.4.2023 | – | Art. 40 Abs. 3 (Art. 209 Abs. 3 aDBG) i.V.m. Art. 8 | Satzbestimmung bei beschränkter Steuerpflicht | Die Umrechnung auf zwölf Monate gilt, wenn die unbeschränkte Steuerpflicht im Lauf der Periode entsteht oder endet; bei bloss beschränkter Steuerpflicht ist sie von vornherein ausgeschlossen. | 8.3.5 | – | B | aDBG (Quellensteuer bis 2020); Aussage zu Art. 40 Abs. 3 geltend |

Herkunft: Besprechung Oesterhelt/Opel, FStR 2023/3, Ziff. 3 (Fn. 29); Zitierstring und Erwägung über Open Case Law (`cite`, `find_relevant_erwaegung`) geprüft.
