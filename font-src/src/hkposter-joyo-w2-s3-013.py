"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s3-013。

本批 24 字，笔画范围 10–13，取自 2010 年文化厅《常用漢字表》。

整体取舍
--------
* 字面框 x 60..940、y 0..820，与繁体汉字完全一致；advance 1000。
* 笔画权重：主 96 / 次 92 / 细 84 / 点 84。10 画以下字用满 96 档找重心，
  11–13 画的密字在方框段用 84 档，保证腔不被吃光。
* 三个方框母题（口/日/目/田/罒）统一用同一套算法：横 84、竖 96、
  内白净距 30，框高 = (n_inner+1)×114 + 84，绝不压到 24 以下。
* 同部件在批内复用同一套坐标与笔画拆法：亻（借/傾）、扌（掲/探/揮）、
  辶（遠/遊）、冖（探/揮）、木（探/棄）、心（恵）全部同坐标，
  只做位置光学校正（docs/03 GLY-004）。
* 点与短撇一律用斜切平行四边形，slant 分档：右下的点 −14、左下的点 +14、
  竖点 0、氵类短撇 26，不自造档位（GLY-003）。
* 笔画角度照标准骨架，不改方向（项目所有者 2026-10-25）。
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

# 方框类笔画的内白净距与交叠深度（单位：字体单位）
GAP = 30
OV = 28


# ---------------------------------------------------------------- 基础构件

def _kou(g, x1, x2, yt, yb, wh=W_THIN, wv=W_MAIN, ov=OV):
    """口 型方框。yt=外框上缘，yb=外框下缘。内白高 = (yt-yb) - 2*wh。"""
    g.hbar(x1, x2, yt - wh / 2, weight=wh)
    g.hbar(x1, x2, yb + wh / 2, weight=wh)
    g.vbar(x1 + wv / 2, yt - ov, yb + wh - ov, weight=wv)
    g.vbar(x2 - wv / 2, yt - ov, yb + wh - ov, weight=wv)


def _ri(g, x1, x2, yt, yb, n_inner, wh=W_THIN, wv=W_MAIN, ov=OV, gap=GAP):
    """日/目 型方框（n_inner 条内横）。

    约定：yt-yb = (n_inner+1)*(wh+gap) + wh，内白净距恒为 gap。
    返回全部横的中心线（自下而上）。
    """
    sp = wh + gap
    c = yb + wh / 2
    centers = [c]
    for _ in range(n_inner):
        c += sp
        centers.append(c)
    c += sp
    centers.append(c)
    for cy in centers:
        g.hbar(x1, x2, cy, weight=wh)
    g.vbar(x1 + wv / 2, yt - ov, yb + wh - ov, weight=wv)
    g.vbar(x2 - wv / 2, yt - ov, yb + wh - ov, weight=wv)
    return centers


def _tian(g, x1, x2, yt, yb, cx, cy, wh=W_THIN, wv=W_MAIN, ov=OV):
    """田 型方框：中竖 + 中横。cy 为中横中心线。"""
    g.hbar(x1, x2, yt - wh / 2, weight=wh)
    g.hbar(x1, x2, cy, weight=wh)
    g.hbar(x1, x2, yb + wh / 2, weight=wh)
    g.vbar(x1 + wv / 2, yt - ov, yb + wh - ov, weight=wv)
    g.vbar(x2 - wv / 2, yt - ov, yb + wh - ov, weight=wv)
    g.vbar(cx, yt - ov, yb + wh - ov, weight=W_THIN)


def _si(g, x1, x2, yt, yb, mids, wh=W_THIN, wv=W_MAIN, ov=OV):
    """罒 型方框：横框 + 若干内竖（mids 为内竖中心线列表）。"""
    g.hbar(x1, x2, yt - wh / 2, weight=wh)
    g.hbar(x1, x2, yb + wh / 2, weight=wh)
    g.vbar(x1 + wv / 2, yt - ov, yb + wh - ov, weight=wv)
    g.vbar(x2 - wv / 2, yt - ov, yb + wh - ov, weight=wv)
    for cx in mids:
        g.vbar(cx, yt - ov, yb + wh - ov, weight=W_THIN)


def _mu(g, x, y, w=W_THIN):
    """厶（厶）：丿 + 折 + 丶。x=左缘，y=底部折线中心线高度。"""
    g.diag(x + 112, y + 96, x + 18, y + 34, weight=w)
    g.hbar(x + 14, x + 118, y, weight=w)
    g.dot(x + 148, y + 46, w=w, h=100, slant=-14)


