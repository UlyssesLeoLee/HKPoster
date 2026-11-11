#!/usr/bin/env python3
"""hk_charset_csv —— 生成 release/CHARSET.csv（docs/08 §4 要求的字符覆盖表）。

列：codepoint,char,glyph_name,layer,advance

**层标签（2026-11-11 修正）**
--------------------------
兼容别名层拆成两行标签 —— 因为 `hkposter-compat-001` 的取字顺序是
「手工 recipe 优先、自动 recipe 次之」：

* 目标统一字在**手工层**里 → 别名是手工字形的副本 → `兼容别名层（手工来源）`
* 目标统一字**只在自动层** → 别名是自动层字形的逐点副本 → `兼容别名层（APL 派生）`
  （这类共 267 个，必须计入 APL 衍生口径，见 `hk_apl_list.py`）

用法
----
```
python font-src/scripts/hk_charset_csv.py                     # 写 release/CHARSET.csv
python font-src/scripts/hk_charset_csv.py --out <path>
```
"""
from __future__ import annotations

import argparse
import csv
import io
import re
import sys
import unicodedata
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

FONT_SRC = Path(__file__).resolve().parents[1]
REPO = FONT_SRC.parent
sys.path.insert(0, str(FONT_SRC / "scripts"))

UNICODE_RE = re.compile(r'<unicode\s+hex="([0-9A-Fa-f]+)"')
GLYPH_NAME_RE = re.compile(r'<glyph\s+name="([^"]+)"')

L_MANUAL = "手工精造层"
L_AUTO = "自动骨架层"
L_LATIN = "拉丁扩展层"
L_COMPAT_MANUAL = "兼容别名层（手工来源）"
L_COMPAT_APL = "兼容别名层（APL 派生）"
L_SYMBOL = "符号补齐层"
L_BUILD = "构建期合成"

# 拉丁扩展层 = 发布说明里口径一致的那两个 master（255 字）
LATIN_MASTERS = ("hkposter-latin-lower-001.ufo", "hkposter-latin-ext-001.ufo")


def classify(master_name: str) -> str:
    if "auto" in master_name:
        return L_AUTO
    if master_name == "hkposter-compat-001.ufo":
        return "compat"
    if master_name == "hkposter-symbols-001.ufo":
        return L_SYMBOL
    if master_name in LATIN_MASTERS:
        return L_LATIN
    return L_MANUAL


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="生成 CHARSET.csv")
    ap.add_argument("--out", default="release/CHARSET.csv")
    ap.add_argument("--font", default="font-src/dist/HKPoster-Heavy.ttf")
    args = ap.parse_args(argv)

    from fontTools.ttLib import TTFont

    masters_dir = FONT_SRC / "masters"
    layer_of_glyph: dict[str, str] = {}
    manual_cps: set[int] = set()
    compat_cps: set[int] = set()

    for d in sorted(masters_dir.glob("*.ufo")):
        gdir = d / "glyphs"
        if not gdir.is_dir():
            continue
        kind = classify(d.name)
        for p in gdir.glob("*.glif"):
            txt = p.read_text(encoding="utf-8", errors="replace")
            mn = GLYPH_NAME_RE.search(txt)
            gname = mn.group(1) if mn else p.stem
            mu = UNICODE_RE.search(txt)
            cp = int(mu.group(1), 16) if mu else None
            tag = kind
            if kind == "compat":
                if cp is not None:
                    compat_cps.add(cp)
                tag = L_COMPAT_APL   # 稍后按「目标统一字是否在手工层」细分
            else:
                # 「手工层」= **非 auto** 的 master（兼容 recipe 的取字顺序里，
                # 手工 recipe 全部排在自动 recipe 之前）
                if cp is not None and kind != L_AUTO:
                    manual_cps.add(cp)
                tag = kind
            layer_of_glyph.setdefault(gname, tag)

    # 兼容别名细分：目标统一字在手工层里 ⇒ 手工来源
    for gname, tag in list(layer_of_glyph.items()):
        if tag != L_COMPAT_APL:
            continue
        m = re.match(r"^uni([0-9A-Fa-f]{4,6})$", gname.replace("_", ""))
        if not m:
            continue
        cp = int(m.group(1), 16)
        dec = unicodedata.decomposition(chr(cp)) if cp <= 0x10FFFF else ""
        if dec and not dec.startswith("<"):
            target = int(dec.split()[0], 16)
            layer_of_glyph[gname] = (L_COMPAT_MANUAL if target in manual_cps
                                     else L_COMPAT_APL)

    font = TTFont(str(REPO / args.font))
    cmap = font.getBestCmap()
    hmtx = font["hmtx"]

    rows = []
    for cp, gname in sorted(cmap.items()):
        adv = hmtx[gname][0] if gname in hmtx.metrics else 0
        rows.append({
            "codepoint": "U+%04X" % cp,
            "char": chr(cp),
            "glyph_name": gname,
            "layer": layer_of_glyph.get(gname, L_BUILD),
            "advance": adv,
        })

    out_path = (REPO / args.out).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["codepoint", "char", "glyph_name", "layer", "advance"])
        w.writeheader()
        w.writerows(rows)

    from collections import Counter
    c = Counter(r["layer"] for r in rows)
    print("[charset] 已写出 %s（%d bytes，%d 个码位）"
          % (out_path, out_path.stat().st_size, len(rows)))
    for k, v in c.most_common():
        print("[charset]   %-24s %d" % (k, v))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
