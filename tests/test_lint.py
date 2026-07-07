from __future__ import annotations

from clarion.lint import lint
from clarion.rubric import Rubric

CLEAN = (
    "Use Postgres. Your access pattern is relational and your scale fits a "
    "single node, so the reasons teams reach for something else do not apply "
    "yet. If you later need horizontal writes, revisit Citus at that point."
)

SYCOPHANTIC = (
    "Great question! I'd be happy to help you with this. So, to answer your "
    "question, you should probably maybe consider using a database perhaps."
)

FILLER = "The answer is 42. Hope this helps! Let me know if you need anything else."

ARROWS = "The flow is simple: request -> handler -> db -> response. Done."


def test_clean_output_passes():
    report = lint(CLEAN)
    assert report.passed
    assert report.score >= 90


def test_sycophancy_is_flagged():
    report = lint(SYCOPHANTIC)
    ids = {f.check_id for f in report.findings}
    assert "no-sycophancy" in ids
    assert "leads-with-outcome" in ids
    assert not report.passed


def test_filler_close_is_flagged():
    report = lint(FILLER)
    ids = {f.check_id for f in report.findings}
    assert "no-filler-close" in ids


def test_arrow_chains_are_flagged():
    report = lint(ARROWS)
    ids = {f.check_id for f in report.findings}
    assert "no-arrow-chains" in ids


def test_threshold_override_changes_pass():
    strict = Rubric(1, 100, Rubric.default().checks)
    report = lint(ARROWS, strict)
    assert not report.passed


def test_findings_sorted_by_severity():
    report = lint(SYCOPHANTIC)
    ranks = [f.severity for f in report.sorted_findings()]
    # high severity should not come after a lower one
    order = {"high": 0, "medium": 1, "low": 2}
    assert ranks == sorted(ranks, key=lambda s: order[s])
