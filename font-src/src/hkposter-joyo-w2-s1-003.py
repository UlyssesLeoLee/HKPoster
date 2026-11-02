"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s1-003。

本批 15 字，笔画范围 3–5，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
============
* 字面框：x 60..940 / y 0..820，advance = 1000，与 zh-HK 繁体 master 完全一致，
  中英日混排时三套字共享同一组竖位与基线。
* 权重档（与 zh-HK 同一档）：主 96 / 次 92 / 细 84 / 点 84–96。
  - 竖画取 96（骨架），横画取 92（次），点与短撇取 84。
  - 笔画少的字（乞 3 画、巾 3 画、斤 4 画、匂 4 画、勾 4 画）整体提重到 96，
    不显轻；笔画多的字在拥挤处把内框横画降到 84–88。
* 对齐语义：横画一律走 bar_top（墨迹上缘 = 820）、bar_base（墨迹下缘 = 0）
  或显式中心线；竖画一律走 vline（端点即墨迹端点），不拍脑袋给坐标。
* 部件复用（GLY-004）：批内 勹（匂 / 勾）、㔾（厄 / 氾）、氵（氾）走同一套
  拆笔与相对坐标（draw_men / draw_he / draw_sanzui），只做位置与大小的光学校正。
* 批内墨量平衡（GLY-001）：check_glyphs 按「本 master 同笔画档中位数 ±35%」预警，
  所以外形封闭的字（囚 / 凸 / 凹 / 且 / 旦）把外框收进 8–12%，
  笔画稀疏的字（斤 / 斥 / 匂 / 勾 / 氾）把次级笔画提重到 96，
  使 4–6 画档的墨量率收在 0.17–0.37 的窄带内。
* 字体本体与海报特效分离：本 recipe 只产出字形轮廓，不含描边 / 霓虹 / 旧化。

字形依据
========
* 凸 = 竖、横、竖、横折折折、横；凹 = 竖、横折折、竖、横折、横
  —— 笔顺互为镜像，故本批把 凹 做成 凸 的上下镜像（宽顶 + 窄底足）。
* 𠮟 U+20B9F = ⿰口七（口 3 画 + 七 2 画，共 5 画，读 chì，同「叱」），
  不是「母」形；按左右结构画，左「口」右「七」。
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


# --------------------------------------------------------------- 对齐辅助
def bar_top(g: Glyph, x1: float, x2: float, w: int = W_SEC) -> None:
    """顶对齐横画：墨迹上缘贴 820（中心线上移半个笔画宽）。"""
    g.hbar(x1, x2, TOP - w / 2, weight=w)


def bar_base(g: Glyph, x1: float, x2: float, w: int = W_SEC) -> None:
    """底对齐横画：墨迹下缘贴 0（中心线下移半个笔画宽）。"""
    g.hbar(x1, x2, BASE + w / 2, weight=w)


def vline(g: Glyph, x: float, y_top: float, y_bot: float, w: int = W_MAIN) -> None:
    """竖画：中心线在 x，端点即墨迹端点（约定 y_top > y_bot）。"""
    g.vbar(x, y_top, y_bot, weight=w)


# --------------------------------------------------------------- 复用部件
def draw_men(g: Glyph, x_left: float, x_right: float, y_top: float,
             y_bot: float, w: int = W_SEC) -> None:
    """勹（匂 / 勾 共用）：ノ + ㇆（横折钩）。

    局部坐标（相对 x_left / y_top）：
      ノ   由 (x_left+250, y_top-40) 撇到 (x_left, y_top-290)；
      ㇆   横画自 x_left+70 起（与ノ相交）横到 x_right，折竖落到 y_bot，
           末端向左上挑 70 / 65 的小钩。
    """
    g.diag(x_left + 250, y_top - 40, x_left, y_top - 290, weight=w)
    g.hbar(x_left + 70, x_right, y_top - 140, weight=w)
    g.vbar(x_right, y_top - 140, y_bot, weight=w)
    g.diag(x_right, y_bot, x_right - 70, y_bot + 65, weight=W_DOT)


def draw_he(g: Glyph, x1: float, x2: float, x3: float, y_top: float,
            y_bot: float, w: int = W_SEC) -> None:
    """㔾（厄 / 氾 共用）：横折 + 竖弯钩，方螺线。

    局部坐标：
      横折   上横 x1..x2 @ y_top + 右侧短竖落到 y_mid；
      竖弯钩 左侧长竖落到 y_bot + 底横 x1..x3 @ y_bot + 右上小钩。
    y_mid 取 0.40 高，使折竖与钩之间留出可读的白口。
    """
    y_mid = y_bot + (y_top - y_bot) * 0.40
    g.hbar(x1, x2, y_top, weight=w)
    g.vbar(x2, y_top, y_mid, weight=w)
    g.vbar(x1, y_top, y_bot, weight=w)
    g.hbar(x1, x3, y_bot, weight=w)
    g.diag(x3, y_bot, x3 + 60, y_bot + 60, weight=W_DOT)


