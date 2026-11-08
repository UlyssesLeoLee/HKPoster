"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s3-015。

本批 24 字，笔画范围 10–13（照 13 / 酒 10 / 堂 11 / 渋 11 / 群 13 / 悲 12 /
携 13 / 奥 12 / 診 12 / 詰 13 / 託 10 / 晴 12 / 掛 11 / 寝 13 / 暗 13 /
裂 12 / 敏 10 / 鳥 11 / 純 10 / 飯 12 / 排 11 / 裕 12 / 堅 12 / 訳 11），
取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
* 字面框 x 60..940 / y 0..820，advance = 1000，与繁体汉字同档。
* 笔画权重：主 96 / 次 92 / 细 84 / 点 84。密字（照/携/詰/寝/暗）把腔体
  内的横画降到 84 或把框高拉开，保证「白口 ≥ 24」。
* **方框硬规**：口/日/目/田 型方框的框高一律 ≥ 2×笔画宽 + 24。
  例：口（w=96）框高 ≥ 216；日（w=96）框高 ≥ 216（实际取 240+）。
* **横横相邻白口 ≥ 24**：每条横的中心线差 ≥ 120（w=96）或 ≥ 108（w=84）。
  全批按 120 网格排（620 / 500 / 380 / 250 …），单字微调 ±5..10 只在
  「同一部件整体平移」的原则下做，绝不单独改某一条横的高度。
* **同族复用（GLY-004）**：言（診/詰/託/訳）、扌（携/掛/排）、日（晴）、
  氵（酒/渋）四个部件在本批内用同一套坐标与同一套笔画拆法。
* 点/短撇一律用斜切平行四边形，档位只用既有档：26（短撇 / 氵上点）、
  -14（丶）、+14（丿 / 丷右 / 灬首点）、0（竖点 / 亠的点）。
  丷（ソ形）左 -14 右 +14；⺌（小字頭）左 +14 右 -14（向外撇开）。
* 竖与竖之间 ≥ 60 单位；斜笔的余隙一律按「垂直于中心线」估算，不按 ±w/2 估。
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

X_L = 60
X_R = 940
Y_B = 0
Y_T = 820


def _g(name: str, cp: int, note: str) -> Glyph:
    return Glyph(name=name, advance=1000, unicode=cp, note=note)


# --------------------------------------------------------------------------
# 可复用部件（本批内坐标完全一致）
# --------------------------------------------------------------------------
def comp_sanzui(g: Glyph) -> None:
    """氵（三点水）：上点短撇 / 中点短撇 / 底部提。x 60..306。"""
    g.dot(170, 700, w=80, h=100, slant=26)          # 上点（短撇 slant=26）
    g.dot(150, 520, w=80, h=100, slant=26)          # 中点（短撇 slant=26）
    g.diag(85, 300, 285, 400, weight=W_SEC)         # 提（右上斜）


def comp_ri(g: Glyph) -> None:
    """言（7 画）：亠 + 二 + 口。x 60..390。用于 診 / 詰 / 託 / 訳。"""
    g.dot(230, 770, w=70, h=80, slant=0)            # 亠 的点（竖点）
    g.hbar(70, 390, 690, weight=W_MAIN)            # 亠 的一
    g.hbar(100, 360, 565, weight=W_MAIN)           # 二的上横
    g.hbar(100, 360, 440, weight=W_MAIN)           # 二的下横
    g.hbar(100, 360, 310, weight=W_MAIN)           # 口的上横
    g.hbar(100, 360, 160, weight=W_MAIN)           # 口的下横
    g.vbar(150, 112, 358, weight=W_MAIN)           # 口的左竖
    g.vbar(310, 112, 358, weight=W_MAIN)           # 口的右竖


def comp_te(g: Glyph) -> None:
    """扌（3 画）：一 + 亅 + 提。x 60..318。用于 携 / 掛 / 排。"""
    g.hbar(70, 300, 700, weight=W_MAIN)            # 上横
    g.vbar(190, 130, 790, weight=W_MAIN)            # 竖（亅）
    g.diag(80, 330, 300, 425, weight=W_SEC)         # 提（右上斜）


def comp_sun(g: Glyph) -> None:
    """日（4 画）：横三 + 竖二。x 60..320。用于 晴。"""
    g.hbar(60, 320, 770, weight=W_MAIN)            # 上横
    g.hbar(60, 320, 470, weight=W_MAIN)            # 中横
    g.hbar(60, 320, 120, weight=W_MAIN)            # 下横
    g.vbar(110, 72, 818, weight=W_MAIN)            # 左竖
    g.vbar(270, 72, 818, weight=W_MAIN)            # 右竖


