"""HK Poster Heavy —— hkposter-auto-legacy29.py 恢复层（29 字）。

这批字在 v0.6 里**相对 v0.5 成了回退**（新生成器过不了质量闸 ⇒ 丢字）。
逐字对比后确认：**v0.5 的几何反而更好** —— 新生成器修掉四个真 bug 后，
这 29 个字的接头延长把相邻横画从「刚好相接」推成了「x 区间重叠」，
于是 `check_hcounters` 判白口 FAIL（典型：`擼` U+64FC，y=597.5 / y=620 两横）。

所以这里的原语**逐字照抄**自提交 `40fe068757185bf0bdd7fec3aa702d5041b5cc78` 的
`font-src/src/hkposter-auto-cjk.py` / `hkposter-auto-joyo.py`，
未做任何改动 —— 它们在 v0.5 已经过了全部门禁（`verify_all` 14/14）。
恢复它们等于回到一个**已知通过**的状态，而不是新造一个几何。

抽取脚本：`font-src/scripts/hk_extract_legacy.py`（可复现）。

字表
----
* `喋` U+558B —— CJK UNIFIED IDEOGRAPH-558B
* `嫱` U+5AF1 —— CJK UNIFIED IDEOGRAPH-5AF1
* `嬗` U+5B17 —— CJK UNIFIED IDEOGRAPH-5B17
* `帏` U+5E0F —— CJK UNIFIED IDEOGRAPH-5E0F
* `撾` U+64BE —— CJK UNIFIED IDEOGRAPH-64BE
* `擼` U+64FC —— CJK UNIFIED IDEOGRAPH-64FC
* `欞` U+6B1E —— CJK UNIFIED IDEOGRAPH-6B1E
* `毽` U+6BFD —— CJK UNIFIED IDEOGRAPH-6BFD
* `氆` U+6C06 —— CJK UNIFIED IDEOGRAPH-6C06
* `氪` U+6C2A —— CJK UNIFIED IDEOGRAPH-6C2A
* `犍` U+728D —— CJK UNIFIED IDEOGRAPH-728D
* `矓` U+77D3 —— CJK UNIFIED IDEOGRAPH-77D3
* `碟` U+789F —— CJK UNIFIED IDEOGRAPH-789F
* `蔷` U+8537 —— CJK UNIFIED IDEOGRAPH-8537
* `襢` U+8962 —— CJK UNIFIED IDEOGRAPH-8962
* `谍` U+8C0D —— CJK UNIFIED IDEOGRAPH-8C0D
* `輿` U+8F3F —— CJK UNIFIED IDEOGRAPH-8F3F
* `轀` U+8F40 —— CJK UNIFIED IDEOGRAPH-8F40
* `鄙` U+9119 —— CJK UNIFIED IDEOGRAPH-9119
* `醴` U+91B4 —— CJK UNIFIED IDEOGRAPH-91B4
* `馘` U+9998 —— CJK UNIFIED IDEOGRAPH-9998
* `魝` U+9B5D —— CJK UNIFIED IDEOGRAPH-9B5D
* `鯡` U+9BE1 —— CJK UNIFIED IDEOGRAPH-9BE1
* `鳟` U+9CDF —— CJK UNIFIED IDEOGRAPH-9CDF
* `鸪` U+9E2A —— CJK UNIFIED IDEOGRAPH-9E2A
* `鼾` U+9F3E —— CJK UNIFIED IDEOGRAPH-9F3E
* `尊` U+5C0A —— CJK UNIFIED IDEOGRAPH-5C0A
* `論` U+8AD6 —— CJK UNIFIED IDEOGRAPH-8AD6
* `輪` U+8F2A —— CJK UNIFIED IDEOGRAPH-8F2A

运行：python font-src/src/hkposter-auto-legacy29.py
"""

from __future__ import annotations

import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, write_ufo  # noqa: E402

def g_cjk_unified_ideograph_558b() -> Glyph:
    """喋 U+558B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni558B", advance=1000, unicode=0x558B, note="喋：自动生成")
    g.vbar(142.4, 363.8, 573.3, weight=96.0)
    g.hbar(150.4, 305.2, 575.8, weight=64.0)
    g.vbar(277.9, 454.3, 593.2, weight=64.0)
    g.hbar(174.7, 288.8, 417.8, weight=96.0)
    g.diag(288.8, 435.0, 296.5, 440.4, weight=96.0)
    g.hbar(317.5, 861.4, 591.0, weight=64.0)
    g.diag(520.0, 724.6, 557.9, 695.4, weight=64.0)
    g.vbar(563.5, 466.1, 695.4, weight=64.0)
    g.diag(668.0, 772.0, 702.1, 733.3, weight=76.0)
    g.diag(702.1, 733.3, 677.6, 545.7, weight=76.0)
    g.diag(677.6, 545.7, 662.2, 526.3, weight=76.0)
    g.hbar(587.7, 686.4, 495.1, weight=64.0)
    g.vbar(689.8, 506.3, 521.7, weight=64.0)
    g.diag(400.1, 698.5, 483.7, 393.1, weight=64.0)
    g.hbar(483.7, 787.9, 400.3, weight=64.0)
    g.hbar(308.2, 871.1, 264.3, weight=64.0)
    g.diag(535.5, 373.5, 590.2, 314.8, weight=96.0)
    g.vbar(579.3, -52.0, 314.8, weight=96.0)
    g.diag(534.5, 245.9, 265.6, 33.1, weight=64.0)
    g.diag(592.5, 252.6, 942.6, 75.7, weight=64.0)
    return g

def g_cjk_unified_ideograph_5af1() -> Glyph:
    """嫱 U+5AF1 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5AF1", advance=1000, unicode=0x5AF1, note="嫱：自动生成")
    g.vbar(265.0, 624.1, 773.8, weight=64.0)
    g.diag(268.7, 624.1, 206.4, 308.0, weight=64.0)
    g.diag(206.4, 308.0, 381.0, 176.0, weight=64.0)
    g.hbar(381.0, 430.3, 181.5, weight=64.0)
    g.diag(341.1, 511.0, 317.1, 390.4, weight=64.0)
    g.diag(317.1, 390.4, 131.7, 80.5, weight=64.0)
    g.hbar(74.8, 124.9, 425.4, weight=96.0)
    g.hbar(124.9, 338.0, 449.9, weight=96.0)
    g.diag(483.2, 620.5, 534.6, 660.0, weight=96.0)
    g.hbar(534.6, 753.9, 681.9, weight=96.0)
    g.diag(753.9, 703.8, 800.2, 674.6, weight=96.0)
    g.diag(611.0, 820.0, 657.2, 779.8, weight=84.0)
    g.vbar(655.2, 487.1, 779.8, weight=84.0)
    g.diag(653.2, 487.1, 636.5, 463.5, weight=84.0)
    g.diag(488.4, 640.3, 538.3, 540.1, weight=76.0)
    g.vbar(535.4, 466.3, 540.1, weight=76.0)
    g.diag(768.4, 675.4, 804.4, 604.0, weight=64.0)
    g.hbar(713.1, 804.4, 586.2, weight=64.0)
    g.hbar(418.4, 895.6, 449.2, weight=96.0)
    g.diag(895.6, 461.0, 855.3, 386.7, weight=96.0)
    g.vbar(480.5, 35.5, 326.3, weight=64.0)
    g.hbar(466.6, 864.3, 339.7, weight=64.0)
    g.vbar(841.4, 53.5, 350.1, weight=64.0)
    g.hbar(770.2, 818.4, 51.2, weight=64.0)
    g.vbar(579.5, 129.6, 251.5, weight=64.0)
    g.hbar(583.5, 730.5, 253.3, weight=64.0)
    g.diag(730.5, 254.2, 687.4, 190.0, weight=64.0)
    g.diag(614.9, 145.3, 622.8, 153.3, weight=64.0)
    g.hbar(622.8, 728.1, 167.2, weight=64.0)
    g.hbar(532.4, 800.7, 69.2, weight=64.0)
    return g

