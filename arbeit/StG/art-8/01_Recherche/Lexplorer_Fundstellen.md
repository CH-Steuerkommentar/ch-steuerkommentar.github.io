# Art. 8 StG – Bemessung der Emissionsabgabe auf Beteiligungsrechten: Verwaltungspraxis und ILE-Lehre

Arbeitsdatei, Stand 28.10.2026. Hilfsagent Praxis/ILE.

## 0. Methode und Grenzen

- **Verwaltungspraxis:** Open Case Law (`search_practice`, ESTV, Quelle estv_ks; `get_practice` für Volltexte). Lange Volltexte wurden automatisch in Dateien ausgelagert und dort gelesen: KS 32a (51 327 Zeichen) ganz; KS 37A ganz (direkt ausgegeben); Mitteilung-020 Checkliste ganz; KS 29c an allen Fundstellen zu «Ausgabekosten», «Emissionsabgabe», «Verkehrswert» (Grep) samt Kontext, nicht ganz; KS 5a (365 209 Zeichen) **alle Abschnitte «Emissionsabgabe»** im Haupttext (Ziff. 2.4.1, 3.2.6, 4.1.2.5–4.6.4) und im Anhang (Beispiele Nr. 2, 3, 5–8, 10, 11, 13–19, 21, 25) vollständig, übrige Abschnitte (DBG, VSt, Umsatzabgabe) nicht. Lexplorer, Kategorie 02-verwaltungspraxis, durch Navigation: Quellen «ESTV Stempelabgaben» (6 Dokumente, kein Emissionsabgabe-Merkblatt), «ESTV Mitteilungen» (29 Titel gesichtet; Mitteilung-020, -022, -029 ganz gelesen), «SSK Kreisschreiben» (KS 28: Rz. 1–69 ganz gelesen, Anhang/Beispiele nicht), «ESTV Medien und News» (Dossier «Geltende Steuern» 2026 und Broschüre «Das schweizerische Steuersystem» 2025, je Abschnitt Emissionsabgabe).
- **ILE-Literatur:** Lexplorer Tax, filter_kanton CH, filter_category 08-institut-fuer-law-und-economics. Alle unten als «heute gelesen» bezeichneten Chunks wurden mit `get_chunk_content` vollständig gelesen; Autor:innen jeweils am Chunk-Ende. Treffer aus «ILE-HSG — Lehrbuch Steuerrecht» (e_chunks 44703, 44705, 44791, 44799, 44685) übergangen.
- **Vorarbeiten wiederverwendet:** art-5/01_Recherche/Lexplorer_ILE.md und Lexplorer_Fundstellen.md, art-6 und art-7 Lexplorer_Fundstellen.md. Wo ein Zitat nur aus Vorarbeiten stammt, steht «Wortlaut Vorlauf (art-5)»; die zentralen Oesterhelt/Tschan-Chunks (§ 6, § 7, § 1) wurden heute erneut gelesen.
- **Keine Rechtsprechung recherchiert.** Urteile erscheinen nur, soweit ein Praxis- oder Lehrtext sie nennt (als Hinweis, am Original prüfen). Keine Websuche.
- **Bandnummern IFF-Schriftenreihe** («Schriftenreihe Finanzwissenschaft und Finanzrecht»): Pfad `iff-schriftenreihe/doc_0127_128_Verrechnungssteuer_und_Stempelabgaben` → **Bd. 128** (2025, Oesterhelt/Tschan, «Verrechnungssteuer und Stempelabgaben – Fallbeispiele zu aktuellen Entwicklungen»; Titel gemäss Vorlauf art-5, Chunks 48414/48415); Pfad `doc_0361_132_Impot_anticipe_et_droits_de_timbre` → **Bd. 132** (2026, französische Fassung, Oesterhelt/Tschan).

## 1. Suchprotokoll

### 1.1 Lexplorer (15 von höchstens 20 Suchen; find_leading_cases: 0)

| Nr. | Werkzeug | Kategorie | Abfrage | Treffer | verwendet |
|---|---|---|---|---|---|
| 1 | search_chunks_hybrid | 08-ILE | Bemessung Emissionsabgabe Art. 8 Abs. 1 lit. a StG Betrag der Gesellschaft als Gegenleistung zufliesst mindestens Nennwert Agio | 10 | 53568 (Bertschinger/Risi), 30334 (§ 7 N 25), 64016 (Risi-Bravin/Stocker), 48412 (Seminar 2025), 54972; Lehrbuch 44791/44703/44705 übergangen |
| 2 | search_chunks_hybrid | 08-ILE | Emissionsabgabe Abzug Emissionskosten Abgabe auf der Abgabe Überwälzung Überpari-Emission 100/99 Bemessungsgrundlage | 10 | nichts Neues (MWST-Emissionsrechte, Seminar 2023 Folie «Keine Steuerfolgen») |
| 3 | search_chunks_keyword | 08-ILE | Art. 8 Abs. 3 StG | 10 | keiner (Tokenisierung trifft Art. 13/14 StG, VStA) |
| 4 | search_chunks_hybrid | 08-ILE | Sacheinlage Emissionsabgabe Bewertung zum Verkehrswert im Zeitpunkt der Einbringung Bewertungsgutachten immaterielle Güter Patente Einlage | 10 | 29840, 65235 (Seminar 2018), 30341 (§ 7 IP), 53391 (Seminar 2023), 59470 (Seminar 2021), 30332 |
| 5 | search_chunks_hybrid | 08-ILE | Forderungsverzicht Emissionsabgabe Nennwert der Forderung oder werthaltiger Teil nicht werthaltige Forderung Bemessung Zuschuss | 10 | 30428 (§ 6), 48603/48604 (Seminar 2025 Bilanzsteuerrecht, nur Gewinnsteuer), 4476 (Brülisauer, nur Überschrift) |
| 6 | search_chunks_hybrid | 08-ILE | Mantelhandel Emissionsabgabe Bemessung Reinvermögen im Zeitpunkt des Handwechsels stille Reserven Verkehrswert Gesellschaftsmantel Kaufpreis | 10 | 15125 (Waldburger), 48864 (Seminar 2025 personenbezogen); keine Bemessungsaussage zum Mantelhandel |
| 7 | search_chunks_keyword | 08-ILE | Wahldividende Emissionsabgabe | 0 | – |
| 8 | search_chunks_hybrid | 08-ILE | Wahldividende Stockdividende Ausgabe neuer Aktien aus bedingtem Kapital Liberierung zum Nennwert Emissionsabgabe Freibetrag Art. 6 Abs. 1 lit. h StG | 10 | 57923/57924 (Seminar 2020 COTD), 46363/46365 (Bd. 132, § 10 IV) |
| 9 | search_chunks_hybrid | 08-ILE | Emissionsabgabe Genussscheine ohne Nennwert drei Franken je Titel Genossenschaftsanteile Einzahlung Bemessung Art. 9 Abs. 1 lit. d StG | 8 | nichts Neues; 64016 ganz gelesen |
| 10 | search_chunks_hybrid | 08-ILE | Umwandlung Personenunternehmung Kapitalgesellschaft Emissionsabgabe 1 Prozent des Nennwerts Art. 9 Abs. 1 lit. e StG Sperrfrist fünf Jahre Mehrwert nachträglich | 8 | 48395 (Seminar 2025, nur KER), 53405 (Seminar 2023), 29746 (§ 1 N 134 ff.); 1441 (Neuhaus FStR 2001/1, nur DBG, nicht verwendet) |
| 11 | search_chunks_hybrid | 08-ILE | Bewertung der eingebrachten Beteiligung Emissionsabgabe Verkehrswert Praktikermethode Minderheitsabzug Kontrollprämie Unternehmensbewertung Zuschuss | 8 | Brozzo/Stocker FStR 2021/2 (10584, 10618; nur Vermögens-/Einkommenssteuer, als Analogie) |
| 12 | search_chunks_hybrid | 08-ILE | Senkung des Satzes der Emissionsabgabe von 2 Prozent auf 1 Prozent Unternehmenssteuerreform 1997 Abgabesatz Beteiligungsrechte | 8 | 8138, 8028 (Baumann FStR 2004/1 und 2004/2); 65588 (Hug FStR 2026, ohne Emissionsabgabe) |
| 13 | search_chunks_hybrid | 08-ILE | Aktienkapital in Fremdwährung Emissionsabgabe Umrechnung Schweizer Franken Kurs im Zeitpunkt Nennwert Währungswechsel | 8 | 53606 (Seminar 2023 Bilanzsteuerrecht); 46439 (Bd. 132, nur KER) |
| 14 | search_chunks_hybrid | 08-ILE | Emissionsabgabe Zuschuss zinsloses Darlehen Gewinnverzicht unentgeltliche Nutzungsüberlassung Dienstleistung kein Zuschuss Bemessung Betrag des Zuschusses | 8 | 61917 (Int. Steuerseminar 2016); zum Nutzungsvorteil nichts |
| 15 | search_chunks_hybrid | 02-Verwaltungspraxis | Emissionsabgabe berechnet vom Betrag der der Gesellschaft zufliesst mindestens vom Nennwert Sacheinlage Verkehrswert Zuschuss Mantelhandel Reinvermögen | 10 | nur Bekanntes (Dossier 2026, Broschüre 2025, KS 32a, MB S-027.289.1, MB S-02.141, KS 29a/29b, KS 5a) |

Navigation/Lesen ohne Suchzählung: `nav_list_sources` (CH, 02-verwaltungspraxis); `nav_list_documents` (ESTV Stempelabgaben, ESTV Mitteilungen, SSK Kreisschreiben, ESTV Medien und News); `get_document_slice` (SSK KS 28, Slices 0–2; Mitteilungen 020, 022, 029); `nav_list_chunks` (FStR 2023/1 Bertschinger; Bd. 132 Part 11; FStR 2001/1 Neuhaus; FStR 2021/2 Brozzo/Stocker); `get_chunk_content` für alle unten genannten Chunks.

### 1.2 Open Case Law (nicht auf das Lexplorer-Budget angerechnet)

| Nr. | Abfrage (search_practice, ESTV) | Treffer |
|---|---|---|
| OCL 1 | Emissionsabgabe Verkehrswert Sacheinlage (estv_ks) | KS 5 (2004), KS 5a, KS 29, 29a, 29b, KS 12 |
| OCL 2 | Emissionsabgabe Mitarbeiteraktien OR Mitarbeiterbeteiligung Agio Zufluss (estv_ks) | nur W99-005 (eigene Beteiligungsrechte), nicht einschlägig |
| OCL 3 | Emissionsabgabe "1 Prozent des Nennwerts" OR Reinvermögen OR Mantelhandel (estv_ks) | KS 5, KS 5a, KS 25 (nur Kapitalsteuer) |
| OCL 4 | Bewertung Wertpapiere ohne Kurswert Praktikermethode (ESTV) | 0 |
| OCL 5 | Emissionsabgabe Ausgabekosten OR Emissionskosten OR Emissionsspesen (ESTV) | KS 29b, KS 37A |
| OCL 6 | Emissionsabgabe Genossenschaftsanteile OR Genussscheine Bemessung Nennwert (ESTV) | KS 32a, KS 5, KS 5a |
| OCL 7 | Wahldividende OR Stockdividende OR Titeldividende (ESTV) | nur MWST-Branchen-Info 14 (nicht einschlägig) |
| OCL 8 | Verrechnungsliberierung OR "Liberierung durch Verrechnung" Emissionsabgabe (ESTV) | 0 |

`get_practice`: estv_ks_dbst_ks_2022_1_005a_dvs_de (KS 5a), estv_ks_dbst_ks_2025_1_032a_dvs_de (KS 32a), estv_ks_dbst_ks_2022_1_029c_dvs_de (KS 29c), estv_ks_dbst_ks_2018_1_037a_d_de (KS 37A), estv_ks_estv_mitteilung_020_dvs_checkliste_de (Checkliste).

---

## 2. Fundstellen je Sachfrage

Legende Position: P = Praxisdarstellung; K = Kritik; A = abweichende Auffassung; O = offene Frage.

### (1) Abgabesatz (1 Prozent)

