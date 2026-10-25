"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-010。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

设计基线（与繁体汉字完全一致，便于中英日混排）：
- UPM 1000，advance = 1000，字面框 x 60..940 / y 0..820。
- 笔画权重四档：主 96 / 次 92 / 细 84 / 点 84（与 zh-HK 繁体同档）。
- 横画中心线内缩半个笔画宽，使墨迹上缘对齐 820 / 下缘对齐 0；
  竖画端点即墨迹端点（见 vhook / frame 辅助函数）。

同批观感统一的做法（docs/03 GLY-004）：
- 同一部件（扌、刂、氵、囗、口、日、月）在本批内复用同一套坐标与笔画拆法，
  只有随右部件宽度做的光学缩放，不做逐字机械挤压（docs/02 偏差 D）。
- 点与短撇一律用斜切平行四边形（g.dot），slant 固定三档：
  常规点 26 / 次级点 20 / 短撇 14（反向短撇 -14），同类部件同族同档。
- 结构性封闭的字（囗 / 皿 / 日 / 目 / 曲）墨量率必然偏厚，属集成方已裁定允许项，
  不为压阈值把字压畸形。

每字 docstring 写明笔画清单与部件分区坐标，注释标注所属部件。
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

# 字面框（与繁体汉字一致）
X_L, X_R = 60, 940
Y_B, Y_T = 0, 820

# 斜切档位（只许用于点 / 短撇 / 记号，GLY-003）
SLANT_DOT = 26       # 常规点
SLANT_DOT2 = 20      # 次级点
SLANT_SHORT = 14     # 短撇
SLANT_BACK = -14     # 反向短撇


# --------------------------------------------------------------------------
# 通用辅助
# --------------------------------------------------------------------------
def hbar_top(g, x1, x2, w=W_MAIN):
    """上缘对齐 820 的横画：中心线内缩半个笔画宽。"""
    g.hbar(x1, x2, Y_T - w / 2.0, w)


def hbar_base(g, x1, x2, w=W_MAIN):
    """下缘对齐 0 的横画。"""
    g.hbar(x1, x2, w / 2.0, w)


def frame(g, x1, x2, yb, yt, w=W_MAIN):
    """闭合矩形（口 / 囗 的框）：左右竖中心线在 x1 / x2，横画墨迹上缘 yt、下缘 yb。"""
    g.vbar(x1, yb, yt, w)
    g.vbar(x2, yb, yt, w)
    g.hbar(x1, x2, yt - w / 2.0, w)
    g.hbar(x1, x2, yb + w / 2.0, w)


def vhook(g, x, y_bot, y_top, w=W_MAIN, reach=95, hw=84, tick=70):
    """竖钩：竖画 + 末端向左横折 + 微上翘（亅 / 乚 的方切写法）。"""
    g.vbar(x, y_bot, y_top, w)
    g.hbar(x - reach, x, y_bot, hw)
    g.vbar(x - reach, y_bot, y_bot + tick, hw)


def radical_tehen(g, w=W_MAIN):
    """扌（三画）：一 + 竖钩 + 提。本批批内统一坐标。"""
    g.hbar(70, 400, 560, w)
    vhook(g, 235, 200, 810, w, reach=95, hw=W_THIN, tick=80)
    g.diag(120, 340, 330, 440, W_THIN)


def radical_ritou(g, x=810, w=W_MAIN):
    """刂（两画）：短竖 + 长竖钩。"""
    g.vbar(x - 130, 200, 560, W_THIN)
    vhook(g, x, 60, 800, w, reach=100, hw=W_THIN, tick=70)


def radical_sanzui(g):
    """氵（三画）：两点 + 提。"""
    g.dot(230, 690, 88, 110, SLANT_DOT)
    g.dot(165, 470, 88, 110, SLANT_DOT)
    g.diag(115, 230, 355, 340, W_THIN)


def radical_hitsuji(g, cx=500, y=700, w=W_MAIN):
    """禾字头（5 画中的 4 画：短撇 + 一 + 丨 + 丿 + ㇏）。"""
    g.diag(cx + 110, y + 90, cx - 100, y, W_THIN)
    g.hbar(cx - 250, cx + 280, y, w)
    g.vbar(cx, y + 48, y - 220, w)
    g.diag(cx, y - 80, cx - 250, y - 220, W_SEC)
    g.diag(cx, y - 80, cx + 270, y - 220, W_SEC)


def radical_kata(g):
    """片（4 画）：丿（竖 + 末端左撇）+ 一 + 丨 + 一（底横）。

    参照 M PLUS 1p Black / Noto Sans JP 的日本字形：左竖贯通全高并在
    末端向左撇出；中部横画向右伸出后折下成竖；底部有横画封口。
    批内统一坐标（版 / 坂 共用），右部件只做光学让位。
    """
    g.vbar(200, 60, 820, W_MAIN)          # ① 丿 竖（贯通）
    g.diag(200, 130, 110, 30, W_MAIN)     # ①′ 丿 末端左撇
    g.hbar(130, 380, 526, W_MAIN)         # ② 一（墨迹 478..574，向左出头）
    g.vbar(380, 60, 526, W_SEC)           # ③ 丨
    g.hbar(190, 380, 60, W_SEC)           # ④ 一（底横，墨迹 14..106）
    return g


def radical_han(g):
    """反（4 画）：短丿 + 一 + 长丿 + 又（㇇ + ㇏）。批内统一坐标（版 / 坂 共用）。"""
    g.diag(540, 790, 480, 660, W_THIN)    # ① 短丿
    g.hbar(480, 890, 700, W_SEC)          # ② 一（墨迹 654..746）
    g.diag(530, 690, 505, 110, W_SEC)     # ③ 长丿
    g.hbar(620, 850, 520, W_THIN)         # ④ 又 ㇇ 横
    g.diag(850, 520, 640, 90, W_THIN)     # ④′ 又 ㇇ 斜
    g.diag(630, 320, 870, 60, W_SEC)      # ⑤ 又 ㇏ 捺
    return g


