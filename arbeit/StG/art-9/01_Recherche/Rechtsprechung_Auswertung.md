# Art. 9 StG – Auswertung der Rechtsprechung (Register-Grundlage)

Stand der Recherche: 28.10.2026. Quellen: die Cache-Dateien in `data/entscheide/` (Feld `text`, Zitierstring aus `zitat_de`), Open Case Law (`cite`, `search_decisions`, `get_decision`, `get_erwaegung`, `find_appeal_chain`) und Entscheidsuche (POST `_search.php`, Volltext in `_source.attachment.content`). Lexplorer und Websuche habe ich nicht benutzt. Die Volltexte habe ich nur an den einschlägigen Erwägungen gelesen.

Die Zitierstrings der BGer- und BVGer-Entscheide stammen aus `citation_string_de` (Open Case Law) oder aus `zitat_de` (Cache). VPB-Entscheide haben keinen Open-Case-Law-Zitierstring; ich zitiere sie im Format von `kommentare/StG/art-8.md`. Die Zitate sind wörtlich übernommen. Trennstriche aus Zeilenumbrüchen der PDF-Fassungen (z.B. «ristruttur- azioni») habe ich zusammengezogen; OCR-Fehler der Quelle sind mit [sic] markiert.

**Klassen:**
- **A** = Art. 9 StG trägt das Ergebnis.
- **B** = Art. 9 StG wird angewendet oder ausgelegt, ist aber nicht der Hauptpunkt (oder die Rechtsprechung dazu wird auf eine andere Norm übertragen).
- **C** = Art. 9 StG wird nur erwähnt.

**Fassungen von Art. 9 StG:**
- F1973 = Fassung vom 27.6.1973 (AS 1974 11): Abs. 1 lit. a ermässigter Satz (1 % statt 2 %, ab 1.4.1978 1 % statt 3 %) für Fusionen, fusionsähnliche Zusammenschlüsse, Umwandlungen und Aufspaltungen von AG/KAG/GmbH/Genossenschaften. In Kraft bis 31.3.1993.
- F2004 = Abs. 1 lit. e, eingefügt durch Anhang Ziff. 6 FusG, in Kraft seit 1.7.2004.
- geltend = Fassung seit 1.1.2023/1.1.2024 (lit. a–c aufgehoben; lit. d, lit. e, Abs. 2, Abs. 3 Kapitalband).

---

## (i) Suchprotokoll

### 1. Vorgegebene Entscheide

| Schritt | Werkzeug / Abfrage | Ergebnis |
|---|---|---|
| BGE 102 Ib 140, BGE 115 Ib 125, BGer 2A.618/1998, BGer 2C_976/2014, BGer 2C_1001/2014 | Cache-Dateien `ocl_bge_102_IB_140.json`, `ocl_bge_115_IB_125.json`, `ocl_bger_2A.618_1998.json`, `ocl_bger_2C_976_2014.json`, `ocl_bger_2C_1001_2014.json`, Feld `text` | gelesen an E. 1–7 / 1–3 / 2–5 / 3.1–3.2 / 3.1–3.2 |
| BGer 2A.83/2001, 2A.84/2001 | OCL `cite` → beide vorhanden; Volltext über Entscheidsuche (`CH_BGer_002_2A-83-2001_2002-03-05`, `CH_BGer_002_2A-84-2001_2002-03-05`); Textvergleich mit difflib | Übereinstimmung 96,3 %, Unterschiede nur im Sachverhalt und in E. 4.3 |
| BVGer A-3761/2021 | OCL `search_decisions` «A-3761/2021» → 11 Treffer (nur 1 einschlägig: `bvger_A-3761_2021`); Volltext über Entscheidsuche `CH_BVGE_001_A-3761-2021_2024-10-15`; OCL `get_erwaegung` E. 8 und E. 10 | Kopfzeile: «Decisione impugnata davanti al TF» |
| Weiterzug A-3761/2021 | OCL `find_appeal_chain` → keine Instanzen; OCL `search_decisions` court=bger «"A-3761/2021"» → 0; «"9 cpv. 1 lett. e LTB"» → 0; «"lett. abis LTB"» → 0; «"tassa di bollo d'emissione" ristrutturazione "ditta individuale"» ab 1.11.2024 → 176 (nach Relevanz, ohne Stempelabgabefall); «tassa bollo emissione» ab 1.1.2025 → 261 (dto.); «"tasse di bollo" ristrutturazione "società di persone"» → 68 (nur ältere Fälle bis 2021); Entscheidsuche CH_BGer: «"A-3761/2021"» → 0; «"9 cpv. 1 lett. e"» → 0; «"tassa di bollo" AND "9 cpv. 1"» → 0; «"versamenti suppletivi" AND "tassa di bollo" AND ristrutturazione» → 0; «bollo AND emissione» → 5 (alle bis 2021); «LTB AND bollo» → 6 (alle bis 2021) | kein BGer-Urteil auffindbar (siehe unten) |
| BGer 9C_653/2024 | OCL `cite` → BGer 9C_653/2024 vom 3. April 2025; Volltext Entscheidsuche | AHV-Beitragssache (Cassa cantonale di compensazione TI), kein Bezug |
| Zitierungen von A-3761/2021 | Entscheidsuche «"A-3761/2021"» in CH_BGer, CH_BVGE → 4 Treffer: A-3761/2021 selbst, A-5377/2023 (2.7.2025), A-4789/2021 (23.10.2025), A-556/2024 (26.11.2024) | A-5377/2023 zitiert «A-3761/2021 vom 15. Oktober 2024 [angefochten]» |
| 9C_232/2026, 9C_209/2025 (wiederholt in den Trefferlisten) | OCL `get_decision` (Metadaten) | 9C_232/2026 = Emissionsabgabe/Mantelhandel (Vorinstanz A-5128/2024); 9C_209/2025 = Einkommenssteuer TI. Keines betrifft A-3761/2021 |
| BVGer A-1552/2006, A-6592/2013, A-6142/2012 | Entscheidsuche (`CH_BVGE_001_…`) | gelesen an E. 4.4.1–4.4.3 / 3.3.2.2 / 7.4–7.8 |
| Weiterzug A-6592/2013 | Cache 2C_976/2014: Vorinstanz «Urteil des Bundesverwaltungsgerichts, Abteilung I, vom 18. September 2014» | bestätigt durch BGer 2C_976/2014 |
| Weiterzug A-6142/2012, A-1552/2006 | OCL `find_appeal_chain` A-6142/2012 → keine; Entscheidsuche CH_BGer/CH_BGE «"A-6142/2012"» → 0, «"A-6592/2013" OR "A-1552/2006"» → 0; OCL court=bger 2014–2017 «Kapitaleinlageprinzip Umwandlung …» → 66, «formwechselnde Umwandlung Anstalt …» → 64 (geprüft: 2C_697/2014 = DBG AR; 2C_16/2015 = Nachsteuer BL) | keine Bestätigung durch das BGer ermittelt |
| VPB 69.60, 61.64, 59.60 | Entscheidsuche IDs `CH_VB_015_JAAC-69-60--_2005-01-06`, `CH_VB_015_JAAC-61-64--_1995-04-28`, `CH_VB_008_JAAC-59-60--_1994-06-13` | gelesen |
| BGer vom 3.10.1996 (ASA 65 827, Walliser Kantonalbank; Bestätigung von VPB 61.64) | Entscheidsuche CH_BGer/CH_BGE «"droit de timbre" AND "Banque cantonale du Valais"» → 0; «Emissionsabgabe AND "Walliser Kantonalbank"» → 0 | nicht online; nur über ASA 65 827 zitierbar |

