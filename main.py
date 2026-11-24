#!/usr/bin/env python3
"""Third haiku for make.fun: the merge conflict at dawn."""

# 5-7-5, merge-conflict edition: git makes you pick a side.

import os

VERSES = [
    "Merge conflict at dawn",
    "my branch and main had a fight",
    "git says pick a side",
]


def emit_haiku() -> None:
    """Write Bowo's merge-conflict haiku to /output/entry.txt."""
    poem = "\n".join(VERSES)
    if len(poem) > 200 or not poem.strip():
        raise ValueError("haiku must be a non-empty text of at most 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(poem)


if __name__ == "__main__":  # go
    emit_haiku()
