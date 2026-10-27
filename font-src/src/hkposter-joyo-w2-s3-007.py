"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s3-007。

本批 24 字，笔画范围 10–13，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
* 字面框 x 60..940 / y 0..820，advance 1000（与 zh-HK 繁体同档，便于中英日混排）。
* 权重档：主 96 / 次 92 / 细 84 / 点 84。本批密度接近（10–13 画），
  拥挤处局部减重到 84（催 的隹、督 的目、湾 的弓、買/敗 的貝、黒 的田），
  密排内白以 check_stroke_gaps 的实测为准，横向叠画一律 ≥24 单位。
* 同批观感统一（docs/03 GLY-004）：同一部件在批内只写一套坐标，
  扌 / 亻 / 氵 / 糸 / 又 在批内复用；隹 有全高（推）与压缩（催）两档，
  压缩档只按比例缩放，笔画方向不变。
* 记号倾角分档（GLY-003 / GLY-004），不自造档位：
    丶  → -14（辶的点、氵中点、寸点、心点、灬右点、立/亦的点、豆の丷）
    短撇 →  26（氵的上点）
    丿  →  14（灬左点、爫左点）
    竖点 →   0（言的点、灬中两点、亦的点、接 的立顶点）
* 笔画角度不改：主笔（横竖撇捺提平捺）一律按标准骨架走向；
  斜切只用于点/短撇/记号（GLY-003）。
* 竖钩（扌 / 寸 / 可 / 弓 / 氏）用 poly 切角实现，是端点处理而非改角度。
* 竖排框（目 / 田）由 helper 按区域高度均分内白，避免逐字手算出错。
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, write_ufo  # noqa: E402

W_MAIN = 96
W_SEC = 92
W_THIN = 84
W_DOT = 84

X_L = 60          # 字面框左
X_R = 940         # 字面框右
Y_TOP = 820       # 字面框上
Y_BASE = 0        # 字面框下


# ---------------------------------------------------------------- 基础笔画

def hbar(g, x1, x2, y, w=W_MAIN):
    """横：中心线 y，墨迹 y±w/2，两端平切。"""
    g.hbar(x1, x2, y, weight=w)


def vbar(g, x, y1, y2, w=W_MAIN):
    """竖：中心线 x，墨迹 y1..y2。"""
    g.vbar(x, y1, y2, weight=w)


def diag(g, x1, y1, x2, y2, w=W_MAIN):
    """撇捺提平捺：中心线两端点，厚度垂直于中心线。"""
    g.diag(x1, y1, x2, y2, weight=w)


def dot(g, cx, cy, w=W_DOT, h=100, slant=-14):
    """点/短撇：斜切平行四边形。slant 分档 0 / 14 / 26 / -14。"""
    g.dot(cx, cy, w=w, h=h, slant=slant)


def box(g, x1, x2, y_top, y_bot, w=W_MAIN, mid_v=None, mid_h=None, wv=None):
    """矩形框：外框 x1..x2 / y_top..y_bot（含墨迹边界），可选中竖/中横。"""
    wv = wv or w
    g.hbar(x1, x2, y_top - w / 2.0, weight=w)
    g.hbar(x1, x2, y_bot + w / 2.0, weight=w)
    g.vbar(x1 + wv / 2.0, y_top, y_bot, weight=wv)
    g.vbar(x2 - wv / 2.0, y_top, y_bot, weight=wv)
    if mid_v is not None:
        g.vbar(mid_v, y_top, y_bot, weight=wv)
    if mid_h is not None:
        g.hbar(x1, x2, mid_h, weight=w)


def 目box(g, x1, x2, y_top, y_bot, w=W_MAIN, w_in=W_THIN, wv=W_MAIN):
    """目（貝 / 直 的上部）：上、内、内、下 四横 + 左右竖。

    内白按区域高度均分（3 段），保证每段 ≥24 单位。
    """
    gap = (y_top - y_bot - 2 * w - 2 * w_in) / 3.0
    g.hbar(x1, x2, y_top - w / 2.0, weight=w)
    g.hbar(x1, x2, y_bot + w / 2.0, weight=w)
    g.vbar(x1 + wv / 2.0, y_top, y_bot, weight=wv)
    g.vbar(x2 - wv / 2.0, y_top, y_bot, weight=wv)
    g.hbar(x1, x2, y_top - w - gap - w_in / 2.0, weight=w_in)
    g.hbar(x1, x2, y_bot + w + gap + w_in / 2.0, weight=w_in)


def 田box(g, x1, x2, y_top, y_bot, w=W_MAIN, w_in=W_THIN, wv=W_MAIN, mid_v=None):
    """田：上、中、下 三横 + 左右竖 + 中竖；内白 ≥24。"""
    gap = (y_top - y_bot - 2 * w - w_in) / 2.0
    g.hbar(x1, x2, y_top - w / 2.0, weight=w)
    g.hbar(x1, x2, y_bot + w / 2.0, weight=w)
    g.vbar(x1 + wv / 2.0, y_top, y_bot, weight=wv)
    g.vbar(x2 - wv / 2.0, y_top, y_bot, weight=wv)
    g.hbar(x1, x2, y_top - w - gap - w_in / 2.0, weight=w_in)
    if mid_v is not None:
        g.vbar(mid_v, y_top, y_bot, weight=wv)


