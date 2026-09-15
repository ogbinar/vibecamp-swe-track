# Whole-repository persona review

Date: 2026-09-13  
Review mode: read-only inspection of the current working tree, which contained
modified and untracked curriculum work and was not a stable reviewed commit  
Primary question: **Can a career shifter with basic Python knowledge use this
course independently with minimal instructor support?**

## Verdict

Not consistently yet.

The repository is an unusually strong engineering curriculum specification. It
has a coherent capability arc, disciplined tool choices, concrete business
failures, reproducible entry exercises, and serious quality standards. The M0
experience is genuinely guided. After M1, however, the course increasingly asks
the learner to invent the assignment as well as solve it.

The recurring gap is between a high-level instruction such as “rebuild the
reservation invariant in PostgreSQL” and the next independently executable
action. A solo learner often lacks one or more of these:

- a fixed product contract;
- a declared starting architecture;
- a named file or extension point;
- a supplied failing test or bounded harness contract;
- an intermediate green checkpoint;
- a precise evidence destination;
- a reset or escalation path.

The panel agrees that adding finished solutions would weaken the course. The
needed change is **more process and contract scaffolding, not solution code**.

## Panel and review method

Eight personas reviewed the same repository surface.

| Persona | Primary lens | Decision weight |
|---|---|---:|
| Career shifter | Can I understand and perform the next action alone? | 25% |
| Instructional designer and technical writer | Is the learning sequenced, readable, and appropriately scaffolded? | 20% |
| Senior FastAPI/backend engineer | Are contracts, boundaries, tests, and architecture technically coherent? | 15% |
| Data specialist moving into software engineering | Does the course bridge data skill into application, API, and operational ownership? | 10% |
| Application-security reviewer | Are security choices justified, safe to exercise, and objectively tested? | 10% |
| Reliability and operations engineer | Can the learner deploy, observe, fail, and recover the product honestly? | 10% |
| Skeptical hiring manager | Does the completed work demonstrate credible employable capability? | 5% |
| Small-business product owner | Does the engineering work solve a recognizable customer problem? | 5% |

Each persona inspected:

1. learner entry, navigation, workflow, progress, glossary, stack, and gates;
2. every M0–M10 milestone and its seven-file contract;
3. all five project launch kits, requirements, source modules, tests, and failure
   harnesses;
4. challenge governance and every reusable template;
5. GitHub issue/PR/Actions workflow, repository validator, planning, and
   maintenance material.

Severity is used consistently:

- **Blocker:** the learner cannot make a justified choice or satisfy the gate
  from the supplied contract.
- **High:** instructor intervention or substantial guesswork is likely.
- **Medium:** progress is possible, but avoidable friction or weak evidence is
  likely.
- **Low:** polish or defense in depth.

Static-review confidence is high for document, contract, dependency, and
navigation findings. Confidence is medium for actual learner behavior until a
target career shifter completes a cold test. Passing starter commands and the
structural validator are not substitutes for that observation.

## Shared learner-experience rubric

All personas used the target learner from `USABILITY.md`: basic Python and Git,
some SQL exposure, limited professional engineering experience, studying alone
in short sessions. Scores mean:

- **1:** likely blocked;
- **2:** substantial instructor help required;
- **3:** workable with repeated ambiguity or independent research;
- **4:** independently usable with occasional reference lookup;
- **5:** exceptionally clear and self-correcting.

| Dimension | Score | Panel explanation |
|---|---:|---|
| Readability | 3/5 | Predictable headings help scanning, but later Concepts, Review, and Acceptance files compress many advanced ideas into dense sentences. |
| Clarity of instructions | 2/5 | Starting commands are usually precise; Core implementation work relies on broad verbs without files, intermediate checks, or expected observations. |
| Learning progression | 3/5 | The conceptual progression is excellent, but implementation scaffolding drops sharply at several product transitions. |
| Terminology | 2/5 | Headline terms are defined, but supporting vocabulary often appears in clusters before it is taught. |
| Career-shifter accessibility | 2/5 | Business scenarios are familiar; system design, security, concurrency, deployment, and operations assumptions are not. |
| Navigation | 3/5 | Root-to-M0 and milestone-to-next navigation are clear; the route through the seven milestone files is rarely step-by-step. |
| Context | 4/5 | Concrete failure consequences consistently explain why engineering work matters. |
| Actionability | 2/5 | Acceptance intent is strong, but many items lack exact commands, edit locations, supplied fixtures, and recovery. |
| Cognitive load | 2/5 | Several milestones combine too many new concepts, tools, decisions, and evidence duties at once. |
| Self-sufficiency | 2/5 | The learner can begin independently but is likely to need design help after M1. |

**Overall: 25/50, or 2.5/5.** Minimal-instructor release should require at
least 4/5 in every dimension plus observed human completion of high-risk
transitions.

## End-to-end transition map

| Transition | Panel verdict | Primary reason |
|---|---|---|
| Repository → M0 | Needs one high-priority repair | The quickstart works, but repository ownership is introduced after the upstream clone. |
| M0 → M1 | Mostly ready, with alignment defects | The contract is concrete; work slicing and test/brief/acceptance agreement need repair. |
| M1 → M2 | Needs work | PostgreSQL starts, but the learner must invent the API, models, failures, and proof route. |
| M2 → M3 | Needs work | The product's checkout, state, and arithmetic contract is underspecified. |
| M3 → M4 | Needs work | The learner must invent the awkward change and architecture defect. |
| M4 → M5 | Blocked | Ecommerce lacks the persistence substrate and client context required by Core. |
| M5 → M6 | Blocked by M5; M6 harness partial | Provider uncertainty is demonstrated, but the graded transport/webhook contract is broader. |
| M6 → M7 | Needs work | The outbox symptom is supplied; durable schema, worker lifecycle, and operating path are not. |
| M7 → M8 | Blocked | An in-memory race demonstrator must become an unspecified PostgreSQL/FastAPI product. |
| M8 → M9 | Blocked | An in-memory call-count example must become an unspecified database, load, cache, and realtime system. |
| M9 → M10 | Blocked for minimal-support use | The capstone assumes external infrastructure and bundles most production disciplines. |

