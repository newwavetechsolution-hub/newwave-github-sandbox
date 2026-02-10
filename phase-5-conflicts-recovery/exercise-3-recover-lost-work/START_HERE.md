# START HERE — Recover lost work

1. [ ] Create branch `feature/recover-demo`. Add `rescue.py` with `print("saved")`, commit. Note the commit hash or leave it as HEAD
2. [ ] "Lose" it: `git reset --hard HEAD~1` — the commit is gone from the branch
3. [ ] Find it: `git reflog` — find the hash of the "lost" commit
4. [ ] Recover: `git checkout <hash>` then `git switch -c recovered` (or `git cherry-pick <hash>` onto a new branch)
5. [ ] Confirm: `rescue.py` is back and the commit is in history

Check [expected-result.md](expected-result.md) and [docs/common-mistakes.md](../../docs/common-mistakes.md).
