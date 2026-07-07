# FAQ

### Is this a jailbreak or a way to clone a specific model?
No. Clarion shapes *how* a model communicates (structure, calibration, voice),
not *what* it's allowed to say. It has no bypass of any model's safety behavior,
and it does not attempt to reproduce any proprietary system prompt. The
principles are distilled from public writing on clear communication and
prompting.

### Does it work with models other than Claude?
Yes — that's the point. The core is a plain system prompt with no
model-specific tokens. Adapters ship for Claude Code, OpenAI, Gemini, and
Cursor; any model with a system-instruction slot works.

### Why a system prompt *and* a linter? Isn't one enough?
They cover different risks. The prompt changes behavior; the linter *verifies*
it, so a model upgrade or prompt edit can't silently regress your output style.
Prompt without linter is untested; linter without prompt is a spell-checker with
no author.

### The linter is just regex. Isn't that crude?
Deliberately. The core needs to be deterministic, offline, and free so it can
run in CI on every commit. Regex catches the high-frequency mechanical tells,
which is most of the value. Subtle judgment is the job of a model-graded eval,
which is on the roadmap as a *complement*, not a replacement.

### Won't optimizing for the linter game the metric (Goodhart)?
It can, if you treat 100/100 as the goal. Don't. The score is a floor that says
"no obvious tells", not a ceiling that says "great answer". Keep a correctness
eval or human review in the loop. The docs say this everywhere on purpose.

### Can I customize the voice for my brand?
Add a module with your own `profiles` tag and compose it in. Don't fork the
prompt — you'll lose upstream improvements. See
[best-practices.md](best-practices.md).

### Does it add latency or cost?
The prompt adds tokens (a few hundred, fewer on `concise`). The linter is local
and adds microseconds. There are no runtime dependencies and no network calls.

### What Python versions are supported?
3.9 through 3.12, tested on Linux, macOS, and Windows in CI.

### Why is it called Clarion?
A clarion is a clear, ringing signal — and a clarion call is one that cuts
through noise. That's the whole product in one word.
