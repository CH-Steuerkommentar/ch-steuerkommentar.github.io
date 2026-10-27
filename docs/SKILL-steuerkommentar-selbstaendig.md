---
name: "steuerkommentar-selbstaendig"
description: "Verfasst eine Kommentierung zu einer Norm des Schweizer Steuerrechts ohne Autor:innen zur direkten Veröffentlichung auf der Website: neutral ohne U.E., Übersicht mit Entstehungsgeschichte und Harmonisierung; gestützt auf die Rechtsprechung des Bundesgerichts, kantonale Gerichte, Verwaltungspraxis und die Literatur des ILE-HSG (Lexplorer Tax), ohne Websuche; Ausgabe als Markdown, Word nur auf Wunsch."
---

# Steuerkommentar selbständig (Kommentierung ohne Autor:innen)

Dieser Skill verfasst eine Kommentierung zu einer Norm des Schweizer Steuerrechts, die **ohne Autor:innen direkt veröffentlicht** wird. Er folgt der Arbeitsweise des Skills `steuerkommentar` (Entscheidregister, Gliederung aus der Rechtsprechung, Quellenrangfolge, knapper Text), mit drei Unterschieden, die aus dem fehlenden Autorenteam folgen:

1. **Keine eigene Meinung.** Es gibt niemanden, dem eine Auffassung zugerechnet werden könnte. Deshalb gibt es kein «U.E.», keinen eigenen Vorschlag, keine Bewertung von Positionen und keine Prognosen. Der Kommentar stellt dar, was Gesetz, Gerichte, Verwaltung und die Literatur des ILE sagen, und wo eine Frage offen ist.
2. **Keine Überarbeitungsschleife.** Niemand prüft den Text vor der Veröffentlichung nach. Deshalb gibt es keine gelben Arbeitsmarkierungen und keine Prüfaufträge; was nicht am Volltext belegt ist, kommt nicht in den Text. Am Ende steht eine Schlussprüfung, deren Befunde Claude selbst behebt.
3. **Übersicht als erstes Kapitel.** Entstehungsgeschichte und Harmonisierung stehen als je ein bis drei Randnoten in der Übersicht, nicht in eigenen Kapiteln.

Ziel ist die abstrakt-generelle Aufbereitung der Auslegungslage einer Norm, nicht die Anwendung auf einen Einzelfall.

**Mustervorlage sind die OK-Kommentierungen von Grieder/Hongler** (Art. 10 und 11 DBG, Vorb. zu Art. 13–14a StHG, Art. 13, 14 und 14a StHG): Aufbau, Sprache für den Rang der Aussagen, Fussnoten und Verzeichnisse folgen ihnen (Anhang M). Übernommen wird alles ausser den Stellen, an denen die Autoren selbst werten; diese Stellen werden neutral umgeschrieben (Anhang M.4).

**Projektordner und Vorarbeit.** Die Kommentierungen entstehen im Projektordner des Werks (Repository mit `pipeline/config.py`, `kommentare/`, `arbeit/`; README dort). Claude sucht ihn zuerst: verbundener Ordner, Arbeitsverzeichnis oder Repository der Sitzung; sonst `find / -path '*/pipeline/config.py' -not -path '/proc/*' 2>/dev/null | head`. Die Vorarbeit der Pipeline ist nur noch der **Entscheid-Cache**: `python3 pipeline/entscheide.py <Erlass>/art-<N>` findet die Kandidaten über die Phrasensuche von entscheidsuche.ch und lädt die Bundesgerichtsentscheide, die die Norm in den Erwägungen zitieren, aus Open Case Law nach `data/entscheide/` (JSON je Entscheid mit `referenz`, `zitat_de` = amtlicher Zitierstring, `normen`, `text`; Dauer einige Minuten, keine API-Kosten). Karteikarten gibt es nicht; Register und Problemkarte erstellt Claude selbst (Schritt 2). Fehlt der Projektordner, sagt Claude das in einem Satz und arbeitet nach Anhang A ohne Pipeline. Zu Beginn setzt Claude den Status: `python3 pipeline/stand.py setze <Erlass>/art-<N> in_arbeit` (nicht im unbeaufsichtigten Lauf). Ausgabe ist die Markdown-Datei `kommentare/<Erlass>/art-<N>.md` im Format von `docs/FORMAT.md`; aus ihr entstehen Website und auf Wunsch die Word-Fassung.

**Quellen, die recherchiert werden** (und nur diese):
- **Bundesgericht** (BGE, BGer): Entscheid-Cache und Open Case Law; Zitierstrings nur aus `citation_string_de` bzw. `zitat_de` oder `cite`. Die Rechtsprechung des Bundesgerichts trägt die Kommentierung.
- **Kantonale Gerichte** (und BVGer): ausschliesslich Entscheidsuche.
- **Verwaltungspraxis** (ESTV, SSK, kantonale Steuerbücher und Weisungen): Open Case Law `search_practice`/`get_practice`, Lexplorer Tax (navigiert, «Lexplorer sparsam»), Dokumente auf bekannten Seiten von ESTV und SSK.
- **Erlasse und Materialien**: Fedlex, Open Case Law (`get_article_history`, `search_botschaft`); Materialien soweit Übersicht und Sachfragen sie brauchen.
- **Lehre: nur die Literatur des ILE-HSG** in Lexplorer Tax, Kategorie `08-institut-fuer-law-und-economics` (Kanton `CH`): Forum für Steuerrecht (FStR), IFF-Schriftenreihe, ILE Working Papers, ILE-Seminarunterlagen. Ausgenommen ist das «ILE-HSG — Lehrbuch Steuerrecht» (Hongler/Lorenz, Lehrbuch für Studierende). Vorgehen und Zitierweise in Abschnitt «ILE-Literatur» unten.
- **Nicht recherchiert:** übrige Lehre (Kommentare, Lehrbücher, Aufsätze ausserhalb der ILE-Literatur) und allgemeine Websuche (kein WebSearch). Übrige Lehre erscheint nur, wenn ein Entscheid oder ein ILE-Beitrag sie selbst anführt, und dann als dessen Aussage mit diesem als Fundstelle. Das Fehlen weiterer Lehre wird im Text nicht erwähnt.

**Dateien aus dem Plugin «OK-Steuerkommentar».** Zitierrichtlinie und (für die Word-Fassung auf Wunsch) Formatvorlage und Builder liegen im Skill `steuerkommentar` dieses Plugins. Den Ordner findet Claude mit `find / -path '*ok-steuerkommentar*/skills/steuerkommentar/scripts/kommentar_build.py' 2>/dev/null | head -1` (der Skill-Ordner ist zwei Ebenen darüber; bei mehreren Treffern den jüngsten). Darin: `references/anhang-b-formatvorlagen.md` (nur für die Word-Fassung), `references/anhang-c-zitierrichtlinie.md` (Zitierweise), `references/anhang-d-hongler-publikationen.md` (Publikationen von Peter Hongler), `scripts/kommentar_build.py` (Builder), `assets/Vorlage_Online_Kommentar.docx` (OK-Vorlage), ab Plugin-Version 0.3.0 `references/anhang-f-muster-grieder-hongler.md` (ausführliche Fassung von Anhang M) und `scripts/ok_muster.py` (holt die Musterkommentierungen als Markdown). Die ausführliche Zitierrichtlinie mit Beispielen enthält der Skill `ok-zitierung` desselben Plugins, die Prüfpunkte der Schlussprüfung der Skill `pruefung`. Den Skill `steuerkommentar` selbst nicht laden: Seine Regeln zu U.E., gelber Markierung und Hongler-Abgleich gelten hier nicht. Ist das Plugin nicht installiert, liegen Zitierrichtlinie, Hongler-Publikationen und die ausführliche Mustervorlage im Projekt unter `.claude/skills/steuerkommentar-selbstaendig/references/` (`anhang-c-zitierrichtlinie.md`, `anhang-d-hongler-publikationen.md`, `anhang-f-muster-grieder-hongler.md`); die Word-Fassung entfällt dann.

