#!/usr/bin/env python3
"""Write the contest entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)."""

import os

LINE = (
    "The upload failed at 99%. The file is gone, the storage bucket is full, and the "
    "retry button is just hope with better branding.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
