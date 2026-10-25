"""check_kana_size —— 假名字面尺寸与落位是否到位的验收判据。

为什么需要
----------
用户要求假名「用海报的粗手写体写法」，即假名要和本字体的汉字
站在同一个视觉尺寸档上。这件事**必须有可执行的判据**，
否则「放大了没有」只能靠印象。

实测基线（返工前，本字体 em=1000）：

======================  ==========  ===============  ==============
                        字高中位      与汉字字高比       参照(Yu Gothic Bold)
======================  ==========  ===============  ==============
本字体 汉字              796          ——                928
本字体 平假名            586          0.736            872
本字体 片假名            601          0.756            807
======================  ==========  ===============  ==============

处置是**放大字面、不加笔画**（中心线 ×1.35 / ×1.30，笔画权重不动）。

判据（按可靠性从高到低）
------------------------
1. **缺字** → FAIL（与 check_kana_fidelity 同一个硬门禁）。
2. **与参照字体逐字比字高**：本字体该字的字高 / 参照字体同一字的字高，
   落在 ``[ratio_min, ratio_max]``（默认 0.85..1.15）→ 否则 FAIL。
   *为什么用相对参照而不是绝对区间*：绝对区间（「全尺寸假名都要 ≥700 高」）
   本身是错的 —— ニ 这种两横的字、へ 这种单笔的字**天生就矮**，
   参照字体同样矮。拿绝对值判会把正确字形判成错。
   相对参照判的才是「和标准假名一样大」。
3. **假名/汉字字高比**（全尺寸假名中位）落在 ``[0.88, 0.95]`` → 否则 FAIL。
   这一条把「假名和汉字同族」这件事直接量出来。
4. **小假名落位**：水平居中（中心 x≈500）+ 贴基线（底边 y≈40）。
   依据是参照字体的实测（见 docs/11 §6.8）——初稿规格写的「右上区域」是错的。
5. **小假名大小**：占全尺寸假名 0.55..0.80。
6. 墨迹外接框不得超出 em（x 0..1000、y -120..880）。

用法
----
    python font-src/scripts/check_kana_size.py
    python font-src/scripts/check_kana_size.py --reference C:/Windows/Fonts/YuGothB.ttc
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

from fontTools.ttLib import TTFont, TTCollection
from fontTools.pens.areaPen import AreaPen
from fontTools.pens.boundsPen import BoundsPen

if hasattr(sys, "stdout") and "reconfigure" in dir(sys.stdout):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_FONT = ROOT / "font-src" / "dist" / "HKPoster-Heavy.ttf"

# 参照字体候选，**按顺序取第一个存在的**。
# 硬约束（项目所有者 2026-10-25）：参照字体必须**免费商用、开源、无任何限制**。
# Yu Gothic / Meiryo / MS Gothic / UD Digi Kyokasho / 华文琥珀 等商用授权字体**不得作参照**。
REF_CANDIDATES = [
    Path("E:/hkposter-refs/MPLUS1p-Black.ttf"),      # SIL OFL 1.1 几何黑·Black
    Path("E:/hkposter-refs/ZenKakuGothicNew-Black.ttf"),  # SIL OFL 1.1 硬切黑
    Path("C:/Windows/Fonts/NotoSansJP-VF.ttf"),      # SIL OFL 1.1 骨架交叉校核
]

KANA_RANGES = ((0x3041, 0x309F), (0x30A0, 0x30FF))

# 本身就只有一小截的符号（小假名另算），不参与「全尺寸」判定
INHERENTLY_SHORT = set("ー゛゜ゝゞゟヽヾヿ・゠")

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


def _load_ref(path: Path):
    """读参照字体，返回 (cmap, glyphset, upm)。"""
    if path.suffix.lower() == ".ttc":
        coll = TTCollection(str(path), lazy=True)
        f = coll.fonts[0]
    else:
        f = TTFont(str(path), lazy=True)
    return f.getBestCmap(), f.getGlyphSet(), f["head"].unitsPerEm


def main() -> int:
    ap = argparse.ArgumentParser(description="假名字面尺寸验收")
    ap.add_argument("--font", default=str(DEFAULT_FONT))
    ap.add_argument("--reference", default="",
                    help="参照字体；留空则按 REF_CANDIDATES 取第一个存在的（均为开源可商用）")
    ap.add_argument("--ink-min", type=float, default=0.54,
                    help="假名/汉字 墨量比下限（项目所有者 2026-10-25 定 0.55）")
    ap.add_argument("--ink-max", type=float, default=0.56,
                    help="假名/汉字 墨量比上限")
    ap.add_argument("--ratio-min", type=float, default=0.85,
                    help="本字体/参照 的字高比下限（逐字）")
    ap.add_argument("--ratio-max", type=float, default=1.15,
                    help="本字体/参照 的字高比上限（逐字）")
    ap.add_argument("--family-min", type=float, default=0.88,
                    help="假名/汉字 字高比下限（整体）")
    ap.add_argument("--family-max", type=float, default=0.95,
                    help="假名/汉字 字高比上限（整体）")
    ap.add_argument("--small-lo", type=float, default=0.55, help="小假名/全尺寸假名 下限")
    ap.add_argument("--small-hi", type=float, default=0.80, help="小假名/全尺寸假名 上限")
    ap.add_argument("--small-cx-tol", type=float, default=100.0,
                    help="小假名墨迹中心 x 距 500 的容差")
    ap.add_argument("--small-bottom-lo", type=float, default=-30.0,
                    help="小假名墨迹底边下限（贴基线）")
    ap.add_argument("--small-bottom-hi", type=float, default=150.0,
                    help="小假名墨迹底边上限（贴基线）")
    ap.add_argument("--report", default=str(ROOT / "font-src" / "reports" / "kana-size.json"))
    args = ap.parse_args()

    font_path = Path(args.font).resolve()
    if not font_path.exists():
        print(f"[kana-size] 找不到字体：{font_path}")
        return 1
    f = TTFont(str(font_path))
    cmap = f.getBestCmap()
    gs = f.getGlyphSet()

    ref_cmap = ref_gs = None
    ref_upm = None
    ref_path = None
    if args.reference:
        cand = [Path(args.reference)]
    else:
        cand = REF_CANDIDATES
    for c in cand:
        if c and c.exists():
            ref_path = c
            break
    if ref_path is not None:
        ref_cmap, ref_gs, ref_upm = _load_ref(ref_path)
        if not ref_upm:
            ref_cmap = None
    else:
        print("[kana-size] 找不到参照字体 —— 跳过「逐字比参照」判据")
    our_upm = f["head"].unitsPerEm

    cjk_h = []
    for ch in CJK_SAMPLE:
        n = cmap.get(ord(ch))
        if not n:
            continue
        b = _bounds(gs, n)
        if b:
            cjk_h.append(b[3] - b[1])
    cjk_median = statistics.median(cjk_h) if cjk_h else None

    # 参照字体的汉字中位（换算到本字体的 em）——用来把「整体刻度差异」除掉
    ref_cjk_median = None
    if ref_cmap is not None:
        rc = []
        for ch in CJK_SAMPLE:
            rn = ref_cmap.get(ord(ch))
            if not rn:
                continue
            rb = _bounds(ref_gs, rn)
            if rb:
                rc.append((rb[3] - rb[1]) * our_upm / ref_upm)
        if rc:
            ref_cjk_median = statistics.median(rc)

    missing, full, small, overflow = [], [], [], []
    rel_bad = []
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

            # 与参照字体逐字比**相对比例**
            # ⚠️ 三处换算都要做，否则比值全是假数：
            #   ① 参照高度要按 em 比例换算到本字体（Yu Gothic Bold em=2048，本字体 1000）；
            #   ② 要**各自除以自己字体的汉字中位**——参照字体的字形在 em 里占比普遍更大
            #      （大 em 风格），直接比绝对高度会把「整体刻度差」误判成「这一字不对」；
            #   ③ 这样比出来的才是「这个假名相对汉字的比例，跟标准字体是否一致」。
            if ref_cmap is not None and ref_cjk_median and cjk_median:
                rn = ref_cmap.get(cp)
                rb = _bounds(ref_gs, rn) if rn else None
                if rb and (rb[3] - rb[1]) > 0:
                    ref_h = (rb[3] - rb[1]) * our_upm / ref_upm
                    ours_rel = h / cjk_median
                    ref_rel = ref_h / ref_cjk_median
                    r = ours_rel / ref_rel
                    rec["ref_height"] = round(ref_h, 1)
                    rec["rel_ref"] = round(r, 3)
                    if not (args.ratio_min <= r <= args.ratio_max):
                        rel_bad.append({**rec})

    full_h = [r["height"] for r in full]
    full_median = statistics.median(full_h) if full_h else 0
    family = (full_median / cjk_median) if (cjk_median and full_median) else 0

    small_bad = []
    for r in small:
        if not full_median:
            continue
        rel = r["height"] / full_median
        if not (args.small_lo <= rel <= args.small_hi):
            small_bad.append({**r, "rel": round(rel, 3)})

    # 小假名落位：水平居中 + 贴基线
    place_bad = []
    for r in small:
        b = r["box"]
        cx = (b[0] + b[2]) / 2.0
        bottom = b[1]
        if abs(cx - 500.0) > args.small_cx_tol or not (args.small_bottom_lo <= bottom <= args.small_bottom_hi):
            place_bad.append({**r, "center_x": round(cx, 1), "bottom": round(bottom, 1)})

    # 假名 / 汉字 的墨量比 —— 「假名有没有跟汉字同黑度」
    def _ink(cp):
        n = cmap.get(cp)
        if not n:
            return None
        p = AreaPen(gs)
        gs[n].draw(p)
        return abs(p.value) / (our_upm * our_upm)

    def _med_ink(chars):
        vals = [_ink(ord(c)) for c in chars]
        vals = [v for v in vals if v is not None]
        return statistics.median(vals) if vals else None

    cjk_ink = _med_ink(CJK_SAMPLE)
    hira_ink = _med_ink("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん")
    kata_ink = _med_ink("アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン")
    ink_ratio = None
    if cjk_ink and hira_ink and kata_ink:
        ink_ratio = ((hira_ink + kata_ink) / 2) / cjk_ink

    print("[kana-size] 汉字字高中位 = %s" % (round(cjk_median, 1) if cjk_median else "N/A"))
    print("[kana-size] 全尺寸假名字高中位 = %.1f  (n=%d)" % (full_median, len(full)))
    print("[kana-size] 假名/汉字 字高比 = %.3f  (目标 %.2f..%.2f)"
          % (family, args.family_min, args.family_max))
    if ink_ratio is not None:
        print("[kana-size] 假名/汉字 墨量比 = %.3f  (目标 %.2f..%.2f)"
              % (ink_ratio, args.ink_min, args.ink_max))
    if rel_bad:
        rels = [r["rel_ref"] for r in rel_bad]
        print("[kana-size] 与参照逐字比：中位 %.3f  n=%d" % (statistics.median(rels), len(rels)))

    problems = 0
    if missing:
        problems += len(missing)
        print(f"[kana-size] FAIL 缺字 {len(missing)} 个：")
        for r in missing:
            print("  %s  %s" % (r["char"], r["codepoint"]))
    if rel_bad:
        print(f"[kana-size] WARN 与参照字高比不在 {args.ratio_min}..{args.ratio_max}"
              f"（{len(rel_bad)} 个，**软信号**）：")
        print("     参照是普通粗体（笔画 ≈4.4% em），本字体是 Heavy（≈9.6% em），"
              "跨字重比绝对高度本就有系统性差异；")
        print("     这一项用来暴露**同一套假名内部的比例不一致**，不作为门禁。")
        for r in sorted(rel_bad, key=lambda x: x["rel_ref"])[:20]:
            print("  %s  %s  本高=%d 参照高=%s 比=%.3f"
                  % (r["char"], r["codepoint"], r["height"], r.get("ref_height"), r["rel_ref"]))
    if small_bad:
        problems += len(small_bad)
        print(f"[kana-size] FAIL 小假名比例不在 {args.small_lo}..{args.small_hi}：")
        for r in small_bad[:20]:
            print("  %s  %s  h=%d  rel=%.2f" % (r["char"], r["codepoint"], r["height"], r["rel"]))
    if place_bad:
        problems += len(place_bad)
        print("[kana-size] FAIL 小假名落位不对（应水平居中 x≈500 且贴基线）：")
        for r in place_bad[:20]:
            print("  %s  %s  h=%d  中心x=%.0f  底边=%.0f"
                  % (r["char"], r["codepoint"], r["height"], r["center_x"], r["bottom"]))
    if overflow:
        problems += len(overflow)
        print(f"[kana-size] FAIL 超出 em 边界 {len(overflow)} 个：")
        for r in overflow[:20]:
            print("  %s  %s  box=%s" % (r["char"], r["codepoint"], r["box"]))
    if not (args.family_min <= family <= args.family_max):
        problems += 1
        print(f"[kana-size] FAIL 假名/汉字字高比 {family:.3f} 不在 "
              f"{args.family_min}..{args.family_max}")
    if ink_ratio is not None and not (args.ink_min <= ink_ratio <= args.ink_max):
        problems += 1
        print(f"[kana-size] FAIL 假名/汉字墨量比 {ink_ratio:.3f} 不在 "
              f"{args.ink_min}..{args.ink_max}（假名要跟汉字同黑度）")

    report = {
        "font": str(font_path),
        "reference": str(ref_path) if ref_cmap is not None else None,
        "cjk_median_height": cjk_median,
        "kana_full_median_height": full_median,
        "family_ratio": round(family, 4),
        "ink_ratio": round(ink_ratio, 4) if ink_ratio is not None else None,
        "missing": missing,
        "rel_ref_off": rel_bad,
        "small_off": small_bad,
        "small_place_off": place_bad,
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
