# M10 — Support multiple businesses safely

[Course home](../../README.md) / M10

**Milestone 11 of 11 · M10**

## Business problem

Correct features are not sellable if one customer can see another's data, an
upgrade loses service, or nobody can restore a backup.

## Product objective

- **Product can:** operators can serve multiple tenants without crossing data, audit, release, or recovery boundaries.
- **You will prove:** tenant isolation, audit, readiness, release rejection, restore, incident, and handoff evidence.

Use the fixed small-retailer scenario in Block 1; personalize only in Stretch.
Then complete C1–C4 in the [challenge brief](#challenge-brief): instrument one user-impact
question, retrofit tenant context across every data path, deploy an immutable
image with migration/readiness gates, attack isolation, fail a migration, reject
an unhealthy release, restore a backup, and run an incident review.

Support onboarding to first sale, export, deletion, auditability, documented
upgrade/rollback, and honest remaining limitations. Add no observability backend
until a named question requires it.

## Start here

- **Gate:** [A1–A7 / Level C local Core; real-target endorsement optional](#core).
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/pos/README.md#pos-launch-kit-for-m2), then return to the saved block; first visit: [Block 1](#1-isolate-one-fixed-customer-required).

Start from the reviewed `m4-maintainable-pos` tag. Re-run its tests and migrations.
Use M5–M9 evidence as patterns; do not merge their unrelated product code.

On resume, preserve your existing `.env` and evidence. Use the validation
commands from the starting checks; first-install copy and destructive reset
steps are not routine resume actions. If a check fails, use Recovery first.

## Build

### 1. Isolate one fixed customer `[REQUIRED]`

Start from the starting checkpoint above. Work in `projects/pos/`;
focus on `tests/m10/test_tenant_isolation.py` and the output named below. Record `evidence/M10/isolation.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 1](#1-isolate-one-fixed-customer-required) using that saved result; continue to Block 2.
When needed: [C2 scenario and hints](#c2--cross-tenant-security-incident) and [concept explanation](#north-saw-souths-receipt). [Tool boundaries](#tools-earned-here) apply to this product.

Use the [fixed capstone contract](../../projects/pos/specs/M10-CAPSTONE-CONTRACT.md):
a small retailer with two tenant organizations, cashier and manager roles,
sales, inventory, exports, and support access. Retrofit tenant context through
every POS read/write/list/export/admin path and add append-only audit facts.
Run cross-tenant attack tests and record `evidence/M10/isolation.md`. Stop at
zero disclosure or mutation across tenants.

### 2. Answer one operational question `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/pos/`;
focus on `tests/m10/test_observability.py` and the output named below. Record `evidence/M10/observability.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 2](#2-answer-one-operational-question-required) using that saved result; continue to Block 3.
When needed: [C1 scenario and hints](#c1--invisible-production-failure) and [concept explanation](#health-was-green-while-the-database-was-unusable).

Question: “Are checkout failures preventing completed sales?” Correlate one
request through database work using structured redacted logs, one error/latency
metric, and one trace. Separate `/health` process liveness from `/ready`
dependency readiness. Record `evidence/M10/observability.md`; stop when a seeded
failure is detectable and routes to a runbook.

### 3. Rehearse release and recovery locally `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in the repository root;
focus on `projects/pos/scripts/rehearse_m10.sh` and the output named below. Record `evidence/M10/release-recovery.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 3](#3-rehearse-release-and-recovery-locally-required) using that saved result; continue to Block 4.
When needed: [C3 scenario and hints](#c3--failed-release-and-migration) and [concept explanation](#production-rebuilt-a-different-image).

Build one immutable image, deploy it by digest to local staging, run an
expand/contract migration, reject an unhealthy candidate, and restore a backup
into isolated local recovery. Record checksums, migration, readiness, rollback/
roll-forward, recovery point objective (RPO), and recovery time objective (RTO)
in `evidence/M10/release-recovery.md`. Stop when two clean environments pass.

### 4. Handoff and optional real target `[REQUIRED + ENDORSEMENT]`

Start from Block 3 green with its result recorded. Work in `projects/pos/`;
focus on `evidence/M10/` and the output named below. Record `evidence/M10/handoff.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 4](#4-handoff-and-optional-real-target-required--endorsement) using that saved result; continue to [Prove it](#prove-it).
When needed: [C4 scenario and hints](#c4--data-loss-and-incident-drill) and [concept explanation](#the-incident-ended-but-nobody-learned-from-it).

Complete incident, customer, operator, and portfolio templates. Core ends with
the local production rehearsal. The stronger Operable/Sellable endorsement
requires an authorized real target, TLS, secret custody, monitoring, encrypted
backup, measured restore, and the CI-published digest. Record
`evidence/M10/handoff.md`; never claim the endorsement without those facts.

Start from the supplied [migration](../../templates/RUNBOOK-MIGRATION.md),
[release rejection](../../templates/RUNBOOK-RELEASE-REJECTION.md),
[restore](../../templates/RUNBOOK-RESTORE.md), and
[incident](../../templates/INCIDENT.md#response-runbook) runbook scaffold. Replace every
blank with commands and owners from your declared target.

### Diagnose deliberate failures

Activate or construct only the current C scenario. Record the symptom and one
hypothesis before inspecting the implementation. Use the matching scenario link
in your active block, then its three hint levels in order. Reset to the last
green checkpoint before starting another scenario.

## Understand

- **Tenant:** one customer organization with an isolation boundary.
- **Audit log:** append-only evidence of important actor actions and changes.
- **SLO:** service-level objective, a measurable reliability target.
- **Telemetry:** structured logs, metrics, and traces used to answer operational questions.
- **Immutable artifact:** the same identified image is promoted between environments.
- **Rollback:** return code/configuration to a prior release; data may require roll-forward.

## Use a tool if earned

Use the current project dependencies first. Open [Use now](#use-now) for the active pattern, [Evaluate after evidence](#evaluate-after-evidence) only after the simpler baseline misses its target, and [Do not add yet](#do-not-add-yet) before adding another runtime or service.

## Prove it

Answer [review prompts](#review) after the Core proof.

Prove [A1–A7](#core) with tenant attack tests, artifact digest,
deployment/migration record, redacted telemetry, restore report, runbooks,
postmortem, release notes, and a cold-reviewed portfolio case study.

## Done / next

Local Core is complete when the tenant, audit, readiness, migration, release-
rejection, and isolated-restore gates pass and the limitations are explicit.
The real-target Operable/Sellable endorsement remains optional and needs its own
authorized evidence. After the applicable gate and cold review, tag and release
`m10-production-saas`.

### Recovery

Use [targeted references](#resources-for-m10) only for the question left by the active hint ladder.

Use the versioned runbook for migration, unhealthy release, isolation incident,
and restore procedures. Recovery commands belong in the repository, not memory.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Re-run the final portfolio review and choose the next product from evidence,
not from a desire to add infrastructure.

[Previous milestone: M9](../m9-performance-caching-realtime-social/README.md) · [Course home](../../README.md) · [Next: Portfolio review / evidence-led next product](../../templates/PORTFOLIO-CASE-STUDY.md#reader-path)


---

## Challenge brief

Use synthetic tenant data. Learner tests run from `projects/pos/`; release drills
run from the repository root.

## **C1 — Invisible production failure**

**YOU BUILD** — answer the fixed checkout-impact question.

### Steps

1. Create `tests/m10/test_observability.py` and seed one checkout failure.
2. Correlate one request through database work with redacted logs, a metric, and a trace.
3. Route the detected symptom to a runbook and run README Block 2.

### Hints

1. Start with the user-impact question and one correlation ID.
2. Inspect request context, database span, error classification, and alert threshold.
3. Use the OpenTelemetry link in the Reference section below.

### Reset

Disable the synthetic failure and run `uv run --locked pytest tests/m10/test_observability.py -q`.

## **C2 — Cross-tenant security incident**

**YOU BUILD** — use only synthetic tenant attack requests.

### Steps

1. Create `tests/m10/test_tenant_isolation.py` for IDs, lists, writes, exports, jobs, caches, logs, and admin paths.
2. Record disclosure/mutation and missing audit facts before repair.
3. Derive tenant from membership, scope every path, and run README Block 1.

### Hints

1. Ask where tenant context originates and where it is lost.
2. Inspect every query/write/export/cache key and support elevation boundary.
3. Use the tenant-security link in the Reference section below.

### Reset

Restore only synthetic North/South fixtures and run
`uv run --locked pytest tests/m10/test_tenant_isolation.py -q`.

## **C3 — Failed release and migration**

**YOU BUILD** — use local rehearsal first; a real target needs authorization.

### Steps

1. Build the revision-labelled image and run `sh projects/pos/scripts/rehearse_m10.sh` with its immutable image ID.
2. Confirm migration completes before readiness and the unhealthy override is rejected.
3. Record artifact, migration, restore, rollback/roll-forward decision, and limitations.

### Hints

1. Distinguish image creation, migration, readiness, promotion, and rollback.
2. Inspect Compose dependency conditions, `/ready`, image ID, and migration revision.
3. Use the Docker, Alembic, and Actions links in the Reference section below.

### Reset

The rehearsal trap removes only its three fixed synthetic Compose projects and
volumes. Rerun `sh projects/pos/scripts/rehearse_m10.sh`; never delete an unexplained volume.

## **C4 — Data-loss and incident drill**

**YOU BUILD** — restore a synthetic backup into an isolated target and follow runbooks.

### Steps

1. Verify `dist/m10-rehearsal.sql.sha256` and inspect the isolated restored revision.
2. Verify tenant totals and audit continuity, then measure recovery point/time.
3. Complete incident, customer, operator, and portfolio evidence using README Block 4.

### Hints

1. A backup file is not recovery evidence; begin with restore and integrity checks.
2. Inspect checksum, schema revision, tenant totals, audit continuity, and elapsed time.
3. Use the PostgreSQL backup/restore link in the Reference section below and follow the runbook.

### Reset

Preserve sanitized evidence, then rerun the fixed rehearsal; its isolated volumes
are recreated. Verify it first with `sha256sum -c dist/m10-rehearsal.sql.sha256`.
Do not claim the optional real-target endorsement from this drill.

Refactor the existing POS—do not rewrite it. Ship explicit limitations.


---

## Acceptance gate

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


---

## Reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M10 concepts through operating failures

## “North saw South’s receipt”

**Example:** one list query omitted tenant scope. **Term — tenant isolation:**
every data path keeps customer organizations separate. **Rule:** derive tenant
from membership and attack IDs, lists, writes, exports, support, and audit paths.

## “A backup existed but would not restore”

**Example:** an untested dump is unusable during an incident. **Term — recovery
time objective (RTO):** target time to restore acceptable service. **Rule:**
restore into isolation, verify product and tenant invariants, and measure actual
RPO/RTO.

## “Support tooling bypassed tenant scope”

**Example:** an admin export reads every organization. **Term — tenant context:**
the trusted customer boundary derived from authenticated membership. **Rule:**
carry it through IDs, lists, writes, jobs, exports, caches, logs, and support tools;
audit actor, tenant, action, target, time, and correlation.

## “Health was green while the database was unusable”

**Example:** the process answers but migrations are missing. **Term — readiness:**
whether dependencies and state permit traffic. **Rule:** keep liveness separate;
use logs, metrics, and traces to answer one user-impact question and link alerts to runbooks.

## “Production rebuilt a different image”

**Example:** deployment installs from source after CI passes. **Term — immutable
artifact:** one identified image promoted unchanged. **Rule:** continuous
integration (CI) validates; continuous delivery/deployment (CD) promotes the same
digest after migration, readiness, and rollback/roll-forward gates.

## “Compose started, so the team called it production-ready”

**Example:** no TLS, secret custody, monitoring, or tested restore exists. **Term —
bounded deployment:** a deliberately limited target with named controls and
limitations. **Rule:** test each required control; a backup counts only after an
isolated restore and integrity verification.

## “The incident ended but nobody learned from it”

**Example:** recovery has no timeline or owned follow-up. **Term — blameless
postmortem:** an evidence-based review of impact, detection, conditions, response,
and prevention. **Rule:** pair release notes and recovery evidence with onboarding,
support, export/deletion, costs, security posture, and honest limitations.

### Tools earned here

- **Docker + GitHub Actions:** CI builds and verifies one immutable artifact; CD promotes that exact digest only after a real target and the deployment gates are present.
- **Docker Compose:** reproduce local/integration environments and, if deliberately chosen, a documented single-host runtime; identify which platform/reverse-proxy controls provide TLS, restart, secrets, backup, monitoring, and rollback.
- **Platform secret/config controls:** separate values by environment; scan/redact outputs and support rotation.
- **Structured logs, metrics, traces:** start with redacted structured logs and correlation IDs. Add OpenTelemetry plus one owned backend for portable instrumentation, or choose Logfire/Sentry when one managed backend better fits the diagnostic need; do not require all three. Record propagation, sampling, retention, cost, and removal criteria.
- **PostgreSQL backup/restore and migration tools:** measured recovery and compatible rollout.
- **Synthetic tenant/security/load harnesses:** repeat isolation and operational drills safely.

Optional endorsements are evaluated one at a time after Core:

- **S3-compatible storage:** only for files that must outlive instances; bound
  tenant-safe keys, presigned expiry, authorization, type/size, checksum,
  retention/delete, partial failure, and orphan reconciliation.
- **OAuth/OIDC:** authorization code plus PKCE and OIDC validation only after an
  external identity need; own state/nonce, redirect allowlist, issuer/audience/
  signature/time/key rotation, linking, logout, and revocation assumptions.
- **Sentry or Logfire:** choose one for one named question; own redaction,
  sampling, retention, access, cost, and deletion, then retain or remove.
- **SQLAdmin:** only after tenant authorization and append-only audit are green;
  every action remains scoped, authorized, and audited.

Each defaults to do not add yet without need, owner, cost/data boundary, removal
trigger, access, and explicit authority. A real deployment is a separate optional
endorsement under the existing target prerequisites.

Prefer platform-managed TLS/secrets and state the boundary outside Compose. Kubernetes, service mesh, microservices, multiple databases, and elaborate deployment strategies remain excluded. Earn canary/blue-green only from measured rollout risk.

Revisit relevant [complexity rejection records](../../templates/COMPLEXITY-REJECTION.md) before adopting observability or deployment machinery; a production label is not evidence that the trigger fired.

## Evaluate after evidence

Evaluate optional tools only after the stated simpler baseline fails. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates current behavior, or creates a second application path.

## Sources

### Resources for M10

Use these to answer a capstone operational question, not to expand the stack. Reviewed 2026-09-14.

- [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup.html) — What is backed up, restored, and actually tested? Applicable tool: current PostgreSQL.
- [GitHub deployment environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments) — Where do approvals, secrets, and deployment history belong? Applicable platform: GitHub Actions.
- [Amazon S3 presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) — Optional: what bearer scope, expiry, and checksum controls bound direct object access?
- [OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/rfc/rfc9700.html) — Optional: why authorization code with PKCE, and why not the resource-owner password grant? Applicable standard: RFC 9700.
- [Logfire FastAPI](https://pydantic.dev/docs/logfire/integrations/web-frameworks/fastapi/) — Optional example: does one backend answer the named diagnostic question under the declared data/cost boundary? Compare Sentry or SQLAdmin only after its separate trigger fires.

Managed tools such as Logfire or Sentry are optional adapters after telemetry questions are explicit.
