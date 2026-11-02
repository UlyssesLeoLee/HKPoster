"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-007。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
- 字面框 x 60..940 / y 0..820，advance 固定 1000，与 zh-HK 繁体档完全一致，
  便于 zh-HK / zh-CN / ja 三语混排时基线与字面统一。
- 笔画权重沿用漢字档：主 96 / 次 92 / 细 84 / 点 84。笔画少的字（字・光・存・否）
  整体吃 96；笔画多的字（専・科・省・室・客・図・周・速）在横画叠横画、竖画挤竖画处
  局部降到 92/84，保住内白（GLY-001 小空腔局部减重 / GLY-006 内白 ≥ 24）。
- 同部件在本批复用同一套坐标与拆法，只做位置与大小的光学校正（GLY-004）：
  氵（3 笔）、扌、木、口、宀（丶 + 冖）、日、目、左形 阝（阜偏）、右形 阝（邑偏）、
  儿、辶 全部走本文件内的辅助函数。
- 横画一律按「墨迹上缘 / 下缘对齐」落位（bar_at / bar_base）：
  顶横的墨迹上缘吃满 820，基线横的墨迹下缘吃满 0；竖画端点即墨迹端点。
- **竖画与横画相接处一律互相压入 30 单位**（竖画端点落进横画的墨迹区），
  不做「端点恰好压在横画墨迹边缘」的对齐——那种齐边接触会在并集轮廓里
  留下退化短边（实测会让 check_glyphs 报「轮廓自交或非法」）。
- 横竖撇捺一律平切硬边；点与短撇用 slant=26 的斜切平行四边形（港产海报签名），
  不用圆头。
- 结构性封闭的字（図・周・省・目・口）内白洞由 hkbuild 自动成洞，
  墨量率超阈由集成方裁定放行，不为了压阈值把字压成畸形。
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

# 字面框
LEFT = 60
RIGHT = 940
TOP = 820
BOTTOM = 0


# --------------------------------------------------------------------------
# 对齐辅助：横画按墨迹上缘 / 下缘定位，竖画端点即墨迹端点
# --------------------------------------------------------------------------
def bar_at(g: Glyph, x1: float, x2: float, ink_top: float, w: float = W_MAIN) -> None:
    """水平笔画：墨迹上缘对齐 ink_top（墨迹占 ink_top-w .. ink_top）。"""
    g.hbar(x1, x2, ink_top - w / 2.0, weight=w)


def bar_top(g: Glyph, x1: float, x2: float, w: float = W_MAIN) -> None:
    """水平笔画：墨迹上缘吃满字面框顶 820。"""
    g.hbar(x1, x2, TOP - w / 2.0, weight=w)


def bar_base(g: Glyph, x1: float, x2: float, w: float = W_MAIN) -> None:
    """水平笔画：墨迹下缘吃满基线 0。"""
    g.hbar(x1, x2, BOTTOM + w / 2.0, weight=w)


def vbar(g: Glyph, x: float, y1: float, y2: float, w: float = W_MAIN) -> None:
    """垂直笔画：中心线 x，墨迹自 y1 到 y2。"""
    g.vbar(x, y1, y2, weight=w)


def diag(g: Glyph, x1: float, y1: float, x2: float, y2: float, w: float = W_MAIN) -> None:
    """斜笔画：中心线两端点。"""
    g.diag(x1, y1, x2, y2, weight=w)


def dot_hk(g: Glyph, cx: float, cy: float, w: float = W_DOT, h: float = 104) -> None:
    """点 / 短撇：slant=26 的斜切平行四边形（港产海报签名）。"""
    g.dot(cx, cy, w=w, h=h, slant=26)


def hook_left(g: Glyph, x: float, y: float, dx: float = -70, dy: float = -34,
              w: float = W_THIN) -> None:
    """竖钩末端向左上挑的小钩。"""
    g.diag(x, y, x + dx, y + dy, weight=w)


def hook_right(g: Glyph, x: float, y: float, dx: float = 70, dy: float = -34,
               w: float = W_THIN) -> None:
    """竖弯钩末端向右上挑的小钩。"""
    g.diag(x, y, x + dx, y + dy, weight=w)


# --------------------------------------------------------------------------
# 复用部件
# --------------------------------------------------------------------------
def comp_sanzui(g: Glyph, x: float = 160, y_top: float = 730, y_mid: float = 545,
                y_low: float = 150) -> None:
    """氵：两点一提（本批 況 / 注 共用同一套相对位置）。"""
    dot_hk(g, x, y_top)
    dot_hk(g, x - 30, y_mid)
    g.diag(x - 55, y_low, x + 60, y_low + 180, weight=W_SEC)


def comp_men(g: Glyph, x_l: float = 270, x_r: float = 880, y_top: float = 700,
             dot_cx: float = 490) -> None:
    """宀：丶 + 冖（顶横 + 左短竖 + 右短竖钩）。"""
    dot_hk(g, dot_cx, y_top + 30, h=110)
    vbar(g, x_l, y_top - 30, y_top - 100, W_SEC)
    bar_at(g, x_l + 34, x_r, y_top, W_MAIN)
    vbar(g, x_r, y_top - 48, y_top - 112, W_SEC)


