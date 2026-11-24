#!/usr/bin/env python3
"""Entry for 'Seventeen Syllables of Debugging' (make.fun).

Writes one haiku about debugging (5-7-5 syllables) to /output/entry.txt.
"""
import os

HAIKU = (
    "Breakpoint holds its breath\n"
    "The log line lies to me again\n"
    "a missing comma"
)

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)

if __name__ == "__main__":
    main()
