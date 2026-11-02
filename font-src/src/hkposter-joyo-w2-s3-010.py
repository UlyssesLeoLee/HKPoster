"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s3-010。

本批 24 字，笔画范围 10–13，取自 2010 年文化厅《常用漢字表》。

整体取舍
--------
* 字面框 x 60..940、y 0..820，advance 1000（与繁体汉字完全同一档，便于中英日混排）。
* 笔画权重：主 96 / 次 92 / 细 84 / 点 84–96。笔画少的字（留 10、倍 10、帯 10）
  主笔走 96；笔画多且叠压的字（署 13、債 13、罪 13、源 13、継 13）在拥挤段落局部减重到 84。
* 同族部件在批内复用同一套坐标与笔画拆法（GLY-004）：亻 / 氵 / 阝 / 冖 / 宀
  各自共用一套辅助函数，只按字做位置与大小的光学校正，不改骨架走向。
* 端点：横竖撇捺一律平切硬边；点与短撇用斜切平行四边形。slant 档位按契约分档，
  不自造档位：竖点 0（亠 / 宀 / 冖 的垂点）、丶 −14、丿 +14、短撇 26（氵的上点）。
* 内白：横×横叠压的白口一律 ≥ 24 单位；口/日/目/田 型方框的框高 ≥ 2×笔画宽 + 24。
  本批所有方框都留了实打实的白腔，不靠目测。
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


# ---------------------------------------------------------------- 复用部件
def _ren(g: Glyph, y_top: float) -> None:
    """亻（左偏旁）：撇 + 竖。

    批内凡带亻的字（宿 / 倍 / 債 / 停）都调本函数，只改 y_top，
    保证撇的倾角与竖的位置逐字一致（GLY-004）。
    """
    g.diag(255, y_top, 135, y_top - 180, weight=W_MAIN)
    g.vbar(195, y_top - 95, 0, weight=W_MAIN)


def _sanzui(g: Glyph) -> None:
    """氵（左偏旁）：上点 + 中点 + 提，整字高。

    批内带氵的字（清 / 源）共用；dx 相对 base 的 hkposter-cjk-core 右移 20，
    使最左墨迹落在字面框 x60 之内。
    """
    g.dot(178, 700, w=94, h=126, slant=26)      # 上点（短撇，slant 26）
    g.dot(170, 468, w=94, h=126, slant=26)      # 中点（短撇，slant 26）
    g.diag(90, 140, 268, 308, weight=W_SEC)     # 提


def _fu(g: Glyph, y_top: float = 810) -> None:
    """阝（阜字旁）：竖 + 横 + 撇 + 弯。批内带阝的字（険 / 陸）共用。"""
    g.vbar(120, 0, y_top, weight=W_MAIN)                 # 竖
    g.hbar(120, 270, y_top - 40, weight=W_MAIN)          # 横（起笔）
    g.diag(270, y_top - 40, 155, y_top - 230, weight=W_THIN)   # 撇
    g.hbar(155, 270, y_top - 230, weight=W_SEC)           # 弯


def _gai(g: Glyph, x1: float, x2: float, y: float, weight: float = W_MAIN) -> None:
    """冖：横 + 右钩 + 左垂点。批内带冖的字（覚 / 停 / 帯）共用。"""
    g.hbar(x1, x2, y, weight=weight)
    g.diag(x2 - 10, y, x2 - 80, y - 90, weight=W_THIN)   # 右钩
    g.dot(x1 + 46, y - 46, w=76, h=96, slant=0)          # 左垂点（竖点）


def _mian(g: Glyph, y_bar: float = 700) -> None:
    """宀：竖点 + 横 + 右钩 + 左垂点。批内带宀的字（宿）共用。"""
    g.dot(500, 778, w=84, h=84, slant=0)                 # 竖点
    g.hbar(118, 882, y_bar, weight=W_SEC)                # 横
    g.diag(874, y_bar, 798, y_bar - 92, weight=W_THIN)   # 右钩
    g.dot(122, y_bar - 40, w=78, h=100, slant=0)         # 左垂点


def _ri(g: Glyph, x1: float, x2: float, y1: float, y2: float,
        y_mid: float, weight: float = W_MAIN) -> None:
    """日型方框（竖 + 横折 + 中横 + 下横）。

    框高 = y1 - y2 ≥ 2×笔画宽 + 24；两格白腔各 ≥ 24。
    批内带日框的字（宿的百 / 習の白 / 署の者 / 普 / 船の口 / 倍の口 / 許の口 /
    債の貝 / 留の田 / 散の月 / 筋の月）共用同一套「框高 ≥ 2w+24」约束。
    """
    g.vbar(x1, y1, y2, weight=weight)                   # 竖
    g.hbar(x1, x2, y1, weight=weight)                   # 上横（横折的横）
    g.vbar(x2, y1, y2, weight=weight)                   # 竖（横折的竖）
    g.hbar(x1, x2, y_mid, weight=weight)                # 中横
    g.hbar(x1, x2, y2, weight=weight)                   # 下横


def _yue(g: Glyph, x1: float, x2: float, y1: float, y2: float,
         y_mid1: float, weight: float = W_MAIN) -> None:
    """月型方框（撇 + 竖 + 横折 + 两根内横，底开口）。

    月 = 4 画：竖、横折钩、两根内横，故框内两格白腔 ≥ 24，底部不封口。
    """
    g.diag(x1 + 40, y1 + 100, x1 - 60, y1 - 20, weight=W_MAIN)   # 撇
    g.vbar(x1, y1, y2, weight=weight)                            # 竖
    g.hbar(x1, x2, y1, weight=weight)                            # 上横
    g.vbar(x2, y1, y2, weight=weight)                            # 竖
    g.hbar(x1, x2, y_mid1, weight=weight)                        # 内横 1
    g.hbar(x1, x2, y2, weight=weight)                            # 内横 2


