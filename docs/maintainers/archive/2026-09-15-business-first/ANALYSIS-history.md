# Career-shifter curriculum resolution analysis

Date: 2026-09-13  
Status: proposed decisions before implementation  
Source: [whole-repository persona review](PERSONA-REVIEW-history.md)

## Decision question

How should the curriculum become independently usable by a career shifter while
preserving demanding, production-quality engineering outcomes?

## Conclusion

The standards should not be lowered and completed learner solutions should not
be added. The repository needs a clearer bridge from each engineering problem to
the learner's next independently executable action.

The correct intervention is **contract and process scaffolding**:

- fix the intended product behavior;
- supply a runnable starting boundary;
- identify what is provided and what the learner creates;
- divide work into observable, resumable steps;
- provide deterministic red and green signals;
- leave implementation and engineering trade-offs learner-owned.

This preserves productive struggle. It removes accidental struggle caused by
missing requirements, infrastructure, or instructions.

## Resolution principles

1. Preserve exactly M0–M10 and the existing capability sequence.
2. Preserve the seven-file milestone contract.
3. Keep README as the only learner front door and each milestone README as its
   lesson controller.
4. Keep the default FastAPI, PostgreSQL, SQLAlchemy, Alembic, pytest, HTTPX,
   Ruff, mypy, uv, Docker, and GitHub stack.
5. Add no completed milestone solutions.
6. Supply neutral infrastructure and public contracts when they are prerequisites
   for the actual learning problem.
7. Introduce professional evidence and workflow progressively rather than all at
   once.
8. Distinguish structural verification, runnable-starter verification, and human
   self-study verification.

## Conflict decisions

### Productive struggle versus blank-canvas work

**Conflict:** Experienced engineers value open design freedom. Career shifters
cannot learn the intended skill when they must also invent requirements,
application boundaries, failure triggers, and proof methods.

**Decision:** Supply the public contract, starting state, extension points,
failing test or harness contract, expected observation, and acceptance proof.
The learner owns the internal design and repair.

**Do not:** supply final repositories, services, transaction code, authorization
policies, locks, caching, or worker solutions.

### Professional rigor versus cognitive load

**Conflict:** Issues, PRs, CI, evidence, runbooks, reviews, and releases are real
engineering work, but applying the full ritual to every small learner change is
overwhelming.

**Decision:** Use two PR modes:

- **Working PR:** focused behavior, narrow tests, risk note, and next step.
- **Milestone gate PR:** full acceptance evidence, failure/recovery proof,
  self-review, cold review, progress update, and release/tag.

Introduce evidence types only when the related engineering problem appears.

### Concision versus comprehension

**Conflict:** Short files are easy to scan, but compressed noun-heavy paragraphs
are difficult to learn from.

**Decision:** Keep documents concise through structure, not compression. Use
short concept cards, examples, timelines, and numbered work blocks. Each
paragraph should normally contain no more than three sentences.

### Seven fixed files versus uneven milestone complexity

**Conflict:** M0 and M10 cannot have the same internal complexity even though a
consistent file contract improves navigation.

**Decision:** Keep seven files. Scale complexity inside them using numbered work
blocks and challenge/acceptance sub-IDs such as `C2.1` and `A2.1`. Do not add an
eighth lesson file.

### Fixed requirements versus learner creativity

**Conflict:** Completely open product briefs make assessment inconsistent;
over-prescription removes design judgment.

**Decision:** Provide one fixed Core customer and behavior contract with
Given/When/Then examples. The learner chooses internal design. Product
personalization belongs in Stretch work after Core passes.

### Minimal stack versus sufficient starter scaffolding

**Conflict:** Adding infrastructure risks hiding fundamentals, but asking a
learner to bootstrap unrelated infrastructure prevents them from reaching the
intended lesson.

**Decision:** Give M5, M8, and M9 a neutral FastAPI/PostgreSQL/SQLAlchemy/Alembic
foundation similar to POS. This is existing Core stack, not additional
architecture. Leave domain tables and milestone solutions learner-owned where
their design is the learning objective.

### Deterministic toy fixtures versus transfer to production mechanisms

**Conflict:** In-memory fixtures reveal races, duplicate work, and N+1 shapes
cleanly, but they do not teach database or process behavior by themselves.

**Decision:** Retain each toy demonstration as the first observation. Follow it
with a supported bridge into the real application stack: a named extension
point, database/application shell, deterministic integration harness, and staged
checks.

### Safe security teaching versus realistic vulnerabilities

**Conflict:** Security mistakes must be diagnosed, but callable vulnerable routes
or real leaked secrets are unsafe teaching artifacts.

**Decision:** Use synthetic data, isolated test-only mutations, negative tests,
and activation mechanisms that cannot be enabled in ordinary runtime
configuration. CI must reject callable vulnerable fixtures.

### Optional tools versus mandatory competence

**Conflict:** Redis and similar tools should only remain when earned, but the
learner still needs practical experience evaluating them.

**Decision:** Distinguish three states everywhere:

- **Required experiment:** exercise and measure the tool in an isolated branch.
- **Optional retention:** keep it only if evidence shows net benefit.
- **Do not introduce:** the prerequisite problem has not occurred.

For M9, the Redis experiment is required; retaining Redis in the final product is
optional.

### Cookie sessions versus JWT

**Conflict:** Comparing both teaches judgment, but choosing without a declared
client is arbitrary and implementing both overloads M5.

**Decision:** Define the Core ecommerce client as a first-party browser. Use a
server-side opaque session referenced by a secure cookie for Core. Require a
short comparison with JWT. Make a JWT implementation a bounded Stretch or later
external/mobile-client exercise.

### Real operations versus equitable access

**Conflict:** A production claim requires more than a local toy, but a mandatory
paid host introduces hidden cost, accounts, and security prerequisites.

**Decision:** Define two honest outcomes:

- **M10 Core — production rehearsal:** a complete local two-environment release,
  migration, readiness, rollback/roll-forward, restore, and incident exercise.
- **Operable/Sellable endorsement:** the same controls proven on an authorized
  real target with TLS, secret custody, monitoring, encrypted backups, and
  measured recovery.

The course can be completed without falsely claiming live production operation.
The stronger final claim requires real-target evidence.

### Local build versus CI-built immutable artifact

**Conflict:** The current README builds locally and copies a tar with SCP, while
acceptance requires the exact artifact built by CI.

**Decision:** Use GitHub Actions to build and publish an immutable image to
GitHub Container Registry, then deploy by digest. The local rehearsal may build
an image locally but must not claim it is the CI artifact. Store any local archive
under ignored `dist/`, record its checksum, and never commit it.

### Default worker versus earned worker

**Conflict:** M10's reference target assumes a POS worker, but the M4 POS lineage
has not earned one.

**Decision:** Remove the worker from the default M10 topology. Add it only if the
fixed POS customer scenario includes a concrete durable background obligation.
M7 already teaches worker semantics in ecommerce.

### Automated confidence versus human learner evidence

**Conflict:** Structural and scripted checks are valuable but cannot show that a
career shifter understands what to do.

**Decision:** Publish separate statuses:

- `STRUCTURALLY READY`;
- `STARTER VERIFIED`;
- `HUMAN SELF-STUDY VERIFIED`.

Never infer the third status from the first two.

### Self-paced progression versus session guidance

**Conflict:** Week-based deadlines violate the course model, but unbounded
milestones are difficult to pause and resume.

**Decision:** Use outcome-based work blocks and safe stopping points. Optional
effort ranges may help planning, but time spent never determines advancement.

## Repository-wide remedies

### One learner-owned start path

The learner should:

1. create a repository from the GitHub template;
2. clone only the owned repository;
3. verify that `origin` points to it;
4. run the catalog baseline;
5. add `upstream` only when curriculum updates are needed.

Define `origin`, `upstream`, staging, branch, pull request, CI, and annotated tag
before their first required use. Replace “keep all branches disabled” with
“leave **Include all branches** unchecked.”

Declare Linux, macOS, and WSL2 as supported environments unless tested
PowerShell equivalents are added. Include a “needed now / needed later” map for
GitHub authentication, Docker, PostgreSQL, and the real M10 target.

### Milestone learner-controller contract

Every M1–M10 README should contain 3–6 numbered work blocks. Each block states:

- `REQUIRED`, `OPTIONAL`, or `CHOOSE ONE`;
- one business or operator outcome;
- what is supplied;
- what the learner creates or changes;
- exact working directory and likely files;
- one initial red signal or observation;
- one narrow green command and expected result;
- evidence destination;
- reset/recovery route;
- safe stopping point and next block.

### Challenge contract

Replace “activate or construct” with exactly one label:

- `PROVIDED — run this; expect this; reset with this`, or
- `YOU BUILD — create this bounded harness; it must produce this observation`.

Use sub-IDs where one challenge currently bundles several behaviors. Map every
sub-ID to an acceptance sub-ID, command, expected observation, and evidence path.

### Language contract

Teach each necessary term as:

> **Term — plain-language meaning.** A short example showing why it matters in
> the current product.

Correct the glossary's two semantic collisions:

- distinguish a network port from an architectural port;
- define HTTP `safe` separately from `idempotent`.

Prioritize M5, M7, M8, M9, and M10 terminology. Move the detailed advanced-tool
exclusion list from the learner front door to `STACK.md`.

### Evidence and progress contract

- Provide milestone-specific evidence bootstrap instructions.
- Mark non-applicable template fields explicitly.
- Show one compact completed synthetic example for each new evidence type.
- Align `PROGRESS.md` field names with its pause instructions.
- Provide one filled synthetic pause/resume example.
- End every hint ladder with a focused GitHub issue format containing expected
  result, actual result, first error, attempted diagnosis, and relevant evidence.

## Milestone resolutions

### M0 — Engineering Baseline

Keep M0 as the presentation reference. Change only the repository ownership
sequence, supported-environment statement, staged GitHub workflow, and
M0-specific evidence guidance.

### M1 — Production-minded API Foundation

Create six slices:

1. create product;
2. retrieve and missing product;
3. complete replacement;
4. retire and repeat;
5. ordered pagination;
6. compatibility regression.

Reconcile the product brief, challenge, supplied contract, and acceptance gate.
Do not tell the learner to add the already-supplied OpenAPI check. Publish all
required error codes and shapes. Change the compatibility activator so it mutates
application behavior while the consumer contract remains stable.

### M2 — POS Persistence and Data Modeling

Provide fixed endpoint/error examples, named model/metadata extension points, a
legacy-data migration fixture, a query-count boundary, a literal database reset
command, and stronger parsed-target reset protection. Keep table design,
constraints, indexes, and mappings learner-owned. Correct the A1–A4/A1–A5
inconsistency.

### M3 — Transactions and Correctness

Publish checkout request/response examples, allowed state transitions, inventory
and payment rules, tax/discount/rounding order, void/refund behavior, and a
deterministic competing-sale harness. The learner decides transaction and
invariant placement.

### M4 — Maintainability, Testing, and Refactoring

Supply one exact stakeholder change, an intentionally awkward bounded baseline
or patch, change-scatter measurement, and a failing module-boundary check. Do not
ask the learner to invent “bad” architecture. Keep the characterization tests
and refactor learner-owned.

### M5 — Secure Multi-user Ecommerce

Add a neutral PostgreSQL/SQLAlchemy/Alembic foundation with readiness, migration,
configuration, reset, and empty persistence extension points. Declare the Core
first-party browser client. Stage identity, session lifecycle, role policy,
object ownership, and order-state authorization. Standardize `fulfilled` versus
`shipped` and publish the command-to-state matrix.

### M6 — Resilient External Integrations

Supply an explicit provider port and deterministic connect/read/total timeout,
rate-limit, server-error, malformed-response, before-effect, and after-effect
fixtures. Add signed raw-body webhook examples, timestamps, replay rules, a retry
budget, customer-visible unknown state, and reconciliation command. Leave the
adapter and state-handling implementation learner-owned.

### M7 — Durable Background Processing

Stage lost in-process work, atomic durable intent, claiming/replay, retries and
quarantine, then operation/recovery. Supply a job-state contract, outbox extension
point, worker command skeleton, deterministic clock/kill hooks, one/two-worker
commands, and an initial replay runbook. Taskiq remains optional after Core.

### M8 — Booking Concurrency Lab

Keep the in-memory barrier demonstration, then provide a neutral FastAPI,
PostgreSQL, SQLAlchemy, Alembic, and Compose shell. Define sequential reservation,
hold, confirmation, cancellation, and expiration behavior. Supply a database
reset and deterministic two-connection race harness. Leave concurrency mechanism
selection learner-owned.

### M9 — Performance, Caching, and Realtime

Provide a PostgreSQL-backed feed shell, deterministic database seed/reset,
query-count capture, `EXPLAIN` workflow, reference workload, cursor contract, and
one-way update requirement. Stage query shape, pagination, controlled Redis
experiment, and realtime decision separately. Require the Redis experiment but
make retention optional. Use SSE for the Core one-way requirement; keep a
WebSocket implementation Stretch unless bidirectional behavior is required.

### M10 — Production Multi-tenant SaaS Capstone

Supply one fixed reference customer and stage:

1. tenant-safe sale;
2. append-only audit evidence;
3. one user-impact observability question;
4. immutable build and migration;
5. unhealthy-release rejection;
6. backup restore;
7. incident response;
8. customer/operator handoff.

Provide local production rehearsal and real-target endorsement paths. Align CI,
GitHub Container Registry, artifact digest, deployment, migration, readiness,
and recovery. Do not prescribe a worker without a concrete durable obligation.

## Implementation sequence

### Pass 1 — Correct contradictions and claims

- Unify repository ownership.
- Declare supported environments and later prerequisites.
- Fix M1 OpenAPI and compatibility exercises.
- Fix M2 acceptance-ID mismatch.
- Standardize ecommerce state names.
- Resolve M9 Redis and realtime requirements.
- Resolve M10 artifact, host, and worker policies.
- Correct M8/M9 command and recovery wording.
- Replace broad self-service claims with staged readiness labels.

### Pass 2 — Make transitions feasible

- Add the M5 persistence foundation.
- Add the M8 database/API foundation.
- Add the M9 database/API/load foundation.
- Add bounded product contracts for M2–M10.
- Align M6/M7 fixtures with their acceptance claims.

### Pass 3 — Make the route executable

- Convert M1–M10 to numbered work blocks.
- Label every challenge `PROVIDED` or `YOU BUILD`.
- Atomize challenge and acceptance criteria.
- Add commands, expected observations, evidence paths, stopping points, and
  recovery.

### Pass 4 — Reduce language and process friction

- Rewrite dense concept material as example-first cards.
- Define decision-driving terminology at first use.
- Simplify early evidence and progress guidance.
- Split working and milestone-final PR requirements.
- Add the shared escalation ladder.
- Document how CI evolves with learner work.

### Pass 5 — Make the production claim honest

- Stage M10 into independently green passes.
- Add local rehearsal and real-target endorsement.
- Align immutable artifact production and deployment.
- Add milestone-appropriate secret, dependency, and container checks.
- Add restore, incident, runbook, and portfolio reader-path scaffolding.

## Repeat-until-complete control loop

After each pass:

1. Run the structural validator.
2. Run all supplied starters and intended-failure harnesses.
3. Check requirements → challenge → acceptance → command → evidence agreement.
4. Perform a fresh career-shifter walkthrough.
5. Record confusion, unsupported choices, failed commands, and recovery results.
6. Reopen every failed item and repair the smallest underlying contract.
7. Repeat until all ten learner-experience dimensions reach at least 4/5.

Human cold-test these transitions before claiming end-to-end self-sufficiency:

- repository → M0;
- M0 → M1;
- M1 → M2;
- M4 → M5;
- M7 → M8;
- M8 → M9;
- M9 → M10.

## Completion conditions

The resolution is complete only when:

- one owned-repository route reaches M0 without moving work between clones;
- every milestone has resumable learner work blocks;
- every Core challenge identifies supplied and learner-created artifacts;
- every Core acceptance item has an observable result and evidence route;
- M5, M8, and M9 start with the infrastructure their Core gates require;
- known M1, M2, M5, M9, and M10 contradictions are removed;
- terminology is taught at first use rather than only collected later;
- M10's local and real-target claims are explicit and evidence-backed;
- the validator reports structural status without implying learner readiness;
- human transition tests complete without author intervention;
- unresolved friction is tracked rather than hidden by an aggregate score.

Until these conditions pass, the honest status is:

> **Strong curriculum design and verified starter demonstrations, with incomplete
> end-to-end self-study scaffolding.**
