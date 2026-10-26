"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-019。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
* 字面框：x 60..940，y 0..820，advance 1000（与繁体汉字完全一致）。
* 笔画权重：主 96 / 次 92 / 细 84 / 点 84。
  横竖撇捺一律平切硬边（`hbar` / `vbar` / `diag` 的 cut 全为 0）；
  点与短撇一律用斜切平行四边形（`dot`），slant 只取既有档位
  26 / 22 / 20 / 18 / 16 / 14 / −14 / 0，不自造档位。
* 同族观感（GLY-004）：扌 / 氵 / 忄 / 亻 / 女 / 月 / 山 / 口 / 木 / 土 / 方 /
  夹 / 夫 / 失 / 辶 等部件在批内复用同一套拆法与坐标，只做位置与大小的
  光学校正；同一部件在批内共用同一组实现函数。
* 笔画角度照标准骨架画（比例与骨架参照 M PLUS 1p Black 与
  Zen Kaku Gothic New Black，均 SIL OFL 1.1；不描轮廓）。斜画与横画交叠时
  角度保持 ≥30°；内白用 `check_stroke_gaps.py` 的数字核对，不靠目测。
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

X_L = 60.0          # 字面框左缘
X_R = 940.0         # 字面框右缘
Y_B = 0.0           # 字面框下缘
Y_T = 820.0         # 字面框上缘

# slant 分档（与既有字族一致，禁止自造）
SL_SHORT_PIE = 26   # 短撇（氵上点）
SL_DOT = -14        # 丶（辶的点 / 寸的点 / 丷左 / 小左点）
SL_PIE = 14         # 丿（丷右 / 小右点）
SL_VERT = 0         # 竖点（亠的点）


# ---------------------------------------------------------------------------
# 基础笔画辅助
# ---------------------------------------------------------------------------

def _diag(g: Glyph, ax: float, ay: float, bx: float, by: float,
          w: float = W_MAIN) -> None:
    """斜画：中心线自 (ax,ay) 到 (bx,by)。

    墨迹沿**垂直于中心线**展开：墨迹外接框比中心线盒每边多出
    w/2·|uy|（横向）与 w/2·|ux|（纵向）。因此斜画落位时必须把这两个
    外扩量算进去，否则会越出字面框。
    """
    g.diag(ax, ay, bx, by, weight=w)


def _dot(g: Glyph, cx: float, cy: float, w: float = W_DOT, h: float = 110,
         slant: float = 0) -> None:
    """点 / 短撇：斜切平行四边形（cx,cy 为形心）。

    slant > 0 → 顶边右移，笔画走「下左」（丿向）；
    slant < 0 → 顶边左移，笔画走「下右」（丶向）。
    """
    g.dot(cx, cy, w=w, h=h, slant=slant)


# ---------------------------------------------------------------------------
# 复用部件（批内统一拆法与坐标）
# ---------------------------------------------------------------------------

def _kuchi(g: Glyph, x0: float, y0: float, x1: float, y1: float,
           w: float = W_MAIN) -> None:
    """口：左竖 + 右竖 + 顶横 + 底横，墨迹框 (x0,y0)-(x1,y1)。"""
    g.vbar(x0 + w / 2, y0, y1, weight=w)
    g.vbar(x1 - w / 2, y0, y1, weight=w)
    g.hbar(x0, x1, y1 - w / 2, weight=w)
    g.hbar(x0, x1, y0 + w / 2, weight=w)


def _moon(g: Glyph, x0: float, y0: float, x1: float, y1: float,
          w: float = W_MAIN) -> None:
    """月：左竖 + 顶横 + 右竖 + 两道内横 + 底横（底横即左撇的收笔）。

    两道内横走 84 细档（拥挤处局部减重），外框与底横留 96。
    """
    h = y1 - y0
    g.vbar(x0 + w / 2, y0, y1, weight=w)
    g.vbar(x1 - w / 2, y0, y1, weight=w)
    g.hbar(x0, x1, y1 - w / 2, weight=w)
    g.hbar(x0, x1, y0 + w / 2, weight=w)
    g.hbar(x0, x1, y1 - h * 0.34, weight=W_THIN)
    g.hbar(x0, x1, y0 + h * 0.34, weight=W_THIN)


def _yama(g: Glyph, x0: float, y0: float, x1: float, y1: float,
          w: float = W_THIN) -> None:
    """山：中竖 + 左竖 + 右竖 + 底横（三竖用 84 细档，保证竖间内白）。"""
    h = y1 - y0
    xc = x0 + (x1 - x0) / 2
    g.vbar(xc, y1, y0, weight=w)
    g.vbar(x0 + w / 2, y1 - h * 0.40, y0, weight=w)
    g.vbar(x1 - w / 2, y1 - h * 0.40, y0, weight=w)
    g.hbar(x0, x1, y0 + w / 2, weight=w)


def _tehen(g: Glyph, x0: float, y0: float, x1: float, y1: float,
           w: float = W_MAIN) -> None:
    """扌：竖（带左钩）+ 横 + 提。"""
    h = y1 - y0
    wd = x1 - x0
    xv = x0 + wd * 0.42
    g.vbar(xv, y1, y0 + w / 2, weight=w)
    g.hbar(xv - wd * 0.26, xv, y0 + w / 2, weight=w)
    g.hbar(x0, x1, y1 - h * 0.30, weight=w)
    _diag(g, x0 + 45, y0 + h * 0.38, xv + 8, y0 + h * 0.17, w=w)


