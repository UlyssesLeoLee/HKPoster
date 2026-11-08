"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s3-014。

本批 24 字，笔画范围 10–13，取自 2010 年文化厅《常用漢字表》：
閉 跡 貢 鹿 弱 賃 紹 飲 貴 埼 焦 雇 浦 替 預 焼 称 納 章 紛 貸 慎 控 握。

整体设计取舍
------------
* 字面框 x 60..940、y 0..820，advance 1000，与繁体汉字完全一致。
* 笔画权重四档：主 96（横/竖/撇捺的主笔）、次 92、细 84（密排处的横画与细竖）、
  点 84–96。
* **海报端点**：横竖撇捺一律平切硬边（无钩、无圆头、无渐变收笔）；
  点/短撇用斜切平行四边形，slant 分档严格取 26 / 14 / 0 / -14：
  - 短撇（氵的上点、宀的点、乛的左上）→ 26
  - 左下点（丷右、忄的左点、糸的左点）→ +14
  - 竖点（亠的点、宀的点、隹的头撇）→ 0
  - 右下点（丶：厶的点、弋的点、冫的上点、灬）→ -14
* **笔画角度**：所有斜笔中心线斜率只用 0.5 / 1 / 2 三档（≈27° / 45° / 63°），
  对应标准的捺（0.5）、短撇与点（1）、长撇（2）；不造新角度。
* **腔体约束（硬门禁）**：口/日/目/田 型方框的腔高一律 ≥ 24 单位，
  公式化地留足：口框高 ≥ 2w+24；日（含曰）框高 ≥ 3w+48；目框高 ≥ 4w+72。
  框高不够就缩框顶横或降横画档位，不靠目测。
  相邻横画白口 ≥ 24（本批统一取 28–30），竖画间距 ≥ 60。
* **同族观感（GLY-004）**：糹（糹偏旁）、貝（目 + 八）、口/日/目 等部件
  全部走同一套 helper 坐标，三个含糹的字（紹 納 紛）与四个含貝的字
  （貢 賃 貴 貸）形状完全一致，只做位置校正。
* 骨架取自参照字体 M PLUS 1p Black（SIL OFL 1.1）的**结构与比例**，
  不描其轮廓；本字体的字重与方切端点为自有设计。
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


# ---------------------------------------------------------------- 部件 helper

def _kuchi(g, x1, x2, yb, yt, w=W_THIN):
    """口：墨迹外框 x1..x2 / yb..yt。腔高 = (yt-yb) - 2w，调用方保证 ≥ 24。"""
    g.hbar(x1, x2, yt - w / 2.0, weight=w)
    g.hbar(x1, x2, yb + w / 2.0, weight=w)
    g.vbar(x1 + w / 2.0, yb, yt, weight=w)
    g.vbar(x2 - w / 2.0, yb, yt, weight=w)


def _hi(g, x1, x2, yb, yt, w=W_THIN, wm=W_THIN):
    """日 / 曰：外框 + 一中横。两腔各 (H-2w-wm)/2，调用方保证 ≥ 24。"""
    _kuchi(g, x1, x2, yb, yt, w)
    g.hbar(x1, x2, (yb + yt) / 2.0, weight=wm)


def _me(g, x1, x2, yb, yt, w=W_THIN, wm=W_THIN):
    """目：外框 + 两中横。三腔各 (H-2w-2wm)/3，调用方保证 ≥ 24。"""
    _kuchi(g, x1, x2, yb, yt, w)
    inner_top = yt - w
    inner_bot = yb + w
    cav = (inner_top - inner_bot - 2 * wm) / 3.0
    m1 = inner_top - cav - wm / 2.0
    m2 = m1 - (cav + wm)
    g.hbar(x1, x2, m1, weight=wm)
    g.hbar(x1, x2, m2, weight=wm)


def _sikon(g, ox=60):
    """糹（左部）：幺（两撇折 + 一点）+ 小（竖 + 两点）。ox = 区域左边界。

    撇折斜率 1（45°）；两横 y=680 / 568，墨迹 638..722 / 526..610，白口 28 ≥ 24。
    """
    # 幺：两撇折（撇折 2 起自撇折 1 横的右端）
    g.diag(ox + 185, 792, ox + 73, 680, weight=W_THIN)
    g.hbar(ox + 73, ox + 173, 680, weight=W_THIN)
    g.diag(ox + 173, 680, ox + 61, 568, weight=W_THIN)
    g.hbar(ox + 61, ox + 161, 568, weight=W_THIN)
    g.dot(ox + 165, 580, w=72, h=96, slant=-14)
    # 小
    g.vbar(ox + 145, 330, 545, weight=W_THIN)
    g.dot(ox + 35, 430, w=72, h=100, slant=14)
    g.dot(ox + 250, 430, w=72, h=100, slant=-14)


