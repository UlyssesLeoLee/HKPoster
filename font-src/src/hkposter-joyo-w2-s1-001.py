"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s1-001。

本批 40 字，笔画范围 2–5，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
1. 字面框与 zh-HK 繁体汉字完全一致：x 60..940、y 0..820，advance 1000。
   保证 zh-HK / ja / zh-CN 混排时基线与视觉大小一致（docs/04）。
2. 笔画权重沿用 CJK 档：主 96 / 次 92 / 细 84 / 点 84。
   本批全是 2–5 画的低密度字：主干一律 96（笔画少要加粗，否则同批内
   "有的太轻、有的太闷"，GLY-001）；只在叠横、竖间等密排处局部降到 92/84
   保内白。
3. 部件复用（GLY-004，docs/03）：同一部件在批内必须用同一套坐标与同一套
   笔画拆法，只做位置与大小的光学校正：
   · 亻（仏 / 仙 / 仁）共用 ren()，坐标与 Wave 1 批次（仕 / 他）完全一致；
   · 厶（払 / 仏）共用 mushi()，坐标完全一致；
   · 辶（巡）共用 Wave 1 批次的 shinnyou() 坐标（辺 / 込），跨批同族；
   · 口 / 日 统一走 kuchi_box()（左竖 + 顶横 + 右竖 + 底横 [+ 中横]），
     只改尺寸。
4. 对齐语义（与 hkposter-latin.py 同办法）：
   · 横画按"墨迹上缘 / 下缘"定位，中心线内缩半个笔画宽
     （bar_top / bar_base）；
   · 竖画端点即墨迹端点（vspan）；
   · 斜画用 diag_cap_base()，让墨迹下缘贴 0、上缘贴目标高度，
     避免斜画溢出版心或顶不到版心。
5. 内白下限（GLY-006）：叠横净空 ≥ 24，竖间净空 ≥ 60。每个字的 docstring
   里写明笔画清单与部件分区坐标，便于复核。
6. 禁止逐字机械挤压或倾斜（docs/02 偏差 D）：斜笔画只出现在汉字本身的
   撇捺结构上，不对整字做倾斜或横向压缩。
7. 钩（乚 / 𠃌 的收笔）一律"起笔落在前一笔的墨迹内部"，不让两笔在端点
   处形成对顶缺口——并集后会出现一个悬空的独立小块。
8. 字面留白：本批字形偏窄（亻旁、厶、幺等），右部件统一推到 x 420 以外，
   左部件不越过 x 82，保证版心不被吃满，也不留出大片空白。
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

TOP_Y = 820.0
BASE_Y = 0.0


# --------------------------------------------------------------------------
# 对齐辅助
# --------------------------------------------------------------------------
def bar_top(g: Glyph, x1: float, x2: float, w: float = W_MAIN) -> None:
    """横画：墨迹上缘贴版心顶 820。"""
    g.hbar(x1, x2, TOP_Y - w / 2.0, w)


def bar_at(g: Glyph, y: float, x1: float, x2: float, w: float = W_MAIN) -> None:
    """横画：中心线在 y。"""
    g.hbar(x1, x2, y, w)


def bar_base(g: Glyph, x1: float, x2: float, w: float = W_MAIN) -> None:
    """横画：墨迹下缘贴基线 0。"""
    g.hbar(x1, x2, BASE_Y + w / 2.0, w)


def vspan(g: Glyph, x: float, y_bot: float, y_top: float, w: float = W_MAIN) -> None:
    """竖画：端点即墨迹端点。"""
    g.vbar(x, y_bot, y_top, w)


def diag_cap_base(
    g: Glyph,
    x_bot: float,
    x_top: float,
    w: float = W_MAIN,
    y_bot: float = BASE_Y,
    y_top: float = TOP_Y,
) -> None:
    """斜画：墨迹下缘贴 y_bot、上缘贴 y_top（中心线两端自动内缩半笔宽）。"""
    dx = x_top - x_bot
    dy = y_top - y_bot
    k = 0.0
    yb = y_bot
    yt = y_top
    for _ in range(3):
        length = math.hypot(dx, dy)
        ux = dx / length
        k = w / 2.0 * abs(ux)
        yb = y_bot + k
        yt = y_top - k
        dy = yt - yb
    g.diag(x_bot, yb, x_top, yt, w)


def kuchi_box(
    g: Glyph,
    x1: float,
    x2: float,
    y_top: float,
    y_bot: float,
    y_mid: float | None = None,
    wv: float = W_SEC,
    wh: float = W_MAIN,
) -> None:
    """口 / 日 / 田：左竖 + 顶横 + 右竖 + 底横（+ 中横）。

    x1 / x2 为左右竖的中心线；y_top / y_bot / y_mid 为横画的中心线。
    """
    bar_at(g, y_top, x1, x2, wh)
    vspan(g, x1, y_top, y_bot, wv)
    vspan(g, x2, y_top, y_bot, wv)
    bar_at(g, y_bot, x1, x2, wh)
    if y_mid is not None:
        bar_at(g, y_mid, x1, x2, W_SEC)


# --------------------------------------------------------------------------
# 复用部件（批内同一套坐标，GLY-004）
# --------------------------------------------------------------------------
def ren(g: Glyph) -> None:
    """亻（人字旁）：撇 + 竖。仏 / 仙 / 仁 共用。

    坐标与 Wave 1 批次（仕 / 他）的 ren() 完全一致，跨批同族。
    撇从右上斜掠到左下，竖顶落在撇的中段上（y=664 处撇心线正好过 x=255），
    两者只在小面积相交，不会粘成一团。
    """
    g.diag(330, 780, 130, 470, W_MAIN)
    vspan(g, 255, 664, 0, W_MAIN)


