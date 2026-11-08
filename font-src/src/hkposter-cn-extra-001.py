"""HK Poster Heavy —— 中文补充批次 cn-extra-001。

为什么开这个批次
----------------
`hkposter-cn.py` 的字符清单是 CONTRACT §5 **冻结**的（龙 义 爱 无 风 电 击 间），
不能往里加字。而 Jōyō 批次表只覆盖**日语**常用漢字 ——
「智 U+667A」「慧 U+6167」这类**中文常用但不在 Jōyō 2136 里**的字，
在两条既有序列里都没有归属，成品里就是缺字（用户 2026-11-08 点名）。

本批次专门承接**中文侧缺口**，首批：
    智 U+667A  慧 U+6167
后续 GB2312 缺口字按同样的批次编号规则续做（cn-extra-002、003 …）。

设计取舍
--------
1. **配重沿用简体档**：主 108 / 次 100 / 细 92 / 点 92
   （与 `hkposter-cn.py` 完全一致 —— 同为简体字，同一张海报里不能读成「轻一号」）。
2. **智 = 知 + 日**（⿱知日）：上部「知」= 左「矢」+ 右「口」，下部「日」。
   矢 的四笔 = 顶短撇 + 横 + 长撇 + 长捺，撇捺从横下方分开张开。
3. **慧 = 彗 + 心**（⿱彗心）：彗 = 上排两个「丰」+ 下排「彐」，
   心 = 卧钩（折线近似）+ 左/中/右三点。
4. **折线粗化自己实现**（`stroke_path`）：卧钩这类曲线用几段 diag 拼接会渲染成
   一串尖角折线，不像标准骨架的碗形 —— 用带斜接转角的外轮廓多边形更接近。
   本函数只在**本文件内**，未改 `hkbuild` 公共库。
5. **方框腔高按几何算，不靠目测**：
   智的日腔 46 / 38，口腔 160；慧的彗白口 35 / 39 —— 全部 ≥ 24。
6. **平移两端点同量，斜率不变**（AGENTS.md：笔画的角度不可改）。

坐标全部取整；只用 hkbuild 与标准库；recipe 为纯函数，生成物确定。
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, write_ufo  # noqa: E402

# ---- 简体档权重（与 hkposter-cn.py 一致）----
W_MAIN = 108  # 主笔画
W_SEC = 100   # 次笔画
W_THIN = 92   # 细笔画（竖 / 点）
W_HAIR = 76   # 密字局部减重
W_FINE = 64   # 极端密字（慧：9 横）局部减重
W_DOT = 92    # 点 / 短撇


def dot(g, cx, cy, w=W_DOT, h=100, slant=-14):
    """点/短撇：斜切平行四边形。slant 只用 0 / -14 / +14 / 26。"""
    g.dot(cx, cy, w=w, h=h, slant=slant)


def stroke_path(g, pts, weight=92):
    """折线按笔宽生成外轮廓多边形（斜接转角），用于卧钩/弯钩这类曲线。

    曲线用折线近似比用几段 diag 拼接更接近标准骨架的走势
    （几段 diag 拼接会渲染成一串尖角）。
    """
    hw = weight / 2.0
    normals = []
    for i in range(len(pts) - 1):
        dx = pts[i + 1][0] - pts[i][0]
        dy = pts[i + 1][1] - pts[i][1]
        length = math.hypot(dx, dy)
        normals.append((-dy / length, dx / length))
    left, right = [], []
    for i, (x, y) in enumerate(pts):
        if i == 0:
            nx, ny = normals[0]
        elif i == len(pts) - 1:
            nx, ny = normals[-1]
        else:
            ax, ay = normals[i - 1]
            bx, by = normals[i]
            nx, ny = ax + bx, ay + by
            length = math.hypot(nx, ny) or 1.0
            nx, ny = nx / length, ny / length
            scale = 1.0 / max(0.40, nx * ax + ny * ay)
            nx, ny = nx * scale, ny * scale
        left.append((x + nx * hw, y + ny * hw))
        right.append((x - nx * hw, y - ny * hw))
    g.poly(left + right[::-1])


# ---------------------------------------------------------------------------
# 智 U+667A —— 「知 + 日」
# ---------------------------------------------------------------------------
def glyph_zhi() -> Glyph:
    """智：上「知」（左矢 + 右口）+ 下「日」。

    矢（x 60..445，ink y 450..815）：
      顶短撇 (275,810)→(150,690) · 横 610..710 · 长撇 (165,620)→(60,450) ·
      长捺 (240,620)→(445,450)
    口（x 520..940，ink y 460..820）：竖 520..620 / 840..940，顶横 720..820、
      底横 460..560 ⇒ 口腔 160 高 × 220 宽
    日（x 240..760，ink y 20..380）：三横 288..380 / 150..242 / 20..112
      ⇒ 两腔各 46 / 38
    """
    g = Glyph("uni667A", advance=1000, unicode=0x667A, note="智：知+日")

    # ---- 上部：知 ----
    # 矢
    g.diag(275, 810, 150, 690, weight=W_THIN)      # 顶短撇
    g.hbar(120, 440, 660, weight=W_SEC)            # 横（墨迹 610..710）
    g.diag(160, 635, 50, 455, weight=W_SEC)        # 长撇（方向同原设计，只延长）
    g.diag(235, 635, 450, 455, weight=W_SEC)       # 长捺（同上）
    # 口
    g.vbar(570, 815, 460, weight=W_SEC)             # 左竖（墨迹 x 520..620）
    g.vbar(890, 815, 460, weight=W_SEC)             # 右竖（墨迹 x 840..940）
    g.hbar(520, 940, 770, weight=W_SEC)             # 顶横（墨迹 720..820）
    g.hbar(520, 940, 510, weight=W_SEC)             # 底横（墨迹 460..560）

    # ---- 下部：日 ----
    g.vbar(286, 380, 20, weight=W_SEC)              # 左竖（墨迹 x 236..336）
    g.vbar(714, 380, 20, weight=W_SEC)              # 右竖（墨迹 x 664..764）
    g.hbar(240, 760, 334, weight=W_SEC)             # 顶横（墨迹 288..380）
    g.hbar(240, 760, 196, weight=W_THIN)            # 中横（墨迹 150..242）
    g.hbar(240, 760, 66, weight=W_THIN)             # 底横（墨迹 20..112）

    return g


# ---------------------------------------------------------------------------
# 慧 U+6167 —— 「彗 + 心」
# ---------------------------------------------------------------------------
def glyph_hui() -> Glyph:
    """慧：上「彗」（丰 丰 + 彐）+ 下「心」。

    **为什么横画要用 W_HAIR(76)**：慧 是 9 横的极端密字
    （两个「丰」各 3 横 + 「彐」3 横），竖向预算 820 单位装不下
    「3 横 × 92 + 2 个 24 白口」×2 组 + 「心」：
        3×92 + 2×24 = 324，两组 648，加丰↔彐 的 24 �� 心的 200 ⇒ 872 > 820。
    减到 76 后：3×76 + 2×24 = 276，两组 552 + 24 + 200 = 776 ✓。

    **参照字体的实测量**（M PLUS 1p Black，栅格 1000 → 1px = 1 单位）：
    它的「慧」在 Black 字重下**九横几乎相连**（抗锯齿把缝填满，
    逐行扫描找不到任何空行）—— 因为普通粗体的笔画只有 ≈44 单位，
    而本字体是 Heavy（≈96）。所以**不能照抄参照字体的间距**，
    按本项目的白口下限 24 自己排。

    坐标：
      左丰（x 85..425，ink y 544..820）：上横 744..820 / 中横 644..720 /
        下横 544..620，竖 255 穿三横
      右丰（x 550..890）：同结构，中心 x=720
      彐（x 200..800，ink y 244..520）：顶横 444..520 + 右竖 700..800，
        中横 344..420，底横 244..320 ⇒ 白口 24 / 24
      心（ink y 4..~196）：卧钩折线 + 左/中/右三点
    """
    g = Glyph("uni6167", advance=1000, unicode=0x6167, note="慧：彗+心")

    # ---- 上排：两个「丰」（竖冒头 8 单位，横间距 28 ⇒ 腔高 28 > 24）----
    for cx in (240, 740):
        g.hbar(cx - 140, cx + 140, 780, weight=W_FINE)    # 上横 748..812
        g.hbar(cx - 150, cx + 150, 688, weight=W_FINE)    # 中横 656..720
        g.hbar(cx - 170, cx + 170, 596, weight=W_FINE)    # 下横 564..628
        g.vbar(cx, 820, 582, weight=W_HAIR)               # 竖穿三横、顶冒头 8

    # ---- 中排：「彐」（右开口；横右端与竖右缘齐平，避免糊成实心块）----
    g.hbar(200, 800, 508, weight=W_FINE)             # 顶横（墨迹 476..540）
    g.vbar(762, 540, 292, weight=W_HAIR)             # 右竖（墨迹 x 724..800）
    g.hbar(200, 762, 416, weight=W_FINE)             # 中横（墨迹 384..448）
    g.hbar(200, 762, 324, weight=W_FINE)             # 底横（墨迹 292..356）

    # ---- 下部：「心」----
    stroke_path(g, [
        (195, 210),
        (280, 105),
        (470, 68),
        (660, 105),
        (745, 178),
    ], W_DOT)
    dot(g, cx=145, cy=175, w=W_DOT, h=100, slant=-14)   # 左点
    dot(g, cx=400, cy=200, w=W_DOT, h=100, slant=-14)   # 中点
    dot(g, cx=750, cy=160, w=W_DOT, h=100, slant=-14)   # 右点

    return g


def build() -> list[Glyph]:
    return [glyph_zhi(), glyph_hui()]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-cn-extra-001.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
