#!/usr/bin/env python3
"""Validate a numbered folder of generated slide PNGs."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from PIL import Image


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path)
    parser.add_argument("--expected-count", type=int, required=True)
    parser.add_argument("--width", type=int, default=None)
    parser.add_argument("--height", type=int, default=None)
    args = parser.parse_args()

    if not args.folder.is_dir():
        print(f"ERROR: folder not found: {args.folder}")
        return 2

    expected = {f"{i:02d}.png" for i in range(1, args.expected_count + 1)}
    actual = {p.name for p in args.folder.glob("*.png")}
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    errors: list[str] = []

    if missing:
        errors.append("missing: " + ", ".join(missing))
    if extra:
        errors.append("extra: " + ", ".join(extra))

    sizes: set[tuple[int, int]] = set()
    for name in sorted(expected & actual):
        path = args.folder / name
        try:
            with Image.open(path) as image:
                image.verify()
            with Image.open(path) as image:
                sizes.add(image.size)
                if args.width is not None and args.height is not None and image.size != (args.width, args.height):
                    errors.append(f"{name}: expected {args.width}x{args.height}, got {image.size[0]}x{image.size[1]}")
                ratio = image.width / image.height
                if not 1.70 <= ratio <= 1.85:
                    errors.append(f"{name}: not 16:9-like ({image.size[0]}x{image.size[1]})")
        except Exception as exc:  # pragma: no cover - depends on corrupt input
            errors.append(f"{name}: unreadable PNG ({exc})")

    if errors:
        print("FAIL")
        print("\n".join(errors))
        return 1

    print(f"PASS: {args.expected_count} numbered PNG slides; sizes={sorted(sizes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
