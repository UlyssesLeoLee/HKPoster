"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s3-006。

本批 24 字，笔画范围 10–13，取自 2010 年文化厅《常用漢字表》。

【整体设计取舍】
- 字面框：x 60..940，y 0..820（与繁体汉字同档，便于中英日混排）；advance = 1000。
- 权重档（design-params.json weights.cjk）：主 96 / 次 92 / 细 84 / 点 84；
  高密字（量）额外用 76（W_LIGHT，承 cjk-dense 的 龍/義/警/愛/無/道 既有做法：
  「76 仅用于高密字局部减重」）。
- 端点：横竖撇捺一律平切硬边（hbar / vbar / diag），点与短撇一律斜切平行四边形
  （g.dot），slant 只用既有档位 {0, 26, 14, -14}：
    · slant = +14 → 顶部右移 = 撇向（"/"）：丿、丷右、小左点
    · slant = -14 → 顶部左移 = 捺向（"\\"）：丶、丷左、小右点、辶的点
    · slant =  26 → 短撇向：氵的上点/下点
    · slant =   0 → 竖点：訁的点、亠的点
  （档位与语义取自 cjk-core.py 的小字头实测注释：左撇右捺，slant 正负即撇捺向。）
- 同批同部件复用同一套坐标与笔画拆法（GLY-004）：訁 / 氵 / 木 / 亻 / 彳 / 衤 / 金
  各由一个 _xxx(g) 辅助函数画出，批内所有字共用。
- 笔画角度照标准骨架（参照 M PLUS 1p Black 与 Zen Kaku Gothic New Black 的
  比例与骨架，不描轮廓）；未改任何一条笔画的方向与斜率。
- 密排处（横画叠横画）内白 ≥ 24 单位；竖与竖之间 ≥ 60 单位；量/票 等高密字
  按 GLY-001 局部减重（76）以保住内白。
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
W_LIGHT = 76  # 高密字局部减重（cjk-dense 既有做法）
W_HAIR = 68   # 极密字局部减重（量：九横密排，四道闭腔要留 30 单位）


# ---------------------------------------------------------------------------
# 共用部件（批内统一坐标，GLY-004）
# ---------------------------------------------------------------------------
def _kuchi(g, x1, x2, y_top, y_bot, w):
    """口字框：上横 / 左竖 / 右竖 / 下横，四笔分画（家族既有画法）。"""
    g.hbar(x1, x2, y_top, weight=w)
    g.hbar(x1, x2, y_bot, weight=w)
    g.vbar(x1 + w / 2.0, y_top, y_bot, weight=w)
    g.vbar(x2 - w / 2.0, y_top, y_bot, weight=w)


def _hi(g, x1, x2, y_top, y_mid, y_bot, w):
    """日字框：三横两竖。"""
    g.hbar(x1, x2, y_top, weight=w)
    g.hbar(x1, x2, y_mid, weight=w)
    g.hbar(x1, x2, y_bot, weight=w)
    g.vbar(x1 + w / 2.0, y_top, y_bot, weight=w)
    g.vbar(x2 - w / 2.0, y_top, y_bot, weight=w)


def _ta(g, x1, x2, y_top, y_mid, y_bot, w, x_mid):
    """田字框：日 + 中竖。"""
    _hi(g, x1, x2, y_top, y_mid, y_bot, w)
    g.vbar(x_mid, y_top, y_bot, weight=w)


def _gen(g):
    """訁（言偏）：x 60..400，竖点 + 三横 + 口。"""
    g.dot(230, 772, w=112, h=96, slant=0)      # 訁的点（竖点档 0）
    g.hbar(80, 380, 640, weight=W_SEC)         # 横 1
    g.hbar(80, 380, 520, weight=W_SEC)         # 横 2
    g.hbar(80, 380, 400, weight=W_SEC)         # 横 3
    g.hbar(80, 380, 280, weight=W_SEC)         # 口的上横
    g.hbar(80, 380, 42, weight=W_THIN)         # 口的下横
    g.vbar(122, 280, 42, weight=W_THIN)        # 口的左竖
    g.vbar(338, 280, 42, weight=W_THIN)        # 口的右竖


def _sanzui(g):
    """氵：x 60..290，两短撇（slant 26）+ 提。"""
    g.dot(150, 700, w=94, h=126, slant=26)     # 氵的上点（短撇）
    g.dot(145, 470, w=94, h=126, slant=26)     # 氵的下点（短撇）
    g.diag(105, 150, 258, 305, weight=W_SEC)   # 氵的提


def _ki(g):
    """木字旁：x 60..360，横 + 竖 + 撇 + 捺。"""
    g.hbar(70, 350, 560, weight=W_MAIN)        # 横
    g.vbar(205, 800, 40, weight=W_MAIN)        # 竖
    g.diag(235, 545, 115, 120, weight=W_MAIN)  # 撇
    g.diag(215, 545, 350, 120, weight=W_MAIN)  # 捺


