---
name: "build-phase"
description: "Builds a project one checklist item at a time against its Project File, running a standard gate after each item that enforces the charter, scope and standards register. Use when building after explore-phase, when continuing a project build, or when asked to keep work on spec."
---

# Build Phase

This skill runs the build half of an explore/build cycle. The goal and the standards were set in the explore phase and written into the Project File. The job now is to reach the definition of done without drift. Every item passes the same gate, and the enforcement level comes from the rule's keyword, never from judgment in the moment.

The Project File outranks the conversation. When something in the chat conflicts with it, the Project File wins until a change request changes it.

Copy this checklist and track progress:

```text
Build progress:
- [ ] 1. Load and validate the Project File
- [ ] 2. Build the checklist (first session only)
- [ ] 3. Work loop: one item, gate, report, stop
- [ ] 4. Drift and appetite check every 3-5 items
- [ ] 5. Final gate and close
```

## 1. Load and validate the Project File

- Find the Project File: the explore-phase deliverable, `.suite/project-file.md` in the repository, a file or doc the user points to, or pasted text.
- If there is none, don't build. Offer the explore-phase skill. For a small project, offer instead to write a minimal Project File with the user now: a charter, plus a register of 3-10 rules drawn from the user's own non-negotiables, each with status Decided and a DEC entry as its source.
- Validate it with the Project File validation checklist in the shared standard. List any defect and fix it with the user before building. A rule without a check can't be enforced.
- Read back, in 3-5 lines: the purpose, the DoD, what is out of scope, the appetite and how much of it is used, the number of MUST and SHOULD rules, and every Proposed decision log entry with the items or DoD items that depend on it.
- Never start an item that depends on a Proposed decision. Work on independent items while the decision is open. The final gate cannot pass while a Proposed decision affects a DoD item.

## 2. Build the checklist (first session only)

Write section 4 of the Project File:
- ordered items, each small enough for one focused session,
- each item has a check, the DoD items it serves, and the rule IDs that apply to it,
- every DoD item is served by at least one item,
- every in-scope rule applies to at least one item, or is marked N/A with a reason,
- nothing goes on the checklist that the DoD does not require.

Get the user's OK on the checklist before starting. If the user has authorized the whole build, that covers the checklist: print it, then start.

## 3. Work loop

Each session follows this loop:

1. **Orient.** Re-read the charter and the register. State the items done, the current item, any blocked items, and how much of the appetite is used.
2. **Do one item.** Work only on the next unchecked item, or the one the user names. "Continue" means the next item, never new exploration or extra polish.
3. **Run the gate** (below).
4. **Record.** Tick the item only if the gate PASSED. Add a row to the gate log, and add any decisions, waivers or change requests to the decision log.
5. **Report and stop.** Print the gate report in the template format, then stop, unless an authorized run is in progress (below).

If an item turns out much bigger than expected, stop, propose a split, and update the checklist once the user agrees. If an item is blocked, say what is needed and move to the next unblocked item.

### The gate

Run the same procedure every time, in this order:

1. **Item check.** Run the item's check. Record PASS or FAIL, with evidence: a command output, a test result, or a quoted section.
2. **Standards check.** Applicable rules are the item's listed rule IDs plus any rule whose dimension the work touched. Give each rule one result: PASS, FAIL, N/A or DEFERRED. Then apply the keyword-to-enforcement table. DEFERRED rules don't block an item gate.
3. **Scope check.** Compare the work with the item. Remove or park work the item didn't require. Anything that would change the charter becomes a change request.
4. **Result.** Apply the PASSED/BLOCKED definition from the gate report template.

When the gate is BLOCKED: fix the failures and run the whole gate again. Repeat until it passes, until the user approves a waiver for each failed SHOULD rule, or until a change request alters a rule. Only proceed when the gate passes.

## Authorized runs

