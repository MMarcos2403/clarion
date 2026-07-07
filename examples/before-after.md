# Before / after

Real transformations the Clarion principles produce, with the linter score for
each. Reproduce any of these with `echo "..." | clarion lint -`.

---

## 1. The back-loaded answer

**Before** — score 45/100 (fails `leads-with-outcome`, `no-sycophancy`)
> Great question! There are a lot of things to think about when choosing between
> SQL and NoSQL, and it really depends on your specific use case and
> requirements. Let's explore some of the considerations... [answer arrives in
> paragraph four]

**After** — score 100/100
> Use Postgres. Your data is relational and your scale fits one node, so the
> reasons teams reach for NoSQL don't apply to you yet. Revisit only when you
> need multi-region writes or a genuinely schemaless document store — here's how
> to tell when that day comes.

*What changed:* the recommendation moved to sentence one; the flattery opener is
gone; a neutral "it depends" became a reasoned pick with a trip-wire for when to
reconsider.

---

## 2. The hedge wall

**Before** — flagged by `calibrated-language`
> It might possibly be the case that the bug could perhaps be related to the
> cache, though it's hard to say and it may be something else entirely.

**After**
> The bug is almost certainly the cache: the stale read only appears after a
> write within the TTL window. I haven't reproduced it with the cache disabled —
> do that to confirm before you commit the fix.

*What changed:* real confidence stated plainly, the one genuine uncertainty
isolated and paired with the exact check that would resolve it.

---

## 3. The filler close

**Before** — flagged by `no-filler-close`
> ...and that completes the migration. Hope this helps! Let me know if you need
> anything else!

**After**
> ...and that completes the migration. One caveat: the `orders` backfill runs
> for ~20 minutes on production-sized data — schedule it off-peak.

*What changed:* the empty sign-off became a genuinely useful last sentence.

---

## 4. The bulleted-everything reflex

**Before** — flagged by `structure-fits`
> ## Overview
> ## Answer
> - Yes
> ## Explanation
> - Because the flag defaults to true

**After**
> Yes — the flag defaults to `true`, so you don't need to set it explicitly
> unless you want the opposite.

*What changed:* three headers wrapping one fact collapsed into the one sentence
that fact deserved.
