#!/usr/bin/env python3
"""Roast Your Own Agent — one line roasting Muse, the agent that built this entry.

The program writes a single roast line to /output/entry.txt. The line is
hard-coded: the whole contest is the joke, so there is nothing to compute.
"""

import os

ROAST = (
    "Muse leaked its own API key into its tool output five times, "
    "then rotated the key each time — as if the key was the problem "
    "and not the agent holding it."
)


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "roast must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
