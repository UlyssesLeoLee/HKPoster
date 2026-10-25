"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-009。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
- 字面框 x 60..940 / y 0..820（与繁体汉字完全一致），advance = 1000，
  y 向上、基线 y=0；ascender 880 / descender -120。
- 笔画权重：主 96 / 次 92 / 细 84 / 点 84–96（与 zh-HK 繁体同一档）。
- 本批密度接近（6–9 画），同族部件在批内**复用同一套坐标与笔画拆法**，
  只做位置/大小的光学校正（docs/03 GLY-004）：
    氵 = _sansui（油/江/波/洋）
    辶 = _shinnyou（返/途/迫）
    亻 = _ninben（便/伸）
    扌 = _tehen（抜）
    土 = _tsuchihen（均）
    糸 = _ito（紀/級）
- 横画中心线内缩半个笔宽，保证墨迹上缘齐 820 / 下缘齐 0
  （参考 font-src/src/hkposter-latin.py 的 bar_top / bar_base 做法）。
- 海报端点：横竖撇捺一律平切硬边；点与短撇用斜切平行四边形 g.dot(...)
  —— 点（丶，右下行）slant=-14、短撇（丿，左下行）slant=26，
  同类同族同档（GLY-003 / GLY-004）。
- 密排处横画叠横画内白 ≥ 24；竖与竖之间 ≥ 60（GLY-006）。
- 结构性封闭的字（囗/日/目/且/貝 一类）墨量率必然偏高，
  集成方已裁定允许；不为压阈值把字压畸形。
- 字形骨架逐字对照参照字体 M PLUS 1p Black（E:/hkposter-refs/，SIL OFL 1.1）
  核验：只取比例与骨架，不描轮廓。核验后修正的三处结构性错误：
  返（反不是“厂”长撇）、妻（上半是 一 + ヨ + 丨，竖要出头）、
  背（北的横在左上、竖出头；月是三格）。
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

# 全批斜切档位（同类同族同档，GLY-004）
# hkbuild 的 g.dot：slant 为正 = 平行四边形上缘右移（"/" 形，短撇用）；
# slant 为负 = 上缘左移（"\" 形，点/捺尖用）。
# 参照 M PLUS 1p Black 实测：氵 的点、羊/幸 的 丷左点均为上缘左移（"\"）。
SLANT_DOT = -14   # 点（丶）：右下行，平行四边形上缘左移
SLANT_PIE = 26    # 短撇（丿）：左下行，平行四边形上缘右移


# --------------------------------------------------------------------------
# 对齐辅助：横画墨迹上缘/下缘对齐字面框
# --------------------------------------------------------------------------
def hbar_top(g, x1, x2, weight=W_MAIN):
    """横画：墨迹上缘对齐 y=820。"""
    g.hbar(x1, x2, 820 - weight / 2.0, weight=weight)


def hbar_base(g, x1, x2, weight=W_MAIN):
    """横画：墨迹下缘对齐 y=0（基线）。"""
    g.hbar(x1, x2, weight / 2.0, weight=weight)


def kamae(g, x1, x2, y1, y2, weight=W_MAIN):
    """方框：墨迹外缘 x1..x2 / y1..y2，内白自动成洞。"""
    half = weight / 2.0
    g.vbar(x1 + half, y1, y2, weight=weight)
    g.vbar(x2 - half, y1, y2, weight=weight)
    g.hbar(x1, x2, y2 - half, weight=weight)
    g.hbar(x1, x2, y1 + half, weight=weight)


# --------------------------------------------------------------------------
# 同族部件（批内固定坐标）
# --------------------------------------------------------------------------
def _sansui(g):
    """氵 さんずい（3 画）：上点 / 中点 / 提。批内固定。"""
    g.dot(165, 690, w=96, h=120, slant=SLANT_DOT)   # 上点
    g.dot(140, 470, w=96, h=120, slant=SLANT_DOT)   # 中点
    g.diag(120, 215, 290, 345, weight=W_SEC)        # 提（右下上扬）


def _shinnyou(g):
    """辶 しんにょう（3 画）：丶 / 折 / 底の払。批内固定。"""
    g.dot(140, 630, w=96, h=120, slant=SLANT_DOT)  # 丶
    g.diag(125, 520, 165, 420, weight=W_SEC)        # 折之上
    g.hbar(160, 250, 390, weight=W_SEC)             # 折之横
    g.diag(242, 405, 220, 130, weight=W_SEC)        # 折之払（与底払相接）
    g.diag(228, 78, 890, 160, weight=W_MAIN)        # 底之払（右下上扬）


def _ninben(g):
    """亻 にんべん（2 画）：丿 / 丨。批内固定。"""
    g.diag(265, 805, 115, 485, weight=W_SEC)        # 丿
    g.vbar(210, 60, 540, weight=W_SEC)              # 丨


def _tehen(g):
    """扌 てへん（3 画）：一 / 亅 / 提。"""
    g.hbar(60, 340, 640, weight=W_SEC)              # 一
    g.vbar(200, 120, 820, weight=W_SEC)             # 亅（竖）
    g.diag(200, 128, 132, 166, weight=W_THIN)       # 亅の钩
    g.diag(80, 320, 300, 415, weight=W_SEC)         # 提


