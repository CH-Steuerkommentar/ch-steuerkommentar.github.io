# Art. 7 DBG – Kantonale Rechtsprechung, BVGer und Lehre

Stand: 26.10.2026. Gesucht wurde mit Open Case Law (search_decisions, get_decision, get_erwaegung, find_relevant_erwaegung, cite, search_scholarship, get_scholarship_full_text, find_scholarship_citing_statute, get_commentary) und mit Entscheidsuche (search, fetch_document). Lexplorer Tax war nach einem Suchversuch gesperrt (Monatskontingent 500/500 erreicht). Zwei FStR-Beiträge wurden deshalb nur über die Navigation gefunden und gelesen (siehe Lexplorer_Fundstellen.md).

## Hinweise zur Verwendung

- **Zitierstrings:** Alle Zitierstrings stammen aus Tool-Ergebnissen (`citation_string_de`). Bei drei Entscheiden stimmt das Datum im Tool-Zitierstring nicht mit dem Urteilsdatum im Volltext überein. Vor der Übernahme ins Werk ist das Datum am Original zu prüfen:
  - **«Steuerrekursgericht ZH ST.2016.82 vom 24. September 2015»:** Der Volltext nennt als Entscheiddatum den 28. Juni 2017. Der 24.9.2015 ist das Datum des Einschätzungsentscheids.
  - **«Verwaltungsgericht ZH SB.2019.00098 vom 10. September 2018»:** Laut Volltext ist es ein Urteil des Einzelrichters vom 2. Dezember 2019.
  - **«Gericht SO SGSTA.2018.39 vom 28. Mai 2018»:** Laut Volltext ist es ein Urteil vom 5. November 2018. Der 28.5.2018 ist das Datum des Einspracheentscheids.
