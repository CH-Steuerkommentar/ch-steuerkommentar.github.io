# Lexplorer-Fundstellen Art. 8 DBG

Suchen (search_*): 1, abgelehnt («Monatliches Kontingent erreicht (500/500 Suchen)»). Keine Suchtreffer verwendet.
Navigation/Lesen (nicht kontingentiert) durch Hilfsagent:

| Abfrage (Werkzeug) | Kanton | Kennung | lexplorer_url | tragender Satz | Seite |
|---|---|---|---|---|---|
| nav_find «Steuerbuch» → get_document_slice | ZH | af406b5e-d1b1-4720-b7d1-662772ffc73d (ZStB 49.3) | https://mcp-tax.lexplorer.ch/s/doc/af406b5e-d1b1-4720-b7d1-662772ffc73d | «Bei Beginn oder Beendigung der unbeschränkten oder beschränkten Steuerpflicht … liegt eine unterjährige Steuerperiode vor.» | Lit. A S. 1; Lit. C S. 3; Lit. E S. 7 |
| dto. | SG | 6c0dbd53-60cf-4547-aac3-db2293d78836 (StB 66 Nr. 2) | https://mcp-tax.lexplorer.ch/s/doc/6c0dbd53-60cf-4547-aac3-db2293d78836 | «Keine unterjährige Steuerpflicht entsteht beim Wohnsitzwechsel innerhalb der Schweiz.» | S. 1 |
| dto. | SG | a51c5942-3c36-4099-a444-98160513d952 (StB 69 Nr. 2) | https://mcp-tax.lexplorer.ch/s/doc/a51c5942-3c36-4099-a444-98160513d952 | «Der Tod gilt einerseits als Beendigung der Steuerpflicht beider Ehegatten …» | S. 1 |
| dto. | LU | 88b87bb2-7c18-456e-b971-a5a6907063e6 | https://mcp-tax.lexplorer.ch/s/doc/88b87bb2-7c18-456e-b971-a5a6907063e6 | «…wie wenn er neu in die Steuerpflicht eingetreten wäre.» | Webseite |
| dto. | CH | 84cf7470-9de3-48d9-9fb5-25d3a18a5947 (SSK-KS 18) | https://mcp-tax.lexplorer.ch/s/doc/84cf7470-9de3-48d9-9fb5-25d3a18a5947 | (nicht im Text verwendet) | S. 2 f. |
Die im Text zitierten Steuerbücher wurden zusätzlich als PDF an den amtlichen URLs geprüft (Fundstellenprüfung).

## ILE-Literatur (Lauf 27.10.2026)

Werkzeug: `search_chunks_hybrid`, `filter_kanton: "CH"`, `filter_category: "08-institut-fuer-law-und-economics"`, limit 8–10. Suchen: 12 (Budget 25). Lesen mit `get_chunk_content`, `get_document_slice` und `nav_list_chunks` (nicht kontingentiert). Autor:innen am Kapitel- bzw. Beitragskopf geprüft (Slice 0 des jeweiligen Dokuments). Lehrbuch Hongler/Lorenz übergangen.

### Abfragen

| # | Abfrage (gekürzt) | Sachfrage | verwendet |
|---|---|---|---|
| 1 | Wechsel beschränkt/unbeschränkt, Zuzug, Aufteilung der Steuerperiode, Art. 40 Abs. 3, BGE 152 II 98 | Wechsel; Rechtsfolgen | ja (FStR 2025/4; FStR 2023/3) |
| 2 | Wegzug, anschliessende Grenzgängertätigkeit, neue beschränkte Steuerpflicht, 2C_977/2020 | Wechsel offen | nein (nur Treffer aus 1) |
| 3 | Fortdauer des Wohnsitzes, Art. 24 ZGB analog, BGE 138 II 300, Kritik | Wegzug, Meinungsstand | ja (FStR 2025-2; FStR 2008/4; FStR 2024/3) |
| 4 | Quasiansässigkeit, Hochrechnung, FZA, Urteil 6.5.2022 | Rechtsfolgen | nein |
| 5 | Ende mit dem Tod, Steuersukzession, Art. 12 DBG | Tod, Erben | ja (FStR 2009/3) |
| 6 | Beginn beschränkte Steuerpflicht, Grundstückerwerb, Grundbuch, Verkauf | Erwerb/Wegfall Grundstück | nein |
| 7 | Wegzug selbständig Erwerbender, stille Reserven, Art. 4 VO zeitliche Bemessung | Geschäftsbetriebe | nein (nur juristische Personen) |
| 8 | Aufenthalt, 90 Tage, Unterbrechung, Ausreise, 2C_186/2020 | Aufenthalt | nein |
| 9 | Vorübergehende Sitzverlegung, Landesversorgung, Art. 54 Abs. 4 DBG | Abs. 3 | nein |
| 10 | Zuzug, Beginn, Tag der Wohnsitznahme, Anmeldung | Zuzug | nein (Seminarfolien) |
| 11 | Tod eines Ehegatten, Art. 42 Abs. 3, separate Veranlagung | Tod eines Ehegatten | ja (IFF-Schriftenreihe 2021, Berdoz/Bugnon) |
| 12 | Kapitalleistung vor/nach Wegzug, Quellensteuer, Bonus | Bedeutung des Zeitpunkts | nein (Seminarfolien) |

