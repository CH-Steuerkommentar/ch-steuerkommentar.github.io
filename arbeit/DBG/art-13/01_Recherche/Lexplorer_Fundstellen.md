# Lexplorer-Fundstellen Art. 13 DBG (ILE-Literatur)

Lauf vom 27.10.2026 (Einbau der ILE-Literatur). Werkzeug: Lexplorer Tax, `filter_kanton: "CH"`, `filter_category: "08-institut-fuer-law-und-economics"`. Treffer aus «ILE-HSG — Lehrbuch Steuerrecht» (Hongler/Lorenz) übergangen. Autor:innen jeweils am Kopf des Beitrags bzw. Kapitels geprüft (nicht nur an der Chunk-Angabe).

## Suchen (14)

| Nr. | Werkzeug | Abfrage | verwendet |
|---|---|---|---|
| 1 | hybrid | Zahlungsunfähigkeit Ehegatte Solidarhaftung Art. 13 Abs. 1 DBG BGE 149 II 442 | Oesterhelt/Opel 2024/1; Rajower/Weber Rajower 2009 |
| 2 | hybrid | Solidarhaftung Ehegatten Trennung Scheidung offene Steuerschulden Art. 13 Abs. 2 DBG Aufteilung Haftungsverfügung | Rajower/Weber Rajower 2009 (Seminarfolien Bern 2021 gelesen, nicht verwendet) |
| 3 | hybrid | Mithaftung Käufer Verkäufer Liegenschaft 3 Prozent Kaufsumme Händler Vermittler ohne Wohnsitz Art. 13 Abs. 3 DBG | – (nichts Einschlägiges) |
| 4 | hybrid | solidarische Haftung Teilhaber Personengesellschaft im Ausland wohnende Teilhaber Gesellschaftsanteil … | – (Brülisauer/Kriesi 2008 und Seminarfolien gelesen, betreffen Art. 10/11 DBG) |
| 5 | keyword | "Art. 13 Abs. 3" DBG | Rostetter 2019; Rajower 2007 (1. Teil) |
| 6 | hybrid | Sicherstellung gegenüber Ehegatten und Mithaftenden Art. 169 DBG … | Rajower 2007 (2. Teil) |
| 7 | hybrid | Haftung Willensvollstrecker Erbschaftsverwalter Steuern des Erblassers Sorgfalt Entlastungsbeweis Art. 13 Abs. 4 DBG | Oesterhelt/Opel 2025-2 |
| 8 | hybrid | Mithaftender Anfechtung rechtskräftige Veranlagung Haftungsverfügung … Art. 55 DBG | – |
| 9 | hybrid | Individualbesteuerung Wegfall Solidarhaftung Ehegatten … | Fenners/Baumgartner/Duss 2026 |
| 10 | hybrid | Nachsteuer getrennte Ehegatten Solidarhaftung Aufteilung Hinterziehungsbusse … Art. 180 DBG | – (Berdoz/Bugnon 2021 gelesen, nichts über den Text hinaus) |
| 11 | hybrid | Kindereinkommen Inhaber der elterlichen Sorge Steuersubstitution Haftung des Kindes … | – (nur Lehrbuch und Art. 9 DBG) |
| 12 | hybrid | Haftung bis zum Betrag des Reinerlöses Veräusserung Grundstück … Auflösung Betriebsstätte | – (leer) |
| 13 | hybrid | Mithaftung Reinerlös Veräusserung Grundstück ohne Wohnsitz Art. 55 Abs. 2 DBG | – (leer) |
| 14 | hybrid | Rechtsmissbrauch Scheidung Ehegatten Solidarhaftung Steuerschulden | Rajower/Weber Rajower 2009 (Chunk-IDs) |

## Verwendete Fundstellen

### Rajower Felix/Weber Rajower Ursula, Ehegatten- und Erbenhaftung im Recht der direkten Steuern, FStR 2009
- lexplorer_url (Dokument): https://app.lexplorer.ch/suche?e_id=403&e_sys=ile; doc_id `f416c88a-6561-44f4-b4c6-7b94abfc0940` (Autoren am Kopf: «Dr. iur. Felix Rajower/Lic. iur. Ursula Weber Rajower»).
- Abfragen 1, 2, 14. Gelesen über `get_document_slice` (Slices 0–4 und 6 zu 15000 Zeichen).

