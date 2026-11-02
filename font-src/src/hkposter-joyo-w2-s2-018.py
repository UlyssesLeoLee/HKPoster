"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-018。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

整体取舍
--------
* 字面框 x 60..940 / y 0..820，advance 1000，与繁体汉字同档，便于中英日混排。
* 笔画权重：主 96 / 次 92 / 细 84 / 点 84。横竖撇捺一律平切硬边矩形，
  点与短撇用斜切平行四边形（slant 分档：-14 捺点 / +14 撇点 / 26 短撇 / 0 竖点）。
* 本批密度接近（6–9 画），批内统一原则：
  - 同部件复用同一套坐标与笔画拆法（GLY-004）：
    亻（伯・伐）、氵（沸・洪）、木（柿・枯・枢）、艹（芽・苗）、口（如・呉・怠）、
    心（忍・怠）、宀（宜・狩）、目/且（盲・貝・宜）、八（呉・共・貝）全部同坐标。
  - 左右结构分栏：左部件 ink ≤ 445，右部件 ink ≥ 470；上下结构分带。
  - 内白：叠横之间 ≥ 24 单位，竖与竖之间 ≥ 60 单位。
* 骨架来源：M PLUS 1p Black（主参照，比例与骨架）＋ Zen Kaku Gothic New Black
  （交叉校核）；KleeOne SemiBold（笔画走向参考）。只取骨架与比例，不描轮廓。

汉字骨架核对说明
----------------
* 呉（U+5449）7 画，上中下结构，笔顺 丨フ一フ一ノ丶，部件 𠃑＋口＋一＋八：
  左上竖、中上小「口」、中段「フ」（横折）、整宽横、底部八。
* 垂（U+5782）8 画：上短撇 ＋ 4 横 ＋ 2 竖（竖贯穿中段）。
* 貝・盲・宜・臭 之「目・且・自」均按参照字体作 3 道内白（3 槽），
  与 M PLUS 1p Black / Zen Kaku Gothic New Black 一致。
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

XL = 60.0          # 字面框左
XR = 940.0         # 字面框右
YT = 820.0         # 字面框上
YB = 0.0           # 字面框下


# ---------------------------------------------------------------- 构件 ------------------------------------------------------------
def _box(g: Glyph, x1: float, x2: float, y_top: float, y_bot: float,
         w: float = W_MAIN) -> None:
    """方框（口／日／田／目 框身）。ink 边：x [x1,x2]，y [y_bot,y_top]。"""
    g.hbar(x1, x2, y_top - w / 2.0, w)
    g.hbar(x1, x2, y_bot + w / 2.0, w)
    g.vbar(x1 + w / 2.0, y_top, y_bot + w, w)
    g.vbar(x2 - w / 2.0, y_top, y_bot + w, w)


def _dot_nan(g: Glyph, cx: float, cy: float, w: float = W_DOT, h: float = 110.0) -> None:
    """丶 右下点，slant -14（\" 形）。"""
    g.dot(cx, cy, w, h, -14)


def _dot_hyaku(g: Glyph, cx: float, cy: float, w: float = W_DOT, h: float = 100.0) -> None:
    """丿 左下点，slant +14（/ 形）。"""
    g.dot(cx, cy, w, h, 14)


def _dot_v(g: Glyph, cx: float, cy: float, w: float = W_DOT, h: float = 110.0) -> None:
    """竖点（亠的点），slant 0。"""
    g.dot(cx, cy, w, h, 0)


def _short_pie(g: Glyph, cx: float, cy: float, w: float = W_SEC, h: float = 118.0) -> None:
    """短撇（氵的上点），slant 26（/ 形）。"""
    g.dot(cx, cy, w, h, 26)


def _person(g: Glyph) -> None:
    """亻 —— 伯・伐 共用同一坐标。"""
    g.diag(400, 790, 190, 470, W_SEC)      # 撇
    g.vbar(265, 520, YB, W_MAIN)           # 竖


