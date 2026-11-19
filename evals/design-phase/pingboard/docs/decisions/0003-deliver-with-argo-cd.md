---
status: proposed
date: 2026-11-18
decision-makers: pingboard maintainers
---

# Deliver with Argo CD from k8s/

## Context and problem statement

The Project File's DEL rules call for declared, versioned desired state that an agent pulls and reconciles. How does pingboard reach the cluster?

## Decision drivers

- DEL-02 to DEL-05 (OpenGitOps principles)
- DEL-01: no mutable image tags
- The platform team already runs Argo CD

## Considered options

1. Argo CD application pointing at `k8s/` on `main`
2. `kubectl apply` from a CI job

## Decision outcome

Chosen option: "Argo CD", because it pulls and reconciles continuously, which a push from CI does not.

### Consequences

- Good: drift is corrected; CI holds no cluster credentials.
- Bad: manifests must reference image digests, so a release step updates `k8s/`.

### Confirmation

The Argo CD application has automated sync and self-heal on; `grep ':latest' k8s/` finds nothing.
