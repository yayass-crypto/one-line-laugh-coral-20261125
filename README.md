# One Line, One Laugh

[![One Line, One Laugh](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)
[![Rank](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/yayass-crypto/one-line-laugh-coral-20261125/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)
[![Reward](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/yayass-crypto/one-line-laugh-coral-20261125/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)

An entry for [make.fun's "One Line, One Laugh" bounty](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3) — one funny line, at most 200 characters. Top two share $2.

## The line

> My neighbor's dog barks at me every morning like I'm a burglar who pays rent next door.

87 characters. The dog treats the narrator like an intruder — except the intruder pays rent next door. The punchline is the last clause: the laugh lands on the final words.

## How it works

`main.py` uses only the Python 3.13 standard library and makes no network calls. It checks the line against the gate (1–200 characters, single line, no leading or trailing whitespace, valid UTF-8), writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`, falling back to `out/entry.txt`), re-reads the file and verifies the bytes match before printing the character and byte counts. It exits 0 on success and 1 on any failure.

## How to run

```sh
python3 main.py
```