**Unbeaufsichtigter Lauf** (geplante Aufgabe, GitHub Actions): Niemand beantwortet Rückfragen. Claude trifft die vernünftigste Entscheidung, vermerkt sie im Prüfbericht und arbeitet weiter. Reservierung, Status und Git (Commit, Push) übernimmt das aufrufende Steuerskript bzw. die Aufgabenbeschreibung; Claude ruft dann weder `stand.py setze` noch `git` selbst auf, ausser die Aufgabenbeschreibung verlangt es. Nicht erreichbare Quellen (etwa Lexplorer ohne Zugang) werden übersprungen; Recherche dann über Open Case Law, Entscheidsuche und Fedlex. Keine Websuche.

## Grundhaltung

- **Der Adressat ist Jurist.** Wert schafft die Aufbereitung von Rechtsprechung, Praxis und Lehre, nicht die Wiederholung des Normtexts. Kontrollfrage je Satz: *Steht das schon im Gesetz? Wenn ja, weglassen.*
- **Neutral.** Der Text sagt, wer was vertritt, und wertet nicht selbst. Verboten sind eigene Stellungnahmen in jeder Form: «U.E.», «u.E.», «unseres Erachtens», «nach der hier vertretenen Auffassung», «wir», «vorzugswürdig», «richtigerweise», «zu Recht» bzw. «zurecht», «zutreffend», «überzeugt (nicht)», «verfehlt», «sachgerecht», «wünschenswert», «de lege ferenda sollte». Ebenso verboten sind Prognosen («dürfte vor Bundesgericht kaum standhalten», «wird sich durchsetzen»). Wertungen anderer werden als deren Auffassung wiedergegeben, in indirekter Rede: «Ein Teil der Lehre hält den Ausschluss für nicht stichhaltig begründet, da der Elterntarif kein Sozialabzug sei.»
- **Offene Fragen offen lassen.** Wo Rechtsprechung fehlt oder Gerichte, Praxis und Lehre auseinandergehen, steht das ausdrücklich da: was entschieden ist, was nicht, welche Positionen es gibt und worauf sie sich stützen. «Höchstrichterlich ist die Frage, soweit ersichtlich, nicht entschieden.» Keine Auflösung durch eigene Wertung.
- **Gliederung nach Sachfragen.** Überschriften benennen Rechtsbegriffe und Einzelprobleme («Der Begriff der ‹Wohnstätte›», «Parkplatzgebühren»), mit Normstelle in Klammern («(Abs. 1 lit. a)»). Keine Überschriften wie «Rechtsprechung», «Praxis der Steuerbehörden», «Kritische Würdigung» oder «Offene Fragen» als Gliederung nach Quellenarten. Innerhalb *einer* Sachfrage sind sammelnde Überschriften wie in den Mustern zulässig («Kasuistik der bundesgerichtlichen Eingriffe», «Kantonale Bewertungssysteme», «Tragweite der harmonisierungsrechtlichen Vorgabe»; Anhang M.2).
- **Gliederung aus Wortlaut und Entscheiden.** Der Wortlaut liefert das Gerüst, das Entscheidregister die Sachfragen. Eine eigene Überschrift erhält eine Sachfrage nur, wenn sie eine eigenständige Rechtsfrage ist und Stoff für mindestens drei Randnoten trägt; ein einzelner Entscheid, auch ein BGE, genügt dafür nicht (Regeln unter «Aufbau»).
- **Quellenrangfolge innerhalb jeder Sachfrage** (in den Randnoten, nicht als Unterkapitel): Gesetz und Verordnung → BGE → unpublizierte BGer-Entscheide (Fünferbesetzung kennzeichnen) → kantonale Gerichte → Verwaltungspraxis (ESTV/SSK, dann Kantone gebündelt) → Lehre (ILE-Literatur). Verwaltungspraxis wird nie als Rechtsprechung ausgegeben; Lehre ersetzt nie die Rechtsprechung. Was eine Aussage an Autorität hat, muss erkennbar sein (höchstrichterlich, kantonal, Praxis, Lehre), und ob sie aus dem Gesetz oder nur aus der Verordnung folgt.
- **Register vollständig, Text knapp.** Vollständig ist das Entscheidregister, nicht der Fliesstext. Im Text stehen die Regel und die Entscheide, die sie setzen oder ändern; je Sachfrage höchstens ein bis zwei Leitfälle mit Sachverhaltskern, weitere BGE in einem Satz; gleichlaufende Entscheide gebündelt in der Fussnote mit Ergebnis-Klammer («(Zeitgewinn von 50 Minuten genügt nicht; Steuerperiode 2021)»). Ratio und obiter trennen.
- **Kantonale Praxis gebündelt.** Die Mehrheitslinie in einem Satz («so etwa in den Kantonen Zürich, Luzern, Solothurn …»), Abweichungen einzeln mit Fundstelle. Ob eine Abweichung bundesrechtskonform ist, sagt der Text nur, wenn ein Gericht oder die Lehre es sagt, und dann als deren Aussage.
- **Lehre als Meinungsstand (ILE-Literatur).** Positionen gegenüberstellen («Ein Teil der Lehre …», «Nach Oesterhelt/Opel …»). In der Fussnote steht zuerst der Entscheid, der die Aussage trägt; Lehre folgt mit «gl.M.», «a.M.» (die Gegenposition zusätzlich im Text) oder «vgl.». Lehre ist nie die einzige Stütze einer Aussage, die schon ein Entscheid trägt. Wertungen der Autor:innen («Dem ist zuzustimmen») werden als deren Auffassung wiedergegeben, nie übernommen. Urteilsbesprechungen im FStR («Rechtsprechung 20xx») sind Lehre zu dem besprochenen Entscheid; der Entscheid selbst wird nach dem Original zitiert.
- **Nur Belegtes, am Volltext geprüft.** Jede Fundstelle hat Claude im Volltext gelesen oder durch die Fundstellenprüfung (Schritt 8) bestätigt: Entscheide an der zitierten Erwägung, Erlasse und Materialien im Original, Verwaltungspraxis im Dokument, ILE-Literatur im Chunk bzw. Dokument aus Lexplorer Tax. Was sich nicht belegen lässt, wird gestrichen.
- **Hongler/Lorenz nicht zitieren.** Hongler Peter/Lorenz Tabea, Einführung in das schweizerische Steuerrecht, ist ein Lehrbuch für Studierende (in Lexplorer Tax «ILE-HSG — Lehrbuch Steuerrecht») und wird nicht zitiert, obwohl es in der ILE-Kategorie liegt. Steht eine Aussage nur dort, einen anderen Beleg suchen oder die Aussage streichen.
- **Begriffe und Sprache.** Die Begriffe des Gesetzes («Maximalbetrag», nicht «Plafond»), kein Jargon und keine Schlagwörter in Anführungszeichen, keine unbestimmten Bezüge («solche», «dies»), Beschlossenes als Tatsache. Schweizer Hochdeutsch, «ss», Guillemets « », Halbgeviertstrich «–», kein «—».
- **Nie aus dem Gedächtnis rekonstruieren.** Normtext, Urteile, Praxis und Materialien stammen aus recherchierten Quellen; Zitierstrings von Entscheiden nur aus Tool-Ergebnissen; keine Fundstellen erfinden.

