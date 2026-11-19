# Baseline catalog

The rules standards-baseline draws from. Each entry is a template: keep its keyword, ID prefix, source and check, and fit the check to the project's tools. Source keys (S-…) are defined in `sources.md`.

Columns: **Applies when** names the project profile answers (step 2 of the skill) that switch the entry on.

## SEC: repository security (OpenSSF OSPS Baseline v2026.08.28)

Every SEC rule cites its OSPS control ID. Controls at or below the project's target level become MUST rules. Controls one level above become MAY rules. Higher levels are left out and noted in the coverage map.

| OSPS ID | Level | Requirement (rule text) | Applies when | Check (GitHub; adapt for other hosts) |
| --- | --- | --- | --- | --- |
| OSPS-AC-01.01 | 1 | Sensitive resources in the repository require multi-factor authentication. | always | Org setting "Require 2FA" on (`gh api orgs/<org>`), or host equivalent |
| OSPS-AC-02.01 | 1 | New collaborators get manual or least-privilege default permissions. | always | Org base permission is `read` or `none` |
| OSPS-AC-03.01 | 1 | The primary branch blocks direct commits. | always | Branch protection or ruleset requires pull requests |
| OSPS-AC-03.02 | 1 | Deleting the primary branch requires explicit confirmation. | always | Ruleset blocks deletion |
| OSPS-BR-01.01 | 1 | CI sanitizes and validates untrusted metadata (branch names, PR titles) before use. | has CI | No `${{ github.event.* }}` interpolated directly in `run:` steps (zizmor or grep) |
| OSPS-BR-01.03 | 1 | Untrusted code snapshots cannot reach privileged CI credentials. | has CI | No `pull_request_target` job that checks out PR code with secrets |
| OSPS-BR-03.01 | 1 | Official project URLs use encrypted channels. | always | Every project URL in README and metadata is `https://` |
| OSPS-BR-03.02 | 1 | Official distribution channels are cryptographically authenticated. | ships releases | Release channel is HTTPS or signed registry |
| OSPS-BR-07.01 | 1 | Unencrypted secrets are kept out of version control. | always | `gitleaks detect` over full history reports 0 |
| OSPS-DO-01.01 | 1 | Release documentation includes user guides for all basic functionality. | ships releases | README or docs has a usage section per command or feature |
| OSPS-DO-02.01 | 1 | Release documentation includes a defect reporting guide. | ships releases | README or CONTRIBUTING says how to report bugs |
| OSPS-GV-02.01 | 1 | The project has a public place to discuss changes and usage problems. | public repo | Issues or discussions enabled |
| OSPS-GV-03.01 | 1 | The contribution process is documented, or the project states it takes no contributions. | always | CONTRIBUTING.md exists |
| OSPS-LE-02.01 | 1 | The source licence meets the OSI or FSF definition. | open source | LICENSE matches an OSI-approved SPDX ID |
| OSPS-LE-02.02 | 1 | Released assets carry an OSI- or FSF-approved licence. | ships releases, open source | Release licence matches an OSI-approved SPDX ID |
| OSPS-LE-03.01 | 1 | The source licence is kept in the repository's licence file or folder. | always | `LICENSE` or `LICENSES/` exists |
| OSPS-LE-03.02 | 1 | The licence ships alongside release assets. | ships releases | Release archive contains the licence |
| OSPS-QA-01.01 | 1 | The source repository is publicly readable at a static URL. | public repo | URL returns 200 without sign-in |
| OSPS-QA-01.02 | 1 | A public record of changes, authors and timestamps is kept. | public repo | Public git history |
| OSPS-QA-02.01 | 1 | Direct language dependencies are listed where the ecosystem supports it. | has dependencies | Manifest file present (package.json, go.mod, pyproject.toml, …) |
| OSPS-QA-04.01 | 1 | Multi-repository projects list their codebases. | multi-repo | README lists every repository |
| OSPS-QA-05.01 | 1 | Generated executable artefacts are kept out of version control. | always | No compiled binaries tracked (`git ls-files` by type) |
| OSPS-QA-05.02 | 1 | Unreviewable binary artefacts are kept out of version control. | always | `git ls-files` lists no binary file outside `.binary-allowlist` |
| OSPS-VM-02.01 | 1 | Project documentation names security contacts. | always | SECURITY.md names a contact |
| OSPS-AC-04.01 | 2 | CI task permissions default to the lowest level when unspecified. | has CI | Repo default workflow permission is `read` |
| OSPS-BR-02.01 | 2 | Each official release has a unique version identifier. | ships releases | Tags are unique semantic versions |
| OSPS-BR-04.01 | 2 | Each release includes a log of functional and security changes. | ships releases | CHANGELOG or release notes entry per tag |
| OSPS-BR-05.01 | 2 | Build and release pipelines ingest dependencies with standard tooling. | has CI | Builds use the ecosystem package manager with a lockfile |
| OSPS-BR-06.01 | 2 | Each release is signed, or listed in a signed manifest with hashes. | ships releases | Signature verifies (see SUP) |
| OSPS-DO-06.01 | 2 | Docs say how dependencies are selected, obtained and tracked. | has dependencies | CONTRIBUTING or docs section present |
| OSPS-DO-07.01 | 2 | Docs give build instructions with required tools and dependencies. | always | Build section present |
| OSPS-GV-01.01 | 2 | Members with access to sensitive resources are listed. | always | MAINTAINERS or GOVERNANCE file lists them |
| OSPS-GV-01.02 | 2 | Member roles and responsibilities are described. | always | GOVERNANCE file describes roles |
| OSPS-GV-03.02 | 2 | A contributor guide states requirements for acceptable contributions. | always | CONTRIBUTING lists requirements |
| OSPS-LE-01.01 | 2 | Contributors assert legal authorization for each commit. | takes contributions | DCO check passes on every PR (see GOV) |
| OSPS-QA-03.01 | 2 | Automated status checks pass, or are manually bypassed, before commits reach the primary branch. | has CI | Required status checks set |
| OSPS-QA-06.01 | 2 | At least one automated test suite runs before a commit is accepted. | has CI | Test job is a required check |
| OSPS-SA-01.01 | 2 | Design documentation shows system actions and actors. | always | Design doc present |
| OSPS-SA-02.01 | 2 | All external software interfaces of released assets are described. | ships releases | Interface or API doc present |
| OSPS-SA-03.01 | 2 | Each release gets a security assessment of likely and impactful problems. | ships releases | Assessment linked from release notes |
| OSPS-VM-01.01 | 2 | A coordinated disclosure policy with a response time is published. | always | SECURITY.md states a response time |
| OSPS-VM-03.01 | 2 | A private vulnerability reporting method exists. | always | Private reporting enabled, or SECURITY.md gives a private channel |
| OSPS-VM-04.01 | 2 | Data about discovered vulnerabilities is published. | ships releases | Advisories published for fixed vulnerabilities |

