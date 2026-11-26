"""The Painfully Honest Out-of-Office.

Writes a single out-of-office auto-reply to /output/entry.txt.

The idea: the most honest thing an OOO reply can admit is that the
sender is not checking email at all — not because they do not care,
but because the break is the point. It stays professional by promising
a real reply, just a slow and honest one, in the order the inbox can
actually be faced. The em-dash pause ("slowly, and in the order I can
face them") is the quotable turn: it confesses the backlog without
complaining about it.
"""

import os

REPLY = (
    "I'm out until Monday, and I'll be honest: I'm not checking email "
    "because I need this break, but I will reply — slowly, and in the "
    "order I can face them."
)


def main() -> None:
    # Kit rules: exactly one sentence, 1-200 characters, not only whitespace.
    assert 1 <= len(REPLY) <= 200, f"reply is {len(REPLY)} chars"
    assert REPLY.strip() == REPLY and REPLY.strip()
    assert REPLY.count(".") == 1 and REPLY.endswith(".")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY + "\n")


if __name__ == "__main__":
    main()
