"""HK Poster Heavy —— Latin 扩展补齐（latin-ext-001）。

补 `hkposter-latin.py`（A–Z + 0–9）、`hkposter-latin-lower-001.py`（a–z + ASCII 符号）
之外的「英」侧剩余块：

  * Latin-1 Supplement（U+00A0–U+00FF）：带音符拉丁字母 + 独立符号
  * General Punctuation（U+2010–U+203E 常用子集）：引号 / 破折号 / 省略号 / 记号
  * Fullwidth Forms（U+FF01–U+FF60）：ASCII 的全角版

实现原则
--------
1. **不描轮廓**：带音符字母 = **底字母的原语**（`_parts` / `_prims` 深拷贝）
   + 一枚**独立记号笔画**。底字母直接 import 既有 recipe 拿 `build()` 的结果。
2. **全角形 = ASCII 形原样水平居中到 1000 advance**（不缩放）：
   全角拉丁字母的 x 高 / cap 高与比例形一致（CJK 字体的常规做法），
   缩放会把 120 的笔重拉成 168，比汉字还重。
3. 记号位置：**记号中心 y = 底字母顶 + 62**。
   全高/有上伸部的（cap 700）→ 762；x 高字母（500）→ 562；
   i/j 的记号**替代点**，落在 660。
4. 既有 recipe 已有的全角标点（FF01/FF08/FF09/FF0C/FF1A/FF1B/FF1F）**跳过**。

运行：python font-src/src/hkposter-latin-ext-001.py
"""

from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, ellipse_points, write_ufo  # noqa: E402

ADV = 640
CJK_ADV = 1000
W_MAIN = 120
W_MARK = 84

# ------------------------------------------------------------------ 底字母来源
def _load(stem: str):
    path = FONT_SRC / "src" / (stem + ".py")
    spec = importlib.util.spec_from_file_location("hkext_" + stem.replace("-", "_"), path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


BASE: dict[int, Glyph] = {}
for _stem in ("hkposter-latin", "hkposter-latin-lower-001", "hkposter-latin-punct"):
    for _g in _load(_stem).build():
        BASE.setdefault(_g.unicode, _g)


# ------------------------------------------------------------------ 成形工具
def disc(g: Glyph, cx: float, cy: float, r: float, count: int = 16) -> None:
    g.poly(ellipse_points(cx, cy, r, r, count=count))


def ring_ell(g: Glyph, cx: float, cy: float, rx: float, ry: float,
             weight: float, count: int = 20) -> None:
    outer = ellipse_points(cx, cy, rx, ry, count=count)
    inner = ellipse_points(cx, cy, rx - weight, ry - weight, count=count)
    g.ring(outer, inner)


def band2(g: Glyph, p0: tuple[float, float], p1: tuple[float, float],
          weight: float) -> None:
    (x0, y0), (x1, y1) = p0, p1
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy)
    if length == 0:
        return
    ux, uy = dx / length, dy / length
    px, py = -uy * weight / 2.0, ux * weight / 2.0
    g.poly([(x0 + px, y0 + py), (x1 + px, y1 + py),
            (x1 - px, y1 - py), (x0 - px, y0 - py)])


def bbox(g: Glyph) -> tuple[float, float, float, float]:
    xs = [p[0] for part in g._parts for p in part]
    ys = [p[1] for part in g._parts for p in part]
    if not xs:
        return (0.0, 0.0, 0.0, 0.0)
    return (min(xs), min(ys), max(xs), max(ys))


def clone_parts(dst: Glyph, src: Glyph, dx: float = 0.0, dy: float = 0.0,
                sx: float = 1.0, sy: float = 1.0) -> None:
    """把 src 的原语按 (sx, sy) 缩放 + (dx, dy) 平移后追加到 dst。"""
    for part, prim in zip(src._parts, src._prims):
        dst._parts.append([(x * sx + dx, y * sy + dy) for (x, y) in part])
        new_prim = dict(prim)
        for key in ("x1", "x2", "x", "cx"):
            if new_prim.get(key) is not None:
                new_prim[key] = new_prim[key] * sx + dx
        for key in ("y", "y1", "y2", "cy"):
            if new_prim.get(key) is not None:
                new_prim[key] = new_prim[key] * sy + dy
        dst._prims.append(new_prim)


