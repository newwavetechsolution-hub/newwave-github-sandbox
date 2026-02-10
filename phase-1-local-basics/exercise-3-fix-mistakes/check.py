#!/usr/bin/env python3
"""Autocheck for exercise-3: oops.py exists and prints 'draft' (after restore)."""
import subprocess
import sys
from pathlib import Path

def main():
    exercise_dir = Path(sys.argv[2]).resolve()
    oops = exercise_dir / "oops.py"
    if not oops.is_file():
        print("oops.py not found.")
        return 1
    result = subprocess.run(
        [sys.executable, str(oops)],
        cwd=str(exercise_dir),
        capture_output=True,
        text=True,
        timeout=5,
    )
    out = (result.stdout or "").strip()
    if "draft" not in out:
        print(f"Expected 'draft' in output; got: {out!r}")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