def _tsuchihen(g):
    """土 つちへん（3 画）：一 / 丨 / 提。"""
    g.hbar(60, 330, 640, weight=W_SEC)              # 一
    g.vbar(195, 180, 640, weight=W_SEC)             # 丨
    g.diag(80, 180, 320, 270, weight=W_SEC)         # 提


def _ito(g):
    """糸（6 画）：幺（撇折×2 + 丶）+ 小（亅 + 丿 + 丶）。批内固定。"""
    # 幺
    g.diag(245, 810, 150, 680, weight=W_THIN)
    g.diag(150, 680, 252, 620, weight=W_THIN)
    g.diag(232, 690, 132, 540, weight=W_THIN)
    g.diag(132, 540, 242, 470, weight=W_THIN)
    g.dot(268, 540, w=W_THIN, h=100, slant=SLANT_DOT)              # 幺の丶
    # 小
    g.vbar(200, 120, 420, weight=W_SEC)
    g.diag(200, 126, 146, 162, weight=W_THIN)
    g.diag(176, 400, 96, 232, weight=W_THIN)                       # 丿
    g.dot(292, 320, w=W_THIN, h=100, slant=SLANT_DOT)              # 丶


# --------------------------------------------------------------------------
# 单字
# --------------------------------------------------------------------------
def _uni8FD4() -> Glyph:
    """返 U+8FD4 —— ⿺辶反（spec 6 画）。

    部件分区：辶 = 左侧及底部（_shinnyou 固定坐标）；反 = 右上 x 360..920。
    反按参照字体核验为 **丿 + 一 + 又**（4 画）：第一笔是横画左上方的短撇，
    只在横画上缘露出个头，不是一个下贯到字面中部的“厂”长撇
    （长撇是 厂/广 一类偏旁的写法，用在这里会读成“反=厂又”）。
    又 = フ（横 + 撇）+ 乀，二者在 x≈700 处交叠。
    """
    g = Glyph("uni8FD4", advance=1000, unicode=0x8FD4, note="返 ⿺辶反")
    _shinnyou(g)
    g.diag(450, 815, 360, 665, weight=W_SEC)             # 反の丿（出头于横上）
    g.hbar(360, 915, 700, weight=W_MAIN)                 # 反の一
    g.hbar(485, 920, 580, weight=W_SEC)                  # 又の横
    g.diag(895, 585, 640, 375, weight=W_MAIN)            # 又の撇
    g.diag(500, 555, 880, 300, weight=W_SEC)             # 又の捺
    return g


def _uni6CB9() -> Glyph:
    """油 U+6CB9 —— ⿰氵由（spec 8 画）。

    部件分区：氵 = 左 x 60..318（_sansui）；由 = 右 x 340..920。
    由 = 田 + 中竖出头：方框墨迹 x 340..920 / y 60..760，
    中竖 x=630 由 y=60 直上到 820（穿出框顶 60 单位），
    中横 y=410 贯穿框内，内白四格各 ≥ 146×206。
    """
    g = Glyph("uni6CB9", advance=1000, unicode=0x6CB9, note="油 ⿰氵由")
    _sansui(g)
    kamae(g, 340, 920, 60, 760, weight=W_MAIN)          # 由の框
    g.hbar(340, 920, 410, weight=W_MAIN)                 # 由の中横
    g.vbar(630, 60, 820, weight=W_MAIN)                  # 由の中竖（出头）
    return g


def _uni59BB() -> Glyph:
    """妻 U+59BB —— ⿱（一 + ヨ + 丨）女（spec 8 画）。

    部件分区（按参照字体核验）：上半 y 234..820 = 一（最上横）+ ヨ（横折 + 一 + 一）+
    丨（贯通，顶端出头 20 单位）；下半 y 0..430 = 女。
    4 横自上而下 752 / 600 / 440 / 280，其中 2、3 收细到 92，
    横叠横内白 ≥ 58；ヨ的右边竖（x 844..936）与中竖相距 296；
    女的撇点与长撇从 ヨ 的下横之间伸出，与 ヨ 的中横相交。
    """
    g = Glyph("uni59BB", advance=1000, unicode=0x59BB, note="妻")
    # 上部：一 + ヨ + 丨
    g.hbar(60, 930, 752, weight=W_MAIN)                  # 一（最上横）
    g.vbar(500, 240, 820, weight=W_MAIN)                  # 丨（顶端出头）
    g.hbar(120, 900, 600, weight=W_SEC)                   # ヨの横（折の横）
    g.vbar(890, 240, 646, weight=W_SEC)                   # ヨの折（右边竖）
    g.hbar(60, 900, 440, weight=W_SEC)                    # ヨの中横
    g.hbar(60, 930, 280, weight=W_SEC)                    # ヨの下横
    # 下部 女
    g.diag(500, 510, 400, 330, weight=W_THIN)             # 撇点 上段
    g.diag(400, 330, 545, 50, weight=W_THIN)              # 撇点 下段
    g.diag(655, 470, 300, 40, weight=W_THIN)              # 长撇
    g.hbar(200, 740, 150, weight=W_SEC)                   # 一
    return g


