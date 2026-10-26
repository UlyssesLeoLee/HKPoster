"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-011。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
* 字面框 x 60..940 / y 0..820，与繁体汉字同一档，advance 一律 1000，
  便于中英日混排时基线与字面一致。
* 笔画权重：主 96 / 次 92 / 细 84 / 点 84。6 画字以 96 为主；
  8–9 画字在拥挤处（内部横叠、竖并）降到 84/92，
  避免同批内出现"有的太轻、有的太闷"（GLY-001 允许小空腔局部减重）。
* 端点（海报端点）：横竖撇捺一律平切硬边（butt cut，无圆角无收锋）；
  只有点与短撇用斜切平行四边形 g.dot()，斜切分档见 SLANT_* 常量，
  同类部件同族同档（GLY-004），斜切不用于任何笔画的主体（GLY-003）。
* 骨架：照 Jōyō 标准骨架画，只改笔画设计（重量、端点处理、转角、
  记号字面与粗细、落位与大小），不改任何一条笔画的方向/角度。
  同码位不同形（例：单 / 単）以 Jōyō 形为准。
* 部件复用：亻 / 扌 / 氵 / 木 / 辶 / 阝 / 宀 在批内用同一套比例拆法，
  由 box 参数做位置与大小的光学校正（docs/03 GLY-004）。
* 内白：横叠横的内白 ≥ 24 单位，竖与竖之间 ≥ 60 单位（GLY-006）。
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
BASE = 0.0
LEFT = 60.0
RIGHT = 940.0

# 斜切分档（只用于点 / 短撇 / 记号）。同族同档，见 GLY-004。
SLANT_DOT = -26      # 丶：右下走向的标准点
SLANT_DOT_SM = -20   # 半高点
SLANT_SHORT = 26     # 短撇：左下走向
SLANT_MARK = 18      # 记号
SLANT_MARK_SM = 14   # 小记号


# ------------------------------------------------------------------ 部件 helper
# 所有 helper 用 box（x0,x1,y0,y1）定位，批内复用同一套笔画拆法。

def _ninben(g, x0, x1, y0=BASE, y1=TOP):
    """亻：撇 + 竖。批内统一拆法（依 / 伴 / 仲 / 似 / 併）。"""
    span = x1 - x0
    height = y1 - y0
    g.diag(x0 + 0.42 * span, y1 - 0.04 * height,
           x0 + 0.12 * span, y1 - 0.44 * height, W_THIN)
    g.vbar(x0 + 0.30 * span, y0, y1 - 0.22 * height, W_MAIN)


def _tehen(g, x0, x1, y0=BASE, y1=TOP):
    """扌：横 + 竖 + 提。批内统一拆法（抱 / 折）。"""
    span = x1 - x0
    height = y1 - y0
    g.hbar(x0, x0 + 0.84 * span, y1 - 0.22 * height, W_MAIN)
    g.vbar(x0 + 0.40 * span, y0, y1 - 0.10 * height, W_MAIN)
    g.diag(x0 + 0.09 * span, y1 - 0.62 * height,
           x0 + 0.78 * span, y1 - 0.46 * height, W_THIN)


def _sanzui(g, x0, x1, y0=BASE, y1=TOP):
    """氵：两点 + 一提。批内统一拆法（汚 / 沖）。"""
    span = x1 - x0
    height = y1 - y0
    g.dot(x0 + 0.55 * span, y1 - 0.12 * height, W_DOT, 104, SLANT_DOT)
    g.dot(x0 + 0.32 * span, y1 - 0.38 * height, W_DOT, 104, SLANT_DOT)
    g.diag(x0 + 0.14 * span, y0 + 0.28 * height,
           x0 + 0.95 * span, y0 + 0.42 * height, W_THIN)


def _moya(g, x0, x1, y0=BASE, y1=TOP):
    """木：横 + 竖 + 撇 + 捺。批内统一拆法（枚 / 板 / 枠 / 栄）。"""
    span = x1 - x0
    height = y1 - y0
    g.hbar(x0, x1, y1 - 0.22 * height, W_MAIN)
    g.vbar(x0 + 0.50 * span, y0, y1 - 0.05 * height, W_MAIN)
    g.diag(x0 + 0.50 * span, y1 - 0.25 * height,
           x0 + 0.13 * span, y0 + 0.16 * height, W_THIN)
    g.diag(x0 + 0.50 * span, y1 - 0.25 * height,
           x0 + 0.88 * span, y0 + 0.16 * height, W_THIN)


