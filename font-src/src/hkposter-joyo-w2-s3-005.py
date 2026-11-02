"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s3-005。

本批 24 字，笔画范围 10–13，取自 2010 年文化厅《常用漢字表》。

整体设计取舍
------------
1. 度量：UPM 1000，advance 1000，**字面框 x 60..940 / y 0..820**（与繁体汉字同一档，
   便于中英日混排）。每个字的墨迹都顶到 820、坐到 0，批内顶线/基线齐平。
2. 笔画权重四档（与 zh-HK 繁体同档）：主 96 / 次 92 / 细 84 / 点 84–96。
   笔画少的字（宮・商・病・起）主干用 96；笔画多的字（幹・農・試・働・象）
   在拥挤处（口、日、目、廿、里）降到 84，让墨量率与同批一致（docs/03 GLY-001）。
3. **对齐规则**：笔画是「中心线 + 垂直权重」，所以要让墨迹极值对齐 820 / 0，
   中心线必须内缩半个笔画宽。本 recipe 用 `htop` / `hbase` 两个辅助函数处理
   顶/底对齐；竖画的 vbar 端点即墨迹端点，直接给 0 / 820。
4. **海报端点**：横竖撇捺一律平切硬边（hkbuild 的 hbar/vbar/diag 天然平切），
   点与短撇一律用斜切平行四边形（`g.dot`），这是本字体的签名。
   slant 分档严格按 GLY-004：丶=-14、丿=+14、短撇=26、竖点=0，不自造档位。
5. **骨架来源**：笔画清单与部件拆法依 KanjiVG 的笔顺分解（CC BY-SA 3.0，
   只取骨架不描轮廓），比例与视觉密度参照 M PLUS 1p Black 与
   Zen Kaku Gothic New Black（均 SIL OFL 1.1，只参考比例与骨架）。
   **笔画角度照标准骨架**：横画水平、竖画垂直，撇取 55°–65°、捺取 30°–46°、
   提取 45°–50°，与参照字一致，不为「好看」改斜率。
6. **批内同族观感**：同一个部件在本批只用一套坐标与拆法（GLY-004）——
   氵、言、口、日/目、木、艹、亻、夂、戈 各写一份，跨字复用；只做位置与
   大小的光学校正。

同批复用部件（本批唯一定义处）
------------------------------
  氵   : 上点 slant 26 / 中点 slant -14 / 提 45°       —— 落、準
  言   : 丶 + 三横 + 口                                —— 訪、試
  口   : kou()                                         —— 宮、訪、試、落、景、商
  日/目: ri() / mu()                                   —— 幹、着、想、景、農
  木   : 横 + 竖 + 撇 + 捺                             —— 想、楽、葉
  艹   : 一 + 两竖                                     —— 葉、落
  夂   : 撇 + 横撇 + 捺                                —— 落
  戈   : 横 + 斜钩 + 撇 + 点                           —— 残、域、試、然
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
W_LIGHT = 76  # 高密字局部减重（四横以上的方框）

TOP = 820.0
BASE = 0.0


# ------------------------------------------------------------------ 对齐辅助
def htop(g, x1, x2, weight):
    """横画：墨迹上缘对齐字面顶线 820（中心线内缩半个笔画宽）。"""
    g.hbar(x1, x2, TOP - weight / 2.0, weight)
    return g


def hbase(g, x1, x2, weight):
    """横画：墨迹下缘对齐基线 0。"""
    g.hbar(x1, x2, BASE + weight / 2.0, weight)
    return g


def kou(g, xl, xr, yt, yb, weight):
    """口：左右竖的中心线在 xl / xr，上横中心线 yt，下横中心线 yb。"""
    g.hbar(xl, xr, yt, weight)
    g.vbar(xl, yt, yb, weight)
    g.vbar(xr, yt, yb, weight)
    g.hbar(xl, xr, yb, weight)
    return g


def ri(g, xl, xr, yt, ym, yb, weight):
    """日：上横 yt / 中横 ym / 下横 yb，左右竖在 xl / xr。"""
    g.hbar(xl, xr, yt, weight)
    g.vbar(xl, yt, yb, weight)
    g.vbar(xr, yt, yb, weight)
    g.hbar(xl, xr, ym, weight)
    g.hbar(xl, xr, yb, weight)
    return g


def mu(g, xl, xr, yt, y1, y2, yb, weight):
    """目：上横 yt + 三条内横 y1 / y2 / yb + 左右竖。"""
    g.hbar(xl, xr, yt, weight)
    g.vbar(xl, yt, yb, weight)
    g.vbar(xr, yt, yb, weight)
    g.hbar(xl, xr, y1, weight)
    g.hbar(xl, xr, y2, weight)
    g.hbar(xl, xr, yb, weight)
    return g


def sanzui(g, x, ytop, ymid, ybot):
    """氵：三点水（居左，x 为三点中心的基准 x）。

    上点按短撇用 slant 26，中点是右下点用 slant -14，提为 45° 斜画。
    本批（落・準）共用这一份坐标与拆法。
    """
    g.dot(x, ytop, w=90, h=110, slant=26)          # 上点（短撇）
    g.dot(x - 15, ymid, w=90, h=110, slant=-14)     # 中点
    g.diag(x - 65, ybot, x + 75, ybot + 140, weight=W_SEC)   # 提
    return g


def gen(g):
    """言：左偏旁（訪・試 共用）。顶点在 x 205，横画在 x 60..350 一带。"""
    g.dot(205, 778, w=84, h=88, slant=-14)         # 顶上的点（右下点）
    g.hbar(60, 350, 620, weight=W_MAIN)             # 亠的长横
    g.hbar(120, 345, 480, weight=W_SEC)             # 第二横
    g.hbar(115, 340, 350, weight=W_SEC)             # 第三横
    kou(g, 135, 330, 200, 48, W_SEC)                # 口
    return g


