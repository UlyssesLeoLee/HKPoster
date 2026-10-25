"""字形级 UT —— 直接读 UFO master，断言度量、几何与家族一致性。

被 run_tests.py 调用；也可单独运行：
    python font-src/tests/test_glyph_metrics.py
"""

from __future__ import annotations

import statistics
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
FONT_SRC = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

UPM = 1000
CJK_ADVANCE = 1000
LATIN_ADVANCE = 640
DIGIT_ADVANCE = 640
CAP_TOP = 700
CAP_TOLERANCE = 8
BOX_TOLERANCE = 120

LATIN_UPPER = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = set("0123456789")


def category_of(codepoint):
    if codepoint is None:
        return "other"
    if 0x4E00 <= codepoint <= 0x9FFF or 0x3400 <= codepoint <= 0x4DBF:
        return "cjk"
    char = chr(codepoint)
    if char in LATIN_UPPER:
        return "latin-upper"
    if char in DIGITS:
        return "digit"
    return "other"


def run(context) -> list[dict]:
    """context: {"sources": [Path], "font": Path}"""
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    from ufoLib2 import Font

    results: list[dict] = []
    records: list[dict] = []

    for source in context["sources"]:
        font = Font.open(str(source))
        for name in font.keys():
            glyph = font[name]
            codepoint = glyph.unicodes[0] if glyph.unicodes else None
            polys = []
            for contour in glyph.contours:
                points = [(p.x, p.y) for p in contour.points]
                if len(points) < 3:
                    results.append(
                        {
                            "name": f"{name}: 轮廓点数不足",
                            "status": "FAIL",
                            "detail": f"{len(points)} 个点",
                        }
                    )
                    continue
                poly = Polygon(points)
                if not poly.is_valid:
                    results.append(
                        {
                            "name": f"{name}: 轮廓自交",
                            "status": "FAIL",
                            "detail": "shapely Polygon.is_valid = False",
                        }
                    )
                polys.append(poly.buffer(0) if not poly.is_valid else poly)

            if not polys:
                results.append(
                    {"name": f"{name}: 空字形", "status": "FAIL", "detail": "无有效轮廓"}
                )
                continue

            merged = unary_union(polys)
            minx, miny, maxx, maxy = merged.bounds
            records.append(
                {
                    "name": name,
                    "category": category_of(codepoint),
                    "advance": glyph.width,
                    "ink_ratio": merged.area / (max(glyph.width, 1) * UPM),
                    "bbox": (minx, miny, maxx, maxy),
                }
            )

            if minx < -BOX_TOLERANCE or maxx > UPM + BOX_TOLERANCE:
                results.append(
                    {
                        "name": f"{name}: 横向越界",
                        "status": "FAIL",
                        "detail": f"bbox x=[{minx:.0f},{maxx:.0f}]",
                    }
                )
            if maxy > 880 + BOX_TOLERANCE or miny < -120 - BOX_TOLERANCE:
                results.append(
                    {
                        "name": f"{name}: 纵向越界",
                        "status": "FAIL",
                        "detail": f"bbox y=[{miny:.0f},{maxy:.0f}]",
                    }
                )

    by_name = {record["name"]: record for record in records}
    for record in records:
        category = record["category"]
        if category == "cjk" and record["advance"] != CJK_ADVANCE:
            results.append(
                {
                    "name": f"{record['name']}: CJK advance",
                    "status": "FAIL",
                    "detail": f"{record['advance']} != {CJK_ADVANCE}",
                }
            )
        if category == "latin-upper":
            if record["advance"] != LATIN_ADVANCE:
                results.append(
                    {
                        "name": f"{record['name']}: 大写 advance",
                        "status": "FAIL",
                        "detail": f"{record['advance']} != {LATIN_ADVANCE}",
                    }
                )
            top = record["bbox"][3]
            if abs(top - CAP_TOP) > CAP_TOLERANCE:
                results.append(
                    {
                        "name": f"{record['name']}: 大写顶线",
                        "status": "FAIL",
                        "detail": f"顶线 {top:.0f}，偏离 {CAP_TOP} 超 {CAP_TOLERANCE} 单位",
                    }
                )
        if category == "digit" and record["advance"] != DIGIT_ADVANCE:
            results.append(
                {
                    "name": f"{record['name']}: 数字 advance",
                    "status": "FAIL",
                    "detail": f"{record['advance']} != {DIGIT_ADVANCE}",
                }
            )

    # 密度离群：记 WARN，不影响退出码（不同结构的字符密度本就不同）
    for category in ("cjk", "latin-upper", "digit"):
        ratios = [r["ink_ratio"] for r in records if r["category"] == category]
        if len(ratios) < 3:
            continue
        median = statistics.median(ratios)
        for record in records:
            if record["category"] != category:
                continue
            if median and record["ink_ratio"] / median > 2.2:
                results.append(
                    {
                        "name": f"{record['name']}: 密度离群",
                        "status": "WARN",
                        "detail": (
                            f"墨量率 {record['ink_ratio']:.3f}，同类中位数 {median:.3f}，"
                            "比例 > 2.2（结构密度差异，需人工判断是否风格漂移）"
                        ),
                    }
                )

    if not results:
        results.append(
            {
                "name": "字形度量与几何",
                "status": "PASS",
                "detail": f"{len(records)} 个字形全部通过",
            }
        )
    return results


if __name__ == "__main__":
    from ufoLib2 import Font  # noqa: F401

    sources = sorted((FONT_SRC / "masters").glob("*.ufo"))
    outcomes = run({"sources": sources, "font": None})
    for item in outcomes:
        print(f"  {item['status']:<4} {item['name']}: {item['detail']}")
    raise SystemExit(1 if any(i["status"] == "FAIL" for i in outcomes) else 0)
