"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-014。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

批内设计取舍（GLY-001 / GLY-003 / GLY-004 / GLY-006）：
* 字面框 x 60..940、y 0..820，advance 1000，与繁体汉字同档，便于中英日混排。
* 笔画权重四档：主 96 / 次 92 / 细 84 / 点 84。
  6 画字（衣、尽）走主档 96；8–9 画字在拥挤处用次档 92、细档 84 局部减重，
  避免同批里出现「有的太轻、有的太闷」。
* 横竖撇捺一律平切硬边（hkbuild 的 hbar / vbar / diag）；
  点与短撇一律用斜切平行四边形（g.dot），斜切档位只用 -14 / 0 / 14 / 26，
  同类部件全批同档：
    丶（右下的点）→ -14；丿（左下的点）→ +14；短撇（氵上点等）→ 26；竖点 → 0。
* 笔画角度照《常用漢字表》标准骨架，不改斜率；只调重量、端点、落位与大小。
* 同一部件（氵、艹、火、阝、忄、日、目、且、力、子、木、且）在批内复用同一套
  坐标与笔画拆法，只做位置与大小的光学校正。
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
W_LIGHT = 76  # 局部减重（GLY-001 小空腔）

TOP = 820.0
BASE = 0.0
L = 60.0
R = 940.0
MID = 500.0

# 斜切档位（全批唯一四个值）
SL_DOT = -14      # 丶：右下方向的点
SL_PIE = 14       # 丿：左下方向的点
SL_SHORT = 26     # 短撇
SL_VERT = 0       # 竖点


# ---------------------------------------------------------------- 基础构件


def hbar_top(g, x1, x2, ink_top=TOP, weight=W_MAIN):
    """横画：墨迹上缘对齐 ink_top，中心线内缩半个笔画宽。"""
    g.hbar(x1, x2, ink_top - weight / 2.0, weight=weight)


def hbar_base(g, x1, x2, ink_base=BASE, weight=W_MAIN):
    """横画：墨迹下缘对齐 ink_base。"""
    g.hbar(x1, x2, ink_base + weight / 2.0, weight=weight)


def hbar_at(g, x1, x2, cy, weight=W_MAIN):
    """横画：中心线在 cy。"""
    g.hbar(x1, x2, cy, weight=weight)


def kusa(g, x1=230.0, x2=790.0, top=TOP, weight=W_MAIN, drop=270.0):
    """艹：一横 + 两竖（竖穿过横，竖头略出横面）。drop = 竖的总长。"""
    hbar_top(g, x1, x2, top, weight)
    g.vbar(x1 + 105.0, top - drop, top, weight=weight)
    g.vbar(x2 - 105.0, top - drop, top, weight=weight)


def sanzui(g, x=150.0, top=TOP, bottom=BASE, weight=W_SEC):
    """氵（左三点水）：上点/中点用短撇档 26，末笔为提（右上斜画）。"""
    g.dot(x + 15.0, top - 120.0, w=88, h=112, slant=26)
    g.dot(x - 20.0, top - 330.0, w=88, h=112, slant=26)
    g.diag(x - 35.0, bottom + 120.0, x + 115.0, bottom + 320.0, weight=weight)


def kozato(g, x=108.0, top=TOP, bottom=BASE):
    """阝（左耳刀）：一竖 + 上部三折的窄弯钩（留出白缝，不糊成一团）。"""
    g.vbar(x, bottom, top, weight=W_MAIN)
    g.diag(x, top - 25.0, x + 162.0, top - 75.0, weight=W_THIN)
    g.diag(x + 162.0, top - 75.0, x + 42.0, top - 165.0, weight=W_THIN)
    g.diag(x + 42.0, top - 165.0, x + 157.0, top - 245.0, weight=W_THIN)
    g.diag(x + 157.0, top - 245.0, x + 32.0, top - 320.0, weight=W_THIN)


def hi(g, x1, x2, y_bot, y_top):
    """火：左点（-14）+ 右短撇（+14）+ 长撇 + 捺。"""
    w = x2 - x1
    g.dot(x1 + 0.22 * w, y_top - 140.0, w=88, h=112, slant=-14)
    g.dot(x1 + 0.78 * w, y_top - 70.0, w=88, h=112, slant=14)
    g.diag(x1 + 0.42 * w, y_top - 60.0, x1 + 0.03 * w, y_bot, weight=W_MAIN)
    g.diag(x1 + 0.49 * w, y_top - 80.0, x1 + 0.97 * w, y_bot, weight=W_MAIN)


def ki(g, x1, x2, y_bot, y_top):
    """木：一 + 丨 + 撇 + 捺。"""
    w = x2 - x1
    hbar_top(g, x1 + 10.0, x2 - 10.0, y_top - 180.0, W_MAIN)
    g.vbar(x1 + 0.48 * w, y_bot, y_top, weight=W_MAIN)
    g.diag(x1 + 0.45 * w, y_top - 210.0, x1 + 0.03 * w, y_bot, weight=W_MAIN)
    g.diag(x1 + 0.52 * w, y_top - 220.0, x1 + 0.97 * w, y_bot + 60.0, weight=W_MAIN)


def ko(g, x1, x2, y_bot, y_top):
    """子：乛（横撇）+ 竖钩 + 一。"""
    w = x2 - x1
    g.hbar(x1 + 20.0, x1 + 0.92 * w, y_top - 48.0, weight=W_MAIN)
    g.diag(x1 + 0.92 * w, y_top - 60.0, x1 + 0.58 * w, y_top - 200.0, weight=W_MAIN)
    g.vbar(x1 + 0.55 * w, y_bot + 30.0, y_top - 60.0, weight=W_MAIN)
    g.diag(x1 + 0.55 * w, y_bot + 30.0, x1 + 0.40 * w, y_bot + 110.0, weight=W_THIN)
    g.hbar(x1, x1 + 0.86 * w, y_top - 300.0, weight=W_MAIN)


def chikara(g, x1, x2, y_bot, y_top):
    """力：横折钩 + 撇。"""
    w = x2 - x1
    g.hbar(x1, x1 + 0.95 * w, y_top - 48.0, weight=W_MAIN)
    g.vbar(x1 + 0.95 * w, y_bot, y_top, weight=W_MAIN)
    g.diag(x1 + 0.95 * w, y_bot + 10.0, x1 + 0.76 * w, y_bot + 95.0, weight=W_THIN)
    g.diag(x1 + 0.48 * w, y_top + 60.0, x1 + 0.04 * w, y_bot, weight=W_MAIN)


