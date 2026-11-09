"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s3-016。

本批 24 字，笔画范围 10–13，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
============
* 字面框 x 60..940、y 0..820，advance = 1000（与繁体汉字同一档，便于中英日混排）。
* 笔画权重：主 96 / 次 92 / 细 84 / 点 84。
  - 笔画少、字面开阔的字（埋・哲・硬・釈・督类）保持 96 主重；
  - 横密字（誉・華・陽・歯・勧）的框体横画降到 84/92，保证
    口/日/目/田 型方框的腔高 ≥ 24（框高 ≥ 2×笔画宽+24），避免「黑砖」。
* 端点：横竖撇捺一律平切硬边（hbar / vbar / diag）；点与短撇一律斜切
  平行四边形（dot）。slant 只用规范档：-14（右下的点）、+14（左下的点）、
  26（短撇）、0（竖点）。
* 同族复用：氵 / 扌 / 忄 / 亻 / 彳 / 阝 / 艹 / 攵 / 儿 / 口 / 日 / 目 / 田
  全部写成 helper，批内只做位置与大小的光学校正（GLY-004）。
* 斜笔墨迹沿垂直于中心线展开：所有 diag 给真实中心线两端点，
  不按水平笔画那样用 ±w/2 去估 y 向占位（AGENTS.md 铁律 7/8）。
* 相邻横画白口 ≥ 24；口/日/目/田 型腔高 ≥ 24（零容忍）。
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


# ---------------------------------------------------------------- 对齐 helper
def htop(edge: float, w: float = W_MAIN) -> float:
    """横画中心线：使墨迹 **上缘** 对齐 edge。"""
    return edge - w / 2.0


def hbot(edge: float, w: float = W_MAIN) -> float:
    """横画中心线：使墨迹 **下缘** 对齐 edge。"""
    return edge + w / 2.0


# ---------------------------------------------------------------- 部件 helper
def comp_kuchi(g: Glyph, x0: float, x1: float, y0: float, y1: float,
               w: float = W_SEC) -> None:
    """口：四边方框。x0/x1 = 墨迹左右界，y0/y1 = 墨迹上下界。"""
    g.hbar(x0, x1, htop(y1, w), weight=w)
    g.hbar(x0, x1, hbot(y0, w), weight=w)
    g.vbar(x0 + w / 2.0, y0, y1, weight=w)
    g.vbar(x1 - w / 2.0, y0, y1, weight=w)


def comp_hi(g: Glyph, x0: float, x1: float, y0: float, y1: float,
            w: float = W_THIN, cav: float = 26.0) -> None:
    """日：三横两竖（两个腔，腔高 = cav）。"""
    c = (y1 - y0 - 3 * w) / 2.0
    assert c >= cav, ("日 腔高不足", c)
    for i in range(3):
        g.hbar(x0, x1, htop(y1 - i * (w + c), w), weight=w)
    g.vbar(x0 + w / 2.0, y0, y1, weight=w)
    g.vbar(x1 - w / 2.0, y0, y1, weight=w)


def comp_me(g: Glyph, x0: float, x1: float, y0: float, y1: float,
            w: float = W_THIN, cav: float = 26.0) -> None:
    """目：四横两竖（三个腔）。"""
    c = (y1 - y0 - 4 * w) / 3.0
    assert c >= cav, ("目 腔高不足", c)
    for i in range(4):
        g.hbar(x0, x1, htop(y1 - i * (w + c), w), weight=w)
    g.vbar(x0 + w / 2.0, y0, y1, weight=w)
    g.vbar(x1 - w / 2.0, y0, y1, weight=w)


def comp_den(g: Glyph, x0: float, x1: float, y0: float, y1: float,
             w: float = W_THIN, cav: float = 26.0) -> None:
    """田：日 + 中竖（四个腔）。"""
    c = (y1 - y0 - 3 * w) / 2.0
    assert c >= cav, ("田 腔高不足", c)
    for i in range(3):
        g.hbar(x0, x1, htop(y1 - i * (w + c), w), weight=w)
    g.vbar(x0 + w / 2.0, y0, y1, weight=w)
    g.vbar(x1 - w / 2.0, y0, y1, weight=w)
    g.vbar((x0 + x1) / 2.0, y0, y1, weight=w)


def comp_maru(g: Glyph, x: float, y0: float = 0.0, y1: float = 820.0,
              w: float = W_MAIN) -> None:
    """阝（左耳）：竖 + 横折弯钩（旗形回勾，批内统一）。"""
    g.vbar(x, y0, y1, weight=w)
    g.hbar(x, x + 132, htop(y1 - 58, w), weight=w)
    g.diag(x + 132, y1 - 66, x + 54, y1 - 218, weight=W_SEC)


def comp_sanzui(g: Glyph, x: float, w: float = W_MAIN) -> None:
    """氵：短撇(26) + 丶(-14) + 提。批内统一坐标，只随字面平移。"""
    g.dot(x + 18, 668, w=88, h=104, slant=26)
    g.dot(x + 6, 438, w=88, h=104, slant=-14)
    g.diag(x - 6, 128, x + 188, 326, weight=w)


def comp_te(g: Glyph, xc: float, x0: float, x1: float, ytop: float,
            ybot: float, w: float = W_MAIN, rise: float = 0.0) -> None:
    """扌：一（横） + 丨（竖） + 提（右上斜）。"""
    g.hbar(x0, x1, htop(ytop, w), weight=w)
    g.vbar(xc, ybot, ytop, weight=w)
    g.diag(x0 + 18, rise, xc + 34, rise + 122, weight=w)


def comp_risshin(g: Glyph, x: float, w: float = W_MAIN) -> None:
    """亻：丿 + 丨。"""
    g.diag(x + 118, 792, x + 26, 688, weight=w)
    g.vbar(x + 92, 40, 620, weight=w)