def draw_sanzui(g: Glyph, w: int = W_DOT) -> None:
    """氵（氾 用）：丶 丶 提，固定落在 x 60..300 的左栏。"""
    g.diag(120, 700, 205, 765, weight=w)
    g.diag(105, 470, 180, 530, weight=w)
    g.diag(85, 215, 265, 320, weight=W_SEC)


# --------------------------------------------------------------- 单字实现
def _g_yu() -> Glyph:
    """囚 U+56DA —— 囗（3 画）+ 人（2 画），共 5 画。

    部件分区：外框 囗 占 x 90..890 / y 30..790（收进 8%，给内白留呼吸）；
    内「人」占 x 259..727 / y 172..634。
    笔画清单：
      1 丨   外框左竖   中心线 x=138，y 790→30
      2 一   外框顶横   x 138..842，中心线 y=742
      3 丨   外框右竖   中心线 x=842，y 790→30
      4 一   外框底横   x 138..842，中心线 y=78
      5 人   内撇 (540,610)→(300,200)；内捺 (480,475)→(690,200)
    """
    g = Glyph("uni56DA", advance=1000, unicode=0x56DA, note="囚：5 画：囗(3) + 人(2)")
    vline(g, 138, 790, 30, W_MAIN)
    g.hbar(138, 842, 742, weight=W_MAIN)
    vline(g, 842, 790, 30, W_MAIN)
    g.hbar(138, 842, 78, weight=W_MAIN)
    g.diag(540, 610, 300, 200, weight=W_SEC)
    g.diag(480, 475, 690, 200, weight=W_SEC)
    return g


def _g_e() -> Glyph:
    """厄 U+5384 —— 厂（2 画）+ 㔾（2 画），共 4 画。

    部件分区：厂占 x 73..297 / y 41..820；㔾占 x 392..930 / y 202..648。
    笔画清单：
      1 一   厂顶横     x 180..920，顶对齐（中心线 y=772）
      2 丿   厂撇       (250,772)→(120,50)
      3 ㇆   㔾 横折    上横 x 440..790 @600 + 右竖 x=790 落到 y=390
      4 乚   㔾 竖弯钩  左竖 x=440 落到 250 + 底横 x 440..840 @250 + 右上钩
    """
    g = Glyph("uni5384", advance=1000, unicode=0x5384, note="厄：4 画：厂(2) + 㔾(2)")
    bar_top(g, 180, 920, W_MAIN)
    g.diag(250, 772, 120, 50, weight=W_MAIN)
    draw_he(g, 440, 790, 840, 600, 250, W_MAIN)
    return g


def _g_tsu() -> Glyph:
    """凸 U+51F8 —— 底座方块 + 顶部方块（5 画）。

    笔顺：竖、横、竖、横折折折、横（见模块 docstring）。
    部件分区：底座 x 60..940 / y 0..478；顶部方块 x 302..694 / y 432..820。
    笔画清单：
      1 一   底横       x 60..940，中心线 y=48
      2 丨   底座左竖   x=108，y 432→0
      3 丨   底座右竖   x=892，y 432→0
      4 一   底座顶左段 x 108..348，中心线 y=432
      5 一   底座顶右段 x 652..892，中心线 y=432
      6 丨   方块左竖   x=348，y 820→432
      7 丨   方块右竖   x=652，y 820→432
      8 一   方块顶横   x 302..694，顶对齐
    """
    g = Glyph("uni51F8", advance=1000, unicode=0x51F8, note="凸：5 画：底座 + 顶块")
    bar_base(g, 60, 940, W_MAIN)
    vline(g, 108, 432, BASE, W_MAIN)
    vline(g, 892, 432, BASE, W_MAIN)
    g.hbar(108, 348, 432, weight=W_SEC)
    g.hbar(652, 892, 432, weight=W_SEC)
    vline(g, 348, TOP, 432, W_SEC)
    vline(g, 652, TOP, 432, W_SEC)
    bar_top(g, 302, 694, W_MAIN)
    return g


