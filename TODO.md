# Career-shifter self-paced curriculum implementation checklist

Status: **PARETO GAP REPAIR COMPLETE — CS0–CS6 LOCAL WORK COMPLETE — EXTERNAL EVIDENCE PENDING**

This is the active completion ledger for [PLAN.md](PLAN.md). Checked items were
implemented and locally verified to the scope stated. Repository remediation,
IA/CU, and CS0–CS6 remain complete; their checked history is not reopened. The
short PG follow-up below is the only active local phase. Pre-existing unchecked
items still require provider authority, a human learner, GitHub-hosted
observation, or a learner-authorized real target. Partial substitutes are
recorded honestly and do not count as stronger external evidence.

## Audit correction and priority order

- [x] Reconcile the plan and checklist with the post-implementation audit.
- [x] Replace the premature `IMPLEMENTED` status with bounded readiness language.

The earlier P0–P2 remediation is complete. Execute new local work in this order:

1. **P0:** Run IA0 and the no-deletion CU0 inventory; then build the root + M0 IA1 pilot.
2. **P1:** Run IA2 cold validation and record `ROLL OUT`, `REVISE`, or `ROLL BACK`.
3. **P2:** Freeze CU1 cleanup decisions; execute IA3/CU3 only after `ROLL OUT`.
4. **P3:** Handle approved local residue in CU2 and reversible tracked batches in CU4; then add stable IA4 automation.
5. **P4:** Run IA5/CU5 evidence, final manifests, and closeout.

Existing hosted, human, and optional real-target evidence remains independently
open; do not use it to bypass the pilot-first IA sequence.

## Review and baseline

- [x] Complete eight-persona repository review and resolution analysis.
- [x] Record implementation start at `d259148` without resetting the dirty tree.
- [x] Separate structural, starter, and human self-study readiness statuses.
- [x] Mark automated usability scores provisional and remove unsupported claims.
- [x] Add a requirements → challenge → acceptance → command → evidence audit.
- [x] Link analysis and review from maintainer navigation.

## Learner entrance and vocabulary

- [x] Put learner-owned GitHub template creation before cloning.
- [x] Define `origin`; delay optional `upstream`; fix Include-all-branches wording.
- [x] State Linux, macOS, and WSL2 support plus needed-now/needed-later tools.
- [x] Add clone/authentication/remote expected results and recovery.
- [x] Distinguish network port from architecture port.
- [x] Distinguish HTTP safe method from idempotent operation.
- [x] Define branch, commit, PR, remote, transaction, service, repository, worker,
  RPO, RTO, and other cross-milestone terms in plain language.

## Contradiction repairs

- [x] Keep M1's supplied OpenAPI guard and mutate application output, not its test.
- [x] Publish M1 domain errors and distinguish transport 422 responses.
- [x] Align create/retrieve/replace/retire/pagination/compatibility examples.
- [x] Fix M2 A1–A5 wording.
- [x] Standardize ecommerce on `fulfilled` and publish its command/state table.
- [x] Require the M9 Redis experiment while making retention optional.
- [x] Make SSE Core and WebSocket implementation Stretch for the fixed one-way need.
- [x] Fix M8/M9 command-block and reset wording.
- [x] Remove the unearned M10 worker and separate local versus real-target claims.
- [x] Put local archives under ignored `dist/` with checksums.

## Runnable neutral foundations

- [x] Give POS one application-owned engine, metadata registry, query counter,
  strict reset, Dockerfile, and production-rehearsal Compose file.
- [x] Give ecommerce locked FastAPI/PostgreSQL/SQLAlchemy/Alembic/Compose setup,
  engine/session seams, readiness, empty migration, strict reset, and browser-client boundary.
- [x] Give booking the same neutral database shell while preserving the deterministic
  in-memory race and leaving concurrency repair to the learner.
- [x] Give social the same neutral database shell while preserving the N+1 lab.
- [x] Add deterministic social database seed, query/EXPLAIN capture, reset, and load seam.
- [x] Verify all database baselines, integrations, refusal guards, resets, and migrations.
- [x] Verify all five starters from an isolated clean copy.

## Product and failure contracts

- [x] Publish fixed M2 persistence endpoints/errors, seams, legacy data, and query-count path.
- [x] Publish M3 checkout/state/inventory/money/void/refund/race rules.
- [x] Publish M4 stakeholder change, scatter measurement, and executable boundary check.
- [x] Publish M5 identity/session/role/object/order rules and opt-in negative contract tests.
- [x] Keep JWT implementation outside M5 Core while requiring the comparison.
- [x] Publish M6 provider contract, timeout phases, response modes, signed webhook
  fixtures, retry budget, unknown state, and reconciliation invocation.
- [x] Publish M7 job/outbox states, neutral seams, clock/ID/kill controls, stable
  worker invocations, and authorized replay CLI/runbook boundary.
- [x] Publish M8 lifecycle/API/time/race/deadlock/contention/retry contract.
- [x] Publish M9 feed/cursor/workload/cache/SSE failure contract.
- [x] Publish M10 fixed customer, tenant route/policy inventory, audit/retention,
  export/deletion/backup/restore/support, and incident contract.

## Guided lessons and language

- [x] Convert M0/M1 headings and M2–M10 into numbered, required, resumable blocks.
- [x] Give each required M1–M10 block an outcome, supplied/learner work, working
  area, literal command or explicit create-then-run target, expected before/after
  observation, evidence path, executable recovery, pause point, and next action.
- [x] Label every challenge exactly `PROVIDED` or `YOU BUILD`.
- [x] Preserve stable top-level C/A trace IDs; use numbered work blocks for
  smaller steps instead of adding a second bookkeeping hierarchy.
- [x] Give every individual C scenario its own three-level hint ladder and
  executable reset/recovery route.
- [x] Split compound C/A work into locally numbered atomic steps mapped to one
  command, result, and evidence item without adding a second global trace matrix.
- [x] Finish rewriting dense milestone concept prose as
  problem → example → term → rule cards, especially in later milestones.
- [x] Convert M1–M10 review prose into one question per numbered prompt.
- [x] Replace ambiguous domain outcomes with fixed artifacts, behaviors, and proof;
  literal invocation and recovery details remain open above.

## Evidence and GitHub workflow

- [x] Split universal gates from conditional data/security/integration/worker/
  performance/cache/production gates.
- [x] Add evidence bootstrap, explicit N/A guidance, and synthetic evidence examples.
- [x] Align progress fields and add a pause/resume example.
- [x] Add a focused learner-help issue template.
- [x] Separate working PRs from milestone-gate PRs.
- [x] Explain milestone-local CI growth.
- [x] Pin third-party Actions to reviewed commits and document review cadence.

## M10 staging

- [x] Stage tenant-safe sale, append-only audit, and one checkout-impact question.
- [x] Stage immutable image, migration, readiness/rejection, restore, incident,
  handoff, and portfolio work as independently executable blocks with literal checks.
- [x] Build and start the image in two isolated local Compose projects; this proves
  process/container startup only, not API readiness, migration order, or rejection.
- [x] Add a GitHub Actions → GitHub Container Registry image build and an approved
  exact-digest handoff record without pretending an undeclared host exists.
- [x] Gate image publication on the same revision passing curriculum, lint,
  format, type, tests, migrations, and declared security/dependency checks.
- [x] Add an explicit one-shot migration step before API promotion.
- [x] Add an API `/ready` health check and a reproducible unhealthy-candidate rejection test.
- [x] Add literal isolated backup/restore and rollback/roll-forward rehearsal commands.
- [x] Keep approval-only digest recording labeled as handoff; implement and claim
  deploy-by-digest only for the optional authorized real-target endorsement.
- [x] Add migration, rejection, restore, and incident runbook scaffolds.
- [x] Document authorization, cost, TLS, secrets, monitoring, backup, and rollback prerequisites.
- [ ] Prove the optional Operable/Sellable endorsement on a learner-authorized real target.

## Semantic automation and local verification

- [x] Validate 11×7 milestone structure and all 58 concept traces.
- [x] Validate relative links and Markdown anchors.
- [x] Validate README/Acceptance maximum IDs and work-block markers.
- [x] Validate one challenge mode per scenario and controlled domain vocabulary.
- [x] Validate database-starter dependencies and required artifacts.
- [x] Reject mutable Action tags, likely secrets, callable vulnerable fixtures,
  and generated archives outside `dist/`.
- [x] Prove new semantic rules with controlled failing mutations.
- [x] Reject required work blocks that omit a literal command or explicit
  create-then-run target, expected observation, recovery, or next action.
- [x] Reject C scenarios without scenario-local hints and reset/recovery.
- [x] Reject M10 publish/rehearsal paths without required CI gating, migration
  ordering, and API readiness semantics.
- [x] Add controlled failing mutations for every new rule above.
- [x] Parse every GitHub YAML file.
- [x] Run lint, format, strict types, and ordinary tests for every starter.
- [x] Run PostgreSQL migrations/integration tests for every database starter.
- [x] Observe intended M1 compatibility, booking race, and social query-budget failures.
- [x] Verify safe reset refusal and recovery; remove created test containers,
  volumes, and local image afterward.
- [x] Run `git diff --check` and scan generated/sensitive artifacts.

## External release evidence — still required

- [ ] Observe GitHub-rendered root/controller navigation, layout and anchor behavior on the hosted candidate; local source traversal is not that observation.

