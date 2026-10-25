你是 HK Poster Heavy 字体工程的并行制作 lane，负责 **Jōyō 常用漢字批量试制：joyo-w2-s1-002**。

【重要：零读文件模式 + 事实已内联】
本项目上一轮有多个子代理会话被运行时中断，零产出。本提示词已内联全部事实。
**你的第一个工具调用必须是 `write`**，一次性写出完整文件；不要先读仓库文件。
**不要读 font-src/scripts/ 下的任何脚本，也不要读别的批次的 recipe**
（例如 `font-src/src/hkposter-joyo-s1-00X.py` 属于**其他批次**，不要读、不要改）——
笔画 API、判定阈值、提交方式都已在下面写全；读文件既浪费预算，又容易撞上连接中断。
若写文件时遇连接中断，**重试 write**（整体覆盖），不要放弃。

【文件名与路径一律以本规格为准】
下面写的 `hkposter-joyo-w2-s1-002.py` 与 `hkposter-joyo-w2-s1-002.ufo` 是**唯一正确**的文件名（由批次 id `joyo-w2-s1-002` 推导）。
不要凭记忆或按"上一批"的命名习惯改写——历史上曾因派单里写错文件名，
差点覆盖已交付批次的 recipe 与 master。**如果你在仓库里看到名字相近但不同的文件，
那是别的批次的，一律不要碰。**

【工作目录 —— 唯一允许写入的地方】
E:/hkposter-lanes/wave2-joyo-s1-002
命令先切过去：`Set-Location 'E:/hkposter-lanes/wave2-joyo-s1-002'`
不要在 E:/HKPoster 里写任何文件。
（若你收到的工作目录与这一行不一致，**以本规格这一行为准**；
 历史上派单文本里曾把 wave 前缀写错成 wave1，导致你在不存在的目录里找文件。）

【你唯一允许写入的路径】
- font-src/src/hkposter-joyo-w2-s1-002.py
- font-src/masters/hkposter-joyo-w2-s1-002.ufo/（由 recipe 生成）

【冻结参数（日本語漢字）】
UPM 1000；y 向上，基线 y=0；ascender 880 / descender -120。
**advance = 1000**；字面框 **x 60..940，y 0..820**（与繁体汉字完全一致，便于中英日混排）。
漢字笔画权重档：**主 96 / 次 92 / 细 84 / 点 84–96**（与 zh-HK 繁体同一档）。

【海报端点 —— 港产海报的签名，别丢】

本字体的「手」来自两件武器，**每个字都要用上**：

```python
g.hbar(x1, x2, y, weight=96)              # 横 = 硬边矩形（两端平切）
g.vbar(x, y1, y2, weight=96)              # 竖 = 硬边矩形
g.diag(x1, y1, x2, y2, weight=96)         # 撇捺 = 斜切边矩形
g.dot(cx, cy, w=94, h=126, slant=26)      # 点/短撇 = 斜切平行四边形  ← 签名
```

* **横竖撇捺用平切硬边**（不是圆头、不是渐变收笔）。
* **点与短撇用斜切平行四边形**，`slant` 是**分档**的：主档 26，
  另有 20 / 18 / 16 / 14 / −14（见 `font-src/src/hkposter-cjk-core.py`）。
  同类部件在同一字族里用同一档（GLY-004）。
* **斜切只许用在点/短撇/记号这类不影响结构的位置**（GLY-003）；
  主笔的识别笔画不许随意斜切。
* **笔画的角度不可改**（项目所有者 2026-10-25）：
  「你可以改变笔画的设计，但不要改变笔画的角度」。
  - **不可改**：任何一条笔画的**方向/角度**（水平 / 垂直 / 某个斜率）——
    中心线的走向属于骨架。新字形是「照标准骨架画」，不是「把角度改成更好看的方向」。
  - **可改**：笔画的**设计** —— 重量档位、端点处理（方切/斜切）、
    转角（外角硬折 / 内角开孔）、记号形状的字面与粗细、落位与大小。
  - **斜切端点不算改角度**：斜切改的是端面切口，笔画走向没变。
* 禁止逐字机械挤压或倾斜（docs/02 偏差 D、docs/03 §1）。

