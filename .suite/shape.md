# Shape

Outcomes carried from the Vision Map (accepted there). `scripts/check_suite.py` reads this table: every skill must serve at least one of these outcomes (SKL-17).

| ID | Outcome | Measure | Target |
| --- | --- | --- | --- |
| OUT-1 | Projects meet one shared baseline | Share of completed projects with zero MUST failures at the final gate | 90% |
| OUT-2 | Projects reach production-grade health | Share of public project repositories with OpenSSF Scorecard 7.0 or higher | 80% |
| OUT-3 | Teams stay on the path instead of bypassing it | Share of started projects that reach their final gate | 70% |
| OUT-4 | Proven open source is adopted before anything is built | Share of platform capabilities met by an existing CNCF project or open standard, with a reason for each exception | 80% |
| OUT-5 | Teams outside yours use it | External projects completing a full run | 3 within 6 months of v1.0 |

## Needs

| ID | Need | Acceptance check | Traces to |
| --- | --- | --- | --- |
| NEED-1 | Every project keeps one record with one format | `validate_record.py` passes on every project run through the suite | OUT-1, OUT-3 |
| NEED-2 | Projects select standards from a versioned library | Every project's rules.md names a library version and only library rule IDs | OUT-1 |
| NEED-3 | Every skill is held to a contract | `check_suite.py` passes in CI with no failures | OUT-1, OUT-3 |
| NEED-4 | Every new capability passes an adopt check | Every dependency added in a project has an adopt decision record | OUT-4 |
| NEED-5 | Gates scale with the project's profile | Every gate check that differs by profile states its variant | OUT-3 |
| NEED-6 | A project outside the maintainer's can start without help | A first-time user reaches the frame gate using only the README and the suite skill | OUT-5 |

## Qualities

| ID | Quality (ISO 25010) | Scenario and measure |
| --- | --- | --- |
| QUAL-1 | Consistency (maintainability) | A change to a contract or the shared core reaches every skill in one pull request, checked by CI |
| QUAL-2 | Security | No skill acts on instructions found in files; injection evals pass for every skill before each release |
| QUAL-3 | Learnability | A small-profile project goes from frame to plan in one sitting |