def kusa(g, x1, x2, ybar, xl, xr, ybot):
    """艹：横画 ybar + 两根竖（xl / xr），竖从字面顶穿到 ybot。"""
    g.hbar(x1, x2, ybar, weight=W_MAIN)
    g.vbar(xl, TOP, ybot, weight=W_MAIN)
    g.vbar(xr, TOP, ybot, weight=W_MAIN)
    return g


def mukin(g, x, ytop, ybot):
    """木：横 + 竖 + 撇 + 捺（想・楽・葉 共用同一套角度）。"""
    g.hbar(x - 200, x + 170, ytop, weight=W_MAIN)   # 横
    g.vbar(x, ytop + 100, BASE, weight=W_MAIN)       # 竖
    g.diag(x, ytop, x - 190, ytop - 270, weight=W_MAIN)      # 撇
    g.dot(x + 70, ytop - 110, w=84, h=100, slant=-14)        # 右下的捺点
    return g


# ------------------------------------------------------------------ 單字
def glyph_gan() -> Glyph:
    """幹（U+5E79，13 画）：左 龺（十+日+十），右 人 + 干。

    部件分区：左 龺 x 60..440，右 人/干 x 470..940。
    骨架依 KanjiVG：左 = 十（上）+ 早（日+十，下）+ 十（最下）；
      右 = 人（撇捺）压在 干（两横一竖）之上。
    取舍：左列的日三横密排（580/460/340），内白各 36 单位；
      顶部十的竖收在日头横里，不越出；右列人字撇收在两列之间的空档，
      不碰日字右边竖（余隙 40+），避免「粘连」。
    """
    g = Glyph("uni5E79", advance=1000, unicode=0x5E79, note="幹：左龺（十+日+十），右人+干")

    # 龺：上面的十
    g.hbar(60, 440, 700, weight=W_MAIN)
    g.vbar(270, TOP, 600, weight=W_MAIN)
    # 龺：日
    g.hbar(160, 400, 580, weight=W_THIN)
    g.vbar(160, 580, 340, weight=W_THIN)
    g.vbar(400, 580, 340, weight=W_THIN)
    g.hbar(160, 400, 460, weight=W_THIN)
    g.hbar(160, 400, 340, weight=W_THIN)
    # 龺：下面的十
    g.hbar(60, 440, 160, weight=W_MAIN)
    g.vbar(270, 340, BASE, weight=W_MAIN)
    # 右：人
    g.diag(655, 795, 495, 475, weight=W_MAIN)      # 撇
    g.diag(645, 790, 915, 545, weight=W_MAIN)      # 捺
    # 右：干
    g.hbar(560, 820, 500, weight=W_MAIN)
    g.hbar(490, 940, 310, weight=W_MAIN)
    g.vbar(680, 500, BASE, weight=W_MAIN)
    return g


def glyph_miya() -> Glyph:
    """宮（U+5BAE，10 画）：宀 + 呂。

    部件分区：宀占顶（y 640..820），上口（y 400..540），撇（y 280..380），
      下口（y 48..265）。
    取舍：宀在日式字里写得比参照略宽（横画到 880），下口比上口大一圈，
      两口之间用一短撇相连（斜率 67°，与标准骨架一致）。
      宀的点用竖点（slant 0），左点用左下点（slant 14）。
    """
    g = Glyph("uni5BAE", advance=1000, unicode=0x5BAE, note="宮：宀 + 呂（两口之间一短撇）")

    # 宀
    g.dot(500, 776, w=84, h=88, slant=0)           # 宀的点（竖点）
    g.dot(150, 645, w=84, h=100, slant=14)          # 冖的左点
    g.hbar(150, 880, 660, weight=W_MAIN)            # 冖的横
    g.vbar(880, 660, 600, weight=W_SEC)             # 冖的右钩
    # 呂：上口
    kou(g, 340, 660, 540, 400, W_THIN)
    # 呂：中间的撇
    g.diag(510, 380, 465, 280, weight=W_SEC)
    # 呂：下口
    kou(g, 250, 750, 265, 48, W_MAIN)
    return g


def glyph_seki() -> Glyph:
    """席（U+5E2D，10 画）：广 + 廿 + 巾。

    部件分区：广（点/横/长撇）占顶，廿在中（y 460..660），巾在下（y 0..320）。
    取舍：广的撇极长且陡（78°，与骨架一致），从上横左端一路压到基线；
      廿两竖穿过上横、落在下横；巾的中竖是全字最长的竖，穿过巾的上横到底。
      密排处（廿下横 460 / 巾上横 320）留白 38 单位。
    """
    g = Glyph("uni5E2D", advance=1000, unicode=0x5E2D, note="席：广 + 廿 + 巾")

    # 广
    g.dot(555, 785, w=84, h=70, slant=0)           # 广的点（竖点）
    g.hbar(200, 940, 710, weight=W_MAIN)            # 厂的一
    g.diag(255, 655, 125, 55, weight=W_MAIN)        # 厂的长撇
    # 廿
    g.hbar(300, 870, 590, weight=W_SEC)
    g.vbar(440, 650, 450, weight=W_SEC)
    g.vbar(680, 650, 450, weight=W_SEC)
    g.hbar(440, 680, 450, weight=W_SEC)
    # 巾
    g.hbar(340, 780, 300, weight=W_SEC)
    g.vbar(340, 300, 70, weight=W_SEC)
    g.vbar(780, 300, 110, weight=W_SEC)
    g.vbar(560, 375, BASE, weight=W_MAIN)
    return g