**1.1 ESTV, Dossier Steuerinformationen «Geltende Steuern», Juni 2026, Ziff. 2.2.3.1** [Lexplorer-Status: Materialien, 25.06.2026; Informationsschrift, keine Verwaltungsverordnung]
- Chunk 46727844-5c39-456f-a5df-011226eb63fd — https://mcp-tax.lexplorer.ch/s/doc/aa95c20d-5592-42af-8c01-a0b0d59a7f61?chunk=46727844-5c39-456f-a5df-011226eb63fd (heute gelesen)
- Wörtlich: «Die Emissionsabgabe beträgt 1 % vom Betrag, welcher der Gesellschaft oder Genossenschaft als Gegenleistung für die Beteiligungsrechte zufliesst, mindestens aber vom Nennwert. Bei der Gründung oder Kapitalerhöhung einer Gesellschaft gilt für entgeltlich ausgegebene Beteiligungsrechte generell ein Freibetrag von CHF 1 Million.» – «Der Bruttoertrag aus der Emissionsabgabe betrug 2025 CHF 188 Millionen.»
- Aussage: Satz 1 % auf dem Zufluss, mindestens Nennwert; lit. h als «Freibetrag».
- Position: P (Informationsschrift).

**1.2 ESTV, «Das schweizerische Steuersystem», Juni 2025, Ziff. 8.2.3.1** [Lexplorer-Status: Materialien, 26.06.2025]
- Chunk 180aff51-887b-4b4a-90a2-dc18885f0562 — https://mcp-tax.lexplorer.ch/s/doc/3c4ec163-b4cc-42d8-80ce-d8ce456b3351?chunk=180aff51-887b-4b4a-90a2-dc18885f0562 (heute gelesen)
- Wörtlich: «Die Emissionsabgabe beträgt 1 % vom Betrag, welcher der Gesell­schaft oder Genossenschaft als Gegenleistung für die Be­teiligungs­rechte zufliesst, mindestens aber vom Nennwert. Bei der Grün­dung oder Kapital­erhöhung einer Gesellschaft gilt für entgeltlich ausgege­bene Beteiligungsrechte generell eine Freigrenze von CHF 1 Million.» – «Der Bruttoertrag aus der Emissionsabgabe betrug 2024 ca. CHF 229 Millionen.»
- Aussage: wie 1.1, aber mit dem Begriff «Freigrenze».
- Position: P; **Befund:** Die ESTV-Informationsschriften sind terminologisch uneinheitlich (2025 «Freigrenze», 2026 «Freibetrag»).

