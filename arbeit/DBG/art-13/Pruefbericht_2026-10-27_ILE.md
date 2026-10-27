# Prüfbericht Art. 13 DBG – Einbau der ILE-Literatur (27.10.2026, unbeaufsichtigter Lauf)

## Auftrag und Rahmen
- Einbau der Literatur des ILE-HSG aus Lexplorer Tax in die bestehende, geprüfte Kommentierung; übriger Text unverändert, Status bleibt «geprueft», keine Reservierung.
- Lehrbuch Hongler/Lorenz («ILE-HSG — Lehrbuch Steuerrecht») nicht verwendet (Treffer übergangen).
- Ablage aller verwendeten Treffer: `01_Recherche/Lexplorer_Fundstellen.md`.

## Suchen
- 14 Suchen in Lexplorer Tax (13 `search_chunks_hybrid`, 1 `search_chunks_keyword`), alle mit `filter_kanton: "CH"` und `filter_category: "08-institut-fuer-law-und-economics"`; Budget 25 eingehalten. Lesen über `get_chunk_content`, `get_document_slice` und `nav_find` (zählen nicht als Suche).
- Ohne einschlägigen Treffer (nichts eingefügt): Kinder unter elterlicher Sorge (Abs. 1 Satz 3, Abs. 3 lit. a), Teilhaber (Abs. 3 lit. b), Auflösung/Veräusserung bis zum Reinerlös (Abs. 3 lit. d), Haftung von Erbschaftsverwalter und Willensvollstrecker (Abs. 4), Nachsteuer und Bussen.

## Eingefügte Fundstellen
- 47 ILE-Fundstellen in 39 Fussnoten (19 neue Fussnoten, 20 bestehende ergänzt); 7 Beiträge, alle neu im Literaturverzeichnis (das Verzeichnis fehlte bisher und steht nun vor dem Materialienverzeichnis):
  - Rajower/Weber Rajower, Ehegatten- und Erbenhaftung im Recht der direkten Steuern, FStR 2009 (26 Fundstellen);
  - Oesterhelt/Opel, Rechtsprechung 2024/1, FStR 2024 (Besprechung BGE 149 II 442; 10);
  - Rostetter, Die Verjährung im Recht der direkten Bundessteuer und der harmonisierten kantonalen Steuern, IFF-Schriftenreihe 2019 (6);
  - Rajower, Sicherstellung und Arrest … (1. Teil), FStR 2007 (1) und (2. Teil), FStR 2007 (2);
  - Oesterhelt/Opel, Rechtsprechung 2025-2, FStR 2025 (Besprechung BGE 151 II 409; 1);
  - Fenners/Baumgartner/Duss, Gesetzgebungs-Agenda 2026/3, FStR 2026 (1).
- Neue Randnoten (2): `kritik-solidarhaftung` (Kritik der Lehre an der Solidarhaftung: eherechtlicher Einwand, Verfassungsmässigkeit, Wahlrecht der Behörde) und `mithaftung-verjaehrung` (Rostetter zur Verjährung gegenüber Mithaftenden nach Abs. 3). Bestehende Labels unverändert.
- Meinungsstand mit «a.M.»: Kritik von Oesterhelt/Opel an der Solidarhaftung; ältere Lehre, die Zahlungsunfähigkeit sei nur auf Begehren zu berücksichtigen (Rajower/Weber Rajower, N. gesuch); teleologische Reduktion von Art. 120 DBG für Mithaftende (Rostetter). Weitere Lehrauffassungen in indirekter Rede ohne Übernahme: offene Frage der «mittleren Frist» (frist), Kritik an der rückwirkenden Aufhebung (rueckwirkung), Anrechnung früherer Zahlungen (offene-schulden), Berechnung der Anteile bei Ermessensveranlagung (anteil-berechnung), hypothetische pfändbare Quote (gesamtwuerdigung), Einwendungen des Mithaftenden gegen die Haftungsverfügung (anfechtung), kantonale Sonderregelungen BS/LU/AR/AI/VD (kantone).
- Ausblick: Das im früheren Prüfbericht offene Ergebnis der Volksabstimmung vom 8.3.2026 (Annahme mit 54,26 %; Umsetzung spätestens 1.1.2032) ist nun als Angabe von Fenners/Baumgartner/Duss wiedergegeben; ein amtlicher Beleg (Erwahrungsbeschluss) wurde in diesem Lauf nicht recherchiert (Auftrag auf ILE-Literatur beschränkt).
- `stand:` war bereits 2026-10-27.

## Entscheide (unbeaufsichtigt)
- Autor:innen am Kopf des Beitrags geprüft: FStR 2009 «Felix Rajower/Ursula Weber Rajower»; FStR 2007 (1. und 2. Teil) nur Felix Rajower; Gesetzgebungs-Agenda in der Reihenfolge des Kopfs (Fenners/Baumgartner/Duss, Lexplorer nennt Baumgartner, Duss, Fenners); Rostetter als Monografie eines Autors.
- Rostetter: Randziffern nur teilweise im Text sichtbar; nicht sichtbare (537, 553, 564, 567, 570, 573–575, 587) aus Querverweisen im Text und aus dem Sachregister der Monografie bestätigt (Sachregister: «Verfahrenssolidarität 537», «Hemmung … Landesabwesenheit … 553–557», «Rechtskraft – solidarische Mithaftung 567–569», «Sicherstellung … bei solidarischer Haftung 570», «Unterbrechung bei solidarischer Mithaftung 549 f., 570–578», «Verlustschein – Verjährung gegenüber Mithaftenden 587»); 575 durch Abzählen der Absätze zwischen 573 und 577.
- Literaturverzeichnis mit dokumentbezogenen lexplorer_url (`e_id`), wie sie `get_document_slice` liefert.
- Berdoz/Bugnon (Die Verfahren im Steuerrecht, 2021) gelesen, aber nicht eingebaut (keine über den Text hinausgehende Aussage).

## Prüfdurchgang (getrennter Arbeitsschritt)
Ein Hilfsagent stand in diesem Lauf nicht zur Verfügung (kein Agent-Werkzeug). Die Prüfung erfolgte deshalb als getrennter Arbeitsschritt nach dem Einbau: jede neu eingefügte Fundstelle am Chunk bzw. Dokumentausschnitt (`get_chunk_content`, `get_document_slice`) gegen Autor:innen, Fundort, Ziffer/Randziffer und tragende Aussage abgeglichen.

| Ergebnis | Zahl | Hinweis |
|---|---|---|
| bestätigt | 45 | – |
| korrigiert | 2 | Rostetter: Fussnote zur Amtshandlung gegenüber Mithaftenden auf «A.M.» gestellt und Rz 537 → «Rz 549 f.; zur Abgrenzung von der Steuersolidarität Rz 536 f.»; Landesabwesenheit «Rz 554–557» → «Rz 553–557» (Sachregister) |
| gestrichen | 0 | – |

## Format
- `python3 pipeline/kommentar.py kommentare/DBG/art-13.md`: 51 Randnoten, 123 Fussnoten, 0 Befunde (vorher 49 Randnoten, 104 Fussnoten).
- `python3 pipeline/md2site.py --pruefen`: 15 bereit, 0 mit Befunden.