def _water(g: Glyph) -> None:
    """氵 —— 沸・洪 共用同一坐标。"""
    _short_pie(g, 190, 700)                # 上点（短撇）
    _dot_nan(g, 165, 480)                  # 中点（丶）
    g.diag(115, 220, 250, 320, W_SEC)      # 下提（撇）


def _tree(g: Glyph) -> None:
    """木 —— 柿・枯・枢 共用同一坐标。"""
    g.hbar(XL, 430, 640, W_SEC)            # 横
    g.vbar(255, YT, YB, W_MAIN)            # 竖
    g.diag(250, 600, 115, 160, W_SEC)      # 撇
    g.diag(260, 600, 400, 200, W_SEC)      # 捺


def _grass(g: Glyph) -> None:
    """艹 —— 芽・苗 共用同一坐标。"""
    g.hbar(XL, XR, 700, W_SEC)
    g.vbar(300, YT, 610, W_THIN)
    g.vbar(600, YT, 610, W_THIN)


def _heart(g: Glyph) -> None:
    """心 —— 忍・怠 共用同一坐标（ink y 0..280）。"""
    _dot_nan(g, 125, 165)                  # 左点
    g.hbar(150, 880, 60, W_SEC)            # 卧钩底
    g.vbar(838, 60, 170, W_THIN)           # 卧钩挑
    _dot_nan(g, 420, 180)                  # 中点
    _dot_nan(g, 640, 210, 84, 100)         # 右点


def _roof(g: Glyph, x1: float, x2: float, dot_cx: float) -> None:
    """宀 —— 宜・狩 共用同一坐标（点居中偏右，冖左端垂短竖）。"""
    _dot_v(g, dot_cx, 760, W_DOT, 100)
    g.hbar(x1, x2, 630, W_SEC)
    g.vbar(x1 + 48, 676, 540, W_THIN)


def _eight(g: Glyph, left_x: float, right_x: float, y_top: float, y_bot: float) -> None:
    """八 —— 呉・共・貝 共用同一写法（左撇 + 右捺，均为斜笔画）。"""
    g.diag(left_x, y_top, left_x - 200, y_bot, W_SEC)
    g.diag(right_x - 200, y_top, right_x, y_bot, W_SEC)


# ---------------------------------------------------------------- 字形 ------------------------------------------------------------
def g_kun() -> Glyph:
    """昆：上 日，下 比（两 匕）。"""
    g = Glyph("uni6606", advance=1000, unicode=0x6606, note="昆：日 + 比")
    # 日（x 130..870，ink y 406..820；内白 69／69）
    g.hbar(130, 870, 774, W_SEC)
    g.hbar(178, 822, 613, W_SEC)
    g.hbar(130, 870, 452, W_SEC)
    g.vbar(178, YT, 452, W_SEC)
    g.vbar(822, YT, 452, W_SEC)
    # 比：左 匕
    g.vbar(190, 360, 56, W_MAIN)
    g.hbar(190, 470, 104, W_MAIN)
    g.diag(440, 330, 90, 210, W_SEC)
    # 比：右 匕
    g.vbar(650, 360, 56, W_MAIN)
    g.hbar(650, XR, 104, W_MAIN)
    g.diag(900, 330, 550, 210, W_SEC)
    return g


def g_teii() -> Glyph:
    """訂：左 言，右 丁。"""
    g = Glyph("uni8A02", advance=1000, unicode=0x8A02, note="訂：言 + 丁")
    # 言（x 60..410）：丶 + 一 + 一 + 一 + 口（内白 90）
    _dot_v(g, 235, 758, W_DOT, 110)
    g.hbar(XL, 410, 630, W_SEC)
    g.hbar(XL, 410, 500, W_SEC)
    g.hbar(XL, 410, 370, W_SEC)
    _box(g, XL, 410, 264, YB, W_SEC)
    # 丁（x 470..940）：一 + 亅（带左挑）
    g.hbar(470, XR, 700, W_MAIN)
    g.vbar(700, 748, 150, W_MAIN)
    g.hbar(560, 700, 126, W_THIN)
    return g


