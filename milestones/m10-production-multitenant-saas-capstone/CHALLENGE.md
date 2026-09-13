# Challenge brief

- **C1 — Invisible production failure:** Seed latency, errors, backlog, and a silent business failure across HTTP/database/worker. Correlate structured logs, metrics, and traces without leaking secrets; make alerts actionable and health/readiness honest.
- **C2 — Cross-tenant security incident:** Attempt reads/writes via IDs, lists, nested routes, jobs, exports, caches, logs, and admin paths. Repair tenant isolation and append-only audit logs; prove synthetic tenant separation.
- **C3 — Failed release/migration:** Build one immutable Docker artifact in CI/CD, deploy an expand/contract migration, seed failed migration/readiness and incompatible rollback, recover without corrupting committed data, and rotate a synthetic secret.
- **C4 — Data-loss/incident drill:** Restore a backup into isolation, verify tenant totals/audit continuity, measure RPO/RTO, then run detection-to-recovery tabletop and blameless postmortem with owned actions.

Refactor the existing POS—do not rewrite it. Operate onboarding/support/export/deletion paths. Ship customer/operator docs, release notes, annotated tag, and explicit limitations.
