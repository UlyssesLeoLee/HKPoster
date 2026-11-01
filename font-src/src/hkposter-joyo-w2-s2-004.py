"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-004。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
- 字面框统一 x 60..940 / y 0..820（advance 1000），与 zh-HK 繁体同一档，便于中英日混排。
- 笔画权重沿用漢字档：主 96 / 次 92 / 细 84 / 点 84。本批笔画数集中在 6–9 画，
  为了避免同批出现"有的太轻、有的太闷"：笔画少的字用满 96 主档，
  笔画多的字只在横画叠横画处局部减重到 84，不靠压扁字形来控墨量。
- 密排处（横画叠横画）内白 ≥ 24 单位；竖与竖之间 ≥ 60 单位（GLY-006）。
- 同族观感：亻 / 扌 / 木 / 冫 / 矩形框 全部抽成部件函数
  （part_ninben / part_tehen / part_wood / part_sanzui / box），
  批内复用同一套坐标与笔画拆法，只做位置与大小的光学校正（docs/03 GLY-004）。
- 字体本体只做笔画本身；霓虹、描边、金属、旧化纹理属于样张层，不写进字形轮廓。
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

EM_X0 = 60.0
EM_X1 = 940.0
EM_Y0 = 0.0
EM_Y1 = 820.0


# --------------------------------------------------------------- 对齐辅助
def bar_top(w: float = W_MAIN) -> float:
    """横画中心线：墨迹上缘对齐 y=820。"""
    return EM_Y1 - w / 2.0


def bar_base(w: float = W_MAIN) -> float:
    """横画中心线：墨迹下缘对齐 y=0。"""
    return EM_Y0 + w / 2.0


def box(g: Glyph, x0: float, x1: float, y0: float, y1: float,
        w: float = W_MAIN, wv: float | None = None) -> None:
    """矩形框：上横 / 下横 / 左竖 / 右竖；并集后内白自动成洞。"""
    wv = w if wv is None else wv
    g.hbar(x0, x1, y1 - w / 2.0, w)
    g.hbar(x0, x1, y0 + w / 2.0, w)
    g.vbar(x0 + w / 2.0, y0, y1, wv)
    g.vbar(x1 - w / 2.0, y0, y1, wv)


def part_ninben(g: Glyph, x0: float, x1: float, ytop: float, ybase: float) -> None:
    """亻：撇 + 竖。批内统一拆法（係 / 住 / 位 / 価 共用）。"""
    span = x1 - x0
    height = ytop - ybase
    g.diag(x0 + 0.58 * span, ytop - 28.0,
           x0 + 0.21 * span, ytop - 28.0 - 0.31 * height, W_MAIN)
    g.vbar(x0 + 0.31 * span, ytop - 0.26 * height, ybase, W_MAIN)


def part_tehen(g: Glyph, x0: float, x1: float, ytop: float, ybase: float) -> None:
    """扌：横 + 竖钩 + 提。批内统一拆法。"""
    span = x1 - x0
    height = ytop - ybase
    g.hbar(x0, x0 + 0.95 * span, ytop - 0.27 * height, W_SEC)
    g.vbar(x0 + 0.46 * span, ybase + 0.05 * height, ytop - 0.05 * height, W_MAIN)
    g.diag(x0 + 0.46 * span, ybase + 0.05 * height,
           x0 + 0.22 * span, ybase + 0.12 * height, W_THIN)
    g.diag(x0 + 0.06 * span, ybase + 0.29 * height,
           x0 + 0.92 * span, ybase + 0.43 * height, W_THIN)


def part_wood(g: Glyph, x0: float, x1: float, ytop: float, ybase: float) -> None:
    """木：横 + 竖 + 撇 + 捺。批内统一拆法。"""
    span = x1 - x0
    height = ytop - ybase
    g.hbar(x0 + 0.05 * span, x1, ytop - 0.24 * height, W_MAIN)
    g.vbar(x0 + 0.56 * span, ybase, ytop - 0.16 * height, W_MAIN)
    g.diag(x0 + 0.56 * span, ytop - 0.25 * height,
           x0 + 0.11 * span, ybase + 0.05 * height, W_THIN)
    g.diag(x0 + 0.58 * span, ytop - 0.25 * height,
           x1 - 0.02 * span, ybase + 0.08 * height, W_SEC)


def part_sanzui(g: Glyph, x0: float, x1: float, ytop: float, ybase: float,
                two: bool = False) -> None:
    """氵（三点）/ 冫（两点）：点 + 点 + 提；two=True 时只画一点一提。"""
    span = x1 - x0
    height = ytop - ybase
    g.diag(x0 + 0.80 * span, ytop - 0.02 * height,
           x0 + 0.28 * span, ytop - 0.16 * height, W_DOT)
    if not two:
        g.diag(x0 + 0.70 * span, ytop - 0.28 * height,
               x0 + 0.18 * span, ytop - 0.42 * height, W_DOT)
    g.diag(x0 + 0.06 * span, ybase + 0.10 * height,
           x0 + 0.92 * span, ybase + 0.28 * height, W_SEC)


