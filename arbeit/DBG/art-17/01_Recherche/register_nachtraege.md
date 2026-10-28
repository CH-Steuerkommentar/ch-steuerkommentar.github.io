# Art. 17 DBG – Gegenprobe zum Entscheidregister: Nachträge

Stand: 27. Oktober 2026. Abgleich gegen `data/zitate/DBG/art-17.json` (139 Entscheide; Kandidatenquelle des Caches: Entscheidsuche `"Art. 17" AND (DBG OR LIFD)`, Entscheide: Open Case Law).
Werkzeuge: Open Case Law (search_decisions, find_leading_cases, find_relevant_erwaegung, get_erwaegung, get_regeste, cite, find_citations) und Entscheidsuche (search, hierarchy CH_BGer). Kein Lexplorer, keine Websuche.
Zitierstrings ausschliesslich aus `citation_string_de` der Tool-Ergebnisse.

Klassen: **A** = Art. 17 DBG (bzw. art. 17 LIFD) wird in den Erwägungen tragend ausgelegt oder angewendet; **B** = Art. 17 wird angewendet, die Begründung stützt sich aber im Wesentlichen auf ein anderes Urteil oder ein anderes Rechtsgebiet (AHV); **C** = Art. 17 wird nur als Verweis genannt (z.B. «Art. 17 ff. DBG») oder ausdrücklich offengelassen.

## Befund in Kürze

Der Cache ist für die Rechtsprechung, die in Entscheidsuche indexiert ist, praktisch vollständig: Alle Phrasensuchen in Entscheidsuche (DBG-, LIFD- und Abs.-2-Varianten) ergaben **keinen** Treffer, der nicht schon im Cache ist. Die Lücken stammen aus BGer-Urteilen, die Entscheidsuche mit der Cache-Abfrage nicht findet (vor allem französisch- und italienischsprachige Urteile sowie Urteile, die nur «Art. 17 ff. DBG» zitieren). Sie liessen sich über den Normindex von Open Case Law (`find_leading_cases` mit law_code LIFD/DBG, Art. 17) ermitteln.

**8 Nachträge**: 2 × A, 2 × B, 4 × C. Zu Abs. 1bis (Weiterbildungskosten seit 2016) wurde kein BGer-Entscheid gefunden, der die Bestimmung anwendet; die Treffer zu Weiterbildungskosten betreffen alle den Abzug nach Art. 26 DBG (aF) und sind entweder schon im Cache (2A.277/2003, 2A.381/2006) oder ohne Bezug zu Art. 17.

## Nachtragstabelle

