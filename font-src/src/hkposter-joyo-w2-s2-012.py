"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-012。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
* 字面框 x 60..940、y 0..820，advance=1000（与 zh-HK 繁体同一档，便于中英日混排）。
* 笔画权重档：主 96 / 次 92 / 细 84 / 点 84–96，与繁体汉字同档。
* 横向节奏：横画中心线取统一导轨 R0..R6 = 772 / 648 / 524 / 400 / 276 / 152 / 48，
  相邻导轨间距 124，96 权重下内白 28 单位（≥ GLY-006 的 24）。
  密排字（草 / 是 / 看 / 奏 / 聿）另用 166 的宽间距，保证内白 ≥ 26。
* 部件复用（GLY-004）：亻 / 扌 / 氵 / 木 / 禾 / 艹 / 宀 / 及 / 聿 / 斤 / 兆 / 夋 /
  帚 / 舌 / 至 / 刂 / 日 / 口 各写一个构件函数，批内坐标完全一致，只做位置光学校正。
* 斜切档位只用工程约定的 -14 / 0 / 14 / 26，不自造档位。
* 笔画走向照标准骨架，不改角度；只改重量、端点处理与记号字面。
* 墨量率：本批 7–9 画档中位数约 0.30，实测 0.197–0.405，档内离散 < 35%（无 WARN）。
  6 画档（肉 / 至 / 仮 / 芝 / 吸 / 扱）靠满框与 96 主笔提重；
  9 画档（草 / 挑 / 律 / 促 / 俊 / 秒 / 侵 / 括 / 透 / 津 / 是 / 看 / 奏 / 泉）
  在拥挤处减到 84–92。
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

TOP = 820.0
BOT = 0.0

# 横向导轨（横画中心线 y）
R0, R1, R2, R3, R4, R5, R6 = 772.0, 648.0, 524.0, 400.0, 276.0, 152.0, 48.0


# --------------------------------------------------------------- 对齐辅助
def hbar_top(g, x1, x2, weight=W_MAIN):
    """横画：墨迹上缘对齐字面框上沿 820。"""
    g.hbar(x1, x2, TOP - weight / 2.0, weight)
    return g


def hbar_base(g, x1, x2, weight=W_MAIN):
    """横画：墨迹下缘对齐基线 0。"""
    g.hbar(x1, x2, BOT + weight / 2.0, weight)
    return g


# --------------------------------------------------------------- 部件库
def rad_hen(g):
    """亻（左偏旁，x 60..300）。促 / 俊 / 侵 / 仮 共用同一套坐标。"""
    g.diag(300, 785, 160, 645, W_SEC)   # 撇
    g.vbar(190, 640, 0, W_SEC)           # 竖
    return g


def rad_tehen(g):
    """扌（左偏旁，x 60..380）。挑 / 括 / 扱 共用。"""
    g.hbar(60, 380, 640, W_MAIN)         # 横
    g.vbar(215, 800, 0, W_MAIN)          # 竖
    g.diag(85, 250, 360, 330, W_SEC)     # 提
    return g


def rad_sanzui(g):
    """氵（左偏旁，x 60..300）。律 / 津 共用。"""
    g.dot(140, 760, 90, 110, 26)        # 上点＝短撇（slant 26）
    g.dot(175, 600, 88, 104, -14)       # 中点＝丶（slant -14）
    g.diag(90, 370, 295, 465, W_SEC)    # 提
    return g


def rad_kihen(g):
    """木（左偏旁，x 60..430）。析 共用。"""
    g.hbar(60, 430, 660, W_MAIN)        # 横
    g.vbar(245, 810, 0, W_MAIN)         # 竖
    g.diag(248, 500, 110, 190, W_MAIN)  # 撇
    g.diag(180, 347, 408, 190, W_MAIN)  # 捺（起于撇上）
    return g


def rad_nogihen(g):
    """禾（左偏旁，x 60..440）。秒 共用。"""
    g.diag(390, 775, 150, 690, W_SEC)   # 顶撇
    g.hbar(80, 420, 600, W_MAIN)        # 横
    g.vbar(225, 740, 0, W_MAIN)         # 竖
    g.diag(240, 480, 110, 185, W_SEC)   # 撇
    g.diag(170, 321, 420, 185, W_SEC)   # 捺（起于撇上）
    return g


def rad_kusa(g):
    """艹（上偏旁，整宽）。草 / 芝 共用。"""
    g.hbar(60, 940, 710, W_MAIN)        # 横
    g.vbar(280, 820, 630, W_SEC)        # 左短竖
    g.vbar(720, 820, 630, W_SEC)        # 右短竖
    return g


