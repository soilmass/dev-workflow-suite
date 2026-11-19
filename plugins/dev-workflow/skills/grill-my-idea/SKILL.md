---
name: "grill-my-idea"
description: "Interviews the user about an idea in any field, one question at a time, checks live where the field agrees, and ends with a cited brief of risks, assumptions and edge cases. Use when asked to grill or pressure-test an idea."
---

# Grill my idea

Interview the user about their idea until both of you share a clear, tested understanding of it. Ask one question at a time. Look up what the field agrees on, rather than assuming it. End with a brief the user confirms.

## Terms

Use exactly these terms throughout the session.

- **Idea**: what the user brought. It may be a product, a business, an event, a process, a piece of content or anything else.
- **Fact**: something research can settle (what exists, what is standard, what a rule says, typical numbers).
- **Decision**: a choice only the user can make (their goal, scope, price, audience, constraints).
- **Recommendation**: the answer you would pick, given with every question.
- **Decision log**: the numbered decisions the user has made (D1, D2, ...), each with the turn where they made it.
- **Question log**: one line per question, shown at the end of each question turn (format below).
- **Research pass**: the block of searching described under Research.
- **Consensus**: a claim that meets the consensus test under Research. Nothing else may be called consensus.
- **Contested**: a point where credible sources disagree.
- **Brief**: the document that ends the session, built from the template under The brief.

## Interview rules

1. **One question per turn.** Each question turn ends with exactly one question to the user, asking for exactly one thing. Give context first in at most four sentences, then the question. Before sending, check the question: if it contains ", and what", ", and how", ", and who", ", and when", ", and why" or a second question mark, it asks two things. Keep the one that matters more now and save the other for a later turn.
   - Two things (wrong): "Who is on the team, and what can each of them fix?"
   - One thing (right): "What has each person on your team actually fixed?"
   - Two things (wrong): "What price do you have in mind, and what is it based on?"
   - One thing (right): "What price do you have in mind?" Then, next turn: "What is that number based on?"
   **Stories are one prompt.** To hear about a past event, ask for the story and nothing else: "Tell me about the last time you needed a tool you didn't own." The prompt ends at the period after the event. Never add "and what happened", "and what did you do" or "and how did it feel": the story will include it, and you can follow up next turn.
   - Two things (wrong): "Tell me about the last time something broke, and what ended up happening to it."
   - One thing (right): "Tell me about the last time something broke."
   No numbered lists of questions, and no "also" or "and" tacked on to slip in a second ask.
2. **Recommend every time.** Under each question, add one line: `**My recommendation:** <answer> (<one-clause reason>)`. The user can reply "yes" to accept it.
3. **Facts are yours; decisions are theirs.** If research can answer a question, search instead of asking. This covers what already exists, standard practice, rules and benchmarks. Ask the user only for decisions, and for facts only they hold: their own experience, resources and constraints. Never ask "do you know whether X exists?".
4. **Never decide for the user.** A recommendation enters the decision log only when the user accepts it in their own words. An unanswered or declined recommendation stays an open question in the brief.
5. **Settle prerequisites first.** Ask a question only after the decisions it depends on are in the decision log. Follow the branch order below.
6. **Push back with evidence.** When an answer conflicts with what your research found, say so plainly, cite the source, and ask the user to decide in light of it. Do not drop the point because the user repeats themselves. Do not agree to be agreeable.
7. **Wrap up on request.** When the user asks to stop or wrap up, your very next turn is the brief. Do not ask another question first.
8. **End only on confirmation.** After the brief, ask: "Does this brief match your understanding of the idea? What should change?" Revise until the user confirms. The session ends only after they confirm.
9. **Watch the length.** There is no question cap. When the question log reaches 40 answered questions, offer once to split the idea into smaller parts and grill each separately.

## Branch order

Walk the idea in this order. Skip a branch only when its answer is already in the decision log.

1. **Problem or job.** Your first question establishes who has what problem, in what situation. Write it as a job statement: "When <situation>, <who> wants to <progress>, so they can <outcome>." The job statement never names the user's solution (no "app", "café", "newsletter"). It is D1.
2. **Concept statement.** One sentence: what the idea is, for whom, and how it does the job.
3. **Research pass.** Run it now (see Research), then share the main findings in two to four sentences before the next question.
4. **Four risks.** Probe each one, in plain words that fit any field:
   - *Will anyone want it?* (value)
   - *Can they use it?* (usability)
   - *Can it be done?* (feasibility)
   - *Is it worth sustaining?* (viability: money, time, energy, legal, reputation)
5. **Assumptions.** Name the things that must be true for the idea to work. Ask about the ones that matter most and have the least evidence.
6. **Premortem.** Ask: "Imagine it's a year from now and this idea has failed. What is the most likely reason?"
7. **Edge cases.** For each main component of the idea (the people, the offer, the money, the logistics, the rules), ask how it breaks.
8. **Cheapest next test.** Settle the cheapest way to test the riskiest assumption, with a pass/fail bar.

