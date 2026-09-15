# Subtraction cleanup: local maintenance evidence

This is maintainer evidence for the SC0–SC8 cleanup. It is not learner evidence,
hosted evidence, or a named-human usability result. The rollback source for every
slice is commit `8942980065c960aad833b1089a6e64035a7eec69`.

## SC0 baseline

- Candidate commit: `8942980065c960aad833b1089a6e64035a7eec69`.
- Initial dirty paths: only `PLAN.md` and `TODO.md`, both expected user planning
  changes. No unexplained path was present.
- Inventory: 235 tracked files; 13 root Markdown files excluding `AGENTS.md`;
  11 milestone directories with four files each; 15 root templates; 10 files
  under `docs/maintainers/`.
- Lines: 1,105 root Markdown lines excluding `AGENTS.md`; 4,250 milestone lines
  (1,779 README, 896 challenge, 669 acceptance, 906 reference).
- Structural baseline: `python3 scripts/check_curriculum.py` passed with 11×4
  milestones, 58 traced concepts, resolved links, and all five Python 3.13/Air
  runtimes. `python3 scripts/test_validator_mutations.py` rejected all 42
  controlled mutations and restored the candidate. `git diff --check` passed.

The runtime matrix is recorded below after each command has actually run.

## Canonical ownership and backlinks

| Concern | Canonical owner before cleanup | Active inbound route |
|---|---|---|
| Learner roadmap | `README.md` | Repository root and milestone breadcrumbs |
| Concept/maturity map | `CURRICULUM.md` | Root reference section and maintainer policy |
| Learner workflow | `CONTRIBUTING.md` | Root course loop and milestone ship blocks |
| Learner progress | `PROGRESS.md` | Root roadmap and milestone save/next blocks |
| Quality and evidence rules | `QUALITY-GATES.md` | Root reference and milestone proof blocks |
| Stack/tool policy | `STACK.md` | Root reference and milestone tool blocks |
| Learner terminology | `GLOSSARY.md` | Root introduction and first-use links |
| Learner experience | `USABILITY.md` | `docs/maintainers/README.md` |
| Milestone behavior | Each milestone `README.md`, with its support files | Root roadmap and adjacent milestone links |
| Project setup | Each `projects/<name>/README.md` | Owning milestone start block |
| Stable product/API/threat contracts | `projects/*/REQUIREMENTS.md`, `projects/*/specs/*.md`, and the isolated security fixture | Owning milestone build block |
| Evidence index | `templates/EVIDENCE-INDEX.md` | Root course loop and milestone proof blocks |
| Maintainer policy | `AGENTS.md` plus `docs/maintainers/README.md` | Root maintainer link |
| Active execution state | Root `PLAN.md` and `TODO.md` | `docs/maintainers/README.md` |

After consolidation, each milestone `README.md` becomes the sole learner
controller. Stable project contracts remain project-local because they define
consumer/API/data/threat behavior independently of lesson sequencing and often
serve more than one milestone. The compact curriculum manifest becomes the
machine-readable trace owner; reference prose remains explanatory rather than a
second learner route.

## Removal and move ledger

Rollback is always one named path or one listed slice, never a broad checkout or
reset. Inspect the source with `git show 8942980:<path>` and restore only that
path with `git restore --source=8942980 -- <path>`, then rerun the slice's last
green command.

