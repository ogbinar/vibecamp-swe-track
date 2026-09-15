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
Then complete C1–C4 in [CHALLENGE.md](CHALLENGE.md#m10-challenge-brief): instrument one user-impact
question, retrofit tenant context across every data path, deploy an immutable
image with migration/readiness gates, attack isolation, fail a migration, reject
an unhealthy release, restore a backup, and run an incident review.

Support onboarding to first sale, export, deletion, auditability, documented
upgrade/rollback, and honest remaining limitations. Add no observability backend
until a named question requires it.

## Start here

- **Gate:** [A1–A7 / Level C local Core; real-target endorsement optional](ACCEPTANCE.md#core).
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
When needed: [C2 scenario and hints](CHALLENGE.md#c2--cross-tenant-security-incident) and [concept explanation](REFERENCE.md#north-saw-souths-receipt). [Tool boundaries](REFERENCE.md#tools-earned-here) apply to this product.

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
When needed: [C1 scenario and hints](CHALLENGE.md#c1--invisible-production-failure) and [concept explanation](REFERENCE.md#health-was-green-while-the-database-was-unusable).

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
When needed: [C3 scenario and hints](CHALLENGE.md#c3--failed-release-and-migration) and [concept explanation](REFERENCE.md#production-rebuilt-a-different-image).

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
When needed: [C4 scenario and hints](CHALLENGE.md#c4--data-loss-and-incident-drill) and [concept explanation](REFERENCE.md#the-incident-ended-but-nobody-learned-from-it).

Complete incident, customer, operator, and portfolio templates. Core ends with
the local production rehearsal. The stronger Operable/Sellable endorsement
requires an authorized real target, TLS, secret custody, monitoring, encrypted
backup, measured restore, and the CI-published digest. Record
`evidence/M10/handoff.md`; never claim the endorsement without those facts.

Start from the supplied [migration](../../templates/RUNBOOK-MIGRATION.md),
[release rejection](../../templates/RUNBOOK-RELEASE-REJECTION.md),
[restore](../../templates/RUNBOOK-RESTORE.md), and
[incident](../../templates/RUNBOOK-INCIDENT.md) runbook scaffolds. Replace every
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

Use the current project dependencies first. Open [Use now](REFERENCE.md#use-now) for the active pattern, [Evaluate after evidence](REFERENCE.md#evaluate-after-evidence) only after the simpler baseline misses its target, and [Do not add yet](REFERENCE.md#do-not-add-yet) before adding another runtime or service.

## Prove it

Answer [review prompts](ACCEPTANCE.md#review) after the Core proof.

Prove [A1–A7](ACCEPTANCE.md#core) with tenant attack tests, artifact digest,
deployment/migration record, redacted telemetry, restore report, runbooks,
postmortem, release notes, and a cold-reviewed portfolio case study.

## Done / next

Local Core is complete when the tenant, audit, readiness, migration, release-
rejection, and isolated-restore gates pass and the limitations are explicit.
The real-target Operable/Sellable endorsement remains optional and needs its own
authorized evidence. After the applicable gate and cold review, tag and release
`m10-production-saas`.

### Recovery

Use [targeted references](REFERENCE.md#resources-for-m10) only for the question left by the active hint ladder.

Use the versioned runbook for migration, unhealthy release, isolation incident,
and restore procedures. Recovery commands belong in the repository, not memory.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Re-run the final portfolio review and choose the next product from evidence,
not from a desire to add infrastructure.

[Previous milestone: M9](../m9-performance-caching-realtime-social/README.md) · [Course home](../../README.md) · [Next: Portfolio review / evidence-led next product](../../templates/PORTFOLIO-CASE-STUDY.md#reader-path)
