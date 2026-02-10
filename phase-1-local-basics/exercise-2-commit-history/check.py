#!/usr/bin/env python3
"""Autocheck for exercise-2: commit history — calc.py exists and add(2,3)==5."""
import subprocess
import sys
from pathlib import Path

def main():
    repo_root = Path(sys.argv[1]).resolve()
    exercise_dir = Path(sys.argv[2]).resolve()
    calc = exercise_dir / "calc.py"
    if not calc.is_file():
        print("calc.py not found.")
        return 1
    result = subprocess.run(
        [sys.executable, str(calc)],
        cwd=str(exercise_dir),
        capture_output=True,
        text=True,
        timeout=5,
    )
    out = (result.stdout or "").strip()
    if "5" not in out:
        print(f"Expected '5' in output (add(2,3)); got: {out!r}")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
