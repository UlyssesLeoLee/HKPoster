你是 HK Poster Heavy 字体工程的并行制作 lane，负责 **Jōyō 常用漢字批量试制：joyo-s1-003**。

【重要：零读文件模式 + 事实已内联】
本项目上一轮有多个子代理会话被运行时中断，零产出。本提示词已内联全部事实。
**你的第一个工具调用必须是 `write`**，一次性写出完整文件；不要先读仓库文件。

【工作目录 —— 唯一允许写入的地方】
E:/hkposter-lanes/wave1-joyo-s1-003
命令先切过去：`Set-Location 'E:/hkposter-lanes/wave1-joyo-s1-003'`
不要在 E:/HKPoster 里写任何文件。

【你唯一允许写入的路径】
- font-src/src/hkposter-joyo-s1-003.py
- font-src/masters/hkposter-joyo-s1-003.ufo/（由 recipe 生成）

【冻结参数（日本語漢字）】
UPM 1000；y 向上，基线 y=0；ascender 880 / descender -120。
**advance = 1000**；字面框 **x 60..940，y 0..820**（与繁体汉字完全一致，便于中英日混排）。
漢字笔画权重档：**主 96 / 次 92 / 细 84 / 点 84–96**（与 zh-HK 繁体同一档）。

【hkbuild 笔画 API（脚本已存在，import 即可，不要打开它）】
```python
from hkbuild import Glyph, write_ufo, ellipse_points

g = Glyph(name, advance=1000, unicode=0x6BD4, note="说明")
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
"""HK Poster Heavy —— Jōyō 常用漢字 joyo-s1-003。

本批 40 字，笔画范围 3–5，取自 2010 年文化厅《常用漢字表》。

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
    return FONT_SRC / "masters" / "hkposter-joyo-s1-003.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
```

【你的字符清单（40 个，冻结，不得增删、不得改 Unicode）】
字形名一律 `uniXXXX`（大写十六进制）。
- 比  U+6BD4  uni6BD4  4 画  (频率排名 329)
- 夫  U+592B  uni592B  4 画  (频率排名 335)
- 収  U+53CE  uni53CE  5 画  (频率排名 337)
- 井  U+4E95  uni4E95  4 画  (频率排名 339)
- 石  U+77F3  uni77F3  5 画  (频率排名 342)
- 万  U+4E07  uni4E07  3 画  (频率排名 375)
- 辺  U+8FBA  uni8FBA  4 画  (频率排名 428)
- 仕  U+4ED5  uni4ED5  5 画  (频率排名 439)
- 去  U+53BB  uni53BB  5 画  (频率排名 440)
- 失  U+5931  uni5931  5 画  (频率排名 447)
- 写  U+5199  uni5199  5 画  (频率排名 453)
- 末  U+672B  uni672B  5 画  (频率排名 456)
- 白  U+767D  uni767D  5 画  (频率排名 483)
- 申  U+7533  uni7533  5 画  (频率排名 492)
- 古  U+53E4  uni53E4  5 画  (频率排名 509)
- 史  U+53F2  uni53F2  5 画  (频率排名 511)
- 天  U+5929  uni5929  4 画  (频率排名 512)
- 士  U+58EB  uni58EB  3 画  (频率排名 526)
- 丸  U+4E38  uni4E38  3 画  (频率排名 542)
- 他  U+4ED6  uni4ED6  5 画  (频率排名 543)
- 及  U+53CA  uni53CA  3 画  (频率排名 544)
- 処  U+51E6  uni51E6  5 画  (频率排名 547)
- 旧  U+65E7  uni65E7  5 画  (频率排名 549)
- 太  U+592A  uni592A  4 画  (频率排名 552)
- 母  U+6BCD  uni6BCD  5 画  (频率排名 570)
- 火  U+706B  uni706B  4 画  (频率排名 574)
- 戸  U+6238  uni6238  4 画  (频率排名 575)
- 央  U+592E  uni592E  5 画  (频率排名 582)
- 号  U+53F7  uni53F7  5 画  (频率排名 585)
- 右  U+53F3  uni53F3  5 画  (频率排名 602)
- 介  U+4ECB  uni4ECB  4 画  (频率排名 617)
- 弁  U+5F01  uni5F01  5 画  (频率排名 619)
- 友  U+53CB  uni53CB  4 画  (频率排名 622)
- 左  U+5DE6  uni5DE6  5 画  (频率排名 630)
- 父  U+7236  uni7236  4 画  (频率排名 646)
- 未  U+672A  uni672A  5 画  (频率排名 650)
- 亡  U+4EA1  uni4EA1  3 画  (频率排名 661)
- 込  U+8FBC  uni8FBC  4 画  (频率排名 675)
- 王  U+738B  uni738B  4 画  (频率排名 684)
- 久  U+4E45  uni4E45  3 画  (频率排名 688)

【設計要点】
- 本批字形密度接近（3–5 画），**务必保持同族观感**：
  同一部件（如 亻、氵、扌、木）在批内要**复用同一套坐标与笔画拆法**，
  只做位置与大小的光学校正（docs/03 GLY-004）。
- 每个字先在 docstring 里写**笔画清单与部件分区坐标**，再逐笔画落坐标并注明所属部件。
- 笔画少的字要**加粗**（用 96），笔画多的字在拥挤处**局部减重**到 84，
  否则同批内会出现"有的太轻、有的太闷"（GLY-001 允许小空腔局部减重）。
- 密排处（横画叠横画）内白不低于 24 单位；竖与竖之间不低于 60 单位（GLY-006）。
- 禁止逐字机械挤压或倾斜（docs/02 偏差 D）。

【要跑的 6 条命令（全部在 lane worktree 下执行）】
```
python font-src/src/hkposter-joyo-s1-003.py
python font-src/scripts/check_recipes.py --recipes font-src/src/hkposter-joyo-s1-003.py
python font-src/scripts/check_glyphs.py --sources font-src/masters/hkposter-joyo-s1-003.ufo
python font-src/scripts/build_font.py --sources font-src/masters/hkposter-joyo-s1-003.ufo --out font-src/dist
python font-src/scripts/verify_font.py --font font-src/dist/HKPoster-Heavy.ttf --sources font-src/masters/hkposter-joyo-s1-003.ufo
python font-src/scripts/render_glyph_sheet.py --font font-src/dist/HKPoster-Heavy.ttf --text "比夫収井石万辺仕去失写末" --size 200 --out font-src/reports/sheet-joyo-s1-003.png
```
判定：check_recipes PASS（问题 0）；check_glyphs FAIL=0；verify_font FAIL=0。
**若第 4 条因特性文件报错**：说明 `font-src/features/*.fea` 引用了本批没有的字形——
子集构建会自动跳过不适用的特性文件，若仍失败请把报错原文写进报告交集成方。

【交付步骤】
1. write 一次性写出完整文件（40 个字形全写完，不要分次追加）。
2. 跑上面 6 条命令。
3. **用 read 工具打开 font-src/reports/sheet-joyo-s1-003.png 亲眼看**（不能省）：
   逐字判断：一眼认得出吗？有没有粘连成黑块？内白还在吗？批内观感一致吗？
   不满意就改 recipe → 重新生成 → 重新渲染 → 再看（最多 4 轮）。
4. 提交：
```
git add font-src/src/hkposter-joyo-s1-003.py font-src/masters/hkposter-joyo-s1-003.ufo
git commit -m "wave1/joyo-s1-003: Jōyō 常用漢字 40 字"
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