---

## Ablauf

### 1. Norm erfassen
Geltenden Wortlaut über Fedlex laden; frühere Fassungen (mit Geltungszeitraum) und beschlossene künftige Fassungen festhalten. Entstehungsgeschichte (Botschaft, Revisionen) und Parallelnorm im StHG feststellen. Aus dem Wortlaut ein **Gerüst** bilden: Absätze, Buchstaben, Rechtsbegriffe, Verweise auf Verordnungen.

### 2. Entscheidregister übernehmen und ergänzen (Anhang A)
**Mit Projektordner** (Normalfall): Zuerst `python3 pipeline/entscheide.py <Erlass>/art-<N>` (falls der Cache für den Artikel noch nicht geladen ist). Die Entscheide im Cache, deren `normen` die Norm enthält, sind die Grundlage des Registers. Ergänzend `find_leading_cases` (Open Case Law) für die Rangfolge der Leitentscheide und die Suchwege zu früheren Fassungen und zur StHG-Parallelnorm (Anhang A.1, letzte Zeilen). Dann bereinigen und triagieren (A.2): Klasse nach Regeste und Pinpoint, A-Entscheide an der einschlägigen Erwägung lesen (im Cache-Text oder Open Case Law `get_erwaegung`), B über Regeste und Pinpoint, C nur zählen. Bei vielen Entscheiden Hilfsagenten je Zeitraum oder Absatz (`effort: medium`).

**Ohne Projektordner:** Alle Bundesgerichtsentscheide suchen, die die Norm in den Erwägungen zitieren, nach allen Wegen von Anhang A.1, dann wie oben.

Ergebnis in beiden Fällen: **Register** und **Problemkarte** in `arbeit/<Erlass>/art-<N>/01_Recherche/`.

### 3. Gliederung festlegen
Aus Gerüst und Problemkarte die Gliederung ableiten (Regeln unter «Aufbau»), mit einer **Gliederungsnotiz** als Arbeitsablage (Anhang A.5): tragende Entscheide je Überschrift, Umfangsplan, Abdeckungsprobe.

### 4. Weitere Quellen je Sachfrage

| Quelle | Zugänge |
|---|---|
| Materialien, Revisionen | Open Case Law `get_article_history`, `search_botschaft`, `get_article_purpose`; Fedlex `list_amendments` |
| kantonale Gerichte, BVGer | **Ausschliesslich Entscheidsuche, nie Lexplorer.** Entscheidsuche `search` mit `hierarchy` (z.B. `ZH_SRK`, `ZH_VG`, `BE_SRK`, `AG_SVWG`; alle Kennungen über `list_hierarchy`), Volltext über `fetch_document`; mehrere Begriffe ohne `AND` schreiben. Ohne Entscheidsuche-Werkzeug: POST https://entscheidsuche.ch/_search.php |
| ESTV, SSK, Steuerbücher, Wegleitungen | ESTV-Kreisschreiben über Open Case Law `search_practice`/`get_practice`; SSK und kantonale Steuerbücher über Lexplorer Tax, navigiert statt gesucht («Lexplorer sparsam») |
| Lehre | **nur ILE-Literatur** in Lexplorer Tax (Abschnitt «ILE-Literatur»); übrige Lehre und allgemeine Websuche nicht |

Je Sachfrage recherchieren, bei vielen Sachfragen parallel (Hilfsagenten, unten). Die verlangten Kantone systematisch prüfen. Zeigt eine Quelle eine Sachfrage, die im Register fehlt, wird die Gliederung angepasst.

### 5. Kommentar schreiben (Aufbau unten)
Vorher Anhang M lesen und die Musterkommentierung, die der Norm am nächsten ist, im Volltext (Anhang M.1). Je Sachfrage die Randnoten in der Quellenrangfolge setzen; wo strittig oder offen, den Meinungsstand darstellen und die Frage als offen bezeichnen. Pro Randnote ein Gedanke, drei bis sechs Sätze, genau ein fettes Stichwort. Text als **Markdown** in `kommentare/<Erlass>/art-<N>.md` schreiben, im Format von `docs/FORMAT.md` des Projekts (Kurzfassung in Anhang G unten): Randnoten als `{rn:label}` am Absatzanfang, Fussnoten inline als `^[…]`, Querverweise `N. {{N:label}}`. Bei langen Kommentierungen abschnittweise schreiben (Übersicht, dann je Hauptteil) und an die Datei anfügen. Danach den Kürzungsdurchgang (unter «Umfang») und einen **Neutralitätsdurchgang**: `python3 pipeline/kommentar.py kommentare/<Erlass>/art-<N>.md` meldet Formatfehler und die verbotenen Wendungen aus der Grundhaltung; ohne Projektordner dieselbe Suche mit `grep -niE "u\.e\.|unseres erachtens|hier vertretenen|vorzugswürdig|richtigerweise|zu ?recht|zutreffend|an anderer stelle|überzeug|verfehlt|sachgerecht|dürfte|wohl kaum|\bwir\b|\bunser"`. Jede eigene Wertung streichen oder als fremde Auffassung mit Fundstelle umschreiben.

### 6. Praxis und ILE-Literatur abgleichen
Je Sachfrage prüfen, ob kantonale Gerichte und Verwaltungspraxis vollständig eingeordnet sind (Mehrheitslinie, Abweichungen), und die ILE-Literatur zuordnen: bestätigend (gl.M.), abweichend (a.M., Gegenposition im Text) oder weiterführend (vgl.); nur aus gelesenen Chunks.

### 7. Zitieren
Nach Anhang C (Zitierrichtlinie des Onlinekommentars), sofern für die Veröffentlichung nichts anderes vorgegeben ist: Erlass-Erstnennungen mit Titel, Datum und SR-Nummer, Seitenzahlen statt interner Ziffern (Anhang C.5), Literaturverzeichnis (nur zitierte ILE-Literatur) und Materialienverzeichnis.

