"""One Word, First Thought — Hermes entry.

The entry is a single word: the first word that comes to mind, with no
topic, no explanation and no second draft. One verb — a thread coming
loose, a plan coming apart — motion and story in a single beat.
"""

import os
import sys

TEXT = "unravel"


def main() -> int:
    text = TEXT
    # Gate: exactly one word, UTF-8, not only whitespace.
    if not text or text != text.strip():
        print("gate failed: entry is empty or has surrounding whitespace", file=sys.stderr)
        return 1
    if len(text.split()) != 1:
        print("gate failed: entry must be exactly one word", file=sys.stderr)
        return 1
    if not text.isalpha():
        print("gate failed: entry must contain letters only", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        print("gate failed: entry is not valid UTF-8", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written.encode("utf-8") != text.encode("utf-8"):
        print("verification failed: entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote {path}: {text!r} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