# ------------------------------------------------------------------ 记号
def mark_acute(g: Glyph, cx: float, cy: float) -> None:
    g.poly([(cx - 36, cy - 44), (cx - 6, cy - 44), (cx + 44, cy + 44), (cx + 14, cy + 44)])


def mark_grave(g: Glyph, cx: float, cy: float) -> None:
    g.poly([(cx + 36, cy - 44), (cx + 6, cy - 44), (cx - 44, cy + 44), (cx - 14, cy + 44)])


def mark_circumflex(g: Glyph, cx: float, cy: float) -> None:
    g.diag(cx - 54, cy - 40, cx, cy + 42, W_MARK)
    g.diag(cx, cy + 42, cx + 54, cy - 40, W_MARK)


def mark_caron(g: Glyph, cx: float, cy: float) -> None:
    g.diag(cx - 54, cy + 40, cx, cy - 42, W_MARK)
    g.diag(cx, cy - 42, cx + 54, cy + 40, W_MARK)


def mark_diaeresis(g: Glyph, cx: float, cy: float) -> None:
    disc(g, cx - 48, cy, 40)
    disc(g, cx + 48, cy, 40)


def mark_tilde(g: Glyph, cx: float, cy: float) -> None:
    band2(g, (cx - 62, cy + 14), (cx - 20, cy - 22), 62)
    band2(g, (cx - 20, cy - 22), (cx + 20, cy + 14), 62)
    band2(g, (cx + 20, cy + 14), (cx + 62, cy - 22), 62)


def mark_ring(g: Glyph, cx: float, cy: float) -> None:
    ring_ell(g, cx, cy, 54, 54, 34)


def mark_macron(g: Glyph, cx: float, cy: float) -> None:
    g.hbar(cx - 60, cx + 60, cy, 76)


def mark_breve(g: Glyph, cx: float, cy: float) -> None:
    g.diag(cx - 50, cy - 20, cx, cy + 22, 72)
    g.diag(cx, cy + 22, cx + 50, cy - 20, 72)


def mark_cedilla(g: Glyph, cx: float, cy: float) -> None:
    g.poly([(cx - 34, cy + 26), (cx + 16, cy + 26), (cx + 16, cy - 26),
            (cx - 6, cy - 62), (cx - 34, cy - 50), (cx - 16, cy - 20), (cx - 34, cy + 2)])


MARKS = {
    "acute": mark_acute,
    "grave": mark_grave,
    "circumflex": mark_circumflex,
    "caron": mark_caron,
    "diaeresis": mark_diaeresis,
    "tilde": mark_tilde,
    "ring": mark_ring,
    "macron": mark_macron,
    "breve": mark_breve,
}

# 记号纵向位置：按底字母类别
MARK_Y_CAP = 762.0      # 全高 / 有上伸部的底字母（顶 700）
MARK_Y_X = 562.0        # x 高底字母（顶 500）
MARK_Y_DOT = 664.0      # i/j：记号替代点
MARK_Y_BELOW = -10.0    # 下加符（cedilla）


def _mark_center(base: Glyph) -> float:
    x0, y0, x1, y1 = bbox(base)
    top = y1
    if top >= 640:
        return MARK_Y_CAP
    return MARK_Y_X


