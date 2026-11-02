"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s3-004。

本批 24 字，笔画范围 10–12，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
* 字面框：advance 1000；墨迹落在冻结框 x 60..940 / y 0..820
  （design-params.json 的 grid.cjk_body_*）。汉字按方形字面排布：
  左右结构左半约 60..380、右半约 430..940；上下结构通栏 90..910。
* 权重：主 96 / 次 92 / 细 84 / 点 84（design-params.json weights.cjk，与繁体同档）。
  笔画少的字（展/配/害）用 W_MAIN 保重量，笔画多的字（裁/費/備/割）在横画上
  局部收到 W_THIN，批内墨量率向同档中位数靠拢（check_glyphs 的 ±35% 口径）。
* 端点：横竖撇捺一律平切硬边；点与短撇用斜切平行四边形（签名）。
  slant 只用工程档位 {-14, 0, 14, 26}（check_stroke_angles.py: ALLOWED_SLANT）。
  -14 = 「\」右下方向的点（丶），+14 = 「/」左下方向的点（丿），
  26 = 短撇（氵的上点），0 = 竖点（亠/宀的点）。
* 同部件批内复用同一套坐标与画法（GLY-004）：氵 沿用 Wave 0「港」的坐标与
  slant=26；見（規/視）、刂（割/副）、口（常/営/害）、米（料/番/断）、
  十（裁）、丰+口（害/割）都走同一套部件函数或同一套坐标；
  用（補/備）走同一套画法，宽度只按左右空间做光学调整。
* 笔画角度一律照标准骨架，未改任何一条笔画的方向或斜率；只调重量档位、
  端点处理与部件落位。