# --------------------------------------------------------------------------
# 24 字
# --------------------------------------------------------------------------
def glyph_zhao() -> Glyph:
    """照（13 画）：左上 日 + 右上 召（刀 + 口）+ 底 灬。

    部件分区：日 x 60..330 / y 272..818；召 x 380..940 / y 202..818；
    灬 y 50..130。
    """
    g = _g("uni7167", 0x7167, "照：日+召+灬")
    # 日（4 画）：三横两竖，腔高 = 722-368 = 354，远高于 216 下限
    g.hbar(60, 330, 770, weight=W_MAIN)
    g.hbar(60, 330, 545, weight=W_MAIN)
    g.hbar(60, 330, 320, weight=W_MAIN)
    g.vbar(110, 272, 818, weight=W_MAIN)
    g.vbar(285, 272, 818, weight=W_MAIN)
    # 召：刀（2 画）
    g.hbar(400, 930, 770, weight=W_MAIN)           # 刀的横
    g.vbar(900, 520, 770, weight=W_MAIN)           # 刀的折（竖）
    g.diag(720, 760, 450, 560, weight=W_SEC)       # 刀的撇
    # 召：口（3 画）：框高 = 478-202 = 276 ≥ 216
    g.hbar(420, 870, 430, weight=W_MAIN)
    g.hbar(420, 870, 250, weight=W_MAIN)
    g.vbar(470, 202, 478, weight=W_MAIN)
    g.vbar(820, 202, 478, weight=W_MAIN)
    # 灬（4 画）：首点作撇（+14），其余三点作点（-14）
    g.dot(150, 55, w=76, h=96, slant=+14)
    g.dot(380, 55, w=76, h=96, slant=-14)
    g.dot(610, 55, w=76, h=96, slant=-14)
    g.dot(840, 55, w=76, h=96, slant=-14)
    return g


def glyph_shu() -> Glyph:
    """酒（10 画）：氵（3）+ 酉（7）。

    酉 = 顶部一 + 冂（丨 + 𠃍）+ 内一 + 儿（丿 + 乚）+ 底一。
    部件分区：氵 x 60..306 / 酉 x 380..940 / y 82..818。
    """
    g = _g("uni9152", 0x9152, "酒：氵+酉")
    comp_sanzui(g)
    g.hbar(380, 930, 770, weight=W_MAIN)            # 顶部一
    g.hbar(400, 900, 640, weight=W_MAIN)            # 冂的横（𠃍的上）
    g.hbar(440, 860, 500, weight=W_MAIN)            # 内一
    g.hbar(440, 860, 130, weight=W_MAIN)            # 底一
    g.vbar(440, 82, 688, weight=W_MAIN)             # 冂的左竖
    g.vbar(860, 82, 688, weight=W_MAIN)             # 冂的右竖
    g.diag(590, 450, 560, 260, weight=W_SEC)        # 儿·撇
    g.vbar(730, 260, 450, weight=W_SEC)             # 儿·竖弯
    return g


def glyph_dou() -> Glyph:
    """堂（11 画）：尚（⺌ + 冖 + 口，8）+ 土（3）。

    部件分区：⺌ y 660..815；冖 y 520..668；口 y 252..498；土 y 0..218。
    口的框高 = 498-252 = 246 ≥ 216。
    """
    g = _g("uni5802", 0x5802, "堂：尚+土")
    g.vbar(500, 660, 815, weight=W_MAIN)            # ⺌的中竖
    g.dot(370, 745, w=72, h=100, slant=+14)         # ⺌的左点（撇形，向外）
    g.dot(630, 745, w=72, h=100, slant=-14)         # ⺌的右点（点形，向外）
    g.hbar(280, 720, 620, weight=W_MAIN)            # 冖的横
    g.vbar(300, 520, 620, weight=W_SEC)             # 冖的左
    g.vbar(700, 520, 620, weight=W_SEC)             # 冖的右
    g.hbar(360, 640, 450, weight=W_MAIN)            # 口的上横
    g.hbar(360, 640, 300, weight=W_MAIN)            # 口的下横
    g.vbar(410, 252, 498, weight=W_MAIN)            # 口的左竖
    g.vbar(590, 252, 498, weight=W_MAIN)            # 口的右竖
    g.hbar(350, 650, 170, weight=W_MAIN)            # 土的上横
    g.hbar(230, 770, 48, weight=W_MAIN)             # 土的下横
    g.vbar(500, 48, 170, weight=W_MAIN)             # 土的竖
    return g