def _wei(g, x1, x2, y_c, w=W_THIN):
    """冖：横 + 左竖 + 右竖。"""
    g.hbar(x1, x2, y_c, weight=w)
    g.vbar(x1 + 42, y_c + 10, y_c - 120, weight=w)
    g.vbar(x2 - 42, y_c + 10, y_c - 120, weight=w)


def _ren(g, x=60, y_top=790, y_bot=120):
    """亻：丿 + 丨。批内（借/傾）复用同一坐标。"""
    g.diag(x + 240, y_top, x + 50, y_top - 270, weight=W_THIN)
    g.vbar(x + 155, y_top - 140, y_bot, weight=W_MAIN)


def _te(g):
    """扌：一 + 亅（带钩）+ 提。批内（掲/探/揮）复用同一坐标。"""
    g.hbar(80, 320, 648, weight=W_MAIN)
    g.vbar(200, 780, 130, weight=W_MAIN)
    g.diag(188, 142, 150, 186, weight=W_THIN)
    g.diag(100, 470, 330, 540, weight=W_THIN)


def _mokuji(g, x1=100, x2=330, y_c=505, x_bottom=380, y_bottom=60, w=W_THIN):
    """辶：丶 + 一 + 折 + 平捺。批内（遠/遊）复用同一坐标。

    平捺贴底走平（近水平、极轻的上扬），不横扫主体。
    """
    g.dot(120, 720, w=W_DOT, h=110, slant=-14)
    g.hbar(80, 220, 610, weight=W_THIN)
    g.diag(210, 580, 120, 150, weight=W_THIN)
    g.diag(120, 110, 930, 130, weight=W_MAIN)


def _mu_glyph(g, cx, y_hbar, y_bottom, x_left, x_right, w_h=W_MAIN):
    """木：一 + 丨 + 丿 + ㇏。"""
    g.hbar(x_left, x_right, y_hbar, weight=w_h)
    g.vbar(cx, y_hbar + 30, y_bottom, weight=W_MAIN)
    g.diag(cx - 30, y_hbar - 20, x_left + 20, y_bottom, weight=W_THIN)
    g.diag(cx + 30, y_hbar - 20, x_right - 20, y_bottom, weight=W_THIN)


# ---------------------------------------------------------------- 字形

def _tou():
    """項（12画）：工 + 頁。

    工（x 60..400）：上横 ink 724..820，中竖 240，下横 ink 130..226。
    頁（x 430..940）：一 ink 724..820，丿 790→620，目 ink 620..194，
    八 250→70。
    """
    g = Glyph("uni9805", advance=1000, unicode=0x9805, note="項：工＋頁，左工右頁。")

    # 工
    g.hbar(100, 380, 772, weight=W_MAIN)          # 上横
    g.vbar(240, 790, 200, weight=W_MAIN)          # 竖
    g.hbar(80, 400, 178, weight=W_MAIN)           # 下横

    # 頁
    g.hbar(460, 920, 772, weight=W_MAIN)          # 一
    g.diag(790, 785, 630, 620, weight=W_SEC)      # 丿
    _ri(g, 520, 880, 620, 194, 2)                 # 目（3 腔，净距 30）
    g.diag(640, 250, 530, 70, weight=W_MAIN)      # 八·撇
    g.diag(750, 250, 870, 70, weight=W_MAIN)      # 八·捺
    return g


def _sou():
    """喪（12画）：亠 + 吅 + 一 + 衣底。

    竖点 0 档在顶；吅用两独立口（x 230..500 / 510..780）；
    衣底 = 丿 + 竖提 + ノ + ㇏。
    """
    g = Glyph("uni55AA", advance=1000, unicode=0x55AA, note="喪：亠＋吅＋一＋衣底。")

    g.dot(500, 770, w=W_DOT, h=96, slant=0)       # 亠的点（竖点 0 档）
    g.hbar(160, 840, 684, weight=W_MAIN)          # 亠的一
    _kou(g, 230, 500, 606, 396)                   # 吅·左口
    _kou(g, 510, 780, 606, 396)                   # 吅·右口
    g.hbar(140, 860, 314, weight=W_MAIN)          # 吅下的一
    g.diag(500, 262, 370, 58, weight=W_MAIN)      # 衣底·丿
    g.vbar(600, 250, 112, weight=W_MAIN)          # 衣底·竖提
    g.diag(610, 128, 700, 192, weight=W_THIN)     # 衣底·提锋
    g.diag(770, 250, 700, 145, weight=W_THIN)     # 衣底·ノ
    g.diag(820, 232, 910, 58, weight=W_MAIN)      # 衣底·㇏
    return g


