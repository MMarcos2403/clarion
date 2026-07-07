# Security Policy

## Supported versions

Clarion is pre-1.0. Security fixes land on the latest `0.x` release only.

| Version | Supported |
|---------|-----------|
| 0.1.x   | ✅        |
| < 0.1   | ❌        |

## Reporting a vulnerability

Please **do not** open a public issue for security problems.

Use GitHub's private [security advisory](https://github.com/OWNER/clarion/security/advisories/new)
flow, or email the maintainers. Include:

- a description of the issue and its impact,
- steps to reproduce,
- affected version(s).

You can expect an acknowledgement within 72 hours and a triage decision within
seven days.

## Scope notes

Clarion runs offline and has no runtime dependencies, which keeps its attack
surface small. The most relevant class of issue is **prompt content that could
be weaponized downstream** — e.g. a module change that would degrade a model's
safety behavior. Report those here too; we treat output-safety regressions as
security issues, not just quality ones.