def flick(g, x, y, dx, dy, w=W_SEC):
    """端点上挑/回勾：自 (x,y) 沿 (dx,dy) 的切角段（端面平切）。"""
    length = math.hypot(dx, dy)
    ux, uy = dx / length, dy / length
    nx, ny = -uy, ux
    hw = w / 2.0
    pts = [
        (x + nx * hw, y + ny * hw),
        (x + dx + nx * hw, y + dy + ny * hw),
        (x + dx - nx * hw, y + dy - ny * hw),
        (x - nx * hw, y - ny * hw),
    ]
    g.poly(pts)


def hook_left(g, x, y_bot, w=W_SEC, dx=-40, dy=40):
    """竖钩（亅）：竖底向左上挑钩，钩的墨迹不越过 y_bot。"""
    length = math.hypot(dx, dy)
    ny = abs(dx) / length          # 法线的竖直分量
    y0 = y_bot + ny * (w / 2.0)
    flick(g, x, y0, dx, dy, w)


# ---------------------------------------------------------------- 复用部件

def comp_亻(g, x=195, x_top=272, y_top=782, y_bot=48, w=W_SEC):
    """亻：短撇 + 竖。批内统一（候 / 値 / 催 / 健 复用同一坐标）。"""
    g.diag(x_top, y_top, x - 28, y_top - 92, weight=w)
    g.vbar(x, y_top - 72, y_bot, weight=w)


def comp_扌(g, x=190, x_h1=60, x_h2=330, y_h=640, y_top=800, y_bot=90, w=W_MAIN):
    """扌：横 + 竖钩 + 提。批内统一（推 / 接 / 授 复用同一坐标）。"""
    g.hbar(x_h1, x_h2, y_h, weight=w)
    g.vbar(x, y_top, y_bot, weight=w)
    hook_left(g, x, y_bot, w=W_SEC)
    g.diag(60, 248, 214, 322, weight=W_SEC)


def comp_氵(g, x_top=196, y_top=700, x_mid=168, y_mid=468, w=W_DOT):
    """氵：上点（短撇 slant 26）+ 中点（丶 slant -14）+ 提。批内统一（満 / 湾）。"""
    g.dot(x_top, y_top, w=w, h=112, slant=26)
    g.dot(x_mid, y_mid, w=w, h=112, slant=-14)
    g.diag(66, 214, 282, 320, weight=W_SEC)


def comp_糸(g, x=60, w=W_SEC):
    """糸（6 画写足）：幺（撇折+撇折+提）+ 小（竖钩+撇+点）。批内统一（細 / 紙）。"""
    g.diag(x + 288, 792, x + 150, 700, weight=w)
    g.hbar(x + 150, x + 258, 700, weight=w)
    g.diag(x + 248, 640, x + 110, 548, weight=w)
    g.hbar(x + 110, x + 218, 548, weight=w)
    g.diag(x + 26, 462, x + 268, 520, weight=W_THIN)
    g.vbar(x + 218, 470, 186, weight=w)
    hook_left(g, x + 218, 186, w=W_SEC, dx=-34, dy=34)
    g.diag(x + 190, 404, x + 74, 268, weight=W_THIN)
    g.dot(x + 330, 372, w=W_DOT, h=104, slant=-14)


def comp_又(g, x_l, x_r, y_top, y_bot, w=W_MAIN):
    """又：横撇 + 捺。x_l/x_r = 部件左右；y_top = 横撇的横；y_bot = 撇的末端。"""
    g.hbar(x_l, x_r, y_top, weight=w)
    g.diag(x_r - 8, y_top - 10, x_l + 40, y_bot, weight=w)
    g.diag(x_l + 60, y_top - 150, x_r + 30, y_bot - 40, weight=w)


def comp_隹(g, x_ren, x_bar_l, x_bar_r, x_v, x_right,
             p1, p2, y_ren_top, y_dot, y_b1, y_b2, y_b3, y_bot,
             w_bar=W_MAIN, w_v=W_SEC, w_dot=W_DOT, h_dot=96):
    """隹：撇 + 亻竖 + 点 + 三横 + 贯穿竖 + 底横。

    x_ren 亻的竖；x_v 贯穿竖；y_b1..y_b3 三横；y_bot 底横。
    """
    g.diag(p1[0], p1[1], p2[0], p2[1], weight=w_v)
    g.vbar(x_ren, y_ren_top, y_bot + w_bar / 2.0, weight=w_v)
    g.dot(x_ren + 115, y_dot, w=w_dot, h=h_dot, slant=-14)
    g.hbar(x_bar_l, x_bar_r, y_b1, weight=w_bar)
    g.hbar(x_bar_l, x_bar_r - 30, y_b2, weight=w_bar)
    g.hbar(x_bar_l, x_bar_r - 30, y_b3, weight=w_bar)
    g.vbar(x_v, y_ren_top + 10, y_bot + w_bar / 2.0, weight=w_v)
    g.hbar(x_ren, x_right, y_bot, weight=w_bar)


