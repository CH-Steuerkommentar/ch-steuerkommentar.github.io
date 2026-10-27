# Prüfbericht Art. 16 DBG – Einbau der ILE-Literatur (27.10.2026)

Unbeaufsichtigter Lauf. Auftrag: bestehende, geprüfte Kommentierung um die Literatur des ILE-HSG aus Lexplorer Tax ergänzen, ohne den übrigen Text umzuschreiben. Status bleibt «geprueft», keine Reservierung.

## Recherche

- **Suchen in Lexplorer Tax: 20** (search_chunks_hybrid 18, search_chunks_keyword 2), alle mit `filter_kanton: "CH"`, `filter_category: "08-institut-fuer-law-und-economics"`, limit 8–10; Budget 25 eingehalten. Lesen über get_chunk_content, get_document_slice, nav_list_chunks (keine Suchen).
- Abfragen, Chunk-IDs, Autor:innen, Ziffern, tragende Sätze und lexplorer_url: `01_Recherche/Lexplorer_Fundstellen.md`, Abschnitt E.
- Treffer aus «ILE-HSG — Lehrbuch Steuerrecht» (Hongler/Lorenz) übergangen.
- Ohne einschlägigen ILE-Treffer (nichts eingefügt): Zuwendungen Dritter/Schenkung, Nutzniessung und Art. 23 lit. d DBG, Kryptowährungen, Naturalbezüge und Marktwert (Abs. 2), Vorzugsmiete (BGE 146 II 97), Baurecht/Substanzverzehr, subjektive Zurechnung, Systemwidrigkeit von Abs. 3.

## Eingefügte Fundstellen (8 Werke, 21 Fussnotenzitate)

| Werk | Ort im Text | Art |
|---|---|---|
| Waldburger, FStR 2009, Rechtsprechung im Jahr 2008 (2. Teil), Ziff. 4 | N. verzicht-grundsatz | a.M. in Fn.; Gegenposition im Text (privater Kapitalgewinn beim Schulderlass) |
| Reich/Waldburger, FStR 2006, Rechtsprechung im Jahr 2005 (1. Teil), Ziff. 3 | neue N. haushaltschaden-lehre (2 Fn.) | Meinungsstand zu BGE 132 II 128 |
| Oesterhelt/Opel, FStR 2026, Rechtsprechung 2026/3, Ziff. 4.3 | N. genugtuung (gl.M. zu BGE 152 II 19 E. 3.1; a.M. zu E. 6.1–6.3), neue N. genugtuung-lehre (2 Fn.) | gl.M., a.M., Meinungsstand |
| Oesterhelt/Opel, FStR 2023, Rechtsprechung im Steuerrecht 2023/1, Ziff. 3.3 | N. genugtuung (gl.M. zu BGE 148 II 551), N. genugtuung-lehre | gl.M., Meinungsstand |
| Oesterhelt/Opel, FStR 2023, Rechtsprechung im Steuerrecht 2023/4, Ziff. 1.3 | N. soll | gl.M. zu BGE 149 II 400 |
| Oesterhelt, FStR 2022, Aus der Rechtsprechung im Jahr 2021/2022 (Teil 2), Ziff. 3.3 und 7.3 | N. stiftung (gl.M.), N. dienstbarkeit (a.M.), neue N. dienstbarkeit-lehre (2 Fn.) | gl.M., a.M., Meinungsstand zu BGE 148 II 378 |
| Reich, FStR 2004, Die ungerechtfertigte Bereicherung …, Ziff. 4.3.1 und 4.3.2 | N. neutralisation (vgl. in Fn.; neuer Satz mit Gegenposition zur Periodenbetrachtung) | vgl., Meinungsstand |
| Hongler/Margraf, Seminar Einkommenssteuer, Vorsorge und Sozialversicherungen 2024, Privater Kapitalgewinn vs. Einkommen und Vermögensertrag (Folien) | N. finanzprodukte (vgl.), N. marchzins (neuer Satz), neue N. privatvermoegen-lehre (2 Fn.) | vgl., Meinungsstand |

- **Neue Randnoten: 4** (haushaltschaden-lehre, genugtuung-lehre, dienstbarkeit-lehre, privatvermoegen-lehre), je mit neuem Label; bestehende Labels unverändert. Gesamt jetzt 57 Randnoten, 185 Fussnoten.
- Literaturverzeichnis neu angelegt (vor dem Materialienverzeichnis), 8 Einträge. Bisherige Literaturzitate anderer Herkunft gab es im Text nicht.
- Kopf: `stand: 2026-10-27` (unverändert, entspricht dem heutigen Datum).

