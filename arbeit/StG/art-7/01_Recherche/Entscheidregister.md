# Art. 7 StG – Entstehung der Abgabeforderung (Emissionsabgabe): Entscheidregister

Arbeitsdatei, Stand der Recherche: 28.10.2026
Norm: Bundesgesetz über die Stempelabgaben vom 27. Juni 1973 (StG, SR 641.10), Art. 7, Fassung vom 1.1.2024 (Abs. 1 lit. a, abis, c, d, e, f; lit. b aufgehoben 1.4.1998; Abs. 2 aufgehoben 1.4.1993; lit. f bis 29.2.2012 Obligationen/Geldmarktpapiere, seit 1.1.2023 Kapitalband).
Werkzeuge: Open Case Law MCP, Entscheidsuche MCP. Keine Websuche, kein Lexplorer.

Klassen: **A** = legt Art. 7 aus oder entscheidet eine Sachfrage daraus; **B** = wendet Art. 7 an (Zeitpunkt trägt die Folgen im Fall: Fälligkeit, Zins, Rechtslage usw.); **C** = Erwähnung (Normtext in den Grundlagen, ohne Bedeutung für das Ergebnis).

Zitierstrings: BGer/BGE aus dem Cache (`zitat_de`) oder aus Open Case Law (`citation_string_de`); BVGer, SRK und Bundesrat mit Geschäftsnummer und Datum aus dem Dokument (Entscheidsuche-PDF bzw. VPB-Volltext).

---

## 1. Suchwege und Trefferzahlen

### 1.0 Ausgangsmaterial (Cache)

`data/zitate/StG/art-7.json`: 15 Einträge (Abfrage «"Art. 7" AND (LT OR LTB OR StG)», 474 Suchtreffer). Bereinigung:
- zusammengeführt: BGE 149 II 462 = 9C_610/2022; BGE 136 II 525 = 2C_17/2010; BGE 150 II 417 = 9C_475/2023;
- 7 Fehltreffer gestrichen (siehe Ziff. 4);
- übrig: 7 Geschäfte (BGE 115 Ib 233, 2A.618/1998, 2A.149/2006, 2C_115/2007, 2C_995/2011, 2C_621/2018, BGE 149 II 462/9C_610/2022).

### 1.1 Bundesgericht (Open Case Law, `search_decisions`, fields compact)

| Abfrage | Gericht | Treffer (gemeldet / ausgegeben) |
|---|---|---|
| `"Art. 7 StG" Emissionsabgabe` | bger | 49 / 49 |
| `"Art. 7 StG" Emissionsabgabe` | bge | 120 (Untergrenze) / 120 |
| `"art. 7 LT" droit de timbre` | bger | 804 (Untergrenze) / 200 |
| `"Abgabeforderung entsteht" Emissionsabgabe` | bger | 804 (Untergrenze) / 200 |
| `"Art. 7 Abs. 1" StG Emissionsabgabe` | bger | 243 (Untergrenze) / 100 |
| `"créance fiscale prend naissance" timbre d'émission` | bger | 434 (Untergrenze) / 100 |
| `"Art. 7 Abs. 1 lit. b StG"` (ältere Fassung) | alle | 0 |
| `Emissionsabgabe "Art. 7 Abs. 1"`, ab 1974 | bge | 43 / 43 |
| `"art. 7 LT" droit de timbre d'émission`, ab 1974 | bge | 265 (Untergrenze) / 60 |
| `find_leading_cases` law_code StG, article 7 | alle | 27 (davon 9 BGer/BGE, 13 BVGer, 3 BE-VGer, 2 kantonal-irrelevante BGE) |

Die Volltextsuche arbeitet unscharf (ODER-Rangierung). Deshalb wurden **371 BGer/BGE-Kandidaten** (alle Treffer der Abfragen mit Steuerbezug, 2A/2C/2P/9C sowie BGE ab 1974) im Volltext maschinell auf Verweise «Art. 7 … StG/LT» geprüft (Volltexte der Open-Case-Law-Entscheidseiten, `canonical_url`) und jeder Treffer im Kontext gelesen.
Ergebnis: **9 Dokumente = 8 Geschäfte** wenden Art. 7 StG (Bund) an: die 7 aus dem Cache und neu **BGer 2C_299/2021**. Keine BGE vor 1974 mit Bezug auf das StG 1973.

### 1.2 Bundesverwaltungsgericht (Entscheidsuche, hierarchy `CH_BVGE`)

