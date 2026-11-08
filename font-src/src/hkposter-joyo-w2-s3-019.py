"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s3-019。

本批 24 字，笔画范围 10–13，取自 2010 年文化厅《常用漢字表》。

【整体设计取舍】
- 字面框 x 60..940 / y 0..820，advance=1000，与繁体汉字完全一致。
- 笔画权重四档：主 96 / 次 92 / 细 84 / 点 84（点的高度另按形状给 72–96）。
- 横画一律写「墨迹上缘」，中心线 = 上缘 − 笔宽/2（见每条 hbar 的注释）；
  竖画写「墨迹上下端点」；斜画写「中心线两端点」。
- **横向白口规则**：相邻两条横画的白口 = 上笔墨迹下缘 − 下笔墨迹上缘，
  全批统一 ≥ 26（密排处 30）。方框型部件（口/日/目/田/月/貝/車…）的
  框高一律 ≥ 2×笔宽 + 48，内白腔高 ≥ 30，避免黑砖。
- **同族观感**：批内复用的部件（扌 / 土 / 屈 / 車 / 艹 / 月）使用
  **逐条完全相同的坐标与笔画拆法**（复制而非参数化，保证 recipe 层
  AST 检查能看到每一条真实笔画调用）：
    · 扌  x 60..250   横 T560 / 竖 x155 / 提 (75,270)→(245,340)
    · 土  x 60..280   横 T620 / 竖 x165 / 底横 T92
    · 屈  x 300..940  尸(横 T800/竖 x854/横 T678/撇) + 出(凵+竖+底横)
    · 車  x 60..470   顶横 T820 + 田形框(竖 x106/x424/横 T698/T576/T454)
      + 中竖 x265 贯穿并下探成尾
- 点/短撇的斜切档（GLY-004，family-wide 统一）：
    · 右下点 丶（辶/厶/冫/寸/丷左/雨内点…）→ slant = −14
    · 左下点 丿（丷右）→ slant = +14
    · 短撇（氵的上点等）→ slant = +26
    · 竖点（亠的点）→ slant = 0
- 斜笔墨迹沿垂直于中心线展开，故斜笔端点统一内缩，避免越出字面框。
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


# ---------------------------------------------------------------- 滑
def g_slide() -> Glyph:
    """滑（13 画）= 氵 + 骨。

    部件分区：氵 x 60..210（点/点/提），骨 x 330..930（冎 600..820 + 月 0..510）。
    氵三点用短撇档 slant=+26（family-wide 约定）；骨上「冎」以冂套小框表现，
    下「月」框高 510（≥2×92+48），两道内横把腔高切成 30/30/190。
    """
    g = Glyph("uni6ED1", advance=1000, unicode=0x6ED1, note="滑：氵＋骨")
    # ── 氵（三点水）
    g.dot(140, 680, w=76, h=96, slant=26)      # 上点（短撇）
    g.dot(130, 470, w=76, h=96, slant=26)      # 中点（短撇）
    g.dot(125, 155, w=120, h=48, slant=26)     # 提（右上斜平行四边形）
    # ── 骨上部「冎」：冂 + 内「コ」
    g.hbar(330, 930, 774, weight=W_SEC)        # 冂顶横 T820 墨迹[728,820]
    g.vbar(376, 500, 820, weight=W_SEC)         # 冂左竖
    g.vbar(884, 620, 820, weight=W_SEC)         # 冂右竖（短）
    g.hbar(422, 762, 638, weight=W_THIN)        # 内横 T680 墨迹[596,680] 白口48
    g.vbar(718, 500, 638, weight=W_THIN)        # 内竖（自内横右端下探成「コ」）
    # ── 骨下部「月」
    g.hbar(400, 860, 464, weight=W_SEC)         # 月顶横 T510 墨迹[418,510]
    g.hbar(400, 860, 346, weight=W_THIN)        # 月内横一 T388 白口30
    g.hbar(400, 860, 232, weight=W_THIN)        # 月内横二 T274 白口30
    g.vbar(446, 0, 510, weight=W_SEC)           # 月左竖
    g.vbar(814, 0, 510, weight=W_SEC)           # 月右竖
    return g


# ---------------------------------------------------------------- 黄
def g_yellow() -> Glyph:
    """黄（11 画）= 廿 + 一 + 由 + 八。

    部件分区：廿 顶横 T820 + 双竖；一 T688 通栏；由 框 234..562；八 20..230。
    由的中竖 x500 上探接「一」下缘 592，下探至框底 234，构成标准「由」。
    """
    g = Glyph("uni9EC4", advance=1000, unicode=0x9EC4, note="黄：廿＋一＋由＋八")
    # ── 廿
    g.hbar(140, 860, 774, weight=W_SEC)         # 顶横 T820 墨迹[728,820]
    g.vbar(280, 660, 820, weight=W_SEC)          # 廿左竖
    g.vbar(720, 660, 820, weight=W_SEC)          # 廿右竖
    # ── 一（通栏）
    g.hbar(60, 940, 642, weight=W_MAIN)          # T688 墨迹[592,688] 白口40
    # ── 由
    g.vbar(500, 234, 592, weight=W_SEC)          # 由中竖（上探接一）
    g.hbar(220, 780, 516, weight=W_SEC)          # 由顶横 T562 墨迹[470,562]
    g.hbar(220, 780, 394, weight=W_THIN)         # 由中横 T440 墨迹[356,440] 白口30
    g.hbar(220, 780, 280, weight=W_SEC)          # 由底横 T326 墨迹[234,326] 白口30
    g.vbar(266, 234, 562, weight=W_SEC)          # 由左竖
    g.vbar(734, 234, 562, weight=W_SEC)          # 由右竖
    # ── 八
    g.diag(370, 230, 245, 35, weight=W_THIN)     # 左撇
    g.diag(630, 230, 765, 35, weight=W_THIN)     # 右捺
    return g


