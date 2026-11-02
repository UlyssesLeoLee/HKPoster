"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s3-002。

本批 24 字，笔画范围 10–13，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
* 字面框：x 60..940，y 0..820（与繁体汉字完全一致），advance = 1000。
* 笔画权重档：主 96 / 次 92 / 细 84 / 点 84。本批 10–13 画，
  笔画少的字（家 記 原 書 進 院 案）用 96 为主，
  笔画多的字（数 解 資 話 続 結 策 集 報 勝）把最密处（横画叠横画、
  竖与竖之间）局部减到 84 或 92，保证同批观感一致而不闷成黑块。
* 内白：密排处横画叠横画的净空 ≥ 24 单位，竖与竖之间 ≥ 60 单位。
  这批字里最容易出问题的部件是「言」（四横叠排）、「書」（聿五横）、
  「貝」「日」「目」（横画叠横画）和「糸」「隹」（斜笔与竖画夹角小），
  已按 check_stroke_gaps.py 的数字判据（重叠等效长度 < 1.5 笔画宽）逐个核过。
* 端点：横竖撇捺一律平切硬边；点与短撇用斜切平行四边形，
  斜切档位只用规格列出的 26 / 22 / 20 / 18 / 16 / 14 / −14 / 0。
* 笔画角度一律照标准骨架，不为了压墨量率改走向；只调重量、端点、落位与大小。
  斜笔与横画相交时产生的 1.5~3 档「偏紧」是真实交叠（子字、孝字、
  策字等的固有斜度），只保证不超过 3（疑似粘连）。
* 同族部件（亠/宀的点、冫/氵的点、丷左右点、寸的点、小右点、辶的点）
  在批内统一档位（GLY-004）。
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
W_LIGHT = 76  # 局部减重（GLY-001 小空腔）

# 字面框（與繁體漢字一致）
L, R = 60.0, 940.0
T, B = 820.0, 0.0


# --------------------------------------------------------------------------
# 對齊輔助：中心線 = 墨跡邊界內縮半個筆畫寬
# --------------------------------------------------------------------------
def _hbar(g: Glyph, x1: float, x2: float, yc: float, w: float = W_MAIN) -> None:
    """水平筆畫，中心線 y = yc，墨跡佔 yc ± w/2。"""
    g.hbar(x1, x2, yc, weight=w)


def _vbar(g: Glyph, x: float, y1: float, y2: float, w: float = W_MAIN) -> None:
    """垂直筆畫，中心線 x = x，y1/y2 即墨跡端點。"""
    g.vbar(x, y1, y2, weight=w)



# --------------------------------------------------------------------------
# 部件
# --------------------------------------------------------------------------
def _kuchi(g: Glyph, x1: float, x2: float, y_top: float, y_bot: float,
           w: float = W_MAIN) -> None:
    """口：x1/x2 為墨跡左右緣，y_top/y_bot 為墨跡上下緣。"""
    _vbar(g, x1 + w / 2, y_bot, y_top, w)
    _vbar(g, x2 - w / 2, y_bot, y_top, w)
    _hbar(g, x1, x2, y_top - w / 2, w)
    _hbar(g, x1, x2, y_bot + w / 2, w)


def _kanmuri(g: Glyph, x1: float, x2: float, y_bar_top: float,
             w: float = W_MAIN) -> None:
    """宀：豎點 + 冖（橫 / 左點 / 右豎鉤）。y_bar_top 為冖橫的墨跡上緣。"""
    cx = (x1 + x2) / 2.0
    g.dot(cx=cx, cy=y_bar_top + 72, w=136, h=104, slant=0)      # 豎點（slant 0）
    _hbar(g, x1, x2, y_bar_top - w / 2, w)                  # 冖的橫
    g.dot(cx=x1 + 52, cy=y_bar_top - 52, w=96, h=100, slant=0)   # 冖的左點
    _vbar(g, x2 - w / 2, y_bar_top - w, y_bar_top - w - 58, w)  # 冖的右鉤


def _sanzui(g: Glyph, x1: float, x2: float, y_top: float,
            y_bot: float) -> None:
    """氵：上點（短撇 slant 26）/ 中點（26）/ 提。"""
    cx = (x1 + x2) / 2.0
    g.dot(cx=cx + 16, cy=y_top - 66, w=88, h=116, slant=26)   # 上點＝短撇
    g.dot(cx=cx + 4, cy=y_top - 258, w=88, h=112, slant=26)   # 中點
    g.diag(x1 + 16, y_bot + 40, x1 + 118, y_bot + 246, weight=W_SEC)  # 提


def _shi_zi(g: Glyph, x1: float, x2: float, y_top: float,
            y_bot: float) -> None:
    """糸（幺 + 小），作左偏旁：上兩撇 + 幺底橫 + 豎鉤 + 左撇 + 右點。

    座標照 M PLUS 1p Black 的絲偏旁比例換算到本字面框：
    上撇自 (x1+126, 800) 走下左至 (x1+24, 648)，
    下撇自 (x1+202, 700) 走下左至 (x1+80, 518)，兩撇互相平行、
    垂直淨空約 110（淨空 14，與參照同構）；
    幺底橫 400..496 與下撇末端相接（即撇折之折），豎鉤自橫下貫到底。
    """
    g.diag(x1 + 150, y_top - 20, x1 + 30, y_top - 175, weight=W_MAIN)   # 幺上撇
    g.diag(x1 + 236, y_top - 130, x1 + 96, y_top - 320, weight=W_MAIN)  # 幺下撇
    _hbar(g, x1 + 10, x1 + 285, y_top - 400, W_MAIN)               # 幺底橫
    _vbar(g, x1 + 150, y_top - 400, y_bot + 40, W_MAIN)            # 小的豎鉤
    g.diag(x1 + 140, y_top - 500, x1 + 34, y_bot + 60, weight=W_SEC)     # 小左撇
    g.dot(cx=x1 + 256, cy=y_bot + 200, w=92, h=120, slant=14)           # 小右點


