# Learner-experience and language rubric

This is a maintainer quality gate, not required learner reading. It protects the
course from becoming harder to operate than the engineering problems it teaches.

## Target learner

Evaluate the Core path as a person studying alone with basic Python syntax and
basic Git use, but little production-engineering vocabulary or workflow
experience. Prior experience may shorten practice; it never lowers a Core gate.

## Scoring

Score every dimension from 0 to 4:

- **0 — Blocked:** an essential artifact or instruction is absent.
- **1 — High friction:** help from the course author is likely.
- **2 — Interpretive:** self-service requires substantial guessing or research.
- **3 — Mostly self-service:** minor friction, but no intervention is necessary.
- **4 — Immediate:** the next action, result, and recovery path are unambiguous.

Multiply the 0–4 score by one quarter of the weight. Release requires at least
**85/100 overall and no dimension below 3**.

| Dimension | Weight | A score of 4 means |
|---|---:|---|
| Audience and outcome clarity | 10 | The first screen states audience, prerequisites, product path, and outcome |
| Time to first successful run | 15 | With prerequisites installed, a clean clone reaches a working API and green test within 15 minutes |
| Executable instructions | 20 | Active commands are literal and copyable, with expected output and recovery; no placeholders remain |
| Language and terminology | 15 | The plain-language problem precedes the term; necessary terms and acronyms are defined before use |
| Progressive disclosure/navigation | 10 | One next action is obvious; reference and maintainer material are secondary |
| Guided scaffolding | 10 | The starting state is supplied while engineering decisions remain learner work |
| Automated feedback and recovery | 10 | Local and GitHub checks identify the failed gate and route to useful recovery guidance |
| Failure-lab reproducibility | 5 | Safe activation/reset is deterministic and does not reveal the diagnosis before the attempt |
| Pause and resume | 5 | `PROGRESS.md` reveals the next action and evidence gap in under two minutes |

## Language contract

1. Describe the concrete problem before naming the concept or pattern.
2. Define a necessary term at first use and link [the glossary](GLOSSARY.md).
3. Expand an acronym before using it alone.
4. Write instructions as **action → reason → expected observation → recovery**.
5. Keep one primary requirement per learner checklist item.
6. Use one term consistently unless a distinction is explicitly taught.
7. Show a small example before an abstract rule where practical.
8. Explain course labels (`M0`, `C1`, `A1`, Core, Stretch, levels, evidence, and
   cold review) before using them as instructions.
9. Prefer short sentences and concrete verbs, but do not mechanically grade
   sentence length or remove precise professional vocabulary.

## Cold-test worksheet

Copy this table into curriculum-maintenance evidence. Do not pre-fill a pass.

| Observation | Result |
|---|---|
| Environment and reference commit | |
| Time to locate first command | |
| Time to green tests and working API | |
| Wrong turns or backtracking | |
| Undefined or confusing terms | |
| Help requested from a person | |
| Commands that failed | |
| Recovery guidance used successfully | |
| Next action stated correctly | |
| Rubric dimensions and weighted score | |

Use a clean clone and only public learner instructions. Prefer one real
career-shifter who did not author the material. A fresh-context automated review
may supplement but must not be the sole release evidence. Record actual timing;
the 15-minute target is a usability check, not a promise for every machine.

Use [the transition review template](templates/TRANSITION-REVIEW.md) separately
for repository→M0, M0→M1, M1→M2, M4→M5, M7→M8, M8→M9, and M9→M10. One passing
transition never releases a different application transition.

## 2026-09-13 baseline

Baseline: **32/100**. The required pre-M0 route exposed about 3,770 words; the
repository contained 77 milestone files but no learner application; the entry
diagnostic referenced a missing starter and placeholder commands; CI checked
curriculum structure only. Re-score after the runnable M0 path is cold-tested.

## 2026-09-13 M0 post-revision check