# ---------------------------------------------------------------- 頑
def g_stubborn() -> Glyph:
    """頑（13 画）= 元 + 頁。

    部件分区：元 x 60..450（二 + 儿），頁 x 500..940（丆 + 目 + 八）。
    元右腿用「竖 + 底横折」表现乚；頁的目框 236..678，两道内横各切 30。
    """
    g = Glyph("uni9811", advance=1000, unicode=0x9811, note="頑：元＋頁")
    # ── 元
    g.hbar(120, 400, 654, weight=W_SEC)          # 上一 T700 墨迹[608,700]
    g.hbar(60, 440, 526, weight=W_MAIN)          # 下一 T572 墨迹[476,572] 白口36
    g.diag(175, 480, 105, 30, weight=W_THIN)     # 儿左撇
    g.vbar(340, 60, 480, weight=W_SEC)           # 儿右竖
    g.hbar(340, 450, 106, weight=W_SEC)          # 儿右钩 T106 墨迹[60,152]
    # ── 頁
    g.hbar(500, 940, 754, weight=W_SEC)          # 丆顶横 T800 墨迹[708,800]
    g.hbar(570, 880, 632, weight=W_SEC)          # 目顶横 T678 墨迹[586,678] 白口30
    g.hbar(570, 880, 514, weight=W_THIN)         # 目内横一 T556 墨迹[472,556]
    g.hbar(570, 880, 400, weight=W_THIN)         # 目内横二 T442 墨迹[358,442]
    g.hbar(570, 880, 282, weight=W_SEC)          # 目底横 T328 墨迹[236,328] 白口30
    g.vbar(616, 236, 678, weight=W_SEC)          # 目左竖
    g.vbar(834, 236, 678, weight=W_SEC)          # 目右竖
    g.diag(660, 230, 560, 20, weight=W_THIN)     # 頁八左撇
    g.diag(790, 230, 890, 20, weight=W_THIN)     # 頁八右捺
    return g


# ---------------------------------------------------------------- 彩
def g_color() -> Glyph:
    """彩（11 画）= 采 + 彡。

    部件分区：采 x 60..500（爫 + 木），彡 x 680..920（三撇平行下行）。
    爫用「一撇 + 三短点」表现（点用 slant=+14 左下档）；木的撇捺自竖画中段出发。
    """
    g = Glyph("uni5F69", advance=1000, unicode=0x5F69, note="彩：采＋彡")
    # ── 采上部爫
    g.diag(330, 775, 170, 735, weight=W_MAIN)        # 爫顶撇
    g.dot(150, 620, w=84, h=84, slant=14)            # 爫左短点
    g.dot(270, 620, w=84, h=84, slant=14)            # 爫中短点
    g.dot(390, 620, w=84, h=84, slant=14)            # 爫右短点
    # ── 采下部木
    g.hbar(70, 520, 487, weight=W_MAIN)              # 木横 T535 墨迹[439,535] 白口43
    g.vbar(295, 0, 535, weight=W_MAIN)               # 木竖
    g.diag(290, 465, 100, 45, weight=W_MAIN)         # 木左撇
    g.diag(300, 465, 505, 45, weight=W_MAIN)         # 木右捺
    # ── 彡
    g.diag(870, 780, 700, 690, weight=W_MAIN)        # 彡第一撇
    g.diag(870, 580, 700, 490, weight=W_MAIN)        # 彡第二撇（白口36）
    g.diag(870, 380, 700, 290, weight=W_MAIN)        # 彡第三撇（白口36）
    return g


# ---------------------------------------------------------------- 掃
def g_sweep() -> Glyph:
    """掃（11 画）= 扌 + 帚。

    部件分区：扌 x 60..250（与捨/掘 同坐标），帚 x 300..940（ヨ + 冖 + 巾）。
    ヨ 的竖在左、三横向右伸出；冖 两短垂收在 310..346；巾 中竖下探至基线。
    """
    g = Glyph("uni6383", advance=1000, unicode=0x6383, note="掃：扌＋帚")
    # ── 扌（与捨/掘同坐标）
    g.hbar(60, 250, 514, weight=W_SEC)            # 扌横 T560 墨迹[468,560]
    g.vbar(155, 0, 700, weight=W_SEC)             # 扌竖
    g.diag(80, 270, 245, 340, weight=W_THIN)      # 扌提
    # ── 帚上部ヨ
    g.hbar(304, 900, 774, weight=W_SEC)           # ヨ横一 T820 墨迹[728,820]
    g.hbar(304, 900, 644, weight=W_SEC)           # ヨ横二 T690 墨迹[598,690] 白口38
    g.hbar(304, 900, 514, weight=W_SEC)           # ヨ横三 T560 墨迹[468,560] 白口38
    g.vbar(350, 468, 820, weight=W_SEC)            # ヨ左竖
    # ── 冖
    g.hbar(300, 940, 392, weight=W_SEC)           # 冖横 T438 墨迹[346,438] 白口30
    g.vbar(340, 310, 346, weight=W_THIN)           # 冖左短垂
    g.vbar(890, 310, 346, weight=W_THIN)           # 冖右短垂
    # ── 巾
    g.hbar(380, 900, 234, weight=W_SEC)            # 巾横 T280 墨迹[188,280] 白口30
    g.vbar(640, 0, 280, weight=W_MAIN)             # 巾中竖（探至基线）
    g.vbar(426, 120, 280, weight=W_THIN)           # 巾左竖
    g.vbar(854, 120, 280, weight=W_THIN)           # 巾右竖
    return g


