"""One Line, Zero Use — write the chosen useless-superpower line to /output/entry.txt.

Pure Python stdlib only. The line is a single original sentence, at most
200 characters, describing a hilariously useless superpower.
"""

import os

LINE = "I can turn any traffic light green \u2014 but only after I've already crossed the street."


def main():
    # Enforce the gate ourselves before writing: UTF-8 text, 1-200 chars,
    # not only whitespace. Fail loudly instead of shipping an invalid entry.
    text = LINE.strip()
    if not text or len(LINE) > 200:
        raise ValueError(f"line fails gate: {len(LINE)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote /output/entry.txt ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
