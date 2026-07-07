# ADR-0002: A heuristic linter before a model-graded judge

- Status: Accepted
- Date: 2026-07-07

## Context

The rubric needs enforcement. Two obvious implementations: a deterministic
heuristic checker, or an LLM-as-judge that scores outputs against the rubric.

## Decision

Ship the **heuristic linter first** as the core enforcement mechanism. Treat a
model-graded eval as a **future complement** (`clarion eval`, v0.2), not the
foundation.

## Rationale

The core must run on every commit in CI, for free, without an API key, and give
the same score every time. A model judge fails all four: it costs money, needs
keys, adds latency, and varies run to run. The heuristic checker catches the
high-frequency mechanical failures (flattery, filler, arrow chains, permission
theater, structure/length mismatch), which is where most of the value is.

## Consequences

**Positive**: deterministic, offline, fast, testable — enforcement can gate CI.

**Negative**: it cannot judge subtle dimensions (depth, correctness, tone
nuance) and can have false positives (e.g. `->` in code). We document this
prominently so nobody mistakes the score for a quality ceiling, and we scope the
model judge to fill the gap.

## Alternatives considered

- **Model judge as the core.** Rejected for the CI/determinism reasons above.
- **No enforcement, prompt only.** Rejected: an unenforced style guide regresses
  silently on every prompt or model change.