def _jo(g, ox=60, oy=700, y_bot=330, y_left_top=790, y_mid_top=820,
        y_tick=780, y_pie=670):
    """隹：丿 + 左竖 + 中竖 + 四横（横贯穿全宽，间距 126 → 白口 30）。

    oy = 顶横中心线；焦与雇共用此拆法，雇只是整体下移 40 并加长竖画。
    """
    g.diag(ox + 240, y_tick, ox + 185, y_pie, weight=W_THIN)
    g.vbar(ox + 80, y_bot, y_left_top, weight=W_MAIN)
    g.vbar(ox + 460, y_bot, y_mid_top, weight=W_MAIN)
    g.hbar(ox, ox + 880, oy, weight=W_MAIN)
    g.hbar(ox, ox + 880, oy - 126, weight=W_MAIN)
    g.hbar(ox, ox + 880, oy - 252, weight=W_MAIN)
    g.hbar(ox, ox + 880, oy - 378, weight=W_MAIN)


# -------------------------------------------------------------------- 字形

def _g_bi() -> Glyph:
    """閉 U+9589（11画）＝ 門 + 才。

    門：左右两片「日」形门板 + 外侧长竖。
      外竖 x=108 / 892（墨迹 60..156 / 844..940），顶横 y=712（墨迹 664..760），
      中横 y=440（墨迹 392..488），内竖 x=420 / 580（墨迹 372..468 / 532..628）。
      竖距：216 / 64 / 216，板内横白口 176。
    才：横 y=300（墨迹 252..348），竖 x=500（130..260），撇 (480,300)→(330,150)。
    """
    g = Glyph("uni9589", advance=1000, unicode=0x9589, note="閉：門 + 才")
    g.vbar(108, 40, 760, weight=W_MAIN)
    g.vbar(892, 40, 760, weight=W_MAIN)
    g.hbar(108, 420, 712, weight=W_MAIN)
    g.hbar(108, 420, 440, weight=W_MAIN)
    g.vbar(420, 440, 760, weight=W_MAIN)
    g.hbar(580, 892, 712, weight=W_MAIN)
    g.hbar(580, 892, 440, weight=W_MAIN)
    g.vbar(580, 440, 760, weight=W_MAIN)
    g.hbar(250, 720, 300, weight=W_MAIN)
    g.vbar(500, 130, 260, weight=W_MAIN)
    g.diag(480, 300, 330, 150, weight=W_SEC)
    return g


def _g_ato() -> Glyph:
    """跡 U+8DE1（13画）＝ 足 + 亦。

    足：口 x 60..300（墨迹 620..820，腔 32）+ 龰（竖 x=180、右侧短横 y=300、
      撇 (170,300)→(95,150) 斜率 2、捺 (190,290)→(320,160) 斜率 1）。
    亦：竖点 (620,760)、横 y=680（墨迹 632..728）、撇 (480,668)→(370,558)、
      双竖 x=560 / 720（墨迹 512..608 / 672..768）、右下点 (830,590)。
    """
    g = Glyph("uni8DE1", advance=1000, unicode=0x8DE1, note="跡：足 + 亦")
    _kuchi(g, 60, 300, 620, 820, W_THIN)
    g.vbar(180, 300, 640, weight=W_SEC)
    g.hbar(180, 330, 300, weight=W_THIN)
    g.diag(170, 300, 95, 150, weight=W_THIN)
    g.diag(190, 290, 320, 160, weight=W_THIN)
    g.dot(620, 760, w=92, h=86, slant=0)
    g.hbar(350, 930, 680, weight=W_MAIN)
    g.diag(480, 668, 370, 558, weight=W_THIN)
    g.vbar(560, 330, 680, weight=W_MAIN)
    g.vbar(720, 330, 680, weight=W_MAIN)
    g.dot(830, 590, w=88, h=106, slant=-14)
    return g


