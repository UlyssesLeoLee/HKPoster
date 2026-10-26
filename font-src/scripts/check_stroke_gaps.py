"""check_stroke_gaps —— 笔画之间的间隙/重叠量报告（recipe 层，AST 解析）。

为什么要有这个检查器
--------------------
「笔画粘连成黑块」是本字体最常见的质量缺陷，但此前**只能靠目视**发现。
目视在小尺寸（48px）下尤其容易漏判。

更隐蔽的是：手工估余隙时容易算错。斜笔（`g.diag`）的墨迹沿**垂直于中心线**
展开，宽度 w 在 y 方向只覆盖 `w/2 * |ux|`（ux = 中心线 x 分量）。
按水平笔画那样用 ±w/2 去估，误差可以到几十单位 —— 本工具的实测值
曾经直接推翻过一次手工估算（城字的斜钩起笔）。

本脚本做什么
------------
1. AST 解析 recipe（不是正则），取出每一笔的几何参数；
2. 用与 `hkbuild` **完全相同**的算法重建每条笔画的墨迹多边形；
3. 用 shapely 算任意两笔之间的：
   - 交集面积（重叠量）
   - 距离（间隙；相交时为 0）
4. 输出「重叠量占较小笔画面积的比例」排序表 —— 汉字里笔画**相接**是常态
   （横竖相交于一点），所以本脚本**不判 FAIL**，只给可核对的数字。
   经验刻度：
     - 比例 < 30%：正常交叠（横竖相交于角）
     - 30% ~ 50%：偏紧，值得看一眼
     - > 50%：疑似粘连（两条本该分开的笔画被压在一起）

用法
----
    python font-src/scripts/check_stroke_gaps.py                        # 全部 recipe
    python font-src/scripts/check_stroke_gaps.py --recipes font-src/src/hkposter-cjk-core.py
    python font-src/scripts/check_stroke_gaps.py --top 15               # 每个字形列前 N 对
    python font-src/scripts/check_stroke_gaps.py --threshold 0.30       # 只列比例 >= 该值的对
"""

from __future__ import annotations

import argparse
import ast
import json
import math
import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from shapely.geometry import Polygon  # noqa: E402

STROKE_METHODS = {"hbar", "vbar", "diag", "dot", "rect", "poly", "ring"}

# 刻度：重叠「等效长度」（重叠面积折算成几个笔画宽）
SUSPECT_EQ = 3.0   # >3 个笔画宽：疑似粘连
TIGHT_EQ = 1.5     # 1.5~3：偏紧
MIN_GAP = 24.0     # 相交（0）之外，小于这个间隙算「临界」


def _num(node: ast.AST | None, consts: dict[str, float]) -> float | None:
    """把 AST 表达式求成数字；无法静态求值时返回 None。"""
    if node is None:
        return None
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        inner = _num(node.operand, consts)
        return None if inner is None else -inner
    if isinstance(node, ast.Name):
        return consts.get(node.id)
    if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
        a = _num(node.left, consts)
        b = _num(node.right, consts)
        if a is None or b is None:
            return None
        if isinstance(node.op, ast.Add):
            return a + b
        if isinstance(node.op, ast.Sub):
            return a - b
        if isinstance(node.op, ast.Mult):
            return a * b
        return a / b if b else None
    return None


def _module_consts(tree: ast.Module) -> dict[str, float]:
    """收集模块级常量（形如 W_MAIN = 96 / CJK_TOP = 820）。"""
    consts: dict[str, float] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant):
            if isinstance(node.value.value, (int, float)):
                for tgt in node.targets:
                    if isinstance(tgt, ast.Name):
                        consts[tgt.id] = float(node.value.value)
    return consts


def _kwargs(call: ast.Call) -> dict[str, ast.AST]:
    return {kw.arg: kw.value for kw in call.keywords if kw.arg}


