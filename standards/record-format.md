<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Project record format (contract version 1)

Every project run through the suite keeps its record in the repository. `scripts/validate_record.py` checks it against the REC rules below; the `suite` skill runs it before routing.

## Layout

```text
.suite/
  record.md          header, gate log, parking lot (every stage appends a gate row)
  frame.md           frame
  shape.md           shape: OUT, NEED, QUAL tables
  plan.md            plan: charter, DOD table
  rules.md           selected library rules, with the library version in front matter
  design.md          design: summary, diagrams, THR table, test strategy
  build.md           build: ITEM checklist
  verify.md          verify: FIND table
  releases/<v>.md    one per release
  operations/        SLOs, runbooks, INC reports
  retros/<date>.md   one per retro
docs/decisions/NNNN-title.md   every decision (MADR), any stage
```

## record.md header

```yaml
---
name: <project>
profile: small | standard | critical
stage: frame | shape | plan | design | build | verify | release | operate | learn | done
version: 1               # raised by one each time learn passes and a new version starts
library: vX.Y.Z
not_applicable:          # optional
  operate: "<reason>"
---
```

The gate log is a table under `## Gate log` with columns Date (ISO), Version, Stage, Result (`passed` or `blocked`), Notes. Version 1 runs every stage from frame; later versions start at plan, because frame and shape carry over unless learn reopens them. A stage that passes its gate appends its row and sets the header `stage` to the next stage (CORE-M2); REC-06 checks the two agree.

## IDs

A row's first cell holds its ID: `OUT-n`, `NEED-n`, `QUAL-n`, `DOD-n`, `ITEM-n`, `THR-n`, `FIND-n`, `INC-n`. IDs are unique across `.suite/`. Library rule IDs (for example `SEC-03`) keep their library value. Decisions are `docs/decisions/NNNN-title.md`.

## REC rules

| ID | Rule |
| --- | --- |
| REC-01 | The header MUST name the project, a valid profile, a stage and the library version; every not-applicable stage MUST give a reason. |
| REC-02 | Every stage before the current one MUST have its file, unless marked not applicable. |
| REC-03 | Every ID MUST be unique across `.suite/`. |
| REC-04 | Every NEED MUST trace to a defined OUT. |
| REC-05 | Every gate log row MUST have an ISO date, a valid stage and a result of passed or blocked. |
| REC-06 | The header stage MUST be the first stage of the current version without a passed gate. |
| REC-07 | Every decision record MUST be named `NNNN-title.md` and carry a valid status. |
| REC-08 | `rules.md` MUST name the library version, and each rule MUST hold exactly one UPPERCASE keyword. |
| REC-09 | Every THR MUST have one response: mitigate, eliminate, transfer or accept. |
| REC-10 | Every FIND MUST carry a CWE ID. |
| REC-11 | Every DOD MUST trace to a defined OUT. |
| REC-12 | Every ITEM MUST carry one status: open, passed, blocked or waived. |
| REC-13 | The header version MUST be a whole number from 1, with every gate row at or below it and each new version after a passed learn. |
