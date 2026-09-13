# Synthetic evidence examples

These examples show shape, not passing learner evidence.

| Slice | Useful evidence | Not enough |
|---|---|---|
| Migration | revision before/after, command, preserved legacy rows, recovery decision | “migration works” |
| Security | synthetic actor/object request, expected denial, actual status/body, unchanged row | screenshot of login |
| Worker | kill point, attempt history, duplicate deliveries, one semantic effect | one happy job |
| Performance | fixed dataset/environment, query count/plan, equal-harness percentiles, correctness test | fastest run |
| Recovery | backup checksum, isolated target, integrity/tenant/audit checks, measured RPO/RTO | backup file exists |

Copy the main evidence template into `evidence/MN/index.md`. Mark irrelevant
fields `N/A — <condition not present>`; never fabricate a command or result.
