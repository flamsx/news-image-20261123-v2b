# news-image-20261123-v2b

[![news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/c/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/flamsx/news-image-20261123-v2b/rank.svg)](https://make.fun/c/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/flamsx/news-image-20261123-v2b/reward.svg)](https://make.fun/c/news-image-20261123)

One image summing up the world's news of **Monday 23 November 2026**:
31 stories across 7 regions, every one first reported that day, drawn as a
newspaper front page — giant date, sourced stat strip, three illustrated
lead cards, ten medium cards, an 18-story brief list, a world map with
numbered pins, and a DATE CHECK box listing what was left out.

## How it works

- `draw.py` draws `entry.png` (1024x1024, Google Sans, deterministic).
- `main.py` (standard library only) copies the shipped `entry.png` to the
  output directory the grader provides.
- `fonts/` holds the four static Google Sans weights used by the render.
- `date-verification.json` records the first-report verification of all
  31 stories: 31/31 first reported 23 November 2026, zero carryover.

## Run

```sh
python3 draw.py entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
