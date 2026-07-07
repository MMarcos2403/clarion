# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Dropped Python 3.9 (end-of-life; pytest 9 and mypy both require 3.10+). The
  supported range is now 3.10–3.13, resolving a dependency-update conflict.

### Planned
- Model-graded eval harness (`clarion eval`) to complement the heuristic linter.
- Additional adapters: LangChain, LlamaIndex, Anthropic Messages API example.
- Localized module sets (the foundations already exist in Spanish).

## [0.1.0] — 2026-07-07

### Added
- Nine modular principle files in `clarion/modules/`, composable by profile
  (`full`, `concise`, `code`).
- `clarion` Python package: `compose`, `load_modules`, `Rubric`, `lint`.
- `clarion` CLI: `build`, `lint`, `rubric`, `adapters`.
- Seven-criterion quality rubric with a deterministic heuristic linter.
- Adapters for Claude Code, OpenAI, Gemini, and Cursor.
- Full documentation set, CI, and packaging.
- Cross-platform UTF-8 console handling (fixes Windows cp1252 crash).

[Unreleased]: https://github.com/OWNER/clarion/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/OWNER/clarion/releases/tag/v0.1.0