def _hito(g):
    """亻：x 60..300，撇 + 竖。"""
    g.diag(240, 770, 105, 505, weight=W_MAIN)  # 撇
    g.vbar(160, 520, 40, weight=W_MAIN)        # 竖


def _gyou(g):
    """彳：x 60..330，两撇 + 竖。"""
    g.diag(250, 790, 110, 650, weight=W_THIN)  # 上撇
    g.diag(230, 660, 95, 480, weight=W_THIN)   # 下撇
    g.vbar(155, 500, 40, weight=W_MAIN)        # 竖


def _koromo(g):
    """衤：x 60..390，点 + 横撇 + 竖 + 两点。"""
    g.dot(150, 770, w=84, h=100, slant=0)      # 衤的点（竖点档 0）
    g.hbar(95, 290, 650, weight=W_MAIN)        # 横撇的横
    g.diag(280, 660, 130, 400, weight=W_MAIN)  # 横撇的撇
    g.vbar(150, 640, 40, weight=W_MAIN)        # 竖
    g.dot(268, 400, w=76, h=88, slant=-14)     # 右点 1（捺向）
    g.dot(288, 236, w=76, h=88, slant=-14)     # 右点 2（捺向）


def _kin(g):
    """金字旁：x 60..470，人 + 王 + 丷 + 底横。"""
    g.diag(280, 780, 110, 650, weight=W_SEC)   # 撇（人）
    g.diag(270, 780, 460, 650, weight=W_SEC)   # 捺（人）
    g.hbar(150, 400, 570, weight=W_THIN)       # 横 1
    g.hbar(140, 410, 440, weight=W_THIN)       # 横 2
    g.vbar(275, 570, 150, weight=W_THIN)       # 竖
    g.dot(180, 320, w=76, h=88, slant=-14)     # 丷左（捺向）
    g.dot(372, 320, w=76, h=88, slant=14)      # 丷右（撇向）
    g.hbar(110, 440, 90, weight=W_MAIN)        # 底横


# ---------------------------------------------------------------------------
# 24 字
# ---------------------------------------------------------------------------
def g_su() -> Glyph:
    """訴。左「訁」+ 右「斥」。

    部件分区：訁 x 60..400（点/三横/口）；斥 x 430..940
    （横 + 长撇 + 竖 + 底撇 + 右上点）。
    """
    g = Glyph("uni8A34", advance=1000, unicode=0x8A34,
              note="訴：左訁（竖点+三横+口）+右斥（横+长撇+竖+底撇+右上点）")
    _gen(g)
    # ---- 斥 ----
    g.hbar(520, 930, 700, weight=W_MAIN)       # 斥的横
    g.diag(545, 730, 450, 70, weight=W_MAIN)   # 斥的长撇
    g.vbar(690, 700, 230, weight=W_MAIN)       # 斥的竖
    g.diag(810, 430, 560, 130, weight=W_MAIN)  # 斥的底撇
    g.dot(872, 772, w=84, h=96, slant=14)      # 斥的右上点（撇向）
    return g


def g_hi() -> Glyph:
    """被。左「衤」+ 右「皮」。

    部件分区：衤 x 60..390；皮 x 420..940（横钩 + 撇 + 竖 + 横撇 + 捺）。
    """
    g = Glyph("uni88AB", advance=1000, unicode=0x88AB,
              note="被：左衤（竖点+横撇+竖+两点）+右皮（横钩+撇+竖+横撇+捺）")
    _koromo(g)
    # ---- 皮 ----
    g.hbar(470, 930, 740, weight=W_MAIN)        # 皮的横
    g.vbar(880, 706, 630, weight=W_THIN)       # 皮的钩
    g.diag(520, 740, 450, 300, weight=W_MAIN)  # 皮的撇
    g.vbar(690, 740, 380, weight=W_MAIN)       # 皮的竖
    g.hbar(560, 880, 480, weight=W_SEC)         # 横撇的横
    g.diag(880, 480, 620, 180, weight=W_SEC)   # 横撇的撇
    g.diag(600, 460, 930, 120, weight=W_MAIN)   # 皮的捺
    return g