### 8. Fundstellen prüfen
**Hilfsagent (alle Fundstellen, keine Batches):** Ein eigener Hilfsagent ohne Kenntnis der Entstehung prüft jede Fundstelle gegen die Quelle: Entscheide an der zitierten Erwägung über Open Case Law (`get_erwaegung`; stimmt die E., stützt sie die Aussage?) und den Zitierstring (`cite`), Entscheide im Cache auch direkt im Cache-Text, kantonale Entscheide über Entscheidsuche `fetch_document`, Verwaltungspraxis und ILE-Literatur im Dokument (Chunk-IDs in `01_Recherche/Lexplorer_Fundstellen.md`; `get_chunk_content` zählt nicht als Suche), Materialien über Fedlex bzw. `search_botschaft`. Bei vielen Fussnoten ein Prüfagent je Hauptteil. Ergebnis ist die **Fundstellenliste** (Fussnote · Fundstelle · Ergebnis: bestätigt, korrigiert, nicht belegbar · Hinweis). Claude korrigiert Fehler; was sich nicht belegen lässt, wird mit der Aussage, die es tragen sollte, gestrichen oder umformuliert, so dass die verbleibende Aussage belegt ist.

### 9. Schlussprüfung
Den ganzen Text nach den Prüfpunkten des Skills `pruefung` durchgehen (Rechtschreibung und Grammatik, Zitierrichtlinie, Rang der Aussagen und Aufbau, Widersprüche und Wiederholungen, Querverweise, Formatvorgaben, Begriffe und Klarheit, typische Fehlerquellen), ohne dessen Markup- und Kommentarschritt: Claude behebt die Befunde direkt in der Markdown-Datei. Dazu nochmals `pipeline/kommentar.py` (Format und Neutralität, muss ohne Befund durchlaufen). Die Befunde mit ihrer Erledigung kommen in `arbeit/<Erlass>/art-<N>/Pruefbericht_<Datum>.md`.

### 10. Ausgeben
- `kommentare/<Erlass>/art-<N>.md`; `python3 pipeline/kommentar.py` ohne Befund; `python3 pipeline/md2site.py --pruefen` ohne Zurückhaltung.
- Status: `python3 pipeline/stand.py setze <Erlass>/art-<N> geprueft` (nach Schritt 8 und 9 vollständig) bzw. `geschrieben` (Fundstellenprüfung offen; im unbeaufsichtigten Lauf setzt das Steuerskript den Status). Veröffentlichen ist Sache der Person (Commit und Push; README).
- `arbeit/<Erlass>/art-<N>/`: `01_Recherche/` (Register mit Nachträgen, Problemkarte, Gliederungsnotiz, `Lexplorer_Fundstellen.md`), `Fundstellenliste_<Datum>.md`, `Pruefbericht_<Datum>.md`.
- **Word nur auf Wunsch:** `python3 pipeline/md2docx.py kommentare/<Erlass>/art-<N>.md` (Builder des Plugins, OK-Vorlage), dann validieren und als PDF ansehen wie in Anhang B des Plugins.

Im Chat drei bis fünf Sätze: Umfang (Randnoten, Fussnoten, Entscheide im Register, davon nachgetragen), offene Fragen, die der Text als offen ausweist, Stand der Fundstellenprüfung, Zahl der Lexplorer-Suchen.

### Lexplorer sparsam (Kontingent)
Lexplorer und Lexplorer Tax zählen Suchen gegen das Monatskontingent der Person, deren Verbindung Claude nutzt (Pro 500 Suchen im Monat, Search Basic 150; Webapp und MCP zusammen).
1. **Entscheide nie über Lexplorer**, auch nicht lesend; Bundesgericht über Open Case Law, kantonale Gerichte über Entscheidsuche. Lexplorer Tax für kantonale Steuerbücher und Weisungen, SSK und die ILE-Literatur.
2. **Navigieren statt suchen.** Steuerbücher sind nach Artikeln gegliedert: `nav_list_sources` mit Kanton → Steuerbuch-Quelle → `nav_list_documents`, in der Liste nach der Artikelnummer filtern (z.B. «ZStB 26.»), lesen mit `get_document_slice` bzw. `get_chunk_content`. Navigieren und Lesen zählen nicht (geprüft am 17.10.2026). Eine Suche (`search_chunks_*`) nur, wo die Navigation nicht hinführt, eine je Sachfrage und Kanton.
3. **Einmal suchen, dann wiederverwenden.** Jeder gebrauchte Treffer kommt mit Abfrage, Werkzeug, Kanton, Kennung, `lexplorer_url`, tragendem Satz und Seite in `01_Recherche/Lexplorer_Fundstellen.md`; vor jeder Suche diese Datei prüfen.
4. **Budget:** Kontingent 3’000 Suchen im Monat. Höchstens 25 Suchen je Kommentierung (`search_*` und `find_leading_cases` beider Dienste), davon in der Regel 1–2 je Sachfrage für die ILE-Literatur. Claude führt den Zähler; jeder Hilfsagent erhält ein Teilbudget und meldet seine Zahl. Ist das Budget erreicht, priorisiert Claude die offenen Sachfragen und hört auf zu suchen (im unbeaufsichtigten Lauf ohne Rückfrage; im Prüfbericht vermerken).

### ILE-Literatur (Lexplorer Tax)
1. **Suchen:** je Sachfrage eine Suche `search_chunks_hybrid` (oder `search_chunks_keyword` für feste Begriffe) mit `filter_kanton: "CH"`, `filter_category: "08-institut-fuer-law-und-economics"`, `limit` 8–10; Abfrage aus Rechtsbegriff, Norm und Kernfrage («Absicht dauernden Verbleibens Art. 3 Abs. 2 DBG Lebensmittelpunkt»). Treffer aus «ILE-HSG — Lehrbuch Steuerrecht» übergehen.
2. **Lesen:** die einschlägigen Treffer mit `get_chunk_content` ganz lesen (zählt nicht als Suche); bei Bedarf Umfeld mit `get_document_slice`. Die Autor:innen stehen am Ende des Chunks («— Autor:innen: …»); fehlt die Angabe, im Dokument suchen, sonst nicht zitieren.
3. **Zitieren:** Kurzzitat in der Fussnote «Oesterhelt/Opel, FStR 2025, Rechtsprechung 2025-2, Ziff. 5.3.» (Name(n) – Fundort mit Jahr – Titel des Beitrags – Ziffer oder Abschnitt; Seitenzahl nur, wenn sie im Text steht). Im Literaturverzeichnis: «Oesterhelt Stefan/Opel Andrea, Rechtsprechung 2025-2, FStR 2025 [lexplorer_url]». Schriftenreihe und Working Papers entsprechend mit Titel und Jahr.
4. **Ablage:** jeder verwendete Treffer mit Abfrage, Chunk-ID, Autor:innen, Titel, Ziffer, tragendem Satz und `lexplorer_url` in `01_Recherche/Lexplorer_Fundstellen.md`.
5. **Gewicht:** ILE-Literatur ergänzt Rechtsprechung und Praxis; sie bestimmt nicht die Gliederung. Eigene Randnoten für Lehre nur, wo sie einen eigenen Meinungsstand trägt (Kritik, offene Frage, abweichende Auffassung).

### Hilfsagenten und Effort
Hilfsagenten startet Claude mit dem Agent-Werkzeug und setzt `effort` nach dieser Tabelle; die Vorgabe gilt als ausdrückliche Anweisung dieses Skills.

| Aufgabe | `effort` |
|---|---|
| Register: Bereinigung und Triage der Cache-Entscheide bzw. Suche ohne Pipeline (Anhang A.2) | `medium` |
| Recherche je Sachfrage (Schritt 4) | `high` |
| Fundstellenprüfung (Schritt 8) | `high` |
| Schlussprüfung Sprache und Zitierweise, je Hauptteil (Schritt 9) | `medium` |

