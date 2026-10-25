"""build_font — 把多个 UFO master 合成一个字体并编译为 TTF / OTF / WOFF2。

用法
----
    python font-src/scripts/build_font.py --out font-src/dist
    python font-src/scripts/build_font.py --out font-src/dist --sources font-src/masters/hkposter-latin.ufo
    python font-src/scripts/build_font.py --out font-src/dist --formats ttf woff2

默认行为
--------
* 源：font-src/masters/*.ufo（全部），或 --sources 指定的目录
* 特性：font-src/features/*.fea 依次拼进 UFO 的 features.fea
* 产物：font-src/dist/HKPoster-Heavy.{ttf,otf,woff2}
* 证据：font-src/reports/build.json（命令、版本、源提交、哈希、表清单）

注意：CPython 3.13 无 skia-pathops 轮子，ufo2ft 的 removeOverlaps 不可用；
轮廓并集已在源阶段由 hkbuild/shapely 完成，故此处固定 removeOverlaps=False。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
FONT_SRC = SCRIPT_DIR.parent
REPO_ROOT = FONT_SRC.parent

sys.path.insert(0, str(SCRIPT_DIR))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import ufo2ft  # noqa: E402
from ufoLib2 import Font  # noqa: E402

from hkbuild import ASCENDER, DESCENDER, UPM, notdef_glyph, space_glyph  # noqa: E402

FAMILY = "HK Poster"
STYLE = "Heavy"
POSTSCRIPT_NAME = "HKPoster-Heavy"


def rel_path(path: Path) -> str:
    """仓库内路径转相对 POSIX 风格；仓库外则原样返回。"""
    try:
        return str(path.relative_to(REPO_ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_info() -> dict:
    def run(*args: str) -> str:
        try:
            result = subprocess.run(
                ["git", *args],
                cwd=str(REPO_ROOT),
                capture_output=True,
                text=True,
                timeout=20,
            )
            return result.stdout.strip()
        except Exception:
            return ""

    status = run("status", "--porcelain")
    return {
        "head": run("rev-parse", "HEAD"),
        "branch": run("rev-parse", "--abbrev-ref", "HEAD"),
        "dirty": bool(status),
    }


def collect_sources(explicit: list[str] | None) -> list[Path]:
    if explicit:
        return [Path(p).resolve() for p in explicit]
    masters = FONT_SRC / "masters"
    if not masters.is_dir():
        return []
    return sorted(p for p in masters.glob("*.ufo") if p.is_dir())


def collect_features() -> list[Path]:
    features_dir = FONT_SRC / "features"
    if not features_dir.is_dir():
        return []
    return sorted(features_dir.glob("*.fea"))


def composite(sources: list[Path]) -> tuple[Font, list[str]]:
    """把多个 master 合成一个 UFO Font；返回 (font, 冲突列表)。"""
    if not sources:
        raise SystemExit("没有找到任何 UFO master（--sources 或 font-src/masters/*.ufo）")
    base = Font.open(str(sources[0]))
    conflicts: list[str] = []
    for source in sources[1:]:
        other = Font.open(str(source))
        for name in other.keys():
            if name in base:
                conflicts.append(f"{name}（{source.name} 与既有 master 重复）")
                continue
            base[name] = other[name]
    if ".notdef" not in base:
        glyph = notdef_glyph()
        target = base.newGlyph(".notdef")
        target.width = glyph.advance
        glyph.draw(target.getPen())
    if "space" not in base:
        glyph = space_glyph()
        target = base.newGlyph("space")
        target.width = glyph.advance
        target.unicodes = [glyph.unicode] if glyph.unicode is not None else []
        glyph.draw(target.getPen())
    return base, conflicts


def apply_features(font: Font, feature_files: list[Path]) -> list[str]:
    chunks = []
    used = []
    for path in feature_files:
        text = path.read_text(encoding="utf-8")
        if text.strip():
            chunks.append(text.rstrip() + "\n")
            used.append(path.name)
    if chunks:
        font.features = "\n".join(chunks)
    return used


def compile_formats(
    font: Font, out_dir: Path, formats: list[str]
) -> list[tuple[str, Path]]:
    outputs: list[tuple[str, Path]] = []
    out_dir.mkdir(parents=True, exist_ok=True)

    ttf_font = None
    ttf_path = out_dir / f"{POSTSCRIPT_NAME}.ttf"
    if "ttf" in formats:
        ttf_font = ufo2ft.compileTTF(font, removeOverlaps=False)
        ttf_font.save(str(ttf_path))
        outputs.append(("ttf", ttf_path))

    if "otf" in formats:
        otf_font = ufo2ft.compileOTF(font, removeOverlaps=False)
        otf_path = out_dir / f"{POSTSCRIPT_NAME}.otf"
        otf_font.save(str(otf_path))
        outputs.append(("otf", otf_path))

    if "woff2" in formats:
        from fontTools.ttLib import TTFont

        ttf_requested = "ttf" in formats
        if not ttf_path.exists():
            ufo2ft.compileTTF(font, removeOverlaps=False).save(str(ttf_path))
        woff2_font = TTFont(str(ttf_path))
        woff2_font.flavor = "woff2"
        woff2_path = out_dir / f"{POSTSCRIPT_NAME}.woff2"
        woff2_font.save(str(woff2_path))
        outputs.append(("woff2", woff2_path))
        if not ttf_requested:
            ttf_path.unlink(missing_ok=True)

    return outputs


def describe_outputs(outputs: list[tuple[str, Path]]) -> list[dict]:
    from fontTools.ttLib import TTFont

    described = []
    for kind, path in outputs:
        font = TTFont(str(path), lazy=True)
        described.append(
            {
                "format": kind,
                "file": rel_path(path),
                "bytes": path.stat().st_size,
                "sha256": sha256_of(path),
                "tables": sorted(font.keys()),
                "num_glyphs": font["maxp"].numGlyphs,
            }
        )
        font.close()
    return described


def main() -> int:
    parser = argparse.ArgumentParser(description="合成 UFO master 并编译字体")
    parser.add_argument("--out", default=str(FONT_SRC / "dist"), help="产物目录")
    parser.add_argument(
        "--sources", nargs="*", default=None, help="UFO master 目录（默认全部 masters/*.ufo）"
    )
    parser.add_argument(
        "--formats", nargs="*", default=["ttf", "otf", "woff2"], help="输出格式"
    )
    parser.add_argument("--report", default=None, help="证据 JSON 路径")
    parser.add_argument("--keep-temp", action="store_true", help="保留合成 UFO")
    args = parser.parse_args()

    sources = collect_sources(args.sources)
    feature_files = collect_features()
    out_dir = Path(args.out).resolve()

    font, conflicts = composite(sources)
    used_features = apply_features(font, feature_files)

    tmp_dir = Path(tempfile.mkdtemp(prefix="hkposter-build-", dir=str(FONT_SRC)))
    try:
        ufo_path = tmp_dir / "composite.ufo"
        font.save(str(ufo_path), overwrite=True)
        outputs = compile_formats(font, out_dir, list(args.formats))
    finally:
        if args.keep_temp:
            print(f"[build_font] 临时目录保留：{tmp_dir}")
        else:
            shutil.rmtree(tmp_dir, ignore_errors=True)

    described = describe_outputs(outputs)
    unicode_count = 0
    for name in font.keys():
        glyph = font[name]
        if glyph.unicodes:
            unicode_count += 1

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "command": " ".join([sys.executable.split("\\")[-1], *sys.argv]),
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "libraries": {
            "fontTools": __import__("fontTools").version,
            "ufo2ft": getattr(ufo2ft, "__version__", "unknown"),
            "ufoLib2": __import__("ufoLib2").__version__,
            "shapely": __import__("shapely").__version__,
        },
        "git": git_info(),
        "metrics": {
            "unitsPerEm": UPM,
            "ascender": ASCENDER,
            "descender": DESCENDER,
        },
        "sources": [rel_path(p) for p in sources],
        "features": used_features,
        "glyph_count": len(font.keys()),
        "unicode_glyph_count": unicode_count,
        "conflicts": conflicts,
        "outputs": described,
    }

    report_path = Path(args.report).resolve() if args.report else FONT_SRC / "reports" / "build.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[build_font] 源 master：{len(sources)} 个")
    for source in sources:
        print(f"           - {source.name}")
    if conflicts:
        print(f"[build_font] 警告：{len(conflicts)} 处 glyph 名重复：")
        for conflict in conflicts:
            print(f"           ! {conflict}")
    print(f"[build_font] glyph：{report['glyph_count']}（含 Unicode：{unicode_count}）")
    for item in described:
        print(
            f"[build_font] {item['format']:>5}  {item['file']}  "
            f"{item['bytes']} bytes  sha256={item['sha256'][:16]}…"
        )
    print(f"[build_font] 证据：{report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
