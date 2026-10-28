# Art. 6 MWSTG – Lexplorer-Fundstellen (ILE-Literatur) und Verwaltungspraxis ESTV

Stand: 28.10.2026, 07:10–07:40 UTC. Lexplorer Tax (Kanton CH) und Open Case Law (OCL, `search_practice`/`get_practice`, Quelle `estv_mwst`). Keine Websuche. Lexplorer nicht für Rechtsprechung verwendet.

## WICHTIGER VORBEHALT: Leselimite von Lexplorer Tax erreicht

Beim ersten Navigations- bzw. Leseaufruf (`nav_find`, danach `get_chunk_content` für `3afdba28-…`) meldete Lexplorer Tax: «Tageslimite für das Lesen und Navigieren erreicht (2000 Aufrufe, Fair Use). Ab 00:00 UTC wieder verfügbar.» Die Suchwerkzeuge (`search_chunks_*`) funktionierten weiterhin, liefern aber nur eine **Vorschau mit den ersten rund 300 Zeichen** eines Chunks (ohne Autorzeile, sofern der Chunk länger ist).

Folge:
- **Kein Treffer konnte in dieser Sitzung ganz gelesen werden.** Die unten mit «Vorschau» gekennzeichneten Zitate sind wörtlich, brechen aber dort ab, wo die Vorschau endet («[…]»). Erst wenn nach 00:00 UTC jeder Chunk mit `get_chunk_content` gelesen ist, sind diese Stellen voll verwendbar.
- Wörtliche Sätze mit der Kennzeichnung **«(art-1)»** stammen aus `/home/claude/ch-steuerkommentar.github.io/arbeit/MWSTG/art-1/01_Recherche/Lexplorer_Fundstellen.md`. Dort wurden sie in einer früheren Sitzung ganz gelesen; heute konnten sie nicht erneut am Chunk geprüft werden.
- Autor:innen: Wo die Vorschau die Autorzeile nicht zeigt, stammt die Angabe aus art-1 (dort am Chunk-Ende abgelesen) oder fehlt und ist als «am Chunk-Ende prüfen» markiert.
- Die Verwaltungspraxis (Aufgabe A) war davon nicht betroffen: Sie wurde über OCL im Volltext gelesen.

---

## 1. Suchprotokoll

### 1.1 Lexplorer Tax – gezählte Suchen (Teilbudget 18; verbraucht 11)

| Nr. | Werkzeug (limit) | Abfrage | Filter | Ergebnis |
|---|---|---|---|---|
| 1 | search_chunks_hybrid (10) | `Art. 6 MWSTG Überwälzung der Steuer richtet sich nach privatrechtlichen Vereinbarungen Privatautonomie keine Überwälzungspflicht` | CH; Kat. 08 | FStR 2024/1 Clavadetscher/Lorenz (Abschn. 2.3, 3.2.1.1, 3.2.3.1, Klausel 6); Handbuch Rz. 158 f.; Seminar 2023 «Überwälzung der MWST»; Seminar 2015 (Kocher); FStR 2019/3 (Bodemann); Seminar 2019 (Clavadetscher). Sehr ergiebig |
| 2 | search_chunks_keyword (20) | `Zivilgerichte` | CH; Kat. 08 | **Handbuch Sachregister «Zivilgericht 125, 159, 1645, 1785»**; Handbuch 5. Teil Ziff. 8 Rz. 1785; Seminar 2015 (Billag); Seminar 2023; übrige Treffer ohne MWST-Bezug (AIAG, Verrechnungssteuer-Regress, Stiftungen) |
| 3 | search_chunks_keyword (15) | `Nachverrechnung` | CH; source ESTV MWST-Publikationen `03033b33-…` | MI 16 «Beispiel 1» und «Beispiel 2» (Chunks 0048/0049); Ziffer nicht in der Vorschau |
| 4 | search_chunks_hybrid (12) | `Rückforderung zu Unrecht überwälzter Mehrwertsteuer Leistungsempfänger ungerechtfertigte Bereicherung Art. 27 Abs. 2 MWSTG Rechnungskorrektur` | CH; Kat. 08 | FStR 2024/1 Rz. 94; Seminar 2023 Fall 7 (Rückforderungsanspruch, Varianten A/C); Seminar 2018 Fall 3 (Rückforderung gegenüber ESTV); FStR 2019/3. Ergiebig |
| 5 | search_chunks_hybrid (12) | `MWST-Klausel Vertrag Preis zuzüglich MWST inklusive MWST Auslegung nachträgliche Überwälzung nach MWST-Kontrolle Nachbelastung Steuersatzänderung` | CH; Kat. 08 | FStR 2024/1 Klauselkatalog Nr. 5–7; Seminar 2023 Teil «Privatrechtliche Ausgestaltung» (Varianten a–h, Prüfschritte, Empfehlungen). Sehr ergiebig |
| 6 | search_chunks_hybrid (12) | `öffentlich-rechtliches Leistungsverhältnis Gemeinwesen Gebühren Überwälzung der Mehrwertsteuer nach öffentlichem Recht Verfügung Billag BGE 140 II 80` | CH; Kat. 08 | Seminar 2015 (Kocher) BGE 140 II 80, vier Folien; Seminar 2024 Nichtentgelte Fall 12 (BGE 141 II 182); Seminar 2016 Fall 5 (2C_882/2014); Seminare 2016/2020 Gemeinwesen (hoheitliche Gebühren; nur am Rand) |
| 7 | search_chunks_keyword (15) | `144 II 412` | CH; Kat. 08 | Handbuch 4. Teil I–II Rechtsprechungsübersicht; **FStR 2024/1 Ziff. 3.2.1.3 «Ergänzendes Steuerobjekt»**; übrige Treffer nicht einschlägig |
| 8 | search_chunks_keyword (15) | `2C_936/2013` | CH; Kat. 08 | nur Seminar 2015 (Inhaltsverzeichnis, Folie Sachverhalt) |
| 9 | search_chunks_keyword (20) | `140 II 80` | CH; Kat. 08 | FStR 2024/1 Abschn. 1, 2.2, 2.3; Handbuch Rechtsprechungsübersicht d) Überwälzbarkeit, Rz. 165; Seminar 2019; FStR 2022/2 (nur Erhebungskonzeption) |
| 10 | search_chunks_keyword (15) | `Billag Überwälzung` | CH; source IFF Forum für Steuerrecht `fdd29b9d-…` | nur FStR 2024/1 Abschn. 1 → **keine Besprechung von BGE 140 II 80 in einer FStR-Rubrik «Rechtsprechung 2014» gefunden** |
| 11 | search_chunks_hybrid (10) | `Abrechnungsverhältnis Überwälzungsverhältnis Leistungsempfänger Rückforderung Mehrwertsteuer ohne Leistungsverhältnis Verjährung Bundesgericht` | CH; source FStR | FStR 2019/3 (Bodemann; Vergütung versagt mangels Leistungsverhältnis; zivilrechtliche Aspekte); FStR 2024/1 Rz. 94; übrige nicht einschlägig |
**Verbraucht: 11 von 18.** 7 Suchen bleiben für einen zweiten Durchgang nach 00:00 UTC (dann zuerst die Chunks unten lesen und navigieren; das zählt nicht).

Nicht gezählte, gescheiterte Aufrufe: `nav_find` («Überwälzung», CH, document) und `get_chunk_content` (`3afdba28-39b3-419d-bf85-4837ff95d615`) – beide mit Fehlermeldung «Tageslimite für das Lesen und Navigieren erreicht».

