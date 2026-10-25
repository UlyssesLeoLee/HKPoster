# HK Poster Heavy — Wave 0 并行制作契约

**编号：FONT-HKP-CTR-001｜版本：v1.0｜基线提交：见 `git log -1 dev`**
**适用对象：参与 Wave 0 制作的全部 lane（子代理）与其集成方**

本契约是并行制作的**唯一接口定义**。所有 lane 在自己的 worktree 里独立施工，
**文件所有权互斥**；集成方按本契约逐条验收后合并。

> 上游依据：`docs/05_工程详细设计.md`（交付链路与目录）、`docs/06_字符集与制作规划.md`
> （Wave 0 范围）、`docs/03_字形结构基本设计.md`（轮廓规则 GLY-001..006）、
> `docs/02_视觉基本设计.md`（风格语义与偏差控制）、`docs/04_字体系统与排版基本设计.md`
> （命名与度量候选）、`docs/09_对抗式自审.md`（Wave 0 是正式批量绘制的前置条件）。

---

## 0. 本轮范围（Wave 0）

| 项 | 内容 | 状态 |
|---|---|---|
| 目标 | 完成 Wave 0 代表字形试制 + 单色样张，**冻结关键比例与端点系统** | 本轮 |
| 汉字 | 12 个高信息量代表字（见 §5） | 本轮 |
| Latin | 大写 A–Z、数字 0–9、中英标点 | 本轮 |
| 字体格式 | OTF / TTF / WOFF2 | 本轮 |
| 测试 | UT / IT / ST 全套可执行 | 本轮 |
| 明确不在本轮 | 500/1500 字扩展、简体衍生、可变字体、发布授权 | 后续阶段 |

**边界（来自 docs/09 §3）：** 本轮产出是"试制 + 冻结参数"，**不等于**成品字体发行；
许可证保持 `UNDECIDED`，发布门禁仍然阻断。

---

## 1. 目录结构与文件所有权（互斥）

```
font-src/
├── CONTRACT.md               # 本契约（集成方维护）
├── data/design-params.json   # 冻结参数（集成方维护）
├── scripts/                  # 构建与检查工具链（集成方维护）
│   ├── hkbuild.py            # 笔画原语库
│   ├── build_font.py         # 合成 UFO → TTF/OTF/WOFF2 + 证据
│   ├── check_glyphs.py       # 字形 UT
│   ├── check_recipes.py      # recipe ↔ UFO 同步校验
│   ├── verify_font.py        # 成品 IT/ST（含 Windows GDI 真实加载）
│   ├── render_glyph_sheet.py # 基础样张渲染
│   └── selftest.py           # 全链路自证
├── src/                      # ★ 各 lane 的 recipe（设计源，唯一权威）
├── masters/                  # ★ 各 lane 的 UFO master（由 recipe 生成）
├── features/                 # ★ OpenType 特性源（.fea）
├── tests/                    # ★ 可执行测试套件
├── specimens/                # ★ 样张（PNG + 生成脚本）
├── tools/reference_recipe.py # 参考实现（风格基准，港/A/0）
├── tools/reference.ufo       # 由参考 recipe 生成
├── dist/                     # 构建产物（不入库）
└── reports/                  # 机器报告（不入库）
```

★ = 各 lane 可写。**除 ★ 之外的任何文件都不得修改**；发现工具链问题请写进交付报告，
由集成方修，不要自己改 `scripts/`。

---

## 2. 冻结参数（数值一律以此为准）

来源：`font-src/data/design-params.json`

| 参数 | 值 |
|---|---|
| UPM | 1000 |
| ascender / descender | 880 / -120 |
| CJK advance | 1000（**必须**） |
| Latin 大写 advance | 640 |
| 数字 advance | 640 |
| 空格 advance | 500 |
| 大写顶线 | y = 700 |
| CJK 字面框 | x 60..940，y 0..820 |
| CJK 笔画权重 | 主 96 / 次 92 / 细 84 / 点 84–96 |
| **Latin 笔画权重** | **主 132 / 次 120 / 斜 112 / 细 104** |

坐标：y 向上，基线 y=0；整数单位。

> **权重分两档，不要混用。** CJK 与 Latin 不能共用同一套笔画权重：
> 同样 96 单位在 1000 UPM 的 CJK 里读作 Heavy，但在 640 advance 的 Latin 里
> 只读作 Regular。这是 Wave 0 样张实测出来的结论（见 `docs/09` RV-14），
> 后续任何新增 master 都要按所属类别取对应那一档。

