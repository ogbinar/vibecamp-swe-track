"""Prove stable curriculum-validator rules with isolated controlled failures."""

from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from check_curriculum import classify_milestone_contract, classify_runtime

ROOT = Path(__file__).resolve().parents[1]

# name: (relative path, exact candidate text or None for a new file, replacement,
# expected validator diagnostic). Each target is checked before mutation.
MUTATIONS: dict[str, tuple[str, str | None, str, str]] = {
    "stable milestone contract": (
        "milestones/m0-engineering-baseline/TOOLS.md", None, "# Superseded file\n",
        "undocumented hybrid contract",
    ),
    "roadmap header": (
        "README.md", "| Milestone | Business problem | Product capability | Start here |",
        "| Milestone | Concepts | Product capability | Start here |",
        "primary roadmap needs exact four business-first headers",
    ),
    "roadmap problem": (
        "README.md", "A catalog works only on its author's machine.", "Catalog setup is difficult.",
        "business route row 1 has wrong problem",
    ),
    "roadmap capability": (
        "README.md", "Make the catalog easy to run.", "Learn application setup.",
        "business route row 1 has wrong product capability",
    ),
    "roadmap destination": (
        "README.md", "[Start M5](milestones/m5-secure-multi-user-ecommerce/README.md)",
        "[Start M5](milestones/m4-maintainability-testing-refactoring/README.md)",
        "IA route row 6 has wrong controller link",
    ),
    "outcome title": (
        "milestones/m3-transactions-correctness/README.md", "# M3 — Make checkout safe",
        "# M3 — Transactions and correctness", "outcome-first title is missing",
    ),
    "controller order": (
        "milestones/m5-secure-multi-user-ecommerce/README.md", "## Understand",
        "### Understand", "business-first sections missing or out of order",
    ),
    "product summary": (
        "milestones/m7-durable-async-background-processing/README.md", "**Product can:**",
        "**Result:**", "expected exactly one **Product can:** summary",
    ),
    "duplicated cue legend": (
        "milestones/m3-transactions-correctness/README.md", "## Build",
        "## Build\n\nEach block keeps the action", "superseded learner-route content remains",
    ),
    "reference section": (
        "milestones/m4-maintainability-testing-refactoring/REFERENCE.md", "## Do not add yet",
        "## Avoid for now", "missing merged reference section '## Do not add yet'",
    ),
    "acceptance review": (
        "milestones/m8-concurrency-booking/ACCEPTANCE.md", "## Review", "## Reflection",
        "four-file contract must merge review prompts",
    ),
    "core boundary": (
        "milestones/m8-concurrency-booking/ACCEPTANCE.md", "## Core", "## Required",
        "expected exactly one ## Core",
    ),
    "challenge mode": (
        "milestones/m8-concurrency-booking/CHALLENGE.md",
        "**PROVIDED** — run the in-memory barrier, then reproduce it on PostgreSQL.",
        "Run the in-memory barrier, then reproduce it on PostgreSQL.",
        "must declare exactly one challenge mode",
    ),
    "challenge hints": (
        "milestones/m8-concurrency-booking/CHALLENGE.md", "### Hints", "### Suggestions",
        "must contain one ### Hints",
    ),
    "trace id": (
        "milestones/m8-concurrency-booking/ACCEPTANCE.md", "**A1", "**Z1",
        "Race conditions: M8 A1 missing",
    ),
    "anchor": (
        "README.md", "projects/catalog/README.md#if-setup-fails",
        "projects/catalog/README.md#missing-anchor", "broken Markdown anchor",
    ),
    "python runtime": (
        "projects/booking/pyproject.toml", 'python_version = "3.13"',
        'python_version = "3.12"', "runtime migration must be wholly",
    ),
    "Air manifest pin": (
        "projects/catalog/pyproject.toml", '"air==0.48.1"', '"air==0.48.0"',
        "runtime migration must be wholly",
    ),
    "Air lock pin": (
        "projects/social/uv.lock", 'name = "air"\nversion = "0.48.1"',
        'name = "air"\nversion = "0.48.0"', "exact air 0.48.1 is not locked",
    ),
    "Air composition": (
        "projects/pos/src/pos_api/web.py", "air.Air(fastapi_app=api)", "air.Air()",
        "Air/FastAPI composition missing",
    ),
    "Air router exclusion": (
        "projects/booking/src/booking_api/web.py", "air.AirRouter(include_in_schema=False)",
        "air.AirRouter()", "Air/FastAPI composition missing",
    ),
    "internal HTTP": (
        "projects/pos/src/pos_api/web.py", '"""Air-owned pages',
        'import httpx\n\n"""Air-owned pages', "web layer must not call its own API over HTTP",
    ),
    "unearned HTMX": (
        "projects/booking/src/booking_api/web.py", "def booking_summary()",
        "hx_get = '/app/internal'\n\ndef booking_summary()",
        "earned HTMX must appear only in ecommerce and social",
    ),
    "unearned SSE": (
        "projects/ecommerce/src/ecommerce_api/web.py", "import air",
        "import air\nSSEResponse = air.SSEResponse", "earned SSE must appear only in social",
    ),
    "explicit AirForm": (
        "projects/catalog/src/catalog_api/web.py", "ProductDraftForm.from_request(request)",
        "ProductDraftForm()", "explicit Pydantic-backed AirForm.from_request validation is missing",
    ),
    "Node runtime": (
        "projects/catalog/package.json", None, '{"private": true}\n',
        "second frontend runtime marker exists: package.json",
    ),
    "custom JavaScript": (
        "projects/social/src/client.js", None, "console.log('parallel client')\n",
        "custom project JavaScript exists",
    ),
    "excluded presentation tool": (
        "projects/catalog/src/catalog_api/web.py", "import air", "import air\nAirDB = object()",
        "excluded presentation tool AirDB",
    ),
    "POS Python image": (
        "projects/pos/Dockerfile", "FROM python:3.13-slim@sha256:",
        "FROM python:3.12-slim@sha256:", "Python 3.13 base image must be digest-pinned",
    ),
    "provenance": (
        "docs/maintainers/archive/2026-09-15-business-first/README.md",
        "`7ef342562ab4933c70546af0bc009ffc7d78a80732d81a41f1fec987e9ea8b8e`",
        "`missing-hash`", "BF provenance manifest needs 44 exact source rows",
    ),
    "external evidence": (
        "TODO.md", "- [ ] Obtain explicit authority", "- [x] Obtain explicit authority",
        "external evidence must remain visible and unchecked",
    ),
    "action pin": (
        ".github/workflows/repository-hygiene.yml",
        "actions/checkout@11d5960a326750d5838078e36cf38b85af677262", "actions/checkout@v4",
        "action is not commit-pinned",
    ),
    "readiness claim": (
        "USABILITY.md", "cannot establish human comprehension", "proves self-service ready",
        "unsupported unqualified self-service-ready claim",
    ),
    "vocabulary": (
        "projects/ecommerce/REQUIREMENTS.md", "fulfilled, and refunded",
        "shipped, and refunded", "controlled vocabulary violation",
    ),
    "M8 database barrier": (
        "projects/booking/tests/test_postgres.py", "SELECT pg_backend_pid()", "SELECT 1",
        "missing neutral concurrency seam",
    ),
    "M10 readiness": (
        "projects/pos/compose.production.yml", "/ready", "/health",
        "missing release gate",
    ),
    "M10 restore drill": (
        "projects/pos/scripts/rehearse_m10.sh", "psql -v ON_ERROR_STOP=1", "psql",
        "missing bounded drill",
    ),
    "likely secret": (
        "README.md", "Software engineering is", "ghp_123456789012345678901234567890 is",
        "likely secret in README.md",
    ),
    "callable vulnerable fixture": (
        "projects/ecommerce/src/ecommerce_api/app.py", "return app",
        'VULNERABLE_ROUTE = "/debug/login-as"\n    return app',
        "callable vulnerable teaching fixture",
    ),
}

