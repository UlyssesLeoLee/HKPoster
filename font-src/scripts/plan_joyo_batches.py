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


def main() -> int:
    meta = json.loads(META.read_text(encoding="utf-8"))
    characters = meta["characters"]
    if len(characters) != 2136:
        print(f"[batches] 元数据条目 {len(characters)} != 2136，先修数据")
        return 1

    buckets: dict[str, list[dict]] = defaultdict(list)
    for char, info in characters.items():
        strokes = info.get("strokes") or 0
        frequency = info.get("frequency")
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
                break

    batches = []
    for name, _low, _high, size in DENSITY_CLASSES:
        items = buckets.get(name, [])
        # 频率排名小的在前（None 排最后）
        items.sort(key=lambda item: (item["frequency"] is None, item["frequency"] or 0))
        for index in range(0, len(items), size):
            chunk = items[index : index + size]
            batches.append(
                {
                    "id": f"joyo-{name}-{index // size + 1:03d}",
                    "class": name,
                    "size": len(chunk),
                    "stroke_range": [min(c["strokes"] for c in chunk), max(c["strokes"] for c in chunk)],
                    "min_frequency": min(
                        (c["frequency"] for c in chunk if c["frequency"]), default=None
                    ),
                    "characters": chunk,
                }
            )

    payload = {
        "source": meta["source"],
        "total": sum(b["size"] for b in batches),
        "batch_count": len(batches),
        "density_classes": [
            {"name": n, "strokes": [lo, hi], "batch_size": size} for n, lo, hi, size in DENSITY_CLASSES
        ],
        "batches": batches,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"[batches] 总字形 {payload['total']}，批次数 {payload['batch_count']}")
    for name, _lo, _hi, _size in DENSITY_CLASSES:
        count = len(buckets.get(name, []))
        lanes = sum(1 for b in batches if b["class"] == name)
        print(f"  {name}: {count} 字 → {lanes} 条 lane")
    print(f"[batches] 已写出 {OUT}")
    head = batches[0]
    print(f"[batches] 首批 {head['id']}：{head['size']} 字，"
          f"笔画 {head['stroke_range']}，例：" +
          " ".join(c["char"] for c in head["characters"][:10]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
