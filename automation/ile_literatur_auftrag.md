# Auftrag: ILE-Literaturkatalog – Arbeitspaket bereinigen und Artikeln zuordnen

Du bearbeitest **ein** Arbeitspaket `daten/ile-literatur/pakete/paket_NN.jsonl` im Repo
CH-Steuerkommentar/ch-steuerkommentar.github.io. Jede Zeile ist ein Kandidat, den ein Skript
mechanisch aus den Literaturverzeichnissen und Fussnoten der ILE-Publikationen (FStR,
Schriftenreihe Finanzwissenschaft und Finanzrecht, Working Papers, Lehrbuch, St.Galler Seminare)
gezogen hat: `zitat` (beste Fassung), `varianten`, `jahr`, `nennungen`, `aus_verzeichnis`, `fundorte`.
Die Kandidaten sind alphabetisch sortiert; Dubletten stehen meist nebeneinander.

Ziel: Für jede Bestimmung von DBG, StHG, VStG, MWSTG und StG die **zentralen Publikationen**
sammeln, damit jede Kommentierung am Schluss einen Abschnitt «Weiterführende Literatur» erhält.

## Arbeitsschritte

1. Lies das ganze Paket (Python, nicht Zeile für Zeile in den Kontext kippen; arbeite in Blöcken
   von etwa 150 Kandidaten).
2. **Verwerfen** (nicht in die Ausgabe):
   - keine Literatur: Urteile, Materialien, Kreisschreiben, Gesetze, OECD-Dokumente, Tabellen,
     Fliesstextreste, Webseiten ohne Autor;
   - **Standardwerke**: Kommentare zu einem ganzen Erlass (BSK, Kommentar zum Schweizerischen
     Steuerrecht, Commentaire romand, Handkommentare, Locher, Agner/Jung/Steinmann, kantonale
     Gesetzeskommentare, OECD-MA-Kommentare), Lehrbücher und Gesamtdarstellungen (Blumenstein/Locher,
     Höhn/Waldburger, Reich, Oberson, Ryser/Rolli, Rivier, Locher Einführungen, Mäusli/Höhn,
     de Vries Reilingh Manuel …), allgemeine Rechtsprechungsübersichten («Die steuerrechtliche
     Rechtsprechung des Bundesgerichts im Jahr …», «Rechtsprechung im Jahr …»);
   - Werke **vor 2000**, ausser sie sind grundlegend (Klassiker, die bis heute zitiert werden,
     z.B. Höhn, Besteuerung der privaten Gewinne 1955; Reich, Abgrenzung Geschäfts-/Privatvermögen
     SJZ 1984; Yersin, Apports et retraits 1977; Zuppinger, Wirtschaftliche Handänderung 1969;
     Böckli, Indirekte Steuern und Lenkungssteuern 1975). Im Zweifel: verwerfen;
   - ausserfiskalische Werke (Zivil-, Straf-, Verfahrensrecht ohne Steuerbezug);
   - Kurzzitate ohne erkennbaren Titel, die du keinem Vollzitat im Paket zuordnen kannst.
3. **Zusammenführen**: Dubletten (gleiches Werk, andere Schreibweise, Kurzzitat + Vollzitat,
   Aufsatz mit Seitenangabe/Randnote) zu einem Eintrag; `nennungen` addieren, `fundorte` vereinigen.
4. **Normalisieren** (Zitierweise des Projekts): `Nachname Vorname[/Nachname Vorname], Titel,
   Fundstelle`. Zeitschriften: `Titel, ASA 89 (2020/21), 123 ff.` bzw. `FStR 2015, 3 ff.`;
   Monografien: `Titel, Ort Jahr` (Diss. vermerken); Beiträge in Sammelwerken:
   `Titel, in: Hrsg. (Hrsg.), Werk, Ort Jahr, Seite ff.`. «Arch.» → ASA. Kapitälchen/Grossschrift
   in normale Schreibung. Keine Fussnoten-Pinpoints (N, Rz., Seite des Zitats).
   **Erfinde nichts**: fehlt eine Angabe, lass sie weg. Die Angaben stammen aus dem Kandidaten.
5. **ILE-Werke kennzeichnen**: `"ile": true` für Beiträge im FStR / IFF Forum für Steuerrecht,
   Bände der Schriftenreihe Finanzwissenschaft und Finanzrecht (früher IFF-Schriftenreihe),
   ILE Working Papers, St.Galler Seminarunterlagen, Lehrbuch ILE. Schriftenreihe-Bände als
   «Schriftenreihe Finanzwissenschaft und Finanzrecht Bd. N» zitieren.
6. **Artikel zuordnen** – nach dem Titel (und, wenn nötig, nach den Titeln der Fundorte):
   Liste `artikel` mit Einträgen wie `"DBG 18"`, `"StHG 12"`, `"VStG 4"`, `"MWSTG 21"`,
   `"StG 5"` (Buchstaben-Artikel `"DBG 18a"`). Mehrere Artikel sind erlaubt und erwünscht, wenn
   das Werk mehrere Bestimmungen zentral behandelt (z.B. Betriebsstätte → DBG 4, 5, 6, 51, 52;
   StHG 21). Ordne nur zu, wo das Werk für die Bestimmung **zentral** ist, nicht jede entfernte
   Berührung; höchstens etwa 8 Artikel. Kantonales Recht: dem harmonisierungsrechtlichen Artikel
   des StHG (z.B. kantonale Grundstückgewinnsteuer → StHG 12). Werke, die keiner Bestimmung
   zugeordnet werden können (Steuerpolitik, Finanzwissenschaft, internationales Recht ohne
   Bezug zu einer Bundesnorm), bekommen `"artikel": []` und bleiben drin.
   Prüfe die Artikelnummern gegen die geltende Fassung (Fedlex/Lexplorer), wenn unsicher.
