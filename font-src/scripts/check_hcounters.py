"""check_hcounters —— 横画内白（counter）封闭专项门禁。

为什么要有这个检查器
--------------------
`check_stroke_gaps` 用「重叠等效长度」判粘连，但**横画墨连成黑带时，
等效长度可能只有 1~2**（短横 / 部分重叠），落在门槛以下 → 门禁不报，
字已经连成黑带。

实测事故（2026-10-27）：
  * 「買」的「罒」：框高 140 却用 96 厚笔画 → 上下横直接叠死，
    等效长度 4.18 被 `check_stroke_gaps` 抓到（这一条侥幸没漏）。
  * 「程 / 崎 / 週 / 登 / 値 / 討」：口 / 目 型方框的**内白被吃光**
    （框高 < 2×笔画宽 + 24），等效长度 0.08~0.88 —— **现有门禁全部不报**，
    而渲染出来是一块黑砖。
  * 「影」（手写基线 cjk-core）：「日」字头三横全贴死 → 渲染成实心黑块。
    已合并的 1277 字里，同类共 156 处。

判据
----
只看**横 × 横**（竖 × 横是 CJK 的正常交叉，不算）。
  * 两笔的墨迹包围盒都是「宽 >> 高」= 横；宽度 < 60 的小记号忽略
    （假名浊点、半浊点天然叠在一起）。
  * 两笔的 x 范围必须有重叠 —— 不同部件互不相干的横不算。
  * **白口** = 两笔墨迹在 y 方向留出的空白；白口 < 24 即报
    （AGENTS.md 铁律 7：相邻横画中心线间距 ≥ 笔画宽 + 24）。

FAIL 判据：白口 **≤ 0**（腔被封死）→ 这类字渲染出来是黑砖，必须修。

为什么不直接对全部白口 < 24 判 FAIL
-----------------------------------
几何上分不清「两横贴死是缺陷」与「两横本来就挨着（合法的密字）」。
实测反例：zh-HK「爱」的「友」部两条横墨迹互相叠 19 单位，
渲染出来完全正常 —— 叠 19 单位是可接受的交叠，不是封闭腔。
所以本门禁只对**白口 ≤ 0**判 FAIL。

**已知欠账用基线记账**（`font-src/data/hcounter-baseline.json`）：
当前 dev 里已有一批白口被吃光的老字（多为手写基线与早期批次）。
它们记在基线里，门禁**不报它们**（否则 dev 一上线就红），
但基线里的欠账数量会打印出来，且**任何新出现的封闭内白都会 FAIL**。
基线只允许变短，不允许变长。

用法
----
    python font-src/scripts/check_hcounters.py                  # 全部 recipe
    python font-src/scripts/check_hcounters.py --recipes font-src/src/hkposter-joyo-w2-s3-007.py
    python font-src/scripts/check_hcounters.py --selftest       # 注入真实错配自证分辨力
    python font-src/scripts/check_hcounters.py --update-baseline  # 重新生成基线
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from shapely.geometry import Polygon  # noqa: E402

import check_stroke_gaps as gaps  # noqa: E402

MIN_W = 60.0        # 宽度小于此的小记号不参与判定
MIN_GAP = 24.0      # 白口门槛：AGENTS.md「相邻横画中心线间距 ≥ 笔画宽 + 24」
CLOSE_GAP = 0.0     # 白口 ≤ 0：腔被封死 → FAIL 级

BASELINE_PATH = FONT_SRC / "data" / "hcounter-baseline.json"


def _is_horizontal(poly: Polygon) -> bool:
    """这条笔画是不是**真正的横**（轴对齐的长条矩形）。

    这是**兜底判据**，只在拿不到原语元数据时使用（例如对外部几何体）。
    不能只看包围盒的宽高比：**平捺**（辶的底、戈的斜钩）是一个很扁的斜四边形，
    宽高比轻松超过 2，会被误判成「横」，然后拿它的 bbox 去跟真的横比白口，
    算出一堆假阳性（实测「辻」的平捺 bbox 高 190、宽 404 → 被当成横）。

    判据用**面积**：轴对齐矩形的面积 == 包围盒面积；斜笔的面积 < 包围盒面积。
    """
    x0, y0, x1, y1 = poly.bounds
    w, h = x1 - x0, y1 - y0
    if w < MIN_W or w <= h * 2.0:
        return False
    bbox_area = w * h
    if bbox_area <= 0:
        return False
    return abs(poly.area - bbox_area) <= max(1.0, bbox_area * 0.02)


def _horizontal_flags(glyph) -> list[bool] | None:
    """每一条笔画是不是横画 —— **用原语类型判，不用几何猜**。

    为什么必须用原语类型：一条**竖桩**（长度短于笔画宽）画出来的多边形是
    (宽, 短) 的矩形，和一条同尺寸的**横桩**多边形完全一样 ——
    几何上根本分不出方向（实测：書 的聿顶點 84×40、授 的冖左竖 88×42，
    都被几何判据当成了横画，去跟真的横比白口，报出假阳性）。

    原语类型（hbar/vbar/diag/dot/rect/ring/poly）是唯一可靠的方向来源。
    """
    parts = getattr(glyph, "_parts", [])
    prims = getattr(glyph, "_prims", None)
    if prims is None or len(prims) != len(parts):
        return None
    flags = []
    for prim in prims:
        kind = prim.get("kind")
        if kind == "hbar":
            # 宽度（横跨长度）小于门槛的小记号忽略
            length = abs(float(prim.get("x2", 0)) - float(prim.get("x1", 0)))
            flags.append(length >= MIN_W)
        else:
            flags.append(False)
    return flags


def _label(poly: Polygon) -> str:
    x0, y0, x1, y1 = poly.bounds
    return f"横({x0:.0f}..{x1:.0f},{y0:.0f}..{y1:.0f})"


def _white_gap(a: Polygon, b: Polygon) -> float:
    """两笔之间在 y 方向留出的空白；互相覆盖时为负。

    先按**竖直中点**定谁在上、谁在下（不能用 a 自己的上下缘比，
    那样会把「谁在上」判反，报出一堆假阳性）。
    """
    a_mid = (a.bounds[1] + a.bounds[3]) / 2.0
    b_mid = (b.bounds[1] + b.bounds[3]) / 2.0
    upper, lower = (a, b) if a_mid >= b_mid else (b, a)
    return upper.bounds[1] - lower.bounds[3]  # 上笔的下缘 − 下笔的上缘


def _x_overlap(a: Polygon, b: Polygon) -> float:
    return min(a.bounds[2], b.bounds[2]) - max(a.bounds[0], b.bounds[0])


def collect(path: Path) -> list[dict]:
    """重建字形笔画多边形，找出白口不足的横×横对。"""
    import importlib.util

    mod_name = "_hk_hc_" + path.stem
    try:
        spec = importlib.util.spec_from_file_location(mod_name, path)
        if spec is None or spec.loader is None:
            return []
        mod = importlib.util.module_from_spec(spec)
        sys.modules[mod_name] = mod
        spec.loader.exec_module(mod)
        built = mod.build()
    except Exception as exc:  # noqa: BLE001
        print(f"[hcounters] {path.name}：import/build 失败（{type(exc).__name__}: {exc}）")
        return []

    findings: list[dict] = []
    for g in built:
        name = getattr(g, "name", "?")
        flags = _horizontal_flags(g)
        polys: list[Polygon | None] = []
        for pts in getattr(g, "_parts", []):
            if len(pts) < 3:
                polys.append(None)
                continue
            poly = Polygon([(float(x), float(y)) for x, y in pts])
            if not poly.is_valid:
                poly = poly.buffer(0)
            polys.append(None if poly.is_empty else poly)
        for i in range(len(polys)):
            for j in range(i + 1, len(polys)):
                a, b = polys[i], polys[j]
                if a is None or b is None:
                    continue
                if flags is not None:
                    if not (flags[i] and flags[j]):
                        continue
                elif not (_is_horizontal(a) and _is_horizontal(b)):
                    continue
                if _x_overlap(a, b) <= 0:
                    continue
                gap = _white_gap(a, b)
                if gap >= MIN_GAP:
                    continue
                findings.append({
                    "recipe": path.name,
                    "glyph": name,
                    "a": _label(a),
                    "b": _label(b),
                    "gap": round(gap, 1),
                    "closed": gap <= CLOSE_GAP,
                })
    return findings


def key_of(f: dict) -> str:
    return f"{f['recipe']}::{f['glyph']}"


def load_baseline() -> set[str]:
    if not BASELINE_PATH.exists():
        return set()
    data = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    return set(data.get("known_closed_counters", []))


def main() -> int:
    parser = argparse.ArgumentParser(description="横画内白封闭专项门禁")
    parser.add_argument("--recipes", nargs="*", default=None)
    parser.add_argument("--update-baseline", action="store_true", help="重新生成基线（回修后用）")
    parser.add_argument("--selftest", action="store_true", help="注入真实错配，自证分辨力")
    parser.add_argument("--report", default=None)
    args = parser.parse_args()

    if args.selftest:
        return _selftest()

    if args.recipes:
        paths = [Path(p) if Path(p).exists() else FONT_SRC / "src" / Path(p).name
                 for p in args.recipes]
    else:
        paths = sorted((FONT_SRC / "src").glob("*.py"))

    baseline = load_baseline()
    all_findings: list[dict] = []
    for p in paths:
        if not p.exists():
            print(f"[hcounters] 找不到 recipe：{p}")
            continue
        all_findings.extend(collect(p))

    closed = [f for f in all_findings if f["closed"]]
    tight = [f for f in all_findings if not f["closed"]]

    if args.update_baseline:
        keys = sorted({key_of(f) for f in closed})
        BASELINE_PATH.parent.mkdir(parents=True, exist_ok=True)
        BASELINE_PATH.write_text(json.dumps({
            "note": "白口 ≤ 0（横画腔被封死）的已知欠账字形。门禁对这些不报；"
                    "任何新出现的 key 都会 FAIL。回修一个就删一个，基线只许变短。",
            "known_closed_counters": keys,
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[hcounters] 基线已更新：{len(keys)} 个字形")
        return 0

    new_closed = [f for f in closed if key_of(f) not in baseline]
    known_closed = [f for f in closed if key_of(f) in baseline]

    print(f"[hcounters] 扫了 {len(paths)} 个 recipe")
    print(f"[hcounters] 白口 < {MIN_GAP:.0f} 的横×横：{len(all_findings)} 对"
          f"（封死 {len(closed)} / 偏紧 {len(tight)}）")
    print(f"[hcounters] 已知欠账 {len(known_closed)} 对（新出现 {len(new_closed)} 对）")

    for f in new_closed:
        print(f"  [FAIL] {f['recipe']} {f['glyph']}  {f['a']}  ×  {f['b']}  gap={f['gap']}")

    report = {
        "min_gap": MIN_GAP,
        "findings": all_findings,
        "known": [key_of(f) for f in known_closed],
        "new": [key_of(f) for f in new_closed],
    }
    out = Path(args.report) if args.report else FONT_SRC / "reports" / "hcounters.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[hcounters] 报告：{out}")

    if new_closed:
        print(f"[hcounters] FAIL：{len(new_closed)} 处横画内白被封死（腔消失，渲染成黑砖）")
        return 1
    print("[hcounters] PASS")
    return 0


def _selftest() -> int:
    """注入真实错配：把某字的一条横抬到与相邻横贴死，看门禁是否多报出来。

    锚点用**源码标记**（`HC_SELFTEST_ANCHOR` 注释）定位，不写死坐标 ——
    写死坐标的话，一改字形坐标这个自证就悄悄失效（锚点找不到 → 返回 2，
    看起来像"自证失败"，其实是自证没在跑）。

    判据是**封闭对的数量**变化（不是 key 集合变化）——
    注入目标字本身可能已经在欠账里，key 不变但封闭对会多一条。
    """
    import ast
    import re
    import shutil
    import tempfile

    MARKER = "HC_SELFTEST_ANCHOR"
    src = FONT_SRC / "src" / "hkposter-cjk-core.py"
    text = src.read_text(encoding="utf-8")
    lines = text.splitlines()

    marker_idx = next((i for i, ln in enumerate(lines) if MARKER in ln), None)
    if marker_idx is None:
        print(f"[hcounters] selftest：源码里没有 {MARKER} 标记，自证失败")
        return 2

    # 顶层常量（W_THIN 之类）用于把 weight 解析成数值
    consts: dict[str, float] = {}
    for node in ast.parse(text).body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant):
            if isinstance(node.value.value, (int, float)):
                for tgt in node.targets:
                    if isinstance(tgt, ast.Name):
                        consts[tgt.id] = float(node.value.value)

    hbar_re = re.compile(r"g\.hbar\(\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^)]+)\)")

    def parse_hbar(line: str):
        m = hbar_re.search(line)
        if not m:
            return None
        vals = []
        for raw in m.groups():
            raw = raw.strip()
            if raw.startswith("weight="):
                raw = raw.split("=", 1)[1].strip()
            try:
                vals.append(float(raw))
            except ValueError:
                if raw in consts:
                    vals.append(consts[raw])
                else:
                    return None
        return vals  # x1, x2, y, weight

    # 同一函数里、标记行之上的第一条 hbar（作为「上面那条横」）
    fn_start = 0
    for i in range(marker_idx, -1, -1):
        if lines[i].startswith("def "):
            fn_start = i
            break
    prev = None
    for i in range(fn_start, marker_idx):
        got = parse_hbar(lines[i])
        if got is not None:
            prev = got
    anchor = parse_hbar(lines[marker_idx])
    if prev is None or anchor is None:
        print("[hcounters] selftest：解析锚点或上一条横失败，自证失败")
        return 2

    # 把锚点横抬到与上面那条横的墨迹重叠 10 单位 → 白口 = −10 → 腔被封死
    prev_ink_bottom = prev[2] - prev[3] / 2.0
    new_y = prev_ink_bottom + 10.0 + anchor[3] / 2.0
    new_line = re.sub(r"(g\.hbar\([^,]+,[^,]+,\s*)([^,]+)(,)",
                      lambda m: m.group(1) + f"{new_y:g}" + m.group(3),
                      lines[marker_idx], count=1)
    if new_line == lines[marker_idx]:
        print("[hcounters] selftest：没能改写锚点行，自证失败")
        return 2

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / src.name
        shutil.copy2(src, tmp)
        before = [f for f in collect(tmp) if f["closed"]]
        patched = list(lines)
        patched[marker_idx] = new_line
        tmp.write_text("\n".join(patched) + "\n", encoding="utf-8")
        after = [f for f in collect(tmp) if f["closed"]]
        if len(after) <= len(before):
            print(f"[hcounters] selftest FAIL：注入后封闭内白没有增加"
                  f"（{len(before)} → {len(after)}），分辨力不足")
            return 1
        print(f"[hcounters] selftest PASS：注入后封闭内白 {len(before)} → {len(after)}"
              f"（+{len(after) - len(before)}），门禁能抓到真实的黑砖")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
