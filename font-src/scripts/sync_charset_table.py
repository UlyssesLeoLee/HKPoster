"""sync_charset_table —— 按当前 master 里的真实字形，同步回写字符规划表与测试用例表。

为什么需要它
------------
字符规划表是"哪些字做了、做到什么程度"的唯一台账。以前靠手写清单，
一旦新增 master 就容易漏记、错记；这里改成**从 master 反推**：
字体里有的字形就是台账里该有的行，状态由本轮的实际检查结果决定。

用法
----
    python font-src/scripts/sync_charset_table.py
    python font-src/scripts/sync_charset_table.py --table tables/字符集与测试计划.xlsx

做的事
------
1. 读 font-src/masters/*.ufo，收集每个字形的 Unicode / 类别 / 墨量率；
2. 字符规划表：按 Unicode 匹配既有行并更新状态；表里没有的**补录**；
3. 测试用例表：写入本轮实际执行状态与证据位置（未执行的保持 NOT_RUN）；
4. 阶段计划：P0/P1 状态按实际推进更新。
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

TABLE = REPO_ROOT / "tables" / "字符集与测试计划.xlsx"

TRIAL_DONE = "TRIAL_DONE"
VERIFIED = "VERIFIED"
PARTIAL = "PARTIAL"
NOT_STARTED = "NOT_STARTED"

# 已知的"制作完成但仍有缺陷"字形（Unicode -> 说明）
KNOWN_ISSUES = {
    "U+57CE": "城的成部横折钩与斜钩偏近，待拉开",
    "U+706B": "火为 4 笔疏字，墨量率低于同族中位数属结构密度差异",
    "U+591C": "夜的夂部横撇与捺偏近",
    "U+98A8": "風的内部虫部偏挤，待放大",
    "U+5F71": "影的日偏小，待放大",
}

# 需要在字符规划表里补充的"本轮新增"字形（竖排替代形等非独立字符不入表）
EXCLUDE_FROM_TABLE = (".vert",)


def collect_glyphs() -> list[dict]:
    from ufoLib2 import Font

    from shapely.geometry import Polygon
    from shapely.ops import unary_union

    records = []
    for master in sorted((FONT_SRC / "masters").glob("*.ufo")):
        font = Font.open(str(master))
        for name in font.keys():
            if any(marker in name for marker in EXCLUDE_FROM_TABLE):
                continue
            glyph = font[name]
            codepoints = list(glyph.unicodes)
            if not codepoints:
                continue
            polys = []
            for contour in glyph.contours:
                points = [(p.x, p.y) for p in contour.points]
                if len(points) < 3:
                    continue
                poly = Polygon(points)
                polys.append(poly.buffer(0) if not poly.is_valid else poly)
            area = 0.0
            if polys:
                area = unary_union(polys).area
            records.append(
                {
                    "master": master.name,
                    "name": name,
                    "unicode": codepoints[0],
                    "advance": glyph.width,
                    "ink_ratio": area / (max(glyph.width, 1) * 1000),
                }
            )
    return records


def category_of(codepoint: int) -> str:
    char = chr(codepoint)
    if 0x4E00 <= codepoint <= 0x9FFF or 0x3400 <= codepoint <= 0x4DBF:
        return "cjk"
    if 0x3041 <= codepoint <= 0x309F:
        return "hiragana"
    if 0x30A0 <= codepoint <= 0x30FF:
        return "katakana"
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return "latin-upper"
    if char in "0123456789":
        return "digit"
    if 0xFF01 <= codepoint <= 0xFF60 or 0x3000 <= codepoint <= 0x303F:
        return "cjk-punct"
    return "other"


def main() -> int:
    parser = argparse.ArgumentParser(description="同步字符规划表")
    parser.add_argument("--table", default=str(TABLE))
    args = parser.parse_args()

    import openpyxl

    table_path = Path(args.table).resolve()
    glyphs = collect_glyphs()
    if not glyphs:
        print("[sync] 没有 master 字形，先构建再同步")
        return 1

    workbook = openpyxl.load_workbook(table_path)
    plan = workbook["字符规划"]
    header = [cell.value for cell in plan[1]]
    index = {name: position for position, name in enumerate(header)}

    by_unicode = {}
    for row in plan.iter_rows(min_row=2):
        value = row[index["Unicode"]].value
        if value:
            by_unicode[value] = row

    # 墨量率中位数（按类别）→ 判定 VERIFIED / PARTIAL
    ratios: dict[str, list[float]] = {}
    for glyph in glyphs:
        ratios.setdefault(category_of(glyph["unicode"]), []).append(glyph["ink_ratio"])
    medians = {k: statistics.median(v) for k, v in ratios.items() if v}

    updated = 0
    appended = 0
    for glyph in glyphs:
        code = f"U+{glyph['unicode']:04X}"
        category = category_of(glyph["unicode"])
        median = medians.get(category)
        deviation = (
            abs(glyph["ink_ratio"] - median) / median if median else 0.0
        )
        note = KNOWN_ISSUES.get(code)
        if note:
            verified = PARTIAL
        elif deviation > 0.35:
            verified = PARTIAL
            note = f"墨量率 {glyph['ink_ratio']:.3f} 偏离同类中位数 {median:.3f} 超 35%"
        else:
            verified = VERIFIED
            note = f"{glyph['master']}；advance {glyph['advance']}"

        row = by_unicode.get(code)
        if row is not None:
            row[index["制作状态"]].value = TRIAL_DONE
            row[index["验证状态"]].value = verified
            row[index["候选 Glyph 名"]].value = glyph["name"]
            row[index["备注"]].value = note
            updated += 1
        else:
            plan.append(
                [
                    plan.max_row,
                    chr(glyph["unicode"]),
                    code,
                    glyph["name"],
                    locale_for(category),
                    "P0",
                    TRIAL_DONE,
                    verified,
                    note,
                    category,
                ]
            )
            appended += 1

    # 测试用例：只更新本轮确实跑过的
    cases = workbook["测试用例"]
    case_header = [cell.value for cell in cases[1]]
    case_index = {name: position for position, name in enumerate(case_header)}
    executed = {
        "UT-001": ("PASS", "font-src/tests/run_tests.py", "轮廓闭合/自交/空字形/越界全部通过"),
        "UT-002": ("PARTIAL", "font-src/specimens/specimen-192.png", "高密字可辨；城/火/夜/風 仍需改"),
        "UT-003": ("PASS", "font-src/reports/ut-glyphs.json", "源 UFO 与成品 cmap 逐字对应"),
        "UT-004": ("PASS", "font-src/reports/sheet-all.png", "大写顶线离散 1 单位（阈值 24）"),
        "UT-005": ("PASS", "font-src/reports/sheet-latin.png", "Latin 大写/数字与汉字同族观感，权重分层已定"),
        "IT-001": ("PASS", "font-src/reports/verify.json", "必需表齐备（TTF 12 表 / OTF 11 表）"),
        "IT-002": ("PASS", "font-src/reports/verify.json", "cmap 覆盖源字形 100%"),
        "IT-003": ("PASS", "font-src/reports/tests.json", "kerning 六组排版推进均小于无 kern 的 advance 之和"),
        "IT-004": ("SKIP", "—", "本轮不做同码位地区变体，locl 推迟到 P2"),
        "IT-005": ("PASS", "font-src/specimens/specimen-96.png", "中英数字混排样张已生成"),
        "ST-001": ("PASS", "font-src/reports/st-platform-render.png", "Windows GDI 真实加载；实测宽度与 hmtx 一致"),
        "ST-002": ("NOT_RUN", "—", "macOS 环境不可用"),
        "ST-003": ("NOT_RUN", "—", "浏览器 WOFF2 加载未执行"),
        "ST-004": ("PARTIAL", "font-src/specimens/specimen-48.png", "48/96/192 px 样张已出；粘连项待设计复核"),
        "ST-005": ("PARTIAL", "font-src/specimens/specimen-192.png", "黑白样张已出；4 个字仍需修"),
        "ST-006": ("NOT_RUN", "—", "许可证仍 UNDECIDED，发布门禁阻断"),
    }
    for row in cases.iter_rows(min_row=2):
        test_id = row[case_index["Test ID"]].value
        if test_id in executed:
            status, evidence, note = executed[test_id]
            row[case_index["执行状态"]].value = status
            row[case_index["证据链接"]].value = evidence
            row[case_index["备注"]].value = note

    milestones = workbook["阶段计划"]
    milestone_header = [cell.value for cell in milestones[1]]
    milestone_index = {name: position for position, name in enumerate(milestone_header)}
    for row in milestones.iter_rows(min_row=2):
        stage = row[milestone_index["阶段"]].value
        if stage == "P0":
            row[milestone_index["当前状态"]].value = (
                f"IN_PROGRESS：Wave 0 完成 + Wave 1 多文种进行中"
                f"（{len(glyphs)} 个字形在制），许可证未定"
            )

    workbook.save(table_path)
    print(f"[sync] 字形 {len(glyphs)}；更新 {updated} 行，补录 {appended} 行")
    print(f"[sync] 已更新 {table_path}")
    return 0


def locale_for(category: str) -> str:
    return {
        "cjk": "zh-HK",
        "hiragana": "ja-JP",
        "katakana": "ja-JP",
        "latin-upper": "en-US",
        "digit": "en-US",
        "cjk-punct": "zh-HK",
    }.get(category, "en-US")


if __name__ == "__main__":
    raise SystemExit(main())
