# Prüfbericht Art. 5 DBG – Einbau der ILE-Literatur (27.10.2026)

Unbeaufsichtigter Lauf; Status unverändert «geprueft», keine Reservierung. Nur `kommentare/DBG/art-5.md` und `arbeit/DBG/art-5/` geändert; Kopf `stand: 2026-10-27`.

## Recherche
- Lexplorer-Tax-Suchen: **16** (`search_chunks_hybrid`, Kanton CH, Kategorie `08-institut-fuer-law-und-economics`, limit 8–10); Budget 25 eingehalten. Lesen mit `get_chunk_content`/`get_document_slice` (nicht gezählt).
- Ohne einschlägigen Treffer (nichts eingefügt): Abs. 2 Künstler/organisierende Dritte (2 Suchen), nachträgliche ordentliche Veranlagung/Quasi-Ansässigkeit, Personengesellschaften (Treffer nicht verwendet), internationale Wochenaufenthalter. Ohne eigene Suche (nichts eingefügt): Harmonisierung, Revisionen, a-homeoffice, a-freistellung, a-erhebungsform, a-verfahren, b-mab, b-abgrenzung, de-abgrenzung, de-luecke, f-revision, f-qst.
- Hongler/Lorenz (Lehrbuch) nicht verwendet; Hongler, IFF-Schriftenreihe 2023, § 2 ist ein anderes Werk.
- Einzelheiten: `01_Recherche/Lexplorer_Fundstellen.md`.

## Eingefügt
- **30 ILE-Fundstellen** (Fussnotenzitate) aus 10 Beiträgen: Seiler § 5 (9), Oesterhelt/Winzap FStR 2008 (5), Waldburger FStR 2012 (4), Oesterhelt/Opel FStR 2024 (3), Oesterhelt/Meier Seminar 2024 (3), Baumgartner/Duss/Fenners FStR 2025 (2), Hongler § 2 (1), Oesterhelt/Opel FStR 2023 (1), Oesterhelt/Opel FStR 2025 (1), Brozzo/Stocker Seminar 2024 (1).
- **Neue Randnoten (2):** `a-lehre-bdbst` (Würdigung von BGE 137 II 246 durch Waldburger), `c-lehre` (Umfang von lit. c nach Oesterhelt/Winzap). Bestehende Labels unverändert.
- **Meinungsstand mit a.M.:** N. subjekt (überwiegende Lehre nach Seiler gegen BGer 2A.23/2007), N. beginn (Kritik von Oesterhelt/Opel an BGE 149 II 34). Weitere Lehrmeinungen in indirekter Rede: quellensteuer, ehegatten, a-selbst, a-zufluss, abis-zweck, b-tatbestand, abs2-grundsatz.
- Bestätigend (gl.M./ebenso/vgl.) in bestehenden Fussnoten: dba (2), a-arbeitsort, a-bonus, a-qst, abis-voraussetzungen, abis-abkommen, b-tatbestand, e-grundlage, e-zeitpunkt, e-dba, f-tatbestand.
- Neu: `# Literaturverzeichnis` vor `# Materialienverzeichnis` (10 Einträge mit lexplorer_url).
- Für die neuen Sätze zu Entscheiden wurden die Pinpoints über Open Case Law gelesen: BGE 149 II 34 (= 2C_977/2020) E. 6.3.2–6.4.4; BGE 152 II 98 (= 9C_416/2024) E. 9.4.3; BGer 2C_662/2010 E. 9 (in BGE 137 II 246 nicht publiziert, daher nach dem BGer-Urteil zitiert).

## Prüfung
Kein Hilfsagent verfügbar; Prüfung als getrennter Arbeitsschritt nach dem Einbau: alle 30 neuen Fundstellen aus dem Diff gezogen und am Chunk (`get_chunk_content`, bei Bemerkungen/Folien mit `get_document_slice`) auf Autor:innen, Fundort, Ziffer/Folie und Tragfähigkeit geprüft.

| Fundstelle | Ergebnis | Hinweis |
|---|---|---|
| Seiler § 5 N. 8, 17 f., 19, 19 f., 21, 25 f., 27, 71 | bestätigt | Randnummern im Text ausgewiesen |
| Seiler § 5 N. 28 ff. | bestätigt | Absatz zur überwiegenden Lehre ohne eigene Randnummer im Chunk; daher «N. 28 ff.» (Abschnitt II.3) |
| Hongler § 2 Ziff. III.1 | bestätigt | Satz «begründet keine Steuerpflicht» im Abschnitt III.1 |
| Waldburger Ziff. 3, Bemerkungen 1–4 | bestätigt | wertende Stellen («sehr zu begrüssen», «nicht sehr überzeugend») nur als seine Auffassung wiedergegeben |
| Oesterhelt/Opel 2024/1 Ziff. 2.3 (3×) | bestätigt | |
| Oesterhelt/Opel 2023/2 Ziff. 3.3 | bestätigt | |
| Oesterhelt/Opel 2025/4 Ziff. 1.3 | korrigiert | «sei offen» → «sei nicht restlos klar» (Wortlaut der Quelle) |
| Baumgartner/Duss/Fenners 2025/1 Ziff. 1.2 (2×) | bestätigt | |
| Oesterhelt/Winzap Ziff. 2.1.1.1 | korrigiert | Satz auf Art. 94 DBG und lit. c beschränkt (Quelle spricht nur von Art. 94) |
| Oesterhelt/Winzap Ziff. 2.1.2, 2.1.4, 2.1.3.1/2.2.2/2.2.3, 2.1.1.5/2.3 | bestätigt | |
| Brozzo/Stocker, Folie «Direkter Bezug des VR-Honorars» | bestätigt | |
| Oesterhelt/Meier Folie 58 | korrigiert | «gl.M.» → «vgl.» (Folie belegt Quellensteuer bei Wohnsitz im Ausland, nicht ausdrücklich «nur») |
| Oesterhelt/Meier Folien 54 und 57, 55 | bestätigt | |

Gestrichen: keine. Nicht belegbar: keine.

## Schlussprüfung
- `python3 pipeline/kommentar.py kommentare/DBG/art-5.md`: 44 Randnoten, 104 Fussnoten, **0 Befunde** (erster Lauf meldete «überzeug» in N. a-lehre-bdbst; umformuliert zu «kritisiert er»).
- `python3 pipeline/md2site.py --pruefen`: ohne Meldung zu Art. 5.
- Neutralitätssuche (grep der verbotenen Wendungen): ohne Treffer.