【hkbuild 笔画 API（脚本已存在，import 即可，不要打开它）】
```python
from hkbuild import Glyph, write_ufo, ellipse_points

g = Glyph(name, advance=1000, unicode=0x5E72, note="说明")
g.hbar(x1, x2, y, weight=96)        # 水平：中心线 y，横跨 x1..x2，墨迹占 y±weight/2
g.vbar(x, y1, y2, weight=96)        # 垂直：中心线 x，跨 y1..y2（端点即墨迹端点）
g.diag(x1, y1, x2, y2, weight=96)    # 斜笔画：中心线两端点，厚度垂直于中心线
g.dot(cx, cy, w=96, h=112, slant=0)  # 点/短撇：平行四边形
g.rect(x1, x2, y1, y2); g.poly([(x, y), ...])   # 原始几何
g.ring(outer_pts, inner_pts)         # 环形带（等长点列），内白自动成洞
```
每条笔画 = "中心线 + 垂直权重"；所有笔画**自动求并集**，轮廓不自交/不重叠，内白自动成洞。
**注意对齐语义**：横画要让墨迹上缘对齐 820 / 下缘对齐 0，中心线必须内缩半个笔画宽
（参考 `font-src/src/hkposter-latin.py` 里的 bar_top / bar_base / diag_cap_base 辅助函数；
本 lane 直接照同样的办法写自己的对齐辅助函数）。

【recipe 文件骨架（照抄，只改 build() 与各字函数）】
```python
"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s1-002。

本批 40 字，笔画范围 1–5，取自 2010 年文化厅《常用漢字表》。

（在这里写整体设计取舍：字面框、权重、与同批次密度的协调）
"""

from __future__ import annotations

import sys
from pathlib import Path

FONT_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FONT_SRC / "scripts"))

from hkbuild import Glyph, write_ufo  # noqa: E402

W_MAIN = 96
W_SEC = 92
W_THIN = 84
W_DOT = 84


def build() -> list[Glyph]:
    return [ ... ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s1-002.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
```

【你的字符清单（40 个，冻结，不得增删、不得改 Unicode）】
字形名一律 `uniXXXX`（大写十六进制）。
- 干  U+5E72  uni5E72  3 画  (频率排名 1349)
- 穴  U+7A74  uni7A74  5 画  (频率排名 1366)
- 丈  U+4E08  uni4E08  3 画  (频率排名 1375)
- 匹  U+5339  uni5339  4 画  (频率排名 1384)
- 丹  U+4E39  uni4E39  4 画  (频率排名 1402)
- 丘  U+4E18  uni4E18  5 画  (频率排名 1405)
- 玄  U+7384  uni7384  5 画  (频率排名 1409)
- 氷  U+6C37  uni6C37  5 画  (频率排名 1450)
- 才  U+624D  uni624D  3 画  (频率排名 1497)
- 巧  U+5DE7  uni5DE7  5 画  (频率排名 1537)
- 矛  U+77DB  uni77DB  5 画  (频率排名 1538)
- 召  U+53EC  uni53EC  5 画  (频率排名 1540)
- 幻  U+5E7B  uni5E7B  4 画  (频率排名 1564)
- 乏  U+4E4F  uni4E4F  3 画  (频率排名 1646)
- 寸  U+5BF8  uni5BF8  3 画  (频率排名 1669)
- 凶  U+51F6  uni51F6  4 画  (频率排名 1673)
- 尻  U+5C3B  uni5C3B  5 画  (频率排名 1692)
- 凡  U+51E1  uni51E1  3 画  (频率排名 1730)
- 刈  U+5208  uni5208  4 画  (频率排名 1738)
- 刃  U+5203  uni5203  3 画  (频率排名 1763)
- 冗  U+5197  uni5197  4 画  (频率排名 1782)
- 刀  U+5200  uni5200  2 画  (频率排名 1794)
- 弓  U+5F13  uni5F13  3 画  (频率排名 1802)
- 皿  U+76BF  uni76BF  5 画  (频率排名 1812)
- 弔  U+5F14  uni5F14  4 画  (频率排名 1840)
- 乙  U+4E59  uni4E59  1 画  (频率排名 1841)
- 汁  U+6C41  uni6C41  5 画  (频率排名 1843)
- 尼  U+5C3C  uni5C3C  5 画  (频率排名 1844)
- 瓦  U+74E6  uni74E6  5 画  (频率排名 1850)
- 又  U+53C8  uni53C8  2 画  (频率排名 1874)
- 斗  U+6597  uni6597  4 画  (频率排名 1885)
- 迅  U+8FC5  uni8FC5  5 画  (频率排名 1888)
- 奴  U+5974  uni5974  5 画  (频率排名 1932)
- 尺  U+5C3A  uni5C3A  4 画  (频率排名 1940)
- 屯  U+5C6F  uni5C6F  4 画  (频率排名 1980)
- 爪  U+722A  uni722A  4 画  (频率排名 2025)
- 孔  U+5B54  uni5B54  4 画  (频率排名 2052)
- 牙  U+7259  uni7259  4 画  (频率排名 2067)
- 升  U+5347  uni5347  4 画  (频率排名 2077)
- 丼  U+4E3C  uni4E3C  5 画  (频率排名 2088)