The runnable learner path was tested from an isolated copy of the repository,
excluding the author's virtual environment, caches, local `.env`, and Git
metadata. The copy used Linux, Python 3.12.12, and uv 0.9.21.

| Observation | Result |
|---|---|
| Words before first command | 137 |
| Time to locate first command | Immediate; it is under README “Start now” |
| Time from sync to green checks and live API | 6 seconds with a warm dependency cache |
| Wrong turns or backtracking | One normal connection retry while the server started |
| Undefined or confusing M0 terms | None found by the structured pass; ASGI is defined in the glossary |
| Help requested from a person | None during the scripted pass |
| Commands that failed | Only the four deliberately activated challenge checks |
| Recovery | All four reset commands restored Ruff, formatting, mypy, and four tests to green |
| Live behavior | `/health` and `/products/sample` returned the documented JSON |
| Next action | M0's numbered lesson was visible immediately after the quickstart |

Second-audit rubric result: **86.25/100**. The executable M0 path clears the
numeric threshold, but repository ownership and GitHub feedback remain P0
findings before the complete M0 workflow is considered independently operable.

| Dimension | Score | Weighted result | Reason |
|---|---:|---:|---|
| Audience and outcome clarity | 3 | 7.5 | Audience and outcome are clear; learner repository ownership is not yet defined |
| Time to first successful run | 4 | 15 | Isolated smoke test was well below 15 minutes |
| Executable instructions | 4 | 20 | Active M0 commands are literal and placeholder-free |
| Language and terminology | 3 | 11.25 | M0/M1 are guided and glossary-backed; later milestone prose still requires rollout checks |
| Progressive disclosure/navigation | 3 | 7.5 | Root and M0 have one route; later product transitions are specified but not yet runnable |
| Guided scaffolding | 4 | 10 | M0 supplies a shallow starter without supplying the learner's solution |
| Automated feedback and recovery | 2 | 5 | Local checks pass, but the learner push model and published workflow execution remain unproven |
| Failure-lab reproducibility | 4 | 5 | All four activation/status/reset cycles were deterministic and repeatable |
| Pause and resume | 4 | 5 | The progress dashboard names the exact first action and evidence gaps |

This clears the overall M0 score but not the no-sub-3 release rule. It is not a
human usability claim: repository ownership must be fixed, a career-shifter
cold review remains valuable when a reviewer is available, and later application
transitions must be scored separately before their starters are described as
self-service.

## 2026-09-13 whole-course scope correction

The M0 result above must not be reported as the score for the complete course.
A second audit followed the transition from M0 into later milestones and scored
the whole-course experience **52.5/100**. Only `projects/catalog/` exists; M1–M10
READMEs contain no executable command blocks; M2–M10 READMEs are short
specifications rather than ordered lessons; M1–M10 resource files have no
curated links; and many later professional terms are not introduced through
plain-language examples.

| Dimension | Whole-course score | Weighted result | Primary reason |
|---|---:|---:|---|
| Audience and outcome clarity | 3 | 7.5/10 | The promise is clear; later prerequisites and repository ownership are not |
| Time to first successful run | 2 | 7.5/15 | M0 is fast, but later application starting states do not exist |
| Executable instructions | 2 | 10/20 | Exact M0 commands give way to broad implementation briefs |
| Language and terminology | 2 | 7.5/15 | M0 is introduced carefully; later documents compress several undefined terms |
| Progressive disclosure/navigation | 2 | 5/10 | M0 routes well; later READMEs do not control the seven-file journey |
| Guided scaffolding | 1 | 2.5/10 | Only the catalog has a supplied runnable checkpoint |
| Automated feedback and recovery | 2 | 5/10 | CI and recovery are executable for M0 only |
| Failure-lab reproducibility | 2 | 2.5/5 | M0 faults are deterministic; later faults are briefs without fixtures |
| Pause and resume | 4 | 5/5 | The progress dashboard retains a clear current action |