def _g_omi() -> Glyph:
    """凹 U+51F9 —— 凸 的上下镜像：宽顶方块 + 窄底足（5 画）。

    笔顺：竖、横折折、竖、横折、横 —— 与「凸」互为镜像，故镜像建模。
    部件分区：顶部方块 x 60..940 / y 388..820；底部方足 x 302..694 / y 0..388。
    笔画清单：
      1 一   顶横       x 60..940，顶对齐
      2 丨   外左壁     x=108，y 388→820
      3 丨   外右壁     x=892，y 388→820
      4 一   肩左横     x 108..348，中心线 y=388
      5 一   肩右横     x 652..892，中心线 y=388
      6 丨   底足左竖   x=348，y 388→0
      7 丨   底足右竖   x=652，y 388→0
      8 一   底足底横   x 302..694，底对齐
    """
    g = Glyph("uni51F9", advance=1000, unicode=0x51F9, note="凹：5 画：宽顶块 + 窄底足")
    bar_top(g, 60, 940, W_MAIN)
    vline(g, 108, 388, TOP, W_MAIN)
    vline(g, 892, 388, TOP, W_MAIN)
    g.hbar(108, 348, 388, weight=W_SEC)
    g.hbar(652, 892, 388, weight=W_SEC)
    vline(g, 348, 388, BASE, W_SEC)
    vline(g, 652, 388, BASE, W_SEC)
    bar_base(g, 302, 694, W_MAIN)
    return g


def _g_nio() -> Glyph:
    """匂 U+5302 —— 勹（2 画）+ 匕（2 画），共 4 画。

    笔画少 → 勹 与匕 都提到 96。
    部件分区：勹占 x 96..908 / y 134..814；匕占 x 304..702 / y 167..600。
    笔画清单：
      1 ノ   勹 撇       (380,780)→(130,530)
      2 ㇆   勹 横折钩   横 x 200..860 @680 + 右竖 x=860 落到 165 + 左上钩
      3 丿   匕 撇       (620,520)→(330,330)
      4 乚   匕 竖弯钩   竖 x=400 由 600 落到 215 + 底横 x 400..660 @215 + 钩
    """
    g = Glyph("uni5302", advance=1000, unicode=0x5302, note="匂：4 画：勹(2) + 匕(2)")
    draw_men(g, 130, 860, 820, 165, W_MAIN)
    g.diag(620, 520, 330, 330, weight=W_MAIN)
    vline(g, 400, 600, 215, W_MAIN)
    g.hbar(400, 660, 215, weight=W_MAIN)
    vline(g, 660, 290, 215, W_DOT)
    return g


def _g_seki() -> Glyph:
    """斥 U+65A5 —— 斤（4 画）+ 丶（1 画），共 5 画。

    部件分区：斤占 x 158..880 / y 41..528；丶占 x 729..871 / y 647..783。
    笔画清单：
      1 丿   上撇       (540,760)→(275,635)
      2 丿   左长撇     (300,655)→(195,38)
      3 一   横         x 235..870，中心线 y=480
      4 丨   竖         x=615，y 490→30
      5 丶   点         (755,750)→(845,680)
    """
    g = Glyph("uni65A5", advance=1000, unicode=0x65A5, note="斥：5 画：斤(4) + 丶(1)")
    g.diag(540, 760, 275, 635, weight=W_SEC)
    g.diag(300, 655, 195, 38, weight=W_MAIN)
    g.hbar(250, 870, 480, weight=W_MAIN)
    vline(g, 615, 480, 50, W_MAIN)
    g.diag(755, 750, 845, 680, weight=W_DOT)
    return g


def _g_ki() -> Glyph:
    """乞 U+4E5E —— 𠂉（2 画）+ 乙（1 画），共 3 画。

    笔画少 → 整体提重：丿 与横用 96，乙 的斜段用 92。
    部件分区：上部件 x 277..760 / y 592..812；乙 段 x 390..770 / y 24..663。
    笔画清单：
      1 丿   撇         (545,770)→(310,630)
      2 一   横         x 280..760，中心线 y=640
      3 乙   横折弯钩   斜段 (730,640)→(430,120) + 底横 x 420..690 @70 + 右上钩
    """
    g = Glyph("uni4E5E", advance=1000, unicode=0x4E5E, note="乞：3 画：𠂉(2) + 乙(1)")
    g.diag(545, 770, 310, 630, weight=W_MAIN)
    g.hbar(280, 760, 640, weight=W_MAIN)
    g.diag(730, 640, 430, 120, weight=W_SEC)
    g.hbar(420, 690, 70, weight=W_SEC)
    vline(g, 690, 160, 70, W_DOT)
    return g


