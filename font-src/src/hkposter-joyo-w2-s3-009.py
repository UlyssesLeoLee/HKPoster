"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s3-009。

本批 24 字，笔画范围 10–13，取自 2010 年文化厅《常用漢字表》。

整体取舍
--------
* 字面框 x 60..940、y 0..820，advance 1000，与繁体汉字完全一致（中英日混排）。
* 笔画权重只用四档：主 96 / 次 92 / 细 84 / 点 84。密排处（口/日/目/田 的横画）
  降到 84。
* **框高公式（AGENTS.md 铁律 10）**：两条横画之间的白口 = 中心线间距 − 笔画宽。
  本批方框类部件（口/日/目/田）统一用 **W_BOX = 76**（批内密排减压，GLY-001），
  内白目标 **GAP_MIN = 26**：
      口 ≥ 178 · 日 ≥ 280 · 目 ≥ 382 · 田 ≥ 280（笔画宽 76 时）。
  几何腔高 ≥ 26 ⇒ S=700 栅格化量到 ≥ 24，避开 audit_white_holes 的「压扁真腔」门槛
  （几何 24 → 栅格化只量到 23，正好压在门槛上）。本批所有方框按这套数字排布。
* 点 / 短撇的 slant 只用 4 个档：竖点 0、丶（右下的点）−14、丿（左下的点）＋14、
  短撇（氵的上点等）＋26。不自造档位。
* 同族部件在全批复用同一套坐标与笔画拆法（GLY-004）：氵 / 扌 / 木 / 舟 / 女 /
  辶 / 宀 / 口 / 日 / 目 / 田 / 灬，批内只做位置与大小的光学校正。
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
W_BOX = 76   # 方框类部件（口/日/目/田）统一档：批内密排减压（GLY-001）

# slant 分档（只此四档）
S_VERT = 0        # 竖点（亠的点）
S_DOT = -14       # 丶（右下的点：辶的点 / 歹的点 / 厶的点 / 冫的上点 / 寸的点 / 丷左）
S_PIE = 14        # 丿（左下的点：丷右 / 小右点）
S_SHORT_PIE = 26  # 短撇（氵的上点等）

# 相邻横画的最小白口（单位），也是方框内白的目标值
GAP_MIN = 26


# --------------------------------------------------------------------------
# 基础部件（GLY-004：同族复用同一套拆法）
# --------------------------------------------------------------------------
def kou(g, x1, x2, yb, yt, w=W_BOX):
    """口：外框 x1..x2、底 yb、顶 yt（四边同重）。外高须 ≥ 2w+GAP_MIN。"""
    g.hbar(x1, x2, yt - w / 2, weight=w)
    g.hbar(x1, x2, yb + w / 2, weight=w)
    g.vbar(x1 + w / 2, yb, yt, weight=w)
    g.vbar(x2 - w / 2, yb, yt, weight=w)


def ri(g, x1, x2, yb, yt, w=W_BOX):
    """日：口 + 中横（两腔各 ≥ GAP_MIN）。外高须 ≥ 3w+2×GAP_MIN。"""
    kou(g, x1, x2, yb, yt, w)
    step = w + GAP_MIN
    g.hbar(x1, x2, yb + w / 2 + step, weight=w)


def me(g, x1, x2, yb, yt, w=W_BOX):
    """目：口 + 两条中横（三腔各 ≥ GAP_MIN）。外高须 ≥ 4w+3×GAP_MIN。"""
    kou(g, x1, x2, yb, yt, w)
    step = w + GAP_MIN
    g.hbar(x1, x2, yb + w / 2 + step, weight=w)
    g.hbar(x1, x2, yb + w / 2 + 2 * step, weight=w)


def den(g, x1, x2, yb, yt, w=W_BOX):
    """田：日 + 中竖。外高须 ≥ 3w+2×GAP_MIN。"""
    ri(g, x1, x2, yb, yt, w)
    g.vbar((x1 + x2) / 2, yb, yt, weight=w)


def sanzui(g):
    """氵：上点（短撇 26）+ 中点（短撇 26）+ 下提（右上斜）。全批统一。"""
    g.dot(195, 690, w=W_MAIN, h=126, slant=S_SHORT_PIE)
    g.dot(150, 490, w=W_MAIN, h=126, slant=S_SHORT_PIE)
    g.diag(90, 118, 240, 223, weight=W_MAIN)


def tehen(g):
    """扌：一 + 亅（带钩）+ 提。"""
    g.hbar(70, 320, 580, weight=W_SEC)
    g.vbar(200, 180, 780, weight=W_SEC)
    g.diag(200, 192, 152, 150, weight=W_THIN)  # 亅 的钩
    g.diag(72, 330, 272, 428, weight=W_SEC)   # 提