def comp_tehen(g: Glyph, x: float = 190, y_top: float = 800) -> None:
    """扌：横 + 竖（带钩）+ 提。"""
    bar_at(g, 70, 330, 700, W_MAIN)
    vbar(g, x, y_top, 120, W_MAIN)
    hook_left(g, x, 155)
    g.diag(85, 380, 320, 500, weight=W_SEC)


def comp_ear_left(g: Glyph, x: float = 110, y_top: float = 790,
                  y_bot: float = 60) -> None:
    """左形 阝（阜偏）：左竖 + 右上折返的耳肚（阪用）。"""
    vbar(g, x, y_top - 30, y_bot, W_MAIN)
    bar_at(g, x, x + 170, y_top, W_SEC)
    g.diag(x + 170, y_top - 46, x + 70, y_top - 190, weight=W_SEC)
    g.diag(x + 70, y_top - 190, x + 160, y_top - 270, weight=W_THIN)


def comp_ear_right(g: Glyph, x: float = 860, y_top: float = 790,
                   y_bot: float = 60) -> None:
    """右形 阝（邑偏）：右竖 + 左侧折返的耳肚（郎用，与阜偏互为镜像）。"""
    vbar(g, x, y_top - 30, y_bot, W_MAIN)
    bar_at(g, x - 160, x, y_top, W_SEC)
    g.diag(x - 160, y_top - 46, x - 70, y_top - 190, weight=W_SEC)
    g.diag(x - 70, y_top - 190, x - 160, y_top - 270, weight=W_THIN)


# --------------------------------------------------------------------------
# 字形
# --------------------------------------------------------------------------
def uni6BB5() -> Glyph:
    """段 9画 —— ⿰𠂤殳。

    左 𠂤（x 89..420）：ノ(210,770→120,690) / 丨(x=205, 800→110) /
    三横（上缘 700 / 560 / 420）。
    右 殳（x 460..916）：ノ(600,785→510,700) / 几(横 570..870 上缘 780 + 竖 870 750→650)
    / 又(横 500..840 上缘 560 + 撇 830,512→640,160 + 捺 580,470→880,120)。
    """
    g = Glyph("uni6BB5", advance=1000, unicode=0x6BB5, note="段 9画 ⿰𠂤殳")
    # 左 𠂤
    g.diag(210, 770, 120, 690, weight=W_SEC)
    vbar(g, 205, 800, 110, W_MAIN)
    bar_at(g, 205, 420, 700, W_MAIN)
    bar_at(g, 205, 405, 560, W_SEC)
    bar_at(g, 205, 390, 420, W_SEC)
    # 右 殳
    g.diag(600, 785, 510, 700, weight=W_SEC)
    bar_at(g, 570, 870, 780, W_MAIN)
    vbar(g, 870, 750, 650, W_SEC)
    bar_at(g, 500, 840, 560, W_MAIN)
    g.diag(830, 512, 640, 160, weight=W_SEC)
    g.diag(580, 470, 880, 120, weight=W_MAIN)
    return g


def uni578B() -> Glyph:
    """型 9画 —— ⿱刑土。

    刑（y 350..820）：开的两横（上缘 790 / 640）+ 丿 + 丨，刂（短竖 630 / 长竖 800）。
    土（y 0..260）：横 200..800 上缘 260，丨 x=500，底横 120..880 下缘 0。
    """
    g = Glyph("uni578B", advance=1000, unicode=0x578B, note="型 9画 ⿱刑土")
    # 刑
    bar_at(g, 80, 620, 790, W_MAIN)
    vbar(g, 400, 760, 350, W_MAIN)
    bar_at(g, 70, 640, 640, W_MAIN)
    g.diag(255, 640, 120, 350, weight=W_SEC)
    vbar(g, 630, 780, 560, W_THIN)
    vbar(g, 800, 800, 360, W_MAIN)
    # 土
    bar_at(g, 200, 800, 260, W_SEC)
    vbar(g, 500, 230, 60, W_MAIN)
    bar_at(g, 120, 880, 96, W_MAIN)
    return g


def uni5B57() -> Glyph:
    """字 6画 —— ⿱宀子。

    宀（y 590..800）：丶(490,730) + 左短竖 270 + 顶横 304..880 上缘 700 + 右短竖 880。
    子（y 82..560）：乛(横 340..700 上缘 560 + 折 650,512→540,380)
    + 一(250..750 上缘 330) + 亅(x=505, 555→100) + 钩。
    """
    g = Glyph("uni5B57", advance=1000, unicode=0x5B57, note="字 6画 ⿱宀子")
    comp_men(g)
    # 子
    bar_at(g, 340, 700, 560, W_MAIN)
    g.diag(650, 512, 540, 380, weight=W_SEC)
    bar_at(g, 250, 750, 330, W_MAIN)
    vbar(g, 505, 555, 100, W_MAIN)
    hook_left(g, 505, 150)
    return g


