"""Runnable demo: score a batch of outputs and print a summary.

    python examples/eval_demo.py

No API keys or network needed — it lints canned samples so you can see the
harness shape before pointing it at your own model outputs.
"""
from __future__ import annotations

from statistics import mean

from clarion import lint

SAMPLES = {
    "back-loaded + flattery": (
        "Great question! It really depends on many factors, so let's explore "
        "them one by one before we get to an answer."
    ),
    "hedge wall": (
        "It might possibly perhaps be the cache, though it could maybe be "
        "something else and it's really hard to say for sure."
    ),
    "filler close": (
        "The migration is complete. Hope this helps! Let me know if you need "
        "anything else."
    ),
    "disciplined": (
        "Use Postgres. Your workload is relational and fits one node, so the "
        "reasons to reach for NoSQL don't apply yet; revisit when you need "
        "multi-region writes."
    ),
}


def main() -> None:
    reports = {name: lint(text) for name, text in SAMPLES.items()}
    width = max(len(n) for n in SAMPLES)
    for name, report in reports.items():
        status = "PASS" if report.passed else "FAIL"
        tags = ", ".join(sorted({f.check_id for f in report.findings})) or "clean"
        print(f"{name:<{width}}  {report.score:>3}/100  {status}  ({tags})")
    print("-" * (width + 24))
    print(f"{'mean score':<{width}}  {round(mean(r.score for r in reports.values())):>3}/100")


if __name__ == "__main__":
    main()
