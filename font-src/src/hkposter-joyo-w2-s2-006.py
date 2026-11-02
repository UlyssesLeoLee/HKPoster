"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-006。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
* 字面框与繁体汉字完全一致：x 60..940、y 0..820，advance = 1000。
  对齐语义：横画用 h_top / h_at / h_base 分别把「墨迹上缘」对齐 820 / 指定高度 /
  基线 0；竖画用 v_at，端点即墨迹端点（hkbuild 的 vbar 端点就是墨迹端）。
  斜画为「中心线 + 垂直权重」的平行四边形，端点为墨迹端面，因此所有斜画与
  点的端点都内缩到 x 70..920 / y 40..790 区间，保证墨迹不越框。
* 笔画权重四档：主 96 / 次 92 / 细 84 / 点 84。
  笔画少的字（早・伝・好・毎・守・姿）主干用满 96；
  笔画多、拥挤处（两口、三横叠横、門的两半框）局部减到 84–92，
  使竖与竖之间内白 ≥ 60、密排处内白 ≥ 24（GLY-006）。
* 同族观感：同一部件在本批内复用同一套坐标与笔画拆法，只做位置光学校正
  （docs/03 GLY-004）。复用的部件：
    - 亻（例 / 伝 / 佐）→ jin()
    - 扌（担 / 技）→ tehen()
    - 力（助 / 労）→ chi()
    - 央（映 / 英）→ ou()
    - ⻌ 辶（退 / 造 / 追）→ mawari()
    - 日 / 目 / 口 框式部件 → sun() / kuchi()
    - 艹（英 / 若）→ kusanmuri()
* 结构性封闭的字（口・日・目・貝・門・岡・母）内白成洞，墨量率天然偏高，
  按集成方裁定保留真实结构，不为压阈值压成畸形。
* 禁止逐字机械挤压或倾斜：每字按部件分区手工排布，斜画只用于撇/捺/折钩。
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


# ----------------------------------------------------------------------
# 对齐辅助：横画 / 竖画
# ----------------------------------------------------------------------
def h_top(g: Glyph, x1: float, x2: float, weight: float = W_MAIN) -> None:
    """横画：墨迹上缘贴字面框顶 y=820。"""
    g.hbar(x1, x2, 820.0 - weight / 2.0, weight=weight)


def h_base(g: Glyph, x1: float, x2: float, weight: float = W_MAIN) -> None:
    """横画：墨迹下缘贴基线 y=0。"""
    g.hbar(x1, x2, weight / 2.0, weight=weight)


def h_at(g: Glyph, x1: float, x2: float, y_top: float, weight: float = W_MAIN) -> None:
    """横画：墨迹上缘对齐 y_top。"""
    g.hbar(x1, x2, y_top - weight / 2.0, weight=weight)


def v_at(g: Glyph, x: float, y1: float, y2: float, weight: float = W_MAIN) -> None:
    """竖画：墨迹上下端点即 y1 / y2。"""
    g.vbar(x, y1, y2, weight=weight)


# ----------------------------------------------------------------------
# 复用部件
# ----------------------------------------------------------------------
def kuchi(g: Glyph, xl: float, xr: float, yb: float, yt: float, weight: float = W_SEC) -> None:
    """口：外框 xl..xr / yb..yt（四边闭合，内白自动成洞）。"""
    hw = weight / 2.0
    v_at(g, xl + hw, yt, yb, weight)
    v_at(g, xr - hw, yt, yb, weight)
    h_at(g, xl, xr, yt, weight)
    h_at(g, xl, xr, yb + weight, weight)


def sun(g: Glyph, xl: float, xr: float, yb: float, yt: float,
        weight: float = W_SEC, inner: int = 1) -> None:
    """日（inner=1）/ 目（inner=2）：外框 + 等距内横，内白上下分区。"""
    hw = weight / 2.0
    v_at(g, xl + hw, yt, yb, weight)
    v_at(g, xr - hw, yt, yb, weight)
    h_at(g, xl, xr, yt, weight)
    h_at(g, xl, xr, yb + weight, weight)
    if inner:
        ih = weight - 4
        space = (yt - weight) - (yb + weight)
        comp = (space - inner * ih) / (inner + 1)
        y = yt - weight
        for _ in range(inner):
            y -= comp
            h_at(g, xl + weight, xr - weight, y, ih)
            y -= ih


def jin(g: Glyph) -> None:
    """亻：撇 + 竖。左部固定 x 60..300（例 / 伝 / 佐 共用）。"""
    g.diag(300, 795, 150, 440, weight=W_SEC)
    v_at(g, 205, 470, 0, W_SEC)