def _henka(g, x0=LEFT, x1=380.0, y0=BASE, y1=TOP):
    """辶：点 + 横折折撇 + 平捺（下降段 + 平走段）。批内统一拆法（逃 / 迷）。"""
    span = x1 - x0
    height = y1 - y0
    g.dot(x0 + 0.45 * span, y1 - 0.07 * height, W_DOT, 96, SLANT_DOT)
    g.hbar(x0 + 0.28 * span, x0 + 0.86 * span, y1 - 0.27 * height, W_THIN)
    g.diag(x0 + 0.80 * span, y1 - 0.27 * height,
           x0 + 0.42 * span, y1 - 0.60 * height, W_THIN)
    g.diag(x0 + 0.42 * span, y1 - 0.60 * height,
           x0 + 1.32 * span, y0 + 0.06 * height, W_MAIN)
    g.hbar(x0 + 1.32 * span, RIGHT, y0 + 0.06 * height, W_MAIN)


def _ears(g, x0, x1, y0=BASE, y1=TOP):
    """阝（右耳旁）：竖 + 折碗。批内统一拆法（邸 / 郡）。"""
    span = x1 - x0
    height = y1 - y0
    g.vbar(x0 + 0.12 * span, y0, y1 - 0.03 * height, W_MAIN)
    g.hbar(x0, x0 + 0.78 * span, y1 - 0.07 * height, W_THIN)
    g.diag(x0 + 0.72 * span, y1 - 0.08 * height,
           x0 + 0.36 * span, y1 - 0.28 * height, W_THIN)
    g.diag(x0 + 0.36 * span, y1 - 0.26 * height,
           x0 + 0.70 * span, y1 - 0.46 * height, W_THIN)
    g.diag(x0 + 0.70 * span, y1 - 0.46 * height,
           x0 + 0.42 * span, y1 - 0.52 * height, W_THIN)


# ------------------------------------------------------------------ 字形函数

def _g_hou():
    """抱 = ⿰扌包。
    扌：横(60..304,y640) 竖(x176) 提(86,312→286,443)。
    包：勹 = 撇(480,780→395,580) + 横折钩(横480..936 y768 / 竖x890 / 钩)。
        巳 = 横折(横545..800 y600 + 竖x754) + 中横(y470) + 竖弯钩(竖x591 + 底横 + 上钩)。
    """
    g = Glyph("uni62B1", advance=1000, unicode=0x62B1, note="抱：扌 + 包")
    _tehen(g, 60.0, 350.0)
    # 勹
    g.diag(480, 780, 395, 580, W_THIN)
    g.hbar(480, 936, 768, W_SEC)
    g.vbar(890, 768, 300, W_SEC)
    g.diag(890, 310, 795, 385, W_THIN)
    # 巳
    g.hbar(545, 800, 600, W_SEC)
    g.vbar(754, 470, 600, W_SEC)
    g.hbar(545, 754, 470, W_SEC)
    g.vbar(591, 250, 470, W_SEC)
    g.hbar(545, 754, 250, W_SEC)
    g.vbar(754, 330, 250, W_THIN)
    return g


def _g_fuku():
    """服 = ⿰月𠬝。
    月：撇(150,800→112,40) 横折钩(横145..350 y774 + 竖x304 + 钩) + 内二横(y560/y340)。
    𠬝：卩(竖x455 + 横折钩横413..660 y700 + 竖x618 + 钩) + 又(横撇 y380 + 撇 + 捺)。
    """
    g = Glyph("uni670D", advance=1000, unicode=0x670D, note="服：月 + 𠬝")
    # 月
    g.diag(150, 800, 112, 40, W_SEC)
    g.hbar(150, 350, 774, W_SEC)
    g.vbar(304, 120, 774, W_SEC)
    g.diag(304, 130, 234, 200, W_THIN)
    g.hbar(130, 304, 560, W_THIN)
    g.hbar(130, 304, 340, W_THIN)
    # 卩
    g.vbar(455, 520, 700, W_THIN)
    g.hbar(413, 660, 700, W_THIN)
    g.vbar(618, 520, 700, W_THIN)
    g.diag(618, 530, 530, 600, W_THIN)
    # 又
    g.hbar(620, 900, 380, W_THIN)
    g.diag(880, 380, 680, 40, W_THIN)
    g.diag(630, 380, 895, 40, W_THIN)
    return g