ROUTE_ROWS = [
    line for line in (ROOT / "README.md").read_text(encoding="utf-8").splitlines()
    if re.match(r"^\| M(?:10|[0-9]) \|", line)
]
MUTATIONS["roadmap count"] = (
    "README.md", ROUTE_ROWS[5] + "\n", "", "IA route map needs eleven ordered rows"
)
MUTATIONS["roadmap order"] = (
    "README.md", "\n".join(ROUTE_ROWS[:2]), "\n".join(reversed(ROUTE_ROWS[:2])),
    "IA route row 1",
)


def main() -> int:
    failures: list[str] = []
    # Keep direct regression coverage for the former transitional classifiers;
    # the repository-level validator below now accepts only the stable states.
    contract_cases = (
        ({"README.md", "CONCEPTS.md", "CHALLENGE.md", "TOOLS.md", "ACCEPTANCE.md", "REVIEW.md", "RESOURCES.md"}, "old"),
        ({"README.md", "CHALLENGE.md", "ACCEPTANCE.md", "REFERENCE.md"}, "new"),
        ({"README.md", "CHALLENGE.md", "ACCEPTANCE.md", "REFERENCE.md", "TOOLS.md"}, "hybrid"),
    )
    for entries, expected in contract_cases:
        actual, _ = classify_milestone_contract(entries)
        if actual != expected:
            failures.append(f"contract classifier: expected {expected}, got {actual}")
    pre_air = 'requires-python = "==3.12.*"\ndependencies = ["fastapi[standard]>=0.116.0"]\ntarget-version = "py312"\npython_version = "3.12"\n'
    post_air = 'requires-python = "==3.13.*"\ndependencies = [\n  "air==0.48.1",\n  "fastapi[standard]>=0.116.0",\n]\ntarget-version = "py313"\npython_version = "3.13"\n'
    hybrid_air = post_air.replace('python_version = "3.13"', 'python_version = "3.12"')
    for manifest, version, expected in (
        (pre_air, "3.12\n", "pre-Air"),
        (post_air, "3.13\n", "Air"),
        (hybrid_air, "3.13\n", "hybrid"),
    ):
        actual, _ = classify_runtime(manifest, version)
        if actual != expected:
            failures.append(f"runtime classifier: expected {expected}, got {actual}")

    with tempfile.TemporaryDirectory(prefix="vibecamp-validator-") as directory:
        candidate = Path(directory) / "repo"
        shutil.copytree(
            ROOT,
            candidate,
            ignore=shutil.ignore_patterns(
                ".git", ".venv", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"
            ),
        )
        baseline = subprocess.run(
            ["python3", "scripts/check_curriculum.py"], cwd=candidate,
            capture_output=True, text=True, check=False,
        )
        if baseline.returncode:
            print("FAIL: unmutated candidate is not green\n" + baseline.stdout)
            return 1

        for name, (relative, old, new, diagnostic) in MUTATIONS.items():
            path = candidate / relative
            existed = path.exists()
            original = path.read_text(encoding="utf-8") if existed else ""
            if old is None:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(new, encoding="utf-8")
            elif old not in original:
                failures.append(f"{name}: mutation target missing")
                continue
            else:
                path.write_text(original.replace(old, new, 1), encoding="utf-8")
            result = subprocess.run(
                ["python3", "scripts/check_curriculum.py"], cwd=candidate,
                capture_output=True, text=True, check=False,
            )
            if existed:
                path.write_text(original, encoding="utf-8")
            else:
                path.unlink()
            if result.returncode == 0:
                failures.append(f"{name}: validator accepted controlled failure")
            elif result.returncode != 1 or diagnostic not in result.stdout:
                failures.append(f"{name}: wrong rejection: {result.stdout} {result.stderr}")
            else:
                print(f"PASS: {name} mutation was rejected for its intended reason")

        archive = candidate / "release.tar"
        archive.write_text("synthetic archive marker", encoding="utf-8")
        result = subprocess.run(
            ["python3", "scripts/check_curriculum.py"], cwd=candidate,
            capture_output=True, text=True, check=False,
        )
        if result.returncode != 1 or "generated archive outside dist/" not in result.stdout:
            failures.append("archive: missing intended generated archive rejection")
        else:
            print("PASS: archive mutation was rejected")
        archive.unlink()

        restored = subprocess.run(
            ["python3", "scripts/check_curriculum.py"], cwd=candidate,
            capture_output=True, text=True, check=False,
        )
        if restored.returncode:
            failures.append("restored candidate is not green: " + restored.stdout)

    if failures:
        print("\n".join(f"FAIL: {failure}" for failure in failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