# --------------------------------------------------------------------------
# 单字
# --------------------------------------------------------------------------
def g_yan() -> Glyph:
    """岩 U+5CA9 —— ⿱山石（8画）。

    上「山」(墨迹 y 474..820)：中心竖 x500、左右竖 x320/x680、底横。
    下「石」(墨迹 y 0..440)：一(344..440) + 丿 + 口(0..306)。
    """
    g = Glyph("uni5CA9", advance=1000, unicode=0x5CA9,
              note="岩：⿱山石；山居上，石居下")
    # —— 上部 山 ——
    g.vbar(500, 474, 820, W_MAIN)        # ① 中心竖（最高）
    g.vbar(320, 474, 750, W_SEC)         # ② 左竖
    g.vbar(680, 474, 730, W_SEC)         # ③ 右竖
    g.hbar(320, 680, 520, W_SEC)         # ③′ 底横（墨迹 474..566，与三竖平齐）
    # —— 下部 石 ——
    g.hbar(130, 800, 392, W_MAIN)        # ① 一（墨迹 344..440）
    g.diag(330, 430, 180, 70, W_SEC)     # ② 丿（自一左端斜下）
    g.vbar(460, 0, 306, W_MAIN)          # ③ 口 左竖
    g.vbar(800, 0, 306, W_MAIN)          # ④ 口 右竖
    g.hbar(460, 800, 258, W_MAIN)        # ④′ 口 上横（墨迹 210..306）
    g.hbar(460, 800, 46, W_MAIN)         # ⑤ 口 下横（墨迹 0..92）
    return g


def g_ya() -> Glyph:
    """押 U+62BC —— ⿰扌甲（8画）。

    左「扌」(x 70..400)：一(512..608) + 竖钩(200..810) + 提(340..440)。
    右「甲」(x 472..938)：外框(332..818) + 中横(528..624) + 中竖下探至 0。
    """
    g = Glyph("uni62BC", advance=1000, unicode=0x62BC,
              note="押：⿰扌甲")
    radical_tehen(g)
    # —— 右部 甲 ——
    g.vbar(520, 380, 820, W_MAIN)        # ① 左竖
    g.vbar(890, 380, 820, W_MAIN)        # ② 右竖
    g.hbar(520, 890, 772, W_MAIN)        # ②′ 上横（墨迹 724..820）
    g.hbar(520, 890, 576, W_MAIN)        # ③ 中横（墨迹 528..624）
    g.hbar(520, 890, 380, W_MAIN)        # ④ 下横（墨迹 332..428）
    g.vbar(720, 0, 772, W_MAIN)          # ⑤ 中竖（下探出框）
    return g


def g_ban() -> Glyph:
    """版 U+7248 —— ⿰片反（8画）。

    左「片」(x 60..426)：丿（竖 + 末端左撇）+ 一 + 丨 + 底横。
    右「反」(x 434..936)：短丿 + 一 + 长丿 + 又（㇇ + ㇏）。
    """
    g = Glyph("uni7248", advance=1000, unicode=0x7248,
              note="版：⿰片反")
    radical_kata(g)
    radical_han(g)
    return g


def g_ro() -> Glyph:
    """老 U+8001 —— ⿸耂匕（6画）。

    「耂」居左上（墨迹 y 532..820）：一 + 丨 + 一 + 长丿（扫至左下）。
    「匕」居右下（墨迹 y 14..330）：短丿 + 竖弯钩（乚）。
    """
    g = Glyph("uni8001", advance=1000, unicode=0x8001,
              note="老：⿸耂匕")
    # —— 耂（左上包围） ——
    g.hbar(330, 700, 772, W_MAIN)        # ① 一（墨迹 724..820）
    g.vbar(500, 580, 772, W_MAIN)        # ② 丨
    g.hbar(240, 780, 580, W_MAIN)        # ③ 一（墨迹 532..628）
    g.diag(760, 760, 150, 60, W_SEC)     # ④ 长丿（自右上扫至左下）
    # —— 匕（右下） ——
    g.diag(560, 330, 400, 230, W_THIN)   # ⑤ 短丿
    g.vbar(500, 60, 330, W_SEC)          # ⑥ 乚 竖
    g.hbar(500, 800, 60, W_SEC)          # ⑥′ 乚 底横（墨迹 14..106）
    g.vbar(800, 60, 150, W_THIN)         # ⑥″ 乚 上翘
    return g


def g_kaku() -> Glyph:
    """角 U+89D2 —— ⿱⺈用（7画）。

    上「⺈」(墨迹 y 537..807)：丿 + ㇇（横撇）。
    下「用」(墨迹 y 0..598)：丿(左) + 横折钩(上右) + 两横 + 中竖。
    """
    g = Glyph("uni89D2", advance=1000, unicode=0x89D2,
              note="角：⿱⺈用")
    # —— 上部 ⺈ ——
    g.diag(460, 780, 370, 670, W_THIN)   # ① 丿
    g.hbar(370, 580, 670, W_SEC)         # ② ㇇ 横（墨迹 628..712）
    g.diag(580, 670, 480, 580, W_SEC)    # ②′ ㇇ 斜
    # —— 下部 用 ——
    g.diag(320, 600, 285, 60, W_SEC)     # ① 丿（左微斜）
    g.vbar(760, 60, 600, W_SEC)          # ② 横折钩 竖
    g.hbar(300, 760, 552, W_SEC)         # ②′ 横折钩 横（墨迹 506..598）
    g.hbar(300, 760, 108, W_SEC)         # ②″ 折钩向左
    g.hbar(300, 760, 400, W_SEC)         # ③ 一（墨迹 354..446）
    g.hbar(300, 760, 250, W_SEC)         # ④ 一（墨迹 204..296）
    g.vbar(530, 0, 598, W_MAIN)          # ⑤ 中竖
    return g


