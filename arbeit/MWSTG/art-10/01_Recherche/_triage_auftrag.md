# Auftrag Triage Entscheidregister Art. 10 MWSTG

Norm: Art. 10 MWSTG (SR 641.20, «Grundsatz» der subjektiven Steuerpflicht), geltende Fassung (Abs. 1 Fassung 30.9.2016, in Kraft 1.1.2018; Abs. 1bis eingefügt 2016; Abs. 1ter eingefügt 16.6.2023, in Kraft 1.1.2025; Abs. 2 lit. a–d, Abs. 2bis, Abs. 3). Wortlaut:
1 Steuerpflichtig ist, wer unabhängig von Rechtsform, Zweck und Gewinnabsicht ein Unternehmen betreibt und: a. mit diesem Unternehmen Leistungen im Inland erbringt; oder b. Sitz, Wohnsitz oder Betriebsstätte im Inland hat.
1bis Ein Unternehmen betreibt, wer: a. eine auf die nachhaltige Erzielung von Einnahmen aus Leistungen ausgerichtete berufliche oder gewerbliche Tätigkeit selbstständig ausübt, unabhängig von der Höhe des Zuflusses von Mitteln, die nach Artikel 18 Absatz 2 nicht als Entgelt gelten; und b. unter eigenem Namen nach aussen auftritt.
1ter Das Erwerben, Halten und Veräussern von Beteiligungen nach Artikel 29 Absätze 2 und 3 stellt eine unternehmerische Tätigkeit dar.
2 Von der Steuerpflicht ist befreit, wer: a. innerhalb eines Jahres im In- und Ausland weniger als 100 000 Franken Umsatz aus Leistungen erzielt, die nicht nach Artikel 21 Absatz 2 von der Steuer ausgenommen sind; b. ein Unternehmen mit Sitz, Wohnsitz oder Betriebsstätte im Ausland betreibt, das im Inland ... ausschliesslich ... (1. befreite Leistungen, 1bis. ausgenommene Leistungen, 2. Dienstleistungen mit Ort nach Art. 8 Abs. 1 im Inland – nicht befreit, wer Telekommunikations- oder elektronische Dienstleistungen an nicht steuerpflichtige Empfänger erbringt, 3. Elektrizität/Gas/Fernwärme an Steuerpflichtige); c. nicht gewinnstrebiger, ehrenamtlich geführter Sport- oder Kulturverein oder gemeinnützige Organisation unter 250 000 Franken; d. Unternehmen mit Sitz im Inland, das im Inland ausschliesslich ausgenommene Leistungen erbringt.
2bis Der Umsatz berechnet sich nach den vereinbarten Entgelten ohne die Steuer.
3 Der Sitz im Inland sowie alle inländischen Betriebsstätten bilden zusammen ein Steuersubjekt.
(Vor 2018: Abs. 1 «Steuerpflichtig ist, wer unabhängig von Rechtsform, Zweck und Gewinnabsicht ein Unternehmen betreibt und nicht nach Absatz 2 von der Steuerpflicht befreit ist. Ein Unternehmen betreibt, wer eine auf die nachhaltige Erzielung von Einnahmen aus Leistungen ausgerichtete berufliche oder gewerbliche Tätigkeit selbständig ausübt und unter eigenem Namen nach aussen auftritt»; Abs. 2 lit. a: Umsatz «im Inland» unter 100 000 Franken.)
Vorgängernormen: Art. 21 aMWSTG 1999 (gewerbliche oder berufliche Tätigkeit, Umsatzgrenze 75 000), Art. 17 MWSTV 1994.

## Sachfragen-Schlüssel (immer einen oder mehrere Schlüssel angeben)
- U-Begriff: Unternehmensbegriff allgemein (berufliche/gewerbliche Tätigkeit, Nachhaltigkeit, Einnahmenerzielung, Leistungsaustausch als Voraussetzung, Unabhängigkeit von Rechtsform/Zweck/Gewinnabsicht)
- U-Selbst: Selbständigkeit (Abgrenzung unselbständige Erwerbstätigkeit, Organe, Verwaltungsrat, AHV-Qualifikation)
- U-Aussen: Auftreten unter eigenem Namen nach aussen; Stellvertretung (Art. 20 MWSTG) als Zurechnungsfrage
- U-Liebhaberei: Abgrenzung Hobby/Liebhaberei/private Vermögensverwaltung/privater Konsum; Eigentümergesellschaften (Flugzeuge, Yachten, Immobilien), Steuerumgehung
- Subjekt: Wer ist Steuersubjekt/Unternehmensträger (einfache Gesellschaft, Personengesellschaft, Ehegatten, Strohmann, Konzern, Erbengemeinschaft, Konkursmasse, faktischer Betreiber)
- Holding: Beteiligungen, Holding, Abs. 1ter
- Gemeinwesen: Abgrenzung zu Art. 12 MWSTG, öffentlich-rechtliche Körperschaften, Gebühren
- Umsatzgrenze: Abs. 2 lit. a (Mindestumsatz, Berechnung, weltweiter Umsatz, Abs. 2bis, ausgenommene Umsätze, Beginn/Ende der Steuerpflicht im Zusammenhang mit der Grenze, Art. 14 MWSTG)
- Ausland: Abs. 2 lit. b, ausländische Unternehmen, Inlandleistungen, Bezugsteuer, elektronische DL
- Verein: Abs. 2 lit. c (Sport-/Kulturvereine, gemeinnützige Organisationen, 250 000)
- Ausgenommen: Abs. 2 lit. d
- Betriebsstätte: Abs. 3 Einheit Sitz und Betriebsstätten; Betriebsstättenbegriff
- Verzicht: Verzicht auf Befreiung (Art. 11 MWSTG) – nur wenn mit Art. 10 verbunden
- Verfahren: Beweislast, Ermessenseinschätzung, Nachweis der Unternehmereigenschaft, Mitwirkung, Haftung, Strafrecht
- Andere: alles andere (z.B. Radio- und Fernsehgebühr Billag, Vorsteuerabzug, Steuerobjekt)

