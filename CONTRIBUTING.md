# Contributing to the Sandbox

This file is part of the training: we use the same habits we want in real repos.

---

## Branch naming

- `feature/<name>` — new exercise, new doc, new feature in examples
- `fix/<name>` — typo, broken instruction, bug in example code
- `chore/<name>` — layout, links, non-functional changes

Examples: `feature/phase2-exercise2`, `fix/typo-contributing`, `chore/add-cheatsheet`.

---

## Commit message format

```
type: short description
```

**Types:** `feat`, `fix`, `docs`, `chore`, `refactor`

**Examples:**

- `feat: add exercise 3 for conflict intro`
- `fix: correct null check in example app.py`
- `docs: add merge vs rebase to workflow-explained.md`
- `chore: align phase-2 folder with template`

Keep the first line under ~72 characters; add a body only if needed.

---

## PR checklist (use the template)

Before submitting a PR:

- [ ] Branch name follows `feature/`, `fix/`, or `chore/`
- [ ] Commits follow `type: short description`
- [ ] Instructions or code run (e.g. Python example runs)
- [ ] No changes to `main` history (no force push)

---

## Review expectations

- **Authors:** Expect feedback on instructions and example code; update from comments.
- **Reviewers:** Check the diff and description; leave clear, constructive comments. Use the PR checklist.
