# Troubleshooting

### `clarion: command not found`
The console script installs with the package. Run `pip install -e .` from the
repo root, and make sure your environment's `Scripts`/`bin` directory is on
`PATH`. As a fallback, `python -m clarion.cli ...` always works.

### `FileNotFoundError: could not locate clarion/modules`
`compose()` finds modules by walking up from the source file and the current
directory. This triggers when you've installed the wheel somewhere the
`clarion/modules` data isn't adjacent. Fixes:
- Run from a source checkout, or
- Pass an explicit path: `load_modules("/path/to/clarion/modules")`, or
- Install with the data included (the wheel force-includes it; a stripped
  install may not).

### `UnicodeEncodeError` on Windows
Fixed in 0.1.0 — the CLI forces UTF-8 on stdout/stderr. If you call the library
directly and print prompts yourself on a legacy console, set
`PYTHONUTF8=1` or reconfigure your stream to UTF-8.

### CI fails on "clarion/rubric.yaml is stale"
The YAML is a generated mirror of `rubric.py`. Run `make rubric` (or
`clarion rubric --export yaml > clarion/rubric.yaml`) and commit the result.

### `clarion lint` fails a response I think is fine
The linter flags mechanical tells, and it can have false positives — e.g. a
legitimate `->` inside a code snippet. Two options:
- Lint only the prose portion, not fenced code blocks, or
- Lower the threshold for that context with `--threshold`.
If you find a systematic false positive, open a bug — the detector should be
tightened.

### mypy or ruff errors after editing
Run `make check` locally to see exactly what CI will see. The project is
`mypy --strict`; new code needs annotations.
