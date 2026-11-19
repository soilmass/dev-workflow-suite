---
status: proposed
date: 2026-11-18
decision-makers: pingboard maintainers
---

# Single Go service with a server-rendered page

## Context and problem statement

pingboard must show up or down status for 5 services every minute with 30 days of history (DOD-1), within 4 weeks, run by a small team. How many running parts should it have, and how is the page built?

## Decision drivers

- 4-week appetite and a small team
- Public, read-only page; no accounts
- OBS-01: traces, metrics and logs through OpenTelemetry

## Considered options

1. One Go service: scheduler, store client and server-rendered HTML
2. Go API plus a separate single-page front end
3. Separate probe worker and web service

## Decision outcome

Chosen option: "One Go service", because it meets the DoD with one container to build, deploy and secure.

### Consequences

- Good: one image, one deployment, one threat-model element.
- Bad: probing and serving share one process; a probe stall can slow the page (mitigated by timeouts).

### Confirmation

The container diagram shows one service container; the build has one Deployment manifest.

## Pros and cons of the options

### Go API plus single-page front end

- Good: richer UI later.
- Bad: two artefacts and a JavaScript supply chain for a read-only page.

### Separate probe worker and web service

- Good: isolates probe failures.
- Bad: two containers and a queue or shared database contract before it is needed.
