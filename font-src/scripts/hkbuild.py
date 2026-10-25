"""hkbuild — HK Poster Heavy 字形构建库（Wave 0 试用版）

用途
----
把「笔画原语」确定性地转换成 UFO (.glif) 轮廓。设计源是各 lane 的 recipe
Python 文件，生成物是 `.ufo` master，最终由 ufo2ft 编译为 TTF/OTF/WOFF2。

坐标系
------
y 向上，基线 y=0，em 盒 0..1000，ascender 880，descender -120。
所有数值单位是字体单位（font units），整数优先。

笔画语义
--------
每条笔画是「中心线 + 垂直权重」：
  * hbar(x1, x2, y, weight)  水平笔画，中心线在 y，横跨 x1..x2，厚 weight
  * vbar(x, y1, y2, weight)  垂直笔画，中心线在 x，跨 y1..y2，厚 weight
  * diag(x1, y1, x2, y2, w)  斜笔画，中心线两端点，厚度垂直于中心线
  * dot(cx, cy, w, h, slant) 点/短撇，平行四边形，slant 为顶部右移量
  * rect/poly               原始几何，用于字面框与特殊形状

端面切角 `cut_left` / `cut_right` 沿笔画方向偏移端面（单位为 font units），
用于海报式斜切端点（见 docs/03 的 GLY-003）。

轮廓生成
--------
所有笔画先求并集（shapely），因此生成的轮廓没有自交、没有重叠，
符合 docs/05「避免无意的自交、重叠和微小残留路径」。
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Iterable, Sequence

from shapely.geometry import Polygon
from shapely.geometry.polygon import orient
from shapely.ops import unary_union

# ---- 冻结参数（与 font-src/data/design-params.json 保持一致）----
UPM = 1000
ASCENDER = 880
DESCENDER = -120
DEFAULT_WEIGHT = 96

Point = tuple[int, int]


def _stroke_quad(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    weight: float,
    cut_start: float = 0.0,
    cut_end: float = 0.0,
) -> list[tuple[float, float]]:
    """中心线 (x1,y1)->(x2,y2) 的平头笔画多边形。

    cut_start / cut_end 沿笔画方向偏移端面，用于斜切端点。
    """
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy)
    if length == 0:
        raise ValueError("zero-length stroke")
    ux, uy = dx / length, dy / length
    px, py = -uy * weight / 2.0, ux * weight / 2.0
    a = (x1 + px + ux * cut_start, y1 + py + uy * cut_start)
    b = (x2 + px + ux * cut_end, y2 + py + uy * cut_end)
    c = (x2 - px + ux * cut_end, y2 - py + uy * cut_end)
    d = (x1 - px + ux * cut_start, y1 - py + uy * cut_start)
    return [a, b, c, d]


class Glyph:
    """一个字形：名字、advance、可选 Unicode、若干笔画。"""

    def __init__(
        self,
        name: str,
        advance: int = UPM,
        unicode: int | None = None,
        note: str = "",
    ) -> None:
        self.name = name
        self.advance = advance
        self.unicode = unicode
        self.note = note
        self._parts: list[list[tuple[float, float]]] = []

    # ---- 笔画原语 ----
    def hbar(
        self,
        x1: float,
        x2: float,
        y: float,
        weight: float = DEFAULT_WEIGHT,
        cut_left: float = 0.0,
        cut_right: float = 0.0,
    ) -> "Glyph":
        """水平笔画：中心线 y，横跨 x1..x2，厚 weight。"""
        self._parts.append(
            _stroke_quad(x1, y, x2, y, weight, cut_left, cut_right)
        )
        return self

    def vbar(
        self,
        x: float,
        y1: float,
        y2: float,
        weight: float = DEFAULT_WEIGHT,
        cut_bottom: float = 0.0,
        cut_top: float = 0.0,
    ) -> "Glyph":
        """垂直笔画：中心线 x，跨 y1..y2，厚 weight。"""
        self._parts.append(
            _stroke_quad(x, y1, x, y2, weight, cut_bottom, cut_top)
        )
        return self

    def diag(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        weight: float = DEFAULT_WEIGHT,
    ) -> "Glyph":
        """斜笔画：中心线 (x1,y1)->(x2,y2)，厚度垂直于中心线。"""
        self._parts.append(_stroke_quad(x1, y1, x2, y2, weight))
        return self

    def dot(
        self,
        cx: float,
        cy: float,
        w: float = DEFAULT_WEIGHT,
        h: float = 112,
        slant: float = 0.0,
    ) -> "Glyph":
        """点/短撇：平行四边形，中心 (cx,cy)，宽 w 高 h，顶部右移 slant。"""
        self._parts.append(
            [
                (cx - w / 2.0, cy - h / 2.0),
                (cx + w / 2.0, cy - h / 2.0),
                (cx + w / 2.0 + slant, cy + h / 2.0),
                (cx - w / 2.0 + slant, cy + h / 2.0),
            ]
        )
        return self

    def rect(self, x1: float, x2: float, y1: float, y2: float) -> "Glyph":
        """原始矩形。"""
        self._parts.append([(x1, y1), (x2, y1), (x2, y2), (x1, y2)])
        return self

    def ring(
        self, outer: Sequence[Sequence[float]], inner: Sequence[Sequence[float]]
    ) -> "Glyph":
        """环形带：outer/inner 是等长点列（对应点一一相接）。

        适合 O / D / 0 这类带内白（counter）的字形：外轮廓与内轮廓之间
        由若干梯形组成，并集后内白自动成为洞。
        """
        outer_pts = [(float(x), float(y)) for x, y in outer]
        inner_pts = [(float(x), float(y)) for x, y in inner]
        if len(outer_pts) != len(inner_pts) or len(outer_pts) < 3:
            raise ValueError("ring 需要等长且 >=3 的外/内点列")
        count = len(outer_pts)
        for index in range(count):
            nxt = (index + 1) % count
            self._parts.append(
                [outer_pts[index], outer_pts[nxt], inner_pts[nxt], inner_pts[index]]
            )
        return self

    def poly(self, points: Iterable[Sequence[float]]) -> "Glyph":
        """原始多边形（用于字面框、钩、特殊形状）。"""
        self._parts.append([(float(x), float(y)) for x, y in points])
        return self

    # ---- 轮廓输出 ----
    def contours(self) -> list[list[Point]]:
        """并集后的轮廓环列表：外环 + 内环（洞），坐标取整。"""
        if not self._parts:
            return []
        polys = []
        for pts in self._parts:
            poly = Polygon(pts)
            if not poly.is_valid:
                poly = poly.buffer(0)
            if not poly.is_empty:
                polys.append(poly)
        if not polys:
            return []
        merged = unary_union(polys)
        geoms = list(merged.geoms) if merged.geom_type == "MultiPolygon" else [merged]
        rings: list[list[Point]] = []
        for geom in geoms:
            if geom.is_empty:
                continue
            geom = orient(geom, sign=1.0)
            rings.append(_ring(geom.exterior.coords))
            for interior in geom.interiors:
                rings.append(_ring(interior.coords))
        return rings

    def draw(self, pen) -> None:
        """把轮廓画进一个 pen（ufoLib2 的 glyph pen）。"""
        for ring in self.contours():
            if len(ring) < 3:
                continue
            pen.moveTo(ring[0])
            for point in ring[1:]:
                pen.lineTo(point)
            pen.closePath()

    @property
    def ink_area(self) -> float:
        """墨量（平方单位），用于家族一致性检查。"""
        if not self._parts:
            return 0.0
        polys = []
        for pts in self._parts:
            poly = Polygon(pts)
            if not poly.is_valid:
                poly = poly.buffer(0)
            polys.append(poly)
        return float(unary_union(polys).area)


def _ring(coords) -> list[Point]:
    points = [(int(round(x)), int(round(y))) for x, y in coords]
    if len(points) > 1 and points[0] == points[-1]:
        points = points[:-1]
    deduped: list[Point] = []
    for point in points:
        if not deduped or deduped[-1] != point:
            deduped.append(point)
    if len(deduped) > 1 and deduped[0] == deduped[-1]:
        deduped = deduped[:-1]
    return deduped


def ellipse_points(
    cx: float, cy: float, rx: float, ry: float, count: int = 16
) -> list[tuple[float, float]]:
    """椭圆/圆角轮廓采样点（逆时针），供 ring() 使用。"""
    points = []
    for index in range(count):
        angle = 2 * math.pi * index / count
        points.append((cx + rx * math.cos(angle), cy + ry * math.sin(angle)))
    return points


def notdef_glyph() -> Glyph:
    """标准 .notdef：矩形框 + 内部斜杠。"""
    g = Glyph(".notdef", advance=UPM)
    g.rect(80, 920, 0, 700)
    return g


def space_glyph(advance: int = 500) -> Glyph:
    """空格：必须有 U+0020 映射，否则排版时空格会落到 .notdef。"""
    return Glyph("space", advance=advance, unicode=0x20)


def write_ufo(
    ufo_dir: str | Path,
    glyphs: Sequence[Glyph],
    family: str = "HK Poster",
    style: str = "Heavy",
    version: tuple[int, int] = (1, 0),
    postscript_name: str = "HKPoster-Heavy",
    note: str = "",
) -> Path:
    """把字形集合写成 UFO master（含 fontinfo.plist）。"""
    from ufoLib2 import Font

    font = Font()
    info = font.info
    info.unitsPerEm = UPM
    info.ascender = ASCENDER
    info.descender = DESCENDER
    info.familyName = family
    info.styleName = style
    info.versionMajor = version[0]
    info.versionMinor = version[1]
    info.openTypeNameVersion = f"Version {version[0]}.{version[1]:03d}"
    info.openTypeNameDesigner = "HK Poster Project"
    info.openTypeNameManufacturer = "HK Poster Project"
    info.openTypeNameDescription = (
        "HK Poster Heavy — 香港电影海报风格粗体（Wave 0 试制，未发布）"
    )
    # Heavy 不是 RIBBI 样式名，fontTools 的 buildNameTable 会把 family 拼成
    # "HK Poster Heavy"、subfamily 退化成 "Regular"。用排版家族名（nameID 16/17）
    # 表达真实的族名/样式名，与真实字体（Inter Black 之类）的做法一致。
    info.openTypeNamePreferredFamilyName = family
    info.openTypeNamePreferredSubfamilyName = style
    info.openTypeNamePreferredFamilyName = family
    info.openTypeNamePreferredSubfamilyName = style
    info.openTypeNameLicense = (
        "UNDECIDED — 发布前必须完成许可证审查（见 docs/08_授权与发布.md）"
    )
    info.copyright = "Copyright (c) 2026 HK Poster Project. All rights reserved."
    info.trademark = "HK Poster Heavy（暂定名，发布前须做名称/商标相似性检查）"
    info.openTypeOS2WeightClass = 900
    info.openTypeOS2WidthClass = 5
    info.openTypeOS2TypoAscender = ASCENDER
    info.openTypeOS2TypoDescender = DESCENDER
    info.openTypeOS2TypoLineGap = 0
    info.openTypeHheaAscender = ASCENDER
    info.openTypeHheaDescender = DESCENDER
    info.openTypeHheaLineGap = 0
    info.postscriptFontName = postscript_name
    info.note = note or "Wave 0 试制 master；轮廓由 hkbuild 笔画原语生成。"

    for glyph in glyphs:
        ufo_glyph = font.newGlyph(glyph.name)
        ufo_glyph.width = glyph.advance
        if glyph.unicode is not None:
            ufo_glyph.unicodes = [glyph.unicode]
        if glyph.note:
            ufo_glyph.note = glyph.note
        glyph.draw(ufo_glyph.getPen())

    path = Path(ufo_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    font.save(str(path), overwrite=True)
    return path