- [ ] Observe the workflows in the learner-owned GitHub repository.
- [ ] Human cold-test repository → M0 and M0 → M1.
- [ ] Human cold-test M1 → M2 and M4 → M5.
- [ ] Human cold-test M7 → M8, M8 → M9, and M9 → M10.
- [ ] Record reviewer, date, Git reference, environment, wrong turns, help,
  recovery, next action, and rubric score for each transition.
- [ ] Repair and repeat any transition below the current nine-dimension threshold
  (at least 85/100 and no dimension below 3); the older 4/5 wording is historical.
- [ ] Set `HUMAN SELF-STUDY VERIFIED` only after those observations pass.

## Release invariants

- [x] No completed learner solution or solution snapshot was added.
- [x] Minimal stack, modular monolith, and explicit exclusions remain intact.
- [x] Plan, TODO, analysis, and usability status distinguish implemented work
  from external evidence.
- [x] Repository remediation R2–R7 is complete and locally verified.
- [x] All remaining unchecked work requires only hosted, human, or explicitly
  authorized real-target evidence.

The final checked statement above records the close of the earlier Pareto
remediation. The newly opened phase below adds local information-architecture
work; it does not reopen or invalidate R1–R7.

## Completed local phase — learner IA and orientation

Execution order is IA0 → IA1 → IA2 → rollout decision → IA3 → IA4 → IA5.
Do not begin M1–M10 rollout before the M0 pilot has passed and a rollout decision
has been recorded. Check an item only after its expected observation and listed
validation succeed.

### IA0 — Baseline and freeze the presentation contract

- [x] **Record the pre-pilot orientation baseline.** Target:
  `README.md`, `PROGRESS.md`, and
  `milestones/{m0-engineering-baseline,m5-secure-multi-user-ecommerce,m10-production-multitenant-saas-capstone}/README.md`.
  Depends on: current uncommitted candidate remaining intact. Observe: time to
  identify current ordinal/label, product, concrete output, gate, repository
  readiness, next block, support destination, and resume action; record wrong
  turns and missing/imprecise signals without editing curriculum content.
  Validate: compare observations against `USABILITY.md` dimensions and the new
  `PLAN.md` current-state gap. Complete when all fields have evidence; rollback:
  discard only the observation draft, not repository work.
- [x] **Inventory the authoritative source for every route-map cell.** Target:
  `CURRICULUM.md`, `milestones/*/ACCEPTANCE.md`, `USABILITY.md`, and
  `PROGRESS.md` (read-only during this task). Depends on: baseline. Observe:
  exactly eleven M0–M10 labels; ordinal equals label number plus one; artifact
  wording traces to existing work and gate wording traces to acceptance/quality
  gates. Validate: `for f in milestones/*/ACCEPTANCE.md; do rg -n '\*\*A[0-9]+' "$f"; done`.
  Complete when no cell needs invented curriculum; rollback: remove disputed
  cell wording from the proposed map.
- [x] **Freeze the milestone-at-a-glance and route-footer grammar.** Target:
  `PLAN.md` decision record, then implementation in milestone READMEs only.
  Depends on: source inventory. Observe: one compact schema for breadcrumb,
  `Milestone n of 11 · Mx`, capability, product, checkpoint, outputs, gate,
  bounded trust/status, resume cue, and previous/home/next; the at-a-glance
  fields remain inside Starting checkpoint and preserve the required
  Why → Starting checkpoint → Terms → Product brief → Ordered work → Failures →
  Evidence → Done → Recovery → Next sequence. Validate: manual review against
  the proposed page grammar and `AGENTS.md`. Complete when maintainers approve
  one schema; rollback: revise the schema before any controller rollout.
- [x] **Freeze canonical execution-route wording and exact-link rules.** Target:
  `PLAN.md` decision record. Depends on: baseline observations. Observe: every
  route verb maps to start/work/run/expected/recover/record/stop/resume/continue,
  every support link has a justified destination heading, one execution path is
  canonical, and alternatives are explicitly optional, fallback, or later.
  Validate: compare root/M0/M5/M10 environment and execution wording, then run
  `rg -n '\]\([^)]*\.md\)' milestones/{m0-engineering-baseline,m5-secure-multi-user-ecommerce,m10-production-multitenant-saas-capstone}/README.md`.
  Complete when exceptions are explicit; rollback: keep current wording until
  a replacement is evidence-backed.

### IA1 — M0 pilot only

- [x] **Add the compact eleven-stop learner route map and ordinal explanation.**
  Target: `README.md`. Depends on: authoritative cell inventory and frozen
  grammar. Observe: eleven rows in M0–M10 order, including `M5` as
  `Milestone 6 of 11`; each row shows capability, product, concrete artifact,
  gate, and bounded repository status while the existing first action remains
  primary. Validate: `rg -n 'Milestone (1|2|3|4|5|6|7|8|9|10|11) of 11|M(10|[0-9])' README.md`
  plus manual source trace. Complete when no row implies learner completion;
  rollback: revert only the route-map block.
- [x] **Decide the signature-evidence preview in the root pilot.** Target:
  `README.md` using only an explicitly synthetic symptom → hypothesis → repair →
  regression-test → operational-evidence chain. Depends on: route map. Observe:
  whether the preview makes the course method concrete without pushing the
  primary start action down, duplicating a lesson, or resembling learner proof.
  Validate in the repository→M0 two-minute orientation check. Complete with an
  evidenced `RETAIN` or `REJECT` decision; rollback: remove only the preview.
- [x] **Pilot one milestone-at-a-glance block.** Target:
  `milestones/m0-engineering-baseline/README.md`. Depends on: root map. Observe:
  `Milestone 1 of 11 · M0`, capability, catalog product, starting checkpoint,
  concrete outputs, A1–A3/Level A gate, bounded repository trust, and resume
  instruction are visible inside the existing Starting checkpoint section,
  after Why and before detailed work. Validate: manual two-minute orientation
  check plus a section-order comparison with `AGENTS.md`. Complete when a cold
  reader states each field correctly and the controller contract is unchanged;
  rollback: restore the prior M0 opening and revise the schema.
- [x] **Add M0 breadcrumb and boundary-aware route footer.** Target:
  `milestones/m0-engineering-baseline/README.md`. Depends on: at-a-glance pilot.
  Observe: `Course home` resolves to `../../README.md`; previous is `Course
  start`; next resolves to M1; there is no M-1. Validate:
  `python3 scripts/check_curriculum.py`. Complete when all three routes resolve;
  rollback: remove the new navigation lines only.
- [x] **Expose bounded scope and resume cues for every M0 required block.**
  Target: `milestones/m0-engineering-baseline/README.md`. Depends on: pilot
  grammar. Observe: each existing block exposes outcome, starting/last-green
  state, working area/files, concrete output/evidence, stop condition, and
  `Resume at ...` without changing commands, C/A IDs, or technical requirements.
  Validate: diff each command block against the pre-pilot version and manually
  trace outputs to A1–A3. Complete when all required blocks are resumable;
  rollback: revert the scope-cue additions, preserving original lesson text.
- [x] **Replace imprecise M0 support links with contextual exact-section links.**
  Target: `milestones/m0-engineering-baseline/README.md` and, only if an existing
  heading cannot serve, the minimum heading-only change in
  `milestones/m0-engineering-baseline/{CONCEPTS,CHALLENGE,TOOLS,ACCEPTANCE,REVIEW,RESOURCES}.md`.
  Depends on: link rules. Observe: every link lands on the contract, scenario,
  hint, gate, review, resource, or recovery section needed at that point.
  Validate: `python3 scripts/check_curriculum.py` and manually follow every M0
  controller link. Complete when whole-file links are intentional; rollback:
  restore the prior links/headings.
- [x] **Align the resume dashboard with the pilot.** Target: `PROGRESS.md`.
  Depends on: M0 block resume cues. Observe: learner status is explicitly
  separate from repository readiness and the dashboard points to an exact M0
  block/command/evidence gap/last-green reference. Validate: pause mid-M0, close
  the controller, and recover the next action from `PROGRESS.md` alone. Complete
  when the stated block and controller cue agree; rollback: restore dashboard
  wording without changing learner records.
- [x] **Pilot a bounded secondary support route.** Target: M0 Recovery/Next
  wording and the existing learner-help issue template link. Depends on: exact
  link rules. Observe: help appears only after the local hint/recovery path and
  asks for the failing command, expected/actual result, last green reference,
  and redacted evidence; it changes no Core content or gate. Validate during the
  bounded-block cold test. Complete when support is optional and actionable;
  rollback: remove only the secondary link.
- [x] **Guard the M0 pilot against curriculum drift.** Target: all IA1 diffs.
  Depends on: all IA1 edits. Observe: no changes to sequence, seven-file count,
  required controller section order, product contract, commands, C/A IDs,
  Core/Stretch, gates, or solution boundary.
  Validate: `git diff -- README.md PROGRESS.md milestones/m0-engineering-baseline`;
  `find milestones/m0-engineering-baseline -maxdepth 1 -type f | wc -l` must
  report `7`; `python3 scripts/check_curriculum.py` passes. Complete when every
  changed line is orientation/navigation; rollback: revert only the offending IA
  hunk.

### IA2 — Validate M0 before any broad rollout

- [x] **Cold-test repository → M0 orientation.** Target: GitHub-rendered
  `README.md` → M0 route using `templates/TRANSITION-REVIEW.md`. Depends on: IA1
  green. Observe: time to next action, ordinal/label recall, artifact/gate/status
  comprehension, wrong turns, and help. Validate: score with `USABILITY.md`.
  Complete at ≥85/100 with no dimension below 3 and no author intervention;
  rollback condition: any new blocker or material regression pauses rollout.
