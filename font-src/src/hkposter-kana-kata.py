"""HK Poster Heavy —— 片假名（カタカナ）。Wave 1 基础 + wave2 返工（补 20 缺字 + 字面放大）。

字符清单：
    基础 48（U+30A2–U+30F3，含 ヰ U+30F0 / ヱ U+30F1）
  + 有浊音/半浊音的预组合形 25（U+30AC–U+30DD）
  + 反复记号 2（U+30FD / U+30FE）
  + wave2 返工新增 20（U+30A0 / U+30A1 / U+30A3 / U+30A5 / U+30A7 / U+30A9 /
      U+30C3 / U+30E3 / U+30E5 / U+30E7 / U+30EE / U+30F4 / U+30F5 / U+30F6 /
      U+30F7 / U+30F8 / U+30F9 / U+30FA / U+30FB / U+30FF）
  = 95 字形

> wave2 返工要点（lane: wave2/kana-kata-rework）
>   * **补 20 个缺字**：U+30A0..U+30FF 区内 20 个码位此前不在字体里（渲染成 .notdef
>     空心框），其中含日文最高频的小假名 ッ ャ ュ ョ。
>   * **字面放大到与汉字同族**：片假名字高中位原本 601（汉字 796，比值 0.756），
>     偏小不偏轻。本轮把全尺寸片假名放大 ×1.30（只缩放中心线坐标，笔画权重
>     96/88/80 一律不动），放大后字高中位与汉字之比回到 0.88~0.95 区间。
>   * **骨架不动**：只改坐标，不改笔画走向与结构（用户原话：「假名字形变化不要
>     过大，只是用海报的粗手写体写法，整体字形必须还保持原有状态」）。

设计取舍：
  * 坐标：UPM 1000，y 向上，基线 y=0。片假名 advance=1000。
    放大后墨迹统一收在 x 60..940 / y 0..820（与汉字同框）。
  * 几何化：片假名笔画直、转折硬，全部用硬折（GLY-002），不做圆转；斜笔仅用中心线两端点
    + 垂直权重表达。
  * 权重档：主 110 / 次 100 / 细 90 / 点 100（wave2 v2：整体加粗到「假名/汉字 墨量比 0.55」；
    加粗只动笔画权重档位，不动笔画走向、不动骨架、不动字面框）。
    点、浊音、手浊音记号一律 100。
  * 放大算法：围绕该字自身墨迹外接框中心 ×1.30，再把墨迹外接框中心对到 (500, 400)；
    宽度/高度超过 x 60..940 / y 0..820 的字按可用空间等比回退（见 _enlarge）。
  * 视觉大小匹配：浊音/半浊音形由**放大后的**基础形再缩放 0.84 并右缘对到 735，
    右上角留出记号位（x 758..926），保证记号与字形不粘连。
  * 小假名：另画的紧凑字形（笔画更少更紧凑），位置在 em 右上区域；
    **ッ** 横向居中、纵向偏下。字高约为对应全尺寸片假名的 0.70 倍。
  * 白口（GLY-005）：八/ハ 类两笔形顶部留 60 单位净空，底部左右分张。

> wave2 v2 返工要点（lane: wave2/kana-kata-rework）
>   * **加粗到墨量比 0.55**（项目所有者 2026-10-25）：四档权重 96/88/80/88 → 110/100/90/100。
>     参照字体换成开源可商用的 M PLUS 1p Black（OFL 1.1），只参考比例与骨架，不描轮廓。
>     重量档位之外的一切（笔画走向、骨架、字面框）保持不变。
>   * **修 ゥ（U+30A5）太小**：原字高 356，只占全尺寸片假名的 0.49，判据要求 0.65..0.78。
>     本轮把 ゥ 的中心线坐标放大到「全尺寸片假名字高中位 × 0.70」，
>     骨架拆法（短竖 + 横 + 横折撇）不变；放大后重新对中（中心 x=500）+ 贴基线（底边 y=40）。
>   * **小假名落位复核**：权重加粗后墨迹会外扩，所有小假名重新做「水平居中 + 贴基线」，
>     保证落位判据（中心 x=500 / 底边 y=40）在新权重下依然成立。
>
> wave2 v3 返工要点（lane: wave2/kana-kata-rework）—— 外观改成港产海报风格
>   * **浊点 / 半浊点统一成斜切平行四边形**（汉字 `g.dot(..., slant=26)` 的语言）：
>     浊点 = 两枚 DOT（slant=26），半浊点 = 一枚 DOT（slant=26）；
>     全字族同一形状（GLY-004），且与基字不相交（浊点让位仍为 0）。
>   * **点画走斜切语言**：ウ/ゥ/ワ/ヮ 的左上点、・（片假名中点）都改成 DOT(slant=26)，
>     本 master 不再使用圆环（RING）语言 —— 汉字词汇里没有环形记号。
>   * **斜笔（撇捺）保持 D（= 汉字 g.diag「斜切边矩形」语言）**：シ/ツ/ソ/ン 的两枚点画
>     倾角约 56°，汉字 slant 档（14~26）表达不了，改成 DOT 会改笔画走向（字形红线），故不动。
>   * **GLY-003**：斜切只用在点/记号上；横竖撇捺一律不斜切。
>   * **内白保护（局部降档，不全局回退）**：シ/ツ 的点画 W_TICK=84、小假名 ッ 的点画
>     W_TICK_SM=76 —— 加粗 + 浊音形 0.84 挤压后两枚点画会糊在一起
>     （check_glyphs 曾报 ジ 轮廓自交），单独降档后净空分别为 15.9 / 8.6 / 5.2 单位。
"""