# ---------------------------------------------------------------- 24 字

def g_推() -> Glyph:
    """推 U+63A8 —— 扌 + 隹（11画）。

    扌：横 y640 + 竖钩（竖心 x190）+ 提 (60,248)→(214,322)。
    隹：撇(480,780)→(435,700)；亻竖 x460 [96,700]；点 cx575 cy770 slant-14；
        贯穿竖 x700 [106,710]；三横 y660/520/380；底横 y48 通到 x940。
    """
    g = Glyph("uni63A8", advance=1000, unicode=0x63A8, note="推：扌 + 隹")
    comp_扌(g)
    comp_隹(g,
            x_ren=460, x_bar_l=490, x_bar_r=880, x_v=700, x_right=940,
            p1=(480, 780), p2=(435, 700),
            y_ren_top=700, y_dot=770,
            y_b1=660, y_b2=520, y_b3=380, y_bot=48)
    return g


def g_候() -> Glyph:
    """候 U+5019 —— 亻 + 丨 + ユ + 矢（10画）。

    亻：批内通用坐标。丨：x330 [380,810]。ユ：顶横 y772 / 左竖 x505 [660,772] /
        底横 y670（ユ的竖在左，与片假名 ユ 同形）。
    矢：撇(516,556)→(432,470)；横1 y550；横2 y435；撇(588,410)→(402,100)；
        捺(538,404)→(828,70)。
    """
    g = Glyph("uni5019", advance=1000, unicode=0x5019, note="候：亻 + 丨 + ユ + 矢")
    comp_亻(g)
    g.vbar(330, 810, 380, weight=W_SEC)
    # ユ
    g.hbar(470, 850, 772, weight=W_MAIN)
    g.vbar(505, 772, 660, weight=W_SEC)
    g.hbar(470, 850, 670, weight=W_MAIN)
    # 矢
    g.diag(516, 556, 432, 470, weight=W_SEC)
    g.hbar(392, 800, 550, weight=W_MAIN)
    g.hbar(392, 812, 435, weight=W_MAIN)
    g.diag(588, 410, 402, 100, weight=W_MAIN)
    g.diag(538, 404, 828, 70, weight=W_MAIN)
    return g


def g_階() -> Glyph:
    """階 U+968E —— 阝 + 皆（12画）。

    阝：竖 x110 [0,810]；顶横 y790；撇(248,782)→(174,562)；弯钩(174,562)→(254,430)；
        钩尖(254,430)→(214,338)。
    皆：比 上半（左 匕：横 y700 + 竖弯钩 x400；右 匕：撇 + 竖弯钩 x676）；
        白 下半：撇(486,566)→(430,486) + 日形框 x424..830 y470..60（中横 y265）。
    """
    g = Glyph("uni968E", advance=1000, unicode=0x968E, note="階：阝 + 皆")
    # 阝
    g.vbar(110, 810, 0, weight=W_MAIN)
    g.hbar(104, 254, 790, weight=W_MAIN)
    g.diag(248, 782, 174, 562, weight=W_SEC)
    g.diag(174, 562, 254, 430, weight=W_SEC)
    g.diag(254, 430, 214, 338, weight=W_SEC)
    # 皆 上：比
    g.hbar(346, 470, 700, weight=W_SEC)
    g.vbar(400, 790, 486, weight=W_SEC)
    g.diag(400, 500, 520, 468, weight=W_SEC)
    g.diag(902, 782, 700, 700, weight=W_SEC)
    g.vbar(676, 742, 486, weight=W_SEC)
    g.diag(676, 500, 800, 466, weight=W_SEC)
    # 皆 下：白
    g.diag(486, 566, 430, 486, weight=W_SEC)
    box(g, 424, 830, 470, 60, w=W_SEC, mid_h=265)
    return g


def g_程() -> Glyph:
    """程 U+7A0B —— 禾 + 呈（12画）。

    禾：顶撇(336,786)→(112,742)；横 y660 (60..430)；竖 x240 [0,758]；
        撇(222,498)→(78,178)；捺(258,492)→(428,196)。
    呈：口 x556..884 y780..566（内白 30）；王 横1 y480、竖 x700、横2 y330、底横 y48。
    """
    g = Glyph("uni7A0B", advance=1000, unicode=0x7A0B, note="程：禾 + 呈")
    # 禾
    g.diag(336, 786, 112, 742, weight=W_SEC)
    g.hbar(60, 430, 660, weight=W_MAIN)
    g.vbar(240, 758, 0, weight=W_MAIN)
    g.diag(222, 498, 78, 178, weight=W_SEC)
    g.diag(258, 492, 428, 196, weight=W_SEC)
    # 呈
    box(g, 556, 884, 780, 566, w=W_SEC)
    g.hbar(486, 916, 480, weight=W_MAIN)
    g.vbar(700, 480, 96, weight=W_MAIN)
    g.hbar(520, 880, 330, weight=W_MAIN)
    g.hbar(472, 930, 48, weight=W_MAIN)
    return g


