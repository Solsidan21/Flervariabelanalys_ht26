#!/usr/bin/env python3
"""Per-sektionskontroll av fulltext-extraktionen mot råtexten.

För varje sektion i scripts/section_map.json:
  - vilka [sid NN] som saknas jämfört med sektionens sidintervall
  - om markörerna är strikt växande
  - antal uppgifter och största uppgiftsnummer (luckor flaggas)

Användning:
    python3 scripts/check_sections.py              # alla sektioner
    python3 scripts/check_sections.py 13.5 13.6    # bara vissa
Exitkod 1 om något saknas.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FULLTEXT = ROOT / "07_fulltext"
SID = re.compile(r"^\[sid (\d+)\]\s*$")
UPG = re.compile(r"^### Uppgift (\d+)\s*$")


def main() -> int:
    data = json.loads((ROOT / "scripts" / "section_map.json").read_text(encoding="utf-8"))
    wanted = set(sys.argv[1:])
    bad = 0
    for s in data["sektioner"]:
        if wanted and s["kurs"] not in wanted:
            continue
        f = FULLTEXT / s["fil"]
        if not f.exists():
            print(f"{s['kurs']:>5}  SAKNAS: {s['fil']}")
            bad += 1
            continue
        lines = f.read_text(encoding="utf-8").splitlines()
        sids = [int(m.group(1)) for m in map(SID.match, lines) if m]
        upg = [int(m.group(1)) for m in map(UPG.match, lines) if m]
        a, b = s["sidor"]
        missing = [p for p in range(a, b + 1) if p not in sids]
        notinc = [(x, y) for x, y in zip(sids, sids[1:]) if y <= x]
        gaps = [n for n in range(1, max(upg) + 1) if n not in upg] if upg else []
        status = "OK" if not missing and not notinc and not gaps else "FEL"
        if status == "FEL":
            bad += 1
        print(f"{s['kurs']:>5}  {status:3}  rader={len(lines):4}  sid={len(sids):2}/{b - a + 1:2}  uppg={len(upg):3}")
        if missing:
            print(f"        saknade [sid]: {missing}")
        if notinc:
            print(f"        ej växande: {notinc}")
        if gaps:
            print(f"        uppgiftsluckor: {gaps}")
    print("RESULTAT:", "OK" if bad == 0 else f"FEL i {bad} sektion(er)")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
