#!/usr/bin/env python3
"""News-image entry for make.fun's news-image-20261118 bounty.

Copies the front-page image (entry.png, drawn for Wednesday 18 November
2026) to the grader's output directory as entry.png.

Standard library only, no network, no randomness, no clock: the bytes
written are always exactly the bytes of entry.png beside this file, so two
runs produce identical output.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    src = HERE / "entry.png"
    if not src.is_file():
        raise SystemExit("entry.png is missing from the repository")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
