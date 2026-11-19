#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Run the mechanical items of the Project File validation checklist on a markdown Project File.

Usage: validate_project_file.py PATH

Checks what a script can decide: section order, coverage map rows, one UPPERCASE
keyword per rule, no lowercase keywords in rule text, every rule field filled,
every source with a tier and a date, DoD items present. The judgement items
(checks are objective, checks are runnable, nothing contested marked Consensus)
are listed as MANUAL for the reviewer. Reads the file only.
"""
import re
import sys

SECTIONS = ["1. Charter", "2. Coverage map", "3. Standards register", "4. Build checklist",
            "5. Decision log", "6. Gate log", "7. Parking lot"]
KEYWORDS = re.compile(r"\b(MUST NOT|SHOULD NOT|MUST|SHOULD|MAY)\b")
LOWER = re.compile(r"\b(must|should|may)\b")
STATUSES = {"Consensus", "Contested", "Emerging", "Outdated", "Decided"}
CONFIDENCE = {"High", "Moderate", "Low"}
DATE = re.compile(r"\d{4}(-\d{2}(-\d{2})?)?|n\.d\., accessed \d{4}-\d{2}-\d{2}|v\d{4}\.\d{2}\.\d{2}|DEC-\d+")
TIER = re.compile(r"\(\s*(?:tier\s*)?[1-5]\b|DEC-\d+")


def table_rows(block):
    rows = [l for l in block.splitlines() if l.startswith("|")]
    return [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows[2:]]


def section(text, name):
    m = re.search(rf"^## {re.escape(name)}\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1) if m else None


def main(path):
    text = open(path, encoding="utf-8").read()
    fails = []
    found = [h for h in re.findall(r"^## (.+)$", text, re.M) if h in SECTIONS]
    if found != SECTIONS:
        fails.append(f"sections present/order: {found}")

    charter = section(text, "1. Charter") or ""
    if not re.search(r"DOD-\d+", charter):
        fails.append("no DOD items in charter")

    reg = table_rows(section(text, "3. Standards register") or "")
    ids = set()
    for r in reg:
        if len(r) < 6:
            fails.append(f"short register row: {r[:1]}")
            continue
        rid, rule, status, conf, check, src = r[:6]
        ids.add(rid)
        kws = KEYWORDS.findall(rule)
        if len(kws) != 1:
            fails.append(f"{rid}: {len(kws)} keywords")
        if LOWER.search(rule):
            fails.append(f"{rid}: lowercase keyword in rule text")
        if status not in STATUSES:
            fails.append(f"{rid}: bad status '{status}'")
        if conf not in CONFIDENCE:
            fails.append(f"{rid}: bad confidence '{conf}'")
        if not check:
            fails.append(f"{rid}: empty check")
        if not (TIER.search(src) and DATE.search(src)):
            fails.append(f"{rid}: source lacks tier or date")

    cov = table_rows(section(text, "2. Coverage map") or "")
    for r in cov:
        if len(r) < 4:
            fails.append(f"short coverage row: {r[:1]}")
            continue
        dim, inscope, rids, notes = r[:4]
        if inscope.lower().startswith("yes"):
            listed = re.findall(r"[A-Z0-9]+-\d+", rids)
            if not listed and not notes:
                fails.append(f"coverage '{dim}': no rules and no reason")
            for x in listed:
                if x not in ids:
                    fails.append(f"coverage '{dim}': {x} not in register")

    for item in ("Every check is objective pass/fail",
                 "Every check can be run with the tools available (or is a Proposed entry)",
                 "Every DoD item is checkable",
                 "No contested finding is written as Consensus",
                 "Every open question is a marker or a Proposed entry"):
        print(f"MANUAL {item}")
    for f in fails:
        print(f"FAIL {f}")
    print(f"{len(reg)} rule(s), {len(fails)} mechanical failure(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
