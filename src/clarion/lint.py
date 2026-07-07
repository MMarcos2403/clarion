"""A heuristic linter for LLM outputs, scored against the Clarion rubric.

This is deliberately a *heuristic* tool, not a model-based judge. It catches the
mechanical tells of low-discipline output — flattery openers, filler closers,
arrow-chain shorthand, permission theater, structure that doesn't fit — fast,
offline, and deterministically. It is meant to run in CI and pre-commit, and to
be paired with (not replace) a model-graded eval for the subtler dimensions.

Each rubric check maps to one detector. A detector returns a list of Findings
plus a 0.0–1.0 pass fraction for its check; the weighted sum becomes the score.
"""
from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass

from clarion.rubric import Rubric, severity_rank

# A detector inspects the output and returns (pass_fraction, findings) for one
# rubric check.
Detector = Callable[[str], "tuple[float, list[Finding]]"]


@dataclass(frozen=True)
class Finding:
    check_id: str
    severity: str
    message: str
    excerpt: str = ""


@dataclass(frozen=True)
class LintReport:
    score: int
    threshold: int
    findings: tuple[Finding, ...]

    @property
    def passed(self) -> bool:
        return self.score >= self.threshold

    def sorted_findings(self) -> list[Finding]:
        return sorted(self.findings, key=lambda f: severity_rank(f.severity))


# --- detectors ------------------------------------------------------------

_SYCOPHANCY = re.compile(
    r"\b(great|excellent|fantastic|wonderful|brilliant)\s+(question|point|idea)\b"
    r"|\bi'?d\s+be\s+happy\s+to\b"
    r"|\bwhat\s+a\s+great\b",
    re.IGNORECASE,
)
_FILLER_CLOSE = re.compile(
    r"\b(hope\s+this\s+helps"
    r"|let\s+me\s+know\s+if\s+you\s+(need|have)"
    r"|feel\s+free\s+to\s+(ask|reach)"
    r"|happy\s+to\s+help)\b",
    re.IGNORECASE,
)
_ARROW = re.compile(r"\s(->|→|=>)\s")
_HEDGE = re.compile(
    r"\b(might|maybe|perhaps|possibly|could|potentially|somewhat|arguably|"
    r"i\s+think|it\s+seems|kind\s+of|sort\s+of)\b",
    re.IGNORECASE,
)
_PERMISSION = re.compile(
    r"(would\s+you\s+like\s+me\s+to"
    r"|do\s+you\s+want\s+me\s+to"
    r"|shall\s+i"
    r"|should\s+i\s+(go\s+ahead|proceed))\b",
    re.IGNORECASE,
)
_HEADER = re.compile(r"^\s{0,3}#{1,6}\s", re.MULTILINE)
_QUESTION_ECHO = re.compile(r"^(so|well|sure|of\s+course|great|certainly|let'?s|to\s+answer)",
                            re.IGNORECASE)


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]


def _first_sentence(text: str) -> str:
    sents = _sentences(text)
    return sents[0] if sents else ""


def _check_leads_with_outcome(text: str) -> tuple[float, list[Finding]]:
    first = _first_sentence(text)
    if not first:
        return 1.0, []
    if _QUESTION_ECHO.match(first) or _SYCOPHANCY.search(first):
        return 0.0, [Finding("leads-with-outcome", "high",
                             "Opening sentence warms up instead of answering.",
                             first[:120])]
    return 1.0, []


def _regex_check(text: str, check_id: str, severity: str, pattern: re.Pattern[str],
                 message: str) -> tuple[float, list[Finding]]:
    matches = list(pattern.finditer(text))
    if not matches:
        return 1.0, []
    excerpt = matches[0].group(0)
    return 0.0, [Finding(check_id, severity, message, excerpt)]


def _check_calibrated_language(text: str) -> tuple[float, list[Finding]]:
    words = max(len(re.findall(r"\w+", text)), 1)
    hedges = len(_HEDGE.findall(text))
    density = hedges / words
    # Some hedging is healthy; only stacked hedging fails.
    if density > 0.06 and hedges >= 4:
        return 0.0, [Finding("calibrated-language", "medium",
                             f"Hedging is stacked ({hedges} qualifiers in {words} words).")]
    return 1.0, []


def _check_structure_fits(text: str) -> tuple[float, list[Finding]]:
    words = len(re.findall(r"\w+", text))
    headers = len(_HEADER.findall(text))
    if words < 120 and headers >= 2:
        return 0.0, [Finding("structure-fits", "medium",
                             f"{headers} headers wrap only {words} words of content.")]
    return 1.0, []


def lint(text: str, rubric: Rubric | None = None) -> LintReport:
    """Score ``text`` against ``rubric`` (defaults to ``Rubric.default()``)."""
    rubric = rubric or Rubric.default()

    detectors: dict[str, Detector] = {
        "leads-with-outcome": _check_leads_with_outcome,
        "no-sycophancy": lambda t: _regex_check(
            t, "no-sycophancy", "high", _SYCOPHANCY, "Opening flattery detected."),
        "no-filler-close": lambda t: _regex_check(
            t, "no-filler-close", "medium", _FILLER_CLOSE, "Filler closing line detected."),
        "calibrated-language": _check_calibrated_language,
        "no-arrow-chains": lambda t: _regex_check(
            t, "no-arrow-chains", "medium", _ARROW, "Arrow-chain shorthand instead of prose."),
        "structure-fits": _check_structure_fits,
        "no-permission-theater": lambda t: _regex_check(
            t, "no-permission-theater", "low", _PERMISSION,
            "Asks permission for a next step instead of taking it."),
    }

    earned = 0.0
    findings: list[Finding] = []
    for check in rubric.checks:
        detector = detectors.get(check.id)
        if detector is None:  # pragma: no cover - guards rubric/detector drift
            continue
        fraction, check_findings = detector(text)
        earned += fraction * check.weight
        findings.extend(check_findings)

    score = round(100 * earned / rubric.total_weight)
    return LintReport(score=score, threshold=rubric.threshold, findings=tuple(findings))
