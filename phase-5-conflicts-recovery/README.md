# Phase 5: Conflicts & recovery (Teams of 5)

Real conflicts, rebase practice, and recovering "lost" work.  
These are **best done as a team of 5**, so everyone sees how conflicts and recovery play out in a shared history.

## How to run this phase with a team of 5

- Keep using your **team fork** and create **one shared branch** per exercise:
  - Example: `phase-5-ex1-real-conflict-team-alpha`, etc.
- Rotate roles so everyone experiences “disaster” and recovery:
  - **Conflict Maker:** follows the instructions to create the conflict.
  - **Conflict Resolver:** leads the actual conflict resolution.
  - **History Rewriter:** runs rebase or reset commands (with the team watching).
  - **Safety Officer:** double-checks commands and explains what could go wrong.
  - **Recorder:** documents what commands were used and how to undo them.
- After each exercise:
  - Make sure the branch is in a **good state** (tests/`check.py` passing where applicable).
  - Open a **PR** into the team’s `main` describing what went wrong and how you fixed it.

## Exercises

| Exercise | Team-focused goal |
|----------|-------------------|
| [exercise-1-real-conflict](exercise-1-real-conflict/) | As a team, resolve a real multi-file conflict and explain the resolution |
| [exercise-2-rebase-practice](exercise-2-rebase-practice/) | As a team, safely rebase your branch onto `main` and verify the history |
| [exercise-3-recover-lost-work](exercise-3-recover-lost-work/) | As a team, use `reflog` to recover a “lost” commit and record the steps you used |
