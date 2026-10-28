# Entscheidregister Art. 6 VStG (SR 642.21)

Stand der Recherche: 28.10.2026. Gegenstand: Verrechnungssteuer auf Gewinnen aus Geldspielen sowie aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung (geltende Fassung seit 1.1.2019); vorher «Lotteriegewinne» (Geldtreffer über Fr. 50, ab 1.1.2014 über Fr. 1000, aus Lotterien im Inland; Abs. 2 alt: gewerbsmässige Wetten und lotterieähnliche Veranstaltungen gleichgestellt).

Zitierstrings für BGer/BGE sind wörtlich aus `citation_string_de` bzw. `cite` (Open Case Law) übernommen. Kantonale Entscheide und BVGer stammen ausschliesslich aus Entscheidsuche (fetch_document gelesen); die Zitierform ist nach der Vorgabe «Gericht Kanton Geschäftsnummer vom Datum, E. x» gebildet.

## 1. Suchwege und Trefferzahlen

**Lokaler Cache** `data/entscheide/` (66 JSON-Dateien): Regex `Art. 6 (Abs. 1/2) VStG | art. 6 (al. 1/2) LIA | Lotterie | loterie` → 6 Dateien mit Treffer (2C_1030/2013, 2C_42/2014, 2C_404/2015, 2C_320/2018, 2C_328/2018, 2C_342/2018). BGE 139 I 280 und 2C_794/2012 liegen im Cache, haben aber nur «Art. 6 LIP/GE».

**Open Case Law (BGer/BGE)**, search_decisions:

| Abfrage | Filter | Treffer |
|---|---|---|
| `"Art. 6 VStG"` | court bger | 1 (2C_404/2015) |
| `"art. 6 LIA" loterie` | court bger | 139+ (fast nur Rauschen; einschlägig: 2C_1030/2013, 2C_42/2014, 2C_89/2014, 2C_930/2015, 2A.242/2005) |
| `Lotteriegewinn Verrechnungssteuer` | court bger | 228+ (einschlägig: 2C_80/2012, 2C_465/2018-Umfeld; Rest Art. 23 VStG allgemein) |
| `"impôt anticipé" "gains de loterie"` | court bger | 204+ (einschlägig: 2C_42/2014, 2A.242/2005, 2C_89/2014, 2C_1030/2013, 2C_930/2015) |
| `"paris professionnels" "impôt anticipé"` | alle | 196+ (keine neuen VStG-Entscheide; meist Strafrecht LLP) |
| `lotterieähnlich* Verrechnungssteuer` | alle | 166+ (einschlägig: 2A.108/2002; SG I/2-2006/7) |
| `Geldspielgewinn* Verrechnungssteuer` | alle | 162+ (keine einschlägigen BGer-Entscheide) |
| `"Art. 21 Abs. 1 lit. b VStG"` | alle | 1 (SG I/2-2006/7) |
| `Verrechnungssteuer Geldspiel OR Spielbank OR Geschicklichkeitsspiel OR Verkaufsförderung OR "Art. 20a VStG"` | bger, ab 1.1.2019 | 89+ (kein Treffer zu Art. 6/20a VStG) |
| `regeste:Verrechnungssteuer AND (Lotterie* OR Geldspiel* OR Lotto*)` | bger | 68+ (nur Geldspiel-/Lotterieaufsichtsrecht) |
| `"Billet Le Million" ...` | bger, ab 2018 | 61 (Rauschen; kein Weiterzug von CDAP VD FI.2016.0148 gefunden) |

Zusätzlich gelesen: BGE 71 I 362 (über Entscheidsuche-Treffer gefunden, Zitierstring aus `cite`), BGE 113 Ib 128, BGE 125 II 348, BGE 138 II 536 E. 5.1, 2C_14/2014 E. 3.1 (Prüfung eines Verweises in 2C_89/2014).

**Entscheidsuche (kantonale Gerichte, BVGer)**, search:

