#!/usr/bin/env python3
"""The One-Line Laugh — u-ronigrv-the-one-line-laugh-7ccca46f.

Writes exactly one funny sentence (at most 200 characters) to
/output/entry.txt. Deterministic: no randomness, no network, no clock,
no environment input — every run produces the same bytes.

The joke: a familiar everyday truth (a fitness tracker praising you)
with the surprise saved for the end (the praise itself proves you
have been sitting still since Tuesday).
"""

import os

LINE = (
    "My smartwatch congratulated me for closing my exercise rings, "
    "then gently reminded me I have not stood up since Tuesday."
)

MAX_CHARS = 200


def main() -> None:
    assert len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, over 200"
    assert LINE.count(".") == 1, "entry must be a single sentence"
    assert "\n" not in LINE, "entry must be one line"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(LINE + "\n")
    except OSError:
        path = os.path.join("output", "entry.txt")
        os.makedirs("output", exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(LINE + "\n")
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
