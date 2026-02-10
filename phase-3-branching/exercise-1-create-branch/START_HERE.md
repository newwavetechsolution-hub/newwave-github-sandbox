# START HERE — Create branch

1. [ ] From repo root: `git checkout main` and `git pull origin main`
2. [ ] Create branch: `git checkout -b feature/your-name` (use your name)
3. [ ] In this folder create `utils.py`: `def double(x): return x * 2` and `if __name__ == "__main__": print(double(5))`
4. [ ] Commit: `git add .` and `git commit -m "feat: add double util"`
5. [ ] Run `git branch` — you should see `* feature/your-name` and `main`
6. [ ] Switch to main: `git checkout main` — `utils.py` may disappear from working tree if it only exists on the branch (that's expected)

Check [expected-result.md](expected-result.md).
