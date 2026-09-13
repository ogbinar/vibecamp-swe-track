# M8 — Concurrency Lab using Booking

**Capability:** reproduce and prevent invariant violations when requests interleave. **Deliverable:** create `projects/booking/` with finite inventory, temporary holds, confirmation, expiry, and cancellation, then make final-capacity correctness hold across multiple processes.

Prerequisite: M7 durable failure reasoning. Sequence: specify capacity/time invariants → build smallest naive slice → deterministically race it → compare database controls → fix and stress → induce deadlock/expiry races → operate contention → ship `m8-concurrency-booking`.

Outputs: state/invariant model, interleaving trace, locking/control rationale, deterministic harness, stress summary, stable conflict API, and deadlock recovery evidence.