def _sanzui(g: Glyph, x0: float, y0: float, x1: float, y1: float,
            w: float = W_MAIN) -> None:
    """氵：上点（短撇）+ 中点（丶）+ 提。三笔都偏小，放大到 120 高以免整字发飘。"""
    h = y1 - y0
    wd = x1 - x0
    _dot(g, x0 + wd * 0.50, y1 - h * 0.10, w=W_DOT, h=120,
         slant=SL_SHORT_PIE)
    _dot(g, x0 + wd * 0.38, y1 - h * 0.42, w=W_DOT, h=120, slant=SL_DOT)
    _diag(g, x0 + 35, y0 + h * 0.06, x0 + wd * 0.92, y0 + h * 0.30, w=w)


def _ritsu(g: Glyph, x0: float, y0: float, x1: float, y1: float,
           w: float = W_MAIN) -> None:
    """忄：中竖 + 左点（丶）+ 右点（丿）。"""
    h = y1 - y0
    wd = x1 - x0
    xc = x0 + wd / 2
    g.vbar(xc, y1, y0, weight=w)
    _dot(g, x0 + wd * 0.20, y1 - h * 0.30, w=W_DOT, h=100, slant=SL_DOT)
    _dot(g, x0 + wd * 0.80, y1 - h * 0.24, w=W_DOT, h=100, slant=SL_PIE)


def _ninben(g: Glyph, x0: float, y0: float, x1: float, y1: float,
            w: float = W_MAIN) -> None:
    """亻：撇 + 竖（竖自撇的中段起笔）。"""
    h = y1 - y0
    wd = x1 - x0
    _diag(g, x0 + 50, y1 - h * 0.36, x0 + wd * 0.86, y1 - h * 0.02, w=w)
    g.vbar(x0 + wd * 0.50, y1 - h * 0.24, y0, weight=w)


def _onna(g: Glyph, x0: float, y0: float, x1: float, y1: float,
          w: float = W_MAIN) -> None:
    """女：撇折（撇 + 折两段）+ 撇 + 横。

    ①撇折：自 (0.42w, 顶) 陡下至 (0.20w, 中偏上) 再折向右下至 (0.90w, 底)；
    ②长撇：自 (0.78w, 顶偏下) 一贯到左下角；
    ③横：中部横贯。折点两段留 6% 重叠，避免并集出尖点。
    """
    h = y1 - y0
    wd = x1 - x0
    g.hbar(x0, x0 + wd * 0.92, y1 - h * 0.52, weight=w)
    _diag(g, x0 + wd * 0.42, y1 - h * 0.02, x0 + wd * 0.20, y1 - h * 0.46,
          w=w)
    _diag(g, x0 + wd * 0.17, y1 - h * 0.49, x0 + wd * 0.90, y0 + h * 0.04,
          w=w)
    _diag(g, x0 + wd * 0.78, y1 - h * 0.10, x0 + wd * 0.04, y0 + h * 0.02,
          w=w)


def _ki(g: Glyph, x0: float, y0: float, x1: float, y1: float,
        w: float = W_MAIN) -> None:
    """木：横 + 竖 + 撇 + 捺。"""
    h = y1 - y0
    wd = x1 - x0
    xc = x0 + wd / 2
    g.hbar(x0, x1, y1 - h * 0.30, weight=w)
    g.vbar(xc, y1, y0, weight=w)
    _diag(g, x0 + 40, y0 + 12, xc, y1 - h * 0.28, w=w)
    _diag(g, xc, y1 - h * 0.28, x1 - 34, y0 + 12, w=w)


def _tsuchi(g: Glyph, x0: float, y0: float, x1: float, y1: float,
            w: float = W_MAIN) -> None:
    """土：上横（短）+ 竖 + 下横（长）。"""
    h = y1 - y0
    wd = x1 - x0
    xc = x0 + wd / 2
    g.hbar(x0 + wd * 0.05, x1 - wd * 0.05, y1 - h * 0.36, weight=w)
    g.vbar(xc, y1 - h * 0.36, y0 + w / 2, weight=w)
    g.hbar(x0, x1, y0 + w / 2, weight=w)


def _hou(g: Glyph, x0: float, y0: float, x1: float, y1: float,
         w: float = W_MAIN) -> None:
    """方：点 + 横 + 横折钩（含底钩）+ 撇。

    点放大到 96×126 并坐在横的左三分之一上；横折钩的横抬到横下方 60
    单位处；撇自横折钩横的上方起笔，斜度约 76°，与参考一致。
    """
    h = y1 - y0
    wd = x1 - x0
    _dot(g, x0 + wd * 0.24, y1 - h * 0.08, w=W_MAIN, h=126, slant=SL_DOT)
    g.hbar(x0, x1, y1 - h * 0.19, weight=w)
    g.hbar(x0 + wd * 0.13, x0 + wd * 0.78, y1 - h * 0.38, weight=w)
    g.vbar(x0 + wd * 0.78, y1 - h * 0.38, y0 + w / 2, weight=w)
    g.hbar(x0 + wd * 0.52, x0 + wd * 0.78, y0 + w / 2, weight=w)
    _diag(g, x0 + wd * 0.30, y1 - h * 0.27, x0 + wd * 0.07, y0 + h * 0.06,
          w=w)


