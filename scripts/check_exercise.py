#!/usr/bin/env python3
"""
Autocheck runner for sandbox exercises.
Usage:
  python scripts/check_exercise.py phase-1-local-basics exercise-1-first-commit
  python scripts/check_exercise.py phase-1-local-basics   # check all in phase
  python scripts/check_exercise.py                        # check all exercises
"""
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def find_exercise_dirs(phase_arg=None, exercise_arg=None):
    """Yield (phase_dir, exercise_dir) paths under REPO_ROOT."""
    phases = [REPO_ROOT / "phase-1-local-basics", REPO_ROOT / "phase-2-remotes",
              REPO_ROOT / "phase-3-branching", REPO_ROOT / "phase-4-pull-requests",
              REPO_ROOT / "phase-5-conflicts-recovery"]
    for phase_dir in phases:
        if not phase_dir.is_dir():
            continue
        if phase_arg and phase_dir.name != phase_arg:
            continue
        for path in sorted(phase_dir.iterdir()):
            if path.is_dir() and path.name.startswith("exercise-"):
                if exercise_arg and path.name != exercise_arg:
                    continue
                yield phase_dir, path


def run_check(phase_name: str, exercise_path: Path) -> bool:
    """Run check.py in exercise dir if present. Returns True if pass or no check."""
    check_script = exercise_path / "check.py"
    if not check_script.is_file():
        print(f"  [--] No autocheck for {phase_name}/{exercise_path.name}")
        return True
    try:
        result = subprocess.run(
            [sys.executable, str(check_script), str(REPO_ROOT), str(exercise_path)],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=10,
        )
        out = (result.stdout or "").strip()
        err = (result.stderr or "").strip()
        if result.returncode == 0:
            print(f"  [OK] {phase_name}/{exercise_path.name}" + (f" — {out}" if out else ""))
            return True
        print(f"  [FAIL] {phase_name}/{exercise_path.name}")
        if out:
            print(f"        {out}")
        if err:
            print(f"        {err}")
        return False
    except subprocess.TimeoutExpired:
        print(f"  [FAIL] {phase_name}/{exercise_path.name} — timeout")
        return False
    except Exception as e:
        print(f"  [FAIL] {phase_name}/{exercise_path.name} — {e}")
        return False


def main():
    phase_arg = (sys.argv[1] if len(sys.argv) > 1 else None)
    exercise_arg = (sys.argv[2] if len(sys.argv) > 2 else None)
    if phase_arg and "/" in phase_arg:
        phase_arg, exercise_arg = phase_arg.split("/", 1)
    pairs = list(find_exercise_dirs(phase_arg, exercise_arg))
    if not pairs:
        print("No matching exercises found.")
        sys.exit(2)
    failed = 0
    for phase_dir, exercise_path in pairs:
        if not run_check(phase_dir.name, exercise_path):
            failed += 1
    if failed:
        sys.exit(1)
    print("All checks passed.")


if __name__ == "__main__":
    main()