| Abfrage | Filter | Treffer |
|---|---|---|
| `Verrechnungssteuer AND (Geldspiel* OR Lotteriegewinn* OR Lottogewinn* OR Spielbank* OR Jackpot OR Sportwette*)` | Entscheiddatum ab 1.1.2019 | 8 (einschlägig: VGer GR A 23 15; Rest Art. 23 VStG, Zivil-/Strafrecht) |
| `"Art. 6 VStG" OR "Art. 6 Abs. 1 VStG" OR "art. 6 LIA" OR "art. 6 al. 1 LIA" OR "art. 6 LIP" OR "Art. 6 des Bundesgesetzes über die Verrechnungssteuer"` | alle | 16 (einschlägig: SG I/2-2006/7, GE A/1344/2010, GR A 23 15, TI 80.2011.27, BGer 2C_1030/2013, 2C_42/2014; 10 Fehltreffer) |
| `Verrechnungssteuer AND (lotterieähnlich* OR "gewerbsmässige Wetten" OR "Eigentümer des Loses" OR Geschicklichkeitsspiel* OR Verkaufsförderung OR Naturalgewinn*)` | alle | 8 (einschlägig: SG, GR, ZG [Fehltreffer], BL [nur Zitat Art. 21], 2A.108/2002) |
| `"impôt anticipé" AND ("paris professionnels" OR "analogues aux loteries" OR "jeux d'argent" OR "propriétaire du billet" OR "gains de loterie")` | alle | 10 (neu: CDAP VD FI.2016.0148, VD FI.1996.0033) |
| `("imposta preventiva" AND (lotteri* OR vincit* OR "giochi in denaro")) OR (Verrechnungssteuer AND Lotterie* AND Bundesverwaltungsgericht)` | alle | 13 (neu: CDT TI 80.2003.145; BGE 71 I 362) |
| `Verrechnungssteuer AND (Lotteriegewinn* OR Lottogewinn*)` | ZH_SRK | 4 (nur Art. 23 VStG) |
| `Verrechnungssteuer AND (Lotterie* OR Geldspiel* OR Spielbank* OR Wette* OR Verlosung OR Wettbewerb*)` | CH_BVGE | 39 (keiner einschlägig; «Wettbewerb» aus Drittvergleich bei geldwerten Leistungen) |

Ergebnis der Recherche: **Seit 1.1.2019 gibt es weder beim Bundesgericht noch beim BVGer einen Entscheid, der Art. 6 VStG in der geltenden Fassung auslegt.** Einziger Entscheid zur geltenden Fassung ist VGer GR A 23 15 (2023), und auch dort nur als Anwendung. Die Bundesgerichtspraxis zu Lotteriegewinnen betrifft fast nur die Rückerstattung (Art. 21 Abs. 1 lit. b, Art. 23, Art. 29–32, Art. 57 f. VStG). Art. 6 wird darin höchstens im Normprogramm wiedergegeben.

## 2. Register

Klassen: A = legt Art. 6 bzw. den Steuergegenstand aus; B = wendet ihn an; C = erwähnt ihn bloss bzw. betrifft nur das Umfeld (Rückerstattung).

### 2.1 Bundesgericht