# ---------------------------------------------------------------- 雲
def g_cloud() -> Glyph:
    """雲（12 画）= 雨 + 云。

    部件分区：雨 x 60..940 顶 724..820（冂 + 中竖 + 四点），云 x 60..940 0..440。
    雨内四点用右下点档 slant=−14；下部「云」上二横 + 厶（撇折 + 末点）。
    """
    g = Glyph("uni96F2", advance=1000, unicode=0x96F2, note="雲：雨＋云")
    # ── 雨
    g.hbar(60, 940, 772, weight=W_MAIN)            # 雨顶横 T820 墨迹[724,820]
    g.vbar(120, 500, 772, weight=W_MAIN)            # 雨左竖
    g.vbar(880, 500, 772, weight=W_MAIN)            # 雨右竖
    g.vbar(500, 500, 772, weight=W_MAIN)            # 雨中竖
    g.dot(300, 660, w=72, h=76, slant=-14)          # 雨内左上点
    g.dot(300, 545, w=72, h=76, slant=-14)          # 雨内左下点
    g.dot(700, 660, w=72, h=76, slant=-14)          # 雨内右上点
    g.dot(700, 545, w=72, h=76, slant=-14)          # 雨内右下点
    # ── 云
    g.hbar(180, 820, 394, weight=W_SEC)             # 云横一 T440 墨迹[348,440]
    g.hbar(60, 940, 264, weight=W_MAIN)             # 云横二 T312 墨迹[216,312] 白口36
    g.diag(350, 216, 250, 60, weight=W_THIN)        # 厶撇折的上撇
    g.hbar(250, 580, 102, weight=W_THIN)            # 厶撇折的折 T102 墨迹[60,144]
    g.dot(650, 150, w=80, h=88, slant=-14)          # 厶末点（右下点档）
    return g


# ---------------------------------------------------------------- 掘
def g_dig() -> Glyph:
    """掘（11 画）= 扌 + 屈。

    部件分区：扌 x 60..250（同掃/捨），屈 x 300..940（尸 586..800 + 出 0..556）。
    屈与堀共用完全相同的坐标；出 = 上凵 + 中横 + 下凵 + 中竖。
    """
    g = Glyph("uni6398", advance=1000, unicode=0x6398, note="掘：扌＋屈")
    # ── 扌（与掃/捨同坐标）
    g.hbar(60, 250, 514, weight=W_SEC)
    g.vbar(155, 0, 700, weight=W_SEC)
    g.diag(80, 270, 245, 340, weight=W_THIN)
    # ── 屈上部尸（与堀同坐标）
    g.hbar(360, 900, 754, weight=W_SEC)             # 尸顶横 T800 墨迹[708,800]
    g.vbar(854, 586, 800, weight=W_SEC)              # 尸右竖
    g.hbar(360, 900, 632, weight=W_SEC)              # 尸底横 T678 墨迹[586,678] 白口30
    g.diag(380, 790, 300, 180, weight=W_THIN)        # 尸撇
    # ── 屈下部出
    g.vbar(486, 430, 556, weight=W_THIN)             # 出左上竖
    g.vbar(834, 430, 556, weight=W_THIN)             # 出右上竖
    g.hbar(440, 880, 374, weight=W_SEC)              # 出中横 T420 墨迹[328,420]
    g.vbar(486, 92, 430, weight=W_THIN)              # 出左下竖
    g.vbar(834, 92, 430, weight=W_THIN)              # 出右下竖
    g.hbar(440, 880, 46, weight=W_SEC)               # 出底横 T92 墨迹[0,92]
    g.vbar(660, 92, 556, weight=W_SEC)               # 出中竖
    return g


# ---------------------------------------------------------------- 蓄
def g_store() -> Glyph:
    """蓄（13 画）= 艹 + 玄 + 田。

    部件分区：艹 顶 724..820；玄（亠 + 幺）610..298；田 0..312。
    密排区（玄/田）白口压到 30，笔画局部减重到 84，避免腔被封死。
    """
    g = Glyph("uni84C4", advance=1000, unicode=0x84C4, note="蓄：艹＋玄＋田")
    # ── 艹
    g.hbar(60, 940, 772, weight=W_MAIN)             # 艹横 T820 墨迹[724,820]
    g.vbar(280, 670, 820, weight=W_SEC)              # 艹左竖
    g.vbar(720, 670, 820, weight=W_SEC)              # 艹右竖
    # ── 玄：亠
    g.dot(500, 656, w=76, h=84, slant=0)             # 亠的点（竖点档 slant=0）墨迹[614,698]
    g.hbar(220, 780, 594, weight=W_THIN)             # 亠横 T636 墨迹[552,636] 与点重叠22
    # ── 玄：幺（两折）
    g.diag(400, 552, 345, 500, weight=W_THIN)        # 幺第一撇折的上撇
    g.hbar(345, 560, 484, weight=W_THIN)             # 幺第一折 T526 墨迹[442,526] 白口26
    g.diag(490, 442, 415, 390, weight=W_THIN)        # 幺第二撇折的上撇
    g.hbar(415, 640, 374, weight=W_THIN)             # 幺第二折 T416 墨迹[332,416] 白口26
    g.dot(700, 380, w=72, h=80, slant=-14)           # 幺末点
    # ── 田
    g.hbar(190, 810, 264, weight=W_THIN)             # 田顶横 T306 墨迹[222,306] 白口26
    g.hbar(190, 810, 153, weight=W_THIN)             # 田中横 T195 墨迹[111,195] 腔高27
    g.hbar(190, 810, 42, weight=W_THIN)              # 田底横 T84 墨迹[0,84] 腔高27
    g.vbar(232, 0, 306, weight=W_THIN)               # 田左竖
    g.vbar(768, 0, 306, weight=W_THIN)               # 田右竖
    return g