def _g_katsu() -> Glyph:
    """且 U+4E14 —— 目形窄框 + 底横外伸（5 画）。

    窄字：框宽 400（45% 字面宽），底横左右各伸 110。
    部件分区：窄框 x 300..700 / y 0..820；底横 x 190..810。
    笔画清单：
      1 丨   左竖       x=348，y 820→48
      2 𠃍   顶横+右竖  顶横 x 348..652 顶对齐 + 右竖 x=652，y 820→48
      3 一   内横一     x 348..652，中心线 y=520，密排处减重到 84
      4 一   内横二     x 348..652，中心线 y=300，减重到 84
      5 一   底横       x 190..810，底对齐
    """
    g = Glyph("uni4E14", advance=1000, unicode=0x4E14, note="且：5 画：目形框 + 外伸底横")
    vline(g, 348, TOP, 48, W_MAIN)
    bar_top(g, 348, 652, W_MAIN)
    vline(g, 652, TOP, 48, W_MAIN)
    g.hbar(348, 652, 520, weight=W_THIN)
    g.hbar(348, 652, 300, weight=W_THIN)
    bar_base(g, 190, 810, W_MAIN)
    return g


def _g_kin() -> Glyph:
    """巾 U+5DFE —— 冂 + 中竖（3 画）。

    笔画少 → 整体提重：顶横 96、两侧竖 92、中竖 96。
    部件分区：横 x 140..860；两侧竖 x 140..232 / 768..860；中竖 x 452..548。
    笔画清单：
      1 𠃍   顶横+右竖  顶横 x 140..860 顶对齐 + 右竖 x=814，y 780→200
      2 丨   左竖       x=186，y 780→200
      3 丨   中竖       x=500，y 780→55（比两侧竖低，示中竖出头）
    """
    g = Glyph("uni5DFE", advance=1000, unicode=0x5DFE, note="巾：3 画：冂 + 中竖")
    bar_top(g, 140, 860, W_MAIN)
    vline(g, 186, 780, 200, W_SEC)
    vline(g, 814, 780, 200, W_SEC)
    vline(g, 500, 780, 55, W_MAIN)
    return g


def _g_kin_axe() -> Glyph:
    """斤 U+65A4 —— 4 画（上撇 + 左长撇 + 横 + 竖）。

    笔画少 → 整体 96；与「斥」同构，斥 = 斤 + 丶。
    部件分区：撇列 x 148..560；横 x 235..890 / y 432..528；竖 x 572..668。
    笔画清单：
      1 丿   上撇       (540,760)→(275,635)
      2 丿   左长撇     (300,655)→(195,38)
      3 一   横         x 235..890，中心线 y=480
      4 丨   竖         x=620，y 490→30
    """
    g = Glyph("uni65A4", advance=1000, unicode=0x65A4, note="斤：4 画：丿 + 丿 + 一 + 丨")
    g.diag(540, 760, 275, 635, weight=W_MAIN)
    g.diag(300, 655, 195, 38, weight=W_MAIN)
    g.hbar(235, 890, 480, weight=W_MAIN)
    vline(g, 620, 490, 30, W_MAIN)
    return g


def _g_magari() -> Glyph:
    """勾 U+52FE —— 勹（2 画）+ 厶（2 画），共 4 画。

    笔画少 → 勹 与 厶 都提到 96。
    部件分区：勹占 x 96..908 / y 119..814；厶占 x 348..705 / y 212..584。
    笔画清单：
      1 ノ   勹 撇       (380,780)→(130,530)
      2 ㇆   勹 横折钩   横 x 200..860 @680 + 右竖 x=860 落到 150 + 左上钩
      3 ㇜   厶 撇折     斜段 (560,560)→(390,260) + 底横 x 390..640 @260
      4 丶   厶 点       (610,390)→(675,455)
    """
    g = Glyph("uni52FE", advance=1000, unicode=0x52FE, note="勾：4 画：勹(2) + 厶(2)")
    draw_men(g, 130, 860, 820, 150, W_MAIN)
    g.diag(560, 560, 390, 260, weight=W_MAIN)
    g.hbar(390, 640, 260, weight=W_MAIN)
    g.diag(610, 390, 675, 455, weight=W_DOT)
    return g


