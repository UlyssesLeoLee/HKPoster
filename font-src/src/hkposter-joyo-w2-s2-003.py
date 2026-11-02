"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-003。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
* 字面框 x 60..940 / y 0..820，advance 1000，与 zh-HK 繁体完全一致，便于中日英混排。
* 笔画权重四档：主 96 / 次 92 / 细 84 / 点 84。笔画少的字（6 画）以 96 为主；
  笔画多的字（8–9 画）在密排处把次要笔画降到 84，避免同批内"有的太轻、有的太闷"。
* 对齐语义：横画按「墨迹上缘」定位（hmid），基线横画按「墨迹下缘」定位（hbase）；
  竖画直接给「墨迹 y 范围」；斜笔画给中心线两端点，末端用 diag_to_base 按
  垂直切口模型解出，使墨迹下缘真正贴住基线。
* 同一部件（氵、亻、刂、口、儿）在批内复用同一套坐标与笔画拆法（shui / ninben /
  daoliang / kou / er），只做位置与大小的光学校正。
* 各字笔画位置以 KanjiVG 参考骨架为结构依据，再映射到本批字面框；
  密排处内白不低于 24 单位，竖与竖之间不低于 60 单位（GLY-006）。
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

INK_TOP = 820.0
INK_BOTTOM = 0.0
INK_LEFT = 60.0
INK_RIGHT = 940.0


# ---------------------------------------------------------------- 基础笔画封装

def hbar(g, x1, x2, y, w=W_MAIN):
    """横画：中心线 y，墨迹占 y±w/2。"""
    g.hbar(x1, x2, y, weight=w)


def hmid(g, x1, x2, ink_top, w=W_MAIN):
    """横画：墨迹上缘贴 ink_top（横画按上缘定位，堆叠时最直观）。"""
    g.hbar(x1, x2, ink_top - w / 2.0, weight=w)


def hbase(g, x1, x2, w=W_MAIN, base=INK_BOTTOM):
    """横画：墨迹下缘贴 base（基线横画）。"""
    g.hbar(x1, x2, base + w / 2.0, weight=w)


def vbar(g, x, y1, y2, w=W_MAIN):
    """竖画：墨迹占 y1..y2（端点即墨迹端点）。"""
    g.vbar(x, y1, y2, weight=w)


def diag(g, x1, y1, x2, y2, w=W_MAIN):
    """斜笔画：中心线两端点，厚度垂直于中心线。"""
    g.diag(x1, y1, x2, y2, weight=w)


def _ink_low(y2, x1, y1, x2, w):
    """斜笔画末端墨迹下缘（垂直切口模型）。"""
    h = w / 2.0
    dx = x2 - x1
    ln = math.hypot(dx, y2 - y1) or 1.0
    return y2 - h * abs(dx / ln)


def diag_to_base(g, x1, y1, x2, w=W_MAIN, base=INK_BOTTOM):
    """斜画：自 (x1,y1) 斜下到 x2 附近，解出中心线终点使墨迹下缘贴 base。"""
    y2 = base + 10.0
    for _ in range(80):
        y2 += base - _ink_low(y2, x1, y1, x2, w)
    g.diag(x1, y1, x2, y2, weight=w)


def diag_to_left(g, x1, y1, x2, y2, w=W_MAIN, left=INK_LEFT):
    """斜画：解出中心线终点 x2 使墨迹左缘贴 left。"""
    h = w / 2.0
    for _ in range(80):
        dy = y2 - y1
        ln = math.hypot(x2 - x1, dy) or 1.0
        x2 += left - (x2 - h * abs(dy / ln))
    g.diag(x1, y1, x2, y2, weight=w)


# ---------------------------------------------------------------- 重复部件库

def shui(g, dx=0.0, dy=0.0):
    """氵（三点水）左偏旁：点、点、提。墨迹 x 86..248 / y 115..769。

    笔画拆法全批统一（派/活/海 复用），只随整字做位置平移。
    """
    diag(g, 150 + dx, 730 + dy, 225 + dx, 700 + dy, w=W_DOT)
    diag(g, 115 + dx, 545 + dy, 190 + dx, 515 + dy, w=W_DOT)
    diag(g, 120 + dx, 140 + dy, 195 + dx, 240 + dy, w=W_DOT)


def ninben(g, dx=0.0):
    """亻（单人旁）：撇 + 竖。墨迹 x 66..289 / y 60..784。

    撇自右上向左下，末端左缘贴 60；竖自撇身中段落到基线附近。
    """
    diag(g, 245 + dx, 765, 110 + dx, 445, w=W_MAIN)
    vbar(g, 215 + dx, 60, 660, w=W_SEC)


def daoliang(g, dx=0.0, short_bot=310.0, long_bot=60.0):
    """刂（立刀旁）：短竖 + 长竖带钩。墨迹 x 602..868。

    短竖 x=648，长竖 x=822，钩向左微上。
    """
    vbar(g, 648 + dx, short_bot, 680, w=W_SEC)
    vbar(g, 822 + dx, long_bot, 800, w=W_MAIN)
    diag(g, 822 + dx, long_bot + 30, 775 + dx, long_bot + 58, w=W_THIN)


def kou(g, x1, x2, y_top, y_bottom, w=W_SEC):
    """口：以 竖 / 横折 / 横 三笔拆出的空心方框，墨迹框恰为 x1..x2 / y_bottom..y_top。"""
    hmid(g, x1, x2, y_top, w=w)
    vbar(g, x1 + w / 2.0, y_bottom, y_top, w=w)
    vbar(g, x2 - w / 2.0, y_bottom, y_top, w=w)
    hbase(g, x1, x2, w=w, base=y_bottom)


def er(g, x_left=350.0, x_right=600.0, y_top=360.0, left_bot=90.0, right_bot=60.0):
    """儿：左撇 + 右竖弯钩（先/売 复用骨架）。"""
    diag(g, x_left, y_top, x_left - 125, left_bot, w=W_MAIN)
    vbar(g, x_right, right_bot, y_top + 20, w=W_MAIN)
    diag(g, x_right, right_bot + 30, x_right + 200, right_bot + 90, w=W_SEC)