def g_cjk_unified_ideograph_5b17() -> Glyph:
    """嬗 U+5B17 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5B17", advance=1000, unicode=0x5B17, note="嬗：自动生成")
    g.vbar(249.1, 605.7, 766.4, weight=64.0)
    g.diag(255.3, 605.7, 204.1, 273.6, weight=64.0)
    g.diag(204.1, 273.6, 399.7, 104.2, weight=64.0)
    g.diag(343.1, 524.2, 312.8, 363.0, weight=64.0)
    g.diag(312.8, 363.0, 124.7, 62.5, weight=64.0)
    g.hbar(73.1, 123.2, 395.5, weight=96.0)
    g.hbar(123.2, 341.2, 424.3, weight=96.0)
    g.dot(637.0, 788.7, w=64.0, h=83.2, slant=-14.0)
    g.hbar(430.5, 880.2, 692.4, weight=64.0)
    g.vbar(497.0, 338.5, 588.7, weight=64.0)
    g.hbar(507.9, 838.8, 604.5, weight=64.0)
    g.vbar(811.3, 381.0, 620.3, weight=64.0)
    g.vbar(785.4, 367.3, 381.0, weight=64.0)
    g.diag(569.5, 532.1, 587.5, 520.4, weight=64.0)
    g.vbar(599.3, 427.9, 520.4, weight=64.0)
    g.diag(607.2, 533.1, 611.4, 531.0, weight=64.0)
    g.hbar(611.4, 718.5, 535.2, weight=64.0)
    g.diag(718.5, 539.3, 681.7, 481.5, weight=64.0)
    g.vbar(626.3, 448.7, 455.9, weight=64.0)
    g.hbar(627.5, 714.4, 460.3, weight=64.0)
    g.hbar(554.6, 745.2, 381.7, weight=64.0)
    g.vbar(524.8, 78.4, 284.9, weight=64.0)
    g.hbar(538.7, 543.8, 281.9, weight=64.0)
    g.hbar(543.8, 801.0, 288.3, weight=64.0)
    g.vbar(778.5, 119.8, 295.9, weight=64.0)
    g.diag(755.9, 119.8, 759.1, 102.3, weight=64.0)
    g.diag(564.5, 182.7, 574.2, 194.8, weight=64.0)
    g.hbar(574.2, 700.5, 201.6, weight=64.0)
    g.diag(568.5, 103.2, 579.8, 112.5, weight=64.0)
    g.hbar(579.8, 706.2, 121.0, weight=64.0)
    g.diag(706.2, 129.5, 717.4, 117.1, weight=64.0)
    g.hbar(404.7, 926.9, 13.4, weight=76.0)
    return g

def g_cjk_unified_ideograph_5e0f() -> Glyph:
    """帏 U+5E0F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5E0F", advance=1000, unicode=0x5E0F, note="帏：自动生成")
    g.vbar(151.3, 328.2, 567.1, weight=64.0)
    g.diag(178.0, 565.6, 196.0, 554.7, weight=64.0)
    g.hbar(196.0, 317.4, 567.1, weight=64.0)
    g.diag(317.4, 579.4, 456.6, 350.3, weight=64.0)
    g.hbar(303.3, 456.6, 378.9, weight=64.0)
    g.vbar(248.0, 543.0, 805.5, weight=64.0)
    g.vbar(260.6, 45.5, 543.0, weight=64.0)
    g.hbar(416.2, 737.6, 635.8, weight=96.0)
    g.vbar(741.4, 576.9, 664.8, weight=96.0)
    g.diag(442.9, 526.3, 510.3, 490.9, weight=96.0)
    g.hbar(510.3, 731.3, 515.8, weight=96.0)
    g.diag(731.3, 540.6, 689.4, 474.3, weight=96.0)
    g.hbar(425.2, 470.0, 368.0, weight=96.0)
    g.hbar(470.0, 876.8, 380.2, weight=96.0)
    g.diag(876.8, 401.6, 794.1, 170.7, weight=96.0)
    g.diag(794.1, 170.7, 698.2, 283.6, weight=96.0)
    g.diag(570.7, 820.0, 617.3, 782.7, weight=96.0)
    g.vbar(613.8, 0.0, 782.7, weight=96.0)
    return g

def g_cjk_unified_ideograph_64be() -> Glyph:
    """撾 U+64BE —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni64BE", advance=1000, unicode=0x64BE, note="撾：自动生成")
    g.hbar(107.2, 323.1, 527.1, weight=96.0)
    g.vbar(230.8, 532.9, 762.3, weight=96.0)
    g.vbar(240.8, 68.5, 532.9, weight=96.0)
    g.diag(237.1, 68.5, 127.6, 126.9, weight=96.0)
    g.hbar(125.5, 127.6, 127.0, weight=96.0)
    g.hbar(60.0, 102.4, 264.5, weight=96.0)
    g.diag(102.4, 264.9, 297.1, 428.8, weight=96.0)
    g.vbar(563.0, 462.2, 654.3, weight=64.0)
    g.diag(592.7, 462.2, 573.7, 445.2, weight=64.0)
    g.hbar(587.2, 773.6, 650.1, weight=64.0)
    g.vbar(760.1, 486.1, 660.3, weight=64.0)
    g.diag(746.6, 486.1, 728.0, 466.4, weight=64.0)
    g.vbar(649.6, 473.8, 582.0, weight=64.0)
    g.diag(665.8, 473.8, 646.0, 460.6, weight=64.0)
    g.diag(677.8, 551.2, 683.2, 559.7, weight=96.0)
    g.hbar(683.2, 734.7, 569.4, weight=96.0)
    g.diag(487.0, 424.9, 499.1, 415.2, weight=64.0)
    g.vbar(506.1, 213.9, 415.2, weight=64.0)
    g.hbar(529.4, 640.5, 424.5, weight=64.0)
    g.hbar(640.5, 845.7, 441.8, weight=64.0)
    g.vbar(829.0, 195.2, 453.7, weight=64.0)
    g.hbar(750.1, 812.3, 207.4, weight=64.0)
    g.diag(573.7, 362.3, 593.0, 346.9, weight=64.0)
    g.vbar(604.1, 239.9, 346.9, weight=64.0)
    g.hbar(616.1, 740.8, 359.9, weight=64.0)
    g.diag(740.8, 365.2, 697.1, 300.6, weight=64.0)
    g.hbar(629.6, 745.3, 263.5, weight=64.0)
    g.dot(405.1, 594.1, w=96.0, h=109.8, slant=-14.0)
    g.hbar(296.1, 416.0, 397.1, weight=64.0)
    g.vbar(399.7, 303.1, 407.8, weight=64.0)
    g.vbar(403.2, 202.5, 303.1, weight=64.0)
    g.diag(422.9, 202.5, 407.0, 189.8, weight=64.0)
    g.hbar(303.9, 476.8, 148.7, weight=96.0)
    g.hbar(476.8, 940.0, 109.2, weight=96.0)
    return g

def g_cjk_unified_ideograph_64fc() -> Glyph:
    """擼 U+64FC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni64FC", advance=1000, unicode=0x64FC, note="擼：自动生成")
    g.hbar(158.6, 405.9, 542.7, weight=96.0)
    g.vbar(283.1, 553.3, 780.9, weight=76.0)
    g.vbar(293.6, 102.1, 553.3, weight=76.0)
    g.diag(290.6, 102.1, 198.0, 148.2, weight=76.0)
    g.hbar(195.9, 198.0, 148.2, weight=76.0)
    g.hbar(111.4, 154.1, 256.8, weight=92.0)
    g.diag(154.1, 255.5, 391.4, 449.1, weight=92.0)
    g.diag(600.5, 820.0, 625.2, 783.9, weight=96.0)
    g.diag(625.2, 783.9, 492.3, 632.7, weight=96.0)
    g.diag(605.9, 716.4, 615.4, 725.8, weight=64.0)
    g.hbar(615.4, 736.5, 733.0, weight=64.0)
    g.diag(736.5, 740.2, 638.6, 630.0, weight=64.0)
    g.vbar(493.2, 410.0, 592.7, weight=64.0)
    g.hbar(502.3, 616.4, 597.5, weight=64.0)
    g.hbar(616.4, 827.2, 620.0, weight=64.0)
    g.vbar(789.3, 437.3, 636.0, weight=64.0)
    g.hbar(554.1, 719.5, 525.5, weight=64.0)
    g.diag(618.6, 595.5, 636.8, 580.9, weight=84.0)
    g.vbar(634.5, 480.0, 580.9, weight=84.0)
    g.diag(632.3, 480.0, 621.4, 467.3, weight=84.0)
    g.diag(545.9, 426.4, 554.5, 436.1, weight=64.0)
    g.hbar(554.5, 734.1, 450.8, weight=64.0)
    g.diag(432.3, 369.1, 391.4, 260.0, weight=64.0)
    g.dot(546.4, 352.7, w=64.0, h=68.6, slant=-14.0)
    g.dot(678.6, 371.8, w=76.0, h=78.7, slant=-14.0)
    g.dot(834.5, 367.3, w=92.0, h=119.6, slant=-14.0)
    g.diag(501.4, 269.1, 531.8, 241.9, weight=84.0)
    g.vbar(524.8, 15.5, 241.9, weight=84.0)
    g.hbar(544.1, 762.2, 264.3, weight=64.0)
    g.vbar(751.8, 0.0, 283.2, weight=64.0)
    g.diag(550.5, 157.3, 559.4, 168.5, weight=84.0)
    g.hbar(559.4, 680.5, 172.0, weight=84.0)
    g.diag(545.0, 46.4, 564.6, 62.1, weight=92.0)
    g.hbar(564.6, 698.6, 66.9, weight=92.0)
    return g