def nichi(g, x1, x2, y_bot, y_top, weight=W_MAIN, mid_frac=0.54):
    """日：丨 + 𠃍（横折）+ 中横 + 下横。x1/x2 为竖画中心线。"""
    g.vbar(x1, y_bot, y_top, weight=weight)
    g.hbar(x1, x2, y_top - weight / 2.0, weight=weight)
    g.vbar(x2, y_bot, y_top, weight=weight)
    cy = y_bot + (y_top - y_bot) * mid_frac
    g.hbar(x1, x2, cy, weight=weight)
    g.hbar(x1, x2, y_bot + weight / 2.0, weight=weight)


def me(g, x1, x2, y_bot, y_top, weight=W_MAIN):
    """目：丨 + 𠃍（横折）+ 两中横 + 下横。"""
    g.vbar(x1, y_bot, y_top, weight=weight)
    g.hbar(x1, x2, y_top - weight / 2.0, weight=weight)
    g.vbar(x2, y_bot, y_top, weight=weight)
    span = y_top - y_bot
    g.hbar(x1, x2, y_bot + span * 0.40, weight=weight)
    g.hbar(x1, x2, y_bot + span * 0.68, weight=weight)
    g.hbar(x1, x2, y_bot + weight / 2.0, weight=weight)


def soko(g, x1, x2, y_bot, y_top, weight=W_MAIN):
    """且：丨 + 𠃍（横折）+ 两中横 + 底横（底横左右出头）。"""
    g.vbar(x1, y_bot, y_top, weight=weight)
    g.hbar(x1, x2, y_top - weight / 2.0, weight=weight)
    g.vbar(x2, y_bot, y_top, weight=weight)
    span = y_top - y_bot
    g.hbar(x1, x2, y_bot + span * 0.42, weight=weight)
    g.hbar(x1, x2, y_bot + span * 0.70, weight=weight)
    g.hbar(x1 - 50.0, x2 + 50.0, y_bot + weight / 2.0, weight=weight)


def tesagari(g, x1, x2, y_top, weight=W_MAIN):
    """冖：左短竖 + 横 + 右短竖。"""
    g.vbar(x1, y_top - 110.0, y_top, weight=weight)
    g.hbar(x1, x2, y_top - weight / 2.0, weight=weight)
    g.vbar(x2, y_top - 110.0, y_top, weight=weight)


# ---------------------------------------------------------------- 各字


def g_mo():
    """茂 8画 艹 + 戊。

    部件分区：艹 y 550..820（横 x 230..790，竖 x 335 / 685）；
    戊 y 40..655。
    笔画清单：
      艹横   hbar_top(230, 790, 820, 96)
      艹左竖 vbar(335, 550, 820, 96)
      艹右竖 vbar(685, 550, 820, 96)
      戊长撇 diag(430, 655, 140, 40)      起笔在横之上
      戊横   hbar_top(300, 720, 590, 96)
      戊斜钩 diag(700, 650, 870, 80)
      戊短横 hbar_top(360, 600, 430, 84)
      戊交叉撇 diag(790, 520, 420, 90, 92)
    """
    g = Glyph("uni8302", advance=1000, unicode=0x8302, note="茂 8画 艹+戊")
    kusa(g, 250.0, 770.0, drop=210.0)
    g.diag(470.0, 600.0, 120.0, 20.0, weight=W_MAIN)
    hbar_top(g, 100.0, 900.0, 540.0, W_MAIN)
    g.diag(740.0, 570.0, 890.0, 30.0, weight=W_MAIN)
    hbar_top(g, 300.0, 560.0, 420.0, W_THIN)
    g.diag(800.0, 470.0, 420.0, 60.0, weight=W_SEC)
    return g


def g_se():
    """昔 8画 廿 + 日。

    部件分区：廿 y 640..820（上横 x 230..770，两竖 x 330 / 670，下横 x 230..770）；
    日 y 0..520（竖 x 300 / 700）。
    笔画清单：
      廿竖   vbar(330, 700, 820) / vbar(670, 700, 820)
      廿上横 hbar_top(230, 770, 780, 96)
      廿下横 hbar_top(230, 770, 640, 96)
      日     nichi(300, 700, 0, 520)
    """
    g = Glyph("uni6614", advance=1000, unicode=0x6614, note="昔 8画 廿+日")
    g.vbar(330.0, 640.0, 820.0, weight=W_MAIN)
    g.vbar(670.0, 640.0, 820.0, weight=W_MAIN)
    hbar_top(g, 230.0, 770.0, 780.0, W_MAIN)
    hbar_top(g, 230.0, 770.0, 640.0, W_MAIN)
    nichi(g, 300.0, 700.0, 0.0, 520.0, W_MAIN, mid_frac=0.54)
    return g


def g_chi():
    """茨 9画 艹 + 次（冫 + 欠）。

    部件分区：艹 y 550..820（横 x 180..820，竖 x 285 / 715）；
    冫 x 90..280 y 110..420；欠 x 320..940 y 40..660。
    笔画清单：
      艹      kusa(180, 820)
      冫上点  dot(170, 560, slant -14)
      冫提    diag(110, 280, 270, 400)
      欠短撇  diag(600, 620, 480, 450)
      欠横撇  hbar_top(520, 880, 520, 96) + diag(880, 500, 760, 330)
      欠长撇  diag(600, 430, 330, 40)
      欠捺    diag(640, 420, 930, 40)
    """
    g = Glyph("uni8328", advance=1000, unicode=0x8328, note="茨 9画 艹+次")
    kusa(g, 180.0, 820.0)
    g.dot(170.0, 560.0, w=88, h=112, slant=-14)
    g.diag(110.0, 300.0, 270.0, 420.0, weight=W_SEC)
    g.diag(464.0, 640.0, 354.0, 480.0, weight=W_MAIN)
    hbar_top(g, 379.0, 940.0, 460.0, W_MAIN)
    g.diag(930.0, 440.0, 700.0, 250.0, weight=W_MAIN)
    g.diag(513.0, 440.0, 342.0, 40.0, weight=W_MAIN)
    g.diag(660.0, 250.0, 940.0, 40.0, weight=W_MAIN)
    return g