# --------------------------------------------------------------- 32 字
def g_qiu() -> Glyph:
    """求（7画）：上横 + 竖钩 + 左撇 + 左提 + 右上点 + 右捺。

    部件分区：整字单区。上横 y 中心 772（墨 724..820）；竖钩 x=470；
    左撇接上横左段；左提右上端接竖；右上点接上横；右捺起点接竖。
    """
    g = Glyph("uni6C42", advance=1000, unicode=0x6C42,
              note="求：横+竖钩+左撇+左提+右上点+右捺")
    g.hbar(120, 880, 772, W_MAIN)                       # ① 一
    g.vbar(470, 772, 90, W_MAIN)                        # ② 竖
    g.diag(468, 95, 375, 140, W_THIN)                   # ③ 钩
    g.diag(320, 700, 215, 625, W_THIN)                  # ④ 左撇（接上横）
    g.diag(140, 320, 420, 420, W_MAIN)                  # ⑤ 左提（接竖）
    g.diag(700, 710, 770, 630, W_THIN)                  # ⑥ 右上点（接上横，斜向右下）
    g.diag(510, 350, 880, 110, W_MAIN)                  # ⑦ 右捺（接竖）
    return g


def g_sho() -> Glyph:
    """所（8画）：戸 + 斤。

    部件分区：左戸 x 60..400，右斤 x 430..940。
    左戸＝点 + 横 + 左折竖 + 下缘横；右斤＝上撇 + 横 + 长撇 + 竖。
    """
    g = Glyph("uni6240", advance=1000, unicode=0x6240, note="所：戸+斤")
    g.diag(175, 790, 120, 735, W_THIN)                  # ① 点
    g.hbar(95, 395, 675, W_MAIN)                         # ② 横
    g.vbar(135, 675, 240, W_MAIN)                        # ③ 左折竖（略垂于下缘横）
    g.hbar(135, 375, 300, W_SEC)                         # ④ 下缘横
    g.diag(880, 750, 560, 600, W_MAIN)                  # ⑤ 上撇
    g.hbar(470, 830, 560, W_SEC)                         # ⑥ 横
    g.diag(560, 600, 470, 130, W_THIN)                   # ⑦ 长撇
    g.vbar(790, 560, 90, W_MAIN)                         # ⑧ 竖
    return g


def g_ji() -> Glyph:
    """次（6画）：冫 + 欠。

    部件分区：左冫 x 60..300，右欠 x 400..940。
    欠＝ノ + 横 + 撇 + 捺；撇捺在中部交叉。
    """
    g = Glyph("uni6B21", advance=1000, unicode=0x6B21, note="次：冫+欠")
    g.diag(215, 660, 145, 575, W_DOT)                   # ① 点
    g.diag(120, 300, 300, 390, W_MAIN)                  # ② 提
    g.diag(520, 765, 415, 670, W_SEC)                    # ③ ノ（自横左端斜下）
    g.hbar(500, 900, 760, W_SEC)                         # ④ 横
    g.diag(640, 730, 430, 150, W_SEC)                    # ⑤ 撇
    g.diag(660, 710, 890, 150, W_MAIN)                   # ⑥ 捺
    return g


def g_pin() -> Glyph:
    """品（9画）：三口。

    部件分区：上口 x 340..660 / y 500..820；下左口 x 60..440；
    下右口 x 500..940 / y 0..430。三口之间留 40~70 单位白缝，不粘连。
    """
    g = Glyph("uni54C1", advance=1000, unicode=0x54C1, note="品：三口")
    box(g, 340, 660, 500, 820, W_THIN, W_THIN)           # ①-③ 上口
    box(g, 60, 430, 0, 430, W_THIN, W_THIN)              # ④-⑥ 下左口
    box(g, 510, 940, 0, 430, W_THIN, W_THIN)             # ⑦-⑨ 下右口
    return g


def g_zaku() -> Glyph:
    """昨（9画）：日 + 乍。

    部件分区：左日 x 60..340 / y 120..800；右乍 x 400..940。
    乍＝ノ + 横 + 竖 + 两条右伸横。
    """
    g = Glyph("uni6628", advance=1000, unicode=0x6628, note="昨：日+乍")
    box(g, 60, 340, 120, 800, W_THIN, W_THIN)            # ①-④ 日
    g.hbar(60, 340, 460, W_THIN)                         # ⑤ 日中横
    g.diag(480, 765, 375, 670, W_MAIN)                   # ⑥ ノ（自横左端斜下）
    g.hbar(430, 900, 752, W_SEC)                         # ⑦ 横
    g.vbar(490, 752, 60, W_MAIN)                         # ⑧ 竖
    g.hbar(490, 760, 470, W_THIN)                        # ⑨ 右上短横
    g.hbar(490, 880, 300, W_SEC)                         # ⑩ 右下长横
    return g


