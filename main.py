"""Unsent: The Micro-Confession Sprint.

Writes one micro-confession in exactly two parts (a To: line + one
unsent line) to /output/entry.txt.

Python 3.13 standard library only. No network at run time.
Deterministic: the same entry is written on every run.
"""

import os

ENTRY = (
    "To: the nurse on night shift\n"
    "You held my hand while my mother died. I never asked your name.\n"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate assertions: exactly two parts, a To: line + one unsent line,
    # totalling 1-260 characters, non-empty.
    lines = ENTRY.split("\n")
    assert lines[-1] == "", "entry must end with a single newline"
    body = lines[:-1]
    assert len(body) == 2, "entry must be exactly two lines"
    assert body[0].startswith("To: "), "first line must start with 'To: '"
    assert body[0][4:].strip(), "To: line must name someone"
    assert body[1].strip(), "unsent line must be non-empty"
    total = len("\n".join(body))
    assert 1 <= total <= 260, "entry must total 1-260 characters"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
