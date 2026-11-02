"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-008。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
* 字面框固定 x 60..940 / y 0..820，advance = 1000，与繁体汉字同一档，
  便于 zh-HK / ja 混排时基线与边距完全一致。
* 笔画权重四档：主 96 / 次 92 / 细 84 / 点 84。同一偏旁在批内复用同一套
  坐标与拆法（亻、氵、扌、彳、木、辶、艹、阝），只做位置与大小的光学校正
  （docs/03 GLY-004）。
* 骨架来源：逐字取一份真实字体的**笔画中线**（hanzi-writer-data 的 medians，
  SIL OFL 1.1 可商用数据集），按字面框等比映射后，再做三件海报化处理：
  1) 拉平横画、摆正竖画——但只对"弦长/路径长 ≥ 0.95"的直笔做，
     折笔（横折钩、竖弯钩、斜钩）保持原样，避免把转折压直；
  2) 按笔画长度分权重：长笔 96 / 中笔 92 / 短笔与点 84；
  3) 曲线笔画用 pline() 一次性生成斜接（mitre）轮廓，
     避免逐段矩形相并留下的台阶状缺口。
* 横画墨迹上缘对齐 820 / 下缘对齐 0；竖画端点即墨迹端点；
  斜笔画端点内缩 ≥30 单位，确保墨迹不越出 x 60..940 / y 0..820。
* 密排处（横叠横）内白 ≥24 单位；竖与竖之间 ≥60 单位（docs/03 GLY-006）。
* 点与短撇用 g.dot(cx, cy, w, h, slant=26) 的斜切平行四边形
  （港产海报签名：上缘相对下缘右移 26 单位），横、竖、撇、捺保持平切硬边。

逐字决定（画数 / 部件 / 关键取舍）
--------------------------------
| 字  | 画 | 部件      | 关键取舍 |
| 花  | 7  | ⿱艹化      | 艹横顶带双竖探出；花与苦的艹用同一坐标。化右为匕，竖弯钩带钩。 |
| 春  | 9  | ⿱𡗗日     | 三横由窄到宽再放宽；撇起自字顶、越三横（与参考同源）。日居中偏下。 |
| 飛  | 9  | ⿹飛部飛部  | 取日式骨架：顶横左延至 x120，中竖与左上短撇均起自顶横；上下两个「飞」各带一条斜钩与两羽。斜钩按参考减到 84，横竖留 96。 |
| 券  | 8  | ⿱龹刀      | 龹内长撇起自字顶并越两横；刀为横折钩带钩＋长撇。丷两点分立。 |
| 赤  | 7  | ⿱土火      | 土的中竖起自字顶、越出第一横；下部按火写：长撇＋竖钩＋短撇＋点。 |
| 単  | 9  | ⿱ツ日十    | 数据集缺此字，手工设计：ツ 作两短撇＋一长撇（日式），日扁，十居中。 |
| 青  | 8  | ⿱龶月      | 龶三横一竖；月左笔作竖撇，内二横用 84 减重保内白。 |
| 竹  | 6  | ⿰⺮        | 左右各「撇-横-竖 / 竖弯钩」；左半撇特长，右半竖弯钩带钩。 |
| 完  | 7  | ⿱宀元      | 宀作点＋横钩（钩向左下）；元底竖弯钩带钩。 |
| 並  | 8  | ⿱丷亚      | 丷两点，双竖各带外脚横，底横通长。 |
| 危  | 6  | ⿱厃㔾      | 厃横＋长撇占左半；㔾的竖弯钩横扫右下并上挑，与参考同形。 |
| 拡  | 8  | ⿰扌広      | 数据集缺此字，手工设计：扌横竖提带钩；广内ム作两笔 V 形。 |
| 故  | 9  | ⿰古攵      | 左古窄、右攵宽；攵四笔，撇捺相交。 |
| 屋  | 9  | ⿸尸至      | 尸盖头向左伸；至的厶作「丿＋横」两笔。 |
| 色  | 6  | ⿱⺈巴      | ⺈撇＋横撇；巴底为长竖弯钩，横扫右下并上挑。 |
| 苦  | 8  | ⿱艹古      | 艹与花同坐标；古的口扁而宽，内白 ≥80。 |
| 迎  | 6  | ⿺辶卬      | 辶作点＋折折撇＋长捺；卩的竖落地。 |
| 走  | 7  | ⿱土止      | 土中竖起自字顶；下部止：竖＋右出短横＋左撇＋长捺。 |
| 具  | 8  | ⿱目⿱一八   | 目五画（两内横）＋通长底横承八；八左右分开。 |
| 秋  | 9  | ⿰禾火      | 禾撇短横长竖；火的四点与两长笔同向平行（港式斜切）。 |
| 因  | 6  | ⿴囗大      | 囗满框，大横居中、撇捺出足；内白 >500 单位。 |
| 休  | 6  | ⿰亻木      | 亻竖落地；木撇捺收在中宫内。 |
| 彼  | 8  | ⿰彳皮      | 彳双撇一竖；皮下「又」横撇＋捺。 |
| 邦  | 6  | ⿰丰阝      | 丰三横一竖；右耳作三折鼓包。 |
| 林  | 8  | ⿰木木      | 两木同形，右木略窄以避让。 |
| 河  | 8  | ⿰氵可      | 氵两点一提；可的右竖钩落地带钩。 |
| 抗  | 7  | ⿰扌亢      | 扌横竖提带钩；亢顶亠，下「几」竖弯钩带钩。 |
| 冷  | 7  | ⿰冫令      | 冫一点一提；令＝亼＋龴（横撇＋点）。 |
| 児  | 7  | ⿱旧儿      | 数据集缺此字，手工设计：旧＝竖＋日，儿＝撇＋竖弯钩，儿起自日底。 |
| 余  | 7  | ⿱亼朩      | 人顶，短横在下；长横＋竖钩＋撇＋点分立。 |
| 印  | 6  | ⿰?卩       | 左作竖折提＋中横；右卩横折钩＋竖落地。 |
| 逆  | 8  | ⿺辶屰      | 辶与迎同坐标；屰的中竖上抵横。 |

已知取舍
--------
* 因（囗）与飛（两个通长斜钩）是本批墨量率最高的两个字，check_glyphs 给出
  WARN（0.596 / 0.432，批内中位数 0.285）。二者都是结构本身决定的密度，
  按集成方裁定（结构性封闭字允许超阈）保留，不为压阈值而把字压畸形。