def _en():
    """遠（12画）：袁 + 辶。

    袁（x 330..880）：土（竖 + 两横）+ 口 + 衣底三笔。
    辶 用批内共用坐标。
    """
    g = Glyph("uni9060", advance=1000, unicode=0x9060, note="遠：袁＋辶，走之底。")

    # 袁
    g.vbar(600, 820, 640, weight=W_MAIN)          # 土的竖
    g.hbar(400, 820, 748, weight=W_MAIN)          # 土上横
    g.hbar(380, 840, 624, weight=W_MAIN)          # 土下横
    _kou(g, 430, 740, 520, 310)                   # 口
    g.diag(545, 300, 445, 215, weight=W_MAIN)     # 衣底·丿
    g.vbar(620, 330, 200, weight=W_MAIN)          # 衣底·竖提（与口底贯通）
    g.diag(630, 210, 700, 255, weight=W_THIN)     # 提锋
    g.diag(715, 310, 660, 215, weight=W_THIN)     # 衣底·ノ
    g.diag(720, 295, 860, 220, weight=W_MAIN)     # 衣底·㇏

    _mokuji(g)
    return g


def _gai():
    """街（12画）：彳 + 圭 + 亍。

    彳（x 60..300）：两撇 + 竖；圭（x 300..660）：土 + 土（四横两竖）；
    亍（x 690..940）：一 + 一 + 亅（带钩）。
    """
    g = Glyph("uni8857", advance=1000, unicode=0x8857, note="街：彳＋圭＋亍。")

    # 彳
    g.diag(240, 780, 130, 660, weight=W_THIN)     # 上撇
    g.diag(255, 640, 125, 490, weight=W_THIN)     # 下撇
    g.vbar(170, 520, 130, weight=W_MAIN)          # 竖

    # 圭
    g.hbar(330, 640, 772, weight=W_MAIN)          # 一
    g.vbar(485, 820, 620, weight=W_MAIN)          # 上竖
    g.hbar(320, 650, 616, weight=W_MAIN)          # 二
    g.hbar(330, 640, 490, weight=W_MAIN)          # 三
    g.vbar(485, 510, 390, weight=W_MAIN)          # 下竖
    g.hbar(330, 640, 364, weight=W_MAIN)          # 四

    # 亍
    g.hbar(720, 900, 742, weight=W_THIN)          # 一
    g.hbar(690, 930, 602, weight=W_THIN)          # 一
    g.vbar(845, 580, 205, weight=W_MAIN)          # 亅
    g.diag(833, 218, 785, 252, weight=W_THIN)     # 钩
    return g


def _kai():
    """絵（12画）：糸 + 会。

    糸（x 60..380）：两组撇折 + 竖 + 小（丿 + 丶）；
    会（x 400..940）：人 + 一 + 厶。
    """
    g = Glyph("uni7D75", advance=1000, unicode=0x7D75, note="絵：糸＋会。")

    # 糸
    g.diag(300, 790, 145, 648, weight=W_THIN)     # 上撇
    g.hbar(145, 305, 606, weight=W_THIN)          # 上折
    g.diag(310, 636, 155, 488, weight=W_THIN)     # 下撇
    g.hbar(155, 315, 446, weight=W_THIN)          # 下折
    g.vbar(235, 424, 118, weight=W_MAIN)          # 竖
    g.diag(158, 396, 76, 186, weight=W_THIN)      # 小·丿
    g.dot(306, 244, w=W_DOT, h=112, slant=14)     # 小·右点（+14）

    # 会
    g.diag(620, 818, 428, 660, weight=W_THIN)     # 人·撇
    g.diag(620, 818, 852, 660, weight=W_THIN)     # 人·捺
    g.hbar(450, 890, 540, weight=W_SEC)           # 一
    _mu(g, 452, 240, w=W_THIN)                    # 厶
    return g


