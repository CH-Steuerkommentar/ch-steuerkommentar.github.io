"""Export der Literaturangaben aus allen ILE-Publikationen in Lexplorer Tax (ohne KI).

Liest jedes Dokument der ILE-Quellen über den MCP-Server von Lexplorer Tax (nur Lesen, keine
Suche), zieht Literaturverzeichnisse und zitatartige Fussnotenstellen heraus, bereinigt sie
mechanisch vor und schreibt Kandidatenlisten nach daten/ile-literatur/roh/ und Arbeitspakete
nach daten/ile-literatur/pakete/. Es werden nur Literaturangaben gespeichert, kein Fliesstext.

Aufruf: LEXPLORER_API_KEY=... python automation/ile_literatur_export.py [--limit N]
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

URL = "https://mcp-tax.lexplorer.ch/mcp"
WURZEL = Path(__file__).resolve().parent.parent / "daten" / "ile-literatur"

QUELLEN = {
    "fstr": ("fdd29b9d-b663-4602-876e-5c34c39b1b71", "Forum für Steuerrecht"),
    "schriftenreihe": ("6af5628c-af7c-4c42-811f-f4911c0242f2", "Schriftenreihe Finanzwissenschaft und Finanzrecht"),
    "working-papers": ("3ae3c711-6b40-4a76-a398-0ff91530195c", "ILE Working Papers"),
    "lehrbuch": ("39e25a14-4b78-4cfb-b294-ac94a160bac1", "ILE Lehrbuch Steuerrecht"),
    "seminare": ("8eaf21ea-8b49-4dd9-ae8a-ccaf6eb7764b", "St.Galler Seminare"),
}


class Mcp:
    def __init__(self, schluessel: str):
        self.kopf = {
            "X-API-KEY": schluessel,
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
        }
        self.n = 0
        antwort, kopf = self._post({"jsonrpc": "2.0", "id": self._id(), "method": "initialize",
                                    "params": {"protocolVersion": "2025-06-18", "capabilities": {},
                                               "clientInfo": {"name": "ile-literatur", "version": "1"}}})
        sid = kopf.get("mcp-session-id") or kopf.get("Mcp-Session-Id")
        if sid:
            self.kopf["Mcp-Session-Id"] = sid
        self._post({"jsonrpc": "2.0", "method": "notifications/initialized"})

    def _id(self) -> int:
        self.n += 1
        return self.n

    def _post(self, daten: dict):
        for versuch in range(5):
            try:
                anfrage = urllib.request.Request(URL, json.dumps(daten).encode(), self.kopf, method="POST")
                with urllib.request.urlopen(anfrage, timeout=120) as r:
                    text = r.read().decode("utf-8", "replace")
                    kopf = {k.lower(): v for k, v in r.headers.items()}
                break
            except (urllib.error.URLError, TimeoutError) as fehler:
                if isinstance(fehler, urllib.error.HTTPError) and fehler.code in (401, 403):
                    raise
                time.sleep(5 * (versuch + 1))
        else:
            raise RuntimeError("Lexplorer nicht erreichbar")
        if not text.strip():
            return None, kopf
        if text.lstrip().startswith("{"):
            return json.loads(text), kopf
        letzte = None
        for zeile in text.splitlines():
            if zeile.startswith("data:"):
                letzte = json.loads(zeile[5:].strip())
        return letzte, kopf

    def werkzeug(self, name: str, argumente: dict):
        antwort, _ = self._post({"jsonrpc": "2.0", "id": self._id(), "method": "tools/call",
                                 "params": {"name": name, "arguments": argumente}})
        if antwort is None or "error" in antwort:
            raise RuntimeError(f"{name}: {antwort}")
        inhalt = antwort["result"].get("content", [])
        text = "".join(teil.get("text", "") for teil in inhalt if teil.get("type") == "text")
        if antwort["result"].get("isError"):
            raise RuntimeError(f"{name}: {text[:300]}")
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return text


def volltext(mcp: Mcp, doc_id: str) -> str:
    teile, i, gesamt = [], 0, 1
    while i < gesamt:
        s = mcp.werkzeug("get_document_slice", {"doc_id": doc_id, "slice": i, "slice_size": 100000})
        teile.append(s.get("content", ""))
        gesamt = int(s.get("total_slices", 1))
        i += 1
        time.sleep(0.2)
    return "".join(teile)


# ---------------------------------------------------------------- Erkennung
VERZEICHNIS = re.compile(r"literatur|bibliogra|quellenverzeichnis|schrifttum|references|zitierte werke", re.I)
ZEITSCHRIFT = (r"ASA|Archiv|StR|ST|FStR|IFF|ZStP|StE|RDAF|RF|SJZ|ZBl|ZSR|AJP|GesKR|SZW|EF|Expert ?Focus|"
               r"Jusletter|ZBJV|IStR|Intertax|EC Tax Review|BTR|Bulletin|TREX|zsis\)|SteuerRevue|"
               r"StR|ZSIS|ZGRG|ZWR|SJ|JdT|RDS|SZS|recht|sic!|ZStrR|ASR|IWB|FR|DStR|StuW|FS|Festschrift|"
               r"Liber amicorum|Mélanges")
HINWEIS = re.compile(rf"\bin:|\b(?:{ZEITSCHRIFT})\b|Diss\.|thèse|Habil|Aufl\.|édition|ed\.|Hrsg\.|éd\.|"
                     r"(?:Zürich|Bern|Basel|Genf|Genève|Lausanne|St\. ?Gallen|Freiburg|Fribourg|Luzern|"
                     r"Neuchâtel|Köln|München|Wien|Berlin|Amsterdam|Paris|Cambridge|Oxford)[^,;]{0,25}\b(?:19|20)\d\d")
JAHR = re.compile(r"\b(19[5-9]\d|20[0-3]\d)\b")
PRAEFIX = re.compile(
    r"^(?:(?:vgl\.|siehe|s\.|so|ebenso|gl\.? ?M\.|a\.? ?M\.|z\.B\.|cf\.|voir|ainsi|ausführlich|dazu|"
    r"statt vieler|statt aller|kritisch|anders|zum Ganzen|insbesondere|namentlich|auch|ferner|"
    r"m\.w\.H\.|mit Hinweisen|zustimmend|ablehnend)[,:]?\s+)+", re.I)
NAME_AM_ANFANG = re.compile(
    r"^(?:[A-ZÄÖÜÉÈ][A-Za-zÄÖÜäöüßéèêàâçëïôûñ'’\-]+(?:\s+(?:von|van|de|du|da|del|di|zu)\s+[A-ZÄÖÜ][\w\-]+)?)"
    r"(?:[ ,/]+[A-ZÄÖÜÉÈ][\w'’.\-]*){0,8}\s*[,:]")
NICHT_LITERATUR = re.compile(
    r"^(?:vgl\.\s+|siehe\s+|s\.\s+)?(?:BGE|BGer|BVGer|BStGer|Urteil|Entscheid|Arrêt|ATF|TF|Art\.|Artikel|"
    r"Botschaft|Message|BBl|FF|AS|SR|KS|Kreisschreiben|Circulaire|Rundschreiben|ESTV|AFC|EStV|SSK|"
    r"OECD|OCDE|Commentary|MA |StE \d|VGer|StRK|RB|KRK|Verwaltungsgericht|Steuerrekurs|Obergericht|"
    r"Tabelle|Abbildung|Figure|Eigene Darstellung|Quelle:|Source:|Ebd|Ibid|a\.a\.O)", re.I)

STANDARD = re.compile(
    r"Kommentar zum (?:Schweizerischen )?Steuerrecht|Basler Kommentar|\bBSK\b|Commentaire romand|"
    r"Handkommentar|Kommentar zum (?:DBG|StHG|MWSTG|VStG|StG|Zürcher|Bundesgesetz)|"
    r"Kommentar DBG|Kommentar StHG|Commentaire (?:LIFD|LHID)|System des schweizerischen Steuerrechts|"
    r"Die Praxis der Bundessteuern|Einführung in das (?:inter)?(?:kantonale|nationale) Steuerrecht|"
    r"Droit fiscal suisse|Précis de droit fiscal|Steuerrecht I{1,2}\b|Schweizerisches Steuerrecht|"
    r"Höhn/Waldburger|Blumenstein/Locher|Locher, Kommentar|Das schweizerische Steuerrecht|"
    r"^Reich Markus, Steuerrecht|^Oberson Xavier, Droit fiscal|Interkantonales Steuerrecht, \d+\. Aufl", re.I)


def saeubern(t: str) -> str:
    t = re.sub(r"\$\s*\{\s*\}\s*\^\s*\{[^}]*\}\s*\$", "", t)          # ${ }^{12}$
    t = re.sub(r"\$\s*(\d+)\s*\^\s*\{[^}]*\}\s*\$", r"\1", t)          # $1995^{6}$ -> 1995
    t = re.sub(r"\$\s*(\d+)\s*\^\s*\{\\text\s*\{\s*([^}]*)\}\s*\}\s*\$", r"\1\2", t)  # $2^{\text{ème}}$
    t = re.sub(r"\[\^\d+\]:?", " ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"[*_`#|]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return re.sub(r"^(?:[-•–·]|\d{1,3}[.)])\s+", "", t)


def fragmente_fliesstext(text: str):
    for absatz in text.split("\n"):
        absatz = saeubern(absatz)
        if len(absatz) < 25:
            continue
        absatz = re.sub(r"^\d{1,4}\s+(?=[A-ZÄÖÜ])", "", absatz)  # Fussnotennummer am Anfang
        for teil in re.split(r";\s+|(?<=[a-zäöüé\)]{2})\.\s+(?=(?:\d{1,4}\s+)?[A-ZÄÖÜ][a-zäöü]+[ ,])", absatz):
            teil = re.sub(r"^\d{1,4}\s+(?=[A-ZÄÖÜ])", "", teil.strip())
            teil = PRAEFIX.sub("", teil)
            if 25 <= len(teil) <= 400 and JAHR.search(teil) and HINWEIS.search(teil) \
                    and NAME_AM_ANFANG.match(teil) and not NICHT_LITERATUR.match(teil):
                yield teil


def eintraege_verzeichnis(text: str):
    for zeile in text.split("\n"):
        zeile = saeubern(zeile)
        if 20 <= len(zeile) <= 700 and JAHR.search(zeile) and not NICHT_LITERATUR.match(zeile) \
                and not zeile.lower().startswith(("chunk", "pages", "document id", "segment id")):
            yield zeile


def chunks(text: str):
    teile = re.split(r"\n## Chunk \d+: (.*)\n", "\n" + text)
    yield "", teile[0]
    for i in range(1, len(teile) - 1, 2):
        yield teile[i], teile[i + 1]


# ---------------------------------------------------------------- Vorbereinigung
def schluessel(t: str) -> str:
    """Grober Werkschlüssel: erster Nachname + erste drei Titelwörter + erstes Jahr."""
    t2 = PRAEFIX.sub("", t)
    name = re.match(r"[A-Za-zÄÖÜäöüßéèêàâçëïôûñ'’\-]+", t2)
    name = name.group(0).lower() if name else ""
    rest = t2.split(",", 2)
    vorname = len(rest) > 2 and len(rest[1].split()) <= 3 and all(w[:1].isupper() for w in rest[1].split())
    titel = rest[2] if vorname else (rest[1] if len(rest) > 1 else "")
    woerter = [w for w in re.findall(r"[a-zäöüéèàç]{4,}", titel.lower())
               if w not in {"über", "dans", "pour", "unter", "nach", "einer", "eines", "der", "und"}][:3]
    jahr = JAHR.search(t)
    return f"{name}|{' '.join(woerter)}|{jahr.group(0) if jahr else ''}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="Dokumente je Quelle (Test)")
    ap.add_argument("--quellen", default=",".join(QUELLEN))
    ap.add_argument("--paket", type=int, default=1200, help="Werke je Arbeitspaket")
    args = ap.parse_args()

    schl = os.environ.get("LEXPLORER_API_KEY", "").strip()
    if not schl:
        print("LEXPLORER_API_KEY fehlt", file=sys.stderr)
        return 1
    mcp = Mcp(schl)
    (WURZEL / "roh").mkdir(parents=True, exist_ok=True)

    werke: dict[str, dict] = {}
    statistik = collections.Counter()
    for kurz in args.quellen.split(","):
        source_id, reihe = QUELLEN[kurz]
        dokumente = mcp.werkzeug("nav_list_documents", {"source_id": source_id})
        if args.limit:
            dokumente = dokumente[: args.limit]
        print(f"{kurz}: {len(dokumente)} Dokumente", flush=True)
        for nr, dok in enumerate(dokumente, 1):
            try:
                text = volltext(mcp, dok["doc_id"])
            except Exception as fehler:  # einzelnes Dokument überspringen
                print(f"  Fehler {dok['title'][:60]}: {fehler}", flush=True)
                statistik["fehler"] += 1
                continue
            titel = dok["title"]
            fundort = {"q": kurz, "t": titel, "u": dok.get("lexplorer_url", "")}
            for kopf, inhalt in chunks(text):
                ist_verz = bool(VERZEICHNIS.search(titel.split(" · ")[-1]) or VERZEICHNIS.search(kopf)
                                or VERZEICHNIS.search(inhalt[:200]))
                quelle = eintraege_verzeichnis(inhalt) if ist_verz else fragmente_fliesstext(inhalt)
                for frag in quelle:
                    statistik["verzeichnis" if ist_verz else "fussnote"] += 1
                    k = schluessel(frag)
                    w = werke.setdefault(k, {"k": k, "texte": collections.Counter(), "fundorte": [],
                                             "verzeichnis": False})
                    w["texte"][frag] += 1
                    w["verzeichnis"] |= ist_verz
                    if fundort not in w["fundorte"] and len(w["fundorte"]) < 12:
                        w["fundorte"].append(fundort)
            if nr % 25 == 0:
                print(f"  {nr}/{len(dokumente)}  Werke bisher {len(werke)}", flush=True)

    # Vorbereinigung: Standardwerke und alte Werke (ausser oft zitiert) aussondern
    liste, aus = [], collections.Counter()
    for w in werke.values():
        haeufig = sum(w["texte"].values())
        bester = max(w["texte"], key=lambda t: (w["verzeichnis"], len(t) if len(t) < 300 else 0))
        jahr = JAHR.search(bester)
        jahr = int(jahr.group(0)) if jahr else None
        eintrag = {"zitat": bester, "varianten": [t for t, _ in w["texte"].most_common(4) if t != bester][:3],
                   "jahr": jahr, "nennungen": haeufig, "aus_verzeichnis": w["verzeichnis"],
                   "fundorte": w["fundorte"]}
        if STANDARD.search(bester):
            aus["standardwerk"] += 1
            continue
        if jahr and jahr < 2000 and haeufig < 3:
            aus["vor_2000_selten"] += 1
            continue
        liste.append(eintrag)
    liste.sort(key=lambda e: e["zitat"].lower())

    with open(WURZEL / "roh" / "kandidaten.jsonl", "w", encoding="utf-8") as f:
        for e in liste:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    pakete = WURZEL / "pakete"
    pakete.mkdir(exist_ok=True)
    for alt in pakete.glob("paket_*.jsonl"):
        alt.unlink()
    for i in range(0, len(liste), args.paket):
        with open(pakete / f"paket_{i // args.paket + 1:02d}.jsonl", "w", encoding="utf-8") as f:
            for e in liste[i:i + args.paket]:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")
    bericht = {"fundstellen": dict(statistik), "werke_roh": len(werke), "kandidaten": len(liste),
               "ausgesondert": dict(aus), "pakete": -(-len(liste) // args.paket)}
    (WURZEL / "roh" / "bericht.json").write_text(json.dumps(bericht, indent=2, ensure_ascii=False))
    print(json.dumps(bericht, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