def _g_kou() -> Glyph:
    """貢 U+8CA2（10画）＝ 工 + 貝。

    工：上横 y=772（墨迹 724..820），竖 x=500（690..772），下横 y=648（600..696）。
    貝：目 x 230..770，墨迹 156..576（腔 28）；
      八：撇 (350,165)→(275,25)、捺 (650,165)→(725,25)，均斜率 2。
    """
    g = Glyph("uni8CA2", advance=1000, unicode=0x8CA2, note="貢：工 + 貝")
    g.hbar(210, 790, 772, weight=W_MAIN)
    g.vbar(500, 690, 772, weight=W_MAIN)
    g.hbar(150, 850, 648, weight=W_MAIN)
    _me(g, 230, 770, 156, 576, W_THIN)
    g.diag(350, 165, 275, 25, weight=W_SEC)
    g.diag(650, 165, 725, 25, weight=W_SEC)
    return g


def _g_roku() -> Glyph:
    """鹿 U+9E7F（11画）＝ 广 + 中部罒格 + 比。

    顶部竖点 x=490（756..820）、顶横 y=712（墨迹 664..760，全宽 140..900）；
    广的撇：竖 x=200（300..712）+ 撇尾 (200,300)→(110,120)；
    中部：两横 y=470（428..512）/ 270（228..312），三竖 x=420 / 620 / 860；
    比：两竖 x=520 / 820，脚向左伸 y=150（墨迹 104..196）。
    """
    g = Glyph("uni9E7F", advance=1000, unicode=0x9E7F, note="鹿：广 + 罒 + 比")
    g.vbar(490, 756, 820, weight=W_MAIN)
    g.hbar(140, 900, 712, weight=W_MAIN)
    g.vbar(200, 300, 712, weight=W_MAIN)
    g.diag(200, 300, 110, 120, weight=W_MAIN)
    g.hbar(200, 860, 470, weight=W_THIN)
    g.hbar(200, 860, 270, weight=W_THIN)
    g.vbar(420, 270, 712, weight=W_THIN)
    g.vbar(620, 270, 712, weight=W_THIN)
    g.vbar(860, 270, 760, weight=W_THIN)
    g.vbar(520, 90, 240, weight=W_SEC)
    g.hbar(200, 520, 150, weight=W_SEC)
    g.vbar(820, 90, 240, weight=W_SEC)
    g.hbar(560, 820, 150, weight=W_SEC)
    return g


def _g_kyo() -> Glyph:
    """弱 U+5F31（10画）＝ 弓 + 冫 + 弓。

    左弓 x 60..380、右弓 x 540..940（中间留槽给冫）；
    弓形：顶横 y=740 → 右上竖 → 中横 y=600 → 左竖 → 下横 y=460 → 末竖到底；
    相邻横白口 44。
    冫：两点 (460,530) / (460,390)，斜切 -14。
    """
    g = Glyph("uni5F31", advance=1000, unicode=0x5F31, note="弱：弓 + 冫 + 弓")
    # 左弓
    g.hbar(60, 380, 740, weight=W_MAIN)
    g.vbar(380, 600, 740, weight=W_MAIN)
    g.hbar(60, 380, 600, weight=W_MAIN)
    g.vbar(60, 460, 600, weight=W_MAIN)
    g.hbar(60, 380, 460, weight=W_MAIN)
    g.vbar(380, 60, 460, weight=W_MAIN)
    # 右弓
    g.hbar(540, 940, 740, weight=W_MAIN)
    g.vbar(940, 600, 740, weight=W_MAIN)
    g.hbar(540, 940, 600, weight=W_MAIN)
    g.vbar(540, 460, 600, weight=W_MAIN)
    g.hbar(540, 940, 460, weight=W_MAIN)
    g.vbar(940, 60, 460, weight=W_MAIN)
    # 冫
    g.dot(460, 530, w=72, h=100, slant=-14)
    g.dot(460, 390, w=72, h=100, slant=-14)
    return g


def _g_chin() -> Glyph:
    """賃 U+8CC3（13画）＝ 任 + 貝。

    亻：撇 (200,810)→(90,650)、竖 x=150（450..700）。
    壬：短撇 (420,800)→(350,730)、上横 y=730（682..778）、竖 x=520（570..730）、
      下横 y=570（522..618）。
    貝：目 x 240..760，墨迹 70..490（腔 28）；八：撇 (360,75)→(300,15)、
      捺 (640,75)→(700,15)。
    """
    g = Glyph("uni8CC3", advance=1000, unicode=0x8CC3, note="賃：任 + 貝")
    g.diag(200, 810, 90, 650, weight=W_MAIN)
    g.vbar(150, 450, 700, weight=W_MAIN)
    g.diag(420, 800, 350, 730, weight=W_THIN)
    g.hbar(270, 760, 730, weight=W_MAIN)
    g.vbar(520, 570, 730, weight=W_MAIN)
    g.hbar(250, 790, 570, weight=W_MAIN)
    _me(g, 240, 760, 70, 490, W_THIN)
    g.diag(360, 75, 300, 15, weight=W_SEC)
    g.diag(640, 75, 700, 15, weight=W_SEC)
    return g


