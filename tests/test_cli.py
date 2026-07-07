from __future__ import annotations

import json

import pytest

from clarion.cli import main


def test_build_prints_prompt(capsys):
    rc = main(["build", "--profile", "concise"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "# Operating principles" in out


def test_build_writes_file(tmp_path):
    target = tmp_path / "prompt.md"
    rc = main(["build", "--out", str(target)])
    assert rc == 0
    assert target.read_text(encoding="utf-8").startswith("# Operating principles")


def test_lint_clean_stdin_passes(monkeypatch, capsys):
    import io
    monkeypatch.setattr("sys.stdin", io.StringIO(
        "Use Postgres; your workload fits one node and needs relational queries."))
    rc = main(["lint", "-"])
    assert rc == 0
    assert "PASS" in capsys.readouterr().out


def test_lint_bad_output_fails_and_exits_nonzero(tmp_path, capsys):
    f = tmp_path / "bad.txt"
    f.write_text("Great question! Hope this helps!", encoding="utf-8")
    rc = main(["lint", str(f)])
    assert rc == 1


def test_lint_json_is_valid(tmp_path, capsys):
    f = tmp_path / "x.txt"
    f.write_text("The answer is 42. Hope this helps!", encoding="utf-8")
    main(["lint", str(f), "--json"])
    payload = json.loads(capsys.readouterr().out)
    assert "score" in payload and "findings" in payload


def test_rubric_export_yaml_roundtrips(capsys):
    main(["rubric", "--export", "yaml"])
    out = capsys.readouterr().out
    assert "checks:" in out and "leads-with-outcome" in out


def test_missing_subcommand_errors():
    with pytest.raises(SystemExit):
        main([])