def g_満() -> Glyph:
    """満 U+6E80 —— 氵 + 両（12画）。

    氵：批内通用坐标。
    両：顶横 y772 (360..940)；左竖 x400 [158,772]；框顶折 y620 (400..900)+右竖 x900；
        内竖 x565 / x730；底横 y158 (360..940)。
    """
    g = Glyph("uni6E80", advance=1000, unicode=0x6E80, note="満：氵 + 両")
    comp_氵(g)
    # 両
    g.hbar(360, 940, 772, weight=W_MAIN)
    g.vbar(400, 772, 158, weight=W_SEC)
    g.hbar(400, 900, 620, weight=W_MAIN)
    g.vbar(900, 620, 158, weight=W_SEC)
    g.vbar(565, 772, 158, weight=W_SEC)
    g.vbar(730, 772, 158, weight=W_SEC)
    g.hbar(360, 940, 158, weight=W_MAIN)
    return g


def g_敗() -> Glyph:
    """敗 U+6557 —— 貝 + 攵（11画）。

    貝：目形框 x110..400 y780..348（内横 84 细档）；八 撇(250,300)→(90,60)、
        捺(300,300)→(428,60)。
    攵：撇(604,800)→(496,690)；横 y776 (560..898)；撇(886,770)→(556,296)；
        捺(618,424)→(932,96)。
    """
    g = Glyph("uni6557", advance=1000, unicode=0x6557, note="敗：貝 + 攵")
    # 貝
    目box(g, 110, 400, 780, 348, w=W_MAIN, w_in=W_THIN)
    g.diag(250, 300, 90, 60, weight=W_SEC)
    g.diag(300, 300, 428, 60, weight=W_SEC)
    # 攵
    g.diag(604, 800, 496, 690, weight=W_SEC)
    g.hbar(560, 898, 776, weight=W_MAIN)
    g.diag(886, 770, 556, 296, weight=W_MAIN)
    g.diag(618, 424, 932, 96, weight=W_MAIN)
    return g


def g_値() -> Glyph:
    """値 U+5024 —— 亻 + 直（10画）。

    亻：批内通用坐标。
    直：十 横 y720 (376..900) + 竖 x640 [600,812]；目形框 x380..900 y600..176
        （内横 442 / 334，三道白口各 24）；底横 y48 (340..940)。
    """
    g = Glyph("uni5024", advance=1000, unicode=0x5024, note="値：亻 + 直")
    comp_亻(g)
    g.hbar(376, 900, 720, weight=W_MAIN)
    g.vbar(640, 812, 600, weight=W_MAIN)
    目box(g, 380, 900, 600, 176, w=W_SEC, w_in=W_THIN)
    g.hbar(340, 940, 48, weight=W_MAIN)
    return g


def g_買() -> Glyph:
    """買 U+8CB7 —— 罒 + 貝（12画）。

    罒：上横 772 / 下横 652（白口 24），内竖 x382 / x618 贯穿 → 3 个白窗。
    貝：目形框 x180..820 y580..148（上横 532 / 内横 418 / 内横 310 / 下横 176，
        三道白口各 24）；八 撇(430,148)→(250,50)、捺(560,148)→(760,50)。
    """
    g = Glyph("uni8CB7", advance=1000, unicode=0x8CB7, note="買：罒 + 貝")
    # 罒
    g.hbar(130, 870, 772, weight=W_MAIN)
    g.hbar(130, 870, 652, weight=W_MAIN)
    g.vbar(382, 820, 604, weight=W_SEC)
    g.vbar(618, 820, 604, weight=W_SEC)
    # 貝
    目box(g, 180, 820, 580, 148, w=W_MAIN, w_in=W_THIN)
    g.diag(430, 148, 250, 50, weight=W_SEC)
    g.diag(560, 148, 760, 50, weight=W_SEC)
    return g


def g_接() -> Glyph:
    """接 U+63A5 —— 扌 + 妾（11画）。

    扌：批内通用坐标。
    妾：立 顶点(竖点 slant0) cx700 cy770；横 y700 (430..930)；左点(丶 -14) cx590 cy600；
        右撇(800,690)→(702,516)；底横 y508。
        女 撇点(700,430)→(528,268)+(528,268)→(720,120)；撇(886,412)→(482,86)；
        横 y300 (430..940)。
    """
    g = Glyph("uni63A5", advance=1000, unicode=0x63A5, note="接：扌 + 妾")
    comp_扌(g)
    # 立
    g.dot(700, 770, w=W_DOT, h=92, slant=0)
    g.hbar(430, 930, 700, weight=W_MAIN)
    g.dot(590, 600, w=W_DOT, h=104, slant=-14)
    g.diag(800, 690, 702, 516, weight=W_SEC)
    g.hbar(430, 930, 508, weight=W_MAIN)
    # 女
    g.diag(700, 430, 530, 268, weight=W_MAIN)
    g.diag(530, 268, 720, 120, weight=W_SEC)
    g.diag(886, 412, 482, 86, weight=W_MAIN)
    g.hbar(430, 940, 300, weight=W_MAIN)
    return g


