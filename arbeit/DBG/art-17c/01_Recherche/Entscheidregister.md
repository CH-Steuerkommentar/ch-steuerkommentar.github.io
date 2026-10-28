# Entscheidregister Bundesgericht – Art. 17c DBG (Einkünfte aus unechten Mitarbeiterbeteiligungen)

Norm: Art. 17c DBG i.d.F. des BG vom 17.12.2010 über die Besteuerung von Mitarbeiterbeteiligungen (AS 2011 3259), in Kraft seit 1.1.2013. Wortlaut: «Geldwerte Vorteile aus unechten Mitarbeiterbeteiligungen sind im Zeitpunkt ihres Zuflusses steuerbar.» Parallelnorm Art. 7e StHG; Begriff in Art. 17a Abs. 2 DBG / Art. 7c Abs. 2 StHG («Anwartschaften auf blosse Bargeldabfindungen»).

Stand der Recherche: 28.10.2026. Quellen: Entscheid-Cache `data/entscheide/` (2C_168/2012, 2C_285/2019, 8C_463/2024), Open Case Law (search_decisions, find_leading_cases, get_erwaegung, find_relevant_erwaegung, get_decision), Entscheidsuche (Hierarchie CH_BGer/CH_BGE). Abgleich mit dem Register zu Art. 17a DBG (`arbeit/DBG/art-17a/01_Recherche/Entscheidregister.md`). Keine Websuche, kein Lexplorer.

Zitierstrings wörtlich aus `citation_string_de` (Open Case Law) bzw. `zitat_de` (Cache).

Klassen: **A** = Erwägung legt den Zuflusszeitpunkt bei unechten Mitarbeiterbeteiligungen oder den Begriff der unechten Beteiligung aus bzw. zieht Art. 17c DBG / Art. 7e StHG tragend heran; **B** = Anwendung bzw. Wiedergabe der Norm im Rahmen einer anderen Sachfrage; **C** = blosse Erwähnung.
Fassung: «n.F.» = Steuerperiode ab 2013; «a.F.» = Steuerperiode vor 2013 (Art. 17 DBG / Art. 7 StHG a.F.; Novelle nur als Bestätigung der Praxis oder analog herangezogen).

## (a) Suchwege und Trefferzahlen

