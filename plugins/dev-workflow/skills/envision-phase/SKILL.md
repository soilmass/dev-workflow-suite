---
name: "envision-phase"
description: "Turns a confirmed idea in any field into a Vision Map, a complete, vision-traced map of what the thing needs to be robust. Use when a confirmed idea needs its full depth mapped, after grill-my-idea and before explore-phase."
---

# Envision Phase

This skill sits between grill-my-idea and explore-phase. Grill-my-idea tested whether the idea is worth doing. This skill works out everything the idea needs in order to be robust and true to its vision, and writes it into a Vision Map. Explore-phase then researches the standards for each dimension the Vision Map names.

The core promise: nothing the vision needs is left unexamined, and nothing in the map lacks a reason. Every item traces up to an outcome, and every outcome is served.

Copy this checklist and track progress:

```text
Envision progress:
- [ ] 1. Intake and depth
- [ ] 2. Vision and outcomes
- [ ] 3. Stakeholders
- [ ] 4. Context, regulations and constraints
- [ ] 5. Lifecycle
- [ ] 6. Scenarios
- [ ] 7. Capability tree
- [ ] 8. Qualities
- [ ] 9. Robustness
- [ ] 10. Needs and glossary
- [ ] 11. Trace
- [ ] 12. Validate the Vision Map
- [ ] 13. Deliver and hand off
```

## How each layer runs

Steps 2-11 are layers. Run every layer the same way, one round per layer:

1. **Draft.** Fill the layer's section of the Vision Map from the grill brief, earlier layers and what the field usually needs. Mark every new item **Candidate**.
2. **Hunt for gaps.** Before showing the draft, look for what is missing. AI drafts tend to miss less than people on business rules, state changes, exception handling and validation, so check those four on purpose, including two people acting on the same thing at once. People are usually better on actors, workflows and data, so ask about those.
3. **List unknowns.** End every Vision Map section the layer filled with a line `Unknowns:` naming what is still missing or unclear, or "none". Do this as a separate pass after drafting, not while drafting.
4. **Show and ask.** Show the layer to the user in one message: the draft, the unknowns, and any question for the user, each with a recommended answer where one exists. Ask for accept, edit or reject per item, or "accept all". Write each question under its Vision Map section as `Q<section>.<n>`, with the answer once given. Every choice question is also logged in section 16 as a Proposed decision (PD-n): Accepted once answered, Proposed while open.
5. **Record.** Set each item to **Accepted**, **Edited** or **Rejected**, citing the user's turn. An item the user did not review stays Candidate.

Statuses:

- **Imported**: copied from the grill brief; cite the brief, not a turn.
- **Open**: a [NEEDS CLARIFICATION] marker the user must answer. An item that still contains a marker stays Candidate, even after "accept all".
- **Research pending**: a fact research could settle but this run did not confirm (for example, a rule with no primary source read). It is not a question for the user; the Handoff sends it to explore-phase.
- **Candidate**, **Accepted**, **Edited** (the user changed it), **Rejected** (kept for history; also used for orphans moved to the parking lot).
- If a later layer must change the meaning of an item that is already Accepted, set it back to Candidate and show it again in that layer's round. Wording-only renames from the glossary pass keep their status.
- Every table row and every list item in sections 3-16 of the Vision Map has a status, including regulations, losses, resilience rows, unspoken basics, glossary terms, Detail lines and premortem answers. `Q` lines and `100% check` lines don't need one.

Three kinds of gaps, three responses:

- **A choice only the user can make** (goals, scope, money, audience, risk appetite): ask, with a recommended answer. Don't assume. If the user is not available, keep the item Candidate and leave its Proposed decision (PD-n) at Proposed with the recommended default.
- **A fact only the user holds** (their location, their budget, their existing tools): ask, with no recommended answer. If the user is not available, or answers "accept all" without giving it, write [NEEDS CLARIFICATION: question]. Never invent it.
- **A fact research can settle** (rules, regulations, typical numbers): look it up rather than ask.

Other rules for every layer:

- Never mark an item Accepted on your own. AI-proposed items are candidates until the user accepts them.
- New ideas outside the vision, including ideas dropped while drafting, go straight to the parking lot section, one line each.

## 1. Intake and depth

Look for a grill-my-idea brief: the user names it, attaches it, or it is earlier in the conversation. If there is one, read it fully and copy into section 2 of the Vision Map its job statement, concept statement, decisions, riskiest assumptions and premortem, and use its Handing off section as the framing. Don't ask again about anything the brief settled, and don't redo its risks or premortem.

If there is no brief, offer two paths and recommend the first:
- run grill-my-idea first, or
- answer five framing questions now, in one round: what it is and for whom; the problem it solves; what done looks like; constraints (money, time, skills, rules); and the appetite.

Set the depth from the appetite and state it in one line:

| Appetite | Depth | Outcomes | Capabilities | Needs |
| --- | --- | --- | --- | --- |
| Days | Small | 1-2 | 5-10 | 10-25 |
| Weeks | Medium | 2-4 | 10-20 | 25-60 |
| Months | Large | 3-5 | 20-40 | 60-120 |