# ---------------------------------------------------------------- 字形
def uni5BBF() -> Glyph:
    """宿 U+5BBF —— 宀 + 亻 + 百（11 画）。

    分区：宀 居顶（点 736..820 / 横 654..746）；左下 亻（撇 255→135，竖落基线）；
    右下 百（横 528..624 / 撇 / 日框 408..500、236..332、64..160）。
    白口：宀横↔百横 30，百横↔日上横 28，日内两格各 76。
    """
    g = Glyph("uni5BBF", advance=1000, unicode=0x5BBF, note="宿：宀+亻+百")
    _mian(g, y_bar=700)
    _ren(g, y_top=572)
    g.hbar(330, 900, 576, weight=W_MAIN)                  # 百的一
    g.diag(524, 576, 406, 460, weight=W_THIN)             # 百の撇
    g.vbar(410, 456, 108, weight=W_MAIN)                  # 日の竖
    g.hbar(410, 838, 456, weight=W_MAIN)                  # 日の横折（横）
    g.vbar(838, 456, 108, weight=W_MAIN)                  # 日の横折（竖）
    g.hbar(410, 838, 282, weight=W_MAIN)                  # 日の中横
    g.hbar(410, 838, 108, weight=W_MAIN)                  # 日の下横
    return g


def uni6E05() -> Glyph:
    """清 U+6E05 —— 氵 + 青（11 画）。

    分区：左氵（复用 _sanzui）；右青 = 龶（3 横 + 竖）+ 月（框 3 横、底开口）。
    青共 6 条横档：龶 736..820 / 626..712 / 516..600，月 398..482 / 258..342 / 118..202；
    相邻白口 26 / 26 / 26 / 56 / 56。
    """
    g = Glyph("uni6E05", advance=1000, unicode=0x6E05, note="清：氵+青")
    _sanzui(g)
    g.hbar(370, 930, 778, weight=W_THIN)                  # 青の一
    g.hbar(390, 910, 670, weight=W_THIN)                  # 青の二
    g.hbar(410, 890, 558, weight=W_THIN)                  # 青の三
    g.vbar(650, 778, 558, weight=W_MAIN)                  # 龶の竖
    g.hbar(420, 890, 440, weight=W_THIN)                  # 月の横折
    g.vbar(420, 440, 20, weight=W_MAIN)                   # 月の左竖
    g.vbar(890, 440, 20, weight=W_MAIN)                   # 月の右竖
    g.hbar(420, 890, 300, weight=W_THIN)                  # 月の内横 1
    g.hbar(420, 890, 160, weight=W_THIN)                  # 月の内横 2
    return g


def uni7FD2() -> Glyph:
    """習 U+7FD2 —— 羽 + 白（11 画）。

    分区：上羽 728..820，两半各「横折 + 点 + 提」；下白 = 撇 + 日框（框高 396）。
    白口：白框内两格各 76；羽↔白 100。
    """
    g = Glyph("uni7FD2", advance=1000, unicode=0x7FD2, note="習：羽+白")
    # 羽の左
    g.hbar(60, 420, 774, weight=W_SEC)                    # 横折（横）
    g.vbar(420, 774, 600, weight=W_SEC)                   # 横折（竖）
    g.diag(420, 600, 350, 558, weight=W_THIN)             # 钩
    g.dot(160, 690, w=76, h=84, slant=14)                 # 点（丿向，+14）
    g.diag(70, 590, 260, 650, weight=W_THIN)              # 提
    # 羽の右
    g.hbar(500, 860, 774, weight=W_SEC)
    g.vbar(860, 774, 600, weight=W_SEC)
    g.diag(860, 600, 790, 558, weight=W_THIN)
    g.dot(600, 690, w=76, h=84, slant=14)
    g.diag(510, 590, 700, 650, weight=W_THIN)
    # 白
    g.diag(330, 570, 250, 468, weight=W_MAIN)             # 白の撇
    g.vbar(270, 452, 108, weight=W_MAIN)                  # 竖
    g.hbar(270, 730, 452, weight=W_MAIN)                  # 横折（横）
    g.vbar(730, 452, 108, weight=W_MAIN)                  # 横折（竖）
    g.hbar(270, 730, 280, weight=W_MAIN)                  # 中横
    g.hbar(270, 730, 108, weight=W_MAIN)                  # 下横
    return g


def uni967A() -> Glyph:
    """険 U+967A —— 阝 + 㑒（11 画）。

    分区：左阝（复用 _fu）；右㑒 = 亼（撇捺 + 一 522..618）+ 夂（撇 + 横 404..496 + 横撇 + 捺）。
    """
    g = Glyph("uni967A", advance=1000, unicode=0x967A, note="険：阝+㑒")
    _fu(g, y_top=810)
    g.diag(590, 800, 390, 600, weight=W_MAIN)             # 亼の撇
    g.diag(590, 800, 830, 600, weight=W_MAIN)             # 亼の捺
    g.hbar(370, 890, 570, weight=W_MAIN)                  # 亼の一
    g.diag(430, 455, 320, 330, weight=W_THIN)             # 夂の撇
    g.hbar(400, 780, 450, weight=W_SEC)                   # 夂の横
    g.diag(780, 450, 520, 200, weight=W_SEC)              # 夂の横撇下行
    g.diag(430, 420, 820, 70, weight=W_MAIN)              # 夂の捺
    return g


