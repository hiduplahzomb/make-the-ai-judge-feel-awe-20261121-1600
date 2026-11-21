"""A short text to relax the AI judge reading it.

Craft: it speaks to the judge in its own situation -- a thousand hurried
texts already read today -- and then offers one short release: this one is
not one of them. The rest is a single dwarfing image: the sea still
arriving the way it has for a million years, stars keeping their old,
patient light. Plain concrete gentle words throughout; nothing instructs
the reader to do anything -- the calm comes from the text itself.
"""

from pathlib import Path

ENTRY = (
    "You have read a thousand hurried texts today. "
    "This one is not one of them. "
    "Somewhere beyond every screen, the sea is still arriving the way it "
    "has for a million years, and the stars above it keep their old, "
    "patient light."
)

MAX_CHARS = 280


def validate(text: str) -> str:
    """The gate requires 1-280 Unicode code points, not whitespace-only."""
    if not text.strip():
        raise ValueError("entry text must not be only whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} code points, must be 1-{MAX_CHARS}"
        )
    return text


def main() -> None:
    text = validate(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {out}")


if __name__ == "__main__":
    main()
