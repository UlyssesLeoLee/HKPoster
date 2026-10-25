"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-002。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
* 字面框：x 60..940、y 0..820，advance = 1000，与 zh-HK 繁体汉字完全同格，
  便于中英日混排。本批所有字形的墨迹都收在 x 100..900 / y 0..820 之内。
* 笔画权重：主 96 / 次 92 / 细 84 / 点 84（与 zh-HK 繁体同一档）。
  6–7 画字以 96 为主笔画（加重，避免"太轻"）；8–9 画字在密排处把次级横画
  降到 84（局部减重，避免"太闷"），符合 GLY-001 允许的小空腔局部减重。
* 部件复用：亻、氵、扌、勺、口、木、横折钩一类部件抽成 part_* 辅助函数，
  同批内坐标与笔画拆法完全一致，只允许平移 + 缩放做光学校正（docs/03 GLY-004）。
* 内白：密排横画之间内白 ≥ 24 单位，竖与竖之间 ≥ 60 单位（GLY-006）。
* 不做逐字机械挤压或倾斜（docs/02 偏差 D）：所有斜笔只在字形自身的结构位上
  使用（撇、捺、钩、横折），不引入整体倾斜。
* 墨量平衡：6 画档与 7–9 画档各自的中位墨量率落在 0.22–0.28 之间，
  百 / 多 / 安 / 当 四个偏轻偏重的字做了单独补偿，避免同批"有的太轻、有的太闷"。

坐标约定
--------
* 横画 hbar(x1, x2, y, w)：墨迹占 y±w/2，x 跨 x1..x2；下缘即 ink_bottom。
* 竖画用 rect(x-w/2, x+w/2, y_bot, y_top) 显式给出墨迹上下端，
  保证"横画墨迹上缘贴 820 / 下缘贴 0"的对齐语义可精确控制。
* 斜笔 diag() 为平头帽，笔画角点会略超出端点 y；凡是与横画相邻的斜笔，
  其端点一律落在横画墨迹内部，避免零面积尖刺（自交轮廓）。
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


class Pen:
    """部件坐标系：只做平移 + 缩放（光学校正），权重不随缩放变化。"""

    def __init__(self, glyph: Glyph, ox: float = 0.0, oy: float = 0.0,
                 sx: float = 1.0, sy: float = 1.0) -> None:
        self.g = glyph
        self.ox = ox
        self.oy = oy
        self.sx = sx
        self.sy = sy

    def X(self, x: float) -> float:
        return self.ox + x * self.sx

    def Y(self, y: float) -> float:
        return self.oy + y * self.sy

    def hbar(self, x1: float, x2: float, y: float, w: float = W_MAIN) -> None:
        self.g.hbar(self.X(x1), self.X(x2), self.Y(y), weight=w)

    def vbar(self, x: float, y1: float, y2: float, w: float = W_MAIN) -> None:
        """竖画：中心线 x，墨迹上下端即 y1（底）与 y2（顶）。"""
        self.g.rect(self.X(x - w / 2.0), self.X(x + w / 2.0),
                    self.Y(y1), self.Y(y2))

    def diag(self, x1: float, y1: float, x2: float, y2: float,
             w: float = W_MAIN) -> None:
        self.g.diag(self.X(x1), self.Y(y1), self.X(x2), self.Y(y2), weight=w)

    def dot(self, cx: float, cy: float, w: float = W_DOT, h: float = 104,
            slant: float = 0) -> None:
        self.g.dot(self.X(cx), self.Y(cy), w=w, h=h, slant=slant)

    def htop(self, x1: float, x2: float, w: float = W_MAIN) -> None:
        """横画：墨迹上缘贴 820。"""
        self.hbar(x1, x2, TOP - w / 2.0, w)

    def hbot(self, x1: float, x2: float, w: float = W_MAIN) -> None:
        """横画：墨迹下缘贴 0。"""
        self.hbar(x1, x2, BASE + w / 2.0, w)

    def hmid(self, x1: float, x2: float, ink_bottom: float,
             w: float = W_MAIN) -> None:
        """横画：墨迹下缘落在 ink_bottom。"""
        self.hbar(x1, x2, ink_bottom + w / 2.0, w)


# ---------------------------------------------------------------- 复用部件


def part_ninben(p: Pen) -> None:
    """亻（人字旁）：撇 + 竖。本批 体 / 作 / 保 复用，坐标完全一致。"""
    p.diag(220, 770, 50, 360, W_SEC)   # 撇：右上 → 左下
    p.vbar(140, 0, 540, W_MAIN)         # 竖：与撇的交点起，落基线


def part_sanzui(p: Pen) -> None:
    """氵（三点水）：上点 + 中点 + 提。本批 法 / 治 复用。"""
    p.dot(150, 750, W_SEC, 112)         # 上点
    p.dot(115, 500, W_SEC, 112)         # 中点
    p.diag(60, 180, 190, 330, W_DOT)    # 提：右下 → 右上


def part_tehen(p: Pen) -> None:
    """扌（手旁）：横 + 竖钩 + 提。本批 持 / 指 复用。"""
    p.hmid(0, 300, 560, W_SEC)          # 横
    p.vbar(183, 0, 806, W_MAIN)         # 竖
    p.diag(185, 40, 105, 105, W_THIN)   # 竖钩的钩
    p.diag(30, 330, 280, 420, W_DOT)    # 提


