# Portfolio strategy (generic until your GitHub is reviewed)

You asked for a brutally honest GitHub audit and a roadmap of projects that make
a recruiter think "I want to interview this person." I can't audit a profile I
can't see — inventing findings about your repos would be exactly the failure
this project exists to prevent. **Give me your GitHub URL/handle and I'll do the
real audit** (profile, READMEs, repo structure, topics, commit hygiene,
pinned-repo strategy, consistency) against reference AI/OSS profiles.

Until then, here's the *generic* strategy, which is genuinely useful on its own.

## What strong AI-engineering profiles have in common

1. **2–4 deep projects, not 30 shallow ones.** Pinned repos do the talking.
   Delete or archive abandoned experiments; they dilute the signal.
2. **Every pinned repo has a real README** — problem, demo, install, how it
   works, why the design is the way it is. The README is the interview.
3. **Evidence of judgment, not just output.** ADRs, tests, CI, a roadmap, an
   honest "non-goals" section. This is what separates "can code" from "can own".
4. **A coherent theme.** Three projects pointing at one area (say, LLM tooling)
   beat nine unrelated ones. It reads as a specialist, not a dabbler.
5. **Maintenance signals.** Green CI badge, recent commits, answered issues,
   semantic-versioned releases, a CHANGELOG.

Clarion itself is built to be exhibit A on all five.

## A portfolio arc for an AI engineer (each project should demonstrate *judgment*)

| Project | Demonstrates | Stack | Difficulty | Positioning |
|---------|--------------|-------|------------|-------------|
| **Clarion** (this) | Prompt engineering as *engineering*; testing the untestable | Python, CLI, CI | Medium | "I bring rigor to LLM work" |
| **LLM eval harness** | Measurement discipline; you don't ship on vibes | Python, async, a judge model, datasets | Medium-High | "I can prove a model change is better" |
| **A small RAG service done right** | Retrieval quality, chunking, eval, latency budget, observability | Python/TS, a vector store, FastAPI, tracing | High | "I can ship production LLM infra" |
| **An agent with real tool use + guardrails** | Orchestration, failure handling, cost/latency control | Python, function-calling, a tracer | High | "I understand agents past the demo" |
| **One systems/non-AI project** | You're an engineer, not just a prompt writer (data structures, a parser, a CLI, perf work) | Rust/Go/Python | Medium | "Fundamentals are solid" |

Rationale for the mix: the two hardest hiring doubts about "AI engineers" are
(a) *can they measure?* and (b) *are they real engineers or just prompt
tinkerers?* The eval harness answers (a); the systems project answers (b). The
RAG service and agent show you can go from notebook to production.

## For each project, write the README to answer five questions

1. What problem does this solve, in one sentence at the top?
2. Can I see it work in 10 seconds? (GIF or a copy-paste command)
3. How do I run it?
4. How does it work, and *why is it built this way*? (this is the judgment part)
5. What are the trade-offs and non-goals? (senior signal)

## Anti-patterns to purge

- Tutorial clones and course projects pinned as if they were original work.
- Repos with a default README or none at all.
- `final_v2_REAL_final` commit histories; force-pushed messes.
- A profile README full of skill-badge walls and zero substance.
- Ten 3-star repos where two 40-star repos would serve you better.

## Next step

Send your GitHub handle. I'll produce a specific, itemized audit: what to pin,
what to rewrite, what to archive, what to build next, and how to phrase each
repo's description and topics for search and for humans.