def _ouchi(g: Glyph, x0: float, y0: float, x1: float, y1: float,
           w: float = W_MAIN) -> None:
    """夹：上横（短）+ 丷 + 下横（长）+ 撇捺（自上横中央下行）。"""
    h = y1 - y0
    wd = x1 - x0
    xc = x0 + wd / 2
    g.hbar(x0 + wd * 0.17, x1 - wd * 0.17, y1 - h * 0.12, weight=w)
    _dot(g, x0 + wd * 0.27, y1 - h * 0.29, w=W_DOT, h=100, slant=SL_DOT)
    _dot(g, x0 + wd * 0.73, y1 - h * 0.29, w=W_DOT, h=100, slant=SL_PIE)
    g.hbar(x0, x1, y1 - h * 0.47, weight=w)
    _diag(g, x0 + 50, y0 + 13, xc, y1 - h * 0.12, w=w)
    _diag(g, xc, y1 - h * 0.12, x1 - 45, y0 + 13, w=w)


def _otto(g: Glyph, x0: float, y0: float, x1: float, y1: float,
          w: float = W_MAIN) -> None:
    """夫：上横（短）+ 下横（长）+ 撇捺（自上横中央下行）。"""
    h = y1 - y0
    wd = x1 - x0
    xc = x0 + wd / 2
    g.hbar(x0 + wd * 0.18, x1 - wd * 0.18, y1 - h * 0.16, weight=w)
    g.hbar(x0, x1, y1 - h * 0.42, weight=w)
    _diag(g, x0 + 50, y0 + 13, xc, y1 - h * 0.16, w=w)
    _diag(g, xc, y1 - h * 0.16, x1 - 45, y0 + 13, w=w)


def _shi(g: Glyph, x0: float, y0: float, x1: float, y1: float,
         w: float = W_MAIN) -> None:
    """失：上撇（短）+ 上横 + 下横 + 撇捺。"""
    h = y1 - y0
    wd = x1 - x0
    xc = x0 + wd / 2
    _diag(g, x0 + 40, y1 - h * 0.21, x0 + wd * 0.34, y1 - h * 0.03, w=w)
    g.hbar(x0 + wd * 0.15, x1 - wd * 0.04, y1 - h * 0.27, weight=w)
    g.hbar(x0 + wd * 0.03, x1, y1 - h * 0.46, weight=w)
    _diag(g, x0 + 40, y0 + 13, xc, y1 - h * 0.27, w=w)
    _diag(g, xc, y1 - h * 0.27, x1 - 40, y0 + 13, w=w)


def _gen(g: Glyph, x0: float, y0: float, x1: float, y1: float,
         w: float = W_MAIN) -> None:
    """艮：左竖 + 顶横 + 右竖 + 中横 + 底横 + 撇 + 捺（框内只两道横）。"""
    h = y1 - y0
    wd = x1 - x0
    g.vbar(x0 + w / 2, y0 + h * 0.49, y1, weight=w)
    g.vbar(x1 - w / 2, y0 + h * 0.49, y1, weight=w)
    g.hbar(x0, x1, y1 - w / 2, weight=w)
    g.hbar(x0, x1, y1 - h * 0.28, weight=w)
    g.hbar(x0, x1, y0 + h * 0.49, weight=w)
    _diag(g, x0 + 40, y0 + 10, x0 + wd * 0.40, y0 + h * 0.51, w=w)
    _diag(g, x0 + wd * 0.58, y0 + h * 0.49, x1 - 34, y0 + 10, w=w)


def _dai(g: Glyph, x0: float, y0: float, x1: float, y1: float,
         w: float = W_MAIN) -> None:
    """台：厶（撇 + 折 + 点）+ 口。

    厶的三笔走 84 细档，口收窄并走 84 细档 —— 台整体是 9 画的密字，
    若全用 96 会闷成黑块。
    """
    h = y1 - y0
    wd = x1 - x0
    _diag(g, x0 + wd * 0.07, y1 - h * 0.37, x0 + wd * 0.32, y1 - h * 0.03,
          w=W_THIN)
    _diag(g, x0 + wd * 0.06, y1 - h * 0.39, x0 + wd * 0.64, y1 - h * 0.33,
          w=W_THIN)
    _dot(g, x0 + wd * 0.78, y1 - h * 0.33, w=W_DOT, h=100, slant=SL_DOT)
    _kuchi(g, x0 + wd * 0.13, y0, x1 - wd * 0.13, y1 - h * 0.50, w=W_THIN)


def _ki_ji(g: Glyph, x0: float, y0: float, x1: float, y1: float,
           w: float = W_MAIN) -> None:
    """己：横折（顶横 + 右竖）+ 中横 + 竖弯钩（左竖 + 底横）。

    三道横之间各留 46 单位空档；早前版本把中横放在 y1−0.38h 处，
    其上缘与顶横下缘只差 0.4 单位，并集会退化成零宽尖点。
    """
    h = y1 - y0
    wd = x1 - x0
    g.hbar(x0, x1, y1 - w / 2, weight=w)                          # 顶横
    g.vbar(x1 - w / 2, y1 - h * 0.50, y1, weight=w)                # 右竖
    g.hbar(x0 + wd * 0.16, x1, y1 - h * 0.50, weight=w)            # 中横
    g.vbar(x0 + wd * 0.16, y0 + w / 2, y1 - h * 0.50, weight=w)    # 左竖
    g.hbar(x0 + wd * 0.16, x1, y0 + w / 2, weight=w)               # 底横