## Coverage ledger

The review covered every repository component. This table records the role of
each area and the panel's dominant concern.

| Repository area | Components reviewed | Dominant concern |
|---|---|---|
| Course entrance | `README.md`, `CONTRIBUTING.md` | The learner clones upstream before being told to create an owned repository. |
| Roadmap and state | `CURRICULUM.md`, `PROGRESS.md` | The roadmap is clear, but the concept matrix is dense and the resume field names disagree. |
| Standards | `STACK.md`, `QUALITY-GATES.md`, `GLOSSARY.md` | Technically strong; vocabulary and universal gates are heavy for early learners. |
| Learner-experience governance | `USABILITY.md` | Automated structure simulation is presented more confidently than human evidence supports. |
| Maintenance | `PLAN.md`, `TODO.md`, `AGENTS.md` | Useful governance, but visible root-level maintainer material increases learner-facing clutter. |
| Challenges | `challenges/README.md`, every milestone `CHALLENGE.md` | The promised `PROVIDED` versus `YOU BUILD` distinction is not consistently applied. |
| Milestones | M0–M10, seven files each | Consistent structure; later README “ordered work” is usually one compressed paragraph. |
| Catalog | app, settings, models, tests, M1 contract, challenge controller, examples | Strongest complete learner route; M1 contract and lesson have alignment gaps. |
| POS | FastAPI shell, PostgreSQL, Compose, Alembic, reset script, tests, requirements | Good infrastructure baseline; product/API/failure contracts remain too open. |
| Ecommerce | FastAPI shell, security brief, provider fake, outbox lab, tests | Required persistence/authentication substrate and client context are missing. |
| Booking | in-memory inventory, barrier race, tests | Useful demonstration, but not a database-backed application launch kit. |
| Social | in-memory graph/feed, skewed seed, query-count test | Useful demonstration, but not a PostgreSQL/performance/realtime launch kit. |
| Templates | ADR, requirements, evidence, diagnostic, transition, data lifecycle, incident, complexity, portfolio | Rigorous but too generic when introduced; early learners need prefilled applicable subsets. |
| GitHub workflow | issue forms, PR template, Actions | Authentic workflow, but the PR template treats every PR like a final gate review. |
| Automation | `scripts/check_curriculum.py`, repository-hygiene workflow | Proves structure and starter health, not semantic completeness or learner self-sufficiency. |

## Persona 1 — Career shifter

### What works

- The first screen states who the course is for and provides a copyable command
  block with an expected result.
- Familiar products make the capability progression understandable.
- M0 names files, commands, expected failures, recovery, evidence, completion,
  and the next milestone.
- Every milestone has a visible Why, starting checkpoint, Done, Recovery, and
  Next section.
- The progress dashboard provides a potentially useful pause/resume location.

### Concerns by repository section

| Section | Career-shifter reaction | Need |
|---|---|---|
| Root quickstart | “I cloned the course, but later it says I need another repository. Which one contains my work?” | Create the learner-owned repository before the first clone or document an explicit conversion path. |
| Supported environment | Commands assume Unix syntax such as `cp`, `curl`, inline environment variables, and later SSH/SCP, but the front door does not declare Linux, macOS, or WSL2. | Declare supported environments before Start now or provide tested PowerShell equivalents. |
| GitHub workflow | `origin`, `upstream`, SSH, `git add -p`, rebase, PRs, Actions, and annotated tags arrive close together. | Introduce one Git operation when it becomes necessary; define every remote term before the command. |
| Curriculum map | The roadmap is motivating; the 58-row matrix looks like required reading. | Label the matrix as reference and keep it out of the required start route. |
| Quality gates | The standards sound professional, but the learner cannot tell which of ten global checks matter in M0. | Separate five universal checks from milestone-conditional security, data, deployment, and recovery checks. |
| M0 | “I can follow this.” | Use M0 as the presentation template for later milestones. |
| M1 | “Which endpoint and file do I implement first?” | Provide named vertical slices, exact file suggestions, one narrow red test, and one expected green result per slice. |
| M2 | “Do I invent the tables, API endpoints, migration failure, and N+1 case?” | State what is supplied and what the learner creates; add bounded product/API examples and failure activators. |
| M3 | “What exactly does checkout accept and return? What arithmetic order is correct?” | Publish state-transition, arithmetic, request, response, and failure examples. |
| M4 | “What is the exact promotion change, and how badly should I implement it first?” | Supply a stakeholder change brief and a known awkward baseline or change-scatter exercise. |
| M5 | “Where is the database? Is the client a browser or mobile app? Should I copy POS?” | Supply neutral persistence infrastructure and declare the client/trust scenario. |
| M6 | “Does the fake represent HTTPX behavior, or must I replace it? How is the webhook signed?” | Define the adapter contract, signed payload fixture, timeout classes, and incremental tests. |
| M7 | “Which job states and columns do I need? How do I run two workers?” | Supply a bounded job-state contract, worker entrypoint skeleton, launch/kill commands, and metric format. |
| M8 | “Where do the PostgreSQL app, endpoints, models, migrations, and tests go?” | Provide a database-backed booking application skeleton without the race solution. |
| M9 | “Is this an API, benchmark, or both? Is Redis actually optional?” | Define the deliverable and resolve the cache-policy contradiction. |
| M10 | “Do I need to buy a server? Who configured TLS, secrets, directories, and backups?” | State prerequisites near the course entrance and provide a sanctioned local rehearsal plus an optional real-target claim. |
| Templates | “Which fields apply now?” | Provide milestone-specific prefill instructions and mark non-applicable fields explicitly. |
| Stuck path | Generic hints eventually send the learner to whole files or documentation. | End every hint ladder with a focused diagnostic command and a prefilled help-issue format. |