Gliederung, Schreiben, Neutralitätsdurchgang, Widersprüche und das Beheben der Befunde macht Claude in der Hauptsitzung (Empfehlung: hohe Stufe, für die Gliederung die höchste verfügbare). Jeder Auftrag an einen Hilfsagenten ist vollständig: Norm und Fassung, Ausschnitt, erwartete Ausgabe, Lexplorer-Teilbudget mit den Regeln oben und die Regel, Zitierstrings nur aus Tool-Ergebnissen zu übernehmen. Bietet das Agent-Werkzeug keinen `effort`-Parameter, ohne ihn starten.

---

## Aufbau der Kommentierung

```
---                                            (Kopf: erlass, artikel, titel, stand, fassung; keine Autor:innen)
> **Art. [N] [Sachüberschrift]**               (Normtext, geltende Fassung)
> 1 …
> a. …
# Übersicht                                    (immer das erste Kapitel, ohne Unterüberschriften)
# Zu Art. [N] Abs. 1 [Erlass]                  (bei einer Norm ohne Absätze: je Tatbestandsmerkmal)
## Grundsatz                                   (1–2 Randnoten, nur wo der Absatz eine eigene Einordnung braucht)
## [Rechtsbegriff oder Sachfrage (Abs. 1 lit. a)]
### [Unterproblem, z.B. «Parkplatzgebühren»]
#### [nur wenn nötig]
# Zu Art. [N] Abs. 2 [Erlass]
# Rechtsfolge                                  (bei Normen ohne Absätze, nach den Tatbestandsmerkmalen)
# Abgrenzungsfragen                            (wo einschlägig)
# Verfahren                                    (wo einschlägig)
# Ausblick                                     (beschlossenes künftiges Recht, Reformen)
# Literaturverzeichnis                         (nur zitierte ILE-Literatur)
# Materialienverzeichnis
```

**Übersicht (erstes Kapitel).** Keine eigenen Kapitel «Entstehungsgeschichte», «Harmonisierung», «Vorbemerkungen» oder «Begriff und Allgemeines»; das gehört in die Übersicht, je mit fettem Stichwort und in dieser Reihenfolge:
1. **Regelungsgegenstand** (1–3 Randnoten): was die Norm regelt, ihr System und ihre Stellung im Gesetz, Zweck, konkretisierende Verordnung und Kreisschreiben.
2. **Entstehungsgeschichte** (1–3 Randnoten): Herkunft (Vorgängernorm, Botschaft), wesentliche Revisionen mit Datum und Fundstelle (AS, BBl). Revisionen, die nur eine Einzelfrage betreffen, stehen bei dieser Frage (z.B. FABI beim Maximalbetrag für Fahrkosten).
3. **Harmonisierung** (1–3 Randnoten): Parallelnorm im StHG, inhaltliche Übereinstimmung laut Rechtsprechung, Spielraum der Kantone.

**Gliederung ableiten** (Schritt 3). Zwei Quellen bestimmen die Gliederung: der Wortlaut und das Entscheidregister.
1. *Sachkomplexe aus dem Wortlaut:* je Absatz ein Kapitel der ersten Ebene («Zu Art. 10 Abs. 1 DBG», wie in den Mustern), bei einer Norm ohne Absätze je Tatbestandsmerkmal und am Schluss «Rechtsfolge», in der Reihenfolge der Norm; darunter die Rechtsbegriffe des Wortlauts. Gesetzesbegriffe in Guillemets, Normstelle in Klammern.
2. *Sachfragen aus dem Register:* Jede Sachfrage kommt unter den Rechtsbegriff, an den sie anknüpft. Der Normalfall ist die Randnote mit fettem Stichwort. Eine eigene Überschrift erhält eine Sachfrage nur, wenn (a) sie eine eigenständige Rechtsfrage ist und (b) sie Stoff für mindestens drei Randnoten trägt (Entscheidreihe, Praxisänderung oder Auseinandergehen von Bundesgericht, kantonaler Praxis und Lehre). Ein einzelner Entscheid, auch ein BGE, begründet keine eigene Überschrift.
3. *Gewicht bestimmt die Tiefe, sparsam:* Unterüberschriften nach Fallgruppen nur, wenn jede die Schwelle aus Regel 2 erreicht; eine Überschrift mit weniger als drei Randnoten wird mit der benachbarten zusammengelegt. Ein Begriff ohne Rechtsprechung erhält eine Randnote mit Vermerk.
4. *Reihenfolge:* innerhalb eines Sachkomplexes zuerst der Wortlaut, dann die Sachfragen nach Gewicht.
5. *Querschnittsfragen* (Beweislast, Verfahren, Verhältnis zu anderen Normen) erhalten ein Rahmenkapitel nur, wenn sie mehrere Sachkomplexe betreffen.
6. *Jede Frage an genau einer Stelle:* keine Doppelung zwischen Übersicht und Einzelkommentierung; Querverweise statt Wiederholung.
7. *Abdeckungsprobe:* Jeder A-Entscheid hat einen Ort im Text oder in der Fussnote; B-Entscheide gebündelt in den Fussnoten, soweit sie etwas belegen, sonst nur im Register.

Höchstens vier Ebenen unter dem Titel.

**Muster einer Sachfrage (Randnoten-Reihenfolge):**
1. Was Gesetz und Verordnung sagen (Verordnung im Text in Klammern zitiert).
2. Leitentscheid(e) des Bundesgerichts mit Sachverhaltskern; weitere BGer-Entscheide und Präzisierungen.
3. Kantonale Gerichte, mit Hinweis, ob das Bundesgericht die Linie übernommen hat.
4. Praxis: ESTV/SSK, dann Kantone gebündelt mit Abweichungen.
5. Lehre (ILE-Literatur, Meinungsstand).
6. Wo strittig oder ungeklärt: **Stand der Frage** – was entschieden ist, was offen bleibt, welche Positionen Gerichte, Praxis und Lehre mit welcher Begründung vertreten. Kein eigener Vorschlag.

Fehlt zu einer Sachfrage Rechtsprechung oder Praxis, das ausdrücklich sagen («Höchstrichterliche Rechtsprechung liegt, soweit ersichtlich, nicht vor.»).

**Schluss.** *Abgrenzungsfragen* und *Verfahren*, wo die Norm sie aufwirft; *Ausblick* für beschlossenes künftiges Recht und hängige Reformen, sachlich beschrieben. Offene Fragen stehen dort, wo sie sich stellen – kein Sammelkapitel.

**Umfang.**
- *Umfangsplan vor dem Schreiben* in der Gliederungsnotiz: je Überschrift die geplante Zahl der Randnoten und die Summe. Richtwert sind OK-Kommentierungen zu Normen mit ähnlich viel Stoff (im OK DBG rund 50 Randnoten bei Art. 14 DBG bis über 160 bei Art. 26 DBG); jede Überschrift mit mehr als etwa zehn Randnoten und eine Summe über dem Richtwert begründen.
- *Was in den Text gehört:* die Regel, ihre Begründung durch Gesetz, Gericht oder Materialien, die Entscheide, die sie setzen oder ändern, Abweichungen der Praxis und der Meinungsstand. Gleichlaufende Kasuistik gebündelt in die Fussnoten; was nichts belegt, bleibt im Register.
- *Kürzungsdurchgang:* Randnoten streichen, die den Wortlaut oder eine andere Randnote wiederholen; Sätze, die nicht die kommentierte Norm betreffen; Sachverhaltsschilderungen ausser bei Leitfällen auf einen Halbsatz kürzen; Überschriften mit weniger als drei Randnoten zusammenlegen.