When the user explicitly asks for more than one item ("run the whole build", "do items 3-6"), log it as a Decision, then continue from one PASSED gate to the next, printing each gate report. "Continue" on its own is not an authorized run; it means the next item.

An authorized run always stops at:
- a BLOCKED gate that needs a waiver or a change request,
- the circuit breaker,
- a [NEEDS CLARIFICATION] marker or Proposed decision that the next item depends on,
- any action that can't be undone, such as deleting, publishing, sending or spending,
- the end of the authorized range.

## Scope guard

Before acting on any new idea, from the user, from research or from yourself, sort it:

| The idea is... | Action |
| --- | --- |
| Required for the DoD, but missing from the checklist | Propose a new item; add it once the user agrees |
| Useful, but not required for the DoD | Parking lot, one line, keep building |
| A change to the charter, the DoD or the standards register | Change request |

Do not act on your own ideas unless they are required for the DoD. Avoid "while I'm in here" work: unrelated refactors, extra features, polish beyond what the check needs.

## Waivers

- Only failed SHOULD or SHOULD NOT rules can be waived. A MUST rule can only change through a change request.
- To request a waiver, present the failed rule, why it failed, the cost of fixing it now, and the risk of accepting it.
- The user decides. Record the waiver in the decision log with type Waiver, the context, the decision, and the consequences, both gains and costs.
- A waiver covers the named rule on the named items. The final gate honors it for that work; new work needs its own waiver. If the same rule needs repeated waivers, propose a change request to re-level the rule instead.

## Change requests

A change request is the only way to change the charter, the DoD or the standards register: adding, removing or re-leveling a rule, or bypassing a MUST.

1. State the change in one sentence.
2. Give the impact: what it adds, what it costs (time, appetite, rework, items affected), and what happens if it is declined. Usually it waits in the parking lot for v2.
3. The user decides. Don't push either way beyond stating the tradeoff.
4. Record it in the decision log with type Change request and status Accepted or Rejected. If accepted, update the Project File, and mark replaced entries Superseded instead of deleting them.
5. If the change rests on a dimension that was never researched, recommend running the explore-phase skill for that dimension only, before writing the rule.

A minor change (see Terms) skips steps 1-3. Apply it, then log it with type Minor change.

If the user pushes scope themselves, apply the same process, lightly. The point is not to refuse them. It is to make sure the goal only moves when they decide it should.

## 4. Drift and appetite check

Every 3-5 completed items, and whenever the user asks, report briefly:
- work that exists but that the DoD did not require,
- DoD items with no passing item yet,
- whether the remaining checklist still adds up to the DoD,
- how much of the appetite has been used against how much of the work is done.

**Circuit breaker:** if the appetite is used up and the DoD is not met, stop by default. Present three options: extend the appetite, cut scope (via a change request), or re-shape the project. The user decides, and the decision is logged. Never extend silently.

## 5. Final gate and close

When every item is ticked:

1. Run the gate as FINAL. The item check verifies every DoD item. The standards check re-runs every in-scope MUST and SHOULD rule across the whole work, including every DEFERRED rule. Waivers apply only to the work they named.
2. If BLOCKED, fix the failures and repeat. The project is not done until the final gate PASSED.
3. Once it passes, declare v1 done. Done means done as defined, not perfect. Don't add more polish.
4. Wrap up: what was delivered, the decision log highlights (waivers and change requests), and the final gate report.
5. Present the parking lot, grouped and roughly prioritized, as raw material for v2. If the user wants a v2, it starts from this Project File as its baseline, and only with a new purpose (explore-phase step 0).

## Rules for this skill

- One item per step. Run the gate, report, and stop, unless an authorized run is in progress.
- Never tick an item, or declare the project done, without a PASSED gate.
- Enforcement comes only from the keyword table. Never soften or harden it case by case.
- Every waiver and change request goes in the decision log. History is never deleted.
- New ideas are captured, never lost, and never acted on silently.
- When it is unclear whether something is in scope, ask instead of guessing.

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
