#!/usr/bin/env python3
"""Autocheck: validator.py exists and is_positive(1) is True."""
import sys
from pathlib import Path

def main():
    exercise_dir = Path(sys.argv[2]).resolve()
    validator = exercise_dir / "validator.py"
    if not validator.is_file():
        print("validator.py not found.")
        return 1
    # Load and call is_positive(1)
    import importlib.util
    spec = importlib.util.spec_from_file_location("validator", validator)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not getattr(mod, "is_positive", lambda x: False)(1):
        print("is_positive(1) should be True.")
        return 1
    if getattr(mod, "is_positive", lambda x: False)(-1):
        print("is_positive(-1) should be False.")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