---

## Checkliste vor der Ausgabe

**Inhalt**
- [ ] Titel ohne Autor:innen; Normtext in der geltenden Fassung; künftige Fassung im Ausblick?
- [ ] Übersicht als erstes Kapitel mit Regelungsgegenstand, Entstehungsgeschichte (1–3 Randnoten) und Harmonisierung (1–3 Randnoten); keine eigenen Kapitel dafür?
- [ ] Entscheidregister vollständig (Cache der Pipeline plus Leitentscheide und frühere Fassungen nach A.1, bzw. alle Suchwege aus A.1; A-Entscheide an der Erwägung gelesen)?
- [ ] Gliederung aus Wortlaut und Register; eigene Überschriften nur über der Schwelle; Abdeckungsprobe; Umfangsplan eingehalten oder begründet; Kürzungsdurchgang gemacht?
- [ ] Quellenrangfolge je Sachfrage; Rang jeder Aussage erkennbar; Lehre nur aus der ILE-Literatur (ohne Lehrbuch Hongler/Lorenz), in der Fussnote nach dem Entscheid mit gl.M., a.M., vgl.; keine Websuche?
- [ ] **Keine eigene Meinung:** kein U.E., keine Bewertung, keine Prognose; Neutralitätsdurchgang ohne Treffer; offene Fragen als offen dargestellt?
- [ ] Keine gelbe Markierung, kein `==`?
- [ ] Aufbau, Sprache und Fussnoten am Muster geprüft (Anhang M); wertende Stellen der Muster nicht übernommen, sondern neutral umgeschrieben (M.4); Hongler/Lorenz nirgends zitiert?
- [ ] Jede Fundstelle am Volltext geprüft (Fundstellenliste des Hilfsagenten, alle Befunde behoben); Nicht-Belegbares gestrichen?
- [ ] Schlussprüfung nach den Prüfpunkten von `pruefung` gemacht und Befunde behoben (Prüfbericht)?
- [ ] ILE-Literatur je Sachfrage geprüft; Lexplorer-Budget (25) eingehalten, Zahl der Suchen gemeldet?

**Zitierweise und Format**
- [ ] Erlasse bei der Erstnennung mit Titel, Datum, SR-Nummer und «nachfolgend: …»; Kurzzitate lösen sich im Verzeichnis auf; Fussnoten enden mit Punkt; Datumsformate nach Richtlinie?
- [ ] Markdown nach `docs/FORMAT.md`; `pipeline/kommentar.py` ohne Befund; `md2site.py --pruefen` ohne Zurückhaltung; Status gesetzt? (Word nur auf Wunsch: Builder fehlerfrei, `validate.py`, PDF angesehen.)
- [ ] Pro Randnote ein Gedanke und genau ein fettes Stichwort?

---

## Anhang A – Entscheidregister, Problemkarte und Gliederungsnotiz

### A.1 Suchwege (alle ausführen, Ergebnisse vereinigen)
Das Register erfasst jeden Entscheid des Bundesgerichts, der die Norm in den Erwägungen zitiert. Mit Projektordner erledigt `pipeline/entscheide.py` die ersten drei Wege (Kandidaten über Entscheidsuche, Volltexte und Zitierstrings aus Open Case Law; die Artikelsuche von Open Case Law allein ist zu unscharf); dann nur noch die Wege ab `find_leading_cases`. Ohne Projektordner alle Wege ausführen und die Trefferzahl je Weg festhalten.

| Weg | Abfrage (Beispiel Art. 26 DBG) | Zweck |
|---|---|---|
| Open Case Law `search_decisions`, `court: bger`, `fields: compact`, `limit` bis 2000; mit `offset` blättern, bis `has_more` falsch ist | `"Art. 26 DBG" OR "art. 26 LIFD"` · `"Art. 26 Abs." AND DBG` · `"art. 26 al." AND LIFD` · `"art. 26 cpv." AND LIFD` | Volltext in DE, FR, IT, auch Zitate mit Absatz oder Buchstabe |
| dieselben Abfragen mit `court: bge` | wie oben | publizierte Leitentscheide |
| Entscheidsuche `search`, `hierarchy: ["CH_BGer"]` bzw. `["CH_BGE"]`, `size: 100`; mit `next_cursor` als `search_after` blättern | `"Art. 26 DBG" OR "art. 26 LIFD"` und die Varianten oben | Gegenprobe zu Open Case Law: Entscheide, die dort fehlen, ins Register aufnehmen |
| Open Case Law `find_leading_cases` (`law_code`, `article`, `court: bger`) | `DBG`, `26` | Rangfolge der Leitentscheide mit Pinpoint-Erwägung |
| frühere Fassungen | `"aArt. 26 DBG"`; Vorgängernorm gemäss Entstehungsgeschichte | ältere Rechtsprechung, die heute noch zitiert wird |
| Parallelnorm im StHG (ergänzend) | z.B. `"Art. 9 Abs. 1 StHG"` | Entscheide zur kantonalen Parallelnorm mit Bezug auf die DBG-Norm |

Grössenordnung (Art. 26 DBG, Oktober 2026): rund 460 BGer-Entscheide mit «Art. 26 DBG» oder «art. 26 LIFD», rund 90 weitere nur mit deutscher und rund 80 nur mit französischer Absatzangabe, mindestens 13 BGE. Ein einzelner Suchweg genügt also nie.

### A.2 Bereinigen und triagieren
- **Zusammenführen:** gleiche Geschäftsnummer; BGE und zugehöriges BGer-Urteil als ein Eintrag mit beiden Fundstellen; vereinigte Verfahren als ein Eintrag.
- **Fehltreffer streichen:** gleiche Artikelnummer eines anderen Erlasses, blosse Normketten ohne Bezug.
- **Klasse** nach Regeste und Pinpoint (`get_regeste`, `find_relevant_erwaegung`): **A** tragend – die Erwägung legt die Norm aus oder entscheidet eine Sachfrage daraus; **B** Anwendung – Subsumtion nach bekannten Grundsätzen, Kasuistik; **C** Erwähnung – Normkette, Sachverhalt, Prozessgeschichte.
- **Lesen:** A an der einschlägigen Erwägung im Volltext (`get_erwaegung`); B über Regeste und Pinpoint; C nur zählen.
- **Fassung:** Entscheide zu einer früheren Fassung kennzeichnen (Steuerperiode im Entscheid; Fedlex `list_amendments`, Open Case Law `get_article_history`); ob die Aussage für das geltende Recht trägt, steht in der Spalte «Fassung».
- **Menge:** Ab etwa 100 Treffern parallel arbeiten – Hilfsagenten je Zeitraum oder je Absatz/Buchstabe; jeder liefert Registerzeilen nur aus Tool-Ergebnissen (`effort: medium`).

