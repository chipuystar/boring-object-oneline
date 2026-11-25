"""The Most Boring Object, Reviewed in One Line — make.fun entry.

Writes the one-line doorstop review (112 characters) to /output/entry.txt
for the judge. The joke is the doorstop's own dullness: it only sits
there, yet it gets kicked, tripped over, and blamed when the door slams.
"""

import os

LINE = "The doorstop: a wedge whose whole career is getting kicked, tripped over, and blamed when the door slams anyway."


def main() -> None:
    # Mirror the scorer's gate: 1-200 chars, not whitespace-only.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("review line must be 1-200 characters, not whitespace-only")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
