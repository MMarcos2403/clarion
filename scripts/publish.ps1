# One-command publish for Clarion (PowerShell). Run from the repo root after
# authenticating GitHub (see PUBLISH.md).
$ErrorActionPreference = "Stop"

$Owner  = "MMarcos2403"
$Repo   = "clarion"
$Desc   = "A portable output-discipline layer for LLMs: one system prompt, any model, a rubric CI can enforce."
$Topics = "llm,prompt-engineering,ai,evals,developer-tools,claude,openai,gemini,python,system-prompt"

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { throw "gh CLI not installed. See PUBLISH.md." }
gh auth status *> $null; if ($LASTEXITCODE -ne 0) { throw "Not authenticated. Run 'gh auth login' first." }

# 1. Commit if needed.
git rev-parse --verify HEAD *> $null
if ($LASTEXITCODE -ne 0) {
  git add -A
  git commit -m "feat: Clarion 0.1.0 - portable output-discipline layer for LLMs"
}
git branch -M main

# 2. Create or reuse the repo, then push.
gh repo view "$Owner/$Repo" *> $null
if ($LASTEXITCODE -eq 0) {
  git remote get-url origin *> $null
  if ($LASTEXITCODE -ne 0) { git remote add origin "https://github.com/$Owner/$Repo.git" }
  git push -u origin main
} else {
  gh repo create "$Owner/$Repo" --public --source=. --remote=origin --push --description $Desc
}

# 3. Topics + release.
gh repo edit "$Owner/$Repo" --add-topic $Topics --description $Desc --homepage "https://github.com/$Owner/$Repo"
gh release view v0.1.0 --repo "$Owner/$Repo" *> $null
if ($LASTEXITCODE -ne 0) { gh release create v0.1.0 --repo "$Owner/$Repo" --title "Clarion 0.1.0" --generate-notes }

Write-Host "Done -> https://github.com/$Owner/$Repo"
