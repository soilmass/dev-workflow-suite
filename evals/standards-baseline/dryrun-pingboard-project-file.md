# pingboard: Project File

## 1. Charter
- Version: 1 (baseline: none)
- Purpose: Ship v1 of pingboard, a self-hosted status page for the team's 5 services.
- Audience: The team that runs the 5 services, and anyone contributing to the public repo.
- Appetite: 4 weeks.
- Definition of done:
  - DOD-1: [NEEDS CLARIFICATION: what must pingboard show or do for v1 to count as done?]
  - DOD-2: Every MUST rule in section 3 passes, and every failed SHOULD rule has a logged waiver.
- In scope: the pingboard service, its CI, its container image and its Kubernetes deployment.
- Out of scope: [NEEDS CLARIFICATION: anything you already know v1 will not include?]
- Stop criteria: stop and re-scope if the 4 weeks are used up and the DoD is not met.

## 2. Coverage map
| Dimension | In scope? | Rule IDs | Notes |
| --- | --- | --- | --- |
| SEC: repository security | Yes | SEC-01 to SEC-42 | Profile: public repo, open source (MIT), takes contributions, GitHub Actions CI, ships releases, single repo. Target level Proposed (DEC-01), so Level 1 is MUST and Level 2 is MAY. Level 3 left out. OSPS-QA-04.01 left out: single repository. |
| SUP: supply chain | Yes | SUP-01 to SUP-04 | Ships releases and container images to GHCR. SBOM rules wait on DEC-02; signing model on DEC-03. |
| DEL: delivery | Yes | DEL-01 to DEL-05 | Deploys to Kubernetes (`k8s/deployment.yaml`). |
| OBS: observability | Yes | OBS-01, OBS-02 | Runs an HTTP service. GenAI conventions left out: no LLM in the project. |
| POL: policy as code | Yes | POL-01 | Engine choice waits on DEC-04. |
| GOV: licences and contributions | Yes | none | MIT licence is covered by SEC rules (OSPS-LE). DCO rule waits on DEC-05. No reused third-party text found. |
| SAFE: agent safety | No | none | No LLM agent or tool-calling model in the project. |