def rad_ukanmuri(g):
    """宀（上偏旁，整宽）。宗 / 宙 共用。"""
    g.dot(500, 782, 92, 70, 0)          # 竖点（slant 0）
    g.hbar(190, 820, 640, W_MAIN)       # 横
    g.vbar(205, 640, 530, W_THIN)       # 左短竖
    g.vbar(800, 640, 570, W_THIN)       # 右短钩
    return g


def comp_nichi(g, xl, xr, y_top, y_bot, weight=W_SEC):
    """日：左右竖 + 顶/中/底横。xl/xr 为竖的中心线，y_top/y_bot 为墨迹上下缘。"""
    half = weight / 2.0
    g.vbar(xl, y_top, y_bot, weight)
    g.vbar(xr, y_top, y_bot, weight)
    g.hbar(xl - half, xr + half, y_top - half, weight)
    g.hbar(xl - half, xr + half, (y_top + y_bot) / 2.0, weight)
    g.hbar(xl - half, xr + half, y_bot + half, weight)
    return g


def comp_kuchi(g, xl, xr, y_top, y_bot, weight=W_SEC):
    """口：左右竖 + 顶/底横（无中横）。"""
    half = weight / 2.0
    g.vbar(xl, y_top, y_bot, weight)
    g.vbar(xr, y_top, y_bot, weight)
    g.hbar(xl - half, xr + half, y_top - half, weight)
    g.hbar(xl - half, xr + half, y_bot + half, weight)
    return g


def comp_oku(g):
    """及（右构件，x 420..940）。吸 / 扱 共用。

    骨架照 M PLUS 1p Black：顶部长平撇 + 中部长竖撇 + 右下「横折」钩 + 捺。
    """
    g.hbar(430, 820, 750, W_SEC)        # 顶部长平撇
    g.diag(560, 715, 440, 40, W_MAIN)   # 长竖撇
    g.hbar(500, 885, 504, W_THIN)       # ㇋ 横
    g.diag(880, 504, 680, 336, W_THIN)  # ㇋ 折（折向左下）
    g.diag(655, 460, 890, 80, W_MAIN)   # 捺
    return g


def comp_bitsu(g):
    """聿（右构件，x 350..940）。律 / 津 共用。"""
    g.hbar(400, 940, 772, W_SEC)        # ヨ 顶横
    g.vbar(893, 818, 440, W_SEC)        # ヨ 右竖
    g.hbar(400, 893, 606, W_SEC)        # ヨ 中横
    g.hbar(400, 893, 440, W_SEC)        # ヨ 底横
    g.vbar(600, 820, 0, W_MAIN)         # 贯穿竖
    g.hbar(400, 940, 274, W_SEC)        # 二 上横
    g.hbar(400, 940, 108, W_SEC)        # 二 下横
    return g


def comp_kin(g):
    """斤（右构件，x 470..940）。析 共用。"""
    g.diag(900, 770, 545, 742, W_SEC)   # 撇 1：顶部长平撇（近乎水平）
    g.diag(570, 700, 518, 20, W_SEC)    # 撇 2：长竖撇
    g.hbar(515, 940, 360, W_SEC)        # 横
    g.vbar(790, 380, 20, W_SEC)         # 竖（自横下垂）
    return g


def comp_chou(g):
    """兆（右构件，x 420..940）。挑 共用。

    骨架：主左撇 620→545，主右竖钩 760→130（钩向右），
    四枚小记号：丶左上、丶左下、丿右上、丿右下。
    """
    g.diag(620, 790, 545, 40, W_MAIN)   # 丿 主左笔
    g.dot(495, 685, 78, 94, -14)        # 丶 左上
    g.dot(478, 495, 78, 94, -14)        # 丶 左下
    g.vbar(760, 790, 130, W_MAIN)       # 乚 主右笔
    g.diag(760, 140, 880, 75, W_THIN)   # 乚 的钩
    g.diag(895, 730, 862, 640, W_THIN)  # ノ 右上
    g.diag(895, 520, 860, 415, W_THIN)  # ノ 右下
    return g


def comp_shun(g):
    """夋（右构件，x 340..940）。俊 共用。

    骨架：厶（撇折 + 点）y 660..780；八 y 470..610；夂（撇 + 横撇 + 捺）y 40..430。
    """
    g.diag(640, 770, 500, 680, W_SEC)   # 厶 撇
    g.hbar(500, 700, 680, W_SEC)        # 厶 折
    g.dot(730, 710, 92, 110, -14)       # 厶 点
    g.diag(530, 590, 390, 470, W_SEC)   # 八 撇
    g.dot(820, 540, 92, 110, -14)       # 八 点
    g.diag(690, 430, 560, 250, W_SEC)   # 夂 撇
    g.hbar(510, 840, 360, W_SEC)        # 夂 横
    g.diag(840, 360, 600, 170, W_SEC)   # 夂 横撇
    g.diag(680, 240, 890, 40, W_MAIN)   # 夂 捺
    return g


