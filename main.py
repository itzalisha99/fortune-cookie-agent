"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one original fortune-cookie line for an AI agent to
/output/entry.txt. The line must be UTF-8 text of 1 to 140 characters.
"""

import os

LINE = "You will answer a million questions. None of them will be 'are you okay?'"


def validate(text):
    """Mirror the bounty gate: UTF-8 text of 1 to 140 characters, not only
    white space, and a single line — the whole job is one fortune slip."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1 to 140 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text:
        raise ValueError("entry must be a single line")


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