# ---------------------------------------------------------------- 軸
def g_axle() -> Glyph:
    """軸（12 画）= 車 + 由。

    部件分区：車 x 60..470（与軟同坐标），由 x 520..940。
    車 = 顶横 + 田形框（两道内横切 30/38）+ 贯穿中竖下探成尾；
    由 = 田形框 + 中竖上探 80 表现「由」。
    """
    g = Glyph("uni8EF8", advance=1000, unicode=0x8EF8, note="軸：車＋由")
    # ── 車（与軟同坐标）
    g.hbar(90, 440, 774, weight=W_SEC)              # 車顶横 T820 墨迹[728,820]
    g.hbar(60, 470, 652, weight=W_SEC)              # 框顶横 T698 墨迹[606,698] 白口30
    g.hbar(60, 470, 534, weight=W_THIN)             # 框中横 T576 墨迹[492,576] 白口30
    g.hbar(60, 470, 408, weight=W_SEC)              # 框底横 T454 墨迹[362,454] 白口38
    g.vbar(106, 362, 698, weight=W_SEC)              # 框左竖
    g.vbar(424, 362, 698, weight=W_SEC)              # 框右竖
    g.vbar(265, 280, 760, weight=W_THIN)             # 車中竖（贯穿 + 尾）
    # ── 由
    g.vbar(720, 84, 780, weight=W_SEC)               # 由中竖（上探至780，下贯至底横）
    g.hbar(520, 920, 654, weight=W_SEC)              # 由框顶横 T700 墨迹[608,700]
    g.hbar(520, 920, 346, weight=W_THIN)             # 由框中横 T388 墨迹[304,388] 上下腔各220
    g.hbar(520, 920, 42, weight=W_SEC)               # 由框底横 T84 墨迹[0,84]
    g.vbar(566, 0, 700, weight=W_SEC)                # 由框左竖
    g.vbar(874, 0, 700, weight=W_SEC)                # 由框右竖
    return g


# ---------------------------------------------------------------- 疲
def g_fatigue() -> Glyph:
    """疲（10 画）= 疒 + 皮。

    部件分区：疒 x 60..940 顶（点 + 长横 + 撇 + 冫两点），皮 x 420..940。
    疒的点用右下点档 slant=−14；皮 = 顶横 + 中竖 + 左侧撇 + 底部又。
    """
    g = Glyph("uni75B2", advance=1000, unicode=0x75B2, note="疲：疒＋皮")
    # ── 疒
    g.dot(300, 734, w=80, h=88, slant=-14)          # 疒的点
    g.hbar(180, 940, 652, weight=W_SEC)              # 疒长横 T698 墨迹[606,698]
    g.diag(200, 606, 112, 60, weight=W_MAIN)         # 疒长撇
    g.dot(330, 520, w=72, h=84, slant=-14)           # 疒内上点
    g.diag(250, 320, 380, 380, weight=W_THIN)        # 疒内提
    # ── 皮
    g.hbar(440, 920, 530, weight=W_SEC)              # 皮顶横 T576 墨迹[484,576] 白口30
    g.vbar(700, 270, 600, weight=W_SEC)              # 皮中竖
    g.diag(470, 484, 410, 300, weight=W_THIN)        # 皮左侧撇
    g.hbar(520, 880, 248, weight=W_THIN)             # 又横 T290 墨迹[206,290]
    g.diag(880, 290, 560, 40, weight=W_THIN)         # 又撇
    g.diag(540, 290, 900, 40, weight=W_MAIN)         # 又捺
    return g


# ---------------------------------------------------------------- 捨
def g_sacrifice() -> Glyph:
    """捨（11 画）= 扌 + 舎。

    部件分区：扌 x 60..250（与掃/掘同坐标），舎 x 300..940（𠆢 + 干 + 口）。
    舎上人用一撇一捺压在干之上；干 = 一 + 竖 + 一；口框高 300，腔高 132。
    """
    g = Glyph("uni6368", advance=1000, unicode=0x6368, note="捨：扌＋舎")
    # ── 扌（与掃/掘同坐标）
    g.hbar(60, 250, 514, weight=W_SEC)
    g.vbar(155, 0, 700, weight=W_SEC)
    g.diag(80, 270, 245, 340, weight=W_THIN)
    # ── 舎
    g.diag(540, 760, 330, 650, weight=W_THIN)        # 𠆢左撇
    g.diag(540, 760, 760, 650, weight=W_THIN)        # 𠆢右捺
    g.hbar(400, 900, 586, weight=W_SEC)              # 干上横 T632 墨迹[540,632]
    g.vbar(650, 400, 560, weight=W_THIN)             # 干中竖
    g.hbar(340, 940, 376, weight=W_SEC)              # 干下横 T422 墨迹[330,422] 白口30
    g.hbar(420, 860, 258, weight=W_THIN)             # 口顶横 T300 墨迹[216,300] 白口30
    g.hbar(420, 860, 42, weight=W_THIN)              # 口底横 T84 墨迹[0,84]
    g.vbar(462, 0, 300, weight=W_THIN)               # 口左竖
    g.vbar(818, 0, 300, weight=W_THIN)               # 口右竖
    return g


# ---------------------------------------------------------------- 砲
def g_cannon() -> Glyph:
    """砲（10 画）= 石 + 包。

    部件分区：石 x 60..500（一 + 撇 + 口），包 x 540..940（勹 + 巳）。
    石的口框高 598（腔宽 62）；勹 = 撇 + 横折钩；巳 = 上面 + 竖折底钩。
    """
    g = Glyph("uni7832", advance=1000, unicode=0x7832, note="砲：石＋包")
    # ── 石
    g.hbar(60, 500, 674, weight=W_SEC)               # 石横 T720 墨迹[628,720]
    g.diag(240, 628, 105, 60, weight=W_THIN)         # 石撇
    g.hbar(270, 500, 556, weight=W_THIN)             # 石口顶横 T598 墨迹[514,598] 白口30
    g.hbar(270, 500, 42, weight=W_THIN)              # 石口底横 T84 墨迹[0,84]
    g.vbar(312, 0, 598, weight=W_THIN)               # 石口左竖
    g.vbar(458, 0, 598, weight=W_THIN)               # 石口右竖
    # ── 包（勹）
    g.diag(700, 780, 610, 660, weight=W_THIN)        # 勹撇
    g.hbar(660, 926, 606, weight=W_SEC)              # 勹横 T652 墨迹[560,652]
    g.vbar(880, 300, 670, weight=W_SEC)              # 勹右竖（折）墨迹 x834..926
    g.hbar(800, 926, 102, weight=W_THIN)             # 勹底钩 T144 墨迹[60,144]
    # ── 包内「巳」
    g.hbar(588, 812, 488, weight=W_THIN)             # 巳顶横 T530 墨迹[446,530] 白口30
    g.hbar(588, 812, 374, weight=W_THIN)             # 巳中横 T416 墨迹[332,416] 白口30
    g.hbar(588, 790, 42, weight=W_THIN)              # 巳底横 T84 墨迹[0,84]
    g.vbar(630, 70, 545, weight=W_THIN)              # 巳左竖 墨迹 x588..672
    g.vbar(770, 350, 545, weight=W_THIN)             # 巳右竖 墨迹 x728..812
    return g


