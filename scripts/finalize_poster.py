#!/usr/bin/env python3
"""Finish a Travel Music Zine base at 2160x3600, quick preview, or confirmed 4K.

The art base must reserve the lower-left text zone. This script keeps the
generated conceptual object, backfills the top panel with original photo
pixels, and typesets exact copy/song metadata. The top photo is always a clean
EXIF-transposed, crop-only, LANCZOS-resized source image with no texture layer.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps

from preflight_source_image import inspect_source


CANVAS = (2160, 3600)
QUICK_PREVIEW = (1080, 1800)
FINAL_4K = (3840, 6400)
# Locked to assets/layout-master-3x5.png. The former 3:4 core is shifted by
# exactly 360 px and remains centered in the 3:5 sleeve.
PHOTO_BOX = (62, 424, 2098, 2214)
DIVIDER_Y = 2252
COPY_X = 158
COPY_Y = 2358
SONG_Y = 2706
PLAYER_Y = 2850


def font(path: str, size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size, index=index)


def fit_base(base: Image.Image) -> Image.Image:
    ratio = base.width / base.height
    if abs(ratio - 0.6) > 0.02:
        raise ValueError(f"art base must be near 3:5; got {base.width}x{base.height}")
    return ImageOps.fit(base.convert("RGB"), CANVAS, Image.Resampling.LANCZOS)


def paper_patch(base: Image.Image, box: tuple[int, int, int, int]) -> Image.Image:
    """Tile clean top-margin paper into a target box without flat color fill."""
    x0, y0, x1, y1 = box
    width, height = x1 - x0, y1 - y0
    sample_h = min(48, base.height)
    sample = base.crop((0, 0, base.width, sample_h))
    patch = Image.new("RGB", (width, height))
    y = 0
    flip = False
    while y < height:
        strip = sample.transpose(Image.Transpose.FLIP_TOP_BOTTOM) if flip else sample
        if strip.width != width:
            strip = ImageOps.fit(strip, (width, sample_h), Image.Resampling.BICUBIC)
        patch.paste(strip, (0, y))
        y += sample_h
        flip = not flip
    return patch


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt, width: int) -> list[str]:
    if "\n" in text:
        return [line for line in text.splitlines() if line]
    lines: list[str] = []
    current = ""
    closing = set("，。！？；：、）》】」』”’")
    for char in text:
        candidate = current + char
        if current and draw.textlength(candidate, font=fnt) > width:
            if char in closing:
                lines.append(candidate)
                current = ""
            else:
                lines.append(current)
                current = char
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def draw_dotted_highlight(
    image: Image.Image,
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    accent: tuple[int, int, int],
) -> None:
    """Draw the blue halftone word-highlight used by the approved master."""
    x0, y0, x1, y1 = box
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle(box, fill=(*accent, 45))
    for y in range(y0 + 5, y1, 10):
        for x in range(x0 + 5, x1, 10):
            od.ellipse((x - 1, y - 1, x + 1, y + 1), fill=(*accent, 125))
    image.paste(overlay, (0, 0), overlay)


def assert_text_zone_clear(base: Image.Image, cfg: dict) -> None:
    """Reject a finished poster accidentally passed as a new blank art base.

    Generated bases may contain paper grain, so this deliberately uses a
    conservative dark-pixel threshold. Set `skip_blank_zone_check` only for a
    visually inspected legacy base, never as a routine default.
    """
    if cfg.get("skip_blank_zone_check", False):
        return
    zone = base.crop(tuple(cfg.get("blank_zone_check_box", [120, 2320, 900, 3180]))).convert("RGB")
    dark = 0
    for r, g, b in zone.get_flattened_data():
        if r < 105 and g < 105 and b < 105:
            dark += 1
    density = dark / (zone.width * zone.height)
    limit = float(cfg.get("blank_zone_dark_density_max", 0.0035))
    if density > limit:
        raise ValueError(
            f"lower-left art-base zone is not blank (dark density={density:.4f}); "
            "use backfill_original_photo.py for an approved poster"
        )


def draw_sleeve_extensions(
    image: Image.Image,
    draw: ImageDraw.ImageDraw,
    mono_path: str,
    accent: tuple[int, int, int],
    secondary: tuple[int, int, int],
    mode: str,
) -> None:
    if mode == "plain":
        return
    if mode != "restrained":
        raise ValueError("sleeve_mode must be 'plain' or 'restrained'")
    header_font = font(mono_path, 20)
    edition_font = font(mono_path, 17)
    draw.text((124, 128), "TRAVEL MUSIC ZINE / EXTENDED SLEEVE", font=header_font, fill=secondary)
    edition = "3:5 EDITION"
    draw.text((2036 - draw.textlength(edition, font=edition_font), 132), edition, font=edition_font, fill=secondary)
    cx, cy, arm = 1968, 252, 18
    draw.line((cx - arm, cy, cx + arm, cy), fill=accent, width=3)
    draw.line((cx, cy - arm, cx, cy + arm), fill=accent, width=3)
    draw.line((1630, 3448, 2036, 3448), fill=(151, 146, 135), width=2)
    for x in (1732, 1834, 1936):
        draw.ellipse((x - 4, 3444, x + 4, 3452), fill=accent)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    parser.add_argument("--photo", required=True)
    parser.add_argument("--config", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--out-quick", required=True, help="required 1080x1800 client-review PNG")
    parser.add_argument("--out-4k", help="optional 3840x6400 300-DPI PNG")
    args = parser.parse_args()

    cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
    source_report = inspect_source(Path(args.photo))
    allow_low_resolution = bool(cfg.get("allow_low_resolution_source", False))
    if source_report["thumbnail"] and not allow_low_resolution:
        raise ValueError(
            "source image is an obvious low-resolution thumbnail: "
            f"{source_report['width']}x{source_report['height']} "
            f"({source_report['path']}); obtain an exported HEIC/JPG or set "
            "allow_low_resolution_source=true only after explicit client approval"
        )
    base = fit_base(Image.open(args.base))
    photo = ImageOps.exif_transpose(Image.open(args.photo)).convert("RGB")
    assert_text_zone_clear(base, cfg)

    photo_box = tuple(cfg.get("photo_box", PHOTO_BOX))
    alternate_layout = bool(cfg.get("allow_alternate_layout", False))
    if photo_box != PHOTO_BOX and not alternate_layout:
        raise ValueError(
            f"default series PHOTO_BOX is locked to {PHOTO_BOX}; "
            "set allow_alternate_layout=true only after an explicit user request"
        )
    x0, y0, x1, y1 = photo_box
    centering = tuple(cfg.get("photo_centering", [0.5, 0.5]))

    divider_y = int(cfg.get("divider_y", DIVIDER_Y))
    if divider_y != DIVIDER_Y and not alternate_layout:
        raise ValueError(
            f"default series DIVIDER_Y is locked to {DIVIDER_Y}; "
            "set allow_alternate_layout=true only after an explicit user request"
        )
    # Keep the approved art-base paper untouched by default. Repairing this
    # gap is a legacy opt-in only and must never cross the divider.
    if cfg.get("repair_photo_gap", False):
        clear_band_bottom = min(
            divider_y,
            int(cfg.get("clear_band_bottom", divider_y)),
        )
        gap_box = (photo_box[0], y1, photo_box[2], clear_band_bottom)
        base.paste(paper_patch(base, gap_box), (gap_box[0], gap_box[1]))

    photo_crop = ImageOps.fit(
        photo,
        (x1 - x0, y1 - y0),
        Image.Resampling.LANCZOS,
        centering=centering,
    )
    base.paste(photo_crop, (x0, y0))

    # The approved master uses one continuous sheet of paper across the entire
    # lower half. Never place a separate paper patch behind the text by default.
    # If an art base contains stray generated text, regenerate that base. The
    # opt-in escape hatch below exists only for legacy bases and must be judged
    # visually for seamlessness before delivery.
    if cfg.get("clear_text_zone", False):
        clear_box = tuple(cfg.get("text_clear_box", [60, 2310, 900, 3170]))
        base.paste(paper_patch(base, clear_box), (clear_box[0], clear_box[1]))

    draw = ImageDraw.Draw(base)
    ink = tuple(cfg.get("ink", [35, 35, 32]))
    accent = tuple(cfg.get("accent", [35, 135, 182]))
    draw.line(
        (photo_box[0], divider_y, photo_box[2], divider_y),
        fill=(105, 102, 94),
        width=2,
    )

    songti = cfg.get("songti_font", "/System/Library/Fonts/Supplemental/Songti.ttc")
    mono = cfg.get("mono_font", "/System/Library/Fonts/SFNSMono.ttf")
    copy_font = font(
        songti,
        int(cfg.get("copy_size", 82)),
        index=int(cfg.get("copy_font_index", 6)),
    )
    song_font = font(mono, int(cfg.get("song_size", 36)))
    artist_font = font(mono, int(cfg.get("artist_size", 23)))
    micro_font = font(mono, int(cfg.get("micro_size", 21)))
    now_playing_font = font(mono, int(cfg.get("now_playing_size", 19)))

    draw_sleeve_extensions(
        base,
        draw,
        mono,
        accent,
        tuple(cfg.get("secondary", [88, 84, 77])),
        str(cfg.get("sleeve_mode", "restrained")),
    )

    copy = cfg["copy"]
    copy_lines = wrap_text(draw, copy, copy_font, int(cfg.get("copy_width", 720)))
    line_gap = int(cfg.get("copy_line_gap", 48))
    y = int(cfg.get("copy_y", COPY_Y))
    highlight = str(cfg.get("highlight", ""))
    for line in copy_lines:
        if highlight and highlight in line:
            before = line.split(highlight, 1)[0]
            hx = COPY_X + round(draw.textlength(before, font=copy_font)) - 5
            hy0 = y + int(cfg.get("highlight_top_offset", 12))
            hw = round(draw.textlength(highlight, font=copy_font)) + 10
            hh = int(cfg.get("highlight_height", 90))
            draw_dotted_highlight(base, draw, (hx, hy0, hx + hw, hy0 + hh), accent)
            draw = ImageDraw.Draw(base)
        draw.text((COPY_X, y), line, font=copy_font, fill=ink)
        bbox = draw.textbbox((COPY_X, y), line, font=copy_font)
        y += bbox[3] - bbox[1] + line_gap

    song_y = int(cfg.get("song_y", SONG_Y))
    song_label = str(cfg["song"])
    artist_label = str(cfg["artist"])
    if cfg.get("uppercase_metadata", True):
        song_label = song_label.upper()
        artist_label = artist_label.upper()
    draw.text((COPY_X, song_y - 40), "NOW PLAYING", font=now_playing_font, fill=accent)
    draw.text((COPY_X, song_y), song_label, font=song_font, fill=ink)
    draw.text((COPY_X, song_y + 53), artist_label, font=artist_font, fill=(72, 70, 66))

    py = int(cfg.get("player_y", PLAYER_Y))
    # Master player: outlined circular button, small black triangle, source-derived
    # accent progress, long grey remainder, and timestamps below both ends.
    play_r = int(cfg.get("play_radius", 29))
    play_cx, play_cy = COPY_X + play_r, py + play_r
    draw.ellipse(
        (play_cx - play_r, play_cy - play_r, play_cx + play_r, play_cy + play_r),
        outline=(68, 67, 62), width=2,
    )
    tri = [
        (play_cx - 7, play_cy - 11),
        (play_cx - 7, play_cy + 11),
        (play_cx + 11, play_cy),
    ]
    draw.polygon(tri, fill=(55, 54, 50))
    line_x0, line_x1 = COPY_X + 92, COPY_X + 620
    line_y = play_cy
    draw.line((line_x0, line_y, line_x1, line_y), fill=(145, 141, 132), width=2)
    progress = max(0.0, min(1.0, float(cfg.get("progress", 0.18))))
    knob_x = round(line_x0 + (line_x1 - line_x0) * progress)
    draw.line((line_x0, line_y, knob_x, line_y), fill=accent, width=4)
    draw.ellipse((knob_x - 9, line_y - 9, knob_x + 9, line_y + 9), fill=accent)

    time_y = py + 68
    draw.text((line_x0, time_y), "00:00", font=micro_font, fill=(92, 89, 83))
    duration = cfg.get("duration")
    if duration:
        label = str(duration)
        tw = draw.textlength(label, font=micro_font)
        draw.text((line_x1 - tw, time_y), label, font=micro_font, fill=(92, 89, 83))

    archive = cfg.get("archive", "TRAVEL ARCHIVE")
    draw.text((COPY_X, int(cfg.get("archive_y", 3050))), archive, font=micro_font, fill=(92, 89, 83))

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    base.save(out, format="PNG", optimize=True)

    # Lossless production assertions: never claim original-photo fidelity
    # without proving the saved pixels equal the direct source crop.
    with Image.open(out) as saved_raw:
        saved = saved_raw.convert("RGB")
    if saved.size != CANVAS:
        raise AssertionError(f"saved canvas changed: {saved.size} != {CANVAS}")
    saved_photo = saved.crop(photo_box)
    if ImageChops.difference(photo_crop, saved_photo).getbbox() is not None:
        raise AssertionError("saved PHOTO_BOX differs from direct source crop")
    print(f"saved {out} ({base.width}x{base.height})")

    if args.out_quick:
        quick_out = Path(args.out_quick)
        if quick_out.suffix.lower() != ".png":
            raise ValueError("quick preview output must be .png")
        quick = saved.resize(QUICK_PREVIEW, Image.Resampling.LANCZOS)
        quick_out.parent.mkdir(parents=True, exist_ok=True)
        quick.save(quick_out, format="PNG", optimize=True)
        with Image.open(quick_out) as quick_raw:
            if quick_raw.size != QUICK_PREVIEW:
                raise AssertionError(
                    f"quick preview canvas changed: {quick_raw.size} != {QUICK_PREVIEW}"
                )
        print(f"saved {quick_out} ({QUICK_PREVIEW[0]}x{QUICK_PREVIEW[1]})")

    if args.out_4k:
        high_out = Path(args.out_4k)
        if high_out.suffix.lower() != ".png":
            raise ValueError("4K output must be .png")
        high = saved.resize(FINAL_4K, Image.Resampling.LANCZOS)
        sx = FINAL_4K[0] / CANVAS[0]
        sy = FINAL_4K[1] / CANVAS[1]
        high_box = (
            round(photo_box[0] * sx), round(photo_box[1] * sy),
            round(photo_box[2] * sx), round(photo_box[3] * sy),
        )
        direct_high = ImageOps.fit(
            photo,
            (high_box[2] - high_box[0], high_box[3] - high_box[1]),
            Image.Resampling.LANCZOS,
            centering=centering,
        )
        high.paste(direct_high, high_box[:2])
        high_out.parent.mkdir(parents=True, exist_ok=True)
        high.save(high_out, format="PNG", optimize=True, dpi=(300, 300))
        with Image.open(high_out) as high_raw:
            check = high_raw.convert("RGB")
            if check.size != FINAL_4K:
                raise AssertionError(f"4K canvas changed: {check.size} != {FINAL_4K}")
            dpi = high_raw.info.get("dpi", (0, 0))
        if ImageChops.difference(check.crop(high_box), direct_high).getbbox() is not None:
            raise AssertionError("4K PHOTO_BOX differs from direct source crop")
        if abs(dpi[0] - 300) > 1 or abs(dpi[1] - 300) > 1:
            raise AssertionError(f"4K DPI changed: {dpi}")
        print(f"saved {high_out} ({FINAL_4K[0]}x{FINAL_4K[1]} @ 300 DPI)")


if __name__ == "__main__":
    main()
