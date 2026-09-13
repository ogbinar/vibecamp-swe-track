# Challenge brief

- **C1 — Final-seat race:** Coordinate two naive check-then-insert transactions with barriers. Capture the exact oversubscribing interleaving, then preserve it as a non-production reproduction.
- **C2 — Database-enforced fix:** Choose constraint/atomic update/optimistic or pessimistic locking from the capacity model. Race the final units at least 100 times across app processes; assert exact winners and final invariant.
- **C3 — Time and lock incident:** Race confirm versus expire and cancel versus confirm at boundary instants. Induce inconsistent lock-order deadlock, observe database behavior, establish order/bounded retry, and report contention/latency/errors.

Refactor from naive to smallest correct database strategy. Operate by inspecting locks and stuck transactions. Ship honest 409/retry semantics and scaling limits.