7. Schreibe `daten/ile-literatur/ergebnis/paket_NN.json` als JSON-Liste von Objekten:
   `{"zitat", "jahr", "ile", "url", "artikel", "nennungen", "fundorte"}`, alphabetisch nach `zitat`
   (`url`: Lexplorer-Link, wenn das Werk ein ILE-Werk ist und ein Fundort/Link dazu bekannt ist, sonst "").
   Dazu eine Zeile Statistik in `daten/ile-literatur/ergebnis/paket_NN.log`
   (Kandidaten, verworfen nach Grund, zusammengeführt, Einträge, davon mit Artikel).
8. Commit (`ILE-Literatur: Paket NN bereinigt`) und Push auf main (bei Konflikt `git pull --rebase`).
   Nichts sonst im Repo ändern.

Keine Lexplorer-Suchen nötig; nur bei Zweifeln an einer Artikelnummer Fedlex/Lexplorer lesen.
Arbeite das Paket vollständig ab. Wenn das Kontingent knapp wird: bisherigen Stand als
`paket_NN.json` mit `"unvollstaendig_ab": "<zitat>"` im Log speichern und pushen.

## Sonderfall: ILE-Pakete (`pakete/ile_NN.jsonl`)

Diese Pakete enthalten **die ILE-Publikationen selbst** (FStR-Beiträge, Bände der Schriftenreihe,
Working Papers, Seminarunterlagen, Lehrbuch), je Zeile: `reihe`, `quelle`, `titel`, `heft`
(z.B. «FStR 2015/1»), `band`, `jahr`, `url` (Lexplorer), `autoren` (aus dem Text, kann leer oder
unsauber sein), `teile` (Kapitel-/Abschnittstitel als Inhaltshinweis).

- Nichts verwerfen ausser Leerstücken (Editorial, Impressum, Inhaltsverzeichnis eines Hefts,
  Register, reine Anhänge ohne eigenen Titel). Rechtsprechungsübersichten («Rechtsprechung im Jahr …»)
  bleiben drin, bekommen aber nur Artikel, wenn ein Entscheid zu einer Bestimmung im Titel steht.
  Die Jahresregel (ab 2000) gilt für ILE-Werke **nicht**.
- Zitat bilden: `Nachname Vorname[/…], Titel, FStR 2015, …` (ohne Seitenzahl, wenn unbekannt);
  Schriftenreihe: `Autor, Titel, Schriftenreihe Finanzwissenschaft und Finanzrecht Bd. N, Jahr`
  (Autor aus `autoren`; fehlt er, ohne Autor); Working Paper: `Autor, Titel, ILE Working Paper Nr., Jahr`;
  Seminar: `Autor, Titel, in: <Seminarname> <Jahr>, St.Gallen`.
- `"ile": true`, `url` übernehmen, `nennungen`: 1, `fundorte`: [].
- Artikel nach Titel **und** `teile` zuordnen; bei Bänden der Schriftenreihe alle Bestimmungen, die
  ein Kapitel zentral behandelt (ein Band kann viele Artikel haben). Seminarunterlagen und
  FStR-Beiträge mit allgemeinem Titel: über `teile` entscheiden.
- Ausgabe `daten/ile-literatur/ergebnis/ile_NN.json` und `ile_NN.log`, sonst wie oben.

## Reihenfolge und Zuteilung

Nimm das Paket mit der kleinsten Nummer, für das es noch kein `ergebnis/<name>.json` und keine
Sperrdatei `ergebnis/<name>.in_arbeit` gibt; zuerst alle `ile_NN`, dann `paket_NN`. Lege sofort die
Sperrdatei an (Inhalt: Startzeit), committe und pushe sie, bevor du arbeitest; entferne sie mit dem
Ergebnis-Commit. Ist eine Sperrdatei älter als 5 Stunden, gilt das Paket als frei.

## Ablauf einer geplanten Sitzung

1. `git pull`. Wenn `daten/ile-literatur/roh/bericht.json` fehlt oder nicht `"vollstaendig": true` enthält,
   oder wenn es kein offenes Paket gibt (alle haben ein `ergebnis/<name>.json`): sofort beenden, nichts ändern.
2. Bis zu **drei** Pakete nacheinander nach obiger Reihenfolge abarbeiten (je Paket Sperrdatei, Ergebnis,
   Commit, Push).
3. Danach `python automation/ile_literatur_zusammenfuehren.py` ausführen und `daten/ile-literatur/katalog.json`,
   `daten/ile-literatur/artikel/`, `daten/ile-literatur/nach_artikel.md` committen
   (`ILE-Literatur: Katalog aktualisiert`) und pushen. Die Website baut sich danach selbst neu.
4. Der vorläufige Katalog aus dem Pilot (Bd. 116) wird dabei ersetzt; das ist gewollt.