def g_sai():
    """斉 8画 丶 + 一 + 乂 + 日。

    部件分区：丶 y 710..820（竖点）；一 y 652..700（x 60..940）；
    乂 y 40..640（丿 x 70..660、捺 x 340..930，中点相交于 500,483）；
    日 x 440..570 y 0..330（居中于乂之下）。
    笔画清单：
      竖点 dot(500, 765, slant 0)
      一   hbar_top(60, 940, 700, 96)
      乂撇 diag(660, 640, 70, 60, 96)
      乂捺 diag(340, 640, 930, 60, 96)
      日   nichi(440, 570, 0, 330, 96, 0.52)
    """
    g = Glyph("uni6589", advance=1000, unicode=0x6589, note="斉 8画 亠+乂+日")
    g.dot(500.0, 765.0, w=84, h=110, slant=0)
    hbar_top(g, 60.0, 940.0, 700.0, W_MAIN)
    g.diag(660.0, 640.0, 70.0, 60.0, weight=W_MAIN)
    g.diag(340.0, 640.0, 930.0, 60.0, weight=W_MAIN)
    nichi(g, 440.0, 570.0, 0.0, 330.0, W_MAIN, mid_frac=0.52)
    return g


def g_i():
    """衣 6画 亠 + 丿 + 竖提 + 丿 + 捺。

    部件分区：亠 y 642..820（竖点 + 一）；下衣身 y 30..640。
    笔画清单：
      竖点 dot(500, 760, slant 0)
      一   hbar_top(60, 940, 690, 96)
      撇   diag(580, 640, 290, 380, 96)
      竖   vbar(440, 150, 640, 96)
      竖提 diag(440, 160, 520, 230, 84)
      短撇 diag(430, 260, 170, 30, 92)
      捺   diag(500, 470, 910, 30, 96)
    """
    g = Glyph("uni8863", advance=1000, unicode=0x8863, note="衣 6画 亠+衣身")
    g.dot(500.0, 760.0, w=84, h=110, slant=0)
    hbar_top(g, 60.0, 940.0, 690.0, W_MAIN)
    g.diag(580.0, 640.0, 290.0, 380.0, weight=W_MAIN)
    g.vbar(440.0, 150.0, 640.0, weight=W_MAIN)
    g.diag(440.0, 160.0, 520.0, 230.0, weight=W_THIN)
    g.diag(430.0, 260.0, 170.0, 30.0, weight=W_SEC)
    g.diag(500.0, 470.0, 910.0, 30.0, weight=W_MAIN)
    return g


def g_kata():
    """肩 8画 戸 + 月。

    部件分区：戸 x 60..600 y 120..820（一 + 尸身 + 长撇）；
    月 x 640..890 y 0..760（丿 + 𠃍 + 两中横）。
    笔画清单：
      戸横   hbar_top(90, 600, 820, 96)
      戸身横 hbar_top(150, 560, 700, 92)
      戸身竖 vbar(560, 300, 700, 92)
      戸内横 hbar_top(150, 560, 520, 84)
      戸长撇 diag(160, 700, 70, 120, 96)
      月撇   vbar(640, 0, 760, 96)
      月横   hbar_top(640, 890, 760, 96)
      月折   vbar(890, 0, 760, 96)
      月中横 hbar_top(640, 890, 540, 84)
      月中横2 hbar_top(640, 890, 340, 84)
    """
    g = Glyph("uni80A9", advance=1000, unicode=0x80A9, note="肩 8画 戸+月")
    hbar_top(g, 90.0, 600.0, 820.0, W_MAIN)
    hbar_top(g, 150.0, 560.0, 700.0, W_SEC)
    g.vbar(560.0, 300.0, 700.0, weight=W_SEC)
    hbar_top(g, 150.0, 560.0, 520.0, W_THIN)
    g.diag(160.0, 700.0, 70.0, 120.0, weight=W_MAIN)
    g.vbar(640.0, 0.0, 760.0, weight=W_MAIN)
    hbar_top(g, 640.0, 890.0, 760.0, W_MAIN)
    g.vbar(890.0, 0.0, 760.0, weight=W_MAIN)
    hbar_top(g, 640.0, 890.0, 540.0, W_THIN)
    hbar_top(g, 640.0, 890.0, 340.0, W_THIN)
    return g


def g_do():
    """怒 9画 奴（女 + 又）+ 心。

    部件分区：奴 y 180..700（女 x 140..500、又 x 560..930）；
    心 y 0..420（点 x 140 / 450 / 650，卧钩 x 290..700）。
    笔画清单：
      女撇点 diag(350, 640, 240, 400) + diag(240, 400, 420, 180, 96)
      女撇   diag(420, 620, 180, 120, 96)
      女横   hbar_top(140, 500, 380, 96)
      又横撇 hbar_top(560, 900, 640, 96) + diag(900, 620, 600, 180, 96)
      又捺   diag(620, 620, 930, 180, 96)
      心左点 dot(140, 300, slant -14)
      心卧钩 diag(290, 270, 690, 180, 96) + diag(690, 185, 620, 275, 84)
      心中点 dot(450, 380, slant -14)
      心右点 dot(650, 390, slant +14)
    """
    g = Glyph("uni6012", advance=1000, unicode=0x6012, note="怒 9画 奴+心")
    # 女：撇点（先左下再右下）+ 撇 + 横
    g.diag(280.0, 815.0, 215.0, 600.0, weight=W_MAIN)
    g.diag(215.0, 600.0, 470.0, 430.0, weight=W_MAIN)
    g.diag(480.0, 800.0, 105.0, 440.0, weight=W_MAIN)
    hbar_top(g, 90.0, 520.0, 620.0, W_MAIN)
    # 又：横撇 + 捺
    hbar_top(g, 570.0, 900.0, 780.0, W_MAIN)
    g.diag(895.0, 760.0, 620.0, 420.0, weight=W_MAIN)
    g.diag(610.0, 760.0, 930.0, 420.0, weight=W_MAIN)
    # 心：左点 + 卧钩（浅碗）+ 中点 + 右点
    g.dot(160.0, 250.0, w=92, h=116, slant=-14)
    g.diag(280.0, 195.0, 560.0, 275.0, weight=W_MAIN)
    g.diag(560.0, 275.0, 860.0, 175.0, weight=W_MAIN)
    g.dot(400.0, 110.0, w=92, h=116, slant=-14)
    g.dot(640.0, 110.0, w=92, h=116, slant=14)
    return g