---

## 3. 笔画原语 API（`font-src/scripts/hkbuild.py`）

```python
g = Glyph(name, advance=1000, unicode=0x6E2F, note="说明")

g.hbar(x1, x2, y, weight=96, cut_left=0, cut_right=0)   # 水平笔画：中心线 y，横跨 x1..x2
g.vbar(x, y1, y2, weight=96, cut_bottom=0, cut_top=0)     # 垂直笔画：中心线 x，跨 y1..y2
g.diag(x1, y1, x2, y2, weight=96)                        # 斜笔画：中心线两端点，厚度垂直于中心线
g.dot(cx, cy, w=96, h=112, slant=0)                      # 点/短撇：平行四边形，slant 为顶部右移
g.rect(x1, x2, y1, y2)                                   # 原始矩形
g.poly([(x, y), ...])                                    # 原始多边形
g.ring(outer_pts, inner_pts)                             # 环形带（等长点列）→ 内白自动成洞
```

要点：

1. **每条笔画是"中心线 + 垂直权重"**，不是"上下边界"。`hbar(330, 920, 790, weight=96)`
   实际占据 y 742..838。
2. 笔画**自动求并集**（shapely），因此轮廓无自交、无重叠；内白（counter）自动成为洞。
   不要再手工画"洞"。
3. `cut_left/cut_right` 沿笔画方向偏移端面，用于海报式斜切端点（GLY-003）：
   只允许用于不影响辨识的结构位置。
4. 坐标全部取整；不要写小数。

---

## 4. Recipe 契约（设计源）

每个 lane 的设计源是 `font-src/src/<lane 名>.py`，必须暴露两个函数：

```python
"""<lane 描述>"""
from __future__ import annotations
import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, write_ufo   # noqa: E402


def build() -> list[Glyph]:
    """返回本 lane 的全部字形。"""
    g = Glyph("uni6E2F", advance=1000, unicode=0x6E2F, note="港")
    g.hbar(330, 920, 790, weight=96)
    ...
    return [g]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-cjk-core.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
```

**规则**

- `.ufo` 是**生成物**。改形状必须改 recipe 再重新生成（`check_recipes.py` 会逐文件比对）。
- recipe 必须**确定性**：同样输入永远生成同样的 `.ufo`；禁止随机、时间戳、外部文件依赖。
- recipe 只允许 import `hkbuild` 与标准库。
- 字形名：CJK 用 `uniXXXX`（大写十六进制），Latin 大写用字母本身（`A`），
  数字用 AGL 名（`zero`、`one`…），标点用 AGL 名（`comma`、`period`…），
  中日韩标点用 `uniXXXX`。
- 一个字形一个 Unicode，禁止私用区码点。

---

## 5. 各 lane 的字符清单（冻结，不得增删）

### Lane `cjk-core` → `font-src/src/hkposter-cjk-core.py` + `masters/hkposter-cjk-core.ufo/`

| 字符 | Unicode | 字形名 | 备注 |
|---|---|---|---|
| 港 | U+6E2F | uni6E2F | 左右结构：氵 + 巷；保护氵与巷的分隔 |
| 影 | U+5F71 | uni5F71 | 左右结构：景 + 彡 |
| 城 | U+57CE | uni57CE | 左右结构：土 + 成 |
| 火 | U+706B | uni706B | 独体点画字 |
| 夜 | U+591C | uni591C | 上中下结构 |
| 風 | U+98A8 | uni98A8 | 包围结构；外框与内部虫部件需形成清晰对比 |

### Lane `cjk-dense` → `font-src/src/hkposter-cjk-dense.py` + `masters/hkposter-cjk-dense.ufo/`

| 字符 | Unicode | 字形名 | 备注 |
|---|---|---|---|
| 龍 | U+9F8D | uni9F8D | 高密字：内部多短笔之间的白必须留出 |
| 義 | U+7FA9 | uni7FA9 | 高密字：层叠横画在小字号不得合并 |
| 警 | U+8B66 | uni8B66 | 高密字：上艹/敬 + 下言 |
| 愛 | U+611B | uni611B | 上中下 + 心部 |
| 無 | U+7121 | uni7121 | 高密字：四点底不得粘连成横 |
| 道 | U+9053 | uni9053 | 包围 + 首 |

### Lane `latin-core` → `font-src/src/hkposter-latin.py` + `masters/hkposter-latin.ufo/` + `features/kerning-latin.fea`

