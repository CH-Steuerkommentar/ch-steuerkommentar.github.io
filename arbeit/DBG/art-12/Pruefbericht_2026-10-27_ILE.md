# Prüfbericht Art. 12 DBG – Einbau der ILE-Literatur (27.10.2026)

Unbeaufsichtigter Lauf. Auftrag: bestehende Kommentierung (Status «geprueft», online) um die Literatur des ILE-HSG aus Lexplorer Tax ergänzen, ohne den Text sonst umzuschreiben. Keine Reservierung, Status unverändert.

## Recherche

- **Zahl der Suchen: 11** (`search_chunks_hybrid`, `filter_kanton: "CH"`, `filter_category: "08-institut-fuer-law-und-economics"`, limit 8–10; Budget 25). Abfragen und Treffer in `01_Recherche/Lexplorer_Fundstellen.md` (Abschnitt «ILE-Literatur», ILE-1 bis ILE-16).
- Gelesen über `get_chunk_content`, `get_document_slice`, `nav_list_chunks`, `nav_find` (zählen nicht als Suche).
- «ILE-HSG — Lehrbuch Steuerrecht» (Hongler/Lorenz, DE und EN) erschien in mehreren Trefferlisten und wurde übergangen.
- Ohne einschlägigen ILE-Treffer blieben: Akteneinsicht vor Annahme der Erbschaft, Ausschlagung und Rechtsmissbrauch (BGer 2C_117/2017), Fristwiederherstellung und Revision, höchstpersönliche Rechte, kantonale Erbschaftssteuer, andere Abgaben (Stempel, Verrechnungssteuer). Dort wurde nichts eingefügt.

## Eingefügte Fundstellen

32 Literaturzitate in 31 Fussnoten (eine Fussnote enthält zwei Zitate), davon 1 neue Randnote:

| Werk | Zitate | Randnoten |
|---|---|---|
| Rajower/Weber Rajower, FStR 2009, Ehegatten- und Erbenhaftung im Recht der direkten Steuern | 19 | rechtsnatur, harmonisierung, haftungsbeschraenkung, erbteil (3), vorempfaenge (3), solidaritaet (2), regress, inventar-zgb, ehegatte-inhalt, ehegatte-art13, ehegatte-kantone (3), partner |
| Oesterhelt/Opel, FStR 2025, Rechtsprechung 2025-2 | 5 | wv-leitfall, wv-erbenrechte, vereinfachte-nachsteuer (3) |
| Hemmerle/Hirt, St.Galler Seminar 2019, Erb- und steuerrechtliche Sonderfragen bei der Unternehmensnachfolge | 4 | verlustvortrag, verlustvortrag-ehegatte, liquidation-erben (2) |
| Hinny/Aebi, St.Galler Seminar 2019, Kapital- vs. Personengesellschaften | 2 | verlustvortrag, verlustvortrag-ehegatte |
| Rostetter, IFF-Schriftenreihe Bd. 115 (2019), Die Verjährung … | 1 | haftungsgegenstand |
| Zigerlig/Cozzio/Hess, FStR 2004, Gesetzgebungs-Agenda 2004/4 | 1 | busse |

Art der Einfügung: bestätigend in bestehenden Fussnoten nach den Entscheiden bzw. der Praxis (gl.M./vgl.: 17), neue Sätze mit Lehrmeinung in indirekter Rede oder als Auffassung der Autor:innen (14), eine Gegenposition mit «a.M.» (Rajower/Weber Rajower gegen CDAP VD zur Haftung des ausschlagenden Ehegatten, Gegenposition im Text).

**Neue Randnote:** `verlustvortrag-ehegatte` («Überlebender Ehegatte»): Meinungsstand Hemmerle/Hirt (Verlustvorträge für den Ehegatten, der das Geschäft weiterführt, weiterhin abziehbar) gegen Hinny/Aebi (verneinend, mit Hinweis auf die abweichende Luzerner Praxis). Bestehende Labels unverändert. Neues Kapitel `# Literaturverzeichnis` vor dem Materialienverzeichnis mit 6 Einträgen.

Kein Satz übernimmt eine Wertung der Autor:innen; Wertungen («Dem ist zuzustimmen», «richtig betrachtet», «ist abzulehnen») sind als deren Auffassung wiedergegeben. Kein U.E. Die Zitate früher geprüfter Quellen blieben unverändert; `stand:` ist 2026-10-27.

## Entscheide im unbeaufsichtigten Lauf

- **Autorenreihenfolge der Seminarunterlagen:** «Hemmerle/Hirt» wie in der bestehenden Kommentierung zu Art. 10 DBG (Lexplorer-Angabe und alphabetisch; auf der Titelfolie steht Hirt zuerst); «Hinny/Aebi» nach der Titelfolie. Die Autor:innen wurden jeweils an der Titelfolie bzw. am Kapitelkopf geprüft (Hinweis auf Fehlzuordnungen in Lexplorer). Alle Zuordnungen stimmten.
- **Titel Rostetter:** Der Speicherpfad in Lexplorer ist abgeschnitten («…kantonalen St»); der Titel folgt dem bestehenden Literaturverzeichnis von art-1 und dem Wortlaut der Einleitung des Werks.
- **Zitierweise der Seminarunterlagen:** Abschnittstitel der Folie (wie in art-10), bei Hinny/Aebi zusätzlich die Foliennummer.
- **Kein Prüfagent verfügbar:** Diese Sitzung bietet kein Werkzeug für Hilfsagenten. Die Prüfung lief deshalb als getrennter Arbeitsschritt nach dem Einbau: Alle neuen Zitate wurden aus dem `git diff` herausgezogen und jeweils am Chunk (`get_chunk_content`) bzw. am vollständigen Dokumenttext (`get_document_slice`) neu gelesen.

## Fundstellenprüfung (getrennter Arbeitsschritt)

Für jedes neue Zitat geprüft: Autor:innen, Fundort, Ziffer bzw. Abschnitt, trägt die Stelle die Aussage?

| Ergebnis | Zahl | Hinweis |
|---|---|---|
| bestätigt | 30 | Ziffern bei Rajower/Weber Rajower über die Querverweise im Text abgeglichen (z.B. «Abschn. 3.3.3.1 bei Fn 173» → Haftungsbeschränkung = Ziff. 3.3.3.1) |
| korrigiert | 2 | (1) vereinfachte-nachsteuer: «hat das Bundesgericht nicht thematisiert» → «lässt sich dem Urteil nach Oesterhelt/Opel nicht entnehmen» (die Aussage stammt von den Autor:innen; «nicht thematisiert» bezogen sie auf die Form). (2) wv-erbenrechte: «ging zuvor auseinander» → «gehen auseinander» (Präsens wie im Text). Zusätzlich bei regress «In der Lehre wird …» → «Nach Rajower/Weber Rajower …», weil die Stelle selbst eine Gegenmeinung nennt. |
| gestrichen | 0 | – |

Danach `python3 pipeline/kommentar.py kommentare/DBG/art-12.md`: 39 Randnoten, 122 Fussnoten, 0 Befunde (Format und Neutralität). `python3 pipeline/md2site.py --pruefen`: keine Meldung zu art-12.
