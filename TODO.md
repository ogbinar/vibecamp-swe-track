# Active curriculum maintenance checklist

This is the execution ledger for the subtraction-first cleanup in
[PLAN.md](PLAN.md). Every SC item begins unchecked. Check an item only after its
named evidence and commands pass; planning, intention, or a partial run is not
completion. If a stop condition fires, leave the item unchecked, record the
failure, and restore only the affected slice from
`8942980065c960aad833b1089a6e64035a7eec69`.

## Historical context — completed

- [x] **BF0.5–BF6.4 — Business-first Air-primary migration.** The former
  seven-file milestones were consolidated to four, outcome-first controllers
  and the root roadmap were introduced, five Air/FastAPI starters were locally
  verified, and external/human limits remained explicit. This is context, not
  the active checklist.

## Global execution rules

- [x] **SC-G1 — Checkbox discipline.** Keep every SC checkbox unchecked until
  its complete acceptance evidence exists. Never bulk-check a phase from prose
  review or a downstream green command.
- [x] **SC-G2 — Scope discipline.** Before and after each change, run
  `git status --short` and inspect `git diff --name-only`; stop if an unexplained
  path appears. Preserve learner work and unrelated dirty files.
- [x] **SC-G3 — No external mutation.** Do not commit, push, tag, publish,
  deploy, call a provider, use credentials, or contact a reviewer without
  separate explicit authority.
- [x] **SC-G4 — Slice rollback.** Before removal, record affected paths,
  last-green commands, and exact `8942980` restore sources. Never use a
  repository-wide reset as rollback.

## SC0 — Baseline, authority, and removal gates

Dependencies: none. No deletion, move, merge, or starter edit is allowed in SC0.

- [x] **SC0.1 — Reconfirm inventory.** Record commit, clean/dirty state, tracked
  paths, root Markdown, 11×4 milestone files, templates, maintainer history, and
  root/milestone line totals. Expected: reconcile with PLAN or explain drift.
- [x] **SC0.2 — Capture canonical ownership.** Name exactly one owner and all
  inbound links for curriculum, workflow, progress, quality, stack, glossary,
  milestone behavior, project setup/contracts, evidence, and maintainer policy.
- [x] **SC0.3 — Capture semantic baseline.** Run
  `python3 scripts/check_curriculum.py` and
  `python3 scripts/test_validator_mutations.py`. Expected: the unmodified
  candidate passes and each controlled mutation fails for its intended reason.
  Save output as maintenance evidence, not learner evidence.
- [x] **SC0.4 — Capture starter green/red matrix.** Record locked Ruff, format,
  mypy, ordinary test, API/OpenAPI, PostgreSQL/migration, and deliberate red/reset
  results for each applicable project. Do not infer unavailable checks.
- [x] **SC0.5 — Build removal ledger.** For every candidate path, record
  KEEP/MERGE/MOVE/DELETE, destination, backlinks, semantic content, validation
  owner, and slice restore command from `8942980`.
- [x] **SC0.6 — Gate SC1.** Run `git diff --check`; verify SC0 changed only
  approved planning/evidence paths and removed nothing. Stop if ownership,
  provenance, baseline behavior, or rollback is ambiguous.

## SC1 — Root and default-branch subtraction

Dependencies: SC0.1–SC0.6. Keep `PLAN.md` and `TODO.md` at root.

- [x] **SC1.1 — Shorten `README.md`.** Retain audience, prerequisites, smallest
  successful run, M0–M10 table, one course-loop explanation, and secondary
  reference/maintainer links. Evidence: the first product, command, expected
  result, and recovery are findable without prerequisite reading.
- [x] **SC1.2 — Evaluate root indirection.** Backlink/provenance-check
  `ANALYSIS.md` and `PERSONA-REVIEW.md`; delete only when active decisions have a
  canonical owner and no live route needs the stubs.
- [x] **SC1.3 — Evaluate directory summaries.** Merge active policy from
  `projects/README.md` and `challenges/README.md`, repair links, then remove only
  if direct routes are clearer.
- [x] **SC1.4 — Evaluate default-branch history.** Check
  `docs/maintainers/business-first-career-shifter-review.md` and
  `docs/maintainers/archive/**`; delete only after unique active decisions move
  and Git `8942980` is proven sufficient recovery.
- [x] **SC1.5 — Keep planning discoverable.** Root README's maintainer link must
  reach root PLAN/TODO through one concise index. Do not move them in SC1.
