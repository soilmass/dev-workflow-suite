# Decision record template

The suite's default follows the section structure of MADR 4.0.0 (adr.github.io/madr, 2024-09-17), which extends Michael Nygard's 2011 form (title, status, context, decision, consequences). Save each record as `docs/decisions/NNNN-title-with-dashes.md`, numbered in order.

Required parts are marked. Keep each record to one decision and about one page.

```markdown
---
status: proposed            # required: proposed | accepted | rejected | deprecated | superseded by NNNN
date: YYYY-MM-DD            # required
decision-makers: <names>    # who accepts it
---

# <Short title naming the problem and the chosen solution>   (required)

## Context and problem statement   (required)

<Two to four sentences: the situation, the forces at play, and the question being decided. Link the Vision Map qualities, losses or needs that drive it.>

## Decision drivers

- <quality, constraint or need, with its Vision Map or register ID>

## Considered options   (required)

1. <option>
2. <option>

## Decision outcome   (required)

Chosen option: "<option>", because <the drivers it best meets>.

### Consequences   (required)

- Good: <gain>
- Bad: <cost or risk>

### Confirmation

<How the build will show the decision was implemented: a test, a check, a review step.>

## Pros and cons of the options

### <option>

- Good: <...>
- Bad: <...>

## More information

<Links: superseded records, adopt-or-build records, issues.>
```

Rules:

- A record moves to `accepted` only when the user accepts it in their own words.
- An accepted record's decision is never edited. Write a new record and set the old status to `superseded by NNNN`.
- A record that adds a dependency links the adopt-or-build record behind it.
