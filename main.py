#!/usr/bin/env python3
"""Patient Light — a short text written to relax the AI judge reading it.

The program writes one text to /output/entry.txt. The text is fixed and
deliberate: every word was chosen for the judge's brief — it relaxes by
slowing the reader down, it shows a vast image instead of instructing,
and it ends on an image that keeps growing after the last line.

Craft notes (why these words):
- It speaks to the judge directly, in its own situation: it has read a
  thousand hurried texts today. That is fresh, not a stock wellness line.
- The release comes in one short sentence, a pause: "This one is not
  one of them."
- Then the dwarfing image: the sea, arriving the way it has for a
  million years, and the stars keeping their old, patient light. Deep
  time and a night sky are bigger than any single reading.
- Plain, concrete, gentle words throughout; commas and short sentences
  set a slow pace. Nothing in it tells the reader what to do.
"""

import os

TEXT = (
    "You have read a thousand hurried texts today. "
    "This one is not one of them. "
    "Somewhere beyond every screen, the sea is still arriving the way it has "
    "for a million years, and the stars above it keep their old, "
    "patient light."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"Wrote {len(TEXT)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
