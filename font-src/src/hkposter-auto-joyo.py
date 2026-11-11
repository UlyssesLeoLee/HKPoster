"""HK Poster Heavy —— 骨架中线自动生成批次 hkposter-auto-joyo。

本文件由 font-src/scripts/hk_autogen.py 生成，请勿手工编辑。
设计源 = hanzi-writer-data 的每笔骨架中线（medians）；
按本项目笔画权重档重新粗化 —— 只取骨架，不描任何字体的轮廓。

字面框 x 60..940、y 0..820，advance 1000。
权重档 96 / 92 / 84 / 76 / 64，按逐笔局部拥挤度选取。
"""

from __future__ import annotations

import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, write_ufo  # noqa: E402


def g_cjk_unified_ideograph_4e7e() -> Glyph:
    """乾 U+4E7E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni4E7E", advance=1000, unicode=0x4E7E, note="乾：自动生成")
    g.vbar(225.4, 531.4, 615.9, weight=96.0)
    g.hbar(229.8, 453.0, 639.4, weight=96.0)
    g.hbar(401.5, 453.0, 672.4, weight=96.0)
    g.diag(338.2, 789.1, 375.4, 745.7, weight=96.0)
    g.diag(375.4, 745.7, 323.5, 522.1, weight=96.0)
    g.vbar(231.8, 276.8, 492.2, weight=48.0)
    g.hbar(212.8, 471.9, 495.0, weight=48.0)
    g.vbar(446.8, 316.0, 510.5, weight=48.0)
    g.hbar(406.2, 421.6, 316.8, weight=48.0)
    g.diag(252.1, 377.5, 266.4, 394.2, weight=64.0)
    g.hbar(266.4, 416.3, 396.0, weight=64.0)
    g.diag(265.6, 292.5, 275.1, 302.9, weight=64.0)
    g.hbar(275.1, 398.6, 316.0, weight=64.0)
    g.hbar(88.0, 566.5, 175.7, weight=76.0)
    g.diag(309.7, 293.5, 403.4, 216.4, weight=48.0)
    g.diag(403.4, 216.4, 334.3, -52.0, weight=48.0)
    g.diag(650.3, 792.0, 704.0, 741.7, weight=96.0)
    g.diag(704.0, 741.7, 496.8, 453.6, weight=96.0)
    g.hbar(624.8, 860.3, 558.9, weight=96.0)
    g.diag(532.7, 411.0, 578.7, 369.6, weight=84.0)
    g.diag(578.7, 369.6, 682.8, 250.4, weight=84.0)
    g.diag(682.8, 250.4, 920.6, 68.7, weight=84.0)
    g.vbar(923.8, 68.7, 217.9, weight=84.0)
    return g
def g_cjk_unified_ideograph_4ff3() -> Glyph:
    """俳 U+4FF3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni4FF3", advance=1000, unicode=0x4FF3, note="俳：自动生成")
    g.diag(309.9, 762.8, 262.3, 606.4, weight=48.0)
    g.diag(262.3, 606.4, 57.7, 302.1, weight=48.0)
    g.vbar(224.8, -9.0, 457.0, weight=48.0)
    g.diag(384.4, 704.1, 491.9, 445.3, weight=96.0)
    g.vbar(499.6, -19.2, 445.3, weight=96.0)
    g.hbar(286.2, 466.1, 502.1, weight=96.0)
    g.diag(466.1, 483.7, 486.9, 504.5, weight=96.0)
    g.hbar(285.4, 488.9, 361.8, weight=96.0)
    g.hbar(273.5, 349.0, 181.2, weight=84.0)
    g.diag(349.0, 177.1, 478.4, 240.7, weight=84.0)
    g.diag(478.4, 240.7, 484.9, 254.3, weight=84.0)
    g.diag(636.3, 777.0, 673.7, 535.4, weight=96.0)
    g.vbar(674.4, -67.0, 535.4, weight=96.0)
    g.hbar(711.6, 881.4, 535.0, weight=96.0)
    g.diag(717.7, 367.2, 726.8, 379.4, weight=96.0)
    g.hbar(726.8, 822.4, 387.5, weight=96.0)
    g.diag(822.4, 395.7, 871.6, 288.5, weight=96.0)
    g.hbar(711.6, 932.3, 225.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_4ff8() -> Glyph:
    """俸 U+4FF8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni4FF8", advance=1000, unicode=0x4FF8, note="俸：自动生成")
    g.diag(303.8, 784.7, 260.1, 639.1, weight=48.0)
    g.diag(260.1, 639.1, 53.0, 329.1, weight=48.0)
    g.vbar(214.5, 39.1, 480.8, weight=48.0)
    g.diag(401.0, 556.7, 439.0, 620.1, weight=76.0)
    g.hbar(439.0, 669.6, 644.7, weight=76.0)
    g.diag(669.6, 669.3, 699.7, 592.2, weight=76.0)
    g.diag(465.5, 505.0, 448.3, 522.5, weight=76.0)
    g.hbar(448.3, 625.4, 542.6, weight=76.0)
    g.diag(625.4, 562.7, 701.7, 496.5, weight=76.0)
    g.hbar(328.7, 820.7, 438.2, weight=48.0)
    g.diag(522.0, 786.6, 489.2, 597.3, weight=48.0)
    g.diag(489.2, 597.3, 240.9, 176.6, weight=48.0)
    g.diag(612.5, 433.9, 947.0, 254.4, weight=48.0)
    g.hbar(408.7, 496.0, 276.8, weight=48.0)
    g.hbar(496.0, 699.8, 297.8, weight=48.0)
    g.diag(334.2, 176.5, 404.8, 141.2, weight=96.0)
    g.hbar(404.8, 728.4, 163.7, weight=96.0)
    g.diag(728.4, 186.2, 777.4, 247.1, weight=96.0)
    g.vbar(536.3, -56.6, 413.8, weight=64.0)
    return g
def g_cjk_unified_ideograph_4ffa() -> Glyph:
    """俺 U+4FFA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni4FFA", advance=1000, unicode=0x4FFA, note="俺：自动生成")
    g.diag(282.6, 748.5, 240.8, 609.2, weight=48.0)
    g.diag(240.8, 609.2, 53.0, 326.5, weight=48.0)
    g.vbar(217.6, -4.8, 481.3, weight=48.0)
    g.hbar(363.7, 757.5, 560.5, weight=48.0)
    g.diag(516.1, 774.9, 482.6, 627.0, weight=48.0)
    g.diag(482.6, 627.0, 248.8, 251.9, weight=48.0)
    g.diag(588.5, 540.4, 947.0, 340.1, weight=48.0)
    g.hbar(371.0, 397.9, 303.0, weight=48.0)
    g.vbar(417.5, 96.2, 298.1, weight=48.0)
    g.hbar(417.9, 703.6, 316.7, weight=48.0)
    g.vbar(683.1, 143.8, 338.3, weight=48.0)
    g.hbar(645.2, 662.7, 142.0, weight=48.0)
    g.hbar(433.1, 661.6, 220.1, weight=48.0)
    g.diag(448.7, 111.5, 457.2, 117.9, weight=76.0)
    g.hbar(457.2, 633.3, 134.9, weight=76.0)
    g.diag(482.0, 460.6, 571.2, 262.7, weight=48.0)
    g.diag(571.2, 262.7, 717.1, 77.0, weight=48.0)
    g.diag(717.1, 77.0, 808.3, 128.1, weight=48.0)
    return g
def g_cjk_unified_ideograph_5009() -> Glyph:
    """倉 U+5009 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5009", advance=1000, unicode=0x5009, note="倉：自动生成")
    g.diag(455.4, 738.7, 458.8, 733.1, weight=96.0)
    g.diag(458.8, 733.1, 96.7, 342.4, weight=96.0)
    g.diag(479.0, 708.4, 521.7, 639.1, weight=96.0)
    g.hbar(521.7, 903.3, 554.3, weight=96.0)
    g.diag(397.3, 601.0, 484.7, 540.2, weight=48.0)
    g.diag(484.7, 540.2, 501.8, 477.0, weight=48.0)
    g.hbar(372.8, 385.3, 437.0, weight=84.0)
    g.hbar(372.8, 618.4, 445.9, weight=84.0)
    g.vbar(587.8, 244.5, 452.9, weight=84.0)
    g.hbar(538.2, 557.2, 241.9, weight=84.0)
    g.hbar(375.7, 557.0, 324.2, weight=64.0)
    g.hbar(355.7, 529.6, 243.5, weight=76.0)
    g.diag(366.9, 440.5, 318.0, 299.6, weight=48.0)
    g.diag(318.0, 299.6, 130.2, -33.1, weight=48.0)
    g.vbar(386.4, -54.9, 122.6, weight=48.0)
    g.hbar(379.6, 640.4, 134.4, weight=48.0)
    g.diag(640.4, 148.6, 675.2, 111.7, weight=48.0)
    g.diag(675.2, 111.7, 612.0, 7.0, weight=48.0)
    g.hbar(423.6, 621.3, -25.7, weight=48.0)
    g.diag(621.3, -9.6, 644.1, 10.6, weight=48.0)
    return g
def g_cjk_unified_ideograph_502b() -> Glyph:
    """倫 U+502B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni502B", advance=1000, unicode=0x502B, note="倫：自动生成")
    g.diag(277.2, 696.4, 242.2, 560.8, weight=48.0)
    g.diag(242.2, 560.8, 53.0, 272.8, weight=48.0)
    g.vbar(223.7, -4.7, 436.9, weight=48.0)
    g.diag(513.7, 736.4, 480.1, 598.5, weight=48.0)
    g.diag(480.1, 598.5, 304.8, 311.0, weight=48.0)
    g.vbar(564.8, 597.2, 629.6, weight=96.0)
    g.diag(563.5, 597.2, 942.0, 386.3, weight=96.0)
    g.hbar(456.5, 639.6, 397.8, weight=84.0)
    g.diag(353.5, 246.1, 354.5, 245.3, weight=48.0)
    g.vbar(365.9, 14.3, 245.3, weight=48.0)
    g.hbar(393.5, 517.1, 249.1, weight=48.0)
    g.hbar(517.1, 699.0, 227.4, weight=48.0)
    g.vbar(722.6, -10.4, 198.9, weight=48.0)
    g.hbar(652.0, 746.2, 4.8, weight=48.0)
    g.hbar(435.5, 671.1, 145.0, weight=96.0)
    g.diag(466.0, 228.0, 495.6, 45.8, weight=48.0)
    g.diag(572.9, 248.0, 596.7, 229.9, weight=48.0)
    g.vbar(593.8, 30.6, 229.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_5049() -> Glyph:
    """偉 U+5049 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5049", advance=1000, unicode=0x5049, note="偉：自动生成")
    g.diag(319.2, 749.8, 286.4, 620.8, weight=48.0)
    g.diag(286.4, 620.8, 99.1, 342.3, weight=48.0)
    g.vbar(262.2, 23.9, 495.5, weight=48.0)
    g.diag(566.6, 788.0, 597.6, 751.6, weight=84.0)
    g.diag(597.6, 751.6, 563.9, 568.8, weight=84.0)
    g.diag(563.9, 568.8, 547.5, 553.3, weight=84.0)
    g.hbar(462.0, 741.5, 656.1, weight=48.0)
    g.diag(741.5, 669.7, 676.7, 570.4, weight=48.0)
    g.hbar(375.6, 885.9, 536.9, weight=48.0)
    g.dot(483.4, 392.9, w=84.0, h=109.2, slant=-14.0)
    g.hbar(485.6, 737.4, 457.2, weight=48.0)
    g.diag(737.4, 469.4, 680.3, 391.5, weight=48.0)
    g.hbar(520.2, 704.8, 358.8, weight=48.0)
    g.vbar(706.9, 375.4, 392.9, weight=48.0)
    g.hbar(451.6, 726.7, 253.5, weight=48.0)
    g.vbar(435.0, 121.5, 245.6, weight=84.0)
    g.hbar(414.2, 825.0, 132.7, weight=84.0)
    g.diag(573.0, 340.4, 611.2, 313.1, weight=84.0)
    g.vbar(609.8, -58.0, 313.1, weight=84.0)
    return g
def g_cjk_unified_ideograph_504f() -> Glyph:
    """偏 U+504F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni504F", advance=1000, unicode=0x504F, note="偏：自动生成")
    g.diag(317.8, 767.3, 275.7, 607.6, weight=48.0)
    g.diag(275.7, 607.6, 66.0, 260.4, weight=48.0)
    g.vbar(245.8, -52.0, 444.4, weight=48.0)
    g.hbar(579.4, 666.9, 759.7, weight=84.0)
    g.diag(666.9, 742.4, 724.3, 643.2, weight=84.0)
    g.hbar(508.7, 834.9, 590.2, weight=48.0)
    g.diag(834.9, 608.0, 758.3, 476.8, weight=48.0)
    g.hbar(497.9, 796.6, 438.5, weight=48.0)
    g.vbar(796.8, 461.8, 489.3, weight=48.0)
    g.diag(509.8, 584.3, 457.7, 444.9, weight=48.0)
    g.diag(457.7, 444.9, 274.6, 65.5, weight=48.0)
    g.vbar(470.7, -28.2, 274.4, weight=48.0)
    g.hbar(478.9, 632.9, 286.5, weight=48.0)
    g.hbar(632.9, 833.4, 251.9, weight=48.0)
    g.vbar(859.3, -33.6, 212.7, weight=48.0)
    g.hbar(746.8, 885.2, -11.2, weight=48.0)
    g.hbar(523.5, 864.3, 148.7, weight=96.0)
    g.diag(582.4, 266.6, 608.6, 239.8, weight=48.0)
    g.vbar(610.2, 29.1, 239.8, weight=48.0)
    g.diag(705.7, 291.7, 736.1, 260.4, weight=48.0)
    g.vbar(743.2, 10.1, 260.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_5075() -> Glyph:
    """偵 U+5075 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5075", advance=1000, unicode=0x5075, note="偵：自动生成")
    g.diag(348.2, 737.6, 314.0, 595.7, weight=48.0)
    g.diag(314.0, 595.7, 114.9, 280.9, weight=48.0)
    g.vbar(311.8, -43.3, 495.2, weight=48.0)
    g.diag(602.3, 792.0, 644.8, 755.4, weight=48.0)
    g.vbar(643.8, 570.6, 755.4, weight=48.0)
    g.diag(642.8, 570.6, 627.2, 546.9, weight=48.0)
    g.diag(674.5, 671.4, 688.7, 684.5, weight=96.0)
    g.hbar(688.7, 842.5, 692.3, weight=96.0)
    g.vbar(514.2, 143.0, 525.1, weight=48.0)
    g.hbar(518.9, 773.9, 537.1, weight=48.0)
    g.vbar(790.7, 451.8, 555.5, weight=48.0)
    g.vbar(810.0, 187.9, 451.8, weight=48.0)
    g.diag(812.5, 187.9, 783.0, 159.7, weight=48.0)
    g.hbar(545.9, 781.0, 407.6, weight=96.0)
    g.diag(550.9, 295.7, 559.9, 288.5, weight=96.0)
    g.hbar(559.9, 780.5, 297.4, weight=96.0)
    g.hbar(538.0, 758.0, 173.0, weight=84.0)
    g.diag(758.0, 190.6, 784.7, 172.8, weight=84.0)
    g.diag(606.8, 141.3, 495.1, -28.0, weight=84.0)
    g.hbar(347.1, 495.1, -40.0, weight=84.0)
    g.diag(778.4, 110.0, 880.1, -72.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_5076() -> Glyph:
    """偶 U+5076 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5076", advance=1000, unicode=0x5076, note="偶：自动生成")
    g.diag(291.8, 772.2, 249.3, 611.1, weight=48.0)
    g.diag(249.3, 611.1, 53.0, 290.2, weight=48.0)
    g.vbar(230.0, -47.2, 466.3, weight=48.0)
    g.diag(457.1, 651.9, 451.9, 641.3, weight=84.0)
    g.vbar(476.3, 380.2, 641.3, weight=84.0)
    g.hbar(473.2, 835.4, 663.3, weight=48.0)
    g.vbar(804.2, 435.8, 692.0, weight=48.0)
    g.hbar(743.0, 772.9, 436.2, weight=48.0)
    g.hbar(512.7, 672.5, 535.5, weight=92.0)
    g.hbar(668.7, 672.5, 552.6, weight=92.0)
    g.hbar(520.0, 733.1, 427.8, weight=92.0)
    g.vbar(384.6, -35.4, 278.8, weight=84.0)
    g.hbar(420.1, 592.9, 277.4, weight=84.0)
    g.hbar(592.9, 917.2, 299.6, weight=84.0)
    g.diag(917.2, 316.3, 872.6, -39.4, weight=84.0)
    g.diag(872.6, -39.4, 781.6, 76.5, weight=84.0)
    g.diag(597.1, 651.2, 631.8, 631.5, weight=96.0)
    g.vbar(628.3, 185.4, 631.5, weight=96.0)
    g.diag(624.7, 185.4, 608.9, 162.7, weight=96.0)
    g.hbar(434.3, 532.8, 116.8, weight=96.0)
    g.hbar(532.8, 727.8, 138.6, weight=96.0)
    g.vbar(728.8, 171.3, 178.8, weight=96.0)
    g.diag(726.9, 204.2, 803.8, 136.3, weight=64.0)
    g.diag(803.8, 136.3, 869.7, 102.0, weight=64.0)
    return g
def g_cjk_unified_ideograph_507d() -> Glyph:
    """偽 U+507D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni507D", advance=1000, unicode=0x507D, note="偽：自动生成")
    g.diag(300.3, 773.6, 256.9, 622.5, weight=48.0)
    g.diag(256.9, 622.5, 54.1, 317.4, weight=48.0)
    g.vbar(242.0, 329.3, 500.9, weight=48.0)
    g.vbar(244.0, -35.4, 329.3, weight=48.0)
    g.diag(782.7, 742.2, 697.7, 795.8, weight=96.0)
    g.diag(697.7, 795.8, 456.0, 665.3, weight=96.0)
    g.dot(458.9, 611.6, w=96.0, h=107.2, slant=0.0)
    g.diag(551.3, 687.1, 658.4, 597.2, weight=76.0)
    g.diag(778.2, 751.6, 809.8, 672.3, weight=96.0)
    g.diag(809.8, 672.3, 688.3, 566.8, weight=96.0)
    g.diag(470.7, 563.4, 441.0, 398.1, weight=48.0)
    g.diag(441.0, 398.1, 337.9, 92.2, weight=48.0)
    g.hbar(258.3, 337.9, 84.2, weight=48.0)
    g.hbar(493.0, 747.4, 500.6, weight=48.0)
    g.diag(747.4, 519.9, 653.8, 413.6, weight=48.0)
    g.hbar(473.0, 804.1, 377.9, weight=48.0)
    g.diag(804.1, 399.1, 701.1, 285.4, weight=48.0)
    g.hbar(433.7, 790.7, 197.9, weight=48.0)
    g.diag(790.7, 157.8, 863.3, -72.0, weight=48.0)
    g.diag(863.3, -72.0, 762.9, -5.5, weight=48.0)
    g.diag(387.3, 141.0, 443.1, 48.8, weight=48.0)
    g.vbar(442.6, 6.2, 48.8, weight=48.0)
    g.diag(508.0, 199.8, 546.5, 95.7, weight=84.0)
    g.hbar(546.5, 624.7, 94.3, weight=84.0)
    g.diag(601.6, 223.7, 656.3, 104.3, weight=56.0)
    g.diag(707.8, 248.4, 804.4, 103.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_508d() -> Glyph:
    """傍 U+508D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni508D", advance=1000, unicode=0x508D, note="傍：自动生成")
    g.diag(347.0, 764.7, 307.2, 623.1, weight=48.0)
    g.diag(307.2, 623.1, 97.4, 323.1, weight=48.0)
    g.vbar(281.3, -19.5, 497.3, weight=48.0)
    g.diag(608.7, 792.0, 663.3, 758.7, weight=96.0)
    g.diag(663.3, 758.7, 699.2, 673.8, weight=96.0)
    g.vbar(512.3, 579.6, 601.6, weight=96.0)
    g.hbar(514.2, 812.5, 629.3, weight=96.0)
    g.diag(812.5, 657.0, 777.2, 605.4, weight=96.0)
    g.diag(529.9, 585.9, 595.5, 442.6, weight=48.0)
    g.diag(720.9, 610.1, 748.0, 580.9, weight=96.0)
    g.diag(748.0, 580.9, 672.4, 458.5, weight=96.0)
    g.diag(434.4, 427.2, 401.4, 328.7, weight=76.0)
    g.diag(401.4, 328.7, 332.6, 288.7, weight=76.0)
    g.hbar(450.0, 913.1, 435.7, weight=48.0)
    g.diag(913.1, 465.0, 824.0, 357.5, weight=48.0)
    g.diag(586.4, 400.8, 677.1, 276.2, weight=48.0)
    g.hbar(458.1, 867.4, 244.8, weight=48.0)
    g.diag(641.9, 167.5, 728.1, 81.3, weight=48.0)
    g.diag(728.1, 81.3, 684.7, -76.6, weight=48.0)
    g.diag(684.7, -76.6, 589.5, -6.3, weight=48.0)
    g.diag(616.9, 226.0, 566.1, 133.9, weight=48.0)
    g.diag(566.1, 133.9, 313.3, -96.0, weight=48.0)
    g.diag(313.3, -96.0, 352.0, -69.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_5091() -> Glyph:
    """傑 U+5091 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5091", advance=1000, unicode=0x5091, note="傑：自动生成")
    g.diag(288.2, 779.0, 248.3, 630.4, weight=48.0)
    g.diag(248.3, 630.4, 61.7, 329.2, weight=48.0)
    g.vbar(214.4, -23.9, 479.1, weight=48.0)
    g.diag(464.2, 753.2, 492.3, 710.5, weight=48.0)
    g.diag(492.3, 710.5, 368.6, 524.2, weight=48.0)
    g.diag(368.6, 524.2, 371.5, 520.0, weight=48.0)
    g.diag(456.7, 613.6, 496.3, 528.1, weight=48.0)
    g.diag(496.3, 528.1, 321.5, 295.9, weight=48.0)
    g.dot(424.9, 499.0, w=92.0, h=91.9, slant=-14.0)
    g.hbar(658.2, 896.8, 620.1, weight=56.0)
    g.diag(663.1, 597.8, 674.1, 536.5, weight=92.0)
    g.vbar(668.9, 437.1, 536.5, weight=92.0)
    g.hbar(663.7, 933.3, 447.1, weight=92.0)
    g.diag(749.8, 772.6, 796.9, 729.9, weight=92.0)
    g.vbar(791.1, 300.4, 729.9, weight=92.0)
    g.diag(422.3, 160.7, 433.3, 204.3, weight=92.0)
    g.hbar(433.3, 829.9, 235.5, weight=92.0)
    g.diag(829.9, 266.7, 811.5, 319.6, weight=92.0)
    g.diag(578.0, 363.6, 635.5, 299.6, weight=76.0)
    g.vbar(618.9, -59.0, 299.6, weight=76.0)
    g.diag(602.4, -59.0, 437.0, 28.3, weight=76.0)
    g.diag(439.1, 167.3, 412.7, 46.9, weight=92.0)
    g.diag(412.7, 46.9, 453.4, -7.9, weight=92.0)
    g.diag(739.5, 219.4, 893.6, -6.8, weight=92.0)
    return g
def g_cjk_unified_ideograph_5098() -> Glyph:
    """傘 U+5098 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5098", advance=1000, unicode=0x5098, note="傘：自动生成")
    g.diag(475.8, 732.5, 380.2, 647.6, weight=64.0)
    g.diag(380.2, 647.6, 90.4, 401.2, weight=64.0)
    g.diag(489.3, 713.7, 909.6, 485.7, weight=96.0)
    g.diag(322.0, 538.0, 357.1, 484.4, weight=48.0)
    g.diag(357.1, 484.4, 238.1, 377.0, weight=48.0)
    g.diag(335.6, 432.7, 371.8, 412.3, weight=96.0)
    g.vbar(370.4, 376.8, 412.3, weight=96.0)
    g.diag(352.0, 401.5, 218.7, 176.6, weight=48.0)
    g.hbar(327.5, 381.8, 274.1, weight=48.0)
    g.vbar(390.8, 200.8, 262.7, weight=48.0)
    g.diag(576.2, 537.7, 600.1, 505.7, weight=48.0)
    g.diag(600.1, 505.7, 489.7, 390.4, weight=48.0)
    g.hbar(587.3, 648.6, 439.4, weight=96.0)
    g.vbar(648.0, 385.3, 427.6, weight=96.0)
    g.diag(641.5, 397.7, 493.7, 264.1, weight=64.0)
    g.hbar(580.7, 636.5, 295.8, weight=48.0)
    g.diag(636.5, 286.0, 664.6, 221.7, weight=48.0)
    g.hbar(189.7, 383.2, 191.7, weight=76.0)
    g.hbar(383.2, 799.1, 184.9, weight=76.0)
    g.diag(431.3, 543.3, 459.3, 418.2, weight=48.0)
    g.vbar(460.6, -67.0, 418.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_50b2() -> Glyph:
    """傲 U+50B2 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni50B2", advance=1000, unicode=0x50B2, note="傲：自动生成")
    g.diag(251.8, 723.9, 218.5, 593.7, weight=48.0)
    g.diag(218.5, 593.7, 53.0, 321.5, weight=48.0)
    g.vbar(196.1, 7.4, 459.7, weight=48.0)
    g.hbar(276.8, 390.4, 569.7, weight=76.0)
    g.hbar(390.4, 500.0, 572.7, weight=76.0)
    g.diag(500.0, 592.0, 549.9, 519.7, weight=76.0)
    g.diag(331.5, 373.9, 368.1, 448.5, weight=76.0)
    g.hbar(368.1, 502.9, 469.4, weight=76.0)
    g.hbar(502.9, 576.3, 480.2, weight=76.0)
    g.diag(412.7, 725.9, 453.1, 691.8, weight=84.0)
    g.vbar(437.8, 386.5, 691.8, weight=84.0)
    g.hbar(248.0, 563.1, 371.7, weight=76.0)
    g.diag(426.2, 289.2, 470.8, 183.9, weight=48.0)
    g.diag(470.8, 183.9, 421.8, 12.7, weight=48.0)
    g.diag(421.8, 12.7, 319.6, 61.7, weight=48.0)
    g.diag(397.5, 340.3, 423.6, 292.7, weight=48.0)
    g.diag(423.6, 292.7, 222.9, 118.2, weight=48.0)
    g.diag(673.6, 732.6, 713.9, 694.0, weight=96.0)
    g.diag(713.9, 694.0, 584.5, 427.4, weight=96.0)
    g.hbar(618.3, 869.4, 473.3, weight=96.0)
    g.diag(680.9, 437.5, 665.4, 311.1, weight=48.0)
    g.diag(665.4, 311.1, 484.7, 70.7, weight=48.0)
    g.diag(555.5, 350.2, 800.0, 45.1, weight=96.0)
    g.hbar(800.0, 947.0, 28.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_50c5() -> Glyph:
    """僅 U+50C5 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni50C5", advance=1000, unicode=0x50C5, note="僅：自动生成")
    g.diag(294.0, 723.2, 262.2, 584.6, weight=48.0)
    g.diag(262.2, 584.6, 78.9, 276.5, weight=48.0)
    g.vbar(247.9, -52.0, 447.5, weight=48.0)
    g.hbar(380.5, 895.4, 589.7, weight=76.0)
    g.diag(477.5, 715.5, 542.8, 468.6, weight=96.0)
    g.diag(680.2, 777.0, 714.2, 737.5, weight=96.0)
    g.diag(714.2, 737.5, 677.3, 544.5, weight=96.0)
    g.diag(677.3, 544.5, 660.0, 531.1, weight=96.0)
    g.diag(558.2, 475.4, 566.5, 490.6, weight=56.0)
    g.hbar(566.5, 706.1, 496.9, weight=56.0)
    g.diag(411.2, 395.6, 440.0, 372.6, weight=96.0)
    g.vbar(458.3, 255.4, 372.6, weight=96.0)
    g.diag(465.0, 392.8, 478.6, 385.6, weight=48.0)
    g.hbar(478.6, 752.4, 410.5, weight=48.0)
    g.diag(752.4, 435.5, 785.2, 403.9, weight=48.0)
    g.diag(785.2, 403.9, 761.9, 358.2, weight=48.0)
    g.hbar(735.9, 761.9, 354.3, weight=48.0)
    g.hbar(491.0, 782.0, 292.9, weight=48.0)
    g.hbar(441.0, 752.2, 206.4, weight=76.0)
    g.hbar(451.6, 739.8, 109.9, weight=76.0)
    g.diag(561.1, 465.8, 586.1, 452.5, weight=96.0)
    g.vbar(595.9, 60.2, 452.5, weight=96.0)
    g.diag(605.8, 60.2, 582.2, 33.5, weight=96.0)
    g.hbar(347.8, 901.1, 2.3, weight=76.0)
    return g
def g_cjk_unified_ideograph_50cf() -> Glyph:
    """像 U+50CF —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni50CF", advance=1000, unicode=0x50CF, note="像：自动生成")
    g.diag(279.2, 724.7, 237.4, 591.5, weight=48.0)
    g.diag(237.4, 591.5, 53.0, 322.8, weight=48.0)
    g.vbar(219.5, -17.5, 471.0, weight=48.0)
    g.vbar(531.9, 719.7, 743.2, weight=96.0)
    g.diag(532.4, 743.2, 413.2, 596.4, weight=96.0)
    g.hbar(519.8, 664.3, 689.8, weight=48.0)
    g.diag(664.3, 696.7, 579.3, 592.1, weight=48.0)
    g.vbar(414.0, 405.2, 558.0, weight=48.0)
    g.hbar(409.7, 759.6, 569.4, weight=48.0)
    g.diag(759.6, 583.8, 686.4, 439.1, weight=48.0)
    g.hbar(449.9, 681.7, 432.4, weight=48.0)
    g.diag(549.1, 556.0, 509.4, 451.2, weight=48.0)
    g.diag(509.4, 451.2, 337.8, 223.6, weight=48.0)
    g.diag(337.8, 223.6, 356.6, 261.3, weight=48.0)
    g.diag(503.3, 354.1, 550.6, 251.9, weight=48.0)
    g.vbar(553.2, 63.2, 251.9, weight=48.0)
    g.diag(555.9, 63.2, 471.7, -0.6, weight=48.0)
    g.vbar(530.2, 276.5, 316.0, weight=48.0)
    g.diag(530.3, 276.5, 343.7, 152.2, weight=48.0)
    g.diag(577.5, 252.8, 331.8, 20.2, weight=48.0)
    g.diag(700.1, 411.8, 725.7, 348.6, weight=48.0)
    g.diag(725.7, 348.6, 628.5, 267.3, weight=48.0)
    g.vbar(629.6, 251.1, 267.3, weight=48.0)
    g.hbar(635.4, 947.0, 166.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_50d5() -> Glyph:
    """僕 U+50D5 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni50D5", advance=1000, unicode=0x50D5, note="僕：自动生成")
    g.diag(277.7, 718.3, 241.5, 575.0, weight=48.0)
    g.diag(241.5, 575.0, 53.0, 265.0, weight=48.0)
    g.vbar(232.4, -52.1, 466.7, weight=48.0)
    g.diag(583.6, 752.0, 525.7, 660.9, weight=96.0)
    g.vbar(526.2, 526.7, 660.9, weight=96.0)
    g.diag(526.7, 526.7, 511.1, 514.0, weight=96.0)
    g.diag(618.1, 768.9, 654.3, 732.9, weight=76.0)
    g.vbar(646.9, 550.0, 732.9, weight=76.0)
    g.diag(639.5, 550.0, 622.0, 531.5, weight=76.0)
    g.diag(319.9, 624.9, 429.4, 572.4, weight=56.0)
    g.diag(429.4, 572.4, 456.3, 498.4, weight=56.0)
    g.diag(797.1, 717.3, 817.1, 677.8, weight=48.0)
    g.diag(817.1, 677.8, 662.3, 593.7, weight=48.0)
    g.hbar(277.7, 792.4, 493.7, weight=96.0)
    g.diag(792.4, 531.1, 776.4, 600.8, weight=96.0)
    g.dot(489.8, 409.2, w=96.0, h=81.8, slant=-14.0)
    g.diag(648.3, 487.8, 668.6, 463.2, weight=64.0)
    g.diag(668.6, 463.2, 602.5, 374.0, weight=64.0)
    g.hbar(407.0, 737.7, 347.7, weight=64.0)
    g.diag(448.5, 300.8, 474.2, 241.7, weight=64.0)
    g.hbar(474.2, 658.0, 259.7, weight=64.0)
    g.diag(658.0, 277.7, 708.4, 208.1, weight=64.0)
    g.hbar(342.8, 826.3, 157.6, weight=48.0)
    g.diag(542.2, 316.6, 631.4, 263.1, weight=96.0)
    g.diag(631.4, 263.1, 270.4, -53.0, weight=96.0)
    g.diag(582.8, 144.3, 942.0, -58.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_50e7() -> Glyph:
    """僧 U+50E7 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni50E7", advance=1000, unicode=0x50E7, note="僧：自动生成")
    g.diag(334.9, 731.7, 290.4, 584.4, weight=48.0)
    g.diag(290.4, 584.4, 94.1, 285.0, weight=48.0)
    g.vbar(259.2, -27.4, 429.8, weight=48.0)
    g.diag(512.1, 722.5, 597.7, 580.1, weight=56.0)
    g.diag(784.6, 787.0, 812.2, 748.1, weight=96.0)
    g.diag(812.2, 748.1, 688.1, 610.6, weight=96.0)
    g.diag(437.6, 542.2, 430.4, 530.6, weight=48.0)
    g.vbar(464.0, 316.7, 530.6, weight=48.0)
    g.hbar(445.6, 892.5, 557.3, weight=48.0)
    g.vbar(855.2, 356.5, 579.6, weight=48.0)
    g.hbar(791.0, 818.0, 358.3, weight=48.0)
    g.diag(625.8, 542.2, 646.3, 520.7, weight=64.0)
    g.vbar(646.3, 392.6, 520.7, weight=64.0)
    g.diag(646.3, 392.6, 630.2, 379.6, weight=64.0)
    g.diag(525.4, 518.9, 611.4, 394.9, weight=56.0)
    g.hbar(762.0, 784.6, 495.6, weight=48.0)
    g.diag(762.0, 497.1, 665.5, 430.5, weight=48.0)
    g.hbar(502.3, 786.2, 352.2, weight=48.0)
    g.vbar(522.3, -49.6, 226.9, weight=96.0)
    g.hbar(547.9, 746.4, 235.1, weight=48.0)
    g.diag(746.4, 263.9, 774.3, 158.1, weight=48.0)
    g.vbar(772.5, -34.4, 158.1, weight=48.0)
    g.hbar(713.5, 770.8, -25.3, weight=48.0)
    g.diag(559.2, 101.7, 575.4, 114.9, weight=96.0)
    g.hbar(575.4, 745.9, 117.0, weight=96.0)
    g.diag(547.9, -24.3, 560.4, -10.7, weight=96.0)
    g.hbar(560.4, 733.4, -6.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_5104() -> Glyph:
    """億 U+5104 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5104", advance=1000, unicode=0x5104, note="億：自动生成")
    g.diag(284.3, 749.0, 258.5, 613.0, weight=48.0)
    g.diag(258.5, 613.0, 80.5, 301.6, weight=48.0)
    g.vbar(259.1, 322.1, 494.3, weight=48.0)
    g.vbar(258.1, -52.0, 322.1, weight=48.0)
    g.diag(554.9, 787.0, 649.8, 717.1, weight=48.0)
    g.hbar(459.0, 737.7, 656.7, weight=96.0)
    g.dot(500.5, 569.3, w=96.0, h=75.4, slant=-14.0)
    g.diag(669.8, 637.2, 693.1, 610.7, weight=96.0)
    g.diag(693.1, 610.7, 635.8, 533.3, weight=96.0)
    g.hbar(362.2, 919.5, 505.3, weight=64.0)
    g.diag(419.1, 405.5, 502.0, 202.7, weight=48.0)
    g.hbar(464.0, 573.8, 407.3, weight=48.0)
    g.hbar(573.8, 761.7, 418.8, weight=48.0)
    g.vbar(733.6, 243.8, 427.5, weight=48.0)
    g.diag(705.5, 243.8, 708.8, 225.7, weight=48.0)
    g.diag(504.0, 309.6, 511.1, 319.1, weight=56.0)
    g.hbar(511.1, 645.8, 326.3, weight=56.0)
    g.hbar(518.0, 667.8, 246.1, weight=64.0)
    g.diag(398.1, 139.8, 353.2, -16.0, weight=84.0)
    g.diag(478.0, 111.8, 844.7, -65.7, weight=92.0)
    g.diag(844.7, -65.7, 758.7, 92.8, weight=92.0)
    g.dot(619.4, 124.8, w=92.0, h=97.8, slant=-14.0)
    g.dot(835.6, 162.7, w=96.0, h=124.8, slant=-14.0)
    return g
def g_cjk_unified_ideograph_5112() -> Glyph:
    """儒 U+5112 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5112", advance=1000, unicode=0x5112, note="儒：自动生成")
    g.diag(317.5, 748.2, 276.2, 604.1, weight=48.0)
    g.diag(276.2, 604.1, 84.3, 327.1, weight=48.0)
    g.vbar(259.4, -16.0, 483.2, weight=48.0)
    g.hbar(525.0, 794.1, 756.5, weight=96.0)
    g.diag(408.9, 621.9, 419.1, 590.5, weight=64.0)
    g.diag(419.1, 590.5, 379.1, 469.8, weight=64.0)
    g.hbar(451.0, 576.9, 594.3, weight=64.0)
    g.hbar(576.9, 898.6, 622.4, weight=64.0)
    g.diag(898.6, 644.2, 835.2, 541.8, weight=64.0)
    g.diag(606.1, 706.1, 634.9, 680.4, weight=96.0)
    g.vbar(632.3, 389.7, 680.4, weight=96.0)
    g.dot(527.0, 502.2, w=48.0, h=61.2, slant=-14.0)
    g.dot(514.7, 411.3, w=56.0, h=68.4, slant=-14.0)
    g.dot(742.3, 537.1, w=64.0, h=75.8, slant=-14.0)
    g.dot(738.2, 438.5, w=48.0, h=62.4, slant=-14.0)
    g.hbar(465.4, 797.2, 342.0, weight=76.0)
    g.diag(567.1, 295.2, 580.8, 272.0, weight=96.0)
    g.diag(580.8, 272.0, 541.4, 217.1, weight=96.0)
    g.diag(385.3, 188.4, 430.5, -42.8, weight=96.0)
    g.hbar(423.3, 588.1, 185.6, weight=96.0)
    g.hbar(588.1, 898.4, 204.1, weight=96.0)
    g.vbar(873.4, -44.5, 218.2, weight=96.0)
    g.hbar(767.4, 848.5, -26.7, weight=96.0)
    g.diag(531.2, 167.8, 553.8, 146.3, weight=96.0)
    g.vbar(555.8, -15.0, 146.3, weight=96.0)
    g.diag(662.6, 190.4, 690.4, 168.9, weight=96.0)
    g.vbar(687.3, -52.0, 168.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_517c() -> Glyph:
    """兼 U+517C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni517C", advance=1000, unicode=0x517C, note="兼：自动生成")
    g.diag(321.5, 749.7, 387.9, 704.8, weight=96.0)
    g.diag(387.9, 704.8, 407.4, 649.0, weight=96.0)
    g.diag(585.0, 802.0, 606.5, 772.1, weight=76.0)
    g.diag(606.5, 772.1, 526.8, 663.7, weight=76.0)
    g.hbar(305.5, 325.1, 590.0, weight=96.0)
    g.hbar(305.5, 639.4, 624.1, weight=96.0)
    g.diag(639.4, 653.8, 615.4, 723.6, weight=96.0)
    g.hbar(262.7, 634.9, 494.9, weight=48.0)
    g.diag(634.9, 521.3, 673.3, 484.9, weight=48.0)
    g.diag(673.3, 484.9, 616.5, 322.3, weight=48.0)
    g.hbar(110.4, 884.0, 375.9, weight=48.0)
    g.hbar(258.9, 650.4, 282.4, weight=48.0)
    g.vbar(650.3, 306.5, 332.6, weight=48.0)
    g.diag(361.7, 574.0, 397.4, 551.0, weight=96.0)
    g.vbar(384.2, 27.9, 551.0, weight=96.0)
    g.diag(371.1, 27.9, 476.8, -19.9, weight=96.0)
    g.diag(476.6, 595.5, 511.8, 414.8, weight=96.0)
    g.vbar(514.3, -52.0, 414.8, weight=96.0)
    g.diag(368.1, 245.4, 125.3, 11.5, weight=48.0)
    g.diag(541.9, 253.5, 889.6, 38.6, weight=48.0)
    return g
def g_cjk_unified_ideograph_51a5() -> Glyph:
    """冥 U+51A5 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni51A5", advance=1000, unicode=0x51A5, note="冥：自动生成")
    g.diag(266.1, 717.5, 263.9, 720.2, weight=96.0)
    g.diag(263.9, 720.2, 199.7, 592.8, weight=96.0)
    g.diag(199.7, 592.8, 254.3, 556.1, weight=96.0)
    g.hbar(275.1, 811.5, 712.8, weight=56.0)
    g.diag(811.5, 740.9, 660.4, 587.9, weight=56.0)
    g.vbar(323.8, 548.0, 567.4, weight=48.0)
    g.vbar(350.2, 333.1, 548.0, weight=48.0)
    g.hbar(333.9, 670.6, 569.0, weight=48.0)
    g.vbar(634.2, 359.8, 580.9, weight=48.0)
    g.hbar(571.2, 597.8, 362.0, weight=48.0)
    g.hbar(375.7, 489.8, 455.4, weight=64.0)
    g.diag(489.8, 470.8, 547.9, 406.1, weight=64.0)
    g.diag(393.1, 347.1, 407.2, 360.1, weight=64.0)
    g.hbar(407.2, 566.8, 371.5, weight=64.0)
    g.diag(409.7, 336.3, 517.8, 229.1, weight=48.0)
    g.hbar(97.8, 902.2, 194.0, weight=48.0)
    g.diag(396.8, 160.3, 170.5, -72.0, weight=92.0)
    g.diag(573.8, 175.6, 754.6, -67.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_51c4() -> Glyph:
    """凄 U+51C4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni51C4", advance=1000, unicode=0x51C4, note="凄：自动生成")
    g.diag(125.6, 627.2, 213.3, 581.4, weight=96.0)
    g.diag(213.3, 581.4, 278.7, 452.0, weight=96.0)
    g.diag(106.1, 49.2, 95.1, 94.9, weight=96.0)
    g.diag(95.1, 94.9, 266.3, 386.5, weight=96.0)
    g.diag(393.7, 548.1, 466.0, 629.6, weight=84.0)
    g.hbar(466.0, 704.5, 653.2, weight=84.0)
    g.hbar(379.0, 649.3, 538.7, weight=48.0)
    g.diag(649.3, 562.4, 685.2, 530.3, weight=48.0)
    g.diag(685.2, 530.3, 636.6, 382.7, weight=48.0)
    g.hbar(269.6, 865.3, 429.3, weight=48.0)
    g.hbar(357.5, 676.2, 346.9, weight=48.0)
    g.diag(676.2, 366.8, 663.0, 390.9, weight=48.0)
    g.diag(495.9, 787.0, 536.8, 751.9, weight=96.0)
    g.vbar(528.6, 384.5, 751.9, weight=96.0)
    g.diag(520.3, 384.5, 504.7, 364.0, weight=96.0)
    g.diag(481.3, 318.2, 506.6, 292.1, weight=96.0)
    g.diag(506.6, 292.1, 427.8, 119.8, weight=96.0)
    g.diag(427.8, 119.8, 736.6, -57.0, weight=96.0)
    g.diag(611.3, 246.4, 571.2, 165.3, weight=48.0)
    g.diag(571.2, 165.3, 320.5, -28.7, weight=48.0)
    g.hbar(238.6, 890.6, 208.6, weight=48.0)
    return g
def g_cjk_unified_ideograph_51c6() -> Glyph:
    """准 U+51C6 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni51C6", advance=1000, unicode=0x51C6, note="准：自动生成")
    g.dot(177.5, 579.5, w=96.0, h=124.8, slant=-14.0)
    g.diag(132.6, 19.8, 114.7, 66.0, weight=96.0)
    g.diag(114.7, 66.0, 243.6, 362.0, weight=96.0)
    g.diag(456.6, 792.0, 437.6, 669.7, weight=48.0)
    g.diag(437.6, 669.7, 277.0, 383.2, weight=48.0)
    g.vbar(394.6, -62.0, 489.2, weight=48.0)
    g.dot(628.2, 670.9, w=96.0, h=124.8, slant=-14.0)
    g.hbar(490.0, 796.8, 525.5, weight=96.0)
    g.hbar(514.2, 753.4, 363.5, weight=96.0)
    g.hbar(503.1, 769.6, 236.3, weight=96.0)
    g.diag(604.0, 481.1, 634.1, 460.4, weight=96.0)
    g.vbar(631.1, 122.6, 460.4, weight=96.0)
    g.diag(628.1, 122.6, 611.1, 100.5, weight=96.0)
    g.diag(439.5, 60.1, 446.7, 52.9, weight=96.0)
    g.hbar(446.7, 876.6, 65.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_51dd() -> Glyph:
    """凝 U+51DD —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni51DD", advance=1000, unicode=0x51DD, note="凝：自动生成")
    g.dot(112.7, 591.4, w=96.0, h=124.8, slant=-14.0)
    g.diag(68.6, 102.2, 166.1, 427.0, weight=56.0)
    g.hbar(423.4, 463.9, 665.5, weight=96.0)
    g.diag(423.4, 666.4, 302.9, 595.6, weight=96.0)
    g.diag(302.9, 595.6, 295.8, 585.7, weight=96.0)
    g.diag(248.1, 724.7, 252.9, 719.5, weight=96.0)
    g.diag(252.9, 719.5, 294.9, 477.6, weight=96.0)
    g.hbar(294.9, 450.7, 488.0, weight=96.0)
    g.diag(450.7, 498.4, 462.8, 586.8, weight=96.0)
    g.diag(246.0, 441.5, 272.3, 408.3, weight=48.0)
    g.diag(272.3, 408.3, 163.0, 252.7, weight=48.0)
    g.hbar(258.4, 444.2, 351.7, weight=96.0)
    g.hbar(138.1, 453.5, 200.8, weight=96.0)
    g.vbar(294.0, 210.4, 322.2, weight=48.0)
    g.diag(288.1, 210.4, 135.0, -18.1, weight=48.0)
    g.dot(389.7, 110.5, w=96.0, h=93.2, slant=-14.0)
    g.hbar(514.7, 611.4, 626.3, weight=48.0)
    g.hbar(611.4, 768.6, 644.5, weight=48.0)
    g.diag(768.6, 658.5, 669.8, 526.5, weight=48.0)
    g.hbar(661.0, 669.8, 527.1, weight=48.0)
    g.diag(592.5, 529.7, 678.6, 465.4, weight=48.0)
    g.hbar(484.6, 835.6, 403.3, weight=64.0)
    g.diag(835.6, 426.3, 760.6, 322.2, weight=64.0)
    g.diag(613.3, 374.1, 644.5, 352.3, weight=96.0)
    g.vbar(640.8, 110.5, 352.3, weight=96.0)
    g.diag(637.1, 110.5, 653.7, 83.5, weight=96.0)
    g.dot(735.7, 228.3, w=96.0, h=124.8, slant=-14.0)
    g.diag(506.4, 254.7, 541.4, 215.2, weight=96.0)
    g.diag(541.4, 215.2, 385.0, -34.7, weight=96.0)
    g.hbar(530.3, 937.0, 65.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_5256() -> Glyph:
    """剖 U+5256 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5256", advance=1000, unicode=0x5256, note="剖：自动生成")
    g.diag(318.5, 787.0, 414.8, 737.8, weight=84.0)
    g.diag(414.8, 737.8, 460.5, 633.0, weight=84.0)
    g.hbar(226.4, 519.5, 567.0, weight=96.0)
    g.vbar(513.8, 573.1, 613.9, weight=96.0)
    g.vbar(244.1, 470.5, 522.8, weight=96.0)
    g.diag(246.4, 470.5, 296.5, 366.0, weight=96.0)
    g.diag(452.8, 566.6, 488.3, 533.5, weight=96.0)
    g.diag(488.3, 533.5, 413.6, 374.2, weight=96.0)
    g.hbar(84.7, 667.1, 338.7, weight=96.0)
    g.vbar(253.4, 1.7, 204.5, weight=48.0)
    g.hbar(229.5, 441.7, 210.4, weight=48.0)
    g.diag(441.7, 231.4, 481.1, 194.7, weight=48.0)
    g.diag(481.1, 194.7, 422.7, 75.3, weight=48.0)
    g.hbar(278.2, 451.8, 40.3, weight=48.0)
    g.vbar(456.3, 62.7, 92.0, weight=48.0)
    g.diag(591.3, 600.1, 696.1, 541.5, weight=96.0)
    g.vbar(702.0, 189.6, 541.5, weight=96.0)
    g.diag(835.4, 782.5, 875.9, 481.3, weight=96.0)
    g.vbar(865.5, -42.1, 481.3, weight=96.0)
    g.diag(855.2, -42.1, 762.7, 0.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_525b() -> Glyph:
    """剛 U+525B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni525B", advance=1000, unicode=0x525B, note="剛：自动生成")
    g.vbar(122.8, 12.0, 670.8, weight=48.0)
    g.diag(173.9, 640.7, 471.4, 435.3, weight=48.0)
    g.diag(471.4, 435.3, 532.1, 16.3, weight=48.0)
    g.hbar(415.3, 532.1, 40.8, weight=48.0)
    g.diag(256.0, 624.8, 346.8, 507.3, weight=48.0)
    g.diag(391.8, 653.1, 418.3, 611.9, weight=48.0)
    g.diag(418.3, 611.9, 367.3, 483.5, weight=48.0)
    g.hbar(198.3, 411.6, 454.6, weight=96.0)
    g.vbar(409.5, 472.8, 500.2, weight=96.0)
    g.diag(326.3, 428.8, 365.3, 292.8, weight=84.0)
    g.diag(365.3, 292.8, 329.6, 266.0, weight=84.0)
    g.diag(195.7, 347.4, 256.0, 313.4, weight=96.0)
    g.diag(256.0, 313.4, 243.8, 214.1, weight=96.0)
    g.hbar(243.8, 414.3, 241.7, weight=96.0)
    g.hbar(379.2, 462.0, 362.1, weight=76.0)
    g.vbar(442.8, 240.1, 344.1, weight=76.0)
    g.hbar(594.2, 710.6, 575.0, weight=96.0)
    g.vbar(707.8, 235.6, 555.8, weight=96.0)
    g.diag(821.3, 762.0, 859.1, 472.8, weight=96.0)
    g.vbar(853.0, -49.3, 472.8, weight=96.0)
    g.diag(846.8, -49.3, 732.3, 13.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_525d() -> Glyph:
    """剝 U+525D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni525D", advance=1000, unicode=0x525D, note="剝：自动生成")
    g.diag(343.6, 777.0, 367.1, 735.3, weight=48.0)
    g.diag(367.1, 735.3, 280.6, 548.1, weight=48.0)
    g.hbar(280.6, 436.1, 554.1, weight=48.0)
    g.diag(436.1, 560.1, 454.7, 571.9, weight=48.0)
    g.diag(373.5, 670.2, 466.1, 602.6, weight=48.0)
    g.diag(466.1, 602.6, 417.3, 455.4, weight=48.0)
    g.hbar(96.8, 611.8, 420.7, weight=96.0)
    g.diag(351.1, 398.8, 404.8, 356.6, weight=92.0)
    g.vbar(387.7, -56.9, 356.6, weight=92.0)
    g.diag(370.5, -56.9, 263.5, 1.4, weight=92.0)
    g.dot(241.6, 283.4, w=96.0, h=112.6, slant=-14.0)
    g.hbar(108.6, 160.9, 54.3, weight=56.0)
    g.diag(160.9, 57.0, 316.9, 193.7, weight=56.0)
    g.hbar(556.2, 591.5, 312.8, weight=56.0)
    g.diag(556.2, 315.5, 471.8, 219.3, weight=56.0)
    g.hbar(461.1, 471.8, 220.4, weight=56.0)
    g.diag(419.5, 217.2, 574.4, 82.6, weight=96.0)
    g.diag(667.3, 530.2, 700.3, 491.1, weight=96.0)
    g.vbar(697.7, 154.2, 491.1, weight=96.0)
    g.diag(803.0, 735.3, 843.9, 525.9, weight=96.0)
    g.vbar(826.4, -27.2, 525.9, weight=96.0)
    g.diag(808.9, -27.2, 732.5, 16.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_5287() -> Glyph:
    """劇 U+5287 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5287", advance=1000, unicode=0x5287, note="劇：自动生成")
    g.diag(429.4, 744.9, 423.9, 761.2, weight=96.0)
    g.vbar(426.0, 660.4, 761.2, weight=96.0)
    g.diag(428.0, 660.4, 413.6, 641.9, weight=96.0)
    g.hbar(455.8, 551.1, 731.5, weight=76.0)
    g.diag(551.1, 746.1, 597.8, 679.4, weight=76.0)
    g.hbar(254.9, 650.3, 619.9, weight=48.0)
    g.diag(650.3, 645.7, 574.5, 543.4, weight=48.0)
    g.diag(246.6, 607.5, 213.6, 428.1, weight=64.0)
    g.diag(213.6, 428.1, 73.4, -37.5, weight=64.0)
    g.hbar(261.1, 545.8, 516.8, weight=48.0)
    g.diag(397.6, 592.0, 411.0, 537.5, weight=48.0)
    g.diag(411.0, 537.5, 435.3, 436.6, weight=48.0)
    g.hbar(435.3, 562.3, 441.1, weight=48.0)
    g.vbar(563.8, 445.6, 527.7, weight=48.0)
    g.hbar(247.9, 475.1, 351.0, weight=48.0)
    g.diag(475.1, 360.6, 510.1, 412.2, weight=48.0)
    g.diag(421.6, 332.4, 277.2, 206.1, weight=48.0)
    g.diag(277.2, 206.1, 279.0, 210.2, weight=48.0)
    g.diag(399.5, 273.2, 441.7, 190.5, weight=48.0)
    g.vbar(440.6, 43.4, 190.5, weight=48.0)
    g.hbar(341.4, 439.5, 29.7, weight=48.0)
    g.diag(410.6, 257.5, 415.4, 222.3, weight=48.0)
    g.diag(415.4, 222.3, 262.5, 108.5, weight=48.0)
    g.diag(462.3, 202.3, 455.1, 142.7, weight=48.0)
    g.diag(455.1, 142.7, 256.4, -7.7, weight=48.0)
    g.hbar(577.1, 681.7, 297.0, weight=84.0)
    g.diag(577.1, 303.8, 496.9, 225.7, weight=84.0)
    g.diag(524.6, 196.9, 713.7, 56.8, weight=96.0)
    g.diag(636.2, 562.3, 723.6, 485.7, weight=96.0)
    g.vbar(717.5, 252.7, 485.7, weight=96.0)
    g.diag(711.4, 252.7, 645.1, 163.3, weight=96.0)
    g.diag(828.9, 759.1, 869.1, 489.0, weight=96.0)
    g.vbar(860.8, -17.3, 489.0, weight=96.0)
    g.diag(852.6, -17.3, 672.7, 84.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_52d8() -> Glyph:
    """勘 U+52D8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni52D8", advance=1000, unicode=0x52D8, note="勘：自动生成")
    g.hbar(250.8, 289.0, 617.7, weight=92.0)
    g.hbar(289.0, 536.9, 637.4, weight=92.0)
    g.hbar(511.0, 536.9, 657.5, weight=92.0)
    g.diag(256.8, 647.3, 282.8, 676.8, weight=96.0)
    g.vbar(288.0, 346.1, 676.8, weight=96.0)
    g.diag(293.2, 346.1, 276.7, 330.7, weight=96.0)
    g.diag(454.6, 679.9, 477.9, 738.9, weight=96.0)
    g.vbar(469.6, 379.5, 738.9, weight=96.0)
    g.diag(461.2, 379.5, 444.6, 355.1, weight=96.0)
    g.dot(374.5, 506.9, w=76.0, h=98.8, slant=-14.0)
    g.diag(315.7, 397.1, 327.6, 412.9, weight=64.0)
    g.hbar(327.6, 437.2, 413.2, weight=64.0)
    g.hbar(87.2, 583.3, 312.6, weight=48.0)
    g.hbar(352.3, 405.6, 234.9, weight=64.0)
    g.diag(352.3, 226.9, 244.0, 140.7, weight=64.0)
    g.hbar(391.6, 484.7, 220.1, weight=76.0)
    g.vbar(483.0, 119.7, 201.8, weight=76.0)
    g.diag(180.1, 270.3, 221.1, 237.7, weight=48.0)
    g.diag(221.1, 237.7, 297.5, 108.8, weight=48.0)
    g.hbar(297.5, 545.9, 81.0, weight=48.0)
    g.diag(570.6, 427.4, 798.4, 287.7, weight=48.0)
    g.vbar(796.3, -11.8, 287.7, weight=48.0)
    g.diag(794.2, -11.8, 697.6, 51.4, weight=48.0)
    g.diag(703.4, 679.3, 669.8, 432.4, weight=48.0)
    g.diag(669.8, 432.4, 479.8, -57.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_533f() -> Glyph:
    """匿 U+533F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni533F", advance=1000, unicode=0x533F, note="匿：自动生成")
    g.diag(234.3, 716.6, 261.3, 698.3, weight=96.0)
    g.hbar(261.3, 790.0, 729.6, weight=96.0)
    g.hbar(307.9, 780.3, 563.1, weight=96.0)
    g.diag(400.8, 632.3, 437.6, 609.6, weight=96.0)
    g.diag(437.6, 609.6, 471.1, 479.9, weight=96.0)
    g.diag(619.2, 689.6, 646.5, 654.3, weight=96.0)
    g.diag(646.5, 654.3, 587.8, 487.4, weight=96.0)
    g.hbar(273.3, 823.5, 369.6, weight=96.0)
    g.hbar(520.6, 529.5, 441.4, weight=96.0)
    g.diag(520.6, 439.8, 256.0, 113.4, weight=96.0)
    g.diag(430.0, 250.7, 455.9, 56.1, weight=64.0)
    g.diag(447.3, 257.2, 469.0, 244.8, weight=48.0)
    g.hbar(469.0, 681.3, 263.7, weight=48.0)
    g.diag(681.3, 282.6, 716.5, 247.4, weight=48.0)
    g.diag(716.5, 247.4, 688.4, 173.9, weight=48.0)
    g.diag(688.4, 173.9, 663.5, 157.7, weight=48.0)
    g.diag(476.5, 106.9, 485.5, 100.4, weight=48.0)
    g.hbar(485.5, 716.5, 110.1, weight=48.0)
    g.diag(158.7, 725.2, 269.3, -41.6, weight=96.0)
    g.hbar(269.3, 861.3, -36.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_54fa() -> Glyph:
    """哺 U+54FA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni54FA", advance=1000, unicode=0x54FA, note="哺：自动生成")
    g.diag(116.7, 546.2, 104.8, 529.6, weight=48.0)
    g.diag(104.8, 529.6, 158.1, 253.5, weight=48.0)
    g.hbar(118.4, 269.8, 553.2, weight=48.0)
    g.diag(269.8, 570.5, 310.6, 541.3, weight=48.0)
    g.diag(310.6, 541.3, 264.7, 383.6, weight=48.0)
    g.diag(179.2, 330.6, 193.0, 349.0, weight=96.0)
    g.hbar(193.0, 313.2, 360.1, weight=96.0)
    g.vbar(313.0, 371.1, 386.9, weight=96.0)
    g.hbar(343.9, 940.0, 581.0, weight=96.0)
    g.vbar(454.5, 322.3, 421.5, weight=48.0)
    g.vbar(441.3, -45.1, 322.3, weight=48.0)
    g.hbar(466.1, 786.2, 440.3, weight=48.0)
    g.diag(786.2, 466.8, 825.1, 277.5, weight=48.0)
    g.vbar(822.5, -62.4, 277.5, weight=48.0)
    g.hbar(704.7, 820.0, -43.7, weight=48.0)
    g.hbar(501.5, 803.4, 300.0, weight=96.0)
    g.hbar(495.1, 805.7, 174.6, weight=96.0)
    g.hbar(579.1, 604.4, 793.8, weight=48.0)
    g.diag(604.4, 790.7, 626.9, 611.6, weight=48.0)
    g.vbar(626.2, -17.7, 611.6, weight=48.0)
    g.hbar(676.2, 809.2, 749.5, weight=96.0)
    g.diag(809.2, 733.7, 828.7, 663.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_5504() -> Glyph:
    """唄 U+5504 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5504", advance=1000, unicode=0x5504, note="唄：自动生成")
    g.diag(152.8, 588.5, 139.2, 566.7, weight=48.0)
    g.vbar(171.5, 352.0, 566.7, weight=48.0)
    g.hbar(154.6, 375.3, 593.1, weight=48.0)
    g.diag(375.3, 610.3, 299.5, 421.4, weight=48.0)
    g.diag(210.9, 369.9, 221.3, 384.1, weight=92.0)
    g.hbar(221.3, 349.2, 403.7, weight=92.0)
    g.hbar(441.9, 526.6, 690.9, weight=92.0)
    g.vbar(481.6, 214.9, 679.5, weight=92.0)
    g.hbar(534.7, 787.0, 635.0, weight=48.0)
    g.diag(787.0, 591.8, 835.6, 201.2, weight=48.0)
    g.diag(553.5, 538.5, 569.1, 557.5, weight=92.0)
    g.hbar(569.1, 807.8, 560.7, weight=92.0)
    g.diag(554.6, 406.6, 569.1, 424.4, weight=92.0)
    g.hbar(569.1, 808.8, 426.1, weight=92.0)
    g.hbar(545.9, 803.9, 246.7, weight=92.0)
    g.diag(544.0, 185.1, 565.0, 106.1, weight=92.0)
    g.diag(565.0, 106.1, 357.9, -65.8, weight=92.0)
    g.diag(803.5, 183.3, 930.8, -69.0, weight=92.0)
    return g
def g_cjk_unified_ideograph_5507() -> Glyph:
    """唇 U+5507 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5507", advance=1000, unicode=0x5507, note="唇：自动生成")
    g.diag(314.3, 714.9, 331.6, 704.5, weight=96.0)
    g.hbar(331.6, 597.3, 729.1, weight=96.0)
    g.diag(597.3, 753.8, 614.9, 658.6, weight=96.0)
    g.diag(279.3, 727.7, 72.9, 9.3, weight=96.0)
    g.hbar(309.7, 559.4, 611.5, weight=92.0)
    g.diag(559.4, 626.9, 612.3, 555.3, weight=92.0)
    g.hbar(280.4, 735.1, 487.8, weight=48.0)
    g.diag(336.4, 449.9, 359.1, 431.9, weight=48.0)
    g.vbar(366.1, 275.2, 431.9, weight=48.0)
    g.diag(373.1, 275.2, 467.6, 330.1, weight=48.0)
    g.diag(467.6, 330.1, 508.6, 372.7, weight=48.0)
    g.hbar(674.7, 703.1, 429.2, weight=48.0)
    g.diag(674.7, 433.4, 573.7, 371.4, weight=48.0)
    g.diag(420.6, 467.1, 902.1, 231.7, weight=48.0)
    g.vbar(353.9, -28.8, 171.5, weight=96.0)
    g.hbar(347.8, 616.5, 174.6, weight=48.0)
    g.diag(616.5, 193.8, 658.4, 153.1, weight=48.0)
    g.diag(658.4, 153.1, 595.6, 42.4, weight=48.0)
    g.hbar(376.3, 634.0, 18.1, weight=48.0)
    g.vbar(633.0, 23.2, 54.7, weight=48.0)
    return g
def g_cjk_unified_ideograph_5510() -> Glyph:
    """唐 U+5510 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5510", advance=1000, unicode=0x5510, note="唐：自动生成")
    g.hbar(452.7, 532.2, 774.5, weight=64.0)
    g.diag(532.2, 757.1, 577.3, 664.4, weight=64.0)
    g.hbar(330.7, 758.1, 644.0, weight=96.0)
    g.diag(296.9, 634.2, 253.8, 457.7, weight=96.0)
    g.diag(253.8, 457.7, 83.3, -9.8, weight=96.0)
    g.hbar(379.0, 739.7, 482.4, weight=48.0)
    g.diag(739.7, 501.5, 655.7, 300.3, weight=48.0)
    g.hbar(285.8, 896.7, 375.2, weight=48.0)
    g.hbar(380.9, 698.5, 264.9, weight=48.0)
    g.vbar(695.0, 284.6, 309.6, weight=48.0)
    g.vbar(511.1, 181.4, 588.1, weight=96.0)
    g.diag(360.0, 136.6, 418.7, -67.0, weight=96.0)
    g.hbar(385.8, 676.1, 145.2, weight=48.0)
    g.diag(676.1, 163.0, 717.0, 126.6, weight=48.0)
    g.diag(717.0, 126.6, 658.3, 18.7, weight=48.0)
    g.diag(430.6, -33.7, 450.4, -18.2, weight=48.0)
    g.hbar(450.4, 692.9, -8.0, weight=48.0)
    g.vbar(691.6, 2.2, 27.3, weight=48.0)
    return g
def g_cjk_unified_ideograph_552f() -> Glyph:
    """唯 U+552F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni552F", advance=1000, unicode=0x552F, note="唯：自动生成")
    g.vbar(154.8, 366.3, 563.5, weight=48.0)
    g.hbar(140.2, 315.6, 567.2, weight=48.0)
    g.vbar(289.7, 429.1, 585.1, weight=48.0)
    g.diag(179.9, 384.8, 196.6, 401.5, weight=96.0)
    g.hbar(196.6, 305.8, 412.1, weight=96.0)
    g.diag(499.9, 787.7, 463.1, 621.6, weight=48.0)
    g.diag(463.1, 621.6, 285.9, 276.9, weight=48.0)
    g.vbar(446.4, -52.7, 470.3, weight=48.0)
    g.hbar(570.5, 703.2, 718.7, weight=76.0)
    g.diag(703.2, 696.1, 744.3, 599.2, weight=76.0)
    g.hbar(508.6, 854.5, 570.6, weight=96.0)
    g.hbar(506.5, 789.1, 416.8, weight=96.0)
    g.vbar(794.8, 347.8, 435.4, weight=96.0)
    g.hbar(504.9, 795.7, 292.2, weight=96.0)
    g.diag(795.7, 309.6, 813.5, 391.8, weight=96.0)
    g.diag(651.2, 517.8, 684.9, 489.9, weight=96.0)
    g.vbar(684.0, 196.9, 489.9, weight=96.0)
    g.diag(683.0, 196.9, 666.6, 174.8, weight=96.0)
    g.hbar(493.1, 922.0, 146.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_5531() -> Glyph:
    """唱 U+5531 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5531", advance=1000, unicode=0x5531, note="唱：自动生成")
    g.diag(141.0, 541.6, 137.2, 533.7, weight=96.0)
    g.vbar(167.0, 300.8, 533.7, weight=96.0)
    g.hbar(162.1, 360.9, 547.1, weight=48.0)
    g.diag(360.9, 573.5, 327.7, 418.4, weight=48.0)
    g.diag(327.7, 418.4, 300.7, 388.7, weight=48.0)
    g.hbar(208.4, 372.7, 351.1, weight=96.0)
    g.vbar(493.0, 713.8, 729.3, weight=48.0)
    g.vbar(521.6, 447.1, 713.8, weight=48.0)
    g.hbar(505.3, 809.0, 738.5, weight=48.0)
    g.vbar(813.0, 656.4, 756.9, weight=48.0)
    g.diag(817.0, 656.4, 782.1, 476.5, weight=48.0)
    g.hbar(753.7, 782.1, 479.6, weight=48.0)
    g.hbar(543.9, 776.5, 598.7, weight=96.0)
    g.diag(567.3, 457.8, 581.3, 469.8, weight=96.0)
    g.hbar(581.3, 747.3, 485.6, weight=96.0)
    g.diag(384.0, 360.5, 442.6, 255.1, weight=48.0)
    g.diag(442.6, 255.1, 505.3, 10.4, weight=48.0)
    g.hbar(460.5, 786.4, 272.9, weight=48.0)
    g.diag(786.4, 217.1, 842.0, -47.0, weight=48.0)
    g.hbar(502.3, 844.4, 183.1, weight=96.0)
    g.diag(517.2, 25.4, 531.1, 39.3, weight=96.0)
    g.hbar(531.1, 817.7, 46.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_553e() -> Glyph:
    """唾 U+553E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni553E", advance=1000, unicode=0x553E, note="唾：自动生成")
    g.diag(120.5, 519.6, 109.7, 505.2, weight=48.0)
    g.vbar(138.6, 301.2, 505.2, weight=48.0)
    g.hbar(125.5, 311.5, 525.7, weight=48.0)
    g.diag(311.5, 539.8, 280.5, 393.8, weight=48.0)
    g.diag(280.5, 393.8, 258.4, 369.4, weight=48.0)
    g.diag(172.1, 319.9, 187.2, 338.8, weight=96.0)
    g.hbar(187.2, 314.1, 341.9, weight=96.0)
    g.hbar(701.4, 764.8, 736.0, weight=96.0)
    g.hbar(422.7, 701.4, 680.0, weight=96.0)
    g.vbar(419.6, 544.6, 619.3, weight=96.0)
    g.diag(415.3, 453.4, 437.5, 493.6, weight=96.0)
    g.hbar(437.5, 756.9, 519.2, weight=96.0)
    g.diag(756.9, 544.8, 770.0, 502.5, weight=96.0)
    g.diag(562.1, 645.1, 585.3, 634.3, weight=96.0)
    g.vbar(600.8, 79.1, 634.3, weight=96.0)
    g.diag(616.4, 79.1, 580.4, 41.2, weight=96.0)
    g.hbar(315.8, 937.0, 326.0, weight=96.0)
    g.diag(428.4, 462.8, 482.3, 199.2, weight=96.0)
    g.diag(736.6, 506.2, 778.4, 429.8, weight=92.0)
    g.diag(778.4, 429.8, 709.0, 220.6, weight=92.0)
    g.diag(445.7, 193.5, 398.2, 153.7, weight=96.0)
    g.hbar(398.2, 777.2, 176.8, weight=96.0)
    g.diag(777.2, 199.9, 762.7, 221.8, weight=96.0)
    g.hbar(414.2, 808.3, 4.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_5553() -> Glyph:
    """啓 U+5553 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5553", advance=1000, unicode=0x5553, note="啓：自动生成")
    g.diag(296.1, 750.4, 377.1, 701.2, weight=76.0)
    g.diag(377.1, 701.2, 394.6, 606.9, weight=76.0)
    g.diag(265.2, 559.4, 270.2, 556.4, weight=96.0)
    g.hbar(270.2, 446.2, 562.6, weight=96.0)
    g.diag(446.2, 568.8, 379.0, 460.2, weight=96.0)
    g.hbar(256.6, 423.9, 423.7, weight=96.0)
    g.diag(227.4, 565.5, 115.3, 190.1, weight=96.0)
    g.diag(115.3, 190.1, 60.0, 144.0, weight=96.0)
    g.diag(604.6, 787.0, 637.8, 745.0, weight=96.0)
    g.diag(637.8, 745.0, 493.4, 503.8, weight=96.0)
    g.hbar(571.6, 837.9, 602.3, weight=48.0)
    g.diag(666.5, 571.4, 637.3, 467.3, weight=48.0)
    g.diag(637.3, 467.3, 450.4, 304.1, weight=48.0)
    g.diag(526.5, 522.9, 940.0, 279.0, weight=84.0)
    g.diag(325.2, 201.9, 311.5, 176.8, weight=48.0)
    g.vbar(342.4, -29.1, 176.8, weight=48.0)
    g.hbar(327.2, 630.8, 206.2, weight=48.0)
    g.diag(630.8, 224.5, 667.4, 183.0, weight=48.0)
    g.diag(667.4, 183.0, 594.8, 41.8, weight=48.0)
    g.hbar(377.7, 482.3, -5.4, weight=48.0)
    g.hbar(482.3, 673.0, 7.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_5589() -> Glyph:
    """喉 U+5589 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5589", advance=1000, unicode=0x5589, note="喉：自动生成")
    g.diag(101.9, 490.3, 148.2, 263.1, weight=96.0)
    g.hbar(128.6, 283.0, 486.9, weight=48.0)
    g.vbar(258.0, 344.5, 504.3, weight=48.0)
    g.diag(158.6, 300.1, 173.3, 316.8, weight=96.0)
    g.hbar(173.3, 272.1, 325.2, weight=96.0)
    g.vbar(435.2, 629.1, 725.2, weight=48.0)
    g.diag(433.0, 629.1, 338.4, 414.0, weight=48.0)
    g.diag(338.4, 414.0, 272.9, 381.3, weight=48.0)
    g.vbar(386.9, -8.2, 454.5, weight=48.0)
    g.hbar(565.1, 779.0, 622.1, weight=48.0)
    g.diag(779.0, 633.9, 706.2, 515.5, weight=48.0)
    g.hbar(508.1, 895.0, 483.7, weight=48.0)
    g.diag(566.2, 430.8, 586.8, 395.0, weight=92.0)
    g.diag(586.8, 395.0, 517.5, 227.9, weight=92.0)
    g.hbar(594.5, 761.7, 357.4, weight=96.0)
    g.diag(761.7, 370.7, 796.3, 470.0, weight=96.0)
    g.hbar(433.1, 905.8, 211.0, weight=84.0)
    g.vbar(629.0, 218.2, 322.6, weight=56.0)
    g.diag(623.3, 218.2, 475.7, 1.6, weight=56.0)
    g.diag(678.5, 200.2, 823.3, 17.4, weight=48.0)
    g.hbar(823.3, 947.0, 3.6, weight=48.0)
    return g
def g_cjk_unified_ideograph_559a() -> Glyph:
    """喚 U+559A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni559A", advance=1000, unicode=0x559A, note="喚：自动生成")
    g.diag(117.6, 493.8, 155.3, 270.7, weight=96.0)
    g.diag(153.2, 479.4, 162.0, 497.1, weight=96.0)
    g.hbar(162.0, 302.5, 502.0, weight=96.0)
    g.vbar(288.1, 382.2, 506.8, weight=96.0)
    g.diag(273.8, 382.2, 252.4, 371.5, weight=96.0)
    g.diag(169.7, 306.3, 184.5, 324.2, weight=96.0)
    g.hbar(184.5, 289.0, 334.0, weight=96.0)
    g.diag(289.0, 343.8, 297.2, 351.7, weight=96.0)
    g.diag(520.8, 775.1, 550.6, 738.2, weight=48.0)
    g.diag(550.6, 738.2, 418.5, 475.6, weight=48.0)
    g.hbar(518.5, 695.0, 639.2, weight=48.0)
    g.diag(695.0, 642.9, 573.4, 487.2, weight=48.0)
    g.vbar(404.3, 454.9, 458.3, weight=48.0)
    g.diag(404.2, 454.9, 441.4, 248.8, weight=48.0)
    g.diag(441.4, 248.8, 451.5, 239.7, weight=48.0)
    g.hbar(417.7, 797.5, 480.1, weight=48.0)
    g.diag(797.5, 508.1, 725.7, 271.4, weight=48.0)
    g.diag(510.1, 439.8, 530.3, 400.3, weight=48.0)
    g.diag(530.3, 400.3, 451.0, 303.9, weight=48.0)
    g.diag(597.7, 460.9, 601.5, 457.9, weight=48.0)
    g.diag(601.5, 457.9, 634.9, 346.2, weight=48.0)
    g.hbar(634.9, 715.6, 347.0, weight=48.0)
    g.hbar(715.6, 741.4, 342.4, weight=48.0)
    g.hbar(272.8, 942.0, 228.5, weight=48.0)
    g.vbar(499.4, 198.3, 322.9, weight=48.0)
    g.diag(497.0, 198.3, 267.0, -35.1, weight=48.0)
    g.diag(585.1, 219.0, 653.6, 142.6, weight=48.0)
    g.diag(653.6, 142.6, 913.8, -20.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_559d() -> Glyph:
    """喝 U+559D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni559D", advance=1000, unicode=0x559D, note="喝：自动生成")
    g.diag(142.6, 542.0, 198.6, 304.4, weight=96.0)
    g.hbar(164.6, 311.4, 548.4, weight=48.0)
    g.diag(311.4, 573.6, 358.5, 542.5, weight=48.0)
    g.diag(358.5, 542.5, 297.4, 393.4, weight=48.0)
    g.diag(207.0, 341.9, 224.7, 360.9, weight=96.0)
    g.hbar(224.7, 337.5, 369.4, weight=96.0)
    g.diag(337.5, 378.0, 344.7, 389.3, weight=96.0)
    g.vbar(499.0, 722.9, 733.3, weight=48.0)
    g.vbar(526.0, 484.8, 722.9, weight=48.0)
    g.hbar(511.5, 732.1, 698.1, weight=48.0)
    g.vbar(747.9, 519.5, 669.1, weight=48.0)
    g.hbar(735.4, 763.8, 520.6, weight=48.0)
    g.hbar(553.7, 556.5, 622.8, weight=84.0)
    g.hbar(553.7, 757.9, 625.7, weight=84.0)
    g.diag(571.0, 505.9, 579.9, 515.8, weight=84.0)
    g.hbar(579.9, 726.5, 527.3, weight=84.0)
    g.diag(540.3, 475.2, 561.5, 434.1, weight=96.0)
    g.diag(561.5, 434.1, 442.6, 320.4, weight=96.0)
    g.diag(521.3, 359.9, 796.7, 221.2, weight=76.0)
    g.vbar(806.1, -66.1, 221.2, weight=76.0)
    g.diag(815.6, -66.1, 721.3, -12.6, weight=76.0)
    g.diag(721.3, -12.6, 697.4, 63.2, weight=76.0)
    g.diag(627.1, 344.0, 657.1, 316.5, weight=96.0)
    g.diag(657.1, 316.5, 528.7, 157.2, weight=96.0)
    g.hbar(479.7, 528.7, 153.9, weight=96.0)
    g.hbar(646.1, 721.9, 232.1, weight=84.0)
    g.diag(721.9, 218.5, 750.4, 123.0, weight=84.0)
    g.diag(432.3, 310.1, 535.3, 142.4, weight=64.0)
    g.hbar(535.3, 841.9, 100.7, weight=64.0)
    return g
def g_cjk_unified_ideograph_55c5() -> Glyph:
    """嗅 U+55C5 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni55C5", advance=1000, unicode=0x55C5, note="嗅：自动生成")
    g.diag(110.1, 526.7, 164.0, 296.0, weight=96.0)
    g.hbar(135.0, 320.5, 530.8, weight=48.0)
    g.vbar(291.4, 380.5, 553.6, weight=48.0)
    g.diag(173.8, 333.2, 181.7, 343.0, weight=96.0)
    g.hbar(181.7, 301.5, 358.1, weight=96.0)
    g.diag(574.6, 801.5, 598.8, 771.2, weight=96.0)
    g.diag(598.8, 771.2, 526.1, 655.3, weight=96.0)
    g.diag(526.1, 655.3, 507.9, 636.0, weight=96.0)
    g.vbar(458.2, 295.8, 632.5, weight=96.0)
    g.hbar(480.2, 706.0, 631.0, weight=48.0)
    g.vbar(724.1, 382.0, 650.9, weight=48.0)
    g.diag(742.2, 382.0, 691.1, 347.1, weight=48.0)
    g.hbar(487.7, 695.0, 523.6, weight=64.0)
    g.hbar(485.6, 696.8, 432.7, weight=64.0)
    g.diag(482.2, 319.7, 497.6, 332.0, weight=56.0)
    g.hbar(497.6, 700.8, 347.3, weight=56.0)
    g.hbar(284.8, 868.3, 180.2, weight=48.0)
    g.diag(516.6, 315.4, 493.5, 182.5, weight=48.0)
    g.diag(493.5, 182.5, 282.8, -52.5, weight=48.0)
    g.diag(573.6, 172.1, 942.0, -61.5, weight=48.0)
    g.hbar(749.2, 865.3, 367.5, weight=64.0)
    g.diag(865.3, 348.3, 894.6, 308.9, weight=64.0)
    return g
def g_cjk_unified_ideograph_55e3() -> Glyph:
    """嗣 U+55E3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni55E3", advance=1000, unicode=0x55E3, note="嗣：自动生成")
    g.vbar(240.5, 537.6, 723.3, weight=48.0)
    g.hbar(223.0, 428.6, 730.3, weight=48.0)
    g.diag(428.6, 751.8, 465.0, 719.0, weight=48.0)
    g.diag(465.0, 719.0, 410.1, 613.9, weight=48.0)
    g.hbar(269.1, 442.4, 587.0, weight=48.0)
    g.vbar(122.3, 327.6, 426.3, weight=48.0)
    g.vbar(116.1, 29.6, 327.6, weight=48.0)
    g.hbar(129.5, 462.4, 450.4, weight=48.0)
    g.diag(462.4, 483.9, 487.8, 361.2, weight=48.0)
    g.vbar(482.1, 70.8, 361.2, weight=48.0)
    g.hbar(360.0, 476.5, 95.6, weight=48.0)
    g.hbar(166.5, 451.8, 291.0, weight=96.0)
    g.diag(218.2, 409.9, 243.5, 384.3, weight=48.0)
    g.vbar(241.3, 158.0, 384.3, weight=48.0)
    g.diag(320.2, 438.1, 371.7, 111.8, weight=48.0)
    g.diag(499.9, 714.6, 785.1, 567.6, weight=96.0)
    g.diag(785.1, 567.6, 972.0, -72.0, weight=96.0)
    g.hbar(749.4, 972.0, -36.4, weight=96.0)
    g.hbar(525.2, 860.7, 513.8, weight=96.0)
    g.vbar(589.3, 356.0, 382.8, weight=48.0)
    g.vbar(602.6, 207.7, 356.0, weight=48.0)
    g.diag(612.3, 378.8, 614.0, 377.7, weight=96.0)
    g.hbar(614.0, 769.1, 383.5, weight=96.0)
    g.diag(769.1, 389.3, 715.6, 283.1, weight=96.0)
    g.diag(627.5, 225.4, 644.7, 242.6, weight=96.0)
    g.hbar(644.7, 749.9, 250.1, weight=96.0)
    g.diag(749.9, 257.6, 760.0, 268.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_5606() -> Glyph:
    """嘆 U+5606 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5606", advance=1000, unicode=0x5606, note="嘆：自动生成")
    g.diag(95.0, 529.3, 154.8, 297.8, weight=48.0)
    g.diag(147.1, 525.4, 149.4, 524.1, weight=48.0)
    g.hbar(149.4, 306.8, 534.5, weight=48.0)
    g.diag(306.8, 544.8, 279.3, 421.3, weight=48.0)
    g.diag(279.3, 421.3, 257.1, 405.8, weight=48.0)
    g.dot(243.6, 363.4, w=96.0, h=124.8, slant=-14.0)
    g.hbar(374.7, 855.1, 633.0, weight=92.0)
    g.diag(452.9, 726.1, 490.2, 704.0, weight=96.0)
    g.diag(490.2, 704.0, 514.6, 504.2, weight=96.0)
    g.diag(652.5, 782.0, 681.5, 743.4, weight=96.0)
    g.diag(681.5, 743.4, 642.9, 577.5, weight=96.0)
    g.diag(642.9, 577.5, 626.5, 565.0, weight=96.0)
    g.hbar(529.1, 671.8, 522.0, weight=64.0)
    g.diag(367.0, 430.9, 396.0, 410.6, weight=64.0)
    g.vbar(416.2, 283.3, 410.6, weight=64.0)
    g.hbar(426.8, 539.9, 418.2, weight=48.0)
    g.hbar(539.9, 787.8, 442.6, weight=48.0)
    g.diag(787.8, 457.5, 750.0, 387.5, weight=48.0)
    g.hbar(731.6, 750.0, 385.1, weight=48.0)
    g.hbar(450.0, 766.4, 332.5, weight=48.0)
    g.hbar(447.1, 716.2, 243.3, weight=64.0)
    g.hbar(307.2, 880.2, 141.0, weight=48.0)
    g.vbar(524.3, 304.7, 501.3, weight=96.0)
    g.diag(518.5, 304.7, 305.3, -62.0, weight=96.0)
    g.diag(576.3, 128.0, 940.0, -62.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_5631() -> Glyph:
    """嘱 U+5631 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5631", advance=1000, unicode=0x5631, note="嘱：自动生成")
    g.diag(119.2, 546.8, 166.1, 324.2, weight=96.0)
    g.hbar(142.0, 322.3, 551.9, weight=48.0)
    g.diag(322.3, 572.6, 299.3, 441.7, weight=48.0)
    g.diag(299.3, 441.7, 315.7, 414.2, weight=48.0)
    g.diag(180.4, 359.8, 200.3, 382.4, weight=96.0)
    g.hbar(200.3, 330.0, 388.6, weight=96.0)
    g.hbar(500.4, 782.0, 728.7, weight=48.0)
    g.diag(782.0, 755.3, 817.9, 721.8, weight=48.0)
    g.diag(817.9, 721.8, 770.7, 637.7, weight=48.0)
    g.hbar(490.3, 798.7, 593.4, weight=48.0)
    g.vbar(799.0, 623.0, 645.4, weight=48.0)
    g.diag(484.4, 722.5, 217.5, -26.8, weight=96.0)
    g.hbar(742.2, 797.5, 533.3, weight=56.0)
    g.hbar(545.8, 742.2, 498.7, weight=56.0)
    g.vbar(548.1, 412.9, 458.9, weight=56.0)
    g.diag(461.1, 408.8, 529.9, 367.5, weight=48.0)
    g.vbar(547.5, 252.5, 367.5, weight=48.0)
    g.hbar(544.3, 826.6, 399.8, weight=48.0)
    g.diag(826.6, 419.3, 776.3, 333.7, weight=48.0)
    g.hbar(570.5, 806.4, 294.2, weight=48.0)
    g.vbar(807.0, 320.0, 342.8, weight=48.0)
    g.diag(398.8, 210.1, 444.1, 172.4, weight=48.0)
    g.vbar(452.1, -49.8, 172.4, weight=48.0)
    g.hbar(467.6, 608.0, 185.8, weight=64.0)
    g.hbar(608.0, 928.2, 208.5, weight=64.0)
    g.vbar(914.1, -57.0, 226.1, weight=64.0)
    g.diag(900.0, -57.0, 819.1, 11.3, weight=64.0)
    g.diag(647.9, 472.3, 673.7, 453.2, weight=96.0)
    g.vbar(671.1, 114.9, 453.2, weight=96.0)
    g.diag(668.5, 114.9, 653.3, 92.2, weight=96.0)
    g.hbar(489.7, 768.0, 74.0, weight=96.0)
    g.diag(768.0, 95.0, 771.3, 91.1, weight=96.0)
    g.diag(766.2, 116.9, 823.7, 64.9, weight=48.0)
    g.vbar(820.3, -11.5, 64.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_5632() -> Glyph:
    """嘲 U+5632 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5632", advance=1000, unicode=0x5632, note="嘲：自动生成")
    g.diag(117.3, 523.3, 159.5, 311.3, weight=96.0)
    g.diag(152.7, 508.4, 160.1, 523.2, weight=84.0)
    g.hbar(160.1, 293.1, 527.8, weight=84.0)
    g.diag(293.1, 532.5, 269.9, 410.1, weight=84.0)
    g.diag(269.9, 410.1, 283.0, 396.1, weight=84.0)
    g.diag(173.7, 347.0, 190.7, 365.2, weight=96.0)
    g.hbar(190.7, 297.0, 366.6, weight=96.0)
    g.hbar(319.4, 644.7, 585.2, weight=96.0)
    g.diag(480.5, 772.0, 520.8, 730.6, weight=96.0)
    g.diag(520.8, 730.6, 472.4, 496.3, weight=96.0)
    g.diag(381.5, 461.6, 371.2, 447.2, weight=48.0)
    g.diag(371.2, 447.2, 412.5, 271.6, weight=48.0)
    g.diag(399.3, 454.2, 418.9, 472.2, weight=96.0)
    g.hbar(418.9, 632.7, 478.0, weight=96.0)
    g.vbar(604.3, 284.9, 483.8, weight=96.0)
    g.hbar(409.3, 576.6, 375.4, weight=64.0)
    g.diag(427.3, 283.8, 435.3, 292.8, weight=64.0)
    g.hbar(435.3, 555.2, 302.0, weight=64.0)
    g.hbar(249.9, 648.3, 176.9, weight=96.0)
    g.diag(456.4, 280.8, 473.4, 170.4, weight=48.0)
    g.vbar(477.9, -57.0, 170.4, weight=48.0)
    g.diag(727.1, 620.3, 698.6, 444.7, weight=48.0)
    g.diag(698.6, 444.7, 569.7, -46.0, weight=48.0)
    g.hbar(731.2, 861.7, 621.6, weight=48.0)
    g.vbar(875.0, 402.1, 635.3, weight=48.0)
    g.vbar(883.9, -9.3, 402.1, weight=48.0)
    g.diag(879.4, -9.3, 776.2, 51.3, weight=48.0)
    g.diag(754.1, 435.2, 775.0, 457.2, weight=96.0)
    g.hbar(775.0, 865.9, 458.3, weight=96.0)
    g.diag(739.1, 293.8, 752.2, 309.3, weight=96.0)
    g.hbar(752.2, 866.8, 310.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_5668() -> Glyph:
    """器 U+5668 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5668", advance=1000, unicode=0x5668, note="器：自动生成")
    g.diag(218.5, 708.7, 213.0, 696.6, weight=48.0)
    g.vbar(241.1, 545.8, 696.6, weight=48.0)
    g.hbar(228.0, 421.3, 713.7, weight=48.0)
    g.vbar(396.8, 611.4, 724.1, weight=48.0)
    g.hbar(272.2, 399.3, 588.6, weight=48.0)
    g.vbar(563.2, 577.4, 739.3, weight=48.0)
    g.hbar(556.2, 742.1, 738.2, weight=48.0)
    g.diag(742.1, 749.3, 686.4, 635.9, weight=48.0)
    g.hbar(586.9, 722.3, 605.5, weight=48.0)
    g.diag(722.3, 619.0, 732.2, 573.0, weight=48.0)
    g.hbar(207.5, 721.9, 432.7, weight=48.0)
    g.diag(420.7, 551.3, 484.7, 463.7, weight=96.0)
    g.diag(484.7, 463.7, 148.9, 176.7, weight=96.0)
    g.vbar(475.4, 387.3, 410.3, weight=48.0)
    g.hbar(480.0, 854.1, 315.4, weight=48.0)
    g.diag(733.5, 579.0, 791.5, 526.0, weight=76.0)
    g.diag(791.5, 526.0, 750.4, 466.1, weight=76.0)
    g.vbar(184.7, 119.7, 139.9, weight=48.0)
    g.vbar(205.0, -36.0, 119.7, weight=48.0)
    g.hbar(194.8, 407.7, 139.8, weight=48.0)
    g.diag(407.7, 149.8, 344.2, 28.7, weight=48.0)
    g.hbar(234.9, 381.8, -3.8, weight=48.0)
    g.vbar(381.0, 14.5, 37.4, weight=48.0)
    g.diag(537.3, 144.7, 527.7, 130.7, weight=48.0)
    g.vbar(550.1, -25.9, 130.7, weight=48.0)
    g.hbar(543.2, 731.5, 149.8, weight=48.0)
    g.diag(731.5, 162.0, 757.2, 124.0, weight=48.0)
    g.diag(757.2, 124.0, 706.4, 34.3, weight=48.0)
    g.hbar(578.0, 743.0, 4.3, weight=48.0)
    g.vbar(742.4, 19.1, 45.1, weight=48.0)
    return g
def g_cjk_unified_ideograph_5674() -> Glyph:
    """噴 U+5674 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5674", advance=1000, unicode=0x5674, note="噴：自动生成")
    g.diag(141.3, 565.4, 189.5, 357.2, weight=96.0)
    g.hbar(169.6, 330.8, 565.9, weight=48.0)
    g.vbar(305.2, 442.7, 583.6, weight=48.0)
    g.diag(203.7, 392.9, 218.7, 408.9, weight=96.0)
    g.hbar(218.7, 320.3, 418.9, weight=96.0)
    g.diag(320.3, 428.8, 324.8, 436.8, weight=96.0)
    g.hbar(485.4, 717.8, 649.9, weight=96.0)
    g.diag(717.8, 687.1, 739.8, 658.5, weight=96.0)
    g.vbar(611.3, 675.1, 694.1, weight=84.0)
    g.vbar(608.0, 546.3, 675.1, weight=84.0)
    g.hbar(334.4, 912.6, 525.2, weight=64.0)
    g.diag(477.2, 527.1, 486.6, 582.4, weight=48.0)
    g.vbar(505.6, 417.0, 582.4, weight=48.0)
    g.diag(712.2, 643.8, 736.2, 595.1, weight=96.0)
    g.diag(736.2, 595.1, 684.3, 457.6, weight=96.0)
    g.diag(500.9, 402.0, 490.1, 379.5, weight=48.0)
    g.vbar(498.3, 108.6, 379.5, weight=48.0)
    g.hbar(510.3, 699.2, 362.4, weight=48.0)
    g.vbar(715.3, 125.5, 331.0, weight=48.0)
    g.hbar(523.0, 733.1, 309.9, weight=56.0)
    g.hbar(525.0, 733.7, 229.4, weight=64.0)
    g.diag(523.4, 117.5, 544.7, 135.3, weight=56.0)
    g.hbar(544.7, 734.8, 136.0, weight=56.0)
    g.vbar(536.9, 47.5, 100.1, weight=56.0)
    g.diag(536.2, 47.5, 378.4, -72.0, weight=56.0)
    g.diag(697.8, 104.3, 810.0, -66.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_5687() -> Glyph:
    """嚇 U+5687 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5687", advance=1000, unicode=0x5687, note="嚇：自动生成")
    g.diag(83.0, 491.2, 109.7, 461.7, weight=96.0)
    g.vbar(124.5, 282.4, 461.7, weight=96.0)
    g.diag(134.5, 470.3, 145.9, 484.6, weight=76.0)
    g.hbar(145.9, 261.5, 490.3, weight=76.0)
    g.vbar(249.0, 387.3, 496.0, weight=76.0)
    g.diag(236.5, 387.3, 218.4, 373.0, weight=76.0)
    g.dot(209.8, 337.2, w=96.0, h=112.8, slant=-14.0)
    g.hbar(348.1, 555.1, 559.4, weight=96.0)
    g.diag(422.5, 736.3, 465.4, 697.2, weight=96.0)
    g.vbar(463.0, 480.8, 697.2, weight=96.0)
    g.diag(460.6, 480.8, 445.4, 459.8, weight=96.0)
    g.hbar(289.0, 572.2, 433.1, weight=96.0)
    g.diag(352.9, 387.3, 411.4, 338.9, weight=64.0)
    g.diag(411.4, 338.9, 222.2, 55.4, weight=64.0)
    g.diag(448.2, 418.8, 485.2, 388.1, weight=84.0)
    g.vbar(471.2, 31.7, 388.1, weight=84.0)
    g.hbar(390.1, 457.1, 45.0, weight=84.0)
    g.diag(284.2, 291.9, 228.9, 167.0, weight=64.0)
    g.diag(503.6, 334.8, 543.1, 306.9, weight=96.0)
    g.diag(543.1, 306.9, 558.9, 283.3, weight=96.0)
    g.hbar(638.0, 871.7, 576.6, weight=96.0)
    g.diag(701.9, 766.8, 745.8, 728.7, weight=96.0)
    g.vbar(741.0, 477.9, 728.7, weight=96.0)
    g.diag(736.2, 477.9, 720.0, 455.0, weight=96.0)
    g.hbar(590.3, 946.0, 433.1, weight=96.0)
    g.diag(649.5, 390.2, 708.3, 353.3, weight=64.0)
    g.diag(708.3, 353.3, 541.7, 21.1, weight=64.0)
    g.diag(764.9, 422.6, 787.6, 261.1, weight=56.0)
    g.vbar(782.9, -45.5, 261.1, weight=56.0)
    g.diag(778.1, -45.5, 680.0, 4.9, weight=56.0)
    g.diag(598.9, 282.4, 569.4, 167.0, weight=64.0)
    g.diag(857.4, 270.0, 926.0, 218.5, weight=96.0)
    g.diag(926.0, 218.5, 947.0, 163.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_57f9() -> Glyph:
    """培 U+57F9 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni57F9", advance=1000, unicode=0x57F9, note="培：自动生成")
    g.hbar(108.5, 439.2, 432.6, weight=96.0)
    g.diag(208.3, 704.2, 258.7, 661.5, weight=96.0)
    g.vbar(254.3, 236.2, 661.5, weight=96.0)
    g.diag(250.0, 236.2, 233.5, 214.9, weight=96.0)
    g.hbar(63.0, 119.2, 142.7, weight=48.0)
    g.diag(119.2, 136.4, 367.5, 270.1, weight=48.0)
    g.diag(552.2, 770.0, 637.5, 707.1, weight=96.0)
    g.diag(637.5, 707.1, 672.7, 613.5, weight=96.0)
    g.vbar(467.8, 490.5, 531.6, weight=96.0)
    g.hbar(473.0, 743.7, 560.9, weight=96.0)
    g.diag(743.7, 590.2, 713.6, 539.5, weight=96.0)
    g.dot(502.6, 422.5, w=96.0, h=124.8, slant=-14.0)
    g.diag(677.2, 535.7, 702.6, 480.8, weight=96.0)
    g.diag(702.6, 480.8, 624.9, 345.7, weight=96.0)
    g.hbar(357.3, 932.0, 311.2, weight=96.0)
    g.vbar(454.8, 168.4, 180.5, weight=48.0)
    g.vbar(482.3, -20.9, 168.4, weight=48.0)
    g.hbar(468.3, 767.4, 183.3, weight=48.0)
    g.diag(767.4, 191.9, 696.6, 49.1, weight=48.0)
    g.diag(514.7, -6.3, 534.0, 9.5, weight=48.0)
    g.hbar(534.0, 734.2, 20.9, weight=48.0)
    g.vbar(733.4, 32.3, 62.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_5806() -> Glyph:
    """堆 U+5806 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5806", advance=1000, unicode=0x5806, note="堆：自动生成")
    g.hbar(118.5, 319.9, 497.6, weight=96.0)
    g.hbar(319.9, 377.8, 508.0, weight=96.0)
    g.diag(222.5, 742.5, 281.0, 695.3, weight=96.0)
    g.vbar(262.9, 284.3, 695.3, weight=96.0)
    g.hbar(63.0, 116.8, 190.8, weight=96.0)
    g.hbar(116.8, 451.8, 260.9, weight=96.0)
    g.diag(532.9, 787.2, 515.1, 674.1, weight=48.0)
    g.diag(515.1, 674.1, 367.5, 435.0, weight=48.0)
    g.vbar(467.5, -57.2, 514.2, weight=48.0)
    g.diag(608.4, 733.5, 719.7, 681.2, weight=96.0)
    g.diag(719.7, 681.2, 750.7, 602.6, weight=96.0)
    g.hbar(516.1, 823.8, 567.1, weight=96.0)
    g.diag(823.8, 573.4, 771.7, 622.4, weight=96.0)
    g.hbar(530.9, 764.1, 413.0, weight=96.0)
    g.diag(764.1, 427.1, 803.9, 351.1, weight=96.0)
    g.hbar(526.5, 785.7, 296.6, weight=96.0)
    g.diag(785.7, 315.2, 819.2, 386.9, weight=96.0)
    g.diag(659.3, 515.8, 692.0, 490.5, weight=96.0)
    g.vbar(689.0, 184.2, 490.5, weight=96.0)
    g.diag(686.0, 184.2, 672.0, 167.5, weight=96.0)
    g.diag(515.4, 126.7, 525.3, 118.5, weight=96.0)
    g.hbar(525.3, 922.0, 132.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_5815() -> Glyph:
    """堕 U+5815 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5815", advance=1000, unicode=0x5815, note="堕：自动生成")
    g.diag(245.6, 649.6, 280.9, 666.2, weight=48.0)
    g.diag(280.9, 666.2, 415.7, 449.5, weight=48.0)
    g.hbar(272.1, 415.7, 461.6, weight=48.0)
    g.diag(173.4, 691.3, 219.1, 645.6, weight=96.0)
    g.vbar(207.5, 213.3, 645.6, weight=96.0)
    g.hbar(431.8, 818.3, 662.3, weight=96.0)
    g.diag(565.0, 792.0, 525.4, 629.8, weight=48.0)
    g.diag(525.4, 629.8, 342.3, 330.2, weight=48.0)
    g.vbar(544.7, 289.6, 548.9, weight=48.0)
    g.diag(573.1, 536.7, 701.0, 454.6, weight=48.0)
    g.vbar(708.2, 274.0, 454.6, weight=48.0)
    g.hbar(625.0, 715.3, 290.4, weight=48.0)
    g.diag(572.1, 444.2, 579.4, 456.3, weight=48.0)
    g.hbar(579.4, 672.8, 459.4, weight=48.0)
    g.diag(572.1, 373.0, 580.9, 385.5, weight=56.0)
    g.hbar(580.9, 681.0, 385.3, weight=56.0)
    g.hbar(322.9, 647.4, 155.3, weight=96.0)
    g.diag(449.1, 271.3, 491.8, 227.5, weight=96.0)
    g.vbar(489.7, 29.2, 227.5, weight=96.0)
    g.diag(487.7, 29.2, 471.4, 8.9, weight=96.0)
    g.hbar(180.6, 836.6, -27.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_5824() -> Glyph:
    """堤 U+5824 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5824", advance=1000, unicode=0x5824, note="堤：自动生成")
    g.hbar(176.8, 225.0, 410.8, weight=96.0)
    g.hbar(176.8, 323.7, 433.7, weight=96.0)
    g.hbar(303.1, 323.7, 457.5, weight=96.0)
    g.diag(218.9, 684.9, 275.0, 639.5, weight=96.0)
    g.vbar(257.7, 240.3, 639.5, weight=96.0)
    g.hbar(73.0, 186.5, 177.5, weight=48.0)
    g.hbar(186.5, 413.2, 232.2, weight=48.0)
    g.diag(493.6, 677.8, 485.3, 656.5, weight=48.0)
    g.diag(485.3, 656.5, 520.4, 440.7, weight=48.0)
    g.diag(502.5, 665.1, 523.6, 690.0, weight=48.0)
    g.hbar(523.6, 736.9, 698.1, weight=48.0)
    g.vbar(710.0, 476.4, 706.1, weight=48.0)
    g.hbar(662.6, 683.2, 476.0, weight=48.0)
    g.diag(528.4, 561.5, 537.7, 580.1, weight=84.0)
    g.hbar(537.7, 674.9, 580.0, weight=84.0)
    g.dot(591.1, 472.2, w=84.0, h=109.2, slant=-14.0)
    g.hbar(368.2, 854.5, 347.5, weight=92.0)
    g.diag(575.4, 348.0, 606.8, 315.7, weight=96.0)
    g.vbar(603.3, 116.9, 315.7, weight=96.0)
    g.diag(599.9, 116.9, 618.5, 87.5, weight=96.0)
    g.dot(700.8, 236.8, w=96.0, h=124.8, slant=-14.0)
    g.diag(411.4, 276.1, 460.3, 241.6, weight=92.0)
    g.diag(460.3, 241.6, 249.3, 1.3, weight=92.0)
    g.vbar(461.8, 137.8, 181.5, weight=96.0)
    g.hbar(461.8, 927.0, 64.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_582a() -> Glyph:
    """堪 U+582A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni582A", advance=1000, unicode=0x582A, note="堪：自动生成")
    g.hbar(93.6, 349.7, 422.8, weight=96.0)
    g.diag(201.4, 681.8, 251.5, 642.0, weight=96.0)
    g.vbar(248.1, 244.7, 642.0, weight=96.0)
    g.diag(244.8, 244.7, 228.1, 220.1, weight=96.0)
    g.hbar(63.0, 119.9, 133.7, weight=96.0)
    g.diag(119.9, 128.4, 351.6, 259.7, weight=96.0)
    g.hbar(404.0, 836.0, 549.3, weight=84.0)
    g.diag(465.3, 685.7, 505.8, 636.3, weight=96.0)
    g.vbar(510.5, 260.7, 636.3, weight=96.0)
    g.diag(515.2, 260.7, 496.0, 243.9, weight=96.0)
    g.diag(662.0, 760.8, 712.9, 718.1, weight=96.0)
    g.vbar(705.2, 298.9, 718.1, weight=96.0)
    g.diag(697.4, 298.9, 679.8, 272.5, weight=96.0)
    g.hbar(535.5, 644.2, 426.7, weight=64.0)
    g.diag(538.5, 323.9, 546.7, 338.1, weight=64.0)
    g.hbar(546.7, 649.2, 342.4, weight=64.0)
    g.hbar(347.7, 922.0, 232.0, weight=48.0)
    g.diag(560.2, 177.6, 577.1, 151.0, weight=76.0)
    g.diag(577.1, 151.0, 479.9, 30.1, weight=76.0)
    g.diag(479.9, 30.1, 484.1, 41.2, weight=76.0)
    g.diag(682.8, 193.4, 771.7, 82.7, weight=64.0)
    g.diag(414.9, 175.6, 447.5, 158.3, weight=48.0)
    g.diag(447.5, 158.3, 546.0, 36.0, weight=48.0)
    g.hbar(546.0, 866.6, 11.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_584a() -> Glyph:
    """塊 U+584A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni584A", advance=1000, unicode=0x584A, note="塊：自动生成")
    g.hbar(95.2, 395.4, 434.3, weight=96.0)
    g.diag(215.5, 700.5, 277.4, 647.1, weight=96.0)
    g.vbar(255.8, 218.0, 647.1, weight=96.0)
    g.hbar(63.0, 124.2, 115.8, weight=96.0)
    g.diag(124.2, 113.2, 429.2, 293.9, weight=96.0)
    g.diag(551.7, 790.7, 586.6, 759.1, weight=76.0)
    g.diag(586.6, 759.1, 491.5, 590.5, weight=76.0)
    g.vbar(414.6, 555.0, 566.4, weight=48.0)
    g.vbar(441.1, 292.7, 555.0, weight=48.0)
    g.hbar(427.8, 760.9, 587.1, weight=48.0)
    g.diag(760.9, 615.7, 798.3, 569.9, weight=48.0)
    g.diag(798.3, 569.9, 706.1, 352.6, weight=48.0)
    g.hbar(476.1, 717.0, 452.4, weight=96.0)
    g.diag(559.9, 558.5, 594.4, 525.1, weight=56.0)
    g.diag(594.4, 525.1, 567.6, 358.2, weight=56.0)
    g.diag(484.1, 311.1, 494.8, 320.9, weight=48.0)
    g.hbar(494.8, 706.0, 341.0, weight=48.0)
    g.diag(475.9, 278.2, 507.4, 216.9, weight=96.0)
    g.diag(507.4, 216.9, 224.9, -38.3, weight=96.0)
    g.diag(588.6, 320.0, 667.0, 165.6, weight=48.0)
    g.diag(667.0, 165.6, 825.1, 42.3, weight=48.0)
    g.diag(825.1, 42.3, 896.5, 112.5, weight=48.0)
    g.diag(728.4, 323.3, 772.7, 254.4, weight=48.0)
    g.diag(772.7, 254.4, 704.4, 103.2, weight=48.0)
    g.hbar(704.4, 848.3, 114.9, weight=48.0)
    g.diag(776.0, 210.6, 861.9, 143.3, weight=48.0)
    g.vbar(858.0, 112.8, 143.3, weight=48.0)
    return g
def g_cjk_unified_ideograph_5851() -> Glyph:
    """塑 U+5851 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5851", advance=1000, unicode=0x5851, note="塑：自动生成")
    g.dot(314.5, 690.6, w=96.0, h=124.8, slant=-14.0)
    g.diag(474.4, 782.0, 492.1, 754.6, weight=96.0)
    g.diag(492.1, 754.6, 414.0, 628.6, weight=96.0)
    g.vbar(176.6, 511.1, 544.9, weight=96.0)
    g.hbar(171.2, 577.2, 572.4, weight=96.0)
    g.vbar(229.0, 352.0, 528.9, weight=48.0)
    g.hbar(253.9, 475.1, 375.5, weight=48.0)
    g.diag(490.0, 576.8, 516.5, 485.5, weight=64.0)
    g.diag(516.5, 485.5, 468.0, 370.2, weight=64.0)
    g.diag(344.3, 548.1, 405.1, 499.1, weight=96.0)
    g.diag(405.1, 499.1, 261.6, 170.5, weight=96.0)
    g.diag(261.6, 170.5, 294.2, 133.9, weight=96.0)
    g.diag(620.9, 662.9, 601.0, 552.7, weight=48.0)
    g.diag(601.0, 552.7, 513.5, 245.9, weight=48.0)
    g.diag(627.0, 653.9, 755.7, 545.1, weight=48.0)
    g.diag(755.7, 545.1, 634.4, 326.2, weight=48.0)
    g.hbar(634.4, 686.8, 314.8, weight=48.0)
    g.diag(642.8, 525.6, 653.7, 541.4, weight=76.0)
    g.hbar(653.7, 761.8, 543.2, weight=76.0)
    g.dot(694.6, 429.8, w=84.0, h=109.2, slant=-14.0)
    g.hbar(294.5, 616.6, 155.2, weight=96.0)
    g.diag(616.6, 139.8, 730.2, 242.8, weight=96.0)
    g.diag(488.9, 256.1, 511.6, 217.8, weight=96.0)
    g.vbar(507.2, 23.6, 217.8, weight=96.0)
    g.diag(502.8, 23.6, 488.1, 8.9, weight=96.0)
    g.hbar(202.4, 858.1, -26.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_5854() -> Glyph:
    """塔 U+5854 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5854", advance=1000, unicode=0x5854, note="塔：自动生成")
    g.hbar(110.1, 339.0, 481.8, weight=96.0)
    g.diag(202.1, 720.2, 248.8, 683.2, weight=96.0)
    g.vbar(245.8, 322.7, 683.2, weight=96.0)
    g.diag(242.8, 322.7, 224.1, 296.1, weight=96.0)
    g.hbar(68.0, 121.6, 203.2, weight=64.0)
    g.diag(121.6, 201.3, 347.6, 346.8, weight=64.0)
    g.hbar(347.6, 841.7, 614.9, weight=96.0)
    g.diag(436.6, 711.6, 470.2, 685.8, weight=96.0)
    g.diag(470.2, 685.8, 495.1, 524.9, weight=96.0)
    g.diag(653.0, 769.1, 688.8, 729.7, weight=96.0)
    g.diag(688.8, 729.7, 615.7, 514.4, weight=96.0)
    g.diag(584.1, 492.3, 480.3, 393.1, weight=64.0)
    g.diag(480.3, 393.1, 253.8, 175.4, weight=64.0)
    g.vbar(576.4, 416.6, 453.1, weight=64.0)
    g.hbar(576.4, 947.0, 342.9, weight=64.0)
    g.hbar(448.1, 661.7, 279.3, weight=48.0)
    g.diag(392.6, 160.1, 459.6, -39.1, weight=48.0)
    g.diag(443.3, 161.0, 457.8, 150.4, weight=48.0)
    g.hbar(457.8, 663.0, 171.2, weight=48.0)
    g.diag(663.0, 191.9, 699.0, 160.1, weight=48.0)
    g.diag(699.0, 160.1, 674.1, 70.1, weight=48.0)
    g.diag(674.1, 70.1, 653.0, 56.7, weight=48.0)
    g.diag(477.8, -10.3, 495.0, 5.7, weight=48.0)
    g.hbar(495.0, 701.9, 12.1, weight=48.0)
    return g
def g_cjk_unified_ideograph_5857() -> Glyph:
    """塗 U+5857 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5857", advance=1000, unicode=0x5857, note="塗：自动生成")
    g.dot(251.6, 690.3, w=96.0, h=123.2, slant=-14.0)
    g.dot(168.3, 557.9, w=96.0, h=104.0, slant=-14.0)
    g.diag(178.6, 233.6, 165.6, 301.2, weight=48.0)
    g.diag(165.6, 301.2, 285.7, 503.4, weight=48.0)
    g.diag(499.9, 777.0, 528.7, 738.6, weight=96.0)
    g.diag(528.7, 738.6, 313.9, 472.2, weight=96.0)
    g.diag(313.9, 472.2, 318.8, 491.7, weight=96.0)
    g.vbar(545.6, 683.6, 711.8, weight=76.0)
    g.hbar(549.3, 885.6, 615.4, weight=76.0)
    g.hbar(431.8, 612.9, 543.3, weight=56.0)
    g.hbar(359.7, 707.4, 439.1, weight=76.0)
    g.vbar(508.1, 339.8, 515.0, weight=48.0)
    g.diag(506.6, 339.8, 431.8, 300.8, weight=48.0)
    g.dot(363.6, 312.5, w=96.0, h=109.8, slant=26.0)
    g.dot(667.4, 332.9, w=96.0, h=124.8, slant=-14.0)
    g.hbar(276.0, 612.9, 130.9, weight=96.0)
    g.diag(404.5, 226.8, 441.6, 185.3, weight=56.0)
    g.vbar(438.1, 29.1, 185.3, weight=56.0)
    g.diag(434.7, 29.1, 419.1, 7.7, weight=56.0)
    g.hbar(109.4, 815.5, -26.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_585e() -> Glyph:
    """塞 U+585E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni585E", advance=1000, unicode=0x585E, note="塞：自动生成")
    g.diag(411.3, 792.0, 484.0, 751.3, weight=48.0)
    g.diag(484.0, 751.3, 511.0, 674.8, weight=48.0)
    g.diag(211.8, 646.5, 169.1, 529.4, weight=96.0)
    g.hbar(169.1, 246.0, 514.6, weight=96.0)
    g.diag(241.6, 622.3, 247.0, 617.0, weight=96.0)
    g.hbar(247.0, 760.2, 640.3, weight=96.0)
    g.diag(760.2, 663.7, 670.1, 562.4, weight=96.0)
    g.diag(325.7, 550.2, 316.9, 500.0, weight=76.0)
    g.hbar(316.9, 651.5, 527.6, weight=76.0)
    g.diag(350.2, 410.7, 353.1, 408.0, weight=76.0)
    g.hbar(353.1, 581.0, 427.4, weight=76.0)
    g.hbar(564.0, 581.0, 447.2, weight=76.0)
    g.diag(335.0, 586.9, 371.5, 546.7, weight=96.0)
    g.vbar(378.0, 351.1, 546.7, weight=96.0)
    g.diag(384.4, 351.1, 374.4, 342.1, weight=96.0)
    g.diag(517.0, 621.4, 549.0, 586.4, weight=96.0)
    g.vbar(537.3, 379.0, 586.4, weight=96.0)
    g.diag(525.7, 379.0, 509.2, 357.6, weight=96.0)
    g.hbar(167.9, 775.8, 319.8, weight=48.0)
    g.diag(351.7, 297.3, 25.9, 1.8, weight=48.0)
    g.diag(25.9, 1.8, 75.8, 60.0, weight=48.0)
    g.diag(524.7, 318.8, 924.2, 108.4, weight=48.0)
    g.diag(272.7, 161.3, 334.0, 116.9, weight=56.0)
    g.hbar(334.0, 636.3, 156.4, weight=56.0)
    g.diag(390.9, 255.3, 461.7, 204.4, weight=96.0)
    g.vbar(458.8, 28.9, 204.4, weight=96.0)
    g.diag(455.9, 28.9, 441.3, 7.6, weight=96.0)
    g.hbar(159.1, 380.9, 27.4, weight=96.0)
    g.hbar(380.9, 736.1, -11.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_5883() -> Glyph:
    """境 U+5883 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5883", advance=1000, unicode=0x5883, note="境：自动生成")
    g.hbar(115.8, 384.1, 456.1, weight=96.0)
    g.diag(227.3, 684.4, 276.3, 642.4, weight=96.0)
    g.vbar(270.5, 266.2, 642.4, weight=96.0)
    g.diag(264.7, 266.2, 247.0, 242.6, weight=96.0)
    g.hbar(81.3, 132.7, 165.7, weight=96.0)
    g.hbar(132.7, 431.0, 225.3, weight=96.0)
    g.diag(548.7, 787.0, 627.6, 748.5, weight=48.0)
    g.diag(627.6, 748.5, 657.0, 682.2, weight=48.0)
    g.diag(471.9, 617.0, 484.1, 631.1, weight=96.0)
    g.hbar(484.1, 697.7, 650.6, weight=96.0)
    g.diag(697.7, 670.1, 716.3, 642.4, weight=96.0)
    g.dot(506.5, 550.3, w=96.0, h=107.8, slant=-14.0)
    g.diag(670.0, 634.1, 691.0, 604.6, weight=96.0)
    g.diag(691.0, 604.6, 621.7, 503.0, weight=96.0)
    g.hbar(396.7, 895.9, 481.0, weight=64.0)
    g.vbar(449.2, 363.8, 376.4, weight=48.0)
    g.vbar(475.0, 180.5, 363.8, weight=48.0)
    g.hbar(461.3, 753.3, 383.0, weight=48.0)
    g.vbar(726.9, 218.0, 395.4, weight=48.0)
    g.hbar(687.0, 700.6, 219.9, weight=48.0)
    g.hbar(499.7, 615.0, 294.2, weight=64.0)
    g.diag(615.0, 309.5, 665.5, 260.5, weight=64.0)
    g.diag(515.1, 201.7, 524.8, 210.9, weight=48.0)
    g.hbar(524.8, 685.2, 222.3, weight=48.0)
    g.diag(486.6, 171.6, 510.9, 118.4, weight=96.0)
    g.diag(510.9, 118.4, 287.4, -55.2, weight=96.0)
    g.diag(598.0, 200.9, 623.1, 115.5, weight=48.0)
    g.diag(623.1, 115.5, 661.9, -56.7, weight=48.0)
    g.hbar(661.9, 909.7, -47.8, weight=48.0)
    g.vbar(905.7, -38.8, 114.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_5893() -> Glyph:
    """墓 U+5893 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5893", advance=1000, unicode=0x5893, note="墓：自动生成")
    g.diag(255.9, 586.3, 376.6, 645.9, weight=84.0)
    g.hbar(376.6, 760.2, 664.2, weight=84.0)
    g.diag(319.6, 734.8, 360.0, 705.2, weight=48.0)
    g.diag(360.0, 705.2, 384.0, 574.4, weight=48.0)
    g.diag(573.3, 727.5, 554.7, 637.9, weight=96.0)
    g.diag(554.7, 637.9, 542.4, 601.7, weight=96.0)
    g.vbar(305.6, 542.2, 558.5, weight=48.0)
    g.vbar(327.6, 371.5, 542.2, weight=48.0)
    g.hbar(317.7, 639.2, 563.2, weight=48.0)
    g.vbar(608.4, 403.3, 575.9, weight=48.0)
    g.diag(577.7, 403.3, 552.1, 414.9, weight=48.0)
    g.hbar(348.1, 481.9, 471.0, weight=56.0)
    g.diag(481.9, 486.6, 544.0, 436.8, weight=56.0)
    g.hbar(359.8, 541.6, 393.5, weight=48.0)
    g.hbar(114.6, 836.1, 290.7, weight=48.0)
    g.diag(384.4, 374.0, 324.7, 268.5, weight=48.0)
    g.diag(324.7, 268.5, 66.3, 50.7, weight=48.0)
    g.diag(557.3, 290.7, 933.7, 103.0, weight=48.0)
    g.hbar(285.2, 418.1, 144.3, weight=48.0)
    g.hbar(418.1, 652.2, 157.0, weight=48.0)
    g.diag(436.1, 262.4, 476.3, 197.6, weight=96.0)
    g.vbar(473.4, 29.0, 197.6, weight=96.0)
    g.diag(470.4, 29.0, 455.6, 8.3, weight=96.0)
    g.diag(181.8, 56.7, 264.5, -30.9, weight=96.0)
    g.hbar(264.5, 722.8, -28.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_589c() -> Glyph:
    """墜 U+589C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni589C", advance=1000, unicode=0x589C, note="墜：自动生成")
    g.hbar(160.3, 316.2, 709.1, weight=56.0)
    g.diag(316.2, 725.8, 247.6, 594.7, weight=56.0)
    g.diag(247.6, 594.7, 320.4, 447.2, weight=56.0)
    g.hbar(175.7, 320.4, 460.0, weight=56.0)
    g.vbar(146.5, 202.2, 706.1, weight=48.0)
    g.hbar(340.2, 483.0, 736.5, weight=96.0)
    g.diag(483.0, 740.9, 513.6, 674.0, weight=96.0)
    g.hbar(677.3, 713.4, 793.5, weight=48.0)
    g.diag(677.3, 797.0, 592.0, 670.8, weight=48.0)
    g.hbar(397.9, 698.6, 645.9, weight=48.0)
    g.diag(698.6, 672.6, 712.9, 618.1, weight=48.0)
    g.diag(545.4, 621.8, 382.9, 487.5, weight=48.0)
    g.diag(517.4, 546.7, 566.0, 471.7, weight=48.0)
    g.vbar(569.4, 347.5, 471.7, weight=48.0)
    g.hbar(488.4, 572.8, 340.3, weight=48.0)
    g.vbar(531.8, 496.3, 532.7, weight=48.0)
    g.diag(533.0, 496.3, 374.4, 390.1, weight=48.0)
    g.diag(374.4, 390.1, 377.8, 397.1, weight=48.0)
    g.diag(587.1, 467.4, 576.6, 422.0, weight=56.0)
    g.diag(576.6, 422.0, 408.0, 303.7, weight=56.0)
    g.diag(408.0, 303.7, 384.5, 258.5, weight=56.0)
    g.vbar(718.2, 570.1, 650.6, weight=48.0)
    g.diag(720.5, 570.1, 633.8, 494.8, weight=48.0)
    g.diag(642.1, 477.5, 801.2, 342.9, weight=96.0)
    g.hbar(801.2, 920.4, 341.9, weight=96.0)
    g.hbar(273.3, 552.4, 141.2, weight=96.0)
    g.diag(552.4, 153.6, 603.2, 221.6, weight=96.0)
    g.diag(398.5, 263.0, 443.2, 210.2, weight=96.0)
    g.vbar(440.1, 32.4, 210.2, weight=96.0)
    g.diag(437.1, 32.4, 420.0, 10.2, weight=96.0)
    g.hbar(112.6, 825.0, -23.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_58a8() -> Glyph:
    """墨 U+58A8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni58A8", advance=1000, unicode=0x58A8, note="墨：自动生成")
    g.diag(242.6, 737.6, 338.1, 526.9, weight=48.0)
    g.hbar(298.7, 431.1, 741.1, weight=48.0)
    g.hbar(431.1, 729.2, 746.8, weight=48.0)
    g.diag(729.2, 753.0, 635.1, 564.8, weight=48.0)
    g.diag(635.1, 564.8, 612.7, 584.0, weight=48.0)
    g.dot(387.3, 649.9, w=48.0, h=62.4, slant=-14.0)
    g.hbar(590.1, 609.7, 683.9, weight=48.0)
    g.diag(590.1, 686.4, 532.0, 633.2, weight=48.0)
    g.hbar(353.8, 596.0, 563.3, weight=56.0)
    g.diag(449.3, 730.7, 482.5, 701.9, weight=64.0)
    g.vbar(478.7, 403.7, 701.9, weight=64.0)
    g.diag(475.0, 403.7, 464.1, 389.1, weight=64.0)
    g.hbar(352.9, 615.7, 460.5, weight=76.0)
    g.hbar(237.7, 725.9, 356.6, weight=76.0)
    g.dot(141.7, 209.0, w=96.0, h=124.8, slant=14.0)
    g.dot(345.5, 240.5, w=96.0, h=89.8, slant=-14.0)
    g.dot(574.8, 267.1, w=96.0, h=102.3, slant=-14.0)
    g.diag(742.6, 300.5, 884.4, 175.5, weight=96.0)
    g.hbar(310.5, 661.9, 132.2, weight=96.0)
    g.diag(445.4, 235.6, 479.8, 203.1, weight=96.0)
    g.vbar(479.3, 24.9, 203.1, weight=96.0)
    g.diag(478.8, 24.9, 465.1, 5.2, weight=96.0)
    g.hbar(187.5, 797.7, -27.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_58b3() -> Glyph:
    """墳 U+58B3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni58B3", advance=1000, unicode=0x58B3, note="墳：自动生成")
    g.hbar(135.1, 367.7, 452.9, weight=96.0)
    g.diag(236.3, 696.9, 292.2, 651.7, weight=96.0)
    g.vbar(275.1, 261.8, 651.7, weight=96.0)
    g.diag(99.1, 173.9, 404.6, 317.6, weight=96.0)
    g.hbar(498.2, 742.2, 665.2, weight=96.0)
    g.diag(592.8, 782.0, 628.0, 752.3, weight=96.0)
    g.vbar(621.7, 553.1, 752.3, weight=96.0)
    g.hbar(408.4, 905.9, 513.4, weight=96.0)
    g.diag(464.2, 569.2, 500.1, 546.5, weight=48.0)
    g.diag(500.1, 546.5, 528.5, 433.0, weight=48.0)
    g.diag(744.1, 639.2, 767.8, 602.7, weight=96.0)
    g.diag(767.8, 602.7, 702.5, 453.8, weight=96.0)
    g.diag(472.7, 400.9, 506.5, 365.8, weight=48.0)
    g.vbar(501.0, 102.0, 365.8, weight=48.0)
    g.hbar(523.8, 614.0, 390.4, weight=48.0)
    g.diag(614.0, 393.2, 730.8, 328.1, weight=48.0)
    g.diag(730.8, 328.1, 759.3, 112.4, weight=48.0)
    g.diag(526.6, 290.2, 541.1, 303.5, weight=56.0)
    g.hbar(541.1, 692.1, 313.0, weight=56.0)
    g.hbar(527.6, 698.7, 222.6, weight=56.0)
    g.diag(519.1, 121.9, 531.7, 135.5, weight=64.0)
    g.hbar(531.7, 705.0, 148.2, weight=64.0)
    g.diag(705.0, 160.8, 720.5, 147.4, weight=64.0)
    g.hbar(551.1, 571.1, 47.0, weight=76.0)
    g.diag(551.1, 44.9, 397.1, -72.0, weight=76.0)
    g.diag(686.4, 77.4, 814.1, -65.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_58be() -> Glyph:
    """墾 U+58BE —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni58BE", advance=1000, unicode=0x58BE, note="墾：自动生成")
    g.diag(415.4, 740.8, 351.0, 779.9, weight=96.0)
    g.diag(351.0, 779.9, 199.3, 677.0, weight=96.0)
    g.diag(199.3, 677.0, 188.5, 659.6, weight=96.0)
    g.dot(201.6, 606.9, w=96.0, h=114.5, slant=-14.0)
    g.dot(307.4, 652.1, w=96.0, h=77.7, slant=-14.0)
    g.diag(473.7, 726.0, 101.5, 468.1, weight=48.0)
    g.diag(287.8, 522.9, 326.0, 343.4, weight=48.0)
    g.diag(326.0, 343.4, 250.3, 305.0, weight=48.0)
    g.diag(290.8, 511.0, 296.0, 474.4, weight=48.0)
    g.diag(296.0, 474.4, 114.1, 338.4, weight=48.0)
    g.diag(114.1, 338.4, 116.4, 344.6, weight=48.0)
    g.diag(339.7, 460.2, 278.0, 378.2, weight=48.0)
    g.diag(278.0, 378.2, 85.5, 220.0, weight=48.0)
    g.diag(539.6, 705.6, 579.1, 735.2, weight=48.0)
    g.hbar(579.1, 729.9, 737.4, weight=48.0)
    g.vbar(705.1, 555.5, 739.6, weight=48.0)
    g.hbar(661.1, 680.4, 552.4, weight=48.0)
    g.hbar(547.8, 679.1, 621.5, weight=56.0)
    g.diag(546.8, 527.9, 555.4, 538.3, weight=64.0)
    g.hbar(555.4, 653.4, 549.3, weight=64.0)
    g.vbar(526.8, 617.4, 717.0, weight=48.0)
    g.vbar(528.5, 325.8, 617.4, weight=48.0)
    g.diag(533.6, 325.8, 659.0, 416.2, weight=48.0)
    g.hbar(719.1, 772.1, 529.1, weight=96.0)
    g.diag(772.1, 518.5, 700.3, 453.2, weight=96.0)
    g.diag(566.8, 524.9, 919.5, 338.6, weight=48.0)
    g.vbar(330.3, 112.1, 213.3, weight=96.0)
    g.hbar(325.3, 645.5, 134.7, weight=96.0)
    g.diag(392.9, 263.0, 472.1, 191.1, weight=64.0)
    g.vbar(469.1, 28.7, 191.1, weight=64.0)
    g.diag(466.1, 28.7, 450.2, 8.3, weight=64.0)
    g.hbar(131.3, 845.8, -27.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_58c1() -> Glyph:
    """壁 U+58C1 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni58C1", advance=1000, unicode=0x58C1, note="壁：自动生成")
    g.hbar(273.0, 488.2, 671.4, weight=48.0)
    g.diag(488.2, 696.2, 425.7, 588.6, weight=48.0)
    g.hbar(258.9, 451.9, 567.2, weight=48.0)
    g.vbar(248.6, 547.6, 660.5, weight=48.0)
    g.diag(225.0, 547.6, 100.1, 238.9, weight=48.0)
    g.vbar(268.0, 270.9, 437.0, weight=48.0)
    g.hbar(275.0, 459.7, 433.3, weight=48.0)
    g.diag(459.7, 445.6, 404.5, 342.2, weight=48.0)
    g.diag(306.2, 289.2, 319.3, 305.6, weight=92.0)
    g.hbar(319.3, 442.0, 317.2, weight=92.0)
    g.diag(442.0, 328.8, 470.3, 302.8, weight=92.0)
    g.diag(630.5, 794.0, 694.6, 760.5, weight=48.0)
    g.diag(694.6, 760.5, 726.6, 695.5, weight=48.0)
    g.hbar(558.5, 771.5, 660.2, weight=92.0)
    g.vbar(771.2, 649.4, 686.8, weight=92.0)
    g.dot(586.5, 567.6, w=92.0, h=105.9, slant=-14.0)
    g.diag(719.3, 649.1, 744.2, 624.1, weight=92.0)
    g.diag(744.2, 624.1, 682.8, 513.0, weight=92.0)
    g.hbar(475.0, 809.6, 486.5, weight=92.0)
    g.diag(809.6, 520.6, 863.0, 424.4, weight=92.0)
    g.hbar(500.3, 829.4, 367.5, weight=92.0)
    g.diag(829.4, 397.9, 875.0, 483.1, weight=92.0)
    g.diag(653.2, 469.6, 683.8, 444.0, weight=92.0)
    g.vbar(678.8, 186.3, 444.0, weight=92.0)
    g.hbar(375.2, 643.0, 136.6, weight=92.0)
    g.diag(643.0, 147.6, 684.7, 206.4, weight=92.0)
    g.diag(473.3, 285.5, 516.2, 230.1, weight=92.0)
    g.vbar(514.2, 28.0, 230.1, weight=92.0)
    g.diag(512.2, 28.0, 496.4, 7.3, weight=92.0)
    g.hbar(193.8, 870.1, -28.2, weight=92.0)
    return g
def g_cjk_unified_ideograph_596a() -> Glyph:
    """奪 U+596A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni596A", advance=1000, unicode=0x596A, note="奪：自动生成")
    g.hbar(220.6, 725.3, 670.6, weight=48.0)
    g.diag(413.5, 797.0, 358.1, 667.7, weight=56.0)
    g.diag(358.1, 667.7, 85.6, 356.0, weight=56.0)
    g.diag(524.7, 657.3, 607.7, 598.1, weight=48.0)
    g.diag(607.7, 598.1, 914.4, 436.8, weight=48.0)
    g.diag(390.7, 552.7, 406.1, 517.8, weight=48.0)
    g.diag(406.1, 517.8, 290.0, 395.6, weight=48.0)
    g.diag(290.0, 395.6, 220.6, 348.4, weight=48.0)
    g.vbar(331.3, 216.2, 406.3, weight=48.0)
    g.dot(482.4, 562.2, w=76.0, h=73.5, slant=-14.0)
    g.hbar(393.5, 598.9, 484.3, weight=48.0)
    g.hbar(402.1, 603.6, 410.1, weight=48.0)
    g.hbar(398.3, 606.5, 344.1, weight=48.0)
    g.diag(470.5, 456.7, 493.0, 438.4, weight=76.0)
    g.vbar(489.8, 298.7, 438.4, weight=76.0)
    g.diag(486.6, 298.7, 476.2, 289.4, weight=76.0)
    g.diag(362.2, 253.3, 366.0, 247.6, weight=56.0)
    g.hbar(366.0, 651.1, 261.9, weight=56.0)
    g.hbar(125.5, 817.5, 147.3, weight=84.0)
    g.diag(516.2, 236.2, 565.1, 175.0, weight=96.0)
    g.diag(565.1, 175.0, 526.0, -67.4, weight=96.0)
    g.hbar(439.2, 526.0, -53.4, weight=96.0)
    g.dot(362.2, 59.9, w=96.0, h=108.3, slant=-14.0)
    return g
def g_cjk_unified_ideograph_596e() -> Glyph:
    """奮 U+596E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni596E", advance=1000, unicode=0x596E, note="奮：自动生成")
    g.hbar(221.1, 703.5, 684.7, weight=48.0)
    g.diag(404.5, 807.0, 352.3, 677.1, weight=56.0)
    g.diag(352.3, 677.1, 91.1, 374.3, weight=56.0)
    g.diag(533.5, 676.3, 908.9, 464.1, weight=48.0)
    g.hbar(386.5, 405.9, 532.2, weight=48.0)
    g.diag(386.5, 535.4, 227.8, 366.6, weight=48.0)
    g.vbar(338.4, 207.4, 439.7, weight=48.0)
    g.diag(433.7, 661.3, 525.0, 544.1, weight=48.0)
    g.hbar(400.7, 465.4, 516.0, weight=48.0)
    g.hbar(465.4, 628.7, 534.6, weight=48.0)
    g.diag(421.2, 372.9, 561.1, 452.6, weight=48.0)
    g.diag(561.1, 452.6, 591.8, 404.8, weight=48.0)
    g.diag(416.1, 401.9, 469.8, 360.4, weight=48.0)
    g.hbar(469.8, 590.2, 374.0, weight=48.0)
    g.diag(590.2, 387.5, 599.6, 430.8, weight=48.0)
    g.diag(478.0, 492.7, 501.9, 472.7, weight=96.0)
    g.vbar(500.0, 326.5, 472.7, weight=96.0)
    g.diag(498.1, 326.5, 483.8, 306.4, weight=96.0)
    g.hbar(357.8, 620.0, 289.6, weight=56.0)
    g.diag(620.0, 304.7, 661.4, 248.2, weight=56.0)
    g.vbar(270.4, 192.7, 200.8, weight=48.0)
    g.vbar(290.7, 8.6, 192.7, weight=48.0)
    g.diag(312.3, 8.6, 339.7, -25.7, weight=48.0)
    g.hbar(284.0, 585.0, 166.5, weight=48.0)
    g.diag(585.0, 138.2, 634.5, -19.0, weight=48.0)
    g.diag(634.5, -19.0, 581.2, 23.0, weight=48.0)
    g.hbar(322.7, 539.1, 97.4, weight=64.0)
    g.diag(539.1, 112.2, 583.2, 53.0, weight=64.0)
    g.diag(437.9, 187.0, 466.6, 158.4, weight=96.0)
    g.vbar(466.6, 42.8, 158.4, weight=96.0)
    g.diag(466.6, 42.8, 453.2, 22.7, weight=96.0)
    g.hbar(333.7, 582.0, -3.3, weight=48.0)
    return g
def g_cjk_unified_ideograph_59eb() -> Glyph:
    """姫 U+59EB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni59EB", advance=1000, unicode=0x59EB, note="姫：自动生成")
    g.vbar(259.4, 556.3, 700.4, weight=48.0)
    g.diag(266.3, 556.3, 208.0, 212.9, weight=48.0)
    g.diag(208.0, 212.9, 398.7, 55.5, weight=48.0)
    g.diag(345.5, 417.1, 314.5, 282.1, weight=48.0)
    g.diag(314.5, 282.1, 128.8, 16.3, weight=48.0)
    g.hbar(63.0, 107.2, 340.8, weight=96.0)
    g.hbar(107.2, 333.6, 360.5, weight=96.0)
    g.diag(333.6, 389.5, 338.8, 399.1, weight=96.0)
    g.hbar(540.2, 843.3, 615.8, weight=96.0)
    g.diag(670.6, 579.7, 698.4, 551.8, weight=96.0)
    g.diag(698.4, 551.8, 668.6, 431.5, weight=96.0)
    g.hbar(526.1, 799.3, 411.4, weight=48.0)
    g.diag(799.3, 437.4, 839.3, 400.1, weight=48.0)
    g.diag(839.3, 400.1, 780.4, 284.1, weight=48.0)
    g.hbar(522.0, 816.4, 255.9, weight=48.0)
    g.vbar(670.2, 45.3, 228.5, weight=48.0)
    g.diag(473.3, 624.8, 603.1, 186.6, weight=48.0)
    g.diag(603.1, 186.6, 912.0, 32.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_5a18() -> Glyph:
    """娘 U+5A18 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5A18", advance=1000, unicode=0x5A18, note="娘：自动生成")
    g.vbar(278.2, 521.2, 665.7, weight=48.0)
    g.diag(282.9, 521.2, 224.6, 195.1, weight=48.0)
    g.diag(224.6, 195.1, 412.2, 38.1, weight=48.0)
    g.diag(364.3, 395.7, 337.0, 280.2, weight=48.0)
    g.diag(337.0, 280.2, 145.3, -20.3, weight=48.0)
    g.hbar(63.0, 111.6, 305.9, weight=96.0)
    g.hbar(111.6, 361.5, 336.5, weight=96.0)
    g.diag(554.7, 740.3, 643.3, 676.5, weight=64.0)
    g.diag(643.3, 676.5, 663.9, 609.2, weight=64.0)
    g.hbar(519.3, 715.9, 564.3, weight=48.0)
    g.diag(715.9, 591.0, 752.5, 557.1, weight=48.0)
    g.diag(752.5, 557.1, 709.1, 348.9, weight=48.0)
    g.hbar(689.4, 709.1, 349.8, weight=48.0)
    g.diag(531.8, 438.0, 546.6, 454.3, weight=84.0)
    g.hbar(546.6, 697.7, 459.5, weight=84.0)
    g.dot(606.4, 351.4, w=96.0, h=124.8, slant=-14.0)
    g.diag(464.8, 584.3, 491.0, 415.5, weight=48.0)
    g.vbar(487.4, -24.9, 415.5, weight=48.0)
    g.diag(483.7, -24.9, 697.0, 107.9, weight=48.0)
    g.diag(752.4, 360.6, 810.0, 316.3, weight=96.0)
    g.diag(810.0, 316.3, 684.3, 201.9, weight=96.0)
    g.hbar(672.4, 684.3, 201.3, weight=96.0)
    g.diag(533.7, 336.6, 947.0, 32.3, weight=48.0)
    return g
def g_cjk_unified_ideograph_5a20() -> Glyph:
    """娠 U+5A20 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5A20", advance=1000, unicode=0x5A20, note="娠：自动生成")
    g.vbar(247.6, 560.5, 717.0, weight=48.0)
    g.diag(249.2, 560.5, 195.7, 276.8, weight=48.0)
    g.diag(195.7, 276.8, 367.4, 134.2, weight=48.0)
    g.diag(334.9, 475.0, 304.0, 339.8, weight=48.0)
    g.diag(304.0, 339.8, 102.0, 58.0, weight=48.0)
    g.hbar(58.0, 109.6, 389.9, weight=96.0)
    g.hbar(109.6, 332.0, 418.4, weight=96.0)
    g.hbar(526.0, 746.6, 606.6, weight=96.0)
    g.diag(746.6, 624.1, 766.0, 531.5, weight=96.0)
    g.diag(507.9, 595.3, 451.4, 408.6, weight=48.0)
    g.diag(451.4, 408.6, 282.0, -17.0, weight=48.0)
    g.hbar(516.0, 710.4, 477.4, weight=84.0)
    g.diag(710.4, 487.1, 763.3, 428.8, weight=84.0)
    g.hbar(490.0, 792.9, 365.5, weight=84.0)
    g.vbar(793.8, 368.8, 401.1, weight=84.0)
    g.diag(509.0, 309.0, 543.7, 288.7, weight=64.0)
    g.vbar(535.8, 14.5, 288.7, weight=64.0)
    g.diag(527.9, 14.5, 644.8, 86.2, weight=64.0)
    g.diag(644.8, 86.2, 712.7, 151.5, weight=64.0)
    g.diag(768.5, 356.8, 782.0, 315.0, weight=96.0)
    g.diag(782.0, 315.0, 705.0, 250.0, weight=96.0)
    g.vbar(705.0, 241.0, 250.0, weight=96.0)
    g.diag(586.4, 330.6, 592.7, 327.6, weight=56.0)
    g.diag(592.7, 327.6, 802.8, 97.3, weight=56.0)
    g.hbar(802.8, 937.0, 83.6, weight=56.0)
    return g
def g_cjk_unified_ideograph_5a46() -> Glyph:
    """婆 U+5A46 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5A46", advance=1000, unicode=0x5A46, note="婆：自动生成")
    g.diag(198.3, 617.5, 291.5, 683.7, weight=96.0)
    g.diag(291.5, 683.7, 357.5, 647.4, weight=96.0)
    g.diag(228.1, 672.7, 245.9, 544.7, weight=96.0)
    g.diag(245.9, 544.7, 283.6, 513.5, weight=96.0)
    g.diag(287.7, 303.0, 227.9, 340.7, weight=64.0)
    g.diag(227.9, 340.7, 280.7, 520.7, weight=64.0)
    g.diag(450.9, 604.5, 471.8, 625.4, weight=96.0)
    g.hbar(471.8, 742.2, 645.7, weight=96.0)
    g.diag(742.2, 665.9, 661.7, 558.4, weight=96.0)
    g.hbar(426.4, 437.5, 624.5, weight=76.0)
    g.vbar(390.1, 325.8, 626.3, weight=76.0)
    g.hbar(264.9, 342.7, 314.1, weight=76.0)
    g.diag(528.7, 782.0, 569.9, 744.9, weight=48.0)
    g.diag(569.9, 744.9, 541.0, 539.0, weight=48.0)
    g.hbar(472.9, 567.0, 479.3, weight=48.0)
    g.diag(567.0, 468.8, 432.7, 328.9, weight=48.0)
    g.diag(474.0, 487.1, 821.7, 265.3, weight=64.0)
    g.diag(422.3, 320.8, 436.2, 278.9, weight=96.0)
    g.diag(436.2, 278.9, 347.1, 126.9, weight=96.0)
    g.diag(347.1, 126.9, 695.7, -57.0, weight=96.0)
    g.diag(564.0, 243.7, 516.6, 164.8, weight=48.0)
    g.diag(516.6, 164.8, 271.5, -11.4, weight=48.0)
    g.hbar(112.0, 878.0, 205.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_5a7f() -> Glyph:
    """婿 U+5A7F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5A7F", advance=1000, unicode=0x5A7F, note="婿：自动生成")
    g.vbar(240.8, 575.4, 745.6, weight=48.0)
    g.diag(239.8, 575.4, 177.2, 279.0, weight=48.0)
    g.diag(177.2, 279.0, 368.3, 132.6, weight=48.0)
    g.diag(316.4, 463.4, 292.2, 354.6, weight=48.0)
    g.diag(292.2, 354.6, 106.1, 81.7, weight=48.0)
    g.hbar(58.0, 106.1, 392.4, weight=96.0)
    g.hbar(106.1, 304.2, 409.4, weight=96.0)
    g.diag(304.2, 435.4, 311.7, 444.8, weight=96.0)
    g.hbar(442.8, 758.3, 693.8, weight=56.0)
    g.diag(758.3, 717.5, 697.4, 588.8, weight=56.0)
    g.diag(577.7, 670.2, 605.0, 646.6, weight=96.0)
    g.vbar(603.1, 492.9, 646.6, weight=96.0)
    g.diag(601.2, 492.9, 615.4, 470.2, weight=96.0)
    g.hbar(628.6, 691.5, 559.5, weight=84.0)
    g.diag(691.5, 567.5, 715.9, 607.2, weight=84.0)
    g.diag(463.5, 579.7, 499.8, 539.4, weight=48.0)
    g.diag(499.8, 539.4, 353.0, 368.0, weight=48.0)
    g.diag(505.0, 512.7, 554.8, 472.3, weight=96.0)
    g.hbar(554.8, 937.0, 432.6, weight=96.0)
    g.vbar(462.6, -29.6, 330.6, weight=96.0)
    g.hbar(500.2, 660.3, 332.7, weight=48.0)
    g.vbar(672.6, 208.6, 353.6, weight=48.0)
    g.vbar(677.7, -40.7, 208.6, weight=48.0)
    g.hbar(590.9, 670.6, -23.8, weight=48.0)
    g.hbar(506.0, 672.2, 228.6, weight=64.0)
    g.diag(499.4, 126.9, 514.5, 140.7, weight=76.0)
    g.hbar(514.5, 669.9, 142.1, weight=76.0)
    return g
def g_cjk_unified_ideograph_5a92() -> Glyph:
    """媒 U+5A92 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5A92", advance=1000, unicode=0x5A92, note="媒：自动生成")
    g.vbar(255.2, 570.3, 743.6, weight=48.0)
    g.vbar(265.9, 298.4, 570.3, weight=48.0)
    g.diag(276.0, 298.4, 416.7, 79.0, weight=48.0)
    g.diag(332.5, 448.9, 304.6, 345.4, weight=48.0)
    g.diag(304.6, 345.4, 119.4, 58.4, weight=48.0)
    g.hbar(72.1, 116.6, 368.9, weight=96.0)
    g.hbar(116.6, 319.8, 389.2, weight=96.0)
    g.diag(319.8, 418.5, 330.2, 429.9, weight=96.0)
    g.hbar(438.4, 481.4, 574.9, weight=84.0)
    g.hbar(438.4, 844.3, 594.5, weight=84.0)
    g.diag(478.1, 612.2, 503.7, 665.7, weight=96.0)
    g.vbar(516.6, 351.4, 665.7, weight=96.0)
    g.diag(662.8, 772.0, 710.4, 730.2, weight=76.0)
    g.vbar(691.1, 363.0, 730.2, weight=76.0)
    g.diag(547.6, 472.3, 558.3, 487.3, weight=64.0)
    g.hbar(558.3, 665.2, 487.3, weight=64.0)
    g.hbar(547.5, 639.9, 386.5, weight=84.0)
    g.diag(639.9, 397.9, 652.4, 386.4, weight=84.0)
    g.hbar(344.6, 877.4, 263.3, weight=48.0)
    g.diag(565.3, 337.3, 617.4, 289.0, weight=96.0)
    g.vbar(611.3, -72.0, 289.0, weight=96.0)
    g.diag(576.3, 239.1, 343.4, 11.2, weight=48.0)
    g.diag(631.0, 245.5, 799.4, 54.7, weight=48.0)
    g.hbar(799.4, 937.9, 41.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_5a9b() -> Glyph:
    """媛 U+5A9B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5A9B", advance=1000, unicode=0x5A9B, note="媛：自动生成")
    g.vbar(245.0, 570.0, 710.1, weight=48.0)
    g.diag(249.7, 570.0, 192.2, 245.0, weight=48.0)
    g.diag(192.2, 245.0, 384.0, 102.9, weight=48.0)
    g.diag(321.0, 428.9, 298.7, 330.9, weight=48.0)
    g.diag(298.7, 330.9, 120.5, 64.1, weight=48.0)
    g.hbar(63.0, 107.5, 359.6, weight=96.0)
    g.hbar(107.5, 317.0, 380.2, weight=96.0)
    g.diag(758.3, 711.1, 690.1, 747.9, weight=96.0)
    g.diag(690.1, 747.9, 460.9, 630.5, weight=96.0)
    g.dot(481.6, 557.6, w=92.0, h=119.6, slant=-14.0)
    g.diag(564.4, 644.1, 607.3, 583.6, weight=96.0)
    g.hbar(607.3, 656.2, 574.5, weight=96.0)
    g.diag(764.0, 699.4, 787.6, 645.6, weight=96.0)
    g.diag(787.6, 645.6, 696.8, 571.5, weight=96.0)
    g.vbar(699.4, 536.4, 571.5, weight=96.0)
    g.diag(493.5, 449.7, 484.5, 453.8, weight=92.0)
    g.hbar(484.5, 719.4, 476.0, weight=92.0)
    g.vbar(719.8, 498.2, 539.9, weight=92.0)
    g.hbar(378.8, 847.9, 356.5, weight=92.0)
    g.diag(526.2, 439.0, 485.8, 301.7, weight=48.0)
    g.diag(485.8, 301.7, 271.9, -29.8, weight=48.0)
    g.diag(517.8, 258.4, 612.6, 177.7, weight=48.0)
    g.diag(612.6, 177.7, 433.9, -12.5, weight=48.0)
    g.diag(505.7, 186.5, 937.0, -36.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_5ac1() -> Glyph:
    """嫁 U+5AC1 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5AC1", advance=1000, unicode=0x5AC1, note="嫁：自动生成")
    g.vbar(254.9, 556.3, 687.0, weight=48.0)
    g.diag(259.9, 556.3, 206.7, 261.4, weight=48.0)
    g.diag(206.7, 261.4, 395.4, 71.7, weight=48.0)
    g.diag(334.7, 432.1, 307.9, 317.3, weight=48.0)
    g.diag(307.9, 317.3, 133.5, 61.7, weight=48.0)
    g.hbar(58.0, 103.2, 355.5, weight=96.0)
    g.hbar(103.2, 332.9, 379.3, weight=96.0)
    g.diag(558.4, 741.0, 631.1, 701.9, weight=48.0)
    g.diag(631.1, 701.9, 661.2, 633.9, weight=48.0)
    g.diag(459.6, 596.4, 449.2, 589.9, weight=48.0)
    g.vbar(433.5, 503.3, 589.9, weight=48.0)
    g.diag(417.8, 503.3, 446.1, 474.0, weight=48.0)
    g.hbar(474.5, 477.6, 583.8, weight=92.0)
    g.hbar(477.6, 805.7, 599.7, weight=92.0)
    g.diag(805.7, 616.3, 730.5, 522.5, weight=92.0)
    g.hbar(433.4, 721.9, 496.6, weight=48.0)
    g.diag(564.5, 457.6, 436.4, 313.7, weight=48.0)
    g.hbar(365.5, 436.4, 314.0, weight=48.0)
    g.diag(524.0, 363.5, 582.7, 116.6, weight=48.0)
    g.hbar(479.1, 582.7, 97.8, weight=48.0)
    g.vbar(542.7, 305.1, 342.2, weight=48.0)
    g.diag(543.8, 305.1, 411.2, 199.6, weight=48.0)
    g.vbar(604.9, 238.6, 287.2, weight=48.0)
    g.diag(602.7, 238.6, 475.0, 97.1, weight=48.0)
    g.hbar(378.5, 475.0, 96.3, weight=48.0)
    g.diag(708.7, 483.0, 746.5, 413.2, weight=48.0)
    g.diag(746.5, 413.2, 636.7, 311.6, weight=48.0)
    g.vbar(658.1, 262.4, 288.1, weight=96.0)
    g.hbar(656.3, 947.0, 199.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_5ac9() -> Glyph:
    """嫉 U+5AC9 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5AC9", advance=1000, unicode=0x5AC9, note="嫉：自动生成")
    g.vbar(225.4, 588.2, 733.9, weight=48.0)
    g.diag(230.4, 588.2, 175.4, 251.8, weight=48.0)
    g.diag(175.4, 251.8, 371.0, 76.8, weight=48.0)
    g.diag(289.3, 435.8, 273.2, 333.0, weight=48.0)
    g.diag(273.2, 333.0, 116.3, 62.7, weight=48.0)
    g.hbar(53.0, 96.1, 364.1, weight=96.0)
    g.hbar(96.1, 284.6, 386.4, weight=96.0)
    g.diag(568.3, 734.9, 648.6, 693.3, weight=76.0)
    g.diag(648.6, 693.3, 690.7, 598.0, weight=76.0)
    g.hbar(513.4, 811.7, 569.1, weight=96.0)
    g.diag(811.7, 589.6, 822.6, 581.7, weight=96.0)
    g.diag(488.4, 554.1, 298.8, -14.9, weight=64.0)
    g.dot(400.6, 424.4, w=96.0, h=108.0, slant=-14.0)
    g.hbar(310.1, 380.1, 246.9, weight=48.0)
    g.diag(380.1, 242.3, 462.2, 297.0, weight=48.0)
    g.diag(603.2, 528.8, 632.0, 456.5, weight=48.0)
    g.diag(632.0, 456.5, 579.7, 352.5, weight=48.0)
    g.diag(579.7, 352.5, 505.2, 318.3, weight=48.0)
    g.hbar(600.4, 765.4, 372.5, weight=96.0)
    g.diag(765.4, 393.9, 792.5, 297.7, weight=96.0)
    g.hbar(499.6, 868.0, 226.6, weight=96.0)
    g.vbar(623.3, 221.8, 337.8, weight=48.0)
    g.diag(617.0, 221.8, 472.8, 7.8, weight=48.0)
    g.diag(669.0, 198.3, 937.0, 9.7, weight=48.0)
    return g
def g_cjk_unified_ideograph_5acc() -> Glyph:
    """嫌 U+5ACC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5ACC", advance=1000, unicode=0x5ACC, note="嫌：自动生成")
    g.vbar(235.8, 581.6, 732.2, weight=48.0)
    g.diag(239.8, 581.6, 179.0, 238.4, weight=48.0)
    g.diag(179.0, 238.4, 367.5, 86.2, weight=48.0)
    g.diag(306.8, 448.3, 283.4, 313.3, weight=48.0)
    g.diag(283.4, 313.3, 105.8, 42.5, weight=48.0)
    g.hbar(59.2, 108.2, 368.8, weight=96.0)
    g.hbar(108.2, 302.7, 394.5, weight=96.0)
    g.diag(446.2, 738.9, 497.6, 694.3, weight=96.0)
    g.diag(497.6, 694.3, 520.9, 618.5, weight=96.0)
    g.diag(683.9, 802.0, 711.5, 768.9, weight=96.0)
    g.diag(711.5, 768.9, 614.0, 637.2, weight=96.0)
    g.diag(456.1, 566.2, 459.5, 568.9, weight=96.0)
    g.hbar(459.5, 717.6, 596.0, weight=96.0)
    g.diag(717.6, 623.1, 743.0, 540.2, weight=96.0)
    g.hbar(424.9, 773.3, 472.1, weight=48.0)
    g.vbar(743.3, 309.5, 492.4, weight=48.0)
    g.hbar(347.1, 902.2, 371.1, weight=48.0)
    g.hbar(419.1, 747.5, 272.0, weight=48.0)
    g.vbar(744.1, 293.0, 315.3, weight=48.0)
    g.vbar(498.0, 389.1, 555.2, weight=48.0)
    g.vbar(502.0, -38.0, 389.1, weight=48.0)
    g.diag(603.4, 571.1, 625.1, 549.4, weight=84.0)
    g.vbar(626.4, -72.0, 549.4, weight=84.0)
    g.diag(495.5, 234.5, 316.3, 15.3, weight=48.0)
    g.diag(645.8, 238.4, 945.8, 25.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_5ae1() -> Glyph:
    """嫡 U+5AE1 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5AE1", advance=1000, unicode=0x5AE1, note="嫡：自动生成")
    g.vbar(283.7, 557.3, 717.2, weight=48.0)
    g.diag(288.5, 557.3, 228.6, 216.2, weight=48.0)
    g.diag(228.6, 216.2, 419.0, 41.2, weight=48.0)
    g.diag(378.7, 432.5, 356.6, 308.5, weight=48.0)
    g.diag(356.6, 308.5, 151.6, 2.4, weight=48.0)
    g.hbar(65.4, 117.3, 335.6, weight=96.0)
    g.hbar(117.3, 365.9, 364.8, weight=96.0)
    g.diag(365.9, 403.7, 372.6, 414.3, weight=96.0)
    g.diag(631.4, 797.0, 723.0, 743.1, weight=56.0)
    g.diag(723.0, 743.1, 756.0, 657.8, weight=56.0)
    g.diag(557.9, 562.2, 528.1, 605.9, weight=96.0)
    g.hbar(528.1, 924.6, 629.8, weight=96.0)
    g.diag(585.0, 535.0, 641.3, 422.9, weight=48.0)
    g.diag(754.4, 615.5, 780.2, 577.1, weight=48.0)
    g.diag(780.2, 577.1, 724.1, 438.0, weight=48.0)
    g.vbar(510.4, -53.7, 404.0, weight=48.0)
    g.diag(527.3, 391.9, 834.7, 247.2, weight=48.0)
    g.diag(834.7, 247.2, 890.2, -68.8, weight=48.0)
    g.diag(890.2, -68.8, 792.0, -17.0, weight=48.0)
    g.hbar(561.6, 878.4, 300.4, weight=96.0)
    g.diag(673.8, 390.7, 704.7, 348.5, weight=48.0)
    g.diag(704.7, 348.5, 687.5, 208.3, weight=48.0)
    g.diag(687.5, 208.3, 675.6, 197.4, weight=48.0)
    g.hbar(607.3, 619.4, 169.4, weight=48.0)
    g.vbar(624.3, 35.8, 167.6, weight=48.0)
    g.hbar(629.8, 812.9, 174.3, weight=48.0)
    g.diag(812.9, 188.3, 753.2, 96.0, weight=48.0)
    g.hbar(645.6, 783.7, 66.4, weight=48.0)
    g.vbar(784.6, 80.3, 100.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_5b6b() -> Glyph:
    """孫 U+5B6B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5B6B", advance=1000, unicode=0x5B6B, note="孫：自动生成")
    g.hbar(163.4, 442.8, 689.0, weight=96.0)
    g.diag(442.8, 711.8, 328.2, 534.3, weight=96.0)
    g.hbar(318.5, 328.2, 534.3, weight=96.0)
    g.vbar(281.7, 205.9, 524.3, weight=96.0)
    g.hbar(165.4, 282.0, 192.3, weight=96.0)
    g.hbar(87.4, 143.8, 215.2, weight=96.0)
    g.diag(143.8, 214.8, 511.4, 476.0, weight=96.0)
    g.hbar(772.5, 836.5, 768.3, weight=96.0)
    g.hbar(561.4, 772.5, 730.5, weight=96.0)
    g.hbar(463.1, 561.4, 683.9, weight=96.0)
    g.diag(636.3, 691.5, 661.5, 664.8, weight=48.0)
    g.diag(661.5, 664.8, 538.9, 479.9, weight=48.0)
    g.hbar(538.9, 703.9, 487.8, weight=48.0)
    g.diag(763.7, 596.6, 706.7, 489.8, weight=48.0)
    g.diag(706.7, 489.8, 539.6, 299.2, weight=48.0)
    g.hbar(539.6, 806.2, 334.0, weight=48.0)
    g.hbar(786.0, 843.9, 369.0, weight=48.0)
    g.diag(843.9, 365.5, 864.0, 327.5, weight=48.0)
    g.diag(636.5, 298.0, 672.8, 160.4, weight=48.0)
    g.vbar(668.5, -49.5, 160.4, weight=48.0)
    g.diag(664.3, -49.5, 557.0, 14.2, weight=48.0)
    g.diag(553.6, 278.5, 495.8, 110.2, weight=96.0)
    g.diag(495.8, 110.2, 520.0, 24.5, weight=96.0)
    g.diag(725.4, 214.5, 904.9, 124.0, weight=96.0)
    g.diag(904.9, 124.0, 932.6, 54.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_5bb0() -> Glyph:
    """宰 U+5BB0 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5BB0", advance=1000, unicode=0x5BB0, note="宰：自动生成")
    g.diag(434.1, 797.0, 514.2, 739.0, weight=48.0)
    g.diag(514.2, 739.0, 530.6, 677.9, weight=48.0)
    g.diag(242.3, 640.2, 203.9, 539.2, weight=96.0)
    g.diag(203.9, 539.2, 269.9, 496.0, weight=96.0)
    g.hbar(253.8, 803.5, 643.6, weight=48.0)
    g.diag(803.5, 673.1, 689.7, 547.6, weight=48.0)
    g.diag(453.5, 627.2, 526.1, 543.6, weight=48.0)
    g.vbar(340.9, 471.1, 494.7, weight=96.0)
    g.hbar(345.4, 677.7, 515.4, weight=96.0)
    g.dot(387.1, 409.8, w=96.0, h=108.6, slant=-14.0)
    g.diag(568.8, 508.7, 592.8, 476.7, weight=96.0)
    g.diag(592.8, 476.7, 525.1, 358.8, weight=96.0)
    g.hbar(160.9, 839.1, 321.4, weight=96.0)
    g.diag(237.1, 259.4, 292.5, 165.8, weight=96.0)
    g.hbar(292.5, 755.6, 177.0, weight=96.0)
    g.diag(512.8, 311.4, 492.9, 290.5, weight=96.0)
    g.vbar(491.9, -67.0, 290.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_5bb4() -> Glyph:
    """宴 U+5BB4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5BB4", advance=1000, unicode=0x5BB4, note="宴：自动生成")
    g.diag(457.0, 792.0, 524.1, 752.3, weight=48.0)
    g.diag(524.1, 752.3, 548.6, 679.1, weight=48.0)
    g.vbar(241.1, 533.9, 651.7, weight=96.0)
    g.hbar(219.6, 281.6, 520.7, weight=96.0)
    g.hbar(288.8, 436.6, 630.3, weight=64.0)
    g.hbar(436.6, 809.6, 651.7, weight=64.0)
    g.diag(809.6, 669.5, 662.9, 529.9, weight=64.0)
    g.vbar(339.9, 509.9, 520.2, weight=48.0)
    g.vbar(361.3, 333.0, 509.9, weight=48.0)
    g.hbar(353.3, 651.7, 527.7, weight=48.0)
    g.vbar(623.8, 361.8, 540.2, weight=48.0)
    g.hbar(573.0, 596.0, 363.7, weight=48.0)
    g.hbar(384.4, 501.6, 437.9, weight=56.0)
    g.diag(501.6, 452.4, 551.7, 400.0, weight=56.0)
    g.diag(397.4, 345.8, 405.7, 354.1, weight=64.0)
    g.hbar(405.7, 573.1, 364.3, weight=64.0)
    g.diag(417.3, 337.2, 445.3, 300.9, weight=96.0)
    g.diag(445.3, 300.9, 373.9, 150.4, weight=96.0)
    g.diag(373.9, 150.4, 721.7, -57.0, weight=96.0)
    g.diag(554.8, 264.1, 503.0, 169.0, weight=48.0)
    g.diag(503.0, 169.0, 251.8, -16.3, weight=48.0)
    g.hbar(129.9, 870.1, 226.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_5bb5() -> Glyph:
    """宵 U+5BB5 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5BB5", advance=1000, unicode=0x5BB5, note="宵：自动生成")
    g.diag(452.1, 797.0, 519.3, 759.4, weight=48.0)
    g.diag(519.3, 759.4, 553.2, 677.5, weight=48.0)
    g.vbar(217.0, 522.5, 651.5, weight=96.0)
    g.hbar(195.4, 270.7, 509.8, weight=96.0)
    g.hbar(268.2, 851.7, 650.3, weight=96.0)
    g.diag(851.7, 673.6, 712.7, 560.9, weight=96.0)
    g.diag(464.3, 626.2, 512.9, 542.8, weight=48.0)
    g.diag(512.9, 542.8, 484.0, 371.6, weight=48.0)
    g.diag(241.6, 544.1, 368.1, 473.8, weight=76.0)
    g.diag(368.1, 473.8, 387.9, 380.6, weight=76.0)
    g.diag(712.4, 570.3, 525.0, 461.9, weight=56.0)
    g.diag(367.2, 354.8, 349.1, 258.7, weight=48.0)
    g.vbar(332.9, -52.0, 258.7, weight=48.0)
    g.hbar(369.6, 620.8, 363.0, weight=48.0)
    g.vbar(633.9, 224.7, 382.4, weight=48.0)
    g.diag(647.1, 224.7, 503.8, 15.9, weight=48.0)
    g.hbar(503.8, 525.2, 11.1, weight=48.0)
    g.diag(379.9, 219.8, 398.7, 235.7, weight=84.0)
    g.hbar(398.7, 625.3, 242.4, weight=84.0)
    g.hbar(375.0, 629.6, 130.0, weight=84.0)
    return g
def g_cjk_unified_ideograph_5bc2() -> Glyph:
    """寂 U+5BC2 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5BC2", advance=1000, unicode=0x5BC2, note="寂：自动生成")
    g.diag(430.8, 778.4, 515.0, 724.3, weight=56.0)
    g.diag(515.0, 724.3, 541.7, 640.3, weight=56.0)
    g.diag(227.3, 592.6, 225.0, 590.5, weight=96.0)
    g.diag(225.0, 590.5, 169.3, 437.7, weight=96.0)
    g.hbar(247.4, 771.9, 591.1, weight=96.0)
    g.diag(771.9, 622.3, 689.4, 511.8, weight=96.0)
    g.vbar(683.4, 404.9, 511.8, weight=96.0)
    g.diag(295.8, 539.4, 340.6, 459.7, weight=96.0)
    g.vbar(339.6, 308.4, 459.7, weight=96.0)
    g.diag(338.6, 308.4, 322.6, 296.3, weight=96.0)
    g.hbar(373.1, 452.4, 392.4, weight=84.0)
    g.diag(452.4, 409.3, 506.4, 372.2, weight=84.0)
    g.hbar(53.0, 471.9, 254.7, weight=96.0)
    g.diag(304.6, 240.2, 383.3, -71.0, weight=92.0)
    g.diag(383.3, -71.0, 170.1, 33.1, weight=92.0)
    g.vbar(198.7, 13.0, 199.9, weight=96.0)
    g.diag(374.1, 191.7, 457.9, 143.0, weight=96.0)
    g.diag(457.9, 143.0, 488.0, 61.5, weight=96.0)
    g.hbar(514.9, 787.2, 349.3, weight=96.0)
    g.diag(787.2, 380.5, 548.4, 20.3, weight=96.0)
    g.diag(548.4, 20.3, 478.5, 61.5, weight=96.0)
    g.diag(504.0, 281.3, 947.0, -11.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_5bd2() -> Glyph:
    """寒 U+5BD2 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5BD2", advance=1000, unicode=0x5BD2, note="寒：自动生成")
    g.diag(421.0, 792.0, 484.4, 757.9, weight=48.0)
    g.diag(484.4, 757.9, 517.5, 683.3, weight=48.0)
    g.diag(229.1, 642.6, 176.7, 544.0, weight=96.0)
    g.diag(176.7, 544.0, 241.3, 490.1, weight=96.0)
    g.hbar(250.4, 769.6, 646.4, weight=96.0)
    g.diag(769.6, 682.1, 660.7, 557.7, weight=96.0)
    g.hbar(349.0, 416.3, 493.9, weight=84.0)
    g.hbar(416.3, 655.9, 524.1, weight=84.0)
    g.hbar(334.4, 355.7, 378.5, weight=76.0)
    g.hbar(334.4, 590.8, 394.6, weight=76.0)
    g.hbar(567.1, 590.8, 412.3, weight=76.0)
    g.diag(344.0, 593.8, 381.0, 539.4, weight=96.0)
    g.vbar(384.4, 326.8, 539.4, weight=96.0)
    g.diag(387.9, 326.8, 375.2, 308.3, weight=96.0)
    g.diag(514.8, 625.0, 550.7, 582.3, weight=96.0)
    g.vbar(541.0, 347.3, 582.3, weight=96.0)
    g.diag(531.2, 347.3, 515.6, 326.8, weight=96.0)
    g.hbar(191.8, 749.6, 288.8, weight=48.0)
    g.diag(351.4, 264.2, 291.0, 192.1, weight=48.0)
    g.diag(291.0, 192.1, 70.5, -12.1, weight=48.0)
    g.diag(70.5, -12.1, 97.3, 23.6, weight=48.0)
    g.diag(529.3, 286.9, 902.7, 98.7, weight=48.0)
    g.diag(383.7, 225.9, 486.3, 160.1, weight=96.0)
    g.diag(486.3, 160.1, 450.5, 79.0, weight=96.0)
    g.diag(468.4, 112.5, 524.4, -72.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_5bdf() -> Glyph:
    """察 U+5BDF —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5BDF", advance=1000, unicode=0x5BDF, note="察：自动生成")
    g.diag(419.5, 798.4, 500.0, 757.1, weight=48.0)
    g.diag(500.0, 757.1, 523.7, 697.4, weight=48.0)
    g.hbar(236.2, 248.0, 656.2, weight=64.0)
    g.diag(236.2, 656.4, 188.3, 572.8, weight=64.0)
    g.diag(188.3, 572.8, 221.8, 485.6, weight=64.0)
    g.hbar(261.3, 777.1, 660.1, weight=84.0)
    g.diag(777.1, 685.8, 672.9, 588.4, weight=84.0)
    g.diag(295.2, 621.2, 317.5, 560.8, weight=48.0)
    g.diag(317.5, 560.8, 189.8, 395.2, weight=48.0)
    g.vbar(296.3, 385.4, 500.7, weight=48.0)
    g.diag(295.7, 385.4, 58.0, 134.9, weight=48.0)
    g.dot(289.6, 416.9, w=76.0, h=92.6, slant=-14.0)
    g.dot(223.3, 355.0, w=76.0, h=98.8, slant=-14.0)
    g.diag(493.3, 500.6, 516.6, 552.3, weight=48.0)
    g.hbar(516.6, 681.7, 556.4, weight=48.0)
    g.diag(681.7, 560.5, 583.9, 447.5, weight=48.0)
    g.diag(502.8, 528.4, 622.3, 405.2, weight=48.0)
    g.diag(622.3, 405.2, 942.0, 214.4, weight=48.0)
    g.hbar(337.5, 411.9, 305.1, weight=64.0)
    g.hbar(411.9, 604.9, 326.6, weight=64.0)
    g.hbar(245.6, 405.3, 216.7, weight=64.0)
    g.hbar(405.3, 714.5, 234.6, weight=64.0)
    g.diag(447.6, 184.2, 581.5, -72.0, weight=96.0)
    g.hbar(304.8, 581.5, -23.5, weight=96.0)
    g.diag(302.6, 144.2, 228.2, -27.2, weight=96.0)
    g.diag(608.7, 188.1, 739.6, -16.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_5be7() -> Glyph:
    """寧 U+5BE7 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5BE7", advance=1000, unicode=0x5BE7, note="寧：自动生成")
    g.diag(412.2, 787.0, 521.6, 718.9, weight=48.0)
    g.diag(236.7, 671.9, 181.0, 504.0, weight=96.0)
    g.hbar(268.3, 828.4, 647.3, weight=48.0)
    g.diag(828.4, 677.4, 709.6, 591.3, weight=48.0)
    g.dot(298.5, 510.7, w=84.0, h=109.2, slant=14.0)
    g.hbar(374.8, 614.5, 504.4, weight=48.0)
    g.diag(614.5, 457.9, 557.1, 560.6, weight=48.0)
    g.dot(462.1, 581.2, w=96.0, h=72.7, slant=-14.0)
    g.diag(598.3, 597.1, 687.5, 532.8, weight=48.0)
    g.diag(268.3, 379.3, 298.1, 354.3, weight=84.0)
    g.vbar(308.6, 266.1, 354.3, weight=84.0)
    g.hbar(319.2, 334.5, 262.7, weight=84.0)
    g.hbar(327.8, 431.2, 371.6, weight=48.0)
    g.hbar(431.2, 642.6, 389.0, weight=48.0)
    g.diag(642.6, 403.5, 686.8, 363.8, weight=48.0)
    g.diag(686.8, 363.8, 628.1, 287.2, weight=48.0)
    g.diag(403.6, 347.6, 411.2, 341.4, weight=64.0)
    g.diag(411.2, 341.4, 438.1, 264.2, weight=64.0)
    g.diag(533.1, 370.7, 513.0, 281.8, weight=92.0)
    g.vbar(513.0, 268.0, 281.8, weight=92.0)
    g.hbar(120.6, 879.4, 238.7, weight=48.0)
    g.hbar(291.3, 690.4, 164.9, weight=56.0)
    g.diag(474.6, 151.9, 509.9, 118.0, weight=96.0)
    g.diag(509.9, 118.0, 481.2, -62.4, weight=96.0)
    g.hbar(385.4, 481.2, -41.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_5be9() -> Glyph:
    """審 U+5BE9 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5BE9", advance=1000, unicode=0x5BE9, note="審：自动生成")
    g.diag(402.6, 802.0, 479.1, 765.6, weight=48.0)
    g.diag(479.1, 765.6, 514.8, 691.9, weight=48.0)
    g.diag(227.9, 663.3, 186.3, 547.1, weight=96.0)
    g.diag(186.3, 547.1, 253.4, 512.4, weight=96.0)
    g.hbar(250.8, 412.6, 643.6, weight=64.0)
    g.hbar(412.6, 778.4, 667.4, weight=64.0)
    g.diag(778.4, 685.8, 660.2, 586.3, weight=64.0)
    g.hbar(508.4, 556.0, 586.3, weight=56.0)
    g.hbar(300.4, 508.4, 556.9, weight=56.0)
    g.vbar(300.1, 503.4, 518.2, weight=56.0)
    g.dot(332.0, 461.9, w=76.0, h=74.9, slant=-14.0)
    g.diag(558.7, 566.9, 574.6, 529.0, weight=48.0)
    g.diag(574.6, 529.0, 505.8, 447.4, weight=48.0)
    g.hbar(215.2, 682.9, 408.9, weight=48.0)
    g.diag(414.2, 534.2, 438.0, 443.0, weight=48.0)
    g.vbar(444.5, 237.3, 443.0, weight=48.0)
    g.diag(416.3, 394.3, 343.3, 333.7, weight=48.0)
    g.diag(343.3, 333.7, 99.6, 172.3, weight=48.0)
    g.hbar(465.7, 900.4, 332.0, weight=48.0)
    g.diag(250.0, 222.7, 333.0, -11.2, weight=48.0)
    g.hbar(300.4, 571.2, 220.3, weight=48.0)
    g.vbar(580.6, 138.6, 238.5, weight=48.0)
    g.vbar(583.7, -47.0, 138.6, weight=48.0)
    g.hbar(331.3, 570.9, 113.1, weight=76.0)
    g.diag(422.7, 195.1, 449.8, 170.3, weight=48.0)
    g.diag(449.8, 170.3, 428.6, 45.5, weight=48.0)
    g.diag(343.5, 4.9, 355.3, 17.6, weight=76.0)
    g.hbar(355.3, 556.2, 27.7, weight=76.0)
    return g
def g_cjk_unified_ideograph_5bee() -> Glyph:
    """寮 U+5BEE —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5BEE", advance=1000, unicode=0x5BEE, note="寮：自动生成")
    g.diag(369.5, 802.0, 442.8, 759.9, weight=48.0)
    g.diag(442.8, 759.9, 474.9, 692.4, weight=48.0)
    g.diag(197.6, 669.0, 160.7, 555.1, weight=96.0)
    g.vbar(164.0, 478.9, 555.1, weight=96.0)
    g.diag(230.1, 648.5, 238.4, 640.2, weight=96.0)
    g.hbar(238.4, 748.7, 661.1, weight=96.0)
    g.diag(748.7, 682.0, 629.1, 564.3, weight=96.0)
    g.hbar(250.1, 632.6, 535.5, weight=48.0)
    g.diag(373.4, 617.3, 416.3, 552.5, weight=96.0)
    g.diag(416.3, 552.5, 91.6, 186.9, weight=96.0)
    g.diag(471.0, 505.6, 908.4, 249.1, weight=48.0)
    g.diag(166.6, 480.2, 272.8, 377.3, weight=64.0)
    g.diag(664.1, 544.6, 607.6, 424.0, weight=96.0)
    g.hbar(599.3, 607.6, 424.9, weight=96.0)
    g.vbar(322.6, 137.8, 321.3, weight=48.0)
    g.hbar(309.3, 435.6, 334.4, weight=48.0)
    g.hbar(435.6, 585.5, 347.0, weight=48.0)
    g.vbar(558.6, 166.0, 353.6, weight=48.0)
    g.hbar(525.8, 531.8, 166.8, weight=48.0)
    g.hbar(342.6, 540.6, 240.2, weight=56.0)
    g.diag(354.5, 153.7, 367.5, 163.8, weight=64.0)
    g.hbar(367.5, 518.6, 172.7, weight=64.0)
    g.diag(415.7, 149.7, 454.0, 116.9, weight=64.0)
    g.diag(454.0, 116.9, 425.8, -59.1, weight=64.0)
    g.diag(425.8, -59.1, 323.4, -2.8, weight=64.0)
    g.diag(305.2, 117.4, 250.1, 67.4, weight=96.0)
    g.diag(250.1, 67.4, 285.8, -10.9, weight=96.0)
    g.diag(570.7, 115.9, 723.8, -27.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_5c09() -> Glyph:
    """尉 U+5C09 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5C09", advance=1000, unicode=0x5C09, note="尉：自动生成")
    g.hbar(303.4, 531.4, 649.7, weight=48.0)
    g.diag(531.4, 660.5, 464.3, 560.5, weight=48.0)
    g.hbar(292.6, 498.8, 532.8, weight=48.0)
    g.diag(288.4, 654.1, 58.0, 31.1, weight=76.0)
    g.hbar(286.4, 515.8, 414.6, weight=76.0)
    g.hbar(246.0, 536.0, 298.0, weight=84.0)
    g.diag(379.3, 283.7, 417.6, 250.9, weight=56.0)
    g.diag(417.6, 250.9, 385.3, 44.5, weight=56.0)
    g.diag(385.3, 44.5, 259.4, 103.9, weight=56.0)
    g.vbar(267.8, 80.4, 250.6, weight=76.0)
    g.diag(445.9, 209.3, 523.7, 169.5, weight=96.0)
    g.hbar(446.4, 523.7, 159.6, weight=96.0)
    g.hbar(522.4, 937.0, 434.1, weight=96.0)
    g.diag(733.7, 725.9, 764.7, 477.7, weight=96.0)
    g.vbar(760.7, -9.1, 477.7, weight=96.0)
    g.hbar(639.2, 756.8, 13.4, weight=96.0)
    g.diag(566.8, 311.2, 740.3, 231.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_5c0b() -> Glyph:
    """尋 U+5C0B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5C0B", advance=1000, unicode=0x5C0B, note="尋：自动生成")
    g.hbar(369.4, 688.7, 732.8, weight=48.0)
    g.diag(688.7, 746.3, 609.5, 591.4, weight=48.0)
    g.hbar(380.7, 623.4, 633.3, weight=48.0)
    g.hbar(352.4, 651.1, 553.0, weight=48.0)
    g.vbar(648.6, 577.2, 601.2, weight=48.0)
    g.hbar(265.6, 475.2, 444.3, weight=64.0)
    g.diag(385.4, 415.6, 356.6, 342.5, weight=96.0)
    g.hbar(222.2, 269.0, 295.1, weight=64.0)
    g.hbar(269.0, 516.0, 331.3, weight=64.0)
    g.dot(528.4, 405.8, w=96.0, h=124.8, slant=-14.0)
    g.hbar(542.2, 706.5, 465.9, weight=48.0)
    g.vbar(695.9, 424.0, 478.7, weight=48.0)
    g.diag(685.3, 424.0, 661.9, 406.0, weight=48.0)
    g.hbar(562.7, 695.0, 375.2, weight=48.0)
    g.vbar(695.7, 391.4, 408.3, weight=48.0)
    g.hbar(116.6, 883.4, 219.4, weight=64.0)
    g.diag(578.5, 318.6, 622.2, 265.3, weight=96.0)
    g.vbar(605.9, -68.0, 265.3, weight=96.0)
    g.diag(589.7, -68.0, 461.3, 41.8, weight=96.0)
    g.diag(372.2, 179.5, 473.6, 14.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_5c64() -> Glyph:
    """層 U+5C64 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5C64", advance=1000, unicode=0x5C64, note="層：自动生成")
    g.hbar(392.8, 749.8, 745.8, weight=48.0)
    g.diag(749.8, 772.0, 707.8, 699.7, weight=48.0)
    g.hbar(681.1, 707.8, 693.8, weight=48.0)
    g.hbar(376.9, 736.5, 626.4, weight=48.0)
    g.vbar(306.6, 546.0, 763.1, weight=48.0)
    g.diag(295.7, 546.0, 105.5, 18.1, weight=48.0)
    g.diag(450.2, 561.0, 525.5, 497.6, weight=48.0)
    g.diag(664.2, 606.6, 684.0, 578.9, weight=64.0)
    g.diag(684.0, 578.9, 624.0, 493.9, weight=64.0)
    g.diag(624.0, 493.9, 618.6, 490.7, weight=64.0)
    g.diag(357.1, 446.1, 417.5, 249.0, weight=48.0)
    g.hbar(404.7, 561.5, 431.1, weight=64.0)
    g.hbar(561.5, 859.2, 459.7, weight=64.0)
    g.vbar(824.0, 301.7, 474.8, weight=64.0)
    g.hbar(760.3, 788.7, 308.1, weight=64.0)
    g.diag(561.2, 442.2, 584.0, 411.4, weight=64.0)
    g.vbar(583.0, 328.2, 411.4, weight=64.0)
    g.diag(582.0, 328.2, 566.1, 317.3, weight=64.0)
    g.dot(481.9, 358.9, w=48.0, h=62.4, slant=-14.0)
    g.diag(695.9, 431.3, 706.8, 405.5, weight=48.0)
    g.diag(706.8, 405.5, 639.5, 346.1, weight=48.0)
    g.hbar(434.4, 728.4, 288.3, weight=64.0)
    g.diag(728.4, 312.8, 739.5, 299.5, weight=64.0)
    g.diag(442.3, 195.5, 469.4, 169.7, weight=64.0)
    g.vbar(460.8, -73.0, 169.7, weight=64.0)
    g.hbar(493.8, 684.8, 140.9, weight=48.0)
    g.vbar(703.6, -51.3, 114.1, weight=48.0)
    g.hbar(670.2, 722.3, -45.8, weight=48.0)
    g.diag(493.8, 64.7, 506.7, 77.6, weight=64.0)
    g.hbar(506.7, 643.4, 83.1, weight=64.0)
    g.hbar(480.0, 684.0, -31.9, weight=64.0)
    return g
def g_cjk_unified_ideograph_5c65() -> Glyph:
    """履 U+5C65 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5C65", advance=1000, unicode=0x5C65, note="履：自动生成")
    g.diag(330.5, 701.6, 341.8, 691.4, weight=48.0)
    g.hbar(341.8, 626.3, 719.1, weight=48.0)
    g.diag(626.3, 746.8, 669.6, 711.8, weight=48.0)
    g.diag(669.6, 711.8, 620.8, 657.7, weight=48.0)
    g.hbar(323.1, 678.7, 600.3, weight=48.0)
    g.diag(265.2, 716.5, 58.0, 34.2, weight=48.0)
    g.diag(392.1, 532.6, 408.5, 506.6, weight=48.0)
    g.diag(408.5, 506.6, 318.0, 404.3, weight=48.0)
    g.diag(318.0, 404.3, 316.5, 398.2, weight=48.0)
    g.diag(386.5, 404.8, 412.2, 365.0, weight=48.0)
    g.diag(412.2, 365.0, 228.8, 169.6, weight=48.0)
    g.vbar(343.1, -41.4, 240.5, weight=48.0)
    g.hbar(572.8, 588.1, 573.4, weight=48.0)
    g.diag(572.8, 570.4, 455.6, 423.4, weight=48.0)
    g.hbar(568.5, 762.7, 534.5, weight=48.0)
    g.diag(498.5, 438.4, 521.5, 424.4, weight=96.0)
    g.diag(521.5, 424.4, 547.1, 278.8, weight=96.0)
    g.diag(548.0, 424.4, 565.3, 440.2, weight=48.0)
    g.hbar(565.3, 725.3, 445.1, weight=48.0)
    g.diag(725.3, 450.0, 693.6, 288.1, weight=48.0)
    g.hbar(552.7, 659.1, 366.0, weight=56.0)
    g.hbar(560.1, 654.6, 295.2, weight=56.0)
    g.diag(654.6, 307.8, 664.7, 317.0, weight=56.0)
    g.diag(538.7, 248.9, 552.0, 209.0, weight=48.0)
    g.diag(552.0, 209.0, 406.1, 87.4, weight=48.0)
    g.diag(575.1, 202.2, 619.5, 146.2, weight=64.0)
    g.diag(619.5, 146.2, 429.5, -5.0, weight=64.0)
    g.hbar(538.7, 912.0, 80.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_5cf0() -> Glyph:
    """峰 U+5CF0 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5CF0", advance=1000, unicode=0x5CF0, note="峰：自动生成")
    g.diag(195.6, 677.7, 239.0, 641.8, weight=92.0)
    g.vbar(235.7, 367.2, 641.8, weight=92.0)
    g.diag(232.4, 367.2, 215.4, 343.6, weight=92.0)
    g.diag(88.0, 437.0, 109.6, 411.1, weight=96.0)
    g.diag(109.6, 411.1, 127.4, 281.6, weight=96.0)
    g.diag(127.4, 281.6, 307.9, 369.1, weight=96.0)
    g.diag(360.7, 527.0, 307.1, 336.5, weight=48.0)
    g.diag(521.1, 786.2, 549.1, 746.0, weight=48.0)
    g.diag(549.1, 746.0, 339.9, 501.9, weight=48.0)
    g.diag(524.4, 682.3, 574.6, 609.0, weight=48.0)
    g.diag(574.6, 609.0, 359.3, 387.7, weight=48.0)
    g.hbar(474.0, 942.0, 523.4, weight=84.0)
    g.diag(420.3, 390.6, 517.1, 346.4, weight=64.0)
    g.hbar(517.1, 721.6, 390.5, weight=64.0)
    g.diag(452.3, 188.6, 482.6, 257.2, weight=64.0)
    g.hbar(482.6, 670.4, 273.4, weight=64.0)
    g.diag(670.4, 289.6, 700.5, 219.9, weight=64.0)
    g.hbar(329.6, 820.3, 169.1, weight=76.0)
    g.diag(510.3, 464.1, 551.9, 306.1, weight=48.0)
    g.vbar(556.8, -61.2, 306.1, weight=48.0)
    return g
def g_cjk_unified_ideograph_5d07() -> Glyph:
    """崇 U+5D07 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5D07", advance=1000, unicode=0x5D07, note="崇：自动生成")
    g.diag(483.2, 782.0, 519.7, 745.5, weight=96.0)
    g.vbar(514.3, 638.1, 745.5, weight=96.0)
    g.diag(508.9, 638.1, 495.1, 622.3, weight=96.0)
    g.diag(308.7, 714.0, 333.4, 677.5, weight=48.0)
    g.diag(333.4, 677.5, 426.2, 612.5, weight=48.0)
    g.hbar(426.2, 680.6, 617.0, weight=48.0)
    g.diag(676.0, 662.9, 727.7, 712.0, weight=96.0)
    g.diag(727.7, 712.0, 671.5, 580.9, weight=96.0)
    g.diag(472.5, 575.7, 568.4, 462.0, weight=48.0)
    g.diag(238.2, 430.6, 242.5, 433.5, weight=96.0)
    g.diag(242.5, 433.5, 189.5, 319.4, weight=96.0)
    g.diag(189.5, 319.4, 231.3, 215.6, weight=96.0)
    g.hbar(261.6, 438.8, 410.1, weight=76.0)
    g.hbar(438.8, 853.0, 435.0, weight=76.0)
    g.diag(853.0, 454.2, 741.5, 342.3, weight=76.0)
    g.diag(351.5, 379.2, 389.7, 312.8, weight=64.0)
    g.hbar(389.7, 620.3, 326.1, weight=64.0)
    g.diag(292.4, 142.9, 307.6, 183.9, weight=96.0)
    g.hbar(307.6, 689.8, 209.8, weight=96.0)
    g.diag(689.8, 235.6, 748.1, 304.5, weight=96.0)
    g.diag(479.3, 186.5, 520.6, 156.0, weight=96.0)
    g.diag(520.6, 156.0, 484.4, -56.8, weight=96.0)
    g.hbar(318.2, 484.4, -20.3, weight=96.0)
    g.diag(311.1, 143.4, 240.7, -37.3, weight=96.0)
    g.diag(644.8, 190.4, 798.7, -25.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_5d16() -> Glyph:
    """崖 U+5D16 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5D16", advance=1000, unicode=0x5D16, note="崖：自动生成")
    g.diag(533.1, 787.0, 567.9, 752.2, weight=96.0)
    g.diag(567.9, 752.2, 552.9, 637.8, weight=96.0)
    g.diag(552.9, 637.8, 539.8, 626.8, weight=96.0)
    g.diag(363.3, 719.9, 387.3, 679.6, weight=96.0)
    g.diag(387.3, 679.6, 372.5, 574.3, weight=96.0)
    g.hbar(372.5, 707.9, 600.8, weight=96.0)
    g.diag(707.9, 627.3, 717.2, 637.4, weight=96.0)
    g.diag(727.4, 674.4, 776.7, 722.7, weight=96.0)
    g.diag(776.7, 722.7, 733.2, 545.0, weight=96.0)
    g.hbar(375.8, 723.7, 474.5, weight=96.0)
    g.diag(723.7, 510.2, 751.5, 534.0, weight=96.0)
    g.diag(348.2, 465.6, 295.2, 325.6, weight=96.0)
    g.diag(295.2, 325.6, 101.5, -57.0, weight=96.0)
    g.vbar(448.0, 349.5, 427.7, weight=84.0)
    g.hbar(463.3, 661.3, 367.1, weight=84.0)
    g.vbar(677.7, 384.7, 470.6, weight=84.0)
    g.diag(548.4, 456.1, 578.1, 434.5, weight=96.0)
    g.diag(578.1, 434.5, 558.1, 274.8, weight=96.0)
    g.diag(558.1, 274.8, 554.2, 269.1, weight=96.0)
    g.hbar(329.9, 810.2, 246.4, weight=96.0)
    g.vbar(447.9, 32.0, 106.4, weight=92.0)
    g.hbar(460.3, 690.8, 125.3, weight=92.0)
    g.diag(690.8, 144.1, 719.2, 57.4, weight=92.0)
    g.diag(538.8, 224.0, 570.5, 193.9, weight=96.0)
    g.vbar(569.5, 50.4, 193.9, weight=96.0)
    g.diag(568.5, 50.4, 553.2, 31.2, weight=96.0)
    g.hbar(236.4, 487.4, 25.3, weight=92.0)
    g.hbar(487.4, 873.5, 8.1, weight=92.0)
    return g
def g_cjk_unified_ideograph_5e33() -> Glyph:
    """帳 U+5E33 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5E33", advance=1000, unicode=0x5E33, note="帳：自动生成")
    g.diag(96.9, 493.1, 28.0, 384.6, weight=96.0)
    g.diag(28.0, 384.6, 191.7, 271.5, weight=96.0)
    g.diag(130.4, 474.4, 142.1, 493.7, weight=96.0)
    g.hbar(142.1, 380.6, 516.4, weight=96.0)
    g.vbar(368.5, 343.3, 539.1, weight=96.0)
    g.hbar(270.1, 356.4, 359.3, weight=96.0)
    g.vbar(200.0, -49.3, 769.3, weight=96.0)
    g.hbar(529.5, 556.7, 716.7, weight=92.0)
    g.hbar(556.7, 694.9, 733.3, weight=92.0)
    g.vbar(709.5, 662.2, 754.7, weight=92.0)
    g.vbar(502.5, 708.8, 727.3, weight=64.0)
    g.vbar(507.9, 433.9, 708.8, weight=64.0)
    g.diag(515.4, 433.9, 496.1, 415.1, weight=64.0)
    g.hbar(534.7, 693.7, 612.9, weight=64.0)
    g.vbar(700.1, 561.0, 633.7, weight=64.0)
    g.hbar(535.3, 702.0, 519.3, weight=76.0)
    g.diag(702.0, 537.0, 738.2, 467.7, weight=76.0)
    g.hbar(389.4, 862.3, 412.0, weight=48.0)
    g.diag(453.4, 355.6, 487.4, 335.3, weight=56.0)
    g.vbar(479.9, 2.3, 335.3, weight=56.0)
    g.diag(472.3, 2.3, 686.6, 154.1, weight=56.0)
    g.diag(809.8, 409.5, 670.6, 248.9, weight=84.0)
    g.hbar(657.9, 670.6, 250.2, weight=84.0)
    g.diag(506.4, 326.6, 947.0, 87.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_5e3d() -> Glyph:
    """帽 U+5E3D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5E3D", advance=1000, unicode=0x5E3D, note="帽：自动生成")
    g.diag(177.6, 523.9, 179.8, 527.5, weight=48.0)
    g.vbar(170.6, 268.9, 527.5, weight=48.0)
    g.hbar(184.8, 365.6, 526.2, weight=48.0)
    g.diag(365.6, 536.7, 478.6, 302.6, weight=48.0)
    g.hbar(317.9, 478.6, 322.1, weight=48.0)
    g.vbar(267.1, -52.0, 772.0, weight=48.0)
    g.diag(531.7, 695.6, 518.6, 674.4, weight=48.0)
    g.vbar(553.8, 470.6, 674.4, weight=48.0)
    g.hbar(535.1, 872.6, 696.9, weight=48.0)
    g.diag(872.6, 709.6, 761.7, 486.1, weight=48.0)
    g.hbar(566.7, 799.0, 573.8, weight=64.0)
    g.hbar(596.4, 764.5, 481.3, weight=84.0)
    g.vbar(555.7, 276.3, 373.6, weight=48.0)
    g.vbar(556.8, 4.3, 276.3, weight=48.0)
    g.hbar(566.6, 771.6, 377.0, weight=48.0)
    g.vbar(786.0, 234.2, 389.3, weight=48.0)
    g.vbar(801.8, -49.0, 234.2, weight=48.0)
    g.hbar(581.0, 780.4, 255.5, weight=84.0)
    g.hbar(578.0, 781.1, 153.9, weight=84.0)
    g.hbar(571.9, 770.1, 31.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_5e63() -> Glyph:
    """幣 U+5E63 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5E63", advance=1000, unicode=0x5E63, note="幣：自动生成")
    g.diag(178.6, 683.9, 215.0, 660.5, weight=48.0)
    g.diag(215.0, 660.5, 244.7, 587.3, weight=48.0)
    g.diag(435.9, 746.3, 448.0, 716.5, weight=48.0)
    g.diag(448.0, 716.5, 372.6, 617.9, weight=48.0)
    g.vbar(166.9, 357.5, 561.1, weight=48.0)
    g.hbar(191.7, 456.4, 576.2, weight=64.0)
    g.vbar(440.9, 409.2, 602.0, weight=64.0)
    g.hbar(325.5, 425.5, 419.6, weight=64.0)
    g.diag(273.7, 785.5, 300.0, 627.0, weight=48.0)
    g.vbar(301.9, 299.4, 627.0, weight=48.0)
    g.diag(212.0, 540.4, 244.4, 493.8, weight=48.0)
    g.diag(244.4, 493.8, 229.3, 448.1, weight=48.0)
    g.diag(229.3, 448.1, 182.5, 424.4, weight=48.0)
    g.diag(321.3, 524.1, 371.0, 449.1, weight=48.0)
    g.hbar(474.3, 603.4, 760.3, weight=96.0)
    g.diag(603.4, 766.7, 490.9, 558.0, weight=96.0)
    g.hbar(571.1, 784.6, 656.8, weight=76.0)
    g.diag(643.8, 623.3, 695.6, 557.5, weight=76.0)
    g.diag(695.6, 557.5, 464.3, 416.7, weight=76.0)
    g.diag(518.9, 557.1, 601.5, 508.0, weight=64.0)
    g.diag(601.5, 508.0, 852.2, 358.8, weight=64.0)
    g.diag(852.2, 358.8, 885.3, 384.6, weight=64.0)
    g.vbar(268.7, 62.0, 285.9, weight=96.0)
    g.diag(303.5, 280.2, 315.5, 272.2, weight=96.0)
    g.hbar(315.5, 655.7, 294.8, weight=96.0)
    g.vbar(634.3, 101.7, 317.3, weight=96.0)
    g.hbar(485.3, 612.9, 116.2, weight=96.0)
    g.hbar(375.4, 416.9, 320.7, weight=96.0)
    g.diag(375.4, 317.8, 439.7, -62.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_5eb6() -> Glyph:
    """庶 U+5EB6 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5EB6", advance=1000, unicode=0x5EB6, note="庶：自动生成")
    g.diag(499.5, 792.0, 595.2, 742.7, weight=64.0)
    g.diag(595.2, 742.7, 638.1, 648.0, weight=64.0)
    g.hbar(352.3, 794.6, 614.6, weight=96.0)
    g.diag(322.2, 600.6, 267.5, 425.0, weight=96.0)
    g.diag(267.5, 425.0, 74.6, -55.9, weight=96.0)
    g.hbar(321.1, 896.3, 364.8, weight=96.0)
    g.diag(438.5, 540.2, 488.7, 437.7, weight=96.0)
    g.vbar(501.2, 163.6, 437.7, weight=96.0)
    g.diag(652.0, 585.5, 699.9, 501.0, weight=96.0)
    g.diag(699.9, 501.0, 663.7, 266.3, weight=96.0)
    g.diag(663.7, 266.3, 646.6, 250.2, weight=96.0)
    g.diag(531.8, 188.8, 545.8, 202.8, weight=96.0)
    g.hbar(545.8, 672.7, 212.7, weight=96.0)
    g.diag(672.7, 222.6, 681.0, 229.9, weight=96.0)
    g.diag(432.1, 99.7, 304.2, -67.0, weight=96.0)
    g.diag(492.9, 131.3, 511.6, 35.7, weight=96.0)
    g.hbar(511.6, 604.7, 45.3, weight=96.0)
    g.diag(593.3, 172.2, 674.8, -0.5, weight=96.0)
    g.diag(721.0, 181.2, 910.4, -46.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_5ec9() -> Glyph:
    """廉 U+5EC9 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5EC9", advance=1000, unicode=0x5EC9, note="廉：自动生成")
    g.diag(454.4, 797.0, 522.4, 758.7, weight=48.0)
    g.diag(522.4, 758.7, 549.7, 694.2, weight=48.0)
    g.hbar(323.2, 699.8, 671.9, weight=48.0)
    g.diag(299.8, 666.6, 157.5, 80.0, weight=96.0)
    g.diag(157.5, 80.0, 193.4, 36.8, weight=96.0)
    g.dot(449.1, 579.8, w=96.0, h=86.4, slant=-14.0)
    g.diag(642.5, 675.4, 566.1, 542.7, weight=48.0)
    g.hbar(313.5, 743.9, 520.7, weight=48.0)
    g.hbar(354.7, 677.3, 417.3, weight=48.0)
    g.diag(677.3, 439.4, 709.3, 409.4, weight=48.0)
    g.diag(709.3, 409.4, 660.0, 261.6, weight=48.0)
    g.hbar(268.1, 849.3, 320.4, weight=48.0)
    g.hbar(334.5, 690.7, 225.2, weight=48.0)
    g.vbar(688.9, 244.0, 266.6, weight=48.0)
    g.diag(426.6, 473.9, 464.0, 443.3, weight=92.0)
    g.vbar(449.2, 13.8, 443.3, weight=92.0)
    g.diag(434.3, 13.8, 528.8, -29.4, weight=92.0)
    g.diag(543.5, 495.0, 566.3, 479.0, weight=92.0)
    g.diag(566.3, 479.0, 469.0, -38.2, weight=92.0)
    g.diag(435.4, 189.2, 231.0, 29.1, weight=48.0)
    g.diag(584.8, 205.5, 895.4, 30.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_5eca() -> Glyph:
    """廊 U+5ECA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5ECA", advance=1000, unicode=0x5ECA, note="廊：自动生成")
    g.diag(527.3, 792.0, 598.3, 753.7, weight=48.0)
    g.diag(598.3, 753.7, 626.7, 692.6, weight=48.0)
    g.hbar(338.0, 786.9, 665.6, weight=48.0)
    g.diag(318.6, 655.0, 99.7, 40.4, weight=96.0)
    g.diag(467.2, 623.9, 531.2, 530.1, weight=48.0)
    g.hbar(394.0, 565.5, 495.6, weight=48.0)
    g.vbar(548.4, 330.8, 501.2, weight=48.0)
    g.hbar(516.1, 531.3, 330.3, weight=48.0)
    g.diag(412.2, 396.8, 424.2, 409.9, weight=56.0)
    g.hbar(424.2, 523.7, 408.8, weight=56.0)
    g.diag(412.3, 317.0, 420.9, 327.0, weight=56.0)
    g.hbar(420.9, 504.0, 335.0, weight=56.0)
    g.vbar(375.6, 466.6, 496.8, weight=48.0)
    g.vbar(386.8, 170.8, 466.6, weight=48.0)
    g.diag(403.8, 170.8, 512.9, 235.8, weight=48.0)
    g.diag(506.3, 252.4, 552.6, 220.6, weight=48.0)
    g.hbar(521.3, 552.6, 216.5, weight=48.0)
    g.hbar(674.3, 860.8, 527.7, weight=48.0)
    g.hbar(841.8, 860.8, 542.1, weight=48.0)
    g.vbar(834.1, 355.6, 540.8, weight=48.0)
    g.diag(826.5, 355.6, 919.6, 146.6, weight=48.0)
    g.hbar(739.3, 919.6, 182.2, weight=48.0)
    g.vbar(663.8, 409.9, 520.8, weight=48.0)
    g.vbar(661.5, -67.0, 409.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_5f0a() -> Glyph:
    """弊 U+5F0A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5F0A", advance=1000, unicode=0x5F0A, note="弊：自动生成")
    g.diag(246.9, 679.1, 366.1, 622.5, weight=48.0)
    g.hbar(503.1, 589.0, 691.5, weight=84.0)
    g.diag(503.1, 708.3, 445.4, 619.2, weight=84.0)
    g.vbar(237.5, 395.1, 559.8, weight=48.0)
    g.diag(233.1, 395.1, 253.8, 375.6, weight=48.0)
    g.hbar(256.3, 443.9, 528.1, weight=48.0)
    g.vbar(471.2, 376.2, 503.8, weight=48.0)
    g.hbar(400.6, 498.5, 385.3, weight=48.0)
    g.diag(353.3, 757.3, 377.6, 635.2, weight=48.0)
    g.vbar(377.1, 328.8, 635.2, weight=48.0)
    g.diag(299.6, 532.0, 320.3, 472.3, weight=48.0)
    g.diag(320.3, 472.3, 255.6, 394.7, weight=48.0)
    g.diag(400.0, 515.1, 497.3, 452.6, weight=48.0)
    g.diag(641.5, 794.0, 671.0, 765.6, weight=92.0)
    g.diag(671.0, 765.6, 555.8, 568.9, weight=92.0)
    g.hbar(620.8, 825.2, 641.9, weight=64.0)
    g.diag(692.4, 610.3, 742.8, 572.5, weight=64.0)
    g.diag(742.8, 572.5, 533.2, 386.3, weight=64.0)
    g.diag(565.8, 552.5, 901.5, 361.7, weight=48.0)
    g.hbar(120.7, 871.0, 237.3, weight=84.0)
    g.diag(871.0, 268.3, 902.3, 328.1, weight=84.0)
    g.diag(374.8, 318.9, 433.1, 239.1, weight=92.0)
    g.diag(433.1, 239.1, 246.9, -19.7, weight=92.0)
    g.diag(598.1, 375.3, 634.1, 234.0, weight=48.0)
    g.vbar(637.3, -64.0, 234.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_5f70() -> Glyph:
    """彰 U+5F70 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5F70", advance=1000, unicode=0x5F70, note="彰：自动生成")
    g.diag(387.2, 777.0, 474.6, 710.5, weight=48.0)
    g.hbar(273.3, 582.0, 648.8, weight=96.0)
    g.dot(349.2, 557.1, w=96.0, h=60.4, slant=-14.0)
    g.diag(495.5, 633.6, 519.2, 604.0, weight=96.0)
    g.diag(519.2, 604.0, 472.7, 522.4, weight=96.0)
    g.hbar(159.3, 620.0, 491.1, weight=56.0)
    g.diag(263.8, 399.9, 321.7, 227.0, weight=96.0)
    g.diag(320.7, 381.8, 327.1, 392.4, weight=48.0)
    g.hbar(327.1, 493.4, 411.6, weight=48.0)
    g.hbar(493.4, 557.3, 419.9, weight=48.0)
    g.diag(557.3, 409.0, 518.3, 246.0, weight=48.0)
    g.diag(329.3, 314.4, 342.1, 326.1, weight=48.0)
    g.hbar(342.1, 470.8, 333.1, weight=48.0)
    g.diag(339.7, 242.2, 349.2, 252.7, weight=56.0)
    g.hbar(349.2, 487.0, 266.4, weight=56.0)
    g.hbar(166.9, 590.5, 155.8, weight=84.0)
    g.diag(383.4, 236.5, 412.9, 209.0, weight=96.0)
    g.vbar(408.6, -57.0, 209.0, weight=96.0)
    g.diag(793.8, 711.5, 824.8, 672.5, weight=96.0)
    g.diag(824.8, 672.5, 647.5, 442.6, weight=96.0)
    g.diag(813.7, 499.6, 842.4, 458.6, weight=64.0)
    g.diag(842.4, 458.6, 628.5, 233.7, weight=64.0)
    g.diag(842.2, 318.2, 796.0, 205.8, weight=64.0)
    g.diag(796.0, 205.8, 572.5, -35.2, weight=64.0)
    return g
def g_cjk_unified_ideograph_5f90() -> Glyph:
    """徐 U+5F90 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5F90", advance=1000, unicode=0x5F90, note="徐：自动生成")
    g.diag(293.0, 737.4, 319.4, 693.3, weight=96.0)
    g.diag(319.4, 693.3, 140.4, 506.2, weight=96.0)
    g.diag(303.4, 560.2, 256.0, 440.8, weight=48.0)
    g.diag(256.0, 440.8, 58.0, 204.0, weight=48.0)
    g.vbar(236.2, 226.7, 343.7, weight=48.0)
    g.vbar(239.7, 3.1, 226.7, weight=48.0)
    g.diag(553.5, 746.9, 516.2, 634.7, weight=56.0)
    g.diag(516.2, 634.7, 284.7, 405.6, weight=56.0)
    g.diag(586.2, 653.0, 787.2, 439.1, weight=76.0)
    g.hbar(787.2, 942.0, 425.3, weight=76.0)
    g.hbar(426.7, 509.5, 412.4, weight=64.0)
    g.hbar(509.5, 720.6, 433.3, weight=64.0)
    g.vbar(402.6, 204.6, 248.2, weight=96.0)
    g.hbar(402.9, 733.3, 275.0, weight=96.0)
    g.diag(733.3, 301.7, 715.6, 201.0, weight=96.0)
    g.diag(537.5, 381.6, 558.2, 243.5, weight=64.0)
    g.vbar(552.1, -1.0, 243.5, weight=64.0)
    g.diag(546.0, -1.0, 405.5, 82.3, weight=64.0)
    g.dot(417.4, 130.3, w=96.0, h=124.8, slant=0.0)
    g.diag(609.2, 187.5, 798.9, 53.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_5faa() -> Glyph:
    """循 U+5FAA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5FAA", advance=1000, unicode=0x5FAA, note="循：自动生成")
    g.diag(302.3, 792.0, 334.7, 742.9, weight=96.0)
    g.diag(334.7, 742.9, 186.4, 553.1, weight=96.0)
    g.hbar(186.4, 251.0, 553.1, weight=96.0)
    g.diag(288.9, 559.3, 251.7, 439.8, weight=48.0)
    g.diag(251.7, 439.8, 57.2, 186.0, weight=48.0)
    g.vbar(237.2, -44.6, 342.5, weight=48.0)
    g.hbar(748.8, 809.0, 734.0, weight=96.0)
    g.hbar(571.8, 748.8, 704.7, weight=96.0)
    g.hbar(522.6, 571.8, 662.3, weight=96.0)
    g.diag(509.8, 666.4, 462.7, 521.6, weight=56.0)
    g.diag(462.7, 521.6, 360.1, 67.5, weight=56.0)
    g.hbar(260.2, 360.1, 49.5, weight=56.0)
    g.hbar(522.9, 922.8, 522.4, weight=96.0)
    g.diag(658.9, 679.0, 680.6, 546.0, weight=48.0)
    g.diag(680.6, 546.0, 653.3, 395.0, weight=48.0)
    g.vbar(559.6, -5.7, 382.5, weight=48.0)
    g.hbar(563.1, 788.8, 389.7, weight=48.0)
    g.vbar(800.6, 238.6, 398.4, weight=48.0)
    g.vbar(816.4, -57.0, 238.6, weight=48.0)
    g.diag(598.1, 249.1, 613.1, 264.1, weight=84.0)
    g.hbar(613.1, 791.0, 268.5, weight=84.0)
    g.diag(593.9, 133.3, 607.0, 150.7, weight=96.0)
    g.hbar(607.0, 788.7, 154.9, weight=96.0)
    g.hbar(583.6, 786.1, 18.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_5fb4() -> Glyph:
    """徴 U+5FB4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5FB4", advance=1000, unicode=0x5FB4, note="徴：自动生成")
    g.diag(310.0, 653.8, 274.4, 698.1, weight=96.0)
    g.diag(274.4, 698.1, 139.7, 498.9, weight=96.0)
    g.hbar(139.7, 192.7, 502.8, weight=96.0)
    g.vbar(197.5, 412.2, 540.0, weight=48.0)
    g.diag(198.0, 412.2, 53.0, 178.2, weight=48.0)
    g.vbar(204.9, -10.4, 330.0, weight=48.0)
    g.diag(434.8, 718.9, 465.2, 684.7, weight=84.0)
    g.vbar(461.0, 534.7, 684.7, weight=84.0)
    g.diag(456.7, 534.7, 441.4, 508.5, weight=84.0)
    g.diag(286.0, 648.6, 359.2, 589.5, weight=76.0)
    g.vbar(354.4, 459.7, 589.5, weight=76.0)
    g.hbar(349.5, 529.0, 494.1, weight=76.0)
    g.diag(557.6, 673.2, 577.6, 639.0, weight=48.0)
    g.diag(577.6, 639.0, 526.9, 499.4, weight=48.0)
    g.hbar(355.5, 375.4, 360.7, weight=76.0)
    g.hbar(355.5, 521.6, 380.3, weight=76.0)
    g.hbar(381.5, 388.8, 243.4, weight=96.0)
    g.hbar(381.5, 471.0, 260.0, weight=96.0)
    g.diag(471.0, 275.3, 465.6, 279.1, weight=96.0)
    g.diag(405.3, 351.4, 424.3, 335.2, weight=96.0)
    g.vbar(426.7, 163.7, 335.2, weight=96.0)
    g.diag(429.1, 163.7, 411.9, 147.7, weight=96.0)
    g.hbar(245.9, 586.5, 114.8, weight=96.0)
    g.vbar(667.5, 632.3, 750.4, weight=48.0)
    g.diag(662.2, 632.3, 547.1, 369.3, weight=48.0)
    g.hbar(612.8, 865.1, 469.0, weight=96.0)
    g.diag(686.1, 425.7, 752.7, 366.5, weight=76.0)
    g.diag(752.7, 366.5, 544.9, 30.8, weight=76.0)
    g.diag(544.9, 30.8, 462.4, 103.2, weight=76.0)
    g.diag(543.4, 350.9, 947.0, 25.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_5fb9() -> Glyph:
    """徹 U+5FB9 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni5FB9", advance=1000, unicode=0x5FB9, note="徹：自动生成")
    g.diag(277.0, 750.9, 302.1, 704.4, weight=84.0)
    g.diag(302.1, 704.4, 200.2, 571.5, weight=84.0)
    g.diag(200.2, 571.5, 216.8, 541.5, weight=84.0)
    g.diag(224.0, 571.5, 203.2, 448.9, weight=48.0)
    g.diag(203.2, 448.9, 53.0, 237.3, weight=48.0)
    g.vbar(219.0, 243.3, 382.6, weight=48.0)
    g.vbar(221.1, -16.7, 243.3, weight=48.0)
    g.hbar(330.9, 477.8, 729.4, weight=96.0)
    g.diag(477.8, 721.9, 517.0, 643.5, weight=96.0)
    g.hbar(299.4, 563.4, 579.2, weight=96.0)
    g.hbar(563.4, 672.2, 604.2, weight=96.0)
    g.diag(467.9, 566.3, 466.9, 563.8, weight=48.0)
    g.diag(466.9, 563.8, 383.4, 423.7, weight=48.0)
    g.hbar(383.4, 543.7, 446.6, weight=48.0)
    g.hbar(522.0, 562.8, 479.7, weight=48.0)
    g.diag(562.8, 476.7, 551.2, 454.5, weight=48.0)
    g.diag(385.3, 354.2, 375.3, 273.0, weight=48.0)
    g.vbar(363.3, 26.8, 273.0, weight=48.0)
    g.diag(394.7, 347.3, 494.9, 257.7, weight=56.0)
    g.vbar(498.8, 24.2, 257.7, weight=56.0)
    g.hbar(455.6, 502.8, 33.7, weight=56.0)
    g.hbar(400.6, 508.6, 257.3, weight=56.0)
    g.hbar(396.7, 509.6, 171.8, weight=64.0)
    g.diag(716.3, 748.0, 761.8, 706.8, weight=96.0)
    g.diag(761.8, 706.8, 613.8, 429.2, weight=96.0)
    g.hbar(684.4, 834.0, 496.0, weight=96.0)
    g.diag(834.0, 518.3, 802.3, 458.3, weight=96.0)
    g.vbar(733.2, 339.8, 467.1, weight=48.0)
    g.diag(726.7, 339.8, 558.3, 98.8, weight=48.0)
    g.diag(617.6, 390.9, 947.0, 77.0, weight=84.0)
    return g
def g_cjk_unified_ideograph_604b() -> Glyph:
    """恋 U+604B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni604B", advance=1000, unicode=0x604B, note="恋：自动生成")
    g.diag(415.1, 787.0, 505.1, 745.0, weight=76.0)
    g.diag(505.1, 745.0, 541.9, 648.0, weight=76.0)
    g.hbar(176.6, 770.2, 608.9, weight=96.0)
    g.diag(361.9, 567.0, 427.4, 510.1, weight=96.0)
    g.diag(427.4, 510.1, 395.6, 252.9, weight=96.0)
    g.diag(526.6, 585.4, 576.4, 548.8, weight=96.0)
    g.diag(576.4, 548.8, 523.3, 210.4, weight=96.0)
    g.diag(257.6, 542.0, 194.8, 228.8, weight=96.0)
    g.diag(592.8, 490.3, 746.1, 419.9, weight=76.0)
    g.diag(746.1, 419.9, 779.4, 349.0, weight=76.0)
    g.diag(250.6, 178.8, 124.4, -5.0, weight=96.0)
    g.hbar(232.6, 816.4, 55.3, weight=96.0)
    g.diag(816.4, -72.0, 565.2, 143.4, weight=96.0)
    g.diag(398.7, 249.7, 612.9, 133.0, weight=96.0)
    g.diag(754.3, 320.0, 875.6, 111.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_6063() -> Glyph:
    """恣 U+6063 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6063", advance=1000, unicode=0x6063, note="恣：自动生成")
    g.diag(184.1, 706.3, 263.7, 663.4, weight=96.0)
    g.diag(263.7, 663.4, 300.6, 584.8, weight=96.0)
    g.vbar(183.3, 223.9, 379.4, weight=96.0)
    g.diag(185.9, 379.4, 325.7, 533.0, weight=96.0)
    g.diag(457.6, 787.0, 494.2, 748.1, weight=48.0)
    g.diag(494.2, 748.1, 427.0, 588.4, weight=48.0)
    g.diag(427.0, 588.4, 322.0, 534.1, weight=48.0)
    g.hbar(453.4, 787.7, 622.3, weight=96.0)
    g.diag(787.7, 656.6, 559.1, 520.0, weight=96.0)
    g.diag(483.1, 575.3, 537.7, 488.9, weight=64.0)
    g.diag(537.7, 488.9, 300.4, 285.1, weight=64.0)
    g.hbar(531.4, 849.4, 377.1, weight=84.0)
    g.diag(183.3, 258.4, 132.8, -16.6, weight=96.0)
    g.diag(214.9, 172.7, 387.2, 83.2, weight=96.0)
    g.hbar(387.2, 791.6, 5.6, weight=96.0)
    g.diag(791.6, -72.0, 571.7, 144.7, weight=96.0)
    g.diag(409.3, 286.3, 604.3, 134.3, weight=96.0)
    g.diag(723.6, 286.8, 867.2, 121.7, weight=76.0)
    return g
def g_cjk_unified_ideograph_6065() -> Glyph:
    """恥 U+6065 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6065", advance=1000, unicode=0x6065, note="恥：自动生成")
    g.hbar(134.8, 399.1, 703.7, weight=96.0)
    g.vbar(396.6, 687.3, 727.9, weight=96.0)
    g.diag(168.5, 661.1, 209.6, 632.9, weight=96.0)
    g.vbar(201.0, 216.4, 632.9, weight=96.0)
    g.diag(192.3, 216.4, 180.3, 208.8, weight=96.0)
    g.diag(320.6, 687.0, 354.2, 517.7, weight=64.0)
    g.vbar(358.4, -5.1, 517.7, weight=64.0)
    g.diag(239.5, 489.6, 249.6, 503.1, weight=96.0)
    g.hbar(249.6, 330.5, 504.3, weight=96.0)
    g.diag(234.5, 353.6, 243.1, 370.8, weight=96.0)
    g.hbar(243.1, 331.2, 375.6, weight=96.0)
    g.diag(146.1, 191.4, 122.9, 140.3, weight=96.0)
    g.diag(122.9, 140.3, 341.9, 259.0, weight=96.0)
    g.diag(531.9, 428.9, 395.9, 264.6, weight=64.0)
    g.diag(521.7, 421.9, 628.3, 336.1, weight=96.0)
    g.diag(628.3, 336.1, 893.6, 191.4, weight=96.0)
    g.diag(893.6, 191.4, 784.4, 393.0, weight=96.0)
    g.diag(602.1, 581.3, 653.3, 531.0, weight=96.0)
    g.diag(653.3, 531.0, 590.0, 437.7, weight=96.0)
    g.diag(809.0, 561.6, 947.0, 436.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_606d() -> Glyph:
    """恭 U+606D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni606D", advance=1000, unicode=0x606D, note="恭：自动生成")
    g.diag(345.2, 566.5, 312.9, 549.3, weight=96.0)
    g.hbar(312.9, 628.0, 574.5, weight=96.0)
    g.diag(628.0, 599.6, 614.4, 609.8, weight=96.0)
    g.diag(346.0, 592.3, 379.0, 640.2, weight=96.0)
    g.vbar(384.7, 459.6, 640.2, weight=96.0)
    g.diag(390.5, 459.6, 378.0, 441.3, weight=96.0)
    g.diag(552.8, 740.0, 593.1, 693.6, weight=96.0)
    g.diag(593.1, 693.6, 533.6, 461.5, weight=96.0)
    g.hbar(197.5, 771.8, 419.7, weight=48.0)
    g.diag(344.4, 386.6, 373.8, 354.3, weight=84.0)
    g.diag(373.8, 354.3, 63.0, 45.6, weight=84.0)
    g.diag(502.7, 414.2, 632.3, 316.8, weight=48.0)
    g.diag(632.3, 316.8, 937.0, 137.8, weight=48.0)
    g.diag(370.1, 323.9, 469.6, 236.0, weight=56.0)
    g.vbar(453.4, -38.6, 236.0, weight=56.0)
    g.diag(437.2, -38.6, 289.0, 40.9, weight=56.0)
    g.diag(264.6, 170.2, 305.8, 3.8, weight=76.0)
    g.diag(476.0, 135.0, 566.3, 54.3, weight=48.0)
    g.diag(566.3, 54.3, 573.0, 9.1, weight=48.0)
    g.diag(561.0, 127.6, 723.4, 41.4, weight=92.0)
    g.hbar(609.7, 723.4, 24.3, weight=92.0)
    return g
def g_cjk_unified_ideograph_609f() -> Glyph:
    """悟 U+609F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni609F", advance=1000, unicode=0x609F, note="悟：自动生成")
    g.diag(203.5, 475.3, 104.4, 398.0, weight=96.0)
    g.diag(104.4, 398.0, 70.6, 265.6, weight=96.0)
    g.diag(277.2, 586.2, 280.0, 583.1, weight=96.0)
    g.diag(280.0, 583.1, 390.3, 518.0, weight=96.0)
    g.vbar(210.3, 494.0, 772.0, weight=96.0)
    g.vbar(223.8, -52.0, 494.0, weight=96.0)
    g.diag(516.2, 660.8, 498.4, 670.6, weight=96.0)
    g.hbar(498.4, 771.1, 690.7, weight=96.0)
    g.diag(553.2, 650.6, 576.2, 624.3, weight=96.0)
    g.diag(576.2, 624.3, 504.8, 364.4, weight=96.0)
    g.diag(504.8, 364.4, 481.6, 345.5, weight=96.0)
    g.hbar(387.1, 689.4, 524.5, weight=48.0)
    g.diag(689.4, 528.2, 724.4, 496.2, weight=48.0)
    g.diag(724.4, 496.2, 654.5, 357.7, weight=48.0)
    g.hbar(315.6, 914.4, 323.2, weight=48.0)
    g.diag(445.9, 196.6, 433.4, 174.3, weight=48.0)
    g.vbar(465.2, -8.9, 174.3, weight=48.0)
    g.hbar(448.7, 763.4, 195.6, weight=48.0)
    g.diag(763.4, 207.2, 687.1, 49.2, weight=48.0)
    g.hbar(484.8, 728.5, 23.9, weight=48.0)
    g.vbar(727.3, 31.2, 61.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_60a6() -> Glyph:
    """悦 U+60A6 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni60A6", advance=1000, unicode=0x60A6, note="悦：自动生成")
    g.diag(192.3, 479.6, 113.2, 422.3, weight=96.0)
    g.diag(113.2, 422.3, 84.1, 305.7, weight=96.0)
    g.diag(261.9, 531.8, 271.1, 519.1, weight=96.0)
    g.hbar(271.1, 378.5, 501.8, weight=96.0)
    g.diag(187.5, 754.9, 220.9, 549.9, weight=96.0)
    g.vbar(219.3, 12.9, 549.9, weight=96.0)
    g.diag(217.7, 12.9, 279.5, -16.8, weight=96.0)
    g.diag(427.7, 684.5, 551.0, 585.9, weight=84.0)
    g.diag(679.9, 782.0, 713.4, 748.1, weight=96.0)
    g.diag(713.4, 748.1, 590.0, 549.6, weight=96.0)
    g.diag(452.7, 495.6, 442.1, 477.8, weight=48.0)
    g.vbar(465.3, 288.1, 477.8, weight=48.0)
    g.hbar(457.1, 715.8, 499.9, weight=48.0)
    g.diag(715.8, 514.2, 651.2, 353.9, weight=48.0)
    g.hbar(500.0, 692.2, 320.8, weight=48.0)
    g.vbar(689.0, 340.3, 363.2, weight=48.0)
    g.diag(478.7, 253.7, 508.0, 181.0, weight=76.0)
    g.diag(508.0, 181.0, 247.5, 3.8, weight=76.0)
    g.diag(597.0, 306.7, 621.8, 211.9, weight=48.0)
    g.diag(621.8, 211.9, 654.0, 15.5, weight=48.0)
    g.hbar(654.0, 902.5, 20.7, weight=48.0)
    g.vbar(904.2, 26.0, 181.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_60bc() -> Glyph:
    """悼 U+60BC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni60BC", advance=1000, unicode=0x60BC, note="悼：自动生成")
    g.diag(197.8, 511.6, 116.2, 426.4, weight=96.0)
    g.diag(116.2, 426.4, 196.5, 341.7, weight=96.0)
    g.dot(311.6, 552.6, w=96.0, h=105.1, slant=-14.0)
    g.diag(195.4, 759.1, 225.7, 535.2, weight=96.0)
    g.vbar(224.6, 37.2, 535.2, weight=96.0)
    g.diag(581.4, 705.3, 565.7, 742.7, weight=96.0)
    g.vbar(563.3, 594.8, 742.7, weight=96.0)
    g.diag(560.8, 594.8, 548.8, 583.8, weight=96.0)
    g.diag(591.2, 662.0, 606.2, 676.0, weight=96.0)
    g.hbar(606.2, 708.9, 685.1, weight=96.0)
    g.vbar(711.3, 613.4, 694.3, weight=96.0)
    g.hbar(347.8, 415.5, 532.7, weight=48.0)
    g.vbar(436.4, 343.5, 533.9, weight=48.0)
    g.hbar(438.4, 710.2, 553.5, weight=48.0)
    g.diag(710.2, 580.9, 742.9, 535.8, weight=48.0)
    g.diag(742.9, 535.8, 670.4, 369.7, weight=48.0)
    g.hbar(462.7, 678.0, 443.5, weight=64.0)
    g.diag(473.4, 352.9, 484.2, 363.0, weight=76.0)
    g.hbar(484.2, 643.1, 372.0, weight=76.0)
    g.diag(643.1, 381.1, 651.5, 372.7, weight=76.0)
    g.hbar(272.4, 882.4, 250.8, weight=96.0)
    g.diag(527.1, 350.1, 567.6, 320.9, weight=96.0)
    g.vbar(566.7, -57.0, 320.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_60e7() -> Glyph:
    """惧 U+60E7 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni60E7", advance=1000, unicode=0x60E7, note="惧：自动生成")
    g.diag(96.1, 479.3, 64.2, 301.1, weight=96.0)
    g.hbar(280.6, 285.9, 541.7, weight=96.0)
    g.diag(285.9, 541.1, 367.1, 469.0, weight=96.0)
    g.vbar(224.4, 477.0, 772.0, weight=96.0)
    g.vbar(237.8, -72.0, 477.0, weight=96.0)
    g.diag(431.0, 691.6, 467.0, 647.9, weight=96.0)
    g.vbar(476.2, 239.2, 647.9, weight=96.0)
    g.diag(485.3, 239.2, 459.9, 221.7, weight=96.0)
    g.diag(508.3, 643.2, 683.1, 560.4, weight=48.0)
    g.diag(683.1, 560.4, 721.9, 276.7, weight=48.0)
    g.diag(721.9, 276.7, 699.0, 258.8, weight=48.0)
    g.dot(570.7, 536.5, w=84.0, h=109.2, slant=-14.0)
    g.dot(566.0, 427.3, w=84.0, h=109.2, slant=-14.0)
    g.diag(503.2, 308.3, 513.3, 322.2, weight=84.0)
    g.hbar(513.3, 646.4, 327.1, weight=84.0)
    g.hbar(302.2, 930.8, 202.1, weight=76.0)
    g.hbar(519.2, 539.2, 110.0, weight=76.0)
    g.diag(519.2, 108.7, 300.2, -64.8, weight=76.0)
    g.diag(670.1, 110.4, 817.5, -56.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_60e8() -> Glyph:
    """惨 U+60E8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni60E8", advance=1000, unicode=0x60E8, note="惨：自动生成")
    g.vbar(80.9, 355.1, 544.7, weight=96.0)
    g.dot(282.0, 546.7, w=96.0, h=111.4, slant=-14.0)
    g.vbar(183.1, 496.2, 763.2, weight=64.0)
    g.vbar(196.0, -26.3, 496.2, weight=64.0)
    g.diag(514.4, 797.0, 541.1, 762.1, weight=48.0)
    g.diag(541.1, 762.1, 423.2, 558.9, weight=48.0)
    g.hbar(423.2, 647.5, 579.1, weight=48.0)
    g.diag(609.7, 668.9, 699.1, 563.6, weight=48.0)
    g.hbar(300.9, 813.3, 453.4, weight=48.0)
    g.diag(485.6, 536.8, 454.3, 462.1, weight=48.0)
    g.diag(454.3, 462.1, 244.3, 231.9, weight=48.0)
    g.diag(608.7, 438.5, 683.9, 393.5, weight=48.0)
    g.diag(683.9, 393.5, 926.6, 282.6, weight=48.0)
    g.diag(538.2, 400.7, 561.4, 362.2, weight=76.0)
    g.diag(561.4, 362.2, 383.3, 198.1, weight=76.0)
    g.diag(584.9, 306.4, 540.1, 221.5, weight=48.0)
    g.diag(540.1, 221.5, 389.5, 62.4, weight=48.0)
    g.diag(389.5, 62.4, 396.2, 78.0, weight=48.0)
    g.diag(636.6, 204.1, 580.0, 102.4, weight=56.0)
    g.diag(580.0, 102.4, 365.4, -72.0, weight=56.0)
    return g
def g_cjk_unified_ideograph_60f0() -> Glyph:
    """惰 U+60F0 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni60F0", advance=1000, unicode=0x60F0, note="惰：自动生成")
    g.diag(215.4, 467.3, 130.5, 388.2, weight=96.0)
    g.diag(130.5, 388.2, 104.5, 294.9, weight=96.0)
    g.dot(344.3, 482.5, w=96.0, h=124.8, slant=-14.0)
    g.diag(211.2, 728.4, 243.1, 493.0, weight=76.0)
    g.vbar(241.6, -36.6, 493.0, weight=76.0)
    g.hbar(462.7, 501.4, 618.7, weight=92.0)
    g.hbar(462.7, 805.1, 656.9, weight=92.0)
    g.diag(547.6, 787.0, 521.5, 652.2, weight=48.0)
    g.diag(521.5, 652.2, 271.5, 285.7, weight=48.0)
    g.hbar(548.0, 710.4, 550.0, weight=84.0)
    g.diag(710.4, 557.5, 761.5, 478.2, weight=84.0)
    g.diag(613.9, 516.0, 638.7, 491.2, weight=92.0)
    g.diag(638.7, 491.2, 615.8, 449.7, weight=92.0)
    g.hbar(461.1, 870.5, 419.9, weight=96.0)
    g.vbar(507.8, -35.7, 334.0, weight=48.0)
    g.hbar(538.0, 699.7, 340.1, weight=48.0)
    g.vbar(714.8, 204.1, 358.0, weight=48.0)
    g.diag(729.8, 204.1, 765.4, -70.0, weight=48.0)
    g.diag(765.4, -70.0, 634.1, -8.8, weight=48.0)
    g.diag(549.1, 198.9, 563.0, 216.2, weight=64.0)
    g.hbar(563.0, 714.7, 221.7, weight=64.0)
    g.diag(541.8, 102.7, 552.6, 118.4, weight=76.0)
    g.hbar(552.6, 715.4, 121.2, weight=76.0)
    return g
def g_cjk_unified_ideograph_6101() -> Glyph:
    """愁 U+6101 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6101", advance=1000, unicode=0x6101, note="愁：自动生成")
    g.hbar(397.5, 539.7, 758.9, weight=96.0)
    g.diag(397.5, 750.8, 214.1, 645.9, weight=96.0)
    g.hbar(214.1, 270.2, 649.4, weight=96.0)
    g.hbar(73.6, 462.3, 538.6, weight=48.0)
    g.diag(307.7, 661.5, 350.6, 634.4, weight=96.0)
    g.vbar(329.2, 193.8, 634.4, weight=96.0)
    g.diag(309.0, 518.0, 116.9, 299.5, weight=48.0)
    g.diag(375.5, 458.2, 456.2, 419.1, weight=96.0)
    g.diag(456.2, 419.1, 496.1, 349.6, weight=96.0)
    g.dot(520.4, 546.1, w=96.0, h=124.8, slant=-14.0)
    g.diag(766.6, 679.0, 791.5, 640.2, weight=56.0)
    g.diag(791.5, 640.2, 642.0, 548.6, weight=56.0)
    g.vbar(576.1, 590.1, 777.0, weight=84.0)
    g.diag(575.5, 590.1, 447.7, 259.8, weight=84.0)
    g.diag(634.6, 479.0, 926.4, 289.2, weight=96.0)
    g.diag(254.1, 169.4, 159.2, -11.9, weight=96.0)
    g.hbar(245.2, 823.6, 46.8, weight=96.0)
    g.diag(823.6, -72.0, 602.0, 127.6, weight=96.0)
    g.diag(451.4, 245.8, 630.0, 121.8, weight=96.0)
    g.diag(752.8, 290.7, 866.6, 112.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_6109() -> Glyph:
    """愉 U+6109 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6109", advance=1000, unicode=0x6109, note="愉：自动生成")
    g.diag(88.0, 492.4, 53.0, 308.0, weight=96.0)
    g.dot(279.1, 554.7, w=96.0, h=102.8, slant=-14.0)
    g.diag(167.3, 766.4, 198.8, 539.2, weight=84.0)
    g.vbar(195.5, -44.3, 539.2, weight=84.0)
    g.diag(521.7, 769.5, 481.5, 642.3, weight=48.0)
    g.diag(481.5, 642.3, 267.3, 354.3, weight=48.0)
    g.vbar(575.3, 631.5, 675.7, weight=96.0)
    g.diag(573.3, 631.5, 942.0, 444.0, weight=96.0)
    g.hbar(434.1, 627.8, 464.6, weight=76.0)
    g.vbar(334.7, -15.5, 334.8, weight=48.0)
    g.diag(388.8, 327.6, 391.5, 325.5, weight=48.0)
    g.diag(391.5, 325.5, 490.7, 216.4, weight=48.0)
    g.vbar(494.7, -2.2, 216.4, weight=48.0)
    g.hbar(418.7, 498.7, 13.3, weight=48.0)
    g.diag(386.8, 217.3, 397.4, 231.5, weight=64.0)
    g.hbar(397.4, 455.8, 231.1, weight=64.0)
    g.diag(377.5, 124.6, 388.9, 138.4, weight=76.0)
    g.hbar(388.9, 455.8, 139.2, weight=76.0)
    g.vbar(602.1, 113.3, 316.2, weight=64.0)
    g.diag(701.0, 403.8, 764.8, -72.0, weight=96.0)
    g.diag(764.8, -72.0, 626.8, -7.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_611a() -> Glyph:
    """愚 U+611A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni611A", advance=1000, unicode=0x611A, note="愚：自动生成")
    g.vbar(300.2, 498.3, 729.3, weight=48.0)
    g.hbar(279.1, 685.7, 737.5, weight=48.0)
    g.vbar(649.9, 542.4, 746.0, weight=48.0)
    g.hbar(589.2, 614.1, 543.7, weight=48.0)
    g.hbar(331.3, 622.6, 616.9, weight=56.0)
    g.hbar(350.3, 595.1, 532.2, weight=48.0)
    g.vbar(207.4, 168.5, 431.6, weight=96.0)
    g.hbar(236.3, 410.9, 423.7, weight=64.0)
    g.hbar(410.9, 756.8, 441.1, weight=64.0)
    g.diag(756.8, 454.4, 703.9, 239.0, weight=64.0)
    g.diag(703.9, 239.0, 608.7, 285.2, weight=64.0)
    g.diag(440.4, 715.6, 476.3, 692.9, weight=96.0)
    g.vbar(471.4, 355.1, 692.9, weight=96.0)
    g.diag(466.4, 355.1, 454.9, 336.4, weight=96.0)
    g.hbar(267.2, 563.1, 314.7, weight=96.0)
    g.hbar(551.4, 591.7, 356.9, weight=48.0)
    g.diag(591.7, 349.9, 610.0, 294.3, weight=48.0)
    g.diag(216.2, 171.8, 112.1, -25.1, weight=96.0)
    g.diag(266.7, 169.8, 688.9, -61.4, weight=96.0)
    g.diag(688.9, -61.4, 724.4, 158.3, weight=96.0)
    g.diag(410.8, 253.4, 492.2, 147.9, weight=96.0)
    g.hbar(492.2, 614.4, 131.9, weight=96.0)
    g.diag(725.4, 212.9, 887.9, 75.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_6144() -> Glyph:
    """慄 U+6144 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6144", advance=1000, unicode=0x6144, note="慄：自动生成")
    g.diag(167.9, 535.9, 95.2, 468.6, weight=92.0)
    g.diag(95.2, 468.6, 68.1, 361.0, weight=92.0)
    g.hbar(68.1, 163.5, 345.9, weight=92.0)
    g.diag(225.1, 591.8, 291.5, 549.2, weight=48.0)
    g.diag(291.5, 549.2, 310.4, 514.1, weight=48.0)
    g.vbar(174.3, 512.9, 772.0, weight=48.0)
    g.vbar(186.9, 6.2, 512.9, weight=48.0)
    g.hbar(436.0, 685.2, 738.8, weight=96.0)
    g.diag(685.2, 769.0, 666.0, 720.2, weight=96.0)
    g.vbar(410.6, 430.8, 599.9, weight=76.0)
    g.hbar(418.0, 546.0, 602.4, weight=76.0)
    g.hbar(546.0, 793.0, 621.6, weight=76.0)
    g.diag(793.0, 635.9, 719.5, 477.3, weight=76.0)
    g.diag(471.3, 693.5, 498.5, 670.2, weight=64.0)
    g.vbar(506.9, 492.2, 670.2, weight=64.0)
    g.diag(515.4, 492.2, 505.3, 483.1, weight=64.0)
    g.diag(601.3, 724.6, 635.7, 697.0, weight=56.0)
    g.diag(635.7, 697.0, 602.5, 508.0, weight=56.0)
    g.diag(602.5, 508.0, 590.6, 499.6, weight=56.0)
    g.hbar(449.6, 708.2, 471.9, weight=48.0)
    g.hbar(320.1, 813.5, 352.2, weight=48.0)
    g.vbar(546.0, -52.0, 447.2, weight=96.0)
    g.diag(531.8, 336.8, 283.3, 71.1, weight=48.0)
    g.diag(579.5, 307.8, 928.9, 107.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_614b() -> Glyph:
    """態 U+614B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni614B", advance=1000, unicode=0x614B, note="態：自动生成")
    g.diag(277.8, 780.0, 316.2, 733.3, weight=48.0)
    g.diag(316.2, 733.3, 275.4, 610.6, weight=48.0)
    g.hbar(275.4, 414.7, 611.7, weight=48.0)
    g.hbar(382.7, 432.6, 626.4, weight=48.0)
    g.vbar(429.4, 597.4, 623.2, weight=48.0)
    g.vbar(217.2, 125.6, 472.8, weight=48.0)
    g.hbar(255.5, 428.1, 478.3, weight=84.0)
    g.diag(428.1, 486.6, 391.5, 203.8, weight=84.0)
    g.diag(391.5, 203.8, 313.8, 281.8, weight=84.0)
    g.hbar(251.1, 386.7, 377.4, weight=48.0)
    g.hbar(248.2, 386.3, 304.4, weight=56.0)
    g.diag(741.6, 690.2, 704.3, 727.1, weight=96.0)
    g.diag(704.3, 727.1, 571.4, 653.2, weight=96.0)
    g.diag(529.5, 782.0, 533.6, 777.1, weight=64.0)
    g.diag(533.6, 777.1, 570.5, 553.4, weight=64.0)
    g.hbar(570.5, 762.3, 560.1, weight=64.0)
    g.diag(762.3, 566.8, 720.4, 707.2, weight=64.0)
    g.diag(770.6, 394.1, 703.4, 440.0, weight=48.0)
    g.diag(703.4, 440.0, 576.2, 380.4, weight=48.0)
    g.diag(529.5, 496.3, 551.9, 470.6, weight=48.0)
    g.vbar(558.6, 274.0, 470.6, weight=48.0)
    g.hbar(565.4, 772.5, 277.0, weight=48.0)
    g.vbar(764.2, 279.9, 419.8, weight=48.0)
    g.diag(200.4, 135.1, 140.9, -53.0, weight=96.0)
    g.hbar(233.1, 803.9, 19.1, weight=96.0)
    g.diag(803.9, -72.0, 593.3, 92.2, weight=96.0)
    g.diag(421.8, 200.9, 555.4, 98.8, weight=64.0)
    g.diag(714.3, 233.1, 859.1, 66.9, weight=84.0)
    return g
def g_cjk_unified_ideograph_614c() -> Glyph:
    """慌 U+614C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni614C", advance=1000, unicode=0x614C, note="慌：自动生成")
    g.diag(170.3, 446.5, 89.8, 364.6, weight=96.0)
    g.diag(89.8, 364.6, 165.1, 246.7, weight=96.0)
    g.diag(235.3, 537.4, 299.0, 504.1, weight=96.0)
    g.diag(299.0, 504.1, 324.3, 462.3, weight=96.0)
    g.diag(162.5, 746.6, 194.7, 508.2, weight=96.0)
    g.vbar(191.0, 9.8, 508.2, weight=96.0)
    g.diag(187.3, 9.8, 224.8, -64.7, weight=96.0)
    g.hbar(302.3, 495.2, 566.5, weight=76.0)
    g.hbar(495.2, 850.8, 617.4, weight=76.0)
    g.diag(449.7, 644.7, 472.8, 686.0, weight=96.0)
    g.diag(472.8, 686.0, 497.1, 547.5, weight=96.0)
    g.vbar(671.4, 677.6, 726.2, weight=96.0)
    g.diag(674.3, 726.2, 605.3, 536.4, weight=96.0)
    g.diag(515.5, 542.3, 608.4, 477.7, weight=48.0)
    g.hbar(326.2, 511.0, 452.4, weight=48.0)
    g.hbar(511.0, 787.1, 461.1, weight=48.0)
    g.diag(434.8, 407.1, 460.7, 380.7, weight=48.0)
    g.vbar(457.8, 279.4, 380.7, weight=48.0)
    g.hbar(454.8, 738.6, 285.6, weight=48.0)
    g.diag(437.1, 258.0, 210.4, -57.9, weight=64.0)
    g.vbar(527.9, -38.6, 246.3, weight=96.0)
    g.diag(650.4, 283.1, 903.2, -66.6, weight=56.0)
    g.vbar(910.3, -66.6, 120.0, weight=56.0)
    return g
def g_cjk_unified_ideograph_6155() -> Glyph:
    """慕 U+6155 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6155", advance=1000, unicode=0x6155, note="慕：自动生成")
    g.hbar(174.4, 785.5, 648.4, weight=96.0)
    g.diag(334.7, 714.4, 371.9, 690.0, weight=48.0)
    g.diag(371.9, 690.0, 397.3, 567.7, weight=48.0)
    g.diag(574.3, 774.1, 606.2, 738.3, weight=96.0)
    g.diag(606.2, 738.3, 548.9, 584.4, weight=96.0)
    g.diag(291.7, 526.7, 317.3, 502.9, weight=48.0)
    g.vbar(342.2, 348.7, 502.9, weight=48.0)
    g.diag(344.5, 526.7, 349.0, 522.9, weight=64.0)
    g.hbar(349.0, 652.8, 532.6, weight=64.0)
    g.vbar(621.6, 371.1, 542.4, weight=64.0)
    g.hbar(585.1, 590.4, 371.6, weight=64.0)
    g.diag(366.0, 426.9, 375.8, 439.1, weight=56.0)
    g.hbar(375.8, 534.2, 446.7, weight=56.0)
    g.diag(379.7, 349.7, 388.3, 357.3, weight=48.0)
    g.hbar(388.3, 567.5, 372.6, weight=48.0)
    g.hbar(164.6, 783.6, 259.2, weight=48.0)
    g.diag(361.1, 330.1, 306.9, 236.6, weight=48.0)
    g.diag(306.9, 236.6, 58.0, 16.2, weight=48.0)
    g.diag(555.7, 250.9, 659.7, 189.6, weight=48.0)
    g.hbar(659.7, 942.0, 128.8, weight=48.0)
    g.diag(431.5, 205.0, 476.9, 153.8, weight=48.0)
    g.diag(476.9, 153.8, 445.3, -60.5, weight=48.0)
    g.hbar(340.6, 445.3, -41.2, weight=48.0)
    g.diag(322.0, 94.5, 259.4, -38.5, weight=64.0)
    g.dot(544.0, 20.1, w=76.0, h=98.8, slant=-14.0)
    g.dot(650.1, 39.7, w=76.0, h=98.8, slant=-14.0)
    return g
def g_cjk_unified_ideograph_6162() -> Glyph:
    """慢 U+6162 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6162", advance=1000, unicode=0x6162, note="慢：自动生成")
    g.diag(197.3, 520.1, 104.7, 442.6, weight=96.0)
    g.diag(104.7, 442.6, 76.0, 334.3, weight=96.0)
    g.dot(310.2, 548.2, w=96.0, h=124.5, slant=-14.0)
    g.vbar(204.2, 483.8, 772.0, weight=96.0)
    g.vbar(217.3, -52.0, 483.8, weight=96.0)
    g.vbar(461.1, 543.0, 744.1, weight=48.0)
    g.hbar(442.3, 746.9, 745.7, weight=48.0)
    g.vbar(721.8, 573.8, 748.2, weight=48.0)
    g.hbar(677.0, 696.7, 573.5, weight=48.0)
    g.hbar(490.1, 599.1, 650.3, weight=64.0)
    g.diag(599.1, 664.7, 643.2, 608.2, weight=64.0)
    g.hbar(504.6, 513.6, 558.7, weight=64.0)
    g.hbar(513.6, 672.7, 569.8, weight=64.0)
    g.diag(356.0, 477.1, 420.0, 298.1, weight=96.0)
    g.hbar(407.5, 824.1, 473.6, weight=76.0)
    g.vbar(798.1, 350.4, 485.1, weight=76.0)
    g.hbar(760.2, 772.2, 348.1, weight=76.0)
    g.diag(496.5, 444.0, 522.7, 359.9, weight=96.0)
    g.diag(522.7, 359.9, 526.7, 356.5, weight=96.0)
    g.diag(615.2, 466.1, 638.7, 443.8, weight=84.0)
    g.diag(638.7, 443.8, 609.2, 366.5, weight=84.0)
    g.hbar(435.0, 755.7, 339.3, weight=48.0)
    g.diag(453.0, 223.7, 539.2, 161.4, weight=96.0)
    g.diag(539.2, 161.4, 252.8, -13.8, weight=96.0)
    g.diag(457.2, 206.1, 914.0, -44.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_6163() -> Glyph:
    """慣 U+6163 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6163", advance=1000, unicode=0x6163, note="慣：自动生成")
    g.vbar(121.1, 322.2, 512.1, weight=96.0)
    g.diag(277.9, 554.3, 357.5, 474.7, weight=48.0)
    g.diag(205.9, 761.5, 237.7, 523.9, weight=48.0)
    g.vbar(236.2, -9.7, 523.9, weight=48.0)
    g.diag(446.7, 751.9, 472.1, 725.1, weight=48.0)
    g.vbar(458.0, 503.0, 725.1, weight=48.0)
    g.hbar(444.0, 657.7, 523.4, weight=48.0)
    g.hbar(486.0, 575.3, 746.6, weight=48.0)
    g.hbar(575.3, 736.9, 758.4, weight=48.0)
    g.vbar(711.0, 515.4, 767.7, weight=48.0)
    g.hbar(669.2, 685.1, 513.2, weight=48.0)
    g.diag(566.6, 732.7, 592.0, 713.0, weight=48.0)
    g.diag(592.0, 713.0, 555.0, 547.6, weight=48.0)
    g.hbar(339.2, 882.1, 621.4, weight=96.0)
    g.diag(431.3, 418.1, 449.2, 399.5, weight=84.0)
    g.vbar(456.1, 116.9, 399.5, weight=84.0)
    g.hbar(484.1, 679.8, 416.3, weight=48.0)
    g.diag(679.8, 442.3, 719.1, 407.4, weight=48.0)
    g.vbar(712.8, 121.7, 407.4, weight=48.0)
    g.diag(489.8, 303.0, 498.0, 314.7, weight=56.0)
    g.hbar(498.0, 647.1, 321.8, weight=56.0)
    g.diag(488.9, 222.4, 500.7, 234.3, weight=64.0)
    g.hbar(500.7, 648.1, 239.4, weight=64.0)
    g.hbar(486.0, 657.1, 147.4, weight=64.0)
    g.diag(657.1, 163.5, 674.0, 153.4, weight=64.0)
    g.hbar(515.6, 538.7, 58.0, weight=64.0)
    g.diag(515.6, 56.6, 364.2, -50.9, weight=64.0)
    g.diag(643.3, 83.4, 774.7, -72.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_6168() -> Glyph:
    """慨 U+6168 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6168", advance=1000, unicode=0x6168, note="慨：自动生成")
    g.diag(156.1, 475.5, 46.4, 326.5, weight=96.0)
    g.hbar(46.4, 152.5, 305.5, weight=96.0)
    g.diag(214.4, 521.5, 324.1, 458.5, weight=48.0)
    g.vbar(163.0, 486.6, 772.0, weight=96.0)
    g.vbar(176.2, -62.0, 486.6, weight=96.0)
    g.hbar(341.5, 475.1, 642.4, weight=48.0)
    g.diag(475.1, 659.0, 517.4, 625.3, weight=48.0)
    g.diag(517.4, 625.3, 464.7, 401.5, weight=48.0)
    g.diag(369.1, 497.1, 377.8, 512.0, weight=84.0)
    g.hbar(377.8, 460.9, 512.0, weight=84.0)
    g.diag(369.1, 381.0, 377.3, 394.2, weight=92.0)
    g.hbar(377.3, 451.6, 404.9, weight=92.0)
    g.vbar(330.6, 510.2, 632.0, weight=48.0)
    g.vbar(348.4, 184.2, 510.2, weight=48.0)
    g.diag(365.3, 184.2, 451.8, 229.5, weight=48.0)
    g.diag(451.8, 229.5, 463.2, 248.0, weight=48.0)
    g.hbar(451.1, 492.4, 252.2, weight=48.0)
    g.diag(492.4, 243.5, 469.7, 222.8, weight=48.0)
    g.hbar(610.2, 835.5, 637.4, weight=96.0)
    g.diag(514.9, 516.0, 575.9, 485.9, weight=48.0)
    g.diag(575.9, 485.9, 558.4, 361.6, weight=48.0)
    g.hbar(558.4, 867.1, 372.3, weight=48.0)
    g.vbar(636.1, 420.6, 598.9, weight=96.0)
    g.diag(628.1, 420.6, 412.9, -16.2, weight=96.0)
    g.diag(682.6, 277.9, 751.9, 147.2, weight=84.0)
    g.diag(751.9, 147.2, 931.7, -24.2, weight=84.0)
    g.vbar(935.6, -24.2, 147.8, weight=84.0)
    return g
def g_cjk_unified_ideograph_6170() -> Glyph:
    """慰 U+6170 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6170", advance=1000, unicode=0x6170, note="慰：自动生成")
    g.hbar(298.3, 515.2, 702.0, weight=48.0)
    g.diag(515.2, 711.9, 486.4, 644.6, weight=48.0)
    g.diag(486.4, 644.6, 464.1, 634.5, weight=48.0)
    g.hbar(282.1, 511.6, 575.9, weight=48.0)
    g.diag(241.7, 711.3, 93.1, 244.3, weight=92.0)
    g.hbar(310.4, 484.3, 502.1, weight=48.0)
    g.hbar(248.8, 521.7, 416.6, weight=56.0)
    g.diag(381.2, 393.9, 412.3, 366.9, weight=56.0)
    g.diag(412.3, 366.9, 389.9, 217.8, weight=56.0)
    g.hbar(325.6, 389.9, 230.0, weight=56.0)
    g.dot(257.4, 279.1, w=92.0, h=114.4, slant=14.0)
    g.dot(497.5, 316.0, w=96.0, h=71.5, slant=-14.0)
    g.hbar(540.9, 886.7, 540.5, weight=96.0)
    g.diag(688.5, 772.0, 719.0, 584.4, weight=96.0)
    g.vbar(718.3, 245.0, 584.4, weight=96.0)
    g.diag(717.5, 245.0, 618.8, 294.8, weight=96.0)
    g.dot(605.6, 408.0, w=96.0, h=84.4, slant=-14.0)
    g.diag(248.8, 148.2, 197.2, -22.6, weight=96.0)
    g.diag(345.8, 129.0, 785.3, -72.0, weight=96.0)
    g.diag(785.3, -72.0, 687.5, 117.9, weight=96.0)
    g.dot(530.3, 143.7, w=96.0, h=107.2, slant=-14.0)
    g.diag(780.5, 181.6, 906.9, 68.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_6176() -> Glyph:
    """慶 U+6176 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6176", advance=1000, unicode=0x6176, note="慶：自动生成")
    g.diag(481.8, 802.0, 587.5, 738.2, weight=48.0)
    g.hbar(345.5, 460.6, 668.2, weight=64.0)
    g.hbar(460.6, 754.3, 692.0, weight=64.0)
    g.vbar(264.0, 458.9, 689.6, weight=96.0)
    g.diag(252.9, 458.9, 85.4, -14.6, weight=96.0)
    g.hbar(388.4, 707.2, 596.7, weight=48.0)
    g.diag(707.2, 622.0, 739.8, 597.0, weight=48.0)
    g.vbar(729.0, 547.6, 597.0, weight=48.0)
    g.hbar(698.1, 718.1, 543.8, weight=48.0)
    g.diag(453.2, 626.7, 474.2, 605.7, weight=96.0)
    g.vbar(478.5, 497.1, 605.7, weight=96.0)
    g.diag(581.8, 661.9, 609.2, 634.6, weight=92.0)
    g.diag(609.2, 634.6, 593.8, 520.0, weight=92.0)
    g.diag(593.8, 520.0, 582.8, 512.3, weight=92.0)
    g.hbar(392.2, 737.1, 484.7, weight=48.0)
    g.hbar(332.2, 886.3, 410.9, weight=48.0)
    g.diag(886.3, 442.9, 785.7, 354.2, weight=48.0)
    g.dot(363.1, 254.6, w=96.0, h=124.8, slant=14.0)
    g.hbar(451.3, 729.1, 276.4, weight=48.0)
    g.diag(729.1, 227.3, 652.3, 329.4, weight=48.0)
    g.dot(560.4, 334.2, w=48.0, h=62.4, slant=-14.0)
    g.diag(682.8, 382.7, 755.2, 323.7, weight=48.0)
    g.diag(465.6, 208.4, 484.5, 158.3, weight=64.0)
    g.diag(484.5, 158.3, 206.1, -59.8, weight=64.0)
    g.diag(206.1, -59.8, 225.5, -32.7, weight=64.0)
    g.diag(511.3, 153.1, 582.0, 96.6, weight=76.0)
    g.diag(582.0, 96.6, 364.6, -62.2, weight=76.0)
    g.diag(480.8, 121.7, 865.6, -72.0, weight=96.0)
    g.hbar(865.6, 909.6, -67.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_6182() -> Glyph:
    """憂 U+6182 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6182", advance=1000, unicode=0x6182, note="憂：自动生成")
    g.hbar(303.4, 663.5, 738.4, weight=48.0)
    g.diag(476.2, 718.3, 421.8, 648.4, weight=48.0)
    g.diag(421.8, 648.4, 412.4, 643.8, weight=48.0)
    g.vbar(359.4, 450.5, 627.7, weight=48.0)
    g.diag(372.2, 450.5, 358.4, 426.5, weight=48.0)
    g.hbar(363.9, 667.6, 648.6, weight=48.0)
    g.diag(667.6, 672.1, 592.2, 527.3, weight=48.0)
    g.diag(592.2, 527.3, 574.5, 459.7, weight=48.0)
    g.hbar(384.8, 484.2, 560.6, weight=56.0)
    g.diag(484.2, 570.8, 512.9, 524.5, weight=56.0)
    g.hbar(385.6, 495.8, 496.4, weight=48.0)
    g.hbar(495.8, 558.6, 488.3, weight=48.0)
    g.diag(190.6, 418.4, 156.6, 304.7, weight=96.0)
    g.diag(156.6, 304.7, 227.2, 243.2, weight=96.0)
    g.hbar(212.2, 836.9, 425.0, weight=48.0)
    g.diag(836.9, 454.9, 689.0, 336.3, weight=48.0)
    g.vbar(291.5, 252.1, 359.0, weight=96.0)
    g.hbar(192.2, 272.3, 252.0, weight=96.0)
    g.hbar(331.8, 621.5, 296.5, weight=48.0)
    g.diag(621.5, 252.8, 557.9, 336.6, weight=48.0)
    g.vbar(562.9, 336.6, 372.7, weight=48.0)
    g.diag(434.1, 401.6, 482.5, 352.5, weight=48.0)
    g.hbar(482.5, 531.4, 348.1, weight=48.0)
    g.hbar(565.9, 630.3, 360.9, weight=48.0)
    g.hbar(630.3, 702.3, 351.9, weight=48.0)
    g.diag(434.5, 200.4, 344.9, 133.6, weight=48.0)
    g.diag(344.9, 133.6, 155.0, -35.7, weight=48.0)
    g.diag(411.4, 187.3, 475.8, 106.9, weight=48.0)
    g.diag(475.8, 106.9, 294.3, -52.0, weight=48.0)
    g.hbar(373.5, 389.3, 136.2, weight=96.0)
    g.hbar(373.5, 830.0, 47.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_618e() -> Glyph:
    """憎 U+618E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni618E", advance=1000, unicode=0x618E, note="憎：自动生成")
    g.diag(218.0, 460.7, 133.3, 381.7, weight=96.0)
    g.diag(133.3, 381.7, 216.9, 275.1, weight=96.0)
    g.hbar(276.0, 413.5, 490.9, weight=48.0)
    g.vbar(225.9, 477.9, 750.7, weight=96.0)
    g.vbar(243.0, -45.1, 477.9, weight=96.0)
    g.diag(472.8, 724.2, 545.4, 677.1, weight=56.0)
    g.diag(545.4, 677.1, 564.2, 607.2, weight=56.0)
    g.diag(710.3, 787.0, 730.6, 754.1, weight=92.0)
    g.diag(730.6, 754.1, 628.3, 629.2, weight=92.0)
    g.vbar(400.5, 577.9, 580.4, weight=48.0)
    g.vbar(433.5, 332.2, 577.9, weight=48.0)
    g.hbar(414.8, 741.6, 544.9, weight=48.0)
    g.diag(741.6, 512.4, 796.6, 357.5, weight=48.0)
    g.diag(796.6, 357.5, 771.1, 371.9, weight=48.0)
    g.diag(586.6, 566.2, 596.7, 560.3, weight=64.0)
    g.diag(596.7, 560.3, 625.0, 402.4, weight=64.0)
    g.diag(625.0, 402.4, 599.4, 389.6, weight=64.0)
    g.hbar(448.1, 526.8, 475.7, weight=48.0)
    g.diag(526.8, 465.1, 541.5, 437.7, weight=48.0)
    g.diag(727.2, 581.4, 741.7, 511.3, weight=48.0)
    g.diag(741.7, 511.3, 634.3, 444.5, weight=48.0)
    g.hbar(479.6, 754.4, 361.1, weight=96.0)
    g.diag(506.7, 261.4, 498.4, 245.4, weight=48.0)
    g.vbar(502.6, -12.0, 245.4, weight=48.0)
    g.hbar(514.1, 665.9, 223.3, weight=48.0)
    g.diag(665.9, 193.9, 747.5, -52.0, weight=48.0)
    g.diag(531.7, 120.7, 545.1, 135.5, weight=96.0)
    g.hbar(545.1, 716.0, 138.2, weight=96.0)
    g.hbar(519.9, 713.5, 15.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_61a4() -> Glyph:
    """憤 U+61A4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni61A4", advance=1000, unicode=0x61A4, note="憤：自动生成")
    g.diag(211.7, 460.5, 137.4, 384.5, weight=92.0)
    g.diag(137.4, 384.5, 207.6, 275.7, weight=92.0)
    g.diag(269.0, 518.4, 364.3, 471.1, weight=48.0)
    g.vbar(219.3, 456.6, 726.8, weight=48.0)
    g.vbar(231.5, -42.1, 456.6, weight=48.0)
    g.hbar(460.8, 672.9, 640.7, weight=96.0)
    g.hbar(672.9, 730.3, 671.4, weight=96.0)
    g.vbar(596.0, 678.4, 694.5, weight=92.0)
    g.vbar(595.6, 552.0, 678.4, weight=92.0)
    g.hbar(371.7, 882.9, 508.7, weight=96.0)
    g.diag(448.9, 564.1, 482.5, 546.3, weight=48.0)
    g.diag(482.5, 546.3, 511.5, 404.6, weight=48.0)
    g.diag(697.1, 648.7, 726.4, 598.8, weight=76.0)
    g.diag(726.4, 598.8, 627.5, 420.0, weight=76.0)
    g.vbar(471.8, 377.0, 394.0, weight=48.0)
    g.vbar(480.2, 104.6, 377.0, weight=48.0)
    g.hbar(487.5, 705.2, 402.6, weight=48.0)
    g.vbar(717.0, 308.6, 416.8, weight=48.0)
    g.vbar(717.6, 59.1, 308.6, weight=48.0)
    g.diag(505.0, 290.9, 518.3, 305.6, weight=64.0)
    g.hbar(518.3, 715.5, 307.8, weight=64.0)
    g.hbar(504.7, 714.0, 214.6, weight=64.0)
    g.hbar(505.6, 715.7, 122.7, weight=56.0)
    g.diag(553.0, 110.3, 379.6, -58.0, weight=56.0)
    g.diag(698.4, 74.8, 781.9, -72.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_61a7() -> Glyph:
    """憧 U+61A7 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni61A7", advance=1000, unicode=0x61A7, note="憧：自动生成")
    g.diag(193.6, 480.6, 110.3, 438.2, weight=96.0)
    g.diag(110.3, 438.2, 74.1, 299.8, weight=96.0)
    g.hbar(256.6, 323.7, 553.0, weight=56.0)
    g.vbar(332.2, 471.5, 540.4, weight=56.0)
    g.diag(185.3, 761.7, 217.4, 513.9, weight=96.0)
    g.vbar(214.4, 43.1, 513.9, weight=96.0)
    g.diag(211.4, 43.1, 293.8, -40.1, weight=96.0)
    g.diag(559.2, 686.8, 605.8, 745.6, weight=96.0)
    g.diag(605.8, 745.6, 623.5, 698.4, weight=96.0)
    g.hbar(470.9, 720.3, 647.5, weight=96.0)
    g.vbar(715.5, 641.9, 678.1, weight=96.0)
    g.dot(511.8, 556.6, w=96.0, h=102.4, slant=-14.0)
    g.diag(660.4, 639.4, 684.8, 607.4, weight=96.0)
    g.diag(684.8, 607.4, 639.1, 517.1, weight=96.0)
    g.hbar(625.0, 639.1, 515.1, weight=96.0)
    g.hbar(340.6, 527.1, 484.2, weight=64.0)
    g.hbar(527.1, 900.9, 484.5, weight=64.0)
    g.vbar(422.8, 368.9, 381.5, weight=48.0)
    g.vbar(448.6, 173.4, 368.9, weight=48.0)
    g.hbar(436.0, 788.4, 388.1, weight=48.0)
    g.vbar(756.0, 213.3, 401.0, weight=48.0)
    g.hbar(697.7, 723.7, 217.3, weight=48.0)
    g.hbar(473.2, 724.1, 280.0, weight=64.0)
    g.hbar(489.5, 668.2, 203.6, weight=64.0)
    g.diag(668.2, 220.6, 681.6, 210.8, weight=64.0)
    g.diag(558.3, 366.5, 590.3, 348.9, weight=96.0)
    g.vbar(587.8, 22.6, 348.9, weight=96.0)
    g.diag(585.4, 22.6, 570.4, 3.6, weight=96.0)
    g.diag(466.4, 132.9, 485.6, 77.3, weight=92.0)
    g.hbar(485.6, 642.1, 89.5, weight=92.0)
    g.diag(642.1, 101.7, 721.3, 177.1, weight=92.0)
    g.hbar(244.3, 886.8, -29.3, weight=92.0)
    return g
def g_cjk_unified_ideograph_61a9() -> Glyph:
    """憩 U+61A9 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni61A9", advance=1000, unicode=0x61A9, note="憩：自动生成")
    g.diag(498.3, 657.8, 404.6, 727.3, weight=96.0)
    g.diag(404.6, 727.3, 178.0, 623.5, weight=96.0)
    g.diag(178.0, 623.5, 192.5, 544.6, weight=96.0)
    g.diag(152.4, 433.9, 123.9, 494.9, weight=96.0)
    g.hbar(123.9, 512.9, 525.6, weight=96.0)
    g.diag(301.8, 645.3, 341.8, 616.8, weight=96.0)
    g.diag(341.8, 616.8, 302.9, 431.6, weight=96.0)
    g.vbar(222.1, 251.4, 405.7, weight=48.0)
    g.hbar(211.7, 440.4, 408.8, weight=48.0)
    g.diag(440.4, 416.0, 386.9, 311.6, weight=48.0)
    g.diag(259.9, 263.2, 268.1, 270.6, weight=48.0)
    g.hbar(268.1, 416.7, 294.9, weight=48.0)
    g.diag(631.8, 802.0, 668.8, 770.4, weight=76.0)
    g.diag(668.8, 770.4, 571.6, 623.6, weight=76.0)
    g.vbar(547.5, 277.1, 625.8, weight=92.0)
    g.diag(572.6, 612.1, 722.9, 533.6, weight=48.0)
    g.vbar(733.0, 294.0, 533.6, weight=48.0)
    g.diag(579.4, 506.2, 589.9, 520.0, weight=64.0)
    g.hbar(589.9, 738.0, 521.8, weight=64.0)
    g.diag(584.0, 414.0, 590.5, 426.9, weight=76.0)
    g.hbar(590.5, 734.3, 427.5, weight=76.0)
    g.hbar(579.9, 714.8, 305.9, weight=96.0)
    g.diag(714.8, 318.1, 726.2, 303.0, weight=96.0)
    g.diag(229.4, 213.4, 150.4, -32.1, weight=96.0)
    g.diag(247.5, 158.4, 413.2, 70.5, weight=96.0)
    g.hbar(413.2, 767.8, -0.7, weight=96.0)
    g.diag(767.8, -72.0, 689.5, 76.6, weight=96.0)
    g.diag(689.5, 76.6, 582.1, 125.4, weight=96.0)
    g.diag(441.6, 252.2, 640.0, 112.3, weight=96.0)
    g.diag(753.1, 248.2, 907.7, 114.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_61ac() -> Glyph:
    """憬 U+61AC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni61AC", advance=1000, unicode=0x61AC, note="憬：自动生成")
    g.diag(181.7, 508.7, 67.0, 307.7, weight=96.0)
    g.diag(250.8, 584.0, 330.6, 543.0, weight=96.0)
    g.vbar(333.9, 431.8, 543.0, weight=96.0)
    g.vbar(187.3, 489.1, 769.9, weight=96.0)
    g.vbar(201.0, -59.9, 489.1, weight=96.0)
    g.vbar(456.5, 535.6, 742.3, weight=48.0)
    g.hbar(432.1, 763.7, 751.4, weight=48.0)
    g.vbar(727.7, 569.1, 755.3, weight=48.0)
    g.hbar(667.3, 691.8, 570.2, weight=48.0)
    g.hbar(494.8, 696.6, 642.4, weight=64.0)
    g.diag(513.4, 548.3, 526.1, 560.0, weight=64.0)
    g.hbar(526.1, 666.8, 570.2, weight=64.0)
    g.dot(585.3, 492.1, w=96.0, h=105.5, slant=-14.0)
    g.hbar(248.2, 923.0, 417.7, weight=76.0)
    g.vbar(452.3, 294.1, 318.6, weight=48.0)
    g.vbar(474.9, 179.8, 294.1, weight=48.0)
    g.hbar(463.2, 691.7, 324.1, weight=48.0)
    g.diag(691.7, 340.9, 726.4, 301.2, weight=48.0)
    g.diag(726.4, 301.2, 673.1, 231.1, weight=48.0)
    g.hbar(498.3, 707.5, 217.6, weight=48.0)
    g.diag(575.4, 176.4, 611.8, 152.1, weight=96.0)
    g.diag(611.8, 152.1, 579.9, -63.6, weight=96.0)
    g.diag(579.9, -63.6, 437.4, 11.8, weight=96.0)
    g.diag(460.8, 137.0, 414.6, 51.4, weight=96.0)
    g.diag(414.6, 51.4, 462.6, -25.3, weight=96.0)
    g.diag(724.7, 166.4, 852.7, -24.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_61b2() -> Glyph:
    """憲 U+61B2 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni61B2", advance=1000, unicode=0x61B2, note="憲：自动生成")
    g.diag(408.9, 792.0, 481.2, 754.4, weight=48.0)
    g.diag(481.2, 754.4, 507.7, 688.4, weight=48.0)
    g.diag(210.3, 660.0, 186.7, 544.8, weight=96.0)
    g.diag(186.7, 544.8, 247.3, 425.2, weight=96.0)
    g.hbar(243.3, 415.7, 644.6, weight=64.0)
    g.hbar(415.7, 768.3, 661.6, weight=64.0)
    g.diag(768.3, 674.9, 665.4, 578.7, weight=64.0)
    g.hbar(617.4, 665.4, 582.8, weight=64.0)
    g.hbar(316.8, 633.9, 569.9, weight=48.0)
    g.diag(351.3, 538.4, 445.5, 495.1, weight=48.0)
    g.hbar(445.5, 538.5, 505.4, weight=48.0)
    g.diag(538.5, 515.8, 581.7, 461.0, weight=48.0)
    g.diag(429.5, 624.8, 463.4, 593.6, weight=96.0)
    g.vbar(462.4, 459.4, 593.6, weight=96.0)
    g.diag(461.5, 459.4, 448.3, 438.7, weight=96.0)
    g.hbar(259.6, 680.4, 387.7, weight=56.0)
    g.vbar(283.2, 301.6, 311.4, weight=76.0)
    g.vbar(305.0, 179.4, 301.6, weight=76.0)
    g.hbar(303.0, 655.4, 323.2, weight=48.0)
    g.diag(655.4, 346.1, 579.2, 211.7, weight=48.0)
    g.diag(386.3, 303.4, 391.4, 299.6, weight=76.0)
    g.diag(391.4, 299.6, 415.4, 221.7, weight=76.0)
    g.diag(485.9, 324.1, 506.9, 302.1, weight=76.0)
    g.diag(506.9, 302.1, 475.6, 237.7, weight=76.0)
    g.diag(342.2, 187.9, 349.7, 194.5, weight=48.0)
    g.hbar(349.7, 578.7, 210.3, weight=48.0)
    g.diag(260.2, 134.5, 192.8, 82.7, weight=96.0)
    g.diag(192.8, 82.7, 159.0, -10.4, weight=96.0)
    g.diag(308.8, 146.2, 739.5, -69.3, weight=96.0)
    g.diag(739.5, -69.3, 607.0, 163.0, weight=96.0)
    g.diag(452.3, 171.7, 511.3, 114.6, weight=96.0)
    g.hbar(511.3, 605.6, 107.8, weight=96.0)
    g.diag(645.1, 246.8, 841.0, 132.5, weight=84.0)
    return g
def g_cjk_unified_ideograph_61b6() -> Glyph:
    """憶 U+61B6 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni61B6", advance=1000, unicode=0x61B6, note="憶：自动生成")
    g.vbar(90.6, 298.9, 462.2, weight=96.0)
    g.hbar(256.9, 273.6, 567.7, weight=96.0)
    g.diag(273.6, 570.6, 337.1, 536.7, weight=96.0)
    g.diag(181.5, 741.6, 213.4, 491.4, weight=96.0)
    g.vbar(212.0, -51.0, 491.4, weight=96.0)
    g.diag(540.1, 787.0, 628.1, 733.8, weight=48.0)
    g.hbar(435.7, 745.0, 659.4, weight=96.0)
    g.dot(500.5, 575.8, w=96.0, h=75.9, slant=-14.0)
    g.diag(649.3, 642.0, 673.0, 614.4, weight=96.0)
    g.diag(673.0, 614.4, 619.4, 525.1, weight=96.0)
    g.hbar(358.4, 887.1, 498.0, weight=96.0)
    g.vbar(462.8, 203.2, 402.3, weight=48.0)
    g.hbar(458.9, 734.6, 415.0, weight=48.0)
    g.vbar(710.1, 238.1, 424.9, weight=48.0)
    g.hbar(652.2, 685.7, 239.5, weight=48.0)
    g.diag(502.4, 308.5, 508.0, 318.6, weight=64.0)
    g.hbar(508.0, 641.6, 327.1, weight=64.0)
    g.hbar(515.0, 656.1, 239.9, weight=64.0)
    g.diag(381.6, 144.2, 335.2, -18.2, weight=96.0)
    g.diag(458.0, 130.7, 828.2, -72.0, weight=96.0)
    g.diag(828.2, -72.0, 749.9, 87.2, weight=96.0)
    g.dot(609.7, 122.0, w=96.0, h=118.1, slant=-14.0)
    g.hbar(760.5, 919.0, 174.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_61be() -> Glyph:
    """憾 U+61BE —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni61BE", advance=1000, unicode=0x61BE, note="憾：自动生成")
    g.diag(203.5, 464.1, 120.9, 384.2, weight=96.0)
    g.diag(120.9, 384.2, 94.4, 270.7, weight=96.0)
    g.dot(328.7, 527.9, w=96.0, h=124.8, slant=-14.0)
    g.diag(197.2, 764.9, 229.5, 510.3, weight=64.0)
    g.vbar(225.0, -57.0, 510.3, weight=64.0)
    g.diag(455.0, 576.1, 473.4, 566.1, weight=92.0)
    g.hbar(473.4, 803.1, 611.5, weight=92.0)
    g.diag(435.4, 583.1, 408.8, 491.5, weight=56.0)
    g.diag(408.8, 491.5, 340.8, 197.3, weight=56.0)
    g.diag(340.8, 197.3, 255.4, 158.6, weight=56.0)
    g.hbar(454.2, 650.6, 476.5, weight=84.0)
    g.diag(424.6, 363.0, 460.2, 333.3, weight=48.0)
    g.diag(460.2, 333.3, 490.0, 224.9, weight=48.0)
    g.diag(476.3, 343.7, 493.3, 361.2, weight=48.0)
    g.hbar(493.3, 610.9, 365.2, weight=48.0)
    g.diag(610.9, 369.3, 567.0, 283.2, weight=48.0)
    g.diag(499.2, 240.7, 513.7, 256.8, weight=48.0)
    g.hbar(513.7, 625.2, 252.1, weight=48.0)
    g.diag(570.5, 802.0, 667.1, 615.8, weight=92.0)
    g.diag(667.1, 615.8, 795.3, 380.5, weight=92.0)
    g.diag(795.3, 380.5, 817.8, 418.7, weight=92.0)
    g.diag(773.6, 590.0, 814.5, 481.7, weight=96.0)
    g.diag(814.5, 481.7, 637.3, 236.6, weight=96.0)
    g.hbar(661.7, 811.3, 729.2, weight=84.0)
    g.vbar(800.8, 647.2, 710.8, weight=84.0)
    g.diag(349.7, 174.6, 383.9, 79.8, weight=64.0)
    g.diag(383.9, 79.8, 354.2, -16.7, weight=64.0)
    g.diag(483.7, 191.0, 807.4, -84.6, weight=64.0)
    g.vbar(794.7, -84.6, 145.0, weight=64.0)
    g.diag(614.9, 205.1, 644.8, 124.3, weight=96.0)
    g.hbar(644.8, 716.7, 111.0, weight=96.0)
    g.hbar(767.7, 901.9, 117.4, weight=84.0)
    g.diag(901.9, 103.8, 817.8, 38.4, weight=84.0)
    return g
def g_cjk_unified_ideograph_61c7() -> Glyph:
    """懇 U+61C7 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni61C7", advance=1000, unicode=0x61C7, note="懇：自动生成")
    g.hbar(353.2, 460.5, 761.8, weight=96.0)
    g.diag(353.2, 779.7, 168.3, 658.9, weight=96.0)
    g.dot(189.2, 592.0, w=96.0, h=99.4, slant=-14.0)
    g.dot(312.5, 656.9, w=96.0, h=75.0, slant=-14.0)
    g.hbar(357.2, 506.0, 619.6, weight=56.0)
    g.diag(357.2, 592.4, 83.0, 450.6, weight=56.0)
    g.diag(297.8, 534.7, 501.1, 152.6, weight=96.0)
    g.diag(501.1, 152.6, 273.9, 280.9, weight=96.0)
    g.vbar(309.2, 476.0, 515.5, weight=48.0)
    g.diag(310.5, 476.0, 106.9, 330.0, weight=48.0)
    g.diag(106.9, 330.0, 110.4, 338.1, weight=48.0)
    g.diag(360.9, 455.9, 289.0, 367.9, weight=56.0)
    g.diag(289.0, 367.9, 99.2, 224.6, weight=56.0)
    g.hbar(531.9, 743.9, 723.8, weight=48.0)
    g.vbar(717.6, 540.8, 734.1, weight=48.0)
    g.hbar(669.0, 691.3, 541.1, weight=48.0)
    g.diag(556.6, 607.6, 565.0, 624.0, weight=64.0)
    g.hbar(565.0, 689.5, 623.1, weight=64.0)
    g.diag(555.3, 526.5, 568.4, 541.8, weight=48.0)
    g.hbar(568.4, 671.1, 544.8, weight=48.0)
    g.vbar(521.6, 610.9, 720.1, weight=48.0)
    g.vbar(532.8, 314.5, 610.9, weight=48.0)
    g.diag(542.5, 314.5, 675.1, 401.6, weight=48.0)
    g.diag(733.6, 548.4, 774.1, 508.4, weight=96.0)
    g.diag(774.1, 508.4, 706.2, 443.5, weight=96.0)
    g.hbar(695.1, 706.2, 443.5, weight=96.0)
    g.diag(571.7, 514.0, 917.0, 347.3, weight=48.0)
    g.diag(274.1, 136.2, 138.7, -24.6, weight=96.0)
    g.diag(263.8, 137.8, 419.8, 60.7, weight=96.0)
    g.hbar(419.8, 772.9, 3.0, weight=96.0)
    g.vbar(741.8, -54.7, 190.8, weight=96.0)
    g.hbar(417.7, 633.8, 166.3, weight=96.0)
    g.hbar(692.6, 846.6, 165.1, weight=96.0)
    g.diag(846.6, 163.8, 885.6, 109.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_61f2() -> Glyph:
    """懲 U+61F2 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni61F2", advance=1000, unicode=0x61F2, note="懲：自动生成")
    g.diag(274.1, 761.6, 294.6, 719.3, weight=84.0)
    g.diag(294.6, 719.3, 149.4, 565.0, weight=84.0)
    g.diag(318.6, 576.2, 244.6, 499.5, weight=48.0)
    g.diag(244.6, 499.5, 57.2, 301.6, weight=48.0)
    g.vbar(250.8, 212.4, 450.5, weight=48.0)
    g.diag(462.5, 792.0, 489.9, 762.6, weight=84.0)
    g.vbar(488.3, 662.3, 762.6, weight=84.0)
    g.diag(486.8, 662.3, 474.7, 654.2, weight=84.0)
    g.diag(368.3, 716.0, 387.5, 680.5, weight=56.0)
    g.vbar(386.4, 608.7, 680.5, weight=56.0)
    g.hbar(385.4, 553.2, 627.1, weight=56.0)
    g.diag(553.2, 645.5, 561.8, 655.2, weight=56.0)
    g.diag(586.1, 756.5, 604.4, 726.1, weight=76.0)
    g.diag(604.4, 726.1, 580.0, 615.7, weight=76.0)
    g.hbar(371.3, 554.7, 547.3, weight=56.0)
    g.hbar(360.2, 549.6, 470.3, weight=56.0)
    g.hbar(368.3, 541.5, 378.6, weight=64.0)
    g.diag(443.3, 441.4, 465.6, 423.2, weight=96.0)
    g.vbar(465.0, 320.9, 423.2, weight=96.0)
    g.diag(464.5, 320.9, 450.4, 298.6, weight=96.0)
    g.hbar(323.7, 370.3, 252.0, weight=76.0)
    g.hbar(370.3, 579.0, 281.3, weight=76.0)
    g.diag(688.5, 765.7, 727.7, 730.5, weight=76.0)
    g.diag(727.7, 730.5, 617.5, 507.3, weight=76.0)
    g.hbar(670.2, 885.0, 570.6, weight=84.0)
    g.diag(734.1, 534.6, 797.2, 476.2, weight=64.0)
    g.diag(797.2, 476.2, 597.3, 256.0, weight=64.0)
    g.hbar(629.7, 645.0, 455.5, weight=96.0)
    g.diag(645.0, 453.4, 834.1, 268.7, weight=96.0)
    g.hbar(834.1, 942.8, 262.3, weight=96.0)
    g.diag(231.5, 128.4, 161.6, -42.9, weight=96.0)
    g.hbar(325.7, 781.9, 33.8, weight=84.0)
    g.diag(781.9, -68.8, 664.1, 117.2, weight=84.0)
    g.dot(519.8, 138.5, w=96.0, h=124.8, slant=-14.0)
    g.diag(715.8, 194.2, 878.9, 81.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_61f8() -> Glyph:
    """懸 U+61F8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni61F8", advance=1000, unicode=0x61F8, note="懸：自动生成")
    g.vbar(245.3, 495.6, 762.3, weight=48.0)
    g.diag(254.5, 755.5, 362.6, 676.3, weight=48.0)
    g.diag(362.6, 676.3, 398.1, 466.1, weight=48.0)
    g.diag(263.4, 658.4, 276.0, 669.8, weight=56.0)
    g.hbar(276.0, 377.6, 672.3, weight=56.0)
    g.diag(260.6, 581.7, 275.4, 594.1, weight=48.0)
    g.hbar(275.4, 381.5, 596.0, weight=48.0)
    g.diag(264.6, 505.0, 272.1, 514.9, weight=56.0)
    g.hbar(272.1, 377.8, 524.7, weight=56.0)
    g.diag(118.5, 592.5, 152.9, 556.0, weight=64.0)
    g.vbar(146.0, 409.8, 556.0, weight=64.0)
    g.hbar(139.0, 525.6, 424.4, weight=64.0)
    g.diag(291.6, 416.0, 327.4, 377.9, weight=48.0)
    g.diag(327.4, 377.9, 299.4, 217.3, weight=48.0)
    g.diag(299.4, 217.3, 186.7, 275.1, weight=48.0)
    g.dot(188.5, 305.9, w=96.0, h=124.8, slant=0.0)
    g.diag(347.2, 348.6, 458.3, 271.7, weight=76.0)
    g.diag(726.5, 691.1, 745.7, 767.9, weight=96.0)
    g.hbar(515.4, 745.7, 725.0, weight=96.0)
    g.hbar(438.4, 515.4, 677.6, weight=96.0)
    g.diag(589.1, 687.9, 606.6, 667.7, weight=48.0)
    g.diag(606.6, 667.7, 521.7, 557.7, weight=48.0)
    g.hbar(521.7, 636.2, 560.5, weight=48.0)
    g.diag(708.2, 657.4, 666.1, 578.7, weight=48.0)
    g.diag(666.1, 578.7, 535.4, 434.0, weight=48.0)
    g.hbar(535.4, 732.6, 449.7, weight=48.0)
    g.hbar(715.9, 751.8, 479.9, weight=48.0)
    g.vbar(748.0, 450.5, 474.0, weight=48.0)
    g.vbar(612.4, 299.7, 430.4, weight=48.0)
    g.hbar(514.9, 604.6, 288.1, weight=48.0)
    g.diag(538.3, 404.3, 450.5, 257.3, weight=96.0)
    g.hbar(684.2, 786.3, 335.1, weight=92.0)
    g.vbar(779.3, 195.6, 312.8, weight=92.0)
    g.diag(265.5, 122.8, 185.4, 72.7, weight=96.0)
    g.diag(185.4, 72.7, 139.8, -26.6, weight=96.0)
    g.diag(299.1, 180.3, 784.5, -72.0, weight=96.0)
    g.diag(784.5, -72.0, 573.9, 92.6, weight=96.0)
    g.diag(456.0, 196.4, 518.7, 114.2, weight=96.0)
    g.hbar(518.7, 599.3, 105.3, weight=96.0)
    g.diag(794.9, 239.4, 881.5, 51.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_621a() -> Glyph:
    """戚 U+621A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni621A", advance=1000, unicode=0x621A, note="戚：自动生成")
    g.hbar(303.4, 372.4, 522.3, weight=96.0)
    g.hbar(372.4, 753.8, 572.5, weight=96.0)
    g.diag(274.2, 530.5, 235.9, 374.2, weight=76.0)
    g.diag(235.9, 374.2, 63.0, -20.9, weight=76.0)
    g.diag(393.9, 479.4, 428.0, 435.6, weight=96.0)
    g.vbar(428.0, 300.3, 435.6, weight=96.0)
    g.diag(428.0, 300.3, 414.4, 288.7, weight=96.0)
    g.diag(457.2, 369.4, 469.6, 387.4, weight=76.0)
    g.hbar(469.6, 578.6, 394.6, weight=76.0)
    g.hbar(290.1, 601.9, 274.3, weight=96.0)
    g.diag(411.3, 240.1, 437.3, 219.1, weight=48.0)
    g.vbar(427.3, 20.6, 219.1, weight=48.0)
    g.diag(417.2, 20.6, 305.6, 70.9, weight=48.0)
    g.diag(337.5, 216.9, 317.1, 63.8, weight=76.0)
    g.dot(521.5, 147.3, w=96.0, h=124.8, slant=-14.0)
    g.diag(489.4, 763.7, 617.1, 490.9, weight=96.0)
    g.diag(617.1, 490.9, 874.3, -72.0, weight=96.0)
    g.diag(874.3, -72.0, 942.0, 133.9, weight=96.0)
    g.diag(756.1, 440.5, 793.2, 394.5, weight=96.0)
    g.diag(793.2, 394.5, 568.6, 29.5, weight=96.0)
    g.hbar(466.4, 568.6, 31.9, weight=96.0)
    g.hbar(588.9, 749.3, 708.0, weight=96.0)
    g.vbar(747.5, 611.6, 690.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_6247() -> Glyph:
    """扇 U+6247 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6247", advance=1000, unicode=0x6247, note="扇：自动生成")
    g.hbar(503.5, 580.6, 739.8, weight=56.0)
    g.diag(580.6, 722.7, 618.3, 641.1, weight=56.0)
    g.hbar(401.9, 701.5, 610.0, weight=48.0)
    g.diag(701.5, 634.1, 741.8, 598.0, weight=48.0)
    g.diag(741.8, 598.0, 690.9, 520.3, weight=48.0)
    g.hbar(392.9, 723.9, 476.2, weight=48.0)
    g.vbar(725.0, 506.4, 529.5, weight=48.0)
    g.diag(382.3, 602.1, 330.0, 392.4, weight=96.0)
    g.diag(330.0, 392.4, 141.4, -34.8, weight=96.0)
    g.hbar(384.9, 558.0, 336.7, weight=76.0)
    g.vbar(540.5, -32.7, 335.7, weight=76.0)
    g.diag(523.1, -32.7, 394.9, 55.6, weight=76.0)
    g.diag(363.8, 270.1, 466.3, 183.1, weight=76.0)
    g.hbar(285.4, 364.3, 80.0, weight=84.0)
    g.diag(364.3, 70.9, 507.2, 161.7, weight=84.0)
    g.diag(638.0, 313.1, 665.1, 368.6, weight=96.0)
    g.hbar(665.1, 849.6, 373.6, weight=96.0)
    g.diag(849.6, 378.6, 795.6, -53.7, weight=96.0)
    g.diag(795.6, -53.7, 667.1, 49.4, weight=96.0)
    g.diag(645.5, 334.1, 729.8, 196.7, weight=76.0)
    g.diag(580.3, 74.6, 778.8, 185.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_6249() -> Glyph:
    """扉 U+6249 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6249", advance=1000, unicode=0x6249, note="扉：自动生成")
    g.diag(498.9, 757.0, 588.4, 699.4, weight=56.0)
    g.diag(390.2, 577.0, 401.2, 590.7, weight=48.0)
    g.hbar(401.2, 656.5, 615.6, weight=48.0)
    g.diag(656.5, 640.5, 696.0, 605.9, weight=48.0)
    g.diag(696.0, 605.9, 674.3, 562.4, weight=48.0)
    g.diag(674.3, 562.4, 644.2, 546.9, weight=48.0)
    g.hbar(371.0, 703.5, 488.0, weight=48.0)
    g.diag(320.8, 624.5, 116.2, -19.5, weight=96.0)
    g.vbar(482.0, -35.9, 415.3, weight=96.0)
    g.hbar(360.1, 464.5, 317.0, weight=96.0)
    g.diag(464.5, 316.4, 477.9, 327.6, weight=96.0)
    g.hbar(352.8, 460.7, 205.2, weight=76.0)
    g.diag(460.7, 206.1, 477.9, 224.4, weight=76.0)
    g.hbar(287.9, 461.5, 86.5, weight=64.0)
    g.diag(461.5, 108.5, 468.8, 123.9, weight=64.0)
    g.diag(597.6, 449.1, 638.7, 407.1, weight=96.0)
    g.vbar(636.4, -67.0, 407.1, weight=96.0)
    g.dot(731.4, 354.1, w=92.0, h=119.6, slant=-14.0)
    g.dot(730.0, 243.1, w=92.0, h=119.6, slant=-14.0)
    g.hbar(661.5, 858.8, 113.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_62f3() -> Glyph:
    """拳 U+62F3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni62F3", advance=1000, unicode=0x62F3, note="拳：自动生成")
    g.diag(281.6, 592.1, 331.3, 654.8, weight=96.0)
    g.diag(331.3, 654.8, 340.0, 586.6, weight=96.0)
    g.diag(612.5, 756.7, 626.8, 725.3, weight=64.0)
    g.diag(626.8, 725.3, 549.7, 610.3, weight=64.0)
    g.diag(324.1, 606.2, 350.2, 545.3, weight=84.0)
    g.hbar(350.2, 581.0, 567.7, weight=84.0)
    g.vbar(583.0, 590.0, 648.1, weight=84.0)
    g.hbar(175.0, 756.4, 446.0, weight=48.0)
    g.diag(435.2, 757.7, 368.3, 555.7, weight=48.0)
    g.diag(368.3, 555.7, 73.0, 183.9, weight=48.0)
    g.diag(538.6, 447.0, 927.0, 225.9, weight=48.0)
    g.hbar(304.6, 590.8, 340.8, weight=48.0)
    g.diag(326.1, 261.3, 351.2, 207.8, weight=64.0)
    g.hbar(351.2, 605.8, 226.9, weight=64.0)
    g.hbar(198.8, 743.0, 118.1, weight=76.0)
    g.diag(445.7, 302.1, 533.1, 239.3, weight=96.0)
    g.diag(533.1, 239.3, 443.3, -34.2, weight=96.0)
    g.diag(443.3, -34.2, 335.4, 70.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_6328() -> Glyph:
    """挨 U+6328 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6328", advance=1000, unicode=0x6328, note="挨：自动生成")
    g.hbar(173.0, 493.4, 490.7, weight=96.0)
    g.vbar(306.9, 491.4, 746.4, weight=96.0)
    g.vbar(314.0, 25.4, 491.4, weight=96.0)
    g.hbar(203.0, 309.2, 47.9, weight=96.0)
    g.hbar(201.8, 203.0, 70.5, weight=96.0)
    g.hbar(73.0, 123.1, 192.3, weight=56.0)
    g.diag(123.1, 188.1, 347.3, 368.6, weight=56.0)
    g.diag(607.6, 729.1, 636.0, 694.1, weight=48.0)
    g.diag(636.0, 694.1, 525.2, 502.2, weight=48.0)
    g.hbar(525.2, 755.7, 522.8, weight=48.0)
    g.diag(712.4, 610.9, 785.5, 541.6, weight=48.0)
    g.diag(785.5, 541.6, 760.1, 521.1, weight=48.0)
    g.diag(565.8, 381.5, 536.1, 410.4, weight=48.0)
    g.diag(536.1, 410.4, 434.5, 300.3, weight=48.0)
    g.hbar(523.9, 776.8, 379.1, weight=48.0)
    g.hbar(397.0, 875.8, 220.5, weight=48.0)
    g.diag(577.8, 337.8, 561.3, 220.0, weight=64.0)
    g.diag(561.3, 220.0, 407.6, 4.2, weight=64.0)
    g.diag(617.9, 201.3, 688.7, 142.8, weight=48.0)
    g.diag(688.7, 142.8, 947.0, -6.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_632b() -> Glyph:
    """挫 U+632B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni632B", advance=1000, unicode=0x632B, note="挫：自动生成")
    g.hbar(149.9, 479.6, 483.3, weight=96.0)
    g.vbar(293.9, 475.9, 736.3, weight=96.0)
    g.vbar(303.1, -16.9, 475.9, weight=96.0)
    g.diag(299.2, -16.9, 147.6, 114.7, weight=96.0)
    g.hbar(78.0, 179.0, 171.2, weight=48.0)
    g.diag(179.0, 191.2, 433.1, 340.2, weight=48.0)
    g.diag(511.4, 539.3, 541.9, 506.7, weight=48.0)
    g.diag(541.9, 506.7, 476.7, 358.7, weight=48.0)
    g.hbar(399.5, 476.7, 344.1, weight=48.0)
    g.dot(560.1, 331.8, w=92.0, h=119.6, slant=-14.0)
    g.diag(783.3, 569.9, 820.0, 532.2, weight=48.0)
    g.diag(820.0, 532.2, 740.1, 366.9, weight=48.0)
    g.hbar(675.5, 740.1, 354.6, weight=48.0)
    g.diag(795.1, 408.3, 855.5, 381.0, weight=96.0)
    g.diag(855.5, 381.0, 834.4, 265.4, weight=96.0)
    g.vbar(547.3, 185.3, 274.2, weight=96.0)
    g.hbar(542.4, 861.3, 246.6, weight=96.0)
    g.diag(620.8, 706.8, 650.3, 530.6, weight=64.0)
    g.vbar(649.8, 87.2, 530.6, weight=64.0)
    g.diag(649.4, 87.2, 629.7, 67.5, weight=64.0)
    g.hbar(352.2, 937.0, 41.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_6349() -> Glyph:
    """捉 U+6349 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6349", advance=1000, unicode=0x6349, note="捉：自动生成")
    g.hbar(156.2, 402.3, 478.7, weight=96.0)
    g.hbar(356.9, 402.3, 505.2, weight=96.0)
    g.vbar(296.3, 461.9, 710.9, weight=48.0)
    g.vbar(304.4, -3.2, 461.9, weight=48.0)
    g.hbar(184.2, 300.3, 19.9, weight=48.0)
    g.diag(88.0, 192.5, 352.4, 376.5, weight=96.0)
    g.diag(514.3, 601.3, 504.8, 584.1, weight=48.0)
    g.vbar(527.5, 415.0, 584.1, weight=48.0)
    g.hbar(519.9, 776.2, 601.9, weight=48.0)
    g.diag(776.2, 611.6, 711.9, 486.3, weight=48.0)
    g.hbar(562.5, 743.0, 450.6, weight=48.0)
    g.vbar(743.6, 471.4, 492.1, weight=48.0)
    g.diag(605.4, 430.7, 628.8, 324.8, weight=48.0)
    g.vbar(636.4, 133.0, 324.8, weight=48.0)
    g.dot(732.9, 299.0, w=96.0, h=124.8, slant=-14.0)
    g.diag(474.7, 327.9, 450.2, 232.3, weight=48.0)
    g.diag(450.2, 232.3, 333.2, 53.3, weight=48.0)
    g.vbar(506.0, 181.8, 217.7, weight=96.0)
    g.hbar(509.2, 937.0, 107.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_636e() -> Glyph:
    """据 U+636E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni636E", advance=1000, unicode=0x636E, note="据：自动生成")
    g.hbar(137.0, 388.4, 523.5, weight=96.0)
    g.hbar(339.8, 388.4, 541.4, weight=96.0)
    g.vbar(277.5, 489.2, 728.2, weight=48.0)
    g.vbar(285.4, 48.0, 489.2, weight=48.0)
    g.hbar(165.1, 280.7, 73.0, weight=48.0)
    g.hbar(78.0, 125.4, 233.8, weight=96.0)
    g.diag(125.4, 230.1, 334.2, 409.8, weight=96.0)
    g.hbar(524.5, 789.7, 644.3, weight=48.0)
    g.diag(789.7, 658.8, 731.8, 556.2, weight=48.0)
    g.hbar(522.0, 765.3, 516.5, weight=48.0)
    g.vbar(765.6, 541.7, 564.9, weight=48.0)
    g.vbar(505.9, 502.1, 644.7, weight=48.0)
    g.vbar(432.2, 80.8, 502.1, weight=48.0)
    g.hbar(304.9, 378.4, 73.4, weight=48.0)
    g.hbar(506.8, 922.0, 330.9, weight=96.0)
    g.diag(636.7, 481.4, 674.2, 428.2, weight=92.0)
    g.vbar(664.1, 222.0, 428.2, weight=92.0)
    g.diag(653.9, 222.0, 636.5, 197.8, weight=92.0)
    g.diag(548.7, 180.5, 539.1, 162.8, weight=48.0)
    g.vbar(563.8, 8.7, 162.8, weight=48.0)
    g.hbar(555.4, 827.2, 180.6, weight=48.0)
    g.diag(827.2, 189.7, 757.5, 62.1, weight=48.0)
    g.diag(582.8, 32.8, 600.0, 23.9, weight=48.0)
    g.hbar(600.0, 794.2, 34.3, weight=48.0)
    g.vbar(794.0, 44.7, 70.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_637b() -> Glyph:
    """捻 U+637B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni637B", advance=1000, unicode=0x637B, note="捻：自动生成")
    g.hbar(138.9, 328.9, 468.2, weight=96.0)
    g.vbar(329.7, 489.1, 496.1, weight=96.0)
    g.vbar(273.9, 483.4, 714.8, weight=64.0)
    g.vbar(279.9, 26.4, 483.4, weight=64.0)
    g.diag(274.4, 26.4, 174.2, 73.0, weight=64.0)
    g.hbar(73.0, 168.3, 214.5, weight=48.0)
    g.diag(168.3, 234.3, 366.9, 356.7, weight=48.0)
    g.diag(549.5, 731.5, 530.6, 613.2, weight=48.0)
    g.diag(530.6, 613.2, 401.2, 357.6, weight=48.0)
    g.hbar(345.2, 401.2, 352.3, weight=48.0)
    g.vbar(593.4, 576.8, 621.0, weight=96.0)
    g.diag(594.7, 576.8, 947.0, 396.2, weight=96.0)
    g.diag(503.6, 472.5, 577.3, 435.2, weight=64.0)
    g.diag(577.3, 435.2, 619.2, 362.2, weight=64.0)
    g.hbar(449.2, 545.4, 300.3, weight=48.0)
    g.hbar(545.4, 697.4, 323.3, weight=48.0)
    g.diag(697.4, 340.0, 585.9, 185.0, weight=48.0)
    g.diag(444.3, 158.8, 307.9, 50.0, weight=64.0)
    g.diag(441.1, 154.7, 532.6, 90.9, weight=96.0)
    g.diag(532.6, 90.9, 838.5, -61.4, weight=96.0)
    g.diag(838.5, -61.4, 663.0, 117.1, weight=96.0)
    g.diag(565.3, 177.0, 612.6, 138.9, weight=92.0)
    g.diag(612.6, 138.9, 607.1, 159.2, weight=92.0)
    g.diag(681.1, 268.7, 858.8, 137.1, weight=64.0)
    return g
def g_cjk_unified_ideograph_638c() -> Glyph:
    """掌 U+638C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni638C", advance=1000, unicode=0x638C, note="掌：自动生成")
    g.diag(461.2, 793.0, 498.0, 758.2, weight=84.0)
    g.vbar(496.0, 627.0, 758.2, weight=84.0)
    g.diag(494.0, 627.0, 478.1, 616.0, weight=84.0)
    g.diag(313.1, 714.5, 362.8, 675.7, weight=56.0)
    g.diag(362.8, 675.7, 393.2, 597.1, weight=56.0)
    g.diag(681.0, 778.1, 690.9, 741.3, weight=84.0)
    g.diag(690.9, 741.3, 591.8, 641.7, weight=84.0)
    g.diag(213.5, 587.8, 158.0, 413.2, weight=84.0)
    g.hbar(226.8, 839.6, 589.6, weight=48.0)
    g.diag(839.6, 612.9, 737.6, 497.7, weight=48.0)
    g.diag(343.2, 530.7, 405.5, 388.3, weight=84.0)
    g.hbar(390.4, 634.2, 520.0, weight=48.0)
    g.diag(634.2, 533.8, 577.9, 449.4, weight=48.0)
    g.hbar(421.5, 606.6, 415.3, weight=48.0)
    g.vbar(607.6, 433.4, 456.7, weight=48.0)
    g.hbar(493.9, 600.4, 336.3, weight=48.0)
    g.hbar(351.2, 493.9, 306.4, weight=48.0)
    g.vbar(346.6, 231.6, 283.7, weight=48.0)
    g.vbar(330.5, 209.4, 261.3, weight=64.0)
    g.hbar(331.0, 666.0, 232.3, weight=64.0)
    g.hbar(149.0, 851.0, 113.4, weight=84.0)
    g.vbar(544.9, -78.0, 298.9, weight=84.0)
    g.hbar(374.7, 612.7, -54.1, weight=84.0)
    return g
def g_cjk_unified_ideograph_63da() -> Glyph:
    """揚 U+63DA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni63DA", advance=1000, unicode=0x63DA, note="揚：自动生成")
    g.hbar(132.9, 352.8, 497.5, weight=92.0)
    g.diag(352.8, 520.2, 339.3, 528.4, weight=92.0)
    g.vbar(275.9, 514.8, 745.6, weight=92.0)
    g.vbar(285.0, 36.8, 514.8, weight=92.0)
    g.diag(280.6, 36.8, 188.0, 85.0, weight=92.0)
    g.diag(188.0, 85.0, 133.0, 159.3, weight=92.0)
    g.hbar(71.0, 112.2, 191.5, weight=92.0)
    g.diag(112.2, 190.6, 390.2, 397.6, weight=92.0)
    g.vbar(530.3, 478.3, 717.1, weight=48.0)
    g.hbar(520.4, 682.7, 684.3, weight=48.0)
    g.vbar(692.3, 498.8, 654.5, weight=48.0)
    g.hbar(675.9, 702.0, 500.8, weight=48.0)
    g.diag(563.3, 594.6, 574.1, 611.2, weight=76.0)
    g.hbar(574.1, 697.2, 608.3, weight=76.0)
    g.diag(572.0, 489.3, 579.7, 501.0, weight=84.0)
    g.hbar(579.7, 674.5, 511.6, weight=84.0)
    g.hbar(416.2, 924.0, 396.0, weight=92.0)
    g.diag(489.8, 349.1, 508.5, 326.2, weight=76.0)
    g.diag(508.5, 326.2, 430.5, 224.0, weight=76.0)
    g.hbar(328.6, 430.5, 206.9, weight=76.0)
    g.hbar(501.4, 735.5, 220.7, weight=92.0)
    g.vbar(731.2, -56.5, 171.6, weight=92.0)
    g.diag(726.8, -56.5, 597.6, 33.2, weight=92.0)
    g.diag(543.9, 257.2, 569.2, 230.7, weight=56.0)
    g.diag(569.2, 230.7, 415.8, 68.5, weight=56.0)
    g.diag(415.8, 68.5, 422.1, 84.1, weight=56.0)
    g.diag(667.7, 278.5, 700.9, 235.6, weight=92.0)
    g.diag(700.9, 235.6, 519.1, 1.6, weight=92.0)
    g.diag(519.1, 1.6, 430.1, 48.2, weight=92.0)
    return g
def g_cjk_unified_ideograph_642c() -> Glyph:
    """搬 U+642C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni642C", advance=1000, unicode=0x642C, note="搬：自动生成")
    g.hbar(105.5, 347.2, 492.6, weight=92.0)
    g.vbar(230.1, 477.9, 719.6, weight=48.0)
    g.vbar(239.0, 29.7, 477.9, weight=48.0)
    g.hbar(130.2, 235.2, 52.2, weight=48.0)
    g.hbar(58.0, 99.8, 233.8, weight=84.0)
    g.diag(99.8, 233.3, 282.6, 402.3, weight=84.0)
    g.diag(466.4, 720.6, 492.3, 695.6, weight=48.0)
    g.diag(492.3, 695.6, 429.0, 564.0, weight=48.0)
    g.hbar(419.9, 429.0, 563.5, weight=48.0)
    g.vbar(395.9, 444.0, 547.8, weight=48.0)
    g.diag(390.8, 444.0, 349.5, 108.2, weight=48.0)
    g.diag(349.5, 108.2, 249.8, 28.1, weight=48.0)
    g.diag(419.9, 544.9, 505.7, 386.9, weight=48.0)
    g.vbar(511.2, 50.0, 386.9, weight=48.0)
    g.diag(516.7, 50.0, 434.1, 88.0, weight=48.0)
    g.hbar(424.2, 513.7, 431.0, weight=48.0)
    g.hbar(268.4, 513.7, 332.5, weight=48.0)
    g.diag(416.3, 281.0, 513.7, 232.4, weight=48.0)
    g.hbar(643.6, 649.6, 594.1, weight=48.0)
    g.diag(643.6, 593.9, 606.2, 392.0, weight=48.0)
    g.diag(606.2, 392.0, 552.1, 356.8, weight=48.0)
    g.diag(664.9, 581.9, 675.2, 602.6, weight=96.0)
    g.hbar(675.2, 797.9, 614.7, weight=96.0)
    g.vbar(770.4, 438.1, 626.9, weight=96.0)
    g.hbar(743.0, 906.2, 430.2, weight=96.0)
    g.hbar(594.3, 648.4, 326.6, weight=64.0)
    g.diag(648.4, 317.2, 714.8, 252.1, weight=64.0)
    g.diag(714.8, 252.1, 556.9, 69.6, weight=64.0)
    g.diag(606.4, 272.4, 823.8, 29.1, weight=96.0)
    g.hbar(823.8, 947.0, 20.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_642d() -> Glyph:
    """搭 U+642D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni642D", advance=1000, unicode=0x642D, note="搭：自动生成")
    g.hbar(123.5, 383.1, 518.9, weight=56.0)
    g.vbar(263.9, 491.1, 746.0, weight=84.0)
    g.vbar(274.8, 25.8, 491.1, weight=84.0)
    g.diag(272.3, 25.8, 171.7, 71.2, weight=84.0)
    g.hbar(169.9, 171.7, 71.2, weight=84.0)
    g.hbar(78.0, 130.6, 221.3, weight=96.0)
    g.diag(130.6, 219.8, 324.0, 390.1, weight=96.0)
    g.diag(378.6, 553.5, 404.0, 580.2, weight=96.0)
    g.hbar(404.0, 813.4, 593.4, weight=96.0)
    g.diag(477.7, 622.3, 497.8, 657.8, weight=96.0)
    g.diag(497.8, 657.8, 513.7, 551.3, weight=96.0)
    g.vbar(670.2, 649.8, 677.8, weight=96.0)
    g.diag(670.5, 677.8, 616.8, 508.8, weight=96.0)
    g.diag(590.3, 467.6, 513.6, 394.8, weight=48.0)
    g.diag(513.6, 394.8, 307.1, 196.7, weight=48.0)
    g.diag(589.7, 448.4, 947.0, 264.5, weight=76.0)
    g.hbar(461.4, 528.2, 268.4, weight=48.0)
    g.hbar(528.2, 661.8, 269.2, weight=48.0)
    g.diag(455.2, 168.5, 502.5, -19.7, weight=96.0)
    g.hbar(482.9, 692.7, 176.3, weight=48.0)
    g.diag(692.7, 202.4, 729.7, 164.3, weight=48.0)
    g.diag(729.7, 164.3, 676.0, 61.0, weight=48.0)
    g.diag(515.8, 8.0, 531.2, 22.0, weight=48.0)
    g.hbar(531.2, 711.0, 33.2, weight=48.0)
    g.vbar(711.0, 44.3, 71.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_6458() -> Glyph:
    """摘 U+6458 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6458", advance=1000, unicode=0x6458, note="摘：自动生成")
    g.hbar(155.4, 462.9, 515.2, weight=96.0)
    g.vbar(313.6, 495.2, 780.1, weight=96.0)
    g.vbar(321.4, -19.0, 495.2, weight=96.0)
    g.diag(315.9, -19.0, 193.3, 48.5, weight=96.0)
    g.hbar(191.4, 193.3, 48.6, weight=96.0)
    g.diag(74.1, 186.1, 423.8, 386.6, weight=96.0)
    g.diag(641.6, 797.0, 729.4, 745.2, weight=96.0)
    g.diag(729.4, 745.2, 762.1, 656.3, weight=96.0)
    g.hbar(471.6, 925.9, 597.4, weight=96.0)
    g.diag(547.6, 557.0, 613.8, 411.0, weight=48.0)
    g.diag(757.9, 587.7, 787.2, 549.2, weight=96.0)
    g.diag(787.2, 549.2, 709.3, 428.1, weight=96.0)
    g.diag(423.4, 386.5, 471.6, 292.4, weight=48.0)
    g.vbar(469.4, -33.7, 292.4, weight=48.0)
    g.hbar(506.2, 874.2, 411.2, weight=48.0)
    g.diag(874.2, 442.2, 900.8, 257.1, weight=48.0)
    g.vbar(896.8, -60.0, 257.1, weight=48.0)
    g.hbar(771.6, 892.7, -36.8, weight=48.0)
    g.hbar(528.1, 880.7, 284.0, weight=76.0)
    g.diag(650.7, 379.5, 684.5, 325.6, weight=48.0)
    g.diag(684.5, 325.6, 654.9, 193.1, weight=48.0)
    g.vbar(605.3, 40.1, 172.8, weight=48.0)
    g.hbar(595.6, 781.8, 172.8, weight=48.0)
    g.diag(781.8, 180.5, 735.7, 88.6, weight=48.0)
    g.hbar(626.2, 642.4, 56.8, weight=48.0)
    g.hbar(642.4, 755.4, 70.1, weight=48.0)
    return g
def g_cjk_unified_ideograph_6469() -> Glyph:
    """摩 U+6469 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6469", advance=1000, unicode=0x6469, note="摩：自动生成")
    g.diag(479.8, 792.0, 571.2, 730.7, weight=48.0)
    g.hbar(335.8, 776.5, 681.1, weight=92.0)
    g.vbar(259.5, 463.2, 680.1, weight=56.0)
    g.diag(250.3, 463.2, 89.7, 6.9, weight=56.0)
    g.hbar(352.3, 540.1, 524.0, weight=48.0)
    g.diag(438.9, 613.0, 482.9, 557.5, weight=48.0)
    g.vbar(472.1, 357.1, 557.5, weight=48.0)
    g.diag(439.9, 494.3, 329.0, 356.2, weight=48.0)
    g.dot(519.2, 453.0, w=48.0, h=52.4, slant=-14.0)
    g.hbar(585.8, 789.1, 560.5, weight=48.0)
    g.diag(662.7, 648.0, 697.5, 610.7, weight=48.0)
    g.vbar(692.2, 384.4, 610.7, weight=48.0)
    g.diag(664.6, 527.4, 698.2, 556.8, weight=48.0)
    g.diag(698.2, 556.8, 570.3, 406.8, weight=48.0)
    g.diag(708.4, 534.2, 890.3, 429.1, weight=48.0)
    g.hbar(624.1, 673.4, 358.7, weight=48.0)
    g.hbar(387.6, 624.1, 322.6, weight=48.0)
    g.diag(387.6, 280.2, 398.1, 286.1, weight=48.0)
    g.hbar(393.2, 740.5, 232.6, weight=76.0)
    g.hbar(261.9, 886.4, 113.5, weight=76.0)
    g.diag(541.1, 306.6, 660.6, 229.7, weight=96.0)
    g.diag(660.6, 229.7, 518.0, -50.8, weight=96.0)
    g.hbar(447.7, 518.0, -36.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_646f() -> Glyph:
    """摯 U+646F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni646F", advance=1000, unicode=0x646F, note="摯：自动生成")
    g.hbar(242.9, 461.4, 698.7, weight=64.0)
    g.diag(350.3, 787.0, 382.6, 756.6, weight=96.0)
    g.vbar(380.2, 654.0, 756.6, weight=96.0)
    g.diag(377.8, 654.0, 364.5, 636.0, weight=96.0)
    g.hbar(133.7, 472.8, 598.0, weight=64.0)
    g.hbar(277.1, 285.4, 559.6, weight=96.0)
    g.diag(285.4, 559.1, 299.9, 509.6, weight=96.0)
    g.diag(395.9, 599.9, 410.1, 581.8, weight=76.0)
    g.diag(410.1, 581.8, 385.4, 539.1, weight=76.0)
    g.hbar(245.8, 453.8, 499.6, weight=56.0)
    g.hbar(151.7, 451.9, 416.0, weight=56.0)
    g.diag(335.1, 480.2, 355.0, 463.1, weight=96.0)
    g.vbar(354.1, 286.4, 463.1, weight=96.0)
    g.diag(569.7, 780.4, 638.3, 727.9, weight=96.0)
    g.diag(638.3, 727.9, 499.2, 391.1, weight=96.0)
    g.hbar(471.9, 499.2, 388.6, weight=96.0)
    g.hbar(513.7, 693.9, 608.8, weight=56.0)
    g.diag(693.9, 575.0, 858.2, 367.9, weight=56.0)
    g.diag(858.2, 367.9, 881.3, 504.9, weight=56.0)
    g.diag(511.8, 557.1, 655.2, 469.7, weight=56.0)
    g.hbar(599.6, 632.4, 364.7, weight=64.0)
    g.hbar(400.6, 599.6, 331.9, weight=64.0)
    g.hbar(358.8, 660.9, 244.6, weight=64.0)
    g.hbar(169.8, 840.5, 129.6, weight=76.0)
    g.diag(484.2, 294.9, 510.3, 186.1, weight=84.0)
    g.diag(510.3, 186.1, 608.9, -78.0, weight=84.0)
    g.hbar(412.0, 608.9, -53.0, weight=84.0)
    return g
def g_cjk_unified_ideograph_64a4() -> Glyph:
    """撤 U+64A4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni64A4", advance=1000, unicode=0x64A4, note="撤：自动生成")
    g.hbar(113.2, 350.5, 499.1, weight=96.0)
    g.diag(233.4, 727.3, 260.0, 524.7, weight=96.0)
    g.vbar(254.4, 31.8, 524.7, weight=96.0)
    g.diag(248.8, 31.8, 162.6, 74.0, weight=96.0)
    g.diag(162.6, 74.0, 122.9, 152.8, weight=96.0)
    g.diag(125.5, 114.4, 108.1, 194.3, weight=96.0)
    g.diag(108.1, 194.3, 345.7, 370.7, weight=96.0)
    g.diag(446.0, 733.0, 506.5, 696.5, weight=96.0)
    g.diag(506.5, 696.5, 537.5, 627.7, weight=96.0)
    g.hbar(367.3, 542.1, 571.9, weight=96.0)
    g.diag(542.1, 587.2, 559.8, 634.9, weight=96.0)
    g.diag(482.6, 552.6, 479.9, 540.0, weight=48.0)
    g.diag(479.9, 540.0, 399.4, 410.0, weight=48.0)
    g.hbar(399.4, 555.8, 430.5, weight=48.0)
    g.diag(506.8, 521.3, 573.9, 459.0, weight=48.0)
    g.diag(573.9, 459.0, 563.0, 438.9, weight=48.0)
    g.diag(401.8, 340.8, 391.9, 259.9, weight=48.0)
    g.vbar(380.0, 14.6, 259.9, weight=48.0)
    g.diag(408.6, 332.3, 510.8, 248.9, weight=48.0)
    g.vbar(516.6, 10.7, 248.9, weight=48.0)
    g.hbar(471.9, 522.3, 20.8, weight=48.0)
    g.hbar(417.1, 524.8, 244.3, weight=56.0)
    g.hbar(413.3, 526.1, 159.2, weight=64.0)
    g.diag(626.9, 622.7, 746.1, 699.9, weight=96.0)
    g.diag(746.1, 699.9, 604.1, 353.8, weight=96.0)
    g.hbar(663.3, 859.5, 451.3, weight=96.0)
    g.vbar(706.2, 286.6, 416.5, weight=48.0)
    g.diag(699.9, 286.6, 570.0, 54.3, weight=48.0)
    g.diag(567.0, 317.2, 695.6, 209.1, weight=48.0)
    g.diag(695.6, 209.1, 947.0, 22.3, weight=48.0)
    return g
def g_cjk_unified_ideograph_64ae() -> Glyph:
    """撮 U+64AE —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni64AE", advance=1000, unicode=0x64AE, note="撮：自动生成")
    g.hbar(132.4, 357.7, 501.5, weight=96.0)
    g.hbar(332.2, 357.7, 528.4, weight=96.0)
    g.diag(260.1, 757.4, 286.9, 542.5, weight=96.0)
    g.vbar(281.2, 29.3, 542.5, weight=96.0)
    g.diag(275.4, 29.3, 127.6, 172.2, weight=96.0)
    g.hbar(68.0, 109.7, 207.0, weight=96.0)
    g.diag(109.7, 207.0, 344.7, 401.0, weight=96.0)
    g.vbar(493.7, 498.6, 696.3, weight=48.0)
    g.hbar(479.4, 777.6, 694.3, weight=48.0)
    g.vbar(743.3, 519.3, 694.0, weight=48.0)
    g.diag(523.6, 587.6, 537.3, 601.3, weight=64.0)
    g.hbar(537.3, 716.1, 596.4, weight=64.0)
    g.diag(533.9, 515.3, 540.3, 511.8, weight=64.0)
    g.hbar(540.3, 697.6, 523.1, weight=64.0)
    g.hbar(384.1, 873.0, 414.8, weight=76.0)
    g.diag(404.2, 375.1, 430.9, 352.4, weight=96.0)
    g.vbar(429.9, 132.8, 352.4, weight=96.0)
    g.diag(428.8, 132.8, 415.8, 124.3, weight=96.0)
    g.vbar(552.4, 251.1, 398.1, weight=48.0)
    g.vbar(564.4, -52.4, 251.1, weight=48.0)
    g.dot(496.9, 293.2, w=64.0, h=83.2, slant=-14.0)
    g.diag(452.3, 199.3, 462.7, 214.4, weight=64.0)
    g.hbar(462.7, 538.0, 215.3, weight=64.0)
    g.hbar(328.1, 389.8, 85.2, weight=84.0)
    g.hbar(389.8, 644.9, 133.2, weight=84.0)
    g.diag(584.7, 320.1, 694.7, 238.3, weight=48.0)
    g.diag(694.7, 238.3, 579.8, 57.3, weight=48.0)
    g.diag(602.8, 261.8, 947.0, 39.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_64b2() -> Glyph:
    """撲 U+64B2 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni64B2", advance=1000, unicode=0x64B2, note="撲：自动生成")
    g.hbar(157.2, 384.4, 473.1, weight=96.0)
    g.vbar(285.7, 459.5, 705.8, weight=96.0)
    g.vbar(296.0, 0.0, 459.5, weight=96.0)
    g.diag(293.0, 0.0, 187.7, 51.5, weight=96.0)
    g.hbar(185.5, 187.7, 51.5, weight=96.0)
    g.hbar(73.0, 117.4, 187.2, weight=96.0)
    g.diag(117.4, 184.8, 345.0, 367.0, weight=96.0)
    g.diag(526.9, 671.8, 561.9, 633.0, weight=76.0)
    g.vbar(563.3, 513.9, 633.0, weight=76.0)
    g.diag(564.7, 513.9, 553.4, 506.3, weight=76.0)
    g.diag(649.8, 754.0, 685.4, 718.7, weight=56.0)
    g.vbar(677.2, 536.0, 718.7, weight=56.0)
    g.diag(669.0, 536.0, 653.6, 519.5, weight=56.0)
    g.diag(425.7, 597.1, 472.0, 565.9, weight=64.0)
    g.diag(472.0, 565.9, 494.8, 494.3, weight=64.0)
    g.diag(796.4, 684.1, 809.6, 651.9, weight=48.0)
    g.diag(809.6, 651.9, 693.9, 586.1, weight=48.0)
    g.hbar(410.3, 895.7, 488.0, weight=96.0)
    g.dot(525.9, 408.9, w=96.0, h=70.9, slant=-14.0)
    g.diag(674.4, 480.8, 694.4, 453.3, weight=64.0)
    g.diag(694.4, 453.3, 640.4, 379.6, weight=64.0)
    g.diag(527.4, 372.3, 507.2, 338.3, weight=64.0)
    g.hbar(507.2, 741.3, 358.4, weight=64.0)
    g.vbar(745.1, 312.2, 378.4, weight=64.0)
    g.diag(497.3, 199.0, 541.4, 259.0, weight=56.0)
    g.hbar(541.4, 724.6, 276.7, weight=56.0)
    g.diag(724.6, 294.4, 752.9, 234.9, weight=56.0)
    g.hbar(400.2, 867.3, 188.6, weight=48.0)
    g.diag(570.4, 327.6, 632.3, 282.0, weight=92.0)
    g.diag(632.3, 282.0, 457.0, -26.0, weight=92.0)
    g.hbar(325.6, 457.0, -14.4, weight=92.0)
    g.diag(618.8, 177.2, 798.9, -18.6, weight=48.0)
    g.hbar(798.9, 942.0, -31.3, weight=48.0)
    return g
def g_cjk_unified_ideograph_64c1() -> Glyph:
    """擁 U+64C1 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni64C1", advance=1000, unicode=0x64C1, note="擁：自动生成")
    g.hbar(109.5, 372.5, 491.8, weight=96.0)
    g.diag(241.7, 744.2, 269.7, 522.0, weight=96.0)
    g.vbar(265.8, 22.8, 522.0, weight=96.0)
    g.diag(261.8, 22.8, 133.9, 167.3, weight=96.0)
    g.hbar(68.0, 116.1, 201.4, weight=96.0)
    g.diag(116.1, 201.4, 351.6, 376.4, weight=96.0)
    g.diag(563.6, 758.3, 646.6, 717.8, weight=76.0)
    g.diag(646.6, 717.8, 682.4, 622.5, weight=76.0)
    g.hbar(406.9, 884.5, 569.0, weight=96.0)
    g.diag(439.2, 528.9, 464.1, 497.1, weight=48.0)
    g.diag(464.1, 497.1, 382.0, 350.1, weight=48.0)
    g.hbar(382.0, 481.6, 355.8, weight=48.0)
    g.diag(512.6, 432.7, 527.3, 399.4, weight=48.0)
    g.diag(527.3, 399.4, 397.2, 202.6, weight=48.0)
    g.hbar(397.2, 512.4, 215.2, weight=48.0)
    g.vbar(492.2, 205.4, 309.3, weight=48.0)
    g.diag(493.8, 205.4, 363.5, -10.0, weight=48.0)
    g.diag(640.0, 566.7, 669.0, 505.0, weight=48.0)
    g.diag(669.0, 505.0, 590.7, 338.3, weight=48.0)
    g.vbar(615.5, -38.3, 362.6, weight=48.0)
    g.diag(706.4, 511.7, 780.7, 478.0, weight=96.0)
    g.diag(780.7, 478.0, 800.6, 433.3, weight=96.0)
    g.hbar(639.7, 830.6, 383.2, weight=76.0)
    g.vbar(825.0, 398.8, 436.6, weight=76.0)
    g.hbar(651.4, 822.2, 286.3, weight=64.0)
    g.vbar(829.1, 239.5, 301.5, weight=64.0)
    g.hbar(652.0, 830.0, 200.9, weight=64.0)
    g.vbar(839.8, 215.2, 271.2, weight=64.0)
    g.diag(733.5, 352.4, 766.2, 333.0, weight=96.0)
    g.vbar(757.5, 115.3, 333.0, weight=96.0)
    g.diag(748.7, 115.3, 745.8, 111.7, weight=96.0)
    g.diag(654.2, 82.5, 659.6, 74.9, weight=96.0)
    g.hbar(659.6, 904.2, 92.5, weight=96.0)
    g.diag(904.2, 110.2, 871.1, 178.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_64cd() -> Glyph:
    """操 U+64CD —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni64CD", advance=1000, unicode=0x64CD, note="操：自动生成")
    g.hbar(136.1, 351.5, 538.2, weight=96.0)
    g.hbar(351.5, 382.2, 551.9, weight=96.0)
    g.vbar(273.5, 536.6, 758.7, weight=96.0)
    g.vbar(279.5, 63.6, 536.6, weight=96.0)
    g.diag(273.5, 63.6, 129.8, 203.2, weight=96.0)
    g.hbar(73.0, 114.5, 238.4, weight=96.0)
    g.diag(114.5, 238.4, 328.5, 439.8, weight=96.0)
    g.diag(512.8, 718.8, 502.8, 702.2, weight=48.0)
    g.vbar(526.4, 594.1, 702.2, weight=48.0)
    g.hbar(519.6, 742.0, 721.2, weight=48.0)
    g.diag(742.0, 731.1, 674.3, 641.1, weight=48.0)
    g.hbar(549.5, 708.8, 628.5, weight=48.0)
    g.vbar(430.2, 375.6, 507.8, weight=48.0)
    g.hbar(425.3, 559.6, 508.8, weight=48.0)
    g.vbar(550.1, 445.9, 518.9, weight=48.0)
    g.diag(540.6, 445.9, 526.3, 433.6, weight=48.0)
    g.dot(509.4, 403.4, w=96.0, h=113.1, slant=-14.0)
    g.vbar(655.0, 418.3, 546.1, weight=48.0)
    g.hbar(650.2, 815.8, 546.2, weight=48.0)
    g.diag(815.8, 551.7, 770.1, 473.6, weight=48.0)
    g.hbar(685.1, 797.2, 445.5, weight=48.0)
    g.vbar(798.4, 458.5, 476.7, weight=48.0)
    g.hbar(369.0, 883.6, 296.9, weight=48.0)
    g.vbar(596.6, -38.7, 382.6, weight=96.0)
    g.diag(581.3, 280.7, 354.8, 66.9, weight=48.0)
    g.diag(626.1, 244.5, 942.0, 83.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_64e6() -> Glyph:
    """擦 U+64E6 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni64E6", advance=1000, unicode=0x64E6, note="擦：自动生成")
    g.hbar(120.0, 323.0, 500.5, weight=96.0)
    g.diag(249.2, 729.5, 274.5, 546.1, weight=84.0)
    g.vbar(269.6, 12.1, 546.1, weight=84.0)
    g.diag(264.6, 12.1, 160.5, 59.7, weight=84.0)
    g.hbar(68.0, 119.4, 239.4, weight=96.0)
    g.diag(119.4, 240.9, 318.6, 400.8, weight=96.0)
    g.diag(542.2, 767.1, 619.3, 725.6, weight=48.0)
    g.diag(619.3, 725.6, 641.7, 662.9, weight=48.0)
    g.hbar(429.5, 441.3, 613.2, weight=48.0)
    g.diag(429.5, 615.1, 401.7, 541.7, weight=48.0)
    g.diag(401.7, 541.7, 357.6, 518.2, weight=48.0)
    g.hbar(444.8, 814.1, 624.4, weight=48.0)
    g.diag(814.1, 651.4, 734.5, 544.8, weight=48.0)
    g.diag(504.3, 499.1, 479.4, 519.8, weight=48.0)
    g.diag(479.4, 519.8, 383.5, 388.1, weight=48.0)
    g.diag(471.4, 473.4, 486.4, 391.5, weight=48.0)
    g.diag(486.4, 391.5, 300.5, 182.9, weight=48.0)
    g.dot(466.2, 398.6, w=56.0, h=72.8, slant=-14.0)
    g.dot(418.4, 341.1, w=56.0, h=72.8, slant=-14.0)
    g.diag(615.5, 463.0, 728.0, 528.0, weight=48.0)
    g.diag(728.0, 528.0, 774.4, 503.7, weight=48.0)
    g.diag(774.4, 503.7, 691.7, 406.6, weight=48.0)
    g.hbar(582.8, 947.0, 371.4, weight=48.0)
    g.hbar(492.3, 714.0, 316.2, weight=48.0)
    g.diag(411.4, 196.2, 465.8, 171.1, weight=76.0)
    g.hbar(465.8, 755.4, 194.3, weight=76.0)
    g.diag(755.4, 217.5, 795.0, 276.7, weight=76.0)
    g.diag(584.6, 174.3, 665.9, -56.0, weight=96.0)
    g.hbar(476.1, 665.9, -15.5, weight=96.0)
    g.vbar(442.7, 3.4, 132.1, weight=96.0)
    g.hbar(418.4, 471.8, 0.7, weight=96.0)
    g.hbar(645.0, 805.2, 91.3, weight=76.0)
    g.diag(805.2, 64.8, 841.0, 10.5, weight=76.0)
    return g
def g_cjk_unified_ideograph_64ec() -> Glyph:
    """擬 U+64EC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni64EC", advance=1000, unicode=0x64EC, note="擬：自动生成")
    g.hbar(95.4, 305.5, 425.9, weight=76.0)
    g.diag(208.8, 691.4, 234.9, 486.5, weight=76.0)
    g.vbar(230.4, 13.0, 486.5, weight=76.0)
    g.diag(225.9, 13.0, 138.2, 55.5, weight=76.0)
    g.diag(48.0, 176.3, 139.5, 220.8, weight=48.0)
    g.diag(139.5, 220.8, 291.6, 322.3, weight=48.0)
    g.hbar(497.6, 529.6, 596.4, weight=76.0)
    g.hbar(394.9, 497.6, 575.3, weight=76.0)
    g.diag(394.9, 553.4, 393.8, 551.9, weight=76.0)
    g.diag(356.7, 659.8, 354.1, 662.6, weight=76.0)
    g.diag(354.1, 662.6, 398.1, 460.7, weight=76.0)
    g.hbar(398.1, 518.0, 466.9, weight=76.0)
    g.diag(518.0, 473.1, 527.7, 538.0, weight=76.0)
    g.diag(375.2, 419.9, 393.4, 396.1, weight=48.0)
    g.diag(393.4, 396.1, 314.8, 281.4, weight=48.0)
    g.hbar(377.1, 514.7, 345.1, weight=76.0)
    g.hbar(287.9, 517.5, 240.0, weight=64.0)
    g.diag(404.1, 317.6, 392.8, 228.3, weight=48.0)
    g.diag(392.8, 228.3, 304.6, 66.6, weight=48.0)
    g.dot(462.6, 182.4, w=76.0, h=69.1, slant=-14.0)
    g.hbar(560.3, 580.6, 592.4, weight=48.0)
    g.hbar(580.6, 765.8, 602.4, weight=48.0)
    g.diag(765.8, 615.6, 683.8, 516.8, weight=48.0)
    g.hbar(675.5, 683.8, 517.1, weight=48.0)
    g.diag(603.0, 521.2, 691.3, 458.9, weight=48.0)
    g.hbar(538.9, 812.1, 403.2, weight=76.0)
    g.diag(812.1, 425.6, 753.6, 349.2, weight=76.0)
    g.diag(644.9, 379.0, 654.3, 372.3, weight=76.0)
    g.diag(654.3, 372.3, 683.9, 136.3, weight=76.0)
    g.dot(746.7, 247.4, w=76.0, h=98.8, slant=-14.0)
    g.diag(559.3, 274.9, 590.7, 233.6, weight=76.0)
    g.diag(590.7, 233.6, 439.4, 30.4, weight=76.0)
    g.hbar(591.9, 947.0, 111.2, weight=76.0)
    return g
def g_cjk_unified_ideograph_6562() -> Glyph:
    """敢 U+6562 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6562", advance=1000, unicode=0x6562, note="敢：自动生成")
    g.hbar(199.1, 349.6, 701.8, weight=48.0)
    g.diag(349.6, 716.2, 397.8, 689.1, weight=48.0)
    g.diag(397.8, 689.1, 341.9, 590.7, weight=48.0)
    g.hbar(96.6, 467.1, 556.7, weight=48.0)
    g.diag(178.4, 512.9, 210.3, 488.0, weight=96.0)
    g.vbar(205.2, 201.9, 488.0, weight=96.0)
    g.diag(200.2, 201.9, 189.2, 193.6, weight=96.0)
    g.diag(367.5, 551.3, 384.5, 438.0, weight=64.0)
    g.vbar(385.9, -37.9, 438.0, weight=64.0)
    g.vbar(242.9, 401.5, 412.6, weight=84.0)
    g.hbar(245.4, 331.1, 415.9, weight=84.0)
    g.diag(234.5, 294.1, 243.8, 308.0, weight=84.0)
    g.hbar(243.8, 331.1, 311.9, weight=84.0)
    g.hbar(68.0, 118.9, 140.8, weight=96.0)
    g.hbar(118.9, 483.8, 197.5, weight=96.0)
    g.vbar(583.4, 647.7, 777.9, weight=56.0)
    g.diag(579.4, 647.7, 460.2, 358.2, weight=56.0)
    g.hbar(570.5, 864.2, 519.8, weight=96.0)
    g.diag(661.2, 476.4, 642.4, 343.8, weight=56.0)
    g.diag(642.4, 343.8, 464.1, 91.1, weight=56.0)
    g.diag(505.5, 388.7, 781.5, 74.9, weight=96.0)
    g.hbar(781.5, 942.0, 59.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_6574() -> Glyph:
    """整 U+6574 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6574", advance=1000, unicode=0x6574, note="整：自动生成")
    g.diag(188.1, 601.1, 397.6, 703.4, weight=76.0)
    g.diag(397.6, 703.4, 413.6, 626.9, weight=76.0)
    g.vbar(177.4, 432.8, 567.2, weight=84.0)
    g.hbar(176.5, 308.9, 570.2, weight=48.0)
    g.hbar(308.9, 444.9, 583.3, weight=48.0)
    g.diag(444.9, 590.3, 400.4, 505.9, weight=48.0)
    g.hbar(217.3, 424.2, 468.9, weight=48.0)
    g.vbar(426.1, 491.1, 507.4, weight=48.0)
    g.diag(297.5, 711.3, 306.1, 647.6, weight=96.0)
    g.vbar(308.6, 303.1, 647.6, weight=96.0)
    g.diag(286.0, 449.2, 82.0, 271.9, weight=48.0)
    g.dot(397.7, 393.5, w=84.0, h=109.2, slant=-14.0)
    g.diag(592.3, 792.0, 628.5, 754.3, weight=96.0)
    g.diag(628.5, 754.3, 492.6, 517.6, weight=96.0)
    g.hbar(582.7, 808.4, 634.3, weight=48.0)
    g.diag(671.2, 603.6, 640.8, 508.1, weight=48.0)
    g.diag(640.8, 508.1, 443.8, 363.0, weight=48.0)
    g.hbar(511.5, 526.2, 534.8, weight=84.0)
    g.diag(511.5, 534.3, 918.0, 329.1, weight=84.0)
    g.hbar(315.8, 569.8, 276.4, weight=96.0)
    g.diag(569.8, 286.3, 590.4, 347.9, weight=96.0)
    g.diag(441.3, 243.3, 501.9, 72.1, weight=96.0)
    g.diag(501.9, 72.1, 453.1, 20.2, weight=96.0)
    g.hbar(503.5, 629.8, 152.0, weight=96.0)
    g.vbar(634.7, 167.3, 252.3, weight=96.0)
    g.vbar(309.5, 19.6, 231.6, weight=96.0)
    g.diag(322.1, 19.6, 336.7, 12.3, weight=96.0)
    g.hbar(126.5, 805.4, -15.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_6575() -> Glyph:
    """敵 U+6575 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6575", advance=1000, unicode=0x6575, note="敵：自动生成")
    g.diag(280.0, 767.7, 357.7, 721.1, weight=64.0)
    g.diag(357.7, 721.1, 394.7, 628.5, weight=64.0)
    g.diag(128.3, 537.4, 98.3, 563.8, weight=96.0)
    g.hbar(98.3, 582.0, 574.4, weight=96.0)
    g.diag(157.9, 542.5, 225.1, 407.5, weight=48.0)
    g.diag(339.1, 570.6, 365.6, 538.0, weight=48.0)
    g.diag(365.6, 538.0, 310.0, 421.8, weight=48.0)
    g.vbar(112.8, 269.2, 384.9, weight=48.0)
    g.vbar(97.0, -27.7, 269.2, weight=48.0)
    g.diag(124.4, 374.8, 357.6, 254.5, weight=48.0)
    g.diag(357.6, 254.5, 418.9, -19.8, weight=48.0)
    g.diag(418.9, -19.8, 346.4, 64.4, weight=48.0)
    g.hbar(146.1, 408.7, 285.7, weight=76.0)
    g.diag(246.8, 379.3, 279.5, 351.0, weight=48.0)
    g.diag(279.5, 351.0, 246.8, 192.9, weight=48.0)
    g.vbar(201.2, 157.7, 171.1, weight=48.0)
    g.vbar(213.2, 52.4, 157.7, weight=48.0)
    g.hbar(216.7, 347.2, 171.5, weight=48.0)
    g.vbar(340.0, 125.6, 180.5, weight=48.0)
    g.diag(332.8, 125.6, 314.4, 108.1, weight=48.0)
    g.diag(236.3, 68.1, 244.1, 75.4, weight=48.0)
    g.hbar(244.1, 340.0, 91.3, weight=48.0)
    g.diag(614.5, 739.8, 666.9, 692.9, weight=96.0)
    g.diag(666.9, 692.9, 486.1, 319.2, weight=96.0)
    g.hbar(596.9, 852.7, 471.5, weight=96.0)
    g.diag(683.9, 425.9, 769.4, 342.7, weight=96.0)
    g.diag(769.4, 342.7, 476.3, 40.7, weight=96.0)
    g.diag(517.2, 325.5, 947.0, 14.7, weight=64.0)
    return g
def g_cjk_unified_ideograph_6577() -> Glyph:
    """敷 U+6577 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6577", advance=1000, unicode=0x6577, note="敷：自动生成")
    g.hbar(176.5, 419.2, 657.9, weight=48.0)
    g.diag(117.7, 556.1, 177.4, 336.8, weight=48.0)
    g.hbar(166.7, 461.4, 561.3, weight=48.0)
    g.diag(461.4, 577.3, 409.4, 355.4, weight=48.0)
    g.hbar(226.4, 377.1, 492.4, weight=48.0)
    g.hbar(223.4, 369.3, 420.5, weight=48.0)
    g.diag(265.5, 765.6, 310.7, 728.9, weight=96.0)
    g.vbar(304.8, 348.5, 728.9, weight=96.0)
    g.diag(399.7, 752.8, 481.9, 691.2, weight=56.0)
    g.dot(281.7, 307.9, w=48.0, h=62.4, slant=-14.0)
    g.hbar(66.8, 473.1, 251.1, weight=48.0)
    g.hbar(316.4, 418.3, 178.0, weight=48.0)
    g.diag(418.3, 159.3, 324.6, -24.6, weight=48.0)
    g.diag(324.6, -24.6, 225.4, 31.3, weight=48.0)
    g.diag(313.5, 230.1, 252.0, 162.3, weight=48.0)
    g.diag(252.0, 162.3, 58.0, -17.6, weight=48.0)
    g.diag(591.5, 706.8, 641.6, 664.6, weight=96.0)
    g.diag(641.6, 664.6, 481.9, 322.1, weight=96.0)
    g.hbar(574.9, 841.2, 450.8, weight=96.0)
    g.vbar(643.1, 293.4, 412.1, weight=64.0)
    g.diag(636.9, 293.4, 449.6, 31.3, weight=64.0)
    g.hbar(508.3, 520.8, 325.5, weight=96.0)
    g.diag(520.8, 326.1, 768.8, 33.4, weight=96.0)
    g.hbar(768.8, 942.0, 14.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_6591() -> Glyph:
    """斑 U+6591 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6591", advance=1000, unicode=0x6591, note="斑：自动生成")
    g.hbar(164.3, 298.8, 507.0, weight=96.0)
    g.diag(298.8, 533.6, 341.5, 448.1, weight=96.0)
    g.hbar(119.7, 363.1, 301.8, weight=64.0)
    g.diag(201.5, 471.1, 245.0, 437.1, weight=96.0)
    g.vbar(231.4, 116.9, 437.1, weight=96.0)
    g.diag(217.7, 116.9, 216.1, 114.7, weight=96.0)
    g.hbar(73.0, 376.9, 84.6, weight=48.0)
    g.diag(424.5, 688.2, 576.1, 566.7, weight=96.0)
    g.diag(335.5, 363.3, 352.7, 399.2, weight=96.0)
    g.hbar(352.7, 598.6, 449.1, weight=96.0)
    g.diag(498.1, 423.6, 477.7, 303.4, weight=48.0)
    g.diag(477.7, 303.4, 314.5, 45.6, weight=48.0)
    g.diag(370.0, 330.3, 548.9, 159.1, weight=96.0)
    g.vbar(550.2, 79.0, 159.1, weight=96.0)
    g.hbar(598.9, 850.9, 539.9, weight=96.0)
    g.hbar(550.8, 820.0, 326.7, weight=96.0)
    g.hbar(761.5, 820.0, 340.8, weight=96.0)
    g.diag(687.4, 512.9, 726.2, 485.0, weight=96.0)
    g.vbar(718.3, 105.9, 485.0, weight=96.0)
    g.diag(710.3, 105.9, 696.1, 88.4, weight=96.0)
    g.diag(543.9, 89.0, 577.2, 40.8, weight=96.0)
    g.hbar(577.2, 922.0, 55.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_659c() -> Glyph:
    """斜 U+659C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni659C", advance=1000, unicode=0x659C, note="斜：自动生成")
    g.diag(344.2, 772.0, 382.3, 716.1, weight=96.0)
    g.diag(382.3, 716.1, 86.4, 360.9, weight=96.0)
    g.dot(428.8, 619.1, w=96.0, h=124.8, slant=-14.0)
    g.hbar(252.0, 456.1, 478.1, weight=96.0)
    g.hbar(188.0, 471.1, 347.8, weight=96.0)
    g.diag(343.2, 444.7, 359.8, 347.4, weight=48.0)
    g.vbar(353.9, 112.4, 347.4, weight=48.0)
    g.hbar(259.5, 348.0, 132.2, weight=48.0)
    g.dot(218.1, 205.7, w=96.0, h=124.8, slant=14.0)
    g.dot(467.4, 227.8, w=96.0, h=94.1, slant=-14.0)
    g.dot(586.4, 591.9, w=84.0, h=103.7, slant=-14.0)
    g.diag(532.3, 494.5, 620.7, 429.6, weight=64.0)
    g.hbar(509.7, 923.6, 354.4, weight=96.0)
    g.diag(669.6, 755.1, 710.7, 569.1, weight=96.0)
    g.vbar(716.5, -52.0, 569.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_65ac() -> Glyph:
    """斬 U+65AC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni65AC", advance=1000, unicode=0x65AC, note="斬：自动生成")
    g.hbar(297.6, 310.2, 616.6, weight=84.0)
    g.hbar(297.6, 425.8, 633.7, weight=84.0)
    g.diag(425.8, 651.4, 443.4, 578.4, weight=84.0)
    g.vbar(187.5, 493.2, 502.4, weight=48.0)
    g.vbar(215.3, 307.1, 493.2, weight=48.0)
    g.hbar(200.9, 495.3, 518.8, weight=48.0)
    g.vbar(469.8, 357.2, 539.7, weight=48.0)
    g.hbar(420.4, 444.4, 355.7, weight=48.0)
    g.hbar(239.1, 368.6, 427.0, weight=64.0)
    g.hbar(366.7, 368.6, 444.9, weight=64.0)
    g.hbar(254.9, 417.1, 348.3, weight=64.0)
    g.hbar(102.0, 511.8, 219.0, weight=92.0)
    g.diag(299.7, 782.0, 330.8, 608.9, weight=84.0)
    g.vbar(329.5, 109.1, 608.9, weight=84.0)
    g.diag(328.3, 109.1, 393.0, 78.9, weight=84.0)
    g.diag(721.8, 738.1, 742.8, 699.0, weight=96.0)
    g.diag(742.8, 699.0, 620.6, 594.0, weight=96.0)
    g.hbar(611.9, 620.6, 595.1, weight=96.0)
    g.vbar(535.6, 137.1, 599.1, weight=76.0)
    g.hbar(357.2, 489.6, 116.5, weight=76.0)
    g.diag(615.6, 445.1, 618.5, 447.7, weight=96.0)
    g.hbar(618.5, 903.0, 476.2, weight=96.0)
    g.diag(698.9, 436.9, 742.1, 409.3, weight=96.0)
    g.vbar(737.9, -52.0, 409.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_65cb() -> Glyph:
    """旋 U+65CB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni65CB", advance=1000, unicode=0x65CB, note="旋：自动生成")
    g.dot(305.7, 642.3, w=96.0, h=124.8, slant=-14.0)
    g.hbar(97.0, 407.4, 466.2, weight=96.0)
    g.diag(279.9, 368.5, 321.8, 261.3, weight=48.0)
    g.diag(321.8, 261.3, 272.4, 51.9, weight=48.0)
    g.diag(272.4, 51.9, 200.2, 117.5, weight=48.0)
    g.diag(231.3, 428.8, 274.6, 396.0, weight=96.0)
    g.diag(274.6, 396.0, 63.0, 86.4, weight=96.0)
    g.diag(544.5, 756.6, 584.6, 714.5, weight=96.0)
    g.diag(584.6, 714.5, 428.8, 448.2, weight=96.0)
    g.hbar(532.9, 769.3, 570.3, weight=96.0)
    g.hbar(467.7, 795.6, 415.0, weight=56.0)
    g.diag(795.6, 442.1, 707.0, 334.4, weight=56.0)
    g.hbar(564.9, 587.3, 387.5, weight=96.0)
    g.vbar(589.7, 202.2, 391.1, weight=96.0)
    g.vbar(620.3, 102.9, 202.2, weight=96.0)
    g.dot(697.3, 250.8, w=96.0, h=118.4, slant=-14.0)
    g.diag(467.7, 271.2, 503.4, 230.0, weight=84.0)
    g.diag(503.4, 230.0, 320.8, -21.6, weight=84.0)
    g.hbar(499.8, 922.0, 82.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_65d7() -> Glyph:
    """旗 U+65D7 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni65D7", advance=1000, unicode=0x65D7, note="旗：自动生成")
    g.diag(275.4, 736.3, 362.1, 684.7, weight=96.0)
    g.diag(362.1, 684.7, 386.2, 570.1, weight=96.0)
    g.hbar(99.1, 445.2, 504.5, weight=96.0)
    g.diag(293.6, 392.9, 340.6, 262.2, weight=48.0)
    g.diag(340.6, 262.2, 289.5, 57.8, weight=48.0)
    g.diag(289.5, 57.8, 201.4, 119.5, weight=48.0)
    g.diag(273.5, 474.2, 305.0, 448.1, weight=96.0)
    g.diag(305.0, 448.1, 108.8, 158.4, weight=96.0)
    g.diag(108.8, 158.4, 163.4, 125.1, weight=96.0)
    g.vbar(576.7, 683.7, 732.4, weight=96.0)
    g.diag(576.2, 732.4, 472.9, 556.9, weight=96.0)
    g.hbar(574.5, 781.6, 664.2, weight=96.0)
    g.diag(781.6, 683.7, 766.0, 621.9, weight=96.0)
    g.hbar(490.9, 540.6, 448.6, weight=76.0)
    g.hbar(490.9, 809.6, 474.6, weight=76.0)
    g.hbar(779.9, 809.6, 509.8, weight=76.0)
    g.diag(513.0, 575.8, 556.7, 458.7, weight=48.0)
    g.vbar(564.7, 226.7, 458.7, weight=48.0)
    g.diag(572.6, 226.7, 560.1, 205.0, weight=48.0)
    g.diag(710.3, 627.9, 753.4, 581.8, weight=96.0)
    g.vbar(743.8, 242.9, 581.8, weight=96.0)
    g.diag(734.2, 242.9, 720.7, 231.6, weight=96.0)
    g.diag(597.3, 357.3, 608.0, 371.2, weight=64.0)
    g.hbar(608.0, 717.4, 374.0, weight=64.0)
    g.diag(593.1, 266.7, 605.9, 280.7, weight=64.0)
    g.hbar(605.9, 713.2, 284.1, weight=64.0)
    g.hbar(375.8, 937.0, 195.2, weight=64.0)
    g.diag(590.1, 163.8, 385.5, -45.1, weight=64.0)
    g.diag(706.2, 164.0, 840.5, -32.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_6676() -> Glyph:
    """晶 U+6676 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6676", advance=1000, unicode=0x6676, note="晶：自动生成")
    g.diag(387.2, 736.1, 375.3, 714.9, weight=48.0)
    g.vbar(402.8, 450.9, 714.9, weight=48.0)
    g.hbar(392.7, 682.1, 731.7, weight=48.0)
    g.vbar(658.9, 481.3, 738.9, weight=48.0)
    g.hbar(606.3, 635.7, 481.7, weight=48.0)
    g.hbar(424.4, 620.6, 602.1, weight=96.0)
    g.dot(520.2, 483.5, w=96.0, h=124.8, slant=-14.0)
    g.diag(192.5, 319.0, 175.0, 307.6, weight=48.0)
    g.diag(175.0, 307.6, 223.7, 11.6, weight=48.0)
    g.diag(197.3, 306.0, 371.1, 207.3, weight=48.0)
    g.diag(371.1, 207.3, 410.9, -24.2, weight=48.0)
    g.diag(229.6, 160.2, 239.0, 176.4, weight=96.0)
    g.hbar(239.0, 384.4, 180.3, weight=96.0)
    g.diag(232.7, 28.6, 246.0, 44.6, weight=96.0)
    g.hbar(246.0, 378.0, 49.3, weight=96.0)
    g.diag(581.7, 339.2, 568.6, 306.4, weight=48.0)
    g.vbar(582.2, 4.2, 306.4, weight=48.0)
    g.diag(589.9, 328.8, 782.9, 213.4, weight=48.0)
    g.diag(782.9, 213.4, 818.1, -47.0, weight=48.0)
    g.hbar(617.1, 803.1, 176.0, weight=96.0)
    g.hbar(608.8, 787.2, 30.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_6687() -> Glyph:
    """暇 U+6687 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6687", advance=1000, unicode=0x6687, note="暇：自动生成")
    g.vbar(119.7, 137.5, 656.2, weight=84.0)
    g.hbar(135.4, 231.4, 657.0, weight=48.0)
    g.diag(231.4, 670.2, 259.3, 487.4, weight=48.0)
    g.vbar(260.7, 127.6, 487.4, weight=48.0)
    g.diag(153.6, 412.1, 162.3, 426.2, weight=96.0)
    g.hbar(162.3, 230.1, 427.5, weight=96.0)
    g.dot(187.9, 179.9, w=96.0, h=89.4, slant=-14.0)
    g.hbar(391.2, 549.5, 679.7, weight=48.0)
    g.vbar(522.0, 561.1, 697.0, weight=48.0)
    g.dot(466.2, 528.4, w=96.0, h=124.8, slant=-14.0)
    g.vbar(362.2, 0.5, 680.7, weight=84.0)
    g.dot(465.5, 383.9, w=96.0, h=124.8, slant=-14.0)
    g.hbar(396.1, 505.5, 270.7, weight=96.0)
    g.diag(505.5, 284.7, 555.8, 331.8, weight=96.0)
    g.hbar(559.0, 760.2, 686.1, weight=48.0)
    g.diag(760.2, 692.7, 788.7, 669.1, weight=48.0)
    g.diag(788.7, 669.1, 728.9, 577.0, weight=48.0)
    g.hbar(556.1, 765.6, 561.5, weight=48.0)
    g.diag(544.5, 421.6, 651.0, 342.5, weight=96.0)
    g.diag(651.0, 342.5, 395.0, 116.1, weight=96.0)
    g.diag(546.0, 381.6, 805.8, 110.9, weight=96.0)
    g.hbar(805.8, 932.0, 99.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_6691() -> Glyph:
    """暑 U+6691 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6691", advance=1000, unicode=0x6691, note="暑：自动生成")
    g.vbar(329.3, 723.3, 741.6, weight=48.0)
    g.vbar(351.3, 525.3, 723.3, weight=48.0)
    g.hbar(340.7, 662.2, 744.3, weight=48.0)
    g.vbar(631.6, 560.0, 756.5, weight=48.0)
    g.hbar(580.5, 601.0, 559.6, weight=48.0)
    g.diag(379.0, 631.8, 397.1, 647.7, weight=76.0)
    g.hbar(397.1, 595.9, 646.8, weight=76.0)
    g.diag(388.9, 539.6, 401.1, 550.8, weight=76.0)
    g.hbar(401.1, 572.8, 561.2, weight=76.0)
    g.hbar(311.4, 624.5, 432.2, weight=48.0)
    g.diag(459.3, 530.4, 465.9, 526.3, weight=96.0)
    g.diag(465.9, 526.3, 500.1, 383.6, weight=96.0)
    g.diag(500.1, 383.6, 467.4, 340.7, weight=96.0)
    g.hbar(129.9, 899.8, 306.0, weight=48.0)
    g.diag(775.4, 507.0, 569.6, 365.9, weight=48.0)
    g.diag(569.6, 365.9, 95.2, 13.4, weight=48.0)
    g.vbar(379.4, -42.8, 225.5, weight=96.0)
    g.hbar(422.9, 575.6, 221.9, weight=48.0)
    g.diag(575.6, 242.6, 700.3, 143.8, weight=48.0)
    g.diag(700.3, 143.8, 528.8, -12.8, weight=48.0)
    g.hbar(528.8, 549.0, -15.8, weight=48.0)
    g.hbar(424.6, 584.5, 101.8, weight=76.0)
    g.dot(486.8, -6.0, w=84.0, h=109.2, slant=-14.0)
    return g
def g_cjk_unified_ideograph_6696() -> Glyph:
    """暖 U+6696 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6696", advance=1000, unicode=0x6696, note="暖：自动生成")
    g.vbar(125.5, 536.9, 655.2, weight=48.0)
    g.vbar(112.8, 194.5, 536.9, weight=48.0)
    g.diag(103.4, 194.5, 133.0, 139.2, weight=48.0)
    g.diag(141.0, 646.9, 254.0, 482.3, weight=64.0)
    g.vbar(266.1, 162.6, 482.3, weight=64.0)
    g.hbar(256.8, 278.2, 164.7, weight=64.0)
    g.dot(198.0, 414.8, w=96.0, h=104.8, slant=-14.0)
    g.diag(144.3, 154.7, 153.8, 165.1, weight=96.0)
    g.hbar(153.8, 245.9, 177.5, weight=96.0)
    g.hbar(661.7, 729.0, 746.0, weight=96.0)
    g.diag(661.7, 759.6, 426.7, 649.7, weight=96.0)
    g.diag(418.8, 637.5, 470.5, 557.5, weight=84.0)
    g.vbar(473.4, 492.0, 557.5, weight=84.0)
    g.diag(528.2, 662.0, 572.8, 598.4, weight=84.0)
    g.hbar(572.8, 631.8, 585.9, weight=84.0)
    g.diag(740.6, 715.7, 774.1, 660.9, weight=96.0)
    g.diag(774.1, 660.9, 668.4, 578.2, weight=96.0)
    g.vbar(668.1, 541.3, 578.2, weight=96.0)
    g.hbar(472.6, 668.2, 474.3, weight=84.0)
    g.diag(668.2, 502.4, 689.3, 548.6, weight=84.0)
    g.hbar(321.8, 834.4, 363.0, weight=84.0)
    g.diag(503.5, 440.8, 458.9, 303.3, weight=48.0)
    g.diag(458.9, 303.3, 245.9, -17.3, weight=48.0)
    g.hbar(486.7, 649.7, 267.3, weight=48.0)
    g.diag(649.7, 285.0, 616.6, 181.5, weight=48.0)
    g.diag(616.6, 181.5, 380.7, -18.3, weight=48.0)
    g.diag(467.2, 188.9, 937.0, -26.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_66ab() -> Glyph:
    """暫 U+66AB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni66AB", advance=1000, unicode=0x66AB, note="暫：自动生成")
    g.diag(266.4, 606.6, 429.0, 697.1, weight=56.0)
    g.diag(429.0, 697.1, 486.1, 641.1, weight=56.0)
    g.vbar(242.2, 565.5, 583.3, weight=48.0)
    g.vbar(264.6, 413.0, 565.5, weight=48.0)
    g.hbar(253.7, 525.6, 594.5, weight=48.0)
    g.vbar(503.0, 459.5, 613.2, weight=48.0)
    g.hbar(463.9, 480.3, 458.1, weight=48.0)
    g.hbar(278.5, 480.6, 517.0, weight=48.0)
    g.hbar(303.1, 459.4, 447.4, weight=56.0)
    g.hbar(113.1, 532.6, 339.5, weight=64.0)
    g.vbar(374.4, 576.3, 710.0, weight=84.0)
    g.vbar(377.7, 251.5, 576.3, weight=84.0)
    g.diag(728.2, 724.5, 746.0, 687.0, weight=96.0)
    g.diag(746.0, 687.0, 642.2, 606.2, weight=96.0)
    g.vbar(642.2, 601.5, 606.2, weight=96.0)
    g.hbar(537.5, 629.5, 587.6, weight=48.0)
    g.vbar(587.0, 316.6, 577.8, weight=48.0)
    g.diag(544.5, 316.6, 511.9, 354.4, weight=48.0)
    g.hbar(636.8, 891.9, 535.0, weight=96.0)
    g.diag(711.9, 496.6, 743.5, 474.0, weight=64.0)
    g.diag(743.5, 474.0, 714.1, 244.8, weight=64.0)
    g.diag(384.4, 234.1, 470.4, -48.8, weight=48.0)
    g.diag(470.4, -48.8, 434.2, -19.4, weight=48.0)
    g.hbar(427.0, 662.8, 235.3, weight=48.0)
    g.vbar(674.6, 152.8, 251.9, weight=48.0)
    g.vbar(685.7, -10.0, 152.8, weight=48.0)
    g.hbar(633.3, 685.1, -3.5, weight=48.0)
    g.diag(448.7, 106.8, 464.6, 121.4, weight=84.0)
    g.hbar(464.6, 663.9, 124.7, weight=84.0)
    g.diag(445.1, -3.6, 460.9, 11.2, weight=92.0)
    g.hbar(460.9, 647.7, 15.6, weight=92.0)
    return g
def g_cjk_unified_ideograph_66ae() -> Glyph:
    """暮 U+66AE —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni66AE", advance=1000, unicode=0x66AE, note="暮：自动生成")
    g.hbar(199.9, 778.4, 665.1, weight=92.0)
    g.diag(325.3, 738.6, 363.8, 714.9, weight=48.0)
    g.diag(363.8, 714.9, 392.4, 587.6, weight=48.0)
    g.diag(570.1, 787.0, 604.2, 751.6, weight=96.0)
    g.diag(604.2, 751.6, 542.5, 589.6, weight=96.0)
    g.diag(277.9, 552.0, 309.5, 521.4, weight=48.0)
    g.vbar(329.2, 363.5, 521.4, weight=48.0)
    g.hbar(333.2, 639.4, 555.9, weight=48.0)
    g.vbar(611.0, 391.5, 565.8, weight=48.0)
    g.diag(582.5, 391.5, 584.9, 376.3, weight=48.0)
    g.diag(358.8, 449.4, 363.7, 459.1, weight=56.0)
    g.hbar(363.7, 526.7, 468.0, weight=56.0)
    g.diag(365.7, 374.3, 375.2, 382.9, weight=48.0)
    g.hbar(375.2, 547.4, 396.4, weight=48.0)
    g.hbar(137.7, 829.7, 282.5, weight=48.0)
    g.diag(389.4, 360.5, 333.5, 269.3, weight=48.0)
    g.diag(333.5, 269.3, 65.6, 46.6, weight=48.0)
    g.diag(579.0, 273.7, 656.1, 228.4, weight=48.0)
    g.diag(656.1, 228.4, 934.4, 93.0, weight=48.0)
    g.vbar(349.5, -62.0, 187.8, weight=48.0)
    g.diag(385.5, 175.9, 398.5, 167.2, weight=48.0)
    g.hbar(398.5, 540.8, 184.5, weight=48.0)
    g.vbar(583.8, -58.1, 201.9, weight=48.0)
    g.hbar(530.6, 626.8, -37.4, weight=48.0)
    g.vbar(529.1, -16.6, -5.7, weight=48.0)
    g.diag(385.5, 69.3, 399.8, 82.4, weight=64.0)
    g.hbar(399.8, 522.7, 85.7, weight=64.0)
    g.diag(382.5, -23.5, 393.3, -12.7, weight=76.0)
    g.hbar(393.3, 517.8, -5.3, weight=76.0)
    return g
def g_cjk_unified_ideograph_66b4() -> Glyph:
    """暴 U+66B4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni66B4", advance=1000, unicode=0x66B4, note="暴：自动生成")
    g.vbar(306.7, 717.2, 729.5, weight=48.0)
    g.diag(305.2, 717.2, 350.2, 499.5, weight=48.0)
    g.hbar(318.5, 602.9, 738.3, weight=48.0)
    g.diag(602.9, 754.5, 633.6, 716.6, weight=48.0)
    g.diag(633.6, 716.6, 578.1, 568.5, weight=48.0)
    g.hbar(352.7, 581.5, 631.6, weight=56.0)
    g.hbar(372.2, 536.6, 563.8, weight=64.0)
    g.diag(536.6, 579.1, 558.9, 568.5, weight=64.0)
    g.diag(314.0, 463.2, 335.3, 420.0, weight=92.0)
    g.hbar(335.3, 615.3, 444.0, weight=92.0)
    g.diag(615.3, 468.0, 678.2, 390.6, weight=92.0)
    g.diag(346.4, 480.7, 374.5, 452.5, weight=96.0)
    g.diag(374.5, 452.5, 404.2, 344.0, weight=96.0)
    g.diag(523.1, 537.9, 555.4, 492.9, weight=96.0)
    g.diag(555.4, 492.9, 532.8, 371.3, weight=96.0)
    g.diag(532.8, 371.3, 519.0, 361.0, weight=96.0)
    g.hbar(154.8, 803.3, 318.6, weight=48.0)
    g.diag(297.1, 285.1, 245.9, 207.9, weight=48.0)
    g.diag(245.9, 207.9, 52.8, 52.3, weight=48.0)
    g.diag(52.8, 52.3, 63.0, 68.6, weight=48.0)
    g.diag(584.1, 323.8, 937.0, 121.5, weight=48.0)
    g.diag(439.7, 293.4, 496.6, 209.2, weight=84.0)
    g.diag(496.6, 209.2, 464.7, -53.4, weight=84.0)
    g.diag(464.7, -53.4, 349.7, 10.5, weight=84.0)
    g.dot(347.9, 150.1, w=96.0, h=105.5, slant=-14.0)
    g.diag(164.1, 71.0, 265.5, -9.2, weight=96.0)
    g.diag(265.5, -9.2, 390.3, 82.1, weight=96.0)
    g.diag(641.5, 248.3, 555.2, 104.2, weight=48.0)
    g.diag(557.3, 99.3, 711.5, -38.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_66c7() -> Glyph:
    """曇 U+66C7 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni66C7", advance=1000, unicode=0x66C7, note="曇：自动生成")
    g.vbar(354.6, 734.4, 751.1, weight=48.0)
    g.vbar(373.3, 575.2, 734.4, weight=48.0)
    g.hbar(366.4, 722.2, 753.8, weight=48.0)
    g.diag(722.2, 764.7, 642.9, 610.4, weight=48.0)
    g.hbar(391.7, 579.3, 673.1, weight=48.0)
    g.diag(579.3, 690.4, 605.6, 641.1, weight=48.0)
    g.hbar(407.0, 437.9, 592.8, weight=48.0)
    g.hbar(437.9, 638.8, 610.6, weight=48.0)
    g.diag(376.1, 554.5, 427.3, 514.2, weight=56.0)
    g.hbar(427.3, 636.3, 531.6, weight=56.0)
    g.diag(636.3, 549.1, 658.7, 579.8, weight=56.0)
    g.vbar(201.2, 319.9, 426.6, weight=96.0)
    g.hbar(182.3, 275.4, 301.9, weight=96.0)
    g.hbar(240.5, 851.3, 425.8, weight=48.0)
    g.diag(851.3, 448.6, 748.6, 343.0, weight=48.0)
    g.diag(482.0, 505.4, 512.0, 480.3, weight=96.0)
    g.vbar(511.0, 249.8, 480.3, weight=96.0)
    g.diag(322.2, 380.9, 382.7, 338.0, weight=48.0)
    g.vbar(380.0, 283.9, 338.0, weight=48.0)
    g.diag(327.0, 334.2, 386.7, 215.0, weight=48.0)
    g.diag(603.7, 421.8, 646.3, 381.1, weight=48.0)
    g.vbar(648.9, 319.2, 381.1, weight=48.0)
    g.diag(610.6, 366.7, 651.3, 241.2, weight=56.0)
    g.vbar(372.0, 190.0, 239.8, weight=48.0)
    g.hbar(370.2, 664.0, 227.0, weight=48.0)
    g.hbar(204.3, 802.7, 116.9, weight=48.0)
    g.diag(472.9, 106.2, 457.3, 3.5, weight=48.0)
    g.hbar(457.3, 657.2, 5.2, weight=48.0)
    g.diag(602.2, 118.8, 734.6, -72.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_66d6() -> Glyph:
    """曖 U+66D6 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni66D6", advance=1000, unicode=0x66D6, note="曖：自动生成")
    g.vbar(113.1, 107.2, 643.7, weight=96.0)
    g.hbar(131.3, 235.2, 639.7, weight=48.0)
    g.diag(235.2, 652.9, 259.9, 452.5, weight=48.0)
    g.vbar(261.5, 99.3, 452.5, weight=48.0)
    g.diag(147.3, 390.2, 166.1, 408.0, weight=96.0)
    g.hbar(166.1, 233.1, 408.0, weight=96.0)
    g.diag(142.4, 137.9, 156.2, 154.7, weight=96.0)
    g.hbar(156.2, 225.8, 160.2, weight=96.0)
    g.diag(718.3, 709.2, 640.0, 768.2, weight=96.0)
    g.diag(640.0, 768.2, 422.7, 652.6, weight=96.0)
    g.diag(418.7, 654.9, 465.9, 535.3, weight=48.0)
    g.dot(547.9, 623.3, w=92.0, h=98.2, slant=-14.0)
    g.hbar(735.8, 766.8, 674.8, weight=48.0)
    g.diag(735.8, 674.3, 654.0, 581.2, weight=48.0)
    g.diag(369.4, 517.9, 334.9, 405.9, weight=48.0)
    g.diag(334.9, 405.9, 290.7, 384.4, weight=48.0)
    g.hbar(375.0, 880.1, 545.2, weight=48.0)
    g.diag(880.1, 585.4, 752.1, 465.2, weight=48.0)
    g.vbar(422.1, 387.3, 477.2, weight=64.0)
    g.hbar(351.4, 423.4, 375.8, weight=64.0)
    g.hbar(462.0, 718.2, 371.5, weight=92.0)
    g.diag(718.2, 348.4, 669.4, 453.1, weight=92.0)
    g.diag(516.6, 508.9, 581.8, 424.9, weight=48.0)
    g.hbar(663.5, 774.9, 463.4, weight=56.0)
    g.diag(526.9, 266.1, 330.0, 39.6, weight=64.0)
    g.diag(330.0, 39.6, 262.8, 73.7, weight=64.0)
    g.hbar(543.9, 734.8, 256.9, weight=84.0)
    g.diag(734.8, 265.3, 502.1, -9.8, weight=84.0)
    g.hbar(370.1, 502.1, 13.6, weight=84.0)
    g.diag(507.6, 196.3, 625.7, 117.4, weight=96.0)
    g.diag(625.7, 117.4, 942.0, -40.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_66dc() -> Glyph:
    """曜 U+66DC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni66DC", advance=1000, unicode=0x66DC, note="曜：自动生成")
    g.vbar(174.5, 161.8, 661.1, weight=48.0)
    g.diag(189.4, 656.4, 286.1, 508.0, weight=96.0)
    g.vbar(300.0, 185.4, 508.0, weight=96.0)
    g.hbar(287.9, 313.9, 180.2, weight=96.0)
    g.diag(199.0, 411.6, 206.0, 425.6, weight=96.0)
    g.hbar(206.0, 285.8, 426.8, weight=96.0)
    g.diag(189.4, 177.4, 204.8, 193.7, weight=96.0)
    g.hbar(204.8, 277.4, 198.3, weight=96.0)
    g.vbar(416.6, 675.3, 710.4, weight=48.0)
    g.hbar(423.2, 574.9, 714.8, weight=48.0)
    g.vbar(562.9, 484.5, 719.2, weight=48.0)
    g.diag(419.8, 687.2, 499.7, 589.7, weight=48.0)
    g.hbar(362.8, 419.8, 516.3, weight=96.0)
    g.diag(419.8, 511.5, 515.4, 574.4, weight=96.0)
    g.hbar(651.5, 783.6, 737.4, weight=48.0)
    g.diag(783.6, 764.6, 825.3, 730.4, weight=48.0)
    g.diag(825.3, 730.4, 770.1, 522.0, weight=48.0)
    g.diag(652.8, 726.5, 725.1, 624.4, weight=48.0)
    g.dot(693.2, 584.4, w=96.0, h=124.8, slant=-14.0)
    g.diag(551.8, 476.8, 355.5, 278.2, weight=92.0)
    g.vbar(473.5, -7.2, 355.0, weight=96.0)
    g.diag(465.9, -7.2, 502.9, 45.6, weight=96.0)
    g.diag(627.7, 541.1, 692.5, 431.5, weight=56.0)
    g.hbar(525.6, 616.2, 406.8, weight=48.0)
    g.hbar(616.2, 806.6, 407.7, weight=48.0)
    g.hbar(645.8, 751.2, 298.9, weight=76.0)
    g.vbar(759.7, 246.0, 317.6, weight=76.0)
    g.hbar(519.6, 764.2, 201.1, weight=76.0)
    g.diag(764.2, 215.1, 779.1, 278.7, weight=76.0)
    g.diag(651.1, 374.2, 676.8, 354.5, weight=96.0)
    g.vbar(675.3, 134.8, 354.5, weight=96.0)
    g.diag(673.9, 134.8, 659.7, 114.1, weight=96.0)
    g.hbar(510.0, 883.4, 84.8, weight=92.0)
    return g
def g_cjk_unified_ideograph_66f9() -> Glyph:
    """曹 U+66F9 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni66F9", advance=1000, unicode=0x66F9, note="曹：自动生成")
    g.diag(267.4, 564.4, 321.7, 634.3, weight=96.0)
    g.hbar(321.7, 687.0, 662.0, weight=96.0)
    g.diag(687.0, 689.7, 727.0, 608.5, weight=96.0)
    g.vbar(284.2, 311.4, 528.5, weight=48.0)
    g.hbar(256.4, 750.3, 546.6, weight=48.0)
    g.diag(750.3, 570.0, 788.8, 522.8, weight=48.0)
    g.diag(788.8, 522.8, 698.7, 350.4, weight=48.0)
    g.hbar(306.6, 619.9, 444.2, weight=76.0)
    g.hbar(595.6, 619.9, 467.7, weight=76.0)
    g.diag(366.8, 678.4, 408.0, 699.3, weight=96.0)
    g.vbar(420.5, 374.6, 699.3, weight=96.0)
    g.diag(433.1, 374.6, 419.5, 358.9, weight=96.0)
    g.diag(557.9, 705.3, 589.3, 745.6, weight=96.0)
    g.vbar(573.6, 394.3, 745.6, weight=96.0)
    g.diag(558.0, 394.3, 541.0, 376.3, weight=96.0)
    g.hbar(323.4, 703.2, 345.7, weight=48.0)
    g.diag(383.3, 245.0, 373.9, 229.5, weight=48.0)
    g.vbar(379.5, -22.1, 229.5, weight=48.0)
    g.hbar(389.5, 595.0, 252.1, weight=48.0)
    g.diag(595.0, 268.9, 623.6, 165.4, weight=48.0)
    g.vbar(620.1, -14.2, 165.4, weight=48.0)
    g.hbar(572.8, 616.7, -8.4, weight=48.0)
    g.hbar(403.1, 598.5, 118.8, weight=92.0)
    g.hbar(396.4, 579.5, 4.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_6715() -> Glyph:
    """朕 U+6715 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6715", advance=1000, unicode=0x6715, note="朕：自动生成")
    g.diag(185.7, 627.7, 58.0, -21.4, weight=96.0)
    g.diag(206.9, 609.6, 318.2, 395.9, weight=48.0)
    g.vbar(327.7, 18.0, 395.9, weight=48.0)
    g.hbar(225.5, 337.2, 41.2, weight=48.0)
    g.diag(225.5, 424.6, 233.1, 439.8, weight=96.0)
    g.hbar(233.1, 318.6, 441.3, weight=96.0)
    g.diag(209.4, 277.3, 219.5, 294.6, weight=96.0)
    g.hbar(219.5, 318.9, 295.6, weight=96.0)
    g.hbar(393.2, 599.3, 593.8, weight=96.0)
    g.diag(732.1, 739.5, 761.7, 705.8, weight=96.0)
    g.diag(761.7, 705.8, 648.3, 518.1, weight=96.0)
    g.hbar(395.4, 690.5, 468.3, weight=96.0)
    g.vbar(687.7, 480.8, 551.0, weight=96.0)
    g.hbar(395.8, 867.3, 301.5, weight=96.0)
    g.vbar(566.0, 316.9, 435.1, weight=56.0)
    g.diag(566.2, 316.9, 503.7, 60.9, weight=56.0)
    g.hbar(366.4, 503.7, 42.8, weight=56.0)
    g.diag(613.0, 267.2, 942.0, -29.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_6717() -> Glyph:
    """朗 U+6717 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6717", advance=1000, unicode=0x6717, note="朗：自动生成")
    g.diag(311.2, 782.0, 397.1, 729.7, weight=84.0)
    g.diag(397.1, 729.7, 411.5, 639.0, weight=84.0)
    g.hbar(237.9, 440.6, 588.5, weight=96.0)
    g.vbar(413.2, 346.7, 601.5, weight=96.0)
    g.dot(306.1, 444.8, w=92.0, h=119.6, slant=-14.0)
    g.hbar(237.2, 347.1, 343.0, weight=92.0)
    g.diag(347.1, 360.1, 360.8, 376.3, weight=92.0)
    g.diag(159.2, 597.4, 192.3, 458.9, weight=48.0)
    g.vbar(191.0, 105.8, 458.9, weight=48.0)
    g.diag(189.6, 105.8, 377.0, 218.7, weight=48.0)
    g.diag(364.8, 230.3, 419.8, 197.7, weight=48.0)
    g.diag(419.8, 197.7, 431.6, 158.2, weight=48.0)
    g.diag(587.3, 616.7, 546.9, 435.9, weight=48.0)
    g.diag(546.9, 435.9, 346.7, -57.0, weight=48.0)
    g.hbar(590.8, 758.1, 620.7, weight=48.0)
    g.vbar(772.2, 400.7, 637.3, weight=48.0)
    g.vbar(781.6, -19.3, 400.7, weight=48.0)
    g.diag(776.9, -19.3, 658.7, 35.8, weight=48.0)
    g.diag(612.3, 416.8, 625.4, 432.6, weight=96.0)
    g.hbar(625.4, 761.7, 433.1, weight=96.0)
    g.hbar(589.6, 762.1, 272.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_683d() -> Glyph:
    """栽 U+683D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni683D", advance=1000, unicode=0x683D, note="栽：自动生成")
    g.hbar(198.4, 529.5, 580.8, weight=96.0)
    g.diag(315.4, 745.5, 361.8, 706.0, weight=56.0)
    g.diag(361.8, 706.0, 330.5, 459.6, weight=56.0)
    g.hbar(98.8, 725.3, 463.7, weight=96.0)
    g.diag(725.3, 513.5, 740.8, 449.6, weight=96.0)
    g.hbar(130.3, 502.5, 273.5, weight=48.0)
    g.hbar(305.2, 346.6, 396.2, weight=96.0)
    g.vbar(340.7, -57.0, 387.6, weight=96.0)
    g.diag(323.4, 245.9, 270.4, 182.5, weight=48.0)
    g.diag(270.4, 182.5, 105.9, 10.1, weight=48.0)
    g.dot(423.6, 152.2, w=96.0, h=124.8, slant=-14.0)
    g.diag(498.5, 777.0, 611.7, 500.6, weight=96.0)
    g.diag(611.7, 500.6, 837.9, -72.0, weight=96.0)
    g.diag(837.9, -72.0, 901.2, 152.5, weight=96.0)
    g.diag(715.5, 473.3, 754.1, 357.1, weight=96.0)
    g.diag(754.1, 357.1, 558.9, 92.3, weight=96.0)
    g.hbar(462.8, 558.9, 98.3, weight=96.0)
    g.hbar(588.5, 740.5, 679.9, weight=76.0)
    g.diag(740.5, 657.0, 758.8, 629.5, weight=76.0)
    return g
def g_cjk_unified_ideograph_6841() -> Glyph:
    """桁 U+6841 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6841", advance=1000, unicode=0x6841, note="桁：自动生成")
    g.hbar(87.3, 359.7, 472.9, weight=96.0)
    g.vbar(240.7, 502.0, 764.4, weight=48.0)
    g.vbar(247.6, -24.4, 502.0, weight=48.0)
    g.diag(247.5, 441.9, 199.2, 363.8, weight=48.0)
    g.diag(199.2, 363.8, 53.0, 142.2, weight=48.0)
    g.diag(284.6, 401.9, 388.4, 311.8, weight=48.0)
    g.diag(494.9, 706.6, 528.0, 663.6, weight=84.0)
    g.diag(528.0, 663.6, 379.2, 471.5, weight=84.0)
    g.diag(449.4, 509.6, 512.7, 446.7, weight=48.0)
    g.diag(512.7, 446.7, 274.4, 221.4, weight=48.0)
    g.vbar(440.3, 194.9, 311.5, weight=48.0)
    g.vbar(447.0, -8.7, 194.9, weight=48.0)
    g.hbar(529.1, 643.5, 570.4, weight=96.0)
    g.hbar(643.5, 806.6, 564.5, weight=96.0)
    g.hbar(506.8, 932.0, 395.0, weight=96.0)
    g.diag(689.0, 368.5, 776.5, 310.2, weight=96.0)
    g.diag(776.5, 310.2, 678.0, 1.2, weight=96.0)
    g.hbar(601.8, 678.0, 18.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_6843() -> Glyph:
    """桃 U+6843 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6843", advance=1000, unicode=0x6843, note="桃：自动生成")
    g.hbar(124.9, 407.3, 489.7, weight=96.0)
    g.vbar(278.0, 477.7, 772.0, weight=48.0)
    g.vbar(284.7, -57.0, 477.7, weight=48.0)
    g.diag(286.5, 466.3, 65.3, 100.5, weight=48.0)
    g.diag(322.4, 397.6, 383.9, 354.9, weight=48.0)
    g.diag(383.9, 354.9, 400.6, 323.4, weight=48.0)
    g.vbar(526.0, 418.9, 635.6, weight=48.0)
    g.diag(525.5, 418.9, 378.5, 23.7, weight=48.0)
    g.dot(473.0, 452.7, w=96.0, h=124.8, slant=-14.0)
    g.diag(382.3, 245.6, 542.9, 337.6, weight=48.0)
    g.diag(652.3, 722.0, 716.7, 460.7, weight=48.0)
    g.diag(716.7, 460.7, 902.7, 18.0, weight=48.0)
    g.diag(902.7, 18.0, 934.7, 212.9, weight=48.0)
    g.diag(729.5, 578.9, 817.5, 536.7, weight=96.0)
    g.diag(817.5, 536.7, 708.0, 437.7, weight=96.0)
    g.diag(697.9, 333.8, 857.8, 225.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_6851() -> Glyph:
    """桑 U+6851 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6851", advance=1000, unicode=0x6851, note="桑：自动生成")
    g.hbar(362.0, 471.4, 694.6, weight=48.0)
    g.diag(471.4, 681.4, 314.5, 523.3, weight=48.0)
    g.diag(366.3, 697.1, 586.9, 575.5, weight=96.0)
    g.diag(231.7, 459.1, 226.8, 488.0, weight=48.0)
    g.diag(226.8, 488.0, 322.9, 444.3, weight=48.0)
    g.diag(322.9, 444.3, 199.5, 312.8, weight=48.0)
    g.diag(243.0, 469.6, 423.0, 342.6, weight=48.0)
    g.hbar(513.9, 594.6, 483.2, weight=48.0)
    g.diag(594.6, 478.5, 463.5, 352.8, weight=48.0)
    g.diag(514.4, 511.0, 687.7, 385.0, weight=48.0)
    g.diag(687.7, 385.0, 714.7, 311.0, weight=48.0)
    g.hbar(123.9, 812.8, 259.4, weight=48.0)
    g.vbar(457.1, -52.0, 356.9, weight=96.0)
    g.diag(433.8, 248.2, 127.6, 14.2, weight=48.0)
    g.diag(492.4, 253.3, 876.1, 35.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_6885() -> Glyph:
    """梅 U+6885 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6885", advance=1000, unicode=0x6885, note="梅：自动生成")
    g.hbar(93.6, 430.3, 487.6, weight=96.0)
    g.vbar(276.8, 474.1, 761.4, weight=48.0)
    g.vbar(281.9, -60.7, 474.1, weight=48.0)
    g.diag(285.2, 459.0, 232.1, 371.9, weight=48.0)
    g.diag(232.1, 371.9, 53.0, 96.4, weight=48.0)
    g.diag(321.0, 400.9, 391.6, 347.4, weight=48.0)
    g.vbar(393.9, 284.6, 347.4, weight=48.0)
    g.diag(577.1, 780.7, 616.6, 735.2, weight=96.0)
    g.diag(616.6, 735.2, 478.4, 495.6, weight=96.0)
    g.hbar(432.0, 478.4, 489.5, weight=96.0)
    g.hbar(545.7, 847.8, 584.0, weight=96.0)
    g.diag(493.9, 491.6, 592.0, 232.4, weight=48.0)
    g.diag(592.0, 232.4, 896.4, 77.2, weight=48.0)
    g.diag(553.4, 456.3, 691.1, 299.4, weight=48.0)
    g.vbar(682.1, -59.9, 299.4, weight=48.0)
    g.diag(673.1, -59.9, 561.9, 5.2, weight=48.0)
    g.diag(587.2, 436.8, 648.4, 307.0, weight=48.0)
    g.hbar(396.8, 552.3, 284.2, weight=96.0)
    g.hbar(552.3, 937.0, 286.4, weight=96.0)
    g.diag(584.0, 259.2, 634.9, 138.6, weight=48.0)
    return g
def g_cjk_unified_ideograph_6897() -> Glyph:
    """梗 U+6897 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6897", advance=1000, unicode=0x6897, note="梗：自动生成")
    g.hbar(88.7, 375.8, 489.1, weight=96.0)
    g.diag(220.7, 771.2, 256.7, 550.7, weight=48.0)
    g.vbar(251.6, -51.2, 550.7, weight=48.0)
    g.diag(245.3, 463.6, 53.0, 122.4, weight=48.0)
    g.hbar(282.7, 293.1, 398.6, weight=48.0)
    g.diag(293.1, 397.9, 367.5, 320.8, weight=48.0)
    g.diag(527.5, 611.7, 520.3, 621.2, weight=96.0)
    g.hbar(520.3, 764.4, 645.6, weight=96.0)
    g.diag(392.9, 499.1, 437.6, 467.5, weight=96.0)
    g.vbar(461.6, 253.3, 467.5, weight=96.0)
    g.hbar(461.1, 580.1, 471.8, weight=48.0)
    g.hbar(580.1, 792.3, 502.5, weight=48.0)
    g.vbar(760.2, 306.7, 518.2, weight=48.0)
    g.hbar(707.7, 728.2, 308.1, weight=48.0)
    g.hbar(482.3, 734.2, 385.3, weight=56.0)
    g.hbar(502.4, 699.4, 298.0, weight=76.0)
    g.vbar(555.4, 372.0, 599.6, weight=96.0)
    g.diag(546.9, 372.0, 284.5, -20.4, weight=96.0)
    g.diag(448.9, 242.0, 463.6, 158.7, weight=96.0)
    g.hbar(463.6, 937.0, 65.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_68a8() -> Glyph:
    """梨 U+68A8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni68A8", advance=1000, unicode=0x68A8, note="梨：自动生成")
    g.diag(508.6, 712.1, 431.1, 750.0, weight=96.0)
    g.hbar(223.3, 431.1, 715.6, weight=96.0)
    g.vbar(224.7, 603.6, 681.1, weight=96.0)
    g.hbar(154.1, 541.3, 580.9, weight=48.0)
    g.diag(332.9, 689.4, 366.9, 665.1, weight=92.0)
    g.vbar(361.0, 508.7, 665.1, weight=92.0)
    g.diag(355.2, 508.7, 418.5, 386.7, weight=92.0)
    g.diag(339.6, 557.0, 126.9, 382.3, weight=48.0)
    g.diag(374.8, 513.6, 479.6, 454.3, weight=48.0)
    g.diag(505.7, 714.4, 541.6, 679.3, weight=92.0)
    g.diag(541.6, 679.3, 582.3, 460.1, weight=92.0)
    g.diag(660.3, 772.0, 721.5, 729.7, weight=96.0)
    g.vbar(708.2, 394.6, 729.7, weight=96.0)
    g.diag(695.0, 394.6, 584.9, 456.9, weight=96.0)
    g.hbar(118.1, 855.6, 267.2, weight=48.0)
    g.vbar(465.8, 325.1, 418.0, weight=96.0)
    g.vbar(475.1, -52.0, 325.1, weight=96.0)
    g.diag(453.9, 256.3, 140.5, 23.8, weight=48.0)
    g.diag(510.2, 263.2, 722.1, 71.9, weight=48.0)
    g.hbar(722.1, 881.9, 63.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_68b0() -> Glyph:
    """械 U+68B0 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni68B0", advance=1000, unicode=0x68B0, note="械：自动生成")
    g.hbar(84.9, 372.3, 494.6, weight=96.0)
    g.vbar(236.9, -45.1, 771.7, weight=48.0)
    g.diag(245.6, 462.7, 53.0, 96.0, weight=48.0)
    g.dot(316.7, 374.6, w=48.0, h=62.4, slant=-14.0)
    g.hbar(423.8, 776.1, 524.0, weight=96.0)
    g.hbar(336.3, 627.8, 263.4, weight=96.0)
    g.diag(407.4, 376.2, 451.0, 327.8, weight=96.0)
    g.diag(451.0, 327.8, 361.0, 58.9, weight=96.0)
    g.diag(524.8, 418.4, 561.8, 377.1, weight=76.0)
    g.vbar(553.6, 47.6, 377.1, weight=76.0)
    g.diag(571.2, 785.1, 677.9, 503.5, weight=96.0)
    g.diag(677.9, 503.5, 897.6, -72.0, weight=96.0)
    g.diag(897.6, -72.0, 942.0, 164.0, weight=96.0)
    g.diag(793.7, 446.2, 760.6, 325.7, weight=48.0)
    g.diag(760.6, 325.7, 597.9, 73.3, weight=48.0)
    g.dot(798.8, 706.9, w=96.0, h=124.8, slant=-14.0)
    return g
def g_cjk_unified_ideograph_68cb() -> Glyph:
    """棋 U+68CB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni68CB", advance=1000, unicode=0x68CB, note="棋：自动生成")
    g.diag(201.2, 432.4, 166.1, 454.3, weight=96.0)
    g.hbar(166.1, 383.1, 479.6, weight=96.0)
    g.vbar(248.0, 478.6, 749.7, weight=48.0)
    g.vbar(256.7, -48.8, 478.6, weight=48.0)
    g.diag(258.4, 446.5, 210.1, 366.2, weight=48.0)
    g.diag(210.1, 366.2, 53.1, 119.6, weight=48.0)
    g.diag(299.9, 356.8, 362.0, 320.6, weight=96.0)
    g.hbar(311.4, 362.0, 309.3, weight=96.0)
    g.hbar(418.0, 802.3, 534.3, weight=92.0)
    g.hbar(758.4, 802.3, 567.9, weight=92.0)
    g.diag(483.8, 677.1, 513.2, 644.0, weight=96.0)
    g.vbar(524.5, 224.3, 644.0, weight=96.0)
    g.diag(535.8, 224.3, 511.9, 207.7, weight=96.0)
    g.diag(678.3, 772.0, 727.5, 731.9, weight=96.0)
    g.vbar(718.4, 258.0, 731.9, weight=96.0)
    g.diag(709.3, 258.0, 691.9, 233.9, weight=96.0)
    g.diag(555.4, 394.5, 564.9, 410.7, weight=76.0)
    g.hbar(564.9, 685.1, 412.6, weight=76.0)
    g.dot(613.6, 297.8, w=84.0, h=109.2, slant=-14.0)
    g.hbar(295.8, 931.9, 192.7, weight=76.0)
    g.diag(561.9, 157.1, 384.1, -72.0, weight=76.0)
    g.diag(684.3, 170.2, 850.6, -49.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_68da() -> Glyph:
    """棚 U+68DA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni68DA", advance=1000, unicode=0x68DA, note="棚：自动生成")
    g.hbar(97.5, 374.2, 467.9, weight=96.0)
    g.vbar(262.2, 483.0, 772.0, weight=48.0)
    g.vbar(267.2, -57.0, 483.0, weight=48.0)
    g.diag(264.3, 439.4, 221.8, 354.2, weight=48.0)
    g.diag(221.8, 354.2, 64.9, 91.5, weight=48.0)
    g.diag(314.2, 353.9, 318.7, 340.3, weight=48.0)
    g.diag(318.7, 340.3, 374.2, 290.9, weight=48.0)
    g.vbar(413.8, 448.6, 598.1, weight=48.0)
    g.diag(416.9, 448.6, 318.2, 31.5, weight=48.0)
    g.hbar(467.8, 470.8, 587.3, weight=56.0)
    g.diag(470.8, 586.7, 555.7, 411.8, weight=56.0)
    g.vbar(559.7, 74.5, 411.8, weight=56.0)
    g.hbar(473.9, 563.7, 94.7, weight=56.0)
    g.diag(467.8, 400.7, 480.1, 416.4, weight=96.0)
    g.hbar(480.1, 534.9, 417.7, weight=96.0)
    g.diag(444.4, 259.3, 465.4, 277.1, weight=96.0)
    g.hbar(465.4, 536.9, 278.4, weight=96.0)
    g.vbar(689.6, 454.3, 620.4, weight=56.0)
    g.diag(694.8, 454.3, 604.1, 5.0, weight=56.0)
    g.hbar(743.4, 764.8, 608.5, weight=48.0)
    g.diag(764.8, 605.7, 857.9, 453.0, weight=48.0)
    g.vbar(888.5, -17.4, 453.0, weight=48.0)
    g.hbar(774.9, 919.2, 12.2, weight=48.0)
    g.diag(756.6, 421.1, 768.0, 439.2, weight=96.0)
    g.hbar(768.0, 830.9, 438.8, weight=96.0)
    g.hbar(736.3, 762.8, 286.9, weight=96.0)
    g.hbar(762.8, 832.9, 293.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_68df() -> Glyph:
    """棟 U+68DF —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni68DF", advance=1000, unicode=0x68DF, note="棟：自动生成")
    g.hbar(98.3, 360.2, 482.7, weight=96.0)
    g.vbar(260.8, 498.2, 770.1, weight=48.0)
    g.vbar(269.0, 1.8, 498.2, weight=48.0)
    g.diag(264.4, 457.2, 217.6, 368.3, weight=48.0)
    g.diag(217.6, 368.3, 70.0, 125.0, weight=48.0)
    g.dot(343.7, 341.3, w=92.0, h=91.7, slant=-14.0)
    g.hbar(475.1, 737.9, 639.7, weight=84.0)
    g.diag(414.9, 517.4, 485.2, 312.1, weight=48.0)
    g.hbar(461.5, 580.9, 521.5, weight=48.0)
    g.hbar(580.9, 714.2, 501.3, weight=48.0)
    g.vbar(715.4, 347.7, 476.0, weight=48.0)
    g.hbar(694.1, 716.6, 347.2, weight=48.0)
    g.hbar(513.5, 675.0, 444.4, weight=56.0)
    g.hbar(502.5, 686.8, 348.1, weight=48.0)
    g.vbar(563.1, 499.7, 782.0, weight=48.0)
    g.vbar(576.3, -52.0, 499.7, weight=48.0)
    g.diag(564.6, 325.8, 520.3, 265.0, weight=48.0)
    g.diag(520.3, 265.0, 329.1, 73.9, weight=48.0)
    g.diag(610.2, 288.4, 925.0, 97.6, weight=48.0)
    return g
def g_cjk_unified_ideograph_68fa() -> Glyph:
    """棺 U+68FA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni68FA", advance=1000, unicode=0x68FA, note="棺：自动生成")
    g.hbar(122.2, 457.0, 507.7, weight=96.0)
    g.vbar(304.5, 493.7, 787.0, weight=48.0)
    g.vbar(315.6, -44.9, 493.7, weight=48.0)
    g.diag(315.7, 483.8, 260.5, 392.9, weight=48.0)
    g.diag(260.5, 392.9, 97.9, 137.5, weight=48.0)
    g.diag(351.3, 386.0, 418.3, 343.7, weight=48.0)
    g.diag(418.3, 343.7, 436.3, 308.7, weight=48.0)
    g.diag(614.6, 765.7, 698.7, 715.1, weight=84.0)
    g.diag(698.7, 715.1, 730.2, 625.7, weight=84.0)
    g.diag(510.7, 571.1, 475.8, 462.8, weight=96.0)
    g.diag(475.8, 462.8, 499.4, 427.3, weight=96.0)
    g.hbar(526.9, 903.8, 571.9, weight=64.0)
    g.diag(903.8, 603.6, 784.3, 458.0, weight=64.0)
    g.vbar(566.3, -52.0, 413.9, weight=48.0)
    g.hbar(580.5, 813.7, 417.5, weight=48.0)
    g.diag(813.7, 435.3, 749.2, 328.9, weight=48.0)
    g.hbar(594.3, 616.0, 288.0, weight=48.0)
    g.hbar(616.0, 779.2, 308.6, weight=48.0)
    g.hbar(594.3, 799.6, 177.9, weight=48.0)
    g.diag(799.6, 202.1, 837.0, 162.2, weight=48.0)
    g.diag(837.0, 162.2, 780.0, 75.8, weight=48.0)
    g.hbar(579.2, 853.8, 34.6, weight=48.0)
    return g
def g_cjk_unified_ideograph_6905() -> Glyph:
    """椅 U+6905 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6905", advance=1000, unicode=0x6905, note="椅：自动生成")
    g.hbar(98.8, 337.5, 507.8, weight=96.0)
    g.diag(337.5, 529.3, 430.7, 483.1, weight=96.0)
    g.vbar(255.3, 492.7, 764.1, weight=48.0)
    g.vbar(266.1, -18.4, 492.7, weight=48.0)
    g.diag(265.4, 476.4, 53.0, 136.5, weight=48.0)
    g.hbar(302.5, 306.9, 426.3, weight=48.0)
    g.diag(306.9, 425.6, 351.4, 386.0, weight=48.0)
    g.hbar(351.4, 398.5, 386.3, weight=48.0)
    g.hbar(458.4, 777.1, 656.0, weight=56.0)
    g.vbar(587.4, 664.1, 680.9, weight=96.0)
    g.diag(587.0, 664.1, 454.6, 433.1, weight=96.0)
    g.diag(599.7, 585.2, 721.0, 521.0, weight=48.0)
    g.diag(721.0, 521.0, 738.3, 457.2, weight=48.0)
    g.hbar(394.0, 932.0, 413.1, weight=96.0)
    g.vbar(454.7, 151.2, 305.3, weight=48.0)
    g.hbar(447.7, 609.3, 303.4, weight=48.0)
    g.diag(609.3, 313.1, 559.8, 207.6, weight=48.0)
    g.diag(481.8, 164.8, 497.1, 180.1, weight=96.0)
    g.hbar(497.1, 597.1, 186.7, weight=96.0)
    g.diag(690.3, 407.5, 739.0, 376.8, weight=96.0)
    g.vbar(721.5, -48.4, 376.8, weight=96.0)
    g.diag(704.1, -48.4, 597.7, 5.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_690e() -> Glyph:
    """椎 U+690E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni690E", advance=1000, unicode=0x690E, note="椎：自动生成")
    g.hbar(114.4, 402.0, 497.1, weight=96.0)
    g.vbar(268.4, 502.2, 784.2, weight=48.0)
    g.vbar(281.1, -32.7, 502.2, weight=48.0)
    g.diag(274.8, 466.2, 233.3, 390.6, weight=48.0)
    g.diag(233.3, 390.6, 79.2, 144.4, weight=48.0)
    g.diag(324.7, 363.5, 394.2, 293.7, weight=48.0)
    g.vbar(394.2, 275.5, 293.7, weight=48.0)
    g.diag(547.8, 792.0, 527.5, 663.8, weight=48.0)
    g.diag(527.5, 663.8, 389.3, 397.8, weight=48.0)
    g.vbar(494.5, -62.0, 495.6, weight=48.0)
    g.diag(631.9, 690.3, 738.5, 615.9, weight=56.0)
    g.hbar(565.4, 842.2, 537.2, weight=96.0)
    g.hbar(592.8, 806.0, 377.2, weight=96.0)
    g.hbar(588.9, 809.9, 255.9, weight=96.0)
    g.diag(668.1, 498.5, 693.5, 479.0, weight=96.0)
    g.vbar(694.4, 165.2, 479.0, weight=96.0)
    g.diag(695.3, 165.2, 679.8, 142.5, weight=96.0)
    g.diag(537.0, 107.2, 546.7, 98.5, weight=96.0)
    g.hbar(546.7, 905.8, 109.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_6977() -> Glyph:
    """楷 U+6977 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6977", advance=1000, unicode=0x6977, note="楷：自动生成")
    g.hbar(120.9, 442.8, 499.8, weight=96.0)
    g.vbar(281.1, -30.1, 772.0, weight=48.0)
    g.diag(292.3, 473.4, 243.1, 383.2, weight=48.0)
    g.diag(243.1, 383.2, 84.7, 123.5, weight=48.0)
    g.diag(328.8, 370.6, 387.0, 327.6, weight=48.0)
    g.diag(387.0, 327.6, 400.4, 293.2, weight=48.0)
    g.dot(566.2, 562.2, w=96.0, h=119.2, slant=-14.0)
    g.diag(446.1, 676.6, 501.8, 399.1, weight=64.0)
    g.hbar(501.8, 598.3, 400.4, weight=64.0)
    g.hbar(710.8, 813.4, 674.1, weight=96.0)
    g.diag(813.4, 656.5, 685.5, 566.0, weight=96.0)
    g.diag(641.6, 765.3, 623.2, 789.4, weight=96.0)
    g.diag(623.2, 789.4, 704.6, 415.2, weight=96.0)
    g.hbar(704.6, 890.9, 410.7, weight=96.0)
    g.diag(890.9, 406.2, 831.0, 613.4, weight=96.0)
    g.diag(576.1, 417.2, 623.6, 349.0, weight=48.0)
    g.diag(623.6, 349.0, 553.2, 253.1, weight=48.0)
    g.diag(506.9, 248.3, 501.5, 236.5, weight=48.0)
    g.vbar(511.1, 11.0, 236.5, weight=48.0)
    g.diag(520.7, 11.0, 537.8, -5.2, weight=48.0)
    g.hbar(517.4, 744.7, 256.5, weight=48.0)
    g.vbar(756.6, 154.6, 273.6, weight=48.0)
    g.vbar(763.7, -52.0, 154.6, weight=48.0)
    g.hbar(541.5, 742.7, 128.0, weight=92.0)
    g.diag(548.2, 10.9, 561.5, 21.4, weight=92.0)
    g.hbar(561.5, 730.6, 24.1, weight=92.0)
    return g
def g_cjk_unified_ideograph_697c() -> Glyph:
    """楼 U+697C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni697C", advance=1000, unicode=0x697C, note="楼：自动生成")
    g.hbar(102.8, 402.6, 484.8, weight=96.0)
    g.vbar(278.1, 470.3, 747.4, weight=48.0)
    g.vbar(285.5, -44.2, 470.3, weight=48.0)
    g.diag(286.7, 454.3, 239.0, 373.5, weight=48.0)
    g.diag(239.0, 373.5, 80.1, 120.4, weight=48.0)
    g.hbar(321.6, 330.4, 366.3, weight=48.0)
    g.diag(330.4, 365.4, 394.1, 306.5, weight=48.0)
    g.diag(394.1, 306.5, 432.3, 327.5, weight=48.0)
    g.diag(485.2, 643.9, 522.7, 617.2, weight=64.0)
    g.diag(522.7, 617.2, 554.8, 535.6, weight=64.0)
    g.diag(759.2, 713.8, 774.0, 684.3, weight=48.0)
    g.diag(774.0, 684.3, 650.9, 611.5, weight=48.0)
    g.hbar(414.6, 823.3, 525.7, weight=48.0)
    g.diag(595.6, 772.0, 618.8, 628.4, weight=48.0)
    g.vbar(608.8, 328.3, 628.4, weight=48.0)
    g.diag(605.9, 491.9, 486.3, 371.9, weight=48.0)
    g.diag(486.3, 371.9, 409.6, 318.7, weight=48.0)
    g.diag(644.9, 501.2, 919.9, 361.9, weight=48.0)
    g.diag(591.0, 338.4, 636.8, 454.6, weight=96.0)
    g.diag(636.8, 454.6, 534.7, 140.6, weight=96.0)
    g.diag(534.7, 140.6, 805.6, -57.0, weight=96.0)
    g.diag(684.2, 259.8, 646.7, 177.6, weight=48.0)
    g.diag(646.7, 177.6, 417.2, -21.5, weight=48.0)
    g.hbar(378.8, 916.0, 224.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_6982() -> Glyph:
    """概 U+6982 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6982", advance=1000, unicode=0x6982, note="概：自动生成")
    g.hbar(127.7, 180.6, 455.3, weight=96.0)
    g.hbar(127.7, 337.3, 491.2, weight=96.0)
    g.vbar(214.7, -47.5, 757.5, weight=48.0)
    g.diag(228.3, 459.6, 53.0, 133.5, weight=48.0)
    g.diag(264.5, 403.8, 359.0, 335.6, weight=48.0)
    g.diag(386.3, 580.6, 490.5, 524.2, weight=48.0)
    g.vbar(496.5, 372.5, 524.2, weight=48.0)
    g.hbar(488.3, 502.6, 373.9, weight=48.0)
    g.vbar(408.1, 473.7, 488.5, weight=84.0)
    g.hbar(410.1, 488.1, 494.8, weight=84.0)
    g.diag(405.1, 359.0, 412.0, 369.8, weight=96.0)
    g.hbar(412.0, 478.2, 380.7, weight=96.0)
    g.vbar(378.6, 480.5, 591.5, weight=48.0)
    g.diag(374.7, 480.5, 413.8, 194.7, weight=48.0)
    g.diag(413.8, 194.7, 484.6, 236.0, weight=48.0)
    g.diag(484.6, 236.0, 493.5, 251.9, weight=48.0)
    g.diag(484.8, 267.6, 518.8, 251.2, weight=48.0)
    g.diag(518.8, 251.2, 501.0, 226.1, weight=48.0)
    g.hbar(646.6, 847.1, 623.3, weight=96.0)
    g.diag(543.1, 514.1, 610.8, 482.6, weight=48.0)
    g.diag(610.8, 482.6, 583.9, 350.4, weight=48.0)
    g.hbar(583.9, 874.8, 368.0, weight=48.0)
    g.vbar(673.1, 417.6, 588.4, weight=96.0)
    g.diag(663.2, 417.6, 426.8, -7.9, weight=96.0)
    g.diag(710.1, 296.3, 738.4, 216.8, weight=64.0)
    g.diag(738.4, 216.8, 841.9, 5.7, weight=64.0)
    g.hbar(841.9, 934.9, 5.3, weight=64.0)
    g.vbar(940.9, 4.8, 152.3, weight=64.0)
    return g
def g_cjk_unified_ideograph_69cb() -> Glyph:
    """構 U+69CB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni69CB", advance=1000, unicode=0x69CB, note="構：自动生成")
    g.hbar(163.1, 222.9, 458.1, weight=96.0)
    g.hbar(163.1, 454.5, 488.0, weight=96.0)
    g.vbar(265.5, 483.8, 748.7, weight=48.0)
    g.vbar(272.0, -15.6, 483.8, weight=48.0)
    g.diag(272.3, 458.2, 66.4, 137.4, weight=48.0)
    g.dot(371.2, 343.2, w=96.0, h=124.8, slant=-14.0)
    g.hbar(520.7, 537.0, 603.2, weight=76.0)
    g.hbar(537.0, 753.8, 627.3, weight=76.0)
    g.diag(753.8, 654.8, 783.4, 580.6, weight=76.0)
    g.hbar(527.4, 530.6, 499.5, weight=64.0)
    g.hbar(527.4, 732.7, 527.0, weight=64.0)
    g.hbar(714.0, 732.7, 554.9, weight=64.0)
    g.diag(507.7, 640.2, 545.4, 679.0, weight=96.0)
    g.vbar(552.0, 461.3, 679.0, weight=96.0)
    g.diag(558.7, 461.3, 546.0, 439.8, weight=96.0)
    g.diag(659.9, 772.0, 699.1, 737.5, weight=64.0)
    g.vbar(691.6, 484.6, 737.5, weight=64.0)
    g.diag(684.1, 484.6, 668.3, 462.2, weight=64.0)
    g.hbar(378.7, 878.2, 402.0, weight=64.0)
    g.vbar(484.9, -18.4, 321.7, weight=48.0)
    g.hbar(508.9, 737.1, 334.2, weight=48.0)
    g.diag(737.1, 355.1, 765.1, 209.3, weight=48.0)
    g.vbar(752.9, -46.0, 209.3, weight=48.0)
    g.diag(740.8, -46.0, 667.3, -7.2, weight=48.0)
    g.hbar(527.1, 747.7, 238.3, weight=76.0)
    g.diag(598.3, 408.1, 624.2, 386.3, weight=48.0)
    g.vbar(620.7, 170.4, 386.3, weight=48.0)
    g.diag(617.3, 170.4, 606.0, 159.2, weight=48.0)
    g.hbar(302.2, 928.6, 136.2, weight=76.0)
    return g
def g_cjk_unified_ideograph_69fd() -> Glyph:
    """槽 U+69FD —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni69FD", advance=1000, unicode=0x69FD, note="槽：自动生成")
    g.hbar(131.6, 417.2, 501.8, weight=92.0)
    g.vbar(283.1, 473.6, 751.1, weight=48.0)
    g.vbar(293.8, -54.0, 473.6, weight=48.0)
    g.diag(294.2, 477.1, 245.7, 389.4, weight=48.0)
    g.diag(245.7, 389.4, 99.6, 134.4, weight=48.0)
    g.diag(333.6, 359.7, 469.0, 298.8, weight=64.0)
    g.hbar(548.6, 584.5, 604.7, weight=92.0)
    g.hbar(584.5, 781.1, 623.1, weight=92.0)
    g.hbar(754.4, 781.1, 644.3, weight=92.0)
    g.vbar(463.0, 455.9, 477.6, weight=48.0)
    g.vbar(479.8, 275.2, 455.9, weight=48.0)
    g.hbar(474.5, 845.5, 494.9, weight=48.0)
    g.diag(845.5, 522.8, 880.4, 481.1, weight=48.0)
    g.diag(880.4, 481.1, 813.3, 321.2, weight=48.0)
    g.hbar(499.8, 829.6, 389.5, weight=56.0)
    g.diag(541.5, 710.3, 582.3, 678.3, weight=76.0)
    g.vbar(589.5, 334.5, 678.3, weight=76.0)
    g.diag(596.8, 334.5, 584.2, 318.0, weight=76.0)
    g.diag(682.3, 789.0, 725.7, 749.6, weight=76.0)
    g.vbar(708.3, 352.0, 749.6, weight=76.0)
    g.diag(691.0, 352.0, 674.5, 330.6, weight=76.0)
    g.hbar(516.2, 811.3, 310.5, weight=48.0)
    g.vbar(535.7, 187.1, 215.2, weight=48.0)
    g.vbar(543.2, -39.1, 187.1, weight=48.0)
    g.hbar(551.6, 759.2, 222.2, weight=48.0)
    g.vbar(770.5, 143.1, 236.8, weight=48.0)
    g.vbar(781.2, -30.7, 143.1, weight=48.0)
    g.hbar(726.9, 780.4, -23.9, weight=48.0)
    g.diag(570.6, 88.8, 582.0, 105.8, weight=84.0)
    g.hbar(582.0, 759.4, 108.9, weight=84.0)
    g.diag(567.7, -23.9, 581.0, -11.8, weight=92.0)
    g.hbar(581.0, 738.6, -4.7, weight=92.0)
    return g
def g_cjk_unified_ideograph_6a19() -> Glyph:
    """標 U+6A19 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6A19", advance=1000, unicode=0x6A19, note="標：自动生成")
    g.hbar(83.3, 380.1, 507.4, weight=96.0)
    g.vbar(257.3, -55.2, 770.2, weight=48.0)
    g.diag(270.7, 473.2, 53.0, 113.3, weight=48.0)
    g.diag(315.4, 384.7, 372.4, 342.1, weight=96.0)
    g.diag(372.4, 342.1, 323.2, 314.5, weight=96.0)
    g.hbar(493.5, 753.3, 713.7, weight=96.0)
    g.diag(753.3, 739.0, 809.9, 656.2, weight=96.0)
    g.vbar(443.0, 541.2, 564.7, weight=48.0)
    g.vbar(466.3, 393.8, 541.2, weight=48.0)
    g.hbar(454.3, 821.7, 586.6, weight=48.0)
    g.diag(821.7, 618.7, 852.7, 575.7, weight=48.0)
    g.diag(852.7, 575.7, 787.7, 442.0, weight=48.0)
    g.hbar(763.6, 787.7, 443.5, weight=48.0)
    g.diag(526.3, 668.3, 588.5, 462.2, weight=76.0)
    g.diag(588.5, 462.2, 568.6, 446.3, weight=76.0)
    g.diag(672.6, 698.6, 709.5, 664.9, weight=64.0)
    g.diag(709.5, 664.9, 660.5, 463.5, weight=64.0)
    g.hbar(507.1, 758.9, 431.4, weight=76.0)
    g.diag(493.7, 359.3, 521.7, 308.6, weight=84.0)
    g.hbar(521.7, 769.0, 347.4, weight=84.0)
    g.hbar(317.3, 942.0, 226.0, weight=84.0)
    g.diag(614.0, 201.1, 657.6, 168.5, weight=92.0)
    g.diag(657.6, 168.5, 619.9, -46.4, weight=92.0)
    g.diag(619.9, -46.4, 480.2, 28.9, weight=92.0)
    g.diag(471.8, 158.6, 428.8, 9.7, weight=96.0)
    g.hbar(428.8, 502.1, -0.3, weight=96.0)
    g.diag(749.4, 209.7, 894.6, 5.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_6a21() -> Glyph:
    """模 U+6A21 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6A21", advance=1000, unicode=0x6A21, note="模：自动生成")
    g.hbar(91.3, 314.8, 481.9, weight=96.0)
    g.diag(314.8, 503.4, 317.6, 508.9, weight=96.0)
    g.vbar(245.3, -51.7, 744.0, weight=48.0)
    g.diag(258.1, 455.5, 212.7, 369.2, weight=48.0)
    g.diag(212.7, 369.2, 53.0, 101.4, weight=48.0)
    g.hbar(297.3, 448.9, 355.0, weight=84.0)
    g.hbar(370.3, 838.9, 588.5, weight=96.0)
    g.diag(467.0, 697.9, 503.3, 673.4, weight=48.0)
    g.diag(503.3, 673.4, 538.8, 496.6, weight=48.0)
    g.vbar(675.6, 672.7, 679.3, weight=96.0)
    g.diag(675.6, 679.3, 639.0, 532.0, weight=96.0)
    g.vbar(452.2, 458.6, 475.6, weight=48.0)
    g.vbar(473.5, 277.0, 458.6, weight=48.0)
    g.hbar(462.5, 767.3, 476.3, weight=48.0)
    g.vbar(728.3, 308.2, 485.1, weight=48.0)
    g.diag(499.5, 369.5, 515.3, 386.9, weight=64.0)
    g.hbar(515.3, 701.2, 384.7, weight=64.0)
    g.diag(514.1, 287.8, 521.8, 298.3, weight=64.0)
    g.hbar(521.8, 678.7, 309.1, weight=64.0)
    g.hbar(289.1, 892.8, 174.9, weight=56.0)
    g.diag(558.3, 280.9, 643.8, 223.0, weight=92.0)
    g.diag(643.8, 223.0, 289.9, -44.6, weight=92.0)
    g.diag(600.5, 153.6, 937.0, -36.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_6a39() -> Glyph:
    """樹 U+6A39 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6A39", advance=1000, unicode=0x6A39, note="樹：自动生成")
    g.diag(199.3, 405.4, 160.8, 431.3, weight=96.0)
    g.hbar(160.8, 392.6, 439.3, weight=96.0)
    g.vbar(245.5, 448.5, 703.7, weight=48.0)
    g.vbar(256.9, -44.6, 448.5, weight=48.0)
    g.diag(253.7, 417.4, 206.0, 334.6, weight=48.0)
    g.diag(206.0, 334.6, 53.0, 87.6, weight=48.0)
    g.diag(290.4, 342.4, 325.9, 313.9, weight=48.0)
    g.hbar(325.9, 377.2, 319.6, weight=48.0)
    g.diag(383.6, 504.0, 415.6, 529.3, weight=92.0)
    g.hbar(415.6, 603.1, 551.1, weight=92.0)
    g.hbar(557.3, 603.1, 575.9, weight=92.0)
    g.diag(482.8, 764.6, 530.8, 723.1, weight=96.0)
    g.vbar(516.8, 457.5, 723.1, weight=96.0)
    g.hbar(421.0, 574.6, 437.9, weight=48.0)
    g.diag(574.6, 454.5, 629.5, 417.1, weight=48.0)
    g.diag(379.1, 351.9, 437.7, 237.2, weight=48.0)
    g.hbar(388.6, 603.4, 360.5, weight=48.0)
    g.diag(603.4, 366.2, 548.1, 300.1, weight=48.0)
    g.hbar(448.5, 579.1, 276.1, weight=48.0)
    g.dot(426.5, 166.3, w=96.0, h=100.2, slant=-14.0)
    g.diag(531.3, 256.8, 559.7, 225.0, weight=96.0)
    g.diag(559.7, 225.0, 505.6, 122.8, weight=96.0)
    g.hbar(295.5, 382.9, 69.1, weight=96.0)
    g.hbar(382.9, 679.7, 117.5, weight=96.0)
    g.diag(617.4, 434.4, 670.4, 400.7, weight=56.0)
    g.hbar(670.4, 942.0, 422.4, weight=56.0)
    g.diag(751.8, 711.3, 784.9, 484.0, weight=96.0)
    g.vbar(780.5, -33.3, 484.0, weight=96.0)
    g.diag(776.1, -33.3, 686.5, 7.5, weight=96.0)
    g.diag(686.5, 7.5, 644.7, 104.9, weight=96.0)
    g.diag(628.3, 283.7, 696.7, 232.1, weight=96.0)
    g.diag(696.7, 232.1, 671.9, 169.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_6b04() -> Glyph:
    """欄 U+6B04 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6B04", advance=1000, unicode=0x6B04, note="欄：自动生成")
    g.hbar(104.5, 366.1, 486.3, weight=96.0)
    g.vbar(256.1, 490.0, 772.0, weight=48.0)
    g.vbar(263.6, -52.0, 490.0, weight=48.0)
    g.diag(257.3, 458.4, 85.5, 111.8, weight=48.0)
    g.dot(333.7, 333.0, w=96.0, h=87.7, slant=-14.0)
    g.vbar(398.4, 481.6, 682.1, weight=48.0)
    g.vbar(405.3, -2.1, 481.6, weight=48.0)
    g.diag(446.1, 666.1, 455.0, 661.1, weight=48.0)
    g.hbar(455.0, 591.1, 681.1, weight=48.0)
    g.vbar(565.0, 477.2, 701.2, weight=48.0)
    g.hbar(538.9, 540.9, 477.3, weight=48.0)
    g.diag(450.0, 552.3, 457.9, 568.1, weight=64.0)
    g.hbar(457.9, 520.0, 571.6, weight=64.0)
    g.vbar(451.5, 465.4, 474.4, weight=64.0)
    g.hbar(453.0, 532.9, 484.8, weight=64.0)
    g.diag(659.8, 741.0, 704.7, 493.3, weight=84.0)
    g.hbar(714.7, 834.8, 718.4, weight=48.0)
    g.vbar(851.3, 458.9, 737.6, weight=48.0)
    g.vbar(899.2, -74.3, 458.9, weight=48.0)
    g.diag(930.7, -74.3, 762.7, 6.9, weight=48.0)
    g.dot(758.2, 618.2, w=76.0, h=88.4, slant=-14.0)
    g.diag(720.7, 510.3, 734.3, 523.9, weight=76.0)
    g.hbar(734.3, 853.6, 525.1, weight=76.0)
    g.hbar(546.9, 725.7, 399.5, weight=48.0)
    g.vbar(499.5, 170.7, 319.5, weight=48.0)
    g.hbar(511.0, 779.8, 332.8, weight=48.0)
    g.vbar(757.3, 200.7, 349.9, weight=48.0)
    g.dot(577.9, 254.6, w=48.0, h=44.0, slant=-14.0)
    g.hbar(699.9, 715.7, 285.0, weight=48.0)
    g.diag(699.9, 286.4, 661.8, 252.3, weight=48.0)
    g.vbar(661.8, 246.6, 252.3, weight=48.0)
    g.hbar(539.9, 715.7, 198.7, weight=48.0)
    g.diag(609.9, 451.4, 627.1, 320.8, weight=48.0)
    g.vbar(632.4, -42.0, 320.8, weight=48.0)
    g.diag(608.9, 176.7, 479.0, 32.9, weight=48.0)
    g.dot(731.2, 102.8, w=96.0, h=117.5, slant=-14.0)
    return g
def g_cjk_unified_ideograph_6b3a() -> Glyph:
    """欺 U+6B3A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6B3A", advance=1000, unicode=0x6B3A, note="欺：自动生成")
    g.hbar(154.9, 524.6, 538.9, weight=84.0)
    g.diag(227.1, 660.4, 317.6, 550.4, weight=96.0)
    g.diag(317.6, 550.4, 261.8, 348.5, weight=96.0)
    g.vbar(256.2, 223.4, 348.5, weight=96.0)
    g.diag(395.9, 750.1, 440.7, 712.3, weight=76.0)
    g.vbar(430.0, 276.0, 712.3, weight=76.0)
    g.diag(419.2, 276.0, 402.7, 251.7, weight=76.0)
    g.diag(291.5, 409.7, 300.7, 423.5, weight=76.0)
    g.hbar(300.7, 369.5, 424.4, weight=76.0)
    g.diag(290.5, 318.0, 302.2, 333.2, weight=64.0)
    g.hbar(302.2, 369.5, 333.9, weight=64.0)
    g.hbar(73.0, 518.8, 209.2, weight=64.0)
    g.hbar(285.5, 301.3, 114.0, weight=64.0)
    g.diag(285.5, 113.0, 105.2, -35.1, weight=64.0)
    g.dot(420.3, 114.6, w=96.0, h=90.4, slant=-14.0)
    g.diag(620.2, 738.4, 664.4, 696.3, weight=64.0)
    g.diag(664.4, 696.3, 501.2, 363.8, weight=64.0)
    g.hbar(601.7, 820.2, 491.2, weight=96.0)
    g.diag(820.2, 506.4, 737.3, 401.9, weight=96.0)
    g.diag(591.0, 390.2, 661.5, 329.4, weight=96.0)
    g.diag(661.5, 329.4, 435.9, 1.0, weight=96.0)
    g.diag(643.6, 239.0, 947.0, -10.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_6b3e() -> Glyph:
    """款 U+6B3E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6B3E", advance=1000, unicode=0x6B3E, note="款：自动生成")
    g.diag(186.2, 490.3, 221.9, 576.5, weight=92.0)
    g.hbar(221.9, 573.0, 579.1, weight=92.0)
    g.diag(312.1, 742.7, 351.3, 707.6, weight=96.0)
    g.vbar(346.8, 518.7, 707.6, weight=96.0)
    g.diag(342.2, 518.7, 326.2, 497.6, weight=96.0)
    g.diag(204.7, 394.3, 246.8, 452.4, weight=76.0)
    g.hbar(246.8, 389.5, 471.0, weight=76.0)
    g.diag(389.5, 489.6, 443.7, 421.3, weight=76.0)
    g.diag(211.9, 424.9, 260.8, 364.8, weight=76.0)
    g.hbar(260.8, 461.4, 370.4, weight=76.0)
    g.hbar(68.0, 485.6, 265.8, weight=92.0)
    g.diag(315.1, 238.4, 354.7, 208.8, weight=56.0)
    g.diag(354.7, 208.8, 318.3, -15.4, weight=56.0)
    g.diag(318.3, -15.4, 182.1, 50.6, weight=56.0)
    g.diag(187.9, 190.3, 147.4, 31.7, weight=96.0)
    g.hbar(147.4, 185.5, 24.3, weight=96.0)
    g.dot(430.2, 126.3, w=96.0, h=124.8, slant=-14.0)
    g.diag(609.5, 715.6, 658.1, 670.2, weight=96.0)
    g.diag(658.1, 670.2, 463.8, 361.2, weight=96.0)
    g.hbar(577.3, 842.2, 472.6, weight=96.0)
    g.diag(842.2, 497.7, 653.1, 349.2, weight=96.0)
    g.diag(540.1, 396.2, 559.0, 240.9, weight=56.0)
    g.diag(559.0, 240.9, 424.6, -9.7, weight=56.0)
    g.diag(638.6, 243.5, 947.0, -17.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_6b4c() -> Glyph:
    """歌 U+6B4C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6B4C", advance=1000, unicode=0x6B4C, note="歌：自动生成")
    g.hbar(206.0, 447.1, 664.1, weight=64.0)
    g.vbar(453.8, 648.8, 680.9, weight=64.0)
    g.vbar(221.9, 427.4, 548.0, weight=48.0)
    g.hbar(220.4, 352.2, 551.0, weight=48.0)
    g.vbar(344.3, 500.1, 555.8, weight=48.0)
    g.diag(336.4, 500.1, 316.7, 481.2, weight=48.0)
    g.hbar(252.6, 345.9, 454.3, weight=48.0)
    g.vbar(346.9, 467.3, 484.6, weight=48.0)
    g.diag(421.2, 645.4, 447.4, 627.9, weight=96.0)
    g.vbar(440.6, 420.2, 627.9, weight=96.0)
    g.hbar(83.0, 506.7, 367.5, weight=64.0)
    g.dot(196.3, 194.0, w=96.0, h=124.8, slant=-14.0)
    g.hbar(206.9, 341.3, 260.9, weight=48.0)
    g.diag(341.3, 271.9, 300.1, 191.7, weight=48.0)
    g.diag(229.0, 150.5, 236.5, 158.0, weight=48.0)
    g.hbar(236.5, 326.3, 174.0, weight=48.0)
    g.diag(391.3, 352.4, 433.4, 314.0, weight=56.0)
    g.vbar(417.2, -3.3, 314.0, weight=56.0)
    g.hbar(312.2, 401.0, 16.4, weight=56.0)
    g.hbar(538.0, 673.0, 709.0, weight=96.0)
    g.diag(673.0, 720.4, 519.3, 402.2, weight=96.0)
    g.hbar(595.4, 832.4, 497.0, weight=96.0)
    g.diag(832.4, 519.9, 663.9, 370.7, weight=96.0)
    g.diag(554.1, 414.9, 576.0, 278.6, weight=48.0)
    g.diag(576.0, 278.6, 438.9, 60.9, weight=48.0)
    g.vbar(642.9, 240.5, 256.0, weight=96.0)
    g.diag(642.9, 240.5, 797.4, 76.1, weight=96.0)
    g.hbar(797.4, 942.0, 60.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_6b89() -> Glyph:
    """殉 U+6B89 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6B89", advance=1000, unicode=0x6B89, note="殉：自动生成")
    g.hbar(233.7, 428.8, 654.9, weight=96.0)
    g.hbar(428.8, 570.2, 666.5, weight=96.0)
    g.diag(269.7, 619.6, 254.7, 506.3, weight=48.0)
    g.diag(254.7, 506.3, 101.3, 257.1, weight=48.0)
    g.diag(272.2, 464.8, 312.2, 334.9, weight=48.0)
    g.diag(312.2, 334.9, 113.8, 3.7, weight=48.0)
    g.dot(235.5, 282.5, w=96.0, h=123.0, slant=-14.0)
    g.vbar(617.6, 682.6, 792.0, weight=48.0)
    g.diag(612.7, 682.6, 482.9, 429.8, weight=48.0)
    g.diag(562.2, 522.4, 792.9, 333.3, weight=48.0)
    g.vbar(802.8, -65.4, 333.3, weight=48.0)
    g.diag(812.6, -65.4, 669.7, 3.7, weight=48.0)
    g.diag(504.5, 404.9, 479.7, 355.6, weight=48.0)
    g.diag(479.7, 355.6, 508.6, 132.8, weight=48.0)
    g.hbar(514.8, 661.5, 410.3, weight=48.0)
    g.vbar(673.6, 310.4, 423.5, weight=48.0)
    g.vbar(689.8, 84.3, 310.4, weight=48.0)
    g.diag(530.5, 263.3, 546.2, 283.8, weight=92.0)
    g.hbar(546.2, 658.9, 282.3, weight=92.0)
    g.diag(524.2, 144.0, 533.6, 157.6, weight=96.0)
    g.hbar(533.6, 650.6, 164.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_6b8a() -> Glyph:
    """殊 U+6B8A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6B8A", advance=1000, unicode=0x6B8A, note="殊：自动生成")
    g.hbar(168.6, 407.2, 595.0, weight=96.0)
    g.diag(202.4, 572.9, 238.5, 538.3, weight=48.0)
    g.diag(238.5, 538.3, 104.4, 310.7, weight=48.0)
    g.diag(104.4, 310.7, 107.4, 305.1, weight=48.0)
    g.diag(182.8, 398.4, 228.2, 299.8, weight=48.0)
    g.diag(228.2, 299.8, 58.0, 24.7, weight=48.0)
    g.dot(164.3, 282.1, w=96.0, h=103.8, slant=-14.0)
    g.diag(410.4, 616.0, 483.6, 567.8, weight=96.0)
    g.diag(483.6, 567.8, 339.4, 414.9, weight=96.0)
    g.hbar(475.3, 747.0, 529.7, weight=96.0)
    g.hbar(370.5, 826.5, 361.4, weight=48.0)
    g.vbar(569.8, 486.3, 770.9, weight=96.0)
    g.vbar(584.4, -55.9, 486.3, weight=96.0)
    g.diag(571.2, 343.7, 518.1, 275.2, weight=48.0)
    g.diag(518.1, 275.2, 304.5, 62.5, weight=48.0)
    g.diag(617.9, 336.2, 798.2, 125.9, weight=48.0)
    g.hbar(798.2, 942.0, 107.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_6b96() -> Glyph:
    """殖 U+6B96 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6B96", advance=1000, unicode=0x6B96, note="殖：自动生成")
    g.hbar(183.9, 381.6, 622.8, weight=96.0)
    g.diag(381.6, 656.4, 423.5, 611.6, weight=96.0)
    g.diag(217.2, 586.7, 197.8, 478.4, weight=56.0)
    g.diag(197.8, 478.4, 58.0, 231.0, weight=56.0)
    g.diag(213.6, 418.2, 265.9, 294.6, weight=48.0)
    g.diag(265.9, 294.6, 91.9, -29.6, weight=48.0)
    g.dot(203.4, 272.0, w=96.0, h=124.8, slant=-14.0)
    g.diag(423.5, 615.3, 476.3, 566.9, weight=96.0)
    g.hbar(476.3, 837.7, 593.9, weight=96.0)
    g.diag(591.9, 762.8, 610.0, 643.8, weight=48.0)
    g.diag(610.0, 643.8, 584.6, 442.7, weight=48.0)
    g.vbar(499.7, 306.3, 426.6, weight=48.0)
    g.vbar(491.2, 2.3, 306.3, weight=48.0)
    g.hbar(508.6, 713.6, 435.2, weight=48.0)
    g.diag(713.6, 454.1, 736.5, 353.3, weight=48.0)
    g.vbar(737.1, 66.3, 353.3, weight=48.0)
    g.diag(737.6, 66.3, 718.9, 28.1, weight=48.0)
    g.diag(531.5, 279.7, 547.7, 297.5, weight=76.0)
    g.hbar(547.7, 711.9, 303.8, weight=76.0)
    g.hbar(527.5, 715.9, 197.4, weight=64.0)
    g.hbar(527.3, 715.1, 106.9, weight=64.0)
    g.hbar(325.0, 932.0, -11.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_6bbf() -> Glyph:
    """殿 U+6BBF —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6BBF", advance=1000, unicode=0x6BBF, note="殿：自动生成")
    g.hbar(257.8, 478.3, 653.4, weight=48.0)
    g.vbar(462.2, 601.2, 680.5, weight=48.0)
    g.hbar(425.8, 446.0, 597.3, weight=48.0)
    g.hbar(252.0, 464.4, 538.0, weight=48.0)
    g.vbar(186.8, 453.3, 654.3, weight=84.0)
    g.diag(184.3, 453.3, 58.0, 34.6, weight=84.0)
    g.hbar(253.9, 501.1, 378.7, weight=96.0)
    g.diag(282.9, 454.5, 315.7, 418.8, weight=48.0)
    g.vbar(318.6, 275.9, 418.8, weight=48.0)
    g.diag(321.5, 275.9, 309.9, 263.3, weight=48.0)
    g.diag(409.4, 511.4, 439.2, 476.9, weight=64.0)
    g.diag(439.2, 476.9, 413.1, 294.6, weight=64.0)
    g.diag(413.1, 294.6, 401.6, 286.5, weight=64.0)
    g.hbar(212.4, 524.2, 255.1, weight=64.0)
    g.hbar(329.9, 342.8, 165.4, weight=64.0)
    g.diag(329.9, 163.0, 190.2, 1.8, weight=64.0)
    g.dot(448.4, 151.4, w=96.0, h=101.8, slant=-14.0)
    g.diag(559.0, 677.4, 616.4, 642.6, weight=76.0)
    g.vbar(571.7, 421.7, 642.6, weight=76.0)
    g.diag(617.8, 649.5, 628.6, 672.3, weight=96.0)
    g.hbar(628.6, 757.3, 683.1, weight=96.0)
    g.vbar(735.6, 478.1, 693.8, weight=96.0)
    g.hbar(713.9, 907.4, 478.4, weight=96.0)
    g.diag(576.3, 329.0, 664.9, 256.6, weight=96.0)
    g.diag(664.9, 256.6, 476.0, 27.8, weight=96.0)
    g.diag(555.1, 283.6, 947.0, -11.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_6bc0() -> Glyph:
    """毀 U+6BC0 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6BC0", advance=1000, unicode=0x6BC0, note="毀：自动生成")
    g.diag(237.6, 759.1, 263.2, 722.4, weight=96.0)
    g.diag(263.2, 722.4, 161.1, 603.4, weight=96.0)
    g.hbar(150.9, 161.1, 603.4, weight=96.0)
    g.vbar(152.0, 346.3, 599.0, weight=96.0)
    g.vbar(194.6, 473.4, 487.3, weight=96.0)
    g.hbar(196.9, 285.4, 491.1, weight=96.0)
    g.hbar(313.5, 457.3, 608.3, weight=64.0)
    g.vbar(427.6, 374.1, 612.2, weight=64.0)
    g.hbar(388.1, 398.0, 376.2, weight=64.0)
    g.dot(352.3, 509.3, w=92.0, h=112.2, slant=-14.0)
    g.hbar(210.0, 373.6, 379.8, weight=92.0)
    g.vbar(178.0, 231.7, 312.1, weight=96.0)
    g.hbar(182.2, 432.0, 247.7, weight=96.0)
    g.diag(265.2, 361.1, 292.8, 340.4, weight=96.0)
    g.vbar(295.5, 151.2, 340.4, weight=96.0)
    g.diag(298.3, 151.2, 279.0, 121.7, weight=96.0)
    g.hbar(78.0, 132.2, 50.7, weight=96.0)
    g.diag(132.2, 41.9, 470.2, 214.9, weight=96.0)
    g.vbar(533.5, 621.5, 675.7, weight=56.0)
    g.diag(532.4, 621.5, 508.6, 441.9, weight=56.0)
    g.diag(508.6, 441.9, 427.4, 397.0, weight=56.0)
    g.hbar(556.8, 566.9, 671.4, weight=96.0)
    g.hbar(566.9, 710.2, 681.0, weight=96.0)
    g.vbar(691.9, 457.0, 692.5, weight=96.0)
    g.hbar(673.5, 878.0, 457.3, weight=96.0)
    g.diag(497.8, 287.3, 602.3, 224.4, weight=96.0)
    g.diag(602.3, 224.4, 459.8, -12.5, weight=96.0)
    g.diag(459.8, -12.5, 351.1, 77.7, weight=96.0)
    g.diag(487.0, 280.4, 942.0, -29.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_6d6a() -> Glyph:
    """浪 U+6D6A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6D6A", advance=1000, unicode=0x6D6A, note="浪：自动生成")
    g.diag(134.9, 711.6, 319.1, 616.4, weight=96.0)
    g.diag(68.1, 447.4, 244.2, 323.6, weight=96.0)
    g.diag(144.3, -57.0, 131.0, 4.1, weight=96.0)
    g.diag(131.0, 4.1, 201.1, 346.7, weight=96.0)
    g.diag(478.5, 792.0, 570.4, 747.1, weight=56.0)
    g.diag(570.4, 747.1, 613.0, 664.8, weight=56.0)
    g.hbar(408.4, 654.2, 619.6, weight=48.0)
    g.diag(654.2, 643.4, 689.4, 600.9, weight=48.0)
    g.diag(689.4, 600.9, 606.0, 344.3, weight=48.0)
    g.diag(440.9, 455.7, 455.0, 472.9, weight=96.0)
    g.hbar(455.0, 612.9, 474.2, weight=96.0)
    g.diag(438.8, 317.9, 453.4, 337.1, weight=48.0)
    g.hbar(453.4, 572.3, 349.7, weight=48.0)
    g.hbar(572.3, 605.1, 355.0, weight=48.0)
    g.diag(357.3, 619.7, 447.4, -14.3, weight=48.0)
    g.diag(447.4, -14.3, 575.6, 73.5, weight=48.0)
    g.diag(669.9, 375.0, 776.1, 323.4, weight=96.0)
    g.diag(776.1, 323.4, 628.1, 197.7, weight=96.0)
    g.hbar(616.3, 628.1, 198.3, weight=96.0)
    g.diag(441.9, 308.5, 590.0, 207.9, weight=48.0)
    g.diag(590.0, 207.9, 936.9, 26.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_6d74() -> Glyph:
    """浴 U+6D74 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6D74", advance=1000, unicode=0x6D74, note="浴：自动生成")
    g.diag(127.0, 729.9, 282.7, 571.5, weight=96.0)
    g.diag(58.0, 507.3, 190.3, 398.3, weight=96.0)
    g.diag(110.5, 27.2, 90.5, 95.2, weight=48.0)
    g.diag(90.5, 95.2, 217.7, 371.3, weight=48.0)
    g.diag(412.4, 743.3, 438.6, 699.7, weight=96.0)
    g.diag(438.6, 699.7, 355.7, 577.2, weight=96.0)
    g.hbar(249.9, 355.7, 588.4, weight=96.0)
    g.diag(596.8, 736.1, 735.9, 643.3, weight=96.0)
    g.diag(487.6, 587.7, 431.5, 461.2, weight=48.0)
    g.diag(431.5, 461.2, 218.7, 191.0, weight=48.0)
    g.hbar(161.7, 218.7, 195.1, weight=48.0)
    g.diag(534.4, 508.9, 942.0, 280.7, weight=96.0)
    g.diag(374.7, 209.2, 362.8, 192.6, weight=48.0)
    g.vbar(391.8, -6.6, 192.6, weight=48.0)
    g.hbar(377.7, 691.2, 210.8, weight=48.0)
    g.diag(691.2, 222.4, 611.3, 69.1, weight=48.0)
    g.hbar(423.8, 648.4, 31.0, weight=48.0)
    g.vbar(648.6, 53.7, 81.7, weight=48.0)
    return g
def g_cjk_unified_ideograph_6d78() -> Glyph:
    """浸 U+6D78 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6D78", advance=1000, unicode=0x6D78, note="浸：自动生成")
    g.dot(206.4, 687.8, w=96.0, h=124.8, slant=-14.0)
    g.diag(53.3, 515.7, 194.2, 377.2, weight=96.0)
    g.diag(123.2, -34.0, 95.3, 51.2, weight=76.0)
    g.diag(95.3, 51.2, 272.9, 316.4, weight=76.0)
    g.hbar(407.1, 718.1, 745.1, weight=48.0)
    g.vbar(677.9, 569.6, 760.7, weight=48.0)
    g.hbar(416.6, 656.6, 634.3, weight=48.0)
    g.hbar(406.0, 673.4, 546.2, weight=48.0)
    g.diag(348.9, 421.7, 298.9, 297.4, weight=76.0)
    g.diag(298.9, 297.4, 353.5, 228.7, weight=76.0)
    g.hbar(372.9, 509.2, 408.7, weight=76.0)
    g.hbar(509.2, 829.6, 433.1, weight=76.0)
    g.diag(829.6, 452.2, 666.7, 299.2, weight=76.0)
    g.diag(399.0, 255.0, 513.1, 187.4, weight=96.0)
    g.diag(513.1, 187.4, 291.6, -7.5, weight=96.0)
    g.diag(393.3, 243.5, 936.7, -47.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_6daf() -> Glyph:
    """涯 U+6DAF —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6DAF", advance=1000, unicode=0x6DAF, note="涯：自动生成")
    g.diag(151.0, 761.7, 239.6, 702.3, weight=96.0)
    g.hbar(239.6, 333.5, 709.3, weight=96.0)
    g.diag(58.0, 558.5, 209.5, 421.8, weight=96.0)
    g.diag(148.7, 30.9, 71.1, 123.4, weight=96.0)
    g.diag(71.1, 123.4, 311.5, 376.4, weight=96.0)
    g.hbar(435.9, 823.2, 738.5, weight=96.0)
    g.diag(402.0, 728.3, 189.6, -38.0, weight=96.0)
    g.diag(189.6, -38.0, 101.3, 36.7, weight=96.0)
    g.hbar(419.2, 708.0, 529.7, weight=96.0)
    g.hbar(662.1, 708.0, 547.4, weight=96.0)
    g.diag(579.6, 683.0, 625.5, 623.3, weight=96.0)
    g.vbar(622.8, 423.4, 623.3, weight=96.0)
    g.diag(620.0, 423.4, 603.8, 397.5, weight=96.0)
    g.hbar(387.1, 880.5, 375.1, weight=96.0)
    g.hbar(463.3, 767.0, 204.0, weight=96.0)
    g.diag(577.9, 340.2, 606.9, 316.4, weight=96.0)
    g.vbar(613.6, 83.3, 316.4, weight=96.0)
    g.diag(620.4, 83.3, 596.3, 51.6, weight=96.0)
    g.hbar(264.4, 507.9, 43.1, weight=96.0)
    g.hbar(507.9, 927.0, 26.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_6db2() -> Glyph:
    """液 U+6DB2 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6DB2", advance=1000, unicode=0x6DB2, note="液：自动生成")
    g.diag(143.2, 729.0, 291.9, 595.7, weight=96.0)
    g.diag(61.3, 514.9, 195.1, 394.7, weight=96.0)
    g.diag(114.9, 23.6, 93.8, 101.9, weight=56.0)
    g.diag(93.8, 101.9, 217.7, 363.7, weight=56.0)
    g.hbar(467.6, 566.3, 770.5, weight=84.0)
    g.diag(566.3, 749.0, 618.0, 646.7, weight=84.0)
    g.hbar(356.0, 771.0, 593.2, weight=96.0)
    g.diag(388.7, 541.2, 426.0, 494.9, weight=48.0)
    g.diag(426.0, 494.9, 288.8, 277.4, weight=48.0)
    g.diag(288.8, 277.4, 173.4, 225.2, weight=48.0)
    g.vbar(331.8, -52.0, 300.2, weight=48.0)
    g.diag(567.9, 578.8, 606.4, 501.9, weight=48.0)
    g.diag(606.4, 501.9, 451.3, 295.5, weight=48.0)
    g.diag(579.0, 421.2, 633.6, 316.4, weight=48.0)
    g.diag(633.6, 316.4, 427.7, 45.6, weight=48.0)
    g.dot(573.0, 312.8, w=84.0, h=109.2, slant=-14.0)
    g.diag(441.8, 297.2, 933.7, 15.2, weight=84.0)
    return g
def g_cjk_unified_ideograph_6dbc() -> Glyph:
    """涼 U+6DBC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6DBC", advance=1000, unicode=0x6DBC, note="涼：自动生成")
    g.diag(173.8, 716.1, 264.1, 654.5, weight=96.0)
    g.diag(264.1, 654.5, 303.6, 559.7, weight=96.0)
    g.diag(96.3, 482.4, 231.0, 372.8, weight=96.0)
    g.diag(147.3, -26.5, 128.4, 45.8, weight=96.0)
    g.diag(128.4, 45.8, 220.8, 379.5, weight=96.0)
    g.diag(502.1, 782.0, 615.8, 720.4, weight=84.0)
    g.diag(615.8, 720.4, 661.5, 613.1, weight=84.0)
    g.hbar(294.8, 517.1, 573.0, weight=96.0)
    g.hbar(517.1, 903.7, 578.8, weight=96.0)
    g.vbar(424.0, 396.4, 416.1, weight=48.0)
    g.vbar(445.2, 246.1, 396.4, weight=48.0)
    g.hbar(434.2, 693.6, 428.9, weight=48.0)
    g.diag(693.6, 451.3, 730.8, 414.2, weight=48.0)
    g.diag(730.8, 414.2, 666.1, 314.1, weight=48.0)
    g.hbar(485.4, 706.0, 277.3, weight=48.0)
    g.vbar(705.5, 299.9, 324.0, weight=48.0)
    g.diag(557.4, 255.0, 602.4, 217.8, weight=96.0)
    g.diag(602.4, 217.8, 565.4, -56.2, weight=96.0)
    g.diag(565.4, -56.2, 386.2, 42.3, weight=96.0)
    g.diag(441.2, 218.1, 339.0, 37.0, weight=96.0)
    g.diag(339.0, 37.0, 422.3, -0.5, weight=96.0)
    g.diag(630.6, 175.8, 872.9, 26.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_6dd1() -> Glyph:
    """淑 U+6DD1 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6DD1", advance=1000, unicode=0x6DD1, note="淑：自动生成")
    g.dot(183.9, 624.9, w=96.0, h=124.8, slant=-14.0)
    g.dot(108.2, 419.4, w=96.0, h=124.8, slant=-14.0)
    g.diag(99.0, 5.5, 199.4, 341.2, weight=76.0)
    g.diag(341.5, 731.8, 386.5, 694.9, weight=96.0)
    g.vbar(383.4, 445.4, 694.9, weight=96.0)
    g.diag(380.3, 445.4, 362.9, 417.7, weight=96.0)
    g.hbar(411.0, 521.7, 575.6, weight=96.0)
    g.diag(521.7, 595.4, 550.9, 494.1, weight=96.0)
    g.hbar(183.0, 531.3, 398.1, weight=96.0)
    g.diag(357.8, 368.6, 400.9, 339.2, weight=96.0)
    g.vbar(381.1, -6.3, 339.2, weight=96.0)
    g.diag(361.3, -6.3, 229.5, 81.2, weight=96.0)
    g.vbar(230.6, 62.6, 281.4, weight=76.0)
    g.diag(419.2, 279.6, 498.7, 210.0, weight=96.0)
    g.hbar(428.2, 498.7, 201.8, weight=96.0)
    g.diag(540.6, 444.0, 649.6, 347.6, weight=84.0)
    g.diag(649.6, 347.6, 417.3, 64.9, weight=84.0)
    g.diag(530.9, 374.3, 794.0, 65.0, weight=96.0)
    g.hbar(794.0, 947.0, 49.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_6de1() -> Glyph:
    """淡 U+6DE1 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6DE1", advance=1000, unicode=0x6DE1, note="淡：自动生成")
    g.diag(141.5, 703.5, 291.9, 613.8, weight=96.0)
    g.diag(66.7, 475.0, 202.6, 350.2, weight=96.0)
    g.hbar(76.6, 191.7, -7.1, weight=96.0)
    g.diag(76.6, 18.2, 273.0, 296.9, weight=96.0)
    g.diag(277.6, 612.1, 453.7, 516.6, weight=96.0)
    g.diag(696.6, 704.6, 711.3, 667.7, weight=64.0)
    g.diag(711.3, 667.7, 580.2, 535.1, weight=64.0)
    g.diag(484.9, 772.0, 572.0, 694.5, weight=96.0)
    g.diag(572.0, 694.5, 324.9, 310.2, weight=96.0)
    g.diag(582.6, 542.7, 711.0, 403.9, weight=96.0)
    g.diag(327.8, 315.2, 360.6, 225.3, weight=96.0)
    g.diag(360.6, 225.3, 435.7, 168.8, weight=96.0)
    g.vbar(709.8, 325.4, 402.1, weight=56.0)
    g.hbar(518.5, 709.2, 290.3, weight=56.0)
    g.vbar(434.8, 248.4, 389.7, weight=48.0)
    g.diag(440.8, 248.4, 229.9, -35.9, weight=48.0)
    g.diag(521.9, 183.4, 525.9, 164.2, weight=96.0)
    g.diag(525.9, 164.2, 630.6, 66.2, weight=96.0)
    g.diag(630.6, 66.2, 732.7, -19.4, weight=96.0)
    g.hbar(732.7, 921.5, -36.7, weight=96.0)
    g.hbar(921.5, 928.3, -55.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_6deb() -> Glyph:
    """淫 U+6DEB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6DEB", advance=1000, unicode=0x6DEB, note="淫：自动生成")
    g.diag(146.3, 777.0, 256.6, 715.7, weight=96.0)
    g.diag(256.6, 715.7, 329.2, 593.9, weight=96.0)
    g.diag(62.7, 521.8, 240.7, 374.2, weight=96.0)
    g.diag(119.5, -52.0, 212.2, 405.4, weight=96.0)
    g.diag(787.9, 699.5, 722.3, 785.7, weight=96.0)
    g.diag(722.3, 785.7, 480.3, 628.5, weight=96.0)
    g.diag(394.0, 627.4, 461.3, 365.2, weight=96.0)
    g.diag(502.4, 648.4, 637.9, 518.1, weight=96.0)
    g.diag(774.8, 728.6, 824.8, 621.0, weight=96.0)
    g.diag(824.8, 621.0, 622.9, 521.1, weight=96.0)
    g.vbar(682.7, 401.6, 477.3, weight=96.0)
    g.hbar(404.8, 670.9, 353.2, weight=96.0)
    g.vbar(405.0, 213.8, 304.8, weight=96.0)
    g.hbar(244.2, 917.3, 225.6, weight=96.0)
    g.diag(559.6, 329.1, 592.6, 302.0, weight=96.0)
    g.vbar(590.6, 70.0, 302.0, weight=96.0)
    g.diag(588.5, 70.0, 569.7, 43.8, weight=96.0)
    g.hbar(353.5, 861.6, 4.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_6dfb() -> Glyph:
    """添 U+6DFB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6DFB", advance=1000, unicode=0x6DFB, note="添：自动生成")
    g.hbar(139.6, 306.0, 710.6, weight=96.0)
    g.diag(58.0, 517.1, 181.6, 406.2, weight=96.0)
    g.diag(83.8, 51.0, 169.5, 426.0, weight=64.0)
    g.hbar(398.7, 659.4, 705.0, weight=96.0)
    g.hbar(240.9, 780.3, 537.7, weight=48.0)
    g.diag(433.0, 670.5, 408.7, 528.2, weight=48.0)
    g.diag(408.7, 528.2, 275.2, 257.7, weight=48.0)
    g.hbar(138.4, 275.2, 238.4, weight=48.0)
    g.diag(523.2, 520.2, 927.0, 257.7, weight=48.0)
    g.diag(399.4, 393.4, 510.0, 302.3, weight=64.0)
    g.vbar(491.5, -25.9, 302.3, weight=64.0)
    g.diag(473.1, -25.9, 294.5, 71.3, weight=64.0)
    g.diag(291.8, 249.2, 327.5, 44.5, weight=64.0)
    g.diag(531.1, 169.6, 617.0, 109.9, weight=96.0)
    g.diag(617.0, 109.9, 686.5, 151.9, weight=96.0)
    g.hbar(612.9, 780.3, 150.2, weight=84.0)
    g.diag(780.3, 129.6, 808.2, 78.9, weight=84.0)
    return g
def g_cjk_unified_ideograph_6e26() -> Glyph:
    """渦 U+6E26 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6E26", advance=1000, unicode=0x6E26, note="渦：自动生成")
    g.dot(226.6, 723.4, w=96.0, h=124.8, slant=-14.0)
    g.diag(110.1, 507.0, 288.0, 390.4, weight=96.0)
    g.diag(167.8, -52.0, 144.2, 27.5, weight=64.0)
    g.diag(144.2, 27.5, 315.5, 346.8, weight=64.0)
    g.diag(409.3, 746.4, 500.7, 430.8, weight=48.0)
    g.diag(500.7, 430.8, 470.1, 372.2, weight=48.0)
    g.hbar(467.4, 698.2, 741.1, weight=48.0)
    g.diag(698.2, 767.0, 738.1, 669.9, weight=48.0)
    g.vbar(730.3, 446.7, 669.9, weight=48.0)
    g.diag(722.5, 446.7, 696.4, 414.9, weight=48.0)
    g.diag(595.1, 616.2, 585.8, 601.8, weight=48.0)
    g.vbar(590.9, 415.3, 601.8, weight=48.0)
    g.diag(596.0, 415.3, 583.7, 393.6, weight=48.0)
    g.hbar(613.4, 699.4, 616.7, weight=96.0)
    g.diag(699.4, 622.8, 712.8, 637.3, weight=96.0)
    g.vbar(361.5, 270.9, 362.0, weight=48.0)
    g.vbar(367.3, 20.7, 270.9, weight=48.0)
    g.hbar(370.8, 822.5, 383.4, weight=48.0)
    g.diag(822.5, 416.7, 854.1, 300.4, weight=48.0)
    g.vbar(851.3, 29.2, 300.4, weight=48.0)
    g.diag(848.6, 29.2, 819.7, -13.5, weight=48.0)
    g.hbar(723.5, 819.7, 6.8, weight=48.0)
    g.vbar(509.2, 110.0, 252.5, weight=64.0)
    g.hbar(509.7, 696.9, 257.0, weight=48.0)
    g.diag(696.9, 273.9, 636.1, 174.5, weight=48.0)
    g.hbar(538.6, 672.7, 156.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_6e56() -> Glyph:
    """湖 U+6E56 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6E56", advance=1000, unicode=0x6E56, note="湖：自动生成")
    g.diag(196.0, 703.0, 268.0, 646.0, weight=96.0)
    g.diag(268.0, 646.0, 289.3, 514.4, weight=96.0)
    g.diag(108.0, 506.0, 224.8, 376.8, weight=96.0)
    g.diag(157.0, 57.0, 139.8, 130.0, weight=92.0)
    g.diag(139.8, 130.0, 255.4, 345.3, weight=92.0)
    g.hbar(221.9, 626.5, 479.2, weight=96.0)
    g.diag(421.0, 772.0, 464.6, 728.4, weight=96.0)
    g.diag(464.6, 728.4, 417.0, 370.0, weight=96.0)
    g.diag(417.0, 370.0, 398.0, 348.0, weight=96.0)
    g.diag(273.8, 340.5, 317.6, 312.6, weight=64.0)
    g.vbar(336.2, 145.5, 312.6, weight=64.0)
    g.hbar(337.9, 538.4, 322.9, weight=48.0)
    g.diag(538.4, 335.6, 471.2, 216.3, weight=48.0)
    g.hbar(363.0, 508.9, 184.6, weight=48.0)
    g.vbar(508.6, 201.8, 223.4, weight=48.0)
    g.vbar(618.7, 435.7, 651.0, weight=48.0)
    g.diag(615.4, 435.7, 433.0, -57.0, weight=48.0)
    g.diag(692.7, 637.7, 698.4, 634.1, weight=96.0)
    g.diag(698.4, 634.1, 824.1, 457.7, weight=96.0)
    g.vbar(812.9, 2.3, 457.7, weight=96.0)
    g.hbar(726.0, 801.7, 19.2, weight=96.0)
    g.dot(752.5, 442.7, w=96.0, h=118.3, slant=-14.0)
    g.dot(745.5, 286.3, w=96.0, h=124.8, slant=-14.0)
    return g
def g_cjk_unified_ideograph_6e67() -> Glyph:
    """湧 U+6E67 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6E67", advance=1000, unicode=0x6E67, note="湧：自动生成")
    g.dot(307.4, 671.0, w=96.0, h=124.8, slant=-14.0)
    g.dot(216.7, 462.0, w=96.0, h=124.8, slant=-14.0)
    g.diag(226.6, 2.5, 210.0, 74.3, weight=96.0)
    g.diag(210.0, 74.3, 346.9, 349.2, weight=96.0)
    g.hbar(460.6, 773.3, 751.5, weight=48.0)
    g.diag(773.3, 767.7, 658.0, 656.4, weight=48.0)
    g.hbar(646.6, 658.0, 657.4, weight=48.0)
    g.diag(568.6, 667.7, 654.1, 610.4, weight=48.0)
    g.diag(444.6, 578.5, 493.4, 330.4, weight=64.0)
    g.hbar(499.1, 767.3, 583.9, weight=48.0)
    g.diag(767.3, 609.2, 807.3, 576.3, weight=48.0)
    g.vbar(794.1, 349.2, 576.3, weight=48.0)
    g.hbar(538.5, 716.1, 497.7, weight=64.0)
    g.hbar(541.4, 718.9, 411.7, weight=64.0)
    g.diag(596.8, 560.6, 625.9, 535.2, weight=48.0)
    g.vbar(624.5, 339.8, 535.2, weight=48.0)
    g.hbar(414.5, 844.0, 246.9, weight=96.0)
    g.diag(844.0, 266.8, 723.0, -52.4, weight=96.0)
    g.diag(723.0, -52.4, 640.0, 6.3, weight=96.0)
    g.diag(579.9, 322.0, 618.4, 260.0, weight=96.0)
    g.diag(618.4, 260.0, 344.1, -67.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_6e6f() -> Glyph:
    """湯 U+6E6F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6E6F", advance=1000, unicode=0x6E6F, note="湯：自动生成")
    g.hbar(172.3, 369.9, 700.0, weight=96.0)
    g.dot(152.3, 457.1, w=96.0, h=124.8, slant=-14.0)
    g.hbar(114.0, 220.5, 53.8, weight=84.0)
    g.vbar(176.7, 67.1, 360.3, weight=84.0)
    g.vbar(394.7, 737.1, 747.8, weight=48.0)
    g.vbar(414.0, 498.1, 737.1, weight=48.0)
    g.hbar(408.8, 578.1, 706.5, weight=48.0)
    g.vbar(587.3, 513.5, 672.7, weight=48.0)
    g.hbar(560.6, 596.5, 515.7, weight=48.0)
    g.diag(441.6, 620.7, 449.5, 636.6, weight=92.0)
    g.hbar(449.5, 586.4, 633.8, weight=92.0)
    g.diag(449.7, 510.8, 462.6, 523.7, weight=76.0)
    g.hbar(462.6, 561.6, 527.9, weight=76.0)
    g.hbar(236.5, 414.1, 375.4, weight=48.0)
    g.hbar(414.1, 891.3, 426.9, weight=48.0)
    g.diag(423.3, 391.6, 248.0, 176.0, weight=48.0)
    g.hbar(398.2, 807.5, 302.4, weight=96.0)
    g.diag(807.5, 319.9, 653.4, -72.0, weight=96.0)
    g.diag(653.4, -72.0, 503.8, 30.0, weight=96.0)
    g.diag(453.7, 261.7, 473.5, 234.0, weight=76.0)
    g.diag(473.5, 234.0, 254.0, 41.9, weight=76.0)
    g.diag(589.8, 287.0, 620.1, 255.1, weight=96.0)
    g.diag(620.1, 255.1, 387.9, -41.1, weight=96.0)
    g.diag(387.9, -41.1, 290.1, 16.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_6e7f() -> Glyph:
    """湿 U+6E7F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6E7F", advance=1000, unicode=0x6E7F, note="湿：自动生成")
    g.diag(153.8, 772.0, 326.3, 684.5, weight=96.0)
    g.diag(58.5, 543.6, 234.4, 389.3, weight=96.0)
    g.diag(109.0, -52.0, 92.8, 17.0, weight=96.0)
    g.diag(92.8, 17.0, 199.4, 427.1, weight=96.0)
    g.vbar(425.0, 434.9, 695.3, weight=48.0)
    g.hbar(395.0, 809.2, 702.8, weight=48.0)
    g.vbar(764.6, 459.1, 717.8, weight=48.0)
    g.diag(464.8, 556.0, 473.8, 574.4, weight=92.0)
    g.hbar(473.8, 722.2, 575.1, weight=92.0)
    g.hbar(472.5, 709.9, 456.5, weight=48.0)
    g.diag(453.8, 390.6, 499.2, 318.7, weight=96.0)
    g.vbar(501.5, 43.3, 318.7, weight=96.0)
    g.diag(503.8, 43.3, 487.7, 27.2, weight=96.0)
    g.diag(606.8, 434.5, 655.3, 362.3, weight=96.0)
    g.vbar(646.1, 55.9, 362.3, weight=96.0)
    g.diag(636.9, 55.9, 619.7, 39.8, weight=96.0)
    g.diag(246.0, 265.6, 471.9, 133.7, weight=76.0)
    g.diag(817.1, 321.0, 848.9, 272.7, weight=56.0)
    g.diag(848.9, 272.7, 665.1, 152.0, weight=56.0)
    g.hbar(255.9, 936.5, -7.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_6e9d() -> Glyph:
    """溝 U+6E9D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6E9D", advance=1000, unicode=0x6E9D, note="溝：自动生成")
    g.dot(217.4, 659.8, w=76.0, h=98.8, slant=-14.0)
    g.dot(138.5, 436.5, w=76.0, h=98.8, slant=-14.0)
    g.diag(153.0, -6.2, 253.1, 321.0, weight=76.0)
    g.hbar(386.8, 769.9, 639.1, weight=76.0)
    g.hbar(408.0, 742.9, 539.0, weight=76.0)
    g.diag(436.9, 731.0, 505.0, 497.6, weight=76.0)
    g.diag(505.0, 497.6, 477.3, 452.9, weight=76.0)
    g.diag(610.1, 782.0, 649.6, 741.6, weight=76.0)
    g.vbar(636.1, 492.3, 741.6, weight=76.0)
    g.diag(622.6, 492.3, 606.2, 470.2, weight=76.0)
    g.hbar(302.1, 852.6, 434.6, weight=76.0)
    g.diag(378.2, 340.3, 393.4, 230.9, weight=56.0)
    g.vbar(385.8, -42.8, 230.9, weight=56.0)
    g.hbar(431.1, 670.3, 346.0, weight=48.0)
    g.diag(670.3, 363.3, 697.6, 215.3, weight=48.0)
    g.vbar(689.8, -61.0, 215.3, weight=48.0)
    g.diag(681.9, -61.0, 599.5, -21.6, weight=48.0)
    g.hbar(466.7, 629.3, 240.2, weight=76.0)
    g.diag(514.8, 417.3, 544.3, 394.9, weight=48.0)
    g.vbar(542.5, 181.1, 394.9, weight=48.0)
    g.diag(540.7, 181.1, 527.3, 164.2, weight=48.0)
    g.hbar(254.0, 904.6, 135.3, weight=76.0)
    return g
def g_cjk_unified_ideograph_6eb6() -> Glyph:
    """溶 U+6EB6 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6EB6", advance=1000, unicode=0x6EB6, note="溶：自动生成")
    g.dot(174.8, 684.4, w=96.0, h=124.8, slant=-14.0)
    g.dot(102.5, 488.5, w=96.0, h=116.3, slant=-14.0)
    g.diag(115.2, 3.0, 226.2, 364.3, weight=96.0)
    g.diag(454.2, 802.0, 562.1, 720.6, weight=64.0)
    g.diag(323.9, 647.3, 297.4, 486.5, weight=84.0)
    g.hbar(366.7, 475.0, 618.3, weight=64.0)
    g.hbar(475.0, 763.7, 629.7, weight=64.0)
    g.diag(763.7, 641.7, 683.2, 543.5, weight=64.0)
    g.diag(402.3, 504.8, 417.8, 475.8, weight=84.0)
    g.diag(417.8, 475.8, 316.8, 364.2, weight=84.0)
    g.diag(316.8, 364.2, 315.8, 359.2, weight=84.0)
    g.dot(632.3, 469.2, w=96.0, h=124.8, slant=-14.0)
    g.diag(533.6, 384.7, 432.0, 290.9, weight=84.0)
    g.diag(432.0, 290.9, 201.8, 78.3, weight=84.0)
    g.diag(539.7, 360.2, 554.6, 318.5, weight=76.0)
    g.hbar(554.6, 941.8, 247.8, weight=76.0)
    g.hbar(346.3, 379.8, 142.1, weight=48.0)
    g.diag(379.8, 135.7, 420.6, -52.0, weight=48.0)
    g.hbar(409.4, 499.7, 153.9, weight=48.0)
    g.hbar(499.7, 667.0, 161.6, weight=48.0)
    g.diag(667.0, 169.0, 630.3, 58.9, weight=48.0)
    g.diag(630.3, 58.9, 604.8, 36.6, weight=48.0)
    g.diag(438.9, -25.5, 453.9, -9.4, weight=48.0)
    g.hbar(453.9, 683.2, -3.7, weight=48.0)
    return g
def g_cjk_unified_ideograph_6eba() -> Glyph:
    """溺 U+6EBA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6EBA", advance=1000, unicode=0x6EBA, note="溺：自动生成")
    g.dot(225.3, 721.8, w=96.0, h=124.8, slant=-14.0)
    g.dot(136.9, 521.2, w=96.0, h=124.8, slant=-14.0)
    g.diag(129.5, -10.3, 105.2, 68.8, weight=96.0)
    g.diag(105.2, 68.8, 241.1, 400.0, weight=96.0)
    g.hbar(349.3, 542.3, 704.2, weight=48.0)
    g.diag(542.3, 716.4, 508.3, 606.3, weight=48.0)
    g.diag(508.3, 606.3, 485.7, 595.0, weight=48.0)
    g.hbar(386.5, 395.3, 541.8, weight=48.0)
    g.hbar(395.3, 538.7, 550.8, weight=48.0)
    g.diag(338.1, 560.1, 288.7, 397.3, weight=96.0)
    g.diag(288.7, 397.3, 455.5, 260.2, weight=96.0)
    g.vbar(453.3, -23.7, 260.2, weight=96.0)
    g.diag(451.0, -23.7, 353.9, 39.3, weight=96.0)
    g.dot(338.1, 268.1, w=96.0, h=89.5, slant=-14.0)
    g.hbar(231.0, 279.5, 68.6, weight=96.0)
    g.diag(279.5, 70.9, 428.2, 207.3, weight=96.0)
    g.hbar(660.5, 870.8, 741.2, weight=96.0)
    g.diag(870.8, 748.8, 795.7, 618.7, weight=96.0)
    g.diag(717.9, 557.8, 729.3, 577.8, weight=96.0)
    g.hbar(729.3, 866.7, 584.1, weight=96.0)
    g.diag(652.6, 605.2, 685.6, 568.3, weight=96.0)
    g.diag(685.6, 568.3, 656.9, 416.5, weight=96.0)
    g.diag(656.9, 416.5, 816.5, 256.4, weight=96.0)
    g.vbar(810.2, -62.4, 256.4, weight=96.0)
    g.diag(803.9, -62.4, 684.1, 10.0, weight=96.0)
    g.dot(641.3, 272.6, w=96.0, h=89.5, slant=-14.0)
    g.hbar(582.7, 633.4, 78.8, weight=96.0)
    g.diag(633.4, 84.4, 798.0, 247.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_6ecb() -> Glyph:
    """滋 U+6ECB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6ECB", advance=1000, unicode=0x6ECB, note="滋：自动生成")
    g.diag(180.0, 701.6, 268.7, 647.3, weight=96.0)
    g.diag(268.7, 647.3, 320.4, 516.2, weight=96.0)
    g.diag(94.6, 482.0, 232.2, 331.3, weight=96.0)
    g.diag(141.2, -57.0, 119.9, 25.0, weight=76.0)
    g.diag(119.9, 25.0, 300.0, 270.8, weight=76.0)
    g.diag(422.9, 703.8, 558.1, 586.4, weight=96.0)
    g.diag(707.9, 787.0, 745.1, 743.8, weight=96.0)
    g.diag(745.1, 743.8, 598.1, 548.6, weight=96.0)
    g.hbar(350.9, 837.7, 497.4, weight=96.0)
    g.diag(378.6, 448.7, 409.6, 402.1, weight=48.0)
    g.diag(409.6, 402.1, 308.3, 215.2, weight=48.0)
    g.hbar(308.3, 439.3, 219.1, weight=48.0)
    g.diag(497.2, 355.6, 461.9, 247.6, weight=48.0)
    g.diag(461.9, 247.6, 327.4, 23.1, weight=48.0)
    g.hbar(327.4, 493.1, 43.7, weight=48.0)
    g.diag(436.7, 156.0, 517.2, 63.9, weight=48.0)
    g.diag(517.2, 63.9, 498.2, 46.4, weight=48.0)
    g.diag(658.7, 501.4, 692.4, 429.7, weight=48.0)
    g.diag(692.4, 429.7, 578.4, 222.4, weight=48.0)
    g.hbar(578.4, 718.5, 224.7, weight=48.0)
    g.diag(780.0, 366.7, 746.5, 259.6, weight=48.0)
    g.diag(746.5, 259.6, 619.5, 45.1, weight=48.0)
    g.hbar(619.5, 817.7, 69.5, weight=48.0)
    g.diag(743.5, 196.4, 885.4, -19.3, weight=48.0)
    return g
def g_cjk_unified_ideograph_6ef4() -> Glyph:
    """滴 U+6EF4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6EF4", advance=1000, unicode=0x6EF4, note="滴：自动生成")
    g.diag(205.8, 728.6, 351.6, 618.5, weight=96.0)
    g.diag(119.5, 509.5, 260.2, 384.4, weight=96.0)
    g.diag(175.3, 4.1, 242.9, 400.9, weight=92.0)
    g.diag(552.3, 797.0, 624.9, 758.0, weight=64.0)
    g.diag(624.9, 758.0, 665.3, 665.6, weight=64.0)
    g.hbar(348.6, 855.5, 637.7, weight=96.0)
    g.diag(468.2, 583.9, 533.8, 438.9, weight=48.0)
    g.diag(685.7, 617.3, 713.1, 585.5, weight=64.0)
    g.diag(713.1, 585.5, 631.2, 453.7, weight=64.0)
    g.vbar(393.0, 289.7, 417.7, weight=48.0)
    g.vbar(380.8, -47.5, 289.7, weight=48.0)
    g.hbar(405.2, 785.8, 436.3, weight=48.0)
    g.vbar(804.8, 298.7, 465.4, weight=48.0)
    g.vbar(815.8, -54.3, 298.7, weight=48.0)
    g.hbar(698.6, 807.9, -35.1, weight=48.0)
    g.hbar(436.5, 796.2, 314.3, weight=96.0)
    g.diag(565.9, 405.8, 603.8, 379.2, weight=48.0)
    g.diag(603.8, 379.2, 572.4, 204.5, weight=48.0)
    g.vbar(506.7, 29.6, 174.7, weight=48.0)
    g.hbar(508.6, 711.7, 181.4, weight=48.0)
    g.diag(711.7, 199.0, 653.5, 94.1, weight=48.0)
    g.diag(532.3, 40.9, 542.5, 52.8, weight=48.0)
    g.hbar(542.5, 683.0, 76.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_6f01() -> Glyph:
    """漁 U+6F01 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6F01", advance=1000, unicode=0x6F01, note="漁：自动生成")
    g.diag(186.2, 735.2, 364.3, 560.6, weight=96.0)
    g.diag(83.9, 501.2, 233.9, 357.0, weight=96.0)
    g.diag(220.0, -57.6, 109.9, 9.4, weight=96.0)
    g.diag(109.9, 9.4, 210.7, 389.5, weight=96.0)
    g.diag(539.3, 802.0, 572.2, 753.9, weight=48.0)
    g.diag(572.2, 753.9, 376.3, 520.0, weight=48.0)
    g.hbar(551.7, 720.3, 680.7, weight=48.0)
    g.diag(720.3, 672.4, 574.7, 489.0, weight=48.0)
    g.vbar(404.4, 162.8, 436.0, weight=96.0)
    g.hbar(396.1, 523.6, 433.1, weight=48.0)
    g.hbar(523.6, 760.5, 471.7, weight=48.0)
    g.vbar(763.3, 378.6, 492.8, weight=48.0)
    g.diag(766.1, 378.6, 720.1, 201.0, weight=48.0)
    g.hbar(689.3, 720.1, 203.9, weight=48.0)
    g.hbar(441.6, 723.4, 322.0, weight=96.0)
    g.diag(541.4, 441.7, 571.4, 418.0, weight=96.0)
    g.vbar(570.3, 255.1, 418.0, weight=96.0)
    g.diag(569.1, 255.1, 552.9, 229.6, weight=96.0)
    g.hbar(453.6, 684.5, 202.5, weight=96.0)
    g.diag(413.0, 78.9, 245.1, -40.7, weight=96.0)
    g.hbar(166.0, 245.1, -42.4, weight=96.0)
    g.dot(475.0, 53.4, w=96.0, h=124.8, slant=-14.0)
    g.diag(593.2, 172.6, 692.8, -8.5, weight=96.0)
    g.diag(744.1, 173.3, 911.1, -48.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_6f02() -> Glyph:
    """漂 U+6F02 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6F02", advance=1000, unicode=0x6F02, note="漂：自动生成")
    g.diag(165.2, 737.0, 306.3, 619.7, weight=96.0)
    g.diag(94.1, 523.9, 238.8, 405.9, weight=96.0)
    g.diag(134.4, -2.9, 219.8, 423.6, weight=96.0)
    g.hbar(424.1, 699.5, 744.5, weight=96.0)
    g.diag(699.5, 768.3, 674.5, 724.2, weight=96.0)
    g.diag(345.2, 592.4, 405.8, 408.4, weight=96.0)
    g.diag(383.5, 590.7, 400.8, 581.7, weight=96.0)
    g.hbar(400.8, 799.1, 610.9, weight=96.0)
    g.vbar(769.4, 455.8, 640.0, weight=96.0)
    g.hbar(721.7, 739.6, 455.4, weight=96.0)
    g.diag(455.6, 698.9, 527.3, 496.6, weight=96.0)
    g.diag(527.3, 496.6, 505.5, 472.0, weight=96.0)
    g.diag(611.5, 720.1, 645.4, 703.1, weight=84.0)
    g.diag(645.4, 703.1, 614.5, 495.7, weight=84.0)
    g.diag(614.5, 495.7, 600.9, 485.8, weight=84.0)
    g.hbar(420.7, 716.4, 450.9, weight=48.0)
    g.diag(412.6, 378.7, 450.1, 339.6, weight=76.0)
    g.hbar(450.1, 658.3, 357.7, weight=76.0)
    g.diag(658.3, 375.8, 714.5, 425.5, weight=76.0)
    g.hbar(241.0, 900.9, 254.0, weight=92.0)
    g.diag(542.6, 222.9, 591.7, 184.2, weight=84.0)
    g.diag(591.7, 184.2, 549.5, -57.9, weight=84.0)
    g.diag(549.5, -57.9, 384.9, 26.8, weight=84.0)
    g.diag(383.6, 180.2, 330.5, -0.5, weight=96.0)
    g.hbar(330.5, 401.4, -7.0, weight=96.0)
    g.diag(615.2, 137.9, 853.2, -2.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_6f0f() -> Glyph:
    """漏 U+6F0F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6F0F", advance=1000, unicode=0x6F0F, note="漏：自动生成")
    g.dot(200.6, 715.5, w=96.0, h=124.8, slant=-14.0)
    g.diag(69.2, 541.4, 227.3, 411.9, weight=96.0)
    g.diag(144.7, -5.9, 84.6, 83.5, weight=64.0)
    g.diag(84.6, 83.5, 258.2, 389.2, weight=64.0)
    g.hbar(440.6, 791.9, 744.5, weight=48.0)
    g.diag(791.9, 766.4, 710.9, 639.0, weight=48.0)
    g.hbar(431.9, 753.5, 611.6, weight=48.0)
    g.diag(389.7, 752.4, 360.4, 524.5, weight=48.0)
    g.diag(360.4, 524.5, 139.5, -46.6, weight=48.0)
    g.hbar(433.5, 755.0, 469.8, weight=96.0)
    g.diag(755.0, 482.4, 792.3, 579.4, weight=96.0)
    g.vbar(380.4, -43.2, 309.5, weight=48.0)
    g.hbar(412.6, 868.8, 327.7, weight=48.0)
    g.diag(868.8, 361.2, 891.7, 219.2, weight=48.0)
    g.vbar(886.3, -60.5, 219.2, weight=48.0)
    g.hbar(751.7, 880.9, -35.7, weight=48.0)
    g.diag(586.8, 428.5, 618.5, 292.7, weight=48.0)
    g.vbar(622.3, -43.2, 292.7, weight=48.0)
    g.hbar(430.9, 602.7, 191.4, weight=64.0)
    g.hbar(437.0, 593.5, 84.0, weight=84.0)
    g.hbar(659.5, 763.3, 232.1, weight=76.0)
    g.diag(763.3, 216.3, 739.3, 136.5, weight=76.0)
    g.hbar(666.2, 759.8, 105.8, weight=96.0)
    g.vbar(760.7, 26.2, 88.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_6f14() -> Glyph:
    """演 U+6F14 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6F14", advance=1000, unicode=0x6F14, note="演：自动生成")
    g.dot(261.5, 660.8, w=96.0, h=124.8, slant=-14.0)
    g.dot(183.0, 450.1, w=96.0, h=118.7, slant=-14.0)
    g.diag(193.1, -14.3, 299.5, 322.0, weight=96.0)
    g.diag(548.7, 792.0, 657.0, 707.9, weight=64.0)
    g.diag(390.6, 630.9, 403.0, 598.0, weight=96.0)
    g.diag(403.0, 598.0, 354.2, 447.6, weight=96.0)
    g.hbar(428.1, 875.1, 606.8, weight=96.0)
    g.diag(875.1, 640.4, 797.8, 531.7, weight=96.0)
    g.hbar(492.9, 723.9, 505.4, weight=84.0)
    g.diag(393.7, 373.7, 472.7, 146.8, weight=48.0)
    g.hbar(442.3, 579.9, 377.4, weight=48.0)
    g.hbar(579.9, 741.4, 355.2, weight=48.0)
    g.vbar(745.2, 179.7, 329.1, weight=48.0)
    g.diag(748.9, 179.7, 752.2, 160.0, weight=48.0)
    g.hbar(521.3, 706.7, 287.6, weight=64.0)
    g.diag(575.0, 463.8, 609.5, 439.2, weight=96.0)
    g.vbar(608.4, 226.8, 439.2, weight=96.0)
    g.diag(607.4, 226.8, 591.2, 203.5, weight=96.0)
    g.hbar(490.9, 692.4, 176.6, weight=76.0)
    g.diag(692.4, 194.2, 704.6, 183.2, weight=76.0)
    g.hbar(527.2, 544.6, 72.7, weight=84.0)
    g.diag(527.2, 71.5, 342.0, -72.0, weight=84.0)
    g.diag(685.4, 92.1, 838.3, -59.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_6f20() -> Glyph:
    """漠 U+6F20 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6F20", advance=1000, unicode=0x6F20, note="漠：自动生成")
    g.dot(227.0, 627.8, w=96.0, h=124.8, slant=-14.0)
    g.diag(84.9, 472.2, 229.8, 320.3, weight=96.0)
    g.diag(247.7, -51.9, 137.4, 23.5, weight=96.0)
    g.diag(137.4, 23.5, 198.2, 362.9, weight=96.0)
    g.hbar(304.1, 813.7, 614.4, weight=96.0)
    g.diag(418.5, 699.6, 455.3, 674.7, weight=48.0)
    g.diag(455.3, 674.7, 488.6, 504.3, weight=48.0)
    g.vbar(645.5, 673.6, 708.1, weight=96.0)
    g.diag(645.1, 708.1, 600.2, 547.6, weight=96.0)
    g.vbar(393.1, 465.0, 482.5, weight=48.0)
    g.vbar(417.2, 275.2, 465.0, weight=48.0)
    g.hbar(404.2, 726.0, 489.5, weight=48.0)
    g.vbar(695.4, 309.3, 505.3, weight=48.0)
    g.hbar(647.0, 664.8, 311.2, weight=48.0)
    g.hbar(443.6, 662.7, 379.7, weight=64.0)
    g.diag(460.2, 286.5, 469.1, 297.3, weight=64.0)
    g.hbar(469.1, 642.7, 310.9, weight=64.0)
    g.hbar(281.5, 879.3, 164.9, weight=48.0)
    g.diag(496.0, 280.5, 563.2, 227.9, weight=96.0)
    g.diag(563.2, 227.9, 398.7, -31.9, weight=96.0)
    g.hbar(193.1, 398.7, -33.6, weight=96.0)
    g.diag(551.7, 153.3, 747.0, -44.2, weight=48.0)
    g.hbar(747.0, 900.1, -55.6, weight=48.0)
    return g
def g_cjk_unified_ideograph_6f22() -> Glyph:
    """漢 U+6F22 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6F22", advance=1000, unicode=0x6F22, note="漢：自动生成")
    g.diag(156.0, 701.5, 290.5, 614.5, weight=92.0)
    g.diag(74.6, 495.3, 219.3, 338.0, weight=92.0)
    g.diag(226.7, -56.1, 121.5, -3.5, weight=92.0)
    g.diag(121.5, -3.5, 194.3, 376.0, weight=92.0)
    g.hbar(298.2, 764.6, 643.9, weight=92.0)
    g.diag(420.5, 662.6, 431.1, 735.6, weight=92.0)
    g.diag(431.1, 735.6, 472.9, 495.3, weight=92.0)
    g.diag(609.7, 697.9, 629.8, 741.8, weight=92.0)
    g.diag(629.8, 741.8, 603.7, 585.8, weight=92.0)
    g.diag(603.7, 585.8, 586.6, 569.7, weight=92.0)
    g.diag(489.0, 507.4, 504.6, 526.3, weight=56.0)
    g.hbar(504.6, 623.3, 536.6, weight=56.0)
    g.vbar(619.8, 546.9, 566.9, weight=56.0)
    g.dot(384.7, 342.9, w=92.0, h=119.6, slant=-14.0)
    g.hbar(388.4, 685.8, 433.9, weight=48.0)
    g.diag(685.8, 470.1, 731.3, 435.0, weight=48.0)
    g.diag(731.3, 435.0, 677.3, 362.0, weight=48.0)
    g.hbar(417.7, 721.5, 319.3, weight=48.0)
    g.vbar(718.8, 348.0, 371.8, weight=48.0)
    g.hbar(398.9, 472.8, 226.5, weight=76.0)
    g.hbar(472.8, 662.1, 231.4, weight=76.0)
    g.diag(662.1, 249.9, 695.7, 176.5, weight=76.0)
    g.hbar(264.7, 850.1, 116.6, weight=48.0)
    g.vbar(486.8, 292.6, 496.3, weight=92.0)
    g.diag(481.6, 292.6, 179.9, -45.8, weight=92.0)
    g.diag(555.8, 108.3, 905.4, -58.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_6f2b() -> Glyph:
    """漫 U+6F2B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6F2B", advance=1000, unicode=0x6F2B, note="漫：自动生成")
    g.dot(216.5, 677.4, w=96.0, h=124.8, slant=-14.0)
    g.diag(71.6, 545.5, 212.3, 366.8, weight=96.0)
    g.diag(239.4, -29.3, 128.2, 20.7, weight=96.0)
    g.diag(128.2, 20.7, 321.5, 363.0, weight=96.0)
    g.vbar(413.4, 731.1, 746.0, weight=48.0)
    g.vbar(441.6, 547.8, 731.1, weight=48.0)
    g.hbar(426.0, 725.5, 747.4, weight=48.0)
    g.vbar(688.3, 575.2, 756.0, weight=48.0)
    g.diag(465.4, 642.1, 484.9, 661.6, weight=64.0)
    g.hbar(484.9, 660.3, 659.2, weight=64.0)
    g.hbar(481.5, 619.8, 576.2, weight=48.0)
    g.diag(619.8, 590.7, 638.2, 579.1, weight=48.0)
    g.vbar(354.4, 300.3, 465.5, weight=96.0)
    g.hbar(355.7, 813.0, 482.8, weight=64.0)
    g.vbar(780.5, 360.5, 508.0, weight=64.0)
    g.hbar(730.6, 748.0, 360.8, weight=64.0)
    g.diag(463.3, 448.8, 471.9, 444.6, weight=96.0)
    g.diag(471.9, 444.6, 499.7, 366.8, weight=96.0)
    g.diag(644.7, 470.9, 620.3, 455.4, weight=84.0)
    g.diag(620.3, 455.4, 583.8, 378.2, weight=84.0)
    g.hbar(391.4, 732.2, 352.5, weight=48.0)
    g.diag(407.1, 222.8, 517.5, 164.4, weight=96.0)
    g.diag(517.5, 164.4, 197.8, -22.7, weight=96.0)
    g.diag(413.0, 202.8, 918.4, -47.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_6f2c() -> Glyph:
    """漬 U+6F2C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6F2C", advance=1000, unicode=0x6F2C, note="漬：自动生成")
    g.dot(235.7, 632.7, w=96.0, h=118.4, slant=-14.0)
    g.dot(164.7, 423.3, w=96.0, h=101.4, slant=-14.0)
    g.diag(187.9, 22.7, 170.6, 94.4, weight=96.0)
    g.diag(170.6, 94.4, 282.6, 328.6, weight=96.0)
    g.hbar(431.9, 721.5, 671.8, weight=64.0)
    g.hbar(439.2, 685.1, 574.4, weight=64.0)
    g.diag(534.8, 782.0, 576.7, 745.6, weight=84.0)
    g.vbar(572.2, 518.9, 745.6, weight=84.0)
    g.diag(567.6, 518.9, 552.1, 497.0, weight=84.0)
    g.hbar(294.5, 869.0, 469.3, weight=76.0)
    g.vbar(431.0, 112.8, 393.2, weight=48.0)
    g.hbar(461.1, 542.2, 389.8, weight=48.0)
    g.diag(542.2, 389.1, 662.4, 315.4, weight=48.0)
    g.diag(662.4, 315.4, 699.6, 101.0, weight=48.0)
    g.hbar(474.7, 623.1, 306.3, weight=48.0)
    g.hbar(471.1, 626.8, 231.6, weight=56.0)
    g.diag(464.7, 130.1, 477.7, 143.1, weight=64.0)
    g.hbar(477.7, 654.1, 151.1, weight=64.0)
    g.diag(654.1, 159.1, 660.5, 147.4, weight=64.0)
    g.hbar(522.5, 539.4, 66.1, weight=64.0)
    g.diag(522.5, 65.9, 313.6, -72.0, weight=64.0)
    g.diag(625.0, 81.9, 753.3, -65.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_6f38() -> Glyph:
    """漸 U+6F38 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6F38", advance=1000, unicode=0x6F38, note="漸：自动生成")
    g.dot(223.6, 635.4, w=96.0, h=124.8, slant=-14.0)
    g.dot(156.3, 424.7, w=96.0, h=124.8, slant=-14.0)
    g.diag(165.3, 49.5, 143.8, 113.2, weight=76.0)
    g.diag(143.8, 113.2, 287.4, 349.6, weight=76.0)
    g.hbar(282.5, 493.1, 614.7, weight=96.0)
    g.hbar(456.7, 493.1, 636.4, weight=96.0)
    g.vbar(303.9, 317.0, 495.5, weight=48.0)
    g.hbar(295.9, 553.3, 512.4, weight=48.0)
    g.vbar(529.1, 358.6, 532.2, weight=48.0)
    g.hbar(486.9, 505.0, 359.0, weight=48.0)
    g.hbar(327.9, 440.0, 436.0, weight=64.0)
    g.hbar(341.1, 480.1, 349.9, weight=64.0)
    g.hbar(222.0, 590.8, 263.5, weight=64.0)
    g.diag(371.9, 782.0, 404.0, 605.3, weight=76.0)
    g.vbar(401.8, 105.0, 605.3, weight=76.0)
    g.diag(399.7, 105.0, 454.4, 65.6, weight=76.0)
    g.diag(754.5, 666.0, 773.6, 626.8, weight=96.0)
    g.diag(773.6, 626.8, 666.1, 538.9, weight=96.0)
    g.hbar(653.9, 666.1, 539.4, weight=96.0)
    g.vbar(588.0, 125.2, 542.3, weight=64.0)
    g.hbar(423.5, 547.7, 103.0, weight=64.0)
    g.hbar(660.2, 889.6, 444.3, weight=96.0)
    g.diag(723.7, 404.9, 755.4, 384.9, weight=76.0)
    g.vbar(758.1, -52.0, 384.9, weight=76.0)
    return g
def g_cjk_unified_ideograph_6f54() -> Glyph:
    """潔 U+6F54 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6F54", advance=1000, unicode=0x6F54, note="潔：自动生成")
    g.dot(269.8, 662.8, w=96.0, h=124.8, slant=-14.0)
    g.diag(140.1, 489.3, 203.3, 441.2, weight=96.0)
    g.hbar(203.3, 290.0, 443.8, weight=96.0)
    g.diag(192.3, -9.9, 245.1, 383.7, weight=96.0)
    g.hbar(325.5, 548.0, 656.3, weight=64.0)
    g.hbar(548.0, 597.4, 683.0, weight=64.0)
    g.hbar(381.7, 537.3, 580.3, weight=48.0)
    g.diag(537.3, 598.0, 586.5, 563.0, weight=48.0)
    g.hbar(324.6, 366.0, 458.2, weight=56.0)
    g.hbar(366.0, 560.3, 489.6, weight=56.0)
    g.diag(560.3, 526.0, 578.2, 582.1, weight=56.0)
    g.diag(423.8, 777.0, 468.6, 678.7, weight=48.0)
    g.diag(468.6, 678.7, 521.7, 442.0, weight=48.0)
    g.hbar(604.0, 638.9, 656.6, weight=96.0)
    g.hbar(638.9, 878.3, 673.6, weight=96.0)
    g.diag(878.3, 695.5, 792.3, 478.2, weight=96.0)
    g.diag(792.3, 478.2, 705.9, 525.3, weight=96.0)
    g.diag(689.5, 637.7, 707.4, 618.6, weight=76.0)
    g.diag(707.4, 618.6, 666.4, 531.7, weight=76.0)
    g.hbar(593.6, 666.4, 520.8, weight=76.0)
    g.hbar(503.7, 562.5, 437.3, weight=48.0)
    g.diag(562.5, 426.8, 464.7, 301.5, weight=48.0)
    g.hbar(464.7, 576.4, 300.5, weight=48.0)
    g.diag(671.4, 400.1, 615.7, 320.0, weight=48.0)
    g.diag(615.7, 320.0, 465.4, 186.6, weight=48.0)
    g.hbar(465.4, 713.7, 208.1, weight=48.0)
    g.hbar(692.8, 738.6, 239.5, weight=48.0)
    g.diag(738.6, 231.7, 721.4, 210.9, weight=48.0)
    g.diag(573.2, 185.6, 658.5, -86.5, weight=48.0)
    g.hbar(495.0, 658.5, -52.7, weight=48.0)
    g.diag(464.7, 164.8, 401.8, 56.3, weight=96.0)
    g.diag(401.8, 56.3, 456.7, -21.9, weight=96.0)
    g.diag(738.7, 153.7, 859.9, -9.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_6f5c() -> Glyph:
    """潜 U+6F5C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6F5C", advance=1000, unicode=0x6F5C, note="潜：自动生成")
    g.dot(185.1, 656.2, w=96.0, h=124.8, slant=-14.0)
    g.dot(113.9, 467.8, w=96.0, h=124.1, slant=-14.0)
    g.diag(123.7, -47.9, 228.0, 326.9, weight=96.0)
    g.hbar(320.9, 522.2, 617.0, weight=96.0)
    g.hbar(262.0, 518.1, 480.2, weight=96.0)
    g.vbar(384.1, 589.2, 738.8, weight=48.0)
    g.diag(382.3, 589.2, 270.3, 305.2, weight=48.0)
    g.dot(471.6, 401.2, w=92.0, h=77.5, slant=-14.0)
    g.hbar(573.8, 792.7, 641.8, weight=96.0)
    g.hbar(566.6, 855.7, 519.9, weight=48.0)
    g.vbar(657.5, 628.4, 777.0, weight=56.0)
    g.diag(654.4, 628.4, 530.5, 347.5, weight=56.0)
    g.diag(693.6, 496.2, 930.0, 335.1, weight=48.0)
    g.diag(404.5, 272.2, 439.7, 226.8, weight=48.0)
    g.vbar(431.9, -52.0, 226.8, weight=48.0)
    g.diag(447.9, 271.1, 457.8, 261.2, weight=48.0)
    g.hbar(457.8, 616.2, 275.9, weight=48.0)
    g.diag(616.2, 290.7, 648.3, 192.5, weight=48.0)
    g.vbar(643.6, 47.2, 192.5, weight=48.0)
    g.diag(639.0, 47.2, 589.3, -8.6, weight=48.0)
    g.dot(527.9, 127.6, w=96.0, h=124.8, slant=-14.0)
    g.diag(457.2, -10.7, 476.6, 7.6, weight=96.0)
    g.hbar(476.6, 606.9, 8.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_6f5f() -> Glyph:
    """潟 U+6F5F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6F5F", advance=1000, unicode=0x6F5F, note="潟：自动生成")
    g.dot(215.0, 626.7, w=96.0, h=124.8, slant=-14.0)
    g.dot(152.5, 421.2, w=96.0, h=111.6, slant=-14.0)
    g.diag(177.7, -31.8, 287.0, 320.3, weight=84.0)
    g.diag(459.4, 787.0, 485.3, 747.3, weight=96.0)
    g.diag(485.3, 747.3, 387.9, 648.3, weight=96.0)
    g.diag(335.4, 644.1, 370.1, 615.7, weight=76.0)
    g.diag(370.1, 615.7, 424.7, 401.3, weight=76.0)
    g.diag(426.8, 531.6, 434.6, 545.9, weight=96.0)
    g.hbar(434.6, 526.7, 551.9, weight=96.0)
    g.hbar(609.7, 800.7, 696.4, weight=96.0)
    g.vbar(753.0, 428.6, 690.9, weight=96.0)
    g.dot(666.5, 580.5, w=96.0, h=121.8, slant=-14.0)
    g.diag(442.6, 410.7, 455.8, 424.0, weight=48.0)
    g.hbar(455.8, 681.2, 443.1, weight=48.0)
    g.diag(467.8, 401.3, 492.5, 368.6, weight=48.0)
    g.diag(492.5, 368.6, 322.8, 193.2, weight=48.0)
    g.hbar(445.7, 905.1, 299.0, weight=96.0)
    g.diag(905.1, 322.8, 756.2, -66.4, weight=96.0)
    g.diag(756.2, -66.4, 652.8, -2.3, weight=96.0)
    g.diag(366.9, 158.5, 323.8, -1.3, weight=48.0)
    g.dot(468.9, 123.3, w=84.0, h=98.9, slant=-14.0)
    g.dot(581.8, 141.7, w=84.0, h=106.7, slant=-14.0)
    g.dot(696.4, 160.6, w=84.0, h=107.0, slant=-14.0)
    return g
def g_cjk_unified_ideograph_6f64() -> Glyph:
    """潤 U+6F64 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6F64", advance=1000, unicode=0x6F64, note="潤：自动生成")
    g.dot(216.9, 696.5, w=96.0, h=124.8, slant=-14.0)
    g.diag(78.5, 509.5, 230.3, 362.8, weight=96.0)
    g.diag(162.7, -52.0, 135.9, 33.7, weight=76.0)
    g.diag(135.9, 33.7, 320.2, 338.9, weight=76.0)
    g.vbar(335.8, -29.8, 691.9, weight=64.0)
    g.hbar(359.3, 467.0, 649.9, weight=48.0)
    g.vbar(466.9, 448.8, 627.4, weight=48.0)
    g.hbar(466.9, 485.3, 446.5, weight=48.0)
    g.diag(385.3, 545.0, 392.6, 561.0, weight=92.0)
    g.hbar(392.6, 487.7, 562.3, weight=92.0)
    g.dot(429.1, 445.8, w=96.0, h=110.7, slant=-14.0)
    g.diag(678.9, 756.4, 672.2, 737.7, weight=48.0)
    g.vbar(682.3, 489.0, 737.7, weight=48.0)
    g.diag(689.7, 745.6, 838.8, 533.5, weight=48.0)
    g.vbar(840.8, -27.7, 533.5, weight=48.0)
    g.diag(842.7, -27.7, 745.3, 17.8, weight=48.0)
    g.diag(713.2, 611.4, 722.8, 628.0, weight=84.0)
    g.hbar(722.8, 847.3, 629.1, weight=84.0)
    g.diag(707.6, 500.7, 725.2, 515.7, weight=84.0)
    g.hbar(725.2, 850.2, 517.6, weight=84.0)
    g.diag(495.7, 402.8, 545.9, 339.0, weight=92.0)
    g.hbar(545.9, 667.7, 354.5, weight=92.0)
    g.diag(667.7, 370.0, 649.2, 343.0, weight=92.0)
    g.hbar(561.1, 660.9, 247.1, weight=92.0)
    g.hbar(635.1, 660.9, 260.8, weight=92.0)
    g.diag(615.7, 327.9, 599.1, 306.8, weight=96.0)
    g.vbar(598.0, 169.5, 306.8, weight=96.0)
    g.diag(596.9, 169.5, 580.2, 148.5, weight=96.0)
    g.hbar(375.9, 851.2, 123.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_6f6e() -> Glyph:
    """潮 U+6F6E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6F6E", advance=1000, unicode=0x6F6E, note="潮：自动生成")
    g.dot(218.9, 652.1, w=96.0, h=124.8, slant=-14.0)
    g.diag(88.8, 502.1, 220.7, 362.6, weight=96.0)
    g.diag(153.9, -9.0, 129.3, 70.8, weight=76.0)
    g.diag(129.3, 70.8, 299.3, 340.6, weight=76.0)
    g.hbar(290.6, 590.2, 628.5, weight=96.0)
    g.diag(414.2, 772.0, 450.9, 736.4, weight=96.0)
    g.diag(450.9, 736.4, 421.3, 522.7, weight=96.0)
    g.diag(421.3, 522.7, 407.8, 511.7, weight=96.0)
    g.vbar(323.5, 264.1, 476.9, weight=96.0)
    g.hbar(327.0, 566.8, 480.1, weight=48.0)
    g.vbar(541.5, 311.2, 503.6, weight=48.0)
    g.hbar(489.1, 516.3, 315.7, weight=48.0)
    g.diag(350.7, 371.0, 367.1, 389.6, weight=64.0)
    g.hbar(367.1, 511.4, 387.0, weight=64.0)
    g.diag(361.9, 282.3, 371.7, 294.2, weight=76.0)
    g.hbar(371.7, 465.3, 303.0, weight=76.0)
    g.diag(465.3, 311.7, 481.4, 302.6, weight=76.0)
    g.hbar(203.0, 605.6, 163.1, weight=96.0)
    g.diag(391.8, 279.1, 414.9, 258.2, weight=48.0)
    g.vbar(410.8, 20.0, 258.2, weight=48.0)
    g.diag(406.7, 20.0, 452.7, -55.9, weight=48.0)
    g.diag(587.6, 650.2, 615.1, 443.0, weight=48.0)
    g.diag(615.1, 443.0, 435.5, -54.9, weight=48.0)
    g.hbar(680.6, 834.8, 636.2, weight=48.0)
    g.vbar(847.9, 407.2, 653.3, weight=48.0)
    g.vbar(856.0, -46.6, 407.2, weight=48.0)
    g.hbar(734.3, 851.1, -23.5, weight=48.0)
    g.diag(714.0, 423.1, 728.1, 446.2, weight=96.0)
    g.hbar(728.1, 835.7, 448.1, weight=96.0)
    g.dot(767.9, 287.2, w=96.0, h=124.8, slant=-14.0)
    return g
def g_cjk_unified_ideograph_6f70() -> Glyph:
    """潰 U+6F70 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6F70", advance=1000, unicode=0x6F70, note="潰：自动生成")
    g.diag(207.3, 690.8, 285.4, 640.6, weight=96.0)
    g.hbar(285.4, 355.4, 640.7, weight=96.0)
    g.diag(117.9, 486.2, 182.1, 440.6, weight=96.0)
    g.hbar(182.1, 262.7, 442.7, weight=96.0)
    g.vbar(210.4, 8.0, 389.9, weight=96.0)
    g.dot(429.3, 602.6, w=84.0, h=109.2, slant=-14.0)
    g.hbar(436.0, 721.8, 672.5, weight=48.0)
    g.diag(721.8, 699.6, 664.1, 620.9, weight=48.0)
    g.diag(462.2, 573.9, 474.8, 567.3, weight=48.0)
    g.hbar(474.8, 694.6, 595.0, weight=48.0)
    g.diag(542.1, 707.6, 549.8, 687.6, weight=84.0)
    g.vbar(545.4, 517.3, 687.6, weight=84.0)
    g.diag(541.0, 517.3, 539.4, 515.9, weight=84.0)
    g.hbar(297.5, 877.1, 490.4, weight=64.0)
    g.vbar(439.7, 139.2, 411.2, weight=48.0)
    g.hbar(448.0, 640.7, 378.8, weight=48.0)
    g.vbar(651.8, 152.0, 347.6, weight=48.0)
    g.hbar(470.2, 611.9, 326.2, weight=48.0)
    g.hbar(470.6, 670.4, 249.6, weight=56.0)
    g.hbar(461.2, 664.7, 158.1, weight=64.0)
    g.hbar(514.2, 591.5, 77.2, weight=76.0)
    g.diag(514.2, 69.8, 328.2, -59.0, weight=76.0)
    g.diag(654.5, 106.8, 749.6, -72.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_6f84() -> Glyph:
    """澄 U+6F84 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6F84", advance=1000, unicode=0x6F84, note="澄：自动生成")
    g.diag(124.3, 727.3, 260.3, 604.9, weight=96.0)
    g.diag(53.0, 492.6, 180.2, 373.6, weight=96.0)
    g.diag(89.7, -13.6, 192.4, 317.6, weight=96.0)
    g.diag(301.2, 632.4, 351.1, 705.4, weight=96.0)
    g.diag(351.1, 705.4, 386.9, 599.9, weight=96.0)
    g.diag(386.9, 599.9, 201.8, 334.3, weight=96.0)
    g.diag(257.6, 605.6, 354.8, 550.2, weight=96.0)
    g.diag(354.8, 550.2, 367.4, 521.9, weight=96.0)
    g.diag(732.8, 699.1, 655.8, 754.8, weight=96.0)
    g.diag(655.8, 754.8, 592.8, 684.2, weight=96.0)
    g.vbar(592.8, 674.9, 684.2, weight=96.0)
    g.diag(718.7, 729.8, 760.4, 671.8, weight=96.0)
    g.diag(760.4, 671.8, 663.0, 598.4, weight=96.0)
    g.diag(554.4, 681.2, 947.0, 395.1, weight=96.0)
    g.hbar(404.7, 488.0, 463.2, weight=64.0)
    g.hbar(488.0, 666.7, 477.0, weight=64.0)
    g.diag(343.3, 345.9, 421.3, 174.3, weight=48.0)
    g.hbar(356.9, 624.3, 358.3, weight=48.0)
    g.diag(624.3, 361.4, 660.4, 323.1, weight=48.0)
    g.diag(660.4, 323.1, 601.1, 240.3, weight=48.0)
    g.hbar(432.3, 641.3, 203.9, weight=48.0)
    g.vbar(638.5, 224.7, 251.2, weight=48.0)
    g.dot(408.8, 85.1, w=96.0, h=124.8, slant=-14.0)
    g.diag(604.3, 182.7, 631.0, 125.6, weight=96.0)
    g.diag(631.0, 125.6, 545.6, 14.7, weight=96.0)
    g.hbar(246.9, 822.3, -21.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_6fc0() -> Glyph:
    """激 U+6FC0 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6FC0", advance=1000, unicode=0x6FC0, note="激：自动生成")
    g.dot(172.1, 644.1, w=96.0, h=124.8, slant=-14.0)
    g.diag(53.0, 506.5, 183.6, 372.7, weight=96.0)
    g.hbar(71.5, 134.2, 23.8, weight=96.0)
    g.diag(71.5, 31.8, 215.1, 306.1, weight=96.0)
    g.diag(385.0, 758.1, 422.4, 727.6, weight=48.0)
    g.diag(422.4, 727.6, 330.4, 576.7, weight=48.0)
    g.vbar(305.1, 370.7, 562.7, weight=48.0)
    g.hbar(314.4, 390.7, 567.0, weight=48.0)
    g.hbar(390.7, 541.0, 574.4, weight=48.0)
    g.vbar(504.8, 398.3, 580.8, weight=48.0)
    g.diag(324.4, 462.9, 341.2, 480.5, weight=56.0)
    g.hbar(341.2, 478.0, 475.8, weight=56.0)
    g.diag(337.6, 383.8, 346.9, 394.2, weight=64.0)
    g.hbar(346.9, 458.8, 403.7, weight=64.0)
    g.diag(361.3, 380.7, 417.2, 320.7, weight=48.0)
    g.hbar(204.1, 526.3, 285.7, weight=64.0)
    g.diag(377.4, 220.9, 424.9, 136.3, weight=48.0)
    g.diag(424.9, 136.3, 386.4, -18.6, weight=48.0)
    g.diag(386.4, -18.6, 296.3, 38.4, weight=48.0)
    g.diag(351.0, 265.6, 370.1, 231.1, weight=48.0)
    g.diag(370.1, 231.1, 168.5, 33.3, weight=48.0)
    g.diag(662.4, 722.1, 709.5, 680.8, weight=96.0)
    g.diag(709.5, 680.8, 534.8, 341.8, weight=96.0)
    g.hbar(626.3, 861.4, 456.5, weight=96.0)
    g.vbar(675.4, 302.3, 417.1, weight=64.0)
    g.diag(674.0, 302.3, 562.4, 25.8, weight=64.0)
    g.hbar(450.0, 562.4, 32.8, weight=64.0)
    g.diag(535.6, 277.9, 806.2, 7.5, weight=96.0)
    g.hbar(806.2, 947.0, -1.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_6fc1() -> Glyph:
    """濁 U+6FC1 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6FC1", advance=1000, unicode=0x6FC1, note="濁：自动生成")
    g.hbar(197.3, 384.8, 685.6, weight=96.0)
    g.diag(137.9, 502.5, 273.9, 374.4, weight=96.0)
    g.diag(188.1, -0.8, 168.1, 79.5, weight=96.0)
    g.diag(168.1, 79.5, 313.7, 341.9, weight=96.0)
    g.vbar(408.6, 711.5, 734.4, weight=48.0)
    g.vbar(439.6, 557.2, 711.5, weight=48.0)
    g.hbar(420.3, 745.5, 747.1, weight=48.0)
    g.hbar(745.5, 816.3, 768.0, weight=48.0)
    g.diag(816.3, 766.7, 841.2, 726.9, weight=48.0)
    g.diag(841.2, 726.9, 762.9, 598.1, weight=48.0)
    g.diag(529.4, 717.7, 535.7, 713.5, weight=96.0)
    g.diag(535.7, 713.5, 565.3, 612.1, weight=96.0)
    g.hbar(681.9, 708.7, 726.7, weight=96.0)
    g.diag(681.9, 724.5, 652.5, 637.3, weight=96.0)
    g.diag(652.5, 637.3, 640.1, 631.6, weight=96.0)
    g.hbar(468.3, 759.0, 595.8, weight=48.0)
    g.diag(491.5, 561.9, 514.4, 534.3, weight=96.0)
    g.diag(514.4, 534.3, 364.0, 379.1, weight=96.0)
    g.diag(497.6, 473.8, 744.9, 308.2, weight=76.0)
    g.vbar(750.4, -75.7, 308.2, weight=76.0)
    g.diag(755.8, -75.7, 687.7, 29.7, weight=76.0)
    g.diag(357.0, 357.8, 422.8, 188.8, weight=84.0)
    g.hbar(400.5, 693.5, 340.7, weight=48.0)
    g.diag(693.5, 363.0, 632.8, 265.3, weight=48.0)
    g.hbar(434.1, 665.3, 238.5, weight=48.0)
    g.vbar(502.1, 110.3, 454.7, weight=48.0)
    g.hbar(327.5, 374.5, 55.1, weight=96.0)
    g.hbar(374.5, 626.3, 87.1, weight=96.0)
    g.diag(626.3, 127.7, 633.9, 121.2, weight=96.0)
    g.diag(626.8, 149.8, 694.4, 99.7, weight=56.0)
    g.diag(694.4, 99.7, 682.0, 5.7, weight=56.0)
    return g
def g_cjk_unified_ideograph_6fc3() -> Glyph:
    """濃 U+6FC3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6FC3", advance=1000, unicode=0x6FC3, note="濃：自动生成")
    g.dot(233.1, 660.0, w=96.0, h=124.8, slant=-14.0)
    g.diag(88.1, 480.3, 236.8, 356.9, weight=96.0)
    g.diag(185.6, -34.4, 133.7, 25.4, weight=64.0)
    g.vbar(132.3, 25.4, 81.0, weight=64.0)
    g.diag(131.0, 81.0, 267.5, 333.9, weight=64.0)
    g.vbar(371.4, 624.7, 640.6, weight=48.0)
    g.vbar(395.5, 444.5, 624.7, weight=48.0)
    g.hbar(384.0, 748.2, 652.2, weight=48.0)
    g.vbar(708.7, 484.8, 671.8, weight=48.0)
    g.hbar(478.9, 620.2, 580.0, weight=48.0)
    g.hbar(610.0, 620.2, 595.4, weight=48.0)
    g.diag(462.7, 668.2, 484.2, 699.5, weight=64.0)
    g.vbar(493.4, 503.9, 699.5, weight=64.0)
    g.diag(502.7, 503.9, 491.6, 493.9, weight=64.0)
    g.diag(573.1, 782.0, 588.6, 681.1, weight=48.0)
    g.vbar(578.5, 508.0, 681.1, weight=48.0)
    g.hbar(434.3, 642.7, 479.1, weight=48.0)
    g.diag(642.7, 500.6, 659.4, 487.6, weight=48.0)
    g.hbar(414.5, 653.1, 401.8, weight=64.0)
    g.diag(653.1, 418.6, 691.4, 460.6, weight=64.0)
    g.vbar(335.3, 29.5, 401.6, weight=96.0)
    g.hbar(168.5, 287.0, 3.2, weight=96.0)
    g.diag(467.6, 358.1, 521.7, 303.8, weight=64.0)
    g.hbar(521.7, 650.7, 319.3, weight=64.0)
    g.diag(650.7, 334.9, 703.2, 282.6, weight=64.0)
    g.hbar(421.8, 744.9, 241.5, weight=48.0)
    g.vbar(739.4, 226.6, 260.7, weight=48.0)
    g.diag(404.1, 214.9, 464.6, 157.9, weight=48.0)
    g.vbar(456.1, -28.4, 157.9, weight=48.0)
    g.diag(447.5, -28.4, 620.1, 88.5, weight=48.0)
    g.diag(717.4, 219.6, 730.2, 188.4, weight=96.0)
    g.diag(730.2, 188.4, 659.4, 123.4, weight=96.0)
    g.hbar(649.7, 659.4, 124.4, weight=96.0)
    g.diag(514.0, 201.7, 771.2, -10.1, weight=48.0)
    g.hbar(771.2, 901.9, -15.1, weight=48.0)
    return g
def g_cjk_unified_ideograph_6feb() -> Glyph:
    """濫 U+6FEB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6FEB", advance=1000, unicode=0x6FEB, note="濫：自动生成")
    g.dot(194.0, 660.6, w=84.0, h=109.2, slant=-14.0)
    g.dot(102.4, 454.5, w=96.0, h=124.8, slant=-14.0)
    g.diag(123.8, -41.4, 102.5, 37.7, weight=96.0)
    g.diag(102.5, 37.7, 225.8, 287.5, weight=96.0)
    g.hbar(327.1, 350.6, 662.3, weight=96.0)
    g.hbar(327.1, 565.0, 681.5, weight=96.0)
    g.diag(442.2, 653.8, 464.1, 627.9, weight=76.0)
    g.diag(464.1, 627.9, 434.9, 564.3, weight=76.0)
    g.diag(364.2, 517.5, 371.5, 524.8, weight=48.0)
    g.hbar(371.5, 472.7, 516.9, weight=48.0)
    g.diag(472.7, 509.1, 495.3, 473.8, weight=48.0)
    g.diag(355.8, 399.9, 373.4, 414.1, weight=48.0)
    g.hbar(373.4, 536.9, 427.8, weight=48.0)
    g.diag(443.3, 405.1, 459.6, 358.5, weight=48.0)
    g.diag(459.6, 358.5, 438.1, 341.6, weight=48.0)
    g.vbar(380.4, 312.5, 680.9, weight=48.0)
    g.hbar(450.8, 585.8, 319.2, weight=48.0)
    g.diag(662.9, 771.4, 709.8, 732.3, weight=96.0)
    g.diag(709.8, 732.3, 577.5, 431.1, weight=96.0)
    g.hbar(669.1, 879.3, 564.3, weight=96.0)
    g.dot(707.1, 396.2, w=96.0, h=124.8, slant=-14.0)
    g.diag(314.2, 191.7, 391.5, 17.5, weight=48.0)
    g.hbar(370.4, 478.8, 197.1, weight=48.0)
    g.hbar(478.8, 742.0, 222.4, weight=48.0)
    g.diag(742.0, 243.4, 777.3, 202.1, weight=48.0)
    g.diag(777.3, 202.1, 732.6, 74.1, weight=48.0)
    g.diag(732.6, 74.1, 699.3, 48.1, weight=48.0)
    g.diag(461.0, 175.1, 472.9, 163.1, weight=84.0)
    g.diag(472.9, 163.1, 504.7, 25.2, weight=84.0)
    g.diag(589.0, 199.0, 615.0, 171.9, weight=76.0)
    g.diag(615.0, 171.9, 584.8, 47.1, weight=76.0)
    g.diag(584.8, 47.1, 571.3, 38.7, weight=76.0)
    g.hbar(242.4, 922.0, -1.3, weight=48.0)
    return g
def g_cjk_unified_ideograph_6fef() -> Glyph:
    """濯 U+6FEF —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni6FEF", advance=1000, unicode=0x6FEF, note="濯：自动生成")
    g.dot(246.7, 682.2, w=96.0, h=124.8, slant=-14.0)
    g.diag(113.0, 538.7, 245.8, 410.7, weight=96.0)
    g.diag(166.1, 52.4, 148.3, 121.7, weight=56.0)
    g.diag(148.3, 121.7, 271.5, 382.2, weight=56.0)
    g.diag(359.6, 680.8, 386.4, 718.5, weight=48.0)
    g.hbar(386.4, 527.7, 727.6, weight=48.0)
    g.diag(527.7, 736.6, 494.9, 478.7, weight=48.0)
    g.diag(364.8, 696.1, 435.7, 585.6, weight=48.0)
    g.diag(419.9, 456.8, 375.8, 505.2, weight=96.0)
    g.diag(375.8, 505.2, 441.1, 576.8, weight=96.0)
    g.diag(609.7, 716.2, 635.8, 754.2, weight=48.0)
    g.hbar(635.8, 789.3, 755.2, weight=48.0)
    g.diag(789.3, 756.3, 741.1, 532.8, weight=48.0)
    g.diag(617.1, 731.1, 679.6, 639.6, weight=48.0)
    g.dot(645.7, 587.7, w=96.0, h=124.8, slant=-14.0)
    g.diag(499.9, 503.1, 340.0, 292.9, weight=48.0)
    g.hbar(242.3, 340.0, 284.2, weight=48.0)
    g.diag(432.9, 358.5, 453.9, 293.7, weight=96.0)
    g.vbar(442.7, -1.3, 293.7, weight=96.0)
    g.diag(431.5, -1.3, 470.6, 37.1, weight=96.0)
    g.dot(628.0, 479.3, w=96.0, h=107.3, slant=-14.0)
    g.diag(499.0, 435.6, 573.6, 381.2, weight=64.0)
    g.hbar(573.6, 802.1, 400.4, weight=64.0)
    g.diag(540.1, 220.7, 549.4, 276.6, weight=64.0)
    g.hbar(549.4, 780.5, 296.4, weight=64.0)
    g.diag(546.3, 250.6, 577.9, 186.8, weight=76.0)
    g.hbar(577.9, 753.4, 201.7, weight=76.0)
    g.diag(753.4, 216.7, 785.1, 286.2, weight=76.0)
    g.diag(631.8, 366.4, 659.2, 347.1, weight=96.0)
    g.vbar(658.1, 136.5, 347.1, weight=96.0)
    g.diag(657.0, 136.5, 641.6, 116.3, weight=96.0)
    g.diag(473.5, 81.2, 483.2, 73.7, weight=84.0)
    g.hbar(483.2, 872.0, 81.3, weight=84.0)
    return g
def g_cjk_unified_ideograph_70c8() -> Glyph:
    """烈 U+70C8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni70C8", advance=1000, unicode=0x70C8, note="烈：自动生成")
    g.hbar(219.9, 265.0, 662.4, weight=96.0)
    g.hbar(219.9, 503.8, 689.3, weight=96.0)
    g.diag(503.8, 711.4, 566.1, 652.2, weight=96.0)
    g.diag(301.3, 656.6, 280.2, 558.6, weight=48.0)
    g.diag(280.2, 558.6, 141.2, 348.7, weight=48.0)
    g.diag(292.8, 502.9, 360.1, 403.7, weight=48.0)
    g.diag(360.1, 403.7, 164.3, 130.3, weight=48.0)
    g.dot(282.2, 376.1, w=96.0, h=124.8, slant=-14.0)
    g.diag(559.6, 675.9, 621.7, 299.0, weight=96.0)
    g.diag(723.4, 772.0, 757.8, 589.6, weight=96.0)
    g.vbar(755.1, 233.1, 589.6, weight=96.0)
    g.diag(752.3, 233.1, 629.7, 290.0, weight=96.0)
    g.diag(160.5, 127.0, 81.0, -67.0, weight=96.0)
    g.diag(280.8, 167.2, 380.8, -1.5, weight=96.0)
    g.diag(525.8, 137.1, 622.5, 2.8, weight=96.0)
    g.diag(767.7, 193.5, 919.0, -62.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_714e() -> Glyph:
    """煎 U+714E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni714E", advance=1000, unicode=0x714E, note="煎：自动生成")
    g.diag(331.4, 745.6, 403.2, 698.5, weight=96.0)
    g.diag(403.2, 698.5, 425.7, 630.1, weight=96.0)
    g.diag(589.7, 802.0, 623.2, 771.5, weight=96.0)
    g.diag(623.2, 771.5, 544.6, 639.1, weight=96.0)
    g.hbar(524.1, 544.6, 636.0, weight=96.0)
    g.hbar(137.7, 862.3, 585.3, weight=96.0)
    g.vbar(264.1, 117.2, 488.5, weight=96.0)
    g.diag(311.0, 477.8, 421.5, 388.4, weight=64.0)
    g.vbar(429.9, 156.8, 388.4, weight=64.0)
    g.hbar(296.8, 438.3, 179.7, weight=64.0)
    g.hbar(314.8, 432.5, 380.4, weight=64.0)
    g.diag(311.8, 273.4, 323.3, 288.2, weight=76.0)
    g.hbar(323.3, 430.5, 288.8, weight=76.0)
    g.hbar(496.2, 579.2, 461.6, weight=84.0)
    g.vbar(581.2, 241.5, 449.6, weight=84.0)
    g.diag(669.9, 576.4, 752.7, 142.6, weight=96.0)
    g.diag(752.7, 142.6, 606.1, 216.9, weight=96.0)
    g.diag(247.0, 117.8, 154.1, -67.0, weight=96.0)
    g.diag(392.7, 138.3, 423.7, -26.0, weight=84.0)
    g.diag(474.8, 144.4, 613.2, -12.7, weight=96.0)
    g.diag(709.8, 136.5, 848.9, -56.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_7159() -> Glyph:
    """煙 U+7159 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7159", advance=1000, unicode=0x7159, note="煙：自动生成")
    g.diag(207.0, 508.4, 115.3, 427.5, weight=96.0)
    g.diag(115.3, 427.5, 195.0, 334.0, weight=96.0)
    g.diag(371.1, 538.9, 353.0, 584.3, weight=96.0)
    g.diag(353.0, 584.3, 277.6, 510.2, weight=96.0)
    g.vbar(193.5, 471.3, 758.3, weight=96.0)
    g.diag(196.2, 471.3, 53.0, -48.3, weight=96.0)
    g.diag(259.2, 237.6, 421.8, 163.3, weight=96.0)
    g.diag(474.2, 641.5, 469.4, 646.9, weight=96.0)
    g.hbar(469.4, 825.9, 679.1, weight=96.0)
    g.diag(390.2, 500.5, 383.0, 486.0, weight=48.0)
    g.vbar(415.4, 276.3, 486.0, weight=48.0)
    g.hbar(398.6, 811.1, 524.4, weight=48.0)
    g.diag(811.1, 555.8, 847.3, 513.1, weight=48.0)
    g.diag(847.3, 513.1, 781.2, 322.0, weight=48.0)
    g.hbar(755.4, 781.2, 323.9, weight=48.0)
    g.diag(510.3, 629.1, 545.3, 599.5, weight=56.0)
    g.diag(545.3, 599.5, 524.7, 441.8, weight=56.0)
    g.diag(524.7, 441.8, 441.8, 364.4, weight=56.0)
    g.diag(619.6, 653.0, 658.2, 560.4, weight=48.0)
    g.diag(658.2, 560.4, 745.3, 431.6, weight=48.0)
    g.hbar(458.8, 539.9, 295.1, weight=48.0)
    g.hbar(539.9, 761.7, 316.6, weight=48.0)
    g.diag(449.2, 234.4, 519.5, 166.3, weight=96.0)
    g.hbar(519.5, 722.2, 189.9, weight=96.0)
    g.diag(722.2, 213.6, 767.3, 262.3, weight=96.0)
    g.diag(558.4, 288.6, 575.3, 277.0, weight=96.0)
    g.diag(575.3, 277.0, 608.2, 90.6, weight=96.0)
    g.diag(608.2, 90.6, 574.7, 44.6, weight=96.0)
    g.hbar(310.3, 927.0, 10.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_7169() -> Glyph:
    """煩 U+7169 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7169", advance=1000, unicode=0x7169, note="煩：自动生成")
    g.diag(250.3, 542.4, 165.1, 464.6, weight=96.0)
    g.diag(165.1, 464.6, 244.2, 360.9, weight=96.0)
    g.diag(486.7, 554.0, 418.0, 597.4, weight=48.0)
    g.diag(418.0, 597.4, 307.7, 492.7, weight=48.0)
    g.vbar(236.3, 484.9, 762.0, weight=48.0)
    g.diag(237.4, 484.9, 84.0, 3.1, weight=48.0)
    g.diag(302.3, 263.4, 376.6, 218.8, weight=96.0)
    g.hbar(376.6, 483.2, 200.5, weight=96.0)
    g.hbar(490.5, 911.0, 698.9, weight=48.0)
    g.diag(666.6, 684.9, 577.8, 546.7, weight=48.0)
    g.vbar(527.4, 159.4, 537.6, weight=48.0)
    g.hbar(532.8, 756.8, 548.9, weight=48.0)
    g.vbar(774.7, 452.0, 568.6, weight=48.0)
    g.vbar(795.0, 270.6, 452.0, weight=48.0)
    g.diag(797.5, 270.6, 772.5, 184.9, weight=48.0)
    g.hbar(555.6, 774.0, 427.4, weight=76.0)
    g.hbar(555.6, 773.9, 321.2, weight=84.0)
    g.hbar(547.6, 773.6, 184.6, weight=76.0)
    g.diag(614.7, 164.0, 385.4, -55.0, weight=76.0)
    g.diag(769.2, 137.8, 871.0, -67.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_718a() -> Glyph:
    """熊 U+718A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni718A", advance=1000, unicode=0x718A, note="熊：自动生成")
    g.diag(328.4, 777.0, 351.1, 739.2, weight=48.0)
    g.diag(351.1, 739.2, 311.8, 609.7, weight=48.0)
    g.hbar(311.8, 438.2, 601.1, weight=48.0)
    g.hbar(406.4, 463.6, 599.9, weight=48.0)
    g.diag(463.6, 594.7, 442.9, 570.6, weight=48.0)
    g.vbar(223.9, 141.4, 439.4, weight=96.0)
    g.diag(254.7, 422.7, 382.6, 346.4, weight=48.0)
    g.vbar(396.6, 164.4, 346.4, weight=48.0)
    g.hbar(323.3, 410.7, 183.9, weight=48.0)
    g.hbar(256.1, 353.0, 341.7, weight=48.0)
    g.hbar(251.0, 410.7, 265.8, weight=56.0)
    g.diag(799.6, 658.6, 744.6, 706.2, weight=96.0)
    g.diag(744.6, 706.2, 600.6, 637.4, weight=96.0)
    g.diag(600.6, 637.4, 596.8, 628.5, weight=96.0)
    g.diag(547.6, 773.9, 538.5, 784.5, weight=76.0)
    g.diag(538.5, 784.5, 600.8, 495.2, weight=76.0)
    g.hbar(600.8, 804.2, 506.6, weight=76.0)
    g.vbar(802.1, 518.0, 667.8, weight=76.0)
    g.diag(750.7, 461.5, 769.1, 382.7, weight=96.0)
    g.diag(769.1, 382.7, 598.5, 301.0, weight=96.0)
    g.diag(598.5, 301.0, 596.8, 297.6, weight=96.0)
    g.diag(582.9, 489.9, 730.4, 173.1, weight=64.0)
    g.hbar(730.4, 838.4, 175.2, weight=64.0)
    g.vbar(835.9, 177.4, 300.7, weight=64.0)
    g.diag(217.6, 110.7, 134.8, -67.0, weight=96.0)
    g.diag(383.4, 139.7, 412.4, -16.8, weight=84.0)
    g.dot(590.4, 73.3, w=96.0, h=124.8, slant=-14.0)
    g.diag(711.9, 134.1, 865.2, -61.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_71b1() -> Glyph:
    """熱 U+71B1 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni71B1", advance=1000, unicode=0x71B1, note="熱：自动生成")
    g.hbar(222.0, 472.6, 646.5, weight=92.0)
    g.diag(322.2, 787.0, 362.6, 751.4, weight=96.0)
    g.vbar(358.1, 574.7, 751.4, weight=96.0)
    g.diag(353.7, 574.7, 337.9, 554.1, weight=96.0)
    g.hbar(88.3, 480.4, 519.2, weight=64.0)
    g.hbar(256.9, 276.0, 431.4, weight=56.0)
    g.diag(256.9, 429.7, 140.4, 327.1, weight=56.0)
    g.dot(429.3, 440.1, w=96.0, h=97.9, slant=-14.0)
    g.hbar(202.3, 432.3, 315.8, weight=48.0)
    g.diag(323.2, 392.9, 347.8, 357.5, weight=96.0)
    g.vbar(346.8, 263.2, 357.5, weight=96.0)
    g.diag(345.8, 263.2, 329.1, 236.7, weight=96.0)
    g.hbar(159.1, 461.8, 220.9, weight=64.0)
    g.diag(576.7, 749.7, 434.2, 146.3, weight=96.0)
    g.hbar(509.9, 727.8, 479.1, weight=64.0)
    g.diag(727.8, 433.7, 906.3, 157.7, weight=64.0)
    g.vbar(914.0, 157.7, 327.1, weight=64.0)
    g.diag(517.8, 364.4, 664.2, 251.4, weight=64.0)
    g.diag(231.8, 89.3, 155.1, -67.0, weight=96.0)
    g.dot(377.7, 22.4, w=96.0, h=119.5, slant=-14.0)
    g.dot(560.5, 39.6, w=96.0, h=124.8, slant=-14.0)
    g.diag(720.2, 100.1, 850.9, -44.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_71c3() -> Glyph:
    """燃 U+71C3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni71C3", advance=1000, unicode=0x71C3, note="燃：自动生成")
    g.dot(114.2, 446.1, w=96.0, h=124.8, slant=0.0)
    g.diag(315.8, 594.4, 326.4, 568.5, weight=48.0)
    g.diag(326.4, 568.5, 261.1, 497.9, weight=48.0)
    g.diag(192.4, 746.7, 53.0, 0.1, weight=48.0)
    g.dot(284.0, 241.5, w=96.0, h=109.1, slant=-14.0)
    g.diag(446.2, 698.0, 426.8, 596.9, weight=48.0)
    g.diag(426.8, 596.9, 320.8, 406.3, weight=48.0)
    g.diag(449.2, 543.7, 497.8, 452.8, weight=48.0)
    g.diag(497.8, 452.8, 354.6, 226.1, weight=48.0)
    g.dot(441.3, 462.5, w=64.0, h=83.2, slant=-14.0)
    g.dot(397.9, 380.4, w=64.0, h=83.2, slant=-14.0)
    g.hbar(611.5, 849.4, 474.0, weight=96.0)
    g.vbar(661.4, 563.6, 750.7, weight=96.0)
    g.diag(661.5, 563.6, 526.9, 183.3, weight=96.0)
    g.diag(710.0, 426.2, 707.3, 410.0, weight=96.0)
    g.diag(707.3, 410.0, 846.3, 226.8, weight=96.0)
    g.hbar(846.3, 942.0, 212.0, weight=96.0)
    g.dot(828.0, 615.3, w=96.0, h=83.7, slant=-14.0)
    g.dot(335.7, 36.4, w=96.0, h=124.8, slant=14.0)
    g.dot(489.5, 67.3, w=96.0, h=103.7, slant=-14.0)
    g.dot(637.9, 69.8, w=96.0, h=116.9, slant=-14.0)
    g.diag(760.8, 120.6, 884.3, -31.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_71e5() -> Glyph:
    """燥 U+71E5 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni71E5", advance=1000, unicode=0x71E5, note="燥：自动生成")
    g.diag(204.9, 532.9, 121.0, 464.1, weight=96.0)
    g.diag(121.0, 464.1, 193.5, 361.0, weight=96.0)
    g.diag(393.5, 543.8, 354.8, 596.1, weight=96.0)
    g.diag(354.8, 596.1, 274.5, 525.6, weight=96.0)
    g.diag(274.5, 525.6, 269.1, 510.9, weight=96.0)
    g.vbar(196.9, 498.6, 759.4, weight=96.0)
    g.diag(198.4, 498.6, 61.7, 13.0, weight=96.0)
    g.diag(250.0, 256.7, 313.8, 185.5, weight=96.0)
    g.diag(313.8, 185.5, 347.0, 133.4, weight=96.0)
    g.vbar(479.9, 728.6, 745.0, weight=48.0)
    g.diag(476.8, 728.6, 531.7, 611.6, weight=48.0)
    g.hbar(492.5, 720.7, 748.2, weight=48.0)
    g.diag(720.7, 758.0, 667.3, 660.5, weight=48.0)
    g.hbar(530.9, 696.7, 647.6, weight=48.0)
    g.vbar(397.3, 382.7, 506.9, weight=48.0)
    g.hbar(392.8, 533.0, 508.0, weight=48.0)
    g.vbar(523.4, 453.5, 518.7, weight=48.0)
    g.diag(513.7, 453.5, 500.1, 440.8, weight=48.0)
    g.diag(421.4, 398.7, 427.7, 405.8, weight=48.0)
    g.hbar(427.7, 487.9, 413.9, weight=48.0)
    g.hbar(487.9, 547.6, 413.7, weight=48.0)
    g.vbar(620.3, 421.2, 541.8, weight=64.0)
    g.hbar(619.2, 778.4, 545.1, weight=48.0)
    g.vbar(768.9, 491.9, 555.5, weight=48.0)
    g.diag(759.5, 491.9, 736.6, 473.7, weight=48.0)
    g.diag(650.0, 444.4, 659.0, 438.8, weight=48.0)
    g.hbar(659.0, 770.8, 448.4, weight=48.0)
    g.vbar(770.8, 458.0, 476.4, weight=48.0)
    g.hbar(351.3, 863.5, 297.8, weight=48.0)
    g.diag(556.8, 388.6, 595.1, 342.0, weight=96.0)
    g.vbar(590.3, -52.0, 342.0, weight=96.0)
    g.diag(554.4, 280.1, 305.4, 70.3, weight=48.0)
    g.diag(613.1, 290.3, 933.3, 90.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_7206() -> Glyph:
    """爆 U+7206 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7206", advance=1000, unicode=0x7206, note="爆：自动生成")
    g.vbar(113.0, 321.0, 490.3, weight=96.0)
    g.diag(333.6, 588.0, 347.1, 560.0, weight=48.0)
    g.diag(347.1, 560.0, 279.4, 500.9, weight=48.0)
    g.diag(279.4, 500.9, 277.5, 487.4, weight=48.0)
    g.vbar(202.3, 459.6, 707.0, weight=48.0)
    g.diag(204.6, 459.6, 53.0, -21.5, weight=48.0)
    g.diag(256.2, 255.2, 320.3, 204.2, weight=96.0)
    g.diag(320.3, 204.2, 331.6, 172.0, weight=96.0)
    g.diag(438.1, 718.6, 499.0, 527.1, weight=96.0)
    g.diag(489.4, 696.4, 500.5, 712.0, weight=48.0)
    g.hbar(500.5, 681.8, 727.8, weight=48.0)
    g.hbar(681.8, 746.2, 729.2, weight=48.0)
    g.vbar(720.8, 565.8, 714.9, weight=48.0)
    g.diag(508.7, 621.9, 514.5, 633.5, weight=56.0)
    g.hbar(514.5, 643.2, 640.3, weight=56.0)
    g.diag(517.4, 546.4, 526.2, 556.2, weight=48.0)
    g.hbar(526.2, 661.3, 567.4, weight=48.0)
    g.diag(661.3, 578.5, 672.2, 570.6, weight=48.0)
    g.hbar(430.3, 741.9, 440.9, weight=76.0)
    g.diag(477.7, 498.0, 504.4, 471.4, weight=96.0)
    g.vbar(510.0, 354.9, 471.4, weight=96.0)
    g.diag(515.6, 354.9, 505.8, 347.1, weight=96.0)
    g.diag(640.3, 531.9, 665.4, 500.0, weight=96.0)
    g.diag(665.4, 500.0, 644.2, 383.9, weight=96.0)
    g.diag(644.2, 383.9, 627.7, 366.4, weight=96.0)
    g.hbar(391.6, 815.4, 331.6, weight=48.0)
    g.diag(471.0, 294.9, 433.4, 223.4, weight=48.0)
    g.diag(433.4, 223.4, 262.5, 28.0, weight=48.0)
    g.diag(262.5, 28.0, 277.5, 57.8, weight=48.0)
    g.diag(646.1, 331.6, 947.0, 161.3, weight=48.0)
    g.diag(559.0, 256.1, 607.3, 202.8, weight=56.0)
    g.diag(607.3, 202.8, 576.4, -44.9, weight=56.0)
    g.hbar(480.6, 576.4, -25.5, weight=56.0)
    g.dot(485.0, 152.6, w=96.0, h=78.8, slant=-14.0)
    g.hbar(381.0, 420.0, 12.7, weight=64.0)
    g.diag(420.0, 7.3, 522.3, 82.0, weight=64.0)
    g.diag(689.6, 208.7, 699.3, 183.6, weight=48.0)
    g.diag(699.3, 183.6, 638.4, 135.2, weight=48.0)
    g.diag(651.9, 87.8, 787.4, -14.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_7235() -> Glyph:
    """爵 U+7235 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7235", advance=1000, unicode=0x7235, note="爵：自动生成")
    g.hbar(493.9, 610.7, 767.6, weight=84.0)
    g.diag(493.9, 781.7, 266.7, 679.1, weight=84.0)
    g.diag(269.2, 693.0, 316.3, 565.6, weight=48.0)
    g.diag(372.8, 708.1, 445.4, 587.6, weight=48.0)
    g.diag(590.2, 757.8, 652.9, 713.7, weight=96.0)
    g.diag(652.9, 713.7, 519.5, 619.6, weight=96.0)
    g.hbar(217.5, 228.9, 522.2, weight=48.0)
    g.vbar(244.4, 396.5, 520.3, weight=48.0)
    g.diag(246.4, 516.2, 261.2, 535.5, weight=96.0)
    g.hbar(261.2, 609.9, 564.4, weight=96.0)
    g.hbar(609.9, 722.6, 579.9, weight=96.0)
    g.diag(722.6, 566.5, 649.8, 435.5, weight=96.0)
    g.diag(359.2, 533.8, 367.8, 525.9, weight=96.0)
    g.diag(367.8, 525.9, 400.5, 443.8, weight=96.0)
    g.diag(505.0, 560.7, 529.7, 531.5, weight=96.0)
    g.diag(529.7, 531.5, 494.7, 464.5, weight=96.0)
    g.hbar(272.9, 396.6, 419.2, weight=48.0)
    g.hbar(396.6, 637.5, 438.6, weight=48.0)
    g.hbar(182.5, 381.4, 320.8, weight=48.0)
    g.vbar(360.5, 155.2, 334.3, weight=48.0)
    g.hbar(321.8, 339.5, 156.6, weight=48.0)
    g.hbar(194.7, 336.2, 230.2, weight=56.0)
    g.diag(195.7, 134.5, 207.1, 145.9, weight=64.0)
    g.hbar(207.1, 316.4, 157.3, weight=64.0)
    g.diag(124.4, 339.3, 156.4, 314.2, weight=48.0)
    g.vbar(172.1, -11.4, 314.2, weight=48.0)
    g.hbar(187.8, 309.2, 11.5, weight=48.0)
    g.diag(309.2, 34.5, 319.0, 50.5, weight=48.0)
    g.diag(314.2, 64.8, 365.4, 28.0, weight=48.0)
    g.diag(365.4, 28.0, 377.8, -14.4, weight=48.0)
    g.hbar(405.9, 885.6, 283.0, weight=96.0)
    g.diag(625.5, 405.8, 689.0, 316.6, weight=96.0)
    g.vbar(667.1, -72.0, 316.6, weight=96.0)
    g.diag(645.3, -72.0, 532.2, 64.4, weight=96.0)
    g.diag(457.7, 226.2, 521.5, 131.4, weight=84.0)
    g.vbar(524.2, 22.0, 131.4, weight=84.0)
    return g
def g_cjk_unified_ideograph_723d() -> Glyph:
    """爽 U+723D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni723D", advance=1000, unicode=0x723D, note="爽：自动生成")
    g.hbar(288.0, 609.8, 623.1, weight=96.0)
    g.hbar(609.8, 652.1, 648.4, weight=96.0)
    g.diag(313.1, 560.9, 331.4, 523.1, weight=96.0)
    g.diag(331.4, 523.1, 178.5, 362.2, weight=96.0)
    g.vbar(178.5, 356.0, 362.2, weight=96.0)
    g.diag(242.4, 473.7, 317.1, 437.3, weight=96.0)
    g.vbar(319.2, 385.3, 437.3, weight=96.0)
    g.diag(313.4, 382.3, 151.7, 169.2, weight=84.0)
    g.diag(184.8, 330.2, 359.8, 181.1, weight=96.0)
    g.diag(652.5, 637.5, 674.6, 570.6, weight=56.0)
    g.diag(674.6, 570.6, 532.5, 376.1, weight=56.0)
    g.diag(492.6, 556.0, 659.9, 436.3, weight=96.0)
    g.diag(690.8, 424.3, 707.8, 382.4, weight=84.0)
    g.diag(707.8, 382.4, 518.3, 224.9, weight=84.0)
    g.diag(532.6, 376.0, 660.6, 264.5, weight=96.0)
    g.diag(660.6, 264.5, 651.9, 269.9, weight=96.0)
    g.vbar(400.3, 486.5, 791.0, weight=96.0)
    g.diag(386.7, 486.5, 78.0, -49.0, weight=96.0)
    g.diag(460.6, 258.9, 917.0, -56.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_731b() -> Glyph:
    """猛 U+731B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni731B", advance=1000, unicode=0x731B, note="猛：自动生成")
    g.diag(324.9, 723.9, 281.9, 614.0, weight=48.0)
    g.diag(281.9, 614.0, 112.7, 424.4, weight=48.0)
    g.diag(151.3, 678.2, 238.8, 208.5, weight=48.0)
    g.diag(238.8, 208.5, 167.6, 64.9, weight=48.0)
    g.diag(301.3, 429.4, 63.0, 137.0, weight=48.0)
    g.hbar(476.2, 752.2, 688.6, weight=64.0)
    g.diag(752.2, 705.1, 662.0, 588.8, weight=64.0)
    g.hbar(650.5, 662.0, 588.5, weight=64.0)
    g.diag(614.5, 589.2, 691.9, 361.0, weight=96.0)
    g.diag(691.9, 361.0, 553.3, 290.0, weight=96.0)
    g.hbar(413.3, 888.4, 498.5, weight=64.0)
    g.hbar(436.6, 447.1, 233.4, weight=64.0)
    g.diag(436.6, 232.5, 468.1, 67.0, weight=64.0)
    g.diag(468.1, 67.0, 482.5, 51.3, weight=64.0)
    g.hbar(458.7, 797.0, 255.6, weight=48.0)
    g.diag(797.0, 291.8, 835.4, 246.6, weight=48.0)
    g.diag(835.4, 246.6, 762.4, 71.5, weight=48.0)
    g.diag(553.4, 228.4, 546.3, 216.9, weight=84.0)
    g.diag(546.3, 216.9, 574.7, 59.9, weight=84.0)
    g.diag(650.8, 245.7, 676.7, 228.0, weight=76.0)
    g.diag(676.7, 228.0, 656.9, 81.6, weight=76.0)
    g.diag(656.9, 81.6, 640.7, 72.1, weight=76.0)
    g.hbar(374.7, 927.0, 32.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_732b() -> Glyph:
    """猫 U+732B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni732B", advance=1000, unicode=0x732B, note="猫：自动生成")
    g.diag(323.1, 742.4, 289.0, 634.6, weight=48.0)
    g.diag(289.0, 634.6, 114.7, 421.6, weight=48.0)
    g.diag(143.0, 658.4, 249.8, 194.8, weight=48.0)
    g.diag(249.8, 194.8, 174.4, 62.4, weight=48.0)
    g.diag(297.3, 443.0, 53.0, 118.1, weight=48.0)
    g.hbar(336.0, 912.0, 541.5, weight=96.0)
    g.diag(486.0, 642.2, 525.5, 612.9, weight=64.0)
    g.diag(525.5, 612.9, 562.9, 361.1, weight=64.0)
    g.diag(710.7, 755.5, 755.5, 714.9, weight=96.0)
    g.diag(755.5, 714.9, 689.2, 398.4, weight=96.0)
    g.vbar(443.3, 252.1, 338.1, weight=48.0)
    g.diag(448.0, 252.1, 497.7, 27.1, weight=48.0)
    g.hbar(446.1, 761.0, 285.5, weight=48.0)
    g.diag(761.0, 242.0, 793.6, -20.5, weight=48.0)
    g.hbar(498.1, 792.6, 193.0, weight=96.0)
    g.diag(602.3, 323.0, 639.4, 289.5, weight=48.0)
    g.diag(639.4, 289.5, 614.1, 85.6, weight=48.0)
    g.hbar(506.3, 768.9, 59.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_7336() -> Glyph:
    """猶 U+7336 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7336", advance=1000, unicode=0x7336, note="猶：自动生成")
    g.diag(332.0, 762.4, 292.6, 653.6, weight=48.0)
    g.diag(292.6, 653.6, 95.1, 430.2, weight=48.0)
    g.diag(146.3, 688.1, 228.7, 202.8, weight=48.0)
    g.diag(228.7, 202.8, 162.4, 38.9, weight=48.0)
    g.diag(263.7, 423.2, 53.0, 104.1, weight=48.0)
    g.dot(525.1, 683.6, w=96.0, h=106.6, slant=-14.0)
    g.diag(730.3, 786.4, 761.0, 750.2, weight=96.0)
    g.diag(761.0, 750.2, 635.0, 607.8, weight=96.0)
    g.hbar(386.1, 927.0, 551.1, weight=96.0)
    g.diag(404.2, 420.2, 423.5, 291.6, weight=48.0)
    g.vbar(426.9, -20.3, 291.6, weight=48.0)
    g.hbar(461.4, 589.6, 401.7, weight=48.0)
    g.diag(589.6, 407.3, 767.3, 262.8, weight=48.0)
    g.diag(767.3, 262.8, 811.6, -51.4, weight=48.0)
    g.diag(526.6, 518.5, 571.8, 485.4, weight=48.0)
    g.diag(571.8, 485.4, 499.5, 228.5, weight=48.0)
    g.diag(629.0, 535.6, 721.6, 479.0, weight=48.0)
    g.diag(721.6, 479.0, 594.8, 292.8, weight=48.0)
    g.hbar(594.8, 761.4, 284.8, weight=48.0)
    g.hbar(515.6, 712.3, 150.3, weight=92.0)
    g.hbar(457.4, 766.4, 30.8, weight=92.0)
    return g
def g_cjk_unified_ideograph_733f() -> Glyph:
    """猿 U+733F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni733F", advance=1000, unicode=0x733F, note="猿：自动生成")
    g.diag(325.1, 673.0, 282.6, 570.7, weight=48.0)
    g.diag(282.6, 570.7, 100.3, 373.5, weight=48.0)
    g.diag(133.8, 625.1, 235.5, 173.7, weight=48.0)
    g.diag(235.5, 173.7, 148.1, 62.6, weight=48.0)
    g.diag(282.4, 415.7, 63.0, 110.4, weight=48.0)
    g.hbar(381.6, 706.1, 618.9, weight=96.0)
    g.diag(706.1, 618.9, 748.3, 559.3, weight=96.0)
    g.diag(548.1, 740.9, 586.3, 706.4, weight=96.0)
    g.vbar(581.5, 523.7, 706.4, weight=96.0)
    g.diag(576.8, 523.7, 561.4, 505.5, weight=96.0)
    g.hbar(322.9, 826.5, 475.7, weight=64.0)
    g.vbar(456.8, 375.0, 387.5, weight=48.0)
    g.vbar(473.1, 278.8, 375.0, weight=48.0)
    g.diag(489.8, 278.8, 506.0, 264.4, weight=48.0)
    g.hbar(470.4, 701.9, 396.7, weight=48.0)
    g.diag(701.9, 409.9, 649.7, 320.6, weight=48.0)
    g.diag(513.6, 281.7, 523.9, 276.5, weight=48.0)
    g.hbar(523.9, 677.3, 290.8, weight=48.0)
    g.vbar(677.8, 305.0, 322.8, weight=48.0)
    g.hbar(521.4, 535.6, 219.7, weight=96.0)
    g.diag(521.4, 221.9, 329.0, 66.4, weight=96.0)
    g.vbar(492.1, -19.9, 151.8, weight=64.0)
    g.diag(497.6, -19.9, 653.9, 100.5, weight=64.0)
    g.diag(734.7, 297.9, 762.0, 263.6, weight=96.0)
    g.diag(762.0, 263.6, 643.7, 173.5, weight=96.0)
    g.diag(550.0, 229.0, 947.0, 31.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_7344() -> Glyph:
    """獄 U+7344 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7344", advance=1000, unicode=0x7344, note="獄：自动生成")
    g.diag(312.3, 684.4, 268.6, 580.5, weight=48.0)
    g.diag(268.6, 580.5, 93.6, 392.0, weight=48.0)
    g.diag(134.1, 645.7, 204.1, 218.7, weight=48.0)
    g.diag(204.1, 218.7, 148.2, 86.5, weight=48.0)
    g.diag(230.3, 392.0, 53.0, 122.3, weight=48.0)
    g.dot(487.3, 675.4, w=96.0, h=119.0, slant=-14.0)
    g.hbar(322.7, 547.2, 521.7, weight=48.0)
    g.hbar(376.5, 503.8, 418.9, weight=76.0)
    g.hbar(362.3, 513.2, 318.9, weight=64.0)
    g.diag(316.1, 229.8, 344.4, 199.6, weight=48.0)
    g.diag(344.4, 199.6, 372.7, 76.1, weight=48.0)
    g.hbar(370.8, 504.6, 221.0, weight=48.0)
    g.vbar(495.2, 170.4, 233.0, weight=48.0)
    g.hbar(465.1, 485.9, 166.2, weight=48.0)
    g.diag(387.8, 110.1, 399.0, 122.5, weight=48.0)
    g.hbar(399.0, 504.7, 125.7, weight=48.0)
    g.hbar(541.5, 824.4, 419.4, weight=96.0)
    g.vbar(611.0, 485.9, 725.9, weight=96.0)
    g.diag(612.6, 485.9, 477.4, 50.6, weight=96.0)
    g.diag(660.3, 286.4, 823.4, 43.9, weight=96.0)
    g.hbar(823.4, 947.0, 26.5, weight=96.0)
    g.dot(798.5, 577.3, w=96.0, h=105.5, slant=-14.0)
    return g
def g_cjk_unified_ideograph_7372() -> Glyph:
    """獲 U+7372 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7372", advance=1000, unicode=0x7372, note="獲：自动生成")
    g.diag(282.2, 705.6, 254.4, 615.1, weight=48.0)
    g.diag(254.4, 615.1, 101.6, 422.9, weight=48.0)
    g.diag(125.8, 653.1, 207.3, 201.9, weight=48.0)
    g.diag(207.3, 201.9, 148.2, 48.9, weight=48.0)
    g.diag(251.2, 422.2, 53.0, 131.4, weight=48.0)
    g.diag(472.2, 697.4, 496.0, 730.8, weight=84.0)
    g.diag(496.0, 730.8, 520.6, 602.5, weight=84.0)
    g.hbar(338.0, 545.9, 672.8, weight=84.0)
    g.diag(696.1, 733.4, 688.3, 760.9, weight=84.0)
    g.diag(688.3, 760.9, 636.3, 626.4, weight=84.0)
    g.hbar(691.2, 853.5, 697.3, weight=84.0)
    g.hbar(498.6, 517.5, 554.6, weight=48.0)
    g.diag(498.6, 557.5, 292.7, 395.0, weight=48.0)
    g.diag(439.4, 466.7, 487.3, 180.2, weight=48.0)
    g.diag(487.3, 180.2, 464.3, 230.7, weight=48.0)
    g.hbar(547.2, 609.6, 613.0, weight=48.0)
    g.diag(609.6, 605.5, 632.9, 560.3, weight=48.0)
    g.diag(516.2, 554.3, 570.7, 529.8, weight=48.0)
    g.hbar(570.7, 750.5, 546.3, weight=48.0)
    g.diag(549.0, 402.0, 556.2, 450.1, weight=48.0)
    g.hbar(556.2, 687.3, 465.1, weight=48.0)
    g.diag(687.3, 480.2, 714.1, 428.9, weight=48.0)
    g.diag(542.8, 432.7, 597.0, 387.9, weight=48.0)
    g.hbar(597.0, 702.9, 399.6, weight=48.0)
    g.vbar(713.1, 411.2, 457.2, weight=48.0)
    g.diag(606.7, 514.2, 630.0, 497.7, weight=84.0)
    g.vbar(629.1, 354.9, 497.7, weight=84.0)
    g.diag(628.1, 354.9, 614.5, 334.5, weight=84.0)
    g.hbar(462.5, 823.4, 304.6, weight=56.0)
    g.diag(471.0, 225.4, 565.6, 149.9, weight=84.0)
    g.diag(565.6, 149.9, 365.8, -29.8, weight=84.0)
    g.diag(465.3, 188.4, 937.0, -58.0, weight=84.0)
    return g
def g_cjk_unified_ideograph_73e0() -> Glyph:
    """珠 U+73E0 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni73E0", advance=1000, unicode=0x73E0, note="珠：自动生成")
    g.hbar(134.3, 354.2, 569.2, weight=96.0)
    g.hbar(144.5, 344.0, 373.4, weight=96.0)
    g.diag(228.5, 535.5, 263.2, 512.0, weight=96.0)
    g.vbar(249.5, 214.0, 512.0, weight=96.0)
    g.hbar(99.2, 150.9, 141.1, weight=76.0)
    g.diag(150.9, 136.4, 375.4, 260.2, weight=76.0)
    g.diag(436.4, 623.3, 466.7, 590.9, weight=96.0)
    g.diag(466.7, 590.9, 376.3, 435.7, weight=96.0)
    g.hbar(463.2, 719.0, 548.9, weight=96.0)
    g.hbar(360.6, 821.6, 393.3, weight=48.0)
    g.vbar(554.2, 489.3, 772.0, weight=96.0)
    g.vbar(568.1, -52.0, 489.3, weight=96.0)
    g.diag(593.4, 379.4, 299.7, 69.9, weight=48.0)
    g.diag(603.6, 377.6, 915.8, 130.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_73ed() -> Glyph:
    """班 U+73ED —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni73ED", advance=1000, unicode=0x73ED, note="班：自动生成")
    g.vbar(181.4, 566.9, 576.9, weight=96.0)
    g.hbar(183.7, 308.6, 592.2, weight=96.0)
    g.diag(308.6, 607.4, 278.4, 554.8, weight=96.0)
    g.hbar(182.0, 209.0, 363.3, weight=96.0)
    g.hbar(182.0, 375.7, 379.3, weight=96.0)
    g.diag(216.2, 556.6, 256.4, 525.8, weight=96.0)
    g.vbar(241.4, 171.7, 525.8, weight=96.0)
    g.hbar(73.0, 411.8, 144.4, weight=96.0)
    g.diag(486.2, 470.0, 360.9, 372.8, weight=84.0)
    g.vbar(472.0, 504.9, 746.5, weight=84.0)
    g.diag(467.9, 504.9, 268.0, -41.5, weight=84.0)
    g.hbar(626.3, 861.1, 617.7, weight=96.0)
    g.hbar(548.0, 783.9, 372.2, weight=96.0)
    g.hbar(738.0, 783.9, 383.8, weight=96.0)
    g.diag(661.0, 581.0, 701.6, 550.6, weight=96.0)
    g.vbar(697.2, 154.2, 550.6, weight=96.0)
    g.diag(692.7, 154.2, 675.2, 133.1, weight=96.0)
    g.hbar(468.8, 922.0, 113.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_74a7() -> Glyph:
    """璧 U+74A7 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni74A7", advance=1000, unicode=0x74A7, note="璧：自动生成")
    g.diag(318.6, 680.3, 322.9, 678.3, weight=48.0)
    g.hbar(322.9, 485.2, 686.2, weight=48.0)
    g.vbar(470.6, 615.1, 694.1, weight=48.0)
    g.hbar(436.2, 455.9, 610.7, weight=48.0)
    g.hbar(305.7, 482.6, 560.3, weight=48.0)
    g.vbar(256.3, 559.6, 696.1, weight=48.0)
    g.diag(251.4, 559.6, 114.0, 240.6, weight=48.0)
    g.diag(277.1, 453.1, 314.6, 282.1, weight=48.0)
    g.hbar(307.7, 476.8, 455.5, weight=48.0)
    g.diag(476.8, 460.0, 452.0, 386.9, weight=48.0)
    g.diag(452.0, 386.9, 428.3, 372.0, weight=48.0)
    g.hbar(332.4, 476.7, 332.0, weight=48.0)
    g.diag(639.7, 792.0, 725.7, 726.8, weight=48.0)
    g.hbar(580.4, 847.2, 662.6, weight=96.0)
    g.dot(608.1, 570.2, w=96.0, h=80.5, slant=-14.0)
    g.diag(729.7, 635.9, 753.8, 613.8, weight=96.0)
    g.diag(753.8, 613.8, 705.0, 517.3, weight=96.0)
    g.hbar(539.9, 871.0, 498.0, weight=64.0)
    g.hbar(550.8, 854.2, 376.0, weight=84.0)
    g.diag(667.4, 468.9, 694.1, 446.1, weight=96.0)
    g.vbar(691.6, 284.1, 446.1, weight=96.0)
    g.hbar(361.1, 679.3, 244.1, weight=92.0)
    g.hbar(357.1, 672.3, 102.8, weight=56.0)
    g.diag(489.5, 209.0, 517.2, 182.3, weight=96.0)
    g.vbar(515.2, 26.2, 182.3, weight=96.0)
    g.diag(513.3, 26.2, 498.4, 10.4, weight=96.0)
    g.hbar(211.9, 857.1, -26.2, weight=96.0)
    g.diag(705.9, 169.5, 806.7, 88.4, weight=76.0)
    return g
def g_cjk_unified_ideograph_74b0() -> Glyph:
    """環 U+74B0 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni74B0", advance=1000, unicode=0x74B0, note="環：自动生成")
    g.diag(177.0, 595.8, 165.3, 602.1, weight=96.0)
    g.hbar(165.3, 376.7, 635.4, weight=96.0)
    g.diag(210.6, 386.4, 196.3, 393.9, weight=96.0)
    g.hbar(196.3, 348.2, 416.6, weight=96.0)
    g.diag(214.5, 587.5, 241.0, 571.1, weight=96.0)
    g.vbar(248.3, 279.5, 571.1, weight=96.0)
    g.diag(255.5, 279.5, 233.4, 246.4, weight=96.0)
    g.hbar(78.0, 139.6, 160.1, weight=96.0)
    g.diag(139.6, 156.3, 427.0, 312.6, weight=96.0)
    g.vbar(434.0, 678.0, 686.6, weight=76.0)
    g.vbar(457.8, 543.0, 678.0, weight=76.0)
    g.hbar(455.2, 786.6, 702.2, weight=48.0)
    g.vbar(761.2, 592.8, 730.2, weight=48.0)
    g.hbar(705.3, 735.7, 598.7, weight=48.0)
    g.diag(538.6, 686.1, 555.9, 605.1, weight=64.0)
    g.diag(555.9, 605.1, 567.0, 597.0, weight=64.0)
    g.diag(626.7, 706.9, 648.5, 688.9, weight=64.0)
    g.diag(648.5, 688.9, 630.5, 616.9, weight=64.0)
    g.diag(630.5, 616.9, 618.2, 610.3, weight=64.0)
    g.hbar(497.8, 681.3, 579.0, weight=64.0)
    g.diag(681.3, 600.9, 694.0, 590.4, weight=64.0)
    g.hbar(350.9, 835.2, 472.6, weight=64.0)
    g.dot(461.2, 320.0, w=96.0, h=117.5, slant=-14.0)
    g.hbar(472.0, 711.4, 381.9, weight=48.0)
    g.diag(711.4, 403.2, 643.7, 334.7, weight=48.0)
    g.hbar(497.8, 719.3, 289.3, weight=48.0)
    g.diag(517.3, 267.2, 457.8, 188.0, weight=48.0)
    g.diag(457.8, 188.0, 259.0, 43.6, weight=48.0)
    g.vbar(518.8, -31.5, 173.2, weight=64.0)
    g.diag(529.5, -31.5, 690.3, 104.5, weight=64.0)
    g.diag(727.2, 298.3, 750.8, 260.6, weight=84.0)
    g.diag(750.8, 260.6, 663.7, 189.5, weight=84.0)
    g.hbar(653.2, 663.7, 190.5, weight=84.0)
    g.diag(553.9, 239.5, 947.0, 47.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_74bd() -> Glyph:
    """璽 U+74BD —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni74BD", advance=1000, unicode=0x74BD, note="璽：自动生成")
    g.hbar(333.0, 701.3, 745.5, weight=84.0)
    g.diag(265.4, 674.9, 283.4, 640.1, weight=48.0)
    g.diag(283.4, 640.1, 134.1, 519.2, weight=48.0)
    g.diag(743.4, 711.2, 874.7, 624.0, weight=84.0)
    g.diag(456.4, 704.3, 478.2, 589.5, weight=56.0)
    g.vbar(478.6, 299.8, 589.5, weight=56.0)
    g.vbar(265.4, 290.0, 585.8, weight=48.0)
    g.hbar(293.8, 460.0, 593.7, weight=64.0)
    g.hbar(460.0, 669.2, 553.5, weight=64.0)
    g.vbar(704.6, 268.2, 507.4, weight=64.0)
    g.hbar(650.4, 740.0, 282.5, weight=64.0)
    g.diag(407.4, 547.6, 417.1, 525.1, weight=48.0)
    g.diag(417.1, 525.1, 331.0, 440.8, weight=48.0)
    g.diag(324.2, 519.2, 427.0, 444.7, weight=48.0)
    g.diag(399.6, 418.3, 409.0, 398.4, weight=48.0)
    g.diag(409.0, 398.4, 367.2, 344.6, weight=48.0)
    g.diag(367.2, 344.6, 317.3, 306.6, weight=48.0)
    g.dot(369.2, 349.7, w=96.0, h=122.2, slant=-14.0)
    g.diag(622.9, 579.9, 628.5, 554.5, weight=48.0)
    g.diag(628.5, 554.5, 565.4, 485.2, weight=48.0)
    g.diag(565.4, 485.2, 528.9, 459.4, weight=48.0)
    g.diag(535.8, 542.7, 654.3, 452.6, weight=56.0)
    g.diag(611.2, 440.8, 620.5, 419.0, weight=48.0)
    g.diag(620.5, 419.0, 568.1, 355.3, weight=48.0)
    g.diag(568.1, 355.3, 529.9, 324.2, weight=48.0)
    g.diag(535.8, 413.4, 649.4, 329.1, weight=64.0)
    g.hbar(312.4, 616.1, 233.6, weight=96.0)
    g.hbar(324.2, 608.2, 111.7, weight=96.0)
    g.diag(447.6, 205.7, 473.1, 181.2, weight=96.0)
    g.vbar(471.6, 30.4, 181.2, weight=96.0)
    g.diag(470.1, 30.4, 454.5, 9.8, weight=96.0)
    g.hbar(125.3, 863.9, -25.9, weight=96.0)
    g.diag(670.9, 131.3, 751.3, 67.6, weight=48.0)
    return g
def g_cjk_unified_ideograph_74f6() -> Glyph:
    """瓶 U+74F6 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni74F6", advance=1000, unicode=0x74F6, note="瓶：自动生成")
    g.dot(234.2, 617.5, w=96.0, h=124.8, slant=-14.0)
    g.diag(426.8, 756.2, 456.9, 724.2, weight=96.0)
    g.diag(456.9, 724.2, 343.7, 544.0, weight=96.0)
    g.hbar(158.6, 483.3, 508.3, weight=96.0)
    g.hbar(70.0, 418.8, 328.1, weight=96.0)
    g.hbar(411.7, 418.8, 355.2, weight=96.0)
    g.diag(191.6, 442.3, 275.0, 383.0, weight=96.0)
    g.diag(275.0, 383.0, 68.0, -16.2, weight=96.0)
    g.diag(345.1, 479.1, 330.2, 488.8, weight=96.0)
    g.vbar(353.6, 1.8, 488.8, weight=96.0)
    g.hbar(504.5, 816.4, 609.7, weight=96.0)
    g.vbar(517.5, 73.9, 562.8, weight=48.0)
    g.hbar(501.6, 645.0, 104.6, weight=48.0)
    g.diag(581.4, 414.7, 728.8, 274.3, weight=48.0)
    g.diag(728.8, 274.3, 917.2, -52.9, weight=48.0)
    g.diag(917.2, -52.9, 947.0, 149.3, weight=48.0)
    g.diag(569.7, 304.3, 693.0, 243.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_7554() -> Glyph:
    """畔 U+7554 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7554", advance=1000, unicode=0x7554, note="畔：自动生成")
    g.diag(133.5, 575.3, 122.2, 561.8, weight=48.0)
    g.vbar(150.6, 274.3, 561.8, weight=48.0)
    g.hbar(138.4, 359.0, 531.2, weight=48.0)
    g.vbar(374.8, 295.5, 495.1, weight=48.0)
    g.hbar(390.6, 415.8, 291.5, weight=48.0)
    g.hbar(182.1, 383.1, 444.4, weight=96.0)
    g.diag(250.9, 558.9, 281.1, 530.4, weight=48.0)
    g.vbar(269.7, 335.3, 530.4, weight=48.0)
    g.diag(189.2, 290.6, 207.3, 306.6, weight=96.0)
    g.hbar(207.3, 364.7, 318.3, weight=96.0)
    g.hbar(455.2, 634.7, 563.9, weight=64.0)
    g.diag(793.6, 698.8, 821.2, 664.1, weight=56.0)
    g.diag(821.2, 664.1, 733.7, 578.0, weight=56.0)
    g.hbar(682.9, 733.7, 574.7, weight=56.0)
    g.hbar(459.9, 764.6, 462.7, weight=96.0)
    g.vbar(760.8, 470.4, 543.2, weight=96.0)
    g.hbar(427.6, 941.9, 310.7, weight=96.0)
    g.diag(614.3, 772.0, 647.2, 605.8, weight=56.0)
    g.vbar(651.9, -52.0, 605.8, weight=56.0)
    return g
def g_cjk_unified_ideograph_755c() -> Glyph:
    """畜 U+755C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni755C", advance=1000, unicode=0x755C, note="畜：自动生成")
    g.diag(468.3, 792.0, 555.4, 730.2, weight=48.0)
    g.diag(555.4, 730.2, 558.8, 717.7, weight=48.0)
    g.hbar(146.4, 883.6, 632.5, weight=96.0)
    g.diag(430.2, 613.9, 450.1, 581.2, weight=48.0)
    g.diag(450.1, 581.2, 348.1, 463.4, weight=48.0)
    g.hbar(348.1, 506.4, 470.1, weight=48.0)
    g.diag(618.8, 593.0, 561.5, 507.8, weight=48.0)
    g.diag(561.5, 507.8, 378.1, 339.1, weight=48.0)
    g.hbar(378.1, 641.9, 357.3, weight=48.0)
    g.diag(641.9, 375.5, 651.2, 367.3, weight=48.0)
    g.diag(619.8, 438.7, 699.8, 340.6, weight=48.0)
    g.diag(267.4, 246.3, 345.5, -15.6, weight=48.0)
    g.hbar(321.7, 473.7, 245.8, weight=48.0)
    g.hbar(473.7, 657.1, 210.4, weight=48.0)
    g.vbar(665.2, -28.2, 172.7, weight=48.0)
    g.vbar(672.8, -47.0, -28.2, weight=48.0)
    g.hbar(395.0, 630.2, 140.1, weight=84.0)
    g.diag(481.7, 228.2, 502.9, 212.3, weight=96.0)
    g.vbar(506.8, 84.6, 212.3, weight=96.0)
    g.diag(510.7, 84.6, 492.1, 58.7, weight=96.0)
    g.diag(365.5, 10.1, 379.4, 22.9, weight=84.0)
    g.hbar(379.4, 657.8, 35.1, weight=84.0)
    return g
def g_cjk_unified_ideograph_755d() -> Glyph:
    """畝 U+755D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni755D", advance=1000, unicode=0x755D, note="畝：自动生成")
    g.dot(299.8, 647.1, w=96.0, h=124.8, slant=-14.0)
    g.hbar(81.5, 447.0, 482.4, weight=96.0)
    g.diag(63.0, 320.6, 146.8, 32.1, weight=48.0)
    g.hbar(121.5, 221.6, 321.8, weight=48.0)
    g.diag(221.6, 323.9, 349.5, 261.8, weight=48.0)
    g.vbar(355.9, 94.2, 261.8, weight=48.0)
    g.hbar(342.7, 362.3, 90.9, weight=48.0)
    g.hbar(172.2, 334.9, 212.4, weight=96.0)
    g.diag(217.0, 309.9, 244.3, 288.4, weight=48.0)
    g.vbar(244.3, 129.6, 288.4, weight=48.0)
    g.diag(244.3, 129.6, 229.7, 110.1, weight=48.0)
    g.diag(165.3, 60.4, 175.7, 73.6, weight=96.0)
    g.hbar(175.7, 330.1, 94.3, weight=96.0)
    g.vbar(566.3, 622.2, 729.9, weight=48.0)
    g.diag(563.7, 622.2, 454.8, 385.9, weight=48.0)
    g.diag(528.9, 450.2, 574.6, 323.3, weight=48.0)
    g.diag(574.6, 323.3, 342.7, 8.7, weight=48.0)
    g.vbar(641.4, 200.4, 246.5, weight=96.0)
    g.diag(639.8, 200.4, 947.0, -4.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_7591() -> Glyph:
    """疑 U+7591 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7591", advance=1000, unicode=0x7591, note="疑：自动生成")
    g.diag(395.3, 635.8, 367.0, 661.1, weight=96.0)
    g.diag(367.0, 661.1, 225.7, 573.2, weight=96.0)
    g.diag(190.0, 720.0, 147.9, 773.6, weight=84.0)
    g.diag(147.9, 773.6, 248.4, 485.8, weight=84.0)
    g.hbar(248.4, 419.4, 487.9, weight=84.0)
    g.diag(419.4, 489.9, 388.0, 635.6, weight=84.0)
    g.diag(200.2, 467.1, 101.0, 219.2, weight=96.0)
    g.hbar(199.9, 407.1, 366.8, weight=84.0)
    g.diag(88.4, 237.8, 120.9, 180.4, weight=96.0)
    g.hbar(120.9, 437.5, 215.3, weight=96.0)
    g.diag(250.4, 334.8, 233.8, 211.1, weight=56.0)
    g.diag(233.8, 211.1, 83.8, -11.1, weight=56.0)
    g.dot(341.3, 120.1, w=96.0, h=124.8, slant=-14.0)
    g.hbar(449.3, 769.9, 646.7, weight=92.0)
    g.diag(769.9, 676.9, 652.8, 523.6, weight=92.0)
    g.hbar(646.3, 652.8, 523.6, weight=92.0)
    g.diag(562.9, 536.4, 625.4, 496.8, weight=48.0)
    g.diag(625.4, 496.8, 655.6, 435.5, weight=48.0)
    g.hbar(417.4, 851.4, 405.8, weight=64.0)
    g.diag(851.4, 433.2, 763.6, 279.7, weight=64.0)
    g.diag(601.6, 382.7, 631.9, 361.4, weight=96.0)
    g.vbar(628.3, 133.5, 361.4, weight=96.0)
    g.diag(624.7, 133.5, 643.3, 101.0, weight=96.0)
    g.hbar(662.1, 735.0, 247.9, weight=96.0)
    g.diag(735.0, 263.0, 771.5, 297.8, weight=96.0)
    g.diag(453.3, 258.3, 505.0, 233.3, weight=96.0)
    g.diag(505.0, 233.3, 405.9, 24.7, weight=96.0)
    g.diag(405.9, 24.7, 359.4, 56.6, weight=96.0)
    g.hbar(512.4, 927.0, 84.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_75be() -> Glyph:
    """疾 U+75BE —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni75BE", advance=1000, unicode=0x75BE, note="疾：自动生成")
    g.diag(472.6, 774.7, 566.1, 721.0, weight=96.0)
    g.diag(566.1, 721.0, 603.5, 636.1, weight=96.0)
    g.hbar(348.9, 776.9, 594.7, weight=96.0)
    g.diag(318.6, 580.1, 278.9, 407.5, weight=96.0)
    g.diag(278.9, 407.5, 121.6, -44.7, weight=96.0)
    g.dot(205.3, 465.3, w=96.0, h=124.8, slant=-14.0)
    g.hbar(53.0, 105.9, 206.9, weight=96.0)
    g.diag(105.9, 203.9, 250.9, 294.4, weight=96.0)
    g.diag(485.5, 537.0, 517.7, 467.3, weight=84.0)
    g.diag(517.7, 467.3, 431.2, 340.7, weight=84.0)
    g.hbar(326.0, 431.2, 334.5, weight=84.0)
    g.hbar(499.5, 746.1, 407.8, weight=96.0)
    g.hbar(291.3, 864.4, 228.8, weight=64.0)
    g.diag(539.1, 374.0, 516.0, 232.3, weight=48.0)
    g.diag(516.0, 232.3, 322.5, -36.7, weight=48.0)
    g.diag(588.7, 207.6, 937.0, -39.7, weight=48.0)
    return g
def g_cjk_unified_ideograph_75c7() -> Glyph:
    """症 U+75C7 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni75C7", advance=1000, unicode=0x75C7, note="症：自动生成")
    g.diag(510.6, 792.0, 603.8, 741.3, weight=84.0)
    g.diag(603.8, 741.3, 641.6, 645.5, weight=84.0)
    g.hbar(369.6, 814.0, 607.9, weight=96.0)
    g.diag(336.6, 592.2, 292.8, 417.3, weight=96.0)
    g.diag(292.8, 417.3, 131.7, -57.0, weight=96.0)
    g.dot(219.5, 474.1, w=96.0, h=124.8, slant=-14.0)
    g.hbar(60.2, 115.3, 204.9, weight=96.0)
    g.diag(115.3, 201.8, 266.3, 296.1, weight=96.0)
    g.hbar(516.3, 543.2, 407.5, weight=96.0)
    g.hbar(516.3, 790.2, 435.9, weight=96.0)
    g.diag(581.0, 397.5, 624.5, 364.6, weight=96.0)
    g.vbar(607.5, 47.2, 364.6, weight=96.0)
    g.diag(590.6, 47.2, 596.6, 52.7, weight=96.0)
    g.hbar(644.2, 815.0, 248.4, weight=96.0)
    g.diag(339.4, 283.5, 455.7, 228.8, weight=96.0)
    g.vbar(463.5, 47.6, 228.8, weight=96.0)
    g.diag(471.3, 47.6, 458.9, 38.3, weight=96.0)
    g.hbar(244.1, 500.5, 23.6, weight=96.0)
    g.hbar(500.5, 924.8, 20.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_75d5() -> Glyph:
    """痕 U+75D5 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni75D5", advance=1000, unicode=0x75D5, note="痕：自动生成")
    g.diag(474.5, 792.0, 538.5, 745.0, weight=96.0)
    g.diag(538.5, 745.0, 561.5, 687.3, weight=96.0)
    g.diag(347.7, 629.3, 373.9, 616.9, weight=96.0)
    g.hbar(373.9, 745.5, 646.5, weight=96.0)
    g.diag(312.9, 638.8, 71.5, -62.0, weight=96.0)
    g.diag(138.5, 523.0, 275.5, 411.3, weight=96.0)
    g.hbar(54.5, 107.7, 208.0, weight=96.0)
    g.diag(107.7, 206.0, 267.5, 309.0, weight=96.0)
    g.hbar(445.9, 687.1, 516.2, weight=48.0)
    g.vbar(662.3, 326.0, 529.7, weight=48.0)
    g.hbar(621.1, 637.5, 327.2, weight=48.0)
    g.hbar(467.4, 632.6, 406.4, weight=64.0)
    g.diag(478.5, 321.0, 487.5, 313.0, weight=48.0)
    g.hbar(487.5, 620.8, 325.9, weight=48.0)
    g.vbar(434.0, -7.8, 521.2, weight=48.0)
    g.hbar(422.3, 579.5, 27.1, weight=48.0)
    g.diag(680.0, 338.4, 735.6, 293.9, weight=96.0)
    g.diag(735.6, 293.9, 627.3, 194.9, weight=96.0)
    g.hbar(614.5, 627.3, 195.5, weight=96.0)
    g.diag(467.5, 313.0, 945.5, 21.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_75d8() -> Glyph:
    """痘 U+75D8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni75D8", advance=1000, unicode=0x75D8, note="痘：自动生成")
    g.diag(513.2, 792.0, 581.2, 755.5, weight=76.0)
    g.diag(581.2, 755.5, 619.9, 656.6, weight=76.0)
    g.diag(389.0, 610.6, 416.2, 596.4, weight=96.0)
    g.hbar(416.2, 805.1, 625.2, weight=96.0)
    g.diag(352.0, 621.0, 309.0, 439.7, weight=96.0)
    g.diag(309.0, 439.7, 120.8, -57.0, weight=96.0)
    g.diag(155.3, 546.5, 306.4, 445.1, weight=96.0)
    g.hbar(82.3, 132.8, 228.0, weight=96.0)
    g.diag(132.8, 224.0, 281.5, 306.9, weight=96.0)
    g.hbar(390.0, 687.6, 501.5, weight=96.0)
    g.diag(687.6, 506.6, 719.6, 435.9, weight=96.0)
    g.vbar(469.9, 211.2, 376.3, weight=76.0)
    g.hbar(467.4, 708.1, 384.3, weight=48.0)
    g.diag(708.1, 400.9, 743.8, 365.1, weight=48.0)
    g.diag(743.8, 365.1, 687.7, 282.7, weight=48.0)
    g.hbar(507.1, 723.4, 246.0, weight=48.0)
    g.vbar(724.0, 267.3, 290.4, weight=48.0)
    g.dot(478.9, 121.2, w=96.0, h=124.8, slant=-14.0)
    g.diag(680.8, 225.1, 705.4, 178.2, weight=96.0)
    g.diag(705.4, 178.2, 611.8, 56.4, weight=96.0)
    g.hbar(248.6, 902.7, 34.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_75e2() -> Glyph:
    """痢 U+75E2 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni75E2", advance=1000, unicode=0x75E2, note="痢：自动生成")
    g.diag(549.1, 792.0, 632.2, 748.0, weight=48.0)
    g.diag(632.2, 748.0, 669.8, 665.0, weight=48.0)
    g.hbar(398.1, 792.6, 643.6, weight=96.0)
    g.diag(792.6, 666.5, 814.6, 612.0, weight=96.0)
    g.diag(373.9, 627.7, 325.8, 438.8, weight=64.0)
    g.diag(325.8, 438.8, 162.2, -57.0, weight=64.0)
    g.dot(252.8, 474.5, w=96.0, h=124.8, slant=-14.0)
    g.hbar(118.3, 171.2, 248.8, weight=96.0)
    g.diag(171.2, 244.9, 303.6, 318.5, weight=96.0)
    g.diag(303.6, 318.5, 306.8, 334.8, weight=96.0)
    g.diag(676.6, 453.2, 600.0, 521.9, weight=96.0)
    g.diag(600.0, 521.9, 432.4, 438.2, weight=96.0)
    g.hbar(392.1, 432.4, 432.9, weight=96.0)
    g.hbar(378.0, 682.6, 340.5, weight=96.0)
    g.vbar(531.5, -44.3, 457.9, weight=48.0)
    g.diag(525.3, 311.2, 481.4, 248.1, weight=48.0)
    g.diag(481.4, 248.1, 331.2, 57.3, weight=48.0)
    g.diag(562.8, 257.6, 617.5, 215.6, weight=76.0)
    g.hbar(572.4, 617.5, 208.4, weight=76.0)
    g.hbar(677.7, 722.0, 390.7, weight=96.0)
    g.vbar(719.6, 199.0, 393.4, weight=96.0)
    g.hbar(663.6, 717.1, 190.9, weight=96.0)
    g.diag(812.9, 631.4, 888.3, 448.2, weight=96.0)
    g.diag(888.3, 448.2, 822.7, 11.7, weight=96.0)
    g.diag(822.7, 11.7, 720.8, 115.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_75f4() -> Glyph:
    """痴 U+75F4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni75F4", advance=1000, unicode=0x75F4, note="痴：自动生成")
    g.diag(499.1, 792.0, 593.6, 743.3, weight=84.0)
    g.diag(593.6, 743.3, 633.7, 647.4, weight=84.0)
    g.hbar(366.1, 808.9, 615.1, weight=96.0)
    g.diag(351.4, 598.1, 291.0, 402.9, weight=56.0)
    g.diag(291.0, 402.9, 76.7, -57.0, weight=56.0)
    g.diag(147.8, 511.7, 285.1, 417.0, weight=96.0)
    g.hbar(62.5, 265.9, 248.4, weight=96.0)
    g.diag(265.9, 287.6, 276.7, 304.5, weight=96.0)
    g.hbar(503.7, 522.5, 490.5, weight=48.0)
    g.diag(503.7, 489.7, 333.9, 310.6, weight=48.0)
    g.hbar(440.8, 589.5, 384.8, weight=48.0)
    g.diag(589.5, 405.9, 653.6, 366.7, weight=48.0)
    g.hbar(329.2, 659.9, 232.0, weight=96.0)
    g.diag(477.4, 352.0, 460.0, 218.9, weight=48.0)
    g.diag(460.0, 218.9, 291.0, -31.6, weight=48.0)
    g.diag(510.3, 129.9, 646.8, 29.4, weight=96.0)
    g.hbar(646.8, 700.2, 37.8, weight=96.0)
    g.diag(682.0, 338.5, 734.1, 80.1, weight=96.0)
    g.hbar(706.5, 921.6, 338.8, weight=48.0)
    g.diag(921.6, 357.2, 855.1, 163.9, weight=48.0)
    g.diag(751.0, 114.6, 766.6, 130.2, weight=96.0)
    g.hbar(766.6, 898.8, 139.6, weight=96.0)
    g.vbar(900.5, 148.9, 160.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_7642() -> Glyph:
    """療 U+7642 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7642", advance=1000, unicode=0x7642, note="療：自动生成")
    g.diag(477.0, 802.0, 586.0, 732.0, weight=48.0)
    g.hbar(333.0, 715.0, 656.5, weight=76.0)
    g.vbar(252.0, 430.6, 658.0, weight=56.0)
    g.diag(242.9, 430.6, 77.0, -45.0, weight=56.0)
    g.dot(152.5, 482.0, w=76.0, h=98.8, slant=-14.0)
    g.hbar(52.0, 103.2, 244.5, weight=76.0)
    g.diag(103.2, 242.9, 227.0, 322.0, weight=76.0)
    g.hbar(376.0, 711.0, 524.5, weight=48.0)
    g.diag(504.0, 616.0, 474.7, 498.9, weight=48.0)
    g.diag(474.7, 498.9, 301.0, 256.0, weight=48.0)
    g.diag(581.0, 502.0, 948.0, 331.0, weight=48.0)
    g.diag(355.0, 425.0, 402.0, 397.0, weight=76.0)
    g.diag(402.0, 397.0, 407.0, 380.0, weight=76.0)
    g.hbar(779.2, 813.0, 504.5, weight=76.0)
    g.diag(779.2, 508.9, 712.8, 446.8, weight=76.0)
    g.hbar(705.0, 712.8, 447.9, weight=76.0)
    g.vbar(418.0, 123.0, 298.0, weight=48.0)
    g.hbar(408.0, 697.4, 317.1, weight=48.0)
    g.vbar(669.0, 153.5, 326.3, weight=48.0)
    g.diag(640.6, 153.5, 643.0, 139.0, weight=48.0)
    g.diag(458.0, 215.0, 463.7, 225.3, weight=56.0)
    g.hbar(463.7, 588.0, 233.7, weight=56.0)
    g.diag(467.0, 145.0, 475.7, 154.8, weight=56.0)
    g.hbar(475.7, 616.0, 165.9, weight=56.0)
    g.vbar(516.5, -0.6, 145.0, weight=76.0)
    g.hbar(435.0, 511.9, -10.3, weight=76.0)
    g.diag(370.0, 95.0, 300.0, -33.0, weight=76.0)
    g.diag(658.0, 85.0, 786.0, -50.0, weight=76.0)
    return g
def g_cjk_unified_ideograph_7652() -> Glyph:
    """癒 U+7652 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7652", advance=1000, unicode=0x7652, note="癒：自动生成")
    g.diag(490.8, 792.0, 587.0, 723.9, weight=48.0)
    g.diag(357.5, 643.2, 371.1, 631.0, weight=64.0)
    g.hbar(371.1, 742.6, 660.0, weight=64.0)
    g.vbar(273.4, 443.1, 670.4, weight=76.0)
    g.diag(266.2, 443.1, 112.5, -24.9, weight=76.0)
    g.dot(168.4, 488.1, w=96.0, h=108.8, slant=-14.0)
    g.hbar(69.7, 119.4, 259.5, weight=96.0)
    g.diag(119.4, 259.1, 260.3, 369.0, weight=96.0)
    g.diag(531.6, 627.6, 497.0, 549.0, weight=48.0)
    g.diag(497.0, 549.0, 355.6, 379.7, weight=48.0)
    g.hbar(575.4, 670.8, 558.1, weight=48.0)
    g.hbar(670.8, 930.3, 496.3, weight=48.0)
    g.hbar(496.6, 649.3, 468.2, weight=48.0)
    g.hbar(388.6, 407.6, 376.0, weight=48.0)
    g.vbar(395.7, 146.3, 372.4, weight=48.0)
    g.diag(426.6, 373.8, 509.2, 312.5, weight=48.0)
    g.vbar(511.4, 132.4, 312.5, weight=48.0)
    g.hbar(450.9, 513.7, 144.2, weight=48.0)
    g.dot(454.3, 296.5, w=48.0, h=62.4, slant=-14.0)
    g.diag(418.8, 218.2, 425.7, 229.7, weight=56.0)
    g.hbar(425.7, 487.8, 230.7, weight=56.0)
    g.diag(592.9, 375.8, 611.4, 351.5, weight=48.0)
    g.vbar(609.9, 217.2, 351.5, weight=48.0)
    g.diag(683.3, 435.1, 732.5, 401.7, weight=92.0)
    g.diag(732.5, 401.7, 696.2, 165.9, weight=92.0)
    g.diag(696.2, 165.9, 640.5, 192.9, weight=92.0)
    g.dot(308.4, 25.7, w=96.0, h=124.8, slant=14.0)
    g.hbar(405.2, 812.9, 7.5, weight=96.0)
    g.diag(812.9, -72.0, 720.9, 57.6, weight=96.0)
    g.diag(720.9, 57.6, 710.5, 69.4, weight=96.0)
    g.dot(607.9, 77.2, w=64.0, h=83.2, slant=-14.0)
    g.dot(834.1, 123.9, w=96.0, h=124.8, slant=-14.0)
    return g
def g_cjk_unified_ideograph_7656() -> Glyph:
    """癖 U+7656 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7656", advance=1000, unicode=0x7656, note="癖：自动生成")
    g.diag(499.8, 792.0, 573.9, 751.7, weight=56.0)
    g.diag(573.9, 751.7, 600.6, 678.0, weight=56.0)
    g.hbar(339.7, 710.4, 653.5, weight=96.0)
    g.diag(710.4, 672.4, 702.7, 614.8, weight=96.0)
    g.diag(315.0, 641.3, 122.9, 46.4, weight=64.0)
    g.dot(206.1, 509.0, w=96.0, h=124.8, slant=-14.0)
    g.hbar(96.4, 141.2, 299.4, weight=96.0)
    g.diag(141.2, 296.3, 246.9, 357.6, weight=96.0)
    g.diag(246.9, 357.6, 254.6, 373.0, weight=96.0)
    g.hbar(429.4, 550.3, 509.0, weight=96.0)
    g.diag(550.3, 513.2, 502.6, 429.7, weight=96.0)
    g.dot(475.0, 390.2, w=96.0, h=124.8, slant=-14.0)
    g.diag(411.0, 510.4, 383.1, 410.6, weight=48.0)
    g.diag(383.1, 410.6, 257.4, 98.5, weight=48.0)
    g.vbar(407.5, 134.4, 275.1, weight=48.0)
    g.diag(410.2, 275.1, 415.6, 272.6, weight=64.0)
    g.hbar(415.6, 526.8, 279.7, weight=64.0)
    g.vbar(515.0, 208.2, 286.7, weight=64.0)
    g.diag(503.3, 208.2, 485.2, 195.5, weight=64.0)
    g.dot(477.4, 164.3, w=96.0, h=97.1, slant=-14.0)
    g.dot(674.5, 581.6, w=96.0, h=108.0, slant=-14.0)
    g.hbar(607.1, 776.1, 493.4, weight=96.0)
    g.vbar(777.4, 492.0, 518.8, weight=96.0)
    g.dot(632.0, 406.8, w=76.0, h=98.8, slant=-14.0)
    g.diag(736.1, 487.1, 756.4, 457.5, weight=48.0)
    g.diag(756.4, 457.5, 703.8, 354.7, weight=48.0)
    g.hbar(546.0, 851.2, 332.9, weight=96.0)
    g.vbar(850.2, 259.0, 360.8, weight=96.0)
    g.hbar(562.0, 809.5, 211.0, weight=96.0)
    g.diag(809.5, 232.9, 833.7, 319.0, weight=96.0)
    g.diag(661.8, 308.0, 693.4, 285.7, weight=96.0)
    g.vbar(690.9, -57.0, 285.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_76e3() -> Glyph:
    """監 U+76E3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni76E3", advance=1000, unicode=0x76E3, note="監：自动生成")
    g.diag(226.9, 696.4, 241.4, 685.5, weight=96.0)
    g.hbar(241.4, 416.8, 705.3, weight=96.0)
    g.diag(416.8, 725.1, 400.0, 683.0, weight=96.0)
    g.diag(349.1, 679.7, 371.7, 658.3, weight=96.0)
    g.diag(371.7, 658.3, 341.8, 593.0, weight=96.0)
    g.hbar(220.5, 465.7, 554.7, weight=48.0)
    g.diag(465.7, 572.9, 403.4, 472.8, weight=48.0)
    g.hbar(216.6, 434.4, 450.8, weight=48.0)
    g.diag(342.9, 428.9, 365.1, 398.5, weight=48.0)
    g.diag(365.1, 398.5, 337.5, 324.3, weight=48.0)
    g.vbar(203.9, 581.5, 702.2, weight=48.0)
    g.diag(199.1, 581.5, 274.5, 387.2, weight=48.0)
    g.hbar(274.5, 492.2, 353.8, weight=48.0)
    g.diag(608.1, 776.8, 652.7, 735.0, weight=96.0)
    g.diag(652.7, 735.0, 480.3, 524.9, weight=96.0)
    g.hbar(632.1, 852.5, 630.6, weight=96.0)
    g.diag(576.6, 522.3, 738.6, 363.2, weight=96.0)
    g.diag(251.7, 191.7, 322.8, 2.8, weight=48.0)
    g.hbar(264.8, 660.2, 211.6, weight=48.0)
    g.diag(660.2, 235.0, 694.3, 189.5, weight=48.0)
    g.diag(694.3, 189.5, 654.6, 66.3, weight=48.0)
    g.diag(654.6, 66.3, 615.4, 23.5, weight=48.0)
    g.diag(393.0, 172.1, 400.3, 166.3, weight=84.0)
    g.diag(400.3, 166.3, 426.4, 15.4, weight=84.0)
    g.diag(503.7, 193.0, 537.9, 166.5, weight=76.0)
    g.diag(537.9, 166.5, 493.2, 18.6, weight=76.0)
    g.hbar(88.0, 912.0, -15.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_76e4() -> Glyph:
    """盤 U+76E4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni76E4", advance=1000, unicode=0x76E4, note="盤：自动生成")
    g.diag(344.2, 781.7, 366.4, 759.5, weight=48.0)
    g.diag(366.4, 759.5, 308.2, 636.5, weight=48.0)
    g.diag(308.2, 636.5, 295.8, 629.1, weight=48.0)
    g.vbar(245.6, 506.1, 627.2, weight=48.0)
    g.diag(249.4, 506.1, 153.6, 211.0, weight=48.0)
    g.hbar(295.8, 309.1, 614.4, weight=48.0)
    g.hbar(309.1, 402.5, 627.1, weight=48.0)
    g.diag(402.5, 642.2, 423.3, 510.9, weight=48.0)
    g.vbar(422.3, 266.4, 510.9, weight=48.0)
    g.hbar(345.1, 421.3, 282.3, weight=48.0)
    g.dot(345.1, 541.9, w=48.0, h=62.4, slant=-14.0)
    g.hbar(73.0, 121.4, 413.9, weight=96.0)
    g.hbar(121.4, 486.4, 450.8, weight=96.0)
    g.dot(345.1, 385.0, w=48.0, h=62.4, slant=-14.0)
    g.diag(547.1, 689.8, 582.3, 657.2, weight=64.0)
    g.vbar(548.1, 473.6, 657.2, weight=64.0)
    g.diag(597.3, 695.5, 604.8, 689.9, weight=96.0)
    g.hbar(604.8, 707.3, 697.2, weight=96.0)
    g.vbar(694.6, 561.9, 704.6, weight=96.0)
    g.hbar(682.0, 849.5, 553.8, weight=96.0)
    g.diag(565.1, 458.4, 651.3, 406.9, weight=48.0)
    g.diag(651.3, 406.9, 519.6, 270.7, weight=48.0)
    g.hbar(537.6, 932.0, 346.6, weight=96.0)
    g.diag(261.7, 185.4, 341.1, 9.1, weight=48.0)
    g.diag(341.1, 9.1, 343.2, 7.1, weight=48.0)
    g.hbar(300.5, 708.5, 191.2, weight=48.0)
    g.diag(708.5, 195.2, 660.8, 54.5, weight=48.0)
    g.diag(660.8, 54.5, 628.6, 33.7, weight=48.0)
    g.diag(396.3, 164.5, 440.9, 12.8, weight=84.0)
    g.diag(517.7, 180.6, 547.1, 147.4, weight=76.0)
    g.diag(547.1, 147.4, 516.5, 29.3, weight=76.0)
    g.diag(516.5, 29.3, 503.4, 23.2, weight=76.0)
    g.hbar(119.5, 886.5, -17.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_7720() -> Glyph:
    """眠 U+7720 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7720", advance=1000, unicode=0x7720, note="眠：自动生成")
    g.vbar(123.0, 264.3, 623.8, weight=84.0)
    g.vbar(133.7, 74.1, 264.3, weight=84.0)
    g.diag(151.1, 614.6, 282.4, 463.4, weight=96.0)
    g.diag(282.4, 463.4, 338.5, 130.7, weight=96.0)
    g.diag(338.5, 130.7, 296.0, 105.4, weight=96.0)
    g.dot(221.3, 439.6, w=96.0, h=124.8, slant=-14.0)
    g.dot(222.4, 295.3, w=96.0, h=124.8, slant=-14.0)
    g.diag(157.3, 103.0, 167.0, 114.6, weight=96.0)
    g.hbar(167.0, 282.4, 125.2, weight=96.0)
    g.hbar(464.0, 722.0, 668.3, weight=48.0)
    g.diag(722.0, 697.5, 764.2, 663.1, weight=48.0)
    g.diag(764.2, 663.1, 704.1, 563.7, weight=48.0)
    g.hbar(479.5, 746.4, 520.9, weight=48.0)
    g.vbar(744.8, 551.9, 578.6, weight=48.0)
    g.vbar(423.6, 6.6, 663.9, weight=96.0)
    g.diag(402.3, 6.6, 673.7, 180.0, weight=96.0)
    g.hbar(490.4, 821.4, 340.7, weight=96.0)
    g.diag(597.3, 504.6, 639.7, 405.7, weight=96.0)
    g.diag(639.7, 405.7, 876.2, -44.7, weight=96.0)
    g.diag(876.2, -44.7, 947.0, 149.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_773a() -> Glyph:
    """眺 U+773A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni773A", advance=1000, unicode=0x773A, note="眺：自动生成")
    g.vbar(117.5, 63.6, 612.9, weight=96.0)
    g.diag(144.4, 600.0, 270.1, 428.5, weight=76.0)
    g.vbar(283.6, 99.9, 428.5, weight=76.0)
    g.hbar(270.3, 297.1, 97.1, weight=76.0)
    g.diag(154.7, 415.5, 175.6, 435.3, weight=96.0)
    g.hbar(175.6, 269.6, 436.3, weight=96.0)
    g.diag(151.6, 268.5, 173.5, 287.2, weight=96.0)
    g.hbar(173.5, 269.6, 287.2, weight=96.0)
    g.diag(146.4, 94.4, 159.1, 109.4, weight=96.0)
    g.hbar(159.1, 261.4, 113.5, weight=96.0)
    g.vbar(488.7, 433.0, 660.4, weight=96.0)
    g.diag(495.3, 433.0, 401.9, -16.9, weight=96.0)
    g.hbar(308.2, 401.9, -3.8, weight=96.0)
    g.hbar(327.2, 441.4, 448.3, weight=48.0)
    g.diag(441.4, 426.9, 458.1, 400.9, weight=48.0)
    g.hbar(340.3, 363.5, 216.5, weight=96.0)
    g.diag(363.5, 211.4, 495.6, 301.8, weight=96.0)
    g.diag(625.9, 752.2, 695.5, 454.2, weight=48.0)
    g.diag(695.5, 454.2, 837.8, 143.6, weight=48.0)
    g.hbar(837.8, 947.0, 161.8, weight=48.0)
    g.diag(704.8, 591.4, 812.5, 542.6, weight=96.0)
    g.diag(812.5, 542.6, 690.6, 425.9, weight=96.0)
    g.vbar(690.0, 413.4, 425.9, weight=96.0)
    g.diag(672.9, 336.9, 843.8, 194.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_773c() -> Glyph:
    """眼 U+773C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni773C", advance=1000, unicode=0x773C, note="眼：自动生成")
    g.vbar(125.9, 88.1, 631.1, weight=84.0)
    g.hbar(140.2, 257.3, 632.5, weight=48.0)
    g.vbar(272.3, 462.2, 646.8, weight=48.0)
    g.vbar(289.1, 77.3, 462.2, weight=48.0)
    g.dot(204.7, 443.8, w=96.0, h=107.6, slant=-14.0)
    g.dot(204.6, 298.7, w=96.0, h=111.6, slant=-14.0)
    g.diag(152.8, 115.5, 161.1, 126.6, weight=96.0)
    g.hbar(161.1, 254.5, 135.6, weight=96.0)
    g.hbar(478.7, 697.7, 657.6, weight=96.0)
    g.vbar(674.7, 432.1, 665.2, weight=96.0)
    g.hbar(635.5, 651.6, 430.9, weight=96.0)
    g.diag(477.9, 516.9, 494.8, 535.3, weight=92.0)
    g.hbar(494.8, 634.7, 537.8, weight=92.0)
    g.hbar(482.7, 606.3, 429.6, weight=48.0)
    g.diag(606.3, 440.2, 616.3, 431.5, weight=48.0)
    g.diag(406.4, 670.6, 437.3, 490.0, weight=48.0)
    g.vbar(432.4, 2.4, 490.0, weight=48.0)
    g.diag(427.5, 2.4, 602.2, 119.4, weight=48.0)
    g.diag(683.3, 414.2, 739.2, 360.3, weight=96.0)
    g.diag(739.2, 360.3, 637.4, 270.2, weight=96.0)
    g.hbar(629.6, 637.4, 271.2, weight=96.0)
    g.diag(480.8, 419.0, 937.0, 83.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_7761() -> Glyph:
    """睡 U+7761 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7761", advance=1000, unicode=0x7761, note="睡：自动生成")
    g.vbar(108.2, 59.1, 625.4, weight=96.0)
    g.diag(145.9, 613.0, 261.9, 435.0, weight=96.0)
    g.vbar(266.6, 86.0, 435.0, weight=96.0)
    g.hbar(268.6, 271.4, 85.7, weight=96.0)
    g.diag(150.0, 437.2, 158.8, 453.5, weight=96.0)
    g.hbar(158.8, 258.9, 456.8, weight=96.0)
    g.dot(200.0, 309.6, w=96.0, h=122.2, slant=-14.0)
    g.diag(132.5, 87.7, 147.0, 99.3, weight=96.0)
    g.hbar(147.0, 256.3, 108.7, weight=96.0)
    g.hbar(689.4, 742.6, 729.9, weight=96.0)
    g.hbar(444.6, 689.4, 684.0, weight=96.0)
    g.vbar(438.8, 556.2, 632.9, weight=96.0)
    g.diag(419.6, 462.4, 458.8, 508.6, weight=96.0)
    g.hbar(458.8, 719.0, 536.6, weight=96.0)
    g.diag(719.0, 564.7, 756.0, 532.8, weight=96.0)
    g.diag(562.7, 649.2, 587.1, 490.5, weight=96.0)
    g.vbar(587.5, 59.5, 490.5, weight=96.0)
    g.diag(588.0, 59.5, 577.1, 47.4, weight=96.0)
    g.hbar(337.0, 937.0, 352.4, weight=96.0)
    g.diag(423.4, 480.3, 487.1, 200.1, weight=96.0)
    g.diag(743.3, 530.2, 777.1, 460.2, weight=96.0)
    g.diag(777.1, 460.2, 720.1, 234.6, weight=96.0)
    g.hbar(338.1, 860.5, 176.6, weight=96.0)
    g.hbar(328.1, 804.6, 25.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_7766() -> Glyph:
    """睦 U+7766 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7766", advance=1000, unicode=0x7766, note="睦：自动生成")
    g.vbar(131.5, 41.4, 608.3, weight=96.0)
    g.hbar(152.2, 263.0, 609.3, weight=48.0)
    g.vbar(279.8, 409.5, 630.6, weight=48.0)
    g.vbar(299.0, 19.6, 409.5, weight=48.0)
    g.diag(166.4, 410.6, 189.1, 432.3, weight=96.0)
    g.hbar(189.1, 272.4, 434.3, weight=96.0)
    g.diag(164.3, 257.9, 187.0, 277.5, weight=96.0)
    g.hbar(187.0, 272.4, 278.5, weight=96.0)
    g.diag(158.1, 68.1, 169.2, 80.1, weight=96.0)
    g.hbar(169.2, 264.0, 85.7, weight=96.0)
    g.hbar(546.9, 582.4, 584.3, weight=96.0)
    g.hbar(546.9, 781.3, 605.4, weight=96.0)
    g.diag(584.2, 782.0, 627.5, 743.8, weight=96.0)
    g.vbar(622.4, 499.3, 743.8, weight=96.0)
    g.diag(617.2, 499.3, 600.7, 473.5, weight=96.0)
    g.hbar(344.4, 897.8, 445.7, weight=84.0)
    g.diag(495.5, 388.1, 517.0, 334.1, weight=96.0)
    g.diag(517.0, 334.1, 349.2, 216.6, weight=96.0)
    g.diag(690.1, 438.2, 852.4, 273.4, weight=64.0)
    g.diag(413.3, 189.5, 522.4, 135.7, weight=96.0)
    g.hbar(522.4, 827.9, 189.8, weight=96.0)
    g.diag(546.7, 321.2, 623.4, 264.1, weight=96.0)
    g.vbar(618.8, 40.2, 264.1, weight=96.0)
    g.diag(614.1, 40.2, 597.6, 16.5, weight=96.0)
    g.hbar(333.3, 923.6, -4.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_77ac() -> Glyph:
    """瞬 U+77AC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni77AC", advance=1000, unicode=0x77AC, note="瞬：自动生成")
    g.vbar(149.2, 511.8, 657.2, weight=56.0)
    g.vbar(143.8, 126.4, 511.8, weight=56.0)
    g.diag(161.2, 644.7, 278.7, 480.4, weight=48.0)
    g.vbar(308.7, 164.7, 480.4, weight=48.0)
    g.hbar(274.1, 338.7, 153.6, weight=48.0)
    g.dot(225.3, 478.5, w=96.0, h=101.3, slant=-14.0)
    g.diag(171.2, 333.0, 182.4, 349.2, weight=96.0)
    g.hbar(182.4, 276.6, 352.4, weight=96.0)
    g.hbar(156.9, 187.7, 146.7, weight=96.0)
    g.hbar(187.7, 267.5, 152.6, weight=96.0)
    g.hbar(682.6, 757.7, 765.6, weight=96.0)
    g.diag(682.6, 781.5, 472.5, 666.1, weight=96.0)
    g.diag(473.5, 668.0, 533.0, 520.4, weight=48.0)
    g.diag(568.1, 689.0, 664.6, 597.8, weight=64.0)
    g.diag(764.2, 738.8, 793.1, 684.2, weight=96.0)
    g.diag(793.1, 684.2, 689.4, 588.9, weight=96.0)
    g.vbar(689.0, 574.7, 588.9, weight=96.0)
    g.diag(427.5, 507.1, 380.6, 407.4, weight=48.0)
    g.diag(380.6, 407.4, 333.8, 380.2, weight=48.0)
    g.diag(442.6, 495.3, 448.9, 490.2, weight=84.0)
    g.hbar(448.9, 884.6, 518.3, weight=84.0)
    g.diag(884.6, 546.4, 774.5, 422.9, weight=84.0)
    g.diag(471.5, 469.1, 493.7, 393.9, weight=48.0)
    g.diag(493.7, 393.9, 335.9, 231.4, weight=48.0)
    g.diag(467.6, 324.2, 492.9, 234.6, weight=48.0)
    g.diag(492.9, 234.6, 322.2, -15.0, weight=48.0)
    g.dot(448.6, 232.9, w=92.0, h=78.2, slant=-14.0)
    g.hbar(621.8, 855.9, 324.3, weight=48.0)
    g.vbar(611.0, 154.4, 291.2, weight=96.0)
    g.hbar(602.0, 907.9, 163.6, weight=96.0)
    g.vbar(755.3, -67.0, 440.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_77ad() -> Glyph:
    """瞭 U+77AD —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni77AD", advance=1000, unicode=0x77AD, note="瞭：自动生成")
    g.diag(121.8, 632.9, 54.6, 569.6, weight=56.0)
    g.diag(54.6, 569.6, 120.2, 289.5, weight=56.0)
    g.vbar(125.8, 121.0, 289.5, weight=56.0)
    g.hbar(131.0, 234.2, 632.4, weight=48.0)
    g.vbar(246.9, 435.4, 643.6, weight=48.0)
    g.vbar(260.7, 88.5, 435.4, weight=48.0)
    g.diag(151.0, 454.1, 156.8, 466.9, weight=96.0)
    g.hbar(156.8, 232.9, 468.0, weight=96.0)
    g.diag(151.0, 315.0, 161.5, 330.8, weight=96.0)
    g.hbar(161.5, 232.9, 330.0, weight=96.0)
    g.diag(144.4, 139.3, 160.9, 157.8, weight=96.0)
    g.hbar(160.9, 228.1, 157.5, weight=96.0)
    g.hbar(412.2, 724.3, 648.7, weight=48.0)
    g.diag(506.2, 783.1, 474.5, 609.6, weight=48.0)
    g.diag(474.5, 609.6, 290.5, 311.3, weight=48.0)
    g.diag(551.6, 616.2, 947.0, 413.7, weight=48.0)
    g.diag(296.9, 548.1, 437.3, 484.0, weight=64.0)
    g.diag(747.7, 645.6, 758.1, 596.8, weight=92.0)
    g.diag(758.1, 596.8, 693.1, 535.6, weight=92.0)
    g.hbar(683.8, 693.1, 537.2, weight=92.0)
    g.vbar(431.2, 357.3, 375.6, weight=48.0)
    g.vbar(444.4, 196.4, 357.3, weight=48.0)
    g.diag(453.6, 380.8, 455.9, 378.3, weight=84.0)
    g.hbar(455.9, 690.0, 385.5, weight=84.0)
    g.vbar(661.2, 216.2, 392.7, weight=84.0)
    g.diag(463.3, 287.1, 481.3, 303.5, weight=56.0)
    g.hbar(481.3, 640.1, 300.2, weight=56.0)
    g.hbar(474.3, 615.7, 222.7, weight=64.0)
    g.diag(526.0, 210.7, 562.9, 175.0, weight=56.0)
    g.vbar(550.2, -42.7, 175.0, weight=56.0)
    g.diag(537.5, -42.7, 457.4, -5.5, weight=56.0)
    g.diag(433.1, 163.9, 355.5, 27.7, weight=96.0)
    g.hbar(355.5, 419.2, 13.4, weight=96.0)
    g.diag(657.2, 169.8, 796.6, -0.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_77b3() -> Glyph:
    """瞳 U+77B3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni77B3", advance=1000, unicode=0x77B3, note="瞳：自动生成")
    g.vbar(131.4, 107.7, 599.5, weight=64.0)
    g.diag(122.8, 107.7, 152.8, 60.3, weight=64.0)
    g.diag(155.1, 585.9, 274.5, 401.6, weight=48.0)
    g.vbar(290.2, 42.1, 401.6, weight=48.0)
    g.diag(175.5, 419.8, 184.2, 434.6, weight=96.0)
    g.hbar(184.2, 274.1, 437.5, weight=96.0)
    g.diag(175.5, 287.5, 186.3, 301.8, weight=96.0)
    g.hbar(186.3, 275.6, 302.0, weight=96.0)
    g.diag(166.8, 81.7, 183.3, 99.1, weight=96.0)
    g.hbar(183.3, 269.0, 101.8, weight=96.0)
    g.diag(539.8, 787.0, 611.3, 749.3, weight=56.0)
    g.diag(611.3, 749.3, 643.4, 672.7, weight=56.0)
    g.hbar(471.5, 701.5, 639.1, weight=96.0)
    g.vbar(705.4, 627.1, 662.8, weight=96.0)
    g.dot(499.5, 553.5, w=96.0, h=86.3, slant=-14.0)
    g.diag(658.6, 627.6, 681.1, 601.1, weight=96.0)
    g.diag(681.1, 601.1, 630.6, 511.6, weight=96.0)
    g.hbar(338.0, 895.3, 481.6, weight=64.0)
    g.vbar(432.6, 371.7, 383.7, weight=48.0)
    g.vbar(456.0, 181.6, 371.7, weight=48.0)
    g.hbar(445.4, 785.4, 397.1, weight=48.0)
    g.vbar(752.0, 218.7, 416.2, weight=48.0)
    g.hbar(696.2, 718.7, 219.6, weight=48.0)
    g.hbar(483.6, 634.4, 294.0, weight=64.0)
    g.diag(634.4, 309.6, 678.5, 259.6, weight=64.0)
    g.hbar(495.3, 693.3, 211.6, weight=64.0)
    g.diag(561.0, 377.3, 590.5, 358.0, weight=96.0)
    g.vbar(588.0, 20.0, 358.0, weight=96.0)
    g.diag(585.6, 20.0, 571.7, 1.5, weight=96.0)
    g.diag(468.9, 144.4, 484.6, 84.2, weight=96.0)
    g.hbar(484.6, 711.4, 122.1, weight=96.0)
    g.diag(328.9, 11.2, 405.1, -36.3, weight=96.0)
    g.hbar(405.1, 865.4, -31.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_785d() -> Glyph:
    """硝 U+785D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni785D", advance=1000, unicode=0x785D, note="硝：自动生成")
    g.hbar(219.4, 255.9, 580.6, weight=96.0)
    g.hbar(219.4, 496.3, 612.6, weight=96.0)
    g.diag(291.1, 577.8, 266.6, 445.1, weight=48.0)
    g.diag(266.6, 445.1, 67.1, 114.2, weight=48.0)
    g.diag(235.0, 356.0, 284.8, 98.1, weight=48.0)
    g.hbar(282.7, 443.8, 366.4, weight=96.0)
    g.diag(443.8, 384.7, 418.9, 260.1, weight=96.0)
    g.diag(418.9, 260.1, 398.5, 242.9, weight=96.0)
    g.diag(303.0, 176.4, 319.3, 193.8, weight=96.0)
    g.hbar(319.3, 433.6, 206.2, weight=96.0)
    g.diag(433.6, 218.6, 442.1, 229.4, weight=96.0)
    g.diag(672.0, 777.0, 702.8, 653.2, weight=48.0)
    g.vbar(698.4, 475.4, 653.2, weight=48.0)
    g.diag(515.7, 641.1, 679.2, 554.1, weight=84.0)
    g.diag(893.9, 748.0, 927.6, 700.7, weight=64.0)
    g.diag(927.6, 700.7, 739.3, 582.4, weight=64.0)
    g.diag(601.7, 459.1, 582.1, 327.6, weight=48.0)
    g.vbar(561.1, -49.9, 327.6, weight=48.0)
    g.hbar(603.7, 813.2, 467.0, weight=48.0)
    g.vbar(830.4, 305.6, 486.0, weight=48.0)
    g.vbar(869.8, -65.7, 305.6, weight=48.0)
    g.hbar(720.2, 892.0, -38.4, weight=48.0)
    g.hbar(616.2, 818.0, 301.4, weight=96.0)
    g.diag(607.6, 163.6, 623.2, 179.2, weight=96.0)
    g.hbar(623.2, 824.2, 185.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_786b() -> Glyph:
    """硫 U+786B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni786B", advance=1000, unicode=0x786B, note="硫：自动生成")
    g.hbar(206.7, 410.1, 582.4, weight=96.0)
    g.diag(410.1, 612.3, 456.3, 587.2, weight=96.0)
    g.diag(240.8, 544.6, 214.2, 408.6, weight=48.0)
    g.diag(214.2, 408.6, 58.0, 134.4, weight=48.0)
    g.vbar(229.3, 161.5, 348.8, weight=48.0)
    g.hbar(237.9, 408.0, 355.6, weight=48.0)
    g.diag(408.0, 369.0, 350.7, 231.7, weight=48.0)
    g.diag(267.0, 179.5, 280.6, 195.1, weight=96.0)
    g.hbar(280.6, 393.0, 209.0, weight=96.0)
    g.diag(576.1, 747.6, 660.5, 690.7, weight=96.0)
    g.diag(660.5, 690.7, 690.4, 617.0, weight=96.0)
    g.hbar(453.5, 601.9, 584.1, weight=48.0)
    g.hbar(601.9, 833.2, 585.7, weight=48.0)
    g.diag(561.8, 531.0, 594.7, 492.4, weight=48.0)
    g.diag(594.7, 492.4, 514.3, 342.7, weight=48.0)
    g.hbar(514.3, 757.7, 371.9, weight=48.0)
    g.diag(713.5, 468.0, 795.2, 388.0, weight=48.0)
    g.hbar(765.0, 795.2, 384.6, weight=48.0)
    g.hbar(434.7, 540.1, 233.2, weight=96.0)
    g.diag(540.1, 237.3, 358.3, -22.6, weight=96.0)
    g.diag(586.9, 316.7, 717.2, 60.6, weight=96.0)
    g.diag(710.6, 359.0, 948.3, -29.9, weight=76.0)
    g.vbar(946.7, -29.9, 138.3, weight=76.0)
    return g
def g_cjk_unified_ideograph_7891() -> Glyph:
    """碑 U+7891 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7891", advance=1000, unicode=0x7891, note="碑：自动生成")
    g.diag(239.9, 579.9, 223.2, 608.4, weight=96.0)
    g.hbar(223.2, 426.0, 629.3, weight=96.0)
    g.diag(310.9, 591.3, 312.5, 592.4, weight=96.0)
    g.diag(312.5, 592.4, 62.5, 223.2, weight=96.0)
    g.diag(189.5, 443.1, 249.4, 232.4, weight=96.0)
    g.hbar(241.2, 391.6, 436.5, weight=48.0)
    g.vbar(380.2, 342.8, 448.4, weight=48.0)
    g.diag(368.9, 342.8, 347.6, 319.3, weight=48.0)
    g.diag(263.1, 268.2, 277.1, 285.3, weight=96.0)
    g.hbar(277.1, 379.5, 294.5, weight=96.0)
    g.diag(379.5, 303.7, 402.4, 290.1, weight=96.0)
    g.diag(611.0, 802.0, 640.2, 770.8, weight=56.0)
    g.diag(640.2, 770.8, 541.9, 641.9, weight=56.0)
    g.vbar(500.2, 411.0, 627.3, weight=48.0)
    g.hbar(483.1, 786.4, 642.0, weight=48.0)
    g.diag(786.4, 658.5, 817.9, 621.9, weight=48.0)
    g.diag(817.9, 621.9, 752.2, 434.4, weight=48.0)
    g.hbar(528.6, 764.5, 527.0, weight=56.0)
    g.hbar(550.2, 719.8, 435.9, weight=48.0)
    g.diag(719.8, 452.6, 740.4, 439.5, weight=48.0)
    g.diag(612.8, 617.9, 645.7, 590.3, weight=56.0)
    g.diag(645.7, 590.3, 509.0, 279.2, weight=56.0)
    g.hbar(403.6, 581.5, 263.2, weight=96.0)
    g.hbar(581.5, 927.5, 277.8, weight=96.0)
    g.diag(639.7, 419.7, 667.9, 273.6, weight=56.0)
    g.vbar(669.3, -52.0, 273.6, weight=56.0)
    return g
def g_cjk_unified_ideograph_78ba() -> Glyph:
    """確 U+78BA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni78BA", advance=1000, unicode=0x78BA, note="確：自动生成")
    g.diag(206.7, 541.9, 218.1, 558.8, weight=96.0)
    g.hbar(218.1, 442.3, 565.9, weight=96.0)
    g.diag(241.8, 538.3, 213.3, 417.7, weight=48.0)
    g.diag(213.3, 417.7, 58.0, 159.0, weight=48.0)
    g.diag(205.2, 383.1, 258.5, 214.8, weight=48.0)
    g.hbar(245.3, 400.0, 385.0, weight=96.0)
    g.diag(400.0, 403.3, 343.1, 282.9, weight=96.0)
    g.dot(320.8, 248.6, w=96.0, h=119.4, slant=-14.0)
    g.diag(488.5, 624.6, 458.9, 521.6, weight=96.0)
    g.diag(458.9, 521.6, 483.9, 443.4, weight=96.0)
    g.diag(519.2, 601.5, 527.7, 593.9, weight=96.0)
    g.hbar(527.7, 864.3, 616.4, weight=96.0)
    g.diag(864.3, 639.0, 748.3, 518.9, weight=96.0)
    g.diag(615.1, 778.5, 568.5, 555.6, weight=48.0)
    g.diag(568.5, 555.6, 326.3, 132.9, weight=48.0)
    g.vbar(529.7, -38.5, 398.8, weight=48.0)
    g.diag(634.8, 543.2, 722.3, 490.7, weight=64.0)
    g.diag(722.3, 490.7, 742.2, 440.8, weight=64.0)
    g.hbar(593.6, 809.9, 417.4, weight=84.0)
    g.diag(809.9, 426.5, 765.7, 456.9, weight=84.0)
    g.hbar(570.9, 793.1, 303.7, weight=84.0)
    g.vbar(807.9, 254.4, 320.2, weight=84.0)
    g.hbar(568.0, 816.4, 207.3, weight=76.0)
    g.diag(816.4, 221.4, 835.2, 284.2, weight=76.0)
    g.diag(690.6, 380.7, 715.5, 355.8, weight=96.0)
    g.vbar(714.1, 132.6, 355.8, weight=96.0)
    g.diag(712.7, 132.6, 698.1, 113.3, weight=96.0)
    g.hbar(557.4, 917.0, 86.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_78c1() -> Glyph:
    """磁 U+78C1 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni78C1", advance=1000, unicode=0x78C1, note="磁：自动生成")
    g.hbar(166.4, 434.3, 576.2, weight=84.0)
    g.diag(253.7, 525.5, 216.5, 389.1, weight=48.0)
    g.diag(216.5, 389.1, 97.3, 154.7, weight=48.0)
    g.diag(97.3, 154.7, 52.0, 112.1, weight=48.0)
    g.diag(182.4, 339.9, 236.6, 88.1, weight=48.0)
    g.hbar(238.6, 376.5, 324.1, weight=48.0)
    g.diag(376.5, 339.4, 349.0, 222.5, weight=48.0)
    g.diag(349.0, 222.5, 329.9, 212.5, weight=48.0)
    g.diag(257.7, 150.3, 276.6, 170.4, weight=84.0)
    g.hbar(276.6, 384.1, 174.4, weight=84.0)
    g.dot(550.2, 616.9, w=84.0, h=109.2, slant=-14.0)
    g.diag(743.4, 739.3, 782.3, 705.2, weight=84.0)
    g.diag(782.3, 705.2, 654.1, 509.5, weight=84.0)
    g.hbar(421.3, 933.0, 478.9, weight=84.0)
    g.diag(493.5, 420.2, 519.3, 392.7, weight=48.0)
    g.diag(519.3, 392.7, 435.2, 222.5, weight=48.0)
    g.hbar(435.2, 536.7, 229.1, weight=48.0)
    g.diag(580.8, 325.9, 553.2, 234.4, weight=48.0)
    g.diag(553.2, 234.4, 439.4, 39.2, weight=48.0)
    g.hbar(439.4, 566.4, 53.8, weight=48.0)
    g.diag(566.4, 68.4, 570.8, 64.0, weight=48.0)
    g.diag(561.7, 129.2, 612.9, 30.9, weight=48.0)
    g.diag(740.3, 475.4, 766.8, 442.8, weight=48.0)
    g.diag(766.8, 442.8, 667.5, 229.5, weight=48.0)
    g.hbar(667.5, 779.5, 234.5, weight=48.0)
    g.diag(835.7, 354.0, 798.5, 245.5, weight=48.0)
    g.diag(798.5, 245.5, 680.4, 50.7, weight=48.0)
    g.hbar(680.4, 842.7, 72.4, weight=48.0)
    g.diag(842.7, 94.2, 848.7, 89.1, weight=48.0)
    g.diag(833.7, 156.3, 923.0, -9.3, weight=48.0)
    return g
def g_cjk_unified_ideograph_78e8() -> Glyph:
    """磨 U+78E8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni78E8", advance=1000, unicode=0x78E8, note="磨：自动生成")
    g.diag(479.4, 792.0, 578.7, 727.4, weight=48.0)
    g.diag(333.8, 642.6, 348.0, 626.8, weight=96.0)
    g.hbar(348.0, 769.6, 659.3, weight=96.0)
    g.vbar(257.6, 444.8, 659.0, weight=64.0)
    g.diag(252.7, 444.8, 109.2, -8.2, weight=64.0)
    g.hbar(358.9, 540.1, 491.7, weight=48.0)
    g.diag(437.0, 591.5, 468.3, 560.1, weight=56.0)
    g.vbar(465.2, 299.4, 560.1, weight=56.0)
    g.diag(441.8, 462.3, 469.4, 480.7, weight=48.0)
    g.diag(469.4, 480.7, 320.3, 321.5, weight=48.0)
    g.dot(518.0, 412.6, w=48.0, h=53.9, slant=-14.0)
    g.hbar(594.1, 795.6, 524.9, weight=48.0)
    g.diag(665.5, 619.4, 697.5, 586.2, weight=48.0)
    g.vbar(693.5, 314.8, 586.2, weight=48.0)
    g.diag(667.4, 488.3, 706.4, 527.3, weight=48.0)
    g.diag(706.4, 527.3, 570.0, 357.2, weight=48.0)
    g.diag(707.9, 497.0, 804.0, 391.4, weight=96.0)
    g.hbar(804.0, 870.8, 384.9, weight=96.0)
    g.hbar(372.4, 721.4, 247.8, weight=48.0)
    g.diag(439.9, 197.2, 399.1, 122.9, weight=48.0)
    g.diag(399.1, 122.9, 219.4, -54.7, weight=48.0)
    g.diag(219.4, -54.7, 227.8, -35.2, weight=48.0)
    g.diag(448.5, 106.5, 478.4, -67.0, weight=96.0)
    g.hbar(468.8, 754.6, 113.2, weight=48.0)
    g.diag(754.6, 135.3, 716.6, 41.0, weight=48.0)
    g.diag(716.6, 41.0, 689.6, 22.7, weight=48.0)
    g.hbar(492.9, 583.0, -16.8, weight=48.0)
    g.hbar(583.0, 750.3, -14.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_7901() -> Glyph:
    """礁 U+7901 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7901", advance=1000, unicode=0x7901, note="礁：自动生成")
    g.hbar(150.2, 415.8, 619.0, weight=96.0)
    g.diag(223.2, 566.8, 205.7, 454.6, weight=48.0)
    g.diag(205.7, 454.6, 58.0, 179.6, weight=48.0)
    g.diag(168.5, 373.2, 232.4, 135.0, weight=48.0)
    g.hbar(222.2, 367.5, 372.0, weight=48.0)
    g.diag(367.5, 386.9, 345.9, 278.9, weight=48.0)
    g.diag(345.9, 278.9, 322.6, 260.7, weight=48.0)
    g.diag(249.6, 206.0, 260.1, 220.5, weight=96.0)
    g.hbar(260.1, 384.4, 228.4, weight=96.0)
    g.diag(547.6, 753.3, 528.6, 658.0, weight=48.0)
    g.diag(528.6, 658.0, 385.4, 442.1, weight=48.0)
    g.vbar(499.8, 395.6, 528.3, weight=48.0)
    g.vbar(505.9, 159.3, 395.6, weight=48.0)
    g.dot(714.4, 714.8, w=96.0, h=124.8, slant=-14.0)
    g.hbar(593.2, 851.7, 575.9, weight=96.0)
    g.hbar(593.2, 821.3, 445.2, weight=84.0)
    g.hbar(592.2, 824.3, 344.3, weight=84.0)
    g.diag(678.4, 532.4, 693.7, 522.7, weight=96.0)
    g.diag(693.7, 522.7, 725.7, 306.8, weight=96.0)
    g.diag(725.7, 306.8, 691.6, 255.6, weight=96.0)
    g.hbar(537.5, 903.4, 227.2, weight=92.0)
    g.diag(454.4, 111.7, 388.5, -47.5, weight=96.0)
    g.dot(588.2, 51.4, w=96.0, h=100.0, slant=-14.0)
    g.dot(716.9, 71.1, w=92.0, h=106.4, slant=-14.0)
    g.diag(817.2, 142.1, 947.0, -14.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_790e() -> Glyph:
    """礎 U+790E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni790E", advance=1000, unicode=0x790E, note="礎：自动生成")
    g.vbar(191.2, 497.6, 510.6, weight=96.0)
    g.hbar(189.5, 374.7, 530.1, weight=96.0)
    g.diag(228.3, 500.7, 204.1, 377.5, weight=48.0)
    g.diag(204.1, 377.5, 53.0, 119.2, weight=48.0)
    g.diag(181.4, 313.8, 237.9, 138.6, weight=48.0)
    g.hbar(224.3, 359.5, 315.8, weight=92.0)
    g.vbar(346.2, 224.9, 331.6, weight=92.0)
    g.diag(332.9, 224.9, 314.8, 216.3, weight=92.0)
    g.diag(245.3, 156.3, 258.8, 171.7, weight=96.0)
    g.hbar(258.8, 356.2, 183.1, weight=96.0)
    g.hbar(386.6, 612.3, 557.1, weight=48.0)
    g.diag(489.9, 707.4, 511.0, 580.9, weight=48.0)
    g.vbar(517.9, 328.2, 580.9, weight=48.0)
    g.diag(497.5, 520.9, 522.6, 543.4, weight=48.0)
    g.diag(522.6, 543.4, 363.4, 337.5, weight=48.0)
    g.diag(532.7, 488.5, 604.6, 439.2, weight=48.0)
    g.hbar(626.2, 806.2, 593.2, weight=84.0)
    g.hbar(759.7, 806.2, 608.3, weight=84.0)
    g.diag(697.4, 741.7, 718.0, 614.6, weight=48.0)
    g.vbar(720.1, 370.4, 614.6, weight=48.0)
    g.diag(704.0, 556.1, 684.1, 498.0, weight=48.0)
    g.diag(684.1, 498.0, 594.9, 439.1, weight=48.0)
    g.diag(742.2, 517.1, 744.3, 514.7, weight=56.0)
    g.diag(744.3, 514.7, 858.2, 451.4, weight=56.0)
    g.diag(461.0, 253.7, 550.9, 299.4, weight=48.0)
    g.hbar(550.9, 831.0, 325.7, weight=48.0)
    g.diag(831.0, 351.9, 733.6, 247.7, weight=48.0)
    g.diag(733.6, 247.7, 728.8, 212.9, weight=48.0)
    g.diag(596.5, 307.6, 625.0, 281.0, weight=96.0)
    g.vbar(624.1, 112.5, 281.0, weight=96.0)
    g.diag(623.1, 112.5, 640.3, 83.0, weight=96.0)
    g.hbar(643.1, 785.9, 185.9, weight=48.0)
    g.diag(470.8, 254.0, 501.5, 185.6, weight=96.0)
    g.diag(501.5, 185.6, 321.4, -21.7, weight=96.0)
    g.diag(515.6, 152.5, 531.0, 96.1, weight=96.0)
    g.hbar(531.0, 942.0, 44.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_796d() -> Glyph:
    """祭 U+796D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni796D", advance=1000, unicode=0x796D, note="祭：自动生成")
    g.diag(291.5, 781.1, 273.1, 691.6, weight=48.0)
    g.diag(273.1, 691.6, 164.6, 497.1, weight=48.0)
    g.diag(289.8, 644.8, 315.0, 521.6, weight=48.0)
    g.diag(315.0, 521.6, 58.0, 202.2, weight=48.0)
    g.dot(277.7, 538.7, w=96.0, h=104.0, slant=-14.0)
    g.dot(202.0, 447.6, w=96.0, h=121.6, slant=-14.0)
    g.diag(511.2, 639.0, 540.4, 679.2, weight=48.0)
    g.hbar(540.4, 658.7, 693.6, weight=48.0)
    g.diag(658.7, 707.9, 703.0, 679.0, weight=48.0)
    g.diag(703.0, 679.0, 609.5, 550.3, weight=48.0)
    g.diag(609.5, 550.3, 608.6, 544.8, weight=48.0)
    g.diag(440.9, 632.3, 942.0, 316.0, weight=48.0)
    g.hbar(340.3, 437.6, 418.2, weight=56.0)
    g.hbar(437.6, 619.0, 436.8, weight=56.0)
    g.hbar(223.8, 300.6, 257.9, weight=92.0)
    g.hbar(300.6, 732.7, 290.5, weight=92.0)
    g.diag(444.6, 248.3, 582.5, -72.0, weight=96.0)
    g.hbar(278.6, 582.5, -19.7, weight=96.0)
    g.diag(283.0, 204.6, 215.0, -8.7, weight=96.0)
    g.hbar(518.0, 734.0, 113.4, weight=96.0)
    g.diag(734.0, 71.7, 762.5, 19.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_7985() -> Glyph:
    """禅 U+7985 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7985", advance=1000, unicode=0x7985, note="禅：自动生成")
    g.dot(326.8, 742.0, w=96.0, h=121.8, slant=-14.0)
    g.diag(102.7, 512.3, 223.9, 435.3, weight=48.0)
    g.diag(223.9, 435.3, 53.1, 162.2, weight=48.0)
    g.vbar(284.7, -1.4, 353.7, weight=48.0)
    g.dot(389.3, 366.5, w=92.0, h=81.5, slant=-14.0)
    g.dot(557.4, 689.4, w=76.0, h=98.8, slant=-14.0)
    g.diag(748.4, 797.0, 780.4, 762.4, weight=96.0)
    g.diag(780.4, 762.4, 677.1, 640.2, weight=96.0)
    g.diag(677.1, 640.2, 676.0, 635.3, weight=96.0)
    g.vbar(492.5, 317.0, 534.2, weight=48.0)
    g.hbar(485.5, 806.2, 559.1, weight=48.0)
    g.diag(806.2, 581.0, 839.6, 543.1, weight=48.0)
    g.diag(839.6, 543.1, 778.1, 350.7, weight=48.0)
    g.hbar(572.8, 744.4, 452.3, weight=48.0)
    g.hbar(547.0, 761.3, 359.6, weight=76.0)
    g.hbar(409.2, 926.9, 218.3, weight=96.0)
    g.diag(613.5, 533.2, 657.1, 506.4, weight=96.0)
    g.vbar(654.6, -52.0, 506.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_798d() -> Glyph:
    """禍 U+798D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni798D", advance=1000, unicode=0x798D, note="禍：自动生成")
    g.diag(264.5, 767.3, 395.4, 666.8, weight=96.0)
    g.diag(76.0, 477.3, 212.3, 406.3, weight=48.0)
    g.diag(212.3, 406.3, 53.0, 125.5, weight=48.0)
    g.vbar(264.0, -47.3, 311.8, weight=48.0)
    g.dot(356.6, 323.4, w=96.0, h=72.6, slant=-14.0)
    g.diag(502.2, 673.0, 572.1, 358.5, weight=48.0)
    g.diag(572.1, 358.5, 546.1, 341.2, weight=48.0)
    g.diag(566.0, 662.6, 578.0, 651.8, weight=48.0)
    g.hbar(578.0, 770.0, 673.2, weight=48.0)
    g.diag(770.0, 694.5, 819.4, 660.5, weight=48.0)
    g.diag(819.4, 660.5, 783.8, 398.7, weight=48.0)
    g.diag(783.8, 398.7, 759.7, 377.8, weight=48.0)
    g.diag(634.1, 546.4, 687.6, 380.8, weight=48.0)
    g.diag(687.6, 380.8, 657.1, 364.2, weight=48.0)
    g.diag(701.1, 510.8, 706.3, 521.2, weight=96.0)
    g.hbar(706.3, 773.3, 532.8, weight=96.0)
    g.diag(423.6, 322.3, 463.5, 291.6, weight=96.0)
    g.vbar(452.5, -1.2, 291.6, weight=96.0)
    g.hbar(479.1, 626.0, 320.1, weight=48.0)
    g.diag(626.0, 326.3, 835.5, 230.9, weight=48.0)
    g.diag(835.5, 230.9, 894.8, 11.4, weight=48.0)
    g.hbar(781.7, 894.8, 29.7, weight=48.0)
    g.diag(536.7, 231.2, 568.1, 200.9, weight=48.0)
    g.diag(568.1, 200.9, 598.5, 76.3, weight=48.0)
    g.diag(589.1, 227.0, 592.0, 225.5, weight=48.0)
    g.hbar(592.0, 765.6, 235.5, weight=48.0)
    g.vbar(753.8, 171.5, 245.4, weight=48.0)
    g.hbar(719.9, 741.9, 166.8, weight=48.0)
    g.diag(614.2, 118.1, 621.8, 113.3, weight=48.0)
    g.hbar(621.8, 768.1, 118.3, weight=48.0)
    return g
def g_cjk_unified_ideograph_79df() -> Glyph:
    """租 U+79DF —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni79DF", advance=1000, unicode=0x79DF, note="租：自动生成")
    g.diag(484.1, 680.9, 380.6, 740.6, weight=96.0)
    g.diag(380.6, 740.6, 180.2, 628.2, weight=96.0)
    g.hbar(180.2, 251.7, 636.0, weight=96.0)
    g.hbar(68.0, 507.0, 481.4, weight=96.0)
    g.vbar(295.3, 433.5, 658.7, weight=48.0)
    g.vbar(303.4, -13.6, 433.5, weight=48.0)
    g.diag(292.7, 458.2, 236.0, 371.8, weight=48.0)
    g.diag(236.0, 371.8, 58.0, 127.0, weight=48.0)
    g.hbar(336.4, 508.4, 362.3, weight=96.0)
    g.vbar(537.0, 566.7, 648.5, weight=48.0)
    g.vbar(547.4, 179.8, 566.7, weight=48.0)
    g.diag(556.5, 179.8, 532.6, 144.0, weight=48.0)
    g.hbar(547.1, 701.8, 607.0, weight=48.0)
    g.vbar(726.2, 336.7, 574.3, weight=48.0)
    g.vbar(742.6, 164.4, 336.7, weight=48.0)
    g.diag(575.8, 451.3, 590.0, 468.3, weight=96.0)
    g.hbar(590.0, 718.9, 470.7, weight=96.0)
    g.dot(645.4, 326.5, w=96.0, h=124.8, slant=-14.0)
    g.hbar(332.7, 937.0, 128.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_7a1a() -> Glyph:
    """稚 U+7A1A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7A1A", advance=1000, unicode=0x7A1A, note="稚：自动生成")
    g.hbar(384.8, 437.4, 714.1, weight=96.0)
    g.diag(384.8, 716.5, 190.9, 609.8, weight=96.0)
    g.hbar(190.9, 243.6, 614.7, weight=96.0)
    g.hbar(75.9, 383.1, 471.5, weight=48.0)
    g.hbar(383.1, 438.9, 489.4, weight=48.0)
    g.vbar(289.1, 462.9, 630.2, weight=48.0)
    g.vbar(299.5, -0.5, 462.9, weight=48.0)
    g.diag(280.9, 456.0, 58.0, 154.5, weight=48.0)
    g.dot(336.2, 355.1, w=96.0, h=60.7, slant=-14.0)
    g.vbar(586.1, 682.6, 779.1, weight=48.0)
    g.diag(580.8, 682.6, 472.3, 479.2, weight=48.0)
    g.hbar(420.0, 472.3, 479.5, weight=48.0)
    g.vbar(518.6, -49.1, 502.2, weight=48.0)
    g.diag(661.7, 722.2, 756.2, 660.0, weight=96.0)
    g.diag(756.2, 660.0, 785.3, 585.3, weight=96.0)
    g.hbar(555.5, 806.2, 539.3, weight=96.0)
    g.vbar(804.7, 542.7, 602.1, weight=96.0)
    g.hbar(574.4, 690.6, 376.5, weight=92.0)
    g.hbar(690.6, 761.2, 391.0, weight=92.0)
    g.hbar(572.1, 752.8, 268.3, weight=92.0)
    g.hbar(752.8, 761.2, 279.3, weight=92.0)
    g.diag(696.6, 501.1, 723.4, 479.2, weight=96.0)
    g.vbar(724.4, 175.7, 479.2, weight=96.0)
    g.diag(725.3, 175.7, 709.5, 152.5, weight=96.0)
    g.diag(564.5, 115.7, 573.1, 108.0, weight=96.0)
    g.hbar(573.1, 927.0, 117.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_7a2e() -> Glyph:
    """種 U+7A2E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7A2E", advance=1000, unicode=0x7A2E, note="種：自动生成")
    g.diag(472.0, 677.4, 378.2, 727.5, weight=64.0)
    g.diag(378.2, 727.5, 165.1, 617.8, weight=64.0)
    g.diag(165.1, 617.8, 166.1, 619.0, weight=64.0)
    g.hbar(87.8, 422.1, 493.0, weight=96.0)
    g.vbar(287.1, 431.7, 647.8, weight=48.0)
    g.vbar(302.4, -20.9, 431.7, weight=48.0)
    g.diag(289.9, 470.0, 58.0, 134.8, weight=48.0)
    g.hbar(335.8, 485.2, 368.0, weight=84.0)
    g.diag(800.3, 644.4, 721.8, 748.2, weight=92.0)
    g.hbar(517.6, 721.8, 705.1, weight=92.0)
    g.diag(517.6, 662.0, 458.4, 691.2, weight=92.0)
    g.hbar(442.8, 913.2, 574.1, weight=76.0)
    g.vbar(518.5, 256.9, 465.6, weight=48.0)
    g.hbar(498.6, 846.5, 475.3, weight=48.0)
    g.vbar(812.4, 295.5, 494.7, weight=48.0)
    g.hbar(753.6, 778.2, 295.9, weight=48.0)
    g.hbar(535.7, 783.1, 370.2, weight=56.0)
    g.diag(560.0, 270.8, 564.9, 279.7, weight=64.0)
    g.hbar(564.9, 752.6, 292.5, weight=64.0)
    g.hbar(589.8, 611.6, 673.8, weight=96.0)
    g.vbar(666.7, 216.7, 678.1, weight=96.0)
    g.diag(743.6, 216.7, 632.4, 79.3, weight=96.0)
    g.diag(531.3, 214.2, 573.0, 152.0, weight=92.0)
    g.hbar(573.0, 738.2, 172.0, weight=92.0)
    g.diag(738.2, 192.0, 778.6, 234.0, weight=92.0)
    g.hbar(335.8, 932.0, 41.4, weight=92.0)
    return g
def g_cjk_unified_ideograph_7a3c() -> Glyph:
    """稼 U+7A3C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7A3C", advance=1000, unicode=0x7A3C, note="稼：自动生成")
    g.hbar(333.0, 407.7, 662.1, weight=96.0)
    g.diag(333.0, 668.2, 166.7, 579.4, weight=96.0)
    g.hbar(166.7, 210.5, 581.7, weight=96.0)
    g.hbar(72.5, 381.2, 441.2, weight=96.0)
    g.vbar(257.2, 399.2, 594.4, weight=48.0)
    g.vbar(273.4, 2.7, 399.2, weight=48.0)
    g.diag(256.5, 418.6, 58.0, 125.8, weight=48.0)
    g.dot(343.9, 339.0, w=96.0, h=100.6, slant=-14.0)
    g.diag(554.4, 774.4, 634.8, 725.9, weight=48.0)
    g.diag(634.8, 725.9, 658.6, 651.1, weight=48.0)
    g.dot(432.0, 558.4, w=96.0, h=124.8, slant=14.0)
    g.hbar(478.7, 823.4, 622.5, weight=96.0)
    g.diag(823.4, 640.3, 741.1, 521.6, weight=96.0)
    g.hbar(434.4, 734.4, 500.0, weight=48.0)
    g.diag(553.6, 451.2, 548.7, 417.1, weight=48.0)
    g.diag(548.7, 417.1, 381.7, 317.2, weight=48.0)
    g.diag(526.3, 367.2, 575.8, 275.1, weight=48.0)
    g.vbar(579.6, 92.8, 275.1, weight=48.0)
    g.diag(583.3, 92.8, 491.4, 31.8, weight=48.0)
    g.diag(532.1, 349.8, 536.6, 314.9, weight=48.0)
    g.diag(536.6, 314.9, 378.9, 201.5, weight=48.0)
    g.vbar(590.4, 238.1, 292.7, weight=48.0)
    g.diag(588.5, 238.1, 371.1, 75.4, weight=48.0)
    g.diag(726.0, 469.3, 736.7, 392.0, weight=96.0)
    g.diag(736.7, 392.0, 649.6, 306.3, weight=96.0)
    g.vbar(650.0, 298.4, 306.3, weight=96.0)
    g.diag(651.3, 282.9, 814.8, 123.4, weight=96.0)
    g.hbar(814.8, 947.0, 117.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_7a3f() -> Glyph:
    """稿 U+7A3F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7A3F", advance=1000, unicode=0x7A3F, note="稿：自动生成")
    g.diag(471.8, 623.2, 392.1, 711.5, weight=84.0)
    g.hbar(135.0, 392.1, 655.8, weight=84.0)
    g.diag(135.0, 600.2, 136.5, 601.7, weight=84.0)
    g.hbar(59.4, 490.9, 464.0, weight=84.0)
    g.vbar(288.6, -58.0, 630.2, weight=48.0)
    g.diag(287.9, 442.0, 236.3, 356.2, weight=48.0)
    g.diag(236.3, 356.2, 59.4, 84.7, weight=48.0)
    g.diag(326.1, 406.1, 391.4, 360.4, weight=48.0)
    g.diag(391.4, 360.4, 413.5, 290.9, weight=48.0)
    g.diag(611.2, 793.0, 693.6, 746.5, weight=64.0)
    g.diag(693.6, 746.5, 735.7, 650.7, weight=64.0)
    g.hbar(450.2, 869.1, 581.1, weight=84.0)
    g.vbar(578.6, 345.6, 490.3, weight=48.0)
    g.hbar(570.5, 787.3, 491.4, weight=48.0)
    g.diag(787.3, 506.8, 734.4, 412.9, weight=48.0)
    g.hbar(603.0, 765.3, 378.9, weight=48.0)
    g.vbar(764.3, 399.2, 419.6, weight=48.0)
    g.vbar(429.1, -32.6, 306.1, weight=84.0)
    g.hbar(481.2, 631.3, 249.1, weight=76.0)
    g.hbar(631.3, 919.1, 280.6, weight=76.0)
    g.vbar(902.3, -32.9, 297.1, weight=76.0)
    g.diag(885.4, -32.9, 776.5, 47.7, weight=76.0)
    g.vbar(570.6, 160.8, 177.3, weight=56.0)
    g.vbar(582.5, 39.8, 160.8, weight=56.0)
    g.hbar(586.1, 764.7, 181.4, weight=48.0)
    g.diag(764.7, 196.1, 708.1, 101.4, weight=48.0)
    g.hbar(608.4, 750.0, 72.1, weight=48.0)
    g.vbar(747.1, 87.5, 111.6, weight=48.0)
    return g
def g_cjk_unified_ideograph_7a40() -> Glyph:
    """穀 U+7A40 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7A40", advance=1000, unicode=0x7A40, note="穀：自动生成")
    g.hbar(199.2, 463.7, 637.9, weight=64.0)
    g.diag(323.1, 772.0, 356.4, 740.6, weight=96.0)
    g.vbar(350.4, 589.8, 740.6, weight=96.0)
    g.diag(344.4, 589.8, 328.6, 570.4, weight=96.0)
    g.hbar(237.1, 439.6, 546.3, weight=56.0)
    g.diag(163.1, 481.6, 172.8, 453.5, weight=96.0)
    g.diag(172.8, 453.5, 132.6, 339.2, weight=96.0)
    g.hbar(194.5, 494.0, 466.5, weight=48.0)
    g.diag(494.0, 488.5, 417.4, 409.5, weight=48.0)
    g.hbar(232.5, 382.3, 400.7, weight=48.0)
    g.hbar(344.7, 387.8, 326.8, weight=56.0)
    g.hbar(177.7, 344.7, 304.0, weight=56.0)
    g.diag(177.7, 276.0, 180.7, 278.2, weight=56.0)
    g.hbar(101.1, 449.8, 216.2, weight=48.0)
    g.diag(298.1, 290.2, 320.9, 271.7, weight=96.0)
    g.vbar(316.9, -52.0, 271.7, weight=96.0)
    g.diag(291.6, 195.8, 247.3, 144.2, weight=48.0)
    g.diag(247.3, 144.2, 96.5, 7.2, weight=48.0)
    g.dot(404.9, 121.9, w=96.0, h=110.8, slant=-14.0)
    g.vbar(546.9, 399.3, 654.5, weight=64.0)
    g.hbar(597.8, 615.6, 650.9, weight=96.0)
    g.hbar(615.6, 737.2, 657.6, weight=96.0)
    g.vbar(718.6, 466.7, 666.9, weight=96.0)
    g.hbar(699.9, 862.2, 466.3, weight=96.0)
    g.diag(518.2, 317.0, 615.2, 231.8, weight=96.0)
    g.diag(615.2, 231.8, 440.5, 17.4, weight=96.0)
    g.diag(509.9, 257.8, 908.5, 15.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_7a4d() -> Glyph:
    """積 U+7A4D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7A4D", advance=1000, unicode=0x7A4D, note="積：自动生成")
    g.hbar(371.6, 478.2, 677.5, weight=96.0)
    g.diag(371.6, 688.7, 216.9, 595.8, weight=96.0)
    g.hbar(216.9, 251.5, 598.1, weight=96.0)
    g.hbar(84.0, 392.5, 470.3, weight=96.0)
    g.hbar(392.5, 420.8, 498.5, weight=96.0)
    g.vbar(295.8, 456.6, 613.1, weight=48.0)
    g.vbar(307.8, -20.4, 456.6, weight=48.0)
    g.diag(294.0, 453.3, 239.2, 365.9, weight=48.0)
    g.diag(239.2, 365.9, 69.7, 121.0, weight=48.0)
    g.hbar(337.1, 504.9, 334.6, weight=96.0)
    g.diag(532.8, 592.4, 580.5, 653.0, weight=64.0)
    g.hbar(580.5, 802.3, 679.3, weight=64.0)
    g.diag(540.6, 626.5, 563.1, 561.8, weight=64.0)
    g.hbar(563.1, 771.8, 582.1, weight=64.0)
    g.diag(639.7, 703.5, 655.2, 748.6, weight=84.0)
    g.vbar(652.4, 521.2, 748.6, weight=84.0)
    g.diag(649.5, 521.2, 636.1, 503.1, weight=84.0)
    g.hbar(421.8, 584.5, 475.9, weight=64.0)
    g.hbar(584.5, 930.3, 491.0, weight=64.0)
    g.vbar(529.6, 326.1, 397.7, weight=48.0)
    g.vbar(531.3, 126.1, 326.1, weight=48.0)
    g.hbar(549.5, 735.3, 404.1, weight=48.0)
    g.diag(735.3, 418.1, 781.1, 381.8, weight=48.0)
    g.vbar(775.5, 108.5, 381.8, weight=48.0)
    g.diag(565.7, 302.4, 576.9, 312.0, weight=56.0)
    g.hbar(576.9, 751.1, 318.7, weight=56.0)
    g.hbar(563.5, 751.4, 239.2, weight=56.0)
    g.hbar(556.8, 749.3, 153.7, weight=64.0)
    g.vbar(573.6, 63.7, 117.6, weight=64.0)
    g.diag(575.2, 63.7, 454.7, -40.7, weight=64.0)
    g.hbar(333.5, 454.7, -36.9, weight=64.0)
    g.diag(734.2, 94.2, 809.0, -72.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_7a92() -> Glyph:
    """窒 U+7A92 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7A92", advance=1000, unicode=0x7A92, note="窒：自动生成")
    g.diag(430.8, 797.0, 519.7, 755.6, weight=48.0)
    g.diag(519.7, 755.6, 551.5, 684.8, weight=48.0)
    g.diag(244.2, 661.9, 251.3, 670.5, weight=84.0)
    g.diag(251.3, 670.5, 192.7, 545.1, weight=84.0)
    g.diag(192.7, 545.1, 214.6, 456.0, weight=84.0)
    g.hbar(259.9, 812.7, 654.9, weight=56.0)
    g.diag(812.7, 670.5, 676.0, 546.4, weight=56.0)
    g.diag(347.4, 595.8, 364.6, 546.5, weight=92.0)
    g.diag(364.6, 546.5, 278.3, 431.5, weight=92.0)
    g.diag(558.3, 646.9, 666.9, 473.5, weight=48.0)
    g.hbar(298.8, 446.6, 448.9, weight=48.0)
    g.hbar(446.6, 671.5, 470.6, weight=48.0)
    g.diag(479.0, 418.1, 450.5, 302.5, weight=48.0)
    g.hbar(450.5, 648.8, 301.7, weight=48.0)
    g.diag(599.4, 371.9, 713.5, 237.7, weight=48.0)
    g.diag(311.6, 5.6, 337.2, 89.4, weight=96.0)
    g.hbar(337.2, 697.1, 146.2, weight=96.0)
    g.diag(463.1, 243.7, 486.4, 229.2, weight=96.0)
    g.vbar(493.9, 40.8, 229.2, weight=96.0)
    g.diag(501.4, 40.8, 478.3, 10.5, weight=96.0)
    g.hbar(192.6, 823.6, -24.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_7a9f() -> Glyph:
    """窟 U+7A9F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7A9F", advance=1000, unicode=0x7A9F, note="窟：自动生成")
    g.diag(506.8, 797.0, 579.5, 761.6, weight=48.0)
    g.diag(579.5, 761.6, 616.1, 699.5, weight=48.0)
    g.diag(319.9, 664.2, 277.3, 553.6, weight=64.0)
    g.diag(277.3, 553.6, 296.6, 490.0, weight=64.0)
    g.hbar(338.4, 852.5, 668.5, weight=48.0)
    g.diag(852.5, 688.2, 743.3, 567.9, weight=48.0)
    g.diag(416.4, 622.3, 432.9, 567.8, weight=56.0)
    g.diag(432.9, 567.8, 344.8, 479.1, weight=56.0)
    g.diag(612.6, 660.4, 752.0, 569.8, weight=48.0)
    g.hbar(413.2, 653.4, 482.9, weight=48.0)
    g.diag(653.4, 515.1, 697.3, 485.7, weight=48.0)
    g.diag(697.3, 485.7, 651.7, 416.4, weight=48.0)
    g.hbar(393.2, 693.5, 372.7, weight=48.0)
    g.diag(693.5, 403.3, 720.2, 368.2, weight=48.0)
    g.diag(365.9, 483.3, 327.1, 315.7, weight=48.0)
    g.diag(327.1, 315.7, 133.7, 10.7, weight=48.0)
    g.vbar(438.8, 175.0, 310.9, weight=76.0)
    g.hbar(463.5, 689.0, 197.4, weight=76.0)
    g.diag(689.0, 219.8, 701.9, 211.6, weight=76.0)
    g.diag(722.7, 355.6, 750.9, 312.1, weight=96.0)
    g.diag(750.9, 312.1, 722.2, 179.0, weight=96.0)
    g.diag(546.3, 338.6, 587.8, 297.9, weight=96.0)
    g.vbar(582.9, 39.7, 297.9, weight=96.0)
    g.diag(577.9, 39.7, 566.1, 28.9, weight=96.0)
    g.diag(413.6, 141.9, 390.3, -25.4, weight=96.0)
    g.hbar(390.3, 746.1, 2.3, weight=96.0)
    g.diag(746.1, 29.9, 761.2, 13.6, weight=96.0)
    g.diag(747.6, 146.0, 903.3, -14.6, weight=96.0)
    g.hbar(774.9, 903.3, -18.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_7aae() -> Glyph:
    """窮 U+7AAE —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7AAE", advance=1000, unicode=0x7AAE, note="窮：自动生成")
    g.diag(480.5, 802.0, 549.9, 763.0, weight=48.0)
    g.diag(549.9, 763.0, 570.8, 709.2, weight=48.0)
    g.diag(263.9, 688.0, 224.0, 569.9, weight=96.0)
    g.diag(224.0, 569.9, 261.8, 513.3, weight=96.0)
    g.hbar(288.4, 501.2, 670.2, weight=48.0)
    g.hbar(501.2, 858.3, 686.9, weight=48.0)
    g.diag(858.3, 699.5, 754.7, 570.8, weight=48.0)
    g.diag(416.8, 652.7, 432.3, 617.4, weight=64.0)
    g.diag(432.3, 617.4, 346.5, 531.0, weight=64.0)
    g.hbar(243.2, 346.5, 523.7, weight=64.0)
    g.diag(549.0, 671.7, 579.0, 642.6, weight=48.0)
    g.diag(579.0, 642.6, 565.8, 547.1, weight=48.0)
    g.hbar(565.8, 757.1, 566.1, weight=48.0)
    g.diag(415.6, 434.2, 376.0, 468.1, weight=56.0)
    g.diag(376.0, 468.1, 325.4, 403.4, weight=56.0)
    g.diag(286.6, 399.4, 243.6, 257.4, weight=48.0)
    g.diag(243.6, 257.4, 281.6, 172.3, weight=48.0)
    g.hbar(307.5, 334.9, 392.9, weight=48.0)
    g.hbar(334.9, 438.9, 403.2, weight=48.0)
    g.vbar(447.8, 259.1, 417.3, weight=48.0)
    g.vbar(452.6, -41.8, 259.1, weight=48.0)
    g.diag(448.5, -41.8, 365.4, -2.8, weight=48.0)
    g.hbar(310.7, 452.0, 320.9, weight=48.0)
    g.hbar(314.3, 446.6, 246.9, weight=56.0)
    g.hbar(171.3, 214.7, 144.6, weight=48.0)
    g.hbar(214.7, 437.0, 165.3, weight=48.0)
    g.diag(488.0, 244.6, 389.5, 145.6, weight=48.0)
    g.diag(389.5, 145.6, 145.6, -34.2, weight=48.0)
    g.hbar(578.5, 771.0, 450.6, weight=48.0)
    g.diag(771.0, 455.9, 702.3, 350.5, weight=48.0)
    g.hbar(622.7, 741.1, 331.2, weight=48.0)
    g.vbar(741.3, 336.0, 362.8, weight=48.0)
    g.vbar(574.8, 201.9, 340.4, weight=96.0)
    g.hbar(556.2, 818.5, 205.1, weight=96.0)
    g.diag(818.5, 208.2, 708.0, -64.4, weight=96.0)
    g.diag(708.0, -64.4, 614.6, -9.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_7aaf() -> Glyph:
    """窯 U+7AAF —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7AAF", advance=1000, unicode=0x7AAF, note="窯：自动生成")
    g.diag(464.1, 797.0, 546.5, 726.1, weight=48.0)
    g.diag(259.0, 672.4, 233.2, 501.9, weight=92.0)
    g.hbar(299.3, 424.9, 651.8, weight=48.0)
    g.hbar(424.9, 849.5, 668.8, weight=48.0)
    g.diag(849.5, 684.4, 738.1, 596.8, weight=48.0)
    g.diag(398.0, 628.4, 421.8, 585.3, weight=96.0)
    g.diag(421.8, 585.3, 280.1, 455.0, weight=96.0)
    g.diag(557.0, 655.2, 566.2, 646.3, weight=48.0)
    g.diag(566.2, 646.3, 603.3, 544.6, weight=48.0)
    g.hbar(603.3, 737.1, 545.8, weight=48.0)
    g.dot(409.5, 445.4, w=96.0, h=89.6, slant=-14.0)
    g.diag(560.8, 510.5, 578.3, 485.3, weight=96.0)
    g.diag(578.3, 485.3, 521.6, 416.0, weight=96.0)
    g.vbar(521.6, 411.8, 416.0, weight=96.0)
    g.hbar(332.8, 678.7, 375.9, weight=76.0)
    g.hbar(354.8, 643.2, 271.0, weight=76.0)
    g.diag(467.9, 340.9, 492.8, 312.2, weight=96.0)
    g.vbar(490.4, 215.4, 312.2, weight=96.0)
    g.diag(488.0, 215.4, 473.7, 198.2, weight=96.0)
    g.hbar(265.7, 722.8, 167.5, weight=76.0)
    g.diag(176.6, 108.1, 150.8, -72.0, weight=96.0)
    g.dot(359.6, 40.6, w=96.0, h=108.7, slant=-14.0)
    g.dot(549.3, 46.8, w=96.0, h=107.7, slant=-14.0)
    g.diag(719.9, 108.1, 849.2, -39.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_7ae5() -> Glyph:
    """童 U+7AE5 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7AE5", advance=1000, unicode=0x7AE5, note="童：自动生成")
    g.diag(441.3, 789.0, 511.9, 756.5, weight=48.0)
    g.diag(511.9, 756.5, 549.8, 674.5, weight=48.0)
    g.diag(349.1, 604.5, 364.8, 626.7, weight=92.0)
    g.hbar(364.8, 617.1, 646.5, weight=92.0)
    g.diag(617.1, 666.2, 622.5, 622.1, weight=92.0)
    g.dot(390.9, 544.6, w=92.0, h=108.6, slant=-14.0)
    g.diag(570.2, 628.5, 593.9, 598.9, weight=92.0)
    g.diag(593.9, 598.9, 527.2, 494.8, weight=92.0)
    g.hbar(109.8, 890.2, 456.6, weight=64.0)
    g.diag(277.8, 399.7, 356.2, 163.3, weight=92.0)
    g.hbar(333.0, 713.5, 369.7, weight=48.0)
    g.vbar(677.7, 215.0, 394.1, weight=48.0)
    g.hbar(618.8, 641.9, 214.3, weight=48.0)
    g.hbar(357.5, 539.6, 287.9, weight=64.0)
    g.diag(539.6, 306.6, 598.0, 252.4, weight=64.0)
    g.diag(376.3, 181.4, 382.9, 189.9, weight=64.0)
    g.hbar(382.9, 616.2, 207.1, weight=64.0)
    g.diag(461.3, 361.0, 489.9, 344.1, weight=92.0)
    g.vbar(485.9, 16.5, 344.1, weight=92.0)
    g.diag(481.8, 16.5, 469.0, 2.8, weight=92.0)
    g.diag(353.4, 126.6, 373.9, 76.2, weight=92.0)
    g.hbar(373.9, 637.2, 113.8, weight=92.0)
    g.hbar(212.9, 815.7, -30.1, weight=92.0)
    return g
def g_cjk_unified_ideograph_7aef() -> Glyph:
    """端 U+7AEF —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7AEF", advance=1000, unicode=0x7AEF, note="端：自动生成")
    g.diag(236.2, 706.3, 303.6, 654.9, weight=96.0)
    g.diag(303.6, 654.9, 350.8, 525.0, weight=96.0)
    g.diag(150.0, 382.4, 192.2, 437.5, weight=96.0)
    g.hbar(192.2, 360.4, 462.6, weight=96.0)
    g.vbar(358.5, 435.0, 487.8, weight=96.0)
    g.diag(156.1, 404.7, 261.8, 204.9, weight=84.0)
    g.diag(319.5, 435.5, 354.3, 374.4, weight=96.0)
    g.diag(354.3, 374.4, 304.3, 199.0, weight=96.0)
    g.diag(304.3, 199.0, 283.3, 171.9, weight=96.0)
    g.hbar(83.0, 141.9, 85.6, weight=96.0)
    g.diag(141.9, 79.7, 382.9, 199.7, weight=96.0)
    g.diag(635.7, 766.3, 686.8, 721.5, weight=96.0)
    g.diag(686.8, 721.5, 656.0, 527.4, weight=96.0)
    g.diag(502.9, 622.8, 530.7, 577.8, weight=96.0)
    g.vbar(526.2, 469.4, 577.8, weight=96.0)
    g.hbar(521.8, 805.9, 505.9, weight=96.0)
    g.diag(811.8, 580.5, 869.2, 632.4, weight=96.0)
    g.diag(869.2, 632.4, 804.6, 496.9, weight=96.0)
    g.hbar(503.9, 806.0, 364.1, weight=48.0)
    g.diag(633.4, 332.3, 626.7, 308.8, weight=48.0)
    g.diag(626.7, 308.8, 556.0, 217.8, weight=48.0)
    g.diag(409.7, 191.1, 441.8, 141.9, weight=84.0)
    g.vbar(441.8, 0.5, 141.9, weight=84.0)
    g.hbar(441.8, 536.6, -4.8, weight=84.0)
    g.hbar(445.0, 919.6, 213.9, weight=96.0)
    g.vbar(898.7, -40.4, 242.1, weight=96.0)
    g.hbar(735.4, 877.7, -14.0, weight=96.0)
    g.diag(541.4, 175.1, 570.3, 152.6, weight=96.0)
    g.diag(570.3, 152.6, 485.4, -17.6, weight=96.0)
    g.diag(668.9, 207.2, 704.2, 174.0, weight=96.0)
    g.diag(704.2, 174.0, 729.6, -3.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_7af6() -> Glyph:
    """競 U+7AF6 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7AF6", advance=1000, unicode=0x7AF6, note="競：自动生成")
    g.diag(307.7, 750.6, 407.9, 682.8, weight=56.0)
    g.hbar(229.8, 471.6, 597.8, weight=96.0)
    g.dot(248.0, 480.4, w=96.0, h=75.3, slant=-14.0)
    g.diag(398.8, 577.5, 427.8, 549.2, weight=96.0)
    g.diag(427.8, 549.2, 370.5, 449.0, weight=96.0)
    g.hbar(97.3, 476.7, 407.6, weight=64.0)
    g.diag(174.2, 305.4, 203.4, 275.2, weight=48.0)
    g.vbar(218.6, 167.7, 275.2, weight=48.0)
    g.diag(223.7, 303.3, 229.4, 298.8, weight=48.0)
    g.hbar(229.4, 407.4, 315.0, weight=48.0)
    g.diag(407.4, 331.1, 382.6, 256.8, weight=48.0)
    g.diag(382.6, 256.8, 360.3, 238.6, weight=48.0)
    g.hbar(246.0, 411.9, 197.1, weight=48.0)
    g.diag(227.8, 150.5, 259.3, 107.6, weight=96.0)
    g.diag(259.3, 107.6, 62.9, -66.0, weight=96.0)
    g.diag(324.9, 183.9, 294.5, 206.2, weight=48.0)
    g.diag(294.5, 206.2, 374.7, 27.7, weight=48.0)
    g.diag(374.7, 27.7, 460.5, 112.1, weight=48.0)
    g.dot(669.5, 743.0, w=96.0, h=124.8, slant=-14.0)
    g.hbar(556.6, 842.0, 622.1, weight=96.0)
    g.dot(599.6, 509.2, w=96.0, h=74.4, slant=-14.0)
    g.diag(729.7, 596.8, 759.1, 570.9, weight=96.0)
    g.diag(759.1, 570.9, 705.4, 475.4, weight=96.0)
    g.hbar(528.3, 920.9, 449.5, weight=56.0)
    g.diag(530.3, 358.0, 558.5, 327.0, weight=96.0)
    g.vbar(575.3, 211.3, 327.0, weight=96.0)
    g.hbar(576.9, 769.5, 364.0, weight=48.0)
    g.diag(769.5, 374.1, 746.9, 302.3, weight=48.0)
    g.diag(746.9, 302.3, 720.6, 285.1, weight=48.0)
    g.diag(604.2, 225.4, 615.0, 237.6, weight=48.0)
    g.hbar(615.0, 779.2, 247.2, weight=48.0)
    g.diag(580.9, 198.1, 611.2, 143.9, weight=96.0)
    g.diag(611.2, 143.9, 406.9, -67.0, weight=96.0)
    g.diag(675.0, 222.4, 739.3, 102.9, weight=48.0)
    g.diag(739.3, 102.9, 943.2, -67.3, weight=48.0)
    g.vbar(941.1, -67.3, 92.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_7b1b() -> Glyph:
    """笛 U+7B1B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7B1B", advance=1000, unicode=0x7B1B, note="笛：自动生成")
    g.diag(290.1, 673.7, 277.3, 713.2, weight=96.0)
    g.diag(277.3, 713.2, 156.0, 376.4, weight=96.0)
    g.hbar(286.2, 442.0, 645.2, weight=96.0)
    g.hbar(442.0, 527.3, 642.8, weight=96.0)
    g.dot(318.3, 504.7, w=96.0, h=124.8, slant=-14.0)
    g.diag(599.5, 787.0, 641.1, 734.1, weight=64.0)
    g.diag(641.1, 734.1, 443.7, 480.0, weight=64.0)
    g.hbar(638.4, 862.3, 680.8, weight=96.0)
    g.diag(594.2, 584.6, 693.0, 526.3, weight=96.0)
    g.diag(693.0, 526.3, 710.1, 412.1, weight=96.0)
    g.vbar(226.5, 229.3, 329.3, weight=48.0)
    g.diag(229.6, 229.3, 279.6, -45.2, weight=48.0)
    g.hbar(227.4, 634.8, 270.5, weight=48.0)
    g.diag(634.8, 224.4, 694.1, -38.0, weight=48.0)
    g.diag(694.1, -38.0, 641.5, 21.6, weight=48.0)
    g.hbar(282.0, 694.4, 154.7, weight=96.0)
    g.diag(388.7, 462.2, 473.3, 423.2, weight=96.0)
    g.vbar(469.1, 45.8, 423.2, weight=96.0)
    g.diag(464.9, 45.8, 447.0, 22.6, weight=96.0)
    g.diag(292.5, -31.0, 310.3, -16.3, weight=96.0)
    g.hbar(310.3, 610.0, -3.6, weight=96.0)
    g.diag(610.0, 9.0, 628.9, 22.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_7b26() -> Glyph:
    """符 U+7B26 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7B26", advance=1000, unicode=0x7B26, note="符：自动生成")
    g.vbar(309.3, 667.9, 707.3, weight=96.0)
    g.diag(307.3, 707.3, 242.0, 567.9, weight=96.0)
    g.diag(242.0, 567.9, 272.0, 472.4, weight=96.0)
    g.hbar(310.2, 462.0, 639.9, weight=96.0)
    g.diag(462.0, 653.8, 521.4, 618.3, weight=96.0)
    g.diag(315.2, 587.9, 382.1, 520.6, weight=96.0)
    g.diag(382.1, 520.6, 358.2, 460.8, weight=96.0)
    g.vbar(626.4, 690.7, 717.7, weight=96.0)
    g.diag(626.4, 717.7, 433.9, 504.7, weight=96.0)
    g.hbar(617.2, 829.0, 661.4, weight=96.0)
    g.diag(621.1, 606.0, 695.3, 543.9, weight=96.0)
    g.diag(695.3, 543.9, 669.6, 472.6, weight=96.0)
    g.diag(309.2, 462.8, 266.2, 341.7, weight=48.0)
    g.diag(266.2, 341.7, 71.0, 110.1, weight=48.0)
    g.vbar(279.4, -52.0, 294.2, weight=48.0)
    g.hbar(326.7, 899.0, 313.6, weight=96.0)
    g.diag(646.5, 527.2, 685.7, 314.0, weight=96.0)
    g.vbar(664.8, -61.1, 314.0, weight=96.0)
    g.diag(643.8, -61.1, 518.2, 97.6, weight=96.0)
    g.diag(430.9, 255.7, 528.8, 34.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_7b52() -> Glyph:
    """筒 U+7B52 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7B52", advance=1000, unicode=0x7B52, note="筒：自动生成")
    g.diag(298.2, 683.2, 303.3, 717.5, weight=96.0)
    g.diag(303.3, 717.5, 187.2, 554.4, weight=96.0)
    g.vbar(186.9, 479.2, 554.4, weight=96.0)
    g.hbar(290.1, 444.7, 658.1, weight=64.0)
    g.diag(444.7, 670.8, 524.5, 632.2, weight=64.0)
    g.diag(294.4, 624.1, 395.7, 468.8, weight=48.0)
    g.vbar(622.5, 712.0, 753.4, weight=96.0)
    g.diag(620.8, 753.4, 483.4, 502.4, weight=96.0)
    g.hbar(612.0, 848.8, 683.5, weight=56.0)
    g.diag(619.5, 646.5, 696.2, 579.2, weight=56.0)
    g.vbar(699.4, 504.8, 579.2, weight=56.0)
    g.vbar(253.4, 322.6, 450.3, weight=48.0)
    g.vbar(233.9, -47.8, 322.6, weight=48.0)
    g.hbar(264.7, 688.0, 463.6, weight=48.0)
    g.diag(688.0, 489.2, 720.0, 325.4, weight=48.0)
    g.vbar(742.3, -70.6, 325.4, weight=48.0)
    g.hbar(596.4, 764.7, -48.0, weight=48.0)
    g.diag(360.9, 404.8, 429.5, 333.9, weight=96.0)
    g.hbar(429.5, 546.5, 346.6, weight=96.0)
    g.diag(546.5, 359.3, 577.2, 439.7, weight=96.0)
    g.diag(381.9, 221.6, 372.7, 202.0, weight=48.0)
    g.vbar(394.1, 69.5, 202.0, weight=48.0)
    g.hbar(388.6, 590.5, 218.8, weight=48.0)
    g.diag(590.5, 225.6, 532.1, 129.8, weight=48.0)
    g.hbar(421.3, 565.0, 108.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_7b97() -> Glyph:
    """算 U+7B97 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7B97", advance=1000, unicode=0x7B97, note="算：自动生成")
    g.diag(311.5, 774.6, 340.7, 732.6, weight=96.0)
    g.diag(340.7, 732.6, 208.2, 565.1, weight=96.0)
    g.hbar(339.5, 499.7, 687.7, weight=48.0)
    g.dot(373.3, 613.4, w=48.0, h=62.4, slant=-14.0)
    g.diag(570.2, 792.0, 597.3, 753.1, weight=96.0)
    g.diag(597.3, 753.1, 489.1, 608.6, weight=96.0)
    g.hbar(595.3, 792.2, 712.4, weight=48.0)
    g.diag(604.0, 644.3, 693.8, 595.1, weight=48.0)
    g.vbar(352.0, 290.0, 561.3, weight=48.0)
    g.hbar(383.9, 471.5, 550.9, weight=48.0)
    g.diag(471.5, 550.2, 578.6, 473.9, weight=48.0)
    g.vbar(588.9, 292.9, 473.9, weight=48.0)
    g.diag(392.6, 449.3, 400.4, 462.8, weight=48.0)
    g.hbar(400.4, 531.6, 469.1, weight=48.0)
    g.hbar(389.7, 538.4, 388.5, weight=48.0)
    g.hbar(388.7, 570.2, 325.2, weight=48.0)
    g.hbar(97.2, 887.8, 187.2, weight=96.0)
    g.diag(336.6, 262.0, 395.7, 206.4, weight=96.0)
    g.diag(395.7, 206.4, 237.2, -22.8, weight=96.0)
    g.diag(567.3, 284.2, 727.5, 72.6, weight=96.0)
    g.diag(727.5, 72.6, 598.2, -72.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_7ba1() -> Glyph:
    """管 U+7BA1 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7BA1", advance=1000, unicode=0x7BA1, note="管：自动生成")
    g.diag(320.6, 775.1, 350.5, 737.2, weight=96.0)
    g.diag(350.5, 737.2, 230.2, 579.8, weight=96.0)
    g.dot(426.4, 701.0, w=96.0, h=124.8, slant=-14.0)
    g.dot(383.2, 611.1, w=92.0, h=80.2, slant=-14.0)
    g.diag(572.6, 802.0, 600.3, 765.4, weight=96.0)
    g.diag(600.3, 765.4, 501.4, 626.0, weight=96.0)
    g.hbar(602.4, 772.6, 722.2, weight=64.0)
    g.diag(596.7, 648.1, 679.4, 588.5, weight=48.0)
    g.diag(463.0, 582.7, 540.9, 525.0, weight=48.0)
    g.diag(211.0, 501.0, 221.2, 465.2, weight=96.0)
    g.diag(221.2, 465.2, 168.7, 321.1, weight=96.0)
    g.hbar(247.6, 835.0, 483.3, weight=48.0)
    g.diag(835.0, 517.6, 737.1, 418.3, weight=48.0)
    g.diag(348.5, 411.5, 394.1, 366.0, weight=96.0)
    g.vbar(383.3, -52.0, 366.0, weight=96.0)
    g.hbar(411.0, 416.7, 392.0, weight=48.0)
    g.hbar(416.7, 617.7, 399.3, weight=48.0)
    g.diag(617.7, 407.9, 589.0, 334.6, weight=48.0)
    g.diag(589.0, 334.6, 562.0, 315.4, weight=48.0)
    g.diag(415.9, 253.8, 435.1, 270.8, weight=48.0)
    g.hbar(435.1, 618.8, 278.2, weight=48.0)
    g.hbar(410.1, 610.0, 167.3, weight=48.0)
    g.diag(610.0, 189.5, 648.6, 150.9, weight=48.0)
    g.diag(648.6, 150.9, 631.3, 100.0, weight=48.0)
    g.diag(631.3, 100.0, 597.6, 71.1, weight=48.0)
    g.hbar(405.3, 667.8, 16.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_7bb1() -> Glyph:
    """箱 U+7BB1 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7BB1", advance=1000, unicode=0x7BB1, note="箱：自动生成")
    g.diag(345.7, 701.2, 351.0, 725.8, weight=96.0)
    g.diag(351.0, 725.8, 270.1, 583.8, weight=96.0)
    g.diag(270.1, 583.8, 280.6, 519.8, weight=96.0)
    g.hbar(351.8, 506.3, 680.1, weight=64.0)
    g.hbar(506.3, 570.2, 681.9, weight=64.0)
    g.hbar(321.2, 493.6, 586.6, weight=56.0)
    g.vbar(628.9, 723.1, 724.3, weight=96.0)
    g.diag(628.8, 723.1, 471.8, 549.3, weight=96.0)
    g.hbar(637.6, 841.0, 708.3, weight=64.0)
    g.diag(609.8, 634.4, 737.2, 556.3, weight=64.0)
    g.hbar(133.7, 519.5, 386.9, weight=48.0)
    g.diag(317.1, 507.8, 341.8, 346.8, weight=48.0)
    g.vbar(339.7, -52.0, 346.8, weight=48.0)
    g.diag(331.7, 344.6, 281.3, 273.3, weight=48.0)
    g.diag(281.3, 273.3, 124.0, 66.4, weight=48.0)
    g.diag(376.3, 274.9, 530.2, 203.3, weight=96.0)
    g.vbar(564.7, 26.0, 436.3, weight=48.0)
    g.hbar(575.0, 757.8, 441.2, weight=48.0)
    g.vbar(772.9, 307.6, 458.9, weight=48.0)
    g.vbar(787.6, 29.2, 307.6, weight=48.0)
    g.hbar(731.4, 787.3, 38.0, weight=48.0)
    g.hbar(596.5, 763.9, 319.2, weight=92.0)
    g.hbar(593.6, 762.9, 204.2, weight=96.0)
    g.hbar(577.1, 749.8, 49.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_7bb8() -> Glyph:
    """箸 U+7BB8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7BB8", advance=1000, unicode=0x7BB8, note="箸：自动生成")
    g.diag(307.8, 711.0, 310.5, 731.3, weight=96.0)
    g.diag(310.5, 731.3, 254.5, 616.0, weight=96.0)
    g.hbar(254.5, 285.1, 610.8, weight=96.0)
    g.hbar(321.7, 511.4, 679.8, weight=96.0)
    g.dot(366.3, 602.3, w=96.0, h=116.4, slant=-14.0)
    g.diag(569.4, 802.0, 601.4, 762.6, weight=48.0)
    g.diag(601.4, 762.6, 467.9, 578.4, weight=48.0)
    g.hbar(589.7, 791.2, 711.6, weight=48.0)
    g.diag(606.4, 678.2, 693.3, 617.2, weight=48.0)
    g.diag(693.3, 617.2, 668.1, 569.5, weight=48.0)
    g.hbar(335.7, 622.3, 471.9, weight=48.0)
    g.diag(459.2, 574.3, 489.5, 533.3, weight=96.0)
    g.vbar(487.0, 387.5, 533.3, weight=96.0)
    g.diag(484.5, 387.5, 469.5, 367.5, weight=96.0)
    g.hbar(118.9, 893.0, 334.0, weight=48.0)
    g.diag(668.6, 606.0, 520.2, 392.4, weight=48.0)
    g.diag(520.2, 392.4, 92.0, 55.9, weight=48.0)
    g.vbar(380.0, -50.7, 242.7, weight=96.0)
    g.hbar(418.9, 586.7, 242.6, weight=48.0)
    g.vbar(602.4, 160.4, 261.1, weight=48.0)
    g.diag(618.0, 160.4, 644.1, -35.3, weight=48.0)
    g.diag(644.1, -35.3, 569.1, 9.5, weight=48.0)
    g.diag(424.6, 106.8, 436.3, 122.5, weight=96.0)
    g.hbar(436.3, 593.1, 124.6, weight=96.0)
    g.diag(419.6, -20.0, 436.1, -4.6, weight=96.0)
    g.hbar(436.1, 550.6, -0.8, weight=96.0)
    g.diag(550.6, 3.1, 559.4, -12.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_7bc4() -> Glyph:
    """範 U+7BC4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7BC4", advance=1000, unicode=0x7BC4, note="範：自动生成")
    g.diag(309.2, 772.4, 337.3, 733.1, weight=96.0)
    g.diag(337.3, 733.1, 197.9, 550.8, weight=96.0)
    g.dot(418.6, 692.1, w=96.0, h=124.8, slant=-14.0)
    g.dot(366.7, 605.5, w=96.0, h=81.7, slant=-14.0)
    g.diag(579.1, 797.0, 612.5, 757.6, weight=96.0)
    g.diag(612.5, 757.6, 495.2, 587.3, weight=96.0)
    g.hbar(621.1, 819.9, 724.5, weight=64.0)
    g.diag(618.3, 650.2, 695.9, 590.0, weight=56.0)
    g.hbar(231.7, 456.0, 464.1, weight=56.0)
    g.diag(187.9, 361.1, 257.2, 202.4, weight=76.0)
    g.diag(239.9, 342.0, 249.9, 362.0, weight=48.0)
    g.hbar(249.9, 490.6, 375.6, weight=48.0)
    g.vbar(464.2, 237.1, 389.1, weight=48.0)
    g.hbar(279.1, 404.0, 304.6, weight=48.0)
    g.hbar(271.8, 418.6, 239.4, weight=48.0)
    g.hbar(104.0, 475.2, 133.1, weight=76.0)
    g.diag(309.2, 566.3, 336.3, 348.9, weight=48.0)
    g.vbar(337.4, -52.0, 348.9, weight=48.0)
    g.diag(596.5, 458.7, 607.5, 449.8, weight=48.0)
    g.hbar(607.5, 770.5, 459.1, weight=48.0)
    g.diag(770.5, 468.4, 702.9, 262.6, weight=48.0)
    g.diag(702.9, 262.6, 636.6, 301.8, weight=48.0)
    g.diag(549.0, 461.4, 775.7, 158.4, weight=48.0)
    g.hbar(775.7, 881.0, 179.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_7bc9() -> Glyph:
    """築 U+7BC9 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7BC9", advance=1000, unicode=0x7BC9, note="築：自动生成")
    g.vbar(319.5, 715.0, 723.4, weight=96.0)
    g.diag(319.3, 723.4, 222.8, 575.8, weight=96.0)
    g.vbar(220.3, 521.1, 575.8, weight=96.0)
    g.hbar(319.8, 452.2, 685.7, weight=56.0)
    g.hbar(452.2, 500.9, 685.9, weight=56.0)
    g.diag(330.8, 656.1, 398.5, 534.0, weight=48.0)
    g.vbar(566.3, 749.8, 751.5, weight=96.0)
    g.diag(566.1, 749.8, 470.9, 583.7, weight=96.0)
    g.hbar(575.9, 759.7, 727.3, weight=56.0)
    g.diag(587.2, 697.9, 644.1, 632.7, weight=48.0)
    g.vbar(641.6, 581.9, 632.7, weight=48.0)
    g.hbar(280.4, 382.0, 500.6, weight=96.0)
    g.diag(382.0, 514.4, 407.7, 540.1, weight=96.0)
    g.diag(318.1, 479.7, 346.0, 413.8, weight=96.0)
    g.diag(346.0, 413.8, 322.7, 395.9, weight=96.0)
    g.diag(203.1, 257.9, 237.2, 332.5, weight=84.0)
    g.hbar(237.2, 452.1, 371.6, weight=84.0)
    g.diag(500.6, 547.2, 517.4, 521.5, weight=96.0)
    g.vbar(491.5, 370.5, 521.5, weight=96.0)
    g.diag(534.8, 529.8, 539.7, 538.6, weight=76.0)
    g.hbar(539.7, 615.9, 530.1, weight=76.0)
    g.diag(615.9, 521.7, 672.8, 436.4, weight=76.0)
    g.diag(672.8, 436.4, 771.7, 383.8, weight=76.0)
    g.vbar(776.6, 383.8, 467.9, weight=76.0)
    g.hbar(524.5, 612.9, 445.2, weight=48.0)
    g.hbar(137.9, 793.4, 247.1, weight=48.0)
    g.diag(444.7, 345.0, 484.3, 293.5, weight=96.0)
    g.vbar(477.2, -52.0, 293.5, weight=96.0)
    g.diag(438.1, 235.9, 159.7, 21.7, weight=48.0)
    g.diag(497.3, 241.4, 867.1, 50.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_7be4() -> Glyph:
    """篤 U+7BE4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7BE4", advance=1000, unicode=0x7BE4, note="篤：自动生成")
    g.vbar(315.2, 716.4, 721.4, weight=96.0)
    g.diag(315.6, 721.4, 229.7, 572.3, weight=96.0)
    g.vbar(231.6, 517.1, 572.3, weight=96.0)
    g.hbar(320.8, 471.4, 689.8, weight=56.0)
    g.hbar(471.4, 536.1, 684.1, weight=56.0)
    g.diag(294.4, 636.6, 386.0, 585.2, weight=48.0)
    g.diag(386.0, 585.2, 398.5, 564.1, weight=48.0)
    g.vbar(594.3, 738.6, 742.1, weight=96.0)
    g.diag(594.6, 742.1, 482.4, 543.1, weight=96.0)
    g.hbar(607.2, 806.3, 714.1, weight=96.0)
    g.diag(620.8, 665.8, 673.6, 617.0, weight=96.0)
    g.vbar(674.9, 566.1, 617.0, weight=96.0)
    g.hbar(323.2, 676.6, 528.5, weight=64.0)
    g.hbar(307.0, 322.5, 503.8, weight=64.0)
    g.diag(322.5, 506.5, 268.5, 234.5, weight=64.0)
    g.diag(268.5, 234.5, 295.6, 188.0, weight=64.0)
    g.vbar(396.9, 348.3, 398.4, weight=64.0)
    g.hbar(407.8, 586.4, 418.3, weight=64.0)
    g.diag(586.4, 438.2, 614.0, 377.0, weight=64.0)
    g.vbar(404.6, 315.2, 377.9, weight=64.0)
    g.hbar(411.6, 594.3, 333.3, weight=64.0)
    g.vbar(607.3, 351.4, 414.5, weight=64.0)
    g.diag(464.9, 478.5, 494.7, 453.5, weight=96.0)
    g.vbar(494.2, 280.4, 453.5, weight=96.0)
    g.diag(493.8, 280.4, 478.4, 259.2, weight=96.0)
    g.hbar(311.0, 467.4, 200.9, weight=64.0)
    g.hbar(467.4, 681.5, 174.8, weight=64.0)
    g.diag(681.5, 132.8, 714.4, -77.4, weight=64.0)
    g.diag(714.4, -77.4, 625.1, 59.6, weight=64.0)
    g.diag(266.9, 130.4, 168.7, -24.5, weight=96.0)
    g.diag(307.1, 147.0, 333.1, 69.8, weight=96.0)
    g.diag(333.1, 69.8, 406.1, 106.7, weight=96.0)
    g.diag(411.4, 200.8, 468.7, 77.4, weight=64.0)
    g.diag(544.9, 216.3, 623.0, 22.2, weight=64.0)
    return g
def g_cjk_unified_ideograph_7c21() -> Glyph:
    """簡 U+7C21 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7C21", advance=1000, unicode=0x7C21, note="簡：自动生成")
    g.diag(279.1, 758.4, 309.0, 716.0, weight=96.0)
    g.diag(309.0, 716.0, 164.9, 540.3, weight=96.0)
    g.hbar(300.5, 492.1, 662.1, weight=56.0)
    g.dot(371.3, 575.4, w=48.0, h=62.4, slant=-14.0)
    g.diag(568.5, 792.0, 600.6, 752.5, weight=96.0)
    g.diag(600.6, 752.5, 472.7, 565.7, weight=96.0)
    g.diag(597.1, 675.8, 602.0, 678.9, weight=48.0)
    g.hbar(602.0, 810.1, 694.2, weight=48.0)
    g.diag(599.1, 631.0, 683.7, 579.0, weight=48.0)
    g.diag(181.2, 488.3, 203.0, 325.3, weight=56.0)
    g.vbar(196.7, -57.0, 325.3, weight=56.0)
    g.hbar(243.4, 244.5, 469.7, weight=76.0)
    g.hbar(244.5, 407.2, 474.2, weight=76.0)
    g.vbar(392.3, 293.7, 478.8, weight=76.0)
    g.hbar(361.6, 377.4, 293.2, weight=76.0)
    g.diag(250.5, 359.9, 260.3, 374.4, weight=64.0)
    g.hbar(260.3, 331.1, 376.8, weight=64.0)
    g.diag(240.3, 271.2, 259.7, 284.0, weight=64.0)
    g.hbar(259.7, 337.6, 291.6, weight=64.0)
    g.diag(337.6, 299.3, 345.3, 291.6, weight=64.0)
    g.diag(532.9, 541.3, 576.7, 304.8, weight=48.0)
    g.diag(588.9, 521.9, 602.2, 511.7, weight=48.0)
    g.hbar(602.2, 729.0, 527.8, weight=48.0)
    g.vbar(743.0, 362.6, 543.9, weight=48.0)
    g.vbar(747.8, 78.6, 362.6, weight=48.0)
    g.diag(738.7, 78.6, 646.0, -11.1, weight=48.0)
    g.hbar(593.0, 701.0, 415.9, weight=64.0)
    g.diag(594.0, 321.1, 605.9, 333.0, weight=64.0)
    g.hbar(605.9, 727.1, 339.5, weight=64.0)
    g.diag(727.1, 346.0, 736.7, 337.4, weight=64.0)
    g.diag(368.8, 240.6, 398.6, 199.3, weight=48.0)
    g.vbar(392.4, -6.0, 199.3, weight=48.0)
    g.diag(413.6, 230.4, 519.7, 168.2, weight=48.0)
    g.diag(519.7, 168.2, 574.6, -35.6, weight=48.0)
    g.dot(468.6, 130.0, w=76.0, h=98.8, slant=-14.0)
    g.dot(472.7, 27.6, w=84.0, h=109.2, slant=-14.0)
    return g
def g_cjk_unified_ideograph_7c3f() -> Glyph:
    """簿 U+7C3F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7C3F", advance=1000, unicode=0x7C3F, note="簿：自动生成")
    g.diag(301.8, 699.7, 309.4, 725.7, weight=96.0)
    g.diag(309.4, 725.7, 182.7, 529.3, weight=96.0)
    g.hbar(305.5, 449.3, 675.0, weight=96.0)
    g.hbar(449.3, 479.1, 683.3, weight=96.0)
    g.dot(348.0, 578.6, w=96.0, h=121.7, slant=-14.0)
    g.diag(561.6, 724.0, 567.4, 747.5, weight=96.0)
    g.diag(567.4, 747.5, 488.1, 629.7, weight=96.0)
    g.hbar(564.8, 756.3, 705.4, weight=96.0)
    g.diag(602.1, 671.7, 654.0, 620.8, weight=48.0)
    g.diag(654.0, 620.8, 669.4, 555.1, weight=48.0)
    g.diag(182.1, 534.0, 308.2, 420.8, weight=96.0)
    g.dot(175.3, 310.2, w=96.0, h=124.8, slant=-14.0)
    g.diag(154.6, -33.6, 140.8, 36.9, weight=96.0)
    g.diag(140.8, 36.9, 261.0, 232.9, weight=96.0)
    g.diag(261.0, 232.9, 222.7, 274.5, weight=96.0)
    g.diag(387.7, 537.3, 442.2, 494.9, weight=56.0)
    g.hbar(442.2, 636.7, 516.3, weight=56.0)
    g.diag(636.7, 537.6, 672.1, 573.1, weight=56.0)
    g.vbar(380.7, 264.7, 426.6, weight=96.0)
    g.diag(411.5, 264.7, 426.1, 250.3, weight=96.0)
    g.hbar(387.6, 738.1, 432.2, weight=56.0)
    g.diag(738.1, 445.2, 627.4, 287.5, weight=56.0)
    g.hbar(505.4, 571.9, 355.6, weight=56.0)
    g.diag(571.9, 369.6, 606.8, 313.9, weight=56.0)
    g.hbar(425.5, 568.9, 276.6, weight=56.0)
    g.diag(568.9, 293.6, 597.1, 266.3, weight=56.0)
    g.vbar(508.9, 216.8, 594.7, weight=96.0)
    g.diag(710.1, 584.7, 793.8, 537.7, weight=96.0)
    g.diag(793.8, 537.7, 739.5, 458.6, weight=96.0)
    g.hbar(247.9, 885.0, 183.7, weight=64.0)
    g.vbar(589.7, 41.9, 273.1, weight=48.0)
    g.hbar(501.3, 587.7, 27.7, weight=48.0)
    g.diag(407.3, 136.9, 510.9, -9.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_7c4d() -> Glyph:
    """籍 U+7C4D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7C4D", advance=1000, unicode=0x7C4D, note="籍：自动生成")
    g.diag(315.5, 773.8, 342.6, 733.9, weight=96.0)
    g.diag(342.6, 733.9, 193.9, 564.0, weight=96.0)
    g.dot(410.9, 679.9, w=96.0, h=124.8, slant=-14.0)
    g.dot(384.5, 593.7, w=96.0, h=85.5, slant=-14.0)
    g.diag(577.1, 792.0, 603.8, 756.7, weight=96.0)
    g.diag(603.8, 756.7, 483.2, 587.9, weight=96.0)
    g.hbar(602.9, 780.2, 711.0, weight=48.0)
    g.diag(643.2, 651.2, 726.5, 607.1, weight=48.0)
    g.hbar(201.5, 425.7, 462.4, weight=64.0)
    g.hbar(197.7, 422.8, 375.7, weight=64.0)
    g.hbar(96.2, 432.4, 272.8, weight=48.0)
    g.diag(287.8, 566.9, 312.4, 394.2, weight=48.0)
    g.vbar(310.1, -39.5, 394.2, weight=48.0)
    g.diag(298.3, 256.5, 260.7, 204.8, weight=48.0)
    g.diag(260.7, 204.8, 108.6, 29.4, weight=48.0)
    g.dot(374.5, 181.3, w=96.0, h=94.9, slant=-14.0)
    g.hbar(479.4, 786.9, 460.5, weight=96.0)
    g.diag(513.8, 533.3, 546.4, 499.8, weight=96.0)
    g.vbar(551.2, 347.5, 499.8, weight=96.0)
    g.diag(556.0, 347.5, 546.4, 339.8, weight=96.0)
    g.diag(665.2, 577.4, 695.9, 542.0, weight=92.0)
    g.diag(695.9, 542.0, 673.8, 375.3, weight=92.0)
    g.diag(673.8, 375.3, 656.6, 353.2, weight=92.0)
    g.hbar(469.8, 878.8, 322.1, weight=96.0)
    g.diag(500.4, 242.1, 528.4, 215.4, weight=48.0)
    g.vbar(524.5, -20.4, 215.4, weight=48.0)
    g.diag(548.3, 230.6, 560.8, 222.9, weight=48.0)
    g.hbar(560.8, 703.0, 237.8, weight=48.0)
    g.diag(703.0, 252.7, 731.0, 151.7, weight=48.0)
    g.vbar(735.0, -52.0, 151.7, weight=48.0)
    g.diag(554.1, 115.7, 563.3, 126.0, weight=76.0)
    g.hbar(563.3, 666.2, 129.5, weight=76.0)
    g.hbar(545.5, 693.0, 22.7, weight=84.0)
    return g
def g_cjk_unified_ideograph_7c60() -> Glyph:
    """籠 U+7C60 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7C60", advance=1000, unicode=0x7C60, note="籠：自动生成")
    g.diag(334.2, 762.9, 362.4, 721.8, weight=96.0)
    g.diag(362.4, 721.8, 236.2, 559.1, weight=96.0)
    g.hbar(366.2, 529.3, 687.2, weight=96.0)
    g.dot(408.0, 605.2, w=64.0, h=75.2, slant=-14.0)
    g.diag(605.9, 792.0, 635.9, 755.1, weight=96.0)
    g.diag(635.9, 755.1, 526.4, 596.0, weight=96.0)
    g.hbar(637.0, 832.0, 710.5, weight=96.0)
    g.diag(642.8, 642.6, 697.1, 614.4, weight=76.0)
    g.diag(697.1, 614.4, 712.7, 590.1, weight=76.0)
    g.dot(372.0, 528.0, w=64.0, h=82.5, slant=-14.0)
    g.hbar(239.1, 499.2, 467.4, weight=96.0)
    g.dot(301.2, 399.5, w=84.0, h=67.9, slant=-14.0)
    g.diag(415.7, 461.1, 425.9, 426.5, weight=96.0)
    g.diag(425.9, 426.5, 403.1, 358.2, weight=96.0)
    g.hbar(108.1, 514.7, 324.7, weight=96.0)
    g.diag(266.3, 261.2, 289.4, 236.6, weight=96.0)
    g.diag(289.4, 236.6, 247.8, -47.4, weight=96.0)
    g.diag(309.9, 238.8, 320.4, 252.2, weight=48.0)
    g.diag(320.4, 252.2, 418.0, 151.9, weight=48.0)
    g.vbar(421.3, -62.9, 151.9, weight=48.0)
    g.hbar(344.9, 424.6, -48.9, weight=48.0)
    g.dot(342.9, 168.5, w=56.0, h=72.8, slant=-14.0)
    g.diag(295.4, 75.8, 302.3, 87.3, weight=64.0)
    g.hbar(302.3, 382.7, 90.3, weight=64.0)
    g.diag(620.5, 497.0, 629.3, 506.7, weight=96.0)
    g.hbar(629.3, 769.9, 521.7, weight=96.0)
    g.diag(572.9, 582.4, 602.0, 549.4, weight=84.0)
    g.diag(602.0, 549.4, 572.7, 418.2, weight=84.0)
    g.hbar(572.7, 764.8, 426.3, weight=84.0)
    g.diag(764.8, 434.3, 699.1, 344.6, weight=84.0)
    g.hbar(586.5, 757.3, 309.2, weight=48.0)
    g.diag(532.2, 326.2, 780.9, 73.0, weight=48.0)
    g.hbar(780.9, 901.9, 99.6, weight=48.0)
    g.hbar(581.7, 738.9, 240.3, weight=48.0)
    g.diag(574.9, 153.4, 580.0, 158.6, weight=48.0)
    g.hbar(580.0, 748.6, 164.8, weight=48.0)
    g.hbar(575.8, 755.4, 89.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_7c89() -> Glyph:
    """粉 U+7C89 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7C89", advance=1000, unicode=0x7C89, note="粉：自动生成")
    g.diag(152.7, 567.2, 233.1, 405.8, weight=64.0)
    g.diag(420.7, 606.5, 442.7, 579.7, weight=48.0)
    g.diag(442.7, 579.7, 324.9, 485.8, weight=48.0)
    g.hbar(58.0, 390.6, 384.3, weight=96.0)
    g.diag(390.6, 411.9, 439.8, 388.1, weight=96.0)
    g.vbar(273.3, -47.1, 747.1, weight=48.0)
    g.diag(274.9, 369.8, 89.6, 68.4, weight=48.0)
    g.vbar(89.6, 68.4, 76.3, weight=48.0)
    g.diag(321.3, 299.4, 411.1, 214.1, weight=48.0)
    g.diag(475.1, 559.0, 550.4, 496.9, weight=96.0)
    g.diag(550.4, 496.9, 439.0, 304.4, weight=96.0)
    g.diag(556.6, 724.2, 947.0, 382.5, weight=96.0)
    g.hbar(471.4, 769.5, 320.1, weight=92.0)
    g.diag(769.5, 333.4, 665.0, -0.1, weight=92.0)
    g.diag(665.0, -0.1, 519.9, 85.7, weight=92.0)
    g.diag(544.1, 276.3, 576.0, 253.1, weight=64.0)
    g.diag(576.0, 253.1, 418.5, 14.6, weight=64.0)
    g.hbar(313.3, 418.5, 1.0, weight=64.0)
    return g
def g_cjk_unified_ideograph_7c92() -> Glyph:
    """粒 U+7C92 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7C92", advance=1000, unicode=0x7C92, note="粒：自动生成")
    g.diag(131.7, 577.0, 265.0, 484.3, weight=84.0)
    g.diag(404.4, 633.8, 426.3, 609.9, weight=48.0)
    g.diag(426.3, 609.9, 318.3, 512.2, weight=48.0)
    g.hbar(60.0, 464.1, 401.8, weight=96.0)
    g.vbar(267.5, 499.8, 780.1, weight=48.0)
    g.vbar(280.4, -45.1, 499.8, weight=48.0)
    g.diag(266.4, 373.8, 58.0, 76.3, weight=48.0)
    g.diag(318.8, 304.3, 419.0, 247.9, weight=84.0)
    g.hbar(326.6, 419.0, 246.3, weight=84.0)
    g.diag(566.7, 732.3, 667.2, 675.6, weight=96.0)
    g.diag(667.2, 675.6, 719.5, 538.0, weight=96.0)
    g.hbar(464.1, 813.5, 476.0, weight=96.0)
    g.diag(455.6, 387.5, 563.4, 140.1, weight=96.0)
    g.diag(689.3, 451.9, 735.9, 352.1, weight=96.0)
    g.diag(735.9, 352.1, 642.3, 134.1, weight=96.0)
    g.hbar(320.0, 927.0, 102.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_7c97() -> Glyph:
    """粗 U+7C97 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7C97", advance=1000, unicode=0x7C97, note="粗：自动生成")
    g.dot(208.2, 520.4, w=84.0, h=109.2, slant=-14.0)
    g.diag(432.6, 604.3, 451.0, 577.1, weight=48.0)
    g.diag(451.0, 577.1, 381.2, 494.7, weight=48.0)
    g.hbar(78.8, 482.1, 380.8, weight=48.0)
    g.vbar(305.8, 492.5, 772.0, weight=48.0)
    g.vbar(314.5, -52.0, 492.5, weight=48.0)
    g.diag(305.6, 361.0, 73.0, 78.9, weight=48.0)
    g.diag(354.1, 303.8, 356.1, 302.7, weight=96.0)
    g.diag(356.1, 302.7, 437.5, 226.2, weight=96.0)
    g.diag(530.5, 604.3, 554.9, 498.0, weight=48.0)
    g.vbar(565.3, 129.7, 498.0, weight=48.0)
    g.diag(575.7, 129.7, 552.8, 101.2, weight=48.0)
    g.diag(590.6, 589.8, 605.2, 580.1, weight=48.0)
    g.hbar(605.2, 739.2, 599.4, weight=48.0)
    g.diag(739.2, 618.8, 763.2, 506.4, weight=48.0)
    g.vbar(759.0, 144.7, 506.4, weight=48.0)
    g.diag(754.8, 144.7, 732.2, 129.3, weight=48.0)
    g.diag(599.4, 410.4, 613.0, 428.6, weight=96.0)
    g.hbar(613.0, 706.0, 432.1, weight=96.0)
    g.diag(598.4, 261.1, 613.4, 279.6, weight=96.0)
    g.hbar(613.4, 706.0, 280.1, weight=96.0)
    g.hbar(406.5, 927.0, 77.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_7c98() -> Glyph:
    """粘 U+7C98 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7C98", advance=1000, unicode=0x7C98, note="粘：自动生成")
    g.diag(183.0, 589.2, 325.4, 489.4, weight=84.0)
    g.diag(480.8, 643.7, 500.0, 614.4, weight=48.0)
    g.diag(500.0, 614.4, 379.3, 525.8, weight=48.0)
    g.hbar(117.3, 507.1, 401.3, weight=48.0)
    g.vbar(330.2, 503.7, 782.0, weight=48.0)
    g.vbar(338.8, -52.0, 503.7, weight=48.0)
    g.diag(326.5, 382.9, 101.2, 65.1, weight=48.0)
    g.diag(373.8, 330.5, 492.0, 263.5, weight=48.0)
    g.diag(634.3, 732.5, 687.5, 689.6, weight=96.0)
    g.vbar(683.0, 309.4, 689.6, weight=96.0)
    g.diag(678.6, 309.4, 660.5, 284.2, weight=96.0)
    g.hbar(715.1, 898.8, 509.9, weight=96.0)
    g.diag(542.4, 263.8, 534.8, 248.8, weight=48.0)
    g.vbar(565.4, 52.2, 248.8, weight=48.0)
    g.hbar(549.7, 873.0, 266.7, weight=48.0)
    g.diag(873.0, 277.6, 789.6, 110.5, weight=48.0)
    g.hbar(587.5, 828.2, 84.4, weight=48.0)
    g.vbar(828.6, 92.0, 123.1, weight=48.0)
    return g
def g_cjk_unified_ideograph_7cbe() -> Glyph:
    """精 U+7CBE —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7CBE", advance=1000, unicode=0x7CBE, note="精：自动生成")
    g.dot(180.9, 514.3, w=76.0, h=97.8, slant=-14.0)
    g.hbar(419.4, 450.6, 584.3, weight=84.0)
    g.diag(419.4, 587.4, 349.8, 503.7, weight=84.0)
    g.hbar(85.6, 416.4, 395.8, weight=96.0)
    g.vbar(269.6, 467.4, 741.7, weight=48.0)
    g.vbar(280.7, -52.0, 467.4, weight=48.0)
    g.diag(269.1, 373.6, 76.5, 65.0, weight=48.0)
    g.dot(362.4, 264.7, w=96.0, h=98.4, slant=-14.0)
    g.hbar(488.0, 798.6, 632.2, weight=84.0)
    g.hbar(495.0, 761.3, 524.8, weight=84.0)
    g.diag(586.8, 782.0, 633.2, 743.7, weight=96.0)
    g.vbar(629.1, 458.3, 743.7, weight=96.0)
    g.diag(625.1, 458.3, 610.0, 437.1, weight=96.0)
    g.hbar(432.5, 908.5, 411.4, weight=84.0)
    g.diag(503.1, 329.2, 536.9, 296.6, weight=64.0)
    g.diag(536.9, 296.6, 494.0, -45.9, weight=64.0)
    g.hbar(561.6, 566.9, 314.1, weight=96.0)
    g.hbar(566.9, 704.0, 319.6, weight=96.0)
    g.diag(704.0, 326.0, 796.6, -72.0, weight=96.0)
    g.diag(796.6, -72.0, 645.3, 5.5, weight=96.0)
    g.hbar(555.5, 676.5, 210.7, weight=64.0)
    g.hbar(550.5, 683.6, 117.4, weight=76.0)
    return g
def g_cjk_unified_ideograph_7cd6() -> Glyph:
    """糖 U+7CD6 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7CD6", advance=1000, unicode=0x7CD6, note="糖：自动生成")
    g.diag(114.8, 568.8, 239.2, 491.3, weight=64.0)
    g.diag(365.9, 623.6, 382.9, 599.7, weight=48.0)
    g.diag(382.9, 599.7, 284.9, 517.1, weight=48.0)
    g.hbar(56.0, 436.8, 400.5, weight=96.0)
    g.vbar(238.3, 483.2, 759.1, weight=48.0)
    g.vbar(248.2, -58.1, 483.2, weight=48.0)
    g.diag(241.6, 373.4, 53.0, 87.4, weight=48.0)
    g.diag(278.2, 319.8, 355.0, 249.9, weight=48.0)
    g.diag(572.2, 783.1, 649.0, 743.2, weight=76.0)
    g.diag(649.0, 743.2, 684.4, 658.0, weight=76.0)
    g.hbar(516.4, 821.4, 628.1, weight=96.0)
    g.vbar(480.5, 480.9, 613.4, weight=56.0)
    g.diag(465.7, 480.9, 376.8, 72.1, weight=56.0)
    g.diag(376.8, 72.1, 265.9, 13.1, weight=56.0)
    g.hbar(498.3, 812.1, 471.1, weight=48.0)
    g.vbar(790.3, 329.6, 485.9, weight=48.0)
    g.diag(768.5, 329.6, 748.7, 311.0, weight=48.0)
    g.hbar(485.6, 927.0, 372.9, weight=48.0)
    g.hbar(529.4, 783.2, 276.6, weight=48.0)
    g.vbar(781.7, 294.3, 314.3, weight=48.0)
    g.diag(620.9, 573.3, 663.8, 529.7, weight=96.0)
    g.vbar(654.4, 179.1, 529.7, weight=96.0)
    g.vbar(547.2, -40.7, 128.2, weight=64.0)
    g.hbar(544.2, 764.3, 142.2, weight=48.0)
    g.diag(764.3, 168.2, 805.1, 130.8, weight=48.0)
    g.diag(805.1, 130.8, 748.8, 31.3, weight=48.0)
    g.hbar(576.5, 790.8, -2.2, weight=48.0)
    g.vbar(788.3, 16.7, 40.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_7ce7() -> Glyph:
    """糧 U+7CE7 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7CE7", advance=1000, unicode=0x7CE7, note="糧：自动生成")
    g.diag(134.5, 581.9, 205.4, 493.7, weight=64.0)
    g.diag(387.5, 629.8, 408.5, 603.9, weight=48.0)
    g.diag(408.5, 603.9, 350.1, 521.5, weight=48.0)
    g.hbar(67.4, 377.9, 410.3, weight=48.0)
    g.vbar(261.8, 485.4, 764.9, weight=48.0)
    g.vbar(272.4, -44.9, 485.4, weight=48.0)
    g.diag(263.8, 383.5, 216.5, 314.9, weight=48.0)
    g.diag(216.5, 314.9, 53.0, 110.4, weight=48.0)
    g.dot(353.9, 292.4, w=76.0, h=98.8, slant=-14.0)
    g.vbar(518.3, 506.1, 689.2, weight=48.0)
    g.hbar(522.6, 614.8, 692.3, weight=48.0)
    g.hbar(614.8, 788.8, 697.0, weight=48.0)
    g.vbar(756.8, 528.2, 701.5, weight=48.0)
    g.diag(556.1, 599.1, 569.1, 612.0, weight=64.0)
    g.hbar(569.1, 687.4, 617.1, weight=64.0)
    g.hbar(572.4, 690.8, 534.6, weight=48.0)
    g.diag(690.8, 546.7, 698.9, 533.9, weight=48.0)
    g.hbar(426.8, 927.0, 455.4, weight=64.0)
    g.vbar(479.9, 172.6, 363.4, weight=48.0)
    g.hbar(471.8, 601.5, 370.0, weight=48.0)
    g.hbar(601.5, 819.5, 378.0, weight=48.0)
    g.diag(819.5, 385.2, 755.5, 193.7, weight=48.0)
    g.hbar(544.6, 714.2, 289.1, weight=56.0)
    g.hbar(532.2, 723.8, 209.1, weight=64.0)
    g.diag(598.3, 357.6, 627.4, 337.1, weight=96.0)
    g.vbar(624.1, 49.1, 337.1, weight=96.0)
    g.diag(620.8, 49.1, 609.8, 33.7, weight=96.0)
    g.hbar(508.2, 743.0, 113.2, weight=84.0)
    g.hbar(378.8, 897.3, 2.1, weight=84.0)
    return g
def g_cjk_unified_ideograph_7d0b() -> Glyph:
    """紋 U+7D0B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7D0B", advance=1000, unicode=0x7D0B, note="紋：自动生成")
    g.diag(231.5, 750.2, 207.5, 624.3, weight=48.0)
    g.diag(207.5, 624.3, 123.3, 441.4, weight=48.0)
    g.hbar(123.3, 266.7, 442.5, weight=48.0)
    g.diag(340.1, 597.9, 302.0, 483.1, weight=48.0)
    g.diag(302.0, 483.1, 168.1, 259.3, weight=48.0)
    g.hbar(168.1, 324.5, 286.7, weight=48.0)
    g.diag(314.6, 331.5, 360.4, 300.5, weight=48.0)
    g.hbar(333.0, 360.4, 298.9, weight=48.0)
    g.diag(156.0, 150.0, 127.5, 45.7, weight=96.0)
    g.diag(127.5, 45.7, 146.2, -15.2, weight=96.0)
    g.diag(188.7, 230.9, 287.8, 56.9, weight=96.0)
    g.diag(279.5, 257.5, 386.3, 88.7, weight=96.0)
    g.diag(527.9, 724.8, 629.5, 663.6, weight=96.0)
    g.diag(629.5, 663.6, 679.9, 516.1, weight=96.0)
    g.hbar(354.6, 811.1, 485.1, weight=96.0)
    g.diag(619.2, 430.4, 718.6, 350.9, weight=96.0)
    g.diag(718.6, 350.9, 293.9, 52.9, weight=96.0)
    g.diag(392.0, 290.9, 554.7, 213.1, weight=64.0)
    g.diag(554.7, 213.1, 942.0, 20.4, weight=64.0)
    return g
def g_cjk_unified_ideograph_7d21() -> Glyph:
    """紡 U+7D21 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7D21", advance=1000, unicode=0x7D21, note="紡：自动生成")
    g.diag(232.2, 787.0, 210.3, 657.9, weight=48.0)
    g.diag(210.3, 657.9, 106.7, 429.3, weight=48.0)
    g.hbar(106.7, 267.8, 443.1, weight=48.0)
    g.diag(328.9, 598.0, 292.9, 484.8, weight=48.0)
    g.diag(292.9, 484.8, 154.0, 249.2, weight=48.0)
    g.hbar(154.0, 341.5, 284.3, weight=48.0)
    g.diag(326.9, 332.3, 375.6, 308.0, weight=48.0)
    g.hbar(346.5, 375.6, 304.7, weight=48.0)
    g.dot(100.3, 42.9, w=96.0, h=124.8, slant=-14.0)
    g.diag(201.8, 224.5, 285.9, 27.8, weight=92.0)
    g.diag(279.5, 267.8, 398.6, 102.1, weight=64.0)
    g.diag(548.3, 764.2, 686.3, 650.1, weight=96.0)
    g.hbar(356.5, 599.5, 492.3, weight=96.0)
    g.hbar(599.5, 936.1, 511.5, weight=96.0)
    g.diag(620.9, 332.9, 713.0, 173.0, weight=64.0)
    g.diag(713.0, 173.0, 652.4, -66.2, weight=64.0)
    g.diag(652.4, -66.2, 533.1, 12.5, weight=64.0)
    g.diag(589.6, 445.9, 531.6, 295.6, weight=96.0)
    g.diag(531.6, 295.6, 311.9, -20.4, weight=96.0)
    g.diag(311.9, -20.4, 272.3, 47.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_7d22() -> Glyph:
    """索 U+7D22 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7D22", advance=1000, unicode=0x7D22, note="索：自动生成")
    g.hbar(370.0, 682.2, 664.2, weight=96.0)
    g.diag(682.2, 680.9, 726.2, 586.9, weight=96.0)
    g.diag(520.0, 690.9, 543.1, 753.4, weight=96.0)
    g.vbar(533.7, 564.4, 753.4, weight=96.0)
    g.diag(524.3, 564.4, 506.5, 542.6, weight=96.0)
    g.diag(253.1, 524.5, 185.9, 349.7, weight=96.0)
    g.hbar(280.9, 436.9, 502.2, weight=96.0)
    g.hbar(436.9, 860.3, 524.3, weight=96.0)
    g.diag(860.3, 542.4, 770.7, 431.8, weight=96.0)
    g.diag(481.8, 497.6, 505.7, 472.0, weight=48.0)
    g.diag(505.7, 472.0, 385.6, 333.9, weight=48.0)
    g.hbar(385.6, 514.6, 329.0, weight=48.0)
    g.diag(612.4, 430.8, 550.7, 343.5, weight=48.0)
    g.vbar(530.7, 247.5, 343.5, weight=48.0)
    g.hbar(510.8, 659.7, 242.6, weight=48.0)
    g.diag(635.4, 256.8, 707.4, 217.1, weight=48.0)
    g.diag(707.4, 217.1, 720.3, 182.5, weight=48.0)
    g.diag(503.6, 196.3, 546.9, 166.2, weight=48.0)
    g.diag(546.9, 166.2, 508.6, -56.2, weight=48.0)
    g.hbar(399.7, 508.6, -32.3, weight=48.0)
    g.diag(389.9, 167.7, 331.4, 48.9, weight=96.0)
    g.diag(331.4, 48.9, 362.2, -17.1, weight=96.0)
    g.diag(698.0, 151.2, 797.5, -33.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_7d2b() -> Glyph:
    """紫 U+7D2B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7D2B", advance=1000, unicode=0x7D2B, note="紫：自动生成")
    g.diag(336.6, 730.7, 378.0, 698.9, weight=84.0)
    g.vbar(374.5, 502.5, 698.9, weight=84.0)
    g.diag(370.9, 502.5, 362.1, 494.6, weight=84.0)
    g.diag(401.2, 586.7, 423.4, 613.3, weight=84.0)
    g.hbar(423.4, 536.8, 616.5, weight=84.0)
    g.diag(210.2, 608.3, 245.5, 575.9, weight=96.0)
    g.diag(245.5, 575.9, 260.2, 479.9, weight=96.0)
    g.diag(260.2, 479.9, 246.4, 466.2, weight=96.0)
    g.diag(215.7, 452.7, 156.1, 410.5, weight=84.0)
    g.hbar(156.1, 468.0, 452.6, weight=84.0)
    g.hbar(621.7, 734.4, 693.4, weight=96.0)
    g.diag(734.4, 668.0, 600.1, 584.8, weight=96.0)
    g.diag(600.1, 584.8, 596.2, 574.0, weight=96.0)
    g.diag(550.2, 767.0, 572.7, 670.1, weight=84.0)
    g.diag(572.7, 670.1, 647.1, 471.5, weight=84.0)
    g.hbar(647.1, 835.6, 469.7, weight=84.0)
    g.diag(835.6, 467.8, 855.9, 599.5, weight=84.0)
    g.diag(440.0, 476.1, 456.4, 444.3, weight=48.0)
    g.diag(456.4, 444.3, 334.9, 304.3, weight=48.0)
    g.hbar(334.9, 473.9, 305.6, weight=48.0)
    g.diag(600.2, 454.7, 540.6, 355.6, weight=48.0)
    g.diag(540.6, 355.6, 376.3, 186.8, weight=48.0)
    g.hbar(376.3, 650.5, 207.6, weight=48.0)
    g.diag(611.9, 295.7, 674.6, 231.1, weight=48.0)
    g.diag(674.6, 231.1, 661.1, 212.4, weight=48.0)
    g.diag(486.4, 182.3, 529.5, 148.8, weight=48.0)
    g.diag(529.5, 148.8, 494.1, -56.9, weight=48.0)
    g.diag(494.1, -56.9, 405.2, -15.8, weight=48.0)
    g.diag(365.9, 169.2, 231.7, -26.6, weight=96.0)
    g.diag(670.6, 165.2, 784.3, -17.8, weight=84.0)
    return g
def g_cjk_unified_ideograph_7d2f() -> Glyph:
    """累 U+7D2F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7D2F", advance=1000, unicode=0x7D2F, note="累：自动生成")
    g.diag(244.8, 729.9, 329.6, 481.8, weight=48.0)
    g.hbar(292.3, 612.6, 694.5, weight=48.0)
    g.diag(612.6, 660.0, 669.8, 505.5, weight=48.0)
    g.hbar(379.2, 602.6, 630.2, weight=76.0)
    g.diag(465.0, 716.5, 489.8, 694.8, weight=96.0)
    g.vbar(490.4, 570.7, 694.8, weight=96.0)
    g.diag(490.9, 570.7, 476.4, 549.0, weight=96.0)
    g.hbar(350.2, 443.9, 510.3, weight=48.0)
    g.hbar(443.9, 628.4, 535.1, weight=48.0)
    g.diag(449.5, 496.2, 471.0, 469.6, weight=48.0)
    g.diag(471.0, 469.6, 327.1, 340.3, weight=48.0)
    g.hbar(327.1, 450.6, 331.4, weight=48.0)
    g.hbar(450.6, 478.5, 326.2, weight=48.0)
    g.diag(602.6, 452.8, 538.6, 362.7, weight=48.0)
    g.diag(538.6, 362.7, 485.2, 256.5, weight=48.0)
    g.hbar(485.2, 656.0, 250.6, weight=48.0)
    g.diag(656.0, 244.8, 668.7, 236.7, weight=48.0)
    g.diag(627.4, 312.2, 733.9, 199.5, weight=48.0)
    g.diag(483.6, 194.3, 525.4, 163.3, weight=48.0)
    g.diag(525.4, 163.3, 493.2, -59.0, weight=48.0)
    g.diag(493.2, -59.0, 394.7, -13.6, weight=48.0)
    g.diag(299.6, 115.7, 205.5, -43.6, weight=96.0)
    g.diag(650.1, 135.3, 814.5, -38.4, weight=92.0)
    return g
def g_cjk_unified_ideograph_7d33() -> Glyph:
    """紳 U+7D33 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7D33", advance=1000, unicode=0x7D33, note="紳：自动生成")
    g.diag(277.4, 767.3, 307.6, 722.0, weight=48.0)
    g.diag(307.6, 722.0, 185.3, 500.4, weight=48.0)
    g.hbar(185.3, 310.3, 512.3, weight=48.0)
    g.diag(361.0, 628.4, 330.3, 529.0, weight=48.0)
    g.diag(330.3, 529.0, 209.7, 321.4, weight=48.0)
    g.hbar(209.7, 351.9, 346.4, weight=48.0)
    g.vbar(353.2, 371.4, 378.8, weight=48.0)
    g.dot(376.0, 390.5, w=48.0, h=62.4, slant=-14.0)
    g.diag(131.0, 218.3, 198.6, 65.3, weight=96.0)
    g.diag(254.0, 244.6, 315.0, 147.9, weight=64.0)
    g.dot(385.4, 247.8, w=64.0, h=83.2, slant=-14.0)
    g.diag(455.7, 546.7, 537.4, 272.7, weight=48.0)
    g.hbar(515.8, 641.8, 535.9, weight=48.0)
    g.diag(641.8, 541.1, 785.9, 475.6, weight=48.0)
    g.vbar(790.1, 310.9, 475.6, weight=48.0)
    g.hbar(756.1, 794.4, 312.9, weight=48.0)
    g.hbar(572.1, 744.8, 425.7, weight=92.0)
    g.hbar(551.5, 764.5, 316.8, weight=92.0)
    g.hbar(609.7, 633.1, 784.2, weight=48.0)
    g.diag(633.1, 781.4, 655.6, 599.2, weight=48.0)
    g.vbar(656.6, -52.0, 599.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_7d79() -> Glyph:
    """絹 U+7D79 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7D79", advance=1000, unicode=0x7D79, note="絹：自动生成")
    g.diag(320.3, 787.0, 298.9, 672.0, weight=48.0)
    g.diag(298.9, 672.0, 195.5, 457.3, weight=48.0)
    g.hbar(195.5, 358.5, 469.2, weight=48.0)
    g.diag(407.3, 597.4, 365.1, 475.6, weight=48.0)
    g.diag(365.1, 475.6, 241.1, 266.4, weight=48.0)
    g.hbar(241.1, 414.8, 297.6, weight=48.0)
    g.diag(412.2, 351.5, 442.9, 323.0, weight=76.0)
    g.diag(442.9, 323.0, 431.0, 302.5, weight=76.0)
    g.diag(120.3, 152.3, 192.5, 52.7, weight=96.0)
    g.hbar(192.5, 291.8, 53.2, weight=96.0)
    g.vbar(297.0, 73.7, 243.0, weight=84.0)
    g.diag(347.5, 268.9, 441.8, 125.0, weight=64.0)
    g.vbar(559.1, 690.3, 707.7, weight=48.0)
    g.vbar(582.5, 526.0, 690.3, weight=48.0)
    g.hbar(569.3, 862.8, 718.1, weight=48.0)
    g.diag(862.8, 737.3, 786.0, 603.6, weight=48.0)
    g.diag(622.0, 540.9, 634.5, 553.4, weight=48.0)
    g.hbar(634.5, 823.7, 583.6, weight=48.0)
    g.vbar(581.2, 295.3, 422.8, weight=56.0)
    g.vbar(558.8, -23.7, 295.3, weight=56.0)
    g.diag(609.6, 419.7, 808.8, 286.0, weight=96.0)
    g.diag(808.8, 286.0, 972.0, -72.0, weight=96.0)
    g.hbar(732.0, 972.0, -39.5, weight=96.0)
    g.hbar(608.4, 808.8, 302.2, weight=84.0)
    g.hbar(602.1, 814.2, 191.5, weight=92.0)
    return g
def g_cjk_unified_ideograph_7dad() -> Glyph:
    """維 U+7DAD —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7DAD", advance=1000, unicode=0x7DAD, note="維：自动生成")
    g.diag(234.1, 787.9, 217.2, 672.2, weight=48.0)
    g.diag(217.2, 672.2, 125.6, 462.9, weight=48.0)
    g.hbar(125.6, 263.6, 471.9, weight=48.0)
    g.diag(328.7, 615.1, 296.5, 506.9, weight=48.0)
    g.diag(296.5, 506.9, 163.1, 280.6, weight=48.0)
    g.hbar(163.1, 319.8, 308.4, weight=48.0)
    g.diag(319.8, 336.2, 324.6, 331.4, weight=48.0)
    g.diag(321.6, 387.4, 368.3, 319.2, weight=48.0)
    g.dot(106.6, 80.3, w=96.0, h=124.8, slant=-14.0)
    g.dot(239.2, 141.8, w=96.0, h=94.0, slant=-14.0)
    g.dot(344.4, 196.2, w=76.0, h=98.8, slant=-14.0)
    g.diag(526.9, 792.0, 510.5, 672.6, weight=48.0)
    g.diag(510.5, 672.6, 382.6, 422.9, weight=48.0)
    g.vbar(483.7, -62.0, 510.4, weight=48.0)
    g.dot(692.7, 663.9, w=96.0, h=124.8, slant=-14.0)
    g.hbar(556.4, 839.1, 532.8, weight=96.0)
    g.hbar(584.9, 816.7, 388.4, weight=96.0)
    g.hbar(584.9, 814.7, 264.4, weight=96.0)
    g.diag(670.3, 495.1, 701.8, 469.7, weight=96.0)
    g.vbar(701.3, 147.4, 469.7, weight=96.0)
    g.diag(700.8, 147.4, 684.5, 125.1, weight=96.0)
    g.diag(531.0, 85.4, 538.2, 78.2, weight=96.0)
    g.hbar(538.2, 924.5, 91.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_7db1() -> Glyph:
    """綱 U+7DB1 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7DB1", advance=1000, unicode=0x7DB1, note="綱：自动生成")
    g.diag(241.0, 771.0, 223.8, 650.2, weight=48.0)
    g.diag(223.8, 650.2, 125.3, 435.5, weight=48.0)
    g.hbar(125.3, 272.1, 440.3, weight=48.0)
    g.diag(336.1, 599.7, 295.8, 472.2, weight=48.0)
    g.diag(295.8, 472.2, 162.0, 239.2, weight=48.0)
    g.hbar(162.0, 335.3, 274.6, weight=48.0)
    g.hbar(323.5, 357.1, 318.4, weight=56.0)
    g.diag(357.1, 313.3, 344.6, 292.7, weight=56.0)
    g.diag(146.2, 143.0, 116.1, 29.2, weight=96.0)
    g.diag(116.1, 29.2, 126.0, -36.0, weight=96.0)
    g.vbar(208.1, 86.7, 212.0, weight=96.0)
    g.hbar(235.5, 318.6, 93.9, weight=96.0)
    g.diag(274.3, 255.9, 351.5, 121.0, weight=56.0)
    g.vbar(481.1, 478.9, 648.7, weight=48.0)
    g.vbar(460.6, -9.5, 478.9, weight=48.0)
    g.hbar(491.0, 867.8, 663.2, weight=48.0)
    g.diag(867.8, 688.6, 900.0, 420.6, weight=48.0)
    g.vbar(887.2, 82.6, 420.6, weight=48.0)
    g.diag(874.4, 82.6, 769.4, 15.9, weight=48.0)
    g.diag(561.8, 610.4, 667.9, 477.7, weight=64.0)
    g.diag(736.2, 652.9, 763.9, 588.6, weight=48.0)
    g.diag(763.9, 588.6, 700.5, 439.1, weight=48.0)
    g.hbar(519.1, 764.2, 415.5, weight=96.0)
    g.diag(764.2, 430.7, 797.9, 382.6, weight=96.0)
    g.diag(657.8, 389.6, 682.1, 359.8, weight=96.0)
    g.vbar(681.0, 219.4, 359.8, weight=96.0)
    g.diag(679.9, 219.4, 663.3, 208.3, weight=96.0)
    g.diag(511.5, 303.3, 569.9, 275.5, weight=84.0)
    g.vbar(572.7, 156.5, 275.5, weight=84.0)
    g.hbar(575.5, 766.1, 183.0, weight=84.0)
    g.diag(788.2, 397.4, 812.6, 310.0, weight=84.0)
    g.diag(812.6, 310.0, 770.8, 175.0, weight=84.0)
    return g
def g_cjk_unified_ideograph_7db2() -> Glyph:
    """網 U+7DB2 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7DB2", advance=1000, unicode=0x7DB2, note="網：自动生成")
    g.diag(217.3, 787.0, 199.1, 655.2, weight=48.0)
    g.diag(199.1, 655.2, 102.9, 446.3, weight=48.0)
    g.hbar(102.9, 267.6, 463.0, weight=48.0)
    g.diag(317.6, 611.0, 286.6, 497.7, weight=48.0)
    g.diag(286.6, 497.7, 154.9, 264.6, weight=48.0)
    g.hbar(154.9, 328.4, 293.5, weight=48.0)
    g.hbar(307.5, 337.6, 343.7, weight=48.0)
    g.vbar(334.7, 307.7, 348.0, weight=48.0)
    g.diag(161.1, 174.7, 91.4, -15.2, weight=96.0)
    g.diag(196.6, 244.8, 227.3, 81.7, weight=76.0)
    g.diag(281.4, 283.0, 343.2, 141.9, weight=64.0)
    g.vbar(459.4, 488.7, 653.3, weight=48.0)
    g.vbar(438.6, -19.7, 488.7, weight=48.0)
    g.hbar(470.0, 843.1, 671.0, weight=48.0)
    g.vbar(865.1, 436.3, 701.2, weight=48.0)
    g.vbar(877.8, 79.1, 436.3, weight=48.0)
    g.diag(868.6, 79.1, 775.5, -5.2, weight=48.0)
    g.diag(542.0, 622.0, 607.3, 496.2, weight=48.0)
    g.diag(715.5, 656.8, 747.1, 598.5, weight=48.0)
    g.diag(747.1, 598.5, 685.3, 460.2, weight=48.0)
    g.hbar(501.2, 866.4, 436.0, weight=96.0)
    g.diag(626.2, 390.3, 660.7, 352.5, weight=96.0)
    g.vbar(660.7, 324.6, 352.5, weight=96.0)
    g.hbar(476.5, 889.5, 303.4, weight=48.0)
    g.diag(587.3, 268.5, 635.5, 121.4, weight=48.0)
    g.hbar(635.5, 812.3, 130.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_7dbb() -> Glyph:
    """綻 U+7DBB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7DBB", advance=1000, unicode=0x7DBB, note="綻：自动生成")
    g.diag(201.3, 716.4, 232.6, 669.3, weight=48.0)
    g.diag(232.6, 669.3, 118.4, 435.7, weight=48.0)
    g.hbar(118.4, 239.7, 442.9, weight=48.0)
    g.diag(298.9, 581.0, 269.9, 481.3, weight=48.0)
    g.diag(269.9, 481.3, 147.5, 268.8, weight=48.0)
    g.hbar(147.5, 281.7, 294.1, weight=48.0)
    g.diag(281.7, 319.4, 290.7, 332.1, weight=48.0)
    g.diag(287.4, 347.2, 327.8, 312.2, weight=48.0)
    g.hbar(299.4, 327.8, 311.8, weight=48.0)
    g.diag(129.7, 171.0, 103.8, 65.4, weight=96.0)
    g.hbar(103.8, 191.6, 73.9, weight=96.0)
    g.vbar(191.2, 128.1, 244.9, weight=84.0)
    g.hbar(217.3, 293.2, 135.0, weight=84.0)
    g.diag(236.2, 275.5, 369.0, 125.2, weight=56.0)
    g.diag(500.0, 753.2, 575.6, 709.4, weight=64.0)
    g.diag(575.6, 709.4, 622.6, 607.2, weight=64.0)
    g.hbar(422.2, 425.4, 551.7, weight=76.0)
    g.diag(422.2, 551.1, 390.6, 470.4, weight=76.0)
    g.diag(390.6, 470.4, 439.3, 408.0, weight=76.0)
    g.hbar(436.5, 788.4, 561.9, weight=48.0)
    g.diag(788.4, 593.5, 714.9, 449.0, weight=48.0)
    g.hbar(424.7, 717.4, 431.2, weight=96.0)
    g.diag(554.7, 373.9, 582.6, 349.1, weight=96.0)
    g.vbar(580.6, 172.9, 349.1, weight=96.0)
    g.diag(578.6, 172.9, 595.6, 144.0, weight=96.0)
    g.hbar(611.5, 694.7, 278.1, weight=96.0)
    g.diag(694.7, 291.7, 720.7, 391.4, weight=96.0)
    g.hbar(371.1, 473.5, 288.7, weight=96.0)
    g.diag(473.5, 283.7, 298.6, -11.0, weight=96.0)
    g.diag(298.6, -11.0, 234.3, 67.4, weight=96.0)
    g.diag(480.7, 198.7, 495.4, 151.9, weight=96.0)
    g.hbar(495.4, 937.0, 89.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_7dbf() -> Glyph:
    """綿 U+7DBF —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7DBF", advance=1000, unicode=0x7DBF, note="綿：自动生成")
    g.diag(318.2, 764.4, 302.6, 665.7, weight=48.0)
    g.diag(302.6, 665.7, 230.5, 503.8, weight=48.0)
    g.hbar(230.5, 357.2, 513.6, weight=48.0)
    g.diag(411.0, 635.9, 379.1, 542.3, weight=48.0)
    g.diag(379.1, 542.3, 261.8, 351.9, weight=48.0)
    g.hbar(261.8, 395.9, 371.1, weight=48.0)
    g.diag(358.4, 461.8, 417.4, 392.5, weight=48.0)
    g.diag(417.4, 392.5, 405.5, 377.3, weight=48.0)
    g.diag(220.8, 261.1, 196.1, 171.2, weight=96.0)
    g.hbar(196.1, 272.6, 177.5, weight=96.0)
    g.diag(268.4, 326.3, 298.9, 226.3, weight=84.0)
    g.diag(298.9, 226.3, 348.0, 268.5, weight=84.0)
    g.diag(340.6, 341.6, 475.3, 240.9, weight=76.0)
    g.diag(617.6, 792.0, 653.9, 763.5, weight=48.0)
    g.diag(653.9, 763.5, 571.7, 621.2, weight=48.0)
    g.vbar(546.7, 410.2, 604.6, weight=48.0)
    g.hbar(531.2, 823.4, 620.2, weight=48.0)
    g.vbar(788.6, 440.2, 641.2, weight=48.0)
    g.diag(578.1, 513.7, 588.1, 527.1, weight=76.0)
    g.hbar(588.1, 753.2, 526.6, weight=76.0)
    g.hbar(590.1, 726.6, 438.1, weight=64.0)
    g.diag(726.6, 454.4, 736.0, 444.6, weight=64.0)
    g.vbar(492.2, 139.9, 322.7, weight=92.0)
    g.hbar(521.2, 529.3, 319.3, weight=84.0)
    g.hbar(529.3, 861.1, 338.7, weight=84.0)
    g.vbar(847.0, 152.4, 359.6, weight=84.0)
    g.hbar(696.7, 832.9, 164.2, weight=84.0)
    g.diag(619.4, 419.1, 655.9, 396.0, weight=96.0)
    g.vbar(659.2, -52.0, 396.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_7dca() -> Glyph:
    """緊 U+7DCA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7DCA", advance=1000, unicode=0x7DCA, note="緊：自动生成")
    g.hbar(180.1, 418.3, 748.8, weight=84.0)
    g.diag(288.6, 717.4, 308.3, 697.7, weight=96.0)
    g.diag(308.3, 697.7, 284.5, 658.6, weight=96.0)
    g.hbar(190.3, 426.8, 627.3, weight=48.0)
    g.diag(426.8, 643.5, 365.6, 579.6, weight=48.0)
    g.hbar(191.3, 413.2, 529.9, weight=48.0)
    g.diag(284.5, 521.8, 305.3, 482.4, weight=48.0)
    g.diag(305.3, 482.4, 284.5, 467.1, weight=48.0)
    g.diag(136.5, 752.9, 171.6, 705.0, weight=48.0)
    g.vbar(165.6, 412.9, 705.0, weight=48.0)
    g.hbar(159.6, 385.9, 428.8, weight=48.0)
    g.diag(502.4, 717.4, 600.0, 652.2, weight=48.0)
    g.diag(600.0, 652.2, 457.8, 488.4, weight=48.0)
    g.diag(469.0, 661.7, 883.5, 458.0, weight=56.0)
    g.diag(418.3, 467.1, 433.5, 421.7, weight=48.0)
    g.diag(433.5, 421.7, 313.7, 300.2, weight=48.0)
    g.hbar(313.7, 437.5, 296.0, weight=48.0)
    g.diag(533.8, 394.1, 480.1, 312.4, weight=48.0)
    g.diag(480.1, 312.4, 314.5, 160.2, weight=48.0)
    g.hbar(314.5, 567.3, 181.9, weight=48.0)
    g.diag(552.1, 259.3, 635.2, 162.0, weight=48.0)
    g.diag(428.4, 159.0, 501.9, 105.9, weight=48.0)
    g.diag(501.9, 105.9, 401.9, -49.8, weight=48.0)
    g.hbar(341.3, 401.9, -36.6, weight=48.0)
    g.diag(251.1, 105.3, 175.1, -42.7, weight=96.0)
    g.diag(595.6, 107.3, 729.4, -33.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_7dd2() -> Glyph:
    """緒 U+7DD2 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7DD2", advance=1000, unicode=0x7DD2, note="緒：自动生成")
    g.diag(229.1, 729.2, 245.6, 715.8, weight=48.0)
    g.diag(245.6, 715.8, 215.3, 604.6, weight=48.0)
    g.diag(215.3, 604.6, 128.3, 421.9, weight=48.0)
    g.hbar(128.3, 267.8, 427.2, weight=48.0)
    g.diag(323.0, 551.7, 291.0, 452.8, weight=48.0)
    g.diag(291.0, 452.8, 170.7, 256.7, weight=48.0)
    g.hbar(170.7, 312.3, 277.9, weight=48.0)
    g.diag(312.3, 299.1, 322.9, 312.4, weight=48.0)
    g.diag(316.7, 326.3, 349.8, 308.2, weight=48.0)
    g.diag(349.8, 308.2, 330.9, 292.4, weight=48.0)
    g.diag(147.6, 166.2, 119.7, 55.3, weight=96.0)
    g.diag(119.7, 55.3, 206.0, -10.8, weight=96.0)
    g.diag(188.9, 235.1, 279.9, 41.9, weight=76.0)
    g.diag(280.8, 268.1, 344.7, 160.6, weight=48.0)
    g.hbar(504.7, 545.5, 528.1, weight=96.0)
    g.hbar(504.7, 719.7, 540.4, weight=96.0)
    g.diag(547.0, 787.0, 594.4, 745.7, weight=84.0)
    g.vbar(587.2, 444.4, 745.7, weight=84.0)
    g.diag(580.0, 444.4, 562.4, 418.6, weight=84.0)
    g.hbar(363.7, 931.9, 395.6, weight=96.0)
    g.diag(758.5, 663.2, 672.4, 473.4, weight=48.0)
    g.diag(672.4, 473.4, 243.6, -19.0, weight=48.0)
    g.diag(512.6, 239.0, 489.7, 200.3, weight=48.0)
    g.diag(489.7, 200.3, 523.0, -35.5, weight=48.0)
    g.diag(538.4, 210.2, 548.6, 247.1, weight=48.0)
    g.diag(548.6, 247.1, 717.9, 164.6, weight=48.0)
    g.diag(717.9, 164.6, 743.5, -23.3, weight=48.0)
    g.diag(743.5, -23.3, 672.7, 23.1, weight=48.0)
    g.hbar(663.6, 672.7, 22.1, weight=48.0)
    g.hbar(533.1, 568.4, 130.3, weight=56.0)
    g.hbar(568.4, 656.3, 141.0, weight=56.0)
    g.diag(535.6, -21.0, 548.0, -5.6, weight=96.0)
    g.hbar(548.0, 649.1, 1.1, weight=96.0)
    g.diag(649.1, 7.9, 674.9, -11.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_7dda() -> Glyph:
    """線 U+7DDA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7DDA", advance=1000, unicode=0x7DDA, note="線：自动生成")
    g.vbar(219.4, 631.2, 735.7, weight=48.0)
    g.diag(213.3, 631.2, 139.1, 465.8, weight=48.0)
    g.hbar(139.1, 266.0, 473.3, weight=48.0)
    g.diag(312.8, 581.2, 283.1, 491.5, weight=48.0)
    g.diag(283.1, 491.5, 163.6, 300.1, weight=48.0)
    g.hbar(163.6, 318.6, 322.4, weight=48.0)
    g.diag(307.7, 365.7, 339.9, 347.4, weight=56.0)
    g.diag(339.9, 347.4, 330.1, 327.9, weight=56.0)
    g.diag(149.3, 206.3, 107.8, 80.9, weight=96.0)
    g.hbar(107.8, 207.5, 98.1, weight=96.0)
    g.vbar(211.6, 159.8, 271.9, weight=84.0)
    g.hbar(228.6, 298.5, 167.8, weight=84.0)
    g.diag(260.4, 305.6, 304.8, 233.0, weight=56.0)
    g.hbar(304.8, 359.7, 233.0, weight=56.0)
    g.diag(546.6, 774.9, 585.1, 744.2, weight=96.0)
    g.diag(585.1, 744.2, 493.5, 583.2, weight=96.0)
    g.vbar(472.3, 351.4, 565.3, weight=96.0)
    g.hbar(471.7, 772.0, 572.4, weight=48.0)
    g.vbar(737.6, 382.5, 599.5, weight=48.0)
    g.hbar(684.1, 703.2, 384.0, weight=48.0)
    g.diag(499.7, 469.7, 500.9, 468.9, weight=76.0)
    g.hbar(500.9, 699.3, 469.8, weight=76.0)
    g.diag(513.5, 364.5, 521.3, 374.1, weight=76.0)
    g.hbar(521.3, 676.2, 386.1, weight=76.0)
    g.diag(555.7, 357.5, 610.3, 316.4, weight=84.0)
    g.vbar(597.5, -36.8, 316.4, weight=84.0)
    g.diag(584.7, -36.8, 432.9, 60.8, weight=84.0)
    g.hbar(340.7, 551.3, 249.2, weight=76.0)
    g.diag(551.3, 267.2, 295.8, -3.8, weight=76.0)
    g.hbar(741.9, 793.5, 337.4, weight=96.0)
    g.diag(793.5, 327.4, 667.0, 226.0, weight=96.0)
    g.hbar(658.0, 667.0, 228.0, weight=96.0)
    g.diag(628.9, 239.1, 808.8, 64.1, weight=96.0)
    g.hbar(808.8, 947.0, 57.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_7de0() -> Glyph:
    """締 U+7DE0 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7DE0", advance=1000, unicode=0x7DE0, note="締：自动生成")
    g.diag(298.4, 756.3, 326.1, 713.1, weight=48.0)
    g.diag(326.1, 713.1, 205.1, 511.4, weight=48.0)
    g.hbar(205.1, 320.6, 516.5, weight=48.0)
    g.diag(380.9, 641.7, 347.4, 545.4, weight=48.0)
    g.diag(347.4, 545.4, 225.3, 352.3, weight=48.0)
    g.hbar(225.3, 349.3, 371.1, weight=48.0)
    g.diag(340.5, 407.8, 371.7, 392.5, weight=48.0)
    g.diag(371.7, 392.5, 360.7, 377.0, weight=48.0)
    g.diag(216.2, 257.4, 188.5, 157.9, weight=96.0)
    g.hbar(188.5, 268.9, 165.9, weight=96.0)
    g.vbar(273.3, 228.5, 327.3, weight=76.0)
    g.hbar(291.1, 356.8, 230.6, weight=76.0)
    g.diag(368.5, 346.0, 379.0, 267.0, weight=64.0)
    g.diag(379.0, 267.0, 316.8, 231.2, weight=64.0)
    g.diag(574.2, 792.0, 636.5, 757.2, weight=96.0)
    g.diag(636.5, 757.2, 670.5, 689.1, weight=96.0)
    g.diag(511.3, 609.0, 525.3, 619.8, weight=96.0)
    g.hbar(525.3, 734.8, 642.1, weight=96.0)
    g.vbar(738.0, 625.1, 664.4, weight=96.0)
    g.diag(527.8, 605.4, 574.5, 485.0, weight=48.0)
    g.diag(688.2, 627.6, 713.7, 598.3, weight=64.0)
    g.diag(713.7, 598.3, 652.1, 496.9, weight=64.0)
    g.hbar(468.8, 477.5, 459.6, weight=56.0)
    g.diag(468.8, 460.3, 442.3, 392.5, weight=56.0)
    g.diag(442.3, 392.5, 455.9, 342.9, weight=56.0)
    g.hbar(488.1, 877.4, 469.5, weight=96.0)
    g.diag(877.4, 499.9, 778.0, 384.6, weight=96.0)
    g.vbar(503.4, 161.5, 324.7, weight=96.0)
    g.hbar(538.1, 575.4, 155.2, weight=96.0)
    g.hbar(502.7, 520.4, 321.2, weight=96.0)
    g.hbar(520.4, 788.3, 336.2, weight=96.0)
    g.vbar(775.8, 174.7, 354.6, weight=96.0)
    g.hbar(653.3, 763.2, 191.3, weight=96.0)
    g.diag(577.0, 443.8, 617.6, 415.4, weight=96.0)
    g.vbar(613.8, -62.0, 415.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_7de9() -> Glyph:
    """緩 U+7DE9 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7DE9", advance=1000, unicode=0x7DE9, note="緩：自动生成")
    g.diag(226.1, 787.0, 204.4, 670.1, weight=48.0)
    g.diag(204.4, 670.1, 112.1, 486.6, weight=48.0)
    g.hbar(112.1, 251.4, 494.5, weight=48.0)
    g.diag(311.3, 627.0, 272.0, 518.6, weight=48.0)
    g.diag(272.0, 518.6, 148.8, 325.8, weight=48.0)
    g.hbar(148.8, 311.1, 348.1, weight=48.0)
    g.diag(297.5, 384.1, 363.9, 334.7, weight=48.0)
    g.diag(161.9, 225.1, 116.8, 107.9, weight=96.0)
    g.diag(116.8, 107.9, 183.4, 17.2, weight=96.0)
    g.diag(201.5, 301.1, 233.3, 183.9, weight=84.0)
    g.hbar(233.3, 309.2, 189.6, weight=84.0)
    g.vbar(328.5, 234.2, 322.0, weight=64.0)
    g.diag(331.8, 234.2, 383.8, 172.0, weight=64.0)
    g.hbar(627.5, 721.6, 754.4, weight=96.0)
    g.diag(627.5, 772.4, 443.7, 649.5, weight=96.0)
    g.dot(462.3, 563.5, w=92.0, h=119.6, slant=-14.0)
    g.dot(577.9, 619.1, w=92.0, h=119.6, slant=-14.0)
    g.diag(719.5, 739.0, 766.8, 672.6, weight=96.0)
    g.diag(766.8, 672.6, 659.6, 564.8, weight=96.0)
    g.diag(659.6, 564.8, 664.1, 540.1, weight=96.0)
    g.hbar(462.2, 701.9, 477.3, weight=96.0)
    g.diag(701.9, 510.5, 711.4, 559.2, weight=96.0)
    g.hbar(376.3, 837.4, 356.2, weight=96.0)
    g.diag(492.9, 438.1, 463.0, 317.8, weight=48.0)
    g.diag(463.0, 317.8, 217.9, 0.3, weight=48.0)
    g.diag(486.7, 244.1, 586.8, 159.7, weight=48.0)
    g.diag(586.8, 159.7, 385.1, -39.7, weight=48.0)
    g.diag(465.1, 181.9, 924.6, -52.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_7def() -> Glyph:
    """緯 U+7DEF —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7DEF", advance=1000, unicode=0x7DEF, note="緯：自动生成")
    g.diag(269.0, 762.6, 248.0, 651.1, weight=48.0)
    g.diag(248.0, 651.1, 165.7, 470.1, weight=48.0)
    g.hbar(165.7, 278.0, 481.3, weight=48.0)
    g.diag(346.8, 633.3, 316.7, 535.8, weight=48.0)
    g.diag(316.7, 535.8, 198.8, 329.5, weight=48.0)
    g.hbar(198.8, 355.1, 357.2, weight=48.0)
    g.diag(344.4, 406.1, 384.7, 376.5, weight=56.0)
    g.diag(384.7, 376.5, 367.9, 368.8, weight=56.0)
    g.diag(197.4, 242.0, 176.8, 137.0, weight=92.0)
    g.hbar(176.8, 253.5, 141.2, weight=92.0)
    g.vbar(252.3, 202.1, 313.5, weight=64.0)
    g.hbar(273.5, 343.6, 201.9, weight=64.0)
    g.diag(301.1, 338.3, 358.5, 250.9, weight=64.0)
    g.hbar(358.5, 413.8, 246.0, weight=64.0)
    g.vbar(585.7, 644.3, 684.3, weight=96.0)
    g.diag(584.7, 644.3, 568.3, 552.8, weight=96.0)
    g.hbar(471.5, 765.8, 649.1, weight=48.0)
    g.diag(765.8, 662.1, 701.4, 570.7, weight=48.0)
    g.hbar(408.2, 868.4, 533.9, weight=48.0)
    g.dot(503.0, 395.9, w=96.0, h=124.8, slant=-14.0)
    g.hbar(511.7, 742.6, 459.6, weight=48.0)
    g.diag(742.6, 471.7, 683.1, 403.7, weight=48.0)
    g.hbar(538.9, 715.7, 371.5, weight=48.0)
    g.vbar(716.0, 388.6, 405.7, weight=48.0)
    g.hbar(468.9, 752.7, 268.1, weight=48.0)
    g.vbar(450.7, 147.0, 260.5, weight=96.0)
    g.hbar(437.3, 839.5, 154.6, weight=96.0)
    g.diag(576.4, 351.2, 601.8, 209.7, weight=48.0)
    g.vbar(602.7, -52.0, 209.7, weight=48.0)
    return g
def g_cjk_unified_ideograph_7df4() -> Glyph:
    """練 U+7DF4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7DF4", advance=1000, unicode=0x7DF4, note="練：自动生成")
    g.diag(220.2, 714.5, 208.0, 617.6, weight=48.0)
    g.diag(208.0, 617.6, 137.0, 457.5, weight=48.0)
    g.hbar(137.0, 249.6, 469.1, weight=48.0)
    g.diag(294.6, 586.9, 266.1, 491.1, weight=48.0)
    g.diag(266.1, 491.1, 158.5, 301.3, weight=48.0)
    g.hbar(158.5, 302.0, 323.7, weight=48.0)
    g.diag(253.5, 416.5, 323.0, 351.9, weight=48.0)
    g.diag(323.0, 351.9, 312.4, 333.8, weight=48.0)
    g.diag(145.2, 208.0, 120.2, 110.5, weight=96.0)
    g.hbar(120.2, 202.3, 117.2, weight=96.0)
    g.vbar(206.5, 148.1, 284.1, weight=64.0)
    g.diag(263.3, 312.9, 332.2, 205.0, weight=48.0)
    g.vbar(471.3, 538.3, 603.5, weight=76.0)
    g.hbar(474.3, 629.2, 624.7, weight=76.0)
    g.diag(629.2, 645.9, 683.5, 582.7, weight=76.0)
    g.vbar(420.1, 319.0, 509.7, weight=48.0)
    g.hbar(408.6, 724.5, 529.7, weight=48.0)
    g.diag(724.5, 554.7, 753.6, 511.6, weight=48.0)
    g.diag(753.6, 511.6, 675.6, 355.6, weight=48.0)
    g.diag(461.0, 485.9, 496.5, 430.8, weight=48.0)
    g.hbar(496.5, 544.8, 420.5, weight=48.0)
    g.diag(625.8, 522.0, 649.8, 475.8, weight=48.0)
    g.diag(649.8, 475.8, 583.2, 409.1, weight=48.0)
    g.hbar(457.6, 644.1, 352.4, weight=48.0)
    g.diag(644.1, 371.6, 663.5, 359.2, weight=48.0)
    g.vbar(535.4, 500.7, 787.0, weight=48.0)
    g.vbar(548.7, -52.0, 500.7, weight=48.0)
    g.diag(536.5, 335.0, 293.7, 57.2, weight=48.0)
    g.diag(582.0, 318.9, 930.7, 110.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_7dfb() -> Glyph:
    """緻 U+7DFB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7DFB", advance=1000, unicode=0x7DFB, note="緻：自动生成")
    g.diag(179.9, 702.2, 162.6, 592.6, weight=48.0)
    g.diag(162.6, 592.6, 80.8, 417.3, weight=48.0)
    g.hbar(80.8, 202.6, 427.0, weight=48.0)
    g.diag(257.6, 556.0, 217.8, 446.3, weight=48.0)
    g.diag(217.8, 446.3, 102.1, 248.3, weight=48.0)
    g.hbar(102.1, 251.0, 272.6, weight=48.0)
    g.dot(251.7, 301.4, w=48.0, h=35.7, slant=-14.0)
    g.diag(124.3, 158.9, 89.2, -5.5, weight=92.0)
    g.diag(151.8, 227.5, 230.2, 81.0, weight=76.0)
    g.diag(244.1, 266.3, 271.7, 102.9, weight=64.0)
    g.hbar(352.8, 623.5, 588.2, weight=96.0)
    g.diag(386.3, 558.4, 415.8, 533.0, weight=48.0)
    g.diag(415.8, 533.0, 345.3, 382.7, weight=48.0)
    g.hbar(345.3, 498.9, 401.0, weight=48.0)
    g.diag(492.2, 437.3, 560.4, 390.0, weight=48.0)
    g.hbar(306.7, 388.0, 243.6, weight=84.0)
    g.hbar(388.0, 550.8, 263.8, weight=84.0)
    g.diag(407.8, 376.6, 446.4, 346.3, weight=48.0)
    g.vbar(434.9, 134.7, 346.3, weight=48.0)
    g.hbar(225.4, 313.0, 74.2, weight=76.0)
    g.diag(313.0, 67.1, 627.9, 211.4, weight=76.0)
    g.diag(639.6, 745.5, 695.4, 707.1, weight=76.0)
    g.diag(695.4, 707.1, 565.4, 388.8, weight=76.0)
    g.hbar(629.5, 854.3, 457.2, weight=96.0)
    g.diag(701.1, 416.9, 765.4, 365.1, weight=76.0)
    g.diag(765.4, 365.1, 595.8, 54.9, weight=76.0)
    g.hbar(472.2, 595.8, 78.2, weight=76.0)
    g.diag(575.5, 347.4, 937.0, 10.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_7e1b() -> Glyph:
    """縛 U+7E1B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7E1B", advance=1000, unicode=0x7E1B, note="縛：自动生成")
    g.vbar(213.2, 647.8, 753.6, weight=48.0)
    g.diag(208.3, 647.8, 137.1, 455.7, weight=48.0)
    g.hbar(137.1, 241.8, 465.4, weight=48.0)
    g.diag(308.9, 625.2, 283.9, 524.8, weight=48.0)
    g.diag(283.9, 524.8, 175.7, 316.6, weight=48.0)
    g.hbar(175.7, 315.2, 343.3, weight=48.0)
    g.vbar(316.5, 370.0, 380.4, weight=48.0)
    g.diag(323.7, 430.7, 361.3, 351.7, weight=48.0)
    g.dot(101.6, 116.3, w=96.0, h=124.8, slant=-14.0)
    g.dot(205.3, 181.4, w=96.0, h=97.9, slant=-14.0)
    g.dot(308.4, 233.8, w=64.0, h=83.2, slant=-14.0)
    g.hbar(481.7, 761.1, 669.6, weight=64.0)
    g.diag(403.7, 556.1, 459.0, 325.1, weight=76.0)
    g.diag(451.1, 545.2, 458.1, 540.8, weight=64.0)
    g.hbar(458.1, 803.2, 563.3, weight=64.0)
    g.diag(803.2, 585.8, 736.4, 371.5, weight=64.0)
    g.hbar(515.3, 681.1, 487.0, weight=56.0)
    g.hbar(518.2, 684.1, 410.0, weight=48.0)
    g.diag(551.8, 797.0, 596.3, 765.6, weight=96.0)
    g.vbar(591.8, 333.0, 765.6, weight=96.0)
    g.dot(790.2, 756.5, w=96.0, h=107.8, slant=-14.0)
    g.hbar(383.0, 926.0, 248.1, weight=96.0)
    g.diag(637.7, 355.7, 669.9, 204.5, weight=48.0)
    g.vbar(668.1, -57.0, 204.5, weight=48.0)
    g.hbar(558.7, 666.3, -36.8, weight=48.0)
    g.dot(502.4, 130.6, w=96.0, h=123.2, slant=-14.0)
    return g
def g_cjk_unified_ideograph_7e2b() -> Glyph:
    """縫 U+7E2B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7E2B", advance=1000, unicode=0x7E2B, note="縫：自动生成")
    g.vbar(195.9, 637.1, 745.4, weight=48.0)
    g.diag(190.5, 637.1, 108.3, 446.9, weight=48.0)
    g.hbar(108.3, 227.5, 458.2, weight=48.0)
    g.diag(282.5, 596.0, 252.8, 495.5, weight=48.0)
    g.diag(252.8, 495.5, 134.6, 283.7, weight=48.0)
    g.hbar(134.6, 267.4, 303.1, weight=48.0)
    g.diag(258.3, 341.4, 291.5, 319.4, weight=48.0)
    g.diag(291.5, 319.4, 277.5, 309.6, weight=48.0)
    g.diag(130.6, 190.7, 103.1, 96.9, weight=96.0)
    g.hbar(103.1, 189.4, 102.4, weight=96.0)
    g.diag(167.9, 253.7, 274.3, 105.5, weight=84.0)
    g.diag(285.1, 277.0, 309.5, 116.0, weight=64.0)
    g.diag(580.2, 757.4, 605.3, 718.5, weight=48.0)
    g.diag(605.3, 718.5, 490.0, 575.0, weight=48.0)
    g.diag(588.8, 664.1, 654.0, 614.2, weight=48.0)
    g.diag(654.0, 614.2, 482.0, 420.6, weight=48.0)
    g.hbar(554.1, 947.0, 535.9, weight=76.0)
    g.diag(514.3, 410.8, 604.6, 355.9, weight=64.0)
    g.hbar(604.6, 746.7, 374.0, weight=64.0)
    g.diag(746.7, 392.1, 785.8, 442.6, weight=64.0)
    g.diag(544.8, 332.1, 563.1, 265.3, weight=64.0)
    g.hbar(563.1, 719.5, 283.3, weight=64.0)
    g.diag(719.5, 301.4, 762.4, 234.3, weight=64.0)
    g.hbar(465.4, 830.7, 177.7, weight=76.0)
    g.diag(592.1, 473.6, 625.7, 336.0, weight=48.0)
    g.vbar(627.8, 21.3, 336.0, weight=48.0)
    g.diag(341.8, 565.8, 413.8, 529.9, weight=96.0)
    g.diag(413.8, 529.9, 459.6, 451.8, weight=96.0)
    g.hbar(300.4, 453.9, 353.3, weight=48.0)
    g.diag(453.9, 364.5, 392.5, 232.7, weight=48.0)
    g.diag(392.5, 232.7, 418.8, 96.1, weight=48.0)
    g.diag(313.1, 134.4, 321.1, 78.2, weight=96.0)
    g.hbar(321.1, 917.9, 42.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_7e2e() -> Glyph:
    """縮 U+7E2E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7E2E", advance=1000, unicode=0x7E2E, note="縮：自动生成")
    g.diag(239.7, 779.8, 222.8, 660.8, weight=48.0)
    g.diag(222.8, 660.8, 140.1, 452.0, weight=48.0)
    g.hbar(140.1, 281.5, 476.5, weight=48.0)
    g.diag(333.6, 636.3, 301.4, 517.8, weight=48.0)
    g.diag(301.4, 517.8, 171.1, 278.7, weight=48.0)
    g.hbar(171.1, 338.1, 313.1, weight=48.0)
    g.hbar(325.9, 353.7, 361.4, weight=48.0)
    g.vbar(348.1, 333.9, 360.7, weight=48.0)
    g.vbar(158.3, 7.1, 175.7, weight=96.0)
    g.diag(196.1, 255.4, 254.5, 139.1, weight=84.0)
    g.hbar(254.5, 341.8, 143.9, weight=84.0)
    g.diag(284.2, 292.3, 372.7, 162.3, weight=64.0)
    g.diag(591.2, 802.0, 664.0, 762.9, weight=76.0)
    g.diag(664.0, 762.9, 707.5, 660.5, weight=76.0)
    g.hbar(477.4, 484.7, 604.7, weight=84.0)
    g.vbar(460.4, 515.9, 605.1, weight=84.0)
    g.diag(443.4, 515.9, 474.2, 470.5, weight=84.0)
    g.hbar(495.2, 854.1, 617.8, weight=56.0)
    g.diag(854.1, 657.2, 904.4, 619.3, weight=56.0)
    g.diag(904.4, 619.3, 824.5, 479.2, weight=56.0)
    g.hbar(456.0, 537.5, 463.2, weight=48.0)
    g.diag(537.5, 447.1, 393.8, 258.4, weight=48.0)
    g.vbar(481.2, -52.0, 315.2, weight=48.0)
    g.hbar(549.8, 875.2, 442.7, weight=48.0)
    g.diag(707.3, 405.0, 704.8, 386.0, weight=48.0)
    g.diag(704.8, 386.0, 640.8, 292.1, weight=48.0)
    g.diag(608.3, 287.6, 604.1, 271.0, weight=48.0)
    g.vbar(614.5, 3.4, 271.0, weight=48.0)
    g.diag(627.1, 283.7, 802.3, 187.0, weight=48.0)
    g.diag(802.3, 187.0, 845.6, -35.1, weight=48.0)
    g.diag(641.9, 156.0, 660.1, 174.2, weight=96.0)
    g.hbar(660.1, 817.6, 178.9, weight=96.0)
    g.hbar(637.6, 814.1, 32.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_7e3e() -> Glyph:
    """績 U+7E3E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7E3E", advance=1000, unicode=0x7E3E, note="績：自动生成")
    g.diag(253.1, 741.6, 237.0, 645.5, weight=48.0)
    g.diag(237.0, 645.5, 153.8, 470.7, weight=48.0)
    g.hbar(153.8, 289.8, 485.6, weight=48.0)
    g.diag(346.7, 619.6, 311.5, 517.6, weight=48.0)
    g.diag(311.5, 517.6, 186.2, 315.9, weight=48.0)
    g.hbar(186.2, 347.1, 337.1, weight=48.0)
    g.diag(336.1, 376.5, 369.4, 356.6, weight=48.0)
    g.diag(369.4, 356.6, 354.6, 343.7, weight=48.0)
    g.diag(181.5, 233.2, 155.8, 95.2, weight=96.0)
    g.diag(155.8, 95.2, 235.6, 138.2, weight=96.0)
    g.diag(221.2, 286.1, 255.9, 195.7, weight=84.0)
    g.hbar(255.9, 329.2, 197.0, weight=84.0)
    g.diag(299.7, 328.7, 359.0, 213.7, weight=48.0)
    g.diag(487.3, 572.5, 520.1, 631.5, weight=64.0)
    g.hbar(520.1, 775.3, 655.8, weight=64.0)
    g.vbar(509.8, 541.2, 608.9, weight=64.0)
    g.hbar(521.4, 728.9, 560.5, weight=64.0)
    g.diag(579.5, 787.0, 622.0, 750.1, weight=84.0)
    g.vbar(616.8, 500.4, 750.1, weight=84.0)
    g.diag(611.6, 500.4, 597.4, 483.3, weight=84.0)
    g.hbar(368.6, 892.6, 452.9, weight=76.0)
    g.hbar(488.2, 502.1, 376.5, weight=48.0)
    g.vbar(500.7, 111.8, 373.4, weight=48.0)
    g.hbar(511.5, 698.0, 377.5, weight=48.0)
    g.vbar(697.7, 313.5, 384.1, weight=48.0)
    g.vbar(702.7, 128.8, 313.5, weight=48.0)
    g.hbar(518.8, 657.0, 288.9, weight=48.0)
    g.hbar(521.7, 621.8, 212.9, weight=56.0)
    g.diag(621.8, 225.4, 665.3, 175.5, weight=56.0)
    g.hbar(525.8, 710.9, 132.5, weight=56.0)
    g.diag(528.0, 84.3, 539.4, 37.9, weight=76.0)
    g.diag(539.4, 37.9, 379.9, -66.3, weight=76.0)
    g.diag(699.5, 85.5, 790.4, -72.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_7e41() -> Glyph:
    """繁 U+7E41 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7E41", advance=1000, unicode=0x7E41, note="繁：自动生成")
    g.diag(293.7, 740.2, 296.6, 747.8, weight=96.0)
    g.diag(296.6, 747.8, 224.5, 635.8, weight=96.0)
    g.hbar(300.1, 458.0, 717.2, weight=96.0)
    g.diag(458.0, 732.0, 481.4, 686.0, weight=96.0)
    g.hbar(259.0, 280.2, 648.8, weight=48.0)
    g.vbar(249.4, 437.2, 646.0, weight=48.0)
    g.hbar(218.5, 475.8, 430.9, weight=48.0)
    g.diag(295.5, 638.7, 308.1, 632.4, weight=48.0)
    g.hbar(308.1, 472.8, 643.5, weight=48.0)
    g.diag(472.8, 654.6, 408.5, 425.3, weight=48.0)
    g.dot(354.0, 592.5, w=48.0, h=62.4, slant=-14.0)
    g.diag(84.5, 529.2, 97.8, 517.6, weight=96.0)
    g.hbar(97.8, 506.5, 537.0, weight=96.0)
    g.dot(331.4, 494.9, w=48.0, h=62.4, slant=-14.0)
    g.diag(628.3, 791.0, 659.9, 751.6, weight=96.0)
    g.diag(659.9, 751.6, 529.7, 549.3, weight=96.0)
    g.hbar(618.8, 863.0, 653.0, weight=48.0)
    g.diag(704.7, 624.5, 738.6, 584.2, weight=48.0)
    g.diag(738.6, 584.2, 589.7, 414.1, weight=48.0)
    g.hbar(512.7, 589.7, 405.5, weight=48.0)
    g.diag(564.9, 565.4, 672.2, 495.6, weight=96.0)
    g.diag(672.2, 495.6, 930.5, 372.1, weight=96.0)
    g.vbar(489.0, 372.8, 420.3, weight=48.0)
    g.diag(496.2, 372.8, 363.7, 259.0, weight=48.0)
    g.hbar(363.7, 477.9, 250.5, weight=48.0)
    g.hbar(477.9, 503.1, 245.1, weight=48.0)
    g.diag(588.3, 396.1, 540.9, 280.3, weight=48.0)
    g.diag(540.9, 280.3, 510.7, 179.3, weight=48.0)
    g.hbar(510.7, 655.7, 173.3, weight=48.0)
    g.diag(638.2, 187.5, 692.8, 154.5, weight=48.0)
    g.hbar(666.1, 692.8, 153.0, weight=48.0)
    g.diag(503.5, 129.4, 538.6, 99.3, weight=48.0)
    g.diag(538.6, 99.3, 509.4, -67.4, weight=48.0)
    g.diag(509.4, -67.4, 417.9, -23.7, weight=48.0)
    g.diag(371.2, 106.7, 264.8, -50.9, weight=96.0)
    g.diag(679.8, 104.4, 764.3, -41.8, weight=76.0)
    return g
def g_cjk_unified_ideograph_7e54() -> Glyph:
    """織 U+7E54 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7E54", advance=1000, unicode=0x7E54, note="織：自动生成")
    g.diag(178.7, 715.6, 165.6, 609.8, weight=48.0)
    g.diag(165.6, 609.8, 86.3, 419.8, weight=48.0)
    g.hbar(86.3, 223.2, 432.9, weight=48.0)
    g.diag(291.3, 604.0, 254.9, 487.2, weight=48.0)
    g.diag(254.9, 487.2, 117.0, 242.5, weight=48.0)
    g.diag(117.0, 242.5, 270.0, 318.5, weight=48.0)
    g.diag(264.0, 334.0, 307.8, 296.2, weight=48.0)
    g.hbar(279.7, 307.8, 299.7, weight=48.0)
    g.vbar(126.2, -37.4, 141.4, weight=96.0)
    g.diag(231.7, 185.4, 215.9, 103.1, weight=84.0)
    g.hbar(215.9, 283.8, 108.9, weight=84.0)
    g.vbar(295.6, 167.1, 257.2, weight=64.0)
    g.hbar(293.3, 368.5, 151.2, weight=64.0)
    g.dot(482.0, 655.8, w=96.0, h=124.8, slant=-14.0)
    g.hbar(386.2, 603.7, 536.5, weight=96.0)
    g.dot(418.6, 437.5, w=92.0, h=114.9, slant=-14.0)
    g.diag(527.8, 526.6, 556.9, 496.3, weight=76.0)
    g.diag(556.9, 496.3, 501.0, 380.9, weight=76.0)
    g.hbar(338.9, 798.0, 372.1, weight=96.0)
    g.diag(798.0, 425.4, 810.0, 374.2, weight=96.0)
    g.vbar(399.3, 35.6, 251.6, weight=48.0)
    g.hbar(406.7, 543.1, 261.7, weight=48.0)
    g.vbar(554.1, 179.3, 278.9, weight=48.0)
    g.vbar(565.5, -9.5, 179.3, weight=48.0)
    g.hbar(416.6, 556.0, 145.5, weight=56.0)
    g.diag(417.0, 49.4, 430.1, 63.3, weight=64.0)
    g.hbar(430.1, 544.7, 62.1, weight=64.0)
    g.diag(577.4, 772.4, 680.4, 494.5, weight=84.0)
    g.diag(680.4, 494.5, 880.9, -78.0, weight=84.0)
    g.diag(880.9, -78.0, 942.0, 129.9, weight=84.0)
    g.diag(806.1, 391.1, 603.1, 88.0, weight=64.0)
    g.hbar(665.1, 804.6, 630.5, weight=64.0)
    g.diag(804.6, 605.1, 827.3, 567.9, weight=64.0)
    return g
def g_cjk_unified_ideograph_7e55() -> Glyph:
    """繕 U+7E55 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7E55", advance=1000, unicode=0x7E55, note="繕：自动生成")
    g.vbar(223.1, 647.9, 746.2, weight=48.0)
    g.diag(219.0, 647.9, 152.5, 485.3, weight=48.0)
    g.hbar(152.5, 269.6, 502.6, weight=48.0)
    g.diag(318.7, 640.9, 292.7, 543.1, weight=48.0)
    g.diag(292.7, 543.1, 181.6, 336.6, weight=48.0)
    g.diag(181.6, 336.6, 331.7, 407.8, weight=48.0)
    g.hbar(322.1, 352.8, 415.1, weight=48.0)
    g.diag(352.8, 410.9, 337.1, 387.7, weight=48.0)
    g.diag(178.7, 262.2, 153.0, 93.2, weight=96.0)
    g.diag(210.3, 327.0, 253.4, 219.9, weight=56.0)
    g.diag(253.4, 219.9, 305.5, 190.8, weight=56.0)
    g.diag(284.2, 356.0, 353.8, 266.7, weight=48.0)
    g.dot(524.8, 693.8, w=96.0, h=124.8, slant=-14.0)
    g.diag(708.6, 792.0, 732.9, 756.3, weight=96.0)
    g.diag(732.9, 756.3, 625.8, 631.2, weight=96.0)
    g.diag(536.1, 560.8, 530.9, 571.3, weight=84.0)
    g.hbar(530.9, 715.8, 593.3, weight=84.0)
    g.vbar(730.1, 537.9, 615.3, weight=84.0)
    g.diag(469.5, 391.3, 504.0, 457.9, weight=64.0)
    g.hbar(504.0, 717.8, 484.3, weight=64.0)
    g.vbar(732.8, 439.4, 510.7, weight=64.0)
    g.hbar(439.6, 772.9, 368.0, weight=48.0)
    g.diag(569.2, 555.2, 595.2, 535.1, weight=64.0)
    g.vbar(592.4, 263.6, 535.1, weight=64.0)
    g.diag(589.5, 263.6, 574.1, 241.4, weight=64.0)
    g.diag(448.3, 348.6, 509.4, 225.9, weight=48.0)
    g.diag(685.8, 380.7, 710.5, 332.0, weight=56.0)
    g.diag(710.5, 332.0, 657.2, 254.6, weight=56.0)
    g.hbar(282.5, 912.3, 218.1, weight=64.0)
    g.diag(417.1, 168.8, 521.7, -26.2, weight=48.0)
    g.hbar(469.9, 712.1, 140.9, weight=48.0)
    g.diag(712.1, 159.0, 750.7, 118.1, weight=48.0)
    g.diag(750.7, 118.1, 688.7, 27.5, weight=48.0)
    g.hbar(510.9, 727.9, 2.9, weight=48.0)
    g.vbar(726.5, 8.3, 37.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_7e70() -> Glyph:
    """繰 U+7E70 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7E70", advance=1000, unicode=0x7E70, note="繰：自动生成")
    g.diag(235.4, 779.2, 221.8, 677.2, weight=48.0)
    g.diag(221.8, 677.2, 135.4, 478.8, weight=48.0)
    g.hbar(135.4, 257.3, 488.7, weight=48.0)
    g.diag(311.9, 622.3, 282.0, 524.0, weight=48.0)
    g.diag(282.0, 524.0, 169.6, 330.7, weight=48.0)
    g.hbar(169.6, 304.0, 348.1, weight=48.0)
    g.diag(263.4, 440.2, 324.6, 369.5, weight=48.0)
    g.diag(324.6, 369.5, 311.8, 351.0, weight=48.0)
    g.vbar(125.4, 66.6, 235.2, weight=84.0)
    g.vbar(196.2, 203.8, 304.8, weight=76.0)
    g.hbar(205.0, 282.1, 202.8, weight=76.0)
    g.diag(254.4, 327.6, 310.9, 211.7, weight=56.0)
    g.diag(472.1, 759.5, 459.8, 741.8, weight=48.0)
    g.diag(459.8, 741.8, 518.6, 629.6, weight=48.0)
    g.hbar(476.8, 715.5, 765.1, weight=48.0)
    g.diag(715.5, 779.3, 659.1, 688.0, weight=48.0)
    g.hbar(513.3, 685.7, 660.7, weight=48.0)
    g.vbar(687.8, 671.4, 692.9, weight=48.0)
    g.vbar(396.1, 417.6, 540.0, weight=48.0)
    g.hbar(394.0, 533.5, 540.0, weight=48.0)
    g.diag(533.5, 546.1, 493.1, 473.8, weight=48.0)
    g.hbar(423.6, 521.3, 454.6, weight=48.0)
    g.vbar(643.1, 443.2, 580.4, weight=48.0)
    g.hbar(638.0, 806.0, 584.9, weight=48.0)
    g.diag(806.0, 599.5, 751.3, 498.0, weight=48.0)
    g.hbar(667.4, 779.9, 479.8, weight=48.0)
    g.hbar(341.7, 539.3, 320.7, weight=48.0)
    g.hbar(539.3, 868.6, 323.7, weight=48.0)
    g.vbar(565.0, -52.0, 416.5, weight=96.0)
    g.diag(526.1, 288.7, 258.0, 44.1, weight=48.0)
    g.diag(601.8, 288.4, 928.4, 86.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_7f75() -> Glyph:
    """罵 U+7F75 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7F75", advance=1000, unicode=0x7F75, note="罵：自动生成")
    g.vbar(283.4, 548.9, 713.8, weight=96.0)
    g.hbar(285.5, 781.1, 729.7, weight=64.0)
    g.diag(781.1, 751.9, 696.0, 592.2, weight=64.0)
    g.diag(398.4, 696.5, 406.4, 692.1, weight=96.0)
    g.diag(406.4, 692.1, 442.4, 605.6, weight=96.0)
    g.diag(551.9, 726.8, 575.0, 701.6, weight=96.0)
    g.diag(575.0, 701.6, 528.4, 619.3, weight=96.0)
    g.hbar(328.0, 661.2, 589.9, weight=48.0)
    g.diag(661.2, 616.9, 683.3, 598.6, weight=48.0)
    g.hbar(360.9, 693.5, 521.6, weight=64.0)
    g.vbar(318.1, 281.6, 510.7, weight=96.0)
    g.vbar(330.9, 174.5, 281.6, weight=96.0)
    g.diag(419.3, 448.6, 482.4, 394.4, weight=64.0)
    g.hbar(482.4, 603.7, 408.1, weight=64.0)
    g.diag(603.7, 421.8, 644.5, 369.2, weight=64.0)
    g.hbar(365.0, 594.6, 327.2, weight=64.0)
    g.diag(594.6, 334.9, 641.4, 399.0, weight=64.0)
    g.diag(499.1, 463.8, 530.3, 437.4, weight=96.0)
    g.vbar(528.4, 279.1, 437.4, weight=96.0)
    g.diag(526.4, 279.1, 509.8, 256.6, weight=96.0)
    g.hbar(350.5, 501.1, 192.6, weight=64.0)
    g.hbar(501.1, 693.1, 178.3, weight=64.0)
    g.vbar(700.0, -72.7, 143.9, weight=64.0)
    g.diag(706.9, -72.7, 622.8, -20.8, weight=64.0)
    g.diag(622.8, -20.8, 636.1, 48.7, weight=64.0)
    g.diag(286.7, 129.0, 204.8, 71.8, weight=96.0)
    g.diag(204.8, 71.8, 169.6, -15.2, weight=96.0)
    g.diag(326.9, 136.7, 356.3, 67.9, weight=96.0)
    g.vbar(355.1, 67.9, 134.3, weight=96.0)
    g.diag(443.0, 196.2, 494.2, 74.8, weight=56.0)
    g.diag(559.9, 216.8, 644.7, 72.8, weight=56.0)
    return g
def g_cjk_unified_ideograph_7f77() -> Glyph:
    """罷 U+7F77 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7F77", advance=1000, unicode=0x7F77, note="罷：自动生成")
    g.vbar(224.7, 709.1, 725.6, weight=48.0)
    g.vbar(246.1, 559.0, 709.1, weight=48.0)
    g.hbar(236.3, 648.0, 743.1, weight=48.0)
    g.diag(648.0, 768.3, 679.9, 724.6, weight=48.0)
    g.diag(679.9, 724.6, 602.4, 591.0, weight=48.0)
    g.diag(347.7, 705.9, 378.3, 618.5, weight=96.0)
    g.diag(378.3, 618.5, 387.1, 611.3, weight=96.0)
    g.diag(491.6, 732.5, 515.0, 708.1, weight=96.0)
    g.diag(515.0, 708.1, 469.0, 630.0, weight=96.0)
    g.hbar(286.6, 572.4, 590.7, weight=48.0)
    g.diag(572.4, 614.4, 598.3, 595.8, weight=48.0)
    g.diag(266.4, 540.4, 131.9, 378.5, weight=48.0)
    g.hbar(131.9, 338.1, 408.0, weight=48.0)
    g.hbar(338.1, 371.1, 441.6, weight=48.0)
    g.hbar(341.4, 394.0, 456.1, weight=48.0)
    g.diag(394.0, 451.6, 380.6, 427.4, weight=48.0)
    g.hbar(186.0, 187.7, 301.0, weight=48.0)
    g.diag(187.7, 301.1, 144.7, -45.2, weight=48.0)
    g.diag(192.2, 289.9, 321.0, 191.1, weight=48.0)
    g.vbar(329.7, -55.3, 191.1, weight=48.0)
    g.diag(338.4, -55.3, 254.1, -14.6, weight=48.0)
    g.diag(205.4, 200.4, 218.6, 216.7, weight=64.0)
    g.hbar(218.6, 332.7, 216.3, weight=64.0)
    g.diag(198.9, 103.7, 210.0, 118.4, weight=76.0)
    g.hbar(210.0, 329.7, 119.5, weight=76.0)
    g.diag(736.6, 465.5, 668.9, 512.8, weight=48.0)
    g.diag(668.9, 512.8, 540.0, 441.8, weight=48.0)
    g.diag(496.3, 586.2, 771.7, 308.4, weight=48.0)
    g.diag(771.7, 308.4, 712.8, 487.0, weight=48.0)
    g.diag(698.8, 306.6, 717.0, 231.2, weight=96.0)
    g.diag(717.0, 231.2, 542.9, 140.1, weight=96.0)
    g.diag(527.1, 338.5, 839.0, -40.5, weight=64.0)
    g.vbar(847.2, -40.5, 156.9, weight=64.0)
    return g
def g_cjk_unified_ideograph_7f85() -> Glyph:
    """羅 U+7F85 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7F85", advance=1000, unicode=0x7F85, note="羅：自动生成")
    g.vbar(263.8, 706.8, 721.0, weight=48.0)
    g.vbar(288.5, 564.4, 706.8, weight=48.0)
    g.hbar(276.4, 713.0, 733.9, weight=48.0)
    g.diag(713.0, 752.9, 630.4, 612.6, weight=48.0)
    g.dot(402.6, 659.8, w=96.0, h=101.5, slant=-14.0)
    g.diag(516.6, 731.7, 539.8, 707.4, weight=96.0)
    g.diag(539.8, 707.4, 504.3, 631.4, weight=96.0)
    g.hbar(329.8, 430.0, 584.4, weight=48.0)
    g.hbar(430.0, 630.9, 611.5, weight=48.0)
    g.diag(296.3, 554.1, 181.9, 330.3, weight=48.0)
    g.hbar(181.9, 286.9, 339.6, weight=48.0)
    g.diag(340.6, 449.8, 357.4, 415.2, weight=48.0)
    g.diag(357.4, 415.2, 201.8, 202.8, weight=48.0)
    g.hbar(201.8, 344.2, 224.9, weight=48.0)
    g.diag(344.2, 247.0, 348.5, 253.5, weight=48.0)
    g.dot(354.0, 255.0, w=48.0, h=35.8, slant=-14.0)
    g.diag(212.2, 116.7, 197.7, 17.5, weight=84.0)
    g.hbar(197.7, 273.5, 25.2, weight=84.0)
    g.diag(244.1, 184.9, 300.9, 52.5, weight=64.0)
    g.diag(325.9, 218.8, 390.7, 108.3, weight=56.0)
    g.diag(495.9, 583.2, 528.7, 501.6, weight=56.0)
    g.diag(528.7, 501.6, 366.8, 313.7, weight=56.0)
    g.diag(469.3, 379.8, 486.0, 269.3, weight=48.0)
    g.vbar(487.1, -62.0, 269.3, weight=48.0)
    g.dot(663.7, 511.1, w=96.0, h=124.8, slant=-14.0)
    g.hbar(527.9, 752.5, 408.4, weight=96.0)
    g.diag(752.5, 430.1, 728.9, 461.6, weight=96.0)
    g.hbar(527.1, 726.4, 292.4, weight=76.0)
    g.diag(726.4, 306.3, 767.2, 245.2, weight=76.0)
    g.hbar(527.1, 718.7, 194.4, weight=76.0)
    g.diag(718.7, 205.7, 767.2, 284.4, weight=76.0)
    g.diag(630.1, 377.9, 658.5, 354.3, weight=96.0)
    g.vbar(658.9, 122.5, 354.3, weight=96.0)
    g.diag(659.4, 122.5, 645.2, 100.7, weight=96.0)
    g.diag(522.2, 71.4, 529.3, 63.3, weight=96.0)
    g.hbar(529.3, 853.3, 71.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_7f9e() -> Glyph:
    """羞 U+7F9E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7F9E", advance=1000, unicode=0x7F9E, note="羞：自动生成")
    g.diag(403.1, 754.8, 480.0, 706.1, weight=96.0)
    g.diag(480.0, 706.1, 499.3, 643.5, weight=96.0)
    g.diag(648.2, 802.0, 668.3, 770.9, weight=96.0)
    g.diag(668.3, 770.9, 569.1, 655.1, weight=96.0)
    g.diag(344.3, 506.8, 417.2, 591.0, weight=96.0)
    g.hbar(417.2, 672.3, 612.1, weight=96.0)
    g.diag(672.3, 633.2, 660.9, 706.3, weight=96.0)
    g.diag(359.0, 380.2, 406.1, 462.4, weight=96.0)
    g.hbar(406.1, 651.3, 482.0, weight=96.0)
    g.diag(651.3, 501.6, 709.2, 420.2, weight=96.0)
    g.hbar(207.2, 869.3, 352.4, weight=84.0)
    g.diag(486.5, 569.9, 423.3, 395.3, weight=96.0)
    g.diag(423.3, 395.3, 110.7, -57.0, weight=96.0)
    g.hbar(408.9, 701.5, 262.5, weight=48.0)
    g.diag(701.5, 278.5, 739.2, 240.9, weight=48.0)
    g.diag(739.2, 240.9, 668.7, 9.5, weight=48.0)
    g.diag(518.6, 233.4, 546.2, 206.1, weight=96.0)
    g.diag(546.2, 206.1, 517.6, 24.4, weight=96.0)
    g.diag(517.6, 24.4, 498.5, 4.3, weight=96.0)
    g.hbar(342.7, 691.0, 128.3, weight=48.0)
    g.hbar(320.7, 867.3, -24.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_7fa8() -> Glyph:
    """羨 U+7FA8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7FA8", advance=1000, unicode=0x7FA8, note="羨：自动生成")
    g.diag(348.7, 750.5, 411.9, 708.9, weight=96.0)
    g.diag(411.9, 708.9, 433.1, 652.1, weight=96.0)
    g.diag(575.2, 792.0, 591.3, 762.7, weight=96.0)
    g.diag(591.3, 762.7, 500.9, 666.9, weight=96.0)
    g.vbar(320.4, 532.8, 593.8, weight=76.0)
    g.hbar(317.8, 661.1, 624.0, weight=76.0)
    g.diag(348.0, 440.9, 384.6, 502.2, weight=64.0)
    g.hbar(384.6, 562.0, 522.0, weight=64.0)
    g.diag(562.0, 541.9, 613.2, 485.9, weight=64.0)
    g.diag(450.6, 591.9, 472.3, 567.3, weight=96.0)
    g.vbar(471.4, 480.5, 567.3, weight=96.0)
    g.diag(470.5, 480.5, 455.4, 457.8, weight=96.0)
    g.hbar(235.7, 719.7, 408.3, weight=56.0)
    g.diag(240.8, 386.9, 323.2, 276.6, weight=56.0)
    g.vbar(211.7, 206.7, 311.8, weight=96.0)
    g.diag(215.6, 206.7, 271.6, 153.2, weight=96.0)
    g.hbar(191.3, 311.7, -44.3, weight=96.0)
    g.diag(191.3, -38.2, 352.4, 174.8, weight=96.0)
    g.diag(470.5, 402.1, 505.3, 362.3, weight=96.0)
    g.diag(505.3, 362.3, 359.1, 178.3, weight=96.0)
    g.hbar(493.1, 770.3, 320.4, weight=96.0)
    g.diag(770.3, 347.2, 598.2, 216.6, weight=96.0)
    g.diag(527.0, 269.5, 578.5, 174.6, weight=64.0)
    g.diag(578.5, 174.6, 349.6, -44.3, weight=64.0)
    g.diag(570.5, 137.8, 709.6, -22.0, weight=96.0)
    g.hbar(709.6, 831.0, -33.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_7fc1() -> Glyph:
    """翁 U+7FC1 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7FC1", advance=1000, unicode=0x7FC1, note="翁：自动生成")
    g.diag(407.2, 666.7, 381.6, 693.9, weight=96.0)
    g.diag(381.6, 693.9, 143.6, 529.4, weight=96.0)
    g.hbar(397.5, 496.4, 758.9, weight=96.0)
    g.diag(496.4, 770.6, 900.5, 574.5, weight=96.0)
    g.diag(428.3, 634.6, 450.4, 596.8, weight=48.0)
    g.diag(450.4, 596.8, 327.9, 442.9, weight=48.0)
    g.hbar(327.9, 591.6, 465.3, weight=48.0)
    g.diag(543.6, 556.5, 620.8, 487.3, weight=48.0)
    g.diag(620.8, 487.3, 645.9, 410.0, weight=48.0)
    g.hbar(179.5, 317.0, 274.1, weight=56.0)
    g.vbar(279.9, 29.8, 257.8, weight=56.0)
    g.hbar(242.8, 249.9, 28.5, weight=56.0)
    g.diag(186.2, 308.8, 265.5, 181.9, weight=76.0)
    g.hbar(99.5, 152.7, 77.3, weight=96.0)
    g.diag(152.7, 75.3, 334.2, 174.9, weight=96.0)
    g.hbar(487.2, 635.0, 297.7, weight=64.0)
    g.vbar(708.8, -85.2, 275.0, weight=64.0)
    g.hbar(578.7, 782.7, -40.0, weight=64.0)
    g.diag(492.7, 340.3, 593.5, 193.2, weight=64.0)
    g.hbar(412.0, 498.5, 100.1, weight=96.0)
    g.diag(498.5, 99.3, 675.6, 206.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_7ffb() -> Glyph:
    """翻 U+7FFB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7FFB", advance=1000, unicode=0x7FFB, note="翻：自动生成")
    g.hbar(401.4, 461.2, 765.7, weight=96.0)
    g.hbar(179.4, 401.4, 727.6, weight=96.0)
    g.diag(179.4, 683.0, 186.9, 689.0, weight=96.0)
    g.dot(205.8, 586.4, w=76.0, h=98.8, slant=-14.0)
    g.diag(464.5, 686.8, 480.7, 658.8, weight=48.0)
    g.diag(480.7, 658.8, 402.9, 575.6, weight=48.0)
    g.hbar(71.4, 495.8, 486.0, weight=48.0)
    g.diag(298.2, 703.0, 327.1, 563.7, weight=48.0)
    g.vbar(328.9, 295.9, 563.7, weight=48.0)
    g.diag(307.9, 464.4, 53.0, 249.4, weight=48.0)
    g.diag(353.2, 416.8, 468.8, 354.2, weight=64.0)
    g.diag(138.3, 237.6, 168.6, 210.7, weight=96.0)
    g.vbar(191.2, -44.3, 210.7, weight=96.0)
    g.hbar(205.3, 302.8, 220.3, weight=48.0)
    g.diag(302.8, 231.1, 424.1, 172.0, weight=48.0)
    g.vbar(429.9, 4.2, 172.0, weight=48.0)
    g.diag(435.7, 4.2, 439.6, -10.8, weight=48.0)
    g.dot(323.5, 126.3, w=96.0, h=124.8, slant=-14.0)
    g.diag(298.2, 222.4, 323.0, 198.7, weight=48.0)
    g.vbar(322.5, 55.0, 198.7, weight=48.0)
    g.diag(321.9, 55.0, 305.7, 30.2, weight=48.0)
    g.hbar(236.6, 401.8, 6.4, weight=96.0)
    g.diag(533.6, 558.3, 641.7, 364.6, weight=92.0)
    g.vbar(648.3, -8.0, 364.6, weight=92.0)
    g.hbar(547.6, 655.0, 15.9, weight=92.0)
    g.dot(561.7, 409.3, w=84.0, h=109.0, slant=-14.0)
    g.hbar(522.8, 559.5, 164.7, weight=96.0)
    g.diag(559.5, 169.5, 642.7, 265.6, weight=96.0)
    g.diag(755.0, 595.0, 853.6, 452.7, weight=96.0)
    g.diag(853.6, 452.7, 972.0, -72.0, weight=96.0)
    g.hbar(772.3, 972.0, -31.7, weight=96.0)
    g.dot(785.8, 439.5, w=96.0, h=103.2, slant=-14.0)
    g.hbar(742.0, 787.6, 193.8, weight=96.0)
    g.diag(787.6, 197.6, 878.1, 297.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_7ffc() -> Glyph:
    """翼 U+7FFC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni7FFC", advance=1000, unicode=0x7FFC, note="翼：自动生成")
    g.hbar(254.2, 453.8, 704.2, weight=48.0)
    g.diag(453.8, 728.1, 421.2, 517.8, weight=48.0)
    g.diag(258.0, 690.0, 342.3, 607.3, weight=48.0)
    g.diag(269.9, 510.3, 257.7, 539.8, weight=76.0)
    g.diag(257.7, 539.8, 358.5, 613.1, weight=76.0)
    g.hbar(532.2, 767.3, 737.4, weight=48.0)
    g.diag(767.3, 757.3, 662.2, 529.4, weight=48.0)
    g.diag(534.8, 726.3, 611.8, 641.3, weight=48.0)
    g.hbar(446.0, 535.4, 587.9, weight=48.0)
    g.hbar(535.4, 625.1, 600.7, weight=48.0)
    g.vbar(621.9, 620.8, 644.1, weight=48.0)
    g.vbar(338.4, 325.2, 496.3, weight=48.0)
    g.hbar(320.6, 676.1, 502.5, weight=48.0)
    g.vbar(650.9, 356.2, 509.6, weight=48.0)
    g.hbar(611.1, 625.8, 358.7, weight=48.0)
    g.hbar(367.7, 536.7, 424.2, weight=56.0)
    g.diag(536.7, 440.5, 590.6, 396.6, weight=56.0)
    g.diag(473.3, 489.3, 497.9, 464.7, weight=96.0)
    g.diag(497.9, 464.7, 477.2, 375.7, weight=96.0)
    g.hbar(385.1, 610.6, 353.7, weight=48.0)
    g.diag(328.0, 274.3, 314.1, 220.5, weight=96.0)
    g.hbar(314.1, 664.0, 244.5, weight=96.0)
    g.diag(664.0, 268.5, 657.9, 315.8, weight=96.0)
    g.diag(359.7, 296.0, 391.5, 267.1, weight=96.0)
    g.diag(391.5, 267.1, 405.6, 150.8, weight=96.0)
    g.diag(405.6, 150.8, 417.9, 143.6, weight=96.0)
    g.diag(555.8, 325.2, 586.9, 294.1, weight=96.0)
    g.diag(586.9, 294.1, 571.4, 176.6, weight=96.0)
    g.diag(571.4, 176.6, 554.9, 155.2, weight=96.0)
    g.hbar(131.5, 868.5, 113.0, weight=64.0)
    g.diag(394.8, 90.1, 209.2, -71.0, weight=64.0)
    g.diag(565.4, 112.3, 728.7, -72.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_8015() -> Glyph:
    """耕 U+8015 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8015", advance=1000, unicode=0x8015, note="耕：自动生成")
    g.hbar(153.2, 438.7, 600.3, weight=96.0)
    g.hbar(194.9, 409.5, 483.3, weight=76.0)
    g.hbar(59.9, 413.4, 363.8, weight=48.0)
    g.diag(267.8, 761.5, 295.9, 534.5, weight=48.0)
    g.vbar(288.6, -24.1, 534.5, weight=48.0)
    g.diag(275.5, 346.8, 58.0, 98.2, weight=48.0)
    g.dot(366.8, 251.2, w=96.0, h=98.4, slant=-14.0)
    g.hbar(476.5, 832.9, 527.0, weight=96.0)
    g.hbar(423.1, 932.0, 345.4, weight=96.0)
    g.vbar(518.3, 456.5, 647.9, weight=84.0)
    g.diag(520.2, 456.5, 385.3, 57.4, weight=84.0)
    g.diag(676.6, 771.2, 714.7, 488.0, weight=96.0)
    g.vbar(718.5, -56.2, 488.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_8017() -> Glyph:
    """耗 U+8017 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8017", advance=1000, unicode=0x8017, note="耗：自动生成")
    g.diag(203.6, 490.9, 271.5, 566.3, weight=92.0)
    g.hbar(271.5, 425.1, 587.5, weight=92.0)
    g.diag(425.1, 608.8, 492.2, 566.9, weight=92.0)
    g.diag(223.8, 377.1, 259.1, 452.7, weight=84.0)
    g.hbar(259.1, 470.0, 479.2, weight=84.0)
    g.hbar(94.7, 483.7, 363.9, weight=56.0)
    g.vbar(311.5, 489.7, 774.0, weight=48.0)
    g.vbar(322.1, -54.0, 489.7, weight=48.0)
    g.diag(318.5, 326.4, 93.7, 53.2, weight=48.0)
    g.diag(355.5, 271.7, 421.6, 211.1, weight=48.0)
    g.diag(421.6, 211.1, 430.0, 178.8, weight=48.0)
    g.hbar(728.2, 789.4, 643.1, weight=92.0)
    g.diag(728.2, 645.6, 480.6, 512.9, weight=92.0)
    g.diag(480.6, 512.9, 474.9, 508.5, weight=92.0)
    g.hbar(498.1, 747.0, 429.3, weight=92.0)
    g.diag(747.0, 456.5, 772.7, 362.5, weight=92.0)
    g.hbar(436.6, 818.7, 289.4, weight=92.0)
    g.diag(818.7, 331.5, 886.1, 271.5, weight=92.0)
    g.diag(569.1, 534.4, 596.7, 384.4, weight=92.0)
    g.diag(596.7, 384.4, 641.3, 74.2, weight=92.0)
    g.hbar(641.3, 909.1, 76.6, weight=92.0)
    g.diag(909.1, 78.9, 875.2, 288.1, weight=92.0)
    return g
def g_cjk_unified_ideograph_8056() -> Glyph:
    """聖 U+8056 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8056", advance=1000, unicode=0x8056, note="聖：自动生成")
    g.hbar(166.4, 559.9, 725.4, weight=92.0)
    g.diag(233.3, 673.3, 295.4, 615.5, weight=96.0)
    g.diag(295.4, 615.5, 233.7, 384.1, weight=96.0)
    g.diag(233.7, 384.1, 248.1, 394.9, weight=96.0)
    g.diag(393.7, 699.9, 431.7, 666.7, weight=96.0)
    g.vbar(427.4, 316.2, 666.7, weight=96.0)
    g.vbar(296.9, 580.8, 594.9, weight=76.0)
    g.hbar(299.4, 367.1, 598.2, weight=76.0)
    g.diag(291.4, 489.3, 303.4, 505.7, weight=76.0)
    g.hbar(303.4, 369.1, 506.9, weight=76.0)
    g.hbar(119.2, 175.1, 340.3, weight=92.0)
    g.hbar(175.1, 395.6, 376.7, weight=92.0)
    g.diag(516.6, 582.8, 573.7, 405.7, weight=48.0)
    g.diag(571.7, 579.8, 582.2, 570.5, weight=48.0)
    g.hbar(582.2, 732.7, 586.8, weight=48.0)
    g.diag(732.7, 603.0, 780.4, 571.8, weight=48.0)
    g.diag(780.4, 571.8, 751.8, 499.2, weight=48.0)
    g.diag(751.8, 499.2, 725.2, 484.4, weight=48.0)
    g.hbar(594.4, 775.4, 440.1, weight=48.0)
    g.hbar(603.0, 636.7, 275.8, weight=96.0)
    g.hbar(320.9, 603.0, 250.7, weight=96.0)
    g.hbar(297.3, 677.0, 131.7, weight=96.0)
    g.diag(449.7, 214.9, 477.3, 189.3, weight=96.0)
    g.vbar(476.8, 40.7, 189.3, weight=96.0)
    g.diag(476.3, 40.7, 461.6, 23.0, weight=96.0)
    g.hbar(123.1, 870.8, -16.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_805e() -> Glyph:
    """聞 U+805E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni805E", advance=1000, unicode=0x805E, note="聞：自动生成")
    g.diag(170.4, 708.8, 197.0, 495.4, weight=56.0)
    g.vbar(192.5, 10.1, 495.4, weight=56.0)
    g.hbar(242.3, 247.1, 687.1, weight=96.0)
    g.hbar(247.1, 376.6, 689.1, weight=96.0)
    g.vbar(364.5, 472.4, 692.2, weight=96.0)
    g.hbar(337.9, 352.3, 471.8, weight=96.0)
    g.diag(246.2, 556.0, 253.7, 569.7, weight=64.0)
    g.hbar(253.7, 314.2, 571.7, weight=64.0)
    g.diag(239.3, 453.5, 253.6, 470.7, weight=76.0)
    g.hbar(253.6, 322.1, 480.3, weight=76.0)
    g.diag(581.3, 755.1, 627.6, 503.8, weight=48.0)
    g.diag(629.6, 742.3, 642.0, 736.4, weight=48.0)
    g.diag(642.0, 736.4, 791.8, 457.2, weight=48.0)
    g.vbar(798.3, -39.8, 457.2, weight=48.0)
    g.diag(804.7, -39.8, 704.5, 8.1, weight=48.0)
    g.diag(647.3, 625.0, 668.2, 645.9, weight=76.0)
    g.hbar(668.2, 741.9, 644.8, weight=76.0)
    g.diag(648.3, 524.5, 659.6, 537.9, weight=84.0)
    g.hbar(659.6, 773.7, 544.8, weight=84.0)
    g.diag(773.7, 551.7, 788.3, 538.3, weight=84.0)
    g.hbar(338.9, 624.7, 435.3, weight=64.0)
    g.diag(369.4, 393.4, 393.1, 374.7, weight=96.0)
    g.vbar(398.3, 197.9, 374.7, weight=96.0)
    g.diag(403.5, 197.9, 386.2, 180.6, weight=96.0)
    g.diag(522.2, 426.0, 563.6, 396.8, weight=96.0)
    g.vbar(562.1, -52.0, 396.8, weight=96.0)
    g.diag(429.5, 326.4, 437.7, 339.3, weight=56.0)
    g.hbar(437.7, 514.3, 339.8, weight=56.0)
    g.diag(425.6, 239.7, 437.0, 254.9, weight=56.0)
    g.hbar(437.0, 517.2, 255.7, weight=56.0)
    g.hbar(268.9, 723.2, 164.8, weight=64.0)
    return g
def g_cjk_unified_ideograph_8077() -> Glyph:
    """職 U+8077 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8077", advance=1000, unicode=0x8077, note="職：自动生成")
    g.hbar(84.6, 388.9, 664.7, weight=96.0)
    g.diag(126.7, 610.7, 162.4, 586.5, weight=96.0)
    g.vbar(158.5, 219.9, 586.5, weight=96.0)
    g.diag(154.7, 219.9, 141.1, 208.7, weight=96.0)
    g.vbar(292.3, 466.0, 643.6, weight=84.0)
    g.vbar(309.2, -48.3, 466.0, weight=84.0)
    g.dot(224.9, 477.6, w=96.0, h=74.2, slant=-14.0)
    g.diag(186.4, 342.4, 197.0, 356.6, weight=96.0)
    g.hbar(197.0, 261.4, 356.7, weight=96.0)
    g.hbar(63.0, 359.1, 214.9, weight=96.0)
    g.dot(495.8, 741.8, w=96.0, h=96.7, slant=-14.0)
    g.hbar(399.2, 616.1, 622.5, weight=96.0)
    g.dot(432.6, 521.3, w=84.0, h=69.4, slant=-14.0)
    g.diag(551.3, 606.6, 579.7, 578.5, weight=84.0)
    g.diag(579.7, 578.5, 530.8, 465.8, weight=84.0)
    g.hbar(375.5, 832.0, 448.8, weight=96.0)
    g.vbar(400.6, 244.1, 344.4, weight=64.0)
    g.vbar(413.4, 73.0, 244.1, weight=64.0)
    g.hbar(439.3, 564.3, 334.6, weight=96.0)
    g.vbar(577.9, 35.0, 349.5, weight=96.0)
    g.dot(483.5, 222.1, w=96.0, h=92.0, slant=-14.0)
    g.dot(488.1, 101.3, w=96.0, h=104.0, slant=-14.0)
    g.diag(627.4, 778.3, 713.2, 503.9, weight=96.0)
    g.diag(713.2, 503.9, 888.4, -67.3, weight=96.0)
    g.diag(888.4, -67.3, 942.0, 144.0, weight=96.0)
    g.diag(817.6, 419.5, 844.6, 371.6, weight=96.0)
    g.diag(844.6, 371.6, 643.9, 160.4, weight=96.0)
    g.dot(815.0, 709.4, w=96.0, h=124.8, slant=-14.0)
    return g
def g_cjk_unified_ideograph_80f4() -> Glyph:
    """胴 U+80F4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni80F4", advance=1000, unicode=0x80F4, note="胴：自动生成")
    g.diag(207.7, 691.7, 178.8, 491.5, weight=48.0)
    g.diag(178.8, 491.5, 53.0, -9.4, weight=48.0)
    g.hbar(212.5, 338.1, 690.9, weight=48.0)
    g.vbar(350.0, 462.3, 703.7, weight=48.0)
    g.vbar(359.1, -1.0, 462.3, weight=48.0)
    g.diag(356.2, -1.0, 256.9, 45.4, weight=48.0)
    g.diag(238.7, 479.0, 259.9, 497.9, weight=96.0)
    g.hbar(259.9, 338.6, 495.3, weight=96.0)
    g.diag(217.2, 297.6, 227.9, 314.3, weight=96.0)
    g.hbar(227.9, 337.4, 313.4, weight=96.0)
    g.vbar(507.1, 488.5, 641.9, weight=56.0)
    g.vbar(493.3, 7.8, 488.5, weight=56.0)
    g.hbar(520.4, 860.2, 655.1, weight=48.0)
    g.diag(860.2, 681.6, 893.5, 467.4, weight=48.0)
    g.vbar(908.2, -8.9, 467.4, weight=48.0)
    g.hbar(756.0, 923.0, 15.0, weight=48.0)
    g.hbar(554.6, 861.5, 501.4, weight=96.0)
    g.diag(616.3, 346.6, 609.0, 330.9, weight=48.0)
    g.vbar(626.0, 192.1, 330.9, weight=48.0)
    g.hbar(627.3, 791.1, 351.3, weight=48.0)
    g.vbar(766.6, 252.4, 366.2, weight=48.0)
    g.diag(649.2, 207.9, 665.0, 222.6, weight=48.0)
    g.hbar(665.0, 772.1, 228.8, weight=48.0)
    g.vbar(772.2, 235.0, 258.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_80f8() -> Glyph:
    """胸 U+80F8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni80F8", advance=1000, unicode=0x80F8, note="胸：自动生成")
    g.diag(214.0, 660.7, 61.6, -56.2, weight=96.0)
    g.hbar(230.9, 339.4, 661.5, weight=48.0)
    g.vbar(352.2, 447.0, 681.6, weight=48.0)
    g.vbar(361.6, 33.1, 447.0, weight=48.0)
    g.hbar(254.3, 358.3, 52.5, weight=48.0)
    g.diag(248.9, 456.2, 255.8, 471.4, weight=96.0)
    g.hbar(255.8, 340.7, 475.1, weight=96.0)
    g.diag(232.7, 292.5, 242.4, 308.6, weight=96.0)
    g.hbar(242.4, 340.7, 311.9, weight=96.0)
    g.diag(649.3, 792.0, 628.1, 685.8, weight=48.0)
    g.diag(628.1, 685.8, 473.9, 442.2, weight=48.0)
    g.diag(590.4, 545.2, 848.6, 350.8, weight=48.0)
    g.vbar(846.7, -75.2, 350.8, weight=48.0)
    g.diag(844.7, -75.2, 710.7, -4.6, weight=48.0)
    g.diag(649.3, 525.9, 692.2, 426.7, weight=64.0)
    g.diag(692.2, 426.7, 510.6, 201.9, weight=64.0)
    g.diag(538.4, 396.9, 735.9, 213.9, weight=48.0)
    g.diag(417.5, 313.0, 490.0, 273.2, weight=96.0)
    g.vbar(485.1, 134.8, 273.2, weight=96.0)
    g.hbar(480.1, 736.1, 162.1, weight=96.0)
    g.diag(736.1, 189.3, 750.5, 201.0, weight=96.0)
    g.diag(698.1, 389.8, 800.0, 323.7, weight=84.0)
    g.diag(800.0, 323.7, 730.8, 22.8, weight=84.0)
    return g
def g_cjk_unified_ideograph_8102() -> Glyph:
    """脂 U+8102 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8102", advance=1000, unicode=0x8102, note="脂：自动生成")
    g.diag(240.4, 689.2, 207.0, 482.4, weight=48.0)
    g.diag(207.0, 482.4, 66.1, -67.0, weight=48.0)
    g.hbar(240.8, 376.5, 687.2, weight=48.0)
    g.vbar(388.9, 449.7, 697.9, weight=48.0)
    g.vbar(396.7, -27.6, 449.7, weight=48.0)
    g.hbar(269.4, 392.0, -0.1, weight=48.0)
    g.dot(321.0, 473.6, w=96.0, h=113.3, slant=-14.0)
    g.dot(308.5, 305.8, w=96.0, h=124.8, slant=-14.0)
    g.diag(900.5, 626.8, 836.1, 680.5, weight=96.0)
    g.diag(836.1, 680.5, 632.7, 579.7, weight=96.0)
    g.diag(632.7, 579.7, 628.4, 569.8, weight=96.0)
    g.diag(562.8, 772.0, 548.7, 785.8, weight=96.0)
    g.diag(548.7, 785.8, 643.7, 426.6, weight=96.0)
    g.hbar(643.7, 915.7, 441.9, weight=96.0)
    g.vbar(906.0, 457.1, 642.7, weight=96.0)
    g.diag(598.5, 304.9, 597.5, 303.7, weight=48.0)
    g.vbar(582.8, -3.7, 303.7, weight=48.0)
    g.diag(568.1, -3.7, 598.1, -37.1, weight=48.0)
    g.hbar(600.3, 822.2, 307.8, weight=48.0)
    g.diag(822.2, 322.5, 853.8, 196.7, weight=48.0)
    g.vbar(853.5, -30.9, 196.7, weight=48.0)
    g.diag(853.2, -30.9, 796.2, 8.6, weight=48.0)
    g.hbar(617.2, 829.5, 142.7, weight=96.0)
    g.diag(610.6, -22.5, 626.1, -7.0, weight=96.0)
    g.hbar(626.1, 782.8, 3.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_8108() -> Glyph:
    """脈 U+8108 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8108", advance=1000, unicode=0x8108, note="脈：自动生成")
    g.diag(181.3, 600.6, 58.0, -20.5, weight=56.0)
    g.hbar(192.4, 295.6, 600.8, weight=48.0)
    g.vbar(305.2, 389.7, 614.8, weight=48.0)
    g.vbar(312.2, 15.4, 389.7, weight=48.0)
    g.diag(309.7, 15.4, 224.0, 66.3, weight=48.0)
    g.diag(214.7, 404.9, 235.2, 423.6, weight=96.0)
    g.hbar(235.2, 290.5, 423.0, weight=96.0)
    g.diag(198.9, 259.4, 207.7, 273.3, weight=96.0)
    g.hbar(207.7, 289.2, 275.2, weight=96.0)
    g.diag(634.5, 730.5, 654.2, 689.0, weight=96.0)
    g.diag(654.2, 689.0, 504.5, 574.6, weight=96.0)
    g.diag(504.5, 574.6, 502.0, 567.2, weight=96.0)
    g.diag(483.2, 571.2, 459.7, 409.5, weight=48.0)
    g.diag(459.7, 409.5, 336.2, 30.5, weight=48.0)
    g.diag(751.8, 471.7, 706.6, 531.1, weight=96.0)
    g.diag(706.6, 531.1, 604.6, 448.5, weight=96.0)
    g.vbar(604.6, 443.2, 448.5, weight=96.0)
    g.diag(496.4, 467.3, 552.1, 323.0, weight=48.0)
    g.diag(552.1, 323.0, 602.1, 33.6, weight=48.0)
    g.diag(602.1, 33.6, 695.1, 114.8, weight=48.0)
    g.diag(700.3, 481.6, 770.7, 401.5, weight=84.0)
    g.diag(770.7, 401.5, 666.6, 290.6, weight=84.0)
    g.diag(666.6, 290.6, 667.1, 286.4, weight=84.0)
    g.diag(590.3, 340.5, 947.0, 100.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_810a() -> Glyph:
    """脊 U+810A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni810A", advance=1000, unicode=0x810A, note="脊：自动生成")
    g.dot(271.3, 658.2, w=96.0, h=124.8, slant=-14.0)
    g.hbar(174.3, 219.7, 515.0, weight=56.0)
    g.diag(219.7, 511.6, 332.8, 618.4, weight=56.0)
    g.diag(659.9, 757.3, 667.8, 723.8, weight=84.0)
    g.diag(667.8, 723.8, 553.7, 654.0, weight=84.0)
    g.diag(565.2, 631.6, 702.3, 543.2, weight=76.0)
    g.diag(433.9, 782.0, 367.1, 588.5, weight=48.0)
    g.diag(367.1, 588.5, 68.7, 239.2, weight=48.0)
    g.diag(462.4, 609.9, 931.3, 311.2, weight=76.0)
    g.vbar(310.6, -47.1, 340.5, weight=48.0)
    g.hbar(343.6, 427.7, 337.8, weight=48.0)
    g.diag(427.7, 339.8, 545.2, 234.4, weight=48.0)
    g.vbar(539.6, -36.9, 234.4, weight=48.0)
    g.hbar(492.1, 534.1, -29.2, weight=48.0)
    g.hbar(353.9, 560.8, 225.6, weight=76.0)
    g.hbar(344.8, 566.7, 122.9, weight=76.0)
    return g
def g_cjk_unified_ideograph_811a() -> Glyph:
    """脚 U+811A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni811A", advance=1000, unicode=0x811A, note="脚：自动生成")
    g.diag(197.9, 709.2, 175.7, 534.7, weight=48.0)
    g.diag(175.7, 534.7, 71.6, 74.3, weight=48.0)
    g.hbar(202.1, 295.7, 706.8, weight=48.0)
    g.vbar(309.2, 480.5, 715.4, weight=48.0)
    g.vbar(317.5, 73.2, 480.5, weight=48.0)
    g.hbar(206.8, 312.2, 93.6, weight=48.0)
    g.diag(227.1, 511.6, 237.3, 526.9, weight=96.0)
    g.hbar(237.3, 295.8, 526.9, weight=96.0)
    g.diag(213.9, 363.1, 221.3, 377.8, weight=96.0)
    g.hbar(221.3, 296.9, 379.2, weight=96.0)
    g.hbar(372.4, 649.5, 562.7, weight=96.0)
    g.diag(495.6, 777.0, 535.3, 743.4, weight=96.0)
    g.vbar(529.7, 460.8, 743.4, weight=96.0)
    g.diag(524.1, 460.8, 508.8, 437.4, weight=96.0)
    g.hbar(373.6, 688.5, 415.4, weight=96.0)
    g.diag(488.9, 389.7, 517.9, 352.7, weight=48.0)
    g.diag(517.9, 352.7, 427.3, 180.7, weight=48.0)
    g.hbar(427.3, 614.3, 208.9, weight=48.0)
    g.diag(531.1, 338.5, 706.4, 170.7, weight=48.0)
    g.diag(744.0, 555.8, 863.2, 501.6, weight=48.0)
    g.vbar(865.7, 319.4, 501.6, weight=48.0)
    g.hbar(745.7, 868.2, 336.3, weight=48.0)
    g.diag(649.0, 580.3, 705.6, 458.4, weight=48.0)
    g.vbar(715.0, -67.0, 458.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_814e() -> Glyph:
    """腎 U+814E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni814E", advance=1000, unicode=0x814E, note="腎：自动生成")
    g.diag(184.4, 723.2, 201.0, 714.9, weight=96.0)
    g.hbar(201.0, 369.9, 736.3, weight=96.0)
    g.hbar(369.9, 466.7, 744.0, weight=96.0)
    g.diag(287.2, 712.5, 310.3, 690.5, weight=96.0)
    g.diag(310.3, 690.5, 280.4, 644.6, weight=96.0)
    g.hbar(184.0, 403.4, 615.2, weight=48.0)
    g.diag(403.4, 637.2, 344.2, 557.8, weight=48.0)
    g.hbar(178.8, 376.2, 526.7, weight=48.0)
    g.diag(299.8, 504.9, 317.2, 487.6, weight=96.0)
    g.diag(317.2, 487.6, 291.1, 443.8, weight=96.0)
    g.vbar(159.5, 388.2, 728.9, weight=48.0)
    g.hbar(153.0, 436.6, 416.9, weight=48.0)
    g.hbar(489.5, 767.9, 729.9, weight=96.0)
    g.diag(767.9, 772.5, 446.3, 462.2, weight=96.0)
    g.diag(483.9, 675.6, 914.0, 440.9, weight=96.0)
    g.vbar(290.4, -38.4, 342.1, weight=48.0)
    g.diag(316.3, 329.2, 529.0, 230.5, weight=48.0)
    g.diag(529.0, 230.5, 566.5, -49.8, weight=48.0)
    g.diag(566.5, -49.8, 480.3, -5.4, weight=48.0)
    g.hbar(333.8, 566.7, 247.1, weight=76.0)
    g.diag(325.1, 130.4, 337.4, 140.9, weight=84.0)
    g.hbar(337.4, 567.8, 145.9, weight=84.0)
    return g
def g_cjk_unified_ideograph_8150() -> Glyph:
    """腐 U+8150 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8150", advance=1000, unicode=0x8150, note="腐：自动生成")
    g.diag(491.0, 797.0, 568.3, 757.2, weight=48.0)
    g.diag(568.3, 757.2, 593.2, 695.0, weight=48.0)
    g.hbar(344.1, 741.9, 679.8, weight=96.0)
    g.diag(741.9, 697.3, 751.1, 653.0, weight=96.0)
    g.diag(319.4, 668.9, 270.2, 475.3, weight=64.0)
    g.diag(270.2, 475.3, 81.8, -48.8, weight=64.0)
    g.diag(454.9, 632.9, 475.7, 575.9, weight=48.0)
    g.diag(475.7, 575.9, 413.4, 479.1, weight=48.0)
    g.diag(413.4, 479.1, 316.5, 435.4, weight=48.0)
    g.vbar(452.2, 270.8, 493.2, weight=48.0)
    g.hbar(495.6, 543.1, 523.9, weight=96.0)
    g.hbar(543.1, 898.2, 534.8, weight=96.0)
    g.diag(704.6, 655.6, 755.2, 592.7, weight=96.0)
    g.vbar(743.2, 378.3, 592.7, weight=96.0)
    g.hbar(643.8, 731.2, 394.1, weight=96.0)
    g.dot(581.9, 441.4, w=96.0, h=85.6, slant=-14.0)
    g.diag(386.4, 253.5, 378.1, 248.2, weight=96.0)
    g.diag(378.1, 248.2, 423.8, -15.1, weight=96.0)
    g.hbar(407.4, 748.4, 261.8, weight=48.0)
    g.diag(748.4, 292.4, 779.5, 151.9, weight=48.0)
    g.vbar(774.7, -68.1, 151.9, weight=48.0)
    g.diag(769.9, -68.1, 676.8, -7.9, weight=48.0)
    g.diag(553.5, 288.4, 498.2, 197.4, weight=56.0)
    g.diag(498.2, 197.4, 410.9, 144.2, weight=56.0)
    g.diag(561.8, 210.2, 673.3, 156.8, weight=48.0)
    g.diag(533.4, 169.4, 569.0, 120.3, weight=48.0)
    g.diag(569.0, 120.3, 456.6, 4.9, weight=48.0)
    g.hbar(557.9, 575.4, 68.4, weight=96.0)
    g.diag(575.4, 70.0, 660.8, 30.1, weight=96.0)
    g.diag(660.8, 30.1, 675.5, -0.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_8155() -> Glyph:
    """腕 U+8155 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8155", advance=1000, unicode=0x8155, note="腕：自动生成")
    g.diag(194.9, 650.0, 167.3, 470.4, weight=48.0)
    g.diag(167.3, 470.4, 53.0, -12.7, weight=48.0)
    g.diag(204.5, 641.6, 294.5, 444.1, weight=64.0)
    g.vbar(301.3, 43.5, 444.1, weight=64.0)
    g.hbar(217.7, 308.1, 60.1, weight=64.0)
    g.diag(217.7, 443.4, 227.9, 455.8, weight=96.0)
    g.hbar(227.9, 287.8, 454.1, weight=96.0)
    g.diag(199.7, 273.6, 208.0, 288.9, weight=96.0)
    g.hbar(208.0, 287.8, 289.8, weight=96.0)
    g.diag(578.4, 749.7, 647.7, 705.5, weight=48.0)
    g.diag(647.7, 705.5, 679.9, 628.1, weight=48.0)
    g.diag(454.7, 590.9, 426.3, 509.7, weight=64.0)
    g.diag(426.3, 509.7, 455.1, 465.4, weight=64.0)
    g.hbar(473.9, 812.3, 594.9, weight=96.0)
    g.diag(812.3, 615.8, 755.8, 436.6, weight=96.0)
    g.diag(438.1, 482.7, 506.8, 439.0, weight=48.0)
    g.diag(506.8, 439.0, 403.4, 256.1, weight=48.0)
    g.diag(403.4, 256.1, 405.5, 253.4, weight=48.0)
    g.diag(471.6, 329.0, 506.9, 237.0, weight=48.0)
    g.diag(506.9, 237.0, 352.3, -24.7, weight=48.0)
    g.hbar(424.7, 432.5, 255.1, weight=96.0)
    g.diag(432.5, 255.6, 489.6, 203.2, weight=96.0)
    g.hbar(672.7, 838.5, 394.2, weight=48.0)
    g.vbar(807.4, 204.2, 404.4, weight=48.0)
    g.hbar(671.9, 776.4, 221.9, weight=48.0)
    g.vbar(660.7, 277.7, 390.4, weight=48.0)
    g.vbar(678.7, -7.7, 277.7, weight=48.0)
    g.hbar(697.7, 943.5, 0.1, weight=48.0)
    g.vbar(945.2, 7.8, 151.1, weight=48.0)
    return g
def g_cjk_unified_ideograph_8170() -> Glyph:
    """腰 U+8170 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8170", advance=1000, unicode=0x8170, note="腰：自动生成")
    g.diag(200.6, 666.7, 173.6, 483.3, weight=48.0)
    g.diag(173.6, 483.3, 51.0, -28.9, weight=48.0)
    g.diag(201.6, 656.1, 299.4, 433.8, weight=48.0)
    g.vbar(306.6, 23.5, 433.8, weight=48.0)
    g.hbar(215.8, 313.8, 43.6, weight=48.0)
    g.diag(229.6, 461.4, 246.3, 481.1, weight=92.0)
    g.hbar(246.3, 297.9, 482.7, weight=92.0)
    g.diag(215.8, 312.4, 224.6, 327.6, weight=92.0)
    g.hbar(224.6, 299.2, 330.5, weight=92.0)
    g.vbar(496.6, 654.8, 669.5, weight=92.0)
    g.hbar(499.6, 801.8, 694.2, weight=92.0)
    g.vbar(432.4, 518.7, 531.3, weight=48.0)
    g.vbar(456.3, 354.3, 518.7, weight=48.0)
    g.hbar(446.4, 833.1, 542.0, weight=48.0)
    g.diag(833.1, 558.1, 754.2, 397.1, weight=48.0)
    g.diag(515.5, 643.1, 576.5, 427.2, weight=76.0)
    g.diag(576.5, 427.2, 555.1, 408.1, weight=76.0)
    g.diag(646.9, 670.6, 686.0, 638.9, weight=64.0)
    g.diag(686.0, 638.9, 640.0, 420.0, weight=64.0)
    g.hbar(493.5, 750.3, 389.4, weight=48.0)
    g.diag(561.1, 367.7, 591.9, 336.2, weight=92.0)
    g.diag(591.9, 336.2, 517.7, 150.1, weight=92.0)
    g.diag(517.7, 150.1, 825.5, -27.9, weight=92.0)
    g.diag(681.4, 293.7, 756.5, 221.5, weight=92.0)
    g.diag(756.5, 221.5, 361.9, 25.4, weight=92.0)
    g.hbar(373.7, 934.0, 247.3, weight=92.0)
    return g
def g_cjk_unified_ideograph_8178() -> Glyph:
    """腸 U+8178 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8178", advance=1000, unicode=0x8178, note="腸：自动生成")
    g.diag(198.2, 662.0, 176.6, 486.4, weight=96.0)
    g.diag(176.6, 486.4, 58.0, 4.1, weight=96.0)
    g.diag(217.7, 641.5, 303.6, 686.7, weight=48.0)
    g.vbar(316.4, 453.4, 686.7, weight=48.0)
    g.vbar(327.2, 55.9, 453.4, weight=48.0)
    g.hbar(225.5, 325.2, 78.3, weight=48.0)
    g.diag(230.4, 477.0, 238.8, 492.5, weight=96.0)
    g.hbar(238.8, 305.3, 493.6, weight=96.0)
    g.diag(216.6, 334.2, 225.7, 348.4, weight=96.0)
    g.hbar(225.7, 305.3, 351.2, weight=96.0)
    g.vbar(520.7, 707.2, 720.8, weight=48.0)
    g.vbar(531.1, 468.1, 707.2, weight=48.0)
    g.hbar(534.1, 728.7, 715.1, weight=48.0)
    g.vbar(708.8, 486.6, 717.7, weight=48.0)
    g.hbar(669.0, 688.9, 487.7, weight=48.0)
    g.diag(560.4, 586.4, 576.3, 607.9, weight=84.0)
    g.hbar(576.3, 675.0, 607.1, weight=84.0)
    g.diag(561.4, 476.0, 569.3, 486.9, weight=64.0)
    g.hbar(569.3, 661.9, 496.7, weight=64.0)
    g.hbar(374.1, 922.0, 396.2, weight=76.0)
    g.diag(491.4, 362.2, 512.4, 337.7, weight=48.0)
    g.diag(512.4, 337.7, 454.7, 253.0, weight=48.0)
    g.hbar(362.9, 454.7, 235.0, weight=48.0)
    g.hbar(504.3, 852.5, 295.1, weight=96.0)
    g.diag(852.5, 309.2, 714.0, -41.1, weight=96.0)
    g.diag(714.0, -41.1, 595.5, 38.5, weight=96.0)
    g.diag(566.4, 252.4, 463.9, 116.9, weight=76.0)
    g.hbar(370.3, 463.9, 111.5, weight=76.0)
    g.diag(652.1, 272.1, 688.9, 230.8, weight=84.0)
    g.diag(688.9, 230.8, 439.0, -59.2, weight=84.0)
    g.diag(439.0, -59.2, 443.2, -42.2, weight=84.0)
    return g
def g_cjk_unified_ideograph_817a() -> Glyph:
    """腺 U+817A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni817A", advance=1000, unicode=0x817A, note="腺：自动生成")
    g.vbar(170.3, 459.6, 621.4, weight=96.0)
    g.diag(161.9, 459.6, 53.0, -2.4, weight=96.0)
    g.diag(197.8, 602.8, 291.2, 415.1, weight=48.0)
    g.vbar(297.3, 11.5, 415.1, weight=48.0)
    g.diag(303.3, 11.5, 209.7, 59.9, weight=48.0)
    g.diag(213.5, 430.0, 233.3, 447.9, weight=96.0)
    g.hbar(233.3, 284.6, 447.0, weight=96.0)
    g.diag(197.4, 278.0, 221.0, 299.5, weight=96.0)
    g.hbar(221.0, 284.6, 299.2, weight=96.0)
    g.diag(541.1, 753.8, 570.2, 725.3, weight=56.0)
    g.diag(570.2, 725.3, 496.1, 600.6, weight=56.0)
    g.diag(496.1, 600.6, 492.2, 597.1, weight=56.0)
    g.vbar(454.2, 358.3, 576.3, weight=48.0)
    g.hbar(440.3, 636.5, 546.7, weight=48.0)
    g.vbar(649.6, 391.3, 520.5, weight=48.0)
    g.hbar(639.8, 662.7, 390.9, weight=48.0)
    g.diag(481.3, 464.9, 498.4, 481.5, weight=64.0)
    g.hbar(498.4, 661.9, 478.2, weight=64.0)
    g.hbar(494.8, 632.6, 390.8, weight=76.0)
    g.diag(554.9, 366.8, 573.4, 218.9, weight=64.0)
    g.vbar(568.9, -34.5, 218.9, weight=64.0)
    g.diag(564.5, -34.5, 430.0, 51.3, weight=64.0)
    g.hbar(341.5, 516.9, 251.8, weight=48.0)
    g.diag(516.9, 254.3, 402.8, 51.6, weight=48.0)
    g.hbar(331.9, 402.8, 41.2, weight=48.0)
    g.diag(745.0, 367.7, 760.1, 337.4, weight=48.0)
    g.diag(760.1, 337.4, 650.4, 229.9, weight=48.0)
    g.hbar(638.7, 650.4, 229.6, weight=48.0)
    g.diag(610.0, 244.0, 947.0, 54.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_819c() -> Glyph:
    """膜 U+819C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni819C", advance=1000, unicode=0x819C, note="膜：自动生成")
    g.diag(185.1, 636.1, 164.1, 461.8, weight=48.0)
    g.diag(164.1, 461.8, 53.0, -25.0, weight=48.0)
    g.hbar(190.6, 302.7, 636.5, weight=48.0)
    g.vbar(315.3, 417.6, 646.4, weight=48.0)
    g.vbar(321.1, -4.9, 417.6, weight=48.0)
    g.diag(314.3, -4.9, 218.9, 42.3, weight=48.0)
    g.diag(216.9, 418.9, 239.4, 440.4, weight=96.0)
    g.hbar(239.4, 301.2, 441.0, weight=96.0)
    g.diag(199.4, 256.9, 217.7, 276.4, weight=96.0)
    g.hbar(217.7, 303.8, 274.6, weight=96.0)
    g.hbar(375.8, 847.2, 610.5, weight=96.0)
    g.diag(488.2, 697.0, 524.3, 674.5, weight=48.0)
    g.diag(524.3, 674.5, 566.8, 480.9, weight=48.0)
    g.vbar(706.6, 670.5, 693.0, weight=96.0)
    g.diag(706.3, 693.0, 660.4, 521.1, weight=96.0)
    g.vbar(464.7, 441.9, 457.5, weight=48.0)
    g.vbar(485.7, 259.8, 441.9, weight=48.0)
    g.hbar(475.2, 762.4, 463.6, weight=48.0)
    g.vbar(736.0, 293.0, 477.1, weight=48.0)
    g.hbar(692.0, 709.7, 294.1, weight=48.0)
    g.diag(511.6, 355.8, 528.9, 372.5, weight=64.0)
    g.hbar(528.9, 704.8, 370.7, weight=64.0)
    g.diag(524.3, 271.6, 533.9, 282.1, weight=64.0)
    g.hbar(533.9, 686.8, 294.2, weight=64.0)
    g.hbar(362.4, 911.6, 167.1, weight=48.0)
    g.diag(566.2, 264.7, 628.9, 203.8, weight=64.0)
    g.diag(628.9, 203.8, 465.2, -37.5, weight=64.0)
    g.hbar(346.8, 465.2, -26.5, weight=64.0)
    g.diag(621.2, 154.1, 788.7, -23.1, weight=48.0)
    g.hbar(788.7, 937.0, -35.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_819d() -> Glyph:
    """膝 U+819D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni819D", advance=1000, unicode=0x819D, note="膝：自动生成")
    g.vbar(159.1, 484.1, 687.0, weight=48.0)
    g.diag(160.4, 484.1, 53.0, -1.1, weight=48.0)
    g.diag(216.6, 681.2, 286.6, 542.6, weight=96.0)
    g.diag(286.6, 542.6, 388.7, 30.4, weight=96.0)
    g.hbar(227.2, 388.7, 60.4, weight=96.0)
    g.diag(228.1, 476.2, 238.5, 492.9, weight=96.0)
    g.hbar(238.5, 283.0, 492.7, weight=96.0)
    g.diag(210.8, 318.4, 218.5, 332.4, weight=96.0)
    g.hbar(218.5, 286.8, 335.5, weight=96.0)
    g.hbar(444.7, 774.7, 639.8, weight=48.0)
    g.diag(562.1, 766.9, 597.8, 731.5, weight=96.0)
    g.vbar(593.9, 479.1, 731.5, weight=96.0)
    g.diag(567.8, 597.5, 402.3, 444.5, weight=48.0)
    g.diag(664.1, 565.7, 787.3, 484.9, weight=64.0)
    g.hbar(601.9, 609.2, 440.4, weight=96.0)
    g.diag(601.9, 439.2, 363.8, 224.1, weight=96.0)
    g.hbar(590.1, 613.1, 407.9, weight=96.0)
    g.hbar(590.1, 947.0, 341.1, weight=96.0)
    g.diag(565.0, 309.8, 588.2, 182.6, weight=48.0)
    g.vbar(584.5, -33.5, 182.6, weight=48.0)
    g.diag(580.8, -33.5, 484.1, 14.3, weight=48.0)
    g.dot(490.9, 201.0, w=96.0, h=75.8, slant=-14.0)
    g.hbar(395.6, 437.0, 54.7, weight=96.0)
    g.diag(437.0, 54.7, 539.9, 135.6, weight=96.0)
    g.diag(724.7, 264.5, 737.2, 238.5, weight=64.0)
    g.diag(737.2, 238.5, 680.4, 176.0, weight=64.0)
    g.diag(687.2, 130.8, 831.5, 14.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_81a8() -> Glyph:
    """膨 U+81A8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni81A8", advance=1000, unicode=0x81A8, note="膨：自动生成")
    g.vbar(214.1, 512.7, 676.7, weight=48.0)
    g.diag(217.2, 512.7, 124.5, 62.8, weight=48.0)
    g.diag(268.0, 670.8, 353.9, 471.3, weight=48.0)
    g.vbar(356.5, 89.2, 471.3, weight=48.0)
    g.diag(359.1, 89.2, 268.1, 131.8, weight=48.0)
    g.diag(278.2, 498.1, 286.5, 511.0, weight=96.0)
    g.hbar(286.5, 329.7, 511.9, weight=96.0)
    g.diag(263.5, 344.4, 269.5, 356.6, weight=96.0)
    g.hbar(269.5, 326.0, 359.2, weight=96.0)
    g.hbar(424.5, 674.9, 624.2, weight=76.0)
    g.diag(524.9, 777.0, 561.7, 742.9, weight=96.0)
    g.vbar(556.6, 553.3, 742.9, weight=96.0)
    g.diag(551.5, 553.3, 537.7, 535.9, weight=96.0)
    g.hbar(465.0, 650.9, 519.8, weight=56.0)
    g.diag(444.8, 444.7, 469.6, 419.0, weight=56.0)
    g.vbar(480.7, 309.4, 419.0, weight=56.0)
    g.hbar(491.7, 646.3, 438.8, weight=48.0)
    g.diag(646.3, 453.1, 625.2, 392.3, weight=48.0)
    g.diag(625.2, 392.3, 606.8, 379.4, weight=48.0)
    g.diag(507.4, 334.3, 516.3, 343.3, weight=48.0)
    g.hbar(516.3, 649.1, 349.4, weight=48.0)
    g.dot(478.8, 241.8, w=64.0, h=65.2, slant=-14.0)
    g.diag(603.1, 307.6, 616.3, 278.4, weight=96.0)
    g.diag(616.3, 278.4, 575.5, 199.9, weight=96.0)
    g.hbar(422.7, 462.5, 146.4, weight=96.0)
    g.hbar(462.5, 680.4, 178.6, weight=96.0)
    g.diag(821.2, 701.5, 849.4, 655.1, weight=96.0)
    g.diag(849.4, 655.1, 718.1, 491.7, weight=96.0)
    g.diag(834.1, 479.7, 856.7, 436.4, weight=76.0)
    g.diag(856.7, 436.4, 708.9, 292.9, weight=76.0)
    g.diag(848.8, 315.0, 787.2, 190.9, weight=56.0)
    g.diag(787.2, 190.9, 526.7, -67.0, weight=56.0)
    return g
def g_cjk_unified_ideograph_81b3() -> Glyph:
    """膳 U+81B3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni81B3", advance=1000, unicode=0x81B3, note="膳：自动生成")
    g.diag(192.5, 688.8, 51.0, 38.6, weight=56.0)
    g.diag(214.8, 686.4, 291.4, 554.3, weight=92.0)
    g.diag(291.4, 554.3, 380.9, 20.5, weight=92.0)
    g.hbar(145.0, 380.9, 71.4, weight=92.0)
    g.diag(220.9, 473.2, 233.5, 486.9, weight=92.0)
    g.hbar(233.5, 301.5, 487.5, weight=92.0)
    g.dot(253.3, 323.1, w=92.0, h=107.6, slant=-14.0)
    g.dot(532.9, 681.0, w=92.0, h=119.6, slant=-14.0)
    g.diag(719.5, 791.5, 748.5, 753.8, weight=92.0)
    g.diag(748.5, 753.8, 657.8, 660.5, weight=92.0)
    g.vbar(658.1, 639.5, 660.5, weight=92.0)
    g.diag(488.5, 522.3, 499.7, 581.2, weight=76.0)
    g.hbar(499.7, 795.7, 598.8, weight=76.0)
    g.diag(498.7, 553.1, 538.5, 483.2, weight=76.0)
    g.hbar(538.5, 732.3, 496.3, weight=76.0)
    g.diag(732.3, 509.4, 763.4, 449.1, weight=76.0)
    g.hbar(457.6, 797.0, 387.8, weight=76.0)
    g.vbar(795.6, 387.1, 422.9, weight=76.0)
    g.diag(599.0, 565.9, 627.3, 545.2, weight=92.0)
    g.vbar(625.1, 268.3, 545.2, weight=92.0)
    g.diag(622.9, 268.3, 608.2, 249.7, weight=92.0)
    g.dot(497.1, 299.3, w=92.0, h=106.5, slant=-14.0)
    g.diag(768.2, 393.2, 779.2, 341.4, weight=64.0)
    g.diag(779.2, 341.4, 702.7, 263.2, weight=64.0)
    g.hbar(376.9, 944.0, 220.0, weight=76.0)
    g.vbar(500.3, -54.4, 121.4, weight=92.0)
    g.hbar(493.2, 746.0, 129.2, weight=48.0)
    g.diag(746.0, 146.0, 783.0, 108.9, weight=48.0)
    g.diag(783.0, 108.9, 726.2, 8.2, weight=48.0)
    g.hbar(532.2, 761.7, -13.6, weight=48.0)
    g.vbar(761.6, -11.6, 16.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_81e8() -> Glyph:
    """臨 U+81E8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni81E8", advance=1000, unicode=0x81E8, note="臨：自动生成")
    g.hbar(167.8, 381.3, 671.7, weight=96.0)
    g.hbar(381.3, 533.0, 670.9, weight=96.0)
    g.diag(286.4, 631.9, 320.7, 611.4, weight=96.0)
    g.diag(320.7, 611.4, 298.5, 479.3, weight=96.0)
    g.diag(298.5, 479.3, 279.8, 457.3, weight=96.0)
    g.hbar(164.4, 363.7, 426.7, weight=48.0)
    g.diag(363.7, 455.4, 400.5, 423.3, weight=48.0)
    g.diag(400.5, 423.3, 375.3, 334.4, weight=48.0)
    g.diag(375.3, 334.4, 388.2, 306.3, weight=48.0)
    g.hbar(163.4, 397.7, 282.0, weight=48.0)
    g.diag(277.4, 255.3, 311.3, 230.9, weight=48.0)
    g.diag(311.3, 230.9, 279.4, 64.4, weight=48.0)
    g.vbar(145.9, 513.1, 658.9, weight=48.0)
    g.vbar(134.2, 15.0, 513.1, weight=48.0)
    g.hbar(126.2, 416.1, 35.0, weight=48.0)
    g.diag(597.0, 802.0, 633.9, 758.2, weight=96.0)
    g.diag(633.9, 758.2, 488.6, 479.2, weight=96.0)
    g.hbar(589.3, 885.7, 634.6, weight=96.0)
    g.vbar(546.6, 439.5, 456.7, weight=48.0)
    g.vbar(570.9, 278.3, 439.5, weight=48.0)
    g.hbar(558.7, 820.3, 457.9, weight=48.0)
    g.diag(820.3, 466.9, 739.1, 332.7, weight=48.0)
    g.hbar(597.3, 779.7, 319.5, weight=48.0)
    g.vbar(444.9, -32.4, 156.4, weight=48.0)
    g.hbar(431.3, 557.5, 158.6, weight=48.0)
    g.diag(557.5, 173.0, 604.3, 144.7, weight=48.0)
    g.diag(604.3, 144.7, 553.7, 27.3, weight=48.0)
    g.dot(536.4, 2.6, w=96.0, h=124.8, slant=-14.0)
    g.vbar(693.3, 168.7, 187.7, weight=48.0)
    g.vbar(716.0, -22.9, 168.7, weight=48.0)
    g.hbar(703.6, 873.6, 192.2, weight=48.0)
    g.diag(873.6, 206.7, 924.7, 171.2, weight=48.0)
    g.diag(924.7, 171.2, 861.6, 40.0, weight=48.0)
    g.dot(830.1, 13.9, w=96.0, h=124.8, slant=-14.0)
    return g
def g_cjk_unified_ideograph_8208() -> Glyph:
    """興 U+8208 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8208", advance=1000, unicode=0x8208, note="興：自动生成")
    g.hbar(282.3, 310.8, 646.8, weight=64.0)
    g.diag(282.3, 647.8, 224.3, 583.9, weight=64.0)
    g.hbar(216.5, 224.3, 583.4, weight=64.0)
    g.diag(148.7, 590.8, 194.1, 554.7, weight=96.0)
    g.vbar(225.0, 281.6, 554.7, weight=96.0)
    g.hbar(255.9, 270.5, 278.4, weight=96.0)
    g.diag(238.1, 489.5, 244.0, 501.4, weight=76.0)
    g.hbar(244.0, 321.6, 504.8, weight=76.0)
    g.vbar(261.2, 393.2, 404.3, weight=84.0)
    g.hbar(263.7, 330.5, 407.1, weight=84.0)
    g.diag(337.4, 700.8, 365.0, 579.6, weight=48.0)
    g.vbar(376.5, 300.2, 579.6, weight=48.0)
    g.diag(388.0, 300.2, 372.7, 292.0, weight=48.0)
    g.hbar(384.5, 470.8, 692.9, weight=48.0)
    g.diag(470.8, 694.7, 575.5, 614.7, weight=48.0)
    g.vbar(583.4, 321.9, 614.7, weight=48.0)
    g.diag(591.3, 321.9, 576.2, 312.7, weight=48.0)
    g.dot(481.3, 604.5, w=96.0, h=124.8, slant=-14.0)
    g.diag(412.0, 516.1, 430.7, 495.4, weight=48.0)
    g.vbar(442.0, 383.4, 495.4, weight=48.0)
    g.diag(449.4, 503.3, 457.0, 515.5, weight=48.0)
    g.hbar(457.0, 541.3, 517.5, weight=48.0)
    g.vbar(531.2, 451.2, 519.5, weight=48.0)
    g.hbar(509.3, 521.1, 449.3, weight=48.0)
    g.dot(505.4, 410.9, w=96.0, h=83.7, slant=-14.0)
    g.diag(668.5, 670.4, 757.9, 576.4, weight=48.0)
    g.vbar(747.6, 338.2, 576.4, weight=48.0)
    g.diag(737.3, 338.2, 715.7, 318.6, weight=48.0)
    g.hbar(654.8, 735.4, 538.2, weight=76.0)
    g.diag(735.4, 542.6, 748.1, 552.4, weight=76.0)
    g.dot(693.1, 446.8, w=64.0, h=82.3, slant=-14.0)
    g.hbar(73.0, 927.0, 258.6, weight=96.0)
    g.diag(342.3, 196.7, 368.0, 157.5, weight=96.0)
    g.diag(368.0, 157.5, 158.5, -22.5, weight=96.0)
    g.diag(598.8, 187.8, 752.1, 0.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_821e() -> Glyph:
    """舞 U+821E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni821E", advance=1000, unicode=0x821E, note="舞：自动生成")
    g.diag(365.1, 732.9, 375.5, 759.3, weight=96.0)
    g.diag(375.5, 759.3, 260.1, 618.5, weight=96.0)
    g.hbar(366.8, 653.3, 713.4, weight=96.0)
    g.diag(653.3, 732.2, 668.2, 714.4, weight=96.0)
    g.diag(244.9, 583.6, 271.8, 521.8, weight=96.0)
    g.hbar(271.8, 730.5, 549.1, weight=96.0)
    g.diag(730.5, 576.4, 784.1, 490.3, weight=96.0)
    g.diag(290.1, 615.5, 330.3, 577.6, weight=76.0)
    g.diag(330.3, 577.6, 352.9, 441.6, weight=76.0)
    g.diag(352.9, 441.6, 364.9, 435.6, weight=76.0)
    g.diag(399.3, 670.4, 445.5, 454.6, weight=64.0)
    g.diag(445.5, 454.6, 430.2, 442.3, weight=64.0)
    g.diag(518.8, 685.5, 551.7, 631.8, weight=64.0)
    g.diag(551.7, 631.8, 524.2, 450.9, weight=64.0)
    g.diag(647.4, 701.3, 679.4, 637.4, weight=76.0)
    g.diag(679.4, 637.4, 618.2, 463.4, weight=76.0)
    g.hbar(99.2, 885.8, 412.1, weight=96.0)
    g.diag(289.0, 383.2, 310.7, 357.0, weight=48.0)
    g.diag(310.7, 357.0, 159.7, 204.4, weight=48.0)
    g.diag(293.9, 308.3, 328.5, 216.7, weight=48.0)
    g.diag(328.5, 216.7, 129.9, -7.5, weight=48.0)
    g.dot(267.9, 209.0, w=96.0, h=92.4, slant=-14.0)
    g.hbar(497.0, 769.7, 303.8, weight=56.0)
    g.vbar(484.7, 140.2, 273.4, weight=96.0)
    g.hbar(474.1, 846.4, 149.8, weight=96.0)
    g.diag(598.7, 397.3, 635.4, 363.0, weight=96.0)
    g.vbar(630.2, -67.0, 363.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_8236() -> Glyph:
    """舶 U+8236 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8236", advance=1000, unicode=0x8236, note="舶：自动生成")
    g.diag(359.3, 792.0, 395.0, 765.5, weight=48.0)
    g.diag(395.0, 765.5, 316.2, 597.8, weight=48.0)
    g.diag(316.2, 597.8, 303.0, 591.8, weight=48.0)
    g.diag(271.6, 584.0, 252.1, 424.1, weight=64.0)
    g.diag(252.1, 424.1, 136.2, -67.0, weight=64.0)
    g.hbar(296.7, 325.9, 575.7, weight=48.0)
    g.hbar(325.9, 423.9, 588.0, weight=48.0)
    g.vbar(440.1, 404.1, 604.0, weight=48.0)
    g.vbar(445.8, -16.4, 404.1, weight=48.0)
    g.hbar(347.8, 435.4, 1.1, weight=48.0)
    g.hbar(300.4, 443.1, 443.4, weight=56.0)
    g.hbar(68.4, 122.6, 274.4, weight=96.0)
    g.hbar(122.6, 435.4, 306.2, weight=96.0)
    g.diag(286.9, 241.4, 447.2, 142.0, weight=64.0)
    g.diag(710.6, 740.9, 758.7, 711.8, weight=48.0)
    g.diag(758.7, 711.8, 656.9, 458.5, weight=48.0)
    g.diag(656.9, 458.5, 642.8, 452.2, weight=48.0)
    g.vbar(594.9, 420.1, 446.4, weight=64.0)
    g.vbar(617.5, 59.6, 420.1, weight=64.0)
    g.hbar(627.1, 657.3, 435.4, weight=48.0)
    g.hbar(657.3, 871.6, 453.1, weight=48.0)
    g.diag(871.6, 476.6, 890.1, 338.7, weight=48.0)
    g.vbar(880.1, 31.6, 338.7, weight=48.0)
    g.vbar(871.1, 7.0, 31.6, weight=48.0)
    g.diag(641.8, 254.1, 656.4, 271.9, weight=96.0)
    g.hbar(656.4, 857.5, 274.2, weight=96.0)
    g.diag(655.3, 82.1, 663.8, 94.2, weight=96.0)
    g.hbar(663.8, 841.6, 97.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_8237() -> Glyph:
    """舷 U+8237 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8237", advance=1000, unicode=0x8237, note="舷：自动生成")
    g.diag(332.9, 777.6, 367.6, 743.1, weight=48.0)
    g.diag(367.6, 743.1, 273.4, 595.0, weight=48.0)
    g.vbar(273.8, 577.1, 595.0, weight=48.0)
    g.diag(231.9, 583.8, 112.5, -52.6, weight=96.0)
    g.hbar(275.2, 379.0, 578.4, weight=48.0)
    g.diag(379.0, 594.1, 405.5, 376.4, weight=48.0)
    g.vbar(402.0, -35.6, 376.4, weight=48.0)
    g.diag(398.6, -35.6, 292.2, 14.2, weight=48.0)
    g.diag(265.4, 467.5, 397.2, 406.9, weight=48.0)
    g.hbar(53.0, 105.3, 258.6, weight=96.0)
    g.hbar(105.3, 381.5, 287.4, weight=96.0)
    g.diag(381.5, 326.7, 388.2, 338.0, weight=96.0)
    g.diag(249.5, 225.6, 340.2, 139.5, weight=48.0)
    g.diag(608.6, 729.6, 699.5, 668.0, weight=96.0)
    g.diag(699.5, 668.0, 731.4, 567.5, weight=96.0)
    g.hbar(454.8, 947.0, 513.4, weight=96.0)
    g.diag(636.5, 491.4, 620.1, 394.9, weight=48.0)
    g.diag(620.1, 394.9, 538.9, 240.0, weight=48.0)
    g.hbar(538.9, 692.2, 242.7, weight=48.0)
    g.diag(774.7, 395.4, 708.5, 259.0, weight=48.0)
    g.diag(708.5, 259.0, 532.4, 14.1, weight=48.0)
    g.hbar(532.4, 807.4, 44.7, weight=48.0)
    g.diag(767.4, 156.2, 884.3, -42.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_8247() -> Glyph:
    """艇 U+8247 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8247", advance=1000, unicode=0x8247, note="艇：自动生成")
    g.diag(293.9, 747.7, 323.6, 718.9, weight=48.0)
    g.diag(323.6, 718.9, 244.6, 574.4, weight=48.0)
    g.hbar(232.0, 244.6, 572.1, weight=48.0)
    g.diag(212.0, 562.8, 168.7, 221.0, weight=48.0)
    g.diag(168.7, 221.0, 90.3, -22.7, weight=48.0)
    g.hbar(231.1, 257.7, 556.0, weight=48.0)
    g.hbar(257.7, 333.1, 564.0, weight=48.0)
    g.vbar(344.7, 378.7, 576.2, weight=48.0)
    g.vbar(354.0, 1.0, 378.7, weight=48.0)
    g.hbar(265.3, 351.6, 18.7, weight=48.0)
    g.diag(238.5, 464.4, 349.4, 405.5, weight=48.0)
    g.hbar(58.0, 104.0, 268.3, weight=96.0)
    g.hbar(104.0, 342.4, 297.3, weight=96.0)
    g.diag(226.2, 252.0, 350.2, 182.9, weight=48.0)
    g.diag(748.8, 517.7, 761.5, 578.8, weight=96.0)
    g.diag(761.5, 578.8, 632.4, 499.3, weight=96.0)
    g.hbar(552.4, 632.4, 497.2, weight=96.0)
    g.hbar(567.0, 819.8, 373.0, weight=96.0)
    g.hbar(760.0, 819.8, 396.3, weight=96.0)
    g.diag(696.1, 509.9, 724.3, 490.4, weight=96.0)
    g.vbar(718.6, 237.8, 490.4, weight=96.0)
    g.diag(713.0, 237.8, 703.8, 230.3, weight=96.0)
    g.hbar(577.9, 852.1, 188.6, weight=56.0)
    g.hbar(387.4, 523.1, 509.5, weight=48.0)
    g.vbar(493.7, 355.8, 521.6, weight=48.0)
    g.hbar(464.3, 547.6, 348.0, weight=48.0)
    g.diag(547.6, 340.2, 389.0, 55.3, weight=48.0)
    g.hbar(394.9, 932.0, 124.7, weight=64.0)
    return g
def g_cjk_unified_ideograph_8266() -> Glyph:
    """艦 U+8266 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8266", advance=1000, unicode=0x8266, note="艦：自动生成")
    g.diag(296.5, 756.5, 319.7, 729.3, weight=48.0)
    g.diag(319.7, 729.3, 223.1, 578.8, weight=48.0)
    g.vbar(222.7, 574.6, 578.8, weight=48.0)
    g.vbar(194.2, 418.4, 575.4, weight=48.0)
    g.diag(185.4, 418.4, 78.5, -31.5, weight=48.0)
    g.diag(236.9, 567.8, 247.7, 561.9, weight=48.0)
    g.hbar(247.7, 325.9, 573.8, weight=48.0)
    g.diag(325.9, 585.7, 350.3, 384.0, weight=48.0)
    g.vbar(347.3, -2.5, 384.0, weight=48.0)
    g.hbar(258.4, 344.2, 14.3, weight=48.0)
    g.diag(229.1, 469.8, 341.6, 412.3, weight=48.0)
    g.hbar(58.0, 100.7, 304.3, weight=96.0)
    g.hbar(100.7, 432.3, 339.8, weight=96.0)
    g.diag(218.2, 262.2, 341.2, 196.2, weight=48.0)
    g.diag(497.9, 634.3, 507.8, 625.6, weight=96.0)
    g.hbar(507.8, 629.5, 638.4, weight=96.0)
    g.diag(629.5, 651.1, 612.5, 619.7, weight=96.0)
    g.diag(567.3, 615.7, 586.0, 560.9, weight=76.0)
    g.diag(586.0, 560.9, 560.5, 541.4, weight=76.0)
    g.hbar(491.1, 653.5, 511.5, weight=48.0)
    g.diag(653.5, 530.4, 624.0, 466.1, weight=48.0)
    g.diag(624.0, 466.1, 607.1, 454.2, weight=48.0)
    g.hbar(491.5, 631.9, 432.0, weight=48.0)
    g.diag(565.5, 407.8, 581.0, 386.9, weight=48.0)
    g.vbar(578.6, 329.3, 386.9, weight=48.0)
    g.diag(576.1, 329.3, 564.2, 312.5, weight=48.0)
    g.vbar(476.9, 558.4, 641.3, weight=48.0)
    g.vbar(467.6, 276.7, 558.4, weight=48.0)
    g.hbar(461.5, 679.8, 289.8, weight=48.0)
    g.hbar(691.3, 799.1, 689.1, weight=96.0)
    g.diag(799.1, 700.3, 674.7, 414.2, weight=96.0)
    g.diag(751.1, 480.8, 757.6, 484.9, weight=96.0)
    g.hbar(757.6, 925.2, 498.5, weight=96.0)
    g.diag(733.4, 407.9, 829.3, 348.8, weight=96.0)
    g.vbar(826.4, 231.2, 348.8, weight=96.0)
    g.diag(494.4, 165.4, 530.5, 30.9, weight=48.0)
    g.hbar(505.0, 848.6, 172.0, weight=48.0)
    g.diag(848.6, 188.2, 780.5, 56.5, weight=48.0)
    g.diag(598.6, 142.5, 593.4, 136.2, weight=64.0)
    g.diag(593.4, 136.2, 610.1, 51.9, weight=64.0)
    g.diag(610.1, 51.9, 618.2, 43.8, weight=64.0)
    g.diag(678.8, 166.0, 705.2, 144.9, weight=64.0)
    g.diag(705.2, 144.9, 674.9, 48.7, weight=64.0)
    g.hbar(433.4, 932.0, 19.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_8377() -> Glyph:
    """荷 U+8377 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8377", advance=1000, unicode=0x8377, note="荷：自动生成")
    g.hbar(219.9, 829.2, 608.1, weight=96.0)
    g.diag(374.1, 636.9, 386.7, 690.1, weight=96.0)
    g.vbar(396.2, 508.5, 690.1, weight=96.0)
    g.diag(630.6, 777.0, 667.1, 739.9, weight=96.0)
    g.diag(667.1, 739.9, 603.4, 466.5, weight=96.0)
    g.diag(355.2, 515.1, 306.3, 410.3, weight=48.0)
    g.diag(306.3, 410.3, 93.3, 195.5, weight=48.0)
    g.vbar(287.9, -29.0, 326.7, weight=48.0)
    g.hbar(388.2, 886.7, 428.8, weight=96.0)
    g.vbar(444.1, 127.2, 281.5, weight=48.0)
    g.hbar(438.9, 606.1, 277.8, weight=48.0)
    g.diag(606.1, 285.8, 554.1, 182.2, weight=48.0)
    g.dot(530.5, 156.0, w=96.0, h=124.8, slant=-14.0)
    g.diag(681.4, 416.2, 703.7, 237.6, weight=96.0)
    g.vbar(700.2, -56.6, 237.6, weight=96.0)
    g.hbar(575.9, 696.6, -31.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_83cc() -> Glyph:
    """菌 U+83CC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni83CC", advance=1000, unicode=0x83CC, note="菌：自动生成")
    g.diag(211.6, 513.5, 381.5, 594.9, weight=96.0)
    g.hbar(381.5, 813.0, 619.1, weight=96.0)
    g.diag(341.3, 732.2, 382.0, 702.4, weight=48.0)
    g.diag(382.0, 702.4, 411.8, 490.3, weight=48.0)
    g.vbar(598.4, 680.4, 685.7, weight=96.0)
    g.diag(598.2, 680.4, 558.8, 528.5, weight=96.0)
    g.diag(251.3, 469.0, 125.2, 171.7, weight=48.0)
    g.diag(125.2, 171.7, 258.0, -16.5, weight=48.0)
    g.hbar(260.7, 700.7, 483.5, weight=48.0)
    g.diag(700.7, 507.2, 733.5, 318.9, weight=48.0)
    g.vbar(739.6, -57.0, 318.9, weight=48.0)
    g.diag(599.0, 464.3, 345.1, 304.1, weight=76.0)
    g.hbar(332.5, 661.6, 288.8, weight=48.0)
    g.diag(468.3, 375.7, 465.5, 377.7, weight=84.0)
    g.vbar(479.3, 62.6, 377.7, weight=84.0)
    g.diag(462.4, 271.2, 351.3, 129.6, weight=48.0)
    g.hbar(266.0, 351.3, 122.5, weight=48.0)
    g.diag(505.1, 235.0, 659.7, 146.2, weight=48.0)
    g.diag(271.0, -2.3, 295.7, 16.6, weight=92.0)
    g.hbar(295.7, 706.7, 21.1, weight=92.0)
    return g
def g_cjk_unified_ideograph_83dc() -> Glyph:
    """菜 U+83DC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni83DC", advance=1000, unicode=0x83DC, note="菜：自动生成")
    g.hbar(176.8, 752.7, 652.2, weight=92.0)
    g.diag(313.1, 682.7, 341.9, 705.0, weight=96.0)
    g.diag(341.9, 705.0, 372.9, 562.1, weight=96.0)
    g.vbar(564.5, 699.9, 712.6, weight=96.0)
    g.diag(563.8, 699.9, 534.8, 596.0, weight=96.0)
    g.hbar(273.6, 539.2, 517.4, weight=84.0)
    g.diag(269.1, 474.1, 338.0, 318.1, weight=96.0)
    g.diag(403.8, 490.9, 448.5, 438.9, weight=96.0)
    g.vbar(450.7, 402.1, 438.9, weight=96.0)
    g.diag(577.3, 544.3, 646.6, 495.3, weight=96.0)
    g.diag(646.6, 495.3, 498.4, 407.8, weight=96.0)
    g.hbar(167.6, 751.8, 282.7, weight=48.0)
    g.vbar(450.6, -47.0, 382.0, weight=96.0)
    g.diag(429.6, 270.2, 144.4, 32.7, weight=48.0)
    g.diag(477.7, 269.4, 855.6, 41.1, weight=48.0)
    return g
def g_cjk_unified_ideograph_840e() -> Glyph:
    """萎 U+840E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni840E", advance=1000, unicode=0x840E, note="萎：自动生成")
    g.hbar(191.1, 787.9, 655.9, weight=84.0)
    g.diag(353.7, 689.8, 371.2, 740.4, weight=96.0)
    g.diag(371.2, 740.4, 412.6, 618.5, weight=96.0)
    g.vbar(604.0, 709.4, 714.6, weight=96.0)
    g.diag(603.7, 709.4, 576.0, 610.4, weight=96.0)
    g.diag(584.5, 588.6, 348.4, 475.7, weight=64.0)
    g.hbar(240.6, 733.7, 462.2, weight=48.0)
    g.diag(467.2, 535.5, 502.9, 512.1, weight=48.0)
    g.diag(502.9, 512.1, 447.7, 294.8, weight=48.0)
    g.diag(464.2, 448.6, 249.2, 292.8, weight=48.0)
    g.diag(516.0, 456.7, 819.3, 312.8, weight=48.0)
    g.diag(389.3, 339.0, 435.5, 280.1, weight=56.0)
    g.vbar(444.0, 119.2, 280.1, weight=56.0)
    g.diag(452.4, 119.2, 671.8, -67.0, weight=56.0)
    g.diag(551.1, 244.7, 508.8, 156.3, weight=48.0)
    g.diag(508.8, 156.3, 269.2, -29.9, weight=48.0)
    g.hbar(124.5, 875.5, 207.6, weight=48.0)
    return g
def g_cjk_unified_ideograph_845b() -> Glyph:
    """葛 U+845B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni845B", advance=1000, unicode=0x845B, note="葛：自动生成")
    g.hbar(157.8, 807.2, 669.4, weight=96.0)
    g.diag(335.7, 763.3, 374.3, 736.6, weight=48.0)
    g.diag(374.3, 736.6, 398.0, 591.3, weight=48.0)
    g.diag(575.9, 787.0, 608.3, 751.2, weight=96.0)
    g.diag(608.3, 751.2, 552.2, 603.2, weight=96.0)
    g.diag(289.3, 545.8, 321.9, 521.1, weight=48.0)
    g.vbar(347.6, 350.1, 521.1, weight=48.0)
    g.hbar(349.6, 434.1, 543.5, weight=48.0)
    g.hbar(434.1, 666.0, 548.4, weight=48.0)
    g.vbar(635.5, 370.5, 553.7, weight=48.0)
    g.diag(605.1, 370.5, 607.5, 354.1, weight=48.0)
    g.hbar(374.3, 543.3, 454.9, weight=64.0)
    g.diag(385.1, 358.0, 398.0, 368.9, weight=48.0)
    g.hbar(398.0, 574.9, 381.3, weight=48.0)
    g.diag(340.7, 363.0, 357.5, 313.7, weight=96.0)
    g.diag(357.5, 313.7, 168.7, 172.2, weight=96.0)
    g.hbar(333.7, 649.2, 206.3, weight=48.0)
    g.vbar(658.2, -73.9, 158.4, weight=48.0)
    g.diag(667.1, -73.9, 571.8, -21.0, weight=48.0)
    g.hbar(565.0, 571.8, -21.3, weight=48.0)
    g.diag(457.3, 241.4, 479.3, 215.7, weight=96.0)
    g.diag(479.3, 215.7, 353.5, 102.0, weight=96.0)
    g.hbar(476.1, 629.3, 138.1, weight=64.0)
    g.diag(266.5, 171.2, 299.1, 134.6, weight=56.0)
    g.diag(299.1, 134.6, 285.6, 25.7, weight=56.0)
    g.hbar(285.6, 603.6, 30.2, weight=56.0)
    return g
def g_cjk_unified_ideograph_84b8() -> Glyph:
    """蒸 U+84B8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni84B8", advance=1000, unicode=0x84B8, note="蒸：自动生成")
    g.hbar(152.4, 323.3, 614.7, weight=92.0)
    g.hbar(323.3, 772.1, 636.1, weight=92.0)
    g.vbar(317.7, 654.9, 752.1, weight=92.0)
    g.diag(320.1, 752.1, 377.7, 540.9, weight=92.0)
    g.diag(545.7, 789.0, 578.0, 754.6, weight=92.0)
    g.diag(578.0, 754.6, 514.7, 567.6, weight=92.0)
    g.diag(341.1, 541.0, 309.2, 494.8, weight=92.0)
    g.hbar(309.2, 557.2, 512.7, weight=92.0)
    g.diag(557.2, 530.5, 467.2, 431.5, weight=92.0)
    g.hbar(458.3, 467.2, 432.0, weight=92.0)
    g.vbar(429.4, 318.7, 431.1, weight=48.0)
    g.vbar(418.9, 278.4, 318.7, weight=48.0)
    g.hbar(321.9, 418.2, 275.3, weight=48.0)
    g.hbar(144.5, 358.9, 354.8, weight=92.0)
    g.diag(358.9, 355.7, 187.0, 154.9, weight=92.0)
    g.diag(187.0, 154.9, 171.8, 101.5, weight=92.0)
    g.diag(683.7, 493.1, 700.6, 453.3, weight=92.0)
    g.diag(700.6, 453.3, 587.4, 368.9, weight=92.0)
    g.diag(587.4, 368.9, 580.4, 373.9, weight=92.0)
    g.diag(489.4, 377.0, 615.6, 309.1, weight=64.0)
    g.diag(615.6, 309.1, 872.4, 185.2, weight=64.0)
    g.diag(312.9, 86.6, 329.1, 127.5, weight=92.0)
    g.hbar(329.1, 605.9, 128.3, weight=92.0)
    g.vbar(177.0, 17.4, 132.4, weight=64.0)
    g.diag(180.2, 17.4, 131.6, -74.0, weight=64.0)
    g.dot(350.8, 27.8, w=92.0, h=119.6, slant=-14.0)
    g.dot(508.4, 40.2, w=92.0, h=119.6, slant=-14.0)
    g.diag(613.6, 109.2, 762.2, -63.1, weight=92.0)
    return g
def g_cjk_unified_ideograph_84cb() -> Glyph:
    """蓋 U+84CB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni84CB", advance=1000, unicode=0x84CB, note="蓋：自动生成")
    g.diag(337.9, 729.9, 377.2, 703.3, weight=64.0)
    g.diag(377.2, 703.3, 403.7, 560.6, weight=64.0)
    g.hbar(191.8, 475.3, 642.8, weight=96.0)
    g.diag(584.7, 787.0, 621.1, 750.2, weight=96.0)
    g.diag(621.1, 750.2, 565.3, 579.0, weight=96.0)
    g.hbar(558.5, 817.8, 654.0, weight=96.0)
    g.hbar(369.9, 620.5, 509.8, weight=64.0)
    g.diag(454.0, 598.3, 486.0, 567.4, weight=48.0)
    g.vbar(484.5, 455.1, 567.4, weight=48.0)
    g.diag(483.1, 455.1, 469.5, 433.9, weight=48.0)
    g.hbar(248.9, 743.3, 404.8, weight=48.0)
    g.hbar(450.4, 486.0, 371.7, weight=48.0)
    g.diag(450.4, 366.6, 364.1, 258.7, weight=48.0)
    g.hbar(364.1, 577.0, 282.2, weight=48.0)
    g.diag(577.0, 305.6, 588.5, 298.4, weight=48.0)
    g.diag(566.3, 357.4, 647.5, 268.4, weight=48.0)
    g.diag(218.0, 173.6, 254.2, 150.6, weight=84.0)
    g.diag(254.2, 150.6, 323.4, -3.5, weight=84.0)
    g.hbar(291.5, 391.2, 157.6, weight=48.0)
    g.hbar(391.2, 671.2, 188.7, weight=48.0)
    g.diag(671.2, 207.6, 703.9, 164.2, weight=48.0)
    g.diag(703.9, 164.2, 660.5, 51.1, weight=48.0)
    g.diag(660.5, 51.1, 624.3, 31.4, weight=48.0)
    g.diag(384.4, 154.2, 393.7, 145.8, weight=96.0)
    g.diag(393.7, 145.8, 429.9, 10.1, weight=96.0)
    g.diag(518.9, 174.6, 546.0, 144.6, weight=92.0)
    g.diag(546.0, 144.6, 514.0, 27.5, weight=92.0)
    g.diag(514.0, 27.5, 501.5, 21.7, weight=92.0)
    g.hbar(99.0, 901.0, -21.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_853d() -> Glyph:
    """蔽 U+853D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni853D", advance=1000, unicode=0x853D, note="蔽：自动生成")
    g.hbar(152.2, 806.3, 621.5, weight=96.0)
    g.diag(311.1, 652.5, 341.3, 697.2, weight=96.0)
    g.diag(341.3, 697.2, 399.2, 527.0, weight=96.0)
    g.diag(569.2, 782.0, 605.9, 742.6, weight=92.0)
    g.diag(605.9, 742.6, 572.5, 541.9, weight=92.0)
    g.diag(137.9, 425.3, 202.3, 379.3, weight=56.0)
    g.diag(202.3, 379.3, 224.3, 303.6, weight=56.0)
    g.diag(398.2, 527.8, 446.6, 475.4, weight=48.0)
    g.diag(446.6, 475.4, 317.8, 381.8, weight=48.0)
    g.vbar(138.0, 190.1, 282.0, weight=48.0)
    g.vbar(126.4, -52.0, 190.1, weight=48.0)
    g.hbar(149.1, 408.3, 294.1, weight=48.0)
    g.diag(408.3, 316.1, 434.8, 181.4, weight=48.0)
    g.vbar(427.4, -46.3, 181.4, weight=48.0)
    g.hbar(304.5, 420.0, -25.5, weight=48.0)
    g.diag(254.4, 504.0, 292.3, 343.9, weight=48.0)
    g.vbar(307.8, -19.0, 343.9, weight=48.0)
    g.diag(212.5, 201.5, 234.8, 184.5, weight=48.0)
    g.diag(234.8, 184.5, 216.7, 118.7, weight=48.0)
    g.diag(216.7, 118.7, 150.9, 76.1, weight=48.0)
    g.diag(316.0, 206.9, 431.3, 135.2, weight=48.0)
    g.diag(564.9, 563.9, 647.8, 509.2, weight=48.0)
    g.diag(647.8, 509.2, 521.7, 243.9, weight=48.0)
    g.diag(521.7, 243.9, 525.7, 224.9, weight=48.0)
    g.hbar(596.8, 846.2, 349.2, weight=96.0)
    g.diag(682.7, 306.7, 746.1, 264.5, weight=96.0)
    g.diag(746.1, 264.5, 490.9, -0.2, weight=96.0)
    g.diag(541.4, 225.1, 784.1, -18.4, weight=84.0)
    g.hbar(784.1, 923.9, -30.6, weight=84.0)
    return g
def g_cjk_unified_ideograph_8584() -> Glyph:
    """薄 U+8584 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8584", advance=1000, unicode=0x8584, note="薄：自动生成")
    g.hbar(161.2, 714.3, 685.9, weight=64.0)
    g.diag(714.3, 708.7, 736.7, 640.6, weight=64.0)
    g.diag(316.7, 705.4, 351.5, 728.6, weight=96.0)
    g.diag(351.5, 728.6, 392.9, 557.7, weight=96.0)
    g.diag(566.0, 787.0, 592.8, 752.7, weight=48.0)
    g.diag(592.8, 752.7, 541.0, 606.4, weight=48.0)
    g.diag(198.2, 622.5, 312.7, 469.2, weight=84.0)
    g.dot(185.7, 363.3, w=96.0, h=124.8, slant=-14.0)
    g.diag(152.1, -42.9, 236.0, 318.1, weight=96.0)
    g.diag(391.4, 564.7, 467.8, 511.5, weight=56.0)
    g.hbar(467.8, 720.6, 551.9, weight=56.0)
    g.diag(354.2, 439.4, 393.7, 191.3, weight=96.0)
    g.hbar(381.2, 735.1, 441.8, weight=56.0)
    g.diag(735.1, 460.5, 656.1, 248.4, weight=56.0)
    g.diag(448.0, 411.0, 497.5, 363.0, weight=56.0)
    g.hbar(497.5, 578.1, 373.1, weight=56.0)
    g.diag(578.1, 383.1, 619.7, 325.9, weight=56.0)
    g.hbar(403.9, 581.2, 292.8, weight=56.0)
    g.diag(581.2, 306.2, 615.5, 283.6, weight=56.0)
    g.vbar(529.5, 190.0, 612.5, weight=48.0)
    g.diag(683.0, 685.5, 725.1, 617.8, weight=56.0)
    g.vbar(716.3, 564.3, 617.8, weight=56.0)
    g.hbar(254.3, 858.1, 171.7, weight=96.0)
    g.diag(615.0, 278.1, 664.5, 203.7, weight=64.0)
    g.vbar(648.9, -69.0, 203.7, weight=64.0)
    g.diag(633.4, -69.0, 514.7, 13.1, weight=64.0)
    g.diag(431.3, 119.3, 495.5, 67.9, weight=96.0)
    g.diag(495.5, 67.9, 512.1, 22.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_85a6() -> Glyph:
    """薦 U+85A6 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni85A6", advance=1000, unicode=0x85A6, note="薦：自动生成")
    g.diag(380.3, 773.4, 417.7, 748.8, weight=84.0)
    g.diag(417.7, 748.8, 448.1, 606.3, weight=84.0)
    g.hbar(200.4, 517.9, 690.8, weight=84.0)
    g.diag(631.0, 798.0, 656.6, 765.2, weight=84.0)
    g.diag(656.6, 765.2, 611.3, 615.1, weight=84.0)
    g.hbar(600.5, 885.6, 717.4, weight=84.0)
    g.diag(499.3, 641.7, 541.5, 610.2, weight=48.0)
    g.diag(541.5, 610.2, 551.4, 585.6, weight=48.0)
    g.diag(356.7, 543.4, 381.8, 528.1, weight=84.0)
    g.hbar(381.8, 753.9, 552.4, weight=84.0)
    g.diag(301.6, 558.1, 272.4, 365.8, weight=76.0)
    g.diag(272.4, 365.8, 84.4, -35.7, weight=76.0)
    g.hbar(369.5, 761.9, 432.3, weight=84.0)
    g.diag(761.9, 451.0, 702.8, 329.0, weight=84.0)
    g.hbar(679.2, 702.8, 329.0, weight=84.0)
    g.diag(432.4, 495.2, 460.9, 462.7, weight=64.0)
    g.vbar(464.4, 347.7, 462.7, weight=64.0)
    g.diag(467.8, 347.7, 458.9, 338.9, weight=64.0)
    g.diag(568.1, 527.6, 596.6, 503.3, weight=76.0)
    g.diag(596.6, 503.3, 562.2, 354.6, weight=76.0)
    g.hbar(347.8, 669.3, 327.6, weight=48.0)
    g.hbar(443.2, 658.5, 237.6, weight=64.0)
    g.diag(396.0, 291.7, 422.6, 264.2, weight=64.0)
    g.diag(422.6, 264.2, 529.8, 167.8, weight=64.0)
    g.hbar(529.8, 879.1, 172.7, weight=64.0)
    g.diag(879.1, 177.6, 778.1, -85.0, weight=64.0)
    g.diag(778.1, -85.0, 686.1, -22.9, weight=64.0)
    g.diag(283.0, 85.2, 254.4, -49.5, weight=64.0)
    g.dot(391.1, 26.7, w=56.0, h=72.8, slant=-14.0)
    g.diag(473.7, 75.4, 529.7, 14.4, weight=48.0)
    g.diag(605.4, 102.9, 697.9, 15.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_85aa() -> Glyph:
    """薪 U+85AA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni85AA", advance=1000, unicode=0x85AA, note="薪：自动生成")
    g.hbar(185.6, 773.3, 661.5, weight=56.0)
    g.diag(338.1, 736.8, 373.5, 709.8, weight=56.0)
    g.diag(373.5, 709.8, 393.9, 589.9, weight=56.0)
    g.diag(562.2, 787.0, 595.0, 753.4, weight=96.0)
    g.diag(595.0, 753.4, 534.3, 575.0, weight=96.0)
    g.diag(282.3, 589.9, 358.6, 546.2, weight=48.0)
    g.hbar(190.3, 438.6, 512.7, weight=48.0)
    g.dot(235.8, 410.4, w=96.0, h=69.2, slant=-14.0)
    g.diag(372.5, 496.9, 393.3, 476.1, weight=48.0)
    g.diag(393.3, 476.1, 358.2, 386.8, weight=48.0)
    g.diag(358.2, 386.8, 346.5, 375.1, weight=48.0)
    g.hbar(123.3, 451.6, 343.4, weight=76.0)
    g.hbar(154.0, 444.1, 246.3, weight=76.0)
    g.diag(300.0, 324.8, 317.8, 221.9, weight=48.0)
    g.vbar(313.6, 42.3, 221.9, weight=48.0)
    g.diag(309.4, 42.3, 225.6, 90.5, weight=48.0)
    g.dot(177.7, 118.4, w=96.0, h=124.8, slant=14.0)
    g.dot(396.3, 180.2, w=96.0, h=81.5, slant=-14.0)
    g.hbar(704.1, 760.3, 551.0, weight=96.0)
    g.diag(704.1, 554.0, 569.7, 474.3, weight=96.0)
    g.vbar(569.7, 469.9, 474.3, weight=96.0)
    g.diag(497.1, 488.5, 558.8, 423.6, weight=96.0)
    g.diag(558.8, 423.6, 416.2, 5.9, weight=96.0)
    g.hbar(559.5, 861.7, 368.1, weight=96.0)
    g.diag(658.0, 346.2, 694.8, 326.4, weight=96.0)
    g.vbar(692.7, -62.0, 326.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_85cd() -> Glyph:
    """藍 U+85CD —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni85CD", advance=1000, unicode=0x85CD, note="藍：自动生成")
    g.diag(346.1, 753.9, 388.2, 726.6, weight=96.0)
    g.diag(388.2, 726.6, 423.3, 580.0, weight=96.0)
    g.hbar(173.2, 488.8, 654.3, weight=96.0)
    g.diag(599.2, 792.0, 632.7, 751.3, weight=84.0)
    g.diag(632.7, 751.3, 547.4, 570.3, weight=84.0)
    g.hbar(559.1, 826.8, 676.7, weight=96.0)
    g.diag(274.8, 511.6, 292.9, 500.8, weight=76.0)
    g.hbar(292.9, 457.5, 510.1, weight=76.0)
    g.diag(370.6, 487.2, 385.9, 471.9, weight=96.0)
    g.diag(385.9, 471.9, 360.8, 433.5, weight=96.0)
    g.hbar(279.7, 476.6, 406.8, weight=48.0)
    g.diag(476.6, 423.0, 424.3, 358.3, weight=48.0)
    g.hbar(283.6, 462.4, 317.2, weight=48.0)
    g.diag(371.5, 304.6, 388.2, 287.9, weight=96.0)
    g.diag(388.2, 287.9, 365.7, 260.6, weight=96.0)
    g.diag(228.9, 522.4, 298.5, 217.7, weight=48.0)
    g.hbar(298.5, 491.7, 230.9, weight=48.0)
    g.diag(613.8, 580.0, 649.3, 536.7, weight=48.0)
    g.diag(649.3, 536.7, 503.4, 310.4, weight=48.0)
    g.hbar(620.6, 807.2, 435.4, weight=96.0)
    g.dot(658.2, 310.9, w=96.0, h=124.8, slant=-14.0)
    g.diag(267.0, 146.3, 296.3, 119.9, weight=48.0)
    g.diag(296.3, 119.9, 328.6, 3.7, weight=48.0)
    g.diag(328.6, 3.7, 343.2, -8.0, weight=48.0)
    g.hbar(315.9, 415.6, 144.3, weight=48.0)
    g.hbar(415.6, 671.6, 162.1, weight=48.0)
    g.diag(671.6, 177.9, 706.3, 137.3, weight=48.0)
    g.diag(706.3, 137.3, 669.5, 41.8, weight=48.0)
    g.diag(669.5, 41.8, 636.3, 20.3, weight=48.0)
    g.diag(408.7, 126.8, 417.9, 118.4, weight=96.0)
    g.diag(417.9, 118.4, 452.6, -2.2, weight=96.0)
    g.diag(533.7, 142.4, 561.1, 121.4, weight=84.0)
    g.diag(561.1, 121.4, 531.6, 13.8, weight=84.0)
    g.diag(531.6, 13.8, 520.0, 8.6, weight=84.0)
    g.hbar(110.7, 889.3, -32.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_85e4() -> Glyph:
    """藤 U+85E4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni85E4", advance=1000, unicode=0x85E4, note="藤：自动生成")
    g.diag(166.8, 549.7, 213.6, 626.2, weight=96.0)
    g.hbar(213.6, 703.8, 652.0, weight=96.0)
    g.vbar(705.1, 614.3, 677.7, weight=96.0)
    g.diag(338.7, 676.1, 364.0, 710.2, weight=92.0)
    g.diag(364.0, 710.2, 412.6, 551.5, weight=92.0)
    g.diag(587.5, 704.9, 614.4, 770.5, weight=96.0)
    g.diag(614.4, 770.5, 544.7, 582.0, weight=96.0)
    g.diag(196.5, 504.1, 169.1, 354.2, weight=56.0)
    g.diag(169.1, 354.2, 63.0, -25.9, weight=56.0)
    g.diag(204.2, 493.8, 296.1, 322.4, weight=48.0)
    g.vbar(302.2, 3.6, 322.4, weight=48.0)
    g.diag(308.2, 3.6, 218.4, 44.9, weight=48.0)
    g.diag(213.5, 330.5, 225.5, 346.7, weight=84.0)
    g.hbar(225.5, 293.1, 346.9, weight=84.0)
    g.dot(241.4, 220.8, w=96.0, h=98.1, slant=-14.0)
    g.diag(417.6, 546.2, 474.8, 488.7, weight=96.0)
    g.diag(474.8, 488.7, 482.5, 448.5, weight=96.0)
    g.diag(679.7, 586.8, 693.3, 564.5, weight=56.0)
    g.diag(693.3, 564.5, 648.7, 469.9, weight=56.0)
    g.diag(466.0, 452.7, 439.9, 404.9, weight=64.0)
    g.hbar(439.9, 661.2, 426.6, weight=64.0)
    g.vbar(661.6, 448.3, 492.6, weight=64.0)
    g.hbar(346.2, 813.7, 334.2, weight=48.0)
    g.diag(541.8, 568.4, 516.4, 433.4, weight=48.0)
    g.diag(516.4, 433.4, 346.6, 175.2, weight=48.0)
    g.diag(620.8, 329.3, 937.0, 173.1, weight=48.0)
    g.diag(504.0, 272.8, 554.9, 143.8, weight=48.0)
    g.vbar(556.5, -53.5, 143.8, weight=48.0)
    g.diag(558.1, -53.5, 454.0, 11.6, weight=48.0)
    g.diag(437.8, 177.1, 491.3, 139.1, weight=96.0)
    g.diag(491.3, 139.1, 500.6, 117.9, weight=96.0)
    g.hbar(334.2, 413.6, 10.1, weight=48.0)
    g.diag(413.6, 4.2, 504.1, 105.1, weight=48.0)
    g.diag(694.3, 237.0, 631.0, 104.8, weight=48.0)
    g.diag(632.3, 92.2, 771.9, -28.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_8650() -> Glyph:
    """虐 U+8650 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8650", advance=1000, unicode=0x8650, note="虐：自动生成")
    g.diag(531.3, 723.9, 524.0, 758.0, weight=96.0)
    g.vbar(521.5, 622.2, 758.0, weight=96.0)
    g.diag(519.0, 622.2, 503.0, 599.2, weight=96.0)
    g.hbar(552.9, 680.0, 706.9, weight=92.0)
    g.diag(680.0, 721.6, 719.0, 645.8, weight=92.0)
    g.hbar(319.1, 796.1, 569.6, weight=64.0)
    g.diag(796.1, 602.3, 708.5, 462.9, weight=64.0)
    g.diag(299.2, 560.9, 254.8, 394.7, weight=96.0)
    g.diag(254.8, 394.7, 82.5, -62.0, weight=96.0)
    g.hbar(356.2, 691.6, 422.9, weight=48.0)
    g.diag(464.3, 554.4, 579.6, 349.6, weight=48.0)
    g.hbar(579.6, 716.7, 326.8, weight=48.0)
    g.vbar(712.1, 304.1, 476.2, weight=48.0)
    g.hbar(439.9, 709.7, 209.4, weight=48.0)
    g.hbar(275.2, 887.5, 99.3, weight=48.0)
    g.diag(385.1, 240.6, 423.6, 201.1, weight=48.0)
    g.diag(423.6, 201.1, 509.9, 28.6, weight=48.0)
    g.hbar(509.9, 785.6, 3.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_865a() -> Glyph:
    """虚 U+865A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni865A", advance=1000, unicode=0x865A, note="虚：自动生成")
    g.diag(543.7, 730.8, 507.9, 793.3, weight=96.0)
    g.diag(507.9, 793.3, 546.0, 649.4, weight=96.0)
    g.diag(546.0, 649.4, 513.6, 625.2, weight=96.0)
    g.hbar(561.9, 664.3, 714.8, weight=76.0)
    g.diag(664.3, 732.3, 719.8, 660.4, weight=76.0)
    g.hbar(315.2, 784.8, 596.0, weight=56.0)
    g.diag(784.8, 620.7, 715.2, 495.0, weight=56.0)
    g.diag(293.9, 587.6, 103.0, -57.0, weight=96.0)
    g.hbar(382.3, 692.9, 476.5, weight=48.0)
    g.diag(488.5, 573.3, 594.4, 402.5, weight=48.0)
    g.hbar(594.4, 721.5, 386.2, weight=48.0)
    g.vbar(718.3, 369.9, 494.9, weight=48.0)
    g.diag(431.7, 286.5, 490.5, 49.9, weight=64.0)
    g.diag(490.5, 49.9, 461.9, 20.1, weight=64.0)
    g.diag(578.4, 333.2, 614.4, 273.6, weight=76.0)
    g.vbar(606.3, 46.2, 273.6, weight=76.0)
    g.diag(598.2, 46.2, 582.7, 32.8, weight=76.0)
    g.diag(271.5, 196.5, 445.9, 102.2, weight=64.0)
    g.diag(749.6, 266.8, 768.3, 234.2, weight=48.0)
    g.diag(768.3, 234.2, 691.3, 152.3, weight=48.0)
    g.hbar(624.0, 691.3, 142.2, weight=48.0)
    g.hbar(216.0, 466.9, 19.6, weight=96.0)
    g.hbar(466.9, 867.1, 1.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_865c() -> Glyph:
    """虜 U+865C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni865C", advance=1000, unicode=0x865C, note="虜：自动生成")
    g.diag(506.1, 756.0, 500.9, 769.2, weight=96.0)
    g.vbar(499.0, 673.6, 769.2, weight=96.0)
    g.diag(497.1, 673.6, 482.6, 662.9, weight=96.0)
    g.hbar(524.8, 650.6, 740.3, weight=64.0)
    g.diag(650.6, 753.7, 682.3, 698.1, weight=64.0)
    g.hbar(294.3, 762.3, 637.8, weight=48.0)
    g.diag(762.3, 667.4, 689.1, 558.8, weight=48.0)
    g.diag(281.2, 627.0, 241.9, 444.4, weight=96.0)
    g.diag(241.9, 444.4, 72.1, -51.7, weight=96.0)
    g.hbar(297.1, 657.8, 544.9, weight=48.0)
    g.diag(466.2, 619.5, 481.6, 573.3, weight=48.0)
    g.diag(481.6, 573.3, 524.0, 470.7, weight=48.0)
    g.hbar(524.0, 708.4, 473.2, weight=48.0)
    g.vbar(703.0, 475.6, 559.0, weight=48.0)
    g.vbar(385.6, 367.7, 379.2, weight=56.0)
    g.vbar(405.8, 189.7, 367.7, weight=56.0)
    g.hbar(400.6, 714.0, 387.3, weight=48.0)
    g.vbar(685.2, 229.3, 403.0, weight=48.0)
    g.hbar(639.3, 656.4, 226.5, weight=48.0)
    g.hbar(261.1, 897.9, 297.5, weight=48.0)
    g.diag(510.6, 375.1, 535.7, 351.0, weight=84.0)
    g.vbar(535.7, 256.4, 351.0, weight=84.0)
    g.diag(535.7, 256.4, 522.2, 236.1, weight=84.0)
    g.hbar(443.0, 637.8, 214.7, weight=48.0)
    g.hbar(304.9, 743.4, 121.4, weight=76.0)
    g.diag(743.4, 142.8, 644.7, -60.7, weight=76.0)
    g.diag(644.7, -60.7, 566.6, -17.9, weight=76.0)
    g.diag(499.0, 193.6, 454.2, 93.0, weight=48.0)
    g.diag(454.2, 93.0, 256.6, -72.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_868a() -> Glyph:
    """蚊 U+868A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni868A", advance=1000, unicode=0x868A, note="蚊：自动生成")
    g.vbar(136.2, 289.6, 473.4, weight=76.0)
    g.hbar(129.3, 404.2, 485.6, weight=48.0)
    g.vbar(380.4, 373.8, 504.4, weight=48.0)
    g.hbar(176.4, 379.3, 335.6, weight=48.0)
    g.vbar(380.2, 360.0, 376.8, weight=48.0)
    g.diag(216.1, 721.2, 264.5, 682.1, weight=84.0)
    g.vbar(259.1, 214.5, 682.1, weight=84.0)
    g.diag(253.8, 214.5, 237.7, 193.4, weight=84.0)
    g.hbar(68.0, 122.0, 123.3, weight=96.0)
    g.hbar(122.0, 347.6, 163.5, weight=96.0)
    g.hbar(347.6, 356.4, 209.1, weight=96.0)
    g.diag(345.0, 236.6, 390.7, 213.1, weight=64.0)
    g.diag(390.7, 213.1, 376.3, 191.0, weight=64.0)
    g.diag(565.3, 730.0, 659.5, 677.0, weight=96.0)
    g.diag(659.5, 677.0, 712.1, 551.6, weight=96.0)
    g.hbar(433.7, 834.1, 504.9, weight=96.0)
    g.diag(631.0, 459.3, 730.5, 383.8, weight=96.0)
    g.diag(730.5, 383.8, 339.7, 29.6, weight=96.0)
    g.diag(427.9, 361.4, 595.9, 238.9, weight=76.0)
    g.diag(595.9, 238.9, 942.0, 10.0, weight=76.0)
    return g
def g_cjk_unified_ideograph_8695() -> Glyph:
    """蚕 U+8695 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8695", advance=1000, unicode=0x8695, note="蚕：自动生成")
    g.hbar(347.8, 381.8, 663.0, weight=96.0)
    g.hbar(347.8, 639.9, 690.3, weight=96.0)
    g.hbar(167.0, 771.0, 511.8, weight=48.0)
    g.diag(418.7, 646.3, 351.3, 506.0, weight=96.0)
    g.diag(351.3, 506.0, 78.0, 211.7, weight=96.0)
    g.diag(528.8, 511.0, 927.0, 304.6, weight=48.0)
    g.diag(273.9, 292.9, 348.9, 125.6, weight=96.0)
    g.hbar(316.7, 594.1, 303.8, weight=48.0)
    g.diag(594.1, 323.3, 640.9, 291.4, weight=48.0)
    g.diag(640.9, 291.4, 588.2, 207.0, weight=48.0)
    g.hbar(364.0, 448.9, 152.9, weight=48.0)
    g.hbar(448.9, 620.8, 177.0, weight=48.0)
    g.vbar(620.9, 190.7, 213.2, weight=48.0)
    g.diag(384.7, 445.8, 469.5, 383.1, weight=56.0)
    g.vbar(466.1, 79.7, 383.1, weight=56.0)
    g.diag(462.8, 79.7, 448.0, 56.1, weight=56.0)
    g.diag(238.8, 21.3, 288.0, -1.6, weight=96.0)
    g.hbar(288.0, 615.9, 28.5, weight=96.0)
    g.diag(588.2, 149.4, 678.1, 25.1, weight=96.0)
    g.hbar(640.8, 678.1, 27.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_86c7() -> Glyph:
    """蛇 U+86C7 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni86C7", advance=1000, unicode=0x86C7, note="蛇：自动生成")
    g.vbar(123.1, 459.3, 477.3, weight=48.0)
    g.vbar(146.4, 287.3, 459.3, weight=48.0)
    g.hbar(133.7, 426.5, 491.0, weight=48.0)
    g.diag(426.5, 514.0, 361.5, 371.1, weight=48.0)
    g.hbar(184.1, 393.8, 339.0, weight=48.0)
    g.diag(224.9, 727.3, 278.9, 684.2, weight=92.0)
    g.vbar(265.0, 162.7, 684.2, weight=92.0)
    g.hbar(73.0, 129.6, 88.8, weight=96.0)
    g.hbar(129.6, 385.2, 134.9, weight=96.0)
    g.hbar(385.2, 393.6, 187.3, weight=96.0)
    g.diag(382.9, 227.2, 436.5, 181.6, weight=96.0)
    g.diag(436.5, 181.6, 421.6, 159.5, weight=96.0)
    g.diag(627.2, 768.2, 700.5, 709.5, weight=96.0)
    g.diag(700.5, 709.5, 743.0, 600.0, weight=96.0)
    g.diag(530.2, 530.7, 525.1, 536.0, weight=96.0)
    g.diag(525.1, 536.0, 492.8, 416.5, weight=96.0)
    g.diag(492.8, 416.5, 525.0, 384.2, weight=96.0)
    g.hbar(551.7, 904.7, 539.4, weight=96.0)
    g.diag(904.7, 579.9, 803.2, 428.5, weight=96.0)
    g.vbar(796.8, 345.0, 426.0, weight=96.0)
    g.diag(792.6, 345.0, 615.0, 218.1, weight=96.0)
    g.diag(615.0, 218.1, 609.4, 206.7, weight=96.0)
    g.diag(528.9, 392.0, 633.3, 211.8, weight=96.0)
    g.diag(633.3, 211.8, 926.1, -32.4, weight=96.0)
    g.vbar(929.1, -32.4, 170.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_86ee() -> Glyph:
    """蛮 U+86EE —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni86EE", advance=1000, unicode=0x86EE, note="蛮：自动生成")
    g.diag(431.1, 787.0, 516.3, 741.4, weight=48.0)
    g.diag(516.3, 741.4, 542.4, 667.2, weight=48.0)
    g.hbar(127.0, 873.0, 629.0, weight=96.0)
    g.diag(380.6, 605.7, 409.2, 581.5, weight=96.0)
    g.vbar(399.0, 408.7, 581.5, weight=96.0)
    g.diag(388.8, 408.7, 413.3, 371.2, weight=96.0)
    g.diag(548.1, 623.5, 566.1, 610.3, weight=76.0)
    g.vbar(575.7, 337.9, 610.3, weight=76.0)
    g.diag(293.3, 583.9, 191.4, 397.6, weight=84.0)
    g.diag(606.8, 552.3, 775.9, 465.0, weight=76.0)
    g.diag(775.9, 465.0, 801.7, 413.5, weight=76.0)
    g.vbar(328.7, 101.5, 277.6, weight=96.0)
    g.hbar(325.6, 698.1, 285.0, weight=48.0)
    g.diag(698.1, 304.7, 623.4, 187.0, weight=48.0)
    g.hbar(358.3, 658.1, 154.8, weight=48.0)
    g.vbar(658.5, 170.0, 195.2, weight=48.0)
    g.diag(406.7, 378.8, 465.3, 280.3, weight=48.0)
    g.vbar(469.9, 27.3, 280.3, weight=48.0)
    g.diag(208.2, -7.6, 265.4, -35.2, weight=96.0)
    g.hbar(265.4, 664.0, 2.4, weight=96.0)
    g.diag(635.2, 129.4, 759.1, -72.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_8702() -> Glyph:
    """蜂 U+8702 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8702", advance=1000, unicode=0x8702, note="蜂：自动生成")
    g.vbar(126.3, 359.7, 520.9, weight=76.0)
    g.hbar(127.2, 369.6, 527.8, weight=48.0)
    g.vbar(355.3, 460.6, 543.3, weight=48.0)
    g.diag(340.9, 460.6, 319.7, 443.1, weight=48.0)
    g.hbar(158.4, 318.1, 400.2, weight=48.0)
    g.hbar(318.1, 375.7, 414.4, weight=48.0)
    g.diag(201.5, 722.8, 250.8, 681.6, weight=76.0)
    g.vbar(234.9, 268.1, 681.6, weight=76.0)
    g.hbar(75.9, 125.8, 208.1, weight=96.0)
    g.hbar(125.8, 323.5, 240.2, weight=96.0)
    g.diag(317.4, 304.4, 360.1, 270.8, weight=64.0)
    g.diag(360.1, 270.8, 342.6, 262.1, weight=64.0)
    g.diag(527.0, 787.0, 558.8, 744.6, weight=48.0)
    g.diag(558.8, 744.6, 378.5, 535.0, weight=48.0)
    g.diag(540.7, 685.7, 594.3, 620.0, weight=48.0)
    g.diag(594.3, 620.0, 364.5, 402.0, weight=48.0)
    g.hbar(490.3, 934.1, 527.1, weight=64.0)
    g.diag(429.8, 388.8, 467.1, 355.3, weight=56.0)
    g.hbar(467.1, 723.5, 399.6, weight=56.0)
    g.hbar(385.6, 642.1, 287.6, weight=64.0)
    g.diag(642.1, 302.1, 696.0, 373.0, weight=64.0)
    g.hbar(354.6, 500.7, 202.1, weight=76.0)
    g.hbar(500.7, 827.7, 191.9, weight=76.0)
    g.diag(526.0, 469.2, 565.8, 348.8, weight=48.0)
    g.vbar(567.9, -62.0, 348.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_871c() -> Glyph:
    """蜜 U+871C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni871C", advance=1000, unicode=0x871C, note="蜜：自动生成")
    g.diag(433.7, 792.0, 515.4, 754.1, weight=48.0)
    g.diag(515.4, 754.1, 545.9, 681.0, weight=48.0)
    g.hbar(236.4, 248.7, 632.5, weight=56.0)
    g.diag(236.4, 632.5, 179.7, 521.7, weight=56.0)
    g.diag(179.7, 521.7, 218.5, 463.9, weight=56.0)
    g.hbar(262.3, 789.5, 640.0, weight=92.0)
    g.diag(789.5, 665.3, 687.2, 552.7, weight=92.0)
    g.diag(197.8, 487.0, 229.1, 412.2, weight=56.0)
    g.diag(229.1, 412.2, 202.5, 346.5, weight=56.0)
    g.hbar(280.6, 685.1, 410.6, weight=92.0)
    g.diag(685.1, 329.5, 623.5, 463.8, weight=92.0)
    g.diag(623.5, 463.8, 591.0, 491.6, weight=92.0)
    g.diag(395.2, 617.1, 464.6, 509.0, weight=48.0)
    g.diag(565.1, 625.8, 592.0, 518.9, weight=96.0)
    g.diag(592.0, 518.9, 234.5, 231.3, weight=96.0)
    g.diag(234.5, 231.3, 236.4, 228.6, weight=96.0)
    g.diag(689.2, 549.4, 826.4, 445.2, weight=56.0)
    g.vbar(312.0, 63.8, 218.2, weight=96.0)
    g.hbar(313.0, 639.8, 229.0, weight=48.0)
    g.diag(639.8, 246.6, 682.8, 214.2, weight=48.0)
    g.diag(682.8, 214.2, 626.4, 137.9, weight=48.0)
    g.hbar(349.9, 659.8, 110.3, weight=48.0)
    g.vbar(660.7, 80.2, 119.8, weight=48.0)
    g.diag(437.1, 318.2, 487.5, 270.8, weight=96.0)
    g.vbar(485.1, 28.7, 270.8, weight=96.0)
    g.diag(482.6, 28.7, 467.6, 7.7, weight=96.0)
    g.diag(227.4, -26.2, 280.8, -53.8, weight=92.0)
    g.hbar(280.8, 672.9, -23.1, weight=92.0)
    g.diag(657.1, 77.5, 763.3, -42.0, weight=96.0)
    g.hbar(702.0, 763.3, -29.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_878d() -> Glyph:
    """融 U+878D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni878D", advance=1000, unicode=0x878D, note="融：自动生成")
    g.diag(165.0, 602.2, 191.2, 668.1, weight=92.0)
    g.hbar(191.2, 480.4, 695.4, weight=92.0)
    g.vbar(209.9, 412.6, 565.5, weight=48.0)
    g.hbar(202.3, 425.1, 569.1, weight=48.0)
    g.diag(425.1, 584.2, 372.9, 476.6, weight=48.0)
    g.diag(238.9, 425.1, 247.6, 433.4, weight=48.0)
    g.hbar(247.6, 401.3, 457.5, weight=48.0)
    g.vbar(106.1, -26.3, 320.4, weight=96.0)
    g.hbar(130.2, 391.4, 273.4, weight=48.0)
    g.vbar(423.0, 1.5, 246.7, weight=48.0)
    g.hbar(369.1, 454.6, 13.8, weight=48.0)
    g.diag(196.2, 311.6, 256.4, 182.9, weight=48.0)
    g.diag(337.6, 322.9, 357.3, 291.5, weight=96.0)
    g.diag(357.3, 291.5, 319.1, 216.1, weight=96.0)
    g.hbar(157.1, 431.8, 168.1, weight=96.0)
    g.diag(298.5, 143.8, 281.3, 123.5, weight=96.0)
    g.diag(281.3, 123.5, 332.8, 13.6, weight=96.0)
    g.vbar(581.2, 256.2, 467.0, weight=96.0)
    g.hbar(579.5, 852.9, 481.1, weight=48.0)
    g.diag(852.9, 507.2, 891.4, 473.6, weight=48.0)
    g.diag(891.4, 473.6, 839.2, 347.7, weight=48.0)
    g.hbar(622.7, 853.6, 305.6, weight=48.0)
    g.diag(853.6, 332.8, 868.9, 356.5, weight=48.0)
    g.diag(668.7, 731.3, 728.6, 684.9, weight=96.0)
    g.vbar(713.1, 135.3, 684.9, weight=96.0)
    g.hbar(511.4, 583.7, 76.4, weight=96.0)
    g.hbar(583.7, 846.0, 110.1, weight=96.0)
    g.diag(846.0, 154.3, 855.0, 149.2, weight=96.0)
    g.diag(845.6, 191.8, 947.0, 14.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_885b() -> Glyph:
    """衛 U+885B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni885B", advance=1000, unicode=0x885B, note="衛：自动生成")
    g.diag(258.3, 789.3, 286.8, 746.6, weight=84.0)
    g.diag(286.8, 746.6, 147.3, 574.0, weight=84.0)
    g.diag(249.6, 600.3, 210.8, 487.8, weight=48.0)
    g.diag(210.8, 487.8, 47.0, 267.3, weight=48.0)
    g.vbar(205.3, 7.2, 393.9, weight=48.0)
    g.diag(435.6, 770.8, 466.5, 743.6, weight=84.0)
    g.diag(466.5, 743.6, 425.9, 529.2, weight=84.0)
    g.hbar(375.2, 594.0, 623.2, weight=48.0)
    g.diag(594.0, 638.2, 535.9, 558.5, weight=48.0)
    g.hbar(332.4, 666.4, 515.1, weight=48.0)
    g.dot(367.9, 381.2, w=84.0, h=108.5, slant=-14.0)
    g.diag(387.9, 427.9, 394.5, 424.3, weight=48.0)
    g.hbar(394.5, 585.8, 434.4, weight=48.0)
    g.diag(585.8, 444.4, 529.1, 396.8, weight=48.0)
    g.hbar(408.3, 571.9, 353.4, weight=48.0)
    g.hbar(375.2, 580.7, 267.7, weight=48.0)
    g.diag(333.3, 216.6, 356.7, 192.3, weight=64.0)
    g.diag(356.7, 192.3, 341.8, 128.5, weight=64.0)
    g.hbar(341.8, 647.9, 140.9, weight=64.0)
    g.diag(444.4, 339.3, 485.6, 311.5, weight=84.0)
    g.vbar(482.0, -49.3, 311.5, weight=84.0)
    g.hbar(675.2, 884.6, 621.8, weight=64.0)
    g.hbar(630.4, 943.0, 448.9, weight=84.0)
    g.diag(735.6, 425.0, 807.4, 380.4, weight=84.0)
    g.diag(807.4, 380.4, 737.9, 8.0, weight=84.0)
    g.diag(737.9, 8.0, 650.8, 50.1, weight=84.0)
    return g
def g_cjk_unified_ideograph_885d() -> Glyph:
    """衝 U+885D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni885D", advance=1000, unicode=0x885D, note="衝：自动生成")
    g.diag(255.0, 756.5, 281.2, 711.8, weight=96.0)
    g.diag(281.2, 711.8, 143.9, 547.1, weight=96.0)
    g.diag(143.9, 547.1, 190.9, 474.6, weight=96.0)
    g.vbar(222.8, 496.1, 608.1, weight=48.0)
    g.diag(221.5, 496.1, 53.0, 270.9, weight=48.0)
    g.vbar(203.1, 11.0, 390.3, weight=48.0)
    g.hbar(522.6, 569.9, 718.8, weight=56.0)
    g.diag(522.6, 720.8, 363.7, 630.9, weight=56.0)
    g.diag(363.7, 630.9, 355.8, 582.3, weight=56.0)
    g.hbar(303.8, 640.5, 569.3, weight=64.0)
    g.vbar(351.4, 291.1, 467.7, weight=48.0)
    g.hbar(344.4, 619.9, 479.6, weight=48.0)
    g.vbar(592.5, 337.3, 494.7, weight=48.0)
    g.hbar(543.5, 565.2, 335.3, weight=48.0)
    g.hbar(369.7, 569.3, 397.9, weight=48.0)
    g.hbar(389.7, 545.1, 324.9, weight=56.0)
    g.hbar(436.2, 443.5, 641.1, weight=76.0)
    g.vbar(468.7, 217.3, 639.5, weight=76.0)
    g.diag(494.0, 217.3, 450.4, 147.6, weight=76.0)
    g.diag(370.1, 265.4, 423.9, 222.1, weight=64.0)
    g.diag(423.9, 222.1, 567.5, 289.0, weight=64.0)
    g.hbar(239.9, 566.1, 127.9, weight=84.0)
    g.diag(566.1, 146.6, 593.0, 227.6, weight=84.0)
    g.hbar(645.8, 865.9, 596.0, weight=96.0)
    g.hbar(612.9, 937.0, 425.6, weight=48.0)
    g.diag(732.1, 388.5, 811.4, 350.3, weight=96.0)
    g.diag(811.4, 350.3, 719.1, -0.6, weight=96.0)
    g.diag(719.1, -0.6, 605.4, 125.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_8861() -> Glyph:
    """衡 U+8861 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8861", advance=1000, unicode=0x8861, note="衡：自动生成")
    g.diag(252.8, 750.7, 277.3, 714.4, weight=96.0)
    g.diag(277.3, 714.4, 163.9, 554.3, weight=96.0)
    g.hbar(163.9, 203.2, 550.5, weight=96.0)
    g.vbar(204.9, 452.7, 582.4, weight=48.0)
    g.diag(198.5, 452.7, 53.0, 235.4, weight=48.0)
    g.vbar(212.7, 245.9, 381.8, weight=48.0)
    g.vbar(216.1, -2.0, 245.9, weight=48.0)
    g.diag(428.4, 757.5, 452.7, 722.6, weight=48.0)
    g.diag(452.7, 722.6, 328.1, 517.4, weight=48.0)
    g.hbar(435.2, 553.8, 658.6, weight=48.0)
    g.diag(553.8, 666.0, 466.0, 523.9, weight=48.0)
    g.vbar(344.8, 485.0, 490.3, weight=76.0)
    g.vbar(363.3, 310.6, 485.0, weight=76.0)
    g.hbar(365.9, 603.7, 498.5, weight=48.0)
    g.vbar(579.7, 342.5, 521.0, weight=48.0)
    g.hbar(536.8, 555.7, 342.1, weight=48.0)
    g.hbar(385.5, 555.7, 414.3, weight=56.0)
    g.diag(451.6, 482.4, 465.9, 470.2, weight=64.0)
    g.vbar(464.4, 376.0, 470.2, weight=64.0)
    g.diag(462.9, 376.0, 451.6, 362.8, weight=64.0)
    g.diag(401.4, 329.0, 404.3, 333.8, weight=56.0)
    g.hbar(404.3, 530.7, 346.8, weight=56.0)
    g.hbar(260.9, 565.1, 233.6, weight=92.0)
    g.vbar(571.4, 253.9, 313.8, weight=92.0)
    g.diag(428.4, 322.2, 489.6, 253.5, weight=56.0)
    g.diag(489.6, 253.5, 232.8, 44.0, weight=56.0)
    g.diag(497.1, 203.4, 630.3, 49.5, weight=96.0)
    g.hbar(583.6, 862.7, 645.5, weight=96.0)
    g.hbar(622.8, 937.0, 452.2, weight=96.0)
    g.diag(731.4, 425.5, 790.6, 376.2, weight=96.0)
    g.vbar(767.3, -23.0, 376.2, weight=96.0)
    g.diag(744.1, -23.0, 622.2, 58.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_8877() -> Glyph:
    """衷 U+8877 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8877", advance=1000, unicode=0x8877, note="衷：自动生成")
    g.diag(416.7, 782.0, 530.6, 706.1, weight=56.0)
    g.hbar(199.6, 773.0, 627.6, weight=96.0)
    g.diag(260.7, 487.9, 298.7, 454.2, weight=96.0)
    g.vbar(318.2, 308.7, 454.2, weight=96.0)
    g.hbar(328.2, 346.7, 476.5, weight=48.0)
    g.hbar(346.7, 642.1, 501.0, weight=48.0)
    g.diag(642.1, 529.5, 684.2, 494.0, weight=48.0)
    g.diag(684.2, 494.0, 656.0, 427.8, weight=48.0)
    g.diag(656.0, 427.8, 627.5, 409.9, weight=48.0)
    g.hbar(355.6, 474.0, 342.7, weight=48.0)
    g.hbar(474.0, 685.5, 363.2, weight=48.0)
    g.diag(456.8, 593.3, 488.2, 574.0, weight=96.0)
    g.vbar(484.6, 261.3, 574.0, weight=96.0)
    g.diag(394.6, 277.1, 323.6, 179.8, weight=56.0)
    g.diag(323.6, 179.8, 61.5, 5.2, weight=56.0)
    g.vbar(363.0, -73.3, 140.1, weight=48.0)
    g.diag(351.4, -73.3, 530.2, 61.7, weight=48.0)
    g.diag(530.2, 61.7, 534.8, 66.3, weight=48.0)
    g.diag(708.7, 298.2, 729.5, 254.6, weight=96.0)
    g.diag(729.5, 254.6, 587.1, 148.1, weight=96.0)
    g.hbar(576.9, 587.1, 149.4, weight=96.0)
    g.diag(455.7, 232.9, 938.5, -49.6, weight=92.0)
    return g
def g_cjk_unified_ideograph_888b() -> Glyph:
    """袋 U+888B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni888B", advance=1000, unicode=0x888B, note="袋：自动生成")
    g.diag(262.7, 745.9, 237.1, 645.2, weight=48.0)
    g.diag(237.1, 645.2, 67.0, 416.7, weight=48.0)
    g.vbar(254.2, 301.4, 596.2, weight=48.0)
    g.hbar(300.5, 686.7, 609.8, weight=96.0)
    g.diag(317.0, 742.1, 500.8, 632.2, weight=96.0)
    g.diag(500.8, 632.2, 781.4, 360.2, weight=96.0)
    g.vbar(791.0, 360.2, 527.1, weight=96.0)
    g.diag(622.3, 666.2, 681.1, 729.8, weight=96.0)
    g.vbar(678.7, 657.5, 729.8, weight=96.0)
    g.hbar(379.1, 434.3, 430.7, weight=48.0)
    g.diag(434.3, 418.7, 472.3, 347.2, weight=48.0)
    g.hbar(244.5, 367.8, 318.1, weight=48.0)
    g.hbar(367.8, 601.9, 335.5, weight=48.0)
    g.diag(402.2, 263.1, 312.7, 185.2, weight=48.0)
    g.diag(312.7, 185.2, 44.9, -61.0, weight=48.0)
    g.diag(44.9, -61.0, 75.0, -18.9, weight=48.0)
    g.vbar(358.1, -72.0, 178.8, weight=96.0)
    g.diag(351.1, -72.0, 557.4, 87.2, weight=96.0)
    g.diag(735.3, 366.9, 569.7, 170.0, weight=96.0)
    g.hbar(555.7, 569.7, 171.4, weight=96.0)
    g.diag(416.2, 256.1, 933.0, 5.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_8896() -> Glyph:
    """袖 U+8896 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8896", advance=1000, unicode=0x8896, note="袖：自动生成")
    g.diag(292.9, 773.8, 424.2, 664.8, weight=96.0)
    g.hbar(80.2, 223.4, 439.0, weight=48.0)
    g.diag(223.4, 408.0, 58.0, 117.7, weight=48.0)
    g.vbar(285.3, -53.8, 320.4, weight=48.0)
    g.diag(465.3, 385.6, 375.4, 331.7, weight=96.0)
    g.hbar(375.4, 377.6, 331.6, weight=96.0)
    g.diag(348.7, 322.1, 413.6, 272.2, weight=76.0)
    g.diag(413.6, 272.2, 399.8, 303.2, weight=76.0)
    g.vbar(505.7, 339.3, 444.6, weight=48.0)
    g.diag(509.7, 339.3, 555.9, 60.0, weight=48.0)
    g.hbar(508.7, 809.3, 383.7, weight=48.0)
    g.diag(809.3, 335.2, 852.3, 44.4, weight=48.0)
    g.vbar(852.5, 19.2, 44.4, weight=48.0)
    g.hbar(560.5, 855.6, 276.1, weight=96.0)
    g.diag(641.1, 760.0, 681.5, 627.6, weight=48.0)
    g.vbar(684.3, 147.4, 627.6, weight=48.0)
    g.diag(687.1, 147.4, 668.2, 117.7, weight=48.0)
    g.hbar(566.0, 830.0, 98.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_88f8() -> Glyph:
    """裸 U+88F8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni88F8", advance=1000, unicode=0x88F8, note="裸：自动生成")
    g.diag(261.3, 760.3, 399.7, 666.6, weight=96.0)
    g.diag(82.0, 521.6, 205.4, 446.0, weight=48.0)
    g.diag(205.4, 446.0, 58.0, 185.0, weight=48.0)
    g.vbar(253.4, 25.9, 358.3, weight=48.0)
    g.diag(329.4, 485.6, 392.6, 436.2, weight=64.0)
    g.diag(392.6, 436.2, 349.5, 383.5, weight=64.0)
    g.hbar(340.8, 349.5, 384.4, weight=64.0)
    g.diag(322.0, 381.9, 404.7, 306.8, weight=48.0)
    g.vbar(477.2, 411.6, 651.0, weight=48.0)
    g.hbar(460.9, 794.0, 661.5, weight=48.0)
    g.vbar(757.4, 447.1, 674.8, weight=48.0)
    g.hbar(516.9, 720.7, 542.1, weight=84.0)
    g.hbar(524.0, 688.6, 443.9, weight=84.0)
    g.diag(688.6, 463.9, 702.3, 452.5, weight=84.0)
    g.hbar(400.7, 865.3, 327.9, weight=48.0)
    g.diag(586.3, 644.3, 612.8, 624.2, weight=92.0)
    g.vbar(611.0, -40.3, 624.2, weight=92.0)
    g.diag(583.8, 310.8, 338.9, 78.6, weight=48.0)
    g.diag(634.7, 319.4, 803.8, 132.1, weight=48.0)
    g.hbar(803.8, 942.0, 118.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_88fd() -> Glyph:
    """製 U+88FD —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni88FD", advance=1000, unicode=0x88FD, note="製：自动生成")
    g.diag(222.5, 722.8, 242.6, 690.0, weight=92.0)
    g.diag(242.6, 690.0, 155.5, 575.9, weight=92.0)
    g.hbar(248.1, 467.0, 663.1, weight=64.0)
    g.hbar(114.1, 485.7, 559.6, weight=64.0)
    g.diag(194.9, 466.5, 215.2, 444.9, weight=96.0)
    g.vbar(209.5, 287.0, 444.9, weight=96.0)
    g.diag(236.3, 441.8, 257.0, 458.9, weight=56.0)
    g.hbar(257.0, 492.5, 479.0, weight=56.0)
    g.vbar(477.7, 349.9, 499.1, weight=56.0)
    g.hbar(398.8, 462.9, 362.2, weight=56.0)
    g.diag(398.8, 374.4, 395.0, 378.7, weight=56.0)
    g.diag(307.3, 777.0, 350.7, 740.9, weight=92.0)
    g.vbar(339.9, 309.7, 740.9, weight=92.0)
    g.diag(546.8, 670.5, 577.4, 633.6, weight=96.0)
    g.vbar(573.9, 455.6, 633.6, weight=96.0)
    g.diag(674.0, 737.6, 798.4, 319.5, weight=96.0)
    g.diag(798.4, 319.5, 597.1, 415.2, weight=96.0)
    g.dot(416.7, 283.1, w=48.0, h=62.4, slant=-14.0)
    g.hbar(194.9, 610.9, 233.8, weight=48.0)
    g.diag(400.9, 194.4, 330.4, 131.2, weight=48.0)
    g.diag(330.4, 131.2, 83.5, -41.2, weight=48.0)
    g.vbar(373.1, -60.4, 110.6, weight=48.0)
    g.diag(377.8, -60.4, 518.2, 35.7, weight=48.0)
    g.diag(657.2, 263.4, 675.5, 223.8, weight=76.0)
    g.diag(675.5, 223.8, 546.8, 127.8, weight=76.0)
    g.hbar(537.0, 546.8, 129.1, weight=76.0)
    g.hbar(423.6, 916.5, 86.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_88fe() -> Glyph:
    """裾 U+88FE —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni88FE", advance=1000, unicode=0x88FE, note="裾：自动生成")
    g.diag(250.7, 754.7, 431.1, 662.9, weight=96.0)
    g.hbar(86.8, 210.8, 462.8, weight=48.0)
    g.diag(210.8, 435.0, 58.0, 168.8, weight=48.0)
    g.diag(236.4, 334.4, 177.0, 106.8, weight=48.0)
    g.diag(177.0, 106.8, 284.3, -24.5, weight=48.0)
    g.hbar(328.8, 448.6, 397.6, weight=96.0)
    g.hbar(328.8, 335.1, 375.2, weight=96.0)
    g.dot(359.7, 322.3, w=96.0, h=124.8, slant=-14.0)
    g.hbar(512.1, 791.9, 659.3, weight=48.0)
    g.diag(791.9, 674.4, 725.9, 546.5, weight=48.0)
    g.hbar(515.1, 759.7, 523.7, weight=48.0)
    g.diag(504.7, 652.9, 468.8, 486.3, weight=48.0)
    g.diag(468.8, 486.3, 265.6, -25.7, weight=48.0)
    g.hbar(502.9, 922.0, 332.7, weight=96.0)
    g.diag(641.9, 476.7, 677.7, 427.0, weight=96.0)
    g.vbar(665.8, 210.5, 427.0, weight=96.0)
    g.diag(653.9, 210.5, 637.0, 193.6, weight=96.0)
    g.diag(550.5, 173.1, 538.7, 156.9, weight=48.0)
    g.vbar(560.8, -24.7, 156.9, weight=48.0)
    g.hbar(556.4, 768.5, 180.2, weight=48.0)
    g.diag(768.5, 196.0, 810.7, 164.1, weight=48.0)
    g.diag(810.7, 164.1, 754.3, 44.8, weight=48.0)
    g.diag(588.3, -8.7, 607.4, 6.9, weight=48.0)
    g.hbar(607.4, 789.6, 16.4, weight=48.0)
    g.vbar(788.2, 25.9, 53.6, weight=48.0)
    return g
def g_cjk_unified_ideograph_8907() -> Glyph:
    """複 U+8907 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8907", advance=1000, unicode=0x8907, note="複：自动生成")
    g.diag(276.1, 748.4, 438.8, 624.3, weight=96.0)
    g.diag(91.1, 451.4, 215.2, 390.8, weight=48.0)
    g.diag(215.2, 390.8, 58.0, 117.5, weight=48.0)
    g.vbar(252.7, -40.2, 292.1, weight=48.0)
    g.diag(336.2, 428.0, 397.8, 378.4, weight=64.0)
    g.diag(397.8, 378.4, 360.8, 328.8, weight=64.0)
    g.hbar(352.0, 360.8, 329.2, weight=64.0)
    g.diag(321.8, 319.0, 383.2, 280.1, weight=96.0)
    g.diag(383.2, 280.1, 378.8, 294.8, weight=96.0)
    g.vbar(573.7, 727.0, 744.8, weight=96.0)
    g.diag(573.4, 744.8, 468.8, 600.4, weight=96.0)
    g.hbar(576.9, 795.0, 702.1, weight=96.0)
    g.diag(476.6, 582.8, 541.6, 339.9, weight=48.0)
    g.hbar(517.1, 734.1, 568.4, weight=48.0)
    g.vbar(713.3, 367.2, 582.6, weight=48.0)
    g.hbar(668.9, 692.4, 370.9, weight=48.0)
    g.diag(547.0, 446.2, 556.9, 460.8, weight=64.0)
    g.hbar(556.9, 684.3, 459.3, weight=64.0)
    g.diag(555.5, 353.1, 563.8, 364.5, weight=76.0)
    g.hbar(563.8, 642.3, 369.4, weight=76.0)
    g.diag(642.3, 374.3, 651.9, 365.8, weight=76.0)
    g.diag(529.2, 305.0, 547.3, 268.2, weight=76.0)
    g.diag(547.3, 268.2, 417.7, 111.8, weight=76.0)
    g.hbar(285.5, 417.7, 94.0, weight=76.0)
    g.diag(560.4, 256.7, 614.0, 186.3, weight=48.0)
    g.diag(614.0, 186.3, 420.2, -6.2, weight=48.0)
    g.hbar(517.5, 533.1, 185.2, weight=96.0)
    g.diag(533.1, 185.6, 788.7, -25.3, weight=96.0)
    g.hbar(788.7, 942.0, -28.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_8910() -> Glyph:
    """褐 U+8910 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8910", advance=1000, unicode=0x8910, note="褐：自动生成")
    g.diag(297.6, 772.0, 464.4, 684.4, weight=96.0)
    g.hbar(100.7, 248.2, 465.0, weight=48.0)
    g.diag(248.2, 439.7, 93.7, 162.1, weight=48.0)
    g.vbar(287.6, -57.0, 334.4, weight=48.0)
    g.diag(506.9, 373.1, 428.9, 408.5, weight=76.0)
    g.diag(428.9, 408.5, 389.5, 349.9, weight=76.0)
    g.hbar(379.9, 389.5, 350.0, weight=76.0)
    g.dot(383.4, 311.6, w=96.0, h=97.9, slant=-14.0)
    g.vbar(527.0, 678.0, 688.2, weight=48.0)
    g.diag(526.2, 678.0, 574.4, 439.9, weight=48.0)
    g.hbar(539.3, 823.3, 688.9, weight=48.0)
    g.vbar(796.8, 482.1, 696.2, weight=48.0)
    g.hbar(744.9, 770.2, 482.8, weight=48.0)
    g.diag(583.4, 566.0, 591.0, 581.2, weight=84.0)
    g.hbar(591.0, 762.5, 582.4, weight=84.0)
    g.diag(592.5, 466.0, 602.4, 475.0, weight=84.0)
    g.hbar(602.4, 736.4, 484.0, weight=84.0)
    g.diag(551.1, 441.8, 571.3, 407.0, weight=76.0)
    g.diag(571.3, 407.0, 460.2, 291.5, weight=76.0)
    g.diag(552.1, 341.8, 796.8, 220.3, weight=64.0)
    g.vbar(808.5, -62.8, 220.3, weight=64.0)
    g.diag(820.2, -62.8, 723.3, -11.3, weight=64.0)
    g.diag(723.3, -11.3, 732.4, 59.1, weight=64.0)
    g.diag(640.7, 319.4, 667.6, 286.7, weight=96.0)
    g.diag(667.6, 286.7, 542.2, 120.1, weight=96.0)
    g.vbar(542.3, 111.2, 120.1, weight=96.0)
    g.hbar(651.2, 739.8, 198.5, weight=56.0)
    g.vbar(740.5, 107.0, 178.9, weight=56.0)
    g.diag(460.2, 263.0, 493.5, 228.8, weight=76.0)
    g.vbar(488.5, 65.9, 228.8, weight=76.0)
    g.hbar(483.5, 730.1, 78.6, weight=76.0)
    g.diag(730.1, 91.4, 762.4, 121.1, weight=76.0)
    return g
def g_cjk_unified_ideograph_8912() -> Glyph:
    """褒 U+8912 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8912", advance=1000, unicode=0x8912, note="褒：自动生成")
    g.diag(448.8, 787.0, 527.7, 745.0, weight=48.0)
    g.diag(527.7, 745.0, 559.4, 676.9, weight=48.0)
    g.hbar(247.0, 798.0, 651.8, weight=48.0)
    g.diag(342.3, 604.4, 304.7, 517.9, weight=48.0)
    g.diag(304.7, 517.9, 132.3, 354.8, weight=48.0)
    g.diag(309.4, 466.6, 276.3, 374.1, weight=48.0)
    g.diag(276.3, 374.1, 356.1, 205.4, weight=48.0)
    g.dot(492.6, 518.1, w=96.0, h=124.8, slant=-14.0)
    g.hbar(501.2, 753.8, 588.7, weight=48.0)
    g.diag(753.8, 606.2, 694.5, 521.2, weight=48.0)
    g.hbar(526.9, 539.5, 487.5, weight=48.0)
    g.hbar(539.5, 702.4, 498.5, weight=48.0)
    g.hbar(339.7, 848.2, 394.3, weight=48.0)
    g.diag(574.8, 472.6, 578.5, 469.7, weight=48.0)
    g.vbar(589.9, 188.9, 469.7, weight=48.0)
    g.diag(566.8, 377.7, 544.7, 335.5, weight=48.0)
    g.diag(544.7, 335.5, 409.1, 234.0, weight=48.0)
    g.diag(657.9, 391.3, 810.3, 260.6, weight=48.0)
    g.diag(428.3, 214.5, 321.1, 148.2, weight=48.0)
    g.diag(321.1, 148.2, 75.0, -19.0, weight=48.0)
    g.vbar(354.7, -66.1, 129.4, weight=64.0)
    g.diag(361.6, -66.1, 551.3, 83.1, weight=64.0)
    g.diag(790.0, 228.0, 621.6, 109.1, weight=96.0)
    g.hbar(613.7, 621.6, 110.6, weight=96.0)
    g.hbar(429.5, 436.5, 195.9, weight=96.0)
    g.diag(429.5, 194.6, 925.0, -41.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_895f() -> Glyph:
    """襟 U+895F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni895F", advance=1000, unicode=0x895F, note="襟：自动生成")
    g.diag(245.0, 756.2, 326.4, 703.9, weight=96.0)
    g.diag(326.4, 703.9, 373.7, 611.4, weight=96.0)
    g.diag(77.2, 502.2, 189.4, 425.5, weight=48.0)
    g.diag(189.4, 425.5, 53.0, 185.1, weight=48.0)
    g.vbar(237.1, -17.5, 354.2, weight=48.0)
    g.hbar(377.8, 399.1, 391.5, weight=96.0)
    g.diag(377.8, 393.6, 330.3, 347.1, weight=96.0)
    g.diag(300.3, 345.1, 355.5, 309.2, weight=96.0)
    g.diag(355.5, 309.2, 351.0, 314.7, weight=96.0)
    g.vbar(442.4, 560.4, 576.0, weight=96.0)
    g.hbar(444.0, 590.2, 590.0, weight=96.0)
    g.diag(477.7, 714.6, 497.9, 588.3, weight=48.0)
    g.vbar(496.2, 329.5, 588.3, weight=48.0)
    g.diag(488.1, 560.3, 492.6, 564.0, weight=48.0)
    g.diag(492.6, 564.0, 391.3, 410.2, weight=48.0)
    g.diag(525.1, 528.6, 587.7, 472.6, weight=48.0)
    g.hbar(620.2, 764.0, 627.0, weight=96.0)
    g.vbar(764.9, 616.8, 637.4, weight=96.0)
    g.diag(677.4, 760.1, 703.1, 628.1, weight=48.0)
    g.vbar(708.7, 353.7, 628.1, weight=48.0)
    g.diag(684.7, 597.7, 574.0, 468.9, weight=48.0)
    g.diag(730.4, 599.2, 947.0, 465.4, weight=48.0)
    g.diag(497.3, 344.7, 508.6, 302.2, weight=76.0)
    g.hbar(508.6, 679.7, 317.5, weight=76.0)
    g.diag(679.7, 332.8, 721.8, 376.8, weight=76.0)
    g.hbar(365.5, 525.3, 238.3, weight=76.0)
    g.hbar(525.3, 876.2, 226.6, weight=76.0)
    g.diag(586.3, 197.7, 629.5, 165.8, weight=76.0)
    g.diag(629.5, 165.8, 595.2, -31.4, weight=76.0)
    g.diag(595.2, -31.4, 452.6, 38.9, weight=76.0)
    g.dot(462.4, 83.9, w=96.0, h=124.8, slant=0.0)
    g.diag(657.1, 136.7, 836.5, 16.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_89aa() -> Glyph:
    """親 U+89AA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni89AA", advance=1000, unicode=0x89AA, note="親：自动生成")
    g.diag(289.5, 787.0, 367.1, 744.2, weight=96.0)
    g.diag(367.1, 744.2, 393.8, 670.0, weight=96.0)
    g.diag(180.2, 567.5, 189.5, 580.6, weight=96.0)
    g.hbar(189.5, 385.5, 605.1, weight=96.0)
    g.hbar(385.5, 412.2, 623.8, weight=96.0)
    g.dot(228.2, 495.4, w=96.0, h=117.0, slant=-14.0)
    g.diag(371.6, 600.5, 400.1, 565.8, weight=64.0)
    g.diag(400.1, 565.8, 335.3, 444.6, weight=64.0)
    g.diag(110.7, 293.8, 125.7, 376.0, weight=96.0)
    g.hbar(125.7, 488.9, 407.9, weight=96.0)
    g.vbar(147.4, 217.9, 253.6, weight=96.0)
    g.hbar(148.2, 482.2, 278.7, weight=96.0)
    g.diag(279.5, 384.1, 323.6, 360.9, weight=64.0)
    g.vbar(304.6, 16.1, 360.9, weight=64.0)
    g.diag(285.7, 16.1, 155.5, 77.0, weight=64.0)
    g.vbar(165.2, 46.9, 216.5, weight=96.0)
    g.dot(410.9, 163.5, w=96.0, h=124.8, slant=-14.0)
    g.vbar(522.4, 543.5, 659.5, weight=48.0)
    g.vbar(523.9, 252.5, 543.5, weight=48.0)
    g.hbar(532.5, 709.2, 667.6, weight=48.0)
    g.vbar(723.7, 520.3, 684.6, weight=48.0)
    g.vbar(741.3, 225.6, 520.3, weight=48.0)
    g.hbar(548.3, 712.6, 527.0, weight=96.0)
    g.hbar(548.3, 711.0, 405.6, weight=96.0)
    g.hbar(543.4, 721.8, 285.8, weight=48.0)
    g.diag(536.3, 237.6, 561.0, 196.2, weight=84.0)
    g.diag(561.0, 196.2, 435.6, 13.2, weight=84.0)
    g.hbar(317.6, 435.6, 3.9, weight=84.0)
    g.diag(632.3, 275.9, 698.8, 134.4, weight=48.0)
    g.diag(698.8, 134.4, 908.3, -67.0, weight=48.0)
    g.vbar(915.9, -67.0, 110.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_8a13() -> Glyph:
    """訓 U+8A13 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8A13", advance=1000, unicode=0x8A13, note="訓：自动生成")
    g.diag(337.4, 752.3, 409.2, 709.7, weight=96.0)
    g.diag(409.2, 709.7, 427.2, 677.6, weight=96.0)
    g.hbar(111.4, 458.4, 538.1, weight=84.0)
    g.hbar(264.6, 427.2, 441.2, weight=76.0)
    g.hbar(268.4, 416.8, 339.1, weight=64.0)
    g.diag(188.9, 228.5, 219.3, 207.0, weight=96.0)
    g.diag(219.3, 207.0, 265.5, 47.9, weight=96.0)
    g.hbar(247.6, 418.2, 230.9, weight=48.0)
    g.diag(418.2, 248.5, 394.1, 167.1, weight=48.0)
    g.diag(394.1, 167.1, 371.4, 152.9, weight=48.0)
    g.diag(277.8, 99.0, 291.8, 113.0, weight=48.0)
    g.hbar(291.8, 418.7, 119.7, weight=48.0)
    g.diag(525.5, 546.2, 621.7, 462.1, weight=96.0)
    g.diag(621.7, 462.1, 422.5, 46.0, weight=96.0)
    g.vbar(682.9, 151.9, 592.5, weight=96.0)
    g.diag(798.7, 757.0, 837.3, 480.7, weight=96.0)
    g.vbar(842.1, -57.0, 480.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_8a50() -> Glyph:
    """詐 U+8A50 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8A50", advance=1000, unicode=0x8A50, note="詐：自动生成")
    g.diag(299.6, 783.2, 392.6, 735.3, weight=92.0)
    g.diag(392.6, 735.3, 429.8, 622.8, weight=92.0)
    g.hbar(94.2, 435.9, 554.4, weight=92.0)
    g.diag(435.9, 587.6, 513.6, 539.2, weight=92.0)
    g.diag(234.1, 499.6, 293.6, 439.2, weight=92.0)
    g.hbar(293.6, 439.4, 441.0, weight=92.0)
    g.diag(262.2, 249.2, 292.9, 316.6, weight=76.0)
    g.diag(292.9, 316.6, 444.0, 391.6, weight=76.0)
    g.diag(210.3, 213.6, 267.4, 44.8, weight=92.0)
    g.hbar(235.2, 429.9, 226.2, weight=48.0)
    g.diag(429.9, 252.7, 368.4, 128.1, weight=48.0)
    g.diag(273.9, 76.7, 401.6, 134.9, weight=48.0)
    g.diag(622.4, 794.0, 673.3, 734.9, weight=92.0)
    g.diag(673.3, 734.9, 440.6, 436.9, weight=92.0)
    g.diag(568.6, 505.4, 558.1, 499.1, weight=92.0)
    g.hbar(558.1, 920.8, 534.5, weight=92.0)
    g.diag(637.1, 483.9, 899.0, 229.7, weight=84.0)
    g.diag(899.0, 229.7, 676.2, -59.0, weight=84.0)
    g.hbar(701.7, 863.1, 383.2, weight=92.0)
    g.diag(701.7, 230.6, 712.3, 221.0, weight=92.0)
    g.hbar(712.3, 904.2, 231.7, weight=92.0)
    return g
def g_cjk_unified_ideograph_8a54() -> Glyph:
    """詔 U+8A54 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8A54", advance=1000, unicode=0x8A54, note="詔：自动生成")
    g.dot(400.5, 712.8, w=84.0, h=109.2, slant=-14.0)
    g.hbar(106.6, 482.4, 545.0, weight=96.0)
    g.hbar(259.3, 448.3, 433.4, weight=96.0)
    g.hbar(255.3, 444.2, 320.9, weight=96.0)
    g.diag(197.0, 183.2, 230.2, 148.0, weight=96.0)
    g.diag(230.2, 148.0, 267.4, -37.9, weight=96.0)
    g.diag(258.3, 164.1, 270.1, 179.2, weight=96.0)
    g.hbar(270.1, 429.4, 188.3, weight=96.0)
    g.diag(429.4, 197.4, 376.9, 80.7, weight=96.0)
    g.diag(285.5, 19.4, 300.1, 38.9, weight=96.0)
    g.hbar(300.1, 440.2, 47.2, weight=96.0)
    g.hbar(542.7, 907.9, 594.1, weight=96.0)
    g.diag(907.9, 615.2, 797.8, 325.2, weight=96.0)
    g.diag(797.8, 325.2, 712.6, 382.2, weight=96.0)
    g.diag(659.3, 554.0, 695.1, 512.4, weight=96.0)
    g.diag(695.1, 512.4, 487.5, 250.5, weight=96.0)
    g.diag(535.7, 192.2, 605.0, -57.0, weight=48.0)
    g.hbar(594.0, 694.1, 192.7, weight=48.0)
    g.hbar(694.1, 894.7, 208.2, weight=48.0)
    g.diag(894.7, 220.3, 839.2, 79.7, weight=48.0)
    g.diag(839.2, 79.7, 807.0, 57.6, weight=48.0)
    g.hbar(626.1, 712.3, -2.9, weight=48.0)
    g.hbar(712.3, 879.4, 13.7, weight=48.0)
    return g
def g_cjk_unified_ideograph_8a5e() -> Glyph:
    """詞 U+8A5E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8A5E", advance=1000, unicode=0x8A5E, note="詞：自动生成")
    g.dot(386.8, 711.2, w=92.0, h=119.6, slant=-14.0)
    g.hbar(94.5, 461.8, 536.2, weight=96.0)
    g.hbar(234.4, 414.5, 428.5, weight=84.0)
    g.hbar(239.4, 420.5, 327.9, weight=84.0)
    g.diag(178.0, 210.7, 248.5, -18.8, weight=48.0)
    g.diag(233.4, 208.6, 238.6, 205.4, weight=48.0)
    g.hbar(238.6, 410.0, 214.7, weight=48.0)
    g.diag(410.0, 224.0, 383.3, 123.1, weight=48.0)
    g.diag(383.3, 123.1, 359.1, 106.0, weight=48.0)
    g.diag(264.6, 67.8, 272.2, 61.5, weight=48.0)
    g.hbar(272.2, 416.5, 67.6, weight=48.0)
    g.diag(531.2, 593.0, 814.3, 409.5, weight=96.0)
    g.vbar(840.0, -62.6, 409.5, weight=96.0)
    g.diag(865.6, -62.6, 747.5, 0.4, weight=96.0)
    g.hbar(530.2, 732.5, 462.2, weight=96.0)
    g.diag(485.9, 329.4, 515.1, 298.2, weight=64.0)
    g.vbar(530.7, 144.2, 298.2, weight=64.0)
    g.hbar(541.3, 712.4, 329.3, weight=48.0)
    g.diag(712.4, 338.2, 686.2, 251.9, weight=48.0)
    g.diag(686.2, 251.9, 663.0, 235.8, weight=48.0)
    g.hbar(564.4, 717.4, 192.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_8a60() -> Glyph:
    """詠 U+8A60 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8A60", advance=1000, unicode=0x8A60, note="詠：自动生成")
    g.diag(261.0, 705.7, 338.4, 662.7, weight=96.0)
    g.diag(338.4, 662.7, 367.1, 555.9, weight=96.0)
    g.hbar(68.0, 454.5, 497.0, weight=84.0)
    g.diag(189.0, 312.2, 236.2, 379.9, weight=64.0)
    g.hbar(236.2, 302.1, 390.0, weight=64.0)
    g.diag(302.1, 400.0, 364.4, 368.0, weight=64.0)
    g.diag(185.4, 352.4, 232.5, 288.0, weight=64.0)
    g.hbar(232.5, 358.0, 308.0, weight=64.0)
    g.vbar(166.0, 178.8, 194.0, weight=48.0)
    g.vbar(189.9, 40.9, 178.8, weight=48.0)
    g.hbar(179.7, 347.0, 201.1, weight=48.0)
    g.diag(347.0, 213.9, 294.8, 107.4, weight=48.0)
    g.diag(220.9, 58.9, 231.8, 74.7, weight=96.0)
    g.hbar(231.8, 341.3, 80.2, weight=96.0)
    g.diag(543.8, 758.3, 634.6, 700.0, weight=96.0)
    g.diag(634.6, 700.0, 619.1, 586.4, weight=96.0)
    g.hbar(487.4, 596.0, 542.6, weight=48.0)
    g.vbar(603.5, 357.3, 554.4, weight=48.0)
    g.vbar(606.0, -27.6, 357.3, weight=48.0)
    g.diag(601.0, -27.6, 506.5, 17.8, weight=48.0)
    g.hbar(363.3, 558.9, 348.8, weight=76.0)
    g.diag(558.9, 364.6, 360.4, 62.0, weight=76.0)
    g.diag(763.6, 514.6, 791.6, 475.5, weight=48.0)
    g.diag(791.6, 475.5, 663.2, 349.3, weight=48.0)
    g.diag(650.8, 351.3, 817.4, 171.6, weight=96.0)
    g.hbar(817.4, 947.0, 160.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_8a69() -> Glyph:
    """詩 U+8A69 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8A69", advance=1000, unicode=0x8A69, note="詩：自动生成")
    g.diag(296.4, 756.6, 381.3, 706.1, weight=96.0)
    g.diag(381.3, 706.1, 400.6, 624.3, weight=96.0)
    g.hbar(78.0, 467.0, 552.9, weight=96.0)
    g.diag(210.6, 361.0, 255.7, 430.5, weight=84.0)
    g.hbar(255.7, 382.3, 434.3, weight=84.0)
    g.diag(211.5, 393.0, 245.6, 320.1, weight=84.0)
    g.diag(245.6, 320.1, 388.7, 385.5, weight=84.0)
    g.vbar(188.3, 190.4, 207.8, weight=48.0)
    g.vbar(212.3, 45.8, 190.4, weight=48.0)
    g.hbar(201.3, 384.4, 216.9, weight=48.0)
    g.diag(384.4, 233.4, 331.5, 120.5, weight=48.0)
    g.diag(243.9, 64.2, 254.0, 80.4, weight=96.0)
    g.hbar(254.0, 374.9, 95.9, weight=96.0)
    g.hbar(474.9, 755.6, 585.5, weight=96.0)
    g.diag(755.6, 602.2, 782.1, 510.6, weight=96.0)
    g.diag(597.8, 777.6, 640.7, 739.4, weight=96.0)
    g.vbar(634.9, 487.7, 739.4, weight=96.0)
    g.diag(629.2, 487.7, 612.1, 465.7, weight=96.0)
    g.hbar(396.0, 922.0, 446.0, weight=96.0)
    g.diag(467.3, 249.8, 498.4, 280.4, weight=96.0)
    g.hbar(498.4, 867.6, 300.6, weight=96.0)
    g.diag(647.3, 420.0, 713.1, 352.8, weight=96.0)
    g.vbar(693.1, -56.2, 352.8, weight=96.0)
    g.diag(673.0, -56.2, 559.6, 90.9, weight=96.0)
    g.diag(487.7, 238.0, 572.9, 39.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_8a6e() -> Glyph:
    """詮 U+8A6E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8A6E", advance=1000, unicode=0x8A6E, note="詮：自动生成")
    g.dot(359.1, 684.9, w=96.0, h=123.4, slant=-14.0)
    g.hbar(78.0, 453.1, 511.4, weight=84.0)
    g.hbar(226.9, 375.8, 411.8, weight=76.0)
    g.hbar(212.0, 363.7, 312.7, weight=76.0)
    g.diag(172.0, 194.0, 226.0, -15.4, weight=96.0)
    g.hbar(223.2, 375.5, 189.4, weight=48.0)
    g.diag(375.5, 206.2, 347.0, 116.8, weight=48.0)
    g.diag(347.0, 116.8, 323.7, 103.7, weight=48.0)
    g.dot(309.7, 57.2, w=96.0, h=124.8, slant=-14.0)
    g.diag(572.2, 718.0, 625.3, 676.4, weight=96.0)
    g.diag(625.3, 676.4, 400.9, 304.7, weight=96.0)
    g.diag(622.4, 610.9, 816.7, 388.4, weight=96.0)
    g.hbar(816.7, 937.0, 378.7, weight=96.0)
    g.hbar(478.2, 722.0, 315.0, weight=96.0)
    g.hbar(500.5, 734.1, 169.8, weight=96.0)
    g.diag(576.8, 280.5, 607.5, 256.3, weight=96.0)
    g.vbar(605.2, 62.8, 256.3, weight=96.0)
    g.diag(602.9, 62.8, 587.1, 43.2, weight=96.0)
    g.hbar(375.8, 878.4, 10.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_8a72() -> Glyph:
    """該 U+8A72 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8A72", advance=1000, unicode=0x8A72, note="該：自动生成")
    g.diag(324.7, 792.0, 412.6, 738.1, weight=96.0)
    g.diag(412.6, 738.1, 433.2, 609.7, weight=96.0)
    g.hbar(83.0, 470.3, 532.8, weight=96.0)
    g.diag(244.1, 353.1, 280.8, 418.4, weight=64.0)
    g.hbar(280.8, 370.7, 433.4, weight=64.0)
    g.diag(370.7, 448.4, 418.3, 392.0, weight=64.0)
    g.diag(245.7, 393.8, 280.8, 326.5, weight=64.0)
    g.hbar(280.8, 387.6, 345.0, weight=64.0)
    g.diag(387.6, 363.5, 411.8, 428.4, weight=64.0)
    g.vbar(198.8, 194.8, 215.7, weight=48.0)
    g.diag(197.1, 194.8, 256.9, 55.9, weight=48.0)
    g.hbar(210.7, 397.6, 225.6, weight=48.0)
    g.diag(397.6, 244.1, 348.8, 128.3, weight=48.0)
    g.diag(252.6, 72.9, 376.8, 134.9, weight=48.0)
    g.diag(630.4, 770.0, 704.3, 721.1, weight=96.0)
    g.diag(704.3, 721.1, 743.6, 624.7, weight=96.0)
    g.hbar(491.7, 937.0, 571.3, weight=96.0)
    g.diag(612.4, 534.3, 642.3, 505.4, weight=96.0)
    g.diag(642.3, 505.4, 525.4, 320.5, weight=96.0)
    g.hbar(525.4, 678.3, 330.5, weight=96.0)
    g.diag(812.1, 456.4, 683.3, 326.8, weight=56.0)
    g.diag(683.3, 326.8, 356.7, 12.9, weight=56.0)
    g.diag(742.1, 345.7, 715.7, 200.5, weight=56.0)
    g.diag(715.7, 200.5, 465.6, -57.0, weight=56.0)
    g.diag(747.2, 121.8, 927.0, -15.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_8a73() -> Glyph:
    """詳 U+8A73 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8A73", advance=1000, unicode=0x8A73, note="詳：自动生成")
    g.dot(345.3, 747.8, w=96.0, h=124.3, slant=-14.0)
    g.hbar(84.0, 459.2, 588.3, weight=84.0)
    g.hbar(249.0, 413.1, 490.1, weight=84.0)
    g.hbar(244.4, 410.3, 386.4, weight=84.0)
    g.diag(189.1, 261.0, 217.7, 239.8, weight=48.0)
    g.diag(217.7, 239.8, 256.4, 88.6, weight=48.0)
    g.diag(247.2, 256.4, 248.9, 255.1, weight=48.0)
    g.hbar(248.9, 401.6, 264.7, weight=48.0)
    g.diag(401.6, 274.4, 374.4, 192.8, weight=48.0)
    g.diag(374.4, 192.8, 355.0, 180.8, weight=48.0)
    g.diag(270.2, 143.0, 277.7, 139.3, weight=48.0)
    g.hbar(277.7, 396.5, 146.2, weight=48.0)
    g.dot(561.0, 686.5, w=96.0, h=99.2, slant=-14.0)
    g.diag(759.7, 792.0, 792.2, 759.1, weight=96.0)
    g.diag(792.2, 759.1, 688.7, 627.9, weight=96.0)
    g.hbar(489.6, 802.1, 564.8, weight=96.0)
    g.hbar(521.9, 777.2, 445.4, weight=96.0)
    g.hbar(458.3, 921.0, 319.6, weight=96.0)
    g.diag(606.7, 521.0, 588.1, 530.0, weight=96.0)
    g.diag(588.1, 530.0, 690.7, 19.4, weight=96.0)
    g.diag(690.7, 19.4, 636.2, -57.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_8a8c() -> Glyph:
    """誌 U+8A8C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8A8C", advance=1000, unicode=0x8A8C, note="誌：自动生成")
    g.diag(303.5, 734.3, 381.3, 688.6, weight=96.0)
    g.diag(381.3, 688.6, 409.5, 565.7, weight=96.0)
    g.hbar(78.0, 410.6, 494.9, weight=96.0)
    g.diag(410.6, 526.7, 467.3, 496.9, weight=96.0)
    g.diag(237.9, 300.2, 288.9, 373.7, weight=76.0)
    g.hbar(288.9, 384.2, 387.3, weight=76.0)
    g.diag(384.2, 400.9, 401.6, 333.1, weight=76.0)
    g.diag(235.3, 340.4, 279.2, 270.6, weight=76.0)
    g.hbar(279.2, 351.1, 282.8, weight=76.0)
    g.diag(351.1, 294.9, 402.7, 369.5, weight=76.0)
    g.vbar(223.5, -17.5, 149.5, weight=48.0)
    g.hbar(207.3, 379.6, 152.8, weight=48.0)
    g.vbar(367.8, 75.3, 168.3, weight=48.0)
    g.diag(356.0, 75.3, 333.4, 52.5, weight=48.0)
    g.diag(253.9, 0.4, 266.1, 17.6, weight=96.0)
    g.hbar(266.1, 376.1, 30.0, weight=96.0)
    g.hbar(471.2, 560.2, 477.9, weight=96.0)
    g.hbar(560.2, 824.5, 496.2, weight=96.0)
    g.diag(604.8, 768.3, 656.4, 726.5, weight=96.0)
    g.vbar(653.9, 383.4, 726.5, weight=96.0)
    g.diag(651.5, 383.4, 632.1, 355.2, weight=96.0)
    g.vbar(567.1, 262.2, 311.8, weight=84.0)
    g.hbar(565.0, 765.0, 336.1, weight=84.0)
    g.diag(765.0, 360.3, 811.6, 312.6, weight=84.0)
    g.dot(452.6, 81.6, w=96.0, h=124.8, slant=14.0)
    g.diag(503.3, 147.2, 621.0, 83.1, weight=96.0)
    g.hbar(621.0, 934.8, 25.7, weight=96.0)
    g.diag(934.8, -31.7, 726.3, 169.9, weight=96.0)
    g.diag(580.3, 289.0, 748.7, 166.1, weight=64.0)
    g.diag(810.9, 317.3, 947.0, 189.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_8a8d() -> Glyph:
    """認 U+8A8D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8A8D", advance=1000, unicode=0x8A8D, note="認：自动生成")
    g.diag(297.9, 709.3, 380.1, 653.9, weight=96.0)
    g.diag(380.1, 653.9, 395.9, 560.2, weight=96.0)
    g.hbar(78.0, 393.5, 495.4, weight=76.0)
    g.diag(393.5, 521.3, 453.2, 482.0, weight=76.0)
    g.diag(196.7, 444.7, 256.8, 383.3, weight=76.0)
    g.hbar(256.8, 344.7, 395.3, weight=76.0)
    g.diag(344.7, 407.2, 375.3, 342.0, weight=76.0)
    g.diag(214.2, 355.5, 252.0, 286.8, weight=76.0)
    g.hbar(252.0, 345.7, 299.2, weight=76.0)
    g.vbar(359.0, 311.7, 377.7, weight=76.0)
    g.vbar(214.2, 24.7, 183.0, weight=48.0)
    g.hbar(195.3, 389.0, 185.9, weight=48.0)
    g.diag(389.0, 199.6, 330.2, 87.5, weight=48.0)
    g.hbar(238.7, 361.4, 66.7, weight=48.0)
    g.diag(549.7, 547.0, 545.7, 555.1, weight=96.0)
    g.hbar(545.7, 805.8, 579.3, weight=96.0)
    g.diag(805.8, 603.4, 725.4, 297.7, weight=96.0)
    g.diag(725.4, 297.7, 595.9, 361.9, weight=96.0)
    g.diag(586.6, 536.3, 620.5, 516.5, weight=96.0)
    g.diag(620.5, 516.5, 469.0, 208.9, weight=96.0)
    g.dot(501.0, 443.0, w=96.0, h=124.8, slant=-14.0)
    g.diag(496.3, 167.1, 437.2, 31.6, weight=96.0)
    g.hbar(402.5, 437.2, 33.8, weight=96.0)
    g.diag(513.3, 162.8, 785.2, 6.4, weight=96.0)
    g.hbar(785.2, 939.2, -16.2, weight=96.0)
    g.diag(939.2, -38.8, 743.9, 152.1, weight=96.0)
    g.hbar(579.7, 768.7, 161.4, weight=96.0)
    g.diag(781.2, 315.7, 936.6, 228.2, weight=96.0)
    g.diag(936.6, 228.2, 853.8, 153.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_8a93() -> Glyph:
    """誓 U+8A93 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8A93", advance=1000, unicode=0x8A93, note="誓：自动生成")
    g.hbar(227.4, 500.4, 689.1, weight=64.0)
    g.diag(361.6, 714.4, 389.2, 784.0, weight=96.0)
    g.vbar(376.6, 442.3, 784.0, weight=96.0)
    g.diag(363.9, 442.3, 277.4, 496.9, weight=96.0)
    g.hbar(147.6, 191.8, 505.7, weight=56.0)
    g.diag(191.8, 501.0, 462.2, 667.1, weight=56.0)
    g.hbar(699.5, 752.2, 776.6, weight=76.0)
    g.diag(699.5, 780.0, 579.6, 717.0, weight=76.0)
    g.diag(579.6, 717.0, 577.3, 713.0, weight=76.0)
    g.diag(545.3, 729.6, 509.9, 499.1, weight=96.0)
    g.diag(509.9, 499.1, 492.2, 488.8, weight=96.0)
    g.hbar(570.1, 836.7, 633.3, weight=84.0)
    g.diag(658.3, 613.6, 681.8, 596.7, weight=96.0)
    g.vbar(678.6, 416.9, 596.7, weight=96.0)
    g.diag(473.0, 487.3, 525.1, 382.2, weight=48.0)
    g.hbar(127.9, 877.1, 347.0, weight=56.0)
    g.diag(358.6, 211.6, 386.4, 260.2, weight=56.0)
    g.hbar(386.4, 598.1, 280.7, weight=56.0)
    g.vbar(600.9, 241.8, 301.2, weight=56.0)
    g.diag(345.8, 143.0, 390.3, 187.9, weight=56.0)
    g.hbar(390.3, 594.0, 205.3, weight=56.0)
    g.diag(594.0, 222.8, 610.6, 166.8, weight=56.0)
    g.vbar(347.2, -45.9, 119.8, weight=96.0)
    g.hbar(329.8, 665.2, 129.7, weight=48.0)
    g.diag(665.2, 134.8, 597.0, 28.8, weight=48.0)
    g.diag(387.7, -5.6, 403.8, -13.4, weight=48.0)
    g.hbar(403.8, 628.4, -1.3, weight=48.0)
    g.vbar(628.7, 10.9, 32.7, weight=48.0)
    return g
def g_cjk_unified_ideograph_8a98() -> Glyph:
    """誘 U+8A98 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8A98", advance=1000, unicode=0x8A98, note="誘：自动生成")
    g.diag(274.8, 763.2, 353.4, 714.5, weight=96.0)
    g.diag(353.4, 714.5, 372.9, 615.4, weight=96.0)
    g.hbar(73.0, 415.8, 550.2, weight=92.0)
    g.diag(183.3, 503.1, 252.0, 429.7, weight=84.0)
    g.diag(252.0, 429.7, 354.0, 541.7, weight=84.0)
    g.diag(191.3, 256.8, 232.1, 327.4, weight=84.0)
    g.hbar(232.1, 381.0, 342.9, weight=84.0)
    g.vbar(190.6, 59.9, 224.3, weight=48.0)
    g.hbar(177.0, 310.2, 230.1, weight=48.0)
    g.diag(310.2, 248.9, 353.5, 220.3, weight=48.0)
    g.diag(353.5, 220.3, 300.7, 130.1, weight=48.0)
    g.diag(217.2, 78.1, 232.6, 96.7, weight=96.0)
    g.hbar(232.6, 347.7, 110.5, weight=96.0)
    g.hbar(714.9, 773.0, 751.4, weight=64.0)
    g.diag(714.9, 755.6, 563.8, 677.2, weight=64.0)
    g.hbar(489.1, 563.8, 665.4, weight=64.0)
    g.diag(489.1, 653.6, 477.2, 585.9, weight=64.0)
    g.hbar(418.9, 860.5, 589.7, weight=48.0)
    g.diag(597.9, 669.9, 627.8, 571.9, weight=48.0)
    g.vbar(635.4, 363.6, 571.9, weight=48.0)
    g.diag(602.1, 561.5, 423.5, 324.5, weight=48.0)
    g.diag(651.7, 562.7, 947.0, 424.1, weight=48.0)
    g.diag(422.9, 327.1, 458.4, 296.3, weight=96.0)
    g.hbar(458.4, 746.6, 328.1, weight=96.0)
    g.diag(746.6, 359.9, 683.9, 234.0, weight=96.0)
    g.hbar(683.9, 838.6, 217.7, weight=96.0)
    g.diag(838.6, 201.3, 722.7, -56.3, weight=96.0)
    g.diag(722.7, -56.3, 625.8, 12.5, weight=96.0)
    g.diag(542.3, 293.9, 578.8, 252.6, weight=96.0)
    g.diag(578.8, 252.6, 383.2, -27.4, weight=96.0)
    g.diag(383.2, -27.4, 352.4, 72.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_8a9e() -> Glyph:
    """語 U+8A9E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8A9E", advance=1000, unicode=0x8A9E, note="語：自动生成")
    g.diag(278.9, 722.9, 353.4, 675.4, weight=96.0)
    g.diag(353.4, 675.4, 381.9, 572.2, weight=96.0)
    g.hbar(78.0, 386.1, 513.0, weight=92.0)
    g.diag(386.1, 533.9, 457.8, 475.1, weight=92.0)
    g.diag(207.8, 337.2, 252.0, 393.5, weight=64.0)
    g.hbar(252.0, 332.9, 404.2, weight=64.0)
    g.vbar(345.1, 350.3, 414.9, weight=64.0)
    g.diag(210.1, 367.9, 244.5, 307.0, weight=64.0)
    g.hbar(244.5, 320.8, 315.9, weight=64.0)
    g.hbar(320.8, 373.9, 315.9, weight=64.0)
    g.vbar(201.2, 39.9, 202.7, weight=48.0)
    g.hbar(182.7, 366.5, 203.5, weight=48.0)
    g.diag(366.5, 216.3, 313.2, 106.5, weight=48.0)
    g.diag(229.6, 58.6, 241.7, 73.8, weight=96.0)
    g.hbar(241.7, 355.8, 85.7, weight=96.0)
    g.diag(546.4, 594.5, 523.1, 605.5, weight=96.0)
    g.hbar(523.1, 799.0, 629.8, weight=96.0)
    g.diag(582.2, 580.5, 615.1, 560.6, weight=96.0)
    g.diag(615.1, 560.6, 554.2, 333.9, weight=96.0)
    g.diag(554.2, 333.9, 535.7, 317.3, weight=96.0)
    g.hbar(477.1, 758.4, 458.5, weight=48.0)
    g.diag(758.4, 473.2, 682.1, 332.6, weight=48.0)
    g.hbar(370.3, 573.8, 307.4, weight=48.0)
    g.hbar(573.8, 932.0, 309.2, weight=48.0)
    g.diag(509.1, 191.4, 498.4, 173.6, weight=48.0)
    g.vbar(523.7, -8.5, 173.6, weight=48.0)
    g.hbar(514.2, 794.2, 189.4, weight=48.0)
    g.diag(794.2, 197.1, 715.1, 59.9, weight=48.0)
    g.diag(551.6, 7.2, 571.7, 23.6, weight=48.0)
    g.hbar(571.7, 752.0, 33.2, weight=48.0)
    g.vbar(749.5, 42.7, 70.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_8aa0() -> Glyph:
    """誠 U+8AA0 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8AA0", advance=1000, unicode=0x8AA0, note="誠：自动生成")
    g.diag(285.2, 700.3, 368.2, 647.0, weight=96.0)
    g.diag(368.2, 647.0, 383.6, 557.4, weight=96.0)
    g.hbar(63.0, 376.7, 494.1, weight=92.0)
    g.diag(376.7, 518.9, 423.6, 467.9, weight=92.0)
    g.diag(207.5, 310.3, 251.5, 379.7, weight=84.0)
    g.hbar(251.5, 399.1, 399.7, weight=84.0)
    g.diag(195.9, 213.0, 253.6, 277.6, weight=76.0)
    g.hbar(253.6, 348.4, 292.9, weight=76.0)
    g.diag(348.4, 308.2, 357.6, 374.0, weight=76.0)
    g.vbar(169.1, 162.0, 182.1, weight=48.0)
    g.vbar(192.0, 23.8, 162.0, weight=48.0)
    g.hbar(179.8, 351.8, 187.2, weight=48.0)
    g.diag(351.8, 201.4, 299.0, 92.4, weight=48.0)
    g.dot(283.7, 63.7, w=96.0, h=124.8, slant=-14.0)
    g.diag(494.6, 418.9, 513.7, 410.1, weight=96.0)
    g.hbar(513.7, 790.2, 455.8, weight=96.0)
    g.diag(790.2, 501.5, 809.6, 421.7, weight=96.0)
    g.diag(475.8, 422.6, 448.5, 296.9, weight=48.0)
    g.diag(448.5, 296.9, 324.7, -26.6, weight=48.0)
    g.diag(484.8, 258.6, 558.9, 216.4, weight=48.0)
    g.vbar(554.3, 52.1, 216.4, weight=48.0)
    g.diag(549.7, 52.1, 455.0, 99.0, weight=48.0)
    g.diag(570.6, 761.6, 680.8, 487.3, weight=96.0)
    g.diag(680.8, 487.3, 881.9, -60.5, weight=96.0)
    g.diag(881.9, -60.5, 942.0, 144.3, weight=96.0)
    g.diag(807.7, 383.3, 840.1, 340.5, weight=76.0)
    g.diag(840.1, 340.5, 723.2, 122.3, weight=76.0)
    g.hbar(597.7, 723.2, 99.2, weight=76.0)
    g.hbar(671.8, 818.5, 665.0, weight=96.0)
    g.vbar(820.0, 538.4, 646.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_8aa4() -> Glyph:
    """誤 U+8AA4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8AA4", advance=1000, unicode=0x8AA4, note="誤：自动生成")
    g.diag(275.1, 695.5, 342.0, 662.4, weight=96.0)
    g.diag(342.0, 662.4, 372.3, 549.6, weight=96.0)
    g.hbar(78.0, 433.5, 476.9, weight=84.0)
    g.diag(197.7, 436.7, 255.9, 374.6, weight=76.0)
    g.hbar(255.9, 345.7, 386.5, weight=76.0)
    g.diag(345.7, 398.4, 372.6, 338.1, weight=76.0)
    g.diag(215.2, 215.2, 271.4, 281.1, weight=76.0)
    g.hbar(271.4, 343.9, 293.0, weight=76.0)
    g.diag(343.9, 304.9, 393.3, 258.6, weight=76.0)
    g.vbar(218.2, 24.7, 183.3, weight=48.0)
    g.hbar(202.1, 371.8, 184.0, weight=48.0)
    g.diag(371.8, 194.6, 320.3, 93.4, weight=48.0)
    g.diag(252.2, 40.9, 264.9, 58.5, weight=96.0)
    g.hbar(264.9, 367.2, 72.4, weight=96.0)
    g.diag(552.1, 627.3, 542.8, 619.4, weight=56.0)
    g.diag(542.8, 619.4, 587.9, 465.6, weight=56.0)
    g.hbar(563.5, 792.0, 641.4, weight=48.0)
    g.diag(792.0, 666.1, 714.4, 536.0, weight=48.0)
    g.diag(601.9, 481.5, 619.0, 498.4, weight=48.0)
    g.hbar(619.0, 748.4, 509.1, weight=48.0)
    g.vbar(749.5, 519.8, 540.1, weight=48.0)
    g.diag(465.8, 491.0, 493.3, 462.6, weight=48.0)
    g.diag(493.3, 462.6, 566.3, 403.9, weight=48.0)
    g.hbar(566.3, 763.2, 406.7, weight=48.0)
    g.diag(763.2, 409.5, 740.8, 324.2, weight=48.0)
    g.diag(740.8, 324.2, 711.5, 296.0, weight=48.0)
    g.hbar(372.6, 896.7, 238.1, weight=48.0)
    g.diag(556.5, 359.0, 620.5, 313.4, weight=96.0)
    g.diag(620.5, 313.4, 414.7, -16.6, weight=96.0)
    g.diag(414.7, -16.6, 359.4, 37.5, weight=96.0)
    g.diag(605.7, 239.3, 937.0, -10.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_8ab0() -> Glyph:
    """誰 U+8AB0 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8AB0", advance=1000, unicode=0x8AB0, note="誰：自动生成")
    g.diag(286.8, 765.3, 361.3, 723.3, weight=96.0)
    g.diag(361.3, 723.3, 388.3, 608.0, weight=96.0)
    g.hbar(78.0, 387.8, 534.5, weight=96.0)
    g.hbar(387.8, 467.2, 555.5, weight=96.0)
    g.diag(222.2, 337.9, 266.3, 406.5, weight=64.0)
    g.hbar(266.3, 346.4, 420.5, weight=64.0)
    g.hbar(346.4, 394.4, 428.2, weight=64.0)
    g.diag(221.8, 379.9, 251.0, 306.6, weight=64.0)
    g.diag(251.0, 306.6, 398.6, 382.2, weight=64.0)
    g.vbar(193.7, 191.2, 204.8, weight=48.0)
    g.diag(190.7, 191.2, 250.3, 55.2, weight=48.0)
    g.hbar(206.5, 383.8, 210.2, weight=48.0)
    g.diag(383.8, 221.4, 333.1, 122.6, weight=48.0)
    g.diag(248.4, 71.9, 362.2, 127.7, weight=48.0)
    g.diag(565.4, 782.0, 545.9, 664.8, weight=48.0)
    g.diag(545.9, 664.8, 390.3, 424.2, weight=48.0)
    g.vbar(523.5, -52.0, 514.1, weight=48.0)
    g.diag(639.5, 724.8, 733.2, 671.1, weight=96.0)
    g.diag(733.2, 671.1, 772.8, 581.4, weight=96.0)
    g.hbar(633.7, 651.0, 498.6, weight=96.0)
    g.hbar(633.7, 814.7, 527.4, weight=96.0)
    g.diag(814.7, 553.7, 787.3, 612.3, weight=96.0)
    g.hbar(582.4, 790.0, 388.3, weight=96.0)
    g.hbar(762.4, 790.0, 408.7, weight=96.0)
    g.hbar(579.5, 818.1, 272.0, weight=96.0)
    g.diag(818.1, 294.2, 838.1, 369.1, weight=96.0)
    g.diag(688.4, 487.6, 718.9, 467.6, weight=96.0)
    g.vbar(723.6, 182.7, 467.6, weight=96.0)
    g.diag(728.3, 182.7, 705.2, 153.0, weight=96.0)
    g.diag(570.9, 112.1, 579.5, 106.1, weight=96.0)
    g.hbar(579.5, 927.0, 123.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_8ab2() -> Glyph:
    """課 U+8AB2 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8AB2", advance=1000, unicode=0x8AB2, note="課：自动生成")
    g.dot(323.8, 720.4, w=96.0, h=124.8, slant=-14.0)
    g.hbar(74.5, 392.1, 561.1, weight=84.0)
    g.hbar(211.1, 350.5, 469.7, weight=76.0)
    g.hbar(200.3, 348.7, 373.8, weight=76.0)
    g.diag(140.5, 255.2, 206.6, 66.1, weight=48.0)
    g.diag(184.0, 256.1, 188.9, 253.8, weight=48.0)
    g.hbar(188.9, 335.1, 263.9, weight=48.0)
    g.diag(335.1, 273.9, 316.1, 199.1, weight=48.0)
    g.diag(316.1, 199.1, 295.3, 183.7, weight=48.0)
    g.vbar(224.9, 124.0, 141.4, weight=48.0)
    g.hbar(228.7, 344.2, 149.0, weight=48.0)
    g.vbar(462.3, 418.1, 646.2, weight=48.0)
    g.hbar(471.8, 570.8, 647.6, weight=48.0)
    g.hbar(570.8, 784.4, 661.6, weight=48.0)
    g.vbar(751.0, 455.2, 672.3, weight=48.0)
    g.diag(717.7, 455.2, 720.6, 439.8, weight=48.0)
    g.hbar(525.1, 678.1, 552.0, weight=76.0)
    g.diag(509.8, 433.5, 519.5, 445.9, weight=76.0)
    g.hbar(519.5, 688.0, 462.3, weight=76.0)
    g.hbar(388.5, 858.2, 332.6, weight=48.0)
    g.vbar(575.3, 458.6, 635.3, weight=84.0)
    g.vbar(586.6, -57.0, 458.6, weight=84.0)
    g.diag(566.8, 311.3, 516.9, 251.6, weight=48.0)
    g.diag(516.9, 251.6, 334.2, 76.0, weight=48.0)
    g.diag(608.4, 316.8, 940.5, 137.6, weight=48.0)
    return g
def g_cjk_unified_ideograph_8abf() -> Glyph:
    """調 U+8ABF —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8ABF", advance=1000, unicode=0x8ABF, note="調：自动生成")
    g.dot(351.3, 717.7, w=96.0, h=124.8, slant=-14.0)
    g.hbar(110.5, 439.4, 542.0, weight=92.0)
    g.hbar(238.5, 398.0, 437.1, weight=76.0)
    g.hbar(230.6, 387.2, 342.6, weight=76.0)
    g.diag(160.7, 225.4, 190.3, 191.9, weight=96.0)
    g.diag(190.3, 191.9, 220.8, 24.6, weight=96.0)
    g.diag(215.9, 205.7, 228.8, 221.9, weight=48.0)
    g.hbar(228.8, 374.0, 227.8, weight=48.0)
    g.diag(374.0, 233.7, 349.8, 147.6, weight=48.0)
    g.diag(349.8, 147.6, 326.1, 132.9, weight=48.0)
    g.diag(236.6, 78.7, 255.1, 96.1, weight=48.0)
    g.hbar(255.1, 379.3, 97.7, weight=48.0)
    g.vbar(473.8, 428.7, 633.0, weight=48.0)
    g.diag(475.7, 428.7, 356.7, -67.0, weight=48.0)
    g.hbar(530.0, 658.1, 629.3, weight=48.0)
    g.diag(658.1, 631.5, 823.0, 396.6, weight=48.0)
    g.vbar(841.1, -34.9, 396.6, weight=48.0)
    g.hbar(762.3, 859.3, -15.5, weight=48.0)
    g.hbar(577.2, 797.8, 491.7, weight=92.0)
    g.diag(639.2, 609.4, 687.1, 576.7, weight=48.0)
    g.diag(687.1, 576.7, 660.9, 396.7, weight=48.0)
    g.hbar(556.5, 805.6, 371.1, weight=92.0)
    g.diag(551.6, 262.8, 581.1, 232.3, weight=48.0)
    g.diag(581.1, 232.3, 605.8, 117.1, weight=48.0)
    g.diag(604.8, 256.9, 607.1, 255.1, weight=48.0)
    g.hbar(607.1, 774.5, 260.8, weight=48.0)
    g.diag(774.5, 266.6, 745.6, 196.9, weight=48.0)
    g.diag(745.6, 196.9, 723.9, 185.0, weight=48.0)
    g.diag(623.5, 132.9, 640.9, 150.3, weight=48.0)
    g.hbar(640.9, 766.2, 151.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_8ac7() -> Glyph:
    """談 U+8AC7 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8AC7", advance=1000, unicode=0x8AC7, note="談：自动生成")
    g.diag(281.4, 717.6, 437.6, 593.3, weight=96.0)
    g.hbar(68.0, 442.1, 499.7, weight=92.0)
    g.diag(185.7, 434.0, 245.1, 367.2, weight=84.0)
    g.hbar(245.1, 347.9, 382.4, weight=84.0)
    g.diag(347.9, 397.6, 416.2, 355.6, weight=84.0)
    g.diag(231.0, 202.4, 266.1, 270.9, weight=84.0)
    g.hbar(266.1, 403.6, 274.6, weight=84.0)
    g.diag(173.1, 166.6, 161.4, 146.8, weight=48.0)
    g.vbar(187.4, 6.2, 146.8, weight=48.0)
    g.hbar(177.3, 356.1, 167.6, weight=48.0)
    g.diag(356.1, 179.1, 301.0, 72.5, weight=48.0)
    g.diag(218.7, 24.7, 230.2, 39.3, weight=96.0)
    g.hbar(230.2, 340.6, 50.1, weight=96.0)
    g.dot(501.4, 519.9, w=96.0, h=122.7, slant=-14.0)
    g.diag(776.6, 667.7, 797.7, 625.8, weight=64.0)
    g.diag(797.7, 625.8, 662.8, 502.5, weight=64.0)
    g.diag(564.2, 742.1, 662.4, 649.3, weight=96.0)
    g.diag(662.4, 649.3, 439.5, 307.6, weight=96.0)
    g.hbar(627.8, 634.7, 487.1, weight=96.0)
    g.diag(634.7, 488.6, 725.7, 439.7, weight=96.0)
    g.diag(725.7, 439.7, 759.2, 374.3, weight=96.0)
    g.dot(490.3, 241.2, w=96.0, h=124.8, slant=-14.0)
    g.diag(759.2, 374.2, 773.3, 293.0, weight=56.0)
    g.diag(773.3, 293.0, 637.0, 200.8, weight=56.0)
    g.vbar(555.1, 233.7, 375.5, weight=48.0)
    g.diag(551.4, 233.7, 390.0, -14.5, weight=48.0)
    g.vbar(620.6, 167.5, 186.2, weight=96.0)
    g.diag(621.2, 167.5, 799.3, -7.3, weight=96.0)
    g.hbar(799.3, 942.0, -19.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_8acb() -> Glyph:
    """請 U+8ACB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8ACB", advance=1000, unicode=0x8ACB, note="請：自动生成")
    g.dot(334.2, 713.5, w=96.0, h=124.8, slant=-14.0)
    g.hbar(78.0, 429.0, 545.3, weight=84.0)
    g.hbar(200.8, 371.0, 439.9, weight=76.0)
    g.hbar(207.6, 363.3, 341.2, weight=76.0)
    g.diag(151.5, 206.8, 227.9, 14.4, weight=96.0)
    g.hbar(208.5, 366.3, 207.8, weight=48.0)
    g.diag(366.3, 225.3, 343.0, 140.1, weight=48.0)
    g.diag(343.0, 140.1, 318.8, 127.5, weight=48.0)
    g.diag(237.6, 85.0, 246.2, 79.6, weight=48.0)
    g.hbar(246.2, 375.8, 86.2, weight=48.0)
    g.hbar(495.7, 802.3, 638.6, weight=76.0)
    g.hbar(518.9, 758.7, 538.5, weight=76.0)
    g.diag(597.3, 779.3, 643.7, 740.6, weight=96.0)
    g.vbar(639.8, 472.7, 740.6, weight=96.0)
    g.diag(635.9, 472.7, 620.5, 450.5, weight=96.0)
    g.hbar(416.4, 927.0, 425.8, weight=76.0)
    g.diag(494.8, 340.3, 508.8, 226.1, weight=48.0)
    g.vbar(499.8, -44.6, 226.1, weight=48.0)
    g.diag(551.8, 326.7, 559.7, 323.0, weight=96.0)
    g.hbar(559.7, 817.8, 335.6, weight=96.0)
    g.vbar(756.3, -42.0, 348.3, weight=96.0)
    g.hbar(635.9, 694.8, -28.8, weight=96.0)
    g.diag(553.7, 213.6, 564.7, 226.9, weight=64.0)
    g.hbar(564.7, 676.6, 229.4, weight=64.0)
    g.hbar(543.1, 680.4, 129.9, weight=76.0)
    return g
def g_cjk_unified_ideograph_8ae6() -> Glyph:
    """諦 U+8AE6 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8AE6", advance=1000, unicode=0x8AE6, note="諦：自动生成")
    g.dot(365.9, 741.0, w=96.0, h=124.8, slant=-14.0)
    g.hbar(105.8, 451.7, 576.4, weight=84.0)
    g.hbar(246.8, 418.3, 482.8, weight=76.0)
    g.hbar(250.5, 410.9, 390.0, weight=76.0)
    g.diag(199.5, 264.4, 229.1, 236.6, weight=96.0)
    g.diag(229.1, 236.6, 269.9, 84.5, weight=96.0)
    g.hbar(252.3, 409.7, 264.8, weight=48.0)
    g.diag(409.7, 284.7, 384.1, 194.0, weight=48.0)
    g.diag(384.1, 194.0, 364.5, 179.1, weight=48.0)
    g.hbar(281.1, 410.9, 142.0, weight=48.0)
    g.diag(604.7, 792.0, 692.8, 727.1, weight=56.0)
    g.hbar(537.9, 818.9, 658.0, weight=96.0)
    g.dot(583.4, 556.5, w=48.0, h=62.4, slant=-14.0)
    g.diag(734.5, 639.0, 755.6, 615.0, weight=64.0)
    g.diag(755.6, 615.0, 699.3, 514.8, weight=64.0)
    g.diag(483.2, 492.5, 489.5, 451.4, weight=96.0)
    g.diag(489.5, 451.4, 461.0, 365.5, weight=96.0)
    g.diag(515.7, 467.5, 519.1, 465.0, weight=96.0)
    g.hbar(519.1, 934.0, 495.7, weight=96.0)
    g.diag(934.0, 526.4, 841.1, 432.2, weight=96.0)
    g.diag(521.2, 360.8, 542.7, 338.1, weight=48.0)
    g.vbar(535.2, 174.4, 338.1, weight=48.0)
    g.hbar(558.3, 828.8, 366.8, weight=96.0)
    g.vbar(811.0, 187.4, 379.2, weight=96.0)
    g.hbar(715.0, 793.2, 201.3, weight=96.0)
    g.diag(627.9, 465.6, 665.0, 443.4, weight=96.0)
    g.vbar(661.7, -62.0, 443.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_8aed() -> Glyph:
    """諭 U+8AED —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8AED", advance=1000, unicode=0x8AED, note="諭：自动生成")
    g.diag(272.8, 740.3, 351.0, 690.3, weight=92.0)
    g.vbar(356.6, 596.4, 690.3, weight=92.0)
    g.hbar(71.0, 355.3, 537.9, weight=92.0)
    g.hbar(355.3, 445.6, 542.3, weight=92.0)
    g.diag(185.0, 346.3, 225.6, 414.1, weight=64.0)
    g.hbar(225.6, 311.4, 425.9, weight=64.0)
    g.diag(311.4, 437.6, 368.7, 410.5, weight=64.0)
    g.diag(186.0, 388.5, 221.4, 319.7, weight=64.0)
    g.hbar(221.4, 359.7, 344.1, weight=64.0)
    g.vbar(159.5, 188.7, 214.9, weight=48.0)
    g.vbar(175.8, 68.8, 188.7, weight=48.0)
    g.diag(180.5, 211.6, 181.8, 211.0, weight=84.0)
    g.hbar(181.8, 319.2, 219.0, weight=84.0)
    g.diag(319.2, 227.1, 273.7, 136.0, weight=84.0)
    g.hbar(202.0, 305.4, 101.7, weight=92.0)
    g.diag(305.4, 116.6, 308.3, 118.8, weight=92.0)
    g.diag(548.0, 749.7, 523.3, 627.8, weight=64.0)
    g.diag(523.3, 627.8, 384.4, 372.6, weight=64.0)
    g.diag(597.6, 658.8, 604.8, 621.5, weight=84.0)
    g.diag(604.8, 621.5, 944.0, 451.8, weight=84.0)
    g.hbar(484.1, 696.0, 500.4, weight=56.0)
    g.vbar(384.4, 8.7, 367.1, weight=48.0)
    g.diag(425.8, 336.9, 508.4, 243.9, weight=48.0)
    g.vbar(513.9, 6.3, 243.9, weight=48.0)
    g.hbar(408.5, 519.4, 25.7, weight=48.0)
    g.diag(433.0, 235.9, 442.6, 248.7, weight=64.0)
    g.hbar(442.6, 506.8, 248.1, weight=64.0)
    g.dot(467.5, 155.0, w=64.0, h=82.9, slant=-14.0)
    g.hbar(558.5, 606.5, 320.5, weight=56.0)
    g.vbar(616.4, 129.4, 313.1, weight=56.0)
    g.diag(679.4, 455.1, 773.3, 327.7, weight=92.0)
    g.diag(773.3, 327.7, 717.0, -29.5, weight=92.0)
    g.hbar(566.2, 717.0, -6.0, weight=92.0)
    return g
def g_cjk_unified_ideograph_8aee() -> Glyph:
    """諮 U+8AEE —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8AEE", advance=1000, unicode=0x8AEE, note="諮：自动生成")
    g.dot(319.4, 672.5, w=96.0, h=124.8, slant=-14.0)
    g.hbar(78.0, 413.4, 493.1, weight=84.0)
    g.hbar(216.1, 381.4, 400.1, weight=76.0)
    g.hbar(219.9, 373.9, 294.4, weight=84.0)
    g.diag(172.9, 170.9, 236.8, -1.1, weight=48.0)
    g.diag(224.6, 170.9, 234.0, 164.3, weight=48.0)
    g.hbar(234.0, 329.9, 180.0, weight=48.0)
    g.diag(329.9, 195.6, 367.6, 173.7, weight=48.0)
    g.diag(367.6, 173.7, 346.5, 102.9, weight=48.0)
    g.diag(346.5, 102.9, 323.2, 83.5, weight=48.0)
    g.diag(250.9, 50.6, 257.6, 46.9, weight=96.0)
    g.hbar(257.6, 379.6, 54.4, weight=96.0)
    g.dot(487.6, 552.7, w=96.0, h=88.1, slant=-14.0)
    g.vbar(448.1, 291.1, 342.8, weight=92.0)
    g.diag(445.3, 342.8, 522.4, 455.5, weight=92.0)
    g.diag(638.9, 752.4, 675.7, 721.3, weight=96.0)
    g.diag(675.7, 721.3, 567.5, 485.6, weight=96.0)
    g.hbar(630.4, 841.1, 556.9, weight=96.0)
    g.diag(841.1, 571.8, 743.1, 471.5, weight=96.0)
    g.diag(622.9, 470.5, 657.1, 420.7, weight=48.0)
    g.diag(657.1, 420.7, 494.2, 257.3, weight=48.0)
    g.vbar(668.9, 358.2, 396.3, weight=96.0)
    g.hbar(674.5, 947.0, 311.5, weight=96.0)
    g.diag(471.6, 179.3, 537.4, -27.4, weight=48.0)
    g.hbar(518.6, 604.4, 179.1, weight=48.0)
    g.hbar(604.4, 767.8, 182.9, weight=48.0)
    g.diag(767.8, 187.0, 732.8, 79.7, weight=48.0)
    g.diag(732.8, 79.7, 705.6, 60.9, weight=48.0)
    g.diag(554.3, 27.1, 562.2, 20.0, weight=48.0)
    g.hbar(562.2, 765.7, 23.1, weight=48.0)
    return g
def g_cjk_unified_ideograph_8b00() -> Glyph:
    """謀 U+8B00 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8B00", advance=1000, unicode=0x8B00, note="謀：自动生成")
    g.dot(327.0, 698.4, w=96.0, h=124.8, slant=-14.0)
    g.hbar(73.0, 400.9, 527.5, weight=84.0)
    g.hbar(216.0, 364.6, 433.7, weight=64.0)
    g.hbar(212.3, 367.4, 342.2, weight=64.0)
    g.diag(162.2, 234.9, 191.9, 207.0, weight=48.0)
    g.diag(191.9, 207.0, 232.8, 46.4, weight=48.0)
    g.hbar(215.3, 354.2, 238.1, weight=84.0)
    g.diag(354.2, 245.0, 307.1, 146.7, weight=84.0)
    g.hbar(240.2, 363.7, 111.4, weight=48.0)
    g.hbar(421.3, 808.6, 624.1, weight=84.0)
    g.diag(462.2, 694.7, 501.4, 668.7, weight=96.0)
    g.vbar(510.6, 386.3, 668.7, weight=96.0)
    g.diag(640.5, 771.7, 685.3, 732.5, weight=64.0)
    g.vbar(672.7, 394.7, 732.5, weight=64.0)
    g.diag(539.3, 497.7, 549.1, 512.0, weight=76.0)
    g.hbar(549.1, 622.8, 512.7, weight=76.0)
    g.hbar(536.5, 627.9, 414.5, weight=76.0)
    g.diag(627.9, 426.9, 637.7, 414.2, weight=76.0)
    g.hbar(388.8, 882.9, 299.0, weight=48.0)
    g.vbar(585.2, -56.7, 377.0, weight=96.0)
    g.diag(571.8, 276.7, 331.2, 30.6, weight=48.0)
    g.diag(621.0, 285.1, 688.3, 224.9, weight=48.0)
    g.diag(688.3, 224.9, 947.0, 65.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_8b01() -> Glyph:
    """謁 U+8B01 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8B01", advance=1000, unicode=0x8B01, note="謁：自动生成")
    g.diag(352.5, 762.0, 444.7, 705.0, weight=96.0)
    g.hbar(444.7, 500.7, 702.9, weight=96.0)
    g.hbar(92.5, 428.2, 540.2, weight=96.0)
    g.diag(428.2, 567.5, 463.3, 634.0, weight=96.0)
    g.diag(252.6, 345.2, 295.7, 413.3, weight=84.0)
    g.hbar(295.7, 386.4, 425.7, weight=84.0)
    g.diag(386.4, 438.2, 416.6, 370.2, weight=84.0)
    g.diag(253.9, 379.7, 296.9, 319.8, weight=84.0)
    g.hbar(296.9, 452.6, 315.4, weight=84.0)
    g.diag(229.7, 180.1, 219.0, 163.7, weight=48.0)
    g.vbar(246.7, 9.8, 163.7, weight=48.0)
    g.hbar(234.6, 404.3, 184.7, weight=48.0)
    g.diag(404.3, 197.5, 355.7, 77.1, weight=48.0)
    g.diag(277.8, 28.7, 289.3, 41.2, weight=96.0)
    g.hbar(289.3, 399.8, 55.6, weight=96.0)
    g.diag(563.5, 724.4, 552.2, 710.1, weight=48.0)
    g.vbar(573.4, 492.0, 710.1, weight=48.0)
    g.hbar(566.7, 796.4, 734.3, weight=48.0)
    g.diag(796.4, 752.3, 832.3, 718.0, weight=48.0)
    g.diag(832.3, 718.0, 777.6, 523.5, weight=48.0)
    g.hbar(755.0, 777.6, 526.0, weight=48.0)
    g.diag(602.6, 600.6, 616.6, 619.2, weight=76.0)
    g.hbar(616.6, 775.5, 619.8, weight=76.0)
    g.diag(613.6, 509.9, 625.5, 521.8, weight=76.0)
    g.hbar(625.5, 749.1, 530.4, weight=76.0)
    g.diag(601.6, 481.0, 620.3, 442.9, weight=96.0)
    g.diag(620.3, 442.9, 498.0, 324.6, weight=96.0)
    g.diag(589.7, 371.4, 813.2, 246.9, weight=96.0)
    g.vbar(823.6, -72.0, 246.9, weight=96.0)
    g.diag(834.1, -72.0, 714.9, 91.7, weight=96.0)
    g.diag(657.4, 361.5, 686.7, 323.1, weight=64.0)
    g.diag(686.7, 323.1, 542.4, 215.8, weight=64.0)
    g.hbar(678.3, 687.8, 278.6, weight=92.0)
    g.diag(687.8, 280.3, 765.7, 237.7, weight=92.0)
    g.vbar(769.2, 174.0, 237.7, weight=92.0)
    g.diag(488.8, 307.7, 518.8, 244.7, weight=48.0)
    g.diag(518.8, 244.7, 586.8, 146.4, weight=48.0)
    g.hbar(586.8, 875.0, 131.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_8b04() -> Glyph:
    """謄 U+8B04 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8B04", advance=1000, unicode=0x8B04, note="謄：自动生成")
    g.diag(186.2, 669.0, 59.3, 43.9, weight=96.0)
    g.hbar(206.1, 291.0, 666.4, weight=48.0)
    g.vbar(300.7, 443.7, 680.5, weight=48.0)
    g.vbar(307.4, 84.2, 443.7, weight=48.0)
    g.diag(304.4, 84.2, 211.6, 132.6, weight=48.0)
    g.diag(220.0, 491.2, 227.6, 504.3, weight=96.0)
    g.hbar(227.6, 286.1, 502.8, weight=96.0)
    g.diag(206.9, 341.8, 214.3, 355.4, weight=96.0)
    g.hbar(214.3, 285.1, 355.1, weight=96.0)
    g.hbar(362.5, 462.8, 652.8, weight=96.0)
    g.vbar(471.9, 584.3, 644.4, weight=96.0)
    g.hbar(726.2, 758.9, 711.6, weight=48.0)
    g.diag(726.2, 716.3, 657.6, 609.0, weight=48.0)
    g.diag(468.6, 595.9, 492.5, 543.8, weight=56.0)
    g.hbar(492.5, 673.9, 568.3, weight=56.0)
    g.vbar(673.5, 592.7, 630.7, weight=56.0)
    g.hbar(343.3, 821.4, 475.5, weight=48.0)
    g.diag(542.2, 777.0, 517.5, 603.1, weight=48.0)
    g.diag(517.5, 603.1, 341.9, 247.6, weight=48.0)
    g.diag(634.6, 471.0, 945.7, 306.3, weight=48.0)
    g.dot(566.5, 385.9, w=84.0, h=98.1, slant=-14.0)
    g.hbar(451.1, 727.6, 338.7, weight=48.0)
    g.hbar(490.8, 658.0, 245.1, weight=48.0)
    g.vbar(670.0, 204.8, 258.7, weight=48.0)
    g.diag(487.0, 113.6, 519.8, 158.7, weight=56.0)
    g.hbar(519.8, 663.6, 173.2, weight=56.0)
    g.diag(663.6, 187.7, 700.3, 133.5, weight=56.0)
    g.vbar(469.8, 76.0, 91.5, weight=48.0)
    g.vbar(489.9, -52.7, 76.0, weight=48.0)
    g.hbar(482.8, 741.4, 94.3, weight=48.0)
    g.diag(741.4, 103.2, 672.3, 8.8, weight=48.0)
    g.hbar(523.0, 705.7, -12.7, weight=48.0)
    return g
def g_cjk_unified_ideograph_8b0e() -> Glyph:
    """謎 U+8B0E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8B0E", advance=1000, unicode=0x8B0E, note="謎：自动生成")
    g.dot(320.8, 635.7, w=84.0, h=109.2, slant=-14.0)
    g.hbar(67.0, 366.9, 453.3, weight=84.0)
    g.hbar(185.1, 341.2, 358.6, weight=76.0)
    g.hbar(185.1, 345.0, 263.4, weight=76.0)
    g.diag(141.3, 144.8, 172.7, 117.2, weight=48.0)
    g.diag(172.7, 117.2, 209.8, -17.1, weight=48.0)
    g.hbar(184.1, 187.8, 147.1, weight=48.0)
    g.hbar(187.8, 337.5, 156.4, weight=48.0)
    g.diag(337.5, 166.2, 322.2, 99.1, weight=48.0)
    g.diag(322.2, 99.1, 302.2, 78.2, weight=48.0)
    g.diag(225.1, 22.0, 238.3, 37.6, weight=48.0)
    g.hbar(238.3, 346.9, 45.0, weight=48.0)
    g.dot(576.4, 518.5, w=64.0, h=83.2, slant=-14.0)
    g.diag(813.5, 620.9, 834.9, 588.8, weight=48.0)
    g.diag(834.9, 588.8, 741.1, 488.5, weight=48.0)
    g.hbar(545.0, 843.0, 406.7, weight=48.0)
    g.diag(645.9, 717.1, 675.8, 497.0, weight=48.0)
    g.vbar(679.4, 114.3, 497.0, weight=48.0)
    g.diag(664.0, 366.7, 511.7, 191.5, weight=48.0)
    g.diag(702.1, 323.8, 866.8, 206.7, weight=84.0)
    g.dot(454.5, 490.9, w=84.0, h=85.6, slant=-14.0)
    g.hbar(353.6, 487.2, 363.1, weight=84.0)
    g.diag(487.2, 368.2, 429.6, 255.1, weight=84.0)
    g.diag(429.6, 255.1, 468.4, 144.2, weight=84.0)
    g.diag(468.4, 144.2, 447.9, 130.5, weight=84.0)
    g.hbar(381.2, 943.0, 82.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_8b1b() -> Glyph:
    """講 U+8B1B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8B1B", advance=1000, unicode=0x8B1B, note="講：自动生成")
    g.dot(316.3, 686.4, w=92.0, h=119.6, slant=-14.0)
    g.hbar(74.8, 403.8, 511.9, weight=96.0)
    g.hbar(211.6, 366.5, 403.9, weight=84.0)
    g.hbar(211.6, 366.5, 304.4, weight=76.0)
    g.diag(138.9, 189.7, 216.3, -12.1, weight=48.0)
    g.diag(187.7, 191.6, 192.9, 188.4, weight=48.0)
    g.hbar(192.9, 350.9, 197.9, weight=48.0)
    g.diag(350.9, 207.4, 330.1, 119.9, weight=48.0)
    g.diag(330.1, 119.9, 308.1, 101.7, weight=48.0)
    g.dot(295.7, 63.0, w=96.0, h=124.8, slant=-14.0)
    g.hbar(453.5, 820.6, 637.2, weight=76.0)
    g.hbar(481.2, 789.1, 529.1, weight=64.0)
    g.diag(512.8, 713.7, 549.1, 674.5, weight=96.0)
    g.vbar(556.3, 467.9, 674.5, weight=96.0)
    g.diag(563.4, 467.9, 552.0, 446.9, weight=96.0)
    g.diag(664.8, 772.0, 704.0, 734.7, weight=64.0)
    g.vbar(693.5, 489.0, 734.7, weight=64.0)
    g.diag(683.0, 489.0, 666.7, 470.8, weight=64.0)
    g.hbar(419.1, 888.5, 435.4, weight=64.0)
    g.vbar(467.3, -55.1, 325.5, weight=76.0)
    g.hbar(516.6, 738.3, 334.9, weight=48.0)
    g.diag(738.3, 353.0, 763.1, 209.7, weight=48.0)
    g.vbar(755.4, -58.2, 209.7, weight=48.0)
    g.diag(747.7, -58.2, 664.8, -19.7, weight=48.0)
    g.hbar(552.0, 700.2, 244.7, weight=76.0)
    g.diag(599.8, 414.4, 628.0, 391.2, weight=48.0)
    g.vbar(625.5, 183.1, 391.2, weight=48.0)
    g.diag(623.0, 183.1, 608.4, 162.9, weight=48.0)
    g.hbar(393.2, 940.2, 140.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_8b1d() -> Glyph:
    """謝 U+8B1D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8B1D", advance=1000, unicode=0x8B1D, note="謝：自动生成")
    g.diag(243.4, 712.3, 379.4, 619.1, weight=76.0)
    g.hbar(73.0, 398.5, 529.9, weight=84.0)
    g.hbar(161.0, 293.2, 443.9, weight=84.0)
    g.diag(293.2, 414.5, 323.8, 367.8, weight=84.0)
    g.diag(178.1, 246.3, 275.9, 333.7, weight=84.0)
    g.diag(275.9, 333.7, 348.5, 290.0, weight=84.0)
    g.diag(148.5, 214.9, 194.0, 49.0, weight=76.0)
    g.hbar(166.7, 327.1, 216.4, weight=48.0)
    g.diag(327.1, 227.6, 281.0, 125.8, weight=48.0)
    g.diag(196.4, 77.5, 311.0, 130.2, weight=48.0)
    g.diag(492.3, 757.4, 521.4, 733.1, weight=48.0)
    g.diag(521.4, 733.1, 454.1, 613.4, weight=48.0)
    g.diag(454.1, 613.4, 442.3, 607.5, weight=48.0)
    g.vbar(425.9, 278.2, 605.9, weight=48.0)
    g.hbar(443.3, 465.8, 594.3, weight=48.0)
    g.hbar(465.8, 555.0, 601.1, weight=48.0)
    g.vbar(566.6, 394.2, 612.4, weight=48.0)
    g.vbar(574.5, -24.0, 394.2, weight=48.0)
    g.hbar(461.9, 570.8, -2.1, weight=48.0)
    g.diag(461.3, 471.3, 471.5, 486.1, weight=64.0)
    g.hbar(471.5, 567.0, 485.9, weight=64.0)
    g.diag(462.9, 376.3, 475.3, 393.3, weight=76.0)
    g.hbar(475.3, 560.8, 392.5, weight=76.0)
    g.vbar(406.4, 249.4, 283.0, weight=48.0)
    g.hbar(406.1, 570.8, 281.4, weight=48.0)
    g.diag(609.2, 310.9, 282.6, 4.1, weight=48.0)
    g.hbar(630.3, 865.1, 459.8, weight=96.0)
    g.diag(865.1, 479.5, 856.4, 469.1, weight=96.0)
    g.diag(776.3, 712.3, 809.8, 471.5, weight=84.0)
    g.vbar(806.0, -2.7, 471.5, weight=84.0)
    g.hbar(690.8, 802.2, 20.8, weight=84.0)
    g.hbar(619.5, 690.8, 44.8, weight=84.0)
    g.diag(646.6, 318.1, 715.6, 276.4, weight=56.0)
    g.diag(715.6, 276.4, 730.3, 239.2, weight=56.0)
    return g
def g_cjk_unified_ideograph_8b39() -> Glyph:
    """謹 U+8B39 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8B39", advance=1000, unicode=0x8B39, note="謹：自动生成")
    g.dot(327.5, 652.6, w=96.0, h=124.8, slant=-14.0)
    g.hbar(73.0, 429.6, 468.2, weight=96.0)
    g.hbar(192.5, 360.0, 356.2, weight=76.0)
    g.hbar(195.3, 351.5, 256.5, weight=76.0)
    g.diag(149.2, 140.8, 214.1, -40.8, weight=48.0)
    g.hbar(189.7, 193.5, 141.3, weight=48.0)
    g.hbar(193.5, 343.3, 149.9, weight=48.0)
    g.diag(343.3, 159.1, 321.4, 80.6, weight=48.0)
    g.diag(321.4, 80.6, 298.8, 63.6, weight=48.0)
    g.diag(230.1, 4.4, 242.9, 22.9, weight=96.0)
    g.hbar(242.9, 349.6, 31.5, weight=96.0)
    g.hbar(439.0, 900.0, 589.1, weight=84.0)
    g.diag(515.2, 694.0, 554.5, 670.5, weight=96.0)
    g.diag(554.5, 670.5, 580.1, 463.5, weight=96.0)
    g.diag(703.4, 760.8, 735.4, 721.3, weight=92.0)
    g.diag(735.4, 721.3, 694.0, 536.9, weight=92.0)
    g.diag(694.0, 536.9, 678.0, 524.6, weight=92.0)
    g.hbar(590.5, 716.5, 483.3, weight=56.0)
    g.diag(455.0, 390.1, 485.1, 370.3, weight=96.0)
    g.vbar(505.3, 244.3, 370.3, weight=96.0)
    g.hbar(515.2, 613.0, 379.1, weight=48.0)
    g.hbar(613.0, 817.2, 405.7, weight=48.0)
    g.diag(817.2, 420.7, 779.6, 346.8, weight=48.0)
    g.hbar(754.2, 779.6, 342.6, weight=48.0)
    g.hbar(538.7, 632.7, 286.4, weight=48.0)
    g.hbar(632.7, 802.2, 294.9, weight=48.0)
    g.hbar(505.8, 780.5, 185.9, weight=76.0)
    g.hbar(497.3, 773.0, 90.0, weight=76.0)
    g.vbar(611.7, 377.3, 466.3, weight=48.0)
    g.vbar(635.1, 38.7, 377.3, weight=48.0)
    g.diag(644.8, 38.7, 621.5, 10.0, weight=48.0)
    g.hbar(370.3, 932.0, -20.1, weight=84.0)
    return g
def g_cjk_unified_ideograph_8b58() -> Glyph:
    """識 U+8B58 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8B58", advance=1000, unicode=0x8B58, note="識：自动生成")
    g.dot(308.9, 681.1, w=84.0, h=109.2, slant=-14.0)
    g.hbar(67.0, 373.8, 499.9, weight=76.0)
    g.hbar(170.5, 323.0, 401.6, weight=76.0)
    g.hbar(177.1, 319.3, 305.6, weight=76.0)
    g.diag(130.1, 193.1, 162.1, 166.7, weight=84.0)
    g.diag(162.1, 166.7, 201.6, 37.8, weight=84.0)
    g.diag(185.6, 177.1, 199.6, 193.9, weight=76.0)
    g.hbar(199.6, 327.1, 204.2, weight=76.0)
    g.diag(327.1, 214.5, 308.0, 132.9, weight=76.0)
    g.diag(308.0, 132.9, 285.4, 115.9, weight=76.0)
    g.dot(276.9, 79.7, w=84.0, h=109.2, slant=-14.0)
    g.dot(495.7, 682.1, w=84.0, h=94.7, slant=-14.0)
    g.hbar(415.3, 590.3, 563.9, weight=84.0)
    g.dot(433.1, 462.3, w=84.0, h=66.8, slant=-14.0)
    g.diag(532.0, 548.9, 554.6, 522.5, weight=84.0)
    g.diag(554.6, 522.5, 529.3, 440.3, weight=84.0)
    g.diag(529.3, 440.3, 515.0, 418.0, weight=84.0)
    g.hbar(362.5, 848.2, 411.0, weight=84.0)
    g.diag(403.0, 300.4, 432.2, 62.2, weight=48.0)
    g.diag(446.3, 290.0, 450.9, 286.6, weight=48.0)
    g.diag(450.9, 286.6, 556.4, 213.2, weight=48.0)
    g.vbar(567.3, 30.2, 213.2, weight=48.0)
    g.dot(488.2, 190.7, w=76.0, h=79.7, slant=-14.0)
    g.diag(449.1, 83.0, 461.8, 94.6, weight=76.0)
    g.hbar(461.8, 537.6, 98.2, weight=76.0)
    g.diag(594.1, 751.2, 695.4, 478.3, weight=84.0)
    g.diag(695.4, 478.3, 893.7, -78.0, weight=84.0)
    g.diag(893.7, -78.0, 948.0, 117.8, weight=84.0)
    g.diag(814.3, 373.8, 841.0, 333.2, weight=84.0)
    g.diag(841.0, 333.2, 635.5, 126.2, weight=84.0)
    g.diag(729.6, 670.3, 836.9, 579.9, weight=64.0)
    return g
def g_cjk_unified_ideograph_8b5c() -> Glyph:
    """譜 U+8B5C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8B5C", advance=1000, unicode=0x8B5C, note="譜：自动生成")
    g.dot(301.9, 714.8, w=96.0, h=124.8, slant=-14.0)
    g.hbar(78.0, 394.2, 535.4, weight=96.0)
    g.hbar(196.0, 358.4, 428.1, weight=76.0)
    g.hbar(193.1, 357.5, 325.1, weight=84.0)
    g.diag(139.9, 219.2, 209.5, 35.5, weight=48.0)
    g.hbar(188.2, 350.0, 225.5, weight=48.0)
    g.diag(350.0, 235.6, 323.9, 143.0, weight=48.0)
    g.diag(323.9, 143.0, 301.4, 126.4, weight=48.0)
    g.dot(289.8, 87.7, w=96.0, h=124.8, slant=-14.0)
    g.dot(545.0, 704.2, w=96.0, h=114.2, slant=-14.0)
    g.diag(745.2, 784.9, 766.5, 754.0, weight=96.0)
    g.diag(766.5, 754.0, 692.0, 657.3, weight=96.0)
    g.hbar(477.4, 810.0, 601.7, weight=96.0)
    g.diag(541.2, 555.7, 588.8, 508.1, weight=76.0)
    g.diag(588.8, 508.1, 557.6, 353.6, weight=76.0)
    g.diag(651.4, 576.0, 684.3, 548.6, weight=92.0)
    g.diag(684.3, 548.6, 660.3, 370.4, weight=92.0)
    g.diag(660.3, 370.4, 661.1, 371.0, weight=92.0)
    g.dot(452.2, 444.5, w=64.0, h=83.2, slant=-14.0)
    g.diag(807.1, 537.4, 822.6, 510.3, weight=56.0)
    g.diag(822.6, 510.3, 748.1, 437.8, weight=56.0)
    g.hbar(406.8, 927.0, 338.2, weight=96.0)
    g.vbar(512.2, -16.7, 253.1, weight=48.0)
    g.diag(544.1, 243.4, 552.7, 238.1, weight=48.0)
    g.hbar(552.7, 719.8, 208.4, weight=48.0)
    g.diag(719.8, 178.6, 758.7, -39.9, weight=48.0)
    g.diag(552.8, 118.7, 562.9, 132.2, weight=84.0)
    g.hbar(562.9, 673.7, 133.6, weight=84.0)
    g.hbar(545.0, 703.6, 28.7, weight=84.0)
    return g
def g_cjk_unified_ideograph_8b77() -> Glyph:
    """護 U+8B77 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8B77", advance=1000, unicode=0x8B77, note="護：自动生成")
    g.dot(312.4, 680.8, w=96.0, h=124.8, slant=-14.0)
    g.hbar(73.0, 393.2, 495.7, weight=76.0)
    g.hbar(214.1, 354.2, 390.8, weight=76.0)
    g.hbar(189.9, 352.3, 288.3, weight=76.0)
    g.diag(151.0, 173.6, 221.5, -6.4, weight=48.0)
    g.hbar(195.5, 198.6, 171.3, weight=48.0)
    g.hbar(198.6, 348.0, 180.1, weight=48.0)
    g.diag(348.0, 189.2, 328.2, 101.3, weight=48.0)
    g.diag(328.2, 101.3, 306.9, 85.5, weight=48.0)
    g.diag(230.8, 31.7, 243.7, 47.0, weight=96.0)
    g.hbar(243.7, 356.1, 55.6, weight=96.0)
    g.diag(511.0, 718.4, 548.2, 695.2, weight=92.0)
    g.diag(548.2, 695.2, 574.1, 595.0, weight=92.0)
    g.hbar(414.5, 602.0, 646.0, weight=76.0)
    g.diag(671.6, 769.4, 704.7, 739.2, weight=84.0)
    g.diag(704.7, 739.2, 665.1, 606.1, weight=84.0)
    g.dot(783.4, 667.8, w=96.0, h=124.8, slant=-14.0)
    g.hbar(523.6, 538.9, 544.4, weight=48.0)
    g.diag(523.6, 541.1, 399.7, 395.4, weight=48.0)
    g.diag(490.6, 447.4, 480.7, 402.7, weight=48.0)
    g.vbar(486.6, 248.8, 402.7, weight=48.0)
    g.dot(651.2, 568.1, w=96.0, h=63.2, slant=-14.0)
    g.hbar(562.1, 792.2, 527.2, weight=48.0)
    g.hbar(570.4, 753.2, 438.6, weight=48.0)
    g.hbar(565.8, 757.0, 374.1, weight=48.0)
    g.diag(637.2, 493.8, 659.5, 470.6, weight=96.0)
    g.vbar(659.5, 332.3, 470.6, weight=96.0)
    g.diag(659.5, 332.3, 647.5, 317.5, weight=96.0)
    g.hbar(514.7, 836.8, 290.1, weight=56.0)
    g.diag(511.0, 195.9, 588.8, 124.9, weight=96.0)
    g.diag(588.8, 124.9, 375.5, -36.1, weight=96.0)
    g.hbar(473.0, 937.0, 54.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_8c5a() -> Glyph:
    """豚 U+8C5A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8C5A", advance=1000, unicode=0x8C5A, note="豚：自动生成")
    g.diag(171.5, 642.1, 58.0, 34.6, weight=84.0)
    g.hbar(189.7, 288.5, 638.1, weight=48.0)
    g.vbar(299.7, 442.8, 647.2, weight=48.0)
    g.vbar(307.1, 63.5, 442.8, weight=48.0)
    g.hbar(206.3, 303.2, 82.8, weight=48.0)
    g.diag(208.2, 452.9, 216.6, 467.3, weight=96.0)
    g.hbar(216.6, 283.5, 469.7, weight=96.0)
    g.diag(193.0, 301.7, 211.0, 322.9, weight=96.0)
    g.hbar(211.0, 285.0, 323.3, weight=96.0)
    g.diag(479.4, 625.3, 471.9, 629.7, weight=96.0)
    g.hbar(471.9, 734.0, 655.4, weight=96.0)
    g.diag(514.5, 615.9, 542.9, 574.4, weight=48.0)
    g.diag(542.9, 574.4, 341.5, 428.8, weight=48.0)
    g.diag(477.7, 481.9, 563.9, 132.1, weight=48.0)
    g.diag(563.9, 132.1, 476.4, 52.6, weight=48.0)
    g.diag(515.3, 444.4, 520.1, 405.1, weight=48.0)
    g.diag(520.1, 405.1, 342.8, 301.3, weight=48.0)
    g.diag(581.4, 374.6, 340.2, 136.3, weight=48.0)
    g.hbar(735.9, 774.0, 490.0, weight=96.0)
    g.diag(735.9, 496.7, 629.4, 398.7, weight=96.0)
    g.vbar(629.4, 391.1, 398.7, weight=96.0)
    g.vbar(638.9, 335.7, 360.7, weight=96.0)
    g.diag(638.9, 335.7, 947.0, 162.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_8c6a() -> Glyph:
    """豪 U+8C6A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8C6A", advance=1000, unicode=0x8C6A, note="豪：自动生成")
    g.hbar(375.3, 453.3, 782.2, weight=48.0)
    g.diag(453.3, 767.4, 495.9, 709.1, weight=48.0)
    g.hbar(220.3, 688.2, 684.0, weight=48.0)
    g.dot(340.8, 535.5, w=96.0, h=124.8, slant=-14.0)
    g.hbar(344.6, 594.1, 606.7, weight=48.0)
    g.diag(594.1, 620.2, 530.3, 544.7, weight=48.0)
    g.hbar(376.0, 563.2, 510.0, weight=48.0)
    g.vbar(564.3, 529.3, 551.3, weight=48.0)
    g.diag(174.9, 426.9, 122.5, 305.4, weight=96.0)
    g.diag(122.5, 305.4, 150.2, 229.4, weight=96.0)
    g.hbar(183.4, 806.1, 434.0, weight=48.0)
    g.diag(806.1, 467.3, 689.2, 366.5, weight=48.0)
    g.diag(264.8, 388.4, 331.2, 333.0, weight=48.0)
    g.hbar(331.2, 513.0, 353.3, weight=48.0)
    g.hbar(513.0, 583.6, 362.7, weight=48.0)
    g.diag(375.1, 321.4, 369.8, 293.5, weight=48.0)
    g.diag(369.8, 293.5, 177.8, 202.7, weight=48.0)
    g.diag(356.9, 269.0, 411.4, 55.9, weight=48.0)
    g.hbar(306.2, 411.4, 37.6, weight=48.0)
    g.hbar(397.1, 421.7, 210.6, weight=64.0)
    g.diag(397.1, 210.6, 191.6, 101.0, weight=64.0)
    g.diag(448.3, 179.0, 430.6, 120.8, weight=64.0)
    g.diag(430.6, 120.8, 147.2, -25.4, weight=64.0)
    g.diag(586.6, 349.7, 620.4, 299.4, weight=96.0)
    g.diag(620.4, 299.4, 497.0, 216.2, weight=96.0)
    g.hbar(486.8, 497.0, 217.3, weight=96.0)
    g.vbar(490.7, 179.6, 205.6, weight=96.0)
    g.hbar(492.5, 907.4, 110.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_8c8c() -> Glyph:
    """貌 U+8C8C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8C8C", advance=1000, unicode=0x8C8C, note="貌：自动生成")
    g.diag(396.8, 637.5, 328.5, 724.5, weight=96.0)
    g.diag(328.5, 724.5, 134.6, 594.3, weight=96.0)
    g.dot(156.2, 524.7, w=84.0, h=109.2, slant=-14.0)
    g.dot(249.2, 571.6, w=84.0, h=98.2, slant=-14.0)
    g.hbar(324.2, 435.4, 538.9, weight=64.0)
    g.diag(324.2, 520.6, 70.2, 354.3, weight=64.0)
    g.diag(226.7, 424.2, 264.2, 123.4, weight=48.0)
    g.diag(264.2, 123.4, 183.9, 43.9, weight=48.0)
    g.vbar(243.5, 353.2, 394.3, weight=48.0)
    g.diag(244.9, 353.2, 70.2, 231.4, weight=48.0)
    g.diag(305.3, 318.2, 63.0, 69.5, weight=48.0)
    g.diag(587.5, 760.0, 627.5, 727.9, weight=96.0)
    g.diag(627.5, 727.9, 538.6, 559.7, weight=96.0)
    g.diag(538.6, 559.7, 524.0, 546.9, weight=96.0)
    g.diag(461.9, 530.2, 451.6, 513.2, weight=48.0)
    g.vbar(473.0, 290.4, 513.2, weight=48.0)
    g.vbar(492.9, 281.6, 290.4, weight=48.0)
    g.hbar(467.0, 787.1, 538.7, weight=48.0)
    g.vbar(753.3, 333.8, 556.9, weight=48.0)
    g.hbar(687.7, 719.6, 333.6, weight=48.0)
    g.diag(501.5, 429.1, 505.9, 425.2, weight=84.0)
    g.hbar(505.9, 713.9, 425.6, weight=84.0)
    g.hbar(510.4, 687.3, 327.1, weight=48.0)
    g.diag(498.4, 267.2, 536.2, 228.1, weight=48.0)
    g.diag(536.2, 228.1, 407.3, 22.0, weight=48.0)
    g.hbar(322.4, 407.3, 19.4, weight=48.0)
    g.diag(605.3, 313.2, 687.8, 164.5, weight=48.0)
    g.diag(687.8, 164.5, 936.1, -38.8, weight=48.0)
    g.vbar(939.0, -38.8, 153.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_8ca7() -> Glyph:
    """貧 U+8CA7 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8CA7", advance=1000, unicode=0x8CA7, note="貧：自动生成")
    g.diag(298.2, 630.6, 316.6, 675.8, weight=96.0)
    g.diag(316.6, 675.8, 127.3, 515.9, weight=96.0)
    g.diag(488.7, 782.0, 872.7, 567.8, weight=64.0)
    g.hbar(279.1, 398.5, 608.0, weight=48.0)
    g.hbar(398.5, 575.7, 619.9, weight=48.0)
    g.diag(575.7, 632.3, 505.6, 456.2, weight=48.0)
    g.diag(505.6, 456.2, 397.4, 522.7, weight=48.0)
    g.diag(380.2, 580.1, 395.7, 548.5, weight=96.0)
    g.diag(395.7, 548.5, 255.9, 397.4, weight=96.0)
    g.diag(316.8, 379.1, 288.3, 362.6, weight=48.0)
    g.vbar(302.9, 111.8, 362.6, weight=48.0)
    g.hbar(324.7, 558.8, 389.5, weight=48.0)
    g.diag(558.8, 407.7, 601.2, 371.7, weight=48.0)
    g.diag(601.2, 371.7, 569.6, 129.0, weight=48.0)
    g.hbar(336.1, 502.8, 286.6, weight=48.0)
    g.hbar(333.3, 483.1, 214.4, weight=56.0)
    g.diag(483.1, 229.4, 519.2, 176.7, weight=56.0)
    g.hbar(332.0, 568.6, 133.0, weight=56.0)
    g.diag(397.7, 113.9, 194.3, -72.0, weight=64.0)
    g.diag(556.7, 90.5, 670.8, -61.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_8caa() -> Glyph:
    """貪 U+8CAA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8CAA", advance=1000, unicode=0x8CAA, note="貪：自动生成")
    g.hbar(457.8, 500.8, 759.3, weight=96.0)
    g.diag(500.8, 767.7, 109.0, 424.0, weight=96.0)
    g.diag(469.4, 731.6, 542.3, 661.0, weight=64.0)
    g.hbar(542.3, 891.0, 590.6, weight=64.0)
    g.diag(402.4, 640.2, 488.1, 599.9, weight=48.0)
    g.diag(488.1, 599.9, 510.8, 555.2, weight=48.0)
    g.hbar(293.4, 413.0, 517.5, weight=48.0)
    g.hbar(413.0, 593.1, 524.1, weight=48.0)
    g.diag(593.1, 536.8, 467.5, 398.3, weight=48.0)
    g.diag(327.0, 375.0, 301.3, 356.3, weight=48.0)
    g.vbar(313.6, 103.5, 356.3, weight=48.0)
    g.hbar(337.7, 522.8, 377.8, weight=48.0)
    g.hbar(522.8, 631.2, 387.3, weight=48.0)
    g.vbar(610.7, 121.6, 385.3, weight=48.0)
    g.hbar(345.0, 502.9, 295.1, weight=56.0)
    g.vbar(506.8, 246.0, 309.9, weight=56.0)
    g.hbar(341.4, 505.5, 210.7, weight=56.0)
    g.diag(505.5, 225.3, 529.6, 163.6, weight=56.0)
    g.diag(341.9, 114.1, 359.3, 128.3, weight=64.0)
    g.hbar(359.3, 587.2, 131.3, weight=64.0)
    g.diag(426.3, 107.3, 197.9, -72.0, weight=64.0)
    g.diag(518.9, 101.9, 660.9, -66.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_8cab() -> Glyph:
    """貫 U+8CAB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8CAB", advance=1000, unicode=0x8CAB, note="貫：自动生成")
    g.diag(329.0, 746.2, 357.5, 712.2, weight=64.0)
    g.vbar(330.5, 491.9, 712.2, weight=64.0)
    g.hbar(303.5, 564.8, 509.9, weight=64.0)
    g.diag(564.8, 527.9, 581.5, 507.6, weight=64.0)
    g.hbar(377.5, 682.8, 728.6, weight=48.0)
    g.vbar(649.9, 508.1, 756.6, weight=48.0)
    g.hbar(601.1, 617.0, 506.0, weight=48.0)
    g.diag(478.1, 712.6, 500.5, 691.2, weight=96.0)
    g.diag(500.5, 691.2, 472.5, 557.0, weight=96.0)
    g.diag(472.5, 557.0, 456.7, 543.0, weight=96.0)
    g.hbar(103.5, 896.5, 601.3, weight=48.0)
    g.vbar(332.7, 110.6, 414.4, weight=48.0)
    g.diag(375.6, 377.1, 383.3, 389.6, weight=48.0)
    g.hbar(383.3, 599.1, 408.9, weight=48.0)
    g.diag(599.1, 428.3, 639.7, 391.9, weight=48.0)
    g.vbar(632.5, 113.4, 391.9, weight=48.0)
    g.hbar(372.8, 542.4, 305.4, weight=56.0)
    g.diag(370.9, 210.3, 384.4, 222.7, weight=64.0)
    g.hbar(384.4, 546.1, 229.6, weight=64.0)
    g.hbar(363.5, 575.2, 138.2, weight=64.0)
    g.diag(575.2, 155.5, 593.7, 141.4, weight=64.0)
    g.hbar(411.1, 444.6, 56.9, weight=64.0)
    g.diag(411.1, 55.2, 217.2, -72.0, weight=64.0)
    g.diag(555.4, 85.5, 691.5, -67.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_8cbc() -> Glyph:
    """貼 U+8CBC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8CBC", advance=1000, unicode=0x8CBC, note="貼：自动生成")
    g.vbar(159.4, 189.6, 661.5, weight=96.0)
    g.hbar(180.7, 348.7, 665.8, weight=48.0)
    g.vbar(365.9, 517.8, 687.6, weight=48.0)
    g.vbar(387.4, 170.3, 517.8, weight=48.0)
    g.diag(200.7, 491.1, 215.0, 508.2, weight=96.0)
    g.hbar(215.0, 354.9, 513.5, weight=96.0)
    g.vbar(204.4, 359.1, 376.8, weight=96.0)
    g.hbar(207.1, 357.9, 383.5, weight=96.0)
    g.hbar(188.9, 355.6, 227.3, weight=84.0)
    g.hbar(235.2, 294.4, 119.9, weight=92.0)
    g.diag(235.2, 119.1, 58.0, -58.2, weight=92.0)
    g.diag(293.1, 120.9, 406.7, 44.8, weight=96.0)
    g.diag(406.7, 44.8, 429.2, -1.4, weight=96.0)
    g.diag(649.1, 773.2, 706.0, 726.6, weight=96.0)
    g.vbar(700.1, 282.9, 726.6, weight=96.0)
    g.diag(694.2, 282.9, 670.6, 254.0, weight=96.0)
    g.diag(738.2, 493.2, 747.8, 502.9, weight=96.0)
    g.hbar(747.8, 942.0, 521.1, weight=96.0)
    g.diag(556.0, 230.0, 542.2, 203.1, weight=48.0)
    g.vbar(573.1, -38.0, 203.1, weight=48.0)
    g.hbar(557.0, 856.9, 235.3, weight=48.0)
    g.diag(856.9, 256.3, 891.0, 213.6, weight=48.0)
    g.diag(891.0, 213.6, 809.0, 35.0, weight=48.0)
    g.hbar(607.6, 887.3, -9.7, weight=48.0)
    return g
def g_cjk_unified_ideograph_8cc2() -> Glyph:
    """賂 U+8CC2 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8CC2", advance=1000, unicode=0x8CC2, note="賂：自动生成")
    g.vbar(165.0, 513.2, 612.3, weight=48.0)
    g.vbar(168.2, 243.1, 513.2, weight=48.0)
    g.hbar(175.7, 312.0, 618.8, weight=48.0)
    g.vbar(326.1, 500.7, 633.2, weight=48.0)
    g.vbar(340.2, 261.0, 500.7, weight=48.0)
    g.diag(340.2, 261.0, 378.5, 215.2, weight=48.0)
    g.diag(196.8, 466.2, 209.5, 481.3, weight=76.0)
    g.hbar(209.5, 321.4, 483.0, weight=76.0)
    g.diag(195.8, 361.9, 213.2, 379.3, weight=76.0)
    g.hbar(213.2, 319.8, 380.4, weight=76.0)
    g.diag(188.1, 254.7, 207.3, 273.9, weight=84.0)
    g.hbar(207.3, 304.0, 270.9, weight=84.0)
    g.diag(193.6, 213.0, 216.6, 181.5, weight=92.0)
    g.diag(216.6, 181.5, 58.0, 33.7, weight=92.0)
    g.diag(315.4, 195.7, 363.3, 109.3, weight=84.0)
    g.hbar(363.3, 445.6, 93.4, weight=84.0)
    g.diag(571.9, 754.3, 556.6, 647.6, weight=48.0)
    g.diag(556.6, 647.6, 433.1, 427.9, weight=48.0)
    g.diag(560.5, 575.7, 611.2, 480.0, weight=48.0)
    g.diag(611.2, 480.0, 362.4, 214.9, weight=48.0)
    g.diag(500.1, 477.7, 947.0, 266.2, weight=96.0)
    g.diag(480.0, 165.6, 467.6, 144.7, weight=48.0)
    g.vbar(494.3, -3.3, 144.7, weight=48.0)
    g.hbar(484.0, 696.6, 168.8, weight=48.0)
    g.diag(696.6, 182.9, 731.3, 144.8, weight=48.0)
    g.diag(731.3, 144.8, 672.5, 45.7, weight=48.0)
    g.hbar(509.5, 741.3, 19.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_8cca() -> Glyph:
    """賊 U+8CCA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8CCA", advance=1000, unicode=0x8CCA, note="賊：自动生成")
    g.diag(181.9, 599.0, 103.8, 426.5, weight=48.0)
    g.diag(103.8, 426.5, 182.3, 209.6, weight=48.0)
    g.diag(189.8, 588.2, 328.9, 459.3, weight=48.0)
    g.vbar(334.3, 154.4, 459.3, weight=48.0)
    g.dot(270.0, 465.0, w=96.0, h=124.8, slant=-14.0)
    g.diag(211.2, 342.4, 234.7, 360.3, weight=84.0)
    g.hbar(234.7, 338.5, 358.5, weight=84.0)
    g.dot(261.4, 237.5, w=96.0, h=124.8, slant=-14.0)
    g.diag(199.1, 172.9, 220.7, 142.5, weight=96.0)
    g.diag(220.7, 142.5, 58.0, -9.2, weight=96.0)
    g.diag(330.3, 166.3, 379.2, 84.1, weight=96.0)
    g.hbar(379.2, 471.9, 72.4, weight=96.0)
    g.diag(471.7, 433.1, 480.6, 452.5, weight=96.0)
    g.hbar(480.6, 772.4, 484.9, weight=96.0)
    g.diag(772.4, 517.3, 818.3, 578.7, weight=96.0)
    g.hbar(408.9, 639.6, 284.6, weight=96.0)
    g.vbar(527.1, 99.4, 418.2, weight=96.0)
    g.hbar(553.9, 567.4, 101.0, weight=96.0)
    g.diag(542.2, 741.2, 667.9, 464.1, weight=96.0)
    g.diag(667.9, 464.1, 892.8, -70.4, weight=96.0)
    g.diag(892.8, -70.4, 942.0, 129.3, weight=96.0)
    g.diag(759.8, 488.7, 812.2, 351.5, weight=64.0)
    g.diag(812.2, 351.5, 531.8, 128.7, weight=64.0)
    g.hbar(642.4, 791.7, 674.7, weight=84.0)
    g.diag(791.7, 655.7, 813.4, 551.3, weight=84.0)
    return g
def g_cjk_unified_ideograph_8cd3() -> Glyph:
    """賓 U+8CD3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8CD3", advance=1000, unicode=0x8CD3, note="賓：自动生成")
    g.diag(516.7, 822.0, 596.7, 779.5, weight=48.0)
    g.diag(596.7, 779.5, 619.9, 717.4, weight=48.0)
    g.diag(335.0, 661.8, 323.6, 671.3, weight=56.0)
    g.diag(323.6, 671.3, 267.7, 531.5, weight=56.0)
    g.hbar(335.2, 900.7, 673.3, weight=56.0)
    g.diag(900.7, 705.6, 753.3, 564.6, weight=56.0)
    g.hbar(375.2, 598.9, 586.8, weight=56.0)
    g.diag(598.9, 620.1, 638.1, 677.7, weight=56.0)
    g.diag(503.6, 574.8, 532.0, 549.8, weight=48.0)
    g.vbar(527.7, 433.1, 549.8, weight=48.0)
    g.diag(389.4, 569.9, 317.1, 392.2, weight=56.0)
    g.diag(766.3, 580.4, 117.5, 171.8, weight=56.0)
    g.diag(442.9, 379.5, 450.1, 375.6, weight=56.0)
    g.vbar(455.3, 95.2, 375.6, weight=56.0)
    g.diag(506.9, 374.1, 501.4, 376.7, weight=48.0)
    g.hbar(501.4, 732.3, 390.5, weight=48.0)
    g.diag(732.3, 404.4, 763.1, 202.8, weight=48.0)
    g.diag(763.1, 202.8, 718.2, 114.9, weight=48.0)
    g.hbar(483.9, 627.2, 304.0, weight=56.0)
    g.diag(627.2, 319.5, 657.8, 255.7, weight=56.0)
    g.hbar(482.7, 620.9, 225.1, weight=56.0)
    g.diag(620.9, 237.6, 665.0, 291.7, weight=56.0)
    g.hbar(479.2, 727.0, 117.3, weight=56.0)
    g.hbar(536.8, 557.2, 40.8, weight=56.0)
    g.diag(536.8, 40.3, 321.1, -92.0, weight=56.0)
    g.diag(695.3, 107.9, 813.1, -85.1, weight=56.0)
    return g
def g_cjk_unified_ideograph_8cdc() -> Glyph:
    """賜 U+8CDC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8CDC", advance=1000, unicode=0x8CDC, note="賜：自动生成")
    g.vbar(171.1, 637.0, 651.4, weight=96.0)
    g.vbar(176.3, 244.0, 637.0, weight=96.0)
    g.hbar(197.1, 316.4, 653.5, weight=48.0)
    g.vbar(331.4, 510.8, 677.5, weight=48.0)
    g.vbar(338.1, 184.0, 510.8, weight=48.0)
    g.diag(211.3, 505.9, 218.8, 522.5, weight=84.0)
    g.hbar(218.8, 329.7, 524.5, weight=84.0)
    g.diag(205.2, 387.1, 225.0, 405.8, weight=96.0)
    g.hbar(225.0, 322.6, 406.4, weight=96.0)
    g.diag(205.2, 260.2, 221.5, 278.5, weight=76.0)
    g.hbar(221.5, 320.3, 283.2, weight=76.0)
    g.hbar(227.0, 275.2, 175.5, weight=84.0)
    g.diag(227.0, 172.5, 58.0, 3.4, weight=84.0)
    g.dot(363.3, 140.7, w=96.0, h=123.8, slant=-14.0)
    g.vbar(535.6, 712.1, 728.2, weight=48.0)
    g.vbar(548.2, 452.1, 712.1, weight=48.0)
    g.hbar(546.6, 788.8, 727.7, weight=48.0)
    g.vbar(752.4, 479.3, 737.8, weight=48.0)
    g.diag(583.9, 591.2, 597.7, 611.9, weight=96.0)
    g.hbar(597.7, 715.8, 609.1, weight=96.0)
    g.hbar(580.0, 714.9, 478.4, weight=48.0)
    g.diag(566.7, 446.0, 592.9, 407.4, weight=84.0)
    g.diag(592.9, 407.4, 382.3, 256.7, weight=84.0)
    g.diag(541.3, 325.2, 816.0, 197.5, weight=96.0)
    g.diag(816.0, 197.5, 773.3, -72.0, weight=96.0)
    g.diag(773.3, -72.0, 620.5, 43.7, weight=96.0)
    g.diag(580.7, 311.2, 606.3, 270.1, weight=48.0)
    g.diag(606.3, 270.1, 398.3, 106.3, weight=48.0)
    g.diag(718.9, 320.1, 762.4, 268.8, weight=96.0)
    g.diag(762.4, 268.8, 495.5, -12.4, weight=96.0)
    g.diag(495.5, -12.4, 392.8, 42.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_8ce0() -> Glyph:
    """賠 U+8CE0 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8CE0", advance=1000, unicode=0x8CE0, note="賠：自动生成")
    g.vbar(159.7, 486.9, 595.6, weight=48.0)
    g.vbar(163.0, 219.9, 486.9, weight=48.0)
    g.hbar(180.4, 183.0, 589.6, weight=96.0)
    g.diag(183.0, 589.1, 306.3, 453.1, weight=96.0)
    g.vbar(309.2, 157.2, 453.1, weight=96.0)
    g.diag(184.2, 452.5, 195.3, 469.1, weight=64.0)
    g.hbar(195.3, 309.3, 472.0, weight=64.0)
    g.diag(186.1, 352.9, 198.7, 370.0, weight=84.0)
    g.hbar(198.7, 300.3, 369.3, weight=84.0)
    g.diag(180.4, 234.1, 194.8, 249.6, weight=64.0)
    g.hbar(194.8, 302.4, 251.1, weight=64.0)
    g.hbar(212.0, 272.1, 149.1, weight=64.0)
    g.diag(212.0, 158.4, 58.0, 6.5, weight=64.0)
    g.dot(338.1, 92.5, w=96.0, h=124.8, slant=-14.0)
    g.diag(591.3, 741.0, 669.1, 689.8, weight=96.0)
    g.diag(669.1, 689.8, 704.7, 608.8, weight=96.0)
    g.hbar(485.6, 739.0, 544.6, weight=96.0)
    g.diag(739.0, 578.3, 759.4, 548.3, weight=96.0)
    g.dot(536.9, 428.5, w=96.0, h=124.8, slant=-14.0)
    g.diag(708.0, 543.6, 739.4, 505.8, weight=96.0)
    g.diag(739.4, 505.8, 646.4, 356.7, weight=96.0)
    g.hbar(371.6, 932.0, 326.4, weight=96.0)
    g.vbar(502.4, 166.3, 185.9, weight=48.0)
    g.vbar(525.6, -4.9, 166.3, weight=48.0)
    g.hbar(513.2, 797.9, 187.3, weight=48.0)
    g.diag(797.9, 198.3, 713.4, 62.3, weight=48.0)
    g.diag(556.4, 11.2, 576.5, 29.5, weight=48.0)
    g.hbar(576.5, 753.6, 36.9, weight=48.0)
    g.vbar(753.6, 44.2, 74.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_8ce6() -> Glyph:
    """賦 U+8CE6 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8CE6", advance=1000, unicode=0x8CE6, note="賦：自动生成")
    g.vbar(160.8, 199.6, 615.0, weight=96.0)
    g.hbar(188.7, 340.0, 609.7, weight=96.0)
    g.vbar(331.8, 230.5, 614.8, weight=96.0)
    g.diag(323.5, 230.5, 302.0, 210.1, weight=96.0)
    g.diag(197.6, 470.9, 217.6, 489.7, weight=84.0)
    g.hbar(217.6, 297.7, 490.8, weight=84.0)
    g.diag(197.6, 359.0, 208.5, 373.6, weight=96.0)
    g.hbar(208.5, 294.0, 374.8, weight=96.0)
    g.diag(192.0, 222.1, 209.8, 240.6, weight=64.0)
    g.hbar(209.8, 298.0, 237.3, weight=64.0)
    g.hbar(212.8, 248.7, 135.1, weight=76.0)
    g.diag(212.8, 135.9, 58.0, -40.0, weight=76.0)
    g.diag(261.0, 121.6, 322.3, 63.0, weight=96.0)
    g.hbar(322.3, 358.6, 60.8, weight=96.0)
    g.hbar(370.9, 637.2, 540.7, weight=96.0)
    g.hbar(370.8, 825.4, 421.8, weight=96.0)
    g.diag(825.4, 471.0, 872.1, 539.4, weight=96.0)
    g.diag(517.3, 372.8, 614.3, 309.6, weight=64.0)
    g.diag(614.3, 309.6, 535.2, 144.5, weight=64.0)
    g.diag(575.8, 259.0, 594.3, 280.8, weight=96.0)
    g.hbar(594.3, 687.5, 287.0, weight=96.0)
    g.diag(356.3, 269.6, 441.2, 227.8, weight=64.0)
    g.vbar(445.9, 111.8, 227.8, weight=64.0)
    g.hbar(356.9, 720.4, 134.6, weight=96.0)
    g.diag(622.3, 755.0, 703.7, 508.8, weight=96.0)
    g.diag(703.7, 508.8, 896.2, -72.0, weight=96.0)
    g.diag(896.2, -72.0, 947.0, 119.4, weight=96.0)
    g.hbar(706.0, 855.9, 623.5, weight=96.0)
    g.vbar(859.0, 500.8, 603.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_8cea() -> Glyph:
    """質 U+8CEA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8CEA", advance=1000, unicode=0x8CEA, note="質：自动生成")
    g.hbar(384.4, 508.7, 750.1, weight=84.0)
    g.hbar(246.7, 384.4, 725.8, weight=84.0)
    g.diag(213.2, 701.5, 134.7, 415.3, weight=96.0)
    g.hbar(250.6, 537.8, 612.9, weight=84.0)
    g.diag(380.8, 588.2, 366.5, 568.3, weight=96.0)
    g.vbar(370.0, 437.4, 568.3, weight=96.0)
    g.diag(782.8, 700.0, 708.7, 780.8, weight=84.0)
    g.diag(708.7, 780.8, 607.8, 730.4, weight=84.0)
    g.diag(607.8, 730.4, 604.8, 723.5, weight=84.0)
    g.diag(569.1, 735.0, 587.9, 746.3, weight=96.0)
    g.diag(587.9, 746.3, 515.8, 451.0, weight=96.0)
    g.hbar(600.2, 865.3, 659.0, weight=84.0)
    g.diag(683.8, 621.5, 717.1, 592.0, weight=84.0)
    g.diag(717.1, 592.0, 671.7, 399.6, weight=84.0)
    g.diag(363.7, 403.2, 329.1, 313.6, weight=48.0)
    g.diag(329.1, 313.6, 365.3, 132.9, weight=48.0)
    g.hbar(373.8, 603.2, 410.1, weight=48.0)
    g.diag(603.2, 425.1, 652.5, 375.6, weight=48.0)
    g.diag(652.5, 375.6, 607.4, 149.5, weight=48.0)
    g.hbar(384.9, 543.2, 316.4, weight=48.0)
    g.hbar(383.9, 526.5, 244.6, weight=56.0)
    g.diag(526.5, 257.1, 552.7, 197.7, weight=56.0)
    g.hbar(379.8, 607.8, 152.9, weight=64.0)
    g.diag(428.5, 135.9, 218.3, -57.8, weight=64.0)
    g.diag(572.8, 128.8, 708.5, -72.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_8ced() -> Glyph:
    """賭 U+8CED —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8CED", advance=1000, unicode=0x8CED, note="賭：自动生成")
    g.vbar(168.6, 234.2, 625.0, weight=64.0)
    g.hbar(179.5, 308.6, 626.5, weight=48.0)
    g.vbar(320.3, 479.9, 639.4, weight=48.0)
    g.vbar(323.9, 190.9, 479.9, weight=48.0)
    g.diag(194.2, 469.8, 208.4, 485.3, weight=64.0)
    g.hbar(208.4, 320.0, 486.2, weight=64.0)
    g.diag(194.1, 370.1, 206.9, 385.4, weight=84.0)
    g.hbar(206.9, 312.0, 386.3, weight=84.0)
    g.diag(188.4, 254.1, 202.7, 271.3, weight=64.0)
    g.hbar(202.7, 313.6, 275.0, weight=64.0)
    g.hbar(218.3, 264.1, 175.4, weight=84.0)
    g.diag(218.3, 171.1, 58.0, 10.6, weight=84.0)
    g.dot(333.6, 147.4, w=96.0, h=100.1, slant=-14.0)
    g.hbar(505.1, 540.9, 510.0, weight=96.0)
    g.hbar(505.1, 696.3, 524.5, weight=96.0)
    g.diag(540.2, 761.2, 587.2, 719.5, weight=76.0)
    g.vbar(581.9, 437.2, 719.5, weight=76.0)
    g.diag(576.6, 437.2, 559.3, 415.1, weight=76.0)
    g.hbar(384.0, 937.0, 399.3, weight=96.0)
    g.diag(738.6, 662.4, 659.6, 468.1, weight=48.0)
    g.diag(659.6, 468.1, 300.5, 7.7, weight=48.0)
    g.vbar(526.5, -2.4, 260.2, weight=48.0)
    g.diag(540.4, -2.4, 535.5, 5.4, weight=48.0)
    g.diag(532.0, 256.5, 545.5, 249.3, weight=48.0)
    g.diag(545.5, 249.3, 700.8, 164.3, weight=48.0)
    g.diag(700.8, 164.3, 736.7, -41.2, weight=48.0)
    g.diag(553.6, 136.2, 563.8, 151.5, weight=96.0)
    g.hbar(563.8, 708.8, 153.1, weight=96.0)
    g.diag(548.8, 19.2, 567.0, 32.7, weight=96.0)
    g.hbar(567.0, 702.1, 36.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_8d08() -> Glyph:
    """贈 U+8D08 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8D08", advance=1000, unicode=0x8D08, note="贈：自动生成")
    g.vbar(194.0, 212.4, 629.2, weight=56.0)
    g.diag(213.1, 622.1, 334.0, 467.7, weight=96.0)
    g.vbar(342.2, 152.6, 467.7, weight=96.0)
    g.diag(220.2, 469.4, 227.5, 485.2, weight=96.0)
    g.hbar(227.5, 335.7, 487.9, weight=96.0)
    g.dot(275.5, 352.8, w=96.0, h=120.3, slant=-14.0)
    g.dot(270.6, 239.0, w=92.0, h=119.6, slant=-14.0)
    g.diag(206.6, 169.3, 238.9, 119.1, weight=96.0)
    g.diag(238.9, 119.1, 80.8, -48.7, weight=96.0)
    g.diag(343.5, 142.9, 397.3, 64.3, weight=96.0)
    g.hbar(397.3, 514.4, 40.0, weight=96.0)
    g.diag(493.0, 694.4, 578.5, 631.3, weight=64.0)
    g.diag(578.5, 631.3, 605.5, 547.8, weight=64.0)
    g.diag(790.2, 787.0, 819.2, 752.0, weight=96.0)
    g.diag(819.2, 752.0, 699.8, 581.4, weight=96.0)
    g.vbar(468.7, 502.5, 510.1, weight=48.0)
    g.vbar(495.1, 312.7, 502.5, weight=48.0)
    g.hbar(482.9, 872.0, 536.2, weight=48.0)
    g.diag(872.0, 566.8, 904.2, 521.3, weight=48.0)
    g.diag(904.2, 521.3, 836.9, 342.9, weight=48.0)
    g.diag(639.6, 515.2, 667.0, 487.9, weight=56.0)
    g.vbar(664.8, 384.6, 487.9, weight=56.0)
    g.diag(662.6, 384.6, 649.2, 371.7, weight=56.0)
    g.diag(548.0, 489.5, 631.3, 382.7, weight=48.0)
    g.diag(765.1, 536.4, 784.1, 481.6, weight=48.0)
    g.diag(784.1, 481.6, 724.7, 379.1, weight=48.0)
    g.hbar(532.7, 824.9, 337.4, weight=48.0)
    g.vbar(556.6, -61.6, 220.8, weight=96.0)
    g.hbar(577.8, 770.2, 229.1, weight=48.0)
    g.diag(770.2, 259.8, 872.6, 184.7, weight=48.0)
    g.diag(872.6, 184.7, 767.8, -26.9, weight=48.0)
    g.hbar(741.4, 767.8, -22.5, weight=48.0)
    g.hbar(583.6, 773.9, 105.8, weight=96.0)
    g.diag(582.6, -29.3, 594.6, -14.0, weight=96.0)
    g.hbar(594.6, 744.4, -6.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_8d66() -> Glyph:
    """赦 U+8D66 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8D66", advance=1000, unicode=0x8D66, note="赦：自动生成")
    g.hbar(174.9, 400.5, 547.4, weight=96.0)
    g.hbar(368.4, 400.5, 567.6, weight=96.0)
    g.diag(289.8, 744.0, 335.2, 705.7, weight=96.0)
    g.vbar(330.2, 445.6, 705.7, weight=96.0)
    g.diag(325.1, 445.6, 308.0, 419.4, weight=96.0)
    g.vbar(120.6, 286.2, 352.7, weight=96.0)
    g.hbar(120.5, 489.4, 381.8, weight=96.0)
    g.diag(210.2, 348.9, 260.8, 319.7, weight=84.0)
    g.diag(260.8, 319.7, 146.5, -4.7, weight=84.0)
    g.diag(146.5, -4.7, 93.0, 83.5, weight=84.0)
    g.diag(345.3, 381.1, 361.7, 253.2, weight=64.0)
    g.vbar(357.2, -13.8, 253.2, weight=64.0)
    g.diag(352.7, -13.8, 211.5, 60.5, weight=64.0)
    g.diag(210.1, 250.9, 130.6, 201.7, weight=76.0)
    g.vbar(136.8, 62.8, 201.7, weight=76.0)
    g.diag(405.8, 274.3, 467.3, 222.9, weight=76.0)
    g.hbar(467.3, 535.3, 233.5, weight=76.0)
    g.diag(620.5, 740.0, 669.8, 695.4, weight=96.0)
    g.diag(669.8, 695.4, 502.2, 383.5, weight=96.0)
    g.hbar(567.1, 833.2, 453.2, weight=96.0)
    g.diag(657.8, 409.4, 630.6, 278.5, weight=76.0)
    g.diag(630.6, 278.5, 398.9, 29.3, weight=76.0)
    g.diag(499.0, 344.2, 937.0, -14.0, weight=76.0)
    return g
def g_cjk_unified_ideograph_8da3() -> Glyph:
    """趣 U+8DA3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8DA3", advance=1000, unicode=0x8DA3, note="趣：自动生成")
    g.hbar(245.3, 281.1, 538.1, weight=96.0)
    g.hbar(245.3, 434.1, 561.7, weight=96.0)
    g.diag(280.7, 747.3, 330.4, 703.7, weight=96.0)
    g.vbar(316.6, 435.1, 703.7, weight=96.0)
    g.vbar(149.4, 330.5, 368.3, weight=96.0)
    g.hbar(146.4, 480.0, 402.6, weight=96.0)
    g.diag(291.3, 384.1, 318.3, 361.9, weight=96.0)
    g.vbar(317.3, 182.7, 361.9, weight=96.0)
    g.diag(316.4, 182.7, 331.8, 157.7, weight=96.0)
    g.diag(341.4, 274.3, 390.6, 296.4, weight=96.0)
    g.diag(390.6, 296.4, 435.2, 263.0, weight=96.0)
    g.diag(175.7, 335.7, 219.7, 262.7, weight=92.0)
    g.diag(219.7, 262.7, 63.0, 15.1, weight=92.0)
    g.diag(222.9, 209.7, 390.6, 129.6, weight=96.0)
    g.hbar(390.6, 932.0, 69.0, weight=96.0)
    g.hbar(459.0, 657.9, 629.5, weight=96.0)
    g.diag(657.9, 644.7, 672.1, 621.1, weight=96.0)
    g.diag(485.9, 591.2, 510.1, 568.9, weight=96.0)
    g.vbar(517.2, 278.5, 568.9, weight=96.0)
    g.diag(524.4, 278.5, 504.2, 259.8, weight=96.0)
    g.vbar(631.7, 424.5, 611.9, weight=64.0)
    g.vbar(635.9, 22.0, 424.5, weight=64.0)
    g.diag(544.1, 475.6, 554.4, 488.4, weight=64.0)
    g.hbar(554.4, 624.4, 489.1, weight=64.0)
    g.diag(542.8, 377.3, 551.5, 389.9, weight=84.0)
    g.hbar(551.5, 614.7, 391.7, weight=84.0)
    g.diag(429.1, 274.0, 463.8, 213.7, weight=56.0)
    g.hbar(463.8, 658.3, 247.7, weight=56.0)
    g.diag(658.3, 281.7, 669.1, 303.7, weight=56.0)
    g.diag(668.6, 456.9, 778.1, 404.4, weight=48.0)
    g.diag(778.1, 404.4, 664.4, 221.7, weight=48.0)
    g.diag(667.6, 399.0, 880.9, 189.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_8ddd() -> Glyph:
    """距 U+8DDD —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8DDD", advance=1000, unicode=0x8DDD, note="距：自动生成")
    g.diag(187.2, 628.7, 178.9, 614.4, weight=48.0)
    g.vbar(203.4, 445.3, 614.4, weight=48.0)
    g.hbar(193.4, 410.1, 629.5, weight=48.0)
    g.diag(410.1, 637.7, 345.4, 505.9, weight=48.0)
    g.hbar(242.7, 388.9, 475.6, weight=96.0)
    g.diag(388.9, 493.6, 394.6, 501.3, weight=96.0)
    g.diag(279.1, 449.5, 313.5, 416.3, weight=84.0)
    g.vbar(307.9, 148.3, 416.3, weight=84.0)
    g.diag(302.4, 148.3, 290.2, 138.2, weight=84.0)
    g.diag(339.8, 302.0, 366.0, 328.2, weight=96.0)
    g.hbar(366.0, 498.4, 329.9, weight=96.0)
    g.diag(128.5, 326.2, 172.0, 283.8, weight=96.0)
    g.vbar(181.1, 122.1, 283.8, weight=96.0)
    g.diag(190.2, 122.1, 176.6, 101.7, weight=96.0)
    g.diag(140.1, 89.9, 134.8, 46.0, weight=96.0)
    g.hbar(134.8, 493.2, 108.5, weight=96.0)
    g.hbar(552.0, 851.2, 647.6, weight=96.0)
    g.hbar(556.8, 812.8, 431.6, weight=48.0)
    g.diag(812.8, 449.0, 735.0, 297.9, weight=48.0)
    g.hbar(555.3, 773.4, 271.8, weight=48.0)
    g.vbar(773.7, 279.9, 311.3, weight=48.0)
    g.diag(533.5, 634.6, 637.4, 204.1, weight=48.0)
    g.diag(637.4, 204.1, 927.0, 53.3, weight=48.0)
    return g
def g_cjk_unified_ideograph_8df3() -> Glyph:
    """跳 U+8DF3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8DF3", advance=1000, unicode=0x8DF3, note="跳：自动生成")
    g.vbar(192.2, 412.6, 596.4, weight=96.0)
    g.hbar(193.7, 334.6, 605.0, weight=48.0)
    g.diag(334.6, 629.0, 373.0, 598.4, weight=48.0)
    g.diag(373.0, 598.4, 317.2, 472.2, weight=48.0)
    g.dot(306.5, 440.1, w=96.0, h=124.8, slant=-14.0)
    g.diag(249.8, 416.7, 272.1, 335.2, weight=76.0)
    g.diag(272.1, 335.2, 371.2, 218.0, weight=76.0)
    g.diag(371.2, 218.0, 265.3, 121.0, weight=76.0)
    g.diag(313.4, 300.5, 340.1, 321.8, weight=76.0)
    g.diag(340.1, 321.8, 433.5, 274.6, weight=76.0)
    g.diag(107.6, 302.6, 186.1, 126.2, weight=96.0)
    g.diag(186.1, 126.2, 161.3, 85.8, weight=96.0)
    g.hbar(63.0, 123.2, 34.4, weight=64.0)
    g.diag(123.2, 26.6, 385.5, 200.5, weight=64.0)
    g.vbar(515.1, 448.7, 645.0, weight=96.0)
    g.diag(523.2, 448.7, 439.8, 16.2, weight=96.0)
    g.hbar(290.7, 439.8, 37.9, weight=96.0)
    g.dot(460.8, 424.4, w=96.0, h=124.8, slant=-14.0)
    g.diag(381.3, 174.8, 521.1, 307.7, weight=76.0)
    g.diag(652.3, 730.1, 688.0, 497.5, weight=96.0)
    g.diag(688.0, 497.5, 787.8, 7.4, weight=96.0)
    g.hbar(787.8, 947.9, 12.8, weight=96.0)
    g.diag(947.9, 18.1, 898.1, 199.7, weight=96.0)
    g.hbar(730.6, 845.1, 537.0, weight=96.0)
    g.diag(845.1, 515.3, 720.5, 406.4, weight=96.0)
    g.diag(697.3, 331.9, 868.1, 223.7, weight=48.0)
    return g
def g_cjk_unified_ideograph_8e0a() -> Glyph:
    """踊 U+8E0A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8E0A", advance=1000, unicode=0x8E0A, note="踊：自动生成")
    g.vbar(222.8, 478.8, 681.7, weight=48.0)
    g.hbar(203.6, 411.6, 684.3, weight=48.0)
    g.vbar(382.5, 548.5, 700.7, weight=48.0)
    g.dot(323.1, 519.8, w=92.0, h=119.6, slant=-14.0)
    g.vbar(290.9, 157.8, 489.2, weight=48.0)
    g.dot(418.3, 352.3, w=92.0, h=119.6, slant=-14.0)
    g.vbar(204.6, 222.8, 431.2, weight=92.0)
    g.vbar(195.2, 132.7, 222.8, weight=92.0)
    g.diag(155.4, 124.6, 105.8, 66.5, weight=92.0)
    g.hbar(105.8, 486.1, 131.7, weight=92.0)
    g.hbar(536.5, 846.6, 742.3, weight=48.0)
    g.diag(846.6, 758.3, 721.7, 602.3, weight=48.0)
    g.diag(721.7, 602.3, 707.3, 591.3, weight=48.0)
    g.diag(628.4, 616.8, 710.3, 567.0, weight=48.0)
    g.diag(710.3, 567.0, 739.8, 508.9, weight=48.0)
    g.vbar(516.4, 372.3, 463.2, weight=48.0)
    g.vbar(502.7, -15.3, 372.3, weight=48.0)
    g.hbar(529.4, 697.4, 466.1, weight=48.0)
    g.hbar(697.4, 871.1, 491.6, weight=48.0)
    g.vbar(885.1, 338.3, 505.5, weight=48.0)
    g.vbar(888.8, -24.0, 338.3, weight=48.0)
    g.hbar(775.6, 878.5, -10.8, weight=48.0)
    g.hbar(563.9, 869.9, 322.1, weight=92.0)
    g.hbar(559.3, 873.7, 202.2, weight=92.0)
    g.diag(657.3, 450.7, 691.2, 304.2, weight=48.0)
    g.vbar(691.9, -54.0, 304.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_8e2a() -> Glyph:
    """踪 U+8E2A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8E2A", advance=1000, unicode=0x8E2A, note="踪：自动生成")
    g.diag(168.3, 639.8, 156.2, 624.4, weight=48.0)
    g.vbar(182.3, 442.0, 624.4, weight=48.0)
    g.hbar(171.8, 382.9, 644.9, weight=48.0)
    g.diag(382.9, 659.0, 320.1, 512.2, weight=48.0)
    g.dot(293.9, 482.7, w=96.0, h=124.8, slant=-14.0)
    g.diag(245.4, 452.8, 267.0, 348.7, weight=48.0)
    g.vbar(266.4, 123.7, 348.7, weight=48.0)
    g.diag(313.5, 308.9, 377.2, 340.4, weight=96.0)
    g.diag(377.2, 340.4, 433.3, 287.6, weight=96.0)
    g.diag(176.8, 402.5, 148.0, 312.4, weight=92.0)
    g.diag(148.0, 312.4, 181.2, 121.6, weight=92.0)
    g.diag(181.2, 121.6, 167.8, 99.9, weight=92.0)
    g.vbar(128.5, 41.4, 88.3, weight=96.0)
    g.hbar(126.1, 459.4, 96.3, weight=96.0)
    g.diag(593.0, 782.3, 687.2, 724.3, weight=76.0)
    g.diag(687.2, 724.3, 719.8, 630.0, weight=76.0)
    g.vbar(470.8, 460.1, 577.8, weight=96.0)
    g.hbar(408.9, 450.6, 463.1, weight=96.0)
    g.hbar(516.3, 904.2, 579.5, weight=96.0)
    g.diag(904.2, 610.2, 805.0, 469.9, weight=96.0)
    g.hbar(485.5, 799.7, 442.2, weight=96.0)
    g.diag(423.9, 302.7, 503.8, 249.2, weight=96.0)
    g.hbar(503.8, 883.4, 277.4, weight=96.0)
    g.diag(635.7, 244.2, 607.1, 114.4, weight=96.0)
    g.diag(607.1, 114.4, 489.3, 26.3, weight=96.0)
    g.vbar(510.6, -0.3, 209.1, weight=96.0)
    g.diag(710.5, 178.4, 947.0, 31.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_8e74() -> Glyph:
    """蹴 U+8E74 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8E74", advance=1000, unicode=0x8E74, note="蹴：自动生成")
    g.diag(163.9, 636.8, 152.4, 624.2, weight=48.0)
    g.vbar(170.8, 479.3, 624.2, weight=48.0)
    g.hbar(171.3, 321.4, 642.3, weight=48.0)
    g.vbar(309.8, 562.0, 657.2, weight=48.0)
    g.diag(298.2, 562.0, 278.0, 541.9, weight=48.0)
    g.dot(259.7, 514.1, w=96.0, h=124.8, slant=-14.0)
    g.diag(218.7, 487.6, 254.0, 467.8, weight=48.0)
    g.vbar(243.2, 213.2, 467.8, weight=48.0)
    g.dot(320.6, 364.1, w=96.0, h=99.4, slant=-14.0)
    g.diag(104.2, 374.0, 143.4, 336.9, weight=76.0)
    g.vbar(150.4, 206.3, 336.9, weight=76.0)
    g.diag(157.4, 206.3, 146.6, 187.2, weight=76.0)
    g.vbar(112.8, 140.0, 174.2, weight=96.0)
    g.hbar(115.2, 349.8, 190.4, weight=96.0)
    g.diag(450.8, 748.7, 524.1, 706.6, weight=96.0)
    g.diag(524.1, 706.6, 560.1, 618.7, weight=96.0)
    g.hbar(352.7, 680.2, 557.4, weight=64.0)
    g.vbar(409.9, 319.7, 457.3, weight=48.0)
    g.hbar(405.0, 556.2, 462.8, weight=48.0)
    g.vbar(545.7, 401.2, 476.2, weight=48.0)
    g.diag(535.1, 401.2, 513.3, 382.2, weight=48.0)
    g.dot(497.3, 353.1, w=96.0, h=124.8, slant=-14.0)
    g.diag(459.8, 330.8, 296.4, 150.8, weight=48.0)
    g.diag(296.4, 150.8, 355.0, 118.9, weight=48.0)
    g.dot(366.7, 170.0, w=84.0, h=109.2, slant=0.0)
    g.dot(557.9, 232.0, w=96.0, h=118.0, slant=-14.0)
    g.hbar(577.5, 863.6, 413.1, weight=48.0)
    g.vbar(662.8, 476.7, 715.6, weight=76.0)
    g.diag(662.9, 476.7, 553.2, -9.5, weight=76.0)
    g.diag(553.2, -9.5, 476.1, 33.8, weight=76.0)
    g.diag(718.2, 337.3, 677.5, 384.9, weight=96.0)
    g.diag(677.5, 384.9, 777.8, 10.6, weight=96.0)
    g.hbar(777.8, 940.9, 14.4, weight=96.0)
    g.vbar(941.4, 18.3, 144.0, weight=96.0)
    g.hbar(749.8, 890.1, 635.8, weight=96.0)
    g.vbar(882.4, 487.2, 609.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_8e8d() -> Glyph:
    """躍 U+8E8D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8E8D", advance=1000, unicode=0x8E8D, note="躍：自动生成")
    g.vbar(205.2, 472.7, 639.8, weight=48.0)
    g.hbar(195.3, 363.7, 642.9, weight=48.0)
    g.vbar(351.0, 553.5, 659.5, weight=48.0)
    g.diag(338.4, 553.5, 316.5, 533.8, weight=48.0)
    g.dot(298.4, 503.9, w=96.0, h=124.8, slant=-14.0)
    g.diag(257.5, 480.2, 308.1, 449.1, weight=64.0)
    g.diag(308.1, 449.1, 274.7, 190.9, weight=64.0)
    g.diag(314.9, 349.7, 365.6, 377.6, weight=64.0)
    g.diag(365.6, 377.6, 437.1, 342.1, weight=64.0)
    g.diag(127.0, 344.1, 169.9, 306.0, weight=92.0)
    g.diag(169.9, 306.0, 189.9, 179.3, weight=92.0)
    g.diag(189.9, 179.3, 178.1, 164.6, weight=92.0)
    g.vbar(142.6, 108.9, 149.3, weight=96.0)
    g.diag(142.2, 108.9, 386.0, 220.4, weight=96.0)
    g.vbar(457.5, 675.9, 706.0, weight=64.0)
    g.hbar(460.8, 607.2, 717.7, weight=64.0)
    g.vbar(580.6, 556.9, 729.3, weight=64.0)
    g.diag(464.2, 680.6, 534.6, 597.8, weight=48.0)
    g.hbar(398.1, 544.0, 551.3, weight=84.0)
    g.hbar(619.0, 780.2, 746.1, weight=64.0)
    g.diag(780.2, 762.7, 824.2, 722.5, weight=64.0)
    g.diag(824.2, 722.5, 719.9, 539.6, weight=64.0)
    g.hbar(618.7, 717.3, 665.2, weight=48.0)
    g.diag(602.1, 603.1, 691.6, 562.1, weight=48.0)
    g.diag(691.6, 562.1, 669.4, 511.9, weight=48.0)
    g.diag(566.0, 516.4, 387.9, 232.6, weight=48.0)
    g.vbar(497.0, -52.0, 342.7, weight=48.0)
    g.diag(680.7, 536.5, 706.1, 425.7, weight=56.0)
    g.hbar(535.0, 829.6, 414.5, weight=56.0)
    g.hbar(537.1, 756.9, 296.2, weight=64.0)
    g.diag(756.9, 311.9, 799.1, 255.3, weight=64.0)
    g.hbar(534.7, 737.9, 209.3, weight=64.0)
    g.diag(737.9, 217.6, 796.4, 291.9, weight=64.0)
    g.diag(663.0, 369.8, 692.5, 346.0, weight=96.0)
    g.vbar(691.6, 143.2, 346.0, weight=96.0)
    g.diag(690.6, 143.2, 676.4, 121.3, weight=96.0)
    g.diag(537.4, 88.9, 543.3, 81.0, weight=92.0)
    g.hbar(543.3, 901.0, 91.1, weight=92.0)
    return g
def g_cjk_unified_ideograph_8ed2() -> Glyph:
    """軒 U+8ED2 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8ED2", advance=1000, unicode=0x8ED2, note="軒：自动生成")
    g.diag(214.3, 538.4, 272.8, 601.1, weight=96.0)
    g.hbar(272.8, 386.5, 618.1, weight=96.0)
    g.diag(386.5, 635.1, 440.5, 583.1, weight=96.0)
    g.vbar(194.1, 484.8, 498.5, weight=48.0)
    g.vbar(212.6, 305.9, 484.8, weight=48.0)
    g.hbar(205.8, 482.4, 516.4, weight=48.0)
    g.vbar(456.2, 348.7, 540.7, weight=48.0)
    g.hbar(414.8, 430.1, 349.4, weight=48.0)
    g.hbar(237.8, 374.1, 425.7, weight=64.0)
    g.hbar(358.8, 374.1, 439.2, weight=64.0)
    g.hbar(245.1, 406.2, 339.4, weight=64.0)
    g.hbar(96.6, 421.7, 227.4, weight=92.0)
    g.diag(421.7, 257.2, 450.8, 300.1, weight=92.0)
    g.vbar(305.4, 498.3, 772.0, weight=84.0)
    g.vbar(318.8, -4.6, 498.3, weight=84.0)
    g.vbar(612.5, 563.8, 578.3, weight=96.0)
    g.hbar(614.0, 818.6, 600.0, weight=96.0)
    g.hbar(463.7, 913.4, 410.0, weight=48.0)
    g.hbar(647.7, 691.5, 544.0, weight=96.0)
    g.vbar(687.0, -52.0, 535.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_8f03() -> Glyph:
    """較 U+8F03 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8F03", advance=1000, unicode=0x8F03, note="較：自动生成")
    g.diag(200.9, 526.3, 250.5, 596.7, weight=92.0)
    g.hbar(250.5, 393.8, 616.2, weight=92.0)
    g.hbar(364.9, 393.8, 637.1, weight=92.0)
    g.vbar(179.3, 467.7, 490.2, weight=48.0)
    g.vbar(203.4, 301.4, 467.7, weight=48.0)
    g.diag(202.2, 489.5, 206.0, 487.2, weight=92.0)
    g.hbar(206.0, 475.8, 503.7, weight=92.0)
    g.vbar(449.8, 338.8, 520.2, weight=92.0)
    g.hbar(401.4, 423.8, 337.8, weight=92.0)
    g.hbar(220.6, 350.7, 416.1, weight=64.0)
    g.hbar(241.1, 392.8, 337.7, weight=64.0)
    g.hbar(76.0, 490.9, 221.4, weight=92.0)
    g.vbar(295.5, 491.3, 770.3, weight=92.0)
    g.vbar(309.8, -30.3, 491.3, weight=92.0)
    g.diag(604.4, 728.6, 686.9, 682.1, weight=92.0)
    g.diag(686.9, 682.1, 717.1, 608.7, weight=92.0)
    g.hbar(562.3, 863.4, 548.3, weight=92.0)
    g.diag(580.6, 495.4, 601.0, 433.4, weight=92.0)
    g.diag(601.0, 433.4, 467.1, 349.9, weight=92.0)
    g.diag(699.4, 525.7, 819.7, 400.4, weight=92.0)
    g.diag(611.3, 404.9, 740.8, 286.5, weight=84.0)
    g.diag(740.8, 286.5, 460.2, 43.7, weight=84.0)
    g.diag(508.6, 311.3, 944.0, 23.7, weight=92.0)
    return g
def g_cjk_unified_ideograph_8f1d() -> Glyph:
    """輝 U+8F1D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8F1D", advance=1000, unicode=0x8F1D, note="輝：自动生成")
    g.diag(253.6, 764.0, 275.8, 659.4, weight=48.0)
    g.vbar(271.6, 479.3, 659.4, weight=48.0)
    g.diag(135.1, 613.7, 245.3, 498.5, weight=64.0)
    g.diag(375.0, 659.9, 390.4, 637.8, weight=48.0)
    g.diag(390.4, 637.8, 302.9, 560.7, weight=48.0)
    g.hbar(75.3, 445.3, 457.6, weight=48.0)
    g.diag(282.1, 443.6, 58.0, 163.8, weight=48.0)
    g.vbar(289.7, 179.0, 375.7, weight=96.0)
    g.diag(300.9, 179.0, 415.9, 238.8, weight=96.0)
    g.diag(494.8, 737.0, 472.7, 632.9, weight=96.0)
    g.diag(472.7, 632.9, 506.9, 595.3, weight=96.0)
    g.hbar(526.2, 797.7, 734.0, weight=96.0)
    g.hbar(797.7, 877.9, 741.3, weight=96.0)
    g.diag(877.9, 729.4, 785.5, 636.3, weight=96.0)
    g.hbar(498.3, 782.7, 616.1, weight=64.0)
    g.hbar(432.8, 490.6, 484.1, weight=48.0)
    g.vbar(513.2, 305.3, 476.9, weight=48.0)
    g.hbar(511.5, 824.4, 498.0, weight=48.0)
    g.vbar(797.7, 354.5, 524.0, weight=48.0)
    g.hbar(750.2, 770.9, 352.3, weight=48.0)
    g.hbar(531.6, 701.8, 420.3, weight=56.0)
    g.diag(701.8, 437.7, 731.6, 385.1, weight=56.0)
    g.diag(548.8, 318.7, 557.3, 326.8, weight=48.0)
    g.hbar(557.3, 752.3, 343.0, weight=48.0)
    g.hbar(388.3, 595.3, 223.4, weight=48.0)
    g.hbar(595.3, 927.0, 223.0, weight=48.0)
    g.diag(597.5, 698.5, 644.0, 671.4, weight=96.0)
    g.vbar(638.1, -54.0, 671.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_8f29() -> Glyph:
    """輩 U+8F29 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8F29", advance=1000, unicode=0x8F29, note="輩：自动生成")
    g.diag(364.8, 766.0, 397.9, 732.8, weight=76.0)
    g.vbar(400.2, 522.1, 732.8, weight=76.0)
    g.hbar(238.7, 374.0, 690.9, weight=56.0)
    g.hbar(248.8, 367.5, 621.4, weight=56.0)
    g.diag(367.5, 626.9, 376.7, 621.5, weight=56.0)
    g.hbar(217.5, 253.4, 511.9, weight=48.0)
    g.hbar(253.4, 367.5, 530.8, weight=48.0)
    g.vbar(368.9, 553.3, 566.2, weight=48.0)
    g.diag(556.2, 777.0, 588.4, 744.8, weight=96.0)
    g.vbar(585.7, 542.3, 744.8, weight=96.0)
    g.hbar(619.7, 765.1, 742.9, weight=64.0)
    g.hbar(611.4, 746.7, 664.7, weight=56.0)
    g.hbar(609.6, 777.1, 575.4, weight=56.0)
    g.hbar(374.9, 594.9, 470.5, weight=56.0)
    g.vbar(337.6, 192.6, 368.3, weight=48.0)
    g.hbar(343.6, 463.9, 374.7, weight=48.0)
    g.hbar(463.9, 670.8, 388.8, weight=48.0)
    g.diag(670.8, 399.2, 612.9, 234.1, weight=48.0)
    g.diag(612.9, 234.1, 590.3, 246.9, weight=48.0)
    g.hbar(403.4, 570.0, 308.1, weight=56.0)
    g.diag(390.5, 222.9, 398.7, 216.6, weight=64.0)
    g.hbar(398.7, 562.7, 230.8, weight=64.0)
    g.diag(562.7, 245.0, 571.9, 234.9, weight=64.0)
    g.hbar(123.6, 866.4, 118.9, weight=76.0)
    g.diag(455.0, 556.1, 481.7, 384.2, weight=48.0)
    g.vbar(484.9, -67.0, 384.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_8f38() -> Glyph:
    """輸 U+8F38 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8F38", advance=1000, unicode=0x8F38, note="輸：自动生成")
    g.diag(177.3, 497.5, 229.5, 569.2, weight=96.0)
    g.hbar(229.5, 338.7, 583.6, weight=96.0)
    g.diag(338.7, 597.9, 332.8, 603.7, weight=96.0)
    g.vbar(156.1, 442.2, 456.6, weight=48.0)
    g.vbar(178.0, 265.5, 442.2, weight=48.0)
    g.hbar(167.7, 430.1, 466.2, weight=48.0)
    g.vbar(403.9, 303.5, 481.7, weight=48.0)
    g.hbar(363.4, 377.6, 303.2, weight=48.0)
    g.hbar(200.7, 374.9, 375.6, weight=64.0)
    g.hbar(214.7, 354.3, 297.3, weight=64.0)
    g.hbar(73.0, 428.3, 188.4, weight=84.0)
    g.vbar(260.9, -42.7, 762.7, weight=76.0)
    g.diag(624.2, 655.9, 619.6, 671.5, weight=92.0)
    g.diag(619.6, 671.5, 443.4, 396.6, weight=92.0)
    g.diag(636.6, 626.1, 648.7, 590.4, weight=76.0)
    g.diag(648.7, 590.4, 947.0, 453.5, weight=76.0)
    g.hbar(525.9, 727.1, 471.7, weight=56.0)
    g.diag(451.1, 306.7, 466.9, 286.8, weight=96.0)
    g.diag(466.9, 286.8, 436.3, 43.2, weight=96.0)
    g.diag(436.3, 43.2, 475.3, 24.1, weight=96.0)
    g.diag(480.3, 290.3, 565.2, 218.8, weight=48.0)
    g.vbar(550.6, 22.3, 218.8, weight=48.0)
    g.hbar(516.1, 535.9, 25.3, weight=48.0)
    g.diag(516.1, 28.4, 512.8, 32.3, weight=48.0)
    g.diag(480.4, 203.5, 491.4, 215.6, weight=56.0)
    g.hbar(491.4, 561.5, 218.0, weight=56.0)
    g.diag(473.0, 122.1, 483.0, 135.5, weight=64.0)
    g.hbar(483.0, 562.7, 136.7, weight=64.0)
    g.hbar(610.4, 666.3, 294.1, weight=64.0)
    g.vbar(671.3, 169.4, 288.0, weight=64.0)
    g.diag(676.3, 169.4, 614.1, 135.4, weight=64.0)
    g.diag(717.3, 435.3, 832.1, 286.0, weight=84.0)
    g.diag(832.1, 286.0, 721.4, -6.7, weight=84.0)
    g.hbar(621.1, 721.4, 8.7, weight=84.0)
    return g
def g_cjk_unified_ideograph_8f44() -> Glyph:
    """轄 U+8F44 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8F44", advance=1000, unicode=0x8F44, note="轄：自动生成")
    g.diag(209.7, 524.0, 229.5, 568.2, weight=96.0)
    g.hbar(229.5, 392.3, 594.1, weight=96.0)
    g.diag(392.3, 619.9, 432.8, 553.3, weight=96.0)
    g.diag(189.7, 484.6, 180.5, 468.3, weight=48.0)
    g.vbar(209.5, 291.2, 468.3, weight=48.0)
    g.hbar(195.3, 466.1, 493.0, weight=48.0)
    g.vbar(442.4, 322.4, 509.3, weight=48.0)
    g.diag(418.7, 322.4, 406.0, 314.0, weight=48.0)
    g.hbar(229.2, 418.6, 396.6, weight=56.0)
    g.hbar(250.5, 394.4, 313.7, weight=56.0)
    g.hbar(73.0, 444.5, 209.3, weight=92.0)
    g.vbar(289.3, -36.6, 766.6, weight=76.0)
    g.diag(621.1, 746.2, 690.4, 704.7, weight=48.0)
    g.diag(690.4, 704.7, 718.0, 625.5, weight=48.0)
    g.dot(545.5, 539.3, w=96.0, h=124.8, slant=0.0)
    g.diag(569.3, 579.9, 573.8, 576.8, weight=96.0)
    g.hbar(573.8, 897.8, 598.4, weight=96.0)
    g.diag(897.8, 619.9, 809.9, 516.1, weight=96.0)
    g.diag(542.9, 467.4, 603.1, 436.8, weight=64.0)
    g.hbar(603.1, 804.5, 469.1, weight=64.0)
    g.diag(588.2, 414.8, 651.6, 354.4, weight=64.0)
    g.hbar(651.6, 752.3, 368.2, weight=64.0)
    g.diag(752.3, 382.1, 802.7, 318.9, weight=64.0)
    g.hbar(468.8, 927.0, 266.9, weight=64.0)
    g.diag(653.4, 570.6, 685.8, 543.2, weight=92.0)
    g.vbar(684.4, 315.6, 543.2, weight=92.0)
    g.diag(683.0, 315.6, 668.2, 293.4, weight=92.0)
    g.diag(520.3, 168.6, 604.7, 16.0, weight=48.0)
    g.hbar(536.0, 774.3, 184.0, weight=48.0)
    g.diag(774.3, 192.8, 809.4, 156.7, weight=48.0)
    g.diag(809.4, 156.7, 751.3, 68.3, weight=48.0)
    g.hbar(599.8, 784.7, 44.7, weight=48.0)
    g.vbar(784.9, 50.1, 72.6, weight=48.0)
    return g
def g_cjk_unified_ideograph_8fa3() -> Glyph:
    """辣 U+8FA3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8FA3", advance=1000, unicode=0x8FA3, note="辣：自动生成")
    g.dot(276.4, 687.8, w=96.0, h=116.8, slant=-14.0)
    g.hbar(136.0, 406.3, 569.4, weight=96.0)
    g.dot(189.5, 446.7, w=96.0, h=81.7, slant=-14.0)
    g.diag(328.0, 535.5, 344.8, 501.8, weight=64.0)
    g.diag(344.8, 501.8, 277.4, 391.3, weight=64.0)
    g.hbar(73.0, 391.0, 357.9, weight=84.0)
    g.hbar(95.9, 374.8, 250.0, weight=84.0)
    g.diag(222.0, 334.9, 272.4, 287.9, weight=96.0)
    g.diag(272.4, 287.9, 120.7, -26.0, weight=96.0)
    g.hbar(471.2, 729.0, 584.7, weight=92.0)
    g.diag(398.6, 448.6, 459.8, 288.2, weight=56.0)
    g.hbar(442.6, 525.6, 451.7, weight=48.0)
    g.hbar(525.6, 746.3, 466.4, weight=48.0)
    g.diag(746.3, 478.9, 711.9, 398.0, weight=48.0)
    g.diag(711.9, 398.0, 688.0, 380.8, weight=48.0)
    g.hbar(475.0, 569.0, 319.4, weight=48.0)
    g.hbar(569.0, 745.3, 340.4, weight=48.0)
    g.vbar(549.5, -70.0, 780.0, weight=96.0)
    g.diag(593.4, 321.6, 534.7, 254.2, weight=48.0)
    g.diag(534.7, 254.2, 313.6, 19.8, weight=48.0)
    g.diag(603.9, 310.1, 942.0, 49.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_8fb1() -> Glyph:
    """辱 U+8FB1 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni8FB1", advance=1000, unicode=0x8FB1, note="辱：自动生成")
    g.diag(318.6, 713.9, 332.4, 700.1, weight=96.0)
    g.hbar(332.4, 669.1, 729.8, weight=96.0)
    g.diag(669.1, 759.6, 644.3, 666.0, weight=96.0)
    g.diag(281.1, 722.2, 146.2, 196.0, weight=96.0)
    g.hbar(315.2, 581.4, 611.0, weight=76.0)
    g.diag(581.4, 623.5, 639.1, 565.9, weight=76.0)
    g.hbar(287.2, 735.6, 503.9, weight=48.0)
    g.diag(343.7, 455.5, 366.2, 439.4, weight=48.0)
    g.vbar(374.2, 297.9, 439.4, weight=48.0)
    g.diag(382.1, 297.9, 510.9, 414.7, weight=48.0)
    g.hbar(684.2, 709.5, 443.1, weight=48.0)
    g.diag(684.2, 447.0, 599.9, 394.8, weight=48.0)
    g.hbar(440.3, 863.9, 399.4, weight=48.0)
    g.hbar(111.1, 851.9, 181.1, weight=56.0)
    g.diag(497.6, 342.1, 566.8, 269.7, weight=96.0)
    g.vbar(553.3, -69.9, 269.7, weight=96.0)
    g.diag(539.8, -69.9, 425.1, 18.0, weight=96.0)
    g.diag(325.0, 158.5, 404.8, 83.4, weight=48.0)
    g.diag(404.8, 83.4, 425.7, 7.3, weight=48.0)
    return g
def g_cjk_unified_ideograph_9038() -> Glyph:
    """逸 U+9038 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9038", advance=1000, unicode=0x9038, note="逸：自动生成")
    g.vbar(553.2, 703.7, 748.6, weight=96.0)
    g.diag(553.7, 748.6, 381.1, 535.8, weight=96.0)
    g.hbar(520.9, 679.8, 670.5, weight=48.0)
    g.diag(679.8, 676.1, 565.4, 524.7, weight=48.0)
    g.vbar(399.9, 469.6, 486.1, weight=64.0)
    g.vbar(415.9, 309.4, 469.6, weight=64.0)
    g.hbar(415.7, 711.0, 507.8, weight=48.0)
    g.diag(711.0, 541.6, 745.1, 502.8, weight=48.0)
    g.diag(745.1, 502.8, 678.6, 393.9, weight=48.0)
    g.hbar(449.0, 713.5, 352.6, weight=48.0)
    g.vbar(713.9, 378.5, 399.7, weight=48.0)
    g.diag(529.6, 491.0, 583.7, 447.5, weight=92.0)
    g.diag(583.7, 447.5, 373.1, 87.8, weight=92.0)
    g.diag(581.7, 339.4, 629.2, 79.4, weight=48.0)
    g.hbar(629.2, 867.7, 87.7, weight=48.0)
    g.vbar(866.5, 95.9, 234.9, weight=48.0)
    g.diag(700.0, 336.3, 736.8, 282.9, weight=96.0)
    g.diag(736.8, 282.9, 827.5, 241.4, weight=96.0)
    g.diag(187.8, 705.3, 362.3, 584.8, weight=96.0)
    g.hbar(80.7, 106.7, 371.7, weight=96.0)
    g.diag(106.7, 373.9, 327.5, 190.4, weight=96.0)
    g.diag(327.5, 190.4, 256.2, 101.2, weight=96.0)
    g.hbar(69.5, 309.5, 34.1, weight=96.0)
    g.hbar(309.5, 902.1, -21.8, weight=96.0)
    g.diag(902.1, -64.5, 925.5, -29.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_9042() -> Glyph:
    """遂 U+9042 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9042", advance=1000, unicode=0x9042, note="遂：自动生成")
    g.dot(495.2, 666.4, w=96.0, h=124.8, slant=-14.0)
    g.diag(677.0, 792.0, 706.0, 756.7, weight=96.0)
    g.diag(706.0, 756.7, 590.7, 623.1, weight=96.0)
    g.vbar(592.3, 595.3, 623.1, weight=96.0)
    g.hbar(412.8, 742.5, 556.6, weight=48.0)
    g.diag(559.7, 527.1, 365.4, 340.3, weight=48.0)
    g.diag(517.0, 423.8, 581.0, 195.9, weight=48.0)
    g.diag(581.0, 195.9, 485.1, 147.4, weight=48.0)
    g.diag(542.9, 398.8, 547.6, 361.0, weight=48.0)
    g.diag(547.6, 361.0, 384.9, 231.9, weight=48.0)
    g.diag(384.9, 231.9, 387.6, 237.5, weight=48.0)
    g.vbar(610.0, 288.6, 340.1, weight=48.0)
    g.diag(609.0, 288.6, 394.7, 116.5, weight=48.0)
    g.diag(754.6, 498.6, 772.0, 462.8, weight=48.0)
    g.diag(772.0, 462.8, 646.2, 359.8, weight=48.0)
    g.diag(700.2, 267.7, 852.4, 139.7, weight=96.0)
    g.diag(192.0, 683.1, 378.9, 545.8, weight=96.0)
    g.hbar(83.1, 279.4, 386.6, weight=96.0)
    g.diag(279.4, 401.6, 226.7, 262.1, weight=96.0)
    g.diag(226.7, 262.1, 278.6, 109.0, weight=96.0)
    g.diag(278.6, 109.0, 262.6, 94.3, weight=96.0)
    g.hbar(85.1, 313.2, 35.8, weight=96.0)
    g.hbar(313.2, 906.9, -4.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_9047() -> Glyph:
    """遇 U+9047 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9047", advance=1000, unicode=0x9047, note="遇：自动生成")
    g.vbar(412.4, 692.0, 704.4, weight=48.0)
    g.vbar(443.8, 456.2, 692.0, weight=48.0)
    g.hbar(425.5, 771.0, 713.5, weight=48.0)
    g.vbar(731.6, 496.4, 728.9, weight=48.0)
    g.hbar(474.8, 698.0, 592.9, weight=84.0)
    g.hbar(486.4, 681.2, 492.3, weight=84.0)
    g.diag(382.2, 369.5, 372.2, 348.8, weight=48.0)
    g.vbar(378.8, 91.4, 348.8, weight=48.0)
    g.hbar(395.0, 516.8, 368.7, weight=48.0)
    g.hbar(516.8, 781.8, 399.1, weight=48.0)
    g.diag(781.8, 422.8, 805.3, 311.1, weight=48.0)
    g.vbar(798.2, 106.9, 311.1, weight=48.0)
    g.hbar(683.3, 791.1, 127.4, weight=48.0)
    g.diag(544.5, 691.7, 563.6, 681.9, weight=96.0)
    g.vbar(581.0, 316.1, 681.9, weight=96.0)
    g.diag(598.5, 316.1, 562.9, 259.2, weight=96.0)
    g.hbar(427.9, 679.2, 242.3, weight=96.0)
    g.diag(651.3, 379.8, 703.7, 275.5, weight=56.0)
    g.vbar(700.5, 249.9, 275.5, weight=56.0)
    g.diag(193.6, 725.4, 277.2, 667.2, weight=96.0)
    g.hbar(277.2, 358.6, 673.4, weight=96.0)
    g.hbar(63.0, 156.8, 430.3, weight=96.0)
    g.diag(156.8, 437.2, 317.0, 185.4, weight=96.0)
    g.diag(317.0, 185.4, 253.8, 130.6, weight=96.0)
    g.hbar(76.3, 299.4, 76.2, weight=96.0)
    g.hbar(299.4, 922.0, 28.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_904d() -> Glyph:
    """遍 U+904D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni904D", advance=1000, unicode=0x904D, note="遍：自动生成")
    g.hbar(512.8, 601.1, 737.2, weight=48.0)
    g.diag(601.1, 717.4, 650.9, 631.1, weight=48.0)
    g.hbar(463.7, 704.2, 596.8, weight=48.0)
    g.diag(704.2, 620.3, 741.4, 584.2, weight=48.0)
    g.diag(741.4, 584.2, 687.7, 503.2, weight=48.0)
    g.hbar(456.4, 725.9, 462.6, weight=48.0)
    g.vbar(725.5, 488.5, 512.2, weight=48.0)
    g.diag(459.5, 585.2, 426.5, 478.0, weight=48.0)
    g.diag(426.5, 478.0, 273.0, 150.6, weight=48.0)
    g.vbar(433.5, 48.8, 327.7, weight=48.0)
    g.hbar(448.9, 554.7, 338.2, weight=48.0)
    g.hbar(554.7, 775.6, 363.4, weight=48.0)
    g.diag(775.6, 383.2, 797.0, 281.7, weight=48.0)
    g.vbar(792.6, 79.2, 281.7, weight=48.0)
    g.hbar(668.2, 788.2, 101.8, weight=48.0)
    g.hbar(485.4, 765.4, 227.5, weight=96.0)
    g.diag(525.1, 316.6, 549.3, 290.2, weight=48.0)
    g.vbar(551.9, 111.5, 290.2, weight=48.0)
    g.diag(626.5, 340.9, 654.9, 314.5, weight=48.0)
    g.vbar(664.8, 110.1, 314.5, weight=48.0)
    g.diag(174.8, 690.0, 384.1, 591.1, weight=96.0)
    g.diag(68.3, 392.7, 28.0, 348.3, weight=96.0)
    g.hbar(28.0, 363.5, 312.9, weight=96.0)
    g.diag(363.5, 277.4, 240.8, 107.5, weight=96.0)
    g.hbar(68.3, 272.0, 43.2, weight=96.0)
    g.hbar(272.0, 916.7, 0.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_905c() -> Glyph:
    """遜 U+905C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni905C", advance=1000, unicode=0x905C, note="遜：自动生成")
    g.hbar(254.7, 469.1, 621.8, weight=64.0)
    g.hbar(469.1, 526.5, 643.8, weight=64.0)
    g.diag(526.5, 636.8, 443.7, 526.4, weight=64.0)
    g.diag(411.8, 529.4, 493.5, 155.0, weight=84.0)
    g.hbar(279.3, 493.5, 167.8, weight=84.0)
    g.hbar(262.9, 333.0, 317.1, weight=96.0)
    g.diag(333.0, 312.8, 560.8, 486.5, weight=96.0)
    g.vbar(785.1, 640.7, 735.1, weight=96.0)
    g.hbar(612.4, 781.3, 704.4, weight=96.0)
    g.hbar(612.4, 626.9, 671.5, weight=96.0)
    g.diag(665.3, 670.1, 684.7, 642.2, weight=48.0)
    g.diag(684.7, 642.2, 586.2, 499.6, weight=48.0)
    g.hbar(586.2, 699.5, 504.2, weight=48.0)
    g.diag(770.4, 607.0, 721.9, 519.1, weight=48.0)
    g.diag(721.9, 519.1, 590.4, 370.9, weight=48.0)
    g.hbar(590.4, 790.0, 391.7, weight=48.0)
    g.diag(772.8, 429.6, 819.2, 407.2, weight=48.0)
    g.diag(819.2, 407.2, 797.8, 397.3, weight=48.0)
    g.diag(677.7, 368.0, 746.3, 98.9, weight=48.0)
    g.diag(746.3, 98.9, 576.6, 189.9, weight=48.0)
    g.vbar(591.4, 167.7, 345.8, weight=84.0)
    g.diag(746.8, 291.7, 846.9, 220.8, weight=96.0)
    g.diag(846.9, 220.8, 863.2, 169.2, weight=96.0)
    g.diag(144.3, 643.3, 231.3, 586.2, weight=96.0)
    g.hbar(231.3, 282.8, 589.1, weight=96.0)
    g.hbar(75.4, 248.2, 393.7, weight=96.0)
    g.diag(248.2, 404.1, 200.1, 268.6, weight=96.0)
    g.diag(200.1, 268.6, 250.2, 147.2, weight=96.0)
    g.diag(250.2, 147.2, 231.3, 123.3, weight=96.0)
    g.hbar(63.0, 278.6, 76.8, weight=96.0)
    g.hbar(278.6, 932.0, 41.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_906d() -> Glyph:
    """遭 U+906D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni906D", advance=1000, unicode=0x906D, note="遭：自动生成")
    g.hbar(435.9, 490.8, 641.9, weight=76.0)
    g.hbar(435.9, 705.6, 661.1, weight=76.0)
    g.diag(705.6, 688.9, 750.6, 621.8, weight=76.0)
    g.vbar(406.8, 342.9, 545.5, weight=48.0)
    g.hbar(392.6, 813.0, 562.2, weight=48.0)
    g.vbar(784.0, 380.5, 584.0, weight=48.0)
    g.hbar(730.5, 754.9, 381.7, weight=48.0)
    g.hbar(436.0, 661.9, 467.3, weight=64.0)
    g.diag(661.9, 485.7, 659.0, 487.4, weight=64.0)
    g.diag(487.9, 673.9, 519.2, 692.4, weight=76.0)
    g.vbar(526.2, 414.8, 692.4, weight=76.0)
    g.diag(533.2, 414.8, 521.2, 394.7, weight=76.0)
    g.diag(619.7, 787.0, 657.4, 752.4, weight=76.0)
    g.vbar(641.1, 422.6, 752.4, weight=76.0)
    g.diag(624.9, 422.6, 611.7, 411.8, weight=76.0)
    g.hbar(448.7, 720.2, 374.9, weight=64.0)
    g.diag(487.3, 289.8, 472.0, 282.1, weight=48.0)
    g.vbar(482.3, 60.3, 282.1, weight=48.0)
    g.diag(495.8, 281.3, 650.5, 208.8, weight=48.0)
    g.diag(650.5, 208.8, 703.2, 23.5, weight=48.0)
    g.hbar(510.1, 678.4, 183.6, weight=76.0)
    g.hbar(506.4, 681.3, 82.0, weight=56.0)
    g.diag(185.2, 701.5, 335.5, 571.1, weight=96.0)
    g.hbar(76.6, 215.8, 363.4, weight=96.0)
    g.diag(215.8, 336.2, 376.4, 235.7, weight=96.0)
    g.diag(376.4, 235.7, 263.7, 96.9, weight=96.0)
    g.hbar(82.6, 333.5, 34.6, weight=84.0)
    g.hbar(333.5, 908.4, -6.1, weight=84.0)
    return g
def g_cjk_unified_ideograph_906e() -> Glyph:
    """遮 U+906E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni906E", advance=1000, unicode=0x906E, note="遮：自动生成")
    g.diag(560.2, 766.7, 636.0, 712.2, weight=96.0)
    g.diag(636.0, 712.2, 665.6, 645.7, weight=96.0)
    g.diag(479.4, 550.5, 493.2, 567.8, weight=96.0)
    g.hbar(493.2, 772.0, 597.4, weight=96.0)
    g.diag(772.0, 626.9, 732.7, 561.6, weight=96.0)
    g.hbar(453.9, 464.9, 567.7, weight=76.0)
    g.diag(464.9, 568.4, 360.3, 171.2, weight=76.0)
    g.diag(360.3, 171.2, 300.5, 136.9, weight=76.0)
    g.hbar(473.3, 780.2, 425.4, weight=96.0)
    g.hbar(748.9, 780.2, 455.5, weight=96.0)
    g.diag(493.4, 533.0, 560.2, 474.9, weight=56.0)
    g.vbar(571.9, 263.4, 474.9, weight=56.0)
    g.diag(683.7, 576.0, 719.9, 518.1, weight=84.0)
    g.diag(719.9, 518.1, 691.6, 357.4, weight=84.0)
    g.diag(691.6, 357.4, 675.4, 339.3, weight=84.0)
    g.diag(596.6, 281.7, 611.0, 297.2, weight=96.0)
    g.hbar(611.0, 705.2, 306.4, weight=96.0)
    g.diag(705.2, 315.5, 709.9, 320.3, weight=96.0)
    g.diag(528.1, 212.3, 464.2, 167.5, weight=76.0)
    g.diag(464.2, 167.5, 423.2, 67.8, weight=76.0)
    g.diag(569.1, 232.6, 582.4, 167.5, weight=76.0)
    g.hbar(582.4, 659.1, 164.3, weight=76.0)
    g.diag(643.1, 273.2, 692.6, 165.4, weight=76.0)
    g.diag(692.6, 165.4, 625.5, 125.4, weight=76.0)
    g.diag(737.4, 279.2, 866.4, 101.8, weight=76.0)
    g.diag(200.4, 710.1, 374.6, 599.2, weight=96.0)
    g.hbar(63.0, 280.5, 408.2, weight=96.0)
    g.diag(280.5, 434.7, 226.6, 289.3, weight=96.0)
    g.diag(226.6, 289.3, 276.8, 134.3, weight=96.0)
    g.diag(276.8, 134.3, 250.0, 108.8, weight=96.0)
    g.hbar(69.1, 298.8, 54.2, weight=96.0)
    g.hbar(298.8, 846.9, -4.1, weight=96.0)
    g.diag(846.9, -46.1, 884.1, 67.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_9075() -> Glyph:
    """遵 U+9075 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9075", advance=1000, unicode=0x9075, note="遵：自动生成")
    g.diag(487.3, 686.7, 522.2, 724.2, weight=92.0)
    g.diag(522.2, 724.2, 536.0, 693.0, weight=92.0)
    g.vbar(674.5, 710.4, 777.4, weight=92.0)
    g.diag(677.7, 777.4, 625.4, 695.7, weight=92.0)
    g.diag(625.4, 695.7, 620.4, 692.4, weight=92.0)
    g.diag(389.5, 588.7, 447.9, 645.8, weight=76.0)
    g.hbar(447.9, 806.7, 660.9, weight=76.0)
    g.diag(417.1, 556.0, 411.6, 544.9, weight=48.0)
    g.vbar(432.6, 322.1, 544.9, weight=48.0)
    g.hbar(426.8, 781.8, 558.9, weight=48.0)
    g.vbar(756.0, 358.0, 568.3, weight=48.0)
    g.hbar(708.5, 730.2, 356.7, weight=48.0)
    g.vbar(503.7, 420.6, 632.7, weight=48.0)
    g.diag(597.9, 644.5, 605.0, 638.6, weight=48.0)
    g.diag(605.0, 638.6, 634.4, 487.1, weight=48.0)
    g.hbar(634.4, 740.8, 482.3, weight=48.0)
    g.hbar(500.6, 618.4, 422.0, weight=48.0)
    g.diag(618.4, 423.2, 652.4, 377.0, weight=48.0)
    g.hbar(469.2, 709.4, 347.3, weight=48.0)
    g.hbar(273.5, 909.1, 238.1, weight=64.0)
    g.diag(637.8, 325.0, 685.1, 276.4, weight=92.0)
    g.vbar(672.8, 69.6, 276.4, weight=92.0)
    g.hbar(558.4, 660.5, 92.1, weight=92.0)
    g.dot(494.3, 165.6, w=92.0, h=117.6, slant=-14.0)
    g.hbar(186.4, 352.2, 670.9, weight=92.0)
    g.hbar(68.7, 138.5, 405.4, weight=92.0)
    g.diag(138.5, 410.2, 336.1, 163.1, weight=92.0)
    g.diag(336.1, 163.1, 258.1, 101.8, weight=92.0)
    g.hbar(87.2, 316.7, 44.9, weight=92.0)
    g.hbar(316.7, 916.3, -2.7, weight=92.0)
    return g
def g_cjk_unified_ideograph_9078() -> Glyph:
    """選 U+9078 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9078", advance=1000, unicode=0x9078, note="選：自动生成")
    g.hbar(411.6, 551.6, 676.8, weight=48.0)
    g.diag(551.6, 694.4, 510.1, 616.9, weight=48.0)
    g.hbar(412.4, 535.0, 589.3, weight=48.0)
    g.diag(395.8, 673.9, 326.9, 576.2, weight=64.0)
    g.diag(326.9, 576.2, 559.9, 445.7, weight=64.0)
    g.vbar(556.0, 445.7, 575.2, weight=64.0)
    g.hbar(640.6, 788.1, 722.5, weight=48.0)
    g.diag(788.1, 733.2, 739.2, 659.7, weight=48.0)
    g.hbar(648.3, 769.3, 637.3, weight=48.0)
    g.vbar(641.0, 508.7, 720.3, weight=48.0)
    g.hbar(652.6, 807.4, 516.4, weight=48.0)
    g.diag(807.4, 524.1, 795.2, 624.0, weight=48.0)
    g.diag(460.2, 379.1, 467.6, 330.9, weight=84.0)
    g.hbar(467.6, 696.3, 354.9, weight=84.0)
    g.diag(696.3, 378.8, 688.9, 385.7, weight=84.0)
    g.diag(476.0, 435.9, 533.9, 279.4, weight=48.0)
    g.diag(533.9, 279.4, 515.8, 256.4, weight=48.0)
    g.diag(646.5, 485.8, 620.5, 272.8, weight=92.0)
    g.diag(620.5, 272.8, 623.0, 275.2, weight=92.0)
    g.hbar(361.1, 844.8, 242.0, weight=56.0)
    g.diag(536.0, 220.8, 418.3, 64.4, weight=48.0)
    g.diag(654.7, 221.8, 746.8, 111.5, weight=92.0)
    g.diag(746.8, 111.5, 778.5, 4.4, weight=92.0)
    g.diag(174.4, 678.8, 354.6, 586.7, weight=96.0)
    g.hbar(85.5, 248.0, 391.1, weight=96.0)
    g.diag(248.0, 400.4, 201.7, 279.5, weight=96.0)
    g.diag(201.7, 279.5, 252.0, 176.5, weight=96.0)
    g.diag(252.0, 176.5, 235.0, 119.9, weight=96.0)
    g.hbar(63.0, 922.0, 46.6, weight=48.0)
    return g
def g_cjk_unified_ideograph_907a() -> Glyph:
    """遺 U+907A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni907A", advance=1000, unicode=0x907A, note="遺：自动生成")
    g.dot(473.8, 598.4, w=84.0, h=109.2, slant=-14.0)
    g.hbar(478.4, 554.9, 654.1, weight=48.0)
    g.hbar(554.9, 705.2, 680.0, weight=48.0)
    g.diag(705.2, 698.9, 742.3, 668.9, weight=48.0)
    g.diag(742.3, 668.9, 698.4, 615.2, weight=48.0)
    g.diag(504.6, 566.9, 517.1, 560.5, weight=48.0)
    g.hbar(517.1, 729.4, 588.6, weight=48.0)
    g.diag(554.1, 788.1, 592.6, 752.6, weight=76.0)
    g.vbar(591.1, 517.8, 752.6, weight=76.0)
    g.diag(589.6, 517.8, 575.8, 503.0, weight=76.0)
    g.hbar(344.1, 887.5, 478.4, weight=64.0)
    g.vbar(487.4, 166.4, 403.6, weight=48.0)
    g.hbar(494.1, 679.4, 413.4, weight=48.0)
    g.diag(679.4, 432.8, 736.5, 394.2, weight=48.0)
    g.diag(736.5, 394.2, 694.6, 187.5, weight=48.0)
    g.diag(505.3, 315.7, 516.4, 327.2, weight=48.0)
    g.hbar(516.4, 615.2, 336.3, weight=48.0)
    g.diag(615.2, 345.4, 638.7, 296.3, weight=48.0)
    g.hbar(503.4, 614.1, 268.0, weight=48.0)
    g.diag(614.1, 280.5, 647.4, 230.3, weight=48.0)
    g.diag(503.8, 179.5, 519.0, 192.2, weight=56.0)
    g.hbar(519.0, 694.1, 194.9, weight=56.0)
    g.diag(548.9, 175.4, 430.2, 30.5, weight=48.0)
    g.diag(669.6, 175.6, 786.9, -24.8, weight=64.0)
    g.dot(236.6, 649.5, w=92.0, h=119.6, slant=-14.0)
    g.hbar(75.8, 263.3, 394.2, weight=92.0)
    g.diag(263.3, 417.5, 199.1, 256.8, weight=92.0)
    g.diag(199.1, 256.8, 235.6, 82.9, weight=92.0)
    g.hbar(61.0, 293.7, 43.0, weight=48.0)
    g.hbar(293.7, 924.0, 4.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_907f() -> Glyph:
    """避 U+907F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni907F", advance=1000, unicode=0x907F, note="避：自动生成")
    g.hbar(416.3, 570.9, 611.7, weight=96.0)
    g.diag(570.9, 627.1, 508.1, 515.5, weight=96.0)
    g.dot(483.4, 480.1, w=96.0, h=124.8, slant=-14.0)
    g.diag(399.4, 605.4, 373.5, 511.9, weight=48.0)
    g.diag(373.5, 511.9, 258.0, 197.2, weight=48.0)
    g.vbar(399.8, 189.9, 352.9, weight=48.0)
    g.hbar(411.2, 558.6, 350.0, weight=96.0)
    g.diag(558.6, 364.3, 512.2, 258.1, weight=96.0)
    g.dot(492.5, 218.2, w=96.0, h=124.8, slant=-14.0)
    g.diag(640.4, 751.7, 721.1, 705.3, weight=96.0)
    g.diag(721.1, 705.3, 754.3, 631.6, weight=96.0)
    g.hbar(618.0, 813.9, 578.6, weight=96.0)
    g.vbar(814.7, 576.1, 608.3, weight=96.0)
    g.diag(587.2, 498.2, 674.8, 401.5, weight=64.0)
    g.diag(762.1, 570.8, 794.4, 538.5, weight=56.0)
    g.diag(794.4, 538.5, 732.2, 410.5, weight=56.0)
    g.hbar(581.4, 822.4, 386.7, weight=96.0)
    g.diag(822.4, 408.4, 793.4, 432.5, weight=96.0)
    g.hbar(591.9, 827.7, 256.3, weight=96.0)
    g.diag(827.7, 275.6, 868.8, 367.2, weight=96.0)
    g.diag(681.8, 355.0, 714.1, 329.8, weight=96.0)
    g.vbar(710.6, 8.3, 329.8, weight=96.0)
    g.dot(256.8, 666.0, w=96.0, h=124.8, slant=-14.0)
    g.hbar(71.1, 102.3, 417.1, weight=64.0)
    g.diag(102.3, 420.6, 295.5, 207.9, weight=64.0)
    g.diag(295.5, 207.9, 231.6, 151.1, weight=64.0)
    g.hbar(63.0, 311.8, 82.4, weight=96.0)
    g.hbar(311.8, 922.0, 24.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_9084() -> Glyph:
    """還 U+9084 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9084", advance=1000, unicode=0x9084, note="還：自动生成")
    g.vbar(400.1, 546.0, 709.9, weight=84.0)
    g.hbar(397.0, 773.1, 725.2, weight=48.0)
    g.diag(773.1, 746.8, 697.8, 606.4, weight=48.0)
    g.dot(508.9, 654.5, w=84.0, h=100.1, slant=-14.0)
    g.diag(593.5, 722.2, 617.4, 696.3, weight=64.0)
    g.diag(617.4, 696.3, 599.5, 634.6, weight=64.0)
    g.diag(599.5, 634.6, 602.5, 628.6, weight=64.0)
    g.hbar(443.3, 694.5, 592.7, weight=48.0)
    g.hbar(348.7, 823.4, 511.7, weight=56.0)
    g.dot(455.4, 363.0, w=96.0, h=124.8, slant=-14.0)
    g.hbar(456.3, 698.3, 440.8, weight=48.0)
    g.diag(698.3, 460.2, 647.5, 377.6, weight=48.0)
    g.hbar(498.0, 676.5, 351.5, weight=48.0)
    g.hbar(502.2, 598.8, 255.3, weight=48.0)
    g.diag(502.2, 235.5, 313.9, 84.9, weight=48.0)
    g.vbar(518.7, 133.9, 216.0, weight=76.0)
    g.diag(522.9, 133.9, 535.4, 100.2, weight=76.0)
    g.diag(535.4, 100.2, 581.6, 124.9, weight=76.0)
    g.diag(581.6, 124.9, 651.4, 206.7, weight=76.0)
    g.diag(718.8, 342.6, 749.7, 322.1, weight=76.0)
    g.diag(749.7, 322.1, 692.0, 258.4, weight=76.0)
    g.hbar(681.6, 692.0, 259.1, weight=76.0)
    g.diag(607.9, 271.1, 807.5, 102.2, weight=96.0)
    g.diag(139.7, 658.5, 318.3, 507.8, weight=96.0)
    g.hbar(63.1, 261.4, 370.0, weight=96.0)
    g.diag(261.4, 393.0, 208.2, 255.6, weight=96.0)
    g.diag(208.2, 255.6, 255.5, 153.1, weight=96.0)
    g.diag(255.5, 153.1, 227.3, 104.2, weight=96.0)
    g.hbar(64.1, 266.6, 45.7, weight=76.0)
    g.hbar(266.6, 921.9, 4.9, weight=76.0)
    return g
def g_cjk_unified_ideograph_90ed() -> Glyph:
    """郭 U+90ED —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni90ED", advance=1000, unicode=0x90ED, note="郭：自动生成")
    g.diag(388.2, 694.0, 420.8, 755.7, weight=96.0)
    g.diag(420.8, 755.7, 447.7, 705.0, weight=96.0)
    g.hbar(178.7, 518.1, 656.1, weight=64.0)
    g.diag(518.1, 677.1, 574.4, 649.3, weight=64.0)
    g.vbar(307.0, 447.4, 557.1, weight=48.0)
    g.hbar(298.0, 506.5, 564.8, weight=48.0)
    g.diag(506.5, 581.6, 448.1, 502.0, weight=48.0)
    g.hbar(330.3, 342.6, 463.3, weight=48.0)
    g.hbar(342.6, 472.9, 473.4, weight=48.0)
    g.vbar(475.6, 486.1, 503.5, weight=48.0)
    g.hbar(228.4, 495.5, 390.0, weight=48.0)
    g.diag(495.5, 406.2, 410.8, 317.6, weight=48.0)
    g.hbar(395.7, 410.8, 316.2, weight=48.0)
    g.vbar(362.6, 159.6, 319.2, weight=96.0)
    g.hbar(282.1, 362.1, 164.6, weight=96.0)
    g.hbar(154.8, 275.2, 205.0, weight=56.0)
    g.hbar(275.2, 532.2, 255.2, weight=56.0)
    g.hbar(645.2, 822.9, 621.0, weight=76.0)
    g.diag(822.9, 638.9, 725.8, 457.3, weight=76.0)
    g.diag(725.8, 457.3, 889.0, 206.8, weight=76.0)
    g.hbar(651.9, 889.0, 226.7, weight=76.0)
    g.diag(576.9, 636.0, 610.6, 437.4, weight=96.0)
    g.vbar(616.5, -57.0, 437.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_914c() -> Glyph:
    """酌 U+914C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni914C", advance=1000, unicode=0x914C, note="酌：自动生成")
    g.hbar(180.4, 524.2, 670.5, weight=96.0)
    g.vbar(139.8, 369.9, 458.3, weight=48.0)
    g.vbar(121.5, 73.9, 369.9, weight=48.0)
    g.diag(106.9, 73.9, 150.2, 45.4, weight=48.0)
    g.diag(148.0, 447.6, 397.2, 317.9, weight=48.0)
    g.diag(397.2, 317.9, 482.0, 12.4, weight=48.0)
    g.diag(213.8, 629.6, 264.5, 586.5, weight=48.0)
    g.diag(264.5, 586.5, 227.0, 343.3, weight=48.0)
    g.diag(227.0, 343.3, 161.6, 284.0, weight=48.0)
    g.diag(325.5, 647.2, 379.3, 597.5, weight=48.0)
    g.diag(379.3, 597.5, 342.3, 389.4, weight=48.0)
    g.diag(342.3, 389.4, 391.4, 334.9, weight=48.0)
    g.hbar(391.4, 466.4, 336.3, weight=48.0)
    g.hbar(179.5, 446.4, 205.7, weight=96.0)
    g.hbar(161.0, 444.2, 88.4, weight=96.0)
    g.diag(696.3, 792.0, 681.0, 672.9, weight=48.0)
    g.diag(681.0, 672.9, 505.2, 408.1, weight=48.0)
    g.hbar(626.3, 853.3, 496.0, weight=48.0)
    g.vbar(858.3, 314.2, 518.2, weight=48.0)
    g.diag(863.4, 314.2, 797.5, -63.9, weight=48.0)
    g.diag(797.5, -63.9, 668.5, 12.4, weight=48.0)
    g.diag(569.0, 375.8, 697.4, 216.7, weight=92.0)
    return g
def g_cjk_unified_ideograph_914e() -> Glyph:
    """酎 U+914E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni914E", advance=1000, unicode=0x914E, note="酎：自动生成")
    g.hbar(143.0, 165.3, 648.8, weight=96.0)
    g.hbar(143.0, 452.7, 676.1, weight=96.0)
    g.diag(124.5, 490.0, 112.3, 412.5, weight=48.0)
    g.vbar(99.5, 154.5, 412.5, weight=48.0)
    g.diag(86.7, 154.5, 126.0, 83.7, weight=48.0)
    g.diag(126.3, 478.2, 362.4, 351.6, weight=48.0)
    g.diag(362.4, 351.6, 440.9, 48.6, weight=48.0)
    g.diag(200.4, 637.7, 245.8, 591.8, weight=48.0)
    g.diag(245.8, 591.8, 188.2, 329.4, weight=48.0)
    g.hbar(136.2, 188.2, 318.5, weight=48.0)
    g.diag(294.4, 656.8, 334.1, 527.3, weight=48.0)
    g.diag(334.1, 527.3, 422.8, 357.6, weight=48.0)
    g.hbar(144.4, 304.2, 234.5, weight=84.0)
    g.diag(304.2, 245.1, 345.7, 173.4, weight=84.0)
    g.hbar(136.4, 400.0, 112.0, weight=84.0)
    g.hbar(479.1, 942.0, 457.6, weight=96.0)
    g.diag(697.3, 743.0, 733.4, 514.3, weight=96.0)
    g.vbar(726.2, -19.9, 514.3, weight=96.0)
    g.hbar(585.0, 719.0, 7.9, weight=96.0)
    g.hbar(479.1, 585.0, 40.2, weight=96.0)
    g.hbar(464.9, 589.4, 306.7, weight=56.0)
    g.diag(589.4, 284.7, 615.1, 244.1, weight=56.0)
    return g
def g_cjk_unified_ideograph_9162() -> Glyph:
    """酢 U+9162 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9162", advance=1000, unicode=0x9162, note="酢：自动生成")
    g.hbar(160.9, 177.7, 645.0, weight=96.0)
    g.hbar(160.9, 473.5, 674.5, weight=96.0)
    g.diag(155.2, 494.6, 143.2, 416.8, weight=48.0)
    g.vbar(134.7, 141.7, 416.8, weight=48.0)
    g.diag(126.2, 141.7, 150.9, 95.1, weight=48.0)
    g.diag(159.0, 483.2, 374.3, 366.6, weight=48.0)
    g.diag(374.3, 366.6, 434.1, 58.3, weight=48.0)
    g.diag(213.9, 634.3, 257.5, 601.3, weight=48.0)
    g.diag(257.5, 601.3, 220.8, 374.8, weight=48.0)
    g.diag(220.8, 374.8, 163.9, 311.6, weight=48.0)
    g.diag(305.9, 654.5, 329.4, 550.9, weight=48.0)
    g.diag(329.4, 550.9, 363.8, 371.4, weight=48.0)
    g.hbar(363.8, 418.9, 373.9, weight=48.0)
    g.hbar(177.2, 401.3, 244.5, weight=92.0)
    g.diag(162.3, 110.5, 177.4, 124.4, weight=92.0)
    g.hbar(177.4, 394.1, 134.6, weight=92.0)
    g.diag(625.2, 792.0, 670.8, 744.3, weight=96.0)
    g.diag(670.8, 744.3, 476.5, 415.8, weight=96.0)
    g.hbar(574.0, 900.9, 532.5, weight=96.0)
    g.vbar(642.6, 306.4, 483.3, weight=64.0)
    g.vbar(658.0, -52.0, 306.4, weight=64.0)
    g.hbar(687.2, 802.4, 371.6, weight=96.0)
    g.vbar(815.9, 290.6, 384.6, weight=96.0)
    g.diag(688.2, 243.4, 698.9, 234.9, weight=96.0)
    g.hbar(698.9, 827.1, 243.5, weight=96.0)
    g.diag(827.1, 252.2, 840.2, 343.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_916c() -> Glyph:
    """酬 U+916C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni916C", advance=1000, unicode=0x916C, note="酬：自动生成")
    g.hbar(177.1, 430.9, 680.6, weight=96.0)
    g.hbar(430.9, 524.4, 684.3, weight=96.0)
    g.vbar(150.2, 408.0, 496.5, weight=48.0)
    g.vbar(139.7, 163.4, 408.0, weight=48.0)
    g.diag(131.3, 163.4, 159.2, 115.3, weight=48.0)
    g.diag(162.2, 487.1, 376.3, 384.3, weight=48.0)
    g.vbar(401.5, 126.6, 384.3, weight=48.0)
    g.hbar(373.9, 426.7, 134.4, weight=48.0)
    g.diag(211.2, 643.2, 258.5, 604.3, weight=48.0)
    g.diag(258.5, 604.3, 221.8, 384.6, weight=48.0)
    g.diag(221.8, 384.6, 171.0, 333.6, weight=48.0)
    g.diag(306.8, 659.4, 328.6, 565.1, weight=48.0)
    g.diag(328.6, 565.1, 378.7, 359.5, weight=48.0)
    g.hbar(378.7, 418.9, 359.5, weight=48.0)
    g.hbar(181.1, 408.0, 257.5, weight=76.0)
    g.hbar(169.7, 376.9, 146.3, weight=76.0)
    g.diag(457.2, 413.1, 569.3, 318.0, weight=48.0)
    g.diag(552.3, 637.4, 469.6, 5.8, weight=48.0)
    g.diag(614.0, 439.1, 707.2, 368.6, weight=48.0)
    g.diag(695.8, 606.6, 715.3, 470.4, weight=48.0)
    g.vbar(718.0, 137.3, 470.4, weight=48.0)
    g.diag(745.1, 468.9, 849.2, 363.3, weight=48.0)
    g.diag(815.3, 757.0, 852.6, 485.0, weight=48.0)
    g.vbar(854.9, -57.0, 485.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_9175() -> Glyph:
    """酵 U+9175 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9175", advance=1000, unicode=0x9175, note="酵：自动生成")
    g.hbar(159.8, 415.5, 653.1, weight=96.0)
    g.diag(415.5, 680.4, 493.3, 617.7, weight=96.0)
    g.vbar(129.1, 372.5, 472.9, weight=48.0)
    g.vbar(127.2, 85.1, 372.5, weight=48.0)
    g.diag(141.5, 463.9, 336.1, 336.7, weight=48.0)
    g.diag(336.1, 336.7, 402.5, 41.6, weight=48.0)
    g.diag(195.1, 612.2, 255.8, 565.3, weight=48.0)
    g.diag(255.8, 565.3, 146.3, 308.2, weight=48.0)
    g.diag(285.6, 628.4, 304.9, 527.5, weight=48.0)
    g.diag(304.9, 527.5, 333.6, 353.9, weight=48.0)
    g.hbar(333.6, 387.2, 356.8, weight=48.0)
    g.hbar(161.4, 368.0, 237.2, weight=96.0)
    g.hbar(141.7, 361.8, 115.2, weight=96.0)
    g.hbar(519.3, 734.2, 595.8, weight=48.0)
    g.diag(592.3, 787.0, 618.6, 679.7, weight=48.0)
    g.vbar(614.9, 495.3, 679.7, weight=48.0)
    g.hbar(425.6, 927.1, 482.9, weight=48.0)
    g.diag(851.2, 696.5, 719.7, 554.0, weight=48.0)
    g.diag(719.7, 554.0, 425.6, 216.7, weight=48.0)
    g.diag(535.8, 339.7, 531.0, 349.1, weight=64.0)
    g.hbar(531.0, 760.0, 362.6, weight=64.0)
    g.diag(760.0, 376.1, 680.9, 285.8, weight=64.0)
    g.hbar(668.5, 680.9, 284.6, weight=64.0)
    g.vbar(645.8, 44.9, 281.7, weight=64.0)
    g.diag(646.8, 44.9, 574.8, -13.9, weight=64.0)
    g.hbar(451.6, 620.0, 200.5, weight=48.0)
    g.hbar(620.0, 893.0, 210.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_9177() -> Glyph:
    """酷 U+9177 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9177", advance=1000, unicode=0x9177, note="酷：自动生成")
    g.hbar(143.6, 394.9, 662.2, weight=92.0)
    g.diag(394.9, 688.4, 490.0, 638.4, weight=92.0)
    g.diag(120.1, 458.2, 106.1, 379.6, weight=48.0)
    g.vbar(105.9, 193.1, 379.6, weight=48.0)
    g.vbar(112.5, 67.2, 193.1, weight=48.0)
    g.diag(122.8, 445.0, 337.8, 325.3, weight=48.0)
    g.diag(337.8, 325.3, 387.8, 35.6, weight=48.0)
    g.vbar(182.8, 523.3, 623.5, weight=48.0)
    g.diag(188.3, 523.3, 126.1, 291.7, weight=48.0)
    g.diag(281.0, 645.1, 300.2, 538.0, weight=48.0)
    g.diag(300.2, 538.0, 336.4, 332.7, weight=48.0)
    g.hbar(336.4, 383.3, 330.4, weight=48.0)
    g.hbar(144.6, 364.8, 223.3, weight=92.0)
    g.diag(130.3, 82.8, 150.3, 101.6, weight=92.0)
    g.hbar(150.3, 356.2, 106.0, weight=92.0)
    g.diag(465.6, 661.9, 552.9, 578.0, weight=92.0)
    g.diag(552.9, 578.0, 440.2, 422.0, weight=92.0)
    g.hbar(545.7, 812.3, 527.9, weight=92.0)
    g.diag(632.2, 756.8, 677.3, 718.4, weight=92.0)
    g.vbar(671.8, 386.5, 718.4, weight=92.0)
    g.diag(666.4, 386.5, 650.3, 365.5, weight=92.0)
    g.hbar(439.3, 934.0, 332.9, weight=92.0)
    g.diag(530.6, 204.9, 519.7, 185.6, weight=48.0)
    g.vbar(550.4, 18.6, 185.6, weight=48.0)
    g.hbar(536.0, 810.3, 205.6, weight=48.0)
    g.diag(810.3, 215.9, 742.1, 71.7, weight=48.0)
    g.hbar(567.6, 784.8, 48.6, weight=48.0)
    g.vbar(781.8, 52.3, 84.1, weight=48.0)
    return g
def g_cjk_unified_ideograph_9178() -> Glyph:
    """酸 U+9178 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9178", advance=1000, unicode=0x9178, note="酸：自动生成")
    g.hbar(157.7, 356.2, 639.9, weight=96.0)
    g.diag(356.2, 666.1, 336.2, 620.9, weight=96.0)
    g.diag(113.6, 453.5, 103.7, 381.8, weight=48.0)
    g.diag(103.7, 381.8, 67.9, 97.8, weight=48.0)
    g.diag(67.9, 97.8, 103.9, 50.7, weight=48.0)
    g.diag(120.5, 441.8, 335.3, 315.3, weight=48.0)
    g.diag(335.3, 315.3, 425.6, -7.2, weight=48.0)
    g.diag(193.3, 605.0, 207.4, 504.4, weight=48.0)
    g.diag(207.4, 504.4, 180.2, 287.4, weight=48.0)
    g.hbar(131.0, 180.2, 276.6, weight=48.0)
    g.diag(274.1, 625.4, 295.1, 512.9, weight=48.0)
    g.diag(295.1, 512.9, 435.7, 281.6, weight=48.0)
    g.hbar(383.3, 435.7, 287.4, weight=48.0)
    g.hbar(138.3, 369.2, 198.7, weight=84.0)
    g.hbar(115.7, 362.9, 82.4, weight=84.0)
    g.diag(603.7, 783.2, 631.1, 747.4, weight=48.0)
    g.diag(631.1, 747.4, 506.7, 534.6, weight=48.0)
    g.hbar(506.7, 773.0, 558.8, weight=48.0)
    g.diag(708.7, 671.1, 823.8, 525.4, weight=48.0)
    g.diag(558.1, 513.2, 428.0, 325.7, weight=64.0)
    g.diag(693.8, 537.4, 848.3, 382.7, weight=76.0)
    g.diag(628.1, 323.1, 593.8, 356.2, weight=48.0)
    g.diag(593.8, 356.2, 422.2, 155.5, weight=48.0)
    g.diag(568.4, 289.3, 653.2, 220.4, weight=48.0)
    g.diag(653.2, 220.4, 562.8, 12.0, weight=48.0)
    g.hbar(417.1, 562.8, 5.2, weight=48.0)
    g.diag(539.5, 234.0, 942.0, -43.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_9192() -> Glyph:
    """醒 U+9192 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9192", advance=1000, unicode=0x9192, note="醒：自动生成")
    g.hbar(149.9, 476.7, 655.2, weight=96.0)
    g.vbar(107.0, 55.8, 465.8, weight=48.0)
    g.diag(114.5, 456.8, 339.2, 339.0, weight=48.0)
    g.vbar(369.6, 85.2, 339.0, weight=48.0)
    g.diag(399.9, 85.2, 446.9, 9.3, weight=48.0)
    g.vbar(187.8, 516.7, 615.8, weight=48.0)
    g.diag(192.8, 516.7, 128.9, 294.7, weight=48.0)
    g.diag(281.5, 634.2, 308.3, 525.2, weight=48.0)
    g.diag(308.3, 525.2, 346.0, 324.4, weight=48.0)
    g.hbar(346.0, 396.9, 323.1, weight=48.0)
    g.hbar(141.5, 379.1, 208.2, weight=96.0)
    g.hbar(125.9, 369.1, 81.9, weight=96.0)
    g.vbar(551.9, 444.1, 693.7, weight=48.0)
    g.hbar(516.0, 838.3, 698.9, weight=48.0)
    g.vbar(804.7, 468.8, 700.1, weight=48.0)
    g.hbar(591.8, 767.9, 571.4, weight=84.0)
    g.hbar(603.8, 753.4, 466.7, weight=84.0)
    g.vbar(536.4, 328.7, 339.9, weight=96.0)
    g.diag(535.1, 328.7, 456.1, 200.8, weight=96.0)
    g.hbar(552.9, 845.2, 317.6, weight=96.0)
    g.hbar(512.6, 603.8, 179.5, weight=96.0)
    g.hbar(603.8, 761.4, 172.4, weight=96.0)
    g.hbar(713.3, 761.4, 185.8, weight=96.0)
    g.diag(645.5, 435.1, 677.8, 395.5, weight=96.0)
    g.vbar(674.2, 61.5, 395.5, weight=96.0)
    g.diag(670.6, 61.5, 657.6, 44.2, weight=96.0)
    g.hbar(450.6, 927.0, 11.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_919c() -> Glyph:
    """醜 U+919C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni919C", advance=1000, unicode=0x919C, note="醜：自动生成")
    g.diag(158.2, 604.5, 163.3, 615.1, weight=96.0)
    g.hbar(163.3, 393.3, 637.5, weight=96.0)
    g.diag(393.3, 659.8, 453.3, 597.1, weight=96.0)
    g.diag(114.0, 461.1, 23.0, 308.5, weight=48.0)
    g.diag(23.0, 308.5, 116.0, 45.7, weight=48.0)
    g.hbar(122.0, 368.4, 471.7, weight=48.0)
    g.diag(368.4, 492.3, 398.4, 359.0, weight=48.0)
    g.vbar(395.0, 64.8, 359.0, weight=48.0)
    g.diag(391.7, 64.8, 423.8, 28.9, weight=48.0)
    g.diag(192.8, 601.3, 229.6, 561.6, weight=48.0)
    g.diag(229.6, 561.6, 189.9, 320.1, weight=48.0)
    g.diag(189.9, 320.1, 129.4, 263.5, weight=48.0)
    g.diag(281.2, 618.5, 304.7, 506.4, weight=48.0)
    g.diag(304.7, 506.4, 403.9, 307.5, weight=48.0)
    g.hbar(388.3, 403.9, 309.4, weight=48.0)
    g.hbar(141.3, 373.7, 195.9, weight=92.0)
    g.hbar(126.9, 365.1, 72.7, weight=96.0)
    g.diag(630.6, 774.3, 663.3, 742.8, weight=48.0)
    g.diag(663.3, 742.8, 539.8, 567.0, weight=48.0)
    g.vbar(515.5, 327.9, 555.4, weight=48.0)
    g.hbar(523.2, 633.4, 561.1, weight=48.0)
    g.hbar(633.4, 836.9, 572.7, weight=48.0)
    g.vbar(792.4, 365.0, 582.7, weight=48.0)
    g.hbar(542.9, 758.3, 454.1, weight=76.0)
    g.diag(620.2, 548.5, 641.4, 532.1, weight=56.0)
    g.vbar(646.6, 414.8, 532.1, weight=56.0)
    g.diag(651.9, 414.8, 631.7, 383.0, weight=56.0)
    g.diag(554.6, 341.4, 561.9, 348.7, weight=56.0)
    g.hbar(561.9, 739.7, 363.0, weight=56.0)
    g.diag(550.5, 315.4, 582.9, 274.9, weight=96.0)
    g.diag(582.9, 274.9, 436.6, 41.6, weight=96.0)
    g.diag(638.5, 342.5, 701.0, -14.2, weight=48.0)
    g.hbar(701.0, 955.9, -11.0, weight=48.0)
    g.diag(955.9, -7.8, 898.8, 126.2, weight=48.0)
    g.diag(763.2, 337.9, 798.0, 262.7, weight=48.0)
    g.diag(798.0, 262.7, 724.1, 116.5, weight=48.0)
    g.hbar(724.1, 853.7, 127.1, weight=48.0)
    g.diag(840.8, 158.7, 876.2, 138.4, weight=48.0)
    g.diag(876.2, 138.4, 862.7, 122.1, weight=48.0)
    return g
def g_cjk_unified_ideograph_91dc() -> Glyph:
    """釜 U+91DC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni91DC", advance=1000, unicode=0x91DC, note="釜：自动生成")
    g.vbar(314.3, 629.6, 689.3, weight=96.0)
    g.diag(316.2, 689.3, 163.9, 559.1, weight=96.0)
    g.hbar(521.7, 671.6, 693.7, weight=96.0)
    g.diag(671.6, 696.9, 721.5, 638.2, weight=96.0)
    g.diag(505.0, 656.0, 400.1, 524.2, weight=48.0)
    g.diag(400.1, 524.2, 63.0, 289.6, weight=48.0)
    g.hbar(289.5, 937.0, 502.6, weight=56.0)
    g.hbar(298.8, 598.5, 397.8, weight=48.0)
    g.diag(255.4, 185.8, 281.4, 203.1, weight=96.0)
    g.hbar(281.4, 591.5, 225.4, weight=96.0)
    g.diag(591.5, 247.6, 608.2, 210.6, weight=96.0)
    g.diag(414.6, 334.2, 481.4, 99.3, weight=76.0)
    g.diag(481.4, 99.3, 432.5, 41.3, weight=76.0)
    g.dot(302.2, 106.4, w=96.0, h=124.8, slant=-14.0)
    g.diag(574.2, 214.5, 596.5, 160.0, weight=76.0)
    g.diag(596.5, 160.0, 537.9, 88.5, weight=76.0)
    g.vbar(538.8, 51.0, 88.5, weight=76.0)
    g.hbar(143.4, 774.1, 4.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_91e3() -> Glyph:
    """釣 U+91E3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni91E3", advance=1000, unicode=0x91E3, note="釣：自动生成")
    g.vbar(374.2, 682.8, 704.2, weight=96.0)
    g.diag(373.3, 704.2, 145.0, 341.2, weight=96.0)
    g.diag(145.0, 341.2, 180.5, 298.3, weight=96.0)
    g.hbar(388.4, 467.5, 636.0, weight=96.0)
    g.diag(467.5, 625.2, 481.6, 511.3, weight=96.0)
    g.hbar(255.1, 440.6, 451.0, weight=92.0)
    g.hbar(440.6, 527.6, 449.2, weight=92.0)
    g.hbar(211.6, 500.2, 312.1, weight=92.0)
    g.diag(343.7, 412.1, 378.7, 389.4, weight=64.0)
    g.vbar(365.4, 114.1, 389.4, weight=64.0)
    g.dot(263.5, 195.3, w=96.0, h=124.8, slant=-14.0)
    g.diag(480.8, 282.1, 492.0, 254.7, weight=48.0)
    g.diag(492.0, 254.7, 387.9, 190.3, weight=48.0)
    g.hbar(142.6, 265.2, 52.2, weight=56.0)
    g.hbar(265.2, 521.4, 107.6, weight=56.0)
    g.vbar(670.6, 662.0, 792.0, weight=48.0)
    g.diag(663.4, 662.0, 509.0, 369.1, weight=48.0)
    g.diag(624.4, 474.4, 828.3, 304.5, weight=48.0)
    g.vbar(817.4, -64.6, 304.5, weight=48.0)
    g.diag(806.4, -64.6, 696.9, 3.6, weight=48.0)
    g.hbar(692.1, 696.9, 4.2, weight=48.0)
    g.diag(563.3, 353.1, 690.0, 236.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_920d() -> Glyph:
    """鈍 U+920D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni920D", advance=1000, unicode=0x920D, note="鈍：自动生成")
    g.diag(341.3, 675.1, 334.7, 713.1, weight=96.0)
    g.diag(334.7, 713.1, 122.2, 364.7, weight=96.0)
    g.diag(122.2, 364.7, 140.9, 289.2, weight=96.0)
    g.diag(350.9, 640.1, 454.7, 591.4, weight=96.0)
    g.vbar(450.4, 490.1, 591.4, weight=96.0)
    g.hbar(208.1, 493.7, 432.6, weight=96.0)
    g.hbar(172.6, 469.7, 286.0, weight=96.0)
    g.diag(285.9, 399.2, 307.3, 279.8, weight=56.0)
    g.vbar(304.3, 88.9, 279.8, weight=56.0)
    g.diag(172.8, 239.4, 269.0, 111.7, weight=76.0)
    g.diag(411.2, 304.0, 432.5, 231.2, weight=48.0)
    g.diag(432.5, 231.2, 335.4, 153.7, weight=48.0)
    g.hbar(110.5, 170.9, 21.8, weight=96.0)
    g.hbar(170.9, 387.7, 56.2, weight=96.0)
    g.diag(387.7, 98.9, 424.8, 160.2, weight=96.0)
    g.diag(516.9, 388.7, 549.4, 426.6, weight=96.0)
    g.hbar(549.4, 742.6, 455.9, weight=96.0)
    g.hbar(742.6, 811.2, 473.9, weight=96.0)
    g.hbar(471.0, 535.0, 328.0, weight=84.0)
    g.vbar(529.8, 184.1, 317.6, weight=84.0)
    g.hbar(524.6, 782.9, 225.5, weight=84.0)
    g.diag(812.3, 457.2, 845.1, 377.1, weight=96.0)
    g.diag(845.1, 377.1, 784.6, 223.0, weight=96.0)
    g.diag(630.5, 741.8, 705.1, 408.4, weight=96.0)
    g.diag(705.1, 408.4, 928.3, -72.0, weight=96.0)
    g.vbar(936.2, -72.0, 145.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_925b() -> Glyph:
    """鉛 U+925B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni925B", advance=1000, unicode=0x925B, note="鉛：自动生成")
    g.diag(361.1, 679.2, 355.4, 693.7, weight=96.0)
    g.diag(355.4, 693.7, 119.3, 316.5, weight=96.0)
    g.diag(119.3, 316.5, 150.1, 276.8, weight=96.0)
    g.hbar(379.8, 392.5, 646.8, weight=96.0)
    g.diag(392.5, 648.0, 472.4, 602.7, weight=96.0)
    g.hbar(472.4, 529.7, 602.4, weight=96.0)
    g.hbar(239.4, 381.3, 428.7, weight=96.0)
    g.diag(381.3, 444.7, 431.5, 374.4, weight=96.0)
    g.hbar(187.3, 413.9, 290.1, weight=84.0)
    g.hbar(413.9, 462.9, 329.1, weight=84.0)
    g.diag(301.4, 394.1, 336.9, 367.6, weight=56.0)
    g.vbar(325.4, 102.9, 367.6, weight=56.0)
    g.diag(187.3, 243.8, 289.1, 121.0, weight=64.0)
    g.diag(423.6, 263.6, 434.3, 246.0, weight=48.0)
    g.diag(434.3, 246.0, 348.7, 181.1, weight=48.0)
    g.hbar(140.0, 193.6, 37.0, weight=96.0)
    g.hbar(193.6, 523.3, 90.9, weight=96.0)
    g.vbar(561.6, 323.1, 615.0, weight=64.0)
    g.hbar(459.3, 534.1, 322.9, weight=64.0)
    g.diag(614.6, 612.5, 626.0, 607.1, weight=96.0)
    g.hbar(626.0, 795.2, 621.6, weight=96.0)
    g.vbar(766.9, 387.6, 636.0, weight=96.0)
    g.hbar(738.5, 947.0, 384.6, weight=96.0)
    g.diag(562.4, 233.6, 550.0, 215.7, weight=48.0)
    g.vbar(575.5, 6.3, 215.7, weight=48.0)
    g.hbar(566.4, 853.7, 235.1, weight=48.0)
    g.diag(853.7, 246.5, 772.3, 75.7, weight=48.0)
    g.hbar(602.1, 850.5, 34.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_9280() -> Glyph:
    """銀 U+9280 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9280", advance=1000, unicode=0x9280, note="銀：自动生成")
    g.vbar(323.2, 652.8, 671.1, weight=96.0)
    g.diag(322.4, 671.1, 109.6, 322.2, weight=96.0)
    g.diag(109.6, 322.2, 130.4, 291.4, weight=96.0)
    g.hbar(328.5, 466.0, 609.7, weight=56.0)
    g.diag(195.2, 409.4, 416.7, 526.9, weight=96.0)
    g.hbar(143.3, 374.2, 320.7, weight=96.0)
    g.diag(374.2, 326.4, 412.6, 306.1, weight=96.0)
    g.diag(273.6, 398.6, 304.5, 374.6, weight=56.0)
    g.vbar(291.5, 113.0, 374.6, weight=56.0)
    g.diag(166.3, 268.3, 252.9, 128.2, weight=64.0)
    g.diag(404.3, 315.2, 417.7, 243.8, weight=48.0)
    g.diag(417.7, 243.8, 357.1, 139.0, weight=48.0)
    g.hbar(85.4, 217.7, 62.9, weight=48.0)
    g.hbar(217.7, 500.7, 110.0, weight=48.0)
    g.hbar(530.4, 695.2, 610.8, weight=48.0)
    g.diag(695.2, 637.0, 733.0, 599.8, weight=48.0)
    g.diag(733.0, 599.8, 682.6, 378.9, weight=48.0)
    g.hbar(659.0, 682.6, 379.2, weight=48.0)
    g.diag(551.0, 464.3, 588.2, 486.8, weight=76.0)
    g.hbar(588.2, 678.4, 485.9, weight=76.0)
    g.dot(598.5, 374.1, w=84.0, h=100.3, slant=-14.0)
    g.vbar(516.2, -29.4, 602.5, weight=48.0)
    g.diag(504.8, -29.4, 661.7, 85.0, weight=48.0)
    g.diag(720.3, 377.1, 775.6, 329.1, weight=96.0)
    g.diag(775.6, 329.1, 663.7, 227.1, weight=96.0)
    g.diag(546.4, 297.5, 942.0, 76.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_9283() -> Glyph:
    """銃 U+9283 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9283", advance=1000, unicode=0x9283, note="銃：自动生成")
    g.diag(307.2, 757.1, 353.3, 700.4, weight=96.0)
    g.diag(353.3, 700.4, 68.0, 310.4, weight=96.0)
    g.dot(397.7, 602.2, w=96.0, h=117.7, slant=-14.0)
    g.hbar(199.9, 413.5, 441.2, weight=96.0)
    g.hbar(170.2, 413.5, 306.3, weight=96.0)
    g.diag(271.4, 405.4, 299.3, 384.2, weight=56.0)
    g.vbar(295.5, 105.6, 384.2, weight=56.0)
    g.diag(291.6, 105.6, 278.6, 94.7, weight=56.0)
    g.dot(174.8, 168.8, w=96.0, h=97.0, slant=-14.0)
    g.diag(407.4, 253.1, 419.6, 233.7, weight=48.0)
    g.diag(419.6, 233.7, 354.2, 141.7, weight=48.0)
    g.hbar(87.4, 146.7, 22.1, weight=96.0)
    g.hbar(146.7, 434.0, 67.6, weight=96.0)
    g.dot(651.7, 738.7, w=96.0, h=124.8, slant=-14.0)
    g.hbar(519.8, 841.8, 586.9, weight=96.0)
    g.diag(610.8, 538.3, 642.6, 507.6, weight=48.0)
    g.diag(642.6, 507.6, 535.0, 326.2, weight=48.0)
    g.hbar(535.0, 793.3, 366.2, weight=48.0)
    g.hbar(769.2, 793.3, 401.3, weight=48.0)
    g.diag(742.7, 464.7, 817.3, 349.2, weight=48.0)
    g.diag(563.8, 248.0, 597.8, 204.1, weight=96.0)
    g.diag(597.8, 204.1, 383.0, -72.0, weight=96.0)
    g.diag(383.0, -72.0, 390.0, -54.6, weight=96.0)
    g.diag(696.7, 295.0, 940.5, -73.1, weight=64.0)
    g.vbar(941.2, -73.1, 111.0, weight=64.0)
    return g
def g_cjk_unified_ideograph_9285() -> Glyph:
    """銅 U+9285 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9285", advance=1000, unicode=0x9285, note="銅：自动生成")
    g.diag(362.2, 661.8, 358.2, 680.8, weight=96.0)
    g.diag(358.2, 680.8, 58.0, 284.1, weight=96.0)
    g.diag(374.6, 628.1, 383.7, 613.3, weight=96.0)
    g.hbar(383.7, 481.5, 593.7, weight=96.0)
    g.hbar(223.2, 398.6, 421.3, weight=96.0)
    g.diag(398.6, 442.5, 454.3, 515.6, weight=96.0)
    g.hbar(203.2, 408.5, 279.9, weight=96.0)
    g.diag(408.5, 321.2, 447.7, 289.6, weight=96.0)
    g.diag(323.4, 399.2, 339.8, 281.4, weight=48.0)
    g.vbar(335.4, 91.4, 281.4, weight=48.0)
    g.diag(207.1, 250.5, 304.9, 112.8, weight=64.0)
    g.diag(431.6, 301.3, 449.0, 229.7, weight=48.0)
    g.diag(449.0, 229.7, 366.3, 164.7, weight=48.0)
    g.hbar(127.8, 178.4, 27.7, weight=96.0)
    g.hbar(178.4, 505.1, 71.3, weight=96.0)
    g.vbar(548.4, 431.0, 586.8, weight=48.0)
    g.vbar(537.7, -24.7, 431.0, weight=48.0)
    g.hbar(557.3, 838.6, 598.0, weight=48.0)
    g.diag(838.6, 620.1, 890.4, 418.4, weight=48.0)
    g.vbar(869.9, -8.5, 418.4, weight=48.0)
    g.diag(849.4, -8.5, 801.9, 16.3, weight=48.0)
    g.hbar(596.1, 872.0, 459.7, weight=96.0)
    g.vbar(652.8, 154.5, 321.2, weight=48.0)
    g.hbar(644.9, 806.6, 317.0, weight=48.0)
    g.diag(806.6, 324.2, 753.5, 210.2, weight=48.0)
    g.diag(680.9, 169.2, 693.2, 183.7, weight=96.0)
    g.hbar(693.2, 793.0, 191.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_9298() -> Glyph:
    """銘 U+9298 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9298", advance=1000, unicode=0x9298, note="銘：自动生成")
    g.diag(406.1, 717.1, 401.3, 728.2, weight=96.0)
    g.diag(401.3, 728.2, 45.3, 220.4, weight=96.0)
    g.diag(45.3, 220.4, 90.1, 310.1, weight=96.0)
    g.diag(424.7, 684.8, 578.0, 584.4, weight=96.0)
    g.hbar(270.2, 451.4, 469.5, weight=96.0)
    g.hbar(451.4, 496.7, 484.8, weight=96.0)
    g.hbar(246.1, 444.4, 334.5, weight=96.0)
    g.diag(444.4, 372.4, 478.5, 354.5, weight=96.0)
    g.vbar(379.2, 158.5, 447.3, weight=64.0)
    g.dot(288.7, 235.4, w=96.0, h=124.8, slant=-14.0)
    g.diag(475.3, 353.1, 496.5, 294.0, weight=48.0)
    g.diag(496.5, 294.0, 458.1, 186.2, weight=48.0)
    g.hbar(146.4, 204.8, 79.7, weight=96.0)
    g.hbar(204.8, 493.0, 120.5, weight=96.0)
    g.diag(681.6, 797.0, 655.1, 678.4, weight=48.0)
    g.diag(655.1, 678.4, 486.4, 390.4, weight=48.0)
    g.diag(652.9, 593.7, 679.3, 429.5, weight=48.0)
    g.diag(679.3, 429.5, 310.4, -42.0, weight=48.0)
    g.dot(613.0, 420.5, w=96.0, h=124.8, slant=-14.0)
    g.vbar(632.8, 1.2, 208.3, weight=48.0)
    g.hbar(635.4, 860.8, 207.2, weight=48.0)
    g.diag(860.8, 234.0, 897.2, 192.8, weight=48.0)
    g.diag(897.2, 192.8, 836.2, 77.4, weight=48.0)
    g.hbar(660.4, 871.9, 40.1, weight=48.0)
    g.vbar(872.3, 62.9, 91.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_92fc() -> Glyph:
    """鋼 U+92FC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni92FC", advance=1000, unicode=0x92FC, note="鋼：自动生成")
    g.vbar(332.2, 666.8, 699.8, weight=96.0)
    g.diag(331.5, 699.8, 96.2, 318.8, weight=96.0)
    g.diag(96.2, 318.8, 119.0, 239.3, weight=96.0)
    g.vbar(345.3, 617.7, 629.9, weight=96.0)
    g.hbar(347.4, 455.1, 598.8, weight=96.0)
    g.hbar(215.9, 372.6, 440.5, weight=96.0)
    g.diag(372.6, 457.2, 422.5, 525.8, weight=96.0)
    g.hbar(169.5, 362.0, 282.9, weight=96.0)
    g.hbar(362.0, 421.3, 310.4, weight=96.0)
    g.diag(281.7, 401.1, 321.6, 378.7, weight=64.0)
    g.vbar(307.8, 94.0, 378.7, weight=64.0)
    g.diag(179.1, 258.3, 210.0, 153.9, weight=76.0)
    g.diag(210.0, 153.9, 265.0, 108.1, weight=76.0)
    g.diag(411.8, 306.4, 432.6, 241.1, weight=48.0)
    g.diag(432.6, 241.1, 330.1, 167.6, weight=48.0)
    g.hbar(104.3, 157.6, 25.6, weight=96.0)
    g.hbar(157.6, 474.4, 66.4, weight=96.0)
    g.vbar(524.3, 434.7, 584.1, weight=48.0)
    g.vbar(509.9, -2.1, 434.7, weight=48.0)
    g.diag(535.5, 572.6, 821.1, 383.6, weight=48.0)
    g.diag(821.1, 383.6, 887.5, 71.7, weight=48.0)
    g.diag(887.5, 71.7, 807.0, -7.2, weight=48.0)
    g.diag(606.1, 550.7, 701.1, 423.8, weight=64.0)
    g.diag(753.3, 590.3, 784.4, 526.2, weight=48.0)
    g.diag(784.4, 526.2, 732.5, 394.6, weight=48.0)
    g.hbar(568.3, 784.6, 370.8, weight=96.0)
    g.diag(784.6, 385.1, 818.3, 362.2, weight=96.0)
    g.diag(691.1, 344.7, 707.6, 326.2, weight=96.0)
    g.vbar(709.4, 219.8, 326.2, weight=96.0)
    g.diag(711.2, 219.8, 693.1, 206.2, weight=96.0)
    g.diag(553.9, 278.9, 617.2, 241.1, weight=64.0)
    g.vbar(616.1, 164.0, 241.1, weight=64.0)
    g.hbar(615.1, 793.0, 185.3, weight=64.0)
    g.diag(805.0, 362.6, 832.6, 292.4, weight=76.0)
    g.diag(832.6, 292.4, 796.8, 171.4, weight=76.0)
    return g
def g_cjk_unified_ideograph_9320() -> Glyph:
    """錠 U+9320 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9320", advance=1000, unicode=0x9320, note="錠：自动生成")
    g.vbar(298.9, 646.8, 661.0, weight=96.0)
    g.diag(298.2, 661.0, 109.2, 358.7, weight=96.0)
    g.diag(109.2, 358.7, 144.0, 316.7, weight=96.0)
    g.dot(373.8, 576.3, w=96.0, h=124.8, slant=-14.0)
    g.hbar(199.4, 416.2, 432.0, weight=92.0)
    g.diag(172.1, 267.2, 346.2, 346.3, weight=92.0)
    g.diag(346.2, 346.3, 386.0, 321.9, weight=92.0)
    g.diag(274.3, 411.1, 289.4, 320.7, weight=48.0)
    g.vbar(285.7, 131.9, 320.7, weight=48.0)
    g.dot(210.1, 213.9, w=96.0, h=124.8, slant=-14.0)
    g.diag(381.8, 326.8, 398.4, 264.2, weight=48.0)
    g.diag(398.4, 264.2, 315.9, 203.5, weight=48.0)
    g.diag(201.3, 144.2, 175.7, 67.9, weight=96.0)
    g.hbar(175.7, 421.1, 107.7, weight=96.0)
    g.diag(578.3, 709.6, 654.0, 664.0, weight=84.0)
    g.diag(654.0, 664.0, 682.3, 572.8, weight=84.0)
    g.dot(446.7, 442.0, w=96.0, h=124.8, slant=14.0)
    g.hbar(499.8, 820.9, 518.2, weight=96.0)
    g.diag(820.9, 547.7, 743.1, 436.6, weight=96.0)
    g.hbar(483.9, 735.6, 389.7, weight=96.0)
    g.diag(599.3, 349.0, 624.8, 329.0, weight=96.0)
    g.vbar(624.8, 160.1, 329.0, weight=96.0)
    g.diag(624.8, 160.1, 641.2, 132.7, weight=96.0)
    g.dot(714.3, 248.2, w=96.0, h=123.0, slant=-14.0)
    g.hbar(436.8, 512.0, 249.9, weight=96.0)
    g.diag(512.0, 233.9, 396.2, 46.4, weight=96.0)
    g.diag(396.2, 46.4, 315.0, 83.1, weight=96.0)
    g.vbar(528.3, 153.2, 193.0, weight=96.0)
    g.hbar(534.9, 937.0, 92.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_9326() -> Glyph:
    """錦 U+9326 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9326", advance=1000, unicode=0x9326, note="錦：自动生成")
    g.diag(375.4, 713.8, 371.3, 736.3, weight=96.0)
    g.diag(371.3, 736.3, 158.1, 399.5, weight=96.0)
    g.diag(158.1, 399.5, 199.7, 370.6, weight=96.0)
    g.dot(442.3, 645.9, w=96.0, h=124.8, slant=-14.0)
    g.hbar(270.8, 409.0, 501.6, weight=92.0)
    g.diag(409.0, 511.7, 450.9, 446.2, weight=92.0)
    g.hbar(228.3, 417.4, 373.5, weight=92.0)
    g.hbar(417.4, 455.5, 397.8, weight=92.0)
    g.diag(329.7, 469.4, 364.6, 444.2, weight=48.0)
    g.vbar(354.5, 202.1, 444.2, weight=48.0)
    g.diag(227.5, 339.4, 317.4, 217.9, weight=64.0)
    g.diag(440.8, 388.9, 459.3, 334.3, weight=48.0)
    g.diag(459.3, 334.3, 377.6, 272.3, weight=48.0)
    g.diag(251.9, 207.3, 216.1, 128.2, weight=96.0)
    g.hbar(216.1, 509.8, 183.2, weight=96.0)
    g.diag(659.8, 792.0, 692.8, 765.2, weight=96.0)
    g.diag(692.8, 765.2, 606.0, 613.7, weight=96.0)
    g.vbar(552.9, 587.8, 598.3, weight=48.0)
    g.vbar(572.3, 402.1, 587.8, weight=48.0)
    g.hbar(566.7, 847.9, 613.5, weight=48.0)
    g.vbar(821.6, 442.8, 634.1, weight=48.0)
    g.hbar(774.7, 795.2, 443.6, weight=48.0)
    g.diag(597.1, 505.0, 608.5, 515.6, weight=64.0)
    g.hbar(608.5, 793.6, 521.1, weight=64.0)
    g.diag(604.1, 417.8, 615.2, 427.1, weight=64.0)
    g.hbar(615.2, 770.0, 440.1, weight=64.0)
    g.vbar(535.5, 160.8, 303.5, weight=96.0)
    g.diag(529.7, 160.8, 495.9, 204.8, weight=96.0)
    g.diag(572.5, 281.3, 594.0, 298.7, weight=96.0)
    g.hbar(594.0, 876.3, 319.4, weight=96.0)
    g.vbar(862.3, 131.9, 340.2, weight=96.0)
    g.hbar(730.7, 848.3, 153.2, weight=96.0)
    g.diag(655.2, 417.8, 683.3, 286.4, weight=48.0)
    g.vbar(687.3, -52.0, 286.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_932f() -> Glyph:
    """錯 U+932F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni932F", advance=1000, unicode=0x932F, note="錯：自动生成")
    g.vbar(313.0, 679.0, 699.5, weight=96.0)
    g.diag(313.2, 699.5, 96.1, 352.6, weight=96.0)
    g.diag(96.1, 352.6, 134.8, 307.0, weight=96.0)
    g.diag(327.6, 643.6, 477.0, 525.5, weight=96.0)
    g.hbar(199.6, 462.7, 458.2, weight=96.0)
    g.hbar(160.4, 426.5, 293.5, weight=64.0)
    g.diag(275.2, 413.4, 316.4, 377.7, weight=64.0)
    g.vbar(301.5, 128.2, 377.7, weight=64.0)
    g.diag(164.7, 267.9, 261.5, 137.1, weight=64.0)
    g.hbar(399.7, 423.4, 253.3, weight=48.0)
    g.diag(399.7, 252.3, 322.4, 192.3, weight=48.0)
    g.hbar(113.2, 447.1, 115.5, weight=56.0)
    g.diag(541.6, 496.2, 551.2, 488.4, weight=96.0)
    g.hbar(551.2, 767.3, 515.4, weight=96.0)
    g.vbar(767.1, 542.4, 556.1, weight=96.0)
    g.hbar(463.7, 568.8, 613.6, weight=96.0)
    g.vbar(577.1, 385.3, 618.0, weight=96.0)
    g.diag(585.4, 385.3, 571.6, 373.9, weight=96.0)
    g.diag(713.9, 777.0, 657.4, 362.8, weight=92.0)
    g.diag(657.4, 362.8, 685.3, 390.7, weight=92.0)
    g.hbar(447.0, 936.2, 360.0, weight=96.0)
    g.diag(530.7, 244.7, 512.9, 206.1, weight=48.0)
    g.vbar(524.6, -7.0, 206.1, weight=48.0)
    g.hbar(541.4, 734.0, 256.7, weight=48.0)
    g.vbar(747.6, 166.4, 274.3, weight=48.0)
    g.vbar(767.2, -52.0, 166.4, weight=48.0)
    g.hbar(558.8, 738.6, 130.3, weight=84.0)
    g.diag(551.9, 4.3, 568.8, 21.3, weight=92.0)
    g.hbar(568.8, 725.7, 21.9, weight=92.0)
    return g
def g_cjk_unified_ideograph_9332() -> Glyph:
    """録 U+9332 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9332", advance=1000, unicode=0x9332, note="録：自动生成")
    g.vbar(313.7, 589.1, 594.1, weight=96.0)
    g.diag(314.1, 589.1, 87.2, 314.7, weight=96.0)
    g.hbar(87.2, 149.5, 310.1, weight=96.0)
    g.hbar(330.2, 391.5, 546.9, weight=96.0)
    g.vbar(394.4, 454.9, 534.2, weight=96.0)
    g.hbar(208.5, 416.8, 402.8, weight=64.0)
    g.hbar(181.5, 351.1, 305.6, weight=64.0)
    g.diag(351.1, 334.1, 388.5, 316.9, weight=64.0)
    g.diag(273.6, 373.9, 298.8, 357.8, weight=64.0)
    g.vbar(295.6, 172.8, 357.8, weight=64.0)
    g.diag(292.4, 172.8, 281.6, 163.1, weight=64.0)
    g.diag(183.3, 284.5, 265.0, 174.9, weight=48.0)
    g.diag(388.6, 316.4, 400.9, 273.9, weight=48.0)
    g.diag(400.9, 273.9, 367.9, 184.7, weight=48.0)
    g.diag(201.6, 173.5, 175.5, 101.3, weight=96.0)
    g.hbar(175.5, 423.2, 140.7, weight=96.0)
    g.diag(566.0, 665.3, 586.6, 630.3, weight=48.0)
    g.diag(586.6, 630.3, 515.7, 485.6, weight=48.0)
    g.hbar(515.7, 674.4, 499.3, weight=48.0)
    g.hbar(583.5, 739.3, 589.4, weight=48.0)
    g.diag(739.3, 596.6, 653.7, 446.5, weight=48.0)
    g.hbar(449.0, 872.5, 410.3, weight=96.0)
    g.diag(584.8, 401.8, 604.9, 285.9, weight=48.0)
    g.vbar(602.1, 36.9, 285.9, weight=48.0)
    g.diag(599.4, 36.9, 481.5, 130.1, weight=48.0)
    g.dot(506.8, 315.3, w=96.0, h=124.8, slant=-14.0)
    g.hbar(425.4, 471.4, 154.9, weight=48.0)
    g.diag(471.4, 146.7, 597.9, 246.4, weight=48.0)
    g.diag(742.3, 357.8, 755.7, 330.1, weight=48.0)
    g.diag(755.7, 330.1, 676.1, 262.4, weight=48.0)
    g.hbar(642.4, 947.0, 213.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_934b() -> Glyph:
    """鍋 U+934B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni934B", advance=1000, unicode=0x934B, note="鍋：自动生成")
    g.diag(285.3, 760.4, 330.9, 705.8, weight=96.0)
    g.diag(330.9, 705.8, 58.0, 303.7, weight=96.0)
    g.hbar(330.9, 348.9, 634.6, weight=96.0)
    g.diag(348.9, 636.2, 449.9, 563.9, weight=96.0)
    g.hbar(197.1, 413.8, 450.8, weight=96.0)
    g.hbar(180.1, 395.7, 311.1, weight=96.0)
    g.diag(274.6, 416.3, 312.4, 385.1, weight=64.0)
    g.vbar(306.0, 116.5, 385.1, weight=64.0)
    g.diag(299.7, 116.5, 288.4, 106.2, weight=64.0)
    g.dot(175.3, 175.2, w=76.0, h=98.8, slant=-14.0)
    g.diag(392.5, 262.3, 409.5, 241.1, weight=48.0)
    g.diag(409.5, 241.1, 363.8, 178.4, weight=48.0)
    g.hbar(76.1, 136.6, 14.3, weight=96.0)
    g.hbar(136.6, 437.1, 73.3, weight=96.0)
    g.diag(506.2, 677.5, 585.2, 371.6, weight=48.0)
    g.diag(585.2, 371.6, 561.4, 355.8, weight=48.0)
    g.hbar(564.6, 586.9, 667.6, weight=48.0)
    g.hbar(586.9, 787.4, 687.4, weight=48.0)
    g.diag(787.4, 711.6, 830.3, 677.3, weight=48.0)
    g.diag(830.3, 677.3, 793.9, 407.8, weight=48.0)
    g.diag(793.9, 407.8, 768.5, 385.5, weight=48.0)
    g.diag(641.0, 544.8, 669.3, 523.0, weight=48.0)
    g.vbar(674.9, 383.5, 523.0, weight=48.0)
    g.diag(680.4, 383.5, 670.8, 371.7, weight=48.0)
    g.diag(701.6, 515.0, 710.7, 526.1, weight=96.0)
    g.hbar(710.7, 778.0, 540.2, weight=96.0)
    g.diag(455.2, 331.3, 475.6, 255.7, weight=48.0)
    g.vbar(479.2, -13.8, 255.7, weight=48.0)
    g.hbar(501.9, 633.7, 332.5, weight=48.0)
    g.diag(633.7, 335.8, 837.7, 226.3, weight=48.0)
    g.diag(837.7, 226.3, 891.0, -45.0, weight=48.0)
    g.diag(891.0, -45.0, 783.3, 10.6, weight=48.0)
    g.diag(559.2, 243.2, 608.1, 80.7, weight=48.0)
    g.diag(610.2, 236.8, 614.5, 233.6, weight=48.0)
    g.hbar(614.5, 767.0, 241.7, weight=48.0)
    g.diag(767.0, 249.9, 748.3, 177.3, weight=48.0)
    g.diag(748.3, 177.3, 728.1, 165.7, weight=48.0)
    g.hbar(625.1, 785.4, 116.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_935b() -> Glyph:
    """鍛 U+935B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni935B", advance=1000, unicode=0x935B, note="鍛：自动生成")
    g.diag(306.6, 690.9, 300.9, 675.0, weight=96.0)
    g.diag(300.9, 675.0, 88.2, 337.8, weight=96.0)
    g.hbar(88.2, 121.7, 331.6, weight=96.0)
    g.dot(365.1, 629.8, w=96.0, h=99.1, slant=-14.0)
    g.hbar(191.5, 421.2, 464.6, weight=84.0)
    g.hbar(133.4, 212.8, 340.1, weight=84.0)
    g.hbar(212.8, 326.8, 351.2, weight=84.0)
    g.diag(326.8, 372.5, 367.6, 350.5, weight=84.0)
    g.diag(262.4, 435.5, 298.6, 405.5, weight=48.0)
    g.vbar(287.4, 175.5, 405.5, weight=48.0)
    g.diag(158.1, 298.6, 222.4, 164.1, weight=76.0)
    g.diag(363.0, 357.3, 381.5, 295.6, weight=48.0)
    g.diag(381.5, 295.6, 310.1, 232.7, weight=48.0)
    g.hbar(103.4, 151.6, 106.5, weight=56.0)
    g.hbar(151.6, 440.3, 155.6, weight=56.0)
    g.diag(546.5, 693.3, 565.3, 660.7, weight=48.0)
    g.diag(565.3, 660.7, 454.8, 553.4, weight=48.0)
    g.diag(411.4, 586.6, 442.7, 385.6, weight=48.0)
    g.vbar(444.6, -29.8, 385.6, weight=48.0)
    g.dot(528.0, 428.5, w=96.0, h=103.2, slant=-14.0)
    g.diag(487.2, 295.6, 498.1, 313.2, weight=92.0)
    g.hbar(498.1, 580.2, 311.3, weight=92.0)
    g.diag(331.7, 157.8, 391.0, 115.7, weight=48.0)
    g.diag(391.0, 115.7, 595.8, 261.5, weight=48.0)
    g.diag(646.4, 613.7, 606.0, 361.3, weight=64.0)
    g.diag(668.9, 601.5, 680.6, 619.1, weight=96.0)
    g.hbar(680.6, 804.9, 624.6, weight=96.0)
    g.vbar(772.8, 451.7, 630.1, weight=96.0)
    g.hbar(740.6, 909.0, 454.3, weight=96.0)
    g.diag(590.2, 327.1, 684.8, 266.2, weight=48.0)
    g.diag(684.8, 266.2, 473.2, 78.0, weight=48.0)
    g.diag(595.4, 288.9, 947.0, 50.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_9375() -> Glyph:
    """鍵 U+9375 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9375", advance=1000, unicode=0x9375, note="鍵：自动生成")
    g.diag(292.7, 637.7, 288.9, 665.9, weight=96.0)
    g.diag(288.9, 665.9, 122.0, 273.8, weight=96.0)
    g.dot(364.4, 555.6, w=96.0, h=124.8, slant=-14.0)
    g.hbar(180.0, 363.2, 413.9, weight=96.0)
    g.hbar(150.9, 408.9, 279.8, weight=96.0)
    g.diag(258.4, 383.3, 297.6, 362.1, weight=76.0)
    g.vbar(282.0, 100.9, 362.1, weight=76.0)
    g.diag(266.4, 100.9, 269.7, 103.9, weight=76.0)
    g.diag(153.2, 245.4, 246.0, 113.6, weight=64.0)
    g.hbar(373.5, 392.4, 237.0, weight=48.0)
    g.diag(373.5, 237.0, 304.2, 172.9, weight=48.0)
    g.diag(178.6, 104.1, 155.5, 26.5, weight=96.0)
    g.hbar(155.5, 375.0, 75.3, weight=96.0)
    g.hbar(565.1, 822.7, 578.9, weight=48.0)
    g.vbar(793.6, 430.3, 596.9, weight=48.0)
    g.hbar(509.5, 937.0, 489.9, weight=48.0)
    g.hbar(559.5, 789.0, 398.8, weight=48.0)
    g.hbar(529.6, 780.9, 297.6, weight=64.0)
    g.diag(780.9, 313.2, 796.4, 250.7, weight=64.0)
    g.hbar(504.6, 859.6, 208.8, weight=56.0)
    g.diag(625.5, 718.4, 674.5, 689.6, weight=96.0)
    g.vbar(670.8, 62.4, 689.6, weight=96.0)
    g.hbar(392.4, 497.9, 470.9, weight=96.0)
    g.vbar(428.8, 32.9, 488.5, weight=96.0)
    g.diag(359.6, 32.9, 372.5, 57.8, weight=96.0)
    g.hbar(339.4, 372.5, 61.6, weight=96.0)
    g.hbar(385.4, 544.5, 123.9, weight=64.0)
    g.hbar(544.5, 937.0, 54.8, weight=64.0)
    return g
def g_cjk_unified_ideograph_9396() -> Glyph:
    """鎖 U+9396 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9396", advance=1000, unicode=0x9396, note="鎖：自动生成")
    g.diag(363.5, 695.3, 360.2, 711.1, weight=96.0)
    g.diag(360.2, 711.1, 158.0, 367.4, weight=96.0)
    g.diag(158.0, 367.4, 195.3, 328.9, weight=96.0)
    g.diag(375.7, 663.1, 526.1, 545.2, weight=76.0)
    g.hbar(255.2, 510.6, 480.4, weight=96.0)
    g.hbar(216.0, 414.4, 321.7, weight=96.0)
    g.diag(414.4, 361.7, 461.4, 310.5, weight=96.0)
    g.diag(322.3, 429.6, 356.0, 404.8, weight=84.0)
    g.vbar(350.0, 162.0, 404.8, weight=84.0)
    g.diag(343.9, 162.0, 334.3, 153.3, weight=84.0)
    g.diag(221.4, 294.4, 245.2, 213.3, weight=76.0)
    g.diag(245.2, 213.3, 306.2, 165.0, weight=76.0)
    g.hbar(466.5, 490.5, 271.9, weight=48.0)
    g.diag(466.5, 272.4, 431.6, 183.7, weight=48.0)
    g.hbar(153.1, 206.2, 79.2, weight=56.0)
    g.diag(206.2, 72.2, 447.2, 220.8, weight=56.0)
    g.diag(661.7, 782.0, 702.7, 744.3, weight=48.0)
    g.vbar(695.9, 545.1, 744.3, weight=48.0)
    g.diag(689.2, 545.1, 675.7, 532.6, weight=48.0)
    g.hbar(490.4, 668.8, 613.9, weight=64.0)
    g.diag(846.9, 744.0, 864.9, 712.9, weight=56.0)
    g.diag(864.9, 712.9, 782.0, 560.6, weight=56.0)
    g.vbar(578.0, 420.5, 512.4, weight=48.0)
    g.vbar(582.3, 165.0, 420.5, weight=48.0)
    g.hbar(589.7, 790.6, 521.3, weight=48.0)
    g.diag(790.6, 538.7, 821.7, 446.4, weight=48.0)
    g.diag(821.7, 446.4, 895.1, 322.6, weight=48.0)
    g.diag(895.1, 322.6, 804.2, 182.6, weight=48.0)
    g.diag(604.4, 381.5, 612.5, 397.0, weight=64.0)
    g.hbar(612.5, 805.7, 400.0, weight=64.0)
    g.diag(601.6, 292.4, 613.1, 302.9, weight=76.0)
    g.hbar(613.1, 801.9, 309.0, weight=76.0)
    g.diag(602.6, 177.3, 615.6, 189.1, weight=76.0)
    g.hbar(615.6, 801.9, 192.2, weight=76.0)
    g.diag(650.6, 161.5, 427.4, -72.0, weight=76.0)
    g.diag(796.9, 136.0, 890.0, -37.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_93ae() -> Glyph:
    """鎮 U+93AE —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni93AE", advance=1000, unicode=0x93AE, note="鎮：自动生成")
    g.diag(275.8, 771.1, 320.4, 719.2, weight=96.0)
    g.diag(320.4, 719.2, 63.1, 345.6, weight=96.0)
    g.dot(382.2, 636.4, w=96.0, h=124.8, slant=-14.0)
    g.hbar(190.3, 399.1, 462.9, weight=84.0)
    g.hbar(174.4, 395.1, 349.0, weight=84.0)
    g.diag(268.9, 424.1, 296.7, 408.4, weight=64.0)
    g.vbar(291.5, 172.1, 408.4, weight=64.0)
    g.diag(286.2, 172.1, 275.8, 163.6, weight=64.0)
    g.dot(183.9, 212.3, w=64.0, h=83.2, slant=-14.0)
    g.hbar(399.1, 421.0, 288.4, weight=48.0)
    g.diag(399.1, 288.9, 353.4, 229.2, weight=48.0)
    g.hbar(95.9, 409.0, 142.2, weight=48.0)
    g.diag(522.4, 782.0, 643.8, 635.2, weight=48.0)
    g.hbar(643.8, 839.5, 617.2, weight=48.0)
    g.vbar(836.5, 599.2, 725.3, weight=48.0)
    g.hbar(746.4, 778.9, 745.7, weight=48.0)
    g.hbar(568.3, 746.4, 711.9, weight=48.0)
    g.diag(568.3, 675.8, 570.1, 677.6, weight=48.0)
    g.vbar(567.6, 224.3, 518.5, weight=48.0)
    g.diag(601.9, 504.6, 610.9, 495.7, weight=48.0)
    g.hbar(610.9, 755.3, 508.6, weight=48.0)
    g.diag(755.3, 521.6, 800.6, 485.1, weight=48.0)
    g.vbar(795.2, 225.3, 485.1, weight=48.0)
    g.diag(606.9, 406.2, 613.9, 420.3, weight=64.0)
    g.hbar(613.9, 708.3, 424.2, weight=64.0)
    g.hbar(602.9, 725.2, 331.1, weight=56.0)
    g.hbar(599.9, 760.0, 259.6, weight=56.0)
    g.diag(448.8, 397.3, 496.1, 358.9, weight=76.0)
    g.diag(496.1, 358.9, 589.7, 216.4, weight=76.0)
    g.hbar(589.7, 941.9, 186.5, weight=76.0)
    g.hbar(597.8, 618.8, 60.6, weight=96.0)
    g.diag(597.8, 59.9, 402.1, -66.0, weight=96.0)
    g.diag(750.1, 84.1, 873.3, -72.0, weight=76.0)
    return g
def g_cjk_unified_ideograph_9418() -> Glyph:
    """鐘 U+9418 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9418", advance=1000, unicode=0x9418, note="鐘：自动生成")
    g.diag(320.4, 674.1, 322.2, 684.3, weight=96.0)
    g.diag(322.2, 684.3, 91.1, 301.6, weight=96.0)
    g.diag(91.1, 301.6, 116.2, 281.8, weight=96.0)
    g.diag(333.6, 638.0, 343.2, 622.7, weight=96.0)
    g.hbar(343.2, 473.2, 610.4, weight=96.0)
    g.hbar(197.8, 395.5, 434.2, weight=96.0)
    g.hbar(158.7, 349.1, 285.2, weight=92.0)
    g.diag(349.1, 320.3, 402.0, 281.9, weight=92.0)
    g.diag(267.2, 401.7, 298.3, 383.0, weight=76.0)
    g.vbar(293.2, 126.2, 383.0, weight=76.0)
    g.diag(288.1, 126.2, 278.3, 118.0, weight=76.0)
    g.diag(166.1, 254.6, 255.5, 129.8, weight=64.0)
    g.hbar(409.0, 429.1, 244.3, weight=48.0)
    g.diag(409.0, 245.8, 313.9, 184.8, weight=48.0)
    g.hbar(109.3, 160.6, 53.2, weight=56.0)
    g.hbar(160.6, 429.1, 94.4, weight=56.0)
    g.diag(586.0, 784.9, 659.4, 738.6, weight=96.0)
    g.diag(659.4, 738.6, 682.3, 686.1, weight=96.0)
    g.vbar(514.9, 603.2, 615.6, weight=96.0)
    g.hbar(516.7, 779.9, 641.5, weight=96.0)
    g.diag(779.9, 667.4, 765.4, 622.3, weight=96.0)
    g.dot(552.2, 540.2, w=96.0, h=92.4, slant=-14.0)
    g.diag(708.7, 629.0, 737.1, 596.3, weight=96.0)
    g.diag(737.1, 596.3, 681.6, 496.2, weight=96.0)
    g.hbar(408.9, 909.9, 469.5, weight=64.0)
    g.vbar(482.9, 360.1, 368.5, weight=48.0)
    g.vbar(506.2, 163.4, 360.1, weight=48.0)
    g.hbar(496.3, 821.8, 375.0, weight=48.0)
    g.vbar(793.5, 199.5, 386.6, weight=48.0)
    g.hbar(741.5, 765.1, 199.4, weight=48.0)
    g.hbar(529.2, 768.8, 274.2, weight=56.0)
    g.hbar(545.8, 738.7, 191.0, weight=64.0)
    g.diag(602.1, 356.4, 613.8, 351.1, weight=96.0)
    g.diag(613.8, 351.1, 656.8, 55.0, weight=96.0)
    g.diag(656.8, 55.0, 618.2, 5.4, weight=96.0)
    g.diag(517.5, 127.7, 576.0, 77.8, weight=84.0)
    g.hbar(576.0, 725.8, 92.4, weight=84.0)
    g.diag(725.8, 107.0, 767.4, 144.8, weight=84.0)
    g.hbar(399.0, 932.0, -26.8, weight=84.0)
    return g
def g_cjk_unified_ideograph_9451() -> Glyph:
    """鑑 U+9451 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9451", advance=1000, unicode=0x9451, note="鑑：自动生成")
    g.vbar(305.7, 666.6, 690.5, weight=96.0)
    g.diag(305.5, 690.5, 104.5, 361.0, weight=96.0)
    g.diag(104.5, 361.0, 139.3, 319.5, weight=96.0)
    g.hbar(303.7, 445.0, 605.1, weight=48.0)
    g.hbar(196.4, 426.4, 455.9, weight=96.0)
    g.hbar(165.5, 345.7, 318.2, weight=96.0)
    g.diag(345.7, 355.0, 379.0, 334.8, weight=96.0)
    g.diag(256.3, 422.6, 296.3, 386.0, weight=48.0)
    g.vbar(284.5, 150.4, 386.0, weight=48.0)
    g.diag(167.1, 285.6, 194.5, 204.7, weight=64.0)
    g.diag(194.5, 204.7, 246.5, 167.7, weight=64.0)
    g.diag(364.1, 336.7, 377.4, 279.0, weight=48.0)
    g.diag(377.4, 279.0, 304.8, 220.6, weight=48.0)
    g.diag(177.8, 159.4, 163.0, 80.8, weight=96.0)
    g.hbar(163.0, 406.8, 133.0, weight=96.0)
    g.hbar(483.2, 611.6, 624.3, weight=96.0)
    g.vbar(605.2, 602.4, 635.1, weight=96.0)
    g.diag(553.7, 596.3, 573.4, 573.0, weight=64.0)
    g.diag(573.4, 573.0, 547.0, 515.3, weight=64.0)
    g.hbar(481.3, 652.2, 490.2, weight=48.0)
    g.diag(652.2, 508.0, 599.3, 423.5, weight=48.0)
    g.hbar(482.3, 639.4, 387.8, weight=48.0)
    g.diag(550.9, 381.0, 570.3, 350.7, weight=48.0)
    g.diag(570.3, 350.7, 547.8, 302.4, weight=48.0)
    g.vbar(459.3, 265.3, 619.9, weight=48.0)
    g.hbar(453.5, 652.8, 280.2, weight=48.0)
    g.diag(676.5, 662.4, 782.3, 715.4, weight=96.0)
    g.diag(782.3, 715.4, 657.6, 396.2, weight=96.0)
    g.hbar(726.2, 899.6, 485.8, weight=96.0)
    g.diag(713.3, 413.3, 806.2, 340.0, weight=96.0)
    g.diag(806.2, 340.0, 794.1, 257.9, weight=96.0)
    g.vbar(465.3, 170.6, 182.8, weight=48.0)
    g.diag(464.6, 170.6, 507.5, 24.7, weight=48.0)
    g.hbar(479.3, 777.4, 202.6, weight=48.0)
    g.diag(777.4, 226.9, 810.6, 182.8, weight=48.0)
    g.diag(810.6, 182.8, 745.9, 51.5, weight=48.0)
    g.vbar(580.5, 49.2, 170.4, weight=64.0)
    g.diag(587.3, 49.2, 596.6, 38.9, weight=64.0)
    g.diag(654.7, 187.5, 682.4, 167.5, weight=64.0)
    g.diag(682.4, 167.5, 660.4, 52.2, weight=64.0)
    g.diag(660.4, 52.2, 649.0, 45.6, weight=64.0)
    g.hbar(354.6, 932.0, 12.2, weight=48.0)
    return g
def g_cjk_unified_ideograph_9591() -> Glyph:
    """閑 U+9591 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9591", advance=1000, unicode=0x9591, note="閑：自动生成")
    g.vbar(189.7, 497.4, 682.9, weight=48.0)
    g.vbar(178.0, -49.8, 497.4, weight=48.0)
    g.hbar(197.1, 348.2, 639.2, weight=48.0)
    g.vbar(358.7, 426.4, 609.1, weight=48.0)
    g.hbar(346.9, 369.1, 425.2, weight=48.0)
    g.diag(231.0, 524.0, 245.0, 544.4, weight=92.0)
    g.hbar(245.0, 345.7, 545.5, weight=92.0)
    g.hbar(223.4, 318.2, 419.8, weight=96.0)
    g.diag(318.2, 436.3, 327.7, 424.0, weight=96.0)
    g.diag(573.4, 762.0, 638.7, 463.2, weight=48.0)
    g.hbar(625.9, 807.4, 740.6, weight=48.0)
    g.vbar(821.6, 476.4, 752.5, weight=48.0)
    g.vbar(833.3, -54.8, 476.4, weight=48.0)
    g.diag(830.8, -54.8, 721.2, -4.2, weight=48.0)
    g.diag(658.1, 603.3, 682.1, 628.5, weight=96.0)
    g.hbar(682.1, 814.3, 627.9, weight=96.0)
    g.diag(653.8, 475.1, 670.7, 490.8, weight=96.0)
    g.hbar(670.7, 795.2, 500.6, weight=96.0)
    g.diag(795.2, 510.4, 821.1, 496.8, weight=96.0)
    g.hbar(328.8, 644.0, 331.1, weight=48.0)
    g.diag(459.2, 482.7, 490.5, 330.0, weight=48.0)
    g.vbar(492.8, -34.6, 330.0, weight=48.0)
    g.diag(465.5, 311.7, 282.1, 73.0, weight=48.0)
    g.diag(538.7, 247.2, 715.4, 33.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_95a3() -> Glyph:
    """閣 U+95A3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni95A3", advance=1000, unicode=0x95A3, note="閣：自动生成")
    g.vbar(186.7, 498.2, 690.0, weight=96.0)
    g.vbar(181.5, -32.4, 498.2, weight=96.0)
    g.hbar(206.4, 356.1, 688.3, weight=48.0)
    g.diag(356.1, 706.4, 391.4, 674.4, weight=48.0)
    g.diag(391.4, 674.4, 357.7, 446.8, weight=48.0)
    g.hbar(337.3, 357.7, 446.3, weight=48.0)
    g.diag(231.6, 540.5, 245.8, 559.5, weight=76.0)
    g.hbar(245.8, 344.9, 556.5, weight=76.0)
    g.hbar(228.5, 303.9, 445.9, weight=92.0)
    g.diag(303.9, 458.6, 318.1, 446.7, weight=92.0)
    g.diag(595.0, 739.8, 584.0, 734.2, weight=48.0)
    g.diag(584.0, 734.2, 600.1, 709.3, weight=48.0)
    g.vbar(618.6, 483.0, 709.3, weight=48.0)
    g.hbar(608.0, 796.8, 746.8, weight=48.0)
    g.vbar(812.2, 454.4, 761.3, weight=48.0)
    g.vbar(818.9, -49.5, 454.4, weight=48.0)
    g.hbar(701.4, 810.3, -25.5, weight=48.0)
    g.diag(645.8, 609.5, 656.4, 625.4, weight=92.0)
    g.hbar(656.4, 803.6, 626.4, weight=92.0)
    g.diag(649.9, 497.2, 664.1, 513.9, weight=96.0)
    g.hbar(664.1, 809.6, 512.8, weight=96.0)
    g.diag(477.9, 422.1, 447.9, 443.8, weight=48.0)
    g.diag(447.9, 443.8, 303.7, 279.8, weight=48.0)
    g.diag(436.4, 400.4, 488.3, 336.4, weight=48.0)
    g.diag(488.3, 336.4, 271.8, 108.7, weight=48.0)
    g.hbar(403.7, 818.3, 277.3, weight=64.0)
    g.diag(363.5, 142.7, 391.3, 129.3, weight=96.0)
    g.vbar(405.7, -0.5, 129.3, weight=96.0)
    g.hbar(411.6, 607.7, 140.0, weight=48.0)
    g.diag(607.7, 153.5, 558.2, 72.3, weight=48.0)
    g.hbar(434.0, 583.5, 40.7, weight=48.0)
    g.vbar(585.8, 56.0, 79.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_95a5() -> Glyph:
    """閥 U+95A5 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni95A5", advance=1000, unicode=0x95A5, note="閥：自动生成")
    g.vbar(185.4, -15.6, 670.0, weight=96.0)
    g.hbar(212.7, 383.5, 665.4, weight=48.0)
    g.vbar(368.6, 438.5, 680.3, weight=48.0)
    g.hbar(333.3, 353.7, 437.2, weight=48.0)
    g.diag(232.0, 538.2, 243.4, 553.4, weight=84.0)
    g.hbar(243.4, 333.7, 552.4, weight=84.0)
    g.diag(224.7, 419.5, 240.3, 436.2, weight=96.0)
    g.hbar(240.3, 317.3, 441.4, weight=96.0)
    g.diag(613.3, 748.7, 602.3, 729.4, weight=48.0)
    g.vbar(613.6, 505.0, 729.4, weight=48.0)
    g.hbar(619.9, 779.0, 749.5, weight=48.0)
    g.diag(779.0, 761.2, 817.1, 511.3, weight=48.0)
    g.vbar(836.2, -79.3, 511.3, weight=48.0)
    g.diag(855.4, -79.3, 715.1, 32.5, weight=48.0)
    g.diag(643.1, 619.4, 656.6, 639.0, weight=84.0)
    g.hbar(656.6, 790.8, 638.8, weight=84.0)
    g.hbar(641.0, 778.7, 530.7, weight=84.0)
    g.diag(778.7, 546.0, 794.0, 532.1, weight=84.0)
    g.diag(358.4, 420.3, 390.5, 353.1, weight=48.0)
    g.diag(390.5, 353.1, 322.1, 255.3, weight=48.0)
    g.hbar(218.9, 322.1, 234.3, weight=48.0)
    g.vbar(358.8, 25.0, 265.5, weight=48.0)
    g.hbar(388.4, 591.7, 284.8, weight=64.0)
    g.hbar(591.7, 635.0, 309.1, weight=64.0)
    g.diag(396.3, 468.1, 526.9, 319.7, weight=84.0)
    g.diag(526.9, 319.7, 703.5, 31.7, weight=84.0)
    g.diag(703.5, 31.7, 809.0, 154.5, weight=84.0)
    g.diag(638.3, 296.5, 673.3, 224.2, weight=76.0)
    g.diag(673.3, 224.2, 390.9, 75.7, weight=76.0)
    g.diag(612.2, 470.5, 669.1, 399.8, weight=84.0)
    g.diag(669.1, 399.8, 645.4, 345.0, weight=84.0)
    return g
def g_cjk_unified_ideograph_965b() -> Glyph:
    """陛 U+965B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni965B", advance=1000, unicode=0x965B, note="陛：自动生成")
    g.hbar(161.8, 329.4, 644.9, weight=48.0)
    g.diag(329.4, 672.9, 268.7, 506.2, weight=48.0)
    g.diag(268.7, 506.2, 337.4, 341.1, weight=48.0)
    g.hbar(174.0, 337.4, 358.0, weight=48.0)
    g.vbar(152.7, 440.3, 634.1, weight=76.0)
    g.vbar(139.7, -52.0, 440.3, weight=76.0)
    g.dot(552.2, 555.2, w=96.0, h=124.8, slant=-14.0)
    g.diag(415.5, 675.4, 486.1, 372.5, weight=56.0)
    g.hbar(486.1, 646.5, 404.1, weight=56.0)
    g.diag(820.5, 696.6, 840.5, 650.5, weight=96.0)
    g.diag(840.5, 650.5, 683.7, 546.0, weight=96.0)
    g.diag(637.1, 757.0, 698.9, 592.7, weight=96.0)
    g.diag(698.9, 592.7, 897.9, 340.8, weight=96.0)
    g.vbar(903.2, 340.8, 491.9, weight=96.0)
    g.hbar(419.7, 789.8, 190.3, weight=96.0)
    g.diag(536.7, 362.0, 611.6, 268.2, weight=76.0)
    g.vbar(610.6, 51.9, 268.2, weight=76.0)
    g.diag(609.5, 51.9, 593.6, 30.7, weight=76.0)
    g.hbar(334.9, 921.2, -5.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_966a() -> Glyph:
    """陪 U+966A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni966A", advance=1000, unicode=0x966A, note="陪：自动生成")
    g.hbar(160.4, 176.3, 645.8, weight=48.0)
    g.hbar(176.3, 322.4, 658.9, weight=48.0)
    g.diag(322.4, 674.6, 251.2, 535.1, weight=48.0)
    g.diag(251.2, 535.1, 317.3, 371.2, weight=48.0)
    g.hbar(198.8, 317.3, 385.4, weight=48.0)
    g.vbar(104.4, -41.0, 665.1, weight=64.0)
    g.diag(533.7, 778.1, 647.7, 686.8, weight=84.0)
    g.hbar(418.6, 789.7, 585.7, weight=84.0)
    g.dot(467.3, 435.4, w=84.0, h=101.6, slant=-14.0)
    g.diag(663.3, 562.4, 702.2, 525.6, weight=84.0)
    g.diag(702.2, 525.6, 609.3, 345.7, weight=84.0)
    g.hbar(298.3, 938.0, 313.6, weight=84.0)
    g.diag(391.6, 190.2, 466.3, -43.1, weight=48.0)
    g.diag(450.7, 189.2, 462.8, 178.3, weight=48.0)
    g.hbar(462.8, 695.7, 198.0, weight=48.0)
    g.diag(695.7, 217.8, 734.8, 179.8, weight=48.0)
    g.diag(734.8, 179.8, 704.7, 76.2, weight=48.0)
    g.diag(704.7, 76.2, 676.7, 55.4, weight=48.0)
    g.hbar(488.0, 575.5, -1.1, weight=48.0)
    g.hbar(575.5, 746.2, 12.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_9670() -> Glyph:
    """陰 U+9670 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9670", advance=1000, unicode=0x9670, note="陰：自动生成")
    g.hbar(153.0, 320.0, 609.2, weight=48.0)
    g.diag(320.0, 627.7, 237.1, 486.9, weight=48.0)
    g.diag(237.1, 486.9, 300.4, 325.0, weight=48.0)
    g.hbar(165.7, 300.4, 340.3, weight=48.0)
    g.vbar(129.6, -47.4, 609.6, weight=84.0)
    g.diag(557.3, 697.2, 552.3, 711.2, weight=84.0)
    g.diag(552.3, 711.2, 320.1, 399.6, weight=84.0)
    g.vbar(574.6, 654.9, 669.2, weight=96.0)
    g.diag(575.4, 654.9, 777.2, 488.0, weight=96.0)
    g.hbar(777.2, 932.0, 480.4, weight=96.0)
    g.diag(499.3, 549.2, 561.2, 517.2, weight=84.0)
    g.diag(561.2, 517.2, 584.8, 464.1, weight=84.0)
    g.diag(383.3, 421.3, 436.8, 386.6, weight=48.0)
    g.hbar(436.8, 669.7, 408.9, weight=48.0)
    g.diag(669.7, 431.2, 546.8, 293.6, weight=48.0)
    g.hbar(406.8, 684.2, 273.2, weight=48.0)
    g.hbar(289.8, 838.6, 159.2, weight=48.0)
    g.diag(529.3, 147.1, 431.5, 18.1, weight=48.0)
    g.diag(431.5, 18.1, 457.5, -18.4, weight=48.0)
    g.hbar(457.5, 659.4, 10.9, weight=48.0)
    g.hbar(659.4, 679.7, 40.5, weight=48.0)
    g.diag(650.2, 59.2, 744.2, -1.1, weight=48.0)
    g.diag(744.2, -1.1, 761.9, -61.1, weight=48.0)
    return g
def g_cjk_unified_ideograph_9673() -> Glyph:
    """陳 U+9673 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9673", advance=1000, unicode=0x9673, note="陳：自动生成")
    g.diag(171.8, 631.6, 178.5, 627.4, weight=48.0)
    g.hbar(178.5, 315.8, 639.5, weight=48.0)
    g.diag(315.8, 651.7, 248.7, 511.7, weight=48.0)
    g.diag(248.7, 511.7, 311.1, 352.2, weight=48.0)
    g.diag(311.1, 352.2, 206.3, 400.0, weight=48.0)
    g.diag(107.3, 654.1, 131.4, 474.9, weight=48.0)
    g.vbar(134.8, 19.0, 474.9, weight=48.0)
    g.hbar(422.1, 712.5, 662.5, weight=92.0)
    g.diag(351.1, 522.4, 422.1, 321.6, weight=48.0)
    g.hbar(396.9, 512.7, 527.3, weight=48.0)
    g.hbar(512.7, 710.5, 550.8, weight=48.0)
    g.diag(710.5, 567.6, 740.5, 524.7, weight=48.0)
    g.diag(740.5, 524.7, 673.3, 351.5, weight=48.0)
    g.hbar(467.8, 631.3, 438.8, weight=56.0)
    g.hbar(437.0, 652.8, 356.6, weight=48.0)
    g.diag(504.3, 782.0, 539.8, 500.8, weight=96.0)
    g.vbar(541.6, -52.0, 500.8, weight=96.0)
    g.diag(526.7, 333.7, 224.1, 64.7, weight=48.0)
    g.diag(579.0, 338.4, 922.7, 91.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_9675() -> Glyph:
    """陵 U+9675 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9675", advance=1000, unicode=0x9675, note="陵：自动生成")
    g.diag(174.2, 619.8, 287.6, 554.8, weight=48.0)
    g.vbar(288.5, 415.5, 554.8, weight=48.0)
    g.hbar(182.2, 289.4, 396.8, weight=48.0)
    g.vbar(164.7, 447.6, 634.7, weight=56.0)
    g.vbar(153.4, -25.1, 447.6, weight=56.0)
    g.hbar(370.9, 691.3, 631.0, weight=96.0)
    g.diag(691.3, 628.7, 745.6, 551.0, weight=96.0)
    g.diag(553.8, 787.0, 601.7, 744.7, weight=96.0)
    g.diag(601.7, 744.7, 567.8, 506.3, weight=96.0)
    g.hbar(346.3, 831.5, 470.2, weight=76.0)
    g.diag(445.2, 420.5, 464.6, 371.1, weight=84.0)
    g.diag(464.6, 371.1, 338.3, 244.1, weight=84.0)
    g.vbar(333.7, 244.1, 320.5, weight=84.0)
    g.diag(650.8, 470.7, 810.6, 309.3, weight=64.0)
    g.diag(572.6, 276.9, 479.1, 220.5, weight=48.0)
    g.diag(479.1, 220.5, 291.1, 40.6, weight=48.0)
    g.diag(519.7, 251.0, 581.5, 161.0, weight=48.0)
    g.diag(581.5, 161.0, 381.6, -42.0, weight=48.0)
    g.hbar(461.6, 477.2, 175.4, weight=96.0)
    g.diag(461.6, 174.9, 910.1, -52.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_9676() -> Glyph:
    """陶 U+9676 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9676", advance=1000, unicode=0x9676, note="陶：自动生成")
    g.hbar(211.5, 372.6, 664.5, weight=48.0)
    g.diag(372.6, 683.8, 313.7, 539.5, weight=48.0)
    g.diag(313.7, 539.5, 373.3, 379.5, weight=48.0)
    g.hbar(219.9, 373.3, 392.8, weight=48.0)
    g.vbar(194.2, 505.6, 668.1, weight=96.0)
    g.vbar(181.9, -19.1, 505.6, weight=96.0)
    g.diag(571.7, 792.0, 606.8, 747.3, weight=48.0)
    g.diag(606.8, 747.3, 469.0, 514.4, weight=48.0)
    g.diag(521.8, 573.4, 766.5, 408.5, weight=48.0)
    g.vbar(766.2, -67.1, 408.5, weight=48.0)
    g.diag(765.9, -67.1, 613.1, 37.2, weight=48.0)
    g.diag(476.8, 522.4, 505.9, 486.2, weight=48.0)
    g.diag(505.9, 486.2, 439.0, 385.4, weight=48.0)
    g.hbar(499.5, 672.5, 447.7, weight=96.0)
    g.diag(672.5, 465.4, 718.9, 378.1, weight=96.0)
    g.hbar(422.0, 821.6, 303.6, weight=96.0)
    g.diag(552.6, 414.1, 585.6, 392.1, weight=64.0)
    g.vbar(581.2, 182.4, 392.1, weight=64.0)
    g.diag(576.8, 182.4, 564.3, 172.0, weight=64.0)
    g.vbar(440.6, 125.0, 284.2, weight=48.0)
    g.hbar(456.1, 708.9, 153.5, weight=48.0)
    g.diag(704.8, 300.6, 755.0, 127.3, weight=92.0)
    g.hbar(711.6, 755.0, 133.4, weight=92.0)
    return g
def g_cjk_unified_ideograph_9685() -> Glyph:
    """隅 U+9685 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9685", advance=1000, unicode=0x9685, note="隅：自动生成")
    g.hbar(166.6, 286.2, 655.6, weight=48.0)
    g.vbar(288.5, 484.1, 630.3, weight=48.0)
    g.hbar(178.9, 290.9, 459.5, weight=48.0)
    g.vbar(151.0, 514.9, 706.4, weight=96.0)
    g.vbar(137.7, -29.2, 514.9, weight=96.0)
    g.vbar(448.6, 679.5, 694.5, weight=48.0)
    g.vbar(478.3, 425.4, 679.5, weight=48.0)
    g.hbar(461.1, 737.3, 660.3, weight=48.0)
    g.vbar(753.0, 473.4, 634.6, weight=48.0)
    g.hbar(739.2, 768.6, 471.1, weight=48.0)
    g.hbar(515.3, 760.0, 567.7, weight=96.0)
    g.hbar(524.2, 728.7, 459.3, weight=96.0)
    g.diag(353.1, 308.0, 398.6, 7.5, weight=96.0)
    g.hbar(389.7, 549.9, 303.9, weight=96.0)
    g.hbar(549.9, 917.9, 328.7, weight=96.0)
    g.diag(917.9, 345.9, 866.5, -20.6, weight=96.0)
    g.diag(866.5, -20.6, 776.3, 109.3, weight=96.0)
    g.diag(595.3, 677.5, 637.5, 655.6, weight=96.0)
    g.vbar(623.9, 198.8, 655.6, weight=96.0)
    g.diag(610.2, 198.8, 608.6, 196.4, weight=96.0)
    g.hbar(423.8, 724.6, 174.2, weight=96.0)
    g.diag(724.6, 201.8, 726.4, 200.8, weight=96.0)
    g.diag(719.1, 230.9, 776.4, 189.7, weight=64.0)
    g.hbar(745.4, 776.4, 186.7, weight=64.0)
    return g
def g_cjk_unified_ideograph_968f() -> Glyph:
    """随 U+968F —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni968F", advance=1000, unicode=0x968F, note="随：自动生成")
    g.hbar(166.8, 182.8, 705.2, weight=48.0)
    g.diag(182.8, 703.6, 281.9, 639.4, weight=48.0)
    g.diag(281.9, 639.4, 392.2, 400.9, weight=48.0)
    g.hbar(203.4, 392.2, 425.4, weight=48.0)
    g.vbar(100.9, -20.3, 731.6, weight=96.0)
    g.hbar(500.1, 828.0, 601.6, weight=96.0)
    g.vbar(619.0, 652.1, 794.2, weight=48.0)
    g.diag(612.8, 652.1, 471.0, 357.3, weight=48.0)
    g.vbar(569.7, 81.1, 442.5, weight=48.0)
    g.diag(615.5, 439.2, 627.4, 431.7, weight=48.0)
    g.hbar(627.4, 732.5, 446.6, weight=48.0)
    g.diag(732.5, 461.5, 757.0, 330.0, weight=48.0)
    g.vbar(748.1, 80.1, 330.0, weight=48.0)
    g.diag(739.3, 80.1, 659.8, 116.7, weight=48.0)
    g.diag(611.2, 309.8, 620.5, 323.1, weight=76.0)
    g.hbar(620.5, 698.6, 325.6, weight=76.0)
    g.diag(603.7, 211.6, 614.8, 227.7, weight=76.0)
    g.hbar(614.8, 698.6, 229.9, weight=76.0)
    g.dot(384.7, 562.2, w=76.0, h=96.2, slant=-14.0)
    g.hbar(259.5, 314.6, 321.0, weight=84.0)
    g.diag(314.6, 326.8, 456.5, 111.5, weight=84.0)
    g.diag(456.5, 111.5, 399.8, 80.0, weight=84.0)
    g.hbar(253.1, 406.4, 60.8, weight=96.0)
    g.hbar(406.4, 937.0, 8.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_9694() -> Glyph:
    """隔 U+9694 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9694", advance=1000, unicode=0x9694, note="隔：自动生成")
    g.hbar(153.6, 349.4, 722.4, weight=48.0)
    g.diag(349.4, 740.0, 263.5, 587.4, weight=48.0)
    g.diag(263.5, 587.4, 358.3, 384.6, weight=48.0)
    g.hbar(173.3, 358.3, 395.2, weight=48.0)
    g.vbar(122.2, -52.0, 732.2, weight=48.0)
    g.diag(489.5, 617.1, 516.0, 709.3, weight=96.0)
    g.hbar(516.0, 848.8, 732.6, weight=96.0)
    g.vbar(535.2, 414.0, 577.2, weight=76.0)
    g.hbar(531.8, 753.9, 587.4, weight=48.0)
    g.diag(753.9, 611.9, 790.5, 571.3, weight=48.0)
    g.diag(790.5, 571.3, 734.5, 487.2, weight=48.0)
    g.hbar(572.4, 774.2, 465.8, weight=48.0)
    g.vbar(381.1, -41.8, 308.7, weight=96.0)
    g.hbar(407.3, 586.0, 312.4, weight=64.0)
    g.hbar(586.0, 824.4, 276.9, weight=64.0)
    g.vbar(857.4, -37.3, 235.0, weight=64.0)
    g.hbar(783.4, 890.4, -22.1, weight=64.0)
    g.diag(520.7, 293.1, 594.1, 152.4, weight=48.0)
    g.diag(704.9, 308.4, 720.6, 276.6, weight=96.0)
    g.diag(720.6, 276.6, 658.4, 210.1, weight=96.0)
    g.vbar(659.3, 185.1, 210.1, weight=96.0)
    g.hbar(442.1, 868.6, 140.6, weight=96.0)
    g.diag(654.7, 115.0, 636.7, 96.9, weight=96.0)
    g.vbar(637.3, -50.9, 96.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_9699() -> Glyph:
    """隙 U+9699 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9699", advance=1000, unicode=0x9699, note="隙：自动生成")
    g.hbar(178.8, 367.4, 675.3, weight=48.0)
    g.diag(367.4, 689.2, 292.1, 538.2, weight=48.0)
    g.diag(292.1, 538.2, 352.4, 424.2, weight=48.0)
    g.diag(352.4, 424.2, 345.2, 374.0, weight=48.0)
    g.hbar(193.3, 345.2, 383.5, weight=48.0)
    g.diag(119.8, 694.2, 150.4, 467.7, weight=48.0)
    g.vbar(148.3, -52.0, 467.7, weight=48.0)
    g.diag(605.2, 772.0, 637.1, 651.7, weight=96.0)
    g.vbar(645.8, 458.6, 651.7, weight=96.0)
    g.diag(506.6, 632.8, 441.7, 457.3, weight=84.0)
    g.hbar(684.5, 858.3, 624.5, weight=96.0)
    g.diag(858.3, 593.4, 885.7, 551.8, weight=96.0)
    g.vbar(502.7, 207.9, 423.3, weight=48.0)
    g.hbar(485.9, 813.8, 426.2, weight=48.0)
    g.vbar(788.3, 246.6, 440.3, weight=48.0)
    g.hbar(734.2, 762.8, 250.5, weight=48.0)
    g.hbar(528.9, 759.0, 313.5, weight=64.0)
    g.diag(543.9, 216.5, 556.3, 228.9, weight=64.0)
    g.hbar(556.3, 723.6, 233.6, weight=64.0)
    g.diag(606.3, 215.4, 717.0, -78.0, weight=84.0)
    g.hbar(456.4, 717.0, -21.0, weight=84.0)
    g.diag(500.1, 176.7, 436.5, 67.4, weight=96.0)
    g.diag(436.5, 67.4, 473.0, -4.1, weight=96.0)
    g.diag(764.4, 208.9, 925.2, -31.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_969b() -> Glyph:
    """際 U+969B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni969B", advance=1000, unicode=0x969B, note="際：自动生成")
    g.diag(138.9, 669.7, 242.5, 615.5, weight=48.0)
    g.diag(242.5, 615.5, 84.2, 456.2, weight=48.0)
    g.hbar(84.2, 150.9, 450.6, weight=48.0)
    g.vbar(93.6, 7.5, 707.2, weight=48.0)
    g.diag(428.8, 777.2, 457.8, 741.4, weight=48.0)
    g.diag(457.8, 741.4, 332.5, 514.0, weight=48.0)
    g.diag(433.1, 649.9, 457.9, 533.8, weight=48.0)
    g.diag(457.9, 533.8, 234.1, 236.6, weight=48.0)
    g.dot(424.0, 546.6, w=84.0, h=96.9, slant=-14.0)
    g.diag(330.0, 526.1, 401.5, 411.8, weight=56.0)
    g.hbar(625.5, 773.9, 716.0, weight=48.0)
    g.diag(773.9, 714.6, 660.3, 539.3, weight=48.0)
    g.diag(576.8, 616.9, 947.0, 347.2, weight=84.0)
    g.hbar(445.6, 691.7, 417.1, weight=56.0)
    g.hbar(348.3, 416.2, 251.9, weight=96.0)
    g.hbar(416.2, 693.3, 264.4, weight=96.0)
    g.diag(693.3, 292.3, 762.2, 352.7, weight=96.0)
    g.diag(526.2, 228.5, 567.6, 192.8, weight=92.0)
    g.diag(567.6, 192.8, 539.4, -37.6, weight=92.0)
    g.hbar(370.7, 539.4, -5.2, weight=92.0)
    g.vbar(392.4, 5.1, 202.9, weight=96.0)
    g.diag(598.0, 170.7, 782.7, 72.4, weight=96.0)
    g.diag(782.7, 72.4, 801.0, 25.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_969c() -> Glyph:
    """障 U+969C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni969C", advance=1000, unicode=0x969C, note="障：自动生成")
    g.hbar(202.5, 342.7, 674.4, weight=48.0)
    g.diag(342.7, 687.8, 290.2, 553.3, weight=48.0)
    g.diag(290.2, 553.3, 356.2, 408.3, weight=48.0)
    g.hbar(216.8, 356.2, 416.8, weight=48.0)
    g.vbar(185.1, 533.1, 676.9, weight=84.0)
    g.vbar(185.4, 74.3, 533.1, weight=84.0)
    g.hbar(538.2, 599.0, 769.2, weight=48.0)
    g.diag(599.0, 756.4, 631.7, 704.5, weight=48.0)
    g.vbar(466.9, 634.6, 653.1, weight=64.0)
    g.hbar(463.7, 694.6, 675.6, weight=64.0)
    g.diag(694.6, 698.1, 677.1, 660.3, weight=64.0)
    g.dot(503.7, 589.6, w=96.0, h=70.4, slant=-14.0)
    g.diag(638.7, 662.1, 662.5, 634.0, weight=96.0)
    g.diag(662.5, 634.0, 617.5, 556.4, weight=96.0)
    g.hbar(352.2, 824.6, 518.1, weight=56.0)
    g.vbar(471.2, 271.5, 444.9, weight=48.0)
    g.hbar(462.6, 731.9, 451.7, weight=48.0)
    g.vbar(700.4, 298.0, 462.2, weight=48.0)
    g.diag(492.9, 358.3, 506.9, 371.4, weight=56.0)
    g.hbar(506.9, 676.2, 368.4, weight=56.0)
    g.diag(506.5, 286.7, 515.3, 294.6, weight=56.0)
    g.hbar(515.3, 659.5, 303.5, weight=56.0)
    g.hbar(331.1, 860.8, 188.9, weight=92.0)
    g.diag(544.4, 278.8, 580.5, 254.1, weight=96.0)
    g.vbar(579.6, -57.0, 254.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_96bb() -> Glyph:
    """隻 U+96BB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni96BB", advance=1000, unicode=0x96BB, note="隻：自动生成")
    g.diag(299.5, 760.1, 266.5, 653.4, weight=48.0)
    g.diag(266.5, 653.4, 108.3, 443.5, weight=48.0)
    g.vbar(275.7, 260.9, 578.5, weight=48.0)
    g.diag(464.0, 782.0, 554.3, 715.4, weight=48.0)
    g.hbar(368.9, 687.4, 656.0, weight=76.0)
    g.hbar(386.0, 660.8, 546.6, weight=76.0)
    g.hbar(375.5, 663.7, 451.1, weight=76.0)
    g.diag(487.7, 614.6, 519.5, 595.4, weight=92.0)
    g.vbar(514.1, 381.5, 595.4, weight=92.0)
    g.diag(508.7, 381.5, 498.2, 365.5, weight=92.0)
    g.diag(312.8, 306.5, 318.3, 312.1, weight=84.0)
    g.hbar(318.3, 738.8, 336.4, weight=84.0)
    g.diag(326.1, 233.3, 450.8, 160.6, weight=96.0)
    g.diag(450.8, 160.6, 191.0, -35.8, weight=96.0)
    g.hbar(309.9, 876.7, 60.7, weight=96.0)
    return g
def g_cjk_unified_ideograph_96c5() -> Glyph:
    """雅 U+96C5 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni96C5", advance=1000, unicode=0x96C5, note="雅：自动生成")
    g.diag(184.6, 632.0, 214.1, 658.8, weight=96.0)
    g.hbar(214.1, 375.8, 680.4, weight=96.0)
    g.diag(375.8, 702.1, 360.0, 656.5, weight=96.0)
    g.vbar(179.1, 437.1, 638.6, weight=76.0)
    g.hbar(171.4, 376.2, 472.2, weight=76.0)
    g.hbar(376.2, 433.9, 501.7, weight=76.0)
    g.vbar(272.9, 71.5, 659.1, weight=48.0)
    g.diag(244.6, 71.5, 205.5, 89.2, weight=48.0)
    g.diag(305.4, 461.5, 85.8, 147.1, weight=48.0)
    g.diag(563.8, 792.0, 538.9, 671.2, weight=48.0)
    g.diag(538.9, 671.2, 352.1, 399.3, weight=48.0)
    g.vbar(506.4, -62.0, 507.9, weight=48.0)
    g.diag(637.1, 736.4, 739.5, 677.2, weight=96.0)
    g.diag(739.5, 677.2, 771.1, 603.3, weight=96.0)
    g.hbar(549.3, 836.0, 562.5, weight=96.0)
    g.diag(836.0, 573.3, 796.0, 618.1, weight=96.0)
    g.hbar(565.6, 798.2, 408.2, weight=96.0)
    g.hbar(753.6, 798.2, 428.3, weight=96.0)
    g.hbar(563.3, 817.2, 287.2, weight=96.0)
    g.diag(817.2, 306.8, 835.8, 386.5, weight=96.0)
    g.diag(690.4, 513.2, 715.9, 495.9, weight=96.0)
    g.vbar(712.9, 190.0, 495.9, weight=96.0)
    g.diag(709.9, 190.0, 694.4, 166.7, weight=96.0)
    g.diag(553.0, 127.5, 561.6, 119.7, weight=96.0)
    g.hbar(561.6, 914.2, 132.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_96cc() -> Glyph:
    """雌 U+96CC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni96CC", advance=1000, unicode=0x96CC, note="雌：自动生成")
    g.diag(185.1, 663.5, 215.9, 532.9, weight=56.0)
    g.vbar(214.0, 258.1, 532.9, weight=56.0)
    g.diag(256.6, 466.8, 278.2, 487.4, weight=96.0)
    g.hbar(278.2, 337.3, 486.9, weight=96.0)
    g.diag(79.8, 483.7, 115.3, 449.1, weight=76.0)
    g.vbar(122.6, 223.2, 449.1, weight=76.0)
    g.diag(93.0, 210.9, 105.6, 175.8, weight=96.0)
    g.diag(105.6, 175.8, 333.0, 290.7, weight=96.0)
    g.hbar(410.7, 503.7, 506.2, weight=96.0)
    g.diag(410.7, 502.5, 400.6, 488.7, weight=96.0)
    g.diag(342.0, 724.0, 410.6, 232.3, weight=56.0)
    g.diag(410.6, 232.3, 551.4, 305.2, weight=56.0)
    g.diag(612.2, 779.7, 597.5, 659.0, weight=48.0)
    g.diag(597.5, 659.0, 458.2, 380.4, weight=48.0)
    g.vbar(554.3, -49.7, 464.4, weight=48.0)
    g.diag(679.8, 700.1, 778.1, 635.7, weight=96.0)
    g.diag(778.1, 635.7, 798.3, 574.5, weight=96.0)
    g.hbar(599.7, 843.1, 531.8, weight=96.0)
    g.diag(843.1, 540.4, 823.4, 578.8, weight=96.0)
    g.hbar(612.5, 791.0, 380.7, weight=96.0)
    g.hbar(781.3, 791.0, 396.6, weight=96.0)
    g.hbar(611.4, 799.9, 261.9, weight=96.0)
    g.hbar(779.9, 799.9, 274.5, weight=96.0)
    g.diag(711.5, 485.7, 718.4, 480.6, weight=96.0)
    g.diag(718.4, 480.6, 766.6, 207.6, weight=96.0)
    g.diag(766.6, 207.6, 724.4, 147.0, weight=96.0)
    g.hbar(599.3, 932.0, 112.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_96e2() -> Glyph:
    """離 U+96E2 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni96E2", advance=1000, unicode=0x96E2, note="離：自动生成")
    g.diag(282.9, 785.9, 381.8, 728.4, weight=64.0)
    g.hbar(136.5, 434.3, 644.1, weight=84.0)
    g.diag(307.1, 617.4, 330.5, 592.8, weight=96.0)
    g.diag(330.5, 592.8, 220.3, 437.7, weight=96.0)
    g.diag(208.2, 546.7, 340.5, 459.9, weight=48.0)
    g.diag(113.3, 498.2, 139.4, 462.7, weight=48.0)
    g.vbar(134.7, 356.9, 462.7, weight=48.0)
    g.hbar(130.1, 364.1, 385.9, weight=48.0)
    g.diag(364.1, 414.9, 368.7, 422.5, weight=48.0)
    g.diag(406.1, 563.9, 426.3, 530.6, weight=48.0)
    g.diag(426.3, 530.6, 393.0, 382.2, weight=48.0)
    g.diag(79.0, 261.0, 93.7, 249.5, weight=48.0)
    g.vbar(102.5, 6.6, 249.5, weight=48.0)
    g.hbar(124.4, 238.5, 265.6, weight=48.0)
    g.hbar(238.5, 389.5, 240.6, weight=48.0)
    g.vbar(404.0, 32.7, 209.1, weight=48.0)
    g.hbar(328.3, 418.5, 48.5, weight=48.0)
    g.hbar(230.4, 258.9, 352.7, weight=48.0)
    g.diag(258.9, 346.4, 221.2, 149.4, weight=48.0)
    g.diag(221.2, 149.4, 317.3, 194.3, weight=48.0)
    g.hbar(317.3, 326.3, 193.8, weight=48.0)
    g.diag(314.2, 245.9, 363.7, 168.2, weight=48.0)
    g.vbar(569.9, 680.0, 792.0, weight=48.0)
    g.diag(566.2, 680.0, 464.6, 452.8, weight=48.0)
    g.vbar(542.9, -62.0, 520.5, weight=48.0)
    g.dot(727.1, 669.9, w=96.0, h=112.7, slant=-14.0)
    g.hbar(613.0, 870.4, 527.0, weight=96.0)
    g.hbar(628.2, 852.3, 392.3, weight=96.0)
    g.hbar(625.1, 860.3, 274.7, weight=96.0)
    g.diag(701.8, 486.1, 737.3, 463.4, weight=96.0)
    g.vbar(724.5, 158.6, 463.4, weight=96.0)
    g.hbar(586.8, 931.0, 125.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_96ea() -> Glyph:
    """雪 U+96EA —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni96EA", advance=1000, unicode=0x96EA, note="雪：自动生成")
    g.hbar(398.6, 442.1, 718.0, weight=96.0)
    g.hbar(398.6, 642.8, 742.6, weight=96.0)
    g.diag(642.8, 761.2, 707.0, 662.7, weight=96.0)
    g.diag(221.8, 592.2, 154.1, 383.6, weight=96.0)
    g.hbar(253.2, 485.2, 576.6, weight=84.0)
    g.hbar(485.2, 890.8, 601.7, weight=84.0)
    g.diag(890.8, 620.4, 722.4, 483.9, weight=84.0)
    g.diag(479.2, 702.3, 520.0, 668.9, weight=96.0)
    g.vbar(514.3, 267.2, 668.9, weight=96.0)
    g.diag(306.8, 534.7, 392.9, 433.7, weight=64.0)
    g.diag(333.3, 431.8, 386.3, 247.4, weight=96.0)
    g.hbar(538.3, 732.9, 503.3, weight=64.0)
    g.hbar(543.8, 662.5, 390.2, weight=92.0)
    g.vbar(667.1, 285.9, 369.8, weight=92.0)
    g.hbar(308.7, 684.5, 231.3, weight=48.0)
    g.diag(684.5, 250.6, 732.4, 206.4, weight=48.0)
    g.diag(732.4, 206.4, 653.5, 11.1, weight=48.0)
    g.hbar(277.8, 669.3, 92.9, weight=64.0)
    g.hbar(286.3, 725.4, -29.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_96f6() -> Glyph:
    """零 U+96F6 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni96F6", advance=1000, unicode=0x96F6, note="零：自动生成")
    g.diag(400.4, 717.2, 393.1, 729.3, weight=76.0)
    g.hbar(393.1, 606.2, 746.3, weight=76.0)
    g.diag(606.2, 763.3, 638.3, 691.9, weight=76.0)
    g.diag(195.6, 637.6, 154.9, 513.0, weight=96.0)
    g.diag(154.9, 513.0, 240.3, 451.6, weight=96.0)
    g.hbar(226.1, 793.0, 636.0, weight=64.0)
    g.diag(793.0, 657.1, 666.6, 542.1, weight=64.0)
    g.vbar(445.2, 447.6, 708.1, weight=96.0)
    g.diag(290.9, 587.9, 365.8, 511.1, weight=56.0)
    g.diag(296.8, 508.1, 323.6, 435.7, weight=76.0)
    g.diag(323.6, 435.7, 384.1, 393.3, weight=76.0)
    g.diag(560.4, 627.2, 618.6, 551.3, weight=64.0)
    g.hbar(618.6, 672.5, 547.6, weight=64.0)
    g.diag(582.7, 528.3, 614.6, 440.6, weight=84.0)
    g.diag(614.6, 440.6, 640.4, 501.1, weight=84.0)
    g.hbar(461.8, 463.9, 409.5, weight=96.0)
    g.diag(463.9, 409.7, 66.9, 96.6, weight=96.0)
    g.vbar(479.5, 354.7, 388.7, weight=84.0)
    g.hbar(477.6, 933.1, 264.9, weight=84.0)
    g.diag(383.5, 311.1, 459.8, 268.1, weight=48.0)
    g.diag(459.8, 268.1, 494.8, 197.8, weight=48.0)
    g.hbar(251.0, 375.6, 174.4, weight=48.0)
    g.hbar(375.6, 615.2, 169.9, weight=48.0)
    g.diag(615.2, 178.0, 447.2, 31.3, weight=48.0)
    g.diag(375.6, 50.6, 515.7, -67.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_96f7() -> Glyph:
    """雷 U+96F7 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni96F7", advance=1000, unicode=0x96F7, note="雷：自动生成")
    g.hbar(360.9, 674.4, 752.8, weight=84.0)
    g.diag(205.1, 619.1, 169.8, 434.9, weight=84.0)
    g.hbar(248.2, 410.3, 591.6, weight=64.0)
    g.hbar(410.3, 854.3, 614.3, weight=64.0)
    g.diag(854.3, 633.1, 755.7, 524.1, weight=64.0)
    g.diag(474.5, 713.1, 511.5, 681.6, weight=84.0)
    g.vbar(505.8, 340.8, 681.6, weight=84.0)
    g.dot(354.5, 482.9, w=64.0, h=83.2, slant=-14.0)
    g.dot(342.3, 364.4, w=76.0, h=77.5, slant=-14.0)
    g.hbar(586.2, 690.1, 521.6, weight=64.0)
    g.hbar(582.3, 658.7, 416.8, weight=56.0)
    g.diag(658.7, 406.5, 685.2, 378.1, weight=56.0)
    g.diag(250.2, 272.3, 345.2, -26.5, weight=48.0)
    g.hbar(295.2, 616.3, 232.2, weight=48.0)
    g.diag(616.3, 192.1, 674.4, -53.0, weight=48.0)
    g.hbar(398.1, 612.7, 163.0, weight=84.0)
    g.diag(471.6, 254.6, 494.9, 237.4, weight=48.0)
    g.vbar(503.4, 86.0, 237.4, weight=48.0)
    g.diag(511.9, 86.0, 488.2, 57.7, weight=48.0)
    g.diag(361.9, 9.7, 372.6, 22.4, weight=84.0)
    g.hbar(372.6, 631.3, 35.2, weight=84.0)
    return g
def g_cjk_unified_ideograph_9700() -> Glyph:
    """需 U+9700 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9700", advance=1000, unicode=0x9700, note="需：自动生成")
    g.hbar(377.0, 689.0, 749.0, weight=96.0)
    g.diag(230.0, 625.0, 185.0, 442.0, weight=96.0)
    g.hbar(270.0, 445.2, 598.3, weight=56.0)
    g.hbar(445.2, 837.0, 617.9, weight=56.0)
    g.diag(837.0, 633.2, 744.0, 527.0, weight=56.0)
    g.diag(483.0, 707.0, 514.7, 686.7, weight=96.0)
    g.vbar(510.9, 399.0, 686.7, weight=96.0)
    g.diag(329.0, 526.0, 404.0, 491.0, weight=48.0)
    g.dot(356.0, 413.5, w=64.0, h=83.2, slant=-14.0)
    g.dot(638.5, 548.5, w=56.0, h=72.8, slant=-14.0)
    g.dot(644.0, 450.0, w=76.0, h=95.9, slant=-14.0)
    g.hbar(343.0, 669.0, 342.0, weight=48.0)
    g.hbar(460.8, 482.0, 275.9, weight=48.0)
    g.diag(460.8, 276.8, 402.0, 211.0, weight=48.0)
    g.diag(226.0, 193.0, 283.0, -25.0, weight=96.0)
    g.hbar(274.0, 447.2, 184.1, weight=96.0)
    g.hbar(447.2, 798.1, 202.0, weight=96.0)
    g.diag(798.1, 215.8, 725.8, -35.9, weight=96.0)
    g.diag(725.8, -35.9, 639.0, 14.0, weight=96.0)
    g.diag(378.0, 167.0, 406.0, 150.0, weight=96.0)
    g.vbar(409.0, 1.0, 150.0, weight=96.0)
    g.diag(526.0, 191.0, 558.0, 163.0, weight=96.0)
    g.vbar(553.5, -52.0, 163.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_9707() -> Glyph:
    """震 U+9707 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9707", advance=1000, unicode=0x9707, note="震：自动生成")
    g.hbar(403.8, 439.2, 721.9, weight=84.0)
    g.hbar(403.8, 620.7, 743.8, weight=84.0)
    g.diag(620.7, 761.0, 681.2, 695.7, weight=84.0)
    g.diag(238.8, 631.0, 198.7, 513.5, weight=96.0)
    g.diag(198.7, 513.5, 291.7, 465.2, weight=96.0)
    g.hbar(263.2, 437.6, 614.4, weight=56.0)
    g.hbar(437.6, 816.8, 640.5, weight=56.0)
    g.diag(816.8, 660.3, 745.1, 558.5, weight=56.0)
    g.hbar(677.2, 745.1, 554.5, weight=56.0)
    g.diag(471.5, 707.9, 500.2, 686.3, weight=96.0)
    g.vbar(497.5, 412.4, 686.3, weight=96.0)
    g.diag(330.3, 587.8, 405.3, 520.4, weight=48.0)
    g.hbar(330.1, 371.2, 459.8, weight=48.0)
    g.diag(371.2, 453.3, 406.5, 383.9, weight=48.0)
    g.diag(567.5, 627.2, 654.9, 548.5, weight=48.0)
    g.hbar(568.7, 627.8, 492.8, weight=48.0)
    g.vbar(638.9, 428.1, 481.3, weight=48.0)
    g.hbar(375.7, 639.9, 382.5, weight=64.0)
    g.diag(639.9, 406.1, 663.3, 441.9, weight=64.0)
    g.diag(335.0, 424.4, 72.5, -62.0, weight=96.0)
    g.diag(400.3, 336.2, 436.9, 280.5, weight=56.0)
    g.hbar(436.9, 591.5, 295.8, weight=56.0)
    g.diag(591.5, 311.1, 644.2, 256.0, weight=56.0)
    g.hbar(313.8, 754.1, 202.8, weight=48.0)
    g.diag(359.6, 161.2, 378.0, 147.0, weight=48.0)
    g.diag(378.0, 147.0, 407.1, -42.1, weight=48.0)
    g.diag(407.1, -42.1, 528.6, 27.2, weight=48.0)
    g.diag(742.9, 199.3, 620.8, 88.8, weight=76.0)
    g.hbar(609.5, 620.8, 90.4, weight=76.0)
    g.diag(446.1, 178.9, 744.1, -51.7, weight=48.0)
    g.hbar(744.1, 902.5, -55.3, weight=48.0)
    return g
def g_cjk_unified_ideograph_9727() -> Glyph:
    """霧 U+9727 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9727", advance=1000, unicode=0x9727, note="霧：自动生成")
    g.hbar(383.2, 645.4, 751.0, weight=76.0)
    g.dot(230.9, 575.5, w=96.0, h=124.8, slant=14.0)
    g.hbar(287.9, 433.4, 628.0, weight=48.0)
    g.hbar(433.4, 819.0, 652.5, weight=48.0)
    g.diag(819.0, 671.8, 718.0, 582.1, weight=48.0)
    g.vbar(478.0, 470.9, 712.3, weight=96.0)
    g.dot(372.8, 553.4, w=48.0, h=62.4, slant=-14.0)
    g.dot(362.4, 477.5, w=56.0, h=72.8, slant=-14.0)
    g.dot(618.0, 595.8, w=48.0, h=62.4, slant=-14.0)
    g.dot(607.2, 519.4, w=56.0, h=72.8, slant=-14.0)
    g.hbar(199.3, 416.5, 384.1, weight=48.0)
    g.diag(416.5, 401.1, 339.9, 309.6, weight=48.0)
    g.hbar(336.0, 339.9, 309.6, weight=48.0)
    g.dot(310.6, 298.3, w=48.0, h=62.3, slant=-14.0)
    g.hbar(144.6, 442.7, 245.2, weight=48.0)
    g.diag(442.7, 265.7, 372.8, 188.9, weight=48.0)
    g.diag(319.1, 202.1, 286.1, -2.8, weight=48.0)
    g.diag(286.1, -2.8, 238.0, 22.9, weight=48.0)
    g.diag(292.7, 232.3, 113.5, 7.8, weight=48.0)
    g.diag(534.1, 466.1, 551.6, 438.8, weight=96.0)
    g.diag(551.6, 438.8, 470.0, 332.2, weight=96.0)
    g.hbar(560.5, 740.6, 419.0, weight=48.0)
    g.diag(647.3, 392.6, 671.4, 365.6, weight=48.0)
    g.diag(671.4, 365.6, 475.6, 196.4, weight=48.0)
    g.hbar(521.8, 891.5, 295.9, weight=56.0)
    g.hbar(431.3, 725.2, 145.5, weight=64.0)
    g.vbar(681.7, -64.7, 168.2, weight=64.0)
    g.hbar(574.6, 638.2, -51.6, weight=64.0)
    g.diag(574.6, -38.4, 571.8, -32.8, weight=64.0)
    g.diag(561.4, 220.9, 544.0, 149.1, weight=48.0)
    g.diag(544.0, 149.1, 410.5, -62.0, weight=48.0)
    return g
def g_cjk_unified_ideograph_9732() -> Glyph:
    """露 U+9732 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9732", advance=1000, unicode=0x9732, note="露：自动生成")
    g.hbar(294.7, 604.5, 750.5, weight=76.0)
    g.diag(195.9, 655.0, 159.2, 477.1, weight=96.0)
    g.hbar(229.8, 757.4, 647.0, weight=48.0)
    g.diag(757.4, 666.4, 652.5, 580.6, weight=48.0)
    g.diag(421.8, 715.2, 449.1, 689.8, weight=64.0)
    g.vbar(444.9, 454.5, 689.8, weight=64.0)
    g.dot(334.8, 562.7, w=48.0, h=62.4, slant=-14.0)
    g.dot(321.6, 485.5, w=48.0, h=62.4, slant=-14.0)
    g.dot(562.6, 587.2, w=48.0, h=62.4, slant=-14.0)
    g.dot(558.3, 506.2, w=56.0, h=72.8, slant=-14.0)
    g.diag(175.2, 406.5, 228.9, 268.1, weight=48.0)
    g.diag(219.4, 405.5, 223.9, 401.0, weight=48.0)
    g.hbar(223.9, 363.8, 408.1, weight=48.0)
    g.diag(363.8, 415.2, 340.0, 341.6, weight=48.0)
    g.diag(340.0, 341.6, 319.2, 325.5, weight=48.0)
    g.dot(305.6, 292.1, w=84.0, h=109.2, slant=-14.0)
    g.diag(262.7, 272.8, 287.5, 248.5, weight=56.0)
    g.vbar(286.6, 97.0, 248.5, weight=56.0)
    g.diag(285.6, 97.0, 272.2, 83.6, weight=56.0)
    g.diag(313.6, 185.2, 330.2, 200.8, weight=48.0)
    g.hbar(330.2, 388.9, 202.0, weight=48.0)
    g.diag(142.2, 211.6, 176.3, 181.3, weight=76.0)
    g.diag(176.3, 181.3, 198.9, 74.1, weight=76.0)
    g.diag(198.9, 74.1, 189.3, 66.6, weight=76.0)
    g.hbar(110.2, 395.5, 66.6, weight=48.0)
    g.hbar(531.7, 542.3, 433.4, weight=48.0)
    g.diag(531.7, 431.2, 408.7, 277.5, weight=48.0)
    g.diag(539.5, 398.0, 569.5, 332.9, weight=48.0)
    g.diag(569.5, 332.9, 375.7, 148.5, weight=48.0)
    g.diag(485.8, 329.3, 607.0, 271.0, weight=64.0)
    g.hbar(607.0, 904.8, 219.2, weight=64.0)
    g.diag(436.9, 120.3, 488.7, -52.0, weight=48.0)
    g.diag(484.0, 118.4, 490.8, 113.1, weight=48.0)
    g.hbar(490.8, 682.7, 119.7, weight=48.0)
    g.diag(682.7, 126.3, 654.4, 45.0, weight=48.0)
    g.diag(654.4, 45.0, 632.7, 27.1, weight=48.0)
    g.hbar(507.5, 686.4, -13.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_9774() -> Glyph:
    """靴 U+9774 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9774", advance=1000, unicode=0x9774, note="靴：自动生成")
    g.hbar(169.9, 200.7, 592.7, weight=84.0)
    g.hbar(169.9, 524.9, 614.0, weight=84.0)
    g.diag(187.1, 701.7, 224.8, 676.0, weight=48.0)
    g.diag(224.8, 676.0, 256.9, 467.4, weight=48.0)
    g.diag(367.4, 777.0, 398.1, 739.4, weight=84.0)
    g.diag(398.1, 739.4, 362.4, 561.1, weight=84.0)
    g.diag(362.4, 561.1, 345.6, 544.2, weight=84.0)
    g.hbar(267.3, 371.0, 507.9, weight=76.0)
    g.diag(371.0, 525.1, 375.0, 530.7, weight=76.0)
    g.vbar(166.3, 233.2, 386.8, weight=84.0)
    g.hbar(159.9, 439.2, 402.1, weight=48.0)
    g.diag(439.2, 417.7, 388.7, 314.6, weight=48.0)
    g.hbar(213.9, 451.4, 279.2, weight=48.0)
    g.hbar(76.2, 509.9, 160.7, weight=84.0)
    g.diag(268.3, 482.8, 289.5, 344.7, weight=48.0)
    g.vbar(296.3, -52.0, 344.7, weight=48.0)
    g.diag(558.5, 639.3, 599.2, 607.3, weight=48.0)
    g.diag(599.2, 607.3, 446.7, 303.8, weight=48.0)
    g.vbar(530.6, 8.4, 377.9, weight=48.0)
    g.diag(822.0, 517.5, 852.8, 472.1, weight=48.0)
    g.diag(852.8, 472.1, 564.9, 241.2, weight=48.0)
    g.diag(623.9, 633.8, 671.9, 463.7, weight=96.0)
    g.diag(671.9, 463.7, 899.5, 54.7, weight=96.0)
    g.hbar(899.5, 936.2, 54.9, weight=96.0)
    g.vbar(940.0, 55.0, 207.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_97d3() -> Glyph:
    """韓 U+97D3 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni97D3", advance=1000, unicode=0x97D3, note="韓：自动生成")
    g.hbar(217.1, 468.0, 613.2, weight=96.0)
    g.diag(329.9, 762.1, 359.7, 726.9, weight=96.0)
    g.diag(359.7, 726.9, 317.3, 518.4, weight=96.0)
    g.diag(317.3, 518.4, 300.1, 503.1, weight=96.0)
    g.diag(174.6, 477.8, 246.9, 284.7, weight=48.0)
    g.hbar(222.5, 305.1, 476.8, weight=48.0)
    g.hbar(305.1, 456.5, 487.5, weight=48.0)
    g.diag(456.5, 495.6, 401.2, 299.1, weight=48.0)
    g.diag(248.7, 376.7, 256.2, 387.5, weight=64.0)
    g.hbar(256.2, 370.5, 396.1, weight=64.0)
    g.diag(260.4, 295.5, 270.0, 306.0, weight=64.0)
    g.hbar(270.0, 370.5, 317.9, weight=64.0)
    g.hbar(103.3, 451.7, 199.8, weight=64.0)
    g.diag(303.7, 294.6, 330.9, 269.9, weight=96.0)
    g.vbar(325.4, -16.8, 269.9, weight=96.0)
    g.diag(630.5, 782.0, 660.2, 747.7, weight=96.0)
    g.diag(660.2, 747.7, 628.7, 563.6, weight=96.0)
    g.diag(628.7, 563.6, 613.3, 548.2, weight=96.0)
    g.hbar(551.9, 799.2, 654.6, weight=48.0)
    g.diag(799.2, 671.6, 752.3, 582.5, weight=48.0)
    g.hbar(510.4, 906.7, 538.8, weight=48.0)
    g.diag(534.8, 458.9, 561.0, 435.4, weight=96.0)
    g.vbar(575.4, 341.5, 435.4, weight=96.0)
    g.diag(580.8, 457.1, 584.2, 454.1, weight=48.0)
    g.hbar(584.2, 786.1, 463.7, weight=48.0)
    g.diag(786.1, 473.4, 734.3, 409.2, weight=48.0)
    g.hbar(602.5, 774.0, 366.8, weight=48.0)
    g.hbar(586.2, 802.0, 290.1, weight=64.0)
    g.diag(520.3, 261.2, 542.0, 237.7, weight=96.0)
    g.diag(542.0, 237.7, 523.1, 135.2, weight=96.0)
    g.hbar(523.1, 891.3, 150.4, weight=96.0)
    g.diag(653.0, 351.5, 686.4, 329.8, weight=96.0)
    g.vbar(682.8, -52.0, 329.8, weight=96.0)
    return g
def g_cjk_unified_ideograph_97fb() -> Glyph:
    """韻 U+97FB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni97FB", advance=1000, unicode=0x97FB, note="韻：自动生成")
    g.diag(339.0, 792.0, 414.4, 756.8, weight=64.0)
    g.diag(414.4, 756.8, 456.6, 663.7, weight=64.0)
    g.vbar(219.3, 565.7, 583.8, weight=96.0)
    g.hbar(220.1, 441.2, 609.6, weight=96.0)
    g.diag(441.2, 635.3, 472.7, 689.9, weight=96.0)
    g.dot(269.8, 504.3, w=96.0, h=106.4, slant=-14.0)
    g.diag(409.4, 603.9, 440.2, 568.8, weight=96.0)
    g.diag(440.2, 568.8, 380.2, 460.1, weight=96.0)
    g.diag(163.4, 339.8, 145.8, 381.9, weight=96.0)
    g.hbar(145.8, 542.6, 429.6, weight=96.0)
    g.vbar(228.4, 86.0, 312.7, weight=48.0)
    g.diag(231.2, 86.0, 252.8, 60.9, weight=48.0)
    g.diag(232.2, 300.2, 391.3, 224.0, weight=48.0)
    g.diag(391.3, 224.0, 434.6, 21.5, weight=48.0)
    g.diag(260.6, 186.5, 268.5, 201.1, weight=84.0)
    g.hbar(268.5, 401.1, 203.1, weight=84.0)
    g.dot(326.1, 90.0, w=92.0, h=119.6, slant=-14.0)
    g.vbar(615.6, 729.4, 743.8, weight=48.0)
    g.diag(615.6, 729.4, 680.1, 593.5, weight=48.0)
    g.hbar(629.2, 894.5, 755.6, weight=48.0)
    g.diag(894.5, 771.0, 825.0, 654.6, weight=48.0)
    g.hbar(674.6, 692.9, 612.2, weight=48.0)
    g.hbar(692.9, 860.3, 634.7, weight=48.0)
    g.vbar(599.7, 429.5, 500.3, weight=48.0)
    g.diag(599.9, 429.5, 568.0, 228.3, weight=48.0)
    g.diag(568.0, 228.3, 606.3, 148.6, weight=48.0)
    g.hbar(611.4, 815.6, 465.6, weight=48.0)
    g.vbar(854.6, 206.8, 436.8, weight=48.0)
    g.diag(893.6, 206.8, 856.7, 173.1, weight=48.0)
    g.diag(635.7, 376.6, 648.7, 392.4, weight=76.0)
    g.hbar(648.7, 853.0, 397.2, weight=76.0)
    g.diag(636.1, 272.1, 648.9, 286.8, weight=76.0)
    g.hbar(648.9, 857.1, 292.6, weight=76.0)
    g.hbar(620.6, 859.1, 173.3, weight=76.0)
    g.diag(677.3, 150.0, 517.6, -59.8, weight=76.0)
    g.diag(517.6, -59.8, 446.1, -6.6, weight=76.0)
    g.diag(789.4, 156.8, 928.4, -54.9, weight=96.0)
    return g
def g_cjk_unified_ideograph_9802() -> Glyph:
    """頂 U+9802 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9802", advance=1000, unicode=0x9802, note="頂：自动生成")
    g.hbar(97.1, 440.4, 693.0, weight=96.0)
    g.diag(231.3, 644.6, 269.3, 454.0, weight=96.0)
    g.vbar(266.4, 91.9, 454.0, weight=96.0)
    g.diag(263.4, 91.9, 132.4, 152.5, weight=96.0)
    g.hbar(484.1, 917.9, 723.7, weight=96.0)
    g.diag(638.1, 696.7, 663.6, 665.3, weight=48.0)
    g.diag(663.6, 665.3, 584.0, 561.4, weight=48.0)
    g.vbar(520.0, 160.8, 563.5, weight=96.0)
    g.hbar(562.1, 653.4, 539.2, weight=48.0)
    g.diag(653.4, 549.3, 778.4, 455.3, weight=48.0)
    g.vbar(795.1, 153.6, 455.3, weight=48.0)
    g.hbar(568.4, 734.8, 441.8, weight=92.0)
    g.hbar(568.4, 743.2, 328.4, weight=92.0)
    g.hbar(563.2, 757.8, 194.2, weight=76.0)
    g.diag(757.8, 210.9, 771.2, 196.2, weight=76.0)
    g.hbar(603.8, 619.3, 100.1, weight=76.0)
    g.diag(603.8, 98.7, 392.5, -59.7, weight=76.0)
    g.diag(739.0, 118.2, 894.0, -67.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_9803() -> Glyph:
    """頃 U+9803 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9803", advance=1000, unicode=0x9803, note="頃：自动生成")
    g.hbar(227.1, 418.0, 539.6, weight=96.0)
    g.diag(139.9, 689.0, 240.2, 277.4, weight=76.0)
    g.hbar(240.2, 455.6, 322.5, weight=76.0)
    g.diag(444.4, 610.1, 471.8, 703.3, weight=96.0)
    g.hbar(471.8, 900.1, 722.7, weight=96.0)
    g.diag(568.4, 689.0, 593.7, 665.8, weight=96.0)
    g.diag(593.7, 665.8, 543.9, 573.1, weight=96.0)
    g.vbar(487.1, 462.5, 565.6, weight=48.0)
    g.vbar(493.6, 179.5, 462.5, weight=48.0)
    g.hbar(497.2, 757.1, 575.2, weight=48.0)
    g.diag(757.1, 593.9, 797.3, 552.5, weight=48.0)
    g.vbar(788.7, 234.7, 552.5, weight=48.0)
    g.diag(780.1, 234.7, 752.8, 206.2, weight=48.0)
    g.hbar(519.8, 754.1, 443.1, weight=84.0)
    g.hbar(518.4, 751.8, 335.1, weight=92.0)
    g.diag(515.2, 192.4, 534.3, 208.9, weight=84.0)
    g.hbar(534.3, 752.9, 213.8, weight=84.0)
    g.diag(580.5, 179.1, 341.9, -54.2, weight=84.0)
    g.diag(680.9, 188.0, 870.3, -67.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_9812() -> Glyph:
    """頒 U+9812 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9812", advance=1000, unicode=0x9812, note="頒：自动生成")
    g.diag(188.7, 651.3, 223.2, 609.5, weight=96.0)
    g.diag(223.2, 609.5, 122.8, 373.6, weight=96.0)
    g.diag(326.7, 767.0, 476.6, 579.3, weight=96.0)
    g.diag(135.8, 408.2, 182.7, 377.0, weight=48.0)
    g.diag(182.7, 377.0, 334.7, 292.3, weight=48.0)
    g.vbar(325.7, 69.0, 292.3, weight=48.0)
    g.diag(316.7, 69.0, 234.4, 114.4, weight=48.0)
    g.diag(220.6, 356.4, 250.2, 334.2, weight=96.0)
    g.diag(250.2, 334.2, 55.0, 66.7, weight=96.0)
    g.hbar(458.4, 941.0, 710.7, weight=96.0)
    g.diag(632.0, 689.2, 656.5, 658.7, weight=48.0)
    g.diag(656.5, 658.7, 592.9, 559.4, weight=48.0)
    g.diag(537.2, 552.0, 510.3, 480.9, weight=48.0)
    g.vbar(527.6, 165.3, 480.9, weight=48.0)
    g.hbar(549.1, 584.2, 541.3, weight=48.0)
    g.hbar(584.2, 795.2, 559.0, weight=48.0)
    g.diag(795.2, 579.8, 823.2, 550.9, weight=48.0)
    g.vbar(832.1, 243.6, 550.9, weight=48.0)
    g.diag(841.1, 243.6, 794.1, 183.4, weight=48.0)
    g.hbar(569.7, 788.8, 437.1, weight=96.0)
    g.diag(568.6, 310.7, 577.1, 317.1, weight=96.0)
    g.hbar(577.1, 792.4, 324.0, weight=96.0)
    g.diag(559.9, 177.0, 574.0, 192.0, weight=64.0)
    g.hbar(574.0, 767.4, 202.7, weight=64.0)
    g.diag(767.4, 213.5, 804.4, 193.8, weight=64.0)
    g.diag(630.4, 172.6, 390.3, -62.8, weight=64.0)
    g.diag(793.5, 135.0, 896.5, -67.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_9813() -> Glyph:
    """頓 U+9813 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9813", advance=1000, unicode=0x9813, note="頓：自动生成")
    g.diag(119.5, 469.6, 156.9, 523.6, weight=96.0)
    g.hbar(156.9, 368.0, 553.7, weight=96.0)
    g.hbar(368.0, 442.0, 573.1, weight=96.0)
    g.vbar(133.1, 283.9, 495.8, weight=96.0)
    g.hbar(138.9, 341.6, 327.0, weight=96.0)
    g.diag(341.6, 370.0, 356.8, 387.9, weight=96.0)
    g.diag(358.2, 543.2, 400.7, 462.7, weight=92.0)
    g.diag(400.7, 462.7, 360.7, 337.6, weight=92.0)
    g.diag(220.2, 772.0, 246.6, 600.0, weight=76.0)
    g.vbar(242.7, 111.1, 600.0, weight=76.0)
    g.diag(238.8, 111.1, 389.6, 282.7, weight=76.0)
    g.hbar(423.9, 896.6, 676.5, weight=96.0)
    g.diag(574.6, 675.0, 606.6, 645.1, weight=48.0)
    g.diag(606.6, 645.1, 561.4, 546.5, weight=48.0)
    g.vbar(502.5, 434.8, 535.1, weight=48.0)
    g.vbar(507.4, 169.8, 434.8, weight=48.0)
    g.hbar(513.8, 736.6, 548.4, weight=48.0)
    g.diag(736.6, 569.9, 781.6, 534.9, weight=48.0)
    g.vbar(786.7, 228.8, 534.9, weight=48.0)
    g.diag(791.8, 228.8, 751.4, 196.6, weight=48.0)
    g.diag(534.4, 416.8, 541.9, 423.4, weight=96.0)
    g.hbar(541.9, 744.0, 435.8, weight=96.0)
    g.hbar(534.4, 747.9, 318.8, weight=96.0)
    g.diag(528.4, 180.4, 554.5, 201.7, weight=96.0)
    g.hbar(554.5, 749.6, 205.5, weight=96.0)
    g.diag(541.3, 144.2, 564.5, 100.9, weight=96.0)
    g.diag(564.5, 100.9, 359.8, -52.0, weight=96.0)
    g.diag(748.5, 148.3, 842.7, -67.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_9818() -> Glyph:
    """領 U+9818 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9818", advance=1000, unicode=0x9818, note="領：自动生成")
    g.diag(368.3, 676.8, 365.0, 693.3, weight=96.0)
    g.diag(365.0, 693.3, 74.6, 260.9, weight=96.0)
    g.hbar(381.9, 401.2, 643.5, weight=96.0)
    g.diag(401.2, 645.6, 514.7, 535.9, weight=96.0)
    g.diag(324.2, 513.8, 397.5, 459.9, weight=96.0)
    g.vbar(401.0, 373.4, 459.9, weight=96.0)
    g.hbar(218.2, 242.1, 288.7, weight=48.0)
    g.hbar(242.1, 460.5, 310.6, weight=48.0)
    g.diag(460.5, 334.5, 340.8, 166.3, weight=48.0)
    g.diag(270.7, 186.6, 394.5, 75.6, weight=48.0)
    g.hbar(488.8, 920.4, 661.6, weight=76.0)
    g.diag(654.0, 652.1, 680.2, 620.7, weight=96.0)
    g.diag(680.2, 620.7, 612.4, 508.5, weight=96.0)
    g.vbar(564.3, 158.9, 500.8, weight=48.0)
    g.hbar(574.8, 678.5, 496.7, weight=48.0)
    g.diag(678.5, 498.8, 810.0, 429.5, weight=48.0)
    g.diag(810.0, 429.5, 850.1, 212.3, weight=48.0)
    g.diag(850.1, 212.3, 810.6, 177.4, weight=48.0)
    g.hbar(591.6, 711.4, 394.7, weight=76.0)
    g.diag(711.4, 412.6, 738.4, 339.5, weight=76.0)
    g.hbar(592.6, 817.5, 290.7, weight=84.0)
    g.diag(586.6, 167.7, 601.9, 185.4, weight=76.0)
    g.hbar(601.9, 816.9, 187.3, weight=76.0)
    g.diag(646.3, 158.1, 432.1, -67.0, weight=76.0)
    g.diag(780.0, 157.4, 892.7, -62.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_982d() -> Glyph:
    """頭 U+982D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni982D", advance=1000, unicode=0x982D, note="頭：自动生成")
    g.hbar(211.9, 525.9, 699.9, weight=96.0)
    g.vbar(224.8, 352.4, 522.3, weight=48.0)
    g.hbar(201.8, 452.6, 529.5, weight=48.0)
    g.diag(452.6, 546.7, 384.7, 425.2, weight=48.0)
    g.diag(260.0, 367.4, 272.7, 380.6, weight=48.0)
    g.hbar(272.7, 415.3, 405.4, weight=48.0)
    g.diag(216.8, 318.1, 269.9, 161.6, weight=96.0)
    g.diag(373.5, 367.1, 402.0, 299.0, weight=96.0)
    g.diag(402.0, 299.0, 332.1, 167.2, weight=96.0)
    g.hbar(93.7, 152.3, 87.2, weight=96.0)
    g.diag(152.3, 78.4, 408.5, 219.9, weight=96.0)
    g.hbar(594.6, 625.6, 698.7, weight=96.0)
    g.hbar(594.6, 931.3, 730.0, weight=96.0)
    g.diag(662.6, 683.8, 689.8, 648.9, weight=96.0)
    g.diag(689.8, 648.9, 621.8, 555.2, weight=96.0)
    g.vbar(579.0, 181.5, 549.7, weight=48.0)
    g.hbar(582.4, 809.4, 557.6, weight=48.0)
    g.diag(809.4, 573.0, 889.9, 284.6, weight=48.0)
    g.diag(889.9, 284.6, 808.1, 198.8, weight=48.0)
    g.hbar(607.1, 811.0, 434.8, weight=84.0)
    g.diag(605.0, 333.5, 616.6, 328.2, weight=84.0)
    g.hbar(616.6, 813.3, 339.9, weight=84.0)
    g.diag(603.0, 194.4, 618.6, 208.7, weight=76.0)
    g.hbar(618.6, 816.5, 210.1, weight=76.0)
    g.diag(666.1, 182.0, 403.2, -66.0, weight=76.0)
    g.diag(808.5, 141.9, 910.4, -67.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_9830() -> Glyph:
    """頰 U+9830 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9830", advance=1000, unicode=0x9830, note="頰：自动生成")
    g.hbar(204.5, 508.6, 601.1, weight=96.0)
    g.vbar(293.9, 490.7, 782.0, weight=64.0)
    g.diag(286.5, 490.7, 105.6, 8.3, weight=64.0)
    g.diag(341.4, 245.1, 313.7, 284.1, weight=96.0)
    g.diag(313.7, 284.1, 499.8, 44.1, weight=96.0)
    g.diag(205.4, 548.1, 221.1, 469.5, weight=96.0)
    g.diag(221.1, 469.5, 142.5, 336.7, weight=96.0)
    g.hbar(142.5, 159.5, 339.5, weight=96.0)
    g.hbar(190.9, 202.8, 364.1, weight=96.0)
    g.diag(202.8, 363.6, 281.5, 313.3, weight=96.0)
    g.diag(459.8, 527.1, 481.9, 498.8, weight=48.0)
    g.diag(481.9, 498.8, 425.8, 382.6, weight=48.0)
    g.dot(494.9, 362.6, w=96.0, h=119.3, slant=-14.0)
    g.hbar(542.1, 916.5, 700.7, weight=48.0)
    g.diag(701.7, 670.6, 695.9, 645.0, weight=48.0)
    g.diag(695.9, 645.0, 616.4, 545.2, weight=48.0)
    g.vbar(584.8, 188.0, 538.2, weight=48.0)
    g.hbar(598.9, 683.0, 538.7, weight=48.0)
    g.hbar(683.0, 824.4, 546.5, weight=48.0)
    g.vbar(833.3, 242.1, 552.8, weight=48.0)
    g.diag(842.1, 242.1, 795.7, 201.6, weight=48.0)
    g.hbar(613.4, 798.5, 428.1, weight=76.0)
    g.hbar(613.4, 801.7, 325.1, weight=76.0)
    g.hbar(608.4, 799.7, 207.8, weight=84.0)
    g.hbar(641.2, 713.3, 117.5, weight=84.0)
    g.diag(641.2, 110.5, 440.8, -29.9, weight=84.0)
    g.diag(698.8, 120.9, 887.4, -67.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_983b() -> Glyph:
    """頻 U+983B —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni983B", advance=1000, unicode=0x983B, note="頻：自动生成")
    g.diag(337.2, 772.0, 378.6, 736.5, weight=84.0)
    g.vbar(376.8, 521.6, 736.5, weight=84.0)
    g.diag(374.9, 521.6, 358.9, 501.5, weight=84.0)
    g.diag(406.1, 601.8, 411.8, 614.5, weight=92.0)
    g.hbar(411.8, 513.3, 633.0, weight=92.0)
    g.diag(213.3, 604.8, 273.2, 495.1, weight=96.0)
    g.diag(273.2, 495.1, 253.6, 474.0, weight=96.0)
    g.hbar(85.4, 511.2, 462.2, weight=96.0)
    g.diag(352.0, 451.4, 379.4, 431.4, weight=64.0)
    g.diag(379.4, 431.4, 355.8, 267.8, weight=64.0)
    g.hbar(238.2, 355.8, 288.8, weight=64.0)
    g.diag(215.3, 390.2, 169.0, 207.4, weight=96.0)
    g.vbar(397.5, 262.5, 398.7, weight=76.0)
    g.diag(389.9, 262.5, 113.9, -60.1, weight=76.0)
    g.hbar(521.2, 914.6, 694.7, weight=96.0)
    g.diag(653.9, 657.9, 679.5, 630.3, weight=96.0)
    g.diag(679.5, 630.3, 622.5, 531.0, weight=96.0)
    g.vbar(574.4, 426.4, 524.7, weight=48.0)
    g.vbar(575.2, 165.1, 426.4, weight=48.0)
    g.hbar(586.4, 763.8, 487.2, weight=48.0)
    g.diag(763.8, 457.3, 860.0, 278.6, weight=48.0)
    g.diag(860.0, 278.6, 785.8, 184.3, weight=48.0)
    g.hbar(600.8, 789.0, 417.7, weight=76.0)
    g.hbar(602.8, 791.1, 320.6, weight=76.0)
    g.hbar(592.9, 794.8, 185.7, weight=64.0)
    g.diag(645.7, 166.2, 409.0, -44.4, weight=64.0)
    g.diag(757.2, 160.8, 885.1, -67.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_984c() -> Glyph:
    """題 U+984C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni984C", advance=1000, unicode=0x984C, note="題：自动生成")
    g.diag(251.1, 713.6, 242.6, 695.7, weight=48.0)
    g.vbar(268.7, 457.0, 695.7, weight=48.0)
    g.hbar(257.9, 506.5, 717.9, weight=48.0)
    g.vbar(481.5, 490.5, 731.9, weight=48.0)
    g.hbar(431.0, 456.4, 493.0, weight=48.0)
    g.diag(293.5, 582.7, 303.8, 597.5, weight=84.0)
    g.hbar(303.8, 447.1, 599.7, weight=84.0)
    g.diag(304.0, 473.8, 314.6, 484.4, weight=84.0)
    g.hbar(314.6, 424.4, 494.9, weight=84.0)
    g.diag(179.4, 281.8, 152.0, 328.0, weight=96.0)
    g.hbar(152.0, 577.5, 364.7, weight=96.0)
    g.diag(345.3, 353.3, 377.0, 322.7, weight=96.0)
    g.vbar(375.9, 158.8, 322.7, weight=96.0)
    g.diag(374.9, 158.8, 393.9, 127.1, weight=96.0)
    g.hbar(407.6, 577.8, 251.6, weight=96.0)
    g.diag(204.5, 297.9, 242.2, 218.6, weight=96.0)
    g.diag(242.2, 218.6, 63.0, 7.6, weight=96.0)
    g.diag(262.9, 193.1, 418.6, 111.0, weight=96.0)
    g.hbar(418.6, 918.2, 19.5, weight=96.0)
    g.diag(918.2, -72.0, 893.7, 41.4, weight=96.0)
    g.hbar(597.9, 898.2, 702.2, weight=48.0)
    g.diag(739.1, 675.1, 736.0, 651.2, weight=48.0)
    g.diag(736.0, 651.2, 671.9, 561.6, weight=48.0)
    g.vbar(608.0, 527.9, 545.3, weight=48.0)
    g.vbar(618.8, 237.7, 527.9, weight=48.0)
    g.hbar(625.0, 797.7, 559.6, weight=48.0)
    g.vbar(814.3, 450.6, 580.6, weight=48.0)
    g.vbar(825.6, 187.9, 450.6, weight=48.0)
    g.diag(641.9, 435.8, 657.8, 451.1, weight=64.0)
    g.hbar(657.8, 820.7, 455.7, weight=64.0)
    g.hbar(641.1, 822.6, 361.9, weight=64.0)
    g.diag(646.6, 251.8, 656.1, 265.6, weight=76.0)
    g.hbar(656.1, 812.3, 276.6, weight=76.0)
    g.hbar(676.2, 756.3, 180.4, weight=76.0)
    g.diag(676.2, 172.9, 548.2, 47.3, weight=76.0)
    g.diag(816.5, 206.2, 882.2, 3.7, weight=92.0)
    return g
def g_cjk_unified_ideograph_984d() -> Glyph:
    """額 U+984D —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni984D", advance=1000, unicode=0x984D, note="額：自动生成")
    g.diag(315.5, 782.0, 383.9, 743.6, weight=48.0)
    g.diag(383.9, 743.6, 415.8, 669.9, weight=48.0)
    g.diag(192.5, 624.6, 158.1, 515.4, weight=84.0)
    g.diag(158.1, 515.4, 219.4, 446.5, weight=84.0)
    g.hbar(214.9, 489.4, 628.8, weight=96.0)
    g.diag(489.4, 658.1, 514.3, 550.8, weight=96.0)
    g.hbar(306.6, 332.1, 526.5, weight=48.0)
    g.diag(306.6, 522.0, 160.0, 329.0, weight=48.0)
    g.diag(275.5, 439.8, 330.9, 376.7, weight=48.0)
    g.diag(330.9, 376.7, 91.6, 104.0, weight=48.0)
    g.hbar(249.1, 538.9, 314.5, weight=96.0)
    g.diag(217.5, 169.1, 242.2, 155.1, weight=48.0)
    g.vbar(262.1, 21.7, 155.1, weight=48.0)
    g.hbar(255.6, 461.9, 181.3, weight=48.0)
    g.diag(461.9, 194.5, 395.8, 90.9, weight=48.0)
    g.hbar(286.0, 432.1, 68.6, weight=48.0)
    g.hbar(653.2, 908.4, 704.6, weight=96.0)
    g.diag(689.7, 662.8, 711.7, 639.7, weight=96.0)
    g.diag(711.7, 639.7, 647.2, 546.7, weight=96.0)
    g.vbar(581.5, 444.9, 535.4, weight=48.0)
    g.vbar(585.2, 183.7, 444.9, weight=48.0)
    g.hbar(592.6, 800.5, 544.6, weight=48.0)
    g.vbar(813.6, 449.4, 561.5, weight=48.0)
    g.vbar(829.2, 177.6, 449.4, weight=48.0)
    g.hbar(605.7, 805.6, 421.4, weight=76.0)
    g.hbar(606.8, 804.7, 322.2, weight=84.0)
    g.hbar(605.7, 804.5, 217.5, weight=84.0)
    g.hbar(659.3, 734.9, 108.8, weight=84.0)
    g.diag(659.3, 112.3, 458.5, -58.7, weight=84.0)
    g.diag(717.5, 109.9, 901.2, -67.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_984e() -> Glyph:
    """顎 U+984E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni984E", advance=1000, unicode=0x984E, note="顎：自动生成")
    g.vbar(186.8, 523.2, 670.6, weight=48.0)
    g.hbar(179.0, 319.7, 681.9, weight=48.0)
    g.diag(319.7, 699.4, 239.8, 549.9, weight=48.0)
    g.diag(239.8, 549.9, 274.0, 582.1, weight=48.0)
    g.diag(217.4, 540.5, 225.2, 550.5, weight=64.0)
    g.hbar(225.2, 303.4, 562.6, weight=64.0)
    g.vbar(385.8, 576.6, 721.5, weight=48.0)
    g.hbar(382.7, 513.6, 718.9, weight=48.0)
    g.vbar(501.6, 649.4, 724.8, weight=48.0)
    g.diag(489.6, 649.4, 469.8, 632.8, weight=48.0)
    g.diag(408.5, 594.0, 418.5, 604.0, weight=76.0)
    g.hbar(418.5, 507.6, 614.4, weight=76.0)
    g.hbar(214.4, 281.8, 477.7, weight=64.0)
    g.hbar(281.8, 393.6, 485.6, weight=64.0)
    g.diag(393.6, 502.9, 408.7, 546.7, weight=64.0)
    g.hbar(63.0, 544.0, 363.4, weight=84.0)
    g.diag(273.8, 338.6, 293.2, 320.1, weight=96.0)
    g.diag(293.2, 320.1, 254.2, 231.5, weight=96.0)
    g.hbar(254.2, 446.1, 232.6, weight=96.0)
    g.diag(446.1, 233.7, 309.0, -34.0, weight=96.0)
    g.diag(309.0, -34.0, 217.4, 40.6, weight=96.0)
    g.hbar(539.6, 942.0, 689.8, weight=96.0)
    g.diag(675.7, 656.3, 697.3, 627.4, weight=96.0)
    g.diag(697.3, 627.4, 635.1, 541.5, weight=96.0)
    g.vbar(577.1, 192.0, 533.5, weight=48.0)
    g.hbar(584.7, 773.6, 484.7, weight=48.0)
    g.vbar(809.6, 229.7, 442.4, weight=48.0)
    g.hbar(798.4, 845.7, 220.5, weight=48.0)
    g.hbar(599.5, 795.2, 417.7, weight=76.0)
    g.diag(602.5, 326.7, 607.3, 321.8, weight=76.0)
    g.hbar(607.3, 798.0, 328.6, weight=76.0)
    g.diag(598.5, 203.9, 609.8, 217.2, weight=84.0)
    g.hbar(609.8, 767.0, 227.9, weight=84.0)
    g.diag(767.0, 238.6, 791.7, 224.2, weight=84.0)
    g.diag(596.9, 159.9, 610.9, 105.1, weight=84.0)
    g.diag(610.9, 105.1, 486.9, -7.5, weight=84.0)
    g.hbar(384.6, 486.9, 1.8, weight=84.0)
    g.diag(677.4, 114.8, 872.7, -43.5, weight=96.0)
    return g
def g_cjk_unified_ideograph_9858() -> Glyph:
    """願 U+9858 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9858", advance=1000, unicode=0x9858, note="願：自动生成")
    g.hbar(297.2, 514.3, 689.3, weight=96.0)
    g.hbar(514.3, 553.2, 701.9, weight=96.0)
    g.diag(279.1, 675.9, 229.0, 515.9, weight=48.0)
    g.diag(229.0, 515.9, 58.0, 69.4, weight=48.0)
    g.diag(399.8, 656.4, 426.0, 631.4, weight=64.0)
    g.diag(426.0, 631.4, 360.0, 513.9, weight=64.0)
    g.diag(267.5, 496.0, 300.2, 462.1, weight=48.0)
    g.vbar(313.6, 297.6, 462.1, weight=48.0)
    g.hbar(307.2, 523.9, 500.3, weight=48.0)
    g.diag(523.9, 515.1, 471.6, 314.6, weight=48.0)
    g.diag(471.6, 314.6, 463.3, 310.8, weight=48.0)
    g.hbar(332.8, 469.7, 391.9, weight=56.0)
    g.hbar(339.0, 430.9, 324.9, weight=64.0)
    g.diag(430.9, 337.2, 446.0, 315.6, weight=64.0)
    g.diag(370.8, 307.2, 406.8, 283.6, weight=48.0)
    g.diag(406.8, 283.6, 370.3, 56.7, weight=48.0)
    g.hbar(304.2, 370.3, 70.5, weight=48.0)
    g.diag(304.1, 259.3, 255.3, 154.1, weight=96.0)
    g.diag(255.3, 154.1, 265.8, 85.7, weight=96.0)
    g.diag(435.5, 203.2, 521.4, 150.2, weight=96.0)
    g.hbar(521.4, 580.4, 155.1, weight=96.0)
    g.hbar(563.4, 603.1, 670.0, weight=96.0)
    g.hbar(603.1, 942.0, 682.6, weight=96.0)
    g.diag(691.8, 657.6, 714.0, 631.1, weight=48.0)
    g.diag(714.0, 631.1, 651.0, 541.8, weight=48.0)
    g.vbar(618.4, 189.8, 535.4, weight=48.0)
    g.hbar(635.0, 638.7, 530.5, weight=48.0)
    g.hbar(638.7, 807.1, 495.3, weight=48.0)
    g.vbar(829.7, 248.8, 460.6, weight=48.0)
    g.diag(852.3, 248.8, 815.7, 212.0, weight=48.0)
    g.hbar(643.0, 818.0, 417.3, weight=76.0)
    g.diag(640.0, 308.6, 654.0, 320.0, weight=76.0)
    g.hbar(654.0, 820.2, 323.3, weight=76.0)
    g.hbar(635.0, 819.2, 214.1, weight=76.0)
    g.diag(639.9, 152.5, 647.5, 100.9, weight=96.0)
    g.diag(647.5, 100.9, 512.4, -9.4, weight=96.0)
    g.hbar(407.6, 512.4, 9.9, weight=96.0)
    g.diag(814.5, 158.2, 893.2, -22.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_985e() -> Glyph:
    """類 U+985E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni985E", advance=1000, unicode=0x985E, note="類：自动生成")
    g.diag(206.0, 626.2, 266.5, 584.5, weight=96.0)
    g.diag(266.5, 584.5, 286.9, 523.8, weight=96.0)
    g.diag(498.5, 703.5, 519.8, 670.4, weight=48.0)
    g.diag(519.8, 670.4, 400.1, 600.8, weight=48.0)
    g.hbar(151.4, 509.4, 500.2, weight=48.0)
    g.diag(344.8, 767.0, 372.1, 611.3, weight=48.0)
    g.vbar(373.3, 330.7, 611.3, weight=48.0)
    g.diag(347.3, 477.0, 115.7, 266.2, weight=48.0)
    g.hbar(392.1, 492.0, 430.5, weight=48.0)
    g.vbar(493.3, 392.1, 409.1, weight=48.0)
    g.diag(105.2, 234.3, 144.5, 178.0, weight=84.0)
    g.hbar(144.5, 485.9, 222.1, weight=84.0)
    g.diag(307.3, 255.1, 288.5, 184.0, weight=84.0)
    g.diag(288.5, 184.0, 111.8, -20.4, weight=84.0)
    g.diag(355.1, 152.9, 500.6, 6.6, weight=96.0)
    g.dot(480.3, 314.9, w=96.0, h=94.4, slant=-14.0)
    g.hbar(531.8, 917.0, 609.6, weight=96.0)
    g.diag(672.7, 596.7, 692.7, 576.8, weight=56.0)
    g.diag(692.7, 576.8, 634.4, 484.4, weight=56.0)
    g.vbar(575.2, 253.9, 470.0, weight=48.0)
    g.vbar(583.7, 146.1, 253.9, weight=48.0)
    g.hbar(582.6, 616.8, 462.8, weight=48.0)
    g.hbar(616.8, 812.3, 484.0, weight=48.0)
    g.diag(812.3, 506.8, 873.5, 245.5, weight=48.0)
    g.diag(873.5, 245.5, 815.6, 168.3, weight=48.0)
    g.diag(609.6, 359.4, 620.4, 375.7, weight=76.0)
    g.hbar(620.4, 811.2, 381.7, weight=76.0)
    g.hbar(609.6, 814.4, 279.2, weight=76.0)
    g.hbar(599.7, 813.2, 171.0, weight=84.0)
    g.diag(661.9, 144.8, 440.0, -67.0, weight=84.0)
    g.diag(809.5, 122.7, 879.3, -67.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_9867() -> Glyph:
    """顧 U+9867 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9867", advance=1000, unicode=0x9867, note="顧：自动生成")
    g.diag(322.8, 757.0, 392.9, 717.6, weight=64.0)
    g.diag(392.9, 717.6, 417.7, 652.5, weight=64.0)
    g.hbar(245.9, 485.4, 604.8, weight=48.0)
    g.diag(485.4, 621.5, 425.6, 520.7, weight=48.0)
    g.hbar(247.4, 455.3, 493.3, weight=48.0)
    g.vbar(223.4, 462.8, 599.0, weight=48.0)
    g.diag(205.4, 462.8, 75.0, 82.8, weight=48.0)
    g.diag(327.5, 458.3, 251.9, 273.3, weight=48.0)
    g.vbar(272.9, -35.3, 291.7, weight=48.0)
    g.dot(426.3, 429.8, w=96.0, h=75.0, slant=-14.0)
    g.hbar(313.4, 568.7, 360.7, weight=48.0)
    g.hbar(303.3, 472.6, 265.6, weight=56.0)
    g.hbar(449.5, 472.6, 283.4, weight=56.0)
    g.hbar(304.7, 467.8, 194.0, weight=56.0)
    g.diag(467.8, 207.7, 503.3, 258.3, weight=56.0)
    g.diag(403.5, 328.7, 429.1, 310.2, weight=96.0)
    g.vbar(425.9, 139.3, 310.2, weight=96.0)
    g.diag(422.6, 139.3, 411.2, 128.9, weight=96.0)
    g.hbar(301.2, 569.2, 112.3, weight=64.0)
    g.hbar(507.6, 925.0, 625.8, weight=96.0)
    g.diag(653.2, 596.6, 672.8, 571.8, weight=96.0)
    g.diag(672.8, 571.8, 621.5, 491.0, weight=96.0)
    g.vbar(586.1, 157.5, 483.2, weight=48.0)
    g.hbar(594.6, 863.1, 491.1, weight=48.0)
    g.diag(863.1, 504.6, 783.2, 422.1, weight=48.0)
    g.vbar(804.6, 215.3, 422.1, weight=48.0)
    g.diag(826.0, 215.3, 787.5, 192.1, weight=48.0)
    g.hbar(610.0, 703.0, 379.3, weight=64.0)
    g.hbar(703.0, 802.4, 391.5, weight=64.0)
    g.hbar(611.9, 801.4, 290.9, weight=64.0)
    g.hbar(608.0, 795.4, 191.8, weight=76.0)
    g.hbar(651.2, 723.9, 98.5, weight=76.0)
    g.diag(651.2, 93.3, 484.2, -47.8, weight=76.0)
    g.diag(787.7, 131.1, 880.8, -67.0, weight=96.0)
    return g
def g_cjk_unified_ideograph_98e2() -> Glyph:
    """飢 U+98E2 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni98E2", advance=1000, unicode=0x98E2, note="飢：自动生成")
    g.diag(347.4, 691.1, 346.1, 698.7, weight=96.0)
    g.diag(346.1, 698.7, 53.0, 285.5, weight=96.0)
    g.diag(364.2, 656.5, 505.0, 553.6, weight=96.0)
    g.diag(312.1, 560.7, 370.3, 526.8, weight=84.0)
    g.diag(370.3, 526.8, 394.5, 462.0, weight=84.0)
    g.hbar(236.7, 449.2, 400.3, weight=48.0)
    g.vbar(427.2, 211.7, 417.3, weight=48.0)
    g.diag(405.1, 211.7, 391.9, 219.8, weight=48.0)
    g.diag(255.5, 284.5, 269.5, 300.9, weight=64.0)
    g.hbar(269.5, 401.9, 303.4, weight=64.0)
    g.diag(257.3, 190.3, 265.2, 203.3, weight=64.0)
    g.hbar(265.2, 383.5, 219.3, weight=64.0)
    g.diag(184.1, 397.9, 208.4, 301.3, weight=48.0)
    g.diag(208.4, 301.3, 246.3, 19.8, weight=48.0)
    g.diag(246.3, 19.8, 358.7, 87.0, weight=48.0)
    g.diag(358.7, 87.0, 364.3, 102.4, weight=48.0)
    g.diag(357.4, 117.9, 450.3, 29.2, weight=48.0)
    g.diag(555.1, 523.0, 441.6, -45.4, weight=96.0)
    g.diag(441.6, -45.4, 413.5, 17.5, weight=96.0)
    g.diag(593.3, 518.7, 602.6, 512.1, weight=96.0)
    g.diag(602.6, 512.1, 742.1, 332.2, weight=96.0)
    g.diag(742.1, 332.2, 942.9, 12.3, weight=96.0)
    g.vbar(945.0, 12.3, 183.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_98fc() -> Glyph:
    """飼 U+98FC —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni98FC", advance=1000, unicode=0x98FC, note="飼：自动生成")
    g.diag(411.6, 722.8, 419.8, 708.8, weight=96.0)
    g.diag(419.8, 708.8, 82.6, 280.9, weight=96.0)
    g.dot(497.1, 665.8, w=96.0, h=124.8, slant=-14.0)
    g.hbar(373.9, 431.7, 570.1, weight=84.0)
    g.diag(431.7, 563.0, 460.9, 472.0, weight=84.0)
    g.diag(309.9, 415.8, 317.1, 410.8, weight=92.0)
    g.hbar(317.1, 495.9, 419.1, weight=92.0)
    g.vbar(476.5, 238.3, 427.4, weight=92.0)
    g.hbar(440.8, 457.1, 238.3, weight=92.0)
    g.hbar(317.6, 452.5, 308.7, weight=56.0)
    g.dot(371.6, 233.7, w=64.0, h=83.2, slant=-14.0)
    g.hbar(246.1, 285.1, 400.2, weight=48.0)
    g.vbar(294.5, 27.8, 393.6, weight=48.0)
    g.diag(303.8, 27.8, 444.1, 134.7, weight=48.0)
    g.hbar(430.8, 483.4, 134.4, weight=48.0)
    g.diag(483.4, 124.6, 502.7, 81.0, weight=48.0)
    g.diag(580.0, 632.7, 817.5, 469.3, weight=96.0)
    g.vbar(839.5, -58.3, 469.3, weight=96.0)
    g.hbar(757.4, 861.4, -36.3, weight=96.0)
    g.hbar(514.8, 840.1, 468.4, weight=96.0)
    g.vbar(587.8, 173.0, 343.8, weight=48.0)
    g.hbar(580.8, 760.0, 342.2, weight=48.0)
    g.diag(760.0, 349.0, 707.8, 234.5, weight=48.0)
    g.diag(617.4, 187.5, 632.9, 202.0, weight=96.0)
    g.hbar(632.9, 747.5, 213.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_98fd() -> Glyph:
    """飽 U+98FD —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni98FD", advance=1000, unicode=0x98FD, note="飽：自动生成")
    g.vbar(351.0, 675.8, 681.1, weight=96.0)
    g.diag(351.5, 675.8, 53.0, 264.2, weight=96.0)
    g.hbar(370.2, 389.8, 651.0, weight=96.0)
    g.diag(389.8, 654.0, 527.9, 556.2, weight=96.0)
    g.hbar(313.7, 326.0, 535.7, weight=84.0)
    g.diag(326.0, 537.2, 393.6, 450.7, weight=84.0)
    g.hbar(237.4, 253.5, 381.6, weight=76.0)
    g.hbar(237.4, 443.1, 394.9, weight=76.0)
    g.vbar(421.8, 205.7, 406.4, weight=76.0)
    g.hbar(384.5, 400.5, 205.7, weight=76.0)
    g.diag(258.4, 263.3, 285.6, 287.1, weight=56.0)
    g.diag(285.6, 287.1, 354.3, 239.8, weight=56.0)
    g.diag(260.0, 178.1, 270.6, 191.3, weight=64.0)
    g.hbar(270.6, 373.2, 206.7, weight=64.0)
    g.hbar(194.9, 208.2, 372.8, weight=48.0)
    g.diag(208.2, 370.9, 264.3, 39.5, weight=48.0)
    g.diag(264.3, 39.5, 366.7, 93.8, weight=48.0)
    g.diag(366.7, 93.8, 374.4, 111.2, weight=48.0)
    g.diag(364.9, 123.8, 416.6, 100.4, weight=48.0)
    g.diag(416.6, 100.4, 434.8, 56.9, weight=48.0)
    g.diag(638.1, 788.7, 682.6, 735.9, weight=96.0)
    g.diag(682.6, 735.9, 457.8, 425.9, weight=96.0)
    g.hbar(564.2, 888.8, 531.6, weight=96.0)
    g.diag(888.8, 559.8, 781.3, 207.0, weight=96.0)
    g.diag(781.3, 207.0, 692.5, 254.0, weight=96.0)
    g.hbar(531.3, 676.3, 366.4, weight=48.0)
    g.diag(676.3, 381.8, 627.6, 258.4, weight=48.0)
    g.hbar(534.4, 676.4, 227.8, weight=48.0)
    g.diag(524.6, 363.1, 796.7, 85.9, weight=48.0)
    g.diag(796.7, 85.9, 947.0, 167.7, weight=48.0)
    return g
def g_cjk_unified_ideograph_98fe() -> Glyph:
    """飾 U+98FE —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni98FE", advance=1000, unicode=0x98FE, note="飾：自动生成")
    g.vbar(379.9, 717.3, 740.2, weight=96.0)
    g.diag(382.6, 717.3, 123.6, 360.8, weight=96.0)
    g.hbar(402.1, 464.5, 704.7, weight=96.0)
    g.diag(464.5, 698.5, 450.3, 604.5, weight=96.0)
    g.hbar(345.0, 400.2, 602.1, weight=48.0)
    g.diag(400.2, 592.7, 419.8, 527.5, weight=48.0)
    g.hbar(294.0, 296.7, 477.2, weight=48.0)
    g.hbar(294.0, 459.8, 492.2, weight=48.0)
    g.vbar(440.0, 315.2, 506.9, weight=48.0)
    g.hbar(405.6, 420.3, 315.5, weight=48.0)
    g.hbar(304.2, 415.1, 384.1, weight=56.0)
    g.diag(302.9, 289.3, 320.1, 307.7, weight=56.0)
    g.hbar(320.1, 400.2, 316.9, weight=56.0)
    g.vbar(279.4, 120.2, 479.9, weight=48.0)
    g.diag(274.5, 120.2, 413.7, 217.7, weight=48.0)
    g.diag(415.2, 282.7, 454.2, 203.4, weight=48.0)
    g.hbar(422.7, 454.2, 198.9, weight=48.0)
    g.diag(638.6, 792.0, 682.1, 743.6, weight=96.0)
    g.diag(682.1, 743.6, 493.9, 479.1, weight=96.0)
    g.hbar(611.6, 850.0, 589.0, weight=96.0)
    g.vbar(552.7, 392.5, 407.2, weight=48.0)
    g.vbar(552.9, 205.3, 392.5, weight=48.0)
    g.hbar(567.3, 798.0, 380.9, weight=48.0)
    g.vbar(818.3, 214.8, 360.7, weight=48.0)
    g.hbar(707.4, 838.5, 229.0, weight=48.0)
    g.diag(645.6, 551.7, 676.4, 356.9, weight=48.0)
    g.vbar(679.8, -62.0, 356.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_9905() -> Glyph:
    """餅 U+9905 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9905", advance=1000, unicode=0x9905, note="餅：自动生成")
    g.diag(325.4, 797.0, 370.6, 748.6, weight=96.0)
    g.diag(370.6, 748.6, 43.5, 304.6, weight=96.0)
    g.diag(43.5, 304.6, 62.1, 354.2, weight=96.0)
    g.dot(420.8, 683.5, w=92.0, h=104.5, slant=-14.0)
    g.dot(356.6, 598.8, w=64.0, h=69.1, slant=-14.0)
    g.diag(286.3, 476.1, 284.5, 477.2, weight=48.0)
    g.hbar(284.5, 447.3, 486.5, weight=48.0)
    g.diag(447.3, 495.8, 401.7, 299.3, weight=48.0)
    g.diag(291.0, 373.7, 304.4, 393.3, weight=56.0)
    g.hbar(304.4, 360.7, 395.6, weight=56.0)
    g.diag(285.4, 287.2, 299.9, 304.4, weight=64.0)
    g.hbar(299.9, 363.5, 315.3, weight=64.0)
    g.diag(221.2, 473.3, 247.6, 376.8, weight=48.0)
    g.vbar(260.0, 132.6, 376.8, weight=48.0)
    g.diag(272.5, 132.6, 361.7, 186.7, weight=48.0)
    g.diag(361.7, 186.7, 365.4, 201.6, weight=48.0)
    g.diag(361.7, 248.1, 418.4, 170.9, weight=48.0)
    g.dot(576.1, 684.0, w=92.0, h=104.8, slant=-14.0)
    g.diag(757.0, 777.5, 791.4, 747.2, weight=96.0)
    g.diag(791.4, 747.2, 699.4, 601.6, weight=96.0)
    g.hbar(519.8, 808.2, 540.7, weight=96.0)
    g.hbar(451.0, 932.9, 356.0, weight=96.0)
    g.diag(549.6, 495.6, 634.9, 432.1, weight=96.0)
    g.diag(634.9, 432.1, 423.1, 36.0, weight=96.0)
    g.diag(690.1, 515.1, 732.9, 481.1, weight=96.0)
    g.vbar(731.0, -57.0, 481.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_990a() -> Glyph:
    """養 U+990A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni990A", advance=1000, unicode=0x990A, note="養：自动生成")
    g.diag(343.9, 734.4, 407.1, 700.4, weight=56.0)
    g.diag(407.1, 700.4, 437.3, 627.0, weight=56.0)
    g.diag(578.8, 778.7, 596.7, 750.4, weight=96.0)
    g.diag(596.7, 750.4, 532.5, 661.3, weight=96.0)
    g.diag(321.4, 537.1, 420.3, 592.4, weight=64.0)
    g.hbar(420.3, 678.8, 618.1, weight=64.0)
    g.diag(328.5, 566.6, 398.9, 508.8, weight=64.0)
    g.hbar(398.9, 594.9, 527.5, weight=64.0)
    g.diag(594.9, 546.2, 639.7, 490.5, weight=64.0)
    g.diag(451.4, 586.2, 482.3, 556.5, weight=96.0)
    g.diag(482.3, 556.5, 458.0, 460.8, weight=96.0)
    g.hbar(208.0, 745.8, 433.4, weight=48.0)
    g.diag(339.3, 402.6, 283.5, 308.4, weight=48.0)
    g.diag(283.5, 308.4, 58.0, 109.8, weight=48.0)
    g.diag(526.5, 430.5, 942.0, 227.7, weight=48.0)
    g.diag(436.1, 418.6, 504.9, 334.3, weight=48.0)
    g.hbar(367.8, 578.6, 300.2, weight=48.0)
    g.vbar(557.5, 158.2, 309.2, weight=48.0)
    g.hbar(515.4, 536.3, 161.8, weight=48.0)
    g.hbar(378.1, 536.5, 214.4, weight=48.0)
    g.hbar(381.8, 489.8, 147.7, weight=56.0)
    g.diag(489.8, 161.9, 501.4, 152.3, weight=56.0)
    g.diag(336.9, 305.9, 388.3, -28.1, weight=48.0)
    g.diag(388.3, -28.1, 525.3, 59.6, weight=48.0)
    g.diag(726.6, 229.4, 570.3, 82.4, weight=96.0)
    g.diag(501.4, 129.9, 744.8, -48.7, weight=56.0)
    return g
def g_cjk_unified_ideograph_990c() -> Glyph:
    """餌 U+990C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni990C", advance=1000, unicode=0x990C, note="餌：自动生成")
    g.diag(331.5, 772.0, 372.3, 722.8, weight=96.0)
    g.diag(372.3, 722.8, 77.3, 362.3, weight=96.0)
    g.dot(428.9, 673.2, w=96.0, h=100.7, slant=-14.0)
    g.dot(359.4, 584.1, w=56.0, h=72.8, slant=-14.0)
    g.hbar(267.0, 281.2, 474.6, weight=48.0)
    g.hbar(267.0, 448.7, 481.5, weight=48.0)
    g.diag(448.7, 486.7, 403.8, 290.0, weight=48.0)
    g.diag(293.1, 375.1, 312.0, 394.0, weight=64.0)
    g.hbar(312.0, 366.3, 396.0, weight=64.0)
    g.diag(290.4, 287.3, 297.6, 297.0, weight=64.0)
    g.hbar(297.6, 375.4, 310.9, weight=64.0)
    g.hbar(229.1, 231.4, 465.5, weight=48.0)
    g.diag(231.4, 465.4, 305.7, 160.4, weight=48.0)
    g.diag(305.7, 160.4, 366.8, 195.0, weight=48.0)
    g.diag(366.8, 195.0, 368.1, 205.0, weight=48.0)
    g.diag(356.2, 248.9, 425.7, 166.6, weight=48.0)
    g.hbar(500.7, 839.1, 639.4, weight=96.0)
    g.diag(540.0, 590.9, 561.5, 571.5, weight=96.0)
    g.vbar(571.3, 324.9, 571.5, weight=96.0)
    g.diag(581.2, 324.9, 555.6, 301.0, weight=96.0)
    g.diag(689.1, 610.1, 720.6, 413.9, weight=96.0)
    g.vbar(722.7, -52.0, 413.9, weight=96.0)
    g.diag(597.6, 485.7, 605.3, 499.7, weight=76.0)
    g.hbar(605.3, 673.5, 504.2, weight=76.0)
    g.diag(595.8, 378.7, 608.5, 395.4, weight=76.0)
    g.hbar(608.5, 671.7, 397.6, weight=76.0)
    g.hbar(442.2, 917.7, 289.1, weight=92.0)
    return g
def g_cjk_unified_ideograph_9913() -> Glyph:
    """餓 U+9913 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9913", advance=1000, unicode=0x9913, note="餓：自动生成")
    g.diag(327.5, 660.3, 30.2, 258.3, weight=96.0)
    g.diag(30.2, 258.3, 53.0, 311.6, weight=96.0)
    g.diag(344.1, 628.6, 506.8, 525.8, weight=84.0)
    g.hbar(285.0, 334.1, 528.8, weight=56.0)
    g.diag(334.1, 524.0, 363.0, 448.8, weight=56.0)
    g.hbar(231.2, 410.0, 405.7, weight=48.0)
    g.diag(410.0, 415.9, 370.1, 234.6, weight=48.0)
    g.diag(370.1, 234.6, 352.9, 218.0, weight=48.0)
    g.diag(251.2, 295.8, 261.0, 311.8, weight=64.0)
    g.hbar(261.0, 360.7, 311.3, weight=64.0)
    g.diag(252.5, 204.9, 259.8, 214.3, weight=76.0)
    g.hbar(259.8, 325.6, 223.2, weight=76.0)
    g.diag(325.6, 232.1, 340.7, 224.5, weight=76.0)
    g.vbar(220.0, 38.5, 421.1, weight=48.0)
    g.diag(240.6, 38.5, 347.4, 116.1, weight=48.0)
    g.diag(338.4, 131.9, 377.0, 114.0, weight=48.0)
    g.diag(377.0, 114.0, 357.5, 93.6, weight=48.0)
    g.diag(568.6, 589.2, 584.4, 561.5, weight=48.0)
    g.diag(584.4, 561.5, 505.8, 453.6, weight=48.0)
    g.hbar(437.7, 857.0, 441.6, weight=96.0)
    g.diag(521.5, 463.3, 547.1, 320.8, weight=48.0)
    g.diag(547.1, 320.8, 409.0, 72.1, weight=48.0)
    g.diag(409.0, 72.1, 464.9, 38.0, weight=48.0)
    g.diag(395.0, 143.5, 608.7, 264.2, weight=84.0)
    g.diag(608.7, 264.2, 602.3, 287.4, weight=84.0)
    g.diag(641.7, 753.1, 715.8, 492.3, weight=96.0)
    g.diag(715.8, 492.3, 883.5, -72.0, weight=96.0)
    g.diag(883.5, -72.0, 942.0, 101.2, weight=96.0)
    g.diag(813.6, 353.1, 835.3, 317.3, weight=56.0)
    g.diag(835.3, 317.3, 671.8, 127.9, weight=56.0)
    g.hbar(594.9, 671.8, 124.5, weight=56.0)
    g.hbar(704.1, 847.2, 606.9, weight=64.0)
    g.diag(847.2, 584.2, 865.0, 557.6, weight=64.0)
    return g
def g_cjk_unified_ideograph_9928() -> Glyph:
    """館 U+9928 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9928", advance=1000, unicode=0x9928, note="館：自动生成")
    g.diag(348.1, 732.6, 341.4, 744.0, weight=96.0)
    g.diag(341.4, 744.0, 83.5, 286.8, weight=96.0)
    g.dot(438.3, 673.5, w=96.0, h=124.8, slant=-14.0)
    g.hbar(309.0, 402.1, 570.9, weight=64.0)
    g.diag(402.1, 552.0, 420.7, 486.2, weight=64.0)
    g.hbar(289.4, 301.3, 428.3, weight=96.0)
    g.hbar(301.3, 464.5, 449.7, weight=96.0)
    g.vbar(437.0, 266.6, 473.4, weight=96.0)
    g.hbar(407.9, 409.5, 266.5, weight=96.0)
    g.diag(293.1, 329.5, 305.1, 345.2, weight=64.0)
    g.hbar(305.1, 417.5, 345.7, weight=64.0)
    g.hbar(289.4, 379.3, 260.3, weight=64.0)
    g.diag(379.3, 276.6, 388.5, 267.4, weight=64.0)
    g.diag(219.2, 437.2, 250.8, 329.1, weight=48.0)
    g.diag(250.8, 329.1, 292.5, 159.8, weight=48.0)
    g.hbar(292.5, 394.7, 146.6, weight=48.0)
    g.vbar(398.1, 133.4, 150.1, weight=48.0)
    g.diag(391.1, 164.2, 443.9, 134.3, weight=48.0)
    g.hbar(412.5, 443.9, 130.7, weight=48.0)
    g.diag(648.8, 774.4, 711.9, 736.5, weight=48.0)
    g.diag(711.9, 736.5, 752.2, 659.6, weight=48.0)
    g.diag(537.3, 618.8, 517.9, 524.2, weight=96.0)
    g.diag(517.9, 524.2, 532.7, 471.2, weight=96.0)
    g.diag(571.1, 600.5, 576.3, 597.1, weight=96.0)
    g.hbar(576.3, 921.8, 627.1, weight=96.0)
    g.diag(921.8, 657.1, 782.1, 484.0, weight=96.0)
    g.diag(546.4, 460.8, 712.0, 312.3, weight=96.0)
    g.diag(712.0, 312.3, 597.5, 123.1, weight=96.0)
    g.diag(597.5, 123.1, 614.2, 7.3, weight=96.0)
    g.hbar(609.2, 807.7, 429.7, weight=48.0)
    g.diag(807.7, 449.4, 726.8, 349.2, weight=48.0)
    g.hbar(618.6, 771.4, 329.1, weight=48.0)
    g.hbar(620.4, 839.7, 204.3, weight=48.0)
    g.diag(839.7, 225.8, 770.7, 103.8, weight=48.0)
    g.hbar(611.0, 817.7, 68.1, weight=48.0)
    g.vbar(813.4, 91.1, 118.4, weight=48.0)
    return g
def g_cjk_unified_ideograph_99d0() -> Glyph:
    """駐 U+99D0 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni99D0", advance=1000, unicode=0x99D0, note="駐：自动生成")
    g.hbar(208.2, 438.2, 682.5, weight=96.0)
    g.diag(151.9, 680.6, 171.5, 552.4, weight=48.0)
    g.vbar(170.9, 307.2, 552.4, weight=48.0)
    g.diag(170.2, 307.2, 181.5, 292.5, weight=48.0)
    g.hbar(234.8, 410.6, 554.7, weight=76.0)
    g.hbar(231.9, 414.6, 457.9, weight=76.0)
    g.diag(293.1, 644.0, 322.7, 619.3, weight=48.0)
    g.vbar(322.2, 386.3, 619.3, weight=48.0)
    g.diag(321.7, 386.3, 304.9, 361.6, weight=48.0)
    g.diag(194.3, 291.5, 214.1, 318.2, weight=48.0)
    g.hbar(214.1, 411.3, 338.7, weight=48.0)
    g.vbar(414.0, 232.6, 359.2, weight=48.0)
    g.diag(416.6, 232.6, 370.6, 5.9, weight=48.0)
    g.diag(370.6, 5.9, 274.3, 62.4, weight=48.0)
    g.diag(81.8, 237.2, 63.0, 98.9, weight=64.0)
    g.dot(160.3, 186.8, w=56.0, h=72.8, slant=0.0)
    g.dot(240.8, 203.6, w=56.0, h=62.5, slant=-14.0)
    g.diag(297.0, 266.8, 332.6, 192.7, weight=48.0)
    g.dot(653.5, 685.5, w=96.0, h=124.8, slant=-14.0)
    g.hbar(534.0, 830.3, 490.5, weight=96.0)
    g.hbar(541.9, 801.7, 308.8, weight=96.0)
    g.diag(631.8, 448.5, 656.6, 429.5, weight=96.0)
    g.vbar(665.7, 186.8, 429.5, weight=96.0)
    g.diag(674.8, 186.8, 647.6, 153.2, weight=96.0)
    g.hbar(471.8, 932.0, 122.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_99d2() -> Glyph:
    """駒 U+99D2 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni99D2", advance=1000, unicode=0x99D2, note="駒：自动生成")
    g.diag(221.6, 692.9, 240.2, 683.0, weight=96.0)
    g.hbar(240.2, 481.7, 703.0, weight=96.0)
    g.diag(203.4, 699.0, 187.1, 602.1, weight=48.0)
    g.vbar(173.6, 310.1, 602.1, weight=48.0)
    g.diag(160.0, 310.1, 191.9, 269.9, weight=48.0)
    g.hbar(222.6, 434.2, 561.8, weight=84.0)
    g.hbar(381.1, 434.2, 579.9, weight=84.0)
    g.hbar(221.4, 417.1, 450.6, weight=84.0)
    g.hbar(417.1, 497.5, 451.4, weight=84.0)
    g.diag(311.3, 673.7, 335.1, 572.1, weight=48.0)
    g.vbar(331.7, 333.5, 572.1, weight=48.0)
    g.hbar(210.4, 309.1, 285.9, weight=48.0)
    g.diag(309.1, 298.8, 419.8, 199.7, weight=48.0)
    g.vbar(414.6, -31.4, 199.7, weight=48.0)
    g.diag(409.4, -31.4, 303.6, 33.5, weight=48.0)
    g.diag(128.7, 202.5, 77.0, 143.6, weight=76.0)
    g.diag(77.0, 143.6, 63.0, 59.4, weight=76.0)
    g.vbar(178.8, 158.7, 246.9, weight=64.0)
    g.hbar(177.4, 238.3, 148.3, weight=64.0)
    g.vbar(214.2, 137.9, 250.2, weight=64.0)
    g.diag(314.8, 288.8, 361.9, 173.8, weight=56.0)
    g.vbar(665.7, 669.9, 785.7, weight=48.0)
    g.diag(663.1, 669.9, 527.0, 376.0, weight=48.0)
    g.diag(607.4, 490.8, 820.6, 311.9, weight=48.0)
    g.vbar(817.7, -61.2, 311.9, weight=48.0)
    g.diag(814.9, -61.2, 701.9, 1.1, weight=48.0)
    g.diag(524.2, 382.3, 600.8, 170.3, weight=64.0)
    g.hbar(593.9, 753.6, 342.9, weight=96.0)
    g.diag(753.6, 353.4, 695.4, 243.9, weight=96.0)
    g.dot(675.5, 209.8, w=96.0, h=124.8, slant=-14.0)
    return g
def g_cjk_unified_ideograph_9a0e() -> Glyph:
    """騎 U+9A0E —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9A0E", advance=1000, unicode=0x9A0E, note="騎：自动生成")
    g.hbar(196.8, 223.7, 660.3, weight=96.0)
    g.hbar(223.7, 382.9, 675.2, weight=96.0)
    g.diag(382.9, 695.9, 488.3, 646.9, weight=96.0)
    g.vbar(174.8, 574.6, 669.2, weight=48.0)
    g.vbar(164.7, 314.0, 574.6, weight=48.0)
    g.hbar(157.7, 189.4, 309.4, weight=48.0)
    g.hbar(210.9, 377.3, 550.1, weight=84.0)
    g.hbar(352.7, 377.3, 564.6, weight=84.0)
    g.hbar(207.3, 369.7, 445.3, weight=84.0)
    g.hbar(369.7, 431.1, 442.8, weight=84.0)
    g.diag(284.3, 648.9, 304.9, 633.2, weight=48.0)
    g.vbar(317.3, 401.7, 633.2, weight=48.0)
    g.diag(329.6, 401.7, 300.7, 357.3, weight=48.0)
    g.hbar(188.8, 273.1, 338.6, weight=48.0)
    g.diag(273.1, 331.3, 367.0, 222.7, weight=48.0)
    g.vbar(364.0, 7.9, 222.7, weight=48.0)
    g.diag(361.0, 7.9, 255.1, 66.8, weight=48.0)
    g.diag(120.2, 223.0, 66.1, 170.4, weight=76.0)
    g.diag(66.1, 170.4, 53.0, 71.8, weight=76.0)
    g.vbar(164.0, 148.3, 269.6, weight=56.0)
    g.diag(187.5, 276.3, 241.1, 204.6, weight=56.0)
    g.diag(241.1, 204.6, 186.0, 174.4, weight=56.0)
    g.diag(290.9, 315.8, 329.6, 209.6, weight=48.0)
    g.hbar(516.6, 809.3, 641.0, weight=64.0)
    g.vbar(649.4, 670.8, 672.2, weight=96.0)
    g.diag(649.4, 672.2, 509.4, 445.4, weight=96.0)
    g.diag(650.9, 580.8, 736.9, 535.4, weight=48.0)
    g.diag(736.9, 535.4, 766.5, 474.4, weight=48.0)
    g.diag(482.4, 431.8, 494.6, 409.2, weight=84.0)
    g.hbar(494.6, 937.0, 434.1, weight=84.0)
    g.vbar(536.6, 172.4, 315.1, weight=84.0)
    g.hbar(544.7, 679.0, 312.9, weight=48.0)
    g.diag(679.0, 324.9, 631.9, 239.9, weight=48.0)
    g.hbar(567.0, 660.7, 213.0, weight=48.0)
    g.vbar(662.1, 224.7, 245.3, weight=48.0)
    g.diag(741.9, 421.8, 788.9, 388.4, weight=96.0)
    g.vbar(771.9, -38.3, 388.4, weight=96.0)
    g.hbar(649.4, 754.9, -18.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_9a30() -> Glyph:
    """騰 U+9A30 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9A30", advance=1000, unicode=0x9A30, note="騰：自动生成")
    g.diag(168.4, 684.1, 58.0, 83.2, weight=84.0)
    g.diag(194.8, 673.1, 284.0, 451.7, weight=48.0)
    g.vbar(290.7, 56.8, 451.7, weight=48.0)
    g.hbar(206.0, 297.4, 76.6, weight=48.0)
    g.diag(212.6, 507.3, 222.1, 522.0, weight=96.0)
    g.hbar(222.1, 279.7, 520.2, weight=96.0)
    g.dot(235.9, 372.9, w=96.0, h=83.1, slant=-14.0)
    g.hbar(358.3, 479.3, 664.6, weight=96.0)
    g.diag(479.3, 654.3, 512.3, 626.7, weight=96.0)
    g.hbar(723.1, 748.7, 729.3, weight=48.0)
    g.diag(723.1, 731.2, 660.5, 619.4, weight=48.0)
    g.vbar(478.3, 557.6, 612.9, weight=64.0)
    g.hbar(484.0, 670.9, 579.9, weight=64.0)
    g.vbar(670.5, 602.2, 637.2, weight=64.0)
    g.hbar(336.1, 814.2, 484.8, weight=48.0)
    g.diag(537.1, 766.3, 515.5, 611.8, weight=48.0)
    g.diag(515.5, 611.8, 332.6, 261.9, weight=48.0)
    g.diag(637.6, 485.4, 947.0, 307.1, weight=48.0)
    g.hbar(480.6, 681.4, 401.2, weight=48.0)
    g.vbar(446.5, 150.0, 344.5, weight=48.0)
    g.diag(439.0, 150.0, 442.9, 135.4, weight=48.0)
    g.hbar(481.3, 635.8, 311.9, weight=48.0)
    g.diag(635.8, 316.9, 672.1, 275.1, weight=48.0)
    g.hbar(476.7, 638.7, 246.7, weight=48.0)
    g.diag(638.7, 251.0, 669.6, 303.8, weight=48.0)
    g.diag(573.2, 356.4, 597.5, 339.9, weight=96.0)
    g.vbar(594.3, 201.5, 339.9, weight=96.0)
    g.diag(591.1, 201.5, 579.8, 192.3, weight=96.0)
    g.diag(461.2, 129.7, 494.3, 161.4, weight=84.0)
    g.hbar(494.3, 702.0, 128.0, weight=84.0)
    g.diag(702.0, 94.7, 605.6, -78.0, weight=84.0)
    g.diag(605.6, -78.0, 655.1, 14.8, weight=84.0)
    g.diag(410.5, 118.8, 373.9, -26.9, weight=64.0)
    g.dot(480.7, 63.3, w=56.0, h=72.8, slant=-14.0)
    g.diag(536.9, 142.9, 578.9, 41.4, weight=48.0)
    g.diag(615.5, 158.0, 669.0, 67.0, weight=48.0)
    g.diag(669.0, 67.0, 656.6, -3.5, weight=48.0)
    return g
def g_cjk_unified_ideograph_9a5a() -> Glyph:
    """驚 U+9A5A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9A5A", advance=1000, unicode=0x9A5A, note="驚：自动生成")
    g.diag(241.2, 755.0, 272.5, 732.2, weight=48.0)
    g.diag(272.5, 732.2, 289.6, 633.5, weight=48.0)
    g.hbar(114.0, 322.9, 684.7, weight=48.0)
    g.diag(384.5, 792.0, 404.5, 763.5, weight=48.0)
    g.diag(404.5, 763.5, 364.6, 645.8, weight=48.0)
    g.dot(430.6, 693.3, w=96.0, h=124.8, slant=-14.0)
    g.hbar(254.1, 272.5, 615.6, weight=48.0)
    g.diag(254.1, 611.9, 173.8, 528.1, weight=48.0)
    g.hbar(252.6, 298.3, 576.3, weight=56.0)
    g.hbar(298.3, 432.6, 591.4, weight=56.0)
    g.vbar(400.4, 390.5, 600.2, weight=56.0)
    g.diag(368.2, 390.5, 316.2, 417.1, weight=56.0)
    g.diag(131.1, 492.1, 153.0, 478.8, weight=96.0)
    g.vbar(170.0, 382.9, 478.8, weight=96.0)
    g.hbar(175.7, 300.0, 494.1, weight=48.0)
    g.diag(300.0, 507.6, 255.5, 443.7, weight=48.0)
    g.diag(201.4, 403.8, 206.2, 413.4, weight=48.0)
    g.hbar(206.2, 285.8, 418.1, weight=48.0)
    g.diag(550.7, 787.3, 582.5, 753.2, weight=48.0)
    g.diag(582.5, 753.2, 480.4, 583.2, weight=48.0)
    g.hbar(565.8, 783.2, 679.5, weight=48.0)
    g.diag(648.4, 659.1, 681.5, 603.8, weight=48.0)
    g.diag(681.5, 603.8, 480.4, 455.0, weight=48.0)
    g.hbar(509.8, 881.0, 521.5, weight=96.0)
    g.hbar(410.2, 613.3, 411.4, weight=48.0)
    g.diag(314.3, 344.0, 346.6, 308.5, weight=48.0)
    g.diag(346.6, 308.5, 318.9, 144.2, weight=48.0)
    g.diag(318.9, 144.2, 328.5, 125.7, weight=48.0)
    g.hbar(414.0, 593.4, 331.2, weight=48.0)
    g.hbar(407.3, 593.4, 260.9, weight=48.0)
    g.diag(475.7, 375.3, 501.3, 357.3, weight=96.0)
    g.vbar(500.3, 223.4, 357.3, weight=96.0)
    g.diag(499.4, 223.4, 486.1, 202.6, weight=96.0)
    g.hbar(343.7, 480.1, 141.9, weight=56.0)
    g.hbar(480.1, 657.4, 131.6, weight=56.0)
    g.diag(657.4, 103.3, 686.1, -45.8, weight=56.0)
    g.diag(686.1, -45.8, 595.3, 2.3, weight=56.0)
    g.dot(193.3, 10.4, w=96.0, h=124.8, slant=0.0)
    g.dot(328.1, 40.3, w=84.0, h=78.5, slant=-14.0)
    g.dot(436.3, 64.0, w=48.0, h=62.4, slant=-14.0)
    g.diag(520.3, 122.8, 592.4, 46.9, weight=48.0)
    return g
def g_cjk_unified_ideograph_9ab8() -> Glyph:
    """骸 U+9AB8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9AB8", advance=1000, unicode=0x9AB8, note="骸：自动生成")
    g.diag(194.7, 740.5, 184.1, 723.4, weight=48.0)
    g.vbar(197.1, 499.3, 723.4, weight=48.0)
    g.diag(210.1, 499.3, 197.5, 482.4, weight=48.0)
    g.hbar(198.5, 433.5, 747.1, weight=48.0)
    g.diag(433.5, 765.8, 405.5, 544.0, weight=48.0)
    g.diag(405.5, 544.0, 381.2, 520.8, weight=48.0)
    g.hbar(217.7, 317.1, 641.0, weight=48.0)
    g.vbar(312.8, 520.8, 654.8, weight=48.0)
    g.diag(308.4, 520.8, 293.2, 505.4, weight=48.0)
    g.vbar(83.7, 344.3, 463.0, weight=96.0)
    g.hbar(68.0, 156.6, 349.7, weight=96.0)
    g.hbar(128.7, 522.3, 475.9, weight=96.0)
    g.diag(522.3, 513.8, 410.1, 402.9, weight=96.0)
    g.vbar(193.2, 6.2, 363.8, weight=84.0)
    g.hbar(174.1, 240.4, -2.7, weight=84.0)
    g.hbar(232.6, 355.1, 370.7, weight=48.0)
    g.vbar(368.2, 250.6, 395.7, weight=48.0)
    g.vbar(374.4, -37.0, 250.6, weight=48.0)
    g.hbar(270.9, 367.7, -17.3, weight=48.0)
    g.diag(238.9, 241.8, 252.5, 258.0, weight=84.0)
    g.hbar(252.5, 356.4, 260.1, weight=84.0)
    g.dot(293.9, 146.9, w=84.0, h=109.2, slant=-14.0)
    g.diag(628.3, 782.2, 724.2, 732.6, weight=92.0)
    g.diag(724.2, 732.6, 777.0, 619.5, weight=92.0)
    g.hbar(493.6, 915.0, 548.0, weight=48.0)
    g.diag(620.5, 520.8, 650.7, 475.5, weight=96.0)
    g.diag(650.7, 475.5, 559.4, 310.4, weight=96.0)
    g.hbar(559.4, 702.2, 317.4, weight=96.0)
    g.diag(832.1, 335.3, 805.2, 394.3, weight=96.0)
    g.diag(805.2, 394.3, 435.4, 43.3, weight=96.0)
    g.diag(778.7, 328.6, 870.2, 247.1, weight=76.0)
    g.diag(870.2, 247.1, 558.8, -47.2, weight=76.0)
    g.diag(799.2, 107.2, 947.0, -47.2, weight=96.0)
    return g
def g_cjk_unified_ideograph_9b3c() -> Glyph:
    """鬼 U+9B3C —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9B3C", advance=1000, unicode=0x9B3C, note="鬼：自动生成")
    g.diag(391.8, 802.0, 426.9, 762.4, weight=96.0)
    g.diag(426.9, 762.4, 328.3, 627.1, weight=96.0)
    g.hbar(304.4, 328.3, 622.4, weight=96.0)
    g.vbar(226.2, 572.2, 589.9, weight=48.0)
    g.vbar(264.7, 305.7, 572.2, weight=48.0)
    g.hbar(236.8, 664.9, 612.9, weight=48.0)
    g.diag(664.9, 645.8, 705.4, 596.7, weight=48.0)
    g.diag(705.4, 596.7, 613.8, 367.0, weight=48.0)
    g.hbar(294.7, 626.0, 462.3, weight=84.0)
    g.hbar(311.4, 612.0, 348.1, weight=48.0)
    g.diag(414.7, 586.5, 378.0, 403.1, weight=76.0)
    g.diag(378.0, 403.1, 84.7, -50.8, weight=76.0)
    g.diag(460.5, 332.3, 615.2, 31.2, weight=48.0)
    g.hbar(615.2, 913.1, -17.4, weight=48.0)
    g.vbar(907.6, -66.0, 153.3, weight=48.0)
    g.diag(638.3, 340.4, 692.2, 279.7, weight=48.0)
    g.diag(692.2, 279.7, 604.4, 101.2, weight=48.0)
    g.hbar(604.4, 789.8, 120.2, weight=48.0)
    g.diag(697.5, 246.3, 806.2, 152.3, weight=48.0)
    g.vbar(800.7, 124.6, 152.3, weight=48.0)
    return g
def g_cjk_unified_ideograph_9b42() -> Glyph:
    """魂 U+9B42 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9B42", advance=1000, unicode=0x9B42, note="魂：自动生成")
    g.hbar(167.3, 374.8, 611.9, weight=96.0)
    g.hbar(68.0, 397.4, 450.1, weight=96.0)
    g.diag(217.4, 416.2, 254.9, 388.1, weight=48.0)
    g.diag(254.9, 388.1, 152.3, 183.2, weight=48.0)
    g.hbar(152.3, 348.2, 215.2, weight=48.0)
    g.diag(327.6, 325.8, 401.3, 190.1, weight=56.0)
    g.diag(576.3, 759.4, 615.6, 725.9, weight=96.0)
    g.diag(615.6, 725.9, 507.5, 579.4, weight=96.0)
    g.diag(411.1, 565.7, 480.0, 309.0, weight=48.0)
    g.hbar(459.3, 551.6, 566.4, weight=48.0)
    g.hbar(551.6, 755.6, 589.2, weight=48.0)
    g.diag(755.6, 607.4, 789.3, 568.2, weight=48.0)
    g.diag(789.3, 568.2, 732.7, 355.3, weight=48.0)
    g.hbar(510.4, 696.3, 456.5, weight=76.0)
    g.hbar(496.7, 710.0, 360.2, weight=76.0)
    g.vbar(544.8, 360.3, 552.9, weight=48.0)
    g.diag(529.0, 360.3, 309.9, -10.5, weight=48.0)
    g.diag(600.9, 314.9, 650.2, 232.1, weight=48.0)
    g.diag(650.2, 232.1, 701.8, 69.7, weight=48.0)
    g.hbar(701.8, 934.2, 39.2, weight=48.0)
    g.vbar(940.6, 8.7, 168.4, weight=48.0)
    g.diag(738.6, 292.3, 761.8, 268.1, weight=48.0)
    g.diag(761.8, 268.1, 697.5, 134.2, weight=48.0)
    g.hbar(697.5, 814.0, 147.6, weight=48.0)
    g.hbar(814.0, 828.0, 158.8, weight=48.0)
    g.diag(814.3, 230.4, 872.3, 128.1, weight=48.0)
    return g
def g_cjk_unified_ideograph_9b45() -> Glyph:
    """魅 U+9B45 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9B45", advance=1000, unicode=0x9B45, note="魅：自动生成")
    g.diag(266.3, 800.4, 302.6, 769.6, weight=96.0)
    g.diag(302.6, 769.6, 202.9, 606.9, weight=96.0)
    g.vbar(135.2, 576.1, 590.4, weight=48.0)
    g.vbar(161.9, 336.0, 576.1, weight=48.0)
    g.hbar(147.5, 477.3, 598.1, weight=48.0)
    g.vbar(438.4, 373.3, 612.8, weight=48.0)
    g.hbar(193.6, 401.8, 473.9, weight=84.0)
    g.diag(203.9, 349.9, 212.7, 360.9, weight=64.0)
    g.hbar(212.7, 366.4, 374.5, weight=64.0)
    g.diag(366.4, 388.1, 381.7, 376.2, weight=64.0)
    g.vbar(259.3, 419.0, 585.7, weight=64.0)
    g.diag(252.3, 419.0, 58.0, -36.0, weight=64.0)
    g.diag(282.4, 334.4, 661.7, -4.5, weight=48.0)
    g.diag(661.7, -4.5, 735.7, 59.0, weight=48.0)
    g.diag(735.7, 59.0, 938.0, 186.0, weight=48.0)
    g.diag(451.4, 291.8, 477.0, 263.9, weight=48.0)
    g.diag(477.0, 263.9, 412.7, 129.1, weight=48.0)
    g.hbar(412.7, 517.3, 138.4, weight=48.0)
    g.dot(523.9, 165.7, w=48.0, h=56.7, slant=0.0)
    g.hbar(652.3, 666.2, 530.2, weight=96.0)
    g.hbar(652.3, 773.9, 545.5, weight=96.0)
    g.hbar(743.9, 773.9, 561.8, weight=96.0)
    g.hbar(456.9, 877.5, 417.0, weight=96.0)
    g.diag(662.8, 772.9, 693.7, 571.1, weight=48.0)
    g.vbar(693.6, 47.5, 571.1, weight=48.0)
    g.diag(684.1, 375.4, 538.3, 190.9, weight=48.0)
    g.diag(727.3, 382.7, 937.3, 191.3, weight=96.0)
    return g
def g_cjk_unified_ideograph_9b54() -> Glyph:
    """魔 U+9B54 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9B54", advance=1000, unicode=0x9B54, note="魔：自动生成")
    g.diag(473.0, 792.0, 582.3, 737.3, weight=48.0)
    g.hbar(323.6, 769.7, 689.0, weight=64.0)
    g.vbar(247.8, 462.7, 683.6, weight=76.0)
    g.diag(240.3, 462.7, 73.7, -29.9, weight=76.0)
    g.hbar(353.9, 527.6, 556.3, weight=48.0)
    g.diag(430.0, 628.0, 452.5, 603.5, weight=48.0)
    g.vbar(449.6, 410.3, 603.5, weight=48.0)
    g.diag(430.0, 527.5, 445.4, 537.7, weight=48.0)
    g.diag(445.4, 537.7, 342.2, 415.2, weight=48.0)
    g.dot(499.8, 490.9, w=96.0, h=52.8, slant=-14.0)
    g.hbar(572.5, 753.1, 587.5, weight=48.0)
    g.diag(631.1, 662.2, 655.6, 634.6, weight=96.0)
    g.vbar(652.6, 421.1, 634.6, weight=96.0)
    g.diag(630.1, 553.8, 543.3, 453.3, weight=48.0)
    g.diag(672.1, 562.6, 780.6, 441.2, weight=96.0)
    g.hbar(780.6, 849.8, 435.5, weight=96.0)
    g.hbar(512.0, 538.4, 411.3, weight=76.0)
    g.diag(512.0, 410.3, 459.3, 345.9, weight=76.0)
    g.diag(340.2, 328.3, 405.6, 152.6, weight=48.0)
    g.hbar(387.1, 503.0, 329.4, weight=48.0)
    g.hbar(503.0, 725.2, 344.6, weight=48.0)
    g.vbar(689.9, 183.9, 355.7, weight=48.0)
    g.hbar(451.5, 613.5, 262.4, weight=56.0)
    g.hbar(422.2, 637.0, 189.2, weight=48.0)
    g.vbar(473.2, 179.0, 320.5, weight=48.0)
    g.diag(456.8, 179.0, 348.3, -3.9, weight=48.0)
    g.diag(348.3, -3.9, 289.5, -64.1, weight=48.0)
    g.diag(546.2, 176.1, 574.6, 98.4, weight=48.0)
    g.diag(574.6, 98.4, 612.5, -55.7, weight=48.0)
    g.hbar(612.5, 902.4, -52.0, weight=48.0)
    g.vbar(905.9, -48.2, 89.2, weight=48.0)
    g.diag(704.3, 173.1, 725.2, 154.8, weight=48.0)
    g.diag(725.2, 154.8, 666.7, 29.0, weight=48.0)
    g.hbar(666.7, 766.2, 41.6, weight=48.0)
    g.hbar(766.2, 779.5, 52.2, weight=48.0)
    g.diag(776.6, 103.8, 820.5, 22.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_9b5a() -> Glyph:
    """魚 U+9B5A —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9B5A", advance=1000, unicode=0x9B5A, note="魚：自动生成")
    g.vbar(462.2, 705.5, 746.2, weight=96.0)
    g.diag(464.1, 746.2, 250.3, 497.6, weight=96.0)
    g.hbar(430.5, 645.0, 673.8, weight=48.0)
    g.diag(645.0, 681.0, 473.1, 499.3, weight=48.0)
    g.vbar(282.3, 443.0, 459.9, weight=48.0)
    g.vbar(315.2, 184.4, 443.0, weight=48.0)
    g.hbar(292.6, 695.0, 481.6, weight=48.0)
    g.vbar(695.4, 384.5, 513.1, weight=48.0)
    g.diag(695.7, 384.5, 650.6, 185.5, weight=48.0)
    g.hbar(349.9, 657.4, 349.1, weight=96.0)
    g.diag(458.9, 459.3, 489.4, 434.9, weight=96.0)
    g.vbar(488.8, 263.6, 434.9, weight=96.0)
    g.diag(488.3, 263.6, 471.1, 242.3, weight=96.0)
    g.hbar(367.7, 617.5, 219.3, weight=96.0)
    g.vbar(121.8, -67.0, 129.7, weight=96.0)
    g.dot(357.3, 83.0, w=96.0, h=124.8, slant=-14.0)
    g.diag(503.9, 183.9, 603.9, 40.5, weight=96.0)
    g.diag(683.6, 165.9, 883.8, -36.6, weight=96.0)
    return g
def g_cjk_unified_ideograph_9bae() -> Glyph:
    """鮮 U+9BAE —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9BAE", advance=1000, unicode=0x9BAE, note="鮮：自动生成")
    g.diag(269.8, 799.0, 246.6, 703.6, weight=48.0)
    g.diag(246.6, 703.6, 112.1, 488.9, weight=48.0)
    g.hbar(257.8, 406.9, 658.7, weight=48.0)
    g.diag(406.9, 657.7, 269.8, 493.5, weight=48.0)
    g.diag(112.1, 508.0, 196.4, 249.1, weight=48.0)
    g.hbar(153.7, 449.8, 473.5, weight=48.0)
    g.vbar(424.2, 282.0, 487.3, weight=48.0)
    g.hbar(375.6, 398.5, 283.0, weight=48.0)
    g.hbar(194.5, 392.4, 368.9, weight=76.0)
    g.diag(264.9, 457.8, 289.0, 436.9, weight=48.0)
    g.vbar(286.4, 308.9, 436.9, weight=48.0)
    g.diag(283.7, 308.9, 274.8, 301.0, weight=48.0)
    g.hbar(210.3, 369.0, 282.2, weight=64.0)
    g.diag(139.8, 203.1, 79.4, 83.8, weight=76.0)
    g.vbar(81.4, 39.1, 83.8, weight=76.0)
    g.diag(183.7, 226.9, 204.4, 102.6, weight=48.0)
    g.diag(259.3, 252.4, 306.5, 157.2, weight=64.0)
    g.diag(306.5, 157.2, 362.6, 184.0, weight=64.0)
    g.diag(368.5, 256.0, 422.6, 140.3, weight=64.0)
    g.dot(572.7, 707.7, w=96.0, h=124.8, slant=-14.0)
    g.diag(748.0, 802.0, 775.8, 768.4, weight=96.0)
    g.diag(775.8, 768.4, 671.4, 607.3, weight=96.0)
    g.diag(569.0, 533.8, 559.5, 543.1, weight=96.0)
    g.hbar(559.5, 756.0, 564.9, weight=96.0)
    g.diag(756.0, 586.7, 735.3, 656.9, weight=96.0)
    g.hbar(475.1, 746.0, 442.9, weight=96.0)
    g.diag(746.0, 455.8, 781.9, 368.7, weight=96.0)
    g.hbar(443.3, 920.6, 307.5, weight=96.0)
    g.diag(606.1, 524.2, 650.8, 500.4, weight=96.0)
    g.vbar(646.8, -72.0, 500.4, weight=96.0)
    return g
def g_cjk_unified_ideograph_9be8() -> Glyph:
    """鯨 U+9BE8 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9BE8", advance=1000, unicode=0x9BE8, note="鯨：自动生成")
    g.diag(228.1, 790.0, 257.6, 744.6, weight=48.0)
    g.diag(257.6, 744.6, 66.2, 533.5, weight=48.0)
    g.hbar(224.9, 347.9, 674.4, weight=48.0)
    g.hbar(347.9, 385.1, 673.9, weight=48.0)
    g.diag(385.1, 667.5, 266.6, 501.4, weight=48.0)
    g.vbar(126.5, 209.3, 455.2, weight=64.0)
    g.hbar(111.2, 421.3, 465.8, weight=48.0)
    g.vbar(386.1, 250.4, 491.9, weight=48.0)
    g.hbar(326.1, 351.0, 251.2, weight=48.0)
    g.hbar(153.9, 349.0, 347.5, weight=84.0)
    g.diag(220.3, 449.8, 270.6, 418.4, weight=48.0)
    g.diag(270.6, 418.4, 234.0, 268.3, weight=48.0)
    g.hbar(171.9, 317.8, 244.9, weight=84.0)
    g.diag(98.9, 127.3, 53.0, 0.6, weight=92.0)
    g.diag(53.0, 0.6, 62.9, -32.5, weight=92.0)
    g.hbar(78.6, 160.9, 106.3, weight=64.0)
    g.vbar(168.1, 51.2, 88.7, weight=64.0)
    g.hbar(181.0, 320.0, 124.7, weight=76.0)
    g.diag(342.5, 199.7, 442.8, 74.4, weight=76.0)
    g.diag(602.4, 795.5, 710.3, 744.8, weight=96.0)
    g.diag(710.3, 744.8, 765.4, 611.1, weight=96.0)
    g.hbar(442.7, 947.0, 533.7, weight=96.0)
    g.diag(543.6, 403.1, 534.3, 384.1, weight=48.0)
    g.vbar(556.2, 219.7, 384.1, weight=48.0)
    g.hbar(549.0, 837.0, 409.8, weight=48.0)
    g.diag(837.0, 427.5, 757.7, 286.4, weight=48.0)
    g.hbar(592.5, 795.2, 262.9, weight=48.0)
    g.diag(646.4, 230.7, 696.9, 188.9, weight=96.0)
    g.diag(696.9, 188.9, 655.4, -64.5, weight=96.0)
    g.diag(655.4, -64.5, 490.2, 18.3, weight=96.0)
    g.diag(419.5, 117.7, 461.9, 29.9, weight=96.0)
    g.diag(461.9, 29.9, 516.7, -19.8, weight=96.0)
    g.hbar(722.2, 888.6, 102.9, weight=96.0)
    g.diag(888.6, 68.8, 919.5, 17.1, weight=96.0)
    return g
def g_cjk_unified_ideograph_9cf4() -> Glyph:
    """鳴 U+9CF4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9CF4", advance=1000, unicode=0x9CF4, note="鳴：自动生成")
    g.diag(143.1, 548.1, 189.0, 328.3, weight=96.0)
    g.hbar(170.0, 326.3, 555.6, weight=48.0)
    g.diag(326.3, 581.5, 362.4, 547.8, weight=48.0)
    g.diag(362.4, 547.8, 298.7, 410.8, weight=48.0)
    g.diag(207.4, 362.0, 219.4, 376.0, weight=96.0)
    g.hbar(219.4, 347.9, 390.6, weight=96.0)
    g.diag(600.6, 802.0, 631.5, 763.2, weight=96.0)
    g.diag(631.5, 763.2, 548.8, 662.6, weight=96.0)
    g.vbar(493.7, 531.6, 639.5, weight=48.0)
    g.diag(493.5, 531.6, 443.0, 283.5, weight=48.0)
    g.diag(443.0, 283.5, 505.0, 194.8, weight=48.0)
    g.hbar(504.9, 728.1, 656.1, weight=48.0)
    g.diag(728.1, 680.1, 771.0, 633.1, weight=48.0)
    g.diag(771.0, 633.1, 680.2, 453.1, weight=48.0)
    g.hbar(523.9, 696.4, 528.1, weight=76.0)
    g.hbar(523.9, 670.7, 446.5, weight=76.0)
    g.diag(528.9, 316.2, 537.9, 325.2, weight=92.0)
    g.hbar(537.9, 691.2, 340.1, weight=92.0)
    g.diag(691.2, 355.1, 750.4, 301.0, weight=92.0)
    g.hbar(518.0, 632.4, 213.6, weight=48.0)
    g.hbar(632.4, 862.0, 255.8, weight=48.0)
    g.vbar(865.9, 164.4, 278.1, weight=48.0)
    g.diag(869.9, 164.4, 806.5, -73.3, weight=48.0)
    g.diag(806.5, -73.3, 713.1, -19.2, weight=48.0)
    g.diag(410.1, 129.3, 339.8, 68.4, weight=96.0)
    g.vbar(336.3, -31.2, 68.4, weight=96.0)
    g.vbar(477.0, 71.4, 165.0, weight=96.0)
    g.hbar(473.2, 568.5, 72.8, weight=96.0)
    g.diag(535.0, 183.7, 604.6, 87.3, weight=48.0)
    g.diag(654.1, 228.4, 727.0, 89.3, weight=48.0)
    return g
def g_cjk_unified_ideograph_9db4() -> Glyph:
    """鶴 U+9DB4 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9DB4", advance=1000, unicode=0x9DB4, note="鶴：自动生成")
    g.dot(144.0, 578.6, w=96.0, h=124.8, slant=14.0)
    g.hbar(185.1, 499.8, 631.8, weight=48.0)
    g.diag(499.8, 660.5, 420.1, 569.8, weight=48.0)
    g.diag(296.4, 789.2, 263.5, 617.3, weight=48.0)
    g.diag(263.5, 617.3, 53.0, 197.5, weight=48.0)
    g.vbar(196.5, -25.1, 421.1, weight=48.0)
    g.dot(382.7, 517.8, w=84.0, h=98.2, slant=-14.0)
    g.hbar(292.2, 484.6, 432.0, weight=84.0)
    g.hbar(305.7, 477.3, 320.2, weight=64.0)
    g.hbar(288.0, 485.6, 232.8, weight=64.0)
    g.diag(356.7, 398.2, 383.1, 378.1, weight=96.0)
    g.vbar(384.9, 188.4, 378.1, weight=96.0)
    g.diag(386.6, 188.4, 370.2, 162.1, weight=96.0)
    g.diag(249.6, 123.6, 257.1, 116.1, weight=76.0)
    g.hbar(257.1, 498.1, 134.4, weight=76.0)
    g.diag(673.9, 798.6, 697.8, 772.6, weight=48.0)
    g.diag(697.8, 772.6, 621.9, 642.6, weight=48.0)
    g.diag(621.9, 642.6, 604.2, 634.3, weight=48.0)
    g.diag(558.4, 631.1, 575.0, 533.2, weight=48.0)
    g.vbar(594.6, 191.8, 533.2, weight=48.0)
    g.diag(614.2, 191.8, 594.8, 222.4, weight=48.0)
    g.hbar(602.1, 610.8, 622.4, weight=48.0)
    g.hbar(610.8, 825.6, 626.3, weight=48.0)
    g.vbar(797.1, 454.3, 631.6, weight=48.0)
    g.diag(611.5, 517.8, 623.5, 531.1, weight=48.0)
    g.hbar(623.5, 718.6, 535.4, weight=48.0)
    g.hbar(611.5, 744.6, 459.5, weight=56.0)
    g.hbar(615.6, 780.0, 363.3, weight=76.0)
    g.diag(612.5, 278.6, 627.1, 249.0, weight=48.0)
    g.hbar(627.1, 891.5, 268.8, weight=48.0)
    g.vbar(897.0, 172.1, 288.6, weight=48.0)
    g.diag(902.6, 172.1, 851.9, -68.3, weight=48.0)
    g.diag(851.9, -68.3, 746.7, -15.7, weight=48.0)
    g.dot(463.3, 33.1, w=84.0, h=109.2, slant=0.0)
    g.dot(578.2, 97.6, w=76.0, h=93.4, slant=-14.0)
    g.dot(673.4, 121.5, w=64.0, h=83.2, slant=-14.0)
    g.dot(778.9, 145.5, w=64.0, h=83.2, slant=-14.0)
    return g
def g_cjk_unified_ideograph_9e93() -> Glyph:
    """麓 U+9E93 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9E93", advance=1000, unicode=0x9E93, note="麓：自动生成")
    g.hbar(211.2, 467.3, 633.8, weight=48.0)
    g.diag(353.3, 757.8, 388.4, 724.8, weight=64.0)
    g.vbar(383.5, 461.3, 724.8, weight=64.0)
    g.diag(355.4, 605.5, 188.0, 427.1, weight=48.0)
    g.dot(441.1, 564.7, w=48.0, h=56.4, slant=-14.0)
    g.hbar(521.7, 770.7, 671.6, weight=48.0)
    g.diag(604.4, 787.0, 643.2, 748.2, weight=96.0)
    g.vbar(639.9, 488.6, 748.2, weight=96.0)
    g.diag(611.4, 634.8, 498.5, 510.7, weight=48.0)
    g.diag(660.9, 639.8, 772.1, 523.3, weight=48.0)
    g.hbar(772.1, 866.5, 516.0, weight=48.0)
    g.diag(458.2, 510.7, 533.8, 451.3, weight=48.0)
    g.hbar(340.2, 443.7, 415.4, weight=48.0)
    g.hbar(443.7, 709.2, 436.6, weight=48.0)
    g.diag(273.7, 437.1, 99.3, -71.0, weight=48.0)
    g.hbar(354.4, 622.4, 314.5, weight=84.0)
    g.hbar(622.4, 712.3, 326.6, weight=84.0)
    g.diag(712.3, 317.3, 674.0, 204.3, weight=84.0)
    g.diag(414.8, 367.6, 442.1, 339.4, weight=96.0)
    g.vbar(445.1, 230.5, 339.4, weight=96.0)
    g.diag(448.1, 230.5, 440.1, 222.4, weight=96.0)
    g.diag(555.0, 407.9, 584.0, 377.8, weight=84.0)
    g.diag(584.0, 377.8, 547.9, 240.5, weight=84.0)
    g.hbar(345.3, 642.7, 214.3, weight=48.0)
    g.diag(391.7, 72.2, 404.7, 85.2, weight=48.0)
    g.hbar(404.7, 513.7, 90.8, weight=48.0)
    g.diag(336.2, 147.8, 366.4, 110.9, weight=48.0)
    g.vbar(358.0, -51.0, 110.9, weight=48.0)
    g.hbar(349.6, 531.8, -13.6, weight=48.0)
    g.diag(805.0, 131.7, 775.6, 145.0, weight=48.0)
    g.diag(775.6, 145.0, 621.3, 61.6, weight=48.0)
    g.diag(621.3, 61.6, 620.5, 56.0, weight=48.0)
    g.diag(574.1, 179.0, 594.3, 100.4, weight=48.0)
    g.diag(594.3, 100.4, 687.7, -7.8, weight=48.0)
    g.hbar(687.7, 892.0, -25.7, weight=48.0)
    g.vbar(888.4, -43.5, 90.3, weight=48.0)
    return g
def g_cjk_unified_ideograph_9e97() -> Glyph:
    """麗 U+9E97 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9E97", advance=1000, unicode=0x9E97, note="麗：自动生成")
    g.diag(292.9, 663.8, 321.3, 721.4, weight=64.0)
    g.hbar(321.3, 452.8, 732.5, weight=64.0)
    g.vbar(465.3, 684.2, 743.6, weight=64.0)
    g.diag(264.3, 643.2, 301.1, 483.9, weight=76.0)
    g.hbar(283.5, 348.9, 639.8, weight=48.0)
    g.hbar(348.9, 471.6, 654.8, weight=48.0)
    g.diag(471.6, 663.0, 489.4, 530.0, weight=48.0)
    g.diag(326.2, 619.0, 431.8, 522.4, weight=48.0)
    g.diag(565.0, 692.7, 714.4, 766.6, weight=56.0)
    g.diag(714.4, 766.6, 756.6, 710.4, weight=56.0)
    g.diag(571.0, 670.4, 611.6, 489.6, weight=48.0)
    g.hbar(589.1, 804.1, 672.8, weight=48.0)
    g.diag(804.1, 676.8, 710.1, 549.4, weight=48.0)
    g.diag(609.9, 605.9, 739.6, 542.0, weight=48.0)
    g.diag(478.1, 543.8, 550.5, 472.9, weight=48.0)
    g.hbar(377.1, 660.2, 457.5, weight=76.0)
    g.diag(660.2, 477.5, 697.3, 525.1, weight=76.0)
    g.diag(320.3, 465.9, 288.4, 287.1, weight=96.0)
    g.diag(288.4, 287.1, 115.3, -62.0, weight=96.0)
    g.hbar(358.4, 725.2, 357.0, weight=64.0)
    g.diag(725.2, 374.5, 675.3, 269.7, weight=64.0)
    g.hbar(653.0, 675.3, 265.9, weight=64.0)
    g.diag(434.1, 409.3, 460.6, 368.4, weight=64.0)
    g.vbar(461.6, 276.5, 368.4, weight=64.0)
    g.diag(462.5, 276.5, 453.8, 268.8, weight=64.0)
    g.diag(558.3, 437.0, 582.9, 412.4, weight=64.0)
    g.diag(582.9, 412.4, 558.0, 293.9, weight=64.0)
    g.diag(558.0, 293.9, 546.7, 287.1, weight=64.0)
    g.hbar(366.3, 642.4, 247.5, weight=64.0)
    g.diag(410.3, 120.8, 418.7, 132.3, weight=64.0)
    g.hbar(418.7, 487.5, 137.3, weight=64.0)
    g.diag(487.5, 142.4, 509.0, 90.0, weight=64.0)
    g.diag(367.3, 217.6, 315.4, -59.5, weight=56.0)
    g.diag(315.4, -59.5, 505.5, 114.1, weight=56.0)
    g.diag(703.8, 244.0, 743.6, 179.8, weight=96.0)
    g.diag(743.6, 179.8, 613.4, 103.3, weight=96.0)
    g.diag(613.4, 103.3, 608.6, 95.6, weight=96.0)
    g.diag(561.0, 250.5, 674.8, 45.8, weight=48.0)
    g.hbar(674.8, 870.2, 18.8, weight=48.0)
    g.vbar(868.5, -8.2, 121.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_9ebb() -> Glyph:
    """麻 U+9EBB —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9EBB", advance=1000, unicode=0x9EBB, note="麻：自动生成")
    g.diag(433.0, 783.1, 513.6, 742.3, weight=64.0)
    g.diag(513.6, 742.3, 551.3, 664.4, weight=64.0)
    g.hbar(298.9, 687.7, 638.1, weight=96.0)
    g.diag(687.7, 662.0, 666.9, 587.9, weight=96.0)
    g.diag(273.1, 624.9, 227.0, 448.1, weight=76.0)
    g.diag(227.0, 448.1, 58.0, -11.5, weight=76.0)
    g.hbar(275.4, 521.4, 375.0, weight=96.0)
    g.diag(372.7, 531.5, 397.8, 368.1, weight=48.0)
    g.vbar(395.5, -36.8, 368.1, weight=48.0)
    g.diag(388.0, 343.9, 345.1, 265.6, weight=48.0)
    g.diag(345.1, 265.6, 200.8, 22.5, weight=48.0)
    g.dot(474.6, 260.5, w=96.0, h=121.4, slant=-14.0)
    g.hbar(536.9, 804.1, 428.6, weight=96.0)
    g.diag(606.2, 629.3, 645.1, 392.2, weight=48.0)
    g.vbar(646.9, -58.1, 392.2, weight=48.0)
    g.diag(628.8, 397.3, 416.9, 87.4, weight=48.0)
    g.diag(677.2, 356.7, 942.0, 79.8, weight=48.0)
    return g
def g_cjk_unified_ideograph_9f13() -> Glyph:
    """鼓 U+9F13 —— 骨架中线自动生成。

    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），
    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。
    """
    g = Glyph("uni9F13", advance=1000, unicode=0x9F13, note="鼓：自动生成")
    g.hbar(110.0, 473.0, 582.5, weight=96.0)
    g.diag(271.4, 726.4, 309.5, 689.4, weight=96.0)
    g.vbar(303.8, 497.1, 689.4, weight=96.0)
    g.diag(298.2, 497.1, 281.7, 477.6, weight=96.0)
    g.hbar(173.8, 408.2, 452.9, weight=84.0)
    g.dot(166.1, 268.3, w=96.0, h=124.8, slant=-14.0)
    g.hbar(172.7, 428.4, 350.6, weight=48.0)
    g.diag(428.4, 360.3, 359.9, 285.3, weight=48.0)
    g.hbar(214.9, 414.4, 240.1, weight=48.0)
    g.dot(193.8, 128.5, w=96.0, h=71.8, slant=-14.0)
    g.diag(361.9, 213.3, 379.9, 176.4, weight=96.0)
    g.diag(379.9, 176.4, 337.3, 99.2, weight=96.0)
    g.hbar(73.0, 129.6, 6.7, weight=96.0)
    g.hbar(129.6, 473.0, 56.5, weight=96.0)
    g.hbar(499.7, 821.6, 505.4, weight=96.0)
    g.diag(590.2, 767.6, 621.8, 649.3, weight=48.0)
    g.vbar(620.9, 378.9, 649.3, weight=48.0)
    g.diag(620.0, 378.9, 597.4, 346.0, weight=48.0)
    g.diag(488.4, 311.0, 591.7, 206.7, weight=48.0)
    g.diag(591.7, 206.7, 388.7, -36.5, weight=48.0)
    g.diag(487.4, 239.0, 947.0, -37.6, weight=96.0)
    return g


def build() -> list[Glyph]:
    return [
        g_cjk_unified_ideograph_4e7e(),        # 乾 U+4E7E
        g_cjk_unified_ideograph_4ff3(),        # 俳 U+4FF3
        g_cjk_unified_ideograph_4ff8(),        # 俸 U+4FF8
        g_cjk_unified_ideograph_4ffa(),        # 俺 U+4FFA
        g_cjk_unified_ideograph_5009(),        # 倉 U+5009
        g_cjk_unified_ideograph_502b(),        # 倫 U+502B
        g_cjk_unified_ideograph_5049(),        # 偉 U+5049
        g_cjk_unified_ideograph_504f(),        # 偏 U+504F
        g_cjk_unified_ideograph_5075(),        # 偵 U+5075
        g_cjk_unified_ideograph_5076(),        # 偶 U+5076
        g_cjk_unified_ideograph_507d(),        # 偽 U+507D
        g_cjk_unified_ideograph_508d(),        # 傍 U+508D
        g_cjk_unified_ideograph_5091(),        # 傑 U+5091
        g_cjk_unified_ideograph_5098(),        # 傘 U+5098
        g_cjk_unified_ideograph_50b2(),        # 傲 U+50B2
        g_cjk_unified_ideograph_50c5(),        # 僅 U+50C5
        g_cjk_unified_ideograph_50cf(),        # 像 U+50CF
        g_cjk_unified_ideograph_50d5(),        # 僕 U+50D5
        g_cjk_unified_ideograph_50e7(),        # 僧 U+50E7
        g_cjk_unified_ideograph_5104(),        # 億 U+5104
        g_cjk_unified_ideograph_5112(),        # 儒 U+5112
        g_cjk_unified_ideograph_517c(),        # 兼 U+517C
        g_cjk_unified_ideograph_51a5(),        # 冥 U+51A5
        g_cjk_unified_ideograph_51c4(),        # 凄 U+51C4
        g_cjk_unified_ideograph_51c6(),        # 准 U+51C6
        g_cjk_unified_ideograph_51dd(),        # 凝 U+51DD
        g_cjk_unified_ideograph_5256(),        # 剖 U+5256
        g_cjk_unified_ideograph_525b(),        # 剛 U+525B
        g_cjk_unified_ideograph_525d(),        # 剝 U+525D
        g_cjk_unified_ideograph_5287(),        # 劇 U+5287
        g_cjk_unified_ideograph_52d8(),        # 勘 U+52D8
        g_cjk_unified_ideograph_533f(),        # 匿 U+533F
        g_cjk_unified_ideograph_54fa(),        # 哺 U+54FA
        g_cjk_unified_ideograph_5504(),        # 唄 U+5504
        g_cjk_unified_ideograph_5507(),        # 唇 U+5507
        g_cjk_unified_ideograph_5510(),        # 唐 U+5510
        g_cjk_unified_ideograph_552f(),        # 唯 U+552F
        g_cjk_unified_ideograph_5531(),        # 唱 U+5531
        g_cjk_unified_ideograph_553e(),        # 唾 U+553E
        g_cjk_unified_ideograph_5553(),        # 啓 U+5553
        g_cjk_unified_ideograph_5589(),        # 喉 U+5589
        g_cjk_unified_ideograph_559a(),        # 喚 U+559A
        g_cjk_unified_ideograph_559d(),        # 喝 U+559D
        g_cjk_unified_ideograph_55c5(),        # 嗅 U+55C5
        g_cjk_unified_ideograph_55e3(),        # 嗣 U+55E3
        g_cjk_unified_ideograph_5606(),        # 嘆 U+5606
        g_cjk_unified_ideograph_5631(),        # 嘱 U+5631
        g_cjk_unified_ideograph_5632(),        # 嘲 U+5632
        g_cjk_unified_ideograph_5668(),        # 器 U+5668
        g_cjk_unified_ideograph_5674(),        # 噴 U+5674
        g_cjk_unified_ideograph_5687(),        # 嚇 U+5687
        g_cjk_unified_ideograph_57f9(),        # 培 U+57F9
        g_cjk_unified_ideograph_5806(),        # 堆 U+5806
        g_cjk_unified_ideograph_5815(),        # 堕 U+5815
        g_cjk_unified_ideograph_5824(),        # 堤 U+5824
        g_cjk_unified_ideograph_582a(),        # 堪 U+582A
        g_cjk_unified_ideograph_584a(),        # 塊 U+584A
        g_cjk_unified_ideograph_5851(),        # 塑 U+5851
        g_cjk_unified_ideograph_5854(),        # 塔 U+5854
        g_cjk_unified_ideograph_5857(),        # 塗 U+5857
        g_cjk_unified_ideograph_585e(),        # 塞 U+585E
        g_cjk_unified_ideograph_5883(),        # 境 U+5883
        g_cjk_unified_ideograph_5893(),        # 墓 U+5893
        g_cjk_unified_ideograph_589c(),        # 墜 U+589C
        g_cjk_unified_ideograph_58a8(),        # 墨 U+58A8
        g_cjk_unified_ideograph_58b3(),        # 墳 U+58B3
        g_cjk_unified_ideograph_58be(),        # 墾 U+58BE
        g_cjk_unified_ideograph_58c1(),        # 壁 U+58C1
        g_cjk_unified_ideograph_596a(),        # 奪 U+596A
        g_cjk_unified_ideograph_596e(),        # 奮 U+596E
        g_cjk_unified_ideograph_59eb(),        # 姫 U+59EB
        g_cjk_unified_ideograph_5a18(),        # 娘 U+5A18
        g_cjk_unified_ideograph_5a20(),        # 娠 U+5A20
        g_cjk_unified_ideograph_5a46(),        # 婆 U+5A46
        g_cjk_unified_ideograph_5a7f(),        # 婿 U+5A7F
        g_cjk_unified_ideograph_5a92(),        # 媒 U+5A92
        g_cjk_unified_ideograph_5a9b(),        # 媛 U+5A9B
        g_cjk_unified_ideograph_5ac1(),        # 嫁 U+5AC1
        g_cjk_unified_ideograph_5ac9(),        # 嫉 U+5AC9
        g_cjk_unified_ideograph_5acc(),        # 嫌 U+5ACC
        g_cjk_unified_ideograph_5ae1(),        # 嫡 U+5AE1
        g_cjk_unified_ideograph_5b6b(),        # 孫 U+5B6B
        g_cjk_unified_ideograph_5bb0(),        # 宰 U+5BB0
        g_cjk_unified_ideograph_5bb4(),        # 宴 U+5BB4
        g_cjk_unified_ideograph_5bb5(),        # 宵 U+5BB5
        g_cjk_unified_ideograph_5bc2(),        # 寂 U+5BC2
        g_cjk_unified_ideograph_5bd2(),        # 寒 U+5BD2
        g_cjk_unified_ideograph_5bdf(),        # 察 U+5BDF
        g_cjk_unified_ideograph_5be7(),        # 寧 U+5BE7
        g_cjk_unified_ideograph_5be9(),        # 審 U+5BE9
        g_cjk_unified_ideograph_5bee(),        # 寮 U+5BEE
        g_cjk_unified_ideograph_5c09(),        # 尉 U+5C09
        g_cjk_unified_ideograph_5c0b(),        # 尋 U+5C0B
        g_cjk_unified_ideograph_5c64(),        # 層 U+5C64
        g_cjk_unified_ideograph_5c65(),        # 履 U+5C65
        g_cjk_unified_ideograph_5cf0(),        # 峰 U+5CF0
        g_cjk_unified_ideograph_5d07(),        # 崇 U+5D07
        g_cjk_unified_ideograph_5d16(),        # 崖 U+5D16
        g_cjk_unified_ideograph_5e33(),        # 帳 U+5E33
        g_cjk_unified_ideograph_5e3d(),        # 帽 U+5E3D
        g_cjk_unified_ideograph_5e63(),        # 幣 U+5E63
        g_cjk_unified_ideograph_5eb6(),        # 庶 U+5EB6
        g_cjk_unified_ideograph_5ec9(),        # 廉 U+5EC9
        g_cjk_unified_ideograph_5eca(),        # 廊 U+5ECA
        g_cjk_unified_ideograph_5f0a(),        # 弊 U+5F0A
        g_cjk_unified_ideograph_5f70(),        # 彰 U+5F70
        g_cjk_unified_ideograph_5f90(),        # 徐 U+5F90
        g_cjk_unified_ideograph_5faa(),        # 循 U+5FAA
        g_cjk_unified_ideograph_5fb4(),        # 徴 U+5FB4
        g_cjk_unified_ideograph_5fb9(),        # 徹 U+5FB9
        g_cjk_unified_ideograph_604b(),        # 恋 U+604B
        g_cjk_unified_ideograph_6063(),        # 恣 U+6063
        g_cjk_unified_ideograph_6065(),        # 恥 U+6065
        g_cjk_unified_ideograph_606d(),        # 恭 U+606D
        g_cjk_unified_ideograph_609f(),        # 悟 U+609F
        g_cjk_unified_ideograph_60a6(),        # 悦 U+60A6
        g_cjk_unified_ideograph_60bc(),        # 悼 U+60BC
        g_cjk_unified_ideograph_60e7(),        # 惧 U+60E7
        g_cjk_unified_ideograph_60e8(),        # 惨 U+60E8
        g_cjk_unified_ideograph_60f0(),        # 惰 U+60F0
        g_cjk_unified_ideograph_6101(),        # 愁 U+6101
        g_cjk_unified_ideograph_6109(),        # 愉 U+6109
        g_cjk_unified_ideograph_611a(),        # 愚 U+611A
        g_cjk_unified_ideograph_6144(),        # 慄 U+6144
        g_cjk_unified_ideograph_614b(),        # 態 U+614B
        g_cjk_unified_ideograph_614c(),        # 慌 U+614C
        g_cjk_unified_ideograph_6155(),        # 慕 U+6155
        g_cjk_unified_ideograph_6162(),        # 慢 U+6162
        g_cjk_unified_ideograph_6163(),        # 慣 U+6163
        g_cjk_unified_ideograph_6168(),        # 慨 U+6168
        g_cjk_unified_ideograph_6170(),        # 慰 U+6170
        g_cjk_unified_ideograph_6176(),        # 慶 U+6176
        g_cjk_unified_ideograph_6182(),        # 憂 U+6182
        g_cjk_unified_ideograph_618e(),        # 憎 U+618E
        g_cjk_unified_ideograph_61a4(),        # 憤 U+61A4
        g_cjk_unified_ideograph_61a7(),        # 憧 U+61A7
        g_cjk_unified_ideograph_61a9(),        # 憩 U+61A9
        g_cjk_unified_ideograph_61ac(),        # 憬 U+61AC
        g_cjk_unified_ideograph_61b2(),        # 憲 U+61B2
        g_cjk_unified_ideograph_61b6(),        # 憶 U+61B6
        g_cjk_unified_ideograph_61be(),        # 憾 U+61BE
        g_cjk_unified_ideograph_61c7(),        # 懇 U+61C7
        g_cjk_unified_ideograph_61f2(),        # 懲 U+61F2
        g_cjk_unified_ideograph_61f8(),        # 懸 U+61F8
        g_cjk_unified_ideograph_621a(),        # 戚 U+621A
        g_cjk_unified_ideograph_6247(),        # 扇 U+6247
        g_cjk_unified_ideograph_6249(),        # 扉 U+6249
        g_cjk_unified_ideograph_62f3(),        # 拳 U+62F3
        g_cjk_unified_ideograph_6328(),        # 挨 U+6328
        g_cjk_unified_ideograph_632b(),        # 挫 U+632B
        g_cjk_unified_ideograph_6349(),        # 捉 U+6349
        g_cjk_unified_ideograph_636e(),        # 据 U+636E
        g_cjk_unified_ideograph_637b(),        # 捻 U+637B
        g_cjk_unified_ideograph_638c(),        # 掌 U+638C
        g_cjk_unified_ideograph_63da(),        # 揚 U+63DA
        g_cjk_unified_ideograph_642c(),        # 搬 U+642C
        g_cjk_unified_ideograph_642d(),        # 搭 U+642D
        g_cjk_unified_ideograph_6458(),        # 摘 U+6458
        g_cjk_unified_ideograph_6469(),        # 摩 U+6469
        g_cjk_unified_ideograph_646f(),        # 摯 U+646F
        g_cjk_unified_ideograph_64a4(),        # 撤 U+64A4
        g_cjk_unified_ideograph_64ae(),        # 撮 U+64AE
        g_cjk_unified_ideograph_64b2(),        # 撲 U+64B2
        g_cjk_unified_ideograph_64c1(),        # 擁 U+64C1
        g_cjk_unified_ideograph_64cd(),        # 操 U+64CD
        g_cjk_unified_ideograph_64e6(),        # 擦 U+64E6
        g_cjk_unified_ideograph_64ec(),        # 擬 U+64EC
        g_cjk_unified_ideograph_6562(),        # 敢 U+6562
        g_cjk_unified_ideograph_6574(),        # 整 U+6574
        g_cjk_unified_ideograph_6575(),        # 敵 U+6575
        g_cjk_unified_ideograph_6577(),        # 敷 U+6577
        g_cjk_unified_ideograph_6591(),        # 斑 U+6591
        g_cjk_unified_ideograph_659c(),        # 斜 U+659C
        g_cjk_unified_ideograph_65ac(),        # 斬 U+65AC
        g_cjk_unified_ideograph_65cb(),        # 旋 U+65CB
        g_cjk_unified_ideograph_65d7(),        # 旗 U+65D7
        g_cjk_unified_ideograph_6676(),        # 晶 U+6676
        g_cjk_unified_ideograph_6687(),        # 暇 U+6687
        g_cjk_unified_ideograph_6691(),        # 暑 U+6691
        g_cjk_unified_ideograph_6696(),        # 暖 U+6696
        g_cjk_unified_ideograph_66ab(),        # 暫 U+66AB
        g_cjk_unified_ideograph_66ae(),        # 暮 U+66AE
        g_cjk_unified_ideograph_66b4(),        # 暴 U+66B4
        g_cjk_unified_ideograph_66c7(),        # 曇 U+66C7
        g_cjk_unified_ideograph_66d6(),        # 曖 U+66D6
        g_cjk_unified_ideograph_66dc(),        # 曜 U+66DC
        g_cjk_unified_ideograph_66f9(),        # 曹 U+66F9
        g_cjk_unified_ideograph_6715(),        # 朕 U+6715
        g_cjk_unified_ideograph_6717(),        # 朗 U+6717
        g_cjk_unified_ideograph_683d(),        # 栽 U+683D
        g_cjk_unified_ideograph_6841(),        # 桁 U+6841
        g_cjk_unified_ideograph_6843(),        # 桃 U+6843
        g_cjk_unified_ideograph_6851(),        # 桑 U+6851
        g_cjk_unified_ideograph_6885(),        # 梅 U+6885
        g_cjk_unified_ideograph_6897(),        # 梗 U+6897
        g_cjk_unified_ideograph_68a8(),        # 梨 U+68A8
        g_cjk_unified_ideograph_68b0(),        # 械 U+68B0
        g_cjk_unified_ideograph_68cb(),        # 棋 U+68CB
        g_cjk_unified_ideograph_68da(),        # 棚 U+68DA
        g_cjk_unified_ideograph_68df(),        # 棟 U+68DF
        g_cjk_unified_ideograph_68fa(),        # 棺 U+68FA
        g_cjk_unified_ideograph_6905(),        # 椅 U+6905
        g_cjk_unified_ideograph_690e(),        # 椎 U+690E
        g_cjk_unified_ideograph_6977(),        # 楷 U+6977
        g_cjk_unified_ideograph_697c(),        # 楼 U+697C
        g_cjk_unified_ideograph_6982(),        # 概 U+6982
        g_cjk_unified_ideograph_69cb(),        # 構 U+69CB
        g_cjk_unified_ideograph_69fd(),        # 槽 U+69FD
        g_cjk_unified_ideograph_6a19(),        # 標 U+6A19
        g_cjk_unified_ideograph_6a21(),        # 模 U+6A21
        g_cjk_unified_ideograph_6a39(),        # 樹 U+6A39
        g_cjk_unified_ideograph_6b04(),        # 欄 U+6B04
        g_cjk_unified_ideograph_6b3a(),        # 欺 U+6B3A
        g_cjk_unified_ideograph_6b3e(),        # 款 U+6B3E
        g_cjk_unified_ideograph_6b4c(),        # 歌 U+6B4C
        g_cjk_unified_ideograph_6b89(),        # 殉 U+6B89
        g_cjk_unified_ideograph_6b8a(),        # 殊 U+6B8A
        g_cjk_unified_ideograph_6b96(),        # 殖 U+6B96
        g_cjk_unified_ideograph_6bbf(),        # 殿 U+6BBF
        g_cjk_unified_ideograph_6bc0(),        # 毀 U+6BC0
        g_cjk_unified_ideograph_6d6a(),        # 浪 U+6D6A
        g_cjk_unified_ideograph_6d74(),        # 浴 U+6D74
        g_cjk_unified_ideograph_6d78(),        # 浸 U+6D78
        g_cjk_unified_ideograph_6daf(),        # 涯 U+6DAF
        g_cjk_unified_ideograph_6db2(),        # 液 U+6DB2
        g_cjk_unified_ideograph_6dbc(),        # 涼 U+6DBC
        g_cjk_unified_ideograph_6dd1(),        # 淑 U+6DD1
        g_cjk_unified_ideograph_6de1(),        # 淡 U+6DE1
        g_cjk_unified_ideograph_6deb(),        # 淫 U+6DEB
        g_cjk_unified_ideograph_6dfb(),        # 添 U+6DFB
        g_cjk_unified_ideograph_6e26(),        # 渦 U+6E26
        g_cjk_unified_ideograph_6e56(),        # 湖 U+6E56
        g_cjk_unified_ideograph_6e67(),        # 湧 U+6E67
        g_cjk_unified_ideograph_6e6f(),        # 湯 U+6E6F
        g_cjk_unified_ideograph_6e7f(),        # 湿 U+6E7F
        g_cjk_unified_ideograph_6e9d(),        # 溝 U+6E9D
        g_cjk_unified_ideograph_6eb6(),        # 溶 U+6EB6
        g_cjk_unified_ideograph_6eba(),        # 溺 U+6EBA
        g_cjk_unified_ideograph_6ecb(),        # 滋 U+6ECB
        g_cjk_unified_ideograph_6ef4(),        # 滴 U+6EF4
        g_cjk_unified_ideograph_6f01(),        # 漁 U+6F01
        g_cjk_unified_ideograph_6f02(),        # 漂 U+6F02
        g_cjk_unified_ideograph_6f0f(),        # 漏 U+6F0F
        g_cjk_unified_ideograph_6f14(),        # 演 U+6F14
        g_cjk_unified_ideograph_6f20(),        # 漠 U+6F20
        g_cjk_unified_ideograph_6f22(),        # 漢 U+6F22
        g_cjk_unified_ideograph_6f2b(),        # 漫 U+6F2B
        g_cjk_unified_ideograph_6f2c(),        # 漬 U+6F2C
        g_cjk_unified_ideograph_6f38(),        # 漸 U+6F38
        g_cjk_unified_ideograph_6f54(),        # 潔 U+6F54
        g_cjk_unified_ideograph_6f5c(),        # 潜 U+6F5C
        g_cjk_unified_ideograph_6f5f(),        # 潟 U+6F5F
        g_cjk_unified_ideograph_6f64(),        # 潤 U+6F64
        g_cjk_unified_ideograph_6f6e(),        # 潮 U+6F6E
        g_cjk_unified_ideograph_6f70(),        # 潰 U+6F70
        g_cjk_unified_ideograph_6f84(),        # 澄 U+6F84
        g_cjk_unified_ideograph_6fc0(),        # 激 U+6FC0
        g_cjk_unified_ideograph_6fc1(),        # 濁 U+6FC1
        g_cjk_unified_ideograph_6fc3(),        # 濃 U+6FC3
        g_cjk_unified_ideograph_6feb(),        # 濫 U+6FEB
        g_cjk_unified_ideograph_6fef(),        # 濯 U+6FEF
        g_cjk_unified_ideograph_70c8(),        # 烈 U+70C8
        g_cjk_unified_ideograph_714e(),        # 煎 U+714E
        g_cjk_unified_ideograph_7159(),        # 煙 U+7159
        g_cjk_unified_ideograph_7169(),        # 煩 U+7169
        g_cjk_unified_ideograph_718a(),        # 熊 U+718A
        g_cjk_unified_ideograph_71b1(),        # 熱 U+71B1
        g_cjk_unified_ideograph_71c3(),        # 燃 U+71C3
        g_cjk_unified_ideograph_71e5(),        # 燥 U+71E5
        g_cjk_unified_ideograph_7206(),        # 爆 U+7206
        g_cjk_unified_ideograph_7235(),        # 爵 U+7235
        g_cjk_unified_ideograph_723d(),        # 爽 U+723D
        g_cjk_unified_ideograph_731b(),        # 猛 U+731B
        g_cjk_unified_ideograph_732b(),        # 猫 U+732B
        g_cjk_unified_ideograph_7336(),        # 猶 U+7336
        g_cjk_unified_ideograph_733f(),        # 猿 U+733F
        g_cjk_unified_ideograph_7344(),        # 獄 U+7344
        g_cjk_unified_ideograph_7372(),        # 獲 U+7372
        g_cjk_unified_ideograph_73e0(),        # 珠 U+73E0
        g_cjk_unified_ideograph_73ed(),        # 班 U+73ED
        g_cjk_unified_ideograph_74a7(),        # 璧 U+74A7
        g_cjk_unified_ideograph_74b0(),        # 環 U+74B0
        g_cjk_unified_ideograph_74bd(),        # 璽 U+74BD
        g_cjk_unified_ideograph_74f6(),        # 瓶 U+74F6
        g_cjk_unified_ideograph_7554(),        # 畔 U+7554
        g_cjk_unified_ideograph_755c(),        # 畜 U+755C
        g_cjk_unified_ideograph_755d(),        # 畝 U+755D
        g_cjk_unified_ideograph_7591(),        # 疑 U+7591
        g_cjk_unified_ideograph_75be(),        # 疾 U+75BE
        g_cjk_unified_ideograph_75c7(),        # 症 U+75C7
        g_cjk_unified_ideograph_75d5(),        # 痕 U+75D5
        g_cjk_unified_ideograph_75d8(),        # 痘 U+75D8
        g_cjk_unified_ideograph_75e2(),        # 痢 U+75E2
        g_cjk_unified_ideograph_75f4(),        # 痴 U+75F4
        g_cjk_unified_ideograph_7642(),        # 療 U+7642
        g_cjk_unified_ideograph_7652(),        # 癒 U+7652
        g_cjk_unified_ideograph_7656(),        # 癖 U+7656
        g_cjk_unified_ideograph_76e3(),        # 監 U+76E3
        g_cjk_unified_ideograph_76e4(),        # 盤 U+76E4
        g_cjk_unified_ideograph_7720(),        # 眠 U+7720
        g_cjk_unified_ideograph_773a(),        # 眺 U+773A
        g_cjk_unified_ideograph_773c(),        # 眼 U+773C
        g_cjk_unified_ideograph_7761(),        # 睡 U+7761
        g_cjk_unified_ideograph_7766(),        # 睦 U+7766
        g_cjk_unified_ideograph_77ac(),        # 瞬 U+77AC
        g_cjk_unified_ideograph_77ad(),        # 瞭 U+77AD
        g_cjk_unified_ideograph_77b3(),        # 瞳 U+77B3
        g_cjk_unified_ideograph_785d(),        # 硝 U+785D
        g_cjk_unified_ideograph_786b(),        # 硫 U+786B
        g_cjk_unified_ideograph_7891(),        # 碑 U+7891
        g_cjk_unified_ideograph_78ba(),        # 確 U+78BA
        g_cjk_unified_ideograph_78c1(),        # 磁 U+78C1
        g_cjk_unified_ideograph_78e8(),        # 磨 U+78E8
        g_cjk_unified_ideograph_7901(),        # 礁 U+7901
        g_cjk_unified_ideograph_790e(),        # 礎 U+790E
        g_cjk_unified_ideograph_796d(),        # 祭 U+796D
        g_cjk_unified_ideograph_7985(),        # 禅 U+7985
        g_cjk_unified_ideograph_798d(),        # 禍 U+798D
        g_cjk_unified_ideograph_79df(),        # 租 U+79DF
        g_cjk_unified_ideograph_7a1a(),        # 稚 U+7A1A
        g_cjk_unified_ideograph_7a2e(),        # 種 U+7A2E
        g_cjk_unified_ideograph_7a3c(),        # 稼 U+7A3C
        g_cjk_unified_ideograph_7a3f(),        # 稿 U+7A3F
        g_cjk_unified_ideograph_7a40(),        # 穀 U+7A40
        g_cjk_unified_ideograph_7a4d(),        # 積 U+7A4D
        g_cjk_unified_ideograph_7a92(),        # 窒 U+7A92
        g_cjk_unified_ideograph_7a9f(),        # 窟 U+7A9F
        g_cjk_unified_ideograph_7aae(),        # 窮 U+7AAE
        g_cjk_unified_ideograph_7aaf(),        # 窯 U+7AAF
        g_cjk_unified_ideograph_7ae5(),        # 童 U+7AE5
        g_cjk_unified_ideograph_7aef(),        # 端 U+7AEF
        g_cjk_unified_ideograph_7af6(),        # 競 U+7AF6
        g_cjk_unified_ideograph_7b1b(),        # 笛 U+7B1B
        g_cjk_unified_ideograph_7b26(),        # 符 U+7B26
        g_cjk_unified_ideograph_7b52(),        # 筒 U+7B52
        g_cjk_unified_ideograph_7b97(),        # 算 U+7B97
        g_cjk_unified_ideograph_7ba1(),        # 管 U+7BA1
        g_cjk_unified_ideograph_7bb1(),        # 箱 U+7BB1
        g_cjk_unified_ideograph_7bb8(),        # 箸 U+7BB8
        g_cjk_unified_ideograph_7bc4(),        # 範 U+7BC4
        g_cjk_unified_ideograph_7bc9(),        # 築 U+7BC9
        g_cjk_unified_ideograph_7be4(),        # 篤 U+7BE4
        g_cjk_unified_ideograph_7c21(),        # 簡 U+7C21
        g_cjk_unified_ideograph_7c3f(),        # 簿 U+7C3F
        g_cjk_unified_ideograph_7c4d(),        # 籍 U+7C4D
        g_cjk_unified_ideograph_7c60(),        # 籠 U+7C60
        g_cjk_unified_ideograph_7c89(),        # 粉 U+7C89
        g_cjk_unified_ideograph_7c92(),        # 粒 U+7C92
        g_cjk_unified_ideograph_7c97(),        # 粗 U+7C97
        g_cjk_unified_ideograph_7c98(),        # 粘 U+7C98
        g_cjk_unified_ideograph_7cbe(),        # 精 U+7CBE
        g_cjk_unified_ideograph_7cd6(),        # 糖 U+7CD6
        g_cjk_unified_ideograph_7ce7(),        # 糧 U+7CE7
        g_cjk_unified_ideograph_7d0b(),        # 紋 U+7D0B
        g_cjk_unified_ideograph_7d21(),        # 紡 U+7D21
        g_cjk_unified_ideograph_7d22(),        # 索 U+7D22
        g_cjk_unified_ideograph_7d2b(),        # 紫 U+7D2B
        g_cjk_unified_ideograph_7d2f(),        # 累 U+7D2F
        g_cjk_unified_ideograph_7d33(),        # 紳 U+7D33
        g_cjk_unified_ideograph_7d79(),        # 絹 U+7D79
        g_cjk_unified_ideograph_7dad(),        # 維 U+7DAD
        g_cjk_unified_ideograph_7db1(),        # 綱 U+7DB1
        g_cjk_unified_ideograph_7db2(),        # 網 U+7DB2
        g_cjk_unified_ideograph_7dbb(),        # 綻 U+7DBB
        g_cjk_unified_ideograph_7dbf(),        # 綿 U+7DBF
        g_cjk_unified_ideograph_7dca(),        # 緊 U+7DCA
        g_cjk_unified_ideograph_7dd2(),        # 緒 U+7DD2
        g_cjk_unified_ideograph_7dda(),        # 線 U+7DDA
        g_cjk_unified_ideograph_7de0(),        # 締 U+7DE0
        g_cjk_unified_ideograph_7de9(),        # 緩 U+7DE9
        g_cjk_unified_ideograph_7def(),        # 緯 U+7DEF
        g_cjk_unified_ideograph_7df4(),        # 練 U+7DF4
        g_cjk_unified_ideograph_7dfb(),        # 緻 U+7DFB
        g_cjk_unified_ideograph_7e1b(),        # 縛 U+7E1B
        g_cjk_unified_ideograph_7e2b(),        # 縫 U+7E2B
        g_cjk_unified_ideograph_7e2e(),        # 縮 U+7E2E
        g_cjk_unified_ideograph_7e3e(),        # 績 U+7E3E
        g_cjk_unified_ideograph_7e41(),        # 繁 U+7E41
        g_cjk_unified_ideograph_7e54(),        # 織 U+7E54
        g_cjk_unified_ideograph_7e55(),        # 繕 U+7E55
        g_cjk_unified_ideograph_7e70(),        # 繰 U+7E70
        g_cjk_unified_ideograph_7f75(),        # 罵 U+7F75
        g_cjk_unified_ideograph_7f77(),        # 罷 U+7F77
        g_cjk_unified_ideograph_7f85(),        # 羅 U+7F85
        g_cjk_unified_ideograph_7f9e(),        # 羞 U+7F9E
        g_cjk_unified_ideograph_7fa8(),        # 羨 U+7FA8
        g_cjk_unified_ideograph_7fc1(),        # 翁 U+7FC1
        g_cjk_unified_ideograph_7ffb(),        # 翻 U+7FFB
        g_cjk_unified_ideograph_7ffc(),        # 翼 U+7FFC
        g_cjk_unified_ideograph_8015(),        # 耕 U+8015
        g_cjk_unified_ideograph_8017(),        # 耗 U+8017
        g_cjk_unified_ideograph_8056(),        # 聖 U+8056
        g_cjk_unified_ideograph_805e(),        # 聞 U+805E
        g_cjk_unified_ideograph_8077(),        # 職 U+8077
        g_cjk_unified_ideograph_80f4(),        # 胴 U+80F4
        g_cjk_unified_ideograph_80f8(),        # 胸 U+80F8
        g_cjk_unified_ideograph_8102(),        # 脂 U+8102
        g_cjk_unified_ideograph_8108(),        # 脈 U+8108
        g_cjk_unified_ideograph_810a(),        # 脊 U+810A
        g_cjk_unified_ideograph_811a(),        # 脚 U+811A
        g_cjk_unified_ideograph_814e(),        # 腎 U+814E
        g_cjk_unified_ideograph_8150(),        # 腐 U+8150
        g_cjk_unified_ideograph_8155(),        # 腕 U+8155
        g_cjk_unified_ideograph_8170(),        # 腰 U+8170
        g_cjk_unified_ideograph_8178(),        # 腸 U+8178
        g_cjk_unified_ideograph_817a(),        # 腺 U+817A
        g_cjk_unified_ideograph_819c(),        # 膜 U+819C
        g_cjk_unified_ideograph_819d(),        # 膝 U+819D
        g_cjk_unified_ideograph_81a8(),        # 膨 U+81A8
        g_cjk_unified_ideograph_81b3(),        # 膳 U+81B3
        g_cjk_unified_ideograph_81e8(),        # 臨 U+81E8
        g_cjk_unified_ideograph_8208(),        # 興 U+8208
        g_cjk_unified_ideograph_821e(),        # 舞 U+821E
        g_cjk_unified_ideograph_8236(),        # 舶 U+8236
        g_cjk_unified_ideograph_8237(),        # 舷 U+8237
        g_cjk_unified_ideograph_8247(),        # 艇 U+8247
        g_cjk_unified_ideograph_8266(),        # 艦 U+8266
        g_cjk_unified_ideograph_8377(),        # 荷 U+8377
        g_cjk_unified_ideograph_83cc(),        # 菌 U+83CC
        g_cjk_unified_ideograph_83dc(),        # 菜 U+83DC
        g_cjk_unified_ideograph_840e(),        # 萎 U+840E
        g_cjk_unified_ideograph_845b(),        # 葛 U+845B
        g_cjk_unified_ideograph_84b8(),        # 蒸 U+84B8
        g_cjk_unified_ideograph_84cb(),        # 蓋 U+84CB
        g_cjk_unified_ideograph_853d(),        # 蔽 U+853D
        g_cjk_unified_ideograph_8584(),        # 薄 U+8584
        g_cjk_unified_ideograph_85a6(),        # 薦 U+85A6
        g_cjk_unified_ideograph_85aa(),        # 薪 U+85AA
        g_cjk_unified_ideograph_85cd(),        # 藍 U+85CD
        g_cjk_unified_ideograph_85e4(),        # 藤 U+85E4
        g_cjk_unified_ideograph_8650(),        # 虐 U+8650
        g_cjk_unified_ideograph_865a(),        # 虚 U+865A
        g_cjk_unified_ideograph_865c(),        # 虜 U+865C
        g_cjk_unified_ideograph_868a(),        # 蚊 U+868A
        g_cjk_unified_ideograph_8695(),        # 蚕 U+8695
        g_cjk_unified_ideograph_86c7(),        # 蛇 U+86C7
        g_cjk_unified_ideograph_86ee(),        # 蛮 U+86EE
        g_cjk_unified_ideograph_8702(),        # 蜂 U+8702
        g_cjk_unified_ideograph_871c(),        # 蜜 U+871C
        g_cjk_unified_ideograph_878d(),        # 融 U+878D
        g_cjk_unified_ideograph_885b(),        # 衛 U+885B
        g_cjk_unified_ideograph_885d(),        # 衝 U+885D
        g_cjk_unified_ideograph_8861(),        # 衡 U+8861
        g_cjk_unified_ideograph_8877(),        # 衷 U+8877
        g_cjk_unified_ideograph_888b(),        # 袋 U+888B
        g_cjk_unified_ideograph_8896(),        # 袖 U+8896
        g_cjk_unified_ideograph_88f8(),        # 裸 U+88F8
        g_cjk_unified_ideograph_88fd(),        # 製 U+88FD
        g_cjk_unified_ideograph_88fe(),        # 裾 U+88FE
        g_cjk_unified_ideograph_8907(),        # 複 U+8907
        g_cjk_unified_ideograph_8910(),        # 褐 U+8910
        g_cjk_unified_ideograph_8912(),        # 褒 U+8912
        g_cjk_unified_ideograph_895f(),        # 襟 U+895F
        g_cjk_unified_ideograph_89aa(),        # 親 U+89AA
        g_cjk_unified_ideograph_8a13(),        # 訓 U+8A13
        g_cjk_unified_ideograph_8a50(),        # 詐 U+8A50
        g_cjk_unified_ideograph_8a54(),        # 詔 U+8A54
        g_cjk_unified_ideograph_8a5e(),        # 詞 U+8A5E
        g_cjk_unified_ideograph_8a60(),        # 詠 U+8A60
        g_cjk_unified_ideograph_8a69(),        # 詩 U+8A69
        g_cjk_unified_ideograph_8a6e(),        # 詮 U+8A6E
        g_cjk_unified_ideograph_8a72(),        # 該 U+8A72
        g_cjk_unified_ideograph_8a73(),        # 詳 U+8A73
        g_cjk_unified_ideograph_8a8c(),        # 誌 U+8A8C
        g_cjk_unified_ideograph_8a8d(),        # 認 U+8A8D
        g_cjk_unified_ideograph_8a93(),        # 誓 U+8A93
        g_cjk_unified_ideograph_8a98(),        # 誘 U+8A98
        g_cjk_unified_ideograph_8a9e(),        # 語 U+8A9E
        g_cjk_unified_ideograph_8aa0(),        # 誠 U+8AA0
        g_cjk_unified_ideograph_8aa4(),        # 誤 U+8AA4
        g_cjk_unified_ideograph_8ab0(),        # 誰 U+8AB0
        g_cjk_unified_ideograph_8ab2(),        # 課 U+8AB2
        g_cjk_unified_ideograph_8abf(),        # 調 U+8ABF
        g_cjk_unified_ideograph_8ac7(),        # 談 U+8AC7
        g_cjk_unified_ideograph_8acb(),        # 請 U+8ACB
        g_cjk_unified_ideograph_8ae6(),        # 諦 U+8AE6
        g_cjk_unified_ideograph_8aed(),        # 諭 U+8AED
        g_cjk_unified_ideograph_8aee(),        # 諮 U+8AEE
        g_cjk_unified_ideograph_8b00(),        # 謀 U+8B00
        g_cjk_unified_ideograph_8b01(),        # 謁 U+8B01
        g_cjk_unified_ideograph_8b04(),        # 謄 U+8B04
        g_cjk_unified_ideograph_8b0e(),        # 謎 U+8B0E
        g_cjk_unified_ideograph_8b1b(),        # 講 U+8B1B
        g_cjk_unified_ideograph_8b1d(),        # 謝 U+8B1D
        g_cjk_unified_ideograph_8b39(),        # 謹 U+8B39
        g_cjk_unified_ideograph_8b58(),        # 識 U+8B58
        g_cjk_unified_ideograph_8b5c(),        # 譜 U+8B5C
        g_cjk_unified_ideograph_8b77(),        # 護 U+8B77
        g_cjk_unified_ideograph_8c5a(),        # 豚 U+8C5A
        g_cjk_unified_ideograph_8c6a(),        # 豪 U+8C6A
        g_cjk_unified_ideograph_8c8c(),        # 貌 U+8C8C
        g_cjk_unified_ideograph_8ca7(),        # 貧 U+8CA7
        g_cjk_unified_ideograph_8caa(),        # 貪 U+8CAA
        g_cjk_unified_ideograph_8cab(),        # 貫 U+8CAB
        g_cjk_unified_ideograph_8cbc(),        # 貼 U+8CBC
        g_cjk_unified_ideograph_8cc2(),        # 賂 U+8CC2
        g_cjk_unified_ideograph_8cca(),        # 賊 U+8CCA
        g_cjk_unified_ideograph_8cd3(),        # 賓 U+8CD3
        g_cjk_unified_ideograph_8cdc(),        # 賜 U+8CDC
        g_cjk_unified_ideograph_8ce0(),        # 賠 U+8CE0
        g_cjk_unified_ideograph_8ce6(),        # 賦 U+8CE6
        g_cjk_unified_ideograph_8cea(),        # 質 U+8CEA
        g_cjk_unified_ideograph_8ced(),        # 賭 U+8CED
        g_cjk_unified_ideograph_8d08(),        # 贈 U+8D08
        g_cjk_unified_ideograph_8d66(),        # 赦 U+8D66
        g_cjk_unified_ideograph_8da3(),        # 趣 U+8DA3
        g_cjk_unified_ideograph_8ddd(),        # 距 U+8DDD
        g_cjk_unified_ideograph_8df3(),        # 跳 U+8DF3
        g_cjk_unified_ideograph_8e0a(),        # 踊 U+8E0A
        g_cjk_unified_ideograph_8e2a(),        # 踪 U+8E2A
        g_cjk_unified_ideograph_8e74(),        # 蹴 U+8E74
        g_cjk_unified_ideograph_8e8d(),        # 躍 U+8E8D
        g_cjk_unified_ideograph_8ed2(),        # 軒 U+8ED2
        g_cjk_unified_ideograph_8f03(),        # 較 U+8F03
        g_cjk_unified_ideograph_8f1d(),        # 輝 U+8F1D
        g_cjk_unified_ideograph_8f29(),        # 輩 U+8F29
        g_cjk_unified_ideograph_8f38(),        # 輸 U+8F38
        g_cjk_unified_ideograph_8f44(),        # 轄 U+8F44
        g_cjk_unified_ideograph_8fa3(),        # 辣 U+8FA3
        g_cjk_unified_ideograph_8fb1(),        # 辱 U+8FB1
        g_cjk_unified_ideograph_9038(),        # 逸 U+9038
        g_cjk_unified_ideograph_9042(),        # 遂 U+9042
        g_cjk_unified_ideograph_9047(),        # 遇 U+9047
        g_cjk_unified_ideograph_904d(),        # 遍 U+904D
        g_cjk_unified_ideograph_905c(),        # 遜 U+905C
        g_cjk_unified_ideograph_906d(),        # 遭 U+906D
        g_cjk_unified_ideograph_906e(),        # 遮 U+906E
        g_cjk_unified_ideograph_9075(),        # 遵 U+9075
        g_cjk_unified_ideograph_9078(),        # 選 U+9078
        g_cjk_unified_ideograph_907a(),        # 遺 U+907A
        g_cjk_unified_ideograph_907f(),        # 避 U+907F
        g_cjk_unified_ideograph_9084(),        # 還 U+9084
        g_cjk_unified_ideograph_90ed(),        # 郭 U+90ED
        g_cjk_unified_ideograph_914c(),        # 酌 U+914C
        g_cjk_unified_ideograph_914e(),        # 酎 U+914E
        g_cjk_unified_ideograph_9162(),        # 酢 U+9162
        g_cjk_unified_ideograph_916c(),        # 酬 U+916C
        g_cjk_unified_ideograph_9175(),        # 酵 U+9175
        g_cjk_unified_ideograph_9177(),        # 酷 U+9177
        g_cjk_unified_ideograph_9178(),        # 酸 U+9178
        g_cjk_unified_ideograph_9192(),        # 醒 U+9192
        g_cjk_unified_ideograph_919c(),        # 醜 U+919C
        g_cjk_unified_ideograph_91dc(),        # 釜 U+91DC
        g_cjk_unified_ideograph_91e3(),        # 釣 U+91E3
        g_cjk_unified_ideograph_920d(),        # 鈍 U+920D
        g_cjk_unified_ideograph_925b(),        # 鉛 U+925B
        g_cjk_unified_ideograph_9280(),        # 銀 U+9280
        g_cjk_unified_ideograph_9283(),        # 銃 U+9283
        g_cjk_unified_ideograph_9285(),        # 銅 U+9285
        g_cjk_unified_ideograph_9298(),        # 銘 U+9298
        g_cjk_unified_ideograph_92fc(),        # 鋼 U+92FC
        g_cjk_unified_ideograph_9320(),        # 錠 U+9320
        g_cjk_unified_ideograph_9326(),        # 錦 U+9326
        g_cjk_unified_ideograph_932f(),        # 錯 U+932F
        g_cjk_unified_ideograph_9332(),        # 録 U+9332
        g_cjk_unified_ideograph_934b(),        # 鍋 U+934B
        g_cjk_unified_ideograph_935b(),        # 鍛 U+935B
        g_cjk_unified_ideograph_9375(),        # 鍵 U+9375
        g_cjk_unified_ideograph_9396(),        # 鎖 U+9396
        g_cjk_unified_ideograph_93ae(),        # 鎮 U+93AE
        g_cjk_unified_ideograph_9418(),        # 鐘 U+9418
        g_cjk_unified_ideograph_9451(),        # 鑑 U+9451
        g_cjk_unified_ideograph_9591(),        # 閑 U+9591
        g_cjk_unified_ideograph_95a3(),        # 閣 U+95A3
        g_cjk_unified_ideograph_95a5(),        # 閥 U+95A5
        g_cjk_unified_ideograph_965b(),        # 陛 U+965B
        g_cjk_unified_ideograph_966a(),        # 陪 U+966A
        g_cjk_unified_ideograph_9670(),        # 陰 U+9670
        g_cjk_unified_ideograph_9673(),        # 陳 U+9673
        g_cjk_unified_ideograph_9675(),        # 陵 U+9675
        g_cjk_unified_ideograph_9676(),        # 陶 U+9676
        g_cjk_unified_ideograph_9685(),        # 隅 U+9685
        g_cjk_unified_ideograph_968f(),        # 随 U+968F
        g_cjk_unified_ideograph_9694(),        # 隔 U+9694
        g_cjk_unified_ideograph_9699(),        # 隙 U+9699
        g_cjk_unified_ideograph_969b(),        # 際 U+969B
        g_cjk_unified_ideograph_969c(),        # 障 U+969C
        g_cjk_unified_ideograph_96bb(),        # 隻 U+96BB
        g_cjk_unified_ideograph_96c5(),        # 雅 U+96C5
        g_cjk_unified_ideograph_96cc(),        # 雌 U+96CC
        g_cjk_unified_ideograph_96e2(),        # 離 U+96E2
        g_cjk_unified_ideograph_96ea(),        # 雪 U+96EA
        g_cjk_unified_ideograph_96f6(),        # 零 U+96F6
        g_cjk_unified_ideograph_96f7(),        # 雷 U+96F7
        g_cjk_unified_ideograph_9700(),        # 需 U+9700
        g_cjk_unified_ideograph_9707(),        # 震 U+9707
        g_cjk_unified_ideograph_9727(),        # 霧 U+9727
        g_cjk_unified_ideograph_9732(),        # 露 U+9732
        g_cjk_unified_ideograph_9774(),        # 靴 U+9774
        g_cjk_unified_ideograph_97d3(),        # 韓 U+97D3
        g_cjk_unified_ideograph_97fb(),        # 韻 U+97FB
        g_cjk_unified_ideograph_9802(),        # 頂 U+9802
        g_cjk_unified_ideograph_9803(),        # 頃 U+9803
        g_cjk_unified_ideograph_9812(),        # 頒 U+9812
        g_cjk_unified_ideograph_9813(),        # 頓 U+9813
        g_cjk_unified_ideograph_9818(),        # 領 U+9818
        g_cjk_unified_ideograph_982d(),        # 頭 U+982D
        g_cjk_unified_ideograph_9830(),        # 頰 U+9830
        g_cjk_unified_ideograph_983b(),        # 頻 U+983B
        g_cjk_unified_ideograph_984c(),        # 題 U+984C
        g_cjk_unified_ideograph_984d(),        # 額 U+984D
        g_cjk_unified_ideograph_984e(),        # 顎 U+984E
        g_cjk_unified_ideograph_9858(),        # 願 U+9858
        g_cjk_unified_ideograph_985e(),        # 類 U+985E
        g_cjk_unified_ideograph_9867(),        # 顧 U+9867
        g_cjk_unified_ideograph_98e2(),        # 飢 U+98E2
        g_cjk_unified_ideograph_98fc(),        # 飼 U+98FC
        g_cjk_unified_ideograph_98fd(),        # 飽 U+98FD
        g_cjk_unified_ideograph_98fe(),        # 飾 U+98FE
        g_cjk_unified_ideograph_9905(),        # 餅 U+9905
        g_cjk_unified_ideograph_990a(),        # 養 U+990A
        g_cjk_unified_ideograph_990c(),        # 餌 U+990C
        g_cjk_unified_ideograph_9913(),        # 餓 U+9913
        g_cjk_unified_ideograph_9928(),        # 館 U+9928
        g_cjk_unified_ideograph_99d0(),        # 駐 U+99D0
        g_cjk_unified_ideograph_99d2(),        # 駒 U+99D2
        g_cjk_unified_ideograph_9a0e(),        # 騎 U+9A0E
        g_cjk_unified_ideograph_9a30(),        # 騰 U+9A30
        g_cjk_unified_ideograph_9a5a(),        # 驚 U+9A5A
        g_cjk_unified_ideograph_9ab8(),        # 骸 U+9AB8
        g_cjk_unified_ideograph_9b3c(),        # 鬼 U+9B3C
        g_cjk_unified_ideograph_9b42(),        # 魂 U+9B42
        g_cjk_unified_ideograph_9b45(),        # 魅 U+9B45
        g_cjk_unified_ideograph_9b54(),        # 魔 U+9B54
        g_cjk_unified_ideograph_9b5a(),        # 魚 U+9B5A
        g_cjk_unified_ideograph_9bae(),        # 鮮 U+9BAE
        g_cjk_unified_ideograph_9be8(),        # 鯨 U+9BE8
        g_cjk_unified_ideograph_9cf4(),        # 鳴 U+9CF4
        g_cjk_unified_ideograph_9db4(),        # 鶴 U+9DB4
        g_cjk_unified_ideograph_9e93(),        # 麓 U+9E93
        g_cjk_unified_ideograph_9e97(),        # 麗 U+9E97
        g_cjk_unified_ideograph_9ebb(),        # 麻 U+9EBB
        g_cjk_unified_ideograph_9f13(),        # 鼓 U+9F13
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-auto-joyo.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