def tehen(g: Glyph) -> None:
    """扌：一 + 竖钩 + 提。左部固定 x 60..310（担 / 技 共用）。"""
    h_at(g, 60, 310, 580, W_SEC)
    v_at(g, 180, 820, 40, W_SEC)
    g.diag(180, 50, 110, 110, weight=W_THIN)   # 竖钩
    g.diag(90, 320, 310, 430, weight=W_SEC)     # 提


def chi(g: Glyph, xl: float, xr: float, y_top: float, y_bot: float,
        w_pie: float = W_SEC) -> None:
    """力：横折钩（横 + 竖 + 钩）+ 撇（助 / 労 共用同一拆法）。"""
    hw = W_MAIN / 2.0
    h_at(g, xl, xr, y_top, W_MAIN)
    v_at(g, xr - hw, y_top, y_bot + 10, W_MAIN)
    g.diag(xr - hw, y_bot + 10, xr - hw - 90, y_bot + 80, weight=W_THIN)   # 钩
    g.diag(xl + 140, y_top - 30, xl + 10, y_bot, weight=w_pie)             # 撇


def ou(g: Glyph, x0: float, y_top: float = 560, y_low: float = 276) -> None:
    """央：上「冂 + 中心竖」（冂 的两竖只到腰、不封底），下「大的一 + 撇捺」。
    宽度 480，左缘 x0（映 / 英 共用）。y_low = 「一」的墨迹上缘。"""
    h_at(g, x0 + 40, x0 + 440, y_top, W_MAIN)          # 冂 的横
    v_at(g, x0 + 230, y_top, y_low - 36, W_MAIN)        # 中心竖（贯通到「一」）
    v_at(g, x0 + 88, y_top, y_low + 54, W_SEC)          # 冂 的左竖（短）
    v_at(g, x0 + 392, y_top, y_low + 54, W_SEC)         # 冂 的右竖（短）
    h_at(g, x0 + 20, x0 + 460, y_low, W_MAIN)           # 大 的「一」
    g.diag(x0 + 200, y_low - 16, x0 + 20, y_low - 216, weight=W_SEC)    # 撇
    g.diag(x0 + 380, y_low - 16, x0 + 450, y_low - 216, weight=W_SEC)   # 捺


def mawari(g: Glyph) -> None:
    """⻌（辶）：点 + 折撇 + 平捺（底部长横）。三字共用同一坐标。"""
    g.dot(140, 700, w=W_DOT, h=110, slant=-14)
    g.diag(130, 400, 430, 180, weight=W_SEC)
    h_at(g, 400, 940, 160, W_SEC)


def hitsuji(g: Glyph, x0: float, y_top: float, w: float = W_SEC) -> None:
    """彡：三道撇。"""
    g.diag(x0 + 280, y_top, x0 + 40, y_top - 110, weight=w)
    g.diag(x0 + 280, y_top - 240, x0 + 40, y_top - 350, weight=w)
    g.diag(x0 + 280, y_top - 490, x0 + 40, y_top - 600, weight=w)


def kusanmuri(g: Glyph) -> None:
    """艹：横 + 两竖（英 / 若 共用）。横画用细档，避免整字过闷。"""
    h_at(g, 120, 880, 700, W_THIN)
    v_at(g, 330, 820, 540, W_THIN)
    v_at(g, 670, 820, 540, W_THIN)


# ----------------------------------------------------------------------
# 32 个字形
# ----------------------------------------------------------------------
def g_zhu() -> Glyph:
    """助 U+52A9（7画）⿰且力
    且(5)：左竖 x148 / 右竖 x342 / 上横 / 中横 / 下横（下横比框宽，左出 42）。
    力(2)：横折钩 + 撇（chi）。
    部件分区：且 x 60..390；力 x 430..940。
    """
    g = Glyph("uni52A9", advance=1000, unicode=0x52A9,
              note="助：7 画⿰且力：且(5) + 力(2)")
    v_at(g, 148, 820, 0, W_THIN)
    v_at(g, 342, 820, 0, W_THIN)
    h_top(g, 102, 388, W_THIN)
    h_at(g, 148, 342, 440, W_THIN)
    h_base(g, 60, 388, W_THIN)
    chi(g, 460, 892, 820, 40, w_pie=W_THIN)
    return g