- 大写 A–Z（26 个），advance 640，大写顶线 **y=700**、基线 0
- 数字 0–9（10 个），advance 640，高度与 A 一致（顶 700、底 0）
- 笔画权重取 **Latin 档**（主 132 / 次 120 / 斜 112 / 细 104，见 §2）
- `features/kerning-latin.fea`：按 docs/04 §3 实现 **AV / AW / TA / TO / YA / LT** 六组，
  并给出可解释的数值依据（侧边距实测差）；文件首行写注释说明取值方法。

### Lane `latin-punct` → `font-src/src/hkposter-latin-punct.py` + `masters/hkposter-latin-punct.ufo/`

- 全角标点 13 个：，。、！？：；（）「」【】，advance 1000，墨形位置按实测系统字体取位
- 半角标点 13 个：. , ! ? : ; ( ) - — " ' &，advance 240–340
- 字形名：半角用 AGL 名（period/comma/exclam…），全角用 `uniXXXX`

### Lane `quality-harness` → `font-src/tests/**` + `font-src/features/features-core.fea`

- `font-src/tests/run_tests.py`：一条命令跑完 UT + IT + ST，输出 PASS/FAIL 汇总与 JSON 报告
- `font-src/tests/test_glyph_metrics.py`：逐字形断言（advance、bbox、笔画权重落在所属档位、
  内白存在性、空字形禁止）
- `font-src/tests/test_opentype.py`：cmap 覆盖、必需表、GSUB/GPOS 存在性、
  排版不出现 .notdef（用 uharfbuzz）
- `font-src/tests/test_platform_load.py`：Windows GDI 真实加载 + 渲染（复用 `verify_font.py` 的做法）
- `font-src/features/features-core.fea`：`locl`（地区字形切换预留）、`palt`/`halt` 占位**注释掉**，
  不得启用没有对应字形的功能

### Lane `specimens` → `font-src/specimens/**`

- `font-src/specimens/render_specimens.py`：从已构建字体生成样张
- 单色黑白样张：48 / 96 / 192 px（docs/04 §4）
- 效果组样张：红字黑底、黄字红边（**仅样张层**，不得写进字体轮廓）
- 样张内容至少覆盖：单字 12 个汉字、双字（龍城/夜行/風暴）、四字（英雄本色/旺角風雲/霓虹之夜/黑夜追擊）、
  英文（CITY OF SHADOWS / LAST BULLET / 1997 / HONG KONG）
- PNG 入库 `font-src/specimens/`；样张脚本必须参数化（字号、文字、配色）

---

## 6. 命令（每个 lane 都要在自己 worktree 里跑通）

```powershell
# 1) 生成自己的 UFO
python font-src/src/hkposter-<lane>.py

# 2) recipe ↔ UFO 同步
python font-src/scripts/check_recipes.py --recipes font-src/src/hkposter-<lane>.py

# 3) 字形 UT
python font-src/scripts/check_glyphs.py --sources font-src/masters/<你的>.ufo

# 4) 构建（只构建自己的 master，避免别人未完成的字形干扰）
python font-src/scripts/build_font.py --sources font-src/masters/<你的>.ufo --out font-src/dist

# 5) 成品 IT/ST
python font-src/scripts/verify_font.py --font font-src/dist/HKPoster-Heavy.ttf --sources font-src/masters/<你的>.ufo

# 6) 渲染样张并**自己看一眼**
python font-src/scripts/render_glyph_sheet.py --font font-src/dist/HKPoster-Heavy.ttf --text "<你的字符>" --size 200 --out font-src/reports/sheet-<lane>.png
```

依赖：`pip install -r requirements.txt`（已在开发机装好；**不要**动系统 Python 环境）。

---

## 7. 验收标准（逐 lane）

每个 lane 必须同时满足：

1. **不越界**：本 lane 只修改 §1 中属于它的路径；`git status` 里不得出现其他 lane 的文件。
2. **可构建**：第 6 节 1–5 步全部退出码 0。
3. **无 .notdef**：成品字体渲染自己的字符时不出现兜底字形。
4. **家族一致性**：`check_glyphs.py` 的 WARN 不得新增（墨量率离同类中位数 > 35% 会报 WARN）。
5. **目视自检**：必须自己看过第 6 节第 6 步的 PNG，确认字形可辨认、没有粘连、没有空洞。
6. **提交**：一个逻辑提交，commit message 说明 lane 名与交付内容。
7. **报告**：交付报告必须包含**实际粘贴的命令输出**（不是描述"应该通过"）。

