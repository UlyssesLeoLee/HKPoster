#!/usr/bin/env python3
"""hk_package —— 组装 HK Poster Heavy 发行包（复制字体/样张 → 校订 README → 打 zip）。

用法
----
```
python font-src/scripts/hk_package.py 0.6
python font-src/scripts/hk_package.py 0.6 --sha-a fec13b8 --sha-b <SHA_B> --date 2026-11-11
```

流程
----
1. 把 `font-src/dist` 的三个字体文件复制进 `release/fonts/`；
2. 把 `font-src/specimens/*.png` 复制进 `release/specimens/`；
3. 跑 `check_coverage.py` 取**实测**覆盖数字，回填 `release/README.md` 的覆盖表
   与「字形总数 / cmap 码位」；
4. 回填 README 的版本号、生成日期与两处提交 SHA 占位符（`__SHA_A__` / `__SHA_B__`）；
5. 打 `release/HKPoster-Heavy-v<版本>.zip`。

**行尾保持**：`release/README.md` 是 CRLF 文件，用文本模式读写会被归一化成 LF
（`git diff` 里整文件都变）⇒ 本脚本一律**按字节读写**。
"""
from __future__ import annotations

import argparse
import io
import os
import re
import shutil
import subprocess
import sys
import time
import zipfile
from datetime import date
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
REPO = FONT_SRC.parent
REL = REPO / "release"

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def copy_retry(src: Path, dst: Path, tries: int = 12, wait: float = 2.0) -> None:
    """带重试的复制 —— 本机 McAfee 实时扫描会短暂独占文件（WinError 32）。"""
    last = None
    for i in range(tries):
        try:
            shutil.copy2(src, dst)
            return
        except PermissionError as exc:  # noqa: PERF203
            last = exc
            print("[package] %s 被占用，第 %d 次重试…" % (dst.name, i + 1))
            time.sleep(wait)
    raise last


def coverage_table() -> tuple[str, str, str]:
    """跑覆盖审计，返回 (字形数, cmap 码位, markdown 覆盖表)。"""
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    env["OPENBLAS_NUM_THREADS"] = "1"
    env["OMP_NUM_THREADS"] = "1"
    r = subprocess.run([sys.executable, str(FONT_SRC / "scripts" / "check_coverage.py")],
                       capture_output=True, text=True, encoding="utf-8", env=env, cwd=REPO)
    cov = r.stdout
    print(cov)
    m = re.search(r"字形总数\s+(\d+)\s+cmap 码位\s+(\d+)", cov)
    glyphs, cmap = (m.group(1), m.group(2)) if m else ("?", "?")
    rows = []
    for line in cov.splitlines():
        if line.startswith(("中·", "日·", "英·")):
            parts = line.split()
            if len(parts) >= 5:
                name = " ".join(parts[:-4])
                total, have, gap, pct = parts[-4:]
                rows.append("| %s | %s | %s | %s | %s |" % (name, total, have, gap, pct))
    return glyphs, cmap, "\n".join(rows)


def rewrite_readme(ver: str, when: str, sha_a: str | None, sha_b: str | None,
                   glyphs: str, cmap: str, table: str) -> None:
    """按字节改写 release/README.md（保持 CRLF）。"""
    p = REL / "README.md"
    raw = p.read_bytes()
    txt = raw.decode("utf-8")

    def sub(pattern: str, repl: str, required: bool = True) -> None:
        nonlocal txt
        new, n = re.subn(pattern, repl, txt)
        if required and n == 0:
            raise SystemExit("[package] README 替换未命中：%s" % pattern)
        txt = new

    sub(r"# HK Poster Heavy —— 发行包 v[\d.]+", "# HK Poster Heavy —— 发行包 v%s" % ver)
    sub(r"- 生成日期：[\d\-]+", "- 生成日期：%s" % when)
    if sha_a:
        sub(r"__SHA_A__", sha_a)
    if sha_b:
        sub(r"__SHA_B__", sha_b)
    sub(r"- 字形总数 \*\*\d+\*\*；cmap 码位 \*\*\d+\*\*",
        "- 字形总数 **%s**；cmap 码位 **%s**" % (glyphs, cmap))

    start = txt.index("| 口径 | 全集 | 已覆盖 | 缺口 | 覆盖率 |")
    end = txt.index("**「智 U+667A」")
    newtab = "| 口径 | 全集 | 已覆盖 | 缺口 | 覆盖率 |\n|---|---|---|---|---|\n" + table + "\n\n"
    txt = txt[:start] + newtab + txt[end:]

    # 行尾：按原文件的换行风格写回
    nl = "\r\n" if b"\r\n" in raw else "\n"
    if nl == "\n":
        txt = txt.replace("\r\n", "\n")
    else:
        txt = re.sub(r"(?<!\r)\n", "\r\n", txt)
    p.write_bytes(txt.encode("utf-8"))
    print("[package] README 已更新")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="组装发行包")
    ap.add_argument("version")
    ap.add_argument("--sha-a", default=None, help="字体二进制构建自提交")
    ap.add_argument("--sha-b", default=None, help="发行 tag 指向的提交")
    ap.add_argument("--date", default=None, help="生成日期（默认今天）")
    args = ap.parse_args(argv)

    ver = args.version
    when = args.date or date.today().isoformat()

    fdst = REL / "fonts"
    fdst.mkdir(parents=True, exist_ok=True)
    for f in ("HKPoster-Heavy.ttf", "HKPoster-Heavy.otf", "HKPoster-Heavy.woff2"):
        src = FONT_SRC / "dist" / f
        copy_retry(src, fdst / f)
        print("[package] fonts/%s %d bytes" % (f, (fdst / f).stat().st_size))

    sdst = REL / "specimens"
    sdst.mkdir(parents=True, exist_ok=True)
    for p in sorted((FONT_SRC / "specimens").glob("*.png")):
        copy_retry(p, sdst / p.name)
        print("[package] specimens/%s" % p.name)

    glyphs, cmap, table = coverage_table()
    rewrite_readme(ver, when, args.sha_a, args.sha_b, glyphs, cmap, table)

    zp = REL / ("HKPoster-Heavy-v%s.zip" % ver)
    if zp.exists():
        zp.unlink()
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for base, _dirs, files in os.walk(REL):
            for f in files:
                full = Path(base) / f
                rel = full.relative_to(REL)
                if rel.suffix == ".zip":
                    continue
                z.write(full, str(Path("HKPoster-Heavy-v%s" % ver) / rel))
    print("[package] zip: %s %d bytes" % (zp, zp.stat().st_size))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
