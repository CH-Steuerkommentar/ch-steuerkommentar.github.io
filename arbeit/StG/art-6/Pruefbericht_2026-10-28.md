# Prüfbericht Art. 6 StG (28.10.2026)

Unbeaufsichtigter Lauf (geplante Aufgabe, Claude-Cloud). Skill `steuerkommentar-selbstaendig` in der Fassung des Repositorys.

## Umfang
- `kommentare/StG/art-6.md`: 58 Randnoten, 177 Fussnoten; `pipeline/kommentar.py` ohne Befund; `md2site.py --pruefen` hält den Artikel nur wegen Status «in_arbeit» zurück (Status setzt `reservierung.py freigeben`).
- Entscheidregister Bundesgericht: 21 Einträge (11 A, 2 B, 8 C); Pipeline-Cache lieferte 13 Kandidaten, davon 4 Fehltreffer (kantonale Steuergesetze, LIFD); nachgetragen u.a. 2C_447/2018, 2A.83/2001, 2A.84/2001, BGE 102 Ib 140, 115 Ib 125, 114 Ib 277, 148 II 121, 2C_1095/2015.
- BVGer/SRK/Bundesrat: 19 BVGer-Urteile, 6 VPB-Entscheide im Text. Kantonale Gerichte: keine einschlägigen (Emissionsabgabe ist reine Bundesabgabe).
- Verwaltungspraxis: KS 5a, 24, 29c, 32a, Mitteilung-020-DVS-2024 Checkliste.
- ILE-Literatur: 17 Einträge im Literaturverzeichnis. Onlinekommentar.ch: keine Kommentierung zu StG, VStG oder einer verwandten Norm (`onlinekommentar.py liste`), daher 0 OK-Fundstellen.
- Lexplorer-Suchen: 17 von 25 (Agent abis/j 4, Agent a/b/c/h/i 6, Agent d/g/k/l 7; Hauptsitzung, Registeragent und Prüfagenten 0 – nur Lesen).

## Entscheide des Laufs (ohne Rückfrage)
- Übersicht mit «Verhältnis zu anderen Erlassen» statt «Harmonisierung» (Auftrag).
- Gliederung nach Buchstaben in Gesetzesreihenfolge; Unterüberschriften nur bei lit. abis und lit. k; aufgehobene lit. e, f, m in einer Randnote.
- Hausstil von art-5 übernommen (Kurzdatum, «Text nach der OCR-Fassung», Lexplorer-Links für ESTV-Dokumente). Statt Volltextlektüre einer Grieder/Hongler-Musterkommentierung diente die bereits musterkonforme Kommentierung zu Art. 5 StG als Vorlage.
- Inhalt der 1993 aufgehobenen lit. e nicht dargestellt (Urfassung AS 1974 11 nicht einsehbar).
- Nicht verwendet, weil nicht am Original prüfbar oder ohne Seite: Botschaft OECD/G20 (Seite 23 im Tool nicht belegt; Abstimmung 2022 nur mit Baumgartner/Duss/Fenners belegt), Botschaft ABRG S. 1185 (Seitenumrechnung unsicher), BGer 2A.17/1994 (nur über Weidmann/Heuberger/Zitter wiedergegeben, als deren Aussage), Entwurf FBG (BBl 2025 1548) und Vernehmlassung BankG 2026 (Stand nicht geprüft).
- Materialienverzeichnis: Fedlex-Links nur aus Tool-Ergebnissen (fedlex.data.admin.ch-ELI); bestehende www-Links aus art-5 übernommen.

## Fundstellenprüfung (Schritt 8)
Vier Hilfsagenten (Fn. 1–45, 46–90, 91–130, 131–173 nach damaliger Zählung), jede Fundstelle am Original: `Fundstellenliste_2026-10-28_TeilA.md` bis `TeilD.md`. Behoben u.a.: Formulierung SRK VPB 61.64; Robert (Aussage betrifft Stempelabgaben und VSt insgesamt); Dividendengrenze 5 % im Entwurf 1972; Postulat Gemperli (Abschreibung); BGE 114 Ib 277 (Inhalt); BGE 149 II 462 (E. 2.2.3 f., 3.4.2, Sachverhalt E. 3.1 f.); 2C_976/2014 E. 3.1 f.; KS 5a Ziff. 4.2.1.5 (Rechtsformwechsel nicht betroffen statt befreit), Bsp. Nr. 4; A-7065/2013 (E. 4.3 f.; Aufhebung E. 4.5 f.); Oesterhelt/Tschan § 1 (N. 172 ff., Ziff. XII.5, Ziff. XI.3.2, CV statt Stiftung) und § 7 (Grossmutter-Fall, N. 5 f.); VPB 61.64 bei lit. ater; Botschaft USR II S. 4841 («echter Freibetrag» bezieht sich auf lit. b); Checkliste (KER und nicht verrechnet); A-3735/2017 (Bestätigung nur Zeitpunkt); A-944/2020 (Restbetrag unbestritten); KS 29c (betrifft Emissionsabgabe nicht unmittelbar); BGE 149 II 158 vor BGE 149 II 462; Oesterhelt/Tschan § 6 N. 87 ff.; Vermerke zu A-5073/2020 vereinheitlicht; Materialienverzeichnis um Daten und ELI ergänzt.
- Offen geblieben (im Text vorsichtig formuliert): KS 24 Ziff. 2.1.9 vs. Inhaltsverzeichnis 2.1.8.1 (wie in art-5 belassen); ASA 65, S. 827 (aus art-5 übernommen, nicht im Korpus); BBl-Seiten vor 1999 nach OCR berechnet.

## Schlussprüfung (Schritt 9)
Hilfsagent: `Schlusspruefung_Befunde.md`, 69 Befunde. Umgesetzt: Erlass-Erstnennungen (BdBSt, EBG, ABRG mit AS), Konjunktiv der indirekten Rede, Attribution an Gericht/Praxis (Nr. 16–23), Zusammenlegung von Überschriften unter drei Randnoten, Abstimmung 2022 in die Übersicht, Wiederholungen (Art. 16 StV, KS 5a Ziff. 2.4.1, VPB 61.64, Genussscheine), Wiederholung des Wortlauts (lit. a, ater, Abs. 2, lit. d), Begriffe (Handelsgesellschaften ohne juristische Persönlichkeit; Umstrukturierungen nach Art. 9 Abs. 1 lit. e), Sprache. Nicht umgesetzt: Nr. 6 (BBl-Seite zu Ziff. 391.24 nicht belegbar; Ziffer belassen), Nr. 7 (KS 6 nur beschreibend), Nr. 10, 12, 24/25 (Reihenfolge entspricht Meinungsstand-Darstellung), 27 (kein amtlicher Beleg verfügbar), 49, 50, 52, 53, 54.
- Neutralitätsdurchgang (`kommentar.py`): ohne Treffer.

## Hinweis ausserhalb dieses Artikels
- Prüfagent C: kommentare/StG/art-1.md führt BVGer A-5128/2024 noch als «(angefochten)»; das BGer hat mit 9C_232/2026 vom 10.9.2026 entschieden. Nicht Gegenstand dieses Laufs, nicht geändert.
