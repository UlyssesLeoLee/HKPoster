"""render_glyph_sheet — 用 PIL/FreeType 把字形渲染成 PNG 证据（基础版）。

用法
----
    python font-src/scripts/render_glyph_sheet.py --font font-src/dist/HKPoster-Heavy.ttf \
        --text "港影龍義" --size 160 --out font-src/reports/sheet.png

正式样张（含黑白版 + 效果版、48/96/192 px、多行混排）由 specimens lane 负责，
本脚本只提供最小可用的渲染与目视检查手段。
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

if hasattr(sys, "stdout") and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).resolve().parent
FONT_SRC = SCRIPT_DIR.parent


def render(
    font_path: Path,
    text: str,
    size: int,
    out_path: Path,
    columns: int = 6,
    cell: int | None = None,
    padding: int = 24,
    label: bool = True,
) -> Path:
    font = ImageFont.truetype(str(font_path), size)
    cell = cell or int(size * 1.6)
    rows = (len(text) + columns - 1) // columns if columns else 1
    width = padding * 2 + columns * cell
    height = padding * 2 + rows * cell + (28 if label else 0)
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    if label:
        draw.text((padding, 6), f"{font_path.name} — {size}px", fill="black")

    for index, char in enumerate(text):
        row, column = divmod(index, columns)
        x = padding + column * cell
        y = padding + row * cell + (20 if label else 0)
        draw.text((x, y), char, font=font, fill="black")
        draw.rectangle(
            [x - 4, y - 4, x + cell - 8, y + cell - 8], outline=(220, 220, 220), width=1
        )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(out_path)
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser(description="渲染字形样张 PNG")
    parser.add_argument("--font", default=str(FONT_SRC / "dist" / "HKPoster-Heavy.ttf"))
    parser.add_argument("--text", default="港影龍義城火夜風警愛無道")
    parser.add_argument("--size", type=int, default=160)
    parser.add_argument("--out", default=str(FONT_SRC / "reports" / "glyph-sheet.png"))
    parser.add_argument("--columns", type=int, default=6)
    parser.add_argument("--no-label", action="store_true")
    args = parser.parse_args()

    font_path = Path(args.font).resolve()
    if not font_path.exists():
        print(f"[render] 找不到字体：{font_path}")
        return 1
    out = render(
        font_path,
        args.text,
        args.size,
        Path(args.out).resolve(),
        columns=args.columns,
        label=not args.no_label,
    )
    print(f"[render] 已输出 {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
