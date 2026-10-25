"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-021。

本批 28 字，笔画范围 6–9，取自 2010 年文化庁《常用漢字表》。

【整体设计取舍】
- 冻结参数：UPM 1000；advance 1000；字面框 x 60..940、y 0..820（与繁体汉字同档）。
- 笔画权重：主 96 / 次 92 / 细 84 / 点 84–96。笔画少的字（但、芋、吏、弐、伎）
  主笔用 96 并让内白开大；笔画多的字（侯、弧、柵、拶、妬、勃、侶、昧）
  在密排处把内层横竖降到 84，保证内白不被墨吃掉。
- 骨架来源：本批每字的**笔顺、角度、部件分区**逐字核对 KanjiVG
  （日本語標準の筆順データ，CC BY-SA 3.0）转出的标准骨架中心线，
  再按本字体字面框做等比归位（保持角度不变，只做位置与大小的光学校正）。
  参照字体 E:/hkposter-refs/（M PLUS 1p Black、Zen Kaku Gothic New Black，
  均 SIL OFL 1.1）只用于比例与骨架交叉校核，不描轮廓。
- 端点：横竖撇捺一律平切硬边（g.hbar / g.vbar / g.diag）；
  点与短撇用斜切平行四边形（g.dot），slant 只取规格档位
  26 / 22 / 20 / 18 / 16 / 14 / −14 / 0：
    · 短撇（氵的上点、下点）→ 26（与基线族 hkposter-cjk-core.py 的氵一致）
    · 丶（右下的点：厶的点 / 冫の上点 / 寸的点 / 弋的点 / 太的点 /
      爫の点 / 木の点 / 丸の点 / 夕の点 / 宀の左点 / 冖の左点）→ −14
    · 丿（丷右 / 小右点一类）→ +14（本批未出现）
    · 竖点（亠的点：宀的点、立案的点）→ 0
- 转角：弓、阝、巳、刂、扌等的折笔用「外角硬折」（两段矩形求并），
  符合港产海报的重方硬朗感。