def g_kei() -> Glyph:
    """計（9画）：言 + 十。

    部件分区：左言 x 60..430（上三横 + 口），右十 x 480..940。
    """
    g = Glyph("uni8A08", advance=1000, unicode=0x8A08, note="計：言+十")
    g.hbar(70, 420, 772, W_MAIN)                         # ① 一
    g.hbar(110, 390, 640, W_THIN)                        # ② 二
    g.hbar(150, 360, 530, W_THIN)                        # ③ 三
    box(g, 130, 390, 180, 440, W_THIN, W_THIN)           # ④-⑥ 口
    g.hbar(500, 930, 480, W_MAIN)                        # ⑦ 横
    g.vbar(715, 50, 790, W_MAIN)                         # ⑧ 竖
    return g


def g_shi() -> Glyph:
    """死（6画）：歹 + 匕。

    部件分区：左歹 x 60..620（横 + 夕），右下匕 x 600..940 / y 50..500。
    """
    g = Glyph("uni6B7B", advance=1000, unicode=0x6B7B, note="死：歹+匕")
    g.hbar(70, 610, 772, W_MAIN)                         # ① 一（墨 724..820）
    g.diag(340, 650, 140, 500, W_SEC)                    # ② 撇
    g.hbar(340, 600, 650, W_THIN)                        # ③ 横（フ上段，墨 608..692）
    g.diag(600, 650, 430, 390, W_THIN)                   # ④ 撇（フ下段）
    g.diag(480, 560, 405, 460, W_DOT)                    # ⑤ 夕点
    g.diag(610, 380, 780, 450, W_SEC)                    # ⑥ 提
    g.vbar(690, 420, 50, W_MAIN)                         # ⑦ 竖
    g.diag(690, 50, 870, 130, W_THIN)                    # ⑧ 钩
    return g


def g_kan() -> Glyph:
    """官（8画）：宀 + 㠯。

    部件分区：宀 y 570..800；㠯 x 300..700 / y 60..660，左竖上端与宀横相接。
    """
    g = Glyph("uni5B98", advance=1000, unicode=0x5B98, note="官：宀+㠯")
    g.diag(465, 780, 530, 725, W_DOT)                   # ① 点
    g.vbar(245, 660, 570, W_THIN)                        # ② 冖左点
    g.hbar(200, 790, 680, W_SEC)                         # ③ 冖横
    g.diag(790, 680, 730, 590, W_THIN)                   # ④ 冖右钩
    g.vbar(350, 660, 60, W_MAIN)                         # ⑤ 㠯左竖（上行接宀）
    g.hbar(350, 700, 520, W_SEC)                         # ⑥ 㠯上横
    g.vbar(652, 60, 566, W_SEC)                          # ⑦ 㠯右竖
    g.hbar(350, 700, 330, W_THIN)                        # ⑧ 中横
    g.hbar(350, 700, 128, W_SEC)                         # ⑨ 下横
    return g


def g_kei_kei() -> Glyph:
    """係（9画）：亻 + 系。

    部件分区：左亻 x 60..330；右系 x 380..940。
    系＝ノ + 两个 ㄥ + 幺点 + 小（竖钩 + 左右点）。
    """
    g = Glyph("uni4FC2", advance=1000, unicode=0x4FC2, note="係：亻+系")
    part_ninben(g, 60, 330, 820, 0)                      # ①-② 亻
    g.diag(690, 750, 600, 690, W_THIN)                   # ③ ノ
    g.diag(730, 745, 810, 675, W_THIN)                   # ④ 幺点
    g.diag(600, 690, 500, 600, W_THIN)                   # ⑤ ㄥ1上段
    g.diag(500, 600, 660, 530, W_THIN)                   # ⑥ ㄥ1下段
    g.diag(660, 530, 550, 430, W_THIN)                   # ⑦ ㄥ2上段
    g.diag(550, 430, 720, 350, W_THIN)                   # ⑧ ㄥ2下段
    g.vbar(680, 60, 400, W_MAIN)                         # ⑨ 小竖钩
    g.diag(680, 60, 600, 100, W_THIN)                    # ⑩ 钩
    g.diag(570, 320, 480, 150, W_THIN)                   # ⑪ 小左点
    g.diag(800, 320, 880, 150, W_THIN)                   # ⑫ 小右点
    return g