## Vorgehen
1. Für jeden Entscheid der Liste die Cache-Datei `data/entscheide/<Datei>` lesen (JSON: `zitat_de`, `datum`, `text`, `normen` – `normen["MWSTG/10"]` sind Textausschnitte, wo die Norm vorkommt). NICHT den ganzen Text lesen: mit Python die Fundstellen von «Art. 10», «art. 10», «10 MWSTG», «10 LTVA», «10 LIVA» im `text` suchen und je ±1500 Zeichen ausgeben; dazu Regeste (Anfang des Textes, ca. 1500 Zeichen). Beispiel: `python3 -c "import json,re;d=json.load(open(P));t=d['text'];print(t[:1500]);[print('---',t[max(0,m.start()-1500):m.start()+1500]) for m in re.finditer(r'(?i)art\.\s*10\b',t)]"` (Ausgabe ggf. kürzen).
2. Fehltreffer erkennen: Art. 10 eines anderen Erlasses (z.B. Art. 10 MWSTV, Art. 10 aMWSTG 1999, Art. 10 BV, Art. 10 VStrR, Art. 10 DBG), blosse Nennung in Normkette ohne Bezug → Klasse C bzw. «Fehltreffer».
3. Klasse: A = die Erwägung legt Art. 10 MWSTG aus oder entscheidet eine Sachfrage daraus (bzw. zu Vorgängernorm, wenn Bezug zum geltenden Recht hergestellt wird); B = Anwendung/Subsumtion nach bekannten Grundsätzen, Kasuistik; C = Erwähnung, Normkette, Sachverhalt, Prozessgeschichte; F = Fehltreffer.
4. A-Entscheide an der einschlägigen Erwägung lesen (im Cache-Text), so dass Kernaussage und Erwägungsnummer (E.) sicher sind. Nummer der Erwägung im Text verifizieren (die Erwägungsnummern stehen im Text vor dem Absatz, z.B. «5.2.1»).
5. Fassung: welche Fassung bzw. welches Recht ist anwendbar (aMWSTG 1999 / MWSTG Fassung 2010–2017 / MWSTG ab 2018), Steuerperioden.
6. Zitierstring nur aus `zitat_de` des Caches übernehmen (nie selbst bilden). Gehört ein BGer-Urteil zu einem BGE in der Liste (gleiche Geschäftsnummer, im BGE-Text am Anfang genannt), als ein Eintrag zusammenführen: «BGE … (BGer … vom …)».
7. Besetzung: Fünferbesetzung vermerken, wenn im Text ersichtlich (Rubrum: fünf Richter), sonst «–».

## Ausgabe
Schreibe die Datei `arbeit/MWSTG/art-10/01_Recherche/_register_teil<N>.md` mit einer Markdown-Tabelle:

| Entscheid | Datum | Besetzung | Normstelle | Sachfrage | Kernaussage (ein Satz; bei A gern zwei, mit kurzer wörtlicher Formel in «», wenn sie zählt) | E. | Ergebnis | Klasse | Fassung |

Darunter einen Abschnitt «Befunde je Sachfrage»: je Sachfrage-Schlüssel 2–6 Zeilen mit der Linie der Rechtsprechung in diesen Entscheiden, Leitentscheiden (mit E.), Brüchen/Praxisänderungen und offen gelassenen Fragen (mit Fundstelle E.), und welche BVGer-Entscheide oder Lehrstellen die BGer-Entscheide in diesen Erwägungen anführen (nur zur Orientierung). Alles nur aus dem gelesenen Text; nichts erfinden. Keine Websuche, kein Lexplorer. Keine anderen Dateien ändern.
Antworte am Ende mit einer kurzen Zusammenfassung (Zahl A/B/C/F, wichtigste A-Entscheide mit E. und Kernaussage in je einem Satz).
