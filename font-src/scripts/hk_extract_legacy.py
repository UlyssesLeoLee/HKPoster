#!/usr/bin/env python3
"""hk_extract_legacy —— 从历史提交里抽出「已通过门禁、但新生成器产出更差几何」的字形。

背景（2026-11-11）
------------------
v0.6 修掉了自动生成器的四个真 bug（`extend_ends` 延长目标取错、折角交点外甩、
`make_transform` 不夹 em 盒、退化笔产生尖刺环）。修完后有 **29 个字**在新生成器下
过不了质量闸（白口 / 腔高），相对 v0.5 成了**回退**（丢字）。

逐字对比后发现：这些字在 **v0.5 的几何其实是更好的**。
典型例子 `擼` U+64FC —— 鱼部里两根横画 y=597.5 与 y=620（相距 22.5）：
  * v0.5：两横的 x 区间在 616.4 **刚好相接不重叠** ⇒ `check_hcounters` 判「无 x 重叠」跳过，
    门禁通过；
  * 新生成器：延长接头后 x 区间**重叠** ⇒ 判白口 FAIL —— 几何反而更差。

所以修法不是「继续压重量」（实测按笔降档只救回 2/29，其余卡在「白口（已最轻）」），
而是**把 v0.5 那 29 个字原样恢复**，做成独立的恢复层。

做法
----
1. 从指定提交（默认 `HEAD`）读 `font-src/src/hkposter-auto-{cjk,joyo}.py`；
2. 按字符名（`unicodedata.name()` → `g_xxx`）切出对应的 `def g_xxx() -> Glyph:` 整块；
3. 原样写进 `font-src/src/hkposter-auto-legacyNN.py`（含 provenance 头）。

**原语逐字照抄，不做任何改动** —— 这些原语在 v0.5 已经过了全部门禁
（`verify_all` 14/14），恢复它们只是回到一个**已知通过**的状态。

用法
----
```
python font-src/scripts/hk_extract_legacy.py --out font-src/src/hkposter-auto-legacy29.py
python font-src/src/hkposter-auto-legacy29.py     # 生成对应 UFO
```
"""
from __future__ import annotations

import argparse
import io
import subprocess
import sys
import unicodedata
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
REPO = FONT_SRC.parent
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# v0.5 → v0.6 回退清单（实测：对比 HEAD 与工作区的 .glif 路径集合得到）
LEGACY_CHARS = (
    "喋嫱嬗帏撾擼欞毽氆氪犍矓碟蔷襢谍輿轀鄙醴馘魝鯡鳟鸪鼾尊論輪"
)

HEADER_TEMPLATE = '''"""HK Poster Heavy —— {outname} 恢复层（{count} 字）。

这批字在 v0.6 里**相对 v0.5 成了回退**（新生成器过不了质量闸 ⇒ 丢字）。
逐字对比后确认：**v0.5 的几何反而更好** —— 新生成器修掉四个真 bug 后，
这 {count} 个字的接头延长把相邻横画从「刚好相接」推成了「x 区间重叠」，
于是 `check_hcounters` 判白口 FAIL（典型：`擼` U+64FC，y=597.5 / y=620 两横）。

所以这里的原语**逐字照抄**自提交 `{commit}` 的
`font-src/src/hkposter-auto-cjk.py` / `hkposter-auto-joyo.py`，
未做任何改动 —— 它们在 v0.5 已经过了全部门禁（`verify_all` 14/14）。
恢复它们等于回到一个**已知通过**的状态，而不是新造一个几何。

抽取脚本：`font-src/scripts/hk_extract_legacy.py`（可复现）。

字表
----
{chartable}

运行：python font-src/src/{outname}
"""

from __future__ import annotations

import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, write_ufo  # noqa: E402

'''

TAIL_TEMPLATE = '''

def build() -> list[Glyph]:
    return [
{listbody}
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "{ufo}.ufo"


if __name__ == "__main__":
    _target = target_ufo()
    _target.parent.mkdir(parents=True, exist_ok=True)
    write_ufo(_target, build())
    print("[recipe] 已写出 %s" % _target)
'''


def git_show(rev: str, path: str) -> str:
    r = subprocess.run(["git", "show", "%s:%s" % (rev, path)],
                       cwd=REPO, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        return ""
    return r.stdout


def fn_name(ch: str) -> str:
    """与 hk_autogen._fnname 同口径：g_<unicode.name 清洗>。"""
    try:
        name = unicodedata.name(ch)
    except ValueError:
        name = "U%04X" % ord(ch)
    return "g_" + "".join(c if c.isalnum() else "_" for c in name).strip("_").lower()


def extract_block(text: str, fn: str) -> str | None:
    """切出 `def <fn>() -> Glyph:` 到下一个顶层 def 之间的整块。"""
    start = text.find("def %s(" % fn)
    if start < 0:
        return None
    nxt = text.find("\ndef ", start + 1)
    block = text[start: nxt if nxt > 0 else len(text)]
    return block.rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="从历史提交抽取恢复层 recipe")
    ap.add_argument("--out", default="font-src/src/hkposter-auto-legacy29.py")
    ap.add_argument("--rev", default="HEAD")
    ap.add_argument("--chars", default=LEGACY_CHARS)
    args = ap.parse_args(argv)

    out_path = (REPO / args.out).resolve()
    chars = [c for c in args.chars if c.strip()]
    out_stem = out_path.stem
    ufo_name = out_stem.replace(".py", "")

    sources = {}
    for stem in ("hkposter-auto-cjk", "hkposter-auto-joyo"):
        text = git_show(args.rev, "font-src/src/%s.py" % stem)
        if text:
            sources[stem] = text
    if not sources:
        print("[legacy] 取不到 %s 的历史 recipe" % args.rev)
        return 1

    blocks = []
    chartable = []
    missing = []
    for ch in chars:
        fn = fn_name(ch)
        block = None
        for stem, text in sources.items():
            block = extract_block(text, fn)
            if block:
                break
        if not block:
            missing.append(ch)
            continue
        blocks.append(block)
        chartable.append("* `%s` U+%04X —— %s"
                         % (ch, ord(ch), unicodedata.name(ch)))

    if missing:
        print("[legacy] ⚠ 在 %s 里找不到 %d 个字：%s"
              % (args.rev, len(missing), "".join(missing)))

    commit = subprocess.run(["git", "rev-parse", args.rev], cwd=REPO,
                            capture_output=True, text=True, encoding="utf-8").stdout.strip()
    subject = subprocess.run(["git", "log", "-1", "--format=%s", args.rev], cwd=REPO,
                              capture_output=True, text=True, encoding="utf-8").stdout.strip()

    header = HEADER_TEMPLATE.format(
        outname=out_path.name, count=len(blocks), commit=commit,
        chartable="\n".join(chartable))
    listbody = "".join("        %s(),        # %s U+%04X\n"
                        % (fn_name(ch), ch, ord(ch)) for ch in chars if ch not in missing)
    tail = TAIL_TEMPLATE.format(listbody=listbody, ufo=ufo_name)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(header + "\n".join(blocks) + "\n" + tail, encoding="utf-8")
    print("[legacy] 已写出 %s（%d 个字，来源 %s %s）"
          % (out_path, len(blocks), commit[:7], subject))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