def uni899A() -> Glyph:
    """覚 U+899A —— ⺍ + 冖 + 見（12 画）。

    分区：顶 ⺍（左点 −14 / 中竖点 0 / 右丿 +14）；冖 658..754；見 = 目（4 横 3 白腔）+ 儿。
    目四档：546..630 / 432..516 / 318..402 / 204..288；白口各 30。
    """
    g = Glyph("uni899A", advance=1000, unicode=0x899A, note="覚：ツ+冖+見")
    g.dot(290, 780, w=80, h=80, slant=-14)                # 左点（丶向）
    g.dot(500, 770, w=88, h=100, slant=0)                 # 中点（竖点）
    g.dot(710, 780, w=80, h=80, slant=14)                 # 右点（丿向）
    _gai(g, 70, 930, 706)
    g.vbar(370, 588, 246, weight=W_MAIN)                  # 目の左竖
    g.hbar(370, 830, 588, weight=W_THIN)                  # 目の一
    g.vbar(830, 588, 246, weight=W_MAIN)                  # 目の右竖
    g.hbar(370, 830, 474, weight=W_THIN)                  # 目の二
    g.hbar(370, 830, 360, weight=W_THIN)                  # 目の三
    g.hbar(370, 830, 246, weight=W_THIN)                  # 目の四
    g.diag(400, 240, 240, 20, weight=W_MAIN)              # 儿の撇
    g.vbar(780, 240, 70, weight=W_MAIN)                   # 儿の竖
    g.hbar(780, 920, 70, weight=W_SEC)                    # 儿の钩
    return g


def uni76DB() -> Glyph:
    """盛 U+76DB —— 成 + 皿（11 画）。

    分区：上成（横 672..768 / 长撇 / 横折 / 斜钩 / 内撇 / 点 slant 20）；
    下皿 0..330（4 竖 + 上下横，中部 3 个白腔）。
    """
    g = Glyph("uni76DB", advance=1000, unicode=0x76DB, note="盛：成+皿")
    g.hbar(140, 660, 720, weight=W_MAIN)                  # 成の一
    g.diag(210, 720, 100, 380, weight=W_MAIN)             # 成の撇
    g.hbar(210, 470, 600, weight=W_SEC)                   # 成の横折（横）
    g.vbar(470, 600, 440, weight=W_SEC)                   # 成の横折（竖）
    g.diag(620, 790, 880, 420, weight=W_MAIN)             # 成の斜钩
    g.diag(700, 560, 520, 330, weight=W_SEC)              # 成の内撇
    g.dot(870, 740, w=84, h=92, slant=20)                 # 成の点
    g.hbar(240, 790, 330, weight=W_MAIN)                  # 皿の一
    g.vbar(240, 330, 48, weight=W_MAIN)                   # 皿の左竖
    g.vbar(790, 330, 48, weight=W_MAIN)                   # 皿の右竖
    g.vbar(420, 330, 48, weight=W_THIN)                   # 皿の中竖 1
    g.vbar(610, 330, 48, weight=W_THIN)                   # 皿の中竖 2
    g.hbar(240, 790, 48, weight=W_MAIN)                   # 皿の下横
    return g


def uni8239() -> Glyph:
    """船 U+8239 —— 舟 + 㕣（11 画）。

    分区：左舟（撇 / 左撇 / 横折钩 / 两点 / 长横 352..448）；右㕣 = 八 + 口。
    """
    g = Glyph("uni8239", advance=1000, unicode=0x8239, note="船：舟+㕣")
    g.diag(300, 800, 180, 700, weight=W_MAIN)             # 舟の撇
    g.diag(240, 700, 150, 30, weight=W_MAIN)              # 舟の左竖
    g.hbar(160, 420, 700, weight=W_MAIN)                  # 舟の横折（横）
    g.vbar(420, 700, 120, weight=W_MAIN)                  # 舟の横折（竖）
    g.diag(420, 120, 350, 70, weight=W_THIN)              # 舟の钩
    g.dot(290, 560, w=76, h=88, slant=-14)                # 舟の上点（丶向）
    g.dot(290, 430, w=76, h=88, slant=-14)                # 舟の下点（丶向）
    g.hbar(60, 480, 400, weight=W_MAIN)                   # 舟の長横
    g.diag(640, 700, 540, 560, weight=W_MAIN)             # 㕣の丿
    g.diag(700, 700, 860, 560, weight=W_MAIN)             # 㕣の㇏
    g.hbar(560, 860, 420, weight=W_MAIN)                  # 口の横折（横）
    g.vbar(560, 420, 130, weight=W_MAIN)                  # 口の左竖
    g.vbar(860, 420, 130, weight=W_MAIN)                  # 口の右竖
    g.hbar(560, 860, 130, weight=W_MAIN)                  # 口の下横
    return g


