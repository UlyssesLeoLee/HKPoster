"""run_tests —— 一条命令跑完 Wave 0 的 UT / IT / ST，并输出汇总与 JSON 报告。

用法
----
    python font-src/tests/run_tests.py
    python font-src/tests/run_tests.py --no-build        # 不重新构建，直接用现有产物

报告：font-src/reports/tests.json
退出码：0 = 无 FAIL（有 WARN/SKIP 仍为 0），1 = 有 FAIL
"""

from __future__ import annotations

import argparse
import importlib.util
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

MODULES = ["test_glyph_metrics", "test_opentype", "test_platform_load"]
TITLES = {
    "test_glyph_metrics": "UT 字形度量与几何",
    "test_opentype": "IT 成品 OpenType 与排版",
    "test_platform_load": "ST 平台真实加载与光栅化",
}


def load_module(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPT_DIR / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser(description="Wave 0 测试套件")
    parser.add_argument("--no-build", action="store_true", help="不重新构建字体")
    parser.add_argument("--font", default=str(FONT_SRC / "dist" / "HKPoster-Heavy.ttf"))
    parser.add_argument("--report", default=str(FONT_SRC / "reports" / "tests.json"))
    args = parser.parse_args()

    font_path = Path(args.font).resolve()
    sources = sorted((FONT_SRC / "masters").glob("*.ufo"))
    if not sources:
        print("[tests] 没有找到 master（font-src/masters/*.ufo）")
        return 1

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "font": str(font_path),
        "masters": [p.name for p in sources],
        "suites": {},
    }

    if not args.no_build:
        print("[tests] 构建字体…")
        build = subprocess.run(
            [
                sys.executable,
                str(FONT_SRC / "scripts" / "build_font.py"),
                "--out",
                str(font_path.parent),
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=str(REPO_ROOT),
        )
        report["build"] = {
            "exit_code": build.returncode,
            "output_tail": (build.stdout or "")[-2000:],
        }
        if build.returncode != 0:
            print(build.stdout or "")
            print(build.stderr or "")
            print("[tests] 构建失败，测试中止")
            return 1

    if not font_path.exists():
        print(f"[tests] 找不到字体产物：{font_path}")
        return 1

    total = {"PASS": 0, "FAIL": 0, "WARN": 0, "SKIP": 0}
    for name in MODULES:
        module = load_module(name)
        try:
            outcomes = module.run({"font": font_path, "sources": sources})
        except Exception as error:  # noqa: BLE001
            outcomes = [
                {
                    "name": f"{name} 执行异常",
                    "status": "FAIL",
                    "detail": f"{type(error).__name__}: {error}",
                }
            ]
        counts = {"PASS": 0, "FAIL": 0, "WARN": 0, "SKIP": 0}
        for item in outcomes:
            counts[item["status"]] = counts.get(item["status"], 0) + 1
            total[item["status"]] = total.get(item["status"], 0) + 1
        report["suites"][name] = {"title": TITLES[name], "counts": counts, "results": outcomes}
        print(f"\n=== {TITLES[name]} ===")
        for item in outcomes:
            print(f"  {item['status']:<4} {item['name']}: {item['detail']}")
        print(f"  —— PASS {counts['PASS']} / FAIL {counts['FAIL']} / WARN {counts['WARN']} / SKIP {counts['SKIP']}")

    report["totals"] = total
    report["passed"] = total["FAIL"] == 0
    report_path = Path(args.report).resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\n=== 总计 ===")
    print(
        f"  PASS {total['PASS']} / FAIL {total['FAIL']} / "
        f"WARN {total['WARN']} / SKIP {total['SKIP']}"
    )
    print(f"[tests] 报告：{report_path}")
    return 0 if total["FAIL"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