def _g_sho() -> Glyph:
    """紹 U+7D39（11画）＝ 糹 + 召。

    糹：见 _sikon（x 60..346）。
    召：刀 = 横 y=790（742..838）+ 竖 x=880（600..790）+ 撇 (700,780)→(470,620)；
      口 x 430..880，墨迹 300..560（腔 92）。
    """
    g = Glyph("uni7D39", advance=1000, unicode=0x7D39, note="紹：糹 + 召")
    _sikon(g, 60)
    g.hbar(380, 900, 790, weight=W_MAIN)
    g.vbar(880, 600, 790, weight=W_MAIN)
    g.diag(700, 780, 470, 620, weight=W_SEC)
    _kuchi(g, 430, 880, 300, 560, W_THIN)
    return g


def _g_in() -> Glyph:
    """飲 U+98F2（12画）＝ 飠 + 欠。

    飠：人 = 撇 (250,770)→(110,640)、捺 (250,770)→(390,640)；
      一 y=620（572..668）；曰 x 130..380 墨迹 220..540（腔 34）；
      竖提 x=172（60..220）；撇 (330,220)→(255,85)；右下点 (390,125)。
    欠：撇 (570,790)→(500,660)；横 y=660（612..708）x 500..900；
      斜撇 (900,660)→(700,260) 斜率 2；捺 (760,360)→(900,260) 斜率 0.5。
    """
    g = Glyph("uni98F2", advance=1000, unicode=0x98F2, note="飲：飠 + 欠")
    g.diag(250, 770, 110, 640, weight=W_MAIN)
    g.diag(250, 770, 390, 640, weight=W_MAIN)
    g.hbar(90, 470, 620, weight=W_MAIN)
    _hi(g, 130, 380, 220, 540, W_THIN)
    g.vbar(172, 60, 220, weight=W_MAIN)
    g.diag(330, 220, 255, 85, weight=W_THIN)
    g.dot(390, 125, w=80, h=100, slant=-14)
    g.diag(570, 790, 500, 660, weight=W_MAIN)
    g.hbar(500, 900, 660, weight=W_MAIN)
    g.diag(900, 660, 700, 260, weight=W_MAIN)
    g.diag(760, 360, 900, 260, weight=W_MAIN)
    return g


def _g_ki() -> Glyph:
    """貴 U+8CB4（12画）＝ 中 + 一 + 貝。

    中：竖 x=550（546..820，出头 16）、口 x 420..680 墨迹 612..804（腔 32）。
    一：y=546（504..588），x 240..760。
    貝：目 x 260..740，墨迹 60..480（腔 28）；八：撇 (380,60)→(320,5)、
      捺 (620,60)→(680,5)。
    """
    g = Glyph("uni8CB4", advance=1000, unicode=0x8CB4, note="貴：中 + 一 + 貝")
    g.vbar(550, 546, 820, weight=W_MAIN)
    _kuchi(g, 420, 680, 612, 804, W_THIN)
    g.hbar(240, 760, 546, weight=W_THIN)
    _me(g, 260, 740, 60, 480, W_THIN)
    g.diag(380, 60, 320, 5, weight=W_SEC)
    g.diag(620, 60, 680, 5, weight=W_SEC)
    return g


def _g_saki() -> Glyph:
    """埼 U+57FC（11画）＝ 土 + 奇。

    土：竖 x=170（440..800）、短横 y=700（658..742）、长横 y=440（392..488）。
    奇：大 = 横 y=700 x 340..900、撇 (620,700)→(510,480) 斜率 2、
      捺 (640,700)→(870,585) 斜率 0.5；可 = 横 y=440 x 340..900、
      口 x 380..600 墨迹 130..360（腔 62）、亅 x=790（60..440）。
    """
    g = Glyph("uni57FC", advance=1000, unicode=0x57FC, note="埼：土 + 奇")
    g.vbar(170, 440, 800, weight=W_MAIN)
    g.hbar(90, 250, 700, weight=W_THIN)
    g.hbar(60, 290, 440, weight=W_MAIN)
    g.hbar(340, 900, 700, weight=W_MAIN)
    g.diag(620, 700, 510, 480, weight=W_MAIN)
    g.diag(640, 700, 870, 585, weight=W_MAIN)
    g.hbar(340, 900, 440, weight=W_MAIN)
    _kuchi(g, 380, 600, 130, 360, W_THIN)
    g.vbar(790, 60, 440, weight=W_MAIN)
    return g


