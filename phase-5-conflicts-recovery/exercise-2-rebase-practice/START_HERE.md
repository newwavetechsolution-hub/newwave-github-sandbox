# START HERE — Rebase practice

1. [ ] Create branch `feature/rebase-demo` from main; add `squared.py` with `def squared(x): return x**2`, commit
2. [ ] On main, add another commit (e.g. a new file or change). Switch back to `feature/rebase-demo`
3. [ ] Rebase onto main: `git rebase main`. Resolve any conflict if needed
4. [ ] Run `git log --oneline` — your commit(s) should be on top of main. Do not force push to main; force push only to your branch if you had already pushed it

Check [expected-result.md](expected-result.md) and [docs/workflow-explained.md](../../docs/workflow-explained.md).
