#!/usr/bin/env python3
"""Autocheck for conflict-intro: app.py exists and has no conflict markers."""
from pathlib import Path
import sys

def main():
    exercise_dir = Path(sys.argv[2]).resolve()
    app = exercise_dir / "app.py"
    if not app.is_file():
        print("app.py not found.")
        return 1
    text = app.read_text()
    for marker in ("<<<<<<<", "=======", ">>>>>>>"):
        if marker in text:
            print(f"Conflict marker still present: {marker!r}")
            return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
