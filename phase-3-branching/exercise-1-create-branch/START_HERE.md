# START HERE — Create branch

> **Note:** All Git commands work the same on Mac/Linux/Windows (Git Bash/PowerShell/CMD).

1. [ ] From repo root: `git checkout main` and `git pull origin main`

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git checkout main
   git pull origin main
   ```

2. [ ] Create branch: `git checkout -b feature/your-name` (use your name)

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git checkout -b feature/your-name
   ```

3. [ ] In this folder create `utils.py`: `def double(x): return x * 2` and `if __name__ == "__main__": print(double(5))`
4. [ ] Commit: `git add .` and `git commit -m "feat: add double util"`

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git add .
   git commit -m "feat: add double util"
   ```

5. [ ] Run `git branch` — you should see `* feature/your-name` and `main`

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git branch
   ```

6. [ ] Switch to main: `git checkout main` — `utils.py` may disappear from working tree if it only exists on the branch (that's expected)

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git checkout main
   ```

Check [expected-result.md](expected-result.md).