from __future__ import annotations

import math
import statistics
import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, write_ufo  # noqa: E402

W_MAIN = 110
W_SEC = 100
W_THIN = 90
W_DOT = 100
# 点画细档（局部降档，**不是全局回退**）：
#   シ/ツ 的两枚点画是「辅助撇」，字面 ×1.30 之后与长笔几乎相接；
#   浊音形还要再缩到 0.84（ツ 更被压到 0.80），加粗后两枚点画会糊成一团
#   （check_glyphs 报 ジ 轮廓自交）。按 v3 规格「糊了就该字单独降一档」处理。
W_TICK = 84
# 小假名 ッ 的两枚点画本来就更挤，再降一档，保住两枚点画之间的内白。
W_TICK_SM = 76

# 设计框中心（缩放用）
_CX = 500.0
_CY = 400.0
# wave2：全尺寸片假名字面放大系数（只缩放中心线坐标，权重不动）
KATA_SCALE = 1.30
# 放大后墨迹外框（与汉字同框）；纵向留 20 单位余量，墨迹不越过基线
FRAME_X0, FRAME_X1 = 60.0, 940.0
FRAME_Y0, FRAME_Y1 = 0.0, 820.0
FRAME_H_MAX = 800.0
# 浊音形参数：放大后的基础形缩到 0.84，基础部分右缘对到 735（记号在 758..926）
_VOICE_SCALE = 0.84
_VOICE_RIGHT = 735.0
# 小假名：字高约为全尺寸的 0.70 倍，位于 em 右上区域（ッ 横向居中、纵向偏下）
SMALL_RATIO = 0.70
# 小假名落位：水平居中（中心 x=500）+ 贴基线（底边 y=40）
SMALL_CX = 500.0
SMALL_BOTTOM = 40.0
# ゥ（U+30A5）目标字高 = 全尺寸片假名字高中位 × 本系数（判据 0.68..0.72）
U_SMALL_RATIO = 0.70


# ---------------------------------------------------------------------------
# 笔画描述符（与汉字同源的四个词汇）：
#   ("H", x1, x2, y, w)          水平笔画（墨迹占 y±w/2，两端平切）
#   ("V", x, y1, y2, w)          垂直笔画（端点即墨迹端点）
#   ("D", x1, y1, x2, y2, w)     斜笔画（厚度垂直于中心线）＝ 汉字的撇捺语言
#   ("DOT", cx, cy, w, h, slant) 点/记号：斜切平行四边形（汉字 g.dot 语言）
#       上下边水平、顶边相对底边右移 slant，slant 沿用汉字档位（26/20/18/16/14/−14）。
#       w 是绝对宽度，h 随字面放大走，slant 是绝对量（角度档不随缩放漂移）。
# 圆环（RING）语言已随浊点/半浊点统一一起去掉：汉字词汇里没有环形记号。
# ---------------------------------------------------------------------------

