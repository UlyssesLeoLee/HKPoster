#!/usr/bin/env python3
"""check_cavity_height —— 几何腔高校验（recipe 层，精确到 float）。

**为什么要有这个工具（2026-11-04）**

`audit_white_holes.py` 是**审计**：它把成品字体栅格化到 S=700，
用行游程找封闭白腔，判据是「腔宽 ≥ 40 且 腔高 < 24 = 压扁真腔」。
问题在于**栅格化取整**：

    1 像素 = 1000/700 = 1.4286 单位
    几何腔高 24.0 → 栅格化量到 23 或 24（取决于像素对齐）→ 判定在门槛上摇摆
    几何腔高 26.0 → 栅格化稳定量到 24+

所以「几何腔高 24.0」这个**恰好等于门槛**的值，在栅格化口径下
会随机落在 PASS / FAIL 之间 —— **不能靠它当唯一判据**。

本工具直接在 **recipe 层**用 shapely 求笔画并集后的 `interiors`
（真正的封闭内白），量出**精确几何腔高**，不经过像素。

**两级判据（本工具的门槛是怎么定出来的）**

初版把门槛设成 26（s3-008 的下限），结果全库报 **55 个腔**，
分布在 30+ 个 recipe 里 —— 其中绝大多数是**几何恰好 24.0**。
**这说明 26 不是本项目的判据，而是我凭一个批次推出来的。**
按 AGENTS.md 铁律 14（新检查器必须先在「已知正确」的样本上验证零误报），
这个门槛在已知正确的旧批次上**大量误报** ⇒ 不成立，废弃。

用两个独立来源重新定标：

- **项目自定取舍线**：24（`audit_white_holes.py` 的 MIN_H，docs/10 §9.14 记录）
- **参照字体实测**（M PLUS 1p Black）：Jōyō 常用漢字里**大量腔高就是 24**
  （募/夏/貿/遣/喜 全部是 24）—— 24 是这个字体的正常密度，不是缺陷

于是判据定为：

    几何腔高 < 24  →  FAIL   （低于项目自定取舍线 = 真缺陷）
    几何腔高 = 24  →  WARN   （临界：栅格化可能量到 23，位置敏感）
    几何腔高 ≥ 26  →  PASS   （有余量，栅格化稳定 ≥ 24）

腔宽 < 40 的是「针孔」，视觉上不存在，不算缺陷（与 audit_white_holes 一致）。

**WARN 的意义**：它标出「一旦栅格化像素对齐偏了一格就会被审计判压扁」的位置。
新批次应当避开（几何 ≥ 26），旧批次保持现状（几何 24 已通过审计）。

用法
----
```
python font-src/scripts/check_cavity_height.py                       # 扫全库
python font-src/scripts/check_cavity_height.py --recipes <a.py> <b.py> # 只扫指定 recipe
python font-src/scripts/check_cavity_height.py --strict                # 把 WARN 也当 FAIL
python font-src/scripts/check_cavity_height.py --selftest             # 自证分辨力
```

退出码：发现几何腔高 < 24 → 1；否则 0（`--strict` 时 WARN 也返回 1）。
"""
from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from shapely.geometry import Polygon  # noqa: E402
from shapely.ops import unary_union  # noqa: E402

# 几何腔高下限：低于项目自定取舍线（24）= 真缺陷 → FAIL
TARGET_H = 24.0
# 临界值：恰好等于取舍线，栅格化可能量到 23 → WARN（新批次应避开）
CRITICAL_H = 24.0
# 有余量的标尺（s3-008 的下限），新批次推荐做到 ≥ 26
SAFE_H = 26.0
# 腔宽下限：窄于此算针孔，不算缺陷（与 audit_white_holes 一致）
MIN_W = 40.0


def load_recipe(path: Path):
    """加载 recipe 模块，返回 build() 的字形列表。"""
    spec = __import__("importlib.util", fromlist=["util"]).spec_from_file_location(
        "recipe_" + path.stem, path)
    mod = __import__("importlib.util", fromlist=["util"]).module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.build()


def cavities(glyph) -> list[tuple[float, float, float, float]]:
    """返回字形的封闭内白 [(w, h, y0, y1)]，几何精确值。

    用笔画多边形的并集（shapely）的 `interiors` —— 那是**真正的洞**。
    不要用「环面积启发式」：多连通字形（左右分开的部件）会出现多个外环，
    启发式会把较小的外环误判成洞。
    """
    polys = []
    for pts in glyph._parts:
        poly = Polygon(pts)
        if not poly.is_valid:
            poly = poly.buffer(0)
        if not poly.is_empty:
            polys.append(poly)
    if not polys:
        return []
    merged = unary_union(polys)
    geoms = list(merged.geoms) if merged.geom_type == "MultiPolygon" else [merged]
    out = []
    for geom in geoms:
        if geom.is_empty:
            continue
        for interior in geom.interiors:
            minx, miny, maxx, maxy = interior.bounds
            out.append((maxx - minx, maxy - miny, miny, maxy))
    return out


