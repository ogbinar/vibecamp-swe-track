# Engineering journal and progress transcript

This file tracks learner course advancement. Curriculum-maintenance work is tracked separately in [TODO.md](TODO.md) against [PLAN.md](PLAN.md).

Repository support is separate from your learner status. Starter verification
does not check off a gate. Keep the recorded values below until your own evidence changes.

Status: `NOT STARTED`, `ACTIVE`, `GATE REVIEW`, `PASSED`, or `REOPENED`.

| Milestone | Required level | Status | Issue | Final PR | Evidence index | Tag/release | Date |
|---|---|---|---|---|---|---|---|
| M0 Engineering Baseline | A | NOT STARTED | — | — | — | — | — |
| M1 Production-minded API Foundation | A + selected B | NOT STARTED | — | — | — | — | — |
| M2 POS Persistence & Data Modeling | B | NOT STARTED | — | — | — | — | — |
| M3 Transactions & Correctness | B | NOT STARTED | — | — | — | — | — |
| M4 Maintainability, Testing & Refactoring | B | NOT STARTED | — | — | — | — | — |
| M5 Secure Multi-user Ecommerce | B + contextual C | NOT STARTED | — | — | — | — | — |
| M6 Resilient External Integrations | B + contextual C | NOT STARTED | — | — | — | — | — |
| M7 Durable Async & Background Processing | C for async slice | NOT STARTED | — | — | — | — | — |
| M8 Concurrency Lab using Booking | B | NOT STARTED | — | — | — | — | — |
| M9 Performance, Caching & Realtime using Social | B + contextual C | NOT STARTED | — | — | — | — | — |
| M10 Production Multi-tenant SaaS Capstone | C | NOT STARTED | — | — | — | — | — |

## Active milestone dashboard

Keep values short and link to the issue/evidence rather than duplicating detail.

| Field | Current value |
|---|---|
| Milestone / required level | Milestone 1 of 11 · M0 / A |
| Branch or issue | — |
| Active challenge / criterion IDs | C1 / A1 |
| Evidence gaps | Clean-checkout transcript and diagnostic result |
| Cold review | NOT SCHEDULED |
| Portfolio case study | NOT STARTED |
| Top risk / blocked decision | Hidden local setup assumptions / none |
| Smallest next action | [Start now](README.md#start-now), then [M0 Block 1](milestones/m0-engineering-baseline/README.md#1-run-the-supplied-baseline-required); work in projects/catalog and run `uv run --locked pytest` |
| Last green reference / date | — |

## Journal entry contract

Append short dated entries linking to durable evidence: what changed, observed result, diagnosis, decision, and next experiment. Keep raw transcripts in the milestone evidence index/release asset, not here. Never claim a pass without a link.

At every pause, update exactly four dashboard fields: active C/A ID, evidence
gap, smallest next action, and last green tag/commit. On return, open only the
active milestone README, run its starting-checkpoint command, and continue that
named C/A item at the exact block anchor saved in Smallest next action. Preserve your existing `.env` and evidence: do not rerun first-install copy
or destructive reset steps merely to resume. If the command is not green,
recovery—not new feature work—is the next action.

### Synthetic pause example

Suppose you stop during M2 after a constraint test passes:

- Active C/A ID: `C1 / A1`
- Evidence gap: `fresh-database migration transcript`
- Smallest next action: `cd projects/pos && uv run --locked alembic upgrade head`
- Last green reference/date: `abc1234 / 2026-09-13`

On return, run that command before opening a new task. Replace this example with
your own dashboard values; do not mark the milestone passed.
