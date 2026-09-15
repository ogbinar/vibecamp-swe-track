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
C1–C3 in [CHALLENGE.md](CHALLENGE.md#m3-challenge-brief): interrupt checkout between writes, bypass
application checks with SQL, and interleave two stock deductions.

Keep transaction ownership at the use-case boundary. Do not commit inside a
repository or add a queue to disguise an unclear transaction.

## Start here

- **Gate:** [A1–A4 / Level B](ACCEPTANCE.md#core).
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
When needed: [C1 scenario and hints](CHALLENGE.md#c1--partial-checkout-incident) and [concept explanation](REFERENCE.md#payment-exists-but-the-sale-does-not). [Tool boundaries](REFERENCE.md#tools-earned-here) apply to this product.

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
When needed: [C3 scenario and hints](CHALLENGE.md#c3--historical-arithmetic) and [concept explanation](REFERENCE.md#the-api-rejected-it-but-direct-sql-accepted-it).

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
When needed: [C2 scenario and hints](CHALLENGE.md#c2--invariant-bypass-and-race) and [concept explanation](REFERENCE.md#both-buyers-saw-the-final-unit).

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

Use the current project dependencies first. Open [Use now](REFERENCE.md#use-now) for the active pattern, [Evaluate after evidence](REFERENCE.md#evaluate-after-evidence) only after the simpler baseline misses its target, and [Do not add yet](REFERENCE.md#do-not-add-yet) before adding another runtime or service.

## Prove it

Answer [review prompts](ACCEPTANCE.md#review) after the Core proof.

Prove [A1–A4](ACCEPTANCE.md#core) with unit calculations, PostgreSQL integration
tests, API tests, before/after state, and rollback evidence.

## Done / next

Every named failure leaves an explainable valid state and all Core checks pass.
Tag `m3-transactions-correctness`.

### Recovery

Use [targeted references](REFERENCE.md#resources-for-m3) only for the question left by the active hint ladder.

Inspect the first partial state, then the transaction owner, then the PostgreSQL
transaction reference in [REFERENCE.md](REFERENCE.md#resources-for-m3). Return to the reviewed M2
tag if you cannot restore a green baseline.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Continue to [M4](../m4-maintainability-testing-refactoring/README.md).

[Previous milestone: M2](../m2-pos-persistence-data-modeling/README.md) · [Course home](../../README.md) · [Next milestone: M4](../m4-maintainability-testing-refactoring/README.md)
