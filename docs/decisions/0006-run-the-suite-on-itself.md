---
status: accepted
date: 2026-11-18
decision-makers: soilmass
---

# Run the suite on itself

## Context and problem statement

The suite's own plans lived in claude.ai docs, a second record outside its rules. You said yes on 2026-11-18.

## Considered options

1. The suite repository keeps its own .suite/ record, validated in its CI
2. Keep the 0.x arrangement

## Decision outcome

Chosen option: "The suite repository keeps its own .suite/ record, validated in its CI".

### Consequences

- Good: the suite is built the way it tells others to build
- Bad: the maintainer keeps the record current
