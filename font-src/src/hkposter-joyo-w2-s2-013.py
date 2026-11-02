"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-013。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

整体取舍
--------
* 字面框 x 60..940 / y 0..820，advance 固定 1000，与繁体汉字同档，便于中日混排。
* 笔画权重只用三档：主 96 / 次 92 / 细 84；点（dot）墨量用 84。
* 斜切档位只取规格冻结的档：丶 -14、丿 +14、短撇 +26、竖点 0。
  （丶＝辶的点/厶的点/寸的点/丷左；丿＝丷右/小右点；短撇＝氵的上点等；
    竖点＝亠的点。）
* **笔画角度一律照标准骨架画**：本批只调重量档位、端点处理（方切/斜切）、
  转角与部件落位，未做任何改向。
* 批内同族观感：亻 / 氵 / 扌 / 木 / 口 / 日 / 田 / 艹 / 宀 等部件统一走
  comp_* 辅助函数，只做位置与大小的光学校正，不重画。
* 密排处（横画叠横画）内白 ≥ 24 单位；竖与竖之间 ≥ 60 单位。
"""

from __future__ import annotations

import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, write_ufo  # noqa: E402

W_MAIN = 96
W_SEC = 92
W_THIN = 84
W_DOT = 84

X0, X1 = 60, 940
Y0, Y1 = 0, 820

# 斜切档位（规格冻结，不得自造）
SLANT_DOT = -14      # 丶：右下的点
SLANT_NIE = 14       # 丿：左下的点 / 小右点
SLANT_SHORT = 26     # 短撇：氵的上点等
SLANT_VERT = 0       # 竖点：亠的点


# ---------------------------------------------------------------- 基础笔法


def hbar(g, x1, x2, y, w=W_MAIN):
    """水平硬边矩形：中心线 y，墨迹占 y±w/2。"""
    g.hbar(x1, x2, y, weight=w)


def vbar(g, x, y1, y2, w=W_MAIN):
    """垂直硬边矩形：中心线 x，端点即墨迹端点。"""
    g.vbar(x, y1, y2, weight=w)


def diag(g, x1, y1, x2, y2, w=W_MAIN):
    """斜笔画（撇/捺/钩）：中心线两端点，厚度垂直于中心线，平切收笔。"""
    g.diag(x1, y1, x2, y2, weight=w)


def dot(g, cx, cy, w=W_DOT, h=104, slant=0):
    """点 / 短撇：斜切平行四边形。cx,cy 为形心。"""
    g.dot(cx, cy, w=w, h=h, slant=slant)


def hook(g, x, y, dx=-60, dy=70, w=W_THIN):
    """竖笔末端的钩（左上挑）。"""
    g.diag(x, y, x + dx, y + dy, weight=w)


# ---------------------------------------------------------------- 通用部件


def comp_亻(g, x=205, w=W_MAIN, top=Y1, bot=Y0):
    """亻：上撇 + 竖。x = 竖的中心线。"""
    g.diag(x + 15, top - 30, x - 85, top - 250, weight=w)
    g.vbar(x, bot, top - 250, weight=w)


def comp_氵(g, x=150, w=W_THIN, top=Y1, bot=Y0):
    """氵：上点（短撇 26）+ 中点（短撇 26）+ 提。"""
    g.dot(x + 25, top - 95, w=88, h=106, slant=SLANT_SHORT)
    g.dot(x + 5, top - 300, w=88, h=106, slant=SLANT_SHORT)
    g.diag(x - 70, bot + 95, x + 70, bot + 235, weight=w)


def comp_扌(g, x=185, w=W_MAIN, top=Y1, bot=Y0):
    """扌：横 + 竖钩 + 提。"""
    g.hbar(x - 125, x + 115, top - 200, weight=w)
    g.vbar(x, bot, top, weight=w)
    g.diag(x - 8, bot + 6, x - 66, bot + 72, weight=W_THIN)
    g.diag(x - 115, bot + 185, x + 90, bot + 295, weight=W_THIN)


def comp_木左(g, x=190, w=W_MAIN, w2=W_SEC, top=Y1, bot=Y0, ybar=610):
    """木（左侧偏旁）：横 + 竖 + 长撇 + 短捺。"""
    g.hbar(x - 130, x + 140, ybar, weight=w)
    g.vbar(x, bot, top, weight=w)
    g.diag(x + 5, ybar - 40, x - 120, bot + 180, weight=w2)
    g.diag(x + 10, ybar - 70, x + 140, ybar - 240, weight=w2)


def comp_木下(g, x=500, w=W_MAIN, w2=W_SEC, top=560, bot=Y0, ybar=470):
    """木（下部）：横 + 竖 + 撇 + 捺。"""
    g.hbar(x - 230, x + 230, ybar, weight=w)
    g.vbar(x, bot, top, weight=w)
    g.diag(x - 5, ybar - 40, x - 240, bot + 80, weight=w2)
    g.diag(x + 5, ybar - 40, x + 250, bot + 80, weight=w2)


def comp_口(g, x1, x2, y1, y2, w=W_MAIN):
    """口：左竖 + 右竖 + 上横 + 下横。"""
    g.vbar(x1, y1, y2, weight=w)
    g.vbar(x2, y1, y2, weight=w)
    g.hbar(x1, x2, y2 - w / 2.0, weight=w)
    g.hbar(x1, x2, y1 + w / 2.0, weight=w)


def comp_日(g, x1, x2, y1, y2, w=W_MAIN, mid_w=W_SEC):
    """日：口 + 中横。"""
    comp_口(g, x1, x2, y1, y2, w)
    g.hbar(x1, x2, (y1 + y2) / 2.0, weight=mid_w)


def comp_田(g, x1, x2, y1, y2, w=W_MAIN, mid_w=W_SEC):
    """田：口 + 中竖 + 中横。"""
    comp_口(g, x1, x2, y1, y2, w)
    g.vbar((x1 + x2) / 2.0, y1, y2, weight=w)
    g.hbar(x1, x2, (y1 + y2) / 2.0, weight=mid_w)


def comp_艹(g, x1, x2, ybar, w=W_MAIN):
    """艹：横 + 两竖（穿过横）。"""
    g.hbar(x1, x2, ybar, weight=w)
    g.vbar(x1 + (x2 - x1) * 0.25, ybar - 55, Y1, weight=w)
    g.vbar(x1 + (x2 - x1) * 0.75, ybar - 55, Y1, weight=w)


def comp_宀(g, x1, x2, w=W_MAIN):
    """宀：竖点（0）+ 左竖 + 横 + 右钩。"""
    g.dot((x1 + x2) / 2.0, Y1 - 58, w=92, h=116, slant=SLANT_VERT)
    g.vbar(x1 + 50, Y1 - 180, Y1 - 100, weight=w)
    g.hbar(x1 + 50, x2 - 40, Y1 - 132, weight=w)
    g.diag(x2 - 45, Y1 - 132, x2 - 110, Y1 - 227, weight=W_THIN)


def comp_心(g, left=190, mid=480, right=810, hook_l=260, hook_r=720,
            base=180, w=W_SEC):
    """心：左撇点（短撇 26）+ 卧钩（带钩）+ 中丶（-14）+ 右丶（-14）。

    卧钩自 hook_l 落到 hook_r（右下），三个点分列左上 / 中上 / 右上，
    整体占满字宽，字面感与 忠 / 忘 里的心一致。
    """
    g.dot(left, base + 120, w=90, h=112, slant=SLANT_SHORT)
    g.diag(hook_l, base + 20, hook_r, base - 90, weight=w)
    g.diag(hook_r - 4, base - 88, hook_r + 70, base - 10, weight=W_THIN)
    g.dot(mid, base + 130, w=88, h=104, slant=SLANT_DOT)
    g.dot(right, base + 160, w=88, h=104, slant=SLANT_DOT)


def comp_女(g, x=520, ytop=760, ymid=520, ybot=60, half=250, w=W_SEC):
    """女：撇点（上段 + 下段）+ 撇 + 横。"""
    g.diag(x, ytop, x - 140, ymid - 40, weight=w)
    g.diag(x - 140, ymid - 40, x + 130, ybot, weight=w)
    g.diag(x + 120, ytop - 20, x - half, ybot + 40, weight=w)
    g.hbar(x - half - 30, x + half + 10, ymid, weight=w)


# ---------------------------------------------------------------- 字形


def g_6749() -> Glyph:
    """杉 U+6749 —— 木 + 彡（7 画）。

    分区：木 x 60..330（横 y610 / 竖 x195 / 长撇 / 短捺）；
    彡 x 385..915（三撇平行，逐级向左下错开）。
    """
    g = Glyph("uni6749", advance=1000, unicode=0x6749, note="杉：木 + 彡")
    g.hbar(60, 330, 610, weight=W_MAIN)            # 1 横
    g.vbar(195, 40, 820, weight=W_MAIN)             # 2 竖
    g.diag(200, 575, 72, 180, weight=W_SEC)         # 3 撇
    g.diag(205, 550, 330, 370, weight=W_SEC)        # 4 捺（短）
    g.diag(915, 795, 605, 632, weight=W_SEC)        # 5 撇
    g.diag(805, 588, 495, 425, weight=W_SEC)        # 6 撇
    g.diag(695, 381, 385, 218, weight=W_SEC)        # 7 撇
    return g


def g_91CC() -> Glyph:
    """里 U+91CC —— 甲 + 二（7 画）。

    分区：上部甲 x 250..750 / y 380..820（中竖贯通）；
    下部二：短横 y200、长横 y0。
    """
    g = Glyph("uni91CC", advance=1000, unicode=0x91CC, note="里：甲 + 二")
    g.vbar(250, 380, 820, weight=W_MAIN)             # 1 竖（左）
    g.hbar(250, 750, 772, weight=W_MAIN)             # 2 横（顶）
    g.vbar(750, 380, 820, weight=W_MAIN)             # 3 竖（右）
    g.hbar(250, 750, 600, weight=W_SEC)              # 4 横（中间）
    g.hbar(250, 750, 428, weight=W_MAIN)             # 5 横（框底）
    g.vbar(500, 200, 820, weight=W_MAIN)             # 6 竖（中）
    g.hbar(330, 670, 200, weight=W_MAIN)             # 7 横（二上）
    g.hbar(90, 910, 48, weight=W_MAIN)               # 8 横（二下）
    return g


def g_8352() -> Glyph:
    """荒 U+8352 —— 艹 + 巟（9 画）。

    分区：艹 y690..820（横 + 两竖穿横）；
    亠 y452..670（竖点 0 明显露出，落在横上方）；
    亡 x250..490 / y60..500（竖折）；
    川 x570..898 / y60..470（撇 + 两竖）。
    """
    g = Glyph("uni8352", advance=1000, unicode=0x8352, note="荒：艹 + 巟")
    g.hbar(110, 890, 740, weight=W_MAIN)             # 1 横（艹）
    g.vbar(320, 690, 820, weight=W_MAIN)             # 2 竖（艹左）
    g.vbar(680, 690, 820, weight=W_MAIN)             # 3 竖（艹右）
    g.dot(500, 620, w=84, h=100, slant=SLANT_VERT)   # 4 丶（亠，竖点）
    g.hbar(140, 860, 500, weight=W_MAIN)             # 5 横（亠）
    g.vbar(250, 60, 500, weight=W_MAIN)              # 6 竖（亡）
    g.hbar(250, 490, 108, weight=W_MAIN)             # 7 竖折的折（亡）
    g.diag(620, 470, 570, 90, weight=W_SEC)          # 8 撇（川）
    g.vbar(720, 60, 470, weight=W_MAIN)              # 9 竖（川）
    g.vbar(850, 60, 470, weight=W_MAIN)              # 10 竖（川）
    return g


def g_59A5() -> Glyph:
    """妥 U+59A5 —— 爫 + 女（7 画）。

    分区：爫 y529..808（顶撇 + 三个下垂短撇，全部向左倾）；
    女 y80..556（横 y330 / 撇点 / 撇）。
    """
    g = Glyph("uni59A5", advance=1000, unicode=0x59A5, note="妥：爫 + 女")
    g.diag(860, 775, 230, 725, weight=W_MAIN)        # 1 撇（爫顶）
    g.dot(300, 600, w=92, h=112, slant=SLANT_SHORT)  # 2 短撇（爫左）
    g.dot(500, 585, w=92, h=112, slant=SLANT_SHORT)  # 3 短撇（爫中）
    g.dot(700, 600, w=92, h=112, slant=SLANT_NIE)    # 4 撇（爫右）
    g.diag(620, 520, 380, 330, weight=W_SEC)         # 5 撇点（上段）
    g.diag(380, 330, 700, 80, weight=W_SEC)          # 6 撇点（下段）
    g.diag(790, 490, 210, 110, weight=W_SEC)         # 7 撇（女）
    g.hbar(110, 900, 330, weight=W_SEC)              # 横（女）
    return g


def g_5A01() -> Glyph:
    """威 U+5A01 —— 戌框 + 女（9 画）。

    分区：顶横只占左半（x150..620 / y780），右上为丶（-14）；
    厂撇 (340,760)→(120,250)；斜钩 (620,790)→(850,200) 带钩；
    戌短横 y560（细 84）；女在左中（横 y330 / 撇点 / 撇），整体减重。
    """
    g = Glyph("uni5A01", advance=1000, unicode=0x5A01, note="威：戌 + 女")
    g.hbar(150, 620, 780, weight=W_THIN)              # 1 横（顶，左半）
    g.dot(705, 762, w=84, h=100, slant=SLANT_DOT)    # 2 丶（右上）
    g.diag(340, 760, 120, 250, weight=W_THIN)        # 3 撇（厂）
    g.diag(620, 790, 850, 200, weight=W_SEC)         # 4 斜钩
    g.diag(846, 208, 910, 275, weight=W_THIN)        # 斜钩的钩
    g.hbar(300, 600, 560, weight=W_THIN)             # 5 横（戌）
    g.hbar(230, 640, 330, weight=W_THIN)             # 6 横（女）
    g.diag(520, 530, 390, 340, weight=W_THIN)        # 7 撇点（上段）
    g.diag(390, 340, 640, 120, weight=W_THIN)         # 8 撇点（下段）
    g.diag(650, 500, 260, 150, weight=W_THIN)         # 9 撇（女）
    return g


def g_5FE0() -> Glyph:
    """忠 U+5FE0 —— 中 + 心（8 画）。

    分区：中 上部（口 x130..870 / y470..740，竖 x500 只露头尾）；
    心 下部（x130..880 / y60..400），与参照字面感一致：口扁而宽、心低而宽。
    """
    g = Glyph("uni5FE0", advance=1000, unicode=0x5FE0, note="忠：中 + 心")
    g.vbar(500, 430, 780, weight=W_MAIN)             # 1 竖（中）
    comp_口(g, 130, 870, 470, 740, W_MAIN)
    comp_心(g, left=190, mid=480, right=810, hook_l=260, hook_r=720, base=180)
    return g


def g_663C() -> Glyph:
    """昼 U+663C —— 尺 + 旦（9 画）。

    分区：尺 y470..820（尸：顶横 724..820 / 右竖 / 下横 604..700 + 长撇 + 乀）；
    2026-10-31 回修：尸顶横与尸底横白口 −12 → 尸底下移 36，白口 24。
    日 x340..760 / y136..472；底横 y48。
    """
    g = Glyph("uni663C", advance=1000, unicode=0x663C, note="昼：尺 + 旦")
    g.hbar(200, 660, 772, weight=W_MAIN)             # 1 横（尸顶，墨 724..820）
    g.vbar(660, 652, 820, weight=W_MAIN)             # 2 竖（尸右）
    g.hbar(200, 660, 652, weight=W_MAIN)             # 3 横（尸底，墨 604..700）
    g.diag(205, 652, 85, 470, weight=W_SEC)          # 4 撇
    g.diag(290, 652, 540, 560, weight=W_THIN)        # 5 乀
    comp_日(g, 340, 760, 136, 472, W_MAIN)            # 日
    g.hbar(90, 910, 48, weight=W_MAIN)               # 横（旦底）
    return g


def g_8336() -> Glyph:
    """茶 U+8336 —— 艹 + 人 + 木（9 画）。

    分区：艹 y652..820；人 y480..660（撇捺）；
    木 y40..508（横 y460 / 竖 x500 / 撇捺）。
    """
    g = Glyph("uni8336", advance=1000, unicode=0x8336, note="茶：艹 + 人 + 木")
    g.hbar(130, 870, 700, weight=W_MAIN)             # 1 横（艹）
    g.vbar(340, 655, 820, weight=W_MAIN)             # 2 竖（艹左）
    g.vbar(660, 655, 820, weight=W_MAIN)             # 3 竖（艹右）
    g.diag(500, 660, 290, 490, weight=W_SEC)         # 4 撇（人）
    g.diag(500, 660, 710, 490, weight=W_SEC)         # 5 捺（人）
    g.hbar(240, 760, 460, weight=W_MAIN)             # 6 横（木）
    g.vbar(500, 40, 640, weight=W_MAIN)              # 7 竖（木）
    g.diag(495, 460, 250, 120, weight=W_SEC)         # 8 撇（木）
    g.diag(505, 460, 750, 120, weight=W_SEC)         # 9 捺（木）
    return g


def g_809D() -> Glyph:
    """肝 U+809D —— 月 + 干（7 画）。

    分区：月 x215..470 / y60..820（撇 / 横折钩 / 两横）；
    干 x520..920（短横 y740 / 长横 y560 / 竖 x720）。
    """
    g = Glyph("uni809D", advance=1000, unicode=0x809D, note="肝：月 + 干")
    g.diag(255, 820, 215, 60, weight=W_MAIN)         # 1 撇（月）
    g.hbar(255, 470, 772, weight=W_MAIN)             # 2 横（月）
    g.vbar(470, 60, 820, weight=W_MAIN)              # 3 竖（月）
    g.diag(468, 62, 412, 118, weight=W_THIN)         # 钩
    g.hbar(250, 470, 540, weight=W_SEC)              # 4 横（月）
    g.hbar(245, 470, 330, weight=W_SEC)              # 5 横（月）
    g.hbar(560, 890, 740, weight=W_SEC)              # 6 横（干）
    g.hbar(520, 920, 560, weight=W_MAIN)             # 7 横（干）
    g.vbar(720, 100, 800, weight=W_MAIN)             # 8 竖（干）
    return g


def g_67F1() -> Glyph:
    """柱 U+67F1 —— 木 + 主（9 画）。

    分区：木 x60..330；主 x420..940（竖点 0 / 三横 / 竖）。
    """
    g = Glyph("uni67F1", advance=1000, unicode=0x67F1, note="柱：木 + 主")
    comp_木左(g, x=190, ybar=610)
    g.dot(680, 740, w=92, h=116, slant=SLANT_VERT)   # 1 丶（主，竖点）
    g.hbar(470, 890, 640, weight=W_SEC)              # 2 横（主）
    g.vbar(680, 130, 640, weight=W_MAIN)             # 3 竖（主）
    g.hbar(450, 910, 380, weight=W_SEC)              # 4 横（主）
    g.hbar(420, 940, 130, weight=W_MAIN)             # 5 横（主）
    return g


def g_6CBF() -> Glyph:
    """沿 U+6CBF —— 氵 + 㕣（8 画）。

    分区：氵 x60..250；㕣 = 丷（-14 / +14）+ 口，
    口 x400..900 / y60..480。
    """
    g = Glyph("uni6CBF", advance=1000, unicode=0x6CBF, note="沿：氵 + 㕣")
    comp_氵(g, x=150)
    g.dot(480, 640, w=90, h=110, slant=SLANT_DOT)    # 1 丶（丷左）
    g.dot(760, 640, w=90, h=110, slant=SLANT_NIE)    # 2 撇（丷右）
    comp_口(g, 400, 900, 60, 480, W_MAIN)
    return g


def g_5999() -> Glyph:
    """妙 U+5999 —— 女 + 少（7 画）。

    分区：女 x70..400 / y340..760（左偏旁，窄）；
    少 x460..940：竖 x690、左撇、右丶、长撇自右上斜落左下（不侵入女区）。
    """
    g = Glyph("uni5999", advance=1000, unicode=0x5999, note="妙：女 + 少")
    g.diag(320, 760, 190, 570, weight=W_SEC)         # 1 撇点（上段）
    g.diag(190, 570, 430, 360, weight=W_SEC)          # 2 撇点（下段）
    g.diag(400, 730, 110, 330, weight=W_SEC)         # 3 撇（女）
    g.hbar(60, 420, 500, weight=W_SEC)               # 4 横（女）
    g.vbar(690, 440, 810, weight=W_MAIN)             # 5 竖（少）
    g.diag(590, 630, 480, 460, weight=W_SEC)          # 6 左撇（少）
    g.dot(820, 590, w=88, h=108, slant=SLANT_DOT)    # 7 右丶（少）
    g.diag(905, 800, 545, 150, weight=W_SEC)         # 8 长撇（少）
    return g


def g_5FD8() -> Glyph:
    """忘 U+5FD8 —— 亡 + 心（7 画）。

    分区：亡 y380..820（竖点 0 / 横 y600 / 竖折）；
    心 y60..380（与忠里的心同套坐标）。
    """
    g = Glyph("uni5FD8", advance=1000, unicode=0x5FD8, note="忘：亡 + 心")
    g.dot(500, 762, w=92, h=116, slant=SLANT_VERT)   # 1 丶（亡，竖点）
    g.hbar(180, 820, 600, weight=W_MAIN)             # 2 横（亡）
    g.vbar(300, 380, 600, weight=W_MAIN)             # 3 竖（亡）
    g.hbar(300, 700, 428, weight=W_MAIN)             # 4 竖折的折（亡）
    comp_心(g, left=190, mid=480, right=810, hook_l=260, hook_r=720, base=170)
    return g


def g_5439() -> Glyph:
    """吹 U+5439 —— 口 + 欠（7 画）。

    分区：口 x70..330 / y280..660；欠 x400..910
    （顶撇 / 横折钩 / 人）。
    """
    g = Glyph("uni5439", advance=1000, unicode=0x5439, note="吹：口 + 欠")
    comp_口(g, 70, 330, 280, 660, W_MAIN)
    g.diag(500, 820, 410, 650, weight=W_MAIN)         # 1 撇（欠顶）
    g.hbar(460, 890, 706, weight=W_MAIN)             # 2 横（欠）
    g.diag(885, 706, 815, 606, weight=W_THIN)        # 3 横撇的撇（欠）
    g.diag(640, 620, 480, 240, weight=W_SEC)          # 4 撇（人）
    g.diag(650, 610, 910, 250, weight=W_SEC)          # 5 捺（人）
    return g


def g_5B9D() -> Glyph:
    """宝 U+5B9D —— 宀 + 玉（8 画）。

    分区：宀 y600..820；玉 x170..830（横 y540 / 横 y350 / 竖 / 底横 y140 / 丶）。
    """
    g = Glyph("uni5B9D", advance=1000, unicode=0x5B9D, note="宝：宀 + 玉")
    comp_宀(g, 60, 940, W_MAIN)
    g.hbar(240, 760, 540, weight=W_MAIN)             # 1 横（玉）
    g.hbar(220, 780, 350, weight=W_MAIN)             # 2 横（玉）
    g.vbar(500, 110, 540, weight=W_MAIN)             # 3 竖（玉）
    g.hbar(170, 830, 140, weight=W_MAIN)             # 4 横（玉）
    g.dot(690, 240, w=84, h=100, slant=SLANT_DOT)    # 5 丶（玉）
    return g


def g_67C4() -> Glyph:
    """柄 U+67C4 —— 木 + 丙（9 画）。

    分区：木 x60..330；丙 x400..940（顶横 y764 / 冂 y220..656 / 内人）。
    """
    g = Glyph("uni67C4", advance=1000, unicode=0x67C4, note="柄：木 + 丙")
    comp_木左(g, x=190, ybar=610)
    g.hbar(400, 940, 764, weight=W_MAIN)             # 1 横（丙顶）
    g.hbar(460, 900, 608, weight=W_MAIN)             # 2 横（冂顶）
    g.vbar(460, 220, 656, weight=W_MAIN)             # 3 竖（冂左）
    g.vbar(900, 220, 656, weight=W_MAIN)             # 4 竖（冂右）
    g.diag(680, 540, 570, 250, weight=W_SEC)         # 5 撇（人）
    g.diag(690, 530, 830, 260, weight=W_SEC)         # 6 捺（人）
    return g


def g_5C01() -> Glyph:
    """封 U+5C01 —— 圭 + 寸（9 画）。

    分区：圭 x80..540（竖 + 四横，y760/640/520/130）；
    寸 x600..930（横 y640 / 竖钩 x800 / 丶 -14）。
    """
    g = Glyph("uni5C01", advance=1000, unicode=0x5C01, note="封：圭 + 寸")
    g.hbar(120, 500, 760, weight=W_SEC)              # 1 横（士）
    g.vbar(310, 640, 806, weight=W_MAIN)             # 2 竖（士）
    g.hbar(90, 530, 640, weight=W_SEC)               # 3 横（士底）
    g.hbar(120, 500, 520, weight=W_SEC)              # 4 横（土）
    g.vbar(310, 130, 566, weight=W_MAIN)             # 5 竖（土）
    g.hbar(80, 540, 130, weight=W_SEC)               # 6 横（土底）
    g.hbar(600, 930, 640, weight=W_MAIN)             # 7 横（寸）
    g.vbar(800, 80, 820, weight=W_MAIN)              # 8 竖钩（寸）
    g.diag(798, 82, 740, 145, weight=W_THIN)         # 钩
    g.dot(690, 400, w=88, h=108, slant=SLANT_DOT)    # 9 丶（寸）
    return g


def g_7802() -> Glyph:
    """砂 U+7802 —— 石 + 少（9 画）。

    分区：石 x60..380（横 y760 / 撇 / 口 y60..470）；
    少 x460..940。
    """
    g = Glyph("uni7802", advance=1000, unicode=0x7802, note="砂：石 + 少")
    g.hbar(60, 380, 760, weight=W_MAIN)              # 1 横（石）
    g.diag(230, 760, 80, 540, weight=W_SEC)          # 2 撇（石）
    comp_口(g, 150, 350, 60, 470, W_MAIN)
    g.vbar(680, 520, 820, weight=W_MAIN)             # 3 竖（少）
    g.diag(580, 630, 460, 450, weight=W_SEC)          # 4 左撇（少）
    g.dot(810, 600, w=88, h=108, slant=SLANT_DOT)    # 5 右丶（少）
    g.diag(900, 800, 520, 200, weight=W_SEC)         # 6 长撇（少）
    return g


def g_5E8F() -> Glyph:
    """序 U+5E8F —— 广 + 予（7 画）。

    分区：广 y660..820（竖点 0 / 横 / 长撇）；
    予 x380..770（乛 / 丶 -14 / 横 / 竖钩）。
    """
    g = Glyph("uni5E8F", advance=1000, unicode=0x5E8F, note="序：广 + 予")
    g.dot(500, 762, w=92, h=116, slant=SLANT_VERT)   # 1 丶（广，竖点）
    g.hbar(90, 900, 660, weight=W_MAIN)              # 2 横（广）
    g.diag(240, 660, 110, 90, weight=W_SEC)          # 3 撇（广）
    g.hbar(420, 720, 560, weight=W_SEC)              # 4 横（乛）
    g.diag(715, 560, 640, 480, weight=W_THIN)        # 5 横撇的撇（乛）
    g.dot(545, 440, w=84, h=100, slant=SLANT_DOT)    # 6 丶（予）
    g.hbar(380, 770, 320, weight=W_SEC)              # 7 横（予）
    g.vbar(575, 90, 366, weight=W_MAIN)              # 8 竖钩（予）
    g.diag(573, 92, 515, 150, weight=W_THIN)         # 钩
    return g


def g_5F1F() -> Glyph:
    """弟 U+5F1F —— 丷 + 弓 + 丨 + 丿（7 画）。

    分区：丷 y689..801（-14 / +14）；弓 x280..700 / y300..638；
    长竖 x490 y160..760；末撇落向左下。
    """
    g = Glyph("uni5F1F", advance=1000, unicode=0x5F1F, note="弟：丷 + 弓")
    g.dot(390, 745, w=92, h=112, slant=SLANT_DOT)    # 1 丶（丷左）
    g.dot(610, 745, w=92, h=112, slant=SLANT_NIE)    # 2 撇（丷右）
    g.hbar(280, 700, 592, weight=W_SEC)              # 3 横（弓）
    g.vbar(700, 470, 638, weight=W_MAIN)             # 4 竖（弓折）
    g.hbar(280, 700, 470, weight=W_SEC)              # 5 横（弓中）
    g.vbar(280, 350, 470, weight=W_MAIN)             # 6 竖（弓）
    g.hbar(280, 700, 350, weight=W_SEC)              # 7 横（弓底）
    g.vbar(490, 160, 760, weight=W_MAIN)             # 8 竖（贯通）
    g.diag(492, 165, 235, 30, weight=W_SEC)          # 9 撇（末笔）
    return g


def g_65EC() -> Glyph:
    """旬 U+65EC —— 勹 + 日（6 画）。

    分区：勹 = 丿 (330,820)→(150,640) + 横折钩 x280..880；
    日 x320..760 / y180..660。
    """
    g = Glyph("uni65EC", advance=1000, unicode=0x65EC, note="旬：勹 + 日")
    g.diag(330, 820, 150, 640, weight=W_MAIN)         # 1 撇（勹）
    g.hbar(280, 880, 760, weight=W_MAIN)             # 2 横（勹）
    g.vbar(880, 180, 760, weight=W_MAIN)              # 3 竖（勹）
    g.diag(878, 182, 810, 250, weight=W_THIN)         # 钩
    comp_日(g, 320, 760, 180, 660, W_MAIN)
    return g


def g_65E8() -> Glyph:
    """旨 U+65E8 —— 匕 + 日（6 画）。

    分区：匕 y540..800（撇 + 竖弯钩）；日 x280..740 / y60..500。
    """
    g = Glyph("uni65E8", advance=1000, unicode=0x65E8, note="旨：匕 + 日")
    g.diag(480, 800, 200, 660, weight=W_SEC)          # 1 撇（匕）
    g.vbar(260, 540, 780, weight=W_MAIN)              # 2 竖（匕）
    g.hbar(260, 700, 588, weight=W_MAIN)             # 3 横（竖弯钩）
    g.diag(696, 590, 755, 655, weight=W_THIN)         # 钩
    comp_日(g, 280, 740, 60, 500, W_MAIN)
    return g


def g_5373() -> Glyph:
    """即 U+5373 —— 皀部 + 卩（7 画）。

    分区：左 x140..500（顶撇 / 框 / 中横 / 长竖折）；
    右卩 x600..880（横折钩 + 丨）。
    """
    g = Glyph("uni5373", advance=1000, unicode=0x5373, note="即：皀 + 卩")
    g.diag(300, 810, 140, 700, weight=W_SEC)          # 1 撇
    g.hbar(180, 500, 740, weight=W_MAIN)             # 2 横（框顶）
    g.vbar(500, 440, 740, weight=W_MAIN)             # 3 竖（框右）
    g.hbar(180, 500, 600, weight=W_SEC)              # 4 横（中）
    g.vbar(180, 120, 600, weight=W_MAIN)             # 5 竖（长）
    g.hbar(180, 380, 168, weight=W_MAIN)             # 6 竖折的折
    g.hbar(600, 880, 740, weight=W_MAIN)             # 7 横（卩）
    g.vbar(880, 400, 740, weight=W_MAIN)              # 8 竖（卩）
    g.diag(878, 402, 812, 468, weight=W_THIN)         # 钩
    g.vbar(690, 340, 740, weight=W_MAIN)             # 9 竖（卩）
    return g


def g_6D17() -> Glyph:
    """洗 U+6D17 —— 氵 + 先（9 画）。

    分区：氵 x60..250；先 x350..940（撇 / 短横 / 竖 / 长横 / 儿）。
    """
    g = Glyph("uni6D17", advance=1000, unicode=0x6D17, note="洗：氵 + 先")
    comp_氵(g, x=150)
    g.diag(480, 800, 370, 680, weight=W_SEC)          # 1 撇（先）
    g.hbar(450, 830, 640, weight=W_SEC)              # 2 横（先）
    g.vbar(630, 460, 640, weight=W_MAIN)             # 3 竖（先）
    g.hbar(360, 910, 460, weight=W_MAIN)             # 4 横（先）
    g.diag(570, 400, 390, 40, weight=W_SEC)          # 5 撇（儿）
    g.vbar(790, 60, 400, weight=W_MAIN)              # 6 竖（儿）
    g.hbar(790, 910, 108, weight=W_MAIN)             # 7 横（竖弯钩）
    g.diag(906, 110, 940, 175, weight=W_THIN)         # 钩
    return g


def g_67F3() -> Glyph:
    """柳 U+67F3 —— 木 + 卯（9 画）。

    分区：木 x60..330；卯 x400..940（左：撇 + 竖提；右：撇 + 横折钩 + 丨）。
    """
    g = Glyph("uni67F3", advance=1000, unicode=0x67F3, note="柳：木 + 卯")
    comp_木左(g, x=190, ybar=610)
    g.diag(570, 810, 430, 690, weight=W_SEC)          # 1 撇（卯左）
    g.vbar(445, 390, 690, weight=W_MAIN)             # 2 竖（卯左）
    g.diag(443, 392, 565, 470, weight=W_THIN)        # 提（卯左）
    g.diag(800, 810, 660, 660, weight=W_SEC)          # 3 撇（卯右）
    g.hbar(650, 900, 640, weight=W_MAIN)             # 4 横（卯右）
    g.vbar(900, 300, 640, weight=W_MAIN)              # 5 竖（卯右）
    g.diag(898, 302, 832, 368, weight=W_THIN)         # 钩
    g.vbar(720, 300, 640, weight=W_MAIN)             # 6 竖（卯右）
    return g


def g_820E() -> Glyph:
    """舎 U+820E —— 人 + 干 + 口（8 画）。

    分区：人 y670..820（撇捺）；短横 y570 / 竖 x500；
    长横 y380；口 x320..680 / y40..300。
    """
    g = Glyph("uni820E", advance=1000, unicode=0x820E, note="舎：人 + 干 + 口")
    g.diag(500, 820, 260, 680, weight=W_SEC)          # 1 撇（人）
    g.diag(505, 815, 740, 680, weight=W_SEC)          # 2 捺（人）
    g.hbar(350, 650, 570, weight=W_SEC)              # 3 横（干）
    g.vbar(500, 400, 570, weight=W_MAIN)             # 4 竖（干）
    g.hbar(240, 760, 380, weight=W_MAIN)             # 5 横（干下）
    comp_口(g, 320, 680, 40, 300, W_MAIN)
    return g


def g_5146() -> Glyph:
    """兆 U+5146 —— 6 画。

    骨架照参照字（M PLUS 1p Black）：左二短撇 + 中部长撇（底端向左微曲）
    + 右二短撇 + 右竖弯钩（底端向右挑）。
    分区：左二撇 x100..300；中长撇 x330..430；右二撇 x560..740；
    右竖弯钩 x820..930。
    """
    g = Glyph("uni5146", advance=1000, unicode=0x5146, note="兆：")
    g.diag(320, 810, 140, 675, weight=W_MAIN)         # 1 撇（左上）
    g.diag(265, 635, 85, 500, weight=W_MAIN)          # 2 撇（左中）
    g.diag(440, 790, 335, 80, weight=W_MAIN)          # 3 长撇（中）
    g.diag(700, 810, 540, 675, weight=W_MAIN)         # 4 撇（右上）
    g.diag(735, 635, 560, 500, weight=W_MAIN)         # 5 撇（右中）
    g.vbar(845, 105, 800, weight=W_MAIN)              # 6 竖（右）
    g.hbar(845, 930, 153, weight=W_MAIN)             # 竖弯钩的底（右）
    g.diag(926, 155, 940, 225, weight=W_THIN)         # 钩（右）
    return g


def g_5E8A() -> Glyph:
    """床 U+5E8A —— 广 + 木（7 画）。

    分区：广 y660..820（竖点 0 / 横 / 长撇）；
    木 x320..790 / y60..560。
    """
    g = Glyph("uni5E8A", advance=1000, unicode=0x5E8A, note="床：广 + 木")
    g.dot(500, 762, w=92, h=116, slant=SLANT_VERT)   # 1 丶（广，竖点）
    g.hbar(90, 900, 660, weight=W_MAIN)              # 2 横（广）
    g.diag(240, 660, 110, 90, weight=W_SEC)          # 3 撇（广）
    comp_木下(g, x=555, top=548, bot=60, ybar=500)
    return g


def g_7551() -> Glyph:
    """畑 U+7551 —— 火 + 田（9 画）。

    分区：火 x100..390（两点 + 撇 + 捺）；
    田 x440..900 / y120..760。
    """
    g = Glyph("uni7551", advance=1000, unicode=0x7551, note="畑：火 + 田")
    g.dot(130, 620, w=88, h=108, slant=SLANT_DOT)    # 1 丶（火左）
    g.dot(340, 620, w=88, h=108, slant=SLANT_NIE)    # 2 撇（火右）
    g.diag(240, 780, 100, 180, weight=W_SEC)         # 3 撇（火）
    g.diag(235, 560, 390, 180, weight=W_SEC)         # 4 捺（火）
    comp_田(g, 440, 900, 120, 760, W_MAIN)
    return g


def g_62B5() -> Glyph:
    """抵 U+62B5 —— 扌 + 氐（8 画）。

    分区：扌 x60..300；氐 x350..930
    （顶撇 / 竖提 / 横 / 长撇 / 右下丶 -14）。
    """
    g = Glyph("uni62B5", advance=1000, unicode=0x62B5, note="抵：扌 + 氐")
    comp_扌(g, x=185)
    g.diag(600, 810, 430, 730, weight=W_SEC)          # 1 撇（氐）
    g.vbar(440, 260, 720, weight=W_MAIN)             # 2 竖（氐）
    g.diag(438, 262, 570, 330, weight=W_THIN)        # 提（氐）
    g.hbar(370, 930, 600, weight=W_MAIN)             # 3 横（氐）
    g.diag(800, 620, 560, 70, weight=W_SEC)          # 4 长撇（氐）
    g.dot(860, 300, w=84, h=100, slant=SLANT_DOT)    # 5 丶（氐）
    return g


def g_795D() -> Glyph:
    """祝 U+795D —— 礻 + 兄（9 画）。

    分区：礻 x80..330（丶 -14 / 横撇 / 竖 / 右丶 -14）；
    兄 x450..910（口 y460..790 + 儿）。
    """
    g = Glyph("uni795D", advance=1000, unicode=0x795D, note="祝：礻 + 兄")
    g.dot(200, 760, w=92, h=116, slant=SLANT_DOT)    # 1 丶（礻）
    g.hbar(80, 330, 620, weight=W_SEC)               # 2 横（礻）
    g.diag(325, 620, 150, 470, weight=W_THIN)        # 3 横撇的撇（礻）
    g.vbar(200, 80, 620, weight=W_MAIN)              # 4 竖（礻）
    g.dot(300, 430, w=84, h=100, slant=SLANT_DOT)    # 5 丶（礻）
    comp_口(g, 500, 880, 460, 790, W_MAIN)
    g.diag(620, 460, 450, 80, weight=W_SEC)          # 6 撇（儿）
    g.vbar(790, 80, 460, weight=W_MAIN)              # 7 竖（儿）
    g.hbar(790, 910, 128, weight=W_MAIN)             # 8 横（竖弯钩）
    g.diag(906, 130, 940, 190, weight=W_THIN)         # 钩
    return g


def g_67D4() -> Glyph:
    """柔 U+67D4 —— 矛 + 木（9 画）。

    分区：矛 y390..816（乛 / 丶 -14 / 横 / 竖钩 / 长撇）；
    木 x280..760 / y40..378。
    """
    g = Glyph("uni67D4", advance=1000, unicode=0x67D4, note="柔：矛 + 木")
    g.hbar(200, 800, 770, weight=W_SEC)              # 1 横（乛）
    g.diag(795, 770, 700, 700, weight=W_THIN)        # 2 横撇的撇（乛）
    g.dot(430, 690, w=84, h=100, slant=SLANT_DOT)    # 3 丶（矛）
    g.hbar(150, 870, 600, weight=W_MAIN)             # 4 横（矛）
    g.vbar(520, 390, 600, weight=W_MAIN)             # 5 竖钩（矛）
    g.diag(518, 392, 450, 460, weight=W_THIN)        # 钩
    g.diag(830, 700, 480, 430, weight=W_SEC)         # 6 撇（矛）
    comp_木下(g, x=520, top=330, bot=40, ybar=330)
    return g


# ---------------------------------------------------------------- 组装


def build() -> list[Glyph]:
    return [
        g_6749(), g_91CC(), g_8352(), g_59A5(), g_5A01(), g_5FE0(), g_663C(), g_8336(),
        g_809D(), g_67F1(), g_6CBF(), g_5999(), g_5FD8(), g_5439(), g_5B9D(), g_67C4(),
        g_5C01(), g_7802(), g_5E8F(), g_5F1F(), g_65EC(), g_65E8(), g_5373(), g_6D17(),
        g_67F3(), g_820E(), g_5146(), g_5E8A(), g_7551(), g_62B5(), g_795D(), g_67D4(),
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-013.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
