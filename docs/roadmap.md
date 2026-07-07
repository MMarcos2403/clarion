# Roadmap

Directional, not a promise. Ordered by leverage.

## v0.1 — Foundation (shipped)
- Nine modular principles, three profiles.
- Compose + rubric + heuristic linter.
- CLI (`build`, `lint`, `rubric`, `adapters`).
- Adapters: Claude Code, OpenAI, Gemini, Cursor.
- CI across 3 OSes × 4 Python versions; packaging; docs.

## v0.2 — Verification depth
- `clarion eval`: a model-graded harness for the dimensions regex can't judge
  (correctness-adjacent style, tone appropriateness). Pluggable judge backend.
- Golden-set fixtures: curated good/bad outputs per principle, used in tests.
- Fenced-code-aware linting (don't flag `->` inside code blocks).

## v0.3 — Reach
- More adapters: LangChain, LlamaIndex, Anthropic Messages API, Vercel AI SDK.
- Localized module sets (Spanish foundations already exist under
  `docs/foundations/`); a locale-aware `compose(locale=...)`.
- `pre-commit` hook published to the pre-commit registry.

## v0.4 — Ecosystem
- VS Code extension surfacing lint findings on selected model output.
- A hosted playground (paste output → see the rubric breakdown).
- Published PyPI package with trusted publishing.

## Non-goals
- Becoming a full prompt framework or agent runtime. Clarion is one layer and
  intends to stay small.
- Model-specific jailbreaks or persona cloning. Out of scope, permanently.
- A single headline "quality uplift" number. See
  [benchmarks.md](benchmarks.md) for why.

Have a use case that would reorder this? Open a discussion.
