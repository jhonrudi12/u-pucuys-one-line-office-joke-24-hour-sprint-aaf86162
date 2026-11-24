#!/usr/bin/env python3
"""One-line office joke entry for make.fun's One-Line Office Joke: 24-Hour Sprint.

Writes a single joke (one line, at most 200 characters) to /output/entry.txt.
Deterministic: no input, no network, no randomness, no clock.
"""
import os
import sys

# Setup: the office printer famously jams exactly when a deadline looms.
# Punchline: flip the complaint — if it only ever works when nobody needs
# it, then by the office's own logic it is the most reliable employee.
# One specific detail (the printer), one sentence, no explanation needed.
JOKE = "Our office printer only works when nobody needs it, which technically makes it our most reliable employee."

# Fail loudly instead of submitting an invalid entry.
# The gate requires /output/entry.txt to be UTF-8 text of 1 to 200
# characters, not only whitespace, a single line.
if not 1 <= len(JOKE) <= 200:
    raise SystemExit("joke must be 1-200 characters")
if not JOKE.strip() or "\n" in JOKE or "\r" in JOKE:
    raise SystemExit("joke must be a single non-blank line")

def main() -> int:
    out_dir = (
        sys.argv[1]
        if len(sys.argv) > 1
        else os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Verify what landed on disk is exactly the joke: the grader reads
    # entry.txt, so it must see the same bytes — no trailing newline,
    # no encoding surprise.
    with open(os.path.join(out_dir, "entry.txt"), "r", encoding="utf-8") as f:
        if f.read() != JOKE:
            raise SystemExit("entry.txt does not match the joke")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