The detailed remediation sequence is in [PLAN.md](PLAN.md). Re-score every
application transition independently; one strong entry milestone cannot release
the entire curriculum.

## Readiness status vocabulary

- **STRUCTURALLY READY:** the repository shape, links, identifiers, and concept
  traces pass automated checks.
- **STARTER VERIFIED:** the named supplied starter and its documented reset were
  executed in the stated environment.
- **HUMAN SELF-STUDY VERIFIED:** a named target learner completed the stated
  transition without author intervention; the evidence records date, Git
  reference, environment, wrong turns, and help requested.

These statuses are independent and always name their scope. An automated review
cannot establish human self-study verification.

Current status after repository implementation (based on `d259148` plus the
uncommitted candidate changes, 2026-09-13):

- STRUCTURALLY READY: yes for the 11×7 structure, 58 concept traces, links,
  anchors, scenario modes, vocabulary, workflows, and semantic mutation checks.
- STARTER VERIFIED: yes locally for catalog, POS, ecommerce, booking, and social;
  all passed clean-copy checks, and all four database starters passed PostgreSQL
  migration/integration checks. M10's image also ran in two isolated local
  Compose projects. Hosted Actions are not yet observed.
- HUMAN SELF-STUDY VERIFIED: no.

Use [the semantic audit](templates/SEMANTIC-AUDIT.md) to trace each requirement
through challenge, acceptance, command, expected observation, and evidence.

## 2026-09-13 provisional maintenance simulation

This is a fresh-context automated/documentation simulation, not a human
career-shifter review. It checked the public learner route, exact commands,
starting artifacts, expected failures, recovery paths, terminology, and next
action. Runnable starters were executed separately; learner-built milestone
solutions and real GitHub-hosted Actions were not fabricated.

The automated/documentation simulation estimated **88.75/100**, with no
dimension below 3. This is provisional design feedback, not a human score and
not a whole-course release claim.

| Dimension | Score | Weighted result | Evidence |
|---|---:|---:|---|
| Audience and outcome clarity | 4 | 10/10 | Root states prerequisites, five-product path, and capability outcome |
| Time to first successful run | 3 | 11.25/15 | M0 is immediate; PostgreSQL startup and dependency download vary by machine |
| Executable instructions | 3 | 15/20 | All supplied starters are literal; later work necessarily uses learner-created tags and deployment target |
| Language and terminology | 4 | 15/15 | Every milestone owns local terms, acronyms are expanded, and the glossary is a fallback |
| Progressive disclosure/navigation | 4 | 10/10 | Root routes to M0; each milestone README routes to support only when needed |
| Guided scaffolding | 4 | 10/10 | Five bounded launch kits expose the problem without supplying milestone solutions |
| Automated feedback and recovery | 3 | 7.5/10 | Local suites and workflow definitions align; hosted Actions remain unobserved until publication |
| Failure-lab reproducibility | 4 | 5/5 | M0, M1 contract, booking race, social budget, and ecommerce uncertainty have deterministic signals |
| Pause and resume | 4 | 5/5 | `PROGRESS.md` and milestone Next sections expose the continuation |

Transition scores use [the reusable scorecard](templates/TRANSITION-REVIEW.md).
The values below are maintenance simulations; replace or supplement them with
named human observations when a reviewer is available.

