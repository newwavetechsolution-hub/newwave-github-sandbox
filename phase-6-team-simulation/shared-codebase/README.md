# Shared codebase — mini app

Fake mini app to simulate real repo collaboration. Everyone edits the same tree.

- **backend/** — Python "API" helpers
- **frontend/** — Python CLI or stubs (simulated frontend)
- **config/** — shared config; editing here causes conflicts on purpose

Try: two people edit different files, then merge; or both edit `config/settings.py` and resolve the conflict.
