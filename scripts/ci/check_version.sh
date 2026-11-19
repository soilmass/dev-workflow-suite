#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# PKG-12: on a tagged release, plugin.json version must equal the tag and differ from the previous tag's.
set -euo pipefail
manifest=plugins/dev-workflow/.claude-plugin/plugin.json
current="$(python3 -I -c 'import json,sys; print(json.load(open(sys.argv[1]))["version"])' "$manifest")"
last_tag="$(git describe --tags --abbrev=0 2>/dev/null || true)"
if [ -z "$last_tag" ]; then echo "PKG-12: no earlier tag; version ${current}"; exit 0; fi
previous="$(git show "${last_tag}:${manifest}" | python3 -I -c 'import json,sys; print(json.load(sys.stdin)["version"])')"
if [ "$(git rev-parse HEAD)" = "$(git rev-list -n1 "$last_tag")" ]; then
  [ "v${current}" = "$last_tag" ] || { echo "PKG-12: tag ${last_tag} but plugin.json says ${current}"; exit 1; }
  echo "PKG-12: tag matches version ${current}"; exit 0
fi
echo "PKG-12: version ${current}; last release ${previous} (${last_tag})"
