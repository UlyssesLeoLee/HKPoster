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
#
# 分组说明（slant = 平行四边形**顶部右移**量）：
#   0   竖点（亠/宀的点）
#   14  短撇（丿，轻度）
#   26  短撇（丿，标准档）
#   22 / 20 / 18 / 16  短撇的微调档（同一方向的斜度分级）
#   -14  点（丶，标准档）
#   -26 / -20 / -16 / -10  点的斜度分级（仍是右下走向 = 同一个「丶」方向）
#
# 方向语义只有一个：正 slant = 撇向（左下），负 slant = 捺向（右下）。
# 斜切端面改的是「切口的斜度」，不改变笔画走向（契约 GLY-003）。
ALLOWED_SLANT = {0, 14, 16, 18, 20, 22, 26, 28, -10, -14, -16, -20, -26}

# 浊点 / 半浊点 记号的变量名（recipe 里模块级常量）
DAKU_NAMES = {"DAKU", "DAKUTEN"}
HAND_NAMES = {"HAND", "HANDAKUTEN"}

# 浊点必须是斜的：与竖直的夹角落在这个区间
DAKU_MIN_DEG = 15.0
DAKU_MAX_DEG = 70.0


def _num(node, env=None):
    """取 AST 节点的数值。

    支持三种写法（2026-10-27 修：原实现只认 `ast.Constant`，
    于是 `-14` 这种 `UnaryOp` **全部被静默跳过** —— 工具报「斜切点 12 处」，
    实际有 41 处。负数档位正是最需要检查的一批）：

    * `ast.Constant`   → 字面量 `26`
    * `ast.UnaryOp`    → 负字面量 `-14`（USub/UAdd）
    * `ast.Name`       → 模块级常量 / 形参默认值（`SLANT_DOT`、`slant`）
    """
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        inner = _num(node.operand, env)
        if inner is None:
            return None
        return -inner if isinstance(node.op, ast.USub) else inner
    if isinstance(node, ast.Name) and env:
        return env.get(node.id)
    return None


def _module_consts(tree):
    """模块级整数常量：名字 -> 数值（供 `slant=SLANT_DOT` 解析）。"""
    env = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            v = _num(node.value, env)
            if v is not None:
                env[node.targets[0].id] = v
    return env


def _func_params(fn, env):
    """函数形参的默认值：名字 -> 数值（供 `slant=slant` 透传解析）。"""
    out = {}
    args = fn.args
    positional = list(getattr(args, "posonlyargs", [])) + list(args.args)
    defaults = list(args.defaults)
    pad = len(positional) - len(defaults)
    for i, a in enumerate(positional):
        if i >= pad:
            v = _num(defaults[i - pad], env)
            if v is not None:
                out[a.arg] = v
    for a, d in zip(args.kwonlyargs, args.kw_defaults):
        if d is not None:
            v = _num(d, env)
            if v is not None:
                out[a.arg] = v
    return out



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
    def __init__(self, env=None):
        self.diags = []     # (lineno, angle_from_vertical)
        self.slants = []    # (lineno, slant)
        self.marks = []     # (lineno, varname, kind, *nums)
        self.unresolved = []  # (lineno, 表达式摘要) —— 斜切倾角解析不出来
        self.env = env or {}
        self.scopes = [self.env]   # 作用域栈：模块级 -> 函数级

    def _lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    def visit_FunctionDef(self, node):
        self.scopes.append(_func_params(node, self.env))
        self.generic_visit(node)
        self.scopes.pop()

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            name = node.func.attr
            args = list(node.args)
            if name == "diag" and len(args) >= 4:
                vals = [_num(a, self.env) for a in args[:4]]
                if all(v is not None for v in vals):
                    ang = _angle_from_vertical(*vals)
                    if ang is not None:
                        self.diags.append((node.lineno, round(ang, 1)))
            if name == "dot":
                sl_node = None
                for kw in node.keywords:
                    if kw.arg == "slant":
                        sl_node = kw.value
                if sl_node is None and len(args) >= 5:
                    sl_node = args[4]
                if sl_node is None:
                    sl_node = _SENTINEL
                sl = self._resolve(sl_node)
                if sl is None:
                    if sl_node is not _SENTINEL:
                        self.unresolved.append((node.lineno, _expr_summary(sl_node)))
                else:
                    self.slants.append((node.lineno, int(sl)))
        self.generic_visit(node)

    def _resolve(self, node):
        """把一个 slant 表达式解析成数值（用当前作用域链）。"""
        if node is _SENTINEL:
            return None
        if isinstance(node, ast.Name):
            v = self._lookup(node.id)
            return v
        return _num(node, self.env)

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