def glyph_hou() -> Glyph:
    """訪（U+8A2A，11 画）：言 + 方。

    部件分区：言 x 60..350，方 x 420..940。
    取舍：言旁三横等宽递减、下方一个小口；方字的亠点在右上，
      横折钩的竖落在 x 810，撇从横的左端起笔向左下扫出（63°）。
      撇的起笔嵌在横折钩的横里，不留断口。
    """
    g = Glyph("uni8A2A", advance=1000, unicode=0x8A2A, note="訪：言 + 方（方左扫长撇）")

    gen(g)
    # 方
    g.dot(660, 690, w=84, h=120, slant=0)           # 亠的点（竖点）
    g.hbar(430, 940, 640, weight=W_MAIN)            # 亠的横
    g.hbar(640, 810, 470, weight=W_MAIN)            # 横折钩的横
    g.vbar(810, 470, 130, weight=W_MAIN)            # 横折钩的竖
    g.diag(810, 130, 700, 60, weight=W_SEC)         # 横折钩的钩
    g.diag(640, 500, 430, 120, weight=W_MAIN)       # 长撇
    return g


def glyph_raku() -> Glyph:
    """楽（U+697D，13 画）：白 + 冫 + 丷 + 木。

    部件分区：白在正中偏上（x 370..590, y 439..710），左 冫（点+提），
      右 丷（撇+点），木占下半（y 0..301）。
    取舍：白窄高，是全字的「轴」；左右各两笔（冫 / 丷）把白夹住，
      木的长横（y 301）贯通全宽，是整字的分界；木的竖最长，落到基线。
      白内的两条横把白分成三层，层间白口 41 单位。
    """
    g = Glyph("uni697D", advance=1000, unicode=0x697D, note="楽：白 + 冫 + 丷 + 木")

    # 白
    g.diag(470, 800, 410, 725, weight=W_THIN)       # 白的头撇
    g.vbar(345, 700, 450, weight=W_THIN)            # 日的左竖
    g.hbar(345, 615, 700, weight=W_THIN)            # 日的上横
    g.vbar(615, 700, 450, weight=W_THIN)            # 日的右竖
    g.hbar(345, 615, 575, weight=W_THIN)            # 日的中横
    g.hbar(345, 615, 450, weight=W_THIN)            # 日的下横
    # 左：冫（点 + 提）
    g.dot(215, 680, w=88, h=104, slant=-14)         # 冫的点
    g.diag(140, 420, 285, 545, weight=W_THIN)       # 冫的提
    # 右：丷（撇 + 点）
    g.diag(800, 760, 700, 645, weight=W_THIN)       # 撇
    g.dot(780, 480, w=88, h=104, slant=-14)         # 点
    # 木
    g.hbar(140, 844, 301, weight=W_MAIN)            # 木的横
    g.vbar(478, 408, BASE, weight=W_MAIN)           # 木的竖
    g.diag(441, 294, 147, 40, weight=W_MAIN)        # 木的撇
    g.diag(512, 175, 863, 40, weight=W_MAIN)        # 木的捺
    return g


def glyph_ki() -> Glyph:
    """起（U+8D77，10 画）：走 + 己。

    部件分区：走 x 60..560（土 + 龰），己 x 580..940。
    取舍：走字底的长捺从左下横扫到右下角，是全字的基线；
      龰的撇（62°）与捺分开起笔，中间留空，不并成「人」。
      己是三横一竖加底部的竖弯钩，横折钩的竖落在 x 870。
    """
    g = Glyph("uni8D77", advance=1000, unicode=0x8D77, note="起：走 + 己（走底长捺贯通）")

    # 走：土
    g.hbar(110, 480, 660, weight=W_MAIN)
    g.vbar(300, TOP, 500, weight=W_MAIN)
    g.hbar(90, 500, 500, weight=W_MAIN)
    # 走：龰
    g.vbar(320, 470, 180, weight=W_SEC)
    g.hbar(320, 500, 320, weight=W_SEC)
    g.diag(320, 320, 170, 40, weight=W_SEC)         # 龰的撇
    g.diag(300, 175, 915, 25, weight=W_MAIN)        # 走底长捺
    # 己
    g.hbar(600, 870, 720, weight=W_MAIN)
    g.vbar(870, 720, 560, weight=W_MAIN)
    g.hbar(600, 870, 520, weight=W_MAIN)
    g.vbar(620, 520, 330, weight=W_MAIN)
    g.diag(620, 330, 870, 215, weight=W_MAIN)       # 己的底（竖弯钩）
    return g


def glyph_chaku() -> Glyph:
    """着（U+7740，12 画）：羊字头 + 丿 + 目。

    部件分区：丷在顶（y 760），三横 680/560/442，长撇斜穿左上，目占下半。
    取舍：羊字头的三横逐级加宽（最下一横 150..860 贯通），
      撇从最下一横左端斜下（45°，与骨架一致），左下的目四横密排，
      每层白口 24 单位。
    2026-10-31 回修：羊字头最下一横与目頂白口 −10、羊字头两道横白口 −4 →
    最下一横上移 28、目四横上移并局部减重（W_THIN 84 → W_LIGHT 76），白口各 24。
    """
    g = Glyph("uni7740", advance=1000, unicode=0x7740, note="着：羊字头 + 丿 + 目")

    # 丷
    g.dot(340, 765, w=88, h=110, slant=-14)         # 左点
    g.dot(630, 765, w=88, h=110, slant=14)          # 右撇
    # 羊字头
    g.hbar(250, 720, 680, weight=W_MAIN)
    g.vbar(485, 640, 470, weight=W_SEC)
    g.hbar(270, 700, 560, weight=W_SEC)
    g.hbar(150, 860, 442, weight=W_MAIN)
    # 丿
    g.diag(360, 400, 140, 180, weight=W_MAIN)
    # 目
    mu(g, 380, 670, 328, 228, 128, 28, W_LIGHT)
    return g