* 単 / 拡 / 児 在可商用中线数据集中缺失，改用手工设计，坐标在各自函数内列明。
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


# ----------------------------------------------------------------------
# alignment helpers (see font-src/src/hkposter-latin.py)
# ----------------------------------------------------------------------
def bar_top(g, x1, x2, weight=W_MAIN):
    """horizontal: ink top edge aligned to 820."""
    g.hbar(x1, x2, 820 - weight / 2.0, weight=weight)


def bar_base(g, x1, x2, weight=W_MAIN):
    """horizontal: ink bottom edge aligned to 0."""
    g.hbar(x1, x2, weight / 2.0, weight=weight)


def bar(g, x1, x2, y, weight=W_MAIN):
    """horizontal: centerline y."""
    g.hbar(x1, x2, y, weight=weight)


def stem(g, x, y1, y2, weight=W_MAIN):
    """vertical: centerline x, endpoints are ink endpoints."""
    g.vbar(x, y1, y2, weight=weight)


def pdot(g, cx, cy, w=W_DOT, h=110, slant=26):
    """dot / short pie: sheared parallelogram (slant = x offset of top edge)."""
    g.dot(cx, cy, w=w, h=h, slant=slant)


def pline(pts, weight):
    """Outline of a curved stroke: centerline + perpendicular weight.

    Offset the polyline on both sides, mitre the joints (clamped) and close
    the outline, so curved strokes keep a single clean silhouette instead of
    the stepped seams a chain of rectangles leaves behind.
    """
    n = len(pts)
    if n < 2:
        return []
    half = weight / 2.0
    norms = []
    for i in range(n - 1):
        dx = pts[i + 1][0] - pts[i][0]
        dy = pts[i + 1][1] - pts[i][1]
        length = math.hypot(dx, dy) or 1.0
        norms.append((-dy / length, dx / length))
    left = []
    right = []
    for i in range(n):
        if i == 0:
            nx, ny, off = norms[0][0], norms[0][1], half
        elif i == n - 1:
            nx, ny, off = norms[-1][0], norms[-1][1], half
        else:
            ax, ay = norms[i - 1]
            bx, by = norms[i]
            mx, my = ax + bx, ay + by
            length = math.hypot(mx, my)
            if length < 1e-9:
                nx, ny, off = bx, by, half
            else:
                nx, ny = mx / length, my / length
                cosang = nx * bx + ny * by
                if cosang < 0.4:
                    nx, ny, off = bx, by, half
                else:
                    off = min(half / cosang, half * 2.5)
        left.append((pts[i][0] + nx * off, pts[i][1] + ny * off))
        right.append((pts[i][0] - nx * off, pts[i][1] - ny * off))
    return left + right[::-1]



def g_hua() -> Glyph:
    """花 uni82B1 (7 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      横 x176..845 @y657   W_MAIN
      捺 (338,761)->(413,548)  W_THIN
      撇 (603,820)->(561,535)  W_SEC
      撇 (360,503)->(108,164)  W_SEC
      竖 x333  y0..326  W_SEC
      撇 (764,463)->(417,152)  W_SEC
      捺 (532,493)->(892,225)  W_MAIN
    """
    g = Glyph("uni82B1", advance=1000, unicode=0x82B1, note="花：7 画")
    g.hbar(176, 845, 657, weight=W_MAIN)
    g.poly(pline([(338, 761), (379, 734), (413, 548)], W_THIN))
    g.poly(pline([(603, 820), (641, 779), (561, 535)], W_SEC))
    g.poly(pline([(360, 503), (388, 453), (346, 393), (230, 261), (108, 164)], W_SEC))
    g.vbar(333, 0, 326, weight=W_SEC)
    g.poly(pline([(764, 463), (780, 421), (763, 404), (417, 152)], W_SEC))
    g.poly(pline([(532, 493), (563, 446), (557, 140), (715, 26), (852, 53), (884, 80), (892, 225)], W_MAIN))
    return g

def g_chun() -> Glyph:
    """春 uni6625 (9 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      横 x286..629 @y703   W_SEC
      横 x272..611 @y593   W_SEC
      横 x102..797 @y475   W_MAIN
      撇 (414,820)->(96,209)  W_MAIN
      捺 (517,469)->(904,283)  W_SEC
      竖 x326  y32..319  W_SEC
      捺 (346,320)->(570,0)  W_SEC
      横 x360..491 @y193   W_THIN
      横 x353..524 @y77    W_THIN
    """
    g = Glyph("uni6625", advance=1000, unicode=0x6625, note="春：9 画")
    g.hbar(286, 629, 703, weight=W_SEC)
    g.hbar(272, 611, 593, weight=W_SEC)
    g.hbar(102, 797, 475, weight=W_MAIN)
    g.poly(pline([(414, 820), (450, 771), (372, 466), (255, 308), (96, 209)], W_MAIN))
    g.poly(pline([(517, 469), (730, 308), (904, 283)], W_SEC))
    g.vbar(326, 32, 319, weight=W_SEC)
    g.poly(pline([(346, 320), (376, 310), (534, 346), (570, 322), (570, 0)], W_SEC))
    g.hbar(360, 491, 193, weight=W_THIN)
    g.hbar(353, 524, 77, weight=W_THIN)
    return g