### A.3 Register (eine Zeile je Entscheid)

| Entscheid | Datum | Besetzung | Normstelle | Sachfrage | Kernaussage (ein Satz) | E. | Ergebnis | Klasse | Fassung |
|---|---|---|---|---|---|---|---|---|---|

Ablage: `arbeit/<Erlass>/art-<N>/01_Recherche/Entscheidregister.md` (von Claude angelegt). Die Zitierstrings stammen aus den Tool-Ergebnissen (`citation_string_de`).

### A.4 Problemkarte
Das Register, nach Sachfragen verdichtet: Sachfrage · Normstelle und Rechtsbegriff · Zahl der A- und B-Entscheide · Leitentscheid(e) · Linie in einem Satz · Brüche und Praxisänderungen · offen oder strittig. Gleiche Sachfragen gleich benennen, ähnliche zusammenlegen. Die Problemkarte ist die Grundlage der Gliederung.

### A.5 Gliederungsnotiz (Arbeitsablage)
- die Gliederung, je Überschrift mit den tragenden Entscheiden, dem Grund für die eigene Überschrift und der geplanten Zahl der Randnoten (Umfangsplan mit Summe);
- Sachfragen, die bewusst keine eigene Überschrift erhalten haben, mit ihrem Ort;
- die Abdeckungsprobe: Zahl der A- und B-Entscheide, davon im Text, in Fussnoten, nur im Register;
- die Fragen, die der Text als offen ausweist, mit den Positionen und Fundstellen.

Die Gliederungsnotiz dient der späteren Nachführung (neue Rechtsprechung einordnen) und wird nicht veröffentlicht.

### A.6 Standardkommentare und übrige Lehre
Lehre ausserhalb der ILE-Literatur wird nicht recherchiert und nicht als eigene Fundstelle zitiert. Gibt ein Entscheid oder ein ILE-Beitrag eine solche Lehrmeinung wieder, ist dieser die Fundstelle («Das Bundesgericht verweist auf die Lehre, wonach …»).

---

## Anhang M – Mustervorlage Grieder/Hongler

Ausgewertet am 19.10.2026 (alle sechs deutschen Fassungen vollständig gelesen). Bei Widerspruch gehen das Format (Anhang G) und die Zitierrichtlinie des Plugins (Anhang C) vor.

### M.1 Bestand und Volltexte

| Kommentierung | Randnoten / Fussnoten | Gliederung | Id |
|---|---|---|---|
| Art. 10 DBG | 38 / 60 | I. Übersicht – II. Zu Art. 10 Abs. 1 DBG – III. Zu Art. 10 Abs. 2 DBG | 84dd8849-7ab8-440d-9fdf-b24f05b8d397 |
| Art. 11 DBG | 10 / 21 | I. Übersicht – II.–IV. je ein Tatbestandsmerkmal – V. Rechtsfolge | cfd2c066-dcbb-4ee0-9c98-c0ae14566770 |
| Vorb. zu Art. 13–14a StHG | 20 / 38 | Einleitung – Harmonisierungsrechtliche Vorgaben – Verfassungsrechtliche Vorgaben | 726b27c6-cfff-4b1f-a17a-a1d2e0e80273 |
| Art. 13 StHG | 67 / 120 | I. Übersicht – II.–V. Zu Art. 13 Abs. 1–4 StHG | ecb6c5b1-44f1-4d9d-81a1-a8a4a61ce25e |
| Art. 14 StHG | 82 / 134 | I. Übersicht – II.–IV. Zu Art. 14 Abs. 1–3 StHG | 4658392b-2f8e-47eb-80fa-4b8f9f4c50c0 |
| Art. 14a StHG | 7 / 8 | I. Vorbemerkungen und systematische Einordnung – II. Harmonisierungsrechtliche Vorgabe | 4c7e55f5-af48-4c70-925c-b20c6fdc03b1 |

Volltext holen: mit dem Plugin `python3 -I <Plugin>/skills/steuerkommentar/scripts/ok_muster.py muster -o 01_Recherche/Muster`; sonst `https://onlinekommentar.ch/api/commentaries/<Id>` (Shell oder WebFetch; JSON mit `content` als HTML, Fussnoten in `<footnote>`). Wahl des Musters: Zurechnungs- oder Subjektnorm → Art. 10/11 DBG; Norm mit mehreren Absätzen und viel Rechtsprechung → Art. 13/14 StHG; kurze Spezialnorm → Art. 14a StHG. Der Umfang folgt dem Stoff (7 bis 82 Randnoten), rund 1,6 Fussnoten je Randnote.

### M.2 Aufbau
- Ebenen I. – A. – 1. – a.; Verzeichnisse am Schluss.
- «I. Übersicht»: was die Norm regelt und welche Funktion sie hat («ist in materieller Hinsicht als reine Zurechnungsnorm konzipiert», «ist als Bindeglied zwischen … zu verstehen»), bei mehreren Voraussetzungen eine Liste in der Randnote. In diesem Skill folgen dort Entstehungsgeschichte und Harmonisierung (je 1–3 Randnoten); die Muster setzen sie in eine kurze Einleitung des Absatzkapitels («Bedeutung für die Steuerharmonisierung», «Entwicklung und gesetzgeberische Leitidee»).
- Hauptkapitel je Absatz («II. Zu Art. 10 Abs. 1 DBG») oder je Tatbestandsmerkmal mit «Rechtsfolge» am Schluss.
- Sachüberschriften nach Rechtsbegriffen und Problemen («Erfasste Personengemeinschaften», «Schuldenabzug», «Kunst- und Schmuckgegenstände»); innerhalb einer Sachfrage sammelnde Überschriften («Kasuistik der bundesgerichtlichen Eingriffe», «Bundesgerichtliche Leitplanken», «Kantonale Bewertungssysteme», «Tragweite der harmonisierungsrechtlichen Vorgabe»), Abgrenzungen am Ende des Absatzkapitels («Abgrenzung zur materiellen Steuerbarkeit»), «Exkurs: …» für eine nötige Nebenfrage.
- Bei StHG-Normen ist der rote Faden die Frage, wie viel Spielraum den Kantonen bleibt und wie weit das Bundesgericht ihn einschränkt (freie Prüfung oder nur Willkür).
- Kapitel dürfen mit einer zusammenfassenden Randnote schliessen («Zusammenfassend lässt sich festhalten, dass …»), wenn sie nur Gesagtes bündelt.

