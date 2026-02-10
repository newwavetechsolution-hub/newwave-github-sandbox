# START HERE — Conflict intro

1. [ ] Create branch `feature/your-name`: `git checkout -b feature/your-name`
2. [ ] Edit line 3 in `app.py` (e.g. set `MOTTO = "Your motto here"`)
3. [ ] Commit: `git add app.py` and `git commit -m "feat: set my motto"`
4. [ ] Pull latest main: `git checkout main`, `git pull origin main`, then `git checkout feature/your-name`
5. [ ] Merge main into your branch: `git merge main` — you should get a conflict in `app.py` (if someone else changed the same line on main)
6. [ ] Resolve conflict: open `app.py`, remove `<<<<<<<`, `=======`, `>>>>>>>`, keep or combine the right content
7. [ ] Finish: `git add app.py`, `git commit`, then `git push origin feature/your-name`

To force a conflict if working alone: on main, change `MOTTO` and commit, then do steps 4–7 on your branch.

Check [expected-result.md](expected-result.md).