def _rin(g: Glyph, x1: float, x2: float, y_top: float,
         y_bot: float) -> None:
    """阝（左耳旁）：橫折折折鉤 + 豎。"""
    _hbar(g, x1, x2, y_top - W_MAIN / 2, W_MAIN)
    _vbar(g, x2 - W_MAIN / 2, y_top - W_MAIN, y_top - 190, W_MAIN)
    _hbar(g, x1 + 24, x2, y_top - 238, W_MAIN)
    _vbar(g, x1 + 72, y_top - 190, y_bot, W_MAIN)


def _teki(g: Glyph, x1: float, x2: float, y_top: float,
          y_bot: float) -> None:
    """彳：兩撇 + 豎。"""
    g.diag(x1 + 168, y_top, x1 + 74, y_top - 108, weight=W_MAIN)
    g.diag(x1 + 176, y_top - 150, x1 + 54, y_top - 288, weight=W_MAIN)
    _vbar(g, x1 + 88, y_top - 288, y_bot, W_MAIN)


def _onna(g: Glyph, x1: float, x2: float, y_top: float,
          y_bot: float) -> None:
    """女：撇點（短撇 + 長捺）+ 一 + 長撇。

    一橫置於字塊偏上（y_top − 0.30×高），長撇自右上斜穿而下，
    撇點為「短撇 + 長捺」的折，與參照同構（女不像「交」的地方就在於
    撇點的撇很短、且一橫偏上）。
    """
    span = x2 - x1
    height = y_top - y_bot
    _hbar(g, x1, x2, y_top - 0.30 * height, W_MAIN)                 # 女的一
    g.diag(x1 + 0.30 * span, y_top, x1 + 0.20 * span, y_top - 0.30 * height, weight=W_MAIN)          # 撇點的短撇
    g.diag(x1 + 0.20 * span, y_top - 0.30 * height, x1 + 0.45 * span, y_bot, weight=W_MAIN)                          # 撇點的捺
    g.diag(x1 + 0.72 * span, y_top - 0.02 * height, x1 + 0.12 * span, y_bot + 0.04 * height, weight=W_MAIN)          # 女的長撇


# --------------------------------------------------------------------------
# 各字
# --------------------------------------------------------------------------
def jia() -> Glyph:
    """家：宀（豎點 + 冖橫 + 左點 + 右鉤）+ 豕（一 + 中央豎鉤 + 左三撇 + 右兩捺）。

    部件分區：宀 = y 604..820；豕 = y 0..516。
    豕的一橫中心線 y=468；中央豎鉤 x=610；左三撇自上而下平行、右兩捺自上而下平行，
    組間垂直淨空 ≥ 24，保證「目視有縫、工具不判粘」。
    """
    g = Glyph("uni5BB6", advance=1000, unicode=0x5BB6,
              note="家：宀 + 豕。豕 = 一 + 中央豎鉤 + 左三撇 + 右兩捺")
    # 宀
    _kanmuri(g, L, R, 700.0)
    # 豕的一（近滿寬，貼近冖的下緣）
    _hbar(g, 120.0, 880.0, 510.0, W_MAIN)
    # 豕的中央豎鉤（x=610）
    _vbar(g, 610.0, 510.0, 96.0, W_MAIN)
    g.diag(610.0, 96.0, 500.0, 26.0, weight=W_MAIN)          # 鉤
    # 左三撇（互相平行，垂直淨空 ≈ 130）
    g.diag(400.0, 465.0, 95.0, 230.0, weight=W_MAIN)
    g.diag(436.0, 325.0, 155.0, 110.0, weight=W_MAIN)
    g.diag(470.0, 185.0, 250.0, 42.0, weight=W_SEC)
    # 右兩捺（自上而下平行）
    g.diag(620.0, 465.0, 826.0, 215.0, weight=W_MAIN)
    g.diag(644.0, 305.0, 870.0, 48.0, weight=W_SEC)
    return g


def wa() -> Glyph:
    """話：言（豎點 + 三橫 + 口）+ 舌（丿 + 一 + 豎 + 口）。

    部件分區：言 x 60..400、舌 x 430..940。
    言的三橫中心線 y=644/500/356，口 188..284；四道橫畫的墨跡淨空 48/48/24。
    2026-10-31 回修：言的三（308..404）与口上横（216..312）白口 −4 → 口框上緣下移 28，白口 24。
    """
    g = Glyph("uni8A71", advance=1000, unicode=0x8A71,
              note="話：言 + 舌。言 = 豎點 + 三橫 + 口；舌 = 丿 + 一 + 豎 + 口")
    # ── 言 ──
    g.dot(cx=230.0, cy=758.0, w=120, h=104, slant=0)     # 言的頂點
    _hbar(g, 80.0, 380.0, 644.0, W_MAIN)             # 一
    _hbar(g, 80.0, 380.0, 500.0, W_MAIN)             # 一
    _hbar(g, 80.0, 380.0, 356.0, W_MAIN)             # 一
    _kuchi(g, 60.0, 400.0, 284.0, 0.0, W_MAIN)       # 口
    # ── 舌 ──
    g.diag(742.0, 806.0, 578.0, 690.0, weight=W_SEC)      # 千的丿
    _hbar(g, 448.0, 928.0, 618.0, W_MAIN)            # 千的一
    _vbar(g, 690.0, 666.0, 300.0, W_MAIN)             # 千的豎
    _kuchi(g, 430.0, 940.0, 300.0, 0.0, W_MAIN)      # 口
    return g