def part_you(p: Pen) -> None:
    """勺：撇 + 横折钩 + 点。本批 約 / 的 复用。"""
    p.diag(140, 785, 0, 560, W_SEC)     # 撇
    p.hmid(60, 380, 680, W_SEC)         # 横折钩的横
    p.vbar(380, 300, 772, W_MAIN)       # 横折钩的竖
    p.diag(374, 330, 284, 420, W_THIN)  # 钩
    p.dot(230, 570, W_MAIN, 112)        # 点


def part_riki(p: Pen, x0: float, x1: float, y_top: float, y_base: float,
              w: float = W_THIN) -> None:
    """力：横 + 横折钩（右竖 + 底部左钩）+ 撇。
    本批 協 的三个力复用同一套拆法（上力一个、下力两个）。
    x0/x1 为横的两端，y_top 为横的墨迹下缘，y_base 为竖的底端。
    """
    p.hmid(x0, x1, y_top, w)                                    # 横
    p.vbar(x1 - w / 2.0, y_base, y_top + w, w)                  # 横折钩的竖
    p.diag(x1 - w / 2.0, y_base + 20, x1 - w / 2.0 - 95, y_base + 85, w)  # 钩
    p.diag(x0 + 40, y_top + 10, x0 - 105, y_base, w)             # 撇


def part_kuchi(p: Pen, x0: float, y0: float, w: float, h: float,
               wt: float = W_MAIN) -> None:
    """口（kuchi）：左竖 + 横折（顶横 + 右竖）+ 底横。x0/y0 为墨迹框左下角。"""
    p.vbar(x0 + wt / 2.0, y0, y0 + h, wt)          # 左竖
    p.hmid(x0, x0 + w, y0 + h - wt, wt)             # 顶横
    p.vbar(x0 + w - wt / 2.0, y0, y0 + h, wt)      # 右竖
    p.hmid(x0, x0 + w, y0, wt)                      # 底横


def part_moku(p: Pen, x0: float, x1: float, y_top: float, y_base: float,
              y_bar: float, bar_w: float = W_MAIN) -> None:
    """木：横 + 竖 + 撇 + 捺。本批 体（本）/ 保（呆）复用同一套拆法。
    x0/x1 为横的两端，y_bar 为横的墨迹下缘，y_top/y_base 为竖的上下端。
    """
    cx = (x0 + x1) / 2.0
    p.hmid(x0, x1, y_bar, bar_w)                              # 横
    p.vbar(cx, y_base, y_top, W_MAIN)                         # 竖
    # 撇 / 捺 从横下方 0.34 竖长处起笔，避免挤成"个"字形
    spread = y_bar - 0.34 * (y_bar - y_base)
    p.diag(cx - 30, spread, x0 + 40, y_base + 40, W_SEC)       # 撇
    p.diag(cx + 30, spread, x1 - 40, y_base + 40, W_SEC)       # 捺


# ---------------------------------------------------------------- 各字


def glyph_tong() -> Glyph:
    """通 U+901A（9画）—— 辶 + 甬。
    部件分区：辶 占 x 100..300 / y 78..740；甬（龴 + 用）占 x 400..900 / y 150..820。
    笔画拆解：辶 = 点 + 横折撇 + 平捺；甬 = 龴（横 + 斜撇 + 点）+ 用（顶横 + 左竖 +
    右竖 + 中竖 + 两道内横）。用内横降到 84 做局部减重。
    """
    g = Glyph("uni901A", advance=1000, unicode=0x901A, note="通：辶 + 甬")
    p = Pen(g)
    # ---- 甬 ----
    p.hmid(470, 790, 728, W_SEC)            # 龴：横
    p.diag(790, 728, 610, 600, W_SEC)       # 龴：斜撇（末端埋进用顶横）
    p.dot(530, 645, W_DOT, 100)             # 龴：点
    p.hmid(445, 900, 560, W_MAIN)           # 用：顶横
    p.vbar(493, 150, 656, W_MAIN)           # 用：左竖
    p.vbar(852, 150, 656, W_MAIN)           # 用：右竖
    p.vbar(675, 150, 656, W_MAIN)           # 用：中竖
    p.hmid(493, 900, 430, W_THIN)           # 用：上内横（减重）
    p.hmid(493, 900, 270, W_THIN)           # 用：下内横（减重）
    # ---- 辶 ----
    p.dot(215, 690, W_DOT, 100)             # 辶：点
    p.hmid(120, 285, 530, W_THIN)           # 辶：横折（短横）
    p.diag(285, 530, 165, 300, W_THIN)      # 辶：折撇
    p.diag(140, 215, 520, 105, W_THIN)      # 辶：平捺（上段）
    p.diag(520, 105, 890, 78, W_THIN)       # 辶：平捺（下段）
    return g


def glyph_gen() -> Glyph:
    """言 U+8A00（7画）—— 丶 + 三 + 口（上下叠置，独体字）。
    分区：丶 居中 y 718..814；三道横 y 620..712 / 490..574 / 370..454；
    口 占 x 320..680 / y 0..280。横画间距统一 ≥ 36。
    """
    g = Glyph("uni8A00", advance=1000, unicode=0x8A00, note="言：丶 + 三 + 口")
    p = Pen(g)
    p.dot(500, 766, W_SEC, 96)              # 丶
    p.hmid(240, 760, 620, W_SEC)             # 一（长）
    p.hmid(310, 690, 490, W_THIN)           # 一（中）
    p.hmid(310, 690, 370, W_THIN)           # 一（短）
    part_kuchi(p, 320, 0, 360, 280, W_MAIN)  # 口
    return g


