# Prüfbericht Art. 2 DBG – Einbau der ILE-Literatur (27.10.2026)

Unbeaufsichtigter Lauf. Auftrag: bestehende, geprüfte Kommentierung um die Literatur des ILE-HSG aus Lexplorer Tax ergänzen, ohne den übrigen Text umzuschreiben. Status unverändert («geprueft»), keine Reservierung.

## Recherche

- Lexplorer-Tax-Suchen: **18** (`search_chunks_hybrid`, Kanton CH, Kategorie `08-institut-fuer-law-und-economics`, limit 8–10); Budget 25 eingehalten. Lesen mit `get_chunk_content`/`get_document_slice` (keine Suchen). Lehrbuch Hongler/Lorenz übergangen.
- Ohne einschlägigen Treffer blieben: abgeleitete Rechtsanwendungskompetenz und ergänzendes kantonales Recht, kantonales Verfahrensrecht, Gläubigerstellung des Kantons und Rechtsöffnung, Verrechnung, Einheit des Veranlagungsorts/Art. 197 DBG, Kantonsanteil, Parteistellung und Eröffnung an die ESTV. Dort wurde nichts eingefügt.
- Ablage: `01_Recherche/Lexplorer_Fundstellen.md` (Abfragen, Chunk-IDs, Autor:innen, Ziffern, tragende Sätze, lexplorer_url).

## Eingefügt

11 Fundstellen (10 Werke im neuen Literaturverzeichnis), 17 Zitierungen in Fussnoten, davon 4 neue Randnoten:

| Ort | Fundstelle | Art |
|---|---|---|
| N. ruling-zustaendigkeit, Fn. | Oesterhelt, FStR 2018, Spontane Information über Steuervorbescheide, Ziff. 3.4.1 | gl.M. |
| N. ruling-zustaendigkeit, Fn. | Schreiber/Wolfensberger, St.Galler Seminar zur Unternehmensbesteuerung 2019, Ziff. 3.3 | gl.M. |
| **neue N. ruling-estv-auskunft** | Oesterhelt, FStR 2018, Ziff. 3.4.1 (2×); Oesterhelt/Dumas, Internationales Steuerseminar 2016, Folie 19 | Meinungsstand (Lehre) |
| N. ruling-bindung, Fn. | Oesterhelt/Opel, FStR 2023, Rechtsprechung im Steuerrecht 2023/3, Ziff. 10.3 | vgl. |
| N. nichtigkeit, Fn. | Oesterhelt/Opel, FStR 2024, Rechtsprechung 2024/3, Ziff. 3.3 | gl.M. (hauptfrageweise) |
| N. nichtigkeit, Fn. | Oesterhelt/Opel, FStR 2024, Rechtsprechung 2024/4, Ziff. 9.3 | a.M. (vorfrageweise, Sitzkanton) |
| **neue N. nichtigkeit-kritik** | Oesterhelt/Opel, FStR 2024, Rechtsprechung 2024/4, Ziff. 9.3 | a.M., indirekte Rede |
| **neue N. rueckabwicklung** | BGE 151 II 101, Regeste und E. 3.6.4–3.6.7; Oesterhelt/Opel, FStR 2024, Rechtsprechung 2024/4, Ziff. 9.3 | Rechtsprechung + a.M. |
| **neue N. kantonale-praxis-bundesrecht** | Oesterhelt/Opel, FStR 2025, Rechtsprechung 2025-2, Ziff. 1.3 | Kritik, indirekte Rede |
| N. interventionslimite, Fn. | Oesterhelt/Opel, FStR 2024, Rechtsprechung 2024/3, Ziff. 7.3 | vgl. |
| N. veranlagung-bezug, Fn. | Rajower, FStR 2007, Sicherstellung und Arrest … (1. Teil), Ziff. 1 | vgl. |
| N. aufsicht, Fn. | Oesterhelt, FStR 2018, Ziff. 3.4.1 | gl.M. |
| N. keine-veranlagungsbehoerde, Fn. | Oesterhelt, FStR 2018, Ziff. 3.4.1 | gl.M. |
| N. verwaltungsverordnungen, Fn. | Teuscher, IFF-Schriftenreihe Bd. 120, 2021, N. 43 | gl.M. |
| N. ausblick, Fn. | Baumgartner/Duss/Fenners, FStR 2018, Gesetzgebungs-Agenda 2018/3, Ziff. 1.1 | vgl. |

Weiter: `stand:` auf 2026-10-27; `# Literaturverzeichnis` vor dem Materialienverzeichnis neu angelegt (nur ILE-Literatur). Die bestehende Lehrstelle Vallender/Cavelti (zitiert nach BGE 142 II 182) bleibt unverändert im Text.

