#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# Fails if any non-merge commit in BASE..HEAD lacks a Signed-off-by line from its author.
set -euo pipefail
base="$1"; head="$2"; bad=0
for c in $(git rev-list --no-merges "${base}..${head}"); do
  author="$(git log -1 --format='%an <%ae>' "$c")"
  if ! git log -1 --format='%B' "$c" | grep -qF "Signed-off-by: ${author}"; then
    echo "missing DCO sign-off by ${author}: $(git log -1 --format='%h %s' "$c")"; bad=1
  fi
done
[ "$bad" -eq 0 ] && echo "DCO: all commits signed off"
exit "$bad"
