# Acceptance gate

Required maturity: **Level C**, cumulatively including Levels A and B.

## Core

- **A1:** C1 correlates one request through database/background work using request/correlation ID, structured redacted logs, metrics, and traces; declared latency/error/job-age SLIs alert, link a runbook, and clear after recovery; health/readiness differ correctly.
- **A2:** C2 two-tenant tests cover every owned resource/list/write/job/export/cache/admin path with zero disclosure/mutation; tenant derives from membership; audit logs capture actor/tenant/action/target/time/correlation and resist normal mutation without sensitive fields.
- **A3:** Clean CI runs Ruff, mypy, tests, migrations, security/dependency checks and builds the exact immutable Docker digest deployed. CD names the real target and environment approval; C3 proves configuration/secrets handling, migration deployment compatibility, readiness gating, failed release rollback/roll-forward, and preserved data. If Compose runs the target, evidence separately identifies and tests TLS, restart, secret custody, backup, monitoring, and rollback controls.
- **A4:** C4 restores an isolated backup, passes integrity/application/tenant/audit checks, measures RPO/RTO against targets, and produces timeline/impact/detection/recovery/communication/postmortem/follow-up evidence.
- **A5:** Onboarding reaches first sale; a [data-lifecycle review](../../templates/DATA-LIFECYCLE.md) traces tenant/user/sale/audit/export/backup copies; export/deletion and restore reconciliation follow documented retention; customer/operator docs cover target user, roles, limits, support, costs/pricing assumptions, security posture, release/rollback, and known limitations.
- **A6:** All earlier POS regression gates pass; no unresolved critical/high security/correctness issue; issue/PR/Actions/evidence/`PROGRESS`/release notes/annotated `m10-production-saas` tag are traceable.
- **A7:** The final [portfolio case study](../../templates/PORTFOLIO-CASE-STUDY.md) links requirements, smallest design, preserved failure/regression, decisions/rejections, contextual before/after evidence, security/operations/recovery, personal contribution, assistance, and honest limitations; a cold reviewer completes its ten-minute reader path.

## Stretch

Add synthetic usage metering or an earned canary/blue-green path; neither substitutes for recovery or isolation Core evidence.
