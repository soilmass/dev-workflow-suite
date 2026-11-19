# Dev Workflow Suite

A set of Claude skills that takes a software project from idea to running system through one standard workflow, built on CNCF tooling, open standards and open source practice. Every skill shares one standard: a Project File with a charter, a standards register of BCP 14 rules, and a gate that runs after every piece of work.

This is wave 1. It ships two skills in the `dev-workflow` plugin:

- **suite-start** finds where a project stands and names the one suite skill to run next.
- **standards-baseline** writes repository security (OpenSSF OSPS Baseline), supply chain (SLSA, Sigstore, CISA SBOM), delivery (OpenGitOps), observability (OpenTelemetry), policy-as-code, licensing and agent-safety (OWASP agentic top 10) rules into a project's Project File.

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
- **Fetches:** nothing. The skills read files in your conversation and your project's repository, and write the Project File you ask for.

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
  skills/suite-start/
  skills/standards-baseline/
shared/standard.md                the shared standard (single source)
shared/consumers.txt              skills that embed it
scripts/                          maintainer tools
evals/                            eval prompts and results
```

## Licences

Code is licensed under Apache-2.0 (`LICENSE`). Documentation, including skill text, is licensed under CC-BY-4.0 (`LICENSE-docs`). Third-party notices are in `THIRD_PARTY_NOTICES.md`.

## Contributing and security

See `CONTRIBUTING.md` (every commit needs a DCO sign-off) and `SECURITY.md`.