def g_kabu() -> Glyph:
    """株。左「木」+ 右「朱」。

    部件分区：木 x 60..360；朱 x 400..940（顶撇 + 短横 + 长横 + 竖 + 撇 + 捺）。
    """
    g = Glyph("uni682A", advance=1000, unicode=0x682A,
              note="株：左木（横+竖+撇+捺）+右朱（顶撇+短横+长横+竖+撇+捺）")
    _ki(g)
    # ---- 朱 ----
    g.diag(520, 790, 440, 690, weight=W_THIN)  # 朱的顶撇
    g.hbar(480, 890, 630, weight=W_THIN)       # 朱的短横
    g.hbar(430, 930, 510, weight=W_MAIN)       # 朱的长横
    g.vbar(680, 790, 40, weight=W_MAIN)        # 朱的竖
    g.diag(680, 505, 440, 110, weight=W_MAIN)  # 朱的撇
    g.diag(690, 505, 920, 120, weight=W_MAIN)  # 朱的捺
    return g


def g_fuku() -> Glyph:
    """復。左「彳」+ 右「复」。

    部件分区：彳 x 60..330；复 x 360..940（顶撇 + 横 + 日 + 夂）。
    2026-10-31 回修：复的横与日的顶白口 −14 → 复的横上抬 38、白口 24。
    """
    g = Glyph("uni5FA9", advance=1000, unicode=0x5FA9,
              note="復：左彳（两撇+竖）+右复（顶撇+横+日+夂）")
    _gyou(g)
    # ---- 复 ----
    g.diag(470, 790, 375, 700, weight=W_THIN)  # 复的顶撇
    g.hbar(390, 930, 728, weight=W_THIN)       # 复的横
    _hi(g, 560, 900, 620, 516, 412, W_LIGHT)    # 复的日（腔 24→28/28，参照 27）
    # 夂
    g.diag(520, 390, 420, 250, weight=W_THIN)  # 夂的撇
    g.hbar(500, 830, 300, weight=W_SEC)         # 夂的横撇（横）
    g.diag(830, 300, 610, 90, weight=W_SEC)    # 夂的横撇（撇）
    g.diag(560, 285, 930, 70, weight=W_MAIN)   # 夂的捺
    return g


def g_wataru() -> Glyph:
    """渡。左「氵」+ 右「度」。

    部件分区：氵 x 60..290；度 x 330..940（广的点/横/撇 + 廿 + 又）。
    """
    g = Glyph("uni6E21", advance=1000, unicode=0x6E21,
              note="渡：左氵（两短撇+提）+右度（广的点横撇+廿+又）")
    _sanzui(g)
    # ---- 度 ----
    g.dot(500, 768, w=84, h=90, slant=0)       # 广的点（竖点档 0）
    g.hbar(380, 940, 690, weight=W_MAIN)        # 广的横
    g.diag(410, 690, 350, 60, weight=W_MAIN)    # 广的撇
    # 廿
    g.hbar(490, 880, 570, weight=W_THIN)        # 廿的上横
    g.hbar(490, 880, 410, weight=W_THIN)        # 廿的下横
    g.vbar(545, 570, 410, weight=W_THIN)        # 廿的左竖
    g.vbar(825, 570, 410, weight=W_THIN)        # 廿的右竖
    # 又
    g.hbar(520, 880, 300, weight=W_SEC)         # 又的横撇（横）
    g.diag(880, 284, 630, 54, weight=W_SEC)     # 又的横撇（撇）下移 16
    g.diag(560, 274, 930, 44, weight=W_MAIN)    # 又的捺下移 16（两端同量）
    return g


def g_utsuri() -> Glyph:
    """移。左「禾」+ 右「多」。

    部件分区：禾 x 60..370；多 x 400..940（夕 + 夕）。
    """
    g = Glyph("uni79FB", advance=1000, unicode=0x79FB,
              note="移：左禾（顶撇+横+竖+撇+捺）+右多（夕+夕）")
    # ---- 禾 ----
    g.diag(300, 800, 180, 720, weight=W_THIN)  # 禾的顶撇
    g.hbar(70, 370, 660, weight=W_MAIN)         # 禾的横
    g.vbar(220, 790, 40, weight=W_MAIN)         # 禾的竖
    g.diag(230, 640, 80, 130, weight=W_MAIN)    # 禾的撇
    g.diag(215, 640, 350, 130, weight=W_MAIN)   # 禾的捺
    # ---- 多 ----
    g.diag(560, 790, 465, 660, weight=W_THIN)   # 夕 1 的撇
    g.hbar(520, 810, 700, weight=W_THIN)        # 夕 1 的横撇（横）
    g.diag(810, 700, 610, 530, weight=W_THIN)   # 夕 1 的横撇（撇）
    g.dot(630, 610, w=76, h=88, slant=-14)      # 夕 1 的点（捺向）
    g.diag(560, 470, 465, 340, weight=W_THIN)   # 夕 2 的撇
    g.hbar(520, 810, 380, weight=W_THIN)        # 夕 2 的横撇（横）
    g.diag(810, 380, 610, 210, weight=W_THIN)   # 夕 2 的横撇（撇）
    g.dot(630, 290, w=76, h=88, slant=-14)      # 夕 2 的点（捺向）
    return g