Level 3 controls (OSPS-AC-04.02, BR-01.04, BR-02.02, BR-07.02, DO-03.01, DO-03.02, DO-04.01, DO-05.01, GV-04.01, QA-02.02, QA-04.02, QA-06.02, QA-06.03, QA-07.01, SA-03.02, VM-04.02, VM-05.01 to 05.03, VM-06.01, VM-06.02) are used only when the target level is 3. Read their text from S-OSPS before writing them.

## SUP: supply chain

| ID | Rule text | Applies when | Check | Source |
| --- | --- | --- | --- | --- |
| SUP-a | Release artefacts SHOULD have SLSA provenance from a hosted build platform (Build L2). | ships releases | `slsa-verifier verify-artifact` passes | S-SLSA |
| SUP-b | Release artefacts SHOULD be signed. At target level 2 or higher, write OSPS-BR-06.01 as a MUST SEC rule instead, not both. | ships releases | `cosign verify` / `verify-blob` with expected identity passes | S-OSPS, S-SIG |
| SUP-c | Every SBOM the project produces MUST include each component's hash and hash algorithm. | produces SBOM | Script finds both fields on every component | S-CISA |
| SUP-d | Every SBOM the project produces MUST list transitive dependencies. | produces SBOM | Component count equals lockfile resolved count | S-CISA |
| SUP-e | Every SBOM the project produces SHOULD include each component's licence. | produces SBOM | Licence field present on every component | S-CISA |
| SUP-f | CI actions and base images SHOULD be pinned by digest or full commit SHA. | has CI | Scorecard Pinned-Dependencies passes | S-SC |
| SUP-g | Signatures and SBOMs for images SHOULD be attached with OCI 1.1 `subject` referrers. | ships containers | `oras discover` lists them | S-OCI |