def g_ei():
    """泳 8画 氵 + 永。

    部件分区：氵 x 60..300 y 0..820；永 x 330..940 y 30..820。
    笔画清单：
      氵   sanzui(150)
      竖点 dot(600, 760, slant 0)
      竖钩 vbar(600, 120, 640, 96) + diag(600, 125, 545, 185, 84)
      横撇 hbar_top(590, 790, 580, 92) + diag(790, 560, 650, 400, 92)
      撇   diag(540, 480, 330, 60, 96)
      捺   diag(620, 470, 900, 40, 96)
    """
    g = Glyph("uni6CF3", advance=1000, unicode=0x6CF3, note="泳 8画 氵+永")
    sanzui(g, 150.0)
    g.dot(600.0, 760.0, w=84, h=110, slant=0)
    g.vbar(600.0, 120.0, 640.0, weight=W_MAIN)
    g.diag(600.0, 125.0, 545.0, 185.0, weight=W_THIN)
    hbar_top(g, 590.0, 790.0, 580.0, W_SEC)
    g.diag(790.0, 560.0, 650.0, 400.0, weight=W_SEC)
    g.diag(540.0, 480.0, 330.0, 60.0, weight=W_MAIN)
    g.diag(620.0, 470.0, 900.0, 40.0, weight=W_MAIN)
    return g


def g_so():
    """祖 9画 礻 + 且。

    部件分区：礻 x 60..360 y 60..820（点 + 横撇 + 竖 + 右点）；
    且 x 400..940 y 0..760。
    笔画清单：
      礻点   dot(190, 770, slant 0)
      礻横撇 hbar_top(100, 330, 620, 92) + diag(330, 600, 200, 470, 92)
      礻竖   vbar(200, 60, 470, 96)
      礻右点 dot(310, 400, slant -14)
      且     soko(450, 890, 0, 760)
    """
    g = Glyph("uni7956", advance=1000, unicode=0x7956, note="祖 9画 礻+且")
    g.dot(190.0, 770.0, w=84, h=110, slant=0)
    hbar_top(g, 100.0, 330.0, 620.0, W_SEC)
    g.diag(330.0, 600.0, 200.0, 470.0, weight=W_SEC)
    g.vbar(200.0, 60.0, 470.0, weight=W_MAIN)
    g.dot(310.0, 400.0, w=84, h=112, slant=-14)
    soko(g, 450.0, 890.0, 0.0, 760.0, W_MAIN)
    return g


def g_haku():
    """泊 8画 氵 + 白。

    部件分区：氵 x 60..300；白 x 340..940（丿 + 日 y 0..640）。
    笔画清单：
      氵   sanzui(150)
      白撇 diag(520, 780, 400, 680, 92)
      日   nichi(430, 870, 0, 640, 96, 0.55)
    """
    g = Glyph("uni6CCA", advance=1000, unicode=0x6CCA, note="泊 8画 氵+白")
    sanzui(g, 150.0)
    g.diag(520.0, 780.0, 400.0, 680.0, weight=W_SEC)
    nichi(g, 430.0, 870.0, 0.0, 640.0, W_MAIN, mid_frac=0.55)
    return g


def g_jin():
    """尽 6画 尺 + 两点。

    部件分区：尺 y 200..760（𠃍 x 200..700 + 内横 + 撇 + 捺）；
    两点 y 60..380（x 340..430）。
    笔画清单：
      尺横折 hbar_top(200, 700, 760, 96) + vbar(700, 560, 760, 96)
      尺内横 hbar_top(200, 700, 560, 92)
      尺撇   diag(250, 740, 110, 240, 96)
      尺捺   diag(620, 540, 880, 200, 96)
      冫上点 dot(360, 320, slant -14)
      冫下点 dot(390, 130, slant -14)
    """
    g = Glyph("uni5C3D", advance=1000, unicode=0x5C3D, note="尽 6画 尺+两点")
    hbar_top(g, 200.0, 700.0, 760.0, W_MAIN)
    g.vbar(700.0, 560.0, 760.0, weight=W_MAIN)
    hbar_top(g, 200.0, 700.0, 560.0, W_SEC)
    g.diag(250.0, 740.0, 110.0, 240.0, weight=W_MAIN)
    g.diag(620.0, 540.0, 880.0, 200.0, weight=W_MAIN)
    g.dot(360.0, 320.0, w=88, h=112, slant=-14)
    g.dot(390.0, 130.0, w=88, h=112, slant=-14)
    return g


def g_hai():
    """杯 8画 木 + 不。

    部件分区：木 x 60..460 y 0..800；不 x 490..940 y 40..760。
    笔画清单：
      木   ki(60, 460, 0, 800)
      不一 hbar_top(490, 940, 760, 96)
      不撇 diag(720, 740, 540, 400, 96)
      不竖 vbar(740, 60, 740, 96)
      不点 dot(860, 480, slant -14)
    """
    g = Glyph("uni676F", advance=1000, unicode=0x676F, note="杯 8画 木+不")
    ki(g, 60.0, 460.0, 0.0, 800.0)
    hbar_top(g, 490.0, 940.0, 760.0, W_MAIN)
    g.diag(720.0, 740.0, 540.0, 400.0, weight=W_MAIN)
    g.vbar(740.0, 60.0, 740.0, weight=W_MAIN)
    g.dot(860.0, 480.0, w=84, h=112, slant=-14)
    return g


def g_ko():
    """孤 9画 子 + 瓜。

    部件分区：子 x 60..470 y 0..520；瓜 x 480..940 y 30..790。
    笔画清单：
      子   ko(60, 470, 0, 520)
      瓜长撇 diag(610, 770, 490, 40, 96)
      瓜竖   vbar(700, 140, 600, 96)
      瓜竖提 vbar(790, 100, 560, 92) + diag(790, 110, 850, 160, 84)
      瓜点   dot(830, 400, slant -14)
      瓜捺   diag(700, 520, 930, 40, 96)
    """
    g = Glyph("uni5B64", advance=1000, unicode=0x5B64, note="孤 9画 子+瓜")
    ko(g, 60.0, 470.0, 0.0, 520.0)
    # 瓜：长撇 + 中竖 + 竖提 + 捺
    g.diag(700.0, 790.0, 520.0, 30.0, weight=W_MAIN)
    g.vbar(780.0, 320.0, 700.0, weight=W_SEC)
    g.vbar(870.0, 180.0, 600.0, weight=W_SEC)
    g.diag(870.0, 190.0, 925.0, 250.0, weight=W_THIN)
    g.diag(800.0, 640.0, 930.0, 30.0, weight=W_MAIN)
    return g


