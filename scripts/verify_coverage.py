#!/usr/bin/env python3
"""Kontrollera att fulltext-extraktionen täcker varje boksida exakt en gång.

Fångar felet från envariabelextraktionen där en sida på gränsen mellan två
sektioner föll bort för att båda agenterna trodde den tillhörde den andra.

Kontroller:
  1. [sid NN]-markörerna är strikt växande inom varje fil.
  2. Varje sida i det förväntade intervallet finns i minst en fil (SAKNAD = fel).
  3. Ingen sida finns i mer än en fil (DUBBLETT = varning; överlapp kan vara ok
     när en sida delas av två sektioner, men ska vara medvetet).

Användning:
    python3 scripts/verify_coverage.py 07_fulltext --range 1-132
    python3 scripts/verify_coverage.py 07_fulltext --range 555-560,571-604
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

SID = re.compile(r"^\[sid (\d+)\]\s*$")


def parse_ranges(spec: str) -> set[int]:
    out: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            out.update(range(int(a), int(b) + 1))
        else:
            out.add(int(part))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", help="mapp med kap_*/*.md")
    ap.add_argument("--range", required=True, help="förväntade boksidor, t.ex. 1-132")
    args = ap.parse_args()

    expected = parse_ranges(args.range)
    seen: dict[int, list[str]] = defaultdict(list)
    problems: list[str] = []

    files = sorted(Path(args.root).glob("kap_*/*.md"))
    if not files:
        print(f"FEL: inga filer under {args.root}/kap_*/*.md", file=sys.stderr)
        return 2

    for f in files:
        pages: list[int] = []
        for lineno, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            m = SID.match(line)
            if m:
                pages.append(int(m.group(1)))
                seen[int(m.group(1))].append(f.name)
        if not pages:
            problems.append(f"INGA SIDMARKÖRER: {f}")
        for a, b in zip(pages, pages[1:]):
            if b <= a:
                problems.append(f"EJ VÄXANDE: {f}: [sid {a}] följs av [sid {b}]")

    missing = sorted(expected - set(seen))
    dupes = sorted(p for p, fs in seen.items() if len(set(fs)) > 1)
    extra = sorted(set(seen) - expected)

    print(f"Filer: {len(files)}   Sidor täckta: {len(set(seen) & expected)}/{len(expected)}")
    for p in problems:
        print("  " + p)
    if missing:
        print(f"  SAKNADE SIDOR ({len(missing)}): {missing}")
    if dupes:
        print(f"  DUBBLETTER ({len(dupes)}): " + ", ".join(f"{p}={sorted(set(seen[p]))}" for p in dupes))
    if extra:
        print(f"  UTANFÖR INTERVALLET ({len(extra)}): {extra}")

    ok = not missing and not problems
    print("RESULTAT:", "OK" if ok else "FEL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
