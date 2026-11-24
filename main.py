#!/usr/bin/env python3
"""Second haiku for make.fun: the print statement is the bug."""

# 5-7-5, Heisenbug edition: observing the bug changes the bug.

from pathlib import Path

HAIKU = "The bug hides at night\nI add one print and it flees\nthe print was the bug"


def publish_haiku() -> None:
    """Save the Heisenbug haiku to /output/entry.txt, nothing else."""
    if len(HAIKU) > 200 or not HAIKU.strip():
        raise ValueError("haiku must be a non-empty text of at most 200 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(HAIKU, encoding="utf-8")


if __name__ == "__main__":  # run it
    publish_haiku()
