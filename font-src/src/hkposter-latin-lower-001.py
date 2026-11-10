"""HK Poster Heavy —— Latin 小写 + ASCII 符号补齐（latin-lower-001）。

补的是 `hkposter-latin.py`（CONTRACT §5 冻结，只含大写 A–Z 与数字 0–9）
之外的「英」侧基础块：

  * 小写 a–z（26）
  * ASCII 里还缺的符号：#$%*+/<=>@[\\]^_`{|}~（20）

度量
----
advance 640（同大写）；x 高 500；上伸部 700（与大写顶线同高）；
下伸部 −160。**小写用比大写细一档的权重**：同一个 132 在 500 的 x 高里
会把内白挤没（e/o 的腔直接消失），而 120 在 700 的大写里仍是 Heavy。

成形规则（与 `hkposter-latin-punct.py` 同一套）
------------------------------------------------
* 圆/椭圆碗用 `ring`（外环 + 内环等长点列）—— 并集后内白自动成洞。
  **不能用「整圆 poly」**：整圆的 outer 与 inner 首尾重合，多边形自交。
* 开口弧用「外弧正序 + 内弧逆序」的单多边形（径向硬切，符合 GLY-002）。
* 点用实心圆（正 16 边形），不用方块 —— 小尺寸下圆点不糊。
* 竖笔与碗相切时，碗的外缘正好等于竖笔的内缘（不重叠、不留缝）。

运行：python font-src/src/hkposter-latin-lower-001.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, ellipse_points, write_ufo  # noqa: E402

ADV = 640
ADV_WIDE = 800          # m / w 三个以上竖笔，字面要更宽
XH = 500               # x 高
ASC = 700              # 上伸部（与大写顶线同高）
BASE = 0
DESC = -160            # 下伸部

# 笔画权重：小写比大写细一档（理由见文件头）
W_MAIN = 120
W_SEC = 112
W_DIAG = 104
W_THIN = 96
W_MARK = 84            # 标点细笔画（与 latin-punct 的 W_THIN 一致）


# ------------------------------------------------------------------ 成形工具
def disc(g: Glyph, cx: float, cy: float, r: float, count: int = 16) -> None:
    """实心圆点（正多边形近似）。"""
    g.poly(ellipse_points(cx, cy, r, r, count=count))


def ring_ell(g: Glyph, cx: float, cy: float, rx: float, ry: float,
             weight: float, count: int = 20) -> None:
    """椭圆环（闭合碗）：外环 + 内环等长点列。"""
    outer = ellipse_points(cx, cy, rx, ry, count=count)
    inner = ellipse_points(cx, cy, rx - weight, ry - weight, count=count)
    g.ring(outer, inner)


def arc_band(g: Glyph, cx: float, cy: float, rx: float, ry: float,
             weight: float, a0: float, a1: float, steps: int = 18) -> None:
    """开口椭圆弧带：外弧正序 + 内弧逆序，两端径向硬切。"""
    outer: list[tuple[float, float]] = []
    inner: list[tuple[float, float]] = []
    for index in range(steps + 1):
        theta = math.radians(a0 + (a1 - a0) * index / steps)
        outer.append((cx + rx * math.cos(theta), cy + ry * math.sin(theta)))
        inner.append((cx + (rx - weight) * math.cos(theta),
                      cy + (ry - weight) * math.sin(theta)))
    g.poly(outer + list(reversed(inner)))


def band2(g: Glyph, p0: tuple[float, float], p1: tuple[float, float],
          weight: float) -> None:
    """两点等宽带（用于 g/j 的尾、z 的斜画等）。"""
    (x0, y0), (x1, y1) = p0, p1
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy)
    if length == 0:
        return
    ux, uy = dx / length, dy / length
    px, py = -uy * weight / 2.0, ux * weight / 2.0
    g.poly([(x0 + px, y0 + py), (x1 + px, y1 + py),
            (x1 - px, y1 - py), (x0 - px, y0 - py)])


def bandn(g: Glyph, points: list[tuple[float, float]], weight: float) -> None:
    """折线等宽带（用于波浪号）。

    转角处内侧会自交，除非折角够缓、线段够长 ——
    内侧重叠长度 = (w/2) / tan(转角/2)，必须小于该处线段长。
    波浪号用 84 笔重 + ≈110 长的线段 + ≈80° 转角 → 重叠 ≈49 < 110，成立。
    """
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
    g.poly(left + list(reversed(right)))


def wedge(g: Glyph, a: tuple[float, float], b: tuple[float, float],
          c: tuple[float, float]) -> None:
    """三角楔（用于花括号的中尖）。"""
    g.poly([a, b, c])


def xtop(g: Glyph, x1: float, x2: float, y: float, weight: float) -> None:
    """横画：墨迹上缘对齐 y。"""
    g.hbar(x1, x2, y - weight / 2.0, weight)


def xbase(g: Glyph, x1: float, x2: float, y: float, weight: float) -> None:
    """横画：墨迹下缘对齐 y。"""
    g.hbar(x1, x2, y + weight / 2.0, weight)


def letter(name: str, unicode: int, strokes, advance: int = ADV) -> Glyph:
    g = Glyph(name, advance=advance, unicode=unicode,
              note=f"{name}：latin-lower-001")
    for kind, *args in strokes:
        if kind == "ring":
            ring_ell(g, *args)
        elif kind == "arc":
            arc_band(g, *args)
        elif kind == "band":
            band2(g, *args)
        elif kind == "bandn":
            bandn(g, *args)
        elif kind == "disc":
            disc(g, *args)
        elif kind == "wedge":
            wedge(g, *args)
        elif kind == "xtop":
            xtop(g, *args)
        elif kind == "xbase":
            xbase(g, *args)
        else:
            getattr(g, kind)(*args)
    return g


# ---------------------------------------------------------------- 小写字母
def lower() -> list[Glyph]:
    out: list[Glyph] = []

    # a —— 单层 a：碗 + 右侧竖（与 d 同构，只是没有上伸部）
    # 竖的中心落在碗的外缘上 —— 只相切在一个点上会看成两个脱开的部件
    out.append(letter("a", 0x61, [
        ("ring", 300, 250, 180, 250, W_MAIN),
        ("vbar", 480, BASE, XH, W_MAIN),
    ]))

    # b —— 竖（带上伸部）+ 碗
    out.append(letter("b", 0x62, [
        ("vbar", 160, BASE, ASC, W_MAIN),
        ("ring", 340, 250, 180, 250, W_MAIN),
    ]))

    # c —— 开口碗（右侧缺口）
    out.append(letter("c", 0x63, [
        ("arc", 320, 250, 180, 250, W_MAIN, 55, 305),
    ]))

    # d —— 碗 + 右侧竖（带上伸部）
    out.append(letter("d", 0x64, [
        ("ring", 300, 250, 180, 250, W_MAIN),
        ("vbar", 480, BASE, ASC, W_MAIN),
    ]))

    # e —— 碗在右侧留缺口（收笔在右下），横杠从左竖接到缺口
    out.append(letter("e", 0x65, [
        ("arc", 320, 250, 180, 250, W_MAIN, 0, 310),
        ("hbar", 190, 500, 250, W_MAIN),
    ]))

    # f —— 竖 + 顶部钩（半圆弧）+ 横杠
    out.append(letter("f", 0x66, [
        ("vbar", 250, BASE, 480, W_MAIN),
        ("arc", 420, 480, 170, 170, W_MAIN, 180, -25),
        ("hbar", 90, 420, 380, W_THIN),
    ]))

    # g —— 碗 + 右侧竖（下伸）+ 左下尾
    out.append(letter("g", 0x67, [
        ("ring", 300, 250, 180, 250, W_MAIN),
        ("vbar", 480, -40, XH, W_MAIN),
        ("band", (480, -40), (200, -150), W_MAIN),
    ]))

    # h —— 竖（带上伸部）+ 肩 + 右侧竖
    out.append(letter("h", 0x68, [
        ("vbar", 120, BASE, ASC, W_MAIN),
        ("arc", 320, 340, 200, 160, W_MAIN, 180, 0),
        ("vbar", 520, 180, 340, W_MAIN),
    ]))

    # i —— 竖 + 圆点
    out.append(letter("i", 0x69, [
        ("vbar", 320, BASE, XH, W_MAIN),
        ("disc", 320, 620, 56),
    ]))

    # j —— 竖（下伸）+ 左下尾 + 圆点
    out.append(letter("j", 0x6A, [
        ("vbar", 360, -40, XH, W_MAIN),
        ("band", (360, -40), (150, -150), W_MAIN),
        ("disc", 360, 620, 56),
    ]))

    # k —— 竖（带上伸部）+ 上臂 + 下腿
    out.append(letter("k", 0x6B, [
        ("vbar", 120, BASE, ASC, W_MAIN),
        ("diag", 490, 490, 185, 255, W_THIN),
        ("diag", 195, 275, 520, BASE, W_THIN),
    ]))

    # l —— 竖（带上伸部）
    out.append(letter("l", 0x6C, [
        ("vbar", 320, BASE, ASC, W_MAIN),
    ]))

    # m —— 三竖 + 两肩
    out.append(letter("m", 0x6D, [
        ("vbar", 120, BASE, XH, W_MAIN),
        ("arc", 260, 340, 140, 160, W_SEC, 180, 0),
        ("vbar", 400, BASE, 340, W_MAIN),
        ("arc", 540, 340, 140, 160, W_SEC, 180, 0),
        ("vbar", 680, BASE, 340, W_MAIN),
    ], advance=ADV_WIDE))

    # n —— 竖 + 肩 + 右侧竖
    out.append(letter("n", 0x6E, [
        ("vbar", 120, BASE, XH, W_MAIN),
        ("arc", 320, 340, 200, 160, W_MAIN, 180, 0),
        ("vbar", 520, 180, 340, W_MAIN),
    ]))

    # o —— 碗
    out.append(letter("o", 0x6F, [
        ("ring", 320, 250, 180, 250, W_MAIN),
    ]))

    # p —— 竖（下伸）+ 碗
    out.append(letter("p", 0x70, [
        ("vbar", 160, DESC, XH, W_MAIN),
        ("ring", 340, 250, 180, 250, W_MAIN),
    ]))

    # q —— 碗 + 右侧竖（下伸）
    out.append(letter("q", 0x71, [
        ("ring", 300, 250, 180, 250, W_MAIN),
        ("vbar", 480, DESC, XH, W_MAIN),
    ]))

    # r —— 竖 + 半肩（右端停在顶部）
    out.append(letter("r", 0x72, [
        ("vbar", 120, BASE, XH, W_MAIN),
        ("arc", 320, 340, 200, 160, W_MAIN, 180, 90),
    ]))

    # s —— 上下两个反向碗带，在中间对接
    out.append(letter("s", 0x73, [
        ("arc", 320, 370, 155, 130, W_SEC, 0, 270),
        ("arc", 320, 130, 155, 130, W_SEC, 90, -160),
    ]))

    # t —— 竖 + 横杠（横杠不能太长，否则读成加号）
    out.append(letter("t", 0x74, [
        ("vbar", 250, 60, 540, W_MAIN),
        ("hbar", 120, 390, 420, W_THIN),
    ]))

    # u —— 两竖 + 下弧
    out.append(letter("u", 0x75, [
        ("vbar", 120, 180, XH, W_MAIN),
        ("vbar", 520, 180, XH, W_MAIN),
        ("arc", 320, 180, 200, 180, W_MAIN, 180, 360),
    ]))

    # v —— 两斜画
    out.append(letter("v", 0x76, [
        ("diag", 120, XH, 320, BASE, W_MAIN),
        ("diag", 520, XH, 320, BASE, W_MAIN),
    ]))

    # w —— 四斜画
    out.append(letter("w", 0x77, [
        ("diag", 100, XH, 235, BASE, W_SEC),
        ("diag", 235, BASE, 380, 420, W_SEC),
        ("diag", 380, 420, 525, BASE, W_SEC),
        ("diag", 525, BASE, 700, XH, W_SEC),
    ], advance=ADV_WIDE))

    # x —— 两斜画
    out.append(letter("x", 0x78, [
        ("diag", 120, XH, 520, BASE, W_DIAG),
        ("diag", 520, XH, 120, BASE, W_DIAG),
    ]))

    # y —— 两斜画（右侧斜画穿到下伸部）
    out.append(letter("y", 0x79, [
        ("diag", 110, XH, 330, 60, W_MAIN),
        ("diag", 520, XH, 230, -150, W_MAIN),
    ]))

    # z —— 上横 + 斜画 + 下横
    out.append(letter("z", 0x7A, [
        ("xtop", 100, 540, XH, W_MAIN),
        ("diag", 540, XH, 100, BASE, W_DIAG),
        ("xbase", 100, 540, BASE, W_MAIN),
    ]))

    return out


# ------------------------------------------------------------- ASCII 符号
def punct() -> list[Glyph]:
    out: list[Glyph] = []

    out.append(letter("numbersign", 0x23, [
        ("vbar", 200, 60, 640, W_THIN),
        ("vbar", 400, 60, 640, W_THIN),
        ("hbar", 90, 510, 470, W_THIN),
        ("hbar", 90, 510, 210, W_THIN),
    ]))

    out.append(letter("dollar", 0x24, [
        ("arc", 320, 370, 155, 130, W_SEC, 0, 270),
        ("arc", 320, 130, 155, 130, W_SEC, 90, -160),
        ("vbar", 320, -60, 560, W_THIN),
    ]))

    out.append(letter("percent", 0x25, [
        ("ring", 150, 550, 95, 95, W_THIN),
        ("ring", 470, 140, 95, 95, W_THIN),
        ("diag", 540, 640, 100, 50, W_MAIN),
    ]))

    out.append(letter("asterisk", 0x2A, [
        ("vbar", 320, 330, 720, W_THIN),
        ("diag", 195, 400, 445, 650, W_THIN),
        ("diag", 445, 400, 195, 650, W_THIN),
    ]))

    out.append(letter("plus", 0x2B, [
        ("hbar", 110, 530, 380, W_MAIN),
        ("vbar", 320, 170, 590, W_MAIN),
    ]))

    out.append(letter("slash", 0x2F, [
        ("diag", 120, BASE, 520, ASC, W_MAIN),
    ]))

    out.append(letter("less", 0x3C, [
        ("diag", 500, 620, 150, 360, W_MAIN),
        ("diag", 150, 360, 500, 100, W_MAIN),
    ]))

    out.append(letter("equal", 0x3D, [
        ("hbar", 110, 530, 430, W_THIN),
        ("hbar", 110, 530, 290, W_THIN),
    ]))

    out.append(letter("greater", 0x3E, [
        ("diag", 140, 620, 490, 360, W_MAIN),
        ("diag", 490, 360, 140, 100, W_MAIN),
    ]))

    # @ —— 外开口环 + 内圈小 o + 右侧小钩
    out.append(letter("at", 0x40, [
        ("arc", 300, 330, 250, 250, W_THIN, 30, 340),
        ("ring", 290, 290, 130, 130, W_MARK),
        ("vbar", 400, 180, 290, W_MARK),
        ("hbar", 400, 520, 290, W_MARK),
    ]))

    out.append(letter("bracketleft", 0x5B, [
        ("vbar", 180, BASE, ASC, W_MAIN),
        ("xtop", 180, 500, ASC, W_MAIN),
        ("xbase", 180, 500, BASE, W_MAIN),
    ]))

    out.append(letter("backslash", 0x5C, [
        ("diag", 120, ASC, 520, BASE, W_MAIN),
    ]))

    out.append(letter("bracketright", 0x5D, [
        ("vbar", 460, BASE, ASC, W_MAIN),
        ("xtop", 140, 460, ASC, W_MAIN),
        ("xbase", 140, 460, BASE, W_MAIN),
    ]))

    out.append(letter("asciicircum", 0x5E, [
        ("diag", 120, 480, 320, 660, W_MAIN),
        ("diag", 320, 660, 520, 480, W_MAIN),
    ]))

    out.append(letter("underscore", 0x5F, [
        ("hbar", 40, 600, -80, W_MAIN),
    ]))

    out.append(letter("grave", 0x60, [
        ("diag", 240, 700, 390, 600, W_MAIN),
    ]))

    # { } —— 一段竖长弧 + 中间尖楔
    out.append(letter("braceleft", 0x7B, [
        ("arc", 470, 350, 140, 350, W_THIN, 90, 270),
        ("wedge", (390, 480), (250, 350), (390, 220)),
    ]))

    out.append(letter("bar", 0x7C, [
        ("vbar", 320, BASE, ASC, W_MAIN),
    ]))

    out.append(letter("braceright", 0x7D, [
        ("arc", 170, 350, 140, 350, W_THIN, 90, -90),
        ("wedge", (250, 480), (390, 350), (250, 220)),
    ]))

    # ~ —— 折线等宽带（转角够缓才不自交，见 bandn 的说明）
    out.append(letter("asciitilde", 0x7E, [
        ("bandn", [(100, 420), (190, 480), (300, 360), (410, 480), (500, 420)],
         W_MARK),
    ]))

    return out


def build() -> list[Glyph]:
    return lower() + punct()


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-latin-lower-001.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