| Ziff. | Chunk | tragender Satz (gekürzt) | verwendet in |
|---|---|---|---|
| 2.2 | 15648 (`1d54e2a2-d818-4d20-b672-e6137e37d856`) | «Die bundesrätliche Fassung zum DBG wollte sich ebenfalls mit einer Teilschuldnerschaft der Ehegatten begnügen … Im eidg. Parlament setzte sich dann aber … die Solidarhaftung der Ehegatten durch»; BS/BL nur Teilschuldnerschaft | entstehung, kantone |
| 2.3.1 | Chunk 11 (über Slice 0/1) | «Aus steuerrechtlicher Sicht ist die Solidarhaftung die konsequente Fortführung der gemeinschaftlichen Veranlagung (Faktorenaddition) im Steuerbezug»; Einwand aus Art. 166 ZGB «insofern unbegründet» für Steuern auf Einkünften für die laufenden Bedürfnisse, für Vermögensbildung «nur schwer begründen»; BGer lehnt Verletzung der derogatorischen Kraft ab; «steht es der Bezugsbehörde frei, den ganzen Steuerbetrag beim Ehemann oder bei der Ehefrau oder bei beiden einzutreiben» | eigenstaendig, kritik-solidarhaftung, or-regeln |
| 2.3.2 | 15653 (`3e8c67dd-a837-4d03-a729-03e129ec4d6f`) | Nationalrat stimmte mit 96 zu 60 Stimmen zu, «nachdem die Solidarhaftung bei Zahlungsunfähigkeit … wie auch bei Ehetrennung für aufhebbar erklärt worden war» | entstehung |
| 2.3.2.1 | 15653 | Aufhebung bei Zahlungsunfähigkeit, um zu verhindern, «dass ein Ehegatte den auf seinen Partner entfallenden Anteil ‹quasi à fonds perdu› leistet» | zweck |
| 2.3.2.1.1 | Chunk 13 (Slice 1) | Zahlungsunfähig, wer «auf unbestimmte Zeit nicht über ausreichende Mittel verfügt» (Art. 83 OR, Art. 897 ZGB analog); Verlustscheine, Konkurs, Nachlassvertrag mit Vermögensabtretung «kann – muss aber nicht –» Zahlungsunfähigkeit bedeuten; kurzer Engpass genügt nie | formel-alt |
| 2.3.2.1.2 | 15658 (`9bbb7f73-10af-4ad3-9e6a-09fe889f697e`) | keine Berufung auf Zahlungsunfähigkeit, wenn Mittellosigkeit auf Entreicherungen zugunsten der Familie beruht (2P.67/2003); hypothetische pfändbare Quote: «das Total des betreibungsrechtlichen Bedarfs beider Ehegatten dem Total des Einkommens beider Ehegatten gegenüberzustellen, wobei ein allfälliger Überschuss prozentual im Verhältnis des jeweiligen Einkommens … aufzuteilen ist»; Konkurs beweist nicht generell Zahlungsunfähigkeit; Vorbehalt des Rechtsmissbrauchs | formel-alt, unwille, gesamtwuerdigung |
| 2.3.2.1.3 | 15662 (`54149b32-b75d-4d84-9985-19f3ea7eb509`) | «Die Zahlungsunfähigkeit eines Ehegatten ist nur auf entsprechendes Begehren hin zu berücksichtigen»; schutzwürdiges Interesse «regelmässig nur der solvente Ehegatte» | gesuch (a.M.) |
| 2.3.2.1.4 | 15663 (`4f5ff4e2-0964-4d20-bb1e-968b470fb6dc`) | Ehegattenhaftung ist eine Frage des Steuerbezugs; «die Frage der Haftung von Ehegatten für die rechtskräftig festgesetzten Gesamtsteuern [fällt] in die Zuständigkeit der Bezugsbehörden» | haftungsverfuegung |
| 2.3.2.1.5 | 15665 (`bf46d316-87b2-4e2f-8168-5670a6edd51a`) | «Der Nachweis der Zahlungsunfähigkeit des andern Ehegatten muss im Sinn einer steuermindernden Tatsache vom Antragsteller erbracht werden» | beweis |
| 2.3.2.1.6 | Chunk 18 (Slice 2) | Wegfall «gemäss allgemeiner Auffassung für alle noch offenen Steuerforderungen»; rückwirkende Aufhebung «inkonsequent und nicht systemkonform» (Behnisch); «beansprucht die historische Auslegung Vorrang vor der systemkonformen Gesetzesauslegung» | rueckwirkung |
| 2.3.2.2 | 15670 (`34e5e930-b6b1-43f4-8558-034d48327832`) | Art. 13 Abs. 2 DBG hält ausdrücklich fest, dass die Solidarhaftung «auch für alle noch offenen Steuern entfällt»; Wortlaut eindeutig und deckt sich mit der Absicht des Gesetzgebers | trennung-begriff |
| 2.3.2.3 | 15673 (`536fd774-2787-480d-a534-cae245aad40c`) | Kantone ohne Klärung im Sinne von Art. 13 Abs. 2 DBG (u.a. ZH, VD); BGer schützte Fortdauer für AR | kantone |
| 2.3.3 | Chunk 25/26 (Slice 3) | AI, AR, VD: Solidarhaftung «unter allen Umständen», auch bei Zahlungsunfähigkeit; strengere Lösungen nach BGer nicht zu beanstanden; Luzern: höchstens das Doppelte des eigenen Steueranteils bei Nachweis | kantone |
| 2.4.1 | 15687 (`054e46a4-88e8-4602-8126-b400548b5dcf`) | Bezugsbehörde bestimmt Anteile auf Grundlage der rechtskräftigen Einschätzung; Verhältnis des Reineinkommens, «nur die organischen Abzüge (Berufskosten) berücksichtigt und die anorganischen (Sozial-)Abzüge ausser Betracht gelassen»; kein Rückkommen auf die rechtskräftige Einschätzung | haftungsverfuegung, anteil-berechnung |
| 2.4.2 | Chunk 28 (Slice 3) | bei Ermessenseinschätzung hat der Gesuchsteller die tatsächlichen Werte beider Ehegatten zu belegen; «Fehlen jegliche Anhaltspunkte, so erscheint … eine hälftige Aufteilung der Gesamtsteuerschuld … als angemessen» | anteil-berechnung |
| 2.4.3 | Chunk 29 (Slice 3/4) | drei Vorschläge zur Anrechnung früherer Zahlungen (zahlender Ehegatte; beide nach Haftungsanteilen; je hälftig); «Alles in allem erscheint die anteilsmässige Anrechnung … im Verhältnis zu den in der Haftungsverfügung festgelegten Anteilen noch die sachgerechteste Lösung» | offene-schulden |
| 3.3.5 | Chunk 51 (Slice 6) | Regress unter Erben: «Richtig betrachtet, beurteilt sich die Frage des Regresses … nach den entsprechenden zivilrechtlichen Bestimmungen, sofern die Kantone von der Möglichkeit, die Rückgriffsordnung zu regeln, keinen Gebrauch gemacht haben» | or-regeln |
| 4.3 | Chunk 52 (Slice 6) | Im Bund haftet der überlebende Ehegatte für die beim Tod ausstehenden Steuern nicht mehr, «sondern [ist] nur noch verpflichtet …, seinen Anteil an der Gesamtsteuer zu leisten»; daneben haftet er als Erbe solidarisch für den Anteil des Erblassers | tod, tod-praxis |

