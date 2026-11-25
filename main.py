#!/usr/bin/env python3
"""Write one sentence about the best meal I ever had to entry.txt.

Stdlib only, deterministic: the same sentence every run.
"""

import os

SENTENCE = (
    "At my grandmother's kitchen table in Lahore, I ate saag and makki di roti "
    "still steaming from the tawa, butter pooling in the corners, while winter "
    "fog pressed against the window."
)


def main() -> None:
    # The gate allows 1 to 200 characters; keep the sentence inside it.
    assert 1 <= len(SENTENCE) <= 200
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
