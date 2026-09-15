# Acceptance gate

Required maturity: **Level C**, cumulatively including Levels A and B.

## Core

- **A1:**
  - [ ] C1 correlates one request through database work using request/correlation ID, structured redacted logs, metrics, and traces
  - [ ] declared latency/error/job-age SLIs alert, link a runbook, and clear after recovery
  - [ ] health/readiness differ correctly.
- **A2:**
  - [ ] C2 two-tenant tests cover every owned resource/list/write/job/export/cache/admin path with zero disclosure/mutation
  - [ ] tenant derives from membership
  - [ ] audit logs capture actor/tenant/action/target/time/correlation and resist normal mutation without sensitive fields.
- **A3:**
  - [ ] Clean CI runs Ruff, mypy, tests, migrations, security/dependency checks and builds an immutable Docker digest.
  - [ ] Core local rehearsal records its local digest; the stronger endorsement deploys the exact CI digest to a named real target with environment approval.
  - [ ] C3 proves configuration/secrets handling, migration deployment compatibility, readiness gating, failed release rollback/roll-forward, and preserved data.
  - [ ] If Compose runs the target, evidence separately identifies and tests TLS, restart, secret custody, backup, monitoring, and rollback controls.
- **A4:**
  - [ ] C4 restores a backup into an isolated environment.
  - [ ] Integrity, application, tenant, and audit checks pass on the restore.
  - [ ] Measured RPO/RTO are compared with declared targets.
  - [ ] Timeline, impact, detection, recovery, communication, postmortem, and owned follow-ups are recorded.
- **A5:**
  - [ ] Onboarding reaches first sale
  - [ ] a [data-lifecycle review](../../templates/DATA-LIFECYCLE.md) traces tenant/user/sale/audit/export/backup copies
  - [ ] export/deletion and restore reconciliation follow documented retention
  - [ ] customer/operator docs cover target user, roles, limits, support, costs/pricing assumptions, security posture, release/rollback, and known limitations.
- **A6:**
  - [ ] All earlier POS regression gates pass
  - [ ] no unresolved critical/high security/correctness issue
  - [ ] issue/PR/Actions/evidence/`PROGRESS`/release notes/annotated `m10-production-saas` tag are traceable.
- **A7:**
  - [ ] The final [portfolio case study](../../templates/PORTFOLIO-CASE-STUDY.md) links requirements and the smallest design.
  - [ ] It links a preserved failure, regression proof, and contextual before/after evidence.
  - [ ] It explains security, operations, recovery, personal contribution, and assistance.
  - [ ] It states honest limitations.
  - [ ] a cold reviewer completes its ten-minute reader path.

## Execution map

Each checklist bullet is a local step in order. From `projects/pos/`, use README
Blocks 2 and 1 for A1 and A2. From the repository root, use Block 3 for A3–A4.
Use Block 4 and `test -s evidence/M10/handoff.md` for A5–A7. Expected: local Core
claims stop at locally observed migration/readiness/rejection/restore facts; the
real-target endorsement stays N/A until separately proven. Record under matching
A headings; the rehearsal’s trap is the bounded recovery route.

## Stretch

Add synthetic usage metering or an earned canary/blue-green path; neither substitutes for recovery or isolation Core evidence.

## Review

### Review

Answer one question at a time in `evidence/M10/index.md`:

1. How is tenant context established from membership?
2. Which boundary enforces that tenant context?
3. How is an audit record different from a diagnostic log?
4. Where does continuous integration (CI) end and continuous deployment (CD) begin?
5. What exact digest was built, approved, and deployed?
6. Which TLS, secret, monitoring, backup, and rollback controls exist outside Compose?
7. Which expand/contract step is backward compatible?
8. When is rollback unsafe and roll-forward required?
9. How is a synthetic secret rotated without logging it?
10. Which user question does each log, metric, and trace answer?
11. What RPO and RTO were measured during isolated restore?
12. What does a buyer or operator need before trusting this product?
13. What is the biggest remaining blocker to real-money use?

Trace a deleted tenant through primary rows, audit exceptions, exports, logs, jobs/caches, and restored backups using the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md). Cold-review the final portfolio reader path. Lens prompt (same A1–A7 gate): a career-shifter translates domain/support judgment into incident and release decisions; a data specialist demonstrates ownership beyond storage—tenant-safe APIs, deployment, observability, recovery, and customer communication.
