"""check_charset —— 字形「字符 ↔ 码位 ↔ 清单」三者的自洽检查。

为什么要有这个检查器
--------------------
2026-10-26 的实测事故：`joyo-kanji-meta.json` 的 `characters` 表里，
「栄」那一行被**以「枤」(U+6804) 为键**写入 —— 键选错了字，
但同一条记录里的 `unicode` 字段和频率数据仍然是「栄」的。
后果是「字段 vs 键」的自洽检查**查不出来**（两边都指向 U+6804），
而成品字体因此**缺 U+8368（栄）、多出 U+6804（枤，字形却是栄的形状）**。

这道检查器用两个互相独立的证据源交叉验证：

1. **glyph 的 note 里的汉字** vs **glyph 的 unicode**。
   每个 recipe 的字形都带 note（如 `note="栄：ツ + 冖 + 木"`），
   note 里的第一个汉字就是这个字形「自称是谁」。
   note 是子代理按规格写的汉字标注，与 unicode 是**两条独立来源** ——
   对不上就说明码位写错了。
2. **每个 master 的码位集合** vs **joyo-batches.json 的冻结清单**。
   缺字或多字都算错。

判据：note 里没有汉字（纯英文/符号标注）的字形跳过第 1 项。

用法
----
    python font-src/scripts/check_charset.py
    python font-src/scripts/check_charset.py --recipes font-src/src/hkposter-joyo-w2-s2-011.py
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))


def _cjk_chars(text: str) -> list[str]:
    return [c for c in text if 0x3400 <= ord(c) <= 0x9FFF]


def _load_module(path: Path):
    name = "_charset_" + path.stem.replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"无法加载 {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--recipes", nargs="*", default=None,
                    help="只查这些 recipe（文件名即可）")
    args = ap.parse_args()

    src_dir = FONT_SRC / "src"
    if args.recipes:
        paths = []
        for item in args.recipes:
            p = Path(item)
            if not p.exists():
                p = src_dir / (Path(item).stem + ".py")
            paths.append(p)
    else:
        paths = sorted(src_dir.glob("hkposter-*.py"))

    # 冻结清单：批次 id -> 码位集合
    expect: dict[str, set[int]] = {}
    batches_path = FONT_SRC / "data" / "joyo-batches.json"
    if batches_path.exists():
        data = json.loads(batches_path.read_text(encoding="utf-8"))
        for batch in data.get("batches", []):
            bid = batch.get("id", "")
            cps = set()
            for c in batch.get("characters", []):
                u = c.get("unicode", "")
                if u.startswith("U+"):
                    cps.add(int(u[2:], 16))
            if cps:
                expect[bid.replace("joyo-w2-", "")] = cps

    problems: list[str] = []
    checked_glyphs = 0
    checked_notes = 0

    for path in paths:
        if not path.exists():
            continue
        try:
            mod = _load_module(path)
            built = mod.build()
        except Exception as exc:  # noqa: BLE001
            problems.append(f"{path.name}: 无法 build（{type(exc).__name__}: {exc}）")
            continue

        actual = {g.unicode for g in built if getattr(g, "unicode", None)}
        checked_glyphs += len(built)

        # --- 1. note 的汉字 vs unicode ---
        # 只在 note 写成「<字>：<部件说明>」这种格式时检查 ——
        # 标点的 note 是描述词（如「全角括号「」」「句号」），不是字形自称，不能查。
        for g in built:
            if getattr(g, "unicode", None) is None:
                continue
            note = getattr(g, "note", "") or ""
            if len(note) < 2 or note[1] != "：":
                continue
            claimed = note[0]
            cp = ord(claimed)
            if not (0x3400 <= cp <= 0x9FFF or 0x3040 <= cp <= 0x30FF):
                continue
            checked_notes += 1
            if cp != g.unicode:
                problems.append(
                    f"{path.name}: {g.name} 的 note 自称「{claimed}」(U+{cp:04X})，"
                    f"但 unicode 是 U+{g.unicode:04X} —— 码位与字形不符"
                )

        # --- 2. 码位集合 vs 冻结清单 ---
        bid = path.stem.replace("hkposter-joyo-w2-", "")
        if bid in expect:
            missing = expect[bid] - actual
            extra = actual - expect[bid]
            if missing:
                problems.append(
                    f"{path.name}: 缺清单里的 {len(missing)} 个字："
                    + " ".join(f"U+{c:04X}" for c in sorted(missing))
                )
            if extra:
                problems.append(
                    f"{path.name}: 多出清单外的 {len(extra)} 个字："
                    + " ".join(f"U+{c:04X}" for c in sorted(extra))
                )

    print(f"[charset] 扫了 {len(paths)} 个 recipe，{checked_glyphs} 个字形"
          f"（其中 {checked_notes} 个带汉字标注已与 unicode 交叉核对）")
    if problems:
        print(f"[charset] 发现 {len(problems)} 处问题：")
        for p in problems:
            print(f"    {p}")
        print(f"[charset] FAIL（问题 {len(problems)}）")
        return 1
    print("[charset] PASS（问题 0）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
