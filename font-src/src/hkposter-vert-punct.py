"""HK Poster Heavy —— wave1/vert-punct：日文竖排（縦書き）标点替代形态。

任务
----
横排 CJK 标点已经做好（font-src/src/hkposter-latin-punct.py）。竖排与横排的差异
只在「位置」与「朝向」，**墨形本身不变**——所以本 lane 的每一个替代字形，都是把
横排字形的同一套轮廓做 90° 旋转 / 平移得到的，绝不重新画一遍笔画。这样竖排与横排
的同一字符粗细天然同族（family 一致性），不会出现「竖排比横排粗/细」。

三类处理规则
------------
1. 句读点（、 。 ， ； ：）——横排在字面左下，竖排移到字面右上；
   其中 、 ： ； 还要整体旋转 90°（顺时针），让笔画朝向随行文方向改变；
   。 是圆点、， 在竖排里保持直立（与句号同位），故只平移不旋转。
2. 括号类（「 」 【 】 （ ））——整体旋转 90°（顺时针）：开口方向随行文方向
   （竖排自上而下）改变：前括号开口朝下、落在字面**下**部去贴后面的内容；
   后括号开口朝上、落在字面**上**部去贴前面的内容。
3. 长音符 ー 与波浪号 〜——横排横着，竖排竖着（同样是 90° 旋转）。

参考依据（实测，不是印象）
--------------------------
Windows 自带 MS Gothic（msgothic.ttc，256 upem）的 GSUB `vert` 特性带一套日文
竖排替代字形。本 lane 的位置与朝向全部按它反推，实测墨形框见 MS_VERT_BOX：

* 句读点落在字面右上（例：。vert 的墨形 x 672..953/1000、y 645..927/1000）；
* 前括号（【（「）在字面**下**部、开口朝下；后括号（】）「）在字面**上**部、
  开口朝上；
* ー 在竖排是居中的竖条，〜 在竖排是竖直波形；
* ！与？ 在 MS Gothic 里**没有** vert 替代（竖排里保持直立），本 lane 同此。

与横排 recipe 的关系
--------------------
本 recipe 在运行时 import 横排 recipe（font-src/src/hkposter-latin-punct.py），
直接取它的字形对象做旋转 / 平移：

* 好处：竖排墨形永远与横排一致；横排 lane 改了形状，竖排跟着变，不会不同步；
* 代价：横排 lane 改了墨形后，本 lane 的 .ufo 需要重新生成
  （python font-src/src/hkposter-vert-punct.py），否则 check_recipes.py 会报不同步。

本 lane 独家提供的基础字形
--------------------------
U+30FC（ー）与 U+301C（〜）在既有 master 里根本不存在，而 vert 特性的 `sub`
两侧字形都必须真实存在（否则 ufo2ft 编译失败），所以这两个**横排基础字形**由本
lane 一并做出（uni30FC / uni301C），它们的竖排形态是同一套墨形的 90° 旋转。

运行：python font-src/src/hkposter-vert-punct.py
"""

from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, ellipse_points, write_ufo  # noqa: E402

# ---- 冻结笔画权重（与横排标点一致：主 96 / 次 92 / 细 84）----
W_MAIN = 96
W_SECOND = 92
W_THIN = 84

# ---- 全角版面（advance 1000，字面框 x 60..940 / y 0..820）----
CJK_ADV = 1000
BODY_L, BODY_R = 60, 940
BODY_B, BODY_T = 0, 820

# ---- MS Gothic（256 upem）竖排替代字形的实测墨形框 ----
# 取值方式：fontTools 读 msgothic.ttc 的 GSUB `vert` 映射，逐个取替代字形的
# BoundsPen 包围盒。MS Gothic 的表意字面框按 x 0..256 / y -28..228 计。
MS_UPEM = 256
MS_EM_BOTTOM = -28
MS_VERT_BOX = {
    "uni3001": (175, 145, 244, 205),   # 、
    "uni3002": (172, 137, 244, 209),   # 。
    "uniFF0C": (210, 142, 233, 191),   # ，
    "uniFF1A": (77, 82, 193, 104),     # ：
    "uni300C": (65, -15, 244, 60),     # 「
    "uni300D": (11, 125, 190, 200),    # 」
    "uni3010": (11, -16, 243, 61),     # 【
    "uni3011": (11, 124, 243, 201),    # 】
    "uniFF08": (14, -15, 234, 46),     # （
    "uniFF09": (14, 139, 234, 200),    # ）
    "uni30FC": (117, -20, 144, 206),   # ー
    "uni301C": (98, -10, 157, 194),    # 〜
}