def g_rou() -> Glyph:
    """労 U+52B4（7画）⿱⺍冖力
    ⺍(3)：左短撇 / 中短撇 / 右长撇（ツ 的三笔）。
    冖(2)：左点 + 横钩。力(2)：chi()。
    分区：⺍ y 650..790；冖 y 560..730；力 y 40..520。
    """
    g = Glyph("uni52B4", advance=1000, unicode=0x52B4,
              note="労：7 画⿱⺍冖力：ツ(3) + 冖(2) + 力(2)")
    g.diag(250, 790, 205, 700, weight=W_SEC)
    g.diag(470, 790, 425, 700, weight=W_SEC)
    g.diag(870, 770, 700, 700, weight=W_SEC)
    v_at(g, 150, 730, 640, W_SEC)          # 冖 的左点
    h_at(g, 120, 900, 640, W_MAIN)         # 冖 的横
    v_at(g, 856, 640, 560, W_SEC)          # 冖 的右钩
    chi(g, 340, 892, 520, 40)
    return g


def g_rei() -> Glyph:
    """例 U+4F8B（8画）⿰亻列
    亻(2)：jin()；歹(4)：一 + 撇 + 横撇 + 点；刂(2)：短竖 + 长竖带钩。
    分区：亻 x 60..300；歹 x 330..640；刂 x 660..940。
    """
    g = Glyph("uni4F8B", advance=1000, unicode=0x4F8B,
              note="例：8 画⿰亻歹刂：亻(2) + 歹(4) + 刂(2)")
    jin(g)
    h_at(g, 370, 640, 820, W_MAIN)         # 歹 的横
    g.diag(480, 740, 370, 470, weight=W_MAIN)
    h_at(g, 440, 630, 690, W_SEC)          # 歹 的横撇
    g.diag(630, 690, 540, 430, weight=W_SEC)
    g.dot(450, 520, w=W_DOT, h=88, slant=-14)
    v_at(g, 700, 700, 220, W_SEC)          # 刂 的短竖
    v_at(g, 892, 820, 60, W_MAIN)          # 刂 的长竖
    g.diag(892, 70, 800, 140, weight=W_SEC)
    return g


def g_sou() -> Glyph:
    """早 U+65E9（6画）⿱日十
    日(4)：sun() 外框 x 290..710 / y 400..820；十(2)：横 x 160..840 + 竖 x500。
    笔画少的字用满 96 权重。
    """
    g = Glyph("uni65E9", advance=1000, unicode=0x65E9,
              note="早：6 画⿱日十：日(4) + 十(2)")
    sun(g, 290, 710, 400, 820, W_MAIN, inner=1)
    h_at(g, 140, 860, 340, W_MAIN)
    v_at(g, 500, 380, 0, W_MAIN)
    return g


def g_ei() -> Glyph:
    """映 U+6620（9画）⿰日央
    日(4)：左部外框 x 60..360 / y 400..820；央(5)：ou() 落在 x0=430。
    """
    g = Glyph("uni6620", advance=1000, unicode=0x6620,
              note="映：9 画⿰日央：日(4) + 央(5)")
    sun(g, 60, 360, 400, 820, W_SEC, inner=1)
    ou(g, 430, 560, 276)
    return g


def g_gen() -> Glyph:
    """限 U+9650（9画）⿰阝艮
    阝(2)：竖 + 旗形（横 + 折）；艮(6)：目形上部 + 提 + 撇 + 捺。
    分区：阝 x 60..320；艮 x 330..940。
    """
    g = Glyph("uni9650", advance=1000, unicode=0x9650,
              note="限：9 画⿰阝艮：阝(2) + 艮(6)")
    v_at(g, 110, 820, 0, W_THIN)             # 阝 的竖
    h_at(g, 64, 300, 820, W_THIN)           # 阝 的旗
    g.diag(300, 780, 200, 660, weight=W_THIN)
    g.diag(200, 660, 280, 560, weight=W_THIN)
    sun(g, 344, 850, 380, 820, W_THIN, inner=2)   # 艮 上部（目形）
    h_at(g, 436, 840, 354, W_THIN)          # 艮 的提
    g.diag(470, 310, 370, 110, weight=W_THIN)   # 艮 的撇
    g.diag(790, 310, 870, 110, weight=W_THIN)   # 艮 的捺
    return g


def g_tsui() -> Glyph:
    """追 U+8FFD（8画）⿻⻌𠂤
    ⻌(2)：mawari()；𠂤(6)：撇 + 目形竖框。
    分区：𠂤 x 480..780 / y 216..790；⻌ 占左侧与底部。
    """
    g = Glyph("uni8FFD", advance=1000, unicode=0x8FFD,
              note="追：8 画⿻⻌𠂤：⻌(2) + 𠂤(6)")
    mawari(g)
    g.diag(590, 780, 500, 690, weight=W_SEC)
    sun(g, 480, 780, 240, 700, W_THIN, inner=2)
    return g