- **Standardkommentare:** Zweifel/Beusch (Oesterhelt/Schreiber), Locher, Richner et al., Agner/Jung/Steinmann und CR-LIFD (Paschoud/de Vries Reilingh) wurden **nicht im Volltext gelesen**. Sie erscheinen hier nur als «zitiert in» einem Entscheid. Vor einer Verwendung ist jede dieser Stellen am Original zu prüfen.
- **Onlinekommentar (onlinekommentar.ch):** Für Art. 6 oder Art. 7 DBG gibt es keine Kommentierung. Zum DBG bestehen nur Kommentierungen zu Art. 10 und Art. 11 (Grieder/Hongler, Stand 18.5.2026) und zu Art. 174 (Fawer/Hongler). Geprüft wurde über die API-Liste (https://onlinekommentar.ch/api/commentaries?search=DBG) und über get_commentary. Für Art. 7 ist nur Art. 11 DBG N 9 f. als Abgrenzung relevant, siehe (b).
- **Lehrbuch Hongler/Lorenz (ILE-Lehrbuch):** wurde nicht verwendet.

---

## (a) Satzbestimmendes Gesamteinkommen: weltweites Einkommen nach Schweizer Regeln, Mitwirkung, Ermessensveranlagung

### Kantonale Rechtsprechung

1. **Gericht VS F1 24 83 vom 30. Juni 2024** (Kantonsgericht Wallis, Steuerrechtliche Abteilung; ob weitergezogen, ist unbekannt). URL: https://mcp.opencaselaw.ch/entscheid/vs_gerichte_F1%2024%2083; Original: https://api-justsearche.vs.ch/api/documents/90f4549f0bb8076cc011f694c1eb21f7/
   - *Sachverhalt:* Eine Rentnerin mit Wohnsitz in London besitzt ein Studio im Wallis. Sie reichte keine vollständige Steuererklärung und keine Belege ein. Das satzbestimmende Einkommen wurde gebildet aus dem «income received» laut HMRC-Auszug plus dem schweizerischen Nettoliegenschaftsertrag («konstante Praxis»). Das satzbestimmende Vermögen wurde nach Ermessen auf CHF 2 Mio. festgesetzt («Maximalsteuersatz»). Der Sonderabzug wurde nur zu 1/10 gewährt, nach «kantonale[r] Praxis in Fällen, in denen eine internationale Steuerausscheidung mangels Angaben nicht möglich sei».
   - *E. 4.2 (Standpunkt der Steuerverwaltung):* «Art. 7 Abs. 1 DBG sehe vor, dass sich der Fiskus ein umfassendes Bild der finanziellen Verhältnisse der Steuerpflichtigen mache. Er habe für die Bestimmung des Steuersatzes nach dem Prinzip des Progressionsvorbehalts alle steuerbaren inländischen und ausländischen Einkommensbestandteile zu ermitteln. Auch eine Auflistung sämtlicher Vermögenswerte im In- und Ausland sei erforderlich.»
   - *E. 4.2.3 (Gericht):* «Für die Bemessung dieser wirtschaftlichen Leistungsfähigkeit ist immer das Steuerobjekt in seiner Gesamtheit zu berücksichtigen, auch wenn es auf mehrere Steuerhoheiten aufgeteilt ist» (mit Verweis auf Cadosch, Kommentar DBG, 2. A. 2008, S. 29).
   - *E. 4.3.4:* Liefert die Behörde genügende Indizien (hier den HMRC-Auszug), muss die steuerpflichtige Person beweisen, dass ihre Angaben stimmen. Die Ermessensveranlagung des satzbestimmenden Vermögens war zulässig. *E. 5.3:* Das Vorgehen ist nicht rechtsmissbräuchlich.
2. **Verwaltungsgericht ZH SB.2019.00098** (Tool-Datum «10. September 2018»; laut Volltext Urteil des Einzelrichters vom 2.12.2019; rechtskräftig). URL: https://mcp.opencaselaw.ch/entscheid/zh_verwaltungsgericht__SB.2019.00098
   - *E. 3.2:* «Der Pflichtige ist aufgrund seiner Liegenschaft in der Stadt D hier beschränkt steuerpflichtig (§ 4 Abs. 1 lit. b StG), wobei zur Satzbestimmung sein gesamtes Einkommen und Vermögen beizuziehen ist (§ 6 Abs. 1 StG).»
   - *E. 3.5:* Angefochten war eine Ermessenseinschätzung. Es «fehlt [...] an einer wahrheitsgetreuen Auflistung der weltweiten Vermögenswerte». Die Begründungsanforderungen nach § 140 Abs. 2 StG ZH waren nicht erfüllt.
3. **Verwaltungsgericht ZH SB.2025.00054 vom 6. Mai 2026** (Beschwerde ans BGer hängig). URL: https://mcp.opencaselaw.ch/entscheid/zh_verwaltungsgericht_SB.2025.00054
   - *E. 5.5.2:* Das satzbestimmende Vermögen wurde nach Ermessen geschätzt; die Schätzung ist nicht willkürlich. Hypothekarschulden, die der Behörde nicht bekannt waren, musste sie nicht berücksichtigen: «Steuermindernde Tatsachen werden nur nach pflichtgemässem Ermessen geschätzt, wenn der Grundsachverhalt hinsichtlich der steuermindernden Tatsachen bewiesen ist, aber Unklarheit über den Umfang besteht».
   - *E. 5.8 (DBG):* Wer nur interkantonal verbunden ist, hat bei der direkten Bundessteuer kein vom steuerbaren abweichendes satzbestimmendes Einkommen. Es «ergeben sich keine Hinweise dafür, dass [...] auf Geschäftsbetriebe, Betriebsstätten und Grundstücke im Ausland entfallende Erträge vorgelegen hätten, welche satzbestimmend zu berücksichtigen gewesen wären (vgl. Art. 7 Abs. 1 DBG)».
4. **Verwaltungsgericht ZH SB.2017.00103 vom 21. Februar 2018** (BGer-Beschwerde abgewiesen, siehe (b)). *E. 3.3.1:* Das Belegprinzip gilt auch für Auslandverluste, «soweit die steuerpflichtige Person ihre Auslandverluste in der Schweiz bei den (satzbestimmenden) Steuerfaktoren in Anrechnung bringen will». Fehlt die Dokumentation, ist «die daraus resultierende Beweislosigkeit durch die steuerpflichtige Person zu tragen». *E. 3.5:* «Während bei der Steuerfestsetzung bzw. Satzbestimmung unzureichend belegte Geschäftsverluste nicht akzeptiert werden müssen, ist es den Steuerbehörden nicht verwehrt, bei steuerbegründenden Faktoren auf die Angaben des Steuerpflichtigen abzustellen».
5. **Gericht GE A/4933/2008 vom 5. Mai 2010** (Commission cantonale de recours en matière administrative, DCCR/640/2010; das kanonische Record ist ge_gerichte_DCCR_640_2010; Rekurs gutgeheissen). URL: https://mcp.opencaselaw.ch/entscheid/ge_gerichte_A_4933_2008; PDF: https://justice.ge.ch/apps/decis/fr/dccr/file/2010/0006/DCCR_000640_2010_A_4933_2008.pdf
   - *Consid. 3:* Die Genfer Praxis wendet den Maximalsatz an, wenn das Gesamteinkommen nicht deklariert wird (Information AFC-GE N° 9/2003): «soit le contribuable domicilié à l'étranger déclare l'ensemble de ses revenus et de sa fortune [...], soit il refuse de déclarer l'ensemble de ces éléments auquel cas l'administration a recours au taux maximum prévu par la loi».
   - *Consid. 4:* «on ne peut pas demander au contribuable de prouver un fait négatif, c'est-à-dire qu'il n'a pas d'autres revenus que ceux annoncés».
   - *Consid. 5:* Hat der Fiskus Zweifel, muss er zuerst nachfragen. Erst «[e]n cas de silence du contribuable ou de refus sans motif de répondre, le fisc aurait été autorisé à appliquer le taux maximum.» Auslandeinkünfte vor Beginn der Steuerpflicht (Art. 8 DBG) sind für den Satz nicht massgebend.
   - *Consid. 7:* Die Belastung beim Maximalsatz darf jene einer Person, die genügend hohe Auslandfaktoren deklariert hätte, nicht übersteigen. Deshalb gelten trotzdem der Verheiratetentarif (Art. 214 Abs. 2 aDBG) und der Kinderabzug.
6. **Gericht GE ATA/1385/2017 vom 10. Oktober 2017** (A/1511/2015). Bestätigt durch **BGer 2C_980/2017 vom 28. Juni 2018**. URL: https://mcp.opencaselaw.ch/entscheid/ge_gerichte_ATA_1385_2017. Zur «procédure simplifiée» siehe (d). *Consid. 3:* Die Deklarationspflicht gilt auch für beschränkt Steuerpflichtige: «Tous les éléments du revenu, du bénéfice, de la fortune ou du capital, qu'ils soient imposable ou non doivent être déclarés (art. 124 al. 2 LIFD)».
7. **Gericht GE ATA/787/1997 vom 23. Dezember 1997** (altes kantonales Recht, LCP). URL: https://mcp.opencaselaw.ch/entscheid/ge_gerichte_ATA_787_1997. Regeste: «Le taux maximum du barème est appliqué à celui qui refuse de communiquer les éléments de ses revenus et de sa fortune.»
8. **Gericht AG WBE.2017.220 vom 3. Juli 2017** (AGVE 2017 Nr. 15). *E. 2.2.3.1:* «Soweit der beschränkt Steuerpflichtige bei der Ermittlung der Bemessungsgrundlagen nicht mitwirkt, steht im Übrigen [...] ebenso wie bei den unbeschränkt Steuerpflichtigen das Instrument der Ermessensveranlagung offen.» Ausländische Liegenschafts- und Renteneinkünfte lassen sich «in aller Regel anhand einfacher, aussagekräftiger Dokumente belegen». Einzelheiten unter (d).

### BVGer

- **BVGer A-4994/2022 vom 2. Mai 2023** (Amtshilfe mit Spanien; nur am Rand einschlägig). In E. 5.1 trug der Beschwerdeführer vor: «Sofern für die Zwecke der Satzbestimmung nach nationalem spanischem Steuerrecht auf das weltweite Einkommen oder Vermögen abzustellen sei, könne ohne weiteres der Höchstsatz verwendet werden, ohne dass die Dokumentation der effektiven Werte erforderlich sei.» Das BVGer folgte dem nicht (E. 5.2.2): Angaben zu Steuerstatus und Einkünften in der Schweiz sind für die Untersuchung einer beschränkten Steuerpflicht in Spanien voraussichtlich erheblich. URL: https://mcp.opencaselaw.ch/entscheid/bvger_A-4994_2022#e-5-2-2
- In BVGer-Entscheiden gibt es sonst keine Treffer zu Art. 7 DBG im Steuerrecht. Die übrigen Treffer betreffen Direktzahlungen (BVGE 2008/22, B-1456/2007, B-7200/2015) und AHV.

### Lehre

- **Komor, Gewinnungskosten (Diss. Bern 2020), S. 178:** «Das satzbestimmende Einkommen von unbeschränkt steuerpflichtigen natürlichen Personen ist immer das weltweite Einkommen und dieses wird nach den Grundsätzen des schweizerischen Steuerrechts ermittelt. Hierbei sind sowohl ausländische Einnahmen als auch ausländische Verluste zu berücksichtigen.» (Fn. 809 verweist auf Oesterhelt/Schreiber, Art. 7 N 5 f.)
- **Komor, a.a.O., S. 178 f.:** Ausländische Liegenschaftssteuern, die als Objektsteuern ausgestaltet sind (z.B. kanadische «taxes municipales»), sind nach Schweizer Recht als Unterhalt abzuziehen und werden nur satzbestimmend berücksichtigt. Hinweis auf VGr ZH SB.2007.98 vom 5.3.2008, ZStP 2008, 145.
- **Brülisauer/Kriesi, FStR 2008/1 (Lexplorer), Abschn. 3.1.2.3 und 3.2.2.3:** Wer als einziger ausländischer Teilhaber eine schweizerische Personengesellschaft hält, ist beschränkt steuerpflichtig: «Dies bedeutet u. a., dass er in der Schweiz eine Steuererklärung einzureichen hat, in der er - zwecks Satzbestimmung - sein weltweites Einkommen (und Vermögen) anzugeben hat.»

---

## (b) Ausländische Verluste im satzbestimmenden Einkommen, Verlustvortrag

### Kantonale Rechtsprechung

1. **Verwaltungsgericht ZH SB.2017.00103 vom 21. Februar 2018** (Gewichtung 2). URL: https://mcp.opencaselaw.ch/entscheid/zh_verwaltungsgericht__SB.2017.00103
   - *Sachverhalt:* Wohnsitz in der Dominikanischen Republik, Grundeigentum im Kanton Zürich, Verluste aus einem Hotelbetrieb im Ausland.
   - *E. 2.2:* § 6 Abs. 2 StG ZH nennt die Grundstücke nicht. Das ist nach dem Gericht «offensichtlich [...] ein gesetzgeberisches Versehen» (gegen Richner et al., Komm. StG ZH, § 6 N 2). Zum Zweck der Norm: «Sinn und Zweck der Bestimmungen von Art. 7 Abs. 2 DBG ist, dass ausländische Verluste ohnehin nicht überprüft werden könnten und deshalb auch nicht zur Satzbestimmung beizuziehen seien (vgl. die Botschaft des Bundesrats zum DBG, BBl 1983 III 158; [...] Oesterhelt/Schreiber, Art. 7 DBG N. 14).» Ergebnis: «Auslandverluste sind damit bei einer [...] beschränkten Steuerpflicht in der Schweiz generell nur im Rahmen der Satzbestimmung und nur unter Ausschluss des negativen Progressionsvorbehalts zu berücksichtigen.»
   - *E. 2.3:* Abziehbar wären die Auslandverluste nur beim satzbestimmenden, nicht beim steuerbaren Einkommen, und erst wenn die selbständige Erwerbstätigkeit nachgewiesen ist.
   - *E. 2.1:* Die Regel in Rz 19 des Merkblatts ZStB Nr. 49.3, wonach Verluste beim steuerbaren und beim satzbestimmenden Einkommen zu berücksichtigen sind, gilt nur bei unterjährigen Wechseln der Steuerpflicht.
   - **Weiterzug:** **BGer 2C_295/2018 vom 6. Februar 2019** (Beschwerde abgewiesen). Das BGer bestätigte nur den fehlenden Nachweis und liess die Frage zu Art. 7 Abs. 2 DBG ausdrücklich offen. *E. 6* (wörtlich): «Ferner erübrigen sich Ausführungen zur Frage, ob der Auslandsverlust im Nebensteuerdomizil anzurechnen oder nur satzbestimmend zu berücksichtigen wäre.»
2. **Gericht AG 3-RV.2021.197 vom 21. Dezember 2023** (Spezialverwaltungsgericht, Abteilung Steuern; ob weitergezogen, ist unbekannt). URL: https://mcp.opencaselaw.ch/entscheid/ag_spezialverwaltungsgericht_3-RV.2021.197
   - *Sachverhalt:* Ein Arzt mit Wohnsitz in Deutschland führt eine Praxis im Aargau. Seine deutschen Liegenschaftsverluste (CHF 244'136) wurden bei der Satzbestimmung nicht berücksichtigt, das Vermögen dagegen zum Gesamtsatz besteuert.
   - Der Einwand des Methodendualismus wurde verworfen. Ebenso wurden die Rügen nach Art. 25 Abs. 1 DBA CH-D, Art. 2 und 21 Abs. 2 FZA und Art. 8 BV abgewiesen.
   - *E. 4.2* gibt WBE.2017.220 E. 1 wieder: «Danach bleiben bei der Besteuerung beschränkt Steuerpflichtiger Auslandsverluste unberücksichtigt und wird mindestens das im Inland erzielte Einkommen der Besteuerung unterworfen (Ausschluss des negativen Progressionsvorbehalts; [...] Athanas/Giglio [...] § 19 N 6; [...] Oesterhelt/Schreiber [...] Art. 7 N 14). Ergibt sich aus der Anwendung des Progressionsvorbehalts ein höherer Steuersatz, so ist dieser höhere Steuersatz zur Anwendung zu bringen».
   - *E. 5.1:* «Die Berechnung des satzbestimmenden Einkommens und Vermögens gemäss § 19 Abs. 2 StG erfolgt jedoch unabhängig von der Staatsangehörigkeit der Steuerpflichtigen.»
   - *E. 2.2.1 (Standpunkt KStA):* Die Quasi-Ansässigkeit wurde verneint, weil nur 77 % der weltweiten Einkünfte in der Schweiz steuerbar waren (Schwelle 90 %).
3. **Steuerrekurskommission BS STRK.2023.65 vom 21. März 2024.** URL: https://mcp.opencaselaw.ch/entscheid/bs_steuerrekurskommission_STRK.2023.65
   - *Sachverhalt:* Wohnsitz in London, Grundstück in Basel-Stadt. Wegen der Liegenschaftskosten in London war das satzbestimmende Einkommen negativ bzw. null.
   - *E. 4c* (zum DBG, obiter): «Diese Bestimmung ist als Minimalsteuer formuliert»; «Damit wird auch die satzbestimmende Berücksichtigung von Auslandverlusten ausgeschlossen»; «Aufgrund des klaren Wortlauts der Bestimmung von Art. 7 Abs. 2 DBG ist diese Minimalsteuer bei der direkten Bundessteuer grundsätzlich anzuwenden.»
   - Für die Kantonssteuer fehlt in § 7 StG BS eine Minimalsteuer. Der Satz beträgt deshalb 0 % (Legalitätsprinzip, E. 4f, 5).
4. **Gericht GR A 2016 31 vom 22. März 2017** (Verwaltungsgericht GR, Einzelrichter). Bestätigt durch **BGer 2C_404/2017 vom 10. Mai 2017** (abgewiesen). URL: https://mcp.opencaselaw.ch/entscheid/gr_gerichte_A_2016_31
   - *Sachverhalt:* Wohnsitz in Graubünden, Liegenschaft in Frankreich. Ein Gewinnungskostenüberschuss von CHF 9'974 wurde nur satzbestimmend berücksichtigt.
   - *E. 2b:* Die Freistellung mit Progressionsvorbehalt «gilt unbedingt, d.h. unabhängig davon, ob der Partnerstaat seine Besteuerungsbefugnis effektiv ausschöpft».
   - *E. 3:* «Gemäss Art. 6 Abs. 3 Satz 2 und Art. 52 Abs. 3 Satz 2 [DBG] sind Auslandsverluste von Geschäftsbetrieben, Betriebsstätten und Grundstücken nicht abzugsfähig, sondern ausschliesslich satzbestimmend zu berücksichtigen [...]. Dabei handelt es sich um eine bundesrechtliche Konkretisierung der vorerwähnten Freistellungsmethode mit Progressionsvorbehalt (vgl. BGE 140 II 157 [...] E.2.3).»
5. **Gericht BL 530 16 19 vom 12. August 2016** (Steuergericht BL, Präsident; DBG 2013). URL: https://mcp.opencaselaw.ch/entscheid/bl_gerichte_530_16_19
   - *E. 2b:* «Entsteht ein Gewinnungskostenüberschuss im Ausland, kann dieser von der schweizerischen Bemessungsgrundlage nicht in Abzug gebracht werden, wird bei der Ermittlung des Steuersatzes aber berücksichtigt. Dasselbe gilt für Schuldzinsenüberschüsse, welche nur vom satzbestimmenden Einkommen in Abzug gebracht werden können.»
   - Ähnlich, aber nicht im Volltext gelesen: BL 530 14 33 vom 6.3.2015 (Eigenmietwert/Unterhalt USA) und BL 2017-09-22-stger-2 (Eigenmietwert ausländische Liegenschaft).
6. **Genf:** Bei Liegenschaften in Frankreich wird der Aufwand- bzw. Schuldzinsüberschuss nur beim Satz berücksichtigt («uniquement pour celle du taux de l'impôt»). Belegt durch die Regesten (nur diese wurden gelesen) von:
   - **Gericht GE A/4074/2010 vom 8. Mai 2012** (ATA/288/2012; BGer 2C_585/2012 abgewiesen),
   - **Gericht GE A/4231/2010 vom 21. August 2012** (ATA/551/2012; BGer 2C_960/2012),
   - **Gericht GE A/1456/2011 vom 14. Januar 2014** (ATA/23/2014; BGer 2C_198/2014),
   - **Gericht GE A/1065/2012 vom 7. Januar 2014** (ATA/8/2014; BGer 2C_148/2014).

### Lehre

- **Komor, Diss. Bern 2020, S. 179 f.:** «Bei der direkten Bundessteuer kann daher ein Gewinnungskostenüberschuss über die Einkünfte aus der ausländischen Liegenschaft von der schweizerischen Bemessungsgrundlage nicht abgezogen, sondern bloss bei der Steuersatzbestimmung berücksichtigt werden.» In Fn. 812 verweist er auf BGE 140 II 141 E. 5.3, 2C_404/2017, 2C_891/2018 u.a. und auf die Kritik von Marantelli, in: Marantelli/Opel, Rechtsprechung Bundesgericht 2014, S. 177 ff.
- **De Vries Reilingh, Diss. Neuchâtel 2010, S. 272 f. N 651:** «Ainsi, en cas de perte provenant d'une activité lucrative indépendante exercée à l'étranger, le taux d'impôt peut être de zéro, ce qui conduit, indirectement, à une prise en compte de la perte étrangère par le biais de l'application du principe du taux global.»
- **De Vries Reilingh, a.a.O., S. 297 N 712 und S. 302 N 722:** Ausserhalb von Betriebsstätten übernimmt die Schweiz keine Auslandverluste. Er kritisiert diese «perte de répartition» als «très insatisfaisant».
- **Brülisauer/Kriesi, FStR 2008/1 (Lexplorer), Abschn. 3.2.1.1 (Fall 6):** «Allerdings ist der Auslandsverlust gestützt auf Art. 6 Abs. 3 Satz 3 DBG in der Schweiz satzbestimmend zu berücksichtigen.»
- **Brülisauer/Kriesi, a.a.O., Abschn. 3.1.2.2 (Fall 4):** Bei beschränkter Steuerpflicht ist kein Verlusttransfer möglich. Er stünde «im Widerspruch zu Art. 6 Abs. 2 Satz 2 DBG».
- **Ausländische Personengesellschaften:**
  - **Steuerrekursgericht ZH DB.2012.287 vom 25. März 2013:** Eine deutsche GmbH & Co. KG, die nur Beteiligungen hält, ist eine nichtkaufmännische Personengesellschaft. Die Erträge sind beim Gesellschafter in der Schweiz steuerbar. Nur die Regeste wurde gelesen.
  - **Kollruss, sui generis 2021, S. 309 f. N 11, 15 mit Fn. 44:** Hält eine in Deutschland ansässige Person eine schweizerische Betriebsstätte über eine GmbH & Co. KG, wird diese in der Schweiz nach Art. 11 DBG wie eine juristische Person besteuert. In Deutschland wird ein Verlust der Schweizer Betriebsstätte dagegen über den negativen Progressionsvorbehalt berücksichtigt.
- **Abgrenzung nach Onlinekommentar Grieder/Hongler, Art. 11 DBG N 9 f.:** Eine ausländische Personengesamtheit mit wirtschaftlicher Zugehörigkeit wird «wie eine juristische Person intransparent behandelt»; dann ist Art. 7 DBG nicht anwendbar. Teilweise werden ausländische Teilhaber auch anteilig besteuert (Baselbieter Steuerbuch). https://onlinekommentar.ch/de/kommentare/dbg11

---

## (c) Verlegung bzw. Zuordnung von Abzügen

### Kantonale Rechtsprechung

1. **Verwaltungsgericht ZH SB.2011.00037 vom 21. September 2011** (rechtskräftig, Gewichtung 2). URL: https://mcp.opencaselaw.ch/entscheid/zh_verwaltungsgericht__SB.2011.00037
   - *E. 3.1:* Der Begriff «steuerfreie Beträge» umfasst «alle Abzüge, die nicht als Gewinnungskosten organisch mit bestimmten Einkünften verknüpft und kollisionsrechtlich folgerichtig diesen objektmässig zuzuweisen sind [...], sondern als 'allgemeine Abzüge' anorganischen Charakter aufweisen und daher auf die beteiligten Gemeinwesen proportional verlegt werden müssen».
   - *E. 3.2:* Zuerst werden die Gewinnungskosten objektmässig zugewiesen, danach die übrigen Abzüge proportional (hier 60,88/39,12).
   - *E. 3.2.1:* Die AHV-Beiträge proportional zuzuweisen ist «sachgerecht».
   - *E. 3.2.2.1:* Die Säule 3a sei «ausschliesslich dem in der Schweiz steuerbaren Einkommen zuzuweisen». **Überholt** durch BGer 2C_95/2015 (siehe Nr. 3).
   - *E. 3.2.2.3:* Versicherungsprämien, gemeinnützige Zuwendungen und Kinderabzug werden proportional verlegt.
   - *E. 2.2:* Eine Ausscheidung ist auch ausserhalb von Geschäftsbetrieb, Betriebsstätte und Grundstück möglich (Künstlerin, Art. 17 OECD-MA).
2. **Steuerrekursgericht ZH DB.2013.239 vom 4. März 2014.** PDF: https://www.strgzh.ch/assets/entscheide/StRG_DB_2013_239_ur.pdf
   - *E. 2a:* «Für das Bundesrecht schreibt Art. 7 Abs. 1 DBG indessen allgemein den Grundsatz der unbedingten Befreiung mit Progressionsvorbehalt vor. Die Bestimmung ist offen formuliert; es besteht deshalb kein Grund, den Anwendungsbereich nur auf die in Art. 6 DBG erwähnten Fälle einzuschränken; vielmehr gilt der Grundsatz auch dann, wenn ein Doppelbesteuerungsabkommen die Freistellung vorschreibt (Locher, Art. 7 N 6 DBG).» Weiter: «[...] bestehen demnach gesetzliche Grundlagen zur Vornahme einer Verlegung von Abzügen bei internationalen Verhältnissen». Hingewiesen wird auf Art. 213 Abs. 3 i.V.m. Art. 208 aDBG (Sozialabzüge anteilig; heute Art. 35 Abs. 2 DBG).
   - *E. 2b/2c:* AHV- und BVG-Beiträge (auch Einkäufe) folgen dem Erwerbseinkommen, wenn das ausländische Einkommen versichert war (Betschart, Komm. IntkStR 2011, § 24 N 12 f.).
3. **Steuerrekursgericht ZH DB.2017.109 vom 18. April 2018.** PDF: https://www.strgzh.ch/assets/entscheide/StRG_DB_2017_109_ju.pdf
   - *E. 2a/b:* Überblick über die Zürcher Praxis. **BGer 2C_95/2015 + 96/2015 vom 27.8.2015** hat entschieden, dass 2.-Säule-Einkäufe und Säule-3a-Beiträge anteilig nach Erwerbseinkommen verlegt werden. Wiedergabe: «Es wäre aber inkonsequent und würde die Schweiz benachteiligen, wenn die vollen Abzüge in der Schweiz zulässig wären, die Einkommen aber nur teilweise in der Schweiz erfasst würden.»
   - *E. 3b/aa:* Bei bloss unterjähriger Steuerpflicht (Art. 40 DBG) sind die Abzüge dagegen voll zulässig. Begründung: «Der schweizerische bzw. zürcherische Steuerhoheitsträger ist daher grundsätzlich nicht befugt, vom Steuerpflichtigen Auskünfte zu Steuerfaktoren einzufordern, welche sich ausserhalb der unterjährigen lokalen Steuerpflicht verwirklicht haben.»
   - *E. 6:* Art. 28 Abs. 3 DBA-DK (Vorsorgebeiträge).
4. **Schuldzinsen und Schulden:** Verlegt wird proportional nach Lage der Aktiven, auch bei beschränkter Steuerpflicht.
   - **Verwaltungsgericht ZH SB.2019.00098, E. 3.2** (mit BGer 2A.36/2007 und 2C_18/2014 E. 2.2.2 und E. 4). *E. 3.5:* Die Hypothekarschuld ist «nicht etwa objektmässig allein der Zürcher Liegenschaft zuzuordnen».
   - **Gericht BL 530 16 19, E. 2b:** «Schulden werden gemäss den interkantonalen Grundsätzen nach Lage der Gesamtaktiven verlegt, Schuldzinsen im Verhältnis der Vermögenserträge».
   - **Verwaltungsgericht AG WBE.2017.220, E. 2.3:** § 18 Abs. 3 StG AG schreibe «auch im Verhältnis zum Ausland die Verlegung von Schulden und Schuldzinsen nach der proportionalen Methode» vor; die objektmässige Ausscheidung führe nicht per se zu tieferen Steuern.
   - Bundesgerichtlich gestützt durch **BGer 2C_980/2017 vom 28. Juni 2018, E. 4.2** (GE-Fall): Schuldzinsen sind «répartis de manière proportionnelle en fonction des actifs localisés».
5. **Berufskosten:**
   - **Verwaltungsgericht SG B 2019/83, B 2019/85 vom 18. September 2019:** Wohn- und Flugkosten USA als Berufskosten; Veranlagung «zum Satz von CHF 65'700». Nur das Snippet wurde gelesen; vor Verwendung ist der Volltext zu prüfen.
   - **Lehre:** De Vries Reilingh, Diss. 2010, S. 273 f. N 653–655 (BGer 9.12.1996, ASA 67, 551): Gewinnungskosten eines Grenzgängers aus Italien werden objektmässig und nicht proportional zugeordnet.

### Lehre

- **Komor, Diss. 2020, S. 179:** Unterhaltskosten werden im internationalen Verhältnis objektmässig verlegt. Fn. 811 verweist auf Senn, Liegenschaft im interkant. und internat. Steuerrecht, S. 108 ff., und auf BGer 2C_404/2017 E. 3.2.1.
- Betschart, in: Kommentar zum Schweizerischen Steuerrecht, Interkantonales Steuerrecht, 2011, § 24 N 9, 12 f., 38: zitiert in SB.2011.00037 und DB.2013.239; nicht im Original gelesen.

---

## (d) Abs. 2: Mindestsatz bei Wohnsitz im Ausland, fehlender Nachweis des Welteinkommens

### Kantonale Rechtsprechung

1. **Verwaltungsgericht AG WBE.2017.220 vom 3. Juli 2017 = AGVE 2017 Nr. 15, S. 93 ff.** (Leitentscheid). URL: https://mcp.opencaselaw.ch/entscheid/ag_verwaltungsgericht_WBE.2017.220; Quelle: https://gesetzessammlungen.ag.ch/app/de/decrees/2441
   - *Sachverhalt:* Rentnerin mit Wohnsitz in Deutschland und Grundstück im Aargau. Die Vorinstanz wollte § 19 Abs. 2 StG AG (entspricht Art. 7 Abs. 2 DBG) nicht anwenden, soweit er zu einem höheren Satz führt (Methodendualismus).
   - *E. 2.1:* «Mit § 19 Abs. 2 StG hat der kantonale Gesetzgeber [...] die gleiche Lösung wie im Bundesrecht gewählt.» Ob ein Kanton davon abweichen dürfte, ist offen.
   - *E. 2.2.1:* Kein Verstoss gegen Art. 25 Abs. 1 DBA CH-D, «weil weder Art. 7 Abs. 2 DBG noch § 19 Abs. 2 StG an die Staatsangehörigkeit anknüpfen». Für das Betriebsstättendiskriminierungsverbot könnte es anders liegen (Oesterhelt/Schreiber, Art. 7 N 14).
   - *E. 2.2.2:* Hinweis auf Locher, Komm. DBG I, Art. 7 N 11: Genügen nicht überprüfbare Auslandsunterlagen für eine höhere Progression, sollte das auch umgekehrt gelten.
   - *E. 2.2.3.1:* Zustimmend zu Locher, Art. 7 N 13, der nur bei Geschäftsbetrieben und Betriebsstätten auf das ausländische Ergebnis verzichten will. Die Gegenposition von Simonek, Liber Amicorum Vonplon 2009, S. 303, übersehe dies.
   - *E. 2.2.3.2:* Würde nur zum Inlandsatz besteuert, liefe das «auf eine systematische Schlechterstellung der in der Schweiz unbeschränkt Steuerpflichtigen hinaus».
   - *Offen gelassen (E. 2.2.3.2):* Ob bei *Auslandverlusten* die fehlende Überprüfbarkeit allein «einen ausreichenden Grund für die steuerliche Erfassung mindestens der Inlandfaktoren sein kann».
2. **Gericht AG 3-RV.2021.197 vom 21. Dezember 2023:** übernimmt WBE.2017.220 «uneingeschränkt» (E. 4.2) und wendet sie auf Auslandverluste an (siehe (b)). *E. 5.4:* Der Steuerpflichtige hat «mindestens zu dem Steuersatz zu entrichten [...], der dem in der Schweiz erzielten Einkommen und dem in der Schweiz gelegenen Vermögen entspricht.»
3. **Verwaltungsgericht ZH SB.2017.00103, E. 2.2/2.3:** Der Mindestsatz gilt auch bei Grundstücken. § 6 Abs. 2 StG ZH ist analog zu Art. 7 Abs. 2 DBG anzuwenden (gesetzgeberisches Versehen). Gestützt wird das auf StRK II ZH vom 16.7.2004, StE 2005 A 31.2 Nr. 5, E. 4.b.bb/cc.
4. **Steuerrekurskommission BS STRK.2023.65:** DBG-Minimalsteuer (siehe (b)). Kantonal fehlt die Grundlage.
5. **Gericht VS F1 24 83, E. 4.2.3:** «Die Bestimmung von Art. 7 Abs. 2 DBG (und Art. 5 Abs. 6 StG) sind als Minimalsteuersatz formuliert. Grundsätzlich sollen auch [...] beschränkt Steuerpflichtige die Steuer aufgrund der Gesamtprogression unter Ausschluss des negativen Progressionsvorbehalts entrichten. Die Doppelbesteuerungsabkommen hindern die Schweiz nicht an der satzbestimmenden Berücksichtigung der weltweiten Einkünfte (zum Ganzen Oesterhelt/Schreiber [...], 4. A., 2022, N. 13 ff. zu Art. 7 DBG).» Die Rüge, nur zum Satz des Walliser Einkommens besteuert zu werden, «geht daher fehl».
6. **Gericht SO SGSTA.2018.39** (Tool-Datum «28. Mai 2018»; laut Volltext Urteil vom 5.11.2018). URL: https://mcp.opencaselaw.ch/entscheid/so_gerichte_SGSTA.2018.39
   - *Sachverhalt:* Wohnsitz in Brasilien, vermietete Liegenschaft in Solothurn. Das brasilianische Einkommen und Vermögen wird satzbestimmend berücksichtigt.
   - *E. 3.3:* «Unabhängig vom Abschluss von Abkommen zur Vermeidung von Doppelbesteuerung vermeidet die Schweiz bereits unilateral die Doppelbesteuerung [...] durch eine Freistellung mit Progressionsvorbehalt, d.h. dass nur die in der Schweiz gelegenen Werte steuerbar sind, aber zum Satz, der dem gesamten Einkommen entspricht (Art. 6 Abs. 1, Art. 7 Abs. 1 DBG [...]; BGer [...] 2C_698/2015, 2C_699/2015, E. 3.2.2).»
7. **Gericht GE ATA/1385/2017 vom 10. Oktober 2017**, bestätigt durch **BGer 2C_980/2017 vom 28. Juni 2018**:
   - *Genfer «procédure simplifiée»* (Information AFC-GE n° 1/2008, vorher 6/1995 und 9/2003): Wer nur die Genfer Liegenschaft deklariert, wird zum Maximalsatz besteuert. Die Schuldzinsen werden auf 60 % der Rendite begrenzt. Die Methode ist eine Option für mindestens zwei Jahre (consid. 6a). *Consid. 6a:* «Le revenu net est ensuite imposé au taux maximum.»
   - *Consid. 5b:* Der Gesamtsatz soll verhindern, dass «la personne qui a des éléments imposables en Suisse et dans d'autres États ne soit privilégiée en Suisse par rapport à la personne dont tous les éléments imposables se trouvent dans cet État» (BGer 2C_1133/2015 E. 5.2).
   - *Consid. 7b:* Bei widersprüchlichem Verhalten bleibt es bei der procédure simplifiée.
   - *BGer 2C_980/2017 E. 4.2* (wörtlich): «La loi fixe cependant deux limites minimales en relation avec cette répartition: au moins le revenu acquis en Suisse doit être imposé (art. 6 al. 2 2e phr. LIFD) et l'imposition n'a lieu qu'à un taux correspondant au moins à ce revenu (art. 7 al. 2 LIFD).»
8. **Gericht GE A/4933/2008** (DCCR/640/2010): Maximalsatz nur nach erfolgloser Nachfrage und mit Belastungsobergrenze, siehe (a).
9. **Gericht GE JTAPI/289/2025 vom 19. März 2025** (Wohnsitz Israel, «déclaration simplifiée» gewählt). URL: https://mcp.opencaselaw.ch/entscheid/ge_gerichte_JTAPI_289_2025. Nur das Snippet wurde gelesen.

### Lehre

- **Kollruss, sui generis 2021, S. 309 N 11:** «Gemäss Art. 7 Abs. 2 DBG einschliesslich der Regelungen der Kantone und Gemeinden ist die Einkommenssteuer mindestens zu dem Steuersatz zu entrichten, der dem in der Schweiz erzielten Einkommen entspricht.»
- **Oesterhelt, FStR 2006/3 (Lexplorer), Anmerkung zu BGer 2P.140/2005 vom 28.11.2005** (juristische Personen, Art. 52 Abs. 4 DBG; Analogie zu Abs. 2):
  - Das BGer hielt fest, der Betriebsstättestaat sei «berechtigt, den für ansässige Unternehmen geltenden progressiven Tarif allein auf die Betriebsstätte anzuwenden und dabei die Gewinne des Gesamtunternehmens ausser Acht zu lassen, selbst wenn die letzteren niedriger seien als die der Betriebsstätte» (OECD-Kommentar zu Art. 24, Ziff. 23, 24 lit. c, 39).
  - Fn. 18: Die satzbestimmende Berücksichtigung ist nach «Ziff. 37 des OECD-Kommentars (idF seit 1977) ausdrücklich als zulässig bezeichnet». § 6 Abs. 2 StG ZH verzichtet für natürliche Personen auf den ausländischen Gewinn beim Satz.
  - Zur alten Fassung «mindestens» in Art. 52 Abs. 4 aDBG und zum «einseitige[n] Methodendualismus zugunsten des Fiskus» (Brülisauer).
- **Simonek, Wirkungen einer nachrangigen Ansässigkeit auf die Steuerpflicht in der Schweiz, in: Ackermann/Bommer (Hrsg.), Liber Amicorum für Dr. Martin Vonplon, Zürich 2009, S. 303:** zitiert in WBE.2017.220 als Gegenposition; nicht im Original gelesen.

---

## (e) Verhältnis zu Art. 6, 38 und 40 DBG, Quellensteuer und DBA (Art. 23A OECD-MA)

### Art. 6 DBG und die interkantonalen Grundsätze

- **Steuerrekursgericht ZH DB.2013.239, E. 2a:** Art. 7 Abs. 1 DBG ist «offen formuliert» und gilt auch bei einer Freistellung nach DBA, nicht nur für die Fälle von Art. 6 DBG.
- **Verwaltungsgericht ZH SB.2011.00037, E. 2.2:** Die in § 5 StG ZH genannten Ausscheidungsfälle sind nicht abschliessend.
- **Gericht VD FI.2023.0121 vom 8. Juli 2024, consid. 4b:** «La deuxième phrase de l'art. 6 al. 2 LIFD limite la prise en considération [...] des éléments du revenu acquis hors du pays; elle interviendra seulement pour la fixation du taux d'imposition»; «Le revenu global déterminant pour le taux est formé de ces revenus ainsi que des éléments imposables à l'étranger» (Paschoud/de Vries Reilingh, CR-LIFD, N 7 ad art. 7).
- **De Vries Reilingh, Diss. 2010, S. 111 N 255–257:** «Les règles des art. 6 al. 1, 7 al. 1 et 52 al. 1 LIFD déclarent donc applicable, dans les rapports internationaux, la méthode de l'exemption inconditionnelle – cette exemption inconditionnelle étant sous réserve de progression en ce qui concerne les personnes physiques.» Fn. 452: Die Methode «évite que la progression du taux ne soit « cassée »». Fn. 451: Für juristische Personen gibt es wegen des proportionalen Satzes keinen «taux global».
- **Interkantonal (nur DBG):** Verwaltungsgericht ZH SB.2025.00054, E. 5.8 (siehe (a)).

### Art. 40 DBG: unterjährige Steuerpflicht

1. **Steuerrekursgericht ZH DB.2015.129 vom 21. Oktober 2015** (Zuzug aus der EU). PDF: https://www.strgzh.ch/assets/entscheide/StRG_DB_2015_129_zl.pdf
   - Die Hochrechnung nach Art. 209 Abs. 3 aDBG (= Art. 40 Abs. 2/3 DBG) verletzt das FZA nicht.
   - *E. 3c/bb:* «Steuerpflichtige, welche im Ausland ein höheres Einkommen erzielt haben als nach ihrem Zuzug in der Schweiz, erhalten mit der getroffenen Lösung einen Vorteil, bleibt doch ihr Auslandseinkommen bei der Satzbestimmung ausser Betracht.» Weiter: «fehlen doch der hiesigen Steuerbehörde Untersuchungsmittel mit Bezug auf die wirtschaftlichen Verhältnisse im Ausland vor Zuzug.»
2. **Gericht GE A/4933/2008, consid. 5:** Auslandeinkünfte vor Beginn der (auch beschränkten) Steuerpflicht nach Art. 8 DBG sind für den Satz nicht massgebend.
3. **Steuerrekursgericht ZH DB.2017.109, E. 3–4:** Wegzug ins Ausland mit beibehaltenem Grundeigentum gilt als *ganzjährige* Steuerperiode. Die Lehre will die Periode aufteilen (Oesterhelt/Seiler, ZB-DBG, Art. 8 N 29 f.; Paschoud/de Vries Reilingh, CR-LIFD, Art. 8 N 24). Das Gericht lehnt das ab, «da das tatsächliche satzbestimmende Einkommen aufgrund der anhaltenden Deklarationspflicht des Steuerpflichtigen bekannt ist».
4. **Gericht VD FI.2023.0121 vom 8. Juli 2024** (ebenso Gericht VD FI.2022.0151 vom 1. Juni 2023): Bei Zuzug mit vorbestehender beschränkter Steuerpflicht wendet Waadt die «méthode unitaire» an. Der französische Lohn für Januar–Februar wird satzbestimmend berücksichtigt.
   - **Vom BGer aufgehoben: BGer 9C_416/2024 vom 14. August 2025 = BGE 152 II 98.** Regeste (deutsche Übersetzung, Entscheidsuche CH_BGE_004_BGE-152-II-98_2026): «Art. 7 Abs. 1 DBG (Progressionsvorbehalt) ist unabhängig von der beschränkten oder unbeschränkten Steuerpflicht sowie von der Aufteilung oder Nicht-Aufteilung der Steuerperiode auf Personen, die dem ordentlichen Veranlagungsverfahren unterliegen, anwendbar (E. 7.2 und 9.1.3). Die Aufteilung der Steuerperiode und damit die Anwendung von Art. 40 Abs. 3 DBG [...] ermöglicht eine bessere Gewährleistung der Grundsätze [...] (E. 9.3.1-9.3.3).»
   - **Spannung:** BGE 152 II 98 betrifft den *Zuzug*. Die Zürcher Lösung für den *Wegzug* mit beibehaltenem Grundeigentum (DB.2017.109) ist daran zu prüfen.
5. **Steuerrekursgericht ZH ST.2016.82** (Tool-Datum «24. September 2015», siehe Hinweis oben), E. 2: Erwerb oder Verkauf einer Liegenschaft durch eine Person mit Wohnsitz im Ausland ergibt eine unterjährige Steuerperiode. Ausländisches Einkommen ist beim Satz zu berücksichtigen (Merkblatt ZStB Nr. 24/300, neu 49.3, Rz 11, 15–17, 22; Weisung Umrechnung ZStB 24/101).
6. **Gericht GR PVG 2008 14:** Umrechnung regelmässiger und unregelmässiger Einkünfte. Nur das Snippet wurde gelesen.

### Art. 38 DBG: Kapitalleistungen

- Keine kantonale Rechtsprechung, die Art. 7 und Art. 38 DBG verknüpft. Die Suche zu «Kapitalleistung beschränkt steuerpflichtig satzbestimmend» blieb ohne einschlägigen Treffer; die gefundenen Entscheide betreffen nur die Abgrenzung zu Art. 38 DBG.

### Quellensteuer

- **Verwaltungsgericht ZH SB.2015.00056 vom 16. Dezember 2015** (rechtskräftig; Rechtslage vor der Quellensteuerrevision 2021). URL: https://mcp.opencaselaw.ch/entscheid/zh_verwaltungsgericht__SB.2015.00056
  - Sachverhalt: internationaler Wochenaufenthalter mit Wohnsitz in Deutschland. Steueramt und ESTV wollten das Auslandseinkommen satzbestimmend berücksichtigen; das Gericht lehnte ab.
  - *E. 4.1:* Bei der Quellensteuer gilt der «Grundsatz der Einzelbetrachtung». «Das führt dazu, dass die übrigen ausländischen Einkünfte für die Satzbestimmung von beschränkt Steuerpflichtigen nicht berücksichtigt werden (Peter Locher, [...] Art. 7 DBG N. 14).» Der Progressionsvorbehalt komme bei der Quellensteuer von im Ausland wohnhaften internationalen Wochenaufenthaltern nicht zur Anwendung (Zigerlig/Jud).
  - *E. 4.2:* Art. 90 Abs. 1 aDBG (sinngemässe Anwendung von Art. 7) gilt nur einseitig für die ergänzende ordentliche Veranlagung.
  - Für das geltende Recht (Art. 99a/99b DBG) ist die Bedeutung neu zu würdigen.
- **Steuerrekursgericht ZH QS.2015.1 vom 22. April 2015:** Satzbestimmung bei Quellensteuer von ausländischen Wochenaufenthaltern. Nur das Snippet wurde gelesen: «Im Übrigen ist nicht einzusehen, weshalb das kantonale Steueramt gestützt auf Art. 7 Abs. 1 DBG bzw. § 6 Abs. 2 StG lediglich zu[...]».

### DBA (Art. 23A OECD-MA)

- **Gericht SO SGSTA.2018.39, E. 3.3:** Die Freistellung mit Progressionsvorbehalt nach Art. 23 Abs. 2 lit. a des DBA CH-BR (zum Entscheidzeitpunkt noch nicht in Kraft) wäre die vereinbarte Methode (Simonek, Komm. IStR 2015, Art. 23 A Abs. 1 OECD-MA N 59 f.).
- **Gericht VD FI.2023.0121, consid. 6:** Art. 25 let. B par. 1 CDI CH-FR «réserve expressément l'imposition au taux global». Art. 4 par. 4 CDI CH-FR hat darauf keinen Einfluss.
- **Gericht GR A 2016 31, E. 2b:** DBA ohne Regel zur Aufteilung von Erträgen und Kosten → es gilt internes Recht (BGE 140 II 157 E. 2.4).
- **Steuerrekursgericht ZH DB.2012.302, E. 2d/bb und 4a:** Satzbestimmung mit Faktoren des Ehegatten nach Art. 24 Abs. 2 Ziff. 1 DBA CH-D, siehe (f).
- **Verwaltungsgericht AG WBE.2017.220, E. 2.2.1 / Gericht AG 3-RV.2021.197, E. 5.1:** Art. 25 Abs. 1 DBA CH-D, Art. 2 und Art. 21 Abs. 2 FZA, siehe (b) und (d).

---

## (f) Satzbestimmung bei Ehegatten und Familie mit teilweiser Steuerpflicht

### Kantonale Rechtsprechung

1. **Steuerrekursgericht ZH DB.2012.302 vom 30. Januar 2013.** PDF: https://www.strgzh.ch/assets/entscheide/StRG_DB_2012_302_nk.pdf
   - *Sachverhalt:* Die Ehefrau wohnt in Zürich, der Ehemann in Deutschland (EU-Beamter). Die Mittel werden getrennt verwendet, der Wille zur Ehe besteht.
   - *E. 2d/aa:* «Wegen der weiterbestehenden Unteilbarkeit des beiden Ehegatten gemeinsam zustehenden Steuerobjekts darf die Steuer aber immerhin auf dem in der Schweiz steuerbaren Einkommen nach dem Steuersatz erhoben werden, der dem gesamten ehelichen Einkommen entspricht, wobei jedoch auch der Verheiratetentarif anzuwenden ist (BGE 138 II 300 E. 2.3; [...]). Im internationalen Verhältnis ist dabei allerdings stets die allenfalls davon abweichende Regelung eines Doppelbesteuerungsabkommens zu beachten.» Für die direkte Bundessteuer folgt das aus Rechtsprechung und Lehre, kantonal aus § 7 Abs. 2 StG ZH.
   - *E. 4a:* Der Progressionsvorbehalt nach Art. 24 Abs. 2 Ziff. 1 DBA-D verlangt an sich Subjektidentität (Vogel, Art. 23 N 220). Trotzdem gilt: «Damit ist es abkommensrechtlich auch im vorliegenden Fall zulässig, für die Berechnung des anwendbaren Steuersatzes auf dem steuerbaren Einkommen und Vermögen der hier ansässigen Pflichtigen die Faktoren des in Deutschland ansässigen Ehegatten mit einzubeziehen.»
   - *E. 4b/bb:* Zur Heiratsstrafe: Die Steuerpflichtige trägt die Beweislast für die Belastungswerte des Ehemanns. Eine Mehrbelastung von 13,8 % ist hinzunehmen.
   - *E. 2c:* Ein Nebensteuerdomizil des im Ausland wohnhaften Ehegatten ist abzulehnen (a.M. BGer 2P.2/2003).
2. **Steuerrekursgericht ZH ST.2016.82** (Tool-Datum «24. September 2015»; laut Volltext 28.6.2017). PDF: https://www.strgzh.ch/assets/entscheide/StRG_ST_2016_82_jj.pdf
   - *E. 1b:* «Ist nur einer von beiden Ehegatten wirtschaftlich zugehörig, ist nur dieser Ehegatte im Kanton steuerpflichtig [...]. Für den Steuersatz ist, unter Anwendung des Verheiratetentarifs und der Sozialabzüge für Verheiratete, auf das gesamte eheliche Einkommen und Vermögen abzustellen (§ 7 Abs. 2 StG, letzter Satz).»
   - *E. 1c:* «Dagegen erweist sich die Faktorenaddition der Einkommens- und Vermögensverhältnisse beider Ehegatten auf der Steuersatzebene für die Einschätzung der Pflichtigen als gesetzmässig.»
3. **Verwaltungsgericht SG B 2013/16 vom 12. Februar 2014** (interkantonal). Der VGr verneinte eine Steuerpflicht des Ehegatten ohne eigene Anknüpfung, rechnete die Faktoren aber zusammen (E. 3.2.4 mit Zweifel, Komm. StHG, Art. 40 N 20). **Vom BGer aufgehoben: BGer 2C_309/2014 vom 16. Juli 2015 = BGE 141 II 318.** Für das internationale Verhältnis wichtig ist *E. 2.2.3* (wörtlich): «Anders präsentiert sich die Rechtslage, wenn nur ein Ehegatte in der Schweiz ansässig ist und der andere Partner sein Hauptsteuerdomizil im Ausland hat. Das Einkommen und Vermögen darf dann nicht zusammengerechnet werden, weil eine Zusammenrechnung im Sinne von Art. 9 Abs. 1 DBG bzw. Art. 3 Abs. 3 Satz 1 StHG nur zulässig ist, wenn beide Eheleute der (schweizerischen) Steuerhoheit unterliegen. Für den in der Schweiz steuerpflichtigen Gatten besteht folglich eine selbständige Steuerpflicht. Lediglich zur Satzbestimmung wird - unter Anwendung des Verheiratetentarifs - auf das eheliche Gesamteinkommen abgestellt. Das gilt bei unbeschränkter Steuerpflicht nur eines der beiden Partner [...], aber auch, wenn diese schweizerische Steuerpflicht des einen Gatten eine beschränkte ist und aufgrund wirtschaftlicher Zugehörigkeit besteht (BGE 75 I 385 [...]; BGE 73 I 405; [...] KS Nr. 30, a.a.O., Ziff. 2.2).» (Zitierstring: «BGer 2C_309/2014 vom 16. Juli 2015, E. 2.2.3»; publiziert als BGE 141 II 318.)
4. **Gericht GE A/4933/2008, consid. 7:** Auch beim Maximalsatz mangels Deklaration gelten der Verheiratetentarif und der Kinderabzug.
5. **Weitere Entscheide (nicht im Volltext gelesen):** Steuerrekursgericht ZH DB.2022.53 vom 25. Oktober 2022 (Ehegatte in Deutschland, getrennte Mittelverwendung behauptet); Steuerrekursgericht ZH ST.2010.37 vom 11. Mai 2010 (Doppelbürgerin, Lebensmittelpunkt); GE ATA/1304/2019 vom 27.8.2019 (Verheiratetentarif, beschränkte oder unbeschränkte Steuerpflicht offen).

### Lehre

- **De Vries Reilingh, Diss. 2010, S. 270 N 643–645 und S. 272 f. N 651:** Im internationalen Verhältnis werden nur die Faktoren des in der Schweiz steuerpflichtigen Ehegatten besteuert. Die Faktoren des im Ausland wohnhaften Ehegatten «sont, en revanche, pris en considération pour fixer le taux de l'impôt». Es gibt keine hälftige Aufteilung wie interkantonal (BGer, StE 1998 B 11.3 Nr. 11).
- **Brülisauer/Kriesi, FStR 2008/1 (Lexplorer), Abschn. 3.1.1.2:** Ist Art. 11 DBG anwendbar, ist für die Satzbestimmung der ausländischen Teilhaber das Ergebnis um den Anteil des inländischen Teilhabers zu kürzen.

---

## Literaturverzeichnis (selbst gelesen)

- Brülisauer Peter/Kriesi Marcel R., Internationale Personenunternehmen im Einkommens- und Gewinnsteuerrecht der Schweiz (2. Teil), FStR 2008, Heft 1. Gelesen über Lexplorer Tax, doc_id 1f882a53-7826-4e5f-ab90-1924576eee3c, https://app.lexplorer.ch/suche?e_id=373&e_sys=ile. Die Abschnittsangaben folgen dem Beitrag; die Originalseiten im Heft sind nicht ermittelt.
- De Vries Reilingh Daniel, Le droit fiscal intercantonal et le droit fiscal international de la Suisse: systèmes, relations, comparaison et examen de la jurisprudence, Diss. Neuchâtel 2010 (LIBRA UniNE, https://libra.unine.ch/handle/123456789/34721).
- Kollruss Thomas, Hybride Gesellschaften im Verhältnis Schweiz-Deutschland, sui generis 2021, S. 305 ff. (DOI 10.21257/sg.194).
- Komor Philipp Jan, Die Gewinnungskosten beim Einkommen aus unbeweglichem Privatvermögen, Diss. Bern 2020 (BORIS, https://boris-portal.unibe.ch/handle/20.500.12422/233213).
- Oesterhelt Stefan, Gesamtverlustvortrag und Verbot der Betriebsstätten-Diskriminierung. Anmerkungen zum Urteil des Bundesgerichts vom 28.11.2005 (2P.140/2005), FStR 2006, Heft 3 (Judikatur-Forum). Gelesen über Lexplorer Tax, doc_id 53bb751a-bbea-4fd8-aa2a-dd57368e9071, https://app.lexplorer.ch/suche?e_id=344&e_sys=ile.
- Grieder Nicolas/Hongler Peter, Kommentierung zu Art. 11 DBG, in: Hongler Peter/Sutter Fabian (Hrsg.), Onlinekommentar zum Bundesgesetz über die direkte Bundessteuer, Stand 18.5.2026, https://onlinekommentar.ch/de/kommentare/dbg11 (nur zur Abgrenzung).

## Nur zitiert in Entscheiden, nicht im Original gelesen

- Agner/Jung/Steinmann, Art. 7 N 3 bzw. Commentaire LIFD 2001, S. 27
- Athanas/Giglio, Komm. AG StG, 4. A. 2015, § 19 N 6, 6b
- Betschart, Komm. IntkStR 2011, § 24
- Cadosch, Komm. DBG, 2. A. 2008
- Locher, Komm. DBG I, Art. 6 N 26/28 und Art. 7 N 6, 11, 13, 14
- Oesterhelt/Schreiber, in: Zweifel/Beusch, DBG, 3. A. 2017 und 4. A. 2022, Art. 6 N 4, 27 f. und Art. 7 N 5 f., 12–14
- Paschoud/de Vries Reilingh, CR-LIFD, 2. A. 2017, Art. 6 N 13, 18 und Art. 7 N 5–7
- Richner/Frei/Kaufmann/Meuter, Komm. StG ZH, § 6 N 2, § 7 N 25 f., 36 und HK DBG Art. 6 N 55 ff., Art. 9 N 37
- Simonek, Liber Amicorum Vonplon, 2009, S. 303
- Simonek, Komm. IStR, Art. 23 A, B N 24 ff., 84 f., 87
- Zigerlig/Jud, ZB-DBG, 2. A., Vor Art. 83–101 N 4, Art. 90 N 3
- Botschaft DBG, BBl 1983 III 158
