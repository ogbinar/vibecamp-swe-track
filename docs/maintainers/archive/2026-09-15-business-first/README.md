# Business-first migration provenance and rollback manifest

This dated maintainer record tracks the local BF migration. It is not a learner
route or a completion claim. The pre-migration files remain recoverable from the
dirty-tree content represented by these SHA-256 hashes and from the repository
diff; do not use `HEAD` to overwrite unrelated user work.

## File merge map

For every milestone, `CONCEPTS.md`, `TOOLS.md`, and `RESOURCES.md` move without
semantic deletion into `REFERENCE.md`; `REVIEW.md` moves into the `## Review`
section of `ACCEPTANCE.md`. Inbound links move to the matching preserved anchor.
Rollback one milestone by restoring its four recorded sources, removing only
that milestone's `REFERENCE.md`/merged review section, and reversing its link
targets. Never reset the repository-wide dirty tree.

## Source hashes

| Milestone | Source | SHA-256 | Destination |
|---|---|---|---|
| M0 | `CONCEPTS.md` | `7ef342562ab4933c70546af0bc009ffc7d78a80732d81a41f1fec987e9ea8b8e` | `REFERENCE.md` |
| M0 | `TOOLS.md` | `b9f7d1276cfe16af64cd3dac58a61f14efdb41e320e36f92e3ddd4e975a7479d` | `REFERENCE.md` |
| M0 | `RESOURCES.md` | `dbaf59e1643732b241ac5010089227c7459db82a24a3d6f6ead9f04d4184f8ae` | `REFERENCE.md` |
| M0 | `REVIEW.md` | `ca6eac0139150fc8adae36ce2a74430b085ef3a940f55fa98ac44b37ee61efd1` | `ACCEPTANCE.md#review` |
| M1 | `CONCEPTS.md` | `834c2bfeaaac18ae9494bd3045d4625a9ae01fbb477fb27deaf314d16d483599` | `REFERENCE.md` |
| M1 | `TOOLS.md` | `f759a82ddfa5502400640a8214e26d25e9703cc311bf5f67f90e73844285fcb1` | `REFERENCE.md` |
| M1 | `RESOURCES.md` | `09541379120cc7cefa9488b139d041d9f05bb1707f0b7496d95f38aae1d17a9b` | `REFERENCE.md` |
| M1 | `REVIEW.md` | `9199d0f80a32f8df8b60d8bc289d341ee723918178fff553aaf60d32784f8eed` | `ACCEPTANCE.md#review` |
| M2 | `CONCEPTS.md` | `96d8ba795c3010f7934e76ce33a86c27522699e63f57371982da91ea4fa746a7` | `REFERENCE.md` |
| M2 | `TOOLS.md` | `643b7cd45b8f2ac3af3221b75b59f5219394ebf1691134f0d1cd18d505e285a1` | `REFERENCE.md` |
| M2 | `RESOURCES.md` | `e506cb38b5651688efe9ef810bafc6adf433054197f841dc63fb2a23f5f92f8a` | `REFERENCE.md` |
| M2 | `REVIEW.md` | `f60e66ac5b536132b17a4a0bb02e4dc698269991bc505b5f589871feca6a214e` | `ACCEPTANCE.md#review` |
| M6 | `CONCEPTS.md` | `a172699a6c14af900ca397194b74f81931b5c6743be18f26d50064d9da606246` | `REFERENCE.md` |
| M6 | `TOOLS.md` | `2276094fe1c7f28d5d2e0770491dbd60ff2a92c63aaa3e3c492264f4fd5cb908` | `REFERENCE.md` |
| M6 | `RESOURCES.md` | `c16d29b25c5ca6f4e39da29b0a9d7540357f6595906a4aa5e16d1dac2379148b` | `REFERENCE.md` |
| M6 | `REVIEW.md` | `febf145a4b143be9d902e5f4e93d36c89ef49aa7be236c96491699981d5d2889` | `ACCEPTANCE.md#review` |
| M9 | `CONCEPTS.md` | `2f371a1b167764e801dcff021eec180daa4251d34627a03c58289c9b72105f40` | `REFERENCE.md` |
| M9 | `TOOLS.md` | `7e465807b5e52c13d301fa9eed3ecb9e98e2d9a8a242d073dd71774291a22013` | `REFERENCE.md` |
| M9 | `RESOURCES.md` | `db54956e11344b6867513a951a685ae1a9a223d543abd9183c876c79cc7d1f4c` | `REFERENCE.md` |
| M9 | `REVIEW.md` | `4914d26a914f9fa6fc3d1fb2eba43c28314fe33edfb026e31719ce3cf084bc8c` | `ACCEPTANCE.md#review` |
| M3 | `CONCEPTS.md` | `b0ba715893bbe850c5b84c5e141475e417d83ed47aeb5228d35459aae74e5201` | `REFERENCE.md` |
| M3 | `TOOLS.md` | `99aad59417373099f52f5086b12466bb2f1e9944b47973bb70dfb14c48f525fd` | `REFERENCE.md` |
| M3 | `RESOURCES.md` | `016ecd3a6dad72f17fd0b9b3da30b507e59de492a2f174872420c8909e381ec4` | `REFERENCE.md` |
| M3 | `REVIEW.md` | `db87b3856ae71a1105a6c265f3a70e4589ae7ddfbb5c7016f4330ac37d584800` | `ACCEPTANCE.md#review` |
| M4 | `CONCEPTS.md` | `f05b7f86f46fddc6a44f28fdf2115e5cdf7764799aba83a60f902d24b0555642` | `REFERENCE.md` |
| M4 | `TOOLS.md` | `3adf66d4dfa864cbeaf633f320d3cbf87acbec757f1eaffb0ad2ce810dad8ee9` | `REFERENCE.md` |
| M4 | `RESOURCES.md` | `4eb9b362775e366df4b0547d3a0118e8f0ebe7b7d37d672d48e41fbb214cbd7b` | `REFERENCE.md` |
| M4 | `REVIEW.md` | `bf21c070341643b5172c873e0fbb3576828b732fcddfac345cf3cce2a07cf86b` | `ACCEPTANCE.md#review` |
| M5 | `CONCEPTS.md` | `10f31ae66dd0506c773c0cb0e433f337a9b7df6c8ef4fb917e94a11e628b101b` | `REFERENCE.md` |
| M5 | `TOOLS.md` | `09185e6db1766f23ea019e5f77946ab4465a00ab364114ad19284c5bed5440e7` | `REFERENCE.md` |
| M5 | `RESOURCES.md` | `d74f62c28efd61ae89c0e1d0870575e4b9ac4368ae3faf052ca38fc1c14da917` | `REFERENCE.md` |
| M5 | `REVIEW.md` | `696f26516398c659fa97774016733ee6c40ad1431517a52f293c0bae62caef8e` | `ACCEPTANCE.md#review` |
| M7 | `CONCEPTS.md` | `d2acd9c89d1c895dbbbeb19bd6364681293d71de311e977af087586ca53eb355` | `REFERENCE.md` |
| M7 | `TOOLS.md` | `c5cef6f1bdecf831fa196d71f6e470c2f0d71b33946223657a5b1c06778fd365` | `REFERENCE.md` |
| M7 | `RESOURCES.md` | `ccfe17ae6554a433f73393fd12b83b828bbcea3a19c914d202bd76a63bd3443b` | `REFERENCE.md` |
| M7 | `REVIEW.md` | `24f7685279823a72ceabea0c5df28fc77880e74c9f85cf68b201fc4aa6451d2b` | `ACCEPTANCE.md#review` |
| M8 | `CONCEPTS.md` | `773612f07667db1f126e20fcbe71ad55affa77ee1338b700244445a82fad02ec` | `REFERENCE.md` |
| M8 | `TOOLS.md` | `e76507a30d93e362fd5c02e89cd0762ddbf3f0e522023544a02edfdeef7ac0fd` | `REFERENCE.md` |
| M8 | `RESOURCES.md` | `c9c549ef5c83cffd137569fb230d745b148f23025fbcd2cd0b8950ffb86a43cf` | `REFERENCE.md` |
| M8 | `REVIEW.md` | `d28953972be78150613d3d252e8c49673752d3917284fc7afb8258fabaded5d7` | `ACCEPTANCE.md#review` |
| M10 | `CONCEPTS.md` | `a0d39be493cae003b8463c43d871b593b0079c28e67f709876a624fed3510eca` | `REFERENCE.md` |
| M10 | `TOOLS.md` | `17cc1a6d749af3617e420ba89e6619b93cf3740c8e26bbf6a6dbf701e477dd8b` | `REFERENCE.md` |
| M10 | `RESOURCES.md` | `c0a8f66ffda9fad0e19d5c606efdb070a1982350415d4248be7f11c35620140e` | `REFERENCE.md` |
| M10 | `REVIEW.md` | `6e60a3b96fdcfaa19df5e99ef839feea2b817283b8605f7e241fc58932f7bc64` | `ACCEPTANCE.md#review` |

