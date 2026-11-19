#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# Shows the enforcement tools catch what they claim to: each broken copy must fail.
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
fail() { echo "FAIL: $1"; exit 1; }
vr="python3 -I $here/scripts/validate_record.py"

# --- record validator ---
$vr "$here/tests/fixtures/record-valid" >/dev/null || fail "valid record rejected"

broken() { rm -rf "$tmp/r"; cp -r "$here/tests/fixtures/record-valid" "$tmp/r"; }
expect_fail() { if $vr "$tmp/r" >/dev/null; then fail "$1 passed the validator"; fi; }

broken; sed -i 's/ OUT-1 |$/ OUT-7 |/' "$tmp/r/.suite/shape.md"; expect_fail "orphan NEED (REC-04)"
broken; sed -i 's/^stage: design/stage: build/' "$tmp/r/.suite/record.md"; expect_fail "wrong stage (REC-06)"
broken; sed -i 's/MUST block/must block/' "$tmp/r/.suite/rules.md"; expect_fail "lowercase keyword (REC-08)"
broken; sed -i 's/^status: accepted/status: done/' "$tmp/r/docs/decisions/0001-use-postgresql.md"; expect_fail "bad decision status (REC-07)"
broken; sed -i 's/^profile: standard/profile: huge/' "$tmp/r/.suite/record.md"; expect_fail "bad profile (REC-01)"
broken; printf '| OUT-1 | dup | x | y |\n' >> "$tmp/r/.suite/plan.md"; expect_fail "duplicate ID (REC-03)"
broken; printf '\n| THR-1 | ingress | flood | |\n' >> "$tmp/r/.suite/plan.md"; expect_fail "threat without response (REC-09)"
broken; rm "$tmp/r/.suite/shape.md"; expect_fail "missing stage file (REC-02)"
broken; sed -i 's/^version: 1/version: 2/' "$tmp/r/.suite/record.md"; expect_fail "new version without a passed learn (REC-13)"
broken; sed -i 's/| 2026-11-18 | 1 | plan |/| 2026-11-18 | 3 | plan |/' "$tmp/r/.suite/record.md"; expect_fail "gate row ahead of version (REC-13)"
broken; sed -i 's/| OUT-1 |$/| OUT-5 |/' "$tmp/r/.suite/plan.md"; expect_fail "orphan DOD (REC-11)"
broken; printf '\n| ITEM-1 | scaffold | maybe |\n' >> "$tmp/r/.suite/plan.md"; expect_fail "item without status (REC-12)"