# ---------------------------------------------------------------- 字形

def uni6D3E() -> Glyph:
    """派 U+6D3E —— 9 画：氵(3) + 派右部(6)。

    部件分区：氵 x 86..248（shui()）；派右部 x 249..909 / y 62..812。
    笔画清单：
      1 氵点(上)  diag(150,730)->(225,700) w84
      2 氵点(中)  diag(115,545)->(190,515) w84
      3 氵提      diag(120,140)->(195,240) w84
      4 撇(顶)    diag(595,770)->(425,655) w84
      5 撇(左长)  diag(350,615)->(290,95) w84
      6 撇(中)    diag(700,630)->(595,560) w84
      7 竖        vbar(530, 82..554) w92
      8 撇(右)    diag(790,545)->(670,480) w84
      9 捺(右下)  diag(630,480)->(870,150) w96
    """
    g = Glyph("uni6D3E", advance=1000, unicode=0x6D3E, note="派：氵 + 派右部")
    shui(g)
    diag(g, 595, 770, 425, 655, w=W_DOT)
    diag(g, 350, 615, 290, 95, w=W_DOT)
    diag(g, 700, 630, 595, 560, w=W_DOT)
    vbar(g, 530, 82, 554, w=W_SEC)
    diag(g, 790, 545, 670, 480, w=W_DOT)
    diag(g, 630, 480, 870, 150, w=W_MAIN)
    return g


def uni70B9() -> Glyph:
    """点 U+70B9 —— 9 画：卜(2) + 口(3) + 灬(4)。

    部件分区：卜 x 422..717 / y 506..820；口 x 300..720 / y 260..510；灬 满宽 x 104..896 / y 47..220。
    笔画清单：
      1 卜竖   vbar(470, 506..820) w96
      2 卜横   hmid(470,717, 墨迹上缘 660) w92
      3 口上横 hmid(300,720, 510) w92
      4 口左竖 vbar(346, 260..510) w92
      5 口右竖 vbar(674, 260..510) w92
      6 口下横 hbase(300,720) w92
      7-10 灬四点 diag(130,175)->(85,75) 等四点 w84
    """
    g = Glyph("uni70B9", advance=1000, unicode=0x70B9, note="点：卜 + 口 + 灬")
    vbar(g, 470, 506, 820, w=W_MAIN)
    hmid(g, 470, 717, 660, w=W_SEC)
    kou(g, 300, 720, 510, 260, w=W_SEC)
    for cx in (130, 370, 600, 830):
        diag(g, cx + 40, 175, cx, 75, w=W_DOT)
    return g


def uni5E9C() -> Glyph:
    """府 U+5E9C —— 8 画：广(3) + 付(5)。

    部件分区：广 x 60..900 / y 155..818；付 = 亻(x 230..425) + 寸(x 434..905)。
    笔画清单：
      1 广点   diag(470,800)->(502,730) w84
      2 广横   hmid(170,900, 墨迹上缘 707) w92
      3 广撇   diag_to_base(200,654 -> 110) w96
      4 亻撇   diag(390,600)->(265,455) w92
      5 亻竖   vbar(336, 71..440) w92
      6 寸横   hmid(434,905, 墨迹上缘 477) w92
      7 寸竖钩 vbar(700, 78..620) w92 + 钩 diag(700,95)->(640,125) w84
      8 寸点   diag(545,300)->(505,255) w84
    """
    g = Glyph("uni5E9C", advance=1000, unicode=0x5E9C, note="府：广 + 付")
    diag(g, 470, 800, 502, 730, w=W_DOT)
    hmid(g, 170, 900, 707, w=W_SEC)
    diag_to_base(g, 200, 654, 110, w=W_MAIN)
    diag(g, 390, 600, 265, 455, w=W_SEC)
    vbar(g, 336, 71, 440, w=W_SEC)
    hmid(g, 434, 905, 477, w=W_SEC)
    vbar(g, 700, 78, 620, w=W_MAIN)
    diag(g, 700, 95, 640, 125, w=W_THIN)
    diag(g, 545, 300, 505, 255, w=W_DOT)
    return g


def uni6D3B() -> Glyph:
    """活 U+6D3B —— 9 画：氵(3) + 舌(6)。

    部件分区：氵 x 86..248（shui()）；舌 x 409..900 / y 0..805（千在上，口在右下）。
    笔画清单：
      1-3 氵 三点水（shui()）
      4 千撇  diag(700,760)->(420,690) w92
      5 千横  hmid(330,900, 墨迹上缘 512) w92
      6 千竖  vbar(596, 330..660) w92
      7-9 口 kou(420,830, 330, 70) w92
    """
    g = Glyph("uni6D3B", advance=1000, unicode=0x6D3B, note="活：氵 + 舌")
    shui(g)
    diag(g, 700, 760, 420, 690, w=W_SEC)
    hmid(g, 330, 900, 512, w=W_SEC)
    vbar(g, 596, 330, 660, w=W_MAIN)
    kou(g, 420, 830, 330, 70, w=W_SEC)
    return g


def uni5148() -> Glyph:
    """先 U+5148 —— 6 画：丿 + 土(3) + 儿(2)。

    部件分区：上部 x 178..888 / y 460..795；下部 儿 x 118..818 / y 18..443。
    笔画清单：
      1 撇    diag(330,700)->(215,545) w92
      2 横    hmid(335,705, 墨迹上缘 654) w92
      3 竖    vbar(492, 460..795) w92
      4 横    hmid(117,888, 墨迹上缘 479) w92
      5 儿撇  diag_to_base(390,420 -> 160) w96
      6 儿竖弯钩 vbar(630, 70..439) w92 + 钩 diag(630,95)->(800,150) w92
    """
    g = Glyph("uni5148", advance=1000, unicode=0x5148, note="先：丿 + 土 + 儿")
    diag(g, 330, 700, 215, 545, w=W_SEC)
    hmid(g, 335, 705, 654, w=W_SEC)
    vbar(g, 492, 460, 795, w=W_MAIN)
    hmid(g, 117, 888, 479, w=W_SEC)
    diag_to_base(g, 390, 420, 160, w=W_MAIN)
    vbar(g, 630, 70, 439, w=W_MAIN)
    diag(g, 630, 95, 800, 150, w=W_SEC)
    return g


