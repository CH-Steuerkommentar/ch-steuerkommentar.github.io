# Art. 7 MWSTG – Rechtsprechung BVGer, SRK und kantonale Gerichte (Stand 28.10.2026)

Werkzeuge: Open Case Law (search_decisions, get_erwaegung, find_relevant_erwaegung, find_appeal_chain, get_decision), Entscheidsuche (search, fetch_document). Kein Lexplorer, keine Websuche. **Lexplorer-Suchen: 0.**
Zitierstrings ausschliesslich aus Tool-Ergebnissen (`citation_string_de`); SRK-Entscheide erscheinen im Tool als «Gericht CH JAAC …» (Bundesverwaltung, VPB/JAAC); die Publikationsangabe «VPB 68.71» / «VPB 69.64» stammt wörtlich aus dem Volltext von A-1469/2006 E. 4.1.3 bzw. A-1525/2006 E. 2.5. Alle Kernsätze wörtlich aus get_erwaegung / find_relevant_erwaegung / get_decision; E.-Nummern am Volltext geprüft.

## 0. Wichtige Vorbefunde

1. **Vorgängernorm MWSTV 1994 ist Art. 11, nicht Art. 12.** Der Ort der Lieferung stand in Art. 11 Bst. a/b MWSTV (1994); Art. 12 MWSTV regelte den Ort der Dienstleistung. Belege: BVGer A-1455/2006 vom 25. April 2007, E. 3.1.2 («C'est l'art. 11 OTVA qui règle la question du lieu de la livraison.»); BVGer A-1612/2006 vom 9. Juli 2009, E. 2.5.1 (Lieferort «Art. 11 Bst. a MWSTV», Dienstleistungsort «Art. 12 Abs. 1 MWSTV»); BVGer A-1525/2006 vom 28. Januar 2008, E. 2.5; SRK, Gericht CH JAAC 69.64 vom 2. November 2004, E. 4a («Art. 11 Bst. a MWSTV»). → `_Auftrag.md` (Zeile 12: «Art. 12 MWSTV 1994») korrigieren.
2. **Vertauschte Etiketten in einem Teil der BVGer-Rechtsprechung.** BVGer A-1612/2006 E. 2.5.1, A-2221/2014 E. 2.2.1 und A-2675/2016 E. 2.2 bezeichnen lit. a als «Beförderungs- oder Versandlieferung» und lit. b als «Abhollieferung» – umgekehrt zu Gesetz und übriger Rechtsprechung (korrekt: A-2855/2008 E. 2.3.1; A-2387/2007 E. 2.3.1; A-4783/2015 E. 4.2.1; A-2888/2016 E. 5.2.1 f.; A-4388/2014 E. 4.1). In A-1612/2006 und A-2675/2016 ist die Sachaussage im Folgesatz jeweils richtig (Beförderung durch Lieferanten → Beginn der Beförderung; Abholung durch Abnehmer → Lageort bei Verschaffung). Für den Kommentar nur mit Hinweis zitieren.
3. **Kein BVGer-Entscheid** gefunden zu: Versandhandelsregel Art. 7 Abs. 3 lit. b (100'000 Fr.) in der Sache; Art. 7 Abs. 2 in der Fassung 2018 (Empfängerortprinzip Energie); Werklieferung/Montage-Ort. A-2106/2017 E. 4.4 lässt Abs. 3 lit. b ausdrücklich offen.
4. **Kantonale Gerichte:** keine einschlägigen Entscheide (nur zivil-/strafrechtliche «Lieferort»-Treffer).

## 1. Suchprotokoll

| # | Werkzeug / Filter | Suchbegriff | Treffer | Relevant |
|---|---|---|---|---|
| 1 | OCL bvger | "Art. 7 Abs. 1 MWSTG" | 39 | 1 (A-2106/2017); Rest Art. 7 aMWSTG = Dienstleistungsbegriff |
| 2 | OCL bvger | "Ort der Lieferung" Mehrwertsteuer | 166+ | ~15 |
| 3 | OCL bvger | Reihengeschäft Mehrwertsteuer | 133+ | 2 (A-1525/2006, A-1526/2006; nur Behauptung) |
| 4 | OCL bvger | Abhollieferung OR Beförderungslieferung OR Versandlieferung | 134+ | 8 |
| 5 | OCL bvger | Unterstellungserklärung Einfuhr | 152+ | 2 (A-2106/2017, A-601/2019); Rest Saldosteuersatz-«Unterstellungserklärung» |
| 6 | OCL bvger | "lieu de la livraison" TVA | 149+ | 6 |
| 7 | OCL bvger | "Art. 7 Abs. 1 Bst. a MWSTG" | 4 | 4 |
| 8 | OCL bvger | "Art. 7 Abs. 1 Bst. b MWSTG" | 3 | 3 |
| 9 | OCL bvger | "art. 7 al. 1 let. a/b LTVA" / "art. 7 al. 1 LTVA" | 179+ | 5 (A-4388/2014, A-2888/2016, A-4783/2015, A-4643/2023, A-3359/2024) |
| 10 | OCL bvger ≥ 6/2010 | "Art. 7 Abs. 3/2/1 MWSTG" | 160+ | 7 |
| 11 | OCL bvger | Konsignationslager OR Auslieferungslager | 64+ | 1 (A-2675/2016) |
| 12 | OCL bvger | Elektrizität Leitungen Ort der Lieferung Empfänger Betriebsstätte | 74+ | 1 (A-1612/2006); A-2036/2022, A-2037/2022 nur Normzitat |
| 13 | OCL bvger | Werklieferung Montage Ausland Ort Lieferung | 60+ | 0 |
| 14 | OCL bger | Docket-Querverweise auf BVGer-Leitentscheide | 2 | 1 (2C_561/2009) |
| 15 | OCL ch_vb (SRK/VPB) | "Ort der Lieferung" Mehrwertsteuer | 160+ | – (compact) |
| 16 | OCL ch_vb | "lieu de la livraison" TVA | 120+ | – (compact) |
| 17 | OCL ch_vb | "Ort der Lieferung" Beförderung Versendung Abnehmer beginnt | 100+ | 3 (VPB 69.64, 68.71; 67.42 nur Begriff) |
| 18 | OCL ch_vb | Reihengeschäft OR "Ausland-Ausland" OR Auslandlieferung | 65+ | 1 (VPB 68.71) |
| 19 | Entscheidsuche CH_BVGer | "Art. 7 Abs. 1 Bst. b MWSTG" | 0 (falsche Hierarchie-ID) | – |
| 20 | Entscheidsuche CH_BVGE | Art. 7 Abs. 1 Bst. a/b MWSTG / art. 7 al. 1 let. a/b LTVA | 6 | 6 |
| 21 | Entscheidsuche CH_BVGE | "Ort der Lieferung" | 10 | 8 |
| 22 | Entscheidsuche CH_BVGE | Reihengeschäft OR opérations/livraisons en chaîne | 3 | 2 (+ A-6593/2024 Zoll) |
| 23 | Entscheidsuche CH_BVGE | Abhollieferung OR Beförderungslieferung OR Versandlieferung | 10 | 10 |
| 24 | Entscheidsuche CH_BVGE | Unterstellungserklärung AND ("im eigenen Namen" OR Einfuhr) | 5 | 2 |
| 25 | Entscheidsuche CH_BVGE | Versandhandel OR "vente par correspondance" | 140 | 0 (IV-/Markenrecht) |
| 26 | Entscheidsuche CH_BVGE | Art. 13 aMWSTG / art. 13 aLTVA (Varianten) | 22 | 18 |
| 27 | Entscheidsuche CH_BVGE | Art. 7 Abs. 2/3 MWSTG / art. 7 al. 2/3 LTVA | 5 | 1 (A-2106/2017); Rest Art. 7 Abs. 2 aMWSTG |
| 28 | Entscheidsuche CH_BVGE ≥ 2011 | "art. 7 LTVA" OR "Art. 7 (Abs. 1) MWSTG" | 4 | 4 |
| 29 | Entscheidsuche 26 Kantone | Art. 7/13 MWSTG bzw. LTVA AND Lieferung/lieu | 2 | 0 (AG SVWG, Dienstleistungsbegriff) |
| 30 | Entscheidsuche 26 Kantone | "Ort der Lieferung"+MWST / "lieu de la livraison"+TVA / "luogo della fornitura"+IVA | 8 | 0 (OR-Erfüllungsort, Strafrecht) |
| 31 | Entscheidsuche 26 Kantone | Mehrwertsteuer AND (Abhollieferung, Reihengeschäft, Unterstellungserklärung, Versandhandel, Lieferort) | 32 | 0 |

Hinweis: Volltextsuche in OCL ist bei OR-Phrasen unscharf; gezielte Phrasensuchen (Nr. 7, 8, 20, 21, 23, 26) waren ergiebiger. Entscheidsuche indexiert BVGer-PDF nur teilweise (Trefferzahlen tiefer als OCL).

## 2. Tabelle der einschlägigen Entscheide

Klassen: **A** = tragend für die Kommentierung (Sachfrage entschieden); **B** = ergänzend (Grundsatz zutreffend formuliert, Anwendung am Rand); **C** = nur Erwähnung/Normwiedergabe.

### 2.1 Grundsatz: Verschaffung der Verfügungsmacht, lit. a vs. lit. b, wer befördert

| Entscheid | Datum | Normstelle | Sachfrage | Kernaussage + wörtlicher Kernsatz | E. | Weiterzug | Klasse | Fassung |
|---|---|---|---|---|---|---|---|---|
| BVGer A-2888/2016 vom 16. Juni 2017 | 16.6.2017 | Art. 7 Abs. 1 lit. a/b | Abgrenzung nach Transportorganisation | Massgebend ist, wer den Transport organisiert; Abholung durch Abnehmer → lit. a (Lageort bei Verschaffung); Transport durch Lieferanten oder seinen Beauftragten → lit. b (Beginn). «Ces règles diffèrent, entre autres, selon la personne organisant le transport.» | 5.2, 5.2.1, 5.2.2 | BGer 2C_709/2017 vom 25. Oktober 2018: bestätigt (prüfte nur Beweiswürdigung, E. 3.4.1) | A | MWSTG 2009 |
| BVGer A-4783/2015 vom 20. Februar 2017 | 20.2.2017 | Art. 7 Abs. 1 lit. a; Art. 3 lit. d | Verfügungsmacht | Lit. a bei Abhollieferung; Verfügungsmacht ohne Eigentumsübergang. «il suffit que le pouvoir de disposer économiquement de la marchandise soit transféré, autrement dit que le preneur puisse en disposer comme un propriétaire» | 4.2.1 | BGer 2C_321/2017 vom 23. Mai 2018: bestätigt (BGer-Begründung zur unternehmerischen Tätigkeit, E. 7.2.2; Lieferort dort soweit ersichtlich nicht Thema) | A | MWSTG 2009 |
| BVGer A-4388/2014 vom 26. November 2015 | 26.11.2015 | Art. 7 Abs. 1 lit. a/b; Art. 3 lit. d Ziff. 1–2 | Systematik; lit. a gilt auch für Werkarbeiten/Gebrauchsüberlassung | «L'art. 7 al. 1 let. a LTVA est également applicable aux prestations assimilées à des livraisons de biens (cf. art. 3 let. d ch. 1 et 2 LTVA …)» | 4.1 | nicht ersichtlich | B | MWSTG 2009 |
| BVGer A-3190/2008 vom 15. Juli 2010 | 15.7.2010 | Art. 13 lit. a/b aMWSTG | Verhältnis lit. a/lit. b; Fakturierung irrelevant | Lit. a bei direkter Übergabe, lit. b bei Transport/Versand; Transportbeginn geht Empfangsort und Rechnung vor. «l'endroit où commence le transport l'emporte sur le lieu de réception du bien ainsi que, par exemple, sur la facturation.» (Ergebnis des Falls: Dienstleistung) | 5.1 | nicht ersichtlich | B | aMWSTG 1999 |
| BVGer A-2387/2007 vom 29. Juli 2010 | 29.7.2010 | Art. 13 lit. a/b aMWSTG | Abhol- vs. Beförderungslieferung; Versand keine selbständige Leistung | «L'expédition n'est ainsi pas conçue comme une prestation autonome» | 2.3.1 | nicht ersichtlich | B | aMWSTG 1999 |
| BVGer A-1612/2006 vom 9. Juli 2009 | 9.7.2009 | Art. 11 MWSTV 1994; Art. 13 aMWSTG | Begriff Beförderungs-/Versandlieferung; Zeitpunkt | «Beförderungs- und Versandlieferungen liegen dann vor, wenn ein Gegenstand vom Lieferanten befördert oder versandt wird.» (Etiketten im Klammerzusatz vertauscht, s. Ziff. 0.2) | 2.5.1 | BGer 2C_561/2009 vom 25. März 2011 (abgewiesen; Lieferort nur referiert, E. 2.1) | B | MWSTV 1994 / aMWSTG |
| SRK, Gericht CH JAAC 69.64 vom 2. November 2004 (SRK 2003-065) | 2.11.2004 | Art. 11 lit. a MWSTV 1994 | Verfügungsmacht | «Verfügungsmacht über einen Gegenstand im Sinne des Mehrwertsteuerrechts kommt dem Abnehmer dann zu, wenn er wie ein Eigentümer über ihn verfügen kann» | 4a | – | B | MWSTV 1994 |
| BVGer A-2855/2008 vom 4. November 2010 | 4.11.2010 | Art. 13 aMWSTG | Standardformel (korrekte Etiketten) | Abhollieferung = lit. a, Beförderungs-/Versandlieferung = lit. b | 2.3.1 | nicht ersichtlich | C | aMWSTG |
| BVGer A-2221/2014 vom 27. Januar 2015 | 27.1.2015 | Art. 13 aMWSTG | Standardformel (Etiketten vertauscht) | wie A-1612/2006 | 2.2.1 | nicht ersichtlich | C | aMWSTG |
| BVGer A-3375/2023 vom 6. September 2024 | 6.9.2024 | Art. 7 Abs. 1 lit. a/b | Standardformel (Fall: Ort der Dienstleistung) | Wiedergabe des Gesetzestexts | 2.3.1 | BGer 9C_578/2024 (20.12.2024, bestätigt; laut Urteilskopf) | C | MWSTG |
| BVGer A-5658/2023 vom 18. Oktober 2024 | 18.10.2024 | Art. 7; Art. 8 | Abgrenzung Lieferung/Dienstleistung (Fernkurse) | «Der Ort der Leistung richtet sich demnach nicht nach Art. 8 Abs. 2 Bst. c MWSTG, sondern nach Art. 7 MWSTG für Lieferungen und/oder nach Art. 8 Abs. 1 MWSTG für elektronische Dienstleistungen.» | 2.5.5 | BGer 9C_671/2024 (4.8.2025; laut Entscheidsuche teilweise bestätigt) | C | MWSTG |
| BVGer A-3359/2024 vom 20. März 2026 | 20.3.2026 | Art. 7 | dito (ESTV-Praxis Fernkurse) | «Le lieu de la livraison est déterminé par l'art. 7 LTVA …» | 3.6.3.2 | nicht ersichtlich | C | MWSTG |
| BVGer A-4898/2018 vom 26. Juni 2019 | 26.6.2019 | Art. 7 Abs. 1 lit. a | Arbeiten an Gegenständen (nur ESTV-Auskunft zitiert) | ESTV: «Übergibt der Leistungsempfänger jedoch seine Triebwerke an einen Dritten und erfolgt die Kontrolle durch diesen, handelt es sich um eine Lieferung nach Art. 7 Abs. 1 Bst. a MWSTG.» | 7.3.2 (Wiedergabe ESTV-E-Mail) | laut Entscheidsuche bestätigt | C | MWSTG |

### 2.2 Abhollieferung ab Inlandlager, Verbringung, Konsignationslager (Art. 4 MWSTV)

| Entscheid | Datum | Normstelle | Sachfrage | Kernaussage + wörtlicher Kernsatz | E. | Weiterzug | Klasse | Fassung |
|---|---|---|---|---|---|---|---|---|
| BVGer A-2675/2016 vom 25. Oktober 2016 | 25.10.2016 | Art. 7 Abs. 1; Art. 4 MWSTV; Art. 54 | Auslieferungslager, Verbringung, Bemessung Einfuhrsteuer | Abhollieferung definiert; Art. 4 MWSTV als «Ausnahmeregelung» (Ort im Ausland, wenn Empfänger und Entgelt beim Verbringen feststehen); sonst Verbringung + Inlandlieferung ab Lager; Konsignationslager (Lehre). «Eine Abhollieferung in letzterem Sinne ist gegeben, «wenn die Gegenstände vom Abnehmer selbst oder in dessen Auftrag von einem Dritten (z.B. Spediteur, Frachtführer) beim Lieferanten abgeholt werden»» | 2.2, 3.1, 3.2 | **aufgehoben** durch BGer 2C_1079/2016 (7.3.2017; laut Urteilskopf; BGer im Cache) | A (mit Vorbehalt Aufhebung) | MWSTG 2009 / aMWSTG |

### 2.3 Lieferung Ausland → Inland, Unterstellungserklärung (Abs. 3 lit. a), Versandhandel (Abs. 3 lit. b)

| Entscheid | Datum | Normstelle | Sachfrage | Kernaussage + wörtlicher Kernsatz | E. | Weiterzug | Klasse | Fassung |
|---|---|---|---|---|---|---|---|---|
| BVGer A-2106/2017 vom 11. Februar 2019 | 11.2.2019 | Art. 13 lit. b aMWSTG; Art. 7 Abs. 1 lit. b, Abs. 3 MWSTG; Art. 3 MWSTV 2010–2017 | Versandlieferung ausländischer Lieferanten; Unterstellungserklärung; Gesetzmässigkeit Art. 3 MWSTV a.F. | Versandlieferung aus dem Ausland = Lieferung im Ausland, Einfuhrsteuer beim Importeur (E. 3.3); unter aMWSTG Unterstellungserklärung als Option nach Art. 27 aMWSTG zulässig, kein Wahlrecht für einzelne Versandlieferungen (E. 4.1.3); Art. 7 Abs. 1 MWSTG keine Grundlage für Art. 3 MWSTV a.F. (E. 4.2.3), Art. 9 MWSTG ebenfalls nicht (E. 4.2.3.1), aber Vollzugskompetenz Art. 182 Abs. 2 BV (E. 4.2.3.2); Art. 7 Abs. 3 n.F. intertemporal nicht anwendbar (E. 4.3.2); Versandhandel offen (E. 4.4). «Demzufolge erbringt ein ausländischer Unternehmer grundsätzlich eine Lieferung im Ausland, wenn er Gegenstände aus dem Ausland in die Schweiz liefert bzw. liefern lässt.» (E. 3.3); «Letztere bestimmt den Ort der Lieferung und enthält weder eine Ausnahme noch eine Delegation an den Bundesrat für eine weitergehende Regelung.» (E. 4.2.3) | 3.3; 4.1.3; 4.2.2–4.2.3.3; 4.3.1 f.; 4.4 | **aufgehoben** durch BGer 2C_266/2019 (23.1.2020; laut Urteilskopf; BGer im Cache) – Tragweite der Aufhebung für E. 4.2.3.2 am BGer-Urteil prüfen | A (mit Vorbehalt Aufhebung) | aMWSTG / MWSTG 2010–2017 / Ausblick 2018 |
| BVGer A-601/2019 vom 19. Februar 2020 | 19.2.2020 | Einfuhr Kunst; Verlagerungsverfahren | Sachverhalt «Unterstellungserklärung Ausland»; Lieferort im BVGer nicht thematisiert (Steuerumgehung, Unternehmereigenschaft) | – (Sachverhalt B.a; E. 2.4 nur Einfuhrsteuer) | 3.1 | BGer 2C_263/2020 vom 10.12.2021 = BGE 148 II 233 (Cache; dort Ort lit. b) | C | aMWSTG/MWSTG |
| BVGer A-1006/2024 vom 1. April 2026 | 1.4.2026 | Einfuhrsteuer; Importeur | Importeur bei Reihengeschäften (BAZG-Richtlinie) | zitiert R-69-01: «Der Grundsatz, dass der Lieferungsempfänger in der Zollanmeldung als Importeur gilt, ist auch dann anwendbar, wenn mit dem Transport des Gegenstands zum Abnehmer mehrere Lieferungen ausgeführt werden (Reihengeschäfte).» | 4.6.4.5.1 | nicht ersichtlich | C | MWSTG |

### 2.4 Reihengeschäft

| Entscheid | Datum | Normstelle | Sachfrage | Kernaussage + wörtlicher Kernsatz | E. | Weiterzug | Klasse | Fassung |
|---|---|---|---|---|---|---|---|---|
| SRK, Gericht CH JAAC 68.71 vom 4. Dezember 2003 (SRK 2003-058; zit. als VPB 68.71) | 4.12.2003 | Art. 5 Abs. 1, Art. 10 MWSTV 1994 | Begriff Reihengeschäft; Zwischenhändler; Rechnung als Mindestvoraussetzung | Eine Warenbewegung, mehrere Lieferungen; Zwischenhändler braucht keinen Besitz; jeder in eigenem Namen auftretende Zwischenhändler ist Lieferer; Rechnungsstellung als Mindestanforderung, da zwischen den Gliedern nur fiktive Lieferungen. «Beim so genannten Reihengeschäft werden durch eine einzige Warenbewegung mehrere Lieferungen von Gegenständen vollzogen.»; «Auch wenn der erste Verkäufer die Ware physisch direkt dem letzten Käufer übergibt, gilt jeder Zwischenhändler, der in eigenem Namen auftritt, als Lieferer»; «zwischen den einzelnen Gliedern deshalb lediglich fiktive Lieferungen von Gegenständen angenommen werden.» | 2a; 3b/bb | – | A | MWSTV 1994 |
| BVGer A-6691/2012 vom 23. Juli 2014 | 23.7.2014 | Art. 23 Abs. 3 MWSTG | Reihengeschäft und Direktausfuhr | «Lorsqu'il y a opération en chaîne, l'exportation directe s'étend à tous les fournisseurs intervenant dans l'opération» | 6.2 | nicht ersichtlich | B | MWSTG 2009 |
| BVGer A-1526/2006 vom 28. Januar 2008 (parallel A-1525/2006 vom 28. Januar 2008) | 28.1.2008 | Art. 13 aMWSTG / Art. 11 MWSTV | Pauschale Berufung auf Reihengeschäfte | Unsubstantiierte Behauptung von «Reihengeschäfte[n] zwecks Ausfuhr von Uhren» genügt nicht | 3.3 (A-1525/2006: 3.1.3) | nicht ersichtlich | C | aMWSTG / MWSTV |

### 2.5 Kommission / Stellvertretung und Lieferort

| Entscheid | Datum | Normstelle | Sachfrage | Kernaussage + wörtlicher Kernsatz | E. | Weiterzug | Klasse | Fassung |
|---|---|---|---|---|---|---|---|---|
| BVGer A-1469/2006 vom 7. Mai 2008 | 7.5.2008 | Art. 10 Abs. 3, Art. 11 MWSTV 1994 | Verkaufskommission ins Ausland (Kunsthandel) | Zwei Lieferungen; Ort der ersten Lieferung = Beförderungsbeginn (Inland) → Ausfuhrnachweis nötig; beide Lieferungen erst bei Geschäft mit Drittem. «Auch bei einer Verkaufskommission direkt ins Ausland (als speziellen Fall der Beförderungslieferung) befindet sich namentlich der Ort der ersten Lieferung (d.h. derjenigen vom Kommittenten zum Kommissionär) dort, wo die Beförderung beginnt und damit grundsätzlich im Inland.» | 4.1.3, 4.1.4 | kein Weiterzug ersichtlich | A | MWSTV 1994 |
| BVGer A-4783/2015 vom 20. Februar 2017 | 20.2.2017 | Art. 7, Art. 20 MWSTG | Kunst-Auktionen im Ausland über Kommissionär | Beide Lieferungen am Ort, wo sich das Werk beim Geschäft mit dem Dritten befindet → Ausland. «la première livraison est réputée fournie au même lieu que la seconde, soit au lieu où se trouve le bien lorsque le représentant effectue l'opération avec le tiers.» | 4.2.2; 9.2.1.3 | BGer 2C_321/2017 vom 23. Mai 2018 (bestätigt) | A | MWSTG 2009 |

*Spannung zu prüfen:* A-1469/2006 (Kommissionsgut aus dem Inland versandt → erste Lieferung Inland, Ausfuhrnachweis) vs. A-4783/2015 (Werk bei Auktion im Ausland → beide Lieferungen Ausland). Unterschied liegt im Lageort bei Übergabe an den Kommissionär/Transportbeginn; im Kommentar abgrenzen.

### 2.6 Lieferung im Ausland, Ausland-Ausland-Geschäft, Abgrenzung zur Ausfuhr (Art. 23)

| Entscheid | Datum | Normstelle | Sachfrage | Kernaussage + wörtlicher Kernsatz | E. | Weiterzug | Klasse | Fassung |
|---|---|---|---|---|---|---|---|---|
| BVGer A-1455/2006 vom 25. April 2007 | 25.4.2007 | Art. 11, 15 Abs. 2 lit. a MWSTV 1994 | Inlandlieferung als Voraussetzung der Ausfuhr; Lieferung im Ausland | «Ainsi, lorsqu'un bien est transporté ou expédié de Suisse à l'étranger, il n'est soumis à la TVA suisse qu'à la condition que sa livraison ait été préalablement effectuée en Suisse.»; Auslandlieferung ausserhalb des Geltungsbereichs, Ort vom Steuerpflichtigen zu beweisen (E. 3.1.4) | 3.1.2–3.1.4 | nicht ersichtlich | A | MWSTV 1994 |
| BVGer A-1526/2006 vom 28. Januar 2008 | 28.1.2008 | Art. 13 aMWSTG | Direktversand ins Ausland = Inlandlieferung (nennt lit. a statt lit. b) | «Auch die Lieferung von Gegenständen, die aus dem Inland direkt ins Ausland versandt werden, gilt nach Art. 13 Bst. a MWSTG grundsätzlich als im Inland erbracht» | 2.5 | nicht ersichtlich | B | aMWSTG |
| BVGer A-2888/2016 vom 16. Juni 2017 | 16.6.2017 | Art. 7; Art. 23 Abs. 2 Ziff. 1, Abs. 3; Art. 81 Abs. 3 | Export vs. Ausland-Ausland; Beweismass | Ausfuhr setzt Inlandlieferung voraus (nur Satz 0 %); Ausland-Ausland: keine zollrechtlichen Obliegenheiten, freie Beweiswürdigung; Lautsprecher CZ→IT ausserhalb CH-MWST. «il se justifie en matière de preuve, de différencier les cas d'exportation des cas où l'opération est entièrement réalisée à l'étranger»; «Cette opération étant intégralement réalisée à l'étranger, elle est ainsi hors du champ d'application de la TVA Suisse.» | 5.3.1, 5.3.4, 5.4.2, 6.2.2 | BGer 2C_709/2017 vom 25. Oktober 2018 (bestätigt; nur Beweiswürdigung, E. 3.4.1) | A | MWSTG 2009 |
| SRK, Gericht CH JAAC 69.64 vom 2. November 2004 (SRK 2003-065; zit. als VPB 69.64) | 2.11.2004 | Art. 11 lit. a MWSTV 1994 | «Ausland-Ausland-Geschäft» Kunst (Auktion UK; Macke-Bild DE); Beweislast | Steuerpflichtiger muss Erwerb und Übertragung der Verfügungsmacht im Ausland lückenlos nachweisen; fehlender Nachweis ausländischer USt als Indiz. «Und zwar hat die Beschwerdeführerin lückenlos und zweifelsfrei darzutun, dass sie die wirtschaftliche Verfügungsmacht über das Bild im Ausland sowohl erworben als in der Folge auch übertragen hat.» | 4b/aa, 4b/bb | – (Rückweisung im Übrigen; Folgeentscheid A-1469/2006) | A | MWSTV 1994 |
| BVGer A-517/2012 vom 9. Januar 2013 | 9.1.2013 | Art. 13 lit. a aMWSTG | Flight Support: Treibstoff/Catering auf ausländischen Flughäfen | Einzelleistungen statt Aircraft-Management-Gesamtleistung; Lieferort Ausland, Rückerstattung. «Der Ort der Lieferungen liegt folglich im Ausland, wo diese Leistungen offensichtlich auch verbraucht worden sind.» | 2.4, 3.5, 3.6 | nicht ersichtlich | A | aMWSTG |

### 2.7 Energie (Abs. 2; altes Recht)

| Entscheid | Datum | Normstelle | Sachfrage | Kernaussage + wörtlicher Kernsatz | E. | Weiterzug | Klasse | Fassung |
|---|---|---|---|---|---|---|---|---|
| BVGer A-1612/2006 vom 9. Juli 2009 | 9.7.2009 | Art. 11 MWSTV 1994; Art. 13 aMWSTG | Strom aus F-Kernkraftwerken; Lieferung vs. Durchleitung (Dienstleistung); Lieferort | Strom ist Gegenstand; Verschaffung der Verfügungsmacht = Lieferung, reine Durchleitungsrechte = Dienstleistung; Beförderungslieferung: Einspeiseort, Abhollieferung: Zählerstandort; Spannungstransformation im Inland als Bearbeitung; Lieferort Ausland. «Als Lieferort von Versand- oder Beförderungslieferungen von Elektrizität gilt der Ort, wo der Produzent die Elektrizität ins Netz einspeist» | 2.5.2; 6.1.1; 6.1.2 | BGer 2C_561/2009 vom 25. März 2011 (abgewiesen; Lieferort nur referiert, E. 2.1) | A | MWSTV 1994 / aMWSTG (vor Abs. 2 MWSTG) |
| BVGer A-2036/2022 vom 6. Januar 2024; A-2037/2022 vom 15. Januar 2024 | 1/2024 | Art. 10 Abs. 2 lit. b MWSTG | nur Normwiedergabe (Steuerpflicht ausländischer Unternehmen, «Lieferung von Elektrizität in Leitungen, Gas über das Erdgasverteilnetz und Fernwärme an …») | – | 2.3.2 | nicht ersichtlich | C | MWSTG |

### 2.8 Gebrauchsüberlassung (Flugzeuge, Fahrzeuge, Kunst)

| Entscheid | Datum | Normstelle | Sachfrage | Kernaussage + wörtlicher Kernsatz | E. | Weiterzug | Klasse | Fassung |
|---|---|---|---|---|---|---|---|---|
| BVGer A-6971/2008 vom 8. Juni 2009 | 8.6.2009 | Art. 6 Abs. 2 lit. b, Art. 13 lit. a aMWSTG | Flugzeugmiete / Mietcharter | Lieferung; Ort = Standort bei Überlassung. «Sowohl die Flugzeugmiete als auch der "Mietcharter" sind mehrwertsteuerrechtlich als Lieferungen zu qualifizieren (Art. 6 Abs. 2 Bst. b MWSTG) und der Leistungsort richtet sich danach, wo sich das Flugzeug zum Zeitpunkt der Überlassung an den Dritten befand» | 2.1.2 | nicht ersichtlich | A | aMWSTG |
| BVGer A-6986/2008 vom 3. Juni 2010 | 3.6.2010 | Art. 13 lit. a aMWSTG | Mietcharter in Saudi-Arabien | «Die Flugzeuge wurden der C._______ unbestrittenermassen in Saudi-Arabien überlassen, wo sich somit auch der Leistungsort nach Art. 13 Bst. a aMWSTG befand.» | 5.2 | nicht ersichtlich | A | aMWSTG |
| BVGer A-2387/2007 vom 29. Juli 2010 | 29.7.2010 | Art. 13 lit. a aMWSTG | Charter/Miete; Positionierungsflüge (Ferry) | «En relation avec les vols de positionnement, la livraison intervient à l'endroit où l'avion se trouve avant la mise en route de ce vol» | 2.4.1 (Anwendung in E. 5) | nicht ersichtlich | A | aMWSTG |
| BVGer A-1667/2006 vom 23. Juni 2008 | 23.6.2008 | Art. 13 lit. a aMWSTG | Vercharterung vs. Beförderungsleistung | Vercharterung i.d.R. Lieferung, Ort beim Standort; hier mangels Nachweis Beförderung (Dienstleistung). «… und deren Ort richtet sich danach, wo sich das Flugzeug zum Zeitpunkt der Überlassung an den Dritten befand (Art. 13 Bst. a MWSTG).» | 3.3 | kein Weiterzug ersichtlich | B | aMWSTG |
| BVGer A-5745/2008 vom 11. Juni 2010 | 11.6.2010 | Art. 13 lit. a, Art. 19 Abs. 2 Ziff. 2 aMWSTG | Flugzeugmiete; Abgrenzung Aircraft Management (Dienstleistung) | Standardformel + Hinweis auf 2A.40/2007 | 2.4 | nicht ersichtlich | B | aMWSTG |
| BVGer A-4674/2010 vom 22. Dezember 2011 | 22.12.2011 | Art. 13 lit. a aLTVA | dito (fr.) | «Le lieu se situe alors là où l'avion se trouve au moment où il est mis à disposition du destinataire» | 2.3.1 | kein Weiterzug ersichtlich | B | aMWSTG |
| BVGer A-1536/2006 vom 16. Juni 2008 | 16.6.2008 | Art. 11 MWSTV 1994; Art. 13 aMWSTG | Überlassung Rennwagen samt Rennservice (Gesamtleistung) | Ort am ausländischen Veranstaltungsort, auch wenn Revisionen im Inland. «Der Ort der Lieferung des "kompletten Rennservices" liegt folglich im Ausland (vgl. E. 2.4.1), selbst wenn einzelne Arbeiten (Fahrzeugrevisionen in der Werkstatt) im Inland ausgeführt werden.» | 3.2.5 | kein Weiterzug ersichtlich | A | MWSTV / aMWSTG |

### 2.9 Werklieferung / Arbeiten an Gegenständen / Montage

Kein BVGer- oder SRK-Entscheid zum Lieferort bei Werklieferung mit Montage gefunden (Suche Nr. 13). Nur: A-4388/2014 E. 4.1 (lit. a gilt für Art. 3 lit. d Ziff. 2) und A-4898/2018 E. 7.3.2 (ESTV-Auskunft zu Triebwerkskontrolle, lit. a) – beide Klasse B/C (s. Tabelle 2.1). Lücke → BGer/Praxis/Lehre.

## 3. Fehltreffer (Auswahl, geprüft)

- **Art. 7 aMWSTG 1999 = Dienstleistungsbegriff** («Als Dienstleistung gilt jede Leistung, die keine Lieferung eines Gegenstandes ist»): A-2458/2009, A-1489/2006, A-1667/2006 E. 2.1, A-1350/2006, A-8437/2007, A-517/2012 E. 2.2, A-3190/2008 E. 2.1, A-3031/2013; Art. 7 Abs. 2 aMWSTG (immaterielle Werte): A-1350/2006, A-1558/2006, A-1540/2006; Kanton AG SVWG EB.2000.50030 und EB.2000.50011.
- **«Unterstellungserklärung» = Saldosteuersatz-Bewilligung:** A-1377/2006, A-2541/2008, A-5751/2009, A-1403/2006, A-2859/2019, A-5384/2014, A-4728/2011, A-6602/2010, A-5727/2024, A-1633/2006, A-1624/2006, A-2323/2018, A-1366/2006.
- **Zoll/Einfuhr ohne Art. 7:** A-2677/2007 (Inlandbegriff Flughafen Basel-Mülhausen, Art. 3 aMWSTG), A-6593/2024 (AEV/Kontingente; «Reihengeschäft» nur im Volltext ohne Erwägung), A-7503/2016, A-7049/2015, A-4077/2021, A-5216/2014, A-983/2018, A-714/2018.
- **Sonstiges ohne Lieferort:** A-683/2025 (Saldosteuersatz Weinbau; Verfügungsmacht nur als Vorinstanz-Argument), A-4643/2023 (Saillie-Rechte = Dienstleistung, E. 7.2.7; BGer 9C_370/2025), A-5601/2019 (Edelmetall-Lohnveredelung, Verfügungsmacht), A-2220/2008 (Goldlagergebühren), A-6692/2012 (Ort der Dienstleistung, art. 14 aLTVA), A-713/2017 (Telekom-Bezugsteuer), A-4090/2016 (Feststellungsinteresse; Lieferort nur erwähnt, E. 8.2), A-4569/2020 (Mineralölsteuer-Rückerstattung; nur Normwiedergabe), A-3285/2017, A-6743/2009, A-135/2011.
- **SRK/ZRK:** Gericht CH JAAC 67.42 vom 7. Oktober 2002 (ZRK, Reisegut; zitiert nur EFD-Kommentar zum Versendungsbegriff ad Art. 11 lit. b MWSTV, E. 4); JAAC 62.48 (WUST, Entgelt bei Kettengeschäften).
- **Entscheidsuche «Versandhandel»/«vente par correspondance» (140) und alle kantonalen Treffer:** IV-Verweisungstätigkeiten, Markenrecht, OR-Erfüllungsort/Incoterms (ZG OG Z1 2022 5, Z1 2025 22; SO OG ZKBER.2019.71), Strafrecht (BetmG).

## 4. Offene Punkte für den Hauptagenten

- BGer 2C_266/2019 und 2C_1079/2016 (Cache) daraufhin lesen, welche Teile von A-2106/2017 (insb. E. 4.2.3.2 Vollzugskompetenz für Art. 3 MWSTV a.F.) und A-2675/2016 (Art. 4 MWSTV, Bemessung) überholt sind.
- BGE 148 II 233 (Cache) mit Vorinstanz A-601/2019 verknüpfen (BVGer äusserte sich nicht zum Ort).
- Zu Abs. 2 n.F. (2018), Abs. 3 lit. b (Versandhandel) und Werklieferung: Verwaltungspraxis (MWST-Info 06, BAZG 52.25/R-69-01) heranziehen – keine Rechtsprechung.