def uni6CC1() -> Glyph:
    """況 8画 —— ⿰氵兄。

    氵：三点一提（与 注 共用 comp_sanzui）。
    兄（x 291..870）：口(390..760, 522..800) + 儿(撇 480→350, 竖 700 + 钩 850)。
    """
    g = Glyph("uni6CC1", advance=1000, unicode=0x6CC1, note="況 8画 ⿰氵兄")
    comp_sanzui(g)
    # 口
    vbar(g, 390, 770, 570, W_MAIN)
    bar_at(g, 390, 760, 800, W_MAIN)
    vbar(g, 760, 770, 570, W_MAIN)
    bar_at(g, 390, 760, 618, W_MAIN)
    # 儿
    g.diag(480, 560, 350, 120, weight=W_SEC)
    vbar(g, 700, 560, 150, W_MAIN)
    hook_right(g, 700, 150)
    return g


def uni97F3() -> Glyph:
    """音 9画 —— ⿱立日。

    立（y 354..790）：丶(500,735) + 一(230..770 上缘 700) + 左点 + 右撇
    + 底横(160..840 上缘 450)。
    日（y 0..324）：两竖 300/700 + 三横（上缘 324 / 204 / 96），内白 24+24。
    """
    g = Glyph("uni97F3", advance=1000, unicode=0x97F3, note="音 9画 ⿱立日")
    # 立
    dot_hk(g, 500, 735, h=110)
    bar_at(g, 230, 770, 700, W_MAIN)
    g.diag(350, 690, 430, 430, weight=W_SEC)
    g.diag(650, 690, 570, 430, weight=W_SEC)
    bar_at(g, 160, 840, 450, W_MAIN)
    # 日
    vbar(g, 300, 294, 60, W_MAIN)
    vbar(g, 700, 294, 60, W_MAIN)
    bar_at(g, 300, 700, 324, W_MAIN)
    bar_at(g, 300, 700, 204, W_THIN)
    bar_at(g, 300, 700, 96, W_MAIN)
    return g


def uni6CE8() -> Glyph:
    """注 8画 —— ⿰氵主。

    氵：与 況 同一套（comp_sanzui）。
    主（x 300..920）：丶(620,725) + 一(330..890 上缘 690) + 丨(x=610, 660→60)
    + 一(390..830 上缘 480) + 底横(300..920 下缘 0)。
    """
    g = Glyph("uni6CE8", advance=1000, unicode=0x6CE8, note="注 8画 ⿰氵主")
    comp_sanzui(g)
    dot_hk(g, 620, 725, h=110)
    bar_at(g, 330, 890, 690, W_MAIN)
    vbar(g, 610, 660, 60, W_MAIN)
    bar_at(g, 390, 830, 480, W_MAIN)
    bar_at(g, 300, 920, 96, W_MAIN)
    return g


def uni547C() -> Glyph:
    """呼 8画 —— ⿰口乎。

    口（x 102..428, 254..720）。
    乎（x 454..920）：ノ(600→490) + 丶短撇(480→555) + 丿(720→640) + 一(450..920 上缘 600)
    + 亅(x=640, 720→120) + 钩。
    """
    g = Glyph("uni547C", advance=1000, unicode=0x547C, note="呼 8画 ⿰口乎")
    # 口（x 102..428, 254..720）
    vbar(g, 150, 690, 330, W_MAIN)
    bar_at(g, 150, 380, 720, W_MAIN)
    vbar(g, 380, 690, 330, W_MAIN)
    bar_at(g, 150, 380, 350, W_MAIN)
    # 乎
    g.diag(600, 765, 490, 700, weight=W_SEC)
    g.diag(480, 685, 555, 735, weight=W_SEC)
    g.diag(720, 700, 640, 620, weight=W_THIN)
    bar_at(g, 450, 920, 600, W_MAIN)
    vbar(g, 640, 720, 120, W_MAIN)
    hook_left(g, 640, 160)
    return g


def uni826F() -> Glyph:
    """良 7画 —— 丶 + 艮。

    丶(500,745) / フ(横 180..800 上缘 700 + 竖 800 670→350) / 一(上缘 560) / 一(上缘 420)
    / 丨(x=180, 670→120) / 撇(320,340→170,100) / 捺(420,320→800,90)。
    """
    g = Glyph("uni826F", advance=1000, unicode=0x826F, note="良 7画 丶+艮")
    dot_hk(g, 500, 745, h=104)
    bar_at(g, 180, 800, 700, W_SEC)
    vbar(g, 800, 670, 350, W_SEC)
    bar_at(g, 180, 800, 560, W_THIN)
    bar_at(g, 180, 800, 420, W_SEC)
    vbar(g, 180, 670, 120, W_SEC)
    g.diag(320, 340, 170, 100, weight=W_SEC)
    g.diag(420, 320, 800, 90, weight=W_MAIN)
    return g


def uni962A() -> Glyph:
    """阪 7画 —— ⿰阝反。

    左 阝（阜偏，x 62..320）：竖 x=110 + 横 + 折返耳肚。
    右 反（x 300..940）：厂(丿 430,800→330,560 + 横 420..900 上缘 790)
    + 又(横 470..880 上缘 520 + 撇 870,472→660,180 + 捺 540,440→900,120)。
    """
    g = Glyph("uni962A", advance=1000, unicode=0x962A, note="阪 7画 ⿰阝反")
    comp_ear_left(g)
    # 反
    g.diag(430, 800, 330, 560, weight=W_SEC)
    bar_at(g, 420, 900, 790, W_MAIN)
    bar_at(g, 470, 880, 520, W_MAIN)
    g.diag(870, 472, 660, 180, weight=W_SEC)
    g.diag(540, 440, 900, 120, weight=W_MAIN)
    return g


