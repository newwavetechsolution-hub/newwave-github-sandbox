# START HERE — Open PR

> **Note:** All Git commands work the same on Mac/Linux/Windows (Git Bash/PowerShell/CMD).

1. [ ] Create branch: `feature/add-validator` (or similar)

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git checkout -b feature/add-validator
   ```

2. [ ] Add a small Python module in this folder, e.g. `validator.py`: `def is_positive(n): return n > 0`
3. [ ] Commit: `git add .` and `git commit -m "feat: add is_positive validator"`

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git add .
   git commit -m "feat: add is_positive validator"
   ```

4. [ ] Push: `git push -u origin feature/add-validator`

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git push -u origin feature/add-validator
   ```

5. [ ] On GitHub, open a Pull Request into `main`. Use the PR template if the repo has one; fill description and checklist
6. [ ] Request a review (or self-merge if sandbox allows)

Check [expected-result.md](expected-result.md).