### Career-shifter conclusion

The learner can confidently begin and complete much of M0. M1 introduces
avoidable design ambiguity. From M2 onward, the learner can understand the
desired engineering outcome but cannot reliably determine the next 30–120
minute action without outside help.

## Persona 2 — Instructional designer and technical writer

### What works

- The course is problem-first and uses realistic consequences rather than a
  tool-topic syllabus.
- The maturity arc spirals concepts through increasingly difficult products.
- Core and Stretch are visibly distinguished.
- M0 demonstrates worked-example fading well: a supplied green state, safe
  breakage, diagnosis, restoration, and evidence.
- Resource lists are concise and introduced near relevant problems.

### Concerns by repository section

1. **Later “ordered work” is not ordered.** M2–M10 usually compress a full
   milestone into one paragraph. The learner cannot see session boundaries,
   prerequisite checks, or the next smallest action.
2. **Challenge bullets bundle learning objectives.** One checkbox may require a
   failure harness, architectural decision, implementation, concurrency run,
   operational observation, explanation, and evidence.
3. **Concept files are expert summaries.** Several contain two or three
   noun-heavy paragraphs instead of short problem → example → term → rule cards.
4. **Review files overload retrieval.** M10 asks the learner to explain roughly
   a dozen advanced ideas in one paragraph. One question per bullet would make
   uncertainty diagnosable.
5. **The course jumps from modeling a symptom to building a system.** Booking
   and social demonstrate a race and N+1 shape, but there is no gradually faded
   path into the required database application.
6. **Evidence is introduced before relevance is clear.** The generic evidence
   template exposes migration, security, rollback, release, and lifecycle fields
   during M0.
7. **No small-session contract exists.** A learner studying for a few hours
   needs explicit “safe to stop here” and “resume by running this” boundaries.

### Instructional needs

- Give every milestone 3–6 numbered work blocks.
- Make each block independently checkable and resumable.
- Limit new decision-driving terms to a small set per block.
- Turn concepts into example-first cards linked to the exact challenge.
- Use sub-IDs such as `C2.1` and `A2.1` when a challenge contains several
  observable behaviors.
- Identify `PROVIDED` and `YOU BUILD` artifacts before the learner searches.
- Give a worked evidence example for each new evidence type, not each feature.

## Persona 3 — Senior FastAPI/backend engineer

### What works

- The minimal synchronous FastAPI/SQLAlchemy/PostgreSQL architecture is a sound
  teaching default.
- The course correctly places transactions at the use-case boundary and rejects
  auto-committing repositories and ceremonial layers.
- FastCRUD, pagination packages, Redis, Taskiq, async database access, and
  observability products require evidence before adoption.
- The M1 black-box contract and M0 application factory are strong starting
  patterns.
- PostgreSQL—not SQLite—is correctly required for database-specific behavior.

### Technical concerns and needs

| Component | Finding | Severity | Improvement |
|---|---|---:|---|
| M1 contract | The lesson tells the learner to add an OpenAPI check that is already supplied. Several acceptance cases are absent from the published contract tests. | High | Reconcile brief, challenge, test names, error envelopes, and acceptance IDs. Mark supplied versus learner-authored tests. |
| M1 compatibility fault | The activator changes the contract test's expected field from `sku` to `title`; it changes the oracle rather than the provider's public behavior. | High | Mutate the application/OpenAPI boundary while keeping the consumer contract stable, so the learner diagnoses a real compatibility regression. |
| POS requirements | The persistence questions are useful, but API endpoints and error translation are not specified while A1 grades API behavior. | High | Add request/response/error examples without prescribing schema design. |
| POS engine lifecycle | `/ready` creates a new SQLAlchemy engine on every request. | Medium | Supply a lifespan-owned engine/session seam and make the metadata wiring point explicit. |
| Alembic baseline | `target_metadata = None` does not show the intended learner extension point for typed mappings/autogeneration. | Medium | Add a named TODO and documented metadata import seam. |
| M3 | Checkout, payment, receipt, stock, void, refund, state, and rounding behavior lack a fixed product contract. | High | Add state tables and Given/When/Then arithmetic examples. |
| M4 | The learner must invent the awkward change and forbidden dependency. | High | Supply the requirement change and a boundary-test harness, not the refactor. |
| Ecommerce | The starter lacks SQLAlchemy, Psycopg, Alembic, PostgreSQL, and the persistence lifecycle needed by M5–M7. | Blocker | Add a green neutral database baseline and migration/reset path. |
| M6 fake | String results demonstrate uncertainty but do not cover connect/read/total timeout or signed raw webhook requirements. | High | Supply an explicit provider port and transport-level fixtures matching acceptance. |
| M7 | No schema/state contract, worker skeleton, claim loop, or commands exist for the required database-backed worker. | High | Supply extension points and deterministic competing-worker/kill harnesses. |
| Booking | The in-memory thread example is a good symptom demonstration but not the required PostgreSQL/FastAPI lab. | High | Add neutral database/API/migration scaffolding and preserve the broken invariant as the learner task. |
| Social | The call counter demonstrates N+1 shape but cannot teach SQL plans, indexes, pagination, Redis, or transports without a large rebuild. | High | Add a PostgreSQL/FastAPI data path, seed command, query capture, and load-harness shell. |
| M10 | The reference target prescribes an API and worker although the M4 POS lineage has not earned a worker. | Medium | Make the worker conditional or add one bounded POS obligation requiring it. |
| M10 release path | README builds locally and transfers an image archive, while C3/A3 require CI to build the exact deployed artifact. | High | Choose one canonical artifact path and make its provenance evidence consistent from CI through deployment. |
| CI | It runs starter checks, but later milestone instructions do not show how the learner evolves CI to run new gates. | High | Add milestone-specific CI modification checkpoints and expected job names. |

