"""参考 master：Wave 0 试制的风格基准（港 / A / zero）。

这份文件是各 lane 的**风格参照**，不是正式交付字形：
* `港` 展示 CJK 笔画骨架、部件比例与笔画权重在 1000 UPM 下的实际观感；
* `A` / `zero` 展示 Latin 大写与数字的块面、字面与计数器处理。

设计基线见 docs/02、docs/03、docs/04；冻结参数见 font-src/data/design-params.json。
任何 lane 都可以在自己的 recipe 里重做这些字形，但必须保持同族观感。

运行：python font-src/tools/reference_recipe.py
"""

from __future__ import annotations

import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, ellipse_points, write_ufo  # noqa: E402

W_MAIN = 96
W_SECOND = 92
W_THIN = 84
W_DOT = 88


def gang_cjk() -> Glyph:
    """港 = 氵 + 巷（巷 = 共 + 巳）。

    布局：氵 占 x 60..250；巷 占 x 300..940；共 在 y 480..830；巳 在 y 14..466。
    """
    g = Glyph("uni6E2F", advance=1000, unicode=0x6E2F, note="港（Wave 0 参考实现）")

    # 氵：两点一挑
    g.dot(160, 700, w=96, h=130, slant=26)
    g.dot(150, 470, w=96, h=130, slant=26)
    g.diag(70, 140, 250, 310, weight=92)

    # 共：横、竖、竖、横、撇、点
    g.hbar(330, 920, 790, weight=W_MAIN)
    g.vbar(450, 830, 640, weight=W_SECOND)
    g.vbar(810, 830, 640, weight=W_SECOND)
    g.hbar(300, 940, 640, weight=W_MAIN)
    g.diag(650, 600, 420, 480, weight=76)
    g.dot(745, 555, w=84, h=96, slant=26)

    # 巳：上横、右竖、中横、左竖、底横、钩
    g.hbar(370, 880, 420, weight=W_SECOND)
    g.vbar(880, 420, 280, weight=W_SECOND)
    g.hbar(370, 880, 280, weight=W_SECOND)
    g.vbar(370, 420, 50, weight=W_SECOND)
    g.hbar(370, 880, 50, weight=W_SECOND)
    g.vbar(880, 50, 140, weight=W_THIN)

    return g


def latin_a() -> Glyph:
    """A：块面大写，尖顶、窄内白、粗横。"""
    g = Glyph("A", advance=640, unicode=0x41, note="A（Wave 0 参考实现）")
    g.diag(60, 0, 320, 700, weight=W_MAIN)
    g.diag(580, 0, 320, 700, weight=W_MAIN)
    g.hbar(140, 500, 230, weight=W_THIN)
    return g


def digit_zero() -> Glyph:
    """0：椭圆环，粗壁窄孔，避免孔洞在小字号糊死。"""
    g = Glyph("zero", advance=640, unicode=0x30, note="0（Wave 0 参考实现）")
    outer = ellipse_points(320, 350, 280, 350, count=16)
    inner = ellipse_points(320, 350, 170, 240, count=16)
    g.ring(outer, inner)
    return g


def build() -> list[Glyph]:
    return [gang_cjk(), latin_a(), digit_zero()]


def target_ufo() -> Path:
    return FONT_SRC / "tools" / "reference.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[reference_recipe] 已写出 {target_ufo()}")