def g_cjk_unified_ideograph_6b1e() -> Glyph:
    """欞 U+6B1E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6B1E", advance=1000, unicode=0x6B1E, note="欞：自动生成")
    g.hbar(101.2, 371.9, 492.0, weight=96.0)
    g.vbar(250.8, 530.7, 803.5, weight=64.0)
    g.vbar(265.4, 0.0, 530.7, weight=64.0)
    g.diag(255.5, 463.9, 68.2, 149.4, weight=64.0)
    g.dot(338.9, 369.2, w=64.0, h=83.2, slant=-14.0)
    g.hbar(525.2, 796.9, 796.7, weight=76.0)
    g.dot(426.7, 621.6, w=96.0, h=124.8, slant=0.0)
    g.hbar(471.9, 589.1, 674.2, weight=64.0)
    g.hbar(589.1, 901.4, 702.1, weight=64.0)
    g.diag(901.4, 724.4, 827.0, 628.8, weight=64.0)
    g.diag(615.5, 756.9, 640.7, 730.7, weight=76.0)
    g.vbar(641.7, 532.8, 730.7, weight=76.0)
    g.dot(540.3, 596.3, w=64.0, h=61.5, slant=-14.0)
    g.dot(526.7, 530.3, w=64.0, h=57.9, slant=-14.0)
    g.dot(740.7, 641.4, w=64.0, h=65.1, slant=-14.0)
    g.dot(741.1, 570.6, w=64.0, h=59.0, slant=-14.0)
    g.diag(403.9, 441.5, 423.3, 428.0, weight=64.0)
    g.vbar(435.5, 334.8, 428.0, weight=64.0)
    g.diag(447.6, 429.9, 453.5, 439.4, weight=64.0)
    g.hbar(453.5, 543.3, 447.3, weight=64.0)
    g.diag(543.3, 455.2, 505.8, 393.0, weight=64.0)
    g.dot(501.9, 361.5, w=64.0, h=83.2, slant=-14.0)
    g.diag(571.8, 473.6, 592.2, 454.2, weight=64.0)
    g.vbar(601.9, 374.6, 454.2, weight=64.0)
    g.hbar(605.8, 608.0, 473.1, weight=64.0)
    g.hbar(608.0, 705.2, 479.7, weight=64.0)
    g.diag(705.2, 486.7, 672.7, 432.8, weight=64.0)
    g.diag(625.2, 395.0, 631.5, 405.1, weight=64.0)
    g.hbar(631.5, 708.6, 407.3, weight=64.0)
    g.diag(737.8, 512.4, 761.0, 491.0, weight=64.0)
    g.vbar(771.7, 408.5, 491.0, weight=64.0)
    g.diag(778.5, 502.7, 788.1, 513.8, weight=64.0)
    g.hbar(788.1, 886.2, 516.8, weight=64.0)
    g.diag(886.2, 519.7, 839.6, 462.9, weight=64.0)
    g.diag(793.1, 440.6, 801.0, 431.7, weight=64.0)
    g.hbar(801.0, 882.3, 432.3, weight=64.0)
    g.hbar(524.3, 789.2, 318.3, weight=64.0)
    g.diag(619.4, 295.0, 646.8, 271.4, weight=64.0)
    g.vbar(648.7, 105.8, 271.4, weight=64.0)
    g.diag(650.5, 105.8, 633.9, 94.1, weight=64.0)
    g.diag(492.2, 259.1, 511.4, 227.5, weight=96.0)
    g.diag(511.4, 227.5, 409.8, 110.6, weight=96.0)
    g.diag(508.7, 165.9, 516.6, 170.4, weight=64.0)
    g.diag(516.6, 170.4, 575.7, 132.0, weight=64.0)
    g.diag(808.6, 285.3, 793.7, 278.2, weight=64.0)
    g.diag(793.7, 278.2, 698.9, 147.5, weight=64.0)
    g.dot(813.0, 180.5, w=64.0, h=83.2, slant=-14.0)
    g.hbar(395.2, 931.8, 57.3, weight=84.0)
    return g

def g_cjk_unified_ideograph_6bfd() -> Glyph:
    """毽 U+6BFD —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6BFD", advance=1000, unicode=0x6BFD, note="毽：自动生成")
    g.hbar(352.1, 419.8, 716.5, weight=96.0)
    g.diag(352.1, 715.0, 186.7, 587.8, weight=96.0)
    g.diag(186.7, 587.8, 142.2, 559.6, weight=96.0)
    g.hbar(119.6, 379.7, 469.6, weight=64.0)
    g.hbar(60.0, 393.1, 328.3, weight=64.0)
    g.diag(232.7, 593.5, 367.9, 389.3, weight=64.0)
    g.diag(367.9, 389.3, 943.6, -34.5, weight=64.0)
    g.vbar(939.2, -34.5, 213.1, weight=64.0)
    g.hbar(559.6, 810.0, 664.8, weight=64.0)
    g.vbar(783.0, 505.8, 687.7, weight=64.0)
    g.diag(755.9, 505.8, 755.0, 505.1, weight=64.0)
    g.hbar(545.2, 916.4, 561.6, weight=64.0)
    g.hbar(551.4, 801.2, 465.5, weight=64.0)
    g.hbar(582.2, 774.5, 372.0, weight=76.0)
    g.hbar(544.2, 839.3, 274.8, weight=64.0)
    g.diag(630.6, 803.2, 681.0, 772.8, weight=96.0)
    g.vbar(675.8, 173.0, 772.8, weight=96.0)
    g.hbar(379.7, 474.2, 565.5, weight=96.0)
    g.diag(474.2, 575.5, 337.1, 121.1, weight=96.0)
    g.diag(337.1, 121.1, 379.7, 144.3, weight=96.0)
    g.hbar(345.8, 888.6, 196.2, weight=64.0)
    return g

def g_cjk_unified_ideograph_6c06() -> Glyph:
    """氆 U+6C06 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6C06", advance=1000, unicode=0x6C06, note="氆：自动生成")
    g.hbar(393.3, 453.5, 693.8, weight=84.0)
    g.diag(393.3, 694.2, 135.7, 527.5, weight=84.0)
    g.diag(135.7, 527.5, 136.2, 528.5, weight=84.0)
    g.hbar(128.9, 434.8, 445.5, weight=64.0)
    g.hbar(60.0, 449.4, 296.7, weight=64.0)
    g.diag(269.8, 576.5, 388.6, 348.1, weight=64.0)
    g.diag(388.6, 348.1, 933.2, -32.4, weight=64.0)
    g.vbar(936.6, -32.4, 196.5, weight=64.0)
    g.dot(562.6, 730.0, w=84.0, h=104.1, slant=-14.0)
    g.diag(747.9, 817.6, 768.2, 784.8, weight=84.0)
    g.diag(768.2, 784.8, 676.9, 688.2, weight=84.0)
    g.hbar(514.1, 823.1, 636.0, weight=84.0)
    g.hbar(615.4, 622.7, 585.1, weight=76.0)
    g.diag(615.4, 584.2, 582.1, 441.5, weight=76.0)
    g.diag(582.1, 441.5, 588.2, 445.0, weight=76.0)
    g.diag(679.0, 610.9, 697.3, 590.4, weight=64.0)
    g.vbar(694.6, 466.5, 590.4, weight=64.0)
    g.diag(691.9, 466.5, 676.9, 458.5, weight=64.0)
    g.dot(511.0, 516.0, w=84.0, h=79.8, slant=-14.0)
    g.diag(789.7, 604.7, 807.4, 576.5, weight=64.0)
    g.diag(807.4, 576.5, 739.6, 497.2, weight=64.0)
    g.hbar(459.8, 887.8, 415.7, weight=84.0)
    g.vbar(539.7, 96.3, 335.4, weight=64.0)
    g.diag(575.7, 332.2, 583.1, 327.3, weight=64.0)
    g.hbar(583.1, 784.0, 337.7, weight=64.0)
    g.vbar(774.8, 133.1, 348.1, weight=64.0)
    g.hbar(717.7, 765.7, 138.7, weight=64.0)
    g.diag(586.1, 231.0, 598.2, 245.7, weight=64.0)
    g.hbar(598.2, 705.1, 247.2, weight=64.0)
    g.diag(584.0, 141.2, 594.8, 156.7, weight=64.0)
    g.hbar(594.8, 726.0, 157.8, weight=64.0)
    return g

def g_cjk_unified_ideograph_6c2a() -> Glyph:
    """氪 U+6C2A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6C2A", advance=1000, unicode=0x6C2A, note="氪：自动生成")
    g.vbar(310.1, 744.3, 771.6, weight=96.0)
    g.diag(314.0, 771.6, 166.2, 552.4, weight=96.0)
    g.hbar(312.5, 604.1, 731.8, weight=64.0)
    g.diag(295.5, 672.5, 371.0, 620.7, weight=64.0)
    g.hbar(371.0, 485.6, 633.7, weight=64.0)
    g.vbar(490.2, 605.3, 646.6, weight=64.0)
    g.hbar(194.3, 328.3, 556.9, weight=64.0)
    g.diag(328.3, 542.2, 580.4, 370.9, weight=64.0)
    g.diag(580.4, 370.9, 871.5, -48.1, weight=64.0)
    g.vbar(876.3, -48.1, 152.4, weight=64.0)
    g.diag(186.3, 359.4, 231.5, 409.7, weight=64.0)
    g.hbar(231.5, 503.5, 428.0, weight=64.0)
    g.diag(314.2, 496.2, 349.7, 467.0, weight=96.0)
    g.vbar(342.7, 364.9, 467.0, weight=96.0)
    g.diag(335.7, 364.9, 324.1, 355.7, weight=96.0)
    g.dot(225.4, 257.7, w=96.0, h=124.8, slant=-14.0)
    g.hbar(232.9, 248.2, 325.9, weight=64.0)
    g.hbar(248.2, 479.2, 336.0, weight=64.0)
    g.diag(479.2, 349.0, 419.8, 264.0, weight=64.0)
    g.diag(265.4, 221.2, 278.7, 214.5, weight=64.0)
    g.hbar(278.7, 453.5, 235.1, weight=64.0)
    g.vbar(273.2, 141.2, 188.3, weight=96.0)
    g.diag(281.1, 141.2, 118.9, 0.0, weight=96.0)
    g.diag(360.0, 210.2, 359.4, 210.7, weight=64.0)
    g.vbar(383.4, 19.7, 210.7, weight=64.0)
    g.hbar(407.3, 574.8, 24.3, weight=64.0)
    g.vbar(583.0, 28.8, 182.5, weight=64.0)
    return g