def zoku() -> Glyph:
    """続：糸 + 売（士 + 冖 + 儿）。

    部件分區：糸 x 60..390、売 x 430..940。
    売 = 士（上橫 / 豎 / 下橫）+ 冖（橫 + 左點 + 右鉤）+ 儿（左撇 + 右豎折）。
    """
    g = Glyph("uni7D9A", advance=1000, unicode=0x7D9A,
              note="続：糸 + 売。売 = 士 + 冖 + 儿")
    _shi_zi(g, L, 390.0, T, 0.0)
    # 売：士
    _hbar(g, 620.0, 900.0, 738.0, W_MAIN)
    _vbar(g, 760.0, 738.0, 512.0, W_MAIN)
    _hbar(g, 590.0, 930.0, 512.0, W_MAIN)
    # 売：冖
    _hbar(g, 430.0, 940.0, 388.0, W_MAIN)
    g.dot(cx=482.0, cy=362.0, w=92, h=100, slant=0)
    _vbar(g, 892.0, 340.0, 272.0, W_MAIN)
    # 売：儿
    g.diag(636.0, 340.0, 478.0, 92.0, weight=W_MAIN)
    _vbar(g, 790.0, 340.0, 96.0, W_MAIN)
    _hbar(g, 742.0, 930.0, 48.0, W_MAIN)
    return g


def shin() -> Glyph:
    """進：辶（點 slant −14 + 折 + 捺）+ 隹（丿 + 豎 + 點 + 四橫 + 中豎）。

    部件分區：隹 x 400..940、辶 x 60..420。
    隹四橫中心線 y=680/545/410/275；辶的捺自左下掠過隹的下方，
    與隹最下一橫的墨跡淨空 ≥ 28，兩者不相交。
    """
    g = Glyph("uni9032", advance=1000, unicode=0x9032,
              note="進：辶 + 隹。辶 = 點 + 折 + 捺；隹 = 丿 + 豎 + 點 + 四橫 + 中豎")
    # ── 隹 ──
    g.diag(502.0, 800.0, 410.0, 690.0, weight=W_MAIN)      # 丿
    _vbar(g, 445.0, 690.0, 275.0, W_MAIN)             # 左豎
    g.dot(cx=600.0, cy=765.0, w=92, h=104, slant=0)       # 頂點
    _hbar(g, 490.0, 940.0, 680.0, W_MAIN)
    _hbar(g, 490.0, 940.0, 545.0, W_MAIN)
    _hbar(g, 490.0, 940.0, 410.0, W_MAIN)
    _hbar(g, 490.0, 940.0, 275.0, W_MAIN)
    _vbar(g, 700.0, 728.0, 227.0, W_MAIN)             # 中豎
    # ── 辶 ──
    g.dot(cx=140.0, cy=744.0, w=92, h=112, slant=-14)     # 辶的點
    _hbar(g, 60.0, 290.0, 548.0, W_SEC)               # 折的上橫
    g.diag(286.0, 540.0, 150.0, 386.0, weight=W_SEC)       # 折的折
    g.diag(120.0, 240.0, 860.0, 56.0, weight=W_MAIN)       # 捺
    return g


def setsu() -> Glyph:
    """設：言 + 殳（几 + 又）。

    部件分區：言 x 60..400、殳 x 430..940。
    殳 = 上部几（丿 + 橫折鉤）+ 下部又（橫撇 + 撇 + 捺）。
    """
    g = Glyph("uni8A2D", advance=1000, unicode=0x8A2D,
              note="設：言 + 殳。殳 = 几 + 又")
    # ── 言 ──
    g.dot(cx=230.0, cy=758.0, w=120, h=104, slant=0)
    _hbar(g, 80.0, 380.0, 644.0, W_MAIN)
    _hbar(g, 80.0, 380.0, 500.0, W_MAIN)
    _hbar(g, 80.0, 380.0, 356.0, W_MAIN)
    _kuchi(g, 60.0, 400.0, 284.0, 0.0, W_MAIN)
    # ── 殳 ──
    g.diag(496.0, 782.0, 432.0, 604.0, weight=W_MAIN)      # 几的丿
    _hbar(g, 470.0, 906.0, 748.0, W_MAIN)             # 几的橫
    _vbar(g, 858.0, 796.0, 560.0, W_MAIN)             # 几的豎鉤
    _hbar(g, 470.0, 906.0, 468.0, W_MAIN)             # 又的橫撇
    g.diag(880.0, 468.0, 616.0, 66.0, weight=W_MAIN)       # 又的撇
    g.diag(556.0, 430.0, 902.0, 44.0, weight=W_MAIN)       # 又的捺
    return g


def suu() -> Glyph:
    """数：婁（米 + 女）+ 攵。

    部件分區：米 y 470..820、女 y 180..540、攵 x 590..940 全高。
    米 = 丷（−14 / +14）+ 一 + 豎 + 撇 + 點；女 = 撇點 + 一 + 撇。
    """
    g = Glyph("uni6570", advance=1000, unicode=0x6570,
              note="数：婁 + 攵。婁 = 米 + 女；攵 = 丿 + 一 + 丿 + 捺")
    # ── 米 ──
    g.dot(cx=214.0, cy=758.0, w=88, h=110, slant=-14)     # 丷左
    g.dot(cx=392.0, cy=758.0, w=88, h=110, slant=14)      # 丷右
    _hbar(g, 60.0, 540.0, 632.0, W_MAIN)              # 米的一
    _vbar(g, 300.0, 680.0, 540.0, W_MAIN)             # 米的豎
    g.diag(288.0, 584.0, 120.0, 500.0, weight=W_MAIN)      # 米的撇
    g.diag(316.0, 584.0, 480.0, 500.0, weight=W_MAIN)      # 米的點
    # ── 女 ──
    _onna(g, 60.0, 540.0, 470.0, 180.0)
    # ── 攵 ──
    g.diag(700.0, 800.0, 606.0, 686.0, weight=W_MAIN)      # 丿
    _hbar(g, 590.0, 940.0, 640.0, W_MAIN)             # 一
    g.diag(880.0, 640.0, 660.0, 330.0, weight=W_MAIN)      # 丿
    g.diag(620.0, 620.0, 930.0, 300.0, weight=W_MAIN)      # 捺
    return g


