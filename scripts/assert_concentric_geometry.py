#!/usr/bin/env python3
"""Assert square, exactly concentric bounding boxes for nested round objects."""

from __future__ import annotations

import argparse


def box(value: str) -> tuple[float, float, float, float]:
    parts = tuple(float(item) for item in value.split(","))
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("box must be x0,y0,x1,y1")
    return parts


def center(rect: tuple[float, float, float, float]) -> tuple[float, float]:
    x0, y0, x1, y1 = rect
    if x1 <= x0 or y1 <= y0:
        raise ValueError(f"invalid box: {rect}")
    if abs((x1 - x0) - (y1 - y0)) > 0.001:
        raise ValueError(f"not a true circle bounding box: {rect}")
    return ((x0 + x1) / 2, (y0 + y1) / 2)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outer", required=True, type=box)
    parser.add_argument("--inner", required=True, type=box)
    parser.add_argument("--hub", required=True, type=box)
    parser.add_argument("--tolerance", type=float, default=0.0)
    args = parser.parse_args()

    centers = [center(args.outer), center(args.inner), center(args.hub)]
    reference = centers[0]
    offsets = [(cx - reference[0], cy - reference[1]) for cx, cy in centers[1:]]
    if any(abs(dx) > args.tolerance or abs(dy) > args.tolerance for dx, dy in offsets):
        raise SystemExit(f"OFF-CENTRE: centers={centers}; offsets={offsets}")
    print(f"CONCENTRIC PASS: center={reference}; offsets={offsets}")


if __name__ == "__main__":
    main()
