"""verify_all — 集成验证：把当前仓库里所有 master 合成构建并跑完整检查。

合并阶段每次合并后都要跑这个脚本，它是"能不能进 dev"的唯一判据。

用法：
    python font-src/scripts/verify_all.py
    python font-src/scripts/verify_all.py --out font-src/dist --report font-src/reports/verify-all.json

检查项：
    1. recipe ↔ UFO 同步（font-src/src/*.py + tools/reference_recipe.py）
    2. 字形 UT（全部 masters）
    3. 构建 TTF / OTF / WOFF2
    4. 成品 IT/ST（含 Windows GDI 真实加载与替换检测）
    5. 渲染总样张 PNG

退出码：0 = 全部通过
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
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
    print(output.strip()[-6000:])
    print(f"----- {label}: {'PASS' if ok else 'FAIL'} (exit {result.returncode})")
    return ok, output


def main() -> int:
    parser = argparse.ArgumentParser(description="集成验证")
    parser.add_argument("--out", default=str(FONT_SRC / "dist"))
    parser.add_argument("--report", default=None)
    parser.add_argument("--skip-render", action="store_true")
    parser.add_argument("--skip-tests", action="store_true")
    parser.add_argument("--skip-kana-check", action="store_true")
    parser.add_argument("--skip-encoding-check", action="store_true")
    args = parser.parse_args()

    masters = sorted((FONT_SRC / "masters").glob("*.ufo"))
    print(f"[verify_all] 发现 {len(masters)} 个 master：{[m.name for m in masters]}")
    if not masters:
        print("[verify_all] 没有 master，无法验证")
        return 1

    results: dict[str, bool] = {}
    outputs: dict[str, str] = {}

    results["check_recipes"], outputs["check_recipes"] = run(
        "1/8 recipe 同步", [PY, str(SCRIPT_DIR / "check_recipes.py")]
    )
    results["check_glyphs"], outputs["check_glyphs"] = run(
        "2/8 字形 UT", [PY, str(SCRIPT_DIR / "check_glyphs.py")]
    )

    build_report = FONT_SRC / "reports" / "build.json"
    results["build_font"], outputs["build_font"] = run(
        "3/8 构建字体",
        [
            PY,
            str(SCRIPT_DIR / "build_font.py"),
            "--out",
            args.out,
            "--report",
            str(build_report),
        ],
    )

    font_path = Path(args.out).resolve() / "HKPoster-Heavy.ttf"
    if results["build_font"]:
        results["verify_font"], outputs["verify_font"] = run(
            "4/8 成品 IT/ST",
            [
                PY,
                str(SCRIPT_DIR / "verify_font.py"),
                "--font",
                str(font_path),
                "--png",
                str(FONT_SRC / "reports" / "st-gdi-render.png"),
            ],
        )
    else:
        results["verify_font"] = False
        outputs["verify_font"] = "构建失败，未执行"

    if not args.skip_render:
        sheet = FONT_SRC / "reports" / "sheet-all.png"
        results["render"], outputs["render"] = run(
            "5/8 渲染总样张",
            [
                PY,
                str(SCRIPT_DIR / "render_glyph_sheet.py"),
                "--font",
                str(font_path),
                "--text",
                "港影城火夜風龍義警愛無道ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789，。！？",
                "--size",
                "150",
                "--columns",
                "10",
                "--out",
                str(sheet),
            ],
        )
    else:
        results["render"] = True
        outputs["render"] = "（跳过）"

    # 6) UT / IT / ST 测试套件（复用上一步已构建的产物，不重复构建）
    if not args.skip_tests:
        results["tests"], outputs["tests"] = run(
            "6/8 UT/IT/ST 测试套件",
            [
                PY,
                str(FONT_SRC / "tests" / "run_tests.py"),
                "--no-build",
                "--font",
                str(font_path),
                "--report",
                str(FONT_SRC / "reports" / "tests.json"),
            ],
        )
    else:
        results["tests"] = True
        outputs["tests"] = "（跳过）"

    # 7) 假名保真度检查（缺字 = 硬门禁；骨架 IoU = 软信号）
    if not args.skip_kana_check:
        results["kana_fidelity"], outputs["kana_fidelity"] = run(
            "7/8 假名保真度检查",
            [
                PY,
                str(SCRIPT_DIR / "check_kana_fidelity.py"),
                "--font",
                str(font_path),
                "--out",
                str(FONT_SRC / "reports" / "kana-fidelity.json"),
                "--sheet",
                str(FONT_SRC / "reports" / "kana-fidelity.png"),
            ],
        )
    else:
        results["kana_fidelity"] = True
        outputs["kana_fidelity"] = "（跳过）"

    # 8) 字符编码检查（坏字符进 recipe 就是错字形）
    if not args.skip_encoding_check:
        results["encoding"], outputs["encoding"] = run(
            "8/8 字符编码检查",
            [PY, str(SCRIPT_DIR / "check_encoding.py")],
        )
    else:
        results["encoding"] = True
        outputs["encoding"] = "（跳过）"

    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "masters": [m.name for m in masters],
        "results": results,
        "all_passed": all(results.values()),
    }
    report_path = (
        Path(args.report).resolve()
        if args.report
        else FONT_SRC / "reports" / "verify-all.json"
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\n===== verify_all 汇总 =====")
    for label, ok in results.items():
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
    overall = all(results.values())
    print(f"[verify_all] {'全部通过' if overall else '存在失败项'}（报告：{report_path}）")
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
