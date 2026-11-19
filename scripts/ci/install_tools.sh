#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# Installs the check tools at exact versions, verifying the gitleaks download.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
pip install --quiet --require-hashes -r "$here/requirements.txt"
npm ci --prefix "$here/tools" --no-audit --no-fund
echo "$here/tools/node_modules/.bin" >> "${GITHUB_PATH:-/dev/null}"
GL_VERSION=8.28.0
GL_SHA256=a65b5253807a68ac0cafa4414031fd740aeb55f54fb7e55f386acb52e6a840eb
tmp="$(mktemp -d)"
curl -sSfL -o "$tmp/gl.tgz" "https://github.com/gitleaks/gitleaks/releases/download/v${GL_VERSION}/gitleaks_${GL_VERSION}_linux_x64.tar.gz"
echo "${GL_SHA256}  $tmp/gl.tgz" | sha256sum --check --quiet
tar -xzf "$tmp/gl.tgz" -C "$tmp" gitleaks
sudo install "$tmp/gitleaks" /usr/local/bin/gitleaks
