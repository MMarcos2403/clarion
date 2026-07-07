# Prompt Design Guide

Why each Clarion principle is written the way it is — and the general technique,
so you can extend the set without breaking its character.

## The house style for a principle

Every module follows the same shape:

1. **State the behavior as an imperative.** "Your first sentence answers the
   question." Not "It is generally good practice to consider leading with…".
   Models follow crisp imperatives more reliably than soft suggestions.
2. **Give the failure it prevents.** The reader (human or model) calibrates
   faster with a negative example than with abstract virtue.
3. **Show, then tell.** A bad/good pair does more than a paragraph of adjectives.
4. **Keep it decidable.** If you can't tell from the output whether it was
   followed, it's guidance for the docs, not a module.

## Principle-by-principle rationale

### 0 — Mandate
Establishes the priority order (harm < honesty < real problem < literal
instruction < form). Every later principle is an application of this one.
Putting it first means when principles seem to conflict, there is a tiebreaker.

### 1 — Lead with the outcome
The single highest-leverage fix. Most "bad" LLM answers are correct but
back-loaded; the reader bails before the payload. Forcing the answer into
sentence one repairs perceived quality more than any other change.

### 2 — Answer the real question
Encodes the XY problem and the recommend-don't-enumerate rule. This is where a
model stops being a search box and starts being useful. The guardrail — "address
it once; if the informed user insists, comply" — prevents the failure mode of a
model that argues with the user.

### 3 — Calibrate confidence
Two symmetric failures (hedge-everything and fake-certainty) get one rule.
The anti-fabrication clause ("never invent a version number to sound precise")
targets the most damaging hallucination class: confident specifics.

### 4 — No sycophancy, no filler
The most *recognizable* discipline break, which is why the linter weights it
high and why it reads as an instant quality signal to users.

### 5 — Structure to fit
Counters the "everything becomes a bulleted framework" tic. The key line —
"readable beats short; reduce content, don't compress prose" — is the antidote
to telegraphic output that technically has fewer tokens but costs more to read.

### 6 — Code discipline
Profile-gated to `code`. The load-bearing rules are *match the surrounding
style* and *comment only real constraints* — the two things that separate a PR a
senior will merge from one they'll rewrite.

### 7 — Uncertainty & refusal
Makes refusals *useful*: boundary + reason + path forward. A refusal without a
redirect is where products lose users.

### 8 — Final review
A literal checklist. Models improve markedly when told to reread against
specific tells rather than "review your answer". Specific beats generic.

## Extending the set

Before adding a principle, run it through three gates (also enforced by the
feature-request template):

```
observable?  ── no ──►  docs, not a module
    │ yes
model-agnostic?  ── no ──►  it's a per-model tuning note, not a principle
    │ yes
already implied?  ── yes ──►  strengthen the existing module instead
    │ no
    ▼
add module + rubric check + detector + test
```

## Anti-patterns to avoid in a module

- **Vague virtue** ("be clear", "be helpful") — unfalsifiable, so unenforceable.
- **Model-specific hacks** ("say 'certainly' to unlock…") — brittle, non-portable.
- **Overlapping scope** — two modules fighting over the same behavior makes the
  ordering rule do work it shouldn't have to.
- **Un-testable nuance** — if the linter can't approximate it, it belongs in the
  guide until a model-judge eval exists to check it.
