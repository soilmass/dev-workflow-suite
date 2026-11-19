---
status: proposed
date: 2026-11-18
decision-makers: pingboard maintainers
---

# Store check history in PostgreSQL

## Context and problem statement

pingboard keeps 30 days of results: 5 services × 1,440 checks a day × 30 days, about 216,000 rows. Where should the history live?

## Decision drivers

- 30-day history survives restarts
- The cluster already offers a managed PostgreSQL
- Few new dependencies

## Considered options

1. PostgreSQL (existing managed instance)
2. SQLite on a persistent volume
3. In-memory only

## Decision outcome

Chosen option: "PostgreSQL", because the history must survive restarts and the platform already runs it, so no new service is added.

### Consequences

- Good: durable history; backups handled by the platform.
- Bad: one Go driver dependency, evaluated in adopt-or-build record AOB-0001; database credentials to protect (threat T2).

### Confirmation

Integration test writes and reads a day of results; credentials come only from a Kubernetes Secret.

## More information

Driver choice: `evals/adopt-or-build/pingboard/AOB-0001-postgresql-driver.md`.