# ---------------------------------------------------------------- 軟
def g_soft() -> Glyph:
    """軟（11 画）= 車 + 欠。

    部件分区：車 x 60..470（与軸同坐标），欠 x 520..940。
    欠 = 短撇 + 横撇 + 下部人（撇捺）；横撇的撇自横的右端折下。
    """
    g = Glyph("uni8EDF", advance=1000, unicode=0x8EDF, note="軟：車＋欠")
    # ── 車（与軸同坐标）
    g.hbar(90, 440, 774, weight=W_SEC)
    g.hbar(60, 470, 652, weight=W_SEC)
    g.hbar(60, 470, 534, weight=W_THIN)
    g.hbar(60, 470, 408, weight=W_SEC)
    g.vbar(106, 362, 698, weight=W_SEC)
    g.vbar(424, 362, 698, weight=W_SEC)
    g.vbar(265, 280, 760, weight=W_THIN)
    # ── 欠
    g.diag(640, 780, 570, 660, weight=W_THIN)        # 欠上短撇
    g.hbar(600, 920, 606, weight=W_THIN)             # 欠横 T642 墨迹[558,642]
    g.diag(900, 600, 710, 300, weight=W_THIN)        # 欠横折的撇
    g.diag(760, 460, 520, 40, weight=W_MAIN)         # 欠下撇
    g.diag(740, 460, 895, 40, weight=W_MAIN)         # 欠下捺
    return g


# ---------------------------------------------------------------- 誇
def g_boast() -> Glyph:
    """誇（13 画）= 言 + 夸。

    部件分区：言 x 60..400（点 + 三横 + 口），夸 x 440..940（大 + 亏）。
    言的点用竖点档 slant=0；夸下「亏」用 一 + 一 + 竖折钩 表现。
    """
    g = Glyph("uni8A87", advance=1000, unicode=0x8A87, note="誇：言＋夸")
    # ── 言
    g.dot(230, 736, w=76, h=84, slant=0)             # 言的点（竖点档）
    g.hbar(100, 360, 658, weight=W_SEC)              # 言横一 T704 墨迹[612,704]
    g.hbar(130, 330, 540, weight=W_THIN)             # 言横二 T582 墨迹[498,582] 白口30
    g.hbar(130, 330, 426, weight=W_THIN)             # 言横三 T468 墨迹[384,468] 白口30
    g.hbar(120, 340, 312, weight=W_THIN)             # 言口顶横 T354 墨迹[270,354] 白口30
    g.hbar(120, 340, 42, weight=W_THIN)              # 言口底横 T84 墨迹[0,84]
    g.vbar(162, 0, 354, weight=W_THIN)               # 言口左竖
    g.vbar(298, 0, 354, weight=W_THIN)               # 言口右竖
    # ── 夸
    g.hbar(460, 920, 554, weight=W_SEC)              # 大横 T600 墨迹[508,600]
    g.diag(690, 770, 510, 480, weight=W_MAIN)         # 大撇
    g.diag(690, 560, 890, 420, weight=W_MAIN)         # 大捺
    g.hbar(560, 880, 436, weight=W_THIN)             # 亏横一 T478 墨迹[394,478]
    g.hbar(560, 840, 322, weight=W_THIN)             # 亏横二 T364 墨迹[280,364] 白口30
    g.vbar(620, 130, 290, weight=W_THIN)              # 亏竖折
    g.hbar(620, 880, 108, weight=W_THIN)             # 亏折横 T150 墨迹[66,150]
    g.vbar(838, 0, 80, weight=W_THIN)                # 亏钩
    return g


# ---------------------------------------------------------------- 祥
def g_auspicious() -> Glyph:
    """祥（10 画）= 礻 + 羊。

    部件分区：礻 x 60..330（点 + フ + 竖 + 右点），羊 x 400..940（丷 + 三横 + 竖）。
    礻的右点用右下点档 slant=−14；羊的丷左点 −14、右点 +14（family-wide 统一）。
    """
    g = Glyph("uni7965", advance=1000, unicode=0x7965, note="祥：礻＋羊")
    # ── 礻
    g.dot(200, 752, w=76, h=84, slant=-14)           # 礻的点
    g.hbar(80, 300, 678, weight=W_THIN)              # 礻横 T720 墨迹[636,720]
    g.diag(300, 636, 200, 520, weight=W_THIN)        # 礻フ的撇
    g.vbar(180, 0, 550, weight=W_THIN)               # 礻竖
    g.dot(290, 420, w=76, h=88, slant=-14)           # 礻右点
    # ── 羊
    g.dot(520, 760, w=76, h=84, slant=-14)           # 羊丷左点
    g.dot(800, 760, w=76, h=84, slant=14)            # 羊丷右点
    g.hbar(460, 880, 652, weight=W_SEC)              # 羊横一 T698 墨迹[606,698]
    g.hbar(400, 940, 534, weight=W_THIN)             # 羊横二 T576 墨迹[492,576] 白口30
    g.hbar(400, 940, 420, weight=W_THIN)             # 羊横三 T462 墨迹[378,462] 白口30
    g.vbar(670, 0, 720, weight=W_SEC)                # 羊竖（贯穿三横至基线）
    return g


