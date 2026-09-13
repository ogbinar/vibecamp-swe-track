# M8 concepts through booking races

## “Two people booked one seat”

**Example:** both transactions read capacity before either writes. **Term —
interleaving:** the order in which concurrent steps occur. **Rule:** enforce the
capacity invariant in PostgreSQL, across processes—not with a Python lock.

## “Both transactions waited forever”

**Example:** each holds one lock and waits for the other. **Term — deadlock:** a
wait cycle the database must break. **Rule:** keep lock order consistent and
retry only the bounded retryable outcome.

## “A stress test passed but never hit the dangerous timing”

**Example:** requests run quickly but never both read the final seat first. **Term —
time-of-check/time-of-use gap:** truth changes between a check and its write.
**Rule:** coordinate the exact interleaving with barriers; speed is not proof.

## “Which concurrency tool should I choose?”

**Example:** a conditional update can enforce capacity without a broad lock.
**Term — optimistic control:** detect conflict and retry instead of waiting first.
**Rule:** compare atomic writes, constraints, locks, isolation, and versions against
the invariant, contention, deadlock, and retry behavior.

## “Expiry and confirmation happened together”

**Example:** app clocks disagree at the hold boundary. **Term — authoritative
time:** the one clock used for the business decision. **Rule:** use database time,
declare allowed winners, keep lock order consistent, and bound retryable failures.
