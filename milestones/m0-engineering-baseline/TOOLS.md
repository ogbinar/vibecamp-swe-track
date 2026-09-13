# Tools earned here

- **uv + lockfile:** reproducible dependency resolution and command execution; avoid a second package manager.
- **`fastapi[standard]`/Pydantic:** smallest typed HTTP slice plus the declared FastAPI CLI/Uvicorn ASGI runtime; development reload is never the production command.
- **pytest + HTTPX:** prove behavior across the API boundary and one configuration unit seam.
- **Ruff + mypy:** Ruff owns lint/format feedback; mypy checks typed module boundaries. Keep both configurations minimal and do not pretend one substitutes for the other.
- **GitHub Actions:** repeat the documented clean path. It is feedback, not evidence that deployment is safe.

No PostgreSQL, container, task runner, or deployment platform yet. Pin one supported Python version in `.python-version` and `pyproject.toml`, resolve it through the uv lockfile, and earn a version matrix only when compatibility is claimed. Earn a task runner only after command drift is observed; remove any tool whose setup exceeds the problem it prevents.