| # | Werkzeug | Abfrage | Treffer | Ergebnis |
|---|---|---|---|---|
| 1 | Cache | 3 Dateien `data/entscheide/ocl_*.json` (Feld `normen` «DBG/17c») | 3 | 2C_168/2012 (E. 2.7) und 2C_285/2019 (E. 5.2.1) einschlägig; 8C_463/2024 Fehltreffer (Art. 17c ELV/OPC-AVS/AI) |
| 2 | OCL search_decisions, court bger, compact | `"Art. 17c DBG" OR "art. 17c LIFD" OR "Art. 17c LIFD"` | 200 (Untergrenze) | Tokenisierung unscharf («17c» → «17»): Ranking liefert überwiegend Art.-17-DBG-Entscheide; unter den ersten 50 nur 2C_168/2012 und 2C_285/2019 einschlägig |
| 3 | OCL search_decisions, court bge, compact | `"Art. 17c DBG" OR "art. 17c LIFD"` | 200 (Untergrenze) | nur Art.-17-DBG-Treffer (BGE 151 II 409, 139 II 363 u.a.); kein einschlägiger BGE |
| 4 | OCL search_decisions, court bger, compact | `"Art. 7e StHG" OR "art. 7e LHID"` | 220 (Untergrenze) | Ranking unscharf (Art. 7 StHG); 2C_1057/2018 an Rang 2 einschlägig, Rest Fehltreffer |
| 5 | OCL search_decisions, court bge, compact | `"Art. 7e StHG" OR "art. 7e LHID"` | 128 (Untergrenze) | nur Art.-7-StHG-Treffer; kein einschlägiger BGE |
| 6 | OCL search_decisions, court bger | `"unechte Mitarbeiterbeteiligung" OR "unechten Mitarbeiterbeteiligungen" OR "unechte Mitarbeiterbeteiligungen" OR "participations de collaborateur(s) improprement dites"` | 129 (Untergrenze) | einschlägig nur 2C_285/2019, 2C_168/2012; sonst «unechte Noven/Urkunde/Rückwirkung», echte Mitarbeiterbeteiligungen (9C_13/2025, 9C_168/2023, 9C_226/2024, 2C_974/2019, 9C_1/2023 – vgl. Register Art. 17a), Zivilentscheide (4C.329/2003, 4A_187/2015, 5A_749/2023) |
| 7 | OCL search_decisions, court bger | `"Phantom" AND (Steuer OR impôt)` | 152 (Untergrenze) | keine Treffer mit «Phantom» im Steuerkontext unter den ersten 30 (Ranking über «impôt»/«Steuer»); kein einschlägiger Entscheid |
| 8 | OCL search_decisions, court bger, compact | `"Stock Appreciation Rights" OR "phantom stock" OR "phantom stocks" OR "phantom shares"` | 206 (Untergrenze) | unscharf (Einzeltokens «stock», «shares», «rights»); erste 50: Zivil-/Strafentscheide, 2C_285/2019, 2C_168/2012; kein SAR-/Phantom-Entscheid |
| 9 | OCL search_decisions, court bger, compact | `Bargeldabfindung OR Bargeldabfindungen` | 91 (Untergrenze) | erste 20: Sozialversicherung, Raumplanung, Zivil (Abfindung); kein Steuerentscheid zu unechten Beteiligungen |
| 10 | OCL search_decisions, court bger, compact | `"Co-Investment" AND Mitarbeiter` | 54 (Untergrenze) | erste 20: Straf-/Zivilentscheide (u.a. Carried-Interest-Pool 4A_380/2011, 4A_526/2016, 4A_528/2016); kein Steuerentscheid |
| 11 | OCL search_decisions, court bger, compact | `Anwartschaft AND Mitarbeiterbeteiligung` | 132 (Untergrenze) | erste 30: echte Beteiligungen/Optionen (2C_138/2010, 2C_889/2019), AHV-Entscheide zur «Anwartschaft auf Lohn» bei Lohngutschrift (H_364/2000, H_257/2000, H_138/2003; geprüft, kein Bezug zu Phantom/SAR), H_97/2006 (Optionen), Zivilentscheide; nichts Neues zu Art. 17c |
| 12 | OCL search_decisions, court bge, compact | `"unechte Mitarbeiterbeteiligung" OR … OR Phantom OR "Stock Appreciation Rights" OR Bargeldabfindung` | 126 (Untergrenze) | BGE 151 II 545 (echte Beteiligungen), BGE 145 V 188 (AVIG, RSU), BGE 152 III 225 (Güterrecht), sonst Fehltreffer; kein BGE zu Art. 17c |
| 13 | OCL find_leading_cases | law_code DBG, article 17c | 2 | nur kantonal (ZH VGer SB.2019.00001; ZH SozVGer AB.2019.00007) – nicht Gegenstand dieses Registers |
| 14 | OCL find_leading_cases | law_code LIFD, article 17c | 4 | 2C_168/2012, 2C_285/2019; kantonal GE A/3151/2023, C/13217/2018 |
| 15 | OCL find_leading_cases | law_code StHG, article 7e | 1 | 2C_1057/2018 |
| 16 | OCL find_leading_cases | law_code LHID, article 7e | 0 | – |
| 17 | OCL find_leading_cases, court bger | Freitext `unechte Mitarbeiterbeteiligung Phantom Stocks Bargeldabfindung Zufluss` | 20 (filters_relaxed) | nur Nachbarn ohne Bezug (Familien-, Sozialversicherungsrecht); kein Treffer |
| 18 | Entscheidsuche CH_BGer/CH_BGE | `"Art. 17c DBG" OR "art. 17c LIFD" OR "Art. 17c LIFD" OR "17c DBG" OR "17c LIFD"` | 2 | 2C_285/2019, 2C_168/2012 |
| 19 | Entscheidsuche CH_BGer/CH_BGE | `"Art. 7e StHG" OR "art. 7e LHID" OR "7e StHG" OR "7e LHID" OR "7e LAID"` | 2 | 2C_1057/2018, 2C_168/2012 |
| 20 | Entscheidsuche CH_BGer/CH_BGE | `"art. 17c" OR "Art. 17c" OR "art. 7e" OR "Art. 7e" OR "17c ff" OR "17b und 17c" OR "17b et 17c" OR "17a-17d" OR "17a–17d"`, ab 2011 | 17 | neu nichts; Fehltreffer: Art. 17c ELV (8C_662/2024, 8C_228/2025, 8C_240/2025, 8C_12/2024, 8C_463/2024), Art. 7e SchlT ZGB (5A_408/2018, 5A_351/2019, 5A_333/2018, 9C_154/2024), Art. 7e RVOG/LOGA (BGE 141 I 20, 2C_97/2014), Art. 17c LEDP/VD (BGE 141 I 221, 1C_58/2015), 1C_420/2017 |
| 21 | Entscheidsuche CH_BGer/CH_BGE | `"unechte(n) Mitarbeiterbeteiligung(en)" OR "improprement dites" OR "partecipazioni improprie" OR "impropriamente dette"` | 51 | einschlägig nur 2C_285/2019, 2C_168/2012; Rest «lacunes/exonérations/fusions/pertes de fusion improprement dites» (Fehltreffer) |
| 22 | Entscheidsuche CH_BGer/CH_BGE | `(Phantom* OR "phantom stock(s)" OR "phantom shares" OR "Phantom-Aktien" OR "actions fantômes" OR "actions fictives") AND (Steuer* OR impôt* OR AHV OR AVS OR Lohn* OR salaire)` | 8 | sämtlich Fehltreffer («Phantomschmerz», «Phantomuniversität», «Phantomgeld», «Phantomwert») |
| 23 | Entscheidsuche CH_BGer/CH_BGE | `"phantom stock(s)" OR "phantom share(s)" OR "Phantom Stock Plan" OR "Phantom(-)Aktien" OR "phantom options" OR "virtuelle(n) Aktien" OR "actions virtuelles" OR "azioni fantasma"` | 0 | – |
| 24 | Entscheidsuche CH_BGer/CH_BGE | `"Stock Appreciation Right(s)" OR "share appreciation rights" OR "SAR-Plan" OR "droits à la plus-value"` | 0 | – |
| 25 | Entscheidsuche CH_BGer/CH_BGE | `Bargeldabfindung(en) OR "indemnité(s) en espèces" OR "Barabgeltung der Wertsteigerung"` | 3 | 2C_168/2012; Fehltreffer BGE 85 I 211 (Ruhetage), 8C_760/2014 (Verpflegung) |
| 26 | Entscheidsuche CH_BGer/CH_BGE | `("Co-Investment(s)" OR "(co)investissement" OR "carried interest") AND (Mitarbeiter* OR collaborateur* OR Steuer* OR impôt*)` | 5 | nur Zivil-/Strafentscheide (4A_528/2016, 4A_526/2016, 4A_380/2011, 4A_19/2015, 6B_309/2021); kein Steuerentscheid |
| 27 | Entscheidsuche CH_BGer/CH_BGE | `(Anwartschaft* OR expectative*) AND (Mitarbeiterbeteiligung* OR Mitarbeiteraktie* OR Mitarbeiteroption* OR "participation(s) de collaborateur" OR "options/actions de collaborateur")` | 27 | einschlägig 2C_168/2012, 2C_285/2019, 2C_1057/2018; übrige betreffen echte Beteiligungen (9C_13/2025, BGE 151 II 545, 9C_168/2023, 9C_226/2024, 2C_974/2019, 2C_397/2015, 2C_138/2010, 2A.573/2002, 2A.517/2002, 2A.736/2004, 2C_705/2017), AHV-Optionen (BGE 133 V 346, H_97/2006), AVIG (BGE 145 V 188, 8C_427/2018), Güterrecht/Zivil (BGE 152 III 225, 5A_749/2023, 5A_54/2024, 5A_804/2018, 5C.6/2003, 4A_155/2019), Vermögenssteuer/Leibrente (BGE 138 II 311, 2C_337/2011), Nachfolgevergleich (2C_368/2013, E. 6.4: «vertragliche Anwartschaften», Art. 23 lit. d / 16 Abs. 1 DBG – kein Bezug zu Art. 17c) |
| 28 | Entscheidsuche CH_BGer/CH_BGE | `("deferred bonus" OR "deferred cash" OR "aufgeschobene(r) Bon(us/i)" OR "bonus différé(s)" OR "cash(-)settled" OR "Barausgleich" OR "share-based payment" OR "Wertsteigerungsrecht*") AND (Steuer* OR impôt* OR DBG OR LIFD OR AHV OR AVS)` | 5 | Fehltreffer: 2C_322/2025 (Massnahmen nach Art. 10a BankG, «Deferred Cash Compensations» – kein Steuerbezug, per get_decision geprüft), BGE 151 II 884 / 9C_41/2024 (Umsatzabgabe; «Barausgleich» bei Call-Optionen), 5A_779/2019, 5A_749/2023 |
| 29 | Entscheidsuche CH_BGer/CH_BGE | `(Mitarbeiterbeteiligung* OR "participation(s) de collaborateur") AND (Zufluss OR "au moment" OR encaissement OR Realisation OR réalisation) AND (bar OR espèces OR Barauszahlung OR Geld)` | 6 | nichts Neues (2C_168/2012, 9C_1/2023, 9C_226/2024, 4C.475/2004, 2C_368/2013, 2C_357/2014) |
| 30 | OCL get_erwaegung / find_relevant_erwaegung | 2C_168/2012 E. 2.2, 2.7, 2.8; 2C_285/2019 E. 5.2; 2C_1057/2018 E. 8.3, 8.5, 8.6 | – | Volltext der tragenden Erwägungen gelesen (Auszüge unten Ziff. c) |

