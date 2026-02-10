# Git cheatsheet

Quick reference for commands used in the sandbox.

---

## Basics

| Action | Command |
|--------|---------|
| Status | `git status` |
| Add all | `git add .` |
| Add file | `git add <file>` |
| Commit | `git commit -m "message"` |
| Log (short) | `git log --oneline` |
| Log (graph) | `git log --oneline --graph` |

---

## Remotes

| Action | Command |
|--------|---------|
| List remotes | `git remote -v` |
| Fetch | `git fetch origin` |
| Pull | `git pull origin main` |
| Push | `git push origin <branch>` |
| Push (set upstream) | `git push -u origin <branch>` |

---

## Branches

| Action | Command |
|--------|---------|
| List branches | `git branch -a` |
| Create branch | `git branch <name>` |
| Switch branch | `git checkout <name>` or `git switch <name>` |
| Create and switch | `git checkout -b <name>` or `git switch -c <name>` |
| Delete branch | `git branch -d <name>` |

---

## Merge & rebase

| Action | Command |
|--------|---------|
| Merge branch into current | `git merge <branch>` |
| Rebase current onto branch | `git rebase <branch>` |
| Abort merge | `git merge --abort` |
| Abort rebase | `git rebase --abort` |

---

## Undo / recover

| Action | Command |
|--------|---------|
| Unstage file | `git restore --staged <file>` |
| Discard changes in file | `git restore <file>` |
| Undo last commit (keep changes) | `git reset --soft HEAD~1` |
| View reflog | `git reflog` |
| Recover commit by hash | `git checkout <hash>` then `git switch -c recovery` |