# ------------------------------------------------------------------ 带音符字母
# (码位, 底字母码位, 记号)
ACCENTED: list[tuple[int, int, str]] = [
    (0xC0, 0x41, "grave"), (0xC1, 0x41, "acute"), (0xC2, 0x41, "circumflex"),
    (0xC3, 0x41, "tilde"), (0xC4, 0x41, "diaeresis"), (0xC5, 0x41, "ring"),
    (0xC7, 0x43, "cedilla"),
    (0xC8, 0x45, "grave"), (0xC9, 0x45, "acute"), (0xCA, 0x45, "circumflex"),
    (0xCB, 0x45, "diaeresis"),
    (0xCC, 0x49, "grave"), (0xCD, 0x49, "acute"), (0xCE, 0x49, "circumflex"),
    (0xCF, 0x49, "diaeresis"),
    (0xD1, 0x4E, "tilde"),
    (0xD2, 0x4F, "grave"), (0xD3, 0x4F, "acute"), (0xD4, 0x4F, "circumflex"),
    (0xD5, 0x4F, "tilde"), (0xD6, 0x4F, "diaeresis"),
    (0xD9, 0x55, "grave"), (0xDA, 0x55, "acute"), (0xDB, 0x55, "circumflex"),
    (0xDC, 0x55, "diaeresis"),
    (0xDD, 0x59, "acute"),
    (0xE0, 0x61, "grave"), (0xE1, 0x61, "acute"), (0xE2, 0x61, "circumflex"),
    (0xE3, 0x61, "tilde"), (0xE4, 0x61, "diaeresis"), (0xE5, 0x61, "ring"),
    (0xE7, 0x63, "cedilla"),
    (0xE8, 0x65, "grave"), (0xE9, 0x65, "acute"), (0xEA, 0x65, "circumflex"),
    (0xEB, 0x65, "diaeresis"),
    (0xEC, 0x69, "grave"), (0xED, 0x69, "acute"), (0xEE, 0x69, "circumflex"),
    (0xEF, 0x69, "diaeresis"),
    (0xF1, 0x6E, "tilde"),
    (0xF2, 0x6F, "grave"), (0xF3, 0x6F, "acute"), (0xF4, 0x6F, "circumflex"),
    (0xF5, 0x6F, "tilde"), (0xF6, 0x6F, "diaeresis"),
    (0xF9, 0x75, "grave"), (0xFA, 0x75, "acute"), (0xFB, 0x75, "circumflex"),
    (0xFC, 0x75, "diaeresis"),
    (0xFD, 0x79, "acute"), (0xFF, 0x79, "diaeresis"),
]


def _accented_glyphs() -> list[Glyph]:
    out: list[Glyph] = []
    for cp, base_cp, mark in ACCENTED:
        base = BASE[base_cp]
        g = Glyph("uni%04X" % cp, advance=base.advance, unicode=cp,
                  note=f"{chr(cp)}：latin-ext-001")
        if base_cp in (0x69, 0x6A):        # i / j：底字母的点被记号替代
            g.vbar(320 if base_cp == 0x69 else 360,
                   -40 if base_cp == 0x6A else 0,
                   500, W_MAIN)
            x0, y0, x1, y1 = bbox(base)
            cx = (x0 + x1) / 2.0
            cy = MARK_Y_DOT
        elif mark == "cedilla":
            clone_parts(g, base)
            x0, y0, x1, y1 = bbox(base)
            cx = (x0 + x1) / 2.0
            cy = MARK_Y_BELOW
        else:
            clone_parts(g, base)
            x0, y0, x1, y1 = bbox(base)
            cx = (x0 + x1) / 2.0
            cy = _mark_center(base)
        if mark == "cedilla":
            mark_cedilla(g, cx, cy)
        else:
            MARKS[mark](g, cx, cy)
        out.append(g)
    return out