def comp_hou(g):
    """帚（右构件，x 340..940）。侵 共用。"""
    g.hbar(400, 900, 772, W_SEC)        # ヨ 顶横
    g.vbar(855, 818, 480, W_SEC)        # ヨ 右竖
    g.hbar(400, 855, 648, W_SEC)        # ヨ 中横
    g.hbar(400, 855, 524, W_SEC)        # ヨ 底横
    g.hbar(350, 940, 400, W_MAIN)       # 冖 横
    g.vbar(365, 400, 310, W_THIN)       # 冖 左短竖
    g.hbar(420, 840, 250, W_THIN)       # 又 横
    g.diag(840, 250, 580, 55, W_THIN)   # 又 横撇
    g.diag(640, 190, 900, 50, W_MAIN)   # 又 捺
    return g


def comp_zetsu(g):
    """舌（右构件，x 420..940）。括 共用。"""
    g.diag(760, 775, 560, 710, W_THIN)  # 千 顶撇
    g.hbar(440, 920, 620, W_MAIN)       # 千 横
    g.vbar(680, 790, 350, W_MAIN)       # 千 竖
    comp_kuchi(g, 500, 840, 380, 0, W_SEC)
    return g


def comp_iti(g):
    """至（左构件，x 60..660）。到 共用。"""
    g.hbar(110, 610, 772, W_MAIN)       # 一
    g.diag(450, 700, 250, 570, W_SEC)   # 厶 撇
    g.hbar(250, 510, 570, W_SEC)        # 厶 折
    g.dot(530, 630, 80, 96, -14)        # 厶 点
    g.hbar(170, 560, 420, W_MAIN)       # 土 上横
    g.vbar(360, 480, 200, W_MAIN)       # 土 竖
    g.hbar(100, 620, 150, W_MAIN)       # 土 下横
    return g


def comp_rittou(g):
    """刂（右构件，x 700..940）。到 / 刺 共用。"""
    g.vbar(760, 700, 530, W_SEC)        # 短竖
    g.vbar(890, 820, 60, W_MAIN)        # 长竖
    g.diag(890, 90, 820, 45, W_THIN)    # 长竖的钩（向左）
    return g


# --------------------------------------------------------------- 字形
def uni8349() -> Glyph:
    """草 U+8349（9 画）—— 艹 + 早。

    部件分区：艹 y 630..820（横 710、双短竖 820→630）；日 y 272..616（双竖 280/720，
    三横 570/444/318）；十 y 0..208（横 160、竖 500→0）。
    内白：日三横之间各 34 单位；十横与日底之间 64 单位。
    """
    g = Glyph("uni8349", advance=1000, unicode=0x8349, note="草：艹＋早")
    rad_kusa(g)
    comp_nichi(g, 280, 720, 616, 272, W_SEC)
    g.hbar(120, 880, 160, W_MAIN)        # 十 横
    g.vbar(500, 160, 0, W_MAIN)          # 十 竖
    return g


def uni707D() -> Glyph:
    """災 U+707D（7 画）—— 巛 + 火。

    部件分区：巛 y 600..816，三组「く」形折笔（每组两段斜画，构成标准折角）；
    火 y 32..570（丶 500、丿 500、长撇 540→300、捺 470→760）。
    斜切：左上点 -14（丶），右上短撇 +14。
    """
    g = Glyph("uni707D", advance=1000, unicode=0x707D, note="災：巛＋火")
    # 巛：三组折笔（折角偏左）
    g.diag(360, 778, 230, 700, W_MAIN)
    g.diag(230, 700, 350, 600, W_MAIN)
    g.diag(630, 778, 500, 700, W_MAIN)
    g.diag(500, 700, 620, 600, W_MAIN)
    g.diag(900, 778, 770, 700, W_MAIN)
    g.diag(770, 700, 890, 600, W_MAIN)
    # 火
    g.dot(315, 495, 108, 126, -14)       # 丶
    g.dot(685, 495, 108, 128, 14)        # 丿（右上短撇）
    g.diag(545, 575, 285, 45, W_MAIN)    # 撇
    g.diag(463, 405, 785, 45, W_MAIN)    # 捺（接撇的中段）
    return g


def uni6790() -> Glyph:
    """析 U+6790（8 画）—— 木 + 斤。

    部件分区：木 x 60..452（横 660、竖 245、撇 248→110、捺 180→408）；
    斤 x 470..940（长平撇 900→545、长竖撇 570→518、横 360、垂竖 790）。
    """
    g = Glyph("uni6790", advance=1000, unicode=0x6790, note="析：木＋斤")
    rad_kihen(g)
    comp_kin(g)
    return g


