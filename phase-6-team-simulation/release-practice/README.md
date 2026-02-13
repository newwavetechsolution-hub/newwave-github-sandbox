# Release practice

Simulate a release: tag a version and update release notes as a team.

> **Note:** All Git commands work the same on Mac/Linux/Windows (Git Bash/PowerShell/CMD).

1. Agree on version (e.g. `v0.1.0`).
2. Update `release-notes.txt` with bullet points (everyone can add a line → conflicts).
3. Commit, merge to main, then tag:

   **Mac/Linux/Windows (Git Bash/PowerShell/CMD):**
   ```bash
   git add release-notes.txt
   git commit -m "docs: update release notes"
   git checkout main
   git merge <your-branch>
   git tag v0.1.0
   git push origin v0.1.0
   ```

4. On GitHub, create a Release from the tag and paste notes.