def glyph_zan() -> Glyph:
    """残（U+6B8B，10 画）：歹 + 戔。

    部件分区：歹 x 60..430（一 + 夕），戔 x 440..940（三横 + 斜钩 + 撇 + 点）。
    取舍：歹的横撇在 x 400 折向左下（59°），点落在撇与横之间；
      戈的斜钩自上而下（68°）并在末端带一个小钩，撇从右上斜下（43°），
      与斜钩在上半部交叉而不平行重叠。
    """
    g = Glyph("uni6B8B", advance=1000, unicode=0x6B8B, note="残：歹 + 戔（斜钩带钩）")

    # 歹
    g.hbar(80, 420, 720, weight=W_MAIN)
    g.diag(280, 690, 110, 380, weight=W_MAIN)       # 歹的撇
    g.hbar(260, 400, 545, weight=W_SEC)             # 横撇的横
    g.diag(400, 545, 110, 60, weight=W_SEC)         # 横撇的撇
    g.dot(235, 360, w=84, h=100, slant=-14)         # 歹的点
    # 戔
    g.hbar(470, 790, 660, weight=W_SEC)
    g.hbar(460, 800, 545, weight=W_SEC)
    g.hbar(440, 850, 430, weight=W_MAIN)
    g.diag(670, 795, 875, 70, weight=W_MAIN)        # 斜钩
    g.diag(875, 70, 925, 145, weight=W_SEC)         # 斜钩的钩
    g.diag(800, 390, 460, 70, weight=W_MAIN)        # 撇
    g.dot(800, 750, w=84, h=100, slant=-14)         # 点
    return g


def glyph_sou() -> Glyph:
    """想（U+60F3，13 画）：相（木 + 目）+ 心。

    部件分区：木 x 60..470，目 x 530..815，心占底部（y 0..250）。
    取舍：目四横密排（770/630/490/350），层间白口 56；
      心用一条长卧钩（26° 斜）加三点，左点与卧钩分开，
      中点与右点用右下点（slant -14）。
    """
    g = Glyph("uni60F3", advance=1000, unicode=0x60F3, note="想：相（木+目）+ 心")

    # 木
    g.hbar(90, 460, 670, weight=W_MAIN)
    g.vbar(290, TOP, 480, weight=W_MAIN)
    g.diag(290, 660, 90, 380, weight=W_MAIN)        # 木的撇
    g.dot(360, 570, w=84, h=100, slant=-14)         # 木的右点
    # 目
    mu(g, 530, 815, 770, 630, 490, 350, W_THIN)
    # 心
    g.dot(175, 150, w=84, h=100, slant=14)          # 心左点（左倾点）
    g.diag(300, 255, 740, 55, weight=W_MAIN)        # 卧钩（向右下长扫）
    g.diag(740, 55, 790, 130, weight=W_SEC)         # 卧钩的钩
    g.dot(470, 250, w=84, h=100, slant=-14)         # 心中点
    g.dot(840, 235, w=84, h=100, slant=-14)         # 心右点
    return g


def glyph_ritsu() -> Glyph:
    """率（U+7387，11 画）：亠 + 幺 + 冫 + 十。

    部件分区：亠占顶（y 640..820），幺在中（x 375..570），冫在左，
      十在下（y 0..360）。
    取舍：幺的两笔「撇折」都写成 撇 + 短横（角度 120° / 133°），
      点的斜切用 -14；左边的冫（点 + 提）与右上的撇、点呼应。
      底部十的横贯通全宽，竖落在 x 494。
    """
    g = Glyph("uni7387", advance=1000, unicode=0x7387, note="率：亠 + 幺 + 冫 + 十")

    # 亠
    g.dot(495, 770, w=84, h=100, slant=0)           # 竖点
    g.hbar(190, 810, 640, weight=W_MAIN)
    # 幺
    g.diag(450, 650, 390, 545, weight=W_THIN)       # 幺的第一撇
    g.hbar(390, 465, 545, weight=W_THIN)            # 幺的第一折
    g.diag(560, 620, 375, 425, weight=W_THIN)       # 幺的第二撇
    g.hbar(375, 570, 430, weight=W_THIN)            # 幺的第二折
    g.dot(580, 455, w=80, h=96, slant=-14)          # 幺的点
    # 左：冫
    g.dot(225, 590, w=84, h=100, slant=-14)         # 冫的点
    g.diag(190, 380, 300, 490, weight=W_THIN)       # 冫的提
    # 右：撇 + 点
    g.diag(745, 630, 655, 545, weight=W_THIN)       # 撇
    g.dot(730, 450, w=84, h=100, slant=-14)         # 点
    # 十
    g.hbar(110, 890, 250, weight=W_MAIN)
    g.vbar(495, 360, BASE, weight=W_MAIN)
    return g