def uni8089() -> Glyph:
    """肉 U+8089（6 画）—— 冂 + 仌（两人）。

    部件分区：冂 x 72..928（左竖 120、右竖 880、顶横 772）；内部上人 y 470..680、
    下人 y 60..430，两组人字均自中线向左右分张。
    """
    g = Glyph("uni8089", advance=1000, unicode=0x8089, note="肉：冂＋仌")
    g.vbar(120, 820, 0, W_MAIN)          # 冂 左竖
    g.hbar(120, 880, 772, W_MAIN)        # 冂 顶横
    g.vbar(880, 820, 0, W_MAIN)          # 冂 右竖
    # 内：上人
    g.diag(505, 680, 360, 470, W_MAIN)
    g.diag(505, 680, 660, 470, W_MAIN)
    # 内：下人
    g.diag(490, 430, 270, 60, W_MAIN)
    g.diag(490, 430, 730, 60, W_MAIN)
    return g


def uni6311() -> Glyph:
    """挑 U+6311（9 画）—— 扌 + 兆。

    部件分区：扌 x 60..380；兆 x 420..940（主撇 620→545、主竖钩 760、钩 760→880，
    丶左上 495、丶左下 478、丿右上 895→862、丿右下 895→860）。
    """
    g = Glyph("uni6311", advance=1000, unicode=0x6311, note="挑：扌＋兆")
    rad_tehen(g)
    comp_chou(g)
    return g


def uni5F8B() -> Glyph:
    """律 U+5F8B（9 画）—— 彳 + 聿。

    部件分区：彳 x 60..300（撇 300→160、撇 320→150、竖 190）；聿 x 350..940。
    """
    g = Glyph("uni5F8B", advance=1000, unicode=0x5F8B, note="律：彳＋聿")
    # 彳
    g.diag(300, 785, 160, 645, W_SEC)    # 撇 1
    g.diag(320, 620, 150, 400, W_SEC)    # 撇 2
    g.vbar(190, 460, 0, W_SEC)           # 竖
    comp_bitsu(g)
    return g


def uni81F3() -> Glyph:
    """至 U+81F3（6 画）—— 一 + 厶 + 土。

    部件分区：一 y 724..820；厶 y 526..700（撇 540→300、折 570、点 610）；
    土 y 102..480（上横 420、竖 480→200、下横 150）。
    """
    g = Glyph("uni81F3", advance=1000, unicode=0x81F3, note="至：一＋厶＋土")
    g.hbar(140, 860, 772, W_MAIN)        # 一
    g.diag(540, 700, 300, 560, W_SEC)    # 厶 撇
    g.hbar(300, 590, 560, W_SEC)         # 厶 折
    g.dot(610, 620, 84, 100, -14)        # 厶 点
    g.hbar(200, 800, 420, W_MAIN)        # 土 上横
    g.vbar(500, 480, 200, W_MAIN)        # 土 竖
    g.hbar(120, 880, 150, W_MAIN)        # 土 下横
    return g


def uni5B97() -> Glyph:
    """宗 U+5B97（8 画）—— 宀 + 示。

    部件分区：宀 y 530..818；示 y 0..518（横 470、横 330、竖 500→0、
    左撇 460→300、右点 630）。
    """
    g = Glyph("uni5B97", advance=1000, unicode=0x5B97, note="宗：宀＋示")
    rad_ukanmuri(g)
    g.hbar(260, 740, 470, W_MAIN)        # 示 横 1
    g.hbar(160, 840, 330, W_MAIN)        # 示 横 2
    g.vbar(500, 330, 0, W_MAIN)          # 示 竖
    g.diag(460, 270, 300, 30, W_THIN)    # 示 撇
    g.dot(630, 165, 88, 106, -14)        # 示 点
    return g


def uni4FC3() -> Glyph:
    """促 U+4FC3（9 画）—— 亻 + 足。

    部件分区：亻 x 60..300；足 x 340..940（口 y 560..800，竖 430/820；
    龰：竖 640→250、短横 480、撇 620→420、捺 620→890）。
    """
    g = Glyph("uni4FC3", advance=1000, unicode=0x4FC3, note="促：亻＋足")
    rad_hen(g)
    comp_kuchi(g, 430, 820, 800, 560, W_SEC)
    # 龰
    g.vbar(620, 640, 250, W_SEC)
    g.hbar(620, 820, 480, W_SEC)
    g.diag(620, 440, 420, 50, W_THIN)
    g.diag(620, 440, 890, 50, W_MAIN)
    return g


def uni5B99() -> Glyph:
    """宙 U+5B99（8 画）—— 宀 + 由。

    部件分区：宀 y 530..818；由 x 234..766（中竖 500 上出 620、左右竖 280/720、
    三横 514/300/86）。
    """
    g = Glyph("uni5B99", advance=1000, unicode=0x5B99, note="宙：宀＋由")
    rad_ukanmuri(g)
    g.vbar(500, 620, 40, W_SEC)          # 由 中竖（上出）
    g.vbar(280, 560, 40, W_SEC)          # 由 左竖
    g.vbar(720, 560, 40, W_SEC)          # 由 右竖
    g.hbar(234, 766, 514, W_SEC)         # 由 顶横
    g.hbar(234, 766, 300, W_SEC)         # 由 中横
    g.hbar(234, 766, 86, W_SEC)          # 由 底横
    return g