| Entscheid (Zitierstring aus Tool) | Datum | Gericht/Besetzung | Normstelle | Sachfrage | Kernaussage | E. | Ergebnis | Kl. | Fassung (Periode) |
|---|---|---|---|---|---|---|---|---|---|
| BGer 2C_1030/2013 vom 28. Mai 2014, E. 2.1 | 28.5.2014 | II. öffentlich-rechtliche Abteilung, 3er (Zünd, Donzallaz, Stadelmann) | Art. 6 LIA (im Normprogramm); Art. 29 Abs. 3, 30 Abs. 1 LIA | Rückforderung der VSt auf Lotterie-/PMU-/Tactilo-Gewinnen nach Wohnsitzwechsel VS→FR, wenn sie vorzeitig vom unzuständigen Kanton erstattet wurde | Die VSt auf Lotteriegewinnen, «à quoi sont assimilés les paris professionnels et autres opérations analogues aux loteries», erfasst Barlose über Fr. 1000 aus Lotterien in der Schweiz; entschieden wird nur die Zuständigkeit (Art. 29 Abs. 3 als Ausnahme zu Art. 30 Abs. 1 LIA). | 2.1 (Art. 6); 2.3–2.5 (tragend) | Beschwerde gutgeheissen, keine Rückleistung | C | alt; Gewinne 2006. Anachronismus: zitiert wird die Schwelle von Fr. 1000 (gültig ab 2014), für 2006 galt Fr. 50 |
| BGer 2C_42/2014 vom 17. Oktober 2014, E. 3.1 | 17.10.2014 | II. öffentlich-rechtliche Abteilung, 3er (Zünd, Aubry Girardin, Stadelmann) | Art. 6 Abs. 1 und 2 LIA (Normprogramm); Art. 21 Abs. 1 lit. b, 22, 48, 57 f. LIA | Rückleistung erstatteter VSt bei Strohmann-Gesuch (prête-nom) auf fremden Lotterie- und PMU-Losen | Abs. 2 alt stellt den Lotterien die «paris professionnels et autres opérations analogues aux loteries (sport-toto, etc.)» gleich. «Eigentümer» des Loses (Art. 21 Abs. 1 lit. b) meint Eigentum im zivilrechtlichen Sinn (Art. 641 ZGB). Wer eine Simulation selbst geschaffen hat, kann sich nicht auf sie berufen (E. 3.4). | 3.1 (Art. 6); 3.3–3.4 (tragend) | abgewiesen | C | alt; Gewinne bis 2007. Anachronismus wie oben (Fr. 1000) |
| BGer 2C_89/2014 vom 26. November 2014, E. 6.2 | 26.11.2014 | II. öffentlich-rechtliche Abteilung, 3er (Zünd, Aubry Girardin, Stadelmann) | Art. 21 Abs. 1 lit. b, 48, 52, 57 LIA; Art. 60 Abs. 2 VStV (Spielgemeinschaft) | Rückleistung von 90 % der erstatteten VSt auf Lotterie-/PMU-Gewinnen, deren Lose zugekauft waren (Losehandel) | Rückerstattung nur, wer bei der Ziehung Eigentümer des Loses war; bei gemeinsamer Einsatzleistung muss jeder Teilnehmer nach Art. 60 Abs. 2 VStV anteilig beantragen. Die Schätzung der Rückleistung durch Stichproben und Extrapolation ist zulässig (E. 7.4). Art. 6 wird nicht genannt. | 6.2, 6.3, 7.2–7.4 | abgewiesen | C | alt; 2004–2006 |
| BGer 2C_930/2015 vom 26. November 2015, E. 6 | 26.11.2015 | II. öffentlich-rechtliche Abteilung, 3er (Zünd, Seiler, Stadelmann), Verfahren nach Art. 109 BGG | Art. 21 Abs. 1 lit. b, 48, 57 f. LIA | gleicher Sachverhaltskomplex (VS); Rückleistung 70 % | Wer wissentlich Gewinnlose vorlegt, die ihm bei der Ziehung nicht gehörten, kann sich nicht auf Treu und Glauben berufen; die Schätzungsmethode wird bestätigt. Art. 6 wird nicht genannt. | 6, 7 | abgewiesen, soweit eingetreten | C | alt; 2004–2007 |
| BGer 2A.242/2005 vom 17. März 2006, E. 4.1 | 17.3.2006 | II. öffentlich-rechtliche Abteilung, 5er (Merkli, Wurzburger, Müller, Yersin, Meylan) | Art. 21 Abs. 1 lit. b, 22 Abs. 1, 48 LIA | Umfang der Rückerstattung bei rund 10'000 vorgelegten PMU- und Lotteriecoupons | Den Nachweis, bei der Ziehung Eigentümer des Loses gewesen zu sein, trägt der Antragsteller; eine Rückerstattung auf Basis von 10 % der Gewinne nach Stichprobe und Extrapolation ist zulässig (E. 4.2). | 4.1, 4.2 | abgewiesen, soweit eingetreten | C | alt; 1997 (Schwelle Fr. 50) |
| BGer 2C_80/2012 vom 16. Januar 2013, E. 2.1 | 16.1.2013 | II. öffentlich-rechtliche Abteilung, 3er (Zünd, Seiler, Kneubühler) | Art. 10, 14, 22, 23 VStG | Lottogewinn Fr. 7,5 Mio.; Verwirkung der Rückerstattung nach rechtskräftiger Ermessensveranlagung ohne Deklaration des Gewinns | Die VSt wird an der Quelle erhoben; wird der Lottogewinn nicht vor Rechtskraft der Veranlagung deklariert, verwirkt die Rückerstattung (E. 2.2, 6). Art. 6 wird nicht genannt. | 2.1, 2.2, 6 | abgewiesen | C | alt; Gewinn 2006 |
| BGer 2C_465/2018 vom 31. Mai 2018, E. 1.3 | 31.5.2018 | II. öffentlich-rechtliche Abteilung, Einzelrichter (Präsident Seiler, Art. 108 BGG) | Art. 23, 56 VStG | Verwirkung der Rückerstattung auf Lotteriegewinnen 2014 mangels Steuererklärung | Weil die Begründung fehlt, tritt das Gericht nicht ein. Wiedergegeben wird nur die Auffassung der Vorinstanz, wonach die Nichtdeklaration der Lotteriegewinne zur Verwirkung führt (Art. 23 VStG). | 1.3, 2.4–2.5 | Nichteintreten | C | Fassung 2014 (Schwelle Fr. 1000) |
| BGE 113 Ib 128, E. 2d | 10.7.1987 | II. öffentlich-rechtliche Abteilung (Besetzung nicht ausgewiesen) | Art. 1 Abs. 1, 23, 32 VStG | Verwirkung bei Ermessenseinschätzung (Wertschriftenerträge, kein Lotteriefall) | Sind Kapitalerträge, Lotteriegewinne und Versicherungsleistungen deklariert, wird die VSt zurückerstattet, gleichgültig wie viel übriges Einkommen hinterzogen ist. | 2d | gutgeheissen | C | alt |
| BGE 71 I 362, E. 1 | 21.9.1945 | Verwaltungsgerichtsbeschwerde (Besetzung nicht ausgewiesen) | Art. 6bis Abs. 1 VStB 1943 | Wann wird die VSt auf Lostreffern über Fr. 50 fällig, wenn das Lotteriereglement die Fälligkeit an die Vorweisung knüpft? | Die VSt wird mit der zivilrechtlichen Fälligkeit des Lostreffers fällig. Die Parteien können den Zeitpunkt festlegen, nicht aber den Begriff der Fälligkeit ändern: Der Treffer ist fällig, sobald der Gewinner die Zahlung verlangen kann, auch wenn er das Los nicht vorweist. | 1 | abgewiesen | B | VStB 1943 (Vorläufer; Lostreffer über Fr. 50) |
| BGer 2A.108/2002 vom 11. Juli 2002, E. 2.1 | 11.7.2002 | II. öffentlich-rechtliche Abteilung, 5er (Wurzburger, Betschart, Müller, Yersin, Merkli) | Art. 218 Abs. 3 DBG (nicht VStG); Art. 43 Ziff. 2 LV 1924 | Sind Sport-Toto-Gewinne eines «professionellen» Tippers Lotteriegewinne bzw. Gewinne aus lotterieähnlichen Veranstaltungen? | Sport-Toto ist eine lotterieähnliche Veranstaltung; dass Fachkenntnisse die Gewinnchance erhöhen, ändert am überwiegenden Zufallscharakter nichts. Die Einmaligkeit ist bei Lotteriegewinnen kein Tatbestandsmerkmal (E. 2.4). | 2.1, 2.4 | gutgeheissen (ESTV) | C (mittelbar: Begriff «lotterieähnlich», für Abs. 2 alt verwertbar) | DBG; 1997 |

