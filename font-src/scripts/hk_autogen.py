"""HK Poster Heavy —— 骨架中线自动生成器。

从 hanzi-writer-data 的**笔画骨架中线**（medians）生成 recipe。

为什么用骨架而不是轮廓
----------------------
项目铁律：参照字体「只参考比例与骨架，不描轮廓」。本生成器走的是同一原则的
更严格版本 —— 数据源提供的是**每笔的中心线折线**（medians），不是字形轮廓；
本工具把中心线按本项目的笔画权重重新「粗化」，得到的是**照标准骨架画**的
字形，而不是任何字体的轮廓拷贝。

数据源
------
hanzi-writer-data（https://github.com/chanind/hanzi-writer-data）
  - `data/<字>.json` → `medians`：每笔的骨架中线点列，1024×1024 网格，**y 向上**，
    按笔顺排列。覆盖约 9,000 字。
  - 许可证：Arphic Public License（见仓库 ARPHICPL.TXT）/ LGPL。
    **本字体若包含由本工具生成的字形，其许可证必须与该许可兼容** ——
    这一点与项目自身的许可证拍板（G4 门禁）直接相关，未拍板前不得公开发布。

坐标标定
--------
用参照字体 M PLUS 1p Black（1000 upm）的**墨迹框**做逐字标定：
把中线框等比映射到「参照墨迹框内缩 w/2」的目标框（w = 本字笔画权重），
使本字体的墨迹外廓 ≈ 参照字体的墨迹外廓 —— 这正是「参考比例与骨架」的含义。
参照字体里没有的字回退到全局映射（1024 网格 → 字面框）。

笔画权重
--------
按**局部拥挤度**逐笔定档：某笔中心线到最近其他笔中心线的距离为 d，
则该笔权重取 ≤ d − 24 的最大档位（白口下限 24）。
档位阶梯 96 / 92 / 84 / 76 / 64（CJK 档）。
"""

from __future__ import annotations

import json
import math
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

# ── 本项目常量（与 font-src/scripts/hkbuild.py 对齐）────────────────────
UPM = 1000
FACE_X0, FACE_X1 = 60.0, 940.0
FACE_Y0, FACE_Y1 = 0.0, 820.0
ASCENDER, DESCENDER = 880.0, -120.0

# CJK 笔画权重档（粗 → 细）
WEIGHTS = (96.0, 92.0, 84.0, 76.0, 64.0)
W_MIN_GAP = 24.0          # 横画白口下限（AGENTS.md 铁律 10）

# 点/短撇的斜切档（house style）
SLANT_RIGHT_DOWN = -14.0   # 右下点 丶
SLANT_LEFT_DOWN = 14.0     # 左下点 丿
SLANT_SHORT_PIE = 26.0     # 短撇
SLANT_VERTICAL = 0.0       # 竖点

DATA_URL = ("https://raw.githubusercontent.com/chanind/hanzi-writer-data/master/"
            "data/%s.json")
CACHE_DIR = Path(__file__).resolve().parents[1] / "data" / "hanzi-cache"

# ── 参照字体（标定用）──────────────────────────────────────────────────
REF_FONT = Path("E:/hkposter-refs/MPLUS1p-Black.ttf")


# ── 数据获取 ───────────────────────────────────────────────────────────
def fetch_medians(ch: str) -> list[list[tuple[float, float]]] | None:
    """取某字的骨架中线（1024 网格，y 向上）。取不到返回 None。"""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cp = CACHE_DIR / ("%04X.json" % ord(ch))
    if not cp.exists():
        url = DATA_URL % urllib.parse.quote(ch)
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                cp.write_bytes(r.read())
        except Exception:
            return None
    try:
        d = json.loads(cp.read_text(encoding="utf-8"))
    except Exception:
        return None
    return d.get("medians") or None


# ── 参照字体墨迹框 ─────────────────────────────────────────────────────
_REF_CACHE: dict[str, tuple] = {}


def ref_ink_box(ch: str):
    """参照字体的墨迹框（1000 upm）：(x0, y0, x1, y1)。"""
    if ch in _REF_CACHE:
        return _REF_CACHE[ch]
    box = None
    try:
        from fontTools.ttLib import TTFont
        from fontTools.pens.boundsPen import BoundsPen
        path = REF_FONT
        if not path.exists():
            path = Path("E:/hkposter-refs/MPLUS1p-Black.ttf")
        if path.exists():
            font = TTFont(str(path))
            cmap = font.getBestCmap()
            gs = font.getGlyphSet()
            if ord(ch) in cmap:
                bp = BoundsPen(gs)
                gs[cmap[ord(ch)]].draw(bp)
                if bp.bounds:
                    box = tuple(float(v) for v in bp.bounds)
            font.close()
    except Exception:
        box = None
    _REF_CACHE[ch] = box
    return box


# ── 坐标映射 ───────────────────────────────────────────────────────────
def make_transform(pts_all, ch: str, weight: float):
    """由**全部笔画**的中线框算出一个统一变换（1024 网格 → 本项目坐标）。

    有参照字体时按参照墨迹框逐字标定（等比 + 居中），
    没有时回退到全局映射（x 0..1024 → 60..940，y 0..900 → 0..820）。
    """
    xs = [p[0] for p in pts_all]
    ys = [p[1] for p in pts_all]
    hx0, hx1, hy0, hy1 = min(xs), max(xs), min(ys), max(ys)

    box = ref_ink_box(ch)
    if box is not None:
        rx0, ry0, rx1, ry1 = box
        # 目标：中线框落在「参照墨迹框内缩 w/2」里
        tx0, tx1 = rx0 + weight / 2, rx1 - weight / 2
        ty0, ty1 = ry0 + weight / 2, ry1 - weight / 2
        if tx1 - tx0 < 40 or ty1 - ty0 < 40:
            tx0, tx1, ty0, ty1 = FACE_X0, FACE_X1, FACE_Y0, FACE_Y1
    else:
        tx0, tx1 = FACE_X0, FACE_X1
        ty0, ty1 = FACE_Y0, FACE_Y1

    sw = max(hx1 - hx0, 1e-6)
    sh = max(hy1 - hy0, 1e-6)
    s = min((tx1 - tx0) / sw, (ty1 - ty0) / sh)
    # 等比缩放后居中
    ox = tx0 + ((tx1 - tx0) - sw * s) / 2 - hx0 * s
    oy = ty0 + ((ty1 - ty0) - sh * s) / 2 - hy0 * s
    return lambda pts: [(ox + x * s, oy + y * s) for (x, y) in pts]


# ── 折线简化与分段 ─────────────────────────────────────────────────────
def _dedup(pts, tol=1.5):
    out = []
    for p in pts:
        if not out or (abs(p[0] - out[-1][0]) + abs(p[1] - out[-1][1])) > tol:
            out.append(p)
    return out


def split_segments(pts, fold_deg=35.0):
    """把中线折线拆成「折笔」分段。

    只有**真正的折角**（局部转折 ≥ fold_deg，如横折、竖钩）才断段；
    平滑的曲线（撇、捺、横的轻微起笔）不断段 —— 否则一段横会被切成
    「斜 + 横 + 斜」三段，端头被切出毛刺（实测 一 字就是这么坏的）。

    返回 [[p0, p1, ...], ...]
    """
    pts = _dedup(pts)
    if len(pts) < 2:
        return []
    pieces = []
    cur = [pts[0]]
    for i in range(1, len(pts) - 1):
        ax, ay = pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]
        bx, by = pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]
        la, lb = math.hypot(ax, ay), math.hypot(bx, by)
        if la < 1e-6 or lb < 1e-6:
            continue
        cosv = (ax * bx + ay * by) / (la * lb)
        cosv = max(-1.0, min(1.0, cosv))
        ang = math.degrees(math.acos(cosv))
        cur.append(pts[i])
        if ang >= fold_deg:
            pieces.append(cur)
            cur = [pts[i]]
    cur.append(pts[-1])
    pieces.append(cur)
    return [p for p in pieces if len(p) >= 2]


def _chord(pts):
    """整段的首尾方向（用于把平滑曲线归为一笔直线）。"""
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    return math.hypot(x2 - x1, y2 - y1)


def _turn_deg(d1, d2):
    la, lb = math.hypot(*d1), math.hypot(*d2)
    if la < 1e-9 or lb < 1e-9:
        return 0.0
    cosv = (d1[0] * d2[0] + d1[1] * d2[1]) / (la * lb)
    return math.degrees(math.acos(max(-1.0, min(1.0, cosv))))


# ── 笔画原语化 ─────────────────────────────────────────────────────────
def _seg_kind(p1, p2, tol=0.45):
    """横/竖/斜判定。

    容差 0.45 ≈ 24°：数据源是**楷体**骨架，竖画带 10~20° 斜度、横画带起笔
    起伏。本字体是海报黑体，必须把这些近轴向笔画吸附成真正的横/竖，
    否则 口/日/中 这类方框会变成歪斜的梯形（实测 Kai 源的口左竖斜 15°）。
    斜画（撇/捺）的角度原样保留。
    """
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    adx, ady = abs(dx), abs(dy)
    if ady <= tol * adx:
        return "hbar"
    if adx <= tol * ady:
        return "vbar"
    return "diag"


def _snap_axis(p1, p2, kind):
    """把近轴向笔画的端点吸附到轴上（保留中点与跨度）。"""
    if kind == "hbar":
        y = (p1[1] + p2[1]) / 2
        return (p1[0], y), (p2[0], y)
    if kind == "vbar":
        x = (p1[0] + p2[0]) / 2
        return (x, p1[1]), (x, p2[1])
    return p1, p2


def _lsq_line(pts):
    """最小二乘拟合直线。返回 (点 p0, 单位方向 u, 拟合长度)。"""
    n = len(pts)
    mx = sum(p[0] for p in pts) / n
    my = sum(p[1] for p in pts) / n
    sxx = sum((p[0] - mx) ** 2 for p in pts)
    sxy = sum((p[0] - mx) * (p[1] - my) for p in pts)
    if sxx < 1e-9:
        # 竖直：x 恒定
        return (mx, my), (0.0, 1.0), abs(pts[-1][1] - pts[0][1])
    slope = sxy / sxx
    u = (1.0, slope)
    L = math.hypot(u[0], u[1])
    u = (u[0] / L, u[1] / L)
    # 沿 u 方向的投影长度
    ts = [((p[0] - mx) * u[0] + (p[1] - my) * u[1]) for p in pts]
    return (mx, my), u, max(ts) - min(ts)


def _isect(a0, au, b0, bu, max_d):
    """两条直线求交；交点过远或近乎平行时返回 None。"""
    cross = au[0] * bu[1] - au[1] * bu[0]
    if abs(cross) < 1e-6:
        return None
    dx = b0[0] - a0[0]
    dy = b0[1] - a0[1]
    t = (dx * bu[1] - dy * bu[0]) / cross
    p = (a0[0] + au[0] * t, a0[1] + au[1] * t)
    if math.hypot(p[0] - b0[0], p[1] - b0[1]) > max_d:
        return None
    return p


def fit_pieces(pts, weight, fold_deg=30.0):
    """把一条笔画中线拟合成 1..n 条**直线**（折笔的每一段）。

    做法：
      1. 局部方向变化 ≥ fold_deg 处判为折角；
      2. 相邻折角距离过近时合并；
      3. 每段用最小二乘拟合直线；
      4. 内部「倒角段」（拟合长度 < 0.8×笔宽）丢弃 —— 源字体的圆角
         在中线上留下的一小段斜线，保留会在折角处画出多余的斜切；
      5. 折角位置 = 相邻两段拟合直线的**求交点**（真正的斜接角）。

    返回 [(起点, 终点), ...]
    """
    pts = _dedup(pts)
    n = len(pts)
    if n < 2:
        return []
    dirs = [(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]) for i in range(n - 1)]

    folds = []
    for i in range(1, n - 1):
        if _turn_deg(dirs[i - 1], dirs[i]) >= fold_deg:
            folds.append(i)
    merged = []
    lim = (0.9 * weight) ** 2
    for i in folds:
        if merged and (pts[i][0] - pts[merged[-1]][0]) ** 2 + \
                (pts[i][1] - pts[merged[-1]][1]) ** 2 < lim:
            if _turn_deg(dirs[i - 1], dirs[i]) > _turn_deg(dirs[merged[-1] - 1], dirs[merged[-1]]):
                merged[-1] = i
        else:
            merged.append(i)

    bounds = [0] + merged + [n - 1]
    segs = []
    for k in range(len(bounds) - 1):
        a, b = bounds[k], bounds[k + 1]
        if b > a:
            segs.append(pts[a:b + 1])
    if not segs:
        return []

    fits = [_lsq_line(s) for s in segs]
    # 丢弃内部倒角段
    keep = [k for k, f in enumerate(fits)
            if k == 0 or k == len(fits) - 1 or f[2] >= 0.8 * weight]
    fits = [fits[k] for k in keep]
    if not fits:
        return []
    if len(fits) == 1:
        return [(pts[0], pts[-1])]

    corners = []
    for k in range(len(fits) - 1):
        (a0, au, _), (b0, bu, _) = fits[k], fits[k + 1]
        c = _isect(a0, au, b0, bu, max_d=3.0 * weight)
        if c is None:
            c = ((a0[0] + b0[0]) / 2, (a0[1] + b0[1]) / 2)
        corners.append(c)

    out = []
    for k in range(len(fits)):
        p_start = pts[0] if k == 0 else corners[k - 1]
        p_end = pts[-1] if k == len(fits) - 1 else corners[k]
        out.append((p_start, p_end))
    return out


def _pt_seg_dist(p, a, b):
    vx, vy = b[0] - a[0], b[1] - a[1]
    L2 = vx * vx + vy * vy
    if L2 < 1e-9:
        return math.hypot(p[0] - a[0], p[1] - a[1])
    t = max(0.0, min(1.0, ((p[0] - a[0]) * vx + (p[1] - a[1]) * vy) / L2))
    return math.hypot(p[0] - (a[0] + t * vx), p[1] - (a[1] + t * vy))


def extend_ends(strokes, weights):
    """把每条笔画的端点向最近的另一条笔画延长，让接头重新咬合。

    楷体源骨架里相邻笔画的中线端点彼此留白，靠笔宽自然搭接；
    本字体的笔画相对更细，搭接会断开（实测 日/口/中 的方框四边脱节）。
    这里把端点补到「离对方中心线 0.4×笔宽」处，两笔的墨迹重新重叠。

    只在「另一条笔画就在 1.5×笔宽以内」时补 —— 那是接头，不是字的轮廓。
    """
    out = []
    for i, st in enumerate(strokes):
        w = weights[i]
        pts = list(st)
        for endi in (0, -1):
            P = pts[endi]
            best = None
            bestd = 1e9
            for j, t in enumerate(strokes):
                if i == j:
                    continue
                for k in range(len(t) - 1):
                    d = _pt_seg_dist(P, t[k], t[k + 1])
                    if d < bestd:
                        bestd = d
                        best = t[k]
            if best is None or bestd > 1.5 * w:
                continue
            ext = max(0.0, min(1.2 * w, bestd - 0.4 * w))
            if ext <= 0:
                continue
            dx, dy = best[0] - P[0], best[1] - P[1]
            L = math.hypot(dx, dy)
            if L < 1e-6:
                continue
            newp = (P[0] + dx / L * ext, P[1] + dy / L * ext)
            if endi == 0:
                pts[0] = newp
            else:
                pts[-1] = newp
        out.append(pts)
    return out


def stroke_prims(pts, weight, kind_hint=None):
    """把一条笔画中线转成一串原语描述。

    返回 [(kind, params, meta), ...]
      hbar: ("hbar", (x1, x2, y), {})
      vbar: ("vbar", (x, y1, y2), {})
      diag: ("diag", (x1, y1, x2, y2), {})
      dot : ("dot",  (cx, cy, w, h, slant), {})
    """
    pieces = fit_pieces(pts, weight)
    if not pieces:
        return []
    total_len = sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in pieces)

    # 点 / 短撇：整笔很短且不折
    if total_len < 1.7 * weight and len(pieces) == 1:
        p1, p2 = pieces[0]
        cx, cy = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        adx, ady = abs(dx), abs(dy)
        h = max(0.55 * weight, min(1.3 * weight, total_len))
        if adx <= 0.18 * ady:
            slant = SLANT_VERTICAL
        elif dx > 0:
            slant = SLANT_RIGHT_DOWN
        else:
            slant = SLANT_SHORT_PIE if total_len < 1.15 * weight else SLANT_LEFT_DOWN
        return [("dot", (cx, cy, weight, h, slant), {})]

    prims = []
    for p1, p2 in pieces:
        kind = _seg_kind(p1, p2)
        a, b = _snap_axis(p1, p2, kind)
        if kind == "hbar":
            y = (a[1] + b[1]) / 2
            x1, x2 = sorted((a[0], b[0]))
            prims.append(("hbar", (x1, x2, y), {}))
        elif kind == "vbar":
            x = (a[0] + b[0]) / 2
            y1, y2 = sorted((a[1], b[1]))
            prims.append(("vbar", (x, y1, y2), {}))
        else:
            prims.append(("diag", (a[0], a[1], b[0], b[1]), {}))
    return prims


# ── 逐笔权重：按局部拥挤度 ─────────────────────────────────────────────
def _sample(pts, step=6.0):
    out = []
    for i in range(len(pts) - 1):
        (x1, y1), (x2, y2) = pts[i], pts[i + 1]
        d = math.hypot(x2 - x1, y2 - y1)
        n = max(1, int(d / step))
        for k in range(n + 1):
            out.append((x1 + (x2 - x1) * k / n, y1 + (y2 - y1) * k / n))
    return out


def assign_weights(strokes):
    """按「到最近其他笔中心线的距离」逐笔定权重档。"""
    samples = [_sample(s) for s in strokes]
    weights = []
    for i, s in enumerate(strokes):
        best = 1e9
        for j, t in enumerate(strokes):
            if i == j:
                continue
            # 粗略：点到线段距离
            for (px, py) in samples[i][::3]:
                for k in range(len(t) - 1):
                    ax, ay = t[k]
                    bx, by = t[k + 1]
                    vx, vy = bx - ax, by - ay
                    L2 = vx * vx + vy * vy
                    if L2 < 1e-9:
                        continue
                    tt = max(0.0, min(1.0, ((px - ax) * vx + (py - ay) * vy) / L2))
                    qx, qy = ax + tt * vx, ay + tt * vy
                    d = math.hypot(px - qx, py - qy)
                    if d < best:
                        best = d
                        if best < 30:
                            break
                if best < 30:
                    break
        limit = best - W_MIN_GAP
        w = WEIGHTS[0]
        for cand in WEIGHTS:
            if cand <= limit:
                w = cand
                break
        else:
            w = WEIGHTS[-1]
        weights.append(w)
    return weights


# ── 顶点标注 ───────────────────────────────────────────────────────────
def _vname(ch: str) -> str:
    return "uni%04X" % ord(ch)


def _fnname(ch: str) -> str:
    import unicodedata
    try:
        name = unicodedata.name(ch)
    except ValueError:
        name = "U%04X" % ord(ch)
    return "g_" + "".join(c if c.isalnum() else "_" for c in name).strip("_").lower()


# ── recipe 文本生成 ────────────────────────────────────────────────────
def build_glyph_code(ch: str, prims_by_stroke, weight_desc=""):
    fn = _fnname(ch)
    lines = []
    lines.append("def %s() -> Glyph:" % fn)
    lines.append('    """%s U+%04X —— 骨架中线自动生成。' % (ch, ord(ch)))
    lines.append("")
    lines.append("    笔画骨架来自 hanzi-writer-data 的 medians（每笔中心线），")
    lines.append("    按本项目笔画权重重新粗化 —— 照标准骨架画，不是轮廓拷贝。")
    if weight_desc:
        lines.append("    %s" % weight_desc)
    lines.append('    """')
    lines.append('    g = Glyph("%s", advance=1000, unicode=0x%04X, note="%s：自动生成")'
                 % (_vname(ch), ord(ch), ch))
    for prims, w in prims_by_stroke:
        for kind, params in prims:
            if kind == "hbar":
                x1, x2, y = params
                lines.append("    g.hbar(%.1f, %.1f, %.1f, weight=%.1f)"
                             % (x1, x2, y, w))
            elif kind == "vbar":
                x, y1, y2 = params
                lines.append("    g.vbar(%.1f, %.1f, %.1f, weight=%.1f)"
                             % (x, y1, y2, w))
            elif kind == "diag":
                x1, y1, x2, y2 = params
                lines.append("    g.diag(%.1f, %.1f, %.1f, %.1f, weight=%.1f)"
                             % (x1, y1, x2, y2, w))
            else:
                cx, cy, ww, hh, slant = params
                lines.append("    g.dot(%.1f, %.1f, w=%.1f, h=%.1f, slant=%.1f)"
                             % (cx, cy, ww, hh, slant))
    lines.append("    return g")
    return "\n".join(lines), fn


def _glyph_ok(glyph):
    """逐字质量闸：轮廓合法（无自交）+ 在 em 盒内 + advance 正确。

    与 check_glyphs.py 同口径 —— 自交的字渲染出来是糊成一块的墨，
    宁可剔除也不能混进成品。
    """
    from shapely.geometry import Polygon
    try:
        contours = glyph.contours()
    except Exception:
        return False
    if not contours:
        return False
    for c in contours:
        pts = [(p[0], p[1]) if isinstance(p, (tuple, list)) else (p.x, p.y) for p in c]
        if len(pts) < 3:
            return False
        try:
            if not Polygon(pts).is_valid:
                return False
        except Exception:
            return False
    flat = []
    for c in contours:
        for p in c:
            flat.append((p[0], p[1]) if isinstance(p, (tuple, list)) else (p.x, p.y))
    xs = [p[0] for p in flat]
    ys = [p[1] for p in flat]
    if not xs:
        return False
    if min(xs) < -20 or max(xs) > 1020 or min(ys) < DESCENDER or max(ys) > ASCENDER:
        return False
    return True


def _r(v):
    """recipe 里写出的坐标精度（1 位小数）。

    质量闸必须用**与 recipe 完全相同**的坐标来判 —— 用全精度浮点判过、
    写盘取整后才自交的字，是实测踩过的坑（口/中 的接头正好落在整数上）。
    """
    return round(float(v), 1)


def _try_build(ch, strokes, weight_desc=""):
    """生成一个字的原语列表；不合格时降重/关掉接头延长重试。

    返回 (prims_by_stroke, ok)
    """
    allpts = [p for s in strokes for p in s]
    for attempt in range(5):
        base = WEIGHTS[min(attempt, len(WEIGHTS) - 1)]
        tf = make_transform(allpts, ch, base)
        mapped = [tf(s) for s in strokes]
        ws = assign_weights(mapped)
        if attempt >= 3:
            # 最后两轮：整体降重
            ws = [min(w, WEIGHTS[min(attempt - 2, len(WEIGHTS) - 1)]) for w in ws]
        mapped2 = extend_ends(mapped, ws) if attempt < 3 else mapped
        prims_by_stroke = []
        for s, w in zip(mapped2, ws):
            prims = []
            for kind, params, _ in stroke_prims(s, w):
                if kind == "dot":
                    prims.append(("dot", tuple(_r(v) for v in params)))
                else:
                    prims.append((kind, tuple(_r(v) for v in params)))
            prims_by_stroke.append((prims, w))
        try:
            from hkbuild import Glyph
            g = Glyph("uni%04X" % ord(ch), advance=1000, unicode=ord(ch),
                      note="%s：自动生成" % ch)
            for prims, w in prims_by_stroke:
                for kind, params in prims:
                    if kind == "hbar":
                        g.hbar(*params, weight=w)
                    elif kind == "vbar":
                        g.vbar(*params, weight=w)
                    elif kind == "diag":
                        g.diag(*params, weight=w)
                    else:
                        g.dot(*params)
            if _glyph_ok(g):
                return prims_by_stroke, True
        except Exception:
            pass
    return prims_by_stroke, False