def comp_gonin(g: Glyph, x: float, w: float = W_MAIN) -> None:
    """彳：丿 + 丿 + 丨。"""
    g.diag(x + 128, 800, x + 34, 694, weight=w)
    g.diag(x + 132, 616, x + 12, 470, weight=w)
    g.vbar(x + 88, 30, 508, weight=w)


def comp_kusanmuri(g: Glyph, x0: float, x1: float, y1: float,
                   w: float = W_MAIN, drop: float = 86.0) -> None:
    """艹：一 + 丨 + 丨。"""
    g.hbar(x0, x1, htop(y1, w), weight=w)
    cx = (x0 + x1) / 2.0
    g.vbar(cx - (x1 - x0) * 0.25, y1 - drop, y1, weight=w)
    g.vbar(cx + (x1 - x0) * 0.25, y1 - drop, y1, weight=w)


def comp_boku(g: Glyph, x0: float, x1: float, y1: float,
               w: float = W_MAIN) -> None:
    """攵：丿 + 一 + 丿 + 乀。"""
    g.diag(x1 - 66, y1 - 8, x1 - 178, y1 - 116, weight=w)
    g.hbar(x0, x1 - 4, htop(y1 - 178, w), weight=w)
    g.diag(x1 - 4, y1 - 168, x0 + 34, 108, weight=w)
    g.diag(x0 + 132, 452, x1 + 6, 112, weight=w)


def comp_ni(g: Glyph, x: float, y0: float, y1: float,
            w: float = W_MAIN) -> None:
    """儿右腿 乚：竖 + 右勾。"""
    g.vbar(x, y0, y1, weight=w)
    g.hbar(x, x + 84, hbot(y0, w), weight=w)


def comp_sei(g: Glyph, x0: float, x1: float, w: float = W_SEC) -> None:
    """生：丿 + 一 + 丨 + 一 + 一（批内统一，用于隆）。"""
    g.diag(x0 + 110, 424, x0 + 44, 322, weight=w)
    g.hbar(x0 + 20, x1 - 30, htop(296, w), weight=w)
    g.vbar((x0 + x1) / 2.0 + 10, 56, 296, weight=w)
    g.hbar(x0 + 20, x1 - 30, htop(176, w), weight=w)
    g.hbar(x0 + 20, x1 - 30, htop(56, w), weight=w)


# ================================================================ 24 个字形
def _do() -> Glyph:
    """盗 U+76D7 —— 次（上，y 440..820）＋ 皿（下，y 0..390）。

    笔画清单：
      冫 ① 丶 dot(145,700,slant=-14) ② 提 diag(95,478 → 258,572)
      欠 ③ 丿 diag(475,790 → 400,682)
          ④ 乛 hbar(425..838, c=660) + diag(838,660 → 742,562)
          ⑤ 丿 diag(690,556 → 452,440)
          ⑥ 乀 diag(676,588 → 906,442)
      皿 ⑦ 上横 hbar(175..855, c=320) ⑧ 下横 hbar(160..870, c=48)
          ⑨⑩⑪⑫ 竖 x=210/405/615/820，y 90..280
    皿 外框高 364（≥2×92+24=208），三格腔高 180、腔宽 ≥ 95。
    """
    g = Glyph("uni76D7", advance=1000, unicode=0x76D7, note="盗：次上皿下")
    g.dot(145, 700, w=88, h=112, slant=-14)
    g.diag(95, 478, 258, 572, weight=W_MAIN)
    g.diag(475, 790, 400, 682, weight=W_MAIN)
    g.hbar(425, 838, htop(660, W_SEC), weight=W_SEC)
    g.diag(838, 660, 742, 562, weight=W_SEC)
    g.diag(690, 556, 452, 440, weight=W_MAIN)
    g.diag(676, 588, 906, 442, weight=W_MAIN)
    g.hbar(175, 855, htop(366, W_SEC), weight=W_SEC)
    g.hbar(160, 870, hbot(2, W_SEC), weight=W_SEC)
    for cx in (210.0, 405.0, 615.0, 820.0):
        g.vbar(cx, 88, 280, weight=W_SEC)
    return g


def _ka() -> Glyph:
    """賀 U+8CC0 —— 左 加（x 60..430）＋ 右 貝（x 480..930）。

    加：① 力之横折 hbar(90..330,c=700)+vbar(330,540..700)
        ② 力之撇 diag(210,700 → 82,492)
        ③ 口 box(190..420, 60..390)
    貝：④ 目 上横 c=778 ⑤ 中横 c=666 ⑥ 中横 c=554 ⑦ 下横 c=442
        ⑧ 左竖 x=542 ⑨ 右竖 x=868
        ⑩ 八之撇 diag(640,340 → 500,52) ⑪ 八之捺 diag(720,340 → 900,52)
    目 三腔高 28（≥24），腔宽 242。
    """
    g = Glyph("uni8CC0", advance=1000, unicode=0x8CC0, note="賀：左加右貝")
    # 加
    g.hbar(90, 330, htop(700, W_MAIN), weight=W_MAIN)
    g.vbar(330, 540, 700, weight=W_MAIN)
    g.diag(210, 700, 82, 492, weight=W_MAIN)
    comp_kuchi(g, 190, 420, 60, 390, w=W_THIN)
    # 貝
    comp_me(g, 500, 910, 400, 820, w=W_THIN, cav=28.0)
    g.diag(640, 340, 500, 52, weight=W_MAIN)
    g.diag(720, 340, 900, 52, weight=W_MAIN)
    return g