def uni5C02() -> Glyph:
    """専 9画 —— 十 + 田 + 寸（竖贯通全字，保证轮廓连通）。

    一(270..730 上缘 790) / 丨(x=500, 760→80) / 田框(290..710, 380..660)
    / 寸一(200..800 上缘 260) / 寸丶(390,180) / 竖钩。
    """
    g = Glyph("uni5C02", advance=1000, unicode=0x5C02, note="専 9画 十+田+寸")
    bar_at(g, 270, 730, 790, W_MAIN)
    vbar(g, 500, 760, 80, W_MAIN)
    # 田框
    vbar(g, 290, 630, 340, W_SEC)
    vbar(g, 710, 630, 340, W_SEC)
    bar_at(g, 290, 710, 660, W_MAIN)
    bar_at(g, 290, 710, 500, W_THIN)
    bar_at(g, 290, 710, 380, W_MAIN)
    # 寸
    bar_at(g, 200, 800, 260, W_MAIN)
    dot_hk(g, 390, 180, w=W_DOT, h=88)
    hook_left(g, 500, 130)
    return g


def uni8C37() -> Glyph:
    """谷 7画 —— ⿱八人口。

    八(430,785→345,715 / 570,785→655,715) / 人(丿 500,700→330,430 + 捺 500,700→670,430)
    / 口(330..670, 96..430)。
    """
    g = Glyph("uni8C37", advance=1000, unicode=0x8C37, note="谷 7画 ⿱八人口")
    # 八
    g.diag(430, 780, 345, 710, weight=W_SEC)
    g.diag(570, 780, 655, 710, weight=W_SEC)
    # 人
    g.diag(500, 700, 330, 430, weight=W_SEC)
    g.diag(500, 700, 670, 430, weight=W_SEC)
    # 口
    vbar(g, 330, 400, 50, W_MAIN)
    bar_at(g, 330, 670, 430, W_MAIN)
    vbar(g, 670, 400, 50, W_MAIN)
    bar_at(g, 330, 670, 96, W_MAIN)
    return g


def uni7A81() -> Glyph:
    """突 8画 —— ⿱穴犬。

    穴 = 宀(同 comp_men) + 八(390,620→300,520 / 610,620→700,520)。
    犬 = 一(250..850 上缘 460) + 撇(520,500→330,100) + 捺(500,480→830,100) + 丶(640,545)。
    """
    g = Glyph("uni7A81", advance=1000, unicode=0x7A81, note="突 8画 ⿱穴犬")
    comp_men(g)
    # 八
    g.diag(390, 620, 300, 520, weight=W_THIN)
    g.diag(610, 620, 700, 520, weight=W_THIN)
    # 犬
    bar_at(g, 250, 850, 460, W_MAIN)
    g.diag(520, 500, 330, 100, weight=W_SEC)
    g.diag(500, 480, 830, 100, weight=W_MAIN)
    dot_hk(g, 640, 545, w=W_DOT, h=84)
    return g


def uni5175() -> Glyph:
    """兵 7画 —— 丘 + 八。

    丘：ノ(250,750→170,670) + 一(230..700 上缘 790) + 丨(x=300, 760→270)
    + 一(300..680 上缘 540) + 一(150..850 上缘 300)。
    八：撇(390,190→260,60) + 点(610,190→740,60)。
    """
    g = Glyph("uni5175", advance=1000, unicode=0x5175, note="兵 7画 丘+八")
    g.diag(250, 750, 170, 670, weight=W_SEC)
    bar_at(g, 230, 700, 790, W_MAIN)
    vbar(g, 300, 760, 270, W_MAIN)
    bar_at(g, 300, 680, 540, W_SEC)
    bar_at(g, 150, 850, 300, W_MAIN)
    # 八
    g.diag(390, 190, 260, 60, weight=W_SEC)
    g.diag(610, 190, 740, 60, weight=W_SEC)
    return g


def uni5149() -> Glyph:
    """光 6画 —— ⿱⺌兀。

    ⺌：丨(x=500, 800→640) + 左点(320,730) + 右撇(680,740→620,650)。
    一(150..850 上缘 560) / 儿(撇 430,520→250,100 / 竖 680 + 钩 840)。
    """
    g = Glyph("uni5149", advance=1000, unicode=0x5149, note="光 6画 ⿱⺌兀")
    vbar(g, 500, 800, 640, W_MAIN)
    dot_hk(g, 320, 730)
    g.diag(680, 740, 620, 650, weight=W_THIN)
    bar_at(g, 150, 850, 560, W_MAIN)
    g.diag(430, 520, 250, 100, weight=W_SEC)
    vbar(g, 680, 520, 140, W_MAIN)
    hook_right(g, 680, 140)
    return g