- [x] **Cold-test a bounded M0 work block.** Target: M0 controller and exact
  support sections. Depends on: repository→M0 pass. Observe: reviewer predicts
  scope, follows only needed support links, reaches the expected result/recovery,
  records evidence, and stops at the stated boundary. Validate: actual command
  transcript plus transition worksheet. Complete when no solution is supplied
  and no navigation guess is required; rollback condition: restore prior M0
  wording if the pilot adds friction that cannot be repaired locally.
- [x] **Cold-test pause → resume → M0→M1.** Target: `PROGRESS.md`, M0 footer, and
  M1 destination. Depends on: bounded-block pass. Observe: a reviewer resumes
  the exact block in under two minutes, distinguishes `M0` from milestone 1 of
  11, then reaches M1 without backtracking. Validate: recorded resume action and
  transition scorecard. Complete at rubric threshold; rollback condition: do
  not roll out until resume/navigation failures are repaired and rerun.
- [x] **Record the pilot decision.** Target: `TODO.md` and the relevant dated
  evidence/result section in `USABILITY.md`. Depends on: all three pilot tests.
  Observe: explicit `ROLL OUT`, `REVISE`, or `ROLL BACK`, with reference, reviewer,
  environment, scores, wrong turns, and limitations. Validate: evidence links
  resolve and claims match observations. Complete only with `ROLL OUT` before
  IA3; rollback: mark IA1 pilot changes for targeted reversal and retain the
  failed evidence.

### IA3 — Conditional M1–M10 rollout

- [x] **Roll out the accepted grammar to M1–M2.** Target:
  `milestones/{m1-production-api-foundation,m2-pos-persistence-data-modeling}/README.md`.
  Depends on: recorded `ROLL OUT`. Observe: correct ordinals 2–3 of 11,
  at-a-glance blocks, bounded work scope, exact contextual links, resume cues,
  and previous/home/next routes. Validate: validator, link walk, and controller
  diff audit. Complete when commands/gates/C/A IDs are unchanged; rollback:
  revert this batch only.
- [x] **Validate the M1→M2 early transition batch.** Target: M1 and M2
  controllers plus transition worksheet. Depends on: M1–M2 rollout. Observe:
  no increased time, wrong turns, or ambiguity versus pilot. Validate: rubric
  threshold and `python3 scripts/check_curriculum.py`. Complete before next
  batch; rollback: repair or revert M1–M2 IA hunks.
- [x] **Roll out the accepted grammar to M4–M5.** Target:
  `milestones/{m4-maintainability-testing-refactoring,m5-secure-multi-user-ecommerce}/README.md`.
  Depends on: early batch pass. Observe: product transition is explicit and M5
  reads `Milestone 6 of 11 · M5`. Validate: validator, exact-link walk, and
  artifact-to-acceptance trace. Complete when one-track/Core gates remain
  unchanged; rollback: revert this batch only.
- [x] **Validate the M4→M5 product/security transition batch.** Target: M4 and M5
  transition worksheet. Depends on: M4–M5 rollout. Observe: learner identifies
  new product/checkpoint, concrete security outputs, and unchanged gate. Validate:
  rubric threshold. Complete before next batch; rollback: repair or revert batch.
- [x] **Roll out the accepted grammar to M7–M9.** Target:
  `milestones/{m7-durable-async-background-processing,m8-concurrency-booking,m9-performance-caching-realtime-social}/README.md`.
  Depends on: M4→M5 pass. Observe: ordinals 8–10 of 11, new-product transitions,
  work scope, resume, and exact support routes are explicit. Validate: validator,
  link walk, and diff audit. Complete without flattening required experiments or
  contextual gates; rollback: revert this batch only.
- [x] **Validate M7→M8, M8→M9, and the M9 handoff.** Target: named transition
  worksheets. Depends on: M7–M9 rollout. Observe: booking/social boundaries and
  M9 required-experiment language remain clear. Validate: each transition meets
  rubric threshold. Complete before final batch; rollback: repair or revert only
  the failing controller(s).
- [x] **Roll out the accepted grammar to M3, M6, and M10.** Target:
  `milestones/{m3-transactions-correctness,m6-resilient-external-integrations,m10-production-multitenant-saas-capstone}/README.md`.
  Depends on: high-complexity batch pass. Observe: remaining ordinals, boundary
  footer for M10, and optional endorsement status are accurate. Validate:
  validator, link walk, artifact/gate/status trace, and diff audit. Complete when
  M10 local Core and optional real-target evidence remain distinct; rollback:
  revert this batch only.
- [x] **Run an all-controller consistency audit.** Target:
  `README.md`, `PROGRESS.md`, and `milestones/*/README.md`. Depends on: all
  batches. Observe: one execution-route vocabulary, eleven correct ordinals,
  unique previous/home/next chain, bounded status language, and no duplicate
  canonical lesson content. Validate: `python3 scripts/check_curriculum.py`;
  `git diff --check`; manual M0→M10 link traversal. Complete when all eleven
  controllers pass; rollback: isolate and revert the smallest failing batch.

### IA4 — Automate only stable facts

- [x] **Specify stable machine-checkable IA invariants.** Target: maintenance
  note in `PLAN.md`/`TODO.md` before validator code. Depends on: all-controller
  audit. Observe: proposed checks cover only eleven-row order, ordinal/label
  mapping, required controller routes, and resolvable anchors—not prose quality,
  section counts as mastery, or learner progress. Validate: maintainer review.
  Complete when each check has a clear false-positive boundary; rollback: keep
  the rule manual.
- [x] **Implement stable IA checks and controlled mutations.** Target:
  `scripts/check_curriculum.py` and `scripts/test_validator_mutations.py`.
  Depends on: approved invariant specification. Observe: wrong `M5` ordinal,
  missing route link, and broken exact anchor fail for the intended reason; valid
  content passes. Validate: `python3 scripts/check_curriculum.py` and
  `python3 scripts/test_validator_mutations.py`. Complete when the validator
  retains its human-understanding limitation; rollback: remove noisy rule and
  its mutation together.

### IA5 — Release evidence and closeout

- [x] **Repeat every named transition review after rollout.** Target:
  repository→M0, M0→M1, M1→M2, M4→M5, M7→M8, M8→M9, and M9→M10 evidence.
  Depends on: IA4 green. Observe: next action, exact support route, artifact,
  gate, status, recovery, and resume are correctly understood. Validate: each
  score is ≥85/100 with no dimension below 3. Complete when failures have been
  repaired and rerun; rollback: reopen only the failing batch.
- [x] **Verify all IA guardrails.** Target: entire implementation diff. Depends
  on: transition passes. Observe: M0–M10 and 11 milestones; exactly seven files
  each; README controllers in the required section order; GitHub-only route;
  problem-first loop; no solutions, topic fragmentation, hosted LMS/progress,
  separate technical tracks, withheld Core content behind support, commercial
  urgency/certification, contradictory execution routes, or an unearned web
  layer. Portfolio framing may vary, but M10 implementation and gates must not.
  Validate:
  `python3 scripts/check_curriculum.py`; `git diff --check`; `git diff --stat`;
  `git status --short`; manual solution/status scan. Complete when every
  invariant is evidenced; rollback: revert the smallest violating IA change.
- [x] **Close the IA phase without merging unrelated evidence claims.** Target:
  `PLAN.md`, `TODO.md`, and `USABILITY.md`. Depends on: all required IA items.
  Observe: local IA completion is stated separately from hosted Actions, human
  self-study verification, and optional real-target endorsement. Validate:
  unchecked-item review and evidence-link check. Complete when no required IA
  item remains unchecked; rollback: keep the phase active and state the exact
  remaining limitation.

## Completed local phase — evidence-first cleanup and consolidation

Execution order is CU0 → CU1 → CU2/CU3 → CU4 → CU5. CU0 may run beside IA0,
but no tracked consolidation, move, or deletion is authorized before IA2 records
`ROLL OUT` and CU1 records an explicit disposition. Check an item only after its
observation, validation, and rollback fields are complete.

### CU0 — No-deletion inventory

- [x] **Capture the repository state without changing it.** Target: all tracked,
  modified, untracked, and ignored paths. Depends on: nothing. Run from the
  repository root: `git status --short --branch`; `git ls-files`;
  `git ls-files --others --exclude-standard`; `git status --ignored --short`.
  Observe: separate lists for committed content, active dirty-tree work, and
  ignored residue. Complete when every path has provenance; rollback: discard
  only the inventory notes.
- [x] **Protect active untracked implementation.** Target: current untracked
  `.github/`, root docs, `projects/`, `scripts/`, and `templates/` paths. Depends
  on: state capture. Observe: each path is marked active candidate, generated,
  local-only, or unknown; no path is classified from Git status alone. Validate:
  compare with the completed remediation record and `git diff --no-index` only
  where a source counterpart exists. Complete when unknowns are deferred;
  rollback: restore `DEFER / OBSERVE` for any unsupported classification.
- [x] **Build the backlink and authority inventory.** Target: root Markdown,
  `.github/`, `templates/`, `challenges/`, `projects/`, milestones, and scripts.
  Depends on: protected-path list. Run targeted `rg -n --fixed-strings
  'candidate-path-or-basename' .` plus `git log --all -- candidate-path`.
  Observe: internal references, validator assumptions, unique obligations,
  last change, and possible public-link exposure. Complete when every tracked
  cleanup candidate has an owner or unresolved flag; rollback: none—read-only.
