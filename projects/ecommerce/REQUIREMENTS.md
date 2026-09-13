# M5 ecommerce and threat brief

Actors are customer, staff member, and administrator. A customer owns carts,
addresses, and orders. Staff may operate fulfillment but may not grant roles.
Administrators manage roles but do not bypass object/tenant scoping silently.

The order states are pending, paid, cancelled, fulfilled, and refunded. The
learner must declare the allowed actor and predecessor state for every command.

| Command | Allowed actor | Allowed predecessor | Result |
|---|---|---|---|
| Pay | customer/system | pending | paid |
| Cancel | owning customer or staff | pending | cancelled |
| Fulfil | staff | paid | fulfilled |
| Refund | staff | paid or fulfilled | refunded |

All other transitions are denied and leave the stored order unchanged. The
learner may refine who initiates payment, but must keep this state vocabulary.

Threat boundaries to test before repair:

- login/recovery reveals whether an identity exists;
- a client supplies its own role;
- one customer guesses another customer's object or list filter;
- an expired, wrong-audience, or wrong-type token is accepted;
- a repeated or forbidden transition mutates the order.

M5 excludes external payment calls, queues, Redis, social login, and a custom
identity provider. Use synthetic identities and secrets only.