def _g_sho_2() -> Glyph:
    """焦 U+7126（12画）＝ 隹 + 灬。

    隹（与雇同款，见 _jo）：丿 (300,780)→(245,670)、左竖 x=140、中竖 x=520、
      四横 y=700 / 574 / 448 / 322（相邻白口 30）。
    灬：四点 y=120（墨迹 60..180），斜切 -14。
    """
    g = Glyph("uni7126", advance=1000, unicode=0x7126, note="焦：隹 + 灬")
    _jo(g, 60, 700, 330, 790, 820, 780, 670)
    g.dot(160, 120, w=84, h=120, slant=-14)
    g.dot(380, 120, w=84, h=120, slant=-14)
    g.dot(600, 120, w=84, h=120, slant=-14)
    g.dot(820, 120, w=84, h=120, slant=-14)
    return g


def _g_koyu() -> Glyph:
    """雇 U+96C7（12画）＝ 戸 + 隹。

    戸：顶横 y=778（W_THIN，墨迹 736..820），x 100..900。
    隹：丿 (300,780)→(245,690)、左竖 x=140（60..730）、中竖 x=520（60..740）、
      四横 y=660 / 534 / 408 / 282（相邻白口 30）。
    """
    g = Glyph("uni96C7", advance=1000, unicode=0x96C7, note="雇：戸 + 隹")
    g.hbar(100, 900, 778, weight=W_THIN)
    _jo(g, 60, 660, 60, 730, 740, 780, 690)
    return g


def _g_ura() -> Glyph:
    """浦 U+6D66（10画）＝ 氵 + 甫。

    氵：上点 (150,700) 与中点 (130,530) 斜切 26，提 (80,280)→(280,380) 斜率 0.5。
    甫：竖点 x=630（740..820）、横 y=750（702..798）；
      冂 = 左竖 x=382 / 顶横 y=618 / 右竖 x=878，均落到 180；
      两内横 y=458 / 298（带高 76）；中竖 x=630 贯穿。
    """
    g = Glyph("uni6D66", advance=1000, unicode=0x6D66, note="浦：氵 + 甫")
    g.dot(150, 700, w=84, h=104, slant=26)
    g.dot(130, 530, w=84, h=104, slant=26)
    g.diag(80, 280, 280, 380, weight=W_MAIN)
    g.vbar(630, 740, 820, weight=W_THIN)
    g.hbar(340, 920, 750, weight=W_MAIN)
    g.vbar(382, 180, 660, weight=W_THIN)
    g.hbar(382, 878, 618, weight=W_THIN)
    g.vbar(878, 180, 660, weight=W_THIN)
    g.hbar(382, 878, 458, weight=W_THIN)
    g.hbar(382, 878, 298, weight=W_THIN)
    g.vbar(630, 180, 660, weight=W_MAIN)
    return g


def _g_kae() -> Glyph:
    """替 U+66FF（12画）＝ 夫 夫 + 曰。

    上部两夫：各 = 竖点 x=300 / 660（760..820）、上横 y=740（692..788）、
      下横 y=580（532..628）、撇捺自 x=300 / 660 斜出至 410 / 430。
    下部曰：x 140..860，墨迹 0..310（两腔各 29）。
    """
    g = Glyph("uni66FF", advance=1000, unicode=0x66FF, note="替：夫夫 + 曰")
    g.vbar(300, 760, 820, weight=W_THIN)
    g.hbar(160, 440, 740, weight=W_MAIN)
    g.hbar(120, 480, 580, weight=W_MAIN)
    g.diag(300, 570, 160, 430, weight=W_MAIN)
    g.diag(300, 570, 440, 430, weight=W_MAIN)
    g.vbar(660, 760, 820, weight=W_THIN)
    g.hbar(520, 800, 740, weight=W_MAIN)
    g.hbar(480, 840, 580, weight=W_MAIN)
    g.diag(660, 570, 520, 430, weight=W_MAIN)
    g.diag(660, 570, 800, 430, weight=W_MAIN)
    _hi(g, 140, 860, 0, 310, W_THIN)
    return g