**1.3 Baumer/Marty, Aktuelle Entwicklungen im Unternehmenssteuerbereich, St. Galler Seminar zur Unternehmensbesteuerung 2021, Folien 14–17** (Wortlaut Vorlauf art-5, ILE-G.3)
- Chunks b91542bb-54de-4191-a487-158fe7c63562 (https://app.lexplorer.ch/suche?e_chunks=59140&e_sys=ile), 2cafb1e6-a3cb-4a8e-89bd-0525c562f028 (https://app.lexplorer.ch/suche?e_chunks=59143&e_sys=ile); Suche 2 bestätigte Folie 59144 («Eine Abgabe zu Unzeiten»)
- Referent:innen: Fabian Baumer, Frank Marty
- Wörtlich: «Die Abgabe ist wirtschaftlich nicht vertretbar und steuersystematisch unerwünscht: Sie belastet Substanz statt Einkommen. – Sie verteuert die Eigenkapitalfinanzierung …»
- Aussage: rechtspolitische Kritik am Satz bzw. an der Abgabe als Substanzsteuer; Vorlage Abschaffung (Pa.Iv. 09.503) am 13.2.2022 abgelehnt (Baumgartner/Duss/Fenners, FStR 2022/3, Ziff. 1.1, e_chunks=11859, Vorlauf art-5).
- Position: K (rechtspolitisch).

**1.4 Baumann, Unternehmenssteuerreform II – Zur Vernehmlassungsvorlage (1. Teil), FStR 2004/1, Ziff. 3.2.2 (vor 3.2.3)**
- Chunk 76276b38-ad19-4e23-8bbe-32c672644bcb — https://app.lexplorer.ch/suche?e_chunks=8138&e_sys=ile (heute gelesen); Autor: Ruedi Baumann
- Wörtlich: «Die Vorlage sieht folgende Erleichterungen vor: – Befreiung von der Abgabe bei Übernahme eines Betriebs oder Teilbetriebs … – Einführung einer echten Freigrenze von CHF 250000 für Genossenschaften; – Erhöhung der Freigrenze für Kapitalgesellschaften auf CHF 1 Mio.» – «In einer rechtsgleichen Unternehmungsbesteuerung ist kein Platz für die Emissionsabgabe.»
- Ergänzend Baumann, FStR 2004/2 (2. Teil), Chunk 24876e95-2fda-45ee-a9ce-76bab18ffe37 — https://app.lexplorer.ch/suche?e_chunks=8028&e_sys=ile: «Die vorgesehenen Erleichterungen bei der Emissionsabgabe stärken die Bedeutung des Leistungsfähigkeitsprinzips; Ziel bleibt die Abschaffung dieser Abgabe.»
- Aussage: Entstehungsgeschichte lit. h (Vernehmlassungsvorlage USTR II sprach von «Freigrenze»); Abgabe mit Leistungsfähigkeitsprinzip unvereinbar.
- Position: K; historisch (Vorlage, nicht geltendes Recht).
- **Lücke:** Zur Senkung des Satzes (frühere Sätze; Fassung Unternehmenssteuerreform 1997, AS 1998 669) kein ILE-Beitrag gefunden (Suche 12).

### (2) lit. a: Gegenleistung, die der Gesellschaft «zufliesst»

**2.1 Grundsatz Zufluss, mindestens Nennwert; Emissionskosten**
- **Risi-Bravin/Stocker, Besteuerung von Private Equity, St. Galler Seminar zur Besteuerung personenbezogener Unternehmen 2019**, Chunk 04afe1c6-cf5f-4251-80fa-be61ab9c9e04 — https://app.lexplorer.ch/suche?e_chunks=64016&e_sys=ile (heute gelesen); Referent:innen: Véronique Risi-Bravin, Raoul Stocker
  - Wörtlich: «Bei der Begründung und Erhöhung von Beteiligungsrechten beträgt die Emissionsabgabe 1% und wird berechnet vom Betrag, der der Gesellschaft als Gegenleistung für die Beteiligungsrechte zufliesst, mindestens aber vom Nennwert (StG 8 I a). Im Fall einer Überpari-Emission können die Emissionsspesen und -abgaben abgezogen werden.»
  - Aussage: Emissionskosten und die Abgabe selbst sind bei Überpari-Emission vom Zufluss abziehbar.
  - Position: P (Folienformat, ohne Beleg).
- **Hinweis Rechtsprechung (nicht Lexplorer, nur Querverweis):** art-5/01_Recherche/Praxis_BVGer.md nennt BVGer A-1552/2006 E. 3 und A-6828/2017 E. 2.4 zum «Abzug von Emissionsspesen und Abgabe bei Überpari-Zufluss» sowie A-7094/2008 zur «Überpari-Praxis (x 100/103)» beim Mantelhandel. Am Original prüfen.
- **ESTV, KS 29c, Ziff. 2.1** (Parallele KER, nicht Emissionsabgabe): «Einlagen, Aufgelder und Zuschüsse (gegebenenfalls nach Abzug der Ausgabekosten), welche direkt von den Inhabern der Beteiligungsrechte geleistet wurden …» – KS 37A, Ziff. 3.1.2: «Mit dieser Gutschrift werden, vermindert um die Emissionskosten, Reserven aus Kapitaleinlagen begründet». Position P (KER-seitige Nettobetrachtung der Ausgabekosten; zur Emissionsabgabe selbst schweigen beide KS).
- **Lücke:** Eine ESTV-Verwaltungsverordnung zur «Abgabe auf der Abgabe» (Überwälzung, Hochrechnung) und zum Abzug der Emissionskosten wurde in beiden Korpora nicht gefunden (Suche 2; OCL 5).

**2.2 Agio, Verrechnungsliberierung (Debt-Equity-Swap)**
- **Oesterhelt/Tschan, § 6 Sanierung, IFF-Schriftenreihe Bd. 128 (2025), Abschn. VI.2.1** (Wortlaut Vorlauf art-5, ILE-A.6; Dokument https://app.lexplorer.ch/suche?e_id=1054&e_sys=ile): «Das Agio unterliegt gemäss Art. 5 Abs. 1 lit. a StG der Emissionsabgabe von 1 %.» (Sachverhalt: Verrechnungsliberierung mit Darlehens- und Cash-Pool-Forderungen von rund CHF 1,08 Mia. = Sachverhalt BGE 149 II 462). Position P.
- **Oesterhelt/Opel, Rechtsprechung im Steuerrecht 2023/4, FStR 2023 Heft 4, Ziff. 5** (Wortlaut Vorlauf art-5, ILE-F.1; Chunk f98c7d8f-3c37-49cb-ab8d-6dfaf4bf0b4b — https://app.lexplorer.ch/suche?e_chunks=13571&e_sys=ile); Autor:innen: Stefan Oesterhelt, Andrea Opel
  - Wörtlich (Wiedergabe der Erwägungen): «Damit obliegt es den Organen der Kapitalgesellschaft, «zwischen Emissionsabgabeersparnis einerseits und Bildung von Reserven aus Kapitaleinlagen andererseits» zu entscheiden.»
  - Aussage: Bei der Verrechnungsliberierung ist der gesamte Agio-Zufluss Bemessungsgrundlage; Wahl zwischen KER und Sanierungsfreibetrag.
  - Position: P mit zurückhaltender K (Hinweis: BGer 7.9.2023, 9C_610/2022 = BGE 149 II 462, am Original prüfen).

**2.3 Sacheinlage (lit. a i.V.m. Abs. 3)** – siehe Sachfrage (5).

**2.4 Mitarbeiteraktien (Verrechnungsliberierung mit Lohnverbindlichkeit)**
- **Bertschinger, Die handels- und steuerrechtliche Behandlung von Mitarbeiterbeteiligungen bei der Arbeitgeberin, FStR 2023 Heft 1, Ziff. 2.1.2.3** — Chunk ea0ae637-53a3-4ada-a98c-46a09e716634 — https://app.lexplorer.ch/suche?e_chunks=12511&e_sys=ile (heute gelesen); Autor: Michael Bertschinger
  - Wörtlich: «Die Kapitalerhöhung unterliegt gemäss Art. 5 Abs. 1 Bst. a StG der Emissionsabgabe von 1 % (Art. 8 Abs. 1 Bst. a StG). Die Höhe der Emissionsabgabe richtet sich dabei ebenfalls grundsätzlich nach der handelsrechtlichen Verbuchung. Aufgrund des formell-zivilrechtlichen Charakters der Emissionsabgabe kann diese bei der Abgabe von Mitarbeiteraktien nur dann und soweit erhoben werden, wenn bei der Arbeitgeberin eine auf einem Lohnaufwand basierende handelsrechtliche Verbindlichkeit gegenüber den Mitarbeitenden für vergangene Arbeitsleistungen dazu verwendet wird, um Agio zu liberieren, und somit ein Zufluss bei der Arbeitgeberin erfolgt. Während bei einer Verrechnungsliberierung der Forderung des Arbeitnehmers deshalb auf dem vollen Betrag der Arbeitsleistung die Emissionsabgabe erhoben wird, unterliegt bei fehlendem handelsrechtlichen Ansatz einer solchen Verbindlichkeit lediglich der Nennwert der neuen Anteile der Emissionsabgabe.»
  - Aussage: Bemessung hängt von der Verbuchung ab: verbuchte Lohnverbindlichkeit = Zufluss in voller Höhe, sonst nur Nennwert.
  - Position: P (Fn. 63/64 im Chunk nicht aufgelöst).
- **Bertschinger, a.a.O., Ziff. 2.2.3.3 (Konzerngesellschaft)** — Chunk 023c3c16-e513-4700-8650-5b930ff53633 — https://app.lexplorer.ch/suche?e_chunks=12533&e_sys=ile (heute gelesen)
  - Wörtlich: «Die Kapitalerhöhung unterliegt gemäss Art. 5 Abs. 1 Bst. a iVm Art. 8 Abs. 1 Bst. a StG auf Stufe der Konzerngesellschaft der Emissionsabgabe. … Die Abgabeforderung auf ein allfälliges Agio resultiert gemäss Praxis der ESTV demgegenüber erst, wenn die Mitarbeiteraktien an die Arbeitnehmenden abgegeben werden, und lediglich insoweit, als handelsrechtlich eine auf einem Lohnaufwand basierende Verbindlichkeit gegenüber den Mitarbeitenden aus vergangenen Arbeitsleistungen für die Liberierung verwendet wird.»
  - Position: P (als «Praxis der ESTV» bezeichnet; ESTV-Fundstelle im Chunk nicht aufgelöst, Fn. 88).
- **Bertschinger, a.a.O., Ziff. 5 (Schlussbemerkungen)** — Chunk be609d37-3c70-4f40-b70c-94c00af602ed — https://app.lexplorer.ch/suche?e_chunks=12541&e_sys=ile (heute gelesen)
  - Wörtlich: «Andererseits gibt das KS 37a vor, welche Verbuchungen akzeptiert werden, damit steuerlich das angestrebte Resultat erreicht werden kann, was sich … beim Ansatz einer Verbindlichkeit für erbrachte Arbeitsleistungen im Zusammenhang mit einer Kapitalerhöhung … äussert. Im Ergebnis führt dies dazu, dass die steuerliche Gewinnermittlung die handelsrechtliche dominiert …»
  - Position: K (umgekehrte Massgeblichkeit; mittelbar für die von der Verbuchung abhängige Bemessung).
- **Bertschinger/Risi, Mitarbeiterbeteiligungspläne aus Sicht der Arbeitgeberin bzw. im Konzern, St. Galler Seminar zur Unternehmensbesteuerung 2023, Folie «Emissionsabgabe»** — Chunk 635e3fd5-35a3-46bb-8623-bf3b5b425287 — https://app.lexplorer.ch/suche?e_chunks=53568&e_sys=ile (heute gelesen); Referent:innen: Michael Bertschinger, Andreas Risi
  - Wörtlich: «Emissionsabgabe entweder geschuldet auf 1'000 oder 200 abhängig von handelsrechtlicher Verbuchung – Emissionsabgabe lediglich auf Nennwert geschuldet, sofern Abgabe ohne Gegenleistung (100)» (gestützt auf «OESTERHELT/TSCHAN, IFF Seminar August 2021, 44»).
  - Position: P.
- **Oesterhelt/Opel, Rechtsprechung 2024/3, FStR 2024 Heft 3, Ziff. 2.3** (Wortlaut Vorlauf art-5, ILE-A.8; Chunk a1d3567b-8273-4b41-a70b-c6cb27782ac0 — https://app.lexplorer.ch/suche?e_chunks=18651&e_sys=ile): «Wenn bei der Gesellschaft eine (auf einem Lohnaufwand basierende) Verbindlichkeit verbucht wird, welche durch die Lieferung der Aktien erfüllt wird, liegt gemäss Praxis der ESTV ein der Emissionsabgabe unterworfener Zufluss vor.» Position P; O (Fn. 35: frühere abweichende Auffassung Oesterhelt/Deiss).
- **ESTV, KS 37A vom 4.5.2018, Ziff. 3.1.2 und Beispiel 2** (DBG; keine Aussage zur Emissionsabgabe): Liberierung «zu Lasten dieser Verbindlichkeiten»; Beispiel 2 bucht «Verkehrswert bei Abgabe» 1'000 auf AK 100 und KER 900. Position P (nur mittelbar).
- **ESTV, Mitteilung-022-DVS-2024 vom 9.12.2024** (eigene Aktien, BGer 9C_135/2023): «Die Verrechnungssteuer und die Stempelabgaben sind vom Urteil 9C_135/2023 des BGer vom 6. Juni 2024 nicht betroffen.» (siehe Teil 3). Für die Bemessung: Wiederbegebung eigener Aktien bleibt ausserhalb von Art. 8 Abs. 1 lit. a (vgl. Oesterhelt/Opel, FStR 2024/3, a.a.O.: «weder eine Liberierung von neugeschaffenen Beteiligungsrechten noch … ein Zuschuss»).
- **ESTV, Mitteilung-029-S-2026 vom 5.2.2026, Ziff. 2.6:** «Werden neue Aktien herausgegeben, welche die Anforderungen an die Ausnahmebestimmungen von Artikel 14 Absatz 1 Buchstabe a und f StG erfüllen (sog. Primärmarkt-Transaktionen), fällt keine UA an. Diese Sachverhalte sind jedoch auf eine mögliche Emissionsabgabe hin zu überprüfen.» Position P (nur Abgrenzung).

**2.5 Wahl-/Titeldividende (Cash or Title Dividend)**
- **Oesterhelt/Tschan, Entwicklungen Verrechnungssteuer und Stempelabgaben, St. Galler Seminar zur Unternehmensbesteuerung 2020** — Chunks 68aacef9-c2ee-4914-8231-51b7c603e82a (Sachverhalt, https://app.lexplorer.ch/suche?e_chunks=57923&e_sys=ile) und 684a1503-1479-497a-a2c3-831ca5b208d0 (Beurteilung, https://app.lexplorer.ch/suche?e_chunks=57924&e_sys=ile) (heute gelesen); Referent:innen: Stefan Oesterhelt, David Tschan
  - Wörtlich: «Nach früherer Praxis stellte sich die ESTV auf den Standpunkt, dass diejenigen Aktionäre, welche sich bei einer COTD anstelle der Bardividende für eine Titeldividende entscheiden, diese letztlich mit ihrem Anspruch auf eine Bardividende liberieren. Somit vertrat die ESTV die Position, dass die Emissionsabgabe nicht bloss auf dem Nennwert der neugeschaffenen Aktie sondern auch auf dem Agio geschuldet ist.» – «Gemäss BGer vom 12.11.2019 (2C_1071/2018) ist die Emissionsabgabe hingegen lediglich auf dem neugeschaffenen Nennwert von CHF 0.01 pro Aktie geschuldet. Das Bundesgericht begründet dies damit, dass das Wahlrecht vor der Dividendenfälligkeit ausgeübt wurde und der Aktionär somit nie einen Anspruch auf eine Bardividende hatte, mit dem er die Aktie liberieren konnte.»
  - Aussage: Kein Zufluss über dem Nennwert, wenn das Wahlrecht vor Fälligkeit ausgeübt wird; frühere ESTV-Praxis (Bemessung auf Wert der Bardividende) überholt.
  - Position: P (Wiedergabe Urteil; Hinweis BGer 2C_1071/2018, am Original prüfen).
- **Oesterhelt/Tschan, § 10 Thèmes divers, IV. Cash or title dividend, IFF-Schriftenreihe Bd. 132 (2026), N 56–58** — Chunk 4b14cebb-2aa6-4629-86f9-dabc8ac263c0 — https://app.lexplorer.ch/suche?e_chunks=46365&e_sys=ile (heute gelesen); Sachverhalt N 54 in 3b46a83f-3dfd-40b2-9c02-f75dc679c28a (e_chunks=46363)
  - Wörtlich: «Selon la pratique antérieure, l'AFC considérait … L'AFC défendait donc la position selon laquelle le droit de timbre d'émission n'est pas dû uniquement sur la valeur nominale de l'action nouvellement créée, mais sur sa valeur vénale totale.» – «Toutefois, selon l'arrêt du Tribunal fédéral du 12 novembre 2019, le droit de timbre d'émission n'est dû que sur la valeur nominale nouvellement créée de 0,01 CHF par action.»
  - Position: P (gleichlautend mit 2020).
- **Lücke:** Keine ESTV-Verwaltungsverordnung zur Titeldividende (OCL 7).

**2.6 Unentgeltliche Ausgabe, Gratisaktien, «mindestens Nennwert»**
- **Oesterhelt/Tschan, § 7 Emissionsabgabe, Bd. 128 (2025), Abschn. III «Compensatory Capital Increase», N 25** — Chunk 84ae112f-a06d-4594-a6ab-f66e2e068642 — https://app.lexplorer.ch/suche?e_chunks=30334&e_sys=ile (heute gelesen); Autor:innen: Stefan Oesterhelt, David Tschan
  - Wörtlich: «Die Emissionsabgabe ist nur auf dem Nominalwert und nicht auf dem Wert der an Y. BV ausgegebenen Aktien geschuldet. Die mit der «Compensatory Capital Increase» abgegoltene Forderung der Käufer basiert auf dem Rechtsgeschäft mit dem Verkäufer und nicht mit der Gesellschaft. Bei der X. AG fehlt es daher (abgesehen vom Nominalwert) am entsprechenden Zufluss.»
  - Aussage: Fehlt ein Zufluss aus dem Verhältnis zur Gesellschaft, greift nur die Mindestbemessung auf dem Nennwert.
  - Position: P/eigene Beurteilung.
- **Gratisaktien:** ESTV, MB S-027.289.1 (30.4.1999), Ziff. 1: «Gratisaktien und Gratispartizipationsscheine sind Gegenstand der Emissionsabgabe.» (Chunk dad88f6b-0157-4641-81f6-b580b44fb741, Vorlauf art-5); Checkliste Mitteilung-020, Abschn. «Gratisaktien»: «Nachweis über die Liberierung von Gratisnennwert zu Lasten von KER». Bemessungsaussage (Nennwert) in keinem Dokument ausdrücklich. **Lücke ILE** (Vorlauf art-5, Suche 12; art-6 Suche 3).

**2.7 Genussscheine ohne Nennwert, Genossenschaftsanteile**
- **ESTV, KS 32a, Ziff. 4.2.4 b):** unentgeltliche Sanierungsgenussscheine: «In diesem Fall beträgt die Emissionsabgabe, gestützt auf Artikel 9 Absatz 1 Buchstabe d StG, drei Franken je Titel.» – entgeltliche: «Liegt eine entgeltliche Ausgabe von Genussscheinen vor, muss der Gesamtbetrag der geleisteten Forderungsverzichte als Zufluss im Sinn von Artikel 8 Absatz 1 Buchstabe a StG bezeichnet werden; die Emissionsabgabe ist folglich auf diesem Betrag zu berechnen; vorbehalten bleibt der Freibetrag gemäss Artikel 6 Absatz 1 Buchstabe k StG.» Position P (die einzige ESTV-Stelle, die Art. 8 Abs. 1 lit. a ausdrücklich anwendet).
- **Oesterhelt/Tschan, Seminar 2025, Folien 46 f.** (Vorlauf art-5, ILE-B.1, e_chunks=48376): «Seit der OR-Revision von 1992 weisen Genussscheine keinen Nennwert mehr auf.» Position P (VSt); **O:** Mindestbemessung «Nennwert» läuft bei nennwertlosen Genussscheinen leer, ILE-Literatur behandelt dies nicht.
- **Genossenschaftsanteile:** kein Praxis- oder ILE-Fund zur Bemessung (Suche 9; OCL 6).

**2.8 Kapitalband (Nettobetrachtung, Hinweis)**
- **Oesterhelt/Tschan, § 4 KER, Bd. 128 (2025), Abschn. 4 «Nettobetrachtung bei Emissionsabgabe», N 68–72** — Chunk ee9997e0-fa60-404e-8b62-aabf8f572df9 — https://app.lexplorer.ch/suche?e_chunks=30315&e_sys=ile (heute gelesen); Autor:innen: Stefan Oesterhelt, David Tschan
  - Wörtlich: «68 Zuflüsse im Rahmen eines Kapitalbands unterliegen gemäss Art. 5 Abs. 1 lit. a StG der Emissionsabgabe. Art. 9 Abs. 3 StG in der seit 1. Januar 2023 geltenden Fassung hält fest, dass auf den Beträgen, die einer Gesellschaft im Rahmen eines Kapitalbands nach Art. 653s ff. OR zufliessen, die Emissionsabgabe nur soweit erhoben wird, als diese Zuflüsse die Rückzahlungen im Rahmen dieses Kapitalbands übersteigen.» – «69 … ist das Nettoprinzip mit Bezug auf Art. 9 Abs. 3 StG - im Gegensatz zu Art. 5 Abs. 1septies VStG - auch für Rückkäufe ausserhalb der zweiten Handelslinie sowie für Rückzahlungen von KER anwendbar.» – «70 Auf den diesbezüglichen zusätzlichen KER nach Ziff. 3.1 KS 29c ist keine Emissionsabgabe geschuldet … hier bleibt es bei der strengen Nettobetrachtung.» – «72 Das KS 29c der ESTV enthält in Bezug auf die Emissionsabgabefolgen des Kapitalbands keine Ausführungen, da sämtliche Ausführungen zur Emissionsabgabe aus dem Kreisschreiben betr. Kapitaleinlagereserven entfernt wurden.»
  - Aussage: Bemessung beim Kapitalband = Nettozufluss (Art. 9 Abs. 3 StG als Sonderregel zu Art. 8 Abs. 1 lit. a).
  - Position: P mit eigener Auslegung (Abweichung EA – VStG).
- **Oesterhelt/Tschan, a.a.O., Abschn. 5** — Chunk d2c70ea0-6945-4a9b-aedc-3ddf7ef4a91a — https://app.lexplorer.ch/suche?e_chunks=30317&e_sys=ile (heute gelesen): «Die Emissionsabgabe ist nach dem strengen Nettoprinzip auf CHF 100 Mio. zu entrichten.» (Einlagen 600, Rückzahlungen 500).
- **Oesterhelt/Tschan, Seminar 2022, Folie 10** — Chunk b8ff96f0-7052-4626-ad97-b91daef2efdc — https://app.lexplorer.ch/suche?e_chunks=54972&e_sys=ile (heute gelesen): «Eigenkapital zu Beginn des Kapitalbandes: 300'000 / Eigenkapital am Ende des Kapitalbandes: 305'000 / Nettozunahme: 5'000 (bei der Emissionsabgabe erfolgt die Beurteilung **unabhängig** der Börsenkotierung)». Position P.
- **ESTV, Checkliste Mitteilung-020, Abschn. «Kapitalband»:** «Hinweis der Deklaration der Emissionsabgabe auf dem Nettozufluss mit Formular 3». Position P.

**2.9 Fremdwährungskapital (Hinweis)**
- **Schreiber/Wolfensberger, Aktuelle Fälle Bilanzsteuerrecht und Beteiligungsabzug, St. Galler Seminar zur Unternehmensbesteuerung 2023, Folie «5. Steuerliche Folgen bei Nennkapital in Fremdwährung»** — Chunk 7989200e-2c8f-4a98-8507-d7f77797b738 — https://app.lexplorer.ch/suche?e_chunks=53606&e_sys=ile (heute gelesen); Referent:innen: Susanne Schreiber, Thomas Wolfensberger
  - Wörtlich: «Erhebung Gewinn- und Kapitalsteuer (wie auch Emissionsabgabe, Verrechnungssteuer, Umsatzabgabe etc.) in CHF» – «Mitteilung ESTV, 11.5.2023: Kurse des Bundesamt für Zoll und Grenzssicherheit (BAZG) anzuwenden»
  - Aussage: Bemessungsgrundlage ist in CHF umzurechnen; massgebender Kurs für die Emissionsabgabe nicht näher bestimmt.
  - Position: P; **O** (Stichtag/Kurs bei Fremdwährungszufluss für die Emissionsabgabe).

### (3) lit. b: Betrag des Zuschusses

**3.1 Grundsatz; Forderungsverzicht (Nennwert oder werthaltiger Teil)**
- **ESTV, KS 32a vom 20.1.2025, Ziff. 4.1.3 a)** (OCL estv_ks_dbst_ks_2025_1_032a_dvs_de; Chunk 0c90ec1f-6b1f-46c5-87bf-d3fba7ec13de): «Demgemäss unterliegen alle Zuschüsse der Emissionsabgabe – vorbehältlich des Freibetrags gemäss Artikel 6 Absatz 1 Buchstabe k StG.» Position P.
- **ESTV, KS 32a, Ziff. 4.2.4 b)**: «… muss der Gesamtbetrag der geleisteten Forderungsverzichte als Zufluss im Sinn von Artikel 8 Absatz 1 Buchstabe a StG bezeichnet werden; die Emissionsabgabe ist folglich auf diesem Betrag zu berechnen …» Aussage: Die ESTV bemisst (jedenfalls bei Genussscheinen) auf dem **Gesamtbetrag** der verzichteten Forderungen; eine Reduktion auf den werthaltigen Teil sieht das KS nicht vor (Grep «werthaltig», «Nennwert», «Verkehrswert» in KS 32a: keine Treffer). Position P.
- **ESTV, Checkliste Mitteilung-020, Abschn. «Forderungsverzicht oder Zuschuss»:** «Bewertungsgutachten, falls Transaktion zum Verkehrswert erfolgt» – «Wurden diese Leistungen als KER geltend gemacht und nicht mit Verlusten verrechnet, ist die Emissionsabgabe von 1% auf dem Betrag des Zuschusses geschuldet. Die Art. 6 Abs. 1 Bst. h StG (Freibetrag 1 Mio. CHF) und Art. 6 Abs. 1 Bst. k StG (10 Mio. CHF) sind in diesen Fällen nicht anwendbar.» Position P.
- **Oesterhelt/Tschan, § 6 Sanierung, Bd. 128 (2025), Abschn. III.2.1** — Chunk 4e9783e8-39ae-47cd-b448-5d3d051f2dd1 — https://app.lexplorer.ch/suche?e_chunks=30428&e_sys=ile (heute gelesen): «Ein Forderungsverzicht des (direkten) Aktionärs unterliegt stets der Emissionsabgabe. Dies gilt selbst dann, wenn der Forderungsverzicht gemäss Praxis ESTV und Bundesgericht einen der Gewinnsteuer unterliegenden «echten Sanierungsertrag» darstellt.» Position P (implizit K: Asymmetrie zur Gewinnsteuer).
- **Oesterhelt/Tschan, Seminar 2025, Folien 91–93** — Chunks d65414e1-8108-4a92-afbf-fdfc64a96428 (e_chunks=48410), e0ecef40-7d27-432b-80db-9b02b939c433 (48411), 97abdc2b-bc18-43c0-8c46-d7a8bcd70a3f (48412) (heute gelesen): «Gemäss Art. 5 Abs. 2 Bst. a StG unterliegt der Forderungsverzicht grundsätzlich der Emissionsabgabe; der Sanierungsfreibetrag von CHF 10 Mio. nach Art. 6 Abs. 1 Bst. k StG kann vorliegend – die Verrechnung der Verluste vorausgesetzt – berücksichtigt werden.» – «Die Emissionsabgabe ist praxisgemäß auf dem höheren Betrag (d.h. Unterkapitalisierung oder Übersanierung) geschuldet; im vorliegenden Fall beträgt die Emissionsabgabe daher CHF 20'000 (1% von CHF 2 Mio.)». Aussage: Beim Teilerlass (Art. 12 StG) bemisst die ESTV die verbleibende Abgabe auf dem höheren Betrag aus Unterkapitalisierung oder Übersanierung. Position P.
- **Schreiber/Wolfensberger, Seminar 2025 «Bilanzsteuerrecht, Beteiligungsabzug, Pillar 2», Folie 1.1 (Abwandlung Mutter-Tochter)** — Chunk 208d3d77-13f2-4da6-86e2-4d7fd833efda — https://app.lexplorer.ch/suche?e_chunks=48604&e_sys=ile (heute gelesen); Referent:innen: Susanne Schreiber, Thomas Wolfensberger
  - Wörtlich: «Praxis: Forderungsverzicht / -einlage auf wertberichtigte Forderung gegen Tochtergesellschaft (TG) → Erhöhung der Gestehungskosten in Höhe des Nominalwerts der Forderung?» – «Wert der Einlage (Drittpreis) vs. Nennwert; ausländische TG: Beurteilung nach CH-Grundsätzen? z.B. Dt.: Einlage nur, soweit werthaltig (hier z.B. CHF 1) …»
  - Aussage: Für die Gewinnsteuer wird die Frage Nennwert vs. werthaltiger Teil offen gestellt; zur Emissionsabgabe keine Aussage.
  - Position: O (nur Analogie; nicht Emissionsabgabe).
- **Schreiber/Wolfensberger, Seminar 2021 «Aktuelle Fragen des Bilanzsteuerrechts», Folie II** — Chunk 87b77ff0-a6c0-4aba-a3eb-b5328310d086 — https://app.lexplorer.ch/suche?e_chunks=59470&e_sys=ile (heute gelesen): «Einlage von nonvaleur? → Bei Forderungseinlage gegen Tochtergesellschaft grds keine Bewertung, sondern Kongruenz von wegfallender Verbindlichkeit und Anschaffungskosten; anders für Gläubiger: leistungsgestörte Forderung …, Dritter würde Forderung nicht zum vollen Nennwert erwerben …» (mit Hinweis Oesterhelt/Schreiber, StR 2020, 438). Position O (Gewinnsteuer, Analogie).
- **Befund:** Eine ausdrückliche Aussage von ESTV oder ILE, ob beim Forderungsverzicht der Nennwert oder nur der werthaltige Teil «Betrag des Zuschusses» ist, wurde **nicht** gefunden. Die ESTV-Texte stellen auf den Gesamtbetrag der Verzichte ab (KS 32a Ziff. 4.2.4 b); die Lehre diskutiert die Frage nur gewinnsteuerlich.

**3.2 Sachzuschuss, Verkauf unter Verkehrswert, verdeckte Kapitaleinlage**
- **Oesterhelt/Tschan, § 7, Bd. 128 (2025), Abschn. V (Beteiligungsverkauf unter Wert)** — Chunk 74f70853-6eec-4fec-9708-72b79fbd5db3 — https://app.lexplorer.ch/suche?e_chunks=30338&e_sys=ile (heute gelesen): «Der Verkauf von B. AG an C. AG für CHF 300 Mio. stellt einen Zuschuss von A. AG an C. AG im Umfang von CHF 200 Mio. durch den direkten Anteilsinhaber dar: Dieser unterliegt grundsätzlich der Emissionsabgabe.» – «Für die Emissionsabgabe als Rechtsverkehrssteuer kann die Fortführung der Gewinnsteuerwerte der von der Muttergesellschaft übernommenen Vermögenswerte keine Rolle spielen.» Aussage: Betrag des Zuschusses = Differenz Verkehrswert – Kaufpreis. Position P/eigene Auffassung (durch KS 5a Ziff. 2.4.1 bestätigt).
- **Oesterhelt/Tschan, § 7, Abschn. V Variante IP (N 50 ff.)** — Chunk 4ea43c1c-9da9-463c-a4cd-d279c20682a9 — https://app.lexplorer.ch/suche?e_chunks=30341&e_sys=ile (heute gelesen): «Der Verkauf des IP mit einem Wert CHF 500 Mio. für CHF 300 Mio. ist ein Zuschuss von A. AG in B. AG im Umfang von CHF 200 Mio., welcher grundsätzlich der Emissionsabgabe unterliegt.» Position P.
- **Oesterhelt/Tschan, § 1 Umstrukturierungen XII–XIX, Bd. 128 (2025), Abschn. XII.2.2 (Quasifusion durch Verkauf zum Nominalwert)** — Chunk 1d95cc21-d58e-4d2d-b6ac-fc69a6d5e0a3 — https://app.lexplorer.ch/suche?e_chunks=29845&e_sys=ile (heute gelesen): «Der direkte Anteilsinhaber A macht einen Zuschuss von CHF 359'950'000 in die Reserven der X. AG. Dieser unterliegt gemäss Art. 5 Abs. 2 lit. a StG der Emissionsabgabe.» Vorlauf art-5 (ILE-C.8, Abschn. 2.1): «Im Umfang der Differenz zwischen Verkehrswert und Barkomponente liegt kein Entgelt, sondern eine verdeckte Kapitaleinlage vor.» Position P; K an BGer 2C_976/2014 (Fn. 55, Oesterhelt, StR 2015, 650 ff.; Hinweis).
- **Oesterhelt/Tschan, § 1 VI–XI, N 134–137 (Spaltung)** — Chunk 3b93e218-4df1-420a-a2ee-9a043212e71c — https://app.lexplorer.ch/suche?e_chunks=29746&e_sys=ile (heute gelesen): «134 Die Kapitalerhöhung von CHF 1 Mio. bei NewCo sowie der verdeckte Zuschuss von SwissCo in NewCo im Umfang von CHF 9 Mio. unterliegt grundsätzlich der Emissionsabgabe.» – «136 Dies hat aber zur Folge, dass der Freibetrag von Art. 6 Abs. 1 lit. h StG für künftige Kapitalerhöhungen nicht mehr geltend gemacht werden kann.» – «137 Die Bildung von Aktienkapital in Höhe von CHF 2 Mio. (= 20 % des Verkehrswertes) stellt keine übermässige Bildung von nominellem Kapital dar …». Position P.
- **Oesterhelt/Opel, Rechtsprechung im Steuerrecht 2023/2, FStR 2023 Heft 2, Ziff. 1.3** (Wortlaut Vorlauf art-5, ILE-C.5; e_chunks=13033–13035): «Verdeckte Kapitaleinlagen des unmittelbaren Anteilsinhabers unterliegen gemäss Art. 5 Abs. 2 lit. a StG der Emissionsabgabe.» Position P; O (Folgen unterlassener Abrechnung für Art. 20 Abs. 3 DBG).
- **Rohner, Quasifusionen, FStR 2017 Heft 3, Abschn. 2.2.2** (Vorlauf art-5, ILE-C.9; e_chunks=4910): Differenz «zwischen dem Kaufpreis von CHF 50000 und dem Verkehrswert der 50 %igen Beteiligung» als Zuschuss; Fn. 23: «es fehlt an der zu «stempelnden» Einlage in das Eigenkapital». Position K (an BGer 2C_976/2014).
- **ESTV, KS 5a, Anhang Beispiele 10, 11, 13–16, 21, 25** (siehe Teil 3): bei Spaltung/Übertragung zwischen Schwestern «Da die Vermögenswerte vorliegend nicht durch den (direkten) Inhaber der Beteiligungsrechte eingebracht werden, ist die Emissionsabgabe nicht betroffen.»

**3.3 Leistungen zwischen Schwestergesellschaften, Grossmutterzuschuss**
- **ESTV, KS 32a, Ziff. 4.1.3 b):** «… unterliegen ausschliesslich Zuschüsse von direkten Inhabern von Beteiligungsrechten der Emissionsabgabe. Auf Forderungsverzichten von Schwestergesellschaften ist somit keine Emissionsabgabe geschuldet.» Ziff. 4.1.3 c): «Zuwendungen durch unabhängige Dritte sind nicht Gegenstand der Emissionsabgabe - vorbehältlich einer allfälligen Abgabeumgehung.» Position P (Hinweis BVGer A-1592/2006 E. 4).
- **Oesterhelt/Tschan, § 7, Abschn. IV «Grossmutterzuschuss», N 33–37** (Wortlaut Vorlauf art-5, ILE-C.1; e_chunks=30335/30336): «Es erfolgt keine Erhebung der Emissionsabgabe auf dem Zuschuss von A. AG in die Reserven von D. AG, da der Zuschuss nicht von der Anteilsinhaberin erfolgt.» – «Nicht bloss der Begriff des «Gesellschafters» ist zivilrechtlich auszulegen, sondern auch der Begriff des «Zuschusses».» Position P; O (Erhebung auf Stufe Zwischengesellschaft).
- **Heuberger/Zitter, Steuerfolgen von internationalen Umstrukturierungen, Internationales Steuerseminar 2016** — Chunk c44c513c-7d90-422f-95be-883baac027a2 — https://app.lexplorer.ch/suche?e_chunks=61917&e_sys=ile (heute gelesen); Referent:innen: Reto Heuberger, Gernot Zitter
  - Wörtlich: «Fazit: Keine EA, da Zuschuss in AkquiCo CH nicht vom Gesellschafter. Der Begriff „Gesellschafter" ist nicht wirtschaftlich, sondern zivilrechtlich geprägt, somit wird ein formeller Aktionärsbegriff zugrunde gelegt (BVGer vom 15. September 2009, Erw. 4.3.2). Allerdings Vorbehalt der Steuerumgehung …»
  - Position: P (Datumsangabe des BVGer-Urteils im Chunk vermutlich ungenau; BVGE 2009/21 datiert 15.4.2009 – am Original prüfen).
