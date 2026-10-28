# Entscheidregister Art. 17d DBG

Stand: 28.10.2026 (unbeaufsichtigter Lauf Claude-Cloud). Zitierstrings aus Open Case Law (`zitat_de` im Cache bzw. `citation_string_de`).

## Suchwege

| Nr. | Weg | Abfrage | Treffer | Ergebnis |
|---|---|---|---|---|
| 1 | `pipeline/entscheide.py DBG/art-17d` | Phrasensuche Entscheidsuche, Volltexte OCL | 1 | 9C_86/2021 |
| 2 | OCL `search_decisions`, court bger, compact, limit 200 | `"Art. 17d DBG" OR "art. 17d LIFD" OR "Art. 7f StHG" OR "art. 7f LHID"` | 800 (unscharf) | darunter 9C_86/2021, 9C_13/2025; Rest Fehltreffer der Artikelsuche |
| 3 | Entscheidsuche CH_BGer/CH_BGE ab 2011 | `"17d DBG" OR "17d LIFD" OR "7f StHG" OR "7f LHID" OR "17d al" OR "Art. 17d" OR "art. 17d"` | 11 | einschlägig 9C_86/2021, 9C_13/2025, 2C_285/2019 (Normkette); Fehltreffer Art. 17d TSV, EnV, ELV/OPC-AVS/AI (6B_590/2024, 1C_7/2022, 8C_354/2025, 9C_334/2023, BGE 142 II 517, 8C_12/2024, 8C_463/2024, 1C_526/2015) |
| 4 | Entscheidsuche CH_BGer/CH_BGE | `("imposition proportionnelle" OR "anteilsmässige Besteuerung" OR …) AND (Mitarbeiteroptionen OR options …)` | 1 | 9C_13/2025 |
| 5 | Entscheidsuche alle Gerichte ab 2012 | `"17d DBG" OR "17d LIFD" OR "7f StHG" OR "7f LHID" OR "imposition proportionnelle" OR "anteilsmässige Besteuerung"` | 13 | kantonal: TAPI GE A/3151/2023, A/720/2025; VGer ZH SB.2011.00013; SVG ZH AB.2019.00007; StRK ZH DB.2015.72; VGer ZH SB.2019.00059 (Normkette) |
| 6 | Entscheidsuche alle ab 2013 | `("§ 17d StG" OR "Art. 97a DBG" OR "art. 97a LIFD" OR "pro rata temporis" OR "Vestingperiode" …) AND (Mitarbeiteroptionen …)` | 34 | neu BGer 2C_397/2015 (altes Recht, Vesting-Begriff); übrige Zivil/ALV ohne Bezug |
| 7 | Nachtrag in den Cache | `entscheide.py DBG/art-17d --nachtragen 9C_13/2025 2C_397/2015 2C_285/2019` | 3 | Cache jetzt 4 Entscheide |
| 8 | Hilfsagent kantonale Gerichte (Entscheidsuche, 15 Suchen) | siehe Kantonale_Entscheide.md | – | – |

`find_leading_cases` nicht verwendet (bei 2 einschlägigen BGer-Entscheiden ohne Erkenntnisgewinn; spart Kontingent). Kein BGE zu Art. 17d DBG.

## Register

| Entscheid | Datum | Besetzung | Normstelle | Sachfrage | Kernaussage (ein Satz) | E. | Ergebnis | Klasse | Fassung |
|---|---|---|---|---|---|---|---|---|---|
| BGer 9C_13/2025 vom 1. Mai 2025 | 01.05.2025 | Dreier (Moser-Szeless) | Art. 17d, 97a Abs. 1, 17a, 17b Abs. 3 DBG; Art. 7f StHG; Art. 15 DBA CH-ES | Referenzperiode bei Austritt; RSU; DBA | Das Ende der Vestingperiode ist Tatfrage; nach dem Austritt liegende Zeit zählt nicht; RSU werden wie Optionen behandelt; abweichende Zähler/Nenner des Ansässigkeitsstaats sind eine «factual issue» und verpflichten die Schweiz nicht zum Verzicht. | 7, 9.1.1 f., 9.2.1 f., 9.3, 10.2–10.4, 11 | Abweisung | A | geltend (SP 2020) |
| BGer 9C_86/2021 vom 14. Juni 2021 | 14.06.2021 | – | Art. 17d DBG/Art. 7f StHG via Art. 7 lit. cbis AHVV | AHV auf ausgeübten Optionen nach Wegzug | Für Mitarbeiterbeteiligungen gelten im AHV-Recht für Zeitpunkt und Bewertung die DBG-Vorschriften; Art. 17d DBG wird wiedergegeben. | 3.2, 5.1 | Abweisung | B | geltend |
| BGer 2C_397/2015 vom 26. Januar 2016 | 26.01.2016 | – | Art. 17 DBG (altes Recht), Rundschreiben ESTV 6.5.2003 | Begriff der Vestingperiode | Bis zum Ablauf der Vestingperiode ist der Rechtserwerb aufschiebend bedingt (Wiedergabe des Rundschreibens); neues Recht ratione temporis nicht anwendbar (Art. 72m StHG). | 3.1, 3.2 | – | B | altes Recht |
| BGer 2C_285/2019 vom 9. März 2020 | 09.03.2020 | Dreier | Art. 17a–17d LIFD (Normkette) | – | Kantonale Bestimmungen gleich Art. 17a–17d LIFD. | 11 | – | C | geltend |

Kantonale Gerichte: siehe Kantonale_Entscheide.md (TAPI GE A/3151/2023 vom 24.6.2024; CJ GE ATA/1365/2024 vom 19.11.2024, nicht im Index, nur über 9C_13/2025; TAPI GE A/720/2025 vom 8.12.2025; SVG ZH AB.2019.00007 vom 2.12.2020; VGer ZH SB.2011.00013 vom 15.2.2012; StRK ZH DB.2015.72 vom 11.8.2015).
