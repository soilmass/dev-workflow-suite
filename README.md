# Dev Workflow Suite

A set of Claude skills that takes a software project from idea to running system through one standard workflow, built on CNCF tooling, open standards and open source practice. Every skill shares one standard: a Project File with a charter, a standards register of BCP 14 rules, and a gate that runs after every piece of work.

This release (0.2.0) ships eight skills in the `dev-workflow` plugin:

| Skill | What it does |
| --- | --- |
| **suite-start** | Finds where a project stands and names the one suite skill to run next. |
| **grill-my-idea** | Interviews you about an idea, one question at a time, and writes a cited concept brief. |
| **envision-phase** | Maps everything the idea needs to be robust into a Vision Map. |
| **explore-phase** | Researches the field's standards and writes the charter and rules into a Project File. |
| **standards-baseline** | Adds repository security (OpenSSF OSPS Baseline), supply chain (SLSA, Sigstore, CISA SBOM), delivery (OpenGitOps), observability (OpenTelemetry), policy, licensing and agent-safety (OWASP agentic top 10) rules to the Project File. |
| **design-phase** | Writes decision records (MADR), C4 context and container diagrams and a four-question threat model before code. |
| **adopt-or-build** | Decides whether to adopt an open source component or build, using the OpenSSF guide for evaluating open source. |
| **build-phase** | Builds one checklist item at a time, with a gate after each that enforces the Project File. |

The usual order is grill-my-idea, envision-phase, explore-phase (with standards-baseline), design-phase (with adopt-or-build), build-phase. Coming next: ci-pipeline and security-review.

## Install

In Claude Code:

```text
/plugin marketplace add soilmass/dev-workflow-suite
/plugin install dev-workflow@dev-workflow-suite
```

Then run `/dev-workflow:suite-start` in your project.

## What this plugin runs, sends and fetches

- **Runs:** nothing. The plugin contains only skills (markdown). It has no hooks, MCP servers, scripts or package installs.
- **Sends:** nothing. Neither skill sends data anywhere.
- **Fetches:** nothing by itself. Some skills ask Claude to look up public information with its own web tools: grill-my-idea and explore-phase research sources, and adopt-or-build reads public package data (for example deps.dev, osv.dev and the OpenSSF Scorecard API). Skills read files in your conversation and repository and write the suite files you ask for under `.suite/` and `docs/decisions/`.

The `scripts/` folder at the repository root holds maintainer tools (`sync_standard.py`, `check_skills.py`, `validate_project_file.py`). They are not part of the installed plugin; they read and write local files only.

## Recommended permissions

The suite never needs to push, publish or delete on its own. You can make that a hard limit, enforced by Claude Code rather than by the skills, with deny rules in `.claude/settings.json`:

```json
{
  "permissions": {
    "deny": [
      "Bash(git push:*)",
      "Bash(gh release create:*)",
      "Bash(npm publish:*)",
      "Bash(rm -rf:*)"
    ]
  }
}
```

## Repository layout

```text
.claude-plugin/marketplace.json   marketplace manifest
plugins/dev-workflow/             the installable plugin
  .claude-plugin/plugin.json
  skills/<skill>/                 one folder per skill
shared/standard.md                the shared standard (single source)
shared/consumers.txt              skills that embed it
scripts/                          maintainer tools
evals/                            eval prompts and results
```

## Licences

Code is licensed under Apache-2.0 (`LICENSE`). Documentation, including skill text, is licensed under CC-BY-4.0 (`LICENSE-docs`). Third-party notices are in `THIRD_PARTY_NOTICES.md`.

## Contributing and security

See `CONTRIBUTING.md` (every commit needs a DCO sign-off) and `SECURITY.md`.
