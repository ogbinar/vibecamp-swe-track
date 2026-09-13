# Acceptance gate

Required maturity: **Level B plus contextual Level C security controls**.

## Core

- **A1:** C1 tests prove adaptive password hashing, bounded login behavior, no user enumeration, strict JWT signature/algorithm/issuer/audience/time/type validation, and no secrets in source/logs/evidence.
- **A2:** A deny-by-default RBAC matrix covers customer/staff/admin and C2 escalation attempts across every privileged route.
- **A3:** Two-user API tests cover every owned resource/list/nested/write path; all C3 object-level authorization attacks fail without cross-user disclosure or mutation.
- **A4:** Order state-machine tests cover allowed, forbidden, repeated, and bypass transitions together with required permissions; C4 prior state remains intact.
- **A5:** Threat model names assets, actors, trust boundaries, abuse cases, mitigations, residual risks; clean unit/integration/API/migration/lint/validator commands pass.
- **A6:** A [data-lifecycle review](../../templates/DATA-LIFECYCLE.md) traces password-derived data, JWT claims/identifiers, addresses, and order ownership through stores/logs/retention/deletion with access tests or explicit justified deferrals.

## Stretch

Add refresh-token rotation/revocation or rate limiting only with explicit threat/UX requirements and replay/lockout tests.
