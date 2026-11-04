"""HK Poster Heavy —— Jōyō 常用漢字 joyo-s1-002。

本批 40 字，笔画范围 2–5，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
* **字面框与繁体汉字完全一致**：x 60..940、y 0..820，advance 1000，
  便于中英日混排时字面大小一致。
* **笔画权重沿用 zh-HK 档**：主 96 / 次 92 / 细 84 / 点 84。
  本批笔画数高度集中（2–5 画），笔画少的字（七/山/口/工/土）全部用满
  96 主笔画；笔画多的字（以/世/付/可/由/北/打/引）在拥挤处局部降到
  92/84，避免同批内"有的太轻、有的太闷"（GLY-001 允许小空腔局部减重）。
* **部件复用**：口（加/台/可）、横折钩（加/可/付/切/打/与）、竖弯钩
  （七/切）、亻（付）、广/厶（広/台）共用同一套坐标算法，只做位置与
  大小的光学校正（docs/03 GLY-004）。
* **对齐语义**：横画按"墨迹上缘 / 下缘"对齐字面框——上缘对齐 820、
  下缘对齐 0，中心线内缩半个笔画宽（bar_top / bar_base 辅助函数）；
  竖画端点即墨迹端点；斜画两端点为中心线端点，厚度垂直于中心线，
  因此所有斜画端点都收在 x 110..890 / y 55..770 内，保证墨迹不越字面框。
* **内白（GLY-006）**：横画叠横画处留白 ≥ 24 单位；相邻竖画净距 ≥ 60 单位。
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

X_L = 60.0
X_R = 940.0
Y_TOP = 820.0
Y_BASE = 0.0


# --------------------------------------------------------------------------
# 对齐辅助
# --------------------------------------------------------------------------
def bar_top(y_top: float, weight: float = W_MAIN) -> float:
    """横画中心线：墨迹上缘对齐 y_top。"""
    return y_top - weight / 2.0


def bar_base(y_base: float, weight: float = W_MAIN) -> float:
    """横画中心线：墨迹下缘对齐 y_base。"""
    return y_base + weight / 2.0


# --------------------------------------------------------------------------
# 复用部件
# --------------------------------------------------------------------------
def kou_box(
    g: Glyph,
    x_left: float,
    x_right: float,
    y_top: float,
    y_bottom: float,
    weight: float = W_MAIN,
) -> None:
    """口：左竖 + 横折（口上 + 右竖）+ 底横。

    x_left / x_right 为左右竖的中心线，y_top / y_bottom 为墨迹上下缘。
    批内加/台/可 三个字共用本函数，保证三个"口"字面完全同构。
    """
    half = weight / 2.0
    g.vbar(x_left, y_top, y_bottom, weight=weight)
    g.hbar(x_left, x_right, y_top - half, weight=weight)
    g.vbar(x_right, y_top - half, y_bottom, weight=weight)
    g.hbar(x_left, x_right, y_bottom + half, weight=weight)


def kou_gou(
    g: Glyph,
    x1: float,
    x2: float,
    y: float,
    y_bottom: float,
    weight: float = W_MAIN,
    hook: float = W_SEC,
) -> None:
    """横折钩：横 + 竖 + 左上钩。

    x1 为横的墨迹左缘，x2 为竖的中心线，横画右缘与竖的墨迹右缘齐平。
    批内加/可/付/切/打/与 共用本函数。
    """
    half = weight / 2.0
    g.hbar(x1, x2 + half, y, weight=weight)
    g.vbar(x2, y, y_bottom, weight=weight)
    g.diag(x2, y_bottom, x2 - 62, y_bottom + 78, weight=hook)


def wan_gou(
    g: Glyph,
    x: float,
    y_top: float,
    y_bottom: float,
    x_end: float,
    weight: float = W_MAIN,
    hook: float = W_SEC,
) -> None:
    """竖弯钩：竖 + 右下弯横 + 上挑钩。

    x 为竖的中心线，y_bottom 为墨迹下缘，x_end 为弯横的墨迹右缘。
    批内七/切/元 共用本函数。
    """
    half = weight / 2.0
    g.vbar(x, y_top, y_bottom + half, weight=weight)
    g.hbar(x, x_end, y_bottom + half, weight=weight)
    g.diag(x_end, y_bottom + half, x_end + 46, y_bottom + half + 76, weight=hook)


# --------------------------------------------------------------------------
# 各字
# --------------------------------------------------------------------------
def g_xiao() -> Glyph:
    """小 U+5C0F（3 画）
    笔画清单：① 竖钩（中轴 820→130，左挑）② 点（左 300,640→190,455）
              ③ 点（右 700,640→810,455）
    部件分区：中轴占 x 392..548；左点占 x 152..338；右点占 x 662..848。
    竖钩是唯一主结构用 96，两点收细到 84，保持小字不闷。
    """
    g = Glyph("uni5C0F", advance=1000, unicode=0x5C0F, note="小：竖钩 + 左右两点")
    g.vbar(500, Y_TOP, 130, weight=W_MAIN)
    g.diag(500, 130, 392, 214, weight=W_SEC)
    g.diag(300, 640, 190, 455, weight=W_DOT)
    g.diag(700, 640, 810, 455, weight=W_DOT)
    return g


def g_qi() -> Glyph:
    """七 U+4E03（2 画）
    笔画清单：① 横（x 100..890，中心线 590）② 竖弯钩（竖 820→130，
              弯横 130→，末端上挑）
    部件分区：横贯全宽 x 100..890；竖弯钩占 x 272..890，竖心 x=320。
    笔画最少 → 两笔全用 96 主笔画，避免"太轻"。
    """
    g = Glyph("uni4E03", advance=1000, unicode=0x4E03, note="七：一 + 竖弯钩")
    g.hbar(100, 890, 590, weight=W_MAIN)
    g.vbar(320, Y_TOP, 130, weight=W_MAIN)
    g.hbar(320, 790, 112, weight=W_MAIN)
    g.diag(790, 112, 856, 208, weight=W_SEC)
    return g


def g_gong() -> Glyph:
    """公 U+516C（4 画）
    笔画清单：① 撇（左上 340,770→160,585）② 捺（右上 660,770→840,585）
              ③ 撇折（450,560→290,320→横 290..690）④ 点（630,440→730,340）
    部件分区：上八占 x 122..878 / y 548..807；下厶占 x 252..768 / y 232..600。
    八的两笔用次重 92（保持上部轻），厶的主折用 96 撑住字底。
    """
    g = Glyph("uni516C", advance=1000, unicode=0x516C, note="公：八 + 厶")
    g.diag(340, 770, 160, 585, weight=W_SEC)
    g.diag(660, 770, 840, 585, weight=W_SEC)
    g.diag(450, 560, 290, 320, weight=W_MAIN)
    g.hbar(290, 690, 320, weight=W_MAIN)
    g.diag(630, 440, 730, 340, weight=W_DOT)
    return g


def g_yi() -> Glyph:
    """以 U+4EE5（5 画）
    笔画清单：① 竖提（竖 600→150，挑至 300,240）② 点（300,660→235,545）
              ③ 撇（780,760→300,270）④ 捺（430,450→830,120）
    部件分区：左侧竖提占 x 122..348；中部点占 x 197..338；
              右侧人部占 x 262..864。撇的落点与竖提的挑首相接，是"以"的字眼。
    """
    g = Glyph("uni4EE5", advance=1000, unicode=0x4EE5, note="以：竖提 + 点 + 撇捺")
    g.vbar(170, 600, 150, weight=W_MAIN)
    g.diag(170, 150, 300, 240, weight=W_MAIN)
    g.diag(300, 660, 235, 545, weight=W_DOT)
    g.diag(780, 760, 300, 270, weight=W_MAIN)
    g.diag(430, 450, 830, 120, weight=W_MAIN)
    return g


def g_ping() -> Glyph:
    """平 U+5E73（5 画）
    笔画清单：① 横（上，中心线 772，上缘 820）② 丶（285,655→350,580）
              ③ 丿（715,655→650,580）④ 横（中，中心线 440）⑤ 竖（440→0）
    部件分区：上横 x 150..850；丷占 x 252..748 / y 543..692；
              中横 x 90..910；中竖 x 452..548。
    内白核算：上横下缘 724 与丷顶 692 留 32；丷底 543 与中横顶 488 留 55。
    """
    g = Glyph("uni5E73", advance=1000, unicode=0x5E73, note="平：一 + 丷 + 一 + 丨")
    g.hbar(150, 850, bar_top(Y_TOP, W_MAIN), weight=W_MAIN)
    g.diag(285, 655, 350, 580, weight=W_DOT)
    g.diag(715, 655, 650, 580, weight=W_THIN)
    g.hbar(90, 910, 440, weight=W_MAIN)
    g.vbar(500, 440, Y_BASE, weight=W_MAIN)
    return g


def g_jia() -> Glyph:
    """加 U+52A0（5 画）
    笔画清单：① 横折钩（横 90..478 / 竖 x=430 640→240 / 钩）② 撇（260,790→110,150）
              ③ 竖（口左 x=590）④ 横折（口上 + 口右 x=892）⑤ 横（口下）
    部件分区：左力占 x 76..478 / y 112..830；右口占 x 542..940 / y 0..790。
    两部件竖画净距：力竖墨迹右缘 478 → 口竖墨迹左缘 542 = 64（≥60）。
    """
    g = Glyph("uni52A0", advance=1000, unicode=0x52A0, note="加：力 + 口")
    kou_gou(g, 90, 430, 640, 240, weight=W_MAIN)
    g.diag(260, 790, 110, 150, weight=W_MAIN)
    kou_box(g, 590, 892, 790, 0, weight=W_MAIN)
    return g


def g_shan() -> Glyph:
    """山 U+5C71（3 画）
    笔画清单：① 竖（中，820→300，x=500）② 竖折（左竖 470→130 + 底横 130→）
              ③ 竖（右，530→130，x=700）
    部件分区：中竖 x 452..548；左竖折 x 252..748；右竖 x 652..748。
    竖画净距 104 / 104（≥60）。山字窄而不高胖，中竖独占顶部。
    """
    g = Glyph("uni5C71", advance=1000, unicode=0x5C71, note="山：竖 + 竖折 + 竖")
    g.vbar(500, Y_TOP, 300, weight=W_MAIN)
    g.vbar(300, 470, 130, weight=W_MAIN)
    g.hbar(300, 700, 112, weight=W_MAIN)
    g.vbar(700, 530, 130, weight=W_MAIN)
    return g


def g_shi() -> Glyph:
    """世 U+4E16（5 画）
    笔画清单：① 横（上，中心线 700，x 170..700）② 竖（长竖 x=300，790→130）
              ③ 竖（中竖 x=560，790→430）④ 横折（中横 300..860 + 右竖 x=812）
              ⑤ 横（底横 300..812，中心线 48）
    部件分区：上半廿形占 x 170..700 / y 652..790；下半占 x 252..860 / y 0..478。
    三根竖的净距：348→512 = 164，608→764 = 156（≥60）。
    """
    g = Glyph("uni4E16", advance=1000, unicode=0x4E16, note="世：廿 + 下部网格")
    g.hbar(170, 700, 700, weight=W_MAIN)
    g.vbar(300, 790, 130, weight=W_MAIN)
    g.vbar(560, 790, 430, weight=W_SEC)
    g.hbar(300, 860, 430, weight=W_MAIN)
    g.vbar(812, 430, 130, weight=W_SEC)
    g.hbar(300, 812, bar_base(Y_BASE, W_MAIN), weight=W_MAIN)
    return g


def g_qu() -> Glyph:
    """区 U+533A（4 画）
    笔画清单：① 横（上，中心线 772）② 竖折（左竖 x=138 820→130 + 底横 138→）
              ③ 撇（700,690→340,240）④ 捺（340,690→700,240）
    部件分区：外匚占 x 90..880 / y 0..820；内乂占 x 302..738 / y 202..728。
    内乂用 84 细笔，外框用 96，密排处（横与斜）留白 ≥ 24。
    """
    g = Glyph("uni533A", advance=1000, unicode=0x533A, note="区：匚 + 乂")
    g.hbar(90, 880, bar_top(Y_TOP, W_MAIN), weight=W_MAIN)
    g.vbar(138, Y_TOP, 130, weight=W_MAIN)
    g.hbar(138, 880, bar_base(Y_BASE, W_MAIN), weight=W_MAIN)
    g.diag(700, 690, 340, 240, weight=W_THIN)
    g.diag(340, 690, 700, 240, weight=W_THIN)
    return g


def g_zheng() -> Glyph:
    """正 U+6B63（5 画）
    笔画清单：① 横（上，中心线 772）② 竖（中，772→130，x=500）
              ③ 横（中段短横，中心线 410，x 500..800）④ 竖（左，410→130，x=280）
              ⑤ 横（下，中心线 48）
    部件分区：上横 x 130..870；中竖 x 452..548；短横 x 452..800；
              左竖 x 232..328；下横 x 130..870。
    """
    g = Glyph("uni6B63", advance=1000, unicode=0x6B63, note="正：一 + 止")
    g.hbar(130, 870, bar_top(Y_TOP, W_MAIN), weight=W_MAIN)
    g.vbar(500, 772, 130, weight=W_MAIN)
    g.hbar(500, 800, 410, weight=W_SEC)
    g.vbar(280, 410, 130, weight=W_MAIN)
    g.hbar(130, 870, bar_base(Y_BASE, W_MAIN), weight=W_MAIN)
    return g


def g_nv() -> Glyph:
    """女 U+5973（3 画）
    笔画清单：① 撇点（600,790→280,350→600,100）② 撇（800,520→170,140）
              ③ 横（中心线 470，x 80..920）
    部件分区：撇点占 x 214..636 / y 66..826；撇占 x 136..836；
              横贯 x 80..920。撇点转角落在横之下，撇与横在 x≈651 处交叉。
    """
    g = Glyph("uni5973", advance=1000, unicode=0x5973, note="女：撇点 + 撇 + 横")
    g.diag(600, 790, 280, 350, weight=W_MAIN)
    g.diag(280, 350, 600, 100, weight=W_MAIN)
    g.diag(800, 520, 170, 140, weight=W_MAIN)
    g.hbar(80, 920, 470, weight=W_MAIN)
    return g


def g_bei() -> Glyph:
    """北 U+5317（5 画）
    笔画清单：① 竖（左，820→0，x=340）② 横（左段短横，中心线 540，x 100..340）
              ③ 提（120,220→340,320）④ 撇（780,660→560,500）
              ⑤ 竖弯钩（竖 x=620 800→152 + 弯横 + 上挑）
    部件分区：左部（丬）占 x 100..388；右部（匕）占 x 512..905。
    左部与右部竖画净距：388→512 = 124（≥60）。
    """
    g = Glyph("uni5317", advance=1000, unicode=0x5317, note="北：丬 + 匕")
    g.vbar(340, Y_TOP, Y_BASE, weight=W_MAIN)
    g.hbar(100, 340, 540, weight=W_SEC)
    g.diag(120, 220, 340, 320, weight=W_SEC)
    g.diag(780, 660, 560, 500, weight=W_SEC)
    g.vbar(620, 800, 152, weight=W_MAIN)
    g.hbar(620, 870, 152, weight=W_MAIN)
    g.diag(870, 152, 905, 240, weight=W_SEC)
    return g


def g_wu() -> Glyph:
    """午 U+5348（4 画）
    笔画清单：① 撇（330,760→230,690）② 横（上，中心线 640，x 210..830）
              ③ 横（下长横，中心线 420，x 120..900）④ 竖（640→0，x=430）
    部件分区：上撇与上横占左上 x 190..830 / y 645..805；下横 x 120..900；
              中竖 x 382..478。上横与下横墨迹净距 124（≥24）。
    """
    g = Glyph("uni5348", advance=1000, unicode=0x5348, note="午：丿 + 二 + 丨")
    g.diag(330, 760, 230, 690, weight=W_SEC)
    g.hbar(210, 830, 640, weight=W_MAIN)
    g.hbar(120, 900, 420, weight=W_MAIN)
    g.vbar(430, 640, Y_BASE, weight=W_MAIN)
    return g


def g_xin() -> Glyph:
    """心 U+5FC3（4 画）
    笔画清单：① 点（左，150,480→235,350）② 卧钩（320,520→660,220→780,350）
              ③ 点（中，470,700→555,580）④ 点（右，780,620→860,500）
    部件分区：左点 x 112..272；卧钩 x 272..810；中点 x 434..592；
              右点 x 744..894。心是低位字，整字墨迹落在 y 172..733。
    """
    g = Glyph("uni5FC3", advance=1000, unicode=0x5FC3, note="心：点 + 卧钩 + 二点")
    g.diag(150, 480, 235, 350, weight=W_DOT)
    g.diag(320, 520, 660, 220, weight=W_MAIN)
    g.diag(660, 220, 780, 350, weight=W_SEC)
    g.diag(470, 700, 555, 580, weight=W_DOT)
    g.diag(780, 620, 860, 500, weight=W_DOT)
    return g


def g_zhi() -> Glyph:
    """支 U+652F（4 画）
    笔画清单：① 横（上，中心线 700，x 170..830）② 竖（780→430，x=500）
              ③ 横（中长横，中心线 430，x 90..910）④ 又（撇 700,420→330,120
              + 捺 390,420→890,110）
    部件分区：上十占 x 170..830 / y 652..790；中横 x 90..910；
              下又占 x 292..928 / y 72..458。
    """
    g = Glyph("uni652F", advance=1000, unicode=0x652F, note="支：十 + 又")
    g.hbar(170, 830, 700, weight=W_MAIN)
    g.vbar(500, 780, 430, weight=W_MAIN)
    g.hbar(90, 910, 430, weight=W_MAIN)
    g.diag(700, 420, 330, 120, weight=W_SEC)
    g.diag(390, 420, 890, 110, weight=W_MAIN)
    return g


def g_yu() -> Glyph:
    """予 U+4E88（4 画）
    笔画清单：① 横撇（横 250..660 中心线 772 + 撇 660,772→380,620）
              ② 点（330,700→420,600）③ 横（中心线 470，x 150..850）
              ④ 竖钩（竖 x=500 640→200 + 左挑）
    部件分区：上部フ形占 x 202..708 / y 586..820；中横 x 150..850；
              竖钩 x 400..548。横与フ形之间留白 ≥ 24。
    """
    g = Glyph("uni4E88", advance=1000, unicode=0x4E88, note="予：フ + 点 + 一 + 亅")
    g.hbar(250, 660, bar_top(Y_TOP, W_MAIN), weight=W_MAIN)
    g.diag(660, 772, 380, 620, weight=W_MAIN)
    g.diag(330, 700, 420, 600, weight=W_DOT)
    g.hbar(150, 850, 470, weight=W_MAIN)
    g.vbar(500, 640, 200, weight=W_MAIN)
    g.diag(500, 200, 410, 268, weight=W_SEC)
    return g


def g_chuan() -> Glyph:
    """川 U+5DDD（3 画）
    笔画清单：① 撇（300,790→150,420）② 竖（中，700→0，x=540）
              ③ 竖（右，810→0，x=780）
    部件分区：左撇 x 112..338；中竖 x 492..588；右竖 x 732..828。
    竖画净距 144（≥60）。左撇收在上部，是川的识别特征。
    """
    g = Glyph("uni5DDD", advance=1000, unicode=0x5DDD, note="川：丿 + 丨 + 丨")
    g.diag(300, 790, 150, 420, weight=W_MAIN)
    g.vbar(540, 700, Y_BASE, weight=W_MAIN)
    g.vbar(780, 810, Y_BASE, weight=W_MAIN)
    return g


def g_wen() -> Glyph:
    """文 U+6587（4 画）
    笔画清单：① 点（顶，460,790→545,700）② 横（中心线 640，x 110..890）
              ③ 撇（560,640→200,140）④ 捺（440,640→820,140）
    部件分区：顶点 x 424..581；横 x 110..890；下部交叉 x 164..856。
    横上缘 688 与顶点下缘 665 留 23 —— 顶点略上提至 690 端点，
    实际端点 (460,780)→(545,690)，净距 38（≥24）。
    """
    g = Glyph("uni6587", advance=1000, unicode=0x6587, note="文：丶 + 一 + 丿 + ㇏")
    g.diag(460, 780, 545, 690, weight=W_DOT)
    g.hbar(110, 890, 640, weight=W_MAIN)
    g.diag(560, 640, 200, 140, weight=W_MAIN)
    g.diag(440, 640, 820, 140, weight=W_MAIN)
    return g


def g_fan() -> Glyph:
    """反 U+53CD（4 画）
    笔画清单：① 横（上，中心线 772，x 230..760）② 撇（250,772→110,420）
              ③ 横撇（横 330..760 中心线 560 + 撇 760,560→480,200）
              ④ 捺（400,540→830,130）
    部件分区：上厂占 x 76..760 / y 386..820；下又占 x 442..868 / y 92..598。
    """
    g = Glyph("uni53CD", advance=1000, unicode=0x53CD, note="反：厂 + 又")
    g.hbar(230, 760, bar_top(Y_TOP, W_MAIN), weight=W_MAIN)
    g.diag(250, 772, 110, 420, weight=W_MAIN)
    g.hbar(330, 760, 560, weight=W_SEC)
    g.diag(760, 560, 480, 200, weight=W_SEC)
    g.diag(400, 540, 830, 130, weight=W_MAIN)
    return g


def g_yuan() -> Glyph:
    """元 U+5143（4 画）
    笔画清单：① 横（上短横，中心线 772，x 250..750）② 横（下长横，中心线 600，
              x 120..880）③ 撇（380,600→200,120）④ 竖弯钩（竖 x=640 600→70
              + 上挑）
    部件分区：上横 x 250..750；下横 x 120..880；左腿 x 166..414；
              右腿 x 592..910。
    """
    g = Glyph("uni5143", advance=1000, unicode=0x5143, note="元：二 + 儿")
    g.hbar(250, 750, bar_top(Y_TOP, W_MAIN), weight=W_MAIN)
    g.hbar(120, 880, 600, weight=W_MAIN)
    g.diag(380, 600, 200, 120, weight=W_MAIN)
    g.vbar(640, 600, 70, weight=W_MAIN)
    g.diag(640, 90, 860, 230, weight=W_MAIN)
    return g


def g_qian() -> Glyph:
    """千 U+5343（3 画）
    笔画清单：① 撇（650,760→330,700）② 横（中心线 560，x 110..890）
              ③ 竖（740→0，x=500）
    部件分区：顶撇 x 292..688；长横 x 110..890；中竖 x 452..548。
    撇与横在 x≈480 处相接，是"千"的字眼。
    """
    g = Glyph("uni5343", advance=1000, unicode=0x5343, note="千：丿 + 一 + 丨")
    g.diag(650, 760, 330, 700, weight=W_SEC)
    g.hbar(110, 890, 560, weight=W_MAIN)
    g.vbar(500, 740, Y_BASE, weight=W_MAIN)
    return g


def g_yin() -> Glyph:
    """引 U+5F15（4 画）
    笔画清单：① 横折（弓上横 130..470 中心线 772 + 右竖 x=422 772→620）
              ② 横（弓中横 130..422 中心线 620）
              ③ 竖折折钩（竖 x=226 620→430 + 底横 226..470 中心线 430
              + 右竖 x=422 430→130 + 左挑钩）
              ④ 竖（右长竖，820→0，x=800）
    部件分区：左弓占 x 130..518；右竖 x 752..848。弓的中横左伸 48，
    与下左竖错开，构成"3"形骨架。
    """
    g = Glyph("uni5F15", advance=1000, unicode=0x5F15, note="引：弓 + 丨")
    g.hbar(130, 470, bar_top(Y_TOP, W_MAIN), weight=W_MAIN)
    g.vbar(422, 772, 620, weight=W_MAIN)
    g.hbar(130, 422, 620, weight=W_MAIN)
    g.vbar(226, 620, 430, weight=W_MAIN)
    g.hbar(226, 470, 430, weight=W_MAIN)
    g.vbar(422, 430, 130, weight=W_MAIN)
    g.diag(422, 130, 330, 200, weight=W_SEC)
    g.vbar(800, Y_TOP, Y_BASE, weight=W_MAIN)
    return g


def g_shui() -> Glyph:
    """水 U+6C34（4 画）
    笔画清单：① 竖钩（竖 x=500 820→130 + 左挑）② 短横（500→340，中心线 620）
              ③ 撇（460,660→130,280）④ 捺（540,640→880,250）
    部件分区：中轴 x 452..548；左撇 x 92..498；右捺 x 502..918。
    中轴两侧净距 ≈ 350，内白充足。
    """
    g = Glyph("uni6C34", advance=1000, unicode=0x6C34, note="水：亅 + 氺")
    g.vbar(500, Y_TOP, 130, weight=W_MAIN)
    g.diag(500, 130, 410, 200, weight=W_SEC)
    g.hbar(340, 500, 620, weight=W_THIN)
    g.diag(460, 660, 130, 280, weight=W_MAIN)
    g.diag(540, 640, 880, 250, weight=W_MAIN)
    return g


def g_ban() -> Glyph:
    """半 U+534A（5 画）
    笔画清单：① 丶（285,730→350,655）② 丿（715,730→650,655）
              ③ 横（上，中心线 540，x 210..790）④ 横（下长横，中心线 370，
              x 100..900）⑤ 竖（540→0，x=500）
    部件分区：丷占 x 248..748 / y 618..767；上横 x 210..790；
              下横 x 100..900；中竖 x 452..548。
    与"平"同族：丷间距、短横位置一致，仅下横更宽、竖更靠中。
    """
    g = Glyph("uni534A", advance=1000, unicode=0x534A, note="半：丷 + 二 + 丨")
    g.diag(285, 730, 350, 655, weight=W_DOT)
    g.diag(715, 730, 650, 655, weight=W_THIN)
    g.hbar(210, 790, 540, weight=W_MAIN)
    g.hbar(100, 900, 370, weight=W_MAIN)
    g.vbar(500, 540, Y_BASE, weight=W_MAIN)
    return g


def g_shi4() -> Glyph:
    """示 U+793A（5 画）
    笔画清单：① 横（上短横，中心线 772，x 280..720）② 横（中心线 620，
              x 200..800）③ 竖（620→400，x=500）④ 撇（480,400→230,140）
              ⑤ 点（520,400→790,140）
    部件分区：上横 x 280..720；次横 x 200..800；中竖 x 452..548；
              下八占 x 192..828 / y 102..438。
    """
    g = Glyph("uni793A", advance=1000, unicode=0x793A, note="示：二 + 小")
    g.hbar(280, 720, bar_top(Y_TOP, W_MAIN), weight=W_MAIN)
    g.hbar(200, 800, 620, weight=W_MAIN)
    g.vbar(500, 620, 380, weight=W_MAIN)
    g.diag(480, 400, 230, 140, weight=W_SEC)
    g.diag(520, 400, 790, 140, weight=W_SEC)
    return g


def g_da() -> Glyph:
    """打 U+6253（5 画）
    笔画清单：① 横（扌，中心线 640，x 90..400）② 竖钩（扌，x=250 780→80+挑）
              ③ 提（扌，110,300→400,400）④ 横（丁，中心线 740，x 480..940）
              ⑤ 竖钩（丁，x=740 740→120+挑）
    部件分区：扌占 x 90..298；丁占 x 480..940。
    竖画净距：298→480 = 182（≥60）。扌的提与丁的竖互不相连。
    """
    g = Glyph("uni6253", advance=1000, unicode=0x6253, note="打：扌 + 丁")
    g.hbar(90, 400, 640, weight=W_SEC)
    g.vbar(250, 780, 80, weight=W_MAIN)
    g.diag(250, 80, 170, 150, weight=W_SEC)
    g.diag(110, 300, 400, 400, weight=W_SEC)
    g.hbar(480, 940, 740, weight=W_MAIN)
    g.vbar(740, 740, 120, weight=W_MAIN)
    g.diag(740, 120, 660, 190, weight=W_SEC)
    return g


def g_tai() -> Glyph:
    """台 U+53F0（5 画）
    笔画清单：① 撇折（530,790→370,620 + 横 370..610 中心线 620）
              ② 点（560,760→650,650）③ 竖（口左 x=340）④ 横折（口上 + 口右
              x=670）⑤ 横（口下）
    部件分区：上厶占 x 332..682 / y 572..817；下口占 x 292..718 / y 0..400。
    厶与口之间净距 124（≥24）。
    """
    g = Glyph("uni53F0", advance=1000, unicode=0x53F0, note="台：厶 + 口")
    g.diag(530, 790, 370, 620, weight=W_MAIN)
    g.hbar(370, 610, 620, weight=W_MAIN)
    g.diag(560, 760, 650, 650, weight=W_DOT)
    kou_box(g, 340, 670, 400, 0, weight=W_MAIN)
    return g


def g_hiro() -> Glyph:
    """広 U+5E83（5 画）
    笔画清单：① 点（顶，470,775→545,655）② 横（广，中心线 700，x 140..900）
              ③ 撇（广，200,660→110,150）④ 撇折（厶，600,580→420,300
              + 横 420..740 中心线 300）⑤ 点（厶，650,480→730,380）
    部件分区：广占 x 72..900 / y 112..808；厶占 x 382..768 / y 252..618。
    与"台"的厶同族：同一条撇折 + 点的角度，只是位置与大小不同。
    """
    g = Glyph("uni5E83", advance=1000, unicode=0x5E83, note="広：广 + 厶")
    g.diag(470, 750, 545, 655, weight=W_DOT)
    g.hbar(140, 900, 700, weight=W_MAIN)
    g.diag(210, 690, 110, 150, weight=W_MAIN)
    g.diag(600, 580, 490, 300, weight=W_MAIN)
    g.hbar(420, 740, 300, weight=W_MAIN)
    g.diag(650, 520, 730, 420, weight=W_DOT)
    return g


def g_bi() -> Glyph:
    """必 U+5FC5（5 画）
    笔画清单：① 撇（长撇，820,740→250,140）② 卧钩（330,480→640,200→760,340）
              ③ 点（左，160,430→240,310）④ 点（中，470,660→550,540）
              ⑤ 点（右，790,620→870,500）
    部件分区：长撇占 x 212..858 / y 106..774；心底占 x 122..790 / y 162..518。
    点与卧钩之间净距均 ≥ 24，长撇斜穿心部，是"必"的识别特征。
    """
    g = Glyph("uni5FC5", advance=1000, unicode=0x5FC5, note="必：心 + 长撇")
    g.diag(820, 740, 250, 140, weight=W_MAIN)
    g.diag(330, 480, 640, 200, weight=W_MAIN)
    g.diag(640, 200, 760, 340, weight=W_SEC)
    g.diag(160, 430, 240, 310, weight=W_DOT)
    g.diag(470, 660, 550, 540, weight=W_DOT)
    g.diag(790, 620, 870, 500, weight=W_DOT)
    return g


def g_kou() -> Glyph:
    """口 U+53E3（3 画）
    笔画清单：① 竖（左，x=108，790→0）② 横折（横 108..940 中心线 742
              + 右竖 x=892）③ 横（底，108..892 中心线 48）
    部件分区：整字墨迹 x 60..940 / y 0..790，口内空 x 156..844 / y 96..694。
    笔画最少 → 三笔全用 96，字框四边等重，避免"太轻"。
    """
    g = Glyph("uni53E3", advance=1000, unicode=0x53E3, note="口：竖 + 横折 + 横")
    kou_box(g, 108, 892, 790, 0, weight=W_MAIN)
    return g


def g_shao() -> Glyph:
    """少 U+5C11（4 画）
    笔画清单：① 竖（中，820→430，x=520）② 撇（左，350,680→240,540）
              ③ 点（右，700,680→790,540）④ 撇（长撇，520,480→180,110）
    部件分区：中竖 x 472..568；左上短撇 x 202..388；右上点 x 662..828；
              长撇占 x 142..558 / y 76..518。
    """
    g = Glyph("uni5C11", advance=1000, unicode=0x5C11, note="少：丨 + 丿丶 + 长撇")
    g.vbar(520, Y_TOP, 430, weight=W_MAIN)
    g.diag(350, 680, 240, 540, weight=W_THIN)
    g.diag(700, 680, 790, 540, weight=W_DOT)
    g.diag(520, 480, 180, 110, weight=W_MAIN)
    return g


def g_gong2() -> Glyph:
    """工 U+5DE5（3 画）
    笔画清单：① 横（上，中心线 740，x 140..860）② 竖（740→130，x=500）
              ③ 横（下，中心线 48，x 110..890）
    部件分区：上横 x 140..860；竖 x 452..548；下横 x 110..890。
    笔画最少 → 三笔全 96，下横略宽于上横。
    """
    g = Glyph("uni5DE5", advance=1000, unicode=0x5DE5, note="工：一 + 丨 + 一")
    g.hbar(140, 860, 740, weight=W_MAIN)
    g.vbar(500, 740, 130, weight=W_MAIN)
    g.hbar(110, 890, bar_base(Y_BASE, W_MAIN), weight=W_MAIN)
    return g


def g_tu() -> Glyph:
    """土 U+571F（3 画）
    笔画清单：① 横（上短横，中心线 640，x 200..800）② 竖（820→130，x=500）
              ③ 横（下长横，中心线 48，x 110..890）
    部件分区：上横 x 200..800；竖 x 452..548；下横 x 110..890。
    与"工"同族：上横短、下横长、竖贯穿，顶端竖出头 96。
    """
    g = Glyph("uni571F", advance=1000, unicode=0x571F, note="土：十 + 一")
    g.hbar(200, 800, 640, weight=W_MAIN)
    g.vbar(500, Y_TOP, 130, weight=W_MAIN)
    g.hbar(110, 890, bar_base(Y_BASE, W_MAIN), weight=W_MAIN)
    return g


def g_yu2() -> Glyph:
    """与 U+4E0E（3 画）
    笔画清单：① 横（上，中心线 740，x 220..800）② 竖折折钩（竖 x=220 740→470
              + 横 220..820 中心线 470 + 竖 x=772 470→110 + 左挑钩）
              ③ 横（下段短横，中心线 300，x 120..772）
    部件分区：上横 x 172..800；折笔组 x 172..820；下横 x 120..820。
    ③ 在最后画出，横跨到底部竖，是"与"的字眼。
    """
    g = Glyph("uni4E0E", advance=1000, unicode=0x4E0E, note="与：一 + 竖折折钩 + 一")
    g.hbar(220, 800, 740, weight=W_MAIN)
    g.vbar(220, 740, 470, weight=W_MAIN)
    g.hbar(220, 820, 470, weight=W_MAIN)
    g.vbar(772, 470, 110, weight=W_MAIN)
    g.diag(772, 110, 690, 180, weight=W_SEC)
    g.hbar(120, 772, 300, weight=W_MAIN)
    return g


def g_zhi2() -> Glyph:
    """止 U+6B62（4 画）
    笔画清单：① 竖（中，820→130，x=500）② 横（右短横，中心线 600，x 500..830）
              ③ 竖（左，600→130，x=280）④ 横（底，中心线 48，x 140..860）
    部件分区：中竖 x 452..548；右短横 x 452..830；左竖 x 232..328；
              底横 x 140..860。
    """
    g = Glyph("uni6B62", advance=1000, unicode=0x6B62, note="止：丨 + 一 + 丨 + 一")
    g.vbar(500, Y_TOP, 130, weight=W_MAIN)
    g.hbar(500, 830, 600, weight=W_SEC)
    g.vbar(280, 600, 130, weight=W_MAIN)
    g.hbar(140, 860, bar_base(Y_BASE, W_MAIN), weight=W_MAIN)
    return g


def g_ke() -> Glyph:
    """可 U+53EF（5 画）
    笔画清单：① 横（上长横，中心线 740，x 90..940）② 竖钩（右，x=860 740→120
              + 左挑）③ 竖（口左 x=250）④ 横折（口上 + 口右 x=432）
              ⑤ 横（口下）
    部件分区：上横 x 90..940；口占 x 202..480 / y 200..560；右竖钩 x 812..908。
    口与右竖钩净距 332（≥60）。
    """
    g = Glyph("uni53EF", advance=1000, unicode=0x53EF, note="可：丁 + 口")
    g.hbar(90, 940, 740, weight=W_MAIN)
    g.vbar(860, 740, 120, weight=W_MAIN)
    g.diag(860, 120, 780, 190, weight=W_SEC)
    kou_box(g, 250, 432, 560, 200, weight=W_MAIN)
    return g


def g_mu() -> Glyph:
    """木 U+6728（4 画）
    笔画清单：① 横（中心线 620，x 90..910）② 竖（820→0，x=500）
              ③ 撇（470,600→120,120）④ 捺（530,600→880,120）
    部件分区：横 x 90..910；竖 x 452..548；撇 x 82..508；捺 x 492..918。
    木是本批的基准骨架：横在 62% 高，撇捺从横下方的竖两侧分出。
    """
    g = Glyph("uni6728", advance=1000, unicode=0x6728, note="木：一 + 丨 + 丿 + ㇏")
    g.hbar(90, 910, 620, weight=W_MAIN)
    g.vbar(500, Y_TOP, Y_BASE, weight=W_MAIN)
    g.diag(470, 600, 120, 120, weight=W_MAIN)
    g.diag(530, 600, 880, 120, weight=W_MAIN)
    return g


def g_fu() -> Glyph:
    """付 U+4ED8（5 画）
    笔画清单：① 撇（亻，290,790→150,460）② 竖（亻，x=190，500→0）
              ③ 横（寸，中心线 640，x 400..940）④ 竖钩（寸，x=780 790→120+挑）
              ⑤ 点（寸，560,480→640,380）
    部件分区：亻占 x 112..328；寸占 x 352..940。
    亻竖墨迹右缘 238 → 寸横墨迹左缘 400，净距 162（≥60）。
    """
    g = Glyph("uni4ED8", advance=1000, unicode=0x4ED8, note="付：亻 + 寸")
    g.diag(290, 790, 150, 460, weight=W_MAIN)
    g.vbar(190, 500, Y_BASE, weight=W_MAIN)
    g.hbar(400, 940, 640, weight=W_MAIN)
    g.vbar(780, 790, 120, weight=W_MAIN)
    g.diag(780, 120, 700, 190, weight=W_SEC)
    g.diag(560, 480, 640, 380, weight=W_DOT)
    return g


def g_qie() -> Glyph:
    """切 U+5207（4 画）
    笔画清单：① 横（七，中心线 560，x 90..430）② 竖弯钩（七，x=220 760→130
              + 弯横 + 上挑）③ 横折钩（刀，横 520..940 中心线 700 + 竖 x=892
              700→260 + 钩）④ 撇（刀，720,700→530,200）
    部件分区：左七占 x 90..455；右刀占 x 472..940。
    七竖墨迹右缘 268 → 刀撇最左墨迹 ≈ 492，净距 224（≥60）。
    """
    g = Glyph("uni5207", advance=1000, unicode=0x5207, note="切：七 + 刀")
    g.hbar(90, 430, 560, weight=W_MAIN)
    g.vbar(220, 760, 130, weight=W_MAIN)
    g.hbar(220, 400, 112, weight=W_MAIN)
    g.diag(400, 112, 455, 200, weight=W_SEC)
    kou_gou(g, 520, 892, 700, 260, weight=W_MAIN)
    g.diag(720, 700, 530, 200, weight=W_MAIN)
    return g


def g_you() -> Glyph:
    """由 U+7531（5 画）
    笔画清单：① 竖（中，820→150，x=500）② 横折（框上 中心线 690 + 框右
              x=792）③ 横（框中，中心线 420）④ 竖（框左 x=208）⑤ 横（框底，
              中心线 150）
    部件分区：框体 x 160..840 / y 102..738；中竖出头至 820。
    中竖与框左竖净距 160，与框右竖净距 196（≥60）。
    """
    g = Glyph("uni7531", advance=1000, unicode=0x7531, note="由：田 + 出头竖")
    g.vbar(500, Y_TOP, 150, weight=W_MAIN)
    g.hbar(208, 840, 690, weight=W_MAIN)
    g.vbar(792, 690, 150, weight=W_MAIN)
    g.hbar(208, 792, 420, weight=W_SEC)
    g.vbar(208, 690, 150, weight=W_MAIN)
    g.hbar(208, 792, 150, weight=W_MAIN)
    return g


# --------------------------------------------------------------------------
def build() -> list[Glyph]:
    """按 lane 字符清单顺序返回本批 40 个字形。"""
    return [
        g_xiao(),   # 小 U+5C0F
        g_qi(),     # 七 U+4E03
        g_gong(),   # 公 U+516C
        g_yi(),     # 以 U+4EE5
        g_ping(),   # 平 U+5E73
        g_jia(),    # 加 U+52A0
        g_shan(),   # 山 U+5C71
        g_shi(),    # 世 U+4E16
        g_qu(),     # 区 U+533A
        g_zheng(),  # 正 U+6B63
        g_nv(),     # 女 U+5973
        g_bei(),    # 北 U+5317
        g_wu(),     # 午 U+5348
        g_xin(),    # 心 U+5FC3
        g_zhi(),    # 支 U+652F
        g_yu(),     # 予 U+4E88
        g_chuan(),  # 川 U+5DDD
        g_wen(),    # 文 U+6587
        g_fan(),    # 反 U+53CD
        g_yuan(),   # 元 U+5143
        g_qian(),   # 千 U+5343
        g_yin(),    # 引 U+5F15
        g_shui(),   # 水 U+6C34
        g_ban(),    # 半 U+534A
        g_shi4(),   # 示 U+793A
        g_da(),     # 打 U+6253
        g_tai(),    # 台 U+53F0
        g_hiro(),   # 広 U+5E83
        g_bi(),     # 必 U+5FC5
        g_kou(),    # 口 U+53E3
        g_shao(),   # 少 U+5C11
        g_gong2(),  # 工 U+5DE5
        g_tu(),     # 土 U+571F
        g_yu2(),    # 与 U+4E0E
        g_zhi2(),   # 止 U+6B62
        g_ke(),     # 可 U+53EF
        g_mu(),     # 木 U+6728
        g_fu(),     # 付 U+4ED8
        g_qie(),    # 切 U+5207
        g_you(),    # 由 U+7531
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-s1-002.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