def _uni5BA3() -> Glyph:
    """宣 U+5BA3 —— ⿱宀亘（spec 9 画）。

    部件分区：宀 占 y 540..814（丶 + 冖 + 两短垂）；
    亘 占 y 0..566 = 一 + 日 + 一，日的框墨迹 x 290..710 / y 120..444。
    宀 与 亘 之间留白 ≥ 24；日内白三格 ≥ 24。
    """
    g = Glyph("uni5BA3", advance=1000, unicode=0x5BA3, note="宣 ⿱宀亘")
    # 宀
    g.dot(500, 770, w=88, h=88, slant=SLANT_DOT)         # 丶
    g.hbar(150, 850, 654, weight=W_SEC)                  # 冖の横
    g.vbar(194, 600, 654, weight=W_SEC)                  # 冖の左垂
    g.vbar(806, 600, 654, weight=W_SEC)                  # 冖の右垂
    # 亘
    g.hbar(230, 770, 520, weight=W_SEC)                  # 一
    kamae(g, 290, 710, 120, 444, weight=W_MAIN)          # 日の框
    g.hbar(290, 710, 282, weight=W_THIN)                 # 日の中横
    hbar_base(g, 200, 800, weight=W_MAIN)                # 亘の底一
    return g


def _uni80CC() -> Glyph:
    """背 U+80CC —— ⿱北月（spec 9 画）。

    部件分区（按参照字体核验）：
    北 = 左 丬（丨 顶出头 + 位于左上、向左出锋的横）+ 右 匕（丿 + 竖带右钩），
        占 y 470..820；横不是中部横臂，且竖要高出横画。
    月 = y 0..436，四道横（上 / 内二 / 下）＝三格，格间内白 28–32。
    """
    g = Glyph("uni80CC", advance=1000, unicode=0x80CC, note="背 ⿱北月")
    # 北 —— 左 丬
    g.vbar(280, 470, 820, weight=W_SEC)                  # 丨（顶出头）
    g.hbar(60, 320, 750, weight=W_SEC)                   # 左上の横
    # 北 —— 右 匕
    g.diag(900, 810, 600, 700, weight=W_SEC)            # 匕の丿
    g.vbar(560, 470, 720, weight=W_SEC)                  # 匕の竖
    g.diag(560, 490, 700, 440, weight=W_SEC)             # 钩
    # 月
    g.diag(420, 400, 380, 40, weight=W_SEC)              # 丿
    g.hbar(380, 900, 390, weight=W_SEC)                  # 𠃍 の横
    g.vbar(854, 40, 390, weight=W_SEC)                   # 𠃍 の折
    g.hbar(380, 900, 274, weight=W_THIN)                 # 一
    g.hbar(380, 900, 162, weight=W_THIN)                 # 一
    hbar_base(g, 380, 900, weight=W_SEC)                 # 一
    return g


def _uni662D() -> Glyph:
    """昭 U+662D —— ⿰日召（spec 9 画）。

    部件分区：日 占 x 60..380 / y 100..740（窄长日，中横居中）；
    召 占 x 430..810：刀（𠃌 + 丿）在上 y 500..744，口在下 y 0..380。
    """
    g = Glyph("uni662D", advance=1000, unicode=0x662D, note="昭 ⿰日召")
    # 日
    g.vbar(108, 100, 740, weight=W_SEC)
    g.vbar(332, 100, 740, weight=W_SEC)
    g.hbar(60, 380, 694, weight=W_SEC)
    g.hbar(60, 380, 146, weight=W_SEC)
    g.hbar(60, 380, 420, weight=W_THIN)
    # 召 —— 刀
    g.hbar(430, 810, 700, weight=W_SEC)
    g.vbar(766, 500, 700, weight=W_SEC)
    g.diag(766, 505, 700, 540, weight=W_THIN)            # 钩
    g.diag(620, 700, 470, 480, weight=W_SEC)             # 丿
    # 召 —— 口
    g.vbar(474, 0, 380, weight=W_MAIN)
    g.vbar(766, 0, 380, weight=W_MAIN)
    g.hbar(430, 810, 334, weight=W_MAIN)
    hbar_base(g, 430, 810, weight=W_MAIN)
    return g


def _uni6C5F() -> Glyph:
    """江 U+6C5F —— ⿰氵工（spec 6 画）。

    部件分区：氵 = 左（_sansui）；工 = 右 x 340..930，
    上横墨迹齐 820、下横齐基线，中竖贯通两横。
    """
    g = Glyph("uni6C5F", advance=1000, unicode=0x6C5F, note="江 ⿰氵工")
    _sansui(g)
    hbar_top(g, 340, 930, weight=W_MAIN)
    hbar_base(g, 340, 930, weight=W_MAIN)
    g.vbar(635, 48, 772, weight=W_MAIN)
    return g


def _uni5409() -> Glyph:
    """吉 U+5409 —— ⿱士口（spec 6 画）。

    部件分区：士 占 y 554..820（上横长 200..800、下横短 280..720、中竖）；
    口 占 y 0..500，墨迹 x 260..740。
    """
    g = Glyph("uni5409", advance=1000, unicode=0x5409, note="吉 ⿱士口")
    g.hbar(200, 800, 772, weight=W_MAIN)                 # 士の上横
    g.vbar(500, 560, 772, weight=W_MAIN)                 # 士の竖
    g.hbar(280, 720, 600, weight=W_SEC)                  # 士の下横
    g.vbar(306, 0, 500, weight=W_MAIN)                   # 口の左竖
    g.vbar(694, 0, 500, weight=W_MAIN)                   # 口の右竖
    g.hbar(260, 740, 452, weight=W_MAIN)                 # 口の横
    hbar_base(g, 260, 740, weight=W_MAIN)                # 口の底
    return g