### 2. Ergänzungssuche (Entscheidsuche, `query_string`, `default_operator` AND)

Bund = Filter `hierarchy` [CH_BGer, CH_BGE, CH_BVGE, CH_VB]; Kantone = [ZH, BE, AG, BL, GE, VD, TI, BS, SG, LU, SO, ZG, FR, VS, NE].

| # | Filter | Abfrage | Treffer | Befund |
|---|---|---|---|---|
| 1 | Bund | `Genussschein* AND Emissionsabgabe` | 20 | geprüft A-5872/2008, A-364/2013, BVGE 2015/25, A-8711/2025, VPB 64.79, VPB 65.102: kein Bezug zu Art. 9 Abs. 1 lit. d (Regex auf «unentgeltlich»/«3 Franken» negativ); BGE 94 I 151, 95 I 560, 97 I 438: StG 1917 |
| 2 | Bund | `Genussschein* AND unentgeltlich AND Emissionsabgabe AND "Art. 9"` | 0 | – |
| 3 | Bund | `"bons de jouissance" AND "droit de timbre"` | 9 | BGE 83 I 128 (StG 1917), sonst VSt/Genussscheine allgemein; kein Art. 9 |
| 4 | Bund | `"buoni di godimento" AND bollo` | 29 | BVGer-VSt-Fälle (Rückerstattung); kein Art. 9 |
| 5 | Bund | `Emissionsabgabe AND Einzelunternehmen AND Umwandlung AND Nennwert*` | 0 | – |
| 6 | Bund | `Emissionsabgabe AND Personenunternehmung AND Umwandlung` | 1 | VPB 69.60 (schon erfasst) |
| 7 | Bund | `Emissionsabgabe AND Mehrwert AND "fünf Jahre*" AND Umwandlung` | 0 | – |
| 8 | Bund | `Emissionsabgabe AND "Art. 9 Abs. 1" AND Umwandlung` | 6 | BGE 115 Ib 125, 2A.618/1998, A-3554/2017, A-6592/2013, BGE 102 Ib 140, VPB 69.60; A-3554/2017: nur Art. 9 Abs. 1 FusG |
| 9 | Bund | `"droit de timbre" AND "art. 9 al. 1 let. e"` | 2 | BGE 148 II 121 / 2C_624/2021: Art. 9 al. 1 let. e LDMG (GE) – Fehltreffer |
| 10 | Bund | `"droit de timbre" AND "entreprise individuelle" AND transformation` | 1 | B-4919/2019: Prüfungsrekurs (Steuerexperten), Art. 9 al. 1 let. e LT nur als Musterlösung – Fehltreffer |
| 11 | Bund | `bollo AND "ditta individuale" AND trasformazione` | 1 | A-3761/2021 (schon erfasst) |
| 12 | Bund | `Emissionsabgabe AND Genossenschaft AND Rückzahlungen AND Einzahlungen` | 2 | A-3032/2021 (VSt), A-659/2007 (MWST) – kein Art. 9 Abs. 2 |
| 13 | Bund | `Emissionsabgabe AND Genossenschaftskapital` | 0 | – |
| 14 | Bund | `"droit de timbre" AND coopérative AND remboursements AND versements` | 1 | BGE 83 I 128 (StG 1917) |
| 15 | Bund | `Emissionsabgabe AND Kapitalband` | 0 | – |
| 16 | Bund | `Emissionsabgabe AND "genehmigte Kapitalerhöhung"` | 0 | – |
| 17 | Bund | `Emissionsabgabe AND Sitzverlegung AND "Art. 9"` | 0 | – |
| 18 | Bund | `Emissionsabgabe AND "nicht voll einbezahlt*" AND Namenaktien` | 0 | – |
| 19 | Bund | `Emissionsabgabe AND "Art. 9 StG"` | 1 | VPB 69.60 |
| 20 | Bund | `"droit de timbre" AND "art. 9 LT"` | 1 | VPB 61.64 |
| 21 | CH_BVGE | `"Art. 9 Abs. 1 Bst. e"` | 2 | B-4364/2009 (Art. 9 Abs. 1 Bst. e NBG), B-3154/2007 – Fehltreffer |
| 22 | CH_BVGE | `"Art. 9 Abs. 1 lit. e"` | 0 | – |
| 23 | CH_BGer | `"droit de timbre" AND "art. 9 al. 1"` | 3 | 2A.83/2001, 2A.84/2001, 2C_624/2021 (LDMG) |
| 24 | CH_BGer | `Emissionsabgabe AND "Art. 9 Abs. 1"` | 5 | 2C_1001/2014, 2C_976/2014, 2A.618/1998; 2C_334/2014 (aMWSTG), 2C_749/2017 (VGKE) – Fehltreffer |
| 25 | CH_VB | `Emissionsabgabe AND Genossenschaft` | 3 | VPB 69.60, 65.102, 69.125 (Letzterer: Erwähnung aArt. 9 Abs. 1 Bst. a, siehe Tabelle) |
| 26 | Kantone | `Emissionsabgabe` / `Emissionsabgabe AND Stempelabgaben` | 15 / 9 | ZH, AG, BS, BE: Einkommens-/Gewinnsteuer, Sozialversicherung; Regex auf Art. 9 StG / Genussschein / Kapitalband negativ |
| 27 | Kantone | `"droit de timbre d'émission"` | 8 | VD TC FI-…, GE CJ A/1572/2017: kein Art. 9 LT |
| 28 | Kantone | `"tassa di bollo" AND emissione` | 4 | TI CATI 80.2001.76: kantonale Legge sul bollo (art. 20 LB) – Fehltreffer |

Gegenprobe in Open Case Law (ohne Gerichtsfilter, compact): «Emissionsabgabe Kapitalband» → 94 (die ersten 8 sind Mantelhandels-/Quasifusionsfälle; Volltextprüfung 2C_621/2018, 2C_1071/2018, A-1592/2006: kein Art. 9 Abs. 3); «Emissionsabgabe Genossenschaft "Überschuss der Einzahlungen"» → 97 (geprüft A-3735/2017, 2A.716/2004, VPB 69.125, 2C_621/2018: kein Art. 9 Abs. 2); «Emissionsabgabe "unentgeltlich ausgegebene Genussscheine"» → 80 (geprüft 2C_299/2021, A-801/2007, A-5872/2008, VPB 65.102: kein Art. 9 Abs. 1 lit. d; BGE 94 I 151, 95 I 560, 97 I 438: StG 1917).