def glyph_shibu() -> Glyph:
    """渋（11 画）：氵（3）+ ソ（2）+ 正（一 + 止，5）。

    部件分区：氵 x 60..306；右上ソ y 722..818；正 x 380..930 / y 82..688。
    """
    g = _g("uni6E0B", 0x6E0B, "渋：氵+ソ+正")
    comp_sanzui(g)
    g.dot(545, 770, w=70, h=95, slant=-14)          # ソ左（丶形）
    g.dot(775, 770, w=70, h=95, slant=+14)          # ソ右（丿形）
    g.hbar(420, 920, 640, weight=W_MAIN)            # 正的顶横
    g.hbar(670, 900, 400, weight=W_MAIN)            # 止的短横
    g.hbar(380, 930, 130, weight=W_MAIN)            # 止的底横
    g.vbar(670, 130, 640, weight=W_MAIN)            # 止的中竖
    g.vbar(470, 178, 400, weight=W_MAIN)            # 止的左竖
    return g


def glyph_gun() -> Glyph:
    """群（13 画）：君（尹 4 + 口 3，7）+ 羊（丷 2 + 三 3 + 丨 1，6）。

    部件分区：君 x 60..410 / y 12..768；羊 x 520..900 / y 152..815。
    君的口框高 = 258-12 = 246 ≥ 216。
    """
    g = _g("uni7FA4", 0x7FA4, "群：君+羊")
    # 君：尹（4 画）
    g.hbar(130, 400, 720, weight=W_MAIN)            # 尹的上横
    g.hbar(130, 380, 560, weight=W_MAIN)            # 尹的中横
    g.hbar(180, 380, 380, weight=W_MAIN)            # 尹的下横
    g.vbar(380, 380, 720, weight=W_MAIN)            # 尹的右竖
    g.diag(320, 710, 120, 430, weight=W_SEC)        # 尹的撇
    # 君：口（3 画）
    g.hbar(140, 410, 210, weight=W_MAIN)
    g.hbar(140, 410, 60, weight=W_MAIN)
    g.vbar(190, 12, 258, weight=W_MAIN)
    g.vbar(360, 12, 258, weight=W_MAIN)
    # 羊（6 画）
    g.dot(620, 770, w=70, h=90, slant=-14)          # 丷左
    g.dot(800, 770, w=70, h=90, slant=+14)          # 丷右
    g.hbar(570, 860, 640, weight=W_MAIN)            # 上横
    g.hbar(590, 840, 460, weight=W_MAIN)            # 中横
    g.hbar(520, 900, 200, weight=W_MAIN)            # 下横
    g.vbar(710, 200, 640, weight=W_MAIN)            # 贯穿竖
    return g


def glyph_hi() -> Glyph:
    """悲（12 画）：非（8）+ 心（4）。

    部件分区：非 y 352..808 / x 180..780；心 y 32..320 / x 170..736。
    """
    g = _g("uni60B2", 0x60B2, "悲：非+心")
    # 非（8 画）：两竖 + 左右各三横
    g.vbar(400, 400, 760, weight=W_MAIN)
    g.vbar(560, 400, 760, weight=W_MAIN)
    g.hbar(180, 400, 760, weight=W_MAIN)
    g.hbar(180, 400, 580, weight=W_MAIN)
    g.hbar(180, 400, 400, weight=W_MAIN)
    g.hbar(560, 780, 760, weight=W_MAIN)
    g.hbar(560, 780, 580, weight=W_MAIN)
    g.hbar(560, 780, 400, weight=W_MAIN)
    # 心（4 画）：左点 + 卧钩 + 两点
    g.dot(210, 230, w=80, h=100, slant=-14)
    g.vbar(360, 80, 290, weight=W_MAIN)
    g.hbar(360, 660, 80, weight=W_MAIN)
    g.dot(520, 250, w=80, h=100, slant=-14)
    g.dot(700, 270, w=80, h=100, slant=-14)
    return g


def glyph_kiei() -> Glyph:
    """携（13 画）：扌（3）+ 隽（隹 8 + 乃 2）。

    部件分区：扌 x 60..318；隹 x 421..870 / y 277..818；乃 x 435..810 / y 25..228。
    隹的四横间距 125（白口 29），乃的横与隹的底横白口 49。
    """
    g = _g("uni643A", 0x643A, "携：扌+隽")
    comp_te(g)
    # 隹（8 画）
    g.diag(540, 775, 450, 700, weight=W_SEC)        # 丿
    g.dot(660, 770, w=66, h=78, slant=-14)          # 丶
    g.vbar(470, 325, 700, weight=W_MAIN)            # 左竖
    g.vbar(830, 325, 700, weight=W_MAIN)            # 右竖
    g.hbar(530, 870, 700, weight=W_MAIN)            # 横一
    g.hbar(530, 870, 575, weight=W_MAIN)            # 横二
    g.hbar(530, 870, 450, weight=W_MAIN)            # 横三
    g.hbar(530, 870, 325, weight=W_MAIN)            # 横四
    # 乃（2 画）：丿 + 乛（横 + 竖）
    g.diag(570, 175, 470, 55, weight=W_SEC)         # 乃的撇
    g.hbar(520, 810, 180, weight=W_MAIN)            # 乃的横
    g.vbar(800, 60, 180, weight=W_MAIN)             # 乃的竖
    return g