def uni79D1() -> Glyph:
    """科 9画 —— ⿰禾斗。

    禾（x 108..503）：ノ(270,765→170,705) + 一(160..470 上缘 700) + 丨(x=310, 670→40)
    + 撇(310,560→110,190) + 点(320,540→470,380)。
    斗（x 519..860）：点(620,700) + 点(580,560) + 一(520..860 上缘 400) + 丨(x=760, 800→100)。
    """
    g = Glyph("uni79D1", advance=1000, unicode=0x79D1, note="科 9画 ⿰禾斗")
    # 禾
    g.diag(270, 765, 170, 705, weight=W_SEC)
    bar_at(g, 160, 470, 700, W_MAIN)
    vbar(g, 310, 670, 40, W_MAIN)
    g.diag(310, 560, 110, 190, weight=W_SEC)
    g.diag(320, 540, 470, 380, weight=W_SEC)
    # 斗
    dot_hk(g, 620, 700, h=92)
    dot_hk(g, 580, 560, h=92)
    bar_at(g, 520, 860, 400, W_MAIN)
    vbar(g, 760, 800, 100, W_MAIN)
    return g


def uni653B() -> Glyph:
    """攻 7画 —— ⿰工攵。

    工（x 62..448）：一(70..400 上缘 780) + 丨(x=235, 750→60) + 底横(70..410 下缘 0)。
    攵（x 429..919）：ノ(560,770→500,700) + 一(500..900 上缘 690)
    + 撇(760,690→470,120) + 捺(560,560→880,110)。
    """
    g = Glyph("uni653B", advance=1000, unicode=0x653B, note="攻 7画 ⿰工攵")
    # 工
    bar_at(g, 70, 400, 780, W_MAIN)
    vbar(g, 235, 750, 60, W_MAIN)
    bar_at(g, 70, 410, 96, W_MAIN)
    # 攵
    g.diag(560, 770, 500, 700, weight=W_SEC)
    bar_at(g, 500, 900, 690, W_MAIN)
    g.diag(760, 690, 470, 120, weight=W_SEC)
    g.diag(560, 560, 880, 110, weight=W_MAIN)
    return g


def uni52B9() -> Glyph:
    """効 8画 —— ⿰交力。

    交（x 139..471）：丶(300,735) + 一(120..480 上缘 700) + 左点 + 右撇
    + 乂(撇 430,640→200,200 + 捺 180,640→420,200)。
    力（x 535..928）：𠃌(横 580..880 上缘 700 + 竖 880 670→380 + 钩)
    + 撇(730,740→580,150)。
    """
    g = Glyph("uni52B9", advance=1000, unicode=0x52B9, note="効 8画 ⿰交力")
    # 交
    dot_hk(g, 300, 735, h=110)
    bar_at(g, 120, 480, 700, W_MAIN)
    g.diag(220, 690, 280, 560, weight=W_THIN)
    g.diag(380, 690, 320, 560, weight=W_THIN)
    g.diag(430, 640, 200, 200, weight=W_SEC)
    g.diag(180, 640, 420, 200, weight=W_SEC)
    # 力
    bar_at(g, 580, 880, 700, W_MAIN)
    vbar(g, 880, 670, 380, W_MAIN)
    hook_left(g, 880, 400, dx=-70, dy=-30)
    g.diag(730, 740, 580, 150, weight=W_SEC)
    return g


def uni56F3() -> Glyph:
    """図 7画 —— ⿴囗メ。

    囗：左竖 x=150 + 顶横 150..850 上缘 800 + 右竖 x=850 + 底横下缘 0。
    メ：乂(330,600→670,260 / 670,600→330,260)。
    """
    g = Glyph("uni56F3", advance=1000, unicode=0x56F3, note="図 7画 ⿴囗メ")
    vbar(g, 150, 770, 60, W_MAIN)
    bar_at(g, 150, 850, 800, W_MAIN)
    vbar(g, 850, 770, 60, W_MAIN)
    bar_at(g, 150, 850, 96, W_MAIN)
    # メ
    g.diag(390, 570, 610, 330, weight=W_SEC)
    g.diag(610, 570, 390, 330, weight=W_SEC)
    return g


def uni7701() -> Glyph:
    """省 9画 —— ⿱少目。

    少：丨(x=500, 800→600) + 左撇(360,720→250,600) + 右点(650,700)
    + 长撇(500,600→330,430)。
    目（y 0..424）：两竖 330/670 + 四横（上缘 424 / 308 / 200 / 92），内白 24×3。
    """
    g = Glyph("uni7701", advance=1000, unicode=0x7701, note="省 9画 ⿱少目")
    # 少
    vbar(g, 500, 800, 600, W_MAIN)
    g.diag(360, 720, 250, 600, weight=W_THIN)
    dot_hk(g, 650, 700, h=92)
    g.diag(500, 600, 330, 430, weight=W_SEC)
    # 目
    vbar(g, 330, 394, 50, W_MAIN)
    vbar(g, 670, 394, 50, W_MAIN)
    bar_at(g, 330, 670, 424, W_SEC)
    bar_at(g, 330, 670, 308, W_THIN)
    bar_at(g, 330, 670, 200, W_THIN)
    bar_at(g, 330, 670, 92, W_SEC)
    return g