"""

from __future__ import annotations

import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, write_ufo  # noqa: E402

# ---- 冻结权重（日本語漢字：主 96 / 次 92 / 细 84 / 点 84）----
W_MAIN = 96
W_SEC = 92
W_THIN = 84
W_DOT = 84
W_LIGHT = 76  # 局部减重（GLY-001 小空腔）

# ---- 点/短撇的斜切档 ----
# 直接写字面量（不写常量名），check_stroke_angles.py 才能在 AST 里核到每一处 slant：
#   -14  丶：右下方向的点（辶的点/厶的点/寸的点/丷左/求的点/八的右脚）
#    14  丿：左下方向的点（丷右/小右点/八的左脚）
#    26  短撇（氵的上点与下点）
#     0  竖点（亠的点、宀的点）


# ======================================================================
# 共用部件（批内同部件同坐标，GLY-004）
# ======================================================================
def part_sanzui(g: Glyph) -> None:
    """氵：与 Wave 0「港」完全同坐标、同 slant（GLY-004 同部件复用）。"""
    g.dot(158, 700, w=94, h=126, slant=26)  # 氵的上点（短撇）
    g.dot(150, 468, w=94, h=126, slant=26)  # 氵的下点（短撇）
    g.diag(70, 140, 248, 308, weight=W_SEC)  # 氵的提


def part_miru(g: Glyph) -> None:
    """見（規/視 共用）：目 + 儿。x 560..880，上框 740，三横 620/490/360。"""
    g.vbar(560, 740, 360, weight=W_THIN)  # 見的左竖
    g.hbar(560, 880, 740, weight=W_THIN)  # 見的上横
    g.vbar(880, 740, 360, weight=W_THIN)  # 見的右竖
    g.hbar(560, 880, 620, weight=W_THIN)  # 見的第一横
    g.hbar(560, 880, 490, weight=W_THIN)  # 見的第二横
    g.hbar(560, 880, 360, weight=W_THIN)  # 見的第三横（目底）
    g.diag(650, 360, 545, 60, weight=W_SEC)  # 兒的撇
    g.vbar(800, 360, 80, weight=W_SEC)  # 兒的竖弯钩竖
    g.hbar(800, 930, 80, weight=W_THIN)  # 兒的竖弯钩底


def part_rittou(g: Glyph, x_short: int, x_long: int, y_top: int, y_mid: int) -> None:
    """刂：左短竖 + 右竖钩。"""
    g.vbar(x_short, y_top, y_mid, weight=W_THIN)  # 刂的短竖
    g.vbar(x_long, y_top, 60, weight=W_SEC)  # 刂的长竖
    g.diag(x_long, 60, x_long - 55, 125, weight=W_THIN)  # 刂的钩


def part_kuchi(g: Glyph, x1: int, x2: int, y_top: int, y_bot: int, w: int = W_THIN) -> None:
    """口：上横 + 左右竖 + 下横（外角硬折）。"""
    g.hbar(x1, x2, y_top, weight=w)
    g.vbar(x1, y_top, y_bot, weight=w)
    g.vbar(x2, y_top, y_bot, weight=w)
    g.hbar(x1, x2, y_bot, weight=w)


def part_mitsu(g: Glyph, x: int, y_top: int, y_bot: int) -> None:
    """小字頭 ⺌：中竖 + 左点(-14) + 右点(+14)。"""
    g.vbar(x, y_top, y_bot, weight=W_SEC)
    g.dot(x - 200, y_top + 55, w=W_DOT, h=96, slant=-14)
    g.dot(x + 200, y_top + 55, w=W_DOT, h=96, slant=14)


def part_mi(g: Glyph, x: int, y_top: int, y_bar: int, y_bot: int, w: int = W_MAIN) -> None:
    """米：丷(-14/+14) + 横 + 竖 + 撇 + 捺。"""
    g.dot(x - 100, y_top, w=W_DOT, h=96, slant=-14)  # 米的左上点
    g.dot(x + 90, y_top, w=W_DOT, h=96, slant=14)  # 米的右上点
    g.hbar(x - 180, x + 180, y_bar, weight=w)  # 米的横
    g.vbar(x, y_top + 40, y_bot, weight=w)  # 米的竖
    g.diag(x, y_bar - 40, x - 160, y_bot, weight=W_SEC)  # 米的撇
    g.diag(x, y_bar - 40, x + 170, y_bot, weight=W_SEC)  # 米的捺


def part_you(g: Glyph, x1: int, x2: int, y_top: int, y_bot: int,
              inner: tuple[int, int] | None = None) -> None:
    """用：左竖 + 横折 + 两横 + 中竖。

    `inner` 给两道内横的中心线 y；缺省时沿用旧画法（中点 / y_bot+90）。
    「備」的用是密字，旧画法把两道内横都堆在下半 → 白口 −9（腔封死），
    因此它显式传 (550, 440)（把两道内横按框高 thirds 均匀分布）。
    """
    g.vbar(x1, y_top, y_bot, weight=W_THIN)
    g.hbar(x1, x2, y_top, weight=W_THIN)
    g.vbar(x2, y_top, y_bot, weight=W_THIN)
    if inner is None:
        i1 = (y_top + y_bot) / 2
        i2 = y_bot + 90
    else:
        i1, i2 = inner
    g.hbar(x1, x2, i1, weight=W_THIN)
    g.hbar(x1, x2, i2, weight=W_THIN)
    g.vbar((x1 + x2) / 2, y_top, y_bot, weight=W_THIN)


def part_hai_to_kuchi(g: Glyph, x1: int, x2: int, y_top: int, y_bar: int, y_bot: int) -> None:
    """害的下部：丰（三横 + 竖）+ 口。割里的「害」与独立的「害」同一套画法。"""
    g.hbar(x1 + 60, x2 - 60, y_top, weight=W_THIN)  # 丰的上横
    g.hbar(x1 + 30, x2 - 30, y_bar, weight=W_THIN)  # 丰的中横
    g.hbar(x1, x2, y_bot, weight=W_SEC)  # 丰的下横
    g.vbar((x1 + x2) / 2, y_top + 60, y_bot, weight=W_SEC)  # 丰的竖
    part_kuchi(g, x1 + 60, x2 - 60, y_bot - 130, y_bot - 290, w=W_THIN)


# ======================================================================
# 24 个字形
# ======================================================================
def glyph_jou() -> Glyph:
    """常（U+5E38, 11画）—— ⺌ + 冖 + 口 + 巾。

    分区：冠 ⺌ y 720..820（x 258..742）；冖 y 648；口 x 330..670 y 400..534；
    巾 x 250..750 y 0..286。
    """
    g = Glyph("uni5E38", advance=1000, unicode=0x5E38, note="常：⺌+冖+口+巾")
    # ---- 冠（小字頭）：中竖 + 左点 + 右点 ----
    g.vbar(500, 820, 720, weight=W_SEC)
    g.dot(300, 765, w=W_DOT, h=96, slant=-14)
    g.dot(700, 765, w=W_DOT, h=96, slant=14)
    # ---- 冖：左点 + 横钩 ----
    g.dot(130, 690, w=W_DOT, h=96, slant=-14)
    g.hbar(100, 900, 648, weight=W_MAIN)
    g.diag(880, 646, 848, 584, weight=W_THIN)
    # ---- 口（内白 50）----
    part_kuchi(g, 330, 670, 534, 400)
    # ---- 巾：横 + 左竖 + 右竖 + 中竖（出脚到基线）----
    g.hbar(250, 750, 286, weight=W_MAIN)
    g.vbar(250, 286, 120, weight=W_SEC)
    g.vbar(750, 286, 120, weight=W_SEC)
    g.vbar(500, 286, 0, weight=W_MAIN)
    return g


def glyph_kou() -> Glyph:
    """校（U+6821, 10画）—— 木 + 交。

    分区：木 x 70..400 y 0..800；交 x 440..940 y 40..810。
    """
    g = Glyph("uni6821", advance=1000, unicode=0x6821, note="校：木+交")
    # ---- 木 ----
    g.hbar(70, 400, 600, weight=W_MAIN)
    g.vbar(235, 800, 0, weight=W_MAIN)
    g.diag(235, 585, 95, 60, weight=W_SEC)
    g.diag(235, 585, 395, 60, weight=W_SEC)
    # ---- 交：亠 + 八 + 乂（乂的两笔必须交叉）----
    g.dot(690, 780, w=76, h=72, slant=0)
    g.hbar(440, 940, 700, weight=W_MAIN)
    g.dot(560, 570, w=W_DOT, h=88, slant=14)  # 八的左脚（撇）
    g.dot(820, 570, w=W_DOT, h=88, slant=-14)  # 八的右脚（点）
    g.diag(760, 560, 520, 60, weight=W_SEC)  # 乂的撇（自右上向左下）
    g.diag(560, 560, 900, 60, weight=W_SEC)  # 乂的捺（自左上向右下）
    return g


def glyph_ryo() -> Glyph:
    """料（U+6599, 10画）—— 米 + 斗。

    分区：米 x 70..430；斗 x 480..940。
    """
    g = Glyph("uni6599", advance=1000, unicode=0x6599, note="料：米+斗")
    # ---- 米（与番/断的米同一套画法）----
    part_mi(g, 250, 750, 620, 0)
    # ---- 斗：两点 + 横 + 竖 ----
    g.dot(580, 720, w=W_DOT, h=96, slant=-14)
    g.dot(540, 570, w=W_DOT, h=96, slant=-14)
    g.hbar(480, 880, 470, weight=W_MAIN)
    g.vbar(790, 820, 40, weight=W_MAIN)
    return g


def glyph_sai() -> Glyph:
    """裁（U+88C1, 12画）—— 十 + 戈 + 衣（𧘇）。

    分区：十 x 70..380 y 600..810；戈 x 400..930 y 340..790；
    衣下部 x 130..900 y 30..540。
    """
    g = Glyph("uni88C1", advance=1000, unicode=0x88C1, note="裁：十+戈+衣")
    # ---- 十 ----
    g.hbar(70, 380, 750, weight=W_MAIN)
    g.vbar(220, 810, 600, weight=W_SEC)
    # ---- 戈（斜钩止于中段，捺留给衣，避免两条长斜并行）----
    g.dot(890, 790, w=76, h=84, slant=-14)  # 戈的点
    g.hbar(400, 930, 670, weight=W_MAIN)  # 戈的横
    g.diag(570, 790, 840, 340, weight=W_SEC)  # 戈的斜钩
    g.diag(840, 340, 876, 386, weight=W_THIN)  # 戈的钩尾
    g.diag(790, 690, 610, 430, weight=W_THIN)  # 戈的撇
    # ---- 衣（下部）----
    g.vbar(270, 540, 90, weight=W_SEC)  # 竖提的竖
    g.diag(270, 90, 340, 145, weight=W_THIN)  # 竖提的挑
    g.diag(340, 460, 130, 270, weight=W_SEC)  # 衣的撇
    g.diag(350, 400, 900, 30, weight=W_MAIN)  # 衣的捺
    return g


def glyph_kyuu() -> Glyph:
    """球（U+7403, 11画）—— 王 + 求。

    分区：王 x 70..380 y 48..820；求 x 450..940 y 60..820。
    """
    g = Glyph("uni7403", advance=1000, unicode=0x7403, note="球：王+求")
    # ---- 王 ----
    g.hbar(70, 380, 700, weight=W_MAIN)
    g.vbar(225, 820, 48, weight=W_MAIN)
    g.hbar(70, 380, 420, weight=W_SEC)
    g.hbar(70, 380, 48, weight=W_MAIN)
    # ---- 求：一 + 竖钩 + 提 + 点 + 撇 + 捺 ----
    g.hbar(450, 940, 720, weight=W_MAIN)
    g.vbar(690, 820, 60, weight=W_MAIN)
    g.diag(690, 60, 640, 125, weight=W_THIN)  # 求的钩
    g.diag(490, 570, 630, 640, weight=W_SEC)  # 求的提
    g.dot(880, 780, w=W_DOT, h=96, slant=-14)  # 求的点
    g.diag(660, 560, 470, 300, weight=W_SEC)  # 求的撇
    g.diag(690, 540, 920, 200, weight=W_SEC)  # 求的捺
    return g


def glyph_ei() -> Glyph:
    """営（U+55B6, 12画）—— ツ + 冖 + 呂。

    分区：ツ y 640..820；冖 y 640；上口 x 300..700 y 396..520；
    丿 y 320..384；下口 x 280..720 y 176..290。
    """
    g = Glyph("uni55B6", advance=1000, unicode=0x55B6, note="営：ツ+冖+呂")
    # ---- ツ：两点(丶) + 一撇 ----
    g.dot(330, 760, w=W_DOT, h=96, slant=-14)
    g.dot(470, 750, w=W_DOT, h=96, slant=-14)
    g.diag(620, 810, 545, 655, weight=W_SEC)
    # ---- 冖 ----
    g.dot(120, 690, w=W_DOT, h=96, slant=-14)
    g.hbar(90, 910, 640, weight=W_MAIN)
    g.diag(890, 638, 858, 576, weight=W_THIN)
    # ---- 呂：上口 + 丿 + 下口 ----
    part_kuchi(g, 300, 700, 520, 396)
    g.diag(440, 384, 330, 320, weight=W_THIN)
    part_kuchi(g, 280, 720, 290, 176)
    return g


def glyph_sei() -> Glyph:
    """証（U+8A3C, 12画）—— 言 + 正。

    分区：言 x 70..350 y 48..816；正 x 430..940 y 48..768。
    """
    g = Glyph("uni8A3C", advance=1000, unicode=0x8A3C, note="証：言+正")
    # ---- 言：点 + 横 + 二 + 口 ----
    g.dot(210, 780, w=76, h=72, slant=0)
    g.hbar(70, 350, 720, weight=W_MAIN)
    g.hbar(110, 320, 600, weight=W_THIN)
    g.hbar(110, 320, 490, weight=W_THIN)
    part_kuchi(g, 110, 320, 330, 48)
    # ---- 正：一 + 竖 + 短横 + 短竖 + 底横 ----
    g.hbar(430, 940, 720, weight=W_MAIN)
    g.vbar(700, 720, 300, weight=W_MAIN)
    g.hbar(700, 930, 520, weight=W_SEC)
    g.vbar(560, 520, 100, weight=W_SEC)
    g.hbar(430, 940, 48, weight=W_MAIN)
    return g


def glyph_en() -> Glyph:
    """援（U+63F4, 12画）—— 扌 + 爰。

    分区：扌 x 70..360 y 120..800；爰 x 430..940 y 60..810。
    """
    g = Glyph("uni63F4", advance=1000, unicode=0x63F4, note="援：扌+爰")
    # ---- 扌 ----
    g.hbar(70, 360, 660, weight=W_MAIN)
    g.vbar(210, 800, 120, weight=W_MAIN)
    g.diag(210, 120, 158, 178, weight=W_THIN)
    g.diag(70, 280, 340, 350, weight=W_SEC)
    # ---- 爰：爫 + 一 + 友 ----
    g.diag(810, 810, 460, 750, weight=W_THIN)  # 爫的撇
    g.dot(540, 700, w=76, h=84, slant=-14)  # 爫的点（左）
    g.dot(640, 712, w=76, h=84, slant=-14)  # 爫的点（中）
    g.dot(740, 724, w=76, h=84, slant=-14)  # 爫的点（右）
    g.hbar(430, 940, 580, weight=W_MAIN)  # 爰的横
    g.hbar(470, 900, 460, weight=W_SEC)  # 友的横
    g.diag(610, 520, 450, 60, weight=W_SEC)  # 友的撇
    g.hbar(500, 800, 320, weight=W_THIN)  # 又的横撇
    g.diag(800, 320, 610, 60, weight=W_THIN)  # 又的撇
    g.diag(540, 370, 920, 50, weight=W_MAIN)  # 又的捺
    return g


def glyph_wari() -> Glyph:
    """割（U+5272, 12画）—— 害 + 刂。

    分区：害 x 74..536 y 14..816；刂 x 680..850。
    """
    g = Glyph("uni5272", advance=1000, unicode=0x5272, note="割：害+刂")
    # ---- 害（宀 + 丰 + 口，纵向节奏与独立的「害」一致）----
    g.dot(300, 780, w=76, h=72, slant=0)  # 宀的点
    g.dot(130, 730, w=W_DOT, h=96, slant=-14)  # 宀的左点
    g.hbar(90, 520, 690, weight=W_MAIN)  # 宀的横钩
    g.diag(500, 688, 468, 626, weight=W_THIN)
    part_hai_to_kuchi(g, 90, 520, 570, 458, 346)
    # ---- 刂 ----
    part_rittou(g, 680, 850, 700, 330)
    return g


def glyph_hi() -> Glyph:
    """費（U+8CBB, 12画）—— 弗 + 貝。

    分区：弗 y 420..820；貝（目 + 八）y 0..484。
    """
    g = Glyph("uni8CBB", advance=1000, unicode=0x8CBB, note="費：弗+貝")
    # ---- 弗：𠃍(横+折) + 中横 + 竖折折钩 + 丨 + 丨（横画逐层下压，避免压住貝）----
    g.hbar(110, 890, 772, weight=W_LIGHT)  # 弗的上横
    g.vbar(850, 772, 658, weight=W_LIGHT)  # 弗的横折竖
    g.hbar(250, 850, 658, weight=W_LIGHT)  # 弗的中横
    g.vbar(250, 658, 550, weight=W_LIGHT)  # 弗的竖折
    g.hbar(250, 760, 550, weight=W_LIGHT)  # 弗的折横
    g.vbar(420, 800, 430, weight=W_LIGHT)  # 弗的左竖
    g.vbar(620, 800, 430, weight=W_LIGHT)  # 弗的右竖
    # ---- 貝：目 + 八 ----
    g.vbar(260, 442, 118, weight=W_LIGHT)
    g.hbar(260, 740, 442, weight=W_LIGHT)
    g.vbar(740, 442, 118, weight=W_LIGHT)
    g.hbar(260, 740, 334, weight=W_LIGHT)
    g.hbar(260, 740, 226, weight=W_LIGHT)
    g.hbar(260, 740, 118, weight=W_LIGHT)
    g.diag(330, 160, 190, 0, weight=W_SEC)  # 貝的撇
    g.diag(670, 160, 810, 0, weight=W_SEC)  # 貝的捺
    return g


def glyph_ten() -> Glyph:
    """転（U+8EE2, 11画）—— 車 + 云。

    分区：車 x 80..520 y 60..800；云 x 540..940 y 144..700。
    """
    g = Glyph("uni8EE2", advance=1000, unicode=0x8EE2, note="転：車+云")
    # ---- 車 ----
    g.hbar(80, 500, 740, weight=W_MAIN)  # 車的上横
    g.vbar(300, 800, 60, weight=W_MAIN)  # 車的中竖
    g.vbar(130, 640, 330, weight=W_THIN)  # 車的左竖
    g.hbar(130, 470, 640, weight=W_THIN)  # 車的横折
    g.vbar(470, 640, 330, weight=W_THIN)  # 車的右竖
    g.hbar(130, 470, 480, weight=W_THIN)  # 車的中横
    g.hbar(130, 470, 330, weight=W_THIN)  # 車的底横
    g.hbar(80, 520, 240, weight=W_SEC)  # 車的下横
    # ---- 云 ----
    g.hbar(560, 940, 700, weight=W_SEC)  # 云的上横
    g.hbar(540, 940, 540, weight=W_SEC)  # 云的下横
    g.diag(660, 430, 560, 190, weight=W_SEC)  # 厶的撇折
    g.hbar(560, 770, 190, weight=W_SEC)  # 厶的折底
    g.dot(830, 240, w=W_DOT, h=96, slant=-14)  # 厶的点
    return g


def glyph_ho() -> Glyph:
    """補（U+88DC, 12画）—— 衤 + 甫。

    分区：衤 x 80..350 y 0..838；甫 x 400..940 y 90..824。
    """
    g = Glyph("uni88DC", advance=1000, unicode=0x88DC, note="補：衤+甫")
    # ---- 衤 ----
    g.dot(200, 790, w=W_DOT, h=96, slant=-14)
    g.hbar(80, 330, 690, weight=W_THIN)  # 衤的横撇
    g.diag(330, 688, 130, 500, weight=W_THIN)
    g.vbar(210, 640, 0, weight=W_SEC)  # 衤的竖
    g.diag(210, 560, 95, 430, weight=W_THIN)  # 衤的撇
    g.dot(300, 450, w=W_DOT, h=88, slant=-14)  # 衤的点
    # ---- 甫 ----
    g.hbar(400, 940, 740, weight=W_THIN)  # 甫的横
    g.dot(900, 780, w=W_DOT, h=88, slant=-14)  # 甫的点
    part_you(g, 460, 880, 640, 90)
    return g


def glyph_dan() -> Glyph:
    """断（U+65AD, 11画）—— 米 + 斤。

    分区：米 x 70..430 y 0..810；斤 x 480..940 y 60..790。
    """
    g = Glyph("uni65AD", advance=1000, unicode=0x65AD, note="断：米+斤")
    # ---- 米（右下捺改点）----
    g.dot(180, 750, w=W_DOT, h=96, slant=-14)
    g.dot(330, 750, w=W_DOT, h=96, slant=14)
    g.hbar(70, 430, 620, weight=W_MAIN)
    g.vbar(250, 810, 0, weight=W_MAIN)
    g.diag(250, 560, 90, 40, weight=W_SEC)
    g.dot(390, 330, w=W_DOT, h=96, slant=-14)  # 米的捺改点
    # ---- 斤 ----
    g.diag(700, 790, 520, 700, weight=W_SEC)  # 斤的撇
    g.diag(560, 700, 500, 60, weight=W_SEC)  # 斤的左撇
    g.hbar(480, 940, 420, weight=W_MAIN)
    g.vbar(800, 700, 60, weight=W_MAIN)
    return g


def glyph_itsu() -> Glyph:
    """違（U+9055, 12画）—— 辶 + 韋。

    分区：韋 x 500..940 y 210..826；辶 x 80..880 y 40..790。
    2026-10-31 回修：韋的橫與上口的底白口 −10 → 韋的橫下移到 432、白口 24；
    上口框高 90 → 108（腔 24）、下口框高 90 → 108（腔 24）。
    """
    g = Glyph("uni9055", advance=1000, unicode=0x9055, note="違：辶+韋")
    # ---- 韋 ----
    g.hbar(520, 900, 780, weight=W_SEC)  # 韋的上横
    part_kuchi(g, 600, 820, 666, 546)  # 韋的上口（腔 36）
    g.hbar(500, 940, 432, weight=W_MAIN)  # 韋的横
    g.vbar(710, 600, 300, weight=W_SEC)  # 韋的竖
    part_kuchi(g, 600, 820, 318, 198)  # 韋的下口（腔 36）
    # ---- 辶 ----
    g.dot(150, 740, w=W_DOT, h=96, slant=-14)  # 辶的点
    g.hbar(80, 240, 620, weight=W_THIN)  # 辶的横折
    g.vbar(240, 620, 480, weight=W_THIN)
    g.hbar(80, 240, 480, weight=W_THIN)
    g.diag(170, 480, 100, 330, weight=W_THIN)  # 辶的折撇
    g.diag(120, 330, 880, 40, weight=W_MAIN)  # 辶的捺
    return g


def glyph_sho() -> Glyph:
    """消（U+6D88, 10画）—— 氵 + 肖。

    分区：氵 x 36..294（与「港」同坐标）；肖 x 430..880 y 100..800。
    """
    g = Glyph("uni6D88", advance=1000, unicode=0x6D88, note="消：氵+肖")
    # ---- 氵（与「港」同坐标）----
    part_sanzui(g)
    # ---- 肖：小字頭 + 月 ----
    part_mitsu(g, 620, 800, 640)
    g.diag(475, 640, 445, 100, weight=W_SEC)  # 月的左撇
    g.hbar(470, 820, 640, weight=W_THIN)  # 月的横折
    g.vbar(820, 640, 100, weight=W_THIN)
    g.diag(820, 100, 768, 156, weight=W_THIN)  # 月的钩
    g.hbar(470, 820, 450, weight=W_THIN)  # 月的第一横
    g.hbar(470, 820, 260, weight=W_THIN)  # 月的第二横
    return g


def glyph_ban() -> Glyph:
    """番（U+756A, 12画）—— 釆 + 田。

    分区：釆 y 380..810；田 x 150..850 y 60..372。
    """
    g = Glyph("uni756A", advance=1000, unicode=0x756A, note="番：釆+田")
    # ---- 釆：丿 + 米 ----
    g.diag(780, 810, 220, 750, weight=W_SEC)  # 釆的撇
    g.dot(400, 700, w=W_DOT, h=96, slant=-14)
    g.dot(640, 700, w=W_DOT, h=96, slant=14)
    g.hbar(280, 720, 600, weight=W_MAIN)  # 釆的横
    g.vbar(500, 740, 360, weight=W_MAIN)  # 釆的竖
    g.diag(500, 540, 330, 380, weight=W_SEC)  # 釆的撇
    g.diag(500, 540, 680, 380, weight=W_SEC)  # 釆的捺
    # ---- 田 ----
    g.vbar(150, 330, 60, weight=W_THIN)
    g.hbar(150, 850, 330, weight=W_THIN)
    g.vbar(850, 330, 60, weight=W_THIN)
    g.vbar(500, 330, 60, weight=W_THIN)
    g.hbar(150, 850, 200, weight=W_THIN)
    g.hbar(150, 850, 60, weight=W_THIN)
    return g


def glyph_ki() -> Glyph:
    """規（U+898F, 11画）—— 夫 + 見。

    分区：夫 x 60..500 y 40..752；見 x 545..930（与「視」同坐标）。
    """
    g = Glyph("uni898F", advance=1000, unicode=0x898F, note="規：夫+見")
    # ---- 夫 ----
    g.hbar(80, 480, 700, weight=W_SEC)
    g.hbar(60, 500, 560, weight=W_SEC)
    g.diag(290, 700, 90, 40, weight=W_SEC)
    g.diag(290, 700, 490, 40, weight=W_SEC)
    # ---- 見 ----
    part_miru(g)
    return g


def glyph_jutsu() -> Glyph:
    """術（U+8853, 11画）—— 彳 + 朮 + 亍。

    分区：彳 x 60..230；朮 x 280..660；亍 x 670..940。
    """
    g = Glyph("uni8853", advance=1000, unicode=0x8853, note="術：彳+朮+亍")
    # ---- 彳 ----
    g.diag(210, 800, 100, 680, weight=W_SEC)
    g.diag(230, 660, 90, 500, weight=W_SEC)
    g.vbar(150, 480, 60, weight=W_SEC)
    # ---- 朮 ----
    g.hbar(280, 640, 640, weight=W_SEC)
    g.vbar(460, 780, 120, weight=W_MAIN)
    g.diag(460, 600, 290, 160, weight=W_SEC)
    g.diag(460, 600, 640, 160, weight=W_SEC)
    g.dot(620, 730, w=W_DOT, h=88, slant=-14)  # 朮的点
    # ---- 亍 ----
    g.hbar(700, 930, 740, weight=W_SEC)
    g.hbar(670, 940, 600, weight=W_SEC)
    g.vbar(800, 600, 60, weight=W_SEC)
    g.diag(800, 60, 748, 122, weight=W_THIN)
    return g


def glyph_ten_bi() -> Glyph:
    """展（U+5C55, 10画）—— 尸 + 龷 + 衣（𧘇）。

    分区：尸 x 90..880 y 60..812；龷 x 230..800 y 380..572；
    衣下部 x 200..900 y 40..380。
    """
    g = Glyph("uni5C55", advance=1000, unicode=0x5C55, note="展：尸+龷+衣")
    # ---- 尸 ----
    g.hbar(120, 880, 760, weight=W_SEC)
    g.vbar(880, 760, 560, weight=W_SEC)
    g.hbar(120, 880, 620, weight=W_SEC)
    g.diag(180, 760, 90, 60, weight=W_SEC)
    # ---- 龷 ----
    g.hbar(230, 800, 520, weight=W_SEC)
    g.vbar(350, 520, 380, weight=W_THIN)
    g.vbar(680, 520, 380, weight=W_THIN)
    g.hbar(230, 800, 380, weight=W_SEC)
    # ---- 衣（下部）----
    g.vbar(430, 380, 120, weight=W_SEC)
    g.diag(430, 300, 200, 60, weight=W_SEC)  # 衣的撇
    g.diag(430, 380, 900, 40, weight=W_MAIN)  # 衣的捺
    return g


def glyph_bi() -> Glyph:
    """備（U+5099, 12画）—— 亻 + 用 + 寸。

    分区：亻 x 60..250；𠂉+用 x 300..900 y 330..810；寸 y 60..250。
    2026-10-31 回修：用的兩道內橫白口 −9（腔封死）→ 兩橫改按框高 thirds 分布
    （550 / 440），各層白口 26。part_you 加 inner 參數，只有備用新畫法。
    """
    g = Glyph("uni5099", advance=1000, unicode=0x5099, note="備：亻+用+寸")
    # ---- 亻 ----
    g.diag(240, 810, 110, 560, weight=W_SEC)
    g.vbar(170, 560, 0, weight=W_MAIN)
    # ---- 𠂉（撇）+ 用 ----
    g.diag(780, 810, 330, 742, weight=W_SEC)
    part_you(g, 330, 900, 660, 330, inner=(550, 440))
    # ---- 寸 ----
    g.hbar(300, 900, 230, weight=W_SEC)
    g.vbar(800, 230, 0, weight=W_SEC)
    g.diag(800, 0, 746, 62, weight=W_THIN)
    g.dot(480, 150, w=W_DOT, h=88, slant=-14)  # 寸的点
    return g


def glyph_gai() -> Glyph:
    """害（U+5BB3, 10画）—— 宀 + 丰 + 口。

    分区：宀 y 642..816；丰 x 260..740 y 346..570；口 x 320..680 y 56..216。
    """
    g = Glyph("uni5BB3", advance=1000, unicode=0x5BB3, note="害：宀+丰+口")
    # ---- 宀 ----
    g.dot(500, 780, w=76, h=72, slant=0)
    g.dot(190, 720, w=W_DOT, h=96, slant=-14)
    g.hbar(120, 880, 690, weight=W_MAIN)
    g.diag(860, 688, 828, 626, weight=W_THIN)
    # ---- 丰 + 口 ----
    part_hai_to_kuchi(g, 260, 740, 570, 458, 346)
    return g


def glyph_hai() -> Glyph:
    """配（U+914D, 10画）—— 酉 + 己。

    分区：酉 x 70..500 y 60..792；己 x 560..940 y 140..772。
    2026-10-31 回修：酉的一與冂的橫白口 −10 → 冂的橫與兩根豎下移 34、白口 24。
    """
    g = Glyph("uni914D", advance=1000, unicode=0x914D, note="配：酉+己")
    # ---- 酉 ----
    g.hbar(70, 500, 740, weight=W_MAIN)
    g.vbar(140, 626, 60, weight=W_THIN)
    g.hbar(140, 440, 626, weight=W_THIN)
    g.vbar(440, 626, 60, weight=W_THIN)
    g.diag(250, 655, 220, 575, weight=W_THIN)  # 酉的内撇
    g.vbar(360, 655, 470, weight=W_THIN)  # 酉的内竖
    g.hbar(140, 440, 470, weight=W_THIN)  # 酉的内横
    g.hbar(140, 440, 60, weight=W_THIN)  # 酉的底横
    # ---- 己 ----
    g.hbar(580, 900, 720, weight=W_MAIN)
    g.vbar(900, 720, 560, weight=W_MAIN)
    g.hbar(580, 900, 560, weight=W_MAIN)
    g.vbar(580, 560, 140, weight=W_MAIN)
    g.hbar(580, 880, 140, weight=W_MAIN)
    g.diag(880, 140, 922, 192, weight=W_THIN)  # 己的钩
    return g


def glyph_fuku() -> Glyph:
    """副（U+526F, 11画）—— 畐 + 刂。

    分区：畐 x 70..560 y 116..820；刂 x 700..880。
    """
    g = Glyph("uni526F", advance=1000, unicode=0x526F, note="副：畐+刂")
    # ---- 畐：一 + 口 + 田 ----
    g.hbar(70, 560, 772, weight=W_MAIN)
    part_kuchi(g, 180, 450, 650, 520)
    g.vbar(90, 400, 160, weight=W_THIN)  # 田的左竖
    g.hbar(90, 530, 400, weight=W_THIN)  # 田的横折
    g.vbar(530, 400, 160, weight=W_THIN)  # 田的右竖
    g.vbar(310, 400, 160, weight=W_THIN)  # 田的中竖
    g.hbar(90, 530, 280, weight=W_THIN)  # 田的中横
    g.hbar(90, 530, 160, weight=W_THIN)  # 田的底横
    # ---- 刂 ----
    part_rittou(g, 700, 870, 700, 330)
    return g


def glyph_shi() -> Glyph:
    """視（U+8996, 11画）—— 礻 + 見。

    分区：礻 x 80..350 y 60..838；見 x 545..930（与「規」同坐标）。
    """
    g = Glyph("uni8996", advance=1000, unicode=0x8996, note="視：礻+見")
    # ---- 礻 ----
    g.dot(190, 790, w=W_DOT, h=96, slant=-14)
    g.hbar(80, 320, 680, weight=W_SEC)  # 礻的横撇
    g.diag(320, 678, 120, 500, weight=W_THIN)
    g.vbar(200, 620, 60, weight=W_MAIN)  # 礻的竖
    g.dot(310, 430, w=W_DOT, h=88, slant=-14)  # 礻的点
    # ---- 見 ----
    part_miru(g)
    return g


# ======================================================================
# 构建
# ======================================================================
def build() -> list[Glyph]:
    return [
        glyph_jou(),
        glyph_kou(),
        glyph_ryo(),
        glyph_sai(),
        glyph_kyuu(),
        glyph_ei(),
        glyph_sei(),
        glyph_en(),
        glyph_wari(),
        glyph_hi(),
        glyph_ten(),
        glyph_ho(),
        glyph_dan(),
        glyph_itsu(),
        glyph_sho(),
        glyph_ban(),
        glyph_ki(),
        glyph_jutsu(),
        glyph_ten_bi(),
        glyph_bi(),
        glyph_gai(),
        glyph_hai(),
        glyph_fuku(),
        glyph_shi(),
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s3-004.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