def _etsu():
    """越（12画）：走 + 戉。

    走（x 60..470）：土（竖 + 两横）+ 下平横 + 竖 + 丿 + 长捺；
    戉（x 460..940）：一 + 竖 + 斜钩 + 撇 + 点。
    """
    g = Glyph("uni8D8A", advance=1000, unicode=0x8D8A, note="越：走＋戉。")

    # 走
    g.hbar(120, 400, 748, weight=W_MAIN)          # 土上横
    g.vbar(260, 820, 640, weight=W_MAIN)          # 土的竖
    g.hbar(100, 420, 608, weight=W_MAIN)          # 土下横
    g.hbar(90, 430, 468, weight=W_MAIN)           # 下平横
    g.vbar(250, 460, 300, weight=W_MAIN)          # 竖
    g.diag(245, 360, 105, 160, weight=W_THIN)     # 丿
    g.diag(240, 60, 850, 110, weight=W_MAIN)      # 长捺（贴底走平）

    # 戉
    g.hbar(490, 900, 738, weight=W_MAIN)          # 一
    g.vbar(560, 700, 560, weight=W_SEC)            # 竖
    g.diag(700, 810, 860, 280, weight=W_MAIN)     # 斜钩
    g.diag(858, 285, 818, 335, weight=W_THIN)     # 钩锋
    g.diag(860, 640, 660, 470, weight=W_THIN)     # 撇
    g.dot(878, 790, w=W_DOT, h=96, slant=-14)      # 点
    return g


def _kei():
    """掲（11画）：扌 + 曷。

    扌用批内共用坐标；曷（x 350..940）= 日 + 匂（丿 + 横折钩 + 匕）。
    """
    g = Glyph("uni63B2", advance=1000, unicode=0x63B2, note="掲：扌＋曷。")

    _te(g)

    # 曷
    _ri(g, 500, 860, 820, 508, 1)                 # 日（2 腔）
    g.diag(690, 540, 540, 240, weight=W_THIN)     # 匂·丿
    g.hbar(600, 890, 420, weight=W_THIN)          # 匂·横
    g.vbar(848, 420, 190, weight=W_THIN)          # 匂·折钩竖
    g.diag(838, 205, 796, 248, weight=W_THIN)     # 钩锋
    g.diag(760, 390, 660, 280, weight=W_THIN)     # 匕·丿
    g.vbar(700, 350, 250, weight=W_THIN)          # 匕·竖
    g.hbar(700, 830, 292, weight=W_THIN)          # 匕·底
    return g


def _ki():
    """棄（13画）：亠 + 廿 + 厶 + 木。

    竖点 0 档；廿（x 240..760）三竖一底；厶居中；木居底。
    """
    g = Glyph("uni68C4", advance=1000, unicode=0x68C4, note="棄：亠＋廿＋厶＋木。")

    g.dot(500, 778, w=W_DOT, h=80, slant=0)       # 竖点（0 档）
    g.hbar(160, 840, 692, weight=W_MAIN)          # 亠的一
    g.hbar(240, 760, 576, weight=W_THIN)          # 廿顶
    g.vbar(300, 590, 452, weight=W_SEC)           # 廿左竖
    g.vbar(500, 590, 452, weight=W_SEC)           # 廿中竖
    g.vbar(700, 590, 452, weight=W_SEC)           # 廿右竖
    g.hbar(240, 760, 466, weight=W_THIN)          # 廿底
    # 厶（丿自廿底伸出，折 + 点居中）
    g.diag(560, 440, 470, 370, weight=W_THIN)      # 厶·丿
    g.hbar(470, 570, 356, weight=W_THIN)          # 厶·折
    g.dot(615, 350, w=W_DOT, h=92, slant=-14)      # 厶·丶
    # 木
    g.hbar(180, 820, 242, weight=W_MAIN)          # 木·一
    g.vbar(500, 262, 40, weight=W_MAIN)           # 木·竖
    g.diag(470, 270, 220, 90, weight=W_THIN)      # 木·丿
    g.diag(530, 270, 800, 90, weight=W_THIN)      # 木·㇏
    return g


def _yoku():
    """欲（11画）：谷 + 欠。

    谷（x 60..460）= 八 + 人 + 口；欠（x 480..940）= 丿 + 横撇 + 人。
    """
    g = Glyph("uni6B32", advance=1000, unicode=0x6B32, note="欲：谷＋欠。")

    # 谷
    g.diag(215, 818, 140, 690, weight=W_THIN)     # 八·丿
    g.dot(330, 752, w=W_DOT, h=100, slant=-14)     # 八·丶
    g.diag(290, 690, 110, 460, weight=W_MAIN)     # 人·丿
    g.diag(290, 690, 430, 460, weight=W_MAIN)     # 人·捺
    _kou(g, 120, 380, 400, 190)                   # 口

    # 欠
    g.diag(620, 818, 490, 640, weight=W_THIN)     # 丿
    g.hbar(560, 790, 590, weight=W_THIN)          # 横撇
    g.diag(780, 610, 670, 470, weight=W_THIN)     # 撇
    g.diag(700, 560, 520, 220, weight=W_MAIN)     # 人·丿
    g.diag(710, 560, 910, 230, weight=W_MAIN)     # 人·捺
    return g


