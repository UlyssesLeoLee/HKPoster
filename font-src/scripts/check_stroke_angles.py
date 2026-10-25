"""check_stroke_angles —— 笔画角度与记号倾角的检查（recipe 层，AST 解析）。

项目所有者 2026-10-25：「你可以改变笔画的设计，但不要改变笔画的角度」。

为什么必须在 recipe 层查
----------------------
直笔轮廓的**边**与笔画方向差 90°，但轮廓里还混着端面斜切的边、硬折转角的边、
曲线每一小段的方向。实测：拿成品轮廓做角度直方图，连「一」（一条横）都报 0.89 差异 ——
量到的是**端点设计**，不是笔画方向。这条路不可用。

recipe 层是准的：Jōyō 的 recipe 按规范用**字面量坐标**调笔画原语
（`g.hbar / g.vbar / g.diag / g.dot`），笔画起终点直接写在代码里。
本脚本用 AST 解析（不是正则），取出每一笔的坐标算角度。

三段判据（能判的判，不能判的只报分布）
--------------------------------------
A. **斜切倾角档位**（GLY-003 / GLY-004）→ **FAIL**
   点与短撇用 `g.dot(..., slant=…)`，slant 必须是工程约定的那一档。
   斜切只许用在点/短撇/记号；主笔（横竖撇捺）出现斜切即违规。

B. **斜画与竖直的夹角** → **只报分布，不判 FAIL**
   逐字期望角度需要逐字参照数据，没有可靠来源。
   夹角接近 0°（读成竖）或接近 90°（读成横）值得人看一眼，所以报出来。

C. **浊点必须是斜的、半浊点必须是圆的** → **FAIL**
   已经发生过一次违规：把浊点从两枚斜画改成两枚竖向斜切块 ——
   形状更「统一」了，但浊点本来就该是斜的，改竖等于改了笔画角度，
   也丢了参照字体的形态（参照的浊点包围盒是斜的：M PLUS 1p Black 383×270 / 1000 em）。

用法
----
    python font-src/scripts/check_stroke_angles.py
    python font-src/scripts/check_stroke_angles.py --recipes a.py b.py
"""

from __future__ import annotations

import argparse
import ast
import json
import math
import sys
from pathlib import Path

if hasattr(sys, "stdout") and "reconfigure" in dir(sys.stdout):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "font-src" / "src"

# 工程在用的斜切倾角档位（0 = 竖点不斜切；其余见 hkposter-cjk-core.py 与派单规格）
ALLOWED_SLANT = {0, 26, 22, 20, 18, 16, 14, -14}

# 浊点 / 半浊点 记号的变量名（recipe 里模块级常量）
DAKU_NAMES = {"DAKU", "DAKUTEN"}
HAND_NAMES = {"HAND", "HANDAKUTEN"}

# 浊点必须是斜的：与竖直的夹角落在这个区间
DAKU_MIN_DEG = 15.0
DAKU_MAX_DEG = 70.0


