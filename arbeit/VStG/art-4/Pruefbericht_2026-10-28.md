# Prüfbericht Art. 4 VStG (Gegenstand der Steuer: Kapitalerträge, Regel) – 28.10.2026

Unbeaufsichtigter Lauf (Claude-Cloud). Ergebnis: 59 Randnoten, 185 Fussnoten; `pipeline/kommentar.py` ohne Befund; `md2site.py --pruefen` ohne Befund (zurückgehalten nur wegen Status «in_arbeit», wird mit der Freigabe gesetzt).

## Entscheide im unbeaufsichtigten Lauf

- Register: Cache `pipeline/entscheide.py` 82 Entscheide (141 Kandidaten), davon 3 Fehltreffer (2C_320/328/342/2018: «LIA» = Tessiner Handwerksgesetz). Gegenprobe (Volltextabgleich aller BGer/BGE mit VSt-Bezug in Entscheidsuche) ergab 42 weitere BGer-Entscheide (9 BGE, 33 BGer), die die Phrasensuche nicht findet (vor allem franz./ital. Langformen). Register gesamt 116 Zeilen (A 24, B 46, C 46). Die nachgetragenen Entscheide sind nicht in den Cache übernommen (kein `--nachtragen` im Lauf); Liste in Register_Gegenprobe.md.
- BVGer und kantonale Gerichte ausschliesslich über Entscheidsuche (rund 35 BVGer-Entscheide, SRK VPB 68.75, StRG ZH ST.2016.115, KGer VS F1 24 147). BVGer A-2591/2019 (vom BGer in 9C_661/2022 aufgehoben) nicht verwendet.
- Lehre: 15 ILE-Fundstellen (FStR, IFF-Schriftenreihe, Seminarunterlagen; Hongler/Lorenz ausgeschieden). Onlinekommentar.ch: keine Kommentierung zum VStG oder zu einer verwandten Norm (`onlinekommentar.py liste`: 7 Kommentierungen zu DBG/StHG, keine einschlägig).
- Lexplorer: 18 von 25 Suchen (15 ILE, 3 Praxis), sonst Navigation; Prüfagenten nur Lesen.
- Übersicht ohne «Harmonisierung», stattdessen «Verhältnis zu anderen Erlassen» (DBG, KEP, DBA).
- Kein Kapitel «Ausblick»: keine beschlossene oder dem Parlament unterbreitete Änderung von Art. 4 (Fedlex; Materialien.md Ziff. 8). Reformgeschichte (Zahlstellenprinzip 2015, Fremdkapitalmarkt 2021/Abstimmung 2022) in der Übersicht. Die Vernehmlassung 2026 zur VStV (Meldeverfahren im Konzern) ist bei der Direktbegünstigung als Materialie erwähnt.
- Sachüberschrift nach Lexplorer Tax (konsolidierte SR-Fassung: «A. Gegenstand der Steuer I. Kapitalerträge 1. Regel»), da Fedlex keine Sachüberschrift liefert.
- Botschaft 1963 nur als OCR-Fassung (Seiten berechnet; Scan beim Bundesarchiv nicht abrufbar); Urfassung AS 1966 371 nicht abrufbar, Wegfall der E-lit. e aus Fassung 2006 erschlossen. AS-Fundstelle der Aktienrechtsrevision 1991 nicht verifiziert und deshalb nicht angegeben.
- Bandnummern der IFF-Schriftenreihe (2023, 2025) nicht verifiziert; zitiert mit Jahr und Bandtitel.

## Fundstellenprüfung (Fundstellenliste_Teil1–4.md)

Vier unabhängige Prüfagenten, alle Fussnoten der Prüffassung (178) und beide Verzeichnisse. 152 bestätigt, 26 korrigiert, 0 nicht belegbar; Verzeichnisse 40 bestätigt, 4 korrigiert. Umgesetzt u.a.:
- Pinpoints: 2C_812/2010 E. 5.1; 2C_349/2008 E. 2.3; 2C_557/2010 E. 3.2.1; 2C_726/2009 E. 3.1; 2C_578/2019 E. 4.1 (Vermutung); 2C_382/2017 E. 5.6.1; BGE 107 Ib 325 E. 2 und 3a; BGE 115 Ib 274 E. 9a und 9c; Kollruss Ziff. 2.2, 2.3, 3, 4.1; Oesterhelt FStR 2026/2 Ziff. 3.3, 4.2; Erläuternder Bericht 2026 Ziff. 3.1.
- BGE 151 II 827 hat keine E. 3.1 → BGer 9C_690/2023, E. 3.1 (nicht publ.).
- Inhalt: BGE 110 Ib 127 auf das damalige DBA USA beschränkt; 2C_344/2018 (DBA AT) allgemein formuliert; 2A.249/2003 (Übernahme einer Abgangsentschädigung der Schwestergesellschaft); 2A.716/2004 (erfolgsneutrale Ausbuchung); A-2637/2016 und A-3066/2017 E. 3.8 als ESTV-Praxis gekennzeichnet; KS 24 Ziff. 3.1.2 genauer; Kundenverhältnis als BGer-Regel (ASA 68 596) über A-629/2010; nur eine liechtensteinische Anstalt (BGE 104 Ib 280/107 Ib 98, summarische Prüfung).
- Lehre: Lissi/Gerber (richtige Reihenfolge) als Kritiker der Direktbegünstigungstheorie, nicht nur als Wiedergabe der Praxis; «zustimmend» bei Engstler/Regli gestrichen; Hinweis auf unpubliziertes BGer-Urteil vom 19.9.1985 zu Abs. 2 nach Brülisauer ergänzt.
- Satz «Das Bundesgericht hat sich mit dieser Kritik nicht auseinandergesetzt» geprüft (Open Case Law, nur 4 BGer-Treffer zur Direktbegünstigungstheorie, alle direkte Steuern) und belegt.

## Schlussprüfung (Prüfpunkte `pruefung`)

Hilfsagent Sprache/Zitierweise; 35 Befunde, umgesetzt bis auf: AS-Fundstellen VStB 1943 und Aktienrecht 1991 (nicht verifizierbar, daher weggelassen); Weidmann FStR 2019/1 ohne Ziffer (im Korpus keine Ziffer). Umgesetzt u.a.: eigene Randnote «Vermutungen» (Text nach Aufzählung), Querverweise, BankG-Erstnennung, Urheber der Aussagen (BVGer/BGer/ESTV) ausdrücklich, Rang der Arrest- und Sicherstellungsentscheide, N.-Zitierweise der Schriftenreihe.
- Neutralität: `kommentar.py` 0 Befunde; Wertungen der Lehre (Spori/Storck, Kollruss, Lissi/Gerber, Brülisauer, Oesterhelt, Engstler/Regli) als deren Auffassung.
- Offene Fragen im Text: Entstehung der Steuer bei Gratisaktien (MB 1999 vs. BVGer A-364/2013); Leistungsempfänger (Kritik an Direktbegünstigungstheorie); Zählregeln lit. a ohne gerichtliche Überprüfung; Cash Pool; Abs. 2: tatsächliche Leitung (Art. 22 Abs. 5 Satz 2 VStV) und Bemessung; Serienschuldbriefe/Schuldbuchguthaben ohne Rechtsprechung.
