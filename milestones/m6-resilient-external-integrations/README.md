# M6 — Resilient External Integrations

[Course home](../../README.md) / M6

**Milestone 7 of 11 · M6**

## Why

A payment request times out. The provider may have completed the payment even
though your application received no answer. Treat that uncertainty as product state.

## Starting checkpoint

- **At a glance:** Resilient · Ecommerce.
- **You will leave with:** Provider boundary and retry/webhook tests; Reconciliation and incident record.
- **Gate:** [A1–A4 / B + contextual C](ACCEPTANCE.md#core).
- **Repository support:** supplied starter locally verified; your learner gate needs your own evidence. [Dated scope and limits](../../USABILITY.md#readiness-status-vocabulary)
separate local structure/starter checks from pending hosted and human evidence.
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[M6 preflight](../../projects/ecommerce/README.md#m6-preflight-after-completing-m5), then return to the saved block; first visit: [Block 1](#1-classify-provider-uncertainty-required).

Start from `m5-secure-ecommerce`. Run the ecommerce checks and preserve the order
state tests before adding any external client.

On resume, preserve your existing `.env`, completed M5 identity routes, and
evidence. Use the validation commands from the M6 preflight; anonymous-starter,
first-install, and destructive-reset steps are not M6 resume actions. If a check
fails, use the preflight's M5-versus-provider recovery boundary first.

## Terms used here

- **Timeout:** the maximum wait before treating an operation as unresolved.
- **Backoff:** increasing delay between bounded retries.
- **Idempotency:** repeating an operation has the same intended effect as once.
- **Webhook:** an inbound HTTP message sent later by another service.
- **Reconciliation:** comparing local and provider truth to resolve uncertainty.
- **Correlation ID:** one safe identifier connecting logs across an operation.

## Product brief

Follow the [integration contract](../../projects/ecommerce/specs/M6-INTEGRATION-CONTRACT.md).
Add one controllable payment client plus signed inbound payment webhooks.
Complete C1–C3 in [CHALLENGE.md](CHALLENGE.md#m6-challenge-brief): simulate timeout-before-effect,
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

## Work blocks

The pilot labels the five cues explicitly in Block 1. Blocks 2–3 preserve the
same accepted order: **Do** (start/work), **Understand** (exact support),
**Check** (command/observation/evidence), **If it fails** (hint/reset), and
**Stop/resume** (last-green boundary/return anchor).

### 1. Classify provider uncertainty `[REQUIRED]`

- **Do:** work in `projects/ecommerce/`; read the fixed contract, then extend
  `tests/m6/test_provider.py` around the supplied fake and run the command below.
- **Understand:** a timeout can mean definite no-effect or an unknown result;
  local database rollback cannot undo provider money. Use the [C1 hints](CHALLENGE.md#c1--unreliable-provider),
  [uncertainty example](CONCEPTS.md#the-request-timed-out-after-the-payment), and
  [tool boundaries](TOOLS.md#tools-earned-here) only when needed.
- **Check:** success, decline, each timeout phase, refund results, and `lookup`
  are distinct; record the command and state table in `evidence/M6/provider.md`.
- **If it fails:** first ask whether provider processing occurred, then inspect
  operation identity and provider fact. Reset by rerunning the in-memory fake test.
- **Stop/resume:** stop when [command-map row 1](#literal-command-map) passes and
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

### 2. Add bounded retries and webhook verification `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/ecommerce/`;
focus on `tests/m6/test_retry_webhook.py` and the output named below. Record `evidence/M6/retry-webhook.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 2](#2-add-bounded-retries-and-webhook-verification-required) using that saved result; continue to Block 3.
When needed: [C2 scenario and hints](CHALLENGE.md#c2--hostile-webhook) and [concept explanation](CONCEPTS.md#retries-made-the-outage-worse).

Implement one combined SDK/application retry budget and raw-body signature checks. Exercise rate
limit, 503, malformed, duplicate, delayed, replayed, tampered, and wrong-account
fixtures. Record commands and transitions in `evidence/M6/retry-webhook.md`.
Reset by rerunning the in-memory fake; stop when no unsafe outcome is retried.

### 3. Reconcile unknown operations `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in `projects/ecommerce/`;
focus on `scripts/reconcile_payment.py` and the output named below. Record `evidence/M6/reconciliation.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 3](#3-reconcile-unknown-operations-required) using that saved result; continue to [Evidence](#evidence).
When needed: [C3 scenario and hints](CHALLENGE.md#c3--integration-incident) and [concept explanation](CONCEPTS.md#nobody-could-connect-the-request-to-the-later-webhook).

Build the named reconciliation command from local operation ID to provider fact
and local transition. Run it twice; observe convergence without duplicate effect.
Record `evidence/M6/reconciliation.md` and an [incident note](../../templates/INCIDENT-POSTMORTEM.md#impact-and-detection). Stop when an
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

### Literal command map

Run from `projects/ecommerce/`; create the M6 learner tests and script named below.

Before: create the named target and observe an outcome-classification,
retry/signature, or convergence assertion fail. File-not-found is not evidence. After: the
row’s stop condition converges without an unsafe duplicate effect.

| Block | Learner target | Copyable command | Expected stop condition |
|---|---|---|---|
| 1 | supplied fake plus `tests/m6/test_provider.py` | `uv run --locked pytest tests/test_failure_harnesses.py tests/m6/test_provider.py -q` | Success, decline, definite timeout, and unknown outcome remain distinguishable. |
| 2 | `tests/m6/test_retry_webhook.py` | `uv run --locked pytest tests/m6/test_retry_webhook.py -q` | Retry budget and every signed-webhook fixture converge without an unsafe repeat. |
| 3 | `scripts/reconcile_payment.py` and `tests/m6/test_reconciliation.py` | `uv run --locked pytest tests/m6/test_reconciliation.py -q && uv run --locked python scripts/reconcile_payment.py --operation synthetic-unknown-1` | Two invocations report the same final state and no duplicate effect. |

Create an absent target before recording a red result. Reset the deterministic fake by
rerunning its focused test; record outcome classification and next action before pausing.

Pause: record the provider mode, local state, and next M6 test.

## Failures and hints

Activate or construct only the current C scenario. Record the symptom and one
hypothesis before inspecting the implementation. Use the matching scenario link
in your active block, then its three hint levels in order. Reset to the last
green checkpoint before starting another scenario.

## Evidence

Answer [review prompts](REVIEW.md#review) after the Core proof.

Prove [A1–A4](ACCEPTANCE.md#core) with state transitions, request identifiers,
signature tests, reconciliation output, correlated redacted logs, and a postmortem.

## Done when

Every provider outcome remains classifiable or explicitly unknown, replay is
safe, reconciliation converges, and all Core checks pass. Tag `m6-resilient-integrations`.

## Recovery

Use [targeted references](RESOURCES.md#resources-for-m6) only for the question left by the active hint ladder.

Reset the in-memory fake by rerunning its test. Start with the challenge hint
ladder before opening [RESOURCES.md](RESOURCES.md#resources-for-m6).

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

## Next

Continue to [M7](../m7-durable-async-background-processing/README.md).

[Previous milestone: M5](../m5-secure-multi-user-ecommerce/README.md) · [Course home](../../README.md) · [Next milestone: M7](../m7-durable-async-background-processing/README.md)