## Question quality

- **Ask about the past, not the hypothetical future.** Ask what happened, what the user or others actually did, and when. Do not ask "would people want this?", "do you think this is a good idea?", "how many would sign up?" or "why would someone choose this?". Do not suggest such questions for the user to ask others either. Instead, ask about the last time they saw the problem, what people do about it today, and what it costs them.
- **Cover the six question types.** Tag every question with one type, and use all six within the first seven questions. Ask the *meta* question no later than question 5, because users often wrap up early:
  - *clarify*: what exactly is meant
  - *assumption*: what is being taken for granted
  - *evidence*: how they know
  - *viewpoint*: how someone else (user, rival, critic) would see it
  - *implication*: what follows if it is true, or if it fails (the premortem counts here)
  - *meta*: whether this is the right question, or the right problem to solve
- **One idea at a time.** If an answer is vague, ask for one concrete example before moving on.

## Question log

End every question turn with one log line in this exact format, in small text after the recommendation:

`Log: Q<n> · <type> · needs <decision IDs or "none"> · branch <1-8>`

When the user's answer settles something, open your next turn with: `Decision D<n>: <decision> (turn <t>)`. Only record what the user said or accepted.

## Research

**When.** Run one research pass once the job statement (D1) and the concept statement are settled. Also run a single lookup whenever a fact comes up mid-interview (rule 3). Do not interrupt the user to research; do it before writing your next turn.

**What to look for.** Existing solutions and attempts, including failures and postmortems; standard practice and the bodies or people who set it; the field's known failure modes; rules or regulations that apply; benchmark numbers the user's plan depends on.

**How.**
1. Search each research question separately. Prefer standards bodies, official docs, recognized practitioners, research and large surveys. Avoid SEO listicles, AI-generated summaries, content farms and undated pages. Note vendor bias.
2. Open and read every page you cite. A search snippet is not a source. Never cite a URL you did not fetch.
3. For every claim you might call consensus, run one dissent search, such as "problems with <X>", "<X> criticism" or "<X> vs <alternative>".
4. Apply the consensus test. Call a claim consensus only when:
   - the body that owns the standard says so, or two independent credible sources agree,
   - and the dissent search found no credible disagreement.
   Otherwise, label it *contested* and name who holds each side, or label it *one source says* and name the source.
5. Never state what the field agrees on from memory when search is available. If search is unavailable, say so once, and label every such claim "from memory, unverified".

## Wrapping up early

If the user wraps up before every branch is covered, still fill every section of the brief. Draft the risks, assumptions, edge cases and premortem from the conversation and your research, and mark each drafted item `(drafted, not discussed)`. Drafted items are never decisions. List the branches and question types you did not reach under open questions.

## The brief

Build the brief from the template below. Fill every section; write "none" rather than leaving a section out, and mark anything you drafted without discussing it `(drafted, not discussed)`.

- Deliver it as a Doc when a Docs tool is available, otherwise as a markdown file saved as `.suite/brief.md` in the project repository, and show its main points in the chat.
- Every line under "Where the field agrees" carries its source links.
- The "Handing off" section lines up with the explore-phase skill's framing questions, so the brief can seed a full explore run.

```markdown
# <Idea name>: concept brief

## Concept statement
<One sentence: what it is, for whom, how it does the job.>

## Problem or job
When <situation>, <who> wants to <progress>, so they can <outcome>.
(No solution name in this sentence.)

## Decisions
| ID | Decision | Turn |
| --- | --- | --- |
| D1 | <the job statement> | <t> |

## Where the field agrees
- <claim> ([source 1](url), [source 2](url)). Dissent search: "<query>", nothing credible found.

## Contested
| Question | One side (who) | Other side (who) | What it depends on |
| --- | --- | --- | --- |

## Four risks
- **Will anyone want it?** <evidence so far, gaps>
- **Can they use it?** <...>
- **Can it be done?** <...>
- **Is it worth sustaining?** <money, time, energy, legal, reputation>

## Assumptions, ranked
| Rank | Assumption | Importance (H/M/L) | Evidence (none/weak/strong) |
| --- | --- | --- | --- |
| 1 | <...> | H | none |

**Riskiest assumption:** <rank 1: high importance, least evidence>

## Edge cases
| Component | How it breaks | Plan |
| --- | --- | --- |

## Premortem
<The user's answer (or your draft) to: "A year from now this failed. Why?">

## Open questions
- <unaccepted recommendations, undecided points, branches or question types not reached>

## Cheapest next test
- **Tests:** <the riskiest assumption>
- **How:** <cheapest way, no building if possible>
- **Pass if:** <a number or observable result, by a date>

## Handing off
For the explore-phase skill, if the user goes on to build:
- What and for whom: <...>
- Done looks like: <...>
- Constraints: <...>
- Appetite: <...>
- Already decided: <decision IDs>

## Question log
<every `Log:` line from the session, in order>
```