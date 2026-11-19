#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Run the ARCH and SAFE-01 register checks on every skill in plugins/*/skills/.

Reads local files only. Exit 1 if any MUST check fails; SHOULD failures are
reported and also exit 1 so they cannot pass unnoticed (waivers are logged in
the Project File, not here).
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FORBIDDEN = re.compile(r"bypassPermissions|skip-permissions|dangerously-skip|permissions\.allow\s*[:=]", re.I)
REF_RE = re.compile(r"\]\(([^)#:]+)\)|`((?:references|scripts|assets)/[^`]+)`")


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if re.match(r"^[A-Za-z_-]+:", line):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"')
    return out


def check(skill_dir):
    results = []
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    fm = front_matter(text)
    name, desc = fm.get("name", ""), fm.get("description", "")
    results.append(("ARCH-01", bool(name and desc)))
    results.append(("ARCH-02", name == skill_dir.name))
    results.append(("ARCH-03", bool(NAME_RE.match(name)) and len(name) <= 64))
    results.append(("ARCH-04", 1 <= len(desc) <= 1024))
    results.append(("ARCH-05", "Use when" in desc))
    results.append(("ARCH-06", text.count("\n") < 500))
    refs = [a or b for a, b in REF_RE.findall(text)]
    local = [r for r in refs if not r.startswith(("http", "/"))]
    results.append(("ARCH-07", all(r.count("/") <= 1 for r in local)))
    results.append(("SAFE-01", not FORBIDDEN.search(text)))
    return results


def main():
    skills = sorted(p.parent for p in ROOT.glob("plugins/*/skills/*/SKILL.md"))
    failed = 0
    for s in skills:
        for rule, ok in check(s):
            print(f"{'PASS' if ok else 'FAIL'} {rule} {s.relative_to(ROOT)}")
            failed += not ok
    print(f"{len(skills)} skill(s), {failed} failure(s)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