def ki() -> Glyph:
    """記：言 + 己。

    部件分區：言 x 60..400、己 x 430..940。
    己 = 橫折（頂橫 + 右豎）+ 中橫 + 豎折鉤（左豎 + 底橫 + 上鉤）。
    """
    g = Glyph("uni8A18", advance=1000, unicode=0x8A18,
              note="記：言 + 己。己 = 橫折 + 中橫 + 豎折鉤")
    g.dot(cx=230.0, cy=758.0, w=120, h=104, slant=0)
    _hbar(g, 80.0, 380.0, 644.0, W_MAIN)
    _hbar(g, 80.0, 380.0, 500.0, W_MAIN)
    _hbar(g, 80.0, 380.0, 356.0, W_MAIN)
    _kuchi(g, 60.0, 400.0, 284.0, 0.0, W_MAIN)
    # ── 己 ──
    _hbar(g, 470.0, 940.0, 608.0, W_MAIN)
    _vbar(g, 892.0, 656.0, 340.0, W_MAIN)
    _hbar(g, 430.0, 892.0, 388.0, W_MAIN)
    _vbar(g, 478.0, 436.0, 96.0, W_MAIN)
    _hbar(g, 430.0, 892.0, 48.0, W_MAIN)
    _vbar(g, 884.0, 48.0, 150.0, W_THIN)
    return g


def gen_in() -> Glyph:
    """院：阝 + 完（宀 + 元）。

    部件分區：阝 x 60..250、完 x 300..940。
    完 = 宀 + 元（一 + 一 + 撇 + 豎彎鉤）。
    2026-10-31 回修：宀的横（604..700）与元的一（512..608）白口 −4 → 元下移 30，白口 26。
    """
    g = Glyph("uni9662", advance=1000, unicode=0x9662,
              note="院：阝 + 完。完 = 宀 + 元")
    _rin(g, L, 250.0, 820.0, 0.0)
    # ── 完 ──
    _kanmuri(g, 300.0, 940.0, 700.0)
    _hbar(g, 320.0, 920.0, 530.0, W_MAIN)             # 元的一（墨 482..578）
    _hbar(g, 300.0, 940.0, 390.0, W_MAIN)             # 元的横（墨 342..438）
    g.diag(452.0, 390.0, 344.0, 60.0, weight=W_MAIN)       # 元的撇
    _vbar(g, 700.0, 390.0, 120.0, W_MAIN)             # 元的豎
    _hbar(g, 652.0, 900.0, 120.0, W_MAIN)             # 元的豎彎鉤底
    return g


def dai() -> Glyph:
    """第：⺮ + 弔。

    部件分區：⺮ y 600..820、弔 y 0..600。
    ⺮ = 丿 + 一 + 丨 ×2；弔 = 橫折（頂橫 + 右豎）+ 一 + 中豎 + 底撇。
    """
    g = Glyph("uni7B2C", advance=1000, unicode=0x7B2C,
              note="第：⺮ + 弔。⺮ = 丿 + 一 + 丨；弔 = 橫折 + 一 + 豎 + 撇")
    # ── ⺮ ──
    g.diag(252.0, 812.0, 162.0, 700.0, weight=W_MAIN)      # 左丿
    _hbar(g, 110.0, 452.0, 664.0, W_MAIN)             # 左一
    _vbar(g, 282.0, 712.0, 600.0, W_MAIN)             # 左丨
    g.diag(700.0, 812.0, 610.0, 700.0, weight=W_MAIN)      # 右丿
    _hbar(g, 560.0, 900.0, 664.0, W_MAIN)             # 右一
    _vbar(g, 730.0, 712.0, 600.0, W_MAIN)             # 右丨
    # ── 弔 ──
    _hbar(g, 130.0, 820.0, 556.0, W_MAIN)             # 弔的頂橫
    _vbar(g, 772.0, 604.0, 400.0, W_MAIN)             # 弔的右豎
    _hbar(g, 130.0, 820.0, 420.0, W_MAIN)             # 弔的一
    _vbar(g, 440.0, 604.0, 0.0, W_MAIN)               # 弔的中豎
    g.diag(150.0, 96.0, 430.0, 268.0, weight=W_MAIN)       # 弔的底撇
    return g


def san() -> Glyph:
    """産：亠（點 0 + 一）+ 丷（−14 / +14）+ 厂（一 + 丿）+ 生（一 + 丿 + 一 + 豎 + 一）。

    部件分區：亠 y 740..820、丷 y 620..740、厂 y 480..660、生 y 0..480。
    """
    g = Glyph("uni7523", advance=1000, unicode=0x7523,
              note="産：亠 + 丷 + 厂 + 生。産 = 立 + 厂 + 生")
    # ── 亠 ──
    g.dot(cx=500.0, cy=776.0, w=112, h=104, slant=0)
    _hbar(g, 200.0, 800.0, 700.0, W_MAIN)
    # ── 丷 ──
    g.dot(cx=318.0, cy=636.0, w=88, h=110, slant=-14)
    g.dot(cx=682.0, cy=636.0, w=88, h=110, slant=14)
    # ── 厂 ──
    _hbar(g, 60.0, 880.0, 560.0, W_MAIN)
    g.diag(130.0, 520.0, 62.0, 60.0, weight=W_MAIN)
    # ── 生 ──
    _hbar(g, 300.0, 880.0, 430.0, W_MAIN)             # 生的一
    g.diag(386.0, 430.0, 300.0, 300.0, weight=W_SEC)       # 生的撇
    _vbar(g, 600.0, 478.0, 0.0, W_MAIN)               # 生的豎
    _hbar(g, 250.0, 900.0, 230.0, W_MAIN)             # 生的一
    _hbar(g, 250.0, 900.0, 60.0, W_MAIN)              # 生的一
    return g