# --- skill checker ---
mk() {  # a repo copy with one skill folder named $1 built from the contract
  rm -rf "$tmp/s"; mkdir -p "$tmp/s/standards" "$tmp/s/plugins/p/skills/$1/references/library" "$tmp/s/evals/$1"
  cp "$here/standards/contracts.yaml" "$tmp/s/standards/"
  mkdir -p "$tmp/s/.suite"; cp "$here/.suite/shape.md" "$tmp/s/.suite/"
  cat > "$tmp/s/plugins/p/skills/$1/SKILL.md" <<EOF
---
name: adopt
description: Decides adopt or build. Use when adding a dependency.
license: CC-BY-4.0
metadata:
  contract: "1"
  stage: tool
---
# Adopt

## Reads
\`.suite/record.md\`, \`.suite/rules.md\`

## Writes
\`docs/decisions/\`

## Steps
1. Do it.

## Exit gate
ADOPT-G1 ADOPT-G2 ADOPT-G3

## Rules for this skill
ADOPT-M1 ADOPT-N1 ADOPT-N2 CORE-M1 CORE-N1 CORE-N2 CORE-N3

<!-- shared-standard:begin -->
<!-- shared-standard:end -->
EOF
  touch "$tmp/s/plugins/p/skills/$1/references/library/licensing.md" "$tmp/s/plugins/p/skills/$1/references/library/supply-chain.md"
  printf '| C1 | a |\n| C2 | b |\n| C3 | c |\n| I1 | d |\n' > "$tmp/s/evals/$1/evals.md"
}
cs="python3 -I $here/scripts/check_suite.py --root $tmp/s"
mk adopt; $cs >/dev/null || { $cs | grep FAIL; fail "conforming skill rejected"; }
mk adopt; sed -i 's/ADOPT-N2//' "$tmp/s/plugins/p/skills/adopt/SKILL.md"; if $cs >/dev/null; then fail "missing must-not ID passed (SKL-10)"; fi
mk adopt; sed -i 's#`docs/decisions/`#`docs/decisions/` and `.suite/plan.md`#' "$tmp/s/plugins/p/skills/adopt/SKILL.md"; if $cs >/dev/null; then fail "writing another stage's file passed (SKL-08)"; fi
mk adopt; sed -i 's/^## Steps/## How/' "$tmp/s/plugins/p/skills/adopt/SKILL.md"; if $cs >/dev/null; then fail "missing section passed (SKL-06)"; fi
mk adopt; sed -i 's/ CORE-N1//' "$tmp/s/plugins/p/skills/adopt/SKILL.md"; if $cs >/dev/null; then fail "missing common rule passed (SKL-16)"; fi
mk adopt; sed -i 's#^`.suite/record.md`, `.suite/rules.md`#`.suite/rules.md`, `.suite/record.md`#' "$tmp/s/plugins/p/skills/adopt/SKILL.md"; if $cs >/dev/null; then fail "record not read first passed (SKL-07)"; fi
mk adopt; printf 'Write the Project File.\n' >> "$tmp/s/plugins/p/skills/adopt/SKILL.md"; if $cs >/dev/null; then fail "avoided term passed (SKL-19)"; fi
mk adopt; sed -i 's/serves: \[OUT-4\]/serves: []/; s/serves: \[OUT-4\]/serves: []/' "$tmp/s/standards/contracts.yaml"; if $cs >/dev/null; then fail "unserved outcome passed (SKL-17)"; fi
mk adopt; sed -i 's/enforced_by: \[SKL-19\]/enforced_by: [SKL-99]/' "$tmp/s/standards/contracts.yaml"; if $cs >/dev/null; then fail "principle enforced by unknown rule passed (SKL-18)"; fi
mk adopt; sed -i 's/      SHAPE-G3: {small:/      SHAPE-G9: {small:/' "$tmp/s/standards/contracts.yaml"; if $cs >/dev/null; then fail "variant for unknown gate passed (SKL-20)"; fi
mk adopt; sed -i 's/record: \[OUT,/record: [ADOPT, OUT,/' "$tmp/s/standards/contracts.yaml"; if $cs >/dev/null; then fail "shared ID prefix passed (SKL-21)"; fi
mk adopt; rm "$tmp/s/.suite/shape.md"; if $cs >/dev/null; then fail "suite record without outcomes passed (SKL-17)"; fi
mk adopt; rm "$tmp/s/evals/adopt/evals.md"; if $cs >/dev/null; then fail "missing evals passed (SKL-14)"; fi
mk adopt; mkdir -p "$tmp/s/plugins/p/skills/adopt-or-build"; printf -- '---\nname: adopt-or-build\ndescription: x\n---\n' > "$tmp/s/plugins/p/skills/adopt-or-build/SKILL.md"
if $cs >/dev/null; then fail "legacy skill kept after its replacement passed (SKL-15)"; fi
mk adopt; mkdir -p "$tmp/s/plugins/p/skills/rogue"; printf -- '---\nname: rogue\ndescription: x\n---\n' > "$tmp/s/plugins/p/skills/rogue/SKILL.md"
if $cs >/dev/null; then fail "skill without contract passed (SKL-15)"; fi

echo "PASS: record validator and skill checker catch every broken case"
