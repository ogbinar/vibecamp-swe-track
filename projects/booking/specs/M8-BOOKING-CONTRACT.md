# M8 booking lifecycle and race contract

One event has fixed capacity. A hold reserves one unit until `expires_at`;
confirmation consumes a live hold; cancellation releases a live hold; expiry
releases an unconfirmed hold. Database time is authoritative. At the exact
boundary, `now >= expires_at` means expired.

`POST /events/{id}/holds` returns 201 or 409 `capacity_unavailable`.
`POST /holds/{id}/confirm` returns 200, 404, 409 `hold_expired`, or the existing
confirmation on a repeat. `POST /holds/{id}/cancel` returns 200 and is
repeatable. Responses state hold status and expiry.

Harness contracts: two independent connections race for the final unit;
confirm races expiry; cancel races confirm; inconsistent lock order reproduces
a deadlock; a bounded retry handles only the database's retryable outcome.
Record exact allowed winners, final invariant, wait time, attempts, and API
response. Stress tests supplement, never replace, the coordinated race.
