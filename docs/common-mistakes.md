# Common mistakes and fixes

“If you see this → do this.”

---

## “Push rejected” / “Updates were rejected”

**Cause:** Remote has commits you don’t have (someone else pushed, or you pushed from another machine).

**Fix:**

1. `git pull origin main` (or your branch name).
2. Resolve any conflicts, then commit.
3. `git push origin <branch>` again.

Never force push to `main`.

---

## “You have divergent branches”

**Cause:** Your branch and the remote branch have different commits.

**Fix:** Pull (merge) or rebase, then push.

- Merge: `git pull origin <branch>` then `git push origin <branch>`.
- Rebase (only if no one else uses this branch): `git pull --rebase origin <branch>` then push.

---

## “Merge conflict” / “CONFLICT in …”

**Cause:** You and someone else (or another branch) changed the same lines.

**Fix:**

1. Open the listed files.
2. Find `<<<<<<<`, `=======`, `>>>>>>>` and choose what to keep (or combine).
3. Remove the conflict markers.
4. `git add <file>` for each fixed file.
5. `git commit` (merge) or `git rebase --continue` (rebase).

---

## “Detached HEAD”

**Cause:** You checked out a commit (or tag) instead of a branch.

**Fix:** Create a branch if you want to keep work: `git switch -c my-branch`. Then you can commit and push. To just go back: `git switch main` (or your branch).

---

## “Force push” temptation

**Rule:** Do not force push to `main` or to shared branches.

**Safe use:** Force push only to **your own** feature branch, and only if you’re sure no one else is using it (e.g. after a rebase). Example: `git push --force-with-lease origin feature/my-branch`.

---

## “I lost my commit”

**Fix:** Use reflog to find the commit hash: `git reflog`. Then `git checkout <hash>` and create a branch: `git switch -c recovery`. Now you can merge this branch or cherry-pick the commit.