【設計要点】
- 本批字形密度接近（1–5 画），**务必保持同族观感**：
  同一部件（如 亻、氵、扌、木）在批内要**复用同一套坐标与笔画拆法**，
  只做位置与大小的光学校正（docs/03 GLY-004）。
- 每个字先在 docstring 里写**笔画清单与部件分区坐标**，再逐笔画落坐标并注明所属部件。
- 笔画少的字要**加粗**（用 96），笔画多的字在拥挤处**局部减重**到 84，
  否则同批内会出现"有的太轻、有的太闷"（GLY-001 允许小空腔局部减重）。
- 密排处（横画叠横画）内白不低于 24 单位；竖与竖之间不低于 60 单位（GLY-006）。
- 禁止逐字机械挤压或倾斜（docs/02 偏差 D）。

【要跑的 6 条命令（全部在 lane worktree 下执行）】
```
python font-src/src/hkposter-joyo-w2-s1-002.py
python font-src/scripts/check_recipes.py --recipes font-src/src/hkposter-joyo-w2-s1-002.py
python font-src/scripts/check_glyphs.py --sources font-src/masters/hkposter-joyo-w2-s1-002.ufo
python font-src/scripts/build_font.py --sources font-src/masters/hkposter-joyo-w2-s1-002.ufo --out font-src/dist
python font-src/scripts/verify_font.py --font font-src/dist/HKPoster-Heavy.ttf --sources font-src/masters/hkposter-joyo-w2-s1-002.ufo
python font-src/scripts/render_glyph_sheet.py --font font-src/dist/HKPoster-Heavy.ttf --text "干穴丈匹丹丘玄氷才巧矛召" --size 200 --out font-src/reports/sheet-joyo-w2-s1-002.png
```
判定：check_recipes PASS（问题 0）；check_glyphs FAIL=0；verify_font FAIL=0。
**若第 4 条因特性文件报错**：说明 `font-src/features/*.fea` 引用了本批没有的字形——
子集构建会自动跳过不适用的特性文件，若仍失败请把报错原文写进报告交集成方。

【交付步骤】
1. write 一次性写出完整文件（40 个字形全写完，不要分次追加）。
2. 跑上面 6 条命令。
3. **用 read 工具打开 font-src/reports/sheet-joyo-w2-s1-002.png 亲眼看**（不能省）：
   逐字判断：一眼认得出吗？有没有粘连成黑块？内白还在吗？批内观感一致吗？
   不满意就改 recipe → 重新生成 → 重新渲染 → 再看（最多 4 轮）。
4. 提交：
```
git add font-src/src/hkposter-joyo-w2-s1-002.py font-src/masters/hkposter-joyo-w2-s1-002.ufo
git commit -m "wave2/joyo-w2-s1-002: Jōyō 常用漢字 40 字"
```
提交所在分支：**agent/wave2/joyo-s1-002**（已 checkout，不要新建分支、不要 rebase、不要 merge）。
font-src/dist 与 font-src/reports 被 .gitignore 忽略，不要 add。

【禁止】
- 改 font-src/scripts/ 或任何 base 文件
- git add -A / git push / 改 git 历史 / rebase
- 写 lane 之外的任何文件（包括 E:/HKPoster）
- 声称"应该通过"——报告里粘贴真实命令输出

【交付报告格式（最后一条消息）】
Task / Owner / Branch / Worktree / Base branch+SHA / Current HEAD / Commits / Files changed /
Validation commands + 真实输出 / 逐字设计决定与理由（笔画清单 + 坐标 + 同批观感如何统一）/
目视自检结论 / 已知问题与风险 / Recommended integration: merge
