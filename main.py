"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.
Deterministic, no network access, standard library only.
Running it twice produces the same file byte for byte.
"""

import os
from pathlib import Path

JOKE = "I asked my barber for a haircut like I have somewhere to be. He gave me one that lies."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
