# Prüfbericht Art. 2 StHG – 28.10.2026

## Entscheide im unbeaufsichtigten Lauf
- Reservierung durch `reservierung.py` (claude-cloud, StHG/art-2). Kein `stand.py setze`, keine Word-Fassung; Git nur über `reservierung.py freigeben`.
- Entscheid-Cache: `entscheide.py StHG/art-2` → 56 Entscheide (445 Suchtreffer). Triage in der Hauptsitzung (Mustersuche nach Art. 2 StHG/LHID/LAID im Volltext, einschlägige Erwägungen gelesen); 10 Fehltreffer. Gegenprobe `find_leading_cases` (29): keine weiteren BGer/BGE. Nachträge über Verweise: 2P.323/2004, 2C_742/2010, 2C_162/2011, BGE 123 II 588, BGE 149 I 125. 2P.456/1994 nicht online (cite: exists=false), nicht selbständig zitiert.
- Kantonale Gerichte und Verwaltungspraxis: Hilfsagent (effort high), ausschliesslich Entscheidsuche bzw. Open Case Law/Lexplorer Tax; Ergebnis `01_Recherche/Kantone_Praxis.md` (17 kantonale Entscheide im Volltext).
- Lehre: ILE-Literatur (Lexplorer Tax, Kategorie 08; Lehrbuch Hongler/Lorenz übergangen) und Onlinekommentar.ch. Keine OK-Kommentierung zu Art. 2 StHG oder Art. 1 DBG; verwendet Vorb. zu Art. 13–14a und Art. 13 StHG (Grieder/Hongler).
- Lexplorer-Suchen: 12 von 25 (6 Hilfsagent Praxis, 6 Hauptsitzung ILE). Fundstellenprüfung ohne Suchen.
- Botschaft 1983: nur OCR-Text über Open Case Law; Amtsdruckschriften (BAR) nicht erreichbar. Die OCR-Seitenindizes entsprechen nicht den BBl-Seiten (Beispiel: Index 179 = BBl-Seite 161), daher Zitat ohne Seitenangabe («Erläuterungen zu Art. 2 E-StHG»). Ob der Entwurf «Die Kantone und Gemeinden erheben» lautete (Konkordanztabelle), wurde mangels gesicherter Zuordnung nicht in den Text aufgenommen.
- Querverweise auf die Kommentierung zu Art. 1 StHG ohne Randnotennummern (Absatzangabe), da das Format nur interne Labels kennt.

## Fundstellenprüfung (Schritt 8, zwei Hilfsagenten, alle Fundstellen)
- Fundstellenliste_Teil1.md (Fn. 1–39) und Fundstellenliste_Teil2.md (Fn. 40–79).
- Behoben:
  - Botschaft: Verknüpfung der Vernehmlassungseinwände korrigiert (Verfassungsgrundlage → Festhalten an Aufzählung; Erbschafts-/Schenkungssteuern → abgelehnt, weil umstritten, ob direkte Steuern).
  - Cour de justice GE ATA/1201/2017 entfernt (vom Bundesgericht mit 2C_869/2017 aufgehoben).
  - SSK: Ziffern korrigiert (1.1; 3.1.3–3.1.12), Wertung «stark» gestrichen; Minimalsteuer-Satz auf «weder Minimal- noch Mindeststeuer» präzisiert.
  - «Kantonale Gerichte bezeichnen … als zwingend» auf VGer GR beschränkt.
  - Erwägungen: 9C_299/2023 E. 1.2; 2C_847/2015 E. 2.2 f. (Beschwerdebefugnis «weitgehend», Art. 89 Abs. 1 BGG vorbehalten); VGer BE 100.2013.380/381U E. 2.1.5–2.1.7; VGer BE 100.2020.266U E. 5.4 i.V.m. 4.2 f.; BGE 140 II 255 E. 3–6; VGer LU A 10 51 E. 1a und 3c/aa; 9C_472/2024 E. 3.1; KG LU 7H 16 61 E. 2.2.
  - 2C_162/2011 auf den Einzelfall zurückgeführt (keine Verallgemeinerung).
  - Rechtsweg aStHG: «im StHG geregelte Materie» statt «Katalogsteuer».
  - Schenkungssteuer: Aussagen des Bundesgerichts auf die Erbschaftssteuer beschränkt.
  - Monistisches/dualistisches System: Beleg BGE 150 II 478 E. 5.1.2 und StRG ZH; Fracheboud/Oesterhelt nur «vgl.».
  - Minimalsteuern: Auffassung VGer LU/Oesterhelt-Opel namentlich zugeordnet; Hinweis auf BGer 2C_272/2009 E. 2.3 («keine eigene Tragweite»); Art. 28 StHG Fassung 1998–2008.
  - Kirchensteuer (StRK BE): Ergebnis-Aussage korrigiert.
  - Abs. 2: BGE 123 II 588 auf damaliges Zürcher Recht bezogen; ZStB nur Rz 4; Tessiner Fall nicht verallgemeinert; Gemeinde als Rekursgegnerin (Rubrum).
  - Ausblick: Bundesgesetz Systemwechsel AS 2026 213 (statt unbelegtem BBl 2025 23, bestätigt über Fedlex-Fussnote zu Art. 7 StHG), Bundesbeschluss mit AS 2026 212; Eigentumsgarantie ergänzt; pa.Iv. 26.419 mit Urheber und korrekter Begründung.
  - Geschäftsnummern: StRG ZH 1 GR.2022.18, VGer BE 100.2019.49U.
- Nicht übernommen: Hinweis zu Fn. 72 (BGE 123 II 588 trägt nur «keine Autonomie») – erster Satz jetzt mit SSK belegt.

## Schlussprüfung (Schritt 9)
- pipeline/kommentar.py: 32 Randnoten, 80 Fussnoten, 0 Befunde; zusätzliche grep-Suche nach wertenden Wendungen: einziger Treffer «bedürfte» in indirekter Rede (VGer GR), keine eigene Wertung.
- Kürzungsdurchgang: Randnote «Verhältnis zu Minimalsteuern» mit «Minimalsteuern» zusammengelegt (Doppelung BGer 2C_272/2009).
- Unbelegte Aussage zur Quellensteuer als «Erhebungsform» gestrichen; Generalisierung zur Belastungsbegrenzung auf die Vermögenssteuer beschränkt.
- md2site.py --pruefen: zurückgehalten nur wegen Status «in_arbeit» (setzt das Steuerskript bei Freigabe).
- Offen ausgewiesen: Rechtsnatur der Erbschaftssteuer; Grenze zwischen zulässiger Entlastung und Neutralisierung der Vermögenssteuer; Erhebung der Grundstückgewinnsteuer durch Kanton und Gemeinden nebeneinander unter Abs. 2; keine Rechtsprechung zu lit. c und zur Anrechnung nach Art. 30 Abs. 2 StHG.

## Hinweis für andere Artikel
- Die Kommentierung zu Art. 1 StHG zitiert das Bundesgesetz über den Systemwechsel bei der Wohneigentumsbesteuerung mit «BBl 2025 23»; nach Fedlex lautet die Fundstelle AS 2026 213 (nicht geändert, da ausserhalb dieses Laufs).