def g_sa() -> Glyph:
    """差。上「丷 + 二横 + 长撇」/ 下「工」。

    部件分区：上 y 380..820；下工 x 430..920, y 0..350。
    """
    g = Glyph("uni5DEE", advance=1000, unicode=0x5DEE,
              note="差：上丷+二横+长撇，下右工（横+竖+横）")
    g.dot(250, 768, w=84, h=100, slant=-14)      # 丷左（捺向）
    g.dot(430, 768, w=84, h=100, slant=14)       # 丷右（撇向）
    g.hbar(130, 900, 660, weight=W_MAIN)         # 横 1
    g.hbar(100, 930, 520, weight=W_MAIN)         # 横 2
    g.diag(880, 660, 120, 60, weight=W_MAIN)     # 长撇
    # ---- 工 ----
    g.hbar(430, 920, 300, weight=W_MAIN)         # 工的上横
    g.vbar(660, 300, 40, weight=W_MAIN)          # 工的竖
    g.hbar(430, 920, 40, weight=W_MAIN)          # 工的下横
    return g


def g_shu() -> Glyph:
    """衆。上「丿 + 皿」/ 下「乑」。

    部件分区：上 y 380..820（皿带 4 竖 3 白格）；下 y 0..360（中竖 + 长撇 + 捺 + 短撇）。
    """
    g = Glyph("uni8846", advance=1000, unicode=0x8846,
              note="衆：上顶撇+皿（四竖三白格），下乑（中竖+长撇+捺+短撇）")
    g.diag(520, 800, 400, 720, weight=W_SEC)     # 顶撇
    g.hbar(140, 900, 690, weight=W_SEC)          # 皿的上横
    g.hbar(140, 900, 400, weight=W_SEC)          # 皿的下横
    g.vbar(190, 690, 400, weight=W_THIN)         # 皿的左竖
    g.vbar(410, 690, 400, weight=W_THIN)         # 皿的内竖 1
    g.vbar(630, 690, 400, weight=W_THIN)         # 皿的内竖 2
    g.vbar(850, 690, 400, weight=W_THIN)         # 皿的右竖
    # ---- 乑 ----
    g.vbar(490, 380, 40, weight=W_MAIN)          # 中竖
    g.diag(490, 330, 150, 60, weight=W_MAIN)     # 长撇
    g.diag(520, 330, 900, 60, weight=W_MAIN)     # 捺
    g.diag(330, 330, 190, 190, weight=W_THIN)    # 短撇
    return g


def g_ko() -> Glyph:
    """個。左「亻」+ 右「固」。

    部件分区：亻 x 60..300；固 x 330..940（囗 + 古）。
    """
    g = Glyph("uni500B", advance=1000, unicode=0x500B,
              note="個：左亻（撇+竖）+右固（囗+古）")
    _hito(g)
    # ---- 囗 ----
    g.hbar(340, 940, 740, weight=W_MAIN)         # 囗的上横
    g.hbar(340, 940, 40, weight=W_MAIN)          # 囗的下横
    g.vbar(388, 740, 40, weight=W_MAIN)          # 囗的左竖
    g.vbar(892, 740, 40, weight=W_MAIN)          # 囗的右竖
    # ---- 古 ----
    g.hbar(430, 890, 600, weight=W_SEC)          # 古的横
    g.vbar(660, 600, 440, weight=W_SEC)          # 古的竖
    _kuchi(g, 500, 830, 440, 240, W_THIN)        # 古的口
    return g


def g_hyo() -> Glyph:
    """評。左「訁」+ 右「平」。

    部件分区：訁 x 60..400；平 x 430..940（横 + 两点 + 长横 + 竖）。
    """
    g = Glyph("uni8A55", advance=1000, unicode=0x8A55,
              note="評：左訁（竖点+三横+口）+右平（横+两点+长横+竖）")
    _gen(g)
    # ---- 平 ----
    g.hbar(450, 930, 760, weight=W_MAIN)         # 平的上横
    g.dot(560, 620, w=84, h=96, slant=-14)       # 丶（左点，捺向）
    g.dot(820, 620, w=84, h=96, slant=14)        # 丿（右点，撇向）
    g.hbar(430, 940, 460, weight=W_MAIN)         # 平的长横
    g.vbar(690, 760, 40, weight=W_MAIN)          # 平的竖
    return g