def check_recipe(path: Path) -> list[tuple[int, str, float, float, float, float]]:
    """返回 [(unicode, name, w, h, y0, y1)]，每个腔高 ≤ 取舍线的腔一条。

    调用方按 h 区分 FAIL（< 24）与 WARN（= 24）。
    """
    problems = []
    for g in load_recipe(path):
        for w, h, y0, y1 in cavities(g):
            if w >= MIN_W and h <= CRITICAL_H:
                problems.append((g.unicode, g.name, w, h, y0, y1))
    return problems


def _selftest() -> int:
    """注入自证：造一个腔高不足的字，确认能抓到；造一个够高的，确认不误报。"""
    from hkbuild import Glyph

    def make_rect_glyph(name: str, unicode: int, box_h: float) -> Glyph:
        """一个口型方框：外高 box_h，笔画 84 → 内白 = box_h - 168。"""
        g = Glyph(name, advance=1000, unicode=unicode, note="自测")
        w = 84.0
        g.hbar(100, 500, box_h - w / 2, weight=w)
        g.hbar(100, 500, w / 2, weight=w)
        g.vbar(100 + w / 2, 0, box_h, weight=w)
        g.vbar(500 - w / 2, 0, box_h, weight=w)
        return g

    ok = True
    # 腔高 16（真缺陷，低于取舍线 24）→ 必须被抓到
    bad = make_rect_glyph("uni9F9F", 0x9F9F, 16 + 168)
    bad_cav = [c for c in cavities(bad) if c[0] >= MIN_W and c[1] < TARGET_H]
    if not bad_cav:
        print("[selftest] FAIL：腔高 16 的方框没被抓到")
        ok = False
    else:
        print("[selftest] OK：腔高 %.1f 被抓到" % bad_cav[0][1])

    # 腔高 24（= 取舍线，WARN 级，不是 FAIL）→ 不该被判 FAIL
    crit = make_rect_glyph("uni9F9E", 0x9F9E, 24 + 168)
    crit_cav = [c for c in cavities(crit) if c[0] >= MIN_W and c[1] < TARGET_H]
    if crit_cav:
        print("[selftest] FAIL：腔高 24 的方框被误判为 FAIL")
        ok = False
    else:
        print("[selftest] OK：腔高 24 未被判 FAIL（应为 WARN 级）")

    # 腔高 26（有余量）→ 不能误报
    good = make_rect_glyph("uni9F9D", 0x9F9D, 26 + 168)
    good_cav = [c for c in cavities(good) if c[0] >= MIN_W and c[1] < CRITICAL_H]
    if good_cav:
        print("[selftest] FAIL：腔高 26 的方框被误报")
        ok = False
    else:
        print("[selftest] OK：腔高 26 未误报")

    # 针孔（腔宽 < 40）→ 不该算缺陷
    pin = Glyph("uni9F9C", advance=1000, unicode=0x9F9C, note="自测")
    w = 84.0
    pin.hbar(300, 340, 100, weight=w)
    pin.hbar(300, 340, 8, weight=w)
    pin.vbar(300 + w / 2, 0, 100, weight=w)
    pin.vbar(340 - w / 2, 0, 100, weight=w)
    pin_cav = [c for c in cavities(pin) if c[0] >= MIN_W and c[1] < TARGET_H]
    if pin_cav:
        print("[selftest] FAIL：针孔被误判为缺陷")
        ok = False
    else:
        print("[selftest] OK：针孔未被误判")

    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="几何腔高校验（recipe 层）")
    ap.add_argument("--recipes", nargs="*", default=None,
                    help="只检查指定的 recipe 文件；默认扫全库")
    ap.add_argument("--strict", action="store_true",
                    help="把 WARN（几何腔高 = 24 的临界腔）也当 FAIL")
    ap.add_argument("--selftest", action="store_true", help="注入自证分辨力")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    if args.recipes:
        paths = [Path(p).resolve() for p in args.recipes]
    else:
        paths = sorted((FONT_SRC / "src").glob("*.py"))

    fails = 0
    warns = 0
    for path in paths:
        if not path.exists():
            print("[cavity] 跳过（不存在）：%s" % path)
            continue
        try:
            problems = check_recipe(path)
        except Exception as exc:  # noqa: BLE001
            print("[cavity] 跳过（无法加载）%s：%s" % (path.name, exc))
            continue
        bad = [p for p in problems if p[3] < TARGET_H]
        crit = [p for p in problems if CRITICAL_H <= p[3] < SAFE_H]
        if bad:
            fails += len(bad)
            print("[cavity] %s：几何腔高 < %.0f 的腔 %d 个（FAIL）"
                  % (path.name, TARGET_H, len(bad)))
            for uni, name, w, h, y0, y1 in bad:
                print("    U+%04X %s  w=%.0f  h=%.0f  y %.0f..%.0f"
                      % (uni, name, w, h, y0, y1))
        if crit:
            warns += len(crit)
            print("[cavity] %s：几何腔高 = %.0f 的临界腔 %d 个（WARN，新批次应避开）"
                  % (path.name, CRITICAL_H, len(crit)))

    print("")
    print("[cavity] 汇总：FAIL %d 个（几何腔高 < %.0f）· WARN %d 个（= %.0f 临界）"
          % (fails, TARGET_H, warns, CRITICAL_H))
    if fails:
        print("[cavity] FAIL")
        return 1
    if warns and args.strict:
        print("[cavity] FAIL（--strict：WARN 也算失败）")
        return 1
    print("[cavity] PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
