"""Word-Fassung (optional): wandelt eine Kommentierung in das Markup des OK-Builders um und
ruft den Builder aus dem Plugin «OK-Steuerkommentar» auf, falls er gefunden wird.

    python3 pipeline/md2docx.py kommentare/DBG/art-26.md [-o Art_26_DBG.docx] [--builder PFAD]

Ohne Builder entsteht nur die Markup-Datei (arbeit/<Erlass>/<art>/markup.txt).
"""
from __future__ import annotations

import argparse
import glob
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import ARBEIT, art_slug  # noqa: E402
from kommentar import fussnoten_finden, lesen  # noqa: E402


def markup(k) -> str:
    def inline(t: str) -> str:
        teile, pos = [], 0
        for s, e, inhalt in fussnoten_finden(t):
            teile += [t[pos:s], "[[", inhalt, "]]"]
            pos = e
        teile.append(t[pos:])
        return "".join(teile)

    m = k.meta
    z = [f"= Kommentierung zu Art. {m['artikel']} {m['erlass']}"]
    z += ["> " + n.replace("**", "") for n in k.normtext]
    z.append("TOC")
    for b in k.bloecke:
        if b.art == "ueberschrift":
            z.append("#" * b.ebene + " " + b.text)
        elif b.art == "zwischentitel":
            z.append("!! " + b.text)
        elif b.art == "randnote":
            kopf = f"RZ{{{b.label}}}: " if b.label else "RZ: "
            # Der Builder kennt keine Listen in Randnoten: Aufzählung im Fliesstext mit Halbgeviertstrich
            liste = "".join(" – " + inline(x) for x in b.zeilen)
            z.append(kopf + inline(b.text) + liste)
        elif b.art in ("liste", "verzeichnis_eintrag"):
            z.append("- " + inline(b.text))
        elif b.art == "absatz":
            z.append("- " + inline(b.text) + "".join(" – " + inline(x) for x in b.zeilen))
    return "\n".join(z) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("datei")
    ap.add_argument("-o", "--ausgabe")
    ap.add_argument("--builder")
    a = ap.parse_args()
    k = lesen(a.datei)
    erlass, slug = k.meta["erlass"], art_slug(k.meta["artikel"])
    ordner = ARBEIT / erlass / slug
    ordner.mkdir(parents=True, exist_ok=True)
    mpfad = ordner / "markup.txt"
    mpfad.write_text(markup(k), encoding="utf-8")
    wurzeln = [Path.home() / ".claude" / "plugins", Path("/root/.claude/plugins"), Path("/mnt/skills"),
               Path.home() / "Library" / "Application Support" / "Claude"]
    kandidaten = []
    for w in wurzeln:
        if w.exists():
            kandidaten += glob.glob(str(w / "**" / "ok-steuerkommentar*" / "skills" / "steuerkommentar"
                                        / "scripts" / "kommentar_build.py"), recursive=True)
    kandidaten.sort(key=lambda p: Path(p).stat().st_mtime, reverse=True)
    builder = a.builder or (kandidaten[0] if kandidaten else None)
    if not builder:
        print(f"Markup: {mpfad} (Builder nicht gefunden; mit --builder angeben)")
        return
    skill = Path(builder).parent.parent
    vorlage = skill / "assets" / "Vorlage_Online_Kommentar.docx"
    aus = a.ausgabe or str(ordner / f"Art_{k.meta['artikel']}_{erlass}_Kommentierung_{k.meta['stand']}.docx")
    cmd = [sys.executable, "-I", builder, str(mpfad), "-o", aus]
    if vorlage.exists():
        cmd += ["--template", str(vorlage)]
    subprocess.run(cmd, check=True)
    print(f"Word: {aus}")


if __name__ == "__main__":
    main()