## (b) Register

| Entscheid (Zitierstring) | Datum | Besetzung | Normstelle | Sachfrage | Kernaussage | E. | Ergebnis | Klasse | Fassung/Steuerperiode |
|---|---|---|---|---|---|---|---|---|---|
| BGer 2C_168/2012 vom 1. März 2013 | 01.03.2013 | **Fünfer** (Zünd, Aubry Girardin, Donzallaz, Stadelmann, Kneubühler) | Art. 17a Abs. 2, Art. 17c DBG; Art. 7c, 7e StHG (Novelle, noch nicht anwendbar) | Gesperrte «Restricted Shares» (US-Plan, beneficial ownership): Aktie (Besteuerung bei Zuteilung) oder blosse Anwartschaft? | Allgemeine Realisationsregel: Eine blosse Anwartschaft (suspensiv bedingte Forderung) löst mangels fester Forderung keine Besteuerung aus; die Novelle unterscheidet echte Beteiligungen von unechten («expectatives de simples indemnités en espèces» / «Anwartschaften auf blosse Bargeldabfindungen»), deren geldwerte Vorteile nach Art. 17c DBG / 7e StHG erst bei Vereinnahmung der Abfindung steuerbar sind; Restricted Shares mit wirtschaftlichem Eigentum sind keine solche Anwartschaft. | 2.2, 2.7 (tragend), 2.8, 4.3 | abgewiesen | **A** | a.F. (SP 2004/2005; Novelle als Bestätigung der Praxis herangezogen) |
| BGer 2C_1057/2018 vom 7. April 2020 | 07.04.2020 | **Fünfer** (Seiler, Aubry Girardin, Donzallaz, Stadelmann, Beusch; gem. Register Art. 17a) | Art. 7e StHG **analog** (i.V.m. Art. 7d Abs. 3 StHG analog) | Unterpreisiger Aktienverkauf durch beherrschenden Aktionär an neuen Mitarbeiter; Vorkaufsrecht des Mitarbeiters aus Aktionärbindungsvertrag zum Substanzwert | Ein künftiger Vorteil aus dem eigenen Vorkaufsrecht (Differenz Verkehrswert – Vorkaufspreis) wird «analog Art. 7e StHG» erst im Vorkaufsfall realisiert und ist in der Steuerperiode der Aktienübertragung eine nicht zu berücksichtigende reine Anwartschaft. | 8.5 (tragend), 8.3, 8.6 | Beschwerde des kant. Steueramts abgewiesen | **A** | a.F. (SP 2011, StG AG; Art. 7d/7e StHG analog) |
| BGer 2C_285/2019 vom 9. März 2020 | 09.03.2020 | Dreier (Seiler, Aubry Girardin, Donzallaz; gem. Register Art. 17a) | Art. 17a Abs. 1/2, Art. 17b, Art. 17c DBG; Art. 7c StHG / Art. 13a–13c StG VS | Performance Shares als Anwartschaft auf Mitarbeiteraktien; Einkommenszurechnung bei güterrechtlicher Übertragung an Ex-Ehegattin | Systematik der Art. 17a–17d DBG: echte (Abs. 1) und unechte (Abs. 2) Beteiligungen; Einkünfte aus unechten Beteiligungen sind im Zeitpunkt der Vereinnahmung der Abfindung steuerbar (Art. 17c DBG). Die Performance Shares werden als Anwartschaften auf Mitarbeiteraktien (echte Beteiligung, Besteuerung bei Umwandlung) eingeordnet; Art. 17c DBG wird nicht angewendet. | 5.2.1 (Wiedergabe Art. 17c), 5.2.3 | teilweise gutgeheissen (nur Unterhaltsabzug); zu den Performance Shares abgewiesen | **B** (Normwiedergabe; Abgrenzung zu Art. 17b; Grenzfall zu A) | n.F. (SP 2013) |