def _g_bi():
    """尾 = ⿸尸毛。
    尸：横折(横166..896 y722 + 竖x878) + 中横(y492) + 撇(218,697→86,41)。
    毛：撇(428,508→270,410) + 横(y344) + 横(y230) + 竖弯钩(竖x324 + 底走 y41)。
    """
    g = Glyph("uni5C3E", advance=1000, unicode=0x5C3E, note="尾：尸 + 毛")
    # 尸
    g.hbar(166, 896, 722, W_SEC)
    g.vbar(878, 344, 722, W_SEC)
    g.hbar(192, 878, 492, W_SEC)
    g.diag(218, 697, 86, 41, W_SEC)
    # 毛
    g.diag(428, 508, 270, 410, W_THIN)
    g.hbar(254, 658, 344, W_THIN)
    g.hbar(306, 606, 230, W_THIN)
    g.vbar(324, 41, 369, W_SEC)
    g.hbar(324, 720, 41, W_SEC)
    return g


def _g_tera():
    """寺 = ⿱士寸。
    士：横(150..850 y760) + 竖(x500) + 短横(280..720 y640)。
    寸：长横(100..900 y470) + 竖钩(x700 + 钩) + 点(400,330)。
    """
    g = Glyph("uni5BFA", advance=1000, unicode=0x5BFA, note="寺：士 + 寸")
    g.hbar(150, 850, 760, W_MAIN)
    g.vbar(500, 620, 780, W_MAIN)
    g.hbar(280, 720, 640, W_SEC)
    g.hbar(100, 900, 470, W_MAIN)
    g.vbar(700, 330, 640, W_MAIN)
    g.diag(700, 340, 615, 420, W_THIN)
    g.dot(400, 330, W_DOT, 100, SLANT_DOT)
    return g


def _g_u():
    """宇 = ⿱宀于。
    宀：点(540,800) + 左短竖(x215) + 横(215..880 y740) + 右斜钩。
    于：短横(380..660 y480) + 长横(300..740 y330) + 竖钩(x520 + 钩)。
    """
    g = Glyph("uni5B87", advance=1000, unicode=0x5B87, note="宇：宀 + 于")
    g.dot(540, 800, W_DOT, 96, SLANT_DOT)
    g.vbar(215, 640, 740, W_THIN)
    g.hbar(215, 880, 740, W_THIN)
    g.diag(870, 740, 810, 660, W_THIN)
    g.hbar(380, 660, 480, W_SEC)
    g.hbar(300, 740, 330, W_SEC)
    g.vbar(520, 150, 480, W_MAIN)
    g.diag(520, 160, 440, 240, W_THIN)
    return g


def _g_ban():
    """伴 = ⿰亻半。
    亻：批内统一拆法(box 60..340)。
    半：丷两点(540,750 / 790,750) + 短横(y620) + 长横(y480) + 竖(x660)。
    """
    g = Glyph("uni4F34", advance=1000, unicode=0x4F34, note="伴：亻 + 半")
    _ninben(g, 60.0, 340.0)
    g.dot(540, 752, W_DOT, 96, SLANT_DOT)
    g.dot(790, 752, W_DOT, 96, SLANT_SHORT)
    g.hbar(500, 820, 620, W_THIN)
    g.hbar(440, 880, 480, W_SEC)
    g.vbar(660, 60, 620, W_MAIN)
    return g


def _g_modosu():
    """戻 = ⿱戸大。
    戸：顶横(360..700 y774) + 横折(横180..900 y640 + 竖x854) + 中横(y500) + 撇(215,665→120,350)。
    大：横(140..880 y330) + 撇(520,330→175,45) + 捺(500,330→860,45)。
    """
    g = Glyph("uni623B", advance=1000, unicode=0x623B, note="戻：戸 + 大")
    g.hbar(360, 700, 774, W_SEC)
    g.hbar(215, 900, 640, W_SEC)
    g.vbar(854, 420, 640, W_SEC)
    g.hbar(215, 854, 500, W_SEC)
    g.diag(215, 665, 120, 350, W_SEC)
    g.hbar(140, 880, 330, W_SEC)
    g.diag(520, 330, 175, 45, W_SEC)
    g.diag(500, 330, 860, 45, W_SEC)
    return g