def g_cjk_unified_ideograph_728d() -> Glyph:
    """犍 U+728D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni728D", advance=1000, unicode=0x728D, note="犍：自动生成")
    g.diag(165.3, 563.3, 172.4, 594.6, weight=92.0)
    g.diag(172.4, 594.6, 75.0, 423.0, weight=92.0)
    g.hbar(173.3, 313.8, 549.5, weight=96.0)
    g.hbar(313.8, 355.5, 564.8, weight=96.0)
    g.vbar(245.4, 7.1, 812.9, weight=64.0)
    g.hbar(60.0, 110.1, 253.1, weight=96.0)
    g.diag(110.1, 251.6, 326.6, 422.3, weight=96.0)
    g.hbar(545.1, 797.6, 644.0, weight=64.0)
    g.vbar(780.1, 499.2, 659.5, weight=64.0)
    g.diag(762.6, 499.2, 747.0, 488.1, weight=64.0)
    g.hbar(477.4, 902.9, 551.0, weight=64.0)
    g.diag(544.1, 503.8, 589.9, 432.0, weight=64.0)
    g.hbar(589.9, 794.5, 458.1, weight=64.0)
    g.hbar(496.7, 730.2, 358.6, weight=76.0)
    g.diag(730.2, 357.7, 756.8, 296.9, weight=76.0)
    g.hbar(490.6, 828.7, 247.0, weight=64.0)
    g.diag(622.3, 807.9, 672.2, 776.3, weight=96.0)
    g.vbar(661.4, 134.3, 776.3, weight=96.0)
    g.hbar(331.6, 382.9, 535.3, weight=64.0)
    g.hbar(382.9, 459.9, 536.9, weight=64.0)
    g.diag(459.9, 545.1, 404.0, 396.3, weight=64.0)
    g.diag(404.0, 396.3, 495.8, 349.9, weight=64.0)
    g.diag(495.8, 349.9, 280.2, 91.2, weight=64.0)
    g.hbar(303.3, 940.0, 170.0, weight=64.0)
    return g

def g_cjk_unified_ideograph_77d3() -> Glyph:
    """矓 U+77D3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni77D3", advance=1000, unicode=0x77D3, note="矓：自动生成")
    g.diag(60.0, 724.4, 104.0, 668.3, weight=96.0)
    g.vbar(96.6, 128.0, 668.3, weight=96.0)
    g.diag(116.3, 709.8, 214.1, 511.3, weight=64.0)
    g.vbar(226.7, 129.0, 511.3, weight=64.0)
    g.diag(124.6, 503.3, 135.0, 517.1, weight=96.0)
    g.hbar(135.0, 195.5, 518.0, weight=96.0)
    g.diag(123.6, 359.4, 133.3, 374.0, weight=96.0)
    g.hbar(133.3, 199.7, 375.6, weight=96.0)
    g.hbar(115.3, 179.6, 167.3, weight=96.0)
    g.diag(179.6, 177.5, 191.4, 164.5, weight=96.0)
    g.dot(454.6, 780.1, w=96.0, h=111.6, slant=-14.0)
    g.hbar(342.6, 546.9, 674.8, weight=96.0)
    g.dot(378.0, 566.4, w=96.0, h=66.3, slant=-14.0)
    g.diag(504.2, 645.1, 523.0, 611.8, weight=96.0)
    g.diag(523.0, 611.8, 466.6, 511.7, weight=96.0)
    g.hbar(292.5, 570.9, 483.0, weight=96.0)
    g.diag(340.5, 389.7, 372.1, 351.5, weight=64.0)
    g.vbar(352.6, 15.4, 351.5, weight=64.0)
    g.hbar(381.5, 388.4, 381.6, weight=64.0)
    g.diag(381.5, 382.9, 483.2, 281.2, weight=64.0)
    g.diag(483.2, 281.2, 329.1, 78.9, weight=64.0)
    g.hbar(329.1, 410.3, 63.3, weight=64.0)
    g.diag(387.4, 257.3, 394.7, 268.7, weight=64.0)
    g.hbar(394.7, 451.0, 272.9, weight=64.0)
    g.diag(383.2, 163.4, 389.4, 175.8, weight=76.0)
    g.hbar(389.4, 457.3, 176.9, weight=76.0)
    g.hbar(681.4, 845.1, 703.5, weight=96.0)
    g.diag(627.2, 785.9, 662.7, 755.6, weight=96.0)
    g.vbar(652.7, 564.6, 755.6, weight=96.0)
    g.hbar(642.7, 815.6, 580.0, weight=96.0)
    g.diag(815.6, 595.3, 755.5, 484.5, weight=96.0)
    g.diag(661.6, 431.4, 673.8, 444.9, weight=76.0)
    g.hbar(673.8, 820.1, 453.3, weight=76.0)
    g.diag(605.3, 461.6, 928.9, -37.1, weight=64.0)
    g.vbar(934.5, -37.1, 181.1, weight=64.0)
    g.hbar(655.4, 818.2, 346.6, weight=64.0)
    g.hbar(818.2, 827.4, 356.5, weight=64.0)
    g.hbar(648.1, 819.1, 266.6, weight=64.0)
    g.diag(647.0, 172.8, 658.8, 165.3, weight=64.0)
    g.hbar(658.8, 836.8, 173.2, weight=64.0)
    return g

def g_cjk_unified_ideograph_789f() -> Glyph:
    """碟 U+789F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni789F", advance=1000, unicode=0x789F, note="碟：自动生成")
    g.hbar(156.8, 183.8, 595.8, weight=96.0)
    g.hbar(156.8, 318.3, 621.4, weight=96.0)
    g.hbar(318.3, 377.3, 635.3, weight=96.0)
    g.diag(219.3, 584.9, 263.2, 549.8, weight=64.0)
    g.diag(263.2, 549.8, 60.0, 230.7, weight=64.0)
    g.vbar(189.3, 206.3, 404.8, weight=64.0)
    g.hbar(206.7, 351.8, 399.9, weight=96.0)
    g.vbar(338.9, 307.7, 415.7, weight=96.0)
    g.diag(326.0, 307.7, 303.5, 292.1, weight=96.0)
    g.diag(227.8, 229.8, 238.4, 248.7, weight=96.0)
    g.hbar(238.4, 362.2, 256.6, weight=96.0)
    g.hbar(358.5, 493.2, 609.1, weight=64.0)
    g.hbar(493.2, 859.5, 624.6, weight=64.0)
    g.diag(540.3, 756.1, 578.7, 726.9, weight=64.0)
    g.vbar(586.3, 503.0, 726.9, weight=64.0)
    g.vbar(683.6, 565.3, 808.8, weight=76.0)
    g.hbar(609.3, 695.3, 533.6, weight=64.0)
    g.diag(695.3, 545.0, 713.3, 565.4, weight=64.0)
    g.hbar(382.8, 469.2, 677.9, weight=64.0)
    g.vbar(480.1, 422.3, 677.4, weight=64.0)
    g.hbar(491.1, 794.3, 434.8, weight=64.0)
    g.hbar(375.5, 860.4, 302.2, weight=64.0)
    g.diag(576.7, 412.9, 619.7, 364.7, weight=96.0)
    g.vbar(612.6, 11.2, 364.7, weight=96.0)
    g.diag(574.8, 284.4, 352.4, 87.9, weight=64.0)
    g.diag(628.5, 290.2, 940.0, 119.5, weight=64.0)
    return g

def g_cjk_unified_ideograph_8537() -> Glyph:
    """蔷 U+8537 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8537", advance=1000, unicode=0x8537, note="蔷：自动生成")
    g.hbar(200.3, 771.9, 705.0, weight=96.0)
    g.hbar(315.7, 367.6, 747.2, weight=96.0)
    g.diag(367.6, 752.8, 418.2, 633.8, weight=96.0)
    g.diag(528.9, 779.9, 616.4, 822.3, weight=64.0)
    g.diag(616.4, 822.3, 538.9, 611.9, weight=64.0)
    g.hbar(302.1, 650.2, 561.2, weight=96.0)
    g.diag(431.0, 676.5, 487.6, 618.7, weight=64.0)
    g.vbar(485.3, 423.9, 618.7, weight=64.0)
    g.diag(482.9, 423.9, 470.0, 405.4, weight=64.0)
    g.diag(301.8, 533.4, 363.8, 455.2, weight=64.0)
    g.vbar(361.4, 413.6, 455.2, weight=64.0)
    g.diag(626.2, 564.4, 648.2, 522.7, weight=64.0)
    g.diag(648.2, 522.7, 531.7, 430.9, weight=64.0)
    g.hbar(144.0, 856.0, 372.6, weight=64.0)
    g.diag(226.4, 320.8, 327.8, 36.9, weight=64.0)
    g.hbar(287.6, 444.1, 303.1, weight=64.0)
    g.diag(444.1, 304.0, 621.0, 209.5, weight=64.0)
    g.diag(621.0, 209.5, 587.8, 12.8, weight=64.0)
    g.vbar(404.7, 119.1, 232.8, weight=64.0)
    g.hbar(413.7, 580.6, 232.5, weight=64.0)
    g.diag(580.6, 242.5, 535.6, 178.2, weight=64.0)
    g.diag(434.9, 133.9, 438.1, 140.3, weight=64.0)
    g.hbar(438.1, 560.9, 148.6, weight=64.0)
    g.diag(560.9, 157.0, 573.2, 166.6, weight=64.0)
    g.diag(344.4, 44.3, 355.0, 56.0, weight=64.0)
    g.hbar(355.0, 638.4, 67.6, weight=64.0)
    return g