| Abfrage | Treffer |
|---|---|
| `"Art. 7 StG" Emissionsabgabe` | 0 (Phrasensuche greift wegen «Art . 7» in PDF-Texten nicht) |
| `"Abgabeforderung entsteht" Emissionsabgabe` | 8 |
| `"Art. 7 Abs. 1" StG Emissionsabgabe` | 21 |
| `Emissionsabgabe "Art. 7 Abs. 1 Bst."` | 12 |
| `"art. 7 al. 1" LT droit de timbre` | 22 |
| `Emissionsabgabe ("Zeitpunkt des Zuschusses" OR Handwechsel OR "Mantelhandel") StG` | 11 |
| `"Art. 7 StG" OR "Art. 7 Abs. 1 StG" OR "art. 7 LT"` | 0 |

Alle Stempelabgaben-Treffer und die vorgegebenen Kandidaten (A-1592/2006, A-1552/2006, A-577/2013, A-6592/2013, A-267/2015, A-3554/2017, A-3735/2017, A-6828/2017, A-1121/2020, A-5128/2024) wurden als PDF (`document_url` der Entscheidsuche) geladen und im Volltext geprüft: **21 Dokumente**, zusätzlich zur Kontrolle 16 weitere Stempelabgaben-Urteile (A-801/2007, A-1615/2006, A-1380/2006, A-1567/2006, A-659/2007, A-6020/2007, A-1521/2006, A-6854/2008, A-4091/2016, A-364/2013, A-4164/2020, A-2595/2020, A-1446/2021, A-8711/2025, A-3032/2021, A-1449/2015): dort kein Verweis auf Art. 7 StG.
Ergebnis: **15 BVGer-Urteile** mit Art. 7 StG.
(Eine Open-Case-Law-Abfrage court bvger, 51 Treffer, diente nur zum Abgleich der Kandidaten, nicht als Quelle.)

### 1.3 Eidg. Steuerrekurskommission und Bundesrat (VPB; Open Case Law court `ch_vb`)

| Abfrage | Treffer (gemeldet / ausgegeben) |
|---|---|
| `"Art. 7 StG" Emissionsabgabe` | 150 (Untergrenze) / 100 |
| `Emissionsabgabe "Abgabeforderung entsteht" Zeitpunkt` | 240 (Untergrenze) / 60 |
| `droit d'émission "art. 7 al. 1" LT` | 243 (Untergrenze) / 60 |

140 VPB-Kandidaten im Volltext geprüft. Ergebnis: **5 Entscheide** (SRK: VPB 61.64, 69.60, 69.125; Bundesrat: VPB 59.60, 64.78). VPB 64.78 fiel erst bei der Gegenprobe in der Entscheidsuche auf (Aufzählung «Art. 5 Abs. 1 Bst. a, Art. 7 Abs. 1 Bst. a und Art. 8 StG») und wurde danach im Volltext bestätigt.

### 1.4 Kantonale Gerichte (Entscheidsuche, Kontrollsuche)

| Abfrage | Treffer |
|---|---|
| `Emissionsabgabe "Art. 7" StG Abgabeforderung` (ohne Hierarchiefilter) | 24, alle Bund (CH: BVGer 13, BGer 5, BGE 2, VPB 4), **kantonal 0** |
| `"Art. 7 StG" Emissionsabgabe NOT hierarchy:CH` | 0 |
| `list_hierarchy` «Emissionsabgabe Abgabeforderung» | nur Bundesebene (CH_BVGE, CH_BGer, CH_BGE, CH_VB, CH_BSTG) |

Ergebnis: **kein kantonaler Entscheid** zu Art. 7 StG (Bund). Die drei BE-Urteile aus `find_leading_cases` betreffen Art. 7 StG/BE (Ziff. 4).

### 1.5 Summe

28 Entscheide: BGer/BGE 8 (A 4, B 3, C 1) · BVGer 15 (A 2, B 7, C 6) · SRK 3 (A 1, B 1, C 1) · Bundesrat 2 (A 1, C 1) · kantonal 0.

---

## 2. Register

Reihenfolge: Gericht, dann Datum. «E.» = einschlägige Erwägung.

