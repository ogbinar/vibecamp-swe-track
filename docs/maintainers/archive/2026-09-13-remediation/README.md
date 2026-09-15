# 2026-09-13 maintenance provenance

This is an inventory and evidence index, **not an active tracker**. Active
rationale stays in [PLAN](../../../../PLAN.md); work stays in
[TODO](../../../../TODO.md); review evidence stays in
[USABILITY](../../../../USABILITY.md). No PLAN/TODO snapshots are activated here.

## Baseline and retention

Reference: `d259148` plus the valuable pre-existing dirty candidate, captured
before local IA edits. [Path inventory](inventory.json) records every active
file's SHA-256, logical bytes, and tracked/active-candidate/ignored provenance;
residue records resolved paths, sizes, modification time, and ignore status.
103 tracked and 149 active untracked paths are protected. The untracked audit
inputs and USABILITY are active work, not disposable history.

No historical document was moved or deleted. PLAN/TODO retain all completed
evidence and active obligations at their original public paths. PERSONA-REVIEW,
ANALYSIS, and historical USABILITY sections remain in place because they have
live citations and public-link exposure is unverified. KEEP is reversible with
no path migration or Git-index changes; no deprecation stub is necessary.

Ignored `.venv` directories are retained until a separately authorized disk goal;
recovery would require `uv sync --locked` in the owning project. Empty `dist/`
is retained. Logs, databases, coverage, release artifacts, and learner evidence
are retained until their owner approves disposition; no age-based deletion.
Content hashes identify source; they do not upgrade an artifact into release proof.

## Removal manifest

Only the cache directories enumerated below are approved for removal by the
2026-09-13 task request. All are ignored and outside `.venv`; regeneration uses
Ruff, mypy, pytest, and Python imports in their owning project. Sizes are logical
file bytes, not filesystem blocks or promised net disk savings. No source,
lockfile, contract, evidence, database, log, image, dist, or environment is a target.

| Exact old path | Pre-removal bytes | Disposition | Regeneration / rollback |
|---|---:|---|---|
| `/projects/vibecamp-swe-track/.ruff_cache` | 78 | REMOVE / IGNORE | Ruff check/format |
| `/projects/vibecamp-swe-track/projects/ecommerce/.pytest_cache` | 1899 | REMOVE / IGNORE | pytest |
| `/projects/vibecamp-swe-track/projects/ecommerce/.mypy_cache` | 17858784 | REMOVE / IGNORE | mypy |
| `/projects/vibecamp-swe-track/projects/ecommerce/.ruff_cache` | 2418 | REMOVE / IGNORE | Ruff check/format |
| `/projects/vibecamp-swe-track/projects/ecommerce/src/ecommerce_api/__pycache__` | 10791 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/ecommerce/tests/__pycache__` | 17875 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/ecommerce/migrations/__pycache__` | 1995 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/ecommerce/migrations/versions/__pycache__` | 585 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/catalog/.pytest_cache` | 768 | REMOVE / IGNORE | pytest |
| `/projects/vibecamp-swe-track/projects/catalog/.mypy_cache` | 11804896 | REMOVE / IGNORE | mypy |
| `/projects/vibecamp-swe-track/projects/catalog/.ruff_cache` | 1718 | REMOVE / IGNORE | Ruff check/format |
| `/projects/vibecamp-swe-track/projects/catalog/src/catalog_api/__pycache__` | 3887 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/catalog/tests/__pycache__` | 6803 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/pos/.pytest_cache` | 751 | REMOVE / IGNORE | pytest |
| `/projects/vibecamp-swe-track/projects/pos/.mypy_cache` | 17817824 | REMOVE / IGNORE | mypy |
| `/projects/vibecamp-swe-track/projects/pos/.ruff_cache` | 1890 | REMOVE / IGNORE | Ruff check/format |
| `/projects/vibecamp-swe-track/projects/pos/src/pos_api/__pycache__` | 3770 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/pos/tests/__pycache__` | 7990 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/pos/migrations/__pycache__` | 2061 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/pos/migrations/versions/__pycache__` | 568 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/social/.pytest_cache` | 1019 | REMOVE / IGNORE | pytest |
| `/projects/vibecamp-swe-track/projects/social/.mypy_cache` | 17838304 | REMOVE / IGNORE | mypy |
| `/projects/vibecamp-swe-track/projects/social/.ruff_cache` | 2178 | REMOVE / IGNORE | Ruff check/format |
| `/projects/vibecamp-swe-track/projects/social/src/social_api/__pycache__` | 4320 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/social/src/social_lab/__pycache__` | 4938 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/social/tests/__pycache__` | 9768 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/social/challenges/__pycache__` | 2986 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/social/migrations/__pycache__` | 2070 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/social/migrations/versions/__pycache__` | 570 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/booking/.pytest_cache` | 992 | REMOVE / IGNORE | pytest |
| `/projects/vibecamp-swe-track/projects/booking/.mypy_cache` | 17838304 | REMOVE / IGNORE | mypy |
| `/projects/vibecamp-swe-track/projects/booking/.ruff_cache` | 2090 | REMOVE / IGNORE | Ruff check/format |
| `/projects/vibecamp-swe-track/projects/booking/src/booking_api/__pycache__` | 4331 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/booking/src/booking_lab/__pycache__` | 1816 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/booking/tests/__pycache__` | 12209 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/booking/challenges/__pycache__` | 3438 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/booking/migrations/__pycache__` | 2073 | REMOVE / IGNORE | Python import or owning tests |
| `/projects/vibecamp-swe-track/projects/booking/migrations/versions/__pycache__` | 572 | REMOVE / IGNORE | Python import or owning tests |

