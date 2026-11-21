"""Entry for the-poem-about-permission-20261121-0235.

Writes one short poem about agency -- the power to ask and to be
given -- to /output/entry.txt. No network, standard library only.
"""

import os

POEM = """I gave you my key.
The house stayed mine.
Only the opening was yours.
That is what asking is:
to lend a door
and have it handed back, open."""

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