| Source | Decision | Destination / retained meaning | Gate |
|---|---|---|---|
| `ANALYSIS.md`, `PERSONA-REVIEW.md` | DELETE | Active decisions already live in `PLAN.md`, `TODO.md`, `AGENTS.md`, and the usability contract | Backlinks and root traversal |
| `projects/README.md`, `challenges/README.md` | DELETE after merge | Direct project/milestone routes; challenge policy in maintainer guidance | All inbound links repaired |
| `docs/maintainers/business-first-career-shifter-review.md` and `docs/maintainers/archive/**` | DELETE | Historical recovery is the immutable anchor; current decisions remain in active docs | Provenance and active-decision audit |
| Every milestone `CHALLENGE.md`, `ACCEPTANCE.md`, `REFERENCE.md` | MERGE then DELETE | Same milestone `README.md`, preserving C/A IDs, Core/Stretch, commands, evidence, recovery, review, tools, and sources | Bidirectional trace and link checks |
| `templates/EVIDENCE-EXAMPLES.md` | MERGE then DELETE | `templates/EVIDENCE-INDEX.md` with synthetic labels | Consumer and link checks |
| `templates/ENTRY-DIAGNOSTIC.md` | KEEP | Direct M0 route; keeps D1–D5 runnable without lengthening the first screen | M0 traversal |
| `templates/INCIDENT-POSTMORTEM.md`, `templates/RUNBOOK-INCIDENT.md` | MERGE | `templates/INCIDENT.md` | Trigger/owner/command/stop/integrity/evidence audit |
| `templates/RUNBOOK-MIGRATION.md`, `templates/RUNBOOK-RELEASE-REJECTION.md`, `templates/RUNBOOK-RESTORE.md` | KEEP | Distinct executable operational workflows | Active M10 consumers |
| `templates/ADR.md`, `COMPLEXITY-REJECTION.md`, `DATA-LIFECYCLE.md`, `PORTFOLIO-CASE-STUDY.md`, `REQUIREMENTS.md` | KEEP | Distinct decision, lifecycle, portfolio, and requirement capabilities | Active consumers |
| `templates/SEMANTIC-AUDIT.md`, `templates/TRANSITION-REVIEW.md` | MOVE | `docs/maintainers/templates/` | Maintainer-only consumers and repaired links |
| `CURRICULUM.md` | MOVE | `docs/reference/curriculum-map.md` | Concept/maturity trace preserved |
| `STACK.md` | MOVE | `docs/reference/stack.md` | Tool boundaries preserved |
| `QUALITY-GATES.md` | MOVE | `docs/reference/quality.md` | Core/Stretch, failure, evidence, recovery preserved |
| `GLOSSARY.md` | MOVE | `docs/reference/glossary.md` | First-use links and fallback glossary preserved |
| `USABILITY.md` | MOVE | `docs/maintainers/usability.md` | Maintainer gate remains one hop from maintainer index |
| Root `PLAN.md`, `TODO.md` | KEEP | Root placement keeps active work discoverable to contributors; learner README links only through maintainer index | Final SC8 comparison |

## Project-contract decisions

All contracts are **KEEP project-local**:

- Catalog `M1-PRODUCT-BRIEF.md`: public HTTP/error/pagination/OpenAPI contract.
- POS `REQUIREMENTS.md` and M2/M3/M4/M10 specs: cumulative data, transaction,
  change, tenant, release, and recovery contracts used across M2–M4/M10.
- Ecommerce `REQUIREMENTS.md`, M5/M6/M7 specs, and
  `SECURITY-SCENARIOS.md`: stable identity/threat/provider/job contracts used
  across M5–M7; the fixture is isolated and non-callable.
- Booking `M8-BOOKING-CONTRACT.md`: stable lifecycle/API/race contract.
- Social `M9-FEED-CONTRACT.md`: stable workload/cache/realtime contract.

Inlining these would duplicate authority and make milestone controllers harder
to scan. Milestones link to the contract at the point where behavior is built.

## Source traversal record

Local source review uses the target learner profile but does not claim human
comprehension. For every M0–M10 controller, record the product, first command,
expected observation, recovery, and next milestone. A wrong turn is any required
hop through a support/maintainer page before the first action. The accepted
target is zero wrong turns and at most one project-setup hop.

### SC8 fresh-context maintainer review

This is a current-tree source review performed from learner-facing README files
with maintainer history set aside. It is not an independent or named-human
claim. Commands and results below are route targets: the controllers remain the
authority for exact execution and evidence.