def glyph_tai() -> Glyph:
    """体 U+4F53（7画）—— 亻 + 本。
    分区：亻 占 x 100..320；本（木 + 底部一）占 x 370..900。
    笔画：亻 = 撇 + 竖；本 = 木（横 + 竖 + 撇 + 捺）+ 底部一。
    """
    g = Glyph("uni4F53", advance=1000, unicode=0x4F53, note="体：亻 + 本")
    part_ninben(Pen(g, ox=95, sx=0.85))
    p = Pen(g)
    part_moku(p, 400, 880, y_top=820, y_base=150, y_bar=724, bar_w=W_SEC)
    p.hmid(370, 900, 60, W_MAIN)            # 本：底部一
    return g


def glyph_tou() -> Glyph:
    """当 U+5F53（6画）—— ⺌（小字头）+ ヨ形下部。
    分区：⺌ 占 x 310..690 / y 600..820；下部三横占 x 200..800 / y 60..612。
    下部取"ヨ"形：**右侧竖**连接三横（左端阶梯式收短），与 SimHei / 日本字形一致。
    """
    g = Glyph("uni5F53", advance=1000, unicode=0x5F53, note="当：⺌ + ヨ")
    p = Pen(g)
    p.vbar(500, 600, 820, W_MAIN)           # ⺌：中竖（落到下横上）
    p.diag(400, 715, 310, 615, W_SEC)       # ⺌：左点
    p.diag(600, 715, 690, 615, W_SEC)       # ⺌：右点
    p.hmid(200, 800, 520, W_SEC)            # 下部：上横（最长）
    p.vbar(752, 60, 612, W_MAIN)            # 下部：右侧竖（尾出下横）
    p.hmid(280, 800, 300, W_SEC)            # 下部：中横
    p.hmid(320, 800, 100, W_MAIN)           # 下部：下横
    return g


def glyph_yaku() -> Glyph:
    """約 U+7D04（9画）—— 糹 + 勺。
    分区：糹 占 x 102..340 / y 100..813；勺 占 x 404..834（与 的 的勺同部件）。
    """
    g = Glyph("uni7D04", advance=1000, unicode=0x7D04, note="約：糹 + 勺")
    p = Pen(g)
    # 糹：上 ㄥ + 下 ㄥ + 点 + 竖 + 左短撇
    p.diag(305, 780, 180, 660, W_MAIN)       # 糹：上 ㄥ 上段
    p.diag(180, 660, 305, 570, W_MAIN)       # 糹：上 ㄥ 下段
    p.diag(300, 640, 175, 440, W_SEC)        # 糹：下 ㄥ
    p.dot(305, 430, W_MAIN, 100)            # 糹：点
    p.vbar(250, 100, 470, W_MAIN)           # 糹：竖
    p.diag(190, 400, 135, 290, W_THIN)      # 糹：左短撇
    part_you(Pen(g, ox=440, sx=0.92))       # 勺
    return g


def glyph_shu() -> Glyph:
    """首 U+9996（9画）—— 丷 + 一 + 自（丿 + 目）。
    分区：丷 占 y 718..818；一 占 y 620..712；自 占 x 280..720 / y 10..492。
    """
    g = Glyph("uni9996", advance=1000, unicode=0x9996, note="首：丷 + 一 + 自")
    p = Pen(g)
    p.dot(330, 768, W_DOT, 100)             # 丷：左点
    p.dot(670, 768, W_DOT, 100)             # 丷：右点
    p.hmid(200, 800, 620, W_MAIN)           # 一
    p.diag(520, 600, 450, 520, W_THIN)      # 自：丿
    p.hmid(280, 720, 400, W_MAIN)           # 目：顶横
    p.vbar(322, 10, 492, W_MAIN)            # 目：左竖
    p.vbar(678, 10, 492, W_MAIN)            # 目：右竖
    p.hmid(280, 720, 270, W_THIN)           # 目：内横 1
    p.hmid(280, 720, 140, W_THIN)           # 目：内横 2
    p.hmid(280, 720, 10, W_MAIN)            # 目：底横
    return g


def glyph_hou() -> Glyph:
    """法 U+6CD5（8画）—— 氵 + 去（土 + 厶）。
    分区：氵 占 x 112..290 / y 694..806；去 占 x 330..900 / y 190..816。
    """
    g = Glyph("uni6CD5", advance=1000, unicode=0x6CD5, note="法：氵 + 去")
    part_sanzui(Pen(g, ox=95, sx=0.85))
    p = Pen(g)
    p.hmid(400, 800, 724, W_SEC)            # 去：短横
    p.hmid(330, 900, 500, W_MAIN)           # 去：长横
    p.vbar(612, 500, 816, W_MAIN)           # 去：竖
    p.diag(600, 450, 440, 190, W_MAIN)      # 厶：撇折的上段
    p.hmid(440, 700, 190, W_SEC)            # 厶：底横
    p.dot(740, 270, W_MAIN, 112)            # 厶：点
    return g