def glyph_oku() -> Glyph:
    """奥（12 画）：丿（1）+ 冂（2）+ 米（6）+ 大（3）。

    部件分区：冂 x 175..805 / y 330..808；米在 x 288..697 / y 409..700；
    大在 x 177..843 / y 23..372。
    """
    g = _g("uni5965", 0x5965, "奥：丿+冂+米+大")
    g.diag(250, 780, 190, 720, weight=W_THIN)       # 顶部丿
    g.hbar(175, 805, 760, weight=W_MAIN)            # 冂的横
    g.vbar(200, 330, 760, weight=W_MAIN)            # 冂的左竖
    g.vbar(780, 330, 760, weight=W_MAIN)            # 冂的右竖
    g.dot(340, 655, w=54, h=58, slant=-14)          # 米的左上丶
    g.dot(640, 655, w=54, h=58, slant=+14)          # 米的右上丿
    g.hbar(290, 690, 545, weight=W_MAIN)            # 米的横
    g.vbar(490, 430, 700, weight=W_MAIN)            # 米的竖
    g.diag(440, 520, 310, 450, weight=W_SEC)        # 米的丿
    g.diag(545, 520, 675, 450, weight=W_SEC)        # 米的㇏
    g.hbar(180, 820, 300, weight=W_MAIN)            # 大的横
    g.diag(480, 340, 210, 55, weight=W_SEC)         # 大的丿
    g.diag(530, 340, 810, 55, weight=W_SEC)         # 大的㇏
    return g


def glyph_shin() -> Glyph:
    """診（12 画）：言（7）+ 㐱（人 2 + 彡 3）。

    部件分区：言 x 60..390；人 x 460..919 / y 595..815；彡 x 616..804 / y 135..570。
    彡 三撇间距 150（白口 15 以上），与参照字的疏排一致。
    """
    g = _g("uni8A3A", 0x8A3A, "診：言+㐱")
    comp_ri(g)
    g.diag(670, 780, 490, 630, weight=W_SEC)        # 人的撇
    g.diag(720, 780, 890, 640, weight=W_SEC)        # 人的捺
    g.diag(790, 530, 630, 475, weight=W_THIN)       # 彡一
    g.diag(790, 380, 630, 325, weight=W_THIN)       # 彡二
    g.diag(790, 230, 630, 175, weight=W_THIN)       # 彡三
    return g


def glyph_ketsu() -> Glyph:
    """詰（13 画）：言（7）+ 吉（士 3 + 口 3）。

    部件分区：言 x 60..390；吉 x 480..910 / y 92..738。口的框高 = 378-92 = 286。
    """
    g = _g("uni8A70", 0x8A70, "詰：言+吉")
    comp_ri(g)
    g.hbar(480, 910, 690, weight=W_MAIN)            # 士的上横
    g.vbar(695, 480, 690, weight=W_MAIN)            # 士的竖
    g.hbar(520, 870, 480, weight=W_MAIN)            # 士的下横
    g.hbar(500, 890, 330, weight=W_MAIN)            # 口的上横
    g.hbar(500, 890, 140, weight=W_MAIN)            # 口的下横
    g.vbar(560, 92, 378, weight=W_MAIN)
    g.vbar(830, 92, 378, weight=W_MAIN)
    return g


def glyph_taku() -> Glyph:
    """託（10 画）：言（7）+ 乇（3：丿 + 一 + 乚）。

    部件分区：言 x 60..390；乇 x 480..900 / y 102..812。
    """
    g = _g("uni8A17", 0x8A17, "託：言+乇")
    comp_ri(g)
    g.diag(700, 770, 520, 690, weight=W_SEC)        # 乇的撇
    g.hbar(480, 900, 640, weight=W_MAIN)            # 乇的横
    g.vbar(690, 150, 640, weight=W_MAIN)            # 乇的竖
    g.hbar(690, 810, 150, weight=W_MAIN)            # 乇的钩
    return g