### Verwendete Fundstellen

| Chunk-ID | Autor:innen (Kopf geprüft) | Titel / Fundort | Ziffer | tragender Satz | lexplorer_url | Randnote |
|---|---|---|---|---|---|---|
| 0f96b46f-1ae2-4dd5-9747-bcf9d0828299 | Oesterhelt/Opel | Rechtsprechung 2025/4, FStR 2025 (BGer 14.8.2025 = BGE 152 II 98) | 1.3 | «Es ist zu begrüssen, dass das Bundesgericht … sich für eine Aufteilung der Steuerperiode ausgesprochen hat. Die gegen die Aufteilung angeführten Praktikabilitätsargumente sind durch den Übergang … zur Gegenwartsbemessung … hinfällig geworden.» | https://app.lexplorer.ch/suche?e_chunks=45242&e_sys=ile | wechsel-lehre |
| fb33aa17-0910-4a40-899d-80d9f1389a4d | Oesterhelt/Opel | dto. | 1.3 | «… ist daher auch beim Wegzug aus der Schweiz selbst dann eine Aufteilung der Steuerperiode vorzunehmen, wenn eine beschränkte Steuerpflicht in der Schweiz beibehalten wird.» (Fn. 9: Paschoud/de Vries Reilingh, Oesterhelt/Seiler, Lichter); Änderung der Veranlagungszuständigkeit | https://app.lexplorer.ch/suche?e_chunks=45246&e_sys=ile | wechsel-offen |
| 7a38ac73-b872-4c60-9185-82ac6e74239d | Oesterhelt/Opel | dto. | 1.3 | «Für das interkantonale Verhältnis sieht Art. 4b StHG dagegen den Grundsatz der Einheit der Steuerperiode vor.» | https://app.lexplorer.ch/suche?e_chunks=45251&e_sys=ile | wechsel-grundsatz |
| a83f4814-7925-409c-b0c4-a124c88fd1e4 | Oesterhelt/Opel | Rechtsprechung im Steuerrecht 2023/3, FStR 2023 (BGer 12.4.2023, 9C_689/2022 = BGE 149 II 177) | 3.3 | «Das höchstrichterliche Auslegungsergebnis lässt sich dem Wortlaut der Norm nicht entnehmen. … Eine Begründung bleibt es jedoch schuldig.» | https://app.lexplorer.ch/suche?e_chunks=13083&e_sys=ile | folgen-satz-beschraenkt (neu) |
| e8e3f920-4182-4d00-a889-22b7cf5e50f1 | Oesterhelt/Opel | dto. | 3.3 | «Fraglich scheint ausserdem, ob es sachgerecht ist, dass Art. 40 Abs. 3 DBG bei beschränkter Steuerpflicht tatsächlich generell keine Anwendung findet … Ferienwohnung … hochzurechnen.» | https://app.lexplorer.ch/suche?e_chunks=13084&e_sys=ile | folgen-satz-beschraenkt (neu) |
| 143efab4-1d69-4739-a2cf-925afa923126 | Oesterhelt/Opel | dto. | 3.3 | «Die beiden Urteile stehen in einem gewissen Widerspruch zueinander.» (Fn. 41: BGer 6.5.2022, 2C_977/2020 = BGE 149 II 34) | https://app.lexplorer.ch/suche?e_chunks=13085&e_sys=ile | folgen-satz-beschraenkt (neu) |
| e21cb60c-1318-4c47-9d03-798c1d04f3cd | Oesterhelt/Opel | Rechtsprechung 2025-2, FStR 2025 (BGer 4.2.2025) | 5.3 | «Fälschlicherweise subsumierte das Bundesgericht im Leiturteil BGE 138 II 300 den fortgesetzten Wohnsitz … unter diese Tatbestandsvariante. Beim fortgesetzten Wohnsitz … handelt es sich nämlich um einen fiktiven und nicht um einen gesetzlichen Wohnsitz.» | https://app.lexplorer.ch/suche?e_chunks=14602&e_sys=ile | wegzug-lehre |
| 835d0e1a-dbb9-4cac-a83e-0679bbb99e90 | Oesterhelt/Opel | Rechtsprechung 2024/3, FStR 2024 (BGer 29.2.2024 = BGE 150 II 244) | 3.3 | «Der Umstand, dass eine Rückkehr in die Schweiz nach zwei Jahren von vornherein geplant war (und deshalb auch die Wohnung … beibehalten wurden), vermag eine Wohnsitznahme im Ausland zu Recht nicht infrage zu stellen.» | https://app.lexplorer.ch/suche?e_chunks=18659&e_sys=ile | wegzug-wohnsitz |
| abd3fd36-474b-4c31-97e0-28dc8c89bb44 / bcf1c0ae-cc6c-494f-8661-1c9515565062 | Reich/Waldburger | Rechtsprechung im Jahr 2007 (2. Teil), FStR 2008 (BGer 2C_303/2007) | 4 (Bemerkungen und Schlussfolgerungen) | «Nach einem Wegzug entfällt die Rechtfertigungsgrundlage der Besteuerung kraft persönlicher Zugehörigkeit.» «Die Weiterbesteuerung darf in diesen Fällen nicht mit dem ZGB begründet, sondern muss durch Darlegung verschiedener Indizien … belegt werden.» | https://app.lexplorer.ch/suche?e_chunks=15164&e_sys=ile | wegzug-lehre |
| 077af2c8-4537-4620-8abf-de3ecc406c2f | Rajower/Weber Rajower | Ehegatten- und Erbenhaftung im Recht der direkten Steuern, FStR 2009 | 3.1.3 | «Schweigt sich das öffentliche Recht über diese Frage aus, so finden die Bestimmungen über die Folgen der Annahme unter öffentlichem Inventar (Art. 589 f. ZGB) keine Anwendung.» | https://app.lexplorer.ch/suche?e_chunks=15696&e_sys=ile | erben |
| 94a67ec8-06b2-473a-b551-9b5dec6a8001 | Rajower/Weber Rajower | dto. | 3.2.2 | «… wird in den meisten Kantonen, nicht aber im Bund, die Erbengemeinschaft selbst … besteuert.» | https://app.lexplorer.ch/suche?e_chunks=15699&e_sys=ile | erben |
| 4dedfe2d-dbdf-4dcb-83a4-6c4561c94217 | Berdoz/Bugnon (Kapitelkopf «La procédure mixte en matière d'impôts directs», Segment I–III) | Die Verfahren im Steuerrecht, 4. Aufl., IFF-Schriftenreihe 2021 | V.A.1 | «Pour les personnes arrivant de l'étranger, l'assujettissement commence à la date de leur arrivée. … le seul fait de s'annoncer au contrôle des habitants … peut ne pas être suffisant pour fonder un domicile fiscal.» | https://app.lexplorer.ch/suche?e_chunks=19898&e_sys=ile | zuzug |
| 2f219709-7ece-4b43-a2e9-a92d01264915 | Berdoz/Bugnon | dto. | V.B.1 | «… le seul fait de s'annoncer partant au contrôle des habitants … peut ne pas être suffisant pour fonder une fin d'assujettissement. Il faut en effet que le contribuable déplace également le centre de ses intérêts.» «Quant à l'assujettissement limité, il prend fin lorsque disparaît l'élément imposable …» | https://app.lexplorer.ch/suche?e_chunks=19903&e_sys=ile | abmeldung; wegfall |
| 5c0b166f-22cb-44fe-9fb4-7d475c196d4f | Berdoz/Bugnon | dto. | V.C | «Pour la personne physique qui exerce une activité indépendante, l'assujettissement ne prend pas fin en cas de transfert temporaire à l'étranger du siège de sa raison individuelle ou du siège de la société de personne …» «… un délégué du CICR, en mission pendant trois ans à l'étranger, ne crée pas de nouveau domicile …» | https://app.lexplorer.ch/suche?e_chunks=19906&e_sys=ile | landesversorgung-inhalt; wegzug-weltenbummler |
| 25891dee-e57a-46a7-a065-f5e502e3c5c3 | Berdoz/Bugnon | dto. | V.D | «Le décès entraîne la fin de l'assujettissement des deux époux et le début de l'assujettissement du conjoint survivant.» | https://app.lexplorer.ch/suche?e_chunks=19908&e_sys=ile | tod-ehegatten |

### Gelesen, nicht verwendet

- FStR 2025/4, Ziff. 1.3, Chunk 5582e0a1-… (Satzbestimmung mit Ehegatteneinkommen; betrifft Art. 7/9 DBG) und Chunk «Auswirkungen des FZA» (Ziff. 1.3; FZA-Diskriminierung bei Annualisierung) – nicht eingebaut (Schwerpunkt bei Art. 7/40 DBG).
- Menzer, IFF-Schriftenreihe 2026, Steuerliche Behandlung finanzieller Sanktionen (BGE 138 II 300 nur beiläufig referiert).
- FStR 2009/3 Ziff. 3.2.1 (Chunk 5714b48f-…): allgemeine Steuersukzession; Aussage folgt schon aus Art. 12 DBG.
- Seminarunterlagen (Internationales Steuerseminar 2016, Seminar Einkommenssteuer 2024): Folien ohne zitierfähige Aussage zu Art. 8 DBG.
- Rostetter, IFF-Schriftenreihe 2019, § 10 N 535 (Steuernachfolge allgemein).
