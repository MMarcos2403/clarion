# Benchmarks

## An honest note first

This project will not ship a "Clarion improves quality by 47%" banner. Output
quality is multi-dimensional and dataset-dependent; a single headline number
would be marketing, not measurement — and shipping one would violate the very
calibration principle Clarion exists to enforce.

What we give you instead is a **reproducible harness** so you can measure the
effect *on your own data*, which is the only number that should influence your
decision.

## What the linter can measure objectively

The heuristic linter is deterministic, so these are stable and honest:

| Dimension | How it's measured | What "good" looks like |
|-----------|-------------------|------------------------|
| Sycophancy rate | `no-sycophancy` fail % across a sample | → 0% |
| Filler-close rate | `no-filler-close` fail % | → 0% |
| Back-loaded answers | `leads-with-outcome` fail % | large drop |
| Structure/length mismatch | `structure-fits` fail % | drop |
| Mean discipline score | mean `lint().score` over the sample | rises, plateaus near 90 |

These are *discipline* metrics, not *correctness* metrics. Clarion targets the
former by design.

## Reproducing on your data

```python
from statistics import mean
from clarion import compose, lint

system = compose("full")
prompts = load_your_prompts()          # your representative queries

baseline = [call_model(p, system=None)   for p in prompts]
clarion  = [call_model(p, system=system) for p in prompts]

def summary(outputs):
    reports = [lint(o) for o in outputs]
    return {
        "mean_score": round(mean(r.score for r in reports), 1),
        "pass_rate": round(100 * sum(r.passed for r in reports) / len(reports)),
    }

print("baseline:", summary(baseline))
print("clarion :", summary(clarion))
```

## What the linter cannot measure

Correctness, factual accuracy, depth, and appropriateness are out of scope for a
regex linter — pair Clarion with a model-graded eval or human rating for those.
The roadmap's `clarion eval` will provide a model-judge harness for the subtle
dimensions; until then, treat linter scores as a *necessary-not-sufficient*
signal.
