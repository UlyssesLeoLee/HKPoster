# AGENTS.md — HK Poster Heavy 仓库工作约定

**仓库**：HK Poster Heavy / 港映重黑（暂定名）—— 香港电影海报风格粗体字体工程
**分支模型**：`dev` 是集成分支；每个制作任务一条 `agent/<set>/<lane-id>` 分支 + 一个独立 worktree。
**当前阶段**：Wave 0 代表字形试制已完成（见 `docs/10_Wave0试制记录.md`）；下一轮是 P1 标题高频字。

## 先读什么

1. `font-src/CONTRACT.md` —— **并行制作契约**：冻结参数、笔画 API、recipe 契约、
   各 lane 的字符清单与验收标准。动手前必读。
2. `docs/01`–`docs/09` —— 设计基线（视觉、结构、排版、工程、测试、发布）。
3. `docs/10_Wave0试制记录.md` —— 上一轮实际做到了什么、证据在哪、还差什么。
4. `00_完整设计文档.md` —— 一体化总览。

## 铁律

1. **证据 beats 声明**：没跑过的命令不算通过；报告里粘贴真实输出，不写"应该通过"。
   测试未执行就保持 `NOT_RUN`，不得标 `PASS`。
2. **不越界**：只修改分配给你的路径（契约 §1 的所有权表）。看到别处的问题，
   写进报告交给集成方，不要自己改。
3. **生成物不是设计源**：`.ufo` 由 `font-src/src/*.py` 生成。改形状改 recipe 再重新生成，
   `check_recipes.py` 会逐文件比对。
4. **字体本体与海报特效分离**：霓虹、描边、金属、旧化纹理只允许出现在样张层，
   不得写进字形轮廓。
5. **不编造**：字符状态、测试状态、许可证状态一律按实际写。
   许可证当前是 `UNDECIDED`，发布门禁阻断（docs/08、docs/09）。
6. **改 `.ufo` 之前先改 recipe**；直接改 `.ufo` 会在 `check_recipes.py` 里暴露为不同步。
7. **「笔画粘连」用数字判，不靠眼估**：跑 `check_stroke_gaps.py` 看重叠等效长度
   （单位=几个笔画宽；<1.5 正常交叠 · 1.5~3 偏紧 · >3 疑似粘连）。
   手工估余隙极易算错 —— 斜笔（`g.diag`）的墨迹沿**垂直于中心线**展开，
   宽度 `w` 在 y 方向只覆盖 `w/2 × |ux|`，按水平笔画那样用 ±w/2 估会差几十单位。
   本轮实测：目视「看着还行」的字里藏着 3 个真 bug（更的日三横压在一起、
   尾的毛上横与尸中横同高、束的口贴住顶横），都是这个工具抓出来的。
8. **码位要交叉核对，不能只查自洽**：字表里的「字符 ↔ 码位」必须与**独立来源**
   对上，不能只验「记录里的字段与键互相吻合」—— 两者来自同一条记录时可能一起错。
   2026-10-26 的实际事故：`joyo-kanji-meta.json` 里「栄」那一行被以「枤」(U+6804)
   为键写入，`unicode` 字段也跟着写 U+6804 —— **自洽检查零不符**，但成品字体因此
   缺「栄」多「枤」。`check_charset.py` 用 glyph `note` 里的汉字（子代理写的字形自称）
   与 `unicode` 对撞，才抓到它。
9. **码位的独立证据源是「参照字体」**（2026-10-26 第二次栽在同一处）：
   Unicode 权威表里 **U+6804 = 栄、U+8368 = 荨** —— 上一轮把「栄」修到 U+8368
   是把字形搬到了「荨」的码位上，并把 `note` 也改成「荨」让自洽检查通过，
   结果自洽检查再也看不出问题，而**真正的「栄」在成品字体里缺失**。
   - **修码位不匹配时，只能改机器侧（unicode / 字形名 / UFO 文件名），
     绝不能改「意图侧」（字表的键、recipe 的 `note` 首字）去迁就机器字段**——
     改了意图，门禁就再也分不出对错。
   - 独立证据源用**参照字体**（免费商用开源的日语字体）：Jōyō 常用漢字在日语字体里
     全都存在，**参照字体里根本没有的码位，几乎一定是选错了字**。
     `check_codepoint_ref.py` 就是干这个的（`--selftest` 会注入真实错配自证分辨力）。
   - 任何「字符 ↔ 码位」的自洽检查都要再问一句：**这个码位在参照字体里存在吗？**

## 常用命令

