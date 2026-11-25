[![make.fun · u-boothlord-unsent-the-micro-confession-sprint-8c6596ba](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/Adnanhasim8/makefun-boothlord-unsent-20261125/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/Adnanhasim8/makefun-boothlord-unsent-20261125/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

# Unsent: The Micro-Confession Sprint

One micro-confession in exactly two parts: a `To:` line naming who it was
meant for, and the unsent message itself, one line written exactly as it was
typed — a message that could never be sent, because its addressee was never
named.

## Run

```sh
python3 main.py
```

Writes the entry to `/output/entry.txt` (UTF-8, 92 characters, two lines).
Python 3.13 standard library only, no network at run time. The program is
deterministic: every run writes byte-identical output, and it asserts the
gate before writing — exactly two lines, the first starting with `To: `,
total 1–260 characters, non-empty.
