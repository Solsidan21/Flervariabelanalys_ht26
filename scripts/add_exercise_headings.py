#!/usr/bin/env python3
"""Add `### Uppgift N` headings before each numbered exercise in 06_fulltext/.

Processes Markdown files that contain a `## Exercises X.Y` heading. For each
numbered exercise (plain `N.` or bold `**N.**`) inside that section, inserts a
`### Uppgift N` heading on the line above and strips the leading number from
the original line. Stops at the next `## ` heading (e.g. `## Chapter Review`).

Idempotent: skips lines already preceded by `### Uppgift N`.
Backup: writes <file>.bak before modifying (unless --no-backup).
Dry-run: --dry-run prints unified diff without writing.

Usage:
    python scripts/add_exercise_headings.py 06_fulltext/kap_5/*.md --dry-run
    python scripts/add_exercise_headings.py 06_fulltext/kap_5/*.md
"""
from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

EXERCISE_LINE = re.compile(r"^(\*\*)?(\d+)\.(?:\*\*)?\s+(.+?)\s*$")
EXERCISES_HEADER = re.compile(r"^## Exercises\s+[A-Za-z]?[\d.]+\b")
NEXT_H2 = re.compile(r"^## ")
EXISTING_HEADING = re.compile(r"^### Uppgift (\d+)\s*$")


def transform(text: str) -> tuple[str, dict]:
    lines = text.splitlines()
    stats = {"added": 0, "skipped_existing": 0, "numbers": [], "last_num": None}

    start = end = None
    for i, line in enumerate(lines):
        if start is None and EXERCISES_HEADER.match(line):
            start = i
            continue
        if start is not None and NEXT_H2.match(line) and not EXERCISES_HEADER.match(line):
            end = i
            break
    if start is None:
        return text, stats
    if end is None:
        end = len(lines)

    out: list[str] = []
    last_num: int | None = None
    expected_continuation_num: int | None = None

    for i, line in enumerate(lines):
        if not (start <= i < end):
            out.append(line)
            continue

        m = EXERCISE_LINE.match(line)
        if m is None:
            out.append(line)
            continue

        num = int(m.group(2))
        body = m.group(3).rstrip()

        prev_heading = EXISTING_HEADING.match(out[-1].rstrip()) if out else None
        if prev_heading and int(prev_heading.group(1)) == num:
            stats["skipped_existing"] += 1
            out.append(line)
            last_num = num
            continue

        if last_num is not None and num <= last_num:
            out.append(line)
            continue
        if last_num is not None and num > last_num + 5 and num > 50:
            out.append(line)
            continue
        if num > 200:
            out.append(line)
            continue

        out.append(f"### Uppgift {num}")
        out.append(body)
        stats["added"] += 1
        stats["numbers"].append(num)
        last_num = num

    stats["last_num"] = last_num
    new_text = "\n".join(out)
    if text.endswith("\n"):
        new_text += "\n"
    return new_text, stats


def count_existing_exercises(text: str) -> list[int]:
    lines = text.splitlines()
    start = end = None
    for i, line in enumerate(lines):
        if start is None and EXERCISES_HEADER.match(line):
            start = i
            continue
        if start is not None and NEXT_H2.match(line) and not EXERCISES_HEADER.match(line):
            end = i
            break
    if start is None:
        return []
    if end is None:
        end = len(lines)

    nums: list[int] = []
    last: int | None = None
    for line in lines[start:end]:
        m = EXERCISE_LINE.match(line)
        if not m:
            heading = EXISTING_HEADING.match(line.rstrip())
            if heading:
                nums.append(int(heading.group(1)))
                last = int(heading.group(1))
            continue
        num = int(m.group(2))
        if last is not None and num <= last:
            continue
        if last is not None and num > last + 5 and num > 50:
            continue
        if num > 200:
            continue
        nums.append(num)
        last = num
    return nums


def process_file(path: Path, dry_run: bool, no_backup: bool) -> dict:
    original = path.read_text()
    before_nums = count_existing_exercises(original)
    transformed, stats = transform(original)
    after_nums = count_existing_exercises(transformed)

    result = {
        "path": str(path),
        "before_count": len(before_nums),
        "after_count": len(after_nums),
        "before_last": before_nums[-1] if before_nums else None,
        "after_last": after_nums[-1] if after_nums else None,
        "added": stats["added"],
        "skipped_existing": stats["skipped_existing"],
        "changed": transformed != original,
    }

    if before_nums != after_nums:
        result["WARNING"] = (
            f"exercise sequence changed! before={before_nums} after={after_nums}"
        )

    if dry_run and result["changed"]:
        diff = difflib.unified_diff(
            original.splitlines(keepends=True),
            transformed.splitlines(keepends=True),
            fromfile=str(path),
            tofile=str(path) + " (after)",
            n=2,
        )
        result["diff"] = "".join(diff)
    elif result["changed"] and not dry_run:
        if not no_backup:
            bak = path.with_suffix(path.suffix + ".bak")
            bak.write_text(original)
        path.write_text(transformed)

    return result


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-backup", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args(argv)

    any_warning = False
    for path in args.files:
        if not path.is_file():
            print(f"skip (not a file): {path}", file=sys.stderr)
            continue
        result = process_file(path, args.dry_run, args.no_backup)
        if "WARNING" in result:
            any_warning = True

        if args.quiet:
            continue

        marker = "DRY-RUN" if args.dry_run else "APPLIED"
        if not result["changed"]:
            print(f"[{marker}] {path}: no change (added={result['added']}, skipped_existing={result['skipped_existing']})")
        else:
            print(
                f"[{marker}] {path}: "
                f"added={result['added']}, "
                f"before_count={result['before_count']} (last={result['before_last']}), "
                f"after_count={result['after_count']} (last={result['after_last']})"
            )
        if "WARNING" in result:
            print(f"  WARNING: {result['WARNING']}")
        if args.dry_run and "diff" in result:
            print(result["diff"])

    return 1 if any_warning else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