def _kokoro(g: Glyph, x0: float, y0: float, x1: float, y1: float,
            w: float = W_MAIN) -> None:
    """心：卧钩（两段）+ 左点 + 中点 + 右点。

    卧钩自左上向右下扫到钩底，再向右上挑出（两段共 6% 重叠）；
    三点都落在卧钩之上，左点偏下、右点偏上。
    """
    h = y1 - y0
    wd = x1 - x0
    _diag(g, x0 + wd * 0.10, y0 + h * 0.55, x0 + wd * 0.58, y0 + h * 0.11,
          w=w)
    _diag(g, x0 + wd * 0.54, y0 + h * 0.13, x0 + wd * 0.94, y0 + h * 0.41,
          w=w)
    _dot(g, x0 + wd * 0.05, y0 + h * 0.71, w=W_DOT, h=104, slant=SL_PIE)
    _dot(g, x0 + wd * 0.47, y0 + h * 0.75, w=W_DOT, h=104, slant=SL_DOT)
    _dot(g, x0 + wd * 0.88, y0 + h * 0.70, w=W_DOT, h=104, slant=SL_PIE)


def _michi(g: Glyph, x0: float, y0: float, x1: float, y1: float,
           w: float = W_MAIN) -> None:
    """辶：点 + コ形折 + 底部长捺。"""
    h = y1 - y0
    wd = x1 - x0
    _dot(g, x0 + wd * 0.13, y1 - h * 0.07, w=W_DOT, h=100, slant=SL_DOT)
    g.hbar(x0 + wd * 0.02, x0 + wd * 0.26, y1 - h * 0.24, weight=w)
    g.vbar(x0 + wd * 0.07, y0 + h * 0.14, y1 - h * 0.24, weight=w)
    g.hbar(x0 + wd * 0.02, x0 + wd * 0.23, y0 + h * 0.14, weight=w)
    _diag(g, x0 + 25, y0 + 70, x1 - 35, y0 + 150, w=w)


def _mata(g: Glyph, x0: float, y0: float, x1: float, y1: float,
          w: float = W_MAIN) -> None:
    """又：横撇 + 捺。"""
    h = y1 - y0
    wd = x1 - x0
    g.hbar(x0, x1, y1 - w / 2, weight=w)
    _diag(g, x0 + 40, y0 + 12, x1 - w / 2, y1 - w / 2, w=w)
    _diag(g, x0 + wd * 0.22, y1 - h * 0.18, x1 - 34, y0 + 12, w=w)


# ---------------------------------------------------------------------------
# 字形
# ---------------------------------------------------------------------------

def _g_she() -> Glyph:
    """舌：千（丿 / 一 / 丨）+ 口。

    丿 = 中心线 (185,672)→(605,758)（12° 的平撇，照 gothic 参考的扁平走向）；
    一 = 满宽 x90..870；丨 = x480，自丿底穿一而下接口；
    口 = x210..720 / y0..330。
    """
    g = Glyph("uni820C", advance=1000, unicode=0x820C, note="舌：千（丿一丨）+ 口")
    _diag(g, 185, 672, 605, 758, w=W_MAIN)
    g.hbar(90, 870, 520, weight=W_MAIN)
    g.vbar(480, 770, 300, weight=W_MAIN)
    g.vbar(258, 0, 330, weight=W_MAIN)
    g.hbar(210, 720, 282, weight=W_MAIN)
    g.vbar(672, 330, 0, weight=W_MAIN)
    g.hbar(210, 720, 48, weight=W_MAIN)
    return g


def _g_bou() -> Glyph:
    """坊：土（左 x60..320）+ 方（右 x360..940）。"""
    g = Glyph("uni574A", advance=1000, unicode=0x574A, note="坊：土 + 方")
    _tsuchi(g, X_L, Y_B, 320, Y_T, w=W_MAIN)
    _hou(g, 360, Y_B, X_R, Y_T, w=W_MAIN)
    return g


def _g_kyo() -> Glyph:
    """峡：山（左 x60..390）+ 夹（右 x420..940）。"""
    g = Glyph("uni5CE1", advance=1000, unicode=0x5CE1, note="峡：山 + 夹")
    _yama(g, X_L, Y_B, 390, Y_T, w=W_THIN)
    _ouchi(g, 420, Y_B, X_R, Y_T, w=W_MAIN)
    return g


def _g_ri() -> Glyph:
    """厘：厂（顶横 + 左撇）+ 里（田 + 土）。

    厂：顶横 x60..940 / 墨迹 y724..820；左撇中心线 (165,740)→(110,60)。
    里：田 x250..800 / y300..660（84 细档），下横 + 中心竖 + 底横。
    """
    g = Glyph("uni5398", advance=1000, unicode=0x5398, note="厘：厂 + 里")
    g.hbar(X_L, X_R, 820 - W_MAIN / 2, weight=W_MAIN)
    _diag(g, 165, 740, 110, 60, w=W_SEC)
    # 里：田
    g.vbar(304, 300, 660, weight=W_THIN)
    g.vbar(746, 300, 660, weight=W_THIN)
    g.hbar(262, 788, 660 - W_THIN / 2, weight=W_THIN)
    g.hbar(262, 788, 480, weight=W_THIN)
    g.hbar(262, 788, 300 + W_THIN / 2, weight=W_THIN)
    g.vbar(525, 300, 660, weight=W_THIN)
    # 里：土
    g.hbar(250, 850, 210, weight=W_THIN)
    g.vbar(525, 42, 252, weight=W_THIN)
    g.hbar(300, 840, W_THIN / 2, weight=W_THIN)
    return g