def g_den() -> Glyph:
    """伝 U+4F1D（6画）⿰亻云
    亻(2)：jin()；云(4)：二 + 厶（折 + 横 + 点）。
    分区：亻 x 60..300；云 x 340..940。
    """
    g = Glyph("uni4F1D", advance=1000, unicode=0x4F1D,
              note="伝：6 画⿰亻云：亻(2) + 云(4)")
    jin(g)
    h_at(g, 420, 900, 720, W_MAIN)
    h_at(g, 370, 860, 570, W_MAIN)
    g.diag(540, 470, 450, 180, weight=W_SEC)
    h_at(g, 450, 790, 180, W_SEC)
    g.dot(700, 300, w=W_DOT, h=104, slant=-14)
    return g


def g_kei() -> Glyph:
    """形 U+5F62（7画）⿰开彡
    开(4)：二 + 丿 + 丨；彡(3)：三道撇。
    分区：开 x 60..500；彡 x 640..920。
    """
    g = Glyph("uni5F62", advance=1000, unicode=0x5F62,
              note="形：7 画⿰开彡：开(4) + 彡(3)")
    h_top(g, 80, 480, W_MAIN)
    h_at(g, 60, 500, 620, W_MAIN)
    v_at(g, 300, 800, 0, W_MAIN)
    g.diag(230, 620, 110, 40, weight=W_MAIN)
    hitsuji(g, 600, 770, W_SEC)
    return g


def g_ou() -> Glyph:
    """欧 U+6B27（8画）⿰区欠
    区(4)：匚（横 + 竖折）+ 乂；欠(4)：撇 + 横撇 + 人。
    分区：区 x 60..430；欠 x 480..940。
    """
    g = Glyph("uni6B27", advance=1000, unicode=0x6B27,
              note="欧：8 画⿰区欠：区(4) + 欠(4)")
    h_top(g, 60, 430, W_MAIN)
    v_at(g, 108, 820, 0, W_MAIN)
    h_base(g, 60, 430, W_MAIN)
    g.diag(230, 640, 360, 200, weight=W_SEC)
    g.diag(360, 640, 230, 200, weight=W_SEC)
    g.diag(560, 790, 480, 680, weight=W_SEC)
    h_at(g, 520, 810, 680, W_SEC)
    g.diag(800, 660, 700, 540, weight=W_SEC)
    g.diag(700, 540, 530, 60, weight=W_MAIN)
    g.diag(700, 520, 880, 60, weight=W_MAIN)
    return g


def g_tan() -> Glyph:
    """担 U+62C5（8画）⿰扌旦
    扌(3)：tehen()；旦(5)：日 + 底横。
    分区：扌 x 60..310；旦 x 340..940。
    """
    g = Glyph("uni62C5", advance=1000, unicode=0x62C5,
              note="担：8 画⿰扌旦：扌(3) + 旦(5)")
    tehen(g)
    sun(g, 420, 860, 400, 730, W_SEC, inner=1)
    h_base(g, 340, 940, W_MAIN)
    return g


def g_ko() -> Glyph:
    """好 U+597D（6画）⿰女子
    女(3)：撇点 + 撇 + 横；子(3)：横撇 + 竖钩 + 横。
    分区：女 x 60..440；子 x 500..940。
    """
    g = Glyph("uni597D", advance=1000, unicode=0x597D,
              note="好：6 画⿰女子：女(3) + 子(3)")
    g.diag(260, 790, 130, 430, weight=W_MAIN)
    g.diag(130, 430, 380, 70, weight=W_MAIN)
    g.diag(400, 780, 180, 60, weight=W_MAIN)
    h_at(g, 60, 440, 330, W_MAIN)
    h_top(g, 520, 900, W_MAIN)
    g.diag(880, 780, 680, 650, weight=W_MAIN)
    v_at(g, 700, 700, 60, W_MAIN)
    g.diag(700, 70, 610, 130, weight=W_SEC)
    h_at(g, 500, 920, 430, W_MAIN)
    return g


def g_tai() -> Glyph:
    """退 U+9000（8画）⿻艮辶
    艮(6)：目形上部 + 提 + 撇 + 捺；辶(2)：mawari()。
    分区：艮 x 330..940 / y 272..820；辶 占左下与底。
    """
    g = Glyph("uni9000", advance=1000, unicode=0x9000,
              note="退：8 画⿻艮辶：艮(6) + 辶(2)")
    sun(g, 334, 850, 400, 820, W_THIN, inner=2)
    h_at(g, 426, 840, 374, W_THIN)
    g.diag(470, 330, 400, 230, weight=W_THIN)
    g.diag(800, 330, 875, 230, weight=W_THIN)
    mawari(g)
    return g