### Backend-engineer conclusion

Leaving architecture choices open is valuable only after external behavior,
starting boundaries, and proof have been fixed. The repository should constrain
the problem more precisely while continuing to leave implementation decisions
to the learner.

## Persona 4 — Data specialist moving into software engineering

### What works

- M2 explicitly links tables, constraints, queries, indexes, and migrations to
  product truth.
- The course distinguishes boundary validation from database invariants.
- Query plans, N+1 diagnosis, transaction ownership, data lifecycle, tenant
  isolation, and restore verification broaden the learner beyond analytics SQL.
- The data-specialist lens correctly keeps the same Core gates.

### Concerns and needs

- M1 may be the first time this learner owns HTTP semantics, serialization, and
  public compatibility. These need examples before the contract test becomes an
  assessment.
- M2 asks for session lifetime, rollback behavior, API error translation, N+1
  guards, and migration recovery in addition to schema design. The familiar SQL
  portion may hide the unfamiliar application responsibilities.
- `repository`, `session`, `flush`, `use-case boundary`, `backfill`, and
  `query plan` need concrete lifecycle diagrams or examples.
- M3 should explicitly trace one checkout from request through service,
  transaction, database rows, commit, and response.
- M5–M7 require durable security and workflow tables, yet no ecommerce database
  continuity exists.
- M9 should distinguish a database query plan from the in-memory call-count
  analogy and provide a stable database seed/reset process.
- M10 data deletion conflicts with append-only audit and backup retention. The
  course needs a fixed example showing policy trade-offs rather than expecting
  the learner to invent them.

The data specialist asks for a repeated **request → application rule → database
operation → commit → response → evidence** trace in M2, M3, M5, M7, M9, and M10.

## Persona 5 — Application-security reviewer

### What works

- Authentication, authorization, role permissions, object ownership, and state
  transitions are correctly separated.
- The course rejects home-grown password cryptography and requires negative tests.
- Security scenarios are documentation-only and synthetic rather than callable
  vulnerable endpoints.
- Logs and evidence are repeatedly required to be sanitized.
- M10 correctly treats tenant isolation as a cross-boundary property.

### Concerns and needs

| Area | Security concern | Severity | Need |
|---|---|---:|---|
| M5 client boundary | Cookie versus JWT must be selected from a client/trust boundary that the requirements never declare. | Blocker | Declare one first-party browser, mobile, or external-client scenario and its constraints. |
| M5 substrate | Secure persistence, session lifecycle, revocation, and migrations cannot be implemented against the supplied shell without inventing infrastructure. | Blocker | Supply neutral persistence and configuration seams. |
| Vulnerability exercises | Learners are asked to seed plaintext/fast hashes, fixation, CSRF gaps, permissive JWT validation, and leaked secrets without a supplied test-only mutation mechanism. | Medium | Provide disabled test-only activators plus CI guards preventing production exposure. |
| M6 webhooks | The fake has event IDs, sequence, and body but no signing timestamp/account fixture matching the gate. | High | Supply signed raw-body examples, replay-window rules, and constant-time verification tests. |
| POS reset | Reset authorization relies partly on the database URL containing `vibecamp_pos`. | Medium | Parse and display the exact target; require a strict local/course allowlist and target-specific confirmation. |
| GitHub Actions | Workflow permissions are read-only, but third-party actions use moving major-version tags. | Medium | Pin external actions to reviewed commit SHAs and automate update review. |
| M10 tenancy | “Across every data path” is correct but too broad to implement unaided. | High | Supply a two-tenant attack matrix covering reads, writes, lists, jobs, cache, logs, exports, and admin paths. |

The security reviewer opposes adding realistic callable vulnerabilities. The
instructional designer agrees and recommends deterministic, isolated test
mutations that are impossible to enable in normal runtime configuration.

## Persona 6 — Reliability and operations engineer

### What works

- The course treats timeout as uncertainty, not simply an exception.
- M7 correctly rejects exactly-once claims and starts durability with persisted
  intent.
- Health and readiness are distinguished.
- M10 connects immutable artifacts, migrations, readiness, rollback, telemetry,
  restore testing, incident response, and runbooks.
- Compose is accurately described as a bounded runtime tool, not a complete
  production platform.

### Concerns and needs

1. Root prerequisites mention Git and uv, but later mandatory work requires
   Docker, PostgreSQL, SSH/SCP, an authorized Linux host, TLS, secrets, and
   backups.
2. M6 lacks a complete transport boundary for the timeout and webhook claims it
   grades.
3. M7 lacks executable worker start/stop/kill/replay commands, a job-state model,
   and an observable metric contract.
4. M8/M9 lack the database and runtime environment needed to observe real locks,
   plans, pool behavior, cache failure, and connection lifecycle.