| Entscheid (Zitierstring) | Datum | Gericht | Normstelle | Sachfrage | Kernaussage (ein Satz) | E. | Ergebnis (Weiterzug? bestätigt durch …) | Klasse | Fassung/Steuerperiode |
|---|---|---|---|---|---|---|---|---|---|
| BGE 115 Ib 233 | 18.10.1989 | BGer | Abs. 1 lit. a | HR-Eintrag bei öffentlich-rechtlicher AG | Die Anknüpfung an den HR-Eintrag schliesst die Abgabe bei Kantonalbank-AG nicht aus, weil auch kaufmännisch tätige öffentlich-rechtliche Unternehmen eintragungspflichtig sind; ob die Abgabe ohne Eintragungspflicht entfiele, bleibt offen. | 3 | Beschwerde abgewiesen; letztinstanzlich | A | StG 1973 (Erstfassung); Emissionen der Zuger Kantonalbank vor 1989 |
| BGer 2A.618/1998 vom 7. Februar 2000 | 07.02.2000 | BGer | Abs. 1 lit. a; Art. 7 allgemein | Entstehung vs. steuerbarer Vorgang; Wegfall einer Steuerbefreiung | Das StG trennt zeitlich nicht zwischen steuerbarem Vorgang und Entstehung der Forderung; eine «logische Sekunde» zwischen Gründung und deklaratorischem Registereintrag ist unerheblich. | 2a, 3c/bb | Vorinstanz SRK; Abgabepflicht bejaht (E. 3); Dispositiv im verfügbaren Volltext nicht enthalten | A | Art. 7 Abs. 1 lit. a i.d.F. vom 4.10.1991; Umwandlung Liechtensteinische Landesbank, Eintrag 4.1.1993 |
| BGer 2A.149/2006 vom 28. Juni 2006 | 28.06.2006 | BGer | Abs. 1 lit. e (i.V.m. Art. 11 lit. c, Art. 30) | Fälligkeit, Verjährung, Verrechnung; Wirkung der Verfügung | Die Forderung entsteht mit dem Zuschuss, wird 30 Tage später fällig und verjährt ab Entstehungsjahr; die Verfügung wirkt bloss deklaratorisch, die Bestreitung verschiebt die Fälligkeit nicht. | 2.1, 2.2 | Vorinstanz SRK; Beschwerde abgewiesen | A | Zuschuss/Aktienverkauf vor 1998; Verrechnung 1998 |
| BGer 2C_115/2007 vom 11. Februar 2008 | 11.02.2008 | BGer | Abs. 1 lit. e (im Urteil: «art. 7 al. 1 let. d LT») | Dividendenverzicht als Zuschuss | Der Verzicht auf eine fällige Dividende ist ein Zuschuss; die Forderung entsteht mit dem Verzicht (GV-Beschluss 11.12.2002). | 7.1–7.3 | bestätigt BVGer A-1360/2006; Beschwerde abgewiesen | B | Verzicht 11.12.2002 |
| BGer 2C_995/2011 vom 16. August 2012 | 16.08.2012 | BGer | Abs. 1 lit. f (alt) | Obligationen; massgebende Fassung | Anwendbar ist das StG in der im Zeitpunkt der Emission geltenden Fassung; die Forderung entsteht mit der Ausgabe der Obligationen. | 2, 3 | bestätigt BVGer A-4930/2010; Beschwerde abgewiesen | B | Anleihe vom 28.10.2009; aArt. 5a, 9a StG |
| BGer 2C_621/2018 vom 10. August 2018 | 10.08.2018 | BGer | Abs. 1 lit. e (i.V.m. Art. 11 lit. c) | Zeitpunkt des Zuschusses bei rückwirkendem Forderungsverzicht; Verzugszins | Vereinbaren die Parteien einen Forderungsverzicht rückwirkend, gilt der Zuschuss als im Rückwirkungszeitpunkt erbracht; ab dann läuft die 30-Tage-Frist. | 2.3, 3.2.3–3.2.5 | bestätigt BVGer A-3735/2017; Beschwerde abgewiesen, soweit eingetreten | A | Zuschuss per 1.1.2010 (Vereinbarung vom 22.9.2010) |
| BGer 2C_299/2021 vom 17. Dezember 2021 | 17.12.2021 | BGer | Abs. 1 lit. f (alt), Art. 53 Abs. 2 | Intertemporales Recht (Obligationen) | Für vor dem 1.3.2012 entstandene Abgabeforderungen gilt das bis Ende Februar 2012 geltende Recht; die Forderung entstand mit der Ausgabe der Obligationen. | 3.3, 4.1 | bestätigt BVGer A-4543/2019 | B | Anleihe, Ausgabe/Erhöhungen 2011 |
| BGE 149 II 462 (= BGer 9C_610/2022 vom 7. September 2023) | 07.09.2023 | BGer | Abs. 1 lit. e | Freibetrag Art. 6 Abs. 1 lit. k / Erlass | Normtext nur als Grundlage; zeitliches Element des Freibetrags knüpft an die Verbuchung der Sanierungsmassnahme an (Regeste), nicht an Art. 7. | 2.3.2 | hebt BVGer A-5073/2020 auf (Gutheissung der ESTV-Beschwerde) | C | Sanierung 2015 |
| BVGer A-1360/2006 vom 1. März 2007 | 01.03.2007 | BVGer (Cour I) | Abs. 1 lit. e | Dividendenverzicht als Zuschuss; Fälligkeit | Die Forderung entsteht im Zeitpunkt des Zuschusses; der Verzicht der Aktionäre vom 11.12.2002 ist der Zuschuss. | 7.1, 7.2 | Weiterzug: BGer 2C_115/2007, abgewiesen | B | 2002; Fälligkeit im Urteil nach «art. 11 let. b LT» (Quartal) angegeben |
| BVGer A-1592/2006 vom 15. April 2009 | 15.04.2009 | BVGer | Abs. 1 lit. e | Zuschussbegriff | Normtext in den Grundlagen. | 3.2 | kein Weiterzugsvermerk im Dokument | C | – |
| BVGer A-1552/2006 vom 22. Juni 2009 | 22.06.2009 | BVGer | Abs. 1 lit. a, abis | Quasifusion, Vorratsaktien | Normtext (lit. a und abis) in den Grundlagen. | 3 | kein Weiterzugsvermerk im Dokument | C | – |
| BVGer A-4930/2010 vom 21. Oktober 2011 | 21.10.2011 | BVGer | Abs. 1 lit. f (alt) | Obligationen; Erneuerung | Forderung entsteht mit der Ausgabe; Grundlage für die Bemessung nach Laufzeit. | 3.1 | Weiterzug: BGer 2C_995/2011, abgewiesen | B | Anleihe vom 28.10.2009 |
| BVGer A-4188/2009 vom 1. September 2011 | 01.09.2011 | BVGer (Cour I) | Abs. 1 lit. e | Forderungsverzicht/Einlagen bei Liquidation | Normtext in den Grundlagen. | 3.1 | kein Weiterzugsvermerk im Dokument | C | – |
| BVGer A-577/2013 vom 20. November 2013 | 20.11.2013 | BVGer | Abs. 1 lit. e | Teilerlass Art. 12 | Normtext in den Grundlagen. | 2.2 | kein Weiterzugsvermerk im Dokument | C | Sanierung nach 1.1.2009 (Art. 6 Abs. 1 lit. k) |
| BVGer A-6592/2013 vom 18. September 2014 | 18.09.2014 | BVGer | Abs. 1 lit. e | Zuschuss durch Verkauf unter Verkehrswert; Quasifusion | Normtext; Bewertung im Zeitpunkt der Einbringung (Art. 8 Abs. 3). | 3.2 | kein Weiterzugsvermerk im Dokument | C | – |
| BVGer A-267/2015 vom 13. Juli 2015 | 13.07.2015 | BVGer | Abs. 1 lit. e (i.V.m. Art. 8 Abs. 3) | Zeitpunkt des Zuschusses = Leistung; Stichtag der Bewertung | Massgebend ist der Zeitpunkt, in welchem der Zuschuss geleistet wird; spätere Korrekturen der Jahresrechnung (ex post) bleiben ausser Betracht. | 2.3, 3.2.1.1 | Beschwerde abgewiesen; kein Weiterzugsvermerk im Dokument | A | Übertragung am 21.12.2011 |
| BVGer A-3554/2017 vom 19. April 2018 | 19.04.2018 | BVGer | Abs. 1 lit. e | Quasifusion; Zuschuss | Übernimmt die Formel aus A-267/2015 (Zeitpunkt der Leistung), Fälligkeit und Verzugszins. | 2.3 | bestätigt durch BGer 2C_447/2018 (Vermerk im Dokument) | B | 2012 |
| BVGer A-3735/2017 vom 12. Juni 2018 | 12.06.2018 | BVGer | Abs. 1 lit. e | Verfügungs- vs. Verpflichtungsgeschäft; Rückwirkung; Erlasszeitpunkt; Verzugszins | Massgebend ist das Verfügungsgeschäft; der «per 1.1.2010» erklärte Verzicht gilt auf diesen Tag, nicht auf den Vereinbarungstag (22.9.2010). | 2.3.1, 2.4, 4.1, 6.1.1 | bestätigt durch BGer 2C_621/2018 | A | Zuschuss per 1.1.2010 |
| BVGer A-6828/2017 vom 29. Oktober 2018 | 29.10.2018 | BVGer | Abs. 1 lit. a, abis | HR-Eintrag vs. Ausgabe bei bedingter Kapitalerhöhung | Lit. abis ist Ausnahme von lit. a, weil bei der bedingten Kapitalerhöhung die Rechte schon mit der Liberierung entstehen und der HR-Eintrag nachhinkt. | 2.3 | teilweise bestätigt durch BGer 2C_1071/2018 | B | GV-Beschluss 7.5.2015; Art. 11 lit. b i.d.F. ab 1.3.2012 |
| BVGer A-4543/2019 vom 1. März 2021 | 01.03.2021 | BVGer | Abs. 1 lit. f (alt), Art. 53 Abs. 2 | Intertemporales Recht (Obligationen) | Auf vor dem 1.3.2012 entstandene Forderungen ist altes Recht anwendbar; Entstehung mit Ausgabe/Erhöhung 2011. | 3.1, 3.2.2 | bestätigt durch BGer 2C_299/2021 | B | 2011 |
| BVGer A-1121/2020 vom 30. Juni 2021 | 30.06.2021 | BVGer | Abs. 1 lit. a, abis | Quasifusion | Normtext mit Verweis auf A-6828/2017. | 2.4 | kein Weiterzugsvermerk im Dokument | C | Kapitalerhöhung, HR 15.7.2014 |
| BVGer A-5073/2020 vom 29. November 2021 | 29.11.2021 | BVGer | Abs. 1 lit. e | Erlass/Freibetrag: massgebender Zeitpunkt; Verzugszins | Für den Erlass ist auf die Entstehung der Forderung abzustellen (Zugang der Mittel; Massnahmen verbindlich beschlossen). | 2.5.1, 2.6.1 | aufgehoben durch BGer 9C_610/2022 (= BGE 149 II 462) | B | 2015 |
| BVGer A-5105/2022 vom 23. September 2025 | 23.09.2025 | BVGer (Cour I) | Abs. 1 lit. e | Erlass Art. 12: massgebender Zeitpunkt | Entscheidend für den Erlass ist der Zeitpunkt der Entstehung der Forderung, d.h. der Zugang der Mittel. | 3.1.3, 3.2.4 | kein Weiterzugsvermerk im Dokument | B | – |
| VPB 59.60 (Entscheid des Bundesrates vom 13. Juni 1994) | 13.06.1994 | Bundesrat | Abs. 1 lit. a; Art. 53 Abs. 2 | Intertemporales Recht (Revision 4.10.1991); Erlasszeitpunkt | Massgebend ist das Recht im Zeitpunkt des HR-Eintrags (28.11.1991); die per 1.4.1993 eingeführte Ausnahme wirkt nicht zurück. | 2, 3, 4.4 | Erlass verneint (Regeste) | A | Gründung, HR 28.11.1991 (3 %-Satz) |
| VPB 61.64 (Décision de la Commission fédérale de recours en matière de contributions du 28 avril 1995, confirmée par le Tribunal fédéral le 3 octobre 1996) | 28.04.1995 | SRK | Abs. 1 lit. a | Deklaratorischer HR-Eintrag; Beginn des Verzugszinses | Art. 7 Abs. 1 lit. a unterscheidet nicht zwischen deklaratorischem und konstitutivem Eintrag; der Verzugszins lief (nach damaligem Art. 29) erst ab Mahnung. | 2, 6a | bestätigt durch BGer am 3.10.1996 (Vermerk im VPB-Titel) | A | Umwandlung einer Bank in öffentlich-rechtliche AG; Verfügung 18.3.1994 |
| VPB 64.78 (Entscheid des Bundesrates vom 20. Dezember 1999) | 20.12.1999 | Bundesrat | Abs. 1 lit. a | Erlass (Auffanggesellschaft) | Normtext: Kapitalerhöhung liess die Forderung entstehen (unbestritten). | 2 | Erlass verneint (Regeste) | C | Kapitalerhöhung 1996 (Satz 2 %) |
| VPB 69.60 (Entscheid der Eidgenössischen Steuerrekurskommission vom 6. Januar 2005 [SRK 2003-185]) | 06.01.2005 | SRK | Abs. 1 lit. a (i.V.m. Art. 11, 29) | Formwechselnde Umwandlung; Verzugszins | HR-Eintrag am 15.5.2002, daher Verzugszins ab 15.6.2002 ohne Mahnung. | 2b, 4 | Beschwerde abgewiesen (E. 5) | B | HR 15.5.2002 |
| VPB 69.125 (Entscheid SRK 2004-068 der Eidgenössischen Steuerrekurskommission vom 28. Juni 2005) | 28.06.2005 | SRK | Abs. 1 lit. e | Zuschuss durch nahestehende Dritte | Normtext in den Grundlagen. | 2b | – | C | Transaktionen nach 1.4.1998 |