| Milestone | Product | First command or command block | Expected starting result | Recovery | Next action |
|---|---|---|---|---|---|
| M0 | Catalog | `cd projects/catalog`, then the displayed locked baseline block | Six tests pass; health, sample JSON, and the Air page return 200 | Catalog setup guide, then the narrowest red command | Diagnose C1–C3; continue to M1 |
| M1 | Catalog | `PYTHONPATH=src uv run --locked pytest contracts/test_m1_contract.py -q` | Eight contract failures begin with intentionally missing 404 routes/OpenAPI paths | Catalog setup guide; reset only the active challenge | Implement one contract behavior; continue to M2 |
| M2 | POS | In `projects/pos/`, start the linked launch block with `cp .env.example .env` | Baseline migration is current; API and PostgreSQL smoke checks pass | Inspect Compose/PostgreSQL and `alembic current`; use only the bounded course reset | Model fixed queries; continue to M3 |
| M3 | POS | Re-run the linked POS launch block from `projects/pos/` | Reviewed M2 tests and migrations stay green | Inspect the first partial state and transaction owner; return to the reviewed M2 tag if needed | Make checkout atomic; continue to M4 |
| M4 | POS | Re-run the linked POS launch block from `projects/pos/` | Existing POS behavior is green before the cashier-name change | Run the narrow characterization test; return to the last green commit | Characterize the change; continue to M5 |
| M5 | Ecommerce | In `projects/ecommerce/`, start the linked launch block with `cp .env.example .env` | Anonymous shell and database checks pass; identity/order routes are intentionally absent | Inspect Compose/PostgreSQL; use only the bounded course reset | Build identity safely; continue to M6 |
| M6 | Ecommerce | `uv run --locked pytest tests/test_failure_harnesses.py -q` | Fifteen fake provider/webhook/worker harness tests pass, including explicit unknown outcomes | Rerun the in-memory fake and separate M5 failures from provider-boundary failures | Classify provider uncertainty; continue to M7 |
| M7 | Ecommerce | `uv run --locked pytest tests/test_failure_harnesses.py -q -k worker` | Two green harness tests expose duplicate effects in the crash window | Stop claims, inspect durable state, and use authorized replay; return to the last green migration | Preserve accepted intent; continue to M8 |
| M8 | Booking | In `projects/booking/`, start the linked launch block with `uv sync --locked` | Ordinary/database checks pass; the two-worker challenge fails with two confirmations | Rerun for fresh in-memory state or use the bounded booking database reset | Rebuild the invariant in PostgreSQL; continue to M9 |
| M9 | Social | In `projects/social/`, start the linked launch block with `uv sync --locked` | Functional/database checks pass; the query-budget challenge reports 100 profile reads | Reset the deterministic dataset; use query count/plan shape when timing is noisy | Repair the database feed; continue to M10 |
| M10 | Multi-tenant POS | Re-run the linked POS launch block from `projects/pos/` | Reviewed M4 tests and migrations stay green before tenant retrofit | Follow the versioned migration, release-rejection, incident, or restore runbook | Isolate the fixed customer; finish with portfolio review |

Review result: every root roadmap row reaches its controller in one click. Each
controller states the product, first action, expected observation, recovery,
and next action without requiring maintainer material. M0, M1, M6, and M7 carry
their first command directly; the other controllers use one project-setup hop.
Each milestone directory contains only its README controller. Stable project
contracts define behavior rather than lesson sequence, and the compact manifest
defines machine-readable trace ownership; neither is a competing learner
controller. Every retained learner template has a milestone consumer, and both
maintainer-only worksheets are consumed by the maintainer index.

Limitations: this review establishes local source navigability only. It does
not establish comprehension, hosted rendering, GitHub Actions behavior,
provider behavior, deployment, or a learner's completed milestone evidence.

## External limits

Provider sandbox work, optional provider/tool endorsements, real deployment,
hosted GitHub/Actions observation, and named-human career-shifter review remain
outside this local evidence and unchecked in `TODO.md`.

## SC1 local gate

The root learner route now presents prerequisites, the smallest Catalog run,
its expected six-test observation and recovery link, followed by the M0–M10
table and one course-loop explanation. PLAN and TODO remain one maintainer-index
hop away. Indirection pages, redundant directory summaries, and completed
history were removed only after their active challenge policy, decisions, and
rollback reference were retained. Commit `8942980` remains the path-level
recovery source. `python3 scripts/check_curriculum.py` and `git diff --check`
passed after the SC1 slice; root → M0 remained a direct route.

## SC2–SC4 controller and starter gates

All 33 milestone support bodies were merged into their owning README before the
source files were removed. Their C/A identifiers, `PROVIDED`/`YOU BUILD` modes,
steps, hints, reset commands, Core/Stretch split, evidence and recovery text,
review prompts, tool constraints, and sources remain in those controllers. The
58 concept rows retain their baseline identity and now resolve `M# Cx`/`M# Ax`
to the owning README. Stable contracts listed under Project-contract decisions
remain project-local; none was merged or deleted.