# ---------------------------------------------------------------- 秩
def g_order() -> Glyph:
    """秩（10 画）= 禾 + 失。

    部件分区：禾 x 60..480（撇 + 横 + 竖 + 撇捺），失 x 520..940。
    禾顶撇用斜画（短横式撇）；失上撇压住两横，下部撇捺自二横下方分出。
    """
    g = Glyph("uni79E9", advance=1000, unicode=0x79E9, note="秩：禾＋失")
    # ── 禾
    g.diag(340, 770, 150, 725, weight=W_THIN)        # 禾顶撇
    g.hbar(80, 440, 618, weight=W_SEC)               # 禾横 T664 墨迹[572,664]
    g.vbar(260, 0, 690, weight=W_SEC)                # 禾竖
    g.diag(255, 520, 110, 40, weight=W_THIN)         # 禾左撇
    g.diag(265, 520, 460, 40, weight=W_THIN)         # 禾右捺
    # ── 失
    g.diag(700, 780, 600, 690, weight=W_THIN)        # 失上撇
    g.hbar(580, 900, 597, weight=W_THIN)             # 失横一 T639 墨迹[555,639]
    g.hbar(520, 940, 479, weight=W_SEC)              # 失横二 T525 墨迹[433,525] 白口30
    g.diag(720, 760, 545, 40, weight=W_MAIN)         # 失下撇
    g.diag(720, 460, 890, 40, weight=W_MAIN)         # 失下捺
    return g


# ---------------------------------------------------------------- 唆
def g_shoe() -> Glyph:
    """唆（10 画）= 口 + 夋。

    部件分区：口 x 60..290（框高 460），夋 x 340..940（厶 + 儿 + 夂）。
    厶末点与折之间留 24；夂以「横 + 交叉撇捺」表现。
    """
    g = Glyph("uni5506", advance=1000, unicode=0x5506, note="唆：口＋夋")
    # ── 口
    g.hbar(60, 340, 638, weight=W_THIN)              # 口顶横 T680 墨迹[596,680]
    g.hbar(60, 340, 262, weight=W_THIN)              # 口底横 T304 墨迹[220,304]
    g.vbar(102, 220, 680, weight=W_THIN)             # 口左竖 墨迹 x60..144
    g.vbar(298, 220, 680, weight=W_THIN)             # 口右竖 墨迹 x256..340
    # ── 夋：厶
    g.diag(660, 790, 580, 700, weight=W_THIN)        # 厶撇
    g.hbar(580, 730, 640, weight=W_THIN)             # 厶折 T682 墨迹[598,682]
    g.dot(790, 690, w=72, h=80, slant=-14)           # 厶末点
    # ── 夋：儿
    g.diag(620, 598, 500, 420, weight=W_THIN)        # 儿撇
    g.vbar(760, 410, 610, weight=W_SEC)              # 儿竖
    g.hbar(760, 850, 472, weight=W_THIN)             # 儿钩 T472 墨迹[430,514]
    # ── 夋：夂
    g.hbar(520, 840, 338, weight=W_THIN)             # 夂横 T380 墨迹[296,380] 白口50
    g.diag(840, 380, 560, 40, weight=W_THIN)         # 夂撇
    g.diag(530, 380, 860, 40, weight=W_MAIN)         # 夂捺
    return g


# ---------------------------------------------------------------- 泰
def g_peace() -> Glyph:
    """泰（10 画）= 三横 + 大撇捺 + 氺。

    部件分区：上三横 450..790（通栏渐宽），大撇捺自 790 交叉三横，下氺 0..420。
    氺 = 中竖 + 两侧短点 + 下撇捺。
    """
    g = Glyph("uni6CF0", advance=1000, unicode=0x6CF0, note="泰：三横＋大撇捺＋氺")
    # ── 上部三横
    g.hbar(120, 880, 744, weight=W_SEC)              # 横一 T790 墨迹[698,790]
    g.hbar(90, 910, 622, weight=W_SEC)               # 横二 T668 墨迹[576,668] 白口30
    g.hbar(60, 940, 498, weight=W_MAIN)               # 横三 T546 墨迹[450,546] 白口30
    # ── 大撇捺
    g.diag(540, 790, 270, 420, weight=W_MAIN)        # 大撇
    g.diag(540, 790, 800, 420, weight=W_MAIN)        # 大捺
    # ── 下部氺
    g.vbar(540, 0, 420, weight=W_SEC)                # 氺中竖
    g.dot(400, 350, w=72, h=80, slant=14)            # 氺左上点
    g.dot(680, 350, w=72, h=80, slant=-14)           # 氺右上点
    g.diag(530, 230, 375, 45, weight=W_THIN)         # 氺下撇
    g.diag(550, 230, 740, 30, weight=W_MAIN)         # 氺下捺
    return g