# 基础形：码位 -> (说明, 笔画表)
BASE: dict[int, tuple[str, list]] = {
    0x30A2: ("ア：短横居中偏上，右端接短撇，长斜笔自左上向右下贯穿", [
        ("H", 320, 720, 600, W_SEC),
        ("D", 720, 600, 470, 380, W_SEC),
        ("D", 230, 720, 690, 130, W_MAIN),
    ]),
    0x30A4: ("イ：左上短斜笔与右侧长竖在顶端相接", [
        ("D", 700, 710, 380, 460, W_MAIN),
        ("V", 650, 90, 710, W_MAIN),
    ]),
    0x30A6: ("ウ：左上点（斜切平行四边形）+ 横折撇，横右端向左下折出", [
        ("DOT", 300, 675, 100, 110, 26),
        ("H", 400, 860, 590, W_MAIN),
        ("D", 860, 590, 600, 330, W_MAIN),
    ]),
    0x30A8: ("エ：上中下三横，中竖居中偏右连上下横", [
        ("H", 180, 820, 700, W_MAIN),
        ("V", 560, 100, 700, W_MAIN),
        ("H", 300, 560, 400, W_SEC),
        ("H", 180, 820, 100, W_MAIN),
    ]),
    0x30AA: ("オ：上横 + 中竖 + 自横右端向左下斜笔", [
        ("H", 240, 760, 680, W_MAIN),
        ("V", 500, 90, 720, W_MAIN),
        ("D", 760, 680, 300, 260, W_SEC),
    ]),
    0x30AB: ("カ：上横 + 右下折笔 + 自上中向左下斜笔", [
        ("H", 230, 760, 660, W_MAIN),
        ("D", 760, 660, 610, 120, W_MAIN),
        ("D", 560, 740, 200, 220, W_SEC),
    ]),
    0x30AD: ("キ：两横 + 自右上向左下斜笔贯穿两横", [
        ("H", 200, 800, 680, W_MAIN),
        ("H", 220, 740, 420, W_MAIN),
        ("D", 780, 710, 280, 180, W_MAIN),
    ]),
    0x30AF: ("ク：左上短撇 + 横折撇", [
        ("D", 250, 540, 390, 730, W_SEC),
        ("H", 330, 800, 570, W_MAIN),
        ("D", 800, 570, 400, 120, W_MAIN),
    ]),
    0x30B1: ("ケ：左上短撇 + 中横 + 自右上向左下长斜笔", [
        ("D", 250, 540, 390, 730, W_SEC),
        ("H", 220, 720, 560, W_SEC),
        ("D", 700, 730, 350, 130, W_MAIN),
    ]),
    0x30B3: ("コ：上下横 + 右侧竖连之", [
        ("H", 140, 780, 680, W_MAIN),
        ("V", 780, 110, 680, W_MAIN),
        ("H", 140, 780, 110, W_MAIN),
    ]),
    0x30B5: ("サ：横 + 右侧长竖（上下皆出）+ 左侧短竖", [
        ("H", 180, 820, 560, W_MAIN),
        ("V", 560, 140, 740, W_MAIN),
        ("V", 300, 140, 560, W_SEC),
    ]),
    0x30B7: ("シ：左上两点 + 自左上向右下长曲笔", [
        ("D", 250, 660, 370, 740, W_TICK),
        ("D", 230, 520, 350, 600, W_TICK),
        ("D", 400, 700, 860, 190, W_MAIN),
    ]),
    0x30B9: ("ス：上横折向左下 + 自左上向右下捺笔相交", [
        ("H", 250, 700, 690, W_MAIN),
        ("D", 700, 690, 330, 170, W_MAIN),
        ("D", 340, 690, 870, 130, W_SEC),
    ]),
    0x30BB: ("セ：上横 + 左竖贯穿 + 底部向右折脚", [
        ("H", 300, 820, 620, W_MAIN),
        ("V", 360, 110, 700, W_MAIN),
        ("H", 360, 560, 110, W_SEC),
    ]),
    0x30BD: ("ソ：左上短撇 + 自右上向左下长斜笔", [
        ("D", 280, 600, 450, 690, W_SEC),
        ("D", 700, 730, 300, 130, W_MAIN),
    ]),
    0x30BF: ("タ：左上短撇 + 外框折笔 + 内侧斜笔", [
        ("D", 340, 690, 210, 580, W_SEC),
        ("D", 250, 690, 760, 540, W_MAIN),
        ("D", 760, 540, 420, 130, W_MAIN),
        ("D", 560, 640, 250, 230, W_SEC),
    ]),
    0x30C1: ("チ：上横右端接长斜笔向左下 + 中横向右伸出", [
        ("H", 250, 700, 690, W_MAIN),
        ("D", 700, 690, 380, 150, W_MAIN),
        ("H", 380, 830, 420, W_SEC),
    ]),
    0x30C4: ("ツ：左上两点 + 自左上向右下长曲笔", [
        ("D", 220, 590, 340, 670, W_TICK),
        ("D", 190, 450, 310, 530, W_TICK),
        ("D", 370, 700, 850, 190, W_MAIN),
    ]),
    0x30C6: ("テ：上横右端接长斜笔向左下 + 中横向左伸出", [
        ("H", 260, 700, 690, W_MAIN),
        ("D", 700, 690, 420, 150, W_MAIN),
        ("H", 300, 560, 380, W_SEC),
    ]),
    0x30C8: ("ト：长竖 + 自竖中段向右下短斜笔", [
        ("V", 420, 100, 740, W_MAIN),
        ("D", 430, 500, 650, 380, W_SEC),
    ]),
    0x30CA: ("ナ：横 + 自上中向左下长斜笔贯穿", [
        ("H", 250, 810, 560, W_MAIN),
        ("D", 600, 750, 360, 110, W_MAIN),
    ]),
    0x30CB: ("ニ：上短横 + 下长横", [
        ("H", 290, 750, 620, W_MAIN),
        ("H", 250, 790, 260, W_MAIN),
    ]),
    0x30CC: ("ヌ：上横折向左下 + 自左上向右下长捺相交", [
        ("H", 230, 620, 690, W_MAIN),
        ("D", 620, 690, 270, 170, W_MAIN),
        ("D", 240, 690, 880, 130, W_SEC),
    ]),
    0x30CD: ("ネ：左上短撇 + 长斜笔 + 中横 + 中竖", [
        ("D", 300, 620, 450, 700, W_SEC),
        ("D", 700, 730, 430, 420, W_MAIN),
        ("H", 250, 720, 430, W_SEC),
        ("V", 470, 120, 440, W_MAIN),
    ]),
    0x30CE: ("ノ：自左上向右下一笔长斜笔", [
        ("D", 320, 720, 700, 140, W_MAIN),
    ]),
    0x30CF: ("ハ：左右两笔分张，顶部留白口", [
        ("D", 400, 700, 220, 130, W_MAIN),
        ("D", 560, 700, 790, 130, W_MAIN),
    ]),
    0x30D2: ("ヒ：左上短竖 + 底部长横", [
        ("V", 320, 540, 740, W_SEC),
        ("H", 300, 830, 160, W_MAIN),
    ]),
    0x30D5: ("フ：上横 + 自右端向左下斜折", [
        ("H", 300, 800, 680, W_MAIN),
        ("D", 800, 680, 420, 140, W_MAIN),
    ]),
    0x30D8: ("ヘ：左长右短两斜笔成折角", [
        ("D", 220, 420, 610, 650, W_MAIN),
        ("D", 610, 650, 850, 420, W_SEC),
    ]),
    0x30DB: ("ホ：上横 + 中竖 + 下部左右分张短斜笔", [
        ("H", 250, 700, 620, W_MAIN),
        ("V", 500, 140, 700, W_MAIN),
        ("D", 440, 430, 260, 160, W_SEC),
        ("D", 560, 430, 740, 160, W_SEC),
    ]),
    0x30DE: ("マ：上横折向左下 + 自左上向右下斜笔相交", [
        ("H", 250, 650, 690, W_MAIN),
        ("D", 650, 690, 330, 260, W_MAIN),
        ("D", 270, 680, 800, 150, W_SEC),
    ]),
    0x30DF: ("ミ：三道平行右上斜笔", [
        ("D", 340, 160, 700, 350, W_MAIN),
        ("D", 310, 350, 670, 540, W_MAIN),
        ("D", 280, 540, 640, 730, W_MAIN),
    ]),
    0x30E0: ("ム：左上短竖 + 右下斜折 + 末端上挑", [
        ("V", 340, 470, 740, W_MAIN),
        ("D", 340, 470, 720, 180, W_MAIN),
        ("D", 720, 180, 520, 290, W_SEC),
    ]),
    0x30E1: ("メ：两斜笔交叉成 X", [
        ("D", 320, 690, 720, 280, W_MAIN),
        ("D", 700, 700, 300, 180, W_SEC),
    ]),
    0x30E2: ("モ：上横 + 中横 + 右竖下端向左上挑", [
        ("H", 260, 780, 690, W_MAIN),
        ("H", 300, 640, 450, W_MAIN),
        ("V", 640, 190, 480, W_MAIN),
        ("D", 640, 190, 420, 280, W_SEC),
    ]),
    0x30E4: ("ヤ：左上短横 + 自右上向左下长斜笔", [
        ("H", 230, 680, 680, W_MAIN),
        ("D", 700, 720, 400, 140, W_MAIN),
    ]),
    0x30E6: ("ユ：左上短撇 + 横折竖 + 底横", [
        ("D", 280, 640, 470, 700, W_SEC),
        ("H", 320, 760, 540, W_MAIN),
        ("V", 760, 200, 540, W_MAIN),
        ("H", 300, 760, 200, W_MAIN),
    ]),
    0x30E8: ("ヨ：左竖 + 三横向右伸出（上短下长）", [
        ("V", 300, 140, 700, W_MAIN),
        ("H", 300, 640, 700, W_MAIN),
        ("H", 300, 700, 430, W_MAIN),
        ("H", 300, 760, 170, W_MAIN),
    ]),
    0x30E9: ("ラ：上短横 + 自右上向左下长斜笔", [
        ("H", 320, 780, 700, W_SEC),
        ("D", 730, 610, 360, 130, W_MAIN),
    ]),
    0x30EA: ("リ：左上短竖 + 右长竖下端向左上挑", [
        ("V", 330, 400, 700, W_SEC),
        ("V", 620, 180, 700, W_MAIN),
        ("D", 620, 180, 480, 260, W_SEC),
    ]),
    0x30EB: ("ル：左上短竖 + 长斜笔下端上挑", [
        ("V", 330, 400, 700, W_SEC),
        ("D", 660, 700, 330, 180, W_MAIN),
        ("D", 330, 180, 430, 260, W_THIN),
    ]),
    0x30EC: ("レ：上段竖 + 底端向右下展开", [
        ("V", 520, 230, 740, W_MAIN),
        ("D", 520, 230, 800, 150, W_MAIN),
    ]),
    0x30ED: ("ロ：左竖 + 上下横 + 右竖成框", [
        ("V", 250, 140, 700, W_MAIN),
        ("H", 250, 750, 700, W_MAIN),
        ("V", 750, 140, 700, W_MAIN),
        ("H", 250, 750, 140, W_MAIN),
    ]),
    0x30EF: ("ワ：左上点（斜切平行四边形）+ 横折撇", [
        ("DOT", 320, 630, 100, 140, 26),
        ("H", 300, 780, 620, W_MAIN),
        ("D", 780, 620, 430, 130, W_MAIN),
    ]),
    0x30F0: ("ヰ：上横 + 下横 + 短左竖 + 长右竖（井形）", [
        ("H", 300, 770, 660, W_MAIN),
        ("H", 280, 730, 340, W_MAIN),
        ("V", 430, 290, 700, W_SEC),
        ("V", 640, 180, 740, W_MAIN),
    ]),
    0x30F1: ("ヱ：上短横 + 中竖 + 下长横", [
        ("H", 320, 700, 690, W_MAIN),
        ("V", 470, 140, 690, W_MAIN),
        ("H", 280, 790, 140, W_MAIN),
    ]),
    0x30F2: ("ヲ：上短横 + 横折撇", [
        ("H", 320, 640, 690, W_SEC),
        ("H", 280, 780, 540, W_MAIN),
        ("D", 780, 540, 420, 140, W_MAIN),
    ]),
    0x30F3: ("ン：左上短撇 + 自左上向右下长斜笔", [
        ("D", 270, 660, 420, 740, W_SEC),
        ("D", 350, 600, 820, 150, W_MAIN),
    ]),
}