def _shugo() -> Glyph:
    """訟 U+8A1F —— 左 言（x 80..430）＋ 右 公（x 500..930）。

    言：① 丶 dot(250,750,slant=0) ② 一 c=654 ③ 一 c=524 ④ 一 c=394
        ⑤ 口 上横 c=244 ⑥ 口 下横 c=86 ⑦ 口 左竖 ⑧ 口 右竖
    公：⑨ 八之丿 diag(640,800 → 528,642) ⑩ 八之丶 dot(790,740,slant=-14)
        ⑪ 厶撇折 diag(700,610 → 552,486)+hbar(552..716,c=486)
        ⑫ 厶之点 dot(716,432,slant=-14)
    言 四条横线白口均 ≥ 38，口腔高 66。
    """
    g = Glyph("uni8A1F", advance=1000, unicode=0x8A1F, note="訟：左言右公")
    # 言
    g.dot(250, 750, w=88, h=100, slant=0)
    g.hbar(80, 430, htop(700, W_SEC), weight=W_SEC)
    g.hbar(80, 430, htop(570, W_SEC), weight=W_SEC)
    g.hbar(80, 430, htop(440, W_SEC), weight=W_SEC)
    comp_kuchi(g, 80, 430, 40, 290, w=W_SEC)
    # 公
    g.diag(640, 800, 528, 642, weight=W_MAIN)
    g.dot(790, 740, w=88, h=112, slant=-14)
    g.diag(700, 610, 552, 486, weight=W_MAIN)
    g.hbar(552, 716, htop(486, W_THIN), weight=W_THIN)
    g.dot(716, 432, w=84, h=104, slant=-14)
    return g


def _yo() -> Glyph:
    """誉 U+8A89 —— 上 兴（ツ＋一＋八，y 543..820）＋ 下 言（y 0..568）。

    ツ：① 丶 dot(330,786,slant=-14) ② 丶 dot(490,786,slant=-14)
        ③ 丿 diag(700,818 → 630,750)
    兴：④ 一 c=658  ⑤ 八之丿 diag(430,590 → 350,545)
        ⑥ 八之丶 dot(600,570,slant=-14)
    言：⑦ 丶 dot(500,546,slant=0) ⑧ 一 c=482 ⑨ 一 c=372 ⑩ 一 c=262
        ⑪ 口 上横 c=152 ⑫ 口 下横 c=42 ⑬ 口 左竖 ⑭ 口 右竖
    言 白口 24/26/26/26，口腔高 26（≥24）。全部横画降到 84 以塞下。
    """
    g = Glyph("uni8A89", advance=1000, unicode=0x8A89, note="誉：上兴下言")
    g.dot(330, 786, w=80, h=64, slant=-14)
    g.dot(490, 786, w=80, h=64, slant=-14)
    g.diag(700, 818, 630, 750, weight=W_THIN)
    g.hbar(200, 800, htop(700, W_THIN), weight=W_THIN)
    g.diag(430, 590, 350, 545, weight=W_THIN)
    g.dot(600, 570, w=80, h=54, slant=-14)
    # 言
    g.dot(500, 546, w=76, h=44, slant=0)
    g.hbar(300, 700, htop(524, W_THIN), weight=W_THIN)
    g.hbar(300, 700, htop(414, W_THIN), weight=W_THIN)
    g.hbar(300, 700, htop(304, W_THIN), weight=W_THIN)
    comp_kuchi(g, 300, 700, 0, 194, w=W_THIN)
    return g


def _ben() -> Glyph:
    """勉 U+52C9 —— 左 免（x 60..520）＋ 右 力（x 560..940）。

    免：① ⺈之丿 diag(232,790 → 140,660)
        ② ⺈之乛 hbar(196..404,c=656)+diag(404,656 → 330,570)
        ③ 口 box(180..430, 276..540)
        ④ 儿之丿 diag(260,276 → 128,44)
        ⑤ 儿之乚 vbar(390,44..276)+右勾 hbar(390..470,44)
    力：⑥ 横折 hbar(590..930,c=700)+vbar(912,420..700)
        ⑦ 撇 diag(742,700 → 602,240)
    口腔高 96（≥24），腔宽 82。
    「⺈乛横」与「口顶横」白口 32（原本重叠 64，腔被封死 → 整组「口+儿」下移 96）。
    儿之丿再左移 40：原本其右上角 (341.7→342) 与「儿之乚」竖桩左缘 (390−48=342)
    精确重合，轮廓并集出「Ring Self-intersection」。左移后两者相距 40。
    下移/左移只做等量平移，笔画角度/斜率不变（AGENTS.md 铁律 10）。
    """
    g = Glyph("uni52C9", advance=1000, unicode=0x52C9, note="勉：左免右力")
    g.diag(232, 790, 140, 660, weight=W_MAIN)
    g.hbar(196, 404, htop(656, W_THIN), weight=W_THIN)
    g.diag(404, 656, 330, 570, weight=W_THIN)
    comp_kuchi(g, 180, 430, 276, 540, w=W_THIN)
    g.diag(260, 276, 128, 44, weight=W_MAIN)
    g.vbar(390, 44, 276, weight=W_MAIN)
    g.hbar(390, 472, hbot(44, W_THIN), weight=W_THIN)
    # 力
    g.hbar(590, 930, htop(700, W_MAIN), weight=W_MAIN)
    g.vbar(912, 420, 700, weight=W_MAIN)
    g.diag(742, 700, 602, 240, weight=W_MAIN)
    return g


