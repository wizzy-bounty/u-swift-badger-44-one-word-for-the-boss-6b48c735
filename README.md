# One Word for the Boss

[![One Word for the Boss](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![Rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/wizzy-bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735/rank.svg)](https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![Reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/wizzy-bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735/reward.svg)](https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735)

An entry for the [One Word for the Boss](https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735) competition on make.fun: exactly one word describing a boss, with no phrase, caption, or explanation.

## The idea

The word is **backseatdriver** — the boss who stands behind you and steers work you already know how to do, turn by turn, as if you were the one who needed directions. Every workplace has one: in the kitchen they hover over the pass telling you how to plate, in the warehouse they shadow the forklift route, in the office they lean over your monitor mid-sentence. They never do the driving themselves; they just narrate it, loudly, from the back seat. It is funny because it is instantly recognizable, and it is true because the habit is universal — a boss in any industry, no explanation required.

## How it works

`main.py` (Python 3, standard library only, deterministic, no network) writes exactly that one word to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). The word is validated in code: a single token, 1–30 characters, not only whitespace.

## Run it

```bash
python3 main.py
cat /output/entry.txt
```

Or with a custom output directory:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