## Pilot validation

On 2026-09-15 the transitional validator reported five new and six old
milestones with all 58 traces intact. Catalog passed eight tests plus lint,
format, strict types, HTML/form/API/OpenAPI, and live startup checks. POS,
Ecommerce, Booking, and Social passed their Python 3.13 locked gates; isolated
PostgreSQL runs passed 4, 20, 5, and 6 tests respectively. The Catalog health,
Booking final-seat, and Social query-budget failures exited non-zero for their
intended reasons and the Catalog reset returned eight tests to green.

The pilot decision is **ROLL OUT**. This authorizes the remaining local BF
migration only. It does not establish hosted, provider, deployment, or named-
human evidence.

## Rollout and closeout audit

The reviewed rollout consolidated all eleven milestones. The manifest has 44
source rows: four superseded files for each milestone. An index-object audit
recomputed every SHA-256 hash and confirmed every source body in its declared
`REFERENCE.md` or `ACCEPTANCE.md#review` destination. The root presents one
four-column learner route; every milestone presents exactly four predictable
choices; active PLAN/TODO/USABILITY and analysis files are concise indexes while
their complete prior contents remain beside this manifest as dated history.

The BF6 validator and its 42 controlled failures protect 11×4 structure, 58
traces, outcome titles, controller/reference structure, Core/Stretch, links,
Python/Air declarations and locks, Air/FastAPI composition, OpenAPI exclusion,
earned HTMX/SSE, no internal HTTP or second frontend runtime, POS Python 3.13
image pinning, provenance, safety, and external-evidence separation. Full local
runtime results are recorded in the current [USABILITY](../../../../USABILITY.md#2026-09-15-bf6-local-closeout).
Rollback remains a slice-specific reconstruction from these source hashes and
history files; never reset the dirty repository wholesale.