**Ergebnis der Ergänzungssuche:** Zu Art. 9 Abs. 1 lit. d (Genussscheine), Abs. 2 (Genossenschaften), Abs. 3 (Kapitalband bzw. früher genehmigte Kapitalerhöhung) und zu den aufgehobenen lit. b und c habe ich keine Rechtsprechung gefunden, weder beim Bund noch in den Kantonen. Zu lit. e gibt es nur BVGer A-3761/2021 (tragend) und die Erwähnung in VPB 69.60.

---

## (ii) Registertabelle

| Entscheid | Datum | Besetzung | Normstelle | Sachfrage | Kernaussage | E. | Ergebnis | Klasse | Fassung |
|---|---|---|---|---|---|---|---|---|---|
| BGE 102 Ib 140 | 14.5.1976 | nicht erkennbar (BGE-Auszug) | Abs. 1 lit. a (fusionsähnlicher Zusammenschluss) | Einbringung beherrschender Beteiligungen an drei Baugesellschaften in eine Holding (Kapitalerhöhung durch Aktienapport); Anspruch auf den halben Satz | Ein Zusammenschluss ist fusionsähnlich, wenn er wirtschaftlich wie eine Fusion wirkt und die Gründe der Privilegierung zutreffen; die Verbindung muss einer Fusion praktisch gleichkommen, was ohne Zweidrittelsmehrheit nicht der Fall ist; vorbestehende Bindungen schaden nicht. | 3a, 3b, 4, 5, 6, 7 | teilweise Gutheissung, Rückweisung (privilegiert für 2 Gesellschaften mit fast 100 %, nicht für N. AG mit 62,2 %) | A | F1973 |
| BGE 115 Ib 125 | 16.6.1989 | nicht erkennbar (BGE-Auszug) | Abs. 1 lit. a (Umwandlung, Aufspaltung) | Umwandlung einer Kommanditgesellschaft (Bank, 96,4 % von einer Holding-AG gehalten) in eine AG; ermässigter Satz? | Abs. 1 lit. a privilegiert nur Umwandlungen und Aufspaltungen der genannten Gesellschaften; Kommanditgesellschaften sind ausgenommen, weil Kommanditeinlagen seit 1.1.1967 nicht mehr abgabepflichtig sind; keine Aufspaltung der Holding. | 1, 2a, 2b, 3a, 3b | Abweisung (gemäss Regeste: Satz 1 % nicht anwendbar) | A | F1973 |
| BGer 2A.618/1998 vom 7. Februar 2000 | 7.2.2000 | Fünferbesetzung (Wurzburger, Hartmann, Hungerbühler, Müller, Yersin) | Abs. 1 lit. a; Art. 8 Abs. 3 | Umwandlung der Liechtensteinischen Landesbank (öffentlich-rechtliche Anstalt) in eine AG; Satz und Bemessungsgrundlage | Abs. 1 lit. a galt nur für Unternehmen, die vor der Umwandlung eine der genannten Rechtsformen hatten; eine öffentlich-rechtliche Anstalt fällt nicht darunter. Bemessung nach dem Wert der Aktiven und Passiven im Zeitpunkt der Umwandlung. | 4b/bb, 5a, 5b | Abweisung, soweit Eintreten; keine reformatio in peius | A | F1973 (Hinweis: «in Kraft bis zum 1. April 1993») |
| BGer 2A.84/2001 vom 5. März 2002 (fr.) | 5.3.2002 | Fünferbesetzung (Wurzburger, Hungerbühler, Müller, Yersin, Merkli) | art. 9 al. 1 let. a LT | Erwerb der restlichen Aktien einer zu 96,51 % gehaltenen Tochter durch Aktientausch, nachdem eine formelle Fusion an den Minderheitsaktionären scheiterte; ist das Privileg nach Überschreiten von 66 2/3 % verbraucht? | Die Zweidrittelschwelle aus BGE 102 Ib 140 schliesst das Privileg nur darunter aus; auch der Ausbau einer bereits qualifizierten Beteiligung kann fusionsähnlich sein, wenn er wirtschaftlich einen Wettbewerbsvorteil anstrebt (wirtschaftlicher Begriff). | 2.2, 2.3, 3, 4.1–4.5 (tragend 4.4) | Abweisung der Beschwerde der ESTV | A | F1973 (Vorgang 1991) |
| BGer 2A.83/2001 vom 5. März 2002 (fr.) | 5.3.2002 | Fünferbesetzung (wie 2A.84/2001) | art. 9 al. 1 let. a LT | Öffentliches Tausch- und Kaufangebot 1991; Erhöhung von 83,4 % auf 99 % des Kapitals der Tochter | Begründung wortgleich mit 2A.84/2001; abweichend nur E. 4.3 (Verstärkung der Beherrschung statt Vorbereitung der Fusion). | 2.2, 2.3, 3, 4.1–4.5 (tragend 4.3, 4.4) | Abweisung der Beschwerde der ESTV | A | F1973 (Vorgang 1991) |
| BGer 2C_976/2014 vom 10. Juni 2015 | 10.6.2015 | Dreierbesetzung (Zünd, Aubry Girardin, Haag) | aufgehobener Abs. 1 lit. a als Vorläufer von Art. 6 Abs. 1 lit. abis | Quasifusion (Hauptfrage Art. 6 Abs. 1 lit. abis) | Abs. 1 lit. a F1973 privilegierte dieselben Tatbestände; die Formel aus BGE 102 Ib 140 E. 3a gilt für Art. 6 Abs. 1 lit. abis weiter; wirtschaftliche Betrachtungsweise (Verweis auf 2A.84/2001). | 3.1, 3.2 | Abweisung (bestätigt BVGer A-6592/2013) | B | F1973 (historisch) |
| BGer 2C_1001/2014 vom 10. August 2015 | 10.8.2015 | Dreierbesetzung (Zünd, Donzallaz, Haag) | aufgehobener Abs. 1 lit. a als Vorläufer von Art. 6 Abs. 1 lit. abis | Quasifusion nach öffentlichem Übernahmeangebot (Beschwerde der ESTV) | Wie 2C_976/2014: Abs. 1 lit. a F1973 als Vorläufer; der Begriff ist im StG nicht umschrieben (BGE 102 Ib 140 E. 3). | 3.1, 3.2 | Gutheissung der Beschwerde der ESTV; BVGer-Urteil vom 11.9.2014 aufgehoben | B | F1973 (historisch) |
| BVGer A-3761/2021 vom 15. Oktober 2024 (it.) | 15.10.2024 | Dreierbesetzung (Rochat Pauchard, Widmer, Mutombo) | Abs. 1 lit. e; Art. 6 Abs. 1 lit. abis; Art. 5 Abs. 2 lit. a | Umstrukturierung eines Einzelunternehmens: Übertragung von Beteiligungen an sechs AG auf eine gekaufte AG-Hülle (Holding) ohne Kapitalerhöhung; ESTV erhebt CHF 1'132'740.35 als Zuschuss | Abs. 1 lit. e ist subsidiär zu Art. 6 Abs. 1 lit. abis (nur wenn eine beteiligte Einheit vorher nicht stempelabgabepflichtig war) und keine Auffangklausel; er ist bloss eine privilegierte Bemessung, keine Ausnahme, und verlangt wie Art. 6 Abs. 1 lit. abis die Begründung oder Erhöhung von Beteiligungsrechten. Erste Auslegung der Norm. | 5.3, 5.5.1, 5.5.2, 5.5.4, 5.5.6.1, 5.5.8, 5.5.9, 7.1, 7.2.3 | Abweisung (Kosten wegen geheilter Gehörsverletzung reduziert, E. 10) | A | F2004 (Vorgang 2011) |
| BVGer A-1552/2006 | 22.6.2009 | Dreierbesetzung (Beusch, Mollard, Stadelmann) | aufgehobener Abs. 1 lit. a als Auslegungshilfe für Art. 6 Abs. 1 lit. abis | Quasifusion: Gesetzmässigkeit einschränkender ESTV-Kriterien (Richtlinien 1997, Merkblatt 2001) | Die Rechtsprechung zu Abs. 1 lit. a F1973 gilt inhaltlich auch für Art. 6 Abs. 1 lit. abis; Hinweis auf BBl 1972 II 1294 (Privileg nur für neu geschaffene, den Gesellschaftern der übernommenen Gesellschaft zugeteilte Rechte). | 4.4.1, 4.4.3 | Gutheissung | B | F1973 (historisch) |
| BVGer A-6592/2013 | 18.9.2014 | Dreierbesetzung (Beusch, Steiger, Riedo) | aufgehobener Abs. 1 lit. a als Auslegungshilfe für Art. 6 Abs. 1 lit. abis | Quasifusion (Ausnahme bei Umstrukturierungen) | Abs. 1 lit. a F1973 ist für die interessierenden Fragen mit Art. 6 Abs. 1 lit. abis inhaltlich identisch (Verweis auf A-1552/2006 E. 4.4.1). Ein Verweis auf BBl 1972 II 1294 findet sich hier nicht. | 3.3.2.2 | Abweisung, soweit Eintreten; bestätigt durch BGer 2C_976/2014 vom 10. Juni 2015 | B | F1973 (historisch) |
| BVGer A-6142/2012 | 4.2.2014 | Dreierbesetzung (Zimmermann, Mollard, Riedo) | Art. 5 Abs. 1bis VStG (KEP); Emissionsabgabe bei Umwandlung (implizit Abs. 1 lit. e) | Formwechselnde Umwandlung einer öffentlich-rechtlichen Anstalt in eine AG; sind die Reserven Kapitaleinlagereserven? | Bei der formwechselnden Umwandlung werden Aktien erstmals ausgegeben; die Abgabe auf dem Verkehrswert entsprach der Praxis zur damaligen, «inzwischen geänderten» Regelung und wurde in der Lehre kritisiert; daraus folgen keine Kapitaleinlagen. | 7.5 (Umfeld 6.1–6.4, 7.4) | Abweisung; keine BGer-Bestätigung ermittelt | C | Rechtslage vor F2004 (Umwandlung vor 1.1.2004) |
| SRK vom 6.1.2005, VPB 69.60 | 6.1.2005 | nicht angegeben | Art. 8 Abs. 1 lit. a, Abs. 3; Hinweis auf Abs. 1 lit. e (F2004) und Abs. 1 lit. a (F1973) | Formwechselnde Umwandlung eines Vereins in eine AG (2002); Abgabe auf dem Nennwert oder auf dem Verkehrswert? | Bemessung nach dem Wert der Aktiven und Passiven; der neue Abs. 1 lit. e ist auf den Fall nicht anwendbar und eine bewusste Änderung der bisherigen Praxis zur Entlastung von Umwandlungen von Personenunternehmungen und Privatisierungen. | 2b, 3b/aa, 3b/bb, 3c | Abweisung (CHF 2'461'558 zusätzlich) | B (zu lit. e: C) | Rechtslage vor F2004; Ausblick auf F2004 |
| SRK vom 28.4.1995, VPB 61.64 (fr.) | 28.4.1995 | nicht angegeben | art. 9 al. 1 let. a LT; Systematik Art. 5/6/9 | Umwandlung einer (Kantonal-)Bank in eine öffentlich-rechtliche AG | Systematik: Regel (Art. 5), Ausnahmen (Art. 6), «cas de calcul dit spéciaux» (Art. 9); Abs. 1 lit. a erfasst nur Umwandlungen der genannten Gesellschaften, nicht von Anstalten. | 2b, 4a, 4b | Abweisung; laut Kopf bestätigt durch das BGer am 3.10.1996 (ASA 65 827; nicht online) | A | F1973 |
| Entscheid des Bundesrates vom 13.6.1994, VPB 59.60 | 13.6.1994 | Bundesrat | Art. 12 StG (Erlass); Abs. 1 lit. a nur referiert | Erlass der Emissionsabgabe bei Sacheinlagegründung einer Holding (Ende 1991) zur Sanierung von Bergbahn-Betriebsgesellschaften | Keine Rückwirkung von Art. 6 Abs. 1 lit. abis (Art. 53 Abs. 2 StG); kein Erlass, weil die abgabepflichtige Gesellschaft selbst nicht saniert wird; dem StG ist eine Konzernbetrachtung fremd. | 2, 3, 4.2–4.6 | Abweisung | C | F1973 (Gründung Ende 1991) |
| SRK vom 28.6.2005, VPB 69.125 | 28.6.2005 | nicht angegeben | aArt. 9 Abs. 1 Bst. a nur als Beispiel | Wirtschaftlich geprägte Begriffe im StG | Nennt den Begriff der fusionsähnlichen Zusammenschlüsse (aArt. 9 Abs. 1 Bst. a, neu Art. 6 Abs. 1 Bst. abis) als wirtschaftlich geprägten Begriff. | E.-Nummer nicht ermittelt | – | C | F1973 (historisch) |

