# Prüfbericht Art. 8 DBG – ILE-Literatur (27.10.2026)

Unbeaufsichtigter Lauf; Status unverändert «geprueft»; nur `kommentare/DBG/art-8.md` und `arbeit/DBG/art-8/` geändert.

## Recherche

- Lexplorer Tax, `search_chunks_hybrid`, Kanton CH, Kategorie `08-institut-fuer-law-und-economics`: **12 Suchen** (Budget 25). Abfragen und Treffer in `01_Recherche/Lexplorer_Fundstellen.md`.
- Lehrbuch Hongler/Lorenz («ILE-HSG — Lehrbuch Steuerrecht») übergangen (Treffer in Suchen 5, 6, 10, 11).
- Autor:innen am Kapitel- bzw. Beitragskopf geprüft: FStR-Rechtsprechungsübersichten (Oesterhelt/Opel; Reich/Waldburger), FStR 2009/3 (Rajower/Weber Rajower), IFF-Schriftenreihe 2021 «Die Verfahren im Steuerrecht», Kapitel «La procédure mixte en matière d'impôts directs» (Kopf im Segment I–III: Berdoz/Bugnon; Segment V–VI gehört zum selben Kapitel).
- Zu folgenden Sachfragen fand sich nichts Einschlägiges; nichts eingefügt: tagesgenaue Bestimmung, abschliessende Aufzählung, Aufenthalt, Grundstückerwerb (Beginn), Geschäftsbetriebe beim Wegzug, Bedeutung des Zeitpunkts (Kapitalleistungen), Abs. 3 (über Berdoz/Bugnon hinaus), Harmonisierung, Ausblick.

## Eingefügte Fundstellen (16; davon 1 neue Randnote)

| Randnote | Fundstelle | Art | Prüfung am Chunk |
|---|---|---|---|
| zuzug | Berdoz/Bugnon, Ziff. V.A.1 | vgl. | bestätigt (4dedfe2d) |
| wegzug-wohnsitz | Oesterhelt/Opel, FStR 2024, Rechtsprechung 2024/3, Ziff. 3.3 | gl.M. | bestätigt (835d0e1a; Ziff. 3 = BGer 29.2.2024 = BGE 150 II 244) |
| wegzug-weltenbummler | Berdoz/Bugnon, Ziff. V.C | vgl. | bestätigt (5c0b166f) |
| abmeldung | Berdoz/Bugnon, Ziff. V.B.1 | gl.M. | bestätigt (2f219709) |
| wegzug-lehre | Reich/Waldburger, FStR 2008, Rechtsprechung im Jahr 2007 (2. Teil), Ziff. 4 | a.M., Meinungsstand im Text | bestätigt (abd3fd36, bcf1c0ae; Bemerkungen zu BGer 2C_303/2007) |
| wegzug-lehre | Oesterhelt/Opel, FStR 2025, Rechtsprechung 2025-2, Ziff. 5.3 | a.M., Meinungsstand im Text | bestätigt (e21cb60c; Fn. 78: BGE 138 II 300 E. 3.6) |
| wegfall | Berdoz/Bugnon, Ziff. V.B.1 | gl.M. | bestätigt (2f219709) |
| tod-ehegatten | Berdoz/Bugnon, Ziff. V.D | gl.M. | bestätigt (25891dee) |
| erben | Rajower/Weber Rajower, FStR 2009, Ziff. 3.1.3 | gl.M. | bestätigt (077af2c8) |
| erben | Rajower/Weber Rajower, FStR 2009, Ziff. 3.2.2 | vgl. | bestätigt (94a67ec8) |
| landesversorgung-inhalt | Berdoz/Bugnon, Ziff. V.C | vgl. | bestätigt (5c0b166f) |
| wechsel-grundsatz | Oesterhelt/Opel, FStR 2025, Rechtsprechung 2025/4, Ziff. 1.3 | gl.M. | bestätigt (7a38ac73) |
| wechsel-lehre | dto. | Meinungsstand (Wertung als deren Auffassung) | bestätigt (0f96b46f) |
| wechsel-offen | dto. | Meinungsstand, offene Frage | bestätigt (fb33aa17; Fn. 9) |
| folgen-satz-beschraenkt (neu) | Oesterhelt/Opel, FStR 2023, Rechtsprechung im Steuerrecht 2023/3, Ziff. 3.3 | a.M. | bestätigt (a83f4814, 143efab4; Fn. 41: 2C_977/2020 = BGE 149 II 34) |
| folgen-satz-beschraenkt (neu) | dto. | Auffassung der Autoren | bestätigt (e8e3f920) |

Neue Randnote `folgen-satz-beschraenkt` (Rechtsfolgen): trägt einen eigenen Meinungsstand (Kritik an BGE 149 II 177). Der besprochene Entscheid wurde nach dem Original zitiert: BGE 149 II 177, E. 8.3.5 (= BGer 9C_689/2022 vom 12. April 2023), Zitierstring und Erwägung über Open Case Law (`cite`, `find_relevant_erwaegung`) geprüft; im Entscheidregister als Nachtrag erfasst.

## Prüfdurchgang

Kein Hilfsagent verfügbar (kein Agent-Werkzeug in dieser Sitzung); Prüfung als getrennter Arbeitsschritt: jede neue Fundstelle erneut mit `get_chunk_content` gelesen und gegen den Text geprüft (Autor:innen, Fundort, Ziffer anhand der Abschnittsüberschriften im Dokument, Tragweite der Aussage). Ergebnis: 16 bestätigt, 0 korrigiert, 0 gestrichen.

Wertungen der Autor:innen nur in indirekter Rede («begrüssen», «halten für fraglich», «wenden ein»); keine eigene Stellungnahme. Bestehende Literaturzitate (De Vries Reilingh, Obrist) unverändert.

## Schlussprüfung

- `python3 pipeline/kommentar.py kommentare/DBG/art-8.md`: 35 Randnoten (zuvor 34), 87 Fussnoten, 0 Befunde.
- Kopf `stand: 2026-10-27`.
- Literaturverzeichnis um sechs ILE-Titel ergänzt (alphabetisch, mit lexplorer_url des Dokuments).