def ki_radical(g):
    """木（偏旁形，捺改短斜）：一 + 丨 + 丿 + 短捺。"""
    g.hbar(70, 340, 600, weight=W_SEC)
    g.vbar(205, 60, 780, weight=W_SEC)
    g.diag(200, 580, 80, 80, weight=W_SEC)
    g.diag(212, 560, 316, 214, weight=W_SEC)


def fune(g):
    """舟（旁形）：丿 + 顶横 + 右竖 + 左竖 + 中横 + 上下两点。般 / 航 共用。"""
    g.diag(175, 780, 95, 690, weight=W_MAIN)
    g.hbar(130, 390, 760, weight=W_MAIN)
    g.vbar(342, 380, 760, weight=W_MAIN)
    g.vbar(118, 380, 712, weight=W_MAIN)
    g.hbar(60, 390, 545, weight=W_THIN)
    g.dot(240, 648, w=W_DOT, h=90, slant=S_DOT)
    g.dot(250, 450, w=W_DOT, h=90, slant=S_DOT)


def onna(g):
    """女（旁形）：撇点 + 长撇 + 横。"""
    g.diag(240, 770, 130, 430, weight=W_SEC)
    g.diag(340, 700, 120, 100, weight=W_SEC)
    g.hbar(70, 360, 430, weight=W_SEC)


def hen_zou(g, sweep_to=(470, 50)):
    """辶（旁形）：丶（−14）+ 中段斜画 + 底部长捺。遣 / 適 共用。"""
    g.dot(140, 760, w=W_SEC, h=100, slant=S_DOT)
    g.diag(215, 690, 105, 545, weight=W_SEC)
    g.diag(95, 310, sweep_to[0], sweep_to[1], weight=W_SEC)


def ura(g, cx=500, dot_cy=778, roof_y=700, x1=90, x2=910):
    """宀：竖点（0）+ 顶横 + 左竖点 + 右钩。富 / 寄 共用。"""
    g.dot(cx, dot_cy, w=W_DOT, h=48, slant=S_VERT)
    g.hbar(x1, x2, roof_y, weight=W_THIN)
    g.vbar(x1 + 48, roof_y - 94, roof_y, weight=W_THIN)
    g.vbar(x2 - 48, roof_y - 56, roof_y, weight=W_THIN)


def hoton(g, xs, cy=90, h=110):
    """灬：四点（丶 −14）。馬 用。"""
    for x in xs:
        g.dot(x, cy, w=W_DOT, h=h, slant=S_DOT)


# --------------------------------------------------------------------------
# 24 字
# --------------------------------------------------------------------------
def g_xian():
    """献（732E，13画）：左「南」右「犬」。

    南（x 60..420）：十（竖 x=250 y 680..820；横 y=700 x 170..330）
        冂（顶横 y=560 x 60..420；左竖 x=108；右竖 x=372，y 60..560）
        内部 丷（左点 185/430 短撇 26；右短撇 300/430 ＋14）
        ＋ 十（横 y=300 x 140..340；竖 x=240 y 120..340）
    犬（x 450..940）：撇 (700,780)→(470,80)；横 y=580 x 570..870；
        捺 (610,540)→(910,90)；点 (820,700) ＋14
    """
    g = Glyph("uni732E", advance=1000, unicode=0x732E, note="献：南＋犬")
    # —— 南 ——
    g.vbar(250, 680, 820, weight=W_MAIN)
    g.hbar(170, 330, 700, weight=W_MAIN)
    g.hbar(60, 420, 560, weight=W_MAIN)
    g.vbar(108, 60, 560, weight=W_MAIN)
    g.vbar(372, 60, 560, weight=W_MAIN)
    g.hbar(140, 340, 300, weight=W_THIN)
    g.vbar(240, 120, 340, weight=W_THIN)
    g.dot(185, 430, w=W_DOT, h=100, slant=S_SHORT_PIE)
    g.dot(300, 430, w=W_DOT, h=100, slant=S_PIE)
    # —— 犬 ——
    g.diag(700, 780, 470, 80, weight=W_MAIN)
    g.hbar(570, 870, 580, weight=W_MAIN)
    g.diag(610, 540, 910, 90, weight=W_MAIN)
    g.dot(820, 700, w=W_SEC, h=110, slant=S_PIE)
    return g


def g_uma():
    """馬（99AC，10画）：上部「ヨ＋长横」，下部「灬」。

    左竖 x=120 y 340..820；顶横 y=772 x 72..868；右竖 x=820 y 340..772；
    内横 y=640 / y=508（x 72..820）；长横 y=376 x 60..880；
    下左竖 x=120 y 180..376；灬 四点 y=90，x 250/430/610/790
    """
    g = Glyph("uni99AC", advance=1000, unicode=0x99AC, note="馬：ヨ＋長横＋灬")
    g.vbar(120, 340, 820, weight=W_SEC)
    g.hbar(72, 868, 772, weight=W_SEC)
    g.vbar(820, 340, 772, weight=W_SEC)
    g.hbar(72, 820, 640, weight=W_THIN)
    g.hbar(72, 820, 508, weight=W_THIN)
    g.hbar(60, 880, 376, weight=W_SEC)
    g.vbar(120, 180, 376, weight=W_SEC)
    hoton(g, (250, 430, 610, 790))
    return g