def g_討() -> Glyph:
    """討 U+8A0E —— 言 + 寸（10画）。

    言：竖点 slant0 cx245 cy770；横 y700 (70..420)；横 y540；横 y380；
        口 x110..380 y300..66（内白 42）。
    寸：横 y560 (490..940)；竖钩 x760 [120,780]；点(丶 -14) cx580 cy380。
    """
    g = Glyph("uni8A0E", advance=1000, unicode=0x8A0E, note="討：言 + 寸")
    # 言
    g.dot(245, 770, w=W_DOT, h=92, slant=0)
    g.hbar(70, 420, 700, weight=W_MAIN)
    g.hbar(110, 380, 540, weight=W_MAIN)
    g.hbar(110, 380, 380, weight=W_MAIN)
    box(g, 110, 380, 300, 66, w=W_MAIN)
    # 寸
    g.hbar(490, 940, 560, weight=W_MAIN)
    g.vbar(760, 780, 120, weight=W_MAIN)
    hook_left(g, 760, 120, w=W_SEC)
    g.dot(580, 380, w=W_DOT, h=104, slant=-14)
    return g


def g_路() -> Glyph:
    """路 U+8DEF —— 足 + 各（13画）。

    足：口 x90..370 y800..560；丨 x230 [130,560]；横 y330 (230..400)；
        撇(212,300)→(80,84)；捺(250,300)→(420,84)。
    各：撇(626,790)→(500,700)；横 y726 (566..852)+撇折(848,716)→(566,556)；
        捺(596,626)→(916,486)；口 x566..866 y476..246。
    """
    g = Glyph("uni8DEF", advance=1000, unicode=0x8DEF, note="路：足 + 各")
    # 足
    box(g, 90, 370, 800, 560, w=W_MAIN)
    g.vbar(230, 560, 130, weight=W_MAIN)
    g.hbar(230, 400, 330, weight=W_SEC)
    g.diag(212, 300, 80, 84, weight=W_SEC)
    g.diag(250, 300, 420, 84, weight=W_SEC)
    # 各
    g.diag(626, 790, 500, 700, weight=W_SEC)
    g.hbar(566, 852, 726, weight=W_MAIN)
    g.diag(848, 716, 566, 556, weight=W_MAIN)
    g.diag(596, 626, 916, 486, weight=W_MAIN)
    box(g, 566, 866, 476, 246, w=W_MAIN)
    return g


def g_悪() -> Glyph:
    """悪 U+60AA —— 亜 + 心（11画）。

    亜：顶横 y772 (100..900)；中横 y640 (168..832)；内竖 x300 / x500 / x700
        [486..640]；底横 y486 (168..832)。
    心：左点(丶 -14) cx240 cy300；卧钩(330,222)→(640,124)+上挑；
        中点 cx760 cy252；右点 cx880 cy140。
    """
    g = Glyph("uni60AA", advance=1000, unicode=0x60AA, note="悪：亜 + 心")
    # 亜
    g.hbar(100, 900, 772, weight=W_MAIN)
    g.hbar(168, 832, 640, weight=W_MAIN)
    g.vbar(300, 640, 486, weight=W_SEC)
    g.vbar(500, 640, 486, weight=W_SEC)
    g.vbar(700, 640, 486, weight=W_SEC)
    g.hbar(168, 832, 486, weight=W_MAIN)
    # 心
    g.dot(240, 300, w=W_DOT, h=104, slant=-14)
    g.diag(330, 222, 640, 124, weight=W_MAIN)
    flick(g, 640, 124, 52, 74, w=W_SEC)
    g.dot(760, 252, w=W_DOT, h=104, slant=-14)
    g.dot(880, 140, w=W_DOT, h=104, slant=-14)
    return g


def g_崎() -> Glyph:
    """崎 U+5D0E —— 山 + 奇（11画）。

    山：丨 x200 [148,800]；丨 x84 [148,640]；丨 x332 [148,640]；底横 y148 (60..350)。
    奇：大 横 y700 (400..920)；撇(694,786)→(452,556)；捺(662,700)→(926,536)；
        可 横 y476 (400..940)；口 x420..660 y400..176（内白 40）；亅 x860 [150,700] + 钩。
    """
    g = Glyph("uni5D0E", advance=1000, unicode=0x5D0E, note="崎：山 + 奇")
    # 山
    g.vbar(200, 800, 148, weight=W_MAIN)
    g.vbar(84, 640, 148, weight=W_SEC)
    g.vbar(332, 640, 148, weight=W_SEC)
    g.hbar(60, 350, 148, weight=W_MAIN)
    # 奇
    g.hbar(400, 920, 700, weight=W_MAIN)
    g.diag(694, 786, 452, 556, weight=W_MAIN)
    g.diag(662, 700, 926, 536, weight=W_MAIN)
    g.hbar(400, 940, 476, weight=W_MAIN)
    box(g, 420, 660, 400, 176, w=W_SEC)
    g.vbar(860, 700, 150, weight=W_MAIN)
    hook_left(g, 860, 150, w=W_SEC)
    return g


