---
status: accepted
date: 2026-11-18
decision-makers: soilmass
---

# Profiles scale the gates

## Context and problem statement

Profiles small, standard and critical existed but changed no gate. You said yes on 2026-11-18.

## Considered options

1. Gate checks carry profile variants in contracts.yaml, checked by SKL-20
2. Keep the 0.x arrangement

## Decision outcome

Chosen option: "Gate checks carry profile variants in contracts.yaml, checked by SKL-20".

### Consequences

- Good: small projects stay light, critical ones get deeper checks
- Bad: each variant must be written and kept in step