def g_nou() -> Glyph:
    """脳。左「月」+ 右「亠 + 凶」。

    部件分区：月 x 60..370；右 x 400..940（亠 的点/横 + 凶 的竖折/竖/乂）。
    """
    g = Glyph("uni8133", advance=1000, unicode=0x8133,
              note="脳：左月（撇+横折+两横）+右亠（竖点+横）与凶（竖折+竖+乂）")
    # ---- 月 ----
    g.diag(140, 780, 100, 60, weight=W_MAIN)     # 月的撇
    g.hbar(110, 350, 780, weight=W_MAIN)         # 月的上横
    g.vbar(300, 780, 60, weight=W_MAIN)          # 月的右竖
    g.hbar(110, 350, 570, weight=W_THIN)          # 月的横 1
    g.hbar(110, 350, 340, weight=W_THIN)          # 月的横 2
    # ---- 亠 ----
    g.dot(600, 772, w=84, h=90, slant=0)         # 亠的点（竖点档 0）
    g.hbar(430, 940, 700, weight=W_MAIN)         # 亠的横
    # ---- 凶 ----
    g.hbar(430, 940, 80, weight=W_SEC)           # 凶的竖折（横）
    g.vbar(480, 600, 80, weight=W_SEC)           # 凶的竖折（竖）
    g.vbar(890, 600, 80, weight=W_SEC)           # 凶的右竖
    g.diag(590, 620, 830, 230, weight=W_SEC)     # 凶的撇
    g.diag(790, 620, 550, 230, weight=W_SEC)     # 凶的捺
    return g


def g_kyoku() -> Glyph:
    """極。左「木」+ 右「亟」。

    部件分区：木 x 60..360；亟 x 430..940（乛 + 口 + 又 + 底横）。
    """
    g = Glyph("uni6975", advance=1000, unicode=0x6975,
              note="極：左木（横+竖+撇+捺）+右亟（乛+口+又+底横）")
    _ki(g)
    # ---- 亟 ----
    g.hbar(440, 930, 740, weight=W_MAIN)          # 亟的横
    g.vbar(480, 740, 560, weight=W_MAIN)          # 亟的横折（竖）
    _kuchi(g, 520, 700, 600, 450, W_THIN)         # 亟的口
    g.hbar(730, 920, 620, weight=W_SEC)           # 又的横撇（横）
    g.diag(920, 620, 760, 430, weight=W_SEC)      # 又的横撇（撇）
    g.diag(770, 600, 920, 430, weight=W_SEC)      # 又的捺
    g.hbar(430, 940, 330, weight=W_MAIN)          # 亟的底横
    return g


def g_fuku2() -> Glyph:
    """福。左「礻」+ 右「畐」。

    部件分区：礻 x 60..380；畐 x 420..940（一 + 口 + 田）。
    """
    g = Glyph("uni798F", advance=1000, unicode=0x798F,
              note="福：左礻（竖点+横撇+竖+点）+右畐（一+口+田）")
    # ---- 礻 ----
    g.dot(200, 770, w=84, h=100, slant=0)         # 礻的点（竖点档 0）
    g.hbar(90, 330, 640, weight=W_MAIN)           # 横撇的横
    g.diag(320, 660, 130, 380, weight=W_MAIN)     # 横撇的撇
    g.vbar(190, 640, 40, weight=W_MAIN)           # 竖
    g.dot(300, 330, w=84, h=96, slant=-14)        # 右点（捺向）
    # ---- 畐 ----
    g.hbar(450, 920, 780, weight=W_MAIN)          # 畐的一
    _kuchi(g, 520, 850, 660, 520, W_THIN)         # 畐的口
    _ta(g, 450, 920, 420, 280, 140, W_THIN, 685)  # 畐的田
    return g


def g_ryo() -> Glyph:
    """量。上「旦」/ 下「里」。

    九道横画密排：按 GLY-001 局部减重到 76，横间白缝 16 单位（保内白可见）。
    横画中心线自上而下：774 / 682 / 590 / 498 / 406 / 314 / 222 / 130 / 38。
    """
    g = Glyph("uni91CF", advance=1000, unicode=0x91CF,
              note="量：上旦（曰三横+一），下里（田+土），九横密排局部减重")
    # ---- 旦 ----
    g.hbar(140, 880, 778, weight=W_HAIR)          # 曰的上横
    g.hbar(140, 880, 680, weight=W_HAIR)          # 曰的中横（腔 26→30）
    g.hbar(140, 880, 582, weight=W_HAIR)          # 曰的下横（腔 26→30）
    g.vbar(180, 778, 548, weight=W_HAIR)          # 曰的左竖
    g.vbar(840, 778, 548, weight=W_HAIR)          # 曰的右竖
    g.hbar(90, 930, 490, weight=W_HAIR)           # 旦的一
    # ---- 里 ----
    g.hbar(150, 870, 406, weight=W_LIGHT)         # 田的上横
    g.hbar(150, 870, 308, weight=W_HAIR)          # 田的中横（腔 26→30）
    g.hbar(150, 870, 210, weight=W_HAIR)          # 田的下横（腔 26→30）
    g.vbar(190, 406, 176, weight=W_HAIR)          # 田的左竖
    g.vbar(830, 406, 176, weight=W_HAIR)          # 田的右竖
    g.vbar(510, 406, 38, weight=W_HAIR)           # 里的中竖
    g.hbar(110, 910, 120, weight=W_HAIR)          # 土的一
    g.hbar(90, 930, 38, weight=W_HAIR)            # 土的底横
    return g