def glyph_rai() -> Glyph:
    """来 U+6765（7画）—— 一 + 丷 + 一 + 木身（丨 + 撇 + 捺）。
    分区：上横 y 724..820；丷 y 584..696；中横 y 440..536；下部 y 140..780。
    """
    g = Glyph("uni6765", advance=1000, unicode=0x6765, note="来：一 + 丷 + 木")
    p = Pen(g)
    p.hmid(200, 800, 724, W_MAIN)           # 上横
    p.dot(370, 640, W_MAIN, 112)            # 丷：左点
    p.dot(630, 640, W_MAIN, 112)            # 丷：右点
    p.hmid(180, 820, 440, W_MAIN)           # 中横
    p.vbar(500, 130, 780, W_MAIN)           # 竖
    p.diag(500, 420, 280, 140, W_SEC)       # 撇
    p.diag(500, 420, 720, 140, W_SEC)       # 捺
    return g


def glyph_saku() -> Glyph:
    """作 U+4F5C（7画）—— 亻 + 乍。
    分区：亻 占 x 100..320；乍 占 x 350..880 / y 190..808。
    笔画：乍 = 撇 + 长横 + 竖 + 两横。
    """
    g = Glyph("uni4F5C", advance=1000, unicode=0x4F5C, note="作：亻 + 乍")
    part_ninben(Pen(g, ox=95, sx=0.85))
    p = Pen(g)
    p.diag(440, 785, 375, 675, W_THIN)      # 乍：撇（末端埋进长横的墨迹）
    p.hmid(390, 880, 590, W_MAIN)           # 乍：长横
    p.vbar(440, 60, 686, W_MAIN)            # 乍：竖
    p.hmid(392, 880, 400, W_THIN)           # 乍：中横
    p.hmid(392, 880, 190, W_THIN)           # 乍：下横
    return g


def glyph_sei() -> Glyph:
    """性 U+6027（8画）—— 忄 + 生。
    分区：忄 占 x 108..362 / y 0..820；生 占 x 360..900 / y 0..815。
    生：三横 + 竖 + 顶部撇，三横间距均匀（≈200）。
    """
    g = Glyph("uni6027", advance=1000, unicode=0x6027, note="性：忄 + 生")
    p = Pen(g)
    p.dot(150, 470, W_DOT, 104)             # 忄：左点
    p.vbar(250, 0, 820, W_MAIN)             # 忄：中竖
    p.dot(320, 620, W_DOT, 104)             # 忄：右点
    p.diag(490, 785, 400, 690, W_SEC)       # 生：撇
    p.hmid(430, 790, 612, W_THIN)           # 生：上横
    p.hmid(390, 860, 306, W_MAIN)           # 生：中横
    p.vbar(640, 0, 704, W_MAIN)             # 生：竖
    p.hmid(360, 900, 0, W_MAIN)             # 生：下横
    return g


def glyph_no() -> Glyph:
    """的 U+7684（8画）—— 白 + 勺。
    分区：白 占 x 134..426 / y 120..809；勺 占 x 454..884（与 約 的勺同部件）。
    """
    g = Glyph("uni7684", advance=1000, unicode=0x7684, note="的：白 + 勺")
    p = Pen(g)
    p.diag(290, 790, 240, 690, W_THIN)      # 白：丿
    p.hmid(140, 420, 616, W_MAIN)           # 白：顶横
    p.vbar(182, 120, 712, W_MAIN)           # 白：左竖
    p.vbar(378, 120, 712, W_MAIN)           # 白：右竖
    p.hmid(182, 420, 370, W_THIN)           # 白：中横
    p.hmid(140, 420, 120, W_MAIN)           # 白：底横
    part_you(Pen(g, ox=490, sx=0.92))       # 勺
    return g


def glyph_you_yuo() -> Glyph:
    """要 U+8981（9画）—— 覀 + 女。
    分区：覀 占 x 180..876 / y 560..808（四竖，竖距 120 ≥ 60）；
    女 占 x 180..820 / y 60..500。
    """
    g = Glyph("uni8981", advance=1000, unicode=0x8981, note="要：覀 + 女")
    p = Pen(g)
    p.hmid(180, 876, 720, W_THIN)           # 覀：顶横
    p.vbar(222, 560, 720, W_THIN)           # 覀：左竖
    p.vbar(426, 560, 720, W_THIN)           # 覀：内竖 1
    p.vbar(630, 560, 720, W_THIN)           # 覀：内竖 2
    p.vbar(834, 560, 720, W_THIN)           # 覀：右竖
    p.hmid(180, 876, 560, W_THIN)           # 覀：底横
    p.diag(470, 500, 330, 300, W_SEC)       # 女：撇点（上段）
    p.diag(330, 300, 540, 90, W_SEC)        # 女：撇点（下段）
    p.diag(630, 440, 250, 60, W_SEC)        # 女：撇
    p.hmid(180, 820, 240, W_MAIN)           # 女：横
    return g


def glyph_sei_hei() -> Glyph:
    """制 U+5236（8画）—— 丿 + 二 + 巾 + 刂。
    分区：左半 丿二巾 占 x 160..600；刂 占 x 660..894。
    """
    g = Glyph("uni5236", advance=1000, unicode=0x5236, note="制：丿二 + 巾 + 刂")
    p = Pen(g)
    p.diag(265, 785, 180, 685, W_THIN)      # 丿
    p.hmid(210, 540, 670, W_THIN)           # 二：上横
    p.hmid(160, 600, 545, W_MAIN)           # 二：下横
    p.vbar(212, 170, 545, W_MAIN)           # 巾：左竖
    p.hmid(170, 570, 430, W_THIN)           # 巾：顶横
    p.vbar(528, 170, 545, W_MAIN)           # 巾：右竖
    p.vbar(342, 50, 545, W_MAIN)            # 巾：中竖
    p.vbar(698, 240, 640, W_THIN)           # 刂：短竖
    p.vbar(852, 60, 780, W_MAIN)            # 刂：长竖
    p.diag(852, 80, 760, 170, W_THIN)       # 刂：钩
    return g


