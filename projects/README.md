# Evolving product laboratories

The repository supplies the smallest starting state needed for honest practice;
the learner builds the product behavior. It does not contain completed milestone
solutions.

- [`catalog/`](catalog/) — runnable M0 baseline plus the opt-in M1 contract.
- [`pos/`](pos/) — PostgreSQL/Alembic M2 launch kit; business tables and rules
  remain learner work. It evolves through M4 and returns in M10.
- [`ecommerce/`](ecommerce/) — anonymous M5 launch kit plus isolated M6/M7
  failure harnesses; identity, policy, resilience, and durable work remain learner work.
- [`booking/`](booking/) — M8 single-request behavior plus a deterministic,
  opt-in double-booking reproduction.
- [`social/`](social/) — M9 small-feed behavior plus a deterministic,
  opt-in N+1 query-budget failure.

Before a new product begins, its milestone README must name the source tag or
fixture, exact green command, expected result, and reset/recovery path. If that
checkpoint does not exist, the milestone is not ready for learner release. Each
linked project README is the canonical setup and recovery guide.

Each project remains independently runnable and follows the repository quality
gates. Evolving products use prior milestone tags; do not add a solution snapshot
for every milestone or create speculative shared libraries. Store actual proof
under `evidence/MN/`, indexed with [the evidence template](../templates/EVIDENCE-INDEX.md).
Store architecture decision records beside the project they govern.