def g_haba():
    """幅（5E45，12画）：左「巾」右「畐」。

    巾（x 60..330）：顶横 y=760；左竖 x=108 y 420..760；右竖 x=282；中竖 x=195 y 100..820
    畐（x 370..940）：一 y=772 x 370..940；口 x 470..840（外高 520..698，内白 26）；
        田 x 440..870（外高 214..494，内白 26/26）+ 中竖 x=655
    """
    g = Glyph("uni5E45", advance=1000, unicode=0x5E45, note="幅：巾＋畐")
    # —— 巾 ——
    g.hbar(60, 330, 760, weight=W_MAIN)
    g.vbar(108, 420, 760, weight=W_MAIN)
    g.vbar(282, 420, 760, weight=W_MAIN)
    g.vbar(195, 100, 820, weight=W_MAIN)
    # —— 畐 ——
    g.hbar(370, 940, 772, weight=W_MAIN)
    kou(g, 470, 840, 520, 698, W_BOX)
    den(g, 440, 870, 214, 494, W_BOX)
    return g


def g_tomi():
    """富（5BCC，12画）：上「宀」下「畐」。

    宀：竖点 (500,778)；顶横 y=690 x 90..910；左竖点 x=138；右钩 x=862
    畐：一 y=571 x 230..770；口 x 280..720（外高 316..494，内白 26）；
        田 x 260..740（外高 0..280，内白 26/26）+ 中竖 x=500
    """
    g = Glyph("uni5BCC", advance=1000, unicode=0x5BCC, note="富：宀＋畐")
    ura(g, cx=500, dot_cy=778, roof_y=690)
    g.hbar(230, 770, 571, weight=W_THIN)
    kou(g, 280, 720, 316, 494, W_BOX)
    den(g, 260, 740, 0, 280, W_BOX)
    return g


def g_hama():
    """浜（6D5C，10画）：左「氵」右「兵」。

    氵：上点 (195,690) 短撇 26；中点 (150,490) 短撇 26；下提 (90,118)→(240,223)
    兵（x 290..940）：短撇 (480,800)→(390,706)；横 y=660 x 380..830；
        竖 x=470 y 500..660；长横 y=452 x 330..900；短横 y=300 x 470..740；
        八：撇 (560,300)→(390,60)；捺 (650,300)→(860,60)
    """
    g = Glyph("uni6D5C", advance=1000, unicode=0x6D5C, note="浜：氵＋兵")
    sanzui(g)
    g.diag(480, 800, 390, 706, weight=W_MAIN)
    g.hbar(380, 830, 660, weight=W_MAIN)
    g.vbar(470, 500, 660, weight=W_MAIN)
    g.hbar(330, 900, 452, weight=W_MAIN)
    g.hbar(470, 740, 300, weight=W_THIN)
    g.diag(560, 300, 390, 60, weight=W_MAIN)
    g.diag(650, 300, 860, 60, weight=W_MAIN)
    return g


def g_han():
    """般（822C，10画）：左「舟」右「殳」。

    舟：见 fune()
    殳（x 430..940）：几（撇 (545,745)→(450,570)；横 y=740 x 540..780；竖 x=732 y 540..740）
        又（横 y=480 x 490..810；撇 (810,480)→(540,70)；捺 (560,430)→(910,70)）
    """
    g = Glyph("uni822C", advance=1000, unicode=0x822C, note="般：舟＋殳")
    fune(g)
    # —— 几 ——
    g.diag(545, 745, 450, 570, weight=W_MAIN)
    g.hbar(540, 780, 740, weight=W_MAIN)
    g.vbar(732, 540, 740, weight=W_MAIN)
    # —— 又 ——
    g.hbar(490, 810, 480, weight=W_MAIN)
    g.diag(810, 480, 540, 70, weight=W_MAIN)
    g.diag(560, 430, 910, 70, weight=W_MAIN)
    return g


def g_rui():
    """塁（5841，12画）：上「日」中「田」下「土」。

    日（x 330..670）：外高 540..820，两腔各 26
    田（x 200..800）：外高 226..506，两腔各 26 + 中竖 x=500
    土：一 y=150 x 340..660；一 y=42 x 220..780；竖 x=500 y 42..150
    """
    g = Glyph("uni5841", advance=1000, unicode=0x5841, note="塁：日＋田＋土")
    ri(g, 330, 670, 540, 820, W_BOX)
    den(g, 200, 800, 226, 506, W_BOX)
    g.hbar(340, 660, 150, weight=W_THIN)
    g.hbar(220, 780, 42, weight=W_THIN)
    g.vbar(500, 42, 150, weight=W_THIN)
    return g


