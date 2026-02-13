# START HERE — Commit history

> **Note:** All Git commands work the same on Mac/Linux/Windows (Git Bash/PowerShell/CMD).

1. [ ] In this folder, create `calc.py`: a function `add(a, b)` that returns `a + b`, and `if __name__ == "__main__": print(add(2, 3))`
2. [ ] Commit: `git add calc.py` and `git commit -m "feat: add calc module"`

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git add calc.py
   git commit -m "feat: add calc module"
   ```

3. [ ] Change line so it prints `add(10, 20)`. Commit: `git add calc.py` and `git commit -m "chore: change demo to 10+20"`

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git add calc.py
   git commit -m "chore: change demo to 10+20"
   ```

4. [ ] Run `git log --oneline` — you should see two commits

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git log --oneline
   ```

5. [ ] Run `git show HEAD` and `git show HEAD~1` — compare the diffs

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git show HEAD
   git show HEAD~1
   ```

Check [expected-result.md](expected-result.md).
