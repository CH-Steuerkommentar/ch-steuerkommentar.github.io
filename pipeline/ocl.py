"""Kleiner Client für den öffentlichen MCP-Server von Open Case Law (https://mcp.opencaselaw.ch/mcp).
Kein Schlüssel nötig. Wird von entscheide.py für die Rechtsprechung des Bundesgerichts verwendet."""
from __future__ import annotations

import json
import time

import requests

from config import USER_AGENT

URL = "https://mcp.opencaselaw.ch/mcp"
KOPF = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream", "User-Agent": USER_AGENT}


class OCL:
    def __init__(self, pause: float = 0.15):
        self.s = requests.Session()
        self.sid = None
        self.n = 0
        self.pause = pause
        self._start()

    def _post(self, nutzlast: dict, timeout: int = 180) -> dict | None:
        kopf = dict(KOPF)
        if self.sid:
            kopf["Mcp-Session-Id"] = self.sid
        r = self.s.post(URL, headers=kopf, json=nutzlast, timeout=timeout)
        r.raise_for_status()
        if r.headers.get("mcp-session-id"):
            self.sid = r.headers["mcp-session-id"]
        text = r.content.decode("utf-8", errors="replace")
        daten = [z[5:].strip() for z in text.splitlines() if z.startswith("data:")]
        if daten:
            return json.loads(daten[-1])
        return json.loads(text) if text.strip() else None

    def _start(self) -> None:
        self.sid = None
        self._post({"jsonrpc": "2.0", "id": 0, "method": "initialize", "params": {
            "protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "steuerkommentar", "version": "1"}}})
        try:
            self._post({"jsonrpc": "2.0", "method": "notifications/initialized"})
        except Exception:  # noqa: BLE001
            pass

    def aufruf(self, werkzeug: str, argumente: dict) -> dict:
        for versuch in range(4):
            self.n += 1
            try:
                antwort = self._post({"jsonrpc": "2.0", "id": self.n, "method": "tools/call",
                                      "params": {"name": werkzeug, "arguments": argumente}})
                if antwort and "error" in antwort:
                    raise RuntimeError(antwort["error"])
                erg = antwort["result"]
                if erg.get("isError"):
                    raise RuntimeError(erg.get("content", [{}])[0].get("text", "Fehler")[:300])
                time.sleep(self.pause)
                return erg.get("structuredContent") or {}
            except Exception:  # noqa: BLE001
                if versuch == 3:
                    raise
                time.sleep(3 * (versuch + 1))
                self._start()
        return {}

    def suche(self, abfrage: str, gericht: str) -> list[dict]:
        """Alle Treffer (kompakt) einer Abfrage, über alle Seiten."""
        treffer, offset = [], 0
        while True:
            erg = self.aufruf("search_decisions", {"query": abfrage, "court": gericht, "limit": 2000,
                                                   "offset": offset, "fields": "compact"})
            treffer += erg.get("results", [])
            if not erg.get("has_more"):
                return treffer
            offset = erg.get("next_offset", offset + len(erg.get("results", [])))

    def entscheid(self, decision_id: str, volltext: bool = True) -> dict:
        return self.aufruf("get_decision", {"decision_id": decision_id, "full_text": volltext})