def uni5BA4() -> Glyph:
    """室 9画 —— ⿱宀至。

    宀：同 comp_men。
    至（y 0..610）：一(280..720 上缘 600) + 厶(撇 430,490→360,370 + 点 430,400→540,350)
    + 土(一 340..660 上缘 330 / 丨 x=500 300→60 / 底横 240..760 下缘 0)。
    """
    g = Glyph("uni5BA4", advance=1000, unicode=0x5BA4, note="室 9画 ⿱宀至")
    comp_men(g)
    bar_at(g, 280, 720, 600, W_MAIN)
    g.diag(430, 490, 360, 370, weight=W_THIN)
    g.diag(430, 400, 540, 350, weight=W_THIN)
    bar_at(g, 340, 660, 330, W_SEC)
    vbar(g, 500, 300, 60, W_MAIN)
    bar_at(g, 240, 760, 96, W_MAIN)
    return g


def uni6B69() -> Glyph:
    """歩 8画 —— ⿱止少。

    止（y 304..820）：丨(x=500, 800→480) + 一(500..780 上缘 700) + 丨(x=300, 700→370)
    + 底横(180..820 上缘 400)。
    少（y 90..380）：丨(x=500, 380→250) + 左撇(380,330→280,230) + 右点(620,320)
    + 长撇(500,260→350,120)。
    """
    g = Glyph("uni6B69", advance=1000, unicode=0x6B69, note="歩 8画 ⿱止少")
    # 止
    vbar(g, 500, 800, 480, W_MAIN)
    bar_at(g, 500, 780, 700, W_MAIN)
    vbar(g, 300, 700, 370, W_MAIN)
    bar_at(g, 180, 820, 400, W_MAIN)
    # 少
    vbar(g, 500, 380, 250, W_MAIN)
    g.diag(380, 330, 280, 230, weight=W_THIN)
    dot_hk(g, 620, 320, h=92)
    g.diag(500, 260, 350, 120, weight=W_SEC)
    return g


def uni5CB8() -> Glyph:
    """岸 8画 —— ⿱山厂干。

    山（y 408..815）：丨(x=500, 800→454) + 左竖 280 + 右竖 720 + 底横 280..720 上缘 500。
    厂（y 44..380）：一(180..850 上缘 380) + 撇(300,340→130,100)。
    干（y 44..256）：一(450..900 上缘 256) + 一(380..940 上缘 136) + 丨(x=660, 210→60)。
    2026-10-31 回修：山底横与厂横白口 −22 → 三横依次下移，三处白口各 28。
    """
    g = Glyph("uni5CB8", advance=1000, unicode=0x5CB8, note="岸 8画 ⿱山厂干")
    # 山
    vbar(g, 500, 800, 454, W_MAIN)
    vbar(g, 280, 690, 454, W_SEC)
    vbar(g, 720, 690, 454, W_SEC)
    bar_at(g, 280, 720, 500, W_SEC)
    # 厂
    bar_at(g, 180, 850, 380, W_MAIN)
    g.diag(300, 340, 130, 100, weight=W_MAIN)
    # 干
    bar_at(g, 450, 900, 256, W_SEC)
    bar_at(g, 380, 940, 136, W_SEC)
    vbar(g, 660, 210, 60, W_MAIN)
    return g


def uni5BA2() -> Glyph:
    """客 9画 —— ⿱宀各。

    宀：同 comp_men。
    各（y 0..620）：夂(丿 540,620→450,510 + 横 500..740 上缘 500 + 撇 720,440→560,320
    + 捺 520,430→720,290) + 口(430..700, 96..290)。
    """
    g = Glyph("uni5BA2", advance=1000, unicode=0x5BA2, note="客 9画 ⿱宀各")
    comp_men(g)
    g.diag(540, 620, 450, 510, weight=W_THIN)
    bar_at(g, 500, 740, 500, W_SEC)
    g.diag(720, 440, 560, 320, weight=W_THIN)
    g.diag(520, 430, 720, 290, weight=W_SEC)
    vbar(g, 430, 260, 50, W_MAIN)
    bar_at(g, 430, 700, 290, W_MAIN)
    vbar(g, 700, 260, 50, W_MAIN)
    bar_at(g, 430, 700, 96, W_MAIN)
    return g


def uni5426() -> Glyph:
    """否 7画 —— ⿱不口。

    不（y 430..800）：一(120..880 上缘 800) + 撇(380,760→180,430) + 丨(x=500, 760→430)
    + 点(610,690→790,520)。
    口（y 50..380）：两竖 340/660 + 顶横上缘 380 + 底横下缘 0。
    """
    g = Glyph("uni5426", advance=1000, unicode=0x5426, note="否 7画 ⿱不口")
    bar_at(g, 120, 880, 800, W_MAIN)
    g.diag(380, 760, 180, 430, weight=W_SEC)
    vbar(g, 500, 760, 430, W_MAIN)
    g.diag(610, 690, 790, 520, weight=W_SEC)
    vbar(g, 340, 350, 50, W_MAIN)
    bar_at(g, 340, 660, 380, W_MAIN)
    vbar(g, 660, 350, 50, W_MAIN)
    bar_at(g, 340, 660, 96, W_MAIN)
    return g