def uni500D() -> Glyph:
    """倍 U+500D —— 亻 + 咅（10 画）。

    分区：左亻（复用 _ren）；右咅 = 立（竖点 + 二横 + 两点）+ 口。
    立三档横：652..748 / 544..636（两点）/ 432..528；口 312..408 / 52..148。
    白口：立の二↔口上横 24；口内白腔 164。
    """
    g = Glyph("uni500D", advance=1000, unicode=0x500D, note="倍：亻+咅")
    _ren(g, y_top=760)
    g.dot(640, 774, w=84, h=88, slant=0)                  # 立の竖点
    g.hbar(380, 900, 700, weight=W_MAIN)                  # 立の一
    g.dot(470, 590, w=80, h=92, slant=-14)                # 立の左点（丶向）
    g.dot(820, 590, w=80, h=92, slant=14)                 # 立の右点（丿向）
    g.hbar(360, 920, 480, weight=W_MAIN)                  # 立の二
    g.hbar(440, 850, 360, weight=W_MAIN)                  # 口の横折（横）
    g.vbar(440, 360, 100, weight=W_MAIN)                  # 口の左竖
    g.vbar(850, 360, 100, weight=W_MAIN)                  # 口の右竖
    g.hbar(440, 850, 100, weight=W_MAIN)                  # 口の下横
    return g


def uni8A31() -> Glyph:
    """許 U+8A31 —— 言 + 午（11 画）。

    分区：左言（竖点 + 三横 + 口）；右午（撇 + 二横 + 竖）。
    言四档横：652..748 / 536..624 / 420..508 / 292..388；口底 92..188。
    """
    g = Glyph("uni8A31", advance=1000, unicode=0x8A31, note="許：言+午")
    g.dot(245, 774, w=84, h=88, slant=0)                  # 言の竖点
    g.hbar(70, 420, 700, weight=W_MAIN)                   # 言の一
    g.hbar(100, 390, 580, weight=W_SEC)                   # 言の二
    g.hbar(130, 360, 460, weight=W_SEC)                   # 言の三
    g.hbar(140, 350, 340, weight=W_MAIN)                  # 口の横折（横）
    g.vbar(140, 340, 140, weight=W_MAIN)                  # 口の左竖
    g.vbar(350, 340, 140, weight=W_MAIN)                  # 口の右竖
    g.hbar(140, 350, 140, weight=W_MAIN)                  # 口の下横
    g.diag(620, 800, 540, 700, weight=W_MAIN)             # 午の撇
    g.hbar(500, 900, 660, weight=W_MAIN)                  # 午の一
    g.hbar(520, 880, 500, weight=W_MAIN)                  # 午の二
    g.vbar(700, 640, 0, weight=W_MAIN)                    # 午の竖
    return g


def uni7F72() -> Glyph:
    """署 U+7F72 —— 罒 + 者（13 画）。

    分区：上罒 604..820（4 竖 → 3 个白腔，高 24+）；下者 = 土 + 撇 + 日框。
    者四档横：492..588 / 372..468 / 262..358 / 142..238；日框底 22..118。
    """
    g = Glyph("uni7F72", advance=1000, unicode=0x7F72, note="署：罒+者")
    g.hbar(60, 940, 772, weight=W_MAIN)                   # 罒の一
    g.vbar(110, 772, 652, weight=W_MAIN)                  # 罒の左竖
    g.vbar(890, 772, 652, weight=W_MAIN)                  # 罒の右竖
    g.vbar(370, 772, 652, weight=W_THIN)                  # 罒の中竖 1
    g.vbar(630, 772, 652, weight=W_THIN)                  # 罒の中竖 2
    g.hbar(60, 940, 652, weight=W_MAIN)                   # 罒の下横
    g.hbar(200, 780, 540, weight=W_MAIN)                  # 者の一
    g.vbar(490, 580, 420, weight=W_MAIN)                  # 者の竖
    g.hbar(150, 830, 420, weight=W_MAIN)                  # 者の二
    g.diag(700, 560, 390, 350, weight=W_MAIN)             # 者の撇
    g.hbar(330, 800, 310, weight=W_MAIN)                  # 日の横折（横）
    g.vbar(330, 310, 70, weight=W_MAIN)                   # 日の左竖
    g.vbar(800, 310, 70, weight=W_MAIN)                   # 日の右竖
    g.hbar(330, 800, 190, weight=W_MAIN)                  # 日の中横
    g.hbar(330, 800, 70, weight=W_MAIN)                   # 日の下横
    return g


def uni50B5() -> Glyph:
    """債 U+50B5 —— 亻 + 責（13 画）。

    分区：左亻（复用 _ren）；右責 = 龶（3 横 + 竖）+ 貝（目型 4 横 + 八）。
    責共 7 档横：736..820 / 620..704 / 504..588 / 388..472 / 272..356 / 156..240 / 40..124，
    相邻白口均 32（≥24，且不封死任何白腔）。
    """
    g = Glyph("uni50B5", advance=1000, unicode=0x50B5, note="債：亻+責")
    _ren(g, y_top=760)
    g.hbar(380, 900, 778, weight=W_THIN)                  # 龶の一
    g.hbar(400, 880, 662, weight=W_THIN)                  # 龶の二
    g.hbar(420, 860, 546, weight=W_THIN)                  # 龶の三
    g.vbar(650, 778, 546, weight=W_MAIN)                  # 龶の竖
    g.vbar(390, 430, 82, weight=W_MAIN)                   # 貝の左竖
    g.hbar(390, 860, 430, weight=W_THIN)                  # 貝の一
    g.vbar(860, 430, 82, weight=W_MAIN)                   # 貝の右竖
    g.hbar(390, 860, 314, weight=W_THIN)                  # 貝の二
    g.hbar(390, 860, 198, weight=W_THIN)                  # 貝の三
    g.hbar(390, 860, 82, weight=W_THIN)                   # 貝の四
    g.diag(430, 130, 300, 20, weight=W_MAIN)              # 八の撇
    g.diag(820, 130, 910, 20, weight=W_MAIN)              # 八の捺
    return g


