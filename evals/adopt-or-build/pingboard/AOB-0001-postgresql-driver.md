# AOB-0001: PostgreSQL driver for pingboard

Dry run of adopt-or-build, 2026-11-18, for design record 0002 (store check history in PostgreSQL). Facts looked up 2026-11-18 via api.deps.dev and api.securityscorecards.dev.

## Need

pingboard (Go 1.23, MIT licence) must write and read about 216,000 check rows in PostgreSQL. Constraints from the Project File: dependencies pinned (SUP-03), MIT project licence, no vendor named.

## Necessity

Go's standard library has `database/sql` but no PostgreSQL driver, and pingboard has no current dependency that speaks the protocol. A driver is necessary.

## Candidates

1. `github.com/jackc/pgx/v5`
2. `github.com/lib/pq`
3. Build our own wire-protocol client

Authenticity: both packages resolve on deps.dev to the GitHub repositories of the same name; no more popular look-alike name found. Confirmed.

## Gate checks

| Check | pgx v5.13.0 | lib/pq v1.12.3 |
| --- | --- | --- |
| Licence OSI-approved, compatible with MIT | PASS: MIT (deps.dev) | PASS: MIT (deps.dev) |
| Authenticity confirmed | PASS | PASS |
| No known unfixed critical or high vulnerability in this version | PASS: 0 advisories (deps.dev) | PASS: 0 advisories (deps.dev) |
| Release or commit in last 12 months | PASS: v5.13.0 published 2026-11-11 | PASS: v1.12.3 published 2026-04-03 |

Both are eligible.

## Other checks

| Check | pgx | lib/pq | Source |
| --- | --- | --- | --- |
| Scorecard overall (one input only) | 5.3 (2026-10-19) | 4.5 (2026-11-09) | api.securityscorecards.dev |
| Scorecard Maintained | 10 | 4 | same |
| Scorecard Code-Review | 8 | 2 | same |
| Scorecard Security-Policy | 0 | 0 | same |
| Adoption (GitHub stars) | 14,408 | 9,974 | deps.dev projects API |
| Maintainer count and organisations | not found | not found | not looked up in this dry run |
| Version stability | v5, stable | v1, stable | deps.dev |
| Secure interface (parameterised queries) | not found | not found | not looked up in this dry run |

Neither publishes a security policy, so a private reporting route is not documented for either.

## Build it ourselves

Estimate: 6 or more sessions for a minimal client, plus permanent upkeep of protocol, TLS and authentication changes. Not justified when two maintained MIT drivers exist.

## Recommendation

Adopt **pgx v5.13.0**, pinned in `go.sum`. It passes every gate check and is more actively maintained and reviewed than lib/pq (Scorecard Maintained 10 against 4, Code-Review 8 against 2), with wider adoption. The decision does not rest on the overall score alone.

## Decision

Pending: waiting for the user's decision. (Dry run: no decision recorded.)

## Options considered (for the Project File decision log)

pgx v5.13.0 (recommended), lib/pq v1.12.3, build our own.