Hinweise zur Tabelle:
- **2C_115/2007** zitiert für Zuschüsse und Handwechsel «art. 7 al. 1 let. d LT». Nach dem Entwurf 1972 und der geltenden Zählung steht die Regel in lit. e (siehe `Materialien.md`, Entwurf lit. e). Wahrscheinlich ein Versehen im Urteil; zitieren als «Art. 7 Abs. 1 lit. e StG».
- **A-1360/2006** gibt für den Zuschuss die Fälligkeit «trente jours après l'expiration du trimestre» nach «art. 11 let. b LT» an. Die übrigen Entscheide nennen für Zuschüsse Art. 11 lit. c StG (30 Tage nach Entstehung). Vor Verwendung am Gesetzestext der damaligen Fassung prüfen.
- Der Weiterzug ist nur dort angegeben, wo das Dokument einen Vermerk trägt oder das BGer-Urteil den Fall erkennbar betrifft (gleicher Sachverhalt).

---

## 3. Tragende Stellen der A-Entscheide (wörtlich)

**BGE 115 Ib 233 E. 3**
> «Es trifft zu, dass das Gesetz (Art. 7 Abs. 1 lit. a StG) die Entstehung der Abgabeforderung bei Aktien an den Eintrag im Handelsregister anknüpft. Eine Eintragungspflicht besteht aber nach der Praxis auch für öffentlichrechtliche Unternehmungen, die eine nach kaufmännischer Art betriebene Tätigkeit ausüben. […] Fragen könnte sich höchstens, ob auf Grund von Art. 7 Abs. 1 lit. a StG eine Abgabenpflicht von gemischtwirtschaftlichen Unternehmungen nicht generell, sondern nur im Falle ihrer Eintragspflicht bestehe. Doch kann die Frage offenbleiben, weil die Beschwerdeführerin eine nach kaufmännischer Art betriebene Unternehmung darstellt und als solche jedenfalls zur Eintragung verpflichtet ist.»

