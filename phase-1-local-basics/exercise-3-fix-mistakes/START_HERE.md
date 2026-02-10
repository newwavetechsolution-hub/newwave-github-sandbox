# START HERE — Fix mistakes

1. [ ] Create `oops.py` with `print("draft")`. Run `git add oops.py`
2. [ ] Unstage: `git restore --staged oops.py`. Run `git status` — file should be untracked or modified, not staged
3. [ ] Stage again and commit: `git add oops.py` and `git commit -m "feat: add oops"`
4. [ ] Change `oops.py` to `print("fixed")`. Discard the change: `git restore oops.py` — file should be back to "draft"
5. [ ] (Optional) Undo last commit but keep file: `git reset --soft HEAD~1`. Then recommit with a better message

Check [expected-result.md](expected-result.md).