| Entscheid (citation_string_de) | Datum | Normstelle | Sachfrage | Kernaussage (ein Satz) | E. | Ergebnis | Klasse | Steuerperiode | Suchweg |
|---|---|---|---|---|---|---|---|---|---|
| BGer 2C_974/2019 vom 17. Dezember 2020 | 17.12.2020 | art. 17 al. 1 LIFD (aF, RO 1991 1184); art. 7 al. 1 LHID | Mitarbeiteroptionen vor 2013: Realisationszeitpunkt (Zuteilung oder Ausübung) | Optionen zu Vorzugsbedingungen gehören zu den «autres avantages appréciables en argent» nach art. 17 al. 1 LIFD; gesperrte, nicht übertragbare Optionen, die bei Auflösung des Arbeitsverhältnisses verfallen, sind erst bei Ausübung erworben und zu besteuern. | 5, 6.1–6.5, 11 | Beschwerde der Steuerpflichtigen abgewiesen (DBG und StHG) | A | 2005–2007 | find_leading_cases LIFD Art. 17; search_decisions «art. 17 al. 1 LIFD» |
| BGer 2C_292/2007 vom 9. Januar 2008 | 09.01.2008 | art. 17 cpv. 1 LIFD; art. 7 cpv. 1 LAID | Verwaltungsratshonorar, das an eine GmbH des VR-Präsidenten ausbezahlt wird | VR-Honorare sind Einkünfte aus unselbständiger Erwerbstätigkeit und vermutungsweise dem Mandatsträger persönlich zuzurechnen; die Vermutung fällt nur bei nachgewiesener Abtretungspflicht an die vertretene juristische Person. | 2.1, 2.2, 3 | Beschwerde abgewiesen; Hälfte der Zahlung an die GmbH dem Pflichtigen als VR-Honorar zugerechnet | A | 2004 | search_decisions «art. 17 al. 1 LIFD»; find_leading_cases LIFD Art. 17 |
| BGer 9C_216/2023 vom 31. Oktober 2023 | 31.10.2023 | art. 16 al. 1 und 17 al. 1 LIFD (Fassung 2008/2010); art. 7 al. 1 LHID | Mitarbeiteroptionen desselben Beteiligungsplans wie in 2C_974/2019; Ruling eines anderen Kantons | Die vor 2013 geltenden art. 16 al. 1 und 17 al. 1 LIFD sind anwendbar; die Optionen sind wie in 2C_974/2019 erst bei Ausübung zu besteuern. | 5, 6.1, 6.2, 8 | Beschwerde abgewiesen | B | 2008 und 2010 | search_decisions «art. 17 al. 1 LIFD»; find_citations eingehend auf 2C_974/2019 |
| BGer 9C_683/2007 vom 26. Mai 2008 | 26.05.2008 | art. 17 LIFD (als steuerliche Referenz im AHV-Recht) | AHV-Beitragspflicht auf Mitarbeiteroptionen | Mitarbeiteroptionen gelten steuerrechtlich als geldwerte Vorteile im Sinne von art. 17 LIFD; bei Vesting-Klausel sind sie erst bei Ausübung zu erfassen, und das Beitragsrecht folgt dieser Praxis. | 2.4 | AHV-Entscheid (II. sozialrechtliche Abteilung) | B | – (Beitragsjahre AHV) | find_leading_cases LIFD Art. 17; search «art. 17 LIFD» |
| BGer 2C_449/2017 vom 26. Februar 2019 | 26.02.2019 | Art. 17 ff. DBG (offengelassen); Art. 16 Abs. 1, 20 Abs. 1 lit. c DBG | Leistungen einer GmbH an ihren faktischen Geschäftsführer (Nicht-Beteiligter): Direktbegünstigung statt Dreieckstheorie | Ob die Leistungen Erwerbseinkommen nach Art. 17 ff. DBG oder sonstiges Einkommen sind, lässt das BGer im Hinterziehungsverfahren offen, da die Steuerbarkeit nach Art. 16 Abs. 1 DBG feststeht. | 2.8 (auch 2.2, 2.5.3) | Gutheissung der Beschwerde der Steuerverwaltung | C | 2005 | find_leading_cases DBG Art. 17 (bekannt) |
| BGE 149 II 400 | 23.06.2023 (BGer 9C_682/2022) | Art. 17 ff. DBG (nur Verweis); Art. 16 DBG; DBA CH-AE | Zuflusszeitpunkt nicht fälliger Forderungen; Abfindung eines Fussballspielers bei vorzeitiger Vertragsauflösung (DBA) | Einkünfte fliessen zu, sobald die steuerpflichtige Person tatsächlich darüber verfügen kann; Sonderregeln der einzelnen Einkommensarten (Art. 17 ff. DBG) bleiben vorbehalten. | 4.2 (Urteil 9C_682/2022) | Dispositiv nicht gelesen (Regeste: Ist-Methode bei Zahlungsunwilligkeit des Schuldners; kein Besteuerungsrecht des Tätigkeitsstaats für die Abfindung) | C | – (nicht geprüft) | find_leading_cases DBG Art. 17 (bekannt) |
| BGE 151 II 418 | 09.12.2024 (BGer 9C_757/2023) | Art. 17 ff. DBG (nur Verweis); Art. 10 Abs. 2, 20 Abs. 1 lit. e DBG | Thesaurierungsfonds: Zeitpunkt der Besteuerung beim Anleger | Wiederholt den Zuflussgrundsatz mit dem Vorbehalt «Art. 17 ff. DBG»; ohne Bezug zur unselbständigen Erwerbstätigkeit. | 5.1 (Urteil 9C_757/2023) | – | C (für Art. 17 ohne Bedeutung; nicht ins Register aufnehmen) | – | find_leading_cases DBG Art. 17 (bekannt) |
| BGer 2C_648/2010 vom 27. Januar 2011 | 27.01.2011 | art. 17 LIFD (Systematik), art. 18 LIFD | Verkauf exklusiver Patentrechte: Einkunft aus selbständiger Erwerbstätigkeit oder steuerfreier privater Kapitalgewinn | art. 17 LIFD unterwirft den Ertrag der unselbständigen Erwerbstätigkeit der Steuer; tragend ist die Abgrenzung nach art. 18 LIFD. | 3.1 | – | C | 2001–2002 | find_leading_cases LIFD Art. 17 |

## A-Entscheide im Detail

### BGer 2C_974/2019 vom 17. Dezember 2020 (Mitarbeiteroptionen, Steuerperioden 2005–2007, VD)