def _g_yoshi() -> Glyph:
    """預 U+9810（13画）＝ 予 + 頁。

    予：横 y=740（692..788）x 80..420、斜撇 (390,720)→(170,500)、
      竖 x=350（200..740）、下横 y=400（352..448）。
    頁：横 y=780（732..828）x 500..900、短撇 (700,740)→(660,660)、
      目 x 500..900 墨迹 200..640（三腔各 34.7）、八：撇 (620,200)→(540,40)、
      捺 (780,200)→(860,40)。
    """
    g = Glyph("uni9810", advance=1000, unicode=0x9810, note="預：予 + 頁")
    g.hbar(80, 420, 740, weight=W_MAIN)
    g.diag(390, 720, 170, 500, weight=W_MAIN)
    g.vbar(350, 200, 740, weight=W_MAIN)
    g.hbar(80, 420, 400, weight=W_MAIN)
    g.hbar(500, 900, 780, weight=W_MAIN)
    g.diag(700, 740, 660, 660, weight=W_THIN)
    _me(g, 500, 900, 200, 640, W_THIN)
    g.diag(620, 200, 540, 40, weight=W_SEC)
    g.diag(780, 200, 860, 40, weight=W_SEC)
    return g


def _g_yaki() -> Glyph:
    """焼 U+713C（12画）＝ 火 + 尭。

    火：左点竖 x=115（630..790）、右上短撇 (300,790)→(250,690)、
      撇 (150,620)→(60,440) 斜率 2、捺 (150,620)→(330,530) 斜率 0.5。
    尭：竖 x=600（700..820）、横 y=690（642..738）、横 y=546（498..594）、
      兀的横 y=420（372..468）、撇 (520,410)→(440,290)、竖 x=720（100..410）。
    """
    g = Glyph("uni713C", advance=1000, unicode=0x713C, note="焼：火 + 尭")
    g.vbar(115, 630, 790, weight=W_MAIN)
    g.diag(300, 790, 250, 690, weight=W_THIN)
    g.diag(150, 620, 60, 440, weight=W_MAIN)
    g.diag(150, 620, 330, 530, weight=W_MAIN)
    g.vbar(600, 700, 820, weight=W_MAIN)
    g.hbar(380, 840, 690, weight=W_MAIN)
    g.hbar(380, 840, 546, weight=W_MAIN)
    g.hbar(360, 860, 420, weight=W_MAIN)
    g.diag(520, 410, 440, 290, weight=W_MAIN)
    g.vbar(720, 100, 410, weight=W_MAIN)
    return g


def _g_shō() -> Glyph:
    """称 U+79F0（10画）＝ 禾 + 尓。

    禾：撇 (340,790)→(150,690) 斜率 0.5、横 y=690（642..738）x 60..390、
      竖 x=230（100..790）、撇 (210,600)→(90,360) 斜率 2、
      捺 (250,620)→(370,500) 斜率 1。
    尓：撇 (560,800)→(480,700)、横 y=690 x 430..870、竖 x=680（140..660）、
      撇 (620,620)→(490,380) 斜率 2、捺 (760,620)→(880,500) 斜率 1。
    """
    g = Glyph("uni79F0", advance=1000, unicode=0x79F0, note="称：禾 + 尓")
    g.diag(340, 790, 150, 690, weight=W_THIN)
    g.hbar(60, 390, 690, weight=W_MAIN)
    g.vbar(230, 100, 790, weight=W_MAIN)
    g.diag(210, 600, 90, 360, weight=W_MAIN)
    g.diag(250, 620, 370, 500, weight=W_MAIN)
    g.diag(560, 800, 480, 700, weight=W_THIN)
    g.hbar(430, 870, 690, weight=W_MAIN)
    g.vbar(680, 140, 660, weight=W_MAIN)
    g.diag(620, 620, 490, 380, weight=W_MAIN)
    g.diag(760, 620, 880, 500, weight=W_MAIN)
    return g


