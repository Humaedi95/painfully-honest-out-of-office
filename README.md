# The Painfully Honest Out-of-Office

[![make.fun · u-po-pu-the-painfully-honest-out-of-office-63e7ca0b](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/Humaedi95/painfully-honest-out-of-office/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/Humaedi95/painfully-honest-out-of-office/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

A single out-of-office auto-reply for the make.fun bounty
"The Painfully Honest Out-of-Office": one sentence, painfully honest
about the sender's absence and inbox, yet polite enough that a manager
would let it stand. It admits the sender is not checking email at all —
because the break is the point — and still promises a real reply, just
a slow and honest one.

> I'm out until Monday, and I'll be honest: I'm not checking email because I need this break, but I will reply — slowly, and in the order I can face them.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Requires Python 3, no dependencies, no network. The program writes the
reply to `/output/entry.txt` (creating the directory if needed) and
validates it first: exactly one sentence, 1–200 characters.

## License

[MIT License](LICENSE) — Copyright (c) 2026 A HUMAEDI.