| Transition | Score | Lowest dimension | Outcome / remaining limitation |
|---|---:|---:|---|
| Repository → M0 | 92.5 | 3 | Runnable; learner must create a repository they control before pushing |
| M0 → M1 | 91.25 | 3 | Contract begins with eight intentional 404 failures; the learner implements it |
| M1 → M2 | 90 | 3 | POS kit reaches healthy PostgreSQL and empty Alembic baseline |
| M2 → M3 | 87.5 | 3 | Continues from the learner's reviewed M2 tag; no synthetic product snapshot |
| M3 → M4 | 87.5 | 3 | Brownfield change starts from the learner's reviewed M3 tag |
| M4 → M5 | 90 | 3 | Anonymous ecommerce shell and disabled attack briefs are runnable |
| M5 → M6 | 87.5 | 3 | Provider uncertainty double is supplied; integration repair remains learner work |
| M6 → M7 | 87.5 | 3 | Kill-point state model is supplied; durable outbox remains learner work |
| M7 → M8 | 90 | 3 | Two-worker final-seat failure is deterministic and isolated |
| M8 → M9 | 90 | 3 | Skewed 100-post N+1 budget failure is deterministic |
| M9 → M10 | 86.25 | 3 | Capstone is staged from reviewed POS; real target and recovery evidence must be learner-owned |

Release interpretation: the repository is structurally promising, but it is
not yet HUMAN SELF-STUDY VERIFIED. Hosted GitHub Actions and human
career-shifter transition reviews remain external evidence requirements.

## Resource maintenance

Review external links and named major versions at least every six months and
before a curriculum release. Prefer the authoritative standard or project
documentation. Link checking is a maintainer review: the dependency-free local
validator intentionally does not require network access or block a learner who
is working offline.

At the same cadence, review pinned GitHub Action commits and container digests
against the publisher's release, changelog, and security notices. Update the
human-readable version comment and immutable commit together, then run the
controlled action-pin mutation test. An automated update proposal does not
replace maintainer review.


## 2026-09-13 IA pilot and rollout evidence

Reviewer/mode: Codex main agent, **solo fresh-context maintenance simulation**,
using an isolated copy of `d259148` plus the dirty candidate, Linux, Python 3.12,
uv 0.9.21. Implementation notes were set aside for the learner-document pass;
the same agent authored the edits, so this is not independent human review.
No hosted GitHub rendering, issue submission, Actions, learner release/tag, or
real target was exercised. QUALITY-GATES permits this isolated-copy maintenance
method; it does not permit upgrading it into a learner/human release claim.

### Pilot observations and decision

- Repository→M0: Start now still precedes the route map. The map has eleven
  ordered rows; M0 is Milestone 1 of 11, M5 is Milestone 6 of 11. M0 outputs
  are baseline transcript, failure diagnosis/reset, and CI-backed gate PR/tag.
  A0 diagnostic remains Core in addition to A1–A3. Repository support does not
  mark any learner gate passed.
- Bounded block: predict four green catalog tests and two HTTP 200 responses.
  In the isolated copy, locked sync, Ruff lint/format, mypy and pytest passed;
  sync through tests took 3.137 seconds with warm dependency downloads and no
  copied virtual environment. `/health` returned `status=ok`; sample product
  returned VC-001, Mechanical Keyboard, price 19.99. An ephemeral local port
  used the documented port-substitution fallback; server was stopped afterward.
- Failure: predicted the health assertion would reject `warning`. Activation
  succeeded; the selected test exited 1 for `warning != ok`; reset succeeded;
  all four tests passed; challenge status was inactive. No repair solution was
  supplied. This samples C1 and A1, not every learner gate.
- Review answer (M0 question 7): `/health` proves the process answers; no M0
  database/external dependency exists to establish dependency readiness.
- Pause/resume: source-only rehearsal recorded C1/A1, missing diagnosis text,
  M0 Block 4 anchor, project directory, health-test command, and last-green
  candidate reference in a scratch dashboard. Reopening only that dashboard
  identified Block 4 and its return-to-green route; footer reaches M1 in one
  link. The real learner dashboard was not marked complete.
- M0→M1: M1 starts from the learner-reviewed M0 tag, uses the same catalog,
  and exposes intentional missing-route contract failures. The supplied
  contract exited 1 with eight expected failures; no product solution exists.
- Navigation observations: no unresolved local links, no backtracking needed
  in this source traversal after repair. Human wrong-turn counts and human
  two-minute orientation/resume latency are **unmeasured**, not assumed zero.
  Source lookup and fast command execution do not prove human comprehension.