def glyph_sei() -> Glyph:
    """晴（12 画）：日（4）+ 青（龶 4 + 月 4）。

    部件分区：日 x 60..320；龶 x 390..900 / y 442..798；月 x 482..878 / y 80..500。
    """
    g = _g("uni6674", 0x6674, "晴：日+青")
    comp_sun(g)
    g.hbar(390, 900, 750, weight=W_MAIN)            # 龶的上横
    g.hbar(420, 870, 620, weight=W_MAIN)            # 龶的中横
    g.hbar(390, 900, 490, weight=W_MAIN)            # 龶的下横
    g.vbar(645, 490, 750, weight=W_MAIN)            # 龶的竖
    g.vbar(530, 80, 500, weight=W_MAIN)             # 月的左撇（作竖）
    g.vbar(830, 80, 500, weight=W_MAIN)             # 月的右竖
    g.hbar(530, 830, 340, weight=W_MAIN)            # 月的内横一
    g.hbar(530, 830, 195, weight=W_MAIN)            # 月的内横二
    return g


def glyph_kake() -> Glyph:
    """掛（11 画）：扌（3）+ 卦（圭 6 + 卜 2）。

    部件分区：扌 x 60..318；圭 x 400..840 / y 152..788；卜 x 812..924 / y 300..720。
    """
    g = _g("uni639B", 0x639B, "掛：扌+卦")
    comp_te(g)
    g.hbar(420, 820, 740, weight=W_MAIN)            # 上土的上横
    g.vbar(620, 560, 740, weight=W_MAIN)            # 上土的竖
    g.hbar(430, 810, 600, weight=W_MAIN)            # 上土的下横
    g.vbar(620, 300, 560, weight=W_MAIN)            # 下土的竖
    g.hbar(450, 790, 380, weight=W_MAIN)            # 下土的上横
    g.hbar(400, 840, 200, weight=W_MAIN)            # 下土的下横
    g.vbar(860, 300, 720, weight=W_MAIN)            # 卜的竖
    g.dot(915, 470, w=46, h=60, slant=-14)          # 卜的点
    return g


def glyph_shin2() -> Glyph:
    """寝（13 画）：宀（3）+ 丬（3）+ 彐（3）+ 又（2）。

    部件分区：宀 x 164..856 / y 630..815；丬 x 147..278 / y 330..610；
    彐 x 302..848 / y 272..618；又 x 385..864 / y 16..238。
    彐三横间距 125（白口 29）；彐的底横与又的横白口 34。
    """
    g = _g("uni5BDD", 0x5BDD, "寝：宀+丬+彐+又")
    g.dot(500, 770, w=80, h=90, slant=0)            # 宀的点
    g.vbar(210, 650, 710, weight=W_SEC)             # 宀的左
    g.hbar(180, 820, 700, weight=W_MAIN)            # 宀的横
    g.vbar(810, 630, 700, weight=W_SEC)             # 宀的右
    g.vbar(230, 330, 610, weight=W_MAIN)            # 丬的竖
    g.dot(175, 555, w=56, h=70, slant=-14)          # 丬的上点
    g.dot(175, 400, w=56, h=70, slant=+14)          # 丬的下撇
    g.hbar(350, 820, 570, weight=W_MAIN)            # 彐的横一
    g.vbar(800, 320, 570, weight=W_MAIN)            # 彐的右竖
    g.hbar(350, 800, 445, weight=W_MAIN)            # 彐的横二
    g.hbar(350, 800, 320, weight=W_MAIN)            # 彐的横三
    g.hbar(430, 810, 190, weight=W_MAIN)            # 又的横
    # 又的两撇捺压到 26° 左右（太浅会读成「Z」，且与横的重叠等效长度超 1.5）
    g.diag(800, 215, 460, 45, weight=W_SEC)         # 又的撇
    g.diag(440, 215, 780, 55, weight=W_SEC)         # 又的捺
    return g


def glyph_an() -> Glyph:
    """暗（13 画）：日（4）+ 音（立 5 + 日 4）。

    部件分区：日 x 60..320；立 x 390..900 / y 422..820；音的日 x 480..810 / y 12..378。
    音的日框高 = 378-12 = 366，内白 44 / 34 均 ≥ 24。
    """
    g = _g("uni6697", 0x6697, "暗：日+音")
    comp_sun(g)
    g.dot(645, 780, w=70, h=80, slant=0)            # 立的点
    g.hbar(390, 900, 700, weight=W_MAIN)            # 立的横
    g.dot(540, 590, w=56, h=72, slant=-14)          # 立的左丶
    g.dot(750, 590, w=56, h=72, slant=+14)          # 立的右丿
    g.hbar(390, 900, 470, weight=W_MAIN)            # 立的底横
    g.hbar(480, 810, 330, weight=W_MAIN)            # 日的上横
    g.hbar(480, 810, 190, weight=W_MAIN)            # 日的中横
    g.hbar(480, 810, 60, weight=W_MAIN)             # 日的下横
    g.vbar(530, 12, 378, weight=W_MAIN)
    g.vbar(760, 12, 378, weight=W_MAIN)
    return g