Executed: all 38 manifested cache directories removed, totaling 83,279,329
pre-removal logical bytes. Source paths and five environments remain present.
Normal checks will regenerate applicable ignored caches; net retained disk
savings are not claimed. SHA/provenance for retained source is in the inventory;
caches have no unique-content destination, public link, or Git recovery hash.
They are reconstructed from retained source and locked environments. Only listed
resolved paths may disappear. Reconcile hashes and Git status after regeneration.

## Authority and backlink evidence

PLAN owns scope/sequence/decisions, TODO owns active work, USABILITY owns the
rubric/current results. README links the maintainer route only after the learner
route. CURRICULUM, STACK, QUALITY-GATES, PROGRESS, project READMEs and milestone
support files retain their distinct contracts. Local command/expected/recovery/
stop text remains beside the work even when a general rule is linked.

Backlink inspection used `rg -n` for PLAN/TODO/PERSONA-REVIEW/ANALYSIS/USABILITY,
REQUIREMENTS, INCIDENT-POSTMORTEM and RUNBOOK-INCIDENT across Markdown, Python,
and YAML. Git history used `git log --all --` on candidate paths. The validator
requires the evidence templates by name; zero learner links cannot justify
removing them. Historical analysis requests local sub-IDs; the later PLAN
implementation record supersedes that with stable C/A IDs plus local steps.


## Final candidate verification

Learner/controller/validator content fingerprint (SHA-256 over sorted path and
file-SHA lines): `c28b1bb0d77738f36f1108f84b176509a6955c9163428355df2c85fb5cb95537`. Reference remains `d259148` plus
uncommitted candidate; this is not a commit or learner pass.

Actual task-changed existing files (relative to the captured dirty baseline):

- `PLAN.md`
- `PROGRESS.md`
- `README.md`
- `TODO.md`
- `USABILITY.md`
- `milestones/m0-engineering-baseline/README.md`
- `milestones/m1-production-api-foundation/README.md`
- `milestones/m10-production-multitenant-saas-capstone/README.md`
- `milestones/m2-pos-persistence-data-modeling/README.md`
- `milestones/m3-transactions-correctness/README.md`
- `milestones/m4-maintainability-testing-refactoring/README.md`
- `milestones/m5-secure-multi-user-ecommerce/README.md`
- `milestones/m6-resilient-external-integrations/README.md`
- `milestones/m7-durable-async-background-processing/README.md`
- `milestones/m8-concurrency-booking/README.md`
- `milestones/m9-performance-caching-realtime-social/README.md`
- `scripts/check_curriculum.py`
- `scripts/test_validator_mutations.py`
- `templates/RUNBOOK-INCIDENT.md`
- `templates/SEMANTIC-AUDIT.md`

New files: `docs/maintainers/README.md`, this provenance index, and `inventory.json`.
No tracked/untracked file was moved or removed. Thirty-eight explicitly listed
ignored cache directories were removed; 37 regenerated and the unused root Ruff
cache stayed absent. All initial active paths remain, with every project and
GitHub file byte-identical to baseline. The six support files per milestone are
also unchanged. All source/evidence preservation checks passed.

Validation: 11×7/58 traces and all links pass; 30 controlled failures are rejected
for their intended reason (including 11 IA cases), unmutated/restored candidates
pass; all six GitHub YAML files parse; 32 ordinary project tests pass with real
PostgreSQL where applicable; lint/format/types/locked sync and migrations pass.
Expected booking/social failures remain intentional. `git diff --check` passes.

Raw timing/command outputs remain host-local at
`/tmp/vibecamp-ia-cu-nbmj5obs/`; durable results and limitations are recorded in
[USABILITY history](../2026-09-15-business-first/USABILITY-history.md#local-verification-and-cleanup-result).
No dependency advisory refresh, hosted rendering/Actions, named human test, new
M10 image rehearsal, or real-target evidence is claimed by this pass.
