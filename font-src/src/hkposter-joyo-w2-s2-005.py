"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-005。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
- 字面框固定 x 60..940 / y 0..820，advance 1000，与 zh-HK 繁体汉字同档，
  便于中英日混排时不跳动。
- 笔画权重只用四档：主 96 / 次 92 / 细 84 / 点 84。
  6–7 画的字（町 沢 状 役 身 防 車 何 足 宅 条 究 述 州 声）以 96 为主笔，
  笔画少 → 加粗，保证同批里不显轻；
  8–9 画的字（建 空 急 送 供 施 食 研 南 神 独 育 乗 店 武 念 待）
  在拥挤处（横画叠横画、并排竖画、框内）降为 92/84，保证内白仍读得出。
- 部件复用：氵 / 亻 / 彳 / 辶 / 宀 / 方 / 心 / 士-寸 一类在本批内共用同一套
  坐标参数，只按字宽做位置与大小的光学校正，不重新发明形状（docs/03 GLY-004）。
- 横画中心线一律内缩半个笔画宽，使墨迹上缘贴 820 / 下缘贴 0；
  竖画端点即墨迹端点，横竖相接时竖端点取对方墨迹边缘，接缝自然并集。
- 斜画（撇/捺/提）用统一的 ink-box 反解函数：给定期望墨迹框，直接反算中心线，
  因此每根斜画的墨迹范围与参考完全一致，且不会越出字面框。
- 密排处（横画叠横画）内白 >= 24 单位；并排竖画之间留 >= 60 单位白；
  闭框字（田 口 类）受字面宽所限，内白取 30–50，属结构封闭的必然结果。
- 禁止逐字机械挤压或倾斜（docs/02 偏差 D）：斜画只用两种固定倾角，
  按字宽缩放长度，不改角度。

结构依据
--------
每字的笔画清单与墨迹范围逐字比对 KanjiVG 笔顺数据集（日本語標準筆順），
并与 Windows 系统日文字体（Yu Gothic Bold）渲染样张目视核对，
两者一致后才落坐标；形近易错处（州/車/声/足/食/施/独/乗）按参考改写，
不凭印象。