- [x] **SC1.6 — Verify SC1.** Run `git diff --check`, changed-path inspection,
  links/anchors, `python3 scripts/check_curriculum.py`, and root→M0 traversal.
  Stop and restore the smallest slice if learner action, authority, or recovery
  is lost.

## SC2 — One-README pilot and contract decisions

Dependencies: SC1.1–SC1.6. Pilot only M0, M1, M6, and M9.

- [x] **SC2.1 — Define one controller.** Require business problem, product
  result, first command, point-of-use challenge, Core/Stretch, evidence,
  recovery, next action, and optional sources in one milestone README. Avoid
  exact prose requirements when semantic structure is sufficient.
- [x] **SC2.2 — Consolidate M0.** Merge
  `milestones/m0-engineering-baseline/{CHALLENGE,ACCEPTANCE,REFERENCE}.md` into
  README. The first green run and diagnosis precede GitHub ceremony.
- [x] **SC2.3 — Consolidate M1.** Merge milestone support while keeping
  `projects/catalog/specs/M1-PRODUCT-BRIEF.md` project-local unless the decision
  rule proves inline ownership clearer. Preserve red contract, HTTP/OpenAPI,
  Core/Stretch, and M0 regression behavior.
- [x] **SC2.4 — Consolidate M6.** Preserve uncertainty, fake, retry, webhook,
  reconciliation, and external-evidence limits. Decide
  `projects/ecommerce/specs/M6-INTEGRATION-CONTRACT.md` independently; do not
  duplicate its full contract.
- [x] **SC2.5 — Consolidate M9.** Preserve equal-workload measurement,
  PostgreSQL authority, Redis retain/remove, SSE loss/replay, and WebSocket
  Stretch. Decide `projects/social/specs/M9-FEED-CONTRACT.md` independently.
- [x] **SC2.6 — Decide every project contract individually.** Apply PLAN's rule
  to `projects/*/REQUIREMENTS.md`, `projects/*/specs/*.md`, and
  `projects/ecommerce/fixtures/SECURITY-SCENARIOS.md`; record rationale and
  destination. No blanket merge/delete is allowed.
- [x] **SC2.7 — Audit semantics both ways.** Trace every Core requirement to
  scenario, criterion, command/observation, and evidence and back again.
  Expected: no loss, invention, or duplicate owner.
- [x] **SC2.8 — Verify navigation.** Fresh-context traversal finds the first
  action without a prerequisite document hop and uses at most one shared project
  setup README. Record wrong turns.
- [x] **SC2.9 — Gate rollout.** Run diff, link, validator/mutation, and affected
  project checks. Stop if choices are not reduced, a semantic gate disappears,
  or canonical routes compete.

## SC3 — Repair no-solution starter boundaries

Dependencies: SC2 pilot contract and SC0 starter baselines.

- [x] **SC3.1 — Catalog M1 form.** Remove supplied `ProductDraft`/
  `ProductDraftForm` page behavior and passing form tests. Keep the M0 Air page,
  `/health`, `/products/sample`, composition, and intentionally red M1 contract.
- [x] **SC3.2 — Ecommerce M6 HTMX.** Remove supplied payment-status HTMX
  page/fragment and passing fragment test. Keep the anonymous shell,
  `FakeProvider`, signed fixtures, retry budget, and failure harnesses.
- [x] **SC3.3 — Social M9 SSE/HTMX.** Remove supplied SSE endpoint,
  `SSEResponse`, HTMX SSE attributes, and passing transport test. Keep a simple
  Air feed, health/readiness, N+1 reproduction, and query seams.
- [x] **SC3.4 — Evaluate premature placeholders.** Check POS `/app/checkout`
  and `/app/operator`, Ecommerce `/app/jobs`, plus M5 identity/order placeholders.
  Remove only routes implying built behavior; retain current-problem observations.
- [x] **SC3.5 — Prove neutral green and intended red.** Catalog M0, Ecommerce
  shell/harnesses, and Social small feed pass. M1, learner-owned M5, and M9
  starting failures remain red only for documented reasons. Do not weaken tests.
- [x] **SC3.6 — Prove framework boundaries.** API/OpenAPI behavior remains;
  Air routes stay excluded; scans find no internal HTTP, custom JavaScript,
  second frontend runtime, or completed learner solution.
- [x] **SC3.7 — Verify SC3.** Run affected locked Ruff/format/mypy/tests,
  curriculum validator/mutations, and `git diff --check`. Restore the project
  slice if a runnable shell or deterministic failure seam is lost.

## SC4 — Remaining milestone consolidation