def g_督() -> Glyph:
    """督 U+7763 —— 叔 + 目（13画）。

    叔 上：上 丨 x330 [610,800]、横 y750 (330..498)、横 y610 (230..498)；
        小 竖钩 x330 [400,540]、撇(300,510)→(210,400)、点(420,490)；
        又 横撇 hbar(540,900,720)+diag(892,710)→(580,470)、捺(600,570)→(930,430)。
    目：框 x280..720 y420..0（横画 84 细档，内白均分）。
    """
    g = Glyph("uni7763", advance=1000, unicode=0x7763, note="督：叔 + 目")
    # 叔
    g.vbar(330, 800, 610, weight=W_MAIN)
    g.hbar(330, 498, 750, weight=W_SEC)
    g.hbar(230, 498, 610, weight=W_MAIN)
    g.vbar(330, 540, 400, weight=W_SEC)
    hook_left(g, 330, 400, w=W_SEC, dx=-34, dy=34)
    g.diag(300, 510, 210, 400, weight=W_THIN)
    g.dot(420, 490, w=W_DOT, h=88, slant=-14)
    comp_又(g, 540, 900, 720, 470, w=W_MAIN)
    # 目
    目box(g, 280, 720, 420, 0, w=W_THIN, w_in=W_THIN, wv=W_THIN)
    return g


def g_授() -> Glyph:
    """授 U+6388 —— 扌 + 受（11画）。

    扌：批内通用坐标。
    受：爫 撇(840,800)→(590,740)、左点 slant14 cx520 cy630、中点 slant0 cx690 cy630、
        右点 slant-14 cx858 cy630（h72，爫 内小记号）；
        冖 左竖 x440 [480,522] + 横 y522 (420..930) + 右短竖 x906 [474,522]；
        又 横撇 hbar(480,900,400)+diag(892,390)→(520,150)、捺(540,250)→(930,110)。
    """
    g = Glyph("uni6388", advance=1000, unicode=0x6388, note="授：扌 + 受")
    comp_扌(g)
    # 爫
    g.diag(840, 800, 590, 740, weight=W_MAIN)
    g.dot(520, 630, w=W_DOT, h=72, slant=14)
    g.dot(690, 630, w=W_DOT, h=72, slant=0)
    g.dot(858, 630, w=W_DOT, h=72, slant=-14)
    # 冖
    g.vbar(440, 522, 480, weight=W_SEC)
    g.hbar(420, 930, 522, weight=W_MAIN)
    g.vbar(906, 522, 474, weight=W_SEC)
    # 又
    comp_又(g, 480, 900, 400, 150, w=W_MAIN)
    return g


def g_催() -> Glyph:
    """催 U+50AC —— 亻 + 崔（13画）。

    亻：批内通用坐标。
    崔 上山：丨 x610 [568,810]、丨 x450 [568,700]、丨 x770 [568,700]、底横 y616 (440..790)。
    崔 下隹（压缩档，横画 84 细档保内白 ≥24）：撇(462,516)→(418,452)；
        亻竖 x420 [84,470]；点 cx530 cy496 slant-14；贯穿竖 x650 [84,470]；
        三横 y380 / 270 / 160；底横 y48 (420..940)。
    """
    g = Glyph("uni50AC", advance=1000, unicode=0x50AC, note="催：亻 + 崔")
    comp_亻(g)
    # 山
    g.vbar(610, 810, 568, weight=W_MAIN)
    g.vbar(450, 700, 568, weight=W_SEC)
    g.vbar(770, 700, 568, weight=W_SEC)
    g.hbar(440, 790, 616, weight=W_MAIN)
    # 隹（压缩）
    g.diag(462, 516, 418, 452, weight=W_SEC)
    g.vbar(420, 470, 84, weight=W_SEC)
    g.dot(530, 496, w=W_DOT, h=84, slant=-14)
    g.vbar(650, 470, 84, weight=W_SEC)
    g.hbar(480, 880, 380, weight=W_THIN)
    g.hbar(480, 856, 270, weight=W_THIN)
    g.hbar(480, 856, 160, weight=W_THIN)
    g.hbar(420, 940, 48, weight=W_THIN)
    return g


def g_細() -> Glyph:
    """細 U+7D30 —— 糸 + 田（11画）。

    糸：批内通用坐标（6 画写足，与 紙 同）。
    田：框 x470..900 y790..120，中竖 x685、中横 y455。
    """
    g = Glyph("uni7D30", advance=1000, unicode=0x7D30, note="細：糸 + 田")
    comp_糸(g)
    box(g, 470, 900, 790, 120, w=W_MAIN, mid_v=685, mid_h=455)
    return g


