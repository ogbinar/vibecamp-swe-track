# Review

Answer one question at a time in `evidence/M3/index.md`:

1. Which facts must commit or roll back together?
2. Why does the use case own commit and rollback?
3. What observation demonstrates each ACID property in this checkout?
4. Which receipt facts are immutable snapshots?
5. Which invariants are enforced by application code, database rules, or both?
6. Which sale transitions are allowed?
7. What is the exact two-request C2 interleaving?
8. Where could a hidden commit create partial work?
9. Where is rounding applied, and why only there?
10. What final state do you predict after a mid-checkout crash?
