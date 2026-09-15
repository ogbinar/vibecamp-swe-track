# Acceptance gate

Required maturity: **Level B** for financial/inventory correctness.

## Core

- **A1:**
  - [ ] Checkout atomically persists local sale, payment-intent, receipt-line, and stock-movement facts
  - [ ] both C1 failure points leave none of the partial effects, proving transaction/ACID behavior.
  - [ ] evidence states that database rollback cannot undo provider money and routes remote uncertainty to M6 lookup/reconciliation.
- **A2:**
  - [ ] An invariant map links code, database constraint/atomic mechanism, and tests
  - [ ] duplicate completion, oversell, over-refund, invalid transitions, bypass attempts, and the C2 race preserve truth with stable outcomes.
- **A3:**
  - [ ] At least five decimal/rounding cases prove documented order
  - [ ] price/metadata changes cannot alter historical receipts
  - [ ] controlled clock/IDs make repeated tests deterministic.
- **A4:**
  - [ ] Unit rule tests, PostgreSQL integration tests, and HTTP API tests have distinct named purposes and pass with migrations/lint/validator from a clean environment.

## Execution map

Each checklist bullet is a local step in order. From `projects/pos/`, use README
Block 1 for A1, Block 3 for A2, Block 2 for A3, and
`uv run --locked ruff check . && uv run --locked mypy && uv run --locked pytest`
for A4. Record command/result under the matching A heading in `evidence/M3/`;
recover through the POS bounded reset and the last green focused test.

Record pre/post database queries for each injected failure and explain isolation assumptions still deferred to M8.

## Stretch

Add cash-drawer reconciliation or receipt rendering only after Core; rendering must consume canonical snapshots, not recalculate totals.

## Review

### Review

Answer one question at a time in `evidence/M3/index.md`:

1. Which facts must commit or roll back together?
2. Why does the use case own commit and rollback?
3. What observation demonstrates each ACID property in this checkout?
4. Which receipt facts are immutable snapshots?
5. Which invariants are enforced by application code, database rules, or both?
6. Which sale transitions are allowed?
7. What is the exact two-request C2 interleaving?
8. Where could a hidden commit create partial work?
9. Where is rounding applied, and why only there?
10. What final state do you predict after a mid-checkout crash?