def uni5171() -> Glyph:
    """共 U+5171 —— 6 画：廿(4) + 八(2)。

    部件分区：廿 x 202..814 / y 363..792；八 x 123..392 / y 0..353。
    笔画清单：
      1 横 hmid(202,814, 墨迹上缘 617) w92
      2 竖 vbar(364, 384..742) w92
      3 竖 vbar(622, 400..792) w92
      4 横 hmid(94,905, 墨迹上缘 409) w92
      5 撇 diag_to_base(350,330 -> 165) w96
      6 捺 diag_to_base(650,330 -> 835) w96
    """
    g = Glyph("uni5171", advance=1000, unicode=0x5171, note="共：廿 + 八")
    hmid(g, 202, 814, 617, w=W_SEC)
    vbar(g, 364, 384, 742, w=W_SEC)
    vbar(g, 622, 400, 792, w=W_SEC)
    hmid(g, 94, 905, 409, w=W_MAIN)
    diag_to_base(g, 350, 330, 165, w=W_MAIN)
    diag_to_base(g, 650, 330, 835, w=W_MAIN)
    return g


def uni540D() -> Glyph:
    """名 U+540D —— 6 画：夕(3) + 口(3)。

    部件分区：夕 x 217..748 / y 232..813；口 x 380..810 / y 40..350。
    笔画清单：
      1 撇   diag(470,780)->(250,560) w92
      2 横撇 hmid(250,739, 墨迹上缘 729) w92 + diag(739,683)->(150,260) w96
      3 点   diag(460,540)->(410,480) w84
      4-6 口 kou(380,810, 350, 40) w92
    """
    g = Glyph("uni540D", advance=1000, unicode=0x540D, note="名：夕 + 口")
    diag(g, 470, 780, 250, 560, w=W_SEC)
    hmid(g, 250, 739, 729, w=W_SEC)
    diag(g, 739, 683, 150, 260, w=W_MAIN)
    diag(g, 460, 540, 410, 480, w=W_DOT)
    kou(g, 380, 810, 350, 40, w=W_SEC)
    return g


def uni4EA4() -> Glyph:
    """交 U+4EA4 —— 6 画：亠(2) + 父(4)。

    部件分区：亠 x 172..818 / y 631..798；下部两组乂 x 126..878 / y 0..591。
    笔画清单：
      1 点     diag(478,780)->(500,700) w84
      2 横     hmid(172,818, 墨迹上缘 670) w92
      3 短撇   diag(320,545)->(215,425) w84
      4 短捺   diag(650,555)->(780,480) w84
      5 长撇   diag_to_base(600,450 -> 165) w96
      6 长捺   diag_to_base(320,400 -> 870) w96
    """
    g = Glyph("uni4EA4", advance=1000, unicode=0x4EA4, note="交：亠 + 父")
    diag(g, 478, 780, 500, 700, w=W_DOT)
    hmid(g, 172, 818, 670, w=W_SEC)
    diag(g, 320, 545, 215, 425, w=W_DOT)
    diag(g, 650, 555, 780, 480, w=W_DOT)
    diag_to_base(g, 600, 450, 165, w=W_MAIN)
    diag_to_base(g, 320, 400, 870, w=W_MAIN)
    return g


def uni5411() -> Glyph:
    """向 U+5411 —— 6 画：丿(1) + 冂(2) + 口(3)。

    部件分区：丿 x 273..467 / y 542..758；冂 x 114..906 / y 60..620；口 x 342..645 / y 250..438。
    笔画清单：
      1 撇   diag(430,730)->(310,570) w92
      2 竖   vbar(160, 60..540) w96
      3 横折钩 hmid(160,860, 墨迹上缘 576) w96 + vbar(860, 60..576) w96 + 钩 diag(860,80)->(795,110) w84
      4-6 口 kou(342,645, 438, 250) w92
    """
    g = Glyph("uni5411", advance=1000, unicode=0x5411, note="向：丿 + 冂 + 口")
    diag(g, 430, 730, 310, 570, w=W_SEC)
    vbar(g, 160, 60, 540, w=W_MAIN)
    hmid(g, 160, 860, 576, w=W_MAIN)
    vbar(g, 860, 60, 576, w=W_MAIN)
    diag(g, 860, 80, 795, 110, w=W_THIN)
    kou(g, 342, 645, 438, 250, w=W_SEC)
    return g


def uni67FB() -> Glyph:
    """査 U+67FB —— 9 画：木(4) + 且(5)。

    部件分区：木 x 114..869 / y 392..831；且 x 118..841 / y 0..455。
    笔画清单：
      1 木横   hmid(179,763, 墨迹上缘 686) w92
      2 木竖   vbar(488, 461..802) w92
      3 木撇   diag(460,650)->(140,430) w92
      4 木捺   diag(515,650)->(845,450) w92
      5 且左竖 vbar(340, 60..420) w84
      6 且上横+右竖 hmid(357,647, 墨迹上缘 420) w84 + vbar(610, 60..420) w84
      7 且内横 hmid(359,635, 墨迹上缘 317) w84
      8 且内横 hmid(359,633, 墨迹上缘 216) w84
      9 且底横 hbase(143,841) w92
    """
    g = Glyph("uni67FB", advance=1000, unicode=0x67FB, note="査：木 + 且")
    hmid(g, 179, 763, 686, w=W_SEC)
    vbar(g, 488, 461, 802, w=W_MAIN)
    diag(g, 460, 650, 140, 430, w=W_SEC)
    diag(g, 515, 650, 845, 450, w=W_SEC)
    vbar(g, 340, 60, 420, w=W_THIN)
    hmid(g, 357, 647, 420, w=W_THIN)
    vbar(g, 610, 60, 420, w=W_THIN)
    hmid(g, 359, 635, 317, w=W_THIN)
    hmid(g, 359, 633, 216, w=W_THIN)
    hbase(g, 143, 841, w=W_SEC)
    return g