# 浊音形：码位 -> (基础形码位, 说明)
# 码位以 Unicode 权威表为准（unicodedata.name 校对）：
#   ガ30AC ギ30AE グ30B0 ゲ30B2 ゴ30B4 ザ30B6 ジ30B8 ズ30BA ゼ30BC ゾ30BE
#   ダ30C0 ヂ30C2 ヅ30C5 デ30C7 ド30C9 バ30D0 ビ30D3 ブ30D6 ベ30D9 ボ30DC
VOICED: list[tuple[int, int, str]] = [
    (0x30AC, 0x30AB, "ガ"),
    (0x30AE, 0x30AD, "ギ"),
    (0x30B0, 0x30AF, "グ"),
    (0x30B2, 0x30B1, "ゲ"),
    (0x30B4, 0x30B3, "ゴ"),
    (0x30B6, 0x30B5, "ザ"),
    (0x30B8, 0x30B7, "ジ"),
    (0x30BA, 0x30B9, "ズ"),
    (0x30BC, 0x30BB, "ゼ"),
    (0x30BE, 0x30BD, "ゾ"),
    (0x30C0, 0x30BF, "ダ"),
    (0x30C2, 0x30C1, "ヂ"),
    (0x30C5, 0x30C4, "ヅ"),
    (0x30C7, 0x30C6, "デ"),
    (0x30C9, 0x30C8, "ド"),
    (0x30D0, 0x30CF, "バ"),
    (0x30D3, 0x30D2, "ビ"),
    (0x30D6, 0x30D5, "ブ"),
    (0x30D9, 0x30D8, "ベ"),
    (0x30DC, 0x30DB, "ボ"),
]

