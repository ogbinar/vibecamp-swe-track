# Problems and mental models

Individually valid writes can create an invalid sale. A transaction groups the smallest business operation whose effects must commit or roll back together. ACID is behavior to test: atomic effects, constraints/consistency, isolation assumptions, and durability after commit.

Application invariants give expressive decisions and errors; database invariants defend against alternate writers and races. State machines name allowed transitions and make duplicate/late commands explicit. Historical receipt facts are snapshots, not joins to mutable current prices.

The use case owns the transaction because it knows which reads, decisions, writes, and durable intents form one business operation. A repository may flush or expose persistence operations but must not independently commit and make partial work irreversible. A service that only forwards arguments and a generic repository that hides query shape are costs without an earned boundary.

Race conditions begin here: check-then-write inventory can interleave even when ordinary tests pass. M3 identifies and bounds that risk; M8 deeply compares locking/control strategies. Deterministic clocks/IDs and rounding policy make failure reproduction credible.
