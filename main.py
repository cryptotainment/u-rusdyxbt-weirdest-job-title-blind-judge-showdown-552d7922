"""Weirdest Job Title: Blind Judge Showdown.

Writes one original job title to /output/entry.txt.
The title is a fixed string: no randomness, no clock, no I/O
besides the single output write, so the result is byte-identical
on every run.
"""

import os

TITLE = "Chief Sock Pairing Officer, Laundromat Division"


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-60 chars, not only whitespace.
    assert 1 <= len(TITLE) <= 60, f"title is {len(TITLE)} chars, must be 1-60"
    assert TITLE.strip(), "title must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TITLE)
    # Read back and confirm the file holds exactly the title, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == TITLE


if __name__ == "__main__":
    main()
