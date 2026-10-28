# Prüfbericht Art. 3 StHG – 28.10.2026

Unbeaufsichtigter Lauf (Claude-Cloud, geplante Aufgabe). Skill: steuerkommentar-selbstaendig (Fassung im Repository). Ergebnis: kommentare/StHG/art-3.md, 56 Randnoten, 169 Fussnoten; `pipeline/kommentar.py` ohne Befund.

## Ablauf
1. Norm erfasst (Fedlex, Fassung 1.1.2025; künftige konsolidierte Fassungen 2028/2029 ohne Änderung von Art. 3).
2. Entscheid-Cache `pipeline/entscheide.py StHG/art-3`: 216 Treffer; Triage durch drei Hilfsagenten (medium) → Register mit 196 Einträgen (A 25, B 115, C 58), 9 Fehltreffer; Gegenprobe zu 24 BGE (2 nachgetragen: BGE 131 I 145, BGE 132 I 29). Problemkarte, Gliederungsnotiz.
3. Recherche je Sachfrage durch drei Hilfsagenten (high): kantonale Gerichte (Entscheidsuche), Praxis (Lexplorer Tax navigiert; Open Case Law), ILE-Literatur, Materialien (Fedlex, Open Case Law), Onlinekommentar (Art. 13 StHG, Art. 10 DBG; zu Art. 3 StHG selbst gibt es keine OK-Kommentierung).
4. Text in der Hauptsitzung; Kürzungs- und Neutralitätsdurchgang.
5. Fundstellenprüfung: vier Hilfsagenten (high), alle 164 Fussnoten der Erstfassung einzeln, keine Stichproben (Fundstellenliste_Teil1–4.md).
6. Schlussprüfung: zwei Hilfsagenten (medium) nach den Prüfpunkten von `pruefung` (Schlusspruefung_TeilA.md, _TeilB.md); Befunde in der Hauptsitzung behoben.

## Entscheide im unbeaufsichtigten Lauf (vermerkt)
- **Lexplorer-Tageslimite:** Während der Recherche wurde die Tageslimite für Lesen/Navigieren in Lexplorer Tax erreicht. Die Fundstellenprüfung der Lexplorer-Quellen (ILE-Literatur, Steuerbücher, SSK, ESTV/SSK-Dossier, Medienmitteilung) erfolgte deshalb gegen die wörtlichen, mit Chunk-/Doc-ID erfassten Auszüge der Recherche und gegen die bereits geprüfte Fundstellenliste zu Art. 3 DBG («bestätigt (Rechercheauszug)»). Quellen ohne Auszug wurden gestrichen (Berdoz/Bugnon; Tessiner Zuteilung bei Unterhaltsbeiträgen). Eine Nachprüfung am Chunk ist bei der nächsten Nachführung sinnvoll.
- **Individualbesteuerung:** Der Wortlaut der beschlossenen StHG-Änderung (BBl 2025 2033) war in keinem Tool greifbar; der Ausblick gibt deshalb den Entwurf des Bundesrates (BBl 2024 591) als Entwurf wieder. Annahme in der Volksabstimmung vom 8.3.2026 und Inkrafttreten 1.1.2032 sind über FStR 2026/3 (Gesetzgebungs-Agenda) und die Medienmitteilung des Bundesrates vom 19.8.2026 belegt.
- **Botschaft 1983:** nur OCR-Schnipsel; S. 21 und 86 f. sind durch BGE 141 II 318 bzw. BGE 150 II 244 bestätigt, S. 288 f. (Entwurfstext) über die OCR-Seitenzählung.
- **Kantonale Erlassdaten:** Für StG/LU, StG/VS und StG/ZH war das Erlassdatum in keinem Tool belegt; zitiert mit systematischer Nummer ohne Datum. StG/BE (21.5.2000) und LI/VD (4.7.2000) aus BGE 150 II 244 bzw. BGer 9C_448/2025.
- **Kurzzitate der Lehre:** wie in den übrigen Kommentierungen des Projekts (z.B. DBG/art-3) mit Fundort, Titel und Ziffer bzw. Randziffer; Seitenzahlen der FStR-Beiträge waren ohne Lexplorer nicht ermittelbar.
- **BGE 151 II 154:** BGer 9C_47/2024 ist teilweise publiziert (E. 3–6); E. 8 und 9.1 (Kantonssteuern) werden nach dem Urteil mit Hinweis «in BGE 151 II 154 nicht publiziert» zitiert.