def _num(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    return None


def _angle_from_vertical(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    if abs(dx) < 1e-9 and abs(dy) < 1e-9:
        return None
    return math.degrees(math.atan2(abs(dx), abs(dy)))


def _tuple_kind(node):
    """返回一个元组的类型与数值（能取到的话）。"""
    if not isinstance(node, ast.Tuple) or not node.elts:
        return None, []
    head = node.elts[0]
    if isinstance(head, ast.Constant) and isinstance(head.value, str):
        kind = head.value
        rest = node.elts[1:]
        return kind, rest
    return None, []


def _collect_marks(node, kind, rest):
    """从一条记号笔画里取出类型与关键数值。"""
    if kind in ("D", "d"):
        nums = [_num(a) for a in rest[:4]]
        if all(n is not None for n in nums):
            return ("D", nums[0], nums[1], nums[2], nums[3])
    if kind in ("p", "P"):
        if rest and isinstance(rest[0], (ast.List, ast.Tuple)):
            pts = []
            for pt in rest[0].elts:
                if isinstance(pt, (ast.List, ast.Tuple)) and len(pt.elts) >= 2:
                    a, b = _num(pt.elts[0]), _num(pt.elts[1])
                    if a is not None and b is not None:
                        pts.append((a, b))
            if len(pts) >= 2:
                return ("p", pts[0][0], pts[0][1], pts[-1][0], pts[-1][1])
    if kind in ("dot", "DOT"):
        nums = [_num(a) for a in rest[:2]]
        if nums[0] is not None and nums[1] is not None:
            return ("dot", nums[0], nums[1])
    if kind in ("ring", "RING"):
        return ("ring",)
    return (kind,)


class _Visitor(ast.NodeVisitor):
    def __init__(self):
        self.diags = []     # (lineno, angle_from_vertical)
        self.slants = []    # (lineno, slant)
        self.marks = []     # (lineno, varname, kind, *nums)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            name = node.func.attr
            args = list(node.args)
            if name == "diag" and len(args) >= 4:
                vals = [_num(a) for a in args[:4]]
                if all(v is not None for v in vals):
                    ang = _angle_from_vertical(*vals)
                    if ang is not None:
                        self.diags.append((node.lineno, round(ang, 1)))
            if name == "dot":
                sl = None
                for a in args[4:5]:
                    sl = _num(a)
                for kw in node.keywords:
                    if kw.arg == "slant":
                        sl = _num(kw.value)
                if sl is not None:
                    self.slants.append((node.lineno, int(sl)))
        self.generic_visit(node)

    def visit_Assign(self, node):
        if isinstance(node.value, (ast.List, ast.Tuple)):
            for t in node.value.elts:
                kind, rest = _tuple_kind(t)
                if kind is None:
                    continue
                for tgt in node.targets:
                    if isinstance(tgt, ast.Name) and tgt.id in DAKU_NAMES | HAND_NAMES:
                        self.marks.append((node.lineno, tgt.id) + _collect_marks(t, kind, rest))
        self.generic_visit(node)


def main() -> int:
    ap = argparse.ArgumentParser(description="recipe 层笔画角度与记号倾角检查")
    ap.add_argument("--recipes", nargs="*", help="要检查的 recipe 文件（默认扫 font-src/src 下全部）")
    ap.add_argument("--out", default=str(ROOT / "font-src" / "reports" / "stroke-angles.json"))
    args = ap.parse_args()

    files = ([Path(p) for p in args.recipes] if args.recipes
             else sorted(SRC.glob("hkposter-*.py")))
    if not files:
        print("[angles] 没有找到 recipe")
        return 1

    problems = []
    dist = []
    n_files = n_diags = n_slants = 0
    for p in files:
        if not p.exists():
            continue
        try:
            tree = ast.parse(p.read_text(encoding="utf-8"))
        except SyntaxError as e:
            problems.append({"file": p.name, "line": 0, "kind": "parse", "detail": f"语法错误：{e}"})
            continue
        v = _Visitor()
        v.visit(tree)
        n_files += 1
        n_diags += len(v.diags)
        n_slants += len(v.slants)

        # A. 斜切档位（只适用于 CJK 家族 —— Latin 标点有自己的一套）
        if not p.name.startswith("hkposter-latin"):
            for lineno, sl in v.slants:
                if sl not in ALLOWED_SLANT:
                    problems.append({
                        "file": p.name, "line": lineno, "kind": "slant",
                        "detail": f"斜切倾角 slant={sl} 不在工程档位 "
                                  f"{sorted(ALLOWED_SLANT, reverse=True)} 内"
                                  f"（GLY-003：斜切只许用在点/短撇/记号）",
                    })

        # B. 斜画角度（只报分布）
        for lineno, ang in v.diags:
            dist.append({"file": p.name, "line": lineno, "deg": ang})

        # C. 浊点 / 半浊点形态
        for item in v.marks:
            lineno, var, kind = item[0], item[1], item[2]
            if var in DAKU_NAMES:
                if kind == "dot":
                    problems.append({
                        "file": p.name, "line": lineno, "kind": "daku",
                        "detail": f"{var} 用了点/竖块 —— 浊点本来是**斜**的，"
                                  f"改成竖块等于改了笔画角度（已发生过一次违规）",
                    })
                elif kind in ("D", "p"):
                    ang = _angle_from_vertical(item[3], item[4], item[5], item[6])
                    if ang is not None and not (DAKU_MIN_DEG <= ang <= DAKU_MAX_DEG):
                        problems.append({
                            "file": p.name, "line": lineno, "kind": "daku",
                            "detail": f"{var} 的斜画与竖直夹角 {ang:.1f}° 超出 "
                                      f"[{DAKU_MIN_DEG}, {DAKU_MAX_DEG}] —— 浊点应是斜画",
                        })
            if var in HAND_NAMES:
                if kind != "ring":
                    problems.append({
                        "file": p.name, "line": lineno, "kind": "handaku",
                        "detail": f"{var} 不是圆环（是 {kind}）—— 半浊点按定义就是圆圈，"
                                  f"参照字体的 ゚ 包围盒是正方形",
                    })

    out = Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"problems": problems, "diag_degrees": dist},
                              ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[angles] 扫了 {n_files} 个 recipe：斜画 {n_diags} 笔、斜切点 {n_slants} 处")
    if dist:
        degs = sorted(d["deg"] for d in dist)
        print(f"[angles] 斜画与竖直夹角分布：中位 {degs[len(degs) // 2]:.1f}°  "
              f"最小 {degs[0]:.1f}°  最大 {degs[-1]:.1f}°（只报分布，不判 FAIL）")
        extreme = [d for d in dist if d["deg"] < 5.0 or d["deg"] > 85.0]
        if extreme:
            print(f"[angles]   其中 {len(extreme)} 笔接近水平/竖直，值得人看一眼：")
            for d in extreme[:10]:
                print(f"    {d['file']}:{d['line']}  {d['deg']}°")
    if problems:
        print(f"[angles] 违规 {len(problems)} 处：")
        for pr in problems[:30]:
            print(f"  {pr['file']}:{pr['line']}  [{pr['kind']}]  {pr['detail']}")
        if len(problems) > 30:
            print(f"  …… 还有 {len(problems) - 30} 条")
    else:
        print("[angles] PASS")
    print(f"[angles] 报告：{out}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
