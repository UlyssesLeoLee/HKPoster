# FONT-HKP-TRL-001｜Wave 0 代表字形试制记录

- 对应需求：REQ-001、002、003、004、005、006、007、008、012
- 状态：**试制完成，参数已冻结；尚未达到发布基线**
- 基线分支：`dev`｜本记录对应源码状态：`dev@3861944`
- 证据入口：`font-src/reports/`（机器报告）、`font-src/specimens/`（样张）、`font-src/tests/`（可执行测试）

## 1. 本轮结论

Wave 0 的目标是 docs/09 §3 要求的「先完成代表字形并用单色样张冻结关键比例与端点系统」。
本轮的结果：

- **字形**：12 个代表汉字 + 26 个 Latin 大写 + 10 个数字 + 26 个标点 = **74 个设计字形**，
  加空格（U+0020）与 `.notdef`，成品字体共 **76 个字形**。
- **工程**：从零搭起可运行的字体工程——设计源（recipe）→ UFO master → ufo2ft → OTF/TTF/WOFF2，
  一次命令即可构建，并产出机器可读的证据报告。
- **测试**：UT / IT / ST 三套可执行检查，**28 PASS / 0 FAIL / 0 WARN / 1 SKIP**。
- **平台证据**：Windows GDI 真实加载成功，且**用「GDI 实测文本宽度 vs 字体自身 hmtx」证明没有被系统字体静默替换**。
- **冻结**：字面框、笔画权重分层、advance、cap 线与基线的对齐规则均已固化到代码与参数表。
- **未达发布基线**：4 个汉字（城、火、夜、風）仍有可辨认性缺陷；macOS / 浏览器 / Web 平台未测；
  **许可证仍为 `UNDECIDED`，发布门禁继续阻断**。

**本记录不是字体发行说明，也不构成商用授权。**

## 2. 冻结参数

来源：`font-src/data/design-params.json`（唯一权威）

| 参数 | 值 | 说明 |
|---|---|---|
| UPM | 1000 | — |
| ascender / descender | 880 / -120 | hhea、OS/2 typo 均取此值 |
| CJK advance | 1000 | 全角方格 |
| Latin 大写 / 数字 advance | 640 | 标题排版的字面节奏 |
| 空格 advance | 500 | U+0020 |
| CJK 字面框 | x 60..940，y 0..820 | 顶线 820 |
| Latin 大写顶线 / 基线 | y 700 / 0 | 与 CJK 各自成立 |
| 笔画权重（CJK） | 主 96 / 次 92 / 细 84 / 点 84–96 | — |
| 笔画权重（Latin） | 主 132 / 次 120 / 斜 112 / 细 104 | **比 CJK 更粗**，见 §6 RV-14 |

## 3. 制作链路

```text
recipe（Python，笔画原语，设计源）
  └─ hkbuild：笔画求并集（shapely）→ 无自交、无重叠，内白自动成洞
      └─ UFO master（.ufo，生成物，含 fontinfo / glyphs）
          └─ build_font.py：合成多 master → ufo2ft → TTF / OTF / WOFF2
              └─ font-src/reports/build.json（命令、版本、源提交、哈希、表清单）
```

约定：

- **recipe 是设计源，`.ufo` 是生成物**。改形状必须改 recipe 再重新生成；
  `font-src/scripts/check_recipes.py` 会逐字形、逐属性比对两者是否同步。
- 笔画语义是「中心线 + 垂直权重」。因此横画与斜画必须内缩半个笔画宽，
  才能让墨迹极值对齐到 cap 线与基线——已固化为 `bar_top` / `bar_base` / `diag_cap_base` 等辅助函数。
- 轮廓并集在**源阶段**完成（shapely），因为 CPython 3.13 没有 `skia-pathops` 轮子，
  ufo2ft 的 `removeOverlaps` 不可用。
- 构建按 `SOURCE_DATE_EPOCH = HEAD 提交时间` 定版，**同一源码的两次构建产出完全一致的二进制**，
  哈希才能作为产物身份凭证（docs/05 §6）。

## 4. 字符清单与制作状态

| 组 | 字符 | 数量 | 来源 lane | 状态 |
|---|---|---|---|---|
| 汉字（core） | 港 影 城 火 夜 風 | 6 | cjk-core | 港/影 通过；城/火/夜/風 需再改 |
| 汉字（dense） | 龍 義 警 愛 無 道 | 6 | cjk-dense | 全部通过 |
| Latin 大写 | A–Z | 26 | latin-core | 全部通过 |
| 数字 | 0–9 | 10 | latin-core | 全部通过 |
| 标点 | 全角 13 + 半角 13 | 26 | latin-punct | 全部通过 |
| 空格 | U+0020 | 1 | 构建链 | 通过 |

逐字符状态与证据见 `tables/字符集与测试计划.xlsx` 的「字符规划」工作表
（`制作状态` / `验证状态` / `备注` 三列已回写）。

## 5. 证据

### 5.1 构建产物（`dev@3861944`）

| 格式 | 字节 | sha256（前 24 位） | 字形数 | 表数 |
|---|---:|---|---:|---:|
| HKPoster-Heavy.ttf | 9452 | `54db4aeed23be96e2430e0a2` | 76 | 12 |
| HKPoster-Heavy.otf | 7352 | `9b848eddc0f76412c104d9b4` | 76 | 11 |
| HKPoster-Heavy.woff2 | 4912 | `305de00cc64a416070e171e6` | 76 | 12 |