## Befunde der Fundstellenprüfung und Erledigung (Auszug)
- Pinpoints korrigiert: 2C_183/2007 (E. 3.2), 2C_303/2007 (E. 4), 2C_646/2007, 2C_911/2018, 2P.165/2006, 2C_505/2015, 2C_323/2021, BGE 132 I 29 und 2C_301/2017 (E. 4.3), 2C_73/2018, 9C_702/2024, 9C_229/2023, BGE 141 II 318 (E. 2.2), 9C_249/2023, 2C_952/2020, 2P.2/2003 (E. 2.5), 2C_753/2020 (E. 1.2.1), 2C_897/2018 (E. 2.2.2–2.5), VGer ZH SB.2019.00028.
- Zusätze: Fünferbesetzung bei 2C_662/2010, 2C_704/2019, 2C_354/2022; Publikationshinweise (2C_662/2010 nicht publ. in BGE 137 II 246; 9C_47/2024).
- Aussagen angepasst: BGE 125 I 458 (1999, vor vollem Wirksamwerden des StHG); 2C_533/2018 gestrichen (trug die Aussage nicht); Luzerner alternierender Wohnsitz ohne hälftige Teilung; Gemeindelegitimation (Art. 73 Abs. 2 StHG); OK-Grieder/Hongler Art. 13 StHG nur mit «vgl.»; Oesterhelt zur analogen Anwendung vollständig wiedergegeben; GR-Renovationsbeispiel als hypothetisch gekennzeichnet; VRK SG als obiter.
- Verzeichnisse: KS 1 SSK mit vollem Titel und amtlicher URL; Grieder/Hongler/Lorenz mit Untertitel und Seiten; Hongler/Eggel «S. 34 ff.»; Botschaft Individualbesteuerung ohne unbelegtes Datum.

## Befunde der Schlussprüfung und Erledigung
- Aufbau: Überschriften unter der Schwelle zusammengelegt (Abs. 2: «Wohnsitzbegriff», «Lebensmittelpunkt …», «Wohnsitzwechsel»; Abs. 3: «Ehegatten mit Wohnsitz in verschiedenen Kantonen oder im Ausland», «Kinder unter elterlicher Sorge und Grundstückgewinne»).
- Widersprüche behoben: «mindestens 30 Tage»; Art. 11 Abs. 1 StHG nur Tarif; Luzerner Fortdauerregel nur international; Gemeindeautonomie vs. interkommunale Freiheit; «ersetzen»/«ändern» vereinheitlicht; E-StHG 1983/2024 unterschieden.
- Rang kenntlich gemacht (Bundesgericht, kantonale Gerichte), Belegreihenfolge in Fussnoten (BGE – BGer chronologisch – kantonal – Praxis – Lehre), Erstnennungen ergänzt (BGG, RHG, Individualbesteuerungsgesetz), Datumsformate im Fliesstext ausgeschrieben, Gerichtsabkürzungen in Fussnoten vereinheitlicht, Jargon «ILE-Literatur» im Text ersetzt.
- Nicht übernommen: Umstellung aller Lehre-Kurzzitate auf Seitenzitate (Seiten nicht ermittelbar, Projektstil); Ersatz der Lexplorer-Links durch amtliche Links (nur wo belegt, KS 1 SSK).

## Offene Fragen, die der Text als offen ausweist
Alternierender Wohnsitz unter dem StHG; Pflicht der Kantone zur getrennten Besteuerung der Grundstückgewinne der Ehegatten; kantonale Autonomie beim Umfang der Steuerpflicht; Aufenthalt neben Wohnsitz in einem anderen Kanton; Tessiner Besteuerung des unselbständigen Erwerbseinkommens Minderjähriger; Mindestdauer der tatsächlichen Trennung in der Praxis.

## Zahlen
Randnoten 56; Fussnoten 169; Entscheide im Register 198 (A 25); ILE-Fundstellen 33 (13 Werke); OK-Fundstellen 2; Lexplorer-Suchen 14 (Budget 25).