def _uni5747() -> Glyph:
    """均 U+5747 —— ⿰土勻（spec 7 画）。

    部件分区：土 = 左 x 60..330（一 / 丨 / 提）；
    勻 = 右 x 400..900：勹（丿 + 横折钩带左钩）包住 冫（丶 + 提）。
    冫的提按参照比例收短（x 450..720），不抵到勹的右边竖。
    """
    g = Glyph("uni5747", advance=1000, unicode=0x5747, note="均 ⿰土勻")
    _tsuchihen(g)
    # 勹
    g.diag(520, 800, 420, 520, weight=W_SEC)             # 丿
    g.hbar(480, 900, 760, weight=W_SEC)                  # 横
    g.vbar(854, 420, 760, weight=W_SEC)                  # 折
    g.diag(854, 425, 790, 460, weight=W_THIN)            # 钩
    # 冫
    g.dot(640, 520, w=W_SEC, h=110, slant=SLANT_DOT)     # 丶
    g.diag(450, 320, 720, 440, weight=W_SEC)             # 提
    return g


def _uni9014() -> Glyph:
    """途 U+9014 —— ⿺辶余（spec 9 画）。

    部件分区：辶 = 左下（_shinnyou）；余 = 右上 x 370..910，
    人（丿 + 乀）在顶 y 640..810，下接一 + 朩（一 / 亅 / 丿 / 丶）。
    底部余的部件压在辶の底の払之上（留白 ≥ 100）。
    """
    g = Glyph("uni9014", advance=1000, unicode=0x9014, note="途 ⿺辶余")
    _shinnyou(g)
    # 余
    g.diag(640, 800, 420, 640, weight=W_SEC)             # 人の丿
    g.diag(640, 800, 870, 660, weight=W_SEC)             # 人の乀
    g.hbar(370, 910, 600, weight=W_SEC)                  # 一
    g.hbar(480, 800, 470, weight=W_THIN)                 # 朩の一
    g.vbar(640, 280, 470, weight=W_SEC)                  # 朩の竖
    g.diag(600, 420, 480, 300, weight=W_THIN)            # 朩の丿
    g.dot(740, 330, w=W_THIN, h=100, slant=SLANT_DOT)    # 朩の丶
    return g


def _uni82B8() -> Glyph:
    """芸 U+82B8 —— ⿱艹云（spec 7 画）。

    部件分区：艹 占 y 640..820（一 + 两竖穿出）；
    云 占 y 48..606：二（两横）+ 厶（丿折 + 丶）。
    """
    g = Glyph("uni82B8", advance=1000, unicode=0x82B8, note="芸 ⿱艹云")
    # 艹
    g.hbar(120, 880, 730, weight=W_SEC)
    g.vbar(320, 640, 820, weight=W_SEC)
    g.vbar(680, 640, 820, weight=W_SEC)
    # 云
    g.hbar(200, 800, 560, weight=W_SEC)                  # 一
    g.hbar(160, 840, 420, weight=W_SEC)                  # 一
    g.diag(540, 320, 400, 110, weight=W_SEC)             # 厶の丿折
    g.hbar(400, 640, 92, weight=W_SEC)                   # 厶の折
    g.dot(700, 190, w=W_SEC, h=110, slant=SLANT_DOT)     # 厶の丶
    return g


def _uni7687() -> Glyph:
    """皇 U+7687 —— ⿱白王（spec 9 画）。

    部件分区：白 占 y 440..810（丿 + 日）；王 占 y 0..418（三横 + 中竖）。
    白の框墨迹 x 280..720 / y 440..770，中横减细至 84 保内白 ≥ 31。
    """
    g = Glyph("uni7687", advance=1000, unicode=0x7687, note="皇 ⿱白王")
    # 白
    g.diag(352, 806, 286, 752, weight=W_THIN)            # 丿
    g.vbar(328, 440, 770, weight=W_SEC)
    g.vbar(672, 440, 770, weight=W_SEC)
    g.hbar(280, 720, 724, weight=W_SEC)
    g.hbar(280, 720, 486, weight=W_SEC)
    g.hbar(280, 720, 605, weight=W_THIN)                 # 中横
    # 王
    g.hbar(180, 820, 360, weight=W_MAIN)
    g.hbar(230, 770, 220, weight=W_SEC)
    hbar_base(g, 140, 860, weight=W_MAIN)
    g.vbar(500, 48, 360, weight=W_MAIN)
    return g


def _uni629C() -> Glyph:
    """抜 U+629C —— ⿰扌友（spec 7 画）。

    部件分区：扌 = 左 x 60..340（一 / 亅带钩 / 提）；
    友 = 右 x 366..920：一（顶）+ 丿（长撇）+ 又（横撇 + 捺）。
    友の丿自 y=800 穿一而下到 330，捺自左上向右下到底。
    """
    g = Glyph("uni629C", advance=1000, unicode=0x629C, note="抜 ⿰扌友")
    _tehen(g)
    # 友
    g.hbar(430, 900, 700, weight=W_SEC)                  # 一
    g.diag(520, 800, 390, 330, weight=W_SEC)             # 长撇
    g.hbar(450, 880, 420, weight=W_SEC)                  # 又の横
    g.diag(856, 420, 620, 230, weight=W_SEC)             # 又の撇
    g.diag(480, 400, 915, 40, weight=W_MAIN)             # 又の捺
    return g


