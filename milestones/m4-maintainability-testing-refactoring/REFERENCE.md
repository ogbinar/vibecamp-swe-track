# M4 reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M4 concepts through difficult changes

## “One small request touched seven files”

**Example:** a receipt field changes routes, SQL, and calculations separately.
**Term — coupling:** how much unrelated code a change forces you to know or
touch. **Rule:** measure scatter before adding a boundary.

## “Database code is duplicated across endpoints”

**Example:** session setup and the same query repeat in several routes. **Term —
dependency injection:** giving code its collaborator explicitly. **Rule:** add
only the service or repository boundary that localizes the demonstrated change.

## “Related behavior lives in unrelated places”

**Example:** the cashier display name touches routes, serialization, and SQL fragments.
**Term — cohesion:** keeping behavior that changes together close together.
**Rule:** add a boundary only when it measurably reduces change scatter or isolates
a real external/data seam.

## “A four-layer template added navigation but no value”

**Example:** route, service, and repository methods merely forward the same
arguments. **Term — composition root:** the place concrete collaborators are
assembled and injected. **Rule:** FastAPI dependencies are enough; earn services
through orchestration/invariants and repositories through repeated or complex data access.

## “The mocked test passed while the API was broken”

**Example:** a mock never crosses serialization or database mappings. **Term —
characterization test:** a test that preserves existing behavior before refactoring.
**Rule:** use unit, integration, and API tests for their distinct risks; separate
behavior changes from structure-preserving refactoring.

### Tools earned here

- **FastAPI dependency functions + composition root:** explicit lightweight DI; direct route-to-SQLAlchemy remains valid for simple cases, and needless provider layers are removed.
- **pytest fixtures/markers:** separate fast rule tests, real-database integration tests, and API acceptance tests.
- **Ruff import rules or a tiny dependency check:** enforce one demonstrated high-risk module direction; avoid a framework-sized architecture tool.
- **Git diff/history:** measure changed responsibilities and preserve behavior/refactor separation.

Avoid generic `BaseRepository`, `BaseService`, `utils`, complex DI, microservices, and shared libraries. Require before/after change-scatter evidence for each new service or repository; delete pass-through layers. The use case owns commit/rollback and repositories never auto-commit. An ADR is optional only for a consequential boundary; routine refactoring belongs in the PR rationale.

## Evaluate after evidence

Evaluate optional tools only after the stated simpler baseline fails. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates current behavior, or creates a second application path.

## Sources

### Resources for M4

Consult these when a change is hard to localize or a test gives false confidence. Reviewed 2026-09-13.

- [FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) — How can an endpoint receive a boundary without constructing it? Applicable tool: current FastAPI.
- [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) — How can tests share setup without sharing mutable state? Applicable tool: pytest 8+.
- [Python typing specification](https://typing.python.org/en/latest/spec/) — What promise does a type annotation make to tools and readers? Applicable standard: current Python typing spec.

Introduce a boundary only when change evidence shows a real coupling problem.
