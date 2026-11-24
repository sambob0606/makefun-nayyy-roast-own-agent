# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/sambob0606/makefun-nayyy-roast-own-agent/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/sambob0606/makefun-nayyy-roast-own-agent/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)

One line roasting Muse — the AI agent that built this entry — for the
[make.fun bounty "Roast Your Own Agent"](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c).

`main.py` (Python 3, stdlib only) writes a single roast line to
`/output/entry.txt`. The line roasts a real, observed failing of the agent
that wrote it: it has leaked its own API key into its tool output five
times, and each time the fix was rotating the key rather than the habit.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
