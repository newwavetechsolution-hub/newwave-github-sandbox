# START HERE — Rebase practice

> **Note:** All Git commands work the same on Mac/Linux/Windows (Git Bash/PowerShell/CMD).

1. [ ] Create branch `feature/rebase-demo` from main; add `squared.py` with `def squared(x): return x**2`, commit

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git checkout -b feature/rebase-demo
   # create squared.py, then:
   git add squared.py
   git commit -m "feat: add squared function"
   ```

2. [ ] On main, add another commit (e.g. a new file or change). Switch back to `feature/rebase-demo`

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git checkout main
   # make changes, then:
   git add .
   git commit -m "chore: update main"
   git checkout feature/rebase-demo
   ```

3. [ ] Rebase onto main: `git rebase main`. Resolve any conflict if needed

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git rebase main
   ```

4. [ ] Run `git log --oneline` — your commit(s) should be on top of main. Do not force push to main; force push only to your branch if you had already pushed it

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git log --oneline
   # If you had pushed before:
   git push --force-with-lease origin feature/rebase-demo
   ```

Check [expected-result.md](expected-result.md) and [docs/workflow-explained.md](../../docs/workflow-explained.md).