**BGer 2A.618/1998 vom 7. Februar 2000 E. 2a**
> «Bei Emissionsabgaben, welche für die Ausgabe von Aktien und Partizipationsscheinen geschuldet sind, entsteht die Forderung des Fiskus im Zeitpunkt, in dem die Begründung oder Erhöhung der Beteiligungsrechte im Handelsregister eingetragen wird (Art. 7 Abs. 1 lit. a StG [Fassung vom 4. Oktober 1991]).»

**BGer 2A.618/1998 vom 7. Februar 2000 E. 3c/bb**
> «Letzteres differenziert, wie die Vorinstanz zu Recht festgestellt hat, in zeitlicher Hinsicht nicht zwischen dem steuerbaren Vorgang, hier der Begründung von Aktionärsrechten, und der Entstehung der Abgabeforderung. Es beschränkt sich darauf, abhängig vom jeweiligen Steuerobjekt, zu bestimmen, wann der Anspruch des Staates auf die Emissionsabgabe entsteht (vgl. Art. 7 StG). Deshalb ist auch nicht entscheidend, ob die Gründung der Aktiengesellschaft (durch Gesetz) allenfalls vom (deklaratorischen) Eintrag im Öffentlichkeitsregister durch eine logische Sekunde getrennt ist.»

**BGer 2A.149/2006 vom 28. Juni 2006 E. 2.1**
> «Die Abgabeforderung entsteht im Zeitpunkt des Zuschusses (Art. 7 Abs. 1 lit. e StG). Sie wird 30 Tage nach ihrer Entstehung fällig (Art. 11 lit. c StG). Sie verjährt fünf Jahre nach Ablauf des Kalenderjahres, in dem sie entstanden ist (Art. 30 Abs. 1 StG).»

