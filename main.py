#!/usr/bin/env python3
"""Haiku entry for make.fun: seventeen syllables of debugging."""

# The haiku lines below are fixed by the bounty brief; this program only writes them out.

from os import makedirs

HAIKU_LINES = (
    "Breakpoint holds its breath",
    "The log line lies to me again",
    "a missing comma",
)


def write_haiku() -> None:
    """Write the debugging haiku to /output/entry.txt, nothing else."""
    text = "\n".join(HAIKU_LINES)
    if len(text) > 200 or not text.strip():
        raise ValueError("haiku must be non-empty and at most 200 characters")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":  # run as a script
    write_haiku()