_SENTINEL = object()


def _expr_summary(node):
    """给无法解析的 slant 表达式一个可读的摘要（用于报告定位）。"""
    try:
        return ast.unparse(node)[:60]
    except Exception:
        return type(node).__name__


def _data_slants(tree, env):
    """从**数据表**里提取 slant 值。

    kana 的 recipe 把笔画存在元组里（`("DOT", cx, cy, w, h, slant)`），
    倾角不在 `g.dot(...)` 的实参里，而是元组的第 6 个元素 ——
    靠实参解析看不到它们。这里按「标记 + 下标」把它们取出来核对。

    约定：元组首元素是 `"dot"` / `"DOT"` 时，第 6 个元素（索引 5）是 slant。
    """
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Tuple, ast.List)) or len(node.elts) < 6:
            continue
        head = node.elts[0]
        if not (isinstance(head, ast.Constant) and isinstance(head.value, str)):
            continue
        if head.value not in ("dot", "DOT"):
            continue
        v = _num(node.elts[5], env)
        if v is not None:
            out.append((getattr(node, "lineno", 0), int(v)))
    return out



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
    n_unresolved = 0
    for p in files:
        if not p.exists():
            continue
        try:
            tree = ast.parse(p.read_text(encoding="utf-8"))
        except SyntaxError as e:
            problems.append({"file": p.name, "line": 0, "kind": "parse", "detail": f"语法错误：{e}"})
            continue
        env = _module_consts(tree)
        v = _Visitor(env)
        v.visit(tree)
        n_files += 1
        n_diags += len(v.diags)
        n_slants += len(v.slants)

        # 数据表里的 slant（kana 把笔画存在元组里，倾角不在实参里）
        data_slants = _data_slants(tree, env)
        n_slants += len(data_slants)

        # A. 斜切档位（只适用于 CJK 家族 —— Latin 标点有自己的一套）
        if not p.name.startswith("hkposter-latin"):
            for lineno, sl in list(v.slants) + data_slants:
                if sl not in ALLOWED_SLANT:
                    problems.append({
                        "file": p.name, "line": lineno, "kind": "slant",
                        "detail": f"斜切倾角 slant={sl} 不在工程档位 "
                                  f"{sorted(ALLOWED_SLANT, reverse=True)} 内"
                                  f"（GLY-003：斜切只许用在点/短撇/记号）",
                    })

        # A2. 解析不出来的 slant —— **不静默跳过**：报出来，让人决定是补门禁还是改 recipe。
        # 数据表通道已经覆盖到的文件不再重复报（kana 的倾角在元组里，实参是变量）。
        if not data_slants:
            for lineno, expr in v.unresolved:
                n_unresolved += 1
                problems.append({
                    "file": p.name, "line": lineno, "kind": "slant_unresolved",
                    "detail": f"无法解析斜切倾角表达式 `{expr}` —— 这一处的档位没有被检查到"
                              f"（把字面量/模块常量/形参默认值写清楚，或扩展本工具的解析能力）",
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

    print(f"[angles] 扫了 {n_files} 个 recipe：斜画 {n_diags} 笔、斜切点 {n_slants} 处"
          + (f"（另有 {n_unresolved} 处倾角表达式无法解析）" if n_unresolved else ""))
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
