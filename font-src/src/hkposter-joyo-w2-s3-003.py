"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s3-003。

本批 24 字，笔画范围 10–13，取自 2010 年文化厅《常用漢字表》。

设计取舍（整体）
----------------
1. 字面框 x 60..940、y 0..820，advance 固定 1000（与繁体汉字同框，便于中英日混排）。
2. 权重档：主 96 / 次 92 / 细 84 / 点 84–96（与 zh-HK 繁体同一档）。
   笔画少的字（特 10 画、挙 10 画、真 10 画）用足 96；
   笔画多且密排的字（感 13 画、勢 13 画、置 13 画、歳 13 画、減 12 画）
   在拥挤处局部减重到 84，保住内白（GLY-001 允许小空腔局部减重）。
3. 密排处（横画叠横画）内白 ≥ 24 单位；竖与竖之间的字腔 ≥ 60 单位（GLY-006）。
   具体数字写在每个字的 docstring 里，便于复核。
4. **斜切只用在点/短撇/记号**（GLY-003），档位只用工程约定的
   26 / 22 / 20 / 18 / 16 / 14 / −14 / 0，不自造档位；
   同类部件在全族用同一档（GLY-004）：
     氵的上点/下点（短撇）= 26
     丷左 = −14，丷右 = +14
     辶的点 / 歹的点 / 厶的点 / 冫的上点 / 寸的点 = −14
     亠的点（竖点）= 0
5. **笔画的角度不可改**：每条斜笔、每一道横竖都照标准骨架落位，
   只在重量档位、端点处理、部件落位与大小上做光学校正。
6. 同一部件（咸、辶、木、口、氵、忄…）在批内复用同一套笔画拆法，
   只做位置与大小的光学校正（GLY-004）。
7. 横画是「中心线 + 垂直权重」：要让墨迹上缘对齐 820 / 下缘对齐 0，
   中心线必须内缩半个笔画宽 —— 故本 recipe 自带 `bar_top` / `bar_base`
   两个对齐辅助函数（思路同 hkposter-latin.py）。
8. 坐标全部取整；只用 hkbuild 与标准库；recipe 为纯函数，生成物确定。

