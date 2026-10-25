"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-017。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
* 字面框 x 60..940、y 0..820，advance 1000（与繁体汉字同档，便于中英日混排）。
* 笔画权重档：主 96 / 次 92 / 细 84 / 点 84–96。本批 6–9 画，主体笔画一律用 96；
  只有在密排处（日的三横、亭的口、皿的竖）把局部降到 84，
  以保住内白（密排处 ≥ 24 单位）。
* 对齐语义：**墨迹**对齐，不是中心线对齐。
  横画要上缘到 820 → 中心线 772；要下缘到 0 → 中心线 48；
  竖画要左缘到 60 → 中心线 108；要右缘到 940 → 中心线 892。
  本文件的所有坐标都写成**字面量**（检查器靠 AST 取坐标），
  每个字形函数前的 docstring 写明笔画清单与部件分区。
* 海报端点：横竖撇捺一律**平切硬边**；点与短撇用**斜切平行四边形**（g.dot 的 slant）。
  斜切档只用工程既有档：0（竖点）/ 26（短撇）/ 14 / −14。
  斜切只出现在点/短撇/记号上，主笔不斜切（GLY-003）。
* 笔画角度一律照标准骨架，不改方向；只调重量、端点、转角与落位。
* 同族部件在批内**复用同一套坐标**（GLY-004）：
  亻 / 氵 / 木 / 卜 / 口 / 殳 / 几 在本批内坐标完全一致，
  只在「落在哪一侧」时做光学校正。

部件分区约定
------------
* 左偏旁（亻 彳 氵 木 忄 丬 口 疒 女 走 弓）占 x 60..~480。
* 右部件占 x ~500..940，竖与竖之间留 ≥ 60 单位。
* 撇/捺的倾斜角控制在 **≥ 30°（离水平）** 以上：斜画与横画交叠的
  「等效重叠长度」≈ 1/sin(θ)，θ<19° 会被 check_stroke_gaps 判为疑似粘连。
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


# ---------------------------------------------------------------- 部件：亻
def ren(g: Glyph) -> None:
    """亻（批内通用）：x 60..~340。

    撇 diag(295,800)->(135,490)：离垂直 28.3°，不与任何横画浅角交叠。
    竖 vbar(190, 560..0)：墨迹 x 142..238，与撇在 y 560..500 处相接。
    """
    g.diag(295, 800, 135, 490, weight=W_MAIN)
    g.vbar(190, 560, 0, weight=W_MAIN)


# ---------------------------------------------------------------- 部件：氵
def shui(g: Glyph) -> None:
    """氵（批内通用）：x 62..~233。

    上点/中点用短撇档 slant=26；提为上升斜画（42.5°）。
    """
    g.dot(160, 700, 94, 126, 26)
    g.dot(125, 520, 94, 126, 26)
    g.diag(95, 135, 200, 240, weight=W_MAIN)


# ---------------------------------------------------------------- 部件：木
def mu(g: Glyph) -> None:
    """木（批内通用）：x 90..~490。

    横 660；竖 820..0；撇捺自横画中线分出，成窄 Λ。
    """
    g.hbar(90, 460, 660, weight=W_MAIN)
    g.vbar(275, 820, 0, weight=W_MAIN)
    g.diag(270, 660, 95, 120, weight=W_MAIN)
    g.diag(280, 650, 455, 110, weight=W_MAIN)


# ---------------------------------------------------------------- 部件：卜
def bu(g: Glyph) -> None:
    """卜（批内通用）：竖 x 640（墨迹 592..688）+ 右下点 slant=-14。"""
    g.vbar(640, 820, 0, weight=W_MAIN)
    g.dot(790, 620, 94, 126, -14)


# ---------------------------------------------------------------- 部件：口
def kou(g: Glyph, x1: float, x2: float, y_bot: float, y_top: float,
        weight: float = W_MAIN) -> None:
    """口（批内通用）：左竖贴 x1、右竖贴 x2，横画上下缘对齐 y_top / y_bot。"""
    half = weight / 2.0
    g.hbar(x1, x2, y_top - half, weight=weight)
    g.hbar(x1, x2, y_bot + half, weight=weight)
    g.vbar(x1 + half, y_top, y_bot, weight=weight)
    g.vbar(x2 - half, y_top, y_bot, weight=weight)


# ---------------------------------------------------------------- 部件：殳
def shu(g: Glyph, x: float, y_top: float, y_mid: float, y_bot: float,
        half_w: float) -> None:
    """殳（批内通用，x 为左缘）：上 几（撇 + 横折弯钩）+ 下 又（横撇 + 捺）。"""
    g.diag(x + 150, y_top, x + 45, y_top - 180, weight=W_MAIN)
    g.hbar(x + 120, x + 360, y_top, weight=W_MAIN)
    g.vbar(x + 312, y_top, y_top - 200, weight=W_MAIN)
    g.hbar(x + 312, x + 380, y_top - 214, weight=56)
    g.hbar(x + 30, x + 370, y_mid, weight=W_MAIN)
    g.diag(x + 370, y_mid, x + 150, y_bot, weight=W_MAIN)
    g.diag(x + 50, y_mid, x + 380, y_bot - 60, weight=W_MAIN)


