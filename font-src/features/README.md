# font-src/features —— OpenType 特性源

构建时 `font-src/scripts/build_font.py` 会把本目录下**所有** `*.fea` 按文件名顺序
拼进 UFO 的 `features.fea`，再由 ufo2ft 编译进成品字体。

| 文件 | 归属 lane | 内容 | 当前状态 |
|---|---|---|---|
| `kerning-latin.fea` | `latin-core` | AV / AW / TA / TO / YA / LT 六组 kerning | **已启用**（GPOS 已生成） |
| `features-core.fea` | `quality-harness` | 核心特性（locl / palt / halt 预留位） | 全部以注释预留，未启用 |

## 为什么 palt / halt / locl 现在不启用

OpenType 的 feature 替换目标必须在字体里真实存在，否则 ufo2ft 编译直接失败。
当前字体只有每个字符的单一字形：

* `locl` 需要一套地区字形（简体衍生），本轮未制作；
* `palt` / `halt` 需要标点的比例宽度版本 / 半宽版本，本轮未制作。

因此 `features-core.fea` 里只保留带说明的注释块，等对应字形到位后再启用，
并同时在 `font-src/tests/test_opentype.py` 补上断言。

## 验证

```powershell
python font-src/scripts/build_font.py --out font-src/dist
python font-src/tests/run_tests.py
```

`test_opentype.py` 会检查 GPOS 是否存在，并对 AV / TA / LY 三组断言
「排版推进宽度 < 无 kern 的 advance 之和」——即 kerning 真的生效了，而不只是表存在。
