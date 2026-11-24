#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry (program/v1).

Writes exactly one word describing a boss to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python 3 standard library only, deterministic, no network.
"""

import os

WORD = "backseatdriver"

MIN_LEN = 1
MAX_LEN = 30


def main() -> None:
    word = WORD.strip()
    if not (MIN_LEN <= len(word) <= MAX_LEN):
        raise SystemExit(
            f"word must be {MIN_LEN}-{MAX_LEN} characters, got {len(word)}"
        )
    if not word or word.isspace():
        raise SystemExit("word must not be only whitespace")
    if any(ch.isspace() for ch in word):
        raise SystemExit("entry must be exactly one word, no spaces")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    # verify the file holds exactly the single word, nothing else
    with open(out_path, "r", encoding="utf-8") as f:
        assert f.read() == word, "entry.txt must contain exactly the one word"


if __name__ == "__main__":
    main()