### Oesterhelt Stefan/Opel Andrea, Rechtsprechung 2024/1, FStR 2024 (Besprechung BGer 9C_233/2023 vom 3.10.2023 = BGE 149 II 442)
- lexplorer_url (Dokument): https://app.lexplorer.ch/suche?e_id=577&e_sys=ile; doc_id `c8ae20f7-114b-4b55-a83d-ca6769e84f1b`; Autoren am Kopf «Stefan Oesterhelt/Andrea Opel».
- Abfrage 1. Ziff. 4.3 «Bemerkungen» = Chunks 13690 (`e49ec8b7-48fa-4791-ae40-d13c54189056`), 13691, 13692 (über `get_document_slice`, Slices 2 zu 20000 und 10 zu 6000).

| Ziff. | Chunk | tragender Satz (gekürzt) | verwendet in |
|---|---|---|---|
| 4.3 | 13690 | «Insbesondere bleibt offen, welches der massgebliche Zeithorizont sein soll …»; «Offen bleibt damit, ob der vorliegende Entscheid eine Aufweichung des bisherigen Verständnisses des zeitlichen Kriteriums bedeutet»; kurzfristiger Engpass genügt weiterhin nicht | frist |
| 4.3 | 13691 | Verfassungskonformität der Solidarhaftung «erscheint fraglich»: Schlechterstellung gegenüber Konkubinatspartnern (Art. 14, 8, 127 Abs. 2 BV), faktisch Benachteiligung von Ehefrauen; Art. 190 BV für die direkte Bundessteuer; Literatur verlangt Wahl des belangten Ehegatten nach pflichtgemässem Ermessen und Verhältnismässigkeit; Abs. 2 entfällt auch für Steuern bis zur getrennten Besteuerung | kritik-solidarhaftung, trennung-begriff, eigenstaendig |
| 4.3 | 13692 | «Eine Art. 13 Abs. 1 DBG entsprechende Vorschrift fehlt im StHG. Folglich steht es den Kantonen frei …»; AR, AI, VD Solidarhaftung auch bei Zahlungsunfähigkeit; «Keine solidarische, sondern eine anteilsmässige Haftung kennt – soweit ersichtlich – einzig der Kanton Basel-Stadt»; Luzern: höchstens das Doppelte des Steueranteils | harmonisierung, kantone |