Dependencies: SC2.9 and SC3.7.

- [x] **SC4.1 — Consolidate M2–M3.** Preserve schema/query/migration,
  transaction/money/race, PostgreSQL evidence, and recovery. Evaluate short M2
  requirements for merge; presume the M3 contract stays project-local.
- [x] **SC4.2 — Consolidate M4–M5.** Preserve cashier-name change,
  characterization/refactor, threat/ownership/state matrices, negative tests,
  lifecycle, portfolio, and JWT Stretch.
- [x] **SC4.3 — Consolidate M7–M8.** Preserve durable intent,
  at-least-once/idempotent replay, lease/quarantine, barrier races, database
  invariants, deadlock, authoritative time, and bounded retry.
- [x] **SC4.4 — Consolidate M10.** Preserve tenant isolation, audit, telemetry,
  immutable artifact, migration/readiness/rejection, isolated restore, incident,
  lifecycle, handoff, and optional real-target boundary.
- [x] **SC4.5 — Remove merged support files.** Only after each audit passes,
  remove milestone `CHALLENGE.md`, `ACCEPTANCE.md`, and `REFERENCE.md`; expected:
  exactly one learner README and no competing controller per milestone.
- [x] **SC4.6 — Re-map current concepts.** Record old row/ID → new README anchor
  for every concept. Explain merges/renames; do not force the count to 58.
- [x] **SC4.7 — Verify SC4.** Run semantic audits, links/anchors,
  validator/mutations, affected project checks, and `git diff --check`. Stop on
  lost Core/Stretch, failure, evidence, recovery, API, or no-solution behavior.

## SC5 — Templates and global references

Dependencies: SC4.1–SC4.7.

- [x] **SC5.1 — Merge evidence examples.** Fold
  `templates/EVIDENCE-EXAMPLES.md` and useful Catalog examples into
  `EVIDENCE-INDEX.md`; retain clear synthetic labels.
- [x] **SC5.2 — Place entry diagnostic.** Inline or directly route
  `ENTRY-DIAGNOSTIC.md` without a prerequisite hop or weaker D1–D5 behavior.
- [x] **SC5.3 — Consolidate incident/operations templates.** Evaluate
  `INCIDENT-POSTMORTEM.md` + `RUNBOOK-INCIDENT.md` and the migration,
  release-rejection, and restore runbooks. Preserve triggers, owners, commands,
  stop conditions, integrity checks, and evidence.
- [x] **SC5.4 — Preserve distinct capabilities.** Keep ADR, complexity
  rejection, lifecycle, requirement-change, and portfolio work wherever active
  milestones invoke it; merge only proven duplicate fields.
- [x] **SC5.5 — Move maintainer templates.** Move `SEMANTIC-AUDIT.md` and
  `TRANSITION-REVIEW.md` to `docs/maintainers/templates/`; repair links/checks.
- [x] **SC5.6 — Evaluate root reference moves.** Decide moves for
  `CURRICULUM.md`, `STACK.md`, `QUALITY-GATES.md`, `GLOSSARY.md`, and
  `USABILITY.md` to PLAN's `docs/` candidates. Preserve first-use definitions.
- [x] **SC5.7 — Verify consumers.** Every retained template has an active
  milestone consumer and each artifact has one template or inline schema. A
  lower count alone is not completion.
- [x] **SC5.8 — Verify SC5.** Run links, semantic audits, validator/mutations,
  source traversal, and `git diff --check`. Stop if evidence or recovery becomes
  less executable.

## SC6 — Validator simplification

Dependencies: accepted SC4 and SC5 structures.

- [x] **SC6.1 — Classify rules.** Label every validator check and mutation as
  semantic, safety, runtime, navigation, presentation-only, or history-only.
- [x] **SC6.2 — Add compact manifest.** Represent milestone order/outcome,
  Core/Stretch IDs, requirement/scenario/evidence mappings, project ownership,
  and conditional gates without duplicating full lesson prose.
- [x] **SC6.3 — Remove brittle coupling.** Remove incidental wording,
  completed-plan, 44-hash-row, and fixed form/HTMX/SSE implementation checks.
  Retain semantics, links, secrets, vulnerable-route, runtime, Air/FastAPI/
  OpenAPI, no-internal-HTTP, and no-second-runtime checks.
- [x] **SC6.4 — Remove transitional classifiers.** After one-README structure
  stabilizes, replace seven-file/hybrid logic with competing-controller checks.
- [x] **SC6.5 — Reduce mutations by failure class.** Keep representative
  controlled failures for every durable rule; mutation count is not a target.
