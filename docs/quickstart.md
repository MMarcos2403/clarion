# Quickstart

Five minutes from clone to a linted, model-agnostic system prompt.

## Install

```bash
git clone https://github.com/OWNER/clarion && cd clarion
pip install -e ".[dev]"     # or just ".[dev]" omitted for runtime only
```

Clarion has **zero runtime dependencies**. The `dev` extra pulls in pytest,
ruff, and mypy for contributors.

## 1. Build a system prompt

```bash
clarion build --profile full        # every principle
clarion build --profile concise     # chat, no code-specific guidance
clarion build --profile code -o system.txt   # coding agents, written to a file
```

The output is plain Markdown — paste it into any model's system slot, or load it
programmatically:

```python
from clarion import compose
system = compose("code")
```

## 2. Wire it into your model

Pick the adapter for your platform:

```bash
clarion adapters                 # list them
clarion adapters openai.md       # print one
```

Minimal OpenAI example:

```python
from openai import OpenAI
from clarion import compose

client = OpenAI()
resp = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system", "content": compose("full")},
        {"role": "user", "content": "Should we rewrite the billing service in Rust?"},
    ],
)
```

## 3. Lint the output

```bash
echo "Great question! I'd be happy to help. Hope this helps!" | clarion lint -
# → score 45/100 FAIL, with the specific violations
```

In an eval harness:

```python
from clarion import lint
report = lint(model_output)
assert report.passed, [f.message for f in report.findings]
```

`clarion lint` exits non-zero on failure, so it drops straight into CI or a
pre-commit hook.

## Next

- [Architecture](architecture.md) — how the three layers fit together.
- [Prompt Design Guide](prompt-design-guide.md) — why each principle is written
  the way it is.
- [Best Practices](best-practices.md) — getting the most out of it in production.
