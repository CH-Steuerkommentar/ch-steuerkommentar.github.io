# Art. 7 MWSTG (Ort der Lieferung) – Materialien, Verordnung, Verwaltungspraxis ESTV

Stand: 28.10.2026. Werkzeuge: Fedlex-MCP, Open Case Law (OCL), Lexplorer Tax (nur navigierend). Amtliche PDF aus dem Fedlex-Filestore mit `pdftotext` ausgewertet. Die **Seitenzahl** ist die gedruckte Zahl am Fuss der PDF-Seite (BBl/AS bis 2020). Bei BBl ab 2021 gilt die Seitennummer des Dokuments. Keine Websuche. Keine Rechtsprechung über Lexplorer.

**Lexplorer-Suchen verbraucht: 0 von 3.** Es wurde nur navigiert (nav_list_documents, nav_list_chunks, get_chunk_content).

---

## 1. Suchprotokoll

| Nr. | Werkzeug | Abfrage / Ziel | Ergebnis |
|---|---|---|---|
| F1 | Fedlex get_article | SR 641.20 Art. 7 (Konsolidierung 31.3.2025) | Wortlaut und Fussnoten (AS 2017 3575; BBl 2015 2615) |
| F2 | Fedlex get_article | Art. 7, Datum 2010-01-01 | kein HTML (vor 2021) → AS-PDF |
| F3 | Fedlex list_amendments | SR 641.20 seit 2024; SR 641.201 seit 2017 | MWSTG: letzte Fassung 31.3.2025. MWSTV: Fassung 1.1.2027 vorhanden (künftig) |
| F4 | Fedlex get_article / get_law_text | MWSTV Art. 3, 4, 4a, 4b, 5, 5a (Fassungen 1.1.2025 und 1.1.2027) | Art. 4b existiert nicht. Art. 3, 4a unverändert 2027 |
| F5 | Fedlex get_article | MWSTG Art. 20a | BG vom 16.6.2023, AS 2024 438, in Kraft 1.1.2025 |
| O1 | OCL get_article_purpose | SR 641.20 Art. 7 | nur BBl 2015 2615 (S. 2629 f.) verknüpft |
| O2 | OCL get_materialien | MWSTG Art. 7 | BBl 2015 2615. 14 Vernehmlassungen, u.a. proj/2025/41 (5.12.2025) und proj/2006/125 (2007). Keine parlamentarischen Änderungen erfasst |
| O3 | OCL search_botschaft | `"Ort der Lieferung" Elektrizität Erdgas Betriebsstätte` (2008) | BBl 2008 6885 (PDF-S. 45, 60, 105) |
| O4 | OCL search_botschaft | `"Elektrizität in Leitungen" Erdgas Ort Lieferung` (2008–2009) | BBl 2008 6885 S. 6989. E-MWSTV 2009 (proj/6009/79) |
| O5 | OCL search_botschaft | `"Ort der Lieferung" Mehrwertsteuer Dettling` (bis 1999) sowie zwei Folgeabfragen | Bericht WAK-N, BBl 1996 V 713 (nur OCR) |
| O6 | OCL search_decisions / get_erwaegung | `"Art. 12 MWSTV" "Ort der Lieferung"`; 2A.557/1999 E. 3 | **Korrektur:** Der Ort der Lieferung stand in **Art. 11 MWSTV 1994**, nicht in Art. 12 (Art. 12 MWSTV = Ort der Dienstleistung) |
| O7 | OCL search_botschaft | `"Art. 7 Abs. 3" Versandhandel Plattform` (ab 2020) | BBl 2021 2363. Erläuternder Bericht VE 2025 |
| O8 | OCL search_botschaft | `"Art. 4a" Versandhandel …` (ab 2017); `Versandhandel Folgemonat …` (2016–2019) | VE-MWSTV 2016 (proj/6016/62) und VE-MWSTV 2023 (proj/2023/40) |
| O9 | OCL search_botschaft | Plattformbesteuerung … (Botschaft 2026) | keine Botschaft zur VE 2025 gefunden |
| P1 | OCL search_practice | `"Ort der Lieferung" OR "Ort der Leistungserbringung"` (estv_mwst, de) | 28 Dokumente: MI 06, MI 22, MBI 07, MBI 27 u.a. |
| P2 | OCL get_practice | MI 06 `estv_mwst_de_1016479`; MI 22 `estv_mwst_de_1551451`; MBI 07 `estv_mwst_de_1029216`; MBI 27 `estv_mwst_de_1150270`; MI 04 `estv_mwst_de_1003047`; MBI 05 `estv_mwst_de_1002229` | Volltexte gelesen bzw. durchsucht |
| P3 | OCL search_practice | `Versandhandel OR Kleinsendungen OR "Art. 7 Abs. 3"`; `Versandhandel` (include_superseded) | **Eine MWST-Info «Online-Versandhandel» gibt es nicht.** Die Versandhandelsregelung steht in MI 06 Ziff. 2.6 und Teil IV. MI 22 heisst «Ausländische Unternehmen» (Stand 17.4.2025) |
| P4 | OCL search_practice | `Ladestation "Art. 7 Abs. 2"` | MBI 05 Ziff. 13.4 |
| L1 | Lexplorer nav_list_documents | Quelle `03033b33-…` | doc-IDs MI 06, MI 22, MBI 05, MBI 07, MBI 27 |
| L2 | Lexplorer nav_list_chunks und get_chunk_content | MI 06, MBI 07, MI 22, MBI 27, MBI 05 (Inhaltsverzeichnisse und einschlägige Chunks) | Ziffern festgestellt (siehe Teil 4) |
| D | curl Fedlex-Filestore und pdftotext | BBl 2008 6885 (fga/2008/1202), BBl 2008 7133 (fga/2008/1203), AS 2009 5203 (oc/2009/615), AS 2000 1300 (oc/2000/212), BBl 2015 2615 (fga/2015/540), BBl 2015 2681 (fga/2015/541), AS 2017 3575 (oc/2017/396), BBl 2021 2363, AS 2009 6743 (oc/2009/828), MWSTV-Konsolidierungen 1.1.2025 und 1.1.2027 (cc/2009/828), Erl. Bericht 2007 (proj/6006/125 doc_1), VE-MWSTV 2009 (proj/6009/79 doc_2), VE-MWSTV 2016 (proj/6016/62 doc_2), VE-MWSTV 2023 (proj/2023/40 doc_1, doc_3), VE-MWSTG 2025 (proj/2025/41 doc_1, doc_2), VE 2026 (proj/2026/5), VE 2025/43, VE 2026/23 | gelesen |

Nicht auffindbar: MWSTV 1994 (AS 1994 1464) als PDF im Filestore (der Abruf lieferte HTML). Der Wortlaut von Art. 11 MWSTV 1994 stammt deshalb nur aus BGer 2A.557/1999 E. 3. Ebenfalls nicht auffindbar war der Bericht WAK-N 1996 als PDF; vorhanden sind nur OCL-OCR-Snippets.

---

## 2. Entstehungsgeschichte

### 2.1 Vorgängernormen