**BGer 2A.149/2006 vom 28. Juni 2006 E. 2.2**
> «Der Entscheid der Behörde, in welchem die Abgabeforderung eröffnet bzw. förmlich festgelegt wird, hat also keine konstitutive, sondern bloss deklaratorische Wirkung. An der Fälligkeit - hier 30 Tage nach dem Zuschuss bzw. dem Verkauf der Aktien - ändert sich nichts, wenn die Forderung bestritten ist, in Übereinstimmung mit dem in Art. 120 Abs. 2 OR festgelegten (und auch hier analog gültigen) Grundsatz.»

**BGer 2C_621/2018 vom 10. August 2018 E. 3.2.4**
> «Diese Auffassung überzeugt nicht. Sie übergeht nämlich, dass es sehr wohl denkbar ist, ein bestehendes Rechtsgeschäft rückwirkend abzuändern oder aufzuheben.»

**BGer 2C_621/2018 vom 10. August 2018 E. 3.2.5**
> «Insoweit kommt der Erklärung der Parteien nicht bloss illustrative Bedeutung zu. Vielmehr handelt es sich um ein konstitutives Vertragselement, das abgaberechtlich nicht unbeachtet bleiben darf. Entfiel die Verpflichtung in der Hauptsache (und damit auch die etwaige Zins- und Amortisationspflicht) rückwirkend am 1. Januar 2010, so erfolgte der Zuschuss im selben Zeitpunkt, entstand das emissionsabgaberechtliche Verhältnis gleichzeitig und trat die Fälligkeit 30 Tage später ein, mithin am 31. Januar 2010 (vorne E. 2.3).»

