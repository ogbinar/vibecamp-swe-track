# M3 reference

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
