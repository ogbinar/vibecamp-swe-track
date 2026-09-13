# M0 tools and why they are here

- **uv** installs the pinned Python dependencies and runs commands in the
  project environment. `uv.lock` makes the resolved versions repeatable.
- **FastAPI and Uvicorn** define the API and run the ASGI server process.
- **Pydantic and pydantic-settings** define response shapes and validate
  configuration at startup.
- **pytest and HTTPX** execute behavior through the HTTP boundary.
- **Ruff** checks source rules and formatting. **Mypy** separately checks type
  annotations across files.
- **Git and GitHub** preserve change history and review. **GitHub Actions**
  repeats the same checks in continuous integration (CI).

M0 deliberately has no PostgreSQL, Docker, authentication, task runner,
service/repository layer, frontend, or deployment platform. Adding them would
hide the reproducibility problem under unrelated setup. Use one supported
Python version; a version matrix is earned only when compatibility is claimed.
