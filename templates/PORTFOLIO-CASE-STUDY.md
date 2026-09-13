# Evidence-backed engineering case study

This is a concise navigation layer over repository evidence, not a duplicate report or marketing page. Every factual claim links to a test, query, PR, decision record, runbook drill, or sanitized transcript. Never invent metrics, users, team roles, or production impact.

## Problem, user, and constraints

What ambiguous outcome mattered? Who needed it, what was out of scope, and which constraints shaped the smallest design?

## Smallest correct design

Show the relevant boundary/data-flow diagram or link and explain one consequential decision. Link an ADR only if warranted and one complexity-rejection record where simplicity won.

## Failure → diagnosis → change

Describe one deliberately preserved reproduction: initial hypothesis, observable failure, root/contributing conditions, fix, and regression proof. The production path must be safe.

## Evidence of effect

| Claim | Before | After | Same environment/workload? | Evidence |
|---|---|---|---|---|

State uncertainty and avoid percentages without raw counts/context.

## Security, operation, and recovery

Summarize the applicable authorization/data-lifecycle risk, diagnostic signal, deployment/recovery drill, and remaining limitation. Link details.

## My contribution and trade-offs

Name what you personally specified, built, tested, debugged, reviewed, and explained; disclose material assistance. Explain an alternative declined and the revisit trigger.

## Reader path

Give a cold reviewer a ≤10-minute route: entry point, one command, one failure/decision artifact, and final evidence. External hosting and screenshots are optional, never substitutes for reproducibility.
