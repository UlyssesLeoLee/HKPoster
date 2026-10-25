"""成品字体 IT —— 表结构、name/OS-2 度量、cmap 覆盖、真实排版。

被 run_tests.py 调用；也可单独运行：
    python font-src/tests/test_opentype.py --font font-src/dist/HKPoster-Heavy.ttf
"""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
FONT_SRC = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

TTF_REQUIRED = {"head", "hhea", "hmtx", "maxp", "cmap", "name", "OS/2", "post", "glyf", "loca"}
OTF_REQUIRED = {"head", "hhea", "hmtx", "maxp", "cmap", "name", "OS/2", "post", "CFF "}

EXPECTED_NAME = {
    # RIBBI 兼容名：styleName "Heavy" 不是 RIBBI 样式名，fontTools 会把
    # family 拼成 "HK Poster Heavy"、subfamily 退化为 "Regular"，
    # 真实的族名/样式名放在排版名 nameID 16/17。
    1: "HK Poster Heavy",
    2: "Regular",
    4: "HK Poster Heavy",
    5: "Version 1.000",
    6: "HKPoster-Heavy",
    16: "HK Poster",
    17: "Heavy",
}

SAMPLE_STRINGS = ["HK Poster Heavy", "CITY OF SHADOWS", "1997", "AV", "TA", "LY"]


def run(context) -> list[dict]:
    from fontTools.ttLib import TTFont

    results: list[dict] = []
    font_path = Path(context["font"])
    font = TTFont(str(font_path))

    present = set(font.keys())
    required = TTF_REQUIRED if "glyf" in present else OTF_REQUIRED
    missing = sorted(required - present)
    results.append(
        {
            "name": "必需表齐备",
            "status": "FAIL" if missing else "PASS",
            "detail": f"缺 {missing}" if missing else f"{len(present)} 张表齐备",
        }
    )

    name_table = font["name"]
    for name_id, expected in EXPECTED_NAME.items():
        actual = name_table.getDebugName(name_id)
        results.append(
            {
                "name": f"name 表 id={name_id}",
                "status": "PASS" if actual == expected else "FAIL",
                "detail": f"实际 {actual!r}，期望 {expected!r}",
            }
        )

    os2 = font["OS/2"]
    head = font["head"]
    hhea = font["hhea"]
    for label, actual, expected in (
        ("OS/2 usWeightClass", os2.usWeightClass, 900),
        ("head unitsPerEm", head.unitsPerEm, 1000),
        ("hhea ascender", hhea.ascender, 880),
        ("hhea descender", hhea.descender, -120),
    ):
        results.append(
            {
                "name": label,
                "status": "PASS" if actual == expected else "FAIL",
                "detail": f"实际 {actual}，期望 {expected}",
            }
        )

    # cmap 覆盖：源 UFO 的每个 Unicode 都要能查到
    cmap = font.getBestCmap() or {}
    from ufoLib2 import Font as UfoFont

    missing_unicode = []
    for source in context["sources"]:
        ufo = UfoFont.open(str(source))
        for glyph_name in ufo.keys():
            for codepoint in ufo[glyph_name].unicodes:
                if codepoint not in cmap:
                    missing_unicode.append(f"U+{codepoint:04X}({glyph_name})")
    results.append(
        {
            "name": "cmap 覆盖源字形",
            "status": "FAIL" if missing_unicode else "PASS",
            "detail": (
                f"缺 {missing_unicode}"
                if missing_unicode
                else f"{len(cmap)} 项映射，源字形全部覆盖"
            ),
        }
    )

    # 真实排版：不得出现 .notdef
    import uharfbuzz as hb

    blob = hb.Blob.from_file_path(str(font_path))
    face = hb.Face(blob)
    hb_font = hb.Font(face)
    notdef = 0
    for text in SAMPLE_STRINGS:
        if not all(ord(ch) in cmap for ch in text):
            results.append(
                {
                    "name": f"排版 {text!r}",
                    "status": "SKIP",
                    "detail": "字体尚不含该字符串用到的字符",
                }
            )
            continue
        buffer = hb.Buffer()
        buffer.add_str(text)
        buffer.guess_segment_properties()
        hb.shape(hb_font, buffer)
        used = [info.codepoint for info in buffer.glyph_infos]
        if not used:
            results.append(
                {"name": f"排版 {text!r}", "status": "FAIL", "detail": "排版结果为空"}
            )
        elif any(gid == notdef for gid in used):
            results.append(
                {
                    "name": f"排版 {text!r}",
                    "status": "FAIL",
                    "detail": "出现 .notdef 兜底字形",
                }
            )
        else:
            advances = sum(pos.x_advance for pos in buffer.glyph_positions)
            results.append(
                {
                    "name": f"排版 {text!r}",
                    "status": "PASS",
                    "detail": f"{len(used)} 个字形，总推进 {advances}",
                }
            )

    # kerning 是否真的生效：契约指定的六组关键组合
    if "GPOS" in font:
        hmtx = font["hmtx"]
        for pair in ("AV", "AW", "TA", "TO", "YA", "LT"):
            if not all(ord(ch) in cmap for ch in pair):
                continue
            names = [cmap[ord(ch)] for ch in pair]
            plain = hmtx[names[0]][0] + hmtx[names[1]][0]
            buffer = hb.Buffer()
            buffer.add_str(pair)
            buffer.guess_segment_properties()
            hb.shape(hb_font, buffer)
            shaped = sum(pos.x_advance for pos in buffer.glyph_positions)
            results.append(
                {
                    "name": f"kerning {pair}",
                    "status": "PASS" if shaped < plain else "FAIL",
                    "detail": f"排版推进 {shaped}，无 kern 时应为 {plain}",
                }
            )
    else:
        results.append(
            {
                "name": "kerning 生效",
                "status": "SKIP",
                "detail": "成品字体没有 GPOS 表（Latin kerning 尚未接入）",
            }
        )

    return results


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--font", default=str(FONT_SRC / "dist" / "HKPoster-Heavy.ttf"))
    args = parser.parse_args()
    sources = sorted((FONT_SRC / "masters").glob("*.ufo"))
    outcomes = run({"font": Path(args.font), "sources": sources})
    for item in outcomes:
        print(f"  {item['status']:<4} {item['name']}: {item['detail']}")
    raise SystemExit(1 if any(i["status"] == "FAIL" for i in outcomes) else 0)