**Weiterzug von BVGer A-3761/2021:** Das Urteil wurde beim Bundesgericht angefochten. Das zeigen die Kopfzeile der Entscheidsuche-Fassung («Decisione impugnata davanti al TF») und das spätere BVGer-Urteil A-5377/2023 vom 2.7.2025 («A-3761/2021 vom 15. Oktober 2024 [angefochten]»). Ein BGer-Urteil habe ich in Open Case Law und in Entscheidsuche nicht gefunden (Stand 28.10.2026; Abfragen siehe Suchprotokoll). BGer 9C_653/2024 vom 3. April 2025 betrifft diese Sache nicht: Es ist eine AHV-Beitragssache (Vorinstanz: Tribunale delle assicurazioni TI). Das Verfahren ist also hängig, oder das Urteil ist nicht publiziert bzw. nicht indexiert. Vor der Veröffentlichung neu prüfen.

**BGer 2A.83/2001 und 2A.84/2001 – inhaltsgleich?** In der rechtlichen Begründung ja. E. 2.1–2.3, 3, 4.1, 4.2, 4.4 und 4.5 sind wortgleich (Textübereinstimmung 96,3 %). Verschieden sind nur:
- der Sachverhalt: 2A.83 betrifft die Y. SA (Erhöhung von 83,4 % auf 99 % durch ein öffentliches Tausch- und Kaufangebot, 1'214 Aktien); 2A.84 betrifft die Z. Holding SA (96,51 %, gescheiterte formelle Fusion, danach Absorption, 2'410 Aktien);
- E. 4.3, die Würdigung des Einzelfalls;
- in 2A.84 E. 4.4 zusätzlich der Verweis auf «ATF 102 Ib 140 consid. 4 in fine p. 147».

