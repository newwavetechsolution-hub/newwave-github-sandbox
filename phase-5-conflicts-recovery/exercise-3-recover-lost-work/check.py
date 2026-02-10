#!/usr/bin/env python3
"""Autocheck: rescue.py exists and prints 'saved'."""
import subprocess
import sys
from pathlib import Path

def main():
    exercise_dir = Path(sys.argv[2]).resolve()
    rescue = exercise_dir / "rescue.py"
    if not rescue.is_file():
        print("rescue.py not found (recover it with reflog).")
        return 1
    result = subprocess.run(
        [sys.executable, str(rescue)],
        cwd=str(exercise_dir),
        capture_output=True,
        text=True,
        timeout=5,
    )
    if "saved" not in (result.stdout or "").strip():
        print("Expected 'saved' in rescue.py output.")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