# --------------------------------------------------------------------------


def load_horizontal_recipe():
    """加载横排标点 recipe（只取它的字形对象，不修改它）。"""
    path = FONT_SRC / "src" / "hkposter-latin-punct.py"
    spec = importlib.util.spec_from_file_location("hkposter_latin_punct", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["hkposter_latin_punct"] = module
    spec.loader.exec_module(module)
    return module


HORIZONTAL = {g.name: g for g in load_horizontal_recipe().build()}


# --------------------------------------------------------------------------
# 几何工具
# --------------------------------------------------------------------------
def ms_box(name: str) -> tuple[float, float, float, float]:
    """MS Gothic 的竖排墨形框 → 本字体字面框坐标（按比例换算）。"""
    x0, y0, x1, y1 = MS_VERT_BOX[name]
    scale_x = (BODY_R - BODY_L) / MS_UPEM
    scale_y = (BODY_T - BODY_B) / MS_UPEM
    return (
        BODY_L + x0 * scale_x,
        BODY_B + (y0 - MS_EM_BOTTOM) * scale_y,
        BODY_L + x1 * scale_x,
        BODY_B + (y1 - MS_EM_BOTTOM) * scale_y,
    )


def ms_center(name: str) -> tuple[float, float]:
    """MS Gothic 竖排墨形框的中心 → 本字体字面框坐标。"""
    x0, y0, x1, y1 = ms_box(name)
    return (x0 + x1) / 2, (y0 + y1) / 2


def ms_corner(name: str, corner: str) -> tuple[float, float]:
    """MS Gothic 竖排墨形框的某个角 → 本字体字面框坐标。"""
    x0, y0, x1, y1 = ms_box(name)
    if corner == "br":
        return x1, y0
    if corner == "tl":
        return x0, y1
    raise ValueError(f"未知角点 {corner}")


def rings_bbox(rings) -> tuple[float, float, float, float]:
    xs = [point[0] for ring in rings for point in ring]
    ys = [point[1] for ring in rings for point in ring]
    return min(xs), min(ys), max(xs), max(ys)


def rotate_cw(ring, cx: float, cy: float):
    """把一个轮廓环绕 (cx,cy) 顺时针旋转 90°（视觉顺时针，y 向上）。"""
    return [(cx + (y - cy), cy - (x - cx)) for (x, y) in ring]


def vertical_variant(
    base: Glyph,
    name: str,
    *,
    rotate: bool,
    anchor: tuple,
    target: tuple[float, float],
    note: str,
) -> Glyph:
    """由横排字形生成竖排替代字形。

    rotate=True  —— 整体顺时针旋转 90°（绕墨形包围盒中心）；
    anchor       —— 定位基准：
        ("identity",)    原样不动（竖排里保持直立的字形用）
        ("center",)      变换后包围盒的中心
        ("bbox_br",)     变换后包围盒的右下角
        ("bbox_tl",)     变换后包围盒的左上角
        ("point", x, y)  横排字形里指定的点（随墨形一起变换）
    target       —— 基准点变换后要落到的位置（identity 基准忽略）。
    """
    rings = base.contours()
    if not rings:
        raise ValueError(f"{base.name}：没有轮廓可变换")

    pivot = None
    if rotate:
        x0, y0, x1, y1 = rings_bbox(rings)
        pivot = ((x0 + x1) / 2, (y0 + y1) / 2)
        rings = [rotate_cw(ring, pivot[0], pivot[1]) for ring in rings]

    x0, y0, x1, y1 = rings_bbox(rings)
    kind = anchor[0]
    if kind == "identity":
        dx = dy = 0.0
    else:
        if kind == "center":
            ax, ay = (x0 + x1) / 2, (y0 + y1) / 2
        elif kind == "bbox_br":
            ax, ay = x1, y0
        elif kind == "bbox_tl":
            ax, ay = x0, y1
        elif kind == "point":
            px, py = anchor[1], anchor[2]
            if pivot is not None:
                (ax, ay), = rotate_cw([(px, py)], pivot[0], pivot[1])
            else:
                ax, ay = px, py
        else:
            raise ValueError(f"未知基准 {kind}")
        dx = target[0] - ax
        dy = target[1] - ay

    glyph = Glyph(name, advance=CJK_ADV, unicode=None, note=note)
    for ring in rings:
        glyph.poly([(x + dx, y + dy) for (x, y) in ring])
    return glyph


# --------------------------------------------------------------------------
# 本 lane 独家制作的基础字形（ー / 〜）
# --------------------------------------------------------------------------
def wave_ribbon(
    glyph: Glyph,
    x0: float,
    x1: float,
    y_mid: float,
    amp: float,
    weight: float,
    phase: float = 0.2,
    steps: int = 24,
) -> None:
    """正弦波带：上缘 + 下缘（反向）闭合成一个简单多边形。

    与 MS Gothic 的实测比例对齐：波形中心线振幅 ≈ 字面框高度的 7%，
    带厚 = weight（细档 84）。波峰在 20% 处、波谷在 70% 处——与实测的
    「左高、右低、再抬起」的 〜 一致。
    """
    top: list[tuple[float, float]] = []
    bottom: list[tuple[float, float]] = []
    for index in range(steps + 1):
        t = index / steps
        x = x0 + (x1 - x0) * t
        y = y_mid + amp * math.cos(2 * math.pi * (t - phase))
        top.append((x, y + weight / 2))
        bottom.append((x, y - weight / 2))
    glyph.poly(top + list(reversed(bottom)))


def fw_prolonged_sound_mark() -> Glyph:
    """ー U+30FC 长音符（横排）：贯穿字面宽度的水平细杠。

    长度取 820（= 字面框高度），这样竖排形态是同一根杠的精确 90° 旋转，
    竖起来正好贯穿一个字面高度。
    """
    g = Glyph("uni30FC", advance=CJK_ADV, unicode=0x30FC, note="ー：长音符（横排）")
    g.hbar(90, 910, 388, weight=W_THIN)
    return g


def fw_wave_dash() -> Glyph:
    """〜 U+301C 波浪号（横排）：一条正弦波带。"""
    g = Glyph("uni301C", advance=CJK_ADV, unicode=0x301C, note="〜：波浪号")
    wave_ribbon(g, x0=90, x1=910, y_mid=388, amp=58, weight=W_THIN)
    return g


# --------------------------------------------------------------------------
# 15 个竖排替代字形
# --------------------------------------------------------------------------
def build() -> list[Glyph]:
    """返回本 lane 的全部字形（15 个 .vert 替代形 + 2 个横排基础字形）。"""
    glyphs: list[Glyph] = []

    # ---- 句读点：移到字面右上 ----
    # 。 圆点：只平移，圆头落在句号该在的位置（右上）。
    period_box = ms_center("uni3002")
    glyphs.append(
        vertical_variant(
            HORIZONTAL["uni3002"],
            "uni3002.vert",
            rotate=False,
            anchor=("point", 250, 100),   # 圆点中心
            target=period_box,
            note="。竖排：圆点移到字面右上",
        )
    )

    # ， 逗号：整体顺时针 90°（尾锋由左下改为左上，指向竖排的前一个字），
    # 圆头与句号圆点同位。
    glyphs.append(
        vertical_variant(
            HORIZONTAL["uniFF0C"],
            "uniFF0C.vert",
            rotate=True,
            anchor=("point", 272, 150),   # 圆头中心
            target=period_box,
            note="，竖排：尾锋朝左上，圆头在字面右上",
        )
    )

    # 、 顿号：顺时针 90°（笔锋由左下改为左上），整体落在字面右上。
    glyphs.append(
        vertical_variant(
            HORIZONTAL["uni3001"],
            "uni3001.vert",
            rotate=True,
            anchor=("center",),
            target=ms_center("uni3001"),
            note="、竖排：旋转 90°，落在字面右上",
        )
    )

    # ： 冒号：顺时针 90°（上下两点变成左右两点），位置取 MS 实测。
    glyphs.append(
        vertical_variant(
            HORIZONTAL["uniFF1A"],
            "uniFF1A.vert",
            rotate=True,
            anchor=("center",),
            target=ms_center("uniFF1A"),
            note="：竖排：两点横排，落在字面中部",
        )
    )

    # ； 分号：顺时针 90°（上点变右点、下逗号变左逗号，尾锋朝左上）。
    glyphs.append(
        vertical_variant(
            HORIZONTAL["uniFF1B"],
            "uniFF1B.vert",
            rotate=True,
            anchor=("center",),
            target=ms_center("uniFF1A"),
            note="；竖排：旋转 90°，与冒号同位",
        )
    )

    # ！ 与 ？：竖排里保持直立（MS Gothic 也没有 vert 替代），故墨形原地不动。
    glyphs.append(
        vertical_variant(
            HORIZONTAL["uniFF01"],
            "uniFF01.vert",
            rotate=False,
            anchor=("identity",),
            target=(0, 0),
            note="！竖排：保持直立不变",
        )
    )
    glyphs.append(
        vertical_variant(
            HORIZONTAL["uniFF1F"],
            "uniFF1F.vert",
            rotate=False,
            anchor=("identity",),
            target=(0, 0),
            note="？竖排：保持直立不变",
        )
    )

    # ---- 括号类：整体顺时针 90°，开口方向随行文方向 ----
    # 前括号：开口朝下、落在字面下部（去贴后面的内容）。
    glyphs.append(
        vertical_variant(
            HORIZONTAL["uni300C"],
            "uni300C.vert",
            rotate=True,
            anchor=("bbox_br",),
            target=ms_corner("uni300C", "br"),
            note="「竖排：旋转 90°，开口朝下，落在字面下部",
        )
    )
    glyphs.append(
        vertical_variant(
            HORIZONTAL["uni3010"],
            "uni3010.vert",
            rotate=True,
            anchor=("bbox_br",),
            target=ms_corner("uni3010", "br"),
            note="【竖排：旋转 90°，开口朝下，落在字面下部",
        )
    )
    glyphs.append(
        vertical_variant(
            HORIZONTAL["uniFF08"],
            "uniFF08.vert",
            rotate=True,
            anchor=("bbox_br",),
            target=ms_corner("uniFF08", "br"),
            note="（竖排：旋转 90°，开口朝下，落在字面下部",
        )
    )

    # 后括号：开口朝上、落在字面上部（去贴前面的内容）。
    glyphs.append(
        vertical_variant(
            HORIZONTAL["uni300D"],
            "uni300D.vert",
            rotate=True,
            anchor=("bbox_tl",),
            target=ms_corner("uni300D", "tl"),
            note="」竖排：旋转 90°，开口朝上，落在字面上部",
        )
    )
    glyphs.append(
        vertical_variant(
            HORIZONTAL["uni3011"],
            "uni3011.vert",
            rotate=True,
            anchor=("bbox_tl",),
            target=ms_corner("uni3011", "tl"),
            note="】竖排：旋转 90°，开口朝上，落在字面上部",
        )
    )
    glyphs.append(
        vertical_variant(
            HORIZONTAL["uniFF09"],
            "uniFF09.vert",
            rotate=True,
            anchor=("bbox_tl",),
            target=ms_corner("uniFF09", "tl"),
            note="）竖排：旋转 90°，开口朝上，落在字面上部",
        )
    )

    # ---- 长音符 / 波浪号：由本 lane 独家制作的基础字形旋转而来 ----
    glyphs.append(
        vertical_variant(
            fw_prolonged_sound_mark(),
            "uni30FC.vert",
            rotate=True,
            anchor=("center",),
            target=ms_center("uni30FC"),
            note="ー竖排：竖直长条",
        )
    )
    glyphs.append(
        vertical_variant(
            fw_wave_dash(),
            "uni301C.vert",
            rotate=True,
            anchor=("center",),
            target=ms_center("uni301C"),
            note="〜竖排：竖直波形",
        )
    )

    # ---- 横排基础字形（本 lane 独家提供）----
    glyphs.append(fw_prolonged_sound_mark())
    glyphs.append(fw_wave_dash())

    return glyphs


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-vert-punct.ufo"


if __name__ == "__main__":
    _target = target_ufo()
    _target.parent.mkdir(parents=True, exist_ok=True)
    write_ufo(_target, build())
    print(f"[recipe] 已写出 {_target}")
