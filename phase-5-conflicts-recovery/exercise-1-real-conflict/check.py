#!/usr/bin/env python3
"""Autocheck: shared_config.py exists and has no conflict markers."""
from pathlib import Path
import sys

def main():
    exercise_dir = Path(sys.argv[2]).resolve()
    f = exercise_dir / "shared_config.py"
    if not f.is_file():
        print("shared_config.py not found.")
        return 1
    text = f.read_text()
    for marker in ("<<<<<<<", "=======", ">>>>>>>"):
        if marker in text:
            print(f"Conflict marker still present: {marker!r}")
            return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
