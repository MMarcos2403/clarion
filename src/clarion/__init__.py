"""Clarion — a portable output-discipline layer for LLMs.

Public API:
    compose(profile) -> str            Build the core system prompt.
    load_modules(path) -> list[Module] Load prompt modules from disk.
    Rubric.default() -> Rubric         The quality rubric.
    lint(text, rubric) -> LintReport   Score an LLM output against the rubric.
"""
from __future__ import annotations

from clarion.compose import Module, compose, load_modules
from clarion.lint import Finding, LintReport, lint
from clarion.rubric import Check, Rubric

__version__ = "0.1.0"

__all__ = [
    "Module",
    "compose",
    "load_modules",
    "Check",
    "Rubric",
    "Finding",
    "LintReport",
    "lint",
    "__version__",
]