Tragend sind in beiden Urteilen E. 4.4 (Zweidrittelschwelle ist keine Obergrenze) und E. 4.3 (Würdigung), gestützt auf E. 2.2 (wirtschaftlicher Begriff) und 4.1 (Kriterien aus BGE 102 Ib 140). 2C_976/2014 zitiert 2A.84/2001 mit «E. 2.2, 4.4, in: ASA 72 S. 170, StR 57/2002 S. 577, RDAF 2002 II 361».

**Datum von 2A.618/1998:** VPB 69.60 E. 3b/aa nennt das Urteil «vom 2. Februar 2000 (2A.618/1998, in ASA 69 S. 811 ff.)». Open Case Law und der Urteilskopf nennen den 7. Februar 2000. Massgebend ist das Urteil selbst (7.2.2000).

---

## (iii) Wörtliche Kernsätze

### BGE 102 Ib 140 (F1973; Klasse A)
- E. 3a: «Wirtschaftlich kommt der Zusammenschluss von Aktiengesellschaften einer Fusion gleich, wenn er zwar aus irgendwelchen Gründen nicht in einer der Formen nach Art. 748 ff. OR erfolgt, aber wirtschaftlich die gleichen Wirkungen hat wie eine Fusion und ausserdem die Gründe, die zur steuerlichen Privilegierung der Fusion führen, auch auf einen solchen Zusammenschluss zutreffen.»
- E. 3b: «Es rechtfertigt sich daher zwar, an die aus einem solchen Zusammenschluss zu erwartenden Wirkungen keinen strengeren Massstab anzulegen als gegenüber den eigentlichen Fusionen; indes setzt aber die Annahme eines fusionsgleichen Zusammenschlusses doch stets voraus, dass die Intensität der Verbindung rechtlich und tatsächlich nicht völlig integrierter Gesellschaften jener einer eigentlichen Fusion praktisch gleichkommt.» (Zweck nach der Botschaft BBl 1972 II 1294 ff.: Fusionen zur Stärkung der Wettbewerbsfähigkeit erleichtern, Konzentration aber nicht zu sehr erleichtern.)
- E. 4: «Das Gesetz will in diesem Falle den Zusammenschluss des Privilegs teilhaftig werden lassen ohne Rücksicht auf die rechtliche Form, in der die Wirtschaftskonzentration erreicht wird.»
- E. 5: «Es kommt vielmehr auf die tatsächliche Intensität der Verbindung an, die sich an den Beherrschungsverhältnissen misst.» – «Daraus erhellt, dass jedenfalls beim Fehlen der Zweidrittelsmehrheit die Beherrschung keine absolute ist, die Intensität der Verbindung somit einer eigentlichen Fusion nicht gleichgeachtet werden kann.»
- E. 6: «Ein Grund, hinsichtlich vorbestehender Bindungen die wirtschaftlich fusionsgleichen Zusammenschlüsse anders zu behandeln als die eigentlichen Fusionen, ergibt sich aus dem Gesetz nicht.» – «Sobald die fusionsgleichen Wirkungen Ziel des Zusammenschlusses sind und dieses Ziel durch die entsprechenden Beherrschungsverhältnisse auch erreicht werden kann, ist das Steuerprivileg zu gewähren.»
- E. 7: «Zusammenfassend ist demnach festzustellen, dass die Voraussetzungen für die Zuerkennung des Steuerprivilegs nach Art. 9 Abs. 1 lit. a StG hinsichtlich der Einbringung der Aktien der M. & Sohn AG sowie der O. AG in die M. Holding AG erfüllt sind, nicht aber soweit die 56 Aktien der N. AG in die M. Holding AG eingebracht worden sind.»

### BGE 115 Ib 125 (F1973; Klasse A)
- E. 1 (Agio, unbestritten): «Der Ausdruck "zufliesst" lässt erkennen, dass neben dem Nennwert der ausgegebenen Aktien auch das von der Gesellschaft bei der Ausgabe allenfalls erzielte Agio mit einzubeziehen ist (ASA 51, 496 E. 2a).»
- E. 2a (Gründe nach der Botschaft): «Es sollten damit Fusionen und gleichgestellte Tatbestände weder über Gebühr erleichtert noch erschwert werden (Botschaft des Bundesrates vom 25. Oktober 1972, BBl 1972 II S. 1278, 1284, 1294 ff.; dazu BGE 102 Ib 144 f. E. 3b; ASA 53, 275 E. 3a).»
- E. 2b (Kommanditgesellschaften): «Der Grund dafür ist darin zu erblicken, dass Kommanditeinlagen seit dem 1. Januar 1967 - seit der Aufhebung von Art. 34 bis 40 und 48 des Bundesbeschlusses über die Durchführung der Übergangsordnung des Finanzhaushaltes vom 22. Dezember 1938 (BS 6 S. 38, 43 ff.) durch Art. 72 des Bundesgesetzes über die Verrechnungssteuer vom 13. Oktober 1965 - der Stempelabgabe nicht mehr unterworfen sind.» – «Das gilt nach einem Entscheid des Bundesgerichts vom 11. April 1984 auch dann, wenn die umzuwandelnde Kommanditgesellschaft nach der bis Ende 1966 geltenden Gesetzgebung auf den Kommanditeinlagen Stempelabgaben entrichten musste (ASA 53, 157 ff.).»
- E. 3a (Aufspaltung): «Allgemein wird darunter der Vorgang verstanden, dass aus einer bestehenden Gesellschaft Aktiven und Passiven, die zusammen eine organische Einheit (Betrieb) bilden, ausgegliedert und auf eine Tochter- oder Schwestergesellschaft übertragen werden (ASA 53, 275 E. 3b, 441 E. 3b; […]).»
- E. 3b: «Art. 9 Abs. 1 lit. a StG privilegiert nicht Aufspaltungen, Umwandlungen usw. schlechthin, sondern nur solche von bestimmten Gesellschaften, namentlich von Aktiengesellschaften.»