def g_cjk_unified_ideograph_8962() -> Glyph:
    """襢 U+8962 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8962", advance=1000, unicode=0x8962, note="襢：自动生成")
    g.dot(316.4, 719.5, w=96.0, h=124.8, slant=-14.0)
    g.hbar(121.0, 170.4, 489.7, weight=64.0)
    g.hbar(170.4, 256.8, 466.4, weight=64.0)
    g.diag(256.8, 447.5, 86.2, 223.6, weight=64.0)
    g.diag(285.4, 377.6, 302.7, 325.6, weight=64.0)
    g.vbar(299.7, 0.0, 325.6, weight=64.0)
    g.diag(397.1, 435.8, 413.1, 411.4, weight=64.0)
    g.diag(413.1, 411.4, 378.4, 363.5, weight=64.0)
    g.hbar(369.9, 378.4, 363.5, weight=64.0)
    g.dot(377.4, 319.4, w=64.0, h=83.2, slant=-14.0)
    g.dot(614.1, 783.8, w=96.0, h=109.8, slant=-14.0)
    g.hbar(440.4, 879.0, 669.7, weight=76.0)
    g.diag(454.4, 573.0, 485.4, 542.0, weight=64.0)
    g.vbar(508.0, 346.6, 542.0, weight=64.0)
    g.diag(515.5, 548.5, 528.9, 564.9, weight=64.0)
    g.hbar(528.9, 820.9, 579.3, weight=64.0)
    g.vbar(788.9, 376.4, 593.7, weight=64.0)
    g.hbar(724.0, 757.0, 378.4, weight=64.0)
    g.diag(540.9, 515.7, 563.4, 497.8, weight=64.0)
    g.vbar(575.1, 412.3, 497.8, weight=64.0)
    g.hbar(586.9, 702.7, 510.7, weight=64.0)
    g.diag(702.7, 518.0, 658.3, 460.3, weight=64.0)
    g.dot(646.1, 432.1, w=64.0, h=83.2, slant=-14.0)
    g.hbar(547.4, 724.0, 377.6, weight=64.0)
    g.vbar(515.5, 92.1, 291.2, weight=64.0)
    g.hbar(528.6, 534.1, 280.7, weight=64.0)
    g.hbar(534.1, 757.4, 285.0, weight=64.0)
    g.vbar(744.5, 109.9, 290.3, weight=64.0)
    g.diag(554.0, 191.6, 559.8, 202.3, weight=64.0)
    g.hbar(559.8, 673.7, 209.8, weight=64.0)
    g.hbar(673.7, 689.3, 213.8, weight=64.0)
    g.hbar(562.5, 693.0, 125.4, weight=64.0)
    g.hbar(404.7, 913.8, 31.9, weight=64.0)
    return g

def g_cjk_unified_ideograph_8c0d() -> Glyph:
    """谍 U+8C0D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8C0D", advance=1000, unicode=0x8C0D, note="谍：自动生成")
    g.diag(224.3, 763.3, 348.4, 632.2, weight=96.0)
    g.hbar(85.3, 124.6, 437.5, weight=96.0)
    g.hbar(124.6, 285.4, 473.2, weight=96.0)
    g.vbar(272.9, 144.6, 509.4, weight=96.0)
    g.diag(260.5, 144.6, 387.9, 257.1, weight=96.0)
    g.hbar(340.0, 544.2, 639.3, weight=64.0)
    g.hbar(544.2, 839.1, 643.8, weight=64.0)
    g.hbar(468.0, 562.4, 735.6, weight=96.0)
    g.vbar(571.2, 500.3, 747.0, weight=96.0)
    g.diag(678.3, 820.0, 711.8, 780.6, weight=76.0)
    g.diag(711.8, 780.6, 686.8, 584.5, weight=76.0)
    g.diag(686.8, 584.5, 671.7, 566.5, weight=76.0)
    g.hbar(596.0, 701.2, 533.2, weight=64.0)
    g.vbar(702.0, 547.2, 562.2, weight=64.0)
    g.vbar(464.8, 423.7, 699.9, weight=64.0)
    g.hbar(507.7, 789.9, 433.6, weight=64.0)
    g.hbar(378.9, 841.9, 302.9, weight=64.0)
    g.vbar(592.7, 0.0, 412.4, weight=96.0)
    g.diag(579.0, 292.2, 361.4, 81.3, weight=64.0)
    g.hbar(621.9, 629.1, 300.5, weight=64.0)
    g.diag(621.9, 301.2, 784.5, 126.5, weight=64.0)
    g.hbar(784.5, 914.7, 113.8, weight=64.0)
    return g

def g_cjk_unified_ideograph_8f3f() -> Glyph:
    """輿 U+8F3F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8F3F", advance=1000, unicode=0x8F3F, note="輿：自动生成")
    g.diag(364.9, 638.5, 236.8, 523.5, weight=96.0)
    g.hbar(231.6, 236.8, 523.5, weight=96.0)
    g.diag(193.2, 524.2, 273.1, 208.8, weight=96.0)
    g.diag(273.1, 208.8, 292.3, 187.8, weight=96.0)
    g.dot(310.4, 420.1, w=84.0, h=106.3, slant=-14.0)
    g.dot(324.9, 334.6, w=64.0, h=83.2, slant=-14.0)
    g.hbar(353.8, 583.1, 651.9, weight=96.0)
    g.diag(583.1, 664.8, 631.9, 639.0, weight=96.0)
    g.vbar(394.3, 357.6, 539.3, weight=64.0)
    g.diag(395.9, 538.8, 403.4, 534.7, weight=64.0)
    g.hbar(403.4, 628.7, 548.3, weight=64.0)
    g.vbar(610.3, 399.3, 561.9, weight=64.0)
    g.vbar(598.3, 368.0, 399.3, weight=64.0)
    g.hbar(424.1, 574.8, 483.2, weight=64.0)
    g.hbar(427.9, 564.6, 391.1, weight=64.0)
    g.diag(354.2, 297.0, 397.8, 269.2, weight=76.0)
    g.hbar(397.8, 611.4, 293.5, weight=76.0)
    g.diag(463.0, 772.0, 490.4, 600.4, weight=64.0)
    g.vbar(489.1, 204.9, 600.4, weight=64.0)
    g.hbar(636.1, 800.1, 593.4, weight=96.0)
    g.diag(800.1, 596.3, 718.1, 253.3, weight=96.0)
    g.diag(718.1, 253.3, 693.5, 232.4, weight=96.0)
    g.hbar(643.8, 723.8, 464.4, weight=84.0)
    g.diag(723.8, 468.5, 740.9, 481.8, weight=84.0)
    g.hbar(614.6, 696.3, 356.5, weight=76.0)
    g.diag(696.3, 356.6, 718.1, 370.9, weight=76.0)
    g.hbar(87.5, 912.5, 173.6, weight=64.0)
    g.diag(348.8, 109.4, 369.6, 91.5, weight=64.0)
    g.diag(369.6, 91.5, 168.1, -66.3, weight=64.0)
    g.diag(593.5, 135.6, 776.9, -72.0, weight=96.0)
    return g

def g_cjk_unified_ideograph_8f40() -> Glyph:
    """轀 U+8F40 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8F40", advance=1000, unicode=0x8F40, note="轀：自动生成")
    g.hbar(152.7, 388.8, 685.4, weight=96.0)
    g.vbar(142.5, 335.2, 549.9, weight=64.0)
    g.hbar(156.6, 430.5, 556.6, weight=64.0)
    g.vbar(401.9, 361.4, 576.0, weight=64.0)
    g.hbar(212.9, 344.1, 472.7, weight=76.0)
    g.hbar(199.3, 338.2, 375.5, weight=76.0)
    g.hbar(63.3, 415.0, 255.5, weight=96.0)
    g.vbar(245.5, 0.0, 820.0, weight=76.0)
    g.vbar(523.8, 417.8, 679.1, weight=64.0)
    g.hbar(527.7, 629.2, 673.3, weight=64.0)
    g.hbar(629.2, 815.8, 686.5, weight=64.0)
    g.vbar(787.2, 455.3, 695.9, weight=64.0)
    g.diag(758.6, 455.3, 739.5, 465.4, weight=64.0)
    g.hbar(659.2, 673.4, 641.5, weight=96.0)
    g.diag(659.2, 638.8, 581.1, 481.3, weight=96.0)
    g.vbar(581.1, 481.3, 482.9, weight=96.0)
    g.vbar(665.0, 570.2, 576.1, weight=64.0)
    g.diag(665.3, 570.2, 721.0, 530.5, weight=64.0)
    g.hbar(581.1, 713.6, 459.0, weight=64.0)
    g.diag(713.6, 472.0, 721.0, 458.6, weight=64.0)
    g.diag(458.7, 323.5, 494.3, 290.8, weight=64.0)
    g.diag(494.3, 290.8, 524.4, 133.1, weight=64.0)
    g.diag(524.4, 133.1, 537.4, 123.4, weight=64.0)
    g.diag(521.9, 311.9, 536.7, 300.8, weight=64.0)
    g.hbar(536.7, 852.5, 332.4, weight=64.0)
    g.diag(852.5, 364.0, 766.1, 145.4, weight=64.0)
    g.diag(766.1, 145.4, 774.5, 152.5, weight=64.0)
    g.diag(587.9, 294.4, 598.2, 279.7, weight=64.0)
    g.diag(598.2, 279.7, 622.9, 133.1, weight=64.0)
    g.diag(691.9, 319.6, 721.3, 292.2, weight=64.0)
    g.diag(721.3, 292.2, 688.1, 148.0, weight=64.0)
    g.hbar(675.4, 688.1, 145.9, weight=64.0)
    g.hbar(399.4, 936.7, 103.0, weight=64.0)
    return g