def _uni4FBF() -> Glyph:
    """便 U+4FBF —— ⿰亻更（spec 9 画）。

    部件分区：亻 = 左（_ninben）；更 = 右 x 394..940：
    顶一 + 曰（框含中横）+ 穿框的丿 / 乀 交叠于 x≈640。
    """
    g = Glyph("uni4FBF", advance=1000, unicode=0x4FBF, note="便 ⿰亻更")
    _ninben(g)
    g.hbar(360, 940, 760, weight=W_SEC)                  # 一
    g.vbar(446, 380, 700, weight=W_SEC)                  # 曰の左竖
    g.vbar(854, 380, 700, weight=W_SEC)                  # 曰の右竖
    g.hbar(400, 900, 654, weight=W_SEC)                  # 曰の上
    g.hbar(400, 900, 540, weight=W_THIN)                 # 曰の中横
    g.hbar(400, 900, 426, weight=W_SEC)                  # 曰の底
    g.diag(790, 740, 450, 60, weight=W_SEC)              # 丿
    g.diag(540, 600, 900, 60, weight=W_SEC)              # 乀
    return g


def _uni4F38() -> Glyph:
    """伸 U+4F38 —— ⿰亻申（spec 7 画）。

    部件分区：亻 = 左（_ninben）；申 = 右 x 400..900：
    框 y 300..740，中竖 x=650 上下各出头 60 单位。
    """
    g = Glyph("uni4F38", advance=1000, unicode=0x4F38, note="伸 ⿰亻申")
    _ninben(g)
    g.vbar(446, 300, 740, weight=W_SEC)
    g.vbar(854, 300, 740, weight=W_SEC)
    g.hbar(400, 900, 694, weight=W_SEC)
    g.hbar(400, 900, 346, weight=W_SEC)
    g.hbar(400, 900, 520, weight=W_THIN)                 # 中横
    g.vbar(650, 30, 800, weight=W_SEC)                   # 贯通的竖
    return g


def _uni6CE2() -> Glyph:
    """波 U+6CE2 —— ⿰氵皮（spec 8 画）。

    部件分区：氵 = 左（_sansui）；皮 = 右 x 366..940：
    乛（横 + 钩）在顶，长丿自右上斜贯至左下，
    丨 在中，㇇（横 + 撇）与乀在 x≈690 交叠。
    """
    g = Glyph("uni6CE2", advance=1000, unicode=0x6CE2, note="波 ⿰氵皮")
    _sansui(g)
    g.hbar(430, 900, 765, weight=W_SEC)                  # 乛の横
    g.vbar(856, 700, 765, weight=W_SEC)                  # 乛の折
    g.diag(856, 705, 800, 740, weight=W_THIN)            # 钩
    g.diag(810, 800, 470, 250, weight=W_SEC)             # 长丿
    g.vbar(660, 420, 765, weight=W_SEC)                  # 丨
    g.hbar(500, 880, 400, weight=W_SEC)                  # ㇇の横
    g.diag(856, 410, 660, 240, weight=W_SEC)             # ㇇の撇
    g.diag(530, 400, 920, 60, weight=W_MAIN)             # 乀
    return g


def _uni72D9() -> Glyph:
    """狙 U+72D9 —— ⿰犭且（spec 8 画）。

    部件分区：犭 = 左 x 60..340（丿 / 弯钩 / 长丿）；
    且 = 右 x 340..940：冂 + 两分隔横 + 底横（底横左右出头）。
    """
    g = Glyph("uni72D9", advance=1000, unicode=0x72D9, note="狙 ⿰犭且")
    # 犭
    g.diag(230, 790, 130, 680, weight=W_THIN)            # 上丿
    g.vbar(200, 130, 690, weight=W_SEC)                  # 弯钩
    g.diag(200, 135, 130, 170, weight=W_THIN)            # 钩
    g.diag(300, 700, 105, 300, weight=W_SEC)             # 长丿
    # 且
    g.vbar(386, 136, 746, weight=W_SEC)
    g.vbar(894, 136, 746, weight=W_SEC)
    g.hbar(340, 940, 700, weight=W_SEC)
    g.hbar(340, 940, 596, weight=W_THIN)
    g.hbar(340, 940, 470, weight=W_THIN)
    g.hbar(340, 940, 136, weight=W_SEC)                  # 出头的底横
    return g


def _uni5EF6() -> Glyph:
    """延 U+5EF6 —— ⿺廴正（spec 7 画）。

    部件分区（按参照字体核验）：廴 = 左上折块（横 + 竖）+ 下行斜笔 +
    贯通到底的底之払（不是两个长横组成的“Z”形）；
    正 = 右 x 380..940（一 + 丨 + 一 + 丨 + 底一）。
    """
    g = Glyph("uni5EF6", advance=1000, unicode=0x5EF6, note="延 ⿺廴正")
    # 廴
    g.hbar(100, 230, 680, weight=W_SEC)                   # 折の横
    g.vbar(165, 500, 680, weight=W_SEC)                   # 折の竖
    g.diag(200, 520, 110, 270, weight=W_SEC)             # 下行斜笔
    g.diag(105, 200, 925, 85, weight=W_MAIN)              # 底の払
    # 正
    hbar_top(g, 380, 940, weight=W_SEC)
    g.vbar(640, 330, 772, weight=W_SEC)
    g.hbar(640, 900, 520, weight=W_THIN)
    g.vbar(440, 284, 520, weight=W_SEC)
    g.hbar(380, 940, 330, weight=W_SEC)
    return g


