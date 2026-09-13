# Evolving product laboratories

Create project code only when its milestone begins; this curriculum repository intentionally ships none.

- `catalog/` — M0–M1.
- `pos/` — M2–M4, then evolved in M10.
- `ecommerce/` — M5–M7.
- `booking/` — M8 concurrency lab.
- `social/` — M9 performance lab.

Each project remains independently runnable but follows the repository quality gates. Do not snapshot apps by milestone or create speculative shared libraries. Store actual milestone proof inside the relevant project under `evidence/MN/`, indexed with [the evidence template](../templates/EVIDENCE-INDEX.md). Store ADRs beside the project they govern.