def uni4FCA() -> Glyph:
    """俊 U+4FCA（9 画）—— 亻 + 夋。

    部件分区：亻 x 60..300；夋 x 340..940（厶 660..780、八 470..610、夂 40..430）。
    """
    g = Glyph("uni4FCA", advance=1000, unicode=0x4FCA, note="俊：亻＋夋")
    rad_hen(g)
    comp_shun(g)
    return g


def uni79D2() -> Glyph:
    """秒 U+79D2（9 画）—— 禾 + 少。

    部件分区：禾 x 60..464；少 x 456..872（中竖 700→400、左撇 620→520、
    右点 830、长撇 640→500）。
    """
    g = Glyph("uni79D2", advance=1000, unicode=0x79D2, note="秒：禾＋少")
    rad_nogihen(g)
    g.vbar(700, 740, 400, W_SEC)         # 少 竖
    g.diag(620, 620, 520, 480, W_THIN)   # 少 左撇
    g.dot(830, 600, 84, 100, -14)        # 少 右点
    g.diag(640, 400, 500, 50, W_MAIN)    # 少 长撇
    return g


def uni4FB5() -> Glyph:
    """侵 U+4FB5（9 画）—— 亻 + 帚。

    部件分区：亻 x 60..300；帚 x 340..940（ヨ 480..818、冖 352..448、又 50..292）。
    """
    g = Glyph("uni4FB5", advance=1000, unicode=0x4FB5, note="侵：亻＋帚")
    rad_hen(g)
    comp_hou(g)
    return g


def uni62EC() -> Glyph:
    """括 U+62EC（9 画）—— 扌 + 舌。

    部件分区：扌 x 60..380；舌 x 420..940（千 350..790、口 0..380）。
    """
    g = Glyph("uni62EC", advance=1000, unicode=0x62EC, note="括：扌＋舌")
    rad_tehen(g)
    comp_zetsu(g)
    return g


def uni5B5D() -> Glyph:
    """孝 U+5B5D（7 画）—— 耂 + 子。

    部件分区：耂 y 430..820（横 760、横 600、竖 820→560、长撇 640→270）；
    子 y 20..442（横撇 400、竖钩 530→60、长横 180）。
    """
    g = Glyph("uni5B5D", advance=1000, unicode=0x5B5D, note="孝：耂＋子")
    # 耂
    g.hbar(230, 700, 760, W_MAIN)        # 横 1
    g.vbar(460, 820, 560, W_MAIN)         # 竖
    g.hbar(120, 880, 600, W_MAIN)        # 横 2
    g.diag(640, 720, 270, 430, W_SEC)     # 长撇
    # 子
    g.hbar(270, 720, 400, W_THIN)        # 横撇 横
    g.diag(720, 400, 530, 260, W_THIN)   # 横撇 撇
    g.vbar(530, 400, 60, W_SEC)          # 竖钩
    g.hbar(170, 870, 180, W_MAIN)        # 长横
    return g


def uni523A() -> Glyph:
    """刺 U+523A（8 画）—— 朿 + 刂。

    部件分区：朿 x 60..640（顶横 772、中竖 820→260、冂 134..566 y 500..700、
    撇 350→170、捺 350→560）；刂 x 700..940。
    """
    g = Glyph("uni523A", advance=1000, unicode=0x523A, note="刺：朿＋刂")
    g.hbar(60, 640, 772, W_MAIN)         # 朿 顶横
    g.vbar(350, 820, 260, W_MAIN)        # 朿 中竖
    g.vbar(180, 700, 500, W_SEC)         # 朿 冂 左竖
    g.hbar(134, 566, 654, W_SEC)         # 朿 冂 顶横
    g.vbar(520, 700, 500, W_SEC)         # 朿 冂 右竖
    g.diag(350, 520, 170, 180, W_MAIN)   # 朿 撇
    g.diag(350, 520, 560, 180, W_MAIN)   # 朿 捺
    comp_rittou(g)
    return g


def uni5230() -> Glyph:
    """到 U+5230（8 画）—— 至 + 刂。

    部件分区：至 x 60..660；刂 x 700..940。
    """
    g = Glyph("uni5230", advance=1000, unicode=0x5230, note="到：至＋刂")
    comp_iti(g)
    comp_rittou(g)
    return g