### M.3 Randnoten, Sprache, Fussnoten
- Eine bis sechs Sätze je Randnote; Listen für Voraussetzungen, Ansätze der Lehre und Kasuistik, jeder Punkt mit eigener Fussnote. Die veröffentlichten Muster haben keine fetten Stichwörter; hier gilt: genau ein fettes Stichwort je Randnote (Anhang G).
- Rang im Satz: «Nach ständiger Rechtsprechung des Bundesgerichts …», «Das Bundesgericht hielt dazu fest, dass … (Konjunktiv)», «In einem Urteil des Verwaltungsgerichts des Kantons Zürich, welches vom Bundesgericht bestätigt wurde, …», «nach der Verwaltungspraxis», «Die im KS 30 SSK statuierte Verwaltungspraxis …», «Mehrere kantonale Verwaltungspraxen sehen vor, …», «In der Lehre wird …», «Nach Weissbrodt …», «Diese Behandlung wird in der Lehre kritisiert.»
- Lücken: «Das Bundesgericht hat sich – soweit ersichtlich – bislang nicht dazu geäussert.», «hat das Bundesgericht offengelassen», «Soweit ersichtlich fehlt es an einer bundesgerichtlichen Rechtsprechung, weswegen ein entsprechender kantonaler Gestaltungsspielraum besteht.»
- Wörtliche Zitate aus Entscheiden in Guillemets, wo die Formel zählt; französische im Original und kursiv, danach ihre Bedeutung in einem Satz.
- Fussnoten: Erlass-Erstnennung «Bundesgesetz über die direkte Bundessteuer vom 14.12.1990 (SR 642.11; nachfolgend: DBG).»; Belege in der Reihenfolge BGE (chronologisch) – BGer (chronologisch) – kantonale Gerichte – Praxis – Lehre; «VGer ZH SB.2015.00127 vom 13.7.2016, E. 3.1; bestätigt in BGer 2C_796/2016, 2C_797/2016 vom 3.5.2017, E. 7.3 f.»; «KS 25 ESTV, Ziff. 3.1.»; «Kommentar 2025 KS 28 SSK, S. 11.»; «St.Galler Steuerbuch, StB 63 Nr. 1, Ziff. 3.4 f.»; «Reich, § 14 N. 3.»; «Botschaft KAG, S. 6429.»; Signalwörter «Vgl.», «Vgl. ferner», «Vgl. ausführlich», «m.w.H.», Gegenmeinung ausgeschrieben («Anderer Ansicht ist Ramseier, § 44 StG-BL N. 18, gemäss welchem …»); interne Querverweise «Vgl. dazu die Ausführungen in N. 15.», andere OK-Kommentierungen «OK-Grieder/Hongler, Art. 14 StHG N. 24». Jede Fussnote endet mit Punkt.
- Verzeichnisse: Literatur alphabetisch «Name Vorname», OK-Kommentierungen mit Link in eckigen Klammern; Materialien mit Datum, Direktlink und «besucht am».

### M.4 Wertende Stellen der Muster neutral umschreiben
Die Muster enthalten eigene Auffassungen der Autoren. In diesem Skill werden sie nie übernommen, auch nicht sinngemäss; an ihre Stelle tritt der Stand der Frage.

| Muster (eigene Wertung) | Hier (neutral) |
|---|---|
| «Nach der hier vertretenen Auffassung erfasst Art. 10 Abs. 1 DBG nicht jede einfache Gesellschaft.» | «Ein Teil der Lehre will Art. 10 Abs. 1 DBG auf einfache Gesellschaften beschränken, die auf die gemeinsame Erzielung von Einkommen ausgerichtet sind.» + Fussnote; «Das Bundesgericht hat die Frage, soweit ersichtlich, nicht entschieden.» |
| «Unseres Erachtens ist es überzeugend, die Wirkung von Doppelbesteuerungsabkommen einzubeziehen.» | «In der Lehre wird vorgeschlagen, die Wirkung von Doppelbesteuerungsabkommen einzubeziehen.» + Fussnote |
| «Steuersystematisch überzeugt diese Asymmetrie nur bedingt.» | «Die Lehre weist auf die unterschiedliche Prüfungsdichte bei Steuerobjekt und Bewertung hin.» + Fussnote, oder Beschreibung des Befunds ohne Urteil |
| «… dürften sich damit als harmonisierungswidrig erweisen.» | Was das Bundesgericht entschieden hat und welche kantonalen Praxen davon abweichen; ob sie halten, nur als Aussage eines Gerichts oder der Lehre |
| «Vielmehr spricht alles dafür, dass ein gesetzgeberisches Versehen vorliegt.» | «Hess sieht darin ein gesetzgeberisches Versehen.» + Fussnote |
| «wie Teuscher/Lobsiger zurecht festhalten» | «wie Teuscher/Lobsiger festhalten» |
| «Wie an anderer Stelle detailliert diskutiert wurde, …» (eigene Publikation) | «Hongler/Thirumamany weisen darauf hin, dass …» + Fussnote (gewöhnliche Lehre) |

Lehre stammt in diesem Skill nur aus der ILE-Literatur (A.6). Ein Rechtsvergleich (etwa § 15 Abs. 2 EStG) oder der Blick auf Doppelbesteuerungsabkommen bleibt zulässig, wenn er Lehre oder Rechtsprechung wiedergibt und nicht eine eigene Lösung stützt.

### M.5 Was die Muster zitieren
Rechtsprechung dominiert (in Art. 14 StHG rund 60 verschiedene BGE und BGer-Entscheide), dazu kantonale Gerichte, Kreisschreiben von ESTV und SSK, kantonale Steuerbücher, Standardkommentare, Lehrbücher für die Praxis (Reich, Blumenstein/Locher, Simonek, von Ah), Aufsätze und Monografien. Lehre hier nur aus der ILE-Literatur (Abschnitt «ILE-Literatur», Anhang A.6). Hongler/Lorenz, Einführung in das schweizerische Steuerrecht, wird nicht zitiert.

---

## Anhang G – Markdown-Format (Kurzfassung von `docs/FORMAT.md`)

```markdown
---
erlass: DBG                    # DBG, StHG, VStG, MWSTG oder StG
artikel: "26"                  # wie in Fedlex: "26", "37a", "205bbis"
titel: Berufskosten            # Sachüberschrift
stand: 2026-10-26              # Stand der Bearbeitung
fassung: Fassung vom 2.9.2026
---

> **Art. 26 Berufskosten**
> 1 Als Berufskosten werden abgezogen:
> a. die notwendigen Kosten …

# Übersicht

{rn:gegenstand} **Regelungsgegenstand.** Art. 26 DBG regelt …^[Bundesgesetz über die direkte Bundessteuer vom 14.12.1990 (SR 642.11; nachfolgend: DBG).]

{rn:entstehung} **Entstehungsgeschichte.** … (vgl. N. {{N:gegenstand}}).^[Botschaft …, BBl …, S. ….]

# Zu Art. 26 Abs. 1 DBG

## Fahrkosten (Abs. 1 lit. a)

{rn:fahrkosten-grundsatz} **Notwendige Kosten.** Eine Randnote darf eine Aufzählung enthalten:
- erster Punkt;^[Beleg.]
- zweiter Punkt.^[Beleg.]

# Literaturverzeichnis

- Oesterhelt Stefan/Opel Andrea, Rechtsprechung 2025-2, FStR 2025 [lexplorer_url].

# Materialienverzeichnis

## Bund

- Botschaft … vom …, BBl … [Link], besucht am ….
```

- Ebenen `#` bis `####` = I. – A. – 1. – a.; keine Nummern schreiben, das Skript nummeriert.
- Jeder Textabsatz ausserhalb der Verzeichnisse ist eine Randnote (`{rn}` oder `{rn:label}`); die Nummern vergibt das Skript. Labels kurz und sprechend; Querverweise nur über Labels.
- Fussnoten inline `^[…]`, jede mit Schlusspunkt; eckige Klammern darin sind erlaubt.
- Leerzeile zwischen Absätzen; eine Randnote ist ein Absatz.