5. M10's release commands assume remote directories, Compose services, TLS,
   secret custody, and backup systems already exist.
6. A real external host introduces money, account, network, and security
   prerequisites. These must be disclosed before M10.
7. The learner needs a local two-environment deployment rehearsal that teaches
   build → migrate → readiness → promote → reject → restore. Real-host evidence
   can remain necessary only for the strongest production claim.
8. The M10 runbook must name ownership, detection signal, first safe action,
   verification, escalation, and rollback/roll-forward boundary.

## Persona 7 — Skeptical hiring manager

### What works

- The curriculum targets engineering judgment rather than framework trivia.
- Failure reproduction, diagnosis, regression proof, trade-offs, and recovery
  are stronger portfolio signals than a collection of CRUD applications.
- The complexity-rejection record demonstrates restraint.
- The M4/M10 case-study checkpoints encourage a coherent professional narrative.

### Concerns and needs

- If the assignment is underspecified, reviewers cannot distinguish deliberate
  learner judgment from accidental divergence.
- Generic evidence templates may produce large collections of artifacts without
  a clear story.
- The PR template asks for final-gate evidence on every PR, encouraging artificial
  paperwork rather than realistic incremental development.
- Cold-review claims should identify a human or explicitly say solo
  fresh-context; automated simulation should not appear equivalent.
- The final portfolio needs one short reader path: requirement → design choice →
  failure → diagnosis → fix → proof → operational limitation.
- Each milestone should state which two or three artifacts are worth showing an
  interviewer and which evidence is merely internal course bookkeeping.

The hiring manager would prefer fewer, better explained artifacts over eleven
large evidence folders with weak narrative.

## Persona 8 — Small-business product owner

### What works

- Catalog, checkout, inventory, orders, reservations, feeds, and tenant safety
  are understandable business domains.
- The Why sections explain meaningful harm: missing stock, duplicate charges,
  lost fulfillment, oversold seats, slow feeds, data leakage, and failed recovery.
- The minimal-stack policy limits cost and operational burden.

### Concerns and needs

- M2 specifies data questions but not the staff/customer interaction that
  creates them.
- M3 does not declare tax, rounding, refund, void, and receipt behavior tightly
  enough for the owner to approve the result.
- M4 needs a concrete changed requirement with a decision owner and business
  reason.
- M5 identifies actors but not the actual client experience or account-recovery
  expectations.
- M6 should state what the customer sees while payment truth is unknown.
- M7 should state how delayed fulfillment is communicated and when support
  intervenes.
- M8 needs explicit hold duration, expiration, winner/loser behavior, and
  cancellation expectations.
- M9 needs a user-facing performance target and a precise realtime requirement
  before Redis or WebSockets are considered.
- M10 asks the learner to define the customer and deployment scenario. A fixed
  reference customer should be supplied first so assessment remains comparable.

The product owner wants fewer architecture nouns and more Given/When/Then
examples with observable customer and operator outcomes.

## Component-by-component panel discussion

### Root learner route

**Agreement:** [README.md](../../../../README.md) is now a credible course home. It states
the audience, outcome, product progression, first command, expected result, and
next milestone.

**Concern:** it first clones the upstream curriculum, while
[CONTRIBUTING.md](../../../../CONTRIBUTING.md) later creates a second learner-owned clone.
The career shifter sees two workspaces; the hiring manager worries evidence will
land in the wrong repository; the operations reviewer notes that CI cannot run
in a repository the learner cannot push.

**Need:** one path only:

1. create a repository from the template;
2. clone the owned repository;
3. verify `origin` in plain language;
4. run the catalog baseline;
5. add `upstream` only when updates become relevant.

Replace “keep all branches disabled” with GitHub's actual control: leave
**Include all branches** unchecked.

Declare the supported shell/platform before the command block. The current
course has only been simulated on Linux, while active instructions use Unix
commands and environment syntax. Add a just-in-time “needed now / needed later”
map for GitHub authentication, Docker, PostgreSQL, and the M10 deployment target.

### Curriculum, progress, glossary, stack, and gates

**Agreement:** [CURRICULUM.md](../../../../CURRICULUM.md) provides an excellent product and
capability map. [STACK.md](../../../../STACK.md) contains disciplined engineering choices.
[GLOSSARY.md](../../../../GLOSSARY.md) is a useful fallback, not a substitute for first-use
teaching.

**Concerns:**

- The concept matrix is valuable for maintainers but intimidating in the primary
  learner roadmap.
- `PROGRESS.md` names “Last validated reference / date,” while its pause rule
  tells the learner to update “last green tag/commit.”
- The universal definition of done presents early learners with security, data,
  migration, rollback, release, and cold-review duties even when several are not
  applicable.
- Later concept files use professional terms absent from local term blocks and
  the glossary.

**Needs:** label the matrix as reference, align progress terminology, show one
filled synthetic pause/resume example, and divide quality gates into universal
and milestone-conditional sections.

Two glossary collisions need direct correction:

- `Port` is defined only as an architectural interface, while beginners first
  encounter network port 8000. Define **network port** separately and delay the
  architecture meaning until adapters are taught.
- `Idempotent` is described as “safe to repeat,” but HTTP **safe** has its own
  read-only semantic meaning and M1 asks learners to distinguish them. Define
  both precisely and avoid using “safe” as the idempotency definition.

The root exclusion list also introduces Kubernetes, Kafka, CQRS, event sourcing,
Elasticsearch, and dependency-injection frameworks before the learner needs
those terms. The front door can simply say that advanced distributed
infrastructure is not required and leave the detailed list in `STACK.md`.

### M0 — Engineering Baseline