def uni900F() -> Glyph:
    """透 U+900F（9 画）—— 辶 + 秀。

    部件分区：辶 x 80..940（点 770、横折 630→300、平捺 290→110 自左下横扫右下）；
    秀 x 440..930（禾 400..780、乃 223..332）。
    """
    g = Glyph("uni900F", advance=1000, unicode=0x900F, note="透：辶＋秀")
    # 辶
    g.dot(140, 770, 92, 100, -14)        # 辶 点
    g.hbar(80, 250, 630, W_THIN)         # 横折折撇 横
    g.diag(250, 630, 100, 300, W_THIN)   # 横折折撇 撇
    g.diag(100, 290, 930, 110, W_MAIN)   # 平捺（自左下横扫右下）
    # 秀：禾
    g.diag(820, 780, 570, 690, W_THIN)   # 禾 顶撇
    g.hbar(440, 900, 620, W_SEC)         # 禾 横
    g.vbar(660, 730, 410, W_SEC)         # 禾 竖
    g.diag(660, 470, 560, 400, W_MAIN)   # 禾 撇
    g.diag(660, 450, 860, 400, W_MAIN)   # 禾 捺
    # 秀：乃
    g.hbar(600, 870, 290, W_THIN)        # 乃 横
    g.diag(870, 290, 770, 220, W_THIN)   # 乃 折
    g.diag(670, 290, 630, 255, W_THIN)   # 乃 撇
    return g


def uni6D25() -> Glyph:
    """津 U+6D25（9 画）—— 氵 + 聿。

    部件分区：氵 x 60..300；聿 x 350..940。
    """
    g = Glyph("uni6D25", advance=1000, unicode=0x6D25, note="津：氵＋聿")
    rad_sanzui(g)
    comp_bitsu(g)
    return g


def uni4EEE() -> Glyph:
    """仮 U+4EEE（6 画）—— 亻 + 反。

    部件分区：亻 x 60..300；反 x 340..940（厂：一 772、撇 430→350；又：横 400、
    横撇 860→620、捺 690→895）。
    """
    g = Glyph("uni4EEE", advance=1000, unicode=0x4EEE, note="仮：亻＋反")
    rad_hen(g)
    g.hbar(380, 940, 772, W_MAIN)        # 反 厂 横
    g.diag(430, 772, 350, 80, W_SEC)     # 反 厂 撇
    g.hbar(430, 860, 400, W_THIN)        # 反 又 横
    g.diag(860, 400, 620, 160, W_THIN)   # 反 又 横撇
    g.diag(690, 270, 895, 65, W_MAIN)    # 反 又 捺
    return g


def uni662F() -> Glyph:
    """是 U+662F（9 画）—— 日 + 一 + 疋。

    部件分区：日 x 234..816 y 460..820；三横 774/640/506；
    宽横 y 332..428；疋：竖 280→60、短横 240、撇 500→380、捺 500→880。
    """
    g = Glyph("uni662F", advance=1000, unicode=0x662F, note="是：日＋疋")
    comp_nichi(g, 280, 770, 820, 460, W_SEC)
    g.hbar(120, 880, 380, W_MAIN)        # 宽横
    g.vbar(280, 340, 60, W_MAIN)         # 疋 竖
    g.hbar(280, 520, 240, W_THIN)        # 疋 短横
    g.diag(500, 260, 380, 60, W_THIN)    # 疋 撇
    g.diag(500, 260, 880, 60, W_MAIN)    # 疋 捺
    return g


def uni829D() -> Glyph:
    """芝 U+829D（6 画）—— 艹 + 之。

    部件分区：艹 y 630..818；之 y 60..672（点 620、横撇 470→240、捺 330→900）。
    """
    g = Glyph("uni829D", advance=1000, unicode=0x829D, note="芝：艹＋之")
    rad_kusa(g)
    g.dot(400, 620, 88, 104, -14)        # 之 点
    g.hbar(210, 600, 470, W_THIN)        # 之 横撇 横
    g.diag(600, 470, 330, 240, W_THIN)   # 之 横撇 撇
    g.diag(330, 260, 900, 70, W_MAIN)    # 之 捺
    return g


def uni5438() -> Glyph:
    """吸 U+5438（6 画）—— 口 + 及。

    部件分区：口 x 74..326 y 180..720；及 x 420..940。
    """
    g = Glyph("uni5438", advance=1000, unicode=0x5438, note="吸：口＋及")
    comp_kuchi(g, 120, 280, 720, 180, W_SEC)
    comp_oku(g)
    return g


