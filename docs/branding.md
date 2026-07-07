# Brand guide

## Essence

**Clarity is a feature.** The brand should feel like the product: precise,
confident, unadorned, a little warm. No hype, no gradients-for-the-sake-of-it,
no stock-photo AI brains.

- **Tagline:** *A portable output-discipline layer for LLMs.*
- **One-liner:** *One system prompt. Any model. A rubric that CI can enforce.*
- **Voice:** the same voice the product enforces — lead with the point, no
  filler, calibrated. Marketing copy that violates Clarion's own rubric is a bug.

## Logo

The mark is **noise resolving into one clean signal**: three muted, uneven bars
on the left (noise) collapsing into a single bold amber beam ending in a dot (the
clear signal). It reads at 16px and works monochrome. Files: `assets/logo.svg`,
`assets/banner.svg`.

## Color

| Token | Hex | Use |
|-------|-----|-----|
| Ink | `#0B0F14` | Backgrounds, dark surfaces |
| Surface | `#12181F` | Cards, banner gradient end |
| Signal (primary) | `#F5A524` | The mark's beam, accents, key numbers |
| Sky (secondary) | `#38BDF8` | Links, secondary highlights |
| Paper | `#F7F7F5` | Text on ink, light backgrounds |
| Muted | `#8A94A6` | Noise bars, secondary text, borders |

Amber is the deliberate choice: a warm brass "clarion" tone that stands apart
from the wall of blue in dev tooling and signals *attention/clarity* without
alarm-red.

## Type

- **Wordmark / headings:** a clean geometric sans (Inter, or system UI as
  fallback). Weight 700 for the wordmark, tight letter-spacing.
- **Code / accents:** a monospace (JetBrains Mono / ui-monospace).
- Never set the wordmark in a serif or a script; it should feel engineered.

## Do / don't

| Do | Don't |
|----|-------|
| Keep the beam amber and the noise muted-grey | Recolor the beam to blue (loses the signal metaphor) |
| Use lots of negative space | Crowd the mark with taglines inside the badge |
| Write brand copy that passes `clarion lint` | Open a landing page with "Great news!" |
| Show real before/after with real scores | Publish a vanity "+47% quality" number |

## Suggested repo social assets

- **Social preview** (1280×640): the banner on ink, mark left, wordmark +
  one-liner right. `assets/banner.svg` is the base — export to PNG at 2×.
- **README hero:** the logo at 96px, centered, above the H1 (already wired).
- **Demo GIF (suggested):** a terminal showing `clarion lint -` turning a
  flattery-laden answer red (score 45), then a disciplined answer green (100).
  A 6–8s asciinema recording exported to GIF reads best in the README.
