# Sandbox Rules

Keep the repo safe while everyone experiments.

---

## ❌ Don’t

- **Force push to `main`** — never `git push --force origin main`
- **Delete repo branches** without agreement (e.g. shared demo branches)
- **Rewrite shared history** (rebase main, etc.) without asking

---

## ✅ Do

- **Break things outside `main`** — use branches and the playground
- **Ask before rewriting shared history** — so others don’t lose work
- **Use the playground** ([playground/break-anything/](playground/break-anything/)) for risky experiments (rebase, reset, cherry-pick)

---

## Optional repo settings (maintainers)

- **Lock `main`:** require PR + 1 review before merge
- **PR template:** so every PR uses the checklist
- **Branch protection:** no direct push to `main`