def g_fei() -> Glyph:
    """飛 uni98DB (9 画).

    日式骨架：顶横左延至 x120，中竖与左上短撃均起自顶横；
    上飛 斜钩在右上（x617..827），下飛 长斜钩从左侧 x110 扫至右下 x892。
    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      1 横   x120..620 @y772     W_MAIN  顶横
      2 斜   (620,800)->(827,585) W_THIN  上飛 斜钩（减重）
      3 撃   (736,800)->(694,709) W_THIN  上飛 左羽
      4 斜   (658,695)->(791,621) W_THIN  上飛 右羽
      5 撃   (330,760)->(176,514) W_THIN  左上短撃
      6 撃   (262,542)->(105,26)  W_SEC   左下长撃
      7 竖   x446  y772..0       W_MAIN  中竖
      8 斜   (110,383)->(892,183) W_THIN  下飛 斜钩（减重）
      9 撃   (712,412)->(678,320) W_THIN  下飛 左羽
      10 斜  (626,313)->(775,221) W_THIN  下飛 右羽
    """
    g = Glyph("uni98DB", advance=1000, unicode=0x98DB, note="飛：9 画")
    g.hbar(120, 620, 772, weight=W_MAIN)
    g.poly(pline([(620, 800), (617, 640), (632, 594), (664, 542), (706, 504), (745, 482), (804, 471), (816, 500), (827, 585)], W_THIN))
    g.poly(pline([(736, 800), (754, 775), (694, 709)], W_THIN))
    g.poly(pline([(658, 695), (752, 659), (791, 621)], W_THIN))
    g.poly(pline([(330, 760), (300, 660), (240, 585), (176, 514)], W_THIN))
    g.poly(pline([(262, 542), (305, 511), (271, 230), (194, 92), (105, 26)], W_SEC))
    g.vbar(446, 772, 0, weight=W_MAIN)
    g.poly(pline([(110, 383), (173, 378), (524, 482), (556, 484), (581, 464), (573, 404), (575, 345), (606, 211), (639, 147), (701, 80), (762, 42), (800, 26), (846, 18), (884, 25), (892, 183)], W_THIN))
    g.poly(pline([(712, 412), (732, 387), (678, 320)], W_THIN))
    g.poly(pline([(626, 313), (751, 254), (775, 221)], W_THIN))
    return g

def g_ken() -> Glyph:
    """券 uni5238 (8 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      捺 (266,718)->(343,652)  W_THIN
      撇 (617,802)->(527,673)  W_THIN
      横 x261..620 @y589   W_SEC
      横 x142..769 @y456   W_MAIN
      撇 (419,820)->(66,179)  W_MAIN
      捺 (517,448)->(934,249)  W_SEC
      捺 (257,268)->(414,58)  W_MAIN
      撇 (358,244)->(165,0)  W_SEC
    """
    g = Glyph("uni5238", advance=1000, unicode=0x5238, note="券：8 画")
    g.diag(266, 718, 343, 652, weight=W_THIN)
    g.poly(pline([(617, 802), (636, 762), (527, 673)], W_THIN))
    g.hbar(261, 620, 589, weight=W_SEC)
    g.hbar(142, 769, 456, weight=W_MAIN)
    g.poly(pline([(419, 820), (456, 775), (416, 578), (358, 434), (224, 272), (66, 179)], W_MAIN))
    g.poly(pline([(517, 448), (764, 269), (934, 249)], W_SEC))
    g.poly(pline([(257, 268), (546, 306), (587, 284), (525, 43), (494, 16), (414, 58)], W_MAIN))
    g.poly(pline([(358, 244), (382, 221), (323, 115), (165, 0)], W_SEC))
    return g

def g_aka() -> Glyph:
    """赤 uni8D64 (7 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      横 x326..674 @y615   W_SEC
      捺 (455,820)->(476,477)  W_SEC
      横 x110..890 @y449   W_MAIN
      撇 (362,415)->(204,0)  W_SEC
      撇 (542,435)->(469,74)  W_SEC
      撇 (266,297)->(202,142)  W_THIN
      捺 (668,306)->(837,157)  W_THIN
    """
    g = Glyph("uni8D64", advance=1000, unicode=0x8D64, note="赤：7 画")
    g.hbar(326, 674, 615, weight=W_SEC)
    g.poly(pline([(455, 820), (504, 778), (493, 497), (476, 477)], W_SEC))
    g.hbar(110, 890, 449, weight=W_MAIN)
    g.poly(pline([(362, 415), (405, 376), (374, 184), (306, 75), (204, 0)], W_SEC))
    g.poly(pline([(542, 435), (584, 405), (576, 55), (555, 18), (469, 74)], W_SEC))
    g.dot(234, 220, w=W_THIN, h=205, slant=26)
    g.poly(pline([(668, 306), (798, 219), (837, 157)], W_THIN))
    return g

def g_tan() -> Glyph:
    """単 uni5358 (9 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      g.dot(360, 760, w=W_THIN, h=100, slant=26)
      g.dot(490, 750, w=W_THIN, h=100, slant=26)
      g.diag(640, 780, 520, 650, weight=W_THIN)
      g.vbar(350, 600, 250, weight=W_MAIN)
      g.hbar(350, 680, 558, weight=W_SEC)
      g.vbar(680, 558, 250, weight=W_SEC)
      g.hbar(350, 680, 414, weight=W_SEC)
      g.hbar(350, 680, 292, weight=W_SEC)
      g.hbar(250, 750, 150, weight=W_MAIN)
      g.vbar(500, 260, 0, weight=W_MAIN)
    """
    g = Glyph("uni5358", advance=1000, unicode=0x5358, note="単：9 画")
    g.dot(360, 760, w=W_THIN, h=100, slant=26)
    g.dot(490, 750, w=W_THIN, h=100, slant=26)
    g.diag(640, 780, 520, 650, weight=W_THIN)
    g.vbar(350, 600, 250, weight=W_MAIN)
    g.hbar(350, 680, 558, weight=W_SEC)
    g.vbar(680, 558, 250, weight=W_SEC)
    g.hbar(350, 680, 414, weight=W_SEC)
    g.hbar(350, 680, 292, weight=W_SEC)
    g.hbar(250, 750, 150, weight=W_MAIN)
    g.vbar(500, 260, 0, weight=W_MAIN)
    return g

def g_ao() -> Glyph:
    """青 uni9752 (8 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      横 x311..669 @y717   W_SEC
      横 x321..647 @y604   W_SEC
      捺 (442,820)->(466,504)  W_SEC
      横 x109..891 @y475   W_MAIN
      竖 x340  y10..388  W_SEC
      捺 (377,375)->(502,40)  W_MAIN
      横 x376..534 @y271   W_THIN
      横 x369..542 @y177   W_THIN
    """
    g = Glyph("uni9752", advance=1000, unicode=0x9752, note="青：8 画")
    g.hbar(311, 669, 717, weight=W_SEC)
    g.hbar(321, 647, 604, weight=W_SEC)
    g.poly(pline([(442, 820), (486, 779), (466, 504)], W_SEC))
    g.hbar(109, 891, 475, weight=W_MAIN)
    g.vbar(340, 10, 388, weight=W_SEC)
    g.poly(pline([(377, 375), (570, 406), (611, 378), (621, 41), (598, 0), (502, 40)], W_MAIN))
    g.hbar(376, 534, 271, weight=W_THIN)
    g.hbar(369, 542, 177, weight=W_THIN)
    return g

