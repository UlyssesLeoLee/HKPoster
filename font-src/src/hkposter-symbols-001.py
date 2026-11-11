"""HK Poster Heavy —— 符号补齐层（symbols-001）。

补齐 v0.5 之后仍缺的 151 个符号类码位：

  * Latin-1 补充 3 个：U+00A0 不断行空格 / U+00AD 软连字符 / U+00FE thorn
  * General Punctuation 84 个（U+2000–U+206F 里未被其它层占用的）
  * CJK Symbols & Punctuation 57 个（U+3000–U+303F 里未被其它层占用的）
  * Fullwidth Currency 7 个（U+FFE0–U+FFE6）

设计原则
--------
1. **不描轮廓**：全部由笔画原语（hbar / vbar / diag / dot / ring / poly）拼出。
2. **空格与格式控制符不画东西**：Unicode 类别 Zs / Zl / Zp / Cf 的字形**没有墨**，
   只给 advance —— 这是它们本来的样子。`check_glyphs` 的「空字形」判据对
   这几类放行（见该脚本的 `is_blank_kind`）。
3. **全角符号按 CJK 版面**：advance 1000，字面 x 60..940、y 0..820，
   笔画权重 96 / 92 / 84（与横排标点同档）。
4. **拉丁侧符号按拉丁版面**：advance 按语义定（240 / 320 / 640 / 1000），
   笔画权重 96 / 84。
5. 每个字形的 note 写成「`<字符>`：`<说明>`」—— 这样 `check_charset` 才会
   拿 note 的首字跟 unicode 对撞（部件式 note 会被静默跳过）。

运行：python font-src/src/hkposter-symbols-001.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, ellipse_points, write_ufo  # noqa: E402

# ---- 冻结笔画权重（标点档：主 96 / 次 92 / 细 84）----
W_MAIN = 96
W_SECOND = 92
W_THIN = 84

# ---- 版面 ----
CJK_ADV = 1000
BODY_L, BODY_R = 60, 940
BODY_B, BODY_T = 0, 820
LAT_ADV = 640

# 拉丁侧的基线 / x 高 / 大写顶线（与 latin / latin-lower 同口径）
BASE_Y = 0
X_TOP = 500
CAP_TOP = 716


# --------------------------------------------------------------------------
# 几何工具
# --------------------------------------------------------------------------
def disc(glyph: Glyph, cx: float, cy: float, r: float, count: int = 16) -> None:
    """实心圆点（正 16 边形近似）。"""
    glyph.poly(ellipse_points(cx, cy, r, r, count=count))


def ellipse_ring(glyph: Glyph, cx: float, cy: float, rx: float, ry: float,
                  thick: float, count: int = 24) -> None:
    """椭圆环（圈）。"""
    glyph.ring(ellipse_points(cx, cy, rx, ry, count=count),
               ellipse_points(cx, cy, rx - thick, ry - thick, count=count))


def band(glyph: Glyph, cx: float, cy: float, rx_out: float, ry_out: float,
         rx_in: float, ry_in: float, th0: float, th1: float,
         steps: int = 16) -> None:
    """椭圆环带的一段（开口弧），角度制，0°=+x、90°=+y。"""
    outer: list[tuple[float, float]] = []
    inner: list[tuple[float, float]] = []
    for index in range(steps + 1):
        theta = math.radians(th0 + (th1 - th0) * index / steps)
        outer.append((cx + rx_out * math.cos(theta), cy + ry_out * math.sin(theta)))
        inner.append((cx + rx_in * math.cos(theta), cy + ry_in * math.sin(theta)))
    glyph.poly(outer + list(reversed(inner)))


def wedge(glyph: Glyph, start: tuple[float, float], end: tuple[float, float],
          w_start: float, w_end: float) -> None:
    """两端宽度不同的锥形笔画：中心线 start→end，宽度垂直于中心线。"""
    x0, y0 = start
    x1, y1 = end
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy)
    if length < 1e-9:
        return
    ux, uy = dx / length, dy / length
    px, py = -uy, ux
    glyph.poly([
        (x0 + px * w_start / 2, y0 + py * w_start / 2),
        (x1 + px * w_end / 2, y1 + py * w_end / 2),
        (x1 - px * w_end / 2, y1 - py * w_end / 2),
        (x0 - px * w_start / 2, y0 - py * w_start / 2),
    ])


def wave(glyph: Glyph, x0: float, x1: float, y_mid: float, amp: float,
         weight: float, steps: int = 24, phase: float = 0.2) -> None:
    """正弦波带（上缘 + 下缘闭合成一个简单多边形）。"""
    top: list[tuple[float, float]] = []
    bottom: list[tuple[float, float]] = []
    for index in range(steps + 1):
        t = index / steps
        x = x0 + (x1 - x0) * t
        y = y_mid + amp * math.cos(2 * math.pi * (t - phase))
        top.append((x, y + weight / 2))
        bottom.append((x, y - weight / 2))
    glyph.poly(top + list(reversed(bottom)))


def prime(glyph: Glyph, x: float, y0: float, y1: float, reverse: bool = False,
          weight: int = W_THIN) -> None:
    """撇号 / 撇号类记号（一条短斜笔）。"""
    if reverse:
        wedge(glyph, (x + 40, y1), (x - 40, y0), weight, weight)
    else:
        wedge(glyph, (x - 40, y1), (x + 40, y0), weight, weight)


def aster(glyph: Glyph, cx: float, cy: float, r: float, weight: int = W_THIN,
          arms: int = 3) -> None:
    """星号：arms 条直径方向的短笔（3 条 = 六角星）。"""
    for k in range(arms):
        theta = math.pi * k / arms
        dx, dy = math.cos(theta) * r, math.sin(theta) * r
        wedge(glyph, (cx - dx, cy - dy), (cx + dx, cy + dy), weight, weight)


# --------------------------------------------------------------------------
# 1. 空格与格式控制符（无墨，只给 advance）
# --------------------------------------------------------------------------
BLANK_GLYPHS: list[tuple[int, int, str]] = [
    (0x00A0, 640, "U+00A0 不断行空格"),
    (0x00AD, 640, "U+00AD 软连字符（默认不显示）"),
    (0x2000, 500, "U+2000 EN QUAD（半字宽空格）"),
    (0x2001, 1000, "U+2001 EM QUAD（字宽空格）"),
    (0x2002, 500, "U+2002 EN SPACE（半字宽空格）"),
    (0x2003, 1000, "U+2003 EM SPACE（字宽空格）"),
    (0x2004, 333, "U+2004 三分之一字宽空格"),
    (0x2005, 250, "U+2005 四分之一字宽空格"),
    (0x2006, 167, "U+2006 六分之一字宽空格"),
    (0x2007, 500, "U+2007 数字宽空格"),
    (0x2008, 333, "U+2008 标点宽空格"),
    (0x2009, 167, "U+2009 细空格"),
    (0x200A, 100, "U+200A 发丝空格"),
    (0x200B, 0, "U+200B 零宽空格"),
    (0x200C, 0, "U+200C 零宽不连字"),
    (0x200D, 0, "U+200D 零宽连字"),
    (0x200E, 0, "U+200E 从左到右标记"),
    (0x200F, 0, "U+200F 从右到左标记"),
    (0x202A, 0, "U+202A 从左到右嵌入"),
    (0x202B, 0, "U+202B 从右到左嵌入"),
    (0x202C, 0, "U+202C 弹出方向性格式"),
    (0x202D, 0, "U+202D 从左到右覆盖"),
    (0x202E, 0, "U+202E 从右到左覆盖"),
    (0x202F, 200, "U+202F 窄不断行空格"),
    (0x205F, 333, "U+205F 中等数学空格"),
    (0x2060, 0, "U+2060 词连接符"),
    (0x2061, 0, "U+2061 函数应用"),
    (0x2062, 0, "U+2062 不可见乘号"),
    (0x2063, 0, "U+2063 不可见分隔符"),
    (0x2064, 0, "U+2064 不可见加号"),
    (0x2065, 0, "U+2065 保留字符"),
    (0x2066, 0, "U+2066 从左到右隔离"),
    (0x2067, 0, "U+2067 从右到左隔离"),
    (0x2068, 0, "U+2068 首强隔离"),
    (0x2069, 0, "U+2069 弹出方向性隔离"),
    (0x206A, 0, "U+206A 禁止对称交换"),
    (0x206B, 0, "U+206B 激活对称交换"),
    (0x206C, 0, "U+206C 禁止阿拉伯文整形"),
    (0x206D, 0, "U+206D 激活阿拉伯文整形"),
    (0x206E, 0, "U+206E 国别数字形"),
    (0x206F, 0, "U+206F 名义数字形"),
    (0x3000, 1000, "U+3000 表意文字空格"),
]


def blank_glyphs() -> list[Glyph]:
    out: list[Glyph] = []
    for cp, adv, note in BLANK_GLYPHS:
        out.append(Glyph("uni%04X" % cp, advance=adv, unicode=cp, note=note))
    return out


# --------------------------------------------------------------------------
# 2. Latin-1 补充：thorn
# --------------------------------------------------------------------------
def thorn() -> Glyph:
    """þ U+00FE 拉丁小写 thorn：左竖（带升部）+ 右侧碗。"""
    g = Glyph("uni00FE", advance=LAT_ADV, unicode=0x00FE, note="þ：拉丁小写 thorn")
    g.vbar(240, 0, CAP_TOP, weight=W_MAIN)
    band(g, 280, 250, 150, 250, 84, 184, 90, 270, steps=16)
    return g


# --------------------------------------------------------------------------
# 3. General Punctuation 里可见的 45 个
# --------------------------------------------------------------------------
def general_punctuation() -> list[Glyph]:
    out: list[Glyph] = []

    def sym(cp: int, adv: int, draw, desc: str) -> None:
        g = Glyph("uni%04X" % cp, advance=adv, unicode=cp,
                  note="%s：%s" % (chr(cp), desc))
        draw(g)
        out.append(g)

    # ---- 项目符号 / 引导点 ----
    def _tri_bullet(g):
        g.poly([(230, 470), (410, 470), (320, 260)])
    sym(0x2023, LAT_ADV, _tri_bullet, "三角项目符号")

    def _one_dot(g):
        disc(g, 320, 300, 78)
    sym(0x2024, LAT_ADV, _one_dot, "单点引导符")

    def _two_dot(g):
        disc(g, 230, 300, 78)
        disc(g, 410, 300, 78)
    sym(0x2025, LAT_ADV, _two_dot, "双点引导符")

    def _hyphenation(g):
        g.hbar(80, 240, 520, weight=W_THIN)
    sym(0x2027, 320, _hyphenation, "断字点")

    def _line_sep(g):
        g.hbar(60, 940, 410, weight=W_THIN)
    sym(0x2028, 1000, _line_sep, "行分隔符")

    def _para_sep(g):
        g.hbar(60, 940, 410, weight=W_MAIN)
    sym(0x2029, 1000, _para_sep, "段分隔符")

    # ---- 撇号族 ----
    def _per_10k(g):
        disc(g, 190, 560, 62)
        disc(g, 370, 560, 62)
        disc(g, 130, 250, 62)
        wedge(g, (430, 680), (180, 60), W_THIN, W_THIN)
        wedge(g, (500, 680), (250, 60), W_THIN, W_THIN)
    sym(0x2031, LAT_ADV, _per_10k, "万分之一符号")

    def _triple_prime(g):
        for x in (170, 320, 470):
            prime(g, x, 470, 690)
    sym(0x2034, LAT_ADV, _triple_prime, "三重撇号")

    def _rev_prime(g):
        prime(g, 320, 470, 690, reverse=True)
    sym(0x2035, 320, _rev_prime, "反撇号")

    def _rev_double_prime(g):
        prime(g, 230, 470, 690, reverse=True)
        prime(g, 430, 470, 690, reverse=True)
    sym(0x2036, LAT_ADV, _rev_double_prime, "反双撇号")

    def _rev_triple_prime(g):
        for x in (170, 320, 470):
            prime(g, x, 470, 690, reverse=True)
    sym(0x2037, LAT_ADV, _rev_triple_prime, "反三重撇号")

    def _caret(g):
        wedge(g, (160, 470), (320, 690), W_THIN, W_THIN)
        wedge(g, (320, 690), (480, 470), W_THIN, W_THIN)
    sym(0x2038, LAT_ADV, _caret, "插入符号")

    # ---- 参照号 ※（X + 四个点）----
    def _reference(g):
        wedge(g, (250, 640), (750, 180), W_MAIN, W_MAIN)
        wedge(g, (750, 640), (250, 180), W_MAIN, W_MAIN)
        disc(g, 500, 600, 44)
        disc(g, 500, 220, 44)
        disc(g, 250, 410, 44)
        disc(g, 750, 410, 44)
    sym(0x203B, CJK_ADV, _reference, "参照号")

    # ---- 下划连字符类 ----
    def _undertie(g):
        g.hbar(60, 480, -30, weight=W_THIN)
        wedge(g, (480, -30), (520, 90), W_THIN, W_THIN)
    sym(0x203F, LAT_ADV, _undertie, "下划连字符")

    def _char_tie(g):
        g.hbar(140, 500, -30, weight=W_THIN)
        wedge(g, (140, -30), (180, 90), W_THIN, W_THIN)
        wedge(g, (500, -30), (540, 90), W_THIN, W_THIN)
    sym(0x2040, LAT_ADV, _char_tie, "字符连字符")

    def _caret_insert(g):
        wedge(g, (320, 120), (320, 300), W_THIN, W_THIN)
        wedge(g, (250, 220), (320, 300), W_THIN, W_THIN)
        wedge(g, (390, 220), (320, 300), W_THIN, W_THIN)
    sym(0x2041, LAT_ADV, _caret_insert, "插入符号插入点")

    # ---- 星号族 ----
    def _asterism(g):
        aster(g, 320, 620, 110)
        aster(g, 220, 300, 110)
        aster(g, 420, 300, 110)
    sym(0x2042, LAT_ADV, _asterism, "星号组")

    def _hyphen_bullet(g):
        g.hbar(120, 320, 330, weight=W_THIN)
        disc(g, 470, 330, 60)
    sym(0x2043, LAT_ADV, _hyphen_bullet, "连字符项目符号")

    def _fraction_slash(g):
        wedge(g, (200, 700), (460, 60), W_MAIN, W_MAIN)
    sym(0x2044, LAT_ADV, _fraction_slash, "分数斜线")

    def _bracket_quill_left(g):
        g.hbar(150, 400, 620, weight=W_THIN)
        g.vbar(150, 60, 620, weight=W_THIN)
        wedge(g, (400, 620), (500, 700), W_THIN, W_THIN)
    sym(0x2045, LAT_ADV, _bracket_quill_left, "带羽饰左方括号")

    def _bracket_quill_right(g):
        g.hbar(240, 490, 620, weight=W_THIN)
        g.vbar(490, 60, 620, weight=W_THIN)
        wedge(g, (240, 620), (140, 700), W_THIN, W_THIN)
    sym(0x2046, LAT_ADV, _bracket_quill_right, "带羽饰右方括号")

    # ---- 双问号 / 问叹号族 ----
    def _double_question(g):
        for cy in (560, 220):
            band(g, 320, cy, 110, 110, 46, 46, 150, -80, steps=14)
            g.vbar(330, cy - 110, cy - 60, weight=W_THIN)
            disc(g, 320, cy - 150, 46)
    sym(0x2047, LAT_ADV, _double_question, "双问号")

    def _question_exclam(g):
        band(g, 320, 600, 120, 120, 50, 50, 150, -80, steps=14)
        g.vbar(330, 420, 480, weight=W_THIN)
        disc(g, 320, 360, 50)
        g.vbar(320, 120, 260, weight=W_THIN)
    sym(0x2048, LAT_ADV, _question_exclam, "问叹号")

    def _exclam_question(g):
        g.vbar(320, 560, 700, weight=W_THIN)
        disc(g, 320, 500, 50)
        band(g, 320, 250, 120, 120, 50, 50, 150, -80, steps=14)
        g.vbar(330, 70, 130, weight=W_THIN)
        disc(g, 320, 20, 50)
    sym(0x2049, LAT_ADV, _exclam_question, "叹问号")

    # ---- 提尔干注记 et ----
    def _tironian(g):
        g.hbar(150, 520, 640, weight=W_MAIN)
        wedge(g, (360, 640), (220, 120), W_MAIN, W_THIN)
    sym(0x204A, LAT_ADV, _tironian, "提尔干 et 记号")

    def _rev_pilcrow(g):
        g.poly([(200, 0), (200, 700), (480, 700), (480, 380), (300, 380),
                (300, 0)])
        disc(g, 240, 560, 56)
    sym(0x204B, LAT_ADV, _rev_pilcrow, "反pilcrow记号")

    def _black_left(g):
        g.poly([(430, 620), (170, 400), (430, 180)])
    sym(0x204C, LAT_ADV, _black_left, "实心左向箭头")

    def _black_right(g):
        g.poly([(210, 620), (470, 400), (210, 180)])
    sym(0x204D, LAT_ADV, _black_right, "实心右向箭头")

    def _low_asterisk(g):
        aster(g, 320, 170, 110)
    sym(0x204E, LAT_ADV, _low_asterisk, "低位星号")

    def _rev_semicolon(g):
        disc(g, 320, 120, 50)
        wedge(g, (320, 400), (260, 260), W_THIN, W_THIN)
    sym(0x204F, LAT_ADV, _rev_semicolon, "反分号")

    def _close_up(g):
        g.poly([(150, 120), (490, 120), (490, 520), (150, 520)])
        g.poly([(210, 180), (430, 180), (430, 460), (210, 460)])
        g.poly([(250, 220), (390, 220), (390, 420), (250, 420)])
    sym(0x2050, LAT_ADV, _close_up, "关闭记号")

    def _two_asterisks(g):
        aster(g, 320, 560, 105)
        aster(g, 320, 190, 105)
    sym(0x2051, LAT_ADV, _two_asterisks, "垂直双星号")

    def _commercial_minus(g):
        g.hbar(150, 490, 330, weight=W_MAIN)
    sym(0x2052, LAT_ADV, _commercial_minus, "商业减号")

    def _swung_dash(g):
        wave(g, 120, 520, 330, 58, W_THIN, steps=20)
    sym(0x2053, LAT_ADV, _swung_dash, "摆动破折号")

    def _inv_undertie(g):
        g.hbar(60, 480, 560, weight=W_THIN)
        wedge(g, (480, 560), (520, 440), W_THIN, W_THIN)
    sym(0x2054, LAT_ADV, _inv_undertie, "反下划连字符")

    def _flower(g):
        for k in range(6):
            theta = math.pi * 2 * k / 6
            disc(g, 320 + math.cos(theta) * 130, 330 + math.sin(theta) * 130, 52)
        disc(g, 320, 330, 56)
    sym(0x2055, LAT_ADV, _flower, "花形标点")

    # ---- 点阵类 ----
    def _three_dot(g):
        disc(g, 240, 420, 52)
        disc(g, 400, 420, 52)
        disc(g, 320, 200, 52)
    sym(0x2056, LAT_ADV, _three_dot, "三点标点")

    def _quad_prime(g):
        for x in (150, 270, 390, 510):
            prime(g, x, 470, 690)
    sym(0x2057, LAT_ADV, _quad_prime, "四重撇号")

    def _four_dot(g):
        disc(g, 240, 420, 52)
        disc(g, 400, 420, 52)
        disc(g, 240, 200, 52)
        disc(g, 400, 200, 52)
    sym(0x2058, LAT_ADV, _four_dot, "四点标点")

    def _five_dot(g):
        disc(g, 240, 440, 52)
        disc(g, 400, 440, 52)
        disc(g, 240, 220, 52)
        disc(g, 400, 220, 52)
        disc(g, 320, 330, 52)
    sym(0x2059, LAT_ADV, _five_dot, "五点标点")

    def _two_dot_punct(g):
        disc(g, 320, 440, 52)
        disc(g, 320, 220, 52)
    sym(0x205A, LAT_ADV, _two_dot_punct, "两点标点")

    def _four_dot_mark(g):
        disc(g, 320, 470, 52)
        disc(g, 320, 190, 52)
        disc(g, 200, 330, 52)
        disc(g, 440, 330, 52)
    sym(0x205B, LAT_ADV, _four_dot_mark, "四点记号")

    def _dotted_cross(g):
        wedge(g, (200, 620), (440, 180), W_THIN, W_THIN)
        wedge(g, (440, 620), (200, 180), W_THIN, W_THIN)
        disc(g, 320, 400, 48)
    sym(0x205C, LAT_ADV, _dotted_cross, "点状十字")

    def _tricolon(g):
        disc(g, 320, 520, 50)
        disc(g, 320, 330, 50)
        disc(g, 320, 140, 50)
    sym(0x205D, LAT_ADV, _tricolon, "三点冒号")

    def _vert_four_dots(g):
        for y in (560, 400, 240, 80):
            disc(g, 320, y, 50)
    sym(0x205E, LAT_ADV, _vert_four_dots, "竖排四点")

    return out


# --------------------------------------------------------------------------
# 4. CJK Symbols & Punctuation 里的 56 个可见字形（全角版面）
# --------------------------------------------------------------------------
def cjk_symbols() -> list[Glyph]:
    out: list[Glyph] = []

    def sym(cp: int, draw, desc: str) -> None:
        g = Glyph("uni%04X" % cp, advance=CJK_ADV, unicode=cp,
                  note="%s：%s" % (chr(cp), desc))
        draw(g)
        out.append(g)

    # ---- 〃 〄 々 〆 〇 ----
    def _ditto(g):
        wedge(g, (420, 700), (330, 320), W_THIN, W_THIN)
        wedge(g, (660, 700), (570, 320), W_THIN, W_THIN)
    sym(0x3003, _ditto, "同上记号")

    def _jis(g):
        g.vbar(320, 0, 760, weight=W_MAIN)
        g.hbar(320, 760, 760, weight=W_MAIN)
        g.vbar(660, 260, 760, weight=W_SECOND)
        g.hbar(320, 660, 300, weight=W_SECOND)
    sym(0x3004, _jis, "日本工业标准记号")

    def _iteration(g):
        g.hbar(300, 700, 640, weight=W_THIN)
        wedge(g, (700, 640), (300, 100), W_MAIN, W_THIN)
        wedge(g, (460, 560), (280, 420), W_THIN, W_THIN)
    sym(0x3005, _iteration, "表意反复号")

    def _closing(g):
        wedge(g, (700, 780), (240, 60), W_MAIN, W_THIN)
        wedge(g, (240, 60), (330, 170), W_THIN, W_THIN)
    sym(0x3006, _closing, "表意结束记号")

    def _ideographic_zero(g):
        ellipse_ring(g, 500, 410, 320, 320, 84, count=28)
    sym(0x3007, _ideographic_zero, "表意数字零")

    # ---- 角括号 / 双角括号 ----
    def _angle_left(g):
        wedge(g, (640, 740), (300, 410), W_MAIN, W_MAIN)
        wedge(g, (300, 410), (640, 80), W_MAIN, W_MAIN)
    sym(0x3008, _angle_left, "左角括号")

    def _angle_right(g):
        wedge(g, (360, 740), (700, 410), W_MAIN, W_MAIN)
        wedge(g, (700, 410), (360, 80), W_MAIN, W_MAIN)
    sym(0x3009, _angle_right, "右角括号")

    def _dangle_left(g):
        wedge(g, (600, 740), (280, 410), W_MAIN, W_MAIN)
        wedge(g, (280, 410), (600, 80), W_MAIN, W_MAIN)
        wedge(g, (860, 740), (620, 410), W_MAIN, W_MAIN)
        wedge(g, (620, 410), (860, 80), W_MAIN, W_MAIN)
    sym(0x300A, _dangle_left, "左双角括号")

    def _dangle_right(g):
        wedge(g, (400, 740), (720, 410), W_MAIN, W_MAIN)
        wedge(g, (720, 410), (400, 80), W_MAIN, W_MAIN)
        wedge(g, (140, 740), (280, 410), W_MAIN, W_MAIN)
        wedge(g, (280, 410), (140, 80), W_MAIN, W_MAIN)
    sym(0x300B, _dangle_right, "右双角括号")

    # ---- 『 』：白直角引号（双线角）----
    def _white_corner_left(g):
        g.vbar(780, 60, 760, weight=W_MAIN)
        g.hbar(780, 900, 760, weight=W_MAIN)
        g.vbar(660, 170, 650, weight=W_THIN)
        g.hbar(660, 840, 650, weight=W_THIN)
    sym(0x300E, _white_corner_left, "左白直角引号")

    def _white_corner_right(g):
        g.vbar(220, 60, 760, weight=W_MAIN)
        g.hbar(100, 220, 760, weight=W_MAIN)
        g.vbar(340, 170, 650, weight=W_THIN)
        g.hbar(160, 340, 650, weight=W_THIN)
    sym(0x300F, _white_corner_right, "右白直角引号")

    # ---- 〒 〓 ----
    def _postal(g):
        g.hbar(180, 820, 660, weight=W_MAIN)
        g.hbar(240, 760, 470, weight=W_SECOND)
        g.vbar(500, 40, 660, weight=W_MAIN)
    sym(0x3012, _postal, "邮政记号")

    def _geta(g):
        g.vbar(220, 0, 700, weight=W_MAIN)
        g.hbar(220, 460, 700, weight=W_MAIN)
        g.vbar(620, 0, 700, weight=W_MAIN)
        g.hbar(620, 860, 700, weight=W_MAIN)
    sym(0x3013, _geta, "棋盘记号")

    # ---- 〔 〕 甲鱼括号 ----
    def _tortoise_left(g):
        g.poly([(300, 780), (420, 700), (420, 120), (300, 40)])
        g.poly([(300, 700), (360, 650), (360, 170), (300, 120)])
    sym(0x3014, _tortoise_left, "左甲鱼括号")

    def _tortoise_right(g):
        g.poly([(700, 780), (580, 700), (580, 120), (700, 40)])
        g.poly([(700, 700), (640, 650), (640, 170), (700, 120)])
    sym(0x3015, _tortoise_right, "右甲鱼括号")

    # ---- 〖 〗 白甲鱼括号（空心）----
    def _wlenticular_left(g):
        band(g, 520, 410, 260, 390, 170, 300, 100, 260, steps=18)
        g.hbar(430, 520, 700, weight=W_THIN)
        g.hbar(430, 520, 120, weight=W_THIN)
    sym(0x3016, _wlenticular_left, "左空白龟甲括号")

    def _wlenticular_right(g):
        band(g, 480, 410, 260, 390, 170, 300, -80, 80, steps=18)
        g.hbar(480, 570, 700, weight=W_THIN)
        g.hbar(480, 570, 120, weight=W_THIN)
    sym(0x3017, _wlenticular_right, "右空白龟甲括号")

    # ---- 〘 〙 白甲鱼括号 ----
    def _wtortoise_left(g):
        g.poly([(300, 760), (400, 690), (400, 700), (380, 690),
                (380, 150), (400, 140), (400, 130), (300, 60)])
        g.poly([(300, 700), (350, 665), (350, 150), (300, 115)])
    sym(0x3018, _wtortoise_left, "左空白龟甲括号（双线）")

    def _wtortoise_right(g):
        g.poly([(700, 760), (600, 690), (600, 700), (620, 690),
                (620, 150), (600, 140), (600, 130), (700, 60)])
        g.poly([(700, 700), (650, 665), (650, 150), (700, 115)])
    sym(0x3019, _wtortoise_right, "右空白龟甲括号（双线）")

    # ---- 〚 〛 白方括号 ----
    def _wsquare_left(g):
        g.hbar(300, 420, 700, weight=W_THIN)
        g.vbar(300, 120, 700, weight=W_THIN)
        g.hbar(420, 500, 620, weight=W_THIN)
        g.vbar(500, 200, 620, weight=W_THIN)
    sym(0x301A, _wsquare_left, "左白方括号")

    def _wsquare_right(g):
        g.hbar(580, 700, 700, weight=W_THIN)
        g.vbar(700, 120, 700, weight=W_THIN)
        g.hbar(500, 580, 620, weight=W_THIN)
        g.vbar(500, 200, 620, weight=W_THIN)
    sym(0x301B, _wsquare_right, "右白方括号")

    # ---- 〝 〞 〟 双撇号引号 ----
    def _rev_dprime(g):
        prime(g, 330, 560, 760, reverse=True)
        prime(g, 590, 560, 760, reverse=True)
    sym(0x301D, _rev_dprime, "反双撇号引号")

    def _dprime(g):
        prime(g, 330, 560, 760)
        prime(g, 590, 560, 760)
    sym(0x301E, _dprime, "双撇号引号")

    def _low_dprime(g):
        prime(g, 330, 120, 320)
        prime(g, 590, 120, 320)
    sym(0x301F, _low_dprime, "低双撇号引号")

    # ---- 〠 邮政记号脸 ----
    def _postal_face(g):
        ellipse_ring(g, 500, 380, 300, 300, 84, count=28)
        # 〒 的两条横画必须拉开：白口 ≥ 24（铁律 10）——
        # 470 与 390 之间只有 80，笔宽 84 → 白口 −4，横×横判 FAIL。
        g.hbar(360, 640, 500, weight=W_THIN)
        g.hbar(400, 600, 370, weight=W_THIN)
        g.vbar(500, 180, 500, weight=W_THIN)
        disc(g, 410, 250, 44)
        disc(g, 590, 250, 44)
    sym(0x3020, _postal_face, "邮政记号脸")

    # ---- 杭州数字 〡 〢 〣 〤 〥 ----
    def _hangzhou_strokes(n: int):
        def draw(g):
            gap = 760 / (n + 1)
            for k in range(n):
                x = 120 + gap * (k + 1)
                g.vbar(x, 120, 700, weight=W_MAIN)
        return draw

    for cp, n in ((0x3021, 1), (0x3022, 2), (0x3023, 3), (0x3024, 4), (0x3025, 5)):
        sym(cp, _hangzhou_strokes(n), "杭州数字 %d" % n)

    # ---- 杭州数字 6~9（借用汉字形）----
    def _six(g):
        g.hbar(280, 720, 640, weight=W_MAIN)
        wedge(g, (380, 560), (240, 140), W_MAIN, W_THIN)
        wedge(g, (620, 560), (760, 140), W_MAIN, W_THIN)
    sym(0x3026, _six, "杭州数字 6")

    def _seven(g):
        g.hbar(240, 760, 620, weight=W_MAIN)
        g.vbar(560, 60, 620, weight=W_MAIN)
        wedge(g, (560, 300), (700, 60), W_SECOND, W_THIN)
    sym(0x3027, _seven, "杭州数字 7")

    def _eight(g):
        wedge(g, (400, 660), (220, 100), W_MAIN, W_THIN)
        wedge(g, (600, 660), (780, 100), W_MAIN, W_THIN)
    sym(0x3028, _eight, "杭州数字 8")

    def _nine(g):
        wedge(g, (280, 740), (480, 480), W_MAIN, W_MAIN)
        g.hbar(360, 660, 480, weight=W_MAIN)
        g.vbar(660, 60, 480, weight=W_MAIN)
        wedge(g, (660, 240), (780, 80), W_SECOND, W_THIN)
    sym(0x3029, _nine, "杭州数字 9")

    # ---- 声调记号 〪 〫 〬 〭 ----
    def _level_tone(g):
        g.hbar(240, 760, 620, weight=W_MAIN)
    sym(0x302A, _level_tone, "平声记号")

    def _rising_tone(g):
        wedge(g, (300, 300), (700, 560), W_MAIN, W_MAIN)
    sym(0x302B, _rising_tone, "上声记号")

    def _departing_tone(g):
        wedge(g, (300, 560), (700, 300), W_MAIN, W_MAIN)
    sym(0x302C, _departing_tone, "去声记号")

    def _entering_tone(g):
        g.vbar(360, 120, 600, weight=W_MAIN)
        g.hbar(360, 660, 600, weight=W_MAIN)
    sym(0x302D, _entering_tone, "入声记号")

    def _hangul_dot(g):
        disc(g, 500, 410, 70)
    sym(0x302E, _hangul_dot, "谚文单点声调")

    def _hangul_double_dot(g):
        disc(g, 400, 410, 70)
        disc(g, 600, 410, 70)
    sym(0x302F, _hangul_double_dot, "谚文双点声调")

    # ---- 〰 波浪破折号 ----
    def _wavy_dash(g):
        wave(g, 120, 880, 410, 92, W_THIN, steps=28)
    sym(0x3030, _wavy_dash, "波浪破折号")

    # ---- 〱 〲 〳 〴 〵 竖排假名重复记号 ----
    def _vrepeat(g):
        g.vbar(360, 120, 700, weight=W_MAIN)
        g.vbar(640, 120, 700, weight=W_MAIN)
    sym(0x3031, _vrepeat, "竖排假名重复记号")

    def _vrepeat_voiced(g):
        g.vbar(300, 120, 700, weight=W_MAIN)
        g.vbar(560, 120, 700, weight=W_MAIN)
        g.hbar(700, 820, 620, weight=W_THIN)
    sym(0x3032, _vrepeat_voiced, "竖排假名浊音重复记号")

    def _vrepeat_upper(g):
        g.vbar(380, 380, 760, weight=W_MAIN)
    sym(0x3033, _vrepeat_upper, "竖排假名重复记号上半")

    def _vrepeat_voiced_upper(g):
        g.vbar(320, 380, 760, weight=W_MAIN)
        g.hbar(700, 820, 700, weight=W_THIN)
    sym(0x3034, _vrepeat_voiced_upper, "竖排假名浊音重复记号上半")

    def _vrepeat_lower(g):
        g.vbar(380, 60, 440, weight=W_MAIN)
    sym(0x3035, _vrepeat_lower, "竖排假名重复记号下半")

    # ---- ㊙ 圈邮政记号 ----
    def _circled_postal(g):
        ellipse_ring(g, 500, 410, 320, 320, 84, count=28)
        # 同上：〒 的两条横画要拉开 130 单位（白口 ≥ 24）。
        g.hbar(360, 640, 500, weight=W_THIN)
        g.hbar(400, 600, 370, weight=W_THIN)
        g.vbar(500, 220, 500, weight=W_THIN)
    sym(0x3036, _circled_postal, "圈邮政记号")

    # ---- ㍙ 电报换行分隔符 ----
    def _telegraph(g):
        g.poly([(200, 180), (800, 180), (800, 640), (200, 640)])
        g.poly([(280, 250), (720, 250), (720, 570), (280, 570)])
        wedge(g, (300, 250), (700, 570), W_THIN, W_THIN)
    sym(0x3037, _telegraph, "电报换行分隔符")

    # ---- 杭州数字 10 20 30 ----
    def _ten(g):
        g.hbar(220, 780, 520, weight=W_MAIN)
        g.vbar(500, 100, 720, weight=W_MAIN)
    sym(0x3038, _ten, "杭州数字 10")

    def _twenty(g):
        g.hbar(160, 840, 520, weight=W_MAIN)
        g.vbar(340, 120, 520, weight=W_MAIN)
        g.vbar(660, 120, 520, weight=W_MAIN)
    sym(0x3039, _twenty, "杭州数字 20")

    def _thirty(g):
        g.hbar(120, 880, 520, weight=W_MAIN)
        g.vbar(280, 120, 520, weight=W_MAIN)
        g.vbar(500, 120, 520, weight=W_MAIN)
        g.vbar(720, 120, 520, weight=W_MAIN)
    sym(0x303A, _thirty, "杭州数字 30")

    # ---- 〻 竖排表意反复号 ----
    def _viteration(g):
        g.vbar(370, 100, 720, weight=W_MAIN)
        g.vbar(630, 100, 720, weight=W_MAIN)
    sym(0x303B, _viteration, "竖排表意反复号")

    # ---- 〼 枡记号 ----
    def _masu(g):
        g.poly([(180, 120), (820, 120), (820, 700), (180, 700)])
        g.poly([(260, 190), (740, 190), (740, 630), (260, 630)])
        wedge(g, (260, 190), (740, 630), W_THIN, W_THIN)
        wedge(g, (740, 190), (260, 630), W_THIN, W_THIN)
    sym(0x303C, _masu, "枡记号")

    # ---- 〽 部分交替记号 ----
    def _part_alt(g):
        top: list[tuple[float, float]] = []
        bottom: list[tuple[float, float]] = []
        steps = 28
        for index in range(steps + 1):
            t = index / steps
            y = 60 + (700 - 60) * t
            x = 500 + 190 * math.cos(2 * math.pi * (t - 0.25))
            top.append((x, y + W_THIN / 2))
            bottom.append((x, y - W_THIN / 2))
        g.poly(top + list(reversed(bottom)))
    sym(0x303D, _part_alt, "部分交替记号")

    # ---- 〾 表意变化指标 ----
    def _variation(g):
        wedge(g, (420, 700), (280, 410), W_MAIN, W_MAIN)
        wedge(g, (280, 410), (420, 120), W_MAIN, W_MAIN)
        wedge(g, (620, 640), (520, 410), W_THIN, W_THIN)
        wedge(g, (520, 410), (620, 180), W_THIN, W_THIN)
    sym(0x303E, _variation, "表意变化指标")

    # ---- 〿 表意半填充空格 ----
    def _half_fill(g):
        g.poly([(160, 100), (840, 100), (840, 720), (160, 720)])
        g.poly([(240, 170), (760, 170), (760, 650), (240, 650)])
        g.poly([(240, 170), (500, 170), (500, 650), (240, 650)])
    sym(0x303F, _half_fill, "表意半填充空格")

    return out


# --------------------------------------------------------------------------
# 5. 全角货币符号 7 个
# --------------------------------------------------------------------------
def fullwidth_currency() -> list[Glyph]:
    out: list[Glyph] = []

    def sym(cp: int, draw, desc: str) -> None:
        g = Glyph("uni%04X" % cp, advance=CJK_ADV, unicode=cp,
                  note="%s：%s" % (chr(cp), desc))
        draw(g)
        out.append(g)

    def _cent(g):
        band(g, 480, 410, 240, 240, 150, 150, 40, 320, steps=20)
        g.vbar(500, 140, 680, weight=W_THIN)
    sym(0xFFE0, _cent, "全角分符号")

    def _pound(g):
        g.vbar(380, 120, 700, weight=W_MAIN)
        band(g, 380, 620, 130, 130, 62, 62, 0, 180, steps=14)
        g.hbar(220, 760, 300, weight=W_MAIN)
        g.hbar(200, 800, 80, weight=W_MAIN)
    sym(0xFFE1, _pound, "全角英镑符号")

    def _not(g):
        ellipse_ring(g, 500, 410, 220, 220, 84, count=24)
        wedge(g, (500, 190), (500, 630), W_THIN, W_THIN)
        wedge(g, (280, 410), (720, 410), W_THIN, W_THIN)
    sym(0xFFE2, _not, "全角货币记号")

    def _macron(g):
        g.hbar(160, 840, 560, weight=W_MAIN)
    sym(0xFFE3, _macron, "全角长音符")

    def _broken_bar(g):
        g.vbar(500, 420, 740, weight=W_MAIN)
        g.vbar(500, 100, 360, weight=W_MAIN)
    sym(0xFFE4, _broken_bar, "全角断竖线")

    def _yen(g):
        wedge(g, (280, 740), (500, 420), W_MAIN, W_MAIN)
        wedge(g, (720, 740), (500, 420), W_MAIN, W_MAIN)
        g.vbar(500, 80, 420, weight=W_MAIN)
        g.hbar(330, 670, 300, weight=W_THIN)
        g.hbar(330, 670, 200, weight=W_THIN)
    sym(0xFFE5, _yen, "全角日元符号")

    def _won(g):
        wedge(g, (250, 700), (400, 320), W_MAIN, W_MAIN)
        wedge(g, (400, 320), (550, 640), W_MAIN, W_MAIN)
        wedge(g, (550, 640), (700, 320), W_MAIN, W_MAIN)
        wedge(g, (700, 320), (790, 200), W_MAIN, W_THIN)
        g.hbar(200, 800, 300, weight=W_THIN)
    sym(0xFFE6, _won, "全角韩元符号")

    return out


# --------------------------------------------------------------------------
# 组装
# --------------------------------------------------------------------------
def build() -> list[Glyph]:
    """返回本层的全部字形（3 + 84 + 57 + 7 = 151）。"""
    glyphs: list[Glyph] = []
    glyphs.extend(blank_glyphs())
    glyphs.append(thorn())
    glyphs.extend(general_punctuation())
    glyphs.extend(cjk_symbols())
    glyphs.extend(fullwidth_currency())
    return glyphs


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-symbols-001.ufo"


if __name__ == "__main__":
    _target = target_ufo()
    _target.parent.mkdir(parents=True, exist_ok=True)
    write_ufo(_target, build())
    print("[recipe] 已写出 %s" % _target)