## Prüfdurchgang (getrennter Arbeitsschritt)

Ein Hilfsagent stand in dieser Umgebung nicht zur Verfügung; die Prüfung erfolgte als getrennter Arbeitsschritt nach dem Einbau: jede neue Literaturfundstelle am Chunk (get_chunk_content) auf Autor:innen (Kapitelkopf bzw. Autorenzeile), Fundort, Ziffer und Tragfähigkeit der Aussage geprüft.

| Fundstelle | Ergebnis | Hinweis |
|---|---|---|
| Waldburger 2009, Ziff. 4 (Chunk 0a799444…) | bestätigt | Autor am Kapitelkopf «4 Einkommensteuerfolgen eines Schulderlasses …» (Chunk 0ecdf8cc…); Ziffer 4, Abschnitt «Bemerkungen und Schlussfolgerungen» ohne eigene Nummer |
| Reich/Waldburger 2006, Ziff. 3 (Chunks 9384, 9386, 9387) | bestätigt, Text präzisiert | Hinweis auf die im Fall ebenfalls strittigen IV-Renten ergänzt, damit der Satz zu Art. 22 Abs. 1 DBG verständlich ist; Entscheid laut Fn. 27 des Beitrags vom 23.2.2006 (OCR «BGE 123 II 128», gemeint 132 II 128) |
| Oesterhelt/Opel 2026/3, Ziff. 4.3 (Chunks 66239–66245) | korrigiert | a.M. zu BGE 152 II 19 E. 6.1–6.3 eingeschränkt: Kritik betrifft nur die Abhängigkeit von der Schwere der Persönlichkeitsverletzung, den Verzicht auf eine Aufteilung halten die Autor:innen für vertretbar (Klammerzusatz) |
| Oesterhelt/Opel 2023/1, Ziff. 3.3 (Chunk 12772) | korrigiert | Die Autor:innen sprechen von «missbräuchlicher fristloser Entlassung iSv Art. 337c Abs. 3 OR»; Formulierung im Text auf «fristloser Entlassung nach Art. 337c Abs. 3 OR» mit Vergleich zu Art. 336a OR angepasst |
| Oesterhelt/Opel 2023/4, Ziff. 1.3 (Chunk 13531) | bestätigt | Besprochenes Urteil BGer vom 23.6.2023 = BGE 149 II 400 (Ratenzahlungen aus Aufhebungsvereinbarung) |
| Oesterhelt 2022, Ziff. 3.3 (Chunk 12606) | bestätigt | Stipendienfall (BGer vom 8.7.2022) betrifft nicht die im Text zitierten Entscheide; Zitat daher nur als gl.M. zur allgemeinen Aussage mit Klammerzusatz |
| Oesterhelt 2022, Ziff. 7.3 (Chunks 12628–12630) | bestätigt | Besprochener Fall = BGE 148 II 378 (Bauhöhenbeschränkung, Fr. 1 Mio.); Autor allein Stefan Oesterhelt (Kopf Chunk ad93d562…) |
| Reich 2004, Ziff. 4.3.1 f. (Chunks 7912, 7918) | bestätigt | – |
| Hongler/Margraf 2024 (Chunks 50918, 50920, 50926, 50927, 50929) | bestätigt | Referent:innen laut Titelfolie und Chunkzeile Peter Hongler, Olivier Margraf; kein Lehrbuch; keine Randziffern, Zitat nach Folientitel |

Gestrichen: keine Fundstelle (alle Aussagen am Chunk belegt).

## Format und Neutralität

- `python3 pipeline/kommentar.py kommentare/DBG/art-16.md`: 57 Randnoten, 185 Fussnoten, 0 Befunde. Ein erster Befund («wünschenswert» in N. privatvermoegen-lehre) wurde durch indirekte Wiedergabe ohne Wertwort behoben («sprechen sich … aus»).
- `python3 pipeline/md2site.py --pruefen`: 15 bereit, 0 mit Befunden.
- Wertungen der Autor:innen nur als deren Auffassung in indirekter Rede; kein U.E.

## Entscheide im unbeaufsichtigten Lauf

- Kein Hilfsagent verfügbar: Prüfung als getrennter Arbeitsschritt.
- Seminarfolien (ILE-Seminarunterlagen) nach Folientitel zitiert, da ohne Randziffern.
- Die Buchbesprechung von von Ah (FStR 2007) nicht zitiert, weil sie nur die Auffassung des besprochenen Werks wiedergibt.