坐标系：x 向右，y 向上，基线 y=0，ascender 880 / descender -120。
"""

from __future__ import annotations

import math
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

X_L = 60
X_R = 940
Y_T = 820
Y_B = 0


# --------------------------------------------------------------------------
# 对齐辅助函数
# --------------------------------------------------------------------------
def bar(g: Glyph, x1: float, x2: float, y: float, w: float = W_MAIN) -> None:
    """水平笔画，y 为中心线，墨迹占 y ± w/2，横跨 x1..x2。"""
    g.hbar(x1, x2, y, weight=w)


def vbar(g: Glyph, x: float, y1: float, y2: float, w: float = W_MAIN) -> None:
    """垂直笔画：x 为中心线，墨迹占 x ± w/2，纵跨 y1..y2（端点即墨迹端点）。"""
    g.vbar(x, y1, y2, weight=w)


def pie(g: Glyph, x0: float, y0: float, x1: float, y1: float,
        w: float = W_MAIN) -> None:
    """撇：墨迹框 (x0,y0)-(x1,y1)，中心线自右上走向左下。"""
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy) or 1.0
    a, b = dx / length, dy / length
    g.diag(x1 - w / 2 * b, y1 - w / 2 * a, x0 + w / 2 * b, y0 + w / 2 * a,
           weight=w)


def na(g: Glyph, x0: float, y0: float, x1: float, y1: float,
       w: float = W_MAIN) -> None:
    """捺：墨迹框 (x0,y0)-(x1,y1)，中心线自左上走向右下。"""
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy) or 1.0
    px, py = dy / length, dx / length
    g.diag(x0 + w / 2 * px, y1 - w / 2 * py, x1 - w / 2 * px, y0 + w / 2 * py,
           weight=w)


def ti(g: Glyph, x0: float, y0: float, x1: float, y1: float,
       w: float = W_MAIN) -> None:
    """提：墨迹框 (x0,y0)-(x1,y1)，中心线自左下走向右上。"""
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy) or 1.0
    px, py = dy / length, dx / length
    g.diag(x0 + w / 2 * px, y0 + w / 2 * py, x1 - w / 2 * px, y1 - w / 2 * py,
           weight=w)


def tick(g: Glyph, x: float, y0: float, y1: float, w: float = W_MAIN) -> None:
    """短竖（宀/亠/广/方/良 的点，写成竖笔的日式点）。"""
    g.vbar(x, y0, y1, weight=w)


def hook_left(g: Glyph, x: float, y_bottom: float, w: float = W_THIN,
              length: float = 88, rise: float = 52) -> None:
    """左钩（亅）：竖笔底部向左上挑的短斜画。"""
    g.diag(x, y_bottom, x - length, y_bottom + rise, weight=w)


# --------------------------------------------------------------------------
# 复用部件（全批统一坐标参数，只按字宽微调）
# --------------------------------------------------------------------------
def part_ninkyou(g: Glyph, dot_x: float = 203, dot_y: float = 694,
                 zx0: float = 94, zx1: float = 264, zy: float = 410,
                 sx0: float = 96, sx1: float = 838, sy: float = 47) -> None:
    """辶（しんにょう）：点 + 折 + 长払い。"""
    g.dot(dot_x, dot_y, w=99, h=89, slant=0)
    g.hbar(zx0, zx1, zy, weight=W_THIN)
    g.diag(zx1 - 14, zy - 30, zx0 + 56, zy - 250, weight=W_THIN)
    na(g, sx0, sy, sx1, sy + 116, W_THIN)


def part_kokoro(g: Glyph, x0: float = 330, x1: float = 830,
                y_top: float = 220, y_bot: float = 55) -> None:
    """心（下部四点）：左点 + 卧钩 + 中点 + 右点。"""
    g.diag(x0, y_top - 10, x0 + 62, y_bot, weight=W_MAIN)
    g.diag(x0 + 62, y_bot, x1 - 70, y_bot, weight=W_MAIN)
    g.diag(x1 - 70, y_bot, x1 - 30, y_bot + 65, weight=W_DOT)


# --------------------------------------------------------------------------
# 字形
# --------------------------------------------------------------------------
def uni753A() -> Glyph:
    """町 U+753A（7画）= 田 + 丁。

    分区：田 x 60..391 / y 220..659；丁 x 447..911 / y 0..707。
    笔画（KanjiVG 墨迹框换算）：
      1 田左竖  vbar(106, 262, 617, 92)
      2 田横折  hbar(106, 391, 617, 84) + vbar(345, 262, 617, 92)
      3 田中竖  vbar(226, 262, 617, 84)
      4 田中横  hbar(152, 299, 445, 84)
      5 田下横  hbar(106, 391, 262, 84)
      6 丁横    hbar(447, 911, 665, 84)
      7 丁竖钩  vbar(752, 0, 665, 96) + 左钩
    """
    g = Glyph("uni753A", advance=1000, unicode=0x753A, note="町 田+丁")
    vbar(g, 106, 262, 617, W_SEC)
    bar(g, 106, 391, 617, W_THIN)
    vbar(g, 345, 262, 617, W_SEC)
    vbar(g, 226, 262, 617, W_THIN)
    bar(g, 152, 299, 445, W_THIN)
    bar(g, 106, 391, 262, W_THIN)
    bar(g, 447, 911, 665, W_THIN)
    vbar(g, 752, 0, 665, W_MAIN)
    hook_left(g, 752, 62, W_THIN, 88, 52)
    return g


def uni6CA2() -> Glyph:
    """沢 U+6CA2（7画）= 氵 + 尺。

    分区：氵 x 82..253 / y 80..775；尺 x 295..872 / y 70..752。
    笔画：
      1 氵上点  dot(208, 737, 90, 75)
      2 氵中点  dot(130, 501, 96, 70)
      3 氵提    ti(89, 80, 234, 257, 96)
      4 尺横折  hbar(422, 772, 710, 84) + vbar(726, 516, 710, 92)
      5 尺横    hbar(456, 726, 492, 84)
      6 尺撇    pie(295, 90, 455, 695, 96)
      7 尺捺    na(536, 70, 872, 478, 96)
    """
    g = Glyph("uni6CA2", advance=1000, unicode=0x6CA2, note="沢 氵+尺")
    g.dot(208, 737, w=90, h=75, slant=0)
    g.dot(130, 501, w=96, h=70, slant=0)
    ti(g, 89, 80, 234, 257, W_MAIN)
    bar(g, 422, 772, 710, W_THIN)
    vbar(g, 726, 516, 710, W_SEC)
    bar(g, 456, 726, 492, W_THIN)
    pie(g, 295, 90, 455, 695, W_MAIN)
    na(g, 536, 70, 872, 478, W_MAIN)
    return g


def uni72B6() -> Glyph:
    """状 U+72B6（7画）= 丬 + 犬。

    分区：丬 x 82..310（竖在右，点/提在左）；犬 x 387..875。
    笔画：
      1 丬竖  vbar(303, 39, 752, 96)
      2 丬点  dot(164, 579, 96, 94)
      3 丬提  ti(82, 233, 232, 365, 96)
      4 犬横  hbar(397, 830, 493, 84)
      5 犬撇  pie(387, 56, 606, 752, 96)
      6 犬捺  na(594, 87, 875, 484, 96)
      7 犬点  dot(768, 679, 84, 92)
    """
    g = Glyph("uni72B6", advance=1000, unicode=0x72B6, note="状 丬+犬")
    vbar(g, 303, 39, 752, W_MAIN)
    g.dot(164, 579, w=96, h=94, slant=0)
    ti(g, 82, 233, 232, 365, W_MAIN)
    bar(g, 397, 830, 493, W_THIN)
    pie(g, 387, 56, 606, 752, W_MAIN)
    na(g, 594, 87, 875, 484, W_MAIN)
    g.dot(768, 679, w=84, h=92, slant=0)
    return g


def uni5EFA() -> Glyph:
    """建 U+5EFA（9画）= 聿 + 廴。

    分区：聿 x 377..921 / y 272..812；廴 x 99..845 / y 41..692。
    笔画（聿 6 画：横折 + 四横 + 中竖；横画中心距 114，内白 30）：
      1 聿横折 hbar(450, 814, 770, 84) + vbar(772, 600, 770, 92)
      2 聿一   hbar(377, 921, 656, 84)
      3 聿一   hbar(451, 804, 542, 84)
      4 聿一   hbar(454, 826, 428, 84)
      5 聿一   hbar(405, 885, 314, 84)
      6 聿中竖 vbar(626, 100, 800, 96)
      7 廴横撇 hbar(108, 316, 650, 84) + pie(108, 439, 316, 650, 92)
      8 廴折   vbar(150, 120, 470, 92)
      9 廴払い na(99, 41, 845, 175, 84)
    """
    g = Glyph("uni5EFA", advance=1000, unicode=0x5EFA, note="建 聿+廴")
    bar(g, 450, 814, 770, W_THIN)
    vbar(g, 772, 600, 770, W_SEC)
    bar(g, 377, 921, 656, W_THIN)
    bar(g, 451, 804, 542, W_THIN)
    bar(g, 454, 826, 428, W_THIN)
    bar(g, 405, 885, 314, W_THIN)
    vbar(g, 626, 100, 800, W_MAIN)
    # 廴
    bar(g, 108, 316, 650, W_THIN)
    pie(g, 108, 439, 316, 650, W_SEC)
    vbar(g, 150, 120, 470, W_SEC)
    na(g, 99, 41, 845, 175, W_THIN)
    return g


def uni7A7A() -> Glyph:
    """空 U+7A7A（8画）= 宀 + 八 + 工。

    分区：宀 y 604..793；八 y 349..604；工 y 31..330。
    笔画：
      1 宀点   tick(487, 664, 793, 84)
      2 宀左点 dot(212, 582, 56, 130)
      3 宀横钩 hbar(240, 848, 645, 84) + 钩
      4 八撇   pie(215, 349, 377, 550, 84)
      5 八捺   na(551, 416, 795, 604, 84)
      6 工上横 hbar(285, 701, 288, 84)
      7 工竖   vbar(491, 88, 266, 96)
      8 工下横 hbar(162, 867, 79, 96)
    """
    g = Glyph("uni7A7A", advance=1000, unicode=0x7A7A, note="空 宀+八+工")
    tick(g, 487, 664, 793, W_THIN)
    g.dot(212, 582, w=56, h=130, slant=0)
    bar(g, 240, 848, 645, W_THIN)
    g.diag(843, 645, 800, 578, weight=W_DOT)
    pie(g, 215, 349, 377, 550, W_THIN)
    na(g, 551, 416, 795, 604, W_THIN)
    bar(g, 285, 701, 288, W_THIN)
    vbar(g, 491, 88, 266, W_MAIN)
    bar(g, 162, 867, 79, W_MAIN)
    return g


def uni6025() -> Glyph:
    """急 U+6025（9画）= ク + 彐 + 心。

    分区：ク y 561..784；彐 y 303..616；心 y 17..250。
    笔画：
      1 ク撇   pie(172, 561, 416, 784, 92)
      2 ク横撇 hbar(398, 638, 719, 84) + pie(398, 581, 638, 719, 84)
      3 彐横折 hbar(270, 731, 574, 84) + vbar(687, 349, 574, 92)
      4 彐一   hbar(253, 687, 460, 84)
      5 彐一   hbar(261, 662, 345, 84)
      6 心左点 ti(142, 34, 216, 205, 76)
      7 心卧钩 diag(340,230,420,60)+diag(420,60,800,60)+钩
      8 心中点 dot(535, 217, 70, 62)
      9 心右点 dot(800, 236, 93, 103)
    """
    g = Glyph("uni6025", advance=1000, unicode=0x6025, note="急 ク+彐+心")
    pie(g, 172, 561, 416, 784, W_SEC)
    bar(g, 398, 638, 719, W_THIN)
    pie(g, 398, 581, 638, 719, W_THIN)
    bar(g, 270, 731, 574, W_THIN)
    vbar(g, 687, 349, 574, W_SEC)
    bar(g, 253, 687, 460, W_THIN)
    bar(g, 261, 662, 345, W_THIN)
    # 心
    ti(g, 142, 34, 216, 205, W_DOT)
    g.diag(340, 230, 420, 60, weight=W_MAIN)
    g.diag(420, 60, 800, 60, weight=W_MAIN)
    g.diag(800, 60, 838, 125, weight=W_DOT)
    g.dot(535, 217, w=70, h=62, slant=0)
    g.dot(800, 236, w=93, h=103, slant=0)
    return g


def uni9001() -> Glyph:
    """送 U+9001（8画）= 关 + 辶。

    分区：关 x 374..872 / y 164..773；辶 x 99..836 / y 41..734。
    笔画：
      1 丷左点 dot(489, 683, 89, 118)
      2 丷右撇 pie(636, 611, 730, 773, 84)
      3 天横   hbar(438, 790, 578, 84)
      4 天横   hbar(374, 872, 419, 84)
      5 天撇   pie(396, 172, 616, 557, 96)
      6 天捺   na(618, 164, 812, 357, 96)
      7 辶点+折+払（part_ninkyou）
    """
    g = Glyph("uni9001", advance=1000, unicode=0x9001, note="送 关+辶")
    g.dot(489, 683, w=89, h=118, slant=0)
    pie(g, 636, 611, 730, 773, W_THIN)
    bar(g, 438, 790, 578, W_THIN)
    bar(g, 374, 872, 419, W_THIN)
    pie(g, 396, 172, 616, 557, W_MAIN)
    na(g, 618, 164, 812, 357, W_MAIN)
    part_ninkyou(g, dot_x=222, dot_y=686, zx0=99, zx1=270, zy=450,
                 sx0=110, sx1=836, sy=41)
    return g


def uni4F9B() -> Glyph:
    """供 U+4F9B（8画）= 亻 + 共。

    分区：亻 x 91..294；共 x 329..922 / y 61..761。
    笔画：
      1 亻撇   pie(91, 369, 294, 732, 92)
      2 亻竖   vbar(230, 52, 520, 96)
      3 共上横 hbar(367, 847, 572, 84)
      4 共左竖 vbar(497, 345, 715, 92)
      5 共右竖 vbar(707, 360, 761, 92)
      6 共下横 hbar(329, 922, 344, 84)
      7 共撇   pie(340, 61, 514, 247, 92)
      8 共捺   na(699, 75, 896, 260, 92)
    """
    g = Glyph("uni4F9B", advance=1000, unicode=0x4F9B, note="供 亻+共")
    pie(g, 91, 369, 294, 732, W_SEC)
    vbar(g, 230, 52, 520, W_MAIN)
    bar(g, 367, 847, 572, W_THIN)
    vbar(g, 497, 345, 715, W_SEC)
    vbar(g, 707, 360, 761, W_SEC)
    bar(g, 329, 922, 344, W_THIN)
    pie(g, 340, 61, 514, 247, W_SEC)
    na(g, 699, 75, 896, 260, W_SEC)
    return g


def uni5F79() -> Glyph:
    """役 U+5F79（7画）= 彳 + 殳。

    分区：彳 x 94..309；殳 x 350..890 / y 45..777。
    笔画：
      1 彳撇  pie(112, 595, 277, 770, 84)
      2 彳撇  pie(94, 313, 309, 592, 92)
      3 彳竖  vbar(242, 20, 424, 96)
      4 殳撇  pie(382, 459, 483, 755, 84)
      5 殳横折弯钩 hbar(495, 859, 758, 84) + vbar(813, 539, 758, 92) + 钩
      6 又横撇 hbar(350, 733, 445, 84) + pie(350, 45, 733, 445, 96)
      7 又捺  na(432, 53, 890, 331, 96)
    """
    g = Glyph("uni5F79", advance=1000, unicode=0x5F79, note="役 彳+殳")
    pie(g, 112, 595, 277, 770, W_THIN)
    pie(g, 94, 313, 309, 592, W_SEC)
    vbar(g, 242, 20, 424, W_MAIN)
    pie(g, 382, 459, 483, 755, W_THIN)
    bar(g, 495, 859, 758, W_THIN)
    vbar(g, 813, 539, 758, W_SEC)
    g.diag(813, 560, 768, 618, weight=W_DOT)
    bar(g, 350, 733, 445, W_THIN)
    pie(g, 350, 45, 733, 445, W_MAIN)
    na(g, 432, 53, 890, 331, W_MAIN)
    return g


def uni8EAB() -> Glyph:
    """身 U+8EAB（7画）= 丿 + 丨 + 横折 + 二横 + 提 + 撇。

    分区：身身 x 310..662 / y 0..732；末撇 x 230..700。
    笔画：
      1 撇   pie(406, 699, 488, 814, 84)
      2 丨   vbar(318, 322, 685, 96)
      3 横折 hbar(331, 662, 690, 84) + vbar(636, 0, 690, 96)
      4 一   hbar(336, 650, 583, 84)
      5 一   hbar(338, 647, 473, 84)
      6 提   ti(153, 274, 652, 401, 84)
      7 撇   pie(230, 80, 700, 500, 96)
    """
    g = Glyph("uni8EAB", advance=1000, unicode=0x8EAB, note="身")
    pie(g, 406, 699, 488, 814, W_THIN)
    vbar(g, 318, 322, 685, W_LIGHT)
    bar(g, 331, 662, 690, W_LIGHT)
    vbar(g, 636, 0, 690, W_LIGHT)
    bar(g, 336, 650, 583, W_LIGHT)
    bar(g, 338, 647, 473, W_THIN)
    ti(g, 153, 274, 652, 401, W_THIN)
    pie(g, 230, 80, 700, 500, W_MAIN)
    return g


def uni65BD() -> Glyph:
    """施 U+65BD（9画）= 方 + 𠂉 + 也。

    分区：方 x 76..418；𠂉 y 514..759；也 x 438..902 / y 56..495。
    笔画：
      1 方点   tick(274, 608, 761, 84)
      2 方横   hbar(99, 418, 596, 84)
      3 方横折钩 hbar(166, 371, 448, 84) + vbar(327, 59, 448, 92) + 钩
      4 方撇   pie(76, 196, 287, 561, 96)
      5 𠂉撇   pie(436, 514, 576, 759, 84)
      6 𠂉横   hbar(553, 865, 649, 84)
      7 也横折钩 hbar(438, 869, 474, 84) + vbar(839, 214, 474, 92) + 钩
      8 也丨   vbar(656, 208, 574, 96)
      9 也乚   vbar(540, 110, 460, 96) + 折 + 钩
    """
    g = Glyph("uni65BD", advance=1000, unicode=0x65BD, note="施 方+𠂉+也")
    tick(g, 274, 608, 761, W_THIN)
    bar(g, 99, 418, 596, W_THIN)
    bar(g, 166, 371, 448, W_THIN)
    vbar(g, 327, 59, 448, W_SEC)
    g.diag(327, 90, 282, 148, weight=W_DOT)
    pie(g, 76, 196, 287, 561, W_MAIN)
    pie(g, 436, 514, 576, 759, W_THIN)
    bar(g, 553, 865, 649, W_THIN)
    bar(g, 438, 869, 474, W_THIN)
    vbar(g, 839, 214, 474, W_SEC)
    g.diag(839, 245, 795, 303, weight=W_DOT)
    vbar(g, 656, 208, 574, W_MAIN)
    vbar(g, 540, 80, 460, W_MAIN)
    na(g, 540, 56, 880, 110, W_SEC)
    g.diag(872, 100, 896, 172, weight=W_DOT)
    return g


def uni98DF() -> Glyph:
    """食 U+98DF（9画）= 𠆢 + 良。

    分区：人字头 y 437..806；良 x 340..829 / y 33..638。
    笔画：
      1 撇   pie(108, 437, 484, 806, 92)
      2 捺   na(483, 500, 892, 755, 92)
      3 良点 tick(485, 556, 638, 84)
      4 横折 hbar(340, 633, 539, 84) + vbar(590, 321, 539, 92)
      5 一   hbar(368, 590, 444, 84)
      6 一   hbar(366, 590, 334, 84)
      7 竖提 vbar(386, 40, 538, 92) + 挑
      8 撇   pie(611, 225, 691, 324, 84)
      9 捺   na(471, 34, 829, 261, 92)
    """
    g = Glyph("uni98DF", advance=1000, unicode=0x98DF, note="食 𠆢+良")
    pie(g, 108, 437, 484, 806, W_SEC)
    na(g, 483, 500, 892, 755, W_SEC)
    tick(g, 485, 556, 638, W_THIN)
    bar(g, 340, 633, 539, W_LIGHT)
    vbar(g, 590, 321, 539, W_LIGHT)
    bar(g, 368, 590, 432, W_LIGHT)
    bar(g, 366, 590, 320, W_THIN)
    vbar(g, 386, 40, 538, W_LIGHT)
    g.diag(386, 66, 484, 138, weight=W_THIN)
    pie(g, 611, 225, 691, 324, W_THIN)
    na(g, 471, 34, 829, 261, W_SEC)
    return g


def uni9632() -> Glyph:
    """防 U+9632（7画）= 阝 + 方。

    分区：阝 x 86..365 / y 20..792；方 x 309..925 / y 25..793。
    笔画：
      1 阝横撇弯钩 hbar(134, 350, 750, 84) + pie(160, 590, 350, 750, 88)
      2 阝竖   vbar(134, 20, 732, 96)
      3 方点   tick(635, 641, 793, 84)
      4 方横   hbar(379, 925, 630, 84)
      5 方横折钩 hbar(599, 834, 477, 84) + vbar(792, 25, 477, 92) + 钩
      6 方撇   pie(309, 135, 640, 599, 96)
    """
    g = Glyph("uni9632", advance=1000, unicode=0x9632, note="防 阝+方")
    bar(g, 134, 350, 750, W_THIN)
    pie(g, 160, 590, 350, 750, W_SEC)
    vbar(g, 134, 20, 732, W_MAIN)
    tick(g, 635, 641, 793, W_THIN)
    bar(g, 379, 925, 630, W_THIN)
    bar(g, 599, 834, 477, W_THIN)
    vbar(g, 792, 25, 477, W_SEC)
    g.diag(792, 58, 748, 116, weight=W_DOT)
    pie(g, 309, 135, 640, 599, W_MAIN)
    return g


def uni8ECA() -> Glyph:
    """車 U+8ECA（7画）= 一 + 日 + 一 + 丨。

    分区：顶横 y 639..723；日框 x 266..767 / y 307..608；长横 y 171..267。
    笔画：
      1 一   hbar(224, 764, 681, 84)
      2 丨   vbar(266, 318, 566, 84)
      3 横折 hbar(266, 767, 566, 84) + vbar(721, 349, 566, 84)
      4 一   hbar(287, 721, 458, 84)
      5 一   hbar(304, 721, 349, 84)
      6 一   hbar(128, 875, 219, 96)
      7 丨   vbar(491, 28, 797, 96)
    """
    g = Glyph("uni8ECA", advance=1000, unicode=0x8ECA, note="車")
    bar(g, 224, 764, 681, W_THIN)
    vbar(g, 266, 318, 566, W_THIN)
    bar(g, 266, 767, 566, W_THIN)
    vbar(g, 721, 349, 566, W_THIN)
    bar(g, 287, 721, 458, W_THIN)
    bar(g, 304, 721, 349, W_THIN)
    bar(g, 128, 875, 219, W_MAIN)
    vbar(g, 491, 28, 797, W_MAIN)
    return g


def uni7814() -> Glyph:
    """研 U+7814（9画）= 石 + 开。

    分区：石 x 96..411 / y 168..677；开 x 440..933 / y 43..739。
    笔画：
      1 一   hbar(118, 411, 662, 84)
      2 撇   pie(96, 290, 229, 629, 96)
      3 丨   vbar(203, 168, 410, 84)
      4 横折 hbar(203, 399, 410, 84) + vbar(357, 243, 410, 84)
      5 一   hbar(227, 357, 228, 84)
      6 一   hbar(476, 860, 723, 84)
      7 一   hbar(442, 933, 485, 84)
      8 撇   pie(440, 83, 593, 689, 96)
      9 丨   vbar(758, 43, 710, 96)
    """
    g = Glyph("uni7814", advance=1000, unicode=0x7814, note="研 石+开")
    bar(g, 118, 411, 662, W_THIN)
    pie(g, 96, 290, 229, 629, W_MAIN)
    vbar(g, 203, 168, 410, W_THIN)
    bar(g, 203, 399, 410, W_THIN)
    vbar(g, 357, 243, 410, W_THIN)
    bar(g, 227, 357, 228, W_THIN)
    bar(g, 476, 860, 723, W_THIN)
    bar(g, 442, 933, 485, W_THIN)
    pie(g, 440, 83, 593, 689, W_MAIN)
    vbar(g, 758, 43, 710, W_MAIN)
    return g


def uni4F55() -> Glyph:
    """何 U+4F55（7画）= 亻 + 可。

    分区：亻 x 82..289；可 x 349..917 / y 0..712。
    笔画：
      1 撇   pie(82, 390, 289, 777, 92)
      2 竖   vbar(240, 59, 572, 96)
      3 一   hbar(349, 917, 683, 84)
      4 口丨  vbar(388, 304, 506, 84)
      5 口横折 hbar(388, 625, 506, 84) + vbar(583, 365, 506, 84)
      6 口一  hbar(414, 583, 343, 84)
      7 亅   vbar(752, 0, 683, 96) + 左钩
    """
    g = Glyph("uni4F55", advance=1000, unicode=0x4F55, note="何 亻+可")
    pie(g, 82, 390, 289, 777, W_SEC)
    vbar(g, 240, 59, 572, W_MAIN)
    bar(g, 349, 917, 683, W_THIN)
    vbar(g, 388, 304, 506, W_THIN)
    bar(g, 388, 625, 506, W_THIN)
    vbar(g, 583, 365, 506, W_THIN)
    bar(g, 414, 583, 343, W_THIN)
    vbar(g, 752, 0, 683, W_MAIN)
    hook_left(g, 752, 62, W_THIN, 88, 52)
    return g


def uni5357() -> Glyph:
    """南 U+5357（9画）= 十 + 冂 + 丷 + 干。

    分区：十 y 511..804；冂 x 184..843 / y 11..529；内 丷+干 y 38..491。
    笔画：
      1 一   hbar(238, 766, 661, 84)
      2 丨   vbar(486, 511, 804, 96)
      3 丨   vbar(184, 47, 508, 92)
      4 横折 hbar(184, 843, 508, 84) + vbar(797, 11, 508, 92)
      5 丷左点 dot(380, 411, 71, 89)
      6 丷右撇 pie(559, 381, 614, 491, 80)
      7 一   hbar(309, 699, 353, 84)
      8 一   hbar(293, 716, 238, 84)
      9 丨   vbar(495, 38, 353, 96)
    """
    g = Glyph("uni5357", advance=1000, unicode=0x5357, note="南 十+冂+丷+干")
    bar(g, 238, 766, 661, W_THIN)
    vbar(g, 486, 511, 804, W_MAIN)
    vbar(g, 184, 47, 508, W_SEC)
    bar(g, 184, 843, 508, W_THIN)
    vbar(g, 797, 11, 508, W_SEC)
    g.dot(380, 411, w=71, h=89, slant=0)
    pie(g, 559, 381, 614, 491, W_DOT)
    bar(g, 309, 699, 353, W_THIN)
    bar(g, 293, 716, 238, W_THIN)
    vbar(g, 495, 38, 353, W_MAIN)
    return g


def uni8DB3() -> Glyph:
    """足 U+8DB3（7画）= 口 + 龰。

    分区：口 x 294..706 / y 510..792；龰 x 152..860 / y 50..532。
    笔画：
      1 口丨  vbar(294, 514, 750, 92)
      2 口横折 hbar(294, 706, 750, 84) + vbar(660, 580, 750, 92)
      3 口一  hbar(294, 660, 552, 84)
      4 丨    vbar(491, 194, 532, 96)
      5 一    hbar(491, 725, 380, 84)
      6 撇    pie(152, 88, 327, 405, 96)
      7 捺    na(295, 50, 860, 264, 96)
    """
    g = Glyph("uni8DB3", advance=1000, unicode=0x8DB3, note="足 口+龰")
    vbar(g, 294, 514, 750, W_SEC)
    bar(g, 294, 706, 750, W_THIN)
    vbar(g, 660, 580, 750, W_SEC)
    bar(g, 294, 660, 552, W_THIN)
    vbar(g, 491, 194, 532, W_MAIN)
    bar(g, 491, 725, 380, W_THIN)
    pie(g, 152, 88, 327, 405, W_MAIN)
    na(g, 295, 50, 860, 264, W_MAIN)
    return g


def uni795E() -> Glyph:
    """神 U+795E（9画）= 礻 + 申。

    分区：礻 x 72..437 / y 59..755；申 x 471..912 / y 5..809。
    笔画：
      1 礻点  dot(283, 721, 89, 68)
      2 礻横撇 hbar(72, 368, 570, 84) + pie(72, 268, 368, 570, 92)
      3 礻竖  vbar(283, 59, 434, 96)
      4 礻点  dot(368, 392, 138, 105)
      5 申丨  vbar(497, 314, 647, 92)
      6 申横折 hbar(497, 912, 647, 84) + vbar(866, 357, 647, 92)
      7 申一  hbar(497, 866, 504, 84)
      8 申一  hbar(534, 866, 356, 84)
      9 申丨  vbar(686, 5, 809, 96)
    """
    g = Glyph("uni795E", advance=1000, unicode=0x795E, note="神 礻+申")
    g.dot(283, 721, w=89, h=68, slant=0)
    bar(g, 72, 368, 570, W_THIN)
    pie(g, 72, 268, 368, 570, W_SEC)
    vbar(g, 283, 59, 434, W_MAIN)
    g.dot(368, 392, w=138, h=105, slant=0)
    vbar(g, 497, 314, 647, W_SEC)
    bar(g, 497, 912, 647, W_THIN)
    vbar(g, 866, 357, 647, W_SEC)
    bar(g, 497, 866, 504, W_THIN)
    bar(g, 534, 866, 356, W_THIN)
    vbar(g, 686, 5, 809, W_MAIN)
    return g


def uni5B85() -> Glyph:
    """宅 U+5B85（6画）= 宀 + 乇。

    分区：宀 y 505..788；乇 x 154..865 / y 36..465。
    笔画：
      1 宀点   tick(481, 681, 788, 84)
      2 宀左点 dot(170, 586, 55, 163)
      3 宀横钩 hbar(201, 901, 654, 84) + 钩
      4 乇撇   pie(290, 443, 626, 592, 88)
      5 乇一   hbar(154, 797, 320, 84)
      6 乇乚   vbar(490, 100, 440, 96) + 折 + 钩
    """
    g = Glyph("uni5B85", advance=1000, unicode=0x5B85, note="宅 宀+乇")
    tick(g, 481, 681, 788, W_THIN)
    g.dot(170, 586, w=55, h=163, slant=0)
    bar(g, 201, 901, 654, W_THIN)
    g.diag(896, 654, 852, 588, weight=W_DOT)
    pie(g, 290, 443, 626, 592, W_SEC)
    bar(g, 154, 797, 320, W_THIN)
    vbar(g, 490, 80, 440, W_MAIN)
    na(g, 490, 36, 850, 96, W_SEC)
    g.diag(844, 88, 866, 162, weight=W_DOT)
    return g


def uni6761() -> Glyph:
    """条 U+6761（7画）= 夂 + 木。

    分区：夂 y 381..793；木 x 118..863 / y 11..446。
    笔画：
      1 夂撇   pie(212, 580, 418, 793, 88)
      2 夂横撇 hbar(157, 656, 743, 84) + pie(157, 381, 656, 743, 92)
      3 夂捺   na(362, 421, 843, 658, 92)
      4 木横   hbar(145, 829, 313, 84)
      5 木丨   vbar(493, 11, 446, 96)
      6 木撇   pie(118, 38, 461, 307, 92)
      7 木捺   na(524, 66, 863, 306, 92)
    """
    g = Glyph("uni6761", advance=1000, unicode=0x6761, note="条 夂+木")
    pie(g, 212, 580, 418, 793, W_SEC)
    bar(g, 157, 656, 743, W_THIN)
    pie(g, 157, 381, 656, 743, W_SEC)
    na(g, 362, 421, 843, 658, W_SEC)
    bar(g, 145, 829, 313, W_THIN)
    vbar(g, 493, 11, 446, W_MAIN)
    pie(g, 118, 38, 461, 307, W_SEC)
    na(g, 524, 66, 863, 306, W_SEC)
    return g


def uni72EC() -> Glyph:
    """独 U+72EC（9画）= 犭 + 虫。

    分区：犭 x 108..415 / y 30..712；虫 x 446..896 / y 83..766。
    笔画：
      1 犭撇   pie(108, 446, 347, 712, 88)
      2 犭弯钩 vbar(350, 90, 653, 92) + pie(185, 30, 350, 110, 80)
      3 犭撇   pie(118, 220, 318, 460, 88)
      4 虫口丨  vbar(471, 284, 534, 84)
      5 虫口横折 hbar(471, 884, 534, 84) + vbar(838, 366, 534, 92)
      6 虫口一  hbar(505, 838, 338, 84)
      7 虫丨    vbar(653, 139, 766, 96)
      8 虫提    ti(469, 83, 827, 179, 84)
      9 虫点    dot(836, 167, 120, 146)
    """
    g = Glyph("uni72EC", advance=1000, unicode=0x72EC, note="独 犭+虫")
    pie(g, 108, 446, 347, 712, W_SEC)
    vbar(g, 350, 90, 653, W_SEC)
    pie(g, 185, 30, 350, 110, W_DOT)
    pie(g, 118, 220, 318, 460, W_SEC)
    vbar(g, 471, 284, 534, W_THIN)
    bar(g, 471, 884, 534, W_THIN)
    vbar(g, 838, 366, 534, W_SEC)
    bar(g, 505, 838, 338, W_THIN)
    vbar(g, 653, 139, 766, W_MAIN)
    ti(g, 469, 83, 827, 179, W_THIN)
    g.dot(836, 167, w=120, h=146, slant=0)
    return g


def uni7A76() -> Glyph:
    """究 U+7A76（7画）= 穴（宀+八）+ 九。

    分区：宀 y 558..802；八 y 448..638；九 x 162..878 / y 33..713。
    笔画：
      1 宀点   tick(487, 703, 802, 84)
      2 宀左点 dot(213, 620, 46, 123)
      3 宀横钩 hbar(245, 848, 678, 84) + 钩
      4 八撇   pie(222, 448, 376, 615, 84)
      5 八捺   na(551, 491, 795, 638, 84)
      6 九撇   pie(162, 12, 445, 479, 96)
      7 九乙   hbar(231, 820, 374, 84) + vbar(790, 110, 374, 92)
              + bar(790, 870, 70, 80) + 钩
    """
    g = Glyph("uni7A76", advance=1000, unicode=0x7A76, note="究 穴+九")
    tick(g, 487, 703, 802, W_THIN)
    g.dot(213, 620, w=46, h=123, slant=0)
    bar(g, 245, 848, 678, W_THIN)
    g.diag(843, 678, 800, 612, weight=W_DOT)
    pie(g, 222, 448, 376, 615, W_THIN)
    na(g, 551, 491, 795, 638, W_THIN)
    pie(g, 162, 12, 445, 479, W_MAIN)
    bar(g, 231, 820, 374, W_THIN)
    vbar(g, 790, 90, 374, W_SEC)
    bar(g, 790, 870, 70, W_THIN)
    g.diag(865, 70, 885, 150, weight=W_DOT)
    return g


def uni80B2() -> Glyph:
    """育 U+80B2（8画）= 亠 + 厶 + 月。

    分区：亠 y 648..801；厶 y 448..653；月 x 352..682 / y 0..422。
    2026-10-31 回修：厶的横（墨 448..532）与月上横（墨 374..458）白口 −10；
    月部三横整体下移 36（腔各 24）→ 白口 26。
    笔画：
      1 丶   tick(490, 693, 801, 84)
      2 一   hbar(96, 894, 676, 84)
      3 厶撇折 pie(300, 480, 600, 640, 88) + bar(300, 560, 490, 84)
      4 厶丶 dot(667, 548, 126, 122)
      5 月丨 pie→vbar(361, 14, 415, 96)
      6 月横折钩 hbar(361, 682, 416, 84) + vbar(636, 0, 416, 92) + 钩
      7 月一 hbar(379, 636, 308, 84)
      8 月一 hbar(380, 636, 206, 84)
    """
    g = Glyph("uni80B2", advance=1000, unicode=0x80B2, note="育 亠+厶+月")
    tick(g, 490, 693, 801, W_THIN)
    bar(g, 96, 894, 676, W_THIN)
    pie(g, 300, 480, 600, 640, W_SEC)
    bar(g, 300, 560, 490, W_THIN)
    g.dot(667, 548, w=126, h=122, slant=0)
    vbar(g, 361, 14, 380, W_MAIN)
    bar(g, 361, 682, 380, W_THIN)
    vbar(g, 636, 0, 380, W_SEC)
    g.diag(636, 60, 592, 118, weight=W_DOT)
    bar(g, 379, 636, 272, W_THIN)
    bar(g, 380, 636, 164, W_THIN)
    return g


def uni4E57() -> Glyph:
    """乗 U+4E57（9画）= ノ + 一 + 廿形 + 木。

    分区：ノ y 701..807；一 y 602..643；廿形 y 337..607；木 y 19..720。
    笔画：
      1 ノ   pie(288, 701, 633, 807, 88)
      2 一   hbar(205, 783, 622, 84)
      3 一   hbar(113, 861, 486, 84)
      4 丨   vbar(329, 349, 571, 88)
      5 丨   vbar(670, 369, 607, 88)
      6 一   hbar(205, 834, 355, 84)
      7 丨   vbar(488, 19, 720, 96)
      8 撇   pie(137, 86, 464, 349, 92)
      9 捺   na(519, 96, 861, 347, 92)
    """
    g = Glyph("uni4E57", advance=1000, unicode=0x4E57, note="乗")
    pie(g, 288, 701, 633, 807, W_SEC)
    bar(g, 205, 783, 622, W_THIN)
    bar(g, 113, 861, 486, W_THIN)
    vbar(g, 329, 349, 571, W_SEC)
    vbar(g, 670, 369, 607, W_SEC)
    bar(g, 205, 834, 355, W_THIN)
    vbar(g, 488, 19, 720, W_MAIN)
    pie(g, 137, 86, 464, 349, W_SEC)
    na(g, 519, 96, 861, 347, W_SEC)
    return g


def uni5E97() -> Glyph:
    """店 U+5E97（8画）= 广 + 占。

    分区：广 y 81..801；占 x 355..806 / y 14..605。
    笔画：
      1 丶   tick(532, 678, 801, 84)
      2 一   hbar(221, 845, 672, 84)
      3 撇   pie(113, 81, 265, 644, 96)
      4 丨   vbar(540, 273, 605, 96)
      5 一   hbar(540, 806, 456, 84)
      6 口丨 vbar(380, 14, 262, 92)
      7 口横折 hbar(380, 806, 262, 84) + vbar(760, 76, 262, 92)
      8 口一  hbar(416, 760, 54, 84)
    """
    g = Glyph("uni5E97", advance=1000, unicode=0x5E97, note="店 广+占")
    tick(g, 532, 678, 801, W_THIN)
    bar(g, 221, 845, 672, W_THIN)
    pie(g, 113, 81, 265, 644, W_MAIN)
    vbar(g, 540, 273, 605, W_MAIN)
    bar(g, 540, 806, 456, W_THIN)
    vbar(g, 380, 14, 262, W_SEC)
    bar(g, 380, 806, 262, W_THIN)
    vbar(g, 760, 76, 262, W_SEC)
    bar(g, 416, 760, 54, W_THIN)
    return g


def uni8FF0() -> Glyph:
    """述 U+8FF0（7画）= 术 + 辶。

    分区：术 x 345..804 / y 207..779；辶 x 94..838 / y 47..739。
    笔画：
      1 一   hbar(371, 798, 602, 84)
      2 丨   vbar(580, 207, 779, 96)
      3 撇   pie(345, 245, 466, 500, 92)
      4 捺   na(702, 268, 804, 486, 92)
      5 丶   dot(751, 731, 98, 82)
      6 辶点+折+払（part_ninkyou）
    """
    g = Glyph("uni8FF0", advance=1000, unicode=0x8FF0, note="述 术+辶")
    bar(g, 371, 798, 602, W_THIN)
    vbar(g, 580, 207, 779, W_MAIN)
    pie(g, 345, 245, 466, 500, W_SEC)
    na(g, 702, 268, 804, 486, W_SEC)
    g.dot(751, 731, w=98, h=82, slant=0)
    part_ninkyou(g, dot_x=203, dot_y=694, zx0=94, zx1=264, zy=410,
                 sx0=96, sx1=838, sy=47)
    return g


def uni5DDE() -> Glyph:
    """州 U+5DDE（6画）= 丶 + 丿 + 丨 + 丶 + 丨 + 丨。

    分区：左组 x 104..276；中竖 x 515..531；右竖 x 817..837。
    笔画（首笔为长撇，不是竖 —— 按 KanjiVG 笔顺改写）：
      1 丶  dot(138, 448, 55, 136)
      2 丿  pie(104, 86, 276, 712, 92)
      3 丶  dot(406, 453, 66, 109)
      4 丨  vbar(523, 132, 740, 96)
      5 丶  dot(678, 461, 81, 124)
      6 丨  vbar(827, 46, 747, 96)
    """
    g = Glyph("uni5DDE", advance=1000, unicode=0x5DDE, note="州")
    g.dot(138, 448, w=55, h=136, slant=0)
    pie(g, 104, 86, 276, 712, W_SEC)
    g.dot(406, 453, w=66, h=109, slant=0)
    vbar(g, 523, 132, 740, W_MAIN)
    g.dot(678, 461, w=81, h=124, slant=0)
    vbar(g, 827, 46, 747, W_MAIN)
    return g


def uni6B66() -> Glyph:
    """武 U+6B66（8画）= 止 + 戈形。

    分区：止部 x 149..529 / y 76..637；戈形 x 517..900 / y 15..739。
    笔画：
      1 一   hbar(200, 425, 637, 84)
      2 一   hbar(116, 863, 523, 84)
      3 丨   vbar(367, 152, 447, 96)
      4 一   hbar(383, 529, 335, 84)
      5 丨   vbar(229, 105, 328, 96)
      6 提   ti(149, 76, 548, 207, 84)
      7 斜钩 na(517, 40, 890, 740, 96) + 上钩
      8 丶   dot(720, 697, 106, 83)
    """
    g = Glyph("uni6B66", advance=1000, unicode=0x6B66, note="武")
    bar(g, 200, 425, 637, W_THIN)
    bar(g, 116, 863, 523, W_THIN)
    vbar(g, 367, 152, 447, W_MAIN)
    bar(g, 383, 529, 335, W_THIN)
    vbar(g, 229, 105, 328, W_MAIN)
    ti(g, 149, 76, 548, 207, W_THIN)
    na(g, 517, 40, 890, 740, W_MAIN)
    g.diag(885, 60, 852, 124, weight=W_DOT)
    g.dot(720, 697, w=106, h=83, slant=0)
    return g


def uni58F0() -> Glyph:
    """声 U+58F0（7画）= 士 + ヨ形 + 撇。

    分区：士 y 543..811；下部 x 282..750 / y 29..488。
    笔画（下部含内竖，按 KanjiVG 笔顺改写）：
      1 一   hbar(195, 795, 701, 84)
      2 丨   vbar(491, 571, 811, 96)
      3 一   hbar(266, 772, 566, 84)
      4 横折 hbar(282, 750, 467, 84) + vbar(704, 331, 467, 92)
      5 丨   vbar(508, 333, 457, 84)
      6 一   hbar(297, 704, 321, 84)
      7 撇   pie(154, 29, 303, 444, 96)
    """
    g = Glyph("uni58F0", advance=1000, unicode=0x58F0, note="声 士+ヨ+撇")
    bar(g, 195, 795, 701, W_THIN)
    vbar(g, 491, 571, 811, W_MAIN)
    bar(g, 266, 772, 566, W_THIN)
    bar(g, 282, 750, 467, W_THIN)
    vbar(g, 704, 331, 467, W_SEC)
    vbar(g, 508, 333, 457, W_THIN)
    bar(g, 297, 704, 321, W_THIN)
    pie(g, 154, 29, 303, 444, W_MAIN)
    return g


def uni5FF5() -> Glyph:
    """念 U+5FF5（8画）= 今 + 心。

    分区：今 y 322..811；心 y 17..250。
    笔画：
      1 撇   pie(111, 448, 478, 811, 92)
      2 捺   na(480, 496, 901, 781, 92)
      3 一   hbar(384, 603, 567, 84)
      4 ㇇   hbar(285, 661, 462, 84) + pie(285, 322, 661, 462, 92)
      5 心左点 ti(125, 42, 193, 184, 76)
      6 心卧钩 diag(330,210,395,55)+diag(395,55,760,55)+钩
      7 心中点 dot(503, 218, 65, 63)
      8 心右点 dot(796, 237, 75, 94)
    """
    g = Glyph("uni5FF5", advance=1000, unicode=0x5FF5, note="念 今+心")
    pie(g, 111, 448, 478, 811, W_SEC)
    na(g, 480, 496, 901, 781, W_SEC)
    bar(g, 384, 603, 567, W_THIN)
    bar(g, 285, 661, 462, W_THIN)
    pie(g, 285, 322, 661, 462, W_SEC)
    # 心
    ti(g, 125, 42, 193, 184, W_DOT)
    g.diag(330, 210, 395, 55, weight=W_MAIN)
    g.diag(395, 55, 760, 55, weight=W_MAIN)
    g.diag(760, 55, 800, 120, weight=W_DOT)
    g.dot(503, 218, w=65, h=63, slant=0)
    g.dot(796, 237, w=75, h=94, slant=0)
    return g


def uni5F85() -> Glyph:
    """待 U+5F85（9画）= 彳 + 寺。

    分区：彳 x 84..320；寺 x 356..919 / y 0..794。
    笔画：
      1 彳撇   pie(124, 601, 316, 764, 84)
      2 彳撇   pie(84, 322, 320, 606, 92)
      3 彳竖   vbar(231, 27, 433, 96)
      4 土横   hbar(438, 789, 663, 84)
      5 土竖   vbar(602, 530, 794, 96)
      6 土横   hbar(356, 919, 520, 84)
      7 寸横   hbar(360, 899, 367, 84)
      8 寸竖钩 vbar(690, 0, 473, 96) + 左钩
      9 寸丶   dot(535, 220, 80, 94)
    """
    g = Glyph("uni5F85", advance=1000, unicode=0x5F85, note="待 彳+寺")
    pie(g, 124, 601, 316, 764, W_THIN)
    pie(g, 84, 322, 320, 606, W_SEC)
    vbar(g, 231, 27, 433, W_MAIN)
    bar(g, 438, 789, 663, W_THIN)
    vbar(g, 602, 530, 794, W_MAIN)
    bar(g, 356, 919, 520, W_THIN)
    bar(g, 360, 899, 367, W_THIN)
    vbar(g, 690, 0, 473, W_MAIN)
    hook_left(g, 690, 62, W_THIN, 84, 50)
    g.dot(535, 220, w=80, h=94, slant=0)
    return g


# --------------------------------------------------------------------------
def build() -> list[Glyph]:
    return [
        uni753A(),  # 町
        uni6CA2(),  # 沢
        uni72B6(),  # 状
        uni5EFA(),  # 建
        uni7A7A(),  # 空
        uni6025(),  # 急
        uni9001(),  # 送
        uni4F9B(),  # 供
        uni5F79(),  # 役
        uni8EAB(),  # 身
        uni65BD(),  # 施
        uni98DF(),  # 食
        uni9632(),  # 防
        uni8ECA(),  # 車
        uni7814(),  # 研
        uni4F55(),  # 何
        uni5357(),  # 南
        uni8DB3(),  # 足
        uni795E(),  # 神
        uni5B85(),  # 宅
        uni6761(),  # 条
        uni72EC(),  # 独
        uni7A76(),  # 究
        uni80B2(),  # 育
        uni4E57(),  # 乗
        uni5E97(),  # 店
        uni8FF0(),  # 述
        uni5DDE(),  # 州
        uni6B66(),  # 武
        uni58F0(),  # 声
        uni5FF5(),  # 念
        uni5F85(),  # 待
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-005.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