Zählung: A = 2 (2C_168/2012, 2C_1057/2018), B = 1 (2C_285/2019), C = 0. Fünferbesetzung: 2C_168/2012, 2C_1057/2018. Kein BGE (amtliche Sammlung) zu Art. 17c DBG / Art. 7e StHG; keine Steuerentscheide des Bundesgerichts zu Phantom Stocks, Stock Appreciation Rights, Cash-settled-Plänen oder Co-Investments.

Geprüft, aber nicht aufgenommen (kein Bezug zu unechten Beteiligungen bzw. zum Zufluss nach Art. 17c):
- Echte Mitarbeiterbeteiligungen ohne Bezug auf Art. 17c: BGE 151 II 545 (= 9C_168/2023), 9C_13/2025, 9C_604/2022, 9C_226/2024, 9C_1/2023, 9C_216/2023, 2C_974/2019, 2C_397/2015, 2C_705/2017, 2C_889/2019 (vgl. Register Art. 17a).
- AHV: BGE 133 V 346 und H_97/2006 (Mitarbeiteroptionen mit Vesting, Realisierung bei Ausübung – echte Beteiligung, kein Phantom/SAR); H_364/2000, H_257/2000, H_138/2003 (Anwartschaft auf Lohn bei blosser Lohngutschrift – allgemeiner AHV-Realisationsgrundsatz, kein Bezug zu Beteiligungen). Kein AHV-Entscheid zu Phantom Stocks oder SAR gefunden.
- Fehltreffer: 8C_463/2024 und weitere 8C-Entscheide (Art. 17c ELV), 2C_322/2025 (Art. 10a BankG), 2C_368/2013 (Nachfolgevergleich), Zivil- und Strafentscheide zu Carried Interest / Co-Investment / RSU.