def _itai():
    """痛（12画）：疒 + 甬。

    疒（x 60..430）= 点 + 一 + 长撇 + 冫两点；甬（x 440..940）= マ + 用。
    """
    g = Glyph("uni75DB", advance=1000, unicode=0x75DB, note="痛：疒＋甬。")

    # 疒
    g.dot(160, 780, w=W_DOT, h=110, slant=-14)     # 疒的点
    g.hbar(100, 430, 668, weight=W_MAIN)          # 疒的一
    g.diag(180, 640, 70, 120, weight=W_MAIN)      # 疒的长撇
    g.dot(320, 520, w=W_DOT, h=100, slant=-14)     # 冫·上点
    g.dot(300, 360, w=W_DOT, h=100, slant=14)      # 冫·下提

    # 甬
    g.hbar(480, 790, 706, weight=W_THIN)          # マ的横
    g.diag(790, 726, 690, 620, weight=W_THIN)     # マ的折
    g.dot(640, 660, w=W_DOT, h=100, slant=-14)     # マ的点
    _ri(g, 460, 900, 566, 140, 2)                 # 用（3 腔）
    g.vbar(680, 538, 196, weight=W_SEC)            # 用的中竖
    return g


def _fure():
    """触（13画）：角 + 虫。

    角（x 60..440）= ⺈ + 用型（两内横 + 中竖）；
    虫（x 470..940）= 口 + 中竖 + 底横 + 点。
    """
    g = Glyph("uni89E6", advance=1000, unicode=0x89E6, note="触：角＋虫。")

    # 角
    g.diag(290, 810, 165, 680, weight=W_THIN)     # ⺈·丿
    g.hbar(240, 420, 690, weight=W_THIN)          # ⺈·横
    g.diag(415, 700, 320, 630, weight=W_THIN)     # ⺈·横撇
    _ri(g, 70, 440, 550, 124, 2)                  # 角身（3 腔）
    g.vbar(255, 522, 180, weight=W_THIN)          # 角身中竖

    # 虫
    g.hbar(560, 860, 518, weight=W_THIN)          # 虫·口上横
    g.hbar(560, 860, 392, weight=W_THIN)          # 虫·口下横
    g.vbar(608, 532, 378, weight=W_MAIN)          # 虫·口左竖
    g.vbar(812, 532, 378, weight=W_MAIN)          # 虫·口右竖
    g.vbar(710, 520, 300, weight=W_SEC)           # 虫·中竖
    g.hbar(500, 900, 228, weight=W_MAIN)          # 虫·底横
    g.dot(892, 150, w=W_DOT, h=100, slant=-14)     # 虫·点
    return g


def _zoku():
    """属（12画，日语新字体）：尸 + 禹。

    码位说明：U+5C5E = 属（日语新字体，尸＋禹），U+5C6C 才是繁体「屬」。
    仓库冻结清单（joyo-batches.json / joyo-kanji-meta.json）记的也是
    「属 = U+5C5E」，故本字形按属 画，码位保持冻结值不变。
    禹 = 竖桩式起笔 + 田型块（4 腔）+ 厶。
    """
    g = Glyph("uni5C5E", advance=1000, unicode=0x5C5E, note="属：尸＋禹，日语新字体。")

    # 尸
    g.hbar(180, 660, 778, weight=W_THIN)          # 尸·横折的横
    g.vbar(618, 778, 640, weight=W_THIN)          # 尸·横折的竖
    g.hbar(180, 660, 666, weight=W_THIN)          # 尸·下横
    g.diag(200, 760, 70, 180, weight=W_MAIN)      # 尸·长撇

    # 禹
    g.vbar(640, 660, 500, weight=W_THIN)           # 禹·丿（竖桩式起笔，与中竖贯通）
    _tian(g, 380, 900, 542, 230, 640, 386)        # 禹·田型块（4 腔）
    g.diag(700, 250, 600, 130, weight=W_THIN)     # 厶·丿
    g.hbar(600, 740, 130, weight=W_THIN)          # 厶·折
    g.dot(770, 175, w=W_DOT, h=96, slant=-14)     # 厶·丶
    return g


