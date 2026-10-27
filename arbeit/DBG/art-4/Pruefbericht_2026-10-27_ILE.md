# Prüfbericht Art. 4 DBG – Einbau der ILE-Literatur (27.10.2026)

Unbeaufsichtigter Lauf. Status unverändert («geprueft»), keine Reservierung. Nur `kommentare/DBG/art-4.md` und `arbeit/DBG/art-4/` geändert.

## Recherche
- **Lexplorer-Suchen:** 16 (`search_chunks_hybrid`, Kanton CH, Kategorie `08-institut-fuer-law-und-economics`, limit 8–10); Budget 25. Lesen mit `get_chunk_content` und `get_document_slice` (nicht gezählt).
- Lehrbuch Hongler/Lorenz («ILE-HSG — Lehrbuch Steuerrecht») erschien als Treffer (Suchen 1, 2, 4, 8, 15) und wurde übergangen.
- Ablage aller verwendeten Treffer: `01_Recherche/Lexplorer_Fundstellen.md` (F1–F11, mit Abfrage, Chunk-ID, Autor:innen, Ziffer, tragendem Satz und `lexplorer_url`).
- Ohne einschlägigen Treffer und deshalb ohne Einbau: Grundsatz/Subsidiarität, Verhältnis zu Art. 5 DBG, Verfahren und Sicherstellung (Suche ohne Treffer), Nutzniesser (lit. a), Beginn der Zugehörigkeit (lit. c), Steuersatz, Entstehungsgeschichte.
- Entscheidung im unbeaufsichtigten Lauf: Die Chunks zu «§ 7 Grundstücke» (IFF-Schriftenreihe 2023) tragen die Autorenangabe «Moritz Seiler»; laut Kapitelkopf im Dokument sind Stefan Oesterhelt/Andrea Opel die Autor:innen von § 7. Zitiert wird nach dem Kapitelkopf (Oesterhelt/Opel).
- Ergänzend am Original (Open Case Law) gelesen, weil neue Sätze sich auf sie stützen: BGer 2C_888/2014 E. 4.3 f.; BGE 152 II 98 E. 9.3 und 9.5.

## Eingebaut
Elf ILE-Werke, 28 Fussnoten mit 30 ILE-Zitatstellen:

| Werk | Zitatstellen |
|---|---|
| Brülisauer, IFF-Schriftenreihe 2023, § 14 Betriebsstätten | 6 |
| Weissbrodt, FStR 2015, Ziff. 4.1.2 | 8 |
| Mauchle, IFF-Schriftenreihe 2021, Rz. 43 | 4 |
| Margraf/Schreiber, St.Galler Seminar 2019, Ziff. 1.3 | 3 |
| Oesterhelt/Opel, IFF-Schriftenreihe 2023, § 7 Grundstücke | 2 |
| Oesterhelt/Opel, FStR 2023, Rechtsprechung im Steuerrecht 2023/4, Ziff. 6.3 | 1 |
| Oesterhelt/Opel, FStR 2025, Rechtsprechung 2025-1, Ziff. 8.3 | 1 |
| Oesterhelt/Opel, FStR 2025, Rechtsprechung 2025/4, Ziff. 1.2 f. | 2 |
| Kocher/Stadelmann, FStR 2016, Ziff. 2.2.4.5 | 1 |
| Baumgartner/Duss/Fenners, FStR 2025, Gesetzgebungs-Agenda 2025/1, Ziff. 1.6 | 1 |
| Baumgartner/Duss/Fenners, FStR 2018, Gesetzgebungs-Agenda 2018/2, Ziff. 1.4 | 1 |