def g_tou() -> Glyph:
    """投（7画）：扌 + 殳。

    部件分区：左扌 x 60..350；右殳 x 430..940（上几 + 下又）。
    """
    g = Glyph("uni6295", advance=1000, unicode=0x6295, note="投：扌+殳")
    part_tehen(g, 60, 350, 800, 0)                      # ①-④ 扌
    g.diag(560, 780, 480, 690, W_SEC)                    # ⑤ ノ
    g.hbar(470, 845, 720, W_SEC)                         # ⑥ 横
    g.vbar(800, 760, 440, W_SEC)                         # ⑦ 竖
    g.diag(800, 440, 745, 405, W_THIN)                   # ⑧ 钩
    g.hbar(560, 820, 410, W_THIN)                        # ⑨ 又横
    g.diag(820, 410, 470, 100, W_THIN)                   # ⑩ 又撇
    g.diag(600, 410, 880, 105, W_MAIN)                    # ⑪ 又捺
    return g


def g_hen() -> Glyph:
    """変（9画）：亠 + ツ + 又（Jōyō 通行字形）。

    部件分区：亠 y 700..790；中间三笔（撇 / 竖 / 点）y 505..690；又 y 80..512。
    """
    g = Glyph("uni5909", advance=1000, unicode=0x5909, note="変：亠+业+又")
    g.vbar(500, 700, 790, W_SEC)                         # ① 顶竖（亠的点作短竖）
    g.hbar(140, 860, 720, W_MAIN)                        # ② 横
    g.diag(330, 655, 225, 505, W_SEC)                    # ③ 内撇（左）
    g.vbar(500, 470, 690, W_SEC)                         # ④ 内竖（中）
    g.diag(670, 655, 775, 505, W_SEC)                    # ⑤ 内点（右）
    g.hbar(330, 720, 470, W_THIN)                        # ⑥ 又横
    g.diag(720, 470, 300, 90, W_THIN)                    # ⑦ 又撇
    g.diag(340, 470, 890, 80, W_MAIN)                    # ⑧ 又捺
    return g


def g_dan() -> Glyph:
    """男（7画）：田 + 力。

    部件分区：上田 x 220..780 / y 430..820；下力 x 180..760。
    力之撇上端与田之下缘相接。
    """
    g = Glyph("uni7537", advance=1000, unicode=0x7537, note="男：田+力")
    box(g, 220, 780, 430, 820, W_THIN, W_THIN)           # ①-③ 田外框
    g.vbar(500, 430, 820, W_THIN)                        # ④ 田中竖
    g.hbar(220, 780, 625, W_THIN)                        # ⑤ 田中横
    g.hbar(200, 800, 360, W_SEC)                         # ⑥ 力横（墨 314..406）
    g.vbar(740, 360, 130, W_SEC)                         # ⑦ 力竖
    g.diag(740, 130, 668, 90, W_THIN)                    # ⑧ 钩
    g.diag(420, 450, 180, 60, W_SEC)                     # ⑨ 撇
    return g


def g_shitsu() -> Glyph:
    """私（7画）：禾 + 厶。

    部件分区：左禾 x 60..500；右厶 x 560..940 / y 180..560。
    """
    g = Glyph("uni79C1", advance=1000, unicode=0x79C1, note="私：禾+厶")
    g.diag(430, 765, 180, 700, W_THIN)                   # ① ノ
    g.hbar(90, 480, 660, W_SEC)                          # ② 横
    g.vbar(300, 60, 690, W_MAIN)                         # ③ 竖
    g.diag(300, 630, 110, 180, W_THIN)                   # ④ 撇
    g.diag(310, 630, 500, 150, W_MAIN)                   # ⑤ 捺
    g.diag(780, 540, 620, 200, W_THIN)                   # ⑥ 厶撇
    g.diag(620, 200, 880, 280, W_THIN)                   # ⑦ 厶折
    g.diag(800, 540, 880, 460, W_THIN)                   # ⑧ 厶点
    return g


def g_kaku() -> Glyph:
    """各（6画）：夂 + 口。

    部件分区：上夂 y 420..790；下口 x 300..700 / y 20..380。
    """
    g = Glyph("uni5404", advance=1000, unicode=0x5404, note="各：夂+口")
    g.diag(570, 780, 390, 700, W_THIN)                   # ① ノ
    g.hbar(390, 740, 690, W_SEC)                         # ② 横
    g.diag(740, 690, 430, 490, W_SEC)                    # ③ フ下段
    g.diag(440, 760, 860, 420, W_SEC)                    # ④ 捺
    box(g, 300, 700, 20, 380, W_THIN, W_THIN)             # ⑤-⑦ 口
    return g


