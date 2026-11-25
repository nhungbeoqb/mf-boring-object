#!/usr/bin/env python3
"""One-line review of the most boring everyday object: the coat hanger.

The program writes a single review line to /output/entry.txt.
Python 3.13 standard library only; fully deterministic.
"""

import os
from pathlib import Path

LINE = (
    "The coat hanger held my best shirt for a year, tangled with eleven "
    "brothers every morning, and snapped the day I finally had an interview."
)


def main() -> None:
    text = LINE.strip()
    assert "\n" not in text, "review must be a single line"
    assert 1 <= len(text) <= 200, f"review is {len(text)} chars, must be 1-200"
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