def uni9762() -> Glyph:
    """面 U+9762 —— 9 画：一(1) + 丿(1) + 外框(3) + 内部目(4)。

    部件分区：顶横 x 174..823 / y 774..820；外框 x 90..882 / y 0..620；内部 x 312..648 / y 92..600。
    笔画清单：
      1 横   hmid(174,823, 墨迹上缘 820) w92
      2 撇   diag(465,755)->(400,640) w92
      3 框左竖 vbar(136, 92..620) w92
      4 框上横 hmid(136,881, 墨迹上缘 620) w92
      5 框右竖 vbar(836, 92..620) w92
      6 框下横 hbase(174,806) w92
      7 内左竖 vbar(354, 92..600) w84
      8 内右竖 vbar(606, 92..600) w84
      9 内横一 hmid(354,606, 墨迹上缘 480) w84
      10 内横二 hmid(354,606, 墨迹上缘 320) w84
    """
    g = Glyph("uni9762", advance=1000, unicode=0x9762, note="面：一 + 外框 + 内部目")
    hmid(g, 174, 823, 820, w=W_SEC)
    diag(g, 465, 755, 400, 640, w=W_SEC)
    vbar(g, 136, 92, 620, w=W_SEC)
    hmid(g, 136, 881, 620, w=W_SEC)
    vbar(g, 836, 92, 620, w=W_SEC)
    hbase(g, 174, 806, w=W_SEC)
    vbar(g, 354, 92, 600, w=W_THIN)
    vbar(g, 606, 92, 600, w=W_THIN)
    hmid(g, 354, 606, 480, w=W_THIN)
    hmid(g, 354, 606, 320, w=W_THIN)
    return g


def uni59D4() -> Glyph:
    """委 U+59D4 —— 8 画：禾(5) + 女(3)。

    部件分区：禾 x 126..878 / y 386..825；女 x 100..932 / y 31..409。
    笔画清单：
      1 禾撇  diag(620,774)->(300,720) w92
      2 禾横  hmid(182,818, 墨迹上缘 650) w92
      3 禾竖  vbar(496, 450..721) w92
      4 禾撇  diag(455,615)->(150,425) w92
      5 禾捺  diag(525,605)->(860,465) w92
      6 女撇点 diag(570,400)->(380,190) w92 + diag(380,190)->(700,48) w92
      7 女撇  diag(640,370)->(230,70) w96
      8 女横  hmid(100,932, 墨迹上缘 336) w92
    """
    g = Glyph("uni59D4", advance=1000, unicode=0x59D4, note="委：禾 + 女")
    diag(g, 620, 774, 300, 720, w=W_SEC)
    hmid(g, 182, 818, 650, w=W_SEC)
    vbar(g, 496, 450, 721, w=W_MAIN)
    diag(g, 455, 615, 150, 425, w=W_SEC)
    diag(g, 525, 605, 860, 465, w=W_SEC)
    diag(g, 570, 400, 380, 190, w=W_SEC)
    diag(g, 380, 190, 700, 48, w=W_SEC)
    diag(g, 640, 370, 230, 70, w=W_MAIN)
    hmid(g, 100, 932, 336, w=W_SEC)
    return g


def uni544A() -> Glyph:
    """告 U+544A —— 7 画：丿 + 二 + 丨 + 口(3)。

    部件分区：上部 x 88..880 / y 399..815；口 x 257..738 / y 45..310。
    笔画清单：
      1 撇   diag(290,715)->(180,540) w92
      2 横   hmid(286,707, 墨迹上缘 637) w92
      3 横   hmid(88,880, 墨迹上缘 445) w92
      4 竖   vbar(490, 431..815) w92
      5-7 口 kou(257,738, 310, 45) w92
    """
    g = Glyph("uni544A", advance=1000, unicode=0x544A, note="告：丿 + 二 + 丨 + 口")
    diag(g, 290, 715, 180, 540, w=W_SEC)
    hmid(g, 286, 707, 637, w=W_SEC)
    hmid(g, 88, 880, 445, w=W_SEC)
    vbar(g, 490, 431, 815, w=W_MAIN)
    kou(g, 257, 738, 310, 45, w=W_SEC)
    return g


def uni8ECD() -> Glyph:
    """軍 U+8ECD —— 9 画：冖(2) + 車(7)。

    部件分区：冖 x 118..834 / y 597..760；車 x 221..874 / y 47..737。
    笔画清单：
      1 冖竖   vbar(164, 600..760) w92
      2 冖横钩 hmid(201,833, 墨迹上缘 780) w92 + vbar(787, 695..780) w92
      3 車上横 hmid(288,690, 墨迹上缘 663) w84
      4 車左竖 vbar(263, 256..549) w84
      5 車上横+右竖 hmid(266,744, 墨迹上缘 570) w84 + vbar(702, 256..570) w84
      6 車内横 hmid(285,718, 墨迹上缘 464) w84
      7 車内横 hmid(301,687, 墨迹上缘 359) w84
      8 車底横 hmid(119,874, 墨迹上缘 256) w92
      9 車中竖 vbar(488, 47..737) w92
    """
    g = Glyph("uni8ECD", advance=1000, unicode=0x8ECD, note="軍：冖 + 車")
    vbar(g, 164, 600, 760, w=W_SEC)
    hmid(g, 201, 833, 780, w=W_SEC)
    vbar(g, 787, 695, 780, w=W_SEC)
    hmid(g, 288, 690, 663, w=W_THIN)
    vbar(g, 263, 256, 549, w=W_THIN)
    hmid(g, 266, 744, 570, w=W_THIN)
    vbar(g, 702, 256, 570, w=W_THIN)
    hmid(g, 285, 718, 464, w=W_THIN)
    hmid(g, 301, 687, 359, w=W_THIN)
    hmid(g, 119, 874, 256, w=W_SEC)
    vbar(g, 488, 47, 737, w=W_SEC)
    return g