### 1.2 Open Case Law – Verwaltungspraxis (nicht zum Lexplorer-Budget)

| Nr. | Werkzeug | Abfrage / doc_id | Filter | Ergebnis |
|---|---|---|---|---|
| P1 | search_practice | `"Art. 6 MWSTG" OR Zivilgericht OR Zivilgerichte OR "privatrechtlich"` | estv_mwst, de | MI 17, MI 18, MBI 06, MI 09 (Art. 6), MI 02, MBI 01, MBI 12 (nur «privatrechtlich organisiert») |
| P2 | search_practice | `Überwälzung OR überwälzt OR überwälzen OR "nachträglich"` | estv_mwst, de | 25 Dokumente; einschlägig MI 16, MI 09, MI 17, MBI 19 |
| P3 | get_practice | `estv_mwst_de_1002536` (MI 16) | – | Volltext gelesen (gespeichert und durchsucht) |
| P4 | get_practice | `estv_mwst_de_1014743` (MI 09) | – | Volltext durchsucht |
| P5 | get_practice | `estv_mwst_de_1001226` (MI 18) | – | Volltext gelesen |
| P6 | get_practice | `estv_mwst_de_1004106` (MBI 06) | – | Volltext gelesen |
| P7 | search_practice | `Preisbekanntgabe OR Preisanschrift OR Preisanschriften OR Preisangabe OR "PBV"` | estv_mwst, de | nur MBI 06 (sowie Abkürzungsverzeichnisse) |
| P8 | search_practice | `Praxismitteilung OR "30. Januar 2004" OR "2A.326/2002"` | estv_mwst, alle Sprachen | **0 Treffer** |
| P9 | search_practice | `Überwälzung OR "privatrechtlichen Vereinbarungen" OR "nicht auf die Steuer hinweisen"` | estv_mwst, include_superseded | 12 Dokumente; keine ältere oder aufgehobene Praxismitteilung |
| P10 | get_practice | `estv_mwst_de_1004706` (MBI 19) | – | Volltext durchsucht |
| P11 | search_practice | `"ausgewiesene Steuer gleich geschuldete Steuer" OR "impôt facturé" OR "nicht auf die Steuer hinweisen" OR "unberechtigter Steuerausweis"` | estv_mwst | MI 16, MBI 01, MBI 05 fr, MBI 27 fr |
| P12 | search_practice | `(Einschätzungsmitteilung OR Kontrolle OR Nachbelastung OR rückwirkend) NEAR(Rechnung Mehrwertsteuer, 30)` | estv_mwst, de | 0 |
| P13 | search_practice | `Nachverrechnung OR "nachträglich in Rechnung" OR "nachträglichen Überwälzung" OR "nachträglicher Überwälzung"` | estv_mwst | nur MI 16 |
| P14 | get_practice | `estv_mwst_de_1003204` (MI 17) | – | Volltext gelesen |
| P15 | search_practice | `"auf die MWST hingewiesen" OR "Hinweis auf die MWST" OR "keinen Hinweis auf die MWST" OR "Steuerhinweis"` | estv_mwst, de | 17 Dokumente (Hinweisverbote in Sonderfällen: Meldeverfahren, Gruppe, Wertgutscheine, Ausland usw.) |

---

## 2. Verwendbare ILE-Fundstellen (Kategorie 08-institut-fuer-law-und-economics)

Zitierweise des Handbuchs (wie Art. 1–5): **Honauer/Probst/Rohner/Frey, Handbuch zum Mehrwertsteuergesetz (MWSTG), 4. Aufl., Bern 2024 (IFF-Schriftenreihe)**; Lexplorer-Titel «Schriftenreihe (2024) · <Teil>»; Autorzeile am Chunk-Ende: «Philip Frey, Niklaus Honauer, Simeon L. Probst, Tobias F. Rohner».
Hauptaufsatz: **Clavadetscher Diego/Lorenz Tabea, Überwälzung der Mehrwertsteuer, FStR 2024/1** (doc `d29b067f-51fc-487b-8571-62f9138bd44e`, 41 Chunks laut art-1; mit Randziffern, z.B. «94»). Er ist der einschlägigste ILE-Text zu Art. 6 MWSTG und sollte nach 00:00 UTC ganz gelesen werden (`nav_list_chunks` auf die doc_id).

### Sachfrage 1 – Privatautonomie, keine Überwälzungspflicht, Grundsatz der Überwälzbarkeit (Art. 1 Abs. 3 Bst. c MWSTG)

**L-1 Clavadetscher/Lorenz, FStR 2024/1, Ziff. 2.3 «Steuerüberwälzung mittels privatrechtlicher Vereinbarung»**
- Chunk `3afdba28-39b3-419d-bf85-4837ff95d615`; https://app.lexplorer.ch/suche?e_chunks=13371&e_sys=ile
- Autor:innen: Diego Clavadetscher, Tabea Lorenz (art-1).
- Vorschau wörtlich: «Gemäss Art. 6 Abs. 1 MWSTG richtet sich die Überwälzung der Mehrwertsteuer nach «privatrechtlichen Vereinbarungen» und ist damit hoh[…]»
- (art-1) wörtlich: «Dabei bezieht sich die Überwälzung in dieser Bestimmung auf die ‹wirtschaftliche› Überwälzung und damit auf die Frage, wer die Mehrwertsteuer trägt. Dies ist – anders als die ‹Überwälzbarkeit› – eine Frage des Privatrechts.» Nach art-1 ferner: Art. 6 Abs. 1 neu seit 2010, Abs. 2 entspricht Art. 37 Abs. 6 aMWSTG.
- Rz./Fn.: im Chunk nicht sichtbar; am Original prüfen.

**L-2 Clavadetscher/Lorenz, FStR 2024/1, Ziff. 2.2 «Grundsatz der Überwälzbarkeit»**
- Chunk `87092e1a-6de4-46ba-a7df-4d45df12d8d3`; https://app.lexplorer.ch/suche?e_chunks=13370&e_sys=ile
- Vorschau wörtlich: «Die Erhebung der Mehrwertsteuer soll gemäss Art. 1 Abs. 3 Bst. c MWSTG u. a. unter Berücksichtigung des Grundsatzes der Überwälzbarkeit erfolgen. So sorgt erst[…]»
- (art-1) wörtlich: «Beim Grundsatz der Überwälzbarkeit handelt es sich um einen mehrwertsteuerlichen, d.h. öffentlich-rechtlichen Grundsatz. Allerdings stellt er lediglich eine Leitlinie für den Gesetzgeber und die Verwaltung dar, wobei weder der Leistungserbringer oder -empfänger noch die Verwaltung daraus irgendwelche Rechte ableiten können.» – «Ob die Überwälzung tatsächlich gelingt, ist somit keine Frage des Mehrwertsteuerrechts, sondern einzig eine Frage des Privatrechts bzw. der Marktverhältnisse».

**L-3 Clavadetscher/Lorenz, FStR 2024/1, Ziff. 3.2.1.1 «Allgemeines» (Steuerrechtsverhältnis und Vertragsinhalt)**
- Chunk `a5739c90-3b2c-4416-8594-a13c4e6aca09`; https://app.lexplorer.ch/suche?e_chunks=13379&e_sys=ile
- Vorschau wörtlich: «Wie nachfolgend aufgezeigt wird, nimmt das Steuerrechtsverhältnis hinsichtlich der Bemessungsgrundlage keine Rücksicht auf den Inhalt des Vertrages bzw. den darin vereinbarten Preis, s[…]»
- Sachfrage 1 und 4 (Trennung Steuerrechtsverhältnis / Vertrag).