def g_cjk_unified_ideograph_9119() -> Glyph:
    """鄙 U+9119 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9119", advance=1000, unicode=0x9119, note="鄙：自动生成")
    g.vbar(282.6, 562.4, 723.6, weight=64.0)
    g.diag(286.1, 723.1, 295.5, 718.0, weight=64.0)
    g.hbar(295.5, 510.1, 730.1, weight=64.0)
    g.vbar(492.4, 647.4, 742.2, weight=64.0)
    g.diag(474.7, 647.4, 454.1, 634.3, weight=64.0)
    g.hbar(318.7, 487.4, 601.2, weight=64.0)
    g.diag(163.0, 415.4, 289.4, 472.3, weight=76.0)
    g.hbar(289.4, 615.7, 515.3, weight=76.0)
    g.diag(330.9, 568.0, 359.0, 540.9, weight=96.0)
    g.diag(359.0, 540.9, 307.5, 409.3, weight=96.0)
    g.vbar(201.1, 379.0, 386.9, weight=64.0)
    g.vbar(225.5, 122.0, 379.0, weight=64.0)
    g.hbar(222.1, 556.4, 401.9, weight=64.0)
    g.vbar(529.2, 173.7, 421.3, weight=64.0)
    g.hbar(480.1, 501.9, 170.4, weight=64.0)
    g.vbar(302.7, 206.8, 330.1, weight=64.0)
    g.diag(310.3, 330.9, 315.5, 328.5, weight=64.0)
    g.hbar(315.5, 441.2, 333.6, weight=64.0)
    g.diag(441.2, 338.7, 399.0, 272.0, weight=64.0)
    g.diag(337.4, 226.3, 343.7, 235.7, weight=64.0)
    g.hbar(343.7, 426.3, 243.8, weight=64.0)
    g.diag(426.3, 252.0, 437.5, 265.4, weight=64.0)
    g.hbar(267.4, 473.9, 166.3, weight=64.0)
    g.hbar(685.6, 844.1, 634.1, weight=64.0)
    g.diag(844.1, 656.4, 773.4, 493.0, weight=64.0)
    g.diag(773.4, 493.0, 826.4, 325.2, weight=64.0)
    g.hbar(727.2, 826.4, 331.6, weight=64.0)
    g.hbar(647.6, 660.3, 622.8, weight=96.0)
    g.vbar(653.1, -52.0, 620.2, weight=96.0)
    return g

def g_cjk_unified_ideograph_91b4() -> Glyph:
    """醴 U+91B4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni91B4", advance=1000, unicode=0x91B4, note="醴：自动生成")
    g.hbar(113.8, 399.1, 625.7, weight=84.0)
    g.vbar(86.8, 57.1, 455.5, weight=64.0)
    g.diag(124.0, 441.3, 342.8, 321.3, weight=64.0)
    g.vbar(373.0, 21.5, 321.3, weight=64.0)
    g.diag(172.9, 579.9, 219.8, 545.6, weight=64.0)
    g.vbar(189.2, 278.2, 545.6, weight=64.0)
    g.vbar(285.0, 506.9, 601.3, weight=64.0)
    g.vbar(315.8, 314.8, 506.9, weight=64.0)
    g.hbar(336.5, 362.4, 314.3, weight=64.0)
    g.hbar(165.7, 320.6, 207.9, weight=84.0)
    g.hbar(126.0, 362.4, 101.0, weight=84.0)
    g.vbar(484.2, 378.1, 622.6, weight=64.0)
    g.hbar(480.6, 865.5, 629.3, weight=64.0)
    g.vbar(831.5, 423.7, 638.1, weight=64.0)
    g.diag(797.6, 423.7, 774.0, 437.2, weight=64.0)
    g.hbar(556.0, 756.7, 528.4, weight=64.0)
    g.vbar(578.5, 448.7, 706.2, weight=64.0)
    g.diag(609.2, 448.7, 589.6, 431.1, weight=64.0)
    g.diag(682.3, 785.7, 721.6, 748.9, weight=64.0)
    g.vbar(701.5, 444.3, 748.9, weight=64.0)
    g.diag(539.7, 398.5, 547.0, 405.8, weight=64.0)
    g.hbar(547.0, 748.5, 418.4, weight=64.0)
    g.diag(748.5, 431.1, 758.8, 421.9, weight=64.0)
    g.hbar(549.9, 751.6, 345.0, weight=64.0)
    g.diag(510.1, 259.9, 539.7, 230.4, weight=64.0)
    g.vbar(552.9, 113.2, 230.4, weight=64.0)
    g.diag(560.1, 253.8, 562.7, 251.9, weight=64.0)
    g.hbar(562.7, 784.5, 257.6, weight=64.0)
    g.diag(784.5, 263.2, 726.2, 197.8, weight=64.0)
    g.hbar(581.5, 766.9, 146.8, weight=64.0)
    g.dot(559.6, 46.4, w=84.0, h=87.4, slant=-14.0)
    g.diag(726.2, 126.4, 744.7, 89.0, weight=84.0)
    g.diag(744.7, 89.0, 690.5, 5.2, weight=84.0)
    g.hbar(415.4, 933.0, -26.9, weight=84.0)
    return g

def g_cjk_unified_ideograph_9998() -> Glyph:
    """馘 U+9998 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9998", advance=1000, unicode=0x9998, note="馘：自动生成")
    g.dot(220.4, 695.1, w=96.0, h=124.8, slant=-14.0)
    g.diag(374.9, 795.5, 399.9, 762.6, weight=96.0)
    g.diag(399.9, 762.6, 292.8, 626.2, weight=96.0)
    g.hbar(60.0, 470.9, 565.8, weight=64.0)
    g.diag(249.2, 522.3, 189.4, 421.3, weight=64.0)
    g.vbar(160.6, 58.8, 410.6, weight=64.0)
    g.hbar(179.7, 183.5, 402.2, weight=64.0)
    g.diag(183.5, 401.4, 333.9, 287.7, weight=64.0)
    g.diag(333.9, 287.7, 368.4, 14.8, weight=64.0)
    g.diag(182.9, 275.7, 318.6, 342.1, weight=64.0)
    g.hbar(180.8, 283.0, 199.7, weight=76.0)
    g.diag(283.0, 215.3, 311.0, 244.7, weight=76.0)
    g.diag(177.5, 81.6, 197.6, 92.9, weight=92.0)
    g.hbar(197.6, 327.3, 100.0, weight=92.0)
    g.diag(440.3, 546.2, 519.4, 489.3, weight=96.0)
    g.hbar(519.4, 724.3, 519.5, weight=96.0)
    g.diag(724.3, 549.7, 793.4, 634.5, weight=96.0)
    g.vbar(463.0, 233.7, 383.4, weight=64.0)
    g.hbar(469.5, 600.5, 387.5, weight=64.0)
    g.vbar(591.3, 314.6, 394.1, weight=64.0)
    g.diag(582.1, 314.6, 562.5, 299.5, weight=64.0)
    g.hbar(489.2, 596.6, 272.8, weight=64.0)
    g.diag(412.1, 156.1, 460.1, 129.1, weight=64.0)
    g.hbar(460.1, 593.8, 158.7, weight=64.0)
    g.vbar(598.0, 188.4, 240.4, weight=64.0)
    g.diag(586.3, 809.6, 674.3, 549.5, weight=84.0)
    g.diag(674.3, 549.5, 881.5, -62.4, weight=84.0)
    g.diag(881.5, -62.4, 940.0, 167.9, weight=84.0)
    g.diag(759.6, 506.8, 855.9, 384.9, weight=84.0)
    g.diag(855.9, 384.9, 628.7, 59.5, weight=84.0)
    g.hbar(506.2, 628.7, 78.6, weight=84.0)
    g.diag(659.4, 757.8, 832.2, 661.8, weight=64.0)
    return g

def g_cjk_unified_ideograph_9b5d() -> Glyph:
    """魝 U+9B5D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9B5D", advance=1000, unicode=0x9B5D, note="魝：自动生成")
    g.diag(311.1, 727.8, 319.1, 757.7, weight=96.0)
    g.diag(319.1, 757.7, 141.2, 558.1, weight=96.0)
    g.hbar(311.6, 469.4, 695.6, weight=64.0)
    g.diag(469.4, 700.7, 350.8, 563.0, weight=64.0)
    g.diag(136.7, 546.6, 218.6, 249.3, weight=96.0)
    g.hbar(180.5, 558.0, 530.2, weight=64.0)
    g.vbar(520.9, 297.5, 560.2, weight=64.0)
    g.diag(483.8, 297.5, 497.5, 251.0, weight=64.0)
    g.hbar(218.4, 481.4, 445.9, weight=64.0)
    g.diag(315.7, 520.3, 347.0, 489.0, weight=96.0)
    g.vbar(347.7, 367.4, 489.0, weight=96.0)
    g.diag(348.3, 367.4, 329.5, 338.5, weight=96.0)
    g.hbar(240.5, 449.2, 303.6, weight=92.0)
    g.diag(142.0, 247.0, 87.5, -0.0, weight=96.0)
    g.diag(234.8, 213.4, 299.4, 106.6, weight=96.0)
    g.hbar(299.4, 387.5, 115.1, weight=96.0)
    g.diag(315.6, 250.8, 426.0, 146.7, weight=96.0)
    g.diag(426.0, 146.7, 481.4, 188.4, weight=96.0)
    g.diag(501.3, 242.5, 604.1, 102.8, weight=96.0)
    g.diag(675.5, 615.6, 708.1, 570.5, weight=96.0)
    g.vbar(709.4, 284.6, 570.5, weight=96.0)
    g.diag(841.0, 796.2, 886.3, 545.4, weight=96.0)
    g.diag(886.3, 545.4, 815.2, 46.9, weight=96.0)
    g.diag(815.2, 46.9, 748.0, 81.4, weight=96.0)
    g.hbar(747.0, 748.0, 81.4, weight=96.0)
    return g