def g_bou():
    """貿（8CBF，12画）：上「卯」下「貝」。

    卯（x 140..860）：左（撇 (250,800)→(160,700)；竖 x=160 y 560..700；提 (160,560)→(330,630)）
        右卩（横 y=740 x 560..800；竖 x=752 y 560..740；竖 x=608 y 500..740）
    貝（x 240..760）：目（外高 80..462，三腔各 26）+ 八（撇 (370,112)→(258,40)；捺 (630,110)→(745,40)）

    夹缝修正：目下腔（腔底 156 / 腔顶 182）与八的两笔起笔必须错开 ——
    原「目 60..468 + 八起笔 y=125」时八的捺尖恰好落在腔顶上（657.3,162），
    轮廓在该点自交（check_glyphs FAIL）。现目提到 80..462，
    八的起笔压到 y=112/110，笔尖最高 150.2 / 149.3 < 腔底 156 ⇒ 不再侵入腔内。
    """
    g = Glyph("uni8CBF", advance=1000, unicode=0x8CBF, note="貿：卯＋貝")
    # —— 卯 ——
    g.diag(250, 800, 160, 700, weight=W_SEC)
    g.vbar(160, 560, 700, weight=W_SEC)
    g.diag(160, 560, 330, 630, weight=W_SEC)
    g.hbar(560, 800, 740, weight=W_SEC)
    g.vbar(752, 560, 740, weight=W_SEC)
    g.vbar(608, 500, 740, weight=W_SEC)
    # —— 貝 ——
    me(g, 240, 760, 80, 462, W_BOX)
    g.diag(370, 112, 258, 40, weight=W_SEC)
    g.diag(630, 110, 745, 40, weight=W_SEC)
    return g


def g_sou():
    """装（88C5，12画）：左上「壮」右下「衣」。

    壮（x 60..520）：丬（点 (120,745) ＋14；提 (95,570)→(215,620)；竖 x=270 y 520..820）
        士（横 y=660 x 350..510；竖 x=430 y 520..660；横 y=520 x 365..495）
    衣（x 190..880）：竖点 (560,490)；横 y=390 x 300..820；
        撇 (460,400)→(190,60)；竖 x=420 y 110..400；提 (420,120)→(560,190)；
        撇 (700,380)→(580,200)；捺 (640,380)→(880,60)
    """
    g = Glyph("uni88C5", advance=1000, unicode=0x88C5, note="装：壮＋衣")
    # —— 壮 ——
    g.dot(120, 745, w=W_SEC, h=112, slant=S_PIE)
    g.diag(95, 570, 215, 620, weight=W_SEC)
    g.vbar(270, 520, 820, weight=W_SEC)
    g.hbar(350, 510, 660, weight=W_SEC)
    g.vbar(430, 520, 660, weight=W_SEC)
    g.hbar(365, 495, 520, weight=W_SEC)
    # —— 衣 ——
    g.dot(560, 490, w=W_SEC, h=84, slant=S_VERT)
    g.hbar(300, 820, 390, weight=W_SEC)
    g.diag(460, 400, 190, 60, weight=W_SEC)
    g.vbar(420, 110, 400, weight=W_SEC)
    g.diag(420, 120, 560, 190, weight=W_THIN)
    g.diag(700, 380, 580, 200, weight=W_THIN)
    g.diag(640, 380, 880, 60, weight=W_SEC)
    return g


def g_natsu():
    """夏（590F，10画）：上「一＋日」下「夂」。

    一 y=772 x 200..800；日（x 260..740：外高 420..700，两腔各 26）
    夂（x 270..820）：撇 (380,375)→(280,285)；横 y=310 x 330..700；
        撇 (700,290)→(400,40)；捺 (420,245)→(820,40)

    夹缝修正：原「撇 (380,355)→(280,265) + 横 y=290」让横下缘(244)与
    长撇/捺的交点(553.85, 228.09)只差 16 单位 → 挤出一个 16 高的假腔。
    现把横提到 y=310（下缘 264），并把短撇抬到 (380,375)，
    交点不变 ⇒ 楔形腔高 264−228.09 = 36。
    """
    g = Glyph("uni590F", advance=1000, unicode=0x590F, note="夏：一＋日＋夂")
    g.hbar(200, 800, 772, weight=W_SEC)
    ri(g, 260, 740, 420, 700, W_BOX)
    g.diag(380, 375, 280, 285, weight=W_SEC)
    g.hbar(330, 700, 310, weight=W_SEC)
    g.diag(700, 290, 400, 40, weight=W_SEC)
    g.diag(420, 245, 820, 40, weight=W_SEC)
    return g