- [x] **SC6.6 — Verify SC6.** Unmodified and restored candidates pass; every
  retained semantic/safety/runtime failure is rejected; harmless prose changes
  pass. Run `git diff --check`.

## SC7 — Full local validation and repair

Dependencies: SC1–SC6 complete.

- [x] **SC7.1 — Structure/safety.** Run curriculum validation, controlled
  mutations, links/anchors, YAML parsing, secret/unsafe-fixture/generated-archive
  scans, changed-path review, and `git diff --check`.
- [x] **SC7.2 — Catalog.** Run locked sync, Ruff/format, mypy, ordinary pytest,
  live HTML/API/OpenAPI, M0 deliberate red/reset, and intended M1 red contract.
- [x] **SC7.3 — POS.** Run locked quality/tests, PostgreSQL smoke/migration,
  live HTML/API/OpenAPI, Compose parse, image build, and bounded M10 rehearsal
  when supported by the local environment.
- [x] **SC7.4 — Ecommerce.** Run locked quality/tests, PostgreSQL migration,
  live HTML/API/OpenAPI, provider/webhook/worker harnesses, and intended missing
  learner behavior without restored M6 HTMX.
- [x] **SC7.5 — Booking.** Run locked quality/tests, PostgreSQL connection seam,
  live HTML/API/OpenAPI, and deterministic final-seat red/reset boundary.
- [x] **SC7.6 — Social.** Run locked quality/tests, PostgreSQL query/EXPLAIN,
  deterministic seed, live HTML/API/OpenAPI, and intended N+1 red behavior
  without supplied SSE/HTMX completion.
- [x] **SC7.7 — Traverse sources.** Check root→M0→M1 and all product
  transitions; record first action, expected result, recovery, wrong turns,
  undefined terms, duplicate authority, and next action. Do not claim human proof.
- [x] **SC7.8 — Repair and rerun.** Fix observed defects and rerun the narrow
  check plus its enclosing phase. Leave unchecked until the full matrix is green.

## SC8 — Polish and final placement

Dependencies: SC7.1–SC7.8. No structural expansion is allowed here.

- [x] **SC8.1 — Polish language.** Remove stale names, repeated warnings,
  unnecessary jargon, and dead anchors while preserving action, observation,
  evidence, and recovery.
- [x] **SC8.2 — Check route targets.** One table click reaches each milestone;
  first action has no prerequisite hop and at most one shared setup hop; each
  milestone has one controller; every template has a consumer.
- [x] **SC8.3 — Fresh-context review.** Reviewer can state product, first
  command, expected result, and recovery without maintainer material. Record
  limitations; do not claim named-human status.
- [x] **SC8.4 — Decide PLAN/TODO placement last.** Compare keeping root files
  with `docs/maintainers/`; move only if learner choice and contributor
  discoverability both improve and links/rollback pass.
- [x] **SC8.5 — Close locally.** Re-run SC7, reconcile the removal ledger,
  verify intended paths only, state exact evidence/limits, and avoid appending a
  new giant chronology.

## External evidence — unchanged and unchecked

- [ ] Obtain explicit authority and bounded access for the required M6
  Stripe-like sandbox experiment.
- [ ] Execute exactly one authorized M6 payment sandbox experiment and record
  sanitized provider/local reconciliation and cleanup evidence.
- [ ] Optional M7 email-provider endorsement, only after an individual GO.
- [ ] Optional M10 S3-compatible storage endorsement, only after an individual GO.
- [ ] Optional M10 OAuth authorization-code + PKCE/OIDC endorsement, only after
  an individual GO.
- [ ] Optional M10 Sentry-or-Logfire endorsement, only after an individual GO.
- [ ] Optional M10 SQLAdmin endorsement, only after an individual GO.
- [ ] Optional learner-authorized real deployment / Operable-Sellable
  endorsement, only after its individual GO.
- [ ] Observe root/controller rendering and deterministic Actions in a
  learner-owned hosted GitHub repository.
- [ ] Run the repository→M0, M0→M1, M1→M2, M4→M5, M7→M8, M8→M9, and M9→M10
  cold transitions with named independent career-shifter reviewers.
- [ ] Record reviewer, date, Git reference, environment, wrong turns, help,
  scores, and repairs; repeat transitions below the rubric threshold.
- [ ] Set `HUMAN SELF-STUDY VERIFIED` only after all named-human observations pass.

Local validation, local PostgreSQL/container checks, and maintainer source
review are deliberately not substitutes for any item in this section.