def _shou():
    """笑（10画）：竹 + 夭。

    竹（x 60..860）两组「丿 + 一 + 丨」；夭（x 60..940）= 丿 + 一 + 大。
    """
    g = Glyph("uni7B11", advance=1000, unicode=0x7B11, note="笑：竹＋夭。")

    # 竹
    g.diag(180, 815, 95, 690, weight=W_THIN)      # 左·丿
    g.hbar(150, 330, 700, weight=W_THIN)          # 左·一
    g.vbar(285, 690, 590, weight=W_THIN)          # 左·丨
    g.diag(600, 815, 515, 690, weight=W_THIN)     # 右·丿
    g.hbar(570, 860, 700, weight=W_THIN)          # 右·一
    g.vbar(700, 690, 590, weight=W_THIN)          # 右·丨

    # 夭
    g.diag(560, 600, 300, 520, weight=W_THIN)     # 夭·丿
    g.hbar(150, 870, 472, weight=W_MAIN)          # 一
    g.diag(520, 440, 130, 90, weight=W_MAIN)      # 大·丿
    g.diag(520, 440, 880, 90, weight=W_MAIN)      # 大·捺
    return g


def _yuu():
    """郵（10画）：垂 + 阝。

    垂（x 60..510）= 丿 + 一 + 竖 + 二 + 二 + 竖；
    阝（x 540..830）= 竖 + 两折（呈「3」形）。
    """
    g = Glyph("uni90F5", advance=1000, unicode=0x90F5, note="郵：垂＋阝。")

    # 垂
    g.diag(350, 810, 180, 745, weight=W_THIN)     # 丿
    g.hbar(140, 470, 742, weight=W_MAIN)          # 一
    g.vbar(300, 720, 320, weight=W_MAIN)          # 竖
    g.hbar(140, 290, 582, weight=W_THIN)          # 二·左
    g.hbar(310, 470, 582, weight=W_THIN)          # 二·右
    g.hbar(140, 470, 442, weight=W_THIN)          # 一（横）
    g.hbar(70, 510, 298, weight=W_MAIN)           # 底横

    # 阝
    g.vbar(640, 750, 130, weight=W_THIN)           # 竖
    g.hbar(640, 820, 730, weight=W_THIN)          # 上折
    g.vbar(778, 730, 580, weight=W_THIN)          # 上折竖
    g.hbar(640, 778, 600, weight=W_THIN)          # 中折
    g.vbar(778, 600, 420, weight=W_THIN)          # 下折竖
    g.hbar(640, 800, 440, weight=W_THIN)          # 下折
    return g


def _megumi():
    """恵（10画）：十 + 田型框 + 心。

    田型框两行两列共 4 腔（净距 30）；心 = 乚（带钩）+ 三点（−14）。
    """
    g = Glyph("uni6075", advance=1000, unicode=0x6075, note="恵：十＋田＋心。")

    g.vbar(500, 820, 680, weight=W_MAIN)           # 十的竖
    g.hbar(190, 810, 652, weight=W_MAIN)           # 十的一
    _tian(g, 240, 760, 560, 248, 500, 404)         # 田型框（4 腔）

    # 心
    g.vbar(360, 190, 110, weight=W_THIN)           # 乚·竖
    g.hbar(360, 640, 152, weight=W_THIN)           # 乚·底
    g.vbar(630, 150, 240, weight=W_THIN)           # 乚·钩
    g.dot(215, 170, w=W_DOT, h=100, slant=-14)     # 心·左点
    g.dot(495, 180, w=W_DOT, h=118, slant=-14)     # 心·中点
    g.dot(760, 150, w=W_DOT, h=100, slant=-14)     # 心·右点
    return g


def _tanzan():
    """探（11画）：扌 + 罙。

    扌用批内共用坐标；罙（x 350..940）= 冖 + 八 + 木。
    """
    g = Glyph("uni63A2", advance=1000, unicode=0x63A2, note="探：扌＋罙。")

    _te(g)

    _wei(g, 390, 900, 750)                        # 冖
    g.diag(540, 680, 450, 530, weight=W_THIN)     # 八·丿
    g.diag(690, 680, 780, 530, weight=W_THIN)     # 八·捺
    _mu_glyph(g, 640, 458, 60, 380, 900)          # 木
    return g


def _kari():
    """借（10画）：亻 + 昔。

    亻用批内共用坐标；昔（x 350..940）= 廿 + 日。
    """
    g = Glyph("uni501F", advance=1000, unicode=0x501F, note="借：亻＋昔。")

    _ren(g)

    # 昔
    g.hbar(380, 900, 722, weight=W_MAIN)          # 廿·顶
    g.vbar(460, 700, 560, weight=W_THIN)           # 廿·左竖
    g.vbar(820, 700, 560, weight=W_THIN)           # 廿·右竖
    g.hbar(380, 900, 602, weight=W_THIN)          # 廿·底
    _ri(g, 440, 860, 420, 108, 1)                 # 日（2 腔）
    return g