def mushi(g: Glyph) -> None:
    """厶（撇折 + 点）：払 / 仏 共用同一坐标。

    撇折：(700,700)→(520,430) 后折向右；点落在折横右端上方，净距 36。
    """
    g.diag(700, 700, 520, 430, W_SEC)
    bar_at(g, 430, 520, 780, W_SEC)
    g.dot(800, 560, 84, 96)


def shinnyou(g: Glyph) -> None:
    """辶（しんにょう）：点 + 折 + 底扫。

    坐标与 Wave 1 批次（辺 / 込）的 shinnyou() 完全一致，跨批同族。
    """
    g.dot(160, 690, 110, 120)
    bar_at(g, 520, 110, 270, W_SEC)
    vspan(g, 190, 520, 220, W_SEC)
    g.diag(200, 220, 900, 100, W_MAIN)


# --------------------------------------------------------------------------
# 字形
# --------------------------------------------------------------------------
def g_seru() -> Glyph:
    """占（5画）：卜（竖 + 右横）+ 口。

    部件分区：卜 x 452..790、y 400..820；口 x 182..818、y 0..438。
    卜竖底端 400 落在口顶横墨迹带（342..438）内，两笔相连不断口。
    口内净空 96..342 = 246。
    """
    g = Glyph("uni5360", advance=1000, unicode=0x5360, note="占：卜 + 口")
    vspan(g, 500, 400, 820, W_MAIN)      # 卜的竖
    bar_at(g, 690, 540, 790, W_SEC)      # 卜的右横
    kuchi_box(g, 230, 770, 390, 48)      # 口
    return g


def g_attsu() -> Glyph:
    """圧（5画）：厂（一 + 丿）+ 土（一 + 丨 + 一）。

    部件分区：厂 x 47..890；土 x 300..900。
    厂丿墨迹顶 760 与厂横墨迹（724..820）相接；丿底端墨迹 x 47..143，
    土下横左端 300，净距 157。
    土：上横墨迹 384..476，下横墨迹 0..96，中竖 90..430。
    """
    g = Glyph("uni5727", advance=1000, unicode=0x5727, note="圧：厂 + 土")
    bar_top(g, 110, 890, W_MAIN)                                # 厂的一
    diag_cap_base(g, 95, 245, W_MAIN, y_bot=0, y_top=760)       # 厂的丿
    bar_at(g, 430, 340, 880, W_SEC)                             # 土的上横
    vspan(g, 610, 90, 430, W_MAIN)                              # 土的竖
    bar_base(g, 300, 900, W_MAIN)                               # 土的下横
    return g


def g_tamashii() -> Glyph:
    """玉（5画）：王（三横 + 丨）+ 点。

    三横墨迹：上 724..820、中 372..468、下 0..96；两处净空 256 / 276。
    点落在中横与下横之间（x 714..806、y 166..274）。
    """
    g = Glyph("uni7389", advance=1000, unicode=0x7389, note="玉：王 + 点")
    bar_top(g, 150, 850, W_MAIN)
    bar_at(g, 420, 130, 870, W_MAIN)
    bar_base(g, 110, 890, W_MAIN)
    vspan(g, 500, 90, 420, W_MAIN)
    g.dot(762, 215, 104, 120)
    return g


def g_tsukasa() -> Glyph:
    """司（5画）：𠃌（横折钩）+ 一 + 口。

    部件分区：外框 x 120..928；内一 x 180..700；内口 x 152..688。
    外框右竖墨迹 832..928，内口右竖墨迹 592..688，净距 144。
    内一墨迹 594..686 与口顶横墨迹 432..528 净空 66。
    """
    g = Glyph("uni53F8", advance=1000, unicode=0x53F8, note="司：横折钩 + 一 + 口")
    bar_top(g, 120, 880, W_MAIN)
    vspan(g, 880, 120, 820, W_MAIN)
    g.diag(855, 130, 790, 200, W_THIN)     # 钩
    bar_at(g, 640, 180, 700, W_SEC)         # 内一
    kuchi_box(g, 200, 640, 480, 120)        # 内口
    return g


def g_ryou() -> Glyph:
    """了（2画）：乛（横 + 撇）+ 亅（竖钩）。

    笔画：① 横 中心线 770，x 180..820 ② 撇 (820,770)→(280,450)
          ③ 竖 x=430，y 60..520 ④ 钩 (430,75)→(370,155)
    撇心线在 x=430 处过 y≈539（墨迹 498..580），竖顶 520 落在撇墨迹内，
    两笔相连；钩的起笔落在竖的墨迹内部。
    """
    g = Glyph("uni4E86", advance=1000, unicode=0x4E86, note="了：乛 + 亅")
    bar_at(g, 770, 180, 820, W_MAIN)
    g.diag(820, 770, 280, 450, W_MAIN)
    vspan(g, 430, 60, 520, W_MAIN)
    g.diag(430, 75, 370, 155, W_THIN)
    return g