**Art. 11 MWSTV vom 22.6.1994 (AS 1994 1464)**
- Nur mittelbar belegt über [BGer 2A.557/1999 vom 10. November 2000, E. 3](https://mcp.opencaselaw.ch/entscheid/bger_2A.557_1999#e-3): «Für den Ort der Lieferung trifft Art. 11 MWSTV folgende Regelung: Die Lieferung wird erbracht: a. am Ort, wo sich der Gegenstand im Zeitpunkt der Verschaffung der Befähigung, über ihn wirtschaftlich zu verfügen, der Ablieferung oder der Überlassung zum Gebrauch oder zur Nutzung befindet; b. am Ort, wo die Beförderung oder Versendung des Gegenstandes zum Abnehmer (oder in dessen Auftrag zu einem Dritten) beginnt.»
- **Hinweis zum Auftrag:** Art. 12 MWSTV 1994 regelte den Ort der *Dienstleistung*. Das zeigt die Regeste von BGE 133 II 153 («Art. 12 … MWSTV … Ort der Dienstleistung unter der Herrschaft der MWSTV»).

**Bericht WAK-N vom 28.8.1996 zur Pa.Iv. Dettling (BBl 1996 V 713)**
- Nur OCR-Text aus OCL. Die Seitenangaben sind OCL-Seitenindizes; die gedruckte Seite ist nicht am Scan geprüft.
- Index S. 26 f., zu «Art. 12 Ort der Lieferung (Art. 11)», d.h. E-MWSTG 1996 Art. 12 entspricht Art. 11 MWSTV: «Lieferort ist demnach jener Ort, wo der Abnehmer den Gegenstand vom Lieferer selbst in Empfang nimmt oder von einem Dritten in Empfang nehmen lässt …». Ferner: «Eine Versendung liegt vor, wenn der Lieferer die Beförderung des Gegenstandes durch einen selbständigen Beauftragten ausführen oder besorgen lässt …»
- Index S. 103 (Ziff. 42): «Die Bestimmungen über den Ort der Lieferung stimmen inhaltlich mit Artikel 8 Absatz 1 Buchstaben a und b der 6. EU-Richtlinie überein.»

**Art. 13 aMWSTG vom 2.9.1999 «Ort der Lieferung» (AS 2000 1300, Art. 13 auf S. 1304; PDF oc/2000/212)**
- Wortlaut: «Als Ort einer Lieferung gilt der Ort, wo: a. sich der Gegenstand zum Zeitpunkt der Verschaffung der Befähigung, über ihn wirtschaftlich zu verfügen, der Ablieferung oder der Überlassung zum Gebrauch oder zur Nutzung befindet; b. die Beförderung oder Versendung des Gegenstandes zum Abnehmer oder in dessen Auftrag zu einem Dritten beginnt.»
- Steht im Abschnitt «2. Abschnitt: Ort des steuerbaren Umsatzes». Eine Sonderregel für Energie gab es nicht.

### 2.2 Totalrevision 2009

**Erläuternder Bericht zur Vernehmlassung vom 14.2.2007 (proj/6006/125 doc_1)**
- S. 63, Art. 4 VE «Ort der Lieferung»: «Dieser Artikel regelt den Ort der Lieferung von Gegenständen und entspricht vollumfänglich Artikel 13 MWSTG.»
- S. 201: «Die Bestimmungen über den Ort der Lieferung stimmen inhaltlich mit Artikel 8 Absatz 1 Buchstaben a und b der 6. EG-Richtlinie überein.»
- **Ziff. 6.11 «Änderung der Besteuerung von Elektrizität und Gas»** (Reformmöglichkeit; Ursprung von Abs. 2):
  - S. 260 (6.11.1): «Der Ort der Lieferungen von Gas und Elektrizität bestimmt sich auch dann nach den Regeln über den Ort der Lieferung (Artikel 13 MWSTG), wenn solche Umsätze grenzüberschreitend erbracht werden. Soweit es sich um grenzüberschreitend getätigte Lieferungen von Elektrizität handelt, sieht die Praxis heute für die Besteuerung solcher Umsätze eine Sonderregelung vor (vgl. Merkblatt Nr. 22 der ESTV …).»
  - S. 260 (6.11.2): Verweis auf «Richtlinie 2003/92/EG» vom 7.10.2003 (ABl. L 260 vom 11.10.2003, S. 8 f.).
  - S. 260 (6.11.2.1): «… wäre jedoch entsprechend dem geänderten EG-Richtlinienrecht im Mehrwertsteuergesetz festzuhalten, dass die Besteuerung der Umsätze von Gas und Elektrizität am Ort des Empfängers der Leistung erfolgt (sog. Empfängerortsprinzip …). Ist der Empfänger … im Ausland ansässig, handelt es sich damit um einen Auslandumsatz …»
  - S. 262: «… die ausländischen Lieferanten von Gas oder Elektrizität müssten sich im Inland als steuerpflichtige Personen eintragen lassen. Eine Eintragung … wäre jedoch nur für jene Fälle vorgesehen, bei denen er einen nichtsteuerpflichtigen (inländischen) Abnehmer mit Gas oder Elektrizität beliefert und der Ort des Verbrauchs im Inland liegt.»

**Botschaft zur Vereinfachung der Mehrwertsteuer vom 25.6.2008 (BBl 2008 6885; PDF fga/2008/1202)**
- S. 6929, Ziff. 1.7.4.4 «Ort der Leistung» (Vergleich mit dem EU-Recht): «Soweit der gelieferte Gegenstand vom Lieferer oder der Liefererin weder befördert noch versandt wird, gilt als Lieferort derjenige Ort, wo sich der Gegenstand im Zeitpunkt der Verschaffung der Verfügungsmacht, der Ablieferung oder der Überlassung zum Gebrauch oder zur Nutzung befindet (Art. 7 Abs. 1 Bst. a E-MWSTG). … Die Bestimmungen über den Ort der Lieferung stimmen inhaltlich mit den Artikeln 31 und 32 MwStSystRL überein.»
- S. 6944, zu Art. 7 E-MWSTG: «Die Bestimmungen des Leistungsortes in den Artikeln 7 und 8 E-MWSTG dienen der territorialen Abgrenzung des Geltungsbereichs des Mehrwertsteuergesetzes und begrenzen somit die Steuerhoheit. Sie gehören deshalb zu den allgemeinen Bestimmungen. Der Ort der Lieferung von Gegenständen entspricht vollumfänglich Artikel 13 MWSTG.»
  - **Befund:** Zum neuen Abs. 2 (Elektrizität und Erdgas) schweigt die Botschaft bei Art. 7, obwohl der Entwurf ihn enthält. Er wird nur bei Art. 52 erwähnt.
- S. 6989, zu Art. 52 E-MWSTG: «Die Steuerbefreiung von Elektrizität und Erdgas in Leitungen wurde in Absatz 1 Ziffer 7 als Folge des neuen Orts der Lieferung bei Elektrizität und Erdgas in Leitungen und in Angleichung ans EU-Recht aufgenommen.»
- E-MWSTG (BBl 2008 7133, Art. 7 auf S. 7135): Abs. 1 wie heute. Abs. 2: «Als Ort der Lieferung von Elektrizität und Erdgas in Leitungen gilt der Ort, an dem der Empfänger oder die Empfängerin der Lieferung den Sitz der wirtschaftlichen Tätigkeit oder eine Betriebsstätte hat, für welche die Lieferung erbracht wird, oder in Ermangelung eines solchen Sitzes oder einer solchen Betriebsstätte der Wohnort oder der Ort, von dem aus er oder sie tätig wird.»
- Art. 52 Abs. 1 Ziff. 7 E-MWSTG (S. 7159): «Elektrizität und Erdgas in Leitungen».

**MWSTG vom 12.6.2009 (AS 2009 5203; Art. 7 Abs. 1 auf S. 5205, Abs. 2 auf S. 5206)**
- In Kraft 1.1.2010. Der Wortlaut entspricht dem Entwurf 2008 unverändert (Vergleich von BBl 2008 7135 mit AS 2009 5205 f.). Damit sind für 2009 keine parlamentarischen Änderungen an Art. 7 ersichtlich.
- Art. 53 Abs. 1 Bst. g (AS 2009 5230): «Elektrizität und Erdgas in Leitungen».

### 2.3 Teilrevision 2016 (Abs. 2 neu gefasst, Abs. 3 eingefügt)

**Erläuternder Bericht zur Vernehmlassung (proj/2013/128, Eröffnung 6.6.2014; doc_2, OCL-Seiten 12 f.)**
- Der Text ist weitgehend identisch mit der Botschaft. Zusätzlich zu Abs. 2: «Diese Regelung ist subsidiär. … Unerheblich ist dabei, ob die physische Energielieferung tatsächlich an diesen Sitz oder diese Betriebsstätte erfolgt und ob die Energie dort genutzt oder verbraucht wird. Einzige Voraussetzung ist, dass die Lieferung für den fraglichen Sitz oder die fragliche Betriebsstätte erbracht wird. Wie bei der Lieferung von Waren ist stets zwischen der Lieferung im mehrwertsteuerlichen Sinn (dem Leistungsverhältnis) und der tatsächlichen Lieferung im Sinn einer Warenbewegung – oder vorliegend einer Energieübertragung – zu unterscheiden.»
- Diese Sätze fehlen in der Botschaft.

**Botschaft zur Teilrevision des MWSTG vom 25.2.2015 (BBl 2015 2615; PDF fga/2015/540)**
- S. 2616 (Übersicht): «Ausländische Online-Händlerinnen und -Händler werden abhängig von ihrem Umsatz im Inland obligatorisch steuerpflichtig.»
- S. 2620: «Ausländische Online-Händlerinnen und -Händler werden ab einem Umsatz im Inland von 100 000 Franken pro Jahr obligatorisch steuerpflichtig (Art. 7 Abs. 3 E-MWSTG).»
- S. 2621 (Vernehmlassung): «Praktisch sämtliche Massnahmen, die zugunsten der inländischen Unternehmen den Abbau mehrwertsteuerbedingter Wettbewerbsverzerrungen zum Ziel haben (vgl. Art. 7 Abs. 3 und Art. 10 Abs. 2 E-MWSTG), wurden durchwegs positiv aufgenommen, auch wenn einige kritische Stimmen an der Wirksamkeit der Massnahmen zweifeln.»
- S. 2626 (Rechtsvergleich): «Mit der Steuerpflicht für ausländische Online-Händlerinnen und -Händler, die mit dem einfuhrsteuerfreien Versand von Paketen an Endkonsumentinnen und -konsumenten im Inland jährlich mehr als 100 000 Franken Umsatz erzielen, kommt der Schweiz eine Pionierrolle zu, die insbesondere von der OECD mit Interesse verfolgt wird.»
- **S. 2629, zu Abs. 2:**
  - «Diese Änderung entspricht der geltenden Praxis. Die bisherige Formulierung war im Wortlaut zu eng, da mit dem ‹Wohnort oder dem Ort, von dem aus er oder sie tätig wird› diejenigen Fälle nicht abgedeckt sind, wo weder ein Wohnort gegeben ist noch ein Ort, von dem aus eine Tätigkeit ausgeübt wird, wie dies beispielsweise bei Ferienwohnungen der Fall ist. Neu wird generell auf den Ort abgestellt, an dem die Energielieferung tatsächlich genutzt oder verbraucht wird. Aufgrund teleologischer Auslegung wurde das in der bisherigen Praxis bereits so gehandhabt.»
  - «Keine Änderung erfolgt bezüglich des Orts der Energielieferung an Unternehmen mit Sitz oder Betriebstätte im Inland. Ergänzt wurde, dass diese Bestimmung auch für die Lieferung von Fernwärme gilt. Zudem wurde der zu enge Begriff Erdgas durch Gas ersetzt, damit nicht andere Formen von Gas wie beispielsweise Biogas willkürlich nicht erfasst sind. Es muss sich aber um Gas handeln, das anstelle von Erdgas verwendet wird und deshalb über das Erdgasverteilnetz geliefert wird. Eine vergleichbare Einschränkung findet sich auch in der europäischen Mehrwertsteuersystem-Richtlinie.»
- **S. 2629, zu Abs. 3 Bst. a:**
  - «Die sogenannte Unterstellungserklärung war bisher bloss in Artikel 3 MWSTV geregelt. Durch diese Ergänzung werden die Grundzüge der Unterstellungserklärung im Gesetz selbst genannt, die Details verbleiben auf Verordnungsstufe. Ausländische und inländische Unternehmen, die eine Bewilligung der ESTV haben, können Einfuhren in eigenem Namen vornehmen. Diesfalls sind sie selbst Importeur oder Importeurin und nicht der Lieferungsempfänger oder die Lieferungsempfängerin im Inland. Dies setzt voraus, dass diese Unternehmen im Inland steuerpflichtig sind und sie die Lieferungen ihrerseits mit Mehrwertsteuer weiterfakturieren.»
  - «Neu wird präzisiert, dass der Verzicht im Zeitpunkt der Einfuhr bekanntgegeben werden muss. Denn laut Zollrecht sind allein die Rechtsverhältnisse im Zeitpunkt der Einfuhr für die Bestimmung der importierenden Person und die Veranlagung der Einfuhrsteuer massgebend.»
- **S. 2629 f., zu Abs. 3 Bst. b:**
  - S. 2629: «Gegenstände, bei deren Einfuhr ins Inland ein Steuerbetrag von maximal 5 Franken anfällt (Art. 53 Abs. 1 Bst. a MWSTG i.V.m. Art. 1 Bst. c der Verordnung des EFD vom 2. April 2014 …), können abgabenfrei eingeführt werden. … bei Gütern, die zum Normalsatz von 8 Prozent besteuert werden bis zu einem Preis (inklusive Versandkosten) von 62,50 Franken. Dies führt zu erheblichen Wettbewerbsnachteilen für die inländischen Unternehmen. Um diese mehrwertsteuerbedingten Wettbewerbsverzerrungen weitgehend zu eliminieren, sollen deshalb Unternehmen, die in einem erheblichen Umfang solche Umsätze erzielen, diese Lieferungen im Inland versteuern müssen.»
  - S. 2630: «Dies geschieht durch die Verlagerung des Ortes der Lieferungen ins Inland. Dadurch erbringen solche Unternehmen Leistungen im Inland und werden wie ein inländisches Unternehmen grundsätzlich steuerpflichtig. Die Verlagerung des Leistungsortes ins Inland findet nur Anwendung auf Einfuhren, denen eine Lieferung mit Warenbewegung zugrunde liegt. … Folglich fällt die Abhollieferung nicht unter diese Regelung. Ebenfalls nicht betroffen ist die steuerfreie Einfuhr im Reiseverkehr … Die steuerfreie Einfuhr von Geschenksendungen fällt schon deshalb nicht unter diese Bestimmung, weil bei Geschenksendungen die Beteiligten Privatpersonen sein müssen.»
  - S. 2630: «Wettbewerbsverzerrungen treten in erster Linie bei Lieferungen an nicht steuerpflichtige Personen auf. Es wird aber darauf verzichtet, nur diesen Sachverhalt zu erfassen. Das ausländische Unternehmen muss somit nicht abklären, ob der Empfänger oder die Empfängerin steuerpflichtig ist. Details wie der Zeitpunkt, in dem sich der Leistungsort ins Inland verlagert, werden vom Bundesrat in der MWSTV geregelt.»
- S. 2658, zu Art. 53 Abs. 1 Bst. g: «Die bereits vorhandene Steuerbefreiung bei der Einfuhr von Elektrizität und Gas in Erdgasleitungen wird konsequenterweise auch auf Fernwärme ausgeweitet (vgl. Erläuterungen zu Art. 7 Abs. 2 E-MWSTG). Diese Lieferungen werden nach Artikel 7 Absatz 2 E-MWSTG im Inland besteuert.»
- S. 2673 (finanzielle Auswirkungen): «Wegen Unterschreitens des Mindeststeuerbetrags von 5 Franken von der Einfuhrsteuer befreite Sendungen an inländische Kunden und Kundinnen sollen ab einem jährlichen Umsatz von 100 000 Franken aus solchen Sendungen der Inlandsteuer unterstellt werden (vgl. Ziff. 2, Erläuterungen zu Art. 7 Abs. 3 Bst. b). Dies dürfte jährliche Mehreinnahmen von mindestens 20 Millionen Franken zur Folge haben.»
- S. 2678 (Ziff. 5.2): Die Richtlinie gilt in der Schweiz nicht; die Schweiz «kann ihr Mehrwertsteuerrecht weiterhin autonom gestalten». Die WTO-Vereinbarkeit wird nur zu Art. 10 E-MWSTG begründet.

**Entwurf 2015 (BBl 2015 2681, Art. 7 auf S. 2682) im Vergleich zum Gesetz (AS 2017 3575, Art. 7 auf S. 3576)**

Die Änderungen im parlamentarischen Verfahren sind nur durch diesen Textvergleich belegt. Die Ratsprotokolle waren über die Werkzeuge nicht greifbar.
- Abs. 2: Der Entwurf lautete «Gas **in Erdgasleitungen**», das Gesetz lautet «Gas **über das Erdgasverteilnetz**».
- Abs. 3 Bst. b: Der Entwurf lautete «Lieferungen nach Absatz 1 Buchstabe b erbringt», das Gesetz lautet «… nach Absatz 1 Buchstabe b **des vorliegenden Artikels** erbringt» (redaktionell).
- Abs. 3 Bst. a: unverändert gegenüber dem Entwurf.

**Inkrafttreten (AS 2017 3575, S. 3590)**
- «2 Es wird mit Ausnahme der Bestimmung im nachstehenden Absatz 3, auf den 1. Januar 2018 in Kraft gesetzt. 3 Artikel 7 Absatz 3 Buchstabe b (Ziff. I) wird auf den 1. Januar 2019 in Kraft gesetzt.»
- Bundesratsbeschluss vom 2.6.2017, gefällt am 26.5.2017 im vereinfachten Verfahren (Fn. 15). Referendumsfrist unbenützt abgelaufen am 19.1.2017.
- Das Gesetz selbst überliess das Inkrafttreten dem Bundesrat (Ziff. V Abs. 2). Die Staffelung ist also ein Entscheid des Bundesrates, nicht des Parlaments. Eine Begründung fand sich in den greifbaren Materialien nicht.

### 2.4 Spätere Revisionen und hängige Vorlagen

**MWSTG-Revision 2023 (BG vom 16.6.2023, AS 2024 438; Botschaft BBl 2021 2363)**
- Sie änderte Art. 7 nicht; die Fedlex-Fussnoten zu Art. 7 nennen nur AS 2017 3575. Sie führte aber Art. 20a (Plattformbesteuerung) ein, in Kraft seit 1.1.2025.
- BBl 2021 2363, S. 8: «Trotz der Einführung der Versandhandelsregelung (Art. 7 Abs. 3 Bst. b …) per 1. Januar 2019 bleibt ein beachtlicher Teil des Konsums unbesteuert, denn es ist davon auszugehen, dass sich nicht alle ausländischen Versandhandelsunternehmen, die die Voraussetzungen für die Steuerpflicht erfüllen, auch wirklich haben eintragen lassen.»
- S. 34: «… nur 350 Versandhandelsunternehmen bei der ESTV registriert (Stand: Anfang August 2021). Zum anderen ist davon auszugehen, dass viele Anbieter und Anbieterinnen weniger als 100 000 Franken Umsatz aus Versandhandelslieferungen in die Schweiz erzielen …»
- S. 43: «Stammen die im Inland gelieferten Gegenstände aus dem Ausland, so gilt die Lieferung im Inland als von der Plattform erbracht, wenn diese mit der Lieferung von einfuhrsteuerbefreiten Kleinsendungen mindestens 100 000 Franken pro Jahr erzielt (Art. 7 Abs. 3 Bst. b MWSTG; Versandhandelsregelung). In diesem Fall wird die Plattform steuerpflichtig. Wo sie ansässig ist, ist dabei unerheblich.»

**Hängig: Vernehmlassungsvorlage vom 5.12.2025 (proj/2025/41)**
- Die Vernehmlassung ist abgeschlossen; der Ergebnisbericht steht laut OCL aus. Eine Botschaft war im OCL-Bestand nicht auffindbar.
- **Neuer Art. 7 Abs. 4 VE-MWSTG** (Vorlage doc_1, S. 1): «Liefert der Verkäufer oder die Verkäuferin den Gegenstand an eine Person, die nach Artikel 20a Absatz 1 als Leistungserbringerin gilt, so bleibt der Ort dieser Lieferung in Abweichung von Absatz 3 Buchstabe b im Ausland.»
- Erläuternder Bericht (doc_2), S. 15: «Absatz 4 soll klarstellen, dass sich der Leistungsort bei Leistungen der Verkäuferinnen und Verkäufer an eine Plattform im Sinne von Artikel 20a nicht ins Inland verlagert. Diese Klarstellung ist notwendig, weil es Sinn und Zweck der Plattformbesteuerung ist, dass sich Unternehmen mit Sitz im Ausland, die ihre Leistungen ausschliesslich über Plattformen erbringen, in der Schweiz nicht mehrwertsteuerpflichtig werden. Ihre Leistungen werden in der Schweiz gebündelt von der Plattform besteuert.»
- Zusätzlich soll Art. 79a totalrevidiert werden (Netzsperre als erste Stufe; gilt für Lieferungen «nach Artikel 7 Absatz 3 Buchstabe b»). Erl. Bericht S. 19 f.: «An den materiellen Voraussetzungen sollen sich keine Änderungen zum geltenden Recht ergeben.»

**Nicht betroffen:**
- Vernehmlassung vom 19.6.2026 (proj/2026/5, «Wettbewerbsfähigkeit»): Die Treffer zu «Art. 7» betreffen nur Art. 7 StG.
- Vernehmlassungen proj/2025/43 und proj/2026/23 (MWST-Erhöhung für Rüstungsausgaben): ohne Treffer zu Art. 7.

---

## 3. Verordnung (MWSTV, SR 641.201)

Fedlex-Konsolidierung 1.1.2025. Die Fassung 1.1.2027 ist für Art. 3, 4a und 77 unverändert; ein Textvergleich der PDF zeigt nur redaktionelle Differenzen.

| Artikel | Verweis | Wortlaut (Kern) | Fassung / Inkrafttreten |
|---|---|---|---|
| **Art. 3** «Unterstellungserklärung bei Einfuhr eines Gegenstands» | (Art. 7 Abs. 3 Bst. a MWSTG) | Abs. 1: aufgehoben. «2 Wird die Einfuhr aufgrund der Unterstellungserklärung im eigenen Namen vorgenommen, so gelten bei Reihengeschäften die vorangehenden Lieferungen als im Ausland und die nachfolgenden als im Inland ausgeführt. 3 Verzichtet der Leistungserbringer oder die Leistungserbringerin darauf, die Einfuhr im eigenen Namen vorzunehmen, so muss er oder sie auf der Rechnung an den Abnehmer oder die Abnehmerin darauf hinweisen.» | Ursprünglich AS 2009 6743 (Verweis damals: Art. 7 Abs. 1 MWSTG). Abs. 1 lautete: «Bei der Lieferung eines Gegenstands vom Ausland ins Inland gilt der Ort der Lieferung als im Inland gelegen, wenn der Leistungserbringer … im Zeitpunkt der Einfuhr über eine Bewilligung der … (ESTV) verfügt, die Einfuhr im eigenen Namen vorzunehmen (Unterstellungserklärung).» Abs. 1 aufgehoben und Abs. 3 neu gefasst durch V vom 18.10.2017, AS 2017 6307, in Kraft 1.1.2018 |
| **Art. 4** «Lieferung eines aus dem Ausland ins Inland verbrachten Gegenstands ab Lager im Inland» | (Art. 7 Abs. 1 MWSTG) | «Bei Gegenständen, die aus dem Ausland in ein Lager im Inland verbracht und ab diesem Lager geliefert werden, liegt der Ort der Lieferung im Ausland, wenn der Lieferungsempfänger oder die Lieferungsempfängerin und das zu entrichtende Entgelt beim Verbringen der Gegenstände ins Inland feststehen und sich die Gegenstände im Zeitpunkt der Lieferung im zollrechtlich freien Verkehr befinden.» | Fassung V vom 30.10.2013, AS 2013 3839, in Kraft 1.1.2014. Die Urfassung 2009 begann mit «Bei Lieferungen von Gegenständen, die …». Laut Erl. 2016 wurde 2017 nur der französische und italienische Text geändert |
| **Art. 4a** «Zeitpunkt des Übergangs des Lieferungsortes beim Versandhandel» | (Art. 7 Abs. 3 Bst. b MWSTG) | «1 … so gilt der Ort der Lieferung bis zum Ende desjenigen Monats als im Ausland gelegen, in dem der Leistungserbringer … die Umsatzgrenze von 100 000 Franken aus solchen Lieferungen erreicht hat. 2 Ab dem Folgemonat gilt der Ort der Lieferung für alle Lieferungen … vom Ausland ins Inland als im Inland gelegen. Ab diesem Zeitpunkt muss er oder sie die Einfuhr im eigenen Namen vornehmen. 3 Der Ort der Lieferung bleibt bis zum Ende desjenigen Kalenderjahres im Inland gelegen, in dem … die Umsatzgrenze … unterschreitet. 4 Unterschreitet [er/sie] die Umsatzgrenze und teilt … dies der … (ESTV) nicht schriftlich mit, so gilt er oder sie als unterstellt nach Artikel 7 Absatz 3 Buchstabe a MWSTG.» | Eingefügt durch V vom 15.8.2018, AS 2018 3143, in Kraft 1.1.2019. Abs. 4 neu gefasst durch V vom 21.8.2024, AS 2024 485, in Kraft 1.1.2025; laut Erl. Bericht vom 25.10.2023, S. 5, wurde nur die Abkürzung ESTV eingeführt |
| **Art. 5** «Betriebsstätte» | (Art. 7 Abs. 2, 8 und 10 Abs. 3 MWSTG) | «1 Als Betriebsstätte gilt eine feste Geschäftseinrichtung, durch welche die Tätigkeit eines Unternehmens ganz oder teilweise ausgeübt wird.» Abs. 2: Positivliste. Abs. 3: Negativliste, u.a. «a. reine Auslieferungslager» | Urfassung 2009 |
| Art. 77 Abs. 2 Bst. f | (Art. 37 MWSTG) | Die Saldosteuersatzmethode ist ausgeschlossen für Personen, die «gestützt auf Artikel 7 Absatz 3 MWSTG Lieferungen im Inland erbringen» | V vom 15.8.2018, AS 2018 3143, in Kraft 1.1.2019 |
| Art. 111b | (Art. 51 MWSTG) | «Das Versandhandelsunternehmen kann bei der Einfuhr von Gegenständen mit dem Leistungserbringer oder der Leistungserbringerin nach Artikel 20a MWSTG vereinbaren, dass es die Einfuhr im eigenen Namen vornimmt, sofern es mindestens eine der beiden Bedingungen von Artikel 7 Absatz 3 MWSTG erfüllt.» | V vom 21.8.2024, AS 2024 485, in Kraft 1.1.2025 |
| Art. 166b | Übergangsbestimmung (Art. 7 Abs. 3 Bst. b MWSTG) | Die Steuerpflicht beginnt mit Inkrafttreten der Änderung vom 15.8.2018, wenn in den vorangegangenen 12 Monaten mindestens 100 000 Franken Umsatz mit solchen Lieferungen erzielt wurden und solche Lieferungen auch künftig anzunehmen sind | AS 2018 3143, in Kraft 1.1.2019 |

Es gibt **kein Art. 4b MWSTV** (Fedlex: «Article 4b not found»).

**Verordnungsmaterialien**
- **Erläuterungen E-MWSTV 2009** (Vernehmlassung proj/6009/79 doc_2), zum damaligen Art. 4 E-MWSTV (= Art. 3 MWSTV):
  - S. 2: «Nach dieser Bestimmung ist beim Vorliegen einer Unterstellungserklärung die Abgrenzung zwischen einer Abhollieferung und einer Beförderungs- oder Versandlieferung nicht mehr notwendig. Heute hat die Unterstellungserklärung nämlich bei Abhollieferungen keine Wirkung, was die Vertragsfreiheit der Leistungserbringer einschränkt.»
  - S. 3: «Alle Lieferungen, die der Einfuhr vorausgehen, haben ihren Lieferungsort im Ausland …»
  - Zu Art. 5 E-MWSTV (= Art. 4), S. 3: «Dieser Grundsatz ist unabdingbar für die Rechtssicherheit aller Beteiligten.»
  - **Spannung zur heutigen Praxis:** MI 06 Ziff. 2.4 erklärt die Unterstellungserklärung bei Abhollieferungen für unmöglich.
- **Erläuternder Bericht VE-MWSTV 2016** (proj/6016/62 doc_2), S. 2:
  - Zu Art. 3: «Der bisherige Absatz 1 kann aufgehoben werden, weil sein Regelungsgehalt mit Artikel 7 Absatz 3 Buchstabe a revMWSTG neu auf Gesetzesstufe gehoben worden ist. … Liegt im Zeitpunkt der Einfuhr im Einzelfall noch keine Rechnung vor, kann der Verzicht auf die Anwendung der Unterstellungserklärung auch mit einem anderen Wertnachweis für die Zollveranlagung vorgenommen werden.»
  - Zu Art. 4a: «Die Umsatzgrenze von 100 000 Franken … gilt auch für Unternehmen, die bereits gestützt auf Artikel 10 revMWSTG … eingetragen sind … Auch bereits aufgrund Artikel 10 revMWSTG steuerpflichtige Unternehmen müssen keine Um- oder Hochrechnung der Umsätze aus Lieferungen von Kleinsendungen vornehmen. Nach Artikel 7 Absatz 3 Buchstabe b revMWSTG ist es nicht möglich, sich bereits vor Erreichen der massgebenden Umsatzgrenze für solche Lieferungen im Register der Steuerpflichtigen eintragen zu lassen.»
  - S. 3, zu Abs. 2: Die Verlagerung gilt «generell für sämtliche Lieferungen dieses Unternehmens vom Ausland ins Inland … Andernfalls käme es zu einer doppelten Steuerbelastung des inländischen Lieferungsempfängers».
  - **Achtung:** Der VE 2016 sah noch einen sofortigen Übergang und einen Verzicht nur auf Ende der Steuerperiode vor. Die Endfassung vom 15.8.2018 (Monatsende-Regel, Kalenderjahr) weicht davon ab. Erläuterungen zur Endfassung 2018 waren im Fedlex-Bestand nicht greifbar.

---

## 4. Verwaltungspraxis ESTV

Grundlage: OCL-Volltext. Ziffern und Chunk-IDs wurden in Lexplorer Tax am Dokument festgestellt.

### 4.1 MWST-Info 06 «Ort der Leistungserbringung»
- OCL `estv_mwst_de_1016479` (Datum OCL 15.1.2021, mit späteren Praxisänderungen bis 29.4.2025).
- Lexplorer doc `feb67ec1-f25e-4c10-925d-83f6b6f2e0ef`, https://mcp-tax.lexplorer.ch/s/doc/feb67ec1-f25e-4c10-925d-83f6b6f2e0ef
- Gliederung laut Inhaltsverzeichnis (Chunk `4e4a7d31-ffae-475b-94c5-f37b445d1915`):
  - Teil II Lieferungen: Ziff. 1 Begriff; Ziff. 2 Ort (2.1–2.6); Ziff. 3 Werkvertragliche Lieferungen; Ziff. 4 Mehrere Lieferanten; Ziff. 5 Kommission; Ziff. 6 Auslieferungs- und Konsignationslager; Ziff. 7 Veredelung; Ziff. 8 Vermietung und Leasing
  - Teil IV Versandhandel

| Sachfrage | Ziff. | Kernsatz (wörtlich) | Chunk / Link |
|---|---|---|---|
| Schema, Grundsatz | Teil II Ziff. 2 | «Nur die im Inland erbrachten Lieferungen unterliegen der Inland- oder Bezugsteuer. Lieferungen im Ausland unterliegen nicht der schweizerischen MWST.» | `06641131-f4d4-4cae-8711-639a56cae325` · https://mcp-tax.lexplorer.ch/s/doc/feb67ec1-f25e-4c10-925d-83f6b6f2e0ef?chunk=06641131-f4d4-4cae-8711-639a56cae325 |
| Energie (Abs. 2) | Teil II Ziff. 2.1 «Empfängerort» | «Als Ort der Lieferung von Elektrizität in Leitungen, Gas über das Erdgasverteilnetz und Fernwärme gilt der Ort, an dem der Empfänger der Lieferung den Sitz seiner wirtschaftlichen Tätigkeit oder eine Betriebsstätte hat, … oder in Ermangelung … der Ort, an dem die Elektrizität, das Gas oder die Fernwärme tatsächlich genutzt oder verbraucht wird (Art. 7 Abs. 2 MWSTG).» | `70c304c1-47db-45b8-9f73-89db5273d120` · https://mcp-tax.lexplorer.ch/s/doc/feb67ec1-f25e-4c10-925d-83f6b6f2e0ef?chunk=70c304c1-47db-45b8-9f73-89db5273d120 |
| Abhollieferung (Abs. 1 Bst. a) | Teil II Ziff. 2.2 | «Als Ort der Lieferung eines Gegenstandes, den ein Abnehmer oder in dessen Auftrag ein Dritter (z.B. Spediteur oder Frachtführer) bei einem Lieferanten abholt gilt der Ort, an dem sich der Gegenstand zum Zeitpunkt der Verschaffung der Befähigung, über ihn wirtschaftlich zu verfügen, der Ablieferung oder der Überlassung zum Gebrauch oder zur Nutzung befindet». Ferner: Verfügungsmacht auch «durch die blosse Übergabe von Papieren (z.B. Konnossemente, Lagerscheine)». Werklieferung: «an dem Ort als abgeliefert, an dem die Arbeiten … ausgeführt werden» (Beispiel Waschmaschine) | `e0b0bb66-0b13-40d2-99bd-aa985aef1ef3` · https://mcp-tax.lexplorer.ch/s/doc/feb67ec1-f25e-4c10-925d-83f6b6f2e0ef?chunk=e0b0bb66-0b13-40d2-99bd-aa985aef1ef3 |
| Beförderungs- und Versandlieferung (Abs. 1 Bst. b) | Teil II Ziff. 2.3 | «… gilt der Ort, an dem die Beförderung oder die Versendung des Gegenstandes zum Abnehmer (oder in dessen Auftrag zu einer Drittperson) beginnt … Eine Ausnahme bildet die Lieferung von Elektrizität in Leitungen, Gas über das Erdgasverteilnetz und Fernwärme.» Montage am Ziel: Der Ort bleibt beim Beginn, «sofern die Montage/Installation als Nebenleistung im Sinne von Artikel 19 Absatz 4 MWSTG … qualifiziert werden kann». Sonst «liegt eine werkvertragliche Lieferung vor (Ziff. 3)». Mit Positiv- und Negativbeispielen (z.B. Einbauküche, Deckenlampe, Software-Installation) | `a2cbd6a8-c6b5-49d9-9c38-4b9da5549d35` · https://mcp-tax.lexplorer.ch/s/doc/feb67ec1-f25e-4c10-925d-83f6b6f2e0ef?chunk=a2cbd6a8-c6b5-49d9-9c38-4b9da5549d35 |
| Unterstellungserklärung Ausland (Abs. 3 Bst. a) | Teil II Ziff. 2.4 (mit Beispielen 1–3) | «Bei der Verbringung eines Gegenstandes vom Ausland ins Inland gilt der Ort der Lieferung als im Inland gelegen, wenn der Lieferant im Zeitpunkt der Einfuhr über eine Bewilligung der ESTV verfügt, die Einfuhr im eigenen Namen vorzunehmen (Unterstellungserklärung Ausland, Art. 7 Abs. 3 Bst. a MWSTG).» – «Die Einfuhr mittels Unterstellungserklärung Ausland ist nicht möglich, wenn der Empfänger – oder in seinem Auftrag ein Dritter – den Gegenstand beim Lieferanten abholt (Abhollieferung).» – Verzicht: Hinweis «im Wertnachweis für die Einfuhrsteuer (i. d. R. Rechnung) zum Zeitpunkt der Einfuhr», z.B. «Auf die Vornahme der Einfuhr im eigenen Namen wird verzichtet». – Unterstellungserklärung Inland: «Mit der Anwendung der Unterstellungserklärung Inland ändert der Ort der davon betroffenen Lieferungen nicht.» | `f1b4fc15-27fe-4987-b7b0-cd1c47977efb` (Beispiele `c3006207-e3cd-4b66-950e-041bf1735d3c`, `0a4c3620-8c6f-45ad-99a2-d4ac0ee66ca5`, `637ebfb4-81be-41ac-8595-8e8799a44187`) · https://mcp-tax.lexplorer.ch/s/doc/feb67ec1-f25e-4c10-925d-83f6b6f2e0ef?chunk=f1b4fc15-27fe-4987-b7b0-cd1c47977efb |
| Lager im Inland (Art. 4 MWSTV) | Teil II Ziff. 2.5 | «Als Ort der Lieferung gilt das inländische Lager, an dem der Gegenstand an den Abnehmer übergeben wird … Bei Lieferungen von Gegenständen, die aus dem Ausland in ein Lager im Inland verbracht … werden, liegt der Ort der Lieferung hingegen dann im Ausland, wenn der Lieferungsempfänger und das zu entrichtende Entgelt beim Verbringen der Gegenstände ins Inland bekannt sind …» (vertieft in Ziff. 6.1.1/6.1.2) | `747fb73e-6caa-45e6-88f2-55ca9b9b6122` · https://mcp-tax.lexplorer.ch/s/doc/feb67ec1-f25e-4c10-925d-83f6b6f2e0ef?chunk=747fb73e-6caa-45e6-88f2-55ca9b9b6122 (6.1.1: `fe634c13-3169-4b77-ab4f-ea269caafbf1`; 6.1.2: `cfdae3b5-ccd0-4578-bd75-30aa1380208c`) |
| Versandhandel (Abs. 3 Bst. b) | Teil II Ziff. 2.6 | «Erzielt ein (in- oder ausländischer) Versandhändler pro Jahr mindestens 100'000 Franken Umsatz aus Kleinsendungen (Einfuhrsteuerbetrag bis fünf Franken), die er vom Ausland ins Inland befördert oder versendet, gelten seine Lieferungen als Inlandlieferungen (Art. 7 Abs. 3 Bst. b MWSTG). … Es gelten sodann nicht nur die Kleinsendungen des Versandhändlers als Inlandlieferungen, sondern auch alle weiteren Sendungen, bei denen der Einfuhrsteuerbetrag mehr als fünf Franken pro Sendung beträgt.» | `c1020e44-efb3-4218-932f-4095384755b5` · https://mcp-tax.lexplorer.ch/s/doc/feb67ec1-f25e-4c10-925d-83f6b6f2e0ef?chunk=c1020e44-efb3-4218-932f-4095384755b5 |
| Werklieferung (Bearbeitung) | Teil II Ziff. 3.1 (3.2.1, 3.2.2, 3.3) | «… beginnt die Lieferung – ungeachtet der Inbetriebnahme – mit der Aufnahme der Tätigkeit am Ort der Installation, der Reparatur oder der Montage. Die Lieferung gilt in der Folge als dort erbracht, wo die werkvertragliche Leistung vorgenommen bzw. wo der Gegenstand abgeliefert wird (Art. 7 Abs. 1 Bst. a MWSTG).» – 3.3: «Sofern die Ablieferung des betreffenden Gegenstandes im Ausland erfolgt, liegt beim inländischen Unternehmer eine Lieferung im Ausland vor». – 3.2.1 Vereinfachung: Die ESTV sieht von einer rückwirkenden Eintragung ab, «[s]ofern dem Bund … nachweislich kein Steuernachteil erwachsen ist» | 3.1 `4f3a89fe-d53e-4018-b6c3-4530b091fcdf`; 3.2.2 `184556c1-b701-43aa-878e-0d26040a6b77`; 3.3 `01b765c0-431b-4eea-8eb1-12a43afc00fd` · https://mcp-tax.lexplorer.ch/s/doc/feb67ec1-f25e-4c10-925d-83f6b6f2e0ef?chunk=4f3a89fe-d53e-4018-b6c3-4530b091fcdf |
| Reihengeschäft | Teil II Ziff. 4.1 / 4.2 | «Bei Reihengeschäften gelten sämtliche Lieferungen innerhalb der Reihe als im gleichen Zeitpunkt und am gleichen Ort (Ort der Abholung resp. Ort des Beförderungs- oder Versandbeginns) ausgeführt. Bei Einfuhrreihengeschäften gelten die in der Reihe erbrachten Lieferungen als im Ausland erbracht.» Mit Unterstellungserklärung gelten die Lieferungen des Einführers und die nachfolgenden als im Inland erbracht (Art. 3 Abs. 2 MWSTV). Ausfuhr (4.2): Steuerbefreiung für alle Lieferanten der Reihe bei direkter Ausfuhr (Art. 23 Abs. 3 MWSTG) | 4.1 `e1c78ce8-109c-4abf-82b0-59d446a78030`; 4.2 `ea2752bf-4679-4565-9dab-5f022b885c70` · https://mcp-tax.lexplorer.ch/s/doc/feb67ec1-f25e-4c10-925d-83f6b6f2e0ef?chunk=e1c78ce8-109c-4abf-82b0-59d446a78030 |
| Kommission | Teil II Ziff. 5.2 | Ort beim Kommittenten an den Kommissionär: «Abhollieferung; Ziff. 2.2» bzw. «Beförderungs- oder Versandlieferung; Ziff. 2.3» | `203e1945-8d13-4dee-abe8-5877a175e2ce` · https://mcp-tax.lexplorer.ch/s/doc/feb67ec1-f25e-4c10-925d-83f6b6f2e0ef?chunk=203e1945-8d13-4dee-abe8-5877a175e2ce |
| Lager im Ausland | Teil II Ziff. 6.2 | Inländischer Lieferant mit Lager im Ausland: Ort der Lieferung im Ausland | `a2290afe-0c68-4dc9-87da-1b5f4dfc4e25` |
| Vermietung und Leasing | Teil II Ziff. 8.1 | «Wenn der Vermieter/Leasinggeber den Gegenstand … befördert oder versendet, gilt die Überlassung an dem Ort als erfolgt, an dem die Beförderung oder der Versand beginnt … Die Vermietung und das Verleasen von Gegenständen ab dem Inland gelten demzufolge als Inlandumsätze, und zwar ungeachtet dessen, ob die Gegenstände im Inland verbleiben oder … exportiert werden.» | `53576008-ee0c-491f-aa12-768f3b012900` · https://mcp-tax.lexplorer.ch/s/doc/feb67ec1-f25e-4c10-925d-83f6b6f2e0ef?chunk=53576008-ee0c-491f-aa12-768f3b012900 |
| Versandhandel, Zeitpunkt und Umsatzberechnung | Teil IV (Fragen & Antworten), Abschnitte «Um was geht es …?» und «Wie kann man die Mehrwertsteuerpflicht überprüfen?» | «Die Umsatzgrenze errechnet sich aus den von den Käufern an den Versandhändler bezahlten Entgelten.» – «… so gilt der Ort der Lieferung bis zum Ende desjenigen Monats als im Ausland gelegen, in dem der Leistungserbringer die Umsatzgrenze von 100'000 Franken aus solchen Lieferungen erreicht hat (Art. 4a Abs. 1 MWSTV). Ab dem Folgemonat gilt der Ort der Lieferung für alle Lieferungen des Versandhändlers vom Ausland ins Inland als im Inland gelegen». Fn. [2]: «Relevant sind neben Versand- auch Beförderungslieferungen, nicht jedoch Abhollieferungen.» – «Auch unter der Versandhandelsregelung gilt weiterhin, dass auf Kleinsendungen keine Einfuhrsteuer erhoben wird.» | «Um was geht es …»: `d157cb85-1cf0-43e4-815c-812be0d2a2eb`; «Wie kann man …»: `18331974-8f15-439d-848f-5fcce3775456` · https://mcp-tax.lexplorer.ch/s/doc/feb67ec1-f25e-4c10-925d-83f6b6f2e0ef?chunk=18331974-8f15-439d-848f-5fcce3775456 |
| Versandhandel und Unterstellungserklärung | Teil IV, Abschnitte «Wie ist der Ablauf bei der freiwilligen Steuerpflicht …» und «… bereits mehrwertsteuerpflichtigen Unternehmen …» | «Sobald Steuerpflichtige, welche bereits im Besitz der ‹Unterstellungserklärung Ausland› sind, die Voraussetzungen der Versandhandelsregelung erfüllen (Art. 7 Abs. 3 Bst. b MWSTG), haben sie nicht mehr die Möglichkeit, in Einzelfällen auf die Anwendung der ‹Unterstellungserklärung Ausland› zu verzichten». – Bereits steuerpflichtige Unternehmen: Kleinsendungen bleiben «Auslandumsätze», bis die Grenze «aus solchen Lieferungen (Kleinsendungen) erreicht wird». Kein Saldosteuersatz (Art. 77 Abs. 2 MWSTV) | `b93fc9e2-b7ae-4ea9-846d-530d6697196e`; `d67fbfc4-0cb2-4307-b776-086c2e65ec2e` |
| Doppelbelastung | Teil IV «Was hat der steuerpflichtige Versandhändler zu beachten?» | «… kann grundsätzlich weder die ESTV noch das BAZG die Steuer rückerstatten, da die Inland- und Einfuhrsteuer geschuldet sind.» Der Versandhändler kann die Einfuhrsteuer als Vorsteuer abziehen, «selbst wenn der Käufer auf der Veranlagungsverfügung als Importeur aufgeführt ist». Praxisänderung, publiziert am 29.4.2025 | `dda391b1-a904-40f3-8890-82d6eb4c5908` |

### 4.2 MWST-Branchen-Info 07 «Elektrizität in Leitungen, Gas über das Erdgasverteilnetz und Fernwärme»
- OCL `estv_mwst_de_1029216`. Lexplorer doc `c88dae61-0bbe-4ff1-9b58-6503dd1141b2`, Inhaltsverzeichnis `669f070a-20ee-4add-93f7-ab9b1f7d2e0b`.

| Ziff. | Kernsatz | Chunk |
|---|---|---|
| 1 Einleitung | «Die Lieferung von Elektrizität und Erdgas in Leitungen an Unternehmen mit Sitz im Ausland unterliegt nicht der Mehrwertsteuer, wenn der Sitz des Leistungsempfängers im Ausland einwandfrei nachgewiesen ist.» | (Text aus OCL; der Einleitungs-Chunk ist nicht gesondert nummeriert) |
| 3 Ort der Lieferung | «Der Ort der Lieferung befindet sich an dem Ort, an dem der Leistungsempfänger (Auftraggeber) den Sitz der wirtschaftlichen Tätigkeit oder eine Betriebsstätte hat …» Beispiel Electra AG Chur: Einkauf aus München = Ort Chur (Inland); Verkauf nach Luxemburg = Ausland | `a8b672da-9269-435d-9a96-adc79a69fe52`, Beispiel `9ad31a4c-d546-4b78-b8f3-92a358720e9d` · https://mcp-tax.lexplorer.ch/s/doc/c88dae61-0bbe-4ff1-9b58-6503dd1141b2?chunk=a8b672da-9269-435d-9a96-adc79a69fe52 |
| 4 Steuerpflicht | Ausländische Lieferanten sind befreit bei «Lieferung von Elektrizität in Leitungen, Gas über das Erdgasverteilnetz und Fernwärme an steuerpflichtige Personen im Inland» | `5ea30f62-8256-4614-82bf-cb1ad01fde3a` |
| 5 Geschäftsfälle (Chunk «Beispiele»; Ziffer laut Inhaltsverzeichnis, Überschrift im Chunk nicht erhalten) | Ferienhäuser: «Als Ort der Lieferung gilt der Ort, an dem die Kunden die Betriebsstätte haben bzw. am Ort, von dem aus sie tätig werden und der Strom verbraucht wird. In beiden Fällen ist dies der Standort der Ferienhäuser (Art. 7 Abs. 2 MWSTG).» – «Bei Lieferungen von Gas über das Erdgasverteilnetz und Fernwärme kommen die gleichen gesetzlichen Bestimmungen zur Anwendung.» Nachweis nach Art. 81 Abs. 3 MWSTG | `c47736e7-9061-4da8-a8a1-9d8f502a13c2` · https://mcp-tax.lexplorer.ch/s/doc/c88dae61-0bbe-4ff1-9b58-6503dd1141b2?chunk=c47736e7-9061-4da8-a8a1-9d8f502a13c2 |
| 7.2 Versorgung des grenznahen Auslandes | «… via eigenes Netz im Ausland liegt der Ort der Lieferung im Ausland. Die Lieferung gilt gemäss Artikel 7 Absatz 2 MWSTG als am Sitz des Empfängers erbracht.» | `317d9981-119f-4272-9037-a1ceea3e7632` |
| 7.4 Reihen- und Kaskadengeschäfte | Kraftwerk mit ausländischem Partner: Die Lieferung an den Partner liegt «am Sitz der wirtschaftlichen Tätigkeit des Empfängers, also im Ausland»; die Weiterlieferung an einen inländischen Kunden liegt im Inland | `7028f2ea-1aeb-40f0-b039-b3f2f622cc17` |
| 7.5 Herkunftsnachweise | Zusammen mit der Energielieferung eine Lieferung «(Ort der Leistung nach Art. 7 Abs. 2 MWSTG, Empfängerortsprinzip)»; losgelöst eine Dienstleistung nach Art. 8 Abs. 1 | `287104da-16a2-441d-a70d-d302148707a8` |
| 7.8 Stromüberproduktion | Gratisüberlassung oder negativer Kaufpreis: «gilt nicht als Lieferung, sondern als Dienstleistung» | `648a11aa-a73b-48ea-9ba8-e635d76928ce` |
| 7.9 Ladestationen | Verweis auf MBI 05 | (im Inhaltsverzeichnis) |

**MBI 05 Motorfahrzeuggewerbe, Ziff. 13.4 «Lieferung von Elektrizität in Leitungen»**
- Lexplorer doc `cf09ca02-38a7-4b1b-b081-60f89e1d94b0`, Chunk `322fcc3d-adb1-4908-9056-5cda1958cab7`.
- Kernsatz: «… in Ermangelung eines solchen Sitzes oder einer solchen Betriebsstätte gilt als Ort der Lieferung der Ort, an dem sich die Ladestation befindet (dies ist z. B. bei nicht mehrwertsteuerpflichtigen natürlichen Personen der Fall).»
- Kettengeschäft nach Ziff. 13.2.

### 4.3 MWST-Info 22 «Ausländische Unternehmen» (Stand 17.4.2025)
- OCL `estv_mwst_de_1551451`. Lexplorer doc `b8a136d2-7024-436a-940a-3c68db66fd70`.
- **Ziff. 1.2.1.1** (Chunk `48680a59-52e3-4703-af8f-d8123a98deb2`): «Im Gegensatz zum EU-Mehrwertsteuerrecht gelten im Schweizer Mehrwertsteuerrecht die Vermietung von Gegenständen, das Vornehmen von Reparaturen und sonstigen Arbeiten an Gegenständen sowie deren Installation vor Ort als Lieferungen und nicht als Dienstleistungen. Diese Qualifikation wirkt sich auf den Ort der Leistung (Ziff. 1.2.1.3) und somit auf die Steuerpflicht im Inland aus.»
- **Ziff. 1.2.1.3 «Ort der Lieferung»** (Chunk `b82dd044-638a-4c28-ac38-5e3be480dcae`, https://mcp-tax.lexplorer.ch/s/doc/b8a136d2-7024-436a-940a-3c68db66fd70?chunk=b82dd044-638a-4c28-ac38-5e3be480dcae):
  - «Wird ein Gegenstand neu angefertigt oder vor der Übergabe an den Abnehmer noch bearbeitet …, so gilt der Gegenstand erst im Zeitpunkt der Übergabe an den Abnehmer, d.h. nach Abschluss der Arbeiten, als geliefert.»
  - «Wer somit einen Gegenstand aus dem Ausland in die Schweiz versendet, löst allein mit solchen Lieferungen in der Schweiz keine Steuerpflicht aus, da der Ort der Lieferung im Ausland ist.»
  - Unterstellungserklärung: «Dies hat zur Folge, dass der Ort der Lieferung im Inland liegt, obwohl die Beförderung/Versendung im Ausland begonnen hat.»
  - Versandhandel: wie MI 06 Ziff. 2.6.
- Fall F (Chunk `3e6911d6-ce1e-4ce3-9134-4335b3ef59f2`): Badeteich in Basel durch ein deutsches Unternehmen = «Lieferung im Inland (Art. 7 Abs. 1 Bst. a MWSTG)». Die Steuerpflicht beginnt mit dem Rechnungsdatum der Vorauszahlung.

### 4.4 MWST-Branchen-Info 27 «Elektronische Plattformen» (Art. 20a im Verhältnis zu Art. 7 Abs. 3)
- OCL `estv_mwst_de_1150270`. Lexplorer doc `1ffdd844-e071-419c-b0c5-f0f0cd13f378`.
- **Ziff. 2.1.1 «Eingeführte Gegenstände»** (Chunk `8ded0b83-7807-4315-9731-827becc7eca7`, https://mcp-tax.lexplorer.ch/s/doc/1ffdd844-e071-419c-b0c5-f0f0cd13f378?chunk=8ded0b83-7807-4315-9731-827becc7eca7):
  - «… gilt die erste Lieferung zwischen dem Verkäufer und der steuerpflichtigen Plattformbetreiberin als im Ausland erbracht …»
  - «Die zweite Lieferung … unterliegt der Inlandsteuer, sofern: 1. Die Plattformbetreiberin die Umsatzgrenze von 100'000 Franken pro Jahr für Kleinsendungen … erreicht (eigene Lieferungen und Lieferungen, welche die Plattformbetreiberin im Sinne von Artikel 20a MWSTG ermöglicht hat); oder 2. die Plattformbetreiberin die Anwendung der Unterstellungserklärung Ausland beantragt»
- **Ziff. 4.3** (Chunk `cc8c623e-1f9d-42a7-993d-ce0a58ed18e9`): «Artikel 7 Absatz 3 MWSTG findet diesfalls keine Anwendung auf den Verkäufer. Stattdessen liegt der Ort der zweiten Lieferung von der Plattformbetreiberin an den Käufer im Inland (Art. 20a MWSTG i. V. m. Art. 7 Abs. 3 MWSTG). Artikel 4a MWSTV findet entsprechend auf die Plattformbetreiberin Anwendung …» Ausnahme: Einfuhr durch den Verkäufer nach Art. 111b MWSTV.
  - **Bezug zur VE 2025:** Art. 7 Abs. 4 VE-MWSTG würde diese Praxis im Gesetz verankern.
- **Ziff. 5 «Administrative Massnahmen (Art. 79a MWSTG)»** (Chunk `ec6997e6-3eff-41c4-83fa-37da5f77be13`): «Die ESTV kann gegen eine steuerpflichtige Person, die nach Artikel 7 Absatz 3 Buchstabe b MWSTG Lieferungen im Inland erbringt (Plattformbetreiberin oder Versandhändlerin), ein Einfuhrverbot anordnen …»
- **Ziff. 6.1/6.2** «Steuerliche Auswirkungen» (Chunks `15c0a596-ddb6-4988-8d4e-d739a086cf34`, `73dfa99d-4766-49ce-b50c-3c70ffa5ede8`): «Der Verkäufer erbringt in diesem Fall auch dann eine nicht steuerbare Lieferung im Ausland, wenn er die Umsatzschwelle von 100'000 Franken jährlich für ins Inland eingeführte Kleinsendungen erreicht hat.» – «… empfiehlt die ESTV der Plattformbetreiberin, die Anwendung der Unterstellungserklärung Ausland zu beantragen.»

### 4.5 MWST-Info 04 «Steuerobjekt» (nur Randbezug)
- OCL `estv_mwst_de_1003047`, Lexplorer doc `d2349388-0778-4b1c-b066-f11e1e742b9c`. Ziffer nicht festgestellt, da nur Randbezug.
- Kernsatz: «Leistungen …, welche als im Ausland erbracht gelten (Ort der Lieferung/Dienstleistung befindet sich gemäss Artikel 7 oder 8 MWSTG im Ausland …), werden von der inländischen MWST nicht erfasst.»
- Fahrzeugvermietung: «Ob die Übergabe des Fahrzeuges im Inland (Abhollieferung) oder im Ausland (Beförderungs- oder Versandlieferung) erfolgt, spielt keine Rolle» für die Befreiung nach Art. 23 Abs. 2 Ziff. 2.
- Der Lieferbegriff ist für den Ort in MI 06 Teil II Ziff. 1 dargestellt (Chunk `7b4f99e3-3ed3-412a-8050-db70137ca19a`).

### 4.6 Einfuhr, BAZG
- MI 06 verweist auf die Richtlinie R-69-01 des BAZG (Teil II Ziff. 3 und 4) und auf die Publikation 52.02 (MI 22).
- Diese BAZG-Dokumente sind nicht in der ESTV-Quelle enthalten und wurden nicht ausgewertet.

---

## 5. Offene Punkte
1. BBl 1996 V 713: Die gedruckten Seiten sind am Scan zu prüfen; vorhanden sind nur OCL-Indexseiten 26 f. und 103.
2. Erläuterungen der ESTV zur MWSTV-Änderung vom 15.8.2018 (Art. 4a in der Endfassung) sind in Fedlex und OCL nicht vorhanden.
3. Für die Abweichungen 2016 (Erdgasverteilnetz) und den Grund der Staffelung (lit. b erst 2019) fehlen Ratsprotokolle und Kommissionsunterlagen.
4. Spannung zwischen den Erläuterungen E-MWSTV 2009 (Unterstellungserklärung auch bei Abhollieferung) und MI 06 Ziff. 2.4 (bei Abhollieferung nicht möglich). Diese Frage ist mit Rechtsprechung zu klären (Cache: 2C_1079/2016).