def _fushi():
    """節（13画）：竹 + 即。

    竹（x 60..940）两组；即（x 60..940）= 皀（丿 + 日 + 匕）+ 卩。
    """
    g = Glyph("uni7BC0", advance=1000, unicode=0x7BC0, note="節：竹＋即。")

    # 竹
    g.diag(230, 818, 130, 690, weight=W_THIN)     # 左·丿
    g.hbar(180, 400, 700, weight=W_THIN)          # 左·一
    g.vbar(355, 690, 590, weight=W_THIN)          # 左·丨
    g.diag(700, 818, 600, 690, weight=W_THIN)     # 右·丿
    g.hbar(650, 900, 700, weight=W_THIN)          # 右·一
    g.vbar(855, 690, 590, weight=W_THIN)          # 右·丨

    # 即·皀
    g.diag(310, 560, 170, 490, weight=W_THIN)     # 皀·丿
    _ri(g, 140, 400, 470, 158, 1)                 # 皀·日
    g.diag(285, 180, 185, 80, weight=W_THIN)      # 匕·丿
    g.vbar(340, 160, 60, weight=W_THIN)           # 匕·竖
    g.hbar(340, 440, 90, weight=W_THIN)           # 匕·底

    # 即·卩
    g.hbar(540, 700, 470, weight=W_THIN)          # 卩·横
    g.vbar(658, 470, 330, weight=W_THIN)           # 卩·折
    g.diag(645, 340, 600, 382, weight=W_THIN)     # 卩·钩
    g.vbar(540, 490, 40, weight=W_THIN)           # 卩·竖
    return g


def _hone():
    """骨（10画）：冎 + 月。

    冎（x 200..780）= 冂 + 口；月（x 180..860）= 丿 + 𠃍 + 两内横。
    """
    g = Glyph("uni9AA8", advance=1000, unicode=0x9AA8, note="骨：冎＋月。")

    # 冎
    g.hbar(220, 780, 770, weight=W_THIN)          # 冂·横
    g.vbar(262, 770, 560, weight=W_THIN)           # 冂·左竖
    _kou(g, 400, 680, 700, 508)                   # 冎·口

    # 月
    g.hbar(220, 830, 438, weight=W_THIN)          # 月·横
    g.vbar(788, 438, 100, weight=W_THIN)          # 月·右竖
    g.diag(262, 438, 200, 60, weight=W_THIN)      # 月·左撇
    g.diag(775, 112, 730, 156, weight=W_THIN)     # 月·钩
    g.hbar(270, 788, 324, weight=W_THIN)          # 月·内横一
    g.hbar(270, 788, 210, weight=W_THIN)          # 月·内横二
    return g


def _sha():
    """射（10画）：身 + 寸。

    身（x 60..500）= 丿 + 竖 + 横折 + 三内横 + 长撇；
    寸（x 520..940）= 一 + 亅（带钩）+ 点。
    """
    g = Glyph("uni5C04", advance=1000, unicode=0x5C04, note="射：身＋寸。")

    # 身
    g.diag(370, 800, 250, 720, weight=W_THIN)     # 丿
    g.vbar(150, 730, 240, weight=W_THIN)           # 竖
    g.hbar(150, 440, 730, weight=W_THIN)          # 横折的横
    g.vbar(398, 730, 200, weight=W_THIN)           # 横折的竖
    g.hbar(180, 398, 620, weight=W_THIN)          # 内横一
    g.hbar(180, 398, 510, weight=W_THIN)          # 内横二
    g.hbar(180, 398, 400, weight=W_THIN)          # 内横三
    g.diag(200, 380, 80, 120, weight=W_THIN)      # 长撇

    # 寸
    g.hbar(520, 900, 648, weight=W_MAIN)          # 一
    g.vbar(790, 650, 160, weight=W_MAIN)          # 亅
    g.diag(780, 172, 735, 216, weight=W_THIN)     # 钩
    g.dot(640, 480, w=W_DOT, h=110, slant=-14)     # 点
    return g