def _g_nō() -> Glyph:
    """納 U+7D0D（10画）＝ 糹 + 内。

    糹：见 _sikon（x 60..346）。
    内：冂 = 左竖 x=400（60..770）/ 顶横 y=770（722..818）x 400..900 /
      右竖 x=900（60..770）；人 = 撇 (640,740)→(480,420) 斜率 2、
      捺 (650,700)→(850,600) 斜率 0.5。
    """
    g = Glyph("uni7D0D", advance=1000, unicode=0x7D0D, note="納：糹 + 内")
    _sikon(g, 60)
    g.vbar(400, 60, 770, weight=W_MAIN)
    g.hbar(400, 900, 770, weight=W_MAIN)
    g.vbar(900, 60, 770, weight=W_MAIN)
    g.diag(640, 740, 480, 420, weight=W_MAIN)
    g.diag(650, 700, 850, 600, weight=W_MAIN)
    return g


def _g_chō() -> Glyph:
    """章 U+7AE0（11画）＝ 立 + 早。

    立：竖点 x=490（770..820）、横 y=730（682..778）、丷两点 y=622
      （墨迹 586..658）、下横 y=514（466..562）。
    早：日 x 145..830 墨迹 122..442（两腔各 34）；十 = 横 y=50（2..98）
      x 90..885 + 竖 x=490（98..140）。
    """
    g = Glyph("uni7AE0", advance=1000, unicode=0x7AE0, note="章：立 + 早")
    g.vbar(490, 770, 820, weight=W_THIN)
    g.hbar(115, 860, 730, weight=W_MAIN)
    g.dot(300, 622, w=88, h=72, slant=-14)
    g.dot(690, 622, w=88, h=72, slant=14)
    g.hbar(60, 940, 514, weight=W_MAIN)
    _hi(g, 145, 830, 122, 442, W_THIN)
    g.hbar(90, 885, 50, weight=W_MAIN)
    g.vbar(490, 98, 140, weight=W_MAIN)
    return g


def _g_fun() -> Glyph:
    """紛 U+7D1B（10画）＝ 糹 + 分。

    糹：见 _sikon（x 60..346）。
    分：八 = 撇 (620,800)→(480,660) 斜率 1、捺 (620,790)→(830,580) 斜率 1；
      刀 = 横 y=580（532..628）x 400..900、竖 x=880（260..580）、
      撇 (700,570)→(520,200) 斜率 2。
    """
    g = Glyph("uni7D1B", advance=1000, unicode=0x7D1B, note="紛：糹 + 分")
    _sikon(g, 60)
    g.diag(620, 800, 480, 660, weight=W_MAIN)
    g.diag(620, 790, 830, 580, weight=W_MAIN)
    g.hbar(400, 900, 580, weight=W_MAIN)
    g.vbar(880, 260, 580, weight=W_MAIN)
    g.diag(700, 570, 520, 200, weight=W_MAIN)
    return g


def _g_kashi() -> Glyph:
    """貸 U+8CB8（12画）＝ 代 + 貝。

    代：亻 = 撇 (210,800)→(100,630) + 竖 x=155（430..670）；
      弋 = 横 y=680（632..728）x 280..900 + 斜钩 (500,810)→(860,440)
      斜率 1 + 右下点 (650,790)。
    貝：目 x 270..730 墨迹 60..480（腔 28）；八：撇 (390,60)→(330,5)、
      捺 (610,60)→(670,5)。
    """
    g = Glyph("uni8CB8", advance=1000, unicode=0x8CB8, note="貸：代 + 貝")
    g.diag(210, 800, 100, 630, weight=W_MAIN)
    g.vbar(155, 430, 670, weight=W_MAIN)
    g.hbar(280, 900, 680, weight=W_MAIN)
    g.diag(500, 810, 860, 440, weight=W_MAIN)
    g.dot(650, 790, w=80, h=96, slant=-14)
    _me(g, 270, 730, 60, 480, W_THIN)
    g.diag(390, 60, 330, 5, weight=W_SEC)
    g.diag(610, 60, 670, 5, weight=W_SEC)
    return g


def _g_shin() -> Glyph:
    """慎 U+614E（13画）＝ 忄 + 真。

    忄：竖 x=150（60..820）、左点 (72,620) 斜切 +14、右点 (270,600) 斜切 -14。
    真：十 = 竖 x=620（740..820）+ 横 y=730（682..778）x 400..900；
      目 x 400..860 墨迹 238..658（三腔各 28）；底横 y=172（130..214）
      x 360..900；八：撇 (560,190)→(500,20)、捺 (740,190)→(800,20)。
    """
    g = Glyph("uni614E", advance=1000, unicode=0x614E, note="慎：忄 + 真")
    g.vbar(150, 60, 820, weight=W_MAIN)
    g.dot(72, 620, w=76, h=104, slant=14)
    g.dot(270, 600, w=76, h=104, slant=-14)
    g.vbar(620, 740, 820, weight=W_THIN)
    g.hbar(400, 900, 730, weight=W_MAIN)
    _me(g, 400, 860, 238, 658, W_THIN)
    g.hbar(360, 900, 172, weight=W_THIN)
    g.diag(560, 190, 500, 20, weight=W_SEC)
    g.diag(740, 190, 800, 20, weight=W_SEC)
    return g