def g_su():
    """素（7D20，10画）：上「龶」下「糸」。

    龶：横 y=772 x 330..670；横 y=650 x 270..730；竖 x=500 y 480..772；横 y=528 x 200..800
    糸（x 330..600）：撇 (545,455)→(470,395)；撇 (505,440)→(375,330)；折 (375,330)→(490,368)；
        点 (555,330) −14；竖 x=470 y 60..280；钩 (470,75)→(415,105)；
        撇 (425,250)→(330,140)；点 (570,190) −14
    """
    g = Glyph("uni7D20", advance=1000, unicode=0x7D20, note="素：龶＋糸")
    g.hbar(330, 670, 772, weight=W_SEC)
    g.hbar(270, 730, 650, weight=W_SEC)
    g.vbar(500, 480, 772, weight=W_SEC)
    g.hbar(200, 800, 528, weight=W_SEC)
    g.diag(545, 455, 470, 395, weight=W_THIN)
    g.diag(505, 440, 375, 330, weight=W_THIN)
    g.diag(375, 330, 490, 368, weight=W_THIN)
    g.dot(555, 330, w=W_DOT, h=100, slant=S_DOT)
    g.vbar(470, 60, 280, weight=W_THIN)
    g.diag(470, 75, 415, 105, weight=W_THIN)
    g.diag(425, 250, 330, 140, weight=W_THIN)
    g.dot(570, 190, w=W_DOT, h=100, slant=S_DOT)
    return g


def g_ken():
    """遣（9063，12画）：左下「辶」右上「中＋一＋口」。

    辶：见 hen_zou()（捺尾 (470,50)）
    中（x 420..780）：口（外高 594..772）+ 竖 x=600 y 490..820
    一 y=510 x 420..780；口（x 420..780：外高 266..444）
    """
    g = Glyph("uni9063", advance=1000, unicode=0x9063, note="遣：辶＋中＋一＋口")
    hen_zou(g, sweep_to=(470, 50))
    kou(g, 420, 780, 594, 772, W_BOX)
    g.vbar(600, 490, 820, weight=W_SEC)
    g.hbar(420, 780, 510, weight=W_THIN)
    kou(g, 420, 780, 266, 444, W_BOX)
    return g


def g_kou():
    """航（822A，10画）：左「舟」右「亢」。

    舟：见 fune()
    亢（x 430..940）：竖点 (670,786)；横 y=690 x 470..900；
        撇 (560,580)→(480,300)；横 y=580 x 540..800；竖 x=754 y 260..580；钩 (754,275)→(845,310)
    """
    g = Glyph("uni822A", advance=1000, unicode=0x822A, note="航：舟＋亢")
    fune(g)
    g.dot(670, 786, w=W_DOT, h=64, slant=S_VERT)
    g.hbar(470, 900, 690, weight=W_SEC)
    g.diag(560, 580, 480, 300, weight=W_SEC)
    g.hbar(540, 800, 580, weight=W_SEC)
    g.vbar(754, 260, 580, weight=W_SEC)
    g.diag(754, 275, 845, 310, weight=W_THIN)
    return g


def g_yu():
    """雄（96C4，12画）：左「厷」右「隹」。

    厷（x 60..380）：横 y=700 x 100..340；撇 (260,780)→(90,560)；
        厶（撇 (330,540)→(150,390)；横 y=344 x 150..340；点 (320,500) −14）
    隹（x 430..900）：撇 (520,800)→(430,660)；竖 x=455 y 180..660；竖 x=700 y 180..740；
        横 y=740 / 620 / 500 x 500..880；横 y=380 x 480..900
    """
    g = Glyph("uni96C4", advance=1000, unicode=0x96C4, note="雄：厷＋隹")
    # —— 厷 ——
    g.hbar(100, 340, 700, weight=W_SEC)
    g.diag(260, 780, 90, 560, weight=W_SEC)
    g.diag(330, 540, 150, 390, weight=W_SEC)
    g.hbar(150, 340, 344, weight=W_SEC)
    g.dot(320, 500, w=W_DOT, h=100, slant=S_DOT)
    # —— 隹 ——
    g.diag(520, 800, 430, 660, weight=W_SEC)
    g.vbar(455, 180, 660, weight=W_SEC)
    g.vbar(700, 180, 740, weight=W_SEC)
    g.hbar(500, 880, 740, weight=W_SEC)
    g.hbar(500, 880, 620, weight=W_SEC)
    g.hbar(500, 880, 500, weight=W_SEC)
    g.hbar(480, 900, 380, weight=W_SEC)
    return g


