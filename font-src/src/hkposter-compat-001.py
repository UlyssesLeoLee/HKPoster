"""HK Poster Heavy —— CJK 兼容表意文字别名层（compat-001）。

Unicode 把 U+F900–FAFF 这 512 个「兼容表意文字」定义为
**规范单例分解**（canonical singleton decomposition）到统一表意文字，例如：

    U+F900 豈  →  U+8C48 車
    U+F901  更  →  U+8C48 車

规范等价意味着**它们就是同一个字符**，字体必须渲染成同一个字形
（这是 Unicode 的规定，不是近似；Noto / Source Han 全部这么处理）。

做法
----
1. 用 `unicodedata.decomposition()` 取出每个兼容码位的单例分解目标；
2. 从**既有 recipe**（手工层优先，自动层次之）取该统一字的原语
   （`_parts` / `_prims` 逐条深拷贝）；
3. 换名字、换码位，写进本层的 master。

墨形与统一表意字**逐点相同** —— 因为它们本来就是同一个字。

依赖
----
本 recipe 在运行时 import 其它 recipe 取字形。
⇒ 改了那些 recipe，必须重新生成本 recipe 的 UFO，
   否则 `check_recipes.py` 会报「字形与 recipe 不同步」。

运行：python font-src/src/hkposter-compat-001.py
"""

from __future__ import annotations

import copy
import importlib.util
import sys
import unicodedata
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, write_ufo  # noqa: E402

CJK_ADV = 1000
COMPAT_LO, COMPAT_HI = 0xF900, 0xFAFF

# 本 recipe 自己在 src/ 下，import 时要跳过
SELF = "hkposter-compat-001"


def _recipe_files() -> list[Path]:
    """按「手工层优先、自动层次之、文件名排序」的顺序列出 recipe 文件。

    排序固定 ⇒ 同一个字出现在多个层时，**选中的来源是确定的**
    （否则 check_recipes 会因为「这次选了 A、下次选了 B」而报不同步）。
    """
    files = [p for p in (FONT_SRC / "src").glob("*.py")
             if p.stem != SELF and not p.stem.startswith("_")]
    manual = sorted(p for p in files if "auto" not in p.stem)
    auto = sorted(p for p in files if "auto" in p.stem)
    return manual + auto


def _load(path: Path):
    name = "hkcompat_" + path.stem.replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def collect_by_unicode() -> dict[int, Glyph]:
    """跑一遍既有 recipe，取「码位 → 字形对象」。

    只在需要时逐个 import：找到一个就记下，全部找到就提前收工
    （auto-cjk 有 8800 个字形，全量 build 一次要十几秒）。
    """
    wanted = set()
    for cp in range(COMPAT_LO, COMPAT_HI + 1):
        dec = unicodedata.decomposition(chr(cp))
        if not dec or dec.startswith("<"):
            continue
        wanted.add(int(dec.split()[0], 16))
    print("[compat] 需要的目标统一字 %d 个" % len(wanted))

    found: dict[int, Glyph] = {}
    for path in _recipe_files():
        if not wanted - set(found):
            break
        try:
            module = _load(path)
            builder = getattr(module, "build", None)
            if builder is None:
                continue
            for glyph in builder():
                cp = getattr(glyph, "unicode", None)
                if cp in wanted and cp not in found:
                    found[cp] = glyph
        except Exception as error:  # noqa: BLE001
            print("[compat] 跳过 %s：%s" % (path.name, error))
    return found


def clone_parts(dst: Glyph, src: Glyph) -> None:
    """把 src 的原语逐条深拷贝进 dst（与 latin-ext-001 的同名工具同口径）。

    必须连 `_prims` 一起复制：`_parts`（几何）与 `_prims`（原语类型）
    是一一对应的，缺一个会让 check_hcounters「按原语类型判横」错位。
    """
    for part, prim in zip(src._parts, src._prims):
        dst._parts.append([(float(x), float(y)) for (x, y) in part])
        dst._prims.append(copy.deepcopy(prim))


def build() -> list[Glyph]:
    """返回本层的全部字形（兼容码位 → 统一字形的别名）。"""
    source = collect_by_unicode()
    glyphs: list[Glyph] = []

    for cp in range(COMPAT_LO, COMPAT_HI + 1):
        dec = unicodedata.decomposition(chr(cp))
        if not dec:
            continue
        if dec.startswith("<"):
            # 兼容性分解（非规范等价）—— 不做别名，另案处理。
            continue
        target = int(dec.split()[0], 16)
        base = source.get(target)
        if base is None:
            continue
        glyph = Glyph("uni%04X" % cp, advance=CJK_ADV, unicode=cp,
                      note="%s：兼容表意文字（= 统一表意文字 U+%04X）"
                           % (chr(cp), target))
        clone_parts(glyph, base)
        glyphs.append(glyph)

    print("[compat] 产出 %d 个别名字形（512 个兼容码位中 %d 个有统一字可依）"
          % (len(glyphs), len(glyphs)))
    return glyphs


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-compat-001.ufo"


if __name__ == "__main__":
    _target = target_ufo()
    _target.parent.mkdir(parents=True, exist_ok=True)
    write_ufo(_target, build())
    print("[recipe] 已写出 %s" % _target)
