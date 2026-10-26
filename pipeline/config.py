"""Gemeinsame Einstellungen der Pipeline.

Alle Pfade sind relativ zum Projektordner (dem Ordner, in dem `pipeline/` liegt).
"""
from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _env_laden(pfad: Path) -> None:
    """Liest KEY=WERT-Zeilen aus .env im Projektordner (ohne zusätzliches Paket).
    Bereits gesetzte Umgebungsvariablen haben Vorrang."""
    if not pfad.exists():
        return
    for zeile in pfad.read_text(encoding="utf-8").splitlines():
        zeile = zeile.strip()
        if not zeile or zeile.startswith("#") or "=" not in zeile:
            continue
        k, v = zeile.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


_env_laden(ROOT / ".env")

DATA = ROOT / "data"
INVENTAR = DATA / "inventar"          # Artikellisten je Erlass (aus Fedlex)
ENTSCHEIDE = DATA / "entscheide"      # Cache der Entscheide (Metadaten + Volltext)
KARTEN = DATA / "karten"              # Karteikarten je Entscheid (aus der Batch API)
BATCHES = DATA / "batches"            # eingereichte Batches und Rohergebnisse
QUEUE = DATA / "queue.json"           # Warteschlange und Status je Artikel
ARBEIT = ROOT / "arbeit"              # Arbeitsordner je Artikel (Register, Prüfberichte)
KOMMENTARE = ROOT / "kommentare"      # kanonische Kommentierungen (Markdown)
SITE_DOCS = ROOT / "site" / "src" / "content" / "docs"

# Name des Werks, wie er auf der Website und im Zitiervorschlag erscheint.
WERK = os.environ.get("WERK_NAME", "Offener Steuerrechtskommentar")
WERK_KURZ = os.environ.get("WERK_KURZ", "OSK")

# Modelle der Batch-Schritte (siehe README, Abschnitt Kosten)
MODELL_KARTEN = os.environ.get("MODELL_KARTEN", "claude-opus-5-5")
MODELL_PRUEFUNG = os.environ.get("MODELL_PRUEFUNG", "claude-opus-5-5")

# Batch-Preise in USD pro Million Tokens (Stand 26.10.2026, 50 % Batch-Rabatt eingerechnet).
# Nur für die Kostenschätzung vor dem Einreichen; massgebend ist die Console.
BATCH_PREISE = {
    "claude-sonnet-5-5": {"in": 1.00, "out": 5.00},
    "claude-haiku-5-5": {"in": 0.05, "out": 0.25},   # bis 100'000 Tokens Prompt
    "claude-opus-5-5": {"in": 2.00, "out": 10.00},
}

# Die fünf Erlasse. `abk` sind die Abkürzungen, unter denen Entscheide den Erlass zitieren
# (DE, FR, IT). `abk_mehrdeutig` sind Abkürzungen, die auch kantonale Erlasse bezeichnen;
# Treffer damit prüft erst die Karteikarte.
ERLASSE = {
    "DBG": {
        "name": "Bundesgesetz über die direkte Bundessteuer",
        "sr": "642.11",
        "eli": "https://fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184",
        "abk": ["DBG", "LIFD"],
        "abk_mehrdeutig": [],
    },
    "StHG": {
        "name": "Bundesgesetz über die Harmonisierung der direkten Steuern der Kantone und Gemeinden",
        "sr": "642.14",
        "eli": "https://fedlex.data.admin.ch/eli/cc/1991/1256_1256_1256",
        "abk": ["StHG", "LHID", "LAID"],
        "abk_mehrdeutig": [],
    },
    "VStG": {
        "name": "Bundesgesetz über die Verrechnungssteuer",
        "sr": "642.21",
        "eli": "https://fedlex.data.admin.ch/eli/cc/1966/371_385_384",
        "abk": ["VStG", "LIA", "LIP"],
        "abk_mehrdeutig": [],
    },
    "MWSTG": {
        "name": "Bundesgesetz über die Mehrwertsteuer",
        "sr": "641.20",
        "eli": "https://fedlex.data.admin.ch/eli/cc/2009/615",
        "abk": ["MWSTG", "LTVA", "LIVA"],
        "abk_mehrdeutig": [],
    },
    "StG": {
        "name": "Bundesgesetz über die Stempelabgaben",
        "sr": "641.10",
        "eli": "https://fedlex.data.admin.ch/eli/cc/1974/11_11_11",
        "abk": ["LT", "LTB"],
        # «StG» heisst auch jedes kantonale Steuergesetz; nur mit Bezug auf die Stempelabgaben zählen.
        "abk_mehrdeutig": ["StG"],
    },
}

USER_AGENT = "steuerkommentar-oss/0.1 (Forschungsprojekt; Kontakt im README)"


def lade_json(pfad: Path, standard=None):
    if pfad.exists():
        return json.loads(pfad.read_text(encoding="utf-8"))
    return standard


def schreibe_json(pfad: Path, daten) -> None:
    pfad.parent.mkdir(parents=True, exist_ok=True)
    tmp = pfad.with_suffix(pfad.suffix + ".tmp")
    tmp.write_text(json.dumps(daten, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(pfad)


def art_slug(nummer: str) -> str:
    """'26' -> 'art-26', '37a' -> 'art-37a', '205bis' -> 'art-205bis'."""
    return "art-" + nummer.lower().replace(" ", "")


def art_sortkey(nummer: str) -> tuple:
    import re
    m = re.match(r"(\d+)\s*([a-z]*)", nummer.lower())
    if not m:
        return (10**6, nummer)
    zusatz = m.group(2)
    reihe = ["", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
             "bis", "ter", "quater", "quinquies", "sexies", "septies", "octies", "novies", "decies"]
    return (int(m.group(1)), reihe.index(zusatz) if zusatz in reihe else 99, zusatz)