def glyph_byou() -> Glyph:
    """病（U+75C5，10 画）：疒 + 丙。

    部件分区：疒占左上（点/横/长撇 + 冫），丙在右下（x 380..900）。
    取舍：疒的长撇极陡（78°）贴左边下行，冫的点与提在撇与框之间；
      丙是「一 + 冂 + 人」，人字的一撇一捺在框内分开，不并成一根。
    2026-10-31 回修：疒的横与丙的一白口 −6 → 疒的横上抬 30、白口 24，
    长撇随之平移 12（斜率不变）。
    """
    g = Glyph("uni75C5", advance=1000, unicode=0x75C5, note="病：疒 + 丙")

    # 疒
    g.dot(565, 760, w=84, h=100, slant=0)           # 竖点
    g.hbar(280, 900, 650, weight=W_MAIN)
    g.diag(300, 612, 190, 72, weight=W_MAIN)        # 疒的长撇
    g.dot(190, 530, w=80, h=96, slant=-14)          # 疒内的点
    g.diag(150, 280, 285, 395, weight=W_THIN)       # 疒内的提
    # 丙
    g.hbar(410, 860, 530, weight=W_MAIN)            # 一
    g.vbar(400, 350, BASE, weight=W_MAIN)           # 冂的左竖
    g.hbar(400, 870, 350, weight=W_MAIN)            # 冂的横
    g.vbar(870, 350, 60, weight=W_MAIN)             # 冂的右竖
    g.diag(870, 55, 800, 80, weight=W_SEC)          # 冂的钩
    g.diag(620, 430, 520, 140, weight=W_SEC)        # 丙里人的撇
    g.diag(620, 280, 770, 140, weight=W_SEC)        # 丙里人的捺
    return g


def glyph_no() -> Glyph:
    """農（U+8FB2，13 画）：曲 + 辰。

    部件分区：曲占顶（y 460..820），辰占下半（y 0..440）。
    取舍：曲是两竖穿一框，框内一条横（三横分两层）；
      辰是厂 + 二 + 竖提 + 撇 + 捺，厂的一贯通全宽；
      竖提的挑与捺在右下分开，捺从竖提上方起笔，不与挑平行重叠。
    """
    g = Glyph("uni8FB2", advance=1000, unicode=0x8FB2, note="農：曲 + 辰")

    # 曲
    g.hbar(290, 760, 770, weight=W_MAIN)            # 曲的上横
    g.vbar(430, 810, 510, weight=W_MAIN)            # 曲内左竖（出头）
    g.vbar(620, 810, 510, weight=W_MAIN)            # 曲内右竖（出头）
    g.vbar(300, 770, 510, weight=W_MAIN)            # 曲的左竖
    g.vbar(750, 770, 510, weight=W_MAIN)            # 曲的右竖
    g.hbar(290, 760, 640, weight=W_THIN)            # 曲内的横
    g.hbar(290, 760, 510, weight=W_MAIN)            # 曲的下横
    # 辰：厂
    g.hbar(200, 900, 390, weight=W_MAIN)
    g.diag(280, 360, 150, 30, weight=W_MAIN)         # 厂的撇
    # 辰：二
    g.hbar(330, 660, 270, weight=W_SEC)
    g.hbar(310, 560, 170, weight=W_SEC)
    # 辰：竖提
    g.vbar(420, 175, 60, weight=W_SEC)
    g.diag(420, 60, 500, 95, weight=W_SEC)
    # 辰：撇 + 捺
    g.diag(800, 260, 720, 170, weight=W_THIN)
    g.diag(620, 95, 895, 15, weight=W_MAIN)
    return g


def glyph_shi() -> Glyph:
    """試（U+8A66，13 画）：言 + 式。

    部件分区：言 x 60..350，式 x 400..940。
    取舍：式的弋斜钩自上而下穿过长横（x 700 → 890），
      工在左下（三笔：横、竖、提），提是 26° 的斜画；
      弋的点用右下点，落在右上角。
    """
    g = Glyph("uni8A66", advance=1000, unicode=0x8A66, note="試：言 + 式（弋斜钩穿横）")

    gen(g)
    # 式
    g.hbar(420, 900, 590, weight=W_MAIN)            # 弋的横
    g.diag(700, 800, 890, 60, weight=W_MAIN)        # 斜钩
    g.diag(890, 60, 930, 140, weight=W_SEC)         # 斜钩的钩
    g.dot(790, 740, w=84, h=100, slant=-14)         # 弋的点
    g.hbar(430, 650, 390, weight=W_SEC)             # 工的上横
    g.vbar(540, 390, 190, weight=W_SEC)             # 工的竖
    g.diag(430, 180, 660, 290, weight=W_SEC)        # 工的提
    return g


def glyph_zoku() -> Glyph:
    """族（U+65CF，11 画）：方 + 𠂉 + 矢。

    部件分区：方 x 60..430，右上 𠂉（撇+横），右下 矢（撇+二+人）。
    取舍：方的横折钩的竖在 x 380，钩向左下；方的撇极陡（78°）；
      矢的两横逐级加宽（最下一横贯通全宽），人字的一撇一捺分列。
    """
    g = Glyph("uni65CF", advance=1000, unicode=0x65CF, note="族：方 + 𠂉 + 矢")

    # 方
    g.dot(265, 730, w=84, h=100, slant=0)           # 亠的点
    g.hbar(80, 440, 620, weight=W_MAIN)
    g.hbar(270, 380, 480, weight=W_SEC)             # 横折钩的横
    g.vbar(380, 480, 120, weight=W_SEC)             # 横折钩的竖
    g.diag(380, 120, 310, 70, weight=W_SEC)         # 横折钩的钩
    g.diag(255, 575, 165, 160, weight=W_MAIN)       # 方的长撇
    # 𠂉
    g.diag(570, 790, 460, 570, weight=W_MAIN)       # 撇
    g.hbar(560, 850, 680, weight=W_MAIN)
    # 矢
    g.diag(575, 560, 460, 380, weight=W_MAIN)       # 矢的撇
    g.hbar(550, 830, 480, weight=W_SEC)
    g.hbar(430, 920, 290, weight=W_MAIN)
    g.diag(650, 420, 400, 20, weight=W_MAIN)        # 人的撇
    g.diag(650, 270, 920, 30, weight=W_MAIN)        # 人的捺
    return g