def g_chou() -> Glyph:
    """庁（5画）：广（丶 + 一 + 丿）+ 丁（一 + 竖钩）。

    部件分区：广 x 42..928；丁 x 272..848。
    广的丶墨迹 720..820，广横墨迹 592..688，净空 32。
    广丿在 y=480 处心线 x≈202（墨迹 154..250），丁横左端 320，净距 70。
    """
    g = Glyph("uni5E81", advance=1000, unicode=0x5E81, note="庁：广 + 丁")
    g.dot(500, 770, 92, 100)                                # 广的点
    bar_at(g, 640, 160, 880, W_MAIN)                         # 广的一
    diag_cap_base(g, 90, 240, W_MAIN, y_bot=0, y_top=640)    # 广的丿
    bar_at(g, 480, 320, 800, W_MAIN)                         # 丁的一
    vspan(g, 560, 120, 480, W_MAIN)                          # 丁的竖
    g.diag(560, 135, 500, 205, W_THIN)                       # 丁的钩
    return g


def g_rei() -> Glyph:
    """令（5画）：人（撇 + 捺）+ 丶 + 乛（横 + 撇）+ 丶。

    部件分区：人 x 192..848；下部マ x 202..748。
    撇捺在 (520,790) 相交；点墨迹 452..548 与横墨迹 332..428 净空 24。
    """
    g = Glyph("uni4EE4", advance=1000, unicode=0x4EE4, note="令：人 + マ")
    g.diag(520, 790, 240, 560, W_MAIN)      # 撇
    g.diag(520, 790, 800, 560, W_MAIN)      # 捺
    g.dot(500, 500, 88, 96)                 # 点
    bar_at(g, 380, 250, 700, W_MAIN)        # 乛的横
    g.diag(700, 380, 450, 150, W_MAIN)      # 乛的撇
    g.dot(690, 210, 84, 96)                 # 末点
    return g


def g_harai() -> Glyph:
    """払（5画）：扌（一 + 竖钩 + 提）+ 厶（撇折 + 点）。

    部件分区：扌 x 52..378；厶 x 472..842。
    扌的竖墨迹 192..288，厶左端 472，净距 184。
    提自 (120,330) 上挑至 (320,400)，末端压进竖的墨迹。
    """
    g = Glyph("uni6255", advance=1000, unicode=0x6255, note="払：扌 + 厶")
    bar_at(g, 640, 100, 330, W_SEC)          # 扌的一
    vspan(g, 240, 120, 820, W_MAIN)          # 扌的竖
    g.diag(120, 330, 320, 400, W_SEC)        # 扌的提
    mushi(g)                                 # 厶
    return g


def g_butsu() -> Glyph:
    """仏（4画）：亻（撇 + 竖）+ 厶（撇折 + 点）。

    亻与「仙 / 仁」共用 ren()；厶与「払」共用 mushi()，坐标完全一致
    （左侧部件宽度相近，右侧部件不必另起一套坐标）。
    """
    g = Glyph("uni4ECF", advance=1000, unicode=0x4ECF, note="仏：亻 + 厶")
    ren(g)
    mushi(g)
    return g


def g_ei() -> Glyph:
    """永（5画）：丶 + 丨（竖）+ 𠃋（横 + 撇）+ 撇 + 捺。

    部件分区：点 x 422..498、y 672..817；竖 452..548、y 120..700；
    横撇 195..500、y 500..686；下部撇 137..548、捺 457..923。
    结构取"水 + 顶上一點"：横撇的横从竖向左伸出（不可向右，否则读成"亠"），
    点为短斜撇并压在竖顶（y 672..700 与竖墨迹相交）。
    下撇起笔 (500,380)、捺起笔 (505,420) 都落在竖墨迹 452..548 上。
    """
    g = Glyph("uni6C38", advance=1000, unicode=0x6C38, note="永：点 + 水")
    g.diag(530, 790, 460, 710, W_THIN)     # 点（短斜）
    vspan(g, 500, 120, 700, W_MAIN)         # 竖
    bar_at(g, 640, 290, 500, W_SEC)         # 横撇的横（向左）
    g.diag(290, 640, 195, 500, W_MAIN)      # 横撇的撇
    g.diag(500, 380, 185, 60, W_MAIN)       # 下撇
    g.diag(505, 420, 875, 90, W_MAIN)       # 捺
    return g


def g_kan() -> Glyph:
    """刊（5画）：干（一 + 一 + 丨）+ 刂（丨 + 竖钩）。

    部件分区：干 x 110..600；刂 x 654..928。
    刂两竖墨迹 654..746 与 832..928，竖间净距 86 ≥ 60。
    干的下横右端 580 → 刂短竖墨迹左缘 654，净距 74。
    """
    g = Glyph("uni520A", advance=1000, unicode=0x520A, note="刊：干 + 刂")
    bar_top(g, 200, 520, W_SEC)          # 干的上横
    bar_at(g, 520, 110, 580, W_MAIN)      # 干的下横
    vspan(g, 370, 0, 774, W_MAIN)        # 干的竖
    vspan(g, 700, 150, 620, W_SEC)       # 刂的短竖
    vspan(g, 880, 90, 820, W_MAIN)       # 刂的长竖
    g.diag(880, 105, 810, 190, W_THIN)   # 钩
    return g