def glyph_retsu() -> Glyph:
    """裂（12 画）：列（歹 4 + 刂 2）+ 衣（6）。

    部件分区：歹 x 118..350 / y 385..818；刂 x 432..648 / y 400..790；
    衣 x 163..877 / y 3..378。
    """
    g = _g("uni88C2", 0x88C2, "裂：列+衣")
    # 歹（4 画）
    g.hbar(90, 340, 770, weight=W_MAIN)             # 歹的一
    g.diag(300, 750, 150, 600, weight=W_SEC)        # 歹的撇
    g.hbar(140, 330, 550, weight=W_MAIN)            # 歹的横撇之横
    g.diag(320, 555, 160, 420, weight=W_SEC)        # 歹的横撇之撇
    g.dot(270, 450, w=52, h=68, slant=-14)          # 歹的点
    # 刂（2 画）
    g.vbar(480, 500, 790, weight=W_MAIN)
    g.vbar(600, 400, 790, weight=W_MAIN)
    # 衣（6 画）
    g.dot(500, 330, w=76, h=96, slant=0)            # 衣的点
    g.hbar(250, 750, 250, weight=W_MAIN)            # 衣的横
    g.diag(395, 240, 195, 45, weight=W_SEC)         # 衣的撇
    g.vbar(500, 30, 240, weight=W_MAIN)             # 衣的竖
    g.diag(560, 240, 850, 40, weight=W_SEC)         # 衣的捺
    return g


def glyph_bin() -> Glyph:
    """敏（11 画）：每（7）+ 攵（4）。

    部件分区：每 x 137..490 / y 272..814；攵 x 518..917 / y 142..811。
    每的中横（422..518）与上横（652..748）之间留 134，容得下一颗点而不封腔：
    点的白口 30 / 28，两侧腔高均 ≥ 24。
    """
    g = _g("uni654F", 0x654F, "敏：每+攵")
    # 每（7 画）
    g.diag(325, 772, 155, 698, weight=W_SEC)        # 每的撇
    g.hbar(210, 450, 700, weight=W_MAIN)            # 每的一
    g.vbar(220, 350, 700, weight=W_MAIN)            # 母的左竖
    g.vbar(410, 400, 700, weight=W_MAIN)            # 母的右竖
    g.hbar(140, 490, 470, weight=W_MAIN)            # 母的中横
    g.dot(300, 584, w=52, h=76, slant=-14)          # 母的上点
    g.dot(315, 300, w=46, h=56, slant=-14)          # 母的下点
    # 攵（4 画）
    g.diag(670, 780, 555, 655, weight=W_SEC)        # 攵的撇
    g.hbar(620, 900, 700, weight=W_MAIN)            # 攵的一
    g.diag(770, 660, 560, 160, weight=W_SEC)        # 攵的长撇
    g.diag(690, 660, 875, 210, weight=W_SEC)        # 攵的捺
    return g


def glyph_tori() -> Glyph:
    """鳥（11 画）：丿（1）+ 白（5）+ 一（1）+ 亅（1）+ 灬（4）。

    部件分区：丿 x 359..496 / y 684..818；白 x 282..838 / y 398..742；
    长横 x 220..900 / y 202..298；亅 x 282..378 / y 60..446；
    灬 x 409..847 / y 50..130。
    """
    g = _g("uni9CE5", 0x9CE5, "鳥：丿+白+一+亅+灬")
    g.diag(470, 780, 385, 722, weight=W_SEC)        # 顶部的撇
    g.hbar(330, 790, 694, weight=W_MAIN)            # 白的上横
    g.hbar(330, 790, 570, weight=W_MAIN)            # 白的中横
    g.hbar(330, 790, 446, weight=W_MAIN)            # 白的下横
    g.vbar(330, 446, 694, weight=W_MAIN)            # 白的左竖
    g.vbar(790, 446, 694, weight=W_MAIN)            # 白的右竖
    g.hbar(220, 900, 250, weight=W_MAIN)            # 长横
    g.vbar(330, 60, 446, weight=W_MAIN)             # 亅
    g.dot(440, 90, w=62, h=80, slant=+14)           # 灬首点（撇形）
    g.dot(570, 90, w=62, h=80, slant=-14)
    g.dot(700, 90, w=62, h=80, slant=-14)
    g.dot(830, 90, w=62, h=80, slant=-14)
    return g