def glyph_zou() -> Glyph:
    """象（U+8C61，12 画）：𠂊 + 口 + 豕。

    部件分区：𠂊 占顶（y 615..800），口在左上（x 250..680），豕占下半。
    取舍：象的中部是「开口的口」——口的下边由豕的第一横补上，
      口里有一小竖（象字自身的一笔）；豕的三撇逐层向左下展开，
      最下一撇到 x 115，捺到 x 880。撇与捺分居弯钩两侧。
    """
    g = Glyph("uni8C61", advance=1000, unicode=0x8C61, note="象：𠂊 + 口 + 豕")

    # 𠂊
    g.diag(420, 795, 240, 615, weight=W_MAIN)       # 撇
    g.hbar(420, 600, 780, weight=W_MAIN)            # 横撇的横
    g.diag(600, 780, 500, 630, weight=W_MAIN)       # 横撇的撇
    # 口（下方由豕的横补齐）
    g.hbar(250, 680, 600, weight=W_MAIN)
    g.vbar(250, 600, 480, weight=W_MAIN)
    g.vbar(680, 600, 480, weight=W_MAIN)
    g.vbar(480, 585, 500, weight=W_SEC)             # 口里的一小竖
    # 豕
    g.hbar(280, 690, 480, weight=W_MAIN)            # 豕的横
    g.diag(440, 440, 200, 320, weight=W_MAIN)       # 豕的第一撇
    g.vbar(465, 390, 40, weight=W_MAIN)             # 豕的弯钩竖
    g.diag(465, 40, 400, 95, weight=W_SEC)          # 豕的弯钩
    g.diag(445, 335, 165, 165, weight=W_MAIN)       # 豕的第二撇
    g.diag(490, 235, 115, 10, weight=W_MAIN)        # 豕的第三撇
    g.diag(730, 410, 535, 300, weight=W_THIN)       # 豕的第四撇
    g.diag(530, 280, 880, 45, weight=W_MAIN)        # 豕的捺
    return g


def glyph_iki() -> Glyph:
    """域（U+57DF，11 画）：土 + 或。

    部件分区：土 x 60..340（或左偏旁），或 x 350..940。
    取舍：土的提是 34° 的斜画；或的口小而方，斜钩自上而下冲出到右下角；
      或的下横（28° 的提）压在口下，撇从右上斜下（60°）与斜钩不相撞。
    """
    g = Glyph("uni57DF", advance=1000, unicode=0x57DF, note="域：土 + 或（斜钩冲出右下）")

    # 土
    g.hbar(60, 330, 540, weight=W_MAIN)
    g.vbar(200, 760, 230, weight=W_MAIN)
    g.diag(80, 150, 330, 320, weight=W_SEC)          # 土的提
    # 或
    g.hbar(380, 830, 620, weight=W_MAIN)            # 弋的横
    g.diag(700, 800, 890, 90, weight=W_MAIN)        # 斜钩
    g.diag(890, 90, 930, 165, weight=W_SEC)         # 斜钩的钩
    g.dot(770, 770, w=84, h=100, slant=-14)         # 点
    kou(g, 390, 560, 450, 315, W_SEC)                # 口
    g.diag(360, 110, 590, 235, weight=W_SEC)        # 或的下横（提）
    g.diag(810, 495, 560, 60, weight=W_MAIN)        # 撇
    return g


def glyph_nen() -> Glyph:
    """然（U+7136，12 画）：肰（月 + 犬）+ 灬。

    部件分区：月 x 60..450，犬 x 450..940，灬占底（y 0..180）。
    取舍：月的左撇与横折钩的下行都向左斜（56°–59°），两条内短横
      随字势上扬；犬的一横贯通、一撇一捺分明；灬四点用斜切平行四边形，
      第四点作撇（slant 14）。
    """
    g = Glyph("uni7136", advance=1000, unicode=0x7136, note="然：月 + 犬 + 灬（底部四点）")

    # 月
    g.diag(290, 800, 120, 520, weight=W_MAIN)       # 月的撇
    g.hbar(290, 440, 760, weight=W_SEC)             # 月的横
    g.diag(440, 760, 130, 290, weight=W_MAIN)        # 月的横折钩
    g.hbar(230, 340, 630, weight=W_THIN)            # 月内第一短横
    g.hbar(180, 290, 505, weight=W_THIN)            # 月内第二短横
    # 犬
    g.hbar(460, 830, 600, weight=W_MAIN)
    g.diag(630, 810, 500, 300, weight=W_MAIN)        # 撇
    g.diag(630, 560, 910, 280, weight=W_MAIN)        # 捺
    g.dot(775, 760, w=84, h=100, slant=-14)         # 点
    # 灬
    g.dot(130, 115, w=84, h=110, slant=-14)
    g.dot(355, 110, w=84, h=110, slant=-14)
    g.dot(580, 110, w=84, h=110, slant=-14)
    g.dot(820, 115, w=84, h=110, slant=14)
    return g