完整哈希与命令见 `font-src/reports/build.json`（每次构建覆盖，产物目录 `font-src/dist/` 不入库）。

### 5.2 测试（`font-src/tests/run_tests.py`）

| 套件 | 内容 | 结果 |
|---|---|---|
| UT | 字形度量与几何：advance、cap 顶线、空字形、轮廓自交、越界、重复 Unicode、密度离群 | PASS |
| IT | 必需表、name/OS-2 度量、cmap 覆盖、uharfbuzz 真实排版不出现 .notdef、kerning 生效断言 | PASS |
| ST | Windows GDI 真实加载 + 替换检测 + GetDIBits 光栅化出墨 | PASS |

合计 **28 PASS / 0 FAIL / 0 WARN / 1 SKIP**。
SKIP 为「字体尚无小写字母，`HK Poster Heavy` / `CITY OF SHADOWS` 两串无法排版」——据实标注，不计为通过。

### 5.3 平台证据

- Windows GDI：`AddFontResourceExW(FR_PRIVATE)` 注册成功；`CreateFontW` 建面后，
  GDI 实测文本宽度 **122px**，与字体自身 hmtx 推算的 **122.0px** 一致 → 未被系统字体替换。
  （`CreateFontW` 必须传满 14 个参数，否则 `lfFaceName` 错位会导致静默替换。）
- 光栅化证据：`font-src/reports/st-platform-render.png`。
- macOS / Linux / 浏览器：**NOT_RUN**（环境不可用，不得声称通过）。

### 5.4 样张

`font-src/specimens/` 下 6 张：48 / 96 / 192 px 黑白单色、红字黑底、黄字红边效果组、英文标题组。
生成器 `render_specimens.py` 完全参数化（字体、文字、字号、配色、列数、字距）。

样张中**当前字体没有的字符以洋红 + 虚线下划线标出**，并注明「显示为系统回退字体（非本字体字形）」
（docs/06 §4 缺字策略）。效果组样张只存在于样张层，字体轮廓内没有任何描边、霓虹或旧化处理。

## 6. 本轮发现的问题（已并入 docs/09 的 RV-09..RV-14）

| 编号 | 摘要 | 处理 |
|---|---|---|
| RV-09 | fontTools 的 RIBBI 命名规则使 "Heavy" 样式名的族名/样式名错位 | 已修：用排版名 nameID 16/17 表达真实族名与样式名 |
| RV-10 | 墨量率一致性检查对圆字母与结构密度差异敏感 | 已记为工具口径限制：只能作人工复核信号；硬门禁是 cap 顶线离散 ≤ 24 |
| RV-11 | 笔画是「中心线 + 权重」，横画斜画必须内缩半个笔画宽才能对齐 cap/基线 | 已固化为对齐辅助函数 |
| RV-12 | recipe ↔ UFO 比对未归一化行尾，`core.autocrlf` 下误报不同步 | 已修：比较前归一化 CRLF |
| RV-13 | 部分并行 lane 的子代理会话被运行时中断（网络重置 / 会话回收 / 回合空转） | 流程有效：lane 登记 → worktree → rebase → merge → 独立复验；中断的 lane 由集成方在同一 worktree/分支补交 |
| RV-14 | Latin 与 CJK 共用同一套笔画权重常量，导致 Latin 读作 Regular | 已修：Latin 权重整体上调一档并回算路径极值 |

另有两个**产品缺陷**在本轮修复：空格未映射 U+0020（渲染成 .notdef 黑块）、构建产物含时间戳导致哈希每次都变。

## 7. 未解决项（下一轮 backlog）

1. **汉字 core 组的 4 个字需再改**（见 cjk-core 提交说明）：城的成部横折钩与斜钩偏近、
   火的右上短撇与长撇相接、夜的夂部横撇与捺偏近、風的内部虫部偏挤。
2. **Latin 小写缺失**：当前只有大写与数字，`HK Poster Heavy` / `CITY OF SHADOWS` 无法完整排版。
3. **简体衍生与地区变体未开始**：`locl` / `palt` / `halt` 仅有预留注释。
4. **平台覆盖不足**：macOS、Linux、浏览器 WOFF2 均 NOT_RUN。
5. **许可与商标**：许可证仍 `UNDECIDED`；家族名「HK Poster / 港映重黑」发布前须做商标相似性检查。
6. **500 / 1500 字扩展未开始**：仍为规划估算，不是已制作数量。

## 8. 复现方式

```powershell
pip install -r requirements.txt
python font-src/scripts/selftest.py          # 垂直切片自证
python font-src/scripts/build_font.py --out font-src/dist
python font-src/scripts/check_recipes.py     # recipe ↔ UFO 同步
python font-src/scripts/check_glyphs.py      # 字形 UT
python font-src/tests/run_tests.py           # UT + IT + ST 全套
python font-src/specimens/render_specimens.py --all
```

## 9. 审阅结论

- Wave 0 的**工程链路**已验证可用且可复现，可以支撑下一轮批量制作；
- Wave 0 的**字形**达到「可辨认、无黑块、无粘连」的基本线，但 4 个汉字尚未达到可交付标准；
- 按 docs/09 §3 的门禁，**本轮不构成批量绘制的前置条件已完全达成**——
  比例与端点系统已冻结，剩余问题已逐条定位到具体字形与具体部件。
- 发布门禁（G4）**未通过**，原因见 §7 第 5 条。
