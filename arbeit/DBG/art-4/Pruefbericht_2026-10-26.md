# Prüfbericht zu Art. 4 DBG – 26.10.2026

Unbeaufsichtigter Lauf (API, Steuerskript). Kein `stand.py setze`, kein git, keine Word-Fassung.

## Ergebnis

- `kommentare/DBG/art-4.md`: 42 Randnoten, 94 Fussnoten; `python3 pipeline/kommentar.py` ohne Befund.
- `python3 pipeline/md2site.py --pruefen`: 0 Befunde; Art. 4 wird nur wegen des Status «in_arbeit» zurückgehalten (Status setzt das Steuerskript).
- Register: 42 Entscheide (14 A, 15 B, 13 C; 7 Fehltreffer gestrichen), davon 4 nachgetragen (2A.480/2001, BGE 151 II 154, 2C_199/2011, 2C_41/2012); beim Schreiben zusätzlich BGer 2C_646/2021. Kantonal 15 Entscheide verwendet (Kantonal_Praxis.md).
- Fundstellenprüfung vollständig durch zwei Hilfsagenten (Fundstellenliste_2026-10-26.md mit Teillisten); alle Befunde behoben.

## Entscheide und Annahmen im unbeaufsichtigten Lauf

1. Schritt 2 «Ohne Vorarbeit»: Grundlage war der Cache (Phrasensuche «Art. 4» AND (DBG OR LIFD), 508 Kandidaten, 43 Treffer, 41 verschiedene Entscheide). Die Volltextsuche von Open Case Law mit Absatzvarianten lieferte über 1200 bzw. 1600 unscharfe Treffer; sie wurde nicht ausgewertet. Ergänzt wurden find_leading_cases, Nachtragskandidaten aus den Zitaten der Cache-Entscheide und eine gezielte Suche zu lit. d und Bau-/Montagestellen.
2. Die vor 2000 ergangenen Urteile 2A.47/1995 (ASA 65 S. 822) und 2A.409/1997 sind im Korpus nicht verfügbar; sie erscheinen nur als von BGE 137 II 246 bzw. 2C_996/2012 wiedergegebene Rechtsprechung, nicht als eigene Fundstelle.
3. Botschaft 1983 nur im OCR-Text von Open Case Law geprüft (PDF des Bundesarchivs nicht abrufbar); Botschaft 2016 im Fedlex-PDF.
4. Musterkommentierung: Art. 11 DBG (Grieder/Hongler) für Stil und Aufbau gelesen; die Schwesterkommentierung Art. 3 DBG des Projekts diente als Formatvorbild. Wertende Stellen nicht übernommen.
5. Lexplorer nicht verfügbar; 0 Lexplorer-Suchen. Keine Websuche, keine Lehrrecherche. Lehre erscheint nur als von Entscheiden wiedergegebene Aussage (2C_666/2015, 9C_10/2023, 2C_199/2011, BGE 152 II 98, 2C_996/2012).
6. SSK-Kreisschreiben und Zürcher Steuerbuch nicht eingesehen (keine gesicherte Adresse bzw. dynamische Seite); das Merkblatt ZStB 49.3 erscheint nur als Grundlage eines kantonalen Entscheids. ESTV-Praxis: KS 30 und KS 22a. Das KS Nr. 19/1995 wurde nicht verwendet (Geltung ungeprüft); stattdessen Art. 172 DBG.
7. Ausblick: Art. 4 DBG bleibt in allen Fedlex-Fassungen bis 1.1.2029 unverändert; aufgenommen wurde der Systemwechsel bei der Wohneigentumsbesteuerung (Aufhebung von Art. 21 Abs. 1 lit. b DBG ab 1.1.2029, AS 2026 213).
8. Gerichtsbezeichnungen nach Zitierrichtlinie: übliche Abkürzungen (KGer, VGer), sonst ausgeschrieben (Cour de justice GE, Camera di diritto tributario TI, Steuerrekursgericht ZH).

## Schlussprüfung (Prüfpunkte des Skills `pruefung`, in der Hauptsitzung)

| Prüfpunkt | Befund | Erledigung |
|---|---|---|
| Neutralität | «sachgerecht» (Wiedergabe von BGE 141 V 272) von kommentar.py gemeldet | umformuliert («als gesetzeskonform erachtet») |
| Rang der Aussagen | mehrere kantonale Aussagen zunächst ohne Gericht im Satz; ein BGer-Satz stützte sich auf ein kantonales Urteil | Gericht jeweils im Satz genannt; «bestätigt in» kenntlich gemacht |
| Unbelegte Sätze | Definition Inhaber/Teilhaber ohne Beleg; Aussage, Art.-5-Fälle unterlägen grossteils der Quellensteuer | gestrichen |
| Unbelegte Querverweissätze | drei Sätze nur mit N.-Verweis | Belege ergänzt |
| Zitierweise | Erstnennung OR fehlte; Kreisschreiben ohne Titel | ergänzt (OR mit SR 220; KS 22a und KS 30 mit Titel und «nachfolgend») |
| Wiederholungen | Ehegatten und Wechsel in einer RN (zwei Gedanken) | in zwei RN geteilt |
| Querverweise | alle Labels aufgelöst (kommentar.py) | – |
| Fremdsprachige Zitate | «comme un propriétaire» | im Original kursiv mit Bedeutung |

## Offene Fragen, die der Text als offen ausweist

- Beteiligung an Immobiliengesellschaften und einfachen Gesellschaften als Anknüpfung nach lit. c (für das DBG nicht entschieden).
- Fortgeltung der BdBSt-Praxis zur Vermittlung vom Ausland aus (BGE 137 II 246, E. 8 offengelassen); sonst keine höchstrichterliche Rechtsprechung zu lit. d.
- Bau- und Montagestellen: keine höchstrichterliche Auslegung der Zwölfmonatsgrenze.
- Nutzniesser von Geschäftsbetrieben sowie Nutzniesser und Wohnberechtigte an Grundstücken: keine höchstrichterliche Rechtsprechung.
- Subsidiarität der wirtschaftlichen Zugehörigkeit nur als vom Bundesgericht wiedergegebene Lehrmeinung.