**Panel view:** strongest module and presentation reference.

- Career shifter: executable and recoverable.
- Instructional designer: good worked example and deterministic fault cycle.
- Backend engineer: application factory, typed settings, tests, and explicit
  public behavior are appropriate.
- Security/operations: safe synthetic faults and no secret-dependent setup.
- Hiring/product: first artifact is modest but explainable.

**Needs:** simplify early evidence fields, stage GitHub ceremony after the first
coding success, and ensure the owned-repository flow precedes learner work.

### M1 — Production-minded API Foundation

**Strength:** black-box tests preserve implementation freedom while making HTTP
behavior visible.

**Concerns:**

- The README says to add an OpenAPI check already present in
  `contracts/test_m1_contract.py`.
- The error envelope gives one complete example but not all required codes and
  messages.
- Blank identity, decimal precision, retirement reason, and some invalid paging
  cases are graded more broadly than the supplied tests specify.
- “Implement one behavior at a time” does not name the sequence or files.
- The compatibility activator changes the test expectation rather than the
  application's public output. That teaches diagnosis of a broken test oracle,
  not a provider compatibility regression.

**Need:** six vertical slices—create, retrieve/missing, replace, retire/retry,
list/page, compatibility—each with one red test, edit map, expected green result,
hint ladder, and evidence output.

### M2 — POS Persistence and Data Modeling

**Strength:** real PostgreSQL, Compose, Alembic, and explicit invalid-data cases
make persistence concrete.

**Concerns:** the learner must invent the API, mappings, migration failure,
backfill interruption, N+1 shape, and recovery evidence. A1 grades API error
translation without a published API contract. The README says A1–A4 in Evidence
but A1–A5 in Done.

**Need:** fixed endpoint examples, model extension points, a seeded legacy-data
migration fixture, a supplied query-count boundary, exact evidence bootstrap,
and consistent acceptance IDs.

### M3 — Transactions and Correctness

**Strength:** partial checkout and stock races clearly demonstrate why a
transaction matters.

**Concern:** checkout, payment, stock, receipt, void, refund, state, tax, and
rounding behavior are not sufficiently specified for independent implementation
or consistent assessment.

**Need:** a product state table, decimal examples, fixed API examples, explicit
transaction trace, deterministic two-sale harness, and one checkpoint after
each invariant.

### M4 — Maintainability, Testing, and Refactoring

**Strength:** change scatter is a better reason for boundaries than teaching
service/repository patterns as doctrine.

**Concern:** the learner must invent the awkward implementation, changed
promotion requirement, circular dependency, and test weakness. That requires
the judgment the milestone intends to teach.

**Need:** provide a concrete stakeholder change, a known awkward baseline or
bounded change-scatter target, and a failing import/boundary check. Leave the
refactor learner-owned.

### M5 — Secure Multi-user Ecommerce

**Panel verdict: Blocked as a minimal-support module.**

The starter has FastAPI and settings only. The gate requires database-backed
accounts, carts, addresses, orders, migrations, password hashing, sessions, and
authorization. The product brief names actors but not the client needed to
choose cookies or JWT.

**Need:** add neutral PostgreSQL/SQLAlchemy/Alembic infrastructure, database
readiness/reset, explicit module extension points, a declared first-party
browser or other client, complete endpoint/state contracts, isolated attack
tests, and staged identity → authorization → ownership → lifecycle blocks.

Resolve the state-language contradiction too: requirements define `fulfilled`,
while a security fixture and challenge use `shipped`. Publish one command-to-state
table and use it everywhere.

### M6 — Resilient External Integrations

**Strength:** timeout-before and timeout-after effects teach uncertainty well.

**Concern:** the provided fake does not model the full transport and signed
webhook contract graded by acceptance. The learner invents both the integration
contract and its repair.

**Need:** an explicit provider port, HTTP-style outcomes, connect/read/total
timeout fixtures, signed raw-body webhooks, retry-budget examples, customer-visible
unknown state, reconciliation command, and per-scenario recovery.

### M7 — Durable Background Processing

**Strength:** the after-effect/before-acknowledgement window is an excellent
demonstration of at-least-once execution.

**Concern:** Core expands immediately to outbox schema, competing workers,
leases, retries, poison handling, replay authorization, shutdown, metrics,
runbooks, and lifecycle review without incremental infrastructure.

**Need:** four blocks—lost in-process work, atomic durable intent, claim/replay,
operate/recover—with a job-state contract, worker skeleton, launch/kill commands,
stable clock/ID seams, and one metric per taught failure.

### M8 — Booking Concurrency Lab

**Strength:** the two-thread barrier makes the race deterministic.

**Concern:** a 29-line in-memory example with no runtime dependencies is followed
by a required PostgreSQL/FastAPI reservation system, holds, expiration,
cancellation, isolation, locking, multiprocess tests, and contention evidence.

**Need:** a neutral database-backed booking shell, fixed hold lifecycle and API,
initial migration, deterministic database race harness, strategy-comparison
sequence, and explicit retry/conflict contract.

Its Recovery section currently refers to a “documented course database” that the
booking project does not contain. Recovery must point to an actual supplied
database and reset command.

### M9 — Social Performance, Caching, and Realtime

**Strength:** stable query counts are a better first signal than noisy wall-clock
timing.

**Concern:** the in-memory analogy must be rebuilt into an unspecified database
API and load environment. Redis is both conditional and required to exercise.
Query optimization, pagination, caching, and realtime are bundled.

**Need:** a PostgreSQL feed shell, deterministic seed/reset, SQL capture and
query-budget test, defined feed and cursor semantics, reference workload, and
four separate blocks. Require a controlled Redis experiment while making
production retention optional—or make the entire cache gate conditional with an
equivalent no-cache proof.