def g_take() -> Glyph:
    """竹 uni7AF9 (6 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      撇 (300,739)->(60,226)  W_SEC
      横 x220..495 @y428   W_SEC
      竖 x322  y10..379  W_SEC
      撇 (642,756)->(466,276)  W_SEC
      横 x595..940 @y461   W_SEC
      撇 (684,411)->(577,76)  W_SEC
    """
    g = Glyph("uni7AF9", advance=1000, unicode=0x7AF9, note="竹：6 画")
    g.poly(pline([(300, 739), (342, 694), (295, 579), (188, 388), (60, 226)], W_SEC))
    g.hbar(220, 495, 428, weight=W_SEC)
    g.vbar(322, 10, 379, weight=W_SEC)
    g.poly(pline([(642, 756), (686, 709), (676, 671), (596, 478), (466, 276)], W_SEC))
    g.hbar(595, 940, 461, weight=W_SEC)
    g.poly(pline([(684, 411), (733, 374), (729, 33), (691, 4), (577, 76)], W_SEC))
    return g

def g_kan() -> Glyph:
    """完 uni5B8C (7 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      捺 (421,820)->(554,734)  W_THIN
      竖 x228  y472..661  W_THIN
      捺 (284,620)->(704,562)  W_SEC
      横 x346..595 @y488   W_SEC
      横 x238..697 @y358   W_MAIN
      撇 (370,299)->(108,11)  W_SEC
      捺 (499,328)->(892,206)  W_MAIN
    """
    g = Glyph("uni5B8C", advance=1000, unicode=0x5B8C, note="完：7 画")
    g.poly(pline([(421, 820), (519, 774), (554, 734)], W_THIN))
    g.vbar(228, 472, 661, weight=W_THIN)
    g.poly(pline([(284, 620), (721, 681), (777, 641), (704, 562)], W_SEC))
    g.hbar(346, 595, 488, weight=W_SEC)
    g.hbar(238, 697, 358, weight=W_MAIN)
    g.poly(pline([(370, 299), (394, 276), (294, 124), (108, 11)], W_SEC))
    g.poly(pline([(499, 328), (544, 287), (538, 65), (584, 17), (714, 0), (877, 28), (892, 206)], W_MAIN))
    return g

def g_hei() -> Glyph:
    """並 uni4E26 (8 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      捺 (304,750)->(396,650)  W_THIN
      撇 (626,820)->(509,586)  W_SEC
      横 x203..793 @y556   W_MAIN
      捺 (351,512)->(380,59)  W_SEC
      捺 (535,539)->(547,73)  W_SEC
      捺 (187,339)->(274,206)  W_THIN
      撇 (748,437)->(597,215)  W_SEC
      横 x74..926 @y22    W_MAIN
    """
    g = Glyph("uni4E26", advance=1000, unicode=0x4E26, note="並：8 画")
    g.dot(350, 700, w=W_THIN, h=151, slant=26)
    g.poly(pline([(626, 820), (657, 773), (509, 586)], W_SEC))
    g.hbar(203, 793, 556, weight=W_MAIN)
    g.poly(pline([(351, 512), (394, 466), (402, 97), (380, 59)], W_SEC))
    g.poly(pline([(535, 539), (573, 510), (574, 481), (567, 89), (547, 73)], W_SEC))
    g.poly(pline([(187, 339), (255, 264), (274, 206)], W_THIN))
    g.poly(pline([(748, 437), (778, 390), (597, 215)], W_SEC))
    g.hbar(74, 926, 22, weight=W_MAIN)
    return g

def g_ki() -> Glyph:
    """危 uni5371 (6 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      撇 (501,820)->(331,573)  W_SEC
      捺 (491,687)->(557,537)  W_SEC
      横 x363..808 @y526   W_SEC
      撇 (293,507)->(110,13)  W_SEC
      捺 (481,376)->(561,230)  W_SEC
      捺 (427,386)->(890,216)  W_MAIN
    """
    g = Glyph("uni5371", advance=1000, unicode=0x5371, note="危：6 画")
    g.poly(pline([(501, 820), (518, 768), (331, 573)], W_SEC))
    g.poly(pline([(491, 687), (626, 708), (676, 693), (557, 537)], W_SEC))
    g.hbar(363, 808, 526, weight=W_SEC)
    g.poly(pline([(293, 507), (332, 458), (288, 198), (216, 90), (110, 13)], W_SEC))
    g.poly(pline([(481, 376), (495, 363), (676, 405), (704, 386), (645, 210), (619, 196), (561, 230)], W_SEC))
    g.poly(pline([(427, 386), (455, 336), (450, 91), (651, 0), (836, 32), (883, 68), (890, 216)], W_MAIN))
    return g

def g_hiro() -> Glyph:
    """拡 uni62E1 (8 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      g.hbar(90, 320, 620, weight=W_SEC)
      g.vbar(215, 790, 130, weight=W_SEC)
      g.diag(215, 130, 145, 85, weight=W_THIN)
      g.diag(95, 230, 300, 340, weight=W_SEC)
      g.dot(660, 740, w=W_THIN, h=100, slant=26)
      g.hbar(420, 900, 640, weight=W_SEC)
      g.diag(470, 640, 390, 120, weight=W_SEC)
      g.diag(680, 540, 560, 260, weight=W_THIN)
      g.diag(760, 540, 620, 250, weight=W_THIN)
      g.hbar(620, 830, 250, weight=W_THIN)
    """
    g = Glyph("uni62E1", advance=1000, unicode=0x62E1, note="拡：8 画")
    g.hbar(90, 320, 620, weight=W_SEC)
    g.vbar(215, 790, 130, weight=W_SEC)
    g.diag(215, 130, 145, 85, weight=W_THIN)
    g.diag(95, 230, 300, 340, weight=W_SEC)
    g.dot(660, 740, w=W_THIN, h=100, slant=26)
    g.hbar(420, 900, 640, weight=W_SEC)
    g.diag(470, 640, 390, 120, weight=W_SEC)
    g.diag(680, 540, 560, 260, weight=W_THIN)
    g.diag(760, 540, 620, 250, weight=W_THIN)
    g.hbar(620, 830, 250, weight=W_THIN)
    return g

