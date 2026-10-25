"""HK Poster Heavy —— Wave 0 Latin 大写 + 数字（lane: latin-core）。

字符清单（CONTRACT §5 冻结）：
    大写 A–Z（26）、数字 0–9（10），另加 features/kerning-latin.fea。

设计取舍
--------
1. 度量：UPM 1000，advance 一律 640，**大写顶线 y=700，基线 0**（家族一致性硬要求：
   check_glyphs 会在顶线离散 > 24 单位时 FAIL）。数字与 A 同高同宽。
2. 笔画权重三级：主竖/主横 96；斜笔画 84–88；次级横杠 84。
   统一视觉重量是 docs/03 GLY-001 的要求。
3. **对齐规则（本 recipe 的关键）**：笔画是「中心线 + 垂直权重」，所以要让墨迹
   极值对齐到 cap 线（700）与基线（0），中心线必须内缩半个笔画宽。
   因此横画用 `bar_top` / `bar_base` 生成，斜画用 `diag_cap_base` / `diag_top` /
   `diag_base` 自动回缩端点。竖画的中心线端点即墨迹端点，可直接用 vbar 的 y 值。
   这是 Latin 家族一致性（所有大写顶线齐平、基线齐平）能否成立的关键。
4. 曲线字母（B C D G O P Q R S U 0 3 5 6 8 9）用**圆弧带**而不是多边形拼块：
   `arc_band` 生成外弧 + 内弧的等宽带，端面径向硬切（GLY-002 硬折优先）；
   S / 2 / 3 / 5 这类复合曲线用 `band_along` 沿中心线折线生成等宽带。
   整圆弧一律取 16 段，保证 90° 正好落在采样点上（否则顶线会差几个单位）。
5. O 与 0 必须可区分：O 为正圆（rx=270，ry=350），0 略窄（rx=240，ry=350）。
6. 坐标全部取整；只用 hkbuild 与标准库；recipe 为纯函数，生成物确定。

运行：python font-src/src/hkposter-latin.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, write_ufo  # noqa: E402

ADV = 640
CAP = 700
BASE = 0
# 笔画权重：Latin 必须比 CJK 更粗。
# 同一个 96 单位在 1000 UPM 的 CJK 里读作 Heavy，但在 640 advance 的 Latin 里
# 只读作 Regular（笔画相对字面太小）。Wave 0 实测后把 Latin 的权重整体上调一档。
W_MAIN = 132
W_SEC = 120
W_DIAG = 112
W_THIN = 104
W_HAIR = 96

XL = 60
XR = 580
XC = 320


# ------------------------------------------------------------------ 曲线工具
def arc_pts(cx, cy, rx, ry, a0, a1, steps):
    pts = []
    for i in range(steps + 1):
        angle = math.radians(a0 + (a1 - a0) * i / steps)
        pts.append((cx + rx * math.cos(angle), cy + ry * math.sin(angle)))
    return pts


def arc_band(g, cx, cy, rx, ry, a0, a1, weight, steps=14):
    """圆弧带：外弧正向 + 内弧反向，端面径向硬切。"""
    outer = arc_pts(cx, cy, rx, ry, a0, a1, steps)
    inner = arc_pts(cx, cy, rx - weight, ry - weight, a0, a1, steps)
    g.poly([(round(x), round(y)) for x, y in outer + inner[::-1]])
    return g


def band_along(g, points, weight):
    """沿折线中心线生成等宽带。"""
    half = weight / 2.0
    left: list[tuple[float, float]] = []
    right: list[tuple[float, float]] = []
    count = len(points)
    for index, (x, y) in enumerate(points):
        if index == 0:
            dx, dy = points[1][0] - x, points[1][1] - y
        elif index == count - 1:
            dx, dy = x - points[index - 1][0], y - points[index - 1][1]
        else:
            dx = points[index + 1][0] - points[index - 1][0]
            dy = points[index + 1][1] - points[index - 1][1]
        length = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / length * half, dx / length * half
        left.append((x + nx, y + ny))
        right.append((x - nx, y - ny))
    g.poly([(round(x), round(y)) for x, y in left + right[::-1]])
    return g


# -------------------------------------------------------------- 对齐辅助
def bar_top(g, x1, x2, weight):
    """横画：墨迹上缘对齐 cap 线 700。"""
    g.hbar(x1, x2, CAP - weight / 2.0, weight)
    return g


def bar_base(g, x1, x2, weight):
    """横画：墨迹下缘对齐基线 0。"""
    g.hbar(x1, x2, BASE + weight / 2.0, weight)
    return g


def _perp_y(dx, dy, weight):
    length = math.hypot(dx, dy) or 1.0
    return abs(dx) / length * (weight / 2.0)


def diag_cap_base(g, x1, y1, x2, y2, weight):
    """斜笔画：两端墨迹极值分别对齐 cap 线与基线。"""
    off = _perp_y(x2 - x1, y2 - y1, weight)
    if y1 >= y2:
        y1, y2 = CAP - off, BASE + off
    else:
        y1, y2 = BASE + off, CAP - off
    g.diag(x1, y1, x2, y2, weight)
    return g


def diag_top(g, x1, y1, x2, y2, weight):
    """斜笔画：高端墨迹对齐 cap 线。"""
    off = _perp_y(x2 - x1, y2 - y1, weight)
    if y1 >= y2:
        y1 = CAP - off
    else:
        y2 = CAP - off
    g.diag(x1, y1, x2, y2, weight)
    return g


def diag_base(g, x1, y1, x2, y2, weight):
    """斜笔画：低端墨迹对齐基线。"""
    off = _perp_y(x2 - x1, y2 - y1, weight)
    if y1 >= y2:
        y2 = BASE + off
    else:
        y1 = BASE + off
    g.diag(x1, y1, x2, y2, weight)
    return g


def letter(name: str, unicode: int, strokes) -> Glyph:
    g = Glyph(name, advance=ADV, unicode=unicode, note=f"{name} — HK Poster Heavy Wave 0")
    for kind, *args in strokes:
        if kind == "arc":
            arc_band(g, *args)
        elif kind == "band":
            band_along(g, *args)
        elif kind == "bar_top":
            bar_top(g, *args)
        elif kind == "bar_base":
            bar_base(g, *args)
        elif kind == "diag_cb":
            diag_cap_base(g, *args)
        elif kind == "diag_t":
            diag_top(g, *args)
        elif kind == "diag_b":
            diag_base(g, *args)
        else:
            getattr(g, kind)(*args)
    return g


# ---------------------------------------------------------------- 大写字母
def upper() -> list[Glyph]:
    out: list[Glyph] = []

    out.append(letter("A", 0x41, [
        # A 的两条斜笔用 120 而非 132：加粗后 apex 内白会过度收口
        ("diag_cb", 50, BASE, XC, CAP, 120),
        ("diag_cb", 590, BASE, XC, CAP, 120),
        ("hbar", 140, 500, 230, W_THIN),
    ]))

    out.append(letter("B", 0x42, [
        ("vbar", 110, BASE, CAP, W_MAIN),
        ("arc", 110, 530, 270, 170, 90, -90, W_MAIN),
        ("arc", 110, 180, 290, 180, 90, -90, W_MAIN),
    ]))

    out.append(letter("C", 0x43, [
        ("arc", 330, 350, 250, 350, 55, 305, W_MAIN),
    ]))

    out.append(letter("D", 0x44, [
        ("vbar", 110, BASE, CAP, W_MAIN),
        ("arc", 110, 350, 270, 350, 90, -90, W_MAIN),
    ]))

    out.append(letter("E", 0x45, [
        ("vbar", 110, BASE, CAP, W_MAIN),
        ("bar_top", 110, 560, W_MAIN),
        ("hbar", 110, 520, 350, W_THIN),
        ("bar_base", 110, 520, W_MAIN),
    ]))

    out.append(letter("F", 0x46, [
        ("vbar", 110, BASE, CAP, W_MAIN),
        ("bar_top", 110, 560, W_MAIN),
        ("hbar", 110, 520, 350, W_THIN),
    ]))

    out.append(letter("G", 0x47, [
        ("arc", 330, 350, 250, 350, 55, 340, W_MAIN),
        ("vbar", 580, 230, 400, W_MAIN),
        ("hbar", 430, 580, 400, W_THIN),
    ]))

    out.append(letter("H", 0x48, [
        ("vbar", 110, BASE, CAP, W_MAIN),
        ("vbar", 530, BASE, CAP, W_MAIN),
        ("hbar", 110, 530, 330, W_THIN),
    ]))

    out.append(letter("I", 0x49, [
        ("vbar", XC, BASE, CAP, W_MAIN),
    ]))

    out.append(letter("J", 0x4A, [
        ("vbar", 470, CAP, 200, W_MAIN),
        ("arc", 300, 200, 170, 200, 0, -180, W_MAIN),
    ]))

    out.append(letter("K", 0x4B, [
        ("vbar", 110, BASE, CAP, W_MAIN),
        ("diag_t", 500, CAP, 180, 330, W_THIN),
        ("diag_b", 200, 390, 520, BASE, W_THIN),
    ]))

    out.append(letter("L", 0x4C, [
        ("vbar", 110, CAP, BASE, W_MAIN),
        ("bar_base", 110, 520, W_MAIN),
    ]))

    out.append(letter("M", 0x4D, [
        ("vbar", 90, BASE, CAP, W_MAIN),
        ("vbar", 550, BASE, CAP, W_MAIN),
        ("diag_t", 90, CAP, 320, 180, W_THIN),
        ("diag_t", 550, CAP, 320, 180, W_THIN),
    ]))

    out.append(letter("N", 0x4E, [
        ("vbar", 100, BASE, CAP, W_MAIN),
        ("vbar", 540, BASE, CAP, W_MAIN),
        ("diag_cb", 100, CAP, 540, BASE, W_THIN),
    ]))

    out.append(letter("O", 0x4F, [
        ("arc", XC, 350, 270, 350, 0, 360, W_MAIN, 16),
    ]))

    out.append(letter("P", 0x50, [
        ("vbar", 110, BASE, CAP, W_MAIN),
        ("arc", 110, 520, 270, 180, 90, -90, W_MAIN),
    ]))

    out.append(letter("Q", 0x51, [
        ("arc", XC, 350, 270, 350, 0, 360, W_MAIN, 16),
        ("diag_b", 380, 150, 540, -60, W_THIN),
    ]))

    out.append(letter("R", 0x52, [
        ("vbar", 110, BASE, CAP, W_MAIN),
        ("arc", 110, 520, 270, 180, 90, -90, W_MAIN),
        ("diag_b", 250, 340, 540, BASE, W_THIN),
    ]))

    out.append(letter("S", 0x53, [
        ("band", [
            (520, 582), (450, 616), (330, 632), (215, 598), (175, 532),
            (255, 460), (390, 424), (480, 352), (500, 250), (430, 128),
            (310, 66), (190, 100), (120, 156),
        ], W_MAIN),
    ]))

    out.append(letter("T", 0x54, [
        ("bar_top", XL, XR, W_MAIN),
        ("vbar", XC, BASE, CAP, W_MAIN),
    ]))

    out.append(letter("U", 0x55, [
        ("vbar", 110, CAP, 220, W_MAIN),
        ("vbar", 530, CAP, 220, W_MAIN),
        ("arc", 320, 220, 210, 220, 180, 360, W_MAIN),
    ]))

    out.append(letter("V", 0x56, [
        ("diag_cb", XL, CAP, XC, BASE, W_MAIN),
        ("diag_cb", XR, CAP, XC, BASE, W_MAIN),
    ]))

    out.append(letter("W", 0x57, [
        ("diag_cb", XL, CAP, 190, BASE, W_THIN),
        ("diag_t", 190, BASE, 320, 560, W_THIN),
        ("diag_b", 320, 560, 450, BASE, W_THIN),
        ("diag_cb", 450, BASE, XR, CAP, W_THIN),
    ]))

    out.append(letter("X", 0x58, [
        ("diag_cb", 70, CAP, 570, BASE, W_DIAG),
        ("diag_cb", 570, CAP, 70, BASE, W_DIAG),
    ]))

    out.append(letter("Y", 0x59, [
        ("diag_t", 70, CAP, 320, 340, W_DIAG),
        ("diag_t", 570, CAP, 320, 340, W_DIAG),
        ("vbar", 320, BASE, 340, W_DIAG),
    ]))

    out.append(letter("Z", 0x5A, [
        ("bar_top", 70, 570, W_MAIN),
        ("diag_cb", 570, CAP, 70, BASE, W_DIAG),
        ("bar_base", 70, 570, W_MAIN),
    ]))

    return out


# ------------------------------------------------------------------ 数字
def digits() -> list[Glyph]:
    out: list[Glyph] = []

    out.append(letter("zero", 0x30, [
        ("arc", XC, 350, 240, 350, 0, 360, W_MAIN, 16),
    ]))

    out.append(letter("one", 0x31, [
        ("vbar", 330, BASE, CAP, W_MAIN),
        ("hbar", 190, 430, 600, W_THIN),
        ("bar_base", 150, 510, W_MAIN),
    ]))

    out.append(letter("two", 0x32, [
        ("band", [
            (130, 512), (170, 582), (290, 632), (420, 626), (500, 572),
            (500, 492), (420, 414), (300, 300), (180, 152), (135, 66),
        ], W_MAIN),
        ("bar_base", 135, 570, W_MAIN),
    ]))

    out.append(letter("three", 0x33, [
        ("band", [
            (150, 584), (250, 632), (390, 628), (485, 584), (485, 520),
            (390, 440), (270, 405), (400, 375), (505, 310), (520, 190),
            (450, 96), (300, 66), (170, 102),
        ], W_MAIN),
    ]))

    out.append(letter("four", 0x34, [
        ("diag_t", 400, CAP, 90, 230, W_DIAG),
        ("hbar", 90, 580, 230, W_DIAG),
        ("vbar", 420, BASE, CAP, W_MAIN),
    ]))

    out.append(letter("five", 0x35, [
        ("bar_top", 110, 540, W_MAIN),
        ("vbar", 150, CAP, 420, W_MAIN),
        ("band", [
            (150, 420), (300, 448), (455, 400), (520, 280), (470, 132),
            (310, 66), (165, 98),
        ], W_MAIN),
    ]))

    out.append(letter("six", 0x36, [
        ("arc", XC, 220, 230, 220, 0, 360, W_MAIN, 16),
        ("band", [
            (480, 606), (350, 642), (225, 592), (165, 480), (150, 380),
        ], W_DIAG),
    ]))

    out.append(letter("seven", 0x37, [
        ("bar_top", XL, XR, W_MAIN),
        ("diag_cb", 540, CAP, 190, BASE, W_SEC),
    ]))

    out.append(letter("eight", 0x38, [
        ("arc", XC, 500, 195, 200, 0, 360, W_MAIN, 16),
        ("arc", XC, 200, 230, 200, 0, 360, W_MAIN, 16),
    ]))

    out.append(letter("nine", 0x39, [
        ("arc", XC, 480, 230, 220, 0, 360, W_MAIN, 16),
        ("band", [
            (480, 344), (495, 204), (440, 104), (310, 60), (180, 66),
        ], W_DIAG),
    ]))

    return out


def build() -> list[Glyph]:
    return upper() + digits()


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-latin.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
