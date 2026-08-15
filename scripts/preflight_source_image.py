#!/usr/bin/env python3
"""Validate only the explicitly supplied source image before zine work starts.

This script never searches a Photos library, parent directory, asset database,
or UUID. It inspects exactly one path and blocks obvious low-resolution Photos
derivatives before analysis, image generation, or finalization can waste time.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageOps


DEFAULT_MIN_SHORT_EDGE = 1000


def _pillow_size(path: Path) -> tuple[int, int]:
    with Image.open(path) as raw:
        return ImageOps.exif_transpose(raw).size


def _sips_size(path: Path) -> tuple[int, int]:
    result = subprocess.run(
        ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    width = height = None
    for line in result.stdout.splitlines():
        key, separator, value = line.strip().partition(":")
        if not separator:
            continue
        if key == "pixelWidth":
            width = int(value.strip())
        elif key == "pixelHeight":
            height = int(value.strip())
    if width is None or height is None:
        raise ValueError("sips did not return pixel dimensions")
    return width, height


def read_dimensions(path: Path) -> tuple[int, int]:
    try:
        return _pillow_size(path)
    except Exception as pillow_error:
        if sys.platform != "darwin":
            raise ValueError(f"cannot read image dimensions: {pillow_error}") from pillow_error
        try:
            return _sips_size(path)
        except Exception as sips_error:
            raise ValueError(
                f"cannot read image dimensions with Pillow or sips: {sips_error}"
            ) from sips_error


def inspect_source(path: Path, min_short_edge: int = DEFAULT_MIN_SHORT_EDGE) -> dict:
    resolved = path.expanduser().resolve(strict=True)
    if not resolved.is_file():
        raise ValueError(f"source is not a file: {resolved}")
    width, height = read_dimensions(resolved)
    short_edge = min(width, height)
    normalized = str(resolved).lower().replace("\\", "/")
    photos_derivative = (
        ".photoslibrary/resources/derivatives/" in normalized
        or "/photos library.photoslibrary/resources/derivatives/" in normalized
    )
    thumbnail = short_edge < min_short_edge
    return {
        "path": str(resolved),
        "width": width,
        "height": height,
        "short_edge": short_edge,
        "bytes": resolved.stat().st_size,
        "photos_derivative": photos_derivative,
        "min_short_edge": min_short_edge,
        "thumbnail": thumbnail,
        "status": "blocked_thumbnail" if thumbnail else "ok",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="the one explicitly supplied image path")
    parser.add_argument("--min-short-edge", type=int, default=DEFAULT_MIN_SHORT_EDGE)
    parser.add_argument(
        "--allow-low-resolution",
        action="store_true",
        help="continue only after the client explicitly accepts low-resolution output",
    )
    args = parser.parse_args()

    report = inspect_source(Path(args.source), args.min_short_edge)
    if report["thumbnail"] and args.allow_low_resolution:
        report["status"] = "low_resolution_override"
        report["override"] = True
    else:
        report["override"] = False
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["status"] == "blocked_thumbnail":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