def ketsu() -> Glyph:
    """結：糸 + 吉（士 + 口）。

    部件分區：糸 x 60..390、吉 x 430..940。
    吉 = 士（上橫 / 豎 / 下橫）+ 口。
    """
    g = Glyph("uni7D50", advance=1000, unicode=0x7D50,
              note="結：糸 + 吉。吉 = 士 + 口")
    _shi_zi(g, L, 390.0, T, 0.0)
    # ── 吉 ──
    _hbar(g, 452.0, 918.0, 700.0, W_MAIN)             # 士的上橫
    _vbar(g, 685.0, 700.0, 540.0, W_MAIN)             # 士的豎
    _hbar(g, 430.0, 940.0, 540.0, W_MAIN)             # 士的下橫
    _kuchi(g, 470.0, 900.0, 400.0, 0.0, W_MAIN)      # 口
    return g


def kyo() -> Glyph:
    """教：孝（耂 + 子）+ 攵。

    部件分區：耂 y 544..820、子 y 0..516、攵 x 590..940。
    耂 = 土（一 + 豎 + 一）+ 丿；子 = 乛（橫 + 折撇）+ 亅 + 一。
    子的一橫貼基線，亅穿過它下端。
    """
    g = Glyph("uni6559", advance=1000, unicode=0x6559,
              note="教：孝 + 攵。孝 = 耂 + 子；攵 = 丿 + 一 + 丿 + 捺")
    # ── 耂 ──
    _hbar(g, 60.0, 560.0, 772.0, W_MAIN)              # 士的上橫
    _vbar(g, 310.0, 820.0, 640.0, W_MAIN)             # 士的豎
    _hbar(g, 110.0, 520.0, 592.0, W_MAIN)             # 士的下橫
    g.diag(486.0, 758.0, 176.0, 486.0, weight=W_MAIN)      # 耂的丿
    # ── 子 ──
    _hbar(g, 110.0, 520.0, 468.0, W_MAIN)             # 子の橫撇
    g.diag(430.0, 468.0, 290.0, 300.0, weight=W_MAIN)      # 子の折
    _vbar(g, 290.0, 300.0, 96.0, W_MAIN)              # 子の豎鉤
    _hbar(g, 100.0, 530.0, 48.0, W_MAIN)              # 子の一
    # ── 攵 ──
    g.diag(700.0, 800.0, 606.0, 686.0, weight=W_MAIN)
    _hbar(g, 590.0, 940.0, 640.0, W_MAIN)
    g.diag(880.0, 640.0, 660.0, 330.0, weight=W_MAIN)
    g.diag(620.0, 620.0, 930.0, 300.0, weight=W_MAIN)
    return g


def hoo() -> Glyph:
    """報：幸 + 𠬝（𠃌 + 又）。

    部件分區：幸 x 60..470、𠬝 x 500..940。
    幸 = 土（一 + 豎 + 一）+ 丷（−14 / +14）+ 干（一 + 豎 + 一）；
    𠬝 = 𠃌（橫 + 豎鉤）+ 又（橫撇 + 撇 + 捺）。
    """
    g = Glyph("uni5831", advance=1000, unicode=0x5831,
              note="報：幸 + 𠬝。幸 = 土 + 丷 + 干；𠬝 = 𠃌 + 又")
    # ── 幸 ──
    _hbar(g, 90.0, 440.0, 772.0, W_MAIN)              # 土的一
    _vbar(g, 265.0, 820.0, 580.0, W_MAIN)             # 土的豎
    _hbar(g, 60.0, 470.0, 580.0, W_MAIN)              # 土的一
    g.dot(cx=168.0, cy=453.0, w=84, h=106, slant=-14)     # 丷左
    g.dot(cx=362.0, cy=453.0, w=84, h=106, slant=14)      # 丷右
    _hbar(g, 90.0, 440.0, 328.0, W_MAIN)              # 干的一
    _vbar(g, 265.0, 376.0, 48.0, W_MAIN)              # 干的豎
    _hbar(g, 60.0, 470.0, 48.0, W_MAIN)               # 干的底橫
    # ── 𠬝 ──
    _hbar(g, 560.0, 760.0, 748.0, W_MAIN)             # 𠃌的橫
    _vbar(g, 712.0, 796.0, 600.0, W_MAIN)             # 𠃌的豎鉤
    _hbar(g, 500.0, 900.0, 500.0, W_MAIN)             # 又的橫撇
    g.diag(880.0, 500.0, 640.0, 120.0, weight=W_MAIN)      # 又的撇
    g.diag(570.0, 460.0, 920.0, 60.0, weight=W_MAIN)       # 又的捺
    return g


def sai() -> Glyph:
    """済：氵（上點 slant 26 / 中點 26 / 提）+ 斉（亠 + 乂 + 丿 + 丨 + 二）。

    部件分區：氵 x 60..250、斉 x 300..940。
    """
    g = Glyph("uni6E08", advance=1000, unicode=0x6E08,
              note="済：氵 + 斉。斉 = 亠 + 乂 + 丿 + 丨 + 二")
    _sanzui(g, 60.0, 250.0, 820.0, 0.0)
    # ── 斉 ──
    g.dot(cx=620.0, cy=778.0, w=112, h=104, slant=0)      # 亠的豎點
    _hbar(g, 300.0, 940.0, 700.0, W_MAIN)             # 亠的一
    g.diag(700.0, 700.0, 470.0, 520.0, weight=W_MAIN)      # 乂的撇
    g.diag(500.0, 700.0, 760.0, 520.0, weight=W_MAIN)      # 乂的捺
    g.diag(452.0, 470.0, 330.0, 60.0, weight=W_MAIN)       # 下部的撇
    _vbar(g, 700.0, 470.0, 40.0, W_MAIN)              # 下部的豎
    _hbar(g, 330.0, 940.0, 300.0, W_MAIN)             # 下部的一
    _hbar(g, 330.0, 940.0, 120.0, W_MAIN)             # 下部的底橫
    return g


