"""check_coverage —— 中日英覆盖审计（**审计工具，不是门禁**）。

为什么要有这个检查器
--------------------
「至少覆盖中日英所有字」是一个**长期目标**，不是一条能一次判 FAIL 的门禁：
缺口几千字是**已知的、在推进中的**状态，把它做成 FAIL 门禁会让 verify_all 永远红。

所以这里做的是**审计**：分层报出「全集 / 已覆盖 / 缺口 / 覆盖率」，
让缺口变成**可量化的数字**而不是感觉。
与 `audit_white_holes.py` 同一性质（审计，不是门禁）。

口径分层（从紧到宽）
--------------------
  中·实用层  GB2312 全部有效码位（6763 汉字 + 682 符号/假名区）
  中·全字表  CJK 统一表意文字 U+4E00–9FFF（20992）+ 扩展 A U+3400–4DBF（6592）
  中·兼容表  CJK 兼容表意文字 U+F900–FAFF（512）
  日·漢字    Jōyō 2136（font-src/data/joyo-kanji-meta.json）
  日·假名    平假名 / 片假名 / 浊点 / 半浊点 / 迭代记号
  日·标点    全角标点 U+3000–303F + 全角形式 U+FF01–FF60 · U+FFE0–FFE6
  英·ASCII  U+0020–007E
  英·Latin1 U+00A0–00FF
  英·标点    General Punctuation U+2000–206F

口径来源（都可离线复核）
------------------------
  * GB2312：用 Python 自带的 gb2312 编解码器穷举双字节区（权威、无需联网）
  * Jōyō 2136：joyo-kanji-meta.json（Kanjidic2 + X0213）
  * 其余：Unicode 码位区间（Unicode 15.1 标准块）

用法
----
    python font-src/scripts/check_coverage.py                 # 审计成品字体
    python font-src/scripts/check_coverage.py --font <ttf>
    python font-src/scripts/check_coverage.py --selftest      # 口径自证
    python font-src/scripts/check_coverage.py --json          # 机器可读

`--selftest` 自证的是**口径本身**：GB2312 汉字数必须是 6763、Jōyō 必须是 2136、
ASCII 必须是 95 —— 口径写错的话，覆盖率数字就是错的。
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))
sys.stdout.reconfigure(encoding="utf-8")


def gb2312_all() -> set[int]:
    """GB2312 全部有效码位（汉字 + 符号区）。"""
    out: set[int] = set()
    for hi in range(0xA1, 0xFF):
        for lo in range(0xA1, 0xFF):
            try:
                out.add(ord(bytes([hi, lo]).decode("gb2312")))
            except UnicodeDecodeError:
                continue
    return out


def rng(a: int, b: int) -> set[int]:
    return set(range(a, b + 1))


def joyo_set() -> set[int]:
    meta = json.loads(
        (FONT_SRC / "data" / "joyo-kanji-meta.json").read_text(encoding="utf-8"))
    return {int(v["unicode"][2:], 16) for v in meta["characters"].values()}


def layers() -> list[tuple[str, set[int]]]:
    return [
        ("中·GB2312 常用字（含符号区）", gb2312_all()),
        ("中·CJK 统一表意文字 U+4E00–9FFF", rng(0x4E00, 0x9FFF)),
        ("中·CJK 扩展 A U+3400–4DBF", rng(0x3400, 0x4DBF)),
        ("中·CJK 兼容表意文字 U+F900–FAFF", rng(0xF900, 0xFAFF)),
        ("日·Jōyō 常用漢字 2136", joyo_set()),
        ("日·平假名 U+3041–309F", rng(0x3041, 0x309F)),
        ("日·片假名 U+30A0–30FF", rng(0x30A0, 0x30FF)),
        ("日·假名符号·浊点半浊点",
         {0x309B, 0x309C, 0x3099, 0x309A}),
        ("日·迭代记号 U+309D–309F · ー · ヽヾヿ",
         {0x309D, 0x309E, 0x309F, 0x30FC, 0x30FD, 0x30FE, 0x30FF}),
        ("日·全角标点 U+3000–303F", rng(0x3000, 0x303F)),
        ("日·全角形式 U+FF01–FF60 · U+FFE0–FFE6",
         rng(0xFF01, 0xFF60) | rng(0xFFE0, 0xFFE6)),
        ("英·ASCII U+0020–007E", rng(0x20, 0x7E)),
        ("英·Latin-1 补充 U+00A0–00FF", rng(0xA0, 0xFF)),
        ("英·通用标点 U+2000–206F", rng(0x2000, 0x206F)),
    ]


def selftest() -> int:
    """口径自证：口径写错 ⇒ 覆盖率数字就是错的。"""
    checks = [
        ("GB2312 全部有效码位 = 7445（6763 汉字 + 682 符号区）",
         len(gb2312_all()), 7445),
        ("GB2312 汉字 = 6763", len(gb2312_all() & rng(0x4E00, 0x9FFF)), 6763),
        ("Jōyō = 2136", len(joyo_set()), 2136),
        ("CJK 统一表意文字 = 20992", len(rng(0x4E00, 0x9FFF)), 20992),
        ("CJK 扩展 A = 6592", len(rng(0x3400, 0x4DBF)), 6592),
        ("CJK 兼容表意文字 = 512", len(rng(0xF900, 0xFAFF)), 512),
        ("ASCII = 95", len(rng(0x20, 0x7E)), 95),
        ("Latin-1 = 96", len(rng(0xA0, 0xFF)), 96),
        ("通用标点 U+2000–206F = 112", len(rng(0x2000, 0x206F)), 112),
        ("全角标点 U+3000–303F = 64", len(rng(0x3000, 0x303F)), 64),
    ]
    bad = 0
    for name, got, want in checks:
        ok = got == want
        print(f"  [{'OK ' if ok else 'BAD'}] {name}  实得 {got}")
        if not ok:
            bad += 1
    if bad:
        print(f"[coverage] selftest FAIL：{bad} 项口径不符")
        return 1
    print("[coverage] selftest PASS：全部口径与权威数字一致")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="中日英覆盖审计")
    ap.add_argument("--font", default=str(FONT_SRC / "dist" / "HKPoster-Heavy.ttf"))
    ap.add_argument("--json", action="store_true", help="机器可读输出")
    ap.add_argument("--selftest", action="store_true", help="口径自证")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    from fontTools.ttLib import TTFont

    f = TTFont(args.font)
    cmap: set[int] = set()
    for t in f["cmap"].tables:
        cmap.update(t.cmap.keys())

    rows = []
    for name, s in layers():
        have = s & cmap
        rows.append({
            "layer": name, "total": len(s), "covered": len(have),
            "missing": len(s) - len(have),
            "coverage": round(100.0 * len(have) / len(s), 1) if s else 0.0,
        })

    if args.json:
        print(json.dumps({"font": args.font, "glyphs": f["maxp"].numGlyphs,
                          "cmap": len(cmap), "layers": rows},
                         ensure_ascii=False, indent=2))
        return 0

    print(f"字体：{args.font}")
    print(f"字形总数 {f['maxp'].numGlyphs}   cmap 码位 {len(cmap)}")
    print()
    print(f"{'口径':<48}{'全集':>8}{'已覆盖':>8}{'缺口':>8}{'覆盖率':>9}")
    for r in rows:
        print(f"{r['layer']:<48}{r['total']:>8}{r['covered']:>8}"
              f"{r['missing']:>8}{r['coverage']:>8.1f}%")
    print()
    print("（本工具是**审计**不是门禁：缺口是已知且在推进中的状态，不判 FAIL。）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