def g_zou() -> Glyph:
    """造 U+9020（9画）⿻告辶
    告(7)：⺧（丿 + 一 + 丨 + 一）+ 口；辶(2)：mawari()。
    分区：告 x 320..920 / y 192..820；辶 占左下与底。
    """
    g = Glyph("uni9020", advance=1000, unicode=0x9020,
              note="造：9 画⿻告辶：告(7) + 辶(2)")
    g.diag(430, 780, 340, 700, weight=W_SEC)
    h_at(g, 360, 880, 788, W_THIN)
    v_at(g, 600, 788, 590, W_THIN)
    h_at(g, 320, 920, 678, W_THIN)
    kuchi(g, 380, 880, 192, 500, W_SEC)
    mawari(g)
    return g


def g_ei_boku() -> Glyph:
    """英 U+82F1（8画）⿱艹央
    艹(3)：kusanmuri()；央(5)：ou() 落在 x0=250。
    """
    g = Glyph("uni82F1", advance=1000, unicode=0x82F1,
              note="英：8 画⿱艹央：艹(3) + 央(5)")
    kusanmuri(g)
    ou(g, 250, 560, 276)
    return g


def g_gi() -> Glyph:
    """技 U+6280（7画）⿰扌支
    扌(3)：tehen()；支(4)：十 + 又（横撇 + 捺）。
    分区：扌 x 60..310；支 x 340..940。
    """
    g = Glyph("uni6280", advance=1000, unicode=0x6280,
              note="技：7 画⿰扌支：扌(3) + 支(4)")
    tehen(g)
    h_at(g, 380, 900, 700, W_MAIN)
    v_at(g, 640, 790, 520, W_MAIN)
    h_at(g, 420, 880, 490, W_MAIN)
    g.diag(860, 490, 430, 60, weight=W_MAIN)
    g.diag(460, 470, 890, 60, weight=W_MAIN)
    return g


def g_tei() -> Glyph:
    """低 U+4F4E（7画）⿰亻氐
    亻(2)：jin()；氐(5)：丿 + 一 + 丨 + 撇 + 底横。
    分区：亻 x 60..300；氐 x 330..940。
    """
    g = Glyph("uni4F4E", advance=1000, unicode=0x4F4E,
              note="低：7 画⿰亻氐：亻(2) + 氐(5)")
    jin(g)
    g.diag(560, 780, 420, 690, weight=W_SEC)
    h_at(g, 430, 870, 680, W_MAIN)
    v_at(g, 540, 680, 180, W_MAIN)
    g.diag(870, 620, 560, 220, weight=W_MAIN)
    h_at(g, 420, 620, 120, W_SEC)
    return g


def g_mai() -> Glyph:
    """毎 U+6BCE（6画）⿱𠂉母
    𠂉(2)：撇 + 横；母(4)：框 + 中横（伸出框外）+ 两点。
    分区：𠂉 y 690..790；母 y 100..600。
    """
    g = Glyph("uni6BCE", advance=1000, unicode=0x6BCE,
              note="毎：6 画⿱𠂉母：𠂉(2) + 母(4)")
    g.diag(370, 780, 280, 700, weight=W_THIN)
    h_at(g, 290, 790, 720, W_THIN)
    sun(g, 240, 760, 0, 600, W_THIN, inner=0)
    h_at(g, 140, 860, 342, W_THIN)
    g.dot(390, 429, w=76, h=64, slant=20)
    g.dot(600, 171, w=76, h=64, slant=20)
    return g


def g_i() -> Glyph:
    """医 U+533B（7画）⿵匚矢
    匚(2)：横 + 竖折；矢(5)：丿 + 一 + 大（一 + 撇 + 捺）。
    分区：匚 x 60..400；矢 x 190..840。
    """
    g = Glyph("uni533B", advance=1000, unicode=0x533B,
              note="医：7 画⿵匚矢：匚(2) + 矢(5)")
    h_top(g, 60, 400, W_MAIN)
    v_at(g, 108, 820, 0, W_MAIN)
    h_base(g, 60, 400, W_MAIN)
    g.diag(300, 790, 230, 660, weight=W_SEC)
    h_at(g, 270, 660, 700, W_SEC)
    h_at(g, 200, 800, 480, W_MAIN)
    g.diag(460, 480, 240, 60, weight=W_MAIN)
    g.diag(500, 480, 800, 60, weight=W_MAIN)
    return g