def uni91CD() -> Glyph:
    """重 U+91CD —— 9 画：丿(1) + 一(1) + 目(5) + 一(1) + 丨(1)。

    部件分区：顶撇 x 239..611 / y 659..831；目 x 245..758 / y 178..570；底横 x 130..836 / y 64..110。
    笔画清单：
      1 撇     diag(600,779)->(250,700) w84
      2 横     hmid(89,876, 墨迹上缘 700) w84
      3 目左竖 vbar(266, 260..570) w84
      4 目上横 hmid(266,758, 墨迹上缘 570) w84
      5 目右竖 vbar(716, 290..570) w84
      6 目内横 hmid(283,732, 墨迹上缘 460) w84
      7 目内横 hmid(295,711, 墨迹上缘 340) w84
      8 目底横 hmid(273,729, 墨迹上缘 220) w84
      9 底横   hmid(130,836, 墨迹上缘 110) w84
      10 长竖  vbar(490, 60..700) w84
    """
    g = Glyph("uni91CD", advance=1000, unicode=0x91CD, note="重：丿 + 一 + 目 + 一 + 丨")
    diag(g, 600, 779, 250, 700, w=W_THIN)
    hmid(g, 89, 876, 700, w=W_THIN)
    vbar(g, 266, 260, 570, w=W_THIN)
    hmid(g, 266, 758, 570, w=W_THIN)
    vbar(g, 716, 290, 570, w=W_THIN)
    hmid(g, 283, 732, 460, w=W_THIN)
    hmid(g, 295, 711, 340, w=W_THIN)
    hmid(g, 273, 729, 220, w=W_THIN)
    hmid(g, 130, 836, 110, w=W_THIN)
    vbar(g, 490, 60, 700, w=W_THIN)
    return g


def uni8FD1() -> Glyph:
    """近 U+8FD1 —— 6 画：辶(3) + 斤(3)。

    部件分区：辶 x 81..865 / y 54..501；斤 x 325..876 / y 166..820。
    笔画清单：
      1 辶点   diag(260,730)->(175,660) w84
      2 辶折撇 hmid(89,271, 墨迹上缘 498) w84 + diag(271,477)->(120,230) w92
      3 辶捺   diag(120,185)->(860,100) w92
      4 斤撇   diag(710,780)->(480,700) w84
      5 斤撇   diag(440,670)->(370,300) w92
      6 斤横   hmid(479,876, 墨迹上缘 582) w92
      7 斤竖   vbar(686, 166..563) w92
    """
    g = Glyph("uni8FD1", advance=1000, unicode=0x8FD1, note="近：辶 + 斤")
    diag(g, 260, 730, 175, 660, w=W_DOT)
    hmid(g, 89, 271, 498, w=W_THIN)
    diag(g, 271, 477, 120, 230, w=W_SEC)
    diag(g, 120, 185, 860, 100, w=W_SEC)
    diag(g, 710, 780, 480, 700, w=W_DOT)
    diag(g, 440, 670, 370, 300, w=W_SEC)
    hmid(g, 479, 876, 582, w=W_SEC)
    vbar(g, 686, 166, 563, w=W_SEC)
    return g


def uni8003() -> Glyph:
    """考 U+8003 —— 6 画：耂(4) + 丂(2)。

    部件分区：耂 x 92..921 / y 261..823；丂 x 409..758 / y 53..481。
    笔画清单：
      1 横   hmid(304,650, 墨迹上缘 711) w84
      2 竖   vbar(486, 571..815) w92
      3 横   hmid(92,911, 墨迹上缘 592) w92
      4 撇   diag(750,770)->(120,300) w96
      5 横   hmid(496,711, 墨迹上缘 481) w92
      6 竖钩 vbar(620, 67..435) w92 + 钩 diag(620,90)->(450,120) w84
    """
    g = Glyph("uni8003", advance=1000, unicode=0x8003, note="考：耂 + 丂")
    hmid(g, 304, 650, 711, w=W_THIN)
    vbar(g, 486, 571, 815, w=W_MAIN)
    hmid(g, 92, 911, 592, w=W_SEC)
    diag(g, 750, 770, 120, 300, w=W_MAIN)
    hmid(g, 496, 711, 481, w=W_SEC)
    vbar(g, 620, 67, 435, w=W_SEC)
    diag(g, 620, 90, 450, 120, w=W_THIN)
    return g


def uni5224() -> Glyph:
    """判 U+5224 —— 7 画：半(5) + 刂(2)。

    部件分区：半 x 95..553 / y 47..778；刂 x 602..868 / y 79..803。
    笔画清单：
      1 撇(丶) diag(160,690)->(215,620) w84
      2 捺(丿) diag(510,730)->(440,630) w84
      3 横      hmid(143,504, 墨迹上缘 519) w92
      4 横      hmid(95,553, 墨迹上缘 364) w92
      5 竖      vbar(330, 47..778) w92
      6-7 刂（daoliang：短竖 648 + 长竖 822 带钩）
    """
    g = Glyph("uni5224", advance=1000, unicode=0x5224, note="判：半 + 刂")
    diag(g, 160, 690, 215, 620, w=W_DOT)
    diag(g, 510, 730, 440, 630, w=W_DOT)
    hmid(g, 143, 504, 519, w=W_SEC)
    hmid(g, 95, 553, 364, w=W_SEC)
    vbar(g, 330, 47, 778, w=W_MAIN)
    daoliang(g)
    return g