def g_fu() -> Glyph:
    """房 U+623F —— ⿸户方（8画）。

    上左「户」(墨迹 y 15..805)：丶 + 𠃍 + 一 + 长丿。
    下右「方」(墨迹 y 0..505)：丶 + 一 + 横折钩 + 丿。
    """
    g = Glyph("uni623F", advance=1000, unicode=0x623F,
              note="房：⿸户方")
    # —— 户 ——
    g.dot(480, 750, 92, 110, SLANT_DOT)  # ① 丶
    g.hbar(340, 700, 690, W_MAIN)        # ② 𠃍 横（墨迹 642..738）
    g.vbar(700, 480, 690, W_MAIN)        # ②′ 𠃍 竖
    g.hbar(280, 700, 520, W_MAIN)        # ③ 一（墨迹 472..568，向左伸出）
    g.diag(330, 500, 190, 120, W_SEC)    # ④ 长丿
    # —— 方 ——
    g.dot(560, 460, 84, 110, SLANT_DOT)  # ① 丶
    g.hbar(420, 880, 400, W_MAIN)        # ② 一（墨迹 352..448）
    g.hbar(520, 800, 240, W_MAIN)        # ③ 横折钩 横（墨迹 192..288）
    g.vbar(800, 240, 60, W_MAIN)         # ③′ 竖
    g.hbar(690, 800, 108, W_THIN)        # ③″ 钩向左
    g.vbar(690, 108, 180, W_THIN)        # ③‴ 钩上翘
    g.diag(590, 350, 430, 40, W_SEC)     # ④ 丿
    return g


def g_kyoku() -> Glyph:
    """曲 U+66F2（6画）：外框 + 中横 + 两根上出竖。

    外框 x 144..916 / y 0..618；中横（墨迹 334..426）；
    两根内竖 x430 / x630 自 0 上探至 800（高出上横 182）。
    """
    g = Glyph("uni66F2", advance=1000, unicode=0x66F2,
              note="曲：外框 + 中横 + 两上出竖")
    g.vbar(190, 0, 620, W_SEC)           # ① 左竖
    g.vbar(870, 0, 620, W_SEC)           # ② 横折 竖
    g.hbar(190, 870, 572, W_SEC)         # ②′ 横（墨迹 526..618）
    g.hbar(190, 870, 380, W_SEC)         # ③ 中横（墨迹 334..426）
    g.hbar(190, 870, 46, W_SEC)          # ④ 下横（墨迹 0..92）
    g.vbar(430, 0, 800, W_SEC)           # ⑤ 内竖（上出）
    g.vbar(630, 0, 800, W_SEC)           # ⑥ 内竖（上出）
    return g


def g_saku() -> Glyph:
    """削 U+524A —— ⿰肖刂（9画）。

    左「肖」(x 110..548)：⺌（丨 + 两点）+ 月（下框开底 + 两横）。
    右「刂」(x 658..878)：短竖 + 长竖钩。
    """
    g = Glyph("uni524A", advance=1000, unicode=0x524A,
              note="削：⿰肖刂")
    # —— 肖 ——
    g.vbar(310, 640, 800, W_THIN)        # ⺌ 中竖
    g.dot(150, 730, 84, 100, SLANT_BACK)  # ⺌ 左短撇
    g.dot(470, 730, 84, 100, SLANT_DOT)  # ⺌ 右点
    g.diag(230, 620, 195, 60, W_SEC)     # 月 左丿
    g.hbar(230, 500, 572, W_SEC)         # 月 上横（墨迹 526..618）
    g.vbar(500, 60, 572, W_SEC)          # 月 横折钩 竖
    g.hbar(410, 500, 108, W_THIN)        # 月 钩向左
    g.hbar(230, 500, 400, W_THIN)        # 月 一（墨迹 358..442）
    g.hbar(230, 500, 220, W_THIN)        # 月 一（墨迹 178..262）
    # —— 刂 ——
    radical_ritou(g, x=830, w=W_MAIN)
    return g


def g_shi() -> Glyph:
    """志 U+5FD7 —— ⿱士心（7画）。

    上「士」(墨迹 y 472..820)：长一 + 丨 + 短一。
    下「心」(墨迹 y 0..385)：左点 + 卧钩 + 中点 + 右点。
    """
    g = Glyph("uni5FD7", advance=1000, unicode=0x5FD7,
              note="志：⿱士心")
    # —— 士 ——
    g.hbar(230, 770, 772, W_MAIN)        # ① 一（墨迹 724..820）
    g.vbar(500, 520, 772, W_MAIN)        # ② 丨
    g.hbar(290, 710, 520, W_MAIN)        # ③ 一（墨迹 472..568）
    # —— 心 ——
    g.dot(250, 290, 96, 124, SLANT_DOT)  # ① 左点
    g.dot(450, 320, 96, 124, SLANT_DOT)  # ② 中点
    g.dot(775, 290, 96, 124, SLANT_DOT)  # ③ 右点
    g.hbar(320, 680, 48, W_MAIN)         # ④ 卧钩 横（墨迹 0..96）
    g.vbar(680, 48, 200, W_THIN)         # ④′ 卧钩 上翘
    return g