def uni5468() -> Glyph:
    """周 8画 —— ⿵冂吉。

    冂：左竖 x=180 + 顶横 180..860 上缘 800 + 右竖 x=860。
    吉（x 330..706）：士(一 320..720 上缘 620 + 丨 x=520 + 一 330..710 上缘 420)
    + 口(400..660, 120..300)。
    """
    g = Glyph("uni5468", advance=1000, unicode=0x5468, note="周 8画 ⿵冂吉")
    vbar(g, 180, 770, 60, W_SEC)
    bar_at(g, 180, 860, 800, W_SEC)
    vbar(g, 860, 770, 60, W_SEC)
    # 吉
    bar_at(g, 320, 720, 620, W_THIN)
    vbar(g, 520, 590, 390, W_SEC)
    bar_at(g, 330, 710, 420, W_THIN)
    vbar(g, 400, 270, 80, W_THIN)
    bar_at(g, 400, 660, 300, W_THIN)
    vbar(g, 660, 270, 80, W_THIN)
    bar_at(g, 400, 660, 120, W_THIN)
    return g


def uni6750() -> Glyph:
    """材 7画 —— ⿰木才。

    木（x 78..499）：一(70..460 上缘 700) + 丨(x=265, 670→40) + 撇(265,620→120,250)
    + 点(275,600→460,380)。
    才（x 519..900）：一(520..900 上缘 660) + 亅(x=700, 800→120 + 钩)
    + 撇(790,700→560,240)。
    """
    g = Glyph("uni6750", advance=1000, unicode=0x6750, note="材 7画 ⿰木才")
    # 木
    bar_at(g, 70, 460, 700, W_MAIN)
    vbar(g, 265, 670, 40, W_MAIN)
    g.diag(265, 620, 120, 250, weight=W_SEC)
    g.diag(275, 600, 460, 380, weight=W_SEC)
    # 才
    bar_at(g, 520, 900, 660, W_MAIN)
    vbar(g, 700, 800, 120, W_MAIN)
    hook_left(g, 700, 160)
    g.diag(790, 700, 560, 240, weight=W_SEC)
    return g


def uni7CFB() -> Glyph:
    """系 7画 —— 丿 + 幺 + 小。

    丿(430,760→240,690) / 幺(折 520,700→340,575 + 340,575→480,540
    + 折 460,570→280,440 + 280,440→430,400 + 点 500,450)
    / 小(丨 x=500 340→0 / 撇 500,340→250,60 / 点 600,340→820,150)。
    """
    g = Glyph("uni7CFB", advance=1000, unicode=0x7CFB, note="系 7画 丿+幺+小")
    g.diag(430, 760, 240, 690, weight=W_MAIN)
    # 幺：上下两个折角（每角两笔，转折处两侧角点错开 ≥17 单位）
    g.diag(520, 700, 340, 575, weight=W_MAIN)
    g.diag(340, 575, 480, 540, weight=W_MAIN)
    g.diag(460, 570, 280, 440, weight=W_MAIN)
    g.diag(280, 440, 430, 400, weight=W_MAIN)
    dot_hk(g, 500, 450, w=W_DOT, h=112)
    # 小
    vbar(g, 500, 340, 0, W_MAIN)
    g.diag(500, 340, 250, 60, weight=W_MAIN)
    g.diag(600, 340, 820, 150, weight=W_MAIN)
    return g


def uni6279() -> Glyph:
    """批 7画 —— ⿰扌比。

    扌（x 62..368）：一(70..320 上缘 700) + 丨(x=190, 800→120 + 钩) + 提(85,380→320,500)。
    比（x 382..896）：左匕(横 400..520 上缘 640 + 竖 x=520 610→140 + 提 420,180→520,260)
    + 右匕(撇 820,700→660,615 + 竖 x=760 800→140 + 钩 880)。
    """
    g = Glyph("uni6279", advance=1000, unicode=0x6279, note="批 7画 ⿰扌比")
    # 扌
    bar_at(g, 70, 320, 700, W_MAIN)
    vbar(g, 190, 800, 120, W_MAIN)
    hook_left(g, 190, 160)
    g.diag(85, 380, 320, 500, weight=W_SEC)
    # 比
    bar_at(g, 400, 520, 640, W_THIN)
    vbar(g, 520, 610, 140, W_MAIN)
    g.diag(420, 180, 520, 260, weight=W_THIN)
    g.diag(820, 700, 660, 615, weight=W_THIN)
    vbar(g, 760, 800, 140, W_MAIN)
    hook_right(g, 760, 150)
    return g


def uni90CE() -> Glyph:
    """郎 8画 —— ⿰艮阝。

    左 艮（x 62..500）：フ(横 110..460 上缘 800 + 竖 460 770→430) + 一(上缘 640)
    + 一(上缘 500) + 丨(x=110, 770→130) + 撇(240,430→130,160) + 捺(300,420→470,140)。
    右 阝（邑偏，x 700..908）：右竖 x=860 + 左侧折返耳肚。
    """
    g = Glyph("uni90CE", advance=1000, unicode=0x90CE, note="郎 8画 ⿰艮阝")
    # 艮
    bar_at(g, 110, 460, 800, W_MAIN)
    vbar(g, 460, 770, 430, W_MAIN)
    bar_at(g, 110, 460, 640, W_THIN)
    bar_at(g, 110, 460, 500, W_MAIN)
    vbar(g, 110, 770, 130, W_MAIN)
    g.diag(240, 430, 130, 160, weight=W_SEC)
    g.diag(300, 420, 470, 140, weight=W_SEC)
    # 邑偏
    comp_ear_right(g)
    return g