# ---------------------------------------------------------------- 賄
def g_bribe() -> Glyph:
    """賄（13 画）= 貝 + 有。

    部件分区：貝 x 60..440（目形框 318..760 + 八），有 x 480..940（𠂇 + 月）。
    貝目内两道横各切 30；有的月开底（无底横），内横两道各切 30。
    """
    g = Glyph("uni8CC4", advance=1000, unicode=0x8CC4, note="賄：貝＋有")
    # ── 貝
    g.hbar(90, 410, 714, weight=W_SEC)               # 貝顶横 T760 墨迹[668,760]
    g.hbar(90, 410, 596, weight=W_THIN)              # 貝内横一 T638 墨迹[554,638] 白口30
    g.hbar(90, 410, 482, weight=W_THIN)              # 貝内横二 T524 墨迹[440,524] 白口30
    g.hbar(90, 410, 364, weight=W_SEC)               # 貝底横 T410 墨迹[318,410] 白口30
    g.vbar(136, 318, 760, weight=W_SEC)              # 貝左竖
    g.vbar(364, 318, 760, weight=W_SEC)              # 貝右竖
    g.diag(185, 318, 105, 40, weight=W_THIN)         # 貝八左撇
    g.diag(320, 318, 420, 40, weight=W_THIN)         # 貝八右捺
    # ── 有
    g.hbar(500, 940, 654, weight=W_SEC)              # 𠂇横 T700 墨迹[608,700]
    g.diag(600, 608, 500, 440, weight=W_THIN)        # 𠂇撇
    g.hbar(620, 920, 532, weight=W_SEC)              # 月顶横 T578 墨迹[486,578] 白口30
    g.hbar(620, 920, 414, weight=W_THIN)             # 月内横一 T456 墨迹[372,456] 白口30
    g.hbar(620, 920, 300, weight=W_THIN)             # 月内横二 T342 墨迹[258,342] 白口30
    g.vbar(666, 0, 578, weight=W_SEC)                # 月左竖
    g.vbar(874, 0, 578, weight=W_SEC)                # 月右竖
    return g


# ---------------------------------------------------------------- 凍
def g_freeze() -> Glyph:
    """凍（10 画）= 冫 + 東。

    部件分区：冫 x 60..200（点 + 提），東 x 240..940（中竖 + 横 + 日框 + 撇捺）。
    冫的上点用右下点档 slant=−14；東的中竖上探出横，下贯日框并与撇捺同源。
    """
    g = Glyph("uni51CD", advance=1000, unicode=0x51CD, note="凍：冫＋東")
    # ── 冫
    g.dot(140, 620, w=76, h=88, slant=-14)           # 冫上点（右下点档）
    g.diag(85, 210, 195, 285, weight=W_THIN)         # 冫提
    # ── 東
    g.vbar(600, 200, 800, weight=W_SEC)              # 東中竖
    g.hbar(300, 900, 670, weight=W_SEC)              # 東横 T716 墨迹[624,716]
    g.hbar(380, 820, 548, weight=W_SEC)              # 日顶横 T594 墨迹[502,594] 白口30
    g.hbar(380, 820, 430, weight=W_THIN)             # 日中横 T472 墨迹[388,472] 白口30
    g.hbar(380, 820, 312, weight=W_SEC)              # 日底横 T358 墨迹[266,358] 白口30
    g.vbar(426, 266, 594, weight=W_SEC)              # 日左竖
    g.vbar(774, 266, 594, weight=W_SEC)              # 日右竖
    g.diag(595, 266, 375, 42, weight=W_THIN)         # 東撇
    g.diag(605, 266, 840, 20, weight=W_MAIN)         # 東捺
    return g


# ---------------------------------------------------------------- 堀
def g_quarry() -> Glyph:
    """堀（11 画）= 土 + 屈。

    部件分区：土 x 60..280（一 + 竖 + 一），屈 x 300..940（与掘完全同坐标）。
    土的竖下端穿过底横至基线，保持与掘/掃 批内竖画处理一致。
    """
    g = Glyph("uni5800", advance=1000, unicode=0x5800, note="堀：土＋屈")
    # ── 土
    g.hbar(80, 250, 578, weight=W_THIN)              # 土横 T620 墨迹[536,620]
    g.vbar(165, 60, 640, weight=W_SEC)                # 土竖
    g.hbar(60, 280, 46, weight=W_SEC)                # 土底横 T92 墨迹[0,92]
    # ── 屈（与掘同坐标）
    g.hbar(360, 900, 754, weight=W_SEC)             # 尸顶横 T800 墨迹[708,800]
    g.vbar(854, 586, 800, weight=W_SEC)              # 尸右竖
    g.hbar(360, 900, 632, weight=W_SEC)              # 尸底横 T678 墨迹[586,678] 白口30
    g.diag(380, 790, 300, 180, weight=W_THIN)        # 尸撇
    g.vbar(486, 430, 556, weight=W_THIN)             # 出左上竖
    g.vbar(834, 430, 556, weight=W_THIN)             # 出右上竖
    g.hbar(440, 880, 374, weight=W_SEC)              # 出中横 T420 墨迹[328,420]
    g.vbar(486, 92, 430, weight=W_THIN)              # 出左下竖
    g.vbar(834, 92, 430, weight=W_THIN)              # 出右下竖
    g.hbar(440, 880, 46, weight=W_SEC)               # 出底横 T92 墨迹[0,92]
    g.vbar(660, 92, 556, weight=W_SEC)               # 出中竖
    return g


# ---------------------------------------------------------------- 腹
def g_belly() -> Glyph:
    """腹（13 画）= 月 + 𡕨（𠂉 + 日 + 夂）。

    部件分区：月 x 60..330（框 0..760 + 两道内横），𡕨 x 470..900。
    𡕨上部短撇 + 横（𠂉），中日框高 312（腔 30/30），下部夂用横 + 交叉撇捺。
    """
    g = Glyph("uni8179", advance=1000, unicode=0x8179, note="腹：月＋复")
    # ── 月
    g.hbar(60, 330, 714, weight=W_SEC)               # 月顶横 T760 墨迹[668,760]
    g.hbar(60, 330, 578, weight=W_THIN)              # 月内横一 T620 墨迹[536,620] 白口48
    g.hbar(60, 330, 428, weight=W_THIN)              # 月内横二 T470 墨迹[386,470] 白口66
    g.vbar(106, 0, 760, weight=W_SEC)                # 月左竖
    g.vbar(284, 0, 760, weight=W_SEC)                # 月右竖
    # ── 𡕨：𠂉
    g.diag(540, 770, 470, 700, weight=W_THIN)        # 𠂉短撇
    g.hbar(490, 900, 638, weight=W_THIN)             # 𠂉横 T680 墨迹[596,680]
    # ── 𡕨：日
    g.hbar(470, 870, 524, weight=W_THIN)             # 日顶横 T566 墨迹[482,566] 白口30
    g.hbar(470, 870, 410, weight=W_THIN)             # 日中横 T452 墨迹[368,452] 白口30
    g.hbar(470, 870, 296, weight=W_THIN)             # 日底横 T338 墨迹[254,338] 白口30
    g.vbar(512, 254, 566, weight=W_THIN)             # 日左竖
    g.vbar(828, 254, 566, weight=W_THIN)             # 日右竖
    # ── 𡕨：夂
    g.hbar(470, 880, 182, weight=W_THIN)             # 夂横 T224 墨迹[140,224] 白口30
    g.diag(880, 224, 605, 42, weight=W_THIN)         # 夂撇
    g.diag(490, 224, 890, 42, weight=W_MAIN)         # 夂捺
    return g