# 半浊音形：码位 -> (基础形码位, 说明)
#   パ30D1 ピ30D4 プ30D7 ペ30DA ポ30DD
SEMI_VOICED: list[tuple[int, int, str]] = [
    (0x30D1, 0x30CF, "パ"),
    (0x30D4, 0x30D2, "ピ"),
    (0x30D7, 0x30D5, "プ"),
    (0x30DA, 0x30D8, "ペ"),
    (0x30DD, 0x30DB, "ポ"),
]

# 反复记号
ITERATION: list[tuple[int, str, list]] = [
    (0x30FD, "ヽ：单笔右上斜画（重复形）", [
        ("D", 330, 600, 620, 300, W_SEC),
    ]),
    (0x30FE, "ヾ：ヽ 重复两画", [
        ("D", 300, 600, 570, 330, W_SEC),
        ("D", 470, 600, 740, 330, W_SEC),
    ]),
]


# ---------------------------------------------------------------------------
# wave2 返工：新增 20 字（此前不在字体里，渲染成豆腐块）
# ---------------------------------------------------------------------------

# 新增浊音/半浊音组合形（全尺寸底字 + 右上记号，与既有 25 个浊音形同一套做法）
NEW_VOICED: list[tuple[int, int, str, list]] = [
    (0x30F4, 0x30A6, "ヴ", []),        # ウ + 浊点
    (0x30F7, 0x30EF, "ヷ", []),        # ワ + 浊点
    (0x30F8, 0x30EF, "ヸ", []),        # ワ + 半浊点
    (0x30F9, 0x30F2, "ヹ", []),        # ヲ + 浊点
    (0x30FA, 0x30F2, "ヺ", []),        # ヲ + 半浊点
]

# 新增全尺寸符号字（直接按最终尺寸画，不再参与放大）
NEW_SYMBOL: dict[int, tuple[str, list]] = {
    0x30A0: ("゠：双横线（double hyphen），两条平行短横杠居中", [
        ("H", 305, 695, 450, W_THIN),
        ("H", 305, 695, 300, W_THIN),
    ]),
    0x30FB: ("・：片假名中点，居中斜切平行四边形（非句点）", [
        ("DOT", 487, 380, 140, 170, 26),
    ]),
    0x30FF: ("ヿ：片假名双字（ノ + 丶），上端横折接长斜笔", [
        ("H", 360, 780, 720, W_SEC),
        ("D", 780, 720, 300, 50, W_MAIN),
    ]),
}

