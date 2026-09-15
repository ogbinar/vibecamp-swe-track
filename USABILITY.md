# Learner-experience and language rubric

This is a maintainer quality gate, not required learner reading. Complete dated
reviews are preserved in the [usability history](docs/maintainers/archive/2026-09-15-business-first/USABILITY-history.md).

## Target learner

Evaluate the Core path as a person studying alone with basic Python syntax and
basic Git use, but little production-engineering vocabulary or workflow
experience. Prior experience may shorten practice; it never lowers a Core gate.

## Scoring

Score every dimension from 0 to 4: 0 blocked, 1 high friction, 2 interpretive,
3 mostly self-service, and 4 immediate. Multiply the score by one quarter of
the weight. Release requires **85/100 overall and no dimension below 3**.

| Dimension | Weight | A score of 4 means |
|---|---:|---|
| Audience and outcome clarity | 10 | The first screen states audience, prerequisites, product path, and outcome |
| Time to first successful run | 15 | With prerequisites installed, a clean clone reaches a working product and green test within 15 minutes |
| Executable instructions | 20 | Active commands are copyable, with expected output and recovery; no placeholders remain |
| Language and terminology | 15 | The plain-language problem precedes the term; necessary terms and acronyms are defined before use |
| Progressive disclosure/navigation | 10 | One next action is obvious; reference and maintainer material are secondary |
| Guided scaffolding | 10 | The starting state is supplied while engineering decisions remain learner work |
| Automated feedback and recovery | 10 | Local and GitHub checks identify the failed gate and route to recovery guidance |
| Failure-lab reproducibility | 5 | Safe activation/reset is deterministic and does not reveal the diagnosis before the attempt |
| Pause and resume | 5 | `PROGRESS.md` reveals the next action and evidence gap in under two minutes |

## Language contract

1. Describe the concrete problem before naming the concept or pattern.
2. Define a necessary term at first use and link the glossary.
3. Expand an acronym before using it alone.
4. Write instructions as action → reason → expected observation → recovery.
5. Keep one primary requirement per learner checklist item.
6. Use one term consistently unless a distinction is explicitly taught.
7. Show a small example before an abstract rule where practical.
8. Explain M/C/A labels, Core, Stretch, levels, evidence, and cold review before
   using them as instructions.
9. Prefer short sentences and concrete verbs without removing precise terms.

## Cold-test worksheet

| Observation | Result |
|---|---|
| Environment and reference commit | |
| Time to locate first command | |
| Time to green tests and working product | |
| Wrong turns or backtracking | |
| Undefined or confusing terms | |
| Help requested from a person | |
| Commands that failed | |
| Recovery guidance used successfully | |
| Next action stated correctly | |
| Rubric dimensions and weighted score | |

Use a clean clone and public learner instructions for a real cold test. Prefer
a career shifter who did not author the material. Local fresh-context review is
useful maintenance evidence but cannot establish human comprehension.

## Readiness status vocabulary

- **STRUCTURALLY READY:** the named repository shape, links, identifiers, and
  trace contracts pass automated checks.
- **STARTER VERIFIED:** the named supplied starter and documented recovery were
  executed in the stated local environment.
- **HUMAN SELF-STUDY VERIFIED:** a named target learner completed the stated
  transition without author intervention, with environment and wrong turns
  recorded.

These statuses are independent and always name their scope.

## 2026-09-15 business-first Air pilot

Catalog M0/M1, POS M2, Ecommerce M6, and Social M9 were reviewed locally with
Python 3.13.11 and exact Air 0.48.1. Their controller paths and executable
HTML/form/API/OpenAPI/HTMX/SSE/database gates passed. Stale command-map and
evidence anchors were found, repaired, and revalidated. Air pages stayed out of
OpenAPI; no browser handler called its own API; form errors preserved safe
values; M6 used one focused HTMX fragment; and M9 used one non-durable SSE
transport while learner correctness work stayed absent.

Score vector: audience/outcome 4, first run 4, executable instructions 3,
language 4, disclosure/navigation 4, scaffolding 4, feedback/recovery 3,
failure reproducibility 4, pause/resume 4 = **95/100**, no dimension below 3.
Decision: **ROLL OUT**.

This is local maintainer evidence, not a hosted or named-human result. Exact
commands and source hashes are in the [provenance manifest](docs/maintainers/archive/2026-09-15-business-first/README.md).

## 2026-09-15 BF6 local closeout

Status: **STRUCTURALLY READY** for the business-first 11×4 candidate and
**STARTER VERIFIED** for the five named local starters. **HUMAN SELF-STUDY
VERIFIED** remains unset.

The independent local simplicity pass traversed root → M0 → first build block →
proof → progress → M1 and checked all eleven business briefs, outcome summaries,
recovery routes, and next actions. It found three repairable defects: the M0
controller omitted the Air page from its live proof and request-path model; the
M1 checkpoint still said four rather than eight starter tests; and eight
controllers repeated a cue legend before already self-contained blocks. Those
were repaired. A 73-check source traversal then passed.

Final local score vector remains audience/outcome 4, first run 4, executable
instructions 3, language 4, disclosure/navigation 4, scaffolding 4, feedback/
recovery 3, failure reproducibility 4, pause/resume 4 = **95/100**, no dimension
below 3. This is a maintainer source/runtime assessment, not a named-human score.

Verification results:

- curriculum: 11 milestone directories, four contract files each, 58 concept
  traces, and relative links/anchors passed; all five runtimes report Air/Python
  3.13;
- stable semantic suite: all 42 controlled failures were rejected and the
  restored candidate passed;
- locked starter gates: Catalog 8 passed; POS 4 passed/1 database skip;
  Ecommerce 19 passed/1 skip; Booking 4 passed/1 skip; Social 5 passed/1 skip;
  Ruff, format, mypy, lock checks, and live HTML/API/OpenAPI startup passed for
  every starter;
- isolated PostgreSQL migrations and suites: POS 5, Ecommerce 20, Booking 5,
  and Social 6 tests passed;
- intended red/no-solution boundaries: Catalog health, Booking final-seat, and
  Social query-budget checks failed for their intended reasons; Catalog reset
  returned 8 green. The learner-owned M1 and M5 contracts remained red with
  eight and two missing-behavior failures respectively;
- Air behavior: Catalog shared page/API data and safe form errors passed; M6
  HTMX targeting and no-custom-JavaScript passed; M9 SSE content type/event and
  OpenAPI exclusion passed; no project internal-HTTP import, Node runtime,
  custom JavaScript, or callable vulnerable fixture was found;
- containers: all Compose configurations parsed, the digest-pinned Python 3.13
  POS image built and served HTML/API/OpenAPI, and the M10 migration/readiness/
  rollback-command/restore/unhealthy-rejection rehearsal passed. Its synthetic
  SQL/checksum and task-local image were removed afterward;
- provenance: all 44 removed sources matched their recorded SHA-256 hashes and
  all 44 bodies remain in their declared destinations; YAML, secret/unsafe-
  fixture/generated-archive scans and `git diff --check` passed.

The required M6 sandbox, optional provider/tool and real-deployment
endorsements, hosted GitHub rendering/Actions, and named-human career-shifter
reviews remain pending and unchecked in TODO. None was attempted or inferred
from local evidence.