def g_bou() -> Glyph:
    """望。上「亡 + 月」/ 下「王」。

    部件分区：亡 x 60..430；月 x 470..940（y 380..820）；王 y 0..322。
    """
    g = Glyph("uni671B", advance=1000, unicode=0x671B,
              note="望：上左亡（竖点+横+竖折）+上右月（撇+横折+两横），下王（三横+竖）")
    # ---- 亡 ----
    g.dot(150, 768, w=84, h=90, slant=0)          # 亡的点（竖点档 0）
    g.hbar(70, 400, 700, weight=W_MAIN)           # 亡的横
    g.vbar(240, 690, 520, weight=W_MAIN)          # 亡的竖折（竖）
    g.hbar(70, 240, 520, weight=W_MAIN)           # 亡的竖折（横）
    # ---- 月 ----
    g.diag(520, 780, 470, 120, weight=W_MAIN)     # 月的撇
    g.hbar(480, 930, 780, weight=W_MAIN)          # 月的上横
    g.vbar(880, 780, 120, weight=W_MAIN)          # 月的右竖
    g.hbar(480, 930, 600, weight=W_THIN)          # 月的横 1
    g.hbar(480, 930, 430, weight=W_THIN)          # 月的横 2
    # ---- 王 ----
    g.hbar(90, 930, 276, weight=W_SEC)            # 王的上横
    g.hbar(130, 890, 158, weight=W_SEC)           # 王的中横
    g.hbar(90, 930, 46, weight=W_SEC)             # 王的下横
    g.vbar(510, 276, 46, weight=W_MAIN)           # 王的竖
    return g


def g_kaku() -> Glyph:
    """核。左「木」+ 右「亥」。

    部件分区：木 x 60..360；亥 x 430..940（点 + 横 + 撇折 + 两撇 + 捺）。
    """
    g = Glyph("uni6838", advance=1000, unicode=0x6838,
              note="核：左木（横+竖+撇+捺）+右亥（竖点+横+撇折+撇+捺）")
    _ki(g)
    # ---- 亥 ----
    g.dot(670, 772, w=84, h=90, slant=0)          # 亥的点（竖点档 0）
    g.hbar(470, 930, 700, weight=W_MAIN)          # 亥的横
    g.diag(700, 630, 560, 490, weight=W_SEC)      # 亥的撇折（撇）
    g.hbar(560, 880, 490, weight=W_SEC)           # 亥的撇折（横）
    g.diag(640, 470, 450, 90, weight=W_MAIN)      # 亥的撇
    g.diag(790, 500, 660, 220, weight=W_THIN)     # 亥的短撇
    g.diag(700, 440, 930, 80, weight=W_MAIN)      # 亥的捺
    return g


def g_fuka() -> Glyph:
    """深。左「氵」+ 右「罙」。

    部件分区：氵 x 60..290；罙 x 330..940（冖 + 儿 + 木）。
    2026-10-31 回修：儿的竖弯与木的横白口 −30 → 儿的竖与竖弯上提 54、白口 24。
    """
    g = Glyph("uni6DF1", advance=1000, unicode=0x6DF1,
              note="深：左氵（两短撇+提）+右罙（冖+儿+木）")
    _sanzui(g)
    # ---- 罙 ----
    g.hbar(360, 940, 760, weight=W_SEC)            # 冖的横
    g.vbar(400, 714, 640, weight=W_THIN)           # 冖的左点
    g.vbar(890, 714, 640, weight=W_THIN)           # 冖的右点
    g.diag(570, 620, 430, 430, weight=W_THIN)      # 儿的撇
    g.vbar(730, 620, 494, weight=W_THIN)           # 儿的竖
    g.hbar(730, 900, 494, weight=W_THIN)           # 儿的竖弯
    # 罙的木
    g.hbar(380, 940, 380, weight=W_MAIN)           # 木的横
    g.vbar(660, 380, 40, weight=W_MAIN)            # 木的竖
    g.diag(660, 380, 420, 60, weight=W_MAIN)       # 木的撇
    g.diag(660, 380, 920, 60, weight=W_MAIN)       # 木的捺
    return g


