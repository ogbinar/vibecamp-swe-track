"""Prove selected semantic validator rules with isolated controlled failures."""

from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MUTATIONS = {
    "IA ordinal": (
        "milestones/m5-secure-multi-user-ecommerce/README.md",
        "Milestone 6 of 11 · M5", "Milestone 5 of 11 · M5",
    ),
    "IA footer home": (
        "milestones/m5-secure-multi-user-ecommerce/README.md",
        " · [Course home](../../README.md) · ", " · ",
    ),
    "IA breadcrumb": (
        "milestones/m0-engineering-baseline/README.md",
        "[Course home](../../README.md) / M0", "M0",
    ),
    "IA previous": (
        "milestones/m0-engineering-baseline/README.md",
        "[Previous: Course start](../../README.md#start-now)", "Previous: missing",
    ),
    "IA next": (
        "milestones/m10-production-multitenant-saas-capstone/README.md",
        "[Next: Portfolio review / evidence-led next product](../../templates/PORTFOLIO-CASE-STUDY.md#reader-path)",
        "Next: missing",
    ),
    "IA route row": (
        "README.md", "| 6 · M5 |", "| 5 · M5 |",
    ),
    "IA route destination": (
        "README.md",
        "[Secure Multi-user Ecommerce / Secure](milestones/m5-secure-multi-user-ecommerce/README.md)",
        "[Secure Multi-user Ecommerce / Secure](milestones/m4-maintainability-testing-refactoring/README.md)",
    ),
    "roadmap header": (
        "README.md",
        "| # | Milestone / Capability | Project | Key concepts | FastAPI / Python tools | Real integration |",
        "| Position | Milestone / Capability | Project | Key concepts | FastAPI / Python tools | Real integration |",
    ),
    "roadmap shape": (
        "README.md", "| 1 · M0 |", "| 1 · M0 | Extra |",
    ),
    "roadmap classification": (
        "README.md",
        "**Required after local Core:** exactly one Stripe-like payment sandbox",
        "Deterministic/local Core; optional payment sandbox",
    ),
    "IA section order": (
        "milestones/m5-secure-multi-user-ecommerce/README.md",
        "## Product brief", "### Product brief",
    ),
    "IA exact support": (
        "milestones/m5-secure-multi-user-ecommerce/README.md",
        "CHALLENGE.md#c1--broken-identity", "CHALLENGE.md#missing-identity",
    ),
    "challenge mode": (
        "milestones/m8-concurrency-booking/CHALLENGE.md",
        "**PROVIDED** — run the in-memory barrier, then reproduce it on PostgreSQL.",
        "Run the in-memory barrier, then reproduce it on PostgreSQL.",
    ),
    "anchor": ("README.md", "projects/catalog/README.md#if-setup-fails", "projects/catalog/README.md#missing-anchor"),
    "vocabulary": (
        "projects/ecommerce/REQUIREMENTS.md",
        "fulfilled, and refunded",
        "shipped, and refunded",
    ),
    "action pin": (
        ".github/workflows/repository-hygiene.yml",
        "actions/checkout@11d5960a326750d5838078e36cf38b85af677262",
        "actions/checkout@v4",
    ),
    "readiness claim": (
        "USABILITY.md",
        "not yet HUMAN SELF-STUDY VERIFIED",
        "self-service ready",
    ),
    "acceptance range": (
        "milestones/m2-pos-persistence-data-modeling/README.md",
        "and [A1–A5](ACCEPTANCE.md#core) pass",
        "and [A1–A4](ACCEPTANCE.md#core) pass",
    ),
    "work block": (
        "milestones/m8-concurrency-booking/README.md",
        "## Work blocks",
        "## Exercises",
    ),
    "literal command map": (
        "milestones/m3-transactions-correctness/README.md",
        "### Literal command map",
        "### Suggested commands",
    ),
    "work block observation": (
        "milestones/m3-transactions-correctness/README.md",
        "Before: create the named test and observe its published partial-write, repeat,",
        "Initially the learner may see a failure.",
    ),
    "CS evidence ownership": (
        "README.md",
        "do not create a competing root `evidence/` tree",
        "a root evidence tree is also acceptable",
    ),
    "CS integration classification": (
        "QUALITY-GATES.md",
        "PENDING — ACCESS/PROVIDER OUTAGE",
        "PASSED — SIMULATED",
    ),
    "CS pilot cue": (
        "milestones/m0-engineering-baseline/README.md",
        "**Stop/resume:**",
        "**Finish later:**",
    ),
    "CS provider vocabulary": (
        "projects/ecommerce/src/ecommerce_api/provider_fake.py",
        "def refund(",
        "def reverse(",
    ),
    "scenario-local hints": (
        "milestones/m8-concurrency-booking/CHALLENGE.md",
        "### Hints",
        "### Suggestions",
    ),
    "acceptance execution map": (
        "milestones/m5-secure-multi-user-ecommerce/ACCEPTANCE.md",
        "## Execution map",
        "## Notes",
    ),
    "M8 database barrier": (
        "projects/booking/tests/test_postgres.py",
        "SELECT pg_backend_pid()",
        "SELECT 1",
    ),
    "M10 CI gate": (
        ".github/workflows/m10-image.yml",
        "needs: [curriculum, starters]",
        "needs: curriculum",
    ),
    "M10 readiness": (
        "projects/pos/compose.production.yml",
        "/ready",
        "/health",
    ),
    "M10 restore drill": (
        "projects/pos/scripts/rehearse_m10.sh",
        "psql -v ON_ERROR_STOP=1",
        "psql",
    ),
    "starter dependency": (
        "projects/booking/pyproject.toml",
        '"alembic>=1.16.0"',
        '"migration-tool>=1.0"',
    ),
    "likely secret": (
        "README.md",
        "FastAPI is the vehicle",
        "ghp_123456789012345678901234567890 is the vehicle",
    ),
    "callable vulnerable fixture": (
        "projects/ecommerce/src/ecommerce_api/app.py",
        "return app",
        'VULNERABLE_ROUTE = "/debug/login-as"\n    return app',
    ),
}