def _g_ki():
    """希 = ⿱乂布。
    乂：撇(620,780→330,580) + 捺(350,790→690,580)。
    布：一(y430) + 撇(330,520→140,390) + 巾(左竖x390 / 横折横390..760 y340 + 右竖x718 / 中竖x575)。
    """
    g = Glyph("uni5E0C", advance=1000, unicode=0x5E0C, note="希：乂 + 布")
    g.diag(620, 780, 330, 580, W_THIN)
    g.diag(350, 790, 690, 580, W_THIN)
    g.hbar(110, 880, 430, W_SEC)
    g.diag(330, 520, 140, 390, W_THIN)
    g.vbar(390, 40, 380, W_THIN)
    g.hbar(390, 760, 340, W_THIN)
    g.vbar(718, 40, 340, W_THIN)
    g.vbar(575, 0, 430, W_MAIN)
    return g


def _g_kei():
    """契 = ⿱𠔉大（𠔉 = 丰 + 刀）。
    丰：横(y760/y660/y560) + 竖(x255)。
    刀：横折钩(横500..936 y700 + 竖x890 + 钩) + 撇(760,700→520,560)。
    大：横(120..900 y380) + 撇(520,380→175,45) + 捺(500,380→860,45)。
    """
    g = Glyph("uni5951", advance=1000, unicode=0x5951, note="契：丰 + 刀 + 大")
    g.hbar(60, 420, 760, W_THIN)
    g.hbar(80, 430, 660, W_THIN)
    g.hbar(100, 440, 560, W_THIN)
    g.vbar(255, 480, 800, W_THIN)
    g.hbar(500, 936, 700, W_THIN)
    g.vbar(890, 560, 700, W_THIN)
    g.diag(890, 570, 800, 640, W_THIN)
    g.diag(760, 700, 520, 560, W_THIN)
    g.hbar(120, 900, 380, W_SEC)
    g.diag(520, 380, 175, 45, W_SEC)
    g.diag(500, 380, 860, 45, W_SEC)
    return g


def _g_tei():
    """邸 = ⿰氐阝。
    氐：撇(230,790→120,700) + 竖提(竖x200 + 提) + 一(y520) + 斜钩(260,720→520,140 + 钩) + 底一(y70)。
    阝：批内统一拆法(box 660..940)。
    """
    g = Glyph("uni90B8", advance=1000, unicode=0x90B8, note="邸：氐 + 阝")
    g.diag(230, 790, 120, 700, W_THIN)
    g.vbar(200, 66, 760, W_SEC)
    g.diag(200, 86, 300, 176, W_THIN)
    g.hbar(150, 480, 520, W_THIN)
    g.diag(260, 720, 520, 140, W_SEC)
    g.diag(520, 150, 460, 230, W_THIN)
    g.hbar(120, 540, 70, W_THIN)
    _ears(g, 660.0, 940.0)
    return g


def _g_i():
    """依 = ⿰亻衣。
    亻：批内统一拆法(box 60..340)。
    衣：点(560,790) + 一(y660) + 撇(740,650→450,330) + 竖提(竖x600 + 提) + 撇(760,430→560,180) + 捺(560,400→880,60)。
    """
    g = Glyph("uni4F9D", advance=1000, unicode=0x4F9D, note="依：亻 + 衣")
    _ninben(g, 60.0, 340.0)
    g.dot(560, 790, W_DOT, 96, SLANT_DOT)
    g.hbar(400, 880, 660, W_THIN)
    g.diag(740, 650, 450, 330, W_THIN)
    g.vbar(600, 100, 640, W_SEC)
    g.diag(600, 110, 720, 210, W_THIN)
    g.diag(760, 430, 560, 180, W_THIN)
    g.diag(560, 400, 880, 60, W_THIN)
    return g


def _g_o():
    """汚 = ⿰氵亏。
    氵：批内统一拆法(box 60..330)。
    亏：顶一(y760) + 折横(y620) + 竖(x516) + 底横(y380)。
    """
    g = Glyph("uni6C5A", advance=1000, unicode=0x6C5A, note="汚：氵 + 亏")
    _sanzui(g, 60.0, 330.0)
    g.hbar(560, 800, 760, W_THIN)
    g.hbar(470, 900, 620, W_THIN)
    g.vbar(516, 380, 620, W_THIN)
    g.hbar(474, 860, 380, W_THIN)
    return g


def _g_mai():
    """枚 = ⿰木攵。
    木：批内统一拆法(box 60..420)。
    攵：撇(700,780→520,620) + 横(y660) + 撇(780,660→490,100) + 捺(520,640→900,90)。
    """
    g = Glyph("uni679A", advance=1000, unicode=0x679A, note="枚：木 + 攵")
    _moya(g, 60.0, 420.0)
    g.diag(700, 780, 520, 620, W_THIN)
    g.hbar(480, 900, 660, W_THIN)
    g.diag(780, 660, 490, 100, W_THIN)
    g.diag(520, 640, 895, 90, W_THIN)
    return g