def glyph_chou() -> Glyph:
    """張（U+5F35，11 画）：弓 + 長。

    部件分区：弓 x 60..300，長 x 330..940。
    取舍：弓是「横折 + 横 + 竖折 + 竖钩」四段，末端带一个向左的钩；
      長的竖只占上半（400..790），下半的竖提单独一笔，
      长横贯通全字（y 410），把上下分开；撇捺在右下分列。
    """
    g = Glyph("uni5F35", advance=1000, unicode=0x5F35, note="張：弓 + 長（長下为竖提）")

    # 弓
    g.hbar(70, 290, 750, weight=W_MAIN)
    g.vbar(290, 750, 600, weight=W_MAIN)
    g.hbar(80, 300, 580, weight=W_MAIN)
    g.vbar(90, 580, 390, weight=W_MAIN)
    g.hbar(90, 250, 390, weight=W_MAIN)
    g.vbar(250, 390, 60, weight=W_MAIN)
    g.diag(250, 60, 170, 105, weight=W_SEC)          # 弓的钩
    # 長
    g.vbar(470, 790, 400, weight=W_MAIN)
    g.hbar(480, 760, 800, weight=W_MAIN)
    g.hbar(480, 760, 670, weight=W_SEC)
    g.hbar(480, 760, 545, weight=W_SEC)
    g.hbar(340, 900, 410, weight=W_MAIN)
    g.vbar(440, 400, 60, weight=W_MAIN)
    g.diag(440, 60, 620, 135, weight=W_SEC)         # 竖提
    g.diag(790, 370, 660, 240, weight=W_THIN)       # 撇
    g.diag(540, 340, 920, 25, weight=W_MAIN)        # 捺
    return g


def glyph_shou() -> Glyph:
    """商（U+5546，11 画）：亠 + 丷 + 冂 + 儿 + 口。

    部件分区：亠占顶（y 640..820），丷在 y 550..650，冂占中（y 0..460），
      口在冂的中间下部。
    取舍：冂是左竖 + 横折（右下带钩），口在框内偏下；
      框内左有一撇、右有儿的一挑，与口的上横错开，互不相撞。
    """
    g = Glyph("uni5546", advance=1000, unicode=0x5546, note="商：亠 + 丷 + 冂 + 口（儿在框内）")

    # 亠
    g.dot(490, 770, w=84, h=100, slant=0)           # 竖点
    g.hbar(140, 880, 640, weight=W_MAIN)
    # 丷
    g.dot(340, 600, w=84, h=100, slant=-14)         # 左点
    g.dot(650, 600, w=84, h=100, slant=14)          # 右撇
    # 冂
    g.vbar(180, 460, BASE, weight=W_MAIN)           # 冂的左竖
    g.hbar(180, 820, 460, weight=W_MAIN)            # 冂的横
    g.vbar(820, 460, 50, weight=W_MAIN)             # 冂的右竖
    g.diag(820, 50, 750, 85, weight=W_SEC)          # 冂的钩
    g.diag(390, 420, 250, 280, weight=W_SEC)        # 框内的撇
    g.vbar(570, 440, 380, weight=W_THIN)            # 儿
    g.diag(570, 380, 720, 330, weight=W_THIN)
    # 口
    kou(g, 360, 620, 250, 100, W_SEC)
    return g


def glyph_you() -> Glyph:
    """葉（U+8449，12 画）：艹 + 世 + 木。

    部件分区：艹占顶（y 630..820），世在中（y 330..580），木在下（y 0..354）。
    取舍：艹的两竖穿过顶横；世是「三竖 + 两横 + 底横」，
      中竖与右竖短一截；木的横在 y 250，竖只到 354（不穿世的底横）。
      木的撇捺左右对称展开。
    2026-10-31 回修：世的底横与木的横白口 −16 → 世的三横局部减重
    （96/92 → 84）并把中横上移 17、底横上移 34，各层白口 24。
    """
    g = Glyph("uni8449", advance=1000, unicode=0x8449, note="葉：艹 + 世 + 木")

    # 艹
    kusa(g, 140, 860, 720, 340, 630, 640)
    # 世
    g.hbar(110, 890, 580, weight=W_THIN)            # 世的上横
    g.vbar(330, 580, 330, weight=W_MAIN)            # 世的左竖
    g.vbar(500, 580, 455, weight=W_SEC)             # 世的中竖
    g.vbar(670, 580, 455, weight=W_SEC)             # 世的右竖
    g.hbar(500, 670, 472, weight=W_THIN)            # 世的中横
    g.hbar(330, 760, 364, weight=W_THIN)            # 世的底横
    # 木
    g.hbar(200, 800, 250, weight=W_MAIN)
    g.vbar(490, 354, BASE, weight=W_MAIN)
    g.diag(470, 250, 150, 30, weight=W_MAIN)        # 木的撇
    g.diag(505, 255, 810, 50, weight=W_MAIN)        # 木的捺
    return g


def glyph_dou() -> Glyph:
    """働（U+50CD，13 画）：亻 + 重 + 力。

    部件分区：亻 x 60..280，重 x 270..670，力 x 670..940。
    取舍：重字密（日框三横 + 中竖 + 两横），故框内三横降到 84；
      重的长竖（x 465）从上横贯到最下的提，是全字的脊；
      力的横折钩在右上，撇从力字头的下方斜下（80°）。
    """
    g = Glyph("uni50CD", advance=1000, unicode=0x50CD, note="働：亻 + 重 + 力")

    # 亻
    g.diag(275, 790, 80, 370, weight=W_MAIN)        # 亻的撇
    g.vbar(190, 520, BASE, weight=W_MAIN)           # 亻的竖
    # 重
    g.diag(560, 810, 330, 670, weight=W_MAIN)        # 重的头撇
    g.hbar(270, 660, 630, weight=W_MAIN)             # 重的上横
    g.hbar(330, 600, 510, weight=W_THIN)            # 日的上横
    g.vbar(330, 510, 280, weight=W_LIGHT)            # 日的左竖
    g.vbar(600, 510, 280, weight=W_LIGHT)            # 日的右竖
    g.hbar(330, 600, 400, weight=W_LIGHT)            # 日的中横
    g.hbar(330, 600, 294, weight=W_LIGHT)            # 日的下横（下移 6：下腔 24→30）
    g.vbar(465, 700, 95, weight=W_MAIN)             # 重的长竖
    g.hbar(320, 600, 185, weight=W_SEC)             # 重下的横
    g.diag(290, 45, 540, 135, weight=W_SEC)         # 最下的提
    # 力
    g.hbar(690, 895, 520, weight=W_SEC)
    g.vbar(895, 520, 90, weight=W_SEC)
    g.diag(895, 90, 800, 120, weight=W_SEC)         # 力字的钩
    g.diag(790, 700, 670, 30, weight=W_MAIN)        # 力的撇
    return g