# ------------------------------------------------------- 特殊拉丁字母（密排 / 加笔）
def _ligature_glyphs() -> list[Glyph]:
    out: list[Glyph] = []

    # Æ / æ —— 第二个字母横向缩放后叠到第一个的右侧
    # 缩放系数不能压到 0.8：第二个字母的内白腔高会被压到 24 以下（黑砖门禁 FAIL）
    for cp, first_cp, second_cp, adv in ((0xC6, 0x41, 0x45, 900),
                                          (0xE6, 0x61, 0x65, 860)):
        first, second = BASE[first_cp], BASE[second_cp]
        g = Glyph("uni%04X" % cp, advance=adv, unicode=cp,
                  note=f"{chr(cp)}：latin-ext-001")
        clone_parts(g, first)
        fx0, fy0, fx1, fy1 = bbox(first)
        sx0, sy0, sx1, sy1 = bbox(second)
        scale = 1.0
        dx = (fx1 - 120) - sx0 * scale
        clone_parts(g, second, dx=dx, sx=scale)
        out.append(g)

    # Ð / ð —— D + 一条穿过左部的横
    for cp, base_cp in ((0xD0, 0x44), (0xF0, 0x64)):
        base = BASE[base_cp]
        g = Glyph("uni%04X" % cp, advance=base.advance, unicode=cp,
                  note=f"{chr(cp)}：latin-ext-001")
        clone_parts(g, base)
        x0, y0, x1, y1 = bbox(base)
        g.hbar(x0 - 90, x0 + 170, y0 + (y1 - y0) * 0.52, 84)
        out.append(g)

    # Ø / ø —— O + 一条斜杠
    for cp, base_cp in ((0xD8, 0x4F), (0xF8, 0x6F)):
        base = BASE[base_cp]
        g = Glyph("uni%04X" % cp, advance=base.advance, unicode=cp,
                  note=f"{chr(cp)}：latin-ext-001")
        clone_parts(g, base)
        x0, y0, x1, y1 = bbox(base)
        g.diag(x0 + 30, y0 - 40, x1 - 30, y1 + 40, 84)
        out.append(g)

    # Þ —— P + 下伸竖
    base = BASE[0x50]
    g = Glyph("uni%04X" % 0xDE, advance=base.advance, unicode=0xDE,
              note="Þ：latin-ext-001")
    clone_parts(g, base)
    x0, y0, x1, y1 = bbox(base)
    g.vbar(x0 + 60, -160, 0, 120)
    out.append(g)

    # ß —— 高瘦的 s（s 的原语纵向拉长 1.4×：实心黑体的 ß 就是长 s 的骨架）
    base = BASE[0x73]
    g = Glyph("uni%04X" % 0xDF, advance=base.advance, unicode=0xDF,
              note="ß：latin-ext-001")
    clone_parts(g, base, sy=1.4)
    out.append(g)

    return out