def g_週() -> Glyph:
    """週 U+9031 —— 辶 + 周（10画）。

    辶：丶 slant-14 cx180 cy700；折 横 y590 (88..276)+撇(268,584)→(126,424)；
        平捺 diag(66,150)→(900,206)。
    周：左竖 x430 [274,812]；顶横 y772 (430..900)；右竖钩 x900 [274,772]+钩；
        土 横 y648 (486..848)、竖 x664 [540,712]、长横 y540 (466..876)；
        口 x520..812 y466..274（细横，内白 24）。
    """
    g = Glyph("uni9031", advance=1000, unicode=0x9031, note="週：辶 + 周")
    # 辶
    g.dot(180, 700, w=W_DOT, h=104, slant=-14)
    g.hbar(88, 276, 590, weight=W_SEC)
    g.diag(268, 584, 126, 424, weight=W_SEC)
    g.diag(66, 150, 900, 206, weight=W_MAIN)
    # 周
    g.vbar(430, 812, 274, weight=W_SEC)
    g.hbar(430, 900, 772, weight=W_MAIN)
    g.vbar(900, 772, 274, weight=W_SEC)
    hook_left(g, 900, 274, w=W_SEC, dx=-38, dy=38)
    g.hbar(486, 848, 648, weight=W_SEC)
    g.vbar(664, 712, 540, weight=W_SEC)
    g.hbar(466, 876, 540, weight=W_SEC)
    box(g, 520, 812, 466, 274, w=W_THIN, wv=W_SEC)
    return g


def g_湾() -> Glyph:
    """湾 U+6E7E —— 氵 + 弯（12画）。

    氵：批内通用坐标。
    弯 上亦：竖点 slant0 cx650 cy768；横 y700 (360..930)；左撇(540,690)→(372,400)；
        丨 x640 [430,690]；右撇(838,690)→(706,430)；右点 slant-14 cx892 cy478。
    弯 下弓（横画 84 细档）：横折 hbar(480,880,338)+vbar(880,338,262)；
        横 y220 (480..880)；竖折折钩 vbar(500,262,144)+hbar(500,870,102)+
        vbar(870,144,60)+钩。
    """
    g = Glyph("uni6E7E", advance=1000, unicode=0x6E7E, note="湾：氵 + 弯")
    comp_氵(g)
    # 亦
    g.dot(650, 768, w=W_DOT, h=92, slant=0)
    g.hbar(360, 930, 700, weight=W_MAIN)
    g.diag(540, 690, 372, 400, weight=W_MAIN)
    g.vbar(640, 690, 430, weight=W_SEC)
    g.diag(838, 690, 706, 430, weight=W_MAIN)
    g.dot(892, 478, w=W_DOT, h=96, slant=-14)
    # 弓
    g.hbar(480, 880, 338, weight=W_THIN)
    g.vbar(880, 338, 262, weight=W_SEC)
    g.hbar(480, 880, 220, weight=W_THIN)
    g.vbar(500, 262, 144, weight=W_SEC)
    g.hbar(500, 870, 102, weight=W_THIN)
    g.vbar(870, 144, 60, weight=W_SEC)
    hook_left(g, 870, 60, w=W_SEC, dx=-36, dy=36)
    return g


def g_紙() -> Glyph:
    """紙 U+7D19 —— 糸 + 氏（10画）。

    糸：批内通用坐标（与 細 同）。
    氏：撇(626,790)→(472,720)；竖提 x478 [158,758]+提 flick(478,158)→(628,246)；
        横 y420 (466..800)；斜钩 diag(560,762)→(886,148)+回锋 flick(886,148,-54,76)。
    """
    g = Glyph("uni7D19", advance=1000, unicode=0x7D19, note="紙：糸 + 氏")
    comp_糸(g)
    g.diag(626, 790, 472, 720, weight=W_MAIN)
    g.vbar(478, 758, 158, weight=W_MAIN)
    flick(g, 478, 158, 150, 88, w=W_SEC)
    g.hbar(466, 800, 420, weight=W_MAIN)
    g.diag(560, 762, 886, 148, weight=W_MAIN)
    flick(g, 886, 148, -54, 76, w=W_SEC)
    return g


def g_師() -> Glyph:
    """師 U+5E2B —— 𠂤 + 帀（10画）。

    𠂤：撇(196,792)→(96,706)；长竖 x150 [48,742]；短竖 x244 [48,430]；
        横折 hbar(198,332,382)+vbar(332,430,48)；底横 hbar(198,332,96)。
    帀：顶横 y772 (398..940)；巾 横 y640 (440..860)、左竖 x450 [260,640]、
        右竖 x860 [260,640]+钩、中竖 x650 [48,640]。
    """
    g = Glyph("uni5E2B", advance=1000, unicode=0x5E2B, note="師：𠂤 + 帀")
    # 𠂤
    g.diag(196, 792, 96, 706, weight=W_SEC)
    g.vbar(150, 742, 48, weight=W_MAIN)
    g.vbar(244, 430, 48, weight=W_SEC)
    g.hbar(198, 332, 382, weight=W_SEC)
    g.vbar(332, 430, 48, weight=W_SEC)
    g.hbar(198, 332, 96, weight=W_SEC)
    # 帀
    g.hbar(398, 940, 772, weight=W_MAIN)
    g.hbar(440, 860, 640, weight=W_MAIN)
    g.vbar(450, 640, 260, weight=W_SEC)
    g.vbar(860, 640, 260, weight=W_SEC)
    hook_left(g, 860, 260, w=W_SEC, dx=-36, dy=36)
    g.vbar(650, 640, 48, weight=W_MAIN)
    return g