def _g_soku():
    """束 = ⿳木口（口居中，竖穿口心）。
    顶横(120..880 y700) + 中竖(x482) + 口(左竖x254 / 横折横254..694 y440 + 右竖x694 / 底横y260) + 撇 + 捺。
    """
    g = Glyph("uni675F", advance=1000, unicode=0x675F, note="束：木 + 口")
    g.hbar(120, 880, 700, W_SEC)
    g.vbar(482, 25, 754, W_MAIN)
    g.vbar(254, 260, 440, W_THIN)
    g.hbar(254, 694, 440, W_THIN)
    g.vbar(694, 260, 440, W_THIN)
    g.hbar(254, 694, 260, W_THIN)
    g.diag(394, 262, 104, 16, W_THIN)
    g.diag(588, 262, 896, 16, W_THIN)
    return g


def _g_chu():
    """仲 = ⿰亻中。
    亻：批内统一拆法(box 60..340)。
    中：口(左竖x460 / 横折横460..940 y620 + 右竖x898 / 底横y240) + 中竖(x700)。
    """
    g = Glyph("uni4EF2", advance=1000, unicode=0x4EF2, note="仲：亻 + 中")
    _ninben(g, 60.0, 340.0)
    g.vbar(460, 240, 620, W_THIN)
    g.hbar(460, 940, 620, W_THIN)
    g.vbar(898, 240, 620, W_THIN)
    g.hbar(460, 898, 240, W_THIN)
    g.vbar(700, 0, 700, W_MAIN)
    return g


def _g_ei():
    """栄 = ⿱⿱ツ冖木。
    ツ：点(240,730) + 点(420,730) + 撇(830,790→600,590)。
    冖：左短竖(x200) + 横(y620) + 右斜钩（墨 578..662）。
    木：批内统一拆法，但**只占下半**（box 100..900 × 0..520）——
    原来的 _moya(100, 900) 用满了 0..820，木的横落在 639.6（墨 591.6..687.6），
    与冖的横（墨 578..662）**叠了 70 单位**，两横糊成一条粗横
    （check_stroke_gaps 等效重叠 6.98，远超 3 的粘连阈值）。
    现在木的横落在 405.6（墨 357.6..453.6），与冖的横留 124 单位白口 ✓。
    """
    g = Glyph("uni6804", advance=1000, unicode=0x6804, note="栄：ツ + 冖 + 木")
    g.dot(250, 740, W_DOT, 96, SLANT_DOT)
    g.dot(430, 740, W_DOT, 96, SLANT_DOT)
    g.diag(830, 790, 600, 590, W_THIN)
    g.vbar(200, 540, 620, W_THIN)
    g.hbar(200, 900, 620, W_THIN)
    g.diag(880, 620, 820, 540, W_THIN)
    _moya(g, 100.0, 900.0, 0.0, 520.0)
    return g


def _g_waku():
    """枠 = ⿰木卆（卆 = 九 + 十）。
    木：批内统一拆法(box 60..420)。
    九：横折弯钩(横500..820 y730 + 竖x778 + 底走y460 + 钩) + 撇(620,790→480,590)。
    十：横(y300) + 竖(x700)。
    """
    g = Glyph("uni67A0", advance=1000, unicode=0x67A0, note="枠：木 + 卆")
    _moya(g, 60.0, 420.0)
    g.hbar(500, 820, 730, W_THIN)
    g.vbar(778, 460, 730, W_THIN)
    g.hbar(778, 900, 460, W_THIN)
    g.vbar(858, 460, 550, W_THIN)
    g.diag(620, 790, 480, 590, W_THIN)
    g.hbar(480, 940, 300, W_THIN)
    g.vbar(700, 40, 320, W_THIN)
    return g


def _g_ni():
    """似 = ⿰亻以。
    亻：批内统一拆法(box 60..340)。
    以：竖提(竖x470 + 提470,330→550,395) + 点(720,730) + 撇(760,670→600,150) + 捺(760,670→895,140)。
    """
    g = Glyph("uni4F3C", advance=1000, unicode=0x4F3C, note="似：亻 + 以")
    _ninben(g, 60.0, 340.0)
    g.vbar(470, 320, 700, W_THIN)
    g.diag(470, 330, 550, 395, W_THIN)
    g.dot(720, 730, W_DOT, 96, SLANT_DOT)
    g.diag(760, 670, 600, 150, W_THIN)
    g.diag(760, 670, 895, 140, W_THIN)
    return g