# ---------------------------------------------------------------- 部件：几
def ji(g: Glyph, x: float, y_top: float, y_bot: float) -> None:
    """几（批内通用，x 为左缘）：撇 + 横折弯钩（钩向右）。"""
    g.diag(x + 60, y_top - 30, x - 10, y_top - 200, weight=W_MAIN)
    g.hbar(x + 40, x + 310, y_top, weight=W_MAIN)
    g.vbar(x + 262, y_top, y_bot, weight=W_MAIN)
    g.hbar(x + 262, x + 380, y_bot - 14, weight=56)


def build() -> list[Glyph]:
    """本批 32 字。顺序同规格清单。"""
    glyphs: list[Glyph] = []

    # ---------------------------------------------------------- 呈 U+5448
    # ⿱口王。口 x 300..700 / y 500..820；王 y 0..460（三横 + 竖）。
    # 口内白 x 396..604、y 596..500 之间（口高 320 → 内白 128）。
    # 王三横中心线 412 / 230 / 48，横间空隙 86（远高于 24 下限）。
    g = Glyph("uni5448", advance=1000, unicode=0x5448, note="呈：口 + 王")
    g.hbar(300, 700, 772, weight=W_MAIN)      # 口·上横（墨迹 724..820）
    g.hbar(300, 700, 548, weight=W_MAIN)      # 口·下横（墨迹 500..596）
    g.vbar(348, 820, 500, weight=W_MAIN)      # 口·左竖（墨迹 300..396）
    g.vbar(652, 820, 500, weight=W_MAIN)      # 口·右竖（墨迹 604..700）
    g.hbar(110, 890, 412, weight=W_MAIN)      # 王·上横（墨迹 364..460）
    g.hbar(170, 830, 230, weight=W_MAIN)      # 王·中横（墨迹 182..278）
    g.hbar(140, 860, 48, weight=W_MAIN)       # 王·下横（墨迹 0..96）
    g.vbar(500, 412, 0, weight=W_MAIN)        # 王·竖
    glyphs.append(g)

    # ---------------------------------------------------------- 仰 U+4EF0
    # ⿰亻卬。卬 = 短撇（部件左上）+ 卩（左竖 + 横折 + 钩）。
    # 卩的横折横画 530..890（墨迹 724..820），右竖 842 到 420，钩向左。
    g = Glyph("uni4EF0", advance=1000, unicode=0x4EF0, note="仰：亻 + 卬")
    ren(g)
    g.diag(525, 795, 445, 655, weight=W_MAIN)   # 卬·短撇（右上落左）
    g.vbar(530, 790, 0, weight=W_MAIN)           # 卩·左竖（墨迹 482..578）
    g.hbar(530, 890, 772, weight=W_MAIN)         # 卩·横
    g.vbar(842, 772, 490, weight=W_MAIN)         # 卩·折（竖）
    g.hbar(734, 810, 476, weight=56)             # 卩·钩（向左）
    glyphs.append(g)

    # ---------------------------------------------------------- 征 U+5F81
    # ⿰彳正。彳两撇用**竖向错开**而非平行横移，避免 96 笔画宽把两撇压成一团。
    # 正 = 顶横 + 中竖 + 右中横 + 左短竖 + 底横。
    g = Glyph("uni5F81", advance=1000, unicode=0x5F81, note="征：彳 + 正")
    g.diag(325, 800, 265, 710, weight=W_MAIN)   # 彳·上撇（短）
    g.diag(250, 610, 140, 435, weight=W_MAIN)   # 彳·下撇
    g.vbar(165, 560, 0, weight=W_MAIN)           # 彳·竖
    g.hbar(430, 940, 772, weight=W_MAIN)         # 正·顶横
    g.vbar(690, 772, 180, weight=W_MAIN)         # 正·中竖
    g.hbar(738, 880, 460, weight=W_MAIN)         # 正·右中横（贴竖右缘）
    g.vbar(510, 400, 180, weight=W_MAIN)         # 正·左短竖
    g.hbar(430, 940, 180, weight=W_MAIN)         # 正·底横
    glyphs.append(g)

    # ---------------------------------------------------------- 砕 U+7815
    # ⿰石夬。石：一 + 丿 + 口（口 x 180..440 / y 250..500）。
    # 夬：乛（横 + 右折）+ 一 + 撇 + 捺。
    g = Glyph("uni7815", advance=1000, unicode=0x7815, note="砕：石 + 夬")
    g.hbar(60, 460, 772, weight=W_MAIN)          # 石·一（墨迹 724..820）
    g.diag(200, 772, 105, 340, weight=W_MAIN)    # 石·丿
    g.hbar(220, 460, 500, weight=W_THIN)         # 石·口·上横（墨迹 458..542）
    g.hbar(220, 460, 298, weight=W_THIN)         # 石·口·下横（墨迹 256..340）
    g.vbar(262, 500, 298, weight=W_THIN)         # 石·口·左竖（墨迹 220..304）
    g.vbar(418, 500, 298, weight=W_THIN)         # 石·口·右竖（墨迹 376..460）
    g.hbar(520, 900, 772, weight=W_MAIN)         # 夬·乛（横）
    g.vbar(852, 772, 560, weight=W_MAIN)         # 夬·乛（折）
    g.hbar(500, 900, 560, weight=W_MAIN)         # 夬·一
    g.diag(700, 772, 540, 200, weight=W_MAIN)    # 夬·撇
    g.diag(660, 560, 930, 120, weight=W_MAIN)    # 夬·捺
    glyphs.append(g)

    # ---------------------------------------------------------- 后 U+540E
    # ⿸厂⿱一口：丿（厂）+ 一（厂）+ 一 + 口（口 x 330..870 / y 60..470）。
    g = Glyph("uni540E", advance=1000, unicode=0x540E, note="后：厂 + 一 + 口")
    g.diag(255, 800, 140, 680, weight=W_MAIN)    # 厂·丿
    g.hbar(200, 940, 772, weight=W_MAIN)         # 厂·一（墨迹 724..820）
    g.hbar(240, 900, 620, weight=W_MAIN)         # 一（墨迹 572..668）
    g.hbar(330, 870, 470, weight=W_MAIN)         # 口·上横（墨迹 422..518）
    g.hbar(330, 870, 108, weight=W_MAIN)         # 口·下横（墨迹 60..156）
    g.vbar(378, 470, 108, weight=W_MAIN)         # 口·左竖（墨迹 330..426）
    g.vbar(822, 470, 108, weight=W_MAIN)         # 口·右竖（墨迹 774..870）
    glyphs.append(g)

    # ---------------------------------------------------------- 泥 U+6CE5
    # ⿰氵尼。尼 = 尸（横折 + 横 + 撇）+ 匕（撇 + 竖弯）。
    g = Glyph("uni6CE5", advance=1000, unicode=0x6CE5, note="泥：氵 + 尼")
    shui(g)
    g.hbar(520, 900, 772, weight=W_MAIN)         # 尸·横折（横）
    g.vbar(852, 772, 430, weight=W_MAIN)         # 尸·横折（折）
    g.hbar(460, 852, 430, weight=W_MAIN)         # 尸·横（墨迹 382..478）
    g.diag(520, 772, 430, 60, weight=W_MAIN)     # 尸·撇
    g.diag(760, 330, 600, 120, weight=W_MAIN)    # 匕·撇
    g.vbar(800, 330, 40, weight=W_MAIN)          # 匕·竖
    g.hbar(800, 920, 30, weight=56)              # 匕·弯
    glyphs.append(g)

    # ---------------------------------------------------------- 伏 U+4F0F
    # ⿰亻犬。犬 = 大（一 + 撇 + 捺）+ 右上点（ slant=-14）。
    g = Glyph("uni4F0F", advance=1000, unicode=0x4F0F, note="伏：亻 + 犬")
    ren(g)
    g.hbar(490, 900, 610, weight=W_MAIN)         # 大·一（墨迹 562..658）
    g.diag(690, 780, 490, 40, weight=W_MAIN)     # 大·撇
    g.diag(660, 700, 920, 40, weight=W_MAIN)     # 大·捺
    g.dot(840, 745, 94, 110, -14)                # 犬·点
    glyphs.append(g)

    # ---------------------------------------------------------- 灯 U+706F
    # ⿰火丁。火 = 左点(-14) + 右上短撇(+14) + 长撇 + 捺。
    # 丁 = 横 + 竖钩（钩向左）。
    g = Glyph("uni706F", advance=1000, unicode=0x706F, note="灯：火 + 丁")
    g.dot(122, 600, 94, 126, -14)                # 火·左点
    g.dot(400, 700, 94, 126, 14)                 # 火·右上短撇
    g.diag(310, 780, 110, 60, weight=W_MAIN)      # 火·长撇
    g.diag(265, 640, 420, 55, weight=W_MAIN)     # 火·捺
    g.hbar(500, 940, 772, weight=W_MAIN)         # 丁·横
    g.vbar(720, 772, 60, weight=W_MAIN)          # 丁·竖
    g.hbar(600, 690, 46, weight=56)              # 丁·钩
    glyphs.append(g)

    # ---------------------------------------------------------- 辛 U+8F9B
    # ⿱亠丷干。亠 = 竖点(slant=0) + 横；丷左 -14 / 丷右 +14；干 = 两横 + 竖。
    g = Glyph("uni8F9B", advance=1000, unicode=0x8F9B, note="辛：亠 + 丷 + 干")
    g.dot(500, 768, 84, 100, 0)                  # 亠·竖点
    g.hbar(150, 850, 640, weight=W_MAIN)         # 亠·横（墨迹 592..688）
    g.dot(385, 505, 94, 126, -14)                # 丷·左点
    g.dot(615, 505, 94, 126, 14)                 # 丷·右撇
    g.hbar(200, 800, 330, weight=W_MAIN)         # 干·上横（墨迹 282..378）
    g.hbar(150, 850, 150, weight=W_MAIN)         # 干·下横（墨迹 102..198）
    g.vbar(500, 640, 0, weight=W_MAIN)           # 干·竖
    glyphs.append(g)

    # ---------------------------------------------------------- 俗 U+4FD7
    # ⿰亻谷。谷 = 丷（-14 / +14）+ 人（撇 + 捺）+ 口（口 x 570..900 / y 60..330）。
    g = Glyph("uni4FD7", advance=1000, unicode=0x4FD7, note="俗：亻 + 谷")
    ren(g)
    g.dot(575, 740, 94, 126, -14)                # 谷·丷左
    g.dot(845, 740, 94, 126, 14)                 # 谷·丷右
    g.diag(715, 660, 530, 450, weight=W_MAIN)    # 谷·撇
    g.diag(715, 660, 920, 440, weight=W_MAIN)    # 谷·捺
    g.hbar(570, 900, 330, weight=W_MAIN)         # 口·上横
    g.hbar(570, 900, 108, weight=W_MAIN)         # 口·下横
    g.vbar(618, 330, 108, weight=W_MAIN)         # 口·左竖（墨迹 570..666）
    g.vbar(852, 330, 108, weight=W_MAIN)         # 口·右竖（墨迹 804..900）
    glyphs.append(g)

    # ---------------------------------------------------------- 邪 U+90AA
    # ⿰牙阝（右耳旁）。右耳旁 = 竖在**右**，横撇弯钩的鼓包在左。
    # 牙 = 一 + 竖折（竖 + 短横）+ 亅 + 撇。
    g = Glyph("uni90AA", advance=1000, unicode=0x90AA, note="邪：牙 + 阝")
    g.hbar(60, 560, 700, weight=W_MAIN)          # 牙·一（墨迹 652..748）
    g.vbar(160, 700, 500, weight=W_MAIN)         # 牙·竖
    g.hbar(160, 340, 500, weight=W_MAIN)         # 牙·竖折的横
    g.vbar(300, 700, 60, weight=W_MAIN)          # 牙·亅
    g.hbar(230, 300, 46, weight=56)              # 牙·钩
    g.diag(300, 500, 90, 100, weight=W_MAIN)     # 牙·撇
    g.vbar(892, 820, 0, weight=W_MAIN)           # 阝·竖（墨迹 844..940）
    g.hbar(680, 892, 772, weight=W_MAIN)         # 阝·横撇弯钩·上横
    g.vbar(728, 772, 500, weight=W_MAIN)         # 阝·横撇弯钩·下行
    g.hbar(728, 892, 500, weight=W_MAIN)         # 阝·横撇弯钩·弯
    glyphs.append(g)

    # ---------------------------------------------------------- 麦 U+9EA6
    # ⿱龶夂。龶 = 竖 + 三横；夂 = 短撇 + 横撇（横 + 折）+ 捺。
    g = Glyph("uni9EA6", advance=1000, unicode=0x9EA6, note="麦：龶 + 夂")
    g.vbar(500, 820, 440, weight=W_MAIN)         # 龶·竖
    g.hbar(370, 630, 740, weight=W_MAIN)         # 龶·横1（墨迹 692..788）
    g.hbar(330, 670, 590, weight=W_MAIN)         # 龶·横2（墨迹 542..638）
    g.hbar(280, 720, 440, weight=W_MAIN)         # 龶·横3（墨迹 392..488）
    g.diag(430, 370, 320, 280, weight=W_MAIN)    # 夂·短撇
    g.hbar(320, 640, 280, weight=W_MAIN)         # 夂·横撇·横（墨迹 232..328）
    g.diag(640, 280, 450, 60, weight=W_MAIN)     # 夂·横撇·折
    g.diag(450, 280, 880, 40, weight=W_MAIN)     # 夂·捺
    glyphs.append(g)

    # ---------------------------------------------------------- 洞 U+6D1E
    # ⿰氵同。同 = 冂（横 + 左竖 + 右竖）+ 内一 + 口。
    g = Glyph("uni6D1E", advance=1000, unicode=0x6D1E, note="洞：氵 + 同")
    shui(g)
    g.hbar(500, 940, 772, weight=W_MAIN)         # 同·冂·横
    g.vbar(548, 772, 0, weight=W_MAIN)           # 同·冂·左竖（墨迹 500..596）
    g.vbar(892, 772, 0, weight=W_MAIN)           # 同·冂·右竖（墨迹 844..940）
    g.hbar(596, 850, 580, weight=W_MAIN)         # 同·内一（墨迹 532..628）
    g.hbar(596, 850, 440, weight=W_MAIN)         # 口·上横（墨迹 392..488）
    g.hbar(596, 850, 108, weight=W_MAIN)         # 口·下横（墨迹 60..156）
    g.vbar(644, 440, 108, weight=W_MAIN)         # 口·左竖（墨迹 596..692）
    g.vbar(802, 440, 108, weight=W_MAIN)         # 口·右竖（墨迹 754..850）
    glyphs.append(g)

    # ---------------------------------------------------------- 劣 U+52A3
    # ⿱少力。少 = 丨 + 左短撇(+14) + 右点(-14) + 长撇；力 = 横折钩 + 撇。
    g = Glyph("uni52A3", advance=1000, unicode=0x52A3, note="劣：少 + 力")
    g.vbar(500, 820, 500, weight=W_MAIN)          # 少·丨
    g.dot(335, 670, 94, 126, 14)                 # 少·左短撇
    g.dot(665, 670, 94, 126, -14)                # 少·右点
    g.diag(500, 500, 190, 120, weight=W_MAIN)     # 少·长撇
    g.hbar(480, 880, 300, weight=W_MAIN)         # 力·横（墨迹 252..348）
    g.vbar(832, 348, 60, weight=W_MAIN)          # 力·折（竖）
    g.hbar(714, 790, 46, weight=56)              # 力·钩
    g.diag(690, 300, 430, 60, weight=W_MAIN)     # 力·撇
    glyphs.append(g)

    # ---------------------------------------------------------- 那 U+90A3
    # ⿰（丨+横折+二）+（横折 + 撇）。左部件 = 竖 + 冂 + 二；右部件 = 横折 + 长撇。
    g = Glyph("uni90A3", advance=1000, unicode=0x90A3, note="那：竖折月 + 横折撇")
    g.vbar(110, 790, 0, weight=W_MAIN)           # 那·左·竖
    g.hbar(110, 390, 772, weight=W_MAIN)         # 那·左·横折·横
    g.vbar(342, 772, 100, weight=W_MAIN)         # 那·左·横折·折
    g.hbar(110, 342, 430, weight=W_THIN)         # 那·左·二·上横（墨迹 388..472）
    g.hbar(110, 342, 250, weight=W_THIN)         # 那·左·二·下横（墨迹 208..292）
    g.hbar(500, 900, 772, weight=W_MAIN)         # 那·右·横折·横
    g.vbar(852, 772, 40, weight=W_MAIN)          # 那·右·横折·折
    g.diag(560, 772, 420, 60, weight=W_MAIN)     # 那·右·撇
    glyphs.append(g)

    # ---------------------------------------------------------- 殴 U+6BB4
    # ⿰殳匚又。右部件 = 匚（横 + 左竖）+ 又。
    g = Glyph("uni6BB4", advance=1000, unicode=0x6BB4, note="殴：殳 + 匚又")
    shu(g, 60, 760, 380, 30, 210)
    g.hbar(520, 940, 772, weight=W_MAIN)         # 匚·横
    g.vbar(568, 772, 60, weight=W_MAIN)          # 匚·竖
    g.hbar(560, 900, 560, weight=W_MAIN)         # 又·横撇·横（墨迹 512..608）
    g.diag(900, 560, 680, 130, weight=W_MAIN)    # 又·横撇·折
    g.diag(580, 560, 920, 90, weight=W_MAIN)     # 又·捺
    glyphs.append(g)

    # ---------------------------------------------------------- 奉 U+5949
    # ⿱龶人二丨。龶 = 竖 + 三横；人 = 撇 + 捺；底 = 二 + 竖。
    g = Glyph("uni5949", advance=1000, unicode=0x5949, note="奉：龶 + 人 + 二丨")
    g.vbar(500, 820, 420, weight=W_MAIN)         # 龶·竖
    g.hbar(370, 630, 740, weight=W_MAIN)         # 龶·横1（墨迹 692..788）
    g.hbar(330, 670, 540, weight=W_MAIN)         # 龶·横2（墨迹 492..588）
    g.hbar(280, 720, 420, weight=W_MAIN)         # 龶·横3（墨迹 372..468）
    g.diag(500, 420, 180, 240, weight=W_MAIN)    # 人·撇
    g.diag(500, 420, 820, 240, weight=W_MAIN)    # 人·捺
    g.hbar(330, 670, 200, weight=W_MAIN)         # 底·上横（墨迹 152..248）
    g.hbar(280, 720, 80, weight=W_MAIN)          # 底·下横（墨迹 32..128）
    g.vbar(500, 200, 0, weight=W_MAIN)           # 底·竖
    glyphs.append(g)

    # ---------------------------------------------------------- 朴 U+6734
    # ⿰木卜。卜 的竖落在 x 640（与赴 中的卜同一坐标）。
    g = Glyph("uni6734", advance=1000, unicode=0x6734, note="朴：木 + 卜")
    mu(g)
    bu(g)
    glyphs.append(g)

    # ---------------------------------------------------------- 亭 U+4EAD
    # ⿱亠口冖丁。亭竖排 5 横，故口用 84 细档以保住内白（46 单位）。
    g = Glyph("uni4EAD", advance=1000, unicode=0x4EAD, note="亭：亠 + 口 + 冖 + 丁")
    g.dot(500, 768, 84, 96, 0)                   # 亠·竖点
    g.hbar(150, 850, 640, weight=W_MAIN)         # 亠·横（墨迹 592..688）
    g.hbar(320, 680, 520, weight=W_THIN)         # 口·上横（墨迹 478..562）
    g.hbar(320, 680, 390, weight=W_THIN)         # 口·下横（墨迹 348..432）
    g.vbar(362, 520, 390, weight=W_THIN)         # 口·左竖（墨迹 320..404）
    g.vbar(638, 520, 390, weight=W_THIN)         # 口·右竖（墨迹 596..680）
    g.hbar(140, 860, 270, weight=W_THIN)         # 冖·横（墨迹 228..312）
    g.vbar(182, 312, 240, weight=W_THIN)         # 冖·左点
    g.vbar(818, 312, 240, weight=W_THIN)         # 冖·右点
    g.hbar(300, 700, 140, weight=W_MAIN)         # 丁·横（墨迹 92..188）
    g.vbar(500, 140, 0, weight=W_MAIN)           # 丁·竖
    g.hbar(410, 500, 40, weight=56)              # 丁·钩
    glyphs.append(g)

    # ---------------------------------------------------------- 姓 U+59D3
    # ⿰女生。女 = 撇点（撇 + 点两段）+ 丿 + 一；生 = 丿 + 三横 + 竖。
    g = Glyph("uni59D3", advance=1000, unicode=0x59D3, note="姓：女 + 生")
    g.diag(290, 790, 170, 480, weight=W_MAIN)     # 女·撇点·撇
    g.diag(170, 480, 400, 130, weight=W_MAIN)     # 女·撇点·点
    g.diag(350, 700, 90, 60, weight=W_MAIN)       # 女·丿
    g.hbar(80, 400, 480, weight=W_MAIN)           # 女·一（墨迹 432..528）
    g.diag(570, 790, 500, 700, weight=W_MAIN)     # 生·丿
    g.hbar(530, 900, 650, weight=W_MAIN)          # 生·横1（墨迹 602..698）
    g.hbar(560, 860, 400, weight=W_MAIN)          # 生·横2（墨迹 352..448）
    g.hbar(500, 940, 140, weight=W_MAIN)          # 生·横3（墨迹 92..188）
    g.vbar(720, 650, 0, weight=W_MAIN)            # 生·竖
    glyphs.append(g)

    # ---------------------------------------------------------- 怪 U+602A
    # ⿰忄圣。忄 = 左点(+14) + 丨 + 右点(-14)；圣 = 又（横撇 + 捺）+ 土。
    g = Glyph("uni602A", advance=1000, unicode=0x602A, note="怪：忄 + 圣")
    g.dot(120, 620, 94, 126, 14)                 # 忄·左点
    g.vbar(200, 820, 0, weight=W_MAIN)            # 忄·丨
    g.dot(340, 640, 94, 126, -14)                # 忄·右点
    g.hbar(500, 900, 700, weight=W_MAIN)          # 又·横撇·横（墨迹 652..748）
    g.diag(852, 700, 620, 400, weight=W_MAIN)     # 又·横撇·折
    g.diag(540, 700, 910, 360, weight=W_MAIN)     # 又·捺
    g.hbar(560, 880, 300, weight=W_MAIN)          # 土·上横（墨迹 252..348）
    g.vbar(720, 300, 52, weight=W_MAIN)           # 土·竖
    g.hbar(500, 940, 100, weight=W_MAIN)          # 土·下横（墨迹 52..148）
    glyphs.append(g)

    # ---------------------------------------------------------- 佳 U+4F73
    # ⿰亻圭。圭 = 上下两个「土」：四横 + 两条竖，横间空隙 104。
    g = Glyph("uni4F73", advance=1000, unicode=0x4F73, note="佳：亻 + 圭")
    ren(g)
    g.hbar(540, 900, 690, weight=W_MAIN)          # 圭·横1（墨迹 642..738）
    g.vbar(720, 690, 490, weight=W_MAIN)          # 圭·竖1
    g.hbar(560, 880, 490, weight=W_MAIN)          # 圭·横2（墨迹 442..538）
    g.hbar(540, 900, 290, weight=W_MAIN)          # 圭·横3（墨迹 242..338）
    g.vbar(720, 290, 90, weight=W_MAIN)           # 圭·竖2
    g.hbar(500, 940, 90, weight=W_MAIN)           # 圭·横4（墨迹 42..138）
    glyphs.append(g)

    # ---------------------------------------------------------- 胃 U+80C3
    # ⿱田月。田 = 囗 + 中竖 + 中横；月 = 丿 + 横折 + 二。
    g = Glyph("uni80C3", advance=1000, unicode=0x80C3, note="胃：田 + 月")
    g.hbar(200, 800, 772, weight=W_MAIN)          # 田·上横
    g.hbar(200, 800, 530, weight=W_MAIN)          # 田·下横（墨迹 482..578）
    g.vbar(248, 820, 482, weight=W_MAIN)          # 田·左竖（墨迹 200..296）
    g.vbar(752, 820, 482, weight=W_MAIN)          # 田·右竖（墨迹 704..800）
    g.vbar(500, 820, 482, weight=W_MAIN)          # 田·中竖（墨迹 452..548）
    g.hbar(200, 800, 650, weight=W_THIN)          # 田·中横（墨迹 608..692）
    g.diag(290, 400, 255, 20, weight=W_MAIN)      # 月·丿
    g.hbar(290, 710, 400, weight=W_MAIN)          # 月·横折·横（墨迹 352..448）
    g.vbar(662, 400, 0, weight=W_MAIN)            # 月·横折·折（墨迹 614..710）
    g.hbar(280, 662, 250, weight=W_THIN)          # 月·内横1（墨迹 208..292）
    g.hbar(270, 662, 95, weight=W_THIN)           # 月·内横2（墨迹 53..137）
    glyphs.append(g)

    # ---------------------------------------------------------- 赴 U+8D74
    # ⿰走卜。走 = 土（一 + 丨 + 一）+ 龰（丨 + 一 + 撇 + 捺）。
    g = Glyph("uni8D74", advance=1000, unicode=0x8D74, note="赴：走 + 卜")
    g.hbar(130, 480, 700, weight=W_MAIN)          # 走·土·上横（墨迹 652..748）
    g.vbar(300, 700, 480, weight=W_MAIN)          # 走·土·竖
    g.hbar(100, 500, 480, weight=W_MAIN)          # 走·土·下横（墨迹 432..528）
    g.vbar(300, 480, 260, weight=W_MAIN)          # 走·龰·竖
    g.hbar(300, 470, 300, weight=W_THIN)          # 走·龰·横（墨迹 258..342）
    g.diag(470, 300, 330, 140, weight=W_MAIN)     # 走·龰·撇
    g.diag(300, 280, 520, 30, weight=W_MAIN)      # 走·龰·捺
    bu(g)
    glyphs.append(g)

    # ---------------------------------------------------------- 虎 U+864E
    # ⿱虍儿。虍 = 丨 + 一 + 一 + 丿 + 七；儿 = 丿 + 竖弯。
    g = Glyph("uni864E", advance=1000, unicode=0x864E, note="虎：虍 + 儿")
    g.vbar(500, 820, 740, weight=W_MAIN)          # 虍·顶部竖
    g.hbar(500, 700, 740, weight=W_THIN)          # 虍·顶部横（墨迹 698..782）
    g.hbar(250, 820, 620, weight=W_MAIN)          # 虍·横（墨迹 572..668）
    g.diag(300, 660, 130, 180, weight=W_MAIN)     # 虍·撇
    g.hbar(430, 720, 470, weight=W_MAIN)          # 七·横（墨迹 422..518）
    g.vbar(480, 470, 300, weight=W_MAIN)          # 七·竖
    g.hbar(480, 640, 286, weight=56)              # 七·弯钩
    g.diag(400, 250, 230, 30, weight=W_MAIN)      # 儿·撇
    g.vbar(700, 250, 60, weight=W_MAIN)           # 儿·竖
    g.hbar(700, 880, 46, weight=56)               # 儿·弯
    glyphs.append(g)

    # ---------------------------------------------------------- 盆 U+76C6
    # ⿱分皿。分 = 八（撇 + 捺）+ 刀（横折钩 + 撇）；皿 = 扁框 + 两中竖。
    g = Glyph("uni76C6", advance=1000, unicode=0x76C6, note="盆：分 + 皿")
    g.diag(430, 800, 260, 650, weight=W_MAIN)     # 分·八·撇
    g.diag(570, 800, 740, 650, weight=W_MAIN)     # 分·八·捺
    g.hbar(310, 690, 540, weight=W_MAIN)          # 分·刀·横（墨迹 492..588）
    g.vbar(642, 540, 390, weight=W_MAIN)          # 分·刀·竖钩
    g.hbar(580, 660, 376, weight=56)              # 分·刀·钩
    g.diag(500, 540, 400, 420, weight=W_MAIN)     # 分·刀·撇
    g.hbar(160, 840, 290, weight=W_MAIN)          # 皿·上横（墨迹 242..338）
    g.hbar(160, 840, 48, weight=W_MAIN)           # 皿·下横（墨迹 0..96）
    g.vbar(208, 290, 48, weight=W_MAIN)           # 皿·左竖（墨迹 160..256）
    g.vbar(792, 290, 48, weight=W_MAIN)           # 皿·右竖（墨迹 744..840）
    g.vbar(400, 290, 48, weight=W_MAIN)           # 皿·中竖1（墨迹 352..448）
    g.vbar(600, 290, 48, weight=W_MAIN)           # 皿·中竖2（墨迹 552..648）
    glyphs.append(g)

    # ---------------------------------------------------------- 壮 U+58EE
    # ⿰丬士。丬 = 丶 + 丨 + 提；士 = 上横（长）+ 竖 + 下横（短）。
    g = Glyph("uni58EE", advance=1000, unicode=0x58EE, note="壮：丬 + 士")
    g.dot(120, 640, 84, 120, -14)                 # 丬·点
    g.vbar(330, 820, 0, weight=W_MAIN)            # 丬·丨
    g.diag(120, 180, 320, 315, weight=W_MAIN)     # 丬·提
    g.hbar(440, 940, 600, weight=W_MAIN)          # 士·上横（墨迹 552..648）
    g.vbar(690, 600, 200, weight=W_MAIN)          # 士·竖
    g.hbar(480, 900, 200, weight=W_MAIN)          # 士·下横（墨迹 152..248）
    glyphs.append(g)

    # ---------------------------------------------------------- 疫 U+75AB
    # ⿰疒殳。疒 = 点 + 横 + 撇 + 冫（点 + 提）。
    g = Glyph("uni75AB", advance=1000, unicode=0x75AB, note="疫：疒 + 殳")
    g.dot(250, 772, 84, 96, 0)                   # 疒·点
    g.hbar(60, 430, 650, weight=W_MAIN)           # 疒·横（墨迹 602..698）
    g.diag(200, 690, 115, 120, weight=W_MAIN)     # 疒·撇
    g.dot(165, 480, 94, 126, -14)                # 疒·冫·点
    g.diag(105, 250, 250, 330, weight=W_MAIN)     # 疒·冫·提
    shu(g, 470, 800, 480, 70, 210)
    glyphs.append(g)

    # ---------------------------------------------------------- 机 U+673A
    # ⿰木几。
    g = Glyph("uni673A", advance=1000, unicode=0x673A, note="机：木 + 几")
    mu(g)
    ji(g, 540, 780, 120)
    glyphs.append(g)

    # ---------------------------------------------------------- 尿 U+5C3F
    # ⿱尸水。尸 = 横折 + 横 + 撇；水 = 竖钩 + 横撇（横 + 撇）+ 撇 + 捺。
    g = Glyph("uni5C3F", advance=1000, unicode=0x5C3F, note="尿：尸 + 水")
    g.hbar(150, 800, 772, weight=W_MAIN)          # 尸·横折·横
    g.vbar(752, 772, 500, weight=W_MAIN)          # 尸·横折·折
    g.hbar(110, 752, 500, weight=W_MAIN)          # 尸·横（墨迹 452..548）
    g.diag(160, 772, 95, 300, weight=W_MAIN)      # 尸·撇
    g.vbar(500, 500, 40, weight=W_MAIN)           # 水·竖钩
    g.hbar(410, 500, 26, weight=56)              # 水·钩
    g.hbar(280, 490, 380, weight=W_THIN)          # 水·横撇·横（墨迹 338..422）
    g.diag(440, 380, 230, 170, weight=W_MAIN)     # 水·横撇·撇
    g.diag(540, 380, 870, 130, weight=W_MAIN)     # 水·捺
    glyphs.append(g)

    # ---------------------------------------------------------- 吐 U+5410
    # ⿰口土。口 x 60..420 / y 260..720；土 = 上横 + 竖 + 下横。
    g = Glyph("uni5410", advance=1000, unicode=0x5410, note="吐：口 + 土")
    kou(g, 60, 420, 260, 720)
    g.hbar(480, 940, 620, weight=W_MAIN)          # 土·上横（墨迹 572..668）
    g.vbar(710, 620, 200, weight=W_MAIN)          # 土·竖
    g.hbar(500, 920, 200, weight=W_MAIN)          # 土·下横（墨迹 152..248）
    glyphs.append(g)

    # ---------------------------------------------------------- 弥 U+5F25
    # ⿰弓尔。弓 = 横折 + 中横 + 竖折折钩；尔 = 丿 + 一 + 亅 + 撇 + 点。
    g = Glyph("uni5F25", advance=1000, unicode=0x5F25, note="弥：弓 + 尔")
    g.hbar(100, 380, 760, weight=W_MAIN)          # 弓·横折·横（墨迹 712..808）
    g.vbar(332, 760, 560, weight=W_MAIN)          # 弓·横折·折（墨迹 284..380）
    g.hbar(100, 332, 560, weight=W_MAIN)          # 弓·中横（墨迹 512..608）
    g.vbar(148, 560, 330, weight=W_MAIN)          # 弓·竖（墨迹 100..196）
    g.hbar(148, 380, 330, weight=W_MAIN)          # 弓·竖折折钩·横（墨迹 282..378）
    g.vbar(332, 330, 200, weight=W_MAIN)          # 弓·竖折折钩·折
    g.hbar(250, 332, 186, weight=56)              # 弓·钩
    g.diag(640, 790, 560, 700, weight=W_MAIN)     # 尔·丿
    g.hbar(560, 900, 650, weight=W_MAIN)          # 尔·一（墨迹 602..698）
    g.vbar(720, 650, 180, weight=W_MAIN)          # 尔·亅（墨迹 672..768）
    g.hbar(630, 720, 166, weight=56)              # 尔·钩
    g.diag(560, 560, 470, 300, weight=W_MAIN)     # 尔·撇
    g.dot(870, 500, 94, 126, -14)                # 尔·点
    glyphs.append(g)

    return glyphs


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-017.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
