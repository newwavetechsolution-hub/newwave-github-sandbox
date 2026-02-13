# START HERE — Push rejection

> **Note:** All Git commands work the same on Mac/Linux/Windows (Git Bash/PowerShell/CMD).

Simulate remote changes (e.g. from another clone or a partner):

1. [ ] In another clone (or on GitHub) add a commit to `main` — e.g. add a file to `phase-2-remotes/exercise-3-push-rejection/version.txt` with content `1.0`
2. [ ] In your main clone, on `main`, run `git pull origin main` to get that commit

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git checkout main
   git pull origin main
   ```

3. [ ] On your feature branch, make a new commit (e.g. add a line to a file). Then run `git push origin <branch>` — if you had pushed before and main moved, you might see rejection

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git checkout feature/your-branch
   # make changes, then:
   git add .
   git commit -m "feat: update something"
   git push origin feature/your-branch
   ```

4. [ ] Fix: merge or rebase main into your branch, then push again

   **Option A: Merge**
   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git merge main
   git push origin feature/your-branch
   ```

   **Option B: Rebase**
   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git rebase main
   git push origin feature/your-branch
   ```

Check [expected-result.md](expected-result.md) and [docs/common-mistakes.md](../../docs/common-mistakes.md).