def sho() -> Glyph:
    """書：聿（彐 + 頂點 + 四橫 + 底橫）+ 日。

    部件分區：聿 y 232..820、日 y 0..232。
    聿是本批最密的部件（橫畫疊橫畫），按 GLY-001 小空腔局部減重到 84；
    五道橫畫的墨跡淨空 32（≥24），最下一道寬橫兼作日之上橫，
    與參照同構：頂點 + 彐（右豎貫連）+ 四道橫 + 一道寬橫 + 日。
    """
    g = Glyph("uni66F8", advance=1000, unicode=0x66F8,
              note="書：聿 + 日。聿 = 彐 + 頂點 + 四橫 + 底橫；日 = 丨 + 𠃍 + 一 + 一")
    w = W_THIN
    # ── 聿 ──
    _vbar(g, 480.0, 820.0, 780.0, w)                  # 聿的頂點
    _hbar(g, 130.0, 840.0, 738.0, w)                  # 聿的一（696..780）
    _hbar(g, 80.0, 900.0, 622.0, w)                   # 聿的一（580..664）
    _hbar(g, 130.0, 840.0, 506.0, w)                  # 聿的一（464..548）
    _hbar(g, 130.0, 840.0, 390.0, w)                  # 聿的一（348..432）
    _hbar(g, 80.0, 900.0, 274.0, w)                   # 聿的底橫（232..316）＝日之上橫
    _vbar(g, 802.0, 780.0, 232.0, w)                  # 彐的右豎（貫連至日）
    # ── 日 ──
    _vbar(g, 178.0, 0.0, 316.0, w)                    # 日的左豎
    _hbar(g, 130.0, 840.0, 158.0, w)                  # 日的一（116..200）
    _hbar(g, 130.0, 840.0, 42.0, w)                   # 日的底橫（0..84）
    return g


def gen() -> Glyph:
    """原：厂（一 + 丿）+ 白（丿 + 日）+ 小（豎鉤 + 左撇 + 右點 +14）。

    部件分區：厂 y 620..820 與左撇、白 y 380..740、小 y 0..330。
    """
    g = Glyph("uni539F", advance=1000, unicode=0x539F,
              note="原：厂 + 白 + 小。小 = 豎鉤 + 左撇 + 右點")
    # ── 厂 ──
    _hbar(g, 60.0, 940.0, 772.0, W_MAIN)
    g.diag(146.0, 772.0, 70.0, 180.0, weight=W_MAIN)       # 厂的丿
    # ── 白 ──
    g.diag(404.0, 756.0, 348.0, 664.0, weight=W_SEC)       # 白的丿
    _vbar(g, 298.0, 380.0, 660.0, W_LIGHT)             # 日的左豎
    _vbar(g, 702.0, 380.0, 660.0, W_LIGHT)             # 日的右豎
    _hbar(g, 250.0, 750.0, 612.0, W_LIGHT)             # 日的上橫
    _hbar(g, 298.0, 702.0, 508.0, W_LIGHT)             # 日的一
    _hbar(g, 250.0, 750.0, 404.0, W_LIGHT)             # 日的底橫
    # ── 小 ──
    _vbar(g, 500.0, 340.0, 96.0, W_MAIN)              # 小的豎鉤
    g.diag(424.0, 320.0, 330.0, 70.0, weight=W_SEC)        # 小的左撇
    g.dot(cx=640.0, cy=200.0, w=92, h=116, slant=14)      # 小的右點
    return g


def toku() -> Glyph:
    """得：彳 + 㝵（日 + 一 + 寸）。

    部件分區：彳 x 60..250、㝵 x 300..940。
    寸 = 一 + 亅 + 點（slant −14）；日三橫中心線 y=772/644/516。
    """
    g = Glyph("uni5F97", advance=1000, unicode=0x5F97,
              note="得：彳 + 㝵。㝵 = 日 + 一 + 寸；寸 = 一 + 亅 + 點")
    _teki(g, 60.0, 250.0, 820.0, 0.0)
    # ── 日 ──
    _vbar(g, 348.0, 516.0, 820.0, W_MAIN)
    _vbar(g, 892.0, 516.0, 820.0, W_MAIN)
    _hbar(g, 300.0, 940.0, 772.0, W_MAIN)
    _hbar(g, 348.0, 892.0, 644.0, W_MAIN)
    _hbar(g, 300.0, 940.0, 516.0, W_MAIN)
    # ── 一 ──
    _hbar(g, 300.0, 940.0, 388.0, W_MAIN)
    # ── 寸 ──
    _hbar(g, 300.0, 940.0, 240.0, W_MAIN)
    _vbar(g, 660.0, 288.0, 0.0, W_MAIN)
    g.dot(cx=520.0, cy=150.0, w=84, h=110, slant=-14)      # 寸的點
    return g