**BVGer A-267/2015 vom 13. Juli 2015 E. 2.3**
> «Bei Zuschüssen entsteht die Emissionsabgabeforderung im Zeitpunkt des Zuschusses (Art. 7 Abs. 1 Bst. e StG) und beträgt 1% des Betrags des Zuschusses (Art. 8 Abs. 1 Bst. b StG). Massgebend ist dabei grundsätzlich der Zeitpunkt, in welchem der Zuschuss geleistet wird (DUSS/VON AH/SIEBER, Kommentar Steuerrecht II/3, N 46 zu Art. 7).»

**BVGer A-267/2015 vom 13. Juli 2015 E. 3.2.1.1**
> «Gemäss der gesetzlichen Regelung folgt die Bewertung der eingebrachten Vermögensgegenstände nämlich einer Stichtagsbetrachtung: Massgebend ist der Zeitpunkt der Einbringung, vorliegend also der Übertragung des fraglichen Stammanteils am 21. Dezember 2011.»

**BVGer A-3735/2017 vom 12. Juni 2018 E. 2.3.1**
> «Bei (abgabepflichtigen) Zuschüssen entsteht die Emissionsabgabeforderung im Zeitpunkt des Zuschusses (Art. 7 Abs. 1 Bst. e StG). Massgebend ist dabei grundsätzlich der Zeitpunkt, in welchem der Zuschuss geleistet wird (Urteil des BVGer A-267/2015 vom 13. Juli 2015 E. 2.3), also der Zeitpunkt des Verfügungsgeschäftes (BEAT KÖNIG, in: Kommentar Steuerrecht II/3, Art. 7 N. 46).»

**BVGer A-3735/2017 vom 12. Juni 2018 E. 4.1**
> «Vorliegend ist dies der Zeitpunkt, per welchen der Zuschuss von Fr. 34'800'000.- geleistet wurde (Zeitpunkt des Verfügungsgeschäftes, vgl. vorn E. 2.3.1). Da die beiden Aktionärinnen der Beschwerdeführerin mit der Vereinbarung vom 22. September 2010 «per 1.1.2010» auf ihre Darlehensforderungen verzichteten (vgl. Akten Vorinstanz, act. 18 Blatt 5), ist letzterer Zeitpunkt massgebend. Entgegen der Darstellung in der Beschwerde kann keine Rede davon sein, dass der fragliche Zuschuss emissionsabgaberechtlich gesehen erst am 22. September 2010 geleistet wurde. Dieser Zeitpunkt ist nämlich der im vorliegenden Kontext nicht ausschlaggebende Zeitpunkt des Verpflichtungsgeschäftes.»

**VPB 59.60 (Entscheid des Bundesrates vom 13. Juni 1994) E. 3**
> «Nach der Übergangsbestimmung von Art. 53 Abs. 2 StG - die nicht geändert wurde und auch für die Revision vom 4. Oktober 1991 gilt - bleiben die auf den 1. April 1993 ausser Kraft gesetzten Bestimmungen in bezug auf Abgabeforderungen, die vor dem Inkrafttreten der neuen Bestimmungen entstanden sind, auch nach diesem Zeitpunkt anwendbar.»

