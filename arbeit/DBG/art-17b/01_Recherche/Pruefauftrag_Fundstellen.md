# Auftrag: Fundstellenprüfung Art. 17b DBG

Du prüfst unabhängig (ohne Kenntnis der Entstehung) Fussnoten der Kommentierung `/home/claude/ch-steuerkommentar.github.io/kommentare/DBG/art-17b.md` (Markdown; Fussnoten inline als `^[…]`, durchnummeriert in der Reihenfolge ihres Vorkommens im Text bis zum Literaturverzeichnis). Eine nummerierte Liste aller Fussnoten mit Abschnitt steht in `/tmp/claude-0/-home-claude/a452462b-5dad-5712-b2f8-697a3ad38683/scratchpad/fn.tsv` (Nr. TAB Abschnitt TAB Text). Lies für jede dir zugewiesene Fussnote den Satz bzw. die Sätze im Kommentartext, die sie belegt, und prüfe JEDE Fundstelle in der Fussnote am Original:

1. Stimmt die Fundstelle (Entscheid, Datum, Erwägung/Ziffer/Randziffer/Seite/Folie)?
2. Stützt die Stelle die Aussage im Text (Inhalt, Rang: Gericht/Praxis/Lehre, Konjunktiv bei Lehre, keine Überzeichnung)?
3. Stimmt die Zitierform (Bundesgerichtsentscheide: Zitierstring exakt wie `citation_string_de` aus Open Case Law bzw. `zitat_de` im Cache)?

Quellen und Werkzeuge (Werkzeuge per ToolSearch laden):
- Bundesgericht: Cache `/home/claude/ch-steuerkommentar.github.io/data/entscheide/ocl_*.json` (Felder `zitat_de`, `text`); sonst Open Case Law `get_erwaegung`, `cite`, `get_decision`, `find_relevant_erwaegung`.
- Kantonale Entscheide: NUR Entscheidsuche (`mcp__Entscheidsuche__search`, `fetch_document`); Kennungen/URLs in `arbeit/DBG/art-17b/01_Recherche/Kantonale_Entscheide.md`.
- Botschaft BBl 2005 575: Volltext `arbeit/DBG/art-17b/01_Recherche/quellen/Botschaft_BBl_2005_575.txt`. Achtung Seitenzählung: Die alleinstehende Seitenzahl steht am ENDE (Fusszeile) der jeweiligen Seite; Text vor der Zahl N gehört zu Seite N (erste Seite endet mit «2004-2347 575»).
- KS 37 ESTV (Version 30.10.2020): `arbeit/DBG/art-17b/01_Recherche/quellen/KS37_ESTV_2020.txt`; Anhänge I–V nur in Lexplorer Tax (Kennungen in `Lexplorer_Fundstellen.md`, `Verwaltungspraxis.md`).
- Kantonale Steuerbücher/Merkblätter, SSK: Lexplorer Tax, nur lesend (`get_chunk_content`, `get_document_slice`, `nav_*`; Kennungen in `Verwaltungspraxis.md` und `Lexplorer_Fundstellen.md`). KEINE `search_chunks_*` (Budget 0).
- ILE-Literatur (FStR, Seminarunterlagen): Lexplorer Tax, nur lesend, Kennungen in `ILE_Literatur.md`.
- OK-Kommentierung Art. 14a StHG: `arbeit/DBG/art-17b/01_Recherche/OK_StHG_art-14a.md`.
- Erlasse (DBG 642.11, StHG 642.14, MBV 642.115.325.1): Fedlex `get_article`.
- Die Recherchedateien in `arbeit/DBG/art-17b/01_Recherche/` sind nur Wegweiser; massgebend ist das Original. Keine Websuche. Lexplorer nie für Rechtsprechung.

Ändere die Kommentierung NICHT. Schreibe dein Ergebnis in die dir genannte Datei als Markdown-Tabelle:
| FN | Fundstelle | Ergebnis (bestätigt / korrigiert / nicht belegbar) | Hinweis (bei korrigiert: konkreter Korrekturvorschlag für Fussnote und ggf. Textsatz; bei nicht belegbar: was fehlt) |
Darüber ein Kopf mit Datum, Prüfer, Zahl geprüft/bestätigt/korrigiert/nicht belegbar. Antworte am Ende knapp (max. 300 Wörter) mit der Liste der korrigierten und nicht belegbaren Fussnoten.
