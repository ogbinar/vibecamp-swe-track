"""Small reproducible load seam; run only after the learner feed endpoint exists."""

import argparse
import time

import httpx

parser = argparse.ArgumentParser()
parser.add_argument("--url", default="http://127.0.0.1:8003/feed?limit=20")
parser.add_argument("--requests", type=int, default=20)
args = parser.parse_args()

durations: list[float] = []
errors = 0
with httpx.Client(timeout=2.0) as client:
    for _ in range(args.requests):
        started = time.perf_counter()
        response = client.get(args.url)
        durations.append(time.perf_counter() - started)
        errors += int(response.status_code >= 400)

ordered = sorted(durations)
p95 = ordered[max(0, int(len(ordered) * 0.95) - 1)]
print({"requests": len(ordered), "errors": errors, "p95_seconds": round(p95, 6)})