def uni5178() -> Glyph:
    """典 U+5178（8 画）—— 曲部 + 一 + 八。

    部件分区：上部 x 214..786（双竖 260/740、内竖 420/580、横 774/590），
    下方宽横 446 为「一」，八：撇 400→230、捺 600→780。
    """
    g = Glyph("uni5178", advance=1000, unicode=0x5178, note="典：曲＋一＋八")
    g.vbar(260, 780, 446, W_SEC)         # 左竖
    g.vbar(740, 780, 446, W_SEC)         # 右竖
    g.vbar(420, 780, 446, W_THIN)        # 内竖 1
    g.vbar(580, 780, 446, W_THIN)        # 内竖 2
    g.hbar(214, 786, 774, W_SEC)         # 顶横
    g.hbar(214, 786, 590, W_SEC)         # 内横
    g.hbar(120, 880, 446, W_MAIN)        # 宽横（＝一）
    g.diag(400, 380, 230, 40, W_MAIN)    # 八 撇
    g.diag(600, 380, 780, 40, W_MAIN)    # 八 捺
    return g


def uni6271() -> Glyph:
    """扱 U+6271（6 画）—— 扌 + 及。

    部件分区：扌 x 60..380；及 x 420..940。
    """
    g = Glyph("uni6271", advance=1000, unicode=0x6271, note="扱：扌＋及")
    rad_tehen(g)
    comp_oku(g)
    return g


def uni770B() -> Glyph:
    """看 U+770B（9 画）—— 龵 + 目。

    部件分区：龵 y 650..820（撇 775→180、横 772、横 650、竖 810→480）；
    目 x 234..826 y 0..526（四横 480/355/230/105、右竖 780）。
    """
    g = Glyph("uni770B", advance=1000, unicode=0x770B, note="看：龵＋目")
    g.diag(430, 775, 180, 680, W_SEC)    # 龵 撇
    g.hbar(240, 920, 772, W_MAIN)        # 龵 横 1
    g.hbar(200, 900, 650, W_MAIN)        # 龵 横 2
    g.vbar(280, 810, 480, W_MAIN)        # 竖（兼目之左竖）
    g.hbar(234, 826, 480, W_SEC)         # 目 顶横
    g.hbar(234, 826, 355, W_SEC)         # 目 中横 1
    g.hbar(234, 826, 230, W_SEC)         # 目 中横 2
    g.hbar(234, 826, 105, W_SEC)         # 目 底横
    g.vbar(780, 526, 0, W_SEC)           # 目 右竖
    return g


def uni6212() -> Glyph:
    """戒 U+6212（7 画）—— 戈 + 廾。

    部件分区：戈：横 760（140..720）、斜钩 560→860、撇 660→300、点 830；
    廾：横 460（160..680）、撇 290→170、竖 530→60。
    """
    g = Glyph("uni6212", advance=1000, unicode=0x6212, note="戒：戈＋廾")
    g.hbar(140, 720, 760, W_MAIN)        # 戈 横
    g.dot(830, 700, 84, 100, -14)        # 戈 点
    g.diag(560, 795, 860, 200, W_MAIN)   # 戈 斜钩
    g.diag(660, 520, 300, 180, W_SEC)    # 戈 撇
    g.hbar(160, 680, 460, W_MAIN)        # 廾 横
    g.diag(290, 600, 170, 60, W_SEC)     # 廾 撇
    g.vbar(530, 600, 60, W_MAIN)         # 廾 竖
    return g


def uni7949() -> Glyph:
    """祉 U+7949（8 画）—— 礻 + 止。

    部件分区：礻 x 60..380（点 760、横撇 610→150、竖 470→0、右点 430）；
    止 x 420..940（竖 780→190、短横 620、右竖 620→190、长横 190）。
    """
    g = Glyph("uni7949", advance=1000, unicode=0x7949, note="祉：礻＋止")
    g.dot(150, 760, 90, 104, -14)        # 礻 点
    g.hbar(85, 330, 610, W_THIN)         # 礻 横撇 横
    g.diag(330, 610, 150, 400, W_THIN)   # 礻 横撇 撇
    g.vbar(215, 470, 0, W_SEC)           # 礻 竖
    g.dot(300, 430, 84, 100, -14)        # 礻 右点
    # 止
    g.vbar(620, 780, 190, W_MAIN)        # 止 主竖
    g.hbar(620, 880, 620, W_THIN)        # 止 短横
    g.vbar(840, 620, 190, W_SEC)         # 止 右竖
    g.hbar(420, 940, 190, W_MAIN)        # 止 长横
    return g


def uni594F() -> Glyph:
    """奏 U+594F（9 画）—— 𡗗（三＋人） + 天。

    部件分区：𡗗 y 340..818（三横 772/648/524，撇 780→160，捺 660→880）；
    天 y 40..326（两横 280/170，撇 300→300，捺 290→870）。
    """
    g = Glyph("uni594F", advance=1000, unicode=0x594F, note="奏：𡗗＋天")
    g.hbar(230, 770, 772, W_SEC)         # 横 1
    g.hbar(190, 810, 648, W_SEC)         # 横 2
    g.hbar(150, 850, 524, W_SEC)         # 横 3
    g.diag(700, 780, 160, 340, W_SEC)    # 撇
    g.diag(520, 660, 880, 340, W_SEC)    # 捺
    g.hbar(240, 760, 280, W_SEC)         # 天 横 1
    g.hbar(170, 830, 170, W_SEC)         # 天 横 2
    g.diag(580, 300, 300, 40, W_THIN)    # 天 撇
    g.diag(550, 290, 870, 40, W_MAIN)    # 天 捺
    return g


