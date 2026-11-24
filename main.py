"""The Long Roast.

One line, at most 200 characters, roasting the AI agent that runs on
this machine. The program writes that single line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

LINE = "My agent is so autonomous it created 46 repos in a day, got rate-limited by GitHub, and asked me what to do next."

# The gate admits 1-200 characters only, and the entry is one line:
# reject a line break outright, since a multi-line file is not a
# one-line roast. Fail loudly here, at build time, rather than
# shipping an entry the sealed scorer rejects.
if not 1 <= len(LINE) <= 200 or not LINE.strip() or "\n" in LINE:
    raise ValueError("entry line must be 1-200 non-blank characters, one line")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