def g_cjk_unified_ideograph_9be1() -> Glyph:
    """鯡 U+9BE1 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9BE1", advance=1000, unicode=0x9BE1, note="鯡：自动生成")
    g.diag(240.3, 817.1, 270.3, 775.2, weight=64.0)
    g.diag(270.3, 775.2, 106.2, 544.1, weight=64.0)
    g.hbar(225.5, 355.3, 674.6, weight=64.0)
    g.diag(355.3, 685.3, 245.2, 540.1, weight=64.0)
    g.diag(111.5, 531.2, 165.6, 285.8, weight=92.0)
    g.hbar(157.8, 410.1, 509.2, weight=64.0)
    g.vbar(385.0, 309.2, 524.0, weight=64.0)
    g.hbar(327.7, 360.0, 310.7, weight=64.0)
    g.hbar(181.4, 350.2, 433.4, weight=64.0)
    g.diag(236.3, 500.8, 260.9, 477.3, weight=64.0)
    g.vbar(260.4, 372.2, 477.3, weight=64.0)
    g.diag(259.9, 372.2, 245.2, 349.6, weight=64.0)
    g.hbar(186.2, 328.6, 319.7, weight=64.0)
    g.diag(151.9, 209.8, 88.0, 86.4, weight=64.0)
    g.diag(88.0, 86.4, 93.9, 45.2, weight=64.0)
    g.diag(136.1, 211.5, 200.0, 143.4, weight=64.0)
    g.hbar(200.0, 250.1, 152.4, weight=64.0)
    g.hbar(202.1, 276.6, 200.5, weight=64.0)
    g.hbar(231.7, 276.6, 183.2, weight=64.0)
    g.vbar(352.5, 205.2, 282.3, weight=64.0)
    g.diag(362.0, 205.2, 402.7, 228.7, weight=64.0)
    g.vbar(551.1, 450.9, 690.4, weight=96.0)
    g.diag(555.5, 450.9, 433.7, 18.7, weight=96.0)
    g.hbar(442.0, 551.6, 495.9, weight=96.0)
    g.diag(551.6, 499.9, 567.3, 514.6, weight=96.0)
    g.hbar(443.7, 548.6, 400.3, weight=84.0)
    g.diag(548.6, 382.0, 567.3, 395.8, weight=84.0)
    g.hbar(381.2, 456.3, 244.1, weight=84.0)
    g.diag(456.3, 237.7, 628.2, 327.1, weight=84.0)
    g.diag(676.3, 820.0, 712.2, 538.6, weight=96.0)
    g.vbar(715.3, 0.0, 538.6, weight=96.0)
    g.dot(831.9, 573.0, w=96.0, h=124.8, slant=-14.0)
    g.hbar(751.9, 830.1, 431.9, weight=96.0)
    g.diag(830.1, 442.6, 877.6, 348.6, weight=96.0)
    g.hbar(751.9, 872.4, 299.6, weight=96.0)
    g.diag(872.4, 312.4, 861.7, 390.4, weight=96.0)
    return g

def g_cjk_unified_ideograph_9cdf() -> Glyph:
    """鳟 U+9CDF —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9CDF", advance=1000, unicode=0x9CDF, note="鳟：自动生成")
    g.diag(265.9, 777.4, 295.6, 740.6, weight=64.0)
    g.diag(295.6, 740.6, 141.9, 537.0, weight=64.0)
    g.hbar(257.2, 386.6, 643.7, weight=64.0)
    g.diag(386.6, 654.5, 296.0, 505.0, weight=64.0)
    g.vbar(155.4, 244.3, 464.3, weight=64.0)
    g.hbar(153.5, 422.9, 483.2, weight=64.0)
    g.vbar(400.7, 271.4, 500.2, weight=64.0)
    g.dot(282.9, 380.4, w=84.0, h=109.2, slant=-14.0)
    g.diag(259.1, 462.3, 269.1, 455.0, weight=76.0)
    g.diag(269.1, 455.0, 290.6, 317.1, weight=76.0)
    g.diag(290.6, 317.1, 269.8, 300.5, weight=76.0)
    g.diag(208.7, 258.8, 214.3, 266.3, weight=84.0)
    g.hbar(214.3, 347.3, 283.4, weight=84.0)
    g.hbar(89.5, 140.9, 112.9, weight=84.0)
    g.hbar(140.9, 403.6, 146.4, weight=84.0)
    g.dot(561.5, 745.9, w=84.0, h=95.3, slant=-14.0)
    g.diag(721.5, 820.0, 739.9, 794.8, weight=84.0)
    g.diag(739.9, 794.8, 659.4, 695.9, weight=84.0)
    g.hbar(474.3, 877.5, 650.4, weight=64.0)
    g.vbar(497.1, 316.0, 559.3, weight=64.0)
    g.hbar(524.7, 662.8, 556.2, weight=64.0)
    g.diag(662.8, 562.8, 793.2, 328.6, weight=64.0)
    g.diag(578.0, 629.1, 606.7, 599.0, weight=64.0)
    g.diag(606.7, 599.0, 555.7, 443.0, weight=64.0)
    g.diag(658.5, 642.6, 670.9, 631.9, weight=64.0)
    g.diag(670.9, 631.9, 690.2, 492.8, weight=64.0)
    g.hbar(690.2, 779.7, 484.4, weight=64.0)
    g.hbar(762.2, 779.7, 478.8, weight=64.0)
    g.hbar(586.7, 700.2, 416.8, weight=64.0)
    g.diag(526.7, 326.6, 538.1, 335.6, weight=64.0)
    g.hbar(538.1, 760.2, 343.7, weight=64.0)
    g.hbar(422.9, 910.5, 239.4, weight=84.0)
    g.vbar(676.6, 106.3, 332.5, weight=84.0)
    g.diag(678.3, 106.3, 599.3, 45.6, weight=84.0)
    g.dot(552.3, 140.5, w=84.0, h=99.4, slant=-14.0)
    return g

def g_cjk_unified_ideograph_9e2a() -> Glyph:
    """鸪 U+9E2A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9E2A", advance=1000, unicode=0x9E2A, note="鸪：自动生成")
    g.hbar(92.1, 532.8, 540.8, weight=96.0)
    g.diag(291.3, 769.9, 338.3, 728.2, weight=96.0)
    g.vbar(324.2, 392.3, 728.2, weight=96.0)
    g.diag(310.1, 392.3, 291.3, 369.3, weight=96.0)
    g.vbar(208.1, 137.3, 343.2, weight=64.0)
    g.hbar(203.4, 220.3, 340.2, weight=64.0)
    g.hbar(220.3, 424.3, 346.7, weight=64.0)
    g.vbar(407.0, 247.5, 356.2, weight=64.0)
    g.diag(389.7, 247.5, 358.8, 222.2, weight=64.0)
    g.diag(243.1, 161.3, 261.9, 179.1, weight=64.0)
    g.hbar(261.9, 407.4, 189.8, weight=64.0)
    g.vbar(413.5, 166.2, 200.5, weight=64.0)
    g.diag(673.2, 820.0, 697.5, 789.3, weight=96.0)
    g.diag(697.5, 789.3, 617.4, 644.1, weight=96.0)
    g.hbar(604.3, 617.4, 642.3, weight=96.0)
    g.diag(600.2, 628.0, 611.4, 618.1, weight=64.0)
    g.hbar(611.4, 831.9, 628.7, weight=64.0)
    g.diag(831.9, 639.4, 777.3, 427.4, weight=64.0)
    g.diag(777.3, 427.4, 692.2, 486.2, weight=64.0)
    g.diag(606.1, 568.6, 695.9, 496.0, weight=64.0)
    g.diag(575.7, 635.6, 625.6, 297.8, weight=64.0)
    g.diag(625.6, 297.8, 806.3, 196.5, weight=64.0)
    g.vbar(815.9, -7.5, 196.5, weight=64.0)
    g.diag(825.5, -7.5, 698.2, 58.4, weight=64.0)
    g.hbar(408.7, 555.2, 162.3, weight=64.0)
    g.hbar(555.2, 832.7, 172.4, weight=64.0)
    return g

def g_cjk_unified_ideograph_9f3e() -> Glyph:
    """鼾 U+9F3E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9F3E", advance=1000, unicode=0x9F3E, note="鼾：自动生成")
    g.hbar(337.7, 367.1, 819.1, weight=64.0)
    g.diag(337.7, 818.2, 276.6, 744.4, weight=64.0)
    g.diag(198.2, 731.4, 223.4, 701.5, weight=64.0)
    g.vbar(236.9, 531.7, 701.5, weight=64.0)
    g.diag(243.9, 709.9, 255.6, 726.0, weight=64.0)
    g.hbar(255.6, 462.0, 732.7, weight=64.0)
    g.vbar(436.0, 563.4, 739.5, weight=64.0)
    g.diag(410.1, 563.4, 391.3, 572.8, weight=64.0)
    g.diag(256.1, 653.0, 265.2, 662.2, weight=64.0)
    g.hbar(265.2, 366.1, 667.9, weight=64.0)
    g.dot(313.4, 606.8, w=64.0, h=83.2, slant=-14.0)
    g.diag(268.2, 542.0, 274.1, 551.9, weight=64.0)
    g.hbar(274.1, 368.4, 559.3, weight=64.0)
    g.diag(368.4, 566.6, 378.3, 559.7, weight=64.0)
    g.vbar(195.4, 316.2, 479.5, weight=64.0)
    g.diag(209.4, 478.6, 213.8, 475.1, weight=64.0)
    g.hbar(213.8, 472.3, 484.4, weight=64.0)
    g.vbar(451.4, 334.0, 493.7, weight=64.0)
    g.hbar(253.3, 396.0, 413.3, weight=64.0)
    g.diag(308.3, 467.4, 325.1, 448.7, weight=76.0)
    g.vbar(323.7, 378.7, 448.7, weight=76.0)
    g.diag(322.3, 378.7, 309.2, 359.2, weight=76.0)
    g.diag(239.3, 325.6, 245.6, 331.0, weight=64.0)
    g.hbar(245.6, 399.7, 345.6, weight=64.0)
    g.hbar(97.5, 486.5, 260.3, weight=64.0)
    g.diag(222.5, 221.1, 267.3, 183.8, weight=96.0)
    g.diag(267.3, 183.8, 132.0, 41.0, weight=96.0)
    g.diag(370.8, 252.8, 384.7, 242.2, weight=96.0)
    g.vbar(392.2, 22.4, 242.2, weight=96.0)
    g.hbar(542.4, 815.8, 636.7, weight=96.0)
    g.hbar(500.5, 902.5, 445.0, weight=64.0)
    g.diag(621.7, 597.0, 667.5, 563.5, weight=96.0)
    g.vbar(665.1, 0.0, 563.5, weight=96.0)
    return g