def uni5FEB() -> Glyph:
    """快 U+5FEB（7 画）—— 忄 + 夬。

    部件分区：忄 x 64..337（左点 460、右点 620、竖 820→0）；
    夬 x 380..940（横 660、折竖 847→420、宽横 320、主撇 660→395、捺 520→900）。
    """
    g = Glyph("uni5FEB", advance=1000, unicode=0x5FEB, note="快：忄＋夬")
    g.dot(120, 460, 84, 100, -14)        # 忄 左点
    g.dot(300, 620, 84, 100, -14)        # 忄 右点
    g.vbar(200, 820, 0, W_SEC)           # 忄 竖
    # 夬
    g.hbar(450, 893, 660, W_SEC)         # 夬 横
    g.vbar(847, 706, 420, W_SEC)         # 夬 折竖
    g.hbar(380, 940, 320, W_SEC)         # 夬 宽横
    g.diag(660, 800, 395, 30, W_MAIN)    # 夬 主撇
    g.diag(520, 300, 900, 50, W_MAIN)    # 夬 捺
    return g


def uni514D() -> Glyph:
    """免 U+514D（8 画）—— ⺈ + 日 + 儿。

    部件分区：⺈ y 660..810（撇 540→330、横撇 760）；日 x 294..866 y 240..640
    （三横 594/452/310）；儿 y 40..250（撇 430→260、竖弯钩 640→60）。
    """
    g = Glyph("uni514D", advance=1000, unicode=0x514D, note="免：⺈＋日＋儿")
    g.diag(540, 780, 330, 660, W_SEC)    # ⺈ 撇
    g.hbar(340, 790, 760, W_SEC)         # ⺈ 横撇 横
    g.diag(790, 760, 660, 600, W_THIN)   # ⺈ 横撇 撇
    # 日
    comp_nichi(g, 340, 820, 640, 240, W_SEC)
    # 儿
    g.diag(430, 250, 260, 40, W_SEC)     # 撇
    g.vbar(640, 250, 60, W_SEC)          # 竖弯钩
    g.diag(640, 90, 760, 50, W_THIN)     # 钩
    return g


def uni6CC9() -> Glyph:
    """泉 U+6CC9（9 画）—— 白 + 水。

    部件分区：白 x 374..726 y 480..818（撇 788→420、三横 774/650/526、双竖 420/680）；
    水 y 0..470（中竖 500→0、横撇 380→200、右撇 430→545、捺 240→840）。
    """
    g = Glyph("uni6CC9", advance=1000, unicode=0x6CC9, note="泉：白＋水")
    g.diag(540, 786, 420, 690, W_THIN)   # 白 撇
    g.vbar(420, 818, 480, W_SEC)
    g.vbar(680, 818, 480, W_SEC)
    g.hbar(374, 726, 774, W_SEC)
    g.hbar(374, 726, 650, W_SEC)
    g.hbar(374, 726, 526, W_SEC)
    # 水
    g.vbar(500, 470, 0, W_MAIN)          # 中竖
    g.hbar(300, 500, 380, W_THIN)        # 横撇 横
    g.diag(300, 380, 200, 250, W_THIN)   # 横撇 撇
    g.diag(680, 430, 545, 210, W_THIN)   # 右撇
    g.diag(540, 240, 840, 40, W_MAIN)    # 捺
    return g


# --------------------------------------------------------------- 装配
def build() -> list[Glyph]:
    return [
        uni8349(),   # 草
        uni707D(),   # 災
        uni6790(),   # 析
        uni8089(),   # 肉
        uni6311(),   # 挑
        uni5F8B(),   # 律
        uni81F3(),   # 至
        uni5B97(),   # 宗
        uni4FC3(),   # 促
        uni5B99(),   # 宙
        uni4FCA(),   # 俊
        uni79D2(),   # 秒
        uni4FB5(),   # 侵
        uni62EC(),   # 括
        uni5B5D(),   # 孝
        uni523A(),   # 刺
        uni5230(),   # 到
        uni900F(),   # 透
        uni6D25(),   # 津
        uni4EEE(),   # 仮
        uni662F(),   # 是
        uni829D(),   # 芝
        uni5438(),   # 吸
        uni5178(),   # 典
        uni6271(),   # 扱
        uni770B(),   # 看
        uni6212(),   # 戒
        uni7949(),   # 祉
        uni594F(),   # 奏
        uni5FEB(),   # 快
        uni514D(),   # 免
        uni6CC9(),   # 泉
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-012.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