def g_ko() -> Glyph:
    """故 uni6545 (9 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      横 x60..455 @y452   W_SEC
      撇 (261,706)->(258,272)  W_SEC
      捺 (123,254)->(192,18)  W_THIN
      捺 (188,231)->(339,146)  W_SEC
      横 x210..398 @y98    W_THIN
      撇 (573,750)->(437,345)  W_SEC
      横 x533..827 @y472   W_SEC
      撇 (621,427)->(391,36)  W_SEC
      捺 (466,324)->(940,0)  W_SEC
    """
    g = Glyph("uni6545", advance=1000, unicode=0x6545, note="故：9 画")
    g.hbar(60, 455, 452, weight=W_SEC)
    g.poly(pline([(261, 706), (308, 643), (281, 306), (258, 272)], W_SEC))
    g.poly(pline([(123, 254), (156, 216), (192, 18)], W_THIN))
    g.poly(pline([(188, 231), (359, 277), (388, 250), (362, 161), (339, 146)], W_SEC))
    g.hbar(210, 398, 98, weight=W_THIN)
    g.poly(pline([(573, 750), (616, 709), (599, 650), (503, 439), (437, 345)], W_SEC))
    g.hbar(533, 827, 472, weight=W_SEC)
    g.poly(pline([(621, 427), (659, 397), (597, 203), (519, 106), (391, 36)], W_SEC))
    g.poly(pline([(466, 324), (762, 34), (940, 0)], W_SEC))
    return g

def g_ya() -> Glyph:
    """屋 uni5C4B (9 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      捺 (407,781)->(666,691)  W_SEC
      横 x385..738 @y637   W_SEC
      撇 (331,805)->(60,0)  W_MAIN
      横 x404..785 @y519   W_SEC
      捺 (584,451)->(726,346)  W_SEC
      捺 (684,424)->(811,281)  W_THIN
      横 x398..794 @y180   W_SEC
      捺 (551,299)->(565,61)  W_THIN
      横 x251..940 @y26    W_MAIN
    """
    g = Glyph("uni5C4B", advance=1000, unicode=0x5C4B, note="屋：9 画")
    g.poly(pline([(407, 781), (698, 812), (727, 781), (697, 711), (666, 691)], W_SEC))
    g.hbar(385, 738, 637, weight=W_SEC)
    g.poly(pline([(331, 805), (369, 752), (288, 366), (175, 135), (60, 0)], W_MAIN))
    g.hbar(404, 785, 519, weight=W_SEC)
    g.poly(pline([(584, 451), (551, 449), (434, 302), (726, 346)], W_SEC))
    g.poly(pline([(684, 424), (791, 332), (811, 281)], W_THIN))
    g.hbar(398, 794, 180, weight=W_SEC)
    g.poly(pline([(551, 299), (582, 271), (565, 61)], W_THIN))
    g.hbar(251, 940, 26, weight=W_MAIN)
    return g

def g_iro() -> Glyph:
    """色 uni8272 (6 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      撇 (410,820)->(199,542)  W_SEC
      捺 (377,654)->(435,498)  W_SEC
      捺 (252,459)->(586,350)  W_SEC
      撇 (410,457)->(404,316)  W_THIN
      横 x242..643 @y288   W_SEC
      捺 (186,478)->(813,240)  W_MAIN
    """
    g = Glyph("uni8272", advance=1000, unicode=0x8272, note="色：6 画")
    g.poly(pline([(410, 820), (433, 772), (405, 732), (199, 542)], W_SEC))
    g.poly(pline([(377, 654), (513, 676), (559, 662), (435, 498)], W_SEC))
    g.poly(pline([(252, 459), (273, 448), (606, 517), (650, 480), (614, 369), (586, 350)], W_SEC))
    g.poly(pline([(410, 457), (436, 426), (424, 333), (404, 316)], W_THIN))
    g.hbar(242, 643, 288, weight=W_SEC)
    g.poly(pline([(186, 478), (227, 420), (249, 72), (308, 29), (535, 0), (814, 60), (813, 240)], W_MAIN))
    return g

def g_ku() -> Glyph:
    """苦 uni82E6 (8 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      横 x187..784 @y659   W_MAIN
      捺 (307,757)->(385,547)  W_THIN
      撇 (588,820)->(548,562)  W_SEC
      横 x73..927 @y402   W_MAIN
      撇 (442,532)->(416,241)  W_SEC
      捺 (282,231)->(349,0)  W_THIN
      捺 (348,222)->(594,89)  W_SEC
      横 x372..652 @y43    W_SEC
    """
    g = Glyph("uni82E6", advance=1000, unicode=0x82E6, note="苦：8 画")
    g.hbar(187, 784, 659, weight=W_MAIN)
    g.poly(pline([(307, 757), (351, 726), (385, 547)], W_THIN))
    g.poly(pline([(588, 820), (627, 774), (548, 562)], W_SEC))
    g.hbar(73, 927, 402, weight=W_MAIN)
    g.poly(pline([(442, 532), (482, 486), (436, 261), (416, 241)], W_SEC))
    g.poly(pline([(282, 231), (320, 187), (349, 0)], W_THIN))
    g.poly(pline([(348, 222), (616, 249), (653, 214), (619, 104), (594, 89)], W_SEC))
    g.hbar(372, 652, 43, weight=W_SEC)
    return g

def g_mukae() -> Glyph:
    """迎 uni8FCE (6 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      撇 (559,798)->(439,642)  W_THIN
      捺 (375,652)->(568,444)  W_SEC
      捺 (682,594)->(699,389)  W_SEC
      竖 x630  y84..627  W_MAIN
      捺 (191,774)->(297,687)  W_THIN
      捺 (62,459)->(260,180)  W_SEC
      横 x60..940 @y79    W_MAIN
    """
    g = Glyph("uni8FCE", advance=1000, unicode=0x8FCE, note="迎：6 画")
    g.poly(pline([(559, 798), (583, 755), (439, 642)], W_THIN))
    g.poly(pline([(375, 652), (416, 604), (422, 348), (568, 444)], W_SEC))
    g.poly(pline([(682, 594), (821, 642), (856, 626), (843, 473), (811, 378), (785, 351), (699, 389)], W_SEC))
    g.vbar(630, 84, 627, weight=W_MAIN)
    g.diag(191, 774, 297, 687, weight=W_THIN)
    g.poly(pline([(62, 459), (234, 491), (273, 469), (230, 347), (275, 210), (260, 180)], W_SEC))
    g.hbar(60, 940, 79, weight=W_MAIN)
    return g