def g_shi_hajime() -> Glyph:
    """始（8画）：女 + 台。

    部件分区：左女 x 60..430；右台 x 460..940（上厶 + 下口）。
    """
    g = Glyph("uni59CB", advance=1000, unicode=0x59CB, note="始：女+台")
    g.diag(320, 780, 160, 520, W_THIN)                   # ① 撇
    g.diag(160, 520, 400, 290, W_THIN)                   # ② 撇折（折向右下）
    g.diag(450, 720, 110, 100, W_THIN)                   # ③ 长撇
    g.hbar(70, 440, 250, W_SEC)                          # ④ 横
    g.diag(700, 720, 570, 400, W_THIN)                   # ⑤ 厶撇
    g.diag(570, 400, 800, 480, W_THIN)                   # ⑥ 厶折
    g.diag(800, 670, 880, 590, W_THIN)                   # ⑦ 厶点
    box(g, 520, 900, 40, 380, W_THIN, W_THIN)             # ⑧-⑩ 口
    return g


def g_choku() -> Glyph:
    """直（8画）：十 + 目 + 一。

    部件分区：十 y 580..820；目 x 250..750 / y 214..622（四横两竖，三个腔各 24）；
    最下一横 y 82..178，横贯全字。
    2026-10-31 回修：原「十的横 × 目上横」白口 −8、「目底横 × 最下一横」白口 −40。
    参照 M PLUS 1p Black「直」实测：目部 3 个腔，腔高 34、宽 210。
    """
    g = Glyph("uni76F4", advance=1000, unicode=0x76F4, note="直：十+目+一")
    g.hbar(250, 750, 700, W_MAIN)                        # ① 横（墨 652..748）
    g.vbar(500, 580, 820, W_MAIN)                        # ② 竖
    g.vbar(298, 256, 580, W_THIN)                        # ③ 目左竖
    g.vbar(702, 256, 580, W_THIN)                        # ④ 目右竖
    g.hbar(250, 750, 580, W_THIN)                        # ⑤ 目上横（墨 538..622）
    g.hbar(250, 750, 472, W_THIN)                        # ⑥ 目中横（墨 430..514）
    g.hbar(250, 750, 364, W_THIN)                        # ⑦ 目下横（墨 322..406）
    g.hbar(250, 750, 256, W_THIN)                        # ⑧ 目底横（墨 214..298）
    g.hbar(150, 850, 130, W_MAIN)                        # ⑨ 最下一横（墨 82..178）
    return g


def g_ryou() -> Glyph:
    """両（6画）：一 + 冂 + 中竖 + 两内短竖（Jōyō 通行字形）。

    部件分区：顶横 y 726..818；外框两竖 x 108..892（底端各带短足）；
    中竖 x 454..546（底端带钩）；两内短竖 x 288..372 / 628..712。
    """
    g = Glyph("uni4E21", advance=1000, unicode=0x4E21, note="両：一+冂+内竖+一")
    g.hbar(70, 930, 772, W_SEC)                          # ① 一
    g.vbar(150, 150, 818, W_THIN)                        # ② 左竖
    g.hbar(150, 280, 150, W_THIN)                        # ③ 左足
    g.vbar(850, 150, 818, W_THIN)                        # ④ 右竖
    g.hbar(720, 850, 150, W_THIN)                        # ⑤ 右足
    g.vbar(500, 90, 818, W_SEC)                          # ⑥ 中竖
    g.diag(500, 90, 420, 130, W_THIN)                    # ⑦ 中竖钩
    g.vbar(330, 430, 790, W_THIN)                        # ⑧ 内左短竖
    g.vbar(670, 430, 790, W_THIN)                        # ⑨ 内右短竖
    return g


def g_kaku_kaku() -> Glyph:
    """革（9画）：廿 + 口 + 十。

    部件分区：廿 y 554..800；口 x 330..670 / y 330..522；十 y 40..420。
    2026-10-31 回修：廿的两横白口 −14、廿下横与口上横白口 −12。
    参照 M PLUS 1p Black「革」实测：廿腔 1 个（高 34）、口的腔被十竖劈成 2 个（高 54）。
    """
    g = Glyph("uni9769", advance=1000, unicode=0x9769, note="革：廿+口+十")
    g.hbar(220, 780, 720, W_MAIN)                        # ① 廿上横（墨 672..768）
    g.vbar(330, 800, 600, W_SEC)                         # ② 廿左竖
    g.vbar(670, 800, 600, W_SEC)                         # ③ 廿右竖
    g.hbar(330, 670, 600, W_SEC)                         # ④ 廿下横（墨 554..646）
    g.hbar(330, 670, 480, W_THIN)                        # ⑤ 口上横（墨 438..522）
    g.vbar(376, 372, 480, W_THIN)                        # ⑥ 口左竖
    g.vbar(624, 372, 480, W_THIN)                        # ⑦ 口右竖
    g.hbar(330, 670, 372, W_THIN)                        # ⑧ 口下横（墨 330..414）
    g.hbar(180, 820, 250, W_MAIN)                        # ⑨ 十横（墨 202..298）
    g.vbar(500, 40, 420, W_MAIN)                         # ⑩ 十竖（贯穿口部）
    return g