def uni753B() -> Glyph:
    """画 U+753B —— 8 画：一(1) + 田(5) + 凵(2)。

    部件分区：一 x 217..770 / y 774..820；田 x 246..730 / y 258..587；凵 x 118..910 / y 0..585。
    笔画清单：
      1 横   hmid(217,770, 墨迹上缘 820) w92
      2 田左竖 vbar(288, 273..587) w84
      3 田上横 hmid(288,720, 墨迹上缘 587) w84
      4 田右竖 vbar(688, 273..587) w84
      5 田中竖 vbar(488, 273..587) w84
      6 田内横 hmid(310,691, 墨迹上缘 450) w84
      7 田下横 hmid(327,668, 墨迹上缘 300) w84
      8 凵竖折 vbar(164, 92..503) w84 + hbase(138,840) w84
      9 凵右竖 vbar(864, 92..585) w84
    """
    g = Glyph("uni753B", advance=1000, unicode=0x753B, note="画：一 + 田 + 凵")
    hmid(g, 217, 770, 820, w=W_SEC)
    vbar(g, 288, 273, 587, w=W_THIN)
    hmid(g, 288, 720, 587, w=W_THIN)
    vbar(g, 688, 273, 587, w=W_THIN)
    vbar(g, 488, 273, 587, w=W_THIN)
    hmid(g, 310, 691, 450, w=W_THIN)
    hmid(g, 327, 668, 300, w=W_THIN)
    vbar(g, 164, 92, 503, w=W_THIN)
    hbase(g, 138, 840, w=W_THIN)
    vbar(g, 864, 92, 585, w=W_THIN)
    return g


def uni6D77() -> Glyph:
    """海 U+6D77 —— 9 画：氵(3) + 每(6)。

    部件分区：氵 x 86..248（shui()）；每 x 306..943 / y 77..814。
    笔画清单：
      1-3 氵 三点水（shui()）
      4 每撇   diag(470,790)->(345,590) w92
      5 每横   hmid(463,806, 墨迹上缘 736) w92
      6 每框   kou(350,860, 590, 115) w92
      7 每竖   vbar(567, 233..561) w92
      8 每中横 hmid(261,935, 墨迹上缘 425) w92
      9-10 每两点 diag(665,505)->(620,455) / diag(665,295)->(620,245) w84
    """
    g = Glyph("uni6D77", advance=1000, unicode=0x6D77, note="海：氵 + 每")
    shui(g)
    diag(g, 470, 790, 345, 590, w=W_SEC)
    hmid(g, 463, 806, 736, w=W_SEC)
    kou(g, 350, 860, 590, 115, w=W_SEC)
    vbar(g, 567, 233, 561, w=W_MAIN)
    hmid(g, 261, 935, 425, w=W_SEC)
    diag(g, 665, 505, 620, 455, w=W_DOT)
    diag(g, 665, 295, 620, 245, w=W_DOT)
    return g


def uni53C2() -> Glyph:
    """参 U+53C2 —— 8 画：厶(2) + 大(3) + 彡(3)。

    部件分区：厶 x 255..697 / y 606..840；大 x 76..877 / y 264..634；彡 x 245..635 / y 51..467。
    笔画清单：
      1 撇折 diag(620,778)->(280,660) w92 + hmid(280,645, 墨迹上缘 660) w92
      2 点     diag(600,740)->(665,665) w84
      3 横     hmid(99,838, 墨迹上缘 557) w92
      4 撇     diag(420,600)->(110,290) w96
      5 捺     diag(525,580)->(845,300) w96
      6-8 彡   diag(480,430)->(300,330) / diag(545,320)->(330,225) / diag(620,230)->(260,90) w84
    """
    g = Glyph("uni53C2", advance=1000, unicode=0x53C2, note="参：厶 + 大 + 彡")
    diag(g, 620, 778, 280, 660, w=W_SEC)
    hmid(g, 280, 645, 660, w=W_SEC)
    diag(g, 600, 740, 665, 665, w=W_DOT)
    hmid(g, 99, 838, 557, w=W_MAIN)
    diag(g, 420, 600, 110, 290, w=W_MAIN)
    diag(g, 525, 580, 845, 300, w=W_MAIN)
    diag(g, 480, 430, 300, 330, w=W_THIN)
    diag(g, 545, 320, 330, 225, w=W_THIN)
    diag(g, 620, 230, 260, 90, w=W_THIN)
    return g


def uni58F2() -> Glyph:
    """売 U+58F2 —— 7 画：士(3) + 冖(2) + 儿(2)。

    部件分区：士 x 241..727 / y 546..822；冖 x 70..875 / y 383..483；儿 x 182..812 / y 50..371。
    笔画清单：
      1 横   hmid(241,727, 墨迹上缘 717) w92
      2 竖   vbar(488, 580..815) w92
      3 横   hmid(275,716, 墨迹上缘 592) w92
      4 冖竖 vbar(116, 303..448) w92
      5 冖横钩 hmid(155,875, 墨迹上缘 483) w92 + vbar(829, 383..483) w92
      6 儿撇 diag(350,355)->(225,90) w96
      7 儿竖弯钩 vbar(600, 60..380) w92 + 钩 diag(600,90)->(800,150) w84
    """
    g = Glyph("uni58F2", advance=1000, unicode=0x58F2, note="売：士 + 冖 + 儿")
    hmid(g, 241, 727, 717, w=W_SEC)
    vbar(g, 488, 580, 815, w=W_MAIN)
    hmid(g, 275, 716, 592, w=W_SEC)
    vbar(g, 116, 303, 448, w=W_SEC)
    hmid(g, 155, 875, 483, w=W_SEC)
    vbar(g, 829, 383, 483, w=W_SEC)
    diag(g, 350, 355, 225, 90, w=W_MAIN)
    vbar(g, 600, 60, 380, w=W_SEC)
    diag(g, 600, 90, 800, 150, w=W_THIN)
    return g