def g_en():
    """炎 8画 火 + 火（上下同构，全批共用 hi 构件）。

    部件分区：上火 y 400..820；下火 y 0..400。
    笔画清单：
      上火 hi(60, 940, 400, 820)
      下火 hi(60, 940, 0, 400)
    """
    g = Glyph("uni708E", advance=1000, unicode=0x708E, note="炎 8画 火+火")
    hi(g, 60.0, 940.0, 400.0, 820.0)
    hi(g, 60.0, 940.0, 0.0, 400.0)
    return g


def g_ju():
    """寿 7画 三 + 丿 + 寸。

    部件分区：上三横 y 532..820；长撇贯穿；寸 y 0..400 x 330..880。
    笔画清单：
      横一 hbar_top(280, 720, 820, 96)
      横二 hbar_top(230, 770, 700, 96)
      横三 hbar_top(180, 820, 580, 96)
      长撇 diag(560, 810, 110, 200, 96)
      寸横 hbar_top(330, 880, 400, 96)
      寸竖钩 vbar(700, 40, 400, 96) + diag(700, 45, 645, 105, 84)
      寸点 dot(520, 240, slant -14)
    """
    g = Glyph("uni5BFF", advance=1000, unicode=0x5BFF, note="寿 7画 三+丿+寸")
    hbar_top(g, 280.0, 720.0, 820.0, W_MAIN)
    hbar_top(g, 230.0, 770.0, 700.0, W_MAIN)
    hbar_top(g, 180.0, 820.0, 580.0, W_MAIN)
    g.diag(560.0, 810.0, 110.0, 200.0, weight=W_MAIN)
    hbar_top(g, 330.0, 880.0, 400.0, W_MAIN)
    g.vbar(700.0, 40.0, 400.0, weight=W_MAIN)
    g.diag(700.0, 45.0, 645.0, 105.0, weight=W_THIN)
    g.dot(520.0, 240.0, w=84, h=112, slant=-14)
    return g


def g_shin():
    """臣 7画（外框 + 三条短竖的阶梯结构）。

    部件分区：左竖 x 108（贯通 y 0..820）；四条横 y 48 / 388 / 580 / 772；
    三条短竖 x 460（上下两段）与 x 797（中段）。
    笔画清单：
      左竖 vbar(108, 0, 820, 96)
      横一 hbar(60, 940, 772, 96)      墨迹 724..820
      横二 hbar(108, 940, 580, 96)     墨迹 532..628
      横三 hbar(108, 940, 388, 96)     墨迹 340..436
      横四 hbar(108, 940, 48, 96)      墨迹 0..96
      短竖上 vbar(460, 580, 772, 84)
      短竖中 vbar(797, 388, 580, 84)
      短竖下 vbar(460, 48, 388, 84)
    """
    g = Glyph("uni81E3", advance=1000, unicode=0x81E3, note="臣 7画 外框+短竖")
    g.vbar(108.0, 0.0, 820.0, weight=W_MAIN)
    hbar_at(g, 60.0, 940.0, 772.0, W_MAIN)
    hbar_at(g, 108.0, 940.0, 580.0, W_MAIN)
    hbar_at(g, 108.0, 940.0, 388.0, W_MAIN)
    hbar_at(g, 108.0, 940.0, 48.0, W_MAIN)
    g.vbar(460.0, 580.0, 772.0, weight=W_THIN)
    g.vbar(797.0, 388.0, 580.0, weight=W_THIN)
    g.vbar(460.0, 48.0, 388.0, weight=W_THIN)
    return g


def g_sen():
    """浅 9画 氵 + 戋。

    部件分区：氵 x 60..300；戋 x 340..940（顶横 + 点 + 斜钩 + 交叉撇 + 下横）。
    笔画清单：
      氵   sanzui(150)
      戋横 hbar_top(400, 840, 700, 96)
      戋点 dot(890, 690, slant -14)
      戋斜钩 diag(740, 690, 900, 60, 96)
      戋撇 diag(860, 600, 430, 70, 92)
      戋下横 hbar_top(400, 820, 330, 92)
    """
    g = Glyph("uni6D45", advance=1000, unicode=0x6D45, note="浅 9画 氵+戋")
    sanzui(g, 150.0)
    hbar_top(g, 400.0, 840.0, 680.0, W_MAIN)
    g.dot(870.0, 760.0, w=84, h=108, slant=-14)
    g.diag(640.0, 640.0, 900.0, 50.0, weight=W_MAIN)
    g.diag(800.0, 640.0, 560.0, 60.0, weight=W_SEC)
    hbar_top(g, 380.0, 760.0, 330.0, W_SEC)
    return g


def g_rei():
    """励 7画 厉（厂 + 万）+ 力。

    部件分区：厉 x 70..560 y 40..800；力 x 580..940 y 40..620。
    笔画清单：
      厂横 hbar_top(90, 560, 800, 96)
      厂撇 diag(150, 790, 80, 60, 96)
      万横 hbar_top(200, 520, 620, 92)
      万横折 hbar_top(220, 480, 460, 92) + vbar(480, 140, 460, 92)
      万撇 diag(400, 460, 210, 60, 92)
      力   chikara(600, 940, 40, 620)
    """
    g = Glyph("uni52B1", advance=1000, unicode=0x52B1, note="励 7画 厉+力")
    hbar_top(g, 90.0, 560.0, 800.0, W_MAIN)
    g.diag(150.0, 790.0, 80.0, 60.0, weight=W_MAIN)
    hbar_top(g, 200.0, 520.0, 620.0, W_SEC)
    hbar_top(g, 220.0, 480.0, 460.0, W_SEC)
    g.vbar(480.0, 140.0, 460.0, weight=W_SEC)
    g.diag(400.0, 460.0, 210.0, 60.0, weight=W_SEC)
    chikara(g, 600.0, 940.0, 40.0, 620.0)
    return g


