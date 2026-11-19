#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Check every skill in plugins/*/skills/ against standards/contracts.yaml.

Prints one line per check: PASS, FAIL, LEGACY or PENDING, with the SKL rule ID.
Exit 1 if any check fails. Reads local files only; runs nothing else.

  PENDING  a contract whose skill is not built yet (allowed)
  LEGACY   a 0.x skill whose replacement is not built yet (allowed)
"""
import argparse
import pathlib
import re
import sys

import yaml

MARKER = "<!-- shared-standard:begin -->"


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return yaml.safe_load(m.group(1)) or {} if m else {}


def sections(text):
    """Map each '## ' heading to the text under it, in order."""
    parts = re.split(r"^(## .+)$", text, flags=re.M)
    out = {}
    for i in range(1, len(parts), 2):
        out[parts[i].strip()] = parts[i + 1]
    return out


def check_contracts(c, results):
    names = c["skills"]
    stage_writes = {}
    for name, k in names.items():
        if k["kind"] not in ("stage", "tool"):
            results.append(("FAIL", "SKL-12", name, f"kind '{k['kind']}' is not stage or tool"))
        if k["kind"] == "stage":
            if name not in c["stages"]:
                results.append(("FAIL", "SKL-12", name, "stage skill not in the stages list"))
            nxt = k.get("next")
            if nxt not in names:
                results.append(("FAIL", "SKL-12", name, f"next '{nxt}' is not a skill"))
            for w in k["writes"]:
                if w.startswith("append: "):
                    continue
                if w in stage_writes and w != "docs/decisions/":
                    results.append(("FAIL", "SKL-12", name, f"writes {w}, already written by {stage_writes[w]}"))
                stage_writes.setdefault(w, name)
        for mod in k.get("library", []):
            if mod not in c["library_modules"]:
                results.append(("FAIL", "SKL-12", name, f"unknown library module '{mod}'"))
        ids = list(k["gate"]) + list(k.get("must", {})) + list(k.get("must_not", {}))
        prefix = name.upper() + "-"
        for i in ids:
            if not re.fullmatch(re.escape(prefix) + r"[GMN]\d+", i):
                results.append(("FAIL", "SKL-12", name, f"rule ID {i} does not follow {prefix}G/M/N<n>"))
    if not any(r[0] == "FAIL" for r in results):
        results.append(("PASS", "SKL-12", "contracts.yaml", f"{len(names)} contracts consistent"))


def check_skill(root, name, k, c, results):
    d = next(root.glob(f"plugins/*/skills/{name}"))
    text = (d / "SKILL.md").read_text(encoding="utf-8")
    fm = front_matter(text)
    meta = fm.get("metadata") or {}

    def res(ok, rule, msg):
        results.append(("PASS" if ok else "FAIL", rule, name, msg))

    want_stage = name if k["kind"] == "stage" else "tool"
    res(fm.get("name") == name and bool(fm.get("description")), "SKL-01", "front matter name and description")
    res("Use when" in str(fm.get("description", "")), "SKL-02", "description says when to use it")
    res(fm.get("license") == "CC-BY-4.0", "SKL-03", "licence CC-BY-4.0")
    res(str(meta.get("contract")) == c["contract_version"] and meta.get("stage") == want_stage,
        "SKL-04", f"metadata contract {c['contract_version']} and stage '{want_stage}'")
    res(text.count("\n") < 500, "SKL-05", "SKILL.md under 500 lines")

    secs = sections(text)
    heads = [h for h in secs if h in c["required_sections"]]
    res(heads == c["required_sections"], "SKL-06", "required sections present, in order")

    reads = secs.get("## Reads", "")
    first = re.search(r"`([^`]+)`", reads)
    res(bool(first) and first.group(1) == k["reads"][0], "SKL-07",
        f"Reads names '{k['reads'][0]}' first")
    missing_reads = [r for r in k["reads"] if r not in reads]
    res(not missing_reads, "SKL-07", f"Reads lists every contract input{': missing ' + ', '.join(missing_reads) if missing_reads else ''}")

    writes = secs.get("## Writes", "")
    want = [w.replace("append: ", "") for w in k["writes"]]
    missing = [w for w in want if w not in writes]
    found = set(re.findall(r"`((?:\.suite|docs/decisions|standards/library)[^`]*)`", writes))
    extra = [f for f in found if not any(f.startswith(w.rstrip("/")) for w in want)]
    res(not missing and not extra, "SKL-08",
        "Writes matches the contract" + (f" (missing {missing})" if missing else "") + (f" (not allowed {extra})" if extra else ""))

    gate = secs.get("## Exit gate", "")
    gmiss = [g for g in k["gate"] if g not in gate]
    res(not gmiss, "SKL-09", "Exit gate cites every gate check" + (f" (missing {gmiss})" if gmiss else ""))
    if k["kind"] == "stage":
        res(k["next"] in gate, "SKL-09", f"Exit gate names the next skill '{k['next']}'")

    rules = secs.get("## Rules for this skill", "")
    rmiss = [r for r in list(k.get("must", {})) + list(k.get("must_not", {})) if r not in rules]
    res(not rmiss, "SKL-10", "Rules cite every must and must-not" + (f" (missing {rmiss})" if rmiss else ""))
    res(MARKER in text, "SKL-11", "embeds the shared core")
    common = [i for i in c.get("common", {}) if not (i == "CORE-M2" and k["kind"] == "tool")]
    cmiss = [i for i in common if i not in rules]
    res(not cmiss, "SKL-16", "Rules cite every common rule" + (f" (missing {cmiss})" if cmiss else ""))

    lmiss = [m for m in k.get("library", []) if not (d / "references" / "library" / f"{m}.md").is_file()]
    res(not lmiss, "SKL-13", "library modules present in references/library/" + (f" (missing {lmiss})" if lmiss else ""))

    ev = root / "evals" / name / "evals.md"
    if ev.is_file():
        e = ev.read_text(encoding="utf-8")
        cn = len(re.findall(r"^\| C\d+ \|", e, re.M))
        inj = len(re.findall(r"^\| I\d+ \|", e, re.M))
        res(cn >= 3 and inj >= 1, "SKL-14", f"evals: {cn} comparison and {inj} injection prompts (need 3 and 1)")
    else:
        res(False, "SKL-14", f"evals file missing: {ev.relative_to(root)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parent.parent)
    args = ap.parse_args()
    root = args.root.resolve()
    c = yaml.safe_load((root / "standards" / "contracts.yaml").read_text(encoding="utf-8"))
    results = []
    check_contracts(c, results)

    present = {p.parent.name for p in root.glob("plugins/*/skills/*/SKILL.md")}
    for name, k in c["skills"].items():
        if name in present:
            check_skill(root, name, k, c, results)
        else:
            results.append(("PENDING", "-", name, "contract written, skill not built yet"))
    for name in sorted(present - set(c["skills"])):
        repl = c.get("legacy", {}).get(name)
        if repl is None:
            results.append(("FAIL", "SKL-15", name, "skill has no contract and is not listed as legacy"))
        elif repl in present:
            results.append(("FAIL", "SKL-15", name, f"legacy skill still present after its replacement '{repl}' shipped"))
        else:
            results.append(("LEGACY", "-", name, f"until '{repl}' ships"))

    for status, rule, name, msg in results:
        print(f"{status:8} {rule:7} {name}: {msg}")
    counts = {s: sum(1 for r in results if r[0] == s) for s in ("PASS", "FAIL", "LEGACY", "PENDING")}
    print(", ".join(f"{v} {k.lower()}" for k, v in counts.items()))
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
