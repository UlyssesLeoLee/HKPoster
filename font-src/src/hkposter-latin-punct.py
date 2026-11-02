"""HK Poster Heavy — Wave 0 标点 lane（全角 12 + 半角 13）。

设计基线
--------
* 冻结参数（design-params.json / CONTRACT §2）：UPM 1000、主笔画 96、次笔画 92、
  细笔画 84。本 lane 不使用低于 84 的笔画；圆点以实心圆（16 边形）成形，
  视觉重量与 84–96 的笔画相称。
* 全角：advance 1000，字面 x 60..940、y 0..820。
* 半角：advance 按字形实际宽度定（240 / 300 / 320 / 340），墨形在 advance 内
  居中、字面留白；顶端与参考 master 的 A 实际墨顶（y≈717）对齐。

全角位置约定（整套内部一致，不混用两套约定）
--------------------------------------------
docs/04 §3「墨形居中、字面留白」是通则，但同时点名「全角句号的墨形落在
字面左下 1/3 处」——那正是大陆通用（GB/T 15834）约定。本 lane 采用同一套
约定，保证全角标点之间不互相打架：

1. 句号类（。 U+3002 / ， U+FF0C / 、 U+3001）：墨形落在字面左下 1/3
   （墨形 x 约 160..358，y 约 -28..271），与实测微软雅黑一致
   （U+3002 墨形 x 64..309、U+FF0C x 151..302、U+3001 x 62..302）。
2. 竖向类（！ ？ ： ；）：墨形横向居中于 x=500，纵向与汉字字面同高
   （实测微软雅黑：U+FF01 墨形 x 187..313，居中于 250）。
3. 成对括号（「」（）【】）：按 GB/T 15834「前半标点居右、后半标点居左」，
   前半（ U+FF08 / 「 U+300C / 【 U+3010）居右半，后半（ ） U+FF09 /
   」 U+300D / 】 U+3011）居左半，使括号紧贴被括内容——这是常规排版逻辑，
   不是为标题紧凑做的挪用。

半角位置约定
------------
* 半角与全角并行处理：全角给足留白，半角给紧凑字距，互不迁就。
* em dash（U+2014）advance = 1000（1 em），不用 240–340：320 单位的横杠是
  en dash 的语义，1 em 才是 em dash；按字形实际宽度定原则。
* 弯钩（? ）与 & 的弧段用「椭圆环带的一段」成形，开口端为径向切口，
  符合 GLY-002 的硬折优先；点用实心圆，避免小尺寸下内白糊死（GLY-006）。

运行：python font-src/src/hkposter-latin-punct.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, ellipse_points, write_ufo  # noqa: E402

# ---- 冻结笔画权重（主 / 次 / 细，标点不低于 84）----
W_MAIN = 96
W_SECOND = 92
W_THIN = 84

# ---- 全角版面（advance 1000）----
CJK_ADV = 1000
BODY_L = 60
BODY_R = 940
BODY_TOP = 820
MID = 500  # 全角中线

# ---- 半角版面 ----
CAP_TOP = 716  # 与参考 master 的 A 实际墨顶（717）齐平
ADV_NARROW = 240  # . , ! : ;
ADV_WIDE = 300  # ? ( )
ADV_HYPHEN = 320
ADV_QUOTEDBL = 320
ADV_AMP = 340
ADV_EMDASH = 1000


# --------------------------------------------------------------------------
# 几何工具
# --------------------------------------------------------------------------
def disc(glyph: Glyph, cx: float, cy: float, r: float, count: int = 16) -> None:
    """实心圆点（正 16 边形近似）。"""
    glyph.poly(ellipse_points(cx, cy, r, r, count=count))


def band(
    glyph: Glyph,
    cx: float,
    cy: float,
    rx_out: float,
    ry_out: float,
    rx_in: float,
    ry_in: float,
    th0: float,
    th1: float,
    steps: int = 16,
) -> None:
    """椭圆环带的一段（开口弧）。

    角度制，0°=+x、90°=+y，th0→th1 线性插值。外点列正序 + 内点列逆序
    闭合成一个简单多边形；两端为径向切口。
    """
    outer: list[tuple[float, float]] = []
    inner: list[tuple[float, float]] = []
    for index in range(steps + 1):
        theta = math.radians(th0 + (th1 - th0) * index / steps)
        outer.append((cx + rx_out * math.cos(theta), cy + ry_out * math.sin(theta)))
        inner.append((cx + rx_in * math.cos(theta), cy + ry_in * math.sin(theta)))
    glyph.poly(outer + list(reversed(inner)))


def wedge(
    glyph: Glyph,
    start: tuple[float, float],
    end: tuple[float, float],
    w_start: float,
    w_end: float,
) -> None:
    """两端宽度不同的锥形笔画：start→end 为中心线，宽度垂直于中心线。"""
    x0, y0 = start
    x1, y1 = end
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy)
    ux, uy = dx / length, dy / length
    px, py = -uy, ux
    glyph.poly(
        [
            (x0 + px * w_start / 2, y0 + py * w_start / 2),
            (x1 + px * w_end / 2, y1 + py * w_end / 2),
            (x1 - px * w_end / 2, y1 - py * w_end / 2),
            (x0 - px * w_start / 2, y0 - py * w_start / 2),
        ]
    )


def comma_mark(
    glyph: Glyph,
    cx: float,
    cy: float,
    r: float,
    tip: tuple[float, float],
    w_root: float = 70,
    w_tip: float = 12,
) -> None:
    """逗号：圆头 + 向左下出锋的尾。

    尾根落在圆头内部（距圆心约 0.42r），使尾在圆头边界之外露出足够长度，
    并集后轮廓干净且出锋可辨。
    """
    disc(glyph, cx, cy, r)
    wedge(glyph, (cx - r * 0.12, cy - r * 0.40), tip, w_root, w_tip)


# --------------------------------------------------------------------------
# 全角标点（advance 1000）
# --------------------------------------------------------------------------
def fw_ideographic_full_stop() -> Glyph:
    """。U+3002 全角句号：字面左下 1/3 的实心圆点。"""
    g = Glyph("uni3002", advance=CJK_ADV, unicode=0x3002, note="。：全角句号")
    disc(g, 250, 100, 90)
    return g


def fw_comma() -> Glyph:
    """，U+FF0C 全角逗号：字面左下 1/3，圆头 + 左下出锋尾。"""
    g = Glyph("uniFF0C", advance=CJK_ADV, unicode=0xFF0C, note="，：全角逗号")
    comma_mark(g, 272, 150, 82, tip=(176, -40), w_root=88, w_tip=18)
    return g


def fw_ideographic_comma() -> Glyph:
    """、U+3001 顿号：左下的上重下锐斜笔（起笔顿、收笔出锋）。"""
    g = Glyph("uni3001", advance=CJK_ADV, unicode=0x3001, note="、：顿号")
    wedge(g, (318, 262), (172, 38), W_MAIN, 26)
    return g


def fw_exclamation() -> Glyph:
    """！U+FF01 全角叹号：中线竖笔 + 独立圆点。"""
    g = Glyph("uniFF01", advance=CJK_ADV, unicode=0xFF01, note="！：全角叹号")
    g.vbar(MID, 250, 760, weight=W_MAIN)
    disc(g, MID, 55, 55)
    return g


def fw_question() -> Glyph:
    """？U+FF1F 全角问号：开口环带成钩，竖笔成干，底部独立圆点。"""
    g = Glyph("uniFF1F", advance=CJK_ADV, unicode=0xFF1F, note="？：全角问号")
    band(g, MID, 620, 144, 144, 60, 60, 150, -80, steps=18)
    g.vbar(517, 320, 520, weight=W_SECOND)
    disc(g, MID, 55, 55)
    return g


def fw_colon() -> Glyph:
    """：U+FF1A 全角冒号：中线上下两个圆点。"""
    g = Glyph("uniFF1A", advance=CJK_ADV, unicode=0xFF1A, note="：：全角冒号")
    disc(g, MID, 450, 55)
    disc(g, MID, 55, 55)
    return g


def fw_semicolon() -> Glyph:
    """；U+FF1B 全角分号：上圆点 + 下逗号。"""
    g = Glyph("uniFF1B", advance=CJK_ADV, unicode=0xFF1B, note="；：全角分号")
    disc(g, MID, 450, 55)
    comma_mark(g, MID, 55, 55, tip=(450, -55), w_root=70, w_tip=13)
    return g


def fw_parenleft() -> Glyph:
    """（U+FF08 全角左括号：GB/T 前半标点居右半，紧贴后续内容。"""
    g = Glyph("uniFF08", advance=CJK_ADV, unicode=0xFF08, note="（：全角左括号")
    band(g, 790, 380, 150, 400, 66, 316, 105, 255, steps=16)
    return g


def fw_parenright() -> Glyph:
    """）U+FF09 全角右括号：GB/T 后半标点居左半，紧贴前置内容。"""
    g = Glyph("uniFF09", advance=CJK_ADV, unicode=0xFF09, note="）：全角右括号")
    band(g, 210, 380, 150, 400, 66, 316, 285, 75, steps=16)
    return g


def fw_corner_left() -> Glyph:
    """「U+300C 全角直角引号（左）：竖笔在左、横笔在顶，构成左上角。"""
    g = Glyph("uni300C", advance=CJK_ADV, unicode=0x300C, note="「：全角左直角引号")
    g.vbar(600, 48, 808, weight=W_MAIN)
    g.hbar(600, 900, 760, weight=W_MAIN)
    return g


def fw_corner_right() -> Glyph:
    """」U+300D 全角直角引号（右）：竖笔在右、横笔在底，构成右下角。"""
    g = Glyph("uni300D", advance=CJK_ADV, unicode=0x300D, note="」：全角右直角引号")
    g.vbar(400, 0, 760, weight=W_MAIN)
    g.hbar(100, 400, 48, weight=W_MAIN)
    return g


def fw_lenticular_left() -> Glyph:
    """【U+3010 全角鱼尾括号（左）：实心体块 + 右侧 V 形收口。"""
    g = Glyph("uni3010", advance=CJK_ADV, unicode=0x3010, note="【：全角鱼尾括号")
    g.poly([(552, 0), (900, 0), (700, 400), (900, 800), (552, 800)])
    return g


def fw_lenticular_right() -> Glyph:
    """】U+3011 全角鱼尾括号（右）：实心体块 + 左侧 V 形收口。"""
    g = Glyph("uni3011", advance=CJK_ADV, unicode=0x3011, note="】：全角鱼尾括号")
    g.poly([(448, 0), (100, 0), (300, 400), (100, 800), (448, 800)])
    return g


# --------------------------------------------------------------------------
# 半角标点
# --------------------------------------------------------------------------
def hw_period() -> Glyph:
    """period . 句点：贴基线圆点。"""
    g = Glyph("period", advance=ADV_NARROW, unicode=0x2E, note=".：句点")
    disc(g, 120, 52, 52)
    return g


def hw_comma() -> Glyph:
    """comma , 逗号：圆头 + 左下出锋尾，尾低于基线。"""
    g = Glyph("comma", advance=ADV_NARROW, unicode=0x2C, note=",：逗号")
    comma_mark(g, 120, 52, 52, tip=(74, -54), w_root=70, w_tip=12)
    return g


def hw_exclam() -> Glyph:
    """exclam ! 叹号：竖笔 + 独立圆点，顶端与大写顶线齐平。"""
    g = Glyph("exclam", advance=ADV_NARROW, unicode=0x21, note="!：叹号")
    g.vbar(120, 240, CAP_TOP, weight=W_MAIN)
    disc(g, 120, 52, 52)
    return g


def hw_question() -> Glyph:
    """question ? 问号：开口环带成钩，竖笔成干，底部独立圆点。"""
    g = Glyph("question", advance=ADV_WIDE, unicode=0x3F, note="?：问号")
    band(g, 150, 586, 130, 130, 46, 46, 150, -80, steps=18)
    g.vbar(165, 320, 530, weight=W_SECOND)
    disc(g, 150, 52, 52)
    return g


def hw_colon() -> Glyph:
    """colon : 冒号：x 高处与基线各一个圆点。"""
    g = Glyph("colon", advance=ADV_NARROW, unicode=0x3A, note=":：冒号")
    disc(g, 120, 400, 52)
    disc(g, 120, 52, 52)
    return g


def hw_semicolon() -> Glyph:
    """semicolon ; 分号：上圆点 + 下逗号。"""
    g = Glyph("semicolon", advance=ADV_NARROW, unicode=0x3B, note=";：分号")
    disc(g, 120, 400, 52)
    comma_mark(g, 120, 52, 52, tip=(74, -54), w_root=70, w_tip=12)
    return g


def hw_parenleft() -> Glyph:
    """parenleft ( 左括号：开口环带，凸面朝左。"""
    g = Glyph("parenleft", advance=ADV_WIDE, unicode=0x28, note="(：左括号")
    band(g, 250, 358, 190, 358, 106, 274, 100, 260, steps=16)
    return g


def hw_parenright() -> Glyph:
    """parenright ) 右括号：开口环带，凸面朝右。"""
    g = Glyph("parenright", advance=ADV_WIDE, unicode=0x29, note=")：右括号")
    band(g, 50, 358, 190, 358, 106, 274, -80, 80, steps=16)
    return g


def hw_hyphen() -> Glyph:
    """hyphen - 连字符：短横，置于 x 高中部。"""
    g = Glyph("hyphen", advance=ADV_HYPHEN, unicode=0x2D, note="-：连字符")
    g.hbar(60, 260, 300, weight=W_THIN)
    return g


def hw_emdash() -> Glyph:
    """emdash — 长破折号：1 em 宽通栏横画。"""
    g = Glyph("emdash", advance=ADV_EMDASH, unicode=0x2014, note="—：长破折号")
    g.hbar(BODY_L, BODY_R, 300, weight=W_MAIN)
    return g


def hw_quotedbl() -> Glyph:
    """quotedbl " 双引号：两枚上斜楔形，顶部与大写顶线齐平。"""
    g = Glyph("quotedbl", advance=ADV_QUOTEDBL, unicode=0x22, note='"：双引号')
    g.dot(80, 592, w=90, h=236, slant=28)
    g.dot(210, 592, w=90, h=236, slant=28)
    return g