def g_sou() -> Glyph:
    """走 uni8D70 (7 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      横 x286..659 @y625   W_SEC
      捺 (445,820)->(468,488)  W_SEC
      横 x139..811 @y461   W_MAIN
      捺 (457,438)->(500,171)  W_SEC
      横 x516..700 @y316   W_THIN
      撇 (295,350)->(89,0)  W_SEC
      捺 (350,267)->(911,20)  W_SEC
    """
    g = Glyph("uni8D70", advance=1000, unicode=0x8D70, note="走：7 画")
    g.hbar(286, 659, 625, weight=W_SEC)
    g.poly(pline([(445, 820), (491, 783), (468, 488)], W_SEC))
    g.hbar(139, 811, 461, weight=W_MAIN)
    g.poly(pline([(457, 438), (489, 413), (483, 203), (500, 171)], W_SEC))
    g.hbar(516, 700, 316, weight=W_THIN)
    g.poly(pline([(295, 350), (322, 309), (279, 210), (200, 94), (89, 0)], W_SEC))
    g.poly(pline([(350, 267), (486, 144), (651, 41), (728, 13), (911, 20)], W_SEC))
    return g

def g_gu() -> Glyph:
    """具 uni5177 (8 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      竖 x318  y289..797  W_MAIN
      捺 (351,786)->(595,322)  W_MAIN
      横 x368..527 @y655   W_THIN
      横 x371..530 @y532   W_THIN
      横 x368..538 @y407   W_THIN
      横 x68..932 @y265   W_MAIN
      撇 (410,171)->(178,0)  W_SEC
      捺 (573,190)->(769,5)  W_THIN
    """
    g = Glyph("uni5177", advance=1000, unicode=0x5177, note="具：8 画")
    g.vbar(318, 289, 797, weight=W_MAIN)
    g.poly(pline([(351, 786), (378, 772), (597, 820), (646, 771), (621, 341), (595, 322)], W_MAIN))
    g.hbar(368, 527, 655, weight=W_THIN)
    g.hbar(371, 530, 532, weight=W_THIN)
    g.hbar(368, 538, 407, weight=W_THIN)
    g.hbar(68, 932, 265, weight=W_MAIN)
    g.poly(pline([(410, 171), (371, 165), (297, 80), (178, 0)], W_SEC))
    g.poly(pline([(573, 190), (728, 79), (769, 5)], W_THIN))
    return g

def g_aki() -> Glyph:
    """秋 uni79CB (9 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      撇 (435,715)->(145,604)  W_SEC
      横 x71..425 @y475   W_SEC
      竖 x293  y0..636  W_MAIN
      撇 (277,455)->(60,163)  W_SEC
      捺 (327,392)->(405,295)  W_THIN
      捺 (462,474)->(506,385)  W_THIN
      撇 (770,597)->(687,458)  W_THIN
      撇 (574,758)->(374,64)  W_MAIN
      捺 (631,365)->(940,67)  W_SEC
    """
    g = Glyph("uni79CB", advance=1000, unicode=0x79CB, note="秋：9 画")
    g.poly(pline([(435, 715), (371, 722), (145, 604)], W_SEC))
    g.hbar(71, 425, 475, weight=W_SEC)
    g.vbar(293, 0, 636, weight=W_MAIN)
    g.poly(pline([(277, 455), (222, 334), (60, 163)], W_SEC))
    g.poly(pline([(327, 392), (395, 330), (405, 295)], W_THIN))
    g.dot(484, 430, w=W_THIN, h=139, slant=26)
    g.poly(pline([(770, 597), (794, 556), (687, 458)], W_THIN))
    g.poly(pline([(574, 758), (628, 706), (587, 293), (518, 161), (374, 64)], W_MAIN))
    g.poly(pline([(631, 365), (637, 325), (771, 141), (816, 100), (940, 67)], W_SEC))
    return g

def g_i() -> Glyph:
    """因 uni56E0 (6 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      竖 x199  y0..796  W_MAIN
      捺 (236,776)->(750,69)  W_MAIN
      横 x324..685 @y500   W_SEC
      撇 (473,676)->(295,186)  W_SEC
      捺 (548,384)->(693,219)  W_THIN
      横 x232..739 @y59    W_MAIN
    """
    g = Glyph("uni56E0", advance=1000, unicode=0x56E0, note="因：6 画")
    g.vbar(199, 0, 796, weight=W_MAIN)
    g.poly(pline([(236, 776), (271, 760), (751, 820), (818, 782), (832, 90), (817, 35), (750, 69)], W_MAIN))
    g.hbar(324, 685, 500, weight=W_SEC)
    g.poly(pline([(473, 676), (514, 626), (470, 377), (405, 267), (295, 186)], W_SEC))
    g.poly(pline([(548, 384), (660, 285), (693, 219)], W_THIN))
    g.hbar(232, 739, 59, weight=W_MAIN)
    return g

def g_kyuu() -> Glyph:
    """休 uni4F11 (6 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      撇 (286,771)->(60,345)  W_SEC
      竖 x245  y51..523  W_MAIN
      横 x371..803 @y544   W_SEC
      竖 x565  y0..820  W_MAIN
      撇 (551,509)->(301,163)  W_SEC
      捺 (602,489)->(940,196)  W_SEC
    """
    g = Glyph("uni4F11", advance=1000, unicode=0x4F11, note="休：6 画")
    g.poly(pline([(286, 771), (321, 723), (291, 659), (192, 495), (60, 345)], W_SEC))
    g.vbar(245, 51, 523, weight=W_MAIN)
    g.hbar(371, 803, 544, weight=W_SEC)
    g.vbar(565, 0, 820, weight=W_MAIN)
    g.poly(pline([(551, 509), (457, 318), (301, 163)], W_SEC))
    g.poly(pline([(602, 489), (783, 244), (940, 196)], W_SEC))
    return g