def g_shou() -> Glyph:
    """昇 U+6607 —— ⿱日升（8画）。

    上「日」(墨迹 y 480..818)：框 + 中横。
    下「升」(墨迹 y 0..462)：短丿 + 一 + 长丿 + 丨。
    """
    g = Glyph("uni6607", advance=1000, unicode=0x6607,
              note="昇：⿱日升")
    # —— 日 ——
    g.vbar(300, 480, 820, W_SEC)         # ① 左竖
    g.vbar(700, 480, 820, W_SEC)         # ② 横折 竖
    g.hbar(300, 700, 772, W_SEC)         # ②′ 上横（墨迹 726..818）
    g.hbar(300, 700, 650, W_SEC)         # ③ 中横（墨迹 604..696）
    g.hbar(300, 700, 526, W_SEC)         # ④ 下横（墨迹 480..572）
    # —— 升 ——
    g.diag(300, 462, 235, 385, W_THIN)   # ① 短丿
    g.hbar(210, 800, 380, W_MAIN)        # ② 一（墨迹 332..428）
    g.diag(360, 380, 150, 30, W_SEC)     # ③ 长丿
    g.vbar(760, 0, 470, W_MAIN)          # ④ 丨
    return g


def g_ike() -> Glyph:
    """池 U+6C60 —— ⿰氵也（6画）。

    左「氵」(x 78..400)：两点 + 提。
    右「也」(x 428..922)：横折钩 + 中竖 + 竖弯钩。
    """
    g = Glyph("uni6C60", advance=1000, unicode=0x6C60,
              note="池：⿰氵也")
    radical_sanzui(g)
    # —— 也 ——
    g.diag(470, 760, 400, 660, W_THIN)   # ① 短丿（横折钩的起笔）
    g.hbar(440, 880, 700, W_SEC)         # ①′ 横（墨迹 654..746）
    g.vbar(880, 480, 700, W_SEC)         # ①″ 竖
    g.hbar(790, 880, 480, W_THIN)        # ①‴ 钩向左
    g.vbar(620, 120, 746, W_MAIN)        # ② 中竖
    g.vbar(470, 330, 46, W_SEC)          # ③ 竖弯钩 竖
    g.hbar(470, 790, 46, W_SEC)          # ③′ 竖弯钩 横（墨迹 0..92）
    g.vbar(790, 46, 160, W_THIN)         # ③″ 上翘
    return g


def g_ga() -> Glyph:
    """我 U+6211 —— ⿿扌戈（7画）。

    左「扌」(窄，x 78..372)：一 + 竖钩 + 提。
    右「戈」(x 440..926)：一 + 斜钩 + 撇 + 点。
    """
    g = Glyph("uni6211", advance=1000, unicode=0x6211,
              note="我：⿿扌戈")
    # —— 扌（因右部戈宽，扌做光学缩窄）——
    g.hbar(78, 330, 560, W_MAIN)         # ① 一（墨迹 512..608）
    vhook(g, 220, 200, 800, W_MAIN, reach=90, hw=W_THIN, tick=80)
    g.diag(110, 330, 320, 430, W_THIN)   # ③ 提
    # —— 戈 ——
    g.hbar(430, 880, 640, W_SEC)         # ① 一（墨迹 594..686）
    g.diag(560, 700, 830, 130, W_MAIN)   # ② 斜钩
    g.vbar(840, 80, 190, W_THIN)         # ②′ 斜钩 上挑
    g.diag(790, 620, 480, 60, W_SEC)     # ③ 撇
    g.dot(855, 760, 84, 100, SLANT_DOT)  # ④ 点
    return g


def g_nari() -> Glyph:
    """為 U+70BA（9画）：丶 + 丿 + 横折×3 + 灬四点。

    参照 M PLUS 1p Black / Noto Sans JP 的日本字形：
    ① 丶 在左上；② 长丿 自上方向左下扫过横画；
    ③④⑤ 三折（横 + 竖）在右侧组成阶梯；
    ⑥-⑨ 灬 四点排在底部。
    """
    g = Glyph("uni70BA", advance=1000, unicode=0x70BA,
              note="為：丶 + 丿 + 横折×3 + 灬")
    g.dot(300, 770, 96, 116, SLANT_DOT)  # ① 丶
    g.diag(470, 800, 130, 170, W_SEC)    # ② 长丿
    g.hbar(280, 840, 700, W_SEC)         # ③ 横折 横（墨迹 654..746）
    g.vbar(840, 560, 700, W_SEC)         # ③′ 横折 竖
    g.hbar(420, 840, 560, W_SEC)         # ④ 横折 横（墨迹 514..606）
    g.vbar(840, 430, 560, W_SEC)         # ④′ 横折 竖
    g.hbar(520, 840, 430, W_SEC)         # ⑤ 横折 横（墨迹 384..476）
    g.vbar(840, 300, 430, W_SEC)         # ⑤′ 横折 竖
    g.dot(250, 140, 96, 116, SLANT_DOT)  # ⑥ 灬
    g.dot(390, 110, 96, 116, SLANT_DOT)  # ⑦
    g.dot(520, 110, 96, 116, SLANT_DOT)  # ⑧
    g.dot(650, 140, 96, 116, SLANT_DOT)  # ⑨
    return g


def g_ketsu() -> Glyph:
    """血 U+8840（6画）：上短丿 + 皿（框 + 两内竖）。

    皿外框 x 174..866 / y 0..640；内竖 x420 / x620。
    """
    g = Glyph("uni8840", advance=1000, unicode=0x8840,
              note="血：丿 + 皿")
    g.diag(470, 790, 330, 600, W_THIN)   # ① 丿
    g.vbar(220, 0, 640, W_SEC)           # ② 皿 左竖
    g.vbar(820, 0, 640, W_SEC)           # ③ 皿 横折 竖
    g.hbar(220, 820, 594, W_SEC)         # ③′ 上横（墨迹 548..640）
    g.vbar(420, 46, 594, W_THIN)         # ④ 内竖
    g.vbar(620, 46, 594, W_THIN)         # ⑤ 内竖
    g.hbar(220, 820, 46, W_SEC)          # ⑥ 下横（墨迹 0..92）
    return g