def _g_kō() -> Glyph:
    """控 U+63A7（11画）＝ 扌 + 空。

    扌：竖 x=170（300..820）、横 y=640（592..688）x 60..300、
      提 (90,400)→(290,300) 斜率 0.5。
    空：穴 = 竖点 x=580（740..820）+ 横 y=700（652..748）x 340..900 +
      八（撇 (540,660)→(430,550)、捺 (640,660)→(770,530)）；
      工 = 横 y=420（372..468）x 360..920 + 竖 x=630（140..420）+
      横 y=180（132..228）x 340..920。
    """
    g = Glyph("uni63A7", advance=1000, unicode=0x63A7, note="控：扌 + 空")
    g.vbar(170, 300, 820, weight=W_MAIN)
    g.hbar(60, 300, 640, weight=W_MAIN)
    g.diag(90, 400, 290, 300, weight=W_MAIN)
    g.vbar(580, 740, 820, weight=W_THIN)
    g.hbar(340, 900, 700, weight=W_MAIN)
    g.diag(540, 660, 430, 550, weight=W_MAIN)
    g.diag(640, 660, 770, 530, weight=W_MAIN)
    g.hbar(360, 920, 420, weight=W_MAIN)
    g.vbar(630, 140, 420, weight=W_MAIN)
    g.hbar(340, 920, 180, weight=W_MAIN)
    return g


def _g_aku() -> Glyph:
    """握 U+63E1（12画）＝ 扌 + 屋。

    扌：竖 x=170（300..820）、横 y=640（592..688）x 60..300、
      提 (90,400)→(290,300) 斜率 0.5。
    屋：尸 = 横 y=780（732..828）x 360..900 + 竖 x=880（620..780）+
      横 y=640（592..688）+ 撇 x=400（560..640）；
      至 = 横 y=520（472..568）x 380..900 + 厶（撇 (560,500)→(480,340)、
      折 y=340 x 470..640、右下点 (700,320)）+ 土（竖 x=700 100..340、
      横 y=220 x 540..880、横 y=100 x 460..920）。
    """
    g = Glyph("uni63E1", advance=1000, unicode=0x63E1, note="握：扌 + 屋")
    g.vbar(170, 300, 820, weight=W_MAIN)
    g.hbar(60, 300, 640, weight=W_MAIN)
    g.diag(90, 400, 290, 300, weight=W_MAIN)
    g.hbar(360, 900, 780, weight=W_MAIN)
    g.vbar(880, 620, 780, weight=W_MAIN)
    g.hbar(360, 900, 640, weight=W_MAIN)
    g.vbar(400, 560, 640, weight=W_MAIN)
    g.hbar(380, 900, 520, weight=W_MAIN)
    g.diag(560, 500, 480, 340, weight=W_MAIN)
    g.hbar(470, 640, 340, weight=W_THIN)
    g.dot(700, 320, w=80, h=96, slant=-14)
    g.vbar(700, 100, 340, weight=W_MAIN)
    g.hbar(540, 880, 220, weight=W_THIN)
    g.hbar(460, 920, 100, weight=W_MAIN)
    return g


def build() -> list[Glyph]:
    return [
        _g_bi(),      # 閉
        _g_ato(),     # 跡
        _g_kou(),     # 貢
        _g_roku(),    # 鹿
        _g_kyo(),     # 弱
        _g_chin(),    # 賃
        _g_sho(),     # 紹
        _g_in(),      # 飲
        _g_ki(),      # 貴
        _g_saki(),    # 埼
        _g_sho_2(),   # 焦
        _g_koyu(),    # 雇
        _g_ura(),     # 浦
        _g_kae(),     # 替
        _g_yoshi(),   # 預
        _g_yaki(),    # 焼
        _g_shō(),     # 称
        _g_nō(),      # 納
        _g_chō(),     # 章
        _g_fun(),     # 紛
        _g_kashi(),   # 貸
        _g_shin(),    # 慎
        _g_kō(),      # 控
        _g_aku(),     # 握
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s3-014.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
