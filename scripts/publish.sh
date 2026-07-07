#!/usr/bin/env bash
# One-command publish for Clarion. Run from the repo root after authenticating
# GitHub (see PUBLISH.md). Idempotent-ish: safe to re-run; it skips steps that
# are already done.
set -euo pipefail

OWNER="MMarcos2403"
REPO="clarion"
DESC="A portable output-discipline layer for LLMs: one system prompt, any model, a rubric CI can enforce."
TOPICS="llm,prompt-engineering,ai,evals,developer-tools,claude,openai,gemini,python,system-prompt"

command -v gh >/dev/null || { echo "ERROR: gh CLI not installed. See PUBLISH.md."; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "ERROR: not authenticated. Run 'gh auth login' first."; exit 1; }

# 1. Commit if there's anything uncommitted.
if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
  git add -A
  git commit -m "feat: Clarion 0.1.0 — portable output-discipline layer for LLMs"
fi
git branch -M main

# 2. Create the repo (or reuse it) and push.
if gh repo view "$OWNER/$REPO" >/dev/null 2>&1; then
  git remote get-url origin >/dev/null 2>&1 || git remote add origin "https://github.com/$OWNER/$REPO.git"
  git push -u origin main
else
  gh repo create "$OWNER/$REPO" --public --source=. --remote=origin --push --description "$DESC"
fi

# 3. Topics + release.
gh repo edit "$OWNER/$REPO" --add-topic "$TOPICS" --description "$DESC" --homepage "https://github.com/$OWNER/$REPO"
gh release view v0.1.0 --repo "$OWNER/$REPO" >/dev/null 2>&1 \
  || gh release create v0.1.0 --repo "$OWNER/$REPO" --title "Clarion 0.1.0" --generate-notes

echo "Done → https://github.com/$OWNER/$REPO"