- Bestätigend (gl.M./vgl.) in bestehenden Fussnoten nach den Entscheiden: harmonisierung-vermittlung, gb-begriff, gb-anlagen, gb-vermoegen (2), gs-eigentum (2), gs-nutzungsrechte, lit-d-begriffe, lit-d-dba, bst-feste, bst-interkantonal, umfang, wechsel, art11, ausblick.
- Meinungsstand in indirekter Rede in bestehenden Randnoten: bst-freie-berufe (Mauchle zu freien Berufen und Geschäftsbetrieb), bst-katalog (Brülisauer zum Positivkatalog), bst-bau (Brülisauer zur Dauer), umfang (Kritik von Oesterhelt/Opel an der proportionalen Schuldzinsenverlegung, a.M.), wechsel (BGE 152 II 98 folgt der Mehrheit der Lehre), ehegatten (Lesart von Oesterhelt/Opel zu BGE 152 II 98 und KS 30 ESTV).
- **Neue Randnoten (5)**, je mit eigenem Meinungsstand der Lehre:
  - `gb-sitz-lehre` – feste Geschäftseinrichtung bei Personengesellschaften: Handelsregistereintrag genügt dem Bundesgericht (2C_888/2014 E. 4.3 f.); herrschende Lehre und Minderheitsmeinung nach Margraf/Schreiber; Mauchle.
  - `gs-ig-ile` – Beteiligung an Immobiliengesellschaften und einfachen Gesellschaften: Weissbrodt (keine Anknüpfung) gegenüber Oesterhelt/Opel (Analogie zu Art. 4 Abs. 1 lit. c DBG; Frage nicht abschliessend beantwortet).
  - `lit-d-lehre` – Begriffe Handel und Vermittlung nach Weissbrodt; a.M. zum Handel gegenüber der Cour de justice GE.
  - `bst-hilfstaetigkeiten` – Hilfstätigkeiten nach Landesrecht (Brülisauer; Gegenstimmen und Bundesgericht nach seinen Angaben).
  - `bst-ausland-lehre` – Kritik Brülisauers an den höheren Anforderungen an ausländische Betriebsstätten (BGE 139 II 78), a.M.
- Literaturverzeichnis neu angelegt (11 Einträge) vor dem Materialienverzeichnis. Kopf `stand: 2026-10-27`. Bestehende Labels unverändert; bestehender Text sonst nicht umgeschrieben (nur Anfügungen und Fussnotenergänzungen; in lit-d-begriffe eine zusätzliche Fussnote mitten in der Randnote).

## Fundstellenprüfung (getrennter Arbeitsschritt)
Kein Werkzeug für einen eigenen Hilfsagenten verfügbar; die Prüfung erfolgte als getrennter Durchgang: Alle ILE-Zitatstellen wurden per Skript aus der Datei gezogen (30 Stellen in 28 Fussnoten) und je am Chunk bzw. an der Dokumentstelle (`get_chunk_content`, `get_document_slice`) auf Autor:innen, Fundort, Ziffer und Tragfähigkeit geprüft.

| Ergebnis | Zahl | Hinweis |
|---|---|---|
| bestätigt | 30 | Ziffern der FStR-Beiträge nach Abschnittsnummer (Inhaltsverzeichnis bzw. Überschrift im Dokument), Schriftenreihe nach Randnoten. Bei Brülisauer § 14 sind N. 28, 34, 36, 43, 44, 46, 53, 54, 55, 61, 113, 114 im Text nummeriert; «N. 38–43» und «N. 60 ff.» umfassen unnummeriert extrahierte Absätze zwischen nummerierten Randnoten. |
| korrigiert | 3 | gb-sitz-lehre: «wohl vorausgesetzt» (einfache Gesellschaft) nach dem Wortlaut der Folie präzisiert; Fussnote zur Minderheitsmeinung umformuliert; bst-ausland-lehre: Kritik Brülisauers auf die Unterscheidung nach DBA- und Nicht-DBA-Fall präzisiert. |
| Autorschaft berichtigt | 1 | § 7 IFF-Schriftenreihe 2023: Oesterhelt/Opel statt der Chunk-Angabe «Moritz Seiler» (Kapitelkopf). |
| gestrichen | 0 | – |

## Schlussprüfung
- `python3 pipeline/kommentar.py kommentare/DBG/art-4.md`: 47 Randnoten, 112 Fussnoten, 0 Befunde (Format und Neutralität).
- `python3 pipeline/md2site.py --pruefen`: 15 bereit, 0 mit Befunden.
- Keine eigenen Wertungen: Auffassungen der Autor:innen in indirekter Rede («halten … für nur bedingt stichhaltig», «lehnt es ab», «hält … für nicht mehr zeitgemäss»); Wertungswörter der Vorlagen («überzeugt nur bedingt», «zu begrüssen», «m.E.») nicht übernommen.
