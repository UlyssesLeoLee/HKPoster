"""HK Poster Heavy —— Wave 0 汉字试制（lane: cjk-core）。

字符清单（CONTRACT §5 冻结）：
    港 U+6E2F / 影 U+5F71 / 城 U+57CE / 火 U+706B / 夜 U+591C / 風 U+98A8

方法（与 cjk-dense lane 同法）：每个字先写笔画清单与部件分区坐标，
再逐笔画落坐标并注明所属部件；密排处留白口，疏字用足笔画重量。

CJK 字面顶线 = 820（Latin 大写顶线是 700，两套各自成立）。
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
W_HAIR = 76

CJK_TOP = 820


def glyph_gang() -> Glyph:
    """港。

    左右结构：氵(x 38..250) + 巷(x 300..940)。
    巷分两层：共(480..838) / 巳(4..466)，两层之间留白口 14 单位以上。
    取舍：巷笔画密集，整体降到 84（横 96 保留骨架），让墨量率不压过同族；
      巳的左竖与底弯钩连成一体，保住「己」形识别；氵的两点用 94 宽。
    """
    g = Glyph("uni6E2F", advance=1000, unicode=0x6E2F, note="港（Wave 0 代表字形）")

    # ---- 氵 ----
    g.dot(158, 700, w=94, h=126, slant=26)      # 氵的上点
    g.dot(150, 468, w=94, h=126, slant=26)      # 氵的下点
    g.diag(70, 140, 248, 308, weight=92)       # 氵的提

    # ---- 共 ----
    g.hbar(330, 920, 790, weight=W_MAIN)       # 共的上横
    g.vbar(450, 830, 640, weight=W_THIN)       # 共的左竖
    g.vbar(810, 830, 640, weight=W_THIN)       # 共的右竖
    g.hbar(300, 940, 640, weight=W_MAIN)       # 共的下横
    g.diag(650, 600, 420, 480, weight=W_HAIR)   # 共的撇
    g.dot(745, 552, w=84, h=96, slant=26)      # 共的点

    # ---- 巳 ----
    g.hbar(370, 880, 420, weight=W_THIN)       # 巳的上横
    g.vbar(880, 420, 280, weight=W_THIN)       # 巳的右竖
    g.hbar(370, 880, 280, weight=W_THIN)       # 巳的中横
    g.vbar(370, 420, 50, weight=W_THIN)        # 巳的左竖
    g.hbar(370, 880, 50, weight=W_THIN)        # 巳的底横
    g.vbar(880, 50, 140, weight=W_HAIR)        # 巳的钩
    return g


def glyph_ying() -> Glyph:
    """影。

    左右结构：景(x 60..600) + 彡(x 660..940)。
    景自上而下：日(620..858) / 亠(474..566) / 口(248..452) / 小(40..230)。
    取舍：日与亠之间留 52 单位、亠与口之间留 22 单位、口与小之间留 18 单位；
      彡三撇自上而下等距（每撇落差 190），彼此不相接。
    """
    g = Glyph("uni5F71", advance=1000, unicode=0x5F71, note="影（Wave 0 代表字形）")

    # ---- 景上部：日 ----
    g.hbar(180, 460, 778, weight=W_THIN)       # 日的上横
    g.vbar(220, 778, 620, weight=W_THIN)       # 日的左竖
    g.vbar(420, 778, 620, weight=W_THIN)       # 日的右竖
    g.hbar(180, 460, 700, weight=76)           # 日的中横
    g.hbar(180, 460, 620, weight=W_THIN)       # 日的下横

    # ---- 景：亠 ----
    g.dot(300, 570, w=76, h=70, slant=0)       # 亠的点
    g.hbar(80, 520, 520, weight=W_SEC)         # 亠的横

    # ---- 景：口 ----
    g.hbar(190, 410, 410, weight=W_THIN)       # 口的上横
    g.vbar(230, 410, 290, weight=W_THIN)       # 口的左竖
    g.vbar(370, 410, 290, weight=W_THIN)       # 口的右竖
    g.hbar(190, 410, 290, weight=W_THIN)       # 口的下横

    # ---- 景下部：小 ----
    g.vbar(300, 230, 40, weight=W_SEC)         # 小的竖
    g.dot(190, 150, w=72, h=80, slant=-14)     # 小的左点
    g.dot(410, 150, w=72, h=80, slant=14)      # 小的右点

    # ---- 彡 ----
    g.diag(900, 780, 690, 660, weight=W_THIN)  # 彡的第一撇
    g.diag(900, 590, 690, 470, weight=W_THIN)  # 彡的第二撇
    g.diag(900, 400, 680, 240, weight=W_THIN)  # 彡的第三撇
    return g


def glyph_cheng() -> Glyph:
    """城。

    左右结构：土(x 60..350) + 成(x 390..945)。
    成自上而下：顶横(642..738) / 横折钩(210..474) / 斜钩(130..760) / 内撇 / 点。
    取舍：斜钩走在横折钩的**右侧**（横折钩的竖在 x=790，斜钩从 x=660 斜到 x=880），
      两者不交叉；斜钩尾端补钩，向右下冲出制造动势。
    """
    g = Glyph("uni57CE", advance=1000, unicode=0x57CE, note="城（Wave 0 代表字形）")

    # ---- 土 ----
    g.hbar(90, 320, 570, weight=W_SEC)         # 土的横
    g.vbar(205, 700, 90, weight=W_SEC)         # 土的竖
    g.hbar(60, 350, 130, weight=W_MAIN)        # 土的提

    # ---- 成 ----
    g.hbar(400, 905, 690, weight=W_MAIN)       # 成的顶横
    g.diag(555, 690, 395, 80, weight=W_SEC)    # 成的左撇
    g.hbar(600, 790, 430, weight=W_SEC)        # 成的横折钩横
    g.vbar(790, 430, 210, weight=W_SEC)        # 成的横折钩竖
    g.diag(660, 760, 880, 130, weight=W_SEC)   # 成的斜钩
    g.diag(880, 130, 938, 190, weight=W_HAIR)  # 成的钩尾
    g.diag(745, 570, 600, 350, weight=W_THIN)  # 成的内撇
    g.dot(880, 772, w=84, h=92, slant=20)      # 成的点
    return g


def glyph_huo() -> Glyph:
    """火。

    独体四笔：左点(575..705) / 右上短撇 / 长撇 / 捺。
    取舍：火是本 lane 最疏的字（4 笔），墨量率天然低于同族中位数——
      这是**结构密度差异**而非风格漂移（见 docs/09 RV-10）。
      因此用足重量（长撇捺 96、短撇 92、点放大到 110×130），
      并让上下两段在 y 640 处明确分开，保证它仍显"厚重"。
    """
    g = Glyph("uni706B", advance=1000, unicode=0x706B, note="火（Wave 0 代表字形）")

    g.dot(250, 640, w=110, h=130, slant=26)     # 左点
    g.diag(700, 700, 590, 570, weight=W_SEC)   # 右上短撇
    g.diag(500, 680, 180, 60, weight=W_MAIN)   # 长撇
    g.diag(520, 680, 840, 60, weight=W_MAIN)   # 捺
    return g


def glyph_ye() -> Glyph:
    """夜。

    上中下结构：亠(662..840) / 左亻(60..450) / 右夂+点(120..830)。
    取舍：亠占顶 180 单位独占一层；亻的撇与竖在 (180..240, 398..450) 交汇，
      保证左侧不是一个飘空的撇；夂的横撇与捺分列，内白不粘连。
    """
    g = Glyph("uni591C", advance=1000, unicode=0x591C, note="夜（Wave 0 代表字形）")

    # ---- 亠 ----
    g.dot(500, 800, w=76, h=80, slant=0)       # 亠的点
    g.hbar(100, 900, 710, weight=W_MAIN)       # 亠的横

    # ---- 亻 ----
    g.diag(330, 680, 180, 420, weight=W_SEC)   # 亻的撇
    g.vbar(240, 450, 60, weight=W_SEC)         # 亻的竖

    # ---- 夂 + 点 ----
    g.diag(660, 660, 500, 470, weight=W_SEC)   # 夂的撇
    g.hbar(560, 830, 590, weight=W_SEC)        # 夂的横
    g.diag(710, 590, 545, 420, weight=W_SEC)   # 夂的横撇下行
    g.diag(560, 500, 880, 120, weight=W_MAIN)  # 夂的捺
    g.dot(840, 260, w=74, h=82, slant=18)       # 右下点
    return g


def glyph_feng() -> Glyph:
    """風。

    包围结构：几外框(120..938) + 内部「虫」(330..700)。
    取舍：外框用 92（比主笔画略细），让"框"与"内容"有对比；
      内部虫的口放大到 x 330..690、y 348..662，单独成框看得清；
      几的左撇与右竖带冲出，弯钩向右下收笔，不做满包围。
    """
    g = Glyph("uni98A8", advance=1000, unicode=0x98A8, note="風（Wave 0 代表字形）")

    # ---- 几 ----
    g.hbar(180, 880, 790, weight=W_SEC)        # 几的顶横
    g.diag(215, 800, 115, 60, weight=W_SEC)    # 几的左撇
    g.vbar(855, 800, 210, weight=W_SEC)        # 几的右竖
    g.diag(855, 210, 940, 125, weight=W_THIN)  # 几的弯钩

    # ---- 虫 ----
    g.hbar(330, 690, 620, weight=W_THIN)       # 虫的口上横
    g.vbar(370, 620, 390, weight=W_THIN)       # 虫的口左竖
    g.vbar(650, 620, 390, weight=W_THIN)       # 虫的口右竖
    g.hbar(330, 690, 390, weight=W_THIN)       # 虫的口下横
    g.vbar(510, 620, 210, weight=W_THIN)       # 虫的竖
    g.hbar(350, 700, 210, weight=W_THIN)       # 虫的提
    g.dot(655, 265, w=74, h=82, slant=16)      # 虫的点
    return g


def build() -> list[Glyph]:
    return [
        glyph_gang(),
        glyph_ying(),
        glyph_cheng(),
        glyph_huo(),
        glyph_ye(),
        glyph_feng(),
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-cjk-core.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
