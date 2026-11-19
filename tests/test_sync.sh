#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# ITEM-02 check: --check passes after sync and fails after a one-byte change.
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

mkdir -p "$tmp/shared" "$tmp/skills/a" "$tmp/skills/b"
cp "$here/shared/standard.md" "$tmp/shared/standard.md"
printf 'skills/a\nskills/b\n' > "$tmp/shared/consumers.txt"
for s in a b; do
  printf -- '---\nname: %s\ndescription: test\n---\n# %s\n\n<!-- shared-standard:begin -->\nstale\n<!-- shared-standard:end -->\n' "$s" "$s" > "$tmp/skills/$s/SKILL.md"
done

sync="python3 -I $here/scripts/sync_standard.py --root $tmp"
fail() { echo "FAIL: $1"; exit 1; }

$sync --check >/dev/null && fail "stale copies passed --check"
$sync >/dev/null
$sync --check >/dev/null || fail "--check failed right after sync"
cmp -s <(sed -n '/shared-standard:begin/,/shared-standard:end/p' "$tmp/skills/a/SKILL.md" | sed '1d;$d') "$tmp/shared/standard.md" || fail "copy differs from source"

# change one byte in one copy
python3 -I - "$tmp/skills/b/SKILL.md" <<'EOF'
import sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
i = s.index("MUST")
open(p, "w", encoding="utf-8").write(s[:i] + "N" + s[i + 1:])
EOF
$sync --check >/dev/null && fail "one-byte change passed --check"

# a listed skill with no markers is an error
printf -- '---\nname: c\ndescription: test\n---\n' > "$tmp/skills/a/SKILL.md"
$sync --check >/dev/null 2>&1 && fail "missing markers passed --check"

echo "PASS: sync --check behaves as ITEM-02 requires"