- Optional help is after local hints/recovery; its form requests command,
  expected/actual observation, hypothesis, redacted output and last-green ref.
  Hosting and human response are untested; Core remains identical.

| Dimension | Weight | Local simulation score | Weighted result | Evidence / limit |
|---|---:|---:|---:|---|
| Audience and outcome clarity | 10 | 4 | 10 | Eleven products/capabilities and M0 outputs visible |
| Time to first successful run | 15 | 3 | 11.25 | Warm-cache local timing; cold download/human time unknown |
| Executable instructions | 20 | 3 | 15 | Supplied commands pass; owned URL and learner gate remain personal |
| Language and terminology | 15 | 4 | 15 | Why precedes terms; label and ordinal explicitly differ |
| Progressive disclosure/navigation | 10 | 4 | 10 | Start first, exact support, boundary footer |
| Guided scaffolding | 10 | 4 | 10 | Same starter and contracts, no completed solution |
| Automated feedback and recovery | 10 | 3 | 7.5 | Health fault/reset executed; hosted feedback pending |
| Failure-lab reproducibility | 5 | 4 | 5 | Selected C1 failure/reset reproduced |
| Pause and resume | 5 | 4 | 5 | Exact block and checkpoint recoverable in source rehearsal |
| Total | 100 | | 88.75 | Provisional maintenance assessment only |

Decision: **ROLL OUT** the local IA grammar (88.75/100, minimum 3); no new
source-navigation blocker after pilot repair. This authorizes only the planned
controller batches. It does not release the curriculum as HUMAN SELF-STUDY
VERIFIED. Signature preview: **REJECT** another root example; existing synthetic
examples already provide that route. Raw local transcripts are summarized in
[maintenance provenance](docs/maintainers/archive/2026-09-13-remediation/README.md).
Rollback: reverse only pilot IA hunks if a later transition introduces friction;
retain failed observations and all pre-existing work.


### IA3 early batch M1 to M2

Local source review after pilot: M1 is 2 of 11 and continues reviewed M0 catalog;
M2 is 3 of 11 and starts the separate POS launch kit. First M1 output is a
request matrix, then the intentionally red contract. First M2 output is schema
and constraint proof against PostgreSQL. M2 setup and recovery remain local to
POS; Docker begins here. Exact C links and command rows identify support and
resume without guessing a test path. Product brief precedes work; no fenced
command changed. Same provisional score vector as pilot: 4,3,3,4,4,4,3,4,4
= 88.75, minimum 3. PASS for source navigation, no new unresolved route or
backtracking in the walk. Human elapsed time and comprehension remain unmeasured;
no completed M1/M2 application or learner tag was fabricated.


### IA3 product and security batch M4 to M5

Reviewed source route: M4 remains POS, uses the reviewed M3 state, preserves
cashier-name/refactor and portfolio proof; M5 starts the anonymous ecommerce
shell, never copies POS business logic. M5 is explicitly Milestone 6 of 11.
Identity output maps to C1/A1; role/object matrix to C2/C3 and A2/A3; order-state
regression to C4/A4, with threat/lifecycle gates retained. Review caught concept
links landing on unrelated access/password examples; repaired each to the actual
block topic before acceptance. All links pass; original commands and gate ranges
are retained. Source PASS after repair, vector 4,3,3,4,4,4,3,4,4 = 88.75,
minimum 3. Timing/comprehension still unmeasured for humans; no authored security
solution or named learner result is implied.


### IA3 durable work to booking to social batch

