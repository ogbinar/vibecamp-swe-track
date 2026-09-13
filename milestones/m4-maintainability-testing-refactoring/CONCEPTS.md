# Problems and mental models

Duplicated database code across endpoints and promotion conditionals across layers make a small change scatter. Cohesion groups behavior that changes together; coupling measures what must be known/touched together. A boundary is valuable when it localizes a demonstrated change or isolates a real external/data seam.

Dependency injection means assembling concrete collaborators at a composition root so code can receive capabilities explicitly. FastAPI dependencies suffice; a DI framework would add indirection without a problem. A simple route may call SQLAlchemy directly. Services are earned when use-case orchestration or invariant ownership must be localized; repositories are earned when repeated/complex persistence behavior needs a deliberate seam. Services own transaction intent; repositories expose persistence operations, not business rules or auto-commit. Pass-through layers and universal base classes increase navigation without reducing change scatter.

Characterization tests preserve unknown behavior during refactoring. Unit, integration, and API tests address different risks; mocks at internal implementation seams can pass while the system is broken. Refactoring preserves behavior; feature changes are separated into reviewable steps.