# 小假名：字高约为全尺寸片假名的 0.70 倍，位于 em 右上区域；ッ 横向居中、纵向偏下。
# 下列坐标是**最终尺寸坐标**（已按最终尺寸另行绘制，不参与全尺寸的 ×1.30 放大）。
# wave2 v2：权重加粗后墨迹外扩，落位（中心 x=500 / 底边 y=40）在 build() 里重新对齐。
# 项 = (字符, 基础形, 说明, 笔画表)
NEW_SMALL: dict[int, tuple[str, str, str, list]] = {
    0x30A1: ("ァ", "ア", "水平居中·贴基线", [
        ("H", 370, 717, 474, W_THIN),
        ("D", 717, 474, 500, 283, W_THIN),
        ("D", 292, 578, 691, 67, W_SEC),
    ]),
    0x30A3: ("ィ", "イ", "水平居中·贴基线", [
        ("D", 638, 573, 362, 358, W_SEC),
        ("V", 594, 40, 573, W_SEC),
    ]),
    0x30A5: ("ゥ", "ウ", "水平居中·贴基线；字高 = 全尺寸片假名字高中位 ×0.70（wave2 v2 放大）", [
        ("DOT", 276, 352, 90, 88, 26),
        ("H", 357, 732, 283, W_SEC),
        ("D", 732, 283, 520, 71, W_SEC),
    ]),
    0x30A7: ("ェ", "エ", "水平居中·贴基线", [
        ("H", 237, 763, 576, W_SEC),
        ("V", 549, 84, 576, W_SEC),
        ("H", 336, 549, 330, W_THIN),
        ("H", 237, 763, 84, W_SEC),
    ]),
    0x30A9: ("ォ", "オ", "水平居中·贴基线", [
        ("H", 256, 718, 564, W_SEC),
        ("V", 487, 40, 600, W_SEC),
        ("D", 718, 564, 309, 191, W_THIN),
    ]),
    0x30C3: ("ッ", "ツ", "水平居中·贴基线", [
        ("D", 250, 398, 348, 463, W_TICK_SM),
        ("D", 225, 283, 323, 349, W_TICK_SM),
        ("D", 372, 488, 766, 70, W_SEC),
    ]),
    0x30E3: ("ャ", "ヤ", "水平居中·贴基线", [
        ("H", 272, 671, 539, W_SEC),
        ("D", 688, 574, 422, 60, W_SEC),
    ]),
    0x30E5: ("ュ", "ユ", "水平居中·贴基线", [
        ("D", 266, 484, 439, 539, W_THIN),
        ("H", 302, 703, 393, W_SEC),
        ("V", 703, 84, 393, W_SEC),
        ("H", 284, 703, 84, W_SEC),
    ]),
    0x30E7: ("ョ", "ヨ", "水平居中·贴基线", [
        ("V", 317, 57, 556, W_SEC),
        ("H", 317, 620, 556, W_SEC),
        ("H", 317, 673, 316, W_SEC),
        ("H", 317, 726, 84, W_SEC),
    ]),
    0x30EE: ("ヮ", "ワ", "水平居中·贴基线", [
        ("DOT", 293, 521, 90, 128, 26),
        ("H", 275, 712, 512, W_SEC),
        ("D", 712, 512, 393, 66, W_SEC),
    ]),
    0x30F5: ("ヵ", "カ", "水平居中·贴基线", [
        ("H", 288, 726, 498, W_SEC),
        ("D", 726, 498, 602, 52, W_SEC),
        ("D", 560, 564, 264, 135, W_THIN),
    ]),
    0x30F6: ("ヶ", "ケ", "水平居中·贴基线", [
        ("D", 306, 410, 425, 572, W_THIN),
        ("H", 281, 705, 427, W_THIN),
        ("D", 688, 572, 391, 62, W_SEC),
    ]),
}

# 右上角浊音记号：两枚**斜切平行四边形**（汉字 g.dot(..., slant=26) 的语言）。
# 全字族统一（GLY-004）：同一枚记号在任何字里形状完全一样。
# 两枚之间留出 30 单位左右的净空，不与基字相交（浊点让位）。
DAKUTEN: list = [
    ("DOT", 790, 650, 64, 112, 26),
    ("DOT", 878, 630, 64, 112, 26),
]

# 右上角半浊音记号：一枚斜切平行四边形，与浊点同一套语言（GLY-004）
HANDAKUTEN: list = [
    ("DOT", 840, 650, 80, 100, 26),
]


# ---------------------------------------------------------------------------
# 坐标变换工具：只动中心线坐标，笔画权重一律不变
# ---------------------------------------------------------------------------
def _sx(x: float, ax: float, s: float) -> int:
    return int(round(ax + (x - ax) * s))


def _sy(y: float, ay: float, s: float) -> int:
    return int(round(ay + (y - ay) * s))


def _scale_about(strokes: list, s: float, about: tuple[float, float]) -> list:
    """围绕 about 均匀缩放中心线坐标（权重 / 半径不变）。"""
    ax, ay = about
    out = []
    for st in strokes:
        k = st[0]
        if k == "H":
            out.append(("H", _sx(st[1], ax, s), _sx(st[2], ax, s), _sy(st[3], ay, s), st[4]))
        elif k == "V":
            out.append(("V", _sx(st[1], ax, s), _sy(st[2], ay, s), _sy(st[3], ay, s), st[4]))
        elif k == "D":
            out.append(("D", _sx(st[1], ax, s), _sy(st[2], ay, s),
                        _sx(st[3], ax, s), _sy(st[4], ay, s), st[5]))
        elif k == "DOT":
            # 点/记号：w 与 slant 是绝对量（宽度档 / 汉字倾切角度档），只有高度 h 随缩放走
            out.append(("DOT", _sx(st[1], ax, s), _sy(st[2], ay, s),
                        st[3], int(round(st[4] * s)), st[5]))
        else:
            out.append(st)
    return out


def _translate(strokes: list, dx: float, dy: float) -> list:
    """整体平移中心线坐标。"""
    out = []
    for st in strokes:
        k = st[0]
        if k == "H":
            out.append(("H", st[1] + int(round(dx)), st[2] + int(round(dx)),
                        st[3] + int(round(dy)), st[4]))
        elif k == "V":
            out.append(("V", st[1] + int(round(dx)), st[2] + int(round(dy)),
                        st[3] + int(round(dy)), st[4]))
        elif k == "D":
            out.append(("D", st[1] + int(round(dx)), st[2] + int(round(dy)),
                        st[3] + int(round(dx)), st[4] + int(round(dy)), st[5]))
        elif k == "DOT":
            out.append(("DOT", st[1] + int(round(dx)), st[2] + int(round(dy)),
                        st[3], st[4], st[5]))
        else:
            out.append(st)
    return out


