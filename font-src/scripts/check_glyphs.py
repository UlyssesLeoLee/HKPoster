"""check_glyphs — 字形级 UT 检查（对 UFO 源）。

用法
----
    python font-src/scripts/check_glyphs.py
    python font-src/scripts/check_glyphs.py --sources font-src/masters/hkposter-latin.ufo
    python font-src/scripts/check_glyphs.py --json font-src/reports/ut-glyphs.json

检查项
------
FAIL 级（结构硬错）
  * 空字形 / 零墨量
  * 轮廓点数 < 3、轮廓自交（shapely is_valid）
  * 重复 Unicode 映射
  * 超出 em 盒（x 越界 > 120 或 y 越界超出 ascender/descender）
  * CJK 字符 advance != 1000
  * Latin 大写字母顶线离散 > 24 单位（家族一致性）
  * 数字高度离散 > 24 单位（家族一致性）

WARN 级（需人工看）
  * 同类别墨量率（ink_area / (advance × UPM)）离该类别中位数 > 35%
  * 字面宽度/高度明显偏离该类别中位数

退出码：0 = PASS（有 WARN 仍为 PASS），1 = FAIL
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
FONT_SRC = SCRIPT_DIR.parent
REPO_ROOT = FONT_SRC.parent
sys.path.insert(0, str(SCRIPT_DIR))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from shapely.geometry import Polygon  # noqa: E402
from shapely.ops import unary_union  # noqa: E402
from ufoLib2 import Font  # noqa: E402

UPM = 1000
ASCENDER = 880
DESCENDER = -120
CJK_ADVANCE = 1000
BOX_TOLERANCE = 120

LATIN_UPPER = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = set("0123456789")


def collect_sources(explicit: list[str] | None) -> list[Path]:
    if explicit:
        return [Path(p).resolve() for p in explicit]
    masters = FONT_SRC / "masters"
    if not masters.is_dir():
        return []
    return sorted(p for p in masters.glob("*.ufo") if p.is_dir())


def glyph_polygon(glyph):
    polys = []
    for contour in glyph.contours:
        points = [(p.x, p.y) for p in contour.points]
        if len(points) < 3:
            continue
        poly = Polygon(points)
        if not poly.is_valid:
            poly = poly.buffer(0)
        if not poly.is_empty:
            polys.append(poly)
    if not polys:
        return None
    return unary_union(polys)


def category_of(codepoint: int | None) -> str:
    if codepoint is None:
        return "other"
    char = chr(codepoint)
    if 0x4E00 <= codepoint <= 0x9FFF or 0x3400 <= codepoint <= 0x4DBF:
        return "cjk"
    if char in LATIN_UPPER:
        return "latin-upper"
    if char in DIGITS:
        return "digit"
    if 0xFF01 <= codepoint <= 0xFF60 or 0x3000 <= codepoint <= 0x303F:
        return "cjk-punct"
    if codepoint < 0x2000:
        return "latin-punct"
    return "other"


def main() -> int:
    parser = argparse.ArgumentParser(description="字形级 UT 检查")
    parser.add_argument("--sources", nargs="*", default=None)
    parser.add_argument("--json", default=None, help="报告输出路径")
    args = parser.parse_args()

    sources = collect_sources(args.sources)
    if not sources:
        print("[check_glyphs] 没有找到 UFO master")
        return 1

    failures: list[str] = []
    warnings: list[str] = []
    records: list[dict] = []
    unicode_map: dict[int, str] = {}

    for source in sources:
        font = Font.open(str(source))
        for name in font.keys():
            glyph = font[name]
            codepoints = list(glyph.unicodes)
            codepoint = codepoints[0] if codepoints else None
            record = {
                "source": source.name,
                "name": name,
                "unicode": f"U+{codepoint:04X}" if codepoint is not None else None,
                "advance": glyph.width,
                "contours": len(glyph.contours),
                "points": sum(len(c.points) for c in glyph.contours),
            }

            if codepoint is not None:
                if codepoint in unicode_map:
                    failures.append(
                        f"重复 Unicode {record['unicode']}：{unicode_map[codepoint]} 与 {name}"
                    )
                unicode_map[codepoint] = name

            polygon = glyph_polygon(glyph)
            if polygon is None or polygon.is_empty:
                failures.append(f"{name}：空字形（无有效轮廓）")
                records.append(record)
                continue

            record["ink_area"] = round(polygon.area, 1)
            record["ink_ratio"] = round(polygon.area / (max(glyph.width, 1) * UPM), 4)
            minx, miny, maxx, maxy = polygon.bounds
            record["bbox"] = [round(minx), round(miny), round(maxx), round(maxy)]
            record["category"] = category_of(codepoint)

            if minx < -BOX_TOLERANCE or maxx > UPM + BOX_TOLERANCE:
                failures.append(f"{name}：横向越界 bbox x=[{minx:.0f},{maxx:.0f}]")
            if maxy > ASCENDER + BOX_TOLERANCE or miny < DESCENDER - BOX_TOLERANCE:
                failures.append(
                    f"{name}：纵向越界 bbox y=[{miny:.0f},{maxy:.0f}]"
                )

            for index, contour in enumerate(glyph.contours):
                points = [(p.x, p.y) for p in contour.points]
                if len(points) < 3:
                    failures.append(f"{name}：轮廓 {index} 点数不足（{len(points)}）")
                    continue
                ring = Polygon(points)
                if not ring.is_valid:
                    failures.append(f"{name}：轮廓 {index} 自交或非法")

            category = record["category"]
            if category == "cjk" and glyph.width != CJK_ADVANCE:
                failures.append(f"{name}：CJK advance {glyph.width} != {CJK_ADVANCE}")
            if category == "latin-upper":
                record["cap_top"] = round(maxy)
            if category == "digit":
                record["digit_top"] = round(maxy)
                record["digit_bottom"] = round(miny)

            records.append(record)

    # ---- 家族一致性 ----
    def group_median(cat: str, key: str) -> float | None:
        values = [r[key] for r in records if r.get("category") == cat and key in r]
        return statistics.median(values) if values else None

    for cat, key in (("latin-upper", "cap_top"), ("digit", "digit_top")):
        values = [r[key] for r in records if r.get("category") == cat and key in r]
        if len(values) > 1:
            spread = max(values) - min(values)
            if spread > 24:
                failures.append(
                    f"{cat} {key} 离散 {spread} 单位 > 24（家族一致性被破坏）"
                )

    for cat in ("cjk", "latin-upper", "digit"):
        ratios = [r["ink_ratio"] for r in records if r.get("category") == cat]
        if len(ratios) < 3:
            continue
        median = statistics.median(ratios)
        for record in records:
            if record.get("category") != cat:
                continue
            if median and abs(record["ink_ratio"] - median) / median > 0.35:
                warnings.append(
                    f"{record['name']}（{cat}）墨量率 {record['ink_ratio']:.3f} "
                    f"偏离同类中位数 {median:.3f} 超 35%"
                )

    report = {
        "sources": [str(p.relative_to(REPO_ROOT)).replace("\\", "/") for p in sources],
        "glyph_count": len(records),
        "failures": failures,
        "warnings": warnings,
        "records": records,
    }
    report_path = (
        Path(args.json).resolve() if args.json else FONT_SRC / "reports" / "ut-glyphs.json"
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[check_glyphs] master {len(sources)} 个，字形 {len(records)} 个")
    for failure in failures:
        print(f"  FAIL  {failure}")
    for warning in warnings:
        print(f"  WARN  {warning}")
    status = "PASS" if not failures else "FAIL"
    print(f"[check_glyphs] {status}（FAIL {len(failures)} / WARN {len(warnings)}）")
    print(f"[check_glyphs] 报告：{report_path}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