def _stroke_quad(
    x1: float, y1: float, x2: float, y2: float, weight: float,
    cut_start: float = 0.0, cut_end: float = 0.0,
) -> list[tuple[float, float]]:
    """与 hkbuild._stroke_quad 完全一致。"""
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy)
    if length == 0:
        return []
    ux, uy = dx / length, dy / length
    px, py = -uy * weight / 2.0, ux * weight / 2.0
    return [
        (x1 + px + ux * cut_start, y1 + py + uy * cut_start),
        (x2 + px + ux * cut_end, y2 + py + uy * cut_end),
        (x2 - px + ux * cut_end, y2 - py + uy * cut_end),
        (x1 - px + ux * cut_start, y1 - py - uy * cut_start),
    ]


def _dot_quad(cx: float, cy: float, w: float, h: float, slant: float) -> list[tuple[float, float]]:
    """与 hkbuild.Glyph.dot 完全一致。"""
    return [
        (cx - w / 2.0, cy - h / 2.0),
        (cx + w / 2.0, cy - h / 2.0),
        (cx + w / 2.0 + slant, cy + h / 2.0),
        (cx - w / 2.0 + slant, cy + h / 2.0),
    ]


class _Visitor(ast.NodeVisitor):
    """收集每个字形函数里的笔画调用。"""

    def __init__(self, consts: dict[str, float]):
        self.consts = consts
        self.glyphs: dict[str, list[tuple[str, list[tuple[float, float]]]]] = {}
        self.skipped: list[str] = []
        self._func_stack: list[str] = []

    # ---- 函数名（字形名）----
    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._func_stack.append(node.name)
        self.glyphs.setdefault(node.name, [])
        self.generic_visit(node)
        self._func_stack.pop()

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self.visit_FunctionDef(node)  # type: ignore[arg-type]

    def _cur(self) -> str:
        return self._func_stack[-1] if self._func_stack else "<module>"

    def visit_Call(self, node: ast.Call) -> None:
        if isinstance(node.func, ast.Attribute) and node.func.attr in STROKE_METHODS:
            poly = self._geometry(node)
            if poly is None:
                # 记整条调用栈：栈顶是辅助函数，栈底（第一个）才是字形函数
                self.skipped.append(":".join(self._func_stack) or "<module>")
            else:
                self.glyphs.setdefault(self._cur(), []).append((node.func.attr, poly))
        self.generic_visit(node)

    def _geometry(self, call: ast.Call) -> list[tuple[float, float]] | None:
        consts = self.consts
        pos = call.args
        kw = _kwargs(call)
        method = call.func.attr  # type: ignore[union-attr]

        def arg(i: int, *names: str, default: float | None = None) -> float | None:
            for name in names:
                if name in kw:
                    return _num(kw[name], consts)
            if i < len(pos):
                return _num(pos[i], consts)
            return default

        if method == "hbar":
            x1 = arg(0, "x1"); x2 = arg(1, "x2"); y = arg(2, "y")
            w = arg(3, "weight", default=96.0)
            if None in (x1, x2, y, w):
                return None
            return _stroke_quad(x1, y, x2, y, w, arg(4, "cut_left", default=0.0) or 0.0,
                                arg(5, "cut_right", default=0.0) or 0.0)
        if method == "vbar":
            x = arg(0, "x"); y1 = arg(1, "y1"); y2 = arg(2, "y2")
            w = arg(3, "weight", default=96.0)
            if None in (x, y1, y2, w):
                return None
            return _stroke_quad(x, y1, x, y2, w, arg(4, "cut_bottom", default=0.0) or 0.0,
                                arg(5, "cut_top", default=0.0) or 0.0)
        if method == "diag":
            x1 = arg(0, "x1"); y1 = arg(1, "y1"); x2 = arg(2, "x2"); y2 = arg(3, "y2")
            w = arg(4, "weight", default=96.0)
            if None in (x1, y1, x2, y2, w):
                return None
            return _stroke_quad(x1, y1, x2, y2, w, arg(5, "cut_start", default=0.0) or 0.0,
                                arg(6, "cut_end", default=0.0) or 0.0)
        if method == "dot":
            cx = arg(0, "cx"); cy = arg(1, "cy")
            w = arg(2, "w", default=96.0); h = arg(3, "h", default=112.0)
            slant = arg(4, "slant", default=0.0)
            if None in (cx, cy, w, h, slant):
                return None
            return _dot_quad(cx, cy, w, h, slant)
        if method == "rect":
            x1 = arg(0, "x1"); x2 = arg(1, "x2"); y1 = arg(2, "y1"); y2 = arg(3, "y2")
            if None in (x1, x2, y1, y2):
                return None
            return [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
        # poly / ring：点列参数无法稳定静态求值，交给调用方处理
        return None


def analyse_by_import(path: Path) -> dict | None:
    """直接 import recipe 并调用 build()，拿每个字形的**真实笔画墨迹多边形**。

    这是首选路径：hkbuild.Glyph 把每次笔画调用存成一个独立的 part，
    所以 part 列表 == 笔画列表，且**不受 AST 静态求值的限制** ——
    辅助函数写法（diag_cap_base / bar_at / vspan …）照样能算。

    返回 None 表示这条路走不通（import 或 build 失败），调用方回退到 AST。
    """
    import importlib.util

    mod_name = "_hk_recipe_" + path.stem
    try:
        spec = importlib.util.spec_from_file_location(mod_name, path)
        if spec is None or spec.loader is None:
            return None
        mod = importlib.util.module_from_spec(spec)
        sys.modules[mod_name] = mod
        spec.loader.exec_module(mod)
        built = mod.build()
    except Exception as exc:  # noqa: BLE001
        print(f"[gaps] {path.name}：import/build 失败（{type(exc).__name__}: {exc}），回退到 AST")
        return None

    result = {"recipe": path.name, "glyphs": [], "skipped_dynamic_calls": 0, "skipped_detail": [],
              "method": "import-build"}

    def _label(poly: Polygon) -> str:
        """用几何给笔画起个可读的名字（import 模式拿不到方法名）。"""
        x0, y0, x1, y1 = poly.bounds
        w, h = x1 - x0, y1 - y0
        kind = "横" if w > h * 2 else ("竖" if h > w * 2 else "斜")
        return f"{kind}({x0:.0f}..{x1:.0f},{y0:.0f}..{y1:.0f})"

    def _is_same_stroke(a: Polygon, b: Polygon) -> bool:
        """判断两条笔画是不是**同一条笔画被写成了两段**。

        判据：一条的包围盒完全包含另一条，且两者主轴方向相同（都是横/都是竖）。
        这种「记账重复」在视觉上完全连续，不算缺陷 —— 很多 recipe 会把一条长竖
        分成上下两段写（为了控制竖的端点），工具不该把它报成粘连。
        """
        ax0, ay0, ax1, ay1 = a.bounds
        bx0, by0, bx1, by1 = b.bounds
        a_horiz = (ax1 - ax0) > (ay1 - ay0) * 2
        b_horiz = (bx1 - bx0) > (by1 - by0) * 2
        if a_horiz != b_horiz:
            return False
        a_in_b = ax0 >= bx0 - 1 and ax1 <= bx1 + 1 and ay0 >= by0 - 1 and ay1 <= by1 + 1
        b_in_a = bx0 >= ax0 - 1 and bx1 <= ax1 + 1 and by0 >= ay0 - 1 and by1 <= ay1 + 1
        return a_in_b or b_in_a

    for g in built:
        parts = getattr(g, "_parts", [])
        polys: list[tuple[str, Polygon]] = []
        for pts in parts:
            if len(pts) < 3:
                continue
            poly = Polygon([(float(x), float(y)) for x, y in pts])
            if not poly.is_valid:
                poly = poly.buffer(0)
            if poly.is_empty:
                continue
            polys.append((_label(poly), poly))
        pairs = []
        for i in range(len(polys)):
            for j in range(i + 1, len(polys)):
                a = polys[i][1]
                b = polys[j][1]
                inter = a.intersection(b)
                area = inter.area
                ratio = area / min(a.area, b.area) if min(a.area, b.area) > 0 else 0.0
                gap = 0.0 if area > 0 else a.distance(b)
                thinner = min(a.bounds[2] - a.bounds[0], a.bounds[3] - a.bounds[1],
                              b.bounds[2] - b.bounds[0], b.bounds[3] - b.bounds[1])
                eq_len = area / (thinner * thinner) if thinner > 0 else 0.0
                dup = _is_same_stroke(a, b)
                pairs.append({
                    "a": polys[i][0], "b": polys[j][0],
                    "overlap_area": round(area, 1),
                    "ratio": round(ratio, 3),
                    "eq_len": round(eq_len, 2),
                    "gap": round(gap, 1),
                    "dup": dup,
                })
        pairs.sort(key=lambda p: (-p["eq_len"], p["gap"]))
        result["glyphs"].append({
            "func": getattr(g, "name", "?"), "strokes": len(polys),
            "suspect": [p for p in pairs if p["eq_len"] >= SUSPECT_EQ and not p["dup"]],
            "tight": [p for p in pairs if 0 < p["gap"] < MIN_GAP],
            "dup_pairs": [p for p in pairs if p["dup"]],
            "pairs": pairs,
        })
    return result


def analyse(path: Path) -> dict:
    """优先用 import-build（覆盖全部字形）；失败则回退到 AST 静态解析。"""
    by_import = analyse_by_import(path)
    if by_import is not None:
        return by_import
    tree = ast.parse(path.read_text(encoding="utf-8"))
    consts = _module_consts(tree)
    visitor = _Visitor(consts)
    visitor.visit(tree)

    result = {"recipe": path.name, "glyphs": [], "skipped_dynamic_calls": len(visitor.skipped),
              "skipped_detail": sorted(set(visitor.skipped)), "method": "ast"}
    for fname, strokes in visitor.glyphs.items():
        polys: list[tuple[str, Polygon]] = []
        for kind, pts in strokes:
            if len(pts) < 3:
                continue
            poly = Polygon(pts)
            if not poly.is_valid:
                poly = poly.buffer(0)
            if poly.is_empty:
                continue
            polys.append((kind, poly))
        pairs = []
        for i in range(len(polys)):
            for j in range(i + 1, len(polys)):
                ka, a = polys[i]
                kb, b = polys[j]
                inter = a.intersection(b)
                area = inter.area
                ratio = area / min(a.area, b.area) if min(a.area, b.area) > 0 else 0.0
                gap = 0.0 if area > 0 else a.distance(b)
                # 等效重叠长度：重叠面积折算成「几个笔画宽」。
                # 面积 ÷ (窄边 × 窄边) = 以笔画宽为单位的重叠长度。
                # 比面积比例公允 —— 短撇压在横上时面积比例必然虚高
                # （撇本身只有一根宽），但等效长度仍是有意义的尺度。
                thinner = min(a.bounds[2] - a.bounds[0], a.bounds[3] - a.bounds[1],
                              b.bounds[2] - b.bounds[0], b.bounds[3] - b.bounds[1])
                eq_len = area / (thinner * thinner) if thinner > 0 else 0.0
                pairs.append({
                    "a": f"{i}:{ka}", "b": f"{j}:{kb}",
                    "overlap_area": round(area, 1),
                    "ratio": round(ratio, 3),
                    "eq_len": round(eq_len, 2),
                    "gap": round(gap, 1),
                })
        pairs.sort(key=lambda p: (-p["eq_len"], p["gap"]))
        result["glyphs"].append({
            "func": fname, "strokes": len(polys),
            "suspect": [p for p in pairs if p["eq_len"] >= SUSPECT_EQ and not p.get("dup")],
            "tight": [p for p in pairs if 0 < p["gap"] < MIN_GAP],
            "pairs": pairs,
        })
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--recipes", nargs="*", default=None,
                    help="只查这些 recipe（相对 font-src/src 的路径或文件名）")
    ap.add_argument("--top", type=int, default=8, help="每个字形列出前 N 对（默认 8）")
    ap.add_argument("--threshold", type=float, default=TIGHT_EQ,
                    help=f"列出等效重叠长度 >= 该值的对（默认 {TIGHT_EQ}）")
    args = ap.parse_args()

    src_dir = FONT_SRC / "src"
    if args.recipes:
        paths = []
        for item in args.recipes:
            p = Path(item)
            if not p.exists():
                p = src_dir / Path(item).name
            if not p.exists():
                p = src_dir / (Path(item).stem + ".py")
            paths.append(p)
    else:
        paths = sorted(src_dir.glob("*.py"))

    all_results = []
    total_suspect = 0
    total_tight = 0
    total_dup = 0
    for path in paths:
        if not path.exists():
            print(f"[gaps] 找不到 recipe：{path}")
            continue
        res = analyse(path)
        all_results.append(res)
        for g in res["glyphs"]:
            total_suspect += len(g["suspect"])
            total_tight += len(g["tight"])
            total_dup += len([p for p in g.get("dup_pairs", [])
                              if p["eq_len"] >= args.threshold])

    print(f"[gaps] 扫了 {len(paths)} 个 recipe")
    print(f"[gaps] 指标：重叠等效长度（重叠面积 ÷ 较窄笔画的宽度，单位=笔画宽）· 间隙（相交时为 0）")
    print(f"[gaps] 刻度：等效长度 <1.5 属正常交叠 · 1.5~3 偏紧 · >3 疑似粘连；"
          f"间隙 <{MIN_GAP:.0f} 单位为临界")
    print("[gaps] 注：同一条笔画被写成上下/左右两段（包围盒包含、主轴同向）算「记账重复」，"
          "已排除出粘连统计。")
    print()
    for res in all_results:
        if res["skipped_dynamic_calls"]:
            funcs = sorted({s.split(":")[0] for s in res["skipped_detail"]})
            print(f"[gaps] {res['recipe']}：{res['skipped_dynamic_calls']} 个笔画调用参数是动态的"
                  f"（辅助函数写法），**这些字形未被本工具检查**：")
            print(f"        {', '.join(funcs)}")
            print(f"        → 这些字形仍需目视把关；要让工具覆盖它们，"
                  f"请在 recipe 里写显式坐标而不是辅助函数。")
        for g in res["glyphs"]:
            hot = [p for p in g["pairs"] if p["eq_len"] >= args.threshold]
            if not hot:
                continue
            print(f"[gaps] {res['recipe']} :: {g['func']}（{g['strokes']} 笔）")
            for p in hot[: args.top]:
                if p.get("dup"):
                    flag = "同笔重复段（已排除）"
                else:
                    flag = "疑似粘连" if p["eq_len"] >= 3.0 else "偏紧"
                print(f"        {p['a']} × {p['b']}  等效重叠 {p['eq_len']} 宽  "
                      f"面积 {p['overlap_area']}  间隙 {p['gap']}  ← {flag}")
            print()

    out = FONT_SRC / "reports" / "stroke-gaps.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({
        "suspect_eq_len": SUSPECT_EQ,
        "tight_eq_len": TIGHT_EQ,
        "min_gap": MIN_GAP,
        "recipes": all_results,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[gaps] 疑似粘连 {total_suspect} 对 · 临界间隙 {total_tight} 对"
          f" · 同笔重复段 {total_dup} 对")
    if total_dup:
        print("[gaps]   ↑ 同笔重复段**不计入粘连**，但要看一眼："
              "同一条笔画被写了两次（常见于「加宽某横」），"
              "并集后那一笔会比别的笔画明显粗 —— 视觉上就是「这条横偏胖」。")
    print(f"[gaps] 报告：{out}")
    # 纯参考工具：不判 FAIL
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