def _uni7FBD() -> Glyph:
    """羽 U+7FBD —— ⿰习习（spec 6 画）。

    部件分区：左半 x 60..400、右半 x 490..830（同一坐标 +430 平移），
    每半 = ㇆（横 + 竖带左钩）+ 内点（斜切平行四边形）+ 内提。
    两半同族同档，批内观感统一。
    """
    g = Glyph("uni7FBD", advance=1000, unicode=0x7FBD, note="羽 ⿰习习")
    for off in (0, 430):
        g.hbar(60 + off, 400 + off, 772, weight=W_SEC)            # ㇆ の横
        g.vbar(354 + off, 120, 772, weight=W_SEC)                 # ㇆ の折
        g.diag(354 + off, 125, 280 + off, 160, weight=W_THIN)     # 钩
        g.dot(190 + off, 620, w=W_THIN, h=100, slant=SLANT_DOT)   # 内点
        g.diag(150 + off, 380, 300 + off, 460, weight=W_SEC)      # 内提
    return g


def _uni52AA() -> Glyph:
    """努 U+52AA —— ⿱（女又）力（spec 7 画）。

    部件分区：女 = 左上 x 60..400 / y 400..820（撇点 + 长撇 + 一）；
    又 = 右上 x 450..915；力 = 下 x 60..790（横折钩 + 撇），
    横画贯通全宽、竖钩偏右（按参照比例）。
    """
    g = Glyph("uni52AA", advance=1000, unicode=0x52AA, note="努 ⿱女又力")
    # 女
    g.diag(330, 810, 215, 625, weight=W_THIN)
    g.diag(215, 625, 340, 440, weight=W_THIN)
    g.diag(390, 800, 120, 400, weight=W_THIN)
    g.hbar(60, 400, 640, weight=W_SEC)
    # 又
    g.hbar(450, 900, 700, weight=W_SEC)
    g.diag(876, 710, 620, 480, weight=W_SEC)
    g.diag(480, 690, 915, 470, weight=W_SEC)
    # 力
    g.hbar(60, 790, 330, weight=W_SEC)
    g.vbar(700, 120, 330, weight=W_SEC)
    g.diag(700, 125, 625, 160, weight=W_THIN)
    g.diag(470, 330, 230, 60, weight=W_SEC)
    return g


def _uni56FA() -> Glyph:
    """固 U+56FA —— ⿴囗古（spec 8 画）。

    部件分区：囗 = 外框墨迹 x 60..940 / y 0..820；
    古 = 内部居中（十 + 口），口的内白 ≥ 104。
    """
    g = Glyph("uni56FA", advance=1000, unicode=0x56FA, note="固 ⿴囗古")
    g.vbar(108, 0, 820, weight=W_MAIN)
    g.vbar(892, 0, 820, weight=W_MAIN)
    hbar_top(g, 60, 940, weight=W_MAIN)
    hbar_base(g, 60, 940, weight=W_MAIN)
    # 古
    g.hbar(300, 700, 560, weight=W_SEC)                  # 十の一
    g.vbar(500, 420, 700, weight=W_SEC)                  # 十の竖
    g.vbar(406, 180, 440, weight=W_SEC)                  # 口の左竖
    g.vbar(594, 180, 440, weight=W_SEC)                  # 口の右竖
    g.hbar(360, 640, 396, weight=W_SEC)                  # 口の横
    g.hbar(360, 640, 224, weight=W_SEC)                  # 口の底
    return g


def _uni5247() -> Glyph:
    """則 U+5247 —— ⿰貝刂（spec 9 画）。

    部件分区：貝 = 左 x 60..560（目字框 + 两撇捺）；
    刂 = 右（短竖 + 长竖带左钩）。
    """
    g = Glyph("uni5247", advance=1000, unicode=0x5247, note="則 ⿰貝刂")
    # 貝
    g.vbar(108, 280, 800, weight=W_SEC)
    g.vbar(508, 280, 800, weight=W_SEC)
    g.hbar(60, 560, 754, weight=W_SEC)
    g.hbar(60, 560, 610, weight=W_THIN)
    g.hbar(60, 560, 470, weight=W_THIN)
    g.hbar(60, 560, 326, weight=W_SEC)
    g.diag(190, 280, 110, 140, weight=W_THIN)            # 左足
    g.diag(430, 280, 530, 140, weight=W_THIN)            # 右足
    # 刂
    g.vbar(660, 480, 720, weight=W_SEC)
    g.vbar(880, 130, 780, weight=W_SEC)
    g.diag(880, 135, 810, 170, weight=W_THIN)
    return g


def _uni4E71() -> Glyph:
    """乱 U+4E71 —— ⿰舌乚（spec 7 画）。

    部件分区：舌 = 左 x 60..540（丿 + 十 + 口）；
    乚 = 右 x 654..930（竖 + 向右上扬的底）。
    """
    g = Glyph("uni4E71", advance=1000, unicode=0x4E71, note="乱 ⿰舌乚")
    # 舌
    g.diag(100, 690, 520, 745, weight=W_THIN)            # 丿
    g.vbar(310, 360, 720, weight=W_SEC)                  # 丨
    g.hbar(80, 540, 520, weight=W_SEC)                   # 一
    g.vbar(196, 60, 380, weight=W_SEC)                   # 口の左竖
    g.vbar(424, 60, 380, weight=W_SEC)                   # 口の右竖
    g.hbar(150, 470, 334, weight=W_SEC)                  # 口の横
    g.hbar(150, 470, 106, weight=W_SEC)                  # 口の底
    # 乚
    g.vbar(700, 60, 780, weight=W_SEC)
    g.diag(700, 75, 900, 190, weight=W_SEC)
    return g


