"""Compose the Clarion core system prompt from modular Markdown files.

Modules live in ``clarion/modules/*.md`` at the repo root. Each has a small
front-matter block and a Markdown body:

    ---
    id: lead-with-outcome
    order: 10
    title: Lead with the outcome
    tags: [structure, clarity]
    profiles: [full, concise, code]
    ---
    <body>

A *profile* selects which modules assemble into a prompt. This keeps the core
model-agnostic and lets callers trade breadth for token budget.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

# Profiles are ordered subsets, resolved by module id. "full" means "every
# module that lists this profile" and is handled specially in ``compose``.
PROFILES: dict[str, str] = {
    "full": "Every principle. Use as a standalone system prompt.",
    "concise": "The load-bearing principles, minus code-specific guidance.",
    "code": "Full set tuned for coding agents.",
}

_FRONT_MATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)


@dataclass(frozen=True)
class Module:
    """A single prompt module parsed from a Markdown file."""

    id: str
    order: int
    title: str
    body: str
    tags: tuple[str, ...] = ()
    profiles: tuple[str, ...] = ()
    source: Path | None = field(default=None, compare=False)

    def render(self) -> str:
        return f"## {self.title}\n\n{self.body.strip()}\n"


def _parse_scalar_list(value: str) -> tuple[str, ...]:
    """Parse ``[a, b, c]`` or a bare comma list into a tuple of strings."""
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    parts = [p.strip() for p in value.split(",")]
    return tuple(p for p in parts if p)


def _parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    match = _FRONT_MATTER.match(text)
    if not match:
        raise ValueError("module is missing a '--- ... ---' front-matter block")
    raw, body = match.group(1), match.group(2)
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"malformed front-matter line: {line!r}")
        key, _, val = line.partition(":")
        meta[key.strip()] = val.strip()
    return meta, body


def parse_module(text: str, source: Path | None = None) -> Module:
    meta, body = _parse_front_matter(text)
    try:
        return Module(
            id=meta["id"],
            order=int(meta["order"]),
            title=meta["title"],
            body=body,
            tags=_parse_scalar_list(meta.get("tags", "")),
            profiles=_parse_scalar_list(meta.get("profiles", "")),
            source=source,
        )
    except KeyError as exc:  # pragma: no cover - defensive
        raise ValueError(f"module missing required field {exc}") from exc


def default_modules_dir() -> Path:
    """Locate ``clarion/modules`` by walking up from this file, then the cwd.

    Works for an editable/source checkout. When packaged, callers should pass an
    explicit path or rely on ``importlib.resources`` (see docs/architecture.md).
    """
    starts = [Path(__file__).resolve(), Path.cwd().resolve()]
    for start in starts:
        for base in [start, *start.parents]:
            candidate = base / "clarion" / "modules"
            if candidate.is_dir():
                return candidate
    raise FileNotFoundError("could not locate clarion/modules; pass an explicit path")


def load_modules(path: str | Path | None = None) -> list[Module]:
    """Load and order all modules from ``path`` (defaults to the repo modules)."""
    directory = Path(path) if path is not None else default_modules_dir()
    modules = [
        parse_module(p.read_text(encoding="utf-8"), source=p)
        for p in sorted(directory.glob("*.md"))
    ]
    modules.sort(key=lambda m: m.order)
    return modules


HEADER = (
    "# Operating principles\n\n"
    "You follow the principles below in every response. They are ordered; when "
    "two conflict, the earlier one wins.\n"
)


def compose(profile: str = "full", modules: list[Module] | None = None) -> str:
    """Assemble the system prompt for ``profile``.

    Raises ``KeyError`` for an unknown profile.
    """
    if profile not in PROFILES:
        raise KeyError(f"unknown profile {profile!r}; choose from {sorted(PROFILES)}")
    mods = modules if modules is not None else load_modules()
    selected = [m for m in mods if profile in m.profiles]
    if not selected:
        raise ValueError(f"no modules declare profile {profile!r}")
    body = "\n".join(m.render() for m in selected)
    return f"{HEADER}\n{body}"
