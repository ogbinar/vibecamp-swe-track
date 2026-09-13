# Problems and mental models

“Check availability, then insert” has a time-of-check/time-of-use gap. Lost update, write skew, and oversubscription are interleavings, not speed problems. A concurrency test coordinates transactions at the dangerous boundary; merely launching fast requests may never reproduce it.

Database choices include atomic conditional writes, unique/exclusion constraints, row/advisory locks, isolation levels, and optimistic version checks. Pessimistic locking trades waiting/deadlocks for earlier conflict control; optimistic control trades retries for less blocking. The invariant must hold across processes, not through a Python lock.

Holds are a state machine with database-time policy. Confirmation/expiry/cancellation races need declared winner semantics. Lock ordering limits deadlocks; serialization/deadlock failures need bounded retry or a stable client conflict—not hangs.
