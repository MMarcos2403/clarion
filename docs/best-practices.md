# Best Practices

Getting real value out of Clarion in production.

## Choose the right profile

| Profile | Use for | Roughly |
|---------|---------|---------|
| `full` | General assistants, agents that also write prose | all 9 modules |
| `concise` | Pure chat, tight token budgets | 7 modules, no code/refusal |
| `code` | Coding agents, PR bots, review tools | full + code discipline |

Start with `full`; drop to `concise` only when you measure context pressure.

## Order matters: Clarion first, task second

Put the Clarion block at the **top** of your system message and your
task-specific instructions after it. Clarion governs *how* to answer; your task
governs *what* to answer. Keeping that order avoids a task instruction
accidentally overriding a discipline rule.

```
[ Clarion system prompt ]
---
You are a support agent for ACME. Only discuss ACME products. ...
```

## Lint in three places

1. **Eval harness** — assert `lint(output).passed` on your golden set so a
   prompt or model change can't silently regress style.
2. **CI** — pipe representative sample outputs through `clarion lint`; fail the
   build under threshold.
3. **Pre-commit** — for teams that keep canned/system responses in the repo.

Tune the threshold with `--threshold`; 70 is a sane default, 85 is strict.

## Don't over-lint

The linter is a *floor*, not a *ceiling*. A 100/100 score means "no mechanical
tells", not "excellent answer". Pair it with a model-graded rubric or human
review for correctness and depth. Never optimize purely for the linter — that's
Goodhart's law waiting to happen.

## Combine, don't fork

If you need a house variation (say, a brand voice), add a **module** with your
own `profiles` tag rather than forking the prompt. You keep upstream updates and
your customization in one composable system.

## Measure before and after

The honest way to justify Clarion to a team: run your eval set with and without
it, compare on your own metrics. See [benchmarks.md](benchmarks.md) for a
harness you can point at your data — and for why we don't publish vanity numbers.