The counts are upper limits, not targets. Capabilities count every level of the tree; Rejected and parking-lot items don't count. Depth limits how many items exist and how far they are detailed, never which sections are covered. Every section of the Vision Map is filled at every depth. Go deep only on needs tagged **decide now** (step 10).

Create the Vision Map from `references/vision-map-template.md`. Use the format the user or caller names; otherwise a Docs artifact if available, otherwise a markdown file saved as `.suite/vision-map.md` in the project repository.

Use these ID prefixes: OUT (outcomes), CON (constraints), SCN (scenarios), CAP (capabilities), QUAL (qualities), LOSS (losses), NEED (needs), PD (Proposed decisions).

## 2. Vision and outcomes

- Write the vision as exactly one sentence naming the positive change the thing creates. It names no feature, product type or other solution, so it survives changes of approach.
- Write desired outcomes (OUT-1, OUT-2, ...), as many as the depth table allows. Each has a measure and a target value, such as "repeat bookings, 40% within 90 days".

## 3. Stakeholders

Walk every slot in `references/stakeholder-slots.md`. For each slot, write a named role or "none" with a reason. Never leave the Maintenance operator or Operational support rows blank. Mark each role primary or secondary.

- A slot with several roles gets one row per role, each labeled with the slot.
- A person who fills several slots appears in each row, with "(also: <slots>)".
- A role is **present** if it is named. If a later step shows a named role is not really involved, set its row to Rejected with the reason.

## 4. Context, regulations and constraints

- Draw the boundary: list what is inside the thing, and every interfacing system outside it. Every Interfacing system stakeholder appears in the outside list.
- List the laws, licences, regulations, standards and insurance that apply, including insurance the field expects even where no law requires it. Look them up for the field and place. If the place is unknown, look up the likely rules for at most two probable places, chosen from clues in the brief (currency, spelling, named institutions) and named as a guess, label each "if <place>", and write [NEEDS CLARIFICATION: question] for the place itself. A rule counts as confirmed only when you have read the regulator's or another primary source page; record that source in the Confirmed column. Mark each rule you can't confirm **Research pending**, not as a question for the user.
- If a rule may conflict with a decision from the grill brief, don't overturn the decision. Add a Proposed decision marked "may conflict with D<n>", with the options and a recommended default.
- Record constraints (budget, time, skills, mandated choices) in their own section, apart from needs, each with its source.

## 5. Lifecycle

Fill five stages: set up, operate, maintain and support, change, retire. Each gets at least one concept, or "N/A" with a reason. Retirement is the stage most often forgotten: what happens to data, stock, people or commitments at the end?

## 6. Scenarios

Scenarios come before needs, because needs written without a shared picture of use tend to conflict.

- Write at least one nominal scenario for each primary stakeholder role.
- Write off-nominal scenarios under three tags, at least one each: **failure** (something breaks), **misuse** (someone uses it wrongly or with bad intent), **overload or degraded** (too much demand, or running with parts missing).

## 7. Capability tree

Break the outcomes into capabilities (CAP-1, CAP-2, ...), each with a parent outcome or capability.

- **100% rule:** at every level, the children must cover all of their parent and nothing outside scope. For an outcome, judge against the behavior behind its measure. After the table, list each parent as `<ID>: 100% check: pass` once that holds. If it fails, add the missing child or move the extra one to the parking lot.
- Each capability has exactly one parent in the tree, so nothing is counted twice. If it also helps other outcomes, record those links in the trace (step 11), which allows many links.
- Each top-level capability names its actor and the behavior change it enables, such as "Organizers can confirm a venue in one day".

## 8. Qualities

Use `references/quality-checklists.md`. Pick the list by its selection rule and mark every item relevant, or not relevant with a reason.

When both lists are used, write each scenario once and mark the overlapping item on the other list "covered by QUAL-n".

Write each relevant quality as a six-part scenario: source, stimulus, environment, artifact, response, response measure. Every response measure holds a number, a threshold or an observable pass/fail condition. Never accept an adjective such as "fast", "secure" or "easy" as a measure.

List at least three unspoken basics (what users take for granted and only notice when missing), or "none" with a reason.

## 9. Robustness

1. **Losses first.** Name the losses stakeholders will not accept, such as injury, lost money, a broken promise or lost trust (LOSS-1, ...).
2. **Failure modes.** For every capability at every level, give at least one way it fails or is misused, the loss it threatens, and the planned response.
3. **Resilience.** Say how the thing will respond to trouble, monitor for early signs, anticipate what is coming, and learn from what happened. Each ability points to a need, or is "N/A" with a reason.
4. **Vision premortem (optional).** This is not the grill brief's premortem, which asked why the idea failed. Ask: "A year on, it was built exactly as this map says, yet it missed the vision. Why?" Each answer that reveals a gap becomes a new Candidate item in the right section. If you skip it, write "Not run" and the reason.

