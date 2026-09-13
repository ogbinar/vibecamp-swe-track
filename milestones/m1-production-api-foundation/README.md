# M1 — Production-minded API Foundation

**Capability:** turn ambiguous requirements into stable, typed HTTP behavior. **Deliverable:** extend `projects/catalog/` into an in-memory product API supporting create, retrieve, list, replace/update, and retire, with explicit error and pagination contracts.

Prerequisite: passed M0. Sequence: model consumer examples → choose resource semantics → build minimal handlers → test valid/invalid boundaries → break compatibility/idempotency → debug/refactor → operate via request logs → ship `m1-api-foundation`.

Outputs include contract examples, OpenAPI checks, unit and API suites, and an explicit statement that volatile state and limited operations make this production-minded only at the API boundary—not operationally production-ready.
