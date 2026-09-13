# Tools earned here

- **Maintained password-hashing library:** adaptive hashing and verification; never invent cryptography.
- **JWT library:** short-lived access claims with strict allow-listed validation; avoid sensitive payloads and algorithm defaults.
- **FastAPI security/dependency boundaries:** authenticate once, authorize per action/object.
- **pytest/HTTPX security matrix:** prove negative paths at the API boundary.
- **`pydantic-settings`/CI secrets:** keep secret values outside source and output.

No OAuth server, external identity platform, payment SDK, WAF, or broad security scanner is required. Earn refresh tokens only from session requirements and document revocation/theft behavior.