- **Stocker/Wolfensberger, Kauf und Verkauf von personenbezogenen Unternehmen, St. Galler Seminar zur Besteuerung von personenbezogenen Unternehmen 2025, Frage 2** — Chunk aa563015-11a3-4261-8dbb-ad7d1062ed1a — https://app.lexplorer.ch/suche?e_chunks=48864&e_sys=ile (heute gelesen); Referent:innen: Raoul Stocker, Thomas Wolfensberger: «Liegt keine gewinnsteuerneutrale Spaltung vor, gilt für die Emissionsabgabe grundsätzlich die zivilrechtliche Betrachtungsweise (ESTV KS 5a, Ziff. 4.3.5) – Da die OpCo 1 nicht durch A., den Inhaber der Beteiligungsrechte, eingebracht wird, ist die Emissionsabgabe nicht betroffen.» Position P.
- **Oesterhelt/Tschan, § 6, Abschn. IV, und Seminar 2025, Folien 79 ff.** (Vorlauf art-5, ILE-C.7): VSt-seitig modifizierte Dreieckstheorie bei Sanierung; **Spannungsfeld** zur EA (formeller Zuschussbegriff). Position K/O. Ältere abweichende Praxis: MB S-02.141 (Februar 2001), I.1 a) (Dreieckstheorie mit Zuschuss bei der sanierten Gesellschaft; Vorlauf art-5).

