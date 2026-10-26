#!/usr/bin/env python3
"""码位独立核对 —— 用**参照字体**当第三方证据源。

为什么需要它
------------
`check_charset.py` 比对的是「glyph 的 note 汉字」与「glyph 的 unicode」，
两者来自**同一条记录**，一起错就查不出来。

2026-10-26 的「栄」事故正是如此：`joyo-kanji-meta.json` 里「栄」那一行
被以「**荨**」(U+8368) 为键写入，unicode 字段也跟着写 U+8368 —— 字段自洽检查
零不符。但 Unicode 权威表里 **U+6804 = 栄**、**U+8368 = 荨**，
也就是说成品字体**缺了「栄」**、却把「荨」挂在了别人的码位上。

上一轮的修复把 note 改成「荨」让自洽检查通过 —— 把**意图**改成了跟机器字段对齐，
于是门禁再也看不出问题。

本工具用**独立来源**抓这一类错误：

1. **参照字体必须没有这个码位**：所有 Jōyō 常用漢字都存在于开源日语字体里；
   反过来，一个**日语字体里根本不存在**的码位，几乎一定是选错了字。
   （U+8368「荨」是中文专用字，8 个参照字体里一个都没有 → 直接报警。）
2. **`chr(unicode)` 必须等于字表里的键**：键与码位必须指向同一个字。

用法
----
    python font-src/scripts/check_codepoint_ref.py
    python font-src/scripts/check_codepoint_ref.py --selftest   # 先自证分辨力
"""
from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="backslashreplace")

FONT_SRC = Path(__file__).resolve().parents[1]
REPO = FONT_SRC.parent
META = FONT_SRC / "data" / "joyo-kanji-meta.json"

# 只用免费商用、开源、无任何限制的参照字体（SIL OFL 1.1）
REF_DIR = Path(r"E:/hkposter-refs")
REF_GLOBS = ("MPLUS1p-Black.ttf", "ZenKakuGothicNew-Black.ttf", "ZenMaruGothic-Black.ttf",
             "MPLUSRounded1c-Black.ttf", "KleeOne-SemiBold.ttf", "YuseiMagic-Regular.ttf",
             "KaiseiDecol-Regular.ttf", "KiwiMaru-Regular.ttf")


def ref_cmaps():
    """-> {文件名: set(码位)}"""
    out = {}
    for name in REF_GLOBS:
        p = REF_DIR / name
        if not p.exists():
            continue
        try:
            from fontTools.ttLib import TTFont
            f = TTFont(p, lazy=True)
            out[name] = set(f.getBestCmap().keys())
            f.close()
        except Exception as e:  # pragma: no cover
            print("[codepoint-ref] 参照字体读不了 %s：%s" % (name, e))
    return out


def check(chars, union, n_ref):
    """-> [问题描述]"""
    problems = []
    for key, rec in chars.items():
        uv = str(rec.get("unicode") or "")
        try:
            cp = int(uv.replace("U+", ""), 16)
        except ValueError:
            problems.append("字表「%s」的 unicode 字段不可解析：%r" % (key, uv))
            continue
        # 1) 键 ↔ 码位必须指向同一个字
        if chr(cp) != key:
            problems.append("字表「%s」的码位 %s 实际是「%s」—— 键与码位指向不同的字"
                            % (key, uv, chr(cp)))
            continue
        # 2) 独立证据源：这个码位必须在某个参照字体里存在
        if cp not in union:
            problems.append("「%s」(U+%04X) 在 %d 个参照字体里**都不存在** —— "
                            "极可能选错了字（参照覆盖全部 Jōyō 常用漢字）"
                            % (key, cp, n_ref))
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta", default=str(META))
    ap.add_argument("--font", default=None,
                    help="改为检查这个字体文件里的每个码位（lane 用子集构建的产物）")
    ap.add_argument("--selftest", action="store_true",
                    help="自证分辨力：注入一条已知错配（荨→U+8368），必须被抓到")
    args = ap.parse_args()

    cms = ref_cmaps()
    if not cms:
        print("[codepoint-ref] 找不到参照字体（%s）" % REF_DIR)
        return 2
    union = set()
    for s in cms.values():
        union |= s
    print("[codepoint-ref] 参照字体 %d 个，码位并集 %d 个" % (len(cms), len(union)))

    if args.font:
        # lane 模式：检查成品字体里的每个码位是否在参照字体里存在
        from fontTools.ttLib import TTFont
        f = TTFont(args.font, lazy=True)
        cps = sorted(f.getBestCmap().keys())
        f.close()
        cjk = [cp for cp in cps if 0x3400 <= cp <= 0x9FFF]
        missing = [cp for cp in cjk if cp not in union]
        print("[codepoint-ref] 字体 %s：CJK 码位 %d 个" % (Path(args.font).name, len(cjk)))
        if missing:
            print("[codepoint-ref] %d 个码位在参照字体里**都不存在** —— 极可能选错了字：" % len(missing))
            for cp in missing[:40]:
                print("    U+%04X %s" % (cp, chr(cp)))
            return 1
        print("[codepoint-ref] PASS（每个 CJK 码位都能在参照字体里找到）")
        return 0

    meta = json.loads(Path(args.meta).read_text(encoding="utf-8"))
    chars = meta["characters"]

    if args.selftest:
        # 注入 2026-10-26 的真实错配：把「荨」(U+8368) 塞进字表。
        # 荨是中文专用字，8 个日语参照字体里一个都没有 → 必须被抓到。
        injected = dict(chars)
        injected["荨"] = {"unicode": "U+8368", "strokes": 9, "grade": 4,
                          "frequency": 9999, "nanori": False, "variants": []}
        problems = check(injected, union, len(cms))
        hit = [p for p in problems if "荨" in p]
        print("[codepoint-ref] 自证用例：注入「荨」→U+8368（真实事故的错配）")
        if hit:
            print("[codepoint-ref] 实测：抓到了 → %s" % hit[0])
            # 反向自证：真正的「栄」(U+6804) 不该被报
            clean = check(chars, union, len(cms))
            false_pos = [p for p in clean if "栄" in p]
            if false_pos:
                print("[codepoint-ref] 反向自证失败：真正的「栄」被误报了 → %s" % false_pos)
                return 1
            print("[codepoint-ref] 反向自证：真正的「栄」(U+6804) 未被误报 ✓")
            return 0
        print("[codepoint-ref] 自证失败：已知错配没被抓到 —— 工具没有分辨力")
        return 1

    problems = check(chars, union, len(cms))
    if problems:
        print("[codepoint-ref] %d 个问题：" % len(problems))
        for p in problems[:60]:
            print("  " + p)
        return 1
    print("[codepoint-ref] PASS（%d 字，键 ↔ 码位 ↔ 参照字体三方一致）" % len(chars))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
