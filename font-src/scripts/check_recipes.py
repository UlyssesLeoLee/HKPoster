"""check_recipes — 校验「recipe 与生成的 .ufo 是否同步」。

规则
----
* 每个 recipe 模块必须暴露 `build() -> list[Glyph]` 与 `target_ufo() -> Path`；
* `.ufo` 是**生成物**：改形状必须改 recipe 再重新生成；
* 本脚本重新生成一份到临时目录，与仓库里的 `.ufo` 逐文件比对。

用法：python font-src/scripts/check_recipes.py
退出码：0 = 同步，1 = 不同步或缺文件
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
FONT_SRC = SCRIPT_DIR.parent
REPO_ROOT = FONT_SRC.parent
sys.path.insert(0, str(SCRIPT_DIR))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import ufoLib2  # noqa: E402


def load_recipe(path: Path):
    name = "recipe_" + path.stem.replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def info_dict(font_path: Path) -> dict:
    font = ufoLib2.Font.open(str(font_path))
    return {key: getattr(font.info, key) for key in dir(font.info) if not key.startswith("_")}


def _norm(raw: bytes) -> bytes:
    """归一化行尾后再比对。

    仓库 core.autocrlf=true：checkout 出来的 .glif 是 CRLF，
    而 recipe 重新生成的是 LF。直接比字节会误报"不同步"，
    所以比较前统一把 CRLF 折成 LF。
    """
    return raw.replace(b"\r\n", b"\n")


def compare(recipe_path: Path) -> list[str]:
    problems: list[str] = []
    module = load_recipe(recipe_path)
    if not hasattr(module, "build") or not hasattr(module, "target_ufo"):
        return [f"{recipe_path.name}: 缺少 build() 或 target_ufo()"]
    target = Path(module.target_ufo())
    if not target.exists():
        return [f"{recipe_path.name}: 目标 UFO 不存在：{target}"]

    from hkbuild import write_ufo

    with tempfile.TemporaryDirectory(prefix="hkposter-recipe-") as tmp:
        regenerated = Path(tmp) / "regenerated.ufo"
        write_ufo(regenerated, module.build())
        committed_glifs = {
            p.name: _norm(p.read_bytes()) for p in (target / "glyphs").glob("*.glif")
        }
        regenerated_glifs = {
            p.name: _norm(p.read_bytes()) for p in (regenerated / "glyphs").glob("*.glif")
        }
        if set(committed_glifs) != set(regenerated_glifs):
            missing = sorted(set(regenerated_glifs) - set(committed_glifs))
            extra = sorted(set(committed_glifs) - set(regenerated_glifs))
            if missing:
                problems.append(f"{recipe_path.name}: UFO 缺少字形 {missing}")
            if extra:
                problems.append(f"{recipe_path.name}: UFO 多出字形 {extra}")
        for name in sorted(set(committed_glifs) & set(regenerated_glifs)):
            if committed_glifs[name] != regenerated_glifs[name]:
                problems.append(f"{recipe_path.name}: 字形 {name} 与 recipe 不同步")
        try:
            if info_dict(target) != info_dict(regenerated):
                problems.append(f"{recipe_path.name}: fontinfo 与 recipe 不同步")
        except Exception as error:  # noqa: BLE001
            problems.append(f"{recipe_path.name}: fontinfo 读取失败 {error}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="recipe 与 UFO 同步校验")
    parser.add_argument("--recipes", nargs="*", default=None)
    args = parser.parse_args()

    if args.recipes:
        recipes = [Path(p).resolve() for p in args.recipes]
    else:
        recipes = []
        src_dir = FONT_SRC / "src"
        if src_dir.is_dir():
            recipes = sorted(src_dir.glob("*.py"))
        reference = FONT_SRC / "tools" / "reference_recipe.py"
        if reference.exists():
            recipes.append(reference)

    problems: list[str] = []
    for recipe in recipes:
        found = compare(recipe)
        status = "OK " if not found else "BAD"
        print(f"[check_recipes] {status} {recipe.name}")
        problems.extend(found)
    for problem in problems:
        print(f"  FAIL  {problem}")
    print(f"[check_recipes] {'PASS' if not problems else 'FAIL'}（问题 {len(problems)}）")
    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