### (4) lit. c: Mantelhandel – Reinvermögen, stille Reserven, Bewertung, mindestens Nennwert

- **Waldburger, Rechtsprechung im Jahr 2008 (1. Teil), FStR 2009 Heft 3, Abschn. 2** — Chunk 64752cf5-0b9f-48cb-9c67-baf1c0841174 — https://app.lexplorer.ch/suche?e_chunks=15125&e_sys=ile (heute gelesen); Autor: Robert Waldburger
  - Wörtlich: «Die Qualifikation des beim Mantelhandel zur Besteuerung gelangenden Substrats als Liquidationsüberschuss - und nicht als Kapitalgewinn - vermag zu überzeugen. Sie entspricht auch ständiger Praxis beim Mantelhandel im Zusammenhang mit im Privatvermögen gehaltenen Anteilen an Kapitalgesellschaften.»
  - Aussage: Der Mantelhandel wird als fingierte Liquidation mit Neugründung behandelt; das besteuerte Substrat ist Liquidationsüberschuss (VSt-/ESt-Seite).
  - Position: P (bestätigend); weitere Kritik an der Gewichtung der Indizien in Chunks 9/11 (Vorlauf art-5, ILE-D.1).
- **Bauer-Balmelli, Die Steuerumgehung im Verrechnungssteuerrecht, FStR 2002 Heft 3, Abschn. 3.1.1** (Vorlauf art-5, ILE-D.2; e_chunks=3062): «Der Handwechsel einer Mehrheit von Beteiligungsrechten … wird steuerlich wie eine Liquidation mit anschliessender Neugründung behandelt; dies sowohl für Zwecke der allgemeinen Einkommenssteuern, der Emissionsabgabe als auch der Verrechnungssteuer.» Position: dogmatische Einordnung (objektivierte Umgehung), A zu Waldburger.
- **Bertschinger/Regli, Massgeblichkeiten der handelsrechtlichen Bücher, FStR 2021 Heft 4, Abschn. 4.2.1** (Vorlauf art-5, ILE-A.4; e_chunks=11150): «Die sich am Eigenkapital bemessende Emissionsabgabe orientiert sich für die Beweisfunktion dabei stark an der handelsrechtlichen Verbuchung.» – Mantelhandel «nach den wirtschaftlichen Gegebenheiten - wie sie in der Bilanz und Erfolgsrechnung widergespiegelt werden». Position P (Beweisfunktion der Bilanz; mittelbar für «Reinvermögen»).
- **Hongler/Sutter, FStR 2018 Heft 4, Abschn. 2.2.2** (Vorlauf art-5, ILE-D.3; e_chunks=5922): ESTV erhob «sowohl die Emissionsabgabe als auch die Verrechnungssteuer auf dem Liquidationsüberschuss». Position K (Automatismus EA → VSt). Hinweis: Hongler ist Lehrstuhlinhaber.
- **ESTV-Praxis:** kein Kreisschreiben oder Merkblatt zur Bemessung beim Mantelhandel (Suche 15; OCL 3; Vorlauf art-5). MB S-027.289.1 Ziff. 1/2 nur VSt (Verlustvortrag nach Mantelhandel).
- **Hinweis Rechtsprechung (Querverweis, nicht Lexplorer):** art-5 Praxis_BVGer.md, Nr. 29 (A-7094/2008: «Bemessung nach Reinvermögen, Freibetrag Bst. h, Überpari-Praxis») und Nr. 31 (A-5128/2024, bestätigt durch BGer 9C_232/2026 laut art-7 Entscheidregister). Am Original prüfen.
- **Lücke:** Keine ILE-Aussage zur Bewertung des Reinvermögens (stille Reserven, Goodwill, latente Steuern) und zur Mindestbemessung «Nennwert aller bestehenden Beteiligungsrechte» (Suche 6).

### (5) Abs. 3: Verkehrswert im Zeitpunkt der Einbringung; Bewertungsmethoden; Immaterialgüter

- **Oesterhelt/Tschan, § 7, Bd. 128 (2025), Abschn. I.2, N 4–6** — Chunk d24439fb-28fd-4c22-8fa3-95bf9d043578 — https://app.lexplorer.ch/suche?e_chunks=30329&e_sys=ile (heute gelesen)
  - Wörtlich: «Mangels Anwendung des Ausnahmetatbestandes nach Art. 6 Abs. 1 Bst. a bis StG unterliegt die Einlage nach Art. 5 Abs. 2 Bst. a StG im Umfang des Verkehrswertes der Emissionsabgabe.»
  - Aussage: Sacheinlage ohne Nennwerterhöhung = Zuschuss zum Verkehrswert.
  - Position: P.
- **Oesterhelt/Tschan, § 7, Abschn. I.3 (Enkelgesellschaft), N 14–16** — Chunk decd2906-3fec-4706-9c54-1f59008844b5 — https://app.lexplorer.ch/suche?e_chunks=30330&e_sys=ile (heute gelesen): «Da die frühere Praxis der ESTV zum Kaskadenzuschuss aufgegeben wurde, ist somit auch bei der Y. AG 1 % Emissionsabgabe (CHF 1 Mio.) geschuldet.» Position P.
- **Oesterhelt/Tschan, § 1 I–V, N 68 ff. (Beteiligungsausgliederung)** — Chunk 4f491229-e750-4236-b9a7-567eb0988bdc — https://app.lexplorer.ch/suche?e_chunks=29840&e_sys=ile (Sachverhalt «Beteiligung Z. AG, welche einen Verkehrswert von CHF 100 Mio. aufweist, als Sacheinlage»); Beurteilung (Vorlauf art-5, ILE-E.1): «Somit kann in analoger Anwendung der Regel von KS 6a grundsätzlich nur Aktienkapital im Umfang von 30 % (d. h. CHF 30 Mio.) gebildet werden.» Position P.
- **Oesterhelt/Tschan, Seminar 2018 «Entwicklungen Verrechnungssteuer und Stempelabgaben», Folie 31** — Chunk db247e4c-a8fe-4ea7-9870-41538f3050e3 — https://app.lexplorer.ch/suche?e_chunks=65235&e_sys=ile (heute gelesen): «Sacheinlage der Beteiligung 2016 durch A in SwissCo ist Zuschuss i.S.v. Art. 5 Abs. 2 lit. a StG, welcher grundsätzlich der Emissionsabgabe unterliegt. Aber: Beteiligungsausgliederung daher Befreiung …» – «Es können im Umfang des Verkehrswertes der eingebrachten Beteiligung (CHF 100 Mio.) bei SwissCo KER gebildet werden.» Position P (Gleichlauf Verkehrswert EA/KER).
- **Oesterhelt/Tschan, Seminar 2023, Folie «Beurteilung»** — Chunk 7589e84a-7d6d-46ed-ae3a-b0b597b2c5d1 — https://app.lexplorer.ch/suche?e_chunks=53391&e_sys=ile (heute gelesen): Sacheinlage einer 30 %-Beteiligung = Zuschuss; Umstrukturierungstatbestand bejaht. Position P. – Ebenso Chunk 350af3fe-961e-4807-8299-10fba459d030 (e_chunks=53405): «Einlage durch A (inkl. Variante) unterliegt gemäss Art. 5 Abs. 1 Bst. a StG der Emissionsabgabe Bildung von KER im Umfang der Einlage von A … (unter Berücksichtigung Nominalwert)».
- **Immaterialgüter:** Oesterhelt/Tschan, § 7, Variante IP (Chunk 30341, oben 3.2): Bemessung nach «Verkehrswert: CHF 500 Mio., Buchwert: CHF 0.01»; Befreiung nur bei Betriebsnotwendigkeit. Position P.
- **ESTV, Checkliste Mitteilung-020:** Abschn. «Gründung oder Aktienkapitalerhöhung mit Agio»: «Sacheinlagevertrag oder Vermögensübertragungsvertrag – Bewertungsgutachten»; Abschn. «Forderungsverzicht oder Zuschuss» und «Ausgliederung»: «Bewertungsgutachten, falls Transaktion zum Verkehrswert erfolgt». Position P (Beweismittel für Abs. 3).
- **ESTV, KS 5a, Ziff. 4.1.7.5:** «… ist eine Kapitalerhöhung im Umfang von in der Regel 30 Prozent des Verkehrswertes der übertragenen Beteiligung(en) zulässig.» Position P (Verkehrswert als Referenz für Abgabeumgehung).
- **KS 28 SSK?** – **SSK, Kreisschreiben Nr. 28 vom 28.8.2008, Wegleitung zur Bewertung von Wertpapieren ohne Kurswert für die Vermögenssteuer (Fassung 2022)**, Lexplorer-Dokument ed3cb7a9-5106-43ce-8804-1c4de4ca5c04 — https://mcp-tax.lexplorer.ch/s/doc/ed3cb7a9-5106-43ce-8804-1c4de4ca5c04 (Rz. 1–69 heute gelesen)
  - Rz. 1 Abs. 1: «Diese Wegleitung bezweckt im Rahmen der Vermögenssteuer eine in der Schweiz einheitliche Bewertung von inländischen und ausländischen Wertpapieren, die an keiner Börse gehandelt werden.» – Rz. 2 Abs. 5: «Hat für Titel gemäss Absatz 4 eine massgebliche Handänderung unter unabhängigen Dritten stattgefunden, dann gilt als Verkehrswert grundsätzlich der entsprechende Kaufpreis. Ein Verkehrswert wird auch durch Preise begründet, welche von Investoren anlässlich von Finanzierungsrunden bzw. Kapitalerhöhungen bezahlt wurden.» – Rz. 34: «Der Unternehmenswert ergibt sich aus der zweimaligen Gewichtung des Ertragswertes und der einmaligen Gewichtung des Substanzwertes zu Fortführungswerten» (U = (2E+S)/3). – Rz. 61 Abs. 1 und 3: «Dem beschränkten Einfluss des Inhabers einer Minderheitsbeteiligung auf die Geschäftsleitung … wird pauschal Rechnung getragen.» – «… kann der Titelinhaber … einen Pauschalabzug von 30 % geltend machen.» – Rz. 62 Abs. 3: «Sobald der Inhaber einer Minderheitsbeteiligung über einen beherrschenden Einfluss verfügt …, wird der Pauschalabzug nicht gewährt.»
  - Aussage: KS 28 gilt nach Rz. 1 nur für die Vermögenssteuer; eine Übernahme für die Emissionsabgabe ist weder im KS noch in ESTV-Texten vorgesehen.
  - Position: P (nur Analogie).