**VPB 59.60 E. 4.4**
> «Massgeblicher Zeitpunkt für die Beurteilung der Frage, ob eine Sanierung vorliegt, ist allein der Zeitpunkt der Ausgabe der Aktien, welche die Abgabeforderung begründet.»

**VPB 61.64 (SRK vom 28. April 1995) consid. 2**
> «L’autorité intimée relève au surplus à juste titre que l’art. 7 al. 1 let. a LT ne distingue pas entre inscription déclarative et constitutive.»

**VPB 61.64 consid. 6a**
> «Conformément à l’art. 7 al. 1 let. a LT, la créance fiscale prend naissance, s’agissant des actions, lors de l’inscription au registre du commerce de la création ou de l’augmentation des droits de participation. Elle ne devient cependant exigible que trente jours après la naissance (art. 11 let. c LT) […]. Ce dernier ne commence cependant à courir qu’à la suite d’une sommation officielle, laquelle est comparable à une interpellation au sens technique.»

(Textquellen: BGer/BGE aus dem Cache `data/entscheide/*.json` bzw. den Open-Case-Law-Volltexten; BVGer aus den Entscheidsuche-PDF; VPB aus den Open-Case-Law-Volltexten. Die PDF-Texte sind maschinell extrahiert; Silbentrennungen wurden zusammengezogen.)

---

## 4. Gestrichene Fehltreffer und geprüfte, nicht aufgenommene Entscheide

| Entscheid | Grund |
|---|---|
| BGE 94 I 305 | «Art. 7 StG» ist das kantonale Steuergesetz (St. Gallen, Wohnsitzregel); Gewohnheitsrecht im kantonalen Steuerrecht |
| BGE 136 II 525 = BGer 2C_17/2010 | Art. 7 StG/Davos (kommunale Erbschaftssteuer) |
| BGer 2C_1011/2012 | Art. 7 StG/SH (Steuerausscheidung, Auslandsverluste) |
| BGer 2C_864/2021 | Art. 7 StG/BE (interkantonale Ausscheidung) |
| BGE 150 II 417 = BGer 9C_475/2023 | Art. 7 StG/SH und Art. 7 DBG (ausländische Ferienwohnung) |
| BE-VGer 100 2022 301, 100 2020 266, 100 2025 102 (aus `find_leading_cases`) | Kantons- und Gemeindesteuern Bern (StG/BE) |
| BGE 140 II 16; BGer 2C_168/2011; 2C_460/2013 | «Abgabeforderung entsteht» betrifft Art. 23 StG (Versicherungsprämien), nicht Art. 7 |
| BGer 2C_1071/2018; 2C_447/2018; 2C_976/2014; 2C_1001/2014 | Emissionsabgabe (Quasifusion), aber ohne Verweis auf Art. 7 StG |
| BVGer A-7094/2008; A-5128/2024 | Mantelhandel; Zeitpunkt des Handwechsels nur über Art. 8 Abs. 1 lit. c StG (Bemessung), kein Verweis auf Art. 7 |
| BVGer A-7065/2013; A-5377/2023; A-4733/2022 | Treffer nur wegen Art. 7 VGKE bzw. Art. 7 KAG |
| zahlreiche französische BGer-Urteile (z.B. 2C_499/2011, 2C_1154/2015, 2C_382/2017) | «créance fiscale prend naissance» betrifft Art. 12 VStG/LIA |

---

## 5. Nachtrag (Fundstellenprüfung, 28.10.2026)

| Entscheid (Zitierstring) | Datum | Gericht | Normstelle | Sachfrage | Kernaussage (ein Satz) | E. | Ergebnis | Klasse | Fassung/Steuerperiode |
|---|---|---|---|---|---|---|---|---|---|
| BGer 9C_232/2026 vom 10. September 2026 | 10.09.2026 | BGer | (Art. 8 Abs. 1 lit. c, Art. 5 Abs. 2 lit. b; Art. 7 nicht zitiert) | Mantelhandel, Bemessung im Zeitpunkt des Handwechsels | Reinvermögen «im Zeitpunkt des Handwechsels» ist Bemessungsgrundlage; Zeitpunkt nach Art. 7 nicht ausgelegt. | 4.1 | bestätigt BVGer A-5128/2024 (publiziert 21.10.2026) | C (nur als Beleg zur Bemessung verwendet) | Handwechsel 2020er Jahre |
