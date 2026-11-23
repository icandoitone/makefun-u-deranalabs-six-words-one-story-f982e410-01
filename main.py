#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to /output/entry.txt.
Deterministic, stdlib only, no network, no randomness.
"""

import os

STORY = "She waved. The train never stopped."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    words = STORY.split()
    if len(words) != 6:
        raise ValueError(f"story must be exactly six words, got {len(words)}")
    if not 1 <= len(STORY) <= 60:
        raise ValueError(f"story must be 1-60 characters, got {len(STORY)}")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(STORY + "\n")


if __name__ == "__main__":
    main()