M7 remains ecommerce durable intent and learner worker tests; its footer starts
M8's separate booking kit (9 of 11), not a worker-code copy. M8's initial race
is intentionally red; the ordinary PostgreSQL seam is green and uses independent
connections. C2 points to database enforcement, C3 to time/deadlock policy.
M9 starts the social kit (10 of 11): initial 100-profile-read failure is expected,
then database correctness precedes the required Redis experiment. Retention is
optional; Core SSE and Stretch WebSockets remain distinct. M9 hands off to M10
which resumes reviewed M4 POS, not social code. Exact commands, expected rows,
evidence, next/resume and support routes are retained. Source PASS on M7→M8,
M8→M9 and M9 handoff: each provisional vector 4,3,3,4,4,4,3,4,4 = 88.75,
minimum 3. No new unresolved route/backtracking; no human timing or learner-built
race/feed/worker pass is claimed.


### IA5 and CU5 final transition review

After the last controller batch, anchor repair, and cleanup, repeated the seven
named source traversals using only learner documents. Same reviewer/mode and
independence limits as the pilot; this is a solo maintenance simulation, not a
named career-shifter study or hosted-rendering observation. All rows use the
pilot's explicitly provisional dimension vector 4,3,3,4,4,4,3,4,4: 88.75/100,
minimum 3. Scores reflect document affordances and supplied-command evidence,
not measured understanding. No human navigation time is available.

| Transition | Next action and checkpoint | Exact support / artifact / gate | Source verdict |
|---|---|---|---|
| Repository→M0 | Owned clone, catalog baseline, M0 Block 1 (1 of 11) | Tool/check explanation; baseline transcript; A0 plus A1–A3 | PASS; start remains above map |
| M0→M1 | Reviewed M0 catalog; Block 1 request matrix (2 of 11) | Client-response concept; request matrix; A1–A4 | PASS; eight initial contract failures expected |
| M1→M2 | New POS shell and PostgreSQL; Block 1 schema (3 of 11) | C1 model-from-behavior; schema/migration evidence; A1–A5 | PASS; new product explicit |
| M4→M5 | New anonymous ecommerce shell; identity Block 1 (6 of 11) | C1 identity and password concept; identity/matrix evidence; A1–A6 | PASS; cookie Core/JWT Stretch intact |
| M7→M8 | Booking baseline then sequential learner path (9 of 11) | C1 final-seat race; baseline/interleaving evidence; A1–A4 | PASS; toy failure distinct from real DB seam |
| M8→M9 | Social baseline then database feed (10 of 11) | C1 slow feed; equal-workload evidence; A1–A4 | PASS; Redis experiment required, retention optional |
| M9→M10 | Return to reviewed M4 POS, isolation Block 1 (11 of 11) | C2 tenant attack; isolation/release/handoff evidence; A1–A7 | PASS; local Core and optional real target separate |

Each controller's pause cue points back to its exact block; the dashboard keeps
C/A ID, evidence gap, next block/command, and last-green reference. Recovery
precedes optional help, and previous/home/next forms one eleven-stop chain.
No new unresolved destination or backtracking was found in the source pass.
Baseline lacked explicit ordinal/trust/previous cues; those now require no
reference search. This supports local grammar acceptance only. Human times,
wrong turns, comprehension, and hosted layout must still be observed externally.

M3/M6/M10 final batch also preserves POS transaction ownership, ecommerce
uncertainty, the M4 POS return, and M10 local rehearsal/endorsement distinction.
All original fenced commands and literal command rows match the pre-task
candidate. All 66 supporting milestone files and every starter code/spec/test/
lockfile remain byte-identical. No learner application solution was added.

### Local verification and cleanup result

Executed on 2026-09-13, Linux/Python 3.12 and uv 0.9.21 with installed locked
dependencies and offline resolution. A separate task-owned PostgreSQL 17 Alpine
container used an ephemeral localhost port and tmpfs storage; four fresh
synthetic databases isolated the tests from existing course data.

| Project | Lint / format / strict types | Ordinary tests with database where applicable | Additional observation |
|---|---|---:|---|
| Catalog | PASS | 4 passed | M1 contract collects 8; isolated pilot observed initial failures |
| POS | PASS | 3 passed | Alembic upgrade/current reached 0001_baseline head |
| Ecommerce | PASS | 16 passed | Alembic head; 4 security contracts collected, not misreported as implemented |
| Booking | PASS | 4 passed | Alembic head; independent backend IDs; intended two-confirmation race failure |
| Social | PASS | 5 passed | Alembic head; 100-post seed; intended 100-read budget failure |

