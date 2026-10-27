# Prüfbericht Art. 15 DBG – Einbau der ILE-Literatur (27.10.2026)

## Auftrag und Vorgehen

Bestehende, geprüfte Kommentierung (Status «geprueft», online) um die Literatur des ILE-HSG aus Lexplorer Tax ergänzt; Status und Reservierung unverändert. Bestehender Text sonst nicht umgeschrieben, bestehende Labels nicht geändert. Lehrbuch Hongler/Lorenz übergangen. Keine Websuche.

## Recherche

- Lexplorer-Tax-Suchen: **9** (`search_chunks_hybrid`, Kanton CH, Kategorie 08-institut-fuer-law-und-economics, limit 8–10); Budget 25. Ab der fünften Suche lieferten die Suchen nur noch dieselben drei Beiträge oder nicht einschlägige Treffer; deshalb Abbruch der Suche.
- Lesen mit `get_chunk_content`, `get_document_slice`, `nav_list_chunks` (zählen nicht als Suche); Abfragen, Chunk-IDs, tragende Sätze und lexplorer_url in `01_Recherche/Lexplorer_Fundstellen.md`.
- Autor:innen am Beitrags- bzw. Kapitelkopf geprüft: Baumann/Dorasamy (Beitragskopf FStR 2023/4), Berdoz/Bugnon (Kapitelkopf «La procédure mixte en matière d'impôts directs», Segment I–III), Seiler (Kapitelkopf § 10).

## Eingefügte Fundstellen

Drei Werke, 31 Fundstellen in Fussnoten (Baumann/Dorasamy 23, Berdoz/Bugnon 6, Seiler 2), verteilt auf 15 Randnoten:

| Randnote | Art der Einfügung | Fundstelle(n) |
|---|---|---|
| zweck | gl.M. in zwei Fussnoten | Baumann/Dorasamy Ziff. 4.1 |
| entstehung | vgl. | Baumann/Dorasamy Ziff. 4.2.1.2 |
| begleitpersonen | zwei neue Sätze (Lehre) | Baumann/Dorasamy Ziff. 4.1, 4.2.1.2; Berdoz/Bugnon Ziff. IV.C.1.a |
| verweis | gl.M. in zwei Fussnoten | Berdoz/Bugnon Ziff. IV.C.1, IV.C.1.c; Baumann/Dorasamy Ziff. 4.2.1.2 |
| kategorien | vgl. | Baumann/Dorasamy Ziff. 4.1 und 4.2.1.2 |
| wued | vgl.; zwei neue Sätze (Lehre) | Baumann/Dorasamy Ziff. 2, 4.2.1.2; Berdoz/Bugnon Ziff. IV.C.1.a |
| rente-diplomat | gl.M. | Baumann/Dorasamy Ziff. 4.2.1.2 |
| renten | gl.M. | Berdoz/Bugnon Ziff. IV.C.1.c; Baumann/Dorasamy Ziff. 4.2.1.2 |
| schweizer | ein neuer Satz (Doppelbürger) | Baumann/Dorasamy Ziff. 4.2.1.2 |
| schweizer-beamte | gl.M.; ein neuer Satz (internes Besteuerungssystem) | Seiler § 10 Ziff. I; Berdoz/Bugnon Ziff. IV.C.1.c; Baumann/Dorasamy Ziff. 4.2.1.2 |
| **progression-lehre (neu)** | neue Randnote «Meinungsstand» zum Progressionsvorbehalt | Baumann/Dorasamy Ziff. 4.2.1.2 |
| satz-ehegatten | a.M. bei TAPI GE, gl.M. bei CDAP VD; ein neuer Satz | Baumann/Dorasamy Ziff. 4.2.1.2 |
| statuswechsel | a.M. bei TA GE; ein neuer Satz | Baumann/Dorasamy Ziff. 4.2.1.1, 4.2.1.2 |
| aufwand | gl.M. | Baumann/Dorasamy Ziff. 4.2.1.2 |
| entsendestaat | vgl. | Seiler § 10 N. 6; Baumann/Dorasamy Ziff. 4.2.1.1 |

Neue Randnoten: 1 (`progression-lehre`). Randnoten jetzt 24 (vorher 23), Fussnoten 64. Literaturverzeichnis neu angelegt (vor dem Materialienverzeichnis), drei Einträge.

## Entscheide im unbeaufsichtigten Lauf

- Titel Baumann/Dorasamy nach der Überschrift des Beitrags («Questions choisies en matière de fiscalité et d'immigration»); der deutsche Lexplorer-Segmenttitel «Diplomaten und internationale Beamte in der Schweiz» ist im Text nicht als Beitragstitel belegt.
- Seiler § 10: Randziffern 3 und 4 fehlen im Lexplorer-Text; Zitat für die Aussage zu Schweizer Staatsangehörigen daher nach Abschnitt («§ 10 Ziff. I»), für Art. 3 Abs. 5 DBG nach der ausgewiesenen N. 6.
- Bucher (IFF-Schriftenreihe 2023) nicht verwendet: vollständiger Werktitel nicht feststellbar, Aussage (deklaratorischer Charakter) bereits anderweitig belegt.
- Die Angaben von Baumann/Dorasamy zu den Legitimationskarten (subjektive Befreiung für Karten B, C, D) wurden nicht übernommen, weil sie sich mit der Darstellung von BGer 2P.36/2004 (Karten C und D, objektive Befreiung; Steuerperiode 1998) nicht ohne Weiteres decken; zitiert wird nur die Unterscheidung subjektiv/objektiv.
- Kein Prüf-Hilfsagent verfügbar (kein Agent-Werkzeug in dieser Sitzung); Fundstellenprüfung als getrennter Arbeitsschritt nach Abschluss des Einbaus.

## Fundstellenprüfung (getrennter Durchgang am Chunk)

Jede neu eingefügte Fundstelle mit `get_chunk_content` am Chunk geprüft (Autor:innen, Fundort, Ziffer, trägt die Stelle die Aussage):

| Fundstelle | Chunk | Ergebnis |
|---|---|---|
| Baumann/Dorasamy Ziff. 2 (Fn. 21) | 46cab1bf | bestätigt |
| Baumann/Dorasamy Ziff. 4.1 (Zweck, Begleitpersonen, Fn. 131, Formen der Befreiung) | 9f1fe3ae | bestätigt |
| Baumann/Dorasamy Ziff. 4.2.1.1 (unbeschränkte Steuerpflicht; Art. 3 Abs. 5 DBG) | e35ad54a | bestätigt |
| Baumann/Dorasamy Ziff. 4.2.1.2 (keine eigene Tragweite; Kreis der Begünstigten; Progressionsvorbehalt) | aef763d2, ae36e74c (Fn. 152–154) | bestätigt |
| Baumann/Dorasamy Ziff. 4.2.1.2 (Schweizer, Doppelbürger, internes Besteuerungssystem, subjektiv/objektiv) | d1a1fec0 | bestätigt |
| Baumann/Dorasamy Ziff. 4.2.1.2 (Einkünfte aus schweizerischen Quellen; Kapitalerträge) | 2cec714d, ae36e74c | bestätigt |
| Baumann/Dorasamy Ziff. 4.2.1.2 (objektive Befreiung, Satz) | f36bf6be | bestätigt |
| Baumann/Dorasamy Ziff. 4.2.1.2 (Dauer, Pensionen, frühere Renten, Ausweis Ci, Ehegatten) | aedeeb9e | bestätigt |
| Baumann/Dorasamy Ziff. 4.2.1.2 (Aufwandbesteuerung) | 97926b47 | bestätigt |
| Berdoz/Bugnon Ziff. IV.C.1 | 4889ba15 | bestätigt |
| Berdoz/Bugnon Ziff. IV.C.1.a | 81aa056e | bestätigt |
| Berdoz/Bugnon Ziff. IV.C.1.c | dd36eac8 | bestätigt |
| Seiler § 10 Ziff. I | 0adf4c19 | bestätigt |
| Seiler § 10 N. 6 | a99b3770 | bestätigt |

Geprüft: 31 Fundstellen (14 Prüfpositionen); korrigiert: 0 im Kommentar (nur Chunk-IDs in der Ablage nachgetragen); gestrichen: 0.

## Schlusskontrolle

- `python3 pipeline/kommentar.py kommentare/DBG/art-15.md`: 24 Randnoten, 64 Fussnoten, 0 Befunde (Format und Neutralität).
- Wertungen der Autor:innen nur als deren Auffassung in indirekter Rede; kein U.E.
- Bereits vorhandene Literaturzitate (über Entscheide wiedergegebene Lehre) unverändert.
- Kopf `stand: 2026-10-27`.