def generate(chars, master_name, out_path, base_weight=96.0, per_stroke_weight=True):
    """生成 recipe 源文件。返回 (生成的字数, 剔除的字列表)。"""
    body = []
    names = []
    failed = []
    for ch in chars:
        med = fetch_medians(ch)
        if not med:
            failed.append(ch)
            continue
        strokes = []
        for m in med:
            pts = [(float(x), float(y)) for x, y in m]
            if len(pts) < 2:
                continue
            strokes.append(pts)
        if not strokes:
            failed.append(ch)
            continue
        prims_by_stroke, ok = _try_build(ch, strokes)
        if not ok:
            failed.append(ch)
            continue
        code, fn = build_glyph_code(ch, prims_by_stroke)
        body.append(code)
        names.append((fn, ch))

    header = [
        '"""HK Poster Heavy —— 骨架中线自动生成批次 %s。' % master_name,
        "",
        "本文件由 font-src/scripts/hk_autogen.py 生成，请勿手工编辑。",
        "设计源 = hanzi-writer-data 的每笔骨架中线（medians）；",
        "按本项目笔画权重档重新粗化 —— 只取骨架，不描任何字体的轮廓。",
        "",
        "字面框 x 60..940、y 0..820，advance 1000。",
        "权重档 96 / 92 / 84 / 76 / 64，按逐笔局部拥挤度选取。",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "import sys",
        "from pathlib import Path",
        "",
        'FONT_SRC = Path(__file__).resolve().parents[1]',
        'sys.path.insert(0, str(FONT_SRC / "scripts"))',
        "",
        "from hkbuild import Glyph, write_ufo  # noqa: E402",
        "",
        "",
    ]
    tail = [
        "",
        "",
        "def build() -> list[Glyph]:",
        "    return [",
    ]
    for fn, ch in names:
        tail.append("        %s(),        # %s U+%04X" % (fn, ch, ord(ch)))
    tail.append("    ]")
    tail.append("")
    tail.append("")
    tail.append("def target_ufo() -> Path:")
    tail.append('    return FONT_SRC / "masters" / "%s.ufo"' % master_name)
    tail.append("")
    tail.append("")
    tail.append('if __name__ == "__main__":')
    tail.append("    write_ufo(target_ufo(), build())")
    tail.append('    print(f"[recipe] 已写出 {target_ufo()}")')
    tail.append("")

    Path(out_path).write_text("\n".join(header + body + tail), encoding="utf-8")
    return len(names), failed


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--chars", required=True, help="字列表文件（每行一个字或码位）")
    ap.add_argument("--out", required=True)
    ap.add_argument("--master", required=True)
    ap.add_argument("--weight", type=float, default=96.0)
    ap.add_argument("--uniform-weight", action="store_true")
    a = ap.parse_args()

    txt = Path(a.chars).read_text(encoding="utf-8")
    chars = []
    for line in txt.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("U+"):
            chars.append(chr(int(line[2:], 16)))
        else:
            chars.extend(list(line))
    n, failed = generate(chars, a.master, a.out, a.weight, not a.uniform_weight)
    print("[autogen] 生成 %d 字 → %s" % (n, a.out))
    if failed:
        print("[autogen] 取不到骨架数据 %d 个：%s" % (len(failed), "".join(failed)))