def _g_yoh() -> Glyph:
    """羊：丷 + 三横 + 中竖。

    丷：左丶 slant −14 / 右丿 slant +14，中心 y730；
    三横 y600 / 450 / 300（下横最长 x90..940）；中竖 x500 自 760 落至 0。
    """
    g = Glyph("uni7F8A", advance=1000, unicode=0x7F8A, note="羊：丷 + 三横 + 竖")
    _dot(g, 370, 730, w=W_DOT, h=104, slant=SL_DOT)
    _dot(g, 630, 730, w=W_DOT, h=104, slant=SL_PIE)
    g.hbar(180, 820, 600, weight=W_MAIN)
    g.hbar(140, 860, 450, weight=W_MAIN)
    g.hbar(90, 940, 300, weight=W_MAIN)
    g.vbar(500, 760, 0, weight=W_MAIN)
    return g


def _g_tai() -> Glyph:
    """胎：月（左 x60..330）+ 台（右 x360..940）。"""
    g = Glyph("uni80CE", advance=1000, unicode=0x80CE, note="胎：月 + 台")
    _moon(g, X_L, Y_B, 330, Y_T, w=W_MAIN)
    _dai(g, 360, Y_B, X_R, Y_T, w=W_MAIN)
    return g


def _g_kyo2() -> Glyph:
    """挟：扌（左 x60..340）+ 夹（右 x420..940）。"""
    g = Glyph("uni631F", advance=1000, unicode=0x631F, note="挟：扌 + 夹")
    _tehen(g, X_L, Y_B, 340, Y_T, w=W_MAIN)
    _ouchi(g, 420, Y_B, X_R, Y_T, w=W_MAIN)
    return g


def _g_setsu() -> Glyph:
    """窃：穴（宀 + 儿）+ 切（七 + 刀）。

    宀：竖点 (500,760) + 横 x180..820 + 左右短竖；
    儿：丿 (390,650)→(250,480)、乚 x620..760 / y488..608；
    切：七 = 一 + 竖弯钩；刀 = 横折钩 + 撇。
    """
    g = Glyph("uni7A83", advance=1000, unicode=0x7A83, note="窃：穴 + 切")
    # 宀
    _dot(g, 500, 760, w=W_DOT, h=100, slant=SL_VERT)
    g.hbar(180, 820, 660, weight=W_MAIN)
    g.vbar(228, 560, 660, weight=W_MAIN)
    g.vbar(772, 560, 660, weight=W_MAIN)
    # 儿
    _diag(g, 390, 650, 250, 480, w=W_THIN)
    g.vbar(620, 480, 548, weight=W_THIN)
    g.hbar(620, 760, 548, weight=W_THIN)
    # 切：七
    g.hbar(140, 560, 300, weight=W_MAIN)
    g.vbar(390, 100, 350, weight=W_MAIN)
    g.hbar(390, 560, 100, weight=W_MAIN)
    # 切：刀
    g.hbar(580, 900, 380, weight=W_MAIN)
    g.vbar(852, 200, 380, weight=W_MAIN)
    g.hbar(740, 852, 200, weight=W_MAIN)
    _diag(g, 760, 400, 640, 80, w=W_MAIN)
    return g


def _g_hou2() -> Glyph:
    """泡：氵（左 x60..280）+ 包（右 x320..940：勹 + 巳）。"""
    g = Glyph("uni6CE1", advance=1000, unicode=0x6CE1, note="泡：氵 + 包")
    _sanzui(g, X_L, Y_B, 280, Y_T, w=W_MAIN)
    # 勹
    _diag(g, 560, 790, 380, 560, w=W_MAIN)
    g.hbar(500, 900, 760, weight=W_MAIN)
    g.vbar(852, 400, 760, weight=W_MAIN)
    g.hbar(700, 852, 400, weight=W_MAIN)
    # 巳
    g.hbar(480, 780, 580, weight=W_MAIN)
    g.vbar(732, 380, 580, weight=W_MAIN)
    g.hbar(480, 732, 380, weight=W_MAIN)
    g.vbar(520, 200, 380, weight=W_MAIN)
    g.hbar(520, 840, 200, weight=W_MAIN)
    return g


def _g_kon() -> Glyph:
    """恨：忄（左 x60..360）+ 艮（右 x390..940）。"""
    g = Glyph("uni6068", advance=1000, unicode=0x6068, note="恨：忄 + 艮")
    _ritsu(g, X_L, Y_B, 360, Y_T, w=W_MAIN)
    _gen(g, 390, Y_B, X_R, Y_T, w=W_MAIN)
    return g


def _g_fang() -> Glyph:
    """肪：月（左 x60..330）+ 方（右 x360..940）。"""
    g = Glyph("uni80AA", advance=1000, unicode=0x80AA, note="肪：月 + 方")
    _moon(g, X_L, Y_B, 330, Y_T, w=W_MAIN)
    _hou(g, 360, Y_B, X_R, Y_T, w=W_MAIN)
    return g


def _g_fu() -> Glyph:
    """扶：扌（左 x60..340）+ 夫（右 x370..940）。"""
    g = Glyph("uni6276", advance=1000, unicode=0x6276, note="扶：扌 + 夫")
    _tehen(g, X_L, Y_B, 340, Y_T, w=W_MAIN)
    _otto(g, 370, Y_B, X_R, Y_T, w=W_MAIN)
    return g


def _g_ki() -> Glyph:
    """忌：己（上 x200..800 / y440..820）+ 心（下 x80..880 / y0..380）。"""
    g = Glyph("uni5FCC", advance=1000, unicode=0x5FCC, note="忌：己 + 心")
    _ki_ji(g, 200, 440, 800, 820, w=W_MAIN)
    _kokoro(g, 80, 0, 880, 380, w=W_MAIN)
    return g


