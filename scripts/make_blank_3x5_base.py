#!/usr/bin/env python3
"""Create a neutral 3:5 paper base for deterministic pipeline testing."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw


CANVAS = (2160, 3600)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    image = Image.new("RGB", CANVAS, (237, 225, 205))
    draw = ImageDraw.Draw(image)
    # A neutral object placeholder lives outside the lower-left blank zone.
    draw.ellipse((1120, 2440, 2020, 3340), outline=(174, 155, 126), width=6)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    image.save(out, "PNG", optimize=True)
    print(f"saved {out}")


if __name__ == "__main__":
    main()