### BGer 2A.618/1998 vom 7. Februar 2000 (F1973; Klasse A; Fünferbesetzung)
- E. 4b/bb: «Dennoch kann letztlich offen bleiben, wie der Rechtsformwechsel bei der Beschwerdeführerin genau abgewickelt worden ist.» – «Eine Abänderung des angefochtenen Entscheids zuungunsten der Beschwerdeführerin ist deshalb - ungeachtet des Umstands, dass einer Korrektur angesichts der Differenz im Steuerbetrag erhebliche Bedeutung zukäme - nicht geboten.»
- E. 5a: «Diese Bestimmung fand aber ausschliesslich auf jene Unternehmen Anwendung, welche vor der Umwandlung in eine der Rechtsformen gekleidet waren, die im Gesetzestext erwähnt werden (Aktien-, Kommanditaktiengesellschaft, Genossenschaft oder Gesellschaft mit beschränkter Haftung; Urteil vom 3. Oktober 1996 in: ASA 65 S. 835 f., mit Hinweisen). Da dies bei der Beschwerdeführerin als öffentlichrechtliche Anstalt nicht der Fall war, kann sie sich nicht auf Art. 9 Abs. 1 lit. a StG berufen.»
- E. 5b: «Die Vorinstanz hat dieses Argument mit der (zutreffenden) Begründung verworfen, dass die Emissionsabgabe nach dem Wert zu bestimmen sei, den die eingebrachten Aktiven und Passiven im Zeitpunkt der Umwandlung gehabt hätten (Art. 8 Abs. 3 StG ; vgl. Urteil vom 3. Oktober 1996 in: ASA 65 S. 836 f.).»

### BGer 2A.84/2001 vom 5. März 2002 (fr.; F1973; Klasse A; Fünferbesetzung)
- E. 2.2: «Il est conforme au caractère formel des droits de timbre que la forme juridique donnée à l'opération soit décisive et non pas le but économique poursuivi par les intéressés.» (Ausnahme: Begriffe mit wirtschaftlichem Gehalt wie «concentration équivalant économiquement à une fusion».)
- E. 4.1 (wirtschaftlich aktive Gesellschaften, Hinweis auf das Urteil vom 12.12.1997): «le Tribunal fédéral a précisé que le privilège fiscal de l'art. 9 al. 1 lettre a LT (nouvellement art. 6 al. 1 lettre a bis LT) supposait que les sociétés concernées soient économiquement actives».
- E. 4.4: «Toutefois, ce faisant, il excluait uniquement l'octroi du privilège fiscal de l'art. 9 al. 1 lettre a LT tant que l'augmentation des participations ne conférait pas la majorité des deux tiers des droits de vote à son détenteur.» – «Mais, elles ne préjugent toutefois pas de l'avantage concurrentiel recherché ou attendu sous l'angle économique d'une augmentation de la participation au delà d'un tel seuil, ce que la Commission de recours s'est attachée à bon droit à démontrer de manière convaincante.»
- E. 4.5: «Par conséquent, en qualifiant de concentration analogue à une fusion l'émission des actions nécessaire à l'échange des participations des sociétés X.________ SA et Z.________ SA et la privilégiant fiscalement, la Commission de recours n'a pas violé l'art. 9 al. 1 lettre a LT.»

### BGer 2A.83/2001 vom 5. März 2002 (fr.; F1973; Klasse A; Fünferbesetzung)
- E. 4.3 (abweichende Würdigung): «Il apparaît, dans ces conditions, que l'offre publique d'achat permettait à X.________ SA de renforcer considérablement sa domination de Y.________ SA et sa capacité concurrentielle conformément aux exigences de la jurisprudence rappelée ci-dessus.»
- E. 2.2, 4.1, 4.4: wortgleich mit 2A.84/2001 (ohne den Zusatzverweis auf BGE 102 Ib 140 E. 4 in 4.4).

### BGer 2C_976/2014 vom 10. Juni 2015 (Klasse B)
- E. 3.1: «Bereits das Stempelgesetz in der Fassung vom 27. Juni 1973 (AS 1974 11) kannte für "Beteiligungsrechte, die in Durchführung von Beschlüssen über Fusionen oder diesen wirtschaftlich gleichkommende Zusammenschlüsse, Umwandlungen und Spaltungen" begründet werden, einen privilegierten Satz (aufgehobener Art. 9 Abs. 1 lit. a StG).»
- E. 3.2 (Übertragung der Formel auf Art. 6 Abs. 1 lit. abis): «Nach einer Formel des Bundesgerichts zur Stempelabgabe werden als der Fusion wirtschaftlich gleichkommende Zusammenschlüsse Transaktionen bezeichnet, die aus irgendwelchen Gründen nicht als Fusionen abgewickelt werden, aber wirtschaftlich die gleiche Wirkung haben wie eine Fusion und ausserdem die Gründe, die zur steuerlichen Privilegierung der Fusion führen, auch auf einen solchen Zusammenschluss zutreffen (BGE 102 Ib 140 E. 3a S. 143; Urteil 2A.17/1994 vom 5. Februar 1996 E. 3b, in ASA 65 S. 666).»

### BGer 2C_1001/2014 vom 10. August 2015 (Klasse B)
- E. 3.1: «Schon das Stempelgesetz in der Fassung vom 27. Juni 1973 (AS 1974 11) kannte für "Beteiligungsrechte, die in Durchführung von Beschlüssen über Fusionen oder diesen wirtschaftlich gleichkommende Zusammenschlüsse, Umwandlungen und Spaltungen" begründet werden, einen privilegierten Satz (aufgehobener Art. 9 Abs. 1 lit. a StG).»
- E. 3.2: «Der Begriff des wirtschaftlich einer Fusion gleichkommenden Zusammenschlusses von Gesellschaften wird im Bundesgesetz über die Stempelabgaben nicht näher umschrieben (s. auch BGE 102 Ib 140 E. 3 S. 143 ff.).»

