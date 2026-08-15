#!/usr/bin/env python3
"""Create an objective logo inspection sheet from a raster image."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
except ImportError as exc:  # pragma: no cover - environment-dependent message
    raise SystemExit("Pillow is required: install it with `python -m pip install Pillow`.") from exc


SIZES = (256, 128, 64, 32, 16)
PADDING = 24
LABEL_HEIGHT = 28


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build light, dark, and grayscale logo previews at multiple sizes."
    )
    parser.add_argument("input", type=Path, help="Source PNG, JPEG, or WebP image")
    parser.add_argument("--out", required=True, type=Path, help="Output PNG path")
    return parser.parse_args()


def contain(image: Image.Image, size: int) -> Image.Image:
    copy = image.copy()
    copy.thumbnail((size, size), Image.Resampling.LANCZOS)
    return copy


def composite(tile: Image.Image, logo: Image.Image, background: tuple[int, int, int, int]) -> None:
    tile.paste(background, (0, 0, tile.width, tile.height))
    x = (tile.width - logo.width) // 2
    y = LABEL_HEIGHT + (tile.height - LABEL_HEIGHT - logo.height) // 2
    tile.alpha_composite(logo, (x, y))


def main() -> int:
    args = parse_args()
    if not args.input.is_file():
        raise SystemExit(f"Input does not exist or is not a file: {args.input}")
    if args.out.suffix.lower() != ".png":
        raise SystemExit("--out must use a .png extension")

    with Image.open(args.input) as opened:
        original_size = opened.size
        original_mode = opened.mode
        logo = ImageOps.exif_transpose(opened).convert("RGBA")

    warnings: list[str] = []
    if abs(logo.width - logo.height) > max(logo.width, logo.height) * 0.1:
        warnings.append("Source is not approximately square; small-size comparisons include extra whitespace.")
    if original_mode not in ("RGBA", "LA", "P"):
        warnings.append("Source has no explicit alpha mode; transparency may not be present.")

    tile_size = max(SIZES) + PADDING * 2
    rows = ("Light", "Dark", "Grayscale")
    sheet = Image.new(
        "RGBA",
        (tile_size * len(SIZES), (tile_size + LABEL_HEIGHT) * len(rows)),
        (238, 240, 244, 255),
    )
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()

    for row_index, row_name in enumerate(rows):
        for column_index, size in enumerate(SIZES):
            tile = Image.new("RGBA", (tile_size, tile_size + LABEL_HEIGHT))
            preview = contain(logo, size)
            if row_name == "Grayscale":
                alpha = preview.getchannel("A")
                preview = ImageOps.grayscale(preview.convert("RGB")).convert("RGBA")
                preview.putalpha(alpha)
                background = (255, 255, 255, 255)
            elif row_name == "Dark":
                background = (24, 26, 31, 255)
            else:
                background = (255, 255, 255, 255)

            composite(tile, preview, background)
            label = f"{row_name} · {size}px"
            draw_tile = ImageDraw.Draw(tile)
            draw_tile.rectangle((0, 0, tile.width, LABEL_HEIGHT), fill=(238, 240, 244, 255))
            draw_tile.text((10, 8), label, fill=(25, 28, 34, 255), font=font)
            x = column_index * tile_size
            y = row_index * (tile_size + LABEL_HEIGHT)
            sheet.alpha_composite(tile, (x, y))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    sheet.convert("RGB").save(args.out, format="PNG", optimize=True)

    result = {
        "input": str(args.input.resolve()),
        "output": str(args.out.resolve()),
        "input_size": list(original_size),
        "input_mode": original_mode,
        "preview_sizes": list(SIZES),
        "rows": list(rows),
        "warnings": warnings,
    }
    json.dump(result, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
