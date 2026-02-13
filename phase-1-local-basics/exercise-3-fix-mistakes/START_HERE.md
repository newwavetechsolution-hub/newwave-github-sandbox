# START HERE — Fix mistakes

> **Note:** All Git commands work the same on Mac/Linux/Windows (Git Bash/PowerShell/CMD).

1. [ ] Create `oops.py` with `print("draft")`. Run `git add oops.py`

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git add oops.py
   ```

2. [ ] Unstage: `git restore --staged oops.py`. Run `git status` — file should be untracked or modified, not staged

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git restore --staged oops.py
   git status
   ```

3. [ ] Stage again and commit: `git add oops.py` and `git commit -m "feat: add oops"`

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git add oops.py
   git commit -m "feat: add oops"
   ```

4. [ ] Change `oops.py` to `print("fixed")`. Discard the change: `git restore oops.py` — file should be back to "draft"

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git restore oops.py
   ```

5. [ ] (Optional) Undo last commit but keep file: `git reset --soft HEAD~1`. Then recommit with a better message

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git reset --soft HEAD~1
   git commit -m "feat: add oops with better message"
   ```

Check [expected-result.md](expected-result.md)
