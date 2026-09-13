# Acceptance gate

Required maturity: **Level B** for financial/inventory correctness.

## Core

- **A1:** Checkout atomically persists sale, payment, receipt lines, and stock movements; both C1 failure points leave none of the partial effects, proving transaction/ACID behavior.
- **A2:** An invariant map links code, database constraint/atomic mechanism, and tests; duplicate completion, oversell, over-refund, invalid transitions, bypass attempts, and the C2 race preserve truth with stable outcomes.
- **A3:** At least five decimal/rounding cases prove documented order; price/metadata changes cannot alter historical receipts; controlled clock/IDs make repeated tests deterministic.
- **A4:** Unit rule tests, PostgreSQL integration tests, and HTTP API tests have distinct named purposes and pass with migrations/lint/validator from a clean environment.

Record pre/post database queries for each injected failure and explain isolation assumptions still deferred to M8.

## Stretch

Add cash-drawer reconciliation or receipt rendering only after Core; rendering must consume canonical snapshots, not recalculate totals.
