"""plan_joyo_batches —— 把 Jōyō 2136 字切分成可并行生产的 lane 批次。

分批原则
--------
1. **同 lane 内密度接近**：按笔画数分档（1–5 / 6–9 / 10–13 / 14–17 / 18+），
   同档的字形放在一起，family 观感才可能一致。
2. **高频字优先**：档内按 Kanjidic2 频率排名排序，先做最常用的字——
   即使程序中途停下，留下的也是最有用的子集。
3. **批次大小随密度递减**：简单字一批多（40），极密字一批少（10），
   因为越密的字单个越难做。
4. 每个批次一条 lane = 一个 recipe + 一个 UFO master，文件所有权天然互斥。

输出：font-src/data/joyo-batches.json
用法：python font-src/scripts/plan_joyo_batches.py
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parent.parent
META = FONT_SRC / "data" / "joyo-kanji-meta.json"
OUT = FONT_SRC / "data" / "joyo-batches.json"

# (密度档名, 笔画下限, 笔画上限, 每批字数)
DENSITY_CLASSES = [
    ("s1", 1, 5, 40),
    ("s2", 6, 9, 32),
    ("s3", 10, 13, 24),
    ("s4", 14, 17, 16),
    ("s5", 18, 99, 10),
]


def covered_by_masters() -> set[str]:
    """当前 master 已经提供的汉字（码位集合）。

    Jōyō 集合与我们的繁体 12 字**完全重叠**（港影城火夜風龍義警愛無道 都在常用漢字表里）。
    重画一遍既浪费，还会在合成时撞码（同一码位两个字形）。
    所以分批时必须先排除已覆盖的字。
    """
    from ufoLib2 import Font

    covered: set[str] = set()
    masters = FONT_SRC / "masters"
    if not masters.is_dir():
        return covered
    for master in sorted(masters.glob("*.ufo")):
        font = Font.open(str(master))
        for name in font.keys():
            for codepoint in font[name].unicodes:
                if 0x4E00 <= codepoint <= 0x9FFF:
                    covered.add(chr(codepoint))
    return covered


def main() -> int:
    meta = json.loads(META.read_text(encoding="utf-8"))
    characters = meta["characters"]
    if len(characters) != 2136:
        print(f"[batches] 元数据条目 {len(characters)} != 2136，先修数据")
        return 1

    # 计划是**追加式**的：已有批次不再重排（否则批次 id 对应的字集会漂移，
    # "机械续做"的承诺就废了）。本次只把**尚未分配**的字追加成新批次。
    existing_batches: list[dict] = []
    assigned: set[str] = set()
    wave_number = 2
    if OUT.exists():
        try:
            existing = json.loads(OUT.read_text(encoding="utf-8"))
            existing_batches = existing.get("batches", [])
            for batch in existing_batches:
                for item in batch.get("characters", []):
                    assigned.add(item["char"])
            for batch in existing_batches:
                match = re.search(r"-w(\d+)-", batch.get("id", ""))
                if match:
                    wave_number = max(wave_number, int(match.group(1)) + 1)
        except (OSError, ValueError):
            existing_batches = []
    wave = f"w{wave_number}"

    covered = covered_by_masters()
    buckets: dict[str, list[dict]] = defaultdict(list)
    unassigned: list[dict] = []
    for char, info in characters.items():
        if char in covered:
            continue  # 已有字形，跳过（不重画，也就不会撞码）
        if char in assigned:
            continue  # 已分配到既有批次，批次是追加式的，不再重排
        strokes = info.get("strokes") or 0
        frequency = info.get("frequency")
        placed = False
        for name, low, high, _ in DENSITY_CLASSES:
            if low <= strokes <= high:
                buckets[name].append(
                    {
                        "char": char,
                        "unicode": info["unicode"],
                        "strokes": strokes,
                        "grade": info.get("grade"),
                        "frequency": frequency,
                    }
                )
                placed = True
                break
        if not placed:
            # 笔画数缺失/异常的字不能被静默丢弃，否则会悄悄少做几个字
            unassigned.append(
                {
                    "char": char,
                    "unicode": info["unicode"],
                    "strokes": strokes,
                    "grade": info.get("grade"),
                    "frequency": frequency,
                }
            )
    if unassigned:
        # 归入最简单的一档，但必须显式记录，避免"以为都排进去了"
        buckets["s1"].extend(unassigned)
        print(f"[batches] 警告：{len(unassigned)} 个字笔画数缺失/异常，已并入 s1 档："
              f"{''.join(item['char'] for item in unassigned)}")

    batches = []
    for name, _low, _high, size in DENSITY_CLASSES:
        items = buckets.get(name, [])
        # 频率排名小的在前（None 排最后）
        items.sort(key=lambda item: (item["frequency"] is None, item["frequency"] or 0))
        for index in range(0, len(items), size):
            chunk = items[index : index + size]
            batches.append(
                {
                    "id": f"joyo-{wave}-{name}-{index // size + 1:03d}",
                    "class": name,
                    "size": len(chunk),
                    "stroke_range": [min(c["strokes"] for c in chunk), max(c["strokes"] for c in chunk)],
                    "min_frequency": min(
                        (c["frequency"] for c in chunk if c["frequency"]), default=None
                    ),
                    "characters": chunk,
                }
            )

    joyo_covered = {c for c in covered if c in characters}
    new_batches = batches
    all_batches = existing_batches + new_batches
    payload = {
        "source": meta["source"],
        "wave": wave,
        "total": sum(b["size"] for b in all_batches),
        "batch_count": len(all_batches),
        "already_covered": sorted(joyo_covered),
        "unassigned_strokes": [item["char"] for item in unassigned],
        "density_classes": [
            {"name": n, "strokes": [lo, hi], "batch_size": size} for n, lo, hi, size in DENSITY_CLASSES
        ],
        "batches": all_batches,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"[batches] 已被其他 master 覆盖的 Jōyō 字：{len(joyo_covered)} 个（不重画，避免撞码）")
    print(f"[batches] 本次新增 {len(new_batches)} 条批次（{wave}），累计 {payload['total']} 字 / {payload['batch_count']} 条 lane")
    if payload["total"] + len(joyo_covered) != 2136:
        print(f"[batches] 警告：{payload['total']} + {len(joyo_covered)} != 2136（必须有字被漏掉）")
    for name, _lo, _hi, _size in DENSITY_CLASSES:
        count = len(buckets.get(name, []))
        lanes = sum(1 for b in all_batches if b["class"] == name)
        print(f"  {name}: 本次 {count} 字 → 累计 {lanes} 条 lane")
    print(f"[batches] 已写出 {OUT}")
    if new_batches:
        head = new_batches[0]
        print(f"[batches] 本次首批 {head['id']}：{head['size']} 字，"
              f"笔画 {head['stroke_range']}，例：" +
              " ".join(c["char"] for c in head["characters"][:10]))
    else:
        pending = [
            b["id"] for b in all_batches
            if not (FONT_SRC / "masters" / f"hkposter-{b['id'].replace('joyo-', '')}.ufo").exists()
        ]
        print(f"[batches] 本次没有新批次可排（剩余字已全部分配）；待做批次 {len(pending)} 条")
        if pending:
            print(f"[batches] 下一条：{pending[0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