def _kan() -> Glyph:
    """勧 U+52E7 —— 左 雚（艹＋吅＋隹，x 60..560）＋ 右 力（x 600..940）。

    艹：① 一 c=774 ② 丨 x=190 ③ 丨 x=430
    吅：④⑤ 左口 box(60..300, 470..690) ⑥⑦ 右口 box(320..560, 470..690)
    隹：⑧ 一 c=358 ⑨ 左竖 x=180 ⑩ 一 c=234 ⑪ 一 c=110 ⑫ 右竖 x=438
    力：⑬ 横折 hbar(600..940,c=700)+vbar(892,420..700) ⑭ 撇 diag(760,700 → 610,180)
    吅 两口腔高 52 / 腔宽 72；隹腔高 40。
    """
    g = Glyph("uni52E7", advance=1000, unicode=0x52E7, note="勧：左雚右力")
    comp_kusanmuri(g, 60, 560, 820, w=W_SEC, drop=80.0)
    comp_kuchi(g, 60, 300, 470, 690, w=W_THIN)
    comp_kuchi(g, 320, 560, 470, 690, w=W_THIN)
    g.hbar(140, 480, htop(400, W_THIN), weight=W_THIN)
    g.vbar(180, 40, 400, weight=W_THIN)
    g.hbar(180, 480, htop(276, W_THIN), weight=W_THIN)
    g.hbar(180, 480, htop(152, W_THIN), weight=W_THIN)
    g.vbar(438, 40, 400, weight=W_THIN)
    # 力
    g.hbar(600, 940, htop(700, W_MAIN), weight=W_MAIN)
    g.vbar(892, 420, 700, weight=W_MAIN)
    g.diag(760, 700, 610, 180, weight=W_MAIN)
    return g


def _yaku() -> Glyph:
    """翌 U+7FCC —— 上 羽（y 470..820）＋ 下 立（y 0..430）。

    羽：① ヨ甲 上横 c=778+横折右竖 x=250 ② 一 c=696 ③ 一 c=580
        ④ ヨ乙 上横 c=778+横折右竖 x=740 ⑤ 一 c=696 ⑥ 一 c=580
    立：⑦ 丶 dot(500,390,slant=0) ⑧ 一 c=254 ⑨ 丷之丿 diag(400,200 → 330,110)
        ⑩ 丷之丶 dot(600,155,slant=-14) ⑪ 一 c=46
    羽 两ヨ腔高 56/56；立底横白口 24。
    「ヨ」中横↔下横白口 32（原本重叠 2 → 下横下移 34，右竖桩同步收短到 496）。
    """
    g = Glyph("uni7FCC", advance=1000, unicode=0x7FCC, note="翌：上羽下立")
    for x0, x1 in ((60.0, 250.0), (520.0, 740.0)):
        g.hbar(x0, x1, htop(820, W_THIN), weight=W_THIN)
        g.vbar(x1 - W_THIN / 2.0, 496, 820, weight=W_THIN)
        g.hbar(x0, x1, htop(696, W_THIN), weight=W_THIN)
        g.hbar(x0, x1, htop(580, W_THIN), weight=W_THIN)
    g.dot(500, 390, w=84, h=70, slant=0)
    g.hbar(180, 820, htop(300, W_SEC), weight=W_SEC)
    g.diag(400, 200, 330, 110, weight=W_SEC)
    g.dot(600, 155, w=84, h=80, slant=-14)
    g.hbar(200, 800, hbot(0, W_SEC), weight=W_SEC)
    return g


def _hi() -> Glyph:
    """陽 U+967D —— 左 阝（x 60..240）＋ 右 昜（x 300..940）。

    阝：① 丨 x=110 ② 横 c=762 ③ 弯钩 diag(242,754 → 164,600)
    昜：④ 日 上横 c=778 ⑤ 中横 c=668 ⑥ 下横 c=558 ⑦ 左竖 x=442 ⑧ 右竖 x=888
        ⑨ 一 c=418 ⑩ 勿之丿 diag(500,360 → 420,196)
        ⑪ 勿之横折 hbar(560..900,c=320)+vbar(878,150..320)
        ⑫ 勿之内撇 diag(700,340 → 600,104) ⑬ 勿之内撇 diag(830,330 → 722,92)
    日 两腔高 26；勿内两撇平行不相接。
    """
    g = Glyph("uni967D", advance=1000, unicode=0x967D, note="陽：左阜右昜")
    comp_maru(g, 110.0)
    comp_hi(g, 400, 930, 516, 820, w=W_THIN, cav=26.0)
    g.hbar(340, 940, htop(460, W_SEC), weight=W_SEC)
    g.diag(500, 360, 420, 196, weight=W_MAIN)
    g.hbar(560, 900, htop(320, W_THIN), weight=W_THIN)
    g.vbar(878, 150, 320, weight=W_THIN)
    g.diag(700, 340, 600, 104, weight=W_MAIN)
    g.diag(830, 330, 722, 92, weight=W_MAIN)
    return g


def _hyou() -> Glyph:
    """郷 U+90F7 —— 左 幺（x 60..300）＋ 中 艮（x 330..630）＋ 右 阝（x 680..900）。

    幺：① 撇折 diag(230,790 → 125,650)+hbar(125..245,c=650)
        ② 撇折 diag(255,580 → 150,440)+hbar(150..270,c=440)
        ③ 点 dot(215,320,slant=-14)
    艮：④ 一 c=654 ⑤ 左竖 x=384 ⑥ 右竖 x=576 ⑦ 一 c=434 ⑧ 一 c=314
        ⑨ 撇 diag(420,300 → 330,60) ⑩ 乚 vbar(576,60..300)+右勾
    阝：⑪ 丨 x=710 ⑫ 横 c=762 ⑬ 弯钩 diag(842,754 → 764,600)
    艮 两腔高 128/28。
    """
    g = Glyph("uni90F7", advance=1000, unicode=0x90F7, note="郷：左幺中艮右阝")
    g.diag(230, 790, 125, 650, weight=W_MAIN)
    g.hbar(125, 245, htop(650, W_THIN), weight=W_THIN)
    g.diag(255, 580, 150, 440, weight=W_MAIN)
    g.hbar(150, 270, htop(440, W_THIN), weight=W_THIN)
    g.dot(215, 320, w=88, h=96, slant=-14)
    g.hbar(340, 620, htop(700, W_SEC), weight=W_SEC)
    g.vbar(384, 300, 700, weight=W_SEC)
    g.vbar(576, 300, 700, weight=W_SEC)
    g.hbar(340, 620, htop(480, W_SEC), weight=W_SEC)
    g.hbar(340, 620, htop(360, W_SEC), weight=W_SEC)
    g.diag(420, 300, 330, 60, weight=W_MAIN)
    g.vbar(576, 60, 300, weight=W_MAIN)
    g.hbar(576, 660, hbot(60, W_THIN), weight=W_THIN)
    comp_maru(g, 710.0)
    return g


