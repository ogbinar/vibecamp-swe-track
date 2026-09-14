# Career-shifter self-paced curriculum revision plan

Status: **PARETO GAP REPAIR COMPLETE — CS LOCAL IMPLEMENTATION COMPLETE — EXTERNAL EVIDENCE PENDING**
Date: 2026-09-14

Latest plan: [Pareto post-closeout gap repair](#pareto-post-closeout-gap-repair).
Completed plan: [career-shifter/self-paced instructional revision](#active-plan--career-shifterself-paced-instructional-revision).
Prior evidence: [local closeout](#local-ia-and-cleanup-closeout),
[dispositions](#cu1-disposition-and-authority-decisions),
[remaining external work](TODO.md#external-release-evidence--still-required).

## Objective

Make M0–M10 independently usable by a career shifter with basic Python, some
Git/SQL exposure, and limited professional engineering experience. At every
point, the learner should know what to do, why it matters, where to work, what
should happen, how to recover, how to pause, and how to know they are finished.

Preserve production-quality outcomes without supplying completed learner
solutions.

## Sources and current status

This plan implements:

- [the eight-persona repository review](PERSONA-REVIEW.md);
- [the conflict and resolution analysis](ANALYSIS.md);
- [the learner-experience rubric](USABILITY.md).

Repository remediation R1–R7 is complete and locally verified. Required work
blocks now have literal create/run contracts; each challenge has local steps,
scenario-specific hints, and reset commands; acceptance maps steps to commands,
results, and evidence; the M8 PostgreSQL barrier seam is runnable; dense concept
prose is split into example-first cards; and stable requirements have validator
mutation proof. The M10 local rehearsal now proves migration-before-readiness,
rollback/roll-forward command mechanics, isolated restore, and unhealthy-release
rejection. Human transition reviews, hosted Actions observation, and the optional
real-target endorsement remain external evidence in [TODO.md](TODO.md).

The existing modified/untracked worktree was preserved; this implementation
does not claim that the candidate has run in hosted GitHub Actions or on a real
deployment target.

## Implementation record

Top-level `C#` and `A#` identifiers remain the 58-concept trace contract.
Smaller resumable units use local step labels inside a scenario or acceptance
criterion instead of entering the global concept matrix. This preserves one
simple trace hierarchy while still requiring each step to name its command,
expected result, evidence, recovery, and stopping point. The validator now
checks the stable structure; human review still judges whether the wording works.

Neutral infrastructure exists across the five starters without supplying domain
solutions. M8 supplies a domain-neutral barrier that coordinates two independent
PostgreSQL connections while leaving booking behavior and correctness to the
learner. M10 supplies and locally verifies migration ordering, `/ready` health,
unhealthy-candidate rejection, isolated restore, and bounded cleanup. The
real-target Operable/Sellable endorsement remains optional and requires
authorization and external evidence.

## Post-implementation audit

| Phase | Status | Audit conclusion |
|---|---|---|
| Phase 0 — Honest baseline | Complete | Readiness categories and audit artifacts exist; this plan/TODO update corrects the premature completion label. |
| Phase 1 — Entrance and contradictions | Complete | Repository ownership, environment support, terminology collisions, and known contract contradictions were repaired. |
| Phase 2 — Product transitions | Complete locally | Runnable database shells and the neutral M8 two-connection coordination seam pass local checks. |
| Phase 3 — Product/failure contracts | Complete | Fixed contracts cover M2–M10 without supplying completed domain solutions. |
| Phase 4 — Executable lessons | Complete locally | Literal command maps, local scenario steps, scenario-specific hints/resets, and acceptance execution maps are present and validated. |
| Phase 5 — Language/workflow | Complete locally | Dense concept summaries were converted to short problem/example/term/rule cards; human readability remains Phase 8 evidence. |
| Phase 6 — M10 staging | Core complete locally | CI-gated image workflow and migration/readiness/rejection/restore rehearsal are executable; hosted workflow and real-target endorsement remain external. |
| Phase 7 — Semantic automation | Complete locally | New stable rules have controlled failure proof; the validator explicitly leaves understanding to humans. |
| Phase 8 — Human cold testing | Pending | It requires named human reviewers and hosted/learner-authorized evidence. |

## Non-negotiable decisions

1. Keep exactly M0–M10 and the current capability arc.
2. Keep exactly seven files per milestone.
3. Keep the root README as the only course entrance and each milestone README
   as its lesson controller.
4. Keep the minimal FastAPI/PostgreSQL modular-monolith stack.
5. Supply contracts, neutral infrastructure, extension points, and red/green
   checks—not completed solutions.
6. Use one fixed Core scenario; reserve personalization for Stretch.
7. Label challenge artifacts `PROVIDED` or `YOU BUILD`.
8. Distinguish `required experiment`, `optional retention`, and `do not add yet`.
9. Use first-party browser cookie sessions for M5 Core; keep JWT comparison or
   implementation outside Core unless a different client earns it.
10. Remove an assumed M10 worker unless a concrete POS obligation earns it.
11. Require a local production rehearsal for M10 Core and a real authorized
    target only for the stronger Operable/Sellable endorsement.
12. Use a CI-built immutable image deployed by digest for that real-target path.
13. Report `STRUCTURALLY READY`, `STARTER VERIFIED`, and
    `HUMAN SELF-STUDY VERIFIED` separately.

## Scope boundaries

Included: navigation, repository ownership, milestone work blocks, terminology,
product contracts, non-solution scaffolding, deterministic failures, acceptance
traceability, progressive GitHub workflow, M10 operations, semantic validation,
and human transition testing.

Excluded: completed learner applications, solution snapshots, a second persona
track, weaker Core gates, or new enterprise infrastructure. Kubernetes, Kafka,
microservices, service mesh, CQRS, event sourcing, Elasticsearch, complex DI,
and multiple databases remain excluded.

## Target learner route

```text
README
  → create and clone one learner-owned repository
  → run current project checkpoint
  → open current milestone README
  → complete one numbered work block
  → run its narrow check
  → record evidence and pause or continue
  → complete milestone gate PR and tag
  → open the next milestone
```

The seven milestone files retain distinct roles:

| File | Responsibility |
|---|---|
| `README.md` | Ordered work blocks, checkpoints, recovery, pause, and next action |
| `CONCEPTS.md` | Example-first concept cards linked from the block that needs them |
| `CHALLENGE.md` | Supplied or learner-built scenario cards with hints and reset |
| `TOOLS.md` | Use-now, experiment, retain/remove, and avoid decisions |
| `ACCEPTANCE.md` | Atomic observable checks mapped to commands and evidence |
| `REVIEW.md` | One explain, predict, modify, or debug prompt per bullet |
| `RESOURCES.md` | Just-in-time primary sources keyed to active work |

## Standard work-block contract

Every active block must name:

1. required/optional status;
2. one customer or operator outcome;
3. prerequisite and prior green reference;
4. supplied artifacts;
5. learner-created artifacts;
6. working directory and likely files;
7. exact command;
8. expected observation before and after;
9. evidence destination;
10. escalating hints and recovery;
11. safe stopping point and next block.

Work blocks are outcome-based. Effort ranges may help planning, but time never
controls advancement.

## Implementation sequence

### Phase 0 — Establish an honest baseline

Separate structural, starter, and human-readiness statuses. Mark automated
usability simulations provisional, link the review/analysis from maintainer-only
navigation, record the working-tree baseline, and define a reusable semantic
audit for requirements → challenges → acceptance → commands → evidence.

Exit: no unsupported whole-course self-service claim; `TODO.md` is the only
active implementation tracker; pre-change validation is recorded.

### Phase 1 — Repair entrance and contradictions

- Make learner-owned template creation precede the first clone; define `origin`
  and delay `upstream`.
- Declare Linux, macOS, and WSL2 support plus needed-now/needed-later tools.
- Fix GitHub template wording and setup recovery.
- Reconcile M1 brief, OpenAPI instruction, compatibility mutation, error shapes,
  tests, and acceptance.
- Fix M2 acceptance-ID wording.
- Standardize ecommerce state names.
- Define the M9 Redis experiment as required with retention optional; clarify
  realtime Core versus Stretch.
- Fix M8/M9 command and recovery wording.
- Align M10 CI artifact, archive destination, worker, and target claims.
- Correct glossary collisions for network/architecture port and HTTP
  safe/idempotent.

Exit: all known contradictions in `ANALYSIS.md` are closed and a fresh learner
can identify one repository, supported environment, first command, and next step.

### Phase 2 — Make product transitions feasible

Add neutral, non-solution foundations:

- **M5:** PostgreSQL/SQLAlchemy/Alembic, configuration, readiness, migration,
  reset, extension points, and a declared first-party browser client.
- **M8:** retain the in-memory race demonstration; add a FastAPI/PostgreSQL/
  SQLAlchemy/Alembic/Compose shell, sequential booking boundary, migration,
  reset, and two-connection harness seam.
- **M9:** retain the in-memory N+1 demonstration; add a PostgreSQL feed shell,
  deterministic seed/reset, query capture, reference workload, cursor boundary,
  and load-harness seam.

Exit: every starter reaches a clean documented green baseline, exposes a
deterministic initial problem, and has literal safe setup/stop/reset/recovery.

### Phase 3 — Publish bounded product and failure contracts

- **M1:** six public-contract slices.
- **M2:** endpoint/error examples, metadata seams, legacy-data migration fixture,
  and query-count boundary.
- **M3:** checkout/state/inventory/payment/decimal/void/refund contract and
  competing-sale harness.
- **M4:** fixed stakeholder change, bounded awkward baseline, scatter measure,
  and failing dependency rule.
- **M5:** identity/session/role/object/order contracts and safe negative tests.
- **M6:** provider port, timeout/response fixtures, signed webhook, retry budget,
  unknown state, and reconciliation.
- **M7:** job-state contract, outbox/worker seams, clock/kill hooks, competing
  worker commands, and starter runbook.
- **M8:** booking lifecycle/API/database-race contract.
- **M9:** feed/pagination/workload/cache-experiment/realtime contract.
- **M10:** fixed customer, tenant, support, deployment, recovery, and handoff
  scenario.

Exit: each Core outcome has Given/When/Then examples; every failure is explicitly
supplied or learner-built; acceptance introduces no unbriefed behavior.

### Phase 4 — Convert specifications into executable lessons

Turn every M1–M10 README into 3–6 resumable work blocks. Convert challenge
bullets to scenario cards, split compound work into `C#.#`/`A#.#`, map every
sub-ID to a command/result/evidence path, add per-scenario hints, and make every
Recovery and stopping-point instruction executable.

Exit: a cold reader can identify the next action within two minutes, every Core
check is independently observable, and every block can be paused and resumed.

### Phase 5 — Teach language and workflow progressively

Rewrite dense concepts as problem → example → term → rule cards; expand acronyms
at first use; make Review prompts atomic; split universal and conditional gates;
add milestone-specific evidence bootstrap/N/A guidance; align progress fields;
add a pause example and escalation issue; split working versus gate PRs; and
teach CI evolution at the relevant milestone.

Exit: no decision-driving term is unexplained, no ambiguous verb lacks artifact/
behavior/proof, and early milestones avoid irrelevant production paperwork.

### Phase 6 — Stage M10 honestly

Create independently green blocks for tenant-safe sale, audit, one observability
question, immutable build/migration, unhealthy-release rejection, restore,
incident response, and customer/operator handoff.

Provide:

- a local two-environment production rehearsal for Core;
- GitHub Actions → GitHub Container Registry → deploy-by-digest for the stronger
  real-target endorsement;
- explicit cost, authorization, TLS, secrets, monitoring, backup, and recovery
  prerequisites;
- versioned runbook scaffolds;
- no default worker without a fixed durable requirement.

Exit: local and real-target claims are distinct, executable, and no stronger
than their evidence.

### Phase 7 — Strengthen semantic automation

Add stable checks for README/Acceptance IDs, challenge mode labels, Markdown
anchors, work-block markers, starter dependency/Core-environment agreement,
controlled domain vocabulary, workflow parity, readiness claims, generated
archives, secrets, and callable vulnerable fixtures. Prove each check with a
controlled failure. Pin third-party Actions to reviewed commits.

Exit: validator output states its scope and limits; all new rules have detection
proof and do not pretend to measure human understanding.

### Phase 8 — Repeat cold testing until complete

Human-test repository→M0, M0→M1, M1→M2, M4→M5, M7→M8, M8→M9, and M9→M10.
Record environment, first action, wrong turns, undefined terms, person help,
failed commands, recovery, next action, and rubric score. Repair and rerun every
failed transition.

Historical Phase 8 threshold (superseded): all ten learner-experience dimensions reach at least 4/5; no transition
requires author intervention; human status names reviewer, reference, date, and
scope.

## Audit remediation sequence

Complete this sequence before Phase 8 human testing. The order follows the
Pareto principle: first repair the gaps most likely to make a solo learner stop
or to create a false production claim.

Local repository status: **R1–R7 complete**. Phase 8 and optional real-target
evidence remain open; they cannot be inferred from local automation.

### R1 — Restore truthful status and tracking

- Use `IMPLEMENTATION CANDIDATE` until repository remediation is complete.
- Keep hosted, human, and optional real-target evidence unchecked and separate.
- Do not infer a passing release gate from a successful process start.

Exit: `PLAN.md`, `TODO.md`, `USABILITY.md`, and learner-facing readiness language
make the same bounded claim.

### R2 — Make every required work block directly executable

For M1–M10, audit every required block against the standard work-block contract.
Replace phrases such as “run focused tests” or “run a named test” with a literal
working directory and copyable command. When the learner must create the target
first, name the exact target path and expected initial result (`missing`, `red`,
or `green`). State the expected observation, evidence destination, recovery
command, safe pause, and next block.

Exit: a cold reader can run or intentionally create every named Core check
without inventing filenames, selectors, environment variables, or success
criteria.

### R3 — Make scenarios atomic without adding global bookkeeping

- Keep top-level `C#`/`A#` IDs as the curriculum-wide trace contract.
- Add local `Step 1`, `Step 2`, and similar labels inside compound scenarios and
  acceptance criteria.
- Map each local step to one command, observable result, and evidence item.
- Give each scenario its own three-level hint ladder and executable reset route.

Exit: every Core failure can be attempted, diagnosed, reset, and resumed in
isolation; the concept matrix still references only stable top-level IDs.

### R4 — Strengthen neutral learner seams

Provide a domain-neutral M8 helper or test scaffold that coordinates two
independent PostgreSQL connections at a barrier. It may demonstrate coordination
and cleanup, but must leave booking queries, invariant enforcement, lock choice,
and correctness assertions to the learner. Re-audit M5/M8/M9 extension points
for request/session lifetime, deterministic setup, and literal reset/recovery.

Exit: setup mechanics are runnable while the product solution remains learner
work.

### R5 — Make the M10 Core rehearsal match its claims

- Gate image publication on the same revision passing curriculum, lint, format,
  type, test, migration, and declared security/dependency checks.
- Add an explicit one-shot migration step before API promotion.
- Add an API health check that probes `/ready`; prove an unhealthy candidate is
  rejected rather than merely running.
- Rehearse rollback/roll-forward and restore into isolated local environments
  with literal commands and recorded checks.
- Treat the environment approval that records a digest as a handoff, not a
  deployment. Claim deploy-by-digest only after an authorized target actually
  performs and records it.
- Keep TLS, managed secrets, monitoring, encrypted backup, and real-target cost/
  authorization outside local Core unless a declared target supplies them.

Exit: local Core proves only what its commands observe; the optional endorsement
proves the exact CI digest, migration, readiness, recovery, and target controls.

### R6 — Automate the stable parts of the remediation contract

Extend the validator and controlled mutation suite to reject:

- required blocks without a literal command or explicit create-then-run target;
- scenarios without their own hint ladder and reset route;
- acceptance steps without command/result/evidence mapping;
- an image-publish path not gated by the required checks;
- a production Compose rehearsal without API readiness and migration ordering;
- language that upgrades process-start evidence into health or production proof.

Keep human readability, pedagogical quality, and understanding as manual review
dimensions.

Exit: each new stable rule has a controlled failing mutation and the validator
states what remains outside automation.

### R7 — Finish the career-shifter language pass

Break dense later-milestone “Rules to carry” paragraphs into short
problem → example → term → rule cards. Expand acronyms at first use, define only
terms needed by the active block, and split sentences that introduce multiple
new operational concepts. Preserve technical vocabulary; teach it progressively.

Exit: a manual language audit finds no decision-driving unexplained term and no
paragraph that requires the learner to absorb several unrelated new concepts at
once.

## Dependency order

| Work | Depends on | Reason |
|---|---|---|
| Honest readiness status | Nothing | Later claims require correct labels. |
| Contradiction repair | Analysis decisions | Scaffolding must not encode conflicts. |
| M5/M8/M9 foundations | Fixed stack and product boundary | Starters must support Core. |
| Product/failure contracts | Contradiction repair | Lessons need one source of truth. |
| Executable work blocks | Contracts and starters | Instructions must point to real artifacts. |
| Language/workflow pass | Stable work blocks | Terms should be taught at actual first use. |
| M10 staging | Fixed target and artifact decisions | Operations need one honest model. |
| Semantic automation | Stable authoring contracts | Automate only settled rules. |
| Human cold testing | Clean candidate implementation | Human evidence must test the release candidate. |

## Risks and controls

| Risk | Control |
|---|---|
| Scaffolding supplies solutions | Supply contracts, seams, and red tests; audit solution leakage. |
| Repository becomes harder to navigate | Keep seven files, one front door, and no duplicate canonical explanations. |
| Fixed scenarios reduce creativity | Fixed Core, personalized Stretch. |
| Infrastructure violates minimalism | Reuse Core stack; require evidence before optional tools remain. |
| Human review delays claims | Publish structural/starter status honestly; never fabricate human status. |
| Automated prose rules create noise | Automate stable facts; review language manually. |
| Existing changes are overwritten | Inspect before edits, patch narrowly, and avoid destructive commands. |

## Verification for every phase

1. Run `python3 scripts/check_curriculum.py` before and after changes.
2. Run `git diff --check`.
3. Run affected lint, format, type, test, migration, and challenge commands.
4. Verify intended failures fail correctly and reset to green.
5. Validate relative links, anchors, and GitHub YAML.
6. Scan secrets, environments, caches, dumps, archives, logs, and unsafe fixtures.
7. Trace changed requirements through C/A IDs, commands, evidence, review, and
   concept coverage.
8. Update `TODO.md`, checking only work actually verified.

## Completion definition

Implementation is complete only when the one-repository route is unambiguous;
all milestones have executable/resumable work blocks; Core work is traceable and
observable; starter infrastructure matches its gates; known contradictions and
terminology gaps are closed; M10 claims are honest; readiness statuses remain
separate; clean validation passes; the historical human cold-test target was 4/5 without author
intervention; and `TODO.md` has no unchecked required implementation item.

Until then:

> **Strong curriculum design and verified starter demonstrations, with incomplete
> end-to-end self-study scaffolding.**

## Learner information architecture — implemented locally

This presentation and navigation phase follows the completed Pareto
curriculum remediation. It does not reopen R1–R7, change the capability arc, or
authorize lesson rewrites. “Carnot-inspired” names the orientation qualities
being borrowed here—an immediately visible route, concrete project outcomes,
small bounded units, explicit progress, and credible proof—not a dependency on
another platform or a mandate to copy its visual design.

### Planning input and evidence limits

The source pattern was audited from the live
[Carnot Data Analysis course](https://carnot-coaching-center.com/courses/data-analysis),
including its module overview, representative lesson, mini-project, capstone,
and coaching pages on 2026-09-13. The transferable evidence is the shallow
course → module → lesson/project hierarchy; global and local navigation;
ordinal position; concrete outcomes; expected outputs; predictable page types;
and a primary-start/secondary-support CTA hierarchy. The audit also found
limits that this plan must not reproduce: traversal counts standing in for
mastery, immediately exposed answer keys, no durable learner-evidence state,
weak debugging/recovery support, and inconsistent browser-versus-Colab/local
execution wording. Rendered mobile interactions, authenticated progress, and
form submission were not tested, so this plan makes no claim about them.

### Current-state gap

The current repository has a valid learner entrance, runnable starters,
executable work blocks, a progress transcript, and strong evidence contracts.
The remaining local gap is wayfinding across those parts:

- The root roadmap groups several milestones together, so a learner cannot scan
  all eleven stops, their concrete outputs, gates, and readiness in one place.
- Milestone labels and ordinals can be conflated: `M5` is the label for
  **milestone 6 of 11**, not “the fifth milestone.”
- The sampled M0, M5, and M10 controllers expose the right ingredients with
  different first-screen grammar (`Why this matters` versus `Why`, combined
  checkpoint/deliverable versus checkpoint alone, numbered sections versus a
  `Work blocks` wrapper).
- Controllers link to supporting files, but frequently to a whole document
  rather than the exact section needed at that work block.
- `Next` links exist, but a consistent breadcrumb and previous/home/next route
  does not. Resume guidance lives mainly in `PROGRESS.md` and is not always
  visible where work restarts.
- Deliverables and evidence are present, but some are described as broad
  behaviors rather than a short, concrete “you will leave with” artifact list.
- Readiness truth exists in `USABILITY.md` and `TODO.md`, but learners cannot
  consistently distinguish supplied-starter verification, automated structure,
  their own gate status, and still-pending hosted/human evidence at the point of
  use.
- Required work blocks are executable, yet their visible scope varies; the
  learner must sometimes read prose to discover the bounded outcome, files,
  evidence destination, stop condition, and resume point.

The result is not a missing-content problem. It is an information hierarchy and
orientation problem around already-remediated content.

### Target IA model

Keep the visible learner route shallow:

```text
README (start + eleven-stop route map)
  → current milestone README (controller + at-a-glance orientation)
    → current bounded work block
      → exact supporting section only when needed
    → acceptance gate + evidence
  → PROGRESS resume record
  → previous / course home / next milestone
```

The root `README.md` remains the only course entrance. `CURRICULUM.md` remains
the detailed concept map, `PROGRESS.md` remains the learner-owned transcript,
and each milestone `README.md` remains its controller. The other six milestone
files remain supporting references, not parallel routes or topic pages.

### Compact eleven-stop route map

The learner-facing map should use the following canonical row meanings. Status
means repository support/readiness, not a learner pass; learner completion stays
in `PROGRESS.md`. Until evidence changes, every row must use bounded language
such as `starter locally verified; learner gate not started`, never a completion
claim based on page counts or file presence.

| Ordinal | Label | Capability | Product | Concrete learner artifact | Gate | IA rollout status |
|---:|---|---|---|---|---|---|
| Milestone 1 of 11 | M0 | Reproducible | Catalog | Green baseline transcript, failure diagnosis, CI-backed gate PR, and `m0-engineering-baseline` tag | A1–A3 / Level A | Local grammar accepted |
| Milestone 2 of 11 | M1 | Functional | Catalog | Tested HTTP catalog contract and compatibility-change evidence | A1–A4 / A + selected B | Local grammar accepted |
| Milestone 3 of 11 | M2 | Persistent | POS | Relational schema, migration, query evidence, and persistence tests | A1–A5 / Level B | Local grammar accepted |
| Milestone 4 of 11 | M3 | Correct | POS | Atomic checkout with money, repeat-request, and final-unit race regressions | A1–A4 / Level B | Local grammar accepted |
| Milestone 5 of 11 | M4 | Maintainable | POS | Fixed stakeholder change, enforced boundary, refactor evidence, and portfolio draft | A1–A6 / Level B | Local grammar accepted |
| Milestone 6 of 11 | M5 | Secure | Ecommerce | Session and authorization matrix plus order-state attack regressions | A1–A6 / B + contextual C | Local grammar accepted |
| Milestone 7 of 11 | M6 | Resilient | Ecommerce | Provider boundary, retry/webhook tests, and reconciliation record | A1–A4 / B + contextual C | Local grammar accepted |
| Milestone 8 of 11 | M7 | Durable | Ecommerce | Persisted job/outbox flow with crash, duplicate, quarantine, and replay evidence | A1–A5 / C for async slice | Local grammar accepted |
| Milestone 9 of 11 | M8 | Concurrent | Booking | Final-seat race reproduction, concurrency repair, and contention evidence | A1–A4 / Level B | Local grammar accepted |
| Milestone 10 of 11 | M9 | Performant | Social | Feed query comparison, bounded Redis decision, and one-way update evidence | A1–A4 / B + contextual C | Local grammar accepted |
| Milestone 11 of 11 | M10 | Operable/sellable candidate | Multi-tenant POS SaaS | Isolation proof, release/recovery record, runbooks, and cold-reviewed handoff | A1–A7 / Level C | Local grammar accepted |

### Adopt, adapt, and reject

| Decision | Treatment in this repository |
|---|---|
| Adopt | A compact visible journey; ordinal plus stable label; capability and product progression; concrete outputs; bounded work units; obvious next action; evidence-backed status; persistent resume cue. |
| Adapt | Express the journey in GitHub-rendered Markdown, relative links, issues, PRs, Actions, evidence files, and tags. Keep statuses split into repository readiness and learner progress. Fit orientation around the existing problem-first engineering loop and seven-file milestone contract. |
| Reject | A hosted learning-management system, passive section counts as mastery, a topic-page tree, a separate career-shifter or data-specialist track, completed solutions, urgency/marketing countdowns, certification claims, and progress inferred from page visits. |
| Defer | A custom website, dashboard, search layer, or other web application. Reconsider only after recorded M0 and cross-transition observations show repeated GitHub navigation friction that Markdown changes cannot fix. |

### Proposed content and page grammar

The root `README.md` should keep one primary start action above reference and
maintainer material, then show the compact eleven-stop route map. The map owns
only orientation; detailed concept coverage remains in `CURRICULUM.md` and
learner state remains in `PROGRESS.md`.

After the primary start route is proven, the root may pilot one compact,
explicitly synthetic signature evidence chain—symptom → hypothesis → repair →
regression test → operational evidence—to preview what “software engineering”
means here. Retain it only if the orientation test shows that it clarifies the
course without pushing the next action down or resembling completed learner
work.

Every milestone controller should use this stable visible grammar while
preserving its existing substantive work and the required section order in
`AGENTS.md`:

1. **Breadcrumb metadata:** `Course home / Mx — title`, with the literal ordinal
   nearby: `Milestone n of 11 · Label Mx`. This is navigation metadata, not a
   replacement content section.
2. **Why:** the product or operator problem before terminology.
3. **Starting checkpoint and at-a-glance orientation:** capability, product,
   starting checkpoint, 2–4 concrete outputs, gate, repository trust/status,
   and one resume instruction. Keep these fields compact inside the required
   Starting checkpoint section rather than adding a competing pre-Why section.
   Name one canonical execution route; label every alternative as optional,
   fallback, or later, and do not let environment wording contradict the root.
4. **Terms used here:** only terms needed for the active work.
5. **Product brief and ordered work:** retain both responsibilities in the
   required order; express the existing problem-first loop as 3–6 bounded
   work blocks, without forcing nine decorative sections.
6. **Each work-block scope cue:** `[REQUIRED]` or Stretch, outcome, prerequisite/
   last-green reference, exact working area/files, concrete output, evidence
   destination, stop condition, and `Resume at ...` cue. Commands retain working
   directory, expected observation, and recovery.
7. **Contextual support links:** links from the controller to exact headings in
   `CONCEPTS.md`, `CHALLENGE.md`, `TOOLS.md`, `ACCEPTANCE.md`, `REVIEW.md`, and
   `RESOURCES.md` only at the block that needs them. A whole-file link is allowed
   only when the whole file is genuinely the next action.
8. **Failures and hints; Evidence; Done; Recovery:** retain the existing
   contracts and distinguish automated structure, supplied-starter checks,
   learner-produced evidence, hosted Actions observation, cold review, and any
   optional real-target endorsement.
9. **Secondary support route:** only after the documented hint/recovery path,
   link to the existing structured learner-help issue. Support adds feedback and
   accountability around the same Core gate; it never introduces withheld
   technical content or a second curriculum.
10. **Route footer:** `Previous milestone · Course home · Next milestone`. M0 uses
   `Previous: Course start`; M10 uses `Next: Portfolio review / evidence-led next
   product`, so neither invents an M-1 or M11.

Carnot's multiple capstone choices translate only into portfolio framing here.
A learner may explain the fixed M10 evidence through a relevant prior-industry
or stakeholder lens, but every learner implements the same M10 Core contract and
passes the same gates.

Canonical execution wording should be imperative and consistent:

- `Start from ...`
- `Work in ...`
- `Run ...`
- `Expected ...`
- `If not ...`
- `Record ...`
- `Stop when ...`
- `Resume at ...`
- `Continue to ...`

“Read,” “complete,” or “verify” alone is not an execution route. A link label
should name the destination and purpose, and an exact heading anchor should
land on the needed contract, hint, gate, or recovery section.

### File impact map for later implementation

The 2026-09-13 execution request authorizes local implementation within this map. A later implementation change must
remain within the following map unless a newly observed dependency is added to
`TODO.md` first.

| Scope | Planned impact | Must remain canonical / unchanged in role |
|---|---|---|
| `README.md` | Add the eleven-row learner route map, explain ordinal versus label, expose bounded repository trust signals, keep one first action, and conditionally pilot one compact synthetic signature evidence chain. | Only learner front door; no maintainer dashboard above the route and no completed learner work. |
| `milestones/m0-engineering-baseline/README.md` | Pilot breadcrumb metadata, at-a-glance fields inside the existing Starting checkpoint section, footer navigation, work-block scope cues, exact support anchors, status language, and resume wording. | Learner controller; required Why → Starting checkpoint → Terms → Product brief → Ordered work → Failures → Evidence → Done → Recovery → Next sequence, M0 capability, and gate unchanged. |
| `PROGRESS.md` | Align the dashboard’s resume fields and explain that learner status is separate from repository readiness. | Learner transcript; no hosted tracking or inferred completion. |
| `milestones/m1-*/README.md` through `milestones/m10-*/README.md` | Roll out only the M0-validated controller grammar and navigation. | Existing ordered work, C/A contracts, Core/Stretch split, and substantive requirements. |
| `CURRICULUM.md` | Add or align navigation only if the root map needs one canonical detailed-roadmap destination; avoid duplicating learner state. | M0–M10 sequence, maturity arc, concept matrix, and one-track policy. |
| `USABILITY.md` | Record the M0 orientation pilot method/results and later transition evidence; add a navigation check only if it measures behavior rather than section presence. | Human rubric and honest readiness vocabulary. |
| `scripts/check_curriculum.py` and `scripts/test_validator_mutations.py` | After the pilot stabilizes, validate only durable facts such as ordinal/label mapping, required route links, and exact anchors; add controlled failing mutations. | Never treat section counts, prose shape, or page visits as mastery. |
| `milestones/*/{CONCEPTS,CHALLENGE,TOOLS,ACCEPTANCE,REVIEW,RESOURCES}.md` | Add heading anchors or minimal link-target clarification only when an exact controller link cannot use an existing heading. | Six supporting roles; no topic-page split and no eighth file. |

### Phased Pareto implementation

#### IA0 — Freeze the contract and baseline observations

Record current time-to-orient, route-map omissions, M0/M5/M10 controller
differences, broken-or-imprecise destinations, and resume discovery using a
clean GitHub-rendered path. Freeze the grammar above before broad edits.

Exit: observations are recorded without claiming that document structure proves
learning, and no curriculum content has been rewritten.

#### IA1 — Pilot the smallest complete route on root + M0

Implement the root route map, then apply the controller grammar only to M0 and
the minimum `PROGRESS.md` alignment needed for a real resume loop. Embed the
at-a-glance fields in M0's required Starting checkpoint section; do not place a
new content section before Why. Preserve M0’s existing commands, outcomes, C/A
IDs, and solution boundary.

Exit: a fresh-context reviewer can state within two minutes: where they are
(`Milestone 1 of 11`, `M0`), what concrete artifacts they will produce, the
current repository trust boundary, the next bounded block, where to record
evidence, how to resume, and how to go home/forward.

#### IA2 — Validate and decide before rollout

Cold-test repository→M0, pause mid-block, resume from `PROGRESS.md`, and traverse
M0→M1. Compare observed wrong turns, backtracking, link precision, and time to
next action with the IA0 baseline. Repair M0 and retest before approval.

Exit: the pilot passes the existing usability release threshold for its tested
scope (at least 85/100 and no dimension below 3), introduces no new wrong turn,
and has an explicit `roll out`, `revise`, or `rollback` decision with evidence.

#### IA3 — Roll out M1–M10 in risk-ordered batches

After an explicit rollout decision, apply only the accepted grammar in batches:
M1–M2 (early transition), M4–M5 (product/security transition), M7–M9
(new-product/high-complexity transitions), then M3, M6, and M10. Review each
batch before starting the next; `M5` must always render as `Milestone 6 of 11`.

Exit: all eleven controllers have consistent orientation and route links while
their existing technical content and sequence remain intact.

#### IA4 — Automate stable navigation facts

Only after the rollout grammar stops changing, add semantic checks and controlled
mutations for durable mappings and route targets. Keep qualitative orientation,
artifact usefulness, and resume comprehension as observed human behaviors.

Exit: the validator detects incorrect ordinal/label mappings and broken route
anchors, and explicitly disclaims learner-understanding measurement.

#### IA5 — Re-run transition evidence

Repeat the named transition reviews already required by Phase 8. Report the
scope of each result and keep hosted Actions, human self-study, and optional
real-target claims independent.

Exit: each tested transition meets the rubric threshold without author
intervention; failures are repaired and rerun rather than averaged away.

### Dependencies

| Work | Depends on | Why |
|---|---|---|
| Root route map vocabulary | Existing `CURRICULUM.md`, acceptance ranges, and readiness vocabulary | The overview must not invent a second source of truth. |
| M0 at-a-glance pilot | Frozen grammar and root map | The first controller must agree with the entrance. |
| Resume loop | M0 pilot plus current `PROGRESS.md` contract | Resume evidence must point to an actual bounded block. |
| M0 rollout decision | Fresh-context pilot observations | Visual consistency alone does not justify eleven-file rollout. |
| M1–M10 rollout | Passing M0 pilot and approved grammar | Limits churn and protects completed remediation. |
| Navigation automation | Stable post-pilot grammar | Avoid encoding a design still under test. |
| Human release claims | Hosted and named human observations | Local structure cannot prove human self-study readiness. |

### Risks and guardrails

| Risk | Guardrail |
|---|---|
| Orientation duplicates canonical curriculum content | Keep root rows compact; link to the controller and detailed curriculum rather than restating lessons. |
| Eleven-row map becomes a completion dashboard | Label it repository orientation; source learner status only from `PROGRESS.md`. |
| `M5` is called the fifth milestone | Always pair stable label with explicit ordinal: `Milestone 6 of 11 · M5`. |
| “At a glance” pushes the next action below the fold or disrupts the controller contract | Keep it compact inside Starting checkpoint, preserve Why first, and preserve one obvious first action before reference material. |
| Grammar rewrite disturbs finished technical work | Move or relabel minimally; do not change commands, gates, C/A IDs, challenge behavior, or product contracts without a separately observed defect. |
| Exact links create fragile anchors | Prefer stable authored headings; validate relative links and anchors after each batch. |
| Status badges overclaim readiness | Use text backed by validator output, starter execution, hosted workflow evidence, or named human review; state scope/date/reference where applicable. |
| Root and milestone execution routes diverge | Name one canonical route at the root and repeat it consistently; mark alternatives optional, fallback, or later and remove stale execution claims. |
| Work blocks imply fixed study duration | Bound by outcome, artifact, and stop condition; do not prescribe urgency, streaks, or time-to-complete. |
| Support becomes a hidden second curriculum | Route help only after local recovery and keep the same technical content, Core gates, and evidence contract for supported and solo learners. |
| Orientation becomes a custom product | Stay in GitHub Markdown. A web layer requires repeated observed friction, an explicit decision record, owner/cost/accessibility plan, and rollback path. |
| Extra pages fragment the route | Keep exactly seven files per milestone and route through the README controller; add no topic pages. |

### Verification method

For planning-only work, run:

```bash
python3 scripts/check_curriculum.py
git diff --check -- PLAN.md TODO.md
git diff -- PLAN.md TODO.md
git status --short
```

For the later pilot and rollout, also:

1. Verify the route map has exactly eleven unique rows in M0–M10 order and each
   label maps to ordinal `label number + 1`.
2. Check every breadcrumb/footer and contextual relative link on GitHub-style
   anchors; M0 and M10 must use their boundary navigation wording.
3. Trace each at-a-glance artifact to its existing work block and A criterion;
   trace each trust/status claim to dated evidence with a named scope.
4. Run the existing curriculum validator and controlled mutation suite; then
   add mutations only for grammar that survived the M0 pilot.
5. Perform repository→M0, mid-block pause/resume, and M0→M1 fresh-context
   observations before rollout. Record time to locate the next action, wrong
   turns, backtracking, support-link usefulness, resume accuracy, and rubric
   score. Do not substitute section counts or automated prose checks.
6. During rollout, compare `git diff --name-only` with the approved file impact
   map and inspect every controller diff for changed commands, C/A IDs, gates,
   or accidental solution content.

### Definition of done for this phase

This phase is done only when the M0 pilot passes before broad rollout; the root
shows a compact, accurate eleven-stop route; every controller states both label
and ordinal, concrete outputs, gate, bounded trust/status, next work block, and
resume cue; every work block exposes bounded scope; exact contextual links and
previous/home/next navigation work; wording follows one execution route; and
all observed transitions pass the usability threshold without author help.

The fixed M0–M10 sequence, exactly seven files per milestone, README controller,
required controller section order, GitHub-only delivery, problem-first loop,
Core/Stretch and gate semantics, no-solution boundary, one technical route, and
current product contracts must remain unchanged. Validation must pass, no learner
status may be inferred from reading or section counts, and `TODO.md` must contain
no unchecked required IA item. Hosted Actions, human self-study, and optional
real-target claims remain separate and may still be pending after the local IA
implementation is complete.

## Complementary phase — evidence-first repository cleanup and consolidation

Cleanup supports the learner IA phase; it is not permission to delete anything
that looks long or currently unreferenced. The goal is to reduce duplicate
authority, root-level maintainer clutter, obsolete historical material, and
regenerable local residue while preserving curriculum evidence, public-link
stability, independent project setup, and the exact milestone contract.

### Cleanup principles and disposition test

1. Inventory before changing. Record tracked, modified, untracked, ignored,
   generated, externally linked, and learner-authored material separately.
2. Preserve user work. Untracked files in the current dirty tree are active
   candidate implementation unless provenance proves otherwise.
3. Prefer `KEEP` or `CONSOLIDATE`; use dated `ARCHIVE` before `REMOVE` when a
   file contains unique rationale, review evidence, or decision history.
4. Remove generated residue only from explicit resolved paths. Never use a
   repository-wide `git clean -fdx` or an unresolved recursive target.
5. Do not delete learner evidence, release artifacts, databases, logs, or local
   environments without checking provenance, retention, and recovery.
6. A tracked move uses `git mv`, an old → new path map, repaired references,
   and a rollback path. Publicly linked paths may require a deprecation period.
7. Cleanup must make the next learner action easier to find. A smaller file
   count that increases indirection is a regression.

| Disposition | Use when | Proof required before action |
|---|---|---|
| `KEEP` | The item owns a current contract, supports an active action, preserves required evidence, or enables independent execution. | Name the canonical obligation or live consumer. |
| `CONSOLIDATE` | Two places state the same rule and one can link to the owner without making the route harder. | Map the destination, backlinks, local context that must remain, and wording removed. |
| `ARCHIVE` | Material is historically useful but no longer active or learner-facing. | Trace accepted decisions forward and record archive path, date, provenance, and retrieval route. |
| `REMOVE / IGNORE` | The item is reproducible residue, empty/stale output, or has no unique obligation after consolidation. | Show zero unresolved references/dependencies and a Git recovery source or regeneration command. |
| `DEFER / OBSERVE` | Ownership, external use, or learner value is uncertain. | Name the observation or decision that will resolve uncertainty; absence of evidence never defaults to deletion. |

### Initial candidate map

This table is an audit hypothesis, not an authorized deletion list.

| Candidate | Provisional disposition | Reason and decision needed |
|---|---|---|
| `README.md`, `CURRICULUM.md`, `STACK.md`, `QUALITY-GATES.md`, `GLOSSARY.md`, `CONTRIBUTING.md`, `PROGRESS.md`, `USABILITY.md`, `LICENSE`, and `AGENTS.md` | `KEEP` | Each owns a distinct learner, maintainer, legal, or agent contract. Navigation may demote links but must not erase these roles. |
| All seven files in every `milestones/*/` directory | `KEEP` | The 11×7 contract is non-negotiable. Shorten conflicting duplication only; never merge/delete a role. |
| `projects/*` code, specs, migrations, fixtures, tests, lockfiles, `.python-version`, and project `.gitignore` files | `KEEP` or `DEFER / OBSERVE` | Starters must remain independently reproducible. Repetition across projects is not sufficient reason to centralize it. |
| Completed remediation history in `PLAN.md` and the large checked portion of `TODO.md` | `CONSOLIDATE` then `ARCHIVE` candidate | Keep current decisions and active work concise; preserve a dated snapshot and accepted-decision summary first. |
| `PERSONA-REVIEW.md` and `ANALYSIS.md` | `ARCHIVE` candidate | These are large one-time review inputs whose accepted decisions now live in the plan. Trace all still-live conclusions and public links before moving them. |
| Historical result sections in `USABILITY.md` | `CONSOLIDATE` or `ARCHIVE` candidate | Keep the rubric and current readiness truth active; move only superseded history when citations and comparisons survive. |
| Root `README.md` maintainer section | `CONSOLIDATE` candidate | Keep one compact maintainer route instead of exposing every historical audit as a peer learner destination. |
| Repeated prerequisite, readiness, exclusion, evidence, and workflow prose | `CONSOLIDATE` candidate | Choose one owner per rule, but retain local commands, expected observations, recovery, and stop conditions where links would cause backtracking. |
| `templates/REQUIREMENTS.md` and `templates/INCIDENT-POSTMORTEM.md` | Decision required | They have weak direct learner routing. Wire them into a real action, consolidate unique content with an active template, or remove them after dependency checks. |
| Other templates | `KEEP` pending use audit | Referenced templates support evidence, decisions, lifecycle, recovery, transition review, or semantic checks; reference count alone is insufficient. |
| `.github/ISSUE_TEMPLATE/*` | `KEEP` or `CONSOLIDATE` | Bug, milestone, and help forms have distinct jobs. Test actual issue routing before removing fields or forms. |
| `.github/workflows/repository-hygiene.yml` and `m10-image.yml` | `CONSOLIDATE` candidate | Audit duplicated starter checks and drift risk; reuse is worthwhile only if M10 publication gates remain explicit and equally strong. |
| `.ruff_cache/`, `projects/*/{.pytest_cache,.ruff_cache,.mypy_cache}`, and `**/__pycache__` | `REMOVE / IGNORE` candidate | Regenerable ignored residue. Use an explicit resolved target list; this is workstation housekeeping, not curriculum improvement. |
| `projects/*/.venv/` | `DEFER / OBSERVE` by default | Regenerable from lockfiles but useful for current work. Remove only for an explicit disk goal after proving `uv sync --locked`. |
| `dist/`, coverage, logs, databases, image archives, and generated evidence | Retention decision | Empty/stale residue may go; release/evidence artifacts require provenance, checksum, retention, and recovery review first. |
| Current untracked starters, specs, workflows, templates, and validator tests | `KEEP` pending normal review | They belong to the active remediation candidate. Untracked does not mean generated or disposable. |

### Canonical authority map

| Information | Canonical owner |
|---|---|
| Learner entrance and first action | `README.md` |
| Capability sequence and concept trace | `CURRICULUM.md` |
| Stack adoption/removal rules | `STACK.md` |
| Gate definitions | `QUALITY-GATES.md` |
| Learner state and resume | `PROGRESS.md` |
| Learner-experience rubric and current review evidence | `USABILITY.md` |
| Active revision rationale and decisions | `PLAN.md` |
| Active maintenance work | `TODO.md` |
| Per-milestone learner route | milestone `README.md` |
| Project setup and recovery | each `projects/*/README.md` |

Local repetition remains valid when it supplies the current command, expected
observation, recovery, or stop condition. The target is conflicting or parallel
authority, not every repeated phrase.

### Cleanup sequence and dependencies

#### CU0 — No-deletion inventory

Inventory tracked, modified, untracked, ignored, generated, empty, large, and
apparently unreferenced items. Capture incoming links, validator assumptions,
Git history, public-path risk, last use, unique obligations, regeneration, and
retention. CU0 may run alongside IA0 and changes no repository content.

Exit: every candidate has provenance and a provisional disposition; active
untracked work and learner evidence are protected explicitly.

#### CU1 — Decide authority and reversible destinations

After IA0 freezes presentation grammar, freeze canonical owners, decide whether
historical material stays, is condensed, or moves to a dated maintainer archive,
and record every proposed old → new path. Assess whether public deprecation
stubs are needed. Do not delete while a unique obligation or reference remains.

The default proposed archive is
`docs/maintainers/archive/2026-09-13-remediation/`, with one `README.md` index
recording provenance and retrieval. If approved, historical PLAN/TODO snapshots
must be clearly labeled inactive records, never a second maintenance tracker.

Exit: every proposed change has an owner, reason, destination, link migration,
recovery source, and approval state.

#### CU2 — Clean regenerable local residue separately

Audit `.gitignore` coverage and remove only approved explicit cache paths.
Treat `.venv`, databases, logs, coverage, `dist/`, images, and evidence as
separate retention decisions. Never mix workstation cleanup into a tracked-doc
batch or report reclaimed disk as learner-IA value.

Exit: ignored residue is deliberately retained or safely regenerated; no active
environment or evidence is removed accidentally.

#### CU3 — Consolidate active content after the M0 IA decision

Only after IA2 records `ROLL OUT`, compact duplicate authority and root-level
maintainer navigation. Preserve required milestone order and local action
context. Compare root→M0 orientation before and after and revert any change that
increases wrong turns or backtracking.

Exit: active documents state each decision once, references land at the owner,
and the learner entrance is clearer by observed behavior.

#### CU4 — Archive or remove approved tracked candidates

Move historical evidence with `git mv`, repair references, and retain a dated
provenance/index at the archive entrance. Delete only candidates marked
`REMOVE / IGNORE` whose unique obligations, backlinks, validator dependencies,
and public-path risks are zero or explicitly accepted. Audit templates, issue
forms, workflows, and generated-artifact rules in separate reversible batches.

Exit: every removed path appears in a manifest with reason and recovery source;
each batch can be reverted independently.

#### CU5 — Verify and close

Run structural validation, controlled mutations, Markdown/backlink checks,
GitHub YAML parsing, affected project checks, secret/generated-artifact scans,
and before/after fresh-context navigation tests. Keep uncertain candidates
deferred rather than forcing closure.

Exit: no broken route, missing obligation, weakened gate, leaked solution, lost
evidence, or discarded active file; cleanup improves orientation or maintenance
and has a complete rollback manifest.

### Cleanup verification and rollback

Use read-only inventory before any removal:

```bash
git status --short --branch
git ls-files
git ls-files --others --exclude-standard
git status --ignored --short
find . -path ./.git -prune -o -type f -print
rg -n 'candidate-name-or-path' --glob '*.md' .
```

Do not use a broad clean command. For every approved batch, record `git diff
--name-status`, old/new paths, link rewrites, Git recovery reference or hashes,
and exact rollback. Then run:

```bash
python3 scripts/check_curriculum.py
python3 scripts/test_validator_mutations.py
git diff --check
git status --short
```

Run affected starter/workflow checks whenever executable or CI material moves.
A passing link check does not prove improved navigation, so repeat the
repository→M0 and affected transition reviews after tracked cleanup.

### Cleanup definition of done

Cleanup is complete only when every candidate has an evidenced disposition;
all approved moves/removals have a manifest and recovery route; current learner
and maintainer authority is unambiguous; historical evidence is retrievable;
ignored-residue policy is accurate; links, validators, YAML, and affected tests
pass; and fresh-context review shows no navigation regression.

Documented `DEFER / OBSERVE` decisions are valid closure. Line-count reduction,
deletion of active untracked work, erased rationale, a weakened seven-file
contract, or extra indirection do not count as cleanup.


## 2026-09-13 IA0 and CU0 execution baseline

Authorization: implement IA/CU locally, preserve the dirty candidate, no commit,
publish, hosted run, or real-target operation. Reference: `d259148` plus the
pre-existing candidate. Recovery copy: `/tmp/vibecamp-ia-cu-nbmj5obs/baseline`;
this host-local copy is temporary assistance, not learner/release evidence.

Read-only inventory found 103 tracked paths and 149 active untracked files.
All 149 untracked files are KEEP: they are the active remediation documents,
five project launch kits, workflow, templates, and mutation suite. No unknown
untracked file is eligible for deletion. Candidate hashes, sizes, status,
backlinks, and Git history were captured before edits. There are 38 explicit
ignored cache directories (83,279,329 logical bytes), five retained virtual
environments, and an empty ignored `dist/`. No active source is cache residue.

Baseline navigation observation (source walkthrough, same-agent maintenance
review; hosted rendering and human timing unavailable): README exposes six
grouped rows instead of eleven stops. M0/M5/M10 have no ordinal, breadcrumb,
explicit bounded repository trust, or previous route. Product/output/gate exist
but need cross-file lookup; M0 lacks a Product brief and Evidence heading;
M5/M10 put the brief after work. M0's concepts/challenge links are whole-file;
M5/M10 have the same broad challenge destination. PROGRESS retains four pause
fields but no exact controller anchor. First command is under Start now;
next action is M0 Block 1. Human time-to-orient/wrong-turn counts are unmeasured,
not zero. These observed missing cues, not document size, motivate the changes.

Source map: CURRICULUM Roadmap owns capability/product/level, each ACCEPTANCE
Core owns gates, existing work blocks own artifacts, USABILITY readiness owns
repository support, PROGRESS owns learner state. Ordinal is label number + 1.
M0 additionally has A0 diagnostic; retain it explicitly alongside A1–A3.

Frozen grammar: breadcrumb metadata, Why, Starting checkpoint with compact
capability/product/output/gate/trust/resume fields, Terms, Product brief,
Work blocks, Failures, Evidence, Done, Recovery, Next with boundary footer.
Commands and C/A contracts remain intact. Each block gets a last-green
prerequisite, work/target/evidence/stop/resume cue and exact support destination.
Use existing heading anchors; add minimal headings only when a resource has no
useful section. Whole-file review/tool references are permitted only when the
whole short document is needed. Execution stays in the learner-owned local
clone on Linux/macOS/WSL2; alternatives remain explicitly optional/later.

Local review protocol: the solo fresh-context option in QUALITY-GATES permits
an isolated copy for an uncommitted maintenance candidate. Put implementation
notes aside and inspect only learner docs, predict a Core observation and a
failure, run supplied commands, then answer a review question. Same-agent
review is maintenance simulation, not independent human evidence. Report source
navigation latency separately from human orientation time. Hosted rendering,
GitHub behavior, and named career-shifter tests remain in the external ledger.


### IA1 signature preview decision

REJECT adding another root preview. The existing synthetic evidence examples
already show evidence shape and are linked after the first run. A second chain
would repeat the lesson and widen the root scan without providing a new next
action. Start now stays in its original position; the eleven-row map replaces
only the grouped roadmap. Reconsider only on named learner feedback. No example
is represented as completed learner work.

Pilot repair before validation: moved M0's detailed deliverables into Product
brief, kept compact orientation inside Starting checkpoint, changed broad
concept links to the exact HTTP-path explanation, and prevented early scope cues
from suggesting premature fault activation. Copying the evidence template is
explicitly first-visit-only so a resume preserves earlier notes.


## CU1 disposition and authority decisions

Evidence: [baseline paths, cache manifest and provenance](docs/maintainers/archive/2026-09-13-remediation/README.md).
All decisions below are authorized local implementation; no publishing permission
is inferred. Recovery of a changed hunk uses the pre-edit local candidate copy,
not HEAD (which lacks valuable user work). Retained paths require no rollback.

| Candidate / owner | Decision and destination | Evidence / references / public risk | Recovery |
|---|---|---|---|
| README maintainer list / PLAN | CONSOLIDATE into `docs/maintainers/README.md` | Six peer maintenance links compete at root; one secondary entry can reach every owner | Restore only original maintainer paragraph |
| README duplicate ownership/exclusion rules / CONTRIBUTING and STACK | CONSOLIDATE into exact canonical links | Initial owned-repository command and all local recovery stay; later ownership paragraph repeats it | Restore these two paragraphs |
| PLAN and TODO / maintainers | KEEP full history; add concise status/evidence navigation | Active IA/CU dependencies and completed results interleave; compaction risks losing obligations and citations | No snapshot or second tracker; originals remain |
| PERSONA-REVIEW and ANALYSIS / maintainers | KEEP at original paths | Both are active untracked inputs with live links and unknown public exposure | No move; future archive requires fresh path evidence |
| USABILITY historical results / rubric owner | KEEP dated sections; append current bounded result | Baseline comparisons remain necessary; historical scores are not current claims | No removal |
| All milestone files / curriculum | KEEP 11×7; navigation only in controllers | Core/Stretch and 58 traces unique; local action context required | Reverse only IA hunks |
| All project files / launch-kit owners | KEEP, including untracked code/spec/test/lockfiles | Independently runnable, no neutral setup centralization justified | No source mutation |
| Cache manifest / local tools | REMOVE / IGNORE enumerated directories only | Ignore checks and tool regeneration; 83,279,329 logical bytes | Run owning checks |
| Five .venv directories / workstation owner | DEFER / OBSERVE | Useful active dependencies; no disk-recovery goal | Retain until fresh authority |
| dist, evidence, logs, databases, coverage and images / artifact owner | KEEP; uncertain future artifacts DEFER / OBSERVE | dist empty; no provenance-based authority to remove evidence | Retain until fresh authority |
| Issue forms and PR / workflow owner | KEEP all fields and forms | bug = defect, help = diagnosis after hints, milestone = gate planning, PR = review; no duplicate obligation | No form removal |
| Hygiene and M10 workflows / workflow owner | KEEP separate event and permission boundaries | Shared starter commands intentionally repeated: push/PR versus tag/manual publication with needs, audit and approval; reusable refactor adds hosted validation risk | No workflow behavior change; hosted runs remain external |

### Template dispositions

All templates are KEEP. Wiring changes supply missing exact links; no unique
obligation is merged away. Requirements owns Given/When/Then, decision rights,
and changed scope (M1 Block 4). Incident/postmortem owns after-incident impact,
timeline, contributing conditions and follow-ups (M6/M10). RUNBOOK-INCIDENT owns
the during-incident lead, communication and containment procedure (M10), then
links the retrospective. These are complementary time phases, not duplicates.

| Template | Live obligation / consumer | Disposition |
|---|---|---|
| ADR.md | consequential design decisions / QUALITY-GATES | KEEP |
| COMPLEXITY-REJECTION.md | rejected complexity / M4, M7, M9, M10 | KEEP |
| DATA-LIFECYCLE.md | storage/access/retention / M2, M5–M7, M9–M10 | KEEP |
| ENTRY-DIAGNOSTIC.md | targeted M0 remediation / A0 | KEEP |
| EVIDENCE-INDEX.md | reproducible C/A proof / every milestone | KEEP |
| EVIDENCE-EXAMPLES.md | explicitly synthetic evidence shape / root | KEEP |
| REQUIREMENTS.md | M1 changed-requirement record | KEEP; wire exact section |
| INCIDENT-POSTMORTEM.md | M6 A3 and M10 A4 retrospective | KEEP; wire exact section |
| PORTFOLIO-CASE-STUDY.md | M4 draft and M10 reader path | KEEP |
| TRANSITION-REVIEW.md | maintenance/human transition scorecard | KEEP |
| SEMANTIC-AUDIT.md | maintainer requirements-to-proof audit | KEEP |
| RUNBOOK-MIGRATION.md | M10 migration preconditions/execute/recovery | KEEP |
| RUNBOOK-RELEASE-REJECTION.md | M10 unhealthy candidate | KEEP |
| RUNBOOK-RESTORE.md | M10 isolated recovery | KEEP |
| RUNBOOK-INCIDENT.md | M10 live response then retrospective | KEEP; link postmortem |

CU3/CU4 design: no historical moves, no PLAN/TODO content deletion, no template
or workflow removal. Those candidate actions resolve as evidenced KEEP, not as
unexecuted mandatory deletions. The one maintainer route and exact general-rule
links are the approved consolidation batch after IA2 ROLL OUT. Cache cleanup
is a separate action. No `git mv` is needed because no historical move is approved.

IA2 decision: **ROLL OUT** local grammar; [pilot evidence](USABILITY.md#2026-09-13-ia-pilot-and-rollout-evidence). CU1 decisions above are now frozen for the authorized local batches. Named human and hosted observations remain external.


## Stable IA invariants after the controller audit

All eleven controllers now preserve original fenced commands and literal command
rows. Manual source audit accepts the grammar after batches M1–M2, M4–M5,
M7–M9, then M3/M6/M10. M10 local Core and optional real-target endorsement stay
separate; fixed products, C/A IDs, seven-file roles and Core/Stretch are unchanged.

Automate only: eleven root route rows in numeric M0–M10 order, ordinal equals
label + 1, each root label links its controller, controller ordinal/breadcrumb,
previous/home/next destinations including M0/M10 boundaries, exact controller
section order, and resolvable relative anchors. Parse links rather than counting
words. Require navigation metadata only on active controllers, not archived
reviews or learner evidence. Do not validate prose tone, effort/time estimates,
mastery, human scores, or learner completion from headings. Keep local commands
and source contracts independently validated. If headings legitimately change,
update their links and mutation targets together; no prose wording is a mastery
signal. GitHub anchors preserve repeated hyphens after punctuation removal;
correct the old collapsing implementation and repair references before final
navigation evidence. A broken exact anchor must fail specifically, not merely
coincide with another broken rule.

Approved tests: wrong M5 ordinal, absent home/previous/next, swapped root rows,
wrong root destination, Product brief out of order, broken exact support anchor.
Each mutation must begin from a green isolated candidate, fail with the intended
diagnostic, restore, then end green. No mutation runs against the valuable tree.


## CU3 and CU4 executed consolidation

README now exposes one secondary maintainer index after the learner route;
all six active owners/audit inputs remain reachable. Duplicate later ownership
and advanced-exclusion prose link CONTRIBUTING and STACK; the initial create/
clone/check/recover commands remain local and unchanged. Templates are retained:
M1 now links REQUIREMENTS change record; M6 and RUNBOOK-INCIDENT link the
postmortem's impact section. SEMANTIC-AUDIT now routes new conflicts to PLAN/TODO,
so historical ANALYSIS no longer acts as parallel current authority.

PLAN/TODO compaction decision: KEEP full evidence, use current status and exact
section links for scanning. No approved historical move or tracked removal;
CU4 historical-move task resolves KEEP. No old public paths disappeared and no
archived tracker exists. Workflows/forms remain KEEP, as authorized by the task's
preference for preserving unique gates. Hosted behavior is still unobserved.

Backtracking comparison: first learner action is unchanged, root→M0 remains one
link after quickstart, maintenance is explicitly secondary, and no local command
requires a new lookup. Exact links validate after punctuation repair. Rollback
is limited to the root paragraphs/index and template link edits; never restore
HEAD over the dirty candidate.


## Local IA and cleanup closeout

IA0–IA5 and CU0–CU5 are locally complete. [Current verification and final
transition observations](USABILITY.md#ia5-and-cu5-final-transition-review)
record the solo maintenance method and its limits. The stronger hosted-rendered,
human and real-target claims remain external in TODO. Prior completed evidence
is retained. No commit, push, issue submission, deployment or publication occurred.

The prior-phase closeout recorded in this section supersedes future-tense design
language in the preserved IA/CU history. The new active CS plan below owns the
next revision decisions, TODO is the sole active
maintenance tracker, PROGRESS is untouched learner advancement. Historical
inputs remain at their original public paths; no archived PLAN/TODO tracker exists.
The approved KEEP/no-compaction decisions close those candidate actions without
pretending that a move, removal or workflow refactor happened.

Maintenance changes: root README/PROGRESS, eleven controller READMEs,
PLAN/TODO/USABILITY, both validator scripts, SEMANTIC-AUDIT and RUNBOOK-INCIDENT
links; new maintainer index and dated provenance/inventory. No starter source,
spec/test/lockfile, support milestone contract, workflow, issue form, environment,
learner evidence or release artifact changed. Only 38 named ignored caches were
removed and normal checks recreated 37. Refer to the removal manifest for exact
paths and regeneration. Source hashes were compared with the pre-edit candidate;
HEAD alone is not an adequate recovery source for the original dirty work.

## Active plan — career-shifter/self-paced instructional revision

This is the canonical rationale, scope, and implementation sequence for the next
curriculum revision. It begins after the completed R1–R7, IA0–IA5, and CU0–CU5
work above. Those phases and their evidence remain closed; their hosted, named-
human, and authorized real-target checklist items remain external and unchecked.
This planning update changes no learner lesson, starter, validator, workflow, or
learner progress record.

The governing principle is:

> Practical engineering without compromise. Use the smallest tool that preserves correctness, security, maintainability, and operability. Add complexity only when the product earns it.

### Current state: strength and remaining friction

Already working: GitHub is the only delivery surface; the root README is the
learner front door; all eleven M0–M10 controllers have the completed IA grammar;
each milestone has exactly seven role-specific files; five launch kits provide
neutral, runnable starting points; Core and Stretch are distinct; challenges are
deterministic; advancement requires evidence; and the course repeatedly asks the
learner to build, break, debug, refactor, operate, and ship. Local structure,
links, starters, PostgreSQL paths, controlled mutations, and the M10 rehearsal
have bounded verification. No completed learner solutions are supplied, and CI
is deterministic without provider secrets.

The remaining friction is instructional, not structural. The root-table override
now shows concepts, FastAPI/Python tools, integration status, and capability in
one scan; deeper lesson and contract work remains pending. Some blocks lead with
identifiers or repeated contract boilerplate before the concrete problem. Tool
timing is distributed across files, so learners can mistake an ecosystem package
for the concept it automates. Several narrow contradictions make Core scope and
proof ambiguous, especially in M4, M6, M7, and M9. Real-provider work is either
prohibited or weakly modeled where one bounded sandbox experiment would teach the
boundary honestly. Historical score language also conflicts with the current
nine-dimension, 0–4 `USABILITY.md` rubric.

### Frozen course shape and five-product journey

The revision keeps M0–M10 exactly: eleven milestones, exactly seven files per
milestone, and the current maturity arc. The five-product journey remains
Catalog (M0–M1) → POS (M2–M4 and M10 capstone) → Ecommerce (M5–M7) → Booking
(M8) → Social (M9). The root `README.md` remains the only front door and route
controller. By explicit user override on 2026-09-14, its primary course table—not
`CURRICULUM.md`—owns the combined organization/reference scan. Delivery stays
GitHub-only through local work, issues, pull requests, Actions, project-local
evidence, and tags/releases.
No learning-management system, website, or second track is introduced.

Levels, Core/Stretch, the 58 stable top-level concept traces, the recurring
engineering cycle, and evidence-based advancement remain. Career-shifter and
data-specialist lenses frame the same work and gates. Implementation may supply
contracts, controlled failures, and neutral seams, but never completed learner
solutions or fabricated evidence.

### Root course-table override — implemented 2026-09-14

The earlier compact-root/eight-column-only-`CURRICULUM.md` proposal is
superseded. The primary table in `README.md` now has exactly these six columns:
`#`; `Milestone / Capability`; `Project`; `Key concepts`;
`FastAPI / Python tools`; `Real integration`. It has exactly eleven M0–M10 rows
in order; `#` pairs ordinal and label (`1 · M0` through `11 · M10`); and the
capability text links each milestone controller. It shows the five-product
journey, concise earned-tool qualifiers, deterministic/local Core throughout,
the one required M6 Stripe-like sandbox after local Core, and only the approved
optional M7/M10 integrations. It explicitly avoids any provider-account or
secret prerequisite at course start.

`CURRICULUM.md` remains the detailed maturity and concept-trace authority and
must not receive a duplicate version of the root table. `STACK.md` owns adoption
and removal detail; `QUALITY-GATES.md` owns evidence thresholds. Future CS work
may refine the underlying contracts, but must update the root row in place and
must not recreate the superseded eight-column table elsewhere.

### Learner grammar and visible block contract

Every revised teaching slice follows this causal grammar:

**Concrete problem/example → necessary concept → smallest implementation → failure → diagnosis → proof → tool decision**

The visible learner layer uses plain names before stable `C#`/`A#` references
and exposes five short cues:

- **Do:** the bounded action, working directory, files, and exact command.
- **Understand:** the minimum concept needed for that action, introduced through
  the concrete example rather than a survey.
- **Check:** the expected observation and evidence destination.
- **If it fails:** the diagnostic question, targeted hint, recovery/reset, and
  protection of the last-green state.
- **Stop/resume:** the safe stopping condition and exact return anchor/command.

These cues compress presentation; they do not remove challenge modes, C/A
traceability, the controller section order, evidence, recovery, or the full
build/break/debug/refactor/operate/ship loop.

### Tool ladder and timing

1. Start with FastAPI, Uvicorn, Pydantic, and settings so configuration and HTTP
   behavior stay visible.
2. Introduce `APIRouter`, `Depends`, and generated OpenAPI when multiple routes,
   composition, or public-contract inspection creates the need.
3. Teach ordering, limits/cursors, error semantics, and insertion-between-pages
   behavior by hand before evaluating `fastapi-pagination`. The adapter must
   preserve the contract; it does not define it.
4. Teach explicit CRUD and transaction ownership before evaluating FastCRUD.
   Treat it as a comparison, not the default architecture. Verify generated
   query/response behavior, do not let a helper commit independently, and do not
   introduce async sessions merely to fit an adapter: async must earn itself
   through measured need, with session lifetime and commit/rollback caveats made
   explicit.
5. Teach authentication versus authorization, credential/session lifecycle,
   object checks, and negative cases before FastAPI Security helpers. M5 Core is
   a first-party secure cookie session; JWT remains a bounded comparison/Stretch.
6. Use `BackgroundTasks` first only for short, disposable, safe-to-lose/repeat
   work. Deliberately crash it to contrast acknowledgement with durability before
   M7's database outbox/worker. A process-local callback never satisfies a
   durable obligation.
7. Add Redis, native server-sent events (SSE), or WebSockets only after a named
   workload or latency/interaction need fails the simpler design. PostgreSQL
   remains durable truth; SSE is one-way and WebSockets require a bidirectional
   need.
8. Add SQLAdmin only after tenant authorization and append-only audit behavior
   are proven, and test tenant scope and audit on every administrative action.
9. Choose Sentry **or** Logfire—not both—to answer one named diagnostic question;
   bound redaction, sampling, retention, ownership, and cost before retention.

### Real-integration taxonomy and classification

| Class | Meaning | Milestones |
|---|---|---|
| Deterministic offline Core | Required behavior is reproducible in local tests/fixtures, CI needs no provider secrets, and failure modes can be replayed | Every milestone, M0–M10 |
| REQUIRED real-provider experiment | A bounded credentialed sandbox observation supplements local Core and is required for the real-provider evidence claim | Exactly M6: one Stripe-like payment sandbox, only after local Core |
| OPTIONAL endorsement | Stronger evidence that never blocks Core or creates an account prerequisite | M7 email test provider; M10 S3-compatible storage, OAuth/OIDC, Sentry or Logfire, SQLAdmin, and authorized real deployment |

The curriculum must not turn four or more provider accounts into prerequisites.
If M6 provider access is unavailable or the sandbox is down, record the provider
step as `PENDING — ACCESS/PROVIDER OUTAGE`, continue any independent local work,
and preserve the last-green local state. Pending access cannot count as a real-
provider observation or complete that evidence requirement. All real calls,
including sandbox calls, require separate explicit authorization at implementation
time; CI and ordinary local checks remain secret-free and offline.

### M6 payment ladder: fake → protocol/SDK → sandbox

1. **Deterministic fake provider.** Model success, decline, connect timeout,
   response/read timeout, total deadline exhaustion, timeout-before-processing,
   timeout-after-processing, duplicate delivery, out-of-order delivery, refund
   success/failure/unknown, and lookup/reconciliation. Keep provider facts and
   local business state separate and prove the local state machine first.
2. **Understand the boundary.** Explain test versus live keys, least privilege,
   environment isolation, rotation/redaction, and why keys never enter Git,
   evidence, URLs, logs, fixtures, or CI. Compare direct HTTP with the selected
   provider SDK: the SDK may handle serialization/signing/retries, but the
   application still owns business state, deadlines, idempotency, and recovery.
   Configure and observe separate connect, read, and total timeouts. Define one
   combined SDK/application retry budget so nested retries cannot multiply
   requests beyond the deadline.
3. **Webhook correctness.** Verify the provider signature over the exact raw
   request body before JSON parsing or mutation, with the provider timestamp and
   tolerance where supported. Persist the provider event ID and business
   idempotency key durably. Treat duplicates as normal, tolerate out-of-order
   events through legal state transitions/current-provider lookup, and return a
   bounded response without claiming the side effect happened exactly once.
4. **Refunds and uncertainty.** Teach full/partial refund vocabulary if supported,
   repeat-refund idempotency, decline/failure, timeout before and after provider
   processing, and a local `pending/unknown` state that blocks unsafe repetition.
   A database rollback cannot undo provider money. On an unknown outcome, do not
   guess or blindly retry: look up by provider operation/idempotency key, compare
   provider fact with local intent, reconcile forward, and leave an auditable
   operator decision when automation cannot resolve it.
5. **One authorized Stripe-like sandbox experiment.** After local Core is green,
   use a test credential and test instrument to perform the chosen payment flow,
   retrieve/lookup the result, receive and verify a signed webhook, exercise one
   bounded refund, and reconcile local/provider records. Store only sanitized
   request IDs, timestamps, status transitions, timeout/retry settings, webhook
   verification result, refund/lookup result, and cleanup outcome. Revoke/delete
   task-scoped credentials where supported and remove local secrets/transient
   provider objects according to the sandbox's safe cleanup controls; never put
   secret values, full payloads, customer data, or payment instruments in evidence.

Provider interface vocabulary must be decided before implementation. Prefer a
payment-shaped port such as `authorize`, `capture`, `refund`, and `lookup` if the
selected reference flow teaches those distinct facts; otherwise choose a single
documented immediate-payment operation consistently. Do not leave a fake
`charge` method contradicting an authorize/capture learner contract.

### Other bounded integration ladders

- **Email (M7 optional):** deterministic Core records intent, attempts,
  idempotency/deduplication window, provider message ID, and terminal/uncertain
  result. A provider's API acceptance means it accepted the request, not that a
  mailbox received, displayed, or was read. Retries and duplicate suppression
  have explicit limits; no exactly-once delivery claim is allowed.
- **S3-compatible storage (M10 optional):** define tenant-scoped, non-secret
  object keys; authentication/authorization; content length/type; presigned URL
  scope and short expiry; checksum verification; overwrite/version behavior;
  delete/retention; partial failures; and orphan cleanup/reconciliation. Database
  rollback does not remove an uploaded object.
- **OAuth/OIDC (M10 optional):** use OAuth 2 authorization code with Proof Key
  for Code Exchange (PKCE) and OpenID Connect (OIDC) identity validation. Test
  state/nonce, redirect allowlist, issuer/audience/signature/expiry, key rotation,
  callback errors, logout/revocation assumptions, and explicit account linking/
  unlinking rules. Do not teach the resource-owner password grant.
- **Monitoring (M10 optional):** choose Sentry or Logfire for one named question,
  define field redaction, environment separation, sampling, retention, access,
  budget/cost limit, and deletion. Inject one synthetic failure, correlate it
  without personal/secrets leakage, record the answer, then decide retain/remove.

### Primary implementation references

Re-verify these official sources when implementation begins and record the
retrieval date in the affected `RESOURCES.md` or `STACK.md`; product and library
behavior can change. Prefer primary documentation over tutorials:

- FastAPI: [BackgroundTasks](https://fastapi.tiangolo.com/tutorial/background-tasks/),
  [security helpers](https://fastapi.tiangolo.com/reference/security/), and
  [server-sent events](https://fastapi.tiangolo.com/tutorial/server-sent-events/).
- Starlette: [background task execution](https://starlette.dev/background/).
- FastCRUD: [documentation](https://benavlabs.github.io/fastcrud/) and
  [commit control](https://benavlabs.github.io/fastcrud/advanced/crud/#skipping-database-commit).
- fastapi-pagination: [documentation](https://uriyyo-fastapi-pagination.netlify.app/)
  and [SQLAlchemy integration](https://uriyyo-fastapi-pagination.netlify.app/integrations/sqlalchemy/general/).
- Stripe: [sandboxes](https://docs.stripe.com/sandboxes),
  [API keys](https://docs.stripe.com/keys),
  [idempotent requests](https://docs.stripe.com/api/idempotent_requests),
  [low-level errors](https://docs.stripe.com/error-low-level),
  [webhooks](https://docs.stripe.com/webhooks),
  [signature verification](https://docs.stripe.com/webhooks/signature),
  [refunds](https://docs.stripe.com/refunds), and the
  [official Python SDK](https://github.com/stripe/stripe-python).
- Storage: [Amazon S3 presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html)
  and [Cloudflare R2 S3 compatibility](https://developers.cloudflare.com/r2/api/s3/api/).
- OAuth/OIDC: [OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/rfc/rfc9700.html),
  [Authlib's FastAPI client integration](https://docs.authlib.org/en/latest/oauth2/client/web/fastapi.html),
  and [Google OpenID Connect](https://developers.google.com/identity/openid-connect/openid-connect).
- Observability/admin: [Sentry for FastAPI](https://docs.sentry.io/platforms/python/integrations/fastapi/),
  [Logfire for FastAPI](https://pydantic.dev/docs/logfire/integrations/web-frameworks/fastapi/),
  and [SQLAdmin](https://smithyhq.github.io/sqladmin/).

### Contradictions to repair before expansion

### CS0 execution record and frozen decisions — 2026-09-14

Baseline reference: `main` at the existing dirty candidate (`PLAN.md`,
`README.md`, `TODO.md`, `scripts/check_curriculum.py`, and
`scripts/test_validator_mutations.py` modified before CS learner edits). The
baseline validator reported 11 milestone directories, exactly seven contract
files in each, and 58 traced concepts; all 33 pre-existing controlled mutations
passed, `git diff --check` passed, and no provider access was assumed. Prior
R/IA/CU work remains closed; hosted, named-human, real-target, and credentialed
provider evidence remains external and unchecked. These paths are user-owned and
must not be restored from `HEAD` as a rollback mechanism.

The four contradiction decisions are frozen as follows:

1. **Evidence ownership:** evidence is project-local. From a milestone's stated
   `projects/<product>/` working directory, `evidence/MN/...` resolves to
   `projects/<product>/evidence/MN/...`. Root documents use the fully qualified
   project path when referring to an artifact. Existing artifacts stay in place;
   this is a link/wording migration, not a move or overwrite.
2. **M4 Core:** the only Core stakeholder change is the supplied optional
   `cashier_name` receipt field, including legacy rows returning `null`.
   Promotions/returns remain background examples only where needed to explain
   coupling; no second implementation variant is required. Any future variant
   is Stretch and must bring its own complete contract and tests.
3. **M6 payment vocabulary:** use one immediate-payment port with `pay`,
   `refund`, and `lookup` operations, modeled after a confirmed Stripe-like
   PaymentIntent rather than an unimplemented authorize/capture split. Provider
   facts are `succeeded`, `declined`, or `unknown`; local state remains separate.
   The deterministic fake and learner port share these names. A separately
   authorized sandbox may map the same contract to its provider SDK.
4. **M9 realtime:** Core SSE is earned by the fixed, measurable one-way update
   requirement after polling misses its latency bound. Core must define and test
   disconnect/reconnect, gaps, restart/loss, and slow-consumer behavior. SSE does
   not become durable truth. WebSockets remain Stretch until a bidirectional
   need is observed.

The causal grammar and integration taxonomy above are also frozen. The root
six-column table stays canonical; every milestone retains deterministic offline
Core; only the M6 sandbox is a required real-provider experiment, and the listed
M7/M10 integrations remain optional endorsements.

Official-reference review completed 2026-09-14 against the primary links above
and the locked project manifests (`fastapi[standard]>=0.116.0`; optional tools
are not installed). Current FastAPI documents post-response `BackgroundTasks`,
security helpers, and native SSE; Starlette documents response-attached task
execution. FastCRUD documents explicit commit control; fastapi-pagination's
SQLAlchemy adapter still operates on an application query/session rather than
owning the course's ordering contract. Stripe documents isolated sandboxes,
restricted/test keys, idempotent request behavior, ambiguous low-level network
failures, raw-body webhook verification, and refunds. S3 presigned URLs remain
bearer access bounded by credential policy and expiry. RFC 9700 supports
authorization code plus PKCE and rejects the resource-owner password grant.
Sentry, Logfire, and SQLAdmin remain optional because their documentation does
not establish a course need. Where a documentation site did not render through
the read-only fetch, the integration stays deferred rather than being inferred.
Affected `RESOURCES.md` files carry the same retrieval date.

| Conflict | Exact target files/scopes | Required repair |
|---|---|---|
| Root versus project-local evidence paths | `README.md`; `QUALITY-GATES.md`; `PROGRESS.md`; `templates/EVIDENCE-INDEX.md`; `milestones/*/{README,CHALLENGE,ACCEPTANCE}.md`; project `evidence/` examples | Choose one learner-owned convention and make every command unambiguous from its stated working directory; migrate links without losing existing evidence. |
| M2 mandatory-sounding repository/service layers versus earned boundaries | `CURRICULUM.md` concept row; `STACK.md`; `milestones/m2-pos-persistence-data-modeling/{README,CONCEPTS,CHALLENGE,TOOLS,ACCEPTANCE,REVIEW,RESOURCES}.md`; `projects/pos/specs/M2-PERSISTENCE-CONTRACT.md` | Permit direct route-to-SQLAlchemy for simple work; require a service/repository only when orchestration, invariants, duplication, or substitution earns it. |
| M3 local transaction versus remote money boundary | M3 seven-file milestone set; `projects/pos/specs/M3-CHECKOUT-CONTRACT.md`; M6 handoff wording | State that the database transaction owns local checkout/inventory/intent only; remote provider money needs idempotency, unknown-state handling, lookup, and reconciliation. |
| M4 cashier-name spec versus returns/promotions prose and unsupported second variant | M4 seven-file milestone set; `projects/pos/specs/M4-CHANGE-BRIEF.md`; portfolio/template references | Decide and use one Core change everywhere; default proposal is the existing cashier-name change. Remove mandatory returns/promotions and any unsupported second variant or label a bounded alternative Stretch. |
| M5 required PyJWT lab versus cookie Core/JWT Stretch | M5 seven-file milestone set; `projects/ecommerce/specs/M5-SECURITY-CONTRACT.md`; `projects/ecommerce/REQUIREMENTS.md`; `STACK.md`; relevant contract tests | Keep secure cookie session Core. Make PyJWT comparison/Stretch conditional and prevent acceptance or resources from implying it is required. |
| M6 prohibited real calls, authorize/capture/lookup versus fake charge, missing refund, weak timeout model | M6 seven-file milestone set; `projects/ecommerce/specs/M6-INTEGRATION-CONTRACT.md`; `projects/ecommerce/src/ecommerce_api/provider_fake.py`; `projects/ecommerce/tests/test_failure_harnesses.py`; settings/env/dependency files only if the chosen sandbox earns them | Preserve deterministic fake Core, add refund and connect/read/total/unknown cases, settle interface vocabulary, then authorize exactly one separately approved sandbox experiment. |
| M7 exactly-once external email claims | M7 seven-file milestone set; `projects/ecommerce/specs/M7-JOB-CONTRACT.md`; worker/outbox seams and tests; email endorsement material if added | Use at-least-once processing plus bounded business idempotency; distinguish provider acceptance from delivery and state duplicate limits. |
| M9 SSE required versus earned-tool policy | M9 seven-file milestone set; `projects/social/specs/M9-FEED-CONTRACT.md`; `STACK.md`; social tests/harness | Decide whether Core is polling with an earned SSE experiment or SSE is required by a fixed latency constraint; keep WebSockets Stretch and align every file. |
| `pytest -s` or missing-test mechanics treated as proof | `milestones/*/{README,CHALLENGE,ACCEPTANCE}.md`; project tests/contracts referenced by changed blocks | Replace output-capture flags and absent-file/selector failures with substantive behavioral assertions, intended red states, and deterministic reset-to-green proof. |
| Concept first-use drift | `CURRICULUM.md` coverage matrix; `GLOSSARY.md`; `milestones/*/{README,CONCEPTS,CHALLENGE,ACCEPTANCE}.md` | Trace each decision-driving concept to its first concrete example, later practice, and objective proof; define it where first used. |
| Historical `4/5`, five/ten-dimension language versus current rubric | active claims in `PLAN.md` and `TODO.md`; `USABILITY.md` only during implementation if its current authority needs clarification; `templates/TRANSITION-REVIEW.md` | Use the current nine dimensions scored 0–4, release threshold at least 85/100 and no dimension below 3; label immutable historical results rather than silently rewriting their evidence. |

The four decisions that freeze contradiction repair are: one M4 Core change and
any variant status; one M6 provider reference flow and interface vocabulary; one
evidence-path convention; and whether M9 SSE is Core because of a fixed need or
an earned experiment after polling. No broad curriculum rewrite begins until
these are recorded.

### Simplification and pilot boundary

Compress repeated block boilerplate into the five visible cues while retaining
unique commands, failure fixtures, expected observations, hints, evidence,
recovery, and stop/resume state. Put plain block/scenario names before `C#`/`A#`
IDs. Keep support wording short and action-specific. Move maintainer/process
explanation behind learner action or exact links. Preserve unique templates and
their obligations. Keep the concept coverage matrix as a secondary audit map,
not the primary lesson route.

Pilot the grammar on exactly one representative M0 block and one difficult M6
payment block before broad rollout. Compare orientation, action selection,
failure diagnosis, evidence capture, and resume accuracy. The pilot may change
only its named blocks and unavoidable exact-link targets. It must preserve the
controller order, commands' substantive meaning, Core gates, C/A traceability,
and solution boundary. Roll out only after a stop/go decision based on the
current nine-dimension rubric and no regression below 3.

### Phased dependency order and gates

| Phase | Depends on | Work and gate |
|---|---|---|
| CS0 — Baseline and decision freeze | Prior local closeout | Re-run structural baseline; inventory first-use/tool/integration/evidence conflicts; record the four decisions. Gate: one internally consistent contract and no learner-file edits yet. |
| CS1 — Contradiction repair | CS0 decisions | Repair only the narrow conflicts above. **STOP/GO 1:** validator/mutations, YAML, affected project/PostgreSQL checks, and manual contract trace pass before expansion. |
| CS2 — Root course table and tool visibility | Root-table override implemented; remaining work depends on CS1 GO | Preserve the validated six-column table in `README.md`; align `STACK.md`, `QUALITY-GATES.md`, glossary, and milestone tool decisions without duplicating the table in `CURRICULUM.md`. |
| CS3 — Two-block compression pilot | CS2 stable authority | Apply the visible grammar to one M0 block and one hard M6 block; fresh-context review both. **STOP/GO 2:** roll out, revise, or revert based on observed behavior and rubric. |
| CS4 — M6 deterministic contract and sandbox implementation | CS3 GO | Complete the fake/provider contract, refund/timeout/reconciliation tests, then keep the credentialed sandbox evidence as a separate authorized task. Local Core stays deterministic and secret-free. |
| CS5 — Bounded rollout and optional endorsements | CS4 local green and sandbox status honestly recorded | Roll accepted grammar through remaining blocks in risk-ordered batches. **STOP/GO 3 before optional integrations:** require an observed need, owner, cost/data/safety boundary, removal trigger, access, and explicit authorization. Optional endorsements never block Core. |
| CS6 — Validator migration and closeout | Stable CS1–CS5 contracts | Update only durable semantic checks/mutations, run the full local matrix, perform named human reviews, repair and rerun failures, and close local versus external evidence separately. |

### CS gate decisions and optional-integration review — 2026-09-14

- **STOP/GO 1: GO.** The narrow contradiction batch preserves 11×7, 58 traces,
  Core/Stretch, the learner-solution boundary, and offline CI. Root validation,
  controlled mutations, YAML parsing, affected locked project checks, and four
  isolated PostgreSQL upgrade/current/test runs passed. No provider or human
  evidence was inferred.
- **STOP/GO 2: ROLL OUT.** The M0/M6 pilot scored 97.5/100 for both scopes with
  no dimension below 3 in the dated internal maintenance review in
  `USABILITY.md`. It is not named-human evidence.
- **CS4 local: GO.** The neutral M6 fake now exposes immediate `pay`, `refund`,
  `lookup`, timeout phases, post-effect uncertainty, and a combined retry budget;
  local tests pass without credentials. The sandbox remains pending authority.

STOP/GO 3 applies the [complexity-rejection](templates/COMPLEXITY-REJECTION.md)
questions and [data-lifecycle](templates/DATA-LIFECYCLE.md) boundary without
creating learner evidence. No observed local need or external authority exists,
so every endorsement receives a separate **NO-GO — DO NOT ADD YET** decision:

| Optional endorsement | Observed need / simpler baseline | Owner, data/cost/access boundary | Removal trigger / decision |
|---|---|---|---|
| M7 email provider | No mailbox/provider question observed; deterministic intent/acceptance fake is sufficient | No owner, recipient, credential, privacy or spend authority | Any provider dependency is removable; **NO-GO** |
| M10 S3-compatible storage | No file-lifecycle requirement; PostgreSQL/local rehearsal covers Core | No bucket owner, object-data approval, credential, retention or cost cap | Remove until files must outlive instances; **NO-GO** |
| M10 OAuth/OIDC | First-party cookie Core has no external identity requirement | No identity owner, test users/client, redirect or credential authority | Remove until an external identity boundary is observed; **NO-GO** |
| M10 Sentry or Logfire | Existing redacted local signals answer the rehearsal question | No telemetry owner, data-processing approval, DSN, retention or budget | Remove until one named question remains unanswered; **NO-GO** |
| M10 SQLAdmin | No administrative workflow beyond ordinary authorized paths | No surface owner or exposure authority; tenant/audit Core is learner work | Remove until repeated operator work earns it; **NO-GO** |
| M10 real deployment | Local two-environment rehearsal is the authorized scope | No target owner, credentials, TLS/secrets/backup/monitoring or spend approval | Do not deploy until all prerequisites and authority exist; **NO-GO** |

These NO-GO decisions preserve each optional checklist item as unchecked and
non-blocking. They do not prohibit a later learner-owned experiment after a new
observed need and explicit authority.

### Exact target file map

| Work | Authorized implementation targets after planning | Excluded or conditional |
|---|---|---|
| Course authority and route | `README.md`, `CURRICULUM.md`, `STACK.md`, `QUALITY-GATES.md`, `GLOSSARY.md` | Preserve the root six-column primary table; do not duplicate it in `CURRICULUM.md`; `PROGRESS.md` only if an evidence-path migration must preserve learner resume data |
| Learner controllers/support | `milestones/m0-engineering-baseline/*.md` through `milestones/m10-production-multitenant-saas-capstone/*.md` | Always retain exactly the seven existing files; no new lesson file |
| Product contracts | `projects/catalog/specs/M1-PRODUCT-BRIEF.md`; `projects/catalog/contracts/*`; `projects/pos/specs/M2-PERSISTENCE-CONTRACT.md`, `M3-CHECKOUT-CONTRACT.md`, `M4-CHANGE-BRIEF.md`, `M10-CAPSTONE-CONTRACT.md`; `projects/ecommerce/specs/M5-SECURITY-CONTRACT.md`, `M6-INTEGRATION-CONTRACT.md`, `M7-JOB-CONTRACT.md`; `projects/booking/specs/M8-BOOKING-CONTRACT.md`; `projects/social/specs/M9-FEED-CONTRACT.md` | Contract/fixture work must remain incomplete learner scaffolding |
| Deterministic project support | affected `projects/{catalog,pos,ecommerce,booking,social}/{README.md,REQUIREMENTS.md,.env.example,pyproject.toml,uv.lock,src/**,tests/**,contracts/**}` and existing migration/Compose files only when required by the settled contract | No real credentials, live endpoints, completed domain implementation, or unrelated dependency refresh |
| External evidence | learner-owned project-local evidence indexes/assets, named human transition records, and sanitized provider/deployment observations | Never write secrets/customer/payment data; provider calls and deployment require separate explicit authority |
| Automation | `scripts/check_curriculum.py`, `scripts/test_validator_mutations.py`, `.github/workflows/repository-hygiene.yml`, `.github/workflows/m10-image.yml` | Change workflows only for stable, deterministic, provider-secret-free checks; hosted execution remains external |
| Maintenance record | `PLAN.md`, `TODO.md`, `USABILITY.md`, `templates/TRANSITION-REVIEW.md`, existing unique evidence/runbook/decision templates | `PROGRESS.md` remains learner progress; preserve prior IA/CU history and external items |

### Risks, safety, rollback, and verification

| Risk | Control and rollback boundary |
|---|---|
| Compression removes learning or recovery detail | Compare each pilot against the pre-change block contract; revert only that block if any unique action, failure, proof, or resume cue disappears. |
| Tool visibility becomes a package survey | Every tool follows an observed problem, simpler baseline, evaluation, operational cost, and removal trigger; revert the tool insertion without reverting the concept. |
| Provider dependence blocks self-study or CI | Offline deterministic Core exists everywhere; exactly one M6 sandbox is separately authorized; outage is pending, never simulated as evidence. Remove/revoke task-scoped secrets and keep provider jobs out of CI. |
| Retrying duplicates money or messages | Combine SDK/application retry budgets, use durable business idempotency, lookup/reconciliation, and explicitly teach that database rollback cannot reverse an external effect. |
| Evidence leaks secrets or personal data | Use test tenants/instruments, redact headers/bodies/addresses, store only sanitized IDs/status/timing, scan diffs, and discard unsafe captures rather than editing them into plausibility. |
| Existing work/history is overwritten | Patch in dependency-sized batches, record pre-change status, preserve checked IA/CU and external tasks, and revert only the failing batch/hunk. |
| Validator overfits prose | Automate exact rows, classifications, paths, anchors, and stable contract facts only; keep comprehension/tool judgment for human review and remove noisy rule plus mutation together. |

Baseline and every completed local phase run from the repository root:

```bash
python3 -B scripts/check_curriculum.py
python3 -B scripts/test_validator_mutations.py
git diff --check
python3 - <<'PY'
from pathlib import Path
import yaml
for path in sorted(Path('.github').rglob('*.y*ml')):
    yaml.safe_load(path.read_text())
    print(path)
PY
```

Affected projects additionally run `uv sync --locked`, `uv run --locked ruff
check .`, `uv run --locked ruff format --check .`, `uv run --locked mypy .`,
and `uv run --locked pytest`, all from that project directory. Database changes
also run Alembic upgrade/current and the project's PostgreSQL integration tests
against an isolated temporary PostgreSQL instance. M6 local checks use only the
fake provider. Sandbox and optional-provider observations are manual, sanitized,
non-CI evidence after access and explicit authority. Human review names reviewer,
date, Git reference, environment, wrong turns, help, recovery, next action, and
all nine 0–4 rubric scores.

### Definition of done

The CS revision is complete only when M0–M10, eleven milestones, five products,
seven files per milestone, README control, and GitHub-only delivery are unchanged;
the exact root six-column course table and tool ladder are consistent, with no
duplicate roadmap table in `CURRICULUM.md`; every revised block
uses the causal and visible learner grammar without lost substance; all listed
contradictions are closed; M6 has deterministic fake/refund/timeout/webhook/
reconciliation proof plus an honestly classified authorized sandbox result or an
explicit still-pending external item; optional endorsements stay optional; CI
needs no provider secrets; no completed learner solution or fabricated evidence
exists; validators, mutations, YAML, affected lint/format/type/tests, and relevant
PostgreSQL checks pass; named human evidence is separate and truthful; and TODO
checks only work whose observation, validation, and rollback condition are met.

Real provider calls, credential creation/use, external messages, hosted
deployment, publication, commit, push, and release remain outside this plan's
implementation authority and require separate explicit authorization.

### CS6 local closeout — 2026-09-14

No locally actionable CS0–CS6 item remains. The final local candidate preserves
exactly M0–M10, 11×7 milestone files, 58 top-level concept traces, the maturity
and five-product arc, Core/Stretch boundaries, README control, GitHub-only
delivery, and the learner-solution boundary.

For M9 specifically, local closeout means the SSE contract, lesson, and
acceptance requirements are present. The neutral starter intentionally omits the
SSE application and `projects/social/tests/m9/test_sse.py`; those remain learner-
built work and were not counted as supplied runtime evidence.

Validation evidence:

- curriculum validator: pass (`11` milestone directories, `7` files each,
  `58` concepts, relative links/anchors resolved), with its human-understanding
  limitation printed;
- controlled mutations: all `37` intended semantic failures rejected and the
  candidate restored green;
- YAML: all four issue forms and both workflows parsed with `yaml.safe_load`;
- locked project gates: Catalog `4 passed`; POS `2 passed, 1 skipped` without a
  database; Ecommerce `17 passed, 1 skipped`; Booking `3 passed, 1 skipped`;
  Social `4 passed, 1 skipped`; Ruff lint/format and mypy passed for all five;
- isolated PostgreSQL upgrade/current/integration: POS `3 passed`, Ecommerce
  `18 passed`, Booking `4 passed`, Social `5 passed`;
- intended red behavior: Catalog compatibility produced the expected public
  `name`→`title` mismatch and reset to four green tests; Booking's supplied lab
  observed two winners for one seat; Social's supplied lab observed 100 profile
  reads against the two-read budget. The latter two stay red by design because
  their fixes are learner work;
- M10 local rehearsal: migration preceded readiness, rollback/roll-forward
  command mechanics passed, isolated restore became ready, and the unhealthy
  candidate was rejected. The generated synthetic SQL/checksum, all task-created
  containers/volumes/networks, and the local image tag were removed afterward;
- `git diff --check`, secret/unsafe-fixture/generated-archive checks, and exact
  changed-file/status audit passed.

External limitations remain deliberately unchecked: M6 sandbox authority and
execution; all six optional endorsements (each currently NO-GO / do not add
yet); hosted GitHub rendering/Actions; named independent career-shifter reviews;
the prior optional real-target endorsement; and `HUMAN SELF-STUDY VERIFIED`.
Local maintenance review cannot satisfy any named-human item.

## Pareto post-closeout gap repair

This small follow-up closes the four discrepancies found when the plan and TODO
were compared with the implementation. It does not reopen CS0–CS6, broaden the
curriculum, add learner solutions, or authorize external work.

### Decisions

1. Fix the stale M9 support label so it names the FastAPI SSE reference that is
   actually linked.
2. Accept the implemented presentation rule: use explicit five-cue labels in
   the M0 baseline and difficult M6 payment pilot; use one compact cue legend
   plus the same ordered block facts elsewhere. Do not add repetitive bold
   labels merely for visual uniformity.
3. State that M9's SSE contract, lesson, and acceptance requirements are
   implemented while the SSE application and `tests/m9/test_sse.py` remain
   learner-built work.
4. After those wording repairs, obtain one independent fresh-context local
   maintenance review of M0 Block 1, M6 Block 1, one ordinary compressed block
   (M5 or M9), and the M5→M6 transition. This is structural/local evidence only
   and cannot satisfy named-human review.

### Order and validation

Execute PG1 → PG2 → PG3 → PG4 from the matching `TODO.md` section. Keep the
edits narrow: M9 challenge/closeout wording, the grammar decision record, and
one bounded review record. Then run:

```bash
python3 -B scripts/check_curriculum.py
python3 -B scripts/test_validator_mutations.py
git diff --check
```

The follow-up is complete when the stale label is gone, compact-versus-explicit
cue usage is intentional rather than accidental, M9 cannot be mistaken for a
supplied SSE solution, and the review evidence names its reviewer/context and
limitations. Provider, hosted GitHub, deployment, and named-human items remain
unchecked.

### Pareto follow-up closeout — 2026-09-14

PG1–PG4 are complete. The M9 hint names the linked FastAPI SSE reference; the
explicit-pilot/compact-controller cue rule is frozen; M9 states that its SSE
runtime and `tests/m9/test_sse.py` remain learner work; and an independent
fresh-context local review is recorded in `USABILITY.md`.

The first review correctly returned `REPAIR` for a contradictory M5→M6 recovery
route. The repaired route now uses an M6-specific post-M5 preflight, preserves
completed identity work, and distinguishes M5 regression from provider-fake
failure. The rerun returned `PASS`: M0 Block 1 96.25%, M6 Block 1 97.5%, M5
Block 1 92.5%, and M5→M6 93.75%, with no dimension below 3. This remains local
structural evidence, not named-human verification.