## (c) Wörtliche Auszüge der A-Entscheide (und des B-Entscheids)

### BGer 2C_168/2012 vom 1. März 2013

E. 2.2 (Realisation; Anwartschaft):
> «S'agissant du moment de la réalisation effective, un revenu est considéré comme réalisé quand le contribuable reçoit une prestation en espèces ou (déjà) lorsqu'il acquiert une créance ferme permettant d'exiger cette prestation, créance dont il peut effectivement disposer»

> «Faute de constituer une prétention ferme, une simple expectative (soit une créance soumise à une condition suspensive […]) ne déclenche pas l'imposition»

E. 2.7 (Begriff und Zuflusszeitpunkt nach der Novelle):
> «La loi en question distingue entre les participations de collaborateur proprement dites, au nombre desquelles figurent les actions accordées au collaborateur, et les participations improprement dites que sont les "expectatives de simples indemnités en espèces" ("Anwartschaften auf blosse Bargeldabfindungen"; nouv. art. 17a LIFD et 7c LHID).»

> «Selon les nouveaux art. 17c LIFD et 7e LHID, les avantages appréciables en argent dérivant de participations de collaborateur improprement dites (expectatives) ne sont en revanche imposables qu'au moment où l'indemnité est encaissée.»

E. 2.8 (Abgrenzung wirtschaftliches Eigentum):
> «il convient d'admettre que l'imposition se justifie aussi, sous l'angle du principe constitutionnel de l'imposition selon la capacité contributive (art. 127 al. 2 Cst.), lorsque le collaborateur, sans avoir obtenu la propriété des actions au sens du droit civil, a acquis sur elles un pouvoir de disposer économiquement qui justifie de l'assimiler à un propriétaire au plan fiscal.»