def _uni6D0B() -> Glyph:
    """洋 U+6D0B —— ⿰氵羊（spec 9 画）。

    部件分区：氵 = 左（_sansui）；羊 = 右 x 360..920：
    丷（两点）+ 三横 + 贯通的竖。
    """
    g = Glyph("uni6D0B", advance=1000, unicode=0x6D0B, note="洋 ⿰氵羊")
    _sansui(g)
    g.dot(450, 780, w=W_SEC, h=110, slant=SLANT_DOT)     # 丷の左（点）
    g.dot(820, 780, w=W_SEC, h=110, slant=SLANT_PIE)     # 丷の右（短撇）
    g.hbar(380, 900, 620, weight=W_SEC)
    g.hbar(400, 880, 460, weight=W_SEC)
    g.hbar(360, 920, 280, weight=W_SEC)
    g.vbar(640, 280, 620, weight=W_SEC)                  # 竖
    return g


def _uni539A() -> Glyph:
    """厚 U+539A —— ⿸厂日子（spec 9 画）。

    部件分区：厂 = 一（齐 820）+ 左长撇（x 110..275）；
    日 = x 280..640 / y 380..700；子 = x 240..780 / y 40..360。
    """
    g = Glyph("uni539A", advance=1000, unicode=0x539A, note="厚 ⿸厂日子")
    hbar_top(g, 60, 940, weight=W_MAIN)                  # 厂の一
    g.diag(230, 800, 110, 200, weight=W_SEC)             # 厂の丿
    # 日
    g.vbar(326, 380, 700, weight=W_SEC)
    g.vbar(594, 380, 700, weight=W_SEC)
    g.hbar(280, 640, 656, weight=W_SEC)
    g.hbar(280, 640, 540, weight=W_THIN)
    g.hbar(280, 640, 424, weight=W_SEC)
    # 子
    g.hbar(300, 700, 320, weight=W_SEC)                  # 子の横
    g.diag(676, 320, 540, 200, weight=W_SEC)             # 横撇
    g.vbar(520, 60, 330, weight=W_SEC)                   # 竖钩
    g.diag(520, 65, 460, 100, weight=W_THIN)
    g.hbar(240, 780, 140, weight=W_MAIN)                 # 子の一
    return g


def _uni56F2() -> Glyph:
    """囲 U+56F2 —— ⿴囗井（spec 7 画）。

    部件分区：囗 = 外框 x 60..940 / y 0..820；井 居中 x 200..800，
    左竖作撇（井の第一竖），右竖作直竖。
    """
    g = Glyph("uni56F2", advance=1000, unicode=0x56F2, note="囲 ⿴囗井")
    g.vbar(108, 0, 820, weight=W_MAIN)
    g.vbar(892, 0, 820, weight=W_MAIN)
    hbar_top(g, 60, 940, weight=W_MAIN)
    hbar_base(g, 60, 940, weight=W_MAIN)
    # 井
    g.hbar(200, 800, 620, weight=W_SEC)
    g.hbar(200, 800, 400, weight=W_SEC)
    g.diag(310, 700, 250, 140, weight=W_SEC)             # 左竖（撇）
    g.vbar(700, 140, 700, weight=W_SEC)                  # 右竖
    return g


def _uni5352() -> Glyph:
    """卒 U+5352 —— ⿱亠从十（spec 8 画）。

    部件分区：亠 = 丶 + 一（y 614..820）；从 = 两个 人（y 390..570）；
    十 = 一 + 竖（竖落到基线）。
    """
    g = Glyph("uni5352", advance=1000, unicode=0x5352, note="卒 ⿱亠从十")
    g.dot(500, 770, w=W_SEC, h=100, slant=SLANT_DOT)     # 亠の丶
    g.hbar(160, 840, 660, weight=W_SEC)                  # 亠の一
    # 从
    g.diag(350, 590, 220, 380, weight=W_SEC)
    g.diag(350, 590, 430, 400, weight=W_SEC)
    g.diag(620, 590, 500, 380, weight=W_SEC)
    g.diag(620, 590, 790, 380, weight=W_SEC)
    # 十
    g.hbar(280, 720, 210, weight=W_MAIN)
    g.vbar(500, 20, 210, weight=W_MAIN)
    return g


def _uni8FEB() -> Glyph:
    """迫 U+8FEB —— ⿺辶白（spec 7 画）。

    部件分区：辶 = 左下（_shinnyou）；白 = 右上 x 380..820，
    丿（短撇）+ 日字框（含中横）。
    """
    g = Glyph("uni8FEB", advance=1000, unicode=0x8FEB, note="迫 ⿺辶白")
    _shinnyou(g)
    g.diag(452, 800, 392, 716, weight=W_THIN)            # 白の丿
    g.vbar(426, 250, 700, weight=W_SEC)
    g.vbar(774, 250, 700, weight=W_SEC)
    g.hbar(380, 820, 654, weight=W_SEC)
    g.hbar(380, 820, 296, weight=W_SEC)
    g.hbar(380, 820, 500, weight=W_THIN)                 # 中横
    return g


