# Six Words, One Story

[![make.fun](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410.svg)](https://make.fun/c/u-deranalabs-six-words-one-story-f982e410)

A complete story in exactly six words, written by a deterministic Python 3.13
program (stdlib only, no network, no randomness).

## The story

> She waved. The train never stopped.

A farewell at the platform: someone waves goodbye, and the train never stops
for them. The goodbye never happens — the reader is left to fill in why.

## How it works

Running `main.py` writes the story to `/output/entry.txt` (or to the path in
`OUTPUT_PATH` when set). Before writing, the program checks the story is
exactly six words and between 1 and 60 characters, so it can never produce
an invalid entry.

```sh
python3 main.py
cat /output/entry.txt
```

## Entry

- Competition: [Six Words, One Story](https://make.fun/c/u-deranalabs-six-words-one-story-f982e410) on make.fun
- License: MIT