## Fundstellenprüfung

Ein Hilfsagent stand in dieser Umgebung nicht zur Verfügung (kein Agent-Werkzeug). Die Prüfung erfolgte deshalb als getrennter Arbeitsschritt nach dem Einbau: Jede neu eingefügte Literaturfundstelle wurde erneut am Chunk bzw. Dokument (`get_chunk_content`, `get_document_slice`) gegen Autor:innen, Fundort, Ziffer und Aussage geprüft; die Gegenposition des Bundesgerichts in den neuen Randnoten am Original (Open Case Law, BGE 151 II 101, E. 3.6 und 4.1, Regeste).

| Fundstelle | Autor:innen | Fundort/Ziffer | trägt Aussage | Ergebnis |
|---|---|---|---|---|
| Oesterhelt, FStR 2018, Ziff. 3.4.1 (5 Stellen) | bestätigt (Chunks 21, 22, 24, 25) | Ziff. 3.4.1 «Auskunft der zuständigen Behörde» bestätigt | ja (Zuständigkeit Kanton; Aufsichtsmittel und Rechtsmittel; keine Feststellungsverfügungen; Auskunft bindet nur ESTV; Genehmigungsvorbehalt mit Fn. 36 KS 8) | bestätigt |
| Schreiber/Wolfensberger 2019, Ziff. 3.3 | bestätigt | Folie «3.3 Rulings: Zuständigkeit der genehmigenden Behörde» | ja | bestätigt |
| Oesterhelt/Dumas 2016, Folie 19 | bestätigt | Folie 19 | ja | bestätigt |
| Oesterhelt/Opel, FStR 2023/3, Ziff. 10.3 | bestätigt | Ziff. 10.3 (Chunk 46 nach «10.3 Bemerkungen») | ja (vgl.) | bestätigt |
| Oesterhelt/Opel, FStR 2024/3, Ziff. 3.3 | bestätigt | Chunk 26 liegt in 3.3 (nach «3.3 Bemerkungen», vor Ziff. 4) | ja | bestätigt |
| Oesterhelt/Opel, FStR 2024/3, Ziff. 7.3 | bestätigt | Chunk 43 liegt in 7.3 | ja | bestätigt |
| Oesterhelt/Opel, FStR 2024/4, Ziff. 9.3 (4 Stellen) | bestätigt | Ziff. 9.3 | ja, nach Korrektur | **korrigiert**: Die Kritik betrifft die Verfügung des statutarischen Sitzkantons (Art. 105 Abs. 3 DBG); Text und Fussnote in N. nichtigkeit und nichtigkeit-kritik entsprechend eingegrenzt |
| Oesterhelt/Opel, FStR 2025-2, Ziff. 1.3 | bestätigt | Chunk 17 in 1.3 | ja | bestätigt |
| Teuscher 2021, N. 43 | bestätigt | N. 43 | ja | bestätigt |
| Rajower, FStR 2007/2, Ziff. 1 | bestätigt | «1 Ausgangslage» | ja (vgl.) | bestätigt |
| Baumgartner/Duss/Fenners, FStR 2018/3, Ziff. 1.1 | bestätigt | Ziff. 1.1 | ja | bestätigt |

Gestrichen: keine. Korrigiert: 1 (Eingrenzung auf den Sitzkanton). Verworfen vor dem Einbau: FStR 2012/3 (Finanzaufsicht; Umsetzung nicht belegbar), FStR 2014/1 (Quellensteuer-Sonderfall).

## Neutralität und Format

`python3 pipeline/kommentar.py kommentare/DBG/art-2.md`: 36 Randnoten, 75 Fussnoten, **0 Befunde**. Wertungen der Autor:innen («fragwürdig», «schwer zu begründen», «richtigerweise») nur in indirekter Rede als deren Auffassung; kein U.E.

## Hinweis für die Nachführung (nicht geändert)

N. kein-eigener-anspruch sagt, das Bundesgericht habe das BVGer-Urteil «auf Beschwerde der Steuerpflichtigen» aufgehoben und die Beschwerde «im Übrigen» abgewiesen. Nach Oesterhelt/Opel, FStR 2024, Rechtsprechung 2024/4, Ziff. 9.1, focht der Kanton Zug das BVGer-Urteil an; nach BGE 151 II 101, E. 4.1, war der Kanton Zug die unterliegende Partei und die steuerpflichtige Person obsiegte. Die Prozesslage sollte bei der nächsten Überarbeitung am Sachverhalt und Dispositiv des Originals geprüft werden. Sie wurde hier nicht geändert, weil der Auftrag auf den Einbau der ILE-Literatur beschränkt war.