In E. 5 hält das BGer fest, dass die seit 1. Januar 2013 geltenden Art. 17a ff. DBG und Art. 7c ff. StHG wegen des Rückwirkungsverbots nicht anwendbar sind, weil die Optionen «ont été reçues et exercées par le contribuable 1 avant 2013»; massgebend ist allein das Recht von 2005–2007. In E. 6.1 legt es art. 17 al. 1 LIFD in der damaligen Fassung aus: Die Abgabe von Optionen gehört zu den «autres avantages appréciables en argent au sens de la disposition précitée et est traitée comme un revenu du travail», soweit der Ausübungspreis unter dem Verkehrswert liegt. Ein Einkommen ist realisiert, wenn der Pflichtige «acquiert une prétention ferme sur laquelle il a effectivement un pouvoir de disposition». E. 6.2–6.4 fassen das KS ESTV Nr. 5/1997 und das Rundschreiben von 2003 zum Vesting zusammen; Optionen unter einer aufschiebenden Bedingung (Verfall bei Austritt während der Sperrfrist) sind noch nicht unwiderruflich erworben. In E. 6.5 wendet das BGer dies an: Die Optionen waren nicht übertragbar und hatten gestaffelte Sperrfristen von einem bis vier Jahren; die Besteuerung im Zeitpunkt der Ausübung (nicht erst nach Ablauf der Sperrfristen) «n'apparaît pas critiquable». Nach E. 11 gilt dasselbe für die Kantonssteuer, weil art. 20 al. 1 LI/VD «la même teneur que l'art. 17 al. 1 LIFD» hat (Harmonisierung mit art. 7 al. 1 LHID). Für die Kommentierung: Leitentscheid zur Rechtslage vor 2013 (Abgrenzung zu Art. 17a–17e DBG) und zur Parallelnorm im StHG.

### BGer 2C_292/2007 vom 9. Januar 2008 (Verwaltungsratshonorar, Steuerperiode 2004, TI)

In E. 2.1 zählt das BGer gestützt auf art. 17 cpv. 1 LIFD die VR-Vergütungen zu den Einkünften aus unselbständiger Erwerbstätigkeit: «Tra questi proventi figurano anche le retribuzioni percepite in qualità di membro di un consiglio d'amministrazione» (mit Hinweis auf BGE 121 I 259 und die AHV-Parallele BGE 133 V 498). Da nur natürliche Personen VR-Mitglied sein können (Art. 707 Abs. 3 OR), sind die Honorare grundsätzlich diesen zuzurechnen; es gilt «la presunzione secondo cui l'onorario è devoluto personalmente all'amministratore». Die Vermutung fällt nur, wenn die Vergütung aufgrund einer Abtretungspflicht direkt an die vertretene juristische Person fliesst; die Beweislast trägt der Mandatsträger bzw. die empfangende Gesellschaft. In E. 2.2 rechnet das BGer bei einem VR-Präsidenten die Hälfte einer an seine GmbH bezahlten Vergütung (Fr. 75'000.–) ihm persönlich als VR-Honorar zu; einer Steuerumgehung bedarf es dafür nicht. Nach E. 3 gilt das auch für die Kantonssteuer, weil art. 7 cpv. 1 LAID und art. 16 cpv. 1 LT/TI «sostanzialmente il medesimo tenore dell'art. 17 cpv. 1 LIFD» haben. Ergänzt die im Cache enthaltenen Urteile zum VR-Honorar (2C_331/2017, 2C_95/2013).

## Trefferzahlen je Suchweg

