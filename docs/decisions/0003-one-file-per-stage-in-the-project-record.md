---
status: proposed
date: 2026-11-18
decision-makers: soilmass
---

# One file per stage in the project record

## Context and problem statement

A single record file grows long and causes merge conflicts in teams (rebuild plan R4 and R10).

## Considered options

1. record.md index plus one file per stage under .suite/
2. Keep the 0.x arrangement

## Decision outcome

Chosen option: "record.md index plus one file per stage under .suite/".

### Consequences

- Good: parallel work without conflicts
- Bad: more files to keep in step