def _g_ita():
    """板 = ⿰木反。
    木：批内统一拆法(box 60..420)。
    反：厂(横470..940 y750 + 撇520,755→465,420) + 又(横撇横600..900 y470 + 撇880,470→660,120 + 捺610,470→900,120)。
    """
    g = Glyph("uni677F", advance=1000, unicode=0x677F, note="板：木 + 反")
    _moya(g, 60.0, 420.0)
    g.hbar(470, 940, 750, W_THIN)
    g.diag(520, 755, 465, 420, W_THIN)
    g.hbar(600, 900, 470, W_THIN)
    g.diag(880, 470, 660, 120, W_THIN)
    g.diag(610, 470, 895, 120, W_THIN)
    return g


def _g_retsu():
    """列 = ⿰歹刂。
    歹：一(y760) + 夕(撇330,730→230,520 + 横撇横280..520 y560 + 撇500,560→260,200 + 点330,400)。
    刂：短竖(x700) + 长竖钩(x894 + 钩)。
    """
    g = Glyph("uni5217", advance=1000, unicode=0x5217, note="列：歹 + 刂")
    g.hbar(80, 560, 760, W_THIN)
    g.diag(330, 730, 230, 520, W_THIN)
    g.hbar(280, 520, 560, W_THIN)
    g.diag(500, 560, 260, 200, W_THIN)
    g.dot(330, 400, W_DOT, 96, SLANT_DOT)
    g.vbar(700, 380, 640, W_THIN)
    g.vbar(894, 100, 740, W_SEC)
    g.diag(894, 110, 814, 180, W_THIN)
    return g


def _g_chu2():
    """沖 = ⿰氵中。
    氵：批内统一拆法(box 60..330)。
    中：口(左竖x430 / 横折横430..940 y620 + 右竖x898 / 底横y240) + 中竖(x685)。
    """
    g = Glyph("uni6C96", advance=1000, unicode=0x6C96, note="沖：氵 + 中")
    _sanzui(g, 60.0, 330.0)
    g.vbar(430, 240, 620, W_THIN)
    g.hbar(430, 940, 620, W_THIN)
    g.vbar(898, 240, 620, W_THIN)
    g.hbar(430, 898, 240, W_THIN)
    g.vbar(685, 0, 700, W_MAIN)
    return g


def _g_nigete():
    """逃 = ⿺辶兆。
    辶：批内统一拆法。
    兆：中撇(640,790→590,380 + 左下撇) + 中竖弯钩(x700 + 底走 y340 + 钩) + 左二点 + 右二点。
    """
    g = Glyph("uni9003", advance=1000, unicode=0x9003, note="逃：辶 + 兆")
    _henka(g, 60.0, 380.0)
    g.diag(640, 790, 590, 400, W_THIN)
    g.diag(590, 400, 480, 300, W_THIN)
    g.vbar(700, 340, 790, W_THIN)
    g.hbar(700, 840, 340, W_THIN)
    g.vbar(798, 340, 440, W_THIN)
    g.dot(450, 700, W_DOT, 96, SLANT_DOT)
    g.dot(430, 540, W_DOT, 96, SLANT_DOT)
    g.dot(860, 700, W_DOT, 96, SLANT_DOT)
    g.dot(880, 540, W_DOT, 96, SLANT_DOT)
    return g


def _g_itte():
    """届 = ⿸尸由。
    尸：横折(横180..940 y774 + 竖x894) + 中横(y580) + 撇(180,790→110,380)。
    由：口(左竖x322 / 横折横280..830 y460 + 右竖x788 / 底横y90) + 中横(y270) + 中竖(x555)。
    """
    g = Glyph("uni5C4A", advance=1000, unicode=0x5C4A, note="届：尸 + 由")
    g.hbar(180, 940, 774, W_SEC)
    g.vbar(894, 520, 774, W_SEC)
    g.hbar(180, 894, 580, W_SEC)
    g.diag(180, 790, 110, 380, W_SEC)
    g.vbar(322, 90, 460, W_THIN)
    g.hbar(280, 830, 460, W_THIN)
    g.vbar(788, 90, 460, W_THIN)
    g.hbar(280, 788, 90, W_THIN)
    g.hbar(280, 788, 270, W_THIN)
    g.vbar(555, 60, 500, W_SEC)
    return g


