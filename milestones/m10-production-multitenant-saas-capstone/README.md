# M10 — Production Multi-tenant SaaS Capstone

[Course home](../../README.md) / M10

**Milestone 11 of 11 · M10**

## Why

Correct features are not sellable if one customer can see another's data, an
upgrade loses service, or nobody can restore a backup.

## Starting checkpoint

- **At a glance:** Operable/sellable candidate · Multi-tenant POS SaaS.
- **You will leave with:** Tenant-isolation proof; Release/recovery record; Runbooks and cold-reviewed handoff.
- **Gate:** [A1–A7 / Level C local Core; real-target endorsement optional](ACCEPTANCE.md#core).
- **Repository support:** supplied starter locally verified; your learner gate needs your own evidence. [Dated scope and limits](../../USABILITY.md#readiness-status-vocabulary)
separate local structure/starter checks from pending hosted and human evidence.
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/pos/README.md#pos-launch-kit-for-m2), then return to the saved block; first visit: [Block 1](#1-isolate-one-fixed-customer-required).

Start from the reviewed `m4-maintainable-pos` tag. Re-run its tests and migrations.
Use M5–M9 evidence as patterns; do not merge their unrelated product code.

On resume, preserve your existing `.env` and evidence. Use the validation
commands from the starting checks; first-install copy and destructive reset
steps are not routine resume actions. If a check fails, use Recovery first.

## Terms used here

- **Tenant:** one customer organization with an isolation boundary.
- **Audit log:** append-only evidence of important actor actions and changes.
- **SLO:** service-level objective, a measurable reliability target.
- **Telemetry:** structured logs, metrics, and traces used to answer operational questions.
- **Immutable artifact:** the same identified image is promoted between environments.
- **Rollback:** return code/configuration to a prior release; data may require roll-forward.

## Product brief

Use the fixed small-retailer scenario in Block 1; personalize only in Stretch.
Then complete C1–C4 in [CHALLENGE.md](CHALLENGE.md#m10-challenge-brief): instrument one user-impact
question, retrofit tenant context across every data path, deploy an immutable
image with migration/readiness gates, attack isolation, fail a migration, reject
an unhealthy release, restore a backup, and run an incident review.

Support onboarding to first sale, export, deletion, auditability, documented
upgrade/rollback, and honest remaining limitations. Add no observability backend
until a named question requires it.

## Work blocks

### 1. Isolate one fixed customer `[REQUIRED]`

Start from the starting checkpoint above. Work in `projects/pos/`;
focus on `tests/m10/test_tenant_isolation.py` and the output named below. Record `evidence/M10/isolation.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 1](#1-isolate-one-fixed-customer-required) using that saved result; continue to Block 2.
When needed: [C2 scenario and hints](CHALLENGE.md#c2--cross-tenant-security-incident) and [concept explanation](CONCEPTS.md#north-saw-souths-receipt). [Tool boundaries](TOOLS.md#tools-earned-here) apply to this product.

Use the [fixed capstone contract](../../projects/pos/specs/M10-CAPSTONE-CONTRACT.md):
a small retailer with two tenant organizations, cashier and manager roles,
sales, inventory, exports, and support access. Retrofit tenant context through
every POS read/write/list/export/admin path and add append-only audit facts.
Run cross-tenant attack tests and record `evidence/M10/isolation.md`. Stop at
zero disclosure or mutation across tenants.

### 2. Answer one operational question `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/pos/`;
focus on `tests/m10/test_observability.py` and the output named below. Record `evidence/M10/observability.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 2](#2-answer-one-operational-question-required) using that saved result; continue to Block 3.
When needed: [C1 scenario and hints](CHALLENGE.md#c1--invisible-production-failure) and [concept explanation](CONCEPTS.md#health-was-green-while-the-database-was-unusable).

Question: “Are checkout failures preventing completed sales?” Correlate one
request through database work using structured redacted logs, one error/latency
metric, and one trace. Separate `/health` process liveness from `/ready`
dependency readiness. Record `evidence/M10/observability.md`; stop when a seeded
failure is detectable and routes to a runbook.

### 3. Rehearse release and recovery locally `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in the repository root;
focus on `projects/pos/scripts/rehearse_m10.sh` and the output named below. Record `evidence/M10/release-recovery.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 3](#3-rehearse-release-and-recovery-locally-required) using that saved result; continue to Block 4.
When needed: [C3 scenario and hints](CHALLENGE.md#c3--failed-release-and-migration) and [concept explanation](CONCEPTS.md#production-rebuilt-a-different-image).

Build one immutable image, deploy it by digest to local staging, run an
expand/contract migration, reject an unhealthy candidate, and restore a backup
into isolated local recovery. Record checksums, migration, readiness, rollback/
roll-forward, recovery point objective (RPO), and recovery time objective (RTO)
in `evidence/M10/release-recovery.md`. Stop when two clean environments pass.

### 4. Handoff and optional real target `[REQUIRED + ENDORSEMENT]`

Start from Block 3 green with its result recorded. Work in `projects/pos/`;
focus on `evidence/M10/` and the output named below. Record `evidence/M10/handoff.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 4](#4-handoff-and-optional-real-target-required--endorsement) using that saved result; continue to [Evidence](#evidence).
When needed: [C4 scenario and hints](CHALLENGE.md#c4--data-loss-and-incident-drill) and [concept explanation](CONCEPTS.md#the-incident-ended-but-nobody-learned-from-it).

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

### Literal command map

Run learner tests from `projects/pos/`; run the release rehearsal from the
repository root. Create missing M10 learner tests before expecting green.

Before: learner product tests are absent/red and no release claim exists. After:
the row’s locally observable stop condition and limitation are recorded.

| Block | Copyable command | Expected stop condition |
|---|---|---|
| 1 | `POS_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5432/vibecamp_pos uv run --locked pytest tests/m10/test_tenant_isolation.py -q` | Every owned path rejects cross-tenant reads and writes and records safe audit facts. |
| 2 | `uv run --locked pytest tests/m10/test_observability.py -q` | One seeded checkout failure is correlated, measurable, redacted, and linked to a runbook. |
| 3 | `IMAGE_REF="$(docker image inspect vibecamp-pos:"$(git rev-parse HEAD)" --format '{{.Id}}')" PREVIOUS_IMAGE_REF="$(docker image inspect vibecamp-pos:"$(git rev-parse HEAD)" --format '{{.Id}}')" sh projects/pos/scripts/rehearse_m10.sh` | Migration precedes readiness, rollback/roll-forward commands execute, isolated restore becomes ready, and the unhealthy candidate is rejected. Use a distinct compatible prior image for learner release evidence. |
| 4 | `test -s evidence/M10/handoff.md && test -s evidence/M10/portfolio.md` | Core handoff evidence exists; optional endorsement remains unclaimed without real-target proof. |

Before Block 3, build the exact local image with the command below. Recover by
rerunning the rehearsal: its trap removes only the three fixed synthetic Compose
projects and volumes. Preserve `dist/m10-rehearsal.sql*` only as sanitized local
evidence, then record the next action before pausing.

Pause: record the image ID, environment, last gate, evidence path, and next block.

```bash
docker build --label "org.opencontainers.image.revision=$(git rev-parse HEAD)" --tag "vibecamp-pos:$(git rev-parse HEAD)" projects/pos
```

## Reference deployment target

The optional real target is one Linux host running Docker Engine and Docker Compose,
with one application image used by the API and one PostgreSQL service,
host-level TLS, encrypted backups, and an environment-scoped secret store. This
is intentionally small. Choose another target only when you record its owner,
cost, secret custody, database, TLS, backup, and rollback behavior.

Before using a real target, record authorization and cost owner; domain and TLS
termination; environment-scoped secret custody; monitoring/alert destination;
encrypted backup retention; restore target; and rollback/roll-forward owner.
Missing any item means remain on the local Core rehearsal.

Core uses the local two-environment rehearsal. For the optional endorsement,
GitHub Actions publishes `ghcr.io/OWNER/IMAGE@sha256:DIGEST`; an approved job
records the exact handoff. Only a learner-authorized target may deploy that
digest and claim promotion evidence. Never rebuild on the host. A local archive is
only rehearsal evidence and belongs under ignored `dist/` with a checksum:

```bash
revision=$(git rev-parse HEAD)
image="vibecamp-pos:$revision"
docker build --label "org.opencontainers.image.revision=$revision" --tag "$image" projects/pos
docker image inspect "$image" --format '{{.Id}} {{index .Config.Labels "org.opencontainers.image.revision"}}'
mkdir -p dist
docker save "$image" --output "dist/vibecamp-pos-$revision.tar"
sha256sum "dist/vibecamp-pos-$revision.tar" > "dist/vibecamp-pos-$revision.tar.sha256"
```

Expected locally: the inspected revision equals the Git commit and the checksum
verifies. Expected for the endorsement: the deployed digest exactly equals the
digest published by CI, migration exits zero, readiness becomes healthy, and
the release record stores that digest.

Rehearse two isolated local environments with different Compose project names
and secret values; never point both at one data volume:

```bash
POSTGRES_PASSWORD=synthetic-staging IMAGE_REF="$image" docker compose -p vibecamp-staging -f projects/pos/compose.production.yml up -d --wait
POSTGRES_PASSWORD=synthetic-recovery IMAGE_REF="$image" docker compose -p vibecamp-recovery -f projects/pos/compose.production.yml up -d --wait
docker compose -p vibecamp-staging -f projects/pos/compose.production.yml ps
docker compose -p vibecamp-recovery -f projects/pos/compose.production.yml ps
```

Expected: both projects are healthy and list different named volumes. The base
file exposes the API only inside each Compose network; add target-specific TLS
routing separately. Stop them with the same `-p` and `-f` values plus `down`;
do not add `--volumes` until restore evidence is preserved.
Rollback promotes the recorded previous `IMAGE_REF`; use roll-forward when the
data migration is not safely reversible. Never improvise a data downgrade.

## Failures and hints

Activate or construct only the current C scenario. Record the symptom and one
hypothesis before inspecting the implementation. Use the matching scenario link
in your active block, then its three hint levels in order. Reset to the last
green checkpoint before starting another scenario.

## Evidence

Answer [review prompts](REVIEW.md#review) after the Core proof.

Prove [A1–A7](ACCEPTANCE.md#core) with tenant attack tests, artifact digest,
deployment/migration record, redacted telemetry, restore report, runbooks,
postmortem, release notes, and a cold-reviewed portfolio case study.

## Done when

Every Level C Core gate passes on the declared target, the limitations are
explicit, and a cold reviewer completes the reader path. Then tag and release
`m10-production-saas`.

## Recovery

Use [targeted references](RESOURCES.md#resources-for-m10) only for the question left by the active hint ladder.

Use the versioned runbook for migration, unhealthy release, isolation incident,
and restore procedures. Recovery commands belong in the repository, not memory.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

## Next

Re-run the final portfolio review and choose the next product from evidence,
not from a desire to add infrastructure.

[Previous milestone: M9](../m9-performance-caching-realtime-social/README.md) · [Course home](../../README.md) · [Next: Portfolio review / evidence-led next product](../../templates/PORTFOLIO-CASE-STUDY.md#reader-path)
