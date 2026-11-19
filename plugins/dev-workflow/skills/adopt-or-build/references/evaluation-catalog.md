# Evaluation catalog

Organised by the sections of the OpenSSF Concise Guide for Evaluating Open Source Software (Best Practices Working Group, 2025-03-28; best.openssf.org). Checks are paraphrased; read the guide for its full wording. **Gate** checks decide eligibility; the rest inform the recommendation.

For each check record: the finding, the source (URL or command), and the date looked up.

## 1. Initial assessment

| Check | Gate? | How to look it up |
| --- | --- | --- |
| Necessity: can existing code, the standard library or a current dependency do this instead? | (step 2 of the skill) | Read the project's dependency manifest and docs |
| Authenticity: official source, not a fork or an attacker's copy | Gate | Project website links to the repository; package registry names that repository; creation date and popularity make sense |

## 2. Maintenance and sustainability

| Check | Gate? | How to look it up |
| --- | --- | --- |
| Significant commits in the last 12 months | Gate (or written reason) | Repository commit history |
| A release in the last 12 months | Gate (or written reason) | Releases page or registry |
| More than one maintainer, ideally from different organisations | | Contributors and maintainer files |
| Version signals stability (not 0.x, alpha or beta) | | Registry version string |
| Maintainers communicate (release notes, announcements) | | Releases, discussions |

## 3. Security practices

| Check | Gate? | How to look it up |
| --- | --- | --- |
| No known unfixed critical or high vulnerability in the version to adopt | Gate | osv.dev or deps.dev for the exact version |
| OpenSSF Best Practices badge earned or in progress | | bestpractices.dev |
| OpenSSF Scorecard score (one input only) | | deps.dev or api.securityscorecards.dev |
| Dependencies reasonably up to date | | deps.dev dependency view |
| Hosting security features used, such as branch protection | | Scorecard Branch-Protection detail |
| Security bugs fixed promptly; older releases patched or an LTS line exists | | Advisories and release history |
| Automated tests run in CI | | CI configuration, Scorecard CI-Tests |
| Security audits done and findings fixed | | Project docs, OpenSSF security reviews list |

## 4. Usability and security

| Check | Gate? | How to look it up |
| --- | --- | --- |
| The interface is easy to use securely (for example parameterised queries) | | API docs and examples |
| Defaults and examples are secure | | Docs and default configuration |
| Guidance on secure use exists | | Docs |
| Instructions for reporting vulnerabilities exist | | SECURITY.md |
| The interface is stable, or breaking changes follow a stated policy | | Changelog, versioning policy |

## 5. Adoption and licensing

| Check | Gate? | How to look it up |
| --- | --- | --- |
| SPDX licence is OSI-approved and compatible with the project's licence | Gate | Repository licence file; compare with the project licence (for example GPL code cannot go into an Apache-2.0 distribution without care) |
| No more popular look-alike name (typosquatting) | (part of authenticity) | Registry search |
| Significant use by others | | Registry download counts, dependents on deps.dev |
| Fits the problem, not chosen for hype | | Compare with the need from step 1 |

## 6. Practical testing (only with the user's go-ahead, in an isolated sandbox)

| Check | Gate? | How to look it up |
| --- | --- | --- |
| Adding it shows no unexpected behaviour (network calls, file access) | | Sandbox run |
| It adds no unnecessary production dependencies | | Resolved dependency tree |

## 7. Code evaluation

| Check | Gate? | How to look it up |
| --- | --- | --- |
| No signs of incomplete or insecure code (for example many TODOs in security paths) | | Code reading |
| No suspicious install scripts, obfuscated code or reads of secrets and environment variables | | Package contents, install hooks |
| Secure practices visible (input validation, parameterised statements) | | Code reading |
| Top static-analysis findings | | A static analyser run in a sandbox |
| Its own tests pass | | Sandbox run |