def g_yoku() -> Glyph:
    """抑 U+6291 —— ⿰扌卬（7画）。

    左「扌」(x 70..448)。右「卬」(x 406..926)：短丿 + 丨 + 提 + 卩。
    """
    g = Glyph("uni6291", advance=1000, unicode=0x6291,
              note="抑：⿰扌卬")
    radical_tehen(g)
    # —— 卬 ——
    g.diag(530, 800, 450, 700, W_THIN)   # ① 短丿
    g.vbar(470, 100, 700, W_SEC)         # ② 丨
    g.diag(470, 100, 580, 175, W_THIN)   # ③ 提
    g.hbar(700, 880, 700, W_SEC)         # ④ 卩 上横（墨迹 654..746）
    g.vbar(880, 480, 700, W_SEC)         # ④′ 卩 竖
    g.hbar(790, 880, 480, W_THIN)        # ④″ 卩 钩向左
    g.vbar(700, 120, 746, W_SEC)         # ④‴ 卩 左长竖
    return g


def g_kyo() -> Glyph:
    """居 U+5C45 —— ⿸尸古（8画）。

    上左「尸」(墨迹 y 522..820)：𠃍 + 一 + 长丿。
    下右「古」(墨迹 y 0..498)：一 + 丨 + 口。
    """
    g = Glyph("uni5C45", advance=1000, unicode=0x5C45,
              note="居：⿸尸古")
    # —— 尸 ——
    g.hbar(280, 680, 772, W_MAIN)        # ① 𠃍 横（墨迹 724..820）
    g.vbar(680, 600, 772, W_MAIN)        # ①′ 𠃍 竖
    g.hbar(220, 680, 600, W_MAIN)        # ② 一（墨迹 552..648）
    g.diag(240, 570, 120, 40, W_SEC)     # ③ 长丿
    # —— 古 ——
    g.hbar(420, 900, 450, W_MAIN)        # ① 一（墨迹 402..498）
    g.vbar(660, 330, 450, W_MAIN)        # ② 丨
    g.vbar(540, 0, 330, W_SEC)           # ③ 口 左竖
    g.vbar(860, 0, 330, W_SEC)           # ④ 口 右竖
    g.hbar(540, 860, 284, W_SEC)         # ④′ 口 上横（墨迹 238..330）
    g.hbar(540, 860, 46, W_SEC)          # ⑤ 口 下横（墨迹 0..92）
    return g


def g_some() -> Glyph:
    """染 U+67D3 —— ⿱(氵九)木（9画）。

    上部 y 430..805：氵（两点 + 提）+ 九（丿 + 乙）。
    下部「木」(墨迹 y 0..398)：一 + 丨 + 丿 + ㇏。
    """
    g = Glyph("uni67D3", advance=1000, unicode=0x67D3,
              note="染：⿱氵九木")
    # —— 上部 氵 ——
    g.dot(190, 755, 84, 100, SLANT_DOT)  # ① 点
    g.dot(130, 580, 84, 100, SLANT_DOT)  # ② 点
    g.diag(80, 430, 280, 490, W_THIN)    # ③ 提
    # —— 上部 九 ——
    g.hbar(360, 680, 720, W_SEC)         # ① 乙 横（墨迹 674..766）
    g.vbar(680, 480, 720, W_SEC)         # ①′ 乙 竖
    g.hbar(680, 880, 480, W_THIN)        # ①″ 乙 底横
    g.vbar(880, 480, 620, W_THIN)        # ①‴ 乙 上钩
    g.diag(560, 760, 390, 400, W_SEC)    # ② 丿
    # —— 下部 木 ——
    g.hbar(180, 820, 350, W_MAIN)        # ① 一（墨迹 302..398）
    g.vbar(500, 0, 398, W_MAIN)          # ② 丨
    g.diag(500, 330, 220, 60, W_SEC)     # ③ 丿
    g.diag(500, 330, 800, 60, W_SEC)     # ④ ㇏
    return g


def g_shou2() -> Glyph:
    """招 U+62DB —— ⿰扌召（8画）。

    左「扌」(x 70..448)。右「召」(x 486..926)：刀（横折钩 + 丿）+ 口。
    """
    g = Glyph("uni62DB", advance=1000, unicode=0x62DB,
              note="招：⿰扌召")
    radical_tehen(g)
    # —— 召 ——
    g.hbar(480, 880, 760, W_SEC)         # ① 刀 横折钩 横（墨迹 714..806）
    g.vbar(880, 560, 760, W_SEC)         # ①′ 竖
    g.hbar(790, 880, 560, W_THIN)        # ①″ 钩向左
    g.diag(700, 780, 540, 560, W_SEC)    # ② 刀 丿
    g.vbar(540, 0, 480, W_SEC)           # ③ 口 左竖
    g.vbar(840, 0, 480, W_SEC)           # ④ 口 右竖
    g.hbar(540, 840, 434, W_SEC)         # ④′ 口 上横（墨迹 388..480）
    g.hbar(540, 840, 46, W_SEC)          # ⑤ 口 下横（墨迹 0..92）
    return g


def g_nai() -> Glyph:
    """奈 U+5948 —— ⿱大示（8画）。

    上「大」(墨迹 y 450..788)：一 + 丿 + ㇏。
    下「示」(墨迹 y 0..422)：短一 + 长一 + 丨 + 左丿 + 右丶。
    """
    g = Glyph("uni5948", advance=1000, unicode=0x5948,
              note="奈：⿱大示")
    # —— 大 ——
    g.hbar(250, 750, 740, W_MAIN)        # ① 一（墨迹 692..788）
    g.diag(520, 740, 230, 450, W_SEC)    # ② 丿
    g.diag(520, 740, 810, 450, W_SEC)    # ③ ㇏
    # —— 示 ——
    g.hbar(370, 630, 380, W_THIN)        # ① 短一（墨迹 338..422）
    g.hbar(230, 770, 250, W_MAIN)        # ② 长一（墨迹 202..298）
    g.vbar(500, 60, 298, W_MAIN)         # ③ 丨
    g.diag(400, 150, 290, 20, W_THIN)    # ④ 左丿
    g.diag(590, 160, 700, 20, W_THIN)    # ⑤ 右丶
    return g