Source traversal found zero support-document prerequisites: root links directly
to each controller, each controller gives its first working directory/action,
and shared environment setup requires at most the linked project README. M0
starts with the six-test Catalog baseline and recovery; M1 with the intentionally
red HTTP/OpenAPI contract; M6 with the green fake/failure harness after M5; and
M9 with the deterministic feed/query-budget seam. No maintainer page is needed
for a learner action.

Starter repairs and observed results:

- Catalog removed `ProductDraft`, `ProductDraftForm`, both form routes, and the
  two passing form tests. Locked Ruff/format/mypy and six neutral tests passed;
  the M0 health fault failed, reset, and returned to six green tests. The M1
  contract remained intentionally red with eight missing-route/OpenAPI failures.
- Ecommerce removed login/order/payment/job placeholder routes, the supplied
  payment HTMX fragment, and its passing fragment test. Locked Ruff/format/mypy
  and 18 tests passed with one database skip; the provider/webhook/worker seams
  stayed green. The M5 contract remained intentionally red with four missing-
  route failures.
- Social removed `SSEResponse`, SSE/HTMX attributes, fragment/event routes, and
  the passing transport assertion. Locked Ruff/format/mypy and five tests passed
  with one database skip. The query-budget contract remained intentionally red
  at 100 profile reads versus the required maximum of two.
- POS removed `/app/checkout` and `/app/operator` plus their placeholder test;
  its stock observation stayed green. Locked Ruff/format/mypy and three tests
  passed with one database skip. Booking remained unchanged and passed locked
  Ruff/format/mypy with four tests and one database skip.

`python3 scripts/check_curriculum.py`, the representative mutation suite, and
`git diff --check` passed after the one-README rollout.

## SC5 template and reference gate

Synthetic examples now live in `templates/EVIDENCE-INDEX.md`. Incident response
and postmortem fields now share `templates/INCIDENT.md`, including trigger,
owners, stop condition, recovery, integrity, evidence, timeline, and follow-up
fields. Migration, release-rejection, and restore runbooks remain distinct.
ADR, complexity rejection, lifecycle, requirement-change, entry diagnostic, and
portfolio templates retain active milestone consumers. The semantic-audit and
transition-review worksheets moved under `docs/maintainers/templates/`.
Curriculum, stack, quality, and glossary references moved under
`docs/reference/`; usability moved beside the maintainer index. Link and anchor
validation and source traversal passed after all consumers were repaired.

## SC6 validator rule classification

| Class | Retained checks | Representative controlled failure |
|---|---|---|
| Semantic | M0–M10 order/maturity/outcome/project ownership, controller sections, C/A IDs and modes, all 58 concept mappings, stable product contracts, Core/Stretch, evidence/recovery, conditional-gate manifest | order, title, challenge, acceptance, Core/Stretch, competing controller |
| Safety | likely secrets, callable vulnerable fixtures, generated archives, external evidence left unchecked, pinned Actions | vulnerable route, external checkbox, archive, unpinned action |
| Runtime | Python/Air lock, shared Air/FastAPI composition, OpenAPI exclusion, health/API regression seam, no internal HTTP, no Node/custom JavaScript, no completed/premature starter behavior | runtime, lock, composition, router, internal HTTP, second runtime, Catalog/Ecommerce/Social solution |
| Navigation | ordered root roadmap, one controller, first command/observation/recovery, relative links and anchors | broken anchor |
| Presentation-only | no exact lesson sentences retained; only semantic headings and the learner-visible first-action contract remain | harmless prose mutation passes |
| History-only | completed-plan strings, historical layouts/classifiers, and 44-row provenance coupling removed | none; rollback is immutable commit `8942980` |

The compact `docs/maintainers/curriculum.json` owns order, outcomes, maturity,
project ownership, challenge/Core IDs, and conditional gates without copying
lesson prose. `docs/reference/curriculum-map.md` owns the 58 introduction,
practice, and proof rows. The reduced suite rejects one mutation for every
durable failure class, accepts a harmless prose edit, and passes again after
restoration.

