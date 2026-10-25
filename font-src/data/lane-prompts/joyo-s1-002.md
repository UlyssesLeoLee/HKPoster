你是 HK Poster Heavy 字体工程的并行制作 lane，负责 **Jōyō 常用漢字批量试制：joyo-s1-002**。

【重要：零读文件模式 + 事实已内联】
本项目上一轮有多个子代理会话被运行时中断，零产出。本提示词已内联全部事实。
**你的第一个工具调用必须是 `write`**，一次性写出完整文件；不要先读仓库文件。

【工作目录 —— 唯一允许写入的地方】
E:/hkposter-lanes/wave1-joyo-s1-002
命令先切过去：`Set-Location 'E:/hkposter-lanes/wave1-joyo-s1-002'`
不要在 E:/HKPoster 里写任何文件。

【你唯一允许写入的路径】
- font-src/src/hkposter-joyo-s1-002.py
- font-src/masters/hkposter-joyo-s1-002.ufo/（由 recipe 生成）

【冻结参数（日本語漢字）】
UPM 1000；y 向上，基线 y=0；ascender 880 / descender -120。
**advance = 1000**；字面框 **x 60..940，y 0..820**（与繁体汉字完全一致，便于中英日混排）。
漢字笔画权重档：**主 96 / 次 92 / 细 84 / 点 84–96**（与 zh-HK 繁体同一档）。

【hkbuild 笔画 API（脚本已存在，import 即可，不要打开它）】
```python
from hkbuild import Glyph, write_ufo, ellipse_points

g = Glyph(name, advance=1000, unicode=0x5C0F, note="说明")
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
"""HK Poster Heavy —— Jōyō 常用漢字 joyo-s1-002。

本批 40 字，笔画范围 2–5，取自 2010 年文化厅《常用漢字表》。

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
    return FONT_SRC / "masters" / "hkposter-joyo-s1-002.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
```

【你的字符清单（40 个，冻结，不得增删、不得改 Unicode）】
字形名一律 `uniXXXX`（大写十六进制）。
- 小  U+5C0F  uni5C0F  3 画  (频率排名 114)
- 七  U+4E03  uni4E03  2 画  (频率排名 115)
- 公  U+516C  uni516C  4 画  (频率排名 118)
- 以  U+4EE5  uni4EE5  5 画  (频率排名 126)
- 平  U+5E73  uni5E73  5 画  (频率排名 128)
- 加  U+52A0  uni52A0  5 画  (频率排名 130)
- 山  U+5C71  uni5C71  3 画  (频率排名 131)
- 世  U+4E16  uni4E16  5 画  (频率排名 135)
- 区  U+533A  uni533A  4 画  (频率排名 137)
- 正  U+6B63  uni6B63  5 画  (频率排名 143)
- 女  U+5973  uni5973  3 画  (频率排名 151)
- 北  U+5317  uni5317  5 画  (频率排名 153)
- 午  U+5348  uni5348  4 画  (频率排名 154)
- 心  U+5FC3  uni5FC3  4 画  (频率排名 157)
- 支  U+652F  uni652F  4 画  (频率排名 159)
- 予  U+4E88  uni4E88  4 画  (频率排名 180)
- 川  U+5DDD  uni5DDD  3 画  (频率排名 181)
- 文  U+6587  uni6587  4 画  (频率排名 190)
- 反  U+53CD  uni53CD  4 画  (频率排名 191)
- 元  U+5143  uni5143  4 画  (频率排名 192)
- 千  U+5343  uni5343  3 画  (频率排名 195)
- 引  U+5F15  uni5F15  4 画  (频率排名 218)
- 水  U+6C34  uni6C34  4 画  (频率排名 223)
- 半  U+534A  uni534A  5 画  (频率排名 224)
- 示  U+793A  uni793A  5 画  (频率排名 237)
- 打  U+6253  uni6253  5 画  (频率排名 239)
- 台  U+53F0  uni53F0  5 画  (频率排名 262)
- 広  U+5E83  uni5E83  5 画  (频率排名 263)
- 必  U+5FC5  uni5FC5  5 画  (频率排名 265)
- 口  U+53E3  uni53E3  3 画  (频率排名 284)
- 少  U+5C11  uni5C11  4 画  (频率排名 287)
- 工  U+5DE5  uni5DE5  3 画  (频率排名 299)
- 土  U+571F  uni571F  3 画  (频率排名 307)
- 与  U+4E0E  uni4E0E  3 画  (频率排名 308)
- 止  U+6B62  uni6B62  4 画  (频率排名 310)
- 可  U+53EF  uni53EF  5 画  (频率排名 314)
- 木  U+6728  uni6728  4 画  (频率排名 317)
- 付  U+4ED8  uni4ED8  5 画  (频率排名 322)
- 切  U+5207  uni5207  4 画  (频率排名 324)
- 由  U+7531  uni7531  5 画  (频率排名 325)

【設計要点】
- 本批字形密度接近（2–5 画），**务必保持同族观感**：
  同一部件（如 亻、氵、扌、木）在批内要**复用同一套坐标与笔画拆法**，
  只做位置与大小的光学校正（docs/03 GLY-004）。
- 每个字先在 docstring 里写**笔画清单与部件分区坐标**，再逐笔画落坐标并注明所属部件。
- 笔画少的字要**加粗**（用 96），笔画多的字在拥挤处**局部减重**到 84，
  否则同批内会出现"有的太轻、有的太闷"（GLY-001 允许小空腔局部减重）。
- 密排处（横画叠横画）内白不低于 24 单位；竖与竖之间不低于 60 单位（GLY-006）。
- 禁止逐字机械挤压或倾斜（docs/02 偏差 D）。

【要跑的 6 条命令（全部在 lane worktree 下执行）】
```
python font-src/src/hkposter-joyo-s1-002.py
python font-src/scripts/check_recipes.py --recipes font-src/src/hkposter-joyo-s1-002.py
python font-src/scripts/check_glyphs.py --sources font-src/masters/hkposter-joyo-s1-002.ufo
python font-src/scripts/build_font.py --sources font-src/masters/hkposter-joyo-s1-002.ufo --out font-src/dist
python font-src/scripts/verify_font.py --font font-src/dist/HKPoster-Heavy.ttf --sources font-src/masters/hkposter-joyo-s1-002.ufo
python font-src/scripts/render_glyph_sheet.py --font font-src/dist/HKPoster-Heavy.ttf --text "小七公以平加山世区正女北" --size 200 --out font-src/reports/sheet-joyo-s1-002.png
```
判定：check_recipes PASS（问题 0）；check_glyphs FAIL=0；verify_font FAIL=0。
**若第 4 条因特性文件报错**：说明 `font-src/features/*.fea` 引用了本批没有的字形——
子集构建会自动跳过不适用的特性文件，若仍失败请把报错原文写进报告交集成方。

【交付步骤】
1. write 一次性写出完整文件（40 个字形全写完，不要分次追加）。
2. 跑上面 6 条命令。
3. **用 read 工具打开 font-src/reports/sheet-joyo-s1-002.png 亲眼看**（不能省）：
   逐字判断：一眼认得出吗？有没有粘连成黑块？内白还在吗？批内观感一致吗？
   不满意就改 recipe → 重新生成 → 重新渲染 → 再看（最多 4 轮）。
4. 提交：
```
git add font-src/src/hkposter-joyo-s1-002.py font-src/masters/hkposter-joyo-s1-002.ufo
git commit -m "wave1/joyo-s1-002: Jōyō 常用漢字 40 字"
```
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
