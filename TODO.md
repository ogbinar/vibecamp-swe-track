# Active curriculum-maintenance TODO

This is the single execution checklist for [PLAN.md](PLAN.md). Update it in the same change as implementation work. `PROGRESS.md` remains the learner’s course transcript.

## Tier 1 — Required

### Phase 1: entry and review credibility

- [x] Add `templates/ENTRY-DIAGNOSTIC.md` with executable signals, pass/fail interpretation, targeted remediation, re-check, and no-skip rule.
- [x] Integrate diagnostic routing into M0 `README.md`, `CHALLENGE.md`, `ACCEPTANCE.md`, and `REVIEW.md`; add only a routing note to `CURRICULUM.md`.
- [x] Add the global cold-review gate and solo/peer review modes to `QUALITY-GATES.md`.
- [x] Add cold-review evidence fields to `.github/pull_request_template.md`, `templates/EVIDENCE-INDEX.md`, and the `PROGRESS.md` active dashboard.
- [x] Dry-run entry plus cold review in an isolated read-only copy; executed D1/D2 and documentation checks, explicitly recorded D3–D5 as not runnable without learner software, and claimed no learner evidence.

### Phase 2: disciplined simplicity and common learner lenses

- [x] Add `templates/COMPLEXITY-REJECTION.md` distinct from an ADR: pressure, baseline, evidence, alternatives/cost, rejection/removal, and revisit trigger.
- [x] Integrate the rejection record into `STACK.md`, `QUALITY-GATES.md`, `.github/pull_request_template.md`, M4 `CHALLENGE.md`/`ACCEPTANCE.md`, and focused M7/M9/M10 tool/review references.
- [x] Define career-shifter and data-specialist lenses in `CURRICULUM.md` as optional framing over identical Core gates—not tracks.
- [x] Add concrete lens prompts to `templates/EVIDENCE-INDEX.md` and M0/M2/M4/M6/M9/M10 `REVIEW.md`.
- [x] Audit confirmed no new track/milestone/directory or reduced persona gate; lens prompts transfer existing strengths without stereotyped prerequisites.

### Phase 3: portfolio proof

- [x] Add `templates/PORTFOLIO-CASE-STUDY.md` grounded in linked evidence, contextual metrics, trade-offs, contribution, operations/recovery, and limitations.
- [x] Add an interim M4 checkpoint and final M10 case-study evidence to the relevant `ACCEPTANCE.md`/`REVIEW.md` files.
- [x] Link the case study from README deliverables, `QUALITY-GATES.md`, and the `PROGRESS.md` dashboard without duplicating the evidence index.
- [x] Cold-reviewed Tier 1 for navigation, evidence integrity, workload, duplication, leakage, and fabrication risks; findings and one corrected review-script assumption are recorded in `PLAN.md`.

## Tier 2 — Optional; decide after Tier 1

- [x] P6 implemented: the requirements and issue templates plus M1/M4 challenge/acceptance paths now exercise stakeholder change and decision rights without fictional ceremony.
- [x] P7 implemented: one data-lifecycle template is consumed by M2/M5/M6/M7/M9/M10 with field-level evidence and explicit deferral where appropriate.
- [x] P8 implemented: preserve-the-failure guidance now keeps safe reproduction/diagnosis/regression evidence while prohibiting broken callable production paths.
- [x] P9 implemented: `PROGRESS.md` now has an action-oriented dashboard for IDs, gaps, cold review, risk, decision, next action, and validation reference.
- [x] Tier 2 decision: implemented P6–P9 because each directly exercises existing product/data/failure/progress work with bounded templates or fields; no separate ceremony or track was added.

## Tier 3 — Optional polish

- [x] Implemented low-cost validator checks for required templates, stable headings, README navigation, and empty repository files; prose remains unconstrained.
- [x] Declined a cold-review issue template: the PR plus evidence index already owns the review, so another issue would duplicate state.
- [x] Deferred live resource-link curation: no maintenance owner/version cadence exists; current selection standards avoid stale citations.
- [x] Declined a separate maintainer checklist and extra navigation/diagrams: `TODO.md`, PR fields, and README navigation passed the cold read without the added artifacts.

## Final verification

- [x] Ran `python3 scripts/check_curriculum.py` successfully after implementation and review fixes.
- [x] Independently verified exactly 11 milestone directories × exactly 7 required files (77 total).
- [x] Verified all relative Markdown links, including `PLAN.md` and `TODO.md`, through the validator.
- [x] Verified all 58 concepts still trace to existing challenge and acceptance IDs.
- [x] Parsed all four `.github` YAML files successfully.
- [x] Verified no stale legacy application paths/directories or old milestone-file paths.
- [x] Verified expected uncommitted status, zero remotes, zero commits, and no publication/external action.

## Already satisfied / no action

- [x] Exact M0–M10 progression and seven-file milestone contract.
- [x] Problem-first build/test/break/debug/refactor/operate/ship cycle and rising brownfield ratio.
- [x] Seeded failure/incident system and objective Level A/B/C quality gates.
- [x] Fifty-eight-concept introduce/practice/prove matrix with C/A traceability.
- [x] GitHub-only workflow, project evolution, evidence/ADR/requirements/postmortem templates, and release discipline.
- [x] Minimal FastAPI modular monolith, FastCRUD after fundamentals, earned optional tools, and explicit enterprise exclusions.
