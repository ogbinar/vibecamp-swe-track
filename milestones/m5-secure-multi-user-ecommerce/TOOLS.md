# Tools earned here

- **`pwdlib[argon2]`:** adaptive password hashing, verification, and upgrade; never invent cryptography.
- **Server-side opaque session plus secure cookie, or PyJWT:** select from the actual client/trust boundary. Cookie mode requires CSRF/session fixation/rotation/logout tests; JWT mode requires short-lived claims, fixed-algorithm validation, issuer/audience/time/type checks, and explicit refresh/revocation behavior.
- **FastAPI security/dependency boundaries:** authenticate once, authorize per action/object.
- **pytest/HTTPX security matrix:** prove negative paths at the API boundary.
- **`pydantic-settings`/CI secrets:** keep secret values outside source and output.

No OAuth server, external identity platform, payment SDK, WAF, or broad security scanner is required. Do not implement both session mechanisms in Core: compare them, select one, and document why. Earn refresh tokens only from session requirements and document revocation/theft behavior.