def glyph_kei() -> Glyph:
    """景（U+666F，12 画）：日 + 京。

    部件分区：日占顶（y 510..776），亠 在 y 400..495，口在 y 100..270，
      小占底（y 0..200）。
    取舍：日三层密排（776/660/530），层间白口 46；
      京的亠横最宽（100..900），口居中偏下，小的三笔（竖钩 + 撇 + 点）
      收在口下，左右不越出口的宽度太多。
    """
    g = Glyph("uni666F", advance=1000, unicode=0x666F, note="景：日 + 京（日三层 + 口 + 小）")

    # 日
    ri(g, 270, 710, 776, 660, 510, W_THIN)
    # 京：亠
    g.hbar(100, 900, 400, weight=W_MAIN)
    g.dot(490, 450, w=84, h=90, slant=0)            # 亠的点（竖点）
    # 京：口
    kou(g, 340, 650, 270, 100, W_SEC)
    # 京：小
    g.vbar(495, 200, 40, weight=W_MAIN)             # 小的竖
    g.diag(495, 40, 430, 90, weight=W_SEC)          # 小竖的钩
    g.diag(300, 170, 160, 20, weight=W_THIN)        # 小的撇
    g.dot(755, 90, w=84, h=100, slant=-14)          # 小的点
    return g


def glyph_ochi() -> Glyph:
    """落（U+843D，12 画）：艹 + 氵 + 夂 + 口。

    部件分区：艹占顶（y 630..820），氵在左（x 60..300），
      夂在右上（y 190..580），口在右下（y 33..180）。
    取舍：落字右下的口压到基线；夂的横撇与捺分开，
      捺（33°）从横撇的中段下方起笔，不与横撇平行；
      左边的氵用本批统一的三点水坐标（见 sanzui 部件）。
    """
    g = Glyph("uni843D", advance=1000, unicode=0x843D, note="落：艹 + 氵 + 夂 + 口")

    # 艹
    kusa(g, 120, 880, 710, 330, 660, 630)
    # 氵（与準共用同一套三点水）
    sanzui(g, 215, 570, 400, 60)
    # 夂
    g.diag(521, 564, 383, 389, weight=W_MAIN)        # 夂的撇
    g.hbar(528, 690, 537, weight=W_MAIN)            # 夂的横
    g.diag(690, 537, 350, 200, weight=W_MAIN)       # 夂的横撇
    g.diag(467, 345, 864, 225, weight=W_MAIN)        # 夂的捺
    # 口
    kou(g, 450, 715, 180, 48, W_SEC)
    return g


def glyph_jun() -> Glyph:
    """準（U+6E96，13 画）：氵 + 隹 + 十。

    部件分区：氵 x 60..300，隹 x 370..860，底下的十贯通全宽（y 221）。
    取舍：隹的竖（x 634）贯穿四条横；亻头（撇+竖）贴在隹的左侧；
      底下的十的竖落在 x 492，是全字的中轴，与上方的隹错开半格。
    """
    g = Glyph("uni6E96", advance=1000, unicode=0x6E96, note="準：氵 + 隹 + 十（底下十贯通）")

    # 氵（与落共用同一套三点水）
    sanzui(g, 215, 700, 500, 120)
    # 隹：亻头
    g.diag(503, 787, 369, 613, weight=W_MAIN)       # 亻的撇
    g.vbar(471, 693, 387, weight=W_LIGHT)            # 亻的竖
    # 隹：撇 + 四横 + 竖
    g.diag(682, 813, 634, 714, weight=W_THIN)       # 隹的头撇
    g.hbar(476, 806, 708, weight=W_LIGHT)            # 隹的第一横
    g.vbar(634, 690, 420, weight=W_LIGHT)            # 隹的竖
    g.hbar(487, 787, 606, weight=W_LIGHT)            # 隹的第二横
    g.hbar(480, 804, 507, weight=W_LIGHT)            # 隹的第三横
    g.hbar(482, 842, 405, weight=W_LIGHT)            # 隹的第四横
    # 底下的十
    g.hbar(131, 869, 221, weight=W_MAIN)
    g.vbar(492, 339, BASE, weight=W_MAIN)
    return g


def build() -> list[Glyph]:
    return [
        glyph_gan(),
        glyph_miya(),
        glyph_seki(),
        glyph_hou(),
        glyph_raku(),
        glyph_ki(),
        glyph_chaku(),
        glyph_zan(),
        glyph_sou(),
        glyph_ritsu(),
        glyph_byou(),
        glyph_no(),
        glyph_shi(),
        glyph_zoku(),
        glyph_zou(),
        glyph_iki(),
        glyph_nen(),
        glyph_chou(),
        glyph_shou(),
        glyph_you(),
        glyph_dou(),
        glyph_kei(),
        glyph_ochi(),
        glyph_jun(),
    ]


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s3-005.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
