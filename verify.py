"""Local verifier for the Seventeen Syllables of Debugging entry.

Checks the haiku the entry writes: exactly 3 lines, 5-7-5 syllables,
at most 200 characters, plain UTF-8 text. Syllable counts use an
explicit per-word map for the words in this haiku (hand-counted),
so the check is deterministic and does not depend on a heuristic.
"""

import os
import subprocess
import sys
import tempfile

HAIKU = """Cursor blinks at three
log lines scroll past, still no sign
it was a comma"""

# Hand-counted syllables for every word in the haiku.
SYLLABLES = {
    "cursor": 2, "blinks": 1, "at": 1, "three": 1,
    "log": 1, "lines": 1, "scroll": 1, "past": 1,
    "still": 1, "no": 1, "sign": 1,
    "it": 1, "was": 1, "a": 1, "comma": 2,
}

EXPECTED = [5, 7, 5]


def count_line(line):
    words = line.replace(",", "").split()
    total = 0
    for word in words:
        key = word.lower()
        assert key in SYLLABLES, f"unmapped word: {word!r}"
        total += SYLLABLES[key]
    return total


def main():
    lines = HAIKU.split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    for i, (line, want) in enumerate(zip(lines, EXPECTED)):
        got = count_line(line)
        print(f"line {i + 1}: {got} syllables (want {want}): {line!r}")
        assert got == want, f"line {i + 1}: {got} != {want}"
    assert HAIKU.strip(), "haiku must not be only whitespace"
    assert len(HAIKU) <= 200, f"{len(HAIKU)} chars > 200"
    print(f"total chars: {len(HAIKU)} (limit 200)")

    # Run main.py exactly as the harness would and check its output.
    here = os.path.dirname(os.path.abspath(__file__))
    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
        subprocess.run(
            [sys.executable, os.path.join(here, "main.py")],
            env=env, check=True,
        )
        with open(os.path.join(tmp, "entry.txt"), encoding="utf-8") as f:
            written = f.read()
    assert written == HAIKU, f"entry.txt differs: {written!r}"
    print("main.py output matches the haiku byte for byte")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
