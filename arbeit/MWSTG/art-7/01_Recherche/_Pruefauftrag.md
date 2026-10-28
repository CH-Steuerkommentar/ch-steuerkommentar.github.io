# Prüfauftrag Fundstellen Art. 7 MWSTG (28.10.2026)

Du prüfst Fundstellen einer Kommentierung zu Art. 7 MWSTG (Ort der Lieferung), die ohne Autor:innen veröffentlicht wird. Du kennst die Entstehung nicht und prüfst unabhängig. Jede Fussnote einzeln (keine Stichproben, keine Batches).

Dateien (Repository /home/claude/ch-steuerkommentar.github.io):
- Kommentar: kommentare/MWSTG/art-7.md
- Nummerierte Fussnoten mit Kontext: arbeit/MWSTG/art-7/01_Recherche/Fussnoten_nummeriert.md
- Hilfsmaterial (nur als Wegweiser, nicht als Beleg): arbeit/MWSTG/art-7/01_Recherche/Entscheidregister.md, BVGer_kantonal.md, Materialien_Praxis.md (Seiten, Chunk-IDs von ESTV-Publikationen), Lexplorer_Fundstellen.md (Chunk-IDs der ILE-Literatur).

Für jede Fussnote:
1. Stimmt die Fundstelle (Entscheid, Datum, Erwägung; Seite; Ziffer; Randziffer)?
2. Stützt die Quelle die Aussage im Text, so wie sie formuliert ist (auch Rang: Gericht/Praxis/Lehre; «bestätigt durch»; Fassung)?
3. Zitierform (Datum im Format T.M.JJJJ, «E.»; Fussnote endet mit Punkt).

Werkzeuge (mit ToolSearch laden):
- Bundesgericht: Cache /home/claude/ch-steuerkommentar.github.io/data/entscheide/*.json (Feld text, zitat_de) und Open Case Law (get_erwaegung, cite für den Zitierstring). BVGer und SRK: Open Case Law (get_erwaegung, get_decision; SRK unter court ch_vb), ersatzweise Entscheidsuche fetch_document.
- Erlasse: Fedlex (get_article; MWSTG SR 641.20, MWSTV SR 641.201). Materialien: Open Case Law search_botschaft/get_materialien; amtliche PDF über Fedlex-Filestore sind zulässig (wie in Materialien_Praxis.md beschrieben).
- ESTV-Publikationen: Open Case Law get_practice (source estv_mwst) und Lexplorer Tax get_chunk_content (Chunk-IDs aus Materialien_Praxis.md). get_chunk_content und nav_* zählen nicht als Suche. Lexplorer-Suchen (search_*) höchstens 2.
- ILE-Literatur: Lexplorer Tax get_chunk_content/get_document_slice mit den Chunk-IDs aus Lexplorer_Fundstellen.md. Achtung: Im Handbuch (Honauer/Probst/Rohner/Frey) fehlen im OCR viele Randziffern; prüfe, ob eine zitierte «Rz.» im Text sichtbar ist, sonst ob die zitierte «Ziff.» stimmt.
- Keine Websuche, Lexplorer nie für Rechtsprechung. Zitierstrings nur aus Tool-Ergebnissen.

Ausgabe: Schreibe deine Fundstellenliste als Markdown-Tabelle in die dir genannte Datei: | Fn. | Fundstelle | Ergebnis (bestätigt / korrigiert / nicht belegbar) | Hinweis (bei Korrektur: was genau ändern; bei «nicht belegbar»: warum, und welche Formulierung belegt wäre) |. Danach eine kurze Liste «Befunde zum Text» (Aussagen, die über die Quelle hinausgehen oder sie falsch wiedergeben). Antworte am Ende mit einer Zusammenfassung nur der Korrekturen und nicht belegbaren Fundstellen (Fn.-Nummer, konkreter Änderungsvorschlag).