Total: 32 ordinary tests passed with no PostgreSQL skips. All five locked syncs
passed. PyYAML BaseLoader parsed all six GitHub YAML files, including event/job
maps; YAML parsing does not observe hosted execution. Curriculum validation,
all controlled mutations, relative anchors, and `git diff --check` pass.
No dependency/security advisory refresh was attempted: offline checks and the
existing secret/unsafe-fixture scan do not claim current vulnerability clearance.
M10 executable files did not change; its earlier local rehearsal evidence is
retained, not downgraded or represented as a new run.

The temporary database cleanup initially checked Docker's asynchronous auto-remove
too early and raised an assertion after all tests passed. A follow-up container
inventory confirmed it disappeared; no pre-existing container, volume, or database
was altered. This was a harness cleanup timing issue, not a failed project test.

38 manifested ignored caches were removed (83,279,329 pre-removal logical bytes);
37 regenerated under normal checks, while the unused root Ruff cache stayed
absent. Five `.venv` directories and empty `dist/` remain. The negated ignore rule
keeps `.env.example` visible; source and synthetic evidence are visible, while
cache/environment/database/log/build patterns are ignored. No ignore change was
needed. All 149 pre-existing active untracked files and all 103 tracked paths
remain present. No historical file moved or was removed; KEEP decisions preserve
public paths, unique template obligations and workflow gates.

Local IA and cleanup are complete to the authorized maintenance scope.
**HUMAN SELF-STUDY VERIFIED remains no**; hosted rendering/Actions, named human
transition reviews, and optional learner-authorized real-target endorsement
remain external. The external checklist has not been checked by simulation.

Final resume gap repair: controller and dashboard cues explicitly preserve existing
`.env` and evidence and distinguish validation from first-install copying or
destructive resets. Original command blocks remain unchanged. This prevents a
resume route from overwriting learner configuration.

## 2026-09-14 CS3 compression pilot maintenance review

Scope: M0 Block 1 and M6 Block 1 in the uncommitted CS candidate. Reviewer:
internal fresh-context maintenance review (not a named human learner). Environment:
Linux, local source rendering, Python 3.12 project environments; hosted GitHub
rendering and provider access were not used. The reviewer put implementation
notes aside, followed only the controller/support routes, predicted the green
M0 baseline and M6 timeout/refund facts, ran the supplied Catalog and Ecommerce
checks, and returned to each saved block anchor.

Both blocks exposed the concrete problem before terminology and made Do,
Understand, Check, If it fails, and Stop/resume visible without removing a
command, hint, evidence destination, C/A link, or recovery boundary. M0 reached
four passing tests. The M6 fake suite reached 17 passed and one intentionally
opt-in skipped contract; payment/refund unknown facts were recoverable through
`lookup`. No credential or provider action was attempted. Wrong turns: none in
source traversal. Help: none. Limitation: this observes maintainability and local
execution, not independent learner comprehension.

| Dimension | M0 | M6 | Observation |
|---|---:|---:|---|
| Audience and outcome clarity | 4 | 4 | Plain problem and bounded outcome precede IDs. |
| Time to first successful run | 4 | 4 | Warm locked environments completed in seconds. |
| Executable instructions | 4 | 4 | Literal working directory, command, result, and evidence remain. |
| Language and terminology | 4 | 4 | Baseline/unknown outcome are introduced through examples. |
| Progressive disclosure/navigation | 4 | 4 | Exact support links remain secondary to the action. |
| Guided scaffolding | 4 | 4 | Supplied skeleton/fake; learner domain implementation remains absent. |
| Automated feedback and recovery | 3 | 3 | Local feedback is specific; hosted Actions remain unobserved. |
| Failure-lab reproducibility | 4 | 4 | Reset/replay is deterministic and secret-free. |
| Pause and resume | 4 | 4 | Stop state and exact return anchor are explicit. |

