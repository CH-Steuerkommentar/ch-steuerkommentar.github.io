# Offener Steuerrechtskommentar

Kommentierungen zu DBG, StHG, VStG, MWSTG und Stempelabgabengesetz, erstellt mit dem Skill `steuerkommentar-selbstaendig`, veröffentlicht als freie Website.

Die Arbeit ist geteilt:

| Schritt | Werkzeug | bezahlt aus |
|---|---|---|
| 1. Artikelliste aus Fedlex | `pipeline/inventar.py` | – |
| 2. Entscheide suchen und Volltexte laden | `pipeline/entscheide.py` | – |
| 3. Jeden Entscheid einmal auswerten (Karteikarte) | `pipeline/karteikarten.py` (Batch API) | API-Guthaben |
| 4. Entscheidregister und Problemkarte je Artikel | `pipeline/register.py` | – |
| 5. Kommentierung schreiben | Skill `steuerkommentar-selbstaendig` | Max-Abo |
| 6. Fundstellen prüfen (Entscheide) | `pipeline/pruefung.py` (Batch API) | API-Guthaben |
| 7. Website erzeugen und veröffentlichen | `pipeline/md2site.py` + GitHub Actions | – |

Der teure Teil der bisherigen Arbeitsweise, das Lesen aller Entscheide im Volltext während des Schreibens, läuft damit über die Batch API (50 % Rabatt) und jeder Entscheid wird nur einmal gelesen, auch wenn er zehn Artikel zitiert. Das Abo trägt nur noch das Schreiben.

## Einrichten (einmal)

```bash
git clone <dein-repo> steuerkommentar && cd steuerkommentar
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

API-Key: Auf claude.ai unter Settings > Billing die Console-Organisation verknüpfen (dann kommen die monatlichen 100 USD dorthin), in der Console einen eigenen Workspace «Steuerkommentar» mit Ausgabenlimit anlegen, dort einen Key erzeugen und setzen:

```bash
cp .env.example .env      # dann in .env den Key eintragen (die Datei kommt nie ins Repo)
```

## Monatlicher Ablauf

Die API-Guthaben verfallen am Ende jedes Abrechnungszyklus. Deshalb am Monatsanfang die Batches für die nächsten Artikel laufen lassen.

```bash
python3 pipeline/inventar.py                      # nur bei Gesetzesänderungen nötig
python3 pipeline/entscheide.py --naechste 60      # Entscheide für die nächsten 60 Artikel
python3 pipeline/karteikarten.py vorbereiten --budget 40
python3 pipeline/karteikarten.py einreichen
python3 pipeline/karteikarten.py status           # nach einigen Minuten bis Stunden
python3 pipeline/karteikarten.py abholen
python3 pipeline/register.py --alle
python3 pipeline/stand.py naechster               # was als Nächstes geschrieben wird
```

Dann in Claude (Claude Code im Repo-Ordner oder claude.ai mit verbundenem Ordner): «Steuerkommentar selbständig zu Art. 26 DBG». Der Skill findet Register und Karteikarten in `arbeit/DBG/art-26/01_Recherche/` und schreibt nach `kommentare/DBG/art-26.md`.

Danach:

```bash
python3 pipeline/pruefung.py vorbereiten kommentare/DBG/art-26.md
python3 pipeline/karteikarten.py einreichen && python3 pipeline/karteikarten.py status
python3 pipeline/pruefung.py abholen              # → arbeit/DBG/art-26/Fundstellenliste_<Datum>.md
```

Die Befunde der Fundstellenliste behebt der Skill (oder du). Dann:

```bash
python3 pipeline/kommentar.py kommentare/DBG/art-26.md   # Format und Neutralität
python3 pipeline/stand.py setze DBG/art-26 veroeffentlicht
git add -A && git commit -m "Art. 26 DBG" && git push    # die Website baut sich selbst
```

## Kosten (Schätzung)

Gemessen am Probelauf für Art. 26 DBG: 117 Entscheide, rund 24'000 Zeichen je Entscheid. Die Karteikarten dafür kosten mit Sonnet 5.5 im Batch geschätzt 1.50 USD. Weil Entscheide oft mehrere Artikel zitieren, sinken die Kosten je Artikel, je mehr Artikel schon Karten haben. `karteikarten.py vorbereiten` zeigt vor jedem Batch die Schätzung; `stand.py` zeigt die tatsächlichen Kosten aus der Token-Zählung. Günstiger geht es mit `MODELL_KARTEN=claude-haiku-5-5` (für Klasse C reicht das; für A- und B-Karten erst an einem Artikel vergleichen).

## Grenzen der Automatik

- **Abdeckung:** `entscheide.py` sucht über entscheidsuche.ch. Open Case Law findet zu manchen Normen mehr Entscheide. Der Skill macht deshalb beim Schreiben die Gegenprobe (Liste, ohne Volltexte) und liest fehlende A-Entscheide selbst oder trägt sie mit `entscheide.py DBG/art-26 --nachtragen 2C_123/2020` nach.
- **Karteikarten sind Arbeitsmittel, keine Belege.** Jede Fundstelle im Text wird am Volltext geprüft (Schritt 6 und Skill).
- **Neutralität und Format** prüft `kommentar.py` maschinell; das ersetzt nicht die Schlussprüfung im Skill.

## Website

Die Website ist eine statische Seite (Astro mit Starlight), gebaut aus `kommentare/`. Sie hat Volltextsuche, eine Adresse je Randnote (`/dbg/art-26/#n12`), Fussnoten, Hell- und Dunkelmodus und läuft gratis auf GitHub Pages.

