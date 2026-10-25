你是 HK Poster Heavy 字体工程的并行制作 lane，负责 **Jōyō 常用漢字批量试制：joyo-w2-s2-012**。

【重要：零读文件模式 + 事实已内联】
本项目上一轮有多个子代理会话被运行时中断，零产出。本提示词已内联全部事实。
**你的第一个工具调用必须是 `write`**，一次性写出完整文件；不要先读仓库文件。
**不要读 font-src/scripts/ 下的任何脚本，也不要读别的批次的 recipe**
（例如 `font-src/src/hkposter-joyo-s1-00X.py` 属于**其他批次**，不要读、不要改）——
笔画 API、判定阈值、提交方式都已在下面写全；读文件既浪费预算，又容易撞上连接中断。
若写文件时遇连接中断，**重试 write**（整体覆盖），不要放弃。

【文件名与路径一律以本规格为准】
下面写的 `hkposter-joyo-w2-s2-012.py` 与 `hkposter-joyo-w2-s2-012.ufo` 是**唯一正确**的文件名（由批次 id `joyo-w2-s2-012` 推导）。
不要凭记忆或按"上一批"的命名习惯改写——历史上曾因派单里写错文件名，
差点覆盖已交付批次的 recipe 与 master。**如果你在仓库里看到名字相近但不同的文件，
那是别的批次的，一律不要碰。**

【工作目录 —— 唯一允许写入的地方】
E:/hkposter-lanes/wave2-joyo-s2-012
命令先切过去：`Set-Location 'E:/hkposter-lanes/wave2-joyo-s2-012'`
不要在 E:/HKPoster 里写任何文件。
（若你收到的工作目录与这一行不一致，**以本规格这一行为准**；
 历史上派单文本里曾把 wave 前缀写错成 wave1，导致你在不存在的目录里找文件。）

【你唯一允许写入的路径】
- font-src/src/hkposter-joyo-w2-s2-012.py
- font-src/masters/hkposter-joyo-w2-s2-012.ufo/（由 recipe 生成）

【冻结参数（日本語漢字）】
UPM 1000；y 向上，基线 y=0；ascender 880 / descender -120。
**advance = 1000**；字面框 **x 60..940，y 0..820**（与繁体汉字完全一致，便于中英日混排）。
漢字笔画权重档：**主 96 / 次 92 / 细 84 / 点 84–96**（与 zh-HK 繁体同一档）。

【hkbuild 笔画 API（脚本已存在，import 即可，不要打开它）】
```python
from hkbuild import Glyph, write_ufo, ellipse_points

g = Glyph(name, advance=1000, unicode=0x8349, note="说明")
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
"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s2-012。

本批 32 字，笔画范围 6–9，取自 2010 年文化厅《常用漢字表》。

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
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s2-012.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
```

【你的字符清单（32 个，冻结，不得增删、不得改 Unicode）】
字形名一律 `uniXXXX`（大写十六进制）。
- 草  U+8349  uni8349  9 画  (频率排名 967)
- 災  U+707D  uni707D  7 画  (频率排名 976)
- 析  U+6790  uni6790  8 画  (频率排名 980)
- 肉  U+8089  uni8089  6 画  (频率排名 986)
- 挑  U+6311  uni6311  9 画  (频率排名 989)
- 律  U+5F8B  uni5F8B  9 画  (频率排名 992)
- 至  U+81F3  uni81F3  6 画  (频率排名 996)
- 宗  U+5B97  uni5B97  8 画  (频率排名 997)
- 促  U+4FC3  uni4FC3  9 画  (频率排名 998)
- 宙  U+5B99  uni5B99  8 画  (频率排名 1005)
- 俊  U+4FCA  uni4FCA  9 画  (频率排名 1007)
- 秒  U+79D2  uni79D2  9 画  (频率排名 1015)
- 侵  U+4FB5  uni4FB5  9 画  (频率排名 1025)
- 括  U+62EC  uni62EC  9 画  (频率排名 1026)
- 孝  U+5B5D  uni5B5D  7 画  (频率排名 1030)
- 刺  U+523A  uni523A  8 画  (频率排名 1031)
- 到  U+5230  uni5230  8 画  (频率排名 1032)
- 透  U+900F  uni900F  9 画  (频率排名 1035)
- 津  U+6D25  uni6D25  9 画  (频率排名 1036)
- 仮  U+4EEE  uni4EEE  6 画  (频率排名 1039)
- 是  U+662F  uni662F  9 画  (频率排名 1045)
- 芝  U+829D  uni829D  6 画  (频率排名 1052)
- 吸  U+5438  uni5438  6 画  (频率排名 1054)
- 典  U+5178  uni5178  8 画  (频率排名 1055)
- 扱  U+6271  uni6271  6 画  (频率排名 1057)
- 看  U+770B  uni770B  9 画  (频率排名 1060)
- 戒  U+6212  uni6212  7 画  (频率排名 1062)
- 祉  U+7949  uni7949  8 画  (频率排名 1063)
- 奏  U+594F  uni594F  9 画  (频率排名 1067)
- 快  U+5FEB  uni5FEB  7 画  (频率排名 1074)
- 免  U+514D  uni514D  8 画  (频率排名 1080)
- 泉  U+6CC9  uni6CC9  9 画  (频率排名 1086)

