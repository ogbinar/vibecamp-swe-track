# M6 — Handle uncertain payments

[Course home](../../README.md) / M6

**Milestone 7 of 11 · M6**

## Business problem

A payment request times out. The provider may have completed the payment even
though your application received no answer. Treat that uncertainty as product state.

## Product objective

- **Product can:** customers and operators can see an unknown payment without unsafe repetition.
- **You will prove:** timeout, retry, webhook, refund, HTMX-fragment, and reconciliation evidence.

Follow the [integration contract](../../projects/ecommerce/specs/M6-INTEGRATION-CONTRACT.md).
Add one controllable payment client plus signed inbound payment webhooks.
Complete C1–C3 in the [challenge brief](#challenge-brief): simulate timeout-before-effect,
timeout-after-effect, duplicate/delayed webhook, bad signature, and conflicting
provider state. Define a retry budget before writing retry code.

Use fakes that expose the same `pay`/`refund`/`lookup` contract as the real
boundary. Local Core makes no real call. After local Core, one Stripe-like
sandbox experiment is required for the separate real-provider evidence claim,
but it needs explicit authority and never runs in CI. Do not hide uncertainty
behind an automatic retry loop.

From `projects/ecommerce/`, first run:

```bash
uv run --locked pytest tests/test_failure_harnesses.py -q
```

Expected: the supplied modes demonstrate a completed-but-timed-out payment,
429/503/malformed results, and duplicate/out-of-order webhook deliveries while
the suite remains green. Replace no assertion; integrate the fake behind your
adapter and add product-facing failure expectations.

## Start here

- **Gate:** [A1–A4 / B + contextual C](#core).
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[M6 preflight](../../projects/ecommerce/README.md#m6-preflight-after-completing-m5), then return to the saved block; first visit: [Block 1](#1-classify-provider-uncertainty-required).

Start from `m5-secure-ecommerce`. Run the ecommerce checks and preserve the order
state tests before adding any external client.

On resume, preserve your existing `.env`, completed M5 identity routes, and
evidence. Use the validation commands from the M6 preflight; anonymous-starter,
first-install, and destructive-reset steps are not M6 resume actions. If a check
fails, use the preflight's M5-versus-provider recovery boundary first.

## Build

The pilot labels the five cues explicitly in Block 1. Blocks 2–3 preserve the
same accepted order: **Do** (start/work), **Understand** (exact support),
**Check** (command/observation/evidence), **If it fails** (hint/reset), and
**Stop/resume** (last-green boundary/return anchor).

### 1. Classify provider uncertainty `[REQUIRED]`

- **Do:** work in `projects/ecommerce/`; read the fixed contract, then extend
  `tests/m6/test_provider.py` around the supplied fake and run the command below.
- **Understand:** a timeout can mean definite no-effect or an unknown result;
  local database rollback cannot undo provider money. Use the [C1 hints](#c1--unreliable-provider),
  [uncertainty example](#the-request-timed-out-after-the-payment), and
  [tool boundaries](#tools-earned-here) only when needed.
- **Check:** success, decline, each timeout phase, refund results, and `lookup`
  are distinct; record the command and state table in `evidence/M6/provider.md`.
- **If it fails:** first ask whether provider processing occurred, then inspect
  operation identity and provider fact. Reset by rerunning the in-memory fake test.
- **Stop/resume:** stop when the listed command passes and
  evidence is saved. Resume at [Block 1](#1-classify-provider-uncertainty-required),
  then continue to Block 2. The sandbox remains separately authorized and pending.

Read the [integration contract](../../projects/ecommerce/specs/M6-INTEGRATION-CONTRACT.md).
Connect the supplied fake behind a `PaymentProvider` interface; do not add
retries yet. Run `uv run --locked pytest tests/test_failure_harnesses.py -q`.
Observe success, decline, connect/read/total and before-effect timeouts, and an
after-effect unknown state. Exercise refund success, definite failure, and
post-effect timeout; use `lookup` to reveal provider fact without inventing the
learner's local transition.
Record `evidence/M6/provider.md`; stop when every outcome is explicit.

Run from the stated project directory:

```bash
uv run --locked pytest tests/test_failure_harnesses.py tests/m6/test_provider.py -q
```

### 2. Add bounded retries and webhook verification `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/ecommerce/`;
focus on `tests/m6/test_retry_webhook.py` and the output named below. Record `evidence/M6/retry-webhook.md`.
Stop when this block's listed command passes and its evidence is saved.
Resume at [Block 2](#2-add-bounded-retries-and-webhook-verification-required) using that saved result; continue to Block 3.
When needed: [C2 scenario and hints](#c2--hostile-webhook) and [concept explanation](#retries-made-the-outage-worse).

Implement one combined SDK/application retry budget and raw-body signature checks. Exercise rate
limit, 503, malformed, duplicate, delayed, replayed, tampered, and wrong-account
fixtures. Record commands and transitions in `evidence/M6/retry-webhook.md`.
Reset by rerunning the in-memory fake; stop when no unsafe outcome is retried.

Run from the stated project directory:

```bash
uv run --locked pytest tests/m6/test_retry_webhook.py -q
```

### 3. Reconcile unknown operations `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in `projects/ecommerce/`;
focus on `scripts/reconcile_payment.py` and the output named below. Record `evidence/M6/reconciliation.md`.
Stop when this block's listed command passes and its evidence is saved.
Resume at [Block 3](#3-reconcile-unknown-operations-required) using that saved result; continue to [Prove it](#prove-it).
When needed: [C3 scenario and hints](#c3--integration-incident) and [concept explanation](#nobody-could-connect-the-request-to-the-later-webhook).

Build the named reconciliation command from local operation ID to provider fact
and local transition. Run it twice; observe convergence without duplicate effect.
Record `evidence/M6/reconciliation.md` and an [incident note](../../templates/INCIDENT.md#impact-and-detection). Stop when an
after-effect timeout becomes one explainable final state.

After all local checks pass, record the sandbox item as `PENDING — ACCESS` until
the repository owner separately authorizes a named provider, test credential,
bounded actions, evidence destination, and cleanup. A fake or simulated result
cannot satisfy that item.

Create `scripts/reconcile_payment.py`, then use
`uv run --locked python scripts/reconcile_payment.py --operation synthetic-unknown-1`.
Expected: it prints the provider fact, prior local state, chosen transition, and
final local state without credentials. Running it twice produces the same final
state.

Run from the stated project directory:

```bash
uv run --locked pytest tests/m6/test_reconciliation.py -q && uv run --locked python scripts/reconcile_payment.py --operation synthetic-unknown-1
```

### Diagnose deliberate failures

Activate or construct only the current C scenario. Record the symptom and one
hypothesis before inspecting the implementation. Use the matching scenario link
in your active block, then its three hint levels in order. Reset to the last
green checkpoint before starting another scenario.

## Understand

- **Timeout:** the maximum wait before treating an operation as unresolved.
- **Backoff:** increasing delay between bounded retries.
- **Idempotency:** repeating an operation has the same intended effect as once.
- **Webhook:** an inbound HTTP message sent later by another service.
- **Reconciliation:** comparing local and provider truth to resolve uncertainty.
- **Correlation ID:** one safe identifier connecting logs across an operation.

## Use a tool if earned

Use the current project dependencies first. Open [Use now](#use-now) for the active pattern, [Evaluate after evidence](#evaluate-after-evidence) only after the simpler baseline misses its target, and [Do not add yet](#do-not-add-yet) before adding another runtime or service.

## Prove it

Answer [review prompts](#review) after the Core proof.

Prove [A1–A4](#core) with state transitions, request identifiers,
signature tests, reconciliation output, correlated redacted logs, and a postmortem.

## Done / next

Every provider outcome remains classifiable or explicitly unknown, replay is
safe, reconciliation converges, and all Core checks pass. Tag `m6-resilient-integrations`.

### Recovery

Use [targeted references](#resources-for-m6) only for the question left by the active hint ladder.

Reset the in-memory fake by rerunning its test. Start with the challenge hint
ladder before opening [reference](#resources-for-m6).

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Continue to [M7](../m7-durable-async-background-processing/README.md).

[Previous milestone: M5](../m5-secure-multi-user-ecommerce/README.md) · [Course home](../../README.md) · [Next milestone: M7](../m7-durable-async-background-processing/README.md)


---

## Challenge brief

Run from `projects/ecommerce/`. Keep provider data and credentials synthetic.

## **C1 — Unreliable provider**

**PROVIDED** — extend the deterministic provider fake with published modes.

### Steps

1. Create `tests/m6/test_provider.py` for payment/refund, latency, 429/503, malformed response, and before/after-effect timeout.
2. Classify each outcome and use `lookup` after uncertainty before adding timeout, backoff, jitter, or retry.
3. Run README Block 1 and preserve unknown outcomes for reconciliation.

### Hints

1. Ask whether failure is definite or the outcome is unknown.
2. Inspect timeout phase, operation identity, retry budget, and provider fact.
3. Use the HTTPX timeout link in the Reference section below.

### Reset

Rerun `uv run --locked pytest tests/test_failure_harnesses.py -q`; the fake is
in-memory and returns to its deterministic initial state.

## **C2 — Hostile webhook**

**YOU BUILD** — create synthetic signed fixtures from the matrix.

### Steps

1. Create `tests/m6/test_retry_webhook.py` for duplicate, replay, reorder, tamper, age, and wrong bytes/account.
2. Verify the raw body before parsing or applying an effect.
3. Deduplicate and apply order-aware transitions; run README Block 2.

### Hints

1. Compare the exact signed bytes, timestamp, event ID, and account.
2. Inspect verification order, durable event identity, and transition policy.
3. Use the webhook-security link in the Reference section below.

### Reset

Reload the synthetic fixture set and run
`uv run --locked pytest tests/m6/test_retry_webhook.py -q`.

## **C3 — Integration incident**

**YOU BUILD** — reconcile a fixed unknown operation against fake provider state.

### Steps

1. Create `tests/m6/test_reconciliation.py` and `scripts/reconcile_payment.py`.
2. Reconstruct attempts by correlation ID and choose one legal local transition.
3. Run README Block 3 twice and write a concise incident note.

### Hints

1. Start with provider fact, prior local state, and semantic operation ID.
2. Inspect idempotency record, correlation fields, and transition ownership.
3. Use the idempotency reference in the Reference section below.

### Reset

Restore the fixed `synthetic-unknown-1` fake state and rerun
`uv run --locked pytest tests/m6/test_reconciliation.py -q`.

Ship documented degraded behavior and residual provider risk.


---

## Acceptance gate

Required maturity: **Level B plus contextual Level C reliability/diagnostics**.

## Core

- **A1:**
  - [ ] the immediate-payment port uses `pay`, `refund`, and `lookup` consistently; success, decline, connect/read/total/before-processing timeout, post-processing unknown, and refund success/failure/unknown are deterministic
  - [ ] SDK and application retries share one maximum-three-attempt/five-second budget, and decline is never retried
  - [ ] C1 tests distinguish connect, read, and total timeouts.
  - [ ] Retry tests cover classification, exponential backoff with jitter, and maximum attempts/elapsed budget.
  - [ ] `Retry-After` is honored within the budget.
  - [ ] Unknown outcomes never create a duplicate semantic effect.
- **A2:**
  - [ ] C2 validates raw-body signature, timestamp, and account before side effects.
  - [ ] Replay is rejected and event identity is durable.
  - [ ] Duplicate delivery is idempotent and out-of-order delivery preserves state-machine truth.
- **A3:**
  - [ ] Client/API idempotency records bind key to operation/payload
  - [ ] structured redacted logs correlate request, attempts, webhook, and reconciliation
  - [ ] C3 postmortem links a regression test and recovery evidence.
- **A4:**
  - [ ] Degraded and unknown states remain visible until reconciliation converges them.
  - [ ] A [data-lifecycle review](../../templates/DATA-LIFECYCLE.md) traces provider payload/identifier copies, logs, and replay records.
  - [ ] The review covers retention, deletion, and access.
  - [ ] integration/unit/API/migration/lint/validator commands pass cleanly.

Local A1–A4 finish offline. The separately authorized Stripe-like sandbox is a
required experiment only for the real-provider evidence claim. If access is
missing or the provider is unavailable, record `PENDING — ACCESS/PROVIDER
OUTAGE`; do not replace it with fake evidence or block independent local work.

## Execution map

Each checklist bullet is a local step in order. From `projects/ecommerce/`, use
README Block 1 for A1, Block 2 for A2, and Block 3 for A3–A4. Also run
`test -s evidence/M6/data-lifecycle.md` for the lifecycle step. Expected:
uncertain outcomes remain explicit and repeated delivery converges. Record under
matching A headings; reset the deterministic fake and rerun one focused test.

## Stretch

Add a circuit breaker only after quantified cascading harm and test half-open/recovery semantics; compare a second provider only from a real continuity requirement.

## Review

### Review

Answer one question at a time in `evidence/M6/index.md`:

1. Why does a timeout create an unknown outcome?
2. Which failures are retryable, and which are not?
3. How does backoff change load on a struggling provider?
4. Where is the semantic idempotency key created and stored?
5. Why is the webhook signature checked against raw bytes?
6. How do duplicate and out-of-order events converge?
7. Can nested retries exceed the total budget?
8. Does any log expose payment or signature data?
9. Which accepted post-response action can be lost, and is that acceptable?
10. Can you reconstruct C3 only from evidence, and what was the earliest signal?
11. Why can database rollback not undo a provider payment or refund?
12. Which facts would a separately authorized sandbox prove that the fake cannot?

Trace one provider field through request, provider, webhook, idempotency record, and logs using the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md). Lens prompt (same A1–A4 gate): a career-shifter states incident impact for a nontechnical stakeholder; a data specialist explains why payload persistence and reconciliation are application/security responsibilities, not merely ingestion.


---

## Reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M6 concepts through provider failures

## “The request timed out after the payment”

**Example:** the provider completed work but its response never arrived. **Term —
unknown outcome:** neither success nor failure is yet proven. **Rule:** preserve
that state and reconcile; do not blindly retry a money effect.

## “The webhook arrived twice and out of order”

**Example:** fulfilled arrives before paid, then paid repeats. **Term —
idempotent consumer:** repeated delivery converges to one intended effect.
**Rule:** verify raw signed input, identify the event, and apply declared state
rules.

## “Retries made the outage worse”

**Example:** every request retries immediately during a provider failure. **Term —
exponential backoff with jitter:** progressively longer, slightly randomized
delays. **Rule:** classify retryability and bound connect/read/overall time,
attempts, and total elapsed budget.

## “The webhook signature passed after parsing changed the bytes”

**Example:** normalized JSON differs from the signed request body. **Term — replay
window:** the allowed age of a signed event. **Rule:** verify raw bytes, timestamp,
event identity, and account before durable, idempotent handling.

## “Nobody could connect the request to the later webhook”

**Example:** logs omit the operation and correlation IDs. **Term — correlation
ID:** a safe identifier joining related work across boundaries. **Rule:** correlate
attempts and state changes, preserve uncertainty, redact data, and review incidents
through impact, timeline, recovery, and prevention rather than blame.

## “The database rolled back but the provider did not”

**Example:** the provider completed a payment or refund before the local
transaction failed. **Term — reconciliation:** compare durable local intent with
provider fact using the operation/idempotency key. **Rule:** a database rollback
cannot reverse external money; block unsafe repetition, look up, and reconcile
forward.

### Tools earned here

- **HTTPX client with explicit limits:** controlled outbound timeouts and testable transport.
- **Small retry policy:** explicit classification/backoff/jitter/budget; avoid opaque retry-all decorators.
- **Provider fakes:** deterministically produce uncertain outcomes; do not mock internal business logic.
- **Direct HTTP or one provider SDK (sandbox only):** evaluate after local Core; either adapter must preserve `pay`/`refund`/`lookup`, the combined retry/deadline budget, business idempotency, and reconciliation. Remove it if it obscures those facts.
- **HMAC/signature library and constant-time comparison:** implement provider-specified verification with replay bounds.
- **Structured logging:** stable fields and correlation/request IDs, with redaction.

FastAPI `BackgroundTasks` is allowed only for short, noncritical, same-process work whose loss or repetition is explicitly acceptable. It may not carry an accepted payment, fulfillment, webhook, or reconciliation obligation. Persist durable intent and defer its worker semantics to M7.

S3-compatible object storage is earned only if the integration introduces files that must outlive application instances. Prefer direct presigned transfer; define authorization, checksums, size/type limits, retention/deletion, orphan cleanup, and provider failure behavior. Do not proxy large media through FastAPI or add object storage for JSON records.

No circuit-breaker library, queue, broker, fallback provider, or object store without its trigger. Remove retries that amplify load or obscure terminal outcomes. Durable async work is earned in M7.

The sandbox is not a CI dependency. Keys remain test-only, least-privilege,
environment-isolated, redacted, and separately authorized; no key belongs in
Git, evidence, URLs, logs, fixtures, or workflow configuration.

## Evaluate after evidence

Evaluate only optional tools after the stated simpler baseline fails. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates current behavior, or creates a second application path.

## Sources

### Resources for M6

Open these after observing timeout, duplicate, signature, or unknown-outcome behavior. Reviewed 2026-09-14.

- [HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/) — Which phase timed out and what limit should be bounded? Applicable tool: HTTPX 0.28+.
- [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) — What does a mature provider require for safe request replay? Applicable example: current Stripe API.
- [Stripe sandboxes](https://docs.stripe.com/sandboxes) — What separates test from live access, and how should a bounded test credential be handled? Applicable example: current Stripe API.
- [Stripe webhook signatures](https://docs.stripe.com/webhooks/signature) — What exact bytes and secret are authenticated? Applicable example: current Stripe API.
- [Stripe refunds](https://docs.stripe.com/refunds) — What provider facts and failure states must refund/lookup expose? Applicable example: current Stripe API.

Stripe is the reference protocol and sandbox example, not a required vendor for
local Core. A real sandbox call requires separate authority.
