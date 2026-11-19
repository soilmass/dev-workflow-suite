#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Copy shared/standard.md into every skill listed in shared/consumers.txt.

Each consumer SKILL.md holds the copy between two marker lines:

    <!-- shared-standard:begin -->
    <!-- shared-standard:end -->

Usage:
    sync_standard.py [--root DIR]          write the source into every copy
    sync_standard.py [--root DIR] --check  report differences; exit 1 if any

The script reads and writes local files only. It runs nothing else and makes
no network calls.
"""
import argparse
import pathlib
import sys

BEGIN = "<!-- shared-standard:begin -->"
END = "<!-- shared-standard:end -->"


def load_consumers(root):
    path = root / "shared" / "consumers.txt"
    lines = path.read_text(encoding="utf-8").splitlines()
    return [l.strip() for l in lines if l.strip() and not l.lstrip().startswith("#")]


def split(text, where):
    if text.count(BEGIN) != 1 or text.count(END) != 1:
        raise ValueError(f"{where}: needs exactly one begin and one end marker")
    head, rest = text.split(BEGIN, 1)
    body, tail = rest.split(END, 1)
    return head, body, tail


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=pathlib.Path(__file__).resolve().parent.parent, type=pathlib.Path)
    ap.add_argument("--check", action="store_true", help="report differences and exit 1 if any")
    args = ap.parse_args()
    root = args.root.resolve()

    source = (root / "shared" / "standard.md").read_text(encoding="utf-8")
    block = "\n" + source.rstrip("\n") + "\n"
    consumers = load_consumers(root)
    if not consumers:
        print("error: shared/consumers.txt lists no skills", file=sys.stderr)
        return 2

    differing, errors = [], []
    for rel in consumers:
        skill = root / rel / "SKILL.md"
        if not skill.is_file():
            errors.append(f"{rel}: SKILL.md not found")
            continue
        text = skill.read_text(encoding="utf-8")
        try:
            head, body, tail = split(text, rel)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if body == block:
            continue
        differing.append(rel)
        if not args.check:
            skill.write_text(head + BEGIN + block + END + tail, encoding="utf-8")

    for e in errors:
        print(f"error: {e}", file=sys.stderr)
    if args.check:
        for rel in differing:
            print(f"differs: {rel}")
        print(f"checked {len(consumers)} skill(s): {len(differing)} differ, {len(errors)} error(s)")
        return 1 if (differing or errors) else 0
    print(f"synced {len(differing)} of {len(consumers)} skill(s); {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
