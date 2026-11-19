---
status: accepted
date: 2026-11-18
decision-makers: soilmass
---

# Separate ID spaces

## Context and problem statement

Library rules, contract rules and project items could reuse a prefix. You said yes on 2026-11-18.

## Considered options

1. Three ID spaces with no shared prefix, checked by SKL-21
2. Keep the 0.x arrangement

## Decision outcome

Chosen option: "Three ID spaces with no shared prefix, checked by SKL-21".

### Consequences

- Good: every ID says where it belongs
- Bad: library prefixes are fixed early