def g_ki() -> Glyph:
    """季 U+5B63 —— ⿱禾子（8画）。

    上「禾」(墨迹 y 420..790)：短撇 + 一 + 丨 + 丿 + ㇏。
    下「子」(墨迹 y 60..386)：乛 + 竖钩 + 一。
    """
    g = Glyph("uni5B63", advance=1000, unicode=0x5B63,
              note="季：⿱禾子")
    # —— 禾 ——
    g.diag(610, 790, 400, 700, W_THIN)   # ① 短撇
    g.hbar(250, 780, 700, W_MAIN)        # ② 一（墨迹 652..748）
    g.vbar(500, 420, 748, W_MAIN)        # ③ 丨
    g.diag(500, 600, 260, 440, W_SEC)    # ④ 丿
    g.diag(500, 600, 760, 440, W_SEC)    # ⑤ ㇏
    # —— 子 ——
    g.hbar(330, 700, 340, W_SEC)         # ① 乛 横（墨迹 294..386）
    g.diag(700, 340, 560, 230, W_SEC)    # ①′ 乛 斜
    g.vbar(560, 100, 340, W_MAIN)        # ② 竖钩 竖
    g.hbar(470, 560, 108, W_THIN)        # ②′ 钩向左
    g.vbar(470, 108, 190, W_THIN)        # ②″ 上翘
    g.hbar(300, 720, 200, W_SEC)         # ③ 一（墨迹 154..246）
    return g


def g_kun() -> Glyph:
    """困 U+56F0 —— 囗包木（7画）。

    囗外框 x 62..938 / y 0..820；内「木」墨迹 y 230..566。
    （结构性封闭字，墨量率偏厚属已知允许项。）
    """
    g = Glyph("uni56F0", advance=1000, unicode=0x56F0,
              note="困：囗 + 木")
    g.vbar(110, 0, 820, W_MAIN)          # ① 囗 左竖
    g.hbar(110, 890, 772, W_MAIN)        # ② 囗 横折 横（墨迹 724..820）
    g.vbar(890, 0, 772, W_MAIN)          # ②′ 囗 横折 竖
    g.hbar(110, 890, 48, W_MAIN)         # ③ 囗 下横（墨迹 0..96）
    # —— 内 木 ——
    g.hbar(250, 750, 520, W_SEC)         # ① 一（墨迹 474..566）
    g.vbar(500, 250, 566, W_SEC)         # ② 丨
    g.diag(500, 450, 280, 230, W_THIN)   # ③ 丿
    g.diag(500, 450, 720, 230, W_THIN)   # ④ ㇏
    return g


def g_hoshi() -> Glyph:
    """星 U+661F —— ⿱日生（9画）。

    上「日」(墨迹 y 480..820)：框 + 中横。
    下「生」(墨迹 y 0..446)：丿 + 一 + 一 + 丨 + 一。
    """
    g = Glyph("uni661F", advance=1000, unicode=0x661F,
              note="星：⿱日生")
    # —— 日 ——
    g.vbar(330, 480, 820, W_SEC)         # ① 左竖
    g.vbar(670, 480, 820, W_SEC)         # ② 横折 竖
    g.hbar(330, 670, 773, W_SEC)         # ②′ 上横（墨迹 727..819）
    g.hbar(330, 670, 646, W_SEC)         # ③ 中横（墨迹 600..692）
    g.hbar(330, 670, 526, W_SEC)         # ④ 下横（墨迹 480..572）
    # —— 生 ——
    g.diag(330, 440, 240, 350, W_THIN)   # ① 丿
    g.hbar(300, 760, 400, W_SEC)         # ② 一（墨迹 354..446）
    g.hbar(240, 820, 260, W_SEC)         # ③ 一（墨迹 214..306）
    g.vbar(560, 0, 446, W_MAIN)          # ④ 丨
    g.hbar(180, 880, 48, W_MAIN)         # ⑤ 一（墨迹 0..96）
    return g


def g_taku() -> Glyph:
    """択 U+629E —— ⿰扌尺（7画）。

    左「扌」(x 70..448)。右「尺」(x 384..926)：𠃍 + 一 + 丿 + ㇏。
    """
    g = Glyph("uni629E", advance=1000, unicode=0x629E,
              note="択：⿰扌尺")
    radical_tehen(g)
    # —— 尺 ——
    g.hbar(480, 880, 760, W_SEC)         # ① 𠃍 横（墨迹 714..806）
    g.vbar(880, 560, 760, W_SEC)         # ①′ 𠃍 竖
    g.hbar(420, 880, 580, W_SEC)         # ② 一（墨迹 534..626，向左伸出）
    g.diag(470, 560, 430, 50, W_SEC)     # ③ 丿
    g.diag(620, 560, 880, 50, W_SEC)     # ④ ㇏
    return g