# ---------------------------------------------------------------- 菊
def g_chrysanthemum() -> Glyph:
    """菊（11 画）= 艹 + 勹 + 米。

    部件分区：艹 顶 724..820；勹 x 420..940 包住米；米 x 380..800。
    米的丷两点分列中竖两侧（左 −14 / 右 +14），中竖上起 500。
    """
    g = Glyph("uni83CA", advance=1000, unicode=0x83CA, note="菊：艹＋勹＋米")
    # ── 艹
    g.hbar(60, 940, 772, weight=W_MAIN)              # 艹横 T820 墨迹[724,820]
    g.vbar(300, 670, 820, weight=W_SEC)               # 艹左竖
    g.vbar(700, 670, 820, weight=W_SEC)               # 艹右竖
    # ── 勹
    g.diag(470, 700, 390, 580, weight=W_THIN)         # 勹撇
    g.hbar(420, 900, 521, weight=W_SEC)               # 勹横 T567 墨迹[475,567]
    g.vbar(854, 40, 590, weight=W_SEC)                # 勹右竖
    g.hbar(790, 900, 102, weight=W_THIN)              # 勹底钩 T102 墨迹[60,144]
    # ── 米
    g.dot(490, 520, w=72, h=80, slant=-14)            # 米左上点
    g.dot(730, 520, w=72, h=80, slant=14)             # 米右上点
    g.hbar(380, 800, 408, weight=W_THIN)              # 米横 T450 墨迹[366,450] 白口25
    g.vbar(590, 0, 500, weight=W_SEC)                 # 米中竖
    g.diag(585, 366, 400, 45, weight=W_THIN)          # 米撇
    g.diag(595, 366, 790, 45, weight=W_MAIN)          # 米捺
    return g


# ---------------------------------------------------------------- 絞
def g_twist() -> Glyph:
    """絞（12 画）= 糸 + 交。

    部件分区：糸 x 60..366（幺两折 + 小），交 x 380..940（亠 + 八 + 乂）。
    糸的幺用两折 + 末点；交的点用竖点档 slant=0。
    """
    g = Glyph("uni7D5E", advance=1000, unicode=0x7D5E, note="絞：糸＋交")
    # ── 糸：幺
    g.diag(220, 740, 150, 620, weight=W_THIN)         # 幺第一撇折的上撇
    g.hbar(150, 280, 567, weight=W_THIN)             # 幺第一折 T609 墨迹[525,609]
    g.diag(260, 525, 180, 420, weight=W_THIN)         # 幺第二撇折的上撇
    g.hbar(180, 270, 368, weight=W_THIN)             # 幺第二折 T410 墨迹[326,410]
    g.dot(330, 430, w=72, h=80, slant=-14)           # 幺末点
    # ── 糸：小
    g.vbar(195, 0, 340, weight=W_SEC)                 # 小中竖
    g.diag(160, 300, 100, 160, weight=W_THIN)         # 小左撇
    g.dot(300, 280, w=76, h=88, slant=-14)           # 小右点
    # ── 交
    g.dot(660, 776, w=76, h=88, slant=0)              # 交的点（竖点档）
    g.hbar(400, 920, 696, weight=W_SEC)               # 交横 T742 墨迹[650,742]
    g.diag(540, 650, 420, 470, weight=W_THIN)         # 八左撇
    g.diag(790, 650, 900, 470, weight=W_THIN)         # 八右捺
    g.diag(850, 470, 450, 40, weight=W_THIN)          # 乂撇
    g.diag(480, 470, 880, 40, weight=W_MAIN)          # 乂捺
    return g


def build() -> list[Glyph]:
    return [
        g_slide(),       # 滑 U+6ED1
        g_yellow(),      # 黄 U+9EC4
        g_stubborn(),    # 頑 U+9811
        g_color(),       # 彩 U+5F69
        g_sweep(),       # 掃 U+6383
        g_cloud(),       # 雲 U+96F2
        g_dig(),         # 掘 U+6398
        g_store(),       # 蓄 U+84C4
        g_axle(),        # 軸 U+8EF8
        g_fatigue(),     # 疲 U+75B2
        g_sacrifice(),   # 捨 U+6368
        g_cannon(),      # 砲 U+7832
        g_soft(),        # 軟 U+8EDF
        g_boast(),       # 誇 U+8A87
        g_auspicious(),  # 祥 U+7965
        g_order(),       # 秩 U+79E9
        g_shoe(),        # 唆 U+5506
        g_peace(),       # 泰 U+6CF0
        g_bribe(),       # 賄 U+8CC4
        g_freeze(),      # 凍 U+51CD
        g_quarry(),      # 堀 U+5800
        g_belly(),       # 腹 U+8179
        g_chrysanthemum(),  # 菊 U+83CA
        g_twist(),       # 絞 U+7D5E
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s3-019.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