【設計要点】
- 本批字形密度接近（6–9 画），**务必保持同族观感**：
  同一部件（如 亻、氵、扌、木）在批内要**复用同一套坐标与笔画拆法**，
  只做位置与大小的光学校正（docs/03 GLY-004）。
- 每个字先在 docstring 里写**笔画清单与部件分区坐标**，再逐笔画落坐标并注明所属部件。
- 笔画少的字要**加粗**（用 96），笔画多的字在拥挤处**局部减重**到 84，
  否则同批内会出现"有的太轻、有的太闷"（GLY-001 允许小空腔局部减重）。
- 密排处（横画叠横画）内白不低于 24 单位；竖与竖之间不低于 60 单位（GLY-006）。
- 禁止逐字机械挤压或倾斜（docs/02 偏差 D）。

【要跑的 6 条命令（全部在 lane worktree 下执行）】
```
python font-src/src/hkposter-joyo-w2-s2-012.py
python font-src/scripts/check_recipes.py --recipes font-src/src/hkposter-joyo-w2-s2-012.py
python font-src/scripts/check_glyphs.py --sources font-src/masters/hkposter-joyo-w2-s2-012.ufo
python font-src/scripts/build_font.py --sources font-src/masters/hkposter-joyo-w2-s2-012.ufo --out font-src/dist
python font-src/scripts/verify_font.py --font font-src/dist/HKPoster-Heavy.ttf --sources font-src/masters/hkposter-joyo-w2-s2-012.ufo
python font-src/scripts/render_glyph_sheet.py --font font-src/dist/HKPoster-Heavy.ttf --text "草災析肉挑律至宗促宙俊秒" --size 200 --out font-src/reports/sheet-joyo-w2-s2-012.png
```
判定：check_recipes PASS（问题 0）；check_glyphs FAIL=0；verify_font FAIL=0。
**若第 4 条因特性文件报错**：说明 `font-src/features/*.fea` 引用了本批没有的字形——
子集构建会自动跳过不适用的特性文件，若仍失败请把报错原文写进报告交集成方。

【交付步骤】
1. write 一次性写出完整文件（32 个字形全写完，不要分次追加）。
2. 跑上面 6 条命令。
3. **用 read 工具打开 font-src/reports/sheet-joyo-w2-s2-012.png 亲眼看**（不能省）：
   逐字判断：一眼认得出吗？有没有粘连成黑块？内白还在吗？批内观感一致吗？
   不满意就改 recipe → 重新生成 → 重新渲染 → 再看（最多 4 轮）。
4. 提交：
```
git add font-src/src/hkposter-joyo-w2-s2-012.py font-src/masters/hkposter-joyo-w2-s2-012.ufo
git commit -m "wave2/joyo-w2-s2-012: Jōyō 常用漢字 32 字"
```
提交所在分支：**agent/wave2/joyo-s2-012**（已 checkout，不要新建分支、不要 rebase、不要 merge）。
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
