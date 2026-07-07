# Architecture

Clarion has one idea: **treat output discipline as code.** Everything else
follows from making that idea real — versioned, composable, and testable.

## The three layers

```
          ┌──────────────────────────────────────────────┐
          │  clarion/modules/*.md   (source of truth)     │
          │  nine principles, each with front-matter      │
          └───────────────┬──────────────────────────────┘
                          │
        compose(profile)  │  mirrors        rubric.py
                          ▼                    │
          ┌───────────────────────┐           ▼
          │  system prompt (text) │   ┌──────────────────┐
          │  → Claude/GPT/Gemini  │   │  Rubric (7 checks)│
          └───────────────────────┘   └────────┬─────────┘
                                                │
                            lint(output) uses ──┘
                                                ▼
                                    ┌──────────────────────┐
                                    │  LintReport: score +  │
                                    │  findings → CI gate   │
                                    └──────────────────────┘
```

1. **Modules** (`clarion/modules/*.md`) are the source of truth. Each is a
   Markdown file with front-matter (`id`, `order`, `title`, `tags`, `profiles`)
   and a body. Prose lives here, not in Python string literals — so principles
   read well, diff cleanly, and translate.

2. **Compose** (`src/clarion/compose.py`) parses modules, filters by *profile*,
   orders by `order`, and concatenates them into a system prompt. Profiles
   (`full`, `concise`, `code`) trade breadth against token budget.

3. **Rubric + lint** (`src/clarion/rubric.py`, `lint.py`) express the same
   principles as weighted, machine-checkable criteria and enforce them on
   outputs. The rubric is code-first; `rubric.yaml` is a generated mirror that
   CI checks for drift.

## Why modules instead of one big prompt

- **Composability.** A coding agent needs the code module; a chat product
  doesn't. Profiles select subsets without maintaining divergent copies.
- **Reviewability.** A change to one principle is a one-file diff, not a hunt
  through a 2,000-word blob.
- **Testability.** Each module maps to a rubric check maps to a linter detector
  maps to a test. The chain is what keeps the prompt honest over time.

## Why a heuristic linter (not a model judge) at the core

The linter is deliberately regex-and-rules, not an LLM call. That buys three
properties the core needs:

| Property | Heuristic linter | Model judge |
|----------|------------------|-------------|
| Deterministic | ✅ same input → same score | ❌ sampling variance |
| Offline / free | ✅ runs in CI with no keys | ❌ needs an API |
| Fast | ✅ microseconds | ❌ network round-trip |
| Subtle judgment | ❌ catches mechanical tells only | ✅ nuance |

The mechanical tells (flattery openers, filler closers, arrow chains, permission
theater, structure/length mismatch) are exactly the high-frequency failures, so
a cheap detector catches most of the value. A model-graded eval (`clarion eval`,
on the roadmap) is the complement for the subtle dimensions — not a replacement.

## Data flow for `clarion lint`

```
text ──► for each rubric check:
             detector(text) → (pass_fraction, [findings])
         weighted sum of fractions × 100 ──► score
         score ≥ threshold ──► passed
```

Each detector owns exactly one check. Adding a principle means adding a module,
a `Check`, a detector, and a test — see [CONTRIBUTING](../CONTRIBUTING.md).

## Design decisions

Recorded as ADRs in [`docs/adr/`](adr/). Start with
[ADR-0001: model-agnostic core](adr/0001-model-agnostic-core.md).
