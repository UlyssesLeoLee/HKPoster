"""check_kana_size —— 假名字面尺寸是否到位的验收判据。

为什么需要
----------
用户要求假名「用海报的粗手写体写法」，即假名要和本字体的汉字
站在同一个视觉尺寸档上。这件事**必须有可执行的判据**，
否则「放大了没有」只能靠印象。

实测基线（返工前，本字体 em=1000）：

======================  ==========  ===============  ==========
                        字高中位      与汉字字高比       参照(Yu Gothic Bold)
======================  ==========  ===============  ==========
本字体 汉字              796          ——                928
本字体 平假名            586          0.736            872
本字体 片假名            601          0.756            807
======================  ==========  ===============  ==========

处置是**放大字面、不加笔画**（中心线 ×1.35 / ×1.30，笔画权重不动）。

判据
----
1. **缺字** → FAIL（与 check_kana_fidelity 同一个硬门禁）。
2. **全尺寸假名**字高落在 ``[min_h, max_h]``（默认 700..880）→ 否则 FAIL。
3. **假名/汉字字高比**（全尺寸假名中位）落在 ``[0.88, 0.95]`` → 否则 FAIL。
4. **小假名**字高落在全尺寸假名中位的 ``[0.55, 0.80]`` 倍 → 否则 FAIL。
5. 墨迹外接框不得超出 em（x 0..1000、y -120..880）。

用法
----
    python font-src/scripts/check_kana_size.py
    python font-src/scripts/check_kana_size.py --min-h 700 --max-h 880
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

if hasattr(sys, "stdout") and "reconfigure" in dir(sys.stdout):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_FONT = ROOT / "font-src" / "dist" / "HKPoster-Heavy.ttf"

KANA_RANGES = ((0x3041, 0x309F), (0x30A0, 0x30FF))

# 本身就只有一小截的符号，不参与「全尺寸」判定
INHERENTLY_SHORT = set("ー゛゜ゝゞゟヽヾ゠・…‥ヿ")

# 小假名（码位）
SMALL_KANA = {
    0x3041, 0x3043, 0x3045, 0x3047, 0x3049, 0x3083, 0x3085, 0x3087, 0x308E,
    0x3095, 0x3096, 0x30A1, 0x30A3, 0x30A5, 0x30A7, 0x30A9, 0x30C3,
    0x30E3, 0x30E5, 0x30E7, 0x30EE, 0x30F5, 0x30F6,
}

# 用来量「汉字字高」的样本（本字体已做的繁体 + Jōyō）
CJK_SAMPLE = "港影城火夜風龍義警愛無道時間部党業新場員開問高動"


def _bounds(glyphset, name):
    bp = BoundsPen(glyphset)
    try:
        glyphset[name].draw(bp)
    except Exception:
        return None
    return bp.bounds


def main() -> int:
    ap = argparse.ArgumentParser(description="假名字面尺寸验收")
    ap.add_argument("--font", default=str(DEFAULT_FONT))
    ap.add_argument("--min-h", type=int, default=700, help="全尺寸假名字高下限")
    ap.add_argument("--max-h", type=int, default=880, help="全尺寸假名字高上限")
    ap.add_argument("--ratio-min", type=float, default=0.88, help="假名/汉字字高比下限")
    ap.add_argument("--ratio-max", type=float, default=0.95, help="假名/汉字字高比上限")
    ap.add_argument("--small-lo", type=float, default=0.55, help="小假名/全尺寸假名 下限")
    ap.add_argument("--small-hi", type=float, default=0.80, help="小假名/全尺寸假名 上限")
    ap.add_argument("--report", default=str(ROOT / "font-src" / "reports" / "kana-size.json"))
    args = ap.parse_args()

    font_path = Path(args.font).resolve()
    if not font_path.exists():
        print(f"[kana-size] 找不到字体：{font_path}")
        return 1
    f = TTFont(str(font_path))
    cmap = f.getBestCmap()
    gs = f.getGlyphSet()

    cjk_h = []
    for ch in CJK_SAMPLE:
        n = cmap.get(ord(ch))
        if not n:
            continue
        b = _bounds(gs, n)
        if b:
            cjk_h.append(b[3] - b[1])
    cjk_median = statistics.median(cjk_h) if cjk_h else None

    missing, full, small, overflow = [], [], [], []
    for lo, hi in KANA_RANGES:
        for cp in range(lo, hi + 1):
            ch = chr(cp)
            n = cmap.get(cp)
            if not n:
                missing.append({"char": ch, "codepoint": f"U+{cp:04X}"})
                continue
            b = _bounds(gs, n)
            if not b:
                continue
            h = b[3] - b[1]
            w = b[2] - b[0]
            rec = {"char": ch, "codepoint": f"U+{cp:04X}", "height": h, "width": w,
                   "box": [round(v, 1) for v in b]}
            if b[0] < 0 or b[2] > 1000 or b[1] < -120 or b[3] > 880:
                overflow.append(rec)
            if cp in SMALL_KANA:
                small.append(rec)
            elif ch not in INHERENTLY_SHORT:
                full.append(rec)

    full_h = [r["height"] for r in full]
    full_median = statistics.median(full_h) if full_h else 0
    ratio = (full_median / cjk_median) if (cjk_median and full_median) else 0

    too_small = [r for r in full if r["height"] < args.min_h]
    too_tall = [r for r in full if r["height"] > args.max_h]
    small_bad = []
    for r in small:
        if not full_median:
            continue
        rel = r["height"] / full_median
        if not (args.small_lo <= rel <= args.small_hi):
            small_bad.append({**r, "rel": round(rel, 3)})

    print("[kana-size] 汉字字高中位 = %s" % (round(cjk_median, 1) if cjk_median else "N/A"))
    print("[kana-size] 全尺寸假名字高中位 = %.1f  (n=%d)" % (full_median, len(full)))
    print("[kana-size] 假名/汉字 字高比 = %.3f  (目标 %.2f..%.2f)"
          % (ratio, args.ratio_min, args.ratio_max))

    problems = 0
    if missing:
        problems += len(missing)
        print(f"[kana-size] FAIL 缺字 {len(missing)} 个：")
        for r in missing:
            print("  %s  %s" % (r["char"], r["codepoint"]))
    if too_small:
        problems += len(too_small)
        print(f"[kana-size] FAIL 偏小（<{args.min_h}）{len(too_small)} 个：")
        for r in sorted(too_small, key=lambda x: x["height"])[:20]:
            print("  %s  %s  h=%d" % (r["char"], r["codepoint"], r["height"]))
    if too_tall:
        problems += len(too_tall)
        print(f"[kana-size] FAIL 偏高（>{args.max_h}）{len(too_tall)} 个：")
        for r in sorted(too_tall, key=lambda x: -x["height"])[:20]:
            print("  %s  %s  h=%d" % (r["char"], r["codepoint"], r["height"]))
    if small_bad:
        problems += len(small_bad)
        print(f"[kana-size] FAIL 小假名比例不在 "
              f"{args.small_lo}..{args.small_hi}：")
        for r in small_bad[:20]:
            print("  %s  %s  h=%d  rel=%.2f" % (r["char"], r["codepoint"], r["height"], r["rel"]))
    if overflow:
        problems += len(overflow)
        print(f"[kana-size] FAIL 超出 em 边界 {len(overflow)} 个：")
        for r in overflow[:20]:
            print("  %s  %s  box=%s" % (r["char"], r["codepoint"], r["box"]))
    if not (args.ratio_min <= ratio <= args.ratio_max):
        problems += 1
        print(f"[kana-size] FAIL 假名/汉字字高比 {ratio:.3f} 不在 "
              f"{args.ratio_min}..{args.ratio_max}")

    report = {
        "font": str(font_path),
        "cjk_median_height": cjk_median,
        "kana_full_median_height": full_median,
        "ratio": round(ratio, 4),
        "missing": missing,
        "too_small": too_small,
        "too_tall": too_tall,
        "small_off": small_bad,
        "overflow": overflow,
        "problems": problems,
    }
    out = Path(args.report).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[kana-size] 报告：{out}")

    if problems:
        print(f"[kana-size] 失败项 {problems} 个")
        return 1
    print("[kana-size] PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
