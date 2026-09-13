# Career-shifter self-study implementation checklist

Status: **REPOSITORY REMEDIATION COMPLETE — LOCAL LEARNER IA AND CLEANUP COMPLETE — EXTERNAL EVIDENCE PENDING**

This is the active completion ledger for [PLAN.md](PLAN.md). Checked items were
implemented and locally verified to the scope stated. The earlier repository
remediation is complete. All locally actionable IA/CU work is verified or resolved by an evidenced KEEP/DEFER
decision. Current unchecked items require a human learner, GitHub-hosted
observation, or learner-authorized real target. Partial substitutes are recorded honestly and do not
count as completion of the stronger original requirement.

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
- [ ] Repair and repeat any transition below 4/5 in any rubric dimension.
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
the optional real-target endorsement. No new locally actionable item remains.