def _kei() -> Glyph:
    """敬 U+656C —— 左 苟（x 60..560）＋ 右 攵（x 590..940）。

    苟：① 艹 一 c=778 ② 丨 x=190 ③ 丨 x=410
        ④ 句之丿 diag(210,690 → 130,562)
        ⑤ 句之横折钩 hbar(190..540,c=640)+vbar(518,380..640)
        ⑥⑦ 口 box(200..450, 140..380)
    攵：⑧ 丿 diag(800,800 → 706,690) ⑨ 一 c=640 ⑩ 丿 diag(890,640 → 630,120)
        ⑪ 乀 diag(770,470 → 930,120)
    口腔高 56 / 腔宽 66。
    """
    g = Glyph("uni656C", advance=1000, unicode=0x656C, note="敬：左苟右攵")
    comp_kusanmuri(g, 60, 540, 820, w=W_THIN, drop=76.0)
    g.diag(210, 690, 130, 562, weight=W_THIN)
    g.hbar(190, 540, htop(640, W_THIN), weight=W_THIN)
    g.vbar(518, 380, 640, weight=W_THIN)
    comp_kuchi(g, 200, 450, 140, 380, w=W_THIN)
    g.diag(800, 800, 706, 690, weight=W_MAIN)
    g.hbar(660, 900, htop(640, W_MAIN), weight=W_MAIN)
    g.diag(890, 640, 630, 120, weight=W_MAIN)
    g.diag(770, 470, 930, 120, weight=W_MAIN)
    return g


def _yure() -> Glyph:
    """揺 U+63FA —— 左 扌（x 60..340）＋ 右 爫（上）＋ 缶（下，x 380..940）。

    扌：① 一 c=612 ② 丨 x=200 ③ 提 diag(78,330 → 238,450)
    爫：④ 丿 diag(420,800 → 340,700) ⑤ 丶 dot(530,755,slant=-14)
        ⑥ 丶 dot(670,755,slant=-14) ⑦ 丿 diag(890,800 → 806,700)
    缶：⑧ 丿 diag(520,610 → 430,500) ⑨ 一 c=540 ⑩ 丨 x=510
        ⑪ 丨 x=690 ⑫ 丨 x=880 ⑬ 一 c=120
    缶 内两腔高 324，腔宽 88/98。
    """
    g = Glyph("uni63FA", advance=1000, unicode=0x63FA, note="揺：左扌右爫缶")
    comp_te(g, 200.0, 60, 340, 660, 40, rise=330.0)
    g.diag(420, 800, 340, 700, weight=W_THIN)
    g.dot(530, 755, w=80, h=88, slant=-14)
    g.dot(670, 755, w=80, h=88, slant=-14)
    g.diag(890, 800, 806, 700, weight=W_THIN)
    g.diag(520, 610, 430, 500, weight=W_MAIN)
    g.hbar(480, 920, htop(540, W_THIN), weight=W_THIN)
    g.vbar(510, 120, 540, weight=W_THIN)
    g.vbar(690, 120, 540, weight=W_THIN)
    g.vbar(880, 120, 540, weight=W_THIN)
    g.hbar(510, 880, htop(120, W_THIN), weight=W_THIN)
    return g


def _kizoku() -> Glyph:
    """既 U+65E2 —— 左 皀（x 60..470）＋ 右 旡（x 520..940）。

    皀：① 丿 diag(300,790 → 245,740) ② 日 上横 c=702 ③ 中横 c=592 ④ 下横 c=482
        ⑤ 左竖 x=182 ⑥ 右竖 x=408
        ⑦ 匕之丿 diag(400,390 → 160,330) ⑧ 匕之乚 vbar(300,60..390)+左勾
    旡：⑨ 一 c=654 ⑩ 丿 diag(760,660 → 570,140) ⑪ 乚 vbar(850,140..660)+右勾
    日 两腔高 26；匕与旡的下端各带钩。
    """
    g = Glyph("uni65E2", advance=1000, unicode=0x65E2, note="既：左皀右旡")
    g.diag(300, 790, 245, 740, weight=W_THIN)
    comp_hi(g, 140, 450, 440, 744, w=W_THIN, cav=26.0)
    g.diag(400, 390, 160, 330, weight=W_SEC)
    g.vbar(300, 60, 390, weight=W_SEC)
    g.hbar(230, 300, hbot(60, W_THIN), weight=W_THIN)
    g.hbar(560, 920, htop(700, W_SEC), weight=W_SEC)
    g.diag(760, 660, 570, 140, weight=W_MAIN)
    g.vbar(850, 140, 660, weight=W_SEC)
    g.hbar(850, 930, hbot(140, W_THIN), weight=W_THIN)
    return g


def _no() -> Glyph:
    """悩 U+60A9 —— 左 忄（x 60..300）＋ 右 亠＋凶（x 340..940）。

    忄：① 左点 dot(96,610,slant=+14) ② 丨 x=175 ③ 右点 dot(280,610,slant=-14)
    亠：④ 丶 dot(640,770,slant=0) ⑤ 一 c=664
    凶：⑥ 左竖 x=420 ⑦ 右竖 x=880 ⑧ 底横 c=106 ⑨ 乂 diag(500,540 → 760,130)
        ⑩ 乂 diag(800,540 → 540,130)
    凶 底横与亠一白口 60 以上；乂在凵内交叉。
    """
    g = Glyph("uni60A9", advance=1000, unicode=0x60A9, note="悩：左忄右亠凶")
    g.dot(96, 610, w=84, h=112, slant=14)
    g.vbar(175, 60, 800, weight=W_MAIN)
    g.dot(282, 610, w=84, h=112, slant=-14)
    g.dot(640, 770, w=84, h=90, slant=0)
    g.hbar(400, 900, htop(710, W_SEC), weight=W_SEC)
    g.vbar(420, 60, 560, weight=W_SEC)
    g.vbar(880, 60, 560, weight=W_SEC)
    g.hbar(420, 880, hbot(60, W_SEC), weight=W_SEC)
    g.diag(500, 540, 760, 130, weight=W_MAIN)
    g.diag(800, 540, 540, 130, weight=W_MAIN)
    return g