---

## 8. 风格规则速查（docs/02、docs/03）

| 规则 | 要求 |
|---|---|
| GLY-001 | 横竖笔画统一视觉重量；高频交叉与小空腔允许局部减重 |
| GLY-002 | 外角硬折为主；弧形轮廓需光学平滑 |
| GLY-003 | 装饰斜切只作用于不影响结构的位置；关键辨识笔画不得去除 |
| GLY-004 | 同部件保持家族相似性；偏旁在不同位置需光学校正 |
| GLY-005 | 字间紧凑但不得接触 |
| GLY-006 | 缩小后仍要维护负空间，小尺寸不得让内部白块消失 |

### 3.1 笔画角度不可改（项目所有者 2026-10-25）

> 「你可以改变笔画的设计，但不要改变笔画的角度」

| | 内容 | 判定 |
|---|---|---|
| **不可改** | 任何一条笔画的**方向/角度**：水平、垂直、某个斜率。中心线的走向属于骨架 | 「它现在朝另一个方向了」→ 违规 |
| **可改** | 笔画的**设计**：重量档位、端点处理（方切/斜切）、转角（外角硬折/内角开孔）、记号形状的字面与粗细、落位与大小 | 「它现在更粗/更方/更硬」→ 允许 |

**斜切端点不算改角度**：斜切改的是端面切口，笔画走向没变
（汉字的 `g.dot(..., slant=26)` 就是这个用法）。

**典型违规（已发生过）**：把浊点从两枚**斜画**改成两枚**竖向斜切块** ——
形状确实更「统一」了，但浊点本来就该是斜的，改竖等于改了笔画角度，
也丢了参照字体的形态（参照的浊点包围盒是斜的：M PLUS 1p Black 383×270 / 1000 em）。
→ 已改回斜画；斜画仍用平切端面与细档重量，海报语言体现在端点与重量上。

**这条对所有 lane 生效**：包括 Jōyō 的每一批新字形 ——
新字形是「照标准骨架画」，不是「把角度改成更好看的方向」。

风格语义（docs/02 §2）：**厚重、紧凑、动势、戏剧性、手工感、港片时代感**；
偏差 A（过于普通黑体）、B（过分书法化）、C（靠特效港风化）、D（过多斜切碎裂）均为失败。

必须避免：

- 霓虹/描边/金属/旧化纹理进入**字体轮廓**（那是样张层的事）
- 逐字机械挤压或倾斜
- 高密字（龍義警愛無）变成黑块

---

## 9. 证据纪律

- **没跑过 = 没通过。** 不允许在报告里写"应该通过""预计通过"。
- 不允许把 `NOT_RUN` 的测试写成 `PASS`（docs/07 §2）。
- 不允许声称"字体已编译""已安装"而没有对应的构建产物与检查输出。
- 样张里调用了系统回退字体的字符，必须在样张上标注（docs/06 §4）。
- 设计评审要写**具体修改记录**，不是"更港风""更好看"（docs/01 §5）。

---

## 10. 提交与集成

- 分支：`agent/<set>/<lane-id>`；worktree 与分支一一对应，一 lane 一可写工作区。
- 只提交本 lane 拥有的路径；不要 `git add -A`。
- 集成方在合并前会独立重跑 §6 的命令，**以实际输出为准**，不接受子代理的口头结论。
- 合并顺序：构建链 → 字形 lane → 特性/测试 → 样张；每次合并后重跑全链路自证。

## 11. 产物与证据的存放位置

| 内容 | 位置 | 是否入库 |
|---|---|---|
| 设计源（recipe）、UFO master、特性、测试、样张 PNG | `font-src/src`、`masters`、`features`、`tests`、`specimens` | **入库** |
| 构建产物 TTF/OTF/WOFF2 | `font-src/dist/` | 不入库（可由上面全部内容重建） |
| 机器报告（build.json / verify.json / tests.json / 渲染证据 PNG） | `font-src/reports/` | **不入库**（每次运行覆盖，路径在文档中作为「在哪里跑出来的」指引） |

因此文档里出现的 `font-src/reports/...` 是**本地运行后产生的证据路径**，
克隆仓库时需要按第 6 节命令自己跑一遍才能得到；`docs/10_Wave0试制记录.md` 里已摘录关键数值。

## 12. 变更记录

