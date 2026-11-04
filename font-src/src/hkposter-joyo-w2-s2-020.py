"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-020。

本批 32 字（U+5351 卑 … U+58F1 壱），取自 2010 年文化庁《常用漢字表》，
笔画 6–9 画，密度接近，按「同族观感」统一处理。

整体取舍
--------
* 字面框：x 60..940，y 0..820；advance 1000（与繁体汉字同一档）。
* 权重：主 96 / 次 92 / 细 84 / 点 84。6–7 画字用满 96 保分量；
  8–9 画字在拥挤处（田 / 母 / 目 / 甘 类内白）局部降到 92 / 84。
* 端点：横竖撇捺一律平切硬边（hkbuild 的 hbar / vbar / diag 天然平切）；
  点与短撇一律用斜切平行四边形，slant 只用规格档
  26（短撇）/ 14（丿）/ -14（丶）/ 0（竖点）。
* 部件复用：氵 / 亻 / 扌 / 木 / 口 / 月 / 王 / 心 / 辶 / 力 / 艹 / 工 / 儿
  等在批内共用同一套部件函数，只做位置与大小的光学校正（GLY-004）。
* 内白：横画叠横画 ≥ 24 单位，竖与竖之间 ≥ 60 单位（GLY-006）；
  斜画离水平 ≥ 30°，以免与横画产生大重叠被 check_stroke_gaps 判为粘连。
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

# 字面框（墨迹外沿）
XL, XR = 60, 940
YT, YB = 820, 0

# 点 / 短撇的斜切档位（只用规格允许的值）
SLANT_DOT = -14   # 丶（右下的点）
SLANT_HI = 14     # 丿（左下的点）
SLANT_NOE = 26    # 短撇（氵的上点等）
SLANT_VERT = 0    # 竖点（亠的点）


# ---------------------------------------------------------------- 基础部件
def part_sanzui(g, x=60):
    """氵（三点水）：上点=短撇 26 / 中点=丶 -14 / 提=斜画。

    批内 汎・汽・泌 共用此坐标，仅整体平移。
    """
    g.dot(x + 128, 655, w=W_SEC, h=120, slant=SLANT_NOE)   # 上点（短撇）
    g.dot(x + 72, 450, w=W_SEC, h=120, slant=SLANT_DOT)    # 中点（丶）
    g.diag(x + 40, 230, x + 225, 360, weight=W_SEC)        # 提


def part_ni(g, x=60):
    """亻（单人旁）：撇 + 竖。侮・伺 共用。"""
    g.diag(x + 258, 775, x + 142, 480, weight=W_MAIN)      # 撇
    g.vbar(x + 152, 505, 0, weight=W_MAIN)                 # 竖


def part_tehen(g, x=60, right=345):
    """扌（提手旁）：横 + 竖 + 提。抹・拷・抄 共用。"""
    g.hbar(x, right, 620, weight=W_MAIN)                  # 横
    g.vbar(x + 140, 790, 0, weight=W_MAIN)                 # 竖
    g.diag(x + 20, 230, right - 5, 410, weight=W_SEC)      # 提


def part_kou(g, x1, x2, y1, y2, w=W_MAIN):
    """口：左竖 + 上横 + 右竖 + 下横（四角平切）。"""
    g.vbar(x1 + w / 2.0, y1, y2, weight=w)
    g.hbar(x1, x2, y2 - w / 2.0, weight=w)
    g.vbar(x2 - w / 2.0, y1, y2, weight=w)
    g.hbar(x1, x2, y1 + w / 2.0, weight=w)


def part_mu(g, cx, x1, x2, y_h, y_top, y_bot, sw=W_SEC):
    """木：横 + 竖 + 撇 + 捺。某・枕 共用同一套拆法。"""
    g.hbar(x1, x2, y_h, weight=W_MAIN)
    g.vbar(cx, y_top, y_bot, weight=W_MAIN)
    g.diag(cx, y_bot + 330, x1 + 15, y_bot + 10, weight=sw)
    g.diag(cx, y_bot + 330, x2 - 15, y_bot + 10, weight=sw)


def part_kusa(g, x1=60, x2=940, y=700):
    """艹：横 + 两竖（竖出头）。茎・芯 共用。"""
    g.hbar(x1, x2, y, weight=W_MAIN)
    g.vbar(330, YT, y - 10, weight=W_SEC)
    g.vbar(670, YT, y - 10, weight=W_SEC)