def _g_me():
    """迷 = ⿺辶米。
    辶：批内统一拆法。
    米：丷两点(520,760 / 790,760) + 一(y560) + 竖(x660) + 撇(660,560→450,230) + 捺(660,560→880,230)。
    """
    g = Glyph("uni8FF7", advance=1000, unicode=0x8FF7, note="迷：辶 + 米")
    _henka(g, 60.0, 380.0)
    g.dot(520, 760, W_DOT, 96, SLANT_DOT)
    g.dot(790, 760, W_DOT, 96, SLANT_SHORT)
    g.hbar(430, 900, 560, W_THIN)
    g.vbar(660, 200, 700, W_MAIN)
    g.diag(660, 560, 450, 230, W_THIN)
    g.diag(660, 560, 880, 230, W_THIN)
    return g


def _g_maki():
    """巻 = ⿱龹己。
    龹：丷两点(370,780 / 630,780) + 短横(y690) + 长横(y570) + 撇(500,570→200,380) + 捺(500,570→860,380)。
    己：横折(横200..760 y330 + 竖x714) + 中横(y200) + 竖弯钩(竖x246 + 底走y60 + 钩)。
    """
    g = Glyph("uni5DFB", advance=1000, unicode=0x5DFB, note="巻：龹 + 己")
    g.dot(370, 780, W_DOT, 96, SLANT_DOT)
    g.dot(630, 780, W_DOT, 96, SLANT_SHORT)
    g.hbar(300, 700, 690, W_THIN)
    g.hbar(200, 800, 570, W_THIN)
    g.diag(500, 570, 200, 380, W_THIN)
    g.diag(500, 570, 860, 380, W_THIN)
    g.hbar(200, 760, 330, W_SEC)
    g.vbar(714, 200, 330, W_SEC)
    g.hbar(200, 714, 200, W_SEC)
    g.vbar(246, 66, 200, W_SEC)
    g.hbar(246, 780, 66, W_SEC)
    g.vbar(738, 66, 160, W_THIN)
    return g


def _g_kimi():
    """君 = ⿱尹口。
    尹：横折(横180..900 y774 + 竖x854) + 一2(y650) + 一3(y520) + 撇(700,770→215,445)。
    口：左竖x292 + 横折(横280..790 y380 + 右竖x744) + 底横(y90)。
    """
    g = Glyph("uni541B", advance=1000, unicode=0x541B, note="君：尹 + 口")
    g.hbar(180, 900, 774, W_SEC)
    g.vbar(854, 600, 774, W_SEC)
    g.hbar(260, 854, 650, W_SEC)
    g.hbar(100, 800, 520, W_SEC)
    g.diag(700, 770, 215, 445, W_SEC)
    g.vbar(326, 90, 380, W_SEC)
    g.hbar(280, 790, 380, W_SEC)
    g.vbar(744, 90, 380, W_SEC)
    g.hbar(280, 744, 90, W_SEC)
    return g


def _g_ju():
    """充 = ⿱亠允。
    亠：点(500,770) + 一(y650)。
    厶：ㄥ(撇620,560→470,390 + 底横y390) + 点(690,430)。
    儿：撇(500,350→250,40) + 竖弯钩(竖x640 + 底走y56 + 钩)。
    """
    g = Glyph("uni5145", advance=1000, unicode=0x5145, note="充：亠 + 允")
    g.dot(500, 770, W_DOT, 96, SLANT_DOT)
    g.hbar(200, 800, 650, W_SEC)
    g.diag(620, 560, 470, 390, W_THIN)
    g.hbar(470, 610, 390, W_THIN)
    g.dot(690, 430, W_DOT, 96, SLANT_DOT)
    g.diag(500, 350, 250, 40, W_THIN)
    g.vbar(640, 56, 340, W_SEC)
    g.hbar(640, 880, 56, W_SEC)
    g.vbar(838, 56, 160, W_THIN)
    return g


def _g_ame():
    """雨 = 雨。
    一(y774) + 冂(左竖x160 + 横折横160..900 y660 + 右竖x854) + 中竖(x530) + 四点。
    """
    g = Glyph("uni96E8", advance=1000, unicode=0x96E8, note="雨：雨")
    g.hbar(120, 880, 774, W_SEC)
    g.vbar(160, 100, 660, W_SEC)
    g.hbar(160, 900, 660, W_SEC)
    g.vbar(854, 100, 660, W_SEC)
    g.vbar(530, 140, 660, W_SEC)
    g.dot(330, 510, W_DOT, 96, SLANT_DOT)
    g.dot(330, 290, W_DOT, 96, SLANT_DOT)
    g.dot(710, 510, W_DOT, 96, SLANT_DOT)
    g.dot(710, 290, W_DOT, 96, SLANT_DOT)
    return g