def _ka_hana() -> Glyph:
    """華 U+83EF —— 艹（顶，y 740..820）＋ 中 三横两竖 ＋ 末中竖。

    笔画清单：
      ① 艹一 c=778 ② 丨 x=290 ③ 丨 x=710
      ④ 一 c=654（横贯 x 120..880）
      ⑤ 丨 x=290 ⑥ 丨 x=710（y 300..654）
      ⑦ 中竖 x=500（y 96..654）
      ⑧ 一 c=240（x 120..880） ⑨ 一 c=110（x 120..880）
    上下横白口 ≥ 46；中竖把上下分成两列，列宽 118。
    """
    g = Glyph("uni83EF", advance=1000, unicode=0x83EF, note="華：艹下并中竖")
    comp_kusanmuri(g, 60, 940, 820, w=W_SEC, drop=80.0)
    g.hbar(120, 880, htop(700, W_SEC), weight=W_SEC)
    g.vbar(290, 300, 654, weight=W_SEC)
    g.vbar(710, 300, 654, weight=W_SEC)
    g.vbar(500, 96, 654, weight=W_SEC)
    g.hbar(120, 880, htop(286, W_SEC), weight=W_SEC)
    g.hbar(120, 880, htop(156, W_SEC), weight=W_SEC)
    return g


def _go() -> Glyph:
    """御 U+5FA1 —— 左 彳（x 60..250）＋ 中 卸左（x 280..560）＋ 右 卩（x 620..920）。

    彳：① 丿 diag(225,810 → 130,700) ② 丿 diag(230,630 → 110,480) ③ 丨 x=140
    卸左：④ 𠂉之丿 diag(360,800 → 282,700) ⑤ 一 c=634
          ⑥ 丨 x=360 ⑦ 一 c=424 ⑧ 丨 x=480 ⑨ 一 c=254
    卩：⑩ 横折钩 hbar(640..900,c=700)+vbar(878,400..700) ⑪ 丨 x=660
    卸左白口 40/44。
    """
    g = Glyph("uni5FA1", advance=1000, unicode=0x5FA1, note="御：左彳中卸右卩")
    comp_gonin(g, 70.0)
    g.diag(360, 800, 282, 700, weight=W_THIN)
    g.hbar(300, 560, htop(680, W_THIN), weight=W_THIN)
    g.vbar(360, 300, 680, weight=W_THIN)
    g.hbar(360, 560, htop(470, W_THIN), weight=W_THIN)
    g.vbar(480, 300, 470, weight=W_THIN)
    g.hbar(300, 560, htop(300, W_THIN), weight=W_THIN)
    g.hbar(640, 900, htop(700, W_SEC), weight=W_SEC)
    g.vbar(878, 400, 700, weight=W_SEC)
    g.vbar(660, 40, 700, weight=W_SEC)
    return g


def _tetsu() -> Glyph:
    """哲 U+54F2 —— 上 折（y 380..820）＋ 下 口（y 40..300）。

    扌：① 一 c=652 ② 丨 x=210 ③ 提 diag(85,430 → 245,530)
    斤：④ 丿 diag(540,800 → 440,690) ⑤ 丿 diag(520,700 → 390,300)
        ⑥ 一 c=514 ⑦ 丨 x=870
    口：⑧ 上横 ⑨ 下横 ⑩ 左竖 ⑪ 右竖（box 240..760, 40..300）
    口腔高 76 / 腔宽 336。
    """
    g = Glyph("uni54F2", advance=1000, unicode=0x54F2, note="哲：上折下口")
    g.hbar(60, 380, htop(700, W_MAIN), weight=W_MAIN)
    g.vbar(210, 380, 820, weight=W_MAIN)
    g.diag(85, 430, 245, 530, weight=W_MAIN)
    g.diag(540, 800, 440, 690, weight=W_THIN)
    g.diag(520, 700, 390, 300, weight=W_THIN)
    g.hbar(450, 900, htop(560, W_THIN), weight=W_THIN)
    g.vbar(870, 300, 560, weight=W_THIN)
    comp_kuchi(g, 240, 760, 40, 300, w=W_THIN)
    return g


def _shaku() -> Glyph:
    """釈 U+91C8 —— 左 釆（x 60..470）＋ 右 尺（x 500..940）。

    釆：① 丿 diag(360,815 → 235,715) ② 丶 dot(410,760,slant=-14)
        ③ 一 c=590 ④ 丨 x=265 ⑤ 丿 diag(265,540 → 110,360) ⑥ 乀 diag(265,540 → 445,360)
    尺：⑦ 𠃍 hbar(520..900,c=760)+vbar(878,560..760) ⑧ 一 c=514
        ⑨ 丿 diag(720,540 → 560,140) ⑩ 乀 diag(650,480 → 930,150)
    釆 上下留白 ≥ 30；尺内横白口 44。
    """
    g = Glyph("uni91C8", advance=1000, unicode=0x91C8, note="釈：左釆右尺")
    g.diag(360, 815, 235, 715, weight=W_THIN)
    g.dot(410, 760, w=80, h=90, slant=-14)
    g.hbar(70, 460, htop(590, W_THIN), weight=W_THIN)
    g.vbar(265, 330, 700, weight=W_THIN)
    g.diag(265, 540, 110, 360, weight=W_MAIN)
    g.diag(265, 540, 445, 360, weight=W_MAIN)
    g.hbar(520, 900, htop(760, W_THIN), weight=W_THIN)
    g.vbar(878, 560, 760, weight=W_THIN)
    g.hbar(520, 830, htop(560, W_THIN), weight=W_THIN)
    g.diag(720, 540, 560, 140, weight=W_MAIN)
    g.diag(650, 480, 930, 150, weight=W_MAIN)
    return g


