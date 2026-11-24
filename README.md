# Seventeen Syllables of Debugging

[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![make.fun · rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Rizal556z/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![make.fun · reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Rizal556z/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

Entry for the [make.fun bounty "Seventeen Syllables of Debugging"](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605).

## What the program does

`main.py` (pure Python standard library, no network, no model calls)
writes exactly one haiku to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`).

## The haiku

> Cursor blinks at three
> log lines scroll past, still no sign
> it was a comma

Three lines, 5-7-5 syllables, 74 characters. The picture at the
centre is concrete — a cursor blinking at three in the morning while
log lines scroll past with no sign of the bug — and the last line
turns the poem: after all that staring, the bug was a single comma.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/haiku-test python3 main.py
cat /tmp/haiku-test/entry.txt
```

## Verify it

```sh
python3 verify.py
```

Checks the haiku: exactly 3 lines, 5-7-5 syllables (explicit
hand-counted per-word map), at most 200 characters, and that
`main.py` writes it byte for byte.
