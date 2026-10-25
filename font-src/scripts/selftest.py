"""selftest — Phase 0 垂直切片自证。

证明整条链路真的能跑通（而不是纸面规格）：
    recipe → UFO → 合成 → TTF/OTF/WOFF2 → 字形 UT → 字体 IT/ST → PNG 样张

用法：python font-src/scripts/selftest.py
退出码：0 = 全链路 PASS
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
FONT_SRC = SCRIPT_DIR.parent
REPO_ROOT = FONT_SRC.parent
sys.path.insert(0, str(SCRIPT_DIR))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PY = sys.executable


def run(label: str, command: list[str]) -> tuple[bool, str]:
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=str(REPO_ROOT),
    )
    output = (result.stdout or "") + (result.stderr or "")
    ok = result.returncode == 0
    print(f"\n===== {label} =====")
    print(output.strip()[-4000:])
    print(f"----- {label}: {'PASS' if ok else 'FAIL'} (exit {result.returncode})")
    return ok, output


def main() -> int:
    results: dict[str, bool] = {}

    # 1. 参考 master 重新生成
    reference_recipe = FONT_SRC / "tools" / "reference_recipe.py"
    results["reference_recipe"] = run(
        "1/6 生成参考 master",
        [PY, str(reference_recipe)],
    )[0]

    # 2. recipe 与 UFO 同步
    results["check_recipes"] = run(
        "2/6 recipe 同步校验", [PY, str(SCRIPT_DIR / "check_recipes.py")]
    )[0]

    # 3. 字形 UT
    with tempfile.TemporaryDirectory(prefix="hkposter-selftest-") as tmp:
        report = Path(tmp) / "ut.json"
        results["check_glyphs"] = run(
            "3/6 字形 UT",
            [
                PY,
                str(SCRIPT_DIR / "check_glyphs.py"),
                "--sources",
                str(FONT_SRC / "tools" / "reference.ufo"),
                "--json",
                str(report),
            ],
        )[0]

        # 4. 构建字体
        dist = Path(tmp) / "dist"
        build_report = Path(tmp) / "build.json"
        results["build_font"] = run(
            "4/6 构建字体",
            [
                PY,
                str(SCRIPT_DIR / "build_font.py"),
                "--sources",
                str(FONT_SRC / "tools" / "reference.ufo"),
                "--out",
                str(dist),
                "--report",
                str(build_report),
            ],
        )[0]

        if not results["build_font"]:
            print("\n[selftest] 构建失败，后续检查跳过")
            print(json.dumps(results, ensure_ascii=False, indent=2))
            return 1

        # 5. 成品 IT/ST
        results["verify_font"] = run(
            "5/6 成品 IT/ST",
            [
                PY,
                str(SCRIPT_DIR / "verify_font.py"),
                "--font",
                str(dist / "HKPoster-Heavy.ttf"),
                "--sources",
                str(FONT_SRC / "tools" / "reference.ufo"),
                "--json",
                str(Path(tmp) / "verify.json"),
                "--png",
                str(Path(tmp) / "st-gdi-render.png"),
            ],
        )[0]

        # 6. 渲染样张
        sheet = Path(tmp) / "sheet.png"
        results["render"] = run(
            "6/6 渲染样张",
            [
                PY,
                str(SCRIPT_DIR / "render_glyph_sheet.py"),
                "--font",
                str(dist / "HKPoster-Heavy.ttf"),
                "--text",
                "港A0",
                "--size",
                "180",
                "--out",
                str(sheet),
            ],
        )[0]
        if sheet.exists():
            print(f"[selftest] 样张 PNG：{sheet}")

    print("\n===== selftest 汇总 =====")
    for label, ok in results.items():
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
    overall = all(results.values())
    print(f"[selftest] 全链路 {'PASS' if overall else 'FAIL'}")
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