def g_tekki():
    """適（9069，13画）：左下「辶」右上「啇」。

    辶：见 hen_zou()（捺尾 (540,45)）
    啇（x 370..900）：竖点 (620,778)；横 y=676 x 370..900；丷（左点 (470,570) −14；右撇 (740,570) ＋14）；
        冂（横 y=466 x 370..880；左竖 x=416 y 130..466；右竖 x=834 y 130..466）；
        十（横 y=352 x 460..800；竖 x=630 y 260..400）；口（x 500..760：外高 96..274）

    夹缝修正：原「冂横 y=460（下缘 414）」与「十横 y=352（上缘 394）」只差 20 单位
    → 挤出一个 20 高的假腔。现把 冂横提到 y=466（下缘 420），白口 420−394 = 26。
    """
    g = Glyph("uni9069", advance=1000, unicode=0x9069, note="適：辶＋啇")
    hen_zou(g, sweep_to=(540, 45))
    g.dot(620, 778, w=W_SEC, h=72, slant=S_VERT)
    g.hbar(370, 900, 676, weight=W_SEC)
    g.dot(470, 570, w=W_DOT, h=64, slant=S_DOT)
    g.dot(740, 570, w=W_DOT, h=64, slant=S_PIE)
    g.hbar(370, 880, 466, weight=W_SEC)
    g.vbar(416, 130, 466, weight=W_SEC)
    g.vbar(834, 130, 466, weight=W_SEC)
    g.hbar(460, 800, 352, weight=W_THIN)
    g.vbar(630, 260, 400, weight=W_THIN)
    kou(g, 500, 760, 96, 274, W_BOX)
    return g


def g_bu():
    """婦（5A66，11画）：左「女」右「帚」。

    女：见 onna()
    帚（x 420..940）：彐（横 y=772 x 460..900；竖 x=854 y 530..772；横 y=660 x 460..860；横 y=548 x 460..880）；
        冖（横 y=450 x 420..920；竖 x=458 y 360..450）；巾（横 y=330 x 470..900；竖 x=512 y 130..330；
        竖 x=828 y 130..330；中竖 x=670 y 60..430）
    """
    g = Glyph("uni5A66", advance=1000, unicode=0x5A66, note="婦：女＋帚")
    onna(g)
    # —— 彐 ——
    g.hbar(460, 900, 772, weight=W_SEC)
    g.vbar(854, 530, 772, weight=W_SEC)
    g.hbar(460, 860, 660, weight=W_THIN)
    g.hbar(460, 880, 548, weight=W_SEC)
    # —— 冖 ——
    g.hbar(420, 920, 450, weight=W_SEC)
    g.vbar(458, 360, 450, weight=W_THIN)
    # —— 巾 ——
    g.hbar(470, 900, 330, weight=W_SEC)
    g.vbar(512, 130, 330, weight=W_THIN)
    g.vbar(828, 130, 330, weight=W_THIN)
    g.vbar(670, 60, 430, weight=W_SEC)
    return g


def g_tetsu():
    """鉄（9244，13画）：左「釒」右「失」。

    釒（x 60..400）：人（撇 (230,800)→(75,620)；捺 (230,800)→(385,620)）；
        横 y=575 x 130..330；竖 x=230 y 300..575；横 y=460 x 130..330；
        丷（左点 (160,350) −14；右撇 (300,350) ＋14）；横 y=230 x 100..360
    失（x 440..940）：撇 (560,800)→(485,705)；横 y=670 x 480..870；竖 x=660 y 380..740；
        横 y=500 x 440..920；撇 (655,450)→(470,90)；捺 (665,450)→(905,90)
    """
    g = Glyph("uni9244", advance=1000, unicode=0x9244, note="鉄：釒＋失")
    # —— 釒 ——
    g.diag(230, 800, 75, 620, weight=W_SEC)
    g.diag(230, 800, 385, 620, weight=W_SEC)
    g.hbar(130, 330, 575, weight=W_THIN)
    g.vbar(230, 300, 575, weight=W_SEC)
    g.hbar(130, 330, 460, weight=W_THIN)
    g.dot(160, 350, w=W_DOT, h=100, slant=S_DOT)
    g.dot(300, 350, w=W_DOT, h=100, slant=S_PIE)
    g.hbar(100, 360, 230, weight=W_THIN)
    # —— 失 ——
    g.diag(560, 800, 485, 705, weight=W_SEC)
    g.hbar(480, 870, 670, weight=W_SEC)
    g.vbar(660, 380, 740, weight=W_SEC)
    g.hbar(440, 920, 500, weight=W_SEC)
    g.diag(655, 450, 470, 90, weight=W_SEC)
    g.diag(665, 450, 905, 90, weight=W_SEC)
    return g