## 3. Standards register
| ID | Rule | Status | Confidence | Check | Sources (tier, date) |
| --- | --- | --- | --- | --- | --- |
| SEC-01 | The project MUST meet OSPS-AC-01.01: sensitive resources in the repository require multi-factor authentication. | Consensus | High | Org setting "Require 2FA" on (`gh api orgs/<org>`), or host equivalent | OSPS Baseline OSPS-AC-01.01 (1, v2026.08.28) |
| SEC-02 | The project MUST meet OSPS-AC-02.01: new collaborators get manual or least-privilege default permissions. | Consensus | High | Org base permission is `read` or `none` | OSPS Baseline OSPS-AC-02.01 (1, v2026.08.28) |
| SEC-03 | The project MUST meet OSPS-AC-03.01: the primary branch blocks direct commits. | Consensus | High | Branch protection or ruleset requires pull requests | OSPS Baseline OSPS-AC-03.01 (1, v2026.08.28) |
| SEC-04 | The project MUST meet OSPS-AC-03.02: deleting the primary branch requires explicit confirmation. | Consensus | High | Ruleset blocks deletion | OSPS Baseline OSPS-AC-03.02 (1, v2026.08.28) |
| SEC-05 | The project MUST meet OSPS-BR-01.01: cI sanitizes and validates untrusted metadata (branch names, PR titles) before use. | Consensus | High | No `${{ github.event.* }}` value interpolated in a `run:` step of `.github/workflows/*.yml` (`zizmor .` reports 0 template-injection findings) | OSPS Baseline OSPS-BR-01.01 (1, v2026.08.28) |
| SEC-06 | The project MUST meet OSPS-BR-01.03: untrusted code snapshots cannot reach privileged CI credentials. | Consensus | High | No `pull_request_target` job that checks out PR code with secrets | OSPS Baseline OSPS-BR-01.03 (1, v2026.08.28) |
| SEC-07 | The project MUST meet OSPS-BR-03.01: official project URLs use encrypted channels. | Consensus | High | Every project URL in README and metadata is `https://` | OSPS Baseline OSPS-BR-03.01 (1, v2026.08.28) |
| SEC-08 | The project MUST meet OSPS-BR-03.02: official distribution channels are cryptographically authenticated. | Consensus | High | Images are pulled from `ghcr.io` over HTTPS and releases from GitHub Releases | OSPS Baseline OSPS-BR-03.02 (1, v2026.08.28) |
| SEC-09 | The project MUST meet OSPS-BR-07.01: unencrypted secrets are kept out of version control. | Consensus | High | `gitleaks detect` over full history reports 0 | OSPS Baseline OSPS-BR-07.01 (1, v2026.08.28) |
| SEC-10 | The project MUST meet OSPS-DO-01.01: release documentation includes user guides for all basic functionality. | Consensus | High | README or docs has a usage section per command or feature | OSPS Baseline OSPS-DO-01.01 (1, v2026.08.28) |
| SEC-11 | The project MUST meet OSPS-DO-02.01: release documentation includes a defect reporting guide. | Consensus | High | README or CONTRIBUTING says how to report bugs | OSPS Baseline OSPS-DO-02.01 (1, v2026.08.28) |
| SEC-12 | The project MUST meet OSPS-GV-02.01: the project has a public place to discuss changes and usage problems. | Consensus | High | Issues or discussions enabled | OSPS Baseline OSPS-GV-02.01 (1, v2026.08.28) |
| SEC-13 | The project MUST meet OSPS-GV-03.01: the contribution process is documented, or the project states it takes no contributions. | Consensus | High | CONTRIBUTING.md exists | OSPS Baseline OSPS-GV-03.01 (1, v2026.08.28) |
| SEC-14 | The project MUST meet OSPS-LE-02.01: the source licence meets the OSI or FSF definition. | Consensus | High | LICENSE matches an OSI-approved SPDX ID | OSPS Baseline OSPS-LE-02.01 (1, v2026.08.28) |
| SEC-15 | The project MUST meet OSPS-LE-02.02: released assets carry an OSI- or FSF-approved licence. | Consensus | High | Release licence matches an OSI-approved SPDX ID | OSPS Baseline OSPS-LE-02.02 (1, v2026.08.28) |
| SEC-16 | The project MUST meet OSPS-LE-03.01: the source licence is kept in the repository's licence file or folder. | Consensus | High | `LICENSE` or `LICENSES/` exists | OSPS Baseline OSPS-LE-03.01 (1, v2026.08.28) |
| SEC-17 | The project MUST meet OSPS-LE-03.02: the licence ships alongside release assets. | Consensus | High | Release archive contains the licence | OSPS Baseline OSPS-LE-03.02 (1, v2026.08.28) |
| SEC-18 | The project MUST meet OSPS-QA-01.01: the source repository is publicly readable at a static URL. | Consensus | High | URL returns 200 without sign-in | OSPS Baseline OSPS-QA-01.01 (1, v2026.08.28) |
| SEC-19 | The project MUST meet OSPS-QA-01.02: a public record of changes, authors and timestamps is kept. | Consensus | High | Public git history | OSPS Baseline OSPS-QA-01.02 (1, v2026.08.28) |
| SEC-20 | The project MUST meet OSPS-QA-02.01: direct language dependencies are listed where the ecosystem supports it. | Consensus | High | `go.mod` present and lists direct dependencies | OSPS Baseline OSPS-QA-02.01 (1, v2026.08.28) |
| SEC-21 | The project MUST meet OSPS-QA-05.01: generated executable artefacts are kept out of version control. | Consensus | High | No compiled binaries tracked (`git ls-files` by type) | OSPS Baseline OSPS-QA-05.01 (1, v2026.08.28) |
| SEC-22 | The project MUST meet OSPS-QA-05.02: unreviewable binary artefacts are kept out of version control. | Consensus | High | `git ls-files` lists no binary file outside `.binary-allowlist` | OSPS Baseline OSPS-QA-05.02 (1, v2026.08.28) |
| SEC-23 | The project MUST meet OSPS-VM-02.01: project documentation names security contacts. | Consensus | High | SECURITY.md names a contact | OSPS Baseline OSPS-VM-02.01 (1, v2026.08.28) |
| SEC-24 | The project MAY meet OSPS-AC-04.01 ahead of its target level: cI task permissions default to the lowest level when unspecified. | Consensus | High | Repo default workflow permission is `read` | OSPS Baseline OSPS-AC-04.01 (1, v2026.08.28) |
| SEC-25 | The project MAY meet OSPS-BR-02.01 ahead of its target level: each official release has a unique version identifier. | Consensus | High | Tags are unique semantic versions | OSPS Baseline OSPS-BR-02.01 (1, v2026.08.28) |
| SEC-26 | The project MAY meet OSPS-BR-04.01 ahead of its target level: each release includes a log of functional and security changes. | Consensus | High | CHANGELOG or release notes entry per tag | OSPS Baseline OSPS-BR-04.01 (1, v2026.08.28) |
| SEC-27 | The project MAY meet OSPS-BR-05.01 ahead of its target level: build and release pipelines ingest dependencies with standard tooling. | Consensus | High | CI builds with `go build` using `go.mod`/`go.sum` | OSPS Baseline OSPS-BR-05.01 (1, v2026.08.28) |
| SEC-28 | The project MAY meet OSPS-BR-06.01 ahead of its target level: each release is signed, or listed in a signed manifest with hashes. | Consensus | High | Signature verifies (see SUP) | OSPS Baseline OSPS-BR-06.01 (1, v2026.08.28) |
| SEC-29 | The project MAY meet OSPS-DO-06.01 ahead of its target level: docs say how dependencies are selected, obtained and tracked. | Consensus | High | CONTRIBUTING or docs section present | OSPS Baseline OSPS-DO-06.01 (1, v2026.08.28) |
| SEC-30 | The project MAY meet OSPS-DO-07.01 ahead of its target level: docs give build instructions with required tools and dependencies. | Consensus | High | Build section present | OSPS Baseline OSPS-DO-07.01 (1, v2026.08.28) |
| SEC-31 | The project MAY meet OSPS-GV-01.01 ahead of its target level: members with access to sensitive resources are listed. | Consensus | High | MAINTAINERS or GOVERNANCE file lists them | OSPS Baseline OSPS-GV-01.01 (1, v2026.08.28) |
| SEC-32 | The project MAY meet OSPS-GV-01.02 ahead of its target level: member roles and responsibilities are described. | Consensus | High | GOVERNANCE file describes roles | OSPS Baseline OSPS-GV-01.02 (1, v2026.08.28) |
| SEC-33 | The project MAY meet OSPS-GV-03.02 ahead of its target level: a contributor guide states requirements for acceptable contributions. | Consensus | High | CONTRIBUTING lists requirements | OSPS Baseline OSPS-GV-03.02 (1, v2026.08.28) |
| SEC-34 | The project MAY meet OSPS-LE-01.01 ahead of its target level: contributors assert legal authorization for each commit. | Consensus | High | DCO check passes on every PR (see GOV) | OSPS Baseline OSPS-LE-01.01 (1, v2026.08.28) |
| SEC-35 | The project MAY meet OSPS-QA-03.01 ahead of its target level: automated status checks pass, or are manually bypassed, before commits reach the primary branch. | Consensus | High | Required status checks set | OSPS Baseline OSPS-QA-03.01 (1, v2026.08.28) |
| SEC-36 | The project MAY meet OSPS-QA-06.01 ahead of its target level: at least one automated test suite runs before a commit is accepted. | Consensus | High | Test job is a required check | OSPS Baseline OSPS-QA-06.01 (1, v2026.08.28) |
| SEC-37 | The project MAY meet OSPS-SA-01.01 ahead of its target level: design documentation shows system actions and actors. | Consensus | High | Design doc present | OSPS Baseline OSPS-SA-01.01 (1, v2026.08.28) |
| SEC-38 | The project MAY meet OSPS-SA-02.01 ahead of its target level: all external software interfaces of released assets are described. | Consensus | High | Interface or API doc present | OSPS Baseline OSPS-SA-02.01 (1, v2026.08.28) |
| SEC-39 | The project MAY meet OSPS-SA-03.01 ahead of its target level: each release gets a security assessment of likely and impactful problems. | Consensus | High | Assessment linked from release notes | OSPS Baseline OSPS-SA-03.01 (1, v2026.08.28) |
| SEC-40 | The project MAY meet OSPS-VM-01.01 ahead of its target level: a coordinated disclosure policy with a response time is published. | Consensus | High | SECURITY.md states a response time | OSPS Baseline OSPS-VM-01.01 (1, v2026.08.28) |
| SEC-41 | The project MAY meet OSPS-VM-03.01 ahead of its target level: a private vulnerability reporting method exists. | Consensus | High | Private reporting enabled, or SECURITY.md gives a private channel | OSPS Baseline OSPS-VM-03.01 (1, v2026.08.28) |
| SEC-42 | The project MAY meet OSPS-VM-04.01 ahead of its target level: data about discovered vulnerabilities is published. | Consensus | High | Advisories published for fixed vulnerabilities | OSPS Baseline OSPS-VM-04.01 (1, v2026.08.28) |
| SUP-01 | Release artefacts SHOULD have SLSA provenance from a hosted build platform. | Consensus | High | `slsa-verifier verify-image ghcr.io/example/pingboard@<digest>` passes | SLSA v1.2 levels (1, n.d., accessed 2026-11-18) |
| SUP-02 | Release artefacts SHOULD be signed. | Consensus | High | `cosign verify ghcr.io/example/pingboard@<digest>` with the expected identity passes | OSPS Baseline OSPS-BR-06.01 (1, v2026.08.28); Sigstore overview (2, n.d., accessed 2026-11-18) |
| SUP-03 | CI actions and base images SHOULD be pinned by digest or full commit SHA. | Consensus | High | Scorecard Pinned-Dependencies passes | OpenSSF Scorecard (2, n.d., accessed 2026-11-18) |
| SUP-04 | Image signatures and SBOMs SHOULD be attached with OCI 1.1 `subject` referrers. | Consensus | High | `oras discover ghcr.io/example/pingboard@<digest>` lists them | OCI v1.1 (1, 2024-03-13) |
| DEL-01 | Deployed config MUST NOT reference mutable tags such as `latest`. | Consensus | High | `grep -rn ':latest' k8s/` finds none | OpenGitOps 1.0 (1, 2021-11-08) |
| DEL-02 | The desired state of the system SHOULD be declared in version-controlled files. | Consensus | High | Every resource in the cluster namespace has a manifest in `k8s/` | OpenGitOps 1.0 (1, 2021-11-08) |
| DEL-03 | Desired state SHOULD be stored versioned and immutable. | Consensus | High | Manifests reference image tags with versions or digests, never branches | OpenGitOps 1.0 (1, 2021-11-08) |
| DEL-04 | An agent SHOULD pull desired state automatically from the repository. | Consensus | High | An Argo CD or Flux application points at `k8s/` | OpenGitOps 1.0 (1, 2021-11-08) |
| DEL-05 | An agent SHOULD continuously reconcile actual state with desired state. | Consensus | High | The application has automated sync and drift detection on | OpenGitOps 1.0 (1, 2021-11-08) |
| OBS-01 | The service SHOULD emit traces, metrics and logs through OpenTelemetry. | Consensus | High | `go.mod` requires `go.opentelemetry.io/otel` and the service exports to a Collector | OpenTelemetry blog (2, 2026) |
| OBS-02 | Telemetry SHOULD follow the stable OpenTelemetry semantic conventions. | Consensus | High | HTTP span attributes use stable `http.*` names | OpenTelemetry blog (2, 2026) |
| POL-01 | Policy checks SHOULD run as code in CI. | Consensus | Moderate | A CI job runs a policy engine over `k8s/` | CNCF Kyverno graduation (2, 2026-03-24) |

