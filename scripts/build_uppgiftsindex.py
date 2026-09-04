#!/usr/bin/env python3
"""Generera 00_index/uppgiftsindex.md ur 07_fulltext/.

Läser de faktiska `### Uppgift N`-rubrikerna i filerna, så indexet kan aldrig
komma ur synk med innehållet. Kör om efter varje ändring i 07_fulltext/.

    python3 scripts/build_uppgiftsindex.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FULLTEXT = ROOT / "07_fulltext"
UPG = re.compile(r"^### Uppgift (\d+)\s*$")

KAPITEL = {
    "9": "Binomialsatsen",
    "10": "Rummet R^n, kvadriker och koordinatsystem",
    "12": "Vektorfunktioner och kurvor",
    "13": "Partiella derivator",
    "14": "Extremvärden och parameterberoende integraler",
    "15": "Multipelintegraler",
}


def spans(nums: list[int]) -> str:
    if not nums:
        return "–"
    nums = sorted(set(nums))
    out, start, prev = [], nums[0], nums[0]
    for n in nums[1:] + [None]:
        if n != prev + 1:
            out.append(str(start) if start == prev else f"{start}–{prev}")
            start = n
        prev = n
    return ", ".join(out)


def main() -> None:
    data = json.loads((ROOT / "scripts" / "section_map.json").read_text(encoding="utf-8"))
    L = ["# Uppgiftsindex — MATB21 Flervariabelanalys HT26", "",
         "Snabbtabell för att hitta en specifik övningsuppgift i fulltexten.",
         "Genererad av `scripts/build_uppgiftsindex.py` direkt ur `07_fulltext/` —",
         "kör om skriptet efter varje ändring där.", "",
         "**Direktlänk:** `07_fulltext/kap_13/13.5.md#uppgift-11` (uppgift 11 i avsnitt 13.5)", "",
         "> Sektionerna är namngivna efter **kursens** numrering (Adams 10:e uppl.).",
         "> Texten och sidmarkörerna `[sid NN]` kommer ur 9:e upplagan — se `CLAUDE.md`",
         "> för mappningen mellan upplagorna.", "", "---", ""]

    tot = 0
    kap_nu = None
    for s in data["sektioner"]:
        f = FULLTEXT / s["fil"]
        if not f.exists():
            continue
        kap = s["kurs"].split(".")[0]
        if kap != kap_nu:
            if kap_nu is not None:
                L.append("")
            L += [f"## Kapitel {kap} — {KAPITEL.get(kap, '')}", "",
                  "| Avsnitt (10:e) | 9:e uppl. | Uppgifter | Antal | Sidor (9:e) | Fil |",
                  "|---|---|---|---|---|---|"]
            kap_nu = kap
        nums = [int(m.group(1)) for m in map(UPG.match, f.read_text(encoding="utf-8").splitlines()) if m]
        tot += len(nums)
        a, b = s["sidor"]
        L.append(f"| {s['kurs']} | {s['nionde']} | {spans(nums)} | {len(nums)} | "
                 f"{a}–{b} | [`{s['fil']}`](../07_fulltext/{s['fil']}) |")

    L += ["", "---", "", f"**Totalt:** {tot} övningsuppgifter i "
          f"{len([s for s in data['sektioner'] if (FULLTEXT / s['fil']).exists()])} avsnitt.", "",
          "Övningsblad från Canvas ligger separat i "
          "[`01_kursmaterial/ovningsblad/`](../01_kursmaterial/ovningsblad/),",
          "gamla tentor i [`05_tentor/`](../05_tentor/).", ""]

    out = ROOT / "00_index" / "uppgiftsindex.md"
    out.write_text("\n".join(L), encoding="utf-8")
    print(f"Skrev {out.relative_to(ROOT)}: {tot} uppgifter")


if __name__ == "__main__":
    main()
