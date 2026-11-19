---
name: explore-phase
description: Researches what experts and the industry agree on for a project's topic and records it as enforceable standards plus a charter in a Project File. Use when starting or re-scoping a project, or when asked for best practices or industry standards to build against.
license: CC-BY-4.0
metadata:
  suite: dev-workflow
  wave: "2a"
---

# Explore Phase

This skill runs the explore half of an explore/build cycle. It finds the standards for every in-scope dimension of a topic, writes them as rules that the build-phase skill can enforce, and ends with a charter the user confirms. It always ends in a decision. Open-ended exploration is a failure of this skill.

Copy this checklist and track progress:

```text
Explore progress:
- [ ] 0. Start from the baseline, if one exists
- [ ] 1. Set depth
- [ ] 2. Frame the project
- [ ] 3. Build the coverage map
- [ ] 4. Map authorities
- [ ] 5. Research
- [ ] 6. Write rules
- [ ] 7. Draft the charter
- [ ] 8. Validate the Project File
- [ ] 9. Deliver and close
```

## 0. Starting a new version

If a previous Project File exists for this project, it is the baseline.

First, name the purpose of the new version. It must be something new since the baseline: a parking-lot idea the user picks, a new requirement from the user, or defects found in use. A request like "again" is not a purpose. If no new purpose exists, say so, show the parking lot and any Proposed decisions, recommend stopping, and do not start a new version until the user names one.

Then build from the baseline. Do not start from scratch:
- Copy the baseline Project File whole, then set Version to the next number. Copy; don't retype.
- Keep the framing answers. Ask only what has changed.
- Keep carried rules as they are, unless their dimension is being re-researched or a source has been flagged.
- Keep every decision log entry with its ID. Proposed entries stay Proposed.
- Empty the build checklist and gate log. Triage the parking lot: each idea goes into scope for this version or stays parked.
- Run steps 3-8 only for new or changed dimensions.

## 1. Set depth

Scale the work to the project. A heavy process on a small project is its own kind of drift.

| Project size | Dimensions | Searches | Rules |
| --- | --- | --- | --- |
| Small (days) | 3-5 | 8-12 | 5-15 |
| Medium (weeks) | 5-8 | 12-20 | 15-35 |
| Large (months) | 8-12 | 20-30 | 35-60 |

Pick the row that fits the larger of the two: the time involved, or the number of dimensions the topic really has. On a re-run, count only new searches and new dimensions; carried-over rules still count toward the rule total. State the depth you chose in one line.

## 2. Frame the project

Ask the user, in one round (AskUserQuestion if available):
1. What are you building, and for whom?
2. What does done look like?
3. Constraints: stack, budget, skill level, existing systems.
4. Appetite: how much time is this worth?
5. What is already decided?

If the user is not available, take the most reasonable reading, state it, and mark each unknown with [NEEDS CLARIFICATION: question].

Narrow the niche to something specific enough to have experts. "Web development" is too broad; "authentication for a multi-tenant Next.js SaaS" works. Write it in one line.

## 3. Build the coverage map

"Everything relating to the topic" means every dimension that the field's experts treat as part of doing it well. Find the dimensions from:
- the section structure of the field's main standards, certifications or body-of-knowledge documents,
- the category structure of major industry surveys,
- the common failure areas named in postmortems and checklists,
- the project's own constraints.

List each dimension and mark it in or out of scope, with a reason when out. Write 1-3 research questions per in-scope dimension. Every later search serves one of these questions.

## 4. Map authorities

For each in-scope dimension, name the sources that count, by tier (see Evidence scales below). Authority is shown by evidence: the person maintains the major project, wrote the reference work, is cited by other experts, or speaks at the field's main venues. Self-description doesn't count.

Exclude or down-rate: SEO listicles, content farms, AI-generated summaries, undated posts, and unverified rewrites of official docs. Flag vendor sources as possibly biased.

## 5. Research

The consensus criteria below are fixed before research starts. Do not loosen them to fit what you find.