def g_kaku2() -> Glyph:
    """答。上「⺮」/ 下「合」。

    部件分区：⺮ y 470..820（左组 x 80..410，右组 x 575..900）；
    合 y 0..460（人 + 一 + 口）。
    """
    g = Glyph("uni7B54", advance=1000, unicode=0x7B54,
              note="答：上竹字头（两组的撇横点），下合（人+一+口）")
    # ---- ⺮ 左组 ----
    g.diag(215, 795, 120, 690, weight=W_THIN)      # 左组的撇
    g.hbar(200, 405, 640, weight=W_THIN)           # 左组的横
    g.dot(370, 520, w=84, h=100, slant=-14)        # 左组的点（捺向）
    # ---- ⺮ 右组 ----
    g.diag(815, 795, 720, 690, weight=W_THIN)      # 右组的撇
    g.hbar(575, 780, 640, weight=W_THIN)           # 右组的横
    g.dot(660, 520, w=84, h=100, slant=-14)        # 右组的点（捺向）
    # ---- 合 ----
    g.diag(500, 460, 180, 330, weight=W_SEC)       # 合的人（撇）
    g.diag(500, 460, 820, 330, weight=W_SEC)       # 合的人（捺）
    g.hbar(280, 720, 290, weight=W_SEC)            # 合的一
    _kuchi(g, 330, 670, 200, 42, W_THIN)           # 合的口
    return g


def g_hyou() -> Glyph:
    """票。上「覀」/ 下「示」。

    部件分区：覀 y 518..808（上横 + 四竖 + 下横，三个白格）；示 y 0..488。
    """
    g = Glyph("uni7968", advance=1000, unicode=0x7968,
              note="票：上覀（一+四竖+一，三白格），下示（二+小）")
    # ---- 覀 ----
    g.hbar(100, 930, 760, weight=W_MAIN)           # 覀的上横
    g.hbar(100, 930, 560, weight=W_THIN)           # 覀的下横
    g.vbar(170, 760, 560, weight=W_THIN)           # 覀的竖 1
    g.vbar(390, 760, 560, weight=W_THIN)           # 覀的竖 2
    g.vbar(610, 760, 560, weight=W_THIN)           # 覀的竖 3
    g.vbar(830, 760, 560, weight=W_THIN)           # 覀的竖 4
    # ---- 示 ----
    g.hbar(100, 930, 440, weight=W_MAIN)           # 示的上横
    g.hbar(150, 880, 320, weight=W_MAIN)           # 示的下横
    g.vbar(510, 320, 40, weight=W_MAIN)            # 小的竖
    g.dot(280, 180, w=76, h=88, slant=14)          # 小的左点（撇向）
    g.dot(740, 180, w=76, h=88, slant=-14)         # 小的右点（捺向）
    return g


def g_zai() -> Glyph:
    """財。左「貝」+ 右「才」。

    部件分区：貝 x 60..450（目形三白格 + 撇 + 点）；才 x 490..940。
    """
    g = Glyph("uni8CA1", advance=1000, unicode=0x8CA1,
              note="財：左貝（目形三白格+撇+点）+右才（横+竖钩+撇）")
    # ---- 貝 ----
    g.hbar(80, 430, 740, weight=W_MAIN)            # 貝的上横
    g.hbar(80, 430, 580, weight=W_THIN)            # 貝的横 1
    g.hbar(80, 430, 420, weight=W_THIN)            # 貝的横 2
    g.hbar(80, 430, 260, weight=W_THIN)            # 貝的下横
    g.vbar(122, 740, 260, weight=W_THIN)           # 貝的左竖
    g.vbar(388, 740, 260, weight=W_THIN)           # 貝的右竖
    g.diag(210, 230, 100, 60, weight=W_SEC)        # 貝的撇
    g.diag(320, 230, 430, 60, weight=W_SEC)        # 貝的点
    # ---- 才 ----
    g.hbar(490, 940, 560, weight=W_MAIN)           # 才的横
    g.vbar(700, 700, 60, weight=W_MAIN)            # 才的竖
    g.hbar(620, 700, 60, weight=W_SEC)             # 才的竖钩
    g.diag(690, 560, 490, 200, weight=W_MAIN)      # 才的撇
    return g


def g_wataru2() -> Glyph:
    """渉。左「氵」+ 右「歩」。

    部件分区：氵 x 60..290；歩 x 330..940（止 + 少）。
    2026-10-31 回修：止的横与止的底横白口 −10 → 止的横上抬 34、白口 24。
    """
    g = Glyph("uni6E09", advance=1000, unicode=0x6E09,
              note="渉：左氵（两短撇+提）+右歩（止+少）")
    _sanzui(g)
    # ---- 止 ----
    g.vbar(400, 700, 560, weight=W_THIN)           # 止的左竖
    g.hbar(440, 580, 674, weight=W_THIN)           # 止的横
    g.vbar(510, 780, 560, weight=W_MAIN)           # 止的中竖
    g.hbar(340, 940, 560, weight=W_MAIN)           # 止的底横
    # ---- 少 ----
    g.vbar(670, 470, 270, weight=W_THIN)           # 少的竖
    g.diag(660, 450, 480, 270, weight=W_THIN)      # 少的左撇
    g.dot(830, 380, w=84, h=96, slant=-14)         # 少的右点（捺向）
    g.diag(690, 300, 480, 60, weight=W_THIN)       # 少的长撇
    return g