- [x] **Inventory size and regeneration separately from content value.** Target:
  `.ruff_cache/`, `projects/*/{.pytest_cache,.ruff_cache,.mypy_cache,.venv}`,
  `**/__pycache__`, `dist/`, logs, coverage, databases, and image/evidence
  artifacts. Depends on: state capture. Run explicit `du -sh`/`find` commands;
  do not run `git clean`. Observe: resolved paths, sizes, last modification,
  ignore status, provenance, and regeneration/retention command. Complete when
  disk residue cannot be confused with tracked curriculum; rollback: none.
- [x] **Record the baseline learner-tree observation.** Target: GitHub-rendered
  root → M0 plus the visible root file list. Depends on: IA0 baseline. Observe:
  which files or repeated explanations cause wrong turns, not merely which are
  long. Validate with `templates/TRANSITION-REVIEW.md`. Complete when cleanup
  candidates are tied to observed friction; rollback: retain raw observations.

### CU1 — Decide canonical ownership and disposition

- [x] **Create the candidate decision log.** Target: the initial candidate map
  in `PLAN.md`. Depends on: CU0. For every candidate record `KEEP`,
  `CONSOLIDATE`, `ARCHIVE`, `REMOVE / IGNORE`, or `DEFER / OBSERVE`; include
  owner, evidence, destination, references, public-path risk, recovery source,
  and approval state. Complete when no ambiguity defaults to removal; rollback:
  change the item to `DEFER / OBSERVE`.
- [x] **Audit root maintainer-document consolidation.** Target: `PLAN.md`,
  `TODO.md`, `PERSONA-REVIEW.md`, `ANALYSIS.md`, `USABILITY.md`, and the
  maintainer section of `README.md`. Depends on: decision log and IA2 decision.
  Observe: accepted decisions traced into current owners, completed chronology
  separable from active work, and a proposed dated archive map. Validate every
  statement still cited by `AGENTS.md`, PLAN, TODO, or README. Complete with an
  old → new path/section proposal under the default
  `docs/maintainers/archive/2026-09-13-remediation/` destination; rollback:
  `KEEP` unresolved files in place.
- [x] **Decide whether to compact active PLAN/TODO history.** Target: completed
  Phase 0–8/R1–R7 plan material and checked TODO sections. Depends on: root audit.
  Observe: a concise current summary can stand alone while a dated archive keeps
  full provenance. Validate that current decisions, readiness limits, and links
  survive. Complete with an archive-and-summary design; rollback: retain current
  documents unchanged.
- [x] **Audit duplicate authority without over-centralizing.** Target:
  prerequisite, environment, readiness, evidence, workflow, exclusion, and
  recovery wording across root, milestone, and project READMEs. Depends on:
  canonical-authority map. Observe: conflicting/parallel rules versus necessary
  local action context. Complete when each proposed deletion names its canonical
  destination and learner backtracking test; rollback: keep the local wording.
- [x] **Audit template usefulness and overlap.** Target: `templates/*.md`, with
  explicit decisions for `REQUIREMENTS.md`, `INCIDENT-POSTMORTEM.md`, and
  `RUNBOOK-INCIDENT.md`. Depends on: backlink inventory. Observe: real learner
  route, unique obligation, overlap, and whether wiring, consolidation, or
  removal is smallest. Validate against milestone acceptance/review and M10
  runbook requirements. Complete with one disposition per template; rollback:
  `KEEP` any template whose obligation is unclear.
- [x] **Audit GitHub forms and workflow duplication.** Target:
  `.github/ISSUE_TEMPLATE/*`, `.github/pull_request_template.md`,
  `.github/workflows/repository-hygiene.yml`, and `m10-image.yml`. Depends on:
  backlink/behavior inventory. Observe: distinct learner jobs, duplicated CI
  steps, drift risk, permissions, and M10 publication gates. Validate YAML and
  event behavior conceptually. Complete with separate issue/workflow decisions;
  rollback: preserve current files rather than weakening a gate.

### CU2 — Regenerable local residue

- [x] **Audit ignore coverage before housekeeping.** Target: root `.gitignore`
  and project `.gitignore` files. Depends on: size/regeneration inventory.
  Observe: all actual cache/log/database/build patterns are covered without
  hiding source, fixtures, learner evidence, or `.env.example`. Validate with
  `git check-ignore -v` on representative resolved paths. Complete with a narrow
  proposed ignore delta or an evidenced no-change decision; rollback: reject any
  pattern that hides required files.
- [x] **Prepare an explicit cache-removal manifest.** Target only resolved
  `.ruff_cache`, `.pytest_cache`, `.mypy_cache`, and `__pycache__` directories.
  Depends on: ignore audit. Record exact paths and pre-removal sizes; exclude
  `.venv`, `dist`, evidence, logs, databases, and images. Complete when the list
  can be reviewed without globs or unresolved variables; rollback: do nothing.
- [x] **Remove approved cache residue in a separate housekeeping action.** Target:
  only paths approved in the manifest. Depends on: explicit authorization at
  execution time. Observe: paths disappear and normal checks recreate only
  ignored caches. Validate `git status --short` shows no source loss and rerun
  relevant checks. Complete with reclaimed-size and regeneration evidence;
  rollback: rerun the documented tools to regenerate caches.
- [x] **Keep virtual-environment cleanup opt-in.** Target:
  `projects/*/.venv/`. Depends on: explicit disk-recovery requirement and user
  confirmation. First prove every project can run `uv sync --locked`; never
  include `.venv` in routine cleanup. Complete with `DEFER / OBSERVE` unless a
  disk goal is authorized; rollback: recreate the exact project environment from
  its lockfile.
- [x] **Resolve generated-artifact retention.** Target: `dist/`, coverage,
  logs, databases, image archives, and generated evidence. Depends on: provenance
  inventory. Observe: empty/stale output versus release, learner, or recovery
  evidence. Complete when each path has keep-until, checksum/source, and recovery
  rules; rollback: retain uncertain artifacts.

### CU3 — Consolidate active content after the M0 pilot

- [x] **Compact the root maintainer route.** Target: the maintainer section of
  `README.md`. Depends on: IA2 `ROLL OUT` and root audit. Observe: learners see
  one secondary maintainer entry rather than peer links to historical audits;
  maintainers can still reach every active owner. Validate before/after root→M0
  wrong turns and time to next action. Complete only with no regression;
  rollback: restore the previous section.
- [x] **Consolidate approved repeated authority in small batches.** Target:
  exact paths from the CU1 log. Depends on: root route pass. Preserve local
  command/expected/recovery/stop context; replace only conflicting or needless
  restatement with precise links. Validate affected transition and link anchors
  after each batch. Complete when each rule has one owner without added
  backtracking; rollback: revert the smallest batch.
- [x] **Apply the approved PLAN/TODO compaction.** Target: `PLAN.md` and
  `TODO.md`, with a dated archive if approved. Depends on: archive design and
  current IA/cleanup decisions being self-contained. Observe: active work is
  easier to scan and completed evidence remains retrievable. Validate all
  incoming links and status claims. Complete when no live obligation exists only
  in the archive; rollback: restore the archived snapshot.

### CU4 — Archive/remove tracked candidates reversibly

- [x] **Stage historical-document moves as one batch.** Target only approved
  `PERSONA-REVIEW.md`, `ANALYSIS.md`, completed plan/TODO history, or historical
  usability sections. Depends on: CU3 and public-path decision. Use `git mv` to
  `docs/maintainers/archive/2026-09-13-remediation/` unless CU1 records another
  approved destination; create one `README.md` provenance index and label any
  PLAN/TODO snapshots inactive. Observe: no unexplained root disappearance or
  second active tracker. Validate backlinks and Git history. Complete when
  recovery is one batch revert; rollback: reverse the moves and link edits.
- [x] **Resolve unused/overlapping templates as a separate batch.** Target only
  templates approved by CU1. Depends on: unique-obligation trace. Wire an active
  template, merge unique content into the canonical owner, or remove it; never
  remove based only on zero direct links. Validate milestone C/A obligations and
  the seven-file contract. Complete with reason and Git recovery reference;
  rollback: restore the template and prior links.
- [x] **Resolve GitHub issue/workflow cleanup separately.** Target only approved
  `.github` changes. Depends on: CU1 behavior decision. Observe: learner help,
  defect, milestone, PR, hygiene, and M10 publication jobs retain their declared
  behavior. Validate all YAML plus hosted behavior when available. Complete only
  when duplication falls without weakening permissions/gates; rollback: restore
  the previous form/workflow batch.
- [x] **Repair references and anchors for every move/removal.** Target: all
  Markdown, YAML, Python validator expectations, and public navigation affected
  by the batch. Depends on: each CU4 change. Run `rg` for old paths and
  `python3 scripts/check_curriculum.py`. Complete at zero unintended old-path
  references and zero broken anchors; rollback: restore the path or link.
- [x] **Maintain a removal manifest.** Target: cleanup decision log in
  `PLAN.md` or the approved archive index. Depends on: each executed batch.
  Record old path, disposition, reason, unique content destination, Git
  reference/hash, external-link handling, validation, and exact rollback.
  Complete when every disappearance is accountable; rollback: reopen the batch.

### CU5 — Verification and closeout

- [x] **Run the complete local cleanup gate.** Target: final candidate tree.
  Depends on: CU2–CU4. Run `python3 scripts/check_curriculum.py`, `python3
  scripts/test_validator_mutations.py`, `git diff --check`, YAML parsing, secret/
  generated-artifact scans, and affected project checks. Observe: 11×7, 58
  traces, links, failure mutations, and executable behavior remain green.
  Complete when outputs are recorded; rollback: isolate the first failing batch.
