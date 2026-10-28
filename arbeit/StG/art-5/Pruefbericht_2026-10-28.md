# Prüfbericht Art. 5 StG (28.10.2026)

Unbeaufsichtigter Lauf (geplante Aufgabe, Claude-Cloud). Skill `steuerkommentar-selbstaendig` in der Fassung des Repositorys.

## Umfang
- Kommentierung `kommentare/StG/art-5.md`: 52 Randnoten, 152 Fussnoten; `pipeline/kommentar.py` ohne Befund; `md2site.py --pruefen` hält den Artikel nur wegen Status «in_arbeit» zurück (Status setzt `reservierung.py freigeben`).
- Entscheidregister Bundesgericht: 39 Einträge (18 A, 10 B, 11 C); Pipeline lieferte 34 Kandidaten, davon 8 Fehltreffer (kantonale Steuergesetze); 15 Entscheide nachgetragen (u.a. 2C_176/2008, 2A.361/2001, BGE 94 I 151, 97 I 438, 80 I 30, 87 I 295, 76 I 53, 55 I 321).
- BVGer/SRK: 23 BVGer-Urteile, 9 SRK-Entscheide (VPB), 4 kantonale Randhinweise (Entscheidsuche).
- Verwaltungspraxis: KS 5a, 24, 29c, 32a, MB S-02.141, MB S-027.289.1, Arbeitspapier Kryptowährungen, Mitteilung-020-DVS-2024.
- ILE-Literatur: 16 Beiträge im Literaturverzeichnis. Onlinekommentar.ch: keine Kommentierung zu StG, VStG oder einer verwandten Norm vorhanden (`onlinekommentar.py liste`).
- Lexplorer-Suchen: 20 von 25 (Praxis 5, ILE 15; Hauptsitzung und Prüfagenten 0).

## Entscheide des Laufs (ohne Rückfrage)
- Übersicht mit «Verhältnis zu anderen Erlassen» (VSt, direkte Steuern) statt «Harmonisierung».
- Entscheide zum StG 1917 und ErgStG 1937 aufgenommen, soweit die Begriffsbildung zu Zuschuss und Mantel darauf beruht (Botschaft: «im wesentlichen geltendes Recht»).
- Details zu Art. 6 Abs. 1 lit. k und Art. 12 StG (Sanierung) nur soweit für Abs. 2 lit. a nötig; Verweis auf die Kommentierungen zu Art. 6 und 12.
- Ausblick: Vernehmlassung 2026 (Sanierungsausnahme), weil sie die Tragweite von Abs. 2 lit. a betrifft.
- Hausstil von art-4 übernommen (Kurzdatum, «Text nach der OCR-Fassung», Lexplorer-Links für ESTV-Dokumente ohne estv.admin.ch-Link).
- Nicht verwendet, weil am Original nicht prüfbar: BGer 2A.107/1999 und 2A.17/1994 (nicht im Korpus; 2A.107/1999 nur als Bestätigungsvermerk aus VPB 64.114), AS 1974 11 und AS 1992 733 (Wortlaut der Urfassung bzw. der Neufassung von Abs. 2 lit. b 1992), AS-Fundstelle des ErgStG 1937 (Erstnennung ohne AS).
- Arbeitshinweis zum fortbestehenden Merkblatt S-02.141 aus dem Text gestrichen.

## Fundstellenprüfung (Schritt 8)
Vier Hilfsagenten (Fn. 1–37, 38–74, 75–112, 113–148), jede Fundstelle an der Quelle: `Fundstellenliste_2026-10-28_TeilA.md` bis `TeilD.md` (237 Fundstellen; 211 bestätigt, 25 korrigiert, 1 ohne Seitenbeleg im Tool). Behoben u.a.:
- Pinpoints: VPB 61.64 E. 2b; BGE 115 Ib 233 E. 3 a.E.; BGE 95 I 560 E. 1/2–4; 2A.618/1998 E. 3c/bb; A-1592/2006 E. 4.4.1/4.4.5; MB S-02.141 Ziff. II.1 a); KS 29c Ziff. 2.1, 2.2.1, 3.2; A-7760/2009 E. 3.2.2; BGE 87 I 295 E. 1b; VPB 62.81 E. 3c statt VPB 61.94 E. 2a; 2C_79/2010 E. 2.3.2; Ergänzungen 2C_1071/2018 E. 5.4.1 und E. 6, BGE 149 II 462 E. 3.2, 2C_976/2014 E. 3.4/4.2.
- Aussagen: Art. 5a bis 29.2.2012; Abgabesatz Art. 8; Art. 9 Abs. 1 lit. e = 1 % des Nennwerts; Bundesrat 1991 «unter anderem» wegen Ausfall; 2A.618/1998 («wann», obiter); Freibetrag lit. h (BGer 2C_1071/2018 E. 6); Oesterhelt/Tschan zu lit. abis (Gewinnsteuerwerte); Oesterhelt/Opel (keine Urteilskritik, zwei getrennte Punkte); SRK vs. BVGer bei der Dreieckstheorie präzisiert; A-5377/2023 «nicht Teil der Umstrukturierung»; A-5128/2024 bestätigt durch 9C_232/2026; VPB 64.114 (Pakete als wirtschaftliche Einheit; zeitlicher Abstand Liquidierung–Verkauf); Ausblick (Bericht nennt Art. 6, 11, 12, 53a StG).
- Botschaft OECD/G20, S. 23: im Tool ohne Seitenangabe; in der Fundstellenprüfung zu Art. 1 StG am 27./28.10.2026 als S. 23 bestätigt, beibehalten.

## Schlussprüfung (Schritt 9)
Hilfsagent: `Schlusspruefung_Befunde.md`, 71 Befunde. Umgesetzt: Nr. 1, 3–9, 11–14, 15 (Wiederholung durch Querverweis), 16, 17, 20–25, 26 (teilweise), 27–47, 48 (ohne Geschäftsnummer, da nicht geprüft), 49–51, 53–56, 57 (Satz gestrichen), 58–68, 69 (als Aussage Oesterhelt/Tschan), 70, 71 («Ziff.» einheitlich). Nicht umgesetzt: Nr. 2 (art-4 nicht Gegenstand dieses Laufs; Hinweis: art-4 nennt 28.2.2012), Nr. 10 nur teilweise (AS 1992 733 nicht einsehbar; Botschaftsaussage und Querverweis ergänzt), Nr. 18/19 (beide Stellen mit unterschiedlicher Funktion belassen), Nr. 52 (KS 32a stützt sich ausdrücklich auf A-1592/2006).
- Neutralitätsdurchgang (`kommentar.py` und grep): ohne Treffer.

## Offene Fragen, die der Text als offen ausweist
- Zuschüsse von Schwester- und Grossmuttergesellschaften: BGer unter StG 1973 nicht entschieden; Erhebung auf Stufe Zwischengesellschaft offen.
- Erkennbarkeit des Mehrwerts unter StG 1973 nicht ausdrücklich entschieden.
- Genussscheine, Stammanteile, Genossenschaftsanteile, Beteiligungsscheine: keine Rechtsprechung zum geltenden Recht.
- Grenze der Restaktivität beim Mantelhandel; Berufung der Steuerpflichtigen auf den Mantelhandel (2C_349/2008 E. 2.6).