- **Brozzo/Stocker, Steuerliche Bewertung nicht-kotierter Unternehmen, FStR 2021 Heft 2, Ziff. 1 (Fn. 7/8) und Ziff. 5** — Chunks 29fe1545-3d6e-48af-a2b4-ab71477c231d (https://app.lexplorer.ch/suche?e_chunks=10584&e_sys=ile) und 93c29181-bb15-4f5a-8838-a8d55e6e2163 (https://app.lexplorer.ch/suche?e_chunks=10618&e_sys=ile) (heute gelesen); Autor:innen: Hanna Brozzo, Raoul Stocker
  - Wörtlich: «Bemerkenswert erscheint in diesem Zusammenhang lediglich, dass das Bundesgericht in seinem Entscheid vom 18.9.2013 (BGer 2C_309/2013) für die Zwecke der Gewinnsteuer festgehalten hat, dass die Praktikermethode nach KS SSK 28 nicht geeignet ist und vielmehr international verbreitete, zukunftsorientierte Bewertungsmethoden zu verwenden sind.» – «Das Schweizer Steuerrecht zeichnet sich im Bereich der Bewertung von Unternehmen durch einen eigentlichen Methodenpluralismus aus.» – «Bei Minderheitsbeteiligungen sollte zudem - unabhängig von der Dividendenpolitik und Art des Unternehmens - ein Einschlag von zwischen 10 % und 30 % gewährt werden.»
  - Aussage: Praktikermethode ist ein Massenverfahren-Instrument der Vermögenssteuer; bei Transaktionen (Gewinnsteuer) verlangt das BGer zukunftsorientierte Methoden.
  - Position: K (an Kapitalisierungssatz, Minderheitsabzug); für die Emissionsabgabe nur Analogie, kein Stempelabgaben-Abschnitt im Beitrag.
- **Hinweis Rechtsprechung (Querverweis):** art-5 Praxis_BVGer.md Nr. 8: BVGer A-6592/2013 E. 2.5 (Bewertung nach Art. 8 Abs. 3 StG zum Verkehrswert im Einbringungszeitpunkt), E. 3.2.2 (kein Minderheitsabzug bei Erlangung voller Kontrolle); art-7 Entscheidregister: BVGer A-267/2015 E. 2.3 (Stichtag, spätere Korrekturen der Jahresrechnung unbeachtlich). Am Original prüfen.
- **Lücke:** Keine ESTV-Verwaltungsverordnung und kein ILE-Beitrag zu Bewertungsmethoden **für die Emissionsabgabe** (Praktikermethode, DCF, Minderheitsabzug, Kontrollprämie) (Suchen 4, 11; OCL 4).

### (6) Verhältnis zu Art. 9 StG, Freibetrag Art. 6 Abs. 1 lit. h und lit. k, VSt/KER

**6.1 Art. 9 Abs. 1 lit. e StG (1 % des Nennwerts bei Umwandlung von Nicht-Kapitalgesellschaften)**
- **ESTV, KS 5a vom 1.2.2022, Ziff. 2.4.1** (Chunk fca050a7-c150-48c4-88e2-a46fe552bc6b; OCL): «Artikel 9 Absatz 1 Buchstabe e StG bestimmt, dass die Emissionsabgabe bei der Begründung oder Erhöhung von Beteiligungsrechten im Rahmen von Fusionen, Spaltungen oder Umwandlungen von andern Rechtsträgern als Kapitalgesellschaften und Genossenschaften auf ein Prozent des Nennwerts beschränkt wird. Die Reduktion der Bemessungsgrundlage für die Emissionsabgabe bei Fusionen, Spaltungen oder Umwandlungen wird jedoch nur dann gewährt, wenn der bisherige Rechtsträger während mindestens fünf Jahren bestand. Im Weiteren wird über den Mehrwert nachträglich abgerechnet, soweit während den der Umstrukturierung nachfolgenden fünf Jahren die Beteiligungsrechte veräussert werden.» Position P.
- **KS 5a, Ziff. 3.2.6** (Personenunternehmung): «… vorbehältlich des Freibetrages nach Artikel 6 Absatz 1 Buchstabe h StG, 1 Prozent des Nennwerts. Die übertragenen offenen und stillen Reserven sind von der Steuer ausgenommen.» – «Der Übergang des Eigentums an den Beteiligungsrechten durch Erbgang, Schenkung oder andere unentgeltliche Rechtsgeschäfte, einschliesslich steuerneutraler Umstrukturierungen, stellt keine Sperrfristverletzung dar. Dies gilt auch für entgeltliche Übertragungen, sofern der Preis das übertragene Eigenkapital nicht übersteigt.» Position P.
- **KS 5a, Anhang Beispiel Nr. 2** (Umwandlung Einzelunternehmen A. Müller in GmbH; Sperrfristverletzung; Zahlen in Tausend CHF): «Im Weiteren ist über den Mehrwert nachträglich anteilsmässig abzurechnen, soweit während den der Umwandlung nachfolgenden fünf Jahren Beteiligungsrechte veräussert werden und der Verkehrswert den Freibetrag (Art. 6 Abs. 1 Bst. h StG) übersteigt. Berechnung Sperrfristverletzung gemäss Beispiel a): Stammkapital 100 / 60% der übertragenen offenen Reserven von 100 60 / 60% der übertragenen stillen Reserven von 500 300 / 460 Nach Abzug des Freibetrags von 1'000 ist keine Emissionsabgabe geschuldet.» Aussage: Nachbemessung = Nennwert + anteilige offene und stille Reserven (also Verkehrswert des übertragenen Eigenkapitals), abzüglich lit. h. Position P.
- **KS 5a, Ziff. 4.2.1.5, 4.2.4.5, 4.2.5.4** (Verein, Stiftung, Unternehmen des öffentlichen Rechts) gleichlautend; **Anhang Beispiel Nr. 8** (Institut des öffentlichen Rechts): «Der Nennwert der im Zuge der Umwandlung begründeten Beteiligungsrechte beträgt 2'000. Von diesem Betrag kann der noch nicht beanspruchte Freibetrag (Art. 6 Abs. 1 Bst. h StG) in Abzug gebracht werden.» Position P.
- **ILE:** kein eigener Beitrag zu Art. 9 Abs. 1 lit. e (Suche 10). Oesterhelt/Tschan, § 1 XII–XIX, N 217–219 (Stiftung; Vorlauf art-6, e_chunks=29871): lit. abis nicht anwendbar, Art. 9 Abs. 1 lit. e StG anwendbar. Oesterhelt/Tschan, Seminar 2025, Folie 74 (Chunk 600d0652-ba7a-4de9-94ae-07e71b77e9e8, e_chunks=48395, heute gelesen) betrifft nur KER bei direkter Umwandlung übriger juristischer Personen.
- **ESTV, KS 5 vom 1.6.2004, Ziff. 4.4.1.3** (aufgehoben; Vorlauf art-7): «… ist die Emissionsabgabe anteilsmässig auf dem Verkehrswert des übertragenen Aktivenüberschusses … geschuldet.» Position: frühere Praxis.

**6.2 Freibetrag lit. h (1 Mio.) und lit. k (10 Mio.)**
- Dossier 2026 «Freibetrag», Broschüre 2025 «Freigrenze» (oben 1.1/1.2); Baumann FStR 2004/1 «echte Freigrenze … Erhöhung der Freigrenze … auf CHF 1 Mio.» (Vorlage).
- Checkliste Mitteilung-020: lit. h und lit. k bei als KER geltend gemachten, nicht mit Verlusten verrechneten Zuschüssen «nicht anwendbar».
- Oesterhelt/Tschan, § 1 VI–XI, N 136 (oben 3.2): Befreiung nach lit. abis verbraucht den Freibetrag lit. h für künftige Kapitalerhöhungen. Position P.
- KS 32a, Ziff. 3.3.2 c): «Der Freibetrag von 10 Millionen Franken ist einmalig, kann sich aber auf mehrere Sanierungen aufteilen.» Ziff. 3.3.3: Kapitalreserven, auf welchen die Emissionsabgabe entrichtet wurde, «werden wie nominelles Kapital behandelt». Position P.
- Oesterhelt/Tschan, § 6 VI.2.6 (Vorlauf art-6): «Somit gilt die … Wahlmöglichkeit zwischen Reserven aus Kapitaleinlagen einerseits und Emissionsabgabebefreiung andererseits nicht mehr uneingeschränkt.» Position K/O.

**6.3 Verrechnungssteuer / Kapitaleinlagereserven**
- KS 29c Ziff. 2.1 (Ausgabekosten), Ziff. 2.2.1 (Schwesterleistungen keine KER), Ziff. 2.2.3 (Sanierung: erfolgswirksame Forderungsverzichte «nie als KER») – Vorlauf art-5; KS 29c enthält zur Emissionsabgabe keine Ausführungen (Grep heute: kein Treffer «Emissionsabgabe»; ebenso Oesterhelt/Tschan § 4 N 72).
- Oesterhelt/Tschan, Seminar 2018 (Chunk 65235): KER «im Umfang des Verkehrswertes der eingebrachten Beteiligung» – Gleichlauf der Bewertung EA/KER.
- Mitteilung-020-DVS-2024 vom 18.9.2024 (Hauptmitteilung, Lexplorer-Dokument eedd23ad-e753-4cb9-bde6-c4e8fcdd443b): KER-Meldung «mittels Formular 170»; Kapitalband «erst nach Beendigung des Kapitalbands». Position P.

---

## 3. Verwaltungspraxis (Register mit Ziffern und Wortlaut)