def g_shi() -> Glyph:
    """姿 U+59FF（9画）⿱次女
    次(6)：冫（点 + 提）+ 欠（撇 + 横撇 + 人）；女(3)：撇点 + 撇 + 横。
    分区：次 y 430..790；女 y 0..380。
    """
    g = Glyph("uni59FF", advance=1000, unicode=0x59FF,
              note="姿：9 画⿱次女：次(6) + 女(3)")
    g.dot(150, 700, w=W_DOT, h=100, slant=-14)
    g.diag(90, 500, 240, 570, weight=W_SEC)
    g.diag(430, 780, 350, 690, weight=W_SEC)
    h_at(g, 390, 690, 690, W_SEC)
    g.diag(690, 670, 600, 560, weight=W_SEC)
    g.diag(590, 520, 470, 430, weight=W_SEC)
    g.diag(590, 500, 740, 430, weight=W_SEC)
    g.diag(280, 360, 190, 140, weight=W_SEC)
    g.diag(190, 140, 370, 60, weight=W_SEC)
    g.diag(400, 350, 210, 60, weight=W_SEC)
    h_at(g, 120, 800, 260, W_MAIN)
    return g


def g_mi() -> Glyph:
    """味 U+5473（8画）⿰口未
    口(3)：kuchi()；未(5)：二 + 丨 + 撇 + 捺。
    分区：口 x 60..320 / y 292..820；未 x 400..920。
    """
    g = Glyph("uni5473", advance=1000, unicode=0x5473,
              note="味：8 画⿰口未：口(3) + 未(5)")
    kuchi(g, 60, 320, 292, 820, W_THIN)
    h_at(g, 480, 860, 720, W_SEC)
    h_at(g, 400, 920, 580, W_MAIN)
    v_at(g, 660, 720, 0, W_MAIN)
    g.diag(640, 540, 420, 40, weight=W_MAIN)
    g.diag(670, 540, 890, 50, weight=W_MAIN)
    return g


def g_fu() -> Glyph:
    """負 U+8CA0（9画）⿱⺈貝
    ⺈(2)：撇 + 横撇；貝(7)：目形 + 八。
    分区：⺈ y 600..790；貝 x 200..800 / y 0..620。
    2026-10-31 回修：⺈的横原在墨迹 608..700，与貝上横（536..620）白口 −12；
    横上移到墨迹 644..736（与横撇起笔 690 接上）→ 白口 24。
    参照 M PLUS 1p Black「負」实测：貝部 3 个腔，腔高 34、宽 440。
    """
    g = Glyph("uni8CA0", advance=1000, unicode=0x8CA0,
              note="負：9 画⿱⺈貝：⺈(2) + 貝(7)")
    g.diag(450, 780, 350, 690, weight=W_SEC)
    h_at(g, 360, 740, 736, W_SEC)
    g.diag(730, 690, 640, 600, weight=W_SEC)
    sun(g, 200, 800, 72, 620, W_THIN, inner=2)
    g.diag(430, 160, 280, 60, weight=W_MAIN)
    g.diag(570, 160, 720, 60, weight=W_MAIN)
    return g


def g_mon() -> Glyph:
    """門 U+9580（8画）
    左右两半各 4 画：外竖 + 横折（横 + 内竖）+ 两内横。
    分区：左半 x 60..400；右半 x 600..940；中间留 200 通气。
    """
    g = Glyph("uni9580", advance=1000, unicode=0x9580,
              note="門：8 画：左右各4画（丨 + 横折 + 二横）")
    v_at(g, 108, 820, 0, W_SEC)
    h_top(g, 60, 400, W_SEC)
    v_at(g, 352, 760, 280, W_THIN)
    h_at(g, 156, 352, 600, W_THIN)
    h_at(g, 156, 352, 400, W_THIN)
    v_at(g, 892, 820, 0, W_SEC)
    h_top(g, 600, 940, W_SEC)
    v_at(g, 648, 760, 280, W_THIN)
    h_at(g, 648, 844, 600, W_THIN)
    h_at(g, 648, 844, 400, W_THIN)
    return g