def g_me() -> Glyph:
    """芽：上 艹，下 牙。"""
    g = Glyph("uni82BD", advance=1000, unicode=0x82BD, note="芽：艹 + 牙")
    _grass(g)
    # 牙（x 190..880）：一 + 丨 + 一 + 撇 + 竖钩
    g.hbar(220, 880, 520, W_MAIN)
    g.vbar(280, 520, 90, W_SEC)
    g.hbar(280, 800, 330, W_SEC)
    g.hbar(200, 280, 122, W_THIN)
    g.diag(770, 340, 220, 90, W_SEC)
    return g


def g_nin() -> Glyph:
    """忍：上 刃，下 心。"""
    g = Glyph("uni5FCD", advance=1000, unicode=0x5FCD, note="忍：刃 + 心")
    # 刃（x 288..760）
    g.hbar(300, 760, 716, W_MAIN)
    g.vbar(712, 716, 400, W_MAIN)
    g.diag(460, 700, 320, 380, W_SEC)
    _dot_nan(g, 590, 540, W_DOT, 110)
    _heart(g)
    return g


def g_tai() -> Glyph:
    """怠：上 台（厶 + 口），下 心。"""
    g = Glyph("uni6020", advance=1000, unicode=0x6020, note="怠：台 + 心")
    # 厶
    g.diag(600, 780, 430, 640, W_THIN)
    g.hbar(430, 660, 640, W_THIN)
    _dot_nan(g, 690, 765, W_DOT, 100)
    # 口
    _box(g, 340, 760, 570, 290, W_MAIN)
    _heart(g)
    return g


def g_jo() -> Glyph:
    """如：左 女，右 口。"""
    g = Glyph("uni5982", advance=1000, unicode=0x5982, note="如：女 + 口")
    # 女（x 60..470）：横 + 撇 + 捺
    g.hbar(XL, 470, 560, W_SEC)
    g.diag(400, 795, 110, 175, W_SEC)
    g.diag(170, 790, 400, 90, W_SEC)
    # 口（x 530..940）
    _box(g, 530, XR, 700, 260, W_MAIN)
    return g


def g_futsu() -> Glyph:
    """沸：左 氵，右 弗。"""
    g = Glyph("uni6CB8", advance=1000, unicode=0x6CB8, note="沸：氵 + 弗")
    _water(g)
    # 弗（x 330..940）：横 + 竖折 + 横 + 2 竖 + 横 + 撇
    g.hbar(380, 880, 760, W_MAIN)
    g.vbar(832, 760, 540, W_MAIN)
    g.hbar(380, 880, 600, W_SEC)
    g.vbar(430, 800, 120, W_MAIN)
    g.vbar(670, 800, 120, W_MAIN)
    g.hbar(330, 880, 380, W_SEC)
    g.diag(600, 380, 360, 60, W_SEC)
    return g


def g_nao() -> Glyph:
    """苗：上 艹，下 田。"""
    g = Glyph("uni82D7", advance=1000, unicode=0x82D7, note="苗：艹 + 田")
    _grass(g)
    # 田（x 280..720）
    _box(g, 280, 720, 560, 60, W_MAIN)
    g.vbar(500, 560, 60, W_THIN)
    g.hbar(280, 720, 330, W_THIN)
    return g


def g_ai() -> Glyph:
    """哀：亠 + 口 + 衣底（一 + 竖 + 撇 + 捺）。"""
    g = Glyph("uni54C0", advance=1000, unicode=0x54C0, note="哀：亠 + 口 + 衣")
    _dot_v(g, 500, 760, W_DOT, 100)
    g.hbar(XL, XR, 630, W_SEC)
    _box(g, 330, 670, 564, 280, W_SEC)
    g.hbar(160, 840, 200, W_SEC)
    g.vbar(500, 246, 60, W_THIN)
    g.diag(420, 190, 150, 60, W_SEC)
    g.diag(580, 190, 850, 60, W_SEC)
    return g