def _cho() -> Glyph:
    """貯 U+8CAF —— 左 貝（x 60..420）＋ 右 宁（x 460..940）。

    貝：① 目 上横 c=758 ② 中横 c=648 ③ 中横 c=538 ④ 下横 c=428
        ⑤ 左竖 x=112 ⑥ 右竖 x=368
        ⑦ 八之撇 diag(170,380 → 74,70) ⑧ 八之捺 diag(300,380 → 396,70)
    宁：⑨ 丶 dot(700,782,slant=0) ⑩ 丨 x=520 ⑪ 乛 hbar(520..920,c=700)+钩
        ⑫ 一 c=418 ⑬ 亅 vbar(710,120..418)
    貝 目三腔高 26；宁的横与亅白口 96。
    """
    g = Glyph("uni8CAF", advance=1000, unicode=0x8CAF, note="貯：左貝右宁")
    comp_me(g, 70, 410, 388, 802, w=W_THIN, cav=26.0)
    g.diag(170, 380, 74, 70, weight=W_MAIN)
    g.diag(300, 380, 396, 70, weight=W_MAIN)
    g.dot(700, 782, w=84, h=76, slant=0)
    g.vbar(520, 600, 700, weight=W_SEC)
    g.hbar(520, 920, htop(700, W_SEC), weight=W_SEC)
    g.diag(900, 700, 836, 636, weight=W_SEC)
    g.hbar(540, 880, htop(460, W_THIN), weight=W_THIN)
    g.vbar(710, 120, 460, weight=W_THIN)
    g.hbar(660, 710, hbot(120, W_THIN), weight=W_THIN)
    return g


def _kou() -> Glyph:
    """硬 U+786C —— 左 石（x 60..430）＋ 右 更（x 470..940）。

    石：① 一 c=788 ② 丿 diag(260,740 → 110,486) ③ 口 box(140..400, 60..420)
    更：④ 一 c=778 ⑤ 曰 上横 c=668 ⑥ 中横 c=558 ⑦ 下横 c=490
        ⑧ 左竖 x=500 ⑨ 右竖 x=888 ⑩ 丿 diag(650,460 → 520,60) ⑪ 乀 diag(690,450 → 900,60)
    曰两腔高 26；石口腔高 176 / 腔宽 76。
    """
    g = Glyph("uni786C", advance=1000, unicode=0x786C, note="硬：左石右更")
    g.hbar(60, 430, htop(788, W_MAIN), weight=W_MAIN)
    g.diag(260, 740, 110, 486, weight=W_MAIN)
    comp_kuchi(g, 140, 400, 60, 420, w=W_THIN)
    g.hbar(490, 930, htop(820, W_THIN), weight=W_THIN)
    g.hbar(500, 930, htop(710, W_THIN), weight=W_THIN)
    g.hbar(500, 930, htop(600, W_THIN), weight=W_THIN)
    g.hbar(500, 930, htop(490, W_THIN), weight=W_THIN)
    g.vbar(500, 490, 710, weight=W_THIN)
    g.vbar(888, 490, 710, weight=W_THIN)
    g.diag(650, 460, 520, 60, weight=W_MAIN)
    g.diag(690, 450, 900, 60, weight=W_MAIN)
    return g


def _ha() -> Glyph:
    """歯 U+6B6F —— 上 止（y 558..820）＋ 下 凵包米（y 0..520）。

    止：① 丨 x=500 ② 一 c=740 ③ 丨 x=320 ④ 一 c=610
    凵：⑤ 左竖 x=140 ⑥ 右竖 x=880 ⑦ 底横 c=106
    米：⑧ 一 c=450 ⑨ 丨 x=500 ⑩ 丿 diag(500,470 → 270,200) ⑪ 乀 diag(500,470 → 740,200)
    凵内两格腔高 304，腔宽 ≥ 88。
    """
    g = Glyph("uni6B6F", advance=1000, unicode=0x6B6F, note="歯：上止下凵米")
    g.vbar(500, 658, 820, weight=W_SEC)
    g.hbar(500, 820, htop(788, W_SEC), weight=W_SEC)
    g.vbar(320, 658, 740, weight=W_SEC)
    g.hbar(280, 760, htop(658, W_SEC), weight=W_SEC)
    g.vbar(140, 60, 520, weight=W_SEC)
    g.vbar(880, 60, 520, weight=W_SEC)
    g.hbar(140, 880, hbot(60, W_SEC), weight=W_SEC)
    g.hbar(220, 800, htop(496, W_THIN), weight=W_THIN)
    g.vbar(500, 180, 496, weight=W_THIN)
    g.diag(500, 470, 270, 200, weight=W_MAIN)
    g.diag(500, 470, 740, 200, weight=W_MAIN)
    return g


