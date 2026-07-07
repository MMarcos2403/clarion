# ADR-0001: A model-agnostic core with thin adapters

- Status: Accepted
- Date: 2026-07-07

## Context

Prompt-style guidance tends to be written for one model and one SDK, then
copy-pasted and mutated across others until the versions disagree. We want one
discipline layer usable from Claude, GPT, Gemini, Cursor, and Claude Code
without maintaining divergent copies.

## Decision

Keep the **core a plain-text system prompt** compiled from Markdown modules,
with **no model-specific tokens or hacks**. Per-platform integration lives in
thin *adapters* that only show how to inject `compose(profile)` into that
platform's system-instruction slot.

## Consequences

**Positive**
- One source of truth; adapters are ~30 lines and rarely change.
- Portability is a property of the design, not an afterthought.
- New platforms cost an adapter, not a rewrite.

**Negative**
- We forgo model-specific optimizations that might squeeze out extra compliance
  on a single model. We accept this: portability and maintainability outweigh
  marginal per-model gains, and such hacks are brittle across model upgrades.

## Alternatives considered

- **Per-model prompt files.** Rejected: guarantees drift, multiplies maintenance.
- **A runtime framework that wraps each SDK.** Rejected: couples us to fast-moving
  SDKs and expands scope far beyond "output discipline".