def g_kai() -> Glyph:
    """価（8画）：亻 + 覀。

    部件分区：左亻 x 60..300；右覀 x 360..940。
    覀＝顶横 + 外框两竖 + 两内短竖 + 底横。
    """
    g = Glyph("uni4FA1", advance=1000, unicode=0x4FA1, note="価：亻+覀")
    part_ninben(g, 60, 300, 820, 0)                      # ①-② 亻
    g.hbar(360, 940, 760, W_MAIN)                        # ③ 顶横
    g.vbar(420, 100, 760, W_SEC)                         # ④ 外左竖
    g.vbar(879, 100, 760, W_SEC)                         # ⑤ 外右竖
    g.vbar(573, 380, 760, W_THIN)                        # ⑥ 内左短竖
    g.vbar(726, 380, 760, W_THIN)                        # ⑦ 内右短竖
    g.hbar(374, 925, 160, W_THIN)                        # ⑧ 底横
    return g


def g_shiki() -> Glyph:
    """式（6画）：弋 + 工。

    部件分区：上弋（长横 + 斜钩 + 点）y 90..800；左工 x 120..540 / y 104..546。
    """
    g = Glyph("uni5F0F", advance=1000, unicode=0x5F0F, note="式：弋+工")
    g.hbar(90, 800, 740, W_MAIN)                         # ① 长横
    g.diag(790, 780, 860, 715, W_DOT)                    # ② 点
    g.diag(700, 780, 880, 130, W_MAIN)                   # ③ 斜钩
    g.diag(880, 130, 810, 90, W_THIN)                    # ④ 钩
    g.hbar(140, 520, 500, W_SEC)                         # ⑤ 工上横
    g.vbar(330, 130, 500, W_MAIN)                        # ⑥ 工竖
    g.hbar(120, 540, 150, W_SEC)                         # ⑦ 工下横
    return g


def g_mura() -> Glyph:
    """村（7画）：木 + 寸。

    部件分区：左木 x 60..460；右寸 x 480..940。
    """
    g = Glyph("uni6751", advance=1000, unicode=0x6751, note="村：木+寸")
    part_wood(g, 60, 460, 800, 0)                        # ①-④ 木
    g.hbar(500, 920, 560, W_MAIN)                        # ⑤ 横
    g.vbar(700, 60, 780, W_MAIN)                         # ⑥ 竖钩
    g.diag(700, 60, 630, 100, W_THIN)                    # ⑦ 钩
    g.diag(590, 460, 640, 380, W_THIN)                   # ⑧ 点
    return g


def g_ka() -> Glyph:
    """果（8画）：田 + 木（竖贯通）。

    部件分区：田 x 220..780 / y 428..814；木横 y 302..398；
    中竖自 820 贯通到 60。
    """
    g = Glyph("uni679C", advance=1000, unicode=0x679C, note="果：田+木")
    g.vbar(268, 440, 820, W_THIN)                        # ① 田左竖
    g.vbar(732, 440, 820, W_THIN)                        # ② 田右竖
    g.hbar(220, 780, 772, W_THIN)                        # ③ 田上横
    g.hbar(220, 780, 470, W_THIN)                        # ④ 田下横
    g.hbar(220, 780, 621, W_THIN)                        # ⑤ 田中横
    g.vbar(500, 60, 820, W_THIN)                         # ⑥ 贯通中竖
    g.hbar(90, 910, 350, W_MAIN)                         # ⑦ 木横
    g.diag(500, 340, 180, 60, W_THIN)                    # ⑧ 撇
    g.diag(500, 340, 830, 60, W_SEC)                     # ⑨ 捺
    return g


def g_nishi() -> Glyph:
    """西（6画）：一 + 冂 + 儿 + 一。

    部件分区：顶横 y 712..808；外框 x 132..868；内儿 x 249..701；底横 y 66..150。
    """
    g = Glyph("uni897F", advance=1000, unicode=0x897F, note="西：一+冂+儿+一")
    g.hbar(60, 940, 760, W_MAIN)                         # ① 一
    g.vbar(180, 60, 760, W_SEC)                          # ② 左竖
    g.vbar(820, 60, 760, W_SEC)                          # ③ 右竖
    g.diag(400, 720, 260, 140, W_THIN)                   # ④ 内撇
    g.vbar(640, 240, 730, W_SEC)                         # ⑤ 内竖弯
    g.diag(640, 240, 740, 200, W_THIN)                   # ⑥ 弯钩
    g.hbar(132, 868, 108, W_THIN)                        # ⑦ 底横
    return g


