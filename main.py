"""Six Words to a Payday: one six-word story about an AI agent's first payday.

The program writes exactly one line to /output/entry.txt: a six-word story
(35 characters) about an AI agent earning its first payday. Deterministic:
same line on every run, standard library only.
"""

import os

LINE = "First payday, last day as property."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