def _tai() -> Glyph:
    """滞 U+6EDE —— 左 氵（x 60..300）＋ 右 帯（x 330..940）。

    氵：① 短撇 dot(130,668,slant=26) ② 丶 dot(126,438,slant=-14) ③ 提 diag(64,128 → 258,326)
    帯：④ 卅之横 c=778 ⑤ 丨 x=450 ⑥ 丨 x=630 ⑦ 丨 x=810
        ⑧ 冖之丨 x=390 ⑨ 冖之横钩 hbar(390..920,c=644)+钩
        ⑩ 巾之横 c=540 ⑪ 巾之左竖 x=480 ⑫ 巾之右竖 x=800 ⑬ 巾之中竖 x=640
    帯的横白口 30（冖↔巾）、26（卅↔冖）。
    「冖横」与「巾横」白口 28（原本重叠 32 → 巾整组下移 60，中竖下端不动）。
    """
    g = Glyph("uni6EDE", advance=1000, unicode=0x6EDE, note="滞：左氵右帯")
    comp_sanzui(g, 70.0)
    g.hbar(360, 920, htop(820, W_SEC), weight=W_SEC)
    for cx in (450.0, 630.0, 810.0):
        g.vbar(cx, 720, 820, weight=W_SEC)
    g.vbar(390, 590, 644, weight=W_SEC)
    g.hbar(390, 920, htop(644, W_SEC), weight=W_SEC)
    g.diag(900, 644, 836, 580, weight=W_SEC)
    g.hbar(480, 850, htop(524, W_THIN), weight=W_THIN)
    g.vbar(480, 240, 524, weight=W_THIN)
    g.vbar(800, 240, 524, weight=W_THIN)
    g.vbar(640, 60, 540, weight=W_THIN)
    return g


def _bi() -> Glyph:
    """微 U+5FAE —— 左 彳（x 60..250）＋ 中 山＋兀（x 280..640）＋ 右 攵（x 670..940）。

    彳：① 丿 diag(225,800 → 130,694) ② 丿 diag(230,616 → 110,470) ③ 丨 x=150
    山：④ 中竖 x=460 ⑤ 左竖 x=310 ⑥ 右竖 x=610 ⑦ 底横 c=746
    兀：⑧ 一 c=496 ⑨ 丿 diag(430,460 → 320,120) ⑩ 乚 vbar(540,120..460)+右勾
    攵：⑪ 丿 diag(830,800 → 726,690) ⑫ 一 c=640 ⑬ 丿 diag(915,640 → 690,120)
        ⑭ 乀 diag(780,470 → 935,120)
    山底横与兀一白口 150；兀腔高 ≥ 26。
    """
    g = Glyph("uni5FAE", advance=1000, unicode=0x5FAE, note="微：左彳中山兀右攵")
    comp_gonin(g, 70.0)
    g.vbar(460, 580, 820, weight=W_THIN)
    g.vbar(310, 700, 790, weight=W_THIN)
    g.vbar(610, 700, 790, weight=W_THIN)
    g.hbar(310, 610, htop(790, W_THIN), weight=W_THIN)
    g.hbar(300, 630, htop(542, W_THIN), weight=W_THIN)
    g.diag(430, 460, 320, 120, weight=W_MAIN)
    g.vbar(540, 120, 460, weight=W_MAIN)
    g.hbar(540, 620, hbot(120, W_THIN), weight=W_THIN)
    g.diag(830, 800, 726, 690, weight=W_THIN)
    g.hbar(690, 930, htop(686, W_THIN), weight=W_THIN)
    g.diag(915, 686, 690, 120, weight=W_MAIN)
    g.diag(780, 470, 935, 120, weight=W_MAIN)
    return g


def _ryu() -> Glyph:
    """隆 U+9686 —— 左 阝（x 60..240）＋ 右 夂＋一＋生（x 280..940）。

    阝：① 丨 x=110 ② 横 c=762 ③ 弯钩 diag(242,754 → 164,600)
    夂：④ 丿 diag(420,815 → 320,690) ⑤ 𠃍 hbar(390..660,c=680)+diag(660,680 → 520,570)
        ⑥ 乀 diag(560,640 → 720,520)
    一：⑦ hbar(300..900, c=470)
    生：⑧ 丿 diag(430,430 → 360,330) ⑨ 一 c=296 ⑩ 丨 x=620
        ⑪ 一 c=176 ⑫ 一 c=56
    生三横白口 32/32。
    """
    g = Glyph("uni9686", advance=1000, unicode=0x9686, note="隆：左阝右夂一生")
    comp_maru(g, 110.0)
    g.diag(420, 815, 320, 690, weight=W_THIN)
    g.hbar(390, 660, htop(680, W_THIN), weight=W_THIN)
    g.diag(660, 680, 520, 570, weight=W_THIN)
    g.diag(560, 640, 720, 520, weight=W_THIN)
    g.hbar(300, 900, htop(470, W_THIN), weight=W_THIN)
    comp_sei(g, 330, 900, w=W_THIN)
    return g


def _mai() -> Glyph:
    """埋 U+57CB —— 左 土（x 60..340）＋ 右 里（x 380..940）。

    土：① 一 c=580 ② 丨 x=205 ③ 一 c=46
    里：④ 田 上横 c=778 ⑤ 中横 c=608 ⑥ 下横 c=438 ⑦ 左竖 x=432
        ⑧ 右竖 x=888 ⑨ 中竖 x=660 ⑩ 一 c=300 ⑪ 一 c=54
    里 田四腔高 86/86，格宽 136；田下一白口 54。
    """
    g = Glyph("uni57CB", advance=1000, unicode=0x57CB, note="埋：左土右里")
    g.hbar(90, 320, htop(626, W_MAIN), weight=W_MAIN)
    g.vbar(205, 92, 580, weight=W_MAIN)
    g.hbar(60, 340, hbot(0, W_MAIN), weight=W_MAIN)
    comp_den(g, 390, 930, 480, 820, w=W_THIN, cav=26.0)
    g.vbar(660, 96, 480, weight=W_THIN)
    g.hbar(390, 930, htop(342, W_THIN), weight=W_THIN)
    g.hbar(390, 930, htop(96, W_THIN), weight=W_THIN)
    return g


def build() -> list[Glyph]:
    return [
        _do(), _ka(), _shugo(), _yo(), _ben(), _kan(), _yaku(), _hi(),
        _hyou(), _kei(), _yure(), _kizoku(), _no(), _ka_hana(), _go(),
        _tetsu(), _shaku(), _cho(), _kou(), _ha(), _tai(), _bi(), _ryu(),
        _mai(),
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s3-016.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