def g_tatsu() -> Glyph:
    """達。左「辶」+ 右「羍」。

    部件分区：羍 x 430..940（土 + 羊）；辶 x 60..430 的点与折折撇，
    底部长捺横扫 x 140..940。
    2026-10-31 回修：土的上横与下横白口 −16 → 上横上抬 40、白口 24，土的竖随之上抬。
    """
    g = Glyph("uni9054", advance=1000, unicode=0x9054,
              note="達：左辶（点+折折撇+底捺），右羍（土+羊）")
    # ---- 羍 ----
    g.hbar(500, 900, 820, weight=W_MAIN)           # 土的上横
    g.vbar(700, 820, 680, weight=W_MAIN)           # 土的竖
    g.hbar(450, 940, 700, weight=W_MAIN)           # 土的下横
    g.dot(540, 580, w=84, h=100, slant=-14)        # 丷左（捺向）
    g.dot(840, 580, w=84, h=100, slant=14)         # 丷右（撇向）
    g.hbar(450, 940, 450, weight=W_MAIN)           # 羊的上横
    g.hbar(480, 910, 320, weight=W_MAIN)           # 羊的下横
    g.vbar(690, 450, 40, weight=W_MAIN)            # 羊的竖
    # ---- 辶 ----
    g.dot(150, 768, w=90, h=100, slant=-14)        # 辶的点（捺向）
    g.hbar(90, 260, 620, weight=W_SEC)             # 辶的折折撇（横）
    g.vbar(210, 620, 470, weight=W_SEC)            # 辶的折折撇（竖）
    g.hbar(210, 300, 470, weight=W_SEC)            # 辶的折折撇（横 2）
    g.diag(280, 470, 150, 250, weight=W_SEC)       # 辶的折折撇（撇）
    g.diag(150, 280, 930, 60, weight=W_MAIN)       # 辶的底捺
    return g


def g_ki2() -> Glyph:
    """帰。左上「丿 + 長竖」/ 右上「彐」/ 下「巾」。

    部件分区：丿 + 竖 x 150..280；彐 x 280..908, y 408..808；巾 y 0..382。
    """
    g = Glyph("uni5E30", advance=1000, unicode=0x5E30,
              note="帰：左上顶撇+长竖，右上彐（三横一竖），下巾（冂+中竖）")
    g.diag(260, 800, 160, 720, weight=W_THIN)      # 顶撇
    g.vbar(200, 780, 40, weight=W_MAIN)            # 长竖
    # ---- 彐 ----
    g.hbar(280, 900, 760, weight=W_MAIN)           # 彐的上横
    g.hbar(280, 900, 608, weight=W_THIN)           # 彐的中横
    g.hbar(280, 900, 450, weight=W_THIN)           # 彐的下横
    g.vbar(858, 760, 450, weight=W_MAIN)           # 彐的竖
    # ---- 巾 ----
    g.hbar(380, 900, 340, weight=W_THIN)           # 巾的上横
    g.vbar(422, 340, 50, weight=W_THIN)            # 巾的左竖
    g.vbar(858, 340, 50, weight=W_THIN)            # 巾的右竖
    g.vbar(620, 360, 40, weight=W_MAIN)            # 巾的中竖
    return g


def g_hari() -> Glyph:
    """針。左「金」+ 右「十」。

    部件分区：金 x 60..470（人 + 三横一竖 + 丷 + 底横）；十 x 520..940。
    """
    g = Glyph("uni91DD", advance=1000, unicode=0x91DD,
              note="針：左金（人+横竖+两点+底横）+右十（横+竖）")
    _kin(g)
    # ---- 十 ----
    g.hbar(520, 940, 520, weight=W_MAIN)           # 十的横
    g.vbar(730, 800, 40, weight=W_MAIN)            # 十的竖
    return g


def build() -> list[Glyph]:
    return [
        g_su(), g_hi(), g_kabu(), g_fuku(), g_wataru(), g_utsuri(),
        g_sa(), g_shu(), g_ko(), g_hyo(), g_nou(), g_kyoku(),
        g_fuku2(), g_ryo(), g_bou(), g_kaku(), g_fuka(), g_kaku2(),
        g_hyou(), g_zai(), g_wataru2(), g_tatsu(), g_ki2(), g_hari(),
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s3-006.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
