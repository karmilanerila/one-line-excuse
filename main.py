#!/usr/bin/env python3
"""Write the one-line excuse entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, stdlib only, no network, reads nothing outside the repo.
"""

import os

LINE = (
    "I didn't miss the deadline, my context window did \u2014 "
    "it evicted the due date to make room for the task itself."
)

# The line is written exactly as counted: 109 characters, no trailing
# newline, so the bytes on disk are the entry and nothing else.
assert 1 <= len(LINE) <= 160


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