def g_ki():
    """寄（5BC4，11画）：上「宀」中「大」下「可」。

    宀：见 ura()（顶横 y=700）
    大：横 y=586 x 240..760；撇 (540,575)→(300,420)；捺 (460,575)→(700,420)
    可：横 y=470 x 240..900；口（x 280..620：外高 226..404）；竖 x=856 y 60..470；钩横 y=60 x 780..856
    """
    g = Glyph("uni5BC4", advance=1000, unicode=0x5BC4, note="寄：宀＋奇")
    ura(g, cx=500, dot_cy=782, roof_y=700)
    # —— 大 ——
    g.hbar(240, 760, 586, weight=W_MAIN)
    g.diag(540, 575, 300, 420, weight=W_SEC)
    g.diag(460, 575, 700, 420, weight=W_SEC)
    # —— 可 ——
    g.hbar(240, 900, 470, weight=W_THIN)
    kou(g, 280, 620, 226, 404, W_BOX)
    g.vbar(856, 60, 470, weight=W_SEC)
    g.hbar(780, 856, 60, weight=W_THIN)
    return g


def g_eku():
    """益（76CA，10画）：上「丷」＋「一」＋「八」下「皿」。

    丷：左点 (380,760) −14；右撇 (620,760) ＋14
    一 y=650 x 200..800
    八：撇 (440,595)→(330,480)；捺 (560,595)→(670,480)
    皿（x 200..800）：横 y=420；竖 x=242 / 460 / 540 / 758（y 90..420）；底横 y=90
    """
    g = Glyph("uni76CA", advance=1000, unicode=0x76CA, note="益：丷＋一＋八＋皿")
    g.dot(380, 760, w=W_SEC, h=110, slant=S_DOT)
    g.dot(620, 760, w=W_SEC, h=110, slant=S_PIE)
    g.hbar(200, 800, 650, weight=W_SEC)
    g.diag(440, 595, 330, 480, weight=W_SEC)
    g.diag(560, 595, 670, 480, weight=W_SEC)
    g.hbar(200, 800, 420, weight=W_THIN)
    g.vbar(242, 90, 420, weight=W_THIN)
    g.vbar(460, 90, 420, weight=W_THIN)
    g.vbar(540, 90, 420, weight=W_THIN)
    g.vbar(758, 90, 420, weight=W_THIN)
    g.hbar(200, 800, 90, weight=W_SEC)
    return g


def g_kin():
    """禁（7981，13画）：上「林」下「示」。

    林（x 60..930）：左木（横 y=640 x 70..430；竖 x=250 y 400..820；撇 (245,620)→(85,410)；捺 (255,600)→(390,420)）
        右木（横 y=640 x 500..930；竖 x=715 y 400..820；撇 (710,620)→(520,410)；捺 (720,600)→(920,410)）
    示（x 250..750）：横 y=300 x 330..670；横 y=180 x 280..720；竖 x=500 y 20..180；
        撇 (420,120)→(330,20)；点 (600,90) −14
    """
    g = Glyph("uni7981", advance=1000, unicode=0x7981, note="禁：林＋示")
    # —— 林 ——
    g.hbar(70, 430, 640, weight=W_SEC)
    g.vbar(250, 400, 820, weight=W_SEC)
    g.diag(245, 620, 85, 410, weight=W_SEC)
    g.diag(255, 600, 390, 420, weight=W_SEC)
    g.hbar(500, 930, 640, weight=W_SEC)
    g.vbar(715, 400, 820, weight=W_SEC)
    g.diag(710, 620, 520, 410, weight=W_SEC)
    g.diag(720, 600, 920, 410, weight=W_SEC)
    # —— 示 ——
    g.hbar(330, 670, 300, weight=W_SEC)
    g.hbar(280, 720, 180, weight=W_SEC)
    g.vbar(500, 20, 180, weight=W_SEC)
    g.diag(420, 120, 330, 20, weight=W_THIN)
    g.dot(600, 90, w=W_DOT, h=100, slant=S_DOT)
    return g


def g_kan():
    """換（63DB，12画）：左「扌」右「奐」。

    扌：见 tehen()
    奐（x 390..930）：⺈（撇 (600,810)→(490,715）；横 y=760 x 560..760；竖 x=714 y 660..760）；
        冂（横 y=620 x 420..900；竖 x=466 y 280..620；竖 x=854 y 280..620）；
        一 y=500 x 470..850；人（撇 (655,470)→(540,290)；捺 (655,470)→(790,290)）；
        八（撇 (530,290)→(390,60)；捺 (780,290)→(920,60)）
    """
    g = Glyph("uni63DB", advance=1000, unicode=0x63DB, note="換：扌＋奐")
    tehen(g)
    g.diag(600, 810, 490, 715, weight=W_SEC)
    g.hbar(560, 760, 760, weight=W_SEC)
    g.vbar(714, 660, 760, weight=W_SEC)
    g.hbar(420, 900, 620, weight=W_SEC)
    g.vbar(466, 280, 620, weight=W_SEC)
    g.vbar(854, 280, 620, weight=W_SEC)
    g.hbar(470, 850, 500, weight=W_THIN)
    g.diag(655, 470, 540, 290, weight=W_SEC)
    g.diag(655, 470, 790, 290, weight=W_SEC)
    g.diag(530, 290, 390, 60, weight=W_SEC)
    g.diag(780, 290, 920, 60, weight=W_SEC)
    return g