def _g_hon() -> Glyph:
    """奔：大（上）+ 卉（下：十 + 廾）。"""
    g = Glyph("uni5954", advance=1000, unicode=0x5954, note="奔：大 + 卉")
    # 大
    g.hbar(120, 880, 700, weight=W_MAIN)
    _diag(g, 500, 700, 150, 440, w=W_MAIN)
    _diag(g, 500, 700, 850, 440, w=W_MAIN)
    # 卉：十
    g.hbar(240, 760, 420, weight=W_MAIN)
    g.vbar(500, 360, 480, weight=W_MAIN)
    # 卉：廾
    g.hbar(90, 940, 250, weight=W_MAIN)
    _diag(g, 330, 250, 210, 60, w=W_MAIN)
    g.vbar(760, 0, 250, weight=W_MAIN)
    return g


def _g_shou() -> Glyph:
    """肖：⺌（丶 + 丨 + 丿，上部）+ 月（下部 x220..780 / y0..560）。"""
    g = Glyph("uni8096", advance=1000, unicode=0x8096, note="肖：⺌ + 月")
    _dot(g, 350, 750, w=W_DOT, h=104, slant=SL_DOT)
    g.vbar(500, 560, 820, weight=W_MAIN)
    _dot(g, 650, 750, w=W_DOT, h=104, slant=SL_PIE)
    _moon(g, 220, 0, 780, 560, w=W_MAIN)
    return g


def _g_kyu() -> Glyph:
    """朽：木（左 x60..400）+ 丂（右 x430..940）。"""
    g = Glyph("uni673D", advance=1000, unicode=0x673D, note="朽：木 + 丂")
    _ki(g, X_L, Y_B, 400, Y_T, w=W_MAIN)
    g.hbar(430, 940, 740, weight=W_MAIN)
    g.hbar(470, 880, 600, weight=W_MAIN)
    g.vbar(832, 600, 160, weight=W_MAIN)
    g.hbar(630, 832, 160, weight=W_MAIN)
    return g


def _g_kyo3() -> Glyph:
    """享：亠（竖点 + 横）+ 口（中 x250..750 / y340..570）+ 子（乛 + 亅 + 一）。"""
    g = Glyph("uni4EAB", advance=1000, unicode=0x4EAB, note="享：亠 + 口 + 子")
    _dot(g, 500, 765, w=W_DOT, h=100, slant=SL_VERT)
    g.hbar(120, 880, 672, weight=W_MAIN)
    _kuchi(g, 250, 340, 750, 570, w=W_MAIN)
    # 子
    g.hbar(320, 690, 260, weight=W_MAIN)
    _diag(g, 690, 260, 545, 190, w=W_MAIN)
    g.vbar(500, 280, 40, weight=W_MAIN)
    g.hbar(410, 500, 40, weight=W_MAIN)
    g.hbar(160, 840, 170, weight=W_MAIN)
    return g


def _g_sha() -> Glyph:
    """沙：氵（左 x60..280）+ 少（右 x320..940）。

    少 = 丨 + 丿 + 丶 + 长撇。右点放大到 96×170（参考里少点的右点最重），
    竖与长撇都拉到满，否则整字墨量只有同档中位数的 45%，在批里会发飘。
    """
    g = Glyph("uni6C99", advance=1000, unicode=0x6C99, note="沙：氵 + 少")
    _sanzui(g, X_L, Y_B, 280, Y_T, w=W_MAIN)
    g.vbar(600, 400, 820, weight=W_MAIN)
    _diag(g, 630, 700, 340, 440, w=W_MAIN)
    _dot(g, 790, 540, w=W_MAIN, h=200, slant=SL_DOT)
    _diag(g, 720, 480, 340, 30, w=W_MAIN)
    return g


def _g_tetsu() -> Glyph:
    """迭：失（右 x360..940 / y220..820）+ 辶（左 + 底捺）。"""
    g = Glyph("uni8FED", advance=1000, unicode=0x8FED, note="迭：辶 + 失")
    _shi(g, 360, 220, X_R, 820, w=W_MAIN)
    _michi(g, X_L, 0, X_R, 820, w=W_MAIN)
    return g


def _g_han() -> Glyph:
    """帆：巾（左 x60..360，三竖用 84 细档）+ 凡（右 x390..940）。"""
    g = Glyph("uni5E06", advance=1000, unicode=0x5E06, note="帆：巾 + 凡")
    # 巾
    g.vbar(210, 0, 820, weight=W_THIN)
    g.hbar(60, 360, 760, weight=W_MAIN)
    g.vbar(102, 300, 760, weight=W_THIN)
    g.vbar(318, 300, 760, weight=W_THIN)
    # 凡
    _diag(g, 510, 700, 440, 80, w=W_MAIN)
    g.hbar(490, 880, 700, weight=W_MAIN)
    g.vbar(832, 200, 700, weight=W_MAIN)
    g.hbar(832, 940, 200, weight=W_MAIN)
    _dot(g, 700, 470, w=W_DOT, h=104, slant=SL_DOT)
    return g