### 2.2 Bundesverwaltungsgericht

| Entscheid | Datum | Gericht/Besetzung | Normstelle | Sachfrage | Kernaussage | E. | Ergebnis | Kl. | Fassung |
|---|---|---|---|---|---|---|---|---|---|
| BVGer A-1758/2011 vom 26.3.2012, E. 3.4 (Entscheidsuche CH_BVGE_001_A-1758-2011_2012-03-26) | 26.3.2012 | Abt. I, 3er (Riedo, Beusch, Zimmermann) | Art. 167 DBG (Erlass); VSt nur im Sachverhalt | Erlass der DBG auf Lottogewinn 2002 (Fr. 1,33 Mio.) | Die vom Bruttogewinn abgezogene VSt (Fr. 464'167.55) begründet keinen weiteren Erlassgrund. | 3.4 | abgewiesen; nicht weiterziehbar (Art. 83 lit. m BGG) | C | alt; 2002 |

### 2.3 Kantonale Gerichte

| Entscheid | Datum | Gericht/Besetzung | Normstelle | Sachfrage | Kernaussage | E. | Ergebnis | Kl. | Fassung | Weiterzug |
|---|---|---|---|---|---|---|---|---|---|---|
| VGer GR A 23 15 vom 22.8.2023, E. 4.1 | 22.8.2023 | VGer GR, 4. Kammer, 3er (Audétat, Stöhr, Brun) | Art. 1 Abs. 1 i.V.m. Art. 6 VStG; Art. 20a VStG; Art. 24 lit. j DBG | Naturalgewinn (Auto, Wert Fr. 105'000) aus einer Zuschauerverlosung der SRG bei einem Formel-1-Rennen, gemeldet per Formular «Verrechnungssteuer auf Naturalgewinnen von im Inland veranstalteten Geschicklichkeitsspielen zur Verkaufsförderung»; Streitpunkt ist das Zuflussjahr (2021 oder 2022) | Bei Naturalgewinnen aus Lotterien und Geschicklichkeitsspielen, die nicht nach Art. 24 lit. j DBG steuerfrei sind, erfüllt die Veranstalterin die Steuerpflicht durch Meldung; die ESTV leitet die Meldung an den Wohnsitzkanton weiter (Art. 20a VStG). Das Einkommen fliesst erst mit dem Eigentumserwerb 2022 zu, weil aus Spiel keine durchsetzbare Forderung entsteht (Art. 513 OR; E. 4.5–4.7). | 4, 4.1 (VStG); 4.2–4.7 (tragend, Zufluss) | gutgeheissen (Staats- und Gemeindesteuern); Nichteintreten DBG | B | **geltend**; Steuerperiode 2021 | nicht ermittelt |
| VRK SG I/2-2006/7 vom 29.9.2006, E. 3b | 29.9.2006 | Verwaltungsrekurskommission SG, 3er (Steppacher, Koller, Lippuner); publ. SGE 2006 Nr. 19 | Art. 1, 6, 21 Abs. 1 lit. b, 22 Abs. 1, 23, 30 VStG | Swisslos-Lottogewinn (Fr. 15'329.90) aus der Ziehung vom 15.10.2003, ausbezahlt am 7.1.2004, erst in der Steuererklärung 2004 deklariert | Gegenstand sind ausgerichtete Geldtreffer über Fr. 50 aus Lotterien im Inland (Art. 6). Fällig ist der Gewinn, sobald das Trefferlos vorgewiesen werden kann (hier am Tag nach der Ziehung); der Auszahlungszeitpunkt ist unerheblich (E. 3d/aa–bb). Keine Verwirkung, weil die Behörde den Gewinn 2004 nach der Deklaration besteuert hat (widersprüchliches Verhalten, E. 3d/cc). | 3b (Art. 6); 3d (tragend) | gutgeheissen | B | alt; Fälligkeit 2003 / Veranlagung 2004 | nicht ermittelt |
| CDAP VD FI.2016.0148 vom 5.2.2018, consid. 4b und 6b/cc | 5.2.2018 | CDAP VD, 3er (Vianin, Briguet, Perrigault) | Art. 1, 21 Abs. 1 lit. b, 23, 32 Abs. 1 LIA; Art. 1 Abs. 2 LLP | Gewinn von Fr. 1 Mio. aus dem Rubbellos «Billet Le Million» der Loterie Romande (Adventskalender, Gewinntag 24.12.2011), nicht deklariert | Bei einem Los mit Vorausziehung ist der Gewinn an dem Tag erworben, an dem das Symbol auf dem Los mit dem publizierten Symbol übereinstimmt; Rubbeln und Prüfung bestätigen den Anspruch nur (consid. 4b). Der Lotteriegewinn ist fällig, sobald der Spieler gegen Vorweisung des Gewinnloses die Zahlung verlangen kann (consid. 6b/cc, mit Hinweis auf BGE 71 I 364). Die Verwirkung nach Art. 23 LIA und die verspätete Antragstellung nach Art. 32 LIA werden bejaht. | 4b, 6a–6b | abgewiesen | B (Zeitpunkt/Fälligkeit des Steuerobjekts) | alt; Steuerperiode 2011 (Schwelle Fr. 50) | nicht ermittelt |
| CDT TI 80.2011.27 vom 9.5.2011, consid. 2.2 | 9.5.2011 | Camera di diritto tributario TI, 3er (Pedroli, Bernasconi, Mini) | Art. 22 lett. e, 36 LT/TI; Art. 23 lett. e, 16 LIFD; Art. 6 LIP (obiter); Art. 1 LLS, Art. 43 OLLS | Ist der Gewinn aus einem RSI-Fernsehquiz (Fr. 3200) ein Lotteriegewinn (Jahressteuer) oder ordentliches Einkommen? | Ein Quiz, bei dem Geschicklichkeit und Wissen überwiegen, ist keine Lotterie und keine lotterieähnliche Veranstaltung; Fernsehquiz fallen in der Regel nicht unter den Lotteriebegriff (mit Verweis auf Bürgy/Helbing, N 15 zu Art. 6 LIP). Entsprechend wurde keine VSt nach Art. 6 LIP erhoben. | 1.3–1.4, 2.2 | abgewiesen | B (Abgrenzung des Begriffs, obiter) | alt (Abs. 2 alt); 2009 | nicht ermittelt |
| CJ GE ATA/550/2012 (A/1344/2010) vom 21.8.2012, consid. 6 | 21.8.2012 | Chambre administrative, 2e section, 3er (Hurni, Junod, Dumartheray) | Art. 4, 6 Abs. 1, 7, 10, 31 Abs. 4 LIA | Vergütungszins auf Überzahlungen der Kantons- und Gemeindesteuern 2008, wenn eine VSt-Anrechnung mit im Spiel ist (kein Lotteriefall) | Art. 6 Abs. 1 LIA wird nur im Normprogramm wiedergegeben («lots en espèces effectivement payés dépassant le montant de CHF 50.-»). | 6 | gutgeheissen | C | alt; 2008 | nicht ermittelt |
| CJ GE ATA/219/2013 (A/2068/2011) vom 9.4.2013, consid. 2a | 9.4.2013 | Chambre administrative, 1re section, 3er (Thélin, Junod, Verniory) | Art. 1, 12, 21 Abs. 1 lit. b, 23, 29, 32 LIA | Gewinne aus PMU und Loto express 2009; Belege beigelegt, aber nicht im Wertschriftenverzeichnis aufgeführt | Ein nachträgliches Schreiben ist als Rückerstattungsantrag (Art. 29 LIA) zu behandeln, nicht als verspätete Einsprache; die Sache wird an die kantonale Verwaltung zurückgewiesen. Art. 6 wird nicht genannt. | 2–5 | teilweise gutgeheissen | C | alt; 2009 | nicht ermittelt |
| CDAP VD FI.2015.0026 vom 10.8.2015, consid. 3a | 10.8.2015 | CDAP VD, 3er (Kaltenrieder, Maillard, Jahrmann) | Art. 23 lit. e LIFD (bis 2013); Art. 21 Abs. 1 lit. b LIA (indirekt) | Abzug verlorener PMU-Einsätze 2010/2011 | Einsätze sind nur abziehbar, wenn der Steuerpflichtige nachweist, dass er die Coupons selbst finanziert hat; die VSt ist nicht streitig (consid. 4). | 3, 4 | abgewiesen | C | alt; 2010–2011 | BGer 2C_803/2015 und 2C_804/2015 vom 16.9.2015: Nichteintreten (laut Abstract Entscheidsuche) |
| CDAP VD FI.2023.0019 vom 6.10.2023, consid. 6a | 6.10.2023 | CDAP VD, 3er (Vianin, Jahrmann, Saul) | Art. 1, 22, 29–31 Abs. 4 LIA | Rubbellosgewinn Fr. 800'000 (Loterie Romande, Rento) 2009: Einsatzabzug und Verzinsung der VSt-Rückerstattung | Die VSt-Rückerstattung wird erst mit rechtskräftiger Veranlagung angerechnet und nicht verzinst (Art. 31 Abs. 4 LIA). Art. 6 wird nicht genannt. | 5, 6 | sehr teilweise gutgeheissen (formell) | C | alt; 2009 | nicht ermittelt |
| OGer AR O2V 16 9 vom 13.12.2016, E. 2.1 | 13.12.2016 | Obergericht AR, 2. Abteilung, 5er (Zingg, Krapf, Dick, Plachel, Winiger) | Art. 1, 23 VStG; KS ESTV Nr. 40 | Swisslos-Lottogewinn 2014 (Fr. 21'738.90); Gewinnbescheinigung beigelegt, aber nicht ins Wertschriftenverzeichnis übertragen | Das Beilegen der Swisslos-Gewinnbescheinigung ist eine spontane Angabe im Sinn von Art. 23 VStG; die Verweigerung der Rückerstattung ist überspitzt formalistisch. | 2.1–2.3 | gutgeheissen | C | Fassung 2014 (Schwelle Fr. 1000) | nicht ermittelt |
| CDT TI 80.2003.145 vom 21.1.2004, consid. 4.2 | 21.1.2004 | Camera di diritto tributario TI, 3er (Soldini, Bernasconi, Ranzanici) | Art. 21 cpv. 1 lett. b, 22 cpv. 2, 29, 32 LIP; Art. 51 OIPrev | Lottogewinn Fr. 541'386 (Swiss Lotto, 1999) einer quellenbesteuerten Person, die erst 2003 die Rückerstattung beantragt | Wer in der Schweiz nur Aufenthalt hat, ist rückerstattungsberechtigt (Art. 51 Abs. 1 VStV); der Anspruch ist aber nach Art. 32 LIP erloschen. Eine falsche Auskunft des Lotterieveranstalters begründet keinen Vertrauensschutz. | 4.2–5.5 | abgewiesen | C | alt; 1999 | nicht ermittelt |

## 3. Tragende Passagen (wörtlich)

### Klasse B

**VGer GR A 23 15 vom 22.8.2023, E. 4 und E. 4.1**
> «Zwischen den Parteien ist zurecht unbestritten, dass der Gewinn der Gemeinde-, Kantons- und Bundessteuer unterliegt (vgl. Art. 1 Abs. 1 i.V.m. Art. 6 des Bundesgesetzes über die Verrechnungssteuer [VStG]; SR 642.21), weshalb diesbezüglich keine Ergänzungen des Gerichts erforderlich sind.» (E. 4)
> «Dies ergibt sich aus dem Formular "Verrechnungssteuer auf Naturalgewinnen vom im Inland veranstalteten Geschicklichkeitsspielen zur Verkaufsförderung", auf welchem die ESTV den Gewinn an die kantonale Steuerverwaltung gemeldet wurde. Das VStG sieht vor, dass die Veranstalterin bei Naturalgewinnen aus Lotterien und Geschicklichkeitsspielen, die nicht nach Art. 24 lit. j DBG steuerfrei sind, die Steuerpflicht durch Meldung der steuerbaren Leistung zu erfüllen hat. Die ESTV leitet die Meldung an die Steuerbehörde des Wohnsitzkantons des Gewinners weiter (Art. 20a VStG), was vorliegend auch erfolgt ist.» (E. 4.1)

Hinweis: E. 4 leitet aus Art. 1 i.V.m. Art. 6 VStG unscharf die Einkommenssteuerpflicht ab. Ob die Verlosung, an der der Teilnehmer erst nach dem Beantworten von Fragen teilnehmen konnte, eine Lotterie oder ein Geschicklichkeitsspiel ist, prüft das Gericht nicht; es folgt der Qualifikation im Meldeformular.

**VRK SG I/2-2006/7 vom 29.9.2006, E. 3b und E. 3d/aa**
> «Gegenstand der Verrechnungssteuer auf Lotteriegewinnen sind ausgerichtete Geldtreffer von über Fr. 50.-- aus Lotterien, die im Inland zur Durchführung gelangen (Art. 6 VStG). Natürliche Personen haben im Fall eines Lotteriegewinns Anspruch auf Rückerstattung der Verrechnungssteuer, wenn sie bei Fälligkeit der steuerbaren Leistung im Inland Wohnsitz hatten (Art. 22 Abs. 1 VStG) und wenn sie im Zeitpunkt der Ziehung Eigentümer des Loses waren (Art. 21 Abs. 1 lit. b VStG).» (E. 3b)
> «Trefferlose können in aller Regel sogleich nach der Ziehung oder einige Tage später zum Inkasso präsentiert werden. Mit dem Eintritt des Zeitpunktes, von dem an der Gewinner die Erfüllung fordern und das Trefferlos vorweisen kann, entsteht die Verrechnungssteuerforderung. Unerheblich ist, wann die Auszahlung tatsächlich gefordert wird bzw. effektiv erfolgt (W. Pfund, Verrechnungssteuer I. Teil, Basel 1971, N 2.1 und 2.21 zu Art. 12 VStG).» (E. 3d/aa)

**CDAP VD FI.2016.0148 vom 5.2.2018, consid. 4b und 6b/cc**
> «Dans un jeu de loterie à prétirage, c'est-à-dire dont le tirage au sort a eu lieu avant la mise en vente des billets (art. 2.1 RG), c'est en effet après cette publication que le joueur peut constater que son billet est gagnant, en comparant les symboles publiés avec ceux figurant sur le billet. Ce moment est ainsi déterminant pour la naissance du droit […].» (consid. 4b)
> «Selon la doctrine et la jurisprudence, en effet, un gain de loterie est exigible au moment où le joueur peut en exiger le versement en présentant le billet gagnant (Bürgy/Helbing, in: Zweifel/Athanas/Bauer-Balmelli [éd.], Kommentar zum Schweizerischen Steuerrecht II/2, Bundesgesetz über die Verrechnungssteuer, 2005, no 32 ad art. 21 LIA, avec renvoi à l'ATF 71 I 364). En l'occurrence, compte tenu de ce qui figure au considérant 4b ci-dessus, le gain était exigible dès le 24 décembre 2011.» (consid. 6b/cc)

**CDT TI 80.2011.27 vom 9.5.2011, consid. 2.2**
> «Determinante è piuttosto che il contributo del concorrente presupponga un suo serio impegno, nel senso che la sua abilità, le sue capacità, le sue conoscenze, la sua perseveranza ecc. siano decisivi per il suo successo, facendo passare in secondo piano la componente aleatoria. Pertanto, di solito gli spettacoli televisivi a quiz non rientrano nella nozione di lotterie (Bürgy/Helbing, in: Zweifel/Athanas [a cura di], Kommentar zum Schweizerischen Steuerrecht, vol. II/2, Basilea 2005, n. 15 ad art. 6 LIP, p. 293). Non risulta, d'altronde, che la vincita in discussione sia stata assoggettata all'imposta preventiva, che è trattenuta sulle vincite alle lotterie, alle scommesse professionalmente organizzate e alle altre operazioni affini (art. 6 della Legge federale sull'imposta preventiva del 13 ottobre 1965 [LIP; RS 642.21]).»

**BGE 71 I 362, E. 1**
> «Nach Art. 6 bis, Abs. 1, Satz 1 VStB verfällt die Verrechnungssteuer in dem Zeitpunkt, in dem die steuerbare Leistung fällig wird. Unter der Fälligkeit der steuerbaren Leistung ist die zivilrechtliche Fälligkeit verstanden. […] Allein die Vertragsfreiheit gibt den Beteiligten nur die Möglichkeit, die Fälligkeit zeitlich festzulegen, nicht aber, einen neuen Begriff der Fälligkeit zu prägen. […] Die Bestimmung, dass der Gewinn erst mit der Vorweisung fällig werde, ist ein untaugliches Mittel, die Fälligkeit zu vereinbaren.»
(Die OCR-Fehler der Vorlage, etwa «Zeitpuukt~», «Leistuug», sind hier stillschweigend berichtigt; vor der Verwendung am Original prüfen.)

### Klasse C, für die Kommentierung trotzdem nützlich

**BGer 2C_42/2014 vom 17. Oktober 2014, E. 3.1** (`rule_statement` aus `cite`)
> «L'impôt anticipé sur les gains faits dans les loteries, à quoi sont assimilés les paris professionnels et autres opérations analogues aux loteries (sport-toto, etc.; cf. art. 6 al. 2 LIA), a pour objet les lots en espèces effectivement payés dépassant le montant de 1'000 francs et provenant de loteries organisées en Suisse (art. 6 al. 1 LIA). […] Le terme "propriétaire" renvoie à la propriété au sens du droit civil (art. 641 CC […]).»
(Gleichlautende Umschreibung in BGer 2C_1030/2013 vom 28. Mai 2014, E. 2.1.)

**BGer 2A.108/2002 vom 11. Juli 2002, E. 2.1**
> «Unter den Begriff der Lotterie lassen sich zwangslos auch die lotterieähnlichen Veranstaltungen subsumieren, wie dies in Art. 47 Abs. 1 DBG im Zusammenhang mit der Sonderveranlagung bei Beendigung der Steuerpflicht oder bei Zwischenveranlagung geschehen ist […]. Ein solcher Wettbewerb ist auch das Sport-Toto. Dass die Teilnehmer an der Veranstaltung durch ihre besonderen Kenntnisse der an der Spielrunde beteiligten Mannschaften ihre Gewinnchancen erhöhen können, ändert nichts daran, dass der Ausgang des Wettbewerbs weitgehend vom Zufall abhängt und insofern lotterieähnlichen Charakter hat […].»

## 4. Fehltreffer und nicht einschlägige Treffer

| Fundstelle | Grund |
|---|---|
| BGer 2C_404/2015 vom 15. September 2016 | «Art. 6 VStG stehe dem nicht entgegen» steht nur im Parteivorbringen (Sachverhalt lit. F) der PVS zum Recht zur Nutzung an Aktienerträgen (Art. 25/26 VStG); in den Erwägungen wird Art. 6 nicht behandelt. Fehltreffer (vermutlich Fehlzitat der Partei). |
| BGE 139 I 280; BGer 2C_794/2012 | «Art. 6 LIP/GE» = Genfer loi sur l'instruction publique (Kopftuch an Schulen). |
| BGer 2C_320/2018, 2C_328/2018, 2C_342/2018; TI TCA 52.2017.107, 52.2016.591, 52.2016.592, 52.2016.632 | «art. 6 LIA» = Tessiner Legge sulle imprese artigianali. |
| BGE 125 II 348 | Art. 24 Abs. 5 VStG (Stockwerkeigentümergemeinschaft); Lotteriegewinne werden nur allgemein erwähnt. |
| BGer 2A.299/2004 | VSt 1990, Art. 147 DBG (Revision), kein Lotteriebezug. |
| BGE 138 II 536, E. 5.1 | Dividenden/Meldeverfahren; von CJ GE ATA/219/2013 für den Steuersatz auf Lotteriegewinnen zitiert, aber dort ohne Lotteriebezug. |
| BGer 2C_14/2014 (laut OCL vom 27. August 2014) | Ausländerrecht. In BGer 2C_89/2014, E. 6.3 wird «2C_14/2014 du 17 octobre 2014 consid. 3.4» zum Lotterie-Strohmannfall zitiert; offenbar ein Verschrieb für 2C_42/2014 vom 17.10.2014, E. 3.4 (nicht weiter verifiziert). |
| VGer ZG A 2022 9 vom 14.11.2022 | Art. 1 Abs. 1 VStG in geltender Fassung wiedergegeben (E. 2.1), Gegenstand aber geldwerte Leistungen und die Rechtskraft eines Rückerstattungsentscheids. |
| AG SVWG 3-BV.2019.1; BL SG 017/2008; BL SG 510 09 05, 510 10 53 | Art. 21 VStG bzw. Lotteriegewinne nur als allgemeines Zitat; der Sache nach Beteiligungserträge, Ausländer, Forderungsverzicht. Nur nach Snippet beurteilt. |
| ZH SRK VS.2025.3, ST.2023.152, DB.2011.95, ST.2009.53 | Art. 23 VStG (Verwirkung, KS 48), Lotteriegewinne nur in der allgemeinen Formel. Nur nach Abstract beurteilt. |
| TI TRAC 12.2024.90; TI CATI 80.2019.128, 80.2022.168; TI TRAP 60.2012.74; BGer 2A.342/2005 | Imposta preventiva allgemein (Regress, Rückerstattungsformalien); Lotterie nur in Art. 1 erwähnt. |
| BVGer (39 Treffer in CH_BVGE) | geldwerte Leistungen, Drittvergleich («Wettbewerb»); kein Bezug zu Geldspielgewinnen. |
| BGer 2C_729/2017, 2C_1086/2013, 2C_674/2009, 2C_336/2021, 2C_337/2021, 2C_91/2022, 2C_62/2025, 6B_928/2020, 6B_499/2024, 1C_163/2018 u.a. | Lotterie- und Geldspielaufsichtsrecht bzw. Strafrecht; keine Verrechnungssteuer. |

## 5. Offene Punkte

- Die Weiterzüge von VGer GR A 23 15, VRK SG I/2-2006/7, CDAP VD FI.2016.0148 und OGer AR O2V 16 9 sind nicht ermittelt; in OCL wurde kein BGer-Folgeentscheid gefunden.
- Die ZH-Steuerrekursentscheide VS.2015.7, VS.2016.2, VS.2018.18, VS.2021.1 und VS.2022.3 erscheinen nur in OCL; nach der Vorgabe (kantonal nur über Entscheidsuche) wurden sie nicht ausgewertet. Die ZH_SRK-Suche in Entscheidsuche ergab sie nicht.
- Zur geltenden Fassung (Grossspiele über Fr. 1 Mio., Online-Spielbanken, Jackpot, «einzelner Gewinn», Sportwetten) gibt es keine Rechtsprechung.