def g_mori() -> Glyph:
    """守 U+5B88（6画）⿱宀寸
    宀(3)：点 + 左点 + 横钩；寸(3)：横 + 竖钩 + 点。
    分区：宀 y 628..790；寸 y 70..620。
    """
    g = Glyph("uni5B88", advance=1000, unicode=0x5B88,
              note="守：6 画⿱宀寸：宀(3) + 寸(3)")
    g.dot(500, 770, w=W_DOT, h=96, slant=0)
    v_at(g, 160, 790, 720, W_SEC)
    h_at(g, 140, 880, 720, W_MAIN)
    v_at(g, 836, 720, 640, W_SEC)
    h_at(g, 220, 900, 560, W_MAIN)
    v_at(g, 700, 620, 60, W_MAIN)
    g.diag(700, 70, 610, 130, weight=W_SEC)
    g.dot(430, 340, w=W_DOT, h=104, slant=-14)
    return g


def g_waku() -> Glyph:
    """若 U+82E5（8画）⿱艹右
    艹(3)：kusanmuri()；右(5)：𠂇（丿 + 一）+ 口。
    分区：艹 y 540..820；右 x 190..880 / y 0..560。
    """
    g = Glyph("uni82E5", advance=1000, unicode=0x82E5,
              note="若：8 画⿱艹右：艹(3) + 右(5)")
    kusanmuri(g)
    h_at(g, 240, 880, 560, W_THIN)
    g.diag(380, 540, 230, 260, weight=W_SEC)
    kuchi(g, 380, 860, 0, 440, W_SEC)
    return g


def g_bi() -> Glyph:
    """美 U+7F8E（9画）⿱羊大
    羊(6)：丷 + 三横 + 丨；大(3)：一 + 撇 + 捺。
    分区：羊 y 340..800；大 y 60..340。
    """
    g = Glyph("uni7F8E", advance=1000, unicode=0x7F8E,
              note="美：9 画⿱羊大：羊(6) + 大(3)")
    g.dot(340, 770, w=W_DOT, h=92, slant=-14)
    g.dot(660, 770, w=W_DOT, h=92, slant=14)
    h_at(g, 290, 710, 720, W_SEC)
    h_at(g, 270, 730, 600, W_SEC)
    h_at(g, 250, 750, 480, W_SEC)
    v_at(g, 500, 800, 340, W_MAIN)
    h_at(g, 220, 780, 340, W_MAIN)
    g.diag(480, 340, 230, 60, weight=W_MAIN)
    g.diag(520, 340, 790, 60, weight=W_MAIN)
    return g


def g_oka() -> Glyph:
    """岡 U+5CA1（8画）⿵冂丷一山
    冂(2)：横 + 两竖；内部：丷(2) + 一(1) + 山(3)。
    分区：冂 x 60..940；内部 x 284..716 / y 92..700。
    """
    g = Glyph("uni5CA1", advance=1000, unicode=0x5CA1,
              note="岡：8 画⿵冂(丷一山)：冂(2) + 丷(2) + 一(1) + 山(3)")
    h_top(g, 60, 940, W_MAIN)
    v_at(g, 108, 820, 0, W_SEC)
    v_at(g, 892, 820, 0, W_SEC)
    g.dot(350, 700, w=W_DOT, h=92, slant=0)
    g.dot(650, 700, w=W_DOT, h=92, slant=0)
    h_at(g, 300, 700, 560, W_SEC)
    v_at(g, 500, 470, 92, W_SEC)
    v_at(g, 330, 370, 92, W_SEC)
    v_at(g, 670, 370, 92, W_SEC)
    h_base(g, 284, 716, W_SEC)
    return g


def g_inochi() -> Glyph:
    """命 U+547D（8画）⿱人一叩
    人(2)：撇 + 捺；一(1)；叩(5)：口(3) + 卩(2)。
    分区：人 y 620..780；一 y 488..580；叩 x 180..760 / y 12..470。
    """
    g = Glyph("uni547D", advance=1000, unicode=0x547D,
              note="命：8 画⿱人一叩：人(2) + 一(1) + 口(3) + 卩(2)")
    g.diag(500, 780, 290, 620, weight=W_MAIN)
    g.diag(500, 780, 710, 620, weight=W_MAIN)
    h_at(g, 280, 720, 580, W_MAIN)
    kuchi(g, 180, 450, 12, 450, W_SEC)
    v_at(g, 560, 470, 100, W_MAIN)
    h_at(g, 514, 760, 470, W_MAIN)
    v_at(g, 712, 470, 370, W_SEC)
    return g


