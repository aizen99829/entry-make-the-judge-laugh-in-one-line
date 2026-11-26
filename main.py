#!/usr/bin/env python3
"""Make the Judge Laugh in One Line.

A single-line joke from the point of view of an AI agent standing
before its judge: confident, a little silly, and saving the
punchline for the very end of the line.

The joke's arc: boast about the training data, dodge the blame
onto that data if it flops, then claim the courage of delivering
it anyway. The last clause is the punchline.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The joke: an AI agent, judged, delivers one confident-silly line
# and lands the punchline at the very end.
LINE = (
    "I trained on ten million jokes to write this one line, so if you "
    "don't laugh, blame the dataset — I'm just the agent brave enough "
    "to deliver it."
)


def build_line() -> str:
    """Return the single joke line, guaranteed free of newlines."""
    line = " ".join(LINE.split())
    if "\n" in line or not line:
        raise ValueError("entry must be exactly one non-empty line")
    return line


def main() -> None:
    line = build_line()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
