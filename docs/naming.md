# Naming study

The 30 candidates generated for this project, the criteria, and why **Clarion**
won. Kept in the repo because naming rationale is part of the design record.

## Criteria

A great OSS/dev-tool name is: **short** (1–3 syllables), **typeable** (no
ambiguous spelling), **evocative of the function**, **brandable** (works as a
logo and a CLI verb), and **not already a major package** in the space. The best
names in this ecosystem — `ripgrep`, `fzf`, `zod`, `vite`, `bun`, `ruff`,
`prisma`, `resend` — clear all five.

## The 30 candidates

| # | Name | Why it could work |
|---|------|-------------------|
| 1 | **Clarion** | A clear, ringing signal; "clarion call" = cuts through noise. Function-in-a-word. ✅ chosen |
| 2 | Lucent | Latin *lucere*, to shine; clarity. Slightly generic. |
| 3 | Candor | Honesty + clarity, the two core values. Strong but common as a brand. |
| 4 | Rubric | A rubric *is* a scoring standard — on the nose, memorable. Risk: literal. |
| 5 | Lodestar | A guiding star; "north". Evokes direction, less "output". |
| 6 | Plainly | Plain speech as a virtue. Adverb names read soft. |
| 7 | Diapason | The reference pitch a whole orchestra tunes to — perfect metaphor, hard to spell. |
| 8 | Clef | The mark that sets how everything after it is read. Elegant, tiny, maybe too musical. |
| 9 | Signal | Clarity vs. noise. Beautiful but heavily overused in tooling. |
| 10 | Terse | The behavior itself. Negative connotation (curt), risky. |
| 11 | Prose | It disciplines prose. Too generic to own. |
| 12 | Distil | Reduce to essence. Spelling variants (distill) hurt typeability. |
| 13 | Keel | What keeps a ship steady/true. Evocative, abstract. |
| 14 | Plumb | To true a line (plumb line). Nice metaphor, verb clash ("plumbing"). |
| 15 | Grain | "With the grain"; honest texture. Abstract for this domain. |
| 16 | Cadence | Rhythm of good writing. Taken by several products. |
| 17 | Verbatim | Faithful, exact. Long, means "word for word" (not quite it). |
| 18 | Sift | Separate signal from noise. Short, but crowded namespace. |
| 19 | Tenet | A held principle. Clean, but abstract and film-associated. |
| 20 | Marque | A mark of quality/brand. Obscure spelling. |
| 21 | Ledger | A record of standards. More finance-coded. |
| 22 | Clarity | The literal goal. Too plain to brand, hard to own. |
| 23 | Beacon | A clear signal in the dark. Common in tooling. |
| 24 | Concord | Agreement/harmony (concert pitch A). Diplomacy-coded. |
| 25 | Vellum | The clean surface you write on. Elegant, indirect. |
| 26 | Trueline | A true, straight line. Compound feels startup-y. |
| 27 | Plainspeak | Says exactly what it does. A little long. |
| 28 | Lucida | Brightest star in a constellation; also a typeface. Font clash. |
| 29 | Northword | North + word. Coined, brandable, slightly forced. |
| 30 | Clar/Klar | *klar* = clear (DE). Ultra-short, but too bare alone. |

## Why Clarion

It scores on every criterion: two syllables, unambiguous spelling, and its
meaning *is* the product — a clear signal that cuts through noise, which is
exactly what the layer does to LLM output. It works as a CLI verb (`clarion
build`, `clarion lint`), as a package name, and as a mark (a signal resolving
from noise to one clean line). Runners-up **Rubric** and **Candor** were strong
but each captures only half the idea (the scoring, or the honesty) where Clarion
captures the whole.

> Availability note: before publishing, check PyPI, npm, and the GitHub org for
> collisions and pick the namespace accordingly (e.g. `clarion-llm` if `clarion`
> is taken on a given registry).