**V.1 ESTV, Kreisschreiben Nr. 5a vom 1. Februar 2022, Umstrukturierungen (direkte Bundessteuer, Verrechnungssteuer und Stempelabgaben), 1-005a-DVS-2022-d**
- OCL doc_id: estv_ks_dbst_ks_2022_1_005a_dvs_de; PDF https://www.estv.admin.ch/dam/de/sd-web/BmJ1WWSC79gq/dbst-ks-2022-1-005a-dvs-de.pdf; Lexplorer-Dokument https://mcp-tax.lexplorer.ch/s/doc/e163e163-e38f-4631-85a6-455c20a8c29a (Chunks: Ziff. 2.4.1 fca050a7-c150-48c4-88e2-a46fe552bc6b; Fortsetzung 9170fcb7-2a44-4cf5-afa2-fa5d338547b9; 4.1.2.5–4.1.7.5 54f9e916-814e-4322-b245-3f48a9521892; 4.3.5/4.4 2e7dba3e-0b62-411c-a16d-a4c0dc226ba6; 4.5.4 33c7e60d-835d-4e35-b165-29dc4ac608d4)
- Ziff. 2.4.1: «Der Tatbestand von Artikel 6 Absatz 1 Buchstabe abis StG setzt nicht voraus, dass die für die direkte Bundessteuer massgeblichen Werte übernommen werden.» + Art. 9 Abs. 1 lit. e (oben 6.1).
- Ziff. 3.2.6, 4.2.1.5, 4.2.4.5, 4.2.5.4: 1 % des Nennwerts, Reserven ausgenommen, fünf Jahre Bestand, nachträgliche Abrechnung über den Mehrwert (oben 6.1).
- Ziff. 4.1.2.5: «Nicht abgabebefreit sind (vorbehältlich Art. 6 Abs. 1 Bst. d StG): a) Eine Kapitalerhöhung der übernehmenden Gesellschaft, die das nominelle Kapital der übertragenden Gesellschaft übersteigt, sofern die Merkmale der Abgabeumgehung erfüllt sind. b) Eine zusätzliche Kapitalerhöhung der übernehmenden Gesellschaft. c) Eine Kapitalerhöhung der übertragenden Gesellschaft im Hinblick auf eine Fusion.» – «Verwendet die übernehmende Gesellschaft für den Austausch der Titel eigene Beteiligungs­rechte, deren Rückkauf bereits steuerlich abgerechnet worden ist, löst dies keine Emissions­abgabe aus, weil das förmliche Kapital durch den Rückkauf und die anschliessende Wieder­ausgabe nicht berührt ist …»
- Ziff. 4.1.5.4: «Eine allfällige – der Verrechnungssteuer unterliegende – Kapitalerhöhung der Muttergesell­schaft bis zur Höhe des Kapitals der übertragenden Tochtergesellschaft ist nach Artikel 6 Ab­satz 1 Buchstabe abis StG von der Emissionsabgabe ausgenommen.»
- Ziff. 4.1.7.5: 30 % des Verkehrswerts ausländischer Beteiligungen (oben 5).
- Ziff. 4.3.5 / 4.4.1.4 / 4.4.2.4: «Nicht abgabebefreit ist derjenige Teil des neu geschaffenen nominellen Kapitals der überneh­menden Gesellschaft(en), der das minimal erforderliche Eigenkapital nach dem Kreisschreiben der ESTV Nr. 6 vom 6. Juni 1997 betreffend verdecktes Eigenkapital (Art. 65 DBG) … übersteigt, sofern die Merkmale der Abgabeumge­hung erfüllt sind.» – Ziff. 4.3.5: «Liegt keine gewinnsteuerneutrale Spaltung vor, gilt für die Emissionsabgabe grundsätzlich die zivilrechtliche Betrachtungsweise.»
- Ziff. 4.6.4: «Die Emissionsabgabe ist auf der Stufe der übernehmenden Kapitalgesellschaften und Genos­senschaften (Emittent) betroffen (vgl. Ziff. 4.1.2.5).»
- Anhang Nr. 2, 3, 8 (Art. 9 Abs. 1 lit. e; oben 6.1); Nr. 10, 11, 13, 14, 15, 16, 21, 25: «Da die Vermögenswerte vorliegend nicht durch den (direkten) Inhaber der Beteiligungsrechte eingebracht werden, ist die Emissionsabgabe nicht betroffen.»; Nr. 6: «Die ohne Kapitalerhöhung erfolgte Absorption der Muttergesellschaft ist nach Artikel 6 Absatz 1 Buchstabe abis StG von der Emissionsabgabe ausgenommen.»
- Bemessung ausdrücklich: nur über Art. 9 Abs. 1 lit. e (Nennwert; Nachbemessung mit Reserven/Verkehrswert). Zu Art. 8 Abs. 1 lit. a, b, c und Abs. 3 enthält KS 5a keine eigene Regel.

**V.2 ESTV, Kreisschreiben Nr. 32a vom 20. Januar 2025, Sanierung von Kapitalgesellschaften und Genossenschaften (Direkte Bundessteuer, Verrechnungssteuer und Stempelabgaben)**
- OCL doc_id: estv_ks_dbst_ks_2025_1_032a_dvs_de (ganz gelesen); PDF https://www.estv.admin.ch/dam/de/sd-web/NkHH-TkCqMnq/dbst-ks-2025-1-032a-dvs-de.pdf; Lexplorer https://mcp-tax.lexplorer.ch/s/doc/c5dfca80-98f2-47a1-a63b-a8660c765a93 (Ziff. 3.3 626a736f-56ad-4c0a-9c46-807c9f5f4b86; 4.1.3 0c90ec1f-6b1f-46c5-87bf-d3fba7ec13de; 4.2.4 a) 88604f4c-1d9a-4864-b989-c5108205e4b3; b) 8b50916c-d9c2-4c38-b1c6-171458c71f9c)
- Ziff. 3.3: «Nach Artikel 6 Absatz 1 Buchstaben j und k StG sind … offene und stille Sanierungen von Kapitalgesellschaften oder Genossenschaften bis zu einem Gesamtbetrag von zehn Millionen Franken (Freibetrag) von der Emissionsabgabe ausgenommen.»
- Ziff. 3.3.2 c): «Bei offenen oder stillen Sanierungen sind die Leistungen der Anteilsinhaber, welche den Be­trag von gesamthaft 10 Millionen Franken nicht übersteigen, von der Emissionsabgabe aus­genommen.» – «Wenn der Freibetrag von 10 Millionen Franken überschritten wird, ist ein Erlass der Emissi­onsabgabe gemäss Artikel 12 StG auf den, den Freibetrag übersteigenden Sanierungsleis­tungen weiterhin möglich …»
- Ziff. 3.3.3 (Erlass): «Kapitalreserven, auf welchen die Emissionsabgabe entrichtet wurde oder welche von der Emissionsabgabe wegen Umstrukturierung ausgenommen waren, werden wie nominel­les Kapital behandelt und stehen dem Erlass der Emissionsabgabe nicht entgegen»; «keine Übersanierung vorliegt (keine Bildung oder Erhalt von offenen und/oder stillen (Willkür)-Reserven …)».
- Ziff. 3.3.4, 4.1.3 a)–c), 4.2.4 a)–b): oben 3.1, 3.3, 2.7.
- Einzige ausdrückliche Anwendung von Art. 8 Abs. 1 lit. a StG in der ESTV-Praxis: Ziff. 4.2.4 b) (Gesamtbetrag der Forderungsverzichte als Zufluss).

**V.3 ESTV, Kreisschreiben Nr. 29c vom 23. Dezember 2022, Kapitaleinlageprinzip (Direkte Bundessteuer, Verrechnungssteuer und Stempelabgaben)**
- OCL doc_id: estv_ks_dbst_ks_2022_1_029c_dvs_de; PDF https://www.estv.admin.ch/dam/de/sd-web/h36nmhxQYuz5/dbst-ks-2022-1-029c-dvs-de.pdf; Lexplorer https://mcp-tax.lexplorer.ch/s/doc/2822de22-4ad4-4636-9199-db732d79a79d
- Ziff. 2.1: «Einlagen, Aufgelder und Zuschüsse (gegebenenfalls nach Abzug der Ausgabekosten), wel­che direkt von den Inhabern der Beteiligungsrechte geleistet wurden und in der Handelsbi­lanz der empfangenden Kapitalgesellschaft oder Genossenschaft verbucht und offen ausge­wiesen sind (offene Kapitaleinlagen) gelten als Reserven aus Kapitaleinlagen (KER) …» – «… sind für Kapitaleinlagen in fremder Währung sowohl die Einlagen als auch die Rückzahlungen (im Zeitpunkt der jeweiligen Fälligkeit) von Reserven aus Kapitaleinlagen zum Tageskurs in Schweizer Franken umzurechnen.»
- Keine Aussage zur Emissionsabgabe (Grep: kein Treffer; vgl. Oesterhelt/Tschan § 4 N 72).

**V.4 ESTV, Kreisschreiben Nr. 37A vom 4. Mai 2018, Steuerliche Behandlung von Mitarbeiterbeteiligungen bei der Arbeitgeberin (Direkte Bundessteuer), 1-037A-D-2018-d**
- OCL doc_id: estv_ks_dbst_ks_2018_1_037a_d_de (ganz gelesen); PDF https://www.estv.admin.ch/dam/de/sd-web/idfYC2mWhSpo/dbst-ks-2018-1-037a-d-de.pdf
- Ziff. 2.1: «Bei börsenkotierten Mitarbeiteraktien gilt als Verkehrswert grundsätzlich der Börsenschluss­kurs am Tage des Rechtserwerbs … Bei nicht an einer Börse kotierten Mitarbeiteraktien gilt als massgeblicher Wert grundsätzlich der nach einer für die entspre­chende Arbeitgeberin tauglichen und anerkannten Methode ermittelte Formelwert.»
- Ziff. 3.1.2: «Die Arbeitgeberin verbucht das Arbeitsentgelt für die bereits geleistete Arbeit als geschäfts­mässig begründeten Aufwand zu Gunsten Verbindlichkeiten Mitarbeitende. Die Liberierung der Mitarbeiteraktien erfolgt anschliessend zu Lasten dieser Verbindlichkeiten. … Mit dieser Gutschrift werden, vermindert um die Emissionskosten, Reserven aus Kapi­taleinlagen begründet (vgl. Beispiel 2).» – «Spätestens im Zeitpunkt der Liberierung muss eine durchsetzbare Forderung des Mitarbeiten­den gegenüber der Arbeitgeberin bestehen; künftige Arbeitsleistungen reichen nicht aus.»
- Ziff. 3.2.1: «Beschafft die Konzerngesellschaft die Aktien mittels Kapitalerhöhung, zählt die von der Ar­beitgeberin im Rahmen der Entschädigung entrichtete Optionsprämie nicht zu den Reserven aus Kapitaleinlagen.»
- Keine Aussage zur Emissionsabgabe; nur mittelbar für den «Zufluss» (lit. a).

**V.5 ESTV, Mitteilung-020-DVS-2024-d vom 18. September 2024, Checkliste für Spezialfälle (PDF vom 16. Mai 2025)**
- OCL doc_id: estv_ks_estv_mitteilung_020_dvs_checkliste_de (ganz gelesen); PDF https://www.estv.admin.ch/dam/de/sd-web/2hqENQZfloRj/estv-mitteilung-020-dvs-checkliste-de.pdf; Lexplorer-Chunk 90d43197-c66f-423c-aef2-5781a90ed51c — https://mcp-tax.lexplorer.ch/s/doc/cc089a32-3c79-4649-bb8b-801e60de6539?chunk=90d43197-c66f-423c-aef2-5781a90ed51c
- «Ausgliederung»: «Bewertungsgutachten falls Transkation zum Verkehrswert erfolgt»
- «Forderungsverzicht oder Zuschuss»: «Bewertungsgutachten, falls Transaktion zum Verkehrswert erfolgt» – «Bei Zuschüssen und Forderungsverzichte ist das Formular 4 auszufüllen und einzureichen. Wurden diese Leistungen als KER geltend gemacht und nicht mit Verlusten verrechnet, ist die Emissionsabgabe von 1% auf dem Betrag des Zuschusses geschuldet. Die Art. 6 Abs. 1 Bst. h StG (Freibetrag 1 Mio. CHF) und Art. 6 Abs. 1 Bst. k StG (10 Mio. CHF) sind in diesen Fällen nicht anwendbar.» – «Steuerruling (… bei Einbringung von Sacheinlagen oder Beteiligungen)»
- «Gratisaktien»: «Nachweis über die Liberierung von Gratisnennwert zu Lasten von KER»
- «Gründung oder Aktienkapitalerhöhung mit Agio»: «Sacheinlagevertrag oder Vermögensübertragungsvertrag – Bewertungsgutachten – Hinweis auf Formular 3 (mit Angabe des Datums der Einreichung des Formulars bei der ESTV), sofern Emissionsabgabe deklariert wurde, andernfalls ist der Ausnahmetatbestand zu schildern.»
- «Kapitalband»: «Hinweis der Deklaration der Emissionsabgabe auf dem Nettozufluss mit Formular 3»
- «Währungswechsel»: «Nachweis des angewandten Wechselkurses»

**V.6 ESTV, Mitteilung-020-DVS-2024-d vom 18.09.2024, Verrechnungssteuer: Deklaration der Reserven aus Kapitaleinlagen**
- Lexplorer-Dokument eedd23ad-e753-4cb9-bde6-c4e8fcdd443b — https://mcp-tax.lexplorer.ch/s/doc/eedd23ad-e753-4cb9-bde6-c4e8fcdd443b (ganz gelesen); PDF https://www.estv.admin.ch/dam/de/sd-web/MZlDJcIa4QSH/estv-mitteilung-020-dvs-de.pdf
- «Einlagen in die beziehungsweise Rückzahlungen aus den KER, die während eines Kapitalbands … geleistet werden, sind aufgrund der Nettobetrachtung erst nach Beendigung des Kapitalbands als KER oder Ausland-KER mittels Formular 170 zu melden». Keine Emissionsabgabe-Aussage.

