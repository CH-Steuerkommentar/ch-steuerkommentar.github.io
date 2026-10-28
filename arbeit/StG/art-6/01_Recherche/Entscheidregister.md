# Entscheidregister Bundesgericht zu Art. 6 StG (Ausnahmen von der Emissionsabgabe)

Stand der Recherche: 28.10.2026. Quellen: Entscheid-Cache `data/entscheide/` (Kandidatenliste `data/zitate/StG/art-6.json`, 13 Kandidaten mit normen «StG/6», dazu 3 Cache-Einträge mit normen «StG/67»/«StG/68») und Open Case Law (`search_decisions`, `find_leading_cases`, `get_decision`, `get_erwaegung`, `cite`); Gegenprobe über Entscheidsuche (Hierarchie CH_BGer/CH_BGE). Zitierstrings ausschliesslich aus `zitat_de` (Cache) bzw. `citation_string_de` (Open Case Law). Kantonale Gerichte und BVGer sind nicht bearbeitet. Das Register zu Art. 5 StG (`arbeit/StG/art-5/01_Recherche/Entscheidregister.md`) wurde wiederverwendet; alle übernommenen Entscheide sind an der Art.-6-Stelle neu gelesen.

## 0. Kopf

### Methode

1. Kandidatenliste bereinigt: Von den 13 Cache-Kandidaten sind 4 Fehltreffer (kantonales Steuergesetz bzw. DBG), 9 behalten (davon BGE 149 II 462 = BGer 9C_610/2022, zusammengeführt).
2. 38 Abfragen in Open Case Law (je `bger` und `bge`, `fields: compact`). Weil die Suche bei Phrasen unscharf ist (Oder-Logik, Totale bis über 3'000), wurden bei grossen Treffermengen die ersten 150 Treffer nach Relevanz, bei kleinen alle Treffer (bis 400) übernommen. Zusammen 4'855 verschiedene BGer/BGE-Entscheide; deren Volltexte (aus dem Cache, sonst über `get_decision`, abgelegt nur im Scratchpad, nicht im Cache) wurden maschinell durchsucht auf: Art. 6 Abs. 1 lit./Bst. a–m bzw. Abs. 2 StG, art. 6 al. 1 let./lettre LT, art. 6 cpv. 1 lett. LTB, Art. 6 StG/LT/LTB ohne Absatz, Art. 9 Abs. 1 lit. a aStG (Vorzugssatz), sowie Emissionsabgabe/droit d'émission/tassa d'emissione zusammen mit Quasifusion, fusionsähnlich, concentration analogue, Freibetrag, Wandlungskapital, gemeinnützig. Rund 50 Trefferkandidaten wurden an der einschlägigen Stelle gelesen.
3. `find_leading_cases` (StG, Art. 6) für `bger` und `bge`.
4. Gegenprobe Entscheidsuche (CH_BGer, CH_BGE) mit drei Abfragen.
5. Zitatnetz: In den A-Entscheiden zitierte Vorentscheide (2A.17/1994, 2A.107/1999, 2A.135/2000, 2C_374/2021, Urteil vom 12. Dezember 1997, ASA 53, 156/275) geprüft; soweit im Korpus, gelesen.

Klassen: A = Erwägung legt Art. 6 StG (oder eine Vorgängernorm, namentlich Art. 9 Abs. 1 lit. a StG 1973) aus oder entscheidet eine Sachfrage daraus; B = Anwendung ohne eigene Auslegung; C = blosse Erwähnung oder nur Vorgeschichte.

### Suchwege mit Trefferzahl

«Total» ist die von Open Case Law gemeldete Untergrenze beim ersten Aufruf (`total_is_lower_bound: true`; die Zahl schwankt zwischen Aufrufen). «Gescannt» = Volltexte maschinell durchsucht. «Neu» = einschlägiger Entscheid, der auf früheren Wegen noch nicht gefunden war.

| Weg | Abfrage / Filter | Total | gescannt | einschlägig | neu |
|---|---|---|---|---|---|
| Cache | normen «StG/6» | 13 | 13 | 9 | 9 Kandidaten (4 Fehltreffer) |
| OCL bger | "Art. 6 Abs. 1 lit." AND StG | 1'973 | 150 | 3 | 2C_976/2014, 9C_610/2022, 2C_1071/2018 |
| OCL bge | "Art. 6 Abs. 1 lit." AND StG | 2'500 | 150 | 2 | BGE 149 II 462, BGE 105 Ib 175 |
| OCL bger | "Art. 6 Abs. 1 Bst." AND StG | 3'144 | 150 | 4 | 2C_1001/2014 |
| OCL bge | "Art. 6 Abs. 1 Bst." AND StG | 1'342 | 150 | 1 | BGE 114 Ib 277 |
| OCL bger | "art. 6 al. 1 let." AND LT | 1'605 | 150 | 0 | – |
| OCL bge | "art. 6 al. 1 let." AND LT | 1'601 | 150 | 1 | – |
| OCL bger | "art. 6 cpv. 1 lett." AND LTB | 1'661 | 150 | 5 | 2C_1095/2015, 2C_447/2018 |
| OCL bge | "art. 6 cpv. 1 lett." AND LTB | 2'542 | 150 | 2 | – |
| OCL bger | Quasifusion | 25 | 264 | 7 | 2A.83/2001, 2A.84/2001, 2A.618/1998 |
| OCL bge | Quasifusion | 68 | 26 | 1 | BGE 102 Ib 140 |
| OCL bger | Emissionsabgabe Fusion | 2'514 | 150 | 11 | 2C_621/2018, 9C_232/2026, 2A.225/1999 |
| OCL bge | Emissionsabgabe Fusion | 1'778 | 150 | 9 | BGE 61 I 285, 115 Ib 125, 97 I 438, 98 Ib 197, 55 I 321 |
| OCL bger / bge | Emissionsabgabe Sanierung Freibetrag | 1'603 / 836 | 150 / 150 | 9 / 8 | – |
| OCL bger / bge | Emissionsabgabe Umwandlung | 945 / 2'096 | 150 / 150 | 9 / 9 | – |
| OCL bger / bge | "droit de timbre d'émission" exonération | 20 / 1'608 | 400 / 150 | 9 / 6 | – |
| OCL bger / bge | Emissionsabgabe gemeinnützig | 84 / 92 | 400 / 400 | 9 / 9 | – |
| OCL bger / bge | Emissionsabgabe Genossenschaft | 1'146 / 796 | 150 / 150 | 9 / 9 | – |
| OCL bger / bge | Emissionsabgabe Transportunternehmen | 149 / 1'687 | 150 / 89 | 11 / 9 | – |
| OCL bger / bge | Aufgelder Zuschüsse "Art. 6" | 1'125 / 1'104 | 150 / 150 | 0 / 1 | – |
| OCL bger / bge | Wandlungskapital | 31 / 7 | 31 / 7 | 1 / 0 | – (kein Entscheid zu lit. l) |
| OCL bger / bge | Anlagefonds Emissionsabgabe | 140 / 154 | 400 / 139 | 11 / 9 | – |
| OCL bger / bge | "Art. 6 StG" Emissionsabgabe | 36 / 116 | 192 / 56 | 12 / 9 | – |
| OCL bger / bge | "tassa d'emissione" esenzione | 17 / 2'121 | 400 / 150 | 8 / 5 | – |
| OCL bger / bge | Emissionsabgabe Spaltung | 1'614 / 1'743 | 150 / 150 | 9 / 9 | – |
| OCL bger / bge | Emissionsabgabe Partizipationskapital | 381 / 76 | 87 / 63 | 12 / 9 | – |
| OCL find_leading_cases | StG, Art. 6, court bger | 7 | 7 | 5 | – (Fehltreffer 2C_254/2022) |
| OCL find_leading_cases | StG, Art. 6, court bge | 4 | 4 | 1 | – (Fehltreffer BGE 73 I 125, 75 I 225, 86 I 10) |
| Entscheidsuche CH_BGer/CH_BGE | ("Art. 6 Abs. 1 lit" OR … OR "art. 6 LT") AND (Emissionsabgabe OR "droit d'émission" OR …) | 13 | 13 | 13 | – (alle bekannt) |
| Entscheidsuche CH_BGer/CH_BGE | (Emissionsabgabe OR …) AND (Fusion OR fusionsähnlich OR Quasifusion OR Sanierung OR Freibetrag OR gemeinnützig OR Umwandlung OR Spaltung OR Aufgeld OR concentration OR assainissement OR Transportunternehmen OR Anlagefonds OR Wandlungskapital) | 28 | 28 | 16 | BGE 148 II 121 (= 2C_624/2021) |
| Entscheidsuche CH_BGer/CH_BGE | (Emissionsabgabe OR … OR Stempelabgaben) AND (gemeinnützig* OR Wohnbaugenossenschaft OR Bürgschaftsgenossenschaft OR "utilité publique" OR Transportunternehmen OR Investitionsbeiträge OR "kollektive Kapitalanlage" OR SICAV OR Wandlungskapital OR Partizipationskapital) | 21 | 21 | 5 | – (2C_578/2019, 2A.299/2004, 2A.300/2004 geprüft: VSt) |

Gesamt gescannt: 4'855 BGer/BGE-Volltexte aus den OCL-Wegen, dazu 17 gezielt nachgeladene Entscheide. Die engen Wege (Entscheidsuche mit Normzitat, «Art. 6 StG» Emissionsabgabe, Quasifusion, Wandlungskapital) sind vollständig durchgesehen; die grossen, unscharfen Treffermengen nur in den ersten 150 Treffern. Über alle Wege ergab sich kein einschlägiger Entscheid, der nicht spätestens auf dem dritten Weg schon erfasst war.

### Fassungshinweise

- **lit. a** (gemeinnützige und ähnliche Gesellschaften): seit dem StG 1973; Vorläufer Art. 1 Abs. 2 ErgStG 1937 (gemeinnützige GmbH/Genossenschaften; erwähnt in BGE 97 I 438 E. 2). Keine Auslegungsrechtsprechung.
- **lit. abis** (Umstrukturierungen): eingefügt mit der Revision vom 4.10.1991, in Kraft 1.4.1993; Wortlaut an das FusG angepasst, in Kraft 1.7.2004. Vorgänger: Art. 9 Abs. 1 lit. a StG 1973 (bis 31.3.1993) sah für dieselben Vorgänge keinen Ausnahmetatbestand, sondern einen ermässigten Satz vor (1 % statt 2 %/3 %). Das StG 1917 kannte keine Fusionsentlastung (BGE 61 I 285). Die Begriffe «Fusion» und «wirtschaftlich gleichkommender Zusammenschluss» hat das Bundesgericht unter Art. 9 aStG gebildet (BGE 102 Ib 140) und unter lit. abis weitergeführt (2C_976/2014 E. 3.2).
- **lit. d** (frühere Aufgelder und Zuschüsse): seit dem StG 1973 unverändert (Wortlaut zitiert in BGE 105 Ib 175 E. 3).
- **lit. e** (aufgehoben mit Wirkung seit 1.4.1993) und **lit. f** (ABRG 1988 bis 2018), **lit. m** (2016 bis 2022): keine Bundesgerichtsentscheide gefunden; der Inhalt der alten lit. e ist am Normtext 1973 (AS 1974 11) zu prüfen.
- **lit. g** (Partizipations-/Beteiligungskapital): eingefügt mit der Aktienrechtsrevision vom 4.10.1991, in Kraft 1.7.1992; Beteiligungskapital der Genossenschaftsbanken seit 1.1.2020 (FINIG). Vorher Doppelbelastung bei Umwandlung von PS in Aktien (BGE 105 Ib 175).
- **lit. h** (Freibetrag 1 Mio. bei AG/KAG/GmbH): eingefügt 24.3.1995, geltende Fassung seit 1.1.2006.
- **lit. b, j, k** (Genossenschaften 1 Mio.; Übernahme von Betrieben notleidender Gesellschaften; Sanierungsfreibetrag 10 Mio.): USTR II, in Kraft 1.1.2009; nicht anwendbar auf frühere Sachverhalte (BGer 2C_1001/2014 E. 5; BGer 2C_1095/2015 E. 5.3.5).
- **lit. i** (kollektive Kapitalanlagen): KAG, in Kraft 1.1.2007. Vorher unterlagen Anteile an Anlagefonds der Emissionsabgabe (StG 1917 Art. 48; BGE 98 Ib 197).
- **lit. ater, c, l** und **Abs. 2**: keine Bundesgerichtsentscheide.

## 1. Tabelle

| Entscheid (Zitierstring) | Datum | Besetzung | Normstelle (lit.) | Sachfrage | Kernaussage (ein Satz, am Text) | E. | Ergebnis | Klasse | Fassung |
|---|---|---|---|---|---|---|---|---|---|
| BGE 149 II 462 (= BGer 9C_610/2022 vom 7. September 2023) | 07.09.2023 | Fünferbesetzung (Parrino, Stadelmann, Moser-Szeless, Beusch, Scherrer Reber) | lit. k (Verhältnis zu Art. 12 und Art. 5 Abs. 1bis VStG) | Sanierungsfreibetrag bei Debt-Equity-Swap mit Agio: Erfordernis der «Beseitigung bestehender Verluste» | Der Freibetrag von 10 Mio. Franken setzt die tatsächliche Ausbuchung des Verlustvortrags im Zeitpunkt der Verbuchung der Sanierungsmassnahme voraus; wer das Agio den Kapitaleinlagereserven gutschreibt und erst später ausbucht, verwirkt den Anspruch. | 2.3.3, 3.3.1–3.3.7, 3.4.1–3.4.2 (Rechtsweg Erlass: 1.2) | Beschwerde der ESTV gutgeheissen | A | StG ab 2009 (Swap 21.9.2015) |
| BGer 2C_1071/2018 vom 12. November 2019 | 12.11.2019 | Dreierbesetzung (Seiler, Donzallaz, Stadelmann) | lit. abis; lit. h | (1) Aktiendividende nach Quasifusion als Teil eines einheitlichen Umstrukturierungsvorgangs? (2) Charakter des Betrags von 1 Mio. Franken | (1) Eine Kapitalerhöhung fällt nur unter lit. abis, wenn sie mit der Quasifusion zeitlich und sachlich so eng zusammenhängt, dass ein einheitlicher Umstrukturierungsvorgang vorliegt; (2) lit. h ist ein Freibetrag, keine Freigrenze, und kann insgesamt nur einmal verbraucht werden. | 4.1–4.3; 6 | Beschwerde der ESTV teilweise gutgeheissen (Freibetrag verneint; Bemessung auf Nennwert) | A | StG ab 2009 (Ausgabe Mai 2015) |
| BGer 2C_976/2014 vom 10. Juni 2015 | 10.06.2015 | Dreierbesetzung (Zünd, Aubry Girardin, Haag) | lit. abis | Begriff der Quasifusion; Einbringung einer 50 %-Beteiligung zum Nennwert durch den Alleinaktionär | Eine Quasifusion bedingt immer eine Kapitalerhöhung bei der übernehmenden Gesellschaft unter Ausschluss der Bezugsrechte und einen Aktientausch; die Praxis der ESTV (KS 5: mindestens 50 % der Stimmrechte, höchstens 50 % bar) ist massgebend. | 3.1–3.7, 4.1–4.4 | Beschwerde der Gesellschaft abgewiesen | A | StG 2004–2008 (FusG-Fassung; Verkauf 15.6.2007) |
| BGer 2C_1001/2014 vom 10. August 2015 | 10.08.2015 | Dreierbesetzung (Zünd, Donzallaz, Haag) | lit. abis; lit. j, k (intertemporal) | Quasifusion mit ausländischen Beteiligungen: Kapitalerhöhung weit über dem nominellen Kapital der übernommenen Gesellschaften durch eine notleidende Gesellschaft | Liegt bei der Quasifusion eine Abgabeumgehung vor (Kapitalerhöhung «à discrétion» ohne plausibles Austauschverhältnis), ist der Vorgang nicht als fusionsähnlicher Zusammenschluss anzuerkennen; lit. j und k gelten erst seit der USTR II. | 3.1–3.7, 4.1–4.6, 5 | Beschwerde der ESTV gutgeheissen | A | StG 2004–2008 (FusG-Fassung; Vorgang vor 2009) |
| BGer 2C_447/2018 vom 12. März 2019 | 12.03.2019 | Dreierbesetzung (Zünd, Aubry Girardin, Haag) | lit. abis (iVm Art. 5 Abs. 2 lit. a) | Verkauf von Beteiligungen unter Wert durch den Alleinaktionär an seine Gesellschaft ohne Kapitalerhöhung | Ohne Kapitalerhöhung und Austausch von Beteiligungsrechten liegt keine Quasifusion vor, auch wenn dem Bezugsrechtsausschluss beim Alleinaktionär materiell keine Bedeutung zukommt; von dieser «klaren Rechtsprechung» abzuweichen besteht kein Anlass. | 4.1–4.4 | Beschwerde der Gesellschaft abgewiesen | A | StG ab 2009 (Käufe 2012) |
| BGer 2A.83/2001 vom 5. März 2002 | 05.03.2002 | Fünferbesetzung (Wurzburger, Hungerbühler, Müller, Yersin, Merkli) | Art. 9 Abs. 1 lit. a aStG (Vorgänger lit. abis) | Aufstockung einer bereits über 66⅔ % liegenden Beteiligung durch Umtauschangebot: nochmals fusionsähnlicher Zusammenschluss? | Der fusionsähnliche Zusammenschluss ist ein wirtschaftlicher Begriff; das Privileg ist nicht nur einmal beim Überschreiten der Zweidrittelsschwelle zu gewähren, sondern auch bei der Aufstockung auf höhere Schwellen, wenn sie die Beherrschung und Wettbewerbsfähigkeit verstärkt. | 2.2–2.3, 4.1–4.5 | Beschwerde der ESTV abgewiesen | A | StG 1973 vor 1993 (Umtausch Juni 1991) |
| BGer 2A.84/2001 vom 5. März 2002 | 05.03.2002 | Fünferbesetzung (Wurzburger, Hungerbühler, Müller, Yersin, Merkli) | Art. 9 Abs. 1 lit. a aStG (Vorgänger lit. abis) | wie 2A.83/2001 (Parallelverfahren, andere Gesellschaft) | wie 2A.83/2001 (gleiche Erwägungen; wird in 2C_976/2014 E. 3.2 für die wirtschaftliche Betrachtung zitiert). | 2.2, 4.4 | Beschwerde der ESTV abgewiesen | A | StG 1973 vor 1993 (1991) |
| BGE 115 Ib 125 | 16.06.1989 | nicht ersichtlich | Art. 9 Abs. 1 lit. a aStG (Vorgänger lit. abis: Umwandlung, Aufspaltung) | Umwandlung einer von einer AG beherrschten Kommanditgesellschaft in eine AG | Der Vorzugssatz erfasst nur Umwandlungen und Aufspaltungen der im Gesetz genannten Gesellschaftsformen; die Umwandlung einer KG fällt nicht darunter, auch nicht als Aufspaltung der beherrschenden AG. | 2a–2b, 3 | Beschwerde abgewiesen | A | StG 1973 vor 1993 |
| BGE 102 Ib 140 | 14.05.1976 | nicht ersichtlich | Art. 9 Abs. 1 lit. a aStG (Vorgänger lit. abis) | Begriff des einer Fusion wirtschaftlich gleichkommenden Zusammenschlusses (Holdinggründung durch Einbringung von Aktienmehrheiten) | Ein Zusammenschluss kommt einer Fusion wirtschaftlich gleich, wenn er nicht in den Formen von Art. 748 ff. OR erfolgt, aber die gleichen Wirkungen hat und die Gründe der Privilegierung auch auf ihn zutreffen; massgebend ist die Intensität der Verbindung, gemessen an den Beherrschungsverhältnissen (mindestens zwei Drittel der Stimmen). | 2, 3a–3b, 4, 5 | Beschwerde teilweise gutgeheissen | A | StG 1973 vor 1993 |
| BGE 105 Ib 175 | 02.03.1979 | nicht ersichtlich | lit. d; Ausnahmen allgemein (abschliessende Aufzählung) | Umwandlung von Partizipationsscheinen in Aktien: Befreiung als Verwendung früherer «Zuschüsse»? | Die Ausnahmen von Art. 6 Abs. 1 sind abschliessend; «Zuschüsse» (versements) in lit. d sind nur zusätzliche Leistungen im Sinn von Art. 5 Abs. 2 lit. a, nicht der Nennwert früher ausgegebener PS, und lit. d will die Doppelbelastung bei späterer Umwandlung von Agio und Zuschüssen in Kapital vermeiden. | 2a, 3 | Beschwerde abgewiesen | A | StG 1973 vor 1993 (Umwandlung 1975; heute lit. g) |
| BGer 2A.618/1998 vom 7. Februar 2000 | 07.02.2000 | Fünferbesetzung (Wurzburger, Hartmann, Hungerbühler, Müller, Yersin) | lit. g | Umwandlung von abgabefrei gebildetem Partizipationskapital (Liechtensteinische Landesbank) in Aktienkapital | Die Ausnahme nach lit. g greift nach dem klaren Wortlaut nur, wenn auf dem umgewandelten Partizipationskapital die Emissionsabgabe tatsächlich bezahlt worden ist, nicht bei steuerbefreit gebildetem PS-Kapital. | 2a, 4a | Beschwerde abgewiesen | A | StG ab 1.7.1992 (lit. g); Umwandlung 7.5.1993 |
| BGer 2A.225/1999 vom 31. Januar 2000 | 31.01.2000 | Fünferbesetzung (Wurzburger, Betschart, Hungerbühler, Müller, Yersin) | lit. g | Umwandlung von Dotations- in Zertifikatskapital einer Kantonalbank | lit. g schliesst seit 1992 die nochmalige Abgabe bei Umwandlung von bereits belastetem PS-Kapital aus, lässt die Praxis zur Begründung neuer Beteiligungsrechte im Übrigen unberührt. | 2 | Beschwerde abgewiesen | B | StG 1993–2007 |
| BGer 2C_621/2018 vom 10. August 2018 | 10.08.2018 | Dreierbesetzung (Seiler, Zünd, Aubry Girardin) | lit. k (Abgrenzung Art. 12) | Rückwirkender Forderungsverzicht; Freibetrag 10 Mio. von der ESTV gewährt; Anfechtbarkeit | Entscheide über die Abgabebefreiung nach Art. 6 Abs. 1 StG sind mit Beschwerde in öffentlich-rechtlichen Angelegenheiten anfechtbar, Entscheide über Erlass und Stundung (Art. 12) nicht. | 1.3, 2.2, 3.3 | Beschwerde abgewiesen, soweit eingetreten | B | StG ab 2009 (Verzicht 2010) |
| BGer 2C_1095/2015 vom 27. Mai 2016 | 27.05.2016 | – | lit. k (intertemporal) | Forderungsverzicht 2007 | Obiter: lit. k ist erst seit 1.1.2009 in Kraft und auf einen Zuschuss von 2007 nicht anwendbar (mit Verweis auf 2C_1001/2014 E. 5). | 3.3, 5.3.5 | – | C | StG 1993–2007 |
| BGer 9C_232/2026 vom 10. September 2026 | 10.09.2026 | – | lit. h | Mantelhandel: Bemessung | Der Freibetrag von 1 Mio. Franken wird von der Bemessung abgezogen; unbestritten, keine Erwägung dazu. | Sachverhalt A.b–A.d, 3 | – | C | StG ab 2009 |
| BGE 148 II 121 (= BGer 2C_624/2021 vom 28. März 2022) | 28.03.2022 | – | lit. i (Motiv) | Handänderungsabgabe beim Wechsel der Fondsleitung | Zitiert die Botschaft KAG, wonach ohne Gesetzesänderung die Ausgabe von SICAV-Anteilen der Emissionsabgabe unterläge. | 7.5 | – (kantonale Handänderungsabgabe) | C | KAG ab 2007 |
| BGE 114 Ib 277 | 28.10.1988 | – | lit. a | Steuerbefreiung einer Stiftung zur Wohnbauförderung (BdBSt) | Erwähnt, dass Art. 6 Abs. 1 lit. a StG Gesellschaften zur Beschaffung von Wohnungen zu mässigen Mietzinsen ausdrücklich von der Emissionsabgabe befreit, anders als das BdBSt. | 3d | – (BdBSt) | C | StG 1973 vor 1993 |
| BGE 97 I 438 | 11.06.1971 | – | lit. a (Vorläufer), lit. d (Vorläufer) | Leistungen von GmbH-Gesellschaftern (ErgStG) | Nennt die Ausnahmen von Art. 1 Abs. 1 lit. b und Abs. 2 ErgStG (Nachschüsse nach Art. 803 OR, Beteiligungen an gemeinnützigen Gesellschaften) als nicht anwendbar. | 2 | – | C | ErgStG 1937 |
| BGE 98 Ib 197 | 13.10.1972 | – | lit. i (Vorgeschichte) | Emissionsabgabe auf Anteilen an Anlagefonds oder «Vermögen ähnlicher Art» (Art. 48 StG 1917) | Abgrenzung Anlagefonds / Investment-Club für die damals abgabepflichtigen Fondsanteile. | 1 ff. | – | C | StG 1917 |
| BGE 61 I 285 | 16.07.1935 | – | lit. abis (Vorgeschichte) | Emissionsabgabe bei Absorptionsfusion | Unter dem StG 1917 war die Kapitalerhöhung der übernehmenden Gesellschaft bei einer Fusion voll abgabepflichtig; eine Ausnahme aus den Materialien abzuleiten lehnte das Gericht ab. | 1a | Beschwerde abgewiesen | C | StG 1917 |
| BGE 55 I 321 | 21.11.1929 | – | lit. k (Vorgeschichte) | Wiedererhöhung des Nennwerts aus Sanierungsreserve | Unter dem StG 1917 war auch die Wiedererhöhung nach Sanierung abgabepflichtig (heute lit. k). | 1 | Beschwerde abgewiesen | C | StG 1917 |

Zählung: 21 Einträge (A 11, B 2, C 8). Nach lit.: abis 8 A (davon 4 zu Art. 9 Abs. 1 lit. a aStG), 1 C; k 1 A, 1 B, 1 C (+ 2C_1001/2014 E. 5, + BGE 55 I 321 C); h 1 A (2C_1071/2018 E. 6), 1 C; d 1 A; g 1 A, 1 B; a 2 C; i 2 C; ater, b, c, j (nur intertemporal in 2C_1001/2014), l, Abs. 2: keine. Zusammengeführt: BGE 149 II 462 = BGer 9C_610/2022; BGE 148 II 121 = BGer 2C_624/2021. 2A.83/2001 und 2A.84/2001 sind Parallelurteile, getrennt aufgeführt.

## 2. Tragende Sätze der A-Entscheide (wörtlich)

Quelle: Cache-Volltext bzw. `get_erwaegung` (Open Case Law). Ältere Texte können OCR-Fehler enthalten; vor Veröffentlichung am amtlichen Druck prüfen.

### BGE 149 II 462 (= BGer 9C_610/2022 vom 7. September 2023)

E. 2.3.3: «Die bei einer offenen Sanierung vorgenommene Begründung von Beteiligungsrechten oder die (Wieder-)Erhöhung deren Nennwerts bis zur Höhe vor der Sanierung sowie Zuschüsse von Gesellschaftern oder Genossenschaftern bei stillen Sanierungen sind gemäss Art. 6 Abs. 1 lit. k StG von der Emissionsabgabe ausgenommen, soweit a. bestehende Verluste beseitigt werden, und [Seitenwechsel S. 469] b. die Leistungen der Gesellschafter oder Genossenschafter gesamthaft zehn Millionen Franken nicht übersteigen. Hier streitig ist einzig die "Beseitigung bestehender Verluste". Dazu liegt keine vertiefende bundesgerichtliche Rechtsprechung vor.»

E. 3.3.6: «Sinn und Zweck der Norm (teleologisches Auslegungselement) erschliessen sich im Rahmen einer Gesamtbetrachtung. Mit der Norm verfolgt der Gesetzgeber die Absicht, die ansonsten anfallende Emissionsabgabe dann nicht entstehen zu lassen, wenn die Kapitalzufuhr anlässlich einer offenen oder stillen Sanierung erfolgt.» – «Indem der Gesetzgeber die Bedingung der "Verlustbeseitigung" schuf, hat er mit anderen Worten eine Erwartung verbunden. Diese geht dahin, dass der Verlustvortrag auch tatsächlich ausgebucht wird, ansonsten die Bedingung sinnlos bliebe.» (zweiter Satzteil nach dem Text von BGer 9C_610/2022; am BGE-Druck prüfen)

E. 3.4.1: «Zusammenfassend zeigt sich, dass Art. 6 Abs. 1 lit. k StG - neben den beiden hier unstrittigen Elementen (Sanierung, Leistung von höchstens zehn Millionen Franken; vorne E. 2.3.3) - in buchungstechnischer Hinsicht die tatsächliche Ausbuchung des Verlustvortrags erfordert. […] Sachlogisch ergibt sich daraus, dass dies in zeitlicher Hinsicht in jenem Zeitpunkt zu geschehen hat, in welchem die Sanierungsmassnahme zu verbuchen ist.»

E. 3.4.2: «Im Lichte der getroffenen Auslegung stellt sich Art. 6 Abs. 1 lit. k StG als das speziellere Recht dar. Dieses geht der allgemeineren Norm vor.»

Hinweis: E. 3.3.4 hält fest, der Bundesrat habe lit. k als «zusätzliche emissionsabgaberechtliche Ausnahme» neben Art. 12 verstanden; E. 3.3.5 bezeichnet lit. k als «zusätzliche, weitestgehend eigenständige Ausnahme von der Bemessungsgrundlage». E. 1.2: Erlassentscheide (Art. 12) des BVGer sind letztinstanzlich.

### BGer 2C_1071/2018 vom 12. November 2019

E. 4.3: «Vor diesem Hintergrund könnte überhaupt nur dann von einer "Quasifusion" die Rede sein, wenn zwischen der Auszahlung der Aktiendividende im Jahr 2015 und dem unbestrittenermassen als "Quasifusion" zu qualifizierenden Aktienumtausch im Jahr 2014 ein derart enger Zusammenhang bestehen würde, dass von einem einheitlichen Umstrukturierungsvorgang gesprochen werden müsste, auf den Art. 6 Abs. 1 lit. a bis StG integral zur Anwendung gelangt.»

E. 4.3: «Eine solche Auslegung entspräche offensichtlich nicht dem Sinn und Zweck von Art. 6 Abs. 1 lit. abis StG, Kapitalbeschaffungen im Zusammenhang mit oftmals unter dem Druck wirtschaftlicher Notwendigkeit erfolgenden Umstrukturierungen zu entlasten (vgl. Urteil 2C_1001/2014 vom 10. August 2015 E. 3.2, mit Hinweis auf die Materialien).»

E. 6: «Tatsächlich handelt es sich bei Art. 6 Abs. 1 lit. h StG entgegen der Annahme der Vorinstanz nicht um eine Freigrenze, sondern um einen Freibetrag, der insgesamt nur einmal "verbraucht" werden kann (vgl. NORDIN/WILD, a.a.O., N. 1c zu Art. 6 StG).»

Hinweis: E. 4.1 fasst die Quasifusionspraxis zusammen (mindestens 50 % der Stimmrechte, höchstens 50 % bar, Kapitalerhöhung unter Bezugsrechtsausschluss als Voraussetzung «von der bundesgerichtlich bestätigten Verwaltungspraxis»).

### BGer 2C_976/2014 vom 10. Juni 2015

E. 3.1: «Die Vorschrift bezweckt, Kapitalbeschaffungen im Zusammenhang mit Umstrukturierungen, die oftmals unter dem Druck wirtschaftlicher Notwendigkeit erfolgen, steuerlich zu entlasten (Bericht der Kommission des Nationalrates vom 16. September 1991, BBl 1991 IV 516 Ziff. 42).»

E. 3.2: «Es handelt sich bei den fusionsähnlichen Zusammenschlüssen um wirtschaftliche Vorgänge, weshalb eine wirtschaftliche Betrachtungsweise Platz greifen muss (Urteil 2A.84/2001 vom 5. März 2002 E. 2.2, 4.4, in: ASA 72 S. 170, StR 57/2002 S. 577, RDAF 2002 II 361).»

E. 3.4: «Eine Quasifusion bedingt somit immer eine Kapitalerhöhung bei der übernehmenden Gesellschaft unter Ausschluss der Bezugsrechte der bisherigen Gesellschafter und einen Aktientausch bei den Gesellschaftern der übernommenen Gesellschaft (vgl. Kreisschreiben Nr. 5, Ziff. 4.1.7.1; Ludwig/Tarolli Schmidt, in: Zürcher Kommentar zum Fusionsgesetz, 2. Aufl. 2012, Anhang Steuern [Fusion] N. 79 S. 1240).»

E. 4.2: «Die Kapitalerhöhung und Ausgabe neuer Beteiligungsrechte ist daher kein bloss formales Kriterium, sondern die Voraussetzung dafür, dass auf der Beteiligungsebene eine wirtschaftliche Verflechtung der beteiligten Unternehmen stattfinden kann.»

Hinweis: E. 3.6 übernimmt die Schwellen des KS 5 (Ziff. 4.1.7.1) und hält sie im Vergleich zur EU-Fusionsrichtlinie nicht für zu streng; E. 3.7: «Diese Praxis ist auch im Falle der Beschwerdeführerin massgebend.»

### BGer 2C_1001/2014 vom 10. August 2015

E. 3.4: «Daher bedingt eine Quasifusion eine Kapitalerhöhung bei der übernehmenden Gesellschaft unter Ausschluss der Bezugsrechte der bisherigen Gesellschafter und einen Aktientausch bei den Gesellschaftern der übernommenen Gesellschaft […]. Ob und in welchem Umfang eine Kapitalerhöhung der übernehmenden Gesellschaft zulässig und notwendig ist, bestimmen nicht die Steuergesetze, sondern ist nach Massgabe von Art. 7 und 8 FusG zu beurteilen.»

E. 3.4 (a.E.): «In steuerrechtlicher Hinsicht gilt das Verbot der Steuer- oder Abgabeumgehung. Diese Grundsätze können analog auch bei fusionsähnlichen Tatbeständen berücksichtigt werden.»

E. 4.6: «Da alle Voraussetzungen der Steuerumgehung erfüllt sind, kann das Vorgehen der Beschwerdegegnerin nicht als ein fusionsähnlicher Zusammenschluss anerkannt werden (Art. 6 Abs.1 lit. a bis StG) und ist die Emissionsabgabe geschuldet.»

E. 5: «Nicht zu prüfen sind die Ausnahmen von der Abgabe gemäss Art. 6 Abs. 1 lit. j und k StG , da diese erst mit der Unternehmenssteuerreform II eingeführt wurden und auf den vorliegenden Fall noch keine Anwendung finden.»

Hinweis: E. 3.6 gibt die Sonderregel des KS 5 für ausländische Beteiligungen (Kapitalerhöhung in der Regel bis 30 % des Verkehrswerts befreit) wieder; E. 4.6 benutzt sie als Indiz der Umgehungsabsicht.

### BGer 2C_447/2018 vom 12. März 2019

E. 4.3: «Soll eine Quasifusion trotz Selbständigkeit der betroffenen Gesellschaften einen wirtschaftlichen Zusammenschluss derselben bewirken, ist erforderlich, dass Beteiligungsrechte ausgetauscht werden. An diesem Erfordernis ist auch festzuhalten, wenn die neuen Beteiligungsrechte von B.________ in seiner Funktion als Aktionär der übernommenen Gesellschaften erworben würden.»

E. 4.3: «Es besteht kein Anlass, von dieser klaren Rechtsprechung abzuweichen. Zwar mag es zutreffen, dass dem Ausschluss der Bezugsrechte der bisherigen Gesellschafter der übernehmenden Gesellschaft im Falle, dass der Verkäufer der Stammanteile wie vorliegend Alleinaktionär der übernehmenden Gesellschaft ist, letztlich materiell keine Bedeutung zukommt. Dies ändert indes nichts daran, dass ein fusionsähnlicher Zusammenschluss eine enge Verflechtung der Gesellschaften erfordert, wofür praxisgemäss eine Kapitalerhöhung verlangt wird.»

E. 4.4: «Nach dem Gesagten qualifizierte die Vorinstanz die vorliegend zur Diskussion stehenden Beteiligungskäufe durch die Beschwerdeführerin mangels Kapitalerhöhung berechtigterweise nicht als Quasifusion und gelangte folgerichtig zum Schluss, die Zuschüsse seien von der Emissionsabgabe nicht ausgenommen.»

### BGer 2A.83/2001 vom 5. März 2002 (gleichlautend BGer 2A.84/2001 vom 5. März 2002)

E. 2.2: «L'Administration fédérale ne saurait se laisser guider pour ce motif par une vision économique des opérations, à l'exception toutefois des cas dans lesquels la loi utilise elle-même des notions à contenu économique telles que celle de "manteau d'actions" décrite par l' art. 5 al. 2 lettre b LT ou celle de "concentration équivalant économiquement à une fusion" (arrêt du Tribunal fédéral du 5 février 1996 in: Archives 65, p. 666 consid. 3a p. 668/669).»

E. 4.1: «Dans ces deux arrêts, le Tribunal fédéral a souligné que le but du privilège fiscal de l' art. 9 al. 1 lettre a LT (nouvellement art. 6 al. 1 lettre a bis LT), voulu par le législateur, consistait à alléger les fusions des entreprises de façon à accroître leur capacité concurrentielle, avant tout à l'endroit de la concurrence étrangère, et à la maintenir, les fusions ayant le plus souvent lieu sous la pression urgente de l'économie, en favorisant la concentration de domaines d'activités qui resteraient sinon séparés et ne bénéficieraient pas d'économies de moyens.»

E. 4.4: «L'Administration fédérale ne saurait par conséquent sérieusement soutenir que l'effet analogue à une fusion, recherché lors de la concentration d'entreprises, ne peut être atteint qu'une fois, lorsque le seuil de 66 2/3% des droits de vote - résultant des dispositions du droit de la société anonyme en vigueur en 1991 - est franchi et non lorsque des seuils supérieurs, permettant à la société d'asseoir sa position, en particulier au regard de nouvelles exigences législatives, sont atteints […].»

Hinweis: E. 4.1 referiert ein nicht im Korpus enthaltenes Urteil vom 12. Dezember 1997 (Revue fiscale 53/1998 358): Das Privileg setzt wirtschaftlich aktive Gesellschaften voraus; die Einbringung von Aktien einer reinen Liquiditätsgesellschaft genügt nicht.

### BGE 115 Ib 125

E. 2a: «Es sollten damit Fusionen und gleichgestellte Tatbestände weder über Gebühr erleichtert noch erschwert werden (Botschaft des Bundesrates vom 25. Oktober 1972, BBl 1972 II S. 1278, 1284, 1294 ff.; dazu BGE 102 Ib 144 f. E. 3b; ASA 53, 275 E. 3a).»

E. 2b: «Art. 9 Abs. 1 lit. a StG nennt allerdings nur Fusionen und diesen gleichkommende Umwandlungen, Aufspaltungen usw. von Aktiengesellschaften, Kommanditaktiengesellschaften, Gesellschaften mit beschränkter Haftung und Genossenschaften. […] Umwandlungen von Kommanditgesellschaften fallen deshalb nicht unter Art. 9 Abs. 1 lit. a StG .»

Hinweis: E. 3 verneint, dass die Umwandlung der KG als privilegierte Aufspaltung der zu 96,4 % beteiligten AG gelten kann (laut Regeste). Der Gesellschaftskreis in lit. abis ist bis heute gleich (AG, KAG, GmbH, Genossenschaft).

### BGE 102 Ib 140

E. 3a: «Wirtschaftlich kommt der Zusammenschluss von Aktiengesellschaften einer Fusion gleich, wenn er zwar aus irgendwelchen Gründen nicht in einer der Formen nach Art. 748 ff. OR erfolgt, aber wirtschaftlich die gleichen Wirkungen hat wie eine Fusion und ausserdem die Gründe, die zur steuerlichen Privilegierung der Fusion führen, auch auf einen solchen Zusammenschluss zutreffen.»

E. 3b: «Es rechtfertigt sich daher zwar, an die aus einem solchen Zusammenschluss zu erwartenden Wirkungen keinen strengeren Massstab anzulegen als gegenüber den eigentlichen Fusionen; indes setzt aber die Annahme eines fusionsgleichen Zusammenschlusses doch stets voraus, dass die Intensität der Verbindung rechtlich und tatsächlich nicht völlig integrierter Gesellschaften jener einer eigentlichen Fusion praktisch gleichkommt.»

E. 5: «Doch sind die Gründe, weshalb die Fusion unterbleibt und die Beteiligten sich für einen wirtschaftlich fusionsgleichen Zusammenschluss entscheiden, hinsichtlich der steuerlichen Behandlung des Zusammenschlusses nicht ausschlaggebend. Es kommt vielmehr auf die tatsächliche Intensität der Verbindung an, die sich an den Beherrschungsverhältnissen misst.»

Hinweis: Die Zweidrittelsschwelle (E. 5 a.E.) hat die Praxis seit dem FusG durch 50 % ersetzt (vgl. 2C_976/2014 E. 3.6, 4.4).

### BGE 105 Ib 175

E. 2a: «Seuls font exception les droits de participation énumérés limitativement à l'art. 6 al. 1 LT.»

E. 3: «Cependant, il faut se garder de confondre les versements dont parle l'art. 6 al. 1 lettre d LT et ceux dont il est question à l'art. 5 al. 2 lettre a LT. […] Il apparaît dès lors qu'en concédant l'exonération prévue par l'art. 6 al. 1 lettre d LT, le législateur a voulu éviter une double imposition lorsque l'agio qui a normalement été frappé du droit lors de l'émission des titres de participation au-dessus du pair, ou un versement supplémentaire lors de son exécution, viennent à être incorporés au capital social […].»

E. 3: «Par versements supplémentaires au sens de l'art. 6 al. 1 lettre d LT, il faut entendre, par exemple, ceux que les associés de la société à responsabilité limitée ou les membres de la société coopérative seront appelés à effectuer, selon les statuts dans la mesure nécessaire pour éteindre des pertes constatées par le bilan (art. 803; 871 CO) […].»

### BGer 2A.618/1998 vom 7. Februar 2000

E. 2a: «Ausgenommen sind jene Beteiligungsrechte, welche unter Verwendung von Partizipationskapital begründet oder erhöht werden, falls die Gesellschaft nachzuweisen vermag, dass sie die Abgabe auf diesem Kapital bereits entrichtet hat (Art. 6 Abs. 1 lit. g StG [eingefügt am 4. Oktober 1991, in Kraft seit 1. Juli 1992]).»

E. 4a: «Zu Recht stützt die Beschwerdeführerin ihre Argumentation nicht auf Art. 6 lit. g StG : Die Ausnahme kommt nur dann zum Tragen, wenn auf dem umgewandelten Partizipationskapital bereits Emissionsabgaben bezahlt worden sind; nicht erfasst wird nach dem klaren Wortlaut Partizipationskapital, das - aus welchen Gründen auch immer - steuerbefreit gebildet werden konnte.»

## 3. Fehltreffer

Aus der Cache-Kandidatenliste (normen «StG/6»):
- BGE 86 I 10: Art. 6 Abs. 1 und 2 des st. gallischen Steuergesetzes (Wohnsitz, Aufenthalt von mehr als drei Monaten).
- BGer 2C_254/2022 vom 27. Dezember 2022: Art. 6 Abs. 2 StG/GR (steuerlicher Wohnsitz; Grundstückgewinnsteuer).
- BGer 2P.188/2005 vom 12. Mai 2006: art. 6 cpv. 2 LIFD (beschränkte Steuerpflicht).
- BGer 9C_646/2022 vom 7. Februar 2023: art. 6 cpv. 1 LIFD und art. 6 cpv. 1 LT/TI (Steuerpflicht, Liegenschaften im Ausland).
- Im Cache unter normen «StG/67»/«StG/68» (Präfixtreffer, nicht Art. 6): BGer 2C_26/2007, 2C_681/2020 (Art. 6 GGS/SG), 2C_821/2010.

Aus `find_leading_cases`:
- BGE 73 I 125: Art. 6 StG 1917 (Überwachung der Abgabepflicht, Couponabgabe), kein Ausnahmetatbestand.
- BGE 75 I 225: rechtliches Gehör im kantonalen Steuerverfahren.

Aus dem Volltext-Scan (Art. 6 anderer Erlasse oder Emissionsabgabe in anderem Sinn):
- BGer 2A.40/2007, 2C_632/2007, BGE 148 II 233: Art. 6 Abs. 1 lit. a MWSTGV.
- BGer 2P.34/2006: art. 6 LT/TI (beschränkte Steuerpflicht).
- BGer 2C_510/2018, 2C_748/2018: Art. 6 Abs. 1 lit. e/f StG/BE.
- BGer 2C_643/2017: Art. 6 Abs. 1 lit. f HG/VS.
- BGer 2C_121/2020: art. 6 al. 1 let. c LAAF.
- BGer 9C_342/2024: Art. 6 Abs. 2 StGB/StPO.
- BGE 125 I 182, BGE 124 II 293: «Emissionsabgabe» als Lärm-/Schadstoffabgabe am Flughafen.
- BGE 97 I 450, BGer 2C_299/2021, 2C_995/2011: Obligationen-Emissionsabgabe (Art. 4/5a StG), kein Art. 6.
- BGer 2C_374/2021: Erlass der Emissionsabgabe (Art. 12 StG), nur Rechtsweg.
- BGer 2C_578/2019, 2A.299/2004, 2A.300/2004: Verrechnungssteuer (Partizipationskapital nur im Sachverhalt).
- BGer 9C_381/2025: erwähnt frühere Stempelabgabeurteile nur zur Bindung kantonaler Behörden.
- BGer 2A.135/2000: Quasifusion im Recht der direkten Bundessteuer (in 2C_976/2014 E. 3.4 zitiert), keine Emissionsabgabe.
- BGE 114 Ib 277, 97 I 438, 98 Ib 197, 148 II 121 sind keine Fehltreffer, sondern als C aufgenommen.

## 4. Lücken und Hinweise

- Nicht im Korpus von Open Case Law (geprüft, nicht gefunden): BGer 2A.17/1994 vom 5. Februar 1996 (ASA 65 S. 666; wirtschaftliche Betrachtung beim fusionsähnlichen Zusammenschluss, in 2C_976/2014 E. 3.2 und 2A.83/2001 E. 2.2 zitiert) und BGer 2A.107/1999 vom 23. September 1999. Nicht geprüft (nur in Zeitschriften): Urteil vom 12. Dezember 1997 (Revue fiscale 53/1998 358; wirtschaftlich aktive Gesellschaften als Voraussetzung des Fusionsprivilegs), ASA 53, 156 (Umwandlung einer KG, Urteil vom 11. April 1984) und ASA 53, 275 (Zweck des Vorzugssatzes), ASA 46 S. 538/542 (PS-Umwandlung). Diese Fundstellen sind für die Kommentierung am Original zu prüfen.
- Keine Bundesgerichtsrechtsprechung gefunden zu: lit. a (Begriff der Gemeinnützigkeit, Statutenerfordernisse, Wohnbau- und Bürgschaftsgenossenschaften), lit. ater, lit. b (Genossenschaften), lit. c (Transportunternehmen), lit. i (kollektive Kapitalanlagen), lit. j (Übernahme von Betrieben notleidender Gesellschaften), lit. l (Wandlungskapital), Abs. 2 (Wegfall der Befreiungsvoraussetzungen), Spaltungen und Umwandlungen nach FusG unter lit. abis.
- lit. abis: Die Voraussetzungen der Quasifusion (50 %-Schwelle, 50 % Barabgeltung, 30 %-Regel bei ausländischen Beteiligungen) beruhen auf dem KS 5 der ESTV; das Bundesgericht hat sie bestätigt (2C_976/2014 E. 3.6–3.7; 2C_1071/2018 E. 4.1), aber nicht aus dem Gesetz abgeleitet. Die Rechtsprechung zur Zweidrittelsschwelle (BGE 102 Ib 140, 2A.83/2001) betrifft den Vorzugssatz des alten Rechts.
- 2C_976/2014 E. 3.2 (wirtschaftliche Betrachtung, gestützt auf 2A.84/2001) und 2C_447/2018 E. 4.3 (Kapitalerhöhung als zwingendes formelles Erfordernis auch beim Alleinaktionär) stehen in Spannung; der Autor sollte das Verhältnis darstellen.
- Die Entscheide aus der Zeit vor 1993 (BGE 102 Ib 140, 115 Ib 125, 2A.83/2001, 2A.84/2001) betreffen einen ermässigten Satz, nicht eine Befreiung; ihre Übertragbarkeit auf lit. abis wird in 2C_976/2014 E. 3.1–3.2 und 2C_1001/2014 E. 3.1–3.2 bejaht (Verweis auf BGE 102 Ib 140).