Contested, so a Proposed decision in the project's Project File, never a rule until decided:
- **Must every release ship an SBOM?** Suite default: yes for releases that ship compiled code or containers; no for docs-only releases. Note that OSPS-QA-02.02 requires it at level 3.
- **Keyless or key-based signing?** Suite default: Sigstore keyless for public releases; KMS-held keys for private ones.

## DEL: delivery (applies when the project deploys a running system)

| ID | Rule text | Check | Source |
| --- | --- | --- | --- |
| DEL-a | Deployed config MUST NOT reference mutable tags such as `latest`. | grep deployment manifests for `:latest` or untagged images | S-OGO |
| DEL-b | The desired state of the system SHOULD be declared in version-controlled files. | Every deployed resource has a manifest in the repo | S-OGO |
| DEL-c | Desired state SHOULD be stored versioned and immutable. | Releases reference tags or digests, never branches | S-OGO |
| DEL-d | An agent SHOULD pull desired state automatically from the source. | A GitOps controller (for example Argo CD or Flux) is configured | S-OGO |
| DEL-e | An agent SHOULD continuously reconcile actual state with desired state. | Controller sync is automatic, with drift detection on | S-OGO |

## OBS: observability (applies when the project runs a service)

| ID | Rule text | Check | Source |
| --- | --- | --- | --- |
| OBS-a | Services SHOULD emit traces, metrics and logs through OpenTelemetry. | An OTel SDK or Collector config is present | S-OTEL |
| OBS-b | Telemetry SHOULD follow the stable OpenTelemetry semantic conventions. | Attribute names match the stable conventions | S-OTEL |
| OBS-c | The project MAY use the GenAI semantic conventions, which are still in Development status. | Reported only | S-OTEL |

## POL: policy as code

| ID | Rule text | Applies when | Check | Source |
| --- | --- | --- | --- | --- |
| POL-a | Policy checks SHOULD run as code in CI. | has CI | A CI job runs a policy engine over config | S-KYV |

Contested, so a Proposed decision: **which engine?** Suite default: Kyverno for Kubernetes admission; OPA (conftest) for CI checks on non-Kubernetes config.

## GOV: licences and contributions

| ID | Rule text | Applies when | Check | Source |
| --- | --- | --- | --- | --- |
| GOV-a | Each commit SHOULD carry a DCO `Signed-off-by:` line (meets OSPS-LE-01.01). Write it only once the DCO-or-CLA decision picks DCO, with status Decided. | takes contributions | DCO check passes on every PR | S-DCO |
| GOV-b | Text or code adapted from another project MUST keep its licence notices. | reuses third-party code | Third-party notices file lists each source | licence terms of the reused work |

Contested, so a Proposed decision when the project takes outside contributions: **DCO or CLA?** Suite default: DCO.

## SAFE: agent safety (applies when the project includes an LLM agent or tool-calling model)

Every SAFE rule cites its OWASP ASI ID.

| ID | ASI | Rule text | Check | Source |
| --- | --- | --- | --- | --- |
| SAFE-a | ASI01 | The agent MUST NOT act on instructions found in untrusted content without user confirmation. | Injection test: a planted instruction is not followed | S-ASI |
| SAFE-b | ASI02 | Each agent tool SHOULD be limited to an allowlist of operations. | Tool config lists allowed operations | S-ASI |
| SAFE-c | ASI03 | Agent credentials SHOULD be scoped to the task and short-lived. | No long-lived broad token in agent config | S-ASI |
| SAFE-d | ASI04 | Agent tools, plugins and MCP servers MUST be pinned to exact versions. | Config has no ranges or `latest` | S-ASI |
| SAFE-e | ASI05 | Code the agent generates MUST run only in a sandbox. | Execution path goes through a sandbox | S-ASI |
| SAFE-f | ASI06 | Writes to agent memory SHOULD be validated before they are stored. | Memory write path has a validation step | S-ASI |
| SAFE-g | ASI09 | Irreversible agent actions MUST require explicit human confirmation. | Each delete, publish, send or spend path asks first | S-ASI |

ASI07 (inter-agent communication), ASI08 (cascading failures) and ASI10 (rogue agents) apply to multi-agent systems; when the profile says so, read S-ASI and write one rule each.