def uni6613() -> Glyph:
    """易 8画 —— ⿱日勿。

    日（y 354..800）：两竖 260/740 + 三横（上缘 800 / 620 / 450）。
    勿（y 130..330）：撇(400,430→260,140) + 𠃌(横 380..880 上缘 330 + 竖 880 282→180 + 钩)
    + 撇(560,282→430,130) + 撇(720,282→570,130)。
    2026-10-31 回修：日的下横（358..450）与勿的横（334..430）白口 −72，日部糊成一团；
    勿整体下移 100 → 白口 28。参照 M PLUS 1p Black「易」实测：日部 2 腔，腔高 40、宽 360。
    """
    g = Glyph("uni6613", advance=1000, unicode=0x6613, note="易 8画 ⿱日勿")
    # 日
    vbar(g, 260, 770, 400, W_SEC)
    vbar(g, 740, 770, 400, W_SEC)
    bar_at(g, 260, 740, 800, W_SEC)
    bar_at(g, 260, 740, 620, W_THIN)
    bar_at(g, 260, 740, 450, W_SEC)
    # 勿
    g.diag(400, 430, 260, 140, weight=W_SEC)
    bar_at(g, 380, 880, 330, W_MAIN)
    vbar(g, 880, 282, 180, W_MAIN)
    hook_left(g, 880, 200, dx=-70, dy=-30)
    g.diag(560, 282, 430, 130, weight=W_SEC)
    g.diag(720, 282, 570, 130, weight=W_SEC)
    return g


def uni901F() -> Glyph:
    """速 9画 —— ⿺辶束。

    辶：点(120,740) + 折(横 75..215 上缘 580 + 撇 220,535→120,320)
    + 捺(120,270→880,110)。
    束（x 378..901）：一(330..880 上缘 790) + 丨(x=600, 800→60) + 口框(450..770, 420..640)
    + 撇(600,450→400,200) + 捺(630,460→860,130)。
    """
    g = Glyph("uni901F", advance=1000, unicode=0x901F, note="速 9画 ⿺辶束")
    # 辶
    dot_hk(g, 120, 740, h=96)
    bar_at(g, 75, 215, 580, W_THIN)
    g.diag(220, 535, 120, 320, weight=W_THIN)
    g.diag(120, 270, 880, 110, weight=W_THIN)
    # 束
    bar_at(g, 330, 880, 790, W_THIN)
    vbar(g, 600, 800, 60, W_THIN)
    vbar(g, 450, 610, 420, W_THIN)
    vbar(g, 770, 610, 420, W_THIN)
    bar_at(g, 450, 770, 640, W_THIN)
    bar_at(g, 450, 770, 450, W_THIN)
    g.diag(600, 450, 400, 200, weight=W_THIN)
    g.diag(630, 460, 860, 130, weight=W_THIN)
    return g


def uni5B58() -> Glyph:
    """存 6画 —— ⿸𠂇子。

    𠂇：一(70..560 上缘 720) + 撇(480,720→130,200)。
    子：乛(横 470..900 上缘 560 + 折 865,500→750,400)
    + 一(420..900 上缘 320) + 亅(x=660, 530→90 + 钩)。
    """
    g = Glyph("uni5B58", advance=1000, unicode=0x5B58, note="存 6画 ⿸𠂇子")
    bar_at(g, 70, 560, 720, W_MAIN)
    g.diag(480, 720, 130, 200, weight=W_MAIN)
    bar_at(g, 470, 900, 560, W_MAIN)
    g.diag(865, 500, 750, 400, weight=W_SEC)
    bar_at(g, 420, 900, 320, W_MAIN)
    vbar(g, 660, 530, 90, W_MAIN)
    hook_left(g, 660, 130)
    return g


# --------------------------------------------------------------------------
def build() -> list[Glyph]:
    return [
        uni6BB5(),  # 段
        uni578B(),  # 型
        uni5B57(),  # 字
        uni6CC1(),  # 況
        uni97F3(),  # 音
        uni6CE8(),  # 注
        uni547C(),  # 呼
        uni826F(),  # 良
        uni962A(),  # 阪
        uni5C02(),  # 専
        uni8C37(),  # 谷
        uni7A81(),  # 突
        uni5175(),  # 兵
        uni5149(),  # 光
        uni79D1(),  # 科
        uni653B(),  # 攻
        uni52B9(),  # 効
        uni56F3(),  # 図
        uni7701(),  # 省
        uni5BA4(),  # 室
        uni6B69(),  # 歩
        uni5CB8(),  # 岸
        uni5BA2(),  # 客
        uni5426(),  # 否
        uni5468(),  # 周
        uni6750(),  # 材
        uni7CFB(),  # 系
        uni6279(),  # 批
        uni90CE(),  # 郎
        uni6613(),  # 易
        uni901F(),  # 速
        uni5B58(),  # 存
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-007.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
