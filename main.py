"""Seventeen Syllables of Debugging — make.fun entry.

One haiku about debugging, 5-7-5 syllables, three lines:

    Cursor blinks at three
    log lines scroll past, still no sign
    it was a comma

The picture at the centre is concrete: a cursor blinking at three in
the morning while log lines scroll past with no sign of the bug. The
last line turns the poem — after all that staring, the bug was a
single comma. Syllables per line: 5-7-5 (Cursor(2) blinks at three;
log lines scroll past, still no sign; it was a com-ma(2)). Pure
standard library, no network access, no model
calls — the haiku is chosen by the author and written to the
competition output file.
"""

import os

HAIKU = """Cursor blinks at three
log lines scroll past, still no sign
it was a comma"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
