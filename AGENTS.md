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

## 常用命令

```powershell
pip install -r requirements.txt

python font-src/scripts/verify_all.py      # 一条命令跑完全链路：recipe 同步 → 字形 UT → 构建 → IT/ST → 样张 → 测试套件
python font-src/scripts/selftest.py        # 垂直切片自证（参考 master）
python font-src/scripts/build_font.py --out font-src/dist  # 构建 TTF/OTF/WOFF2
python font-src/scripts/check_glyphs.py     # 字形 UT
python font-src/scripts/check_recipes.py    # recipe ↔ UFO 同步
python font-src/scripts/verify_font.py      # 成品 IT/ST（含 Windows GDI 真实加载）
python font-src/tests/run_tests.py         # UT + IT + ST 全套
python font-src/specimens/render_specimens.py --all        # 重生成样张
```

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