def _g_zhuo() -> Glyph:
    """拙：扌（左 x60..340）+ 出（右 x370..940）。"""
    g = Glyph("uni62D9", advance=1000, unicode=0x62D9, note="拙：扌 + 出")
    _tehen(g, X_L, Y_B, 340, Y_T, w=W_MAIN)
    # 出：中竖 + 上凵 + 下凵
    g.vbar(655, 0, 820, weight=W_MAIN)
    g.vbar(430, 520, 620, weight=W_MAIN)
    g.vbar(880, 520, 620, weight=W_MAIN)
    g.hbar(430, 880, 620 - W_MAIN / 2, weight=W_MAIN)
    g.vbar(430, 0, 420, weight=W_MAIN)
    g.vbar(880, 0, 420, weight=W_MAIN)
    g.hbar(430, 880, W_MAIN / 2, weight=W_MAIN)
    return g


def _g_ji() -> Glyph:
    """侍：亻（左 x60..340）+ 寺（右 x370..940：土 + 寸）。"""
    g = Glyph("uni4F8D", advance=1000, unicode=0x4F8D, note="侍：亻 + 寺")
    _ninben(g, X_L, Y_B, 340, Y_T, w=W_MAIN)
    # 土
    g.hbar(430, 880, 740, weight=W_MAIN)
    g.vbar(655, 560, 740, weight=W_MAIN)
    g.hbar(370, 940, 570, weight=W_MAIN)
    # 寸
    g.hbar(370, 940, 420, weight=W_MAIN)
    g.vbar(740, 40, 560, weight=W_MAIN)
    g.hbar(660, 740, 40, weight=W_MAIN)
    _dot(g, 470, 240, w=W_DOT, h=100, slant=SL_DOT)
    return g


def _g_touge() -> Glyph:
    """峠：山（左 x60..390）+ 上（右 x440..940）。"""
    g = Glyph("uni5CE0", advance=1000, unicode=0x5CE0, note="峠：山 + 上")
    _yama(g, X_L, Y_B, 390, Y_T, w=W_THIN)
    g.vbar(600, 60, 820, weight=W_MAIN)
    g.hbar(600, 880, 620, weight=W_MAIN)
    g.hbar(440, 940, 60, weight=W_MAIN)
    return g


def _g_shuku() -> Glyph:
    """叔：尗（左 x60..450：上 + 小）+ 又（右 x480..940）。"""
    g = Glyph("uni53D4", advance=1000, unicode=0x53D4, note="叔：尗 + 又")
    # 上
    g.vbar(250, 470, 820, weight=W_MAIN)
    g.hbar(250, 440, 690, weight=W_MAIN)
    g.hbar(60, 450, 470, weight=W_MAIN)
    # 小
    g.vbar(250, 0, 470, weight=W_MAIN)
    _diag(g, 255, 380, 95, 100, w=W_MAIN)
    _dot(g, 390, 280, w=W_DOT, h=100, slant=SL_PIE)
    # 又
    _mata(g, 480, 0, X_R, 820, w=W_MAIN)
    return g


def _g_jo() -> Glyph:
    """叙：余（左 x60..480）+ 又（右 x510..940）。"""
    g = Glyph("uni53D9", advance=1000, unicode=0x53D9, note="叙：余 + 又")
    # 余 = 人 + 一 + 朩（人字头两腿放低到 655，下面的横才分得开）
    _diag(g, 270, 810, 95, 655, w=W_MAIN)
    _diag(g, 270, 810, 450, 655, w=W_MAIN)
    g.hbar(120, 420, 570, weight=W_MAIN)
    g.hbar(60, 480, 430, weight=W_MAIN)
    g.vbar(270, 0, 570, weight=W_MAIN)
    _dot(g, 140, 300, w=W_DOT, h=100, slant=SL_DOT)
    _dot(g, 410, 300, w=W_DOT, h=100, slant=SL_PIE)
    # 又
    _mata(g, 510, 0, X_R, 820, w=W_MAIN)
    return g


def _g_gen() -> Glyph:
    """吟：口（左 x60..300 / y200..640）+ 今（右 x340..940：人 + 一 + 乛）。"""
    g = Glyph("uni541F", advance=1000, unicode=0x541F, note="吟：口 + 今")
    _kuchi(g, X_L, 200, 300, 640, w=W_MAIN)
    # 今
    _diag(g, 640, 780, 380, 560, w=W_MAIN)
    _diag(g, 640, 780, 890, 570, w=W_MAIN)
    g.hbar(470, 810, 500, weight=W_MAIN)
    g.hbar(500, 880, 380, weight=W_MAIN)
    _diag(g, 880, 380, 600, 80, w=W_MAIN)
    return g


def _g_tei() -> Glyph:
    """逓：辶（左 + 底捺）+ 乕（丿 + 三，右 x400..900 / y240..790）。"""
    g = Glyph("uni9013", advance=1000, unicode=0x9013, note="逓：辶 + 乕")
    _diag(g, 480, 770, 870, 715, w=W_MAIN)
    g.hbar(400, 900, 560, weight=W_MAIN)
    g.hbar(400, 900, 400, weight=W_MAIN)
    g.hbar(400, 900, 240, weight=W_MAIN)
    _michi(g, X_L, 0, X_R, 820, w=W_MAIN)
    return g


def _g_sen() -> Glyph:
    """甚：甘上 + 两内横 + 底下长横 + 丿 + 乚。"""
    g = Glyph("uni751A", advance=1000, unicode=0x751A, note="甚：其上 + 丿 + 乚")
    g.hbar(140, 820, 720, weight=W_MAIN)
    g.vbar(280, 300, 820, weight=W_MAIN)
    g.vbar(700, 300, 820, weight=W_MAIN)
    g.hbar(280, 700, 570, weight=W_MAIN)
    g.hbar(280, 700, 420, weight=W_MAIN)
    g.hbar(90, 900, 280, weight=W_MAIN)
    _diag(g, 300, 280, 120, 60, w=W_MAIN)
    g.vbar(700, 60, 280, weight=W_MAIN)
    g.hbar(700, 900, 60, weight=W_MAIN)
    return g