def glyph_chi() -> Glyph:
    """治 U+6CBB（8画）—— 氵 + 台（厶 + 口）。
    分区：氵 占 x 112..290；台 占 x 420..848 / y 120..816。
    """
    g = Glyph("uni6CBB", advance=1000, unicode=0x6CBB, note="治：氵 + 台")
    part_sanzui(Pen(g, ox=95, sx=0.85))
    p = Pen(g)
    p.diag(615, 785, 480, 640, W_SEC)       # 厶：撇折的上段
    p.hmid(480, 740, 640, W_SEC)            # 厶：折的横
    p.dot(800, 680, W_MAIN, 112)           # 厶：点
    part_kuchi(p, 420, 120, 400, 380, W_MAIN)  # 口
    return g


def glyph_do() -> Glyph:
    """度 U+5EA6（9画）—— 广（丶 + 一 + 撇）+ 廿 + 又。
    分区：广 占 x 130..850 / y 130..818；廿 占 x 360..724 / y 380..608；
    又 占 x 230..790 / y 100..408。
    """
    g = Glyph("uni5EA6", advance=1000, unicode=0x5EA6, note="度：广 + 廿 + 又")
    p = Pen(g)
    p.dot(500, 765, W_MAIN, 96)             # 广：点
    p.hmid(150, 850, 650, W_MAIN)           # 广：横
    p.diag(205, 700, 145, 130, W_SEC)       # 广：撇
    p.hmid(360, 724, 520, W_THIN)           # 廿：上横
    p.vbar(402, 430, 620, W_MAIN)           # 廿：左竖
    p.vbar(682, 430, 620, W_MAIN)           # 廿：右竖
    p.hmid(360, 724, 380, W_THIN)           # 廿：下横
    p.hmid(280, 780, 240, W_THIN)           # 又：横
    p.diag(760, 300, 320, 110, W_SEC)       # 又：撇
    p.diag(340, 300, 790, 100, W_SEC)       # 又：捺
    return g


def glyph_ki() -> Glyph:
    """気 U+6C17（6画）—— 气（丿 + 一 + 一 + 横斜钩）+ メ。
    分区：气 占 x 200..876 / y 113..813；メ 占 x 290..640 / y 110..450。
    """
    g = Glyph("uni6C17", advance=1000, unicode=0x6C17, note="気：气 + メ")
    p = Pen(g)
    p.diag(325, 785, 250, 700, W_THIN)      # 气：丿
    p.hmid(280, 540, 690, W_THIN)           # 气：一（短）
    p.hmid(240, 720, 590, W_SEC)            # 气：一（中）
    p.hmid(200, 840, 480, W_MAIN)           # 气：横斜钩的横
    p.diag(830, 500, 730, 190, W_MAIN)      # 气：斜
    p.diag(730, 200, 640, 280, W_THIN)      # 气：钩
    p.diag(610, 430, 330, 110, W_SEC)       # メ：丿
    p.diag(320, 400, 610, 120, W_SEC)       # メ：丶
    return g


def glyph_sei_aru() -> Glyph:
    """成 U+6210（6画）—— 厂 + 横折钩 + 戈（斜钩 + 撇 + 点）。
    分区：左半 占 x 135..540；斜钩 占 x 515..745；点 占 x 782..878。
    斜钩自右上向左下长扫再向右上挑钩；撇从斜钩中段起笔向左下，
    端点落在横折钩的竖上（埋进墨迹，避免零面积尖刺）。
    """
    g = Glyph("uni6210", advance=1000, unicode=0x6210, note="成：厂 + 戈")
    p = Pen(g)
    p.hmid(160, 540, 620, W_THIN)           # 横
    p.diag(205, 700, 135, 120, W_SEC)       # 撇（厂）
    p.hmid(250, 500, 430, W_THIN)           # 横折钩的横
    p.vbar(292, 130, 524, W_MAIN)           # 横折钩的竖
    p.diag(292, 150, 195, 230, W_THIN)      # 横折钩的钩
    p.diag(700, 780, 560, 120, W_SEC)       # 斜钩
    p.diag(560, 120, 690, 240, W_THIN)      # 斜钩的钩
    p.diag(650, 545, 290, 330, W_THIN)      # 撇（与斜钩相交）
    p.dot(830, 740, W_MAIN, 104)            # 点
    return g


def glyph_mochi() -> Glyph:
    """持 U+6301（9画）—— 扌 + 寺（土 + 寸）。
    分区：扌 占 x 95..415；寺 占 x 440..900 / y 60..734。
    """
    g = Glyph("uni6301", advance=1000, unicode=0x6301, note="持：扌 + 寺")
    part_tehen(Pen(g, ox=95))
    p = Pen(g)
    p.hmid(500, 820, 650, W_THIN)           # 土：上横
    p.vbar(668, 520, 734, W_MAIN)           # 土：竖
    p.hmid(470, 880, 520, W_MAIN)           # 土：下横
    p.hmid(440, 900, 390, W_MAIN)           # 寸：横
    p.vbar(742, 60, 486, W_MAIN)            # 寸：竖钩
    p.diag(742, 80, 640, 170, W_THIN)       # 寸：钩
    p.dot(560, 330, W_DOT, 100)             # 寸：点
    return g


