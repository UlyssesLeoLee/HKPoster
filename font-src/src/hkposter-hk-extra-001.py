"""HK Poster Heavy —— 繁体补字 lane（lane: hk-extra-001）。

字符清单（**不在 Jōyō 2136 内**的 zh-HK 繁体字）：
    之 U+4E4B / 擊 U+64CA / 霓 U+9713 / 黑 U+9ED1

为什么有这条 lane
----------------
样张的四字词组是「英雄本色 / 旺角風雲 / 霓虹之夜 / 黑夜追擊」
（`font-src/specimens/render_specimens.py` 的 FOUR_WORDS），
其中 **霓 / 黑 / 擊** 与 **之** 不在 Jōyō 2136 之内 ——
Jōyō 收的是日文形「撃 U+6483」「黒 U+9ED2」，
繁体形「擊 U+64CA」「黑 U+9ED1」是**独立码位**，必须另做。
不做这 4 个字，样张上就是 4 个方框。

方法（与 cjk-core / cjk-dense 同法）：先写笔画清单与部件分区坐标，
再逐笔画落坐标并注明所属部件。

**骨架照标准，不改笔画角度**：只做海报式端点与重量，
不改变任何一笔的走向（项目所有者 2026-10-25：「你可以改变笔画的设计，
但不要改变笔画的角度」）。

**坐标来自参照实测**（不是目视估计）：
Zen Kaku Gothic New Black（`E:/hkposter-refs/ZenKakuGothicNew-Black.ttf`，
SIL OFL 1.1）的轮廓横竖段实测值见各字 docstring，
换算到本字面框（x 60..940 / y 0..820）的比例写进代码。

**两条硬规矩（本 lane 踩过的坑）**：
1. **横画间距 ≥ 笔画宽 + 24**。相邻横画的墨一旦接上就是一条黑带，
   而 check_stroke_gaps 只在重叠 > 1.5 倍笔宽时才报「疑似粘连」——
   **门禁不报 ≠ 字能看**。密字（擊 17 画）的横画用 W_HAIR(76)，间距 100。
2. **部件不能想当然**。「擊」的下部是「手」= 顶撇 + 二横 + 竖钩，
   漏掉顶撇就画成了「王」。
   （第 8 版之前写「兒」比「臼」多一个右上「冂」—— 那是**误读**，
   已按 Klee One SemiBold U+9713/U+5150/U+81FC 实测推翻：
   兒 = 臼 + 儿，**没有**右上冂；雨 的四点也**不是小点**，
   是横卧短撇，约 176 宽 × 52 高。）

CJK 字面顶线 = 820（与 cjk-core 同一档）。
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
W_HAIR = 76

CJK_TOP = 820


def glyph_zhi() -> Glyph:
    """之 U+4E4B（3 画）。

    标准骨架：竖点（右上）+ 横撇（横起，右端折向左下）+ 捺（自左上向右下扫出）。
    之是「之字旁」的主形，简体/繁体同码位同形。

    参照实测（Zen Kaku Gothic New Black，U+4E4B，x 33..961 / y -74..833）：
        点：竖块 x 425..582，y 661..833（竖点，不是斜点）
        横：y=661 从 x=121 到 878（**占字宽 78%**）
        撇：从右端向左下落到 x=33（**落到最左**）
        捺：起笔 (170,300) 附近，向右下扫到 (961,-5)（**落到最右**）

    取舍：字形疏（3 画），用足笔画重量：主横与捺给 W_MAIN，点用 W_SEC。
    「之」与「又」的差别全在「点 + 长横 + 撇捺分头落地」这三处，
    横画短了或撇捺收在中间，字就读成「又」。
    """
    g = Glyph("uni4E4B", advance=1000, unicode=0x4E4B, note="之（繁体补字，zh-HK）")

    # ---- 竖点（右上，slant=0 竖点） ----
    g.dot(505, 750, w=96, h=120, slant=0)

    # ---- 横撇：横 y=600 从 x=120 到 880，右端折向左下撇到 (80, 40) ----
    g.hbar(120, 880, 600, weight=W_MAIN)
    g.diag(880, 600, 80, 40, weight=W_MAIN)

    # ---- 捺：起笔 (150, 400) —— 在撇的路径左侧 —— 扫向右下 (930, 20) ----
    g.diag(150, 400, 930, 20, weight=W_MAIN)

    return g


def glyph_ji() -> Glyph:
    """擊 U+64CA（17 画）：上「車 + 殳」+ 下「手」。

    繁体「擊」= 車（左）+ 殳（右）+ 手（下），三部分。

    标准骨架：
        上部左「車」：一（顶横）+ 日（中）+ 丨（贯通）+ 一（底横）
        上部右「殳」：几（横折弯 + 撇）+ 又（横撇 + 捺）
        下部「手」：**顶撇** + 二横 + 竖钩（带钩）

    **手的第一笔是顶撇** —— 漏了它，下部就成了「王」，整个字读不出来。
    顶撇的左端**落在上横上**（参照 Klee One：撇尾压着横，不是浮在上面）。

    横画间距：密字（17 画）的横画用 W_HAIR(76)，白口 ≥ 24。
    上下分区：上部（車+殳）y 334..820，下部（手）y 0..330。

    日的内白：日宽 340（x 90..430），中竖 76 厚 → 每格内白 85 / 95 单位。
    """
    g = Glyph("uni64CA", advance=1000, unicode=0x64CA, note="擊（繁体补字，zh-HK）")

    # ================= 上部左：車（x 60..450，y 334..820） =================
    g.hbar(60, 450, 778, weight=W_THIN)           # 車 顶横
    g.vbar(255, 778, 372, weight=W_HAIR)          # 車 中竖（穿日）
    # 日（x 90..430）：上横 672 / 中横 572 / 下横 472
    g.hbar(90, 430, 672, weight=W_HAIR)           # 日 上横
    g.vbar(90, 672, 472, weight=W_THIN)           # 日 左竖
    g.vbar(430, 672, 472, weight=W_THIN)          # 日 右竖
    g.hbar(90, 430, 572, weight=W_HAIR)           # 日 中横
    g.hbar(90, 430, 472, weight=W_HAIR)           # 日 下横
    g.hbar(60, 450, 372, weight=W_HAIR)           # 車 底横

    # ================= 上部右：殳（x 480..940，y 360..820） =================
    # 几：撇 + 横 + 折 + 弯钩（弯钩向右下再勾，不是向左下）
    g.diag(640, 790, 530, 610, weight=W_THIN)     # 几 的撇
    g.hbar(600, 870, 778, weight=W_THIN)          # 几 的横
    g.vbar(870, 778, 680, weight=W_THIN)          # 几 的折
    g.diag(870, 680, 930, 610, weight=W_THIN)     # 几 的弯钩
    # 又：横 + 横撇 + 捺（整体上提，让出下半部给「手」）
    g.hbar(500, 880, 505, weight=W_THIN)          # 又 的横
    g.diag(880, 505, 680, 430, weight=W_THIN)     # 又 的横撇
    g.diag(660, 505, 930, 390, weight=W_THIN)     # 又 的捺

    # ================= 下部：手（x 200..900，y 0..340） =================
    g.diag(660, 320, 480, 270, weight=W_THIN)     # 手 顶撇（第一笔！漏了就读成「王」）
    g.hbar(300, 820, 230, weight=W_SEC)           # 手 上横
    g.hbar(200, 900, 115, weight=W_SEC)           # 手 下横
    g.vbar(540, 340, 45, weight=W_MAIN)           # 手 竖钩
    g.diag(540, 45, 630, 90, weight=W_HAIR)       # 手 竖钩的钩

    return g


def glyph_ni() -> Glyph:
    """霓 U+9713（16 画）：上「雨」+ 下「兒」。

    标准骨架：雨 = 一（顶横）+ 冂（横折）+ 丨（中竖）+ 四点；
    兒 = 臼（丿 + 左竖 + 右竖 + 分半中横 + 底横）+ 儿（撇 + 竖弯钩）。

    参照实测（Klee One SemiBold，U+9713 / U+5150 / U+81FC，OFL 1.1）：
        雨：顶横贯通全宽；冂 上横在中竖处断开成两段；冂 无底横；
            **四点不是小点，是横卧短撇**（约 176 宽 × 52 高），两列各二。
        臼：左上角有一撇（丿）与左竖相接；中横**分成左右两半**，
            两半之间留缝；底横贯通。
        兒 = 臼 + 儿，**没有右上「冂」**（第 8 版之前的那个判断是误读，
        已按 Klee One 实测推翻 —— 多画一笔会让 霓 读成「臼+儿」的错形）。
    """
    g = Glyph("uni9713", advance=1000, unicode=0x9713, note="霓（繁体补字，zh-HK）")

    # ================= 上部：雨（x 60..940，y 460..820） =================
    g.hbar(60, 940, 778, weight=W_THIN)          # 雨 顶横
    g.vbar(500, 778, 480, weight=W_THIN)         # 雨 中竖（把顶横与冂上横各断成两段）
    g.hbar(90, 896, 672, weight=W_THIN)          # 雨 冂 上横
    g.vbar(90, 672, 470, weight=W_THIN)          # 雨 冂 左竖
    g.vbar(896, 672, 470, weight=W_THIN)         # 雨 冂 右竖
    # 雨 四点：横卧短撇（参照 176×52），两列各二，行距 33
    g.dot(245, 575, w=176, h=52, slant=14)       # 雨 点1（左上）
    g.dot(245, 490, w=176, h=52, slant=14)       # 雨 点2（左下）
    g.dot(700, 575, w=176, h=52, slant=14)       # 雨 点3（右上）
    g.dot(700, 490, w=176, h=52, slant=14)       # 雨 点4（右下）

    # ================= 下部：兒（x 86..940，y 0..480） =================
    # 臼：左上撇 + 左竖 + 右竖 + 中横分两半 + 底横贯通
    g.diag(250, 445, 150, 370, weight=W_THIN)    # 臼 左上撇（丿）
    g.vbar(170, 400, 240, weight=W_THIN)         # 臼 左竖
    g.vbar(560, 400, 200, weight=W_THIN)         # 臼 右竖
    g.hbar(170, 380, 310, weight=W_HAIR)         # 臼 中横 左半
    g.hbar(450, 560, 310, weight=W_HAIR)         # 臼 中横 右半（中缝 380..450）
    g.hbar(170, 560, 200, weight=W_HAIR)         # 臼 底横
    # 儿：撇（从臼的左下角起势）+ 竖弯钩（贴着臼的右侧落下）
    g.diag(185, 165, 80, 50, weight=W_THIN)       # 儿 撇（只擦到底横的左端，不穿臼）
    g.vbar(600, 210, 80, weight=W_SEC)           # 儿 竖
    g.hbar(600, 900, 80, weight=W_SEC)           # 儿 竖弯钩的底
    g.diag(900, 80, 940, 150, weight=W_THIN)     # 儿 竖弯钩的钩

    return g


def glyph_hei() -> Glyph:
    """黑 U+9ED1（12 画）：上「田」+ 中「三横」+ 下「灬」。

    标准骨架：黑 = 田 + 三横 + 灬 —— 田 的中竖贯通，其下**三道横**，再下面是灬四点。
    **不是「里」**（「里」的下部是「土」，「黑」的下部是灬）。

    参照实测（Zen Kaku Gothic New Black，U+9ED1，x 32..960 / y -95..823）：
        田：外框 x 149..851，y 256..713；中竖 x=428 贯通；内中横 y=530
        田下三横：y=422 (x 149..851)、y=283 (x 113..887)、y=140 (x 47..955)
        灬：四点，y -95..256

    **横画间距**：田 的三道横（790 / 620 / 450）间距 170；
    田下三横（350 / 240 / 130）间距 110；灬 的墨顶与最下一横留 24 白口。
    """
    g = Glyph("uni9ED1", advance=1000, unicode=0x9ED1, note="黑（繁体补字，zh-HK）")

    # ================= 上部：田（x 150..850，y 450..790） =================
    g.hbar(150, 850, 790, weight=W_THIN)         # 田 上横
    g.vbar(150, 790, 450, weight=W_THIN)         # 田 左竖
    g.vbar(850, 790, 450, weight=W_THIN)         # 田 右竖
    g.vbar(500, 790, 450, weight=W_THIN)         # 田 中竖（贯通）
    g.hbar(150, 850, 620, weight=W_THIN)         # 田 中横
    g.hbar(150, 850, 450, weight=W_THIN)         # 田 下横

    # ================= 中部：田下三横 =================
    g.hbar(150, 850, 350, weight=W_THIN)         # 横1
    g.hbar(110, 890, 240, weight=W_THIN)         # 横2
    g.hbar(60, 940, 130, weight=W_THIN)          # 横3

    # ================= 下部：灬（四点，y 0..90） =================
    g.dot(215, 45, w=84, h=90, slant=14)         # 灬 点1
    g.dot(415, 45, w=84, h=90, slant=14)         # 灬 点2
    g.dot(615, 45, w=84, h=90, slant=14)         # 灬 点3
    g.dot(815, 45, w=84, h=90, slant=14)         # 灬 点4

    return g


def build() -> list[Glyph]:
    return [glyph_zhi(), glyph_ji(), glyph_ni(), glyph_hei()]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-hk-extra-001.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
