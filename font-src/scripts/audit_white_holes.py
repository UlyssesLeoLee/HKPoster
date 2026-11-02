#!/usr/bin/env python
"""audit_white_holes —— 全库白洞扫描：找「腔被压扁」的封闭内白。

为什么需要它（docs/10 §9.14 / §9.15）
--------------------------------------
`check_hcounters.py` 只看**横 × 横的墨迹间隙**，判据是「白口 ≤ 0 = 封死」。
它判不出「腔没封死，但被压到只剩一条缝」：两条横之间还剩 1~23 单位白口时，
字面上是一条**看不见的缝**，渲染上等同黑砖，但门禁**不 FAIL**（白口 > 0）。
这不是假阳性，是门禁的判据边界。

本脚本走另一条路：把字形**栅格化** → 找被墨迹包围的白色连通区
（**封闭腔**，触边的开口不算）→ 量腔的宽高。

判据
----
- **压扁真腔**：宽 ≥ `MIN_W`（默认 40 单位）且高 < `MIN_H`（默认 24 单位）
  → 渲染上基本看不见，需要回修。**这才是缺陷。**
- **针孔**：宽 < `MIN_W` → 笔画接点上的 1~2 单位小孔，视觉上不存在，不算缺陷。

注意：参照字体自己也可能做不到 24（实测 M PLUS 1p Black 的 `警` 只有 19），
所以 24 是「我们自己的取舍线」，不是普适真理。想对照参照时加 `--ref <TTF>`。

用法
----
```
python font-src/scripts/audit_white_holes.py font-src/dist/HKPoster-Heavy.ttf
python font-src/scripts/audit_white_holes.py <TTF> --ref E:/hkposter-refs/MPLUS1p-Black.ttf
python font-src/scripts/audit_white_holes.py --selftest
```

退出码：发现压扁真腔 → 1；否则 0。

**本脚本不接入 `verify_all.py`** —— 它是**审计**不是**门禁**：
门槛值是取舍线而非硬真理，且新批次产出的密字会被误伤。
要接入前请先用 `--ref` 校准门槛，并给 `check_hcounters` 同样的注入自证。
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

# 栅格化边长（像素）。1000 upm / S → 1 像素 = 1000/S 单位。
S = 700
# 判定门槛（单位）
MIN_W = 40.0   # 腔宽下限：窄于此算针孔
MIN_H = 24.0   # 腔高下限：矮于此算压扁真腔


def _label_runs(white: np.ndarray):
    """把白色像素按行游程 + 并查集标号，返回 (runs, find)。"""
    parent: list[int] = []

    def find(a: int) -> int:
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[max(ra, rb)] = min(ra, rb)

    prev: list[tuple[int, int, int]] = []
    runs: list[tuple[int, int, int, int]] = []
    H, W = white.shape
    for y in range(H):
        row = white[y]
        cur: list[tuple[int, int, int]] = []
        idx = 0
        n = len(row)
        while idx < n:
            if not row[idx]:
                idx += 1
                continue
            start = idx
            while idx < n and row[idx]:
                idx += 1
            end = idx - 1
            lab = len(parent)
            parent.append(lab)
            for (ps, pe, pl) in prev:
                if ps <= end and start <= pe:
                    union(lab, pl)
            cur.append((start, end, lab))
            runs.append((y, start, end, lab))
        prev = cur
    return runs, find


def holes_from_mask(ink: np.ndarray) -> list[dict]:
    """从一个二值墨迹掩码里找出**封闭腔**（不触边的白色连通区）。

    ink[y, x] 为 True 表示有墨迹。返回 [{"w": 单位, "h": 单位}, ...]。
    """
    runs, find = _label_runs(~ink)
    groups: dict[int, list] = {}
    for (y, x0, x1, lab) in runs:
        groups.setdefault(find(lab), []).append((y, x0, x1))
    out = []
    for _k, rs in groups.items():
        ys = [r[0] for r in rs]
        x0s = [r[1] for r in rs]
        x1s = [r[2] for r in rs]
        # 触到画布边 = 开口，不是封闭腔
        if min(ys) == 0 or max(ys) == ink.shape[0] - 1 or min(x0s) == 0 or max(x1s) == ink.shape[1] - 1:
            continue
        out.append({
            "h": (max(ys) - min(ys) + 1) * 1000.0 / ink.shape[0],
            "w": (max(x1s) - min(x0s) + 1) * 1000.0 / ink.shape[1],
        })
    return out


def holes_of(path: str, cp: int):
    """渲染单个码位并返回它的封闭腔列表；字体读不了返回 None。"""
    try:
        font = ImageFont.truetype(path, S)
    except Exception:  # noqa: BLE001
        return None
    img = Image.new("L", (S, S), 255)
    ImageDraw.Draw(img).text((0, 0), chr(cp), font=font, fill=0)
    return holes_from_mask(np.asarray(img) < 128)


def classify(holes: list[dict]) -> tuple[list[dict], list[dict]]:
    """把腔分成 (压扁真腔, 针孔)。"""
    bad = [h for h in holes if h["w"] >= MIN_W and h["h"] < MIN_H]
    pin = [h for h in holes if h["w"] < MIN_W]
    return bad, pin


def _selftest() -> int:
    """注入实验：合成三个洞，验证「栅格化 + 连通域 + 判定」这条链真的有分辨力。

    用合成的矩形环而不是真实字体，这样测的判据与被测字形无关 ——
    证的是「工具能不能把一个已知的压扁腔挑出来」，不是「这个字好不好看」。
    """
    px = 1000.0 / S  # 1 像素 = 1000/S 单位

    def ring(hole_w_units: float, hole_h_units: float) -> np.ndarray:
        img = Image.new("L", (S, S), 255)
        d = ImageDraw.Draw(img)
        hw = int(round(hole_w_units / px))
        hh = int(round(hole_h_units / px))
        x0, y0 = (S - hw) // 2, (S - hh) // 2
        x1, y1 = x0 + hw - 1, y0 + hh - 1
        # 外框（墨）
        d.rectangle([x0 - 40, y0 - 40, x1 + 40, y1 + 40], fill=0)
        # 内洞（白）
        d.rectangle([x0, y0, x1, y1], fill=255)
        return np.asarray(img) < 128

    cases = [
        ("压扁真腔：宽 60 / 高 10", ring(60, 10), "bad"),
        ("偏窄不判：宽 60 / 高 30", ring(60, 30), "ok"),
        ("针孔：宽 20 / 高 10", ring(20, 10), "pin"),
    ]
    fails = 0
    for label, ink, expect in cases:
        holes = holes_from_mask(ink)
        bad, pin = classify(holes)
        got = "bad" if bad else ("pin" if pin else "ok")
        ok = got == expect
        if not ok:
            fails += 1
        detail = ", ".join("w=%.0f h=%.0f" % (h["w"], h["h"]) for h in holes) or "无洞"
        print("  [%s] %s -> 判定=%s（期望 %s）  洞：%s"
              % ("OK " if ok else "FAIL", label, got, expect, detail))
    if fails:
        print("[selftest] FAIL：%d 个用例没过 —— 工具没有分辨力" % fails)
        return 1
    print("[selftest] PASS：3 个用例全过 —— 压扁腔/偏窄/针孔 三类分得开")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="全库白洞扫描（压扁腔审计）")
    ap.add_argument("ttf", nargs="?", help="成品 TTF 路径")
    ap.add_argument("--ref", help="参照字体 TTF（可选），用来对照同字的腔高")
    ap.add_argument("--selftest", action="store_true", help="注入实验：自证分辨力")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()
    if not args.ttf:
        ap.print_help()
        return 2
    ttf = Path(args.ttf)
    if not ttf.exists():
        print("[audit] 找不到字体：%s" % ttf)
        return 2

    f = TTFont(str(ttf))
    cps = sorted(f.getBestCmap().keys())
    print("扫描 %d 个码位（S=%d，判据：封闭腔 宽≥%.0f 且 高<%.0f）"
          % (len(cps), S, MIN_W, MIN_H))
    bad: list[tuple[int, float, int]] = []
    pin = 0
    for cp in cps:
        hs = holes_of(str(ttf), cp)
        if hs is None:
            continue
        thin, pins = classify(hs)
        if thin:
            thin.sort(key=lambda h: h["h"])
            bad.append((cp, thin[0]["h"], len(thin)))
        pin += len(pins)

    print("  压扁真腔（宽≥%.0f 且 高<%.0f）：%d 个" % (MIN_W, MIN_H, len(bad)))
    for cp, h, n in bad:
        extra = ""
        if args.ref:
            rh = holes_of(args.ref, cp)
            if rh:
                ok = [x["h"] for x in rh if x["w"] >= MIN_W]
                extra = "  | 参照最矮 %.0f" % min(ok) if ok else "  | 参照无宽腔"
        print("    U+%04X  最矮腔 %.0f（%d 个）%s" % (cp, h, n, extra))
    print("  针孔（宽<%.0f）：%d 个（视觉上不存在，不算缺陷）" % (MIN_W, pin))
    return 1 if bad else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