### M10 — Production Multi-tenant SaaS Capstone

**Strength:** it names the real reasons correct features may still be unsellable.

**Concern:** tenancy, audit, observability, deployment, migrations, secrets,
TLS, backup, recovery, incidents, onboarding, export, deletion, support, and
portfolio work are combined. The commands assume an authorized host and remote
layout that were never established.

**Need:** fix one reference customer and deployment scenario, then stage:

1. tenant-safe sale and audit;
2. one user-impact observability question;
3. build, migrate, readiness, promote, and reject;
4. restore and incident response;
5. customer/operator handoff and portfolio review.

Provide a local two-environment rehearsal. Reserve the real-host claim for a
declared external prerequisite or an optional stronger production proof.

The canonical artifact story must agree with its own gate. The current README
builds locally and copies an image archive over SCP, while acceptance requires
the exact CI-built artifact. Write local archives under ignored `dist/`, record
a checksum, and either deploy the CI-produced digest or relax that claim.

### Project launch kits and source modules

#### Catalog

The panel considers the catalog a real launch kit: it has a working application,
configuration, typed responses, tests, failure controller, product contract,
and evidence examples. Needed improvements are confined to M1 alignment and a
clear file-by-file implementation route.

#### POS

The POS is a real infrastructure launch kit but not yet a guided product slice.
Improve engine/session lifecycle, Alembic metadata wiring, endpoint contracts,
failure fixtures, and reset safety. Keep business tables learner-owned.

The reset path should provide a literal course-only command, preview the parsed
host/database/user, and reject targets outside a strict allowlist before
dropping a schema. The current substring check is too weak for a course teaching
operational safety.

#### Ecommerce

The ecommerce directory is a symptom shell, not a sufficient M5–M7 launch kit.
Add neutral persistence and migration infrastructure, declare the client,
provide extension points, and align the provider/outbox fixtures with the
acceptance contracts. Do not add completed authentication or worker solutions.

#### Booking

The booking directory is a high-quality race demonstrator. Rename it honestly or
extend it into a database-backed launch kit. The present transition requires the
learner to invent too much unrelated setup.

#### Social

The social directory is a high-quality N+1 analogy. Rename it honestly or add the
database/API/load shell required by M9. Explain how the call counter maps to
actual SQL query capture.

### Challenges and templates

The challenge system promises every scenario will identify whether the fixture
is supplied or learner-created. M2–M10 instead repeat “activate or construct.”
Each challenge must explicitly use one of these labels:

- `PROVIDED — run this command; reset with this command`, or
- `YOU BUILD — create this bounded harness; it must produce this observation`.

Template needs:

| Template | Panel finding | Improvement |
|---|---|---|
| Entry diagnostic | Appropriate at M0 | Add direct remediation links for every failed item. |
| Evidence index | Professionally credible but broad | Provide milestone prefill and explicit N/A guidance. |
| Requirements | Good structure | Add Given/When/Then examples and decision owner. |
| ADR | Correctly limited to consequential choices | Include one small annotated example. |
| Complexity rejection | Strong course differentiator | Show one M4 example focused on a rejected base repository. |
| Data lifecycle | Valuable from M2 onward | Do not expose as a universal early requirement. |
| Incident/postmortem | Appropriate for M6/M10 | Add a short synthetic example separating facts from hypotheses. |
| Transition review | Useful for maintainers | Mark automated and human evidence as different statuses. |
| Portfolio case study | Strong hiring artifact | Add a ten-minute reader-path checklist and maximum recommended length. |

### GitHub workflow and automation

**Strengths:** read-only workflow permissions, locked environments, real
PostgreSQL smoke checks, consistent lint/type/test commands, issue templates,
and a structurally strict validator.

**Concerns:**

- The PR template requests final milestone evidence on every PR even though the
  course encourages several coherent PRs.
- CI tests starter baselines, not learner-created later contracts unless the
  learner knows how to extend it.
- M1 contract is collected but not run in the default workflow.
- External actions use movable major-version tags.
- The validator checks filenames, markers, link destinations, resource counts,
  and trace IDs. It does not prove contract agreement, atomic tasks, first-use
  definitions, command executability, prerequisite disclosure, or
  starter-to-Core feasibility.

**Needs:** distinguish working PR from milestone-gate PR, teach CI evolution in
the relevant milestone, pin actions, add semantic validator checks for stable
contracts, and describe validator success as structural—not learner readiness.

Add secret, dependency, and container scanning only when the corresponding
M5/M10 problem becomes active; do not burden M0 with the production toolchain.

### Governance and maintenance claims

[USABILITY.md](USABILITY-history.md) honestly says its latest score is an automated
documentation simulation, but then calls the repository self-service ready.
The target career-shifter review does not support that claim for M2–M10.

Use three independent statuses:

- `STRUCTURALLY READY` — files, links, traceability, and required markers pass;
- `STARTER VERIFIED` — supplied commands and intended failures run as documented;
- `HUMAN SELF-STUDY VERIFIED` — a target learner completes the transition without
  author intervention.

Do not close the final status from automated simulation.

## Cross-persona discussion and resolved tensions

### Freedom versus scaffolding

- **Backend/security view:** do not prescribe one architecture or reveal the fix.
- **Career-shifter/teaching view:** without fixed behavior and starting seams,
  the learner is designing the assignment rather than solving it.
- **Resolution:** specify behavior, initial state, failure trigger, proof, and
  extension locations. Leave internal decomposition and repair learner-owned.