- [x] **Cold-test navigation before versus after cleanup.** Target:
  repository→M0 and every transition touched by consolidation. Depends on: local
  gate. Observe: next-action time, wrong turns, backtracking, exact support path,
  and resume accuracy. Validate with `USABILITY.md` and
  `templates/TRANSITION-REVIEW.md`. Complete only with no dimension regression;
  rollback: restore the cleanup batch responsible for the regression.
- [x] **Audit the final tree and deferred list.** Target: tracked/untracked/
  ignored manifests and every CU1 disposition. Depends on: cold test. Observe:
  no active untracked work deleted, no evidence lost, no empty/stale claim, and
  every uncertain candidate retained as `DEFER / OBSERVE`. Complete when the
  manifest reconciles with `git status`; rollback: reopen discrepancies.
- [x] **Close cleanup independently from external evidence.** Target:
  `PLAN.md`, `TODO.md`, `USABILITY.md`, and removal manifest. Depends on: all
  required CU items. Observe: local cleanup, hosted Actions, human self-study,
  and optional real-target statuses remain separate. Complete when no required
  CU item remains unchecked and all limitations are explicit; rollback: keep the
  phase active with the exact remaining item.

IA0/CU0 local evidence: [execution baseline](PLAN.md#2026-09-13-ia0-and-cu0-execution-baseline). GitHub-rendered and human observations remain external; local source walkthrough is the explicitly bounded substitute.


Local closeout evidence: [final transitions and tests](USABILITY.md#ia5-and-cu5-final-transition-review),
[dispositions](PLAN.md#cu1-disposition-and-authority-decisions), and
[removal/provenance manifest](docs/maintainers/archive/2026-09-13-remediation/README.md).
IA/CU navigation checks use the authorized solo isolated-copy maintenance method,
not named human or hosted evidence. CU3/CU4 archive/compaction/template/workflow
candidates resolve KEEP where recorded; no deletion is implied by those checks.
All remaining unchecked items are external: hosted rendering/Actions, named target
humans and their review/repair/retest records, human-readiness designation, or
the optional real-target endorsement. At the IA/CU closeout, no locally
actionable item remained; the new CS phase below now supersedes that historical
statement without reopening any checked item.

## ACTIVE PHASE — CS career-shifter/self-paced revision

Status: **LOCAL CLOSEOUT COMPLETE — EXTERNAL EVIDENCE REMAINS PENDING**

Canonical rationale and frozen decisions: [active CS plan](PLAN.md#active-plan--career-shifterself-paced-instructional-revision).
Execution order is CS0 → CS1 → Stop/Go 1 → CS2 → CS3 → Stop/Go 2 → CS4 →
Stop/Go 3 → CS5 → CS6. The explicit root-table override is the only completed
CS implementation item; every unrelated item remains unchecked. Checking an item
requires its stated observation, commands, completion condition, and rollback
record. Preserve all earlier checked R/IA/CU items and all pre-existing unchecked
hosted/human/real-target evidence.

When a bundle says **YAML parse**, run this from the repository root:

```bash
python3 - <<'PY'
from pathlib import Path
import yaml

for path in sorted(Path(".github").rglob("*.y*ml")):
    yaml.safe_load(path.read_text())
    print(path)
PY
```

### Immediate root-table override — binding note

The user-directed primary six-column course table explicitly overrides the
earlier compact-root/eight-column-only-`CURRICULUM.md` placement and the normal
CS dependency order. Do not add the superseded eight-column table to
`CURRICULUM.md` or create a second root roadmap. Future changes update the root
table in place. CS2.1 below is the single checklist item for this override; no
other CS item is completed by it.

### CS0 — Baseline and decision freeze (planning/local, no learner edits)

- [x] **CS0.1 Capture the implementation baseline.** Depends on: this planning
  phase only. Targets: read-only `README.md`, `CURRICULUM.md`, `STACK.md`,
  `QUALITY-GATES.md`, `PROGRESS.md`, `USABILITY.md`, `milestones/*/*.md`,
  `projects/**`, `scripts/*`, `.github/**/*.yml`, plus `PLAN.md`/`TODO.md` status.
  Expected: cleanly separated prior completion, external pending work, current
  tree state, 11×7 count, concept count, current commands, and no assumed
  provider access. Validate from root: `git status --short --branch`; `python3
  -B scripts/check_curriculum.py`; `python3 -B
  scripts/test_validator_mutations.py`; `git diff --check`. Complete when the
  baseline reference and dirty-path ownership are recorded before learner edits;
  rollback: discard only new baseline notes.

- [x] **CS0.2 Decide the evidence-path convention.** Depends on: CS0.1. Targets:
  `README.md`, `QUALITY-GATES.md`, `PROGRESS.md`,
  `templates/EVIDENCE-INDEX.md`, `milestones/*/{README,CHALLENGE,ACCEPTANCE}.md`,
  and existing project `evidence/` examples. Expected: one explicit convention
  that resolves identically from every stated working directory and a migration
  map that preserves existing evidence. Validate: `rg -n 'evidence/' README.md
  QUALITY-GATES.md PROGRESS.md templates milestones projects`; `python3 -B
  scripts/check_curriculum.py`. Complete when root-versus-project ownership and
  command resolution are unambiguous; rollback: retain current paths and mark
  the decision unresolved rather than moving evidence.

- [x] **CS0.3 Decide the M4 Core change and variant policy.** Depends on: CS0.1.
  Targets: M4 seven-file set and `projects/pos/specs/M4-CHANGE-BRIEF.md`.
  Expected: one Core stakeholder request used everywhere; proposed default is
  cashier name, with returns/promotions and any second variant removed from Core
  or explicitly bounded as Stretch. Validate: `rg -n
  'cashier|return|promotion|variant' milestones/m4-maintainability-testing-refactoring
  projects/pos/specs/M4-CHANGE-BRIEF.md`; `python3 -B
  scripts/check_curriculum.py`. Complete when a Given/When/Then contract and
  variant disposition are recorded; rollback: no M4 learner edit until decided.

- [x] **CS0.4 Decide the M6 provider reference and interface vocabulary.**
  Depends on: CS0.1. Targets: M6 seven-file set,
  `projects/ecommerce/specs/M6-INTEGRATION-CONTRACT.md`, provider fake/tests, and
  proposed Stripe-like sandbox evidence. Expected: one named reference flow and
  consistent `authorize`/`capture`/`refund`/`lookup` or documented immediate-
  payment vocabulary, with the current fake `charge` conflict mapped. Validate:
  `rg -n 'authorize|capture|charge|refund|lookup|real call|sandbox'
  milestones/m6-resilient-external-integrations projects/ecommerce`; `python3
  -B scripts/check_curriculum.py`. Complete when fake, learner port, webhook,
  refund, lookup, and sandbox terms can align; rollback: retain deterministic
  fake and prohibit implementation expansion.

- [x] **CS0.5 Decide the M9 SSE classification.** Depends on: CS0.1. Targets: M9
  seven-file set, `projects/social/specs/M9-FEED-CONTRACT.md`, `STACK.md`, and
  relevant social tests. Expected: one decision: polling Core followed by an
  earned SSE experiment, or SSE Core justified by a fixed measurable one-way
  latency need; WebSockets remain Stretch. Validate: `rg -n
  'poll|SSE|server-sent|WebSocket|latency' STACK.md
  milestones/m9-performance-caching-realtime-social projects/social`; `python3
  -B scripts/check_curriculum.py`. Complete when contract, gate, and tool policy
  agree; rollback: no M9 rollout while classification conflicts.

- [x] **CS0.6 Freeze the remaining causal grammar and integration
  taxonomy.** Depends on: CS0.2–CS0.5. Targets: the active section of `PLAN.md`
  and implementation map in `TODO.md`; learner files remain read-only. Expected:
  preserve the already implemented exact root six-column M0–M10/five-product
  table without duplicating it in `CURRICULUM.md`; freeze the visible
  Do/Understand/Check/If it fails/Stop-resume cues, deterministic offline Core
  everywhere, exactly one required M6 sandbox experiment, and only listed M7/M10
  optional endorsements. Validate: manual row/column count; `python3 -B
  scripts/check_curriculum.py`; `git diff --check -- PLAN.md TODO.md`. Complete
  when all four decisions have owners and no contradiction is deferred into
  broad rollout; rollback: revise planning only.

- [x] **CS0.7 Re-verify primary tool and provider documentation.** Depends on:
  CS0.6. Targets: the official-reference list in `PLAN.md`, affected
  `milestones/*/RESOURCES.md`, and `STACK.md`; learner implementation remains
  unchanged. Expected: current primary documentation confirms the planned
  FastAPI/Starlette background and security semantics, native SSE availability,
  FastCRUD session/commit behavior, database pagination behavior, Stripe
  sandbox/key/retry/idempotency/webhook/refund behavior, S3-compatible limits,
  OAuth authorization-code + PKCE/OIDC guidance, and the selected observability/
  admin integration. Record retrieval date and any version constraint; do not
  rely on tutorials where an official source exists. Validate: manually open
  every planned reference and compare it with the locked project versions.
  Complete when stale assumptions become explicit decisions or are removed;
  rollback: defer the affected tool/provider and keep the simpler local Core.

### CS1 — Narrow contradiction repair (local implementation)

- [x] **CS1.1 Apply the evidence-path decision without losing evidence.**
  Depends on: CS0.2 and CS0.6. Targets: exact files in CS0.2 plus only affected
  existing example paths. Expected: every command states repository/project
  working directory and resolves to the same learner-owned evidence index; no
  file is overwritten on resume. Validate: `rg -n 'evidence/' README.md
  QUALITY-GATES.md PROGRESS.md templates milestones projects`; `python3 -B
  scripts/check_curriculum.py`; `git diff --check`. Complete when link/command
  traversal passes and existing artifacts remain; rollback: revert path/link
  migration as one batch and restore moved artifacts from the recorded manifest.

- [x] **CS1.2 Make M2 boundaries earned, not ceremonial.** Depends on: CS0.6.
  Targets: `CURRICULUM.md`, `STACK.md`, M2 seven-file set, and
  `projects/pos/specs/M2-PERSISTENCE-CONTRACT.md`. Expected: explicit route-to-
  SQLAlchemy permission for a simple case; service/repository introduced only
  for observed orchestration, invariant, duplication, or substitution; use-case
  owns commit/rollback. Validate: `rg -n 'service|repository|commit|transaction'
  CURRICULUM.md STACK.md milestones/m2-pos-persistence-data-modeling
  projects/pos/specs/M2-PERSISTENCE-CONTRACT.md`; from `projects/pos`, `uv run
  --locked ruff check .`, `uv run --locked ruff format --check .`, `uv run
  --locked mypy .`, `uv run --locked pytest`; then root validator/diff check.
  Complete when no criterion mandates empty layers; rollback: revert M2 batch.

- [x] **CS1.3 Draw the M3 local/remote transaction boundary.** Depends on:
  CS0.4. Targets: M3 seven-file set,
  `projects/pos/specs/M3-CHECKOUT-CONTRACT.md`, and M6 handoff wording. Expected:
  database rollback covers local state/intent only and explicitly cannot undo
  provider money; remote effects route to M6 idempotency, unknown outcome,
  lookup, and reconciliation. Validate: `rg -n 'rollback|payment|provider|money|reconcil'
  milestones/m3-transactions-correctness milestones/m6-resilient-external-integrations
  projects/pos/specs/M3-CHECKOUT-CONTRACT.md`; POS lint/format/type/tests and
  isolated PostgreSQL migration/integration checks; root validator/diff check.
  Complete when no atomicity claim crosses the provider boundary; rollback:
  revert M3/M6 handoff hunks together.

- [x] **CS1.4 Align M4 to the chosen single Core change.** Depends on: CS0.3.
  Targets: M4 seven-file set, `projects/pos/specs/M4-CHANGE-BRIEF.md`, and exact
  portfolio references. Expected: spec, prose, challenge, acceptance, and review
  all use the chosen Core change; any variant is explicitly Stretch and fully
  supported or removed. Validate: CS0.3 search; POS lint/format/type/tests; root
  validator/diff check. Complete when there is one unambiguous Core and no
  unsupported second variant; rollback: revert the M4 batch.

- [x] **CS1.5 Restore cookie Core / JWT Stretch consistency in M5.** Depends on:
  CS0.6. Targets: M5 seven-file set,
  `projects/ecommerce/specs/M5-SECURITY-CONTRACT.md`,
  `projects/ecommerce/REQUIREMENTS.md`, relevant contracts, and `STACK.md`.
  Expected: secure first-party cookie session is Core; FastAPI Security follows
  auth/authz concepts; PyJWT lab/comparison is conditional Stretch unless a
  different client boundary is earned. Validate: `rg -n 'PyJWT|JWT|cookie|Core|Stretch|Security'
  STACK.md milestones/m5-secure-multi-user-ecommerce projects/ecommerce`; from
  `projects/ecommerce`, lint/format/type/tests plus isolated PostgreSQL checks;
  root validator/diff check. Complete when no Core gate implies PyJWT;
  rollback: revert M5 batch without weakening existing security tests.

- [x] **CS1.6 Repair M6 scope/vocabulary before adding behavior.** Depends on:
  CS0.4. Targets: M6 seven-file set and M6 project contract/fake/test targets.
  Expected: deterministic local calls remain allowed and required; real calls
  become one separately authorized sandbox experiment; interface, webhook raw-
  body verification, timeout phases, refund, unknown, lookup, and reconciliation
  requirements are coherent but learner implementation is not supplied. Validate:
  CS0.4 search; ecommerce lint/format/type/tests; root validator/diff check.
  Complete when no file both prohibits and requires the sandbox and no acceptance
  relies on the old fake-only charge vocabulary; rollback: revert M6 contract
  wording as one batch.

- [x] **CS1.7 Remove exactly-once email implications in M7.** Depends on: CS0.6.
  Targets: M7 seven-file set, `projects/ecommerce/specs/M7-JOB-CONTRACT.md`, and
  worker/outbox seams/tests referenced by the lesson. Expected: at-least-once
  delivery, durable business idempotency, bounded duplicates, and provider
  acceptance-versus-mailbox-delivery language; provider lab remains optional.
  Validate: `rg -n 'exactly.once|at.least.once|email|accepted|deliver|duplicate'
  milestones/m7-durable-async-background-processing projects/ecommerce`; ecommerce
  lint/format/type/tests and PostgreSQL checks; root validator/diff check.
  Complete when no external-email exactly-once claim remains; rollback: revert
  M7 batch.

- [x] **CS1.8 Align M9 with the settled SSE decision.** Depends on: CS0.5.
  Targets: M9 seven-file set, `projects/social/specs/M9-FEED-CONTRACT.md`,
  `STACK.md`, and relevant harness/tests. Expected: one Core/experiment status,
  a measurable need, tested reconnect/gap/slow-consumer/loss semantics if SSE is
  retained, and WebSockets only for earned bidirectional Stretch. Validate:
  CS0.5 search; from `projects/social`, lint/format/type/tests and isolated
  PostgreSQL checks; root validator/diff check. Complete when policy, contract,
  challenge, and acceptance agree; rollback: revert M9 batch.

- [x] **CS1.9 Replace mechanical red signals and repair first-use/rubric drift.**
  Depends on: CS1.1–CS1.8. Targets: changed
  `milestones/*/{README,CONCEPTS,CHALLENGE,ACCEPTANCE}.md`, their project tests/
  contracts, `CURRICULUM.md`, `GLOSSARY.md`, active `PLAN.md`/`TODO.md` claims,
  and `templates/TRANSITION-REVIEW.md`; touch `USABILITY.md` only to clarify its
  current authority. Expected: `pytest -s`/missing-selector mechanics are not
  substantive proof; concepts first appear through concrete examples and trace
  to practice/proof; current reviews use nine dimensions scored 0–4, ≥85/100,
  none below 3, while dated historical scores remain labeled. Validate: `rg -n
  'pytest.*-s|missing|4/5|five dimensions|ten dimensions|0.to.4|85/100' PLAN.md
  TODO.md USABILITY.md templates milestones projects`; all affected project
  checks; root validator/mutations/diff check. Complete when intended red states
  assert behavior and current rubric language has one owner; rollback: revert
  only the failing concept/test/rubric sub-batch.

- [x] **CS1.GATE STOP/GO 1 — approve expansion after contradiction repair.**
  Depends on: CS1.1–CS1.9. Targets: the complete CS1 diff and decision record in
  `PLAN.md`/`TODO.md`. Expected: every listed contradiction is closed, four
  decisions are visible, no solution or provider secret exists, and external
  items remain unchecked. Validate: `python3 -B scripts/check_curriculum.py`;
  `python3 -B scripts/test_validator_mutations.py`; `git diff --check`; parse
  all `.github/**/*.yml` with `yaml.safe_load`; affected project uv lint/format/
  type/tests; isolated PostgreSQL checks where applicable. Complete only with a
  recorded `GO`; rollback: `STOP`, identify the smallest failing CS1 batch, and
  revert/repair it before CS2.

### CS2 — Root roadmap and earned-tool visibility (local implementation)

- [x] **CS2.1 Install the user-overridden primary 11×6 table in `README.md`.**
  Depends on: explicit user override, which supersedes CS1.GATE for this item
  only. Targets: `README.md`, planning records, and table validators;
  `CURRICULUM.md` remains the linked detail source and is unchanged. Expected:
  exactly eleven ordered M0–M10 rows and the six exact headers recorded above;
  five-product journey, concise concepts, earned tools, controller links, and
  truthful integration classifications scan in one place. Validated by the
  complete root/mutation/YAML/diff/manual gate named in the override item.
  Complete with no duplicate detailed table; rollback: restore only the prior
  root table and matching stable validator/planning rules.

- [x] **CS2.2 Publish one coherent tool ladder.** Depends on: CS2.1. Targets:
  `STACK.md`, `CURRICULUM.md`, and `milestones/*/TOOLS.md`, with exact contextual
  links from controllers. Expected: timing/caveats for FastAPI/Uvicorn/Pydantic/
  settings, `APIRouter`/`Depends`/OpenAPI, handwritten pagination before
  `fastapi-pagination`, explicit CRUD before FastCRUD including async/commit
  caveats, concepts before FastAPI Security, disposable `BackgroundTasks`
  contrast before outbox/worker, earned Redis/SSE/WebSockets, post-auth/audit
  SQLAdmin, and one of Sentry/Logfire for one question. Validate: targeted `rg`
  for every tool; root validator/mutations/diff check. Complete when every tool
  has observed need, simpler baseline, cost, and removal trigger; rollback:
  revert tool-visibility batch without reverting concepts.

- [x] **CS2.3 Publish the integration taxonomy and ladders.** Depends on: CS2.2.
  Targets: `CURRICULUM.md`, `STACK.md`, `QUALITY-GATES.md`, M6/M7/M10 seven-file
  sets, and their existing project contract specs. Expected: offline Core in all
  milestones; exactly one required M6 sandbox; optional M7 email and M10 storage,
  OAuth/OIDC, monitoring, SQLAdmin, deployment; outage/pending semantics and no
  four-account prerequisite; payment/email/storage/OAuth/monitoring ladders are
  complete. Validate: `rg -n 'REQUIRED|OPTIONAL|sandbox|S3|OAuth|OIDC|Sentry|Logfire|SQLAdmin|email'
  CURRICULUM.md STACK.md QUALITY-GATES.md milestones projects/*/specs`; root
  validator/mutations/diff check. Complete when classifications agree and CI has
  no credential requirement; rollback: revert taxonomy batch.

### CS3 — Two-block compression pilot (local implementation)

- [x] **CS3.1 Pilot one representative M0 block.** Depends on: CS2.3. Targets:
  exactly one named block in `milestones/m0-engineering-baseline/README.md` and
  unavoidable exact-link headings in that milestone's six support files.
  Expected: plain problem name before IDs and visible Do/Understand/Check/If it
  fails/Stop-resume, with every original command, failure, proof, hint, evidence,
  recovery, and gate retained. Validate: pre/post semantic diff; `python3 -B
  scripts/check_curriculum.py`; `git diff --check`; catalog uv lint/format/type/
  tests. Complete when a fresh-context maintenance reviewer selects, executes,
  diagnoses, records, and resumes the block without new backtracking; rollback:
  revert only the M0 pilot hunks.

- [x] **CS3.2 Pilot one difficult M6 payment block.** Depends on: CS3.1. Targets:
  exactly one named M6 block and unavoidable headings in the M6 seven-file set;
  deterministic fake/project contract references only. Expected: the same five
  cues expose fake → protocol/SDK → separately authorized sandbox, timeout/retry/
  webhook/refund/unknown/reconciliation proof, and the DB/provider boundary
  without supplying a learner solution. Validate: pre/post semantic diff; root
  validator/diff check; ecommerce uv lint/format/type/tests (fake only).
  Complete when fresh-context review can predict and diagnose the hard failure
  and identify the external authority boundary; rollback: revert M6 pilot hunks.

- [x] **CS3.GATE STOP/GO 2 — accept, revise, or roll back compression.** Depends
  on: CS3.1–CS3.2. Targets: both pilot blocks and a dated maintenance review in
  `USABILITY.md`. Expected: current nine-dimension 0–4 observations for both
  blocks, ≥85/100 and no dimension below 3, no lost substance, and explicit
  `ROLL OUT`, `REVISE`, or `ROLL BACK`. Validate: root validator/mutations/diff
  check plus catalog/ecommerce checks; manually trace C/A/evidence/recovery.
  Complete only on recorded `ROLL OUT`; rollback: revert both pilot batches if
  revision cannot meet the threshold without added complexity.

### CS4 — M6 deterministic contract and required sandbox evidence

#### CS4 local, deterministic implementation

- [x] **CS4.1 Extend the M6 fake and contract without implementing the learner's
  application.** Depends on: CS3.GATE = ROLL OUT. Targets:
  `projects/ecommerce/specs/M6-INTEGRATION-CONTRACT.md`,
  `src/ecommerce_api/provider_fake.py`, `tests/test_failure_harnesses.py`, and M6
  seven-file references; settings/env/dependencies only if required by the fixed
  contract. Expected: success/decline; connect, read, total, before-processing,
  after-processing timeouts; one combined SDK/application retry budget; raw-body
  signed webhook; durable event/business idempotency; duplicates/out-of-order;
  refund success/failure/unknown; lookup/reconciliation; DB rollback boundary.
  Validate from ecommerce: uv lint/format/type/tests; relevant isolated
  PostgreSQL checks; from root: validator/mutations/diff check. Complete when all
  failure modes are deterministic, CI is secret-free, and only neutral seams/red
  tests are supplied; rollback: revert fake/contract/test batch together.

- [x] **CS4.2 Add the learner-facing M6 local ladder and sanitized evidence
  contract.** Depends on: CS4.1. Targets: M6 seven-file set,
  `QUALITY-GATES.md`, and existing evidence/data-lifecycle templates. Expected:
  keys/secrets, SDK-vs-HTTP, timeout/retry ownership, raw body, refund uncertainty,
  lookup/reconciliation, safe evidence fields, cleanup, and outage/pending rules
  are executable without embedding credentials. Validate: secret-pattern scan;
  root validator/mutations/diff check; ecommerce fake tests. Complete when local
  Core can finish offline and the sandbox step cannot be mistaken for simulated
  evidence; rollback: revert M6 instructional sub-batch.

#### CS4 external, credentialed provider evidence — authority required

- [ ] **CS4.EXT1 Obtain explicit authority and bounded Stripe-like sandbox
  access.** Depends on: CS4.1–CS4.2 local green. Targets: external test account,
  task-scoped test credential, approved operation/refund limits, and learner-owned
  sanitized evidence destination; no repository secret file. Authority/access:
  repository owner approval to make real sandbox calls, valid sandbox account,
  credential custody, and any cost/rate-limit approval. Expected: named provider,
  test/live separation, allowed actions, cleanup/revocation plan, and stop limits.
  Validate: manual authorization record and secret-safe environment check; do not
  run this in CI. Complete only when authority/access are explicit; rollback:
  revoke/delete task-scoped credentials and make no call.

- [ ] **CS4.EXT2 Execute exactly one required payment sandbox experiment.**
  Depends on: CS4.EXT1. Targets: external sandbox plus sanitized project-local
  M6 evidence only. Authority/access: the explicit approval and credential from
  CS4.EXT1. Expected: bounded payment flow, lookup, exact raw-body signature
  verification, one refund, reconciliation, and cleanup; evidence includes only
  sanitized IDs/timestamps/statuses/settings/results. Validate: provider dashboard/
  API lookup, local reconciliation command, secret/personal-data scan, and manual
  evidence review; never expose key, instrument, customer data, or full payload.
  Complete when provider/local facts reconcile and cleanup is observed; provider
  outage/access failure remains unchecked as `PENDING` and does not count as real
  evidence. Rollback: external money cannot be rolled back by the DB—use the
  provider refund/void/cleanup path, reconcile forward, revoke credentials, and
  preserve the sanitized incident record.

### CS5 — Bounded rollout and optional endorsements

#### CS5 local rollout

- [x] **CS5.1 Roll the accepted grammar through remaining blocks in bounded
  batches.** Depends on: CS3.GATE = ROLL OUT and CS4.1 local green; CS4.EXT2 may
  remain pending only where work is independent. Targets: remaining
  `milestones/*/*.md`, grouped M1–M2, M3–M5, M7–M9, then M10; exact support
  targets only. Expected: causal grammar and five cues, plain names before IDs,
  shorter support/process text, unique templates preserved, concept matrix
  secondary, and no technical/gate/solution drift. Validate after each batch:
  root validator/mutations/diff check plus affected project uv checks and
  PostgreSQL checks. Complete when every batch has a fresh-context pass and M0–
  M10/11×7/five products remain exact; rollback: revert smallest failing batch.

- [x] **CS5.GATE STOP/GO 3 — decide whether any optional integration is earned.**
  Depends on: CS5.1. Targets: a decision record in `PLAN.md`/`TODO.md` and the
  relevant complexity-rejection/ADR/data-lifecycle template; no provider call.
  Expected: for each proposed M7/M10 endorsement, record observed need, simpler
  alternative, owner, data/secret boundary, operations/cost cap, removal trigger,
  access, and explicit authority status; default is `DO NOT ADD YET`. Validate:
  manual decision review; root validator/diff check. Complete with a separate GO/
  NO-GO per endorsement; rollback: retain deterministic Core and reject/defer it.

#### CS5 external optional endorsements — each remains non-blocking

- [ ] **CS5.EXT1 Optional M7 email-provider endorsement.** Depends on: individual
  CS5.GATE GO. Targets: one approved email test provider and sanitized M7 evidence.
  Authority/access: explicit approval, test account/recipient, credentials, data/
  cost limit. Expected: acceptance-versus-delivery distinction, provider ID,
  bounded retry/deduplication observation, and cleanup. Validate manually plus
  secret/privacy scan. Complete only as an optional endorsement; rollback: stop
  sends, suppress/revoke access, reconcile duplicates, retain sanitized facts.

- [ ] **CS5.EXT2 Optional M10 S3-compatible storage endorsement.** Depends on:
  individual CS5.GATE GO. Targets: one authorized test bucket and sanitized M10
  evidence. Authority/access: explicit bucket/credential/cost/retention approval.
  Expected: tenant-safe key, auth, short presigned expiry, checksum, delete, and
  orphan cleanup proof. Validate provider lookup plus local checksum and secret/
  privacy scan. Complete only as optional evidence; rollback: delete authorized
  test objects, reconcile orphans, revoke credentials.

- [ ] **CS5.EXT3 Optional M10 OAuth authorization-code + PKCE/OIDC endorsement.**
  Depends on: individual CS5.GATE GO. Targets: one authorized identity-provider
  test client and sanitized M10 evidence. Authority/access: client registration,
  redirect approval, test identities, credentials. Expected: code+PKCE/OIDC,
  state/nonce and token validation, account link/unlink, error/logout assumptions;
  never password grant. Validate provider/client logs and security evidence
  without tokens/personal data. Complete only as optional evidence; rollback:
  unlink test accounts, revoke client secrets/tokens, remove callback access.

- [ ] **CS5.EXT4 Optional M10 Sentry-or-Logfire endorsement.** Depends on:
  individual CS5.GATE GO. Targets: exactly one authorized backend and sanitized
  M10 evidence. Authority/access: explicit project/DSN, data processing,
  retention, access and cost approval. Expected: one synthetic failure answers
  one named diagnostic question under redaction/sampling/retention limits.
  Validate event correlation and secret/personal-data review. Complete with a
  retain/remove decision; rollback: delete test event/project where supported,
  revoke DSN, and remove integration if the question/cost boundary fails.

- [ ] **CS5.EXT5 Optional M10 SQLAdmin endorsement.** Depends on: individual
  CS5.GATE GO and proven tenant auth/audit Core. Targets: bounded admin surface
  and sanitized M10 evidence. Authority/access: explicit approval if exposed on
  any real target. Expected: tenant scoping, authorization, and append-only audit
  on every admin action; no public/default admin. Validate negative auth/tenant
  tests and audit trace. Complete only if it preserves the Core boundary;
  rollback: remove/disable the admin surface and retain ordinary operator paths.

- [ ] **CS5.EXT6 Optional authorized real deployment endorsement.** Depends on:
  individual CS5.GATE GO and existing M10 external prerequisite. Targets: one
  declared deployment target and sanitized release/recovery evidence. Authority/
  access: owner approval, target credentials, cost/TLS/secret/backup/monitoring
  ownership. Expected: exact digest, migration-before-readiness, unhealthy
  rejection, rollback/roll-forward, restore, and cleanup. Validate target health,
  digest, migration and recovery observations. Complete only as optional
  Operable/Sellable endorsement; rollback via declared target procedure, never
  an unreviewed destructive command.

### CS6 — Validator migration, full verification, and closeout

- [x] **CS6.1 Migrate remaining stable validator facts.** Depends on: stable CS1–CS5
  local contracts. Targets: `scripts/check_curriculum.py` and
  `scripts/test_validator_mutations.py`. Expected: durable checks cover exact
  evidence path, Core/optional tool statuses, and stable pilot grammar markers
  where useful; retain the already implemented root table shape/order/
  classification rules; no prose score or
  learner-understanding proxy. Validate: `python3 -B
  scripts/check_curriculum.py`; `python3 -B
  scripts/test_validator_mutations.py`; `git diff --check`. Complete when each
  new rule has one controlled intended failure and green restoration; rollback:
  remove the noisy rule and matching mutation together.

- [x] **CS6.2 Run the full local release-candidate matrix.** Depends on: CS6.1.
  Targets: complete candidate tree, without provider calls. Expected: 11×7,
  concept traces, relative links/anchors, secret/unsafe fixture scan, deterministic
  CI, YAML, all five starters, relevant migrations/PostgreSQL integration, and
  intended red/reset behavior pass. Validate: root validator and mutation suite;
  `git diff --check`; `yaml.safe_load` over `.github/**/*.yml`; in every affected
  project `uv sync --locked`, Ruff check/format, mypy, pytest; isolated PostgreSQL
  upgrade/current/integration tests for POS/ecommerce/booking/social. Complete
  when exact results and limits are recorded and temporary resources are safely
  cleaned; rollback: isolate/revert first failing phase, never erase user work.

#### CS6 external named-human and hosted evidence

- [ ] **CS6.EXT1 Observe hosted GitHub presentation and deterministic Actions.**
  Depends on: CS6.2 and separate publication/hosted-run authority. Targets:
  learner-owned GitHub candidate, root/controllers, anchors, and declared
  workflows. Authority/access: explicit commit/push/publication approval and
  GitHub access. Expected: rendered tables/routes work and Actions pass without
  provider secrets. Validate hosted URLs/run IDs and sanitized observation.
  Complete only with hosted evidence; rollback: fix forward in an authorized
  change—do not rewrite tags or fabricate a run.

- [ ] **CS6.EXT2 Run named human career-shifter reviews.** Depends on: CS6.2 and
  an available independent reviewer; may proceed without optional endorsements.
  Targets: repository→M0, M0→M1, M1→M2, M4→M5, M5→M6, M6→M7, M7→M8, M8→M9,
  and M9→M10 transitions plus the M0/M6 pilot blocks. Authority/access: informed
  reviewer participation and a learner-owned test repository/environment.
  Expected: reviewer, date, Git ref, environment, next action, wrong turns, help,
  recovery, resume, and nine 0–4 scores. Validate against `USABILITY.md` and
  `templates/TRANSITION-REVIEW.md`; threshold ≥85/100 and none below 3.
  Complete only after each failure is repaired and independently rerun; rollback:
  keep HUMAN SELF-STUDY VERIFIED unset and reopen only failed transition scope.

- [x] **CS6.3 Close the CS phase truthfully.** Depends on: CS6.1–CS6.2; external
  tasks may remain explicitly pending and cannot be claimed. Targets: `PLAN.md`,
  `TODO.md`, and `USABILITY.md`; no learner `PROGRESS.md` status changes.
  Expected: local implementation, required M6 real-provider evidence, optional
  endorsements, hosted evidence, and named-human evidence have separate statuses;
  prior R/IA/CU history and checklist items remain intact. Validate unchecked-
  item review; root validator/mutations/diff check; exact changed-file/status
  audit. Complete when no locally required item is falsely checked and every
  stronger claim cites its own evidence; rollback: keep CS status ACTIVE and
  state the exact remaining local blocker.

Local closeout evidence (2026-09-14): [exact matrix and limitations](PLAN.md#cs6-local-closeout--2026-09-14)
and [bounded maintenance review](USABILITY.md#2026-09-14-cs6-local-closeout-review).
All four CS0 decisions and three gate decisions are recorded in `PLAN.md`.
CS4.EXT1–2, CS5.EXT1–6, and CS6.EXT1–2 remain unchecked; no credential,
provider, message, hosted GitHub, deployment, admin, or named-human action was
performed. The older external release-evidence items above remain unchecked for
the same reason.

## ACTIVE FOLLOW-UP — Pareto gap repair

Execution order is PG1 → PG2 → PG3 → PG4. This is a narrow documentation and
local-review pass; it does not authorize provider, hosted, deployment, or
named-human work.

- [x] **PG1 Correct the stale M9 SSE reference label.** Target:
  `milestones/m9-performance-caching-realtime-social/CHALLENGE.md`. Expected:
  the hint names the FastAPI SSE reference currently linked from `RESOURCES.md`.
  Validate: `rg -n 'MDN SSE|FastAPI.*SSE' milestones/m9-performance-caching-realtime-social`;
  rollback: restore only this wording if the destination changes again.

- [x] **PG2 Freeze the compact cue-rollout decision.** Depends on: PG1. Targets:
  the active decision text in `PLAN.md`, `TODO.md`, and only unavoidable
  controller wording. Expected: M0 and M6 retain explicit five-cue pilot labels;
  other controllers retain the compact legend plus ordered action, concept,
  check, recovery, and resume facts. Do not mechanically relabel every block.
  Validate: inspect all eleven controller READMEs and run the curriculum
  validator; rollback: revise the decision record rather than expand boilerplate.

- [x] **PG3 Clarify the M9 implementation boundary.** Depends on: PG2. Targets:
  CS closeout wording in `PLAN.md`/`TODO.md` and M9 controller wording only if
  needed. Expected: the SSE contract, lesson, and acceptance requirements are
  implemented, while the SSE application and `tests/m9/test_sse.py` are
  explicitly learner-built and absent from the neutral starter. Validate:
  `test ! -e projects/social/tests/m9/test_sse.py`; root validator/diff check;
  rollback: remove only wording that implies a supplied solution.

PG1–PG3 local result (2026-09-14): the M9 hint now names the linked FastAPI
reference; all eleven controllers expose the accepted explicit-pilot or compact
cue form; and M9 states that its SSE runtime and behavioral test remain learner
work. The curriculum validator and `git diff --check` passed, and the neutral
starter still has no `projects/social/tests/m9/test_sse.py`.

- [x] **PG4 Run one independent fresh-context local maintenance review.**
  Depends on: PG1–PG3. Targets: M0 Block 1, M6 Block 1, one ordinary compressed
  M5 or M9 block, the M5→M6 transition, and a dated record in `USABILITY.md`.
  Expected: reviewer/context, action selection, diagnosis, evidence, resume,
  wrong turns, and limitations are recorded; any score is clearly local and
  cannot satisfy named-human evidence. Validate:
  `python3 -B scripts/check_curriculum.py`; `python3 -B
  scripts/test_validator_mutations.py`; `git diff --check`. Complete after any
  observed local wording defect is repaired and rechecked; rollback: retain the
  honest failed review and reopen only its smallest affected scope.

PG4 result (2026-09-14): an independent Codex sub-agent first returned
`REPAIR` because M6 sent a completed-M5 learner to anonymous-starter recovery.
The project README now has a post-M5 M6 preflight, M6 links to it, and M5 Block 1
states its supplied-red/test/recovery sequence directly. The independent rerun
returned `PASS` across M0 Block 1, M6 Block 1, M5 Block 1, and M5→M6; all four
scopes scored above 85/100 with no dimension below 3. Exact evidence and limits:
[PG4 independent fresh-context review](USABILITY.md#2026-09-14-pg4-independent-fresh-context-review).

All PG items are locally complete. External/provider/hosted/deployment and
named-human checklist items above remain unchecked and unchanged.