### Einmalig veröffentlichen

1. Auf github.com ein neues **öffentliches** Repository anlegen (z.B. `steuerkommentar`).
2. Diesen Ordner hineinladen: `git init && git add -A && git commit -m "Start" && git branch -M main && git remote add origin https://github.com/<name>/steuerkommentar.git && git push -u origin main`.
3. Im Repository unter **Settings > Pages** bei «Source» **GitHub Actions** wählen.
4. Unter **Actions** läuft «Website» an. Nach etwa zwei Minuten ist die Seite unter `https://<name>.github.io/steuerkommentar/` erreichbar.

Jeder Push mit einer neuen oder geänderten Kommentierung baut die Seite neu. Eine Kommentierung mit Befunden aus der Formatprüfung wird zurückgehalten; das Protokoll der Action zeigt, welche.

### Eigene Adresse (optional)

Eine Domain kaufen (z.B. `steuerkommentar.ch` bei einem Schweizer Registrar), unter Settings > Pages bei «Custom domain» eintragen und beim Registrar einen CNAME-Eintrag auf `<name>.github.io` setzen. HTTPS stellt GitHub selbst aus.

### Lokal ansehen

```bash
python3 pipeline/md2site.py
cd site && npm install && npm run dev        # http://localhost:4321
```

### Name und Aussehen

- Name des Werks und Kürzel im Zitiervorschlag: `WERK_NAME` und `WERK_KURZ` in `pipeline/config.py` (bzw. als Umgebungsvariablen) und `site/astro.config.mjs`.
- Darstellung von Randnoten, Normtext und Fussnoten: `site/src/styles/kommentar.css`.
- Seite «Über dieses Werk»: `site/src/content/docs/ueber.md`.

## Ordner

```
pipeline/            Skripte (siehe oben); config.py enthält Erlasse, Modelle, Preise
data/inventar/       Artikel je Erlass aus Fedlex
data/queue.json      Status je Artikel
data/zitate/         je Artikel die Entscheide, die ihn zitieren
data/karten/         Karteikarten je Entscheid (JSON)
data/entscheide/     Cache der Volltexte (nicht im Repo)
arbeit/              je Artikel: Register, Problemkarte, Karteikarten, Fundstellenliste, Prüfbericht
kommentare/          die Kommentierungen (Markdown, kanonisch)
site/                Website (Astro + Starlight)
docs/                Format der Kommentierungen und Beispiel
```

## Lizenz

Text der Kommentierungen: CC BY 4.0. Code: MIT.

## Automatik

Zwei Läufe schreiben Kommentierungen ohne Zutun und veröffentlichen sie. Damit nie zwei Läufe denselben Artikel bearbeiten, reserviert jeder Lauf seinen Artikel zuerst über `pipeline/reservierung.py`: Status `in_arbeit` in `data/queue.json`, Commit und Push. Git nimmt von zwei gleichzeitigen Pushes nur einen an; der andere nimmt den nächsten freien Artikel. Eine Reservierung, die älter als 12 Stunden ist, verfällt (abgestürzter Lauf). Die Website zeigt nur Kommentierungen mit Status `geprueft` oder `veroeffentlicht`.

### 1. GitHub Actions über das API-Guthaben (`Kommentar-Agent`)

Startet stündlich; läuft noch ein Lauf, wartet der nächste. Es schreibt also immer nur ein Lauf (`.github/workflows/kommentar-agent.yml`, Steuerskript `automation/lauf.py`):

1. fertige Batches abholen: Karteikarten → Register; Fundstellenprüfungen → Korrektur durch den Agent → Freigabe als `geprueft` (dann veröffentlicht die Website den Artikel);
2. Karteikarten für die nächsten Artikel per Batch erstellen (Sonnet 5.5), sobald weniger als drei Artikel `bereit` sind;
3. Artikel schreiben mit dem Skill `steuerkommentar-selbstaendig` (Agent SDK, Opus 5.5, Effort `high`), solange das Budget reicht; danach Fundstellen-Batch einreichen, Status `geschrieben`.

Budget: 30 USD pro Tag, 100 USD pro Monat, höchstens 15 USD pro Artikel (Zählung in `data/kosten/`). Unabhängig davon stoppt die Console bei ihrem Ausgabenlimit oder wenn das Guthaben aufgebraucht ist; der Lauf versucht es dann stündlich wieder. API-Preise hängen nicht von der Tageszeit ab.

Einrichten: Repository-Secret `ANTHROPIC_API_KEY` (Settings > Secrets and variables > Actions). Werte ändern über Variables: `TAGESBUDGET_USD`, `MONATSBUDGET_USD`, `BUDGET_JE_ARTIKEL_USD`, `MODELL_SCHREIBEN`, `EFFORT`.

Ein/aus: Actions > Kommentar-Agent > «…» > Disable workflow bzw. Enable workflow. Von Hand starten: Run workflow.

### 2. Geplante Aufgabe in der Claude-Cloud (Max-Abo)

Eine geplante Aufgabe auf claude.ai reserviert ebenfalls einen Artikel (zuerst `bereit`, sonst `offen`), schreibt ihn mit dem Skill, prüft alle Fundstellen selbst und pusht. Ein/aus: auf claude.ai unter den geplanten Aufgaben.

### Stand ansehen

`python3 pipeline/stand.py` (Status je Erlass, Kosten), `python3 pipeline/reservierung.py liste` (laufende Reservierungen).