## 4. Build checklist

Empty. The build-phase skill writes it.

## 5. Decision log
| ID | Date | Type | Context | Decision | Consequences | Status |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-01 | 2026-11-18 | Decision | Which OSPS Baseline level to target. | Recommended: Level 2, since the repo is public and ships releases. Until decided, Level 1 rules are MUST and Level 2 rules are MAY. | Gain: release signing, changelogs, disclosure policy. Cost: about 19 more controls to meet. | Proposed |
| DEC-02 | 2026-11-18 | Decision | Must every release ship an SBOM (contested)? | Recommended: yes, since releases ship a compiled binary in a container. Then add the CISA hash, transitive and licence rules. | Gain: meets CISA 2026 minimum elements. Cost: one more release step. | Proposed |
| DEC-03 | 2026-11-18 | Decision | Keyless or key-based signing (contested)? | Recommended: Sigstore keyless from GitHub Actions OIDC. | Gain: no key storage. Cost: signer identity is public in Rekor. | Proposed |
| DEC-04 | 2026-11-18 | Decision | Which policy engine (contested)? | Recommended: Kyverno for cluster admission, OPA with conftest for the CI job. | Gain: fits both cluster and CI. Cost: two tools. | Proposed |
| DEC-05 | 2026-11-18 | Decision | DCO or CLA for outside contributions (contested)? | Recommended: DCO, checked on every PR. | Gain: lightweight, LF and CNCF norm. Cost: no relicensing rights. | Proposed |
| DEC-06 | 2026-11-18 | Decision | SEC-01 and SEC-02 need org-admin read access to check. | Recommended: run them with a token that has `read:org`, at the final gate. | Gain: both checks become runnable. Cost: needs an org admin once. | Proposed |

## 6. Gate log

Empty. The build-phase skill fills it.

## 7. Parking lot
- Already found while profiling: `ci.yml` interpolates the PR title in a `run:` step (fails SEC-05); `k8s/deployment.yaml` uses `:latest` (fails DEL-01); actions are pinned by tag, not SHA (fails SUP-03). For build-phase, not fixed here. (standards-baseline dry run, 2026-11-18)