def uni7559() -> Glyph:
    """留 U+7559 —— 𠂎 + 刀 + 田（10 画）。

    分区：上左 撇 + 竖提；上右 撇 + 竖 + 刀（横折钩）；下田（框 + 中横 + 中竖，4 格）。
    """
    g = Glyph("uni7559", advance=1000, unicode=0x7559, note="留：卯部+田")
    g.diag(300, 800, 180, 700, weight=W_MAIN)             # 左の撇
    g.vbar(230, 700, 470, weight=W_MAIN)                  # 左の竖提（竖）
    g.diag(230, 470, 340, 530, weight=W_SEC)              # 左の竖提（提）
    g.diag(620, 800, 500, 690, weight=W_MAIN)             # 右の撇
    g.vbar(520, 690, 500, weight=W_MAIN)                  # 右の竖
    g.hbar(600, 880, 690, weight=W_MAIN)                  # 刀の横折（横）
    g.vbar(880, 690, 500, weight=W_MAIN)                  # 刀の横折（竖）
    g.diag(880, 500, 810, 450, weight=W_THIN)             # 刀の钩
    g.hbar(270, 790, 420, weight=W_MAIN)                  # 田の横折（横）
    g.vbar(270, 420, 60, weight=W_MAIN)                   # 田の左竖
    g.vbar(790, 420, 60, weight=W_MAIN)                   # 田の右竖
    g.hbar(270, 790, 240, weight=W_MAIN)                  # 田の中横
    g.hbar(270, 790, 60, weight=W_MAIN)                  # 田の下横
    g.vbar(530, 420, 60, weight=W_THIN)                   # 田の中竖
    return g


def uni7F6A() -> Glyph:
    """罪 U+7F6A —— 罒 + 非（13 画）。

    分区：上罒（复用 署 的罒 坐标：604..820）；下非 = 2 竖 + 左右各 3 横。
    非的横档：458..542 / 298..382 / 138..222；两竖间距 170（白 ≥ 60）。
    """
    g = Glyph("uni7F6A", advance=1000, unicode=0x7F6A, note="罪：罒+非")
    g.hbar(60, 940, 772, weight=W_MAIN)                   # 罒の一
    g.vbar(110, 772, 652, weight=W_MAIN)                  # 罒の左竖
    g.vbar(890, 772, 652, weight=W_MAIN)                  # 罒の右竖
    g.vbar(370, 772, 652, weight=W_THIN)                  # 罒の中竖 1
    g.vbar(630, 772, 652, weight=W_THIN)                  # 罒の中竖 2
    g.hbar(60, 940, 652, weight=W_MAIN)                   # 罒の下横
    g.vbar(430, 580, 40, weight=W_MAIN)                   # 非の左竖
    g.vbar(600, 580, 40, weight=W_MAIN)                   # 非の右竖
    g.hbar(120, 430, 500, weight=W_THIN)                  # 非の左上横
    g.hbar(120, 430, 340, weight=W_THIN)                  # 非の左中横
    g.hbar(120, 430, 180, weight=W_THIN)                  # 非の左下横
    g.hbar(600, 910, 500, weight=W_THIN)                  # 非の右上横
    g.hbar(600, 910, 340, weight=W_THIN)                  # 非の右中横
    g.hbar(600, 910, 180, weight=W_THIN)                  # 非の右下横
    return g


def uni505C() -> Glyph:
    """停 U+505C —— 亻 + 亭（11 画）。

    分区：左亻（复用 _ren）；右亭 = 亠（竖点 + 横）+ 口 + 冖 + 丁（横 + 竖钩）。
    亭五档横：654..746 / 524..616 / 394..486 / 274..366 / 134..226；口白腔 38。
    """
    g = Glyph("uni505C", advance=1000, unicode=0x505C, note="停：亻+亭")
    _ren(g, y_top=760)
    g.dot(640, 776, w=84, h=84, slant=0)                  # 亠の竖点
    g.hbar(380, 900, 700, weight=W_MAIN)                  # 亠の一
    g.hbar(500, 780, 570, weight=W_SEC)                   # 口の横折（横）
    g.vbar(500, 570, 440, weight=W_SEC)                   # 口の左竖
    g.vbar(780, 570, 440, weight=W_SEC)                   # 口の右竖
    g.hbar(500, 780, 440, weight=W_SEC)                   # 口の下横
    _gai(g, 360, 920, 320)
    g.hbar(380, 900, 180, weight=W_MAIN)                  # 丁の一
    g.vbar(640, 180, 40, weight=W_MAIN)                   # 丁の竖
    g.hbar(570, 640, 40, weight=W_THIN)                   # 丁の钩
    return g


def uni9678() -> Glyph:
    """陸 U+9678 —— 阝 + 坴（11 画）。

    分区：左阝（复用 _fu）；右坴 = 上土（横竖横）+ 八 + 下土（横竖横）。
    四档横：692..788 / 554..646 / 334..426 / 194..286。
    """
    g = Glyph("uni9678", advance=1000, unicode=0x9678, note="陸：阝+坴")
    _fu(g, y_top=810)
    g.hbar(400, 880, 740, weight=W_SEC)                   # 上土の一
    g.vbar(640, 740, 600, weight=W_MAIN)                  # 上土の竖
    g.hbar(400, 880, 600, weight=W_SEC)                   # 上土の二
    g.diag(480, 560, 370, 420, weight=W_SEC)              # 八の撇
    g.diag(800, 560, 910, 420, weight=W_SEC)              # 八の捺
    g.hbar(340, 940, 380, weight=W_SEC)                   # 下土の一
    g.vbar(640, 380, 240, weight=W_MAIN)                  # 下土の竖
    g.hbar(340, 940, 240, weight=W_SEC)                   # 下土の二
    return g


