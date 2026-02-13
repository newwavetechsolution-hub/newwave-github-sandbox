# START HERE — Real conflict

> **Note:** All Git commands work the same on Mac/Linux/Windows (Git Bash/PowerShell/CMD).

1. [ ] On main, add a line to `shared_config.py` (e.g. `EXTRA["key"] = "value"`), commit and push

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git checkout main
   # edit shared_config.py, then:
   git add shared_config.py
   git commit -m "feat: add EXTRA config"
   git push origin main
   ```

2. [ ] Create branch `feature/my-config`, change a different part of `shared_config.py`, commit

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git checkout -b feature/my-config
   # edit shared_config.py, then:
   git add shared_config.py
   git commit -m "feat: add my config change"
   ```

3. [ ] Pull main, merge main into your branch — resolve conflict in `shared_config.py`

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git pull origin main
   git merge main
   # resolve conflict in shared_config.py, then:
   git add shared_config.py
   git commit
   ```

4. [ ] Keep both changes where sensible; remove conflict markers; commit and push

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git push origin feature/my-config
   ```

Check [expected-result.md](expected-result.md).
