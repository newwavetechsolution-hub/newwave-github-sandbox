# START HERE — Clone and push

> **Note:** All Git commands work the same on Mac/Linux/Windows (Git Bash/PowerShell/CMD).

1. [ ] If you haven't: `git clone <repo-url>` and `cd` into it

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git clone <repo-url>
   cd <repo-name>
   ```

2. [ ] Create branch: `git checkout -b feature/my-first-push` (use your name)

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git checkout -b feature/my-first-push
   ```

3. [ ] In this folder create `greet.py`: `def greet(name): return f"Hi, {name}"` and a `__main__` that prints `greet("Git")`
4. [ ] Commit: `git add .` and `git commit -m "feat: add greet module"`

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git add .
   git commit -m "feat: add greet module"
   ```

5. [ ] Push: `git push -u origin feature/my-first-push`

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git push -u origin feature/my-first-push
   ```

6. [ ] On GitHub, confirm the branch and file appear

Check [expected-result.md](expected-result.md).
