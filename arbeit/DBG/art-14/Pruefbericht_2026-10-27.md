# Prüfbericht Art. 14 DBG – 27.10.2026

Unbeaufsichtigter Lauf (Claude-Cloud, geplante Aufgabe). Ergebnis: 44 Randnoten, 116 Fussnoten; `pipeline/kommentar.py` ohne Befund.

## Entscheide im unbeaufsichtigten Lauf

- **Recherche:** Entscheid-Cache (16 Entscheide mit DBG/14), dazu Entscheidsuche für BGer/BGE und kantonale Gerichte (Hilfsagent). Rund 30 BGer-Einträge und rund 30 kantonale bzw. BVGer-Entscheide sind im Register.
- **Lexplorer Tax:** nicht genutzt (0 Suchen). Die Verwaltungspraxis zur direkten Bundessteuer ist im KS 44 ESTV zusammengefasst; abgerufen über Open Case Law `get_practice`. Kantonale Steuerbücher betreffen hier vor allem Art. 6 StHG und wurden deshalb nicht ausgewertet.
- **Lehre:** keine Recherche. Lehrmeinungen erscheinen nur als Wiedergabe durch Entscheide oder Botschaft.
- **Altes Recht:** Die Rechtsprechung betrifft fast ausschliesslich die Fassung von 1990. Sie ist im Text jeweils als altrechtlich gekennzeichnet.
- **Mindestbetrag:** Der Normtext gibt die Fedlex-Fassung vom 2.9.2026 wieder (435 000 Fr.). Der Betrag von 437 000 Fr. ab 2027 (VKP vom 11.9.2026, AS 2026 486) steht in N. «mindestbetrag». Er ist von einem Prüfagenten über Fedlex gemeldet; in Fedlex ist der Titel (SR 642.119.2) bestätigt, eine konsolidierte Fassung ist noch nicht abrufbar.
- **Individualbesteuerung:** Das Abstimmungsergebnis vom 8.3.2026 ist in den zugänglichen amtlichen Quellen nicht belegt. Der Text nennt deshalb nur, dass die Vorlage auf diesen Termin zur Abstimmung gebracht wurde, und die Inkrafttretensregel.

## Fundstellenprüfung (Schritt 8)

Drei Hilfsagenten haben alle 116 Fussnoten geprüft (siehe Fundstellenliste_2026-10-27.md). Diese Befunde sind behoben:

- **Korrigierte Fundstellen:**
  - 2C_603/2012: E. 3.1 statt 6.1.
  - CDT TI 80.2015.118: consid. 4.2 ergänzt.
  - BGE 87 I 376: Regeste und E. 1a, 1d; das wörtliche Zitat stammt jetzt aus der Regeste.
  - 2A.174/2005: Datumsformat.
  - CJ GE ATA/687/2021: consid. 5g und 8.
  - VGer BE: E. 3.1, als unbestrittene Praxis.
  - 9C_436/2025: E. 7.1 f., Prozessgeschichte ergänzt.
  - Botschaft S. 6025 statt 6024 (Pensionspreis).
  - 2C_764/2021: E. 4.2.1.
  - BGE 126 III 89: E. 3a–c.
  - 2C_164/2015: E. 4.2–4.4.
  - H_20/03: Zitierform.
  - BVGer: Datumsformat.
- **Gerichtsbezeichnungen:**
  - «Tessiner Steuerrekurskommission» ersetzt durch «Kammer für Steuerrecht des Tessiner Appellationsgerichts».
  - «Genfer Verwaltungsgericht» ersetzt durch «Cour de justice» (ATA/687/2021).
- **Inhaltlich umformuliert:**
  - ATA/111/2006 als vom BGer aufgehoben bezeichnet.
  - CJ GE consid. 5f nur als Wiedergabe der Lehre, nicht als Entscheid.
  - KGer LU ausdrücklich als AHV-rechtliche Beurteilung.
  - 2C_277/2008 E. 4.2 hypothetisch formuliert.
  - 2C_830/2019 E. 6.2: Zweck nur der altrechtlichen Mietwertgrenze (auch in N. «verfassung»).
  - Hälftige Nutzung nur bei nicht unterhaltenem Ehegatten.
  - Nachsteuer (2C_277/2008 E. 5.1: Zulässigkeit nicht geprüft).
  - Übergangsrecht StHG (Art. 72m, 78e).
  - Indexierung jetzt nach Art. 39 Abs. 2 DBG.
  - Anrechnung ausländischer Quellensteuern nach Art. 4 der Verordnung SR 672.201 statt nur nach KS 44.
  - Vorentscheid: «Möglichkeit» statt «Anspruch».
  - Verhältnis zu Art. 21 Abs. 2 DBG präzisiert.
- **Zitate und Verzeichnis:**
  - Titel DBA CH-FR vervollständigt.
  - Bundesratsbeschluss BBl 2025 3640: Titel und Link.
  - VKP 2025 und 2026 im Materialienverzeichnis.

## Schlussprüfung (Schritt 9)

Die Schlussprüfung hat Claude selbst durchgeführt (Durchsicht des ganzen Texts). Geprüft wurden:

- Neutralität: keine eigene Wertung; offene Fragen sind als offen ausgewiesen.
- Rang der Aussagen: BGer, kantonal, Praxis, Botschaft.
- Querverweise.
- Erstnennungen der Erlasse.
- Schlusspunkte der Fussnoten.

Behoben wurden:

- eine Formulierung mit «überzeugen» (Neutralitätsprüfung von `kommentar.py`);
- die Aussage zu den unterhaltenen Personen im Ausland, die jetzt als Verwaltungspraxis bezeichnet ist;
- der Satz zur gemischten Besteuerung unter Abs. 2, der jetzt als Wiedergabe des Wortlauts formuliert ist.

## Offen ausgewiesene Fragen

- Mietwert und Art. 21 Abs. 2 DBG (tatsächliche Nutzung).
- Unterhaltene Personen bei gemischter Besteuerung (2C_830/2019 E. 11.2).
- Eigengebrauch bei gesundheitlicher Unmöglichkeit.
- Altrechtliche Praxis bei Schweizer Ehegatten.
- Verwaltungsratsmandate und Vermögensverwaltung als Erwerbstätigkeit.
- Verzicht im Nachsteuerverfahren bei der DBSt.
- Wiederaufnahme nach einem Verzicht.