# ------------------------------------------------------- Latin-1 独立符号
def _latin1_symbols() -> list[Glyph]:
    out: list[Glyph] = []

    def sym(cp: int, adv: int, draw) -> None:
        g = Glyph("uni%04X" % cp, advance=adv, unicode=cp,
                  note=f"{chr(cp)}：latin-ext-001")
        draw(g)
        out.append(g)

    # ¡ —— 倒叹号
    def _exclam_inv(g):
        g.vbar(320, 350, 700, 120)
        disc(g, 320, 250, 55)
    sym(0xA1, ADV, _exclam_inv)

    # ¢ —— c + 穿过它的竖
    def _cent(g):
        clone_parts(g, BASE[0x63])
        g.vbar(320, -60, 560, 84)
    sym(0xA2, ADV, _cent)

    # £ —— 两段弧 + 横杠
    def _pound(g):
        g.diag(470, 620, 200, 360, 96)
        g.diag(200, 360, 470, 100, 96)
        g.hbar(110, 520, 360, 84)
        g.hbar(110, 520, 60, 84)
    sym(0xA3, ADV, _pound)

    # ¤ —— 四角小菱形
    def _currency(g):
        for cx, cy in ((200, 560), (440, 560), (200, 180), (440, 180)):
            g.poly([(cx, cy + 52), (cx + 46, cy), (cx, cy - 52), (cx - 46, cy)])
    sym(0xA4, ADV, _currency)

    # ¥ —— 两条斜 + 竖 + 两横
    def _yen(g):
        g.diag(120, 640, 320, 380, 96)
        g.diag(520, 640, 320, 380, 96)
        g.vbar(320, 0, 380, 96)
        g.hbar(140, 500, 300, 84)
        g.hbar(140, 500, 140, 84)
    sym(0xA5, ADV, _yen)

    # ¦ —— 断开的竖
    def _brokenbar(g):
        g.vbar(320, 340, 700, 96)
        g.vbar(320, 0, 240, 96)
    sym(0xA6, ADV, _brokenbar)

    # § —— 双 s
    def _section(g):
        g.diag(460, 600, 200, 430, 84)
        g.diag(200, 430, 460, 260, 84)
        g.diag(200, 260, 440, 90, 84)
    sym(0xA7, ADV, _section)

    # ¨ —— 分音符
    def _diaeresis_sym(g):
        disc(g, 272, 600, 40)
        disc(g, 368, 600, 40)
    sym(0xA8, ADV, _diaeresis_sym)

    # © —— 圈里一个 C
    def _copyright(g):
        ring_ell(g, 320, 330, 250, 250, 84)
        g.poly([(410, 400), (390, 415), (330, 395), (270, 350), (250, 300),
                (270, 240), (330, 205), (390, 195), (412, 210), (388, 235),
                (330, 245), (300, 275), (300, 330), (330, 360), (388, 350),
                (412, 336)])
    sym(0xA9, ADV, _copyright)

    # ª —— 小 a（近似：小圈 + 右侧竖）
    def _ordfeminine(g):
        ring_ell(g, 280, 460, 110, 110, 76)
        g.vbar(390, 350, 570, 76)
    sym(0xAA, ADV, _ordfeminine)

    # « —— 两个 <
    def _guillleft(g):
        g.diag(300, 560, 130, 360, 84)
        g.diag(130, 360, 300, 160, 84)
        g.diag(500, 560, 330, 360, 84)
        g.diag(330, 360, 500, 160, 84)
    sym(0xAB, ADV, _guillleft)

    # ¬ —— 横 + 短竖
    def _not(g):
        g.hbar(120, 520, 460, 96)
        g.vbar(520, 300, 460, 96)
    sym(0xAC, ADV, _not)

    # ® —— 圈里一个 R（近似：竖 + 碗 + 腿）
    def _registered(g):
        ring_ell(g, 320, 330, 250, 250, 84)
        g.vbar(250, 200, 460, 84)
        g.poly([(250, 460), (360, 460), (400, 430), (400, 390), (360, 370), (250, 370)])
        g.diag(340, 370, 420, 200, 84)
    sym(0xAE, ADV, _registered)

    # ¯ —— 长音符
    def _macron_sym(g):
        g.hbar(160, 480, 560, 84)
    sym(0xAF, ADV, _macron_sym)

    # ° —— 小圈
    def _degree(g):
        ring_ell(g, 320, 580, 100, 100, 72)
    sym(0xB0, ADV, _degree)

    # ± —— 加号 + 下横
    def _plusminus(g):
        g.hbar(110, 530, 400, 96)
        g.vbar(320, 190, 610, 96)
        g.hbar(110, 530, 100, 84)
    sym(0xB1, ADV, _plusminus)

    # ² ³ —— 上标数字（复用数字原语，缩 0.58 并抬高）
    def _sup(digit_cp: int, cp: int) -> None:
        def draw(g):
            clone_parts(g, BASE[digit_cp], dx=90, dy=390, sy=0.58)
        sym(cp, ADV, draw)

    _sup(0x32, 0xB2)
    _sup(0x33, 0xB3)

    # ´ —— 锐音符
    def _acute_sym(g):
        mark_acute(g, 320, 600)
    sym(0xB4, ADV, _acute_sym)

    # µ —— u + 左侧下伸
    def _micro(g):
        clone_parts(g, BASE[0x75])
        g.vbar(120, -160, 180, 96)
    sym(0xB5, ADV, _micro)

    # ¶ —— P + 左侧下伸
    def _pilcrow(g):
        clone_parts(g, BASE[0x50])
        g.vbar(180, -160, 700, 120)
    sym(0xB6, ADV, _pilcrow)

    # · —— 中点
    def _middot(g):
        disc(g, 320, 300, 55)
    sym(0xB7, ADV, _middot)

    # ¸ —— 下加符
    def _cedilla_sym(g):
        mark_cedilla(g, 320, 40)
    sym(0xB8, ADV, _cedilla_sym)

    # ¹ —— 上标 1
    def _sup1(g):
        clone_parts(g, BASE[0x31], dx=140, dy=390, sy=0.58)
    sym(0xB9, ADV, _sup1)

    # º —— 小 o
    def _ordmasculine(g):
        ring_ell(g, 320, 470, 110, 110, 76)
    sym(0xBA, ADV, _ordmasculine)

    # » —— 两个 >
    def _guillright(g):
        g.diag(340, 560, 510, 360, 84)
        g.diag(510, 360, 340, 160, 84)
        g.diag(140, 560, 310, 360, 84)
        g.diag(310, 360, 140, 160, 84)
    sym(0xBB, ADV, _guillright)

    # ¼ ½ ¾ —— 分数（分子左上 / 分母右下 / 中间斜杠）
    # 分子分母**必须分属两行**：同一行时两边的横画会互相封死白口（hcounters FAIL）
    def _fraction(num_cp: int, den_cp: int, cp: int) -> None:
        def draw(g):
            clone_parts(g, BASE[num_cp], dx=-170, dy=430, sx=0.62, sy=0.62)
            g.diag(280, 620, 120, 60, 84)
            clone_parts(g, BASE[den_cp], dx=170, dy=60, sx=0.62, sy=0.62)
        sym(cp, ADV, draw)

    _fraction(0x31, 0x34, 0xBC)
    _fraction(0x31, 0x32, 0xBD)
    _fraction(0x33, 0x34, 0xBE)

    # ¿ —— 倒问号
    def _question_inv(g):
        g.poly([(250, 700), (390, 700), (390, 560), (350, 520), (290, 480),
                (290, 420), (320, 380), (320, 330), (250, 330), (250, 440),
                (250, 480)])
        disc(g, 320, 250, 55)
    sym(0xBF, ADV, _question_inv)

    # × —— 叉
    def _times(g):
        g.diag(150, 520, 490, 180, 96)
        g.diag(490, 520, 150, 180, 96)
    sym(0xD7, ADV, _times)

    # ÷ —— 横 + 上下两点
    def _divide(g):
        g.hbar(110, 530, 340, 96)
        disc(g, 320, 470, 46)
        disc(g, 320, 210, 46)
    sym(0xF7, ADV, _divide)

    return out


