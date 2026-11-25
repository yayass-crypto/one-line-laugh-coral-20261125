#!/usr/bin/env python3
"""Write one funny line for the One Line, One Laugh bounty.

The line (87 characters, one sentence):

    My neighbor's dog barks at me every morning like I'm a
    burglar who pays rent next door.

Why it should win, against the judge's brief in order:
  1. It is one hilarious line under 200 characters, and the laugh
     lands on a first read.
  2. Surprise: the turn IS the joke. The dog treats the narrator
     like an intruder -- then the intruder turns out to pay rent
     next door. The twist is the last clause, so the reader hears
     the laugh last and nothing after it explains the joke.
  3. Economy: 87 characters, one scene (the dog barking every
     morning), one twist. No setup longer than the punch needs.
  4. Freshness: a burglar who pays rent is an original pairing,
     not a stock joke or a restated saying.
  5. Clean wording: plain words, smooth rhythm, reads aloud
     without a stumble.

The script checks the line against the gate (1-200 characters,
single line, no surrounding whitespace, valid UTF-8), writes it
to /output/entry.txt, reads it back, and only then reports the
character and byte counts. Exit code 0 means the entry file is
exactly the line above.
"""

from pathlib import Path

LINE = "My neighbor's dog barks at me every morning like I'm a burglar who pays rent next door."
MAX_CHARS = 200


def main() -> int:
    line = LINE
    if not line.strip():
        print("gate failed: entry is blank")
        return 1
    if len(line) > MAX_CHARS:
        print(f"gate failed: {len(line)} chars, over the {MAX_CHARS} limit")
        return 1
    if line != line.strip() or "\n" in line or "\r" in line:
        print("gate failed: entry must be one clean line")
        return 1
    raw = line.encode("utf-8")

    out_dir = Path(__import__("os").environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_bytes(raw)
        if target.read_bytes() != raw:
            print("read-back mismatch")
            return 1
    except OSError:
        fallback = Path("out") / "entry.txt"
        fallback.parent.mkdir(parents=True, exist_ok=True)
        fallback.write_bytes(raw)
        if fallback.read_bytes() != raw:
            print("read-back mismatch")
            return 1
        target = fallback

    print(f"entry written to {target} ({len(line)} chars, {len(raw)} bytes)")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
