#!/usr/bin/env python3
"""Replace only the locked photo box in an approved 3:5 poster.

Use this for crop/ratio/original-photo fixes after the lower design is already
approved. It performs EXIF transpose + crop + scale + LANCZOS only, writes a
lossless PNG, and proves that every pixel outside PHOTO_BOX stayed unchanged.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageChops, ImageOps


CANVAS = (2160, 3600)
PHOTO_BOX = (62, 424, 2098, 2214)
PHOTO_SIZE = (PHOTO_BOX[2] - PHOTO_BOX[0], PHOTO_BOX[3] - PHOTO_BOX[1])


def require_equal(left: Image.Image, right: Image.Image, label: str) -> None:
    if left.size != right.size:
        raise AssertionError(f"{label} size changed: {left.size} != {right.size}")
    if ImageChops.difference(left, right).getbbox() is not None:
        raise AssertionError(f"{label} changed")


def load_source(path: Path, centering: tuple[float, float]) -> Image.Image:
    try:
        with Image.open(path) as raw:
            source = ImageOps.exif_transpose(raw).convert("RGB")
    except Exception as exc:
        raise RuntimeError(
            "Could not decode the source. For HEIC, convert a temporary copy "
            "to PNG/JPEG first; never modify the original file."
        ) from exc
    return ImageOps.fit(
        source,
        PHOTO_SIZE,
        method=Image.Resampling.LANCZOS,
        centering=centering,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True, help="approved 2160x3600 poster")
    parser.add_argument("--source", required=True, help="original photo or temp HEIC conversion")
    parser.add_argument("--out", required=True, help="lossless .png output")
    parser.add_argument("--center-x", type=float, default=0.5)
    parser.add_argument("--center-y", type=float, default=0.5)
    args = parser.parse_args()

    out_path = Path(args.out)
    if out_path.suffix.lower() != ".png":
        raise ValueError("output must be .png for pixel-exact verification")
    centering = (args.center_x, args.center_y)
    if any(value < 0.0 or value > 1.0 for value in centering):
        raise ValueError("centering values must be between 0 and 1")

    with Image.open(args.base) as base_raw:
        base = base_raw.convert("RGB")
    if base.size != CANVAS:
        raise ValueError(f"base must be {CANVAS}; got {base.size}")

    photo = load_source(Path(args.source), centering)
    result = base.copy()
    result.paste(photo, (PHOTO_BOX[0], PHOTO_BOX[1]))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    result.save(out_path, format="PNG", optimize=True)

    with Image.open(out_path) as saved_raw:
        saved = saved_raw.convert("RGB")
    if saved.size != CANVAS:
        raise AssertionError(f"saved canvas changed: {saved.size} != {CANVAS}")

    require_equal(
        photo,
        saved.crop(PHOTO_BOX),
        "saved PHOTO_BOX versus direct original crop",
    )
    # The whole information/object region is frozen, starting at photo bottom.
    require_equal(
        base.crop((0, PHOTO_BOX[3], CANVAS[0], CANVAS[1])),
        saved.crop((0, PHOTO_BOX[3], CANVAS[0], CANVAS[1])),
        "lower poster region y>=2214",
    )
    # Explicitly prove the approved photo margins and top paper did not move.
    unchanged_regions = {
        "top paper": (0, 0, CANVAS[0], PHOTO_BOX[1]),
        "left photo margin": (0, PHOTO_BOX[1], PHOTO_BOX[0], PHOTO_BOX[3]),
        "right photo margin": (PHOTO_BOX[2], PHOTO_BOX[1], CANVAS[0], PHOTO_BOX[3]),
    }
    for label, box in unchanged_regions.items():
        require_equal(base.crop(box), saved.crop(box), label)

    # The 360 px top/bottom sleeve is part of the approved base and must remain
    # byte-for-byte frozen during a crop-only repair.
    require_equal(base.crop((0, 0, CANVAS[0], 360)), saved.crop((0, 0, CANVAS[0], 360)), "top sleeve")
    require_equal(base.crop((0, 3240, CANVAS[0], 3600)), saved.crop((0, 3240, CANVAS[0], 3600)), "bottom sleeve")

    print(
        f"saved {out_path} | canvas={CANVAS} | photo_box={PHOTO_BOX} | "
        f"centering={centering} | pixel assertions=PASS"
    )


if __name__ == "__main__":
    main()
