# M3 — Make checkout safe

[Course home](../../README.md) / M3

**Milestone 4 of 11 · M3**

## Business problem

A checkout that charges money but loses inventory or receipt state is worse than
a rejected sale. Make the whole business operation succeed or fail together.

## Product objective

- **Product can:** a checkout either completes its local inventory, payment intent, and receipt changes together or leaves them unchanged.
- **You will prove:** atomicity, money, repeat-request, partial-failure, and race regressions.

Follow the [fixed checkout contract](../../projects/pos/specs/M3-CHECKOUT-CONTRACT.md).
Add checkout, payment records, immutable receipt snapshots, stock movements,
voids, and refunds. First write invariant and transition examples. Then complete
C1–C3 in the [challenge brief](#challenge-brief): interrupt checkout between writes, bypass
application checks with SQL, and interleave two stock deductions.

Keep transaction ownership at the use-case boundary. Do not commit inside a
repository or add a queue to disguise an unclear transaction.

## Start here

- **Gate:** [A1–A4 / Level B](#core).
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/pos/README.md#pos-launch-kit-for-m2), then return to the saved block; first visit: [Block 1](#1-make-one-checkout-atomic-required).

Start from your reviewed `m2-pos-persistence` tag. Run the POS health,
PostgreSQL, migration, and test commands from `projects/pos/`; all must be green.

On resume, preserve your existing `.env` and evidence. Use the validation
commands from the starting checks; first-install copy and destructive reset
steps are not routine resume actions. If a check fails, use Recovery first.

## Build

### 1. Make one checkout atomic `[REQUIRED]`

Start from the starting checkpoint above. Work in `projects/pos/`;
focus on `tests/m3/test_atomic_checkout.py` and the output named below. Record `evidence/M3/atomic-checkout.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 1](#1-make-one-checkout-atomic-required) using that saved result; continue to Block 2.
When needed: [C1 scenario and hints](#c1--partial-checkout-incident) and [concept explanation](#payment-exists-but-the-sale-does-not). [Tool boundaries](#tools-earned-here) apply to this product.

**Supplied:** the [checkout contract](../../projects/pos/specs/M3-CHECKOUT-CONTRACT.md).
**You build:** checkout service, transaction boundary, and rollback tests in
`projects/pos/`. Run a named narrow integration test; observe no partial facts
after an injected exception. Record `evidence/M3/atomic-checkout.md`. Stop at
one green happy path and one green rollback case.

Run from the stated project directory:

```bash
POS_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5432/vibecamp_pos uv run --locked pytest tests/m3/test_atomic_checkout.py -q
```

### 2. Make money and repeats exact `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/pos/`;
focus on `tests/m3/test_money_and_repeats.py` and the output named below. Record `evidence/M3/money-and-repeats.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 2](#2-make-money-and-repeats-exact-required) using that saved result; continue to Block 3.
When needed: [C3 scenario and hints](#c3--historical-arithmetic) and [concept explanation](#the-api-rejected-it-but-direct-sql-accepted-it).

Implement the contract's discount, tax, rounding, void, refund, and idempotency
examples. Run focused parameterized tests and compare exact decimal strings.
Record `evidence/M3/money-and-repeats.md`. If values drift, write intermediate
amounts before changing rules; stop when every published example is green.

Run from the stated project directory:

```bash
POS_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5432/vibecamp_pos uv run --locked pytest tests/m3/test_money_and_repeats.py -q
```

### 3. Race the final unit `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in `projects/pos/`;
focus on `tests/m3/test_final_unit_race.py` and the output named below. Record `evidence/M3/concurrency.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 3](#3-race-the-final-unit-required) using that saved result; continue to [Prove it](#prove-it).
When needed: [C2 scenario and hints](#c2--invariant-bypass-and-race) and [concept explanation](#both-buyers-saw-the-final-unit).

Build the specified two-connection barrier harness. Observe the naive failure,
then enforce the invariant with the smallest database/application combination.
Record interleaving, winner count, final invariant, and retry rule in
`evidence/M3/concurrency.md`. Stop when exactly one sale wins.

Run from the stated project directory:

```bash
POS_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5432/vibecamp_pos uv run --locked pytest tests/m3/test_final_unit_race.py -q
```

### Diagnose deliberate failures

Activate or construct only the current C scenario. Record the symptom and one
hypothesis before inspecting the implementation. Use the matching scenario link
in your active block, then its three hint levels in order. Reset to the last
green checkpoint before starting another scenario.

## Understand

- **Invariant:** a rule that must remain true, such as stock never becoming negative.
- **Transaction:** reads and writes committed or rolled back as one operation.
- **ACID:** atomicity, consistency, isolation, and durability properties.
- **Atomic:** externally observed as all-or-nothing.
- **State machine:** allowed states and transitions for a sale.

## Use a tool if earned

Use the current project dependencies first. Open [Use now](#use-now) for the active pattern, [Evaluate after evidence](#evaluate-after-evidence) only after the simpler baseline misses its target, and [Do not add yet](#do-not-add-yet) before adding another runtime or service.

## Prove it

Answer [review prompts](#review) after the Core proof.

Prove [A1–A4](#core) with unit calculations, PostgreSQL integration
tests, API tests, before/after state, and rollback evidence.

## Done / next

Every named failure leaves an explainable valid state and all Core checks pass.
Tag `m3-transactions-correctness`.

### Recovery

Use [targeted references](#resources-for-m3) only for the question left by the active hint ladder.

Inspect the first partial state, then the transaction owner, then the PostgreSQL
transaction reference in [reference](#resources-for-m3). Return to the reviewed M2
tag if you cannot restore a green baseline.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Continue to [M4](../m4-maintainability-testing-refactoring/README.md).

[Previous milestone: M2](../m2-pos-persistence-data-modeling/README.md) · [Course home](../../README.md) · [Next milestone: M4](../m4-maintainability-testing-refactoring/README.md)


---

## Challenge brief

Run from `projects/pos/`. Each scenario owns its test, hints, evidence, and reset.

## **C1 — Partial checkout incident**

**YOU BUILD** — add deterministic kill hooks at the published transaction boundaries.

### Steps

1. Create `tests/m3/test_atomic_checkout.py` with happy-path and rollback cases.
2. Fail after payment insert and after receipt creation but before stock movement.
3. Run README Block 1 and prove each failure leaves no partial business fact.

### Hints

1. Query every affected table before and after the failure.
2. Inspect the use-case transaction owner and every flush or commit.
3. Use the SQLAlchemy transaction link in the Reference section below.

### Reset

Disable the kill hook and run `uv run --locked pytest tests/m3/test_atomic_checkout.py -q`.

## **C2 — Invariant bypass and race**

**YOU BUILD** — coordinate two independent database connections with a barrier.

### Steps

1. Create `tests/m3/test_final_unit_race.py` and reproduce check-then-write oversell.
2. Attempt duplicate completion, over-refund, forbidden transition, and direct-SQL invalid state.
3. Place each invariant deliberately, rerun Block 3, and record winners and final rows.

### Hints

1. Write the interleaving and final invariant before selecting a lock.
2. Inspect constraints, isolation, lock target, and retry boundary.
3. Use the PostgreSQL isolation link in the Reference section below.

### Reset

Use the POS bounded reset, migrate to head, and rerun the coordinated test; do
not replace the barrier with sleeps. The focused rerun is
`uv run --locked pytest tests/m3/test_final_unit_race.py -q`.

## **C3 — Historical arithmetic**

**PROVIDED** — money examples and expected totals are fixed in the contract.

### Steps

1. Create `tests/m3/test_money_and_repeats.py` from the decimal examples.
2. Change current product price after sale and exercise rounding, void, and refund.
3. Run README Block 2 and prove receipt history does not change.

### Hints

1. Print named intermediate decimal amounts.
2. Inspect calculation order, receipt snapshots, and allowed transitions.
3. Use the Python decimal and state-machine links in the Reference section below.

### Reset

Restore fixed synthetic prices and run
`uv run --locked pytest tests/m3/test_money_and_repeats.py -q`.

Ship an invariant map, exact money examples, and rollback evidence.


---

## Acceptance gate

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


---

## Reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M3 concepts through checkout failures

## “Payment exists but the sale does not”

**Example:** the process dies between two commits. **Term — transaction:** a
group of database changes that all succeed or all fail. **Rule:** the use case
owns one transaction around the smallest complete business operation.

## “Both buyers saw the final unit”

**Example:** two check-then-write operations interleave. **Term — race
condition:** correctness changes with timing. **Rule:** coordinate the dangerous
interleaving and assert final database truth.

## “Every write was valid, but the sale was invalid”

**Example:** the local payment-intent record and receipt commit while inventory rolls back. **Term — ACID:**
atomicity, consistency, isolation, and durability. **Rule:** test these as observed
behavior around the smallest complete business operation.

This transaction protects only local database facts. A later remote payment
cannot participate in the same rollback; M6 adds idempotency, unknown state,
lookup, and reconciliation for that boundary.

## “The API rejected it, but direct SQL accepted it”

**Example:** another writer bypasses the stock check. **Term — invariant:** a rule
that must always remain true. **Rule:** use application checks for decisions and
clear errors; use database enforcement where alternate writers or races can break truth.

## “The repository committed too early”

**Example:** one repository makes part of checkout irreversible before the use
case finishes. **Term — transaction owner:** the layer deciding which operations
form one unit. **Rule:** the use case commits or rolls back; repositories expose
persistence operations without hiding query shape or independently committing.

## “A timing bug disappeared during debugging”

**Example:** ordinary tests never reproduce two inventory reads before either
writes. **Term — deterministic fixture:** controlled clocks, IDs, and barriers
that reproduce the same condition. **Rule:** preserve the interleaving now; M8
later compares locking and control strategies deeply.

### Tools earned here

Use the existing FastAPI/PostgreSQL/SQLAlchemy/Alembic stack plus pytest failure injection, controlled clock/ID seams, and small SQL inspection scripts. The database transaction and its isolation behavior are the tool; hide neither behind a generic decorator nor a repository that commits independently.

Keep the transaction local: it owns inventory, sale, receipt, and payment-intent
records in PostgreSQL. It cannot roll back a remote provider effect; do not add
a provider here. Carry that uncertainty to M6.

No message broker, cache, distributed lock, or separate inventory/payment service. Avoid mocks for atomicity—use real integration tests. Earn more sophisticated concurrency control only when M8 measures its contention and semantics.

## Evaluate after evidence

Evaluate optional tools only after the stated simpler baseline fails. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates current behavior, or creates a second application path.

## Sources

### Resources for M3

Use these after reproducing partial writes or conflicting checkouts. Reviewed 2026-09-13.

- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — What can concurrent transactions observe? Applicable tool: current PostgreSQL.
- [PostgreSQL explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html) — Which lock protects the invariant, and what can it block? Applicable tool: current PostgreSQL.
- [SQLAlchemy transactions](https://docs.sqlalchemy.org/en/20/orm/session_transaction.html) — Where should commit and rollback boundaries live? Applicable tool: SQLAlchemy 2.0.

Read database behavior first; an ORM cannot strengthen an invariant by itself.