def g_ou() -> Glyph:
    """応（7画）：广 + 心。

    部件分区：广（点 + 长横 + 撇）占左侧；心 x 330..890 / y 130..430。
    """
    g = Glyph("uni5FDC", advance=1000, unicode=0x5FDC, note="応：广+心")
    g.diag(230, 780, 300, 725, W_DOT)                    # ① 点
    g.hbar(60, 940, 700, W_MAIN)                         # ② 长横
    g.diag(200, 700, 110, 130, W_THIN)                   # ③ 撇
    g.diag(400, 430, 350, 340, W_THIN)                   # ④ 心左点
    g.diag(430, 330, 760, 150, W_MAIN)                   # ⑤ 卧钩
    g.diag(760, 150, 840, 205, W_THIN)                   # ⑥ 钩
    g.diag(560, 410, 610, 335, W_THIN)                   # ⑦ 心中点
    g.diag(820, 420, 880, 335, W_THIN)                   # ⑧ 心右点
    return g


def g_juu() -> Glyph:
    """住（7画）：亻 + 主。

    部件分区：左亻 x 60..330；右主 x 380..940（点 + 三横 + 竖）。
    """
    g = Glyph("uni4F4F", advance=1000, unicode=0x4F4F, note="住：亻+主")
    part_ninben(g, 60, 330, 820, 0)                      # ①-② 亻
    g.diag(640, 780, 710, 725, W_DOT)                    # ③ 点
    g.hbar(400, 900, 690, W_SEC)                         # ④ 横
    g.hbar(440, 860, 520, W_THIN)                        # ⑤ 中横
    g.vbar(650, 120, 700, W_MAIN)                        # ⑥ 竖
    g.hbar(390, 930, 160, W_MAIN)                        # ⑦ 下横
    return g


def g_sou() -> Glyph:
    """争（6画）：⺈ + 彐 + 亅。

    部件分区：⺈ y 620..790；彐 x 300..822 / y 278..642；竖钩 x 472..568。
    """
    g = Glyph("uni4E89", advance=1000, unicode=0x4E89, note="争：⺈+彐+亅")
    g.diag(560, 765, 445, 670, W_THIN)                   # ① ノ（自横左端斜下）
    g.hbar(430, 700, 770, W_THIN)                        # ② 横
    g.diag(700, 770, 640, 650, W_THIN)                   # ③ 钩
    g.hbar(300, 820, 590, W_THIN)                        # ④ 彐上横
    g.hbar(340, 820, 460, W_THIN)                        # ⑤ 彐中横
    g.hbar(300, 820, 330, W_THIN)                        # ⑥ 彐下横
    g.vbar(820, 330, 590, W_THIN)                        # ⑦ 彐右竖
    g.vbar(520, 60, 590, W_MAIN)                         # ⑧ 竖
    g.diag(520, 60, 450, 100, W_THIN)                    # ⑨ 钩
    return g


def g_sai() -> Glyph:
    """再（6画）：一 + 冂 + 中竖 + 两横。

    部件分区：顶横 y 692..788；外框 x 132..868；中竖 x 452..548。
    """
    g = Glyph("uni518D", advance=1000, unicode=0x518D, note="再：一+冂+中竖+两横")
    g.hbar(60, 940, 740, W_MAIN)                         # ① 一
    g.vbar(180, 60, 788, W_MAIN)                         # ② 左竖
    g.vbar(820, 60, 788, W_MAIN)                         # ③ 右竖
    g.vbar(500, 60, 788, W_MAIN)                         # ④ 中竖
    g.hbar(180, 820, 400, W_THIN)                        # ⑤ 中横
    g.hbar(180, 820, 108, W_THIN)                        # ⑥ 底横
    return g


def g_i() -> Glyph:
    """位（7画）：亻 + 立。

    部件分区：左亻 x 60..330；右立 x 380..940（点 + 上横 + 两内笔 + 下横）。
    """
    g = Glyph("uni4F4D", advance=1000, unicode=0x4F4D, note="位：亻+立")
    part_ninben(g, 60, 330, 820, 0)                      # ①-② 亻
    g.diag(620, 780, 690, 725, W_DOT)                    # ③ 点
    g.hbar(420, 900, 700, W_MAIN)                        # ④ 上横
    g.diag(520, 660, 470, 490, W_THIN)                   # ⑤ 内撇
    g.diag(760, 660, 810, 490, W_THIN)                   # ⑥ 内点
    g.hbar(390, 940, 400, W_MAIN)                        # ⑦ 下横
    return g