def _g_kyaku():
    """却 = ⿰去卩。
    去：一(y720) + 竖(x340) + 一(y540) + 厶(ㄥ420,490→230,250 + 底横y250 + 点520,280)。
    卩：竖(x700) + 横折钩(横654..900 y774 + 竖x858 + 钩)。
    """
    g = Glyph("uni5374", advance=1000, unicode=0x5374, note="却：去 + 卩")
    g.hbar(120, 560, 720, W_THIN)
    g.vbar(340, 470, 762, W_THIN)
    g.hbar(80, 600, 540, W_THIN)
    g.diag(420, 490, 230, 250, W_THIN)
    g.hbar(230, 420, 250, W_THIN)
    g.dot(520, 280, W_DOT, 96, SLANT_DOT)
    g.vbar(700, 300, 780, W_SEC)
    g.hbar(654, 900, 774, W_THIN)
    g.vbar(858, 420, 774, W_THIN)
    g.diag(858, 430, 780, 490, W_THIN)
    return g


def _g_ori():
    """折 = ⿰扌斤。
    扌：批内统一拆法(box 60..350)。
    斤：撇(560,790→420,700) + 竖撇(470,690→430,60) + 一(y420) + 竖(x760)。
    """
    g = Glyph("uni6298", advance=1000, unicode=0x6298, note="折：扌 + 斤")
    _tehen(g, 60.0, 350.0)
    g.diag(560, 790, 420, 700, W_THIN)
    g.diag(470, 690, 430, 60, W_THIN)
    g.hbar(470, 880, 420, W_SEC)
    g.vbar(760, 60, 520, W_SEC)
    return g


def _g_gun():
    """郡 = ⿰君阝。
    君（缩排）：横折(横120..600 y774 + 竖x558) + 一2(y660) + 一3(y540) + 撇(440,770→120,420) + 口(y380..90)。
    阝：批内统一拆法(box 670..940)。
    """
    g = Glyph("uni90E1", advance=1000, unicode=0x90E1, note="郡：君 + 阝")
    g.hbar(120, 600, 774, W_THIN)
    g.vbar(558, 610, 774, W_THIN)
    g.hbar(180, 558, 660, W_THIN)
    g.hbar(80, 520, 540, W_THIN)
    g.diag(440, 770, 120, 420, W_THIN)
    g.vbar(242, 90, 380, W_THIN)
    g.hbar(200, 498, 380, W_THIN)
    g.vbar(456, 90, 380, W_THIN)
    g.hbar(200, 456, 90, W_THIN)
    _ears(g, 670.0, 940.0)
    return g


def _g_hei():
    """併 = ⿰亻并。
    亻：批内统一拆法(box 60..340)。
    并：丷两点(540,760 / 790,760) + 一(y640) + 一(y480) + 撇(600,480→460,60) + 竖(x800)。
    """
    g = Glyph("uni4F75", advance=1000, unicode=0x4F75, note="併：亻 + 并")
    _ninben(g, 60.0, 340.0)
    g.dot(540, 760, W_DOT, 96, SLANT_DOT)
    g.dot(790, 760, W_DOT, 96, SLANT_SHORT)
    g.hbar(460, 880, 640, W_THIN)
    g.hbar(420, 920, 480, W_SEC)
    g.diag(600, 480, 460, 60, W_THIN)
    g.vbar(800, 60, 480, W_SEC)
    return g


# ------------------------------------------------------------------ 组装

def build() -> list[Glyph]:
    return [
        _g_hou(),
        _g_fuku(),
        _g_bi(),
        _g_tera(),
        _g_u(),
        _g_ban(),
        _g_modosu(),
        _g_ki(),
        _g_kei(),
        _g_tei(),
        _g_i(),
        _g_o(),
        _g_mai(),
        _g_soku(),
        _g_chu(),
        _g_ei(),
        _g_waku(),
        _g_ni(),
        _g_ita(),
        _g_retsu(),
        _g_chu2(),
        _g_nigete(),
        _g_itte(),
        _g_me(),
        _g_maki(),
        _g_kimi(),
        _g_ju(),
        _g_ame(),
        _g_kyaku(),
        _g_ori(),
        _g_gun(),
        _g_hei(),
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-011.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