def part_ri(g, x1=60, x2=340, y_h=600):
    """土：短横 + 竖 + 底横（底横贴基线）。坑 共用。"""
    g.hbar(x1, x2, y_h, weight=W_MAIN)
    g.vbar(x1 + 135, y_h + 100, 96, weight=W_MAIN)
    g.hbar(x1, x2 + 10, 48, weight=W_MAIN)


def part_ou(g, cx, x1, x2, y_h=440, y_top=720, y_bot=96):
    """王：三横 + 竖。玩・旺 共用。"""
    g.hbar(x1, x2, y_h + 260, weight=W_MAIN)               # 上横
    g.hbar(x1 + 20, x2 - 20, y_h, weight=W_MAIN)            # 中横
    g.hbar(x1, x2, y_bot + 48, weight=W_MAIN)               # 下横（贴基线）
    g.vbar(cx, y_h + 260, y_bot + 48, weight=W_MAIN)


def part_tsukushi(g, x1, x2, y1, y2, w=W_MAIN):
    """月：左撇 + 上横 + 右竖 + 两内横。股・肢 共用。"""
    g.diag(x1 + 80, y2, x1 + 38, y1, weight=W_MAIN)         # 左撇
    g.hbar(x1 + 42, x2, y2 - w / 2.0, weight=W_SEC)         # 上横
    g.hbar(x1 + 52, x2 - 10, y1 + 470, weight=W_SEC)        # 内横 1
    g.hbar(x1 + 48, x2 - 15, y1 + 250, weight=W_SEC)        # 内横 2
    g.vbar(x2 - w / 2.0, y1, y2 - w / 2.0, weight=W_SEC)     # 右竖