def g_hai() -> Glyph:
    """灰：厂（横 + 撇）内 火。"""
    g = Glyph("uni7070", advance=1000, unicode=0x7070, note="灰：厂 + 火")
    g.hbar(XL, XR, 740, W_MAIN)
    g.diag(235, 750, 115, 50, W_SEC)
    # 火
    _dot_nan(g, 370, 640)
    _dot_hyaku(g, 840, 640, W_DOT, 100)
    g.diag(600, 660, 330, 60, W_SEC)
    g.diag(600, 600, 900, 60, W_SEC)
    return g


def g_shou() -> Glyph:
    """匠：匚 内 斤。"""
    g = Glyph("uni5320", advance=1000, unicode=0x5320, note="匠：匚 + 斤")
    g.hbar(XL, XR, 740, W_MAIN)
    g.vbar(108, 788, 60, W_MAIN)
    g.hbar(XL, XR, 108, W_MAIN)
    # 斤：长横撇 + 撇 + 一 + 丨
    g.diag(880, 620, 280, 500, W_SEC)
    g.diag(430, 520, 300, 300, W_SEC)
    g.hbar(520, 860, 330, W_SEC)
    g.vbar(790, 376, 90, W_MAIN)
    return g


def g_sui() -> Glyph:
    """垂：上短撇 + 4 横 + 2 竖。"""
    g = Glyph("uni5782", advance=1000, unicode=0x5782, note="垂：丿 + 横 + 竖")
    g.diag(700, 770, 300, 680, W_SEC)
    g.hbar(140, 880, 547, W_MAIN)
    g.vbar(330, 547, 250, W_THIN)
    g.vbar(580, 547, 250, W_THIN)
    g.hbar(200, 850, 399, W_SEC)
    g.hbar(200, 870, 253, W_SEC)
    g.hbar(80, XR, 109, W_MAIN)
    return g


def g_go() -> Glyph:
    """呉：丨 + 口 + フ + 一 + 八（7 画，上中下结构）。"""
    g = Glyph("uni5449", advance=1000, unicode=0x5449, note="呉：口 + 一 + 八")
    g.vbar(140, YT, 560, W_MAIN)           # ① 丨
    _box(g, 300, 700, YT, 600, W_THIN)     # ②③ 口
    g.hbar(92, 820, 520, W_SEC)            # ④ フ 的横
    g.vbar(772, 520, 470, W_SEC)           # ④ フ 的折
    g.hbar(XL, XR, 390, W_MAIN)            # ⑤ 一
    _eight(g, 340, 890, 290, 50)
    return g


def g_haku() -> Glyph:
    """伯：左 亻，右 白（丿 + 日）。"""
    g = Glyph("uni4F2F", advance=1000, unicode=0x4F2F, note="伯：亻 + 白")
    _person(g)
    # 白
    g.diag(590, 780, 490, 680, W_SEC)
    g.hbar(500, 900, 700, W_MAIN)
    g.vbar(548, 700, 296, W_MAIN)
    g.vbar(852, 700, 296, W_MAIN)
    g.hbar(500, 900, 248, W_MAIN)
    g.hbar(548, 852, 450, W_SEC)
    return g


def g_shi() -> Glyph:
    """柿：左 木，右 市（亠 + 巾）。"""
    g = Glyph("uni67FF", advance=1000, unicode=0x67FF, note="柿：木 + 市")
    _tree(g)
    _dot_v(g, 715, 760, W_DOT, 100)
    g.hbar(490, XR, 630, W_SEC)
    # 巾
    g.hbar(570, 870, 486, W_SEC)
    g.vbar(616, 532, 212, W_SEC)
    g.vbar(824, 532, 212, W_SEC)
    g.hbar(570, 870, 166, W_SEC)
    g.vbar(720, 532, 60, W_SEC)
    return g


def g_ko() -> Glyph:
    """枯：左 木，右 古（十 + 口）。"""
    g = Glyph("uni67AF", advance=1000, unicode=0x67AF, note="枯：木 + 古")
    _tree(g)
    g.hbar(490, XR, 700, W_SEC)
    g.vbar(715, YT, 560, W_SEC)
    _box(g, 540, 890, 480, 100, W_MAIN)
    return g


