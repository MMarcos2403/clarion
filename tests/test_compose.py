from __future__ import annotations

import pytest

from clarion.compose import (
    PROFILES,
    Module,
    compose,
    load_modules,
    parse_module,
)

SAMPLE = """---
id: sample
order: 5
title: Sample Module
tags: [a, b]
profiles: [full, concise]
---
This is the body.
"""


def test_parse_module_reads_front_matter():
    m = parse_module(SAMPLE)
    assert m.id == "sample"
    assert m.order == 5
    assert m.title == "Sample Module"
    assert m.tags == ("a", "b")
    assert m.profiles == ("full", "concise")
    assert "This is the body." in m.body


def test_parse_module_requires_front_matter():
    with pytest.raises(ValueError):
        parse_module("no front matter here")


def test_modules_load_and_are_ordered():
    modules = load_modules()
    assert modules, "expected the repo to ship modules"
    orders = [m.order for m in modules]
    assert orders == sorted(orders)
    ids = {m.id for m in modules}
    assert {"mandate", "lead-with-outcome", "calibrate-confidence"} <= ids


@pytest.mark.parametrize("profile", sorted(PROFILES))
def test_every_profile_composes_nonempty(profile):
    prompt = compose(profile=profile)
    assert prompt.startswith("# Operating principles")
    assert len(prompt) > 200


def test_code_profile_includes_code_module_and_full_does_too():
    code = compose(profile="code")
    assert "Code discipline" in code
    concise = compose(profile="concise")
    assert "Code discipline" not in concise


def test_unknown_profile_raises():
    with pytest.raises(KeyError):
        compose(profile="does-not-exist")


def test_compose_accepts_injected_modules():
    mods = [
        Module(id="x", order=1, title="X", body="one", profiles=("full",)),
        Module(id="y", order=2, title="Y", body="two", profiles=("full",)),
    ]
    out = compose(profile="full", modules=mods)
    assert out.index("## X") < out.index("## Y")