def _ink_box(strokes: list) -> tuple[float, float, float, float]:
    """按笔画描述符解析墨迹外接框（与 hkbuild 的画法一致）。"""
    xs: list[float] = []
    ys: list[float] = []
    for st in strokes:
        k = st[0]
        if k == "H":
            x1, x2, y, w = st[1], st[2], st[3], st[4]
            xs += [min(x1, x2), max(x1, x2)]
            ys += [y - w / 2.0, y + w / 2.0]
        elif k == "V":
            x, y1, y2, w = st[1], st[2], st[3], st[4]
            xs += [x - w / 2.0, x + w / 2.0]
            ys += [min(y1, y2), max(y1, y2)]
        elif k == "D":
            x1, y1, x2, y2, w = st[1], st[2], st[3], st[4], st[5]
            dx, dy = x2 - x1, y2 - y1
            length = math.hypot(dx, dy) or 1.0
            nx, ny = -dy / length * w / 2.0, dx / length * w / 2.0
            for px, py in ((x1, y1), (x2, y2)):
                xs += [px + nx, px - nx]
                ys += [py + ny, py - ny]
        elif k == "DOT":
            cx, cy, w, h, slant = st[1], st[2], st[3], st[4], st[5]
            # 斜切平行四边形：上下边水平，顶边相对底边右移 slant
            xs += [cx - w / 2.0, cx + w / 2.0,
                   cx - w / 2.0 + slant, cx + w / 2.0 + slant]
            ys += [cy - h / 2.0, cy + h / 2.0]
    return (min(xs), min(ys), max(xs), max(ys))


def _fits(strokes: list) -> bool:
    """墨迹是否落在 x 60..940 / y 0..820 之内。"""
    x0, y0, x1, y1 = _ink_box(strokes)
    return ((x1 - x0) <= (FRAME_X1 - FRAME_X0)
            and (y1 - y0) <= FRAME_H_MAX
            and x0 >= FRAME_X0 and x1 <= FRAME_X1
            and y0 >= FRAME_Y0 and y1 <= FRAME_Y1)


def _fit_scale(strokes: list, center: tuple[float, float], s_max: float) -> float:
    """在 [0, s_max] 内二分出「放大后仍落在框内」的最大系数。"""
    lo, hi = 0.0, s_max
    for _ in range(24):
        mid = (lo + hi) / 2.0
        if _fits(_scale_about(strokes, mid, center)):
            lo = mid
        else:
            hi = mid
    return lo


def _enlarge(strokes: list) -> list:
    """全尺寸片假名：围绕自身墨迹外接框中心 ×1.30，再把墨迹中心对到 (500, 400)。

    权重不动，故只缩放中心线坐标；斜笔/横笔的外扩量随方向不变而保持不变，
    因此放大后要**重新量**墨迹外接框再对中（不能直接按比例推算）。
    放大后越框的字按可用空间等比回退该字的系数（_fit_scale）。
    """
    x0, y0, x1, y1 = _ink_box(strokes)
    cx, cy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    s = _fit_scale(strokes, (cx, cy), KATA_SCALE)
    moved = _scale_about(strokes, s, (cx, cy))
    nx0, ny0, nx1, ny1 = _ink_box(moved)
    return _translate(moved, _CX - (nx0 + nx1) / 2.0, _CY - (ny0 + ny1) / 2.0)


def _voice_form(base_strokes: list, marks: list) -> list:
    """浊音/半浊音形：放大的基础形缩到 0.84，右缘对到 735，右上加记号。"""
    big = _enlarge(base_strokes)
    x0, y0, x1, y1 = _ink_box(big)
    cx, cy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    s = _VOICE_SCALE
    small = _scale_about(big, s, (cx, cy))
    box = _ink_box(small)
    w = box[2] - box[0]
    if w > (_VOICE_RIGHT - FRAME_X0):
        s = s * (_VOICE_RIGHT - FRAME_X0) / w
        small = _scale_about(big, s, (cx, cy))
        box = _ink_box(small)
    small = _translate(small, _VOICE_RIGHT - box[2], 0.0)
    return small + marks


def _full_size_kata_heights() -> list[float]:
    """全尺寸片假名（含浊音/半浊音形）的墨迹高度 —— 小假名定尺的基准。

    与 check_kana_size.py 的「全尺寸假名」口径一致：浊音形算它带记号后的整体高度。
    """
    hs: list[float] = []
    for cp in sorted(BASE):
        _, strokes = BASE[cp]
        b = _ink_box(_enlarge(strokes))
        hs.append(b[3] - b[1])
    for group in (VOICED, SEMI_VOICED):
        for _cp, base_cp, _label in group:
            _, strokes = BASE[base_cp]
            b = _ink_box(_voice_form(strokes, DAKUTEN))
            hs.append(b[3] - b[1])
    for cp, base_cp, _label, _ in NEW_VOICED:
        _, strokes = BASE[base_cp]
        marks = HANDAKUTEN if cp in (0x30F8, 0x30FA) else DAKUTEN
        b = _ink_box(_voice_form(strokes, marks))
        hs.append(b[3] - b[1])
    return hs