def g_cjk_unified_ideograph_5c0a() -> Glyph:
    """尊 U+5C0A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5C0A", advance=1000, unicode=0x5C0A, note="尊：自动生成")
    g.dot(393.9, 725.8, w=96.0, h=98.7, slant=-14.0)
    g.diag(601.6, 797.0, 615.6, 767.1, weight=96.0)
    g.diag(615.6, 767.1, 534.9, 695.4, weight=96.0)
    g.hbar(187.1, 798.0, 633.6, weight=92.0)
    g.vbar(303.2, 258.9, 525.0, weight=64.0)
    g.hbar(324.6, 454.4, 515.9, weight=64.0)
    g.hbar(454.4, 693.3, 528.2, weight=64.0)
    g.vbar(668.5, 299.1, 537.7, weight=64.0)
    g.hbar(618.6, 643.6, 296.9, weight=64.0)
    g.diag(391.4, 611.7, 441.0, 573.6, weight=64.0)
    g.diag(441.0, 573.6, 360.5, 400.4, weight=64.0)
    g.diag(505.0, 626.6, 533.4, 603.5, weight=64.0)
    g.diag(533.4, 603.5, 515.8, 457.8, weight=64.0)
    g.hbar(515.8, 605.6, 452.0, weight=64.0)
    g.hbar(401.3, 553.8, 371.0, weight=64.0)
    g.hbar(354.5, 611.6, 298.8, weight=64.0)
    g.hbar(113.4, 886.6, 183.7, weight=64.0)
    g.diag(538.9, 282.8, 600.1, 224.2, weight=96.0)
    g.diag(600.1, 224.2, 565.2, -60.7, weight=96.0)
    g.hbar(444.2, 565.2, -34.9, weight=96.0)
    g.diag(319.6, 141.3, 418.3, 50.6, weight=64.0)
    return g

def g_cjk_unified_ideograph_8ad6() -> Glyph:
    """論 U+8AD6 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8AD6", advance=1000, unicode=0x8AD6, note="論：自动生成")
    g.diag(267.3, 702.9, 348.8, 647.0, weight=96.0)
    g.vbar(352.0, 542.5, 647.0, weight=96.0)
    g.hbar(73.0, 473.6, 485.2, weight=84.0)
    g.diag(156.3, 417.7, 241.7, 364.6, weight=76.0)
    g.hbar(241.7, 318.4, 375.5, weight=76.0)
    g.hbar(318.4, 398.7, 372.9, weight=76.0)
    g.diag(187.1, 200.6, 243.8, 269.0, weight=76.0)
    g.hbar(243.8, 359.9, 271.4, weight=76.0)
    g.vbar(185.5, 5.5, 171.4, weight=64.0)
    g.hbar(183.8, 330.4, 173.8, weight=64.0)
    g.vbar(321.1, 99.3, 177.1, weight=64.0)
    g.diag(311.8, 99.3, 289.1, 82.2, weight=64.0)
    g.diag(217.0, 29.1, 231.2, 44.2, weight=96.0)
    g.hbar(231.2, 343.2, 58.3, weight=96.0)
    g.diag(597.9, 648.2, 591.4, 669.0, weight=96.0)
    g.diag(591.4, 669.0, 389.3, 299.7, weight=96.0)
    g.diag(615.1, 613.8, 608.8, 582.8, weight=96.0)
    g.diag(608.8, 582.8, 942.0, 381.7, weight=96.0)
    g.hbar(499.8, 540.9, 376.6, weight=96.0)
    g.hbar(540.9, 710.3, 404.0, weight=96.0)
    g.vbar(413.7, -8.8, 257.0, weight=64.0)
    g.hbar(427.4, 809.7, 269.3, weight=64.0)
    g.vbar(792.0, -6.1, 288.7, weight=64.0)
    g.diag(774.3, -6.1, 670.7, 54.6, weight=64.0)
    g.hbar(461.7, 666.5, 161.5, weight=96.0)
    g.diag(666.5, 173.1, 679.5, 197.2, weight=96.0)
    g.diag(504.2, 233.8, 521.6, 222.6, weight=64.0)
    g.diag(521.6, 222.6, 564.9, 93.4, weight=64.0)
    g.diag(607.5, 257.5, 636.9, 227.2, weight=64.0)
    g.vbar(645.8, 4.0, 227.2, weight=64.0)
    return g

def g_cjk_unified_ideograph_8f2a() -> Glyph:
    """輪 U+8F2A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8F2A", advance=1000, unicode=0x8F2A, note="輪：自动生成")
    g.vbar(258.0, 574.4, 626.0, weight=96.0)
    g.hbar(264.8, 359.7, 589.6, weight=96.0)
    g.vbar(363.7, 604.8, 653.4, weight=96.0)
    g.vbar(186.0, 275.8, 463.1, weight=64.0)
    g.hbar(184.0, 193.4, 462.2, weight=64.0)
    g.hbar(193.4, 456.6, 475.3, weight=64.0)
    g.vbar(419.0, 308.6, 490.0, weight=64.0)
    g.hbar(217.9, 337.6, 403.7, weight=64.0)
    g.diag(337.6, 408.4, 359.7, 432.3, weight=64.0)
    g.hbar(228.8, 370.1, 307.7, weight=64.0)
    g.hbar(73.0, 430.3, 212.8, weight=76.0)
    g.diag(263.8, 758.7, 297.5, 528.2, weight=84.0)
    g.vbar(296.8, -38.7, 528.2, weight=84.0)
    g.diag(616.5, 659.5, 608.4, 675.5, weight=96.0)
    g.diag(608.4, 675.5, 490.1, 374.2, weight=96.0)
    g.diag(490.1, 374.2, 461.0, 361.0, weight=96.0)
    g.diag(638.1, 627.8, 947.0, 397.3, weight=96.0)
    g.hbar(540.6, 591.1, 398.0, weight=64.0)
    g.hbar(591.1, 675.9, 399.6, weight=64.0)
    g.diag(675.9, 411.2, 720.4, 467.4, weight=64.0)
    g.vbar(456.2, 29.5, 279.6, weight=64.0)
    g.hbar(475.0, 839.2, 292.7, weight=64.0)
    g.diag(839.2, 307.9, 800.9, 25.5, weight=64.0)
    g.diag(800.9, 25.5, 704.5, 77.9, weight=64.0)
    g.hbar(509.4, 697.9, 185.2, weight=96.0)
    g.diag(697.9, 200.7, 711.9, 215.5, weight=96.0)
    g.diag(547.8, 262.7, 604.0, 127.6, weight=64.0)
    g.diag(642.8, 278.4, 669.5, 248.9, weight=64.0)
    g.vbar(676.4, 47.5, 248.9, weight=64.0)
    return g



def build() -> list[Glyph]:
    return [
        g_cjk_unified_ideograph_558b(),        # 喋 U+558B
        g_cjk_unified_ideograph_5af1(),        # 嫱 U+5AF1
        g_cjk_unified_ideograph_5b17(),        # 嬗 U+5B17
        g_cjk_unified_ideograph_5e0f(),        # 帏 U+5E0F
        g_cjk_unified_ideograph_64be(),        # 撾 U+64BE
        g_cjk_unified_ideograph_64fc(),        # 擼 U+64FC
        g_cjk_unified_ideograph_6b1e(),        # 欞 U+6B1E
        g_cjk_unified_ideograph_6bfd(),        # 毽 U+6BFD
        g_cjk_unified_ideograph_6c06(),        # 氆 U+6C06
        g_cjk_unified_ideograph_6c2a(),        # 氪 U+6C2A
        g_cjk_unified_ideograph_728d(),        # 犍 U+728D
        g_cjk_unified_ideograph_77d3(),        # 矓 U+77D3
        g_cjk_unified_ideograph_789f(),        # 碟 U+789F
        g_cjk_unified_ideograph_8537(),        # 蔷 U+8537
        g_cjk_unified_ideograph_8962(),        # 襢 U+8962
        g_cjk_unified_ideograph_8c0d(),        # 谍 U+8C0D
        g_cjk_unified_ideograph_8f3f(),        # 輿 U+8F3F
        g_cjk_unified_ideograph_8f40(),        # 轀 U+8F40
        g_cjk_unified_ideograph_9119(),        # 鄙 U+9119
        g_cjk_unified_ideograph_91b4(),        # 醴 U+91B4
        g_cjk_unified_ideograph_9998(),        # 馘 U+9998
        g_cjk_unified_ideograph_9b5d(),        # 魝 U+9B5D
        g_cjk_unified_ideograph_9be1(),        # 鯡 U+9BE1
        g_cjk_unified_ideograph_9cdf(),        # 鳟 U+9CDF
        g_cjk_unified_ideograph_9e2a(),        # 鸪 U+9E2A
        g_cjk_unified_ideograph_9f3e(),        # 鼾 U+9F3E
        g_cjk_unified_ideograph_5c0a(),        # 尊 U+5C0A
        g_cjk_unified_ideograph_8ad6(),        # 論 U+8AD6
        g_cjk_unified_ideograph_8f2a(),        # 輪 U+8F2A

    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-auto-legacy29.ufo"


if __name__ == "__main__":
    _target = target_ufo()
    _target.parent.mkdir(parents=True, exist_ok=True)
    write_ufo(_target, build())
    print("[recipe] 已写出 %s" % _target)