def g_kou() -> Glyph:
    """功（5画）：工（一 + 丨 + 一）+ 力（乛 + 丿）。

    部件分区：工 x 32..498；力 x 472..928。
    工的竖 217..313 与力横起点 520 净距 207；力的撇底端墨迹 492..588，
    与工下横右端 450 净距 42（高度错开，互不相接）。
    """
    g = Glyph("uni529F", advance=1000, unicode=0x529F, note="功：工 + 力")
    bar_top(g, 100, 430, W_MAIN)                              # 工的上横
    vspan(g, 265, 60, 770, W_MAIN)                            # 工的竖
    bar_base(g, 80, 450, W_MAIN)                              # 工的下横
    bar_at(g, 640, 520, 900, W_MAIN)                          # 力的横
    vspan(g, 860, 180, 640, W_MAIN)                           # 力的竖钩
    g.diag(860, 195, 795, 275, W_THIN)                        # 钩
    diag_cap_base(g, 540, 700, W_MAIN, y_bot=0, y_top=640)    # 力的撇
    return g


def g_ketsu() -> Glyph:
    """欠（4画）：𠂊（丿 + 乛）+ 人（丿 + 捺）。

    部件分区：上 𠂊 x 282..828、y 352..790；下人 x 122..918。
    𠂊的撇末端与横左端相接（横墨迹 592..688）；
    乛的撇末端墨迹 512..608 与人的撇起笔 (600,430) 相接。
    """
    g = Glyph("uni6B20", advance=1000, unicode=0x6B20, note="欠：𠂊 + 人")
    g.diag(470, 790, 330, 645, W_MAIN)      # 𠂊的撇
    bar_at(g, 640, 330, 780, W_MAIN)         # 乛的横
    g.diag(780, 640, 560, 400, W_MAIN)       # 乛的撇
    g.diag(600, 430, 170, 50, W_MAIN)        # 人的撇
    g.diag(540, 360, 870, 70, W_MAIN)        # 人的捺
    return g


def g_han() -> Glyph:
    """犯（5画）：犭（丿 + 弯钩 + 丿）+ 㔾（横折 + 乚）。

    部件分区：犭 x 82..398；㔾 x 572..928。
    犭右缘 398 → 㔾左缘 572，净距 174。
    㔾的下横墨迹 12..108，右竖钩自 (895,80) 上挑。
    """
    g = Glyph("uni72AF", advance=1000, unicode=0x72AF, note="犯：犭 + 㔾")
    g.diag(345, 795, 190, 700, W_SEC)       # 犭的撇（顶端短撇）
    g.diag(255, 675, 345, 555, W_MAIN)      # 犭的弯钩上段（陡一点，避免折成"＞"）
    vspan(g, 345, 150, 555, W_MAIN)         # 犭的弯钩下段
    g.diag(345, 165, 270, 245, W_THIN)      # 犭的钩
    g.diag(345, 515, 120, 50, W_MAIN)       # 犭的长撇
    bar_at(g, 620, 600, 880, W_MAIN)        # 㔾的横折
    vspan(g, 880, 350, 620, W_MAIN)
    vspan(g, 620, 60, 350, W_MAIN)          # 㔾的竖
    bar_at(g, 60, 620, 900, W_MAIN)         # 㔾的底
    g.diag(895, 80, 850, 160, W_THIN)
    return g


def g_fu() -> Glyph:
    """布（5画）：𠂇（一 + 丿）+ 巾（丨 + 乛 + 丨）。

    部件分区：𠂇 x 62..918；巾 x 404..918。
    巾三竖墨迹：左 404..496、中 602..698、右 822..918，竖间净距 106 / 124。
    𠂇的丿在 y=600 处心线 x≈292（墨迹 244..340），巾左竖墨迹左缘 404，
    净距 64。
    """
    g = Glyph("uni5E03", advance=1000, unicode=0x5E03, note="布：𠂇 + 巾")
    bar_top(g, 150, 870, W_MAIN)                              # 一
    diag_cap_base(g, 110, 340, W_MAIN, y_bot=0, y_top=760)     # 丿
    bar_at(g, 600, 450, 880, W_MAIN)                           # 巾的冂顶
    vspan(g, 450, 240, 560, W_SEC)                             # 巾的左竖
    vspan(g, 870, 180, 600, W_MAIN)                            # 巾的右竖
    g.diag(865, 195, 800, 275, W_THIN)                         # 钩
    vspan(g, 650, 0, 640, W_MAIN)                              # 巾的中竖
    return g


def g_kyo() -> Glyph:
    """巨（4画）：匚（一 + 竖折）+ コ（一 + 丨）。

    部件分区：外框 x 132..820；内コ x 300..806。
    内横左端 300 与外左竖墨迹 132..228，净距 72 ≥ 60。
    内竖底端 60 落在底横墨迹（0..96）内。
    """
    g = Glyph("uni5DE8", advance=1000, unicode=0x5DE8, note="巨：匚 + コ")
    bar_top(g, 180, 820, W_MAIN)     # 匚的一
    vspan(g, 180, 0, 820, W_MAIN)    # 匚的竖
    bar_base(g, 180, 820, W_MAIN)    # 匚的底
    bar_at(g, 560, 300, 760, W_SEC)  # 内横
    vspan(g, 760, 60, 560, W_SEC)    # 内竖
    return g


