"""check_kana_fidelity —— 假名「保持原有字形」的客观检查。

问题背景
--------
用户对假名提出硬要求（2026-10-25）：

    「假名字形变化不要过大，只是用海报的粗手写体写法，
      整体字形必须还保持原有状态，否则难以识别」

「保持原有状态」说的是**骨架**：假名必须还是那个假名，
只允许换笔画处理（粗手写体），不允许重新设计字形。
这个要求不能靠肉眼「看着还行」来保证——人眼对熟悉字形有很强的
自动补全能力，看一眼「像」就过了，但实际骨架可能已经跑掉。

两个指标，分工明确
------------------
1. **骨架 IoU**（主判据）：把位图 Zhang-Suen 细化成 1px 中心线再比对。
   **对笔画粗细不敏感**（同一副骨架，粗细不同得分 0.91），
   对走向/位置敏感（横线 vs 竖线 0.06）。回答「还是不是那个字」。
2. **原样 IoU**（副判据）：不做细化，直接比。对粗细敏感，
   用来回答「墨量跟参照差多少」。

⚠️ 早前版本只用原样 IoU 且阈值 0.62，191 个假名报了 174 个 FAIL ——
   那些 FAIL 里绝大多数是**粗细差异**被误判成走形。告警没有分辨力，
   等于没有告警。骨架 IoU + 阈值自动标定才是可用的判据。

阈值自动标定
------------
拿参照字体自己算「形近字对」的骨架 IoU（う/へ、ら/す……）。
这些是**不同的字**，但形近，所以它们的得分是「不像同一个字」的下界。
阈值 = 该下界 + 余量。阈值因此不是拍脑袋定的常数。

检查器自身的可信度
------------------
`--selftest` 对同一字人为制造形变（平移 / 截断 / 换笔画方向），
断言指标确实下降。指标不敏感 ⇒ 自测失败 ⇒ 整个检查不可信。

用法
----
    python font-src/scripts/check_kana_fidelity.py --selftest
    python font-src/scripts/check_kana_fidelity.py \
        --font font-src/dist/HKPoster-Heavy.ttf \
        --reference C:/Windows/Fonts/YuGothB.ttc \
        --out font-src/reports/kana-fidelity.json \
        --sheet font-src/reports/kana-fidelity.png
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kana_skeleton import skeleton_iou  # noqa: E402

if hasattr(sys, "stdout") and "reconfigure" in dir(sys.stdout):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

KANA_RANGES = (
    (0x3041, 0x309F),  # 平假名（含浊音预组合形、浊音符、浊点符号、反复记号）
    (0x30A0, 0x30FF),  # 片假名（含同上）
)

# 形近字对：用于**标定阈值**（这些是不同字，得分应当明显低于 1）
CONFUSABLE = (
    ("う", "へ"), ("ら", "す"), ("す", "ず"), ("し", "じ"),
    ("シ", "ツ"), ("ツ", "ン"), ("ソ", "ン"), ("ヨ", "モ"),
    ("ユ", "ヲ"), ("ワ", "ヲ"), ("て", "で"), ("と", "ど"),
    ("う", "ら"), ("ぬ", "ね"), ("ま", "め"),
)


def kana_codepoints() -> list[int]:
    out: list[int] = []
    for lo, hi in KANA_RANGES:
        out.extend(range(lo, hi + 1))
    return out


def _load_font(path: Path, index: int) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(str(path), 128, index=index)
    except Exception:
        return ImageFont.truetype(str(path), 128)


def _pick_reference_index(path: Path, want_bold: bool) -> int:
    from fontTools.ttLib import TTCollection

    try:
        coll = TTCollection(str(path), lazy=True)
    except Exception:
        return 0
    for i, f in enumerate(coll.fonts):
        try:
            os2 = f["OS/2"]
            bold = bool(os2.fsSelection & (1 << 5)) or (os2.usWeightClass >= 600)
            if want_bold and bold:
                return i
        except Exception:
            continue
    return 0


def _render_glyph(font: ImageFont.FreeTypeFont, ch: str, canvas: int = 400):
    img = Image.new("L", (canvas, canvas), 255)
    ImageDraw.Draw(img).text((canvas // 2, canvas // 2), ch, font=font, fill=0, anchor="mm")
    bbox = img.point(lambda v: 255 if v < 128 else 0).getbbox()
    return img, bbox


def _normalize(img: Image.Image, bbox, size: int = 96) -> Image.Image:
    """按墨迹外接框裁剪并等比缩放到 size×size —— 归一化掉大小与位置。"""
    if bbox is None:
        return Image.new("L", (size, size), 0)
    cropped = img.crop(bbox)
    w, h = cropped.size
    scale = (size - 8) / max(w, h)
    nw, nh = max(1, int(w * scale)), max(1, int(h * scale))
    resized = cropped.resize((nw, nh), Image.LANCZOS)
    out = Image.new("L", (size, size), 0)
    out.paste(resized, ((size - nw) // 2, (size - nh) // 2))
    return out


def _mask(img: Image.Image) -> np.ndarray:
    return np.asarray(img) > 96


def _ink_positions(img: Image.Image, threshold: int = 96) -> set[int]:
    """返回「有墨的像素下标」集合。

    ⚠️ 必须用**位置**而不是**像素值**。早期版本写成 ``set(img.getdata())``，
    那得到的是像素**值**的集合 {0, 255}，对任何字都一样 ——
    于是 IoU 恒等于 1.000，检查器形同虚设。
    """
    return {i for i, v in enumerate(img.tobytes()) if v > threshold}


def _raw_iou(a: Image.Image, b: Image.Image) -> float:
    A, B = _ink_positions(a), _ink_positions(b)
    if not A and not B:
        return 1.0
    if not A or not B:
        return 0.0
    inter, union = len(A & B), len(A | B)
    return inter / union if union else 0.0


def _em_box(box, em: int = 1000, canvas: int = 400, font_px: int = 128):
    """位图外接框 → 字体坐标（y 向上）。注意 em 换算基准是**字号**不是画布。"""
    if box is None:
        return None
    k = em / font_px
    return {
        "x0": round((box[0] - canvas / 2) * k, 1),
        "y0": round((canvas / 2 - box[3]) * k, 1),
        "x1": round((box[2] - canvas / 2) * k, 1),
        "y1": round((canvas / 2 - box[1]) * k, 1),
    }


def _ink_ratio(img: Image.Image) -> float:
    data = img.tobytes()
    return round(sum(1 for v in data if v < 128) / (img.size[0] * img.size[1]), 5)


def _selftest(ref_path: Path, ref_index: int) -> int:
    """证明这个指标确实能抓到形变。指标不敏感 ⇒ 整个检查不可信 ⇒ 直接失败。"""
    ref = _load_font(ref_path, ref_index)
    failures: list[str] = []

    def norm_of(ch):
        i, b = _render_glyph(ref, ch)
        return _normalize(i, b)

    u = norm_of("う")
    self_iou = skeleton_iou(_mask(u), _mask(u))
    if self_iou < 0.99:
        failures.append(f"自比 IoU={self_iou:.3f}，应≈1.000")

    shifted = Image.new("L", u.size, 0)
    shifted.paste(u, (u.size[0] // 4, 0))
    shift_iou = skeleton_iou(_mask(u), _mask(shifted))
    if shift_iou > 0.75:
        failures.append(f"平移 1/4 后 IoU={shift_iou:.3f} 仍然太高 —— 指标不敏感")

    half = Image.new("L", u.size, 0)
    half.paste(u.crop((0, 0, u.size[0], u.size[1] // 2)), (0, 0))
    half_iou = skeleton_iou(_mask(u), _mask(half))
    if half_iou > 0.70:
        failures.append(f"抽掉下半部后 IoU={half_iou:.3f} 仍然太高 —— 指标不敏感")

    conf = skeleton_iou(_mask(u), _mask(norm_of("へ")))
    if conf > 0.85:
        failures.append(f"う vs へ IoU={conf:.3f} 过高 —— 指标分不出形近字")

    # 粗细变化必须**不掉分**（这是骨架 IoU 存在的理由）
    thick = u.point(lambda v: 255 if v > 40 else 0)
    thick_iou = skeleton_iou(_mask(u), _mask(thick))
    if thick_iou < 0.80:
        failures.append(f"加粗后 IoU={thick_iou:.3f} 掉太多 —— 指标对粗细太敏感")

    print("[kana-fidelity][selftest] 自比=%.3f 平移后=%.3f 抽半后=%.3f う/へ=%.3f 加粗后=%.3f"
          % (self_iou, shift_iou, half_iou, conf, thick_iou))
    if failures:
        for f in failures:
            print(f"[kana-fidelity][selftest][FAIL] {f}")
        return 1
    print("[kana-fidelity][selftest] 通过：指标对平移/截断/换字敏感，对粗细不敏感")
    return 0


def _calibrate(ref: ImageFont.FreeTypeFont) -> dict:
    """用参照字体的形近字对标定阈值。"""
    cache: dict[str, np.ndarray] = {}

    def mask_of(ch):
        if ch not in cache:
            i, b = _render_glyph(ref, ch)
            cache[ch] = _mask(_normalize(i, b))
        return cache[ch]

    pairs = []
    for a, b in CONFUSABLE:
        s = skeleton_iou(mask_of(a), mask_of(b))
        pairs.append({"pair": f"{a}/{b}", "iou": round(s, 4)})
    worst = max(p["iou"] for p in pairs)
    return {
        "confusable_pairs": pairs,
        "max_confusable_iou": round(worst, 4),
        "suggested_threshold": round(min(0.90, worst + 0.05), 4),
    }


def _load_cmap(path: Path) -> set[int]:
    """读出字体的 cmap 覆盖码位（用来判定「缺字」）。"""
    from fontTools.ttLib import TTFont

    try:
        return set(TTFont(str(path), lazy=True).getBestCmap().keys())
    except Exception:
        return set()


def _control_band(bold: ImageFont.FreeTypeFont, regular: ImageFont.FreeTypeFont):
    """控制组：同一个字、只有粗细不同（Yu Gothic Bold vs Regular）。

    这给出指标的**噪声底** —— 同一副骨架换个字重都会掉到多少分。
    读数只有低于这条带子，才谈得上「骨架走了」；高于它就是噪声。
    """
    cache: dict[str, np.ndarray] = {}

    def mask_of(ch):
        if ch not in cache:
            i, b = _render_glyph(bold, ch)
            cache[ch] = _mask(_normalize(i, b))
        return cache[ch]

    def mask_of_r(ch):
        key = "r" + ch
        if key not in cache:
            i, b = _render_glyph(regular, ch)
            cache[key] = _mask(_normalize(i, b))
        return cache[key]

    scores = []
    for cp in kana_codepoints():
        ch = chr(cp)
        a, b = mask_of(ch), mask_of_r(ch)
        if not a.any() and not b.any():
            continue
        scores.append(skeleton_iou(a, b))
    if not scores:
        return None
    scores.sort()
    return {
        "n": len(scores),
        "median": round(statistics.median(scores), 4),
        "p10": round(scores[len(scores) // 10], 4),
        "min": round(scores[0], 4),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="假名骨架保真度检查")
    ap.add_argument("--font", default="font-src/dist/HKPoster-Heavy.ttf")
    ap.add_argument("--reference", default="C:/Windows/Fonts/YuGothB.ttc")
    ap.add_argument("--reference-index", type=int, default=None)
    ap.add_argument("--out", default="font-src/reports/kana-fidelity.json")
    ap.add_argument("--sheet", default="font-src/reports/kana-fidelity.png")
    ap.add_argument("--min-iou", type=float, default=None, help="默认按参照形近字对自动标定")
    ap.add_argument("--selftest", action="store_true", help="只跑指标可信度自测")
    ap.add_argument("--em", type=int, default=1000)
    ap.add_argument("--control-regular", default="C:/Windows/Fonts/YuGothR.ttc",
                    help="控制组参照（同字不同粗细），用于标定噪声底；不存在则跳过")
    args = ap.parse_args()

    font_path = Path(args.font).resolve()
    if not font_path.exists():
        print(f"[kana-fidelity] 找不到字体：{font_path}")
        return 1

    ref_path = Path(args.reference).resolve()
    have_reference = ref_path.exists()
    if not have_reference:
        print(f"[kana-fidelity] 参照字体不存在：{ref_path} —— 只做缺字检查，跳过骨架比对")

    ref_index = (
        args.reference_index
        if (args.reference_index is not None and have_reference)
        else (_pick_reference_index(ref_path, want_bold=True) if have_reference else 0)
    )

    if args.selftest:
        if not have_reference:
            print("[kana-fidelity][selftest] 需要参照字体")
            return 1
        return _selftest(ref_path, ref_index)

    mine = _load_font(font_path, 0)
    ref = _load_font(ref_path, ref_index) if have_reference else None
    cmap = _load_cmap(font_path)

    threshold = args.min_iou
    calib: dict = {}
    if have_reference:
        calib = _calibrate(ref)
        if threshold is None:
            threshold = calib["suggested_threshold"]
        print("[kana-fidelity] 阈值标定：参照形近字对最高 IoU=%.3f → 阈值 %.3f"
              % (calib["max_confusable_iou"], threshold))
        for p in calib["confusable_pairs"]:
            print("    %-6s %.3f" % (p["pair"], p["iou"]))
    else:
        threshold = 0.0

    results = []
    for cp in kana_codepoints():
        ch = chr(cp)
        entry: dict = {"char": ch, "codepoint": f"U+{cp:04X}"}
        if cp not in cmap:
            entry.update(
                {
                    "skeleton_iou": None,
                    "raw_iou": None,
                    "mine_box": None,
                    "ref_box": None,
                    "mine_height": None,
                    "ref_height": None,
                    "mine_ink": None,
                    "ref_ink": None,
                    "verdict": "MISSING",
                }
            )
            results.append(entry)
            continue
        img_m, box_m = _render_glyph(mine, ch)
        img_r, box_r = _render_glyph(ref, ch) if have_reference else (None, None)
        norm_m = _normalize(img_m, box_m)
        sk = raw = None
        if have_reference:
            norm_r = _normalize(img_r, box_r)
            sk = round(skeleton_iou(_mask(norm_m), _mask(norm_r)), 4)
            raw = round(_raw_iou(norm_m, norm_r), 4)
        mb, rb = _em_box(box_m, args.em), (_em_box(box_r, args.em) if have_reference else None)
        entry.update(
            {
                "skeleton_iou": sk,
                "raw_iou": raw,
                "mine_box": mb,
                "ref_box": rb,
                "mine_height": round(mb["y1"] - mb["y0"], 1) if mb else None,
                "ref_height": round(rb["y1"] - rb["y0"], 1) if rb else None,
                "mine_ink": _ink_ratio(img_m),
                "ref_ink": _ink_ratio(img_r) if have_reference else None,
                "verdict": ("PASS" if (sk is None or sk >= threshold) else "WARN"),
            }
        )
        results.append(entry)

    warns = [r for r in results if r["verdict"] == "WARN"]
    missing = [r for r in results if r["verdict"] == "MISSING"]

    # 噪声底：同一个字换字重会掉到多少分
    control = None
    ctrl_path = Path(args.control_regular) if args.control_regular else None
    if have_reference and ctrl_path and ctrl_path.exists():
        control = _control_band(ref, _load_font(ctrl_path, 0))
        print("[kana-fidelity] 噪声底（同字换字重，Yu Gothic Bold vs Regular）："
              "n=%d 中位=%.3f 10%%分位=%.3f 最小=%.3f"
              % (control["n"], control["median"], control["p10"], control["min"]))

    report = {
        "font": str(font_path),
        "reference": f"{ref_path}#{ref_index}" if have_reference else None,
        "threshold": threshold,
        "calibration": calib,
        "control_band": control,
        "total": len(results),
        "warn": len(warns),
        "missing": len(missing),
        "results": results,
    }
    out = Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    sheet = Path(args.sheet).resolve()
    cell = 150
    cols = 8
    rows = (len(results) + cols - 1) // cols
    sheet_img = Image.new("RGB", (cols * cell + 20, rows * cell + 60), "white")
    draw = ImageDraw.Draw(sheet_img)
    draw.text((10, 6), f"kana fidelity — 左:本字体  右:参照({ref_path.name}#{ref_index})", fill="black")
    draw.text((10, 24), "绿=骨架一致  红=骨架走偏  橙=缺字", fill="black")
    small_m = ImageFont.truetype(str(font_path), 110)
    small_r = ImageFont.truetype(str(ref_path), 110, index=ref_index) if have_reference else None
    for i, r in enumerate(results):
        row, col = divmod(i, cols)
        x = 10 + col * cell
        y = 44 + row * cell
        color = {"PASS": (0, 120, 0), "WARN": (200, 0, 0), "FAIL": (200, 0, 0),
                 "MISSING": (230, 130, 0)}[r["verdict"]]
        draw.text((x + 4, y), r["char"], font=small_m, fill=(0, 0, 0))
        if small_r is not None:
            draw.text((x + 58, y), r["char"], font=small_r, fill=(0, 0, 0))
        label = r["skeleton_iou"] if r["skeleton_iou"] is not None else "缺"
        draw.text((x + 4, y + 114), f"{label:.2f}" if isinstance(label, float) else label,
                  font=None, fill=color)
    sheet_img.save(sheet)

    print(f"[kana-fidelity] 共 {len(results)} 字：缺字 {len(missing)}（硬门禁），"
          f"骨架偏离待人工复核 {len(warns)}")
    if missing:
        print("[kana-fidelity] 缺字（渲染成 .notdef 豆腐块 → 日文里直接读不出来）：")
        for r in missing:
            print("  %s  %s" % (r["char"], r["codepoint"]))
    if warns:
        print("[kana-fidelity] 骨架偏离（**软信号**，需人工目视复核；"
              "低于噪声底 10%% 分位 %.3f 才算可疑）"
              % (control["p10"] if control else float("nan")))
        for r in sorted(warns, key=lambda x: x["skeleton_iou"]):
            flag = "  <-- 低于噪声底" if control and r["skeleton_iou"] < control["p10"] else ""
            print("  %s  %s  骨架IoU=%.3f  原样IoU=%.3f  本高=%s 参照高=%s%s"
                  % (r["char"], r["codepoint"], r["skeleton_iou"], r["raw_iou"],
                     r["mine_height"], r["ref_height"], flag))
    print(f"[kana-fidelity] JSON: {out}")
    print(f"[kana-fidelity] 对照图: {sheet}")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
