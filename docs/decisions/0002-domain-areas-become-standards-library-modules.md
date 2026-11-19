---
status: proposed
date: 2026-11-18
decision-makers: soilmass
---

# Domain areas become standards library modules

## Context and problem statement

CI, supply chain, observability and security were planned as separate skills (rebuild plan R3).

## Considered options

1. One versioned library with modules that stages apply
2. Keep the 0.x arrangement

## Decision outcome

Chosen option: "One versioned library with modules that stages apply".

### Consequences

- Good: one baseline for every project
- Bad: the library needs its own maintenance and versioning