def g_go() -> Glyph:
    """互（4画）：一（上）+ 彑（横 + 右竖 + 左竖）+ 一（下）。

    部件分区：上横 210..790；中横 300..700；下横 130..870。
    右竖 654..746 与左竖 254..346，竖间净距 308。
    右竖顶 790 落在上横墨迹（724..820）内，底 480 落在中横墨迹内；
    左竖顶 480 落在中横墨迹内，底 60 落在下横墨迹（0..96）内。
    """
    g = Glyph("uni4E92", advance=1000, unicode=0x4E92, note="互：一 + 彑 + 一")
    bar_top(g, 210, 790, W_MAIN)
    bar_at(g, 480, 300, 700, W_SEC)
    vspan(g, 700, 480, 790, W_SEC)     # 右竖
    vspan(g, 300, 60, 480, W_SEC)      # 左竖
    bar_base(g, 130, 870, W_MAIN)
    return g


def g_fuda() -> Glyph:
    """札（5画）：木（一 + 丨 + 丿 + 捺）+ 乙（一 + 撇 + 一 + 钩）。

    部件分区：木 x 42..478；乙 x 572..928。
    木的捺底端墨迹 382..478，乙下横左端 620，净距 142。
    乙的撇底端与下横墨迹（132..228）相接。
    """
    g = Glyph("uni672D", advance=1000, unicode=0x672D, note="札：木 + 乙")
    bar_at(g, 700, 100, 400, W_MAIN)                       # 木的一
    vspan(g, 250, 0, 820, W_MAIN)                          # 木的竖
    diag_cap_base(g, 90, 250, W_MAIN, y_bot=0, y_top=700)  # 木的撇
    diag_cap_base(g, 430, 250, W_MAIN, y_bot=0, y_top=700)  # 木的捺
    bar_at(g, 700, 560, 880, W_MAIN)                       # 乙的一
    g.diag(880, 700, 620, 180, W_MAIN)                     # 乙的撇
    bar_at(g, 180, 620, 900, W_MAIN)                       # 乙的底
    g.diag(895, 195, 850, 275, W_THIN)                     # 钩
    return g


def g_yuu() -> Glyph:
    """夕（3画）：丿 + 乛（横 + 撇）+ 丶。

    部件分区：x 300..918、y 72..826。
    撇末端与横左端相接（横墨迹 592..688）；
    点墨迹 468..552 与乛撇墨迹 614..710 净距 62。
    """
    g = Glyph("uni5915", advance=1000, unicode=0x5915, note="夕：丿 + 乛 + 点")
    g.diag(540, 790, 330, 650, W_SEC)
    bar_at(g, 640, 330, 870, W_MAIN)
    g.diag(870, 640, 420, 120, W_MAIN)
    g.dot(510, 400, 84, 100)
    return g


def g_tsutsumi() -> Glyph:
    """包（5画）：勹（丿 + 乛横折钩）+ 巳（横折 + 一 + 乚）。

    部件分区：勹 x 332..928；巳 x 132..806。
    勹的撇末端墨迹 332..428 与巳顶横墨迹（474..566）净空 46；
    巳右竖墨迹 614..706，勹右竖墨迹 812..908，净距 106。
    """
    g = Glyph("uni5305", advance=1000, unicode=0x5305, note="包：勹 + 巳")
    g.diag(620, 790, 380, 640, W_MAIN)     # 勹的撇
    bar_at(g, 640, 380, 870, W_MAIN)        # 勹的横
    vspan(g, 860, 180, 640, W_MAIN)         # 勹的竖钩
    g.diag(855, 195, 790, 275, W_THIN)      # 钩
    bar_at(g, 520, 180, 660, W_SEC)         # 巳的横折
    vspan(g, 660, 300, 520, W_SEC)
    bar_at(g, 300, 180, 660, W_SEC)         # 巳的中横
    vspan(g, 180, 60, 300, W_SEC)           # 巳的竖
    bar_at(g, 60, 180, 770, W_MAIN)         # 巳的底
    g.diag(765, 75, 720, 155, W_THIN)
    return g


def g_sou() -> Glyph:
    """双（4画）：又 + 又（各 横撇 + 捺）。

    部件分区：左又 x 112..468；右又 x 452..928。
    左又的捺底端墨迹 352..448，右又横撇底端墨迹 522..618，净距 74。
    """
    g = Glyph("uni53CC", advance=1000, unicode=0x53CC, note="双：又 + 又")
    bar_at(g, 640, 140, 380, W_SEC)         # 左又的横
    g.diag(380, 640, 160, 90, W_SEC)        # 左又的横撇
    g.diag(165, 620, 400, 130, W_MAIN)      # 左又的捺
    bar_at(g, 640, 500, 830, W_MAIN)        # 右又的横
    g.diag(830, 640, 570, 90, W_MAIN)       # 右又的横撇
    g.diag(545, 620, 880, 130, W_MAIN)      # 右又的捺
    return g


def g_kou_bitsu() -> Glyph:
    """甲（5画）：田 + 贯穿竖（下端出头）。

    部件分区：外框 x 184..816、y 102..748；中竖 x 452..548、y 0..700。
    上格净高 652-466 = 186，下格净高 374-198 = 176；
    竖间净距 184..452 = 268 与 548..724 = 176。
    """
    g = Glyph("uni7532", advance=1000, unicode=0x7532, note="甲：田 + 中竖出头")
    kuchi_box(g, 230, 770, 700, 150, y_mid=420)
    vspan(g, 500, 0, 700, W_MAIN)
    return g


