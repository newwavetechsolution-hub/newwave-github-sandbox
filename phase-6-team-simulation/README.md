# Phase 6: Team simulation (Teams of 5)

Fake issues, shared codebase, release practice — simulate real collaboration.  
This phase is explicitly designed for **teams of 5** working in a shared codebase.

## How to run this phase with a team of 5

- Use your **team fork** and treat `shared-codebase/` as your mini app.
- As a team:
  - **Triage fake issues:** decide which ones to tackle and who leads each.
  - Create **one branch per issue** (e.g., `issue-3-fix-greeting-team-alpha`).
  - Use **PRs** to propose changes and link them back to the fake issue.
- Suggested rotating roles:
  - **Issue Lead:** owns a fake issue from branch creation to merge.
  - **Implementer:** does most of the coding for that issue.
  - **Reviewer(s):** review the PR and request changes if needed.
  - **Release Captain:** coordinates `release-practice/` and updates `release-notes.txt`.
  - **Recorder:** notes which issues were closed and what changed in each release.

## Areas

| Area | Team-focused goal |
|------|-------------------|
| [fake-issues](fake-issues/) | As a team of 5, pick an issue, branch from `main`, fix it, open a PR, and close the issue via that PR |
| [shared-codebase](shared-codebase/) | As a team of 5, work in a mini app (backend/frontend/config) while coordinating branches and reviews |
| [release-practice](release-practice/) | As a team of 5, tag a release, update `release-notes.txt`, and agree on what “shipped” |
