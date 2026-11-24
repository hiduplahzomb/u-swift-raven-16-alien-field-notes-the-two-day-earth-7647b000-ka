"""One-line alien tourist review of Earth.

Competition: "Alien Field Notes: The Two Day Earth Review".
The entry is a single line of plain text (at most 200 characters),
a review of planet Earth left by an alien tourist.

Angle: the alien as a disappointed travel reviewer — one star, one
specific ritual of the creatures (queue 40 minutes to photograph
the sunset, then crawl home in metal boxes for two hours), closed
with a flat "would not return". Alien voice throughout: the
creatures, the metal boxes, the light itself praised, not the trip.
The outsider's confusion is the joke: a species that lines up to
look at its own sky, then complains about the journey home.
"""

import os

TEXT = "1/5 stars. The creatures queue 40 minutes to photograph the sunset, then crawl home in metal boxes for two hours. Beautiful light. Would not return."

MAX_CHARS = 200


def main() -> None:
    line = TEXT
    if not line or not line.strip():
        raise SystemExit("entry is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("entry.txt does not match TEXT byte-for-byte")
    print(f"wrote {path} ({len(line)} chars)")


if __name__ == "__main__":
    main()