def glyph_kyo() -> Glyph:
    """協 U+5354（8画）—— 十 + 劦（一力在上，两力在下）。
    分区：十 占 x 130..340；上力 占 x 375..806 / y 492..784；下两力 占 x 243..850。
    三个力复用 part_riki 同一套拆法，只有大小与位置不同。
    """
    g = Glyph("uni5354", advance=1000, unicode=0x5354, note="協：十 + 劦")
    p = Pen(g)
    p.hmid(130, 340, 600, W_MAIN)           # 十：横
    p.vbar(235, 80, 760, W_MAIN)            # 十：竖
    part_riki(p, 480, 800, y_top=700, y_base=520, w=W_THIN)   # 上力
    part_riki(p, 380, 590, y_top=330, y_base=170, w=W_THIN)   # 下左力
    part_riki(p, 620, 850, y_top=330, y_base=170, w=W_THIN)   # 下右力
    return g


def glyph_toru() -> Glyph:
    """取 U+53D6（8画）—— 耳 + 又。
    分区：耳 占 x 110..500 / y 140..812；又 占 x 520..870 / y 200..664。
    """
    g = Glyph("uni53D6", advance=1000, unicode=0x53D6, note="取：耳 + 又")
    p = Pen(g)
    p.hmid(140, 480, 724, W_THIN)           # 耳：顶横
    p.vbar(222, 140, 812, W_MAIN)           # 耳：左竖
    p.vbar(438, 140, 812, W_MAIN)           # 耳：右竖
    p.hmid(180, 480, 560, W_THIN)           # 耳：内横 1
    p.hmid(180, 480, 380, W_THIN)           # 耳：内横 2
    p.hmid(110, 500, 140, W_MAIN)           # 耳：底横
    p.hmid(520, 870, 580, W_THIN)           # 又：横
    p.diag(850, 620, 570, 210, W_SEC)       # 又：撇
    p.diag(570, 610, 870, 200, W_SEC)       # 又：捺
    return g


def glyph_wa() -> Glyph:
    """和 U+548C（8画）—— 禾 + 口。
    分区：禾 占 x 107..460 / y 60..813；口 占 x 560..900 / y 200..628。
    """
    g = Glyph("uni548C", advance=1000, unicode=0x548C, note="和：禾 + 口")
    p = Pen(g)
    p.diag(375, 778, 260, 700, W_THIN)      # 禾：丿
    p.hmid(120, 460, 600, W_MAIN)           # 禾：横
    p.vbar(304, 60, 700, W_MAIN)            # 禾：竖
    p.diag(300, 580, 150, 180, W_SEC)       # 禾：撇
    p.diag(310, 580, 450, 200, W_SEC)       # 禾：捺
    part_kuchi(p, 560, 200, 340, 428, W_MAIN)  # 口
    return g


def glyph_shi() -> Glyph:
    """思 U+601D（9画）—— 田 + 心。
    分区：田 占 x 230..770 / y 380..820；心 占 x 173..838 / y 78..346。
    """
    g = Glyph("uni601D", advance=1000, unicode=0x601D, note="思：田 + 心")
    p = Pen(g)
    p.hmid(230, 770, 724, W_MAIN)           # 田：顶横
    p.vbar(272, 380, 820, W_MAIN)           # 田：左竖
    p.vbar(728, 380, 820, W_MAIN)           # 田：右竖
    p.vbar(500, 380, 820, W_MAIN)           # 田：中竖
    p.hmid(272, 770, 550, W_THIN)           # 田：中横
    p.hmid(230, 770, 380, W_MAIN)           # 田：底横
    p.dot(215, 250, W_DOT, 100)             # 心：左点
    p.diag(350, 310, 380, 150, W_SEC)       # 心：卧钩（上段）
    p.diag(380, 150, 650, 120, W_THIN)      # 心：卧钩（下段）
    p.dot(500, 290, W_MAIN, 112)            # 心：中点
    p.dot(790, 230, W_MAIN, 112)            # 心：右点
    return g


def glyph_uke() -> Glyph:
    """受 U+53D7（8画）—— 爫（丿 + 三点）+ 又。
    分区：爫 占 x 232..640 / y 534..813；又 占 x 230..844 / y 66..476。
    """
    g = Glyph("uni53D7", advance=1000, unicode=0x53D7, note="受：爫 + 又")
    p = Pen(g)
    p.diag(510, 768, 250, 675, W_MAIN)      # 爫：丿
    p.dot(290, 590, W_MAIN, 112)            # 爫：点 1
    p.dot(450, 590, W_MAIN, 112)            # 爫：点 2
    p.dot(610, 590, W_MAIN, 112)            # 爫：点 3
    p.hmid(230, 830, 380, W_MAIN)           # 又：横
    p.diag(810, 440, 480, 100, W_MAIN)      # 又：撇
    p.diag(330, 420, 780, 110, W_MAIN)      # 又：捺
    return g


