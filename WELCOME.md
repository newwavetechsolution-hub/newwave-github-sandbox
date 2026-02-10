## Welcome to the GitHub Sandbox

This repository is a **safe practice space** for learning Git and GitHub with a group, and is especially tuned for **teams of about 5 people** working together.

- **You can’t “ruin” the project.** If something breaks, you can always reclone or reset.
- **Multiple people can work at the same time.** It’s designed to be used by many learners in parallel.

---

## Quick Start (Learners)

1. **Clone or fork** this repo to your own GitHub account.
2. From your local clone, work through the phases in order:
   - Phase 1 → local basics (first commit, history, fixing mistakes)
   - Phase 2 → remotes (clone, push, pull, push rejection)
   - Phase 3 → branching (create branch, merge, intro to conflicts)
   - Phase 4 → pull requests (open/review PRs)
   - Phase 5 → conflicts & recovery (real conflicts, rebase, recover work)
   - Phase 6 → team simulation (shared codebase, fake issues, releases)
3. For exercises with an `expected-result.md`, use it as your **checklist**.
4. Where available, run the **autocheck** from repo root:

   ```bash
   python3 scripts/check_exercise.py phase-1-local-basics exercise-1-first-commit
   ```

---

## Suggested Setup for Groups (e.g., 12 People)

To avoid stepping on each other’s work and make collaboration smoother, use **teams of 5**:

- **Phases 1–2 (individual practice, per person):**
  - Each person uses **their own fork** of this repo (or their own clone if you’re all on the same machine lab).
  - They follow the instructions in each exercise folder on their own.

- **Phases 3–6 (team practice, teams of 5):**
  - Create **one fork per team of 5** (for example, `team-alpha-sandbox`).
  - Inside each team fork:
    - Create a **branch per exercise** (for example, `phase-3-ex1-team-alpha`).
    - Open **pull requests** from those branches into the team’s `main`.
    - Have teammates **review and merge** each PR.
  - Within each team of 5, you can rotate roles per exercise:
    - **Driver:** shares screen and types commands.
    - **Navigator:** reads `START_HERE.md` / `README.md` and keeps the team on track.
    - **Git Lead:** focuses on Git commands and explains what’s happening.
    - **Reviewer:** reviews PRs using the checklists.
    - **Recorder:** updates checklists in `progress/` and notes what the team learned.

This mirrors how real teams use Git and GitHub, but in a low‑stakes environment.

---

## Where to Look When You’re Stuck

- **Exercise instructions:** `START_HERE.md` and `README.md` inside each exercise folder.
- **What “done” looks like:** `expected-result.md` in each exercise.
- **Cheatsheets and fixes:** files in `docs/` (common mistakes, git cheatsheet, workflow).
- **Progress tracking:** the `progress/phase-*-checklist.md` files.

If you completely break your local repo, it’s okay—just delete your clone and **start again from a fresh clone**. That’s part of the learning.

