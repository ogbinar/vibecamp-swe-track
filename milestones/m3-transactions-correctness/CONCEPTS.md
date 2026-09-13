# Problems and mental models

Individually valid writes can create an invalid sale. A transaction groups the smallest business operation whose effects must commit or roll back together. ACID is behavior to test: atomic effects, constraints/consistency, isolation assumptions, and durability after commit.

Application invariants give expressive decisions and errors; database invariants defend against alternate writers and races. State machines name allowed transitions and make duplicate/late commands explicit. Historical receipt facts are snapshots, not joins to mutable current prices.

Race conditions begin here: check-then-write inventory can interleave even when ordinary tests pass. M3 identifies and bounds that risk; M8 deeply compares locking/control strategies. Deterministic clocks/IDs and rounding policy make failure reproduction credible.