def part_xin(g, x1, x2, y_bot):
    """心：左点 + 卧钩（三段折线近似）+ 中点 + 右点。芯・怨 共用。"""
    g.diag(x1 + 55, y_bot + 250, x1 + 95, y_bot + 60, weight=W_MAIN)
    g.diag(x1 + 95, y_bot + 60, x2 - 130, y_bot + 85, weight=W_MAIN)
    g.diag(x2 - 130, y_bot + 85, x2 - 85, y_bot + 255, weight=W_SEC)
    g.dot(x1 - 5, y_bot + 335, w=W_DOT, h=120, slant=SLANT_DOT)
    g.dot((x1 + x2) // 2, y_bot + 335, w=W_DOT, h=120, slant=SLANT_DOT)
    g.dot(x2 - 55, y_bot + 305, w=W_DOT, h=120, slant=SLANT_DOT)


def part_riki(g, x1, x2, y_top, y_bot, w=W_MAIN):
    """力：横 + 右竖（带左钩）+ 撇。劾・勅 共用。"""
    g.hbar(x1, x2, y_top, weight=W_SEC)                    # 横
    g.vbar(x2 - w / 2.0, y_top - w / 2.0, y_bot, weight=W_SEC)
    g.hbar(x2 - 130, x2, y_bot + 46, weight=W_SEC)           # 钩
    g.diag(x1 + 210, y_top + 60, x1 - 10, y_bot - 60, weight=W_MAIN)


def part_nyuu(g, x1, x2, y_top, y_bot):
    """儿：撇 + 竖弯钩。玩・呪 共用。"""
    g.diag(x1 + 200, y_top, x1 - 20, y_bot, weight=W_SEC)
    g.vbar(x2 - 48, y_top, y_bot + 48, weight=W_SEC)
    g.hbar(x2 - 48, x2, y_bot + 48, weight=W_SEC)


def part_chi(g, x1, x2, y_dot, y_base):
    """辶：丶 + 折 + 长捺。y_dot = 点中心高，y_base = 捺尾高。

    逝・逐 共用；长捺为辶的固有浅势（≈24°），不与任何横画相交。
    """
    g.dot(x1 + 90, y_dot, w=W_DOT, h=104, slant=SLANT_DOT)
    g.diag(x1 + 135, y_dot - 60, x1 + 75, y_dot - 210, weight=W_SEC)
    g.diag(x1 + 70, y_dot - 220, x2, y_base, weight=W_MAIN)


def part_mou(g, x1, x2, y_top, y_bot, shift=0, gap=0):
    """又：横 + 撇 + 捺。茎・支・殳 共用同一拆法。

    `shift` 是整个「又」**均匀上移**的量（三笔同量移 → 斜率与长度全不变，
    AGENTS.md 铁律 10）。

    `gap` 只把**横**额外上抬（撇、捺完全不动 → 它们的斜率绝对不变）：
    决定「横下缘 ↔ 捺上缘」那个中间腔高度的是这两者的**平行间距**，
    整体平移不改变间距（实测「股」的又夹出 h=23.8 的腔），
    单独抬横才能把间距拉开 → 腔高合格。
    """
    g.hbar(x1, x2, y_top + shift + gap, weight=W_SEC)
    g.diag(x2 - 40, y_top - 15 + shift, x1 + 30, y_bot + 60 + shift, weight=W_SEC)
    g.diag(x1 + 200, y_top - 60 + shift, x2 - 10, y_bot + shift, weight=W_SEC)


# ---------------------------------------------------------------- 32 字
def g_hei(g):
    """卑：上撇 + 田 + 下撇 + 横 + 竖。

    部件分区：田 占 x 320..700 / y 430..710；下横贯通 x 60..830；
    撇自田左下斜出，竖自田底穿横到底。
    """
    g.diag(500, 812, 408, 700, weight=W_SEC)               # 上撇
    # 田：上横 / 中横 / 下横 + 左竖 / 中竖 / 右竖
    g.hbar(320, 700, 662, weight=W_MAIN)
    g.hbar(320, 700, 545, weight=W_THIN)
    g.hbar(320, 700, 428, weight=W_MAIN)
    g.vbar(368, 430, 710, weight=W_MAIN)
    g.vbar(510, 430, 710, weight=W_THIN)
    g.vbar(652, 430, 710, weight=W_MAIN)
    g.hbar(60, 830, 300, weight=W_MAIN)                    # 贯通横
    g.diag(330, 392, 108, 88, weight=W_SEC)                # 下撇
    g.vbar(420, 430, 0, weight=W_MAIN)                     # 竖


def g_bu(g):
    """侮：亻 + 每（短撇 + 横 + 母）。

    部件分区：亻 占 x 60..300；每 占 x 420..940 / y 40..810。
    母：上横 + 下横 + 左竖 + 右竖 + 贯通中横 + 上下两点（点用 -14）。
    """
    part_ni(g, 60)
    g.diag(490, 810, 390, 650, weight=W_SEC)               # 每的短撇
    g.hbar(420, 940, 664, weight=W_MAIN)                   # 每的横
    # 母
    g.hbar(420, 880, 532, weight=W_MAIN)                   # 上横
    g.hbar(420, 880, 88, weight=W_MAIN)                    # 下横
    g.vbar(468, 40, 580, weight=W_MAIN)                    # 左竖
    g.vbar(832, 40, 580, weight=W_MAIN)                    # 右竖
    g.hbar(385, 915, 310, weight=W_THIN)                   # 贯通中横
    g.dot(590, 418, w=W_DOT, h=84, slant=SLANT_DOT)        # 上点
    g.dot(590, 202, w=W_DOT, h=84, slant=SLANT_DOT)        # 下点


def g_ma(g):
    """抹：扌 + 末。

    部件分区：扌 占 x 60..345；末 占 x 400..940。
    末：短横（主横之上）+ 长横 + 竖 + 撇 + 捺。
    """
    part_tehen(g, 60, 345)
    g.hbar(460, 880, 700, weight=W_SEC)                    # 短横
    g.hbar(400, 940, 520, weight=W_MAIN)                   # 长横
    g.vbar(670, 746, 0, weight=W_MAIN)                     # 竖
    g.diag(670, 450, 420, 60, weight=W_SEC)                # 撇
    g.diag(670, 450, 920, 60, weight=W_SEC)                # 捺


def g_kei(g):
    """茎：艹 + 又 + 工。

    部件分区：艹 占 y 654..820；又 占 y 300..640；工 占 y 0..260。
    """
    part_kusa(g, 60, 940, 700)
    part_mou(g, 130, 800, 590, 300)                        # 又
    g.hbar(170, 790, 190, weight=W_SEC)                    # 工的上横
    g.vbar(480, 144, 96, weight=W_SEC)                     # 工的竖
    g.hbar(140, 860, 48, weight=W_MAIN)                    # 工的下横


def g_han(g):
    """汎：氵 + 凡。

    部件分区：氵 占 x 60..285；凡 占 x 380..940。
    凡：撇 + 横 + 右竖（弯钩）+ 内部一点。
    """
    part_sanzui(g, 60)
    g.diag(438, 790, 392, 96, weight=W_MAIN)               # 撇
    g.hbar(392, 888, 742, weight=W_MAIN)                   # 横
    g.vbar(840, 742, 120, weight=W_MAIN)                   # 右竖
    g.dot(600, 430, w=W_DOT, h=112, slant=SLANT_DOT)       # 内部点


def g_sui(g):
    """帥：左窄目形 + 巾。

    部件分区：左部 占 x 60..410 / y 48..820；巾 占 x 480..940。
    """
    g.diag(152, 800, 88, 700, weight=W_SEC)                # 左上撇
    g.hbar(60, 410, 700, weight=W_SEC)                     # 上横
    g.hbar(60, 410, 480, weight=W_SEC)                     # 中横
    g.hbar(60, 410, 250, weight=W_SEC)                     # 下横
    g.vbar(110, 48, 720, weight=W_MAIN)                    # 左竖
    g.vbar(360, 48, 720, weight=W_MAIN)                    # 右竖
    g.hbar(480, 940, 700, weight=W_MAIN)                   # 巾的上横
    g.vbar(528, 160, 700, weight=W_MAIN)                   # 巾的左竖
    g.vbar(892, 160, 700, weight=W_MAIN)                   # 巾的右竖
    g.vbar(710, 60, 748, weight=W_MAIN)                    # 巾的中竖


def g_shini(g):
    """逝：辶 + 折。

    部件分区：折 占 x 380..940 / y 120..810；辶 占左下 x 60..700。
    """
    # 折：扌（缩小）+ 斤
    g.hbar(380, 540, 640, weight=W_SEC)                     # 扌横
    g.vbar(460, 760, 360, weight=W_MAIN)                   # 扌竖
    g.diag(390, 400, 560, 490, weight=W_SEC)               # 扌提
    g.diag(645, 795, 572, 706, weight=W_SEC)               # 斤上撇
    g.vbar(590, 700, 430, weight=W_MAIN)                   # 斤左竖
    g.hbar(560, 940, 480, weight=W_SEC)                    # 斤横
    g.vbar(880, 526, 120, weight=W_MAIN)                   # 斤右竖
    part_chi(g, 60, 700, 640, 120)


def g_ki(g):
    """汽：氵 + 気。

    部件分区：氵 占 x 60..285；気 占 x 385..940。
    気：短撇 + 横 + 乙（横 + 斜 + 底横 + 竖钩）。
    """
    part_sanzui(g, 60)
    g.diag(470, 810, 388, 700, weight=W_SEC)               # 𠂉的撇
    g.hbar(420, 940, 720, weight=W_SEC)                    # 𠂉的横
    g.hbar(430, 720, 580, weight=W_SEC)                    # 乙上横
    g.diag(690, 560, 480, 330, weight=W_SEC)               # 乙的斜
    g.hbar(480, 860, 280, weight=W_MAIN)                   # 乙底横
    g.vbar(812, 420, 280, weight=W_SEC)                    # 乙的竖钩


def g_kou(g):
    """坑：土 + 亢。

    部件分区：土 占 x 60..350；亢 占 x 400..940。
    亢：竖点（亠的点，slant 0）+ 横 + 几（撇 + 横 + 右竖）。
    2026-10-31 回修：亠的横（602..698）与几的横（514..606）白口 −4 → 几下移 30，白口 26。
    """
    part_ri(g, 60, 340, 600)
    g.dot(660, 762, w=W_SEC, h=110, slant=SLANT_VERT)      # 亠的点
    g.hbar(400, 940, 650, weight=W_MAIN)                   # 横
    g.diag(525, 530, 462, 96, weight=W_SEC)                # 几的撇
    g.hbar(490, 880, 530, weight=W_SEC)                    # 几的横（墨 484..576）
    g.vbar(832, 530, 110, weight=W_MAIN)                   # 几的右竖


def g_kyuu(g):
    """臼：撇 + 左竖 + 上横（左）+ 上横（右）+ 右竖 + 中横 + 底横。

    部件分区：整字 x 112..888 / y 0..820；左右上横之间留 60 单位白。
    """
    g.diag(215, 805, 130, 700, weight=W_SEC)               # 撇
    g.vbar(160, 48, 740, weight=W_MAIN)                    # 左竖
    g.hbar(112, 500, 760, weight=W_SEC)                    # 左上横
    g.hbar(560, 888, 760, weight=W_SEC)                    # 右上横
    g.vbar(840, 48, 760, weight=W_MAIN)                    # 右竖
    g.hbar(112, 888, 420, weight=W_SEC)                    # 中横
    g.hbar(112, 888, 48, weight=W_MAIN)                    # 底横


def g_ro(g):
    """呂：上口 + 下口（上小下大）。

    部件分区：上口 x 220..780 / y 470..790；下口 x 100..900 / y 40..420。
    """
    part_kou(g, 220, 780, 470, 790, W_SEC)
    part_kou(g, 100, 900, 40, 420, W_MAIN)


def g_kou2(g):
    """拷：扌 + 考。

    部件分区：扌 占 x 60..345；考 占 x 400..940 / y 60..820。
    考：竖 + 上横 + 长横 + 长撇 + 丂（横 + 竖 + 底横）。
    """
    part_tehen(g, 60, 345)
    g.vbar(560, 820, 700, weight=W_MAIN)                   # 竖
    g.hbar(420, 720, 690, weight=W_SEC)                    # 上横
    g.hbar(400, 940, 560, weight=W_SEC)                    # 长横
    g.diag(720, 760, 450, 330, weight=W_MAIN)              # 长撇
    g.hbar(530, 850, 290, weight=W_SEC)                    # 丂的横
    g.vbar(540, 244, 120, weight=W_SEC)                    # 丂的竖
    g.hbar(540, 830, 120, weight=W_MAIN)                   # 丂的底横


def g_shin(g):
    """枕：木 + 冘。

    部件分区：木 占 x 60..340；冘 占 x 380..940。
    冘：短撇 + 冖（横 + 右竖）+ 儿。
    """
    part_mu(g, 200, 60, 340, 560, 760, 0)                  # 木
    g.dot(470, 748, w=W_DOT, h=104, slant=SLANT_NOE)       # 冘的短撇
    g.hbar(510, 900, 640, weight=W_SEC)                    # 冖的横
    g.vbar(858, 640, 470, weight=W_MAIN)                   # 冖的右竖
    g.diag(640, 540, 430, 60, weight=W_SEC)                # 儿的撇
    g.vbar(720, 540, 140, weight=W_MAIN)                   # 儿的竖
    g.hbar(720, 920, 140, weight=W_MAIN)                   # 儿的弯钩


def g_koku(g):
    """劾：亥 + 力。

    部件分区：亥 占 x 60..540；力 占 x 560..940。
    亥：竖点（0）+ 横 + 撇 + 捺（成 X）+ 人（撇 + 捺）。
    """
    g.dot(300, 760, w=W_SEC, h=110, slant=SLANT_VERT)      # 亠的点
    g.hbar(60, 470, 690, weight=W_MAIN)                    # 横
    g.diag(430, 620, 200, 420, weight=W_SEC)               # 撇
    g.diag(250, 520, 450, 380, weight=W_SEC)               # 捺（与撇交叉）
    g.diag(340, 420, 120, 60, weight=W_MAIN)               # 人的撇
    g.diag(340, 420, 540, 60, weight=W_MAIN)               # 人的捺
    part_riki(g, 570, 940, 600, 300)


def g_batsu(g):
    """某：甘 + 木。

    部件分区：甘 占 x 160..840 / y 440..820；木 占 x 200..840 / y 0..420。
    """
    g.hbar(160, 840, 770, weight=W_MAIN)                   # 甘上横
    g.vbar(208, 440, 800, weight=W_MAIN)                   # 甘左竖
    g.vbar(792, 440, 800, weight=W_MAIN)                   # 甘右竖
    g.hbar(208, 792, 630, weight=W_SEC)                    # 甘内横 1
    g.hbar(208, 792, 500, weight=W_SEC)                    # 甘内横 2
    g.hbar(200, 840, 380, weight=W_MAIN)                   # 木上横
    g.vbar(520, 428, 0, weight=W_MAIN)                    # 木竖
    g.diag(520, 350, 250, 20, weight=W_SEC)                # 木撇
    g.diag(520, 350, 800, 20, weight=W_SEC)                # 木捺


def g_kou3(g):
    """虹：虫 + 工。

    部件分区：虫 占 x 60..560 / y 120..760；工 占 x 600..940。
    """
    part_kou(g, 100, 500, 400, 720, W_SEC)                 # 虫的口
    g.vbar(300, 720, 280, weight=W_MAIN)                   # 虫的竖
    g.hbar(60, 560, 240, weight=W_MAIN)                    # 虫的横
    g.dot(580, 150, w=W_DOT, h=100, slant=SLANT_DOT)       # 虫的尾点
    g.hbar(600, 940, 700, weight=W_SEC)                    # 工上横
    g.vbar(770, 654, 96, weight=W_SEC)                     # 工竖
    g.hbar(600, 940, 48, weight=W_MAIN)                    # 工下横


def g_hitsu(g):
    """泌：氵 + 必。

    部件分区：氵 占 x 60..285；必 占 x 330..940。
    必：上点 + 长撇（穿过）+ 卧钩 + 中点 + 右点。
    """
    part_sanzui(g, 60)
    g.dot(408, 690, w=W_DOT, h=104, slant=SLANT_DOT)       # 上点
    g.diag(700, 780, 400, 120, weight=W_MAIN)              # 长撇
    g.diag(480, 560, 520, 200, weight=W_MAIN)              # 卧钩（左）
    g.diag(520, 200, 850, 230, weight=W_MAIN)              # 卧钩（底）
    g.diag(850, 230, 880, 400, weight=W_SEC)               # 卧钩（钩）
    g.dot(600, 520, w=W_DOT, h=110, slant=SLANT_DOT)       # 中点
    g.dot(830, 450, w=W_DOT, h=110, slant=SLANT_DOT)       # 右点


def g_jyu(g):
    """呪：口 + 兄。

    部件分区：口 占 x 60..330 / y 180..680；兄 占 x 380..940。
    """
    part_kou(g, 60, 330, 180, 680, W_SEC)
    part_kou(g, 440, 900, 400, 720, W_SEC)                 # 兄的口
    part_nyuu(g, 480, 900, 446, 60)


def g_enn(g):
    """怨：夕 + 卩形 + 心。

    部件分区：上半 占 y 480..820；心 占 y 0..420。
    """
    g.diag(360, 800, 180, 620, weight=W_SEC)               # 夕的撇
    g.hbar(190, 430, 700, weight=W_SEC)                    # 夕的横
    g.diag(410, 700, 170, 470, weight=W_SEC)               # 夕的横撇
    g.dot(250, 560, w=W_DOT, h=100, slant=SLANT_DOT)       # 夕的点
    g.hbar(520, 880, 740, weight=W_SEC)                    # 卩形的横
    g.vbar(568, 694, 480, weight=W_SEC)                    # 卩形的左竖
    g.vbar(832, 694, 560, weight=W_SEC)                    # 卩形的右竖
    part_xin(g, 220, 900, 0)


def g_kushi(g):
    """串：上口 + 下口 + 中竖（上下出头）。

    部件分区：上口 x 160..840 / y 440..700；下口 x 100..900 / y 60..340。
    """
    part_kou(g, 160, 840, 440, 700, W_SEC)
    part_kou(g, 100, 900, 60, 340, W_MAIN)
    g.vbar(500, 820, 60, weight=W_MAIN)                    # 中竖


def g_choku(g):
    """勅：束 + 力。

    部件分区：束 占 x 60..600；力 占 x 620..940。
    """
    g.vbar(330, 820, 760, weight=W_MAIN)                   # 束的竖
    g.hbar(60, 600, 760, weight=W_MAIN)                    # 束上横
    part_kou(g, 60, 600, 380, 666, W_SEC)                  # 束的口
    g.vbar(330, 666, 380, weight=W_MAIN)                   # 束的中竖
    g.diag(330, 380, 70, 60, weight=W_SEC)                 # 束的撇
    g.diag(330, 380, 590, 60, weight=W_SEC)                # 束的捺
    part_riki(g, 620, 940, 560, 260)


def g_mayumi(g):
    """眉：尸形 + 目。

    部件分区：尸形 占 x 60..200；目 占 x 310..930 / y 132..686。
    """
    g.diag(190, 800, 110, 700, weight=W_SEC)               # 尸形的撇
    g.hbar(60, 940, 772, weight=W_MAIN)                    # 尸形的横
    g.vbar(150, 724, 340, weight=W_MAIN)                   # 尸形的竖
    g.diag(150, 340, 70, 110, weight=W_SEC)                # 尸形的撇脚
    g.hbar(310, 930, 640, weight=W_SEC)                    # 目上横
    g.hbar(310, 930, 500, weight=W_SEC)                    # 目内横 1
    g.hbar(310, 930, 340, weight=W_SEC)                    # 目内横 2
    g.hbar(310, 930, 180, weight=W_MAIN)                   # 目底横
    g.vbar(358, 132, 686, weight=W_SEC)                    # 目左竖
    g.vbar(882, 132, 686, weight=W_MAIN)                   # 目右竖


def g_shin2(g):
    """芯：艹 + 心。

    部件分区：艹 占 y 654..820；心 占 x 220..900 / y 0..600。
    """
    part_kusa(g, 60, 940, 700)
    part_xin(g, 220, 900, 0)


def g_shi(g):
    """伺：亻 + 司。

    部件分区：亻 占 x 60..300；司 占 x 380..940。
    司：横 + 右竖（带钩）+ 内横 + 内口。
    """
    part_ni(g, 60)
    g.hbar(380, 940, 772, weight=W_MAIN)                   # 司的横
    g.vbar(892, 724, 120, weight=W_MAIN)                   # 司的右竖
    g.hbar(820, 892, 120, weight=W_SEC)                    # 司的钩
    g.hbar(430, 800, 580, weight=W_SEC)                    # 内横
    part_kou(g, 470, 800, 180, 500, W_SEC)                 # 内口


def g_bu2(g):
    """股：月 + 殳。

    部件分区：月 占 x 60..330；殳 占 x 380..940。
    殳：几（撇 + 横 + 右竖）+ 又。
    """
    part_tsukushi(g, 60, 330, 60, 820)
    g.diag(438, 800, 386, 600, weight=W_SEC)               # 几的撇
    g.hbar(400, 830, 760, weight=W_SEC)                    # 几的横
    g.vbar(782, 714, 580, weight=W_SEC)                    # 几的右竖
    part_mou(g, 380, 900, 490, 170, gap=22)


def g_gan(g):
    """玩：王 + 元。

    部件分区：王 占 x 60..400；元 占 x 440..940。
    元：两横 + 撇 + 竖弯钩。
    """
    part_ou(g, 230, 60, 400, 400, 720, 0)
    g.hbar(440, 940, 740, weight=W_MAIN)                   # 元上横
    g.hbar(460, 920, 600, weight=W_SEC)                    # 元次横
    g.diag(650, 554, 460, 60, weight=W_SEC)                # 元的撇
    g.vbar(760, 554, 140, weight=W_SEC)                    # 元的竖
    g.hbar(760, 920, 140, weight=W_SEC)                    # 元的弯钩


def g_chiku(g):
    """逐：辶 + 豕。

    部件分区：豕 占 x 400..940 / y 120..810；辶 占左下 x 60..700。
    """
    g.hbar(430, 940, 770, weight=W_MAIN)                   # 豕的横
    g.diag(790, 740, 400, 430, weight=W_MAIN)              # 豕的长撇
    g.vbar(640, 700, 140, weight=W_MAIN)                   # 豕的弯钩竖
    g.hbar(560, 640, 140, weight=W_SEC)                    # 豕的弯钩
    g.diag(860, 700, 660, 470, weight=W_SEC)               # 豕的撇 1
    g.diag(900, 540, 720, 330, weight=W_SEC)               # 豕的撇 2
    g.diag(660, 380, 940, 130, weight=W_SEC)               # 豕的捺
    part_chi(g, 60, 700, 640, 120)


def g_mou2(g):
    """妄：亡 + 女。

    部件分区：亡 占 x 180..820 / y 420..820；女 占 x 180..760 / y 0..420。
    女：撇点（竖头撇 + 长捺）+ 长撇 + 横。
    """
    g.dot(500, 762, w=W_SEC, h=110, slant=SLANT_VERT)      # 亠的点
    g.hbar(180, 820, 700, weight=W_MAIN)                   # 亡的横
    g.vbar(228, 652, 480, weight=W_MAIN)                   # 亡的竖
    g.hbar(228, 720, 480, weight=W_MAIN)                   # 亡的折
    g.diag(360, 420, 250, 240, weight=W_SEC)               # 女的撇点（上）
    g.diag(250, 240, 660, 60, weight=W_SEC)                # 女的撇点（捺）
    g.diag(700, 380, 200, 40, weight=W_SEC)                # 女的撇
    g.hbar(180, 760, 250, weight=W_SEC)                    # 女的横


def g_shi2(g):
    """肢：月 + 支。

    部件分区：月 占 x 60..330；支 占 x 380..940。
    支：十（上）+ 又（下）。
    """
    part_tsukushi(g, 60, 330, 60, 820)
    g.hbar(500, 820, 700, weight=W_MAIN)                   # 十的横
    g.vbar(660, 820, 620, weight=W_MAIN)                   # 十的竖
    part_mou(g, 380, 940, 560, 180)


def g_shou(g):
    """抄：扌 + 少。

    部件分区：扌 占 x 60..345；少 占 x 380..940。
    少：竖 + 左撇点 + 右撇点 + 长撇。
    """
    part_tehen(g, 60, 345)
    g.vbar(660, 800, 330, weight=W_MAIN)                   # 少的竖
    g.diag(520, 660, 440, 470, weight=W_SEC)               # 少的左点
    g.dot(820, 600, w=W_DOT, h=110, slant=SLANT_HI)        # 少的右点
    g.diag(700, 330, 420, 60, weight=W_MAIN)               # 少的长撇


def g_ou2(g):
    """旺：日 + 王。

    部件分区：日 占 x 30..430 / y 118..800；王 占 x 450..940。
    """
    part_kou(g, 60, 400, 120, 800, W_SEC)                   # 日
    # 2026-10-31 回修：原来在 helper 画出的日底横之外又叠画一条同高的加宽横
    # （中心线同为 166、x 重叠 60..400）→ 白口 −94。两条同高等于同一条，删掉重复的那条。
    part_ou(g, 695, 450, 940, 440, 720, 0)


def g_ichi(g):
    """壱：士 + 冖 + 匕。

    部件分区：士 占 x 180..820 / y 552..820；冖 占 x 60..940 / y 320..518；
    匕 占 x 330..760 / y 60..350。
    """
    g.vbar(500, 820, 630, weight=W_MAIN)                   # 士的竖
    g.hbar(180, 820, 730, weight=W_MAIN)                   # 士的长横
    g.hbar(250, 750, 600, weight=W_MAIN)                   # 士的短横
    g.hbar(60, 940, 470, weight=W_MAIN)                    # 冖的横
    g.vbar(108, 422, 320, weight=W_SEC)                     # 冖的左竖
    g.diag(520, 350, 330, 250, weight=W_SEC)               # 匕的撇
    g.vbar(500, 360, 120, weight=W_MAIN)                   # 匕的竖
    g.hbar(500, 740, 120, weight=W_MAIN)                   # 匕的弯钩


# ---------------------------------------------------------------- 清单
TABLE = [
    (g_hei, 0x5351, "卑：上撇+田+下撇+贯通横+竖"),
    (g_bu, 0x4FAE, "侮：亻+每（短撇+横+母）"),
    (g_ma, 0x62B9, "抹：扌+末"),
    (g_kei, 0x830E, "茎：艹+又+工"),
    (g_han, 0x6C4E, "汎：氵+凡"),
    (g_sui, 0x5E25, "帥：左窄目形+巾"),
    (g_shini, 0x901D, "逝：辶+折"),
    (g_ki, 0x6C7D, "汽：氵+気"),
    (g_kou, 0x5751, "坑：土+亢"),
    (g_kyuu, 0x81FC, "臼：撇+左竖+上横+右上横+右竖+中横+底横"),
    (g_ro, 0x5442, "呂：上口+下口"),
    (g_kou2, 0x62F7, "拷：扌+考"),
    (g_shin, 0x6795, "枕：木+冘"),
    (g_koku, 0x52BE, "劾：亥+力"),
    (g_batsu, 0x67D0, "某：甘+木"),
    (g_kou3, 0x8679, "虹：虫+工"),
    (g_hitsu, 0x6CCC, "泌：氵+必"),
    (g_jyu, 0x546A, "呪：口+兄"),
    (g_enn, 0x6028, "怨：夕+卩形+心"),
    (g_kushi, 0x4E32, "串：上口+下口+中竖"),
    (g_choku, 0x52C5, "勅：束+力"),
    (g_mayumi, 0x7709, "眉：尸形+目"),
    (g_shin2, 0x82AF, "芯：艹+心"),
    (g_shi, 0x4F3A, "伺：亻+司"),
    (g_bu2, 0x80A1, "股：月+殳"),
    (g_gan, 0x73A9, "玩：王+元"),
    (g_chiku, 0x9010, "逐：辶+豕"),
    (g_mou2, 0x5984, "妄：亡+女"),
    (g_shi2, 0x80A2, "肢：月+支"),
    (g_shou, 0x6284, "抄：扌+少"),
    (g_ou2, 0x65FA, "旺：日+王"),
    (g_ichi, 0x58F1, "壱：士+冖+匕"),
]


def build() -> list[Glyph]:
    out: list[Glyph] = []
    for fn, uni, note in TABLE:
        g = Glyph(name=f"uni{uni:04X}", advance=1000, unicode=uni, note=note)
        fn(g)
        out.append(g)
    return out


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-020.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