def g_hide() -> Glyph:
    """秀 U+79C0 —— ⿱禾乃（7画）。

    上「禾」(墨迹 y 500..790)：短撇 + 一 + 丨 + 丿 + ㇏。
    下「乃」(墨迹 y 38..422)：横折折折钩 + 丿。
    """
    g = Glyph("uni79C0", advance=1000, unicode=0x79C0,
              note="秀：⿱禾乃")
    # —— 禾 ——
    g.diag(610, 790, 400, 700, W_THIN)   # ① 短撇
    g.hbar(250, 780, 700, W_MAIN)        # ② 一（墨迹 652..748）
    g.vbar(500, 500, 748, W_MAIN)        # ③ 丨
    g.diag(500, 640, 280, 500, W_SEC)    # ④ 丿
    g.diag(500, 640, 740, 500, W_SEC)    # ⑤ ㇏
    # —— 乃 ——
    g.hbar(280, 620, 380, W_THIN)        # ① 横折折折钩 横
    g.vbar(620, 300, 380, W_THIN)        # ①′ 竖
    g.hbar(560, 780, 300, W_THIN)        # ①″ 横
    g.vbar(780, 80, 300, W_THIN)         # ①‴ 竖
    g.hbar(680, 780, 80, W_THIN)         # ①‵ 钩向左
    g.diag(480, 380, 320, 60, W_SEC)     # ② 丿
    return g


def g_kyo2() -> Glyph:
    """拠 U+62E0 —— ⿰扌処（8画）。

    左「扌」(x 70..448)。右「処」(x 388..932)：夂（丿 + ㇇ + ㇏）+ 几（丿 + 乙）。
    """
    g = Glyph("uni62E0", advance=1000, unicode=0x62E0,
              note="拠：⿰扌処")
    radical_tehen(g)
    # —— 処 / 夂（上部左上） ——
    g.diag(580, 810, 480, 700, W_THIN)   # ① 丿
    g.hbar(440, 730, 700, W_THIN)        # ② ㇇ 横（墨迹 658..742）
    g.diag(690, 700, 600, 580, W_THIN)   # ②′ ㇇ 斜
    g.diag(500, 680, 780, 530, W_SEC)    # ③ ㇏
    # —— 処 / 几（右下） ——
    g.hbar(620, 860, 420, W_SEC)         # ④ 乙 横（墨迹 374..466）
    g.vbar(820, 120, 420, W_SEC)         # ④′ 乙 竖（墨迹 774..866）
    g.hbar(820, 896, 120, W_THIN)        # ④″ 乙 底横（墨迹 78..162，右出 30）
    g.vbar(896, 120, 220, W_THIN)        # ④‴ 乙 上钩（墨迹 854..938）
    g.diag(660, 390, 620, 100, W_THIN)   # ⑤ 几 丿
    return g


def g_ka() -> Glyph:
    """香 U+9999 —— ⿱禾日（9画）。

    上「禾」(墨迹 y 480..790)。下「日」(墨迹 y 0..440)：框 + 中横。
    """
    g = Glyph("uni9999", advance=1000, unicode=0x9999,
              note="香：⿱禾日")
    # —— 禾 ——
    g.diag(610, 790, 400, 700, W_THIN)   # ① 短撇
    g.hbar(250, 780, 700, W_MAIN)        # ② 一（墨迹 652..748）
    g.vbar(500, 480, 748, W_MAIN)        # ③ 丨
    g.diag(500, 620, 250, 480, W_SEC)    # ④ 丿
    g.diag(500, 620, 770, 480, W_SEC)    # ⑤ ㇏
    # —— 日 ——
    g.vbar(330, 0, 440, W_SEC)           # ① 左竖
    g.vbar(670, 0, 440, W_SEC)           # ② 横折 竖
    g.hbar(330, 670, 394, W_SEC)         # ②′ 上横（墨迹 348..440）
    g.hbar(330, 670, 260, W_SEC)         # ③ 中横（墨迹 214..306）
    g.hbar(330, 670, 46, W_SEC)          # ④ 下横（墨迹 0..92）
    return g


def g_kou() -> Glyph:
    """更 U+66F4（7画）：一 + ⿻日乂。

    上「一」(墨迹 714..810)；
    中「日」(墨迹 446..686，三横之间留 26 单位内白)；
    下「乂」(丿 / ㇏ 交叉于 510,417，穿过「日」下部——IDS 作 ⿻日乂 相叠)。
    """
    g = Glyph("uni66F4", advance=1000, unicode=0x66F4,
              note="更：一 + ⿻日乂")
    g.hbar(110, 890, 762, W_MAIN)        # ① 一（墨迹 714..810）
    # —— 日 ——
    g.vbar(260, 446, 686, W_SEC)         # ② 丨
    g.vbar(740, 446, 686, W_SEC)         # ③ 横折 竖
    g.hbar(260, 740, 638, W_SEC)         # ③′ 上横（墨迹 590..686）
    g.hbar(260, 740, 614, W_SEC)         # ④ 中横（墨迹 566..662，内白 26）
    g.hbar(260, 740, 494, W_SEC)         # ⑤ 下横（墨迹 446..542，内白 24）
    # —— 乂（与「日」相叠）——
    g.diag(620, 560, 220, 40, W_SEC)     # ⑥ 丿
    g.diag(400, 560, 800, 40, W_SEC)     # ⑦ ㇏
    return g


def g_kyo3() -> Glyph:
    """拒 U+62D2 —— ⿰扌巨（8画）。

    左「扌」(x 70..448)。右「巨」(x 474..936)：一 + 丨 + 一 + 丨 + 一。
    """
    g = Glyph("uni62D2", advance=1000, unicode=0x62D2,
              note="拒：⿰扌巨")
    radical_tehen(g)
    # —— 巨 ——
    g.hbar(520, 890, 740, W_SEC)         # ① 一（墨迹 694..786，最长）
    g.vbar(520, 246, 740, W_SEC)         # ② 丨
    g.hbar(520, 830, 400, W_SEC)         # ③ 一（墨迹 354..446）
    g.vbar(830, 200, 400, W_SEC)         # ④ 丨
    g.hbar(520, 830, 246, W_SEC)         # ⑤ 一（墨迹 200..292）
    return g