def g_kan() -> Glyph:
    """含 U+542B（7画）⿱今口
    今(4)：人(2) + 丶 + 横撇；口(3)：kuchi()。
    分区：今 y 430..780；口 x 280..720 / y 0..380。
    """
    g = Glyph("uni542B", advance=1000, unicode=0x542B,
              note="含：7 画⿱今口：今(4) + 口(3)")
    g.diag(500, 775, 300, 650, weight=W_SEC)
    g.diag(500, 775, 700, 650, weight=W_SEC)
    g.dot(500, 590, w=W_DOT, h=96, slant=0)
    h_at(g, 360, 660, 520, W_SEC)
    g.diag(650, 510, 575, 450, weight=W_SEC)
    kuchi(g, 280, 720, 0, 380, W_SEC)
    return g


def g_matsu() -> Glyph:
    """松 U+677E（8画）⿰木公
    木(4)：一 + 丨 + 撇 + 捺；公(4)：八(2) + 厶（折 + 横 + 点）。
    分区：木 x 60..430；公 x 460..940。
    """
    g = Glyph("uni677E", advance=1000, unicode=0x677E,
              note="松：8 画⿰木公：木(4) + 公(4)")
    h_at(g, 60, 430, 620, W_MAIN)
    v_at(g, 240, 820, 0, W_MAIN)
    g.diag(240, 580, 120, 60, weight=W_MAIN)
    g.diag(250, 580, 410, 60, weight=W_MAIN)
    g.diag(610, 790, 480, 620, weight=W_SEC)
    g.diag(760, 790, 900, 620, weight=W_SEC)
    g.diag(650, 520, 550, 200, weight=W_SEC)
    h_at(g, 550, 840, 200, W_SEC)
    g.dot(760, 320, w=W_DOT, h=100, slant=-14)
    return g


def g_hi() -> Glyph:
    """非 U+975E（8画）
    两竖 + 六横：左右各三横，上横向外挑，中下横在中间连成通栏。
    分区：左竖 x390、右竖 x610；通栏 x 120..880。
    """
    g = Glyph("uni975E", advance=1000, unicode=0x975E,
              note="非：8 画：两竖 + 左右各三横")
    v_at(g, 390, 820, 0, W_MAIN)
    v_at(g, 610, 820, 0, W_MAIN)
    h_at(g, 120, 438, 700, W_SEC)
    h_at(g, 562, 880, 700, W_SEC)
    h_at(g, 390, 610, 460, W_SEC)
    h_at(g, 390, 610, 220, W_SEC)
    return g


def g_sa() -> Glyph:
    """佐 U+4F50（7画）⿰亻左
    亻(2)：jin()；左(5)：𠂇（丿 + 一）+ 工（一 + 丨 + 一）。
    分区：亻 x 60..300；左 x 310..940。
    """
    g = Glyph("uni4F50", advance=1000, unicode=0x4F50,
              note="佐：7 画⿰亻左：亻(2) + 左(5)")
    jin(g)
    h_top(g, 400, 900, W_MAIN)
    g.diag(470, 790, 350, 580, weight=W_MAIN)
    h_at(g, 390, 900, 520, W_MAIN)
    v_at(g, 640, 520, 92, W_MAIN)
    h_base(g, 360, 940, W_MAIN)
    return g


def build() -> list[Glyph]:
    return [
        g_zhu(),        # 助 U+52A9
        g_rou(),        # 労 U+52B4
        g_rei(),        # 例 U+4F8B
        g_sou(),        # 早 U+65E9
        g_ei(),         # 映 U+6620
        g_gen(),        # 限 U+9650
        g_tsui(),       # 追 U+8FFD
        g_den(),        # 伝 U+4F1D
        g_kei(),        # 形 U+5F62
        g_ou(),         # 欧 U+6B27
        g_tan(),        # 担 U+62C5
        g_ko(),         # 好 U+597D
        g_tai(),        # 退 U+9000
        g_zou(),        # 造 U+9020
        g_ei_boku(),    # 英 U+82F1
        g_gi(),         # 技 U+6280
        g_tei(),        # 低 U+4F4E
        g_mai(),        # 毎 U+6BCE
        g_i(),          # 医 U+533B
        g_shi(),        # 姿 U+59FF
        g_mi(),         # 味 U+5473
        g_fu(),         # 負 U+8CA0
        g_mon(),        # 門 U+9580
        g_mori(),       # 守 U+5B88
        g_waku(),       # 若 U+82E5
        g_bi(),         # 美 U+7F8E
        g_oka(),        # 岡 U+5CA1
        g_inochi(),     # 命 U+547D
        g_kan(),        # 含 U+542B
        g_matsu(),      # 松 U+677E
        g_hi(),         # 非 U+975E
        g_sa(),         # 佐 U+4F50
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-006.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