def _keii():
    """傾（13画）：亻 + 頃。

    亻用批内共用坐标；頃（x 330..940）= 匕 + 頁（目 + 八）。
    """
    g = Glyph("uni50BE", advance=1000, unicode=0x50BE, note="傾：亻＋頃。")

    _ren(g)

    # 匕
    g.diag(440, 790, 340, 660, weight=W_THIN)     # 丿
    g.vbar(370, 690, 500, weight=W_THIN)           # 竖
    g.hbar(370, 470, 542, weight=W_THIN)          # 底

    # 頁
    g.hbar(500, 930, 772, weight=W_MAIN)          # 一
    g.diag(790, 780, 660, 660, weight=W_SEC)      # 丿
    _ri(g, 540, 900, 620, 194, 2)                 # 目（3 腔）
    g.diag(650, 250, 540, 60, weight=W_MAIN)      # 八·撇
    g.diag(760, 250, 890, 60, weight=W_MAIN)      # 八·捺
    return g


def _yuu2():
    """遊（11画）：辶 + 斿。

    辶用批内共用坐标；斿（x 320..940）= 方 + 𠂉 + 子。
    """
    g = Glyph("uni904A", advance=1000, unicode=0x904A, note="遊：辶＋斿。")

    # 方
    g.dot(420, 800, w=W_DOT, h=90, slant=0)        # 竖点（0 档）
    g.hbar(330, 560, 742, weight=W_SEC)           # 一
    g.hbar(350, 530, 600, weight=W_THIN)          # 𠃌的横
    g.vbar(488, 600, 420, weight=W_THIN)           # 𠃌的竖
    g.diag(430, 620, 340, 330, weight=W_THIN)      # 丿

    # 𠂉
    g.diag(720, 800, 620, 680, weight=W_THIN)     # 丿
    g.hbar(680, 930, 690, weight=W_THIN)          # 一

    # 子
    g.hbar(640, 900, 580, weight=W_THIN)          # 乛的横
    g.diag(900, 600, 780, 500, weight=W_THIN)     # 乛的撇
    g.vbar(790, 560, 300, weight=W_THIN)          # 丨
    g.hbar(620, 930, 422, weight=W_SEC)           # 一

    _mokuji(g)
    return g


def _yume():
    """夢（13画）：艹 + 罒 + 冖 + 夕。

    艹顶横 ink 736..820；罒三腔；冖横 ink 410..494；夕 = 丿 + 横撇 + 点。
    """
    g = Glyph("uni5922", advance=1000, unicode=0x5922, note="夢：艹＋罒＋冖＋夕。")

    # 艹
    g.hbar(130, 870, 778, weight=W_THIN)          # 艹·横
    g.vbar(330, 778, 640, weight=W_THIN)           # 艹·左竖
    g.vbar(670, 778, 640, weight=W_THIN)           # 艹·右竖

    # 罒
    _si(g, 250, 750, 712, 506, [435, 566], wh=W_THIN, wv=W_THIN)

    # 冖
    g.hbar(180, 820, 436, weight=W_THIN)          # 冖·横
    g.vbar(222, 436, 380, weight=W_THIN)           # 冖·左竖
    g.vbar(778, 436, 380, weight=W_THIN)           # 冖·右竖

    # 夕
    g.diag(620, 420, 420, 230, weight=W_THIN)     # 夕·丿
    g.hbar(460, 790, 328, weight=W_THIN)          # 夕·横
    g.diag(790, 350, 620, 210, weight=W_THIN)      # 夕·横撇
    g.dot(640, 270, w=W_DOT, h=100, slant=-14)     # 夕·点
    return g


def _ki2():
    """揮（12画）：扌 + 軍。

    扌用批内共用坐标；軍（x 350..940）= 冖 + 車（一 + 日 + 一 + 中竖）。
    """
    g = Glyph("uni63EE", advance=1000, unicode=0x63EE, note="揮：扌＋軍。")

    _te(g)

    _wei(g, 380, 900, 760)                        # 冖
    g.hbar(400, 880, 642, weight=W_SEC)           # 車·上横
    _ri(g, 440, 840, 560, 248, 1)                 # 車·日（2 腔）
    g.vbar(640, 600, 190, weight=W_THIN)          # 車·中竖
    g.hbar(400, 880, 166, weight=W_SEC)           # 車·底横
    return g


# ---------------------------------------------------------------- 装配

def build() -> list[Glyph]:
    return [
        _tou(), _sou(), _en(), _gai(), _kai(), _etsu(),
        _kei(), _ki(), _yoku(), _itai(), _fure(), _zoku(),
        _shou(), _yuu(), _megumi(), _tanzan(), _kari(), _fushi(),
        _hone(), _sha(), _keii(), _yuu2(), _yume(), _ki2(),
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s3-013.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