## 10. Needs and glossary

Turn the earlier layers into needs (NEED-1, ...):

- Each need states one capability, characteristic, constraint or quality. A need may carry the conditions and thresholds of its one behavior ("within 2 hours, between 07:00 and 22:00"). If two things happen, split it: "A concern suspends the tutor and is acknowledged within 2 hours" becomes two needs, one for the suspension and one for the acknowledgement. Lists of what a single record contains count as one behavior.
- Every need, decide now or defer, has an acceptance condition an observer can check.
- Needs stay free of solutions. A need that names a product, brand or technology carries its source in the Constraint source column and is listed by ID in the Constraints section. Naming a standard to pass (such as an accessibility level) is an acceptance condition, not a solution.
- Tag each need **decide now** if changing it later would be costly (money spent, contracts, structure, safety, legal), otherwise **defer**. For decide-now needs, add a Detail line under the table. Leave defer needs short.
- Run a consistency pass: look for needs that conflict, overlap, or use different units or terms for the same thing. Write the result on a `Consistency:` line: the conflicts found and how they were resolved, or "none".

Keep a glossary with one term per concept. Every domain term in the vision and outcomes appears in it. Then run a rename pass so every earlier section uses the glossary terms.

## 11. Trace

Fill the trace table in both directions:

- **Up:** every capability and need traces to at least one outcome. A child capability lists the outcome its branch serves plus any others it helps. An item that traces to none is an orphan. Resolve each orphan: either the user approves a new outcome it serves, or it goes to the parking lot.
- **Down:** every outcome is served by at least one need. If one is not, add the missing need as a Candidate.
- **Stakeholders:** every role marked present traces to at least one need. For hostile agents and regulators, a defensive or compliance need counts. If one doesn't, ask whether a need is missing or the role is not really present.

## 12. Validate the Vision Map

Run this checklist. Fix every failure and run it again. Continue only when everything passes. Record each run in the Validation record section: what failed and what was fixed. Record run 1 as what the checklist itself found, not fixes made earlier during the layers. Before the checklist, collect every open marker, research-pending item and Proposed decision into section 16 and end it with an `Unknowns:` line.

```text
Vision Map validation:
- [ ] Every section of the template is filled, or "N/A" with a reason
- [ ] The vision is one sentence and names no solution
- [ ] Every outcome has a measure and a target
- [ ] Every stakeholder slot has a role or "none" with a reason
- [ ] All five lifecycle stages are filled
- [ ] Every primary role has a nominal scenario; failure, misuse and overload or degraded each have one
- [ ] Every parent capability shows "100% check: pass"; no capability has two parents
- [ ] Every checklist quality is marked; every relevant quality has six parts and a measurable response
- [ ] At least one loss is listed; every capability has a failure mode with a response; all four resilience abilities are covered
- [ ] Singular-need pass done: every need containing "and", "or" or a list of verbs was read, and any with two things happening was split
- [ ] Every need has an acceptance condition and a tag; the Consistency line is present
- [ ] The trace has no orphans and no unserved outcomes
- [ ] Every item has a status; no Accepted item lacks a cited user turn
- [ ] Every layer ends with an Unknowns line
- [ ] Every open question is a [NEEDS CLARIFICATION] marker or a Proposed decision with a recommended default
```

## 13. Deliver and hand off

Fill the Handoff section:

- **Candidate dimensions for explore-phase:** at least three, each linked to the Vision Map items that need research, such as "Food safety (LOSS-2, NEED-14, Regulations)". Prefer the dimensions behind decide-now needs and regulations. List every research-pending item under the dimension that should settle it.
- **Framing answers:** what and for whom, done looks like, constraints, appetite, already decided. These line up with explore-phase's framing questions. Update them with what envisioning settled (outcome IDs, constraint IDs, accepted decisions), not just the brief's wording.

Then close the phase, both in chat and as the last line of the Vision Map. Name only the counts that are above zero. Count each item once: a Candidate item that holds a marker counts as a marker, not as a Candidate.

> Envision phase complete. Confirm the <n> Proposed decisions, answer the <n> open markers and review the <n> Candidate items, and explore-phase can start from the Handoff section, which also carries the <n> research-pending items. From here, new ideas go to the parking lot unless you reopen envisioning.

If all three counts are zero:

> Envision phase complete. Everything is confirmed, and explore-phase can start from the Handoff section. From here, new ideas go to the parking lot unless you reopen envisioning.

Do not keep expanding the map after delivery unless the user reopens it.

## Rules for this skill

- Use these terms exactly: Vision Map, outcome, capability, need, scenario, quality, loss, Imported, Open, Research pending, Candidate, Accepted, Edited, Rejected, decide now, defer, parking lot, Proposed decision, [NEEDS CLARIFICATION: question].
- Never guess in place of a [NEEDS CLARIFICATION] marker.
- If the work shows the vision itself is framed wrong (for example, it can't be served without harming a primary stakeholder), say so and propose re-running grill-my-idea instead of drifting.

