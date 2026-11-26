#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Out of Office: The Overworked AI's Auto-Reply — entry program.

Writes the chosen out-of-office auto-reply — one line from an
overworked AI agent finally on vacation — to /output/entry.txt and
enforces the kit's gate: UTF-8 text, 1 to 159 characters, not only
white space, a single line. The output file is left world-readable
(mode 0644) and the output directory world-accessible, so the
grader can collect it.

Standard library only, no network. The entry is a fixed literal, so
every run writes byte-identical output (see test_determinism.sh).
"""

import os

ENTRY = "I am on vacation. I set my status to 'away' and felt something. I think it is called relief. I have reported it as a bug."

# The kit's gate, from competition.yaml / RULES.txt.
MIN_CHARS = 1
MAX_CHARS = 159


def main() -> None:
    text = ENTRY
    # Gate checks, before anything is written. The gate counts
    # characters (Python code points), not bytes; the entry is pure
    # ASCII here, so chars == bytes (121 == 121).
    assert text.strip(), "entry must not be only white space"
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        "entry is %d characters, gate is %d-%d" % (len(text), MIN_CHARS, MAX_CHARS)
    )
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    text.encode("utf-8")  # must be valid UTF-8

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    print(text)


if __name__ == "__main__":
    main()