def g_hime() -> Glyph:
    """妃：左 女，右 己。"""
    g = Glyph("uni5983", advance=1000, unicode=0x5983, note="妃：女 + 己")
    g.hbar(XL, 470, 560, W_SEC)
    g.diag(400, 795, 110, 175, W_SEC)
    g.diag(170, 790, 400, 90, W_SEC)
    # 己
    g.hbar(540, XR, 700, W_SEC)
    g.vbar(888, 700, 500, W_SEC)
    g.hbar(540, 934, 500, W_SEC)
    g.vbar(588, 546, 140, W_SEC)
    g.hbar(542, XR, 140, W_SEC)
    return g


def g_shuu() -> Glyph:
    """臭：上 自（丿 + 目），下 犬。"""
    g = Glyph("uni81ED", advance=1000, unicode=0x81ED, note="臭：自 + 犬")
    # 自
    g.diag(300, 790, 240, 700, W_THIN)
    g.hbar(250, 790, 778, W_THIN)
    g.vbar(292, YT, 424, W_THIN)
    g.vbar(748, YT, 424, W_THIN)
    g.hbar(292, 748, 640, W_THIN)
    g.hbar(292, 748, 502, W_THIN)
    g.hbar(250, 790, 382, W_THIN)
    # 犬
    g.hbar(180, 820, 250, W_SEC)
    g.diag(520, 300, 150, 40, W_SEC)
    g.diag(520, 290, 850, 40, W_SEC)
    _dot_nan(g, 810, 250, W_DOT, 100)
    return g


def g_i() -> Glyph:
    """宜：宀 + 且。"""
    g = Glyph("uni5B9C", advance=1000, unicode=0x5B9C, note="宜：宀 + 且")
    _roof(g, XL, XR, 500)
    # 且
    g.hbar(250, 750, 476, W_SEC)
    g.vbar(296, 476, 152, W_SEC)
    g.vbar(704, 476, 152, W_SEC)
    g.hbar(296, 704, 346, W_THIN)
    g.hbar(296, 704, 226, W_THIN)
    g.hbar(250, 750, 106, W_SEC)
    return g


def g_mou() -> Glyph:
    """盲：亡（丶 + 一 + 乚）+ 目。"""
    g = Glyph("uni76F2", advance=1000, unicode=0x76F2, note="盲：亡 + 目")
    _dot_v(g, 500, 770, W_DOT, 100)
    g.hbar(XL, XR, 640, W_SEC)
    g.vbar(140, 594, 500, W_THIN)
    g.hbar(140, 400, 542, W_THIN)
    # 目
    g.hbar(250, 790, 414, W_SEC)
    g.vbar(296, 460, 96, W_SEC)
    g.vbar(744, 460, 96, W_SEC)
    g.hbar(296, 744, 290, W_THIN)
    g.hbar(296, 744, 170, W_THIN)
    g.hbar(250, 790, 50, W_SEC)
    return g


def g_gen() -> Glyph:
    """弦：左 弓，右 玄（亠 + 幺）。"""
    g = Glyph("uni5F26", advance=1000, unicode=0x5F26, note="弦：弓 + 玄")
    # 弓
    g.hbar(XL, 390, 740, W_SEC)
    g.vbar(342, 740, 560, W_SEC)
    g.hbar(XL, 342, 560, W_SEC)
    g.vbar(108, 560, 340, W_SEC)
    g.hbar(108, 390, 340, W_SEC)
    # 玄
    _dot_v(g, 695, 760, W_DOT, 100)
    g.hbar(450, XR, 630, W_SEC)
    g.diag(700, 510, 520, 340, W_SEC)
    g.hbar(520, 780, 340, W_SEC)
    g.diag(760, 320, 570, 140, W_SEC)
    g.hbar(570, 860, 140, W_SEC)
    _dot_nan(g, 890, 400, W_DOT, 100)
    return g


