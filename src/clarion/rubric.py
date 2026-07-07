"""The Clarion quality rubric — the canonical, code-first source of truth.

``clarion/rubric.yaml`` is a generated mirror for humans; this module is what the
linter and tests use. Keeping one source avoids drift.
"""
from __future__ import annotations

from dataclasses import dataclass

Severity = str  # "high" | "medium" | "low"

_SEVERITY_ORDER: dict[Severity, int] = {"high": 0, "medium": 1, "low": 2}


@dataclass(frozen=True)
class Check:
    id: str
    name: str
    weight: int
    severity: Severity
    description: str


@dataclass(frozen=True)
class Rubric:
    version: int
    threshold: int
    checks: tuple[Check, ...]

    def by_id(self, check_id: str) -> Check:
        for check in self.checks:
            if check.id == check_id:
                return check
        raise KeyError(check_id)

    @property
    def total_weight(self) -> int:
        return sum(c.weight for c in self.checks)

    @classmethod
    def default(cls) -> Rubric:
        return cls(
            version=1,
            threshold=70,
            checks=(
                Check("leads-with-outcome", "Leads with the outcome", 20, "high",
                      "First sentence answers the question rather than restating it."),
                Check("no-sycophancy", "No sycophancy", 15, "high",
                      "No opening flattery."),
                Check("no-filler-close", "No filler close", 10, "medium",
                      "No empty closing lines."),
                Check("calibrated-language", "Calibrated language", 15, "medium",
                      "Hedging where warranted, not stacked into meaningless chains."),
                Check("no-arrow-chains", "Full sentences, not arrow chains", 10, "medium",
                      "Avoids telegraphic A -> B -> C shorthand."),
                Check("structure-fits", "Structure fits length", 15, "medium",
                      "No heavy structure wrapping a short answer."),
                Check("no-permission-theater", "No permission theater", 15, "low",
                      "Doesn't ask permission for the obvious reversible next step."),
            ),
        )

    def to_yaml(self) -> str:
        """Render the rubric as YAML without a third-party dependency."""
        lines = [
            "# Clarion quality rubric — generated from clarion/rubric.py.",
            f"version: {self.version}",
            "scale: 0-100",
            f"threshold: {self.threshold}",
            "",
            "checks:",
        ]
        for c in self.checks:
            lines += [
                f"  - id: {c.id}",
                f"    name: {c.name}",
                f"    weight: {c.weight}",
                f"    severity: {c.severity}",
                f"    description: {c.description}",
            ]
        return "\n".join(lines) + "\n"


def severity_rank(severity: Severity) -> int:
    return _SEVERITY_ORDER.get(severity, 99)