**V.7 ESTV, Mitteilung-022-DVS-2024-d vom 9. Dezember 2024, Eigene Aktien; Urteil 9C_135/2023 des Bundesgerichts vom 6. Juni 2024**
- Lexplorer-Dokument d0a484e2-31be-46b9-bb2a-5d3b6c8de8f0 — https://mcp-tax.lexplorer.ch/s/doc/d0a484e2-31be-46b9-bb2a-5d3b6c8de8f0 (ganz gelesen); PDF https://www.estv.admin.ch/dam/de/sd-web/W0dCk5U-q6mD/estv-mitteilung-022-dvs-2024-de.pdf
- «Entsprechend ist die Wiederbegebung von zuvor von der Gesellschaft zurückgekauften eigenen Aktien als steuerfreier Kapitaleinlagevorgang zu sehen.» – «Die Verrechnungssteuer und die Stempelabgaben sind vom Urteil 9C_135/2023 des BGer vom 6. Juni 2024 nicht betroffen.»
- Aussage: Die gewinnsteuerliche Qualifikation der Wiederbegebung als Kapitaleinlage ändert an der Emissionsabgabe nichts (kein Zufluss i.S.v. Art. 8 Abs. 1 lit. a, kein Zuschuss).

**V.8 ESTV, Mitteilung-029-S-2026 vom 5. Februar 2026, Umsatzabgabe – Mitarbeiterbeteiligungspläne**
- Lexplorer-Dokument dd13b4ec-0f37-4380-9849-beb770b7201f — https://mcp-tax.lexplorer.ch/s/doc/dd13b4ec-0f37-4380-9849-beb770b7201f (ganz gelesen); PDF https://www.estv.admin.ch/dam/de/sd-web/CWSSX4vBP6s-/estv-mitteilung-029-s-2026-de.pdf
- Ziff. 2.6: «Diese Sachverhalte sind jedoch auf eine mögliche Emissionsabgabe hin zu überprüfen.» (nur Abgrenzung UA/EA)

**V.9 ESTV, Dossier Steuerinformationen «Geltende Steuern», Juni 2026, Ziff. 2.2.3.1, und ESTV, «Das schweizerische Steuersystem», Juni 2025, Ziff. 8.2.3.1** – oben 1.1/1.2 (Informationsschriften, Lexplorer-Status «Materialien»; keine Verwaltungsverordnungen).

**V.10 SSK, Kreisschreiben Nr. 28 vom 28. August 2008, Wegleitung zur Bewertung von Wertpapieren ohne Kurswert für die Vermögenssteuer (Fassung 2022, mit Anpassungen bis 2020/2021)** – oben 5; Lexplorer https://mcp-tax.lexplorer.ch/s/doc/ed3cb7a9-5106-43ce-8804-1c4de4ca5c04; PDF https://www.ssk-csi.ch/fileadmin/dokumente/kreisschreiben/KS_28_d_2022.pdf. Rz. 1–69 ganz gelesen (Anhang/Beispiele nicht). Gilt für die Vermögenssteuer; keine Aussage zur Emissionsabgabe.

**V.11 Ältere/aufgehobene Praxis (aus Vorläufen, nicht erneut gelesen):** ESTV, KS 5 vom 1.6.2004 (OCL estv_ks_dbst_ks_2004_1_005_dvs_de), Ziff. 4.4.1.3, 4.5.4 (Sperrfrist; Verkehrswert des Aktivenüberschusses; Fälligkeit 30 Tage); MB S-027.289.1 vom 30.4.1999 (Gratisaktien); MB S-02.141 vom Februar 2001 (Dreieckstheorie bei Sanierung, zur EA inhaltlich durch KS 32a Ziff. 4.1.3 b überholt); KS 29a/29b (Lexplorer-Treffer Suche 15, OCL 1: «Für Kapitaleinlagen, welche diesen Freibetrag übersteigen, kann … der Erlass von der Emissionsabgabe …» – Sanierungspassage, durch KS 29c ersetzt; nicht gelesen).

**Nicht vorhanden (beide Korpora):** Merkblatt oder Wegleitung der ESTV zur Emissionsabgabe auf Beteiligungsrechten (Formulare 1/3/4), insbesondere zur Bemessung (Agio, Emissionskosten, Abgabe auf der Abgabe), zum Mantelhandel (Reinvermögen) und zu Bewertungsmethoden nach Abs. 3. Die ESTV-Quelle «Stempelabgaben» in Lexplorer enthält nur KS 12, KS 33, Mitteilung 2008 Sondervermögen, MB S-02.135, S-02.140.

---

## 4. ILE-Literatur (Register)

| Nr. | Werk | Autor:innen | Fundort (Chunk / URL) | Sachfrage | gelesen |
|---|---|---|---|---|---|
| L1 | Oesterhelt/Tschan, Verrechnungssteuer und Stempelabgaben – Fallbeispiele zu aktuellen Entwicklungen, Schriftenreihe Finanzwissenschaft und Finanzrecht Bd. 128, 2025: § 7 Emissionsabgabe (N 4–6, 14–16, 25, 33–37, Abschn. V) | Stefan Oesterhelt, David Tschan | 30329, 30330, 30332, 30334, 30338, 30341 (heute); 30335/30336 (Vorlauf) | 2, 3, 5 | ja |
| L2 | dito, § 6 Sanierung (III.2.1; VI) | dies. | 30428 (heute); e_id=1054 (Vorlauf) | 2, 3, 6 | ja |
| L3 | dito, § 4 KER (N 68–72; Abschn. 5) | dies. | 30315, 30317 (heute) | 2 (Kapitalband), 6 | ja |
| L4 | dito, § 1 Umstrukturierungen I–V (N 68 ff.), VI–XI (N 134–137), XII–XIX (N 155 ff.) | dies. | 29840, 29746, 29845 (heute); 29841, 29871 (Vorlauf) | 3, 5, 6 | ja |
| L5 | Oesterhelt/Tschan, Impôt anticipé et droits de timbre, Schriftenreihe Bd. 132, 2026, § 10 IV (N 54–58) | dies. | 46363, 46365 (heute) | 2 (COTD) | ja |
| L6 | Bertschinger, Die handels- und steuerrechtliche Behandlung von Mitarbeiterbeteiligungen bei der Arbeitgeberin, FStR 2023 Heft 1, Ziff. 2.1.2.3, 2.2.3.3, 5 | Michael Bertschinger | 12511, 12533, 12541 (heute) | 2 | ja |
| L7 | Bertschinger/Risi, Seminar Unternehmensbesteuerung 2023 | Michael Bertschinger, Andreas Risi | 53568 (heute) | 2 | ja |
| L8 | Oesterhelt/Tschan, Seminar Unternehmensbesteuerung 2020 (COTD) | Stefan Oesterhelt, David Tschan | 57923, 57924 (heute) | 2 | ja |
| L9 | Oesterhelt/Tschan, Seminar Unternehmensbesteuerung 2022 (Kapitalband) | dies. | 54972 (heute) | 2 | ja |
| L10 | Oesterhelt/Tschan, Seminar Unternehmensbesteuerung 2025 (Folien 91–93 Erlass; 74 Umwandlung) | dies. | 48410, 48411, 48412, 48395 (heute) | 3, 6 | ja |
| L11 | Oesterhelt/Tschan, Seminar Unternehmensbesteuerung 2018 (Folie 31) und 2023 (Folien Sacheinlage, Kauf AG) | dies. | 65235, 53391, 53405 (heute) | 5 | ja |
| L12 | Risi-Bravin/Stocker, Besteuerung von Private Equity, Seminar personenbezogene Unternehmen 2019 | Véronique Risi-Bravin, Raoul Stocker | 64016 (heute) | 1, 2 (Emissionskosten) | ja |
| L13 | Brozzo/Stocker, Steuerliche Bewertung nicht-kotierter Unternehmen, FStR 2021 Heft 2, Ziff. 1, 5 | Hanna Brozzo, Raoul Stocker | 10584, 10618 (heute) | 5 (Analogie) | ja |
| L14 | Schreiber/Wolfensberger, Seminar 2021 (Bilanzsteuerrecht), 2023 (Bilanzsteuerrecht/Beteiligungsabzug), 2025 (Bilanzsteuerrecht, Beteiligungsabzug, Pillar 2) | Susanne Schreiber, Thomas Wolfensberger | 59470, 53606, 48603, 48604 (heute) | 2 (Fremdwährung), 3 (Analogie) | ja |
| L15 | Heuberger/Zitter, Internationales Steuerseminar 2016 | Reto Heuberger, Gernot Zitter | 61917 (heute) | 3 | ja |
| L16 | Stocker/Wolfensberger, Seminar personenbezogene Unternehmen 2025 | Raoul Stocker, Thomas Wolfensberger | 48864 (heute) | 3 | ja |
| L17 | Waldburger, Rechtsprechung im Jahr 2008 (1. Teil), FStR 2009 Heft 3, Abschn. 2 | Robert Waldburger | 15125 (heute); weitere Chunks Vorlauf | 4 | ja |
| L18 | Baumann, Unternehmenssteuerreform II – Zur Vernehmlassungsvorlage, FStR 2004 Heft 1 (Ziff. 3.2.2) und Heft 2 | Ruedi Baumann | 8138, 8028 (heute) | 1, 6 | ja |
| L19 | Oesterhelt/Opel, Rechtsprechung im Steuerrecht 2023/2 (Ziff. 1.3), 2023/4 (Ziff. 5), 2024/3 (Ziff. 2.3), FStR 2023 Heft 2 und 4, FStR 2024 Heft 3 | Stefan Oesterhelt, Andrea Opel | 13033–13035, 13568–13574, 18651 (Vorlauf art-5) | 2, 3, 6 | Vorlauf |
| L20 | Bauer-Balmelli, FStR 2002 Heft 3; Bertschinger/Regli, FStR 2021 Heft 4; Hongler/Sutter, FStR 2018 Heft 4; Rohner, FStR 2017 Heft 3; Weidmann, FStR 2010 Heft 1 | je wie angegeben | 3062, 11150, 5922, 4910, 15940 (Vorlauf art-5) | 3, 4 | Vorlauf |
| L21 | Baumer/Marty, Seminar 2021; Baumgartner/Duss/Fenners, FStR 2021/4, 2022/3 | Fabian Baumer, Frank Marty; Heinz Baumgartner, Pascal Duss, Henk Fenners | 59140, 59143, 11072, 11859 (Vorlauf art-5) | 1 | Vorlauf |

Nicht verwendet: Lehrbuch Steuerrecht (Vorgabe); Neuhaus, FStR 2001/1 (nur DBG-Sperrfristen); Hug, FStR 2026 (USTR 1997 ohne Emissionsabgabe); Brülisauer, FStR 2017/1 (nur Gewinnsteuer); Oesterhelt/Tschan Bd. 132 Part 5 N 163 f. (nur KER); MWST-Seminare (Sacheinlage/Emissionsrechte).

---

## 5. Lücken (gelesen, kein Fund)

1. Abgabe auf der Abgabe / Überwälzung (Hochrechnung), Abzug Emissionskosten: nur Risi-Bravin/Stocker (Folie, ohne Beleg); keine ESTV-Verwaltungsverordnung.
2. Forderungsverzicht: Nennwert oder werthaltiger Teil als «Betrag des Zuschusses» – weder ESTV noch ILE ausdrücklich zur Emissionsabgabe; KS 32a Ziff. 4.2.4 b) spricht vom «Gesamtbetrag».
3. Nutzungsvorteile (zinsloses Darlehen, Gewinnverzicht) als Zuschuss und deren Bemessung – kein Fund (Suche 14).
4. Mantelhandel: Bewertung des Reinvermögens (stille Reserven, Goodwill, latente Steuern), Mindestbemessung auf dem Nennwert aller bestehenden Beteiligungsrechte – kein Praxis- oder ILE-Text.
5. Abs. 3: Bewertungsmethoden für die Emissionsabgabe (Praktikermethode, DCF, Minderheitsabzug) – nur Analogie (KS 28 SSK für die Vermögenssteuer; Brozzo/Stocker); ESTV verlangt «Bewertungsgutachten» (Checkliste).
6. Genussscheine ohne Nennwert (Mindestbemessung) und Genossenschaftsanteile – nur KS 32a Ziff. 4.2.4 b) (3 Franken je Titel bei unentgeltlicher Ausgabe).
7. Satzgeschichte (frühere Sätze, Senkung auf 1 %) – kein ILE-Beitrag.

## 6. Zählerstand

- Lexplorer-Suchen: **15** (search_chunks_hybrid 13, search_chunks_keyword 2; find_leading_cases 0).
- Open Case Law: 8 search_practice, 5 get_practice.
- Lesezugriffe Lexplorer (get_chunk_content, get_document_slice, nav_*): ca. 50, nicht gezählt.