def _g_you() -> Glyph:
    """妖：女（左 x60..380）+ 夭（右 x430..940）。女 与 姻里的女同档（92）。"""
    g = Glyph("uni5996", advance=1000, unicode=0x5996, note="妖：女 + 夭")
    _onna(g, X_L, Y_B, 380, Y_T, w=W_SEC)
    _diag(g, 700, 760, 480, 665, w=W_MAIN)
    g.hbar(430, 940, 600, weight=W_MAIN)
    _diag(g, 690, 600, 460, 60, w=W_MAIN)
    _diag(g, 690, 600, 910, 60, w=W_MAIN)
    return g


def _g_misaki() -> Glyph:
    """岬：山（左 x60..390）+ 甲（右 x440..940：田 + 下出竖）。

    甲 是围框结构，全部走 84 细档（与台里的口同处理），否则墨量超上限。
    """
    g = Glyph("uni5CAC", advance=1000, unicode=0x5CAC, note="岬：山 + 甲")
    _yama(g, X_L, Y_B, 390, Y_T, w=W_THIN)
    g.vbar(490, 140, 760, weight=W_THIN)
    g.vbar(890, 140, 760, weight=W_THIN)
    g.hbar(440, 940, 760 - W_THIN / 2, weight=W_THIN)
    g.hbar(440, 940, 450, weight=W_THIN)
    g.hbar(440, 940, 140 + W_THIN / 2, weight=W_THIN)
    g.vbar(690, 0, 760, weight=W_THIN)
    return g


def _g_con() -> Glyph:
    """姻：女（左 x60..380）+ 因（右 x430..940：囗 + 大）。

    因 是全批最密的字（囗 包 大），囗 与大全部走 84 细档并把大收小，
    否则墨量会顶到同档上限之上。
    """
    g = Glyph("uni59FB", advance=1000, unicode=0x59FB, note="姻：女 + 因")
    _onna(g, X_L, Y_B, 380, Y_T, w=W_SEC)
    g.vbar(472, 0, 820, weight=W_THIN)
    g.vbar(898, 0, 820, weight=W_THIN)
    g.hbar(430, 940, 820 - W_THIN / 2, weight=W_THIN)
    g.hbar(430, 940, W_THIN / 2, weight=W_THIN)
    g.hbar(520, 850, 520, weight=W_THIN)
    _diag(g, 685, 520, 545, 170, w=W_THIN)
    _diag(g, 685, 520, 840, 170, w=W_THIN)
    return g


def _g_yuu() -> Glyph:
    """幽：山框（左右竖 + 底横）+ 两个幺。

    两个幺放大到填满山框内部（x250..810 / y380..770），走 96 主档；
    幺 = 撇（下左）+ 折（上右）两笔，两幺错开不交叠。
    """
    g = Glyph("uni5E7D", advance=1000, unicode=0x5E7D, note="幽：山框 + 幺幺")
    g.vbar(X_L + W_MAIN / 2, 0, 820, weight=W_MAIN)
    g.vbar(X_R - W_MAIN / 2, 0, 820, weight=W_MAIN)
    g.hbar(X_L, X_R, W_MAIN / 2, weight=W_MAIN)
    # 幺（左）
    _diag(g, 460, 770, 250, 460, w=W_MAIN)
    _diag(g, 245, 430, 530, 640, w=W_MAIN)
    # 幺（右）
    _diag(g, 750, 720, 540, 410, w=W_MAIN)
    _diag(g, 535, 380, 810, 590, w=W_MAIN)
    return g


def build() -> list[Glyph]:
    return [
        _g_she(),      # 舌 U+820C
        _g_bou(),      # 坊 U+574A
        _g_kyo(),      # 峡 U+5CE1
        _g_ri(),       # 厘 U+5398
        _g_yoh(),      # 羊 U+7F8A
        _g_tai(),      # 胎 U+80CE
        _g_kyo2(),     # 挟 U+631F
        _g_setsu(),    # 窃 U+7A83
        _g_hou2(),     # 泡 U+6CE1
        _g_kon(),      # 恨 U+6068
        _g_fang(),     # 肪 U+80AA
        _g_fu(),       # 扶 U+6276
        _g_ki(),       # 忌 U+5FCC
        _g_hon(),      # 奔 U+5954
        _g_shou(),     # 肖 U+8096
        _g_kyu(),      # 朽 U+673D
        _g_kyo3(),     # 享 U+4EAB
        _g_sha(),      # 沙 U+6C99
        _g_tetsu(),    # 迭 U+8FED
        _g_han(),      # 帆 U+5E06
        _g_zhuo(),     # 拙 U+62D9
        _g_ji(),       # 侍 U+4F8D
        _g_touge(),    # 峠 U+5CE0
        _g_shuku(),    # 叔 U+53D4
        _g_jo(),       # 叙 U+53D9
        _g_gen(),      # 吟 U+541F
        _g_tei(),      # 逓 U+9013
        _g_sen(),      # 甚 U+751A
        _g_you(),      # 妖 U+5996
        _g_misaki(),   # 岬 U+5CAC
        _g_con(),      # 姻 U+59FB
        _g_yuu(),      # 幽 U+5E7D
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-019.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
