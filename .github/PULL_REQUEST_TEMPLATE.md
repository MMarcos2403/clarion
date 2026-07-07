<!-- Keep the title in Conventional Commit form, e.g. "feat: add refusal detector" -->

## What and why

<!-- One paragraph: what changes and what problem it solves. Lead with the outcome. -->

## The three-layer rule

If this PR touches a principle, confirm all three moved together:

- [ ] Module updated in `clarion/modules/`
- [ ] Rubric updated in `src/clarion/rubric.py` (and `make rubric` run)
- [ ] Linter detector + test updated in `src/clarion/lint.py` and `tests/`

## Checklist

- [ ] `make check` passes locally (ruff, mypy, pytest)
- [ ] Docs updated if behavior/CLI changed
- [ ] CHANGELOG entry added under `[Unreleased]`
- [ ] No new runtime dependencies (or justified below)

## Notes for the reviewer

<!-- Anything non-obvious, trade-offs considered, or follow-ups deferred. -->