### Oesterhelt Stefan/Opel Andrea, Rechtsprechung 2025-2, FStR 2025 (Besprechung BGer vom 16.12.2024 = BGE 151 II 409)
- lexplorer_url (Dokument): https://app.lexplorer.ch/suche?e_id=605&e_sys=ile; doc_id `92ba09fe-6240-40f5-b624-8bd7fb30a572`; Autoren am Kopf «Stefan Oesterhelt/Andrea Opel». Abfrage 7.

| Ziff. | Chunk | tragender Satz (gekürzt) | verwendet in |
|---|---|---|---|
| 7.3 | 14612 (`cf448448-2c36-407d-9856-21cec652dd8f`), 14613 (`d765f88e-6fb1-4cfe-911f-56856a9dd8a1`) | «Das Bundesgericht schliesst sich mit seinem Urteil der herrschenden Steuerrechtslehre an, welche ebenfalls davon ausgeht, dass die Prozessführungsbefugnis diesfalls ausschliesslich dem Willensvollstrecker zusteht»; differenzierte Betrachtung der Verfahrensrechte der Erben | willensvollstrecker-verfahren |

### Rostetter Marco, Die Verjährung im Recht der direkten Bundessteuer und der harmonisierten kantonalen Steuern, IFF-Schriftenreihe 2019, § 10 Sonderfragen zur Beteiligung mehrerer Personen am Steuerrechtsverhältnis
- lexplorer_url (Segment § 10): https://app.lexplorer.ch/suche?e_id=1030&e_sys=ile; doc_id `87bfb0d3-afa7-4a63-a3d8-09d7693f22d0`; Monografie eines Autors (Chunk-Angabe «Marco Rostetter»). Abfrage 5; gelesen ganz (Slices 0–2 zu 20000).
- Randziffern: sichtbar 534, 536, 549–551, 555–558, 561, 577, 578, 582–585, 588 f.; erschlossen aus Querverweisen im Text: 537 («vgl. Rz 537»), 554 («Rz 554 ff.»), 562 und 564 (Fn. 1009, 1018), 573 («vorhin (Rz 573)»), daraus 565–572, 574–576 und 586–587 durch Abzählen der Absätze.

| Rz | Chunk | tragender Satz (gekürzt) | verwendet in |
|---|---|---|---|
| 536 | 29503 (`c2cc862e-5c0d-430f-99f7-a71d26eec61e`) | «Solidarische Mithaftung bedeutet, dass eine oder mehrere Drittpersonen für die Steuerschuld des Steuersubjekts haften, ohne in das Steuerrechtsverhältnis einzutreten» | mithaftung |
| 537 | Chunk 5 | Steuersolidarität = Verfahrens- und Zahlungssolidarität; «Ein weiteres Beispiel sind die Ehegatten für die gemeinsame Steuer» | mithaftung-verjaehrung |
| 549 f. | Chunk 12 | Unterbrechung gegenüber solidarisch Mithaftendem nur im Sonderfall des Einbezugs vor Rechtskraft; «Im Normalfall unterbricht eine Amtshandlung gegenüber diesen unbeteiligten Dritten deshalb nicht die Veranlagungsverjährung» | mithaftung-verjaehrung |
| 551 f. | Chunk 13 | Art. 120 Abs. 3 lit. b DBG «ist im Rahmen einer teleologischen Reduktion einzuschränken»; nur bei Steuersolidarität | mithaftung-verjaehrung |
| 553–557 | Chunk 14 | Stillstand nach Art. 120 Abs. 2 lit. c DBG «auf Basis einer teleologischen Reduktion … einzig auf Fälle von Steuersolidarität» anwenden; Gesetzesänderung vorgeschlagen | mithaftung-verjaehrung |
| 564 | Chunk 17 | «Jedoch bestehen zu den Mithaftenden verschiedene Forderungen mit eigenen rechtlichen Schicksalen. Mithin ist die Bezugsverjährung für jede Forderung und jeden Solidarschuldner einzeln zu beurteilen» | mithaftung-verjaehrung |
| 567 | Chunk 19 | Mithaftender «kann die Veranlagung des Steuerpflichtigen nicht anfechten»; «Der Mithaftende kann dabei die Unrichtigkeit der gegenüber dem Steuerpflichtigen bereits rechtskräftigen Veranlagung einwenden» | anfechtung |
| 570 | Chunk 20 | «Nach dem Bundesgericht unterbricht z. B. die Ausstellung eines Zahlungsbefehls gegenüber einem Mithaftenden die Verjährung gegenüber dem anderen» (2C_58/2015 E. 6) | verjaehrung |
| 573–575 | Chunk 21 | Anerkennung durch Mithaftenden unterbricht nach geltendem Recht, aber «nur im Umfang der anerkannten Solidarschuld» | mithaftung-verjaehrung |
| 587 | Chunk 27 | Verlustscheinforderung verjährt nur gegenüber dem Schuldner des Verlustscheins; «für Mithaftende richtet sich die Verjährung generell nach Art. 121 DBG» (2C_58/2015, 2C_1098/2014) | verjaehrung |