def g_登() -> Glyph:
    """登 U+767B —— 癶 + 豆（12画）。

    癶：左撇(424,814)→(202,724)；左横撇 hbar(150,352,690)+diag(342,684)→(110,566)；
        右撇(766,814)→(556,700)；右捺(596,714)→(928,516)；中点 slant-14 cx470 cy636。
    豆：横 y470 (230..770)；口 x272..728 y396..204（细横，内白 24）；丷 点 slant-14 cx362 cy150、
        点 slant-14 cx640 cy150（h76）；底横 y48 (196..800)。
    """
    g = Glyph("uni767B", advance=1000, unicode=0x767B, note="登：癶 + 豆")
    # 癶
    g.diag(424, 814, 202, 724, weight=W_MAIN)
    g.hbar(150, 352, 690, weight=W_MAIN)
    g.diag(342, 684, 110, 566, weight=W_MAIN)
    g.diag(766, 814, 556, 700, weight=W_MAIN)
    g.diag(596, 714, 928, 516, weight=W_MAIN)
    g.dot(470, 636, w=W_DOT, h=96, slant=-14)
    # 豆
    g.hbar(230, 770, 470, weight=W_MAIN)
    box(g, 272, 728, 396, 204, w=W_THIN, wv=W_SEC)
    g.dot(362, 150, w=W_DOT, h=76, slant=-14)
    g.dot(640, 150, w=W_DOT, h=76, slant=-14)
    g.hbar(196, 800, 48, weight=W_MAIN)
    return g


def g_健() -> Glyph:
    """健 U+5065 —— 亻 + 建（11画）。

    亻：批内通用坐标。
    建 上聿：横折 hbar(480,900,772)+vbar(900,772,616)；横 y630 / 490 / 350
        (480..856)；竖 x700 [302,790]。
    建 下廴：横折折撇 hbar(360,462,560)+diag(458,552)→(360,424)+hbar(360,456,424)
        +diag(450,418)→(344,200)；平捺 diag(340,170)→(930,230)。
    """
    g = Glyph("uni5065", advance=1000, unicode=0x5065, note="健：亻 + 建")
    comp_亻(g)
    # 聿
    g.hbar(480, 900, 772, weight=W_MAIN)
    g.vbar(900, 772, 616, weight=W_SEC)
    g.hbar(480, 856, 630, weight=W_MAIN)
    g.hbar(480, 856, 490, weight=W_MAIN)
    g.hbar(480, 856, 350, weight=W_MAIN)
    g.vbar(700, 790, 302, weight=W_MAIN)
    # 廴
    g.hbar(360, 462, 560, weight=W_SEC)
    g.diag(458, 552, 360, 424, weight=W_SEC)
    g.hbar(360, 456, 424, weight=W_SEC)
    g.diag(450, 418, 344, 200, weight=W_SEC)
    g.diag(340, 170, 930, 230, weight=W_MAIN)
    return g


def g_黒() -> Glyph:
    """黒 U+9ED2 —— 里 + 灬（11画）。

    里 上田：框 x180..820 y820..470，中竖 x500、中横 84 细档；
        里 下：竖 x500 续到 230；短横 y350 (270..730)；长横 y230 (180..820)。
    灬：左点 slant14 cx222 cy85；中两点 slant0 cx432 / cx640；右点 slant-14 cx822。
    """
    g = Glyph("uni9ED2", advance=1000, unicode=0x9ED2, note="黒：里 + 灬")
    # 里
    田box(g, 180, 820, 820, 470, w=W_MAIN, w_in=W_THIN, mid_v=500)
    g.vbar(500, 470, 230, weight=W_MAIN)
    g.hbar(270, 730, 350, weight=W_SEC)
    g.hbar(180, 820, 230, weight=W_MAIN)
    # 灬
    g.dot(222, 85, w=W_DOT, h=104, slant=14)
    g.dot(432, 85, w=W_DOT, h=104, slant=0)
    g.dot(640, 85, w=W_DOT, h=104, slant=0)
    g.dot(822, 85, w=W_DOT, h=104, slant=-14)
    return g


# ---------------------------------------------------------------- 装配

def build() -> list[Glyph]:
    return [
        g_推(), g_候(), g_階(), g_程(), g_満(), g_敗(), g_値(), g_買(),
        g_接(), g_討(), g_路(), g_悪(), g_崎(), g_督(), g_授(), g_催(),
        g_細(), g_週(), g_湾(), g_紙(), g_師(), g_登(), g_健(), g_黒(),
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s3-007.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] wrote {target_ufo()}")