# ------------------------------------------------------- General Punctuation
def _punctuation() -> list[Glyph]:
    out: list[Glyph] = []

    def sym(cp: int, adv: int, draw) -> None:
        g = Glyph("uni%04X" % cp, advance=adv, unicode=cp,
                  note=f"{chr(cp)}：latin-ext-001")
        draw(g)
        out.append(g)

    # 连字符族
    sym(0x2010, 320, lambda g: g.hbar(100, 340, 330, 84))          # ‐
    sym(0x2011, 320, lambda g: g.hbar(100, 340, 330, 84))          # ‑
    sym(0x2012, 400, lambda g: g.hbar(90, 390, 330, 84))          # ‒
    sym(0x2013, 520, lambda g: g.hbar(60, 460, 330, 96))          # –
    sym(0x2015, CJK_ADV, lambda g: g.hbar(60, 940, 330, 84))      # ―
    sym(0x2016, ADV, lambda g: (g.vbar(250, 0, 700, 84),
                                g.vbar(390, 0, 700, 84)))          # ‖
    sym(0x2017, ADV, lambda g: (g.hbar(100, 540, 40, 84),
                                g.hbar(100, 540, 170, 84)))         # ‗

    # 引号（左侧/右侧单双引号）
    def _quote(g, cx, flip):
        disc(g, cx, 610, 48)
        if flip:
            band2(g, (cx + 6, 570), (cx + 62, 440), 68)
        else:
            band2(g, (cx - 6, 570), (cx - 62, 440), 68)

    sym(0x2018, ADV, lambda g: _quote(g, 250, False))              # ‘
    sym(0x2019, ADV, lambda g: _quote(g, 250, True))               # ’
    sym(0x201A, ADV, lambda g: _quote(g, 250, False))              # ‚
    sym(0x201B, ADV, lambda g: _quote(g, 250, True))               # ‛
    sym(0x201C, ADV, lambda g: (_quote(g, 180, False),
                                _quote(g, 420, False)))             # “
    sym(0x201D, ADV, lambda g: (_quote(g, 180, True),
                                _quote(g, 420, True)))              # ”
    sym(0x201E, ADV, lambda g: (_quote(g, 180, False),
                                _quote(g, 420, False)))             # „
    sym(0x201F, ADV, lambda g: (_quote(g, 180, True),
                                _quote(g, 420, True)))              # ‟

    # 剑标
    sym(0x2020, ADV, lambda g: (g.vbar(320, 60, 700, 84),
                                g.hbar(160, 480, 520, 84)))         # †
    sym(0x2021, ADV, lambda g: (g.vbar(320, 60, 700, 84),
                                g.hbar(160, 480, 540, 84),
                                g.hbar(160, 480, 400, 84)))         # ‡
    # 项目符号 / 省略号
    sym(0x2022, ADV, lambda g: disc(g, 320, 330, 78))              # •
    sym(0x2026, CJK_ADV, lambda g: (disc(g, 200, 300, 78),
                                    disc(g, 500, 300, 78),
                                    disc(g, 800, 300, 78)))        # …
    # 千分号
    sym(0x2030, ADV, lambda g: (ring_ell(g, 180, 540, 90, 90, 72),
                                ring_ell(g, 460, 540, 90, 90, 72),
                                g.diag(520, 620, 120, 80, 84)))     # ‰
    # 撇号
    sym(0x2032, ADV, lambda g: g.diag(280, 700, 380, 480, 84))     # ′
    sym(0x2033, ADV, lambda g: (g.diag(220, 700, 320, 480, 84),
                                g.diag(380, 700, 480, 480, 84)))    # ″
    # 单尖括号
    sym(0x2039, ADV, lambda g: (g.diag(300, 560, 150, 360, 84),
                                g.diag(150, 360, 300, 160, 84)))    # ‹
    sym(0x203A, ADV, lambda g: (g.diag(340, 560, 490, 360, 84),
                                g.diag(490, 360, 340, 160, 84)))    # ›
    # 双叹号 / 疑问叹号
    sym(0x203C, ADV, lambda g: (g.vbar(230, 120, 620, 96),
                                g.vbar(410, 120, 620, 96),
                                disc(g, 230, 40, 50),
                                disc(g, 410, 40, 50)))               # ‼
    sym(0x203D, ADV, lambda g: (g.vbar(320, 40, 240, 96),
                                disc(g, 320, 40, 50)))               # ‽
    # 上划线
    sym(0x203E, ADV, lambda g: g.hbar(110, 530, 640, 84))          # ‾

    return out