"""

from __future__ import annotations

import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, write_ufo  # noqa: E402

W_MAIN = 96   # 主
W_SEC = 92    # 次
W_THIN = 84   # 细
W_DOT = 84    # 点的横向宽度


# --------------------------------------------------------------------------
# 对齐辅助：横画墨迹上缘贴 820 / 下缘贴 0 时，中心线内缩半个笔画宽。
# --------------------------------------------------------------------------
def bar_top(g: Glyph, x1: float, x2: float, w: float = W_MAIN) -> None:
    """横画：墨迹上缘对齐 y=820。"""
    g.hbar(x1, x2, 820 - w / 2, weight=w)


def bar_bot(g: Glyph, x1: float, x2: float, w: float = W_MAIN) -> None:
    """横画：墨迹下缘对齐 y=0。"""
    g.hbar(x1, x2, w / 2, weight=w)


def dot_up(g: Glyph, cx: float, cy: float, w: float = W_DOT, h: float = 104,
           slant: float = -14) -> None:
    """点：斜切平行四边形（slant 为水平错切量，单位=em 单位）。"""
    g.dot(cx, cy, w=w, h=h, slant=slant)


# --------------------------------------------------------------------------
# 00 侯 U+4FAF —— 亻 + コ(ユ形) + 矢   9 画
# 部件分区：亻 x 60..300；コ x 333..904；矢 x 326..908
# --------------------------------------------------------------------------
def g_hou() -> Glyph:
    g = Glyph(name="uni4FAF", advance=1000, unicode=0x4FAF,
              note="侯：左亻，中部コ形，右下矢")
    # 亻：撇 + 竖
    g.diag(279, 786, 92, 397, weight=W_SEC)      # 亻的撇
    g.vbar(231, 6, 587, weight=W_SEC)           # 亻的竖
    # コ：横折（顶横 + 右竖折下）
    bar_top(g, 415, 745, W_MAIN)                # コ的顶横
    g.vbar(735, 650, 800, weight=W_SEC)         # コ的右竖
    g.hbar(333, 904, 624, weight=W_MAIN)        # コ的长横
    # 矢：𠂉（撇 + 短横）+ 大（长横 + 撇 + 捺）
    g.diag(462, 522, 347, 351, weight=W_THIN)   # 矢的𠂉撇
    g.hbar(476, 794, 478, weight=W_THIN)        # 矢的𠂉横
    g.hbar(326, 895, 305, weight=W_MAIN)        # 大的长横
    g.diag(602, 441, 505, 159, weight=W_SEC)    # 大的撇（上段）
    g.diag(505, 159, 328, 0, weight=W_SEC)      # 大的撇（下段）
    g.diag(606, 306, 908, 21, weight=W_SEC)     # 大的捺
    return g


# --------------------------------------------------------------------------
# 01 弧 U+5F27 —— 弓 + 瓜   9 画
# 部件分区：弓 x 73..315；瓜 x 284..927
# --------------------------------------------------------------------------
def g_arc() -> Glyph:
    g = Glyph(name="uni5F27", advance=1000, unicode=0x5F27,
              note="弧：左弓，右瓜")
    # 弓：横折 / 一 / 竖折折钩
    g.hbar(73, 300, 770, weight=W_MAIN)         # 弓的横折（横）
    g.vbar(298, 600, 782, weight=W_SEC)         # 弓的横折（折）
    g.hbar(111, 299, 587, weight=W_SEC)         # 弓的一
    g.vbar(110, 386, 572, weight=W_SEC)         # 弓的竖折折钩（竖）
    g.hbar(110, 274, 385, weight=W_SEC)         # 弓的竖折折钩（横）
    g.diag(270, 380, 185, 40, weight=W_SEC)     # 弓的竖折折钩（下行）
    g.diag(180, 42, 138, 0, weight=W_THIN)      # 弓的钩
    # 瓜：撇（长撇折下，与第二撇连成一笔）/ 竖 / 提 / 点 / 捺
    g.diag(714, 815, 420, 612, weight=W_SEC)     # 瓜的长撇（上段）
    g.diag(420, 612, 284, 19, weight=W_SEC)      # 瓜的撇（下段，与上段同笔顺）
    g.vbar(578, 160, 605, weight=W_SEC)         # 瓜的竖
    g.diag(453, 122, 695, 199, weight=W_THIN)   # 瓜的提
    dot_up(g, 707, 194, w=92, h=132, slant=-14)     # 瓜的点
    g.diag(698, 603, 927, 25, weight=W_SEC)     # 瓜的捺
    return g


# --------------------------------------------------------------------------
# 02 訃 U+8A03 —— 言 + 卜   9 画
# 部件分区：言 x 121..456；卜 x 630..879
# --------------------------------------------------------------------------
def g_botsu() -> Glyph:
    g = Glyph(name="uni8A03", advance=1000, unicode=0x8A03,
              note="訃：左言，右卜")
    # 言：点 + 三横 + 口
    dot_up(g, 314, 742, w=88, h=116, slant=-14)  # 言的点
    g.hbar(121, 456, 610, weight=W_MAIN)         # 言的长横
    g.hbar(200, 397, 497, weight=W_THIN)        # 言的横 2
    g.hbar(200, 424, 382, weight=W_THIN)        # 言的横 3
    g.vbar(223, 58, 247, weight=W_THIN)          # 言的竖
    g.hbar(210, 438, 252, weight=W_THIN)        # 口的横折（横）
    g.vbar(438, 121, 262, weight=W_THIN)         # 口的横折（折）
    g.hbar(256, 433, 102, weight=W_THIN)        # 口的底横
    # 卜：竖 + 点（长斜点）
    g.vbar(640, 0, 820, weight=W_MAIN)           # 卜的竖
    g.diag(671, 522, 879, 343, weight=W_SEC)     # 卜的点
    return g


# --------------------------------------------------------------------------
# 03 畏 U+754F —— 田 + 一 + 𧘇   9 画
# 部件分区：田 x 227..756；下部 x 117..883
# --------------------------------------------------------------------------
def g_i() -> Glyph:
    g = Glyph(name="uni754F", advance=1000, unicode=0x754F,
              note="畏：上田，下衣字底")
    # 田：竖 / 横折 / 中竖 / 两横（田在上部要占足宽度，与下方一形成横向对比）
    g.vbar(225, 487, 783, weight=W_SEC)          # 田的左竖
    bar_top(g, 225, 785, W_MAIN)                 # 田的横折（横）
    g.vbar(775, 518, 790, weight=W_SEC)          # 田的横折（折）
    g.vbar(500, 542, 779, weight=W_THIN)         # 田的中竖
    g.hbar(250, 750, 663, weight=W_THIN)         # 田的中横
    g.hbar(265, 725, 528, weight=W_THIN)         # 田的下横
    # 下部：一 + 竖撇 + 撇 + 捺
    g.hbar(117, 877, 407, weight=W_MAIN)         # 的一
    g.diag(281, 359, 291, 40, weight=W_SEC)      # 竖撇（上段）
    g.diag(291, 40, 320, 2, weight=W_THIN)       # 竖撇（下段，带钩）
    g.diag(735, 358, 617, 237, weight=W_THIN)    # 撇
    g.diag(408, 342, 883, 4, weight=W_SEC)       # 捺
    return g


# --------------------------------------------------------------------------
# 04 附 U+9644 —— 阝 + 付   8 画
# 部件分区：阝 x 85..250；付 x 338..930
# --------------------------------------------------------------------------
def g_fu() -> Glyph:
    g = Glyph(name="uni9644", advance=1000, unicode=0x9644,
              note="附：左阝，右付")
    # 阝：横撇弯钩 + 竖
    g.hbar(70, 250, 790, weight=W_THIN)          # 阝的横撇弯钩（横）
    g.diag(250, 792, 280, 726, weight=W_THIN)    # 阝的横撇弯钩（弯）
    g.diag(272, 726, 194, 598, weight=W_THIN)    # 阝的横撇弯钩（撇）
    g.vbar(100, 0, 763, weight=W_MAIN)           # 阝的竖
    # 付：亻 + 寸
    g.diag(506, 807, 338, 488, weight=W_SEC)     # 亻的撇
    g.vbar(443, 17, 600, weight=W_SEC)           # 亻的竖
    g.hbar(520, 930, 586, weight=W_MAIN)         # 寸的横
    g.vbar(716, 89, 820, weight=W_SEC)           # 寸的竖钩
    g.diag(760, 60, 725, 10, weight=W_THIN)      # 寸的钩
    dot_up(g, 615, 372, w=96, h=118, slant=-14)    # 寸的点
    return g


# --------------------------------------------------------------------------
# 05 但 U+4F46 —— 亻 + 旦   7 画
# 部件分区：亻 x 60..287；旦 x 357..940
# --------------------------------------------------------------------------
def g_dan() -> Glyph:
    g = Glyph(name="uni4F46", advance=1000, unicode=0x4F46,
              note="但：左亻，右旦")
    g.diag(287, 809, 60, 368, weight=W_SEC)      # 亻的撇
    g.vbar(222, 11, 557, weight=W_SEC)           # 亻的竖
    # 旦：日 + 底横
    g.vbar(456, 229, 729, weight=W_SEC)          # 日的左竖
    bar_top(g, 472, 795, W_MAIN)                 # 日的横折（横）
    g.vbar(806, 231, 740, weight=W_SEC)          # 日的横折（折）
    g.hbar(473, 813, 503, weight=W_THIN)         # 日的中横
    g.hbar(472, 811, 270, weight=W_THIN)         # 日的下横
    g.hbar(357, 940, 66, weight=W_MAIN)          # 旦的底横
    return g


# --------------------------------------------------------------------------
# 06 芋 U+828B —— 艹 + 于   6 画
# 部件分区：艹 x 190..822；于 x 123..877
# --------------------------------------------------------------------------
def g_u() -> Glyph:
    g = Glyph(name="uni828B", advance=1000, unicode=0x828B,
              note="芋：上艹，下于")
    g.hbar(190, 822, 703, weight=W_MAIN)         # 艹的横
    g.vbar(350, 617, 811, weight=W_SEC)          # 艹的左竖
    g.vbar(633, 631, 820, weight=W_SEC)          # 艹的右竖
    g.hbar(258, 712, 540, weight=W_SEC)          # 于的上横
    g.hbar(123, 877, 368, weight=W_MAIN)         # 于的下横
    g.vbar(505, 50, 500, weight=W_SEC)           # 于的竖钩
    g.diag(508, 50, 470, 6, weight=W_THIN)       # 于的钩
    return g


# --------------------------------------------------------------------------
# 07 拭 U+62ED —— 扌 + 式   9 画
# 部件分区：扌 x 84..353；式 x 380..915
# --------------------------------------------------------------------------
def g_shiki() -> Glyph:
    g = Glyph(name="uni62ED", advance=1000, unicode=0x62ED,
              note="拭：左扌，右式")
    # 扌：横 / 竖钩 / 提
    g.hbar(103, 353, 598, weight=W_MAIN)         # 扌的横
    g.vbar(258, 49, 810, weight=W_SEC)           # 扌的竖钩
    g.diag(258, 45, 220, 20, weight=W_THIN)      # 扌的钩
    g.diag(84, 310, 334, 451, weight=W_SEC)      # 扌的提
    # 式：长横 / 工（横 + 竖 + 提）/ 弋（斜钩 + 点）
    g.hbar(412, 872, 591, weight=W_MAIN)         # 式的长横
    g.hbar(395, 622, 421, weight=W_THIN)         # 式的工上横
    g.vbar(504, 208, 397, weight=W_THIN)         # 式的工竖
    g.diag(380, 154, 624, 254, weight=W_SEC)     # 式的工提
    g.diag(645, 812, 800, 190, weight=W_SEC)     # 弋的斜钩（上段）
    g.diag(800, 190, 900, 8, weight=W_SEC)       # 弋的斜钩（下段）
    dot_up(g, 816, 746, w=96, h=112, slant=-14)    # 弋的点
    return g


# --------------------------------------------------------------------------
# 08 宛 U+5B9B —— 宀 + 夗   8 画
# 部件分区：宀 x 187..793；夗 x 132..868
# --------------------------------------------------------------------------
def g_wan() -> Glyph:
    g = Glyph(name="uni5B9B", advance=1000, unicode=0x5B9B,
              note="宛：上宀，下夗")
    # 宀：竖点 / 左点 / 横钩
    dot_up(g, 485, 760, w=84, h=120, slant=0)     # 宀的竖点
    dot_up(g, 208, 597, w=88, h=112, slant=-14)   # 宀的左点
    g.hbar(239, 750, 680, weight=W_SEC)          # 宀的横钩（横）
    g.diag(775, 700, 745, 630, weight=W_SEC)     # 宀的横钩（钩）
    # 夕：撇 / 横撇 / 点
    g.diag(328, 568, 164, 264, weight=W_SEC)     # 夕的撇
    g.hbar(324, 460, 490, weight=W_SEC)          # 夕的横撇（横）
    g.diag(462, 486, 132, 0, weight=W_SEC)       # 夕的横撇（撇）
    dot_up(g, 287, 281, w=96, h=112, slant=-14)  # 夕的点
    # 㔾：横折弯钩 / 竖弯钩
    g.hbar(545, 745, 512, weight=W_SEC)          # 横折弯钩（横）
    g.diag(748, 500, 700, 290, weight=W_SEC)     # 横折弯钩（折）
    g.diag(700, 290, 662, 262, weight=W_SEC)     # 横折弯钩（钩）
    g.vbar(560, 60, 490, weight=W_SEC)           # 竖弯钩（竖）
    g.hbar(560, 645, 60, weight=W_SEC)           # 竖弯钩（底）
    g.diag(645, 60, 868, 152, weight=W_SEC)      # 竖弯钩（右上挑）
    return g


# --------------------------------------------------------------------------
# 09 咽 U+54BD —— 口 + 因   9 画
# 部件分区：口 x 60..306；因 x 414..940
# --------------------------------------------------------------------------
def g_in() -> Glyph:
    g = Glyph(name="uni54BD", advance=1000, unicode=0x54BD,
              note="咽：左口，右因")
    g.vbar(82, 309, 661, weight=W_SEC)           # 口的左竖
    g.hbar(83, 290, 655, weight=W_MAIN)          # 口的横折（横）
    g.vbar(292, 365, 668, weight=W_SEC)          # 口的横折（折）
    g.hbar(117, 298, 346, weight=W_THIN)         # 口的底横
    # 因
    g.vbar(420, 9, 790, weight=W_SEC)            # 因的左竖
    g.hbar(435, 915, 790, weight=W_MAIN)         # 因的横折（横）
    g.vbar(925, 12, 800, weight=W_SEC)           # 因的横折（折）
    g.hbar(509, 852, 525, weight=W_THIN)         # 因的横
    g.diag(671, 715, 636, 349, weight=W_SEC)     # 因的大撇（上段）
    g.diag(636, 349, 547, 186, weight=W_THIN)    # 因的大撇（下段）
    g.diag(686, 396, 852, 175, weight=W_SEC)     # 因的捺
    g.hbar(438, 928, 57, weight=W_THIN)          # 因的底横
    return g


# --------------------------------------------------------------------------
# 10 苛 U+82DB —— 艹 + 可   8 画
# 部件分区：艹 x 167..826；可 x 155..845
# --------------------------------------------------------------------------
def g_kaku() -> Glyph:
    g = Glyph(name="uni82DB", advance=1000, unicode=0x82DB,
              note="苛：上艹，下可")
    g.hbar(167, 826, 697, weight=W_MAIN)         # 艹的横
    g.vbar(358, 599, 798, weight=W_SEC)          # 艹的左竖
    g.vbar(600, 613, 820, weight=W_SEC)          # 艹的右竖
    g.hbar(155, 845, 521, weight=W_MAIN)         # 可的长横
    g.vbar(253, 175, 367, weight=W_THIN)         # 口左竖
    g.hbar(248, 455, 368, weight=W_THIN)         # 口的横折（横）
    g.vbar(462, 232, 375, weight=W_THIN)         # 口的横折（折）
    g.hbar(285, 470, 211, weight=W_THIN)         # 口的底横
    g.vbar(684, 30, 500, weight=W_SEC)           # 可的竖钩
    g.diag(684, 25, 648, 2, weight=W_THIN)       # 可的钩
    return g


# --------------------------------------------------------------------------
# 11 伎 U+4F0E —— 亻 + 支   6 画
# 部件分区：亻 x 89..339；支 x 334..911
# --------------------------------------------------------------------------
def g_gi() -> Glyph:
    g = Glyph(name="uni4F0E", advance=1000, unicode=0x4F0E,
              note="伎：左亻，右支")
    g.diag(339, 791, 89, 344, weight=W_SEC)      # 亻的撇
    g.vbar(242, 0, 508, weight=W_SEC)            # 亻的竖
    g.hbar(377, 872, 628, weight=W_MAIN)         # 支的横
    g.vbar(591, 463, 820, weight=W_SEC)          # 支的竖
    g.hbar(432, 748, 447, weight=W_THIN)         # 支的横撇（横）
    g.diag(744, 458, 334, 6, weight=W_SEC)       # 支的横撇（撇）
    g.diag(425, 381, 911, 16, weight=W_SEC)      # 支的捺
    return g


# --------------------------------------------------------------------------
# 12 采 U+91C7 —— 爫 + 木   8 画
# 部件分区：爫 x 221..817；木 x 154..846
# --------------------------------------------------------------------------
def g_sai() -> Glyph:
    g = Glyph(name="uni91C7", advance=1000, unicode=0x91C7,
              note="采：上爫，下木")
    g.diag(656, 815, 282, 687, weight=W_SEC)     # 爫的长撇
    dot_up(g, 264, 561, w=92, h=118, slant=-14)    # 爫的点 1
    dot_up(g, 489, 603, w=92, h=118, slant=-14)    # 爫的点 2
    g.diag(817, 710, 669, 513, weight=W_THIN)    # 爫的撇
    g.hbar(181, 843, 373, weight=W_MAIN)         # 木的横
    g.vbar(509, 0, 494, weight=W_SEC)            # 木的竖
    g.diag(496, 364, 154, 70, weight=W_SEC)      # 木的撇
    g.diag(527, 361, 846, 93, weight=W_SEC)      # 木的捺
    return g


# --------------------------------------------------------------------------
# 13 柵 U+67F5 —— 木 + 冊   9 画
# 部件分区：木 x 60..339；冊 x 341..940
# --------------------------------------------------------------------------
def g_san() -> Glyph:
    g = Glyph(name="uni67F5", advance=1000, unicode=0x67F5,
              note="柵：左木，右冊")
    g.hbar(74, 339, 559, weight=W_MAIN)          # 木的横
    g.vbar(228, 17, 803, weight=W_SEC)           # 木的竖
    g.diag(231, 538, 60, 183, weight=W_SEC)      # 木的撇
    dot_up(g, 304, 394, w=92, h=112, slant=-14)    # 木的点
    # 冊
    g.vbar(431, 29, 767, weight=W_THIN)          # 冊的左竖
    g.hbar(445, 810, 762, weight=W_MAIN)         # 冊的横折钩（横）
    g.vbar(838, 57, 775, weight=W_THIN)          # 冊的横折钩（折）
    g.diag(836, 40, 805, 18, weight=W_THIN)      # 冊的钩
    g.vbar(555, 77, 732, weight=W_THIN)          # 冊的中竖
    g.vbar(684, 80, 752, weight=W_THIN)          # 冊的右竖
    g.hbar(341, 940, 461, weight=W_THIN)         # 冊的横
    return g


# --------------------------------------------------------------------------
# 14 拶 U+62F6 —— 扌 + 卆   9 画
# 部件分区：扌 x 130..410；卆 x 404..870
# --------------------------------------------------------------------------
def g_satsu() -> Glyph:
    g = Glyph(name="uni62F6", advance=1000, unicode=0x62F6,
              note="拶：左扌，右卆")
    g.hbar(132, 410, 586, weight=W_MAIN)         # 扌的横
    g.vbar(296, 98, 805, weight=W_SEC)           # 扌的竖钩
    g.diag(294, 80, 258, 52, weight=W_THIN)      # 扌的钩
    g.diag(130, 304, 388, 457, weight=W_SEC)     # 扌的提
    # 卆上部三笔（各为折笔）
    g.diag(553, 815, 455, 659, weight=W_THIN)    # 上 1 撇
    g.diag(455, 659, 560, 513, weight=W_THIN)    # 上 1 折
    g.diag(718, 814, 619, 665, weight=W_THIN)    # 上 2 撇
    g.diag(619, 665, 716, 526, weight=W_THIN)    # 上 2 折
    g.diag(863, 820, 768, 681, weight=W_THIN)    # 上 3 撇
    g.diag(768, 681, 870, 533, weight=W_THIN)    # 上 3 折
    # 卆下部
    g.diag(639, 507, 419, 227, weight=W_SEC)     # 撇
    g.hbar(631, 855, 420, weight=W_THIN)         # 横撇（横）
    g.diag(852, 420, 404, 0, weight=W_SEC)       # 横撇（撇）
    dot_up(g, 594, 245, w=96, h=112, slant=-14)    # 点
    return g


# --------------------------------------------------------------------------
# 15 汰 U+6C70 —— 氵 + 太   7 画
# 部件分区：氵 x 61..272；太 x 267..928
# --------------------------------------------------------------------------
def g_tai() -> Glyph:
    g = Glyph(name="uni6C70", advance=1000, unicode=0x6C70,
              note="汰：左氵，右太")
    dot_up(g, 215, 739, w=104, h=132, slant=26)  # 氵の上点
    dot_up(g, 136, 496, w=104, h=132, slant=26)  # 氵の下点
    g.diag(88, 38, 225, 222, weight=W_SEC)       # 氵的提
    g.hbar(313, 894, 539, weight=W_MAIN)         # 太的横
    g.diag(572, 812, 267, 0, weight=W_SEC)       # 太的撇
    g.diag(572, 522, 928, 16, weight=W_SEC)      # 太的捺
    dot_up(g, 595, 96, w=96, h=118, slant=-14)     # 太的点
    return g


# --------------------------------------------------------------------------
# 16 妬 U+59AC —— 女 + 石   8 画
# 部件分区：女 x 60..413；石 x 431..940
# --------------------------------------------------------------------------
def g_jo() -> Glyph:
    g = Glyph(name="uni59AC", advance=1000, unicode=0x59AC,
              note="妬：左女，右石")
    g.diag(280, 788, 182, 316, weight=W_SEC)     # 女的撇点（撇）
    g.diag(182, 316, 388, 151, weight=W_SEC)     # 女的撇点（点）
    g.diag(393, 581, 129, 68, weight=W_SEC)      # 女的撇
    g.diag(60, 441, 413, 520, weight=W_SEC)      # 女的横
    g.hbar(477, 940, 707, weight=W_MAIN)         # 石的横
    g.diag(652, 675, 431, 240, weight=W_SEC)     # 石的撇
    g.vbar(586, 32, 370, weight=W_THIN)          # 石的口左竖
    g.hbar(580, 885, 358, weight=W_THIN)         # 石的口横折（横）
    g.vbar(880, 84, 370, weight=W_THIN)          # 石的口横折（折）
    g.hbar(603, 891, 58, weight=W_THIN)          # 石的口底横
    return g


# --------------------------------------------------------------------------
# 17 弐 U+5F10 —— 弋 + 二   6 画
# 部件分区：二 x 114..449；弋 x 159..890
# --------------------------------------------------------------------------
def g_ni() -> Glyph:
    g = Glyph(name="uni5F10", advance=1000, unicode=0x5F10,
              note="弐：左二，右弋")
    g.hbar(189, 419, 698, weight=W_MAIN)         # 二的上横
    g.hbar(114, 848, 534, weight=W_MAIN)         # 弋的长横
    g.hbar(167, 449, 322, weight=W_MAIN)         # 二的下横
    g.diag(159, 57, 444, 174, weight=W_SEC)      # 弋的提
    g.diag(505, 812, 660, 235, weight=W_SEC)     # 弋的斜钩（上段）
    g.diag(660, 235, 872, 12, weight=W_SEC)      # 弋的斜钩（下段）
    dot_up(g, 748, 723, w=96, h=112, slant=-14)    # 弋的点
    return g


# --------------------------------------------------------------------------
# 18 肘 U+8098 —— 月 + 寸   7 画
# 部件分区：月 x 60..347；寸 x 427..940
# --------------------------------------------------------------------------
def g_chi() -> Glyph:
    g = Glyph(name="uni8098", advance=1000, unicode=0x8098,
              note="肘：左月，右寸")
    g.diag(146, 763, 60, 39, weight=W_SEC)       # 月的撇
    g.hbar(168, 315, 765, weight=W_MAIN)         # 月的横折钩（横）
    g.vbar(336, 55, 760, weight=W_SEC)           # 月的横折钩（折）
    g.diag(334, 50, 296, 26, weight=W_THIN)      # 月的钩
    g.hbar(168, 341, 558, weight=W_THIN)         # 月的横 1
    g.hbar(157, 343, 373, weight=W_THIN)         # 月的横 2
    g.hbar(427, 940, 583, weight=W_MAIN)         # 寸的横
    g.vbar(746, 56, 810, weight=W_SEC)           # 寸的竖钩
    g.diag(745, 50, 712, 12, weight=W_THIN)      # 寸的钩
    dot_up(g, 560, 362, w=96, h=118, slant=-14)    # 寸的点
    return g


# --------------------------------------------------------------------------
# 19 勃 U+52C3 —— 孛 + 力   9 画
# 部件分区：孛 x 96..504；力 x 448..904
# --------------------------------------------------------------------------
def g_boku() -> Glyph:
    g = Glyph(name="uni52C3", advance=1000, unicode=0x52C3,
              note="勃：左孛，右力")
    g.hbar(119, 504, 716, weight=W_MAIN)          # 十的横
    g.vbar(307, 595, 820, weight=W_SEC)           # 十的竖
    dot_up(g, 113, 521, w=88, h=110, slant=-14)    # 冖的左点
    g.hbar(130, 480, 590, weight=W_THIN)          # 冖的横钩（横）
    g.diag(478, 580, 462, 520, weight=W_THIN)    # 冖的横钩（钩）
    g.hbar(195, 398, 468, weight=W_THIN)         # 子的横撇（横）
    g.diag(395, 482, 307, 377, weight=W_THIN)    # 子的横撇（撇）
    g.diag(350, 210, 300, 45, weight=W_SEC)      # 子的竖钩
    g.diag(298, 40, 262, 14, weight=W_THIN)      # 子的钩
    g.diag(146, 217, 483, 340, weight=W_SEC)     # 子的一
    # 力
    g.hbar(580, 885, 545, weight=W_MAIN)         # 力的横折钩（横）
    g.diag(895, 525, 740, 50, weight=W_SEC)      # 力的横折钩（折）
    g.diag(735, 45, 700, 20, weight=W_THIN)      # 力的钩
    g.diag(730, 795, 623, 244, weight=W_SEC)     # 力的撇（上段）
    g.diag(623, 244, 448, 0, weight=W_SEC)       # 力的撇（下段）
    return g


# --------------------------------------------------------------------------
# 20 昧 U+6627 —— 日 + 末   9 画
# 部件分区：日 x 113..311；末 x 306..887
# --------------------------------------------------------------------------
def g_mai() -> Glyph:
    g = Glyph(name="uni6627", advance=1000, unicode=0x6627,
              note="昧：左日，右末")
    g.vbar(116, 250, 676, weight=W_THIN)          # 日的左竖
    g.hbar(126, 295, 678, weight=W_MAIN)          # 日的横折（横）
    g.vbar(302, 260, 685, weight=W_THIN)          # 日的横折（折）
    g.hbar(120, 307, 481, weight=W_THIN)         # 日的中横
    g.hbar(124, 302, 278, weight=W_THIN)         # 日的下横
    g.hbar(441, 771, 624, weight=W_MAIN)         # 末的上横
    g.hbar(362, 860, 464, weight=W_MAIN)         # 末的长横
    g.vbar(590, 0, 820, weight=W_SEC)            # 末的竖
    g.diag(594, 451, 306, 121, weight=W_SEC)     # 末的撇
    g.diag(604, 454, 887, 137, weight=W_SEC)     # 末的捺
    return g


# --------------------------------------------------------------------------
# 21 冶 U+51B6 —— 冫 + 台   7 画
# 部件分区：冫 x 74..262；台 x 418..926
# --------------------------------------------------------------------------
def g_ya() -> Glyph:
    g = Glyph(name="uni51B6", advance=1000, unicode=0x51B6,
              note="冶：左冫，右台")
    dot_up(g, 193, 685, w=120, h=122, slant=-14)  # 冫的上点
    g.diag(74, 83, 261, 335, weight=W_SEC)       # 冫的提
    g.diag(622, 812, 425, 455, weight=W_SEC)     # 台的上撇（厶的撇）
    g.diag(425, 455, 490, 440, weight=W_THIN)    # 台的上撇（厶的折）
    dot_up(g, 847, 535, w=96, h=118, slant=-14)    # 厶的点
    g.vbar(462, 0, 306, weight=W_SEC)            # 口的左竖
    g.hbar(461, 830, 300, weight=W_MAIN)         # 口的横折（横）
    g.vbar(845, 58, 310, weight=W_SEC)           # 口的横折（折）
    g.hbar(503, 848, 37, weight=W_THIN)          # 口的底横
    return g


# --------------------------------------------------------------------------
# 22 沃 U+6C83 —— 氵 + 夭   7 画
# 部件分区：氵 x 61..263；夭 x 291..939
# --------------------------------------------------------------------------
def g_aku() -> Glyph:
    g = Glyph(name="uni6C83", advance=1000, unicode=0x6C83,
              note="沃：左氵，右夭")
    dot_up(g, 196, 752, w=104, h=132, slant=26)  # 氵の上点
    dot_up(g, 140, 531, w=104, h=132, slant=26)  # 氵の下点
    g.diag(61, 63, 214, 233, weight=W_SEC)       # 氵的提
    g.diag(774, 815, 380, 627, weight=W_THIN)    # 夭的撇
    g.hbar(316, 939, 458, weight=W_MAIN)         # 夭的横
    g.diag(597, 660, 291, 0, weight=W_SEC)       # 夭的撇
    g.diag(609, 436, 932, 33, weight=W_SEC)      # 夭的捺
    return g


# --------------------------------------------------------------------------
# 23 吏 U+540F —— 一 + 口 + 史   6 画
# 部件分区：上部 x 201..774；下部 x 162..838
# --------------------------------------------------------------------------
def g_ri() -> Glyph:
    g = Glyph(name="uni540F", advance=1000, unicode=0x540F,
              note="吏：上一，下口，再下史")
    g.hbar(201, 774, 687, weight=W_MAIN)          # 吏的一
    g.vbar(265, 359, 551, weight=W_THIN)          # 口的左竖
    g.hbar(280, 715, 552, weight=W_MAIN)          # 口的横折（横）
    g.vbar(725, 413, 560, weight=W_THIN)          # 口的横折（折）
    g.hbar(304, 730, 391, weight=W_THIN)          # 口的底横
    g.vbar(490, 340, 815, weight=W_SEC)           # 史的撇（上段）
    g.diag(488, 343, 162, 0, weight=W_SEC)        # 史的撇（下段）
    g.diag(303, 299, 838, 10, weight=W_SEC)       # 史的捺
    return g


# --------------------------------------------------------------------------
# 24 侶 U+4FB6 —— 亻 + 呂   9 画
# 部件分区：亻 x 88..310；呂 x 420..912
# --------------------------------------------------------------------------
def g_ro() -> Glyph:
    g = Glyph(name="uni4FB6", advance=1000, unicode=0x4FB6,
              note="侶：左亻，右呂")
    g.diag(310, 817, 88, 379, weight=W_SEC)       # 亻的撇
    g.vbar(246, 0, 563, weight=W_SEC)            # 亻的竖
    g.vbar(455, 521, 793, weight=W_THIN)          # 呂上口的左竖
    g.hbar(452, 830, 795, weight=W_MAIN)          # 上口的横折（横）
    g.vbar(832, 578, 795, weight=W_SEC)           # 上口的横折（折）
    g.hbar(492, 828, 559, weight=W_THIN)         # 上口的底横
    g.diag(631, 529, 558, 334, weight=W_THIN)     # 呂的撇
    g.vbar(446, 7, 315, weight=W_THIN)           # 下口的左竖
    g.hbar(439, 888, 320, weight=W_MAIN)          # 下口的横折（横）
    g.vbar(890, 56, 320, weight=W_SEC)           # 下口的横折（折）
    g.hbar(478, 881, 43, weight=W_THIN)          # 下口的底横
    return g


# --------------------------------------------------------------------------
# 25 弄 U+5F04 —— 王 + 廾   7 画
# 部件分区：王 x 127..880；廾 x 114..886
# --------------------------------------------------------------------------
def g_ryo() -> Glyph:
    g = Glyph(name="uni5F04", advance=1000, unicode=0x5F04,
              note="弄：上王，下廾")
    g.hbar(210, 771, 801, weight=W_MAIN)          # 王的上横
    g.vbar(479, 518, 793, weight=W_SEC)           # 王的竖
    g.hbar(255, 721, 665, weight=W_SEC)           # 王的中横
    g.hbar(127, 880, 507, weight=W_MAIN)          # 王的下横
    g.hbar(114, 886, 329, weight=W_MAIN)          # 廾的横
    g.diag(370, 445, 360, 245, weight=W_SEC)      # 廾的撇（上段）
    g.diag(360, 245, 158, 29, weight=W_SEC)       # 廾的撇（下段）
    g.vbar(626, 0, 473, weight=W_SEC)            # 廾的竖
    return g


# --------------------------------------------------------------------------
# 26 刹 U+5239 —— 杀 + 刂   8 画
# 部件分区：杀 x 121..538；刂 x 658..874
# --------------------------------------------------------------------------
def g_satsu2() -> Glyph:
    g = Glyph(name="uni5239", advance=1000, unicode=0x5239,
              note="刹：左杀，右刂")
    g.diag(469, 815, 169, 546, weight=W_THIN)     # 杀的撇
    g.diag(215, 761, 507, 568, weight=W_THIN)     # 杀的捺
    g.hbar(126, 538, 412, weight=W_MAIN)          # 杀的一
    g.vbar(361, 0, 558, weight=W_SEC)            # 杀的竖
    g.diag(365, 392, 121, 115, weight=W_SEC)      # 杀的撇
    g.diag(404, 326, 518, 214, weight=W_THIN)     # 杀的捺
    g.vbar(666, 294, 704, weight=W_THIN)          # 刂的短竖
    g.vbar(868, 89, 805, weight=W_SEC)            # 刂的竖钩
    g.diag(866, 60, 826, 36, weight=W_THIN)       # 刂的钩
    return g


# --------------------------------------------------------------------------
# 27 拉 U+62C9 —— 扌 + 立   8 画
# 部件分区：扌 x 60..354；立 x 332..940
# --------------------------------------------------------------------------
def g_ration() -> Glyph:
    g = Glyph(name="uni62C9", advance=1000, unicode=0x62C9,
              note="拉：左扌，右立")
    g.hbar(70, 353, 592, weight=W_MAIN)           # 扌的横
    g.vbar(232, 57, 800, weight=W_SEC)            # 扌的竖钩
    g.diag(230, 40, 195, 12, weight=W_THIN)       # 扌的钩
    g.diag(60, 298, 354, 445, weight=W_SEC)       # 扌的提
    dot_up(g, 623, 690, w=84, h=170, slant=0)     # 立的竖点
    g.hbar(400, 886, 575, weight=W_MAIN)          # 立的上横
    g.diag(494, 520, 534, 92, weight=W_THIN)      # 立的左点
    g.diag(765, 554, 710, 92, weight=W_THIN)      # 立的右点
    g.hbar(332, 940, 75, weight=W_MAIN)           # 立的下横
    return g


def build() -> list[Glyph]:
    return [
        g_hou(), g_arc(), g_botsu(), g_i(), g_fu(), g_dan(), g_u(), g_shiki(),
        g_wan(), g_in(), g_kaku(), g_gi(), g_sai(), g_san(), g_satsu(), g_tai(),
        g_jo(), g_ni(), g_chi(), g_boku(), g_mai(), g_ya(), g_aku(), g_ri(),
        g_ro(), g_ryo(), g_satsu2(), g_ration(),
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-021.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