def g_hen() -> Glyph:
    """片（4画）：丿 + 丨（左）+ 丨（右）+ 一。

    部件分区：左 x 232..328；右 x 614..706；横 140..900。
    丿末端墨迹与左竖墨迹（232..328）相接；右竖底端 380 落在横墨迹内。
    """
    g = Glyph("uni7247", advance=1000, unicode=0x7247, note="片：丿 + 丨 + 丨 + 一")
    g.diag(420, 810, 280, 700, W_THIN)    # 丿
    vspan(g, 280, 0, 800, W_MAIN)         # 左竖
    vspan(g, 660, 380, 800, W_SEC)        # 右竖
    bar_at(g, 380, 140, 900, W_MAIN)      # 横
    return g


def g_fuyu() -> Glyph:
    """冬（5画）：夂（丿 + 乛 + 捺）+ ⺀（两点）。

    部件分区：夂 x 272..898；两点 x 356..604。
    两点墨迹 x 356..444 与 516..604，净距 72，不粘连。
    """
    g = Glyph("uni51AC", advance=1000, unicode=0x51AC, note="冬：夂 + 两点")
    g.diag(480, 790, 320, 660, W_MAIN)     # 夂的撇
    bar_at(g, 660, 320, 780, W_MAIN)        # 夂的横
    g.diag(780, 660, 540, 400, W_MAIN)      # 夂的横撇
    g.diag(560, 450, 850, 90, W_MAIN)       # 夂的捺
    g.dot(400, 230, 88, 104)                # 上の点
    g.dot(560, 110, 88, 104)                # 下の点
    return g


def g_kawa() -> Glyph:
    """皮（5画）：丿（左斜）+ 乛（一 + 钩）+ 一 + 竖撇 + 捺。

    部件分区：上 x 202..897；中横 170..790；下撇 132..598、捺 482..938。
    丿顶端墨迹落在乛横墨迹（712..808）内；丿末端与中横墨迹（382..478）相接。
    """
    g = Glyph("uni76AE", advance=1000, unicode=0x76AE, note="皮：丿 + 乛 + 一 + 竖撇 + 捺")
    g.diag(420, 790, 250, 420, W_SEC)      # 左斜的撇
    bar_at(g, 760, 330, 860, W_MAIN)         # 乛的横
    g.diag(855, 760, 790, 665, W_THIN)      # 乛的钩
    bar_at(g, 430, 170, 790, W_MAIN)         # 中横
    vspan(g, 550, 380, 760, W_MAIN)          # 竖撇的上段
    g.diag(545, 400, 180, 50, W_MAIN)       # 竖撇的下段
    g.diag(530, 390, 890, 60, W_MAIN)       # 捺
    return g


def g_ki() -> Glyph:
    """己（3画）：𠃍（横折）+ 一（中横）+ 乚（竖弯钩）。

    部件分区：上 x 230..770；中横 230..660；下 230..770。
    右竖底端 560 与中横墨迹顶 528 留空 32（己字的右上开口）；
    竖与竖净距 184..278 = 94。
    """
    g = Glyph("uni5DF1", advance=1000, unicode=0x5DF1, note="己：横折 + 一 + 乚")
    bar_at(g, 740, 230, 770, W_SEC)
    vspan(g, 770, 560, 740, W_SEC)
    bar_at(g, 480, 230, 660, W_SEC)
    vspan(g, 230, 60, 480, W_SEC)
    bar_at(g, 60, 230, 770, W_SEC)
    g.diag(765, 75, 710, 150, W_THIN)
    return g


def g_sen() -> Glyph:
    """仙（5画）：亻（撇 + 竖）+ 山（丨 + 竖折 + 丨）。

    亻与批内「仏 / 仁」共用 ren()。
    山分区 x 452..928；山三竖墨迹 452..548 / 612..708 / 832..928，
    竖间净距 64 / 124。
    """
    g = Glyph("uni4ED9", advance=1000, unicode=0x4ED9, note="仙：亻 + 山")
    ren(g)
    vspan(g, 660, 60, 820, W_MAIN)      # 山的中间竖（最高）
    bar_base(g, 500, 880, W_MAIN)        # 山的底横
    vspan(g, 500, 60, 560, W_SEC)        # 山的左竖
    vspan(g, 880, 60, 380, W_SEC)        # 山的右竖
    return g


def g_ke() -> Glyph:
    """毛（4画）：丿 + 一 + 一 + 乚（竖弯钩）。

    部件分区：撇 132..448；上横 200..820；中横 150..850；底扫 472..928。
    撇末端墨迹 132..228 与上横墨迹（572..668）相接；
    竖 x=520（472..568）穿过两横。
    """
    g = Glyph("uni6BDB", advance=1000, unicode=0x6BDB, note="毛：丿 + 二 + 乚")
    g.diag(400, 790, 180, 700, W_SEC)
    bar_at(g, 620, 200, 820, W_MAIN)
    bar_at(g, 430, 150, 850, W_MAIN)
    vspan(g, 520, 60, 620, W_MAIN)
    bar_at(g, 60, 520, 880, W_MAIN)
    g.diag(875, 75, 830, 155, W_THIN)
    return g