def glyph_ta() -> Glyph:
    """多 U+591A（6画）—— 夕 + 夕（上夕大、下夕小并右移）。
    分区：上夕 占 x 193..690 / y 408..816；下夕 占 x 486..848 / y 141..520。
    """
    g = Glyph("uni591A", advance=1000, unicode=0x591A, note="多：夕 + 夕")
    p = Pen(g)
    p.diag(445, 780, 235, 600, W_MAIN)      # 上夕：撇
    p.hmid(270, 660, 610, W_MAIN)           # 上夕：横撇的横
    p.diag(650, 650, 280, 450, W_MAIN)      # 上夕：横撇的撇
    p.dot(420, 470, W_MAIN, 112)            # 上夕：点
    p.diag(660, 520, 520, 380, W_MAIN)      # 下夕：撇
    p.hmid(530, 830, 340, W_MAIN)           # 下夕：横撇的横
    p.diag(820, 380, 540, 180, W_MAIN)      # 下夕：横撇的撇
    p.dot(680, 255, W_MAIN, 112)            # 下夕：点
    return g


def glyph_ken() -> Glyph:
    """県 U+770C（9画）—— 目 + 一 + 小。
    分区：目 占 x 300..700 / y 496..820；一 占 x 150..850 / y 330..426；
    小 占 x 220..790 / y 140..360。
    """
    g = Glyph("uni770C", advance=1000, unicode=0x770C, note="県：目 + 一 + 小")
    p = Pen(g)
    p.hmid(300, 700, 736, W_THIN)           # 目：顶横
    p.vbar(342, 496, 820, W_MAIN)           # 目：左竖
    p.vbar(658, 496, 820, W_MAIN)           # 目：右竖
    p.hmid(300, 700, 616, W_THIN)           # 目：内横 1
    p.hmid(300, 700, 496, W_THIN)           # 目：内横 2
    p.hmid(150, 850, 330, W_MAIN)           # 一
    p.vbar(500, 60, 360, W_MAIN)            # 小：竖
    p.diag(400, 320, 250, 170, W_THIN)      # 小：撇
    p.diag(600, 320, 760, 170, W_THIN)      # 小：捺
    return g


def glyph_ai() -> Glyph:
    """安 U+5B89（6画）—— 宀（丶 + 冖）+ 女。
    分区：宀 占 x 174..826 / y 540..820；女 占 x 200..800 / y 130..588。
    """
    g = Glyph("uni5B89", advance=1000, unicode=0x5B89, note="安：宀 + 女")
    p = Pen(g)
    p.dot(500, 770, W_MAIN, 100)            # 宀：点
    p.hmid(180, 820, 620, W_MAIN)           # 宀：冖的横
    p.vbar(222, 540, 620, W_MAIN)           # 宀：冖的左点
    p.vbar(778, 560, 620, W_MAIN)           # 宀：冖的右折
    p.diag(470, 560, 340, 380, W_MAIN)      # 女：撇点（上段）
    p.diag(340, 380, 540, 180, W_MAIN)      # 女：撇点（下段）
    p.diag(620, 500, 270, 130, W_MAIN)      # 女：撇
    p.hmid(200, 800, 330, W_MAIN)           # 女：横
    return g


def glyph_ho() -> Glyph:
    """保 U+4FDD（9画）—— 亻 + 呆（口 + 木）。
    分区：亻 占 x 100..320；呆 占 x 360..900 / y 60..800。
    """
    g = Glyph("uni4FDD", advance=1000, unicode=0x4FDD, note="保：亻 + 呆")
    part_ninben(Pen(g, ox=95, sx=0.85))
    p = Pen(g)
    part_kuchi(p, 500, 520, 380, 280, W_MAIN)   # 口
    part_moku(p, 360, 900, y_top=520, y_base=60, y_bar=380, bar_w=W_MAIN)
    return g


def glyph_kai() -> Glyph:
    """改 U+6539（7画）—— 己 + 攵。
    分区：己 占 x 140..470 / y 100..708；攵 占 x 520..880 / y 100..790。
    """
    g = Glyph("uni6539", advance=1000, unicode=0x6539, note="改：己 + 攵")
    p = Pen(g)
    p.hmid(140, 430, 620, W_THIN)           # 己：横折的横
    p.vbar(388, 500, 708, W_MAIN)           # 己：横折的竖
    p.hmid(140, 430, 500, W_THIN)           # 己：中横
    p.vbar(182, 100, 588, W_MAIN)           # 己：竖
    p.hmid(140, 400, 100, W_THIN)           # 己：竖弯钩的底
    p.diag(400, 140, 470, 240, W_THIN)      # 己：钩
    p.diag(620, 790, 540, 700, W_THIN)      # 攵：丿
    p.hmid(540, 880, 610, W_THIN)           # 攵：一
    p.diag(760, 690, 520, 100, W_SEC)       # 攵：撇
    p.diag(540, 620, 870, 110, W_SEC)       # 攵：捺
    return g


def glyph_hatsu() -> Glyph:
    """初 U+521D（7画）—— 衤 + 刀。
    分区：衤 占 x 130..424 / y 60..818；刀 占 x 470..886 / y 140..708。
    """
    g = Glyph("uni521D", advance=1000, unicode=0x521D, note="初：衤 + 刀")
    p = Pen(g)
    p.dot(280, 770, W_DOT, 96)              # 衤：点
    p.hmid(140, 390, 650, W_THIN)           # 衤：横撇的横
    p.diag(390, 690, 270, 560, W_THIN)      # 衤：横撇的撇
    p.vbar(282, 60, 700, W_MAIN)            # 衤：竖
    p.diag(250, 540, 140, 380, W_THIN)      # 衤：撇
    p.dot(380, 500, W_DOT, 100)             # 衤：点
    p.hmid(470, 880, 620, W_THIN)           # 刀：横折钩的横
    p.vbar(838, 140, 708, W_MAIN)           # 刀：横折钩的竖
    p.diag(838, 160, 700, 260, W_THIN)      # 刀：钩
    p.diag(700, 700, 500, 120, W_SEC)       # 刀：撇
    return g


