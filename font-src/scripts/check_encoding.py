"""check_encoding —— 扫描仓库文本里的字符损坏（U+FFFD 替换字符）。

为什么需要
----------
本项目的**设计源是 Python recipe**，recipe 里写着「干」「令」「圧」这些字符本身。
写入过程（尤其是大文件的一次性 write）会偶发把个别字符写坏，
表现为 U+FFFD 替换字符 —— 一个坏字符进 recipe，就会在字体里变成**错字形**，
而且 `check_glyphs.py` 查不出来（它只验证码位唯一与轮廓合法，不验证字符内容）。

实测：平假名返工规格里就出现过 2 处（说明文字），提交信息里 1 处。

判据
----
* 任何**受版本控制**的文本文件里出现 U+FFFD → FAIL
* 任何文本文件**无法按 UTF-8 解码** → FAIL
* 提交信息里出现 U+FFFD → WARN（历史记录按「不改 git 历史」的约定保留原样，只报不改）

用法
----
    python font-src/scripts/check_encoding.py
    python font-src/scripts/check_encoding.py --include-untracked
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

if hasattr(sys, "stdout") and "reconfigure" in dir(sys.stdout):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[2]
TEXT_EXT = {".py", ".md", ".json", ".txt", ".yaml", ".yml", ".fea", ".toml", ".cfg",
            ".glyphs", ".plist", ".glif", ".designspace"}
SKIP_DIR = {".git", "dist", "reports", "__pycache__", ".worktrees"}


def _tracked_files() -> list[Path]:
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "-z"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        if out.returncode == 0:
            return [ROOT / p for p in out.stdout.split("\0") if p]
    except Exception:
        pass
    return []


def _all_files() -> list[Path]:
    out = []
    for p in ROOT.rglob("*"):
        if p.is_file() and not any(part in SKIP_DIR for part in p.parts):
            out.append(p)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="扫描文本里的字符损坏")
    ap.add_argument("--include-untracked", action="store_true",
                    help="连未受版本控制的文件一起扫（默认只扫已入库的）")
    args = ap.parse_args()

    files = _all_files() if args.include_untracked else _tracked_files()
    bad_decode: list[tuple[Path, str]] = []
    bad_char: list[tuple[Path, int, str]] = []

    for p in files:
        if p.suffix.lower() not in TEXT_EXT:
            continue
        try:
            raw = p.read_bytes()
        except OSError:
            continue
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            bad_decode.append((p, f"{exc.reason} @ byte {exc.start}"))
            continue
        if "\ufffd" in text:
            for i, line in enumerate(text.splitlines(), 1):
                if "\ufffd" in line:
                    idx = line.index("\ufffd")
                    bad_char.append(
                        (p, i, line[max(0, idx - 28):idx + 28].strip())
                    )

    # 提交信息（只报不改）
    try:
        log = subprocess.run(
            ["git", "-C", str(ROOT), "log", "--format=%H%x00%s%x00%b%x00"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        ).stdout
    except Exception:
        log = ""
    commit_hits = [l for l in log.split("\0") if "\ufffd" in l]

    print(f"[encoding] 扫描 {len(files)} 个文件")
    if bad_decode:
        print(f"[encoding] FAIL 无法按 UTF-8 解码 {len(bad_decode)} 个：")
        for p, why in bad_decode:
            print(f"  {p.relative_to(ROOT)}  {why}")
    if bad_char:
        print(f"[encoding] FAIL 含替换字符 U+FFFD {len(bad_char)} 处：")
        for p, ln, ctx in bad_char:
            print(f"  {p.relative_to(ROOT)}:{ln}  …{ctx}…")
    if commit_hits:
        print(f"[encoding] WARN 提交信息里有损坏 {len(commit_hits)} 条"
              f"（按「不改 git 历史」的约定保留原样）：")
        for h in commit_hits[:10]:
            print(f"  {h[:120]}")

    if bad_decode or bad_char:
        print("[encoding] 失败：坏字符进 recipe 就是错字形，必须修掉再进字体")
        return 1
    print("[encoding] PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
