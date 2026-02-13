# 🧪 GitHub Sandbox — Learn Git by Doing

A safe repo to **explore → try → break → fix → repeat**. No production code. Breaking things (outside `main`) is encouraged.

---

## What This Repo Is

- **Training ground** for Git and GitHub workflow
- **Phased exercises** from local basics → remotes → branching → PRs → conflicts → team simulation
- **Python-based examples** in exercises and shared codebase
- **Playground** to experiment (rebase, reset, cherry-pick) without risk

---

## How to Start

1. **Clone this repo** (or fork first if you prefer).
2. **Read** [SANDBOX_RULES.md](SANDBOX_RULES.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
3. **Follow phases in order:**
   - [Phase 1: Local basics](phase-1-local-basics/) → first commit, history, fixing mistakes
   - [Phase 2: Remotes](phase-2-remotes/) → clone, push, pull, push rejection
   - [Phase 3: Branching](phase-3-branching/) → create branch, merge, conflict intro
   - [Phase 4: Pull requests](phase-4-pull-requests/) → open PR, review, feedback cycle
   - [Phase 5: Conflicts & recovery](phase-5-conflicts-recovery/) → real conflict, rebase, recover work
   - [Phase 6: Team simulation](phase-6-team-simulation/) → issues, shared codebase, release practice
4. **Use** [docs/](docs/) for cheatsheets and “if you see this error → do this”.
5. **Mess around** in [playground/](playground/) when you want to try something risky.

---

## Goals per Person

Use these to focus your learning and track progress. Tick in [progress/](progress/) or in your own notes.  
For **phases 3–6**, these goals are best practiced **inside a team of 4**, where you can rotate roles (Driver, Navigator, Git Lead, Reviewer/Recorder) so everyone touches branching, PRs, conflicts, and recovery.

### 🟢 Learner (new to Git / GitHub)

| Goal | Done |
|------|------|
| Complete Phase 1 (first commit, view history, fix a mistake) | ☐ |
| Complete Phase 2 (push to remote, pull, handle push rejected) | ☐ |
| In a team of 4, create a branch, make commits, and merge into main together (Phase 3) | ☐ |
| In a team of 4, open at least one PR using the repo template (Phase 4) | ☐ |
| In a team of 4, help resolve at least one merge conflict (Phase 4 or 5) | ☐ |
| In a team of 4, complete one “disaster” exercise (e.g. recover lost work — Phase 5) | ☐ |
| In a team of 4, close one fake issue via PR in the team simulation (Phase 6) | ☐ |

### 🟡 Reviewer (giving feedback on PRs)

| Goal | Done |
|------|------|
| In your team of 4, review at least 2 PRs using the PR checklist | ☐ |
| Leave at least one “request changes” with clear, kind feedback for a teammate | ☐ |
| Approve a PR only after checking diff and description | ☐ |
| Use agreed branch naming and commit message rules when commenting | ☐ |

### 🔴 Maintainer (protecting main, running drills)

| Goal | Done |
|------|------|
| For your team of 4, ensure main is protected (PR + 1 review required) | ☐ |
| Run or design one “disaster drill” for your team (e.g. recover from bad reset) | ☐ |
| Add or improve one exercise or doc in the sandbox (for all teams) | ☐ |
| Use SANDBOX_RULES when someone asks about force push / history rewrite | ☐ |

---

## Rules (summary)

- ❌ No force push to `main`
- ❌ No deleting repo branches without agreement
- ✅ Breaking things is encouraged outside `main`
- ✅ Ask before rewriting shared history

Full rules: [SANDBOX_RULES.md](SANDBOX_RULES.md).

---

## Autocheck (optional)

Some exercises have a `check.py` that verifies the result (e.g. file exists, script runs). From repo root:

**Mac/Linux:**
```bash
python3 scripts/check_exercise.py                              # all exercises
python3 scripts/check_exercise.py phase-1-local-basics         # one phase
python3 scripts/check_exercise.py phase-1-local-basics exercise-1-first-commit  # one exercise
```

**Windows (Git Bash/PowerShell):**
```bash
python scripts/check_exercise.py                              # all exercises
python scripts/check_exercise.py phase-1-local-basics         # one phase
python scripts/check_exercise.py phase-1-local-basics exercise-1-first-commit  # one exercise
```

**Windows (CMD):**
```cmd
python scripts\check_exercise.py                              # all exercises
python scripts\check_exercise.py phase-1-local-basics         # one phase
python scripts\check_exercise.py phase-1-local-basics exercise-1-first-commit  # one exercise
```

Exercises without `check.py` are not auto-validated (e.g. “open a PR” or “review a PR”).

---

## Getting Help

- **Stuck on an exercise?** Check [docs/common-mistakes.md](docs/common-mistakes.md) and [docs/git-cheatsheet.md](docs/git-cheatsheet.md).
- **Error message?** Search in `docs/` for the message or command.
- **Safe to break something?** Use [playground/break-anything/](playground/break-anything/).

---

## Optional: Progress Checklists

- [progress/phase-1-checklist.md](progress/phase-1-checklist.md)
- [progress/phase-2-checklist.md](progress/phase-2-checklist.md)
- (Further phase checklists in `progress/`)

---

## Repo Layout (quick reference)

```
git-sandbox/
├── README.md              ← you are here
├── CONTRIBUTING.md
├── SANDBOX_RULES.md
├── docs/                  ← cheatsheet, workflow, common mistakes
├── phase-1-local-basics/  → phase-6-team-simulation/
├── progress/              ← per-phase checklists
├── playground/            ← break anything safely
└── _template/             ← exercise template (for maintainers)
```
# newwave-github-sandbox