def g_kai():
    """皆 9画 比 + 白。

    部件分区：比 y 540..820（左匕 x 100..420，右匕 x 540..930）；
    白 y 0..520（丿 + 日 x 430..870）。
    笔画清单：
      左匕横 hbar_top(100, 420, 700, 92)
      左匕竖弯钩 vbar(180, 560, 820, 92) + diag(180, 570, 420, 660, 84)
      右匕撇 diag(900, 800, 540, 690, 92)
      右匕竖弯钩 vbar(560, 560, 820, 92) + diag(560, 570, 930, 660, 84)
      白撇   diag(520, 500, 400, 400, 84)
      白日   nichi(430, 870, 0, 400, 96, 0.52)
    """
    g = Glyph("uni7686", advance=1000, unicode=0x7686, note="皆 9画 比+白")
    hbar_top(g, 100.0, 420.0, 700.0, W_SEC)
    g.vbar(180.0, 560.0, 820.0, weight=W_SEC)
    g.diag(180.0, 570.0, 420.0, 660.0, weight=W_THIN)
    g.diag(900.0, 790.0, 640.0, 690.0, weight=W_SEC)
    g.vbar(560.0, 560.0, 820.0, weight=W_SEC)
    g.diag(560.0, 570.0, 930.0, 660.0, weight=W_THIN)
    g.diag(520.0, 500.0, 400.0, 400.0, weight=W_THIN)
    nichi(g, 430.0, 870.0, 0.0, 400.0, W_MAIN, mid_frac=0.52)
    return g


def g_shin2():
    """沈 7画 氵 + 冘。

    部件分区：氵 x 60..300；冘 x 400..940（丶 + 冖 + 儿）。
    笔画清单：
      氵   sanzui(150)
      冘点 dot(620, 760, slant 0)
      冘横钩 hbar_top(560, 880, 690, 96) + diag(880, 680, 820, 750, 84)
      儿撇 diag(640, 620, 430, 60, 96)
      儿竖弯钩 vbar(760, 120, 620, 96) + diag(760, 130, 900, 200, 84)
    """
    g = Glyph("uni6C88", advance=1000, unicode=0x6C88, note="沈 7画 氵+冘")
    sanzui(g, 150.0)
    g.dot(620.0, 760.0, w=84, h=110, slant=0)
    hbar_top(g, 560.0, 880.0, 690.0, W_MAIN)
    g.diag(880.0, 680.0, 820.0, 750.0, weight=W_THIN)
    g.diag(640.0, 620.0, 430.0, 60.0, weight=W_MAIN)
    g.vbar(760.0, 120.0, 620.0, weight=W_MAIN)
    g.diag(760.0, 130.0, 900.0, 200.0, weight=W_THIN)
    return g


def g_sei():
    """牲 9画 牜 + 生。

    部件分区：牜 x 60..350 y 60..780；生 x 400..940 y 0..800。
    笔画清单：
      牜撇 diag(230, 780, 150, 640, 92)
      牜横 hbar_top(90, 330, 600, 92)
      牜横 hbar_top(110, 350, 420, 92)
      牜竖 vbar(230, 60, 780, 96)
      生撇 diag(560, 800, 440, 640, 92)
      生横 hbar_top(480, 880, 660, 92)
      生横 hbar_top(440, 920, 480, 92)
      生竖 vbar(660, 40, 660, 96)
      生横 hbar_base(400, 940, 0, 96)
    """
    g = Glyph("uni7272", advance=1000, unicode=0x7272, note="牲 9画 牜+生")
    g.diag(230.0, 780.0, 150.0, 640.0, weight=W_SEC)
    hbar_top(g, 90.0, 330.0, 600.0, W_SEC)
    hbar_top(g, 110.0, 350.0, 420.0, W_SEC)
    g.vbar(230.0, 60.0, 780.0, weight=W_MAIN)
    g.diag(560.0, 800.0, 440.0, 640.0, weight=W_SEC)
    hbar_top(g, 480.0, 880.0, 660.0, W_SEC)
    hbar_top(g, 440.0, 920.0, 480.0, W_SEC)
    g.vbar(660.0, 40.0, 660.0, weight=W_MAIN)
    hbar_base(g, 400.0, 940.0, 0.0, W_MAIN)
    return g


def g_tei():
    """帝 9画 亠 + 丷 + 冖 + 巾。

    部件分区：亠 y 604..820；丷 y 514..626；冖 y 410..520；巾 y 0..400。
    2026-10-31 回修：冖的横（388..480）与巾的横（308..400）白口 −12 → 冖上移 40，白口 28。
    笔画清单：
      竖点 dot(500, 765, slant 0)
      一   hbar_top(150, 850, 700, 96)
      丷左 dot(360, 600, slant -14)
      丷右 dot(640, 600, slant +14)
      冖   tesagari(250, 750, 530, 92)
      巾横 hbar_top(380, 620, 420, 92)
      巾左竖 vbar(380, 190, 420, 92)
      巾右折 vbar(620, 60, 420, 92)
      巾中竖 vbar(500, 0, 420, 96)
    """
    g = Glyph("uni5E1D", advance=1000, unicode=0x5E1D, note="帝 9画 亠+丷+冖+巾")
    g.dot(500.0, 765.0, w=84, h=100, slant=0)
    hbar_top(g, 150.0, 850.0, 700.0, W_MAIN)
    g.dot(360.0, 570.0, w=88, h=112, slant=-14)
    g.dot(640.0, 570.0, w=88, h=112, slant=14)
    tesagari(g, 250.0, 750.0, 520.0, W_SEC)
    hbar_top(g, 370.0, 630.0, 400.0, W_SEC)
    g.vbar(370.0, 170.0, 400.0, weight=W_SEC)
    g.vbar(630.0, 40.0, 400.0, weight=W_SEC)
    g.vbar(500.0, 0.0, 400.0, weight=W_MAIN)
    return g


def g_so2():
    """阻 8画 阝 + 且。

    部件分区：阝 x 60..290 y 0..820；且 x 400..940 y 0..760。
    笔画清单：
      阝 kozato(108)
      且 soko(450, 890, 0, 760)
    """
    g = Glyph("uni963B", advance=1000, unicode=0x963B, note="阻 8画 阝+且")
    kozato(g, 108.0)
    soko(g, 450.0, 890.0, 0.0, 760.0, W_MAIN)
    return g


