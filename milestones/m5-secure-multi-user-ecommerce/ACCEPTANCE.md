# Acceptance gate

Required maturity: **Level B plus contextual Level C security controls**.

## Core

- **A1:**
  - [ ] C1 evidence compares opaque secure-cookie sessions with JWT against the declared client/trust boundary and justifies one product choice.
  - [ ] Tests prove `pwdlib[argon2]` hashing/upgrade, bounded login behavior, no user enumeration, and no secrets in source/logs/evidence.
  - [ ] Cookie choice additionally proves `Secure`/`HttpOnly`/`SameSite`, fixation rotation, CSRF defense, expiry, and logout/revocation.
  - [ ] A short JWT comparison explains algorithm allowlist, issuer, audience, time, token type, rotation/revocation, and theft behavior.
  - [ ] JWT implementation tests are Stretch for the declared first-party browser; Core does not implement both session systems.
- **A2:**
  - [ ] A deny-by-default RBAC matrix covers customer/staff/admin and C2 escalation attempts across every privileged route.
- **A3:**
  - [ ] Two-user API tests cover every owned resource/list/nested/write path
  - [ ] all C3 object-level authorization attacks fail without cross-user disclosure or mutation.
- **A4:**
  - [ ] Order state-machine tests cover allowed, forbidden, repeated, and bypass transitions together with required permissions
  - [ ] C4 prior state remains intact.
- **A5:**
  - [ ] Threat model names assets, actors, trust boundaries, abuse cases, mitigations, residual risks
  - [ ] clean unit/integration/API/migration/lint/validator commands pass.
- **A6:**
  - [ ] A [data-lifecycle review](../../templates/DATA-LIFECYCLE.md) traces password-derived data and session identifiers/claims.
  - [ ] It traces addresses and order ownership through stores, logs, retention, and deletion.
  - [ ] Access behavior has tests or explicit justified deferrals.

## Execution map

Each checklist bullet is a local step in order. From `projects/ecommerce/`, use
README Block 1 for A1, Block 2 for A2–A3, and Block 3 for A4. For A5 run
`uv run --locked ruff check . && uv run --locked mypy && uv run --locked pytest`;
for A6 run `test -s evidence/M5/data-lifecycle.md`. Record results under matching
A headings; recover with the bounded ecommerce reset and synthetic fixtures.

## Stretch

Add refresh-token rotation/revocation or rate limiting only with explicit threat/UX requirements and replay/lockout tests.

## Review

### Review

Answer one question at a time in `evidence/M5/index.md`:

1. How is authentication different from authorization?
2. Which decision belongs to a role, and which belongs to object ownership?
3. How is an old password hash upgraded?
4. Why does the first-party browser earn an opaque cookie session for Core?
5. What does that cookie/session design not guarantee?
6. Where is identity established, rotated, expired, and revoked?
7. How do permission and order state combine for one command?
8. Do ID, list, and nested routes deny Alice access to Bob's object without disclosure?
9. Which cookie, Cross-Site Request Forgery (CSRF), log, and secret checks pass?
10. What residual threat remains?

Use the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md) to find copies that authentication tests alone miss: logs, session records or token claims, order snapshots, and retained audit/security records.