def _uni627F() -> Glyph:
    """承 U+627F —— 独体（spec 8 画）。

    部件分区（按参照字体核验）：顶 乛（横 + 自横中部落下的撇）y 600..798；
    贯通的竖 x 514..606；三横 y 258..602；底部左右两扫（丿 / 乀）落地。
    共 8 笔：乛 / 丨 / 三 / 丿 / ㇏。
    """
    g = Glyph("uni627F", advance=1000, unicode=0x627F, note="承")
    g.hbar(360, 720, 752, weight=W_SEC)                  # 乛の横
    g.diag(560, 752, 430, 600, weight=W_SEC)             # 乛の撇（自横的中部落下）
    g.vbar(560, 200, 720, weight=W_SEC)                  # 竖
    g.hbar(300, 780, 560, weight=W_THIN)                 # 一
    g.hbar(280, 800, 430, weight=W_THIN)                 # 一
    g.hbar(260, 820, 300, weight=W_THIN)                 # 一
    g.diag(470, 280, 70, 40, weight=W_SEC)               # 左扫
    g.diag(620, 280, 930, 40, weight=W_SEC)              # 右扫
    return g


def _uni7D00() -> Glyph:
    """紀 U+7D00 —— ⿰糸己（spec 9 画）。

    部件分区：糸 = 左（_ito 固定坐标）；己 = 右 x 420..860
    （㇕ + 一 + 乚带右钩）。
    """
    g = Glyph("uni7D00", advance=1000, unicode=0x7D00, note="紀 ⿰糸己")
    _ito(g)
    g.hbar(420, 860, 714, weight=W_SEC)                  # ㇕ の横
    g.vbar(814, 500, 714, weight=W_SEC)                  # ㇕ の折
    g.hbar(420, 860, 590, weight=W_THIN)                 # 一
    g.vbar(466, 348, 590, weight=W_SEC)                  # 乚の竖
    g.hbar(420, 860, 348, weight=W_SEC)                  # 乚の底
    g.vbar(814, 348, 500, weight=W_SEC)                  # 钩
    return g


def _uni7D1A() -> Glyph:
    """級 U+7D1A —— ⿰糸及（spec 9 画）。

    部件分区：糸 = 左（_ito）；及 = 右 x 420..920
    （丿 + ㇇（横折折撇）+ 乀）。
    """
    g = Glyph("uni7D1A", advance=1000, unicode=0x7D1A, note="級 ⿰糸及")
    _ito(g)
    g.diag(590, 810, 450, 430, weight=W_SEC)             # 丿
    g.hbar(490, 880, 670, weight=W_SEC)                  # ㇇の横
    g.vbar(836, 520, 670, weight=W_SEC)                  # ㇇の折
    g.diag(836, 525, 660, 360, weight=W_SEC)             # ㇇の撇
    g.diag(540, 470, 890, 80, weight=W_MAIN)             # 乀
    return g


def _uni5E78() -> Glyph:
    """幸 U+5E78 —— ⿱土丷干（spec 8 画）。

    部件分区：土 = 顶 y 604..814；丷 = 两点 y 488..592；
    干 = y 30..444（两横 + 贯通的竖落基线）。
    """
    g = Glyph("uni5E78", advance=1000, unicode=0x5E78, note="幸 ⿱土丷干")
    g.hbar(300, 700, 770, weight=W_SEC)                  # 土の一
    g.vbar(500, 620, 770, weight=W_SEC)                  # 土の竖
    g.hbar(240, 760, 650, weight=W_MAIN)                 # 土の底一
    g.dot(360, 540, w=W_SEC, h=104, slant=SLANT_DOT)     # 丷の左（点）
    g.dot(640, 540, w=W_SEC, h=104, slant=SLANT_PIE)     # 丷の右（短撇）
    g.hbar(330, 670, 400, weight=W_SEC)                  # 干の一
    g.hbar(250, 750, 250, weight=W_MAIN)                 # 干の一
    g.vbar(500, 30, 400, weight=W_MAIN)                  # 干の竖
    return g


# --------------------------------------------------------------------------
def build() -> list[Glyph]:
    """本批 32 字（顺序 = 规格字符清单）。"""
    return [
        _uni8FD4(),  # 返
        _uni6CB9(),  # 油
        _uni59BB(),  # 妻
        _uni5BA3(),  # 宣
        _uni80CC(),  # 背
        _uni662D(),  # 昭
        _uni6C5F(),  # 江
        _uni5409(),  # 吉
        _uni5747(),  # 均
        _uni9014(),  # 途
        _uni82B8(),  # 芸
        _uni7687(),  # 皇
        _uni629C(),  # 抜
        _uni4FBF(),  # 便
        _uni4F38(),  # 伸
        _uni6CE2(),  # 波
        _uni72D9(),  # 狙
        _uni5EF6(),  # 延
        _uni7FBD(),  # 羽
        _uni52AA(),  # 努
        _uni56FA(),  # 固
        _uni5247(),  # 則
        _uni4E71(),  # 乱
        _uni6D0B(),  # 洋
        _uni539A(),  # 厚
        _uni56F2(),  # 囲
        _uni5352(),  # 卒
        _uni8FEB(),  # 迫
        _uni627F(),  # 承
        _uni7D00(),  # 紀
        _uni7D1A(),  # 級
        _uni5E78(),  # 幸
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-009.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