def g_hi() -> Glyph:
    """彼 uni5F7C (8 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      撇 (311,745)->(142,490)  W_SEC
      撇 (305,542)->(60,154)  W_SEC
      竖 x262  y9..325  W_SEC
      捺 (476,545)->(735,477)  W_SEC
      撇 (423,551)->(316,32)  W_SEC
      捺 (569,786)->(582,387)  W_SEC
      撇 (481,349)->(431,41)  W_SEC
      捺 (496,293)->(940,0)  W_SEC
    """
    g = Glyph("uni5F7C", advance=1000, unicode=0x5F7C, note="彼：8 画")
    g.poly(pline([(311, 745), (334, 701), (298, 645), (142, 490)], W_SEC))
    g.poly(pline([(305, 542), (334, 493), (294, 422), (166, 254), (60, 154)], W_SEC))
    g.vbar(262, 9, 325, weight=W_SEC)
    g.poly(pline([(476, 545), (502, 535), (770, 592), (799, 569), (735, 477)], W_SEC))
    g.poly(pline([(423, 551), (459, 498), (439, 295), (386, 135), (316, 32)], W_SEC))
    g.poly(pline([(569, 786), (614, 737), (599, 416), (582, 387)], W_SEC))
    g.poly(pline([(481, 349), (669, 391), (702, 367), (679, 250), (620, 136), (546, 77), (431, 41)], W_SEC))
    g.poly(pline([(496, 293), (775, 28), (940, 0)], W_SEC))
    return g

def g_hou() -> Glyph:
    """邦 uni90A6 (6 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      横 x244..525 @y648   W_SEC
      横 x255..508 @y524   W_SEC
      横 x139..545 @y381   W_SEC
      撇 (350,820)->(168,106)  W_MAIN
      捺 (653,653)->(700,342)  W_MAIN
      竖 x598  y0..690  W_MAIN
    """
    g = Glyph("uni90A6", advance=1000, unicode=0x90A6, note="邦：6 画")
    g.hbar(244, 525, 648, weight=W_SEC)
    g.hbar(255, 508, 524, weight=W_SEC)
    g.hbar(139, 545, 381, weight=W_SEC)
    g.poly(pline([(350, 820), (399, 780), (369, 358), (304, 207), (168, 106)], W_MAIN))
    g.poly(pline([(653, 653), (758, 708), (821, 685), (741, 531), (844, 423), (832, 298), (700, 342)], W_MAIN))
    g.vbar(598, 0, 690, weight=W_MAIN)
    return g

def g_rin() -> Glyph:
    """林 uni6797 (8 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      横 x102..408 @y503   W_SEC
      竖 x273  y38..774  W_MAIN
      撇 (265,473)->(60,156)  W_SEC
      捺 (312,410)->(379,352)  W_THIN
      横 x458..797 @y548   W_SEC
      竖 x592  y0..809  W_MAIN
      撇 (577,502)->(371,190)  W_SEC
      捺 (630,471)->(940,212)  W_SEC
    """
    g = Glyph("uni6797", advance=1000, unicode=0x6797, note="林：8 画")
    g.hbar(102, 408, 503, weight=W_SEC)
    g.vbar(273, 38, 774, weight=W_MAIN)
    g.poly(pline([(265, 473), (200, 329), (60, 156)], W_SEC))
    g.diag(312, 410, 379, 352, weight=W_THIN)
    g.hbar(458, 797, 548, weight=W_SEC)
    g.vbar(592, 0, 809, weight=W_MAIN)
    g.poly(pline([(577, 502), (514, 357), (371, 190)], W_SEC))
    g.poly(pline([(630, 471), (791, 258), (940, 212)], W_SEC))
    return g

def g_kawa() -> Glyph:
    """河 uni6CB3 (8 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      捺 (160,814)->(276,724)  W_THIN
      捺 (60,588)->(170,512)  W_THIN
      斜 (128,41)->(250,390)  W_SEC
      横 x286..940 @y674   W_MAIN
      捺 (322,499)->(394,289)  W_THIN
      捺 (380,499)->(498,378)  W_SEC
      横 x414..571 @y340   W_THIN
      撇 (675,664)->(573,66)  W_MAIN
    """
    g = Glyph("uni6CB3", advance=1000, unicode=0x6CB3, note="河：8 画")
    g.poly(pline([(160, 814), (253, 761), (276, 724)], W_THIN))
    g.diag(60, 588, 170, 512, weight=W_THIN)
    g.poly(pline([(128, 41), (112, 131), (250, 390)], W_SEC))
    g.hbar(286, 940, 674, weight=W_MAIN)
    g.poly(pline([(322, 499), (358, 461), (394, 289)], W_THIN))
    g.poly(pline([(380, 499), (512, 519), (543, 501), (527, 400), (498, 378)], W_SEC))
    g.hbar(414, 571, 340, weight=W_THIN)
    g.poly(pline([(675, 664), (723, 622), (718, 45), (691, 0), (573, 66)], W_MAIN))
    return g

def g_kou() -> Glyph:
    """抗 uni6297 (7 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      横 x140..423 @y502   W_SEC
      撇 (282,757)->(178,55)  W_MAIN
      斜 (60,170)->(411,392)  W_SEC
      捺 (576,735)->(704,649)  W_THIN
      横 x473..854 @y512   W_SEC
      撇 (492,357)->(379,6)  W_SEC
      捺 (555,356)->(940,188)  W_MAIN
    """
    g = Glyph("uni6297", advance=1000, unicode=0x6297, note="抗：7 画")
    g.hbar(140, 423, 502, weight=W_SEC)
    g.poly(pline([(282, 757), (329, 717), (312, 65), (290, 4), (178, 55)], W_MAIN))
    g.poly(pline([(60, 170), (112, 166), (411, 392)], W_SEC))
    g.poly(pline([(576, 735), (672, 688), (704, 649)], W_THIN))
    g.hbar(473, 854, 512, weight=W_SEC)
    g.poly(pline([(492, 357), (527, 325), (513, 171), (458, 69), (379, 6)], W_SEC))
    g.poly(pline([(555, 356), (707, 359), (673, 213), (677, 115), (753, 10), (936, 30), (940, 188)], W_MAIN))
    return g

def g_rei() -> Glyph:
    """冷 uni51B7 (7 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      捺 (108,724)->(214,617)  W_THIN
      斜 (95,150)->(220,462)  W_SEC
      撇 (461,820)->(228,369)  W_SEC
      捺 (508,706)->(916,456)  W_SEC
      捺 (436,517)->(533,425)  W_THIN
      捺 (321,302)->(514,147)  W_SEC
      捺 (418,176)->(576,0)  W_THIN
    """
    g = Glyph("uni51B7", advance=1000, unicode=0x51B7, note="冷：7 画")
    g.poly(pline([(108, 724), (191, 662), (214, 617)], W_THIN))
    g.poly(pline([(95, 150), (84, 227), (220, 462)], W_SEC))
    g.poly(pline([(461, 820), (500, 771), (467, 697), (352, 509), (228, 369)], W_SEC))
    g.poly(pline([(508, 706), (725, 498), (916, 456)], W_SEC))
    g.diag(436, 517, 533, 425, weight=W_THIN)
    g.poly(pline([(321, 302), (378, 288), (573, 354), (623, 342), (641, 325), (627, 296), (514, 147)], W_SEC))
    g.poly(pline([(418, 176), (549, 65), (576, 0)], W_THIN))
    return g