def g_sui_fire() -> Glyph:
    """炊：左 火，右 欠（𠂉 + 人）。"""
    g = Glyph("uni708A", advance=1000, unicode=0x708A, note="炊：火 + 欠")
    # 火
    _dot_nan(g, 150, 560)
    _dot_hyaku(g, 380, 570, W_DOT, 100)
    g.diag(310, 640, 120, 60, W_SEC)
    g.diag(260, 600, 380, 140, W_SEC)
    # 欠
    g.diag(650, 780, 500, 630, W_SEC)
    g.hbar(600, XR, 660, W_SEC)
    g.diag(700, 600, 500, 60, W_SEC)
    g.diag(670, 560, 880, 90, W_SEC)
    return g


def g_kou() -> Glyph:
    """洪：左 氵，右 共（廿 + 八）。"""
    g = Glyph("uni6D2A", advance=1000, unicode=0x6D2A, note="洪：氵 + 共")
    _water(g)
    g.vbar(490, YT, 600, W_THIN)
    g.vbar(790, YT, 600, W_THIN)
    g.hbar(340, XR, 740, W_SEC)
    g.hbar(340, XR, 600, W_SEC)
    _eight(g, 560, 880, 470, 60)
    return g


def g_shou_gyo() -> Glyph:
    """狩：左 犭，右 守（宀 + 寸）。"""
    g = Glyph("uni72E9", advance=1000, unicode=0x72E9, note="狩：犭 + 守")
    # 犭
    g.diag(260, 780, 110, 640, W_SEC)
    g.vbar(160, 700, 140, W_SEC)
    g.hbar(110, 160, 182, W_THIN)
    g.diag(300, 520, 120, 300, W_SEC)
    # 守
    _dot_v(g, 650, 770, W_DOT, 100)
    g.hbar(360, XR, 640, W_SEC)
    g.vbar(408, 686, 560, W_THIN)
    g.hbar(420, XR, 520, W_SEC)
    g.vbar(760, 560, 60, W_SEC)
    g.hbar(680, 760, 102, W_THIN)
    _dot_nan(g, 560, 420, W_DOT, 100)
    return g


def g_fune() -> Glyph:
    """舟：丿 + 一 + 丿 + 𠃍 + 两点。"""
    g = Glyph("uni821F", advance=1000, unicode=0x821F, note="舟：丿 + 舟身")
    g.diag(320, 780, 170, 660, W_SEC)       # ① 丿
    g.hbar(300, 880, 700, W_SEC)            # ② 一（舟的上横）
    g.vbar(834, 700, 130, W_SEC)            # ③ 舟的右侧竖
    g.diag(300, 640, 110, 110, W_SEC)       # ④ 丿（舟的左侧斜）
    g.hbar(XL, 780, 450, W_SEC)             # ⑤ 一（中间横，左出锋）
    _dot_nan(g, 600, 590, W_DOT, 100)       # ⑥ 上点
    _dot_nan(g, 620, 380, W_DOT, 100)       # ⑦ 下点
    return g


def g_kai() -> Glyph:
    """貝：目 + 八。"""
    g = Glyph("uni8C9D", advance=1000, unicode=0x8C9D, note="貝：目 + 八")
    g.hbar(250, 790, 774, W_SEC)
    g.vbar(296, YT, 388, W_SEC)
    g.vbar(744, YT, 388, W_SEC)
    g.hbar(296, 744, 630, W_THIN)
    g.hbar(296, 744, 486, W_THIN)
    g.hbar(250, 790, 342, W_SEC)
    _eight(g, 500, 880, 280, 40)
    return g


def g_shu() -> Glyph:
    """朱：丿 + 未（二 + 竖 + 撇 + 捺）。"""
    g = Glyph("uni6731", advance=1000, unicode=0x6731, note="朱：丿 + 木")
    g.diag(300, 790, 190, 660, W_SEC)
    g.hbar(280, 780, 640, W_SEC)
    g.hbar(XL, XR, 500, W_SEC)
    g.vbar(500, YT, 60, W_MAIN)
    g.diag(490, 540, 110, 60, W_SEC)
    g.diag(510, 540, 880, 60, W_SEC)
    return g