def glyph_jun() -> Glyph:
    """純（10 画）：糸（6）+ 屯（4）。

    部件分区：糸 x 103..377 / y 60..797；屯 x 482..908 / y 182..748。
    糸的两折横白口 28；屯的三竖间距 69（≥60）。
    """
    g = _g("uni7D14", 0x7D14, "純：糸+屯")
    # 糸（6 画）：幺（撇折 ×2 + 点）+ 小（竖 + 两点）
    g.diag(330, 760, 170, 640, weight=W_SEC)        # 幺的撇一
    g.hbar(170, 290, 640, weight=W_SEC)             # 幺的折一
    g.diag(340, 700, 180, 520, weight=W_SEC)        # 幺的撇二
    g.hbar(180, 300, 520, weight=W_SEC)             # 幺的折二
    g.dot(360, 540, w=54, h=70, slant=-14)          # 幺的点
    g.vbar(240, 60, 500, weight=W_MAIN)             # 小 的竖
    g.dot(130, 330, w=54, h=70, slant=-14)          # 小 的左点
    g.dot(350, 330, w=54, h=70, slant=-14)          # 小 的右点
    # 屯（4 画）
    g.hbar(490, 910, 700, weight=W_MAIN)            # 屯的横
    g.vbar(530, 380, 652, weight=W_MAIN)            # 屯的左竖
    g.vbar(695, 230, 700, weight=W_MAIN)            # 屯的中竖
    g.vbar(860, 380, 652, weight=W_MAIN)            # 屯的右竖
    g.hbar(530, 860, 430, weight=W_MAIN)            # 屯的底横
    g.hbar(695, 900, 230, weight=W_MAIN)            # 屯的乚
    return g


def glyph_han() -> Glyph:
    """飯（12 画）：飠（8）+ 反（4）。

    部件分区：飠 x 117..458 / y 72..809；反 x 469..928 / y 195..819。
    飠的框：上横 552..648 / 中横 422..518 / 下横 297..393（白口 34 / 29）。
    """
    g = _g("uni98EF", 0x98EF, "飯：飠+反")
    # 飠（8 画）
    g.diag(270, 770, 145, 675, weight=W_SEC)        # 飠的人·撇
    g.diag(285, 770, 425, 680, weight=W_SEC)        # 飠的人·捺
    g.vbar(210, 300, 600, weight=W_MAIN)            # 飠的左竖
    g.hbar(210, 430, 600, weight=W_MAIN)            # 飠的上横
    g.vbar(410, 300, 600, weight=W_MAIN)            # 飠的右竖
    g.hbar(210, 410, 470, weight=W_MAIN)            # 飠的中横
    g.hbar(210, 430, 345, weight=W_MAIN)            # 飠的下横
    g.vbar(260, 90, 345, weight=W_MAIN)             # 飠的竖钩
    g.hbar(260, 400, 120, weight=W_MAIN)            # 飠的钩
    g.dot(370, 240, w=50, h=66, slant=-14)          # 飠的点
    # 反（4 画）
    g.diag(590, 780, 530, 200, weight=W_SEC)        # 厂的撇
    g.hbar(600, 910, 700, weight=W_MAIN)            # 厂的一
    g.hbar(660, 890, 570, weight=W_MAIN)            # 又的横
    g.diag(880, 585, 660, 230, weight=W_SEC)        # 又的撇
    g.diag(680, 585, 890, 270, weight=W_SEC)        # 又的捺
    return g


def glyph_hai() -> Glyph:
    """排（11 画）：扌（3）+ 非（8）。

    部件分区：扌 x 60..318；非 x 370..930 / y 332..808。
    非两竖白口 64（≥60），三横白口 84。
    """
    g = _g("uni6392", 0x6392, "排：扌+非")
    comp_te(g)
    g.vbar(500, 380, 760, weight=W_MAIN)
    g.vbar(660, 380, 760, weight=W_MAIN)
    g.hbar(390, 500, 760, weight=W_MAIN)
    g.hbar(370, 500, 570, weight=W_MAIN)
    g.hbar(390, 500, 380, weight=W_MAIN)
    g.hbar(660, 910, 760, weight=W_MAIN)
    g.hbar(660, 930, 570, weight=W_MAIN)
    g.hbar(660, 910, 380, weight=W_MAIN)
    return g