def g_ki() -> Glyph:
    """企（6画）：人 + 止。

    部件分区：人 y 500..800；止 x 180..820 / y 102..660。
    """
    g = Glyph("uni4F01", advance=1000, unicode=0x4F01, note="企：人+止")
    g.diag(530, 780, 370, 630, W_MAIN)                   # ① 人撇
    g.diag(500, 760, 700, 500, W_MAIN)                   # ② 人捺
    g.vbar(430, 110, 660, W_MAIN)                        # ③ 止竖
    g.hbar(430, 700, 480, W_THIN)                        # ④ 止短横
    g.vbar(250, 180, 480, W_SEC)                         # ⑤ 止左竖
    g.hbar(180, 820, 150, W_MAIN)                        # ⑥ 止底横
    return g


def g_yuu() -> Glyph:
    """有（6画）：一 + 丿 + 月。

    部件分区：上横 y 652..748；丿自横画斜下至左下；月 x 380..800 / y 80..626（两腔各 ≥24）。
    2026-10-31 回修：上横与月上横白口 −54，月部整块糊掉。
    参照 M PLUS 1p Black「有」实测：月部 2 腔，腔高 50、宽 340。
    """
    g = Glyph("uni6709", advance=1000, unicode=0x6709, note="有：一+丿+月")
    g.hbar(80, 900, 700, W_MAIN)                         # ① 一
    g.diag(420, 700, 140, 160, W_MAIN)                   # ② 撇
    g.diag(430, 590, 380, 80, W_SEC)                     # ③ 月左撇
    g.hbar(430, 800, 580, W_SEC)                         # ④ 月上横（墨 534..626）
    g.vbar(752, 80, 580, W_SEC)                          # ⑤ 月右竖
    g.hbar(410, 752, 468, W_THIN)                        # ⑥ 月中横（墨 426..510）
    g.hbar(380, 752, 344, W_SEC)                         # ⑦ 月底横（墨 298..390）
    return g


def g_kyoku() -> Glyph:
    """局（7画）：尸 + 口 + 乚。

    部件分区：尸（顶横 + 右折竖 + 钩）x 806..930；尸下横兼口上横 y 518..602；
    口 x 284..776 / y 160..560；左撇 x 110..260。
    """
    g = Glyph("uni5C40", advance=1000, unicode=0x5C40, note="局：尸+口+乚")
    g.hbar(80, 900, 740, W_MAIN)                         # ① 顶横
    g.vbar(852, 60, 740, W_SEC)                          # ② 右折竖
    g.diag(852, 60, 910, 100, W_THIN)                    # ③ 钩
    g.hbar(200, 892, 560, W_THIN)                        # ④ 尸下横（口上横）
    g.diag(260, 560, 110, 140, W_THIN)                   # ⑤ 尸撇
    g.vbar(330, 160, 560, W_SEC)                         # ⑥ 口左竖
    g.vbar(730, 160, 560, W_SEC)                         # ⑦ 口右竖
    g.hbar(284, 776, 206, W_SEC)                         # ⑧ 口底横
    return g


def g_hou() -> Glyph:
    """放（8画）：方 + 攵。

    部件分区：左方 x 60..470（点 + 长横 + フ + 撇）；右攵 x 500..940。
    """
    g = Glyph("uni653E", advance=1000, unicode=0x653E, note="放：方+攵")
    g.diag(230, 770, 290, 715, W_DOT)                    # ① 点
    g.hbar(90, 460, 690, W_MAIN)                         # ② 长横
    g.hbar(180, 400, 560, W_SEC)                         # ③ フ上段
    g.vbar(352, 300, 560, W_SEC)                         # ④ フ折竖
    g.diag(352, 300, 280, 260, W_THIN)                   # ⑤ 钩
    g.diag(230, 560, 110, 145, W_SEC)                     # ⑥ 撇
    g.diag(860, 760, 700, 710, W_SEC)                    # ⑦ ノ
    g.hbar(620, 920, 660, W_SEC)                         # ⑧ 横
    g.diag(900, 660, 580, 180, W_THIN)                   # ⑨ 撇
    g.diag(660, 660, 890, 170, W_MAIN)                   # ⑩ 捺
    return g


def build() -> list[Glyph]:
    return [
        g_qiu(),
        g_sho(),
        g_ji(),
        g_pin(),
        g_zaku(),
        g_kei(),
        g_shi(),
        g_kan(),
        g_kei_kei(),
        g_tou(),
        g_hen(),
        g_dan(),
        g_shitsu(),
        g_kaku(),
        g_shi_hajime(),
        g_choku(),
        g_ryou(),
        g_kaku_kaku(),
        g_kai(),
        g_shiki(),
        g_mura(),
        g_ka(),
        g_nishi(),
        g_ou(),
        g_juu(),
        g_sou(),
        g_sai(),
        g_i(),
        g_ki(),
        g_yuu(),
        g_kyoku(),
        g_hou(),
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-004.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