### BGer 2C_1057/2018 vom 7. April 2020

E. 8.5 (analoge Anwendung von Art. 7e StHG):
> «Sollte B.________ in Zukunft seine Aktien verkaufen und der Beschwerdegegner sein Vorkaufsrecht ausüben, würde der Beschwerdegegner im Umfang einer (allfälligen) positiven Differenz zwischen dem dann (ohne Berücksichtigung des Aktionärbindungsvertrages anzunehmenden) Verkehrswert der Aktien und dem vereinbarten Vorkaufspreis ein Einkommen realisieren. Dieses Einkommen würde aber (analog Art. 7e StHG) erst im entsprechenden Vorkaufsfall realisiert und bildet damit in der hier interessierenden Steuerperiode 2011 eine nicht zu berücksichtigende reine Anwartschaft.»

E. 8.6 (Kontext, analog Art. 7d Abs. 3 StHG):
> «Sollte dies der Fall sein, wird der entsprechende Mehrwert dannzumal beim Beschwerdegegner als Einkommen besteuert werden (analog Art. 7d Abs. 3 StHG; vgl. auch E. 8.3 hiervor).»

E. 8.3 (Periodizität bei der Einkommenssteuer):
> «Bei der Einkommenssteuer geht es demgegenüber um die Ermittlung des dem Steuerpflichtigen in einer bestimmten Periode zufliessenden Einkommens.»

### BGer 2C_285/2019 vom 9. März 2020 (Klasse B)

E. 5.2.1:
> «La loi distingue entre les participations de collaborateur proprement dites (art. 17a al. 1 LIFD) et les participations improprement dites (art. 17a al. 2 LIFD).»

> «Les revenus provenant de participations de collaborateur improprement dites sont imposables au moment de l'encaissement de l'indemnité (art. 17c LIFD).»

E. 5.2.3:
> «Les expectatives sur des actions de collaborateur sont imposées au moment de la conversion en actions de collaborateur»

## (d) Gezielt gesucht, aber nicht gefunden

- BGer- oder BGE-Entscheid, der Art. 17c DBG oder Art. 7e StHG auf einen Sachverhalt der Steuerperiode ab 2013 **anwendet** (Besteuerung einer Barabfindung aus unechter Beteiligung).
- Entscheid, der den Begriff «Zufluss» in Art. 17c DBG auslegt (z.B. Auszahlung vs. Gutschrift, Verrechnung, Zahlung durch Dritte/Konzerngesellschaft, Zufluss nach Wegzug/Beendigung des Arbeitsverhältnisses).
- Steuerentscheid zu **Phantom Stocks / Phantom Shares**, **Stock Appreciation Rights (SAR)**, **Cash-settled RSU/PSU**, synthetischen Beteiligungen oder Deferred-Cash-Plänen (auch altrechtlich vor 2013; Entscheidsuche: 0 Treffer für die Fachbegriffe).
- Entscheid zur Abgrenzung unechte Mitarbeiterbeteiligung – gewöhnlicher Bonus / Tantieme.
- Entscheid zu **Co-Investment**- oder **Carried-Interest**-Modellen im Steuerrecht (nur Zivil- und Strafentscheide).
- AHV-Entscheid zu Phantom Stocks oder SAR mit Aussage zum Realisationszeitpunkt.
- Entscheid zur internationalen Aufteilung (Art. 17d DBG) bei unechten Beteiligungen.
- BGE zu Art. 17c DBG / Art. 7e StHG (keiner; find_leading_cases liefert für DBG 17c nur kantonale Entscheide, für LIFD 17c 2C_168/2012 und 2C_285/2019, für StHG 7e 2C_1057/2018).
