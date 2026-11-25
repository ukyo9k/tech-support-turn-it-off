#!/usr/bin/env python3
"""One-line tech-support joke for the make.fun bounty
"Have You Tried Turning It Off?".

Writes a single funny line -- a hopeless tech-support agent's reply
to a desperate customer -- to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).
"""

import os

LINE = "Good news \u2014 I turned it off and on again and it worked perfectly on my end, so I'm closing your ticket."

MAX_CHARS = 199


def main() -> None:
    line = LINE.strip()
    # UTF-8 round-trip: the gate reads the file back as UTF-8 text.
    line = line.encode("utf-8").decode("utf-8")
    if not line or len(line) > MAX_CHARS:
        raise SystemExit("entry line must be 1-199 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be a single line")
    if line != line.strip() or not line.strip():
        raise SystemExit("entry line must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
    # Read back and verify what the gate will see.
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    if written != line + "\n" or not 1 <= len(written.rstrip("\n")) <= MAX_CHARS:
        raise SystemExit("written entry failed the 1-199 character gate")


if __name__ == "__main__":
    main()
