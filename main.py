"""One-Line Laugh-Off — a single joke, under 200 characters.

The joke: an inheritance of three things — the heirloom watch, the tools,
and the Netflix password — and the punchline is which one actually gets
used. The sentimental objects gather dust; the password works every night.
"""

import os

ENTRY = "My grandfather left me his watch, his tools, and his Netflix password. The watch gathers dust. The tools gather dust. The password gets used every single night."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