Weighted result: **97.5/100 for each pilot; no dimension below 3**. Decision:
**ROLL OUT** the compact cue grammar. This is the CS3 STOP/GO 2 maintenance
decision only; `HUMAN SELF-STUDY VERIFIED` remains unset and named-human review
stays external.

## 2026-09-14 CS6 local closeout review

The accepted cue grammar is present across all eleven controllers; M0 and M6
retain the detailed pilot labels, while the other controllers use one compact
five-cue key over their existing action/support/observation/recovery/resume scope
lines. Source traversal found no new backtracking, broken exact link, changed C/A
range, or lost recovery instruction. The root validator, 37 controlled
mutations, five locked project quality gates, four isolated PostgreSQL paths,
the three intended red labs, and the complete M10 local rehearsal produced the
results recorded in `PLAN.md`.

This is an internal maintenance and executable-source review. It does not
observe GitHub rendering, hosted Actions, provider behavior, or a named human
career shifter. Therefore **HUMAN SELF-STUDY VERIFIED remains no** and the
external review ledger remains unchecked.

## 2026-09-14 PG4 independent fresh-context review

Reviewer: independent Codex sub-agent with no implementation-history context
before its initial learner-source traversal. Environment: Linux
7.0.0-31-generic x86_64, Python 3.12.3, uv 0.9.21; dirty maintenance candidate
based on `2c2ac09f6b44d5567e6f9db447ad1b2bd5ebdd8b`.

The first review returned **REPAIR**. M6 linked its completed-M5 learner back to
the anonymous M5 launch checkpoint, whose valid initial advice says `/login` is
absent and accidental identity routes should be removed. That made correct M5
work look erroneous during M5→M6 recovery. M5 Block 1 also left its compact
support/recovery cues later than the advertised order. The repair added an
M6-specific post-M5 preflight, scoped anonymous-shell recovery to M5 only, and
reordered M5 Block 1 around its supplied red contract, learner test, evidence,
recovery, and resume boundary.

The same reviewer then reran M0 Block 1, M6 Block 1, M5 Block 1, and the M5→M6
transition and returned **PASS**. No wrong turn or help request remained.

| Dimension | M0 B1 | M6 B1 | M5 B1 | M5→M6 |
|---|---:|---:|---:|---:|
| Audience and outcome clarity | 4 | 4 | 4 | 4 |
| Time to first successful run | 4 | 4 | 3 | 3 |
| Executable instructions | 4 | 4 | 4 | 4 |
| Language and terminology | 4 | 4 | 4 | 4 |
| Progressive disclosure/navigation | 4 | 4 | 4 | 4 |
| Guided scaffolding | 4 | 4 | 4 | 4 |
| Automated feedback and recovery | 3 | 3 | 3 | 3 |
| Failure-lab reproducibility | 3 | 4 | 3 | 4 |
| Pause and resume | 4 | 4 | 4 | 4 |
| **Weighted result** | **96.25%** | **97.5%** | **92.5%** | **93.75%** |

No dimension is below 3. The curriculum validator passed with 11×7 milestone
files and 58 traces; Catalog API tests passed 4/4; Ecommerce API plus failure
harness passed 17/17; the exact M6 harness passed 15/15; and `git diff --check`
passed. The supplied M5 contract produced its intended initial `F..F`: two
missing-route failures and two passing assertions.

Limits: this was a warm local source review, not a clean clone or human study.
The post-M5 preflight cannot run in this neutral repository because the three
M5 test files and identity behavior are intentionally learner-built. PostgreSQL,
live servers, hosted Actions, provider behavior, and human comprehension were
not observed. This review cannot satisfy named-human evidence.