def _g_tan() -> Glyph:
    """旦 U+65E6 —— 日 + 下横（5 画）。

    部件分区：日 x 280..720 / y 202..820；下横 x 140..860 / y 0..96。
    笔画清单：
      1 丨   日左竖      x=328，y 820→250
      2 𠃍   日顶横+右竖 顶横 x 328..672 顶对齐 + 右竖 x=672，y 820→250
      3 一   日中横      x 328..672，中心线 y=540（减重到 88）
      4 一   日底横      x 280..720，中心线 y=250
      5 一   下横        x 140..860，底对齐
    """
    g = Glyph("uni65E6", advance=1000, unicode=0x65E6, note="旦：5 画：日 + 下横")
    vline(g, 328, TOP, 250, W_MAIN)
    bar_top(g, 328, 672, W_MAIN)
    vline(g, 672, TOP, 250, W_MAIN)
    g.hbar(328, 672, 540, weight=88)
    g.hbar(280, 720, 250, weight=W_MAIN)
    bar_base(g, 140, 860, W_MAIN)
    return g


def _g_han() -> Glyph:
    """氾 U+6C3E —— 氵（3 画）+ 㔾（2 画），共 5 画。

    部件分区：氵占 x 64..286；㔾占 x 382..930 / y 42..688。
    笔画清单：
      1 丶   氵 上点     (120,700)→(205,765)
      2 丶   氵 中点     (105,470)→(180,530)
      3 提   氵 提       (85,215)→(265,320)
      4 ㇆   㔾 横折     上横 x 430..790 @640 + 右竖 x=790 落到 310
      5 乚   㔾 竖弯钩   左竖 x=430 落到 90 + 底横 x 430..840 @90 + 右上钩
    """
    g = Glyph("uni6C3E", advance=1000, unicode=0x6C3E, note="氾：5 画：氵(3) + 㔾(2)")
    draw_sanzui(g, W_DOT)
    draw_he(g, 430, 790, 840, 640, 90, W_MAIN)
    return g


def _g_hei() -> Glyph:
    """丙 U+4E19 —— 一 + 冂 + 人（5 画）。

    部件分区：顶横 x 60..940；两壁 x 94..186 / 814..906；内「人」x 288..736。
    笔画清单：
      1 一   顶横       x 60..940，顶对齐
      2 丨   左壁       x=140，y 780→60
      3 𠃍   右壁       x=860，y 780→60（与顶横相交）
      4 丿   内撇       (520,620)→(330,175)
      5 丶   内捺       (465,470)→(700,175)
    """
    g = Glyph("uni4E19", advance=1000, unicode=0x4E19, note="丙：5 画：一 + 冂 + 人")
    bar_top(g, 60, 940, W_MAIN)
    vline(g, 140, 780, 60, W_SEC)
    vline(g, 860, 780, 60, W_SEC)
    g.diag(520, 620, 330, 175, weight=W_SEC)
    g.diag(465, 470, 700, 175, weight=W_SEC)
    return g


def _g_bo() -> Glyph:
    """𠮟 U+20B9F —— ⿰口七，左右结构，共 5 画（读 chì，同「叱」）。

    笔顺 25115：丨（口左竖）、𠃍（口横折）、一（口底横）、一（七横）、乚（七竖弯钩）。
    部件分区：口 x 60..370 / y 300..700；七 x 440..912 / y 94..790。
    笔画清单：
      1 丨   口左竖     x=106，y 658→342
      2 𠃍   口顶横     x 60..370，中心线 y=658
      3 丨   口右竖     x=324，y 658→342
      4 一   口底横     x 60..370，中心线 y=342
      5 一   七横       x 440..900，中心线 y=520
      6 乚   七竖弯钩   竖 x=610 由 780 落到 140 + 底横 x 610..870 @140 + 钩
    """
    g = Glyph("uni20B9F", advance=1000, unicode=0x20B9F, note="𠮟：5 画：⿰口七")
    vline(g, 106, 658, 342, W_SEC)
    g.hbar(60, 370, 658, weight=W_SEC)
    vline(g, 324, 658, 342, W_SEC)
    g.hbar(60, 370, 342, weight=W_SEC)
    g.hbar(440, 900, 520, weight=W_MAIN)
    vline(g, 610, 780, 140, W_MAIN)
    g.hbar(610, 870, 140, weight=W_MAIN)
    vline(g, 870, 225, 140, W_DOT)
    return g


# --------------------------------------------------------------- 装配
def build() -> list[Glyph]:
    return [
        _g_yu(),       # 囚
        _g_e(),        # 厄
        _g_tsu(),      # 凸
        _g_omi(),      # 凹
        _g_nio(),      # 匂
        _g_seki(),     # 斥
        _g_ki(),       # 乞
        _g_katsu(),    # 且
        _g_kin(),      # 巾
        _g_kin_axe(),  # 斤
        _g_magari(),   # 勾
        _g_tan(),      # 旦
        _g_han(),      # 氾
        _g_hei(),      # 丙
        _g_bo(),       # 𠮟
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s1-003.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] wrote {target_ufo()}")