### Professional rigor versus cognitive load

- **Hiring/operations view:** PRs, evidence, runbooks, migration records, and
  recovery proof are authentic.
- **Career-shifter view:** applying the complete ritual to every small change is
  overwhelming.
- **Resolution:** introduce artifacts progressively and distinguish working PRs
  from final gate PRs. Preserve final rigor.

### Concision versus readability

- **Maintainer view:** short files reduce repository size.
- **Teaching/data-shifter view:** compressed professional prose creates semantic
  density even when word count is low.
- **Resolution:** add short examples, timelines, and cards; do not add broader
  technology coverage.

### Real production evidence versus accessibility

- **Operations view:** Level C should not be claimed from a toy environment.
- **Career/product view:** a mandatory external host adds cost and hidden setup.
- **Resolution:** require a complete local deployment rehearsal for learning,
  disclose external prerequisites, and reserve a stronger live-production claim
  for evidence from an authorized real target.

## Consolidated prioritized improvements

### P0 — unblock independent progression

1. **Unify repository ownership before the first clone.**
2. **Repair M5 continuity:** neutral PostgreSQL/SQLAlchemy/Alembic substrate,
   client scenario, migration path, and extension points.
3. **Bridge M8 and M9 into their required stack:** database-backed application
   shells, migrations, deterministic DB tests, and named edit locations.
4. **Turn M1–M10 READMEs into numbered, resumable work blocks.** Every block
   must name purpose, supplied inputs, files, command, expected result, evidence,
   recovery, and stop point.
5. **Publish bounded product contracts and failure activators.** Start with M1,
   M2, M3, M4, M5, M6, M7, M8, M9, and the fixed M10 customer scenario.
6. **Resolve contract contradictions:** M1 OpenAPI/test coverage, M2 A-count,
   M8/M9 command wording, M9 Redis policy, and M10 worker/host assumptions.

### P1 — remove routine instructor dependency

7. Label every challenge `PROVIDED` or `YOU BUILD` and supply the corresponding
   invocation or harness contract.
8. Map every challenge sub-step to an atomic acceptance sub-step, command,
   expected observation, and evidence path.
9. Apply the first-use writing contract to all milestone concept and review
   files; prioritize M5, M7, M8, M9, and M10.
10. Split universal quality gates from conditional milestone gates.
11. Provide milestone-specific evidence bootstrap instructions and examples.
12. Add an escalation ladder: observation question → named file/boundary →
    focused command/reference → prefilled help issue.
13. Add explicit pause/resume checkpoints and one filled journal example.
14. Divide the PR template into working-PR and milestone-final sections.
15. Define and teach how learner CI evolves at each relevant milestone.

### P2 — strengthen trust and maintainability

16. Treat usability simulations as provisional until a target human completes
    the transition.
17. Extend the validator to detect README/Acceptance ID disagreement, missing
    challenge-form labels, broken anchors, missing command/evidence maps, and
    starter dependency contradictions where rules are stable enough to automate.
18. Pin third-party GitHub Actions to reviewed commits.
19. Strengthen the POS destructive-reset target check.
20. Separate or visually demote maintainer material from the learner's root path.

## Standard to apply during revision

Every active learner work block should use this contract:

```markdown
## Work block N — Observable business outcome

Required or optional: REQUIRED

Why:
One concrete customer or operator consequence.

Provided:
- exact starting files, fixture, or prior tag;

You create or change:
- exact likely file or extension point;
- observable behavior, not a prescribed internal solution.

Run from:
`projects/example/`

Command:
`uv run --locked pytest tests/path/test_behavior.py -q`

Expected before:
One named failure or observation.

Expected after:
One named passing behavior and preserved earlier behavior.

Evidence:
`evidence/MN/CN-short-name.md`

If blocked:
1. observation question;
2. named boundary/files;
3. one targeted reference or diagnostic command;
4. focused help-issue fields.

Safe stop point:
Commit when the narrow and regression suites are green. Record the next C/A ID
and last green commit in `PROGRESS.md`.
```

Terminology should follow this form:

> **Transaction — a group of database changes that must all succeed or all fail
> together.** For example, checkout must not save a receipt if reducing stock
> fails.

Replace ambiguous instructions with artifact, behavior, and proof:

- Avoid: “Implement authorization.”
- Prefer: “Before returning `GET /orders/{id}`, verify that the order belongs to
  the signed-in customer. Prove customer B receives `404` for customer A's order
  and that no row changes.”

Use one main action per checkbox, paragraphs of no more than three sentences,
expanded acronyms at first use, familiar business examples, and visible labels:
`REQUIRED`, `OPTIONAL`, `CHOOSE ONE`, and `DO NOT ADD YET`.

## Completion criteria for the improvement effort

The repository should not be described as independently runnable end to end
until all of the following are true:

- A learner creates one owned repository and reaches M0 without changing clones.
- Every milestone has numbered, resumable work blocks.
- Every Core challenge identifies supplied versus learner-built artifacts.
- Every Core acceptance item has an observable result and evidence route.
- M5, M8, and M9 start from the infrastructure their Core gates require.
- M1/M2/M9 contract contradictions are removed.
- M10 discloses and teaches its deployment prerequisites or supplies the approved
  local rehearsal path.
- The validator reports structural readiness without implying instructional
  readiness.
- At least one target career shifter completes repository → M0, M0 → M1,
  M1 → M2, M4 → M5, M7 → M8, M8 → M9, and M9 → M10 transition tests without
  author intervention; confusion and recovery are recorded.

Until then, the honest status is: **strong curriculum design, verified starters,
and incomplete end-to-end self-study scaffolding**.
