# Entscheidregister Art. 5 MWSTG (Indexierung)

Stand: 28.10.2026 (Claude-Cloud, unbeaufsichtigter Lauf).

## Ergebnis

**Kein Entscheid eines Gerichts legt Art. 5 MWSTG (oder Art. 4 aMWSTG 1999) aus oder wendet ihn an.** Das Register enthält deshalb keine A- oder B-Entscheide.

## Suchwege

| Weg | Abfrage | Treffer | Ergebnis |
|---|---|---|---|
| `pipeline/entscheide.py MWSTG/art-5` (Entscheidsuche-Phrasensuche, Volltexte Open Case Law) | `"Art. 5" AND (MWSTG OR LTVA OR LIVA)` | 272 Suchtreffer, 46 Entscheide im Cache | alle 46 Fehltreffer (siehe Tabelle): Art. 5 aMWSTG 1999 (Steuerobjekt), Art. 5 MWSTV 1994, Art. 5 MWSTG/FL; Volltextprüfung auf «Indexier|Landesindex|indexation|indice des prix» ohne Treffer |
| Open Case Law `get_article_history` (SR 641.20, Art. 5) | – | 10 «leading cases» (2A.520/2003, 2A.567/2006, BVGer A-1342/2006 u.a.) | alle zu Art. 5 aMWSTG (Steuerobjekt) – Fehltreffer |
| Open Case Law `search_decisions` | `"Art. 5 MWSTG" AND (Indexierung OR Landesindex OR Teuerung)`; `Mehrwertsteuer "Indexierung" "Frankenbeträge"` (bvger); `"Art. 115 Abs. 1 MWSTG" OR …` | je >200 unscharfe Treffer | Stichprobe der ersten 50 ohne Bezug (Unterhalts-, Miet-, Sozialversicherungsrecht) |
| Entscheidsuche `search` (alle Gerichte) | `("Art. 5 MWSTG" OR "art. 5 LTVA" OR "Art. 4 MWSTG" OR "art. 4 LTVA") AND (Indexierung OR Landesindex OR indexation OR "indice suisse des prix")` | 0 | – |
| Entscheidsuche | `Mehrwertsteuer "Landesindex der Konsumentenpreise seit der letzten Festlegung"` | 0 | – |
| Entscheidsuche | `Mehrwertsteuer Indexierung Frankenbeträge` | 0 | – |
| Entscheidsuche | `Mehrwertsteuer AND (Indexierung OR "Landesindex der Konsumentenpreise") AND (Saldosteuersatz OR Meldeverfahren OR Bezugsteuer OR Geschenke)` | 11 | nur Zivilrecht (Indexierung von Unterhaltsbeiträgen) – Fehltreffer |
| Entscheidsuche | `"Art. 115 Abs. 1 MWSTG" OR "Art. 115 MWSTG"` | 3 (HG ZH HG120063, HG110143; KG FR 101 2023 453) | betreffen den anwendbaren Steuersatz bei Satzänderungen (Art. 115 Abs. 1 Satz 1), nicht die Höchstbeträge – nicht verwendet |

BVGer und kantonale Gerichte: keine einschlägigen Entscheide (Suchen oben; BVGer über Open Case Law und Entscheidsuche).

## Cache-Treffer (alle Klasse «Fehltreffer»)

| Entscheid | Datum | Normstelle im Entscheid | Klasse | Bemerkung |
|---|---|---|---|---|
| BGer 2A.557/1999 vom 10. November 2000 | 2000-11-10 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2A.547/2002 vom 26. Mai 2004 | 2004-05-26 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2A.520/2003 vom 29. Juni 2004 | 2004-06-29 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2A.502/2004 vom 28. April 2005 | 2005-04-28 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 7B.73/2005 vom 12. August 2005 | 2005-08-12 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2A.499/2004 vom 1. November 2005 | 2005-11-01 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2A.197/2005 vom 28. Dezember 2005 | 2005-12-28 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2A.81/2005 vom 7. Februar 2006 | 2006-02-07 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2A.478/2005 vom 8. Mai 2006 | 2006-05-08 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2A.331/2005 vom 9. Mai 2006 | 2006-05-09 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 4C.58/2006 vom 13. Juni 2006 | 2006-06-13 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 7B.89/2006 vom 10. Juli 2006 | 2006-07-10 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGE 132 II 353 | 2006-08-09 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2A.748/2005 vom 25. Oktober 2006 | 2006-10-25 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2A.567/2006 vom 25. April 2007 | 2007-04-25 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2A.369/2005 vom 24. August 2007 | 2007-08-24 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2A.756/2006 vom 22. Oktober 2007 | 2007-10-22 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2A.40/2007 vom 14. November 2007 | 2007-11-14 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_195/2007 vom 8. Januar 2008 | 2008-01-08 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_506/2007 vom 13. Februar 2008 | 2008-02-13 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_518/2007 vom 11. März 2008 | 2008-03-11 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_614/2007 vom 17. März 2008 | 2008-03-17 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_510/2007 vom 15. April 2008 | 2008-04-15 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2A.269/2006 vom 20. Juni 2008 | 2008-06-20 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_639/2007 vom 24. Juni 2008 | 2008-06-24 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_105/2008 vom 25. Juni 2008 | 2008-06-25 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_743/2007 vom 9. Juli 2008 | 2008-07-09 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2A.264/2006 vom 3. September 2008 | 2008-09-03 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_430/2008 vom 18. Februar 2009 | 2009-02-18 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_653/2008 vom 24. Februar 2009 | 2009-02-24 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_531/2008 vom 5. Juni 2009 | 2009-06-05 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_807/2008 vom 19. Juni 2009 | 2009-06-19 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_392/2008 vom 1. September 2009 | 2009-09-01 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_59/2009 vom 3. September 2009 | 2009-09-03 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_904/2008 vom 22. Dezember 2009 | 2009-12-22 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_434/2009 vom 17. Juni 2010 | 2010-06-17 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGE 138 II 239 | 2012-03-19 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_487/2011 vom 13. Februar 2013 | 2013-02-13 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_1003/2011 vom 18. Februar 2013 | 2013-02-18 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_576/2013 vom 20. Dezember 2013 | 2013-12-20 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGE 140 I 153 | 2014-07-28 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_1143/2013 vom 28. Juli 2014 | 2014-07-28 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_171/2015 vom 31. Mai 2016 | 2016-05-31 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_326/2015 vom 24. November 2016 | 2016-11-24 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_1076/2015 vom 9. Dezember 2016 | 2016-12-09 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |
| BGer 2C_1069/2017 vom 16. April 2018 | 2018-04-16 | «Art. 5» eines anderen Erlasses bzw. einer früheren Fassung (aMWSTG/MWSTV/FL-MWSTG) | – (Fehltreffer) | betrifft nicht die Indexierung |