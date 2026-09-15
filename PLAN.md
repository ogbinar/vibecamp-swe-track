# Active maintenance plan — subtraction-first cleanup

This is the canonical rationale and execution design for simplifying the
learner-facing repository without weakening its engineering curriculum. The
actionable ledger is [TODO.md](TODO.md). The completed BF0.5–BF6.4
business-first Air migration remains historical context; its prior decision is **ROLL OUT**,
not the active work.

`PLAN.md` and `TODO.md` remain at the repository root. The final SC8 traversal
confirmed that this keeps active work visible to contributors while learners
reach it only through the concise maintainer index; moving the files would add
indirection without reducing learner choices.

## Baseline and rollback anchor

The reviewed baseline is commit
`8942980065c960aad833b1089a6e64035a7eec69`. It is already an immutable Git
object and is the rollback anchor for this work; this planning pass creates no
tag or branch.

At that baseline the repository has 235 tracked files, 13 root Markdown files,
11 milestone directories with four documents each, 15 templates, and 10 files
under `docs/maintainers/`. Root Markdown excluding `AGENTS.md` totals 1,105
lines. Milestone documents total 4,250 lines: 1,779 README, 896 challenge, 669
acceptance, and 906 reference lines. The curriculum validator and mutation suite
total 1,189 lines and defend 42 controlled mutations, including several exact
prose and historical-manifest strings.

The baseline passes `python3 scripts/check_curriculum.py`: M0–M10 exist, all 58
current concept rows resolve to challenge/acceptance evidence, relative links
resolve, and all five starters declare Python 3.13 with exactly `air==0.48.1`.
These are structural facts, not proof of learner comprehension.

## Objective

Make the default GitHub view feel small and obvious:

> choose a milestone → open one learner README → run one next command → observe
> the result → recover or continue

The root README keeps the clear M0–M10 curriculum table. Each milestone should
ultimately present one learner controller, while project setup remains canonical
in the relevant project README. Maintainer policy, history, semantic trace data,
and validation may remain rigorous without competing for learner attention.

This is subtraction first: remove duplicate navigation, repeated process prose,
premature scaffolding, and default-branch history before polishing language or
adding presentation features.

## Non-goals

- Do not redesign the curriculum, renumber milestones, or create alternate tracks.
- Do not lower Core gates, convert required work to Stretch, or remove failure,
  correctness, security, evidence, or recovery obligations.
- Do not blindly inline every project-local behavioral contract into milestone
  prose; preserve a separate contract when it is the clearer canonical authority.
- Do not front-load the full issue/branch/pull-request/Actions/tag ceremony in
  M0. Teach the first green run and diagnosis first, then introduce the workflow
  once and link to it later.
- Do not unify the five independently runnable projects, rewrite their stack,
  update dependencies, or add a frontend runtime.
- Do not treat line count, file count, or a fixed trace count as a substitute
  for semantic coverage or a human usability result.
- Do not commit, push, tag, publish, deploy, use credentials, call providers, or
  claim hosted/named-human evidence without separate authority.

## Protected invariants

- Exactly M0–M10 and the cumulative maturity arc: reproducible, functional,
  persistent, correct, maintainable, secure, resilient, durable, concurrent,
  performant, operable/sellable.
- One sequence and identical Core gates for all learner backgrounds; Core and
  Stretch remain explicit and separate.
- The cycle remains: Understand problem → Design smallest correct solution →
  Build → Test → Break deliberately → Debug → Refactor → Operate → Ship.
- Learners own milestone solutions. Supplied code may provide a runnable neutral
  seam or deterministic failing harness, never the behavior a milestone asks
  them to build.
- Catalog, POS, Ecommerce, Booking, and Social remain independently runnable
  Air/FastAPI projects with locked environments.
- Air owns server-rendered human routes; FastAPI retains JSON, OpenAPI, response
  models, errors, health/readiness, and dependency boundaries. Human routes stay
  out of OpenAPI. Page and API handlers reuse Python behavior and never call each
  other over HTTP.
- PostgreSQL remains durable truth where persistence begins. Transaction,
  authorization, idempotency, concurrency, cache authority, tenant isolation,
  migration, readiness, and restore claims remain testable at their owning boundary.
- Every milestone retains a deterministic Core path, deliberate failure,
  diagnosis, regression proof, recovery route, objective evidence, and honest
  limitation statement.
- The current 58 named concepts remain protected during initial consolidation.
  A later semantic review may merge or rename a row only when its introduction,
  practice, and proof remain explicit. The number 58 is not itself a learning goal.
- External, hosted, provider, deployment, and named-human evidence is never
  inferred from local validation.

## Target learner experience and candidate tree

The first screen of `README.md` states audience, prerequisites, the smallest
successful run, and the curriculum table. Process and references follow the
first useful action. A learner reaches any milestone in one click and needs no
mandatory reading beyond that milestone README and, when setup is required, one
linked project README.

Candidate final tree; exact placement is accepted only after the relevant phase:

```text
README.md
CONTRIBUTING.md
PROGRESS.md
AGENTS.md
LICENSE
milestones/m0-.../README.md ... milestones/m10-.../README.md
projects/{catalog,pos,ecommerce,booking,social}/README.md + runnable project files
templates/{EVIDENCE,DECISION,DATA-LIFECYCLE,INCIDENT,PORTFOLIO}.md
docs/reference/{curriculum-map,glossary,quality,stack}.md
docs/maintainers/{README,curriculum,usability}.md + maintainer templates
scripts/{check_curriculum,test_validator_mutations}.py
.github/
```

During implementation, root `PLAN.md` and `TODO.md` remain present. Their final
location is evaluated only in SC8; removal from root is not presumed.

## Candidate disposition

### KEEP

- Root learner/workflow files: `README.md`, `CONTRIBUTING.md`, `PROGRESS.md`,
  `LICENSE`; keep `AGENTS.md` for repository governance.
- Active planning files: `PLAN.md` and `TODO.md` until SC8 explicitly decides otherwise.
- `projects/catalog/`, `projects/pos/`, `projects/ecommerce/`,
  `projects/booking/`, and `projects/social/` runtime, lock, migration, test,
  failure-harness, reset, and Compose assets.
- One canonical setup/recovery README in each project.
- `.github/workflows/` and the issue/pull-request support that still serves the
  simplified learner workflow.
- The evidence-index, complexity-rejection, data-lifecycle, portfolio, ADR,
  incident, and operations-runbook capabilities, even when templates merge.
- Semantic curriculum validation, secret/safety checks, relative-link checks,
  runtime boundaries, and controlled validator-failure coverage.

### MERGE candidates

- For each `milestones/m*/`, merge `CHALLENGE.md` and `ACCEPTANCE.md` into the
  point-of-use sections of its `README.md`; merge only the just-in-time concepts,
  tool decisions, and sources from `REFERENCE.md`. Delete source files only after
  a bidirectional semantic audit passes.
- Merge `templates/EVIDENCE-EXAMPLES.md` into `templates/EVIDENCE-INDEX.md`.
- Merge `templates/ENTRY-DIAGNOSTIC.md` into the M0 learner route if the result
  remains runnable without making M0's first screen longer.
- Merge `templates/INCIDENT-POSTMORTEM.md` with
  `templates/RUNBOOK-INCIDENT.md`; merge the migration, release-rejection, and
  restore runbooks only if distinct commands, owners, and evidence remain obvious.
- Merge `challenges/README.md` policy into maintainer guidance after all active
  learner links point directly to milestone scenarios.

### MOVE candidates

- `CURRICULUM.md` → `docs/reference/curriculum-map.md`
- `STACK.md` → `docs/reference/stack.md`
- `QUALITY-GATES.md` → `docs/reference/quality.md`
- `GLOSSARY.md` → `docs/reference/glossary.md`
- `USABILITY.md` → `docs/maintainers/usability.md`
- `templates/SEMANTIC-AUDIT.md` and `templates/TRANSITION-REVIEW.md` →
  `docs/maintainers/templates/`
- Stable machine-readable milestone/concept mappings →
  `docs/maintainers/curriculum.yml` or an equivalently compact manifest.
- `PLAN.md` and `TODO.md` only in SC8, and only if a cold maintainer traversal
  shows that root removal improves learner choice without hiding active work.

### DELETE-from-default-branch candidates

Deletion means removal in a reviewed future commit; Git commit `8942980` remains
the source-level rollback. No deletion occurs during this planning pass.

- Pure indirection: `ANALYSIS.md`, `PERSONA-REVIEW.md`.
- Redundant directory summaries after links are repaired: `projects/README.md`,
  `challenges/README.md`.
- Completed history after provenance review: `docs/maintainers/archive/**` and
  `docs/maintainers/business-first-career-shifter-review.md`.
- Merged milestone support files, redundant project contracts, examples, and
  templates only after their canonical destination and inbound links pass.
- Exact-string validator rules whose only purpose is preserving wording,
  completed plans, source-hash row counts, or one presentation implementation.

## Project-local contract decision rule

Do not merge `projects/*/REQUIREMENTS.md`, `projects/*/specs/*.md`, or
`projects/ecommerce/fixtures/SECURITY-SCENARIOS.md` by default. Decide each file
using the same test:

1. KEEP project-local when it is executable or consumer-facing, is used by more
   than one milestone, defines a stable API/data/threat contract independently
   of lesson sequencing, or would make the milestone controller materially harder
   to scan.
2. MERGE into one milestone README when it serves only that milestone, is short,
   and removes a navigation hop without duplicating authority.
3. MOVE to maintainer data when it exists only for automated trace or release checks.
4. DELETE only after every behavior maps from requirement → challenge → Core
   criterion → command/evidence in both directions and all inbound links change.

The likely initial results are to keep the M1 HTTP, M5 security, M6 provider,
M7 job, M8 booking, M9 feed, and M10 tenant/recovery contracts project-local;
evaluate the short M2 requirements and M4 change brief for inline merge. This is
a hypothesis, not a pre-approved deletion list.

## No-solution boundary repairs

The current starters cross their own stated boundary in three places. Repair
these in a dedicated phase while preserving a green neutral starter:

- Catalog: remove the learner-facing M1 `ProductDraft`/`ProductDraftForm` route
  behavior and its passing form tests from `projects/catalog/`; keep the M0 Air
  page, `/health`, `/products/sample`, and an intentionally red M1 contract.
- Ecommerce: remove the prebuilt M6 HTMX payment-status page/fragment and tests;
  keep the provider fake, failure harnesses, anonymous Air/FastAPI shell, and
  learner-owned M5/M6 contract boundaries.
- Social: remove the prebuilt M9 HTMX/SSE transport and passing SSE test; keep a
  simple Air page, FastAPI health/readiness, deterministic feed/N+1 harness, and
  learner-owned database/cache/realtime work.
- Remove premature placeholder routes after checking each one: POS
  `/app/checkout` and `/app/operator`; Ecommerce `/app/jobs`; and any identity,
  order, or later-milestone placeholder that makes absent behavior appear built.
  Retain current-milestone neutral pages such as POS stock and Booking's final-seat
  observation when they expose a problem without supplying its repair.

## Staged execution

- **SC0 — Freeze facts and decision ledger.** Reconfirm baseline, enumerate
  inbound links and canonical owners, record current green/red behavior, and
  define slice-specific rollback from `8942980`. No deletion.
- **SC1 — Remove root/default-branch process weight.** Shorten the root learner
  route; remove only approved indirection and redundant history/summary files
  after backlink and provenance checks. Keep PLAN/TODO at root.
- **SC2 — Pilot one-README milestones and contract decisions.** Pilot M0, M1,
  M6, and M9 because they span first-run, public API, external uncertainty, and
  performance/realtime risk. Decide project-local specs individually.
- **SC3 — Repair starter no-solution boundaries.** Remove the prebuilt M1 form,
  M6 HTMX fragment, M9 SSE/HTMX transport, and approved premature placeholders;
  retain runnable Air/FastAPI shells and intended red learner contracts.
- **SC4 — Consolidate M2–M5, M7–M8, and M10.** Roll out the accepted controller
  pattern with semantic audits and no blind contract merging.
- **SC5 — Consolidate templates and move optional reference material.** Reduce
  duplicate learner choices while preserving evidence/decision/incident/operation
  capabilities and updating all links.
- **SC6 — Simplify validation machinery.** Move stable semantics into a compact
  manifest; replace prose-string and historical-shape checks with schema,
  traceability, link, safety, no-solution, API/OpenAPI, and runtime checks. Keep
  a small representative mutation suite.
- **SC7 — Full validation and repair.** Run structural, runtime, database,
  deliberate-red/reset, recovery, container, safety, and local traversal gates.
- **SC8 — Polish and final information-architecture decision.** Only after the
  removal stages pass, tighten language and anchors, run fresh-context review,
  and decide whether PLAN/TODO should remain at root or move.

## Quantitative, non-gameable targets

Counts are diagnostic ceilings tied to learner behavior, not success by themselves:

- Root → any milestone: one link from the curriculum table.
- Milestone → first executable action: no prerequisite document hop; at most one
  additional project-README hop when environment setup is genuinely shared.
- Exactly one learner controller README per milestone after SC4; support data may
  exist outside the milestone directory but cannot create a competing learner path.
- Each required block names one action, expected observation, evidence location,
  and recovery route. Removing words must not remove any of those four facts.
- One canonical owner per requirement, command, evidence rule, and concept trace;
  automated duplicate-authority and broken-link checks must pass.
- Reduce 44 learner-visible milestone choices to 11 only if all Core behaviors
  still pass the bidirectional semantic audit.
- Reduce 15 templates only to the number of distinct workflows learners actually
  invoke; every retained/merged capability must have an active milestone consumer.
- No increase in mandatory tools, accounts, services, or first-run commands.
- The named concept set has zero unexplained losses; a count change requires an
  explicit semantic mapping rather than a rewritten constant.
- A fresh-context reviewer can identify the current product, first command,
  expected result, and recovery route without opening maintainer material.

## Risks and controls

- **Semantic loss:** audit requirement/challenge/acceptance/evidence mappings in
  both directions before deleting a source.
- **Broken historical links:** inventory inbound links, publish an old→new anchor
  map in the eventual cleanup change, and restore affected files from `8942980`
  if compatibility cannot be repaired in-slice.
- **False green starters:** test both neutral green behavior and intended red
  learner contracts; never weaken a test merely to restore green.
- **No-solution regression:** inspect supplied source and tests for milestone
  outcomes already implemented; require a named red starting observation.
- **Validator overfitting or weakening:** classify every removed rule as semantic,
  safety, runtime, presentation, or history; preserve the first three, justify
  presentation checks by learner behavior, and remove history-only coupling.
- **Contributor disorientation:** keep active PLAN/TODO discoverable until SC8
  and maintain one short maintainer index.
- **Large unsafe change:** implement one phase or product slice per reviewable
  change; stop on unexplained dirty files, broken rollback, or ambiguous authority.

## Acceptance and rollback gates

A phase may close only when its matching TODO items and evidence pass. At minimum:

1. `git diff --check`, changed-path inspection, relative links/anchors, and the
   phase-appropriate curriculum validator pass.
2. Requirement → challenge → Core → command/evidence mappings have no loss or
   duplicate canonical owner.
3. Affected project lint, format, mypy, tests, API/OpenAPI checks, and relevant
   PostgreSQL/migration/recovery checks pass.
4. Intended learner-start failures still fail for the documented reason and
   reset or neutral baseline returns green.
5. No secret, personal data, generated archive, callable vulnerable route,
   completed learner solution, internal HTTP call, or second frontend runtime is added.
6. A source traversal reaches the next action and recovery without relying on a
   deleted page. Human comprehension remains unclaimed until named review.

Rollback is slice-specific: restore only affected paths from
`8942980065c960aad833b1089a6e64035a7eec69`, repair links and generated lock
state if applicable, then rerun that slice's last-green commands. Never reset or
overwrite unrelated learner or maintainer work.

## External limits

The required M6 sandbox experiment, optional provider/tool endorsements,
hosted GitHub rendering and Actions observation, optional real deployment, and
named-human career-shifter review remain separately unchecked in TODO. Local
source/runtime evidence cannot satisfy them. No provider call, credential use,
deployment, publication, external message, commit, push, or tag is authorized
by this plan.