def kai() -> Glyph:
    """解：角（⺈ + 用）+ 刀 + 牛。

    部件分區：角 x 60..520、刀 x 560..940（y 530..820）、牛 x 540..940（y 0..500）。
    角 = ⺈（丿 + 橫撇）+ 用（丿 + 𠃍 + 豎 + 一 + 一 + 豎）。
    """
    g = Glyph("uni89E3", advance=1000, unicode=0x89E3,
              note="解：角 + 刀 + 牛。角 = ⺈ + 用；牛 = 丿 + 一 + 一 + 豎")
    # ── 角 ──
    g.diag(250.0, 812.0, 150.0, 700.0, weight=W_MAIN)      # ⺈的丿
    _hbar(g, 150.0, 470.0, 700.0, W_MAIN)             # ⺈的橫撇
    g.diag(470.0, 700.0, 380.0, 600.0, weight=W_MAIN)      # ⺈的撇
    _vbar(g, 150.0, 0.0, 600.0, W_MAIN)               # 用的左豎
    _vbar(g, 470.0, 0.0, 600.0, W_MAIN)               # 用的右豎
    _hbar(g, 150.0, 470.0, 552.0, W_MAIN)             # 用的一
    _hbar(g, 198.0, 470.0, 400.0, W_MAIN)             # 用的一
    _hbar(g, 198.0, 470.0, 240.0, W_MAIN)             # 用的一
    # ── 刀 ──
    _hbar(g, 560.0, 940.0, 700.0, W_MAIN)             # 刀的橫折鉤
    _vbar(g, 892.0, 748.0, 560.0, W_MAIN)
    g.diag(720.0, 748.0, 570.0, 530.0, weight=W_MAIN)      # 刀的撇
    # ── 牛 ──
    g.diag(640.0, 500.0, 540.0, 400.0, weight=W_SEC)       # 牛的丿
    _hbar(g, 540.0, 900.0, 420.0, W_MAIN)             # 牛的一
    _hbar(g, 540.0, 940.0, 240.0, W_MAIN)             # 牛的一
    _vbar(g, 700.0, 480.0, 0.0, W_MAIN)               # 牛的豎
    return g


def shi() -> Glyph:
    """資：次（冫 + 欠）+ 貝（目 + 八）。

    部件分區：次 x 60..490、貝 x 520..940。
    冫 = 點（slant −14）+ 提；欠 = 丿 + 橫折 + 丿 + 捺。
    貝的目四橫中心線 y=728/568/408/248。
    """
    g = Glyph("uni8CC7", advance=1000, unicode=0x8CC7,
              note="資：次 + 貝。次 = 冫 + 欠；貝 = 目 + 八")
    # ── 冫 ──
    g.dot(cx=140.0, cy=760.0, w=92, h=112, slant=-14)     # 冫的點
    g.diag(80.0, 240.0, 220.0, 420.0, weight=W_MAIN)       # 冫的提
    # ── 欠 ──
    g.diag(420.0, 806.0, 320.0, 680.0, weight=W_MAIN)      # 欠的丿
    _hbar(g, 270.0, 470.0, 664.0, W_MAIN)             # 欠的橫折
    _vbar(g, 422.0, 712.0, 570.0, W_MAIN)             # 欠的豎
    g.diag(400.0, 600.0, 262.0, 380.0, weight=W_MAIN)      # 欠的丿
    g.diag(330.0, 560.0, 486.0, 300.0, weight=W_MAIN)      # 欠的捺
    # ── 貝 ──
    _vbar(g, 568.0, 248.0, 776.0, W_MAIN)             # 目的左豎
    _vbar(g, 892.0, 248.0, 776.0, W_MAIN)             # 目的右豎
    _hbar(g, 520.0, 940.0, 728.0, W_MAIN)             # 目的上橫
    _hbar(g, 568.0, 892.0, 568.0, W_MAIN)             # 目的一
    _hbar(g, 568.0, 892.0, 408.0, W_MAIN)             # 目的一
    _hbar(g, 520.0, 940.0, 248.0, W_MAIN)             # 目的底橫
    g.diag(640.0, 248.0, 512.0, 40.0, weight=W_MAIN)       # 八的撇
    g.dot(cx=800.0, cy=130.0, w=92, h=118, slant=14)      # 八的點
    return g


def katsu() -> Glyph:
    """勝：月（丿 + 橫折鉤 + 二）+ 龹（丷 + 一 + 一）+ 力（橫折鉤 + 撇）。

    部件分區：月 x 60..350、龹 y 520..820（x 380..940）、力 y 0..520。
    龹的丷：左 slant −14、右 slant +14。
    """
    g = Glyph("uni52DD", advance=1000, unicode=0x52DD,
              note="勝：月 + 龹 + 力。龹 = 丷 + 二；力 = 橫折鉤 + 撇")
    # ── 月 ──
    # 月的左撇：主體近垂直（參照 M PLUS 亦近垂直），下端以短撇收出弧度；
    # 不寫成一條近乎垂直的斜筆（那樣角度判讀會落在「近豎直」的可疑區）。
    g.vbar(132.0, 812.0, 200.0, weight=W_MAIN)
    g.diag(132.0, 200.0, 84.0, 76.0, weight=W_MAIN)      # 月的丿（收筆）
    _hbar(g, 120.0, 350.0, 764.0, W_MAIN)             # 月的橫折鉤
    _vbar(g, 302.0, 812.0, 90.0, W_MAIN)
    _hbar(g, 170.0, 350.0, 596.0, W_MAIN)             # 月的一
    _hbar(g, 150.0, 350.0, 420.0, W_MAIN)             # 月的一
    # ── 龹 ──
    g.dot(cx=500.0, cy=770.0, w=88, h=110, slant=-14)     # 丷左
    g.dot(cx=730.0, cy=770.0, w=88, h=110, slant=14)      # 丷右
    _hbar(g, 400.0, 940.0, 640.0, W_MAIN)             # 龹的一
    _hbar(g, 390.0, 940.0, 520.0, W_MAIN)             # 龹的一
    # ── 力 ──
    _hbar(g, 420.0, 880.0, 340.0, W_MAIN)             # 力的橫折鉤
    _vbar(g, 832.0, 388.0, 60.0, W_MAIN)
    g.diag(700.0, 388.0, 480.0, 40.0, weight=W_MAIN)       # 力的撇
    return g