# Whole rows are captured from the candidate so artifact wording can evolve.
ROUTE_ROWS = [
    line for line in (ROOT / "README.md").read_text(encoding="utf-8").splitlines()
    if re.match(r"^\| \d+ · M(?:10|[0-9]) \|", line)
]
MUTATIONS["IA route count"] = ("README.md", ROUTE_ROWS[5] + "\n", "")
MUTATIONS["IA route order"] = (
    "README.md", "\n".join(ROUTE_ROWS[:2]), "\n".join(reversed(ROUTE_ROWS[:2])),
)


EXPECTED_DIAGNOSTICS = {
    "IA route count": "IA route map needs eleven ordered rows",
    "IA route order": "IA route row 1",
    "IA ordinal": "M5: IA ordinal/label",
    "IA footer home": "M5: IA footer home",
    "IA breadcrumb": "M0: IA breadcrumb",
    "IA previous": "M0: IA footer previous",
    "IA next": "M10: IA footer next",
    "IA route row": "IA route row 6",
    "IA route destination": "IA route row 6 has wrong controller link",
    "roadmap header": "primary roadmap needs exact six headers",
    "roadmap shape": "primary roadmap row 1 needs exactly six columns",
    "roadmap classification": "IA route row 7 has wrong integration classification",
    "IA section order": "learner-route sections missing or out of order",
    "IA exact support": "broken Markdown anchor: CHALLENGE.md#missing-identity",
    "challenge mode": "must declare exactly one challenge mode",
    "anchor": "broken Markdown anchor",
    "vocabulary": "controlled vocabulary violation",
    "action pin": "action is not commit-pinned",
    "readiness claim": "unsupported unqualified self-service-ready claim",
    "acceptance range": "advertised acceptance range",
    "work block": "missing executable work blocks",
    "literal command map": "missing literal command map",
    "work block observation": "command contract missing 'Before:'",
    "CS evidence ownership": "missing stable CS contract",
    "CS integration classification": "missing stable CS contract",
    "CS pilot cue": "missing stable CS contract",
    "CS provider vocabulary": "missing stable CS contract",
    "scenario-local hints": "must contain one ### Hints",
    "acceptance execution map": "missing command/result/evidence execution map",
    "M8 database barrier": "missing neutral concurrency seam",
    "M10 CI gate": "missing immutable release prerequisite",
    "M10 readiness": "missing release gate",
    "M10 restore drill": "missing bounded drill",
    "starter dependency": "missing Core dependency alembic",
    "likely secret": "likely secret in README.md",
    "callable vulnerable fixture": "callable vulnerable teaching fixture",
}


def main() -> int:
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="vibecamp-validator-") as directory:
        candidate = Path(directory) / "repo"
        shutil.copytree(
            ROOT,
            candidate,
            ignore=shutil.ignore_patterns(".git", ".venv", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"),
        )
        baseline_check = subprocess.run(
            ["python3", "scripts/check_curriculum.py"], cwd=candidate,
            capture_output=True, text=True, check=False,
        )
        if baseline_check.returncode:
            print("FAIL: unmutated candidate is not green\n" + baseline_check.stdout)
            return 1
        for name, (relative, old, new) in MUTATIONS.items():
            path = candidate / relative
            baseline = path.read_text(encoding="utf-8")
            if old not in baseline:
                failures.append(f"{name}: mutation target missing")
                continue
            path.write_text(baseline.replace(old, new, 1), encoding="utf-8")
            result = subprocess.run(
                ["python3", "scripts/check_curriculum.py"],
                cwd=candidate,
                capture_output=True,
                text=True,
                check=False,
            )
            path.write_text(baseline, encoding="utf-8")
            if result.returncode == 0:
                failures.append(f"{name}: validator accepted controlled failure")
            elif result.returncode != 1 or EXPECTED_DIAGNOSTICS[name] not in result.stdout:
                failures.append(f"{name}: wrong rejection: {result.stdout} {result.stderr}")
            else:
                print(f"PASS: {name} mutation was rejected for its intended reason")
        archive = candidate / "release.tar"
        archive.write_text("synthetic archive marker", encoding="utf-8")
        result = subprocess.run(
            ["python3", "scripts/check_curriculum.py"],
            cwd=candidate,
            capture_output=True,
            text=True,
            check=False,
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