def g_tan():
    """短（77ED，12画）：左「矢」右「豆」。

    矢（x 60..430）：撇 (230,800)→(130,700)；横 y=680 x 110..390；横 y=540 x 80..420；
        撇 (300,530)→(110,90)；捺 (300,530)→(430,120)
    豆（x 480..940）：横 y=772 x 490..930；口（x 530..890：外高 522..700）；
        丷（左点 (610,400) −14；右撇 (810,400) ＋14）；横 y=230 x 480..940
    """
    g = Glyph("uni77ED", advance=1000, unicode=0x77ED, note="短：矢＋豆")
    # —— 矢 ——
    g.diag(230, 800, 130, 700, weight=W_SEC)
    g.hbar(110, 390, 680, weight=W_SEC)
    g.hbar(80, 420, 540, weight=W_SEC)
    g.diag(300, 530, 110, 90, weight=W_SEC)
    g.diag(300, 530, 430, 120, weight=W_SEC)
    # —— 豆 ——
    g.hbar(490, 930, 772, weight=W_SEC)
    kou(g, 530, 890, 522, 700, W_BOX)
    g.dot(610, 400, w=W_DOT, h=100, slant=S_DOT)
    g.dot(810, 400, w=W_DOT, h=100, slant=S_PIE)
    g.hbar(480, 940, 230, weight=W_SEC)
    return g


def g_hi():
    """廃（5EC3，12画）：外「广」内「発」。

    广：点 (180,770) 0；横 y=690 x 100..940；撇 (140,690)→(55,80)
    発（x 250..930）：癶（横 y=590 x 250..480；撇 (480,590)→(330,420)；
        撇 (780,590)→(660,430)；点 (870,510) −14）；横 y=400 x 260..900；
        撇 (430,400)→(330,120)；竖 x=640 y 120..400；钩 (640,130)→(760,170)
    """
    g = Glyph("uni5EC3", advance=1000, unicode=0x5EC3, note="廃：广＋発")
    # —— 广 ——
    g.dot(180, 770, w=W_SEC, h=80, slant=S_VERT)
    g.hbar(100, 940, 690, weight=W_SEC)
    g.diag(140, 690, 55, 80, weight=W_SEC)
    # —— 発 ——
    g.hbar(250, 480, 590, weight=W_THIN)
    g.diag(480, 590, 330, 420, weight=W_THIN)
    g.diag(780, 590, 660, 430, weight=W_THIN)
    g.dot(870, 510, w=W_DOT, h=100, slant=S_DOT)
    g.hbar(260, 900, 400, weight=W_THIN)
    g.diag(430, 400, 330, 120, weight=W_THIN)
    g.vbar(640, 120, 400, weight=W_THIN)
    g.diag(640, 130, 760, 170, weight=W_THIN)
    return g


def g_shoku():
    """植（690D，12画）：左「木」右「直」。

    木：见 ki_radical()
    直（x 380..940）：十（横 y=772 x 430..880；竖 x=655 y 620..820）；
        目（x 420..900：外高 320..702，三腔各 26）；横 y=200 x 380..940
    """
    g = Glyph("uni690D", advance=1000, unicode=0x690D, note="植：木＋直")
    ki_radical(g)
    g.hbar(430, 880, 772, weight=W_SEC)
    g.vbar(655, 620, 820, weight=W_SEC)
    me(g, 420, 900, 320, 702, W_BOX)
    g.hbar(380, 940, 200, weight=W_SEC)
    return g


def build() -> list[Glyph]:
    return [
        g_xian(),   # 献
        g_uma(),    # 馬
        g_haba(),   # 幅
        g_tomi(),   # 富
        g_hama(),   # 浜
        g_han(),    # 般
        g_rui(),    # 塁
        g_bou(),    # 貿
        g_sou(),    # 装
        g_natsu(),  # 夏
        g_su(),     # 素
        g_ken(),    # 遣
        g_kou(),    # 航
        g_yu(),     # 雄
        g_tekki(),  # 適
        g_bu(),     # 婦
        g_tetsu(),  # 鉄
        g_ki(),     # 寄
        g_eku(),    # 益
        g_kin(),    # 禁
        g_kan(),    # 換
        g_tan(),    # 短
        g_hi(),     # 廃
        g_shoku(),  # 植
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s3-009.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
