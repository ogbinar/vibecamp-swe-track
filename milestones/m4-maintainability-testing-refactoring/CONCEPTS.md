# M4 concepts through difficult changes

## “One small request touched seven files”

**Example:** a receipt field changes routes, SQL, and calculations separately.
**Term — coupling:** how much unrelated code a change forces you to know or
touch. **Rule:** measure scatter before adding a boundary.

## “Database code is duplicated across endpoints”

**Example:** session setup and the same query repeat in several routes. **Term —
dependency injection:** giving code its collaborator explicitly. **Rule:** add
only the service or repository boundary that localizes the demonstrated change.

## “Related behavior lives in unrelated places”

**Example:** one promotion change touches routes, calculations, and SQL fragments.
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
