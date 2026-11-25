#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut.

Writes the GPS's own one-line excuse for sending the driver down the
wrong road to /output/entry.txt. Deterministic, standard library only:
the line is fixed, so every run produces the same entry.
"""

import os

# The GPS's excuse, in its own voice: smug, defensive, blaming the map.
# One line of plain text, no setup, no dialogue tags.
EXCUSE = (
    "In my defense, the map showed a perfectly good road \u2014 "
    "the fact that the road is now a lake is between you and the map. "
    "I just read what it says."
)


def main() -> None:
    line = EXCUSE.strip()
    assert 1 <= len(line) <= 200, f"entry is {len(line)} characters"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