def glyph_yu() -> Glyph:
    """裕（12 画）：衤（5）+ 谷（7：八 2 + 人 2 + 口 3）。

    部件分区：衤 x 88..346 / y 120..800；谷 x 430..908 / y 182..816。
    谷的口框高 = 488-182 = 306，内白 114。
    """
    g = _g("uni88D5", 0x88D5, "裕：衤+谷")
    # 衤（5 画）
    g.dot(200, 760, w=72, h=80, slant=0)            # 衤的点
    g.hbar(90, 330, 650, weight=W_MAIN)             # 衤的横
    g.diag(320, 655, 160, 545, weight=W_SEC)        # 衤的撇
    g.vbar(220, 120, 630, weight=W_MAIN)            # 衤的竖
    g.dot(120, 440, w=54, h=70, slant=-14)          # 衤的左点
    g.dot(320, 420, w=54, h=70, slant=-14)          # 衤的右点
    # 谷（7 画）
    g.diag(560, 780, 490, 725, weight=W_SEC)        # 八的撇
    g.diag(810, 780, 880, 725, weight=W_SEC)        # 八的捺
    g.diag(670, 690, 570, 610, weight=W_SEC)        # 人的撇
    g.diag(670, 690, 790, 610, weight=W_SEC)        # 人的捺
    g.hbar(530, 810, 440, weight=W_MAIN)            # 口的上横
    g.hbar(530, 810, 230, weight=W_MAIN)            # 口的下横
    g.vbar(580, 230, 440, weight=W_MAIN)
    g.vbar(760, 230, 440, weight=W_MAIN)
    return g


def glyph_ken() -> Glyph:
    """堅（12 画）：臣（6）+ 又（2）+ 土（3）。

    部件分区：臣 x 102..468 / y 332..748；又 x 529..920 / y 305..668；
    土 x 230..770 / y 32..278。
    """
    g = _g("uni5805", 0x5805, "堅：臣+又+土")
    # 臣（6 画）
    g.vbar(150, 380, 700, weight=W_MAIN)            # 臣的左竖
    g.hbar(150, 440, 700, weight=W_MAIN)            # 臣的上横
    g.vbar(420, 560, 700, weight=W_MAIN)            # 臣的右上竖
    g.hbar(150, 420, 530, weight=W_MAIN)            # 臣的中横
    g.hbar(150, 440, 380, weight=W_MAIN)            # 臣的下横
    # 又（2 画）
    g.hbar(520, 900, 620, weight=W_MAIN)            # 又的横
    g.diag(890, 625, 560, 340, weight=W_SEC)        # 又的撇
    g.diag(560, 630, 880, 340, weight=W_SEC)        # 又的捺
    # 土（3 画）
    g.hbar(350, 650, 230, weight=W_MAIN)            # 土的上横
    g.hbar(230, 770, 80, weight=W_MAIN)             # 土的下横
    g.vbar(500, 80, 230, weight=W_MAIN)             # 土的竖
    return g


def glyph_yaku() -> Glyph:
    """訳（11 画）：言（7）+ 尺（尸 3 + 乀 1）。

    部件分区：言 x 60..390；尺 x 404..928 / y 75..788。
    尸的中横白口 54。
    """
    g = _g("uni8A33", 0x8A33, "訳：言+尺")
    comp_ri(g)
    g.hbar(480, 900, 740, weight=W_MAIN)            # 尸的横
    g.vbar(880, 600, 740, weight=W_MAIN)            # 尸的折竖
    g.hbar(480, 880, 590, weight=W_MAIN)            # 尸的中横
    g.diag(520, 700, 450, 80, weight=W_SEC)         # 尸的撇
    g.diag(620, 520, 890, 250, weight=W_SEC)        # 尺的乀
    return g


def build() -> list[Glyph]:
    return [
        glyph_zhao(),    # 照
        glyph_shu(),     # 酒
        glyph_dou(),     # 堂
        glyph_shibu(),   # 渋
        glyph_gun(),     # 群
        glyph_hi(),      # 悲
        glyph_kiei(),    # 携
        glyph_oku(),     # 奥
        glyph_shin(),    # 診
        glyph_ketsu(),   # 詰
        glyph_taku(),    # 託
        glyph_sei(),     # 晴
        glyph_kake(),    # 掛
        glyph_shin2(),   # 寝
        glyph_an(),      # 暗
        glyph_retsu(),   # 裂
        glyph_bin(),     # 敏
        glyph_tori(),    # 鳥
        glyph_jun(),     # 純
        glyph_han(),     # 飯
        glyph_hai(),     # 排
        glyph_yu(),      # 裕
        glyph_ken(),     # 堅
        glyph_yaku(),    # 訳
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s3-015.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
