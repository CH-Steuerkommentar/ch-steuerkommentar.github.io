# Französische Fassung einer Kommentierung

Die französische Fassung ist eine Übersetzung der deutschen Kommentierung, keine eigene Kommentierung.

- Quelle: `kommentare/<Erlass>/art-<N>.md` (kanonisch, deutsch)
- Ziel: `kommentare_fr/<Erlass>/art-<N>.md`
- Keine neue Recherche, keine inhaltlichen Änderungen, nichts weglassen, nichts hinzufügen. Jede Randnote, jede Fussnote, jedes Label `{rn:label}` und jeder Querverweis `{{N:label}}` bleibt erhalten (gleiche Labels, gleiche Reihenfolge).

## Regeln

- **Frontmatter:** `erlass` und `artikel` unverändert; `sprache: fr`; `titel`: offizielle französische Sachüberschrift (Fedlex); `stand`: gleiches Datum wie das Original; `fassung`: «version du …».
- **Normtext** (`>`-Zeilen): offizieller französischer Wortlaut von Fedlex (Werkzeug Fedlex `get_article`, Sprache fr), gleiche Gliederung; erste Zeile «**Art. N <titre officiel>**».
- **Kapitel:** erstes Kapitel `# Aperçu`; «Zu Art. 4 Abs. 1 VStG» → «Art. 4, al. 1, LIA»; Verzeichnisse `# Bibliographie`, `# Matériaux` (Unterkapitel übersetzen: Bund → Confédération, Verwaltungspraxis → Pratique administrative).
- **Erlasse:** DBG → LIFD, StHG → LHID, VStG → LIA, VStV → OIA, MWSTG → LTVA, MWSTV → OTVA, StG → LT, StV → OT, KAG → LPCC, OR → CO, ZGB → CC, IPRG → LDIP, BV → Cst., DBA → CDI, FusG → LFus, BGG → LTF, VwVG → PA. Zitierweise «art. 4, al. 1, let. b, LIA»; «Ziff.» → «ch.».
- **Entscheide:** französische Zitierung nur aus Open Case Law (`citation_string_fr` bzw. Werkzeug `cite`), z. B. «ATF 140 II 88 consid. 4.1», «arrêt 2C_123/2016 du 21 novembre 2017 consid. 3», «arrêt du TAF A-5361/2013 du 17 décembre 2015 consid. 3.5.3». Kantonale Entscheide sinngemäss («arrêt du TC VS …»). Nie eine Zitierung erfinden; findet sich keine, die deutsche Zitierung übernehmen. Zusätze in Klammern übersetzen.
- **Verwaltungspraxis:** offizielle französische Titel (Circulaire n° 24 AFC, Notice, Info TVA, Circulaire CSI); Ziffern unverändert.
- **Materialien:** «Message LIA 1963, p. …» mit französischen Seitenzahlen nur, wenn über Open Case Law oder Fedlex nachgeprüft; sonst deutsche Fundstelle mit «(version allemande)».
- **Lehre** (FStR, IFF, Seminarunterlagen, Onlinekommentar): Autor, Titel und Fundstelle unverändert deutsch, Links unverändert. «(Seminarunterlage)» → «(support de séminaire)».
- **Terminologie** der französischsprachigen Praxis, z. B. geldwerte Leistung = prestation appréciable en argent; verdeckte Gewinnausschüttung = distribution dissimulée de bénéfice; Kapitaleinlagereserven = réserves issues d'apports de capital; Steuerumgehung = évasion fiscale; Bundesverwaltungsgericht = Tribunal administratif fédéral (TAF); ESTV = AFC; SSK = CSI; Randnote = N.
- **Neutral** wie das Original: kein «à notre avis», «nous», «à juste titre», «convaincant», «préférable», «il convient», «devrait», «sans doute».
- **Typographie:** « … » mit geschütztem Leerzeichen, Gedankenstrich «–», kein «ß».

## Prüfen

`python3 pipeline/kommentar.py kommentare_fr/<Erlass>/art-<N>.md` ohne Befund; Randnoten- und Fussnotenzahl gleich wie `python3 pipeline/kommentar.py kommentare/<Erlass>/art-<N>.md`. Stichprobe von fünf Entscheidzitaten mit `cite` gegenprüfen.