### BVGer A-3761/2021 vom 15. Oktober 2024 (it.; F2004; Klasse A)
Sachverhalt: Der Inhaber eines Tessiner Einzelunternehmens liess sich 2006/2007 von der ESTV eine Umstrukturierung nach Art. 9 Abs. 1 lit. e bestätigen (Gründung einer oder mehrerer AG mit anschliessender Einbringung in eine Holding). Umgesetzt wurde etwas anderes: 2010 kaufte er eine bestehende AG-Hülle, und 2011 übertrug er ihr ohne Kapitalerhöhung Beteiligungen an sechs AG (Gegenbuchung «Apporto Capitale»/«Aggio d'apporto»). Die ESTV erhob darauf CHF 1'132'740.35 Emissionsabgabe als Zuschuss (Art. 5 Abs. 2 lit. a).
- E. 5.3: «Alle ristrutturazioni con società di persone si applica l’art. 9 cpv. 1 lett. e LTB, che non prevede un’esenzione come nel caso dell’art. 6 cpv. 1 lett. abis LTB, bensì unicamente un trattamento fiscale privilegiato, nel senso che la tassa di bollo non viene calcolata sul valore venale, bensì sul valore nominale dell’operazione interessata».
- E. 5.5.2: «L’art. 9 cpv. 1 lett. e LTB ha una portata sussidiaria rispetto all’art. 6 cpv. 1 lett. abis LTB: esso si applica unicamente nel caso in cui una delle entità interessate dalla ristrutturazione non era soggetta alla tassa di bollo prima di tale processo.» – «L’art. 9 cpv. 1 lett. e LTB non rappresenta dunque una clausola di salvaguardia per le ristrutturazioni d’imprese che non rispettano le condizioni dell’art. 6 cpv. 1 lett. abis LTB».
- E. 5.5.4: «l’art. 9 cpv. 1 lett. e LTB non è ancora stato oggetto d’interpretazione né della giurisprudenza dello scrivente Tribunale, né di quella del Tribunale federale.»
- E. 5.5.6.1: «Detto in altri termini, l’art. 9 cpv. 1 lett. e LTB non prevede una esenzione dalla tassa di bollo d’emissione analogamente all’art. 6 cpv. 1 lett. abis LTB, bensì unicamente un trattamento fiscale privilegiato, a determinate condizioni, delle ristrutturazioni di società di persone, mediante l’assoggettamento alla tassa di bollo d’emissione calcolata sul valore nominale dei diritti di partecipazione costituiti o aumentati in tale contesto».
- E. 5.5.8: «A mente del Tribunale, sebbene non sia contemplato dal testo della disposizione, l’art. 9 cpv. 1 lett. e LTB deve dunque essere interpretato in conformità all’art. 6 cpv. 1 lett. abis LTB.» (Das Gericht weicht damit bewusst von der dort referierten Mehrheitslehre ab.)
- E. 5.5.9: «il trattamento fiscale privilegiato dell’art. 9 cpv. 1 lett. e LTB esige per la sua applicazione la costituzione/creazione o aumento dei diritti di partecipazione conformemente a decisioni di fusione, scissione o trasformazione di società di persone.»
- E. 7.1: «Già per tale motivo, l’art. 9 cpv. 1 lett. e LTB, non trova qui applicazione, poiché – come visto (cfr. considd. 5.3 e 5.5.2 del presente giudizio) – detta norma si applica unicamente alle ristrutturazioni di società di persone in società di capitali.»
- E. 8.2.4 (Ruling): «In definitiva, visto quanto precede, si deve concludere che non vi sono gli estremi per riconoscere la sussistenza di un « ruling » vincolante.»
- E. 10: «In definitiva, il ricorso - per quanto ammissibile (cfr. consid. 1.3 del presente giudizio), il ricorso va respinto.»

### BVGer A-1552/2006 (Klasse B)
- E. 4.4.1: «Wann von einem solchen auszugehen ist, lässt sich grundsätzlich bereits der bundesgerichtlichen Rechtsprechung zum damaligen (inhaltlich für die vorliegend interessierenden Fragen dem ab 1. April 1993 in Kraft stehenden Art. 6 Abs. 1 Bst. abis StG entsprechenden) Art. 9 Abs. 1 Bst. a StG entnehmen.»
- E. 4.4.3: «Weiter wird ausgeführt, die emissionsabgaberechtliche Privilegierung (durch den damaligen Art. 9 Abs. 1 Bst. a StG) solle "natürlich nur für Beteiligungsrechte gelten, die von der aufnehmenden Gesellschaft beim Zusammenschluss neu geschaffen und den Gesellschaftern der aufgenommenen Unternehmung zugeteilt werden, dagegen nicht auch für nebenhergehende Kapitalerhöhungen der aufnehmenden Gesellschaft für ihre alten Aktionäre" (BBl 1972 II 1294).»

### BVGer A-6592/2013 (Klasse B)
- E. 3.3.2.2: «Die Gerichte – insbesondere das Bundesgericht – haben sich bereits verschiedentlich mit fusionsähnlichen Zusammenschlüssen gemäss Art. 6 Abs. 1 Bst. a bis StG bzw. dem inhaltlich für die vorliegend interessierenden Fragen identischen, bis zum 1. April 1993 in Kraft gestandenen Art. 9 Abs. 1 Bst. a StG (vgl. Urteil des Bundesverwaltungsgerichts A-1552/2006 vom 22. Juni 2009 E. 4.4.1) auseinandergesetzt.»
- Der Hinweis auf BBl 1972 II 1294 steht nur in A-1552/2006 E. 4.4.3, nicht in A-6592/2013 (Volltextsuche nach «1294» negativ).

### BVGer A-6142/2012 (Klasse C)
- E. 7.5: «Auch anlässlich einer formwechselnden Umwandlung einer öffentlich-rechtlichen Anstalt in eine Aktiengesellschaft werden Aktien erstmals ausgegeben, womit die Emissionsabgabe geschuldet ist. Dass die Abgabe dabei auf dem Verkehrswert geschuldet war, entsprach der Praxis der ESTV zur dazumal geltenden – inzwischen geänderten – gesetzlichen Regelung und – soweit vorhanden – der dazugehörigen Rechtsprechung, wobei diese Bemessung der Emissionsabgabe auf dem Verkehrswert in der Lehre kritisiert wurde (vgl. beispielsweise SCHMID/LEHMANN, a.a.O., S. 282).»
- E. 7.5 (Folge für die VSt): «Die Emissionsabgabe ist unabhängig davon geschuldet, ob der Gesellschaft mit der Ausgabe der Aktien auch Leistungen von aussen zufliessen, womit bereits aus diesem Grund keine Rückschlüsse auf die verrechnungssteuerrechtliche Qualifikation der streitbetroffenen Reserven gemacht werden können.»
- Art. 9 StG wird nicht ausdrücklich genannt; die «inzwischen geänderte» Regelung meint der Sache nach Art. 9 Abs. 1 lit. e (F2004). Umfeld: E. 6.2.1–6.2.3 (Umwandlung vor dem FusG; FusG seit 1.1.2004).

### SRK vom 6.1.2005, VPB 69.60 (Klasse B; zu lit. e Klasse C)
- E. 2b: «Sachen und Rechte sind zum Verkehrswert im Zeitpunkt ihrer Einbringung zu bewerten (Art. 8 Abs. 3 StG).»
- E. 3b/aa (Wiedergabe von SRK 1997-013, bestätigt durch 2A.618/1998): «Der Gesetzgeber habe aber auf jeden Fall keine Limitierung der Emissionsabgabe auf das nominelle Kapital vorgesehen und sich darauf beschränkt, die Reduktion der Emissionsabgabe für die in Art. 9 Abs. 1 Bst. a StG einschränkend aufgezählten Fälle vorzusehen.»
- E. 3b/bb: «Es ist daher festzuhalten, dass auch bei formwechselnder Umwandlung eines Vereins in eine Aktiengesellschaft, wie sie hier vorliegt, die Berechnung der Emissionsabgabe nach demWert [sic] der eingebrachten Aktiven und Passiven im Zeitpunkt der Umwandlung zu erfolgen hat.»
- E. 3b/bb (zu Abs. 1 lit. e): «Zum Anderen stellt diese Bestimmung eine bewusste Änderung des Gesetzgebers gegenüber der bis anhin geltenden Praxis dar, mit dem Ziel, den in der Praxis häufig anzutreffenden Vorgang der Umwandlung einer Personenunternehmung in eine juristische Person sowie die Privatisierung öffentlicher Unternehmungen steuerlich zu entlasten (vgl. das Votum von Rolf Schweiger als Kommissionssprecher in AB 2001 S 163). Zudem differenziert auch diese Bestimmung nicht zwischen den verschiedenen Formen der Umwandlung, sondern behandelt in Bezug auf die Emissionsabgabe alle identisch.»
- E. 3c: Bewertung des Nettovermögens auf CHF 258'977'400 unbestritten; Nachforderung von CHF 2'461'558 bestätigt.

### SRK vom 28.4.1995, VPB 61.64 (fr.; Klasse A)
- E. 2b (Systematik): «Or, l’assujettissement au droit de timbre d’émission est conçu de telle manière qu’il comprend la règle (art. 5 LT), les exceptions (art. 6 LT) et les cas de calcul dit spéciaux (art. 9 LT).»
- E. 4a: «Du texte de la LT, il ressort que seule la transformation de sociétés - anonymes, en commandite par actions, à responsabilité limitée et coopératives - peut entrer en ligne de compte.» – «Les intentions du législateur étaient en effet d’éviter d’imposer des sociétés qui avaient déjà été frappées du droit de timbre (Archives, vol. 53 p. 158 consid. 1b; BO CE 1973 239; […]).»
- E. 4b (Formalismus): «Ils frappent des transactions résultant d’opérations juridiques fixées par la loi et, eu égard à leur caractère formel, il n’est pas admissible que des considérations d’ordre économique entrent en ligne de compte, seule la forme juridique donnée à la transaction étant déterminante […].»

### Entscheid des Bundesrates vom 13.6.1994, VPB 59.60 (Klasse C)
Gegenstand: Erlass der Emissionsabgabe nach Art. 12 StG bei der Sacheinlagegründung einer Holding Ende 1991. Die Holding sollte die eingebrachten Bergbahn-Betriebsgesellschaften sanieren.
- E. 2 referiert Art. 9 Abs. 1 Bst. a (ermässigter Satz von 1 % für Fusionen, fusionsähnliche Zusammenschlüsse, Umwandlungen und Aufspaltungen von AG).
- E. 3: «Seit dem Inkrafttreten am 1. April 1993 der Änderung des BG über die Stempelabgaben vom 4. Oktober 1991 sind Beteiligungsrechte, die in Durchführung von Beschlüssen über Fusionen oder diesen wirtschaftlich gleichkommende Zusammenschlüsse, Umwandlungen und Aufspaltungen von Aktiengesellschaften begründet oder erhöht werden, von der Emissionsabgabe ausgenommen (Art. 6 Abs. 1 Bst. abis StG, AS 1993 224).» Nach Art. 53 Abs. 2 StG gilt das alte Recht für vorher entstandene Abgabeforderungen weiter.
- E. 4.4: «Die von der Beschwerdeführerin geforderte konzernmässige Betrachtungsweise ist dem hier allein anzuwendenden Stempelsteuerrecht fremd.»
- Ob der Vorgang unter Abs. 1 lit. a fiel, prüft der Entscheid in den gelesenen Stellen nicht.

---

## (iv) Fehltreffer (mit Grund)

| Entscheid | Grund |
|---|---|
| BGE 86 I 60 (11.3.1960) | Kein Stempelabgaberecht: Verantwortlichkeitsgesetz/BZP (Zuständigkeit, Verwirkung; laut Regeste). Fällt jedenfalls in die Zeit des StG 1917. |
| BGE 96 I 602 (25.9.1970) | StG 1917: Art. 11 Abs. 1 lit. c aStG (Steuerfreiheit grundpfandgesicherter Darlehen). |
| BGE 91 I 393 (22.12.1965) | Doppelbesteuerung (Art. 46 BV); «Art. 9 STG» in den Metadaten meint ein kantonales Steuergesetz. |
| BGer 2C_377/2017 vom 4. Oktober 2017 | Kantonssteuer VS und DBG 2011 (Art. 162, 165 kantonales StG). |
| BGer 2C_21/2017 vom 2. August 2017 | Kantonssteuer TI und DBG 2006. |
| BGer 9C_653/2024 vom 3. April 2025 | AHV-Beiträge (TI); kein Bezug zu A-3761/2021. |
| BGE 148 II 121 / BGer 2C_624/2021 vom 28.3.2022 | Art. 9 al. 1 let. e LDMG (Genfer Handänderungssteuer). |
| BGE 83 I 128, BGE 94 I 151, BGE 95 I 560, BGE 97 I 438 | Entscheide zum StG 1917 (vor 1.7.1974); Genussscheine/Genossenschaften nach altem Recht. |
| BVGer B-4919/2019 | Prüfungsrekurs (Steuerexpertenprüfung); «art. 9 al. 1 let. e LT» nur Teil der Musterlösung. |
| BVGer B-4364/2009, B-3154/2007 | Art. 9 Abs. 1 Bst. e NBG bzw. anderer Erlass. |
| BVGer A-3554/2017 | Nur Art. 9 Abs. 1 FusG (Kapitalerhöhung bei Absorptionsfusion), im Rahmen von Art. 6 Abs. 1 lit. abis. |
| BGer 2C_334/2014, 2C_749/2017 | Art. 9 aMWSTG bzw. Art. 9 VGKE. |
| BVGer A-3032/2021, A-659/2007 | VSt bzw. MWST; «Einzahlungen/Rückzahlungen» ohne Bezug zu Art. 9 Abs. 2. |
| TI CATI 80.2001.76 | Kantonale Legge sul bollo (art. 20 LB). |
| BVGer A-4789/2021, A-556/2024 | Zitieren A-3761/2021 nur zu Verwaltungsverordnungen (E. 2.3.2), nicht zu Art. 9. |
| BGer 9C_232/2026, 9C_209/2025 | Mantelhandel (Art. 5 StG) bzw. Einkommenssteuer; tauchen nur in Trefferlisten auf. |