- **Consensus**: the normative owner of the standard says so (for example, the spec body or the tool's maintainers), or at least two independent tier 1-3 sources agree. In both cases, a deliberate search for dissent found none credible.
- **Contested**: credible tier 1-3 sources disagree.
- **Emerging**: promising, but recent, thinly sourced, or without production evidence.
- **Outdated**: once standard, now advised against by an authoritative source.

Confidence (rate down for age, vendor bias, inconsistency or indirect evidence):
- **High**: the owner of the standard, or three or more independent agreeing sources, recent and consistent.
- **Moderate**: two sources, or older or indirect evidence.
- **Low**: one source below tier 2, or conflicting signals.

Procedure:
- Search each research question separately.
- Fetch and read key pages. A search snippet is not a source.
- Record each finding with its claim, source, tier and date (follow the date rule in the Project File field rules).
- Search for dissent on purpose: "X vs Y", "problems with X", "why we moved away from X".
- In fast-moving fields, prefer sources from the last two years, and keep older foundational sources that still hold.
- Stop a dimension at saturation, when new sources only repeat known positions. Stop overall at the search budget from step 1.
- Tangents go to the parking lot.

## 6. Write rules

Turn findings into rules in the standards register:

| Finding | Becomes |
| --- | --- |
| Consensus, and violating it breaks correctness, security, legal compliance or the owner's specification | MUST / MUST NOT |
| Other consensus | SHOULD / SHOULD NOT |
| Outdated practice or anti-pattern | MUST NOT or SHOULD NOT, by the same test |
| Contested | No rule yet. Add a decision log entry with status Proposed: the options, who holds each, what the choice depends on, and a recommended default. Once the user decides, write the rule with status Decided and cite the DEC entry. |
| Emerging | MAY, or the parking lot |

Each rule must:
- contain exactly one UPPERCASE keyword,
- describe one testable behavior (if it needs "and" to join two behaviors, split it),
- have a check that is objective pass/fail and can be run with the tools available (decide how to verify a rule when you write it),
- cite at least one source with its tier and date.

Rewrite or drop any rule that fails these. Every in-scope dimension must end with at least one rule, or a note in the coverage map explaining why it has none.

## 7. Draft the charter

Fill in section 1 of the Project File:
- every DoD item is checkable,
- the appetite is a number of days, weeks or sessions,
- out of scope is explicit,
- stop criteria say when to halt and re-scope.

Write each contested choice and each open [NEEDS CLARIFICATION] marker that needs the user as a decision log entry with status Proposed, each with a recommended default. These entries are the decisions needed.

## 8. Validate the Project File

Run the Project File validation checklist from the shared standard, plus one brief check: every claim in the brief links to its source. Fix every failure and repeat. Deliver only when everything passes.

## 9. Deliver and close

Deliver one document (a Docs artifact if available, otherwise a markdown file saved as `.suite/project-file.md` in the project repository) with two parts:

1. **Exploration brief**: scope and depth, authorities by dimension, contested questions, outdated practices and anti-patterns, emerging practices, a pointer to the Proposed decisions, and sources. Aim for a 10-minute read.
2. **Project File**: sections 1, 2, 3, 5 (Proposed decisions only) and 7 filled in; sections 4 and 6 empty, for the build-phase skill.

Then close the phase:

> Explore phase complete. Confirm the decisions needed and the charter, and the build phase can start. From here, new ideas go to the parking lot unless you reopen exploration.

Do not keep researching unless the user reopens exploration. If the build-phase skill later sends a single dimension back, re-run steps 4-8 for that dimension only, and add the rule changes through a change request.

## Rules for this skill

- Attribute views to the people or bodies who hold them. Never present one expert's opinion as consensus.
- Prefer primary sources (specifications, official docs, the expert's own writing) over summaries of them.
- If the research shows the niche is framed wrong, say so and propose a re-scope instead of drifting.
- Never guess in place of a [NEEDS CLARIFICATION] marker.

<!-- shared-standard:begin -->
## Shared standard (identical in every suite skill that embeds it)

This section is the same in every suite skill that embeds it. Its source is `shared/standard.md` in the suite repository. Never edit a copy: change the source, then run `scripts/sync_standard.py`.

### Terms

Use exactly these terms. Do not substitute synonyms.

- **Project File**: the single document that holds everything below. One per project.
- **Charter**: purpose, audience, appetite, definition of done, scope and stop criteria.
- **Appetite**: the time the user is willing to spend, fixed in advance.
- **Definition of done (DoD)**: numbered, checkable outcomes (DOD-1, DOD-2, ...).
- **Coverage map**: the dimensions of the topic, each marked in or out of scope.
- **Standards register**: the table of rules for the project.
- **Rule**: one requirement with an ID, exactly one keyword, a status, a confidence, a check and sources.
- **Check**: an objective pass/fail test. If two people could disagree on the result, it is not a check.
- **Build checklist**: the ordered items that add up to the DoD (ITEM-01, ITEM-02, ...).
- **Gate**: the fixed procedure run after every item and at the end.
- **Waiver**: user-approved acceptance of a failed SHOULD rule on named work, logged.
- **Change request**: the only way to change the charter, the DoD or the standards register, apart from a minor change.
- **Minor change**: a wording, typo or formatting fix to the Project File that changes no keyword, behavior, check, scope or DoD item. It is applied without approval and logged. If in doubt, it is a change request.
- **Decision log**: the record of decisions, waivers and change requests. Open decisions are entries with status Proposed.
- **Parking lot**: ideas captured for later, not acted on.
- **Baseline**: the previous version's final Project File, which a new version starts from.
- **[NEEDS CLARIFICATION: question]**: the marker for anything unknown. Never guess in its place.

### Keywords and enforcement

Rules use the BCP 14 keywords (RFC 2119, RFC 8174), and only in UPPERCASE. The keyword alone sets enforcement:

| Keyword | Enforcement | When the check fails |
| --- | --- | --- |
| MUST / MUST NOT | Blocking | The item stays open. Only a change request can alter the rule. |
| SHOULD / SHOULD NOT | Blocking unless waived | The user may approve a waiver, logged in the decision log. |
| MAY | Advisory | Reported in the gate report. Never blocks. |

### Evidence scales

- **Status**: Consensus, Contested, Emerging, Outdated, Decided. Decided marks a rule the user set, by choosing between contested options or stating a non-negotiable; its source is the DEC entry.
- **Confidence**: High, Moderate, Low. A Decided rule takes the confidence of the evidence behind the chosen option; a user's own non-negotiable is High.
- **Source tiers**: 1 standards bodies and specifications; 2 official docs and maintainers; 3 recognized practitioners and peer-reviewed research; 4 large industry surveys and data; 5 reference implementations and engineering blogs at scale.

### Project File template

```markdown
# <Project name>: Project File

## 1. Charter
- Version: <n> (baseline: <previous Project File, or none>)
- Purpose:
- Audience:
- Appetite:
- Definition of done:
  - DOD-1: <checkable outcome>
- In scope:
- Out of scope:
- Stop criteria:

## 2. Coverage map
| Dimension | In scope? | Rule IDs | Notes |
| --- | --- | --- | --- |

## 3. Standards register
| ID | Rule | Status | Confidence | Check | Sources (tier, date) |
| --- | --- | --- | --- | --- | --- |

## 4. Build checklist
- [ ] ITEM-01: <item>. Check: <pass/fail test>. Serves: DOD-1. Rules: <IDs>

## 5. Decision log
| ID | Date | Type | Context | Decision | Consequences | Status |
| --- | --- | --- | --- | --- | --- | --- |

## 6. Gate log
| Date | Item | Result | Failed | Waived | Notes |
| --- | --- | --- | --- | --- | --- |

## 7. Parking lot
- <idea> (source, date)
```

Field rules:
- Rule IDs are a short dimension prefix plus a number: SEC-01, A11Y-02.
- Each source gives its tier and its publication or last-updated date. If the page shows no date, write "n.d., accessed <date>".
- A waiver names the rule ID and the work it covers (item IDs). The final gate honors it for that work.
- Decision log Type is one of: Decision, Waiver, Change request, Minor change. Status is one of: Proposed, Accepted, Rejected, Superseded. Superseded entries stay in the log; never delete history.
- Consequences list both the gains and the costs.

### Gate report template

```text
GATE <ITEM-ID or FINAL>: PASSED | BLOCKED
Item check: PASS | FAIL (<evidence>)
Rules: <n> applicable. MUST <n> pass, <n> fail. SHOULD <n> pass, <n> fail, <n> waived. MAY <n> noted. DEFERRED <n>.
Failures: <rule ID: what failed> | none
Scope: on scope | <out-of-scope work found and what was done with it>
Parking lot: +<n>
Next: <ITEM-ID> | <action needed from the user>
```

Each applicable rule gets one result: PASS, FAIL, N/A (does not apply to this work), or DEFERRED (can only be checked on the whole work; the final gate checks it).

A gate is PASSED only when the item check passes, no MUST rule fails, every failed SHOULD rule has a waiver, and no unresolved out-of-scope work remains. Anything else is BLOCKED.

### Project File validation

Both skills validate a Project File with this checklist. Fix every failure and run it again; continue only when everything passes.

```text
Project File validation:
- [ ] All seven sections are present, in template order
- [ ] Every in-scope dimension in the coverage map has rules or a reason for none
- [ ] Every rule states exactly one behavior with exactly one UPPERCASE keyword
- [ ] Every rule has a status, a confidence, a check and at least one source with tier and date
- [ ] No lowercase "must", "should" or "may" is used as a requirement in a rule
- [ ] Every check is objective pass/fail
- [ ] Every check can be run with the tools available; each one that can't is a Proposed decision log entry (waive, re-level, or get the tools)
- [ ] Every DoD item is checkable
- [ ] No contested finding is written as Consensus
- [ ] Every open question is a [NEEDS CLARIFICATION] marker or a Proposed decision log entry
```
<!-- shared-standard:end -->