| Suchweg | Werkzeug / Filter | Treffer | davon neu (nicht im Cache) und geprüft |
|---|---|---|---|
| «Art. 17 Abs. 1 DBG» | OCL search_decisions, court bger | 52 | 2C_449/2017 |
| «Art. 17 DBG» | OCL search_decisions, court bger | 27 | 9C_682/2022, 9C_757/2023, 2C_449/2017 |
| «art. 17 al. 1 LIFD» | OCL search_decisions, court bger | 27 | 2C_974/2019, 9C_216/2023, 2C_292/2007 |
| «Art. 17 Abs. 2 DBG» OR «art. 17 al. 2 LIFD» OR «Art. 17 Abs. 1bis DBG» OR «art. 17 cpv. 1 LIFD» | OCL search_decisions, court bger | 125 (unscharf, viel UV/AHV) | Stichproben 2C_108/2008, 2C_673/2007, 2C_70/2008, 2A.60/2002, 2C_6/2010, 2C_786/2008: kein Art. 17 DBG |
| «art. 17 LIFD» / «art. 17 s. LIFD» / «art. 17 ss LIFD» / «art. 17 cpv. 1 LIFD» | OCL search_decisions (Ranking eingeschränkt) | 179 | 9C_683/2007, 2C_648/2010 (übrige ausserhalb des Steuerrechts) |
| «Art. 17 ff. DBG» / «Art. 17 und 18 DBG» / «Art. 17 f. DBG» | OCL search_decisions | 869 (unscharf) | nur Bekannte (9C_682/2022, 9C_757/2023, 2C_449/2017) |
| «Art. 17» AND (DBG OR LIFD) | Entscheidsuche CH_BGer, alle Seiten | 345 | 0 (alle nicht gecachten Treffer betreffen Art. 17 AHVV, LP, LPFisc/GE, LISP, aStHG oder den Katalog «art. 17 à 23 LIFD») |
| «Art. 17 Abs. 2 DBG» OR «art. 17 al. 2 LIFD» OR «art. 17 cpv. 2 LIFD» | Entscheidsuche CH_BGer | 10 | 0 |
| «Art. 17 Abs. 1 DBG» OR «Art. 17 DBG» OR «Art. 17 Abs. 1bis DBG» OR «aArt. 17 DBG» | Entscheidsuche CH_BGer | 55 | 0 |
| «art. 17 al. 1 LIFD» OR «art. 17 cpv. 1 LIFD» OR «art. 17 LIFD» | Entscheidsuche CH_BGer | 20 | 0 (2C_974/2019, 9C_216/2023 und 2C_292/2007 fehlen dort) |
| Weiterbildungskosten / «17 Abs. 1bis» / «17 al. 1bis» | Entscheidsuche CH_BGer | 10 | 0 (alle zu Art. 26 DBG) |
| Normindex DBG Art. 17 (alle Gerichte) | OCL find_leading_cases | 100 | 9C_682/2022 (= BGE 149 II 400), 9C_757/2023 (= BGE 151 II 418), 2C_449/2017 |
| Normindex DBG Art. 17, bger ab 2019 / bis 2018 / bge | OCL find_leading_cases | 18 / 41 / 7 | keine weiteren |
| Normindex LIFD Art. 17 (alle Gerichte) / bge | OCL find_leading_cases | 98 / 5 | 2C_974/2019, 9C_216/2023, 2C_292/2007, 9C_683/2007, 2C_648/2010 |
| Normindex StHG Art. 7 + «unselbständiger Erwerbstätigkeit Arbeitsverhältnis» | OCL find_leading_cases | 22 | 9C_4/2018: kein Art. 17 DBG |
| Normindex LHID Art. 7 + «activité lucrative dépendante» | OCL find_leading_cases | 37 | 2C_857/2020, 2C_620/2012, 2C_189/2016, 2C_830/2009, 2C_627/2014: kein Art. 17 |
| Mitarbeiteroptionen / -aktien / -beteiligung | OCL search_decisions | 55 | 2C_393/2015, 2A.286/2004: kein Art. 17 (verfahrensrechtlich) |
| Abgangsentschädigung / Kapitalabfindung Arbeitgeber Art. 38 | OCL search_decisions | 177 | keine neuen Steuerentscheide mit Art. 17 |
| Pauschalspesen / Spesenreglement Lohnbestandteil | OCL search_decisions | 112 | 2C_112/2014, 2C_30/2010: kein Art. 17 |
| Verwaltungsratshonorar | OCL search_decisions | 228 | 2C_22/2016: kein Art. 17 |
| «activité lucrative dépendante» LIFD revenu salaire | OCL search_decisions | 146 | überwiegend Ausländerrecht/AHV; keine neuen |
| «unselbständiger Erwerbstätigkeit» «Art. 7 Abs. 1 StHG» | OCL search_decisions | 158 | nur 2C_449/2017 (bekannt) |
| eingehende Zitate auf 2C_974/2019 | OCL find_citations | 68 | 9C_216/2023 positiv; 9C_154/2025, 9C_686/2023, 9C_409/2023, 9C_74/2023: kein Art. 17 |

## Hinweise zur Übernahme

- 9C_682/2022 und 9C_757/2023 sind als BGE 149 II 400 und BGE 151 II 418 publiziert; im Register mit BGE-Zitat aufnehmen. Die E.-Nummern oben beziehen sich auf die gelesenen BGer-Urteile; vor dem Zitieren der BGE-Fundstelle die Nummerierung im BGE prüfen.
- BGE 151 II 418 hat für Art. 17 DBG keine Bedeutung (nur ein Systemverweis); Aufnahme nur, wenn das Register Verweise vollständig erfassen soll.
- 2C_974/2019 und 9C_216/2023 betreffen denselben Beteiligungsplan; sie bilden zusammen mit dem gecachten 9C_1/2023 die jüngste Linie zu Optionen vor 2013.
