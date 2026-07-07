# Contributing to Clarion

Thanks for considering a contribution. Clarion is small on purpose; the bar for
what goes in is high on purpose. This guide keeps both true.

## The golden rule

The modules in `clarion/modules/` are the single source of truth. A change to a
principle is only complete when all three layers move together:

1. **Module** — the Markdown file that states the principle.
2. **Rubric** — a corresponding check in `src/clarion/rubric.py` (if the
   principle is machine-checkable).
3. **Linter + test** — a detector in `src/clarion/lint.py` and a test in
   `tests/` proving it catches a real violation and passes clean text.

A PR that edits a module without updating the rubric and tests will be asked to
finish the job.

## Development setup

```bash
pip install -e ".[dev]"
make check          # lint + type + test — this is exactly what CI runs
```

## Standards

- **Style:** `ruff format` and `ruff check` must pass. Line length 100.
- **Types:** `mypy --strict` must pass. The package is typed.
- **Tests:** new behavior needs a test. Keep tests deterministic and offline —
  the linter must never call a network or a model.
- **Commits:** use [Conventional Commits](https://www.conventionalcommits.org/)
  (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`). The release
  workflow derives the changelog from them.

## Proposing a new principle

Open an issue first using the **Feature request** template. A new principle has
to clear three questions:

1. Is it *observable* — can you tell from the output alone whether it was
   followed?
2. Is it *model-agnostic* — does it hold for Claude, GPT, and Gemini alike?
3. Does it *change behavior* — or is it already implied by an existing module?

Principles that fail (1) belong in the docs as guidance, not in a module.

## Adding an adapter

Adapters are thin. Add a file under `clarion/adapters/`, show how to inject
`compose(profile)` into that platform's system-instruction slot, and note any
profile recommendation. Keep it under ~40 lines.

## Code of Conduct

Participation is governed by our [Code of Conduct](CODE_OF_CONDUCT.md).
