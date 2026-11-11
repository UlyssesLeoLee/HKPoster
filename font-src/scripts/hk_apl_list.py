#!/usr/bin/env python3
"""hk_apl_list —— 生成 release/APL-derived-codepoints.txt（APL 衍生字形的精确码位清单）。

**口径（2026-11-11 修正）**
--------------------------
APL 衍生 = 一切**源自 `hanzi-writer-data` 笔画中线**的字形，包含两类：

1. **自动骨架层本身**：`hkposter-auto-*.ufo`（cjk / inc1 / joyo / legacy29）；
2. **兼容别名层里、目标统一字只存在于自动层的那部分别名**。

第 2 类以前被漏记了 —— v0.6 准备时实测：
402 个兼容别名里 **267 个**的目标统一字**只存在于自动层**
（`hkposter-compat-001` 的取字顺序是「手工 recipe 优先、自动 recipe 次之」，
目标字在手工层里没有 ⇒ 别名就是自动层字形的逐点副本 ⇒ APL 衍生）。
把它们漏在「手工绘制、不含 APL 数据」那一栏是**不准确的**，
必须据实计入（铁律 5：不编造许可证状态）。

判据实现
--------
「目标统一字是否在手工层里」= 该码位是否出现在**任一非 auto master**的 `<unicode>` 标签里。
这与 `hkposter-compat-001` 的取字顺序等价（手工 recipe 全部排在自动 recipe 之前），
但只需扫文件、不必 import 全部 recipe。

用法
----
```
python font-src/scripts/hk_apl_list.py                       # 写 release/APL-derived-codepoints.txt
python font-src/scripts/hk_apl_list.py --out <path>          # 写到别处
```
"""
from __future__ import annotations

import argparse
import io
import re
import sys
import unicodedata
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
REPO = FONT_SRC.parent
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

UNICODE_RE = re.compile(r'<unicode\s+hex="([0-9A-Fa-f]+)"')
COMPAT_LO, COMPAT_HI = 0xF900, 0xFAFF


def master_codepoints(master: Path) -> set[int]:
    out = set()
    gdir = master / "glyphs"
    if not gdir.is_dir():
        return out
    for p in gdir.glob("*.glif"):
        m = UNICODE_RE.search(p.read_text(encoding="utf-8", errors="replace"))
        if m:
            out.add(int(m.group(1), 16))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="生成 APL 衍生字形码位清单")
    ap.add_argument("--out", default="release/APL-derived-codepoints.txt")
    args = ap.parse_args(argv)

    masters_dir = FONT_SRC / "masters"
    apl_masters: dict[str, list[int]] = {}
    manual_cps: set[int] = set()
    compat_cps: set[int] = set()

    for d in sorted(masters_dir.glob("*.ufo")):
        cps = master_codepoints(d)
        if not cps:
            continue
        if "auto" in d.name:
            apl_masters[d.name] = sorted(cps)
        elif d.name == "hkposter-compat-001.ufo":
            compat_cps = cps
        else:
            manual_cps |= cps

    # 兼容别名：目标统一字在手工层里找不到 ⇒ 别名是自动层字形的副本 ⇒ APL 衍生
    apl_compat = []
    for cp in sorted(compat_cps):
        dec = unicodedata.decomposition(chr(cp))
        if not dec or dec.startswith("<"):
            continue
        target = int(dec.split()[0], 16)
        if target not in manual_cps:
            apl_compat.append(cp)

    auto_union = set()
    for cps in apl_masters.values():
        auto_union |= set(cps)
    total = auto_union | set(apl_compat)

    out_path = (REPO / args.out).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# HK Poster Heavy — Arphic Public License 衍生字形码位清单",
        "#",
        "# 这些字形由 hanzi-writer-data 的「笔画中线」重画生成，属于",
        "# Arphic Public License 项下的衍生物（APL §2：允许修改，但须声明并随包保留许可）。",
        "#",
        "# 生成方式：",
        "#   1) 读 font-src/masters/hkposter-auto-*.ufo/glyphs/*.glif 的 <unicode> 标签（自动骨架层）",
        "#   2) 再扫描 font-src/masters/hkposter-compat-001.ufo —— 其中**目标统一字只存在于",
        "#      自动层**的兼容别名，是自动层字形的逐点副本，同样计入 APL 衍生",
        "#      （兼容 recipe 的取字顺序：手工 recipe 优先、自动 recipe 次之）",
        "# 生成脚本：font-src/scripts/hk_apl_list.py（可复现）",
        "#",
        "# ==== 按来源统计 ====",
    ]
    for m, cps in apl_masters.items():
        lines.append("# %s : %d 个" % (m, len(cps)))
    lines.append("# 自动骨架层合计（去重）：%d 个" % len(auto_union))
    lines.append("# 兼容别名层中的 APL 派生别名：%d 个" % len(apl_compat))
    lines.append("# 合计（去重）：%d 个" % len(total))
    lines.append("")
    for m, cps in apl_masters.items():
        lines.append("## %s (%d)" % (m, len(cps)))
        lines.append(" ".join("U+%04X" % c for c in cps))
        lines.append("")
    lines.append("## 兼容别名层中的 APL 派生别名 (%d)" % len(apl_compat))
    lines.append(" ".join("U+%04X" % c for c in apl_compat))
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print("[apl] 已写出 %s（%d bytes）" % (out_path, out_path.stat().st_size))
    print("[apl] 自动骨架层 %d + APL 派生兼容别名 %d = 合计 %d 个 APL 衍生码位"
          % (len(auto_union), len(apl_compat), len(total)))
    for m, cps in apl_masters.items():
        print("[apl]   %s : %d" % (m, len(cps)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
