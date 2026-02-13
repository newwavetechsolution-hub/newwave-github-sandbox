# START HERE — Recover lost work

> **Note:** All Git commands work the same on Mac/Linux/Windows (Git Bash/PowerShell/CMD).

1. [ ] Create branch `feature/recover-demo`. Add `rescue.py` with `print("saved")`, commit. Note the commit hash or leave it as HEAD

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git checkout -b feature/recover-demo
   # create rescue.py, then:
   git add rescue.py
   git commit -m "feat: add rescue script"
   ```

2. [ ] "Lose" it: `git reset --hard HEAD~1` — the commit is gone from the branch

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git reset --hard HEAD~1
   ```

3. [ ] Find it: `git reflog` — find the hash of the "lost" commit

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git reflog
   ```

4. [ ] Recover: `git checkout <hash>` then `git switch -c recovered` (or `git cherry-pick <hash>` onto a new branch)

   **Option A: Checkout and create branch**
   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git checkout <hash>
   git switch -c recovered
   ```

   **Option B: Cherry-pick**
   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git checkout main
   git checkout -b recovered
   git cherry-pick <hash>
   ```

5. [ ] Confirm: `rescue.py` is back and the commit is in history

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git log --oneline
   ```

Check [expected-result.md](expected-result.md) and [docs/common-mistakes.md](../../docs/common-mistakes.md).