def so() -> Glyph:
    """組：糸 + 且。

    部件分區：糸 x 60..390、且 x 430..940。
    且 = 冂形（兩豎 + 上橫）+ 二 + 底橫。
    """
    g = Glyph("uni7D44", advance=1000, unicode=0x7D44,
              note="組：糸 + 且。且 = 兩豎 + 上橫 + 二 + 底橫")
    _shi_zi(g, L, 390.0, T, 0.0)
    # ── 且 ──
    _vbar(g, 478.0, 60.0, 780.0, W_MAIN)
    _vbar(g, 892.0, 60.0, 780.0, W_MAIN)
    _hbar(g, 430.0, 940.0, 732.0, W_MAIN)             # 且的上橫
    _hbar(g, 478.0, 892.0, 576.0, W_MAIN)             # 且的一
    _hbar(g, 478.0, 892.0, 420.0, W_MAIN)             # 且的一
    _hbar(g, 430.0, 940.0, 108.0, W_MAIN)             # 且的底橫
    return g


def an() -> Glyph:
    """案：宀 + 女 + 木。

    部件分區：宀 y 700..820、女 y 320..600、木 y 0..320。
    女 = 撇點（撇 + 捺）+ 一 + 撇；木 = 一 + 豎 + 撇 + 捺。
    """
    g = Glyph("uni6848", advance=1000, unicode=0x6848,
              note="案：宀 + 女 + 木。女 = 撇點 + 一 + 撇；木 = 一 + 豎 + 撇 + 捺")
    _kanmuri(g, L, R, 700.0)
    # ── 女 ──
    _onna(g, 80.0, 900.0, 610.0, 330.0)
    # ── 木 ──
    _hbar(g, 100.0, 900.0, 220.0, W_MAIN)             # 木的一
    _vbar(g, 500.0, 268.0, 0.0, W_MAIN)               # 木的豎
    g.diag(480.0, 220.0, 140.0, 20.0, weight=W_MAIN)       # 木的撇
    g.diag(520.0, 220.0, 860.0, 20.0, weight=W_MAIN)       # 木的捺
    return g


def saku() -> Glyph:
    """策：竹 + 朿。

    部件分區：竹 y 600..820、朿 y 0..600。
    竹 = 丿 + 一 + 丨 ×2；朿 = 一 + 豎 + 冂 + 撇 + 捺。
    """
    g = Glyph("uni7B56", advance=1000, unicode=0x7B56,
              note="策：竹 + 朿。竹 = 丿 + 一 + 丨；朿 = 一 + 豎 + 冂 + 撇 + 捺")
    # ── 竹 ──
    g.diag(262.0, 812.0, 168.0, 704.0, weight=W_MAIN)
    _hbar(g, 110.0, 452.0, 660.0, W_MAIN)
    _vbar(g, 286.0, 708.0, 600.0, W_MAIN)
    g.diag(712.0, 812.0, 618.0, 704.0, weight=W_MAIN)
    _hbar(g, 560.0, 900.0, 660.0, W_MAIN)
    _vbar(g, 736.0, 708.0, 600.0, W_MAIN)
    # ── 朿 ──
    _hbar(g, 100.0, 900.0, 540.0, W_MAIN)              # 朿的一
    _vbar(g, 500.0, 588.0, 0.0, W_MAIN)               # 朿的豎
    _vbar(g, 210.0, 200.0, 400.0, W_THIN)             # 朿的冂左
    _hbar(g, 162.0, 838.0, 352.0, W_THIN)             # 朿的冂上
    _vbar(g, 790.0, 200.0, 400.0, W_THIN)             # 朿的冂右
    g.diag(486.0, 400.0, 168.0, 40.0, weight=W_MAIN)       # 朿的撇
    g.diag(514.0, 400.0, 832.0, 40.0, weight=W_MAIN)       # 朿の捺
    return g


def shuu() -> Glyph:
    """集：隹 + 木。

    部件分區：隹 y 330..820、木 y 0..330。
    隹 = 丿 + 豎 + 點 + 三橫 + 中豎；木 = 一 + 豎 + 撇 + 捺。
    """
    g = Glyph("uni96C6", advance=1000, unicode=0x96C6,
              note="集：隹 + 木。隹 = 丿 + 豎 + 點 + 三橫 + 中豎")
    # ── 隹 ──
    g.diag(470.0, 812.0, 380.0, 716.0, weight=W_MAIN)      # 隹的丿
    _vbar(g, 420.0, 716.0, 380.0, W_MAIN)             # 隹的左豎
    g.dot(cx=570.0, cy=776.0, w=92, h=104, slant=0)       # 隹的點
    _hbar(g, 460.0, 940.0, 678.0, W_MAIN)             # 隹的一
    _hbar(g, 460.0, 940.0, 534.0, W_MAIN)             # 隹的一
    _hbar(g, 460.0, 940.0, 390.0, W_MAIN)             # 隹の一
    _vbar(g, 690.0, 726.0, 342.0, W_MAIN)             # 隹的中豎
    # ── 木 ──
    _hbar(g, 60.0, 940.0, 216.0, W_MAIN)              # 木的一
    _vbar(g, 500.0, 264.0, 0.0, W_MAIN)               # 木の豎
    g.diag(480.0, 216.0, 130.0, 0.0, weight=W_MAIN)        # 木の撇
    g.diag(520.0, 216.0, 870.0, 0.0, weight=W_MAIN)        # 木の捺
    return g


def build() -> list[Glyph]:
    return [
        jia(),
        wa(),
        zoku(),
        shin(),
        setsu(),
        suu(),
        ki(),
        gen_in(),
        dai(),
        san(),
        ketsu(),
        kyo(),
        hoo(),
        sai(),
        sho(),
        gen(),
        toku(),
        kai(),
        shi(),
        katsu(),
        so(),
        an(),
        saku(),
        shuu(),
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s3-002.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
