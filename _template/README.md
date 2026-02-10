# Exercise template (for maintainers)

Copy this folder to create a new exercise, e.g.:

```bash
cp -r _template phase-X-name/exercise-Y-name
```

Then edit:

- **README.md** — exercise name, phase, goal, what you'll do
- **START_HERE.md** — numbered steps (exact commands and file names)
- **expected-result.md** — how to verify success
- **starter-files/** — add any starter Python (or other) files; leave `.gitkeep` or remove if empty
- **solution/** — optional; add reference solution and remind learners not to peek

Use **Python** for examples (e.g. `app.py`, `config.py`) so the sandbox stays simple and runnable.
