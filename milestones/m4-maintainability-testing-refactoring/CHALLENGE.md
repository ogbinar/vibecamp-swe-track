# Challenge brief

- **C1 — Stakeholder-driven technical-debt change:** Use the [requirements brief](../../templates/REQUIREMENTS.md) to record the decision owner, conflicting promotion/compatibility need, accepted behavior, and rejected scope. Implement the change badly across handlers/models/queries, record files and reasons touched, then refactor by cohesion. Seed a circular/forbidden module dependency and make an automated boundary check catch it.
- **C2 — Duplicated DB behavior:** Seed repeated transaction/query code across endpoints. Introduce only the service/repository boundaries and dependency injection needed to localize return/promotion variants; preserve transaction ownership and explicit SQL.
- **C3 — False-confidence tests:** Supply a mock-heavy test that passes while mappings/routes are broken. Diagnose why, replace it with the appropriate integration/API test, and retain focused unit tests for pure policies.

Operate the same monolith and migration chain. Ship separate behavior/refactor commits or PRs with before/after change-scatter evidence.

Before the final review, complete one [complexity rejection record](../../templates/COMPLEXITY-REJECTION.md) for a meaningful abstraction/tool considered and rejected or removed. This is not an ADR and must name a measurable revisit trigger.