def hw_quotesingle() -> Glyph:
    """quotesingle ' 单引号：一枚上斜楔形。"""
    g = Glyph("quotesingle", advance=ADV_NARROW, unicode=0x27, note="'：单引号")
    g.dot(110, 592, w=96, h=236, slant=28)
    return g


def hw_ampersand() -> Glyph:
    """ampersand & & 号：左上闭环 + 右上斜脊 + 下方开口环带。"""
    g = Glyph("ampersand", advance=ADV_AMP, unicode=0x26, note="&：号")
    # 左上闭环（环带自动成洞）
    g.ring(
        ellipse_points(130, 570, 118, 124, count=16),
        ellipse_points(130, 570, 34, 40, count=16),
    )
    # 右上出发的斜脊，向左下贯穿并埋入下碗
    g.diag(285, 700, 60, 195, weight=W_THIN)
    # 下方开口环带（左上到右上开口，露出碗心）
    band(g, 170, 175, 150, 175, 66, 91, 110, 390, steps=18)
    return g


# --------------------------------------------------------------------------
# 组装
# --------------------------------------------------------------------------
def build() -> list[Glyph]:
    """返回本 lane 的全部字形（全角 12 + 半角 13 = 25）。"""
    return [
        # 全角 12
        fw_ideographic_full_stop(),
        fw_comma(),
        fw_ideographic_comma(),
        fw_exclamation(),
        fw_question(),
        fw_colon(),
        fw_semicolon(),
        fw_parenleft(),
        fw_parenright(),
        fw_corner_left(),
        fw_corner_right(),
        fw_lenticular_left(),
        fw_lenticular_right(),
        # 半角 13
        hw_period(),
        hw_comma(),
        hw_exclam(),
        hw_question(),
        hw_colon(),
        hw_semicolon(),
        hw_parenleft(),
        hw_parenright(),
        hw_hyphen(),
        hw_emdash(),
        hw_quotedbl(),
        hw_quotesingle(),
        hw_ampersand(),
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-latin-punct.ufo"


if __name__ == "__main__":
    _target = target_ufo()
    _target.parent.mkdir(parents=True, exist_ok=True)
    write_ufo(_target, build())
    print(f"[recipe] 已写出 {_target}")
