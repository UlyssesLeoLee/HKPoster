"""vert 特性 IT —— 日文竖排（縦書き）替代形态的独立测试。

可独立运行：
    python font-src/tests/test_vert.py
    python font-src/tests/test_vert.py --font font-src/dist/HKPoster-Heavy.ttf

断言
----
1. 成品字体的 GSUB 里有 `vert` 特性；
2. vert.fea 里列出的每一个替代字形都真实存在于成品字体（glyph 集），
   替换源字形也能通过 Unicode 排到；
3. 用 uharfbuzz 排版含这些标点的字符串并**开启** vert 特性，输出的字形名
   是 .vert 版本；
4. **关闭** vert 特性时，输出的仍是基础版本（证明替换由特性驱动，不是写死的）；
5. 同族一致性：.vert 形态与横排基础形态的墨量一致（旋转不改变墨形）。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
FONT_SRC = SCRIPT_DIR.parent
REPO_ROOT = FONT_SRC.parent

DEFAULT_FONT = FONT_SRC / "dist" / "HKPoster-Heavy.ttf"
FEA_PATH = FONT_SRC / "features" / "vert.fea"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def parse_vert_fea(path: Path = FEA_PATH) -> list[tuple[str, str]]:
    """从 vert.fea 里读出 (源字形, 替代字形) 替换对。"""
    text = path.read_text(encoding="utf-8")
    return [
        (m.group(1), m.group(2))
        for m in re.finditer(r"sub\s+([^\s;]+)\s+by\s+([^\s;]+)\s*;", text)
    ]


def build_cases(cmap: dict, pairs: list[tuple[str, str]]) -> list[tuple[str, str, str]]:
    """由 cmap 反查每个源字形的 Unicode，得到 [(字符, 源字形, 替代字形), ...]。"""
    reverse: dict[str, int] = {}
    for codepoint, name in cmap.items():
        reverse.setdefault(name, codepoint)
    cases = []
    for base, alt in pairs:
        codepoint = reverse.get(base)
        if codepoint is None:
            continue
        cases.append((chr(codepoint), base, alt))
    return cases


def shape(font_path: Path, text: str, features: dict | None = None) -> list[str]:
    """用 uharfbuzz 排版，返回字形名列表。"""
    import uharfbuzz as hb
    from fontTools.ttLib import TTFont

    blob = hb.Blob.from_file_path(str(font_path))
    face = hb.Face(blob)
    hb_font = hb.Font(face)

    buffer = hb.Buffer()
    buffer.add_str(text)
    buffer.guess_segment_properties()
    hb.shape(hb_font, buffer, features)

    order = TTFont(str(font_path)).getGlyphOrder()
    return [
        order[info.codepoint] if info.codepoint < len(order) else "?"
        for info in buffer.glyph_infos
    ]


class _RecordingPen:
    """最小轮廓记录笔：只关心闭合环。"""

    def __init__(self) -> None:
        self._rings: list[list[tuple[float, float]]] = []
        self._current: list[tuple[float, float]] | None = None

    def moveTo(self, pt) -> None:
        self._current = [(pt[0], pt[1])]

    def lineTo(self, pt) -> None:
        if self._current is not None:
            self._current.append((pt[0], pt[1]))

    def qCurveTo(self, *points) -> None:
        pts = [p for p in points if p is not None]
        if self._current is None:
            return
        if len(pts) == 1:
            self._current.append((pts[0][0], pts[0][1]))
        else:
            self._current.extend((p[0], p[1]) for p in pts)

    def curveTo(self, *points) -> None:
        if self._current is not None:
            self._current.extend((p[0], p[1]) for p in points)

    def closePath(self) -> None:
        if self._current and len(self._current) >= 3:
            self._rings.append(self._current)
        self._current = None

    def endPath(self) -> None:
        self._current = None

    def rings(self) -> list[list[tuple[float, float]]]:
        return self._rings


def glyph_ink_area(font, glyph_name: str) -> float:
    """成品字体里一个字形的墨量（平方单位）。"""
    from shapely.geometry import Polygon
    from shapely.ops import unary_union

    glyph_set = font.getGlyphSet()
    if glyph_name not in glyph_set:
        return 0.0

    polygons = []
    pen = _RecordingPen()
    glyph_set[glyph_name].draw(pen)
    for ring in pen.rings():
        points = [(p[0], p[1]) for p in ring]
        if len(points) < 3:
            continue
        polygon = Polygon(points)
        if not polygon.is_valid:
            polygon = polygon.buffer(0)
        if polygon.is_empty:
            continue
        polygons.append(polygon)
    if not polygons:
        return 0.0
    return float(unary_union(polygons).area)


def run(context: dict) -> list[dict]:
    """跑完整套断言，返回逐条结果（与 run_tests.py 的约定一致）。"""
    from fontTools.ttLib import TTFont

    font_path = Path(context.get("font", DEFAULT_FONT))
    results: list[dict] = []

    if not font_path.exists():
        return [
            {
                "name": "成品字体存在",
                "status": "FAIL",
                "detail": f"找不到 {font_path}（先跑 build_font.py）",
            }
        ]

    font = TTFont(str(font_path))
    glyph_order = font.getGlyphOrder()
    cmap = font.getBestCmap() or {}
    pairs = parse_vert_fea()

    # ---- 1. vert 特性存在 ----
    feature_tags: list[str] = []
    if "GSUB" in font:
        for record in font["GSUB"].table.FeatureList.FeatureRecord:
            feature_tags.append(record.FeatureTag)
    results.append(
        {
            "name": "GSUB 里有 vert 特性",
            "status": "PASS" if "vert" in feature_tags else "FAIL",
            "detail": f"特性标签 {sorted(set(feature_tags)) or '无'}",
        }
    )

    # ---- 2. vert.fea 的每个替代字形都存在 ----
    missing_alt = [alt for _, alt in pairs if alt not in glyph_order]
    missing_base = [base for base, _ in pairs if base not in glyph_order]
    results.append(
        {
            "name": "vert.fea 替代字形齐全",
            "status": "PASS" if not (missing_alt or missing_base) else "FAIL",
            "detail": (
                f"{len(pairs)} 组替换，替代形缺失 {missing_alt}，源字形缺失 {missing_base}"
                if (missing_alt or missing_base)
                else f"{len(pairs)} 组替换，源字形与替代形都在成品字体里"
            ),
        }
    )

    cases = build_cases(cmap, pairs)
    results.append(
        {
            "name": "vert.fea 源字形可由 Unicode 排到",
            "status": "PASS" if len(cases) == len(pairs) else "FAIL",
            "detail": (
                f"{len(cases)}/{len(pairs)} 个源字形在 cmap 里"
                + (
                    ""
                    if len(cases) == len(pairs)
                    else f"，缺 {[b for b, _ in pairs if b not in cmap.values()]}"
                )
            ),
        }
    )

    if not cases:
        results.append(
            {
                "name": "可排版的竖排标点串",
                "status": "FAIL",
                "detail": "没有一个替换源字形能由 Unicode 排到，后面的排版断言跳过",
            }
        )
        return results

    text = "".join(case[0] for case in cases)
    expected_on = [case[2] for case in cases]
    expected_off = [case[1] for case in cases]

    # ---- 3. 开启 vert → .vert 形态 ----
    shaped_on = shape(font_path, text, {"vert": True})
    wrong_on = [name for name in shaped_on if not name.endswith(".vert")]
    results.append(
        {
            "name": "开启 vert 排版得到 .vert 形态",
            "status": "PASS" if shaped_on and not wrong_on else "FAIL",
            "detail": (
                f"{len(shaped_on)} 个字形，非 .vert 的有 {wrong_on}"
                if wrong_on
                else f"{len(shaped_on)} 个字形全部是 .vert 形态"
            ),
        }
    )
    results.append(
        {
            "name": "开启 vert 的字形与 vert.fea 一致",
            "status": "PASS" if shaped_on == expected_on else "FAIL",
            "detail": (
                f"排版结果 {shaped_on}"
                if shaped_on != expected_on
                else f"逐字对上 vert.fea 的 {len(pairs)} 组替换"
            ),
        }
    )

    # ---- 4. 关闭 vert → 基础形态 ----
    shaped_off = shape(font_path, text, {"vert": False})
    wrong_off = [name for name in shaped_off if name.endswith(".vert")]
    results.append(
        {
            "name": "关闭 vert 排版得到基础形态",
            "status": "PASS" if shaped_off and not wrong_off else "FAIL",
            "detail": (
                f"仍出现 .vert 的有 {wrong_off}"
                if wrong_off
                else f"{len(shaped_off)} 个字形全部是基础形态"
            ),
        }
    )
    results.append(
        {
            "name": "关闭 vert 的字形与基础字形一致",
            "status": "PASS" if shaped_off == expected_off else "FAIL",
            "detail": (
                f"排版结果 {shaped_off}"
                if shaped_off != expected_off
                else f"逐字对上 vert.fea 的 {len(pairs)} 个源字形"
            ),
        }
    )

    # ---- 5. 同族一致性：竖排形态与横排形态墨量一致 ----
    area_rows = []
    for base, alt in pairs:
        base_area = glyph_ink_area(font, base)
        alt_area = glyph_ink_area(font, alt)
        if base_area <= 0 or alt_area <= 0:
            area_rows.append((base, alt, base_area, alt_area))
            continue
        if abs(alt_area - base_area) / base_area > 0.02:
            area_rows.append((base, alt, round(base_area, 1), round(alt_area, 1)))
    results.append(
        {
            "name": "竖排/横排墨量一致（同族）",
            "status": "PASS" if not area_rows else "FAIL",
            "detail": (
                f"墨量偏差 >2% 的有 {area_rows}"
                if area_rows
                else f"{len(pairs)} 组替代形的墨量与横排一致（±2%）"
            ),
        }
    )

    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="vert 特性（竖排替代形态）测试")
    parser.add_argument("--font", default=str(DEFAULT_FONT))
    args = parser.parse_args()
    outcomes = run({"font": Path(args.font)})
    failures = 0
    for item in outcomes:
        if item["status"] == "FAIL":
            failures += 1
        print(f"  {item['status']:<4} {item['name']}: {item['detail']}")
    print(f"[test_vert] {'PASS' if not failures else 'FAIL'}（FAIL {failures}）")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