**L-4 Clavadetscher/Lorenz, FStR 2024/1, Ziff. 3.2.3.1 «Wirtschaftliche Überwälzung der Mehrwertsteuer»**
- Chunk `13a84d9d-9e87-4e1b-8e94-a7d70c4e3d1b`; https://app.lexplorer.ch/suche?e_chunks=13385&e_sys=ile
- Vorschau wörtlich: «Mehrwertsteuerpflichtige Leistungsverhältnisse beruhen meist auf einem privatrechtlichen Rechtsverhältnis (Kaufvertrag, Auftrag, Mietvert[…]»

**L-5 Honauer/Probst/Rohner/Frey, Handbuch MWSTG, 1. Teil IV, Rz. 126, 157–159 (Überwälzbarkeit)**
- Rz. 158 f.: Chunk `5022b8ab-e1e6-4da3-9fcd-53909d4e4a09`; https://app.lexplorer.ch/suche?e_chunks=21061&e_sys=ile – Vorschau wörtlich: «Die Überwälzbarkeit ist ein systemtragendes Grundprinzip der Mehrwertsteuer. ${ }^{309}$ Der Grundsatz der Überwälzbarkeit der Mehrwertsteuer auf die Kunden stellt wie das Bestimmungsla[…]» (Fn. 309). (art-1) wörtlich: «Grundsätzlich fällt demzufolge die Frage der Überwälzung der Steuer in den Bereich der Privatautonomie.» Zur Rechtsprechung, die keinen «allgemeinen verfassungsmässigen Grundsatz der Überwälzbarkeit der Mehrwertsteuer» anerkennt: «Diese Auffassung ist fraglich, […]» (Lehrmeinung).
- Rz. 157 (art-1): «Entsprechend verlangt der Grundsatz der Überwälzbarkeit eine Ausgestaltung der Mehrwertsteuer, die die Überwälzung nicht erschwert, sondern erleichtert.» – Chunk `5d5a9fb4-4b3d-4351-ae25-b972f74eefd3`; https://app.lexplorer.ch/suche?e_chunks=21059&e_sys=ile
- Rz. 126 (art-1): «Dabei ist zu beachten, dass nach dem geltenden MWSTG keine Pflicht zur Steuerüberwälzung besteht. Auch ein Anspruch auf Überwälzung lässt sich aus der Gesetzgebung nicht ableiten.» – Chunk `6839dc5d-91ee-4836-98a1-9bf8e09ac99e`; https://app.lexplorer.ch/suche?e_chunks=21031&e_sys=ile
- Rz. 160 f. (art-1; Art. 92 MWSTG als «Ventil», Erlass erst nach erfolglosem Zivilrechtsweg) – Chunk `e3079d3e-8bab-4b0e-a557-2ff746406af4`; https://app.lexplorer.ch/suche?e_chunks=21062&e_sys=ile
- Rz. 165 (Rechtsnatur der Prinzipien), Treffer Nr. 9: Chunk `89bce832-284c-43a1-9ab7-081355f2a0cf`; https://app.lexplorer.ch/suche?e_chunks=21067&e_sys=ile – Vorschau: «165 Die Prinzipien, die der gesetzlichen Ausgestaltung zugrunde lagen und die das Mehrwertsteuergesetz in Art. 1 Abs. 1 und […]»

**L-6 Honauer/Probst/Rohner/Frey, Handbuch MWSTG, 5. Teil V–IX, Ziff. 8 «Überwälzbarkeit der MWST», Rz. 1785**
- Chunk `5c7c42a9-677b-4736-b431-2798e1d05c60`; https://app.lexplorer.ch/suche?e_chunks=21382&e_sys=ile (doc `33e81a4d-60b1-4339-adc1-a55d8fa4f18e`)
- Vorschau wörtlich: «1785 Die Überwälzung der Steuer ${ }^{1765}$ richtet sich gemäss Art. 6 MWSTG nach privatrechtlichen Vereinbarungen. Zur Beurteilung von Streitigkei[…]» (Fn. 1765).
- Sachfrage 1 und 2. **Einzige Handbuch-Stelle, die Art. 6 MWSTG unmittelbar kommentiert**; vorrangig ganz lesen (inkl. Folgechunks von Ziff. 8).

**L-7 St.Galler Seminar zur Mehrwertsteuer 2023, «Überwälzung der Mehrwertsteuer» (doc `b95c2050-29f9-4f39-bd1b-8dd284186da5`)**
- Referent:innen: in der Vorschau nicht sichtbar; laut art-1-Protokoll Clavadetscher/Lorenz – am Chunk-Ende prüfen.
- Folie «2. Mehrwertsteuerliche Bestimmungen (I/III) – MWSTG 6 «Steuerüberwälzung»»: Chunk `6674a8a6-8c74-4502-9ddf-b5157255570f`; https://app.lexplorer.ch/suche?e_chunks=53033&e_sys=ile
- Folie «1. Mehrwertsteuerliche Dogmatik (I/II)»: Chunk `534f2881-3219-411f-b038-3d4def4a7553`; https://app.lexplorer.ch/suche?e_chunks=53031&e_sys=ile – Vorschau: «- Netto-Allphasensystem mit Vorsteuerabzug (MWSTG 1 I) - Grundsatz der Überwälzbarkeit (MWSTG 1 […]»
- Folie «Ebene 1: Steuerrechtsverhältnis»: Chunk `2d000053-8cdc-4204-8432-030d146d543b`; https://app.lexplorer.ch/suche?e_chunks=53041&e_sys=ile – Vorschau: «- MWSTG 24 I: Bemessungsgrundlage ist das «tatsächlich empfangene Entgelt[…]»

**L-8 Clavadetscher, St.Galler Seminar zur Mehrwertsteuer 2019, «Zum Verhältnis von Mehrwertsteuer- und Privatrecht», III.A «Grundsätze zur Überwälzung»**
- Chunk `ae464629-d5e0-470c-ad74-9b8e8cdfdf72`; https://app.lexplorer.ch/suche?e_chunks=55927&e_sys=ile
- Referent: Diego Clavadetscher (art-1 für dasselbe Seminar, L-28/L-36) – am Chunk-Ende prüfen.
- Vorschau wörtlich: «III.A. Grundsätze zur Überwälzung – Allgemeine Prinzipien – vgl. Blum/Müller, Seminar Expert suisse 5.12.2018 – Grundsatz der Überwälzbarkeit (M[…]»
- (art-1, Chunk `55b2eced-45c4-40b4-a541-63bf53af9aa4`): «indirekte Erhebung → Steuerpflicht beim Leistungserbringer → trägt Risiko der Nicht-Überwälzung».

### Sachfrage 2 – Zivilgerichte, Rechtsweg, Billag-Rechtsprechung (BGE 140 II 80), BGE 144 II 412

**L-9 Kocher, St.Galler Seminar zur Mehrwertsteuer 2015, «Entwicklungen in der Rechtsprechung», Ziff. 1 «Überwälzung der MWST; Rechtsweg bei Streitigkeiten» (BGE 140 II 80 = 2C_936/2013)** (doc `1678d6d6-808d-40da-b29b-a43d87cf5d9f`)
- Referent: Martin Kocher (art-1).
- Sachverhalt: Chunk `a4f6e6b4-3459-44e4-b801-53678c0f1202`; https://app.lexplorer.ch/suche?e_chunks=63285&e_sys=ile – Vorschau: «- BGer, 2C_936/2013 vom 31. Januar 2014 = BGE 140 II 80 – Sachverhalt – Die Billag AG ist […]»
- Erwägungen: Chunk `66298915-be12-4756-9322-06570ea9f574`; https://app.lexplorer.ch/suche?e_chunks=63286&e_sys=ile – Vorschau: «- Das Verhältnis zwischen Billag AG und Kunde ist **öffentlichrechtlicher** Natur – Art. 6[…]». (art-1) wörtlich: «Damit regelt der Gesetzgeber die zivilrechtlichen Leistungsverhältnisse, nicht aber Konstellationen, die auf öffentlichem Recht beruhen» – «Die MWST ist aber ein blosses Akzessorium der Hauptforderung – Die Gabelung kann nicht gewollt sein». Nach art-1 nennt die Folie irrtümlich «Art. 6 Abs. 1» statt Abs. 2.
- «Überwälzung im privatrechtlichen Verhältnis»: Chunk `309f8180-e780-4025-935f-3441e68f8037`; https://app.lexplorer.ch/suche?e_chunks=63287&e_sys=ile – Vorschau: «- Ob die MWST übe[…]»
- Fazit: Chunk `9d4fcb8f-6db3-4ae9-865e-086064235825`; https://app.lexplorer.ch/suche?e_chunks=63288&e_sys=ile – Vorschau: «- Fazit: Die Billag AG hat, – wenn die Rechnung insgesamt nicht bezahlt wird oder – wenn nu[…]»
- Sachfrage 2 und 5.

**L-10 Clavadetscher/Lorenz, FStR 2024/1, Ziff. 1 (Einführung), Fn. 4**
- Chunk `a26b404c-7253-4708-a59e-46c0812f5081`; https://app.lexplorer.ch/suche?e_chunks=13368&e_sys=ile
- (art-1) Fn. 4 wörtlich: «So hat das Bundesgericht im sog. ‹Billag-Urteil› festgehalten, dass sich die Überwälzung diesfalls – entgegen dem Wortlaut von Art. 6 MWSTG – nach dem öffentlichen Recht richtet und allfällige Streitigkeiten hinsichtlich der Steuerüberwälzung verfügungsweise zu regeln sind (vgl. BGE 140 II 80, E. 2.5).»
- Sachfrage 2 und 5.

**L-11 Bodemann, FStR 2019/3, «Aus der Rechtsprechung zur Mehrwertsteuer in den Jahren 2018, 2019»** (doc `d9636380-d56d-4276-bfab-1c167eac93e9`; Urteilsbesprechung = Lehre)
- Autorin: Clara Bodemann (art-1) – am Chunk-Ende prüfen.
- «Zivilrechtliche Aspekte der Mehrwertsteuerüberwälzung»: Chunk `215c51f0-b679-4fde-8c2d-82211a3220d1`; https://app.lexplorer.ch/suche?e_chunks=30760&e_sys=ile – (art-1) wörtlich: «Ob das Einzelunternehmen B. den Kostenfaktor Mehrwertsteuer berechtigterweise auf die Beschwerdeführerin hätte überwälzen können, bleibt unbestrittenermassen iSv Art. 6 MWSTG eine zivilrechtliche Frage und ist weder ein Problem der Überwälzbarkeit noch ein solches der Vergütung der Inlandsteuer. Das Bundesgericht folgt damit seiner bereits unter dem aMWSTG entwickelten Rechtsprechung, dass sich aus dem Grundsatz der Überwälzbarkeit kein Anspruch des Steuerpflichtigen gegenüber dem Gemeinwesen auf Überwälzung der Steuer ableiten lässt.»
- «Entscheidung des Bundesgerichts zur Mehrwertsteuervergütung»: Chunk `d986bcd4-a4a5-4571-808c-8f9b1f376238`; https://app.lexplorer.ch/suche?e_chunks=30758&e_sys=ile – Vorschau: «Das Bundesgericht versagt vorliegend die Vergütung der inländischen Mehrwertsteuer, da diese im Grundsatz nicht geschuldet gewesen wäre (mangels Leistungsve[…]»
- Würdigung: Chunk `12f166c5-e4a8-476d-ae90-b6e3b2185460`; https://app.lexplorer.ch/suche?e_chunks=30762&e_sys=ile – Vorschau: «Mit dem vorliegenden Urteil konnte sich das Bundesgericht vertieft mit den Fragen sowohl der Leistungszuordnung als auch der Vergütung der […]»
- Der besprochene Entscheid wird in den Vorschauen nicht genannt. Ob es BGE 144 II 412 oder ein anderes Urteil (art-1 vermutete 2C_767/2018) ist, ist am Original und über OCL zu klären. Hier wird keine Zuordnung behauptet.
- Sachfrage 2 und 3.

**L-12 Handbuch MWSTG – Wegweiser (nur zur Orientierung, nicht als Beleg)**
- Sachregister: «Zivilgericht 125, 159, 1645, 1785» – Chunk `24900249-519a-4594-9dd9-1fccba249a3d`; https://app.lexplorer.ch/suche?e_chunks=22374&e_sys=ile. Rz. 125/159 = L-5, Rz. 1785 = L-6; **Rz. 1645** steht im Chunk «Steuerbefreiung für Inlandlieferungen an Touristen zur Ausfuhr» (`ec595bbf-5523-48d2-b2ab-4ccf50a7a790`; https://app.lexplorer.ch/suche?e_chunks=21269&e_sys=ile) und ist noch zu lesen.
- Rechtsprechungsübersicht 1. Teil, d) Überwälzbarkeit (BGE 140 II 80; BGE 123 II 385; 2C_426/2008 und 2C_432/2008; 2C_518/2007 und 2C_519/2007; 2C_382/2007 …): Chunk `a7e3497f-a6c5-4f4d-ba3c-f827281b7e03`; https://app.lexplorer.ch/suche?e_chunks=21018&e_sys=ile. Nach art-1 ist die Zuordnung Entscheid ↔ Leitsatz in diesen Tabellen teils verschoben (OCR).
- Rechtsprechungsübersicht 4. Teil I–II: Vorschau «| BGE 144 II 412 | Fehlt ein Leistungsverhältnis, wird aber dennoch Mehrwertsteuer und Rechnung gestellt und bezahlt, ist diese[…]» – Chunk `97883eb5-37ca-4aa3-b7eb-6a3488e5e95a`; https://app.lexplorer.ch/suche?e_chunks=21056&e_sys=ile. Nur als Wegweiser: Rechtsprechung wird über OCL zitiert.

**Ergebnis zu Sachfrage 2:** Eine Urteilsbesprechung von BGE 140 II 80 in einer FStR-Rubrik «Rechtsprechung 2014» war mit den Suchen Nr. 8–10 nicht auffindbar. Zu BGE 144 II 412 kommt allenfalls FStR 2019/3 (L-11) in Frage, was noch zu klären ist.

### Sachfrage 3 – Rückforderung zu Unrecht überwälzter Steuer, Art. 27 MWSTG

**L-13 Clavadetscher/Lorenz, FStR 2024/1, Ziff. 3.2.1.3 «Ergänzendes Steuerobjekt»**
- Chunk `4a02d803-c965-4490-b4be-22f6194f6276`; https://app.lexplorer.ch/suche?e_chunks=13381&e_sys=ile (Treffer der Suche «144 II 412»)
- Vorschau wörtlich: «Eine Mehrwertsteuerschuld kann auch durch einen unberechtigten oder unrichtigen Steuerausweis in einer Rechnung entstehen, selbst wenn kein steuerbares Leistun[…]»

**L-14 Clavadetscher/Lorenz, FStR 2024/1, Rz. 94 «Vertragliche Rückforderungsansprüche und Preisanpassungen»**
- Chunk `03b2b217-375a-463c-9315-114aca5d21a5`; https://app.lexplorer.ch/suche?e_chunks=13392&e_sys=ile
- Vorschau wörtlich: «94 Die Frage des vertraglichen Rückforderungsanspruchs muss u. E. kongruent mit der ersten Frage (a) beurteilt werden. So besteht ein vertraglicher Rückforderungsanspruch seitens des Leistungse[…]» (Lehrmeinung, «u. E.»)
- Sachfrage 3 und 4.

**L-15 St.Galler Seminar zur Mehrwertsteuer 2023, «Überwälzung der Mehrwertsteuer», Fall 7 (Beratungsvertrag – Rückforderungsanspruch)**
- Variante A: Chunk `d112ab11-37a2-48ea-9680-18e0e76ce4f3`; https://app.lexplorer.ch/suche?e_chunks=53081&e_sys=ile – Vorschau: «Frage 2, Variante A- Beratungsvertrag enthält folgende Vertragsklausel: «Soweit die Leistungserbringerin die MWST zu entrichten hat, erhöht si[…]»
- Variante C: Chunk `b1ebfbf2-ad79-417c-ac8b-e4b2d3e02a34`; https://app.lexplorer.ch/suche?e_chunks=53083&e_sys=ile – Vorschau: «- Beratungsvertrag enthält folgende Vertragsklausel: «Das Honorar schliesst die MWST ein.» – Lösungsskizze – Rechtsg[…]»
- Referent:innen: am Chunk-Ende prüfen. Sachfrage 3 und 4.

**L-16 St.Galler Seminar zur Mehrwertsteuer 2018, «Verfahrens- und Strafrecht», Fall 3 «Rückforderung zu Unrecht bezahlter Mehrwertsteuer» (nur am Rand)**
- Chunk `6816c866-591b-493e-a44e-8e67fd1e7c5f`; https://app.lexplorer.ch/suche?e_chunks=64887&e_sys=ile – Vorschau: «Lösungsansätze Frage 1 – Recht auf Rückerstattung besteht – Art. 88 Abs. 3 MWSTG[…]»; ferner `af4c1939-…` (64886), `3750bc0c-…` (64885).
- Betrifft die Rückforderung durch die steuerpflichtige Person gegenüber der ESTV (Korrekturabrechnungen 2010/2011, Verjährung), nicht das Überwälzungsverhältnis. Nur verwenden, wenn die Abgrenzung Abrechnungs- / Überwälzungsverhältnis dargestellt wird. Referent:innen: am Chunk-Ende prüfen.

### Sachfrage 4 – Vertragsklauseln/MWST-Klauseln, Preis inkl./exkl. MWST, nachträgliche Überwälzung

**L-17 Clavadetscher/Lorenz, FStR 2024/1, Klauselkatalog (Ziff. 3.x, Nr. 5–7)**
- Nr. 5: Chunk `7e4d866a-8b8d-4eb6-bf8e-2d63f36c49da`; https://app.lexplorer.ch/suche?e_chunks=13398&e_sys=ile – Vorschau wörtlich: «5. «Der Preis beträgt CHF X zzgl. 8,1 \% MWST.» Auslegung LORENZ ${ }^{99}$ a) Keine nachträgliche Preisanpassung möglich, wenn sich am Steuerrechtsverhältnis etwas ändert, da die Auslegung des Wortlauts d[…]» (Fn. 99; Auslegung nach Lorenz)
- Nr. 6: Chunk `ecc76174-cf8f-42f2-a85e-3c149b83734a`; https://app.lexplorer.ch/suche?e_chunks=13400&e_sys=ile – Vorschau wörtlich: «6. «Der Preis beträgt CHF X zzgl. MWST zum jeweils gesetzlich geschuldeten Satz, aktuell ausmachend CHF Y.» a) Nachträgliche Preisanpassung möglich, wenn sich am Steuerrechtsverhältnis etwas ändert, da d[…]»
- Nr. 7: Chunk `135f7cd2-b495-4476-9de9-e2d6d9d336a6`; https://app.lexplorer.ch/suche?e_chunks=13401&e_sys=ile – Vorschau wörtlich: «7. «Der Preis beträgt CHF X zzgl. der im massgeblichen Zeitpunkt vom Leistungserbringer geschuldeten Mehrwertsteuer. Der Leistungserbringer ist berechtigt, Wahlrechte, die ihm das Mehrwertsteuerech[…]»
- Nach 00:00 UTC auch die Nr. 1–4 (vorangehende Chunks, ca. 13394–13397) lesen. Diese Stelle ist zentral für «nachträgliche Überwälzung nach Kontrolle/Nachbelastung».

**L-18 St.Galler Seminar zur Mehrwertsteuer 2023, «Überwälzung der Mehrwertsteuer», Teil «Privatrechtliche Ausgestaltung»**
- Prüfschritte bei unklaren Preisvereinbarungen: Chunk `05154426-e6fc-4314-9f54-6b18992ec64b`; https://app.lexplorer.ch/suche?e_chunks=53050&e_sys=ile – Vorschau: «1. Prüfschritt: Ist überhaupt ein Vertrag zustande gekommen? 2. Prüfschritt: Was ist der Inhalt der Preisvereinbarung? – Vertragsauslegung – Vertragsergänzung – Vertrags[…]»
- Vertragsauslegung (Beispiel Kaufpreis «CHF 60'000»): `abd133d2-eba1-469d-822b-a5652aac57a0` (53044); Vertragsabschluss (OR 1 I): `a496353a-2b15-4220-9926-fdc586a9982d` (53045)
- Varianten a–h: `a9864c88-a86b-4050-9e99-238b81bbd0f6` (53063; Vorschau: «a. «Der Preis beträgt CHF 107,70.» b. «De[…]»), `7e9d1e15-4f01-441e-b7a4-bb3af2bbc0b8` (53064; «e. «Der Preis beträgt CHF 100,00 zzgl. 7,7 % MWST.»»), `7750d937-9778-4c7b-a297-6f527c79a7e7` (53065; «g. «Der Preis beträgt CHF 100,00 zzgl. der im massgeblichen Zeitpunkt vom Leistungserbri[…]»), `dff1cf93-142f-4839-b5de-e65cd3adaf41` (53066; «h. «Der Preis beträgt CHF 100,00 zzgl. 7,7[…]»)
- Theoretische Erkenntnisse: `1dc38fe9-4415-4d86-985d-b827fede13ea` (53068) – Vorschau: «- Vertragsklauseln können unterschiedlich verstanden werden → den Willen ausführlich[…]»
- Praktische Empfehlungen: `a14b6a7f-23a0-4e83-adb7-306ff8fdfebf` (53069) – Vorschau: «4. Praktische Empfehlungen für Vertragsgestaltung – klarstellen, ob ein fixer oder ein variabler (anpassbarer) Preis vereinbart […]»
- Links jeweils https://app.lexplorer.ch/suche?e_chunks=<Nr.>&e_sys=ile. Referent:innen: am Chunk-Ende prüfen.

Lücke: Eine ILE-Stelle eigens zur **nachträglichen Überwälzung nach einer MWST-Kontrolle oder Nachbelastung** wurde in den Vorschauen nicht gefunden. In Frage kommen L-17 (Nr. 5/6: «nachträgliche Preisanpassung») und L-14. Das ist nach dem Lesen zu prüfen.

### Sachfrage 5 – Öffentlich-rechtliche Leistungsverhältnisse/Gemeinwesen

- **L-10** (Clavadetscher/Lorenz Fn. 4) und **L-9** (Kocher, Seminar 2015) sind die tragenden Stellen.
- **L-19 Baumgartner/Imstepf, St.Galler Seminar zur Mehrwertsteuer 2024, «Nichtentgelte», V. (Öffentliche) Abgaben, Fall 12 Billag-Gebühren (BGE 141 II 182)** – Chunks `1e2cc7dd-0e39-47ff-9440-6579b81a3263` (50693), `f5377afa-d787-4bf0-9957-a0cab7eb8686` (50694; Vorschau: «- Vorbemerkung: Inkasso durch Dritte – Direkte Stellvertretung des BAKOM – Zentrale Erwägungen BGer[…]»), `f2d077bd-74f1-4b6f-b79a-a539bf6c8279` (50691). Referenten laut Folienfuss «Baumgartner/Imstepf». Betrifft die Entgeltqualifikation der Empfangsgebühr, nicht die Überwälzung. Nur am Rand.
- **L-20 St.Galler Seminar zur Mehrwertsteuer 2016, «Entwicklungen in der Rechtsprechung», Fall 5 Billag (2C_882/2014)** – Chunk `016e57bf-e3e9-46fa-9947-a312e1af0557` (62389; Vorschau: «- Billag AG stellte Rechnung mit MWST – Art. 12 Ab[…]»), `6d6017d6-522b-47d9-80f1-3efe86962831` (62390). Nur am Rand (Folgeverfahren zu BGE 140 II 80 im Sinne einer Steuerbarkeitsfrage). Referent: am Chunk-Ende prüfen.
- Nicht einschlägig (nur hoheitliche Gebühren / Art. 18 Abs. 2 Bst. l): Seminar 2016 Gemeinwesen (`18eb6e73-…`), Seminar 2020 Abfallentsorgung (`54e86f26-…`).

---

## 3. Verwaltungspraxis ESTV

Allgemeiner Befund: Die ESTV-Publikationen enthalten **keine eigene Erläuterung von Art. 6 MWSTG**. Sie nennen die Norm an fünf Stellen beiläufig, und zwar in zwei Formeln:
1. Die Durchsetzung (Rechnungsanspruch, Überwälzungsstreit) ist «nicht Sache der ESTV» und gehört «i. d. R.» vor die Zivilgerichte: MI 09, MI 17, MI 18, MBI 06.
2. «Die Überwälzung der Mehrwertsteuer auf den Kunden richtet sich nach privatrechtlichen Vereinbarungen (Art. 6 Abs. 1 MWSTG)», bei der nachträglichen Überwälzung: MI 16.

Eine ausdrückliche Aussage, dass **keine Überwälzungspflicht** besteht, oder zum **Grundsatz der Überwälzbarkeit (Art. 1 Abs. 3 Bst. c)** fehlt in der ESTV-Praxis (OCL-Volltextsuchen P1, P2, P9). Die Grenze «ausgewiesene Steuer = geschuldete Steuer» (Art. 27) ist in MI 16 und in mehreren Branchen-Infos ausgeführt.

OCL-«Stand» = Datumsfeld in OCL. Der Volltext enthält zum Teil spätere Praxisanpassungen (z.B. MI 16 mit Publikationsdatum 05.01.2024, Steuersätze 2024).

**P-1 MWST-Info 16 Buchführung und Rechnungsstellung** – OCL `estv_mwst_de_1002536` (Stand OCL 2021-02-01); Lexplorer doc `0a010f4d-9c80-4380-872d-50bc0fe9f983`
- *Nachträgliche Rechnungskorrektur / nachträgliche Überwälzung* (Abschnitt unmittelbar nach Ziff. 2.5; die Ziffer ist weder im OCL-Text noch in der Lexplorer-Vorschau ausgewiesen, vermutlich eine eigene Unterziffer nach 2.5, am Original prüfen). Lexplorer: «Beispiel 1» Chunk `94569e49-553f-433a-bac1-d1b79ac5b3b7` (https://mcp-tax.lexplorer.ch/s/doc/0a010f4d-9c80-4380-872d-50bc0fe9f983?chunk=94569e49-553f-433a-bac1-d1b79ac5b3b7), «Beispiel 2» Chunk `dd894ab8-76ed-4077-8f18-6e5625e7f2b0` (https://mcp-tax.lexplorer.ch/s/doc/0a010f4d-9c80-4380-872d-50bc0fe9f983?chunk=dd894ab8-76ed-4077-8f18-6e5625e7f2b0).
  - Wörtlich: «Die nachträgliche Korrektur einer früher ausgestellten Rechnung kann in den folgenden Fällen innerhalb des handelsrechtlich Zulässigen durch ein zusätzliches empfangsbedürftiges Dokument erfolgen, wenn dieses auf die ursprüngliche Rechnung verweist, diese widerruft oder ergänzt: 1. Bei nachträglicher Überwälzung von nicht in Rechnung gestellter Mehrwertsteuer; 2. bei nachträglicher Korrektur eines auf der Rechnung ausgewiesenen und zu tiefen Mehrwertsteuersatzes; 3. bei Entgeltsänderungen.»
  - Beispiel 1 (rückwirkende Eintragung per 1.1.2022): «Ihrer Kundin, die Schreinerei Müller AG, ist mit der «Nachverrechnung» der Mehrwertsteuer einverstanden. Somit kann die Beratungs GmbH die Mehrwertsteuer nachträglich in Rechnung stellen. Die Überwälzung der Mehrwertsteuer auf den Kunden richtet sich nach privatrechtlichen Vereinbarungen ( Art. 6 Abs. 1 MWSTG ). Erfolgt eine «Nachverrechnung» der Mehrwertsteuer, ist zwingend auf die ursprüngliche Rechnung hinzuweisen.» Ferner: Die Leistungsempfängerin kann den Vorsteuerabzug in der Periode der Rechnungskorrektur geltend machen, «sofern sie zum damaligen Zeitpunkt des Leistungsbezuges hierfür berechtigt gewesen wäre».
  - Beispiel 2 (zu tiefer Steuersatz, gastgewerbliche Leistung): gleiche Formel «richtet sich nach privatrechtlichen Vereinbarungen ( Art. 6 Abs. 1 MWSTG )»; «Erfolgt eine «Nachverrechnung» der zu tief in Rechnung gestellten Mehrwertsteuer, ist zwingend auf die ursprünglich ausgestellte Rechnung hinzuweisen.»
  - Beispiel 3 (Entgeltsminderung um 50 %): «Nach dem Grundsatz «ausgewiesene Steuer gleich geschuldete Steuer» ist die auf der ursprünglichen Rechnung ausgewiesene Mehrwertsteuer geschuldet, da der Leistungsempfänger grundsätzlich im Rahmen seiner zum Vorsteuerabzug berechtigenden Tätigkeit den Vorsteuerabzug geltend machen kann. Daher ist eine Rechnungskorrektur notwendig, um den korrekten Ausweis der Mehrwertsteuer sicherzustellen.» Gekennzeichnet als «Praxispräzisierung».
  - Sachfragen: nachträgliche Überwälzung nach Kontrolle/Nachbelastung, Rechnungskorrektur, Privatautonomie. **Wichtigste Praxisstelle zu Art. 6 Abs. 1.**
- *Ziff. 2.5 Unrichtiger oder unberechtigter Steuerausweis (Art. 27 MWSTG)* (Ziffer laut Querverweis im Text «Folgen eines unrichtigen oder unberechtigten Steuerausweises: Ziff. 2.5»; Lexplorer-Chunk `f2bbf1b3-5864-44a7-b514-b3168ff6d794` laut art-1, https://mcp-tax.lexplorer.ch/s/doc/0a010f4d-9c80-4380-872d-50bc0fe9f983?chunk=f2bbf1b3-5864-44a7-b514-b3168ff6d794)
  - Wörtlich: «Wer nicht im Register der steuerpflichtigen Personen eingetragen ist oder wer das Meldeverfahren nach Artikel 38 MWSTG anwendet, darf in Rechnungen nicht auf die Steuer hinweisen. Wer in einer Rechnung eine Steuer ausweist, obwohl er zu deren Ausweis nicht berechtigt ist, oder wer für eine Leistung eine zu hohe Steuer ausweist, schuldet die ausgewiesene Steuer, es sei denn: Es erfolgt eine Korrektur der Rechnung […]; oder der Leistungserbringer macht glaubhaft, dass dem Bund kein Steuerausfall entstanden ist. Dem Bund entsteht namentlich dann kein Steuerausfall, wenn der Rechnungsempfänger keinen Vorsteuerabzug vorgenommen hat oder die geltend gemachte Vorsteuer dem Bund zurückerstattet worden ist.»
  - Sachfragen: Hinweisverbot für Nicht-Eingetragene, «impôt facturé = impôt dû» als Grenze.
- *Ziff. 2.1 bis 2.4 (Rechnungsbegriff, Form und Inhalt; Ziffern laut Querverweisen «Ziff. 2.1», «Ziffer 2.4.4»)*
  - Rechnungsmuster mit Ausweis «8,1 % MWST» und mit «blosser Angabe des Steuersatzes»: «CHF 5'940.00 inkl. 8,1 % MWST». Sachfrage: Preisangabe inkl./exkl. MWST, Steuerausweis.
  - Wörtlich: «Bei der Übertragung eines Gesamt- oder Teilvermögens mit Meldeverfahren (Art. 38 MWSTG) darf in Rechnungen ( Ziff. 2.1 ) nicht auf die MWST hingewiesen werden.» – «Bei Anwendung der Gruppenbesteuerung dürfen gruppeninterne Transaktionen (Belege) keinen Hinweis auf die MWST tragen.»
  - Ziff. 2.2 (art-1, Chunk `3260db98-4160-48c3-b148-ce5fa13c5c03`): «Der Leistungserbringer hat dem Leistungsempfänger auf Verlangen eine Rechnung auszustellen […] (Art. 26 MWSTG).»

**P-2 MWST-Info 09 Vorsteuerabzug** – OCL `estv_mwst_de_1014743` (Stand OCL 2025-11-03); Ziffer im OCL-Text nicht ausgewiesen (Abschnitt Nachweis/Rechnung, Art. 26 MWSTG) – am Original oder über Lexplorer bestimmen
- Wörtlich: «Der Leistungserbringer hat dem Leistungsempfänger auf Verlangen eine Rechnung auszustellen ( Art. 26 Abs. 1 MWSTG ). Die Durchsetzung dieses Anspruchs ist nicht Sache der ESTV, sondern i. d. R. zivilrechtlicher Natur ( Art. 6 MWSTG ).»
- Wörtlich (Ausschluss des Vorsteuerabzugs): «Der Leistungsempfänger muss nicht prüfen, ob die MWST zu Recht eingefordert wurde. Weiss er aber, dass die Person, die die MWST überwälzt hat, nicht als steuerpflichtige Person eingetragen ist, so ist der Vorsteuerabzug ausgeschlossen ( Art. 59 Abs. 2 MWSTV ).»
- Sachfragen: Zivilgerichte; Hinweis auf die Steuer durch Nicht-Steuerpflichtige.

**P-3 MWST-Info 17 Leistungen an diplomatische Vertretungen und internationale Organisationen** – OCL `estv_mwst_de_1003204` (Stand OCL 2021-01-12); Lexplorer-Chunk Ziff. 4.8 `258c1b58-f940-4bac-8963-73386258d17e` (art-1), https://mcp-tax.lexplorer.ch/s/doc/e42295ee-4d93-4e5c-bdf4-bb7fb9dadb62?chunk=258c1b58-f940-4bac-8963-73386258d17e
- Ziff. 4.8 «Ausweis der MWST» (Ziffer laut art-1), wörtlich: «Hat der Leistungserbringer die Lieferung oder Dienstleistung versteuert und die MWST offen ausgewiesen, kann er nachträglich keine Steuerbefreiung mehr geltend machen. […] Die Beurteilung von Streitigkeiten über die Überwälzung (Fakturierung) der MWST durch den steuerpflichtigen Leistungserbringer an den institutionellen Begünstigen oder an die begünstigte Person fällt auch im Falle der rechtzeitigen Übergabe einer gültigen Bescheinigung nicht in die Zuständigkeit der ESTV, sondern in der Regel in jene der Zivilgerichte ( Art. 6 MWSTG ).»
- Ziff. 5 (laut Querverweis «Vorgehen bei der steuerpflichtigen Person, siehe Ziffer 5»), Bst. d, wörtlich: «Sollte in der Rechnung der Vermerk «inkl. MWST» (mit oder ohne Steuersatz) aufgedruckt sein, ist dieser von der steuerpflichtigen Person sowohl auf dem Original als auch auf sämtlichen Kopien durchzustreichen. Wird dies unterlassen, ist die MWST zu entrichten, auch wenn das amtliche Formular vollständig ausgefüllt vorliegt».
- Sachfragen: Zivilgerichte; Steuerausweis / Art. 27.

**P-4 MWST-Info 18 Vergütungsverfahren** – OCL `estv_mwst_de_1001226` (Stand OCL 2021-01-12); Ziffer im OCL-Text nicht ausgewiesen (Abschnitt zu Art. 153 Abs. 1 MWSTV, Höchstbetrag der Vergütung)
- Wörtlich: «Bezahlte Mehrwertsteuer auf Leistungen, die nach dem MWSTG nicht der Mehrwertsteuer unterliegen oder davon befreit sind, wird nicht vergütet ( Art. 153 Abs. 1 MWSTV ). Zur Beurteilung von Streitigkeiten über die Steuerüberwälzung ist nicht die ESTV zuständig. Dies obliegt i. d. R. den Zivilgerichten ( Art. 6 MWSTG ).» – Beispiele 1/2: «Eine Korrektur bzw. Rückerstattung der Steuer kann nur über den Leistungserbringer vorgenommen werden.»
- Sachfragen: Zivilgerichte; Rückforderung zu Unrecht überwälzter Steuer (nur beim Leistungserbringer). Vgl. die Konstellation von BGE 144 II 412 (über OCL prüfen).

**P-5 MWST-Branchen-Info 06 Detailhandel** – OCL `estv_mwst_de_1004106` (Stand OCL 2021-01-12); Ziffern im OCL-Text grossteils nicht ausgewiesen
- Rechnungsstellung, wörtlich: «Der Leistungsempfänger kann vom Leistungserbringer (Lieferant) verlangen, dass dieser ihm eine Rechnung ausstellt, die den Anforderungen von Artikel 26 Absatz 2 und 3 MWSTG genügt. Zur Beurteilung von Streitigkeiten über die Steuerüberwälzung ist nicht die ESTV zuständig. Dies obliegt i. d. R. den Zivilgerichten ( Art. 6 MWSTG ).»
- Preisangaben, wörtlich: «Sowohl bei Preisanschriften in Schaufenstern, Inseraten usw. als auch auf Preisetiketten an den Gegenständen oder Verkaufsregalen sind gemäss PBV gegenüber dem Konsumenten immer die tatsächlich zu bezahlenden Beträge in Schweizerfranken (inkl. MWST) bekannt zu geben.» **Einzige Praxisstelle zur Preisangabe inkl. MWST (PBV).**
- Kassenzettel: «Die auf den Kassenzetteln und -coupons ausgewiesene MWST ist geschuldet ( Art. 27 MWSTG ).»
- Bons (Ziff. 1.14.1.1–1.14.1.3 laut Text «Beispiel für Ziffern 1.14.1.1–1.14.1.3»): «Erfolgt der Hinweis auf die MWST auf einem höheren als dem bezahlten Betrag (z. B. vor der Anrechnung eines Bons), so ist die ausgewiesene Steuer geschuldet ( Art 27 Abs. 2 MWSTG ).»
- Stellvertretung: «Dem Käufer abgegebene Belege (Rechnungen, Kassenbelege usw.) dürfen keinen Steuerhinweis des Vertreters (Detailhändler) tragen; ansonsten ist gemäss Artikel 27 MWSTG die ausgewiesene Steuer zu entrichten.»
- Sachfragen: Zivilgerichte; Preisangaben inkl./exkl.; Art. 27.

**P-6 MWST-Branchen-Info 19 Gemeinwesen** – OCL `estv_mwst_de_1004706` (Stand OCL 2021-01-12)
- **Keine Aussage zu Art. 6 MWSTG**, zur Billag-Rechtsprechung oder zur Überwälzung in öffentlich-rechtlichen Leistungsverhältnissen (Volltextsuche nach «Art. 6 MWSTG», «Zivilgericht», «Überwälzung»).
- Akontorechnungen (Ziff. E.1.4 mit Beispielen E.1.4.1–E.1.4.4 laut Querverweisen), wörtlich: «Anlässlich der Schlussrechnung ist insbesondere darauf zu achten, dass die Mehrwertsteuer aufgrund der Akontorechnungen nicht doppelt bzw. nicht zu hoch ausgewiesen wird, da diese ansonsten vom jeweiligen Rechnungssteller gegenüber der ESTV geschuldet ist ( Art. 27 Abs. 2 MWSTG ).» Ausnahme: «Auf den Akontorechnungen darf in solchen Fällen nicht auf die MWST hingewiesen werden.»
- Umtriebsgebühren (Abschnitt Entsorgung, Verweis auf Ziff. H.1.1): «Ist dies nicht möglich bzw. wird die Steuer auf den gesamten Umtriebsgebühren ausgewiesen, ist diese auch geschuldet ( Art. 27 MWSTG ).»
- Kehrichtgebühren: «Im Zusammenhang mit der Überwälzung von Kehrichtgebühren (Entgelt für zum Normalsatz steuerbare Entsorgungsleistungen) sind verschiedene Konstellationen möglich.» (Ziffer nicht ausgewiesen)
- Sachfragen: Gemeinwesen; Art. 27. Für die Billag-Konstellation bleibt es bei der Rechtsprechung und der Lehre (L-9, L-10).

**P-7 Weitere Stellen (nur am Rand)**
- Hinweisverbote in Sonderfällen («keinen Hinweis auf die MWST»): MI 03 Gruppenbesteuerung (`estv_mwst_de_1005811`), MBI 10, MBI 12 (Wertgutscheine), MBI 23 (ausländischer Künstler), MBI 04, MI 07 u.a. (P15).
- Begriff «offene Überwälzung» im Zusammenhang mit der fiktiven Vorsteuer (Art. 28a MWSTG): MI 09, MBI 05, MBI 16, MBI 22, MBI 23; MI 04 (Ersteigerer). Für Art. 6 nur terminologisch.
- MI 01 ist laut art-1 (OCL `estv_mwst_de_1038520`) aufgehoben. MI 02 Steuerpflicht enthält zur Überwälzung nichts (nur «privatrechtlich … organisierte Unternehmensträger»).

**Praxismitteilung der ESTV vom 30. Januar 2004 (Botschaft BBl 2008 6885, 6943 f.)**
- **Über die zugelassenen Quellen nicht auffindbar.** OCL `search_practice` (estv_mwst, alle Sprachen, auch mit include_superseded) nach «Praxismitteilung», «30. Januar 2004» und «2A.326/2002»: 0 Treffer. Der OCL-Bestand `estv_mwst` umfasst nur MWST-Infos und MWST-Branchen-Infos zum MWSTG 2009.
- Die Lexplorer-Quelle «ESTV MWST-Publikationen» enthält laut Navigation in art-2 nur die geltenden MI 02–20, 22 und MBI 01–27. Eine Praxismitteilung von 2004 ist dort nicht zu erwarten. Wegen der Leselimite wurde dies heute nicht erneut navigiert und dafür kein Suchbudget eingesetzt.
- Für die Kommentierung daher nur über die Botschaft zitieren («Praxismitteilung der ESTV vom 30.1.2004», zit. in BBl 2008 6885, 6944), ohne eigenen Fundort.

---

## 4. Offene Punkte für einen zweiten Durchgang (nach 00:00 UTC; Navigation und Lesen sind budgetfrei)

1. `nav_list_chunks` auf FStR 2024/1 (doc `d29b067f-51fc-487b-8571-62f9138bd44e`) und alle 41 Chunks lesen. Insbesondere Ziff. 2.3, 3.2.1.3, Rz. 94 ff., den Klauselkatalog Nr. 1–7 und den Schluss. Dabei Randziffern und Fussnoten erfassen.
2. Handbuch Rz. 1785 ff. (Chunk `5c7c42a9-…` und Folgechunks; doc `33e81a4d-…`) sowie Rz. 1645 (`ec595bbf-…`) lesen.
3. Seminar 2023 «Überwälzung der Mehrwertsteuer» (doc `b95c2050-…`) und Seminar 2015 Ziff. 1 (doc `1678d6d6-…`) ganz lesen, um die Referent:innen am Chunk-Ende festzustellen.
4. FStR 2019/3 Bodemann (doc `d9636380-…`, Chunks 30758–30762): Klären, welcher Entscheid besprochen wird (BGE 144 II 412?).
5. Die Ziffern in MI 16 (Abschnitt Rechnungskorrektur), MI 09 und MBI 06 über die Kapitelstruktur der Lexplorer-Dokumente bestimmen (`nav_list_chunks` doc `0a010f4d-…` usw.).