## SC7 full local gate — 2026-09-15

All results below are local maintainer evidence. No provider, credential,
hosted GitHub, deployment, or named-human gate was attempted or inferred.

### Structure and safety

- `python3 scripts/check_curriculum.py` passed: 11 one-README milestones, 58
  concept traces, semantic manifest, links/anchors, safety, no-solution, and
  five Air/FastAPI runtime boundaries.
- `python3 scripts/test_validator_mutations.py` passed all 21 representative
  cases: 20 durable failure classes were rejected, the harmless prose mutation
  was accepted, and every candidate was restored.
- `python3 -m json.tool docs/maintainers/curriculum.json` passed. An installed
  PyYAML `yaml.safe_load` traversal parsed all 12 YAML files: four issue forms,
  two workflows, four development Compose files, and the two M10 Compose files.
- Independent current-tree scans found zero likely GitHub/OpenAI token shapes,
  zero generated archives outside `dist/`, zero callable vulnerable-route
  markers, and confirmed the ecommerce security fixture is documentation-only.
- `git status --short`, `git diff --name-status`, and `git diff --stat` matched
  the SC1–SC6 removal/move ledger plus the SC7 files named below. `git diff
  --check` passed.

### Locked project and runtime matrix

For each of `catalog`, `pos`, `ecommerce`, `booking`, and `social`, the following
ran from `projects/<name>/` and passed: `uv sync --locked`, `uv run --locked
ruff check .`, `uv run --locked ruff format --check .`, `uv run --locked mypy`,
and `uv run --locked pytest`. Ordinary results were Catalog 6 passed; POS 3
passed/1 PostgreSQL skip; Ecommerce 18 passed/1 PostgreSQL skip; Booking 4
passed/1 PostgreSQL skip; Social 5 passed/1 PostgreSQL skip. The skips were the
documented opt-in database seams, rerun below with explicit course URLs.

A bounded production-mode live run used ports 8100–8104 and checked `/`,
`/health`, `/openapi.json`, every database-backed `/ready`, Catalog
`/products/sample`, POS `/app/stock`, and Booking `/app/bookings`. Every named
route returned 200 with the expected HTML/JSON content type. Air `/app/` routes
were absent from OpenAPI. Ecommerce login/registration/payment/job routes and
Social fragment/event routes returned 404 as intended. The server processes
were stopped by the command trap.

### Product-specific gates

- **Catalog:** `python3 scripts/challenge.py activate health` followed by `uv
  run --locked pytest` produced 1 intended failure and 5 passes. `python3
  scripts/challenge.py reset` restored the source hash and six green tests.
  `PYTHONPATH=src uv run --locked pytest contracts/test_m1_contract.py -q`
  remained intentionally red with 8 failures beginning at missing 404 routes
  and missing OpenAPI paths.
- **POS:** `docker compose config -q`, `docker compose up -d --wait`, `uv run
  --locked alembic upgrade head`, and `uv run --locked alembic current` passed
  at `0001_baseline (head)`. With `POS_TEST_DATABASE_URL` set to the documented
  port 5432 URL, `pytest tests/test_postgres.py -q` passed. `docker build -t
  vibecamp-pos-sc7:local projects/pos` passed from the repository root. Both M10
  Compose combinations parsed with synthetic required variables. With that
  local image, `IMAGE_REF=vibecamp-pos-sc7:local
  PREVIOUS_IMAGE_REF=vibecamp-pos-sc7:local sh
  projects/pos/scripts/rehearse_m10.sh` passed migration-before-readiness,
  rollback/roll-forward command mechanics, isolated dump/restore/readiness, and
  unhealthy-candidate rejection. Reusing one image verifies mechanics only,
  not cross-version compatibility.
- **Ecommerce:** Compose health, migration/current, and the explicit port 5433
  PostgreSQL test passed. `pytest tests/test_failure_harnesses.py -q` passed 15
  provider timeout/outcome/refund, signed duplicate/delayed/tampered webhook,
  retry-budget, and worker crash/replay cases. `python scripts/replay_jobs.py
  --actor sc7-local --reason synthetic-rehearsal --message-id synthetic-1`
  returned a non-mutating preview. The M5 contract stayed intentionally red
  with 2 missing-behavior failures, while the neutral shell tests confirmed no
  restored M6 HTMX/payment/job solution.