def g_rei_shimesu() -> Glyph:
    """礼（5画）：礻（丶 + 横撇 + 丨 + 丶）+ 乚（竖弯钩）。

    部件分区：礻 x 100..424；乚 x 572..928。
    礻的右点墨迹 336..424 与竖墨迹（172..268）净距 68；
    礻右缘 424 → 乚左缘 572，净距 148。
    """
    g = Glyph("uni793C", advance=1000, unicode=0x793C, note="礼：礻 + 乚")
    g.dot(180, 760, 88, 110)          # 礻的点
    bar_at(g, 640, 110, 320, W_SEC)    # 礻的横
    g.diag(320, 640, 160, 540, W_SEC)  # 礻的撇
    vspan(g, 220, 0, 640, W_MAIN)      # 礻的竖
    g.dot(380, 340, 88, 100)          # 礻的右点
    vspan(g, 620, 120, 700, W_MAIN)    # 乚的竖
    bar_at(g, 120, 620, 880, W_MAIN)   # 乚的底
    g.diag(875, 135, 830, 215, W_THIN)
    return g


def g_ushi() -> Glyph:
    """牛（4画）：丿 + 一（短）+ 一（长）+ 丨。

    部件分区：丿 272..608；上横 280..780；下横 120..860；竖 512..608。
    撇起笔 (560,780) 压在竖上，末端 (320,690) 与上横墨迹（592..688）相接。
    """
    g = Glyph("uni725B", advance=1000, unicode=0x725B, note="牛：丿 + 二 + 丨")
    vspan(g, 560, 0, 790, W_MAIN)
    g.diag(560, 780, 320, 690, W_SEC)
    bar_at(g, 640, 280, 780, W_MAIN)
    bar_at(g, 430, 120, 860, W_MAIN)
    return g


def g_an() -> Glyph:
    """兄（5画）：口（3 笔）+ 儿（丿 + 乚）。

    部件分区：口 x 254..746、y 388..748；儿 x 182..918。
    口内净空 526..652 = 126；
    撇起笔 (430,460) 与口底横墨迹（432..528）相接。
    """
    g = Glyph("uni5144", advance=1000, unicode=0x5144, note="兄：口 + 儿")
    kuchi_box(g, 300, 700, 700, 480)
    g.diag(430, 460, 230, 40, W_MAIN)
    vspan(g, 640, 60, 460, W_MAIN)
    bar_at(g, 60, 640, 870, W_MAIN)
    g.diag(865, 75, 820, 155, W_THIN)
    return g


def g_toki() -> Glyph:
    """幼（5画）：幺（𠃋 + 𠃋 + 丶）+ 力（乛 + 丿）。

    部件分区：幺 x 112..392；力 x 472..928。
    第二撇折的撇起笔 (330,620) 与第一折横墨迹（574..666）相接；
    幺的末点墨迹 286..374、y 148..252 与折横墨迹（294..386）净空 42。
    """
    g = Glyph("uni5E7C", advance=1000, unicode=0x5E7C, note="幼：幺 + 力")
    g.diag(330, 790, 160, 620, W_SEC)      # 幺的第一撇
    bar_at(g, 620, 160, 300, W_SEC)         # 幺的第一折
    g.diag(330, 620, 180, 340, W_SEC)       # 幺的第二撇
    bar_at(g, 340, 180, 320, W_SEC)         # 幺的第二折
    g.dot(330, 200, 88, 104)                # 幺的末点
    bar_at(g, 640, 520, 900, W_MAIN)        # 力的横
    vspan(g, 880, 180, 640, W_MAIN)         # 力的竖钩
    g.diag(875, 195, 810, 275, W_THIN)      # 钩
    diag_cap_base(g, 540, 700, W_MAIN, y_bot=0, y_top=640)  # 力的撇
    return g


def g_ku() -> Glyph:
    """句（5画）：勹（丿 + 乛横折钩）+ 口。

    部件分区：勹 x 432..928；口 x 192..726。
    勹的撇末端墨迹 432..528 与口顶横墨迹（372..468）净空 64；
    口右竖墨迹 634..726，勹右竖墨迹 822..918，净距 96。
    """
    g = Glyph("uni53E5", advance=1000, unicode=0x53E5, note="句：勹 + 口")
    g.diag(700, 790, 480, 640, W_MAIN)
    bar_at(g, 700, 420, 880, W_MAIN)
    vspan(g, 870, 160, 700, W_MAIN)
    g.diag(865, 175, 800, 255, W_THIN)
    kuchi_box(g, 240, 680, 420, 60)
    return g


def g_kan_ama() -> Glyph:
    """甘（5画）：一（上）+ 丨 + 丨 + 一（中）+ 一（下）。

    部件分区：上横 140..860；两竖 282..378 / 622..718；中横 200..800；
    下横 180..820。两竖墨迹净距 244。
    """
    g = Glyph("uni7518", advance=1000, unicode=0x7518, note="甘：三横两竖")
    bar_top(g, 140, 860, W_MAIN)
    bar_at(g, 420, 200, 800, W_SEC)
    bar_base(g, 180, 820, W_MAIN)
    vspan(g, 330, 60, 780, W_MAIN)
    vspan(g, 670, 60, 780, W_MAIN)
    return g


def g_jun() -> Glyph:
    """巡（5画）：巛（3 笔）+ 辶（丶 + 折 + 底扫）。

    辶与 Wave 1 批次（辺 / 込）的 shinnyou() 共用同一坐标（GLY-004 跨批同族）。
    巛占 x 294..856、y 603..817：三笔等距左下斜行，间距 170（墨迹净距 53），
    读作三道波纹；若画得太短会退化成一串小方块（自检第 2 轮修掉）。
    巛底墨迹 603 与辶折横墨迹（474..566）净空 37。
    """
    g = Glyph("uni5DE1", advance=1000, unicode=0x5DE1, note="巡：巛 + 辶")
    shinnyou(g)
    g.diag(470, 790, 340, 630, W_THIN)
    g.diag(640, 790, 510, 630, W_THIN)
    g.diag(810, 790, 680, 630, W_THIN)
    return g