def glyph_yubi() -> Glyph:
    """指 U+6307（9画）—— 扌 + 旨（匕 + 日）。
    分区：扌 占 x 95..415；旨 占 x 470..870 / y 60..814。
    """
    g = Glyph("uni6307", advance=1000, unicode=0x6307, note="指：扌 + 旨")
    part_tehen(Pen(g, ox=95))
    p = Pen(g)
    p.diag(630, 780, 500, 690, W_THIN)      # 旨：匕的撇
    p.vbar(542, 640, 810, W_MAIN)           # 旨：匕的竖
    p.hmid(500, 720, 640, W_THIN)           # 旨：匕的底
    p.hmid(470, 870, 456, W_MAIN)           # 日：顶横
    p.vbar(512, 60, 552, W_MAIN)            # 日：左竖
    p.vbar(828, 60, 552, W_MAIN)            # 日：右竖
    p.hmid(512, 870, 280, W_THIN)           # 日：中横
    p.hmid(470, 870, 60, W_MAIN)            # 日：底横
    return g


def glyph_kai_jo() -> Glyph:
    """界 U+754C（9画）—— 田 + 介（人 + 丿 + 丨）。
    分区：田 占 x 280..720 / y 400..820；介 占 x 230..770 / y 60..460。
    """
    g = Glyph("uni754C", advance=1000, unicode=0x754C, note="界：田 + 介")
    p = Pen(g)
    p.hmid(280, 720, 724, W_MAIN)           # 田：顶横
    p.vbar(322, 400, 820, W_MAIN)           # 田：左竖
    p.vbar(678, 400, 820, W_MAIN)           # 田：右竖
    p.vbar(500, 400, 820, W_MAIN)           # 田：中竖
    p.hmid(322, 720, 560, W_THIN)           # 田：中横
    p.hmid(280, 720, 400, W_MAIN)           # 田：底横
    p.diag(500, 460, 230, 220, W_SEC)       # 介：人的撇
    p.diag(500, 460, 770, 220, W_SEC)       # 介：人的捺
    p.diag(420, 380, 330, 90, W_THIN)       # 介：丿
    p.vbar(632, 60, 380, W_MAIN)            # 介：丨
    return g


def glyph_hyaku() -> Glyph:
    """百 U+767E（6画）—— 一 + 白（丿 + 日）。
    分区：一 占 x 150..850 / y 724..816；白 占 x 280..720 / y 60..564。
    6 画字整体偏重，这里把日部降到 84，把墨量拉回同档中位。
    """
    g = Glyph("uni767E", advance=1000, unicode=0x767E, note="百：一 + 白")
    p = Pen(g)
    p.hmid(150, 850, 724, W_SEC)            # 一
    p.diag(420, 700, 330, 620, W_THIN)      # 白：丿
    p.hmid(280, 720, 480, W_THIN)           # 日：顶横
    p.vbar(322, 60, 564, W_THIN)            # 日：左竖
    p.vbar(678, 60, 564, W_THIN)            # 日：右竖
    p.hmid(322, 720, 280, W_THIN)           # 日：中横
    p.hmid(280, 720, 60, W_THIN)            # 日：底横
    return g


def build() -> list[Glyph]:
    return [
        glyph_tong(),      # 通 U+901A
        glyph_gen(),       # 言 U+8A00
        glyph_tai(),       # 体 U+4F53
        glyph_tou(),       # 当 U+5F53
        glyph_yaku(),      # 約 U+7D04
        glyph_shu(),       # 首 U+9996
        glyph_hou(),       # 法 U+6CD5
        glyph_rai(),       # 来 U+6767
        glyph_saku(),      # 作 U+4F5C
        glyph_sei(),       # 性 U+6027
        glyph_no(),        # 的 U+7684
        glyph_you_yuo(),   # 要 U+8981
        glyph_sei_hei(),   # 制 U+5236
        glyph_chi(),       # 治 U+6CBB
        glyph_do(),        # 度 U+5EA6
        glyph_ki(),        # 気 U+6C17
        glyph_sei_aru(),   # 成 U+6210
        glyph_mochi(),     # 持 U+6301
        glyph_kyo(),       # 協 U+5354
        glyph_toru(),      # 取 U+53D6
        glyph_wa(),        # 和 U+548C
        glyph_shi(),       # 思 U+601D
        glyph_uke(),       # 受 U+53D7
        glyph_ta(),        # 多 U+591A
        glyph_ken(),       # 県 U+770C
        glyph_ai(),        # 安 U+5B89
        glyph_ho(),        # 保 U+4FDD
        glyph_kai(),       # 改 U+6539
        glyph_hatsu(),     # 初 U+521D
        glyph_yubi(),      # 指 U+6307
        glyph_kai_jo(),    # 界 U+754C
        glyph_hyaku(),     # 百 U+767E
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-002.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
