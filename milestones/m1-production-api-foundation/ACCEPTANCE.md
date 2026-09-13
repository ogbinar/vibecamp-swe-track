# Acceptance gate

Required maturity: **Level A plus selected Level B boundary engineering**; no Level C claim.

## Core

- **A1:** API tests prove create/get/list/update/retire HTTP semantics, stable errors, headers where relevant, deterministic bounded pagination, and repeat-request/idempotency behavior from C1.
- **A2:** Unit and API tests cover every documented typing/validation rule, duplicate identity, decimal money, and reset isolation; malformed input never becomes an unhandled 500 and C2 defects fail specifically.
- **A3:** A semantic OpenAPI/contract comparison detects a seeded breaking change; C3 preserves the original/new requirement, decision owner, accepted/rejected scope, changed tests, and release/deprecation evidence.
- **A4:** Documentation explicitly names the volatile-state, security, deployment, and recovery limitations; the declared FastAPI CLI/Uvicorn no-reload command serves the same tested contract; clean-checkout tests/Ruff/mypy/validator pass.

Evidence must include sanitized requests/responses and test names, not screenshots alone.

## Stretch

Add ETag conditional updates or a tiny typed client only after Core, preserving the established contract with tests.
