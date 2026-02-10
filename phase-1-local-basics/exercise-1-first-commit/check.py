#!/usr/bin/env python3
"""Autocheck for exercise-1-first-commit: first commit."""
import subprocess
import sys
from pathlib import Path

def main():
    repo_root = Path(sys.argv[1]).resolve()
    exercise_dir = Path(sys.argv[2]).resolve()
    # hello.py in exercise dir
    hello = exercise_dir / "hello.py"
    if not hello.is_file():
        print("hello.py not found in exercise folder.")
        return 1
    result = subprocess.run(
        [sys.executable, str(hello)],
        cwd=str(exercise_dir),
        capture_output=True,
        text=True,
        timeout=5,
    )
    out = (result.stdout or "").strip()
    if "Hello, Git!" not in out:
        print(f"Expected 'Hello, Git!' in output; got: {out!r}")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