def _scale_small(strokes: list, target_h: float) -> list:
    """把小假名的中心线坐标放大到目标字高（笔画权重不变，只改大小）。

    以墨迹底边中心为支点等比缩放中心线坐标；墨迹高度随系数单调递增，二分求解。
    """
    x0, y0, x1, y1 = _ink_box(strokes)
    pivot = ((x0 + x1) / 2.0, y0)
    lo, hi = 0.2, 4.0
    for _ in range(48):
        mid = (lo + hi) / 2.0
        b = _ink_box(_scale_about(strokes, mid, pivot))
        if (b[3] - b[1]) < target_h:
            lo = mid
        else:
            hi = mid
    return _scale_about(strokes, (lo + hi) / 2.0, pivot)


def _place_small(strokes: list) -> list:
    """小假名落位：水平居中（中心 x=500）+ 贴基线（底边 y=40）。"""
    x0, y0, x1, y1 = _ink_box(strokes)
    return _translate(strokes, SMALL_CX - (x0 + x1) / 2.0, SMALL_BOTTOM - y0)


def _render(name: str, codepoint: int, strokes: list, note: str) -> Glyph:
    g = Glyph(name, advance=1000, unicode=codepoint, note=note)
    for st in strokes:
        k = st[0]
        if k == "H":
            g.hbar(st[1], st[2], st[3], weight=st[4])
        elif k == "V":
            g.vbar(st[1], st[2], st[3], weight=st[4])
        elif k == "D":
            g.diag(st[1], st[2], st[3], st[4], weight=st[5])
        elif k == "DOT":
            g.dot(st[1], st[2], w=st[3], h=st[4], slant=st[5])
    return g


def build() -> list[Glyph]:
    glyphs: list[Glyph] = []
    # 1) 基础 48：字面放大到与汉字同族（只改坐标，不改骨架与权重）
    for cp in sorted(BASE):
        note, strokes = BASE[cp]
        glyphs.append(_render(
            f"uni{cp:04X}", cp, _enlarge(strokes),
            f"{note}（字面 ×1.30，与汉字同族）",
        ))
    # 2) 浊音形 20
    for cp, base_cp, label in VOICED:
        note, strokes = BASE[base_cp]
        glyphs.append(_render(
            f"uni{cp:04X}", cp, _voice_form(strokes, DAKUTEN),
            f"{label}：{note}（浊音形，基础形缩放并左移，右上加浊音符）",
        ))
    # 3) 半浊音形 5
    for cp, base_cp, label in SEMI_VOICED:
        note, strokes = BASE[base_cp]
        glyphs.append(_render(
            f"uni{cp:04X}", cp, _voice_form(strokes, HANDAKUTEN),
            f"{label}：{note}（半浊音形，基础形缩放并左移，右上加圆点记号）",
        ))
    # 4) 反复记号 2（字面同样放大，与字体其余部分同族）
    for cp, note, strokes in ITERATION:
        glyphs.append(_render(f"uni{cp:04X}", cp, _enlarge(strokes), f"{note}（字面 ×1.30）"))
    # 5) wave2 新增：浊音/半浊音组合形 5（与既有浊音形同一套做法）
    for cp, base_cp, label, _ in NEW_VOICED:
        note, strokes = BASE[base_cp]
        marks = HANDAKUTEN if cp in (0x30F8, 0x30FA) else DAKUTEN
        glyphs.append(_render(
            f"uni{cp:04X}", cp, _voice_form(strokes, marks),
            f"{label}：{note}（wave2 新增，浊音形，基础形缩放并左移，右上加记号）",
        ))
    # 6) wave2 新增：全尺寸符号字 3（直接按最终尺寸画）
    for cp in sorted(NEW_SYMBOL):
        note, strokes = NEW_SYMBOL[cp]
        glyphs.append(_render(f"uni{cp:04X}", cp, strokes, f"{note}（wave2 新增）"))
    # 7) wave2 v2：小假名 12（另画，em 右上区域；ッ 横向居中、纵向偏下）
    #    加粗后墨迹外扩 -> 重新「水平居中 + 贴基线」；
    #    ゥ（U+30A5）另按「全尺寸片假名字高中位 ×0.70」放大（骨架拆法不变）。
    med_h = statistics.median(_full_size_kata_heights())
    for cp in sorted(NEW_SMALL):
        label, base_label, desc, strokes = NEW_SMALL[cp]
        if cp == 0x30A5:
            strokes = _scale_small(strokes, U_SMALL_RATIO * med_h)
        strokes = _place_small(strokes)
        b = _ink_box(strokes)
        glyphs.append(_render(
            f"uni{cp:04X}", cp, strokes,
            f"{label}：小假名，由 {base_label} 另行绘制（wave2 v2 加粗，字高 {b[3] - b[1]:.0f}，{desc}）",
        ))
    return glyphs


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-kana-kata.ufo"


if __name__ == "__main__":
    gs = build()
    write_ufo(target_ufo(), gs)
    print(f"[recipe] 已写出 {target_ufo()}（{len(gs)} 字形）")