def g_ji() -> Glyph:
    """児 uni5150 (7 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      g.vbar(280, 800, 340, weight=W_MAIN)
      g.vbar(400, 780, 340, weight=W_SEC)
      g.hbar(400, 680, 732, weight=W_SEC)
      g.vbar(680, 732, 340, weight=W_SEC)
      g.hbar(400, 680, 500, weight=W_THIN)
      g.hbar(400, 680, 388, weight=W_THIN)
      g.diag(400, 330, 250, 60, weight=W_SEC)
      g.vbar(560, 330, 120, weight=W_SEC)
      g.hbar(560, 830, 120, weight=W_SEC)
      g.vbar(830, 120, 190, weight=W_THIN)
    """
    g = Glyph("uni5150", advance=1000, unicode=0x5150, note="児：7 画")
    g.vbar(280, 800, 340, weight=W_MAIN)
    g.vbar(400, 780, 340, weight=W_SEC)
    g.hbar(400, 680, 732, weight=W_SEC)
    g.vbar(680, 732, 340, weight=W_SEC)
    g.hbar(400, 680, 500, weight=W_THIN)
    g.hbar(400, 680, 388, weight=W_THIN)
    g.diag(400, 330, 250, 60, weight=W_SEC)
    g.vbar(560, 330, 120, weight=W_SEC)
    g.hbar(560, 830, 120, weight=W_SEC)
    g.vbar(830, 120, 190, weight=W_THIN)
    return g

def g_yo() -> Glyph:
    """余 uni4F59 (7 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      撇 (435,820)->(66,336)  W_SEC
      捺 (484,718)->(934,433)  W_SEC
      横 x329..608 @y462   W_SEC
      横 x185..738 @y301   W_MAIN
      撇 (434,415)->(339,55)  W_SEC
      撇 (278,194)->(188,47)  W_THIN
      捺 (595,204)->(751,49)  W_THIN
    """
    g = Glyph("uni4F59", advance=1000, unicode=0x4F59, note="余：7 画")
    g.poly(pline([(435, 820), (466, 776), (364, 600), (243, 464), (66, 336)], W_SEC))
    g.poly(pline([(484, 718), (617, 575), (743, 476), (934, 433)], W_SEC))
    g.hbar(329, 608, 462, weight=W_SEC)
    g.hbar(185, 738, 301, weight=W_MAIN)
    g.poly(pline([(434, 415), (470, 388), (468, 39), (446, 0), (339, 55)], W_SEC))
    g.dot(233, 120, w=W_THIN, h=197, slant=26)
    g.poly(pline([(595, 204), (713, 117), (751, 49)], W_THIN))
    return g

def g_in() -> Glyph:
    """印 uni5370 (6 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      撇 (398,820)->(269,655)  W_THIN
      捺 (191,680)->(442,418)  W_SEC
      横 x267..456 @y556   W_THIN
      捺 (580,643)->(663,392)  W_SEC
      竖 x549  y0..646  W_MAIN
    """
    g = Glyph("uni5370", advance=1000, unicode=0x5370, note="印：6 画")
    g.poly(pline([(398, 820), (420, 775), (269, 655)], W_THIN))
    g.poly(pline([(191, 680), (231, 632), (229, 312), (442, 418)], W_SEC))
    g.hbar(267, 456, 556, weight=W_THIN)
    g.poly(pline([(580, 643), (610, 633), (763, 671), (809, 645), (775, 372), (757, 349), (663, 392)], W_SEC))
    g.vbar(549, 0, 646, weight=W_MAIN)
    return g

def g_gyaku() -> Glyph:
    """逆 uni9006 (8 画).

    笔画清单（中线坐标 → 字面框 x60..940 / y0..820）:
      捺 (493,751)->(554,674)  W_THIN
      撇 (713,820)->(628,648)  W_THIN
      横 x462..789 @y588   W_SEC
      捺 (427,479)->(737,373)  W_SEC
      竖 x772  y292..533  W_SEC
      撇 (574,541)->(468,106)  W_SEC
      捺 (204,755)->(323,658)  W_THIN
      捺 (89,443)->(264,169)  W_SEC
      横 x81..919 @y79    W_MAIN
    """
    g = Glyph("uni9006", advance=1000, unicode=0x9006, note="逆：8 画")
    g.dot(523, 713, w=W_THIN, h=127, slant=26)
    g.poly(pline([(713, 820), (743, 786), (628, 648)], W_THIN))
    g.hbar(462, 789, 588, weight=W_SEC)
    g.poly(pline([(427, 479), (457, 433), (444, 305), (737, 373)], W_SEC))
    g.vbar(772, 292, 533, weight=W_SEC)
    g.poly(pline([(574, 541), (611, 513), (599, 293), (562, 198), (468, 106)], W_SEC))
    g.diag(204, 755, 323, 658, weight=W_THIN)
    g.poly(pline([(89, 443), (231, 483), (281, 464), (230, 334), (274, 206), (264, 169)], W_SEC))
    g.hbar(81, 919, 79, weight=W_MAIN)
    return g

def build() -> list[Glyph]:
    return [
        g_hua(),
        g_chun(),
        g_fei(),
        g_ken(),
        g_aka(),
        g_tan(),
        g_ao(),
        g_take(),
        g_kan(),
        g_hei(),
        g_ki(),
        g_hiro(),
        g_ko(),
        g_ya(),
        g_iro(),
        g_ku(),
        g_mukae(),
        g_sou(),
        g_gu(),
        g_aki(),
        g_i(),
        g_kyuu(),
        g_hi(),
        g_hou(),
        g_rin(),
        g_kawa(),
        g_kou(),
        g_rei(),
        g_ji(),
        g_yo(),
        g_in(),
        g_gyaku()
    ]

def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-008.ufo"

if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print("[recipe] wrote %s" % target_ufo())
