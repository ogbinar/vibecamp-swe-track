"""Exercise one representative mutation for each durable validator class."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# name: path, existing text (None creates a file), replacement, diagnostic
MUTATIONS: dict[str, tuple[str, str | None, str, str]] = {
    "manifest order": (
        "docs/maintainers/curriculum.json",
        '"id":"M0"',
        '"id":"M2"',
        "milestones must be ordered M0 through M10",
    ),
    "competing controller": (
        "milestones/m0-engineering-baseline/CHALLENGE.md",
        None,
        "# Competing route\n",
        "exactly one learner controller README is required",
    ),
    "outcome contract": (
        "milestones/m3-transactions-correctness/README.md",
        "# M3 — Make checkout safe",
        "# M3 — Learn transactions",
        "controller outcome disagrees with manifest",
    ),
    "challenge trace": (
        "milestones/m8-concurrency-booking/README.md",
        "**C1 — Final-seat race**",
        "**Z1 — Final-seat race**",
        "challenge IDs disagree with manifest",
    ),
    "acceptance trace": (
        "milestones/m8-concurrency-booking/README.md",
        "**A1:",
        "**Z1:",
        "Core IDs disagree with manifest",
    ),
    "Core and Stretch boundary": (
        "milestones/m7-durable-async-background-processing/README.md",
        "## Stretch",
        "## Optional",
        "missing controller section 'Stretch'",
    ),
    "broken navigation": (
        "README.md",
        "projects/catalog/README.md#if-setup-fails",
        "projects/catalog/README.md#missing-anchor",
        "broken Markdown anchor",
    ),
    "runtime": (
        "projects/booking/pyproject.toml",
        'requires-python = "==3.13.*"',
        'requires-python = "==3.12.*"',
        "Python 3.13 and exact Air 0.48.1 runtime required",
    ),
    "lock": (
        "projects/social/uv.lock",
        'name = "air"\nversion = "0.48.1"',
        'name = "air"\nversion = "0.48.0"',
        "exact Air 0.48.1 is not locked",
    ),
    "Air composition": (
        "projects/pos/src/pos_api/web.py",
        "air.Air(fastapi_app=api)",
        "air.Air()",
        "shared Air/FastAPI composition or OpenAPI exclusion missing",
    ),
    "OpenAPI exclusion": (
        "projects/booking/src/booking_api/web.py",
        "air.AirRouter(include_in_schema=False)",
        "air.AirRouter()",
        "shared Air/FastAPI composition or OpenAPI exclusion missing",
    ),
    "internal HTTP": (
        "projects/pos/src/pos_api/web.py",
        "import air",
        "import air\nimport httpx",
        "must not call its own API over HTTP",
    ),
    "second runtime": (
        "projects/catalog/package.json",
        None,
        '{"private": true}\n',
        "second frontend runtime marker exists",
    ),
    "Catalog solution": (
        "projects/catalog/src/catalog_api/models.py",
        "class ProductResponse",
        "class ProductDraft: ...\n\nclass ProductResponse",
        "completed or premature learner behavior remains",
    ),
    "Ecommerce HTMX solution": (
        "projects/ecommerce/src/ecommerce_api/web.py",
        "def create_web_router",
        "hx_get = '/app/payment'\n\ndef create_web_router",
        "completed or premature learner behavior remains",
    ),
    "Social SSE solution": (
        "projects/social/src/social_api/web.py",
        "import air",
        "import air\nSSEResponse = air.SSEResponse",
        "completed or premature learner behavior remains",
    ),
    "callable vulnerable fixture": (
        "projects/ecommerce/src/ecommerce_api/app.py",
        "return app",
        'VULNERABLE_ROUTE = "/debug/login-as"\n    return app',
        "callable vulnerable teaching fixture",
    ),
    "external evidence": (
        "TODO.md",
        "- [ ] Obtain explicit authority",
        "- [x] Obtain explicit authority",
        "external evidence must remain visible and unchecked",
    ),
    "unpinned action": (
        ".github/workflows/repository-hygiene.yml",
        "actions/checkout@11d5960a326750d5838078e36cf38b85af677262",
        "actions/checkout@v4",
        "action is not commit-pinned",
    ),
}


def run_validator(candidate: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", "scripts/check_curriculum.py"],
        cwd=candidate,
        capture_output=True,
        text=True,
        check=False,
    )


def main() -> int:
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="vibecamp-validator-") as directory:
        candidate = Path(directory) / "repo"
        shutil.copytree(
            ROOT,
            candidate,
            ignore=shutil.ignore_patterns(
                ".git", ".venv", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"
            ),
        )
        baseline = run_validator(candidate)
        if baseline.returncode:
            print("FAIL: unmodified candidate is not green\n" + baseline.stdout)
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
            result = run_validator(candidate)
            if existed:
                path.write_text(original, encoding="utf-8")
            else:
                path.unlink()
            if result.returncode == 0:
                failures.append(f"{name}: validator accepted controlled failure")
            elif diagnostic not in result.stdout:
                failures.append(f"{name}: wrong rejection: {result.stdout}")
            else:
                print(f"PASS: {name}")

        archive = candidate / "release.tar"
        archive.write_text("synthetic archive marker", encoding="utf-8")
        result = run_validator(candidate)
        archive.unlink()
        if result.returncode != 1 or "generated archive outside dist/" not in result.stdout:
            failures.append("generated archive: validator missed controlled failure")
        else:
            print("PASS: generated archive")

        readme = candidate / "README.md"
        original = readme.read_text(encoding="utf-8")
        readme.write_text(
            original.replace("Build, test, break", "Build carefully, test, break", 1),
            encoding="utf-8",
        )
        harmless = run_validator(candidate)
        readme.write_text(original, encoding="utf-8")
        if harmless.returncode:
            failures.append("harmless prose: validator remains wording-coupled: " + harmless.stdout)
        else:
            print("PASS: harmless prose")

        restored = run_validator(candidate)
        if restored.returncode:
            failures.append("restored candidate is not green: " + restored.stdout)

    if failures:
        print("\n".join(f"FAIL: {failure}" for failure in failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