| 版本 | 变更 | 原因 |
|---|---|---|
| v1.0 | 初始契约（单套笔画权重 96/92/84，latin-core 含标点） | — |
| v1.1 | 笔画权重分 CJK / Latin 两档；标点拆出独立 `latin-punct` lane | Wave 0 样张实测：Latin 用 96 只读作 Regular（docs/09 RV-14）；标点 26 个字形单拆可降低单 lane 负载与中断风险 |
| v1.2 | 新增多文种：CJK / Latin / 简体 / 假名 四档权重；Jōyō 批次化生产；vert 特性 | 用户纳入 zh-CN 与 ja-JP（2026-10-25） |

## 13. Wave 1 多文种 lane（2026-10-25 起）

多文种的**码位策略**（决定了要不要 `locl`）：

| 文种 | 策略 | 说明 |
|---|---|---|
| zh-HK 繁体 | 独立 master | 现有 12 字 + 后续繁体批次 |
| zh-CN 简体 | 独立 master（**独立码位**） | 龙 U+9F99 / 义 U+4E49 / 爱 U+7231 / 无 U+65E0 / 风 U+98CE 等与繁体不同码位，**共用码位的问题不存在**，无需 `locl`；简繁同形字（港影警道城火夜）直接共用现有 master |
| ja 假名 | 独立 master | 平假名 77 + 片假名 73 |
| ja 漢字 | 独立 master（Jōyō 2136） | Jōyō 集合自带日文形（画 U+753B、竜 U+7ADC…），与繁体形同码位冲突的是 P2 的 JIS-vs-GB 变体，届时才启用 `locl` |
| vert 竖排 | 独立 master + `vert` 特性 | 替代字形命名 `<基础名>.vert`（生产名已实测原样保留） |

**四档笔画权重**（见 `font-src/data/design-params.json` 的 `weights`）：

| 类别 | 主 | 次 | 斜/细 | 点 | 理由 |
|---|---:|---:|---:|---:|---|
| CJK 繁体 | 96 | 92 | 84 | 84 | 基准 |
| CJK 简体 | 108 | 100 | 92 | 92 | 笔画少 → 需上调约 12% 才能与繁体等黑 |
| Latin | 132 | 120 | 112 | 104 | 640 advance 里 96 只读作 Regular |
| 假名 | 92 | 84 | 76 | 84 | 笔画少、曲线笔多 |

**Jōyō 2136 字的批次化生产**：

- 数据源：Project X0213（依据 2010 年文化厅《常用漢字表》修订版）+ Kanjidic2（笔画/学级/频率）
- 落库：`font-src/data/joyo-kanji.json`（2136 字 + Unicode）、`joyo-kanji-meta.json`（笔画/学级/频率）
- 分批：`font-src/scripts/plan_joyo_batches.py` → `font-src/data/joyo-batches.json`
  （按笔画密度分 5 档：1–5 / 6–9 / 10–13 / 14–17 / 18+，档内按频率排名优先；
  共 **93 条 lane**：s1 6 条 / s2 21 / s3 34 / s4 23 / s5 9）
- 提示词生成：`font-src/scripts/lane_prompt.py --batch <id>` —— 规格固化，后续会话可机械续做
- 每条 lane = 一个 recipe + 一个 UFO master，文件所有权天然互斥

**lane 清单（Wave 1）**：

| Lane | 拥有路径 | 产出 |
|---|---|---|
| `kana-hira` | `font-src/src/hkposter-kana-hira.py` + `masters/hkposter-kana-hira.ufo/` | 平假名 77 |
| `kana-kata` | `font-src/src/hkposter-kana-kata.py` + `masters/hkposter-kana-kata.ufo/` | 片假名 73 |
| `cn-simplified` | `font-src/src/hkposter-cn.py` + `masters/hkposter-cn.ufo/` | 简体 8 |
| `joyo-<class>-<n>` | `font-src/src/hkposter-joyo-*.py` + `masters/hkposter-joyo-*.ufo/` | Jōyō 批次 |
| `vert-punct` | `font-src/src/hkposter-vert-punct.py` + `masters/hkposter-vert-punct.ufo/` + `features/vert.fea` + `tests/test_vert.py` | 竖排替代形 + vert 特性 |

**子集构建与特性文件的关系（已修）**：`build_font.py --sources <子集>` 只编译**引用的字形都存在**的特性文件，
不适用则跳过并打印说明；全量构建遇到不适用的特性文件直接报错（防止特性被静默丢掉）。