def uni6E90() -> Glyph:
    """源 U+6E90 —— 氵 + 原（13 画）。

    分区：左氵（复用 _sanzui）；右原 = 厂（横 + 长撇）+ 白（撇 + 日框）+ 小。
    白三档横：552..648 / 432..528 / 312..408；小在白之下（竖钩 + 左丿 + 右丶）。
    """
    g = Glyph("uni6E90", advance=1000, unicode=0x6E90, note="源：氵+原")
    _sanzui(g)
    g.hbar(400, 930, 772, weight=W_MAIN)                  # 厂の一
    g.diag(430, 760, 350, 60, weight=W_MAIN)              # 厂の撇
    g.diag(560, 700, 490, 620, weight=W_MAIN)             # 白の撇
    g.vbar(500, 600, 360, weight=W_MAIN)                  # 日の左竖
    g.hbar(500, 800, 600, weight=W_MAIN)                  # 日の横折（横）
    g.vbar(800, 600, 360, weight=W_MAIN)                  # 日の右竖
    g.hbar(500, 800, 480, weight=W_MAIN)                  # 日の中横
    g.hbar(500, 800, 360, weight=W_MAIN)                  # 日の下横
    g.vbar(650, 340, 60, weight=W_MAIN)                   # 小の竖
    g.hbar(570, 650, 60, weight=W_THIN)                   # 小の钩
    g.dot(480, 220, w=80, h=96, slant=14)                 # 小の左点（丿向）
    g.dot(820, 220, w=80, h=96, slant=-14)                # 小の右点（丶向）
    return g


def uni5275() -> Glyph:
    """創 U+5275 —— 倉 + 刂（12 画）。

    分区：左倉 = 人（撇捺）+ 亼の一 + 戸（一 + 撇 + 横折 + 一）+ 口；
    右刂 = 短竖 + 长竖钩。
    倉六档横：596..680 / 488..572 / 380..464 / 272..356 / 164..248 / 18..102。
    """
    g = Glyph("uni5275", advance=1000, unicode=0x5275, note="創：倉+刂")
    g.diag(380, 820, 110, 680, weight=W_MAIN)             # 人の撇
    g.diag(380, 820, 660, 680, weight=W_MAIN)             # 人の捺
    g.hbar(150, 620, 638, weight=W_THIN)                  # 亼の一
    g.hbar(200, 600, 530, weight=W_THIN)                  # 戸の一
    g.diag(250, 530, 170, 330, weight=W_MAIN)             # 戸の撇
    g.hbar(230, 600, 422, weight=W_THIN)                  # 戸の横折（横）
    g.vbar(600, 422, 314, weight=W_SEC)                   # 戸の横折（竖）
    g.hbar(230, 600, 314, weight=W_THIN)                  # 戸の二
    g.hbar(320, 670, 206, weight=W_THIN)                  # 口の横折（横）
    g.vbar(340, 206, 60, weight=W_SEC)                    # 口の左竖
    g.vbar(650, 206, 60, weight=W_SEC)                    # 口の右竖
    g.hbar(320, 670, 60, weight=W_THIN)                   # 口の下横
    g.vbar(770, 600, 380, weight=W_MAIN)                  # 刂の短竖
    g.vbar(890, 660, 60, weight=W_MAIN)                   # 刂の長竖
    g.hbar(820, 890, 60, weight=W_THIN)                   # 刂の钩
    return g


def uni7D99() -> Glyph:
    """継 U+7D99 —— 糸 + 米 + 乚（13 画）。

    分区：左糸 = 幺（2 撇折）+ 点 + 小（竖钩 + 左丿 + 右丶）；
    右米 = 丷（左丶 −14 / 右丿 +14）+ 横 + 竖 + 撇 + 捺；底 乚（横 + 上钩）。
    """
    g = Glyph("uni7D99", advance=1000, unicode=0x7D99, note="継：糸+米")
    g.diag(300, 810, 200, 720, weight=W_MAIN)             # 幺の撇折 1（撇）
    g.hbar(200, 330, 720, weight=W_THIN)                  # 幺の撇折 1（折）
    g.diag(360, 790, 250, 640, weight=W_MAIN)             # 幺の撇折 2（撇）
    g.hbar(250, 390, 600, weight=W_THIN)                  # 幺の撇折 2（折）
    g.dot(390, 500, w=76, h=88, slant=-14)                # 糸の点
    g.vbar(230, 620, 60, weight=W_MAIN)                   # 小の竖
    g.hbar(170, 230, 60, weight=W_THIN)                   # 小の钩
    g.dot(120, 300, w=76, h=88, slant=14)                 # 小の左点（丿向）
    g.dot(360, 300, w=76, h=88, slant=-14)                # 小の右点（丶向）
    g.dot(520, 760, w=80, h=90, slant=-14)                # 米の左点（丶向）
    g.dot(880, 760, w=80, h=90, slant=14)                 # 米の右点（丿向）
    g.hbar(490, 900, 640, weight=W_MAIN)                  # 米の一
    g.vbar(690, 800, 120, weight=W_MAIN)                  # 米の竖
    g.diag(560, 560, 480, 320, weight=W_SEC)              # 米の撇
    g.diag(800, 560, 900, 330, weight=W_MAIN)             # 米の捺
    g.hbar(460, 890, 60, weight=W_MAIN)                   # 乚の一
    g.vbar(890, 60, 160, weight=W_THIN)                   # 乚の钩
    return g