def g_nyu():
    """乳 8画 爫 + 子 + 乚。

    部件分区：爫 x 60..620 y 480..820；子 x 60..520 y 0..500；乚 x 700..900。
    笔画清单：
      爫撇   diag(600, 780, 140, 700, 96)
      爫左撇 dot(220, 600, slant +14)
      爫中点 dot(390, 590, slant -14)
      爫右点 dot(540, 590, slant -14)
      子   ko(60, 520, 0, 500)
      乚竖 vbar(700, 120, 800, 96)
      乚曲 diag(700, 130, 890, 220, 84)
    """
    g = Glyph("uni4E73", advance=1000, unicode=0x4E73, note="乳 8画 爫+子+乚")
    g.diag(600.0, 780.0, 140.0, 700.0, weight=W_MAIN)
    g.dot(220.0, 600.0, w=84, h=108, slant=14)
    g.dot(390.0, 590.0, w=84, h=108, slant=-14)
    g.dot(540.0, 590.0, w=84, h=108, slant=-14)
    ko(g, 60.0, 520.0, 0.0, 500.0)
    g.vbar(700.0, 120.0, 800.0, weight=W_MAIN)
    g.diag(700.0, 130.0, 890.0, 220.0, weight=W_THIN)
    return g


def g_tai():
    """耐 9画 而 + 寸。

    部件分区：而 x 80..600 y 60..800；寸 x 620..940 y 60..700。
    笔画清单：
      而横 hbar_top(80, 600, 800, 96)
      而撇 diag(330, 780, 280, 630, 84)
      而左竖 vbar(140, 60, 560, 92)
      而横折 hbar_top(140, 560, 560, 92) + vbar(560, 60, 560, 92)
      而中竖 vbar(300, 60, 560, 84)
      而中竖2 vbar(420, 60, 560, 84)
      寸横 hbar_top(620, 940, 700, 96)
      寸竖钩 vbar(800, 60, 700, 96) + diag(800, 65, 745, 125, 84)
      寸点 dot(680, 480, slant -14)
    """
    g = Glyph("uni8010", advance=1000, unicode=0x8010, note="耐 9画 而+寸")
    hbar_top(g, 80.0, 600.0, 800.0, W_MAIN)
    g.diag(330.0, 780.0, 280.0, 630.0, weight=W_THIN)
    g.vbar(140.0, 60.0, 560.0, weight=W_SEC)
    hbar_top(g, 140.0, 560.0, 560.0, W_SEC)
    g.vbar(560.0, 60.0, 560.0, weight=W_SEC)
    g.vbar(300.0, 60.0, 560.0, weight=W_THIN)
    g.vbar(420.0, 60.0, 560.0, weight=W_THIN)
    hbar_top(g, 620.0, 940.0, 700.0, W_MAIN)
    g.vbar(800.0, 60.0, 700.0, weight=W_MAIN)
    g.diag(800.0, 65.0, 745.0, 125.0, weight=W_THIN)
    g.dot(680.0, 480.0, w=84, h=112, slant=-14)
    return g


def g_ku():
    """紅 9画 糸 + 工。

    部件分区：糸 x 60..380 y 60..780；工 x 420..940 y 0..700。
    笔画清单：
      糸撇   diag(300, 780, 200, 620, 92)
      糸撇折 diag(210, 640, 140, 500, 92) + diag(140, 505, 340, 570, 92)
      糸点   dot(320, 560, slant -14)
      糸竖   vbar(230, 100, 500, 96)
      糸左点 dot(140, 260, slant -14)
      糸右点 dot(330, 260, slant +14)
      工横   hbar_top(440, 920, 700, 96)
      工竖   vbar(680, 60, 700, 96)
      工横   hbar_base(420, 940, 0, 96)
    """
    g = Glyph("uni7D05", advance=1000, unicode=0x7D05, note="紅 9画 糸+工")
    g.diag(300.0, 780.0, 200.0, 620.0, weight=W_SEC)
    g.diag(210.0, 640.0, 140.0, 500.0, weight=W_SEC)
    g.diag(140.0, 505.0, 340.0, 570.0, weight=W_SEC)
    g.dot(320.0, 560.0, w=84, h=108, slant=-14)
    g.vbar(230.0, 100.0, 500.0, weight=W_MAIN)
    g.dot(140.0, 260.0, w=84, h=112, slant=-14)
    g.dot(330.0, 260.0, w=84, h=112, slant=14)
    hbar_top(g, 440.0, 920.0, 700.0, W_MAIN)
    g.vbar(680.0, 60.0, 700.0, weight=W_MAIN)
    hbar_base(g, 420.0, 940.0, 0.0, W_MAIN)
    return g


def g_hou():
    """芳 7画 艹 + 方。

    部件分区：艹 y 550..820（横 x 180..820，竖 x 285 / 715）；方 y 30..620。
    笔画清单：
      艹 kusa(180, 820)
      方点 dot(500, 560, slant 0)
      方横 hbar_top(180, 820, 480, 96)
      方横折 hbar_top(250, 720, 340, 92) + vbar(720, 40, 340, 92)
      方撇 diag(560, 340, 250, 30, 92)
    """
    g = Glyph("uni82B3", advance=1000, unicode=0x82B3, note="芳 7画 艹+方")
    kusa(g, 180.0, 820.0)
    g.dot(500.0, 560.0, w=84, h=108, slant=0)
    hbar_top(g, 180.0, 820.0, 480.0, W_MAIN)
    hbar_top(g, 250.0, 720.0, 340.0, W_SEC)
    g.vbar(720.0, 40.0, 340.0, weight=W_SEC)
    g.diag(560.0, 340.0, 250.0, 30.0, weight=W_SEC)
    return g


def g_kou():
    """郊 8画 交 + 阝。

    部件分区：交 x 60..640 y 60..780；阝 x 700..880 y 0..820。
    笔画清单：
      交点 dot(350, 760, slant 0)
      交横 hbar_top(100, 620, 700, 96)
      交撇 diag(480, 660, 250, 420, 92)
      交捺 diag(350, 660, 590, 420, 92)
      交撇 diag(430, 480, 120, 60, 96)
      交捺 diag(430, 480, 620, 60, 96)
      阝 kozato(700)
    """
    g = Glyph("uni90CA", advance=1000, unicode=0x90CA, note="郊 8画 交+阝")
    g.dot(350.0, 760.0, w=84, h=108, slant=0)
    hbar_top(g, 100.0, 620.0, 700.0, W_MAIN)
    g.diag(480.0, 660.0, 250.0, 420.0, weight=W_SEC)
    g.diag(350.0, 660.0, 590.0, 420.0, weight=W_SEC)
    g.diag(430.0, 480.0, 120.0, 60.0, weight=W_MAIN)
    g.diag(430.0, 480.0, 620.0, 60.0, weight=W_MAIN)
    kozato(g, 700.0)
    return g


