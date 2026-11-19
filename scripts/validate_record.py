#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Validate a project's suite record (.suite/ and docs/decisions/) against the REC rules.

Usage: validate_record.py [PROJECT_DIR]   (default: current directory)

Prints PASS or FAIL per REC rule and exits 1 on any failure.
Reads local files only; runs nothing else.
"""
import datetime
import pathlib
import re
import sys

import yaml

STAGES = ["frame", "shape", "plan", "design", "build", "verify", "release", "operate", "learn"]
STAGE_FILES = {"frame": "frame.md", "shape": "shape.md", "plan": "plan.md", "design": "design.md",
               "build": "build.md", "verify": "verify.md", "release": "releases", "operate": "operations",
               "learn": "retros"}
PROFILES = {"small", "standard", "critical"}
ID_RE = re.compile(r"^(OUT|NEED|QUAL|DOD|ITEM|THR|FIND|INC)-\d+$")
DECISION_STATUS = re.compile(r"^(proposed|accepted|rejected|deprecated|superseded by \d{4})$")
KEYWORDS = re.compile(r"\b(MUST NOT|SHOULD NOT|MUST|SHOULD|MAY)\b")
LOWER = re.compile(r"\b(must|should|may)\b")
RESPONSES = {"mitigate", "eliminate", "transfer", "accept"}


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


def rows(text):
    """Table rows as cell lists, header and separator rows skipped."""
    out = []
    for line in text.splitlines():
        if not line.startswith("|") or re.match(r"^\|\s*-", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        out.append(cells)
    return out


def main(root):
    root = pathlib.Path(root).resolve()
    s = root / ".suite"
    res = []

    def check(rule, ok, msg):
        res.append(("PASS" if ok else "FAIL", rule, msg))

    rec = s / "record.md"
    if not rec.is_file():
        print("FAIL REC-01 .suite/record.md not found")
        return 1
    rtext = rec.read_text(encoding="utf-8")
    h = front_matter(rtext)
    na = h.get("not_applicable") or {}
    stage = h.get("stage")
    check("REC-01", bool(h.get("name")) and h.get("profile") in PROFILES and (stage in STAGES or stage == "done")
          and bool(re.fullmatch(r"v\d+\.\d+\.\d+", str(h.get("library", "")))),
          f"header: name, profile in {sorted(PROFILES)}, stage, library vX.Y.Z")
    check("REC-01", all(k in STAGES and str(v).strip() for k, v in na.items()),
          "every not-applicable stage gives a reason")

    # gate log: Date | Version | Stage | Result | Notes
    version = h.get("version")
    check("REC-13", isinstance(version, int) and version >= 1, "header version is a whole number from 1")
    gates = [r for r in rows(rtext.split("## Gate log", 1)[1].split("\n## ", 1)[0])] if "## Gate log" in rtext else []
    gates = [g for g in gates if g and g[0].lower() != "date"]
    bad = []
    for g in gates:
        try:
            datetime.date.fromisoformat(g[0])
            ok = int(g[1]) >= 1 and g[2] in STAGES and g[3] in ("passed", "blocked")
        except (ValueError, IndexError):
            ok = False
        if not ok:
            bad.append(" | ".join(g))
    check("REC-05", "## Gate log" in rtext and not bad,
          "gate log rows have an ISO date, a version, a stage and passed or blocked" + (f" (bad: {bad})" if bad else ""))
    good = [g for g in gates if " | ".join(g) not in bad]
    if isinstance(version, int):
        ahead = [g for g in good if int(g[1]) > version]
        prev_learn = version == 1 or any(int(g[1]) == version - 1 and g[2] == "learn" and g[3] == "passed" for g in good)
        check("REC-13", not ahead and prev_learn,
              "no gate row is ahead of the header version, and each new version follows a passed learn"
              + (f" (ahead: {len(ahead)})" if ahead else "") + ("" if prev_learn else f" (no passed learn for version {version - 1})"))
    cur = version if isinstance(version, int) else 1
    passed = {g[2] for g in good if int(g[1]) == cur and g[3] == "passed"}
    cycle = STAGES if cur == 1 else STAGES[STAGES.index("plan"):]
    expected = next((st for st in cycle if st not in passed and st not in na), "done")
    check("REC-06", stage == expected,
          f"header stage '{stage}' is the first stage of version {cur} without a passed gate ('{expected}')")

    before = STAGES[:STAGES.index(stage)] if stage in STAGES else STAGES
    missing = [st for st in before if st not in na and not (s / STAGE_FILES[st]).exists()]
    check("REC-02", not missing, "every stage before the current one has its file" + (f" (missing {missing})" if missing else ""))

    # IDs
    defined, dupes, need_rows, thr_rows, find_rows, dod_rows, item_rows = {}, [], [], [], [], [], []
    for f in sorted(s.rglob("*.md")):
        for r in rows(f.read_text(encoding="utf-8")):
            if r and ID_RE.match(r[0]):
                if r[0] in defined:
                    dupes.append(f"{r[0]} ({f.name} and {defined[r[0]]})")
                defined.setdefault(r[0], f.name)
                kind = r[0].split("-")[0]
                {"NEED": need_rows, "THR": thr_rows, "FIND": find_rows, "DOD": dod_rows, "ITEM": item_rows}.get(kind, []).append(r)
    check("REC-03", not dupes, "IDs are unique across the record" + (f" (duplicates: {dupes})" if dupes else ""))
    orphan = [r[0] for r in need_rows if not any(o in defined for o in re.findall(r"OUT-\d+", " ".join(r[1:])))]
    check("REC-04", not orphan, "every NEED traces to a defined OUT" + (f" (orphans: {orphan})" if orphan else ""))
    dorph = [r[0] for r in dod_rows if not any(o in defined for o in re.findall(r"OUT-\d+", " ".join(r[1:])))]
    check("REC-11", not dorph, "every DOD traces to a defined OUT" + (f" (orphans: {dorph})" if dorph else ""))
    badst = [r[0] for r in item_rows if not {"open", "passed", "blocked", "waived"} & {c.lower() for c in r[1:]}]
    check("REC-12", not badst, "every ITEM has a status: open, passed, blocked or waived"
          + (f" (missing: {badst})" if badst else ""))
    noresp = [r[0] for r in thr_rows if not RESPONSES & {c.lower() for c in r[1:]}]
    check("REC-09", not noresp, "every THR has one response: mitigate, eliminate, transfer or accept"
          + (f" (missing: {noresp})" if noresp else ""))
    nocwe = [r[0] for r in find_rows if not re.search(r"CWE-\d+", " ".join(r[1:]))]
    check("REC-10", not nocwe, "every FIND carries a CWE ID" + (f" (missing: {nocwe})" if nocwe else ""))

    # rules.md
    rules = s / "rules.md"
    if rules.is_file():
        rt = rules.read_text(encoding="utf-8")
        rfm = front_matter(rt)
        bad = []
        for r in rows(rt):
            if len(r) > 1 and re.fullmatch(r"[A-Z][A-Z0-9]*-\d+", r[0]):
                if len(KEYWORDS.findall(r[1])) != 1 or LOWER.search(r[1]):
                    bad.append(r[0])
        check("REC-08", bool(re.fullmatch(r"v\d+\.\d+\.\d+", str(rfm.get("library", "")))) and not bad,
              "rules.md names the library version; each rule has exactly one UPPERCASE keyword"
              + (f" (bad: {bad})" if bad else ""))

    # decisions
    dd = root / "docs" / "decisions"
    bad = []
    for f in sorted(dd.glob("*.md")) if dd.is_dir() else []:
        st = str(front_matter(f.read_text(encoding="utf-8")).get("status", ""))
        if not re.match(r"^\d{4}-[a-z0-9-]+\.md$", f.name) or not DECISION_STATUS.match(st):
            bad.append(f.name)
    check("REC-07", not bad, "decision records are NNNN-title.md with a valid status" + (f" (bad: {bad})" if bad else ""))

    for status, rule, msg in res:
        print(f"{status} {rule} {msg}")
    fails = sum(1 for r in res if r[0] == "FAIL")
    print(f"{len(res)} checks, {fails} failure(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
