"""Command-line interface for Clarion.

    clarion build   [--profile full] [-o FILE]   Assemble the core system prompt.
    clarion lint    FILE|-  [--threshold N] [--json]   Score an LLM output.
    clarion rubric  [--export yaml]               Print the quality rubric.
    clarion adapters [NAME]                        List or print an adapter wrapper.

Exit codes: 0 on success; `lint` exits 1 when the score is below threshold, so it
can gate CI.
"""
from __future__ import annotations

import argparse
import contextlib
import json
import sys
from pathlib import Path

from clarion import __version__
from clarion.compose import PROFILES, compose
from clarion.lint import lint
from clarion.rubric import Rubric


def _force_utf8_stdio() -> None:
    """Ensure UTF-8 output regardless of the platform's console codepage.

    Windows consoles default to a legacy codepage (e.g. cp1252) that cannot
    encode the glyphs the prompt and reports use. Reconfiguring is a no-op on
    platforms that already default to UTF-8.
    """
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            with contextlib.suppress(ValueError, OSError):  # detached streams
                reconfigure(encoding="utf-8", errors="replace")


def _read_input(source: str) -> str:
    if source == "-":
        return sys.stdin.read()
    return Path(source).read_text(encoding="utf-8")


def _cmd_build(args: argparse.Namespace) -> int:
    prompt = compose(profile=args.profile)
    if args.out:
        Path(args.out).write_text(prompt, encoding="utf-8")
        print(f"wrote {args.out} ({len(prompt)} chars, profile={args.profile})",
              file=sys.stderr)
    else:
        print(prompt)
    return 0


def _cmd_lint(args: argparse.Namespace) -> int:
    text = _read_input(args.file)
    rubric = Rubric.default()
    if args.threshold is not None:
        rubric = Rubric(rubric.version, args.threshold, rubric.checks)
    report = lint(text, rubric)

    if args.json:
        print(json.dumps({
            "score": report.score,
            "threshold": report.threshold,
            "passed": report.passed,
            "findings": [f.__dict__ for f in report.sorted_findings()],
        }, indent=2))
    else:
        status = "PASS" if report.passed else "FAIL"
        print(f"clarion score: {report.score}/100  (threshold {report.threshold})  {status}")
        for f in report.sorted_findings():
            print(f"  [{f.severity:>6}] {f.check_id}: {f.message}")
            if f.excerpt:
                print(f"           ↳ {f.excerpt!r}")
        if not report.findings:
            print("  no findings")
    return 0 if report.passed else 1


def _cmd_rubric(args: argparse.Namespace) -> int:
    rubric = Rubric.default()
    if args.export == "yaml":
        print(rubric.to_yaml(), end="")
        return 0
    print(f"Clarion rubric v{rubric.version} — threshold {rubric.threshold}/100\n")
    for c in rubric.checks:
        print(f"  {c.weight:>3}pt [{c.severity:>6}] {c.id}\n        {c.description}")
    return 0


def _cmd_adapters(args: argparse.Namespace) -> int:
    root = Path(__file__).resolve()
    adapters_dir = None
    for base in [root, *root.parents]:
        candidate = base / "clarion" / "adapters"
        if candidate.is_dir():
            adapters_dir = candidate
            break
    if adapters_dir is None:
        print("adapters directory not found", file=sys.stderr)
        return 2
    available = sorted(p.name for p in adapters_dir.iterdir())
    if not args.name:
        print("available adapters:")
        for name in available:
            print(f"  {name}")
        return 0
    target = adapters_dir / args.name
    if target.is_dir():
        target = next(target.glob("*"), None)
    if target is None or not target.exists():
        print(f"unknown adapter {args.name!r}; try one of {available}", file=sys.stderr)
        return 2
    print(target.read_text(encoding="utf-8"))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="clarion", description=__doc__.splitlines()[0])
    parser.add_argument("--version", action="version", version=f"clarion {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    p_build = sub.add_parser("build", help="assemble the core system prompt")
    p_build.add_argument("--profile", choices=sorted(PROFILES), default="full")
    p_build.add_argument("-o", "--out", help="write to FILE instead of stdout")
    p_build.set_defaults(func=_cmd_build)

    p_lint = sub.add_parser("lint", help="score an LLM output against the rubric")
    p_lint.add_argument("file", help="path to a text file, or - for stdin")
    p_lint.add_argument("--threshold", type=int, help="override the pass mark")
    p_lint.add_argument("--json", action="store_true", help="machine-readable output")
    p_lint.set_defaults(func=_cmd_lint)

    p_rubric = sub.add_parser("rubric", help="print the quality rubric")
    p_rubric.add_argument("--export", choices=["yaml"], help="export format")
    p_rubric.set_defaults(func=_cmd_rubric)

    p_adapters = sub.add_parser("adapters", help="list or print an adapter wrapper")
    p_adapters.add_argument("name", nargs="?", help="adapter to print")
    p_adapters.set_defaults(func=_cmd_adapters)

    return parser


def main(argv: list[str] | None = None) -> int:
    _force_utf8_stdio()
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