def g_ya() -> Glyph:
    """矢（5画）：丿 + 一（短）+ 一（长）+ 丿 + 捺。

    部件分区：上撇 252..568；短横 260..760；长横 160..840。
    撇末端墨迹 252..348 与短横墨迹（652..748）相接；
    长横墨迹 472..568，丿捺起笔都落在其上。
    """
    g = Glyph("uni77E2", advance=1000, unicode=0x77E2, note="矢：丿 + 二 + 人")
    g.diag(520, 800, 300, 700, W_SEC)
    bar_at(g, 700, 260, 760, W_MAIN)
    bar_at(g, 520, 160, 840, W_MAIN)
    g.diag(520, 520, 180, 60, W_MAIN)
    g.diag(540, 500, 880, 80, W_MAIN)
    return g


def g_chou_tetsu() -> Glyph:
    """丁（2画）：一 + 亅（竖钩）。

    部件分区：横 100..900；竖 452..548、y 100..772；钩 (500,115)→(440,195)。
    竖顶 772 落在横墨迹（724..820）内。
    """
    g = Glyph("uni4E01", advance=1000, unicode=0x4E01, note="丁：一 + 竖钩")
    bar_top(g, 100, 900, W_MAIN)
    vspan(g, 500, 100, 772, W_MAIN)
    g.diag(500, 115, 440, 195, W_THIN)
    return g


def g_satsu() -> Glyph:
    """冊（5画）：丨 + 𠃍 + 丨 + 丨 + 一。

    部件分区：外框 x 184..826；内竖 371..455 / 555..639。
    四竖墨迹净距 95 / 100 / 95，均 ≥ 60。
    册字四竖皆长，故竖用 92、内竖用 84 局部减重（GLY-001），
    顶横压到 770 让字面不顶死版心。
    """
    g = Glyph("uni518A", advance=1000, unicode=0x518A, note="冊：框 + 两内竖")
    bar_at(g, 770, 230, 780, W_MAIN)
    bar_base(g, 230, 780, W_MAIN)
    vspan(g, 230, 60, 770, W_SEC)
    vspan(g, 780, 60, 770, W_SEC)
    vspan(g, 413, 60, 770, W_THIN)
    vspan(g, 597, 60, 770, W_THIN)
    return g


def g_inu() -> Glyph:
    """犬（4画）：大（一 + 丿 + 捺）+ 丶。

    部件分区：横 150..830；丿 102..568；捺 472..928；点 746..834、y 710..810。
    捺起笔 (520,640) 的墨迹与横墨迹（592..688）相接。
    """
    g = Glyph("uni72AC", advance=1000, unicode=0x72AC, note="犬：大 + 点")
    bar_at(g, 640, 150, 830, W_MAIN)
    diag_cap_base(g, 150, 520, W_MAIN, y_bot=0, y_top=790)
    diag_cap_base(g, 880, 520, W_MAIN, y_bot=0, y_top=640)
    g.dot(790, 760, 88, 100)
    return g


def g_jin() -> Glyph:
    """仁（4画）：亻（撇 + 竖）+ 二（一 + 一）。

    亻与批内「仏 / 仙」共用 ren()。
    二：上横 480..880；下横 440..900；两横墨迹 592..688 / 0..96。
    亻右缘 378 → 二下横左端 440，净距 62。
    """
    g = Glyph("uni4EC1", advance=1000, unicode=0x4EC1, note="仁：亻 + 二")
    ren(g)
    bar_at(g, 640, 480, 880, W_MAIN)
    bar_base(g, 440, 900, W_MAIN)
    return g


# --------------------------------------------------------------------------
# 批次清单
# --------------------------------------------------------------------------
def build() -> list[Glyph]:
    """本批 40 字，按《常用漢字表》频率顺序排列。"""
    return [
        g_seru(),        # 占
        g_attsu(),       # 圧
        g_tamashii(),    # 玉
        g_tsukasa(),     # 司
        g_ryou(),        # 了
        g_chou(),        # 庁
        g_rei(),         # 令
        g_harai(),       # 払
        g_butsu(),       # 仏
        g_ei(),          # 永
        g_kan(),         # 刊
        g_kou(),         # 功
        g_ketsu(),       # 欠
        g_han(),         # 犯
        g_fu(),          # 布
        g_kyo(),         # 巨
        g_go(),          # 互
        g_fuda(),        # 札
        g_yuu(),         # 夕
        g_tsutsumi(),    # 包
        g_sou(),         # 双
        g_kou_bitsu(),   # 甲
        g_hen(),         # 片
        g_fuyu(),        # 冬
        g_kawa(),        # 皮
        g_ki(),          # 己
        g_sen(),         # 仙
        g_ke(),          # 毛
        g_rei_shimesu(), # 礼
        g_ushi(),        # 牛
        g_an(),          # 兄
        g_toki(),        # 幼
        g_ku(),          # 句
        g_kan_ama(),     # 甘
        g_jun(),         # 巡
        g_ya(),          # 矢
        g_chou_tetsu(),  # 丁
        g_satsu(),       # 冊
        g_inu(),         # 犬
        g_jin(),         # 仁
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s1-001.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