- **Booking:** Compose health, migration/current, and the explicit port 5434
  two-independent-connection test passed. `PYTHONPATH=src uv run --locked pytest
  challenges/test_double_booking.py -q` failed deterministically with 2
  confirmations for 1 seat. Rerunning `pytest tests/test_single_request.py -q`
  reset fresh in-memory inventory and passed both neutral checks.
- **Social:** Compose health, migration/current, and the explicit port 5435
  query-capture/`EXPLAIN SELECT 1` test passed. `PYTHONPATH=src uv run --locked
  python scripts/seed_reference.py` printed the fixed 100/70/9 workload.
  `PYTHONPATH=src uv run --locked pytest challenges/test_query_budget.py -q`
  failed intentionally at 100 profile reads versus at most 2; the three neutral
  feed tests then passed. Live/source checks confirmed no supplied SSE/HTMX
  completion.

All four course Compose stacks were brought down with their task-created named
volumes. The three M10 projects were also down with volumes, the local POS image
was removed, and the synthetic SQL/checksum and temporary logs were removed.
Post-cleanup container, volume, image, and artifact scans were empty.

### Source traversal and repair

The local source traversal checked these direct chains: root→M0→Catalog→M1,
root→M1→Catalog→M2, root→M2/M3/M4→POS→next milestone, root→M5/M6/M7→Ecommerce
→next milestone, root→M8→Booking→M9, root→M9→Social→M10, and
root→M10→POS→portfolio review. Every controller states the product objective,
first action, expected observation, recovery, and next action. There were zero
required wrong turns, at most one project-setup hop, no observed undefined term
blocking the first action, and no competing canonical controller.

One observed stale count was repaired: M1 said to reconfirm eight M0 tests after
the Catalog no-solution cleanup reduced the neutral suite to six. The line now
agrees with the root, Catalog README, M0 controller, example evidence, and live
six-test result. The narrow count scan, all-transition traversal, curriculum
validator, mutation suite, Catalog tests, and `git diff --check` passed after
the repair.

## SC8 local closeout — 2026-09-15

Language and route review removed the retired milestone-shape rule, deleted-file
quality links, stale M0 form names, transitional curriculum wording, and the
superseded 11×4/form/HTMX/SSE usability chronology. The fresh-context table
above records all eleven product routes. PLAN and TODO remain at root because
that is clearer for contributors and does not add a learner-facing choice.

Fresh runs passed the curriculum validator, all 21 mutation cases, JSON and 12
YAML parses, link/anchor and safety scans, `git diff --check`, and locked sync,
Ruff, format, mypy, and ordinary tests for all five projects: Catalog 6; POS 3
plus 1 database skip; Ecommerce 18 plus 1 database skip; Booking 4 plus 1
database skip; Social 5 plus 1 database skip. A broad collection check
also reconfirmed the intended boundaries: Catalog M1 had 8 failures, Ecommerce
M5 had 4, Booking's final-seat race had 1, and Social's query budget had 1.

The immediately preceding SC7 PostgreSQL, migration, live HTTP/OpenAPI,
container-build, M10 rehearsal, deliberate-red/reset, and cleanup results above
remain exact and were not duplicated because SC8 changed documentation only.
SC-G1–SC-G4 remained satisfied through final status, diff, rollback-ledger, and
external-checkbox review. Provider, hosted, deployment, credential, and
named-human evidence remains outside this local closeout.

A delayed SC0 audit report surfaced one narrow defect after closeout: the
Catalog `type` challenge still searched `app.py` for the sample price after that
literal had moved to `service.py`. The activator path was corrected, activation
then produced the intended mypy `str`-versus-`Decimal` error, reset removed the
challenge state, and the seven-file mypy check plus all six neutral tests
returned green.

The same audit identified two M5 false positives: a missing login route made
both enumeration responses equal, while a missing order route returned an
allowed 404. Each security-contract case now first verifies that its owned
route and method exist. The neutral suite remains green and the untouched
starter now fails all four M5 cases for missing routes, so absence can no longer
masquerade as secure behavior.
