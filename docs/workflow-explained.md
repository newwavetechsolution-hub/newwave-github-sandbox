# Workflow explained

Mental model and when to use what.

---

## Local → Remote flow

1. Work on a **branch** (never commit directly to `main` for features).
2. **Commit** often with clear messages (`type: description`).
3. **Push** your branch: `git push -u origin your-branch`.
4. Open a **Pull Request** (PR) against `main`.
5. After review and approval, **merge** (usually via GitHub).
6. **Pull** latest `main` before starting the next task: `git pull origin main`.

---

## When to use merge vs rebase

- **Merge:** Preserves history, adds a merge commit. Use when bringing a branch into `main` or when combining work from others. Safe default.
- **Rebase:** Replays your commits on top of another branch; history is linear but rewritten. Use only on **your own** branches (e.g. “update my branch with latest main”). Never rebase commits that are already pushed and shared.

In this sandbox we practice both in Phase 5; in real repos, follow your team’s rule (often “merge to main, optional rebase for your branch”).

---

## Conflict resolution (high level)

1. You run `git merge other-branch` or `git pull` and Git says “Conflict”.
2. Open the conflicted files; look for `<<<<<<<`, `=======`, `>>>>>>>`.
3. Edit to keep the right code and remove the markers.
4. `git add` the fixed files.
5. `git commit` (merge) or `git rebase --continue` (rebase).

See [common-mistakes.md](common-mistakes.md) for “if you see this error → do this”.