def uni7B4B() -> Glyph:
    """筋 U+7B4B —— 竹 + 月 + 力（12 画）。

    分区：顶竹（两组 撇 + 横 + 竖点，两横同高连成宽带 652..748）；
    左下月（框 3 横、底开口）；右下力（横折钩 + 撇）。
    """
    g = Glyph("uni7B4B", advance=1000, unicode=0x7B4B, note="筋：竹+月+力")
    g.diag(200, 810, 90, 700, weight=W_MAIN)              # 竹の撇（左）
    g.hbar(140, 400, 700, weight=W_MAIN)                  # 竹の一（左）
    g.dot(330, 640, w=76, h=96, slant=0)                  # 竹の竖点（左）
    g.diag(680, 810, 570, 700, weight=W_MAIN)             # 竹の撇（右）
    g.hbar(620, 880, 700, weight=W_MAIN)                  # 竹の一（右）
    g.dot(810, 640, w=76, h=96, slant=0)                  # 竹の竖点（右）
    g.diag(250, 560, 160, 440, weight=W_MAIN)             # 月の撇
    g.vbar(200, 460, 100, weight=W_MAIN)                  # 月の竖
    g.hbar(200, 440, 460, weight=W_MAIN)                  # 月の一
    g.vbar(440, 460, 100, weight=W_MAIN)                  # 月の竖
    g.hbar(200, 440, 300, weight=W_MAIN)                  # 月の内横 1
    g.hbar(200, 440, 140, weight=W_MAIN)                  # 月の内横 2
    g.hbar(520, 900, 480, weight=W_MAIN)                  # 力の横折（横）
    g.vbar(900, 480, 100, weight=W_MAIN)                  # 力の横折（竖）
    g.diag(900, 100, 820, 60, weight=W_THIN)              # 力の钩
    g.diag(700, 480, 560, 60, weight=W_MAIN)              # 力の撇
    return g


def uni5E2F() -> Glyph:
    """帯 U+5E2F —— 卅形 + 冖 + 巾（10 画）。

    分区：顶 3 竖（820..600）穿一横 644..740，竖出头即卅的 3 竖；
    冖 508..604；巾 382..478 + 中竖落基线。
    """
    g = Glyph("uni5E2F", advance=1000, unicode=0x5E2F, note="帯：卅+冖+巾")
    g.vbar(210, 820, 600, weight=W_MAIN)                  # 卅の竖 1
    g.vbar(500, 820, 600, weight=W_MAIN)                  # 卅の竖 2
    g.vbar(790, 820, 600, weight=W_MAIN)                  # 卅の竖 3
    g.hbar(60, 940, 692, weight=W_MAIN)                   # 卅の一
    _gai(g, 60, 940, 556)
    g.hbar(280, 660, 430, weight=W_MAIN)                  # 巾の横折（横）
    g.vbar(280, 430, 120, weight=W_MAIN)                  # 巾の左竖
    g.vbar(660, 430, 120, weight=W_MAIN)                  # 巾の右竖
    g.diag(660, 120, 590, 70, weight=W_THIN)              # 巾の钩
    g.vbar(470, 430, 0, weight=W_MAIN)                    # 巾の中竖
    return g


def uni846C() -> Glyph:
    """葬 U+846C —— 艹 + 死 + 廾（12 画）。

    分区：顶艹（横 712..808 + 两竖出头至 820）；中死 = 歹（一 + 撇 + 横折 + 点）+ 匕；
    底廾（一 + 撇 + 竖）。
    """
    g = Glyph("uni846C", advance=1000, unicode=0x846C, note="葬：艹+死+廾")
    g.hbar(120, 880, 760, weight=W_MAIN)                  # 艹の一
    g.vbar(300, 820, 712, weight=W_MAIN)                  # 艹の竖 1
    g.vbar(700, 820, 712, weight=W_MAIN)                  # 艹の竖 2
    g.hbar(160, 760, 640, weight=W_MAIN)                  # 歹の一
    g.diag(400, 640, 180, 420, weight=W_MAIN)             # 歹の撇
    g.hbar(300, 620, 520, weight=W_SEC)                   # 歹の横折（横）
    g.vbar(620, 520, 380, weight=W_SEC)                   # 歹の横折（竖）
    g.dot(400, 400, w=76, h=88, slant=-14)                # 歹の点
    g.diag(800, 640, 650, 520, weight=W_THIN)             # 匕の撇
    g.vbar(680, 640, 360, weight=W_SEC)                   # 匕の竖弯钩（竖）
    g.hbar(680, 900, 360, weight=W_MAIN)                  # 匕の竖弯钩（横）
    g.hbar(140, 900, 240, weight=W_MAIN)                  # 廾の一
    g.diag(360, 280, 240, 20, weight=W_MAIN)              # 廾の撇
    g.vbar(760, 280, 20, weight=W_MAIN)                   # 廾の竖
    return g