def g_tan():
    """炭 9画 山 + 灰（厂 + 火）。

    部件分区：山 y 620..820；灰 y 0..600（厂 y 40..580，火 x 300..940）。
    笔画清单：
      山中竖 vbar(500, 620, 820, 96)
      山竖折 vbar(250, 660, 760, 92) + hbar(250, 750, 716, 92)
      山右竖 vbar(750, 660, 760, 92)
      厂横 hbar_top(120, 900, 580, 96)
      厂撇 diag(180, 570, 80, 40, 96)
      火   hi(300, 940, 40, 560)
    """
    g = Glyph("uni70AD", advance=1000, unicode=0x70AD, note="炭 9画 山+灰")
    g.vbar(500.0, 716.0, 820.0, weight=W_MAIN)
    g.vbar(250.0, 660.0, 760.0, weight=W_SEC)
    hbar_at(g, 250.0, 750.0, 716.0, W_SEC)
    g.vbar(750.0, 660.0, 760.0, weight=W_SEC)
    hbar_top(g, 120.0, 900.0, 580.0, W_MAIN)
    g.diag(180.0, 570.0, 80.0, 40.0, weight=W_MAIN)
    hi(g, 300.0, 940.0, 40.0, 560.0)
    return g


def g_kou2():
    """恒 9画 忄 + 亘。

    部件分区：忄 x 60..360 y 0..800；亘 x 380..940 y 0..800。
    笔画清单：
      忄左点 dot(130, 560, slant -14)
      忄竖   vbar(230, 0, 800, 96)
      忄右点 dot(330, 620, slant +14)
      亘顶横 hbar_top(400, 920, 800, 96)
      亘日   nichi(460, 860, 200, 700, 92, 0.5)
      亘底横 hbar_base(380, 940, 0, 96)
    """
    g = Glyph("uni6052", advance=1000, unicode=0x6052, note="恒 9画 忄+亘")
    g.dot(130.0, 560.0, w=84, h=112, slant=-14)
    g.vbar(230.0, 0.0, 800.0, weight=W_MAIN)
    g.dot(330.0, 620.0, w=84, h=112, slant=14)
    hbar_top(g, 400.0, 920.0, 800.0, W_MAIN)
    nichi(g, 460.0, 860.0, 200.0, 700.0, W_SEC, mid_frac=0.50)
    hbar_base(g, 380.0, 940.0, 0.0, W_MAIN)
    return g


def g_mou():
    """冒 9画 日（上）+ 目（下）。

    部件分区：上日 x 120..880 y 488..820；下目 x 160..840 y 0..452。
    笔画清单：
      上日 vbar(120, 488, 820) / hbar(120,880,772) / vbar(880,488,820)
            / 中横 hbar(120,880,628) / 下横 hbar(120,880,520)
      下目 me(160, 840, 0, 452, 92)
    """
    g = Glyph("uni5192", advance=1000, unicode=0x5192, note="冒 9画 日+目")
    g.vbar(120.0, 488.0, 820.0, weight=W_LIGHT)
    hbar_at(g, 120.0, 880.0, 772.0, W_SEC)
    g.vbar(880.0, 488.0, 820.0, weight=W_LIGHT)
    hbar_at(g, 120.0, 880.0, 628.0, W_LIGHT)
    hbar_at(g, 120.0, 880.0, 516.0, W_LIGHT)
    me(g, 160.0, 840.0, 0.0, 452.0, W_LIGHT)
    return g


def g_yu():
    """勇 9画 マ + 用 + 力。

    部件分区：マ y 632..820（竖点 + 一）；用 y 218..640（三横 + 中竖）；
    力 y 0..190。
    2026-10-31 回修：用底横（218..310）与力的横（144..240）白口 −22 → 力下移 50，白口 28。
    笔画清单：
      マ竖点 dot(300, 760, slant 0)
      マ横   hbar_top(140, 860, 680, 96)
      用撇   diag(330, 620, 250, 500, 84)
      用横   hbar_top(140, 860, 620, 96)
      用右竖 vbar(860, 228, 620, 96)
      用中横 hbar_top(140, 860, 424, 92)
      用底横 hbar_top(140, 860, 276, 92)
      用中竖 vbar(500, 228, 620, 92)
      力   chikara(140, 860, 0, 220)
    """
    g = Glyph("uni52C7", advance=1000, unicode=0x52C7, note="勇 9画 マ+用+力")
    # マ：一横（右端折向左下）+ 横下短点
    hbar_top(g, 140.0, 860.0, 820.0, W_MAIN)
    g.diag(850.0, 800.0, 770.0, 720.0, weight=W_THIN)
    g.dot(280.0, 710.0, w=84, h=96, slant=-14)
    # 用：短撇 + 左竖 + 横 + 右竖 + 中横 + 底横 + 中竖
    g.diag(330.0, 640.0, 250.0, 520.0, weight=W_THIN)
    g.vbar(140.0, 250.0, 640.0, weight=W_MAIN)
    hbar_top(g, 140.0, 860.0, 640.0, W_MAIN)
    g.vbar(860.0, 250.0, 640.0, weight=W_MAIN)
    hbar_top(g, 140.0, 860.0, 460.0, W_SEC)
    hbar_top(g, 140.0, 860.0, 310.0, W_SEC)
    g.vbar(500.0, 250.0, 640.0, weight=W_SEC)
    # 力
    chikara(g, 140.0, 860.0, 0.0, 190.0)
    return g


def build() -> list[Glyph]:
    return [
        g_mo(),    # 茂
        g_se(),    # 昔
        g_chi(),   # 茨
        g_sai(),   # 斉
        g_i(),     # 衣
        g_kata(),  # 肩
        g_do(),    # 怒
        g_ei(),    # 泳
        g_so(),    # 祖
        g_haku(),  # 泊
        g_jin(),   # 尽
        g_hai(),   # 杯
        g_ko(),    # 孤
        g_en(),    # 炎
        g_ju(),    # 寿
        g_shin(),  # 臣
        g_sen(),   # 浅
        g_rei(),   # 励
        g_kai(),   # 皆
        g_shin2(), # 沈
        g_sei(),   # 牲
        g_tei(),   # 帝
        g_so2(),   # 阻
        g_nyu(),   # 乳
        g_tai(),   # 耐
        g_ku(),    # 紅
        g_hou(),   # 芳
        g_kou(),   # 郊
        g_tan(),   # 炭
        g_kou2(),  # 恒
        g_mou(),   # 冒
        g_yu(),    # 勇
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-014.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
