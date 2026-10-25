"""HK Poster Heavy —— Jōyō 常用漢字 joyo-s1-003。

本批 40 字，笔画范围 3–5，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
1. 字面框与 zh-HK 繁体汉字完全一致：x 60..940、y 0..820，advance 1000。
   保证 zh-HK / ja / zh-CN 混排时基线与视觉大小一致。
2. 笔画权重沿用 CJK 档：主 96 / 次 92 / 细 84 / 点 84–96。本批全是
   3–5 画的低密度字，若取轻字重会整体"发飘"，因此主干一律 96；
   只在叠横、竖间等密排处局部降到 92/84 保内白（GLY-001 允许密排减重）。
3. 部件复用（GLY-004，docs/03）：同一部件在批内必须用同一套坐标与
   同一套笔画拆法，只做位置与大小的光学校正。本批的复用件：
   · 亻（仕 / 他）共用同一坐标与拆法；
   · 辶（辺 / 込）共用同一坐标与拆法；
   · 口 / 日 统一走 kuchi_box()（左竖 + 横折 + 中横 + 底横），只改尺寸；
   · 木骨架（末 / 未）共用同一坐标，只交换上下横的长短。
4. 对齐语义（与 hkposter-latin.py 同办法）：
   · 横画按"墨迹上缘 / 下缘"定位，中心线内缩半个笔画宽；
   · 竖画端点即墨迹端点；
   · 斜画用 diag_cap_base()，让墨迹下缘贴 0、上缘贴目标高度，
     避免斜画溢出版心或顶不到版心。
5. 内白下限（GLY-006）：叠横净空 ≥ 24，竖间净空 ≥ 60。每个字的
   docstring 里写明笔画清单与部件分区坐标，便于复核。
6. 禁止逐字机械挤压或倾斜（docs/02 偏差 D）：斜笔画只出现在汉字本身的
   撇捺结构上，不对整字做倾斜或横向压缩。
7. 钩（乚 / ㇆ 的收笔）一律"起笔落在前一笔的墨迹内部"，不让两笔在端点
   处形成对顶缺口——并集后会出现一个悬空的独立小块。
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
    """口 / 日：左竖 + 横折（顶横+右竖）+ 中横（可选）+ 底横。

    x1 / x2 为左右竖的中心线；y_top / y_bot / y_mid 为横画的中心线。
    """
    bar_at(g, y_top, x1, x2, wh)
    vspan(g, x1, y_top, y_bot, wv)
    vspan(g, x2, y_top, y_bot, wv)
    bar_at(g, y_bot, x1, x2, wh)
    if y_mid is not None:
        bar_at(g, y_mid, x1, x2, W_SEC)


def ren(g: Glyph) -> None:
    """亻（人字旁）：撇 + 竖。仕 / 他 共用同一坐标。

    撇从右上斜掠到左下（比竖心高 300 单位），竖顶落在撇的中段上
    （y=664 处撇心线正好过 x=255），两者只在小面积相交，不会粘成一团。
    """
    g.diag(330, 780, 130, 470, W_MAIN)
    vspan(g, 255, 664, 0, W_MAIN)


def shinnyou(g: Glyph) -> None:
    """辶（しんにょう）：点 + 折 + 底扫。辺 / 込 共用同一坐标。"""
    g.dot(160, 690, 110, 120)
    bar_at(g, 520, 110, 270, W_SEC)
    vspan(g, 190, 520, 220, W_SEC)
    g.diag(200, 220, 900, 100, W_MAIN)


# --------------------------------------------------------------------------
# 字形
# --------------------------------------------------------------------------
def g_bi() -> Glyph:
    """比（4画）：左匕（一 + 竖 + 提）+ 右匕（撇 + 竖 + 竖弯钩）。

    部件分区：左 x 90..375，右 x 632..855。
    竖间净空 632-298 = 334 ≥ 60。
    """
    g = Glyph("uni6BD4", advance=1000, unicode=0x6BD4, note="比：左匕横提，右匕撇竖弯")
    bar_at(g, 640, 90, 300, W_SEC)
    vspan(g, 250, 640, 150, W_MAIN)
    g.diag(250, 150, 375, 235, W_SEC)
    g.diag(790, 720, 655, 600, W_SEC)
    vspan(g, 680, 820, 120, W_MAIN)
    g.diag(680, 120, 855, 205, W_MAIN)
    return g


def g_fu() -> Glyph:
    """夫（4画）：一（短）+ 一（长）+ 撇 + 捺。

    上下横之间净空 724-648 = 76 ≥ 24。
    """
    g = Glyph("uni592B", advance=1000, unicode=0x592B, note="夫：二横 + 人")
    bar_top(g, 250, 750)
    bar_at(g, 600, 150, 850)
    diag_cap_base(g, 140, 330, W_MAIN, y_bot=0.0, y_top=772.0)
    diag_cap_base(g, 860, 520, W_MAIN, y_bot=0.0, y_top=600.0)
    return g


def g_shu() -> Glyph:
    """収（5画）：丩（竖 + 竖弯）+ 又（横撇 + 捺）。

    部件分区：丩 x 142..588，又 x 422..898。
    丩右竖（墨迹 388）与又顶横起点（墨迹 422）净空 34 ≥ 24。
    """
    g = Glyph("uni53CE", advance=1000, unicode=0x53CE, note="収：丩 + 又")
    vspan(g, 190, 800, 300, W_MAIN)
    vspan(g, 340, 800, 140, W_MAIN)
    bar_at(g, 140, 340, 540, W_SEC)
    bar_at(g, 650, 470, 850, W_MAIN)
    g.diag(850, 650, 560, 280, W_MAIN)
    g.diag(490, 640, 880, 240, W_MAIN)
    return g


def g_jing() -> Glyph:
    """井（4画）：横 + 横 + 撇（竖）+ 竖。

    竖间净空 612-388 = 224 ≥ 60；两横净空 652-278 = 374 ≥ 24。
    """
    g = Glyph("uni4E95", advance=1000, unicode=0x4E95, note="井：两横两竖，左竖微撇")
    bar_at(g, 700, 140, 860)
    bar_at(g, 230, 140, 860)
    diag_cap_base(g, 310, 370, W_MAIN, y_bot=0.0, y_top=820.0)
    vspan(g, 660, 820, 0, W_MAIN)
    return g


def g_shitsu() -> Glyph:
    """石（5画）：一 + 撇 + 口。

    口分区 x 354..876、y 0..430；口内净空 774-446 = 328。
    """
    g = Glyph("uni77F3", advance=1000, unicode=0x77F3, note="石：一 + 撇 + 口")
    bar_top(g, 150, 850)
    diag_cap_base(g, 140, 300, W_MAIN, y_bot=0.0, y_top=772.0)
    kuchi_box(g, 400, 830, 382, 48)
    return g


def g_man() -> Glyph:
    """万（3画）：一 + 横折钩 + 撇。

    撇自顶横中段下行，横折钩位于右下；撇与钩之间净空 544-307 = 237。
    钩的起笔落在竖的墨迹内部，避免对顶缺口。
    """
    g = Glyph("uni4E07", advance=1000, unicode=0x4E07, note="万：一 + 横折钩 + 撇")
    bar_top(g, 130, 870)
    bar_at(g, 470, 210, 590, W_SEC)
    vspan(g, 590, 470, 170, W_SEC)
    g.diag(585, 195, 505, 250, W_THIN)
    diag_cap_base(g, 160, 540, W_MAIN, y_bot=0.0, y_top=772.0)
    return g


def g_heritsu() -> Glyph:
    """辺（4画）：刀（横折钩 + 撇）+ 辶（点 + 折 + 底扫）。

    辶 与 込 共用 shinnyou()，坐标完全一致。
    """
    g = Glyph("uni8FBA", advance=1000, unicode=0x8FBA, note="辺：刀 + 辶")
    bar_at(g, 700, 390, 790, W_MAIN)
    vspan(g, 790, 700, 400, W_MAIN)
    g.diag(785, 415, 700, 350, W_THIN)
    g.diag(620, 700, 380, 330, W_MAIN)
    shinnyou(g)
    return g


def g_shi() -> Glyph:
    """仕（5画）：亻（撇 + 竖）+ 士（横 + 竖 + 横）。

    亻与「他」共用 ren()；士上横长、下横短。
    """
    g = Glyph("uni4ED5", advance=1000, unicode=0x4ED5, note="仕：亻 + 士")
    ren(g)
    bar_at(g, 640, 420, 900, W_MAIN)
    vspan(g, 660, 640, 230, W_MAIN)
    bar_at(g, 230, 480, 860, W_SEC)
    return g


def g_kyo() -> Glyph:
    """去（5画）：土（横 + 竖 + 横）+ 厶（撇折 + 点）。

    土下横墨迹下缘 382 与厶撇起笔墨迹上缘 ≈397 相连（无断口）。
    点压在撇折横的右端上方，净空 38，不与横画粘连。
    """
    g = Glyph("uni53BB", advance=1000, unicode=0x53BB, note="去：土 + 厶")
    bar_at(g, 700, 240, 760)
    vspan(g, 500, 700, 430, W_MAIN)
    bar_at(g, 430, 150, 850)
    g.diag(450, 380, 320, 90, W_MAIN)
    bar_base(g, 320, 620, W_MAIN)
    g.dot(600, 190, 96, 112)
    return g


def g_sitsu() -> Glyph:
    """失（5画）：撇（短）+ 一 + 一 + 撇 + 捺。

    上横与下横净空 654-508 = 146 ≥ 24。
    """
    g = Glyph("uni5931", advance=1000, unicode=0x5931, note="失：短撇 + 二 + 人")
    g.diag(350, 785, 240, 660, W_SEC)
    bar_at(g, 700, 240, 790, W_SEC)
    bar_at(g, 460, 110, 880)
    diag_cap_base(g, 160, 440, W_MAIN, y_bot=0.0, y_top=700.0)
    diag_cap_base(g, 860, 520, W_MAIN, y_bot=0.0, y_top=460.0)
    return g


def g_kaku() -> Glyph:
    """写（5画）：冖（点 + 横钩）+ 与（一 + 竖 + 右折 + 底横）。

    冖占 x 106..874；与占 x 170..840，竖自 600 直落到底横。
    冖左点改用短斜笔，斜入顶横，避免出现方块状的"角"。
    """
    g = Glyph("uni5199", advance=1000, unicode=0x5199, note="写：冖 + 与")
    g.diag(150, 690, 210, 780, W_THIN)
    bar_top(g, 200, 830)
    vspan(g, 830, 690, 772, W_MAIN)
    g.diag(815, 700, 755, 645, W_THIN)
    bar_at(g, 600, 280, 600, W_SEC)
    vspan(g, 380, 600, 60, W_SEC)
    bar_at(g, 330, 380, 700, W_SEC)
    bar_base(g, 170, 840)
    return g


def g_matsu() -> Glyph:
    """末（5画）：木骨架（竖 + 上横长 + 下横短 + 撇 + 捺）。

    与「未」共用同一坐标，只交换上下横长短。
    """
    g = Glyph("uni672B", advance=1000, unicode=0x672B, note="末：上横长")
    vspan(g, 500, 820, 0, W_MAIN)
    bar_at(g, 700, 130, 870)
    bar_at(g, 470, 220, 780)
    diag_cap_base(g, 140, 500, W_MAIN, y_bot=0.0, y_top=470.0)
    diag_cap_base(g, 860, 500, W_MAIN, y_bot=0.0, y_top=470.0)
    return g


def g_mizu() -> Glyph:
    """白（5画）：撇 + 日（竖 + 横折 + 中横 + 底横）。

    日内两格净高各 208 ≥ 24；竖间净空 714-286 = 428。
    """
    g = Glyph("uni767D", advance=1000, unicode=0x767D, note="白：撇 + 日")
    g.diag(320, 785, 245, 700, W_SEC)
    kuchi_box(g, 240, 760, 652, 48, y_mid=350)
    return g


def g_shin() -> Glyph:
    """申（5画）：日 + 贯穿竖（上下出头）。

    两格净高各 122；中竖与左右竖净空各 186 ≥ 60。
    """
    g = Glyph("uni7533", advance=1000, unicode=0x7533, note="申：日 + 中竖出头")
    kuchi_box(g, 220, 780, 630, 198, y_mid=414)
    vspan(g, 500, 820, 0, W_MAIN)
    return g


def g_ko() -> Glyph:
    """古（5画）：十（一 + 竖）+ 口。

    口分区 x 204..796、y 0..448；竖与口两侧净空各 156 ≥ 60。
    """
    g = Glyph("uni53E4", advance=1000, unicode=0x53E4, note="古：十 + 口")
    bar_at(g, 700, 170, 830)
    vspan(g, 500, 820, 400, W_MAIN)
    kuchi_box(g, 250, 750, 400, 48)
    return g


def g_shi_ji() -> Glyph:
    """史（5画）：口 + 撇 + 捺。

    口分区 x 284..716、y 382..688；撇自口上横左段斜穿口左竖下行至基线，
    捺自口底横中段向右下冲出，两笔不切内白。
    """
    g = Glyph("uni53F2", advance=1000, unicode=0x53F2, note="史：口 + 乂")
    kuchi_box(g, 330, 670, 640, 430)
    diag_cap_base(g, 140, 390, W_MAIN, y_bot=0.0, y_top=700.0)
    diag_cap_base(g, 880, 400, W_MAIN, y_bot=0.0, y_top=430.0)
    return g


def g_ten() -> Glyph:
    """天（4画）：一（短）+ 一（长）+ 撇 + 捺。

    两横净空 724-648 = 76 ≥ 24。
    """
    g = Glyph("uni5929", advance=1000, unicode=0x5929, note="天：二 + 人")
    bar_top(g, 280, 720)
    bar_at(g, 600, 120, 880)
    diag_cap_base(g, 140, 490, W_MAIN, y_bot=0.0, y_top=600.0)
    diag_cap_base(g, 870, 510, W_MAIN, y_bot=0.0, y_top=600.0)
    return g


def g_shi_solo() -> Glyph:
    """士（3画）：一（长）+ 竖 + 一（短）。

    两横净空 652-246 = 406 ≥ 24。
    """
    g = Glyph("uni58EB", advance=1000, unicode=0x58EB, note="士：上横长下横短")
    bar_at(g, 700, 120, 880)
    vspan(g, 500, 700, 200, W_MAIN)
    bar_at(g, 200, 220, 780, W_SEC)
    return g


def g_maru() -> Glyph:
    """丸（3画）：九（撇 + 横折弯钩）+ 点。

    点置于撇与竖之间，净空 422-340 = 82 ≥ 60。
    钩的起笔落在底弯的墨迹内部，两笔连成一体。
    """
    g = Glyph("uni4E38", advance=1000, unicode=0x4E38, note="丸：九 + 点")
    diag_cap_base(g, 170, 400, W_MAIN, y_bot=0.0, y_top=810.0)
    bar_at(g, 700, 390, 730)
    vspan(g, 730, 700, 200, W_MAIN)
    g.diag(730, 200, 875, 135, W_MAIN)
    g.diag(845, 165, 890, 250, W_THIN)
    g.dot(470, 430, 96, 112)
    return g


def g_ta() -> Glyph:
    """他（5画）：亻（撇 + 竖）+ 也（横折钩 + 竖 + 竖弯钩）。

    亻与「仕」共用 ren()，坐标完全一致。
    也的两处钩都把起笔压进前一笔的墨迹内，避免悬空小块。
    """
    g = Glyph("uni4ED6", advance=1000, unicode=0x4ED6, note="他：亻 + 也")
    ren(g)
    bar_at(g, 700, 420, 870, W_MAIN)
    vspan(g, 870, 700, 545, W_MAIN)
    g.diag(855, 560, 795, 610, W_THIN)
    vspan(g, 650, 700, 130, W_MAIN)
    vspan(g, 450, 680, 130, W_MAIN)
    bar_base(g, 450, 870)
    g.diag(845, 95, 880, 185, W_THIN)
    return g


def g_kyuu() -> Glyph:
    """及（3画）：撇 + 横折折撇 + 捺。

    横折折撇占 x 320..788、y 392..748；捺自上部向右下冲出。
    """
    g = Glyph("uni53CA", advance=1000, unicode=0x53CA, note="及：丿 + 横折折撇 + 捺")
    diag_cap_base(g, 150, 480, W_MAIN, y_bot=0.0, y_top=800.0)
    bar_at(g, 700, 470, 740)
    vspan(g, 740, 700, 440, W_MAIN)
    bar_at(g, 440, 470, 740)
    g.diag(470, 440, 320, 60, W_MAIN)
    diag_cap_base(g, 880, 470, W_MAIN, y_bot=0.0, y_top=690.0)
    return g


def g_sho() -> Glyph:
    """処（5画）：夂（撇 + 横撇 + 捺）+ 几（撇 + 横折弯钩）。

    左夂压在左下（x 106..458），右几占右上（x 522..928），
    夂的捺与几的撇底部相距约 120，不互相粘连。
    """
    g = Glyph("uni51E6", advance=1000, unicode=0x51E6, note="処：夂 + 几")
    g.diag(470, 790, 270, 570, W_SEC)
    bar_at(g, 570, 270, 410, W_SEC)
    g.diag(410, 570, 150, 130, W_MAIN)
    g.diag(270, 570, 410, 230, W_MAIN)
    g.diag(600, 780, 530, 190, W_MAIN)
    bar_at(g, 780, 600, 880)
    vspan(g, 880, 780, 190, W_MAIN)
    g.diag(865, 200, 900, 280, W_THIN)
    return g


def g_kyuu_old() -> Glyph:
    """旧（5画）：竖 + 日。

    竖与日左竖净空 304-228 = 76 ≥ 60。
    """
    g = Glyph("uni65E7", advance=1000, unicode=0x65E7, note="旧：丨 + 日")
    vspan(g, 180, 820, 0, W_MAIN)
    kuchi_box(g, 350, 820, 652, 48, y_mid=350)
    return g


def g_tai() -> Glyph:
    """太（4画）：一 + 撇 + 捺 + 点。

    点落在撇捺之间（x 472..568），与横墨迹净空 652-406 = 246。
    """
    g = Glyph("uni592A", advance=1000, unicode=0x592A, note="太：大 + 点")
    bar_at(g, 700, 150, 850)
    diag_cap_base(g, 150, 500, W_MAIN, y_bot=0.0, y_top=700.0)
    diag_cap_base(g, 860, 500, W_MAIN, y_bot=0.0, y_top=700.0)
    g.dot(520, 350, 96, 112)
    return g


def g_bo() -> Glyph:
    """母（5画）：丿（左竖）+ 顶横 + 右竖 + 横折钩（中横）+ 底横 + 两点。

    母腔被中横分上下两格，两点各占一格；中横墨迹 332..428 与上点净空 58。
    """
    g = Glyph("uni6BCD", advance=1000, unicode=0x6BCD, note="母：框 + 中横出头 + 两点")
    diag_cap_base(g, 230, 310, W_MAIN, y_bot=0.0, y_top=700.0)
    bar_at(g, 700, 300, 760)
    vspan(g, 760, 700, 380, W_SEC)
    bar_at(g, 380, 260, 860)
    g.diag(840, 370, 785, 295, W_THIN)
    bar_at(g, 48, 260, 760)
    g.dot(430, 540, 92, 108)
    g.dot(600, 220, 92, 108)
    return g


def g_hi() -> Glyph:
    """火（4画）：点（左）+ 撇（右）+ 长撇 + 捺。

    长撇自顶心下行，捺自撇身中段冲出，构成火焰外张。
    """
    g = Glyph("uni706B", advance=1000, unicode=0x706B, note="火：两点 + 人")
    g.diag(195, 690, 270, 600, W_MAIN)
    g.diag(805, 690, 730, 600, W_MAIN)
    diag_cap_base(g, 150, 520, W_MAIN, y_bot=0.0, y_top=810.0)
    diag_cap_base(g, 860, 480, W_MAIN, y_bot=0.0, y_top=520.0)
    return g


def g_to() -> Glyph:
    """戸（4画）：点（短横）+ 尸（横折 + 横 + 撇）。

    尸身占 x 150..846；撇自横折的下横左端下行至基线。
    """
    g = Glyph("uni6238", advance=1000, unicode=0x6238, note="戸：短横 + 尸")
    bar_at(g, 758, 400, 640, W_THIN)
    bar_at(g, 640, 150, 800)
    vspan(g, 800, 640, 430, W_SEC)
    bar_at(g, 430, 150, 800)
    diag_cap_base(g, 110, 240, W_MAIN, y_bot=0.0, y_top=430.0)
    return g


def g_ou() -> Glyph:
    """央（5画）：冂（横 + 左竖 + 右竖）+ 横 + 撇 + 捺。

    框内净空 x 276..724、y 428..652；撇捺自框底横两分处下行。
    """
    g = Glyph("uni592E", advance=1000, unicode=0x592E, note="央：冂 + 大")
    bar_at(g, 700, 230, 770)
    vspan(g, 230, 700, 380, W_SEC)
    vspan(g, 770, 700, 380, W_SEC)
    bar_at(g, 380, 230, 770)
    diag_cap_base(g, 160, 480, W_MAIN, y_bot=0.0, y_top=380.0)
    diag_cap_base(g, 860, 520, W_MAIN, y_bot=0.0, y_top=380.0)
    return g


def g_gou() -> Glyph:
    """号（5画）：口 + 一 + 竖折弯钩。

    口占 x 234..766、y 434..800；口底与下方横净空 434-408 = 26 ≥ 24。
    钩的起笔压在底横墨迹内。
    """
    g = Glyph("uni53F7", advance=1000, unicode=0x53F7, note="号：口 + 丂")
    kuchi_box(g, 280, 720, 752, 482)
    bar_at(g, 360, 150, 850)
    vspan(g, 480, 360, 48, W_MAIN)
    bar_base(g, 480, 820)
    g.diag(800, 85, 845, 180, W_THIN)
    return g


def g_yu_u() -> Glyph:
    """右（5画）：一 + 撇（短）+ 口。

    撇只落到口的高度（约 y 440），与「石」的长撇区分开。
    """
    g = Glyph("uni53F3", advance=1000, unicode=0x53F3, note="右：一 + 短撇 + 口")
    bar_top(g, 180, 830)
    g.diag(330, 772, 150, 440, W_MAIN)
    kuchi_box(g, 380, 840, 400, 48)
    return g


def g_kai() -> Glyph:
    """介（4画）：人（撇 + 捺，停在半高）+ 撇（垂）+ 竖（垂）。

    两条垂笔分别吊在人字两腿内侧，垂笔间净空 264 ≥ 60。
    """
    g = Glyph("uni4ECB", advance=1000, unicode=0x4ECB, note="介：人 + 两垂")
    g.diag(520, 800, 230, 520, W_MAIN)
    g.diag(520, 800, 810, 520, W_MAIN)
    diag_cap_base(g, 300, 350, W_MAIN, y_bot=0.0, y_top=640.0)
    vspan(g, 660, 665, 0, W_MAIN)
    return g


def g_ben() -> Glyph:
    """弁（5画）：ム（撇折 + 点）+ 廾（一 + 撇 + 竖）。

    上ム占 x 292..578、下廾占 x 72..928；点与撇折横净空 68。
    """
    g = Glyph("uni5F01", advance=1000, unicode=0x5F01, note="弁：ム + 廾")
    g.diag(430, 790, 340, 570, W_SEC)
    bar_at(g, 570, 340, 530, W_SEC)
    g.dot(520, 740, 96, 112)
    bar_at(g, 430, 120, 880)
    diag_cap_base(g, 330, 390, W_MAIN, y_bot=0.0, y_top=430.0)
    vspan(g, 680, 430, 0, W_MAIN)
    return g


def g_yu() -> Glyph:
    """友（4画）：一 + 撇 + 横撇 + 捺。

    撇自横心下行至基线；横撇横画占 x 282..878、y 352..448。
    """
    g = Glyph("uni53CB", advance=1000, unicode=0x53CB, note="友：一 + 丿 + 又")
    bar_at(g, 700, 230, 850)
    diag_cap_base(g, 140, 470, W_MAIN, y_bot=0.0, y_top=700.0)
    bar_at(g, 400, 330, 830)
    g.diag(830, 400, 470, 30, W_MAIN)
    diag_cap_base(g, 880, 430, W_MAIN, y_bot=0.0, y_top=690.0)
    return g


def g_sa() -> Glyph:
    """左（5画）：一 + 撇 + 工（横 + 竖 + 横）。

    工占 x 442..948 右侧区，撇与工左端净空 142 ≥ 60。
    """
    g = Glyph("uni5DE6", advance=1000, unicode=0x5DE6, note="左：一 + 丿 + 工")
    bar_top(g, 180, 830)
    diag_cap_base(g, 130, 410, W_MAIN, y_bot=0.0, y_top=772.0)
    bar_at(g, 470, 490, 870)
    vspan(g, 680, 470, 48, W_SEC)
    bar_base(g, 490, 900)
    return g


def g_chichi() -> Glyph:
    """父（4画）：八（撇 + 点）+ 乂（撇 + 捺）。

    上八占 x 192..695、下乂占 x 102..918。
    """
    g = Glyph("uni7236", advance=1000, unicode=0x7236, note="父：八 + 乂")
    g.diag(430, 780, 240, 540, W_MAIN)
    g.dot(640, 640, 110, 130)
    diag_cap_base(g, 150, 520, W_MAIN, y_bot=0.0, y_top=520.0)
    diag_cap_base(g, 870, 430, W_MAIN, y_bot=0.0, y_top=520.0)
    return g


def g_mizu_2() -> Glyph:
    """未（5画）：木骨架（竖 + 上横短 + 下横长 + 撇 + 捺）。

    与「末」共用同一坐标，只交换上下横长短。
    """
    g = Glyph("uni672A", advance=1000, unicode=0x672A, note="未：下横长")
    vspan(g, 500, 820, 0, W_MAIN)
    bar_at(g, 700, 220, 780)
    bar_at(g, 470, 130, 870)
    diag_cap_base(g, 140, 500, W_MAIN, y_bot=0.0, y_top=470.0)
    diag_cap_base(g, 860, 500, W_MAIN, y_bot=0.0, y_top=470.0)
    return g


def g_bou() -> Glyph:
    """亡（3画）：点 + 一 + 竖折。

    点与横净空 700-648 = 52 ≥ 24。
    """
    g = Glyph("uni4EA1", advance=1000, unicode=0x4EA1, note="亡：亠 + 乚")
    g.dot(500, 760, 110, 120)
    bar_at(g, 600, 180, 820)
    vspan(g, 330, 600, 48, W_MAIN)
    bar_base(g, 330, 780)
    return g


def g_komi() -> Glyph:
    """込（4画）：入（撇 + 捺）+ 辶（点 + 折 + 底扫）。

    辶与「辺」共用 shinnyou()，坐标完全一致。
    """
    g = Glyph("uni8FBC", advance=1000, unicode=0x8FBC, note="込：入 + 辶")
    g.diag(680, 800, 420, 300, W_MAIN)
    g.diag(590, 500, 890, 310, W_MAIN)
    shinnyou(g)
    return g


def g_ou_kings() -> Glyph:
    """王（4画）：一 + 一 + 竖 + 一（三横一竖）。

    横距 652-466 = 186、466-96 = 370 ≥ 24。
    """
    g = Glyph("uni738B", advance=1000, unicode=0x738B, note="王：三横一竖")
    bar_at(g, 700, 180, 820)
    bar_at(g, 420, 250, 750, W_SEC)
    bar_base(g, 130, 870)
    vspan(g, 500, 700, 0, W_MAIN)
    return g


def g_kyuu_2() -> Glyph:
    """久（3画）：撇 + 横撇 + 捺。

    横撇横画占 x 232..708、y 512..608；捺自横撇的撇身中段冲出。
    """
    g = Glyph("uni4E45", advance=1000, unicode=0x4E45, note="久：丿 + 横撇 + 捺")
    g.diag(500, 785, 280, 560, W_MAIN)
    bar_at(g, 560, 280, 660)
    g.diag(660, 560, 280, 60, W_MAIN)
    diag_cap_base(g, 850, 520, W_MAIN, y_bot=0.0, y_top=380.0)
    return g


# --------------------------------------------------------------------------
# 装配
# --------------------------------------------------------------------------
def build() -> list[Glyph]:
    return [
        g_bi(),
        g_fu(),
        g_shu(),
        g_jing(),
        g_shitsu(),
        g_man(),
        g_heritsu(),
        g_shi(),
        g_kyo(),
        g_sitsu(),
        g_kaku(),
        g_matsu(),
        g_mizu(),
        g_shin(),
        g_ko(),
        g_shi_ji(),
        g_ten(),
        g_shi_solo(),
        g_maru(),
        g_ta(),
        g_kyuu(),
        g_sho(),
        g_kyuu_old(),
        g_tai(),
        g_bo(),
        g_hi(),
        g_to(),
        g_ou(),
        g_gou(),
        g_yu_u(),
        g_kai(),
        g_ben(),
        g_yu(),
        g_sa(),
        g_chichi(),
        g_mizu_2(),
        g_bou(),
        g_komi(),
        g_ou_kings(),
        g_kyuu_2(),
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-s1-003.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