def g_su() -> Glyph:
    """枢：左 木，右 区（匚 + 乂）。"""
    g = Glyph("uni67A2", advance=1000, unicode=0x67A2, note="枢：木 + 区")
    _tree(g)
    g.hbar(490, XR, 740, W_SEC)
    g.vbar(538, 740, 100, W_SEC)
    g.hbar(490, XR, 146, W_SEC)
    g.diag(820, 620, 600, 280, W_SEC)
    g.diag(600, 620, 830, 280, W_SEC)
    return g


def g_kou_ka() -> Glyph:
    """肯：止 + 月。

    2026-10-31 回修：止的横（422..518）与月上横（334..426）白口 −4 → 月部下移 40，白口 36。
    """
    g = Glyph("uni80AF", advance=1000, unicode=0x80AF, note="肯：止 + 月")
    # 止
    g.vbar(500, YT, 420, W_MAIN)
    g.hbar(548, 800, 690, W_SEC)
    g.vbar(280, 700, 470, W_THIN)
    g.hbar(XL, XR, 470, W_MAIN)
    # 月
    g.diag(310, 340, 230, 60, W_SEC)
    g.hbar(250, 790, 340, W_SEC)
    g.vbar(744, 340, 80, W_SEC)
    g.hbar(300, 744, 210, W_THIN)
    g.hbar(300, 744, 80, W_THIN)
    return g


def g_batsu() -> Glyph:
    """伐：左 亻，右 戈（一 + 斜钩 + 撇 + 点）。"""
    g = Glyph("uni4F10", advance=1000, unicode=0x4F10, note="伐：亻 + 戈")
    _person(g)
    g.hbar(470, XR, 700, W_SEC)
    g.diag(770, 800, 590, 140, W_MAIN)
    g.hbar(520, 600, 175, W_THIN)
    g.diag(700, 600, 500, 300, W_SEC)
    _dot_nan(g, 880, 760, W_DOT, 100)
    return g


def g_kyu() -> Glyph:
    """糾：左 糹，右 丩。"""
    g = Glyph("uni7CFE", advance=1000, unicode=0x7CFE, note="糾：糹 + 丩")
    # 糹
    g.diag(300, 780, 150, 590, W_THIN)
    g.hbar(150, 350, 600, W_THIN)
    g.diag(350, 620, 200, 440, W_THIN)
    g.hbar(200, 400, 440, W_THIN)
    g.vbar(275, 440, 80, W_THIN)
    _dot_hyaku(g, 140, 320, W_DOT, 100)
    _dot_nan(g, 400, 320, W_DOT, 100)
    # 丩
    g.vbar(600, 520, 200, W_SEC)
    g.vbar(800, 700, 120, W_SEC)
    g.hbar(700, 800, 162, W_THIN)
    return g


def g_heijo() -> Glyph:
    """坪：左 土，右 平（一 + 丷 + 十）。"""
    g = Glyph("uni576A", advance=1000, unicode=0x576A, note="坪：土 + 平")
    # 土
    g.hbar(110, 370, 560, W_SEC)
    g.vbar(240, 700, 60, W_SEC)
    g.hbar(XL, 420, 106, W_SEC)
    # 平
    g.hbar(470, XR, 740, W_SEC)
    _dot_nan(g, 600, 600, W_DOT, 100)
    _dot_hyaku(g, 820, 600, W_DOT, 100)
    g.hbar(470, XR, 470, W_SEC)
    g.vbar(705, 786, 60, W_SEC)
    return g


def build() -> list[Glyph]:
    return [
        g_kun(), g_teii(), g_me(), g_nin(), g_tai(), g_jo(), g_futsu(), g_nao(),
        g_ai(), g_hai(), g_shou(), g_sui(), g_go(), g_haku(), g_shi(), g_ko(),
        g_hime(), g_shuu(), g_i(), g_mou(), g_gen(), g_sui_fire(), g_kou(),
        g_shou_gyo(), g_fune(), g_kai(), g_shu(), g_su(), g_kou_ka(),
        g_batsu(), g_kyu(), g_heijo(),
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-018.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