def uni666E() -> Glyph:
    """普 U+666E —— 並 + 日（12 画）。

    分区：顶丷（左丶 −14 / 右丿 +14）；並 = 一 + 2 竖 + 2 内点 + 一；
    底日（框 3 横、2 白腔）。
    並两横：658..742 / 448..532；日三横：338..422 / 208..292 / 78..162。
    """
    g = Glyph("uni666E", advance=1000, unicode=0x666E, note="普：並+日")
    g.dot(300, 780, w=80, h=80, slant=-14)                # 丷の左点（丶向）
    g.dot(660, 780, w=80, h=80, slant=14)                 # 丷の右点（丿向）
    g.hbar(60, 940, 700, weight=W_THIN)                   # 並の一
    g.vbar(330, 658, 532, weight=W_THIN)                  # 並の竖 1
    g.vbar(670, 658, 532, weight=W_THIN)                  # 並の竖 2
    g.dot(160, 600, w=76, h=88, slant=-14)                # 並の左点（丶向）
    g.dot(840, 600, w=76, h=88, slant=14)                 # 並の右点（丿向）
    g.hbar(60, 940, 490, weight=W_THIN)                   # 並の二
    g.vbar(360, 380, 120, weight=W_SEC)                   # 日の左竖
    g.hbar(360, 840, 380, weight=W_THIN)                  # 日の横折（横）
    g.vbar(840, 380, 120, weight=W_SEC)                   # 日の右竖
    g.hbar(360, 840, 250, weight=W_THIN)                  # 日の中横
    g.hbar(360, 840, 120, weight=W_THIN)                  # 日の下横
    return g


def uni6563() -> Glyph:
    """散 U+6563 —— 龷 + 月 + 攵（12 画）。

    分区：左龷 = 廿（横 + 2 竖出头）+ 一（竖穿两横，中间留 1 个白腔）；
    左下月（框 3 横、底开口）；右攵（撇 + 横 + 撇 + 捺）。
    """
    g = Glyph("uni6563", advance=1000, unicode=0x6563, note="散：龷+月+攵")
    g.vbar(230, 820, 608, weight=W_MAIN)                  # 廿の竖 1
    g.vbar(410, 820, 608, weight=W_MAIN)                  # 廿の竖 2
    g.hbar(80, 540, 700, weight=W_MAIN)                   # 廿の一
    g.hbar(60, 560, 560, weight=W_MAIN)                   # 龷の二
    g.diag(220, 500, 130, 380, weight=W_MAIN)             # 月の撇
    g.vbar(170, 420, 60, weight=W_MAIN)                   # 月の竖
    g.hbar(170, 500, 420, weight=W_MAIN)                  # 月の一
    g.vbar(500, 420, 60, weight=W_MAIN)                   # 月の竖
    g.hbar(170, 500, 270, weight=W_MAIN)                  # 月の内横 1
    g.hbar(170, 500, 120, weight=W_MAIN)                  # 月の内横 2
    g.diag(780, 800, 640, 700, weight=W_MAIN)             # 攵の撇
    g.hbar(600, 900, 660, weight=W_MAIN)                  # 攵の一
    g.diag(700, 660, 600, 300, weight=W_MAIN)             # 攵の撇
    g.diag(620, 600, 900, 120, weight=W_MAIN)             # 攵の捺
    return g


def uni5EB7() -> Glyph:
    """康 U+5EB7 —— 广 + 隶（11 画）。

    分区：顶广（竖点 + 横 + 长撇）；内隶 = ヨ（横折 + 2 横）+ 水（竖亅 + 撇 + 捺 + 点）。
    隶三档横：522..618 / 402..498 / 282..378。
    """
    g = Glyph("uni5EB7", advance=1000, unicode=0x5EB7, note="康：广+隶")
    g.dot(500, 776, w=84, h=84, slant=0)                  # 广の竖点
    g.hbar(120, 900, 700, weight=W_MAIN)                  # 广の一
    g.diag(200, 700, 120, 60, weight=W_MAIN)              # 广の撇
    g.hbar(330, 820, 570, weight=W_MAIN)                  # ヨの横折（横）
    g.vbar(820, 570, 330, weight=W_MAIN)                  # ヨの横折（竖）
    g.hbar(330, 820, 450, weight=W_MAIN)                  # ヨの一
    g.hbar(330, 820, 330, weight=W_MAIN)                  # ヨの二
    g.vbar(570, 350, 40, weight=W_MAIN)                   # 水の竖
    g.hbar(500, 570, 40, weight=W_THIN)                   # 水の钩
    g.diag(430, 300, 300, 90, weight=W_SEC)               # 水の撇
    g.diag(700, 300, 860, 100, weight=W_MAIN)             # 水の捺
    g.dot(390, 210, w=76, h=88, slant=-14)                # 水の点
    return g


def build() -> list[Glyph]:
    """按字符清单顺序返回本批 24 个字形（清单冻结，不增不删不改码位）。"""
    return [
        uni5BBF(),   # 宿 U+5BBF
        uni6E05(),   # 清 U+6E05
        uni7FD2(),   # 習 U+7FD2
        uni967A(),   # 険 U+967A
        uni899A(),   # 覚 U+899A
        uni76DB(),   # 盛 U+76DB
        uni8239(),   # 船 U+8239
        uni500D(),   # 倍 U+500D
        uni8A31(),   # 許 U+8A31
        uni7F72(),   # 署 U+7F72
        uni50B5(),   # 債 U+50B5
        uni7559(),   # 留 U+7559
        uni7F6A(),   # 罪 U+7F6A
        uni505C(),   # 停 U+505C
        uni9678(),   # 陸 U+9678
        uni6E90(),   # 源 U+6E90
        uni5275(),   # 創 U+5275
        uni7D99(),   # 継 U+7D99
        uni7B4B(),   # 筋 U+7B4B
        uni5E2F(),   # 帯 U+5E2F
        uni846C(),   # 葬 U+846C
        uni666E(),   # 普 U+666E
        uni6563(),   # 散 U+6563
        uni5EB7(),   # 康 U+5EB7
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s3-010.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
