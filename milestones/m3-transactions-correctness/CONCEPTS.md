# M3 concepts through checkout failures

## “Payment exists but the sale does not”

**Example:** the process dies between two commits. **Term — transaction:** a
group of database changes that all succeed or all fail. **Rule:** the use case
owns one transaction around the smallest complete business operation.

## “Both buyers saw the final unit”

**Example:** two check-then-write operations interleave. **Term — race
condition:** correctness changes with timing. **Rule:** coordinate the dangerous
interleaving and assert final database truth.

## “Every write was valid, but the sale was invalid”

**Example:** payment and receipt commit while inventory rolls back. **Term — ACID:**
atomicity, consistency, isolation, and durability. **Rule:** test these as observed
behavior around the smallest complete business operation.

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