def uni5229() -> Glyph:
    """利 U+5229 —— 7 画：禾(5) + 刂(2)。

    部件分区：禾 x 72..495 / y 56..824；刂 x 602..868 / y 58..803。
    笔画清单：
      1 撇   diag(410,774)->(130,700) w92
      2 横   hmid(78,503, 墨迹上缘 561) w92
      3 竖   vbar(321, 56..683) w92
      4 撇   diag(300,520)->(110,230) w92
      5 捺   diag(400,450)->(465,395) w92
      6-7 刂（daoliang）
    """
    g = Glyph("uni5229", advance=1000, unicode=0x5229, note="利：禾 + 刂")
    diag(g, 410, 774, 130, 700, w=W_SEC)
    hmid(g, 78, 503, 561, w=W_SEC)
    vbar(g, 321, 56, 683, w=W_MAIN)
    diag(g, 300, 520, 110, 230, w=W_SEC)
    diag(g, 400, 450, 465, 395, w=W_SEC)
    daoliang(g)
    return g


def uni77E5() -> Glyph:
    """知 U+77E5 —— 8 画：矢(5) + 口(3)。

    部件分区：矢 x 67..511 / y 99..771；口 x 548..878 / y 267..532。
    笔画清单：
      1 撇   diag(250,750)->(150,560) w92
      2 横   hmid(244,474, 墨迹上缘 638) w92
      3 横   hmid(80,496, 墨迹上缘 440) w92
      4 撇   diag(330,580)->(110,120) w96
      5 捺   diag(360,320)->(480,210) w92
      6-8 口 kou(548,878, 532, 267) w92
    """
    g = Glyph("uni77E5", advance=1000, unicode=0x77E5, note="知：矢 + 口")
    diag(g, 250, 750, 150, 560, w=W_SEC)
    hmid(g, 244, 474, 638, w=W_SEC)
    hmid(g, 80, 496, 440, w=W_SEC)
    diag(g, 330, 580, 110, 120, w=W_MAIN)
    diag(g, 360, 320, 480, 210, w=W_SEC)
    kou(g, 548, 878, 532, 267, w=W_SEC)
    return g


def uni4FE1() -> Glyph:
    """信 U+4FE1 —— 9 画：亻(2) + 言(7)。

    部件分区：亻 x 66..289（ninben()）；言 x 375..903 / y 67..807。
    笔画清单：
      1-2 亻（ninben()）
      3 言点 diag(570,780)->(620,720) w84
      4 横   hmid(375,903, 墨迹上缘 644) w92
      5 横   hmid(482,774, 墨迹上缘 520) w84
      6 横   hmid(490,770, 墨迹上缘 403) w84
      7-9 口 kou(469,799, 294, 69) w84
      2026-10-31 回修：言的三与口上横白口 −5 → 整字下移 30，白口 25。
    """
    g = Glyph("uni4FE1", advance=1000, unicode=0x4FE1, note="信：亻 + 言")
    ninben(g)
    diag(g, 570, 780, 620, 720, w=W_DOT)
    hmid(g, 375, 903, 644, w=W_SEC)
    hmid(g, 482, 774, 520, w=W_THIN)
    hmid(g, 490, 770, 403, w=W_THIN)
    kou(g, 469, 799, 294, 69, w=W_THIN)
    return g


def uni5728() -> Glyph:
    """在 U+5728 —— 6 画：一(1) + 丿(1) + 土(3)。

    部件分区：上横 x 162..816 / y 593..639；长撇 x 87..523 / y 0..722；土 x 326..890 / y 76..560。
    笔画清单：
      1 横 hmid(162,816, 墨迹上缘 639) w92
      2 撇 diag_to_base(480,700 -> 130) w96
      3 竖 vbar(597, 119..560) w92
      4 横 hmid(387,805, 墨迹上缘 341) w92
      5 横 hbase(326,890) w92
    """
    g = Glyph("uni5728", advance=1000, unicode=0x5728, note="在：一 + 丿 + 土")
    hmid(g, 162, 816, 639, w=W_SEC)
    diag_to_base(g, 480, 700, 130, w=W_MAIN)
    vbar(g, 597, 119, 560, w=W_MAIN)
    hmid(g, 387, 805, 341, w=W_SEC)
    hbase(g, 326, 890, w=W_SEC)
    return g


def uni4EF6() -> Glyph:
    """件 U+4EF6 —— 6 画：亻(2) + 牛(4)。

    部件分区：亻 x 66..289（ninben()）；牛 x 291..932 / y 67..799。
    笔画清单：
      1-2 亻（ninben()）
      3 撇 diag(450,710)->(330,520) w92
      4 横 hmid(427,853, 墨迹上缘 620) w92
      5 横 hmid(335,932, 墨迹上缘 419) w92
      6 竖 vbar(635, 67..799) w92
    """
    g = Glyph("uni4EF6", advance=1000, unicode=0x4EF6, note="件：亻 + 牛")
    ninben(g)
    diag(g, 450, 710, 330, 520, w=W_SEC)
    hmid(g, 427, 853, 620, w=W_SEC)
    hmid(g, 335, 932, 419, w=W_SEC)
    vbar(g, 635, 67, 799, w=W_MAIN)
    return g


def uni56E3() -> Glyph:
    """団 U+56E3 —— 6 画：囗(3) + 寸(3)。

    部件分区：囗 x 92..849 / y 0..783；寸 x 248..748 / y 216..568。
    笔画清单：
      1 竖   vbar(138, 60..752) w96
      2 横折 hmid(159,849, 墨迹上缘 783) w96 + vbar(803, 60..783) w96
      3 横   hbase(160,838) w96
      4 寸横 hmid(248,748, 墨迹上缘 568) w92
      5 寸竖钩 vbar(563, 216..693) w92 + 钩 diag(563,235)->(490,268) w84
      6 寸点 diag(420,420)->(365,340) w84
    """
    g = Glyph("uni56E3", advance=1000, unicode=0x56E3, note="団：囗 + 寸")
    vbar(g, 138, 60, 752, w=W_MAIN)
    hmid(g, 159, 849, 783, w=W_MAIN)
    vbar(g, 803, 60, 783, w=W_MAIN)
    hbase(g, 160, 838, w=W_MAIN)
    hmid(g, 248, 748, 568, w=W_SEC)
    vbar(g, 563, 216, 693, w=W_SEC)
    diag(g, 563, 235, 490, 268, w=W_THIN)
    diag(g, 420, 420, 365, 340, w=W_DOT)
    return g