def g_kei() -> Glyph:
    """刑 U+5211 —— ⿰开刂（6画）。

    左「开」(x 62..648)：一 + 一 + 丿 + 丨。
    右「刂」(x 618..876)：短竖 + 长竖钩。
    """
    g = Glyph("uni5211", advance=1000, unicode=0x5211,
              note="刑：⿰开刂")
    # —— 开 ——
    g.hbar(180, 520, 740, W_MAIN)        # ① 一（墨迹 692..788）
    g.hbar(80, 600, 560, W_MAIN)         # ② 一（墨迹 512..608）
    g.diag(300, 560, 170, 60, W_SEC)     # ③ 丿
    g.vbar(450, 0, 560, W_MAIN)          # ④ 丨
    # —— 刂 ——
    g.vbar(680, 200, 560, W_THIN)        # ① 短竖
    vhook(g, 830, 60, 800, W_MAIN, reach=100, hw=W_THIN, tick=70)
    return g


def g_saka() -> Glyph:
    """坂 U+5742 —— ⿰土反（7画）。

    左「土」(x 60..436)：一 + 丨 + 一。
    右「反」(x 434..936)：短丿 + 一 + 长丿 + 又（㇇ + ㇏）。
    """
    g = Glyph("uni5742", advance=1000, unicode=0x5742,
              note="坂：⿰土反")
    # —— 土 ——
    g.hbar(90, 390, 620, W_SEC)          # ① 一（墨迹 574..666）
    g.vbar(245, 46, 666, W_SEC)          # ② 丨
    g.hbar(60, 390, 46, W_SEC)           # ③ 一（墨迹 0..92）
    radical_han(g)
    return g


def g_koku() -> Glyph:
    """刻 U+523B —— ⿰亥刂（8画）。

    左「亥」(x 90..490)：丶 + 一 + 丿 + 丿 + 丿 + ㇏。
    右「刂」(x 618..876)：短竖 + 长竖钩。
    """
    g = Glyph("uni523B", advance=1000, unicode=0x523B,
              note="刻：⿰亥刂")
    # —— 亥（⿳亠𠂈人） ——
    g.dot(330, 770, 92, 110, SLANT_DOT)  # ① 丶
    g.hbar(110, 480, 690, W_SEC)         # ② 一（墨迹 644..736）
    g.diag(400, 630, 310, 545, W_THIN)   # ③ 𠂈 上折
    g.diag(350, 545, 260, 460, W_THIN)   # ④ 𠂈 下折
    g.diag(420, 520, 150, 60, W_SEC)     # ⑤ 人 丿
    g.diag(300, 520, 520, 60, W_SEC)     # ⑥ 人 ㇏
    # —— 刂 ——
    g.vbar(660, 200, 560, W_THIN)        # ① 短竖
    vhook(g, 830, 60, 800, W_MAIN, reach=100, hw=W_THIN, tick=70)
    return g


def g_soko() -> Glyph:
    """底 U+5E95 —— ⿸广氐（8画）。

    上左「广」(墨迹 y 5..815)：丶 + 一 + 长丿。
    下右「氐」(墨迹 y 30..600)：丿 + 竖提 + 一 + ㇏ + 丶。
    """
    g = Glyph("uni5E95", advance=1000, unicode=0x5E95,
              note="底：⿸广氐")
    # —— 广 ——
    g.dot(500, 760, 92, 110, SLANT_DOT)  # ① 丶
    g.hbar(180, 900, 680, W_MAIN)        # ② 一（墨迹 632..728）
    g.diag(230, 660, 120, 50, W_SEC)     # ③ 长丿
    # —— 氐 ——
    g.diag(480, 600, 380, 500, W_THIN)   # ① 丿
    g.vbar(430, 100, 580, W_SEC)         # ② 竖提 竖
    g.diag(430, 100, 570, 190, W_THIN)   # ②′ 竖提 挑
    g.hbar(430, 880, 420, W_SEC)         # ③ 一（墨迹 374..466）
    g.diag(480, 420, 860, 60, W_SEC)     # ④ ㇏
    g.vbar(860, 60, 170, W_THIN)         # ④′ ㇏ 上挑
    g.dot(690, 250, 84, 100, SLANT_DOT)  # ⑤ 丶
    return g


def build() -> list[Glyph]:
    return [
        g_yan(),    # 岩 U+5CA9
        g_ya(),     # 押 U+62BC
        g_ban(),    # 版 U+7248
        g_ro(),     # 老 U+8001
        g_kaku(),   # 角 U+89D2
        g_fu(),     # 房 U+623F
        g_kyoku(),  # 曲 U+66F2
        g_saku(),   # 削 U+524A
        g_shi(),    # 志 U+5FD7
        g_shou(),   # 昇 U+6607
        g_ike(),    # 池 U+6C60
        g_ga(),     # 我 U+6211
        g_nari(),   # 為 U+70BA
        g_ketsu(),  # 血 U+8840
        g_yoku(),   # 抑 U+6291
        g_kyo(),    # 居 U+5C45
        g_some(),   # 染 U+67D3
        g_shou2(),  # 招 U+62DB
        g_nai(),    # 奈 U+5948
        g_ki(),     # 季 U+5B63
        g_kun(),    # 困 U+56F0
        g_hoshi(),  # 星 U+661F
        g_taku(),   # 択 U+629E
        g_hide(),   # 秀 U+79C0
        g_kyo2(),   # 拠 U+62E0
        g_ka(),     # 香 U+9999
        g_kou(),    # 更 U+66F4
        g_kyo3(),   # 拒 U+62D2
        g_kei(),    # 刑 U+5211
        g_saka(),   # 坂 U+5742
        g_koku(),   # 刻 U+523B
        g_soko(),   # 底 U+5E95
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-010.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