### Rajower Felix, Sicherstellung und Arrest im Recht der direkten Bundessteuer und nach zürcherischem Steuergesetz (1. Teil), FStR 2007
- lexplorer_url (Dokument): https://app.lexplorer.ch/suche?e_id=364&e_sys=ile; doc_id `5fd0bc0b-1d04-4ded-b075-aecf1552c7fc`; Autor am Kopf «Dr. iur. Felix Rajower, RA». Abfrage 5.

| Ziff. | Chunk | tragender Satz | verwendet in |
|---|---|---|---|
| 2.1 | 30818 (`63b88bf2-eb37-4a2a-afd2-a784b49eb0c2`) | Steuersicherungsmittel des DBG u.a. «die Sicherstellung der für die Vermittlungstätigkeit an Grundstücken geschuldeten Steuern (Art. 173 iVm Art. 13 Abs. 3 Bst. c und Art. 55 Abs. 3 DBG)» | liegenschaft |

### Rajower Felix, Sicherstellung und Arrest im Recht der direkten Bundessteuer und nach zürcherischem Steuergesetz (2. Teil), FStR 2007
- lexplorer_url (Dokument): https://app.lexplorer.ch/suche?e_id=524&e_sys=ile; doc_id `447acb4b-fa6d-4f74-9a5f-3c505d65081d`; Autor am Kopf «Dr. iur. Felix Rajower, RA». Abfrage 6.

| Ziff. | Chunk | tragender Satz | verwendet in |
|---|---|---|---|
| 4.4.3 | 11623 (`a040fb16-0533-45c7-87fe-47c4efcdacf5`) | «… kann gegen jeden einzelnen Ehegatten Arrest für die gesamte Steuerforderung angeordnet werden»; bei unklarer Haftungsbeschränkung (Art. 13 Abs. 1 Satz 2 DBG) Arrest gegen beide «ohne dass eine Haftungsverfügung erlassen werden muss» | sicherstellung |

### Fenners Henk/Baumgartner Heinz/Duss Pascal, Gesetzgebungs-Agenda 2026/3, FStR 2026
- lexplorer_url (Dokument): https://app.lexplorer.ch/suche?e_id=1841&e_sys=ile; doc_id `05b2fa0e-6823-4825-b623-2a9722272ed9`; Autoren am Kopf «Dr. iur. Henk Fenners/lic. iur. Heinz Baumgartner/lic. iur. Pascal Duss» (Lexplorer-Chunk nennt die Reihenfolge Baumgartner, Duss, Fenners). Abfrage 9.

| Ziff. | Chunk | tragender Satz | verwendet in |
|---|---|---|---|
| 1.3 | 66151 (`cb996e4e-7e4f-48bf-a0f1-b883bc567c03`) | «In der Referendumsabstimmung vom 8.3.2026 nahm das Stimmvolk das BG über die Individualbesteuerung mit einem Ja-Anteil von 54,26 % an … muss bis spätestens am 1.1.2032 umgesetzt sein» | ausblick |

## Gelesen, nicht verwendet
- St.Galler Seminar zum Interkantonalen Steuerrecht 2021, Interkantonale Aspekte bei der Besteuerung von Privatpersonen (Chunks 59593, 59595): Folien zur bernischen Praxis, nichts zu Art. 13 DBG.
- Brülisauer/Kriesi, FStR 2008/1 (Chunk 14769) und Seminarfolien 2019/2025 zu Personengesellschaften: betreffen Art. 10/11 DBG, nicht die Haftung nach Abs. 3 lit. b.
- Berdoz/Bugnon, La procédure mixte en matière d'impôts directs, in: Die Verfahren im Steuerrecht, 4. Aufl., IFF-Schriftenreihe 2021 (Chunk 20090): nur allgemeine Wiedergabe von Solidarhaftung und Beweislast; nicht eingebaut.
