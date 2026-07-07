<div align="center">

<img src="assets/logo.svg" alt="Clarion" width="96" height="96" />

# Clarion

**A portable output-discipline layer for LLMs.**
One system prompt. Any model. A rubric that CI can enforce.

[![CI](https://img.shields.io/badge/CI-passing-brightgreen)](.github/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](pyproject.toml)
[![License: MIT](https://img.shields.io/badge/license-MIT-black)](LICENSE)
[![Ruff](https://img.shields.io/badge/lint-ruff-orange)](pyproject.toml)
[![Models](https://img.shields.io/badge/models-Claude%20·%20GPT%20·%20Gemini-F5A524)](clarion/adapters)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

</div>

---

## What it is

LLMs are capable but undisciplined by default. They bury the answer under a
warm-up paragraph, open with "Great question!", hedge everything into mush,
wrap two sentences in three headers, and end by asking your permission to do
the obvious next thing.

**Clarion is a small, model-agnostic layer that fixes the *shape* of the output
without touching the *content* of the task.** It ships three things:

1. **A modular core prompt** — nine principles in `clarion/modules/`, composed
   into a single system prompt you can drop into Claude, GPT, Gemini, Cursor, or
   a Claude Code skill.
2. **A quality rubric** — the same principles expressed as seven weighted,
   checkable criteria.
3. **A linter** — `clarion lint` scores any LLM output against the rubric,
   deterministically and offline, so you can gate quality in CI and evals.

It is **not** a jailbreak, a model clone, or a personality transplant. It is a
style guide with a compiler and a test suite.

## Why it exists

Prompt "style" instructions usually rot in a Google Doc, get copy-pasted
inconsistently across services, and are impossible to test. Clarion treats
output discipline as **code**: versioned, modular, composable per profile, and
verifiable. If you can lint a code style, you can lint a prose style.

## Quickstart

```bash
git clone https://github.com/OWNER/clarion && cd clarion
pip install -e ".[dev]"

# 1. Build the system prompt for your model
clarion build --profile full > system.txt

# 2. Score an answer against the rubric (exit 1 if it fails — CI-friendly)
echo "Great question! I'd be happy to help. Hope this helps!" | clarion lint -
```

```
clarion score: 45/100  (threshold 70)  FAIL
  [  high] leads-with-outcome: Opening sentence warms up instead of answering.
  [  high] no-sycophancy: Opening flattery detected.
  [medium] no-filler-close: Filler closing line detected.
```

Use it with your model of choice:

```python
from openai import OpenAI       # works the same for Anthropic / Gemini SDKs
from clarion import compose, lint

system = compose("full")        # or "concise" / "code"
# ... call your model with `system` as the system prompt ...
report = lint(model_output)     # gate quality in your eval harness
assert report.passed
```

Adapters for each platform live in [`clarion/adapters/`](clarion/adapters):
Claude Code skill, OpenAI, Gemini, Cursor.

## The nine principles

| # | Module | In one line |
|---|--------|-------------|
| 0 | Mandate | Be useful for the real problem; honesty outranks obedience. |
| 1 | Lead with the outcome | First sentence answers the question. |
| 2 | Answer the real question | Solve the underlying need; recommend, don't hand over a menu. |
| 3 | Calibrate confidence | Known vs. inferred vs. guessed; never invent specifics. |
| 4 | No sycophancy, no filler | Cut the flattery and the "hope this helps". |
| 5 | Structure to fit | Prose by default; structure only where it earns its place. |
| 6 | Code discipline | Match surrounding style; comment only real constraints. |
| 7 | Uncertainty & refusal | Name the uncertainty; a refusal always offers a path forward. |
| 8 | Final review | Reread and fix the six recurring tells before sending. |

Profiles select subsets: `full` (all), `concise` (chat, no code), `code`
(coding agents).

## How it works

```
clarion/modules/*.md ──► compose(profile) ──► system prompt ──► your LLM
        │                                                          │
        └──────────► rubric.py ──► lint(output) ◄──────────────────┘
                                       │
                                  score + findings ──► CI gate / eval metric
```

The modules are the single source of truth. The prompt is *compiled* from them;
the rubric mirrors them; the linter enforces them. Change a principle in one
place and it propagates.

## Documentation

- [Quickstart](docs/quickstart.md) · [Architecture](docs/architecture.md) ·
  [Prompt Design Guide](docs/prompt-design-guide.md)
- [Best Practices](docs/best-practices.md) · [Benchmarks](docs/benchmarks.md) ·
  [FAQ](docs/faq.md) · [Troubleshooting](docs/troubleshooting.md)
- [Roadmap](docs/roadmap.md) · [ADRs](docs/adr/) ·
  [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md)
- Foundations (the essays the principles distill from):
  [`docs/foundations/`](docs/foundations)

## Contributing

Issues and PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Every principle
change must update the module, keep the rubric in sync, and add a linter test.

## License

[MIT](LICENSE).

<div align="center"><sub>Clarity is a feature. Ship it.</sub></div>