```powershell
pip install -r requirements.txt

python font-src/scripts/verify_all.py      # 一条命令跑完全链路：recipe 同步 → 字形 UT → 构建 → IT/ST → 样张 → 测试套件 → 假名保真度
python font-src/scripts/selftest.py        # 垂直切片自证（参考 master）
python font-src/scripts/build_font.py --out font-src/dist  # 构建 TTF/OTF/WOFF2
python font-src/scripts/check_glyphs.py     # 字形 UT
python font-src/scripts/check_recipes.py    # recipe ↔ UFO 同步
python font-src/scripts/verify_font.py      # 成品 IT/ST（含 Windows GDI 真实加载）
python font-src/scripts/check_kana_fidelity.py            # 假名保真度：缺字=硬门禁，骨架 IoU=软信号
python font-src/scripts/check_kana_fidelity.py --selftest # 先自证该检查器本身的分辨力
python font-src/scripts/check_kana_size.py              # 假名字面尺寸验收（与汉字同档 + 平/片对称）
python font-src/scripts/check_stroke_angles.py          # 笔画角度与记号倾角（recipe 层 AST 检查）
python font-src/scripts/check_stroke_gaps.py            # 笔画粘连/间隙报告（重叠等效长度，单位=笔画宽）
python font-src/scripts/check_charset.py              # 字符↔码位↔冻结清单自洽（note 汉字 vs unicode）
python font-src/scripts/check_codepoint_ref.py        # 码位独立核对（参照字体当第三方证据源）
python font-src/scripts/check_codepoint_ref.py --selftest  # 先自证该门禁的分辨力
python font-src/scripts/check_encoding.py              # 字符损坏扫描（坏字符进 recipe 就是错字形）
python font-src/tests/run_tests.py         # UT + IT + ST 全套
python font-src/specimens/render_specimens.py --all        # 重生成样张
python font-src/scripts/sync_charset_table.py              # 把 master 里的真实字形回写进字符规划表
python font-src/scripts/plan_joyo_batches.py               # 生成 Jōyō 2136 字的批次计划（90 条 lane）
python font-src/scripts/lane_prompt.py --batch <id>        # 生成某批次的 lane 提示词（续做用）
python font-src/scripts/lane_prompt.py --list              # 列出全部 lane（分支 ↔ worktree ↔ 字数对照）
```

## 多文种与批量生产（Wave 1）

- 文种：zh-HK 繁体（主）/ zh-CN 简体 / ja 假名 / ja 漢字（Jōyō 2136）/ vert 竖排。
- 简、假名、Jōyō 多为**独立码位**，本轮不启用 `locl`（同码位地区异形留给 P2）。
- 笔画权重**分四档**：繁体 96/92/84、简体 108/100/92、Latin 132/120/112、假名 92/84/76。
  同一数值在不同字面宽度里的视觉重量不同，**新增 master 必须按所属类别取对应档位**。
- Jōyō 2136 字按笔画密度分 5 档切成 **90 条 lane**（见 `font-src/data/joyo-batches.json`），
  提示词由 `lane_prompt.py` 生成，续做时机械重复「登记 → 建 worktree → 派发 → 复验 → rebase → merge」。
- **批次 id ≠ 分支名 ≠ worktree 名**：例如 `joyo-w2-s3-001`（批次）→ `agent/wave2/joyo-s3-001`（分支）
  → `E:/hkposter-lanes/wave2-joyo-s3-001`（worktree）。三者由 batch id 推导，**不得手写**。
- **lane 名 ≠ recipe 文件名**：lane `kana-hira-rework` 拥有的是
  `font-src/src/hkposter-kana-hira.py`（文件名**不带** `-rework`）。
- **guard `plan` 之后必须 `guard list` 回读确认登记的路径**：路径拼错时 guard 不会报错，
  会照错登记，等于这条 lane 的文件**没有被任何 claim 保护**。
  PowerShell 里 `$arr[0]` 插进双引号字符串会被展开成整个数组（空格拼接），
  写路径时要用显式变量，不要用数组下标。
- **假名要求（项目所有者 2026-10-25）**：假名骨架必须保持标准形，只改笔画处理（粗手写体）；
  缺字是硬门禁（`check_kana_fidelity.py`）。判据见 `docs/11` §6.8。
- **笔画的角度不可改（项目所有者 2026-10-25）**：
  「你可以改变笔画的设计，但不要改变笔画的角度」。
  * **不可改**：任何一条笔画的**方向/角度**（水平/垂直/某个斜率）—— 中心线走向属于骨架。
  * **可改**：笔画的**设计** —— 重量档位、端点处理（方切/斜切）、转角（外角硬折/内角开孔）、
    记号形状的字面与粗细、落位与大小。
  * **斜切端点不算改角度**（斜切改的是端面切口，走向没变）。
  * 这条对 Jōyō 的每一批新字形同样生效：新字形是「照标准骨架画」，
    不是「把角度改成更好看的方向」。
- **参照字体必须免费商用、开源、无任何限制**（项目所有者 2026-10-25）：
  Yu Gothic / Meiryo / MS Gothic / UD Digi Kyokasho / BIZ UD / 华文琥珀 等**商用授权字体不得作参照**。
  当前参照：`E:/hkposter-refs/`（M PLUS 1p Black = 主参照，Noto Sans JP Black = 骨架交叉校核，
  均为 SIL OFL 1.1）。**只参考比例与骨架，不描轮廓。**
- **一条 lane 只能改自己的文件**：上一轮 kana-hira 的提交越界改了 kana-kata 的 recipe。
  跨 lane 改文件 = 交付无效。
- 规划与缺口见 `docs/11_多文种规划.md`。

## 环境注意

- CPython 3.13 **没有** `skia-pathops` 轮子 → ufo2ft 的 `removeOverlaps` 不可用，
  轮廓并集在源阶段由 `hkbuild`/shapely 完成（构建脚本已固定 `removeOverlaps=False`）。
- Windows GDI 的 `CreateFontW` 必须传满 14 个参数，否则 `lfFaceName` 错位，
  表现为 GDI 静默替换成系统字体。`verify_font.py` 用 **GDI 实测宽度 vs 字体 hmtx**
  来判定是否被替换。
- **CJK 与 Latin 的笔画权重分两档**（CJK 96/92/84，Latin 132/120/112/104）：
  同样 96 单位在 Latin 里只读作 Regular。新增 master 必须按所属类别取对应档位。
- 构建按 `SOURCE_DATE_EPOCH = HEAD 提交时间` 定版，**同一源码两次构建哈希一致**；
  改了源码哈希就会变，跨提交比较哈希没有意义。
- `font-src/reports/` 与 `font-src/dist/` **不入库**（本地生成）；证据数值以 `docs/10` 摘录为准。