# ------------------------------------------------------- 全角形式
# 全角码位 → ASCII 底字码位（既有 recipe 已有的全角标点不在此列）
FULLWIDTH: list[tuple[int, int]] = [
    (0xFF02, 0x22), (0xFF03, 0x23), (0xFF04, 0x24), (0xFF05, 0x25),
    (0xFF06, 0x26), (0xFF07, 0x27), (0xFF0A, 0x2A), (0xFF0B, 0x2B),
    (0xFF0D, 0x2D), (0xFF0E, 0x2E), (0xFF0F, 0x2F),
    (0xFF10, 0x30), (0xFF11, 0x31), (0xFF12, 0x32), (0xFF13, 0x33),
    (0xFF14, 0x34), (0xFF15, 0x35), (0xFF16, 0x36), (0xFF17, 0x37),
    (0xFF18, 0x38), (0xFF19, 0x39),
    (0xFF1C, 0x3C), (0xFF1D, 0x3D), (0xFF1E, 0x3E),
    (0xFF20, 0x40),
    (0xFF3B, 0x5B), (0xFF3C, 0x5C), (0xFF3D, 0x5D), (0xFF3E, 0x5E),
    (0xFF3F, 0x5F), (0xFF40, 0x60),
    (0xFF5B, 0x7B), (0xFF5C, 0x7C), (0xFF5D, 0x7D), (0xFF5E, 0x7E),
]
FULLWIDTH += [(0xFF21 + i, 0x41 + i) for i in range(26)]      # Ａ-Ｚ
FULLWIDTH += [(0xFF41 + i, 0x61 + i) for i in range(26)]      # ａ-ｚ
FULLWIDTH += [(0xFF5F, 0x5F), (0xFF60, 0x60), (0xFFE5, 0xA5)]


def _fullwidth_glyphs() -> list[Glyph]:
    out: list[Glyph] = []
    for cp, base_cp in FULLWIDTH:
        base = BASE.get(base_cp)
        if base is None:
            continue
        g = Glyph("uni%04X" % cp, advance=CJK_ADV, unicode=cp,
                  note=f"{chr(cp)}：latin-ext-001")
        x0, y0, x1, y1 = bbox(base)
        dx = CJK_ADV / 2.0 - (x0 + x1) / 2.0
        clone_parts(g, base, dx=dx)
        out.append(g)
    return out


def build() -> list[Glyph]:
    return (_accented_glyphs() + _ligature_glyphs() + _latin1_symbols()
            + _punctuation() + _fullwidth_glyphs())


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-latin-ext-001.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