运行：python font-src/src/hkposter-joyo-w2-s3-003.py
"""

from __future__ import annotations

import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, write_ufo  # noqa: E402

# ---- 冻结权重（日本語漢字：主 96 / 次 92 / 细 84 / 点 84–96）----
W_MAIN = 96
W_SEC = 92
W_THIN = 84
W_DOT = 84

# ---- 字面框 ----
CJK_TOP = 820
CJK_BOT = 0
XL, XR = 60, 940


# -------------------------------------------------------------- 对齐辅助
def bar_top(g: Glyph, x1: float, x2: float, weight: float = W_MAIN) -> None:
    """横画：墨迹上缘对齐 820（中心线内缩半个笔画宽）。"""
    g.hbar(x1, x2, CJK_TOP - weight / 2.0, weight)


def bar_base(g: Glyph, x1: float, x2: float, weight: float = W_MAIN) -> None:
    """横画：墨迹下缘对齐 0。"""
    g.hbar(x1, x2, CJK_BOT + weight / 2.0, weight)


# ===========================================================================
# 共用部件（同一套笔画拆法，只做位置平移 —— GLY-004）
# ===========================================================================
def comp_kao(g: Glyph, ox: float, oy: float) -> None:
    """咸（感 / 減 共用）：戌框 + 内一 + 口 + 戈。

    局部坐标（相对 (ox, oy)）：
      顶横   一(120..620, 中心线 772)      墨迹 724..820
      左撇   (120,790)→(35,520)            竖向，构成厂形
      内一   一(170..570, 中心线 640)       墨迹 598..682
      口     顶 一(170..430, 中心线 512)   墨迹 470..554
             左竖 x=212 (554→300) / 右竖 x=388 (554→300)
             底 一(170..430, 中心线 342)    墨迹 300..384
      戈     斜钩 (560,760)→(700,330) + 钩尾 (698,332)→(730,378)
             撇   (650,600)→(540,440)
             丶   (610,776) 斜切 −14
    """
    g.hbar(ox + 120, ox + 620, oy + 772, weight=W_MAIN)
    g.diag(ox + 120, oy + 790, ox + 35, oy + 520, weight=W_SEC)
    g.hbar(ox + 170, ox + 570, oy + 640, weight=W_THIN)
    g.hbar(ox + 170, ox + 430, oy + 512, weight=W_THIN)
    g.vbar(ox + 212, oy + 300, oy + 554, weight=W_THIN)
    g.vbar(ox + 388, oy + 300, oy + 554, weight=W_THIN)
    g.hbar(ox + 170, ox + 430, oy + 342, weight=W_THIN)
    g.diag(ox + 560, oy + 760, ox + 700, oy + 330, weight=W_SEC)
    g.diag(ox + 698, oy + 332, ox + 730, oy + 378, weight=W_THIN)
    g.diag(ox + 650, oy + 600, ox + 540, oy + 440, weight=W_THIN)
    g.dot(ox + 610, oy + 776, w=W_DOT, h=88, slant=-14)


def comp_mok(g: Glyph, ox: float, oy: float, scale: float = 1.0) -> None:
    """木（格 / 検 共用）：一 + 丨 + 撇 + 捺。"""
    w = W_MAIN
    g.hbar(ox + 10 * scale, ox + 290 * scale, oy + 620, weight=w)
    g.vbar(ox + 150 * scale, oy + 40, oy + 790, weight=W_SEC)
    g.diag(ox + 150 * scale, oy + 630, ox + 25 * scale, oy + 210, weight=W_THIN)
    g.diag(ox + 155 * scale, oy + 630, ox + 300 * scale, oy + 240, weight=W_THIN)


def comp_benzang(g: Glyph, ox: float, oy: float) -> None:
    """辶（運 / 過 共用）：丶 + 横折折撇 + 平捺。

    丶 = −14 档（工程约定），平捺是全字的落地线。
    """
    g.dot(ox + 120, oy + 700, w=W_DOT, h=96, slant=-14)
    g.vbar(ox + 110, oy + 230, oy + 620, weight=W_THIN)
    g.diag(ox + 110, oy + 250, ox + 210, oy + 190, weight=W_THIN)
    g.diag(ox + 150, oy + 200, ox + 800, oy + 70, weight=W_SEC)


def comp_kuchi(g: Glyph, x1: float, x2: float, ybot: float, ytop: float,
               weight: float = W_THIN) -> None:
    """口：左右两竖 + 上下两横（横的墨迹上缘/下缘按对齐语义内缩）。"""
    g.hbar(x1, x2, ytop - weight / 2.0, weight)
    g.hbar(x1, x2, ybot + weight / 2.0, weight)
    g.vbar(x1 + weight / 2.0, ybot, ytop, weight)
    g.vbar(x2 - weight / 2.0, ybot, ytop, weight)


# ===========================================================================
# 各字形
# ===========================================================================
def glyph_soku() -> Glyph:
    """側（11 画）＝ 亻 + 貝 + 刂。

    分区：亻 x 60..300 / 貝 x 314..660 / 刂 x 698..926。
    貝 = 目（3 个字腔）+ 八：目部 4 道横，墨迹 728..820 / 606..690 / 488..572 /
    370..454，横间白口 38 / 34 / 34（≥ 24 ✓）；左右竖内缘相距 162（≥ 60 ✓）。
    刂：短竖 x=740（墨 698..782），长竖 x=880（墨 834..926），两者相距 52；
    与貝的右缘（660）白口 38。
    """
    g = Glyph("uni5074", advance=1000, unicode=0x5074, note="側：亻 + 貝 + 刂")

    # ---- 亻 ----
    g.diag(280, 795, 120, 620, weight=W_SEC)
    g.vbar(200, 700, 0, weight=W_MAIN)

    # ---- 貝：目 ----
    g.hbar(314, 660, 774, weight=W_SEC)        # 目：上横（墨 728..820）
    g.vbar(360, 420, 820, weight=W_SEC)        # 目：左竖
    g.vbar(614, 420, 820, weight=W_SEC)        # 目：右竖
    g.hbar(314, 660, 648, weight=W_THIN)       # 目：内横 1（墨 606..690）
    g.hbar(314, 660, 530, weight=W_THIN)       # 目：内横 2（墨 488..572）
    g.hbar(314, 660, 412, weight=W_THIN)       # 目：底横（墨 370..454）
    # ---- 貝：八 ----
    # 八腿沿原直线**向上平移**（同斜率，角度不变）：起笔抬进目部底横内部，
    # 避免腿的上端与底横「切向接触」——底横墨迹下缘 370，腿的上角原在 369.5，
    # 只差 0.5 即造成零面积相切 → shapely 判为轮廓自交（check_glyphs FAIL）。
    # 现在腿的上端完整落在底横墨迹（370..454）内部，是正面积交叠。
    g.diag(429, 415, 330, 30, weight=W_THIN)      # 撇：沿 (420,380)→(330,30) 同线放大 1.1×
    g.diag(534.5, 415, 650, 30, weight=W_THIN)    # 捺：沿 (545,380)→(650,30) 同线放大 1.1×

    # ---- 刂 ----
    g.vbar(740, 660, 440, weight=W_THIN)
    g.vbar(880, 820, 110, weight=W_SEC)
    g.diag(878, 120, 790, 155, weight=W_THIN)
    return g


def glyph_kan() -> Glyph:
    """感（13 画）＝ 咸（9）+ 心（4）。

    咸区 y 300..820：顶横墨 724..820；内一墨 598..682（白口 42 ✓）；
    口：顶 470..554 / 底 300..384，字腔 92×86 ✓；
    戈的斜钩自顶横下方 (700,760) 冲向右下至 (860,330)，钩尾回到右上；
    撇 (790,600)→(680,440) 与斜钩相交（交角约 50°，等效重叠 < 1.5）。
    心区 y 0..280：卧钩底 84..176，左点 173..257、中点、右点分列。
    """
    g = Glyph("uni611F", advance=1000, unicode=0x611F, note="感：咸 + 心")

    # ---- 咸 ----
    g.hbar(250, 900, 772, weight=W_MAIN)        # 顶横（墨 724..820）
    g.dot(894, 776, w=W_DOT, h=84, slant=-14)   # 戈的点（右上角）
    g.diag(280, 790, 165, 500, weight=W_SEC)    # 戌的左撇
    g.hbar(330, 700, 640, weight=W_THIN)        # 内一（墨 598..682）
    comp_kuchi(g, 330, 590, 300, 554, W_THIN)  # 口
    g.diag(700, 760, 860, 330, weight=W_SEC)    # 戈的斜钩
    g.diag(858, 332, 890, 378, weight=W_THIN)   # 斜钩的钩尾
    g.diag(790, 600, 680, 440, weight=W_THIN)   # 戈的撇

    # ---- 心 ----
    g.hbar(180, 800, 130, weight=W_SEC)         # 卧钩（墨 84..176）
    g.diag(798, 135, 872, 200, weight=W_THIN)   # 卧钩的钩
    g.dot(215, 250, w=W_DOT, h=96, slant=-14)   # 左点
    g.dot(520, 262, w=W_DOT, h=96, slant=-14)   # 中点
    g.dot(790, 258, w=W_DOT, h=96, slant=14)    # 右点
    return g


def glyph_toku() -> Glyph:
    """特（10 画）＝ 牜（4）+ 寺（6）。

    牜区 x 60..330：撇 (300,790)→(175,700)；横墨 594..686；竖墨 164..256；
    提自 (75,130) 升到 (300,290)（与水平约 35°，不与横画长距离交叠）。
    寺区 x 360..940：土的顶横 674..766、竖 614..706、底横 554..646；
    寸的一 394..486；亅 x=790；点 x 478..562（与竖白口 52）。
    横排白口：766→646 = 120，646→486 = 68，486→（寸点顶 202）= 192。
    """
    g = Glyph("uni7279", advance=1000, unicode=0x7279, note="特：牜 + 寺")

    # ---- 牜 ----
    g.diag(300, 790, 175, 700, weight=W_SEC)
    g.hbar(85, 330, 640, weight=W_SEC)
    g.vbar(210, 800, 60, weight=W_MAIN)
    g.diag(75, 130, 300, 290, weight=W_SEC)

    # ---- 寺：土 ----
    g.hbar(420, 900, 720, weight=W_MAIN)        # 土的顶横（墨 674..766）
    g.vbar(660, 790, 630, weight=W_SEC)         # 土的竖
    g.hbar(380, 940, 600, weight=W_MAIN)        # 土的底横（墨 554..646）
    # ---- 寺：寸 ----
    g.hbar(360, 940, 440, weight=W_MAIN)        # 寸的一（墨 394..486）
    g.vbar(790, 460, 90, weight=W_SEC)          # 寸的亅
    g.diag(788, 95, 706, 130, weight=W_THIN)    # 亅的钩
    g.dot(520, 250, w=W_DOT, h=96, slant=-14)   # 寸的点
    return g


def glyph_jo() -> Glyph:
    """情（11 画）＝ 忄（3）+ 青（8）。

    忄区 x 66..322：左点墨 66..150 / 565..675，竖墨 142..238，右点 238..322。
    青区 x 330..940：龶三横墨 728..820 / 618..702 / 508..592（白口 26 ✓），
    竖 x=600 贯穿；月部四竖…三横 396..484 / 258..342 / 118..202，
    两字腔 54 与 56 ✓，左右竖内缘相距 312 ✓。
    """
    g = Glyph("uni60C5", advance=1000, unicode=0x60C5, note="情：忄 + 青")

    # ---- 忄 ----
    g.dot(108, 620, w=W_DOT, h=110, slant=-14)  # 左点
    g.vbar(190, 780, 60, weight=W_MAIN)         # 竖
    g.dot(280, 690, w=W_DOT, h=110, slant=14)   # 右点

    # ---- 青：龶 ----
    g.hbar(360, 900, 776, weight=W_SEC)         # 一（墨 732..820）
    g.vbar(600, 800, 540, weight=W_THIN)        # 竖
    g.hbar(340, 920, 662, weight=W_THIN)        # 一（墨 620..704）
    g.hbar(330, 930, 550, weight=W_THIN)        # 一（墨 508..592）
    # ---- 青：月 ----
    g.hbar(384, 880, 440, weight=W_SEC)         # 顶（墨 396..484）
    g.vbar(430, 90, 440, weight=W_SEC)          # 左竖
    g.vbar(834, 484, 180, weight=W_SEC)         # 右竖
    g.hbar(384, 880, 300, weight=W_THIN)        # 中横（墨 258..342）
    g.hbar(384, 880, 160, weight=W_THIN)        # 底横（墨 118..202）
    return g


def glyph_ki() -> Glyph:
    """基（11 画）＝ 其（8）+ 土（3）。

    其区 y 300..820：四道横墨 732..820 / 620..704 / 508..592 / 396..480，
    横间白口 28 ✓；两竖墨 258..342 与 658..742，字腔 316 ✓；
    八腿自 (370,400) 与 (630,400) 向下分张。
    土区 y 0..280：短横墨 174..266，竖 454..546，底横墨 0..96（对齐基线）。
    """
    g = Glyph("uni57FA", advance=1000, unicode=0x57FA, note="基：其 + 土")

    # ---- 其 ----
    g.hbar(150, 850, 776, weight=W_SEC)         # 一（墨 732..820）
    g.vbar(300, 800, 480, weight=W_THIN)        # 左竖
    g.vbar(700, 800, 480, weight=W_THIN)        # 右竖
    g.hbar(150, 850, 662, weight=W_THIN)        # 一（墨 620..704）
    g.hbar(180, 820, 550, weight=W_THIN)        # 一（墨 508..592）
    g.hbar(180, 820, 438, weight=W_THIN)        # 一（墨 396..480）
    g.diag(370, 400, 260, 300, weight=W_THIN)   # 八的撇
    g.diag(630, 400, 740, 300, weight=W_THIN)   # 八的捺

    # ---- 土 ----
    g.hbar(330, 670, 220, weight=W_SEC)         # 土的短横（墨 174..266）
    g.vbar(500, 280, 60, weight=W_SEC)          # 土的竖
    g.hbar(230, 770, 48, weight=W_MAIN)         # 土的底横（墨 0..96）
    return g


def glyph_shima() -> Glyph:
    """島（10 画）＝ 鳥頭（丿 + 白 + 一）+ 山。

    鳥頭區 x 254..800：頭上的丿 墨 669..816（壓在日頂橫上）；
    日：頂橫 654..746、內橫 540..624、日底 426..510（白口 30 / 30 ✓）；
    鳥的一 墨 318..402 —— **必須與日底留白**：原坐标把「日底」(426..510) 与
    「鳥的一」(378..462) 疊了 36，兩條橫黏成一條粗橫
    （check_stroke_gaps 等效重疊 2.79，差 0.21 沒被報成「疑似粘連」，
    但白口已經是負的 —— 鐵律 7 說的正是這種情況）。
    山區 y 60..318：底橫 60..144、左豎 80..250、中豎 130..290、右豎 100..265；
    中豎頂 290 與鳥的一的下緣 318 留 28 ✓；日的左右豎落到 450（壓進日底）。
    """
    g = Glyph("uni5CF6", advance=1000, unicode=0x5CF6, note="島：鳥頭 + 山")

    # ---- 鳥頭 ----
    g.diag(340, 780, 220, 705, weight=W_THIN)   # 頭上的撇
    g.hbar(254, 800, 700, weight=W_SEC)         # 日：頂橫（墨 654..746）
    g.vbar(300, 450, 746, weight=W_SEC)         # 日：左豎
    g.vbar(754, 450, 746, weight=W_SEC)         # 日：右豎
    g.hbar(254, 800, 582, weight=W_THIN)        # 日：內橫（墨 540..624）
    g.hbar(254, 800, 468, weight=W_THIN)        # 日：底橫（墨 426..510）
    g.hbar(254, 800, 360, weight=W_THIN)        # 鳥的一（墨 318..402）

    # ---- 山 ----
    g.hbar(300, 700, 102, weight=W_THIN)        # 底橫（墨 60..144）
    g.vbar(300, 80, 250, weight=W_SEC)          # 左豎
    g.vbar(520, 130, 290, weight=W_THIN)        # 中豎
    g.vbar(660, 100, 265, weight=W_THIN)        # 右豎
    return g


def glyph_asa() -> Glyph:
    """朝（12 画）＝ 龺（8）+ 月（4）。

    龺區 x 60..500：十（頂）墨 694..786；日部三橫 616..700 / 458..542 / 338..422，
    字腔 74 / 36；十（底）墨 214..306，與日白口 32。
    月區 x 554..934：三橫 702..794 / 558..642 / 418..502，字腔 60 / 56 ✓，
    左右豎內緣 646..842 = 196 ✓。
    """
    g = Glyph("uni671D", advance=1000, unicode=0x671D, note="朝：龺 + 月")

    # ---- 龺：十 + 日 + 十 ----
    g.hbar(120, 480, 740, weight=W_SEC)         # 十的橫（墨 694..786）
    g.vbar(300, 820, 640, weight=W_SEC)         # 十的豎
    g.hbar(148, 460, 658, weight=W_THIN)        # 日：頂（墨 616..700）
    g.vbar(190, 380, 700, weight=W_THIN)        # 日：左豎
    g.vbar(418, 380, 700, weight=W_THIN)        # 日：右豎
    g.hbar(148, 460, 500, weight=W_THIN)        # 日：中（墨 458..542）
    g.hbar(148, 460, 380, weight=W_THIN)        # 日：底（墨 338..422）
    g.hbar(100, 500, 260, weight=W_SEC)         # 十（底）的橫（墨 214..306）
    g.vbar(300, 380, 214, weight=W_SEC)         # 十（底）的豎

    # ---- 月 ----
    g.hbar(554, 934, 748, weight=W_SEC)         # 月：頂（墨 702..794）
    g.vbar(600, 40, 790, weight=W_SEC)          # 月：左豎
    g.vbar(888, 40, 794, weight=W_SEC)          # 月：右豎
    g.hbar(554, 934, 600, weight=W_THIN)        # 月：中（墨 558..642）
    g.hbar(554, 934, 460, weight=W_THIN)        # 月：底（墨 418..502）
    return g


def glyph_sagi() -> Glyph:
    """提（12 画）＝ 扌（3）+ 是（9）。

    扌區 x 80..330：橫墨 594..686；豎 x=200（墨 144..256）下端帶鉤；
    提自 (80,230) 升到 (320,340)，與橫畫不平行重疊。
    是區 x 388..940：日部三橫 698..782 / 578..662 / 518..602，字腔 36；
    疋的一 394..486（與日白口 32），豎 658..742，短橫 158..242，
    撇自 (660,200) 至 (480,60)，捺自 (700,250) 至 (900,90)。
    """
    g = Glyph("uni63D0", advance=1000, unicode=0x63D0, note="提：扌 + 是")

    # ---- 扌 ----
    g.hbar(80, 330, 640, weight=W_SEC)
    g.vbar(200, 780, 60, weight=W_MAIN)
    g.diag(198, 75, 120, 115, weight=W_THIN)     # 豎鉤
    g.diag(80, 230, 320, 340, weight=W_SEC)     # 提

    # ---- 是：日 ----
    g.hbar(388, 780, 740, weight=W_SEC)         # 頂（墨 698..782）
    g.vbar(430, 520, 782, weight=W_SEC)         # 左豎
    g.vbar(738, 520, 782, weight=W_SEC)         # 右豎
    g.hbar(388, 780, 620, weight=W_THIN)        # 中（墨 578..662）
    g.hbar(388, 780, 560, weight=W_THIN)        # 底（墨 518..602）
    # ---- 是：疋 ----
    g.hbar(400, 900, 440, weight=W_MAIN)        # 的一（墨 394..486）
    g.vbar(700, 440, 160, weight=W_SEC)         # 豎
    g.hbar(520, 720, 200, weight=W_THIN)        # 短橫（墨 158..242）
    g.diag(660, 200, 480, 60, weight=W_THIN)    # 撇
    g.diag(700, 250, 900, 90, weight=W_SEC)     # 捺
    return g


def glyph_un() -> Glyph:
    """運（11 画）＝ 辶（2）+ 軍（9）。

    軍區 x 348..912：冖的橫墨 726..818，兩端豎 348..432 / 828..912；
    車的上橫 574..666；車體三橫 574..666 / 418..502 / 258..342，
    兩道白口 72 / 76 ✓；中豎 584..676 貫穿至 180；底橫 134..226。
    辶：點 78..162 / 652..748（斜切 −14），豎 68..152，捺自 (150,200)
    鋪到 (880,45)，是全字的落地線。
    """
    g = Glyph("uni904B", advance=1000, unicode=0x904B, note="運：辶 + 軍")

    # ---- 軍 ----
    g.hbar(348, 912, 772, weight=W_MAIN)        # 冖的橫（墨 726..818）
    g.vbar(390, 810, 700, weight=W_THIN)        # 冖的左垂
    g.vbar(870, 810, 730, weight=W_THIN)        # 冖的右垂
    g.hbar(424, 836, 620, weight=W_SEC)         # 車的上橫（墨 574..666）
    g.vbar(470, 620, 300, weight=W_SEC)         # 車：左豎
    g.vbar(790, 620, 300, weight=W_SEC)         # 車：右豎
    g.hbar(424, 836, 460, weight=W_THIN)        # 車：內橫 1（墨 418..502）
    g.hbar(424, 836, 300, weight=W_THIN)        # 車：內橫 2（墨 258..342）
    g.vbar(630, 700, 180, weight=W_SEC)         # 車的中豎
    g.hbar(400, 860, 180, weight=W_SEC)         # 車的底橫（墨 134..226）

    # ---- 辶 ----
    comp_benzang(g, 0, 0)
    return g


def glyph_shu() -> Glyph:
    """終（11 画）＝ 糸（6）+ 冬（5）。

    糸區 x 60..380：幺部兩折（撇 + 折橫）自上而下，橫 418..502，
    豎 178..262，左撇 90..170、右點 270..350。
    冬區 x 420..940：夂（撇 440..560 / 橫折 430..700 / 捺 500..880），
    下方兩點 478..562 與 598..682（斜切 −14）。
    """
    g = Glyph("uni7D42", advance=1000, unicode=0x7D42, note="終：糸 + 冬")

    # ---- 糸 ----
    g.diag(300, 800, 150, 700, weight=W_SEC)    # 幺的第一撇
    g.hbar(150, 300, 700, weight=W_THIN)        # 幺的折橫
    g.diag(260, 640, 130, 540, weight=W_SEC)    # 幺的第二撇
    g.hbar(130, 280, 540, weight=W_THIN)        # 幺的折橫
    g.hbar(120, 320, 460, weight=W_THIN)        # 糸的一（墨 418..502）
    g.vbar(220, 460, 60, weight=W_SEC)          # 糸的豎
    g.diag(170, 440, 90, 250, weight=W_THIN)    # 糸的左撇
    g.diag(270, 440, 350, 250, weight=W_THIN)   # 糸的右點

    # ---- 冬 ----
    g.diag(560, 800, 440, 680, weight=W_SEC)    # 夂的撇
    g.hbar(430, 700, 660, weight=W_THIN)        # 夂的橫
    g.diag(700, 660, 560, 500, weight=W_SEC)    # 夂的橫折
    g.diag(500, 560, 880, 300, weight=W_SEC)    # 夂的捺
    g.dot(520, 380, w=W_DOT, h=96, slant=-14)   # 冬的第一點
    g.dot(640, 240, w=W_DOT, h=96, slant=-14)   # 冬的第二點
    return g


def glyph_kyo() -> Glyph:
    """挙（10 画）＝ ツ（3）+ 興の省形（下部 7 画）。

    上部：ツ的三筆（左短撇 150..250 / 右短撇 300..400 / 長撇 260..460），
    皆自 y≈800 落下，不與任何橫畫長距離平行。
    下部：橫 574..666（墨）；八的撇捺自 (500,560) 分張到 (300,360)/(760,330)；
    再一橫 436..528；末橫 298..390；豎 454..546 下端帶鉤。
    """
    g = Glyph("uni6319", advance=1000, unicode=0x6319, note="挙：ツ + 興の省形")

    # ---- ツ ----
    g.diag(250, 810, 160, 740, weight=W_SEC)    # ツの左短撇
    g.diag(400, 810, 310, 740, weight=W_SEC)    # ツの右短撇
    g.diag(460, 800, 270, 700, weight=W_SEC)    # ツの長撇

    # ---- 下部 ----
    g.hbar(90, 910, 620, weight=W_MAIN)         # 橫（墨 574..666）
    g.diag(500, 560, 300, 360, weight=W_SEC)    # 八の撇
    g.diag(500, 560, 760, 330, weight=W_SEC)    # 八の捺
    g.hbar(280, 840, 482, weight=W_SEC)         # 橫（墨 436..528）
    g.hbar(150, 870, 344, weight=W_SEC)         # 橫（墨 298..390）
    g.vbar(500, 344, 60, weight=W_SEC)          # 豎
    g.diag(498, 75, 420, 115, weight=W_THIN)    # 豎鉤
    return g


def glyph_seki() -> Glyph:
    """勢（13 画）＝ 埶（11）+ 力（2）。

    埶上半：坴部（頂橫 728..820、豎 154..246、橫 614..706、八 120..310）+
    丸部（横折弯钩 362..626、丶 388..472）。
    埶下半/力區 y 0..300：橫折鉤 254..346 / 628..720，撇自 (430,290) 至 (250,40)。
    密排處（坴部的三道橫）白口 22 / 88 / 120，最窄處仍是 22（接近下限，
    故把坴部的內橫降到 84 檔以保 22 以上的白口）。
    """
    g = Glyph("uni52E2", advance=1000, unicode=0x52E2, note="勢：埶 + 力")

    # ---- 坴 ----
    g.hbar(90, 330, 774, weight=W_SEC)          # 頂橫（墨 732..816）
    g.vbar(200, 800, 660, weight=W_THIN)        # 豎
    g.hbar(90, 330, 660, weight=W_THIN)         # 橫（墨 618..702）
    # 八的两腿沿原直线**向上平移**（同斜率，角度不变）并让两腿在顶点**正面积交叠**：
    # 原坐标下两腿的内上角分别落在 (214.95, 586.70) 与 (215.05, 586.70)，
    # 只差 0.1 单位 → 并集后「孔洞」被压成一个沙漏（ring 自交于 215,587）。
    # 现在两腿上端在 y=609..656 之间互相压住，孔洞上沿收成一个正常的尖顶。
    g.diag(195, 632.5, 120, 520, weight=W_THIN)   # 八的撇：沿 (180,610)→(120,520) 同线放大 1.25×
    g.diag(235, 632.5, 310, 520, weight=W_THIN)   # 八的捺：沿 (250,610)→(310,520) 同线放大 1.25×
    g.hbar(90, 330, 480, weight=W_THIN)         # 橫（墨 438..522）

    # ---- 丸 ----
    g.diag(420, 790, 350, 690, weight=W_THIN)   # 丸的撇
    g.hbar(390, 626, 720, weight=W_SEC)         # 丸的橫
    g.vbar(580, 720, 520, weight=W_SEC)         # 丸的豎
    g.diag(578, 540, 634, 600, weight=W_THIN)   # 丸的鉤
    g.dot(430, 660, w=W_DOT, h=96, slant=-14)   # 丸的點

    # ---- 力 ----
    g.hbar(180, 720, 300, weight=W_MAIN)        # 力：橫折（墨 254..346）
    g.vbar(674, 346, 60, weight=W_SEC)          # 力：豎
    g.diag(672, 75, 590, 115, weight=W_THIN)    # 力：鉤
    g.diag(430, 290, 250, 40, weight=W_SEC)     # 力：撇
    return g


def glyph_gen() -> Glyph:
    """減（12 画）＝ 冫（2）+ 咸（10）。

    冫區 x 58..162：上點（斜切 −14，落在 700..790 帶）與提
    (70,210)→(255,330)；與咸區的白口 ≥ 100。
    咸區沿用 comp_kao 的筆畫拆法（感用同一套），整體右移 250、下移 0，
    尺寸不變：頂橫 724..820、口 470..554 / 300..384、字腔 92×86。
    """
    g = Glyph("uni6E1B", advance=1000, unicode=0x6E1B, note="減：冫 + 咸")

    # ---- 冫 ----
    g.dot(110, 740, w=W_DOT, h=110, slant=-14)   # 冫的上點
    g.diag(70, 210, 255, 330, weight=W_SEC)     # 冫的提

    # ---- 咸（與感同一部件，同一套筆畫拆法）----
    comp_kao(g, 250, 0)
    return g


def glyph_yoh() -> Glyph:
    """容（10 画）＝ 宀（3）+ 谷（7）。

    宀區：竪點（斜切 0，墨 730..830 → 實際落在 730..820 內）、
    冖的橫 690..782、左垂 150..234。
    谷區：八（430..520 與 570..660 兩撇）、人（500→330 / 500→670）、
    口 350..640，底橫墨 0..84。
    """
    g = Glyph("uni5BB9", advance=1000, unicode=0x5BB9, note="容：宀 + 谷")

    # ---- 宀 ----
    g.dot(500, 775, w=W_DOT, h=96, slant=0)     # 宀的竪點
    g.hbar(150, 850, 738, weight=W_MAIN)        # 冖的橫（墨 690..782）
    g.vbar(192, 690, 600, weight=W_THIN)        # 冖的左垂

    # ---- 谷 ----
    g.diag(430, 640, 350, 560, weight=W_THIN)   # 八的撇
    g.diag(570, 640, 650, 560, weight=W_THIN)   # 八的捺
    g.diag(500, 560, 330, 380, weight=W_SEC)    # 人的撇
    g.diag(500, 560, 670, 380, weight=W_SEC)    # 人的捺
    comp_kuchi(g, 350, 640, 0, 280, W_THIN)     # 口
    return g


def glyph_den() -> Glyph:
    """電（13 画）＝ 雨（8）+ 电（5）。

    雨區 y 380..808：頂橫 712..808；冂的左豎 118..202、右豎 798..882、
    中豎 458..542；四點（−14 檔）分列左右：310 / 690 兩處。
    电區 y 60..400：日部三橫 294..386 / 178..262 / 58..142，字腔 32 / 36 ✓；
    中豎 431..523 貫穿到底，下端向左鉤出 40 單位。
    """
    g = Glyph("uni96FB", advance=1000, unicode=0x96FB, note="電：雨 + 电")

    # ---- 雨 ----
    g.hbar(90, 910, 760, weight=W_MAIN)         # 頂橫（墨 712..808）
    g.hbar(118, 882, 670, weight=W_SEC)         # 冂的橫（墨 624..716）
    g.vbar(160, 380, 716, weight=W_SEC)         # 冂的左豎
    g.vbar(840, 380, 716, weight=W_SEC)         # 冂的右豎
    g.vbar(500, 380, 716, weight=W_SEC)         # 中豎
    g.dot(300, 640, w=76, h=84, slant=-14)      # 雨點 1
    g.dot(300, 480, w=76, h=84, slant=-14)      # 雨點 2
    g.dot(700, 640, w=76, h=84, slant=-14)      # 雨點 3
    g.dot(700, 480, w=76, h=84, slant=-14)      # 雨點 4

    # ---- 电 ----
    g.hbar(254, 700, 340, weight=W_SEC)         # 頂（墨 294..386）
    g.vbar(300, 60, 386, weight=W_SEC)          # 左豎
    g.vbar(654, 60, 386, weight=W_SEC)          # 右豎
    g.hbar(254, 700, 220, weight=W_THIN)        # 中（墨 178..262）
    g.hbar(254, 700, 100, weight=W_THIN)        # 底（墨 58..142）
    g.vbar(477, 60, 400, weight=W_SEC)          # 電的中豎
    g.diag(475, 110, 600, 70, weight=W_SEC)     # 電的鉤
    return g


def glyph_sai() -> Glyph:
    """歳（13 画）＝ 止（4）+ 戌（6）+ 小（3）。

    止區 x 60..330：豎 154..246（620..810）、短橫 678..762、底橫 544..636。
    戌區 x 330..940：頂橫 654..746、厂撇 330..444、內一 518..602、
    斜鉤 700..880、撇 680..760、點（−14）778..862。
    小區 y 60..380：豎 434..526，撇 300..380，點 580..660。
    """
    g = Glyph("uni6B73", advance=1000, unicode=0x6B73, note="歳：止 + 戌 + 小")

    # ---- 止 ----
    g.vbar(200, 810, 620, weight=W_SEC)         # 豎
    g.hbar(80, 246, 720, weight=W_THIN)         # 短橫（墨 678..762）
    g.hbar(60, 330, 590, weight=W_SEC)          # 底橫（墨 544..636）

    # ---- 戌 ----
    g.hbar(330, 900, 700, weight=W_SEC)         # 頂橫（墨 654..746）
    g.diag(400, 690, 330, 400, weight=W_SEC)    # 厂的撇
    g.hbar(360, 640, 560, weight=W_THIN)        # 內一（墨 518..602）
    g.diag(700, 720, 880, 380, weight=W_SEC)    # 斜鉤
    g.diag(876, 382, 908, 428, weight=W_THIN)   # 鉤尾
    g.diag(760, 560, 680, 460, weight=W_THIN)   # 撇
    g.dot(820, 720, w=W_DOT, h=96, slant=-14)   # 點

    # ---- 小 ----
    g.vbar(480, 380, 60, weight=W_SEC)          # 豎
    g.diag(380, 330, 300, 180, weight=W_THIN)   # 撇
    g.diag(580, 330, 660, 180, weight=W_THIN)   # 點
    return g


def glyph_no() -> Glyph:
    """能（10 画）＝ 厶（2）+ 月（4）+ 匕（2）+ 匕（2）。

    厶區 x 60..300 y 620..820：撇折 + 點（−14）。
    月區 x 74..404 y 60..644：四橫 596..688 / 452..544 / 308..400 / 164..256，
    三個字腔 52 / 52 / 52 ✓；左右豎內緣 166..312 = 146 ✓。
    匕×2：右上 500..800 y 560..820，右下 500..800 y 60..500，各為撇 + 豎彎鉤。
    """
    g = Glyph("uni80FD", advance=1000, unicode=0x80FD, note="能：厶 + 月 + 匕 + 匕")

    # ---- 厶 ----
    g.diag(240, 800, 130, 700, weight=W_SEC)    # 厶的撇
    g.hbar(130, 300, 700, weight=W_THIN)        # 厶的折
    g.dot(280, 690, w=W_DOT, h=96, slant=-14)   # 厶的點

    # ---- 月 ----
    g.hbar(74, 404, 642, weight=W_SEC)          # 頂（墨 596..688）
    g.vbar(120, 60, 688, weight=W_SEC)          # 左豎
    g.vbar(358, 60, 688, weight=W_SEC)          # 右豎
    g.hbar(74, 404, 498, weight=W_THIN)         # 內橫 1（墨 452..544）
    g.hbar(74, 404, 354, weight=W_THIN)         # 內橫 2（墨 308..400）
    g.hbar(74, 404, 210, weight=W_THIN)         # 內橫 3（墨 164..256）

    # ---- 匕（上） ----
    g.diag(700, 790, 520, 700, weight=W_THIN)   # 撇
    g.vbar(540, 560, 700, weight=W_SEC)         # 豎彎
    g.hbar(540, 800, 600, weight=W_SEC)         # 彎鉤的橫
    g.diag(798, 602, 740, 660, weight=W_THIN)   # 鉤

    # ---- 匕（下） ----
    g.diag(700, 470, 520, 380, weight=W_THIN)   # 撇
    g.vbar(540, 240, 380, weight=W_SEC)         # 豎彎
    g.hbar(540, 800, 280, weight=W_SEC)         # 彎鉤的橫
    g.diag(798, 282, 740, 340, weight=W_THIN)   # 鉤
    return g


def glyph_oki() -> Glyph:
    """置（13 画）＝ 罒（5）+ 直（8）。

    罒區 y 550..782：頂橫 690..782、底橫 550..642、中豎 458..542，
    三個字腔 120 / 116 / 136 ✓。
    直區 y 12..496：十（橫 404..496、豎 458..542）、目三橫 318..402 / 208..292 /
    98..182（字腔 26 / 26 ✓）、底橫 12..108。
    """
    g = Glyph("uni7F6E", advance=1000, unicode=0x7F6E, note="置：罒 + 直")

    # ---- 罒 ----
    g.hbar(120, 880, 736, weight=W_SEC)         # 頂（墨 690..782）
    g.vbar(162, 550, 782, weight=W_THIN)        # 左豎
    g.vbar(838, 550, 782, weight=W_THIN)        # 右豎
    g.vbar(500, 550, 782, weight=W_THIN)        # 中豎
    g.hbar(120, 880, 596, weight=W_THIN)        # 底（墨 550..642）

    # ---- 直：十 ----
    g.hbar(240, 760, 450, weight=W_SEC)         # 十的橫（墨 404..496）
    g.vbar(500, 470, 330, weight=W_THIN)        # 十的豎
    # ---- 直：目 ----
    g.hbar(258, 740, 360, weight=W_THIN)        # 頂（墨 318..402）
    g.vbar(300, 100, 402, weight=W_THIN)        # 左豎
    g.vbar(698, 100, 402, weight=W_THIN)        # 右豎
    g.hbar(258, 740, 250, weight=W_THIN)        # 內橫 1（墨 208..292）
    g.hbar(258, 740, 140, weight=W_THIN)        # 內橫 2（墨 98..182）
    # ---- 直：底 ----
    g.hbar(180, 820, 60, weight=W_MAIN)         # 底橫（墨 12..108）
    return g


def glyph_shin() -> Glyph:
    """真（10 画）＝ 十（2）+ 目（5）+ 一（1）+ 八（2）。

    骨架照 M PLUS 1p Black 与 Zen Kaku Gothic New Black（两者一致）：
    **竖只冒出横的上缘**（短竖秃头，不穿横）+ 满宽横 + 具的目 + 满宽一 + 八。
    参照的「目」是「实心盒 + 细缝」（白口只有 25 单位），本字族按 GLY-006
    要白口 ≥ 24 且**竖排节奏必须重排**，否则「一」会与目的底横压在一起
    （原坐标：目底横墨 218..302 与一墨 174..266 叠了 48 单位 → 等效粘连 3.56）。

    重排后的竖排节奏（合计 0..820）：
      十的横    墨 658..754（满宽 60..940）
      十的短竖  墨 730..820（x 458..542），压进横里 24 单位
      目        顶 550..634 / 內1 442..526 / 內2 334..418 / 底 226..310
                三格白口 24 / 24 / 24 ✓（下限）；目的外缘 x 156..844，
                左右竖内缘 244..756，字腔 512 ✓
      一        墨 110..202（满宽 60..940），与目底白口 24 ✓
      八        两腿自一的下缘里起笔（撇 (390,145)→(140,45)、捺 (610,145)→(860,45)），
                墨底 6（不破基线）；两腿顶端相距 188，不会挤成蝴蝶结。
    """
    g = Glyph("uni771F", advance=1000, unicode=0x771F, note="真：十 + 目 + 一 + 八")

    # ---- 十 ----
    g.hbar(60, 940, 706, weight=W_MAIN)          # 橫（墨 658..754）
    g.vbar(500, 730, 820, weight=W_THIN)          # 短豎（墨 730..820）

    # ---- 目 ----
    g.vbar(202, 226, 634, weight=W_THIN)          # 左豎（墨 160..244）
    g.vbar(798, 226, 634, weight=W_THIN)          # 右豎（墨 756..840）
    g.hbar(156, 844, 592, weight=W_THIN)          # 頂（墨 550..634）
    g.hbar(156, 844, 484, weight=W_THIN)          # 內橫 1（墨 442..526）
    g.hbar(156, 844, 376, weight=W_THIN)          # 內橫 2（墨 334..418）
    g.hbar(156, 844, 268, weight=W_THIN)          # 底（墨 226..310）

    # ---- 一 ----
    g.hbar(60, 940, 156, weight=W_SEC)            # 一（墨 110..202）

    # ---- 八 ----
    g.diag(390, 145, 140, 45, weight=W_THIN)      # 八的撇
    g.diag(610, 145, 860, 45, weight=W_THIN)      # 八的捺
    return g


def glyph_nagare() -> Glyph:
    """流（10 画）＝ 氵（3）+ 㐬（7）。

    氵區 x 70..270：上點（短撇，26 檔，墨 634..746）、下點（26 檔，墨 402..514）、
    提 (70,140)→(248,308)（與港字的氵同一套筆畫拆法）。
    㐬區 x 350..940：亠的竪點（0 檔，726..836 → 落在 726..820 內）、一 644..736；
    厶：撇 (560,620)→(450,480)、折橫 438..522、點（−14）578..662；
    川：左豎 388..472、中豎 558..642、右豎 814..906（帶鉤）。
    """
    g = Glyph("uni6D41", advance=1000, unicode=0x6D41, note="流：氵 + 㐬")

    # ---- 氵 ----
    g.dot(158, 690, w=94, h=126, slant=26)      # 上點（短撇，26 檔）
    g.dot(150, 458, w=94, h=126, slant=26)      # 下點（26 檔）
    g.diag(70, 140, 248, 308, weight=W_SEC)     # 提

    # ---- 㐬：亠 ----
    g.dot(630, 773, w=W_DOT, h=100, slant=0)    # 竪點（0 檔）
    g.hbar(350, 900, 690, weight=W_MAIN)        # 一（墨 644..736）
    # ---- 㐬：厶 ----
    g.diag(560, 620, 450, 480, weight=W_SEC)    # 撇
    g.hbar(450, 620, 480, weight=W_THIN)        # 折橫（墨 438..522）
    g.dot(620, 520, w=W_DOT, h=96, slant=-14)   # 點
    # ---- 㐬：川 ----
    g.vbar(430, 60, 400, weight=W_THIN)         # 左豎
    g.vbar(600, 60, 420, weight=W_SEC)          # 中豎
    g.vbar(860, 100, 440, weight=W_SEC)         # 右豎
    g.diag(858, 110, 780, 150, weight=W_THIN)   # 右鉤
    return g


def glyph_kaku() -> Glyph:
    """格（10 画）＝ 木（4）+ 各（6）。

    木區 x 60..360：橫墨 574..666，豎 104..196，撇自 (150,630) 到 (25,210)，
    捺自 (155,630) 到 (300,240)；與右部白口 ≥ 40。
    各區 x 400..940：夂（撇 400..540 / 橫 430..820 / 橫撇 560..820 / 捺 560..900），
    口 518..860，底橫墨 78..162。
    """
    g = Glyph("uni683C", advance=1000, unicode=0x683C, note="格：木 + 各")

    # ---- 木 ----
    comp_mok(g, 60, 0)

    # ---- 各：夂 ----
    g.diag(540, 800, 400, 620, weight=W_SEC)    # 撇
    g.hbar(430, 820, 600, weight=W_SEC)         # 橫（墨 554..646）
    g.diag(820, 600, 560, 420, weight=W_SEC)    # 橫撇
    g.diag(560, 480, 900, 240, weight=W_SEC)    # 捺
    # ---- 各：口 ----
    comp_kuchi(g, 560, 860, 78, 380, W_THIN)
    return g


def glyph_ka() -> Glyph:
    """検（12 画）＝ 木（4）+ 僉（8）。

    木區 x 60..360（與格字同一部件，同一套筆畫拆法）。
    僉區 x 520..940：人（520..940 的兩撇）、一 578..662、
    吅（兩口：左 560..644 / 右 816..900，中豎 688..772；三橫 428..512 / 288..372）、
    從（四筆：兩組人分別 520..700 / 720..880）。
    """
    g = Glyph("uni691C", advance=1000, unicode=0x691C, note="検：木 + 僉")

    # ---- 木 ----
    comp_mok(g, 60, 0)

    # ---- 僉：人 ----
    g.diag(760, 800, 520, 640, weight=W_SEC)    # 人的撇
    g.diag(760, 800, 940, 640, weight=W_SEC)    # 人的捺
    # ---- 僉：一 ----
    g.hbar(540, 900, 620, weight=W_THIN)        # 一（墨 578..662）
    # ---- 僉：吅 ----
    g.hbar(560, 900, 470, weight=W_THIN)        # 吅的上橫（墨 428..512）
    g.hbar(560, 900, 330, weight=W_THIN)        # 吅的下橫（墨 288..372）
    g.vbar(602, 330, 512, weight=W_THIN)        # 左豎
    g.vbar(730, 330, 512, weight=W_THIN)        # 中豎
    g.vbar(858, 330, 512, weight=W_THIN)        # 右豎
    # ---- 僉：從 ----
    g.diag(620, 310, 540, 120, weight=W_THIN)   # 從（左）的撇
    g.diag(620, 310, 700, 120, weight=W_THIN)   # 從（左）的捺
    g.diag(800, 310, 720, 120, weight=W_THIN)   # 從（右）的撇
    g.diag(800, 310, 880, 120, weight=W_THIN)   # 從（右）的捺
    return g


def glyph_ze() -> Glyph:
    """税（12 画）＝ 禾（5）+ 兌（7）。

    禾區 x 60..340：頂撇 (300,800)→(160,720)、橫 614..706、豎 154..246、
    撇自 (200,630) 至 (70,200)、捺自 (205,630) 至 (340,220)。
    兌區 x 380..940：丷（左 −14 / 右 +14）、口 438..880（字腔 92×44）、
    儿（撇 460..620 / 豎彎鉤 788..892）。
    """
    g = Glyph("uni7A0E", advance=1000, unicode=0x7A0E, note="税：禾 + 兌")

    # ---- 禾 ----
    g.diag(300, 800, 160, 720, weight=W_SEC)    # 頂撇
    g.hbar(70, 330, 660, weight=W_SEC)          # 橫（墨 614..706）
    g.vbar(200, 780, 40, weight=W_MAIN)         # 豎
    g.diag(200, 630, 70, 200, weight=W_THIN)    # 撇
    g.diag(205, 630, 340, 220, weight=W_THIN)   # 捺

    # ---- 兌：丷 ----
    g.dot(520, 790, w=W_DOT, h=96, slant=-14)   # 丷左
    g.dot(780, 790, w=W_DOT, h=96, slant=14)    # 丷右
    # ---- 兌：口 ----
    comp_kuchi(g, 480, 880, 418, 662, W_THIN)
    # ---- 兌：儿 ----
    g.diag(620, 400, 460, 60, weight=W_SEC)     # 撇
    g.vbar(840, 60, 418, weight=W_SEC)          # 豎
    g.hbar(840, 900, 102, weight=W_THIN)        # 豎彎鉤的橫
    return g


def glyph_ka_gu() -> Glyph:
    """過（11 画）＝ 辶（2）+ 咼（8）。

    咼區 x 418..906：冎（外框 414..506 / 814..906，上橫 734..826，
    內冂 518..602 / 718..802，上橫 648..732）+ 口（418..502 / 616..700，
    頂 438..522，底 158..242）。
    辶：點 78..162 / 652..748，豎 68..152，捺自 (150,200) 鋪到 (880,45)。
    """
    g = Glyph("uni904E", advance=1000, unicode=0x904E, note="過：辶 + 咼")

    # ---- 咼：冎 ----
    g.hbar(414, 906, 780, weight=W_SEC)         # 冎的橫（墨 734..826）
    g.vbar(460, 560, 826, weight=W_SEC)         # 冎的左豎
    g.vbar(860, 560, 826, weight=W_SEC)         # 冎的右豎
    g.hbar(518, 802, 690, weight=W_THIN)        # 內冂的橫（墨 648..732）
    g.vbar(560, 600, 732, weight=W_THIN)        # 內冂的左豎
    g.vbar(760, 600, 732, weight=W_THIN)        # 內冂的右豎
    # ---- 咼：口 ----
    comp_kuchi(g, 460, 700, 158, 522, W_THIN)
    # ---- 辶 ----
    comp_benzang(g, 0, 0)
    return g


# ===========================================================================
def build() -> list[Glyph]:
    """本批全部字形（24 个）。"""
    return [
        glyph_soku(),    # 側 U+5074
        glyph_kan(),     # 感 U+611F
        glyph_toku(),    # 特 U+7279
        glyph_jo(),      # 情 U+60C5
        glyph_ki(),      # 基 U+57FA
        glyph_shima(),   # 島 U+5CF6
        glyph_asa(),     # 朝 U+671D
        glyph_sagi(),    # 提 U+63D0
        glyph_un(),      # 運 U+904B
        glyph_shu(),     # 終 U+7D42
        glyph_kyo(),     # 挙 U+6319
        glyph_seki(),    # 勢 U+52E2
        glyph_gen(),     # 減 U+6E1B
        glyph_yoh(),     # 容 U+5BB9
        glyph_den(),     # 電 U+96FB
        glyph_sai(),     # 歳 U+6B73
        glyph_no(),      # 能 U+80FD
        glyph_oki(),     # 置 U+7F6E
        glyph_shin(),    # 真 U+771F
        glyph_nagare(),  # 流 U+6D41
        glyph_kaku(),    # 格 U+683C
        glyph_ka_gu(),   # 過 U+904E
        glyph_ze(),      # 税 U+7A0E
        glyph_ka(),      # 検 U+691C
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s3-003.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