def uni5225() -> Glyph:
    """別 U+5225 —— 7 画：口(3) + 力(2) + 刂(2)。

    部件分区：口 x 157..500 / y 560..755；力 x 74..488 / y 90..555；刂 x 602..868 / y 79..782。
    笔画清单：
      1-3 口 kou(157,500, 755, 560) w92
      4 横折钩 hmid(269,488, 墨迹上缘 483) w92 + vbar(442, 108..483) w92 + 钩 diag(442,130)->(310,170) w84
      5 撇   diag(300,530)->(115,230) w96
      6-7 刂（daoliang）
    """
    g = Glyph("uni5225", advance=1000, unicode=0x5225, note="別：口 + 力 + 刂")
    kou(g, 157, 500, 755, 560, w=W_SEC)
    hmid(g, 269, 488, 483, w=W_SEC)
    vbar(g, 442, 108, 483, w=W_SEC)
    diag(g, 442, 130, 310, 170, w=W_THIN)
    diag(g, 300, 530, 115, 230, w=W_MAIN)
    daoliang(g, short_bot=337, long_bot=79)
    return g


def uni7269() -> Glyph:
    """物 U+7269 —— 8 画：牛(4) + 勿(4)。

    部件分区：牛 x 72..435 / y 73..784；勿 x 437..905 / y 107..775。
    笔画清单：
      1 撇   diag(190,690)->(110,470) w92
      2 横   hmid(199,435, 墨迹上缘 596) w92
      3 竖   vbar(315, 73..784) w92
      4 横   hmid(105,393, 墨迹上缘 430) w92
      5 撇   diag(610,750)->(475,545) w92
      6 横折钩 hmid(551,905, 墨迹上缘 609) w92 + vbar(859, 107..609) w92 + 钩 diag(859,130)->(790,165) w84
      7 撇   diag(600,520)->(430,320) w84
      8 撇   diag(765,540)->(535,200) w84
    """
    g = Glyph("uni7269", advance=1000, unicode=0x7269, note="物：牛 + 勿")
    diag(g, 190, 690, 110, 470, w=W_SEC)
    hmid(g, 199, 435, 596, w=W_SEC)
    vbar(g, 315, 73, 784, w=W_MAIN)
    hmid(g, 105, 393, 430, w=W_SEC)
    diag(g, 610, 750, 475, 545, w=W_SEC)
    hmid(g, 551, 905, 609, w=W_SEC)
    vbar(g, 859, 107, 609, w=W_SEC)
    diag(g, 859, 130, 790, 165, w=W_THIN)
    diag(g, 600, 520, 430, 320, w=W_THIN)
    diag(g, 765, 540, 535, 200, w=W_THIN)
    return g


def uni4EFB() -> Glyph:
    """任 U+4EFB —— 6 画：亻(2) + 壬(4)。

    部件分区：亻 x 66..289（ninben()）；壬 x 408..884 / y 0..788。
    笔画清单：
      1-2 亻（ninben()）
      3 撇 diag(720,745)->(425,630) w92
      4 横 hmid(346,922, 墨迹上缘 455) w92
      5 竖 vbar(635, 92..643) w92
      6 横 hbase(416,884) w92
    """
    g = Glyph("uni4EFB", advance=1000, unicode=0x4EFB, note="任：亻 + 壬")
    ninben(g)
    diag(g, 720, 745, 425, 630, w=W_SEC)
    hmid(g, 346, 922, 455, w=W_SEC)
    vbar(g, 635, 92, 643, w=W_MAIN)
    hbase(g, 416, 884, w=W_SEC)
    return g


def uni4F7F() -> Glyph:
    """使 U+4F7F —— 8 画：亻(2) + 吏(6)。

    部件分区：亻 x 66..289（ninben()）；吏 x 383..892 / y 57..669。
    笔画清单：
      1-2 亻（ninben()）
      3 横   hmid(394,806, 墨迹上缘 669) w92
      4 口上横 hmid(383,817, 墨迹上缘 530) w92
      5 口左竖 vbar(429, 362..530) w92
      6 口右竖 vbar(771, 362..530) w92
      7 口下横 hmid(383,817, 墨迹上缘 408) w92
      8 竖   vbar(600, 82..669) w92
      9 捺   diag(410,330)->(870,100) w96
    """
    g = Glyph("uni4F7F", advance=1000, unicode=0x4F7F, note="使：亻 + 吏")
    ninben(g)
    hmid(g, 394, 806, 669, w=W_SEC)
    hmid(g, 383, 817, 530, w=W_SEC)
    vbar(g, 429, 362, 530, w=W_SEC)
    vbar(g, 771, 362, 530, w=W_SEC)
    hmid(g, 383, 817, 408, w=W_SEC)
    vbar(g, 600, 82, 669, w=W_MAIN)
    diag(g, 410, 330, 870, 100, w=W_MAIN)
    return g


# ---------------------------------------------------------------- 组装

def build() -> list[Glyph]:
    return [
        uni6D3E(),  # 派
        uni70B9(),  # 点
        uni5E9C(),  # 府
        uni6D3B(),  # 活
        uni5148(),  # 先
        uni5171(),  # 共
        uni540D(),  # 名
        uni4EA4(),  # 交
        uni5411(),  # 向
        uni67FB(),  # 査
        uni9762(),  # 面
        uni59D4(),  # 委
        uni544A(),  # 告
        uni8ECD(),  # 軍
        uni91CD(),  # 重
        uni8FD1(),  # 近
        uni8003(),  # 考
        uni5224(),  # 判
        uni753B(),  # 画
        uni6D77(),  # 海
        uni53C2(),  # 参
        uni58F2(),  # 売
        uni5229(),  # 利
        uni77E5(),  # 知
        uni4FE1(),  # 信
        uni5728(),  # 在
        uni4EF6(),  # 件
        uni56E3(),  # 団
        uni5225(),  # 別
        uni7269(),  # 物
        uni4EFB(),  # 任
        uni4F7F(),  # 使
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-003.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
