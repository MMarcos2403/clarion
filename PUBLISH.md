# Publishing Clarion to GitHub

Everything is committed locally. Publishing needs **one thing only I can't do for
you: authenticate as you.** Pick either path, then run one script.

## Step 1 — authenticate (once)

**Option A — GitHub CLI (recommended).** Install `gh`, then:

```bash
winget install --id GitHub.cli      # or: choco install gh / scoop install gh
gh auth login                       # choose GitHub.com → HTTPS → browser
```

**Option B — Personal Access Token.** Create a fine-grained token with
`repo` scope at https://github.com/settings/tokens, then in your terminal:

```bash
export GH_TOKEN=your_token_here     # PowerShell: $env:GH_TOKEN="your_token_here"
```

Do **not** paste the token into a chat — keep it in your terminal only.

## Step 2 — run the publish script

From `C:\Users\mgmez\Desktop\fable`:

```bash
bash scripts/publish.sh             # macOS/Linux/Git-Bash
```
```powershell
./scripts/publish.ps1               # Windows PowerShell
```

The script commits (if needed), creates `MMarcos2403/clarion` as a public repo,
pushes `main`, sets topics and description, and cuts the `v0.1.0` release with
generated notes. Re-running it is safe.

## Step 3 — publish your profile README

```bash
cd ../github-profile
git init -b main && git add -A && git commit -m "docs: profile README"
gh repo create MMarcos2403 --public --source=. --remote=origin --push
```

## What you'll have

- `github.com/MMarcos2403/clarion` — the project, green CI, a tagged release.
- `github.com/MMarcos2403` — a profile page that leads with the work.

After it's live, come back and I'll do the itemized audit of your other repos
(what to pin, rewrite, archive) now that I can see them.
