"""HK Poster Heavy —— Jōyō 常用漢字 joyo-w2-s3-008。

本批 24 字，笔画范围 10–13，取自 2010 年文化厅《常用漢字表》。

整体设计取舍（与同批观感统一相关）：

* 字面框与繁体汉字完全一致：x 60..940，y 0..820，advance 1000，基线 y=0。
* 笔画权重只用四档：主 96 / 次 92 / 细 84 / 点 84–96。
* 横画的墨迹上缘对齐 820、下缘对齐 0：中心线内缩半个笔画宽；
  竖画用墨迹上下端点（vbar 的 y1/y2 就是墨迹端点）。
* 同族复用：
  - 左侧偏旁（亻 / 彳 / 扌 / 阝 / 丬）统一用次档 92，左竖落在 x 84..346，
    右缘不超过 x=346，给右半部留出稳定的空间。
  - 木（殺 / 採 / 森 / 根）复用同一骨架：一横 96、一竖 96、下撇下捺 92，
    竖底压在基线 y=0，撇捺收在 y≈200–240。
  - 貝（責 / 販）复用同一骨架：目部四横 84、三段白口各 ≥26，下方八脚同坐标。
  - 方框类（口 / 日 / 目 / 田 / 囗 / 臼）统一「框高 ≥ 2×笔画宽 + 24」，
    即框内白口至少 24 单位；密排时先把横降到 84 再算。
  - 扌 / 木 共用同一斜度：提与撇的斜率固定，不逐字微调。
* 点与短撇的 slant 严格按契约分档：亠的点 0、丶 −14、丿 +14、短撇 26，
  不自造档位。
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


# --------------------------------------------------------------------------
# 通用部件（批内复用，保证同族观感一致）
# --------------------------------------------------------------------------

def _box(g, x1, x2, ybot, ytop, weight=W_MAIN, vweight=None):
    """方框：x1/x2 与 ybot/ytop 都是**墨迹边缘**，内白自动成洞。"""
    vw = weight if vweight is None else vweight
    g.hbar(x1, x2, ytop - weight / 2.0, weight=weight)
    g.hbar(x1, x2, ybot + weight / 2.0, weight=weight)
    g.vbar(x1 + vw / 2.0, ybot, ytop, weight=vw)
    g.vbar(x2 - vw / 2.0, ybot, ytop, weight=vw)


def _person(g):
    """亻：撇 + 竖（左侧偏旁）。"""
    g.diag(300, 800, 150, 540, weight=W_SEC)
    g.vbar(210, 600, 0, weight=W_SEC)


def _gyoninben(g):
    """彳：撇 + 撇 + 竖（两撇不相接，各留白口）。"""
    g.diag(310, 800, 185, 665, weight=W_SEC)
    g.diag(265, 585, 125, 440, weight=W_SEC)
    g.vbar(200, 520, 0, weight=W_SEC)


def _tehen(g):
    """扌：一 + 竖 + 提（提的斜率固定）。"""
    g.hbar(70, 350, 540, weight=W_SEC)
    g.vbar(210, 790, 60, weight=W_SEC)
    g.diag(80, 250, 340, 400, weight=W_SEC)


def _ozato(g):
    """阝（阜字旁）：竖 + 横 + 折 + 弯钩。"""
    g.vbar(130, 790, 0, weight=W_SEC)
    g.hbar(130, 300, 772, weight=W_SEC)
    g.vbar(300, 772, 630, weight=W_SEC)
    g.diag(300, 630, 340, 500, weight=W_THIN)
    g.diag(340, 500, 160, 430, weight=W_THIN)


# --------------------------------------------------------------------------
# 24 字
# --------------------------------------------------------------------------

def _kill(g):
    """殺：左「乂 + 木」，右「殳（几 + 又）」。

    乂 占左上（y 640..790），木 占左下（横 500），殳 占右整列。
    """
    # 乂（两斜画交叉成 X，夹角约 82°，不并成黑块）
    g.diag(170, 770, 340, 620, weight=W_SEC)
    g.diag(340, 770, 170, 620, weight=W_SEC)
    # 木
    g.hbar(100, 440, 500, weight=W_MAIN)
    g.vbar(270, 560, 0, weight=W_MAIN)
    g.diag(255, 430, 95, 200, weight=W_SEC)
    g.diag(285, 430, 445, 205, weight=W_SEC)
    # 殳：几
    g.hbar(680, 890, 772, weight=W_SEC)
    g.vbar(890, 772, 560, weight=W_SEC)
    g.diag(700, 772, 615, 585, weight=W_SEC)
    # 殳：又
    g.hbar(560, 880, 500, weight=W_SEC)
    g.diag(880, 500, 575, 145, weight=W_SEC)
    g.diag(660, 500, 900, 135, weight=W_SEC)


def _mei(g):
    """盟：上「明（日 + 月）」，下「皿」。"""
    # 日（两段白口各 59）
    g.hbar(100, 390, 754, weight=W_THIN)
    g.hbar(100, 390, 611, weight=W_THIN)
    g.hbar(100, 390, 468, weight=W_THIN)
    g.vbar(148, 426, 796, weight=W_SEC)
    g.vbar(342, 426, 796, weight=W_SEC)
    # 月
    g.hbar(460, 880, 748, weight=W_THIN)
    g.hbar(460, 880, 606, weight=W_THIN)
    g.hbar(460, 880, 466, weight=W_THIN)
    g.vbar(508, 418, 796, weight=W_SEC)
    g.vbar(832, 418, 796, weight=W_SEC)
    # 皿（密排：横降到 84 档）
    g.hbar(120, 880, 300, weight=W_THIN)
    g.hbar(120, 880, 42, weight=W_THIN)
    g.vbar(166, 0, 348, weight=W_SEC)
    g.vbar(380, 0, 348, weight=W_SEC)
    g.vbar(620, 0, 348, weight=W_SEC)
    g.vbar(834, 0, 348, weight=W_SEC)


def _za(g):
    """座：外「广」（点 0 档 + 横 + 撇），内「坐＝人 + 人 + 土」。"""
    # 广
    g.dot(500, 772, w=W_SEC, h=96, slant=0)
    g.hbar(120, 900, 700, weight=W_MAIN)
    g.diag(165, 700, 85, 90, weight=W_SEC)
    # 坐：两个人
    g.diag(320, 620, 215, 400, weight=W_SEC)
    g.diag(285, 520, 410, 395, weight=W_SEC)
    g.diag(720, 620, 615, 400, weight=W_SEC)
    g.diag(685, 520, 810, 395, weight=W_SEC)
    # 坐：土
    g.hbar(280, 720, 290, weight=W_SEC)
    g.vbar(500, 350, 90, weight=W_SEC)
    g.hbar(200, 800, 48, weight=W_SEC)


def _ha(g):
    """破：左「石（一 + 撇 + 口）」，右「皮（乛 + 撇 + 竖 + 又）」。"""
    # 石
    g.hbar(70, 430, 740, weight=W_MAIN)
    g.diag(255, 700, 140, 390, weight=W_SEC)
    _box(g, 120, 400, 40, 380, weight=W_MAIN)
    # 皮
    g.hbar(490, 880, 740, weight=W_SEC)
    g.diag(610, 760, 470, 420, weight=W_SEC)
    g.vbar(690, 740, 390, weight=W_SEC)
    g.hbar(530, 860, 350, weight=W_SEC)
    g.diag(860, 350, 520, 90, weight=W_SEC)
    g.diag(650, 350, 890, 100, weight=W_SEC)


def _sou(g):
    """捜：左「扌」，右「叟＝臼（带中竖）+ 又」。"""
    _tehen(g)
    # 臼（框内白口 ≥ 24）
    g.hbar(468, 922, 748, weight=W_THIN)
    g.hbar(468, 922, 472, weight=W_THIN)
    g.vbar(510, 430, 790, weight=W_THIN)
    g.vbar(880, 430, 790, weight=W_THIN)
    g.hbar(510, 660, 610, weight=W_THIN)
    g.vbar(660, 330, 790, weight=W_THIN)
    # 又
    g.hbar(500, 880, 290, weight=W_SEC)
    g.diag(880, 290, 520, 60, weight=W_SEC)
    g.diag(640, 290, 900, 60, weight=W_SEC)


def _jo(g):
    """除：左「阝」，右「余（人 + 二 + 小）」。"""
    _ozato(g)
    # 人
    g.diag(620, 815, 490, 670, weight=W_SEC)
    g.diag(615, 740, 755, 670, weight=W_SEC)
    # 余：二 + 小
    g.hbar(470, 790, 570, weight=W_SEC)
    g.hbar(430, 840, 450, weight=W_SEC)
    g.vbar(640, 560, 110, weight=W_SEC)
    g.diag(600, 420, 460, 220, weight=W_THIN)
    g.dot(790, 300, w=W_THIN, h=96, slant=-14)


def _kou(g):
    """降：左「阝」，右「夅＝夂 + 一 + 丨 + 八」。"""
    _ozato(g)
    # 夂
    g.diag(660, 810, 520, 650, weight=W_SEC)
    g.hbar(620, 870, 720, weight=W_SEC)
    g.diag(870, 720, 600, 580, weight=W_SEC)
    g.diag(760, 690, 900, 610, weight=W_SEC)
    # 一 + 丨 + 八
    g.hbar(480, 890, 460, weight=W_SEC)
    g.vbar(680, 500, 200, weight=W_SEC)
    g.diag(640, 380, 490, 180, weight=W_THIN)
    g.dot(800, 280, w=W_THIN, h=96, slant=-14)


def _cho(g):
    """超：左「走（土 + 龰）」，右上「召（刀 + 口）」，底部走字底横贯全宽。"""
    # 走
    g.hbar(120, 380, 740, weight=W_MAIN)
    g.vbar(250, 800, 570, weight=W_MAIN)
    g.hbar(70, 430, 570, weight=W_MAIN)
    g.vbar(175, 570, 280, weight=W_SEC)
    g.diag(180, 470, 90, 350, weight=W_THIN)
    g.diag(270, 440, 430, 300, weight=W_SEC)
    g.hbar(60, 940, 250, weight=W_MAIN)
    # 召：刀
    g.hbar(560, 900, 760, weight=W_SEC)
    g.vbar(900, 760, 640, weight=W_SEC)
    g.diag(700, 760, 570, 610, weight=W_SEC)
    # 召：口
    _box(g, 570, 880, 360, 600, weight=W_MAIN)


def _seki(g):
    """責：上「龶（三横 + 竖）」，下「貝（目 + 八）」。"""
    # 龶
    g.hbar(200, 800, 770, weight=W_MAIN)
    g.vbar(500, 800, 600, weight=W_MAIN)
    g.hbar(250, 750, 650, weight=W_THIN)
    g.hbar(170, 830, 540, weight=W_THIN)
    # 貝：目（四横 84，三段白口各 26）
    g.hbar(250, 750, 428, weight=W_THIN)
    g.hbar(250, 750, 318, weight=W_THIN)
    g.hbar(250, 750, 208, weight=W_THIN)
    g.hbar(250, 750, 98, weight=W_THIN)
    g.vbar(296, 56, 470, weight=W_SEC)
    g.vbar(704, 56, 470, weight=W_SEC)
    # 八
    g.diag(255, 120, 180, 30, weight=W_THIN)
    g.dot(800, 50, w=W_THIN, h=90, slant=-14)


def _ju(g):
    """従：左「彳」，右上「从（人 + 人）」，右下「止」。"""
    _gyoninben(g)
    # 从
    g.diag(490, 810, 380, 660, weight=W_THIN)
    g.diag(465, 730, 555, 650, weight=W_THIN)
    g.diag(760, 810, 650, 660, weight=W_THIN)
    g.diag(735, 730, 850, 640, weight=W_THIN)
    # 止
    g.vbar(680, 560, 120, weight=W_SEC)
    g.hbar(680, 880, 400, weight=W_THIN)
    g.vbar(500, 400, 120, weight=W_THIN)
    g.hbar(420, 900, 90, weight=W_SEC)


def _shu(g):
    """修：左「亻」，中「丨」，右上「夂」，右下「彡」。"""
    _person(g)
    g.vbar(360, 800, 480, weight=W_SEC)
    # 夂
    g.diag(530, 810, 430, 640, weight=W_THIN)
    g.hbar(520, 880, 700, weight=W_THIN)
    g.diag(880, 700, 600, 570, weight=W_THIN)
    g.diag(650, 690, 900, 600, weight=W_THIN)
    # 彡
    g.diag(900, 540, 620, 380, weight=W_THIN)
    g.diag(900, 380, 620, 220, weight=W_THIN)
    g.diag(900, 220, 620, 60, weight=W_THIN)


def _ho(g):
    """捕：左「扌」，右「甫（十 + 丶 + 用）」。"""
    _tehen(g)
    # 十 + 丶
    g.hbar(450, 820, 740, weight=W_SEC)
    g.vbar(680, 800, 620, weight=W_SEC)
    g.dot(870, 770, w=W_THIN, h=88, slant=-14)
    # 用
    g.hbar(454, 932, 590, weight=W_SEC)
    g.hbar(454, 932, 440, weight=W_THIN)
    g.hbar(454, 932, 280, weight=W_THIN)
    g.vbar(500, 100, 636, weight=W_SEC)
    g.vbar(886, 100, 636, weight=W_SEC)
    g.vbar(680, 100, 636, weight=W_SEC)


def _tai(g):
    """隊：左「阝」，右「㒸＝丷 + 豕」。"""
    _ozato(g)
    # 丷
    g.dot(680, 765, w=W_THIN, h=96, slant=-14)
    g.dot(840, 765, w=W_THIN, h=96, slant=14)
    # 豕
    g.hbar(430, 900, 650, weight=W_SEC)
    g.diag(700, 630, 630, 160, weight=W_SEC)
    g.diag(585, 580, 425, 460, weight=W_THIN)
    g.diag(560, 440, 390, 305, weight=W_THIN)
    g.diag(535, 300, 390, 165, weight=W_THIN)
    g.diag(760, 620, 905, 415, weight=W_SEC)


def _sai(g):
    """採：左「扌」，右上「爫」，右下「木」。"""
    _tehen(g)
    # 爫（撇 + 三点，点列与撇同斜率，白口 ≥ 30）
    g.diag(870, 730, 630, 680, weight=W_THIN)
    g.dot(650, 565, w=W_THIN, h=92, slant=-14)
    g.dot(755, 587, w=W_THIN, h=92, slant=-14)
    g.dot(860, 609, w=W_THIN, h=92, slant=14)
    # 木
    g.hbar(440, 930, 440, weight=W_SEC)
    g.vbar(690, 510, 60, weight=W_SEC)
    g.diag(670, 375, 470, 140, weight=W_THIN)
    g.diag(710, 375, 905, 150, weight=W_SEC)


def _mori(g):
    """森：上「木」，下「林（木 + 木）」。"""
    # 上木
    g.hbar(330, 670, 740, weight=W_SEC)
    g.vbar(500, 820, 600, weight=W_SEC)
    g.diag(480, 670, 330, 470, weight=W_THIN)
    g.diag(520, 670, 670, 470, weight=W_THIN)
    # 下林：左木
    g.hbar(80, 460, 340, weight=W_SEC)
    g.vbar(270, 440, 0, weight=W_SEC)
    g.diag(250, 300, 90, 110, weight=W_THIN)
    g.diag(290, 300, 450, 120, weight=W_THIN)
    # 下林：右木
    g.hbar(510, 930, 340, weight=W_SEC)
    g.vbar(720, 440, 0, weight=W_SEC)
    g.diag(700, 300, 540, 110, weight=W_THIN)
    g.diag(740, 300, 900, 120, weight=W_THIN)


def _shin(g):
    """振：左「扌」，右「辰（厂 + 二 + 竖提 + 撇捺）」。"""
    _tehen(g)
    # 厂
    g.hbar(430, 920, 740, weight=W_SEC)
    g.diag(505, 740, 425, 430, weight=W_SEC)
    # 二
    g.hbar(480, 850, 620, weight=W_THIN)
    g.hbar(470, 890, 490, weight=W_THIN)
    # 下部
    g.vbar(680, 620, 230, weight=W_SEC)
    g.diag(680, 250, 790, 300, weight=W_THIN)
    g.diag(650, 400, 480, 160, weight=W_THIN)
    g.diag(710, 400, 900, 170, weight=W_SEC)


def _kyu(g):
    """給：左「糸（幺 + 小）」，右「合（人 + 一 + 口）」。"""
    # 糸
    g.diag(280, 800, 165, 655, weight=W_THIN)
    g.hbar(165, 300, 655, weight=W_THIN)
    g.diag(300, 640, 175, 495, weight=W_THIN)
    g.hbar(175, 310, 495, weight=W_THIN)
    g.vbar(240, 470, 0, weight=W_SEC)
    g.dot(125, 250, w=W_THIN, h=100, slant=-14)
    g.dot(350, 250, w=W_THIN, h=100, slant=14)
    # 合
    g.diag(640, 810, 500, 660, weight=W_SEC)
    g.diag(625, 730, 770, 665, weight=W_SEC)
    g.hbar(490, 790, 600, weight=W_THIN)
    _box(g, 490, 880, 120, 480, weight=W_MAIN)


def _ne(g):
    """根：左「木」，右「艮（日 + 竖提 + 撇捺）」。"""
    # 木
    g.hbar(70, 420, 560, weight=W_MAIN)
    g.vbar(250, 640, 0, weight=W_MAIN)
    g.diag(230, 480, 80, 220, weight=W_SEC)
    g.diag(270, 480, 425, 230, weight=W_SEC)
    # 艮
    g.hbar(500, 880, 740, weight=W_SEC)
    g.hbar(500, 880, 570, weight=W_THIN)
    g.hbar(500, 880, 460, weight=W_THIN)
    g.vbar(880, 740, 430, weight=W_SEC)
    g.vbar(500, 786, 150, weight=W_SEC)
    g.diag(520, 160, 680, 250, weight=W_THIN)
    g.diag(760, 400, 600, 140, weight=W_THIN)
    g.diag(790, 400, 900, 190, weight=W_SEC)


def _shuu(g):
    """就：左「京（亠 + 口 + 小）」，右「尤」。"""
    # 京
    g.dot(300, 770, w=W_SEC, h=96, slant=0)
    g.hbar(80, 520, 690, weight=W_SEC)
    _box(g, 150, 450, 360, 620, weight=W_MAIN)
    g.vbar(300, 330, 60, weight=W_SEC)
    g.dot(140, 200, w=W_THIN, h=100, slant=-14)
    g.dot(460, 200, w=W_THIN, h=100, slant=14)
    # 尤
    g.hbar(580, 900, 690, weight=W_SEC)
    g.dot(880, 770, w=W_THIN, h=100, slant=-14)
    g.diag(740, 700, 570, 180, weight=W_SEC)
    g.vbar(700, 700, 90, weight=W_SEC)
    g.hbar(700, 890, 90, weight=W_SEC)


def _han(g):
    """販：左「貝」，右「反（厂 + 又）」。"""
    # 貝
    g.hbar(80, 430, 472, weight=W_THIN)
    g.hbar(80, 430, 362, weight=W_THIN)
    g.hbar(80, 430, 252, weight=W_THIN)
    g.hbar(80, 430, 142, weight=W_THIN)
    g.vbar(126, 100, 514, weight=W_SEC)
    g.vbar(384, 100, 514, weight=W_SEC)
    g.diag(120, 110, 40, 30, weight=W_THIN)
    g.dot(400, 55, w=W_THIN, h=90, slant=-14)
    # 反
    g.hbar(470, 900, 740, weight=W_SEC)
    g.diag(505, 740, 450, 420, weight=W_SEC)
    g.hbar(520, 880, 380, weight=W_SEC)
    g.diag(880, 380, 540, 60, weight=W_SEC)
    g.diag(650, 380, 900, 80, weight=W_SEC)


def _en(g):
    """園：外「囗」，内「袁（士 + 口 + 𧘇）」。"""
    # 囗
    g.hbar(60, 940, 778, weight=W_THIN)
    g.hbar(60, 940, 42, weight=W_THIN)
    g.vbar(108, 0, 820, weight=W_SEC)
    g.vbar(892, 0, 820, weight=W_SEC)
    # 袁：士
    g.hbar(240, 760, 662, weight=W_THIN)
    g.hbar(280, 720, 550, weight=W_THIN)
    g.vbar(500, 715, 570, weight=W_THIN)
    # 袁：口
    _box(g, 330, 670, 214, 434, weight=W_THIN)
    # 袁：𧘇
    g.diag(410, 250, 290, 130, weight=W_THIN)
    g.vbar(500, 250, 110, weight=W_THIN)
    g.diag(600, 250, 790, 120, weight=W_SEC)


def _i(g):
    """異：上「田」，下「共（廿 + 八）」。"""
    # 田
    g.hbar(200, 800, 778, weight=W_THIN)
    g.hbar(200, 800, 666, weight=W_THIN)
    g.hbar(200, 800, 538, weight=W_THIN)
    g.vbar(246, 496, 820, weight=W_SEC)
    g.vbar(500, 496, 820, weight=W_SEC)
    g.vbar(754, 496, 820, weight=W_SEC)
    # 共
    g.hbar(230, 770, 420, weight=W_SEC)
    g.hbar(140, 860, 246, weight=W_SEC)
    g.vbar(360, 480, 250, weight=W_SEC)
    g.vbar(640, 480, 250, weight=W_SEC)
    g.diag(320, 200, 170, 30, weight=W_THIN)
    g.diag(690, 200, 845, 30, weight=W_SEC)


def _ji(g):
    """辞：左「舌（丿 + 一 + 丨 + 口）」，右「辛（亠 + 丷 + 一 + 十）」。"""
    # 舌
    g.diag(430, 790, 250, 720, weight=W_THIN)
    g.hbar(190, 470, 680, weight=W_SEC)
    g.vbar(330, 700, 374, weight=W_SEC)
    _box(g, 200, 460, 80, 420, weight=W_MAIN)
    # 辛
    g.dot(730, 770, w=W_SEC, h=96, slant=0)
    g.hbar(560, 900, 690, weight=W_SEC)
    g.dot(670, 580, w=W_THIN, h=80, slant=-14)
    g.dot(810, 580, w=W_THIN, h=80, slant=14)
    g.hbar(560, 900, 470, weight=W_THIN)
    g.hbar(520, 940, 350, weight=W_SEC)
    g.vbar(730, 500, 60, weight=W_SEC)


def _sho(g):
    """将：左「丬」，右上「爫」，右下「寸」。"""
    # 丬
    g.vbar(300, 780, 0, weight=W_SEC)
    g.dot(170, 700, w=W_THIN, h=100, slant=-14)
    g.hbar(70, 300, 250, weight=W_SEC)
    # 爫（与採同一套骨架：撇 + 三点同斜率）
    g.diag(900, 745, 660, 695, weight=W_THIN)
    g.dot(680, 580, w=W_THIN, h=92, slant=-14)
    g.dot(785, 602, w=W_THIN, h=92, slant=-14)
    g.dot(890, 624, w=W_THIN, h=92, slant=14)
    # 寸
    g.hbar(420, 930, 420, weight=W_SEC)
    g.vbar(700, 480, 60, weight=W_SEC)
    g.dot(510, 300, w=W_THIN, h=96, slant=-14)


# 清单：(字形名, 码位, note, 造字函数)，顺序即字符清单顺序。
_SPECS = [
    ("uni6BBA", 0x6BBA, "殺：乂＋木＋殳", _kill),
    ("uni76DF", 0x76DF, "盟：明＋皿", _mei),
    ("uni5EA7", 0x5EA7, "座：广＋坐", _za),
    ("uni7834", 0x7834, "破：石＋皮", _ha),
    ("uni635C", 0x635C, "捜：扌＋叟", _sou),
    ("uni9664", 0x9664, "除：阝＋余", _jo),
    ("uni964D", 0x964D, "降：阝＋夅", _kou),
    ("uni8D85", 0x8D85, "超：走＋召", _cho),
    ("uni8CAC", 0x8CAC, "責：龶＋貝", _seki),
    ("uni5F93", 0x5F93, "従：彳＋从＋止", _ju),
    ("uni4FEE", 0x4FEE, "修：亻＋丨＋夂＋彡", _shu),
    ("uni6355", 0x6355, "捕：扌＋甫", _ho),
    ("uni968A", 0x968A, "隊：阝＋㒸", _tai),
    ("uni63A1", 0x63A1, "採：扌＋采", _sai),
    ("uni68EE", 0x68EE, "森：木＋林", _mori),
    ("uni632F", 0x632F, "振：扌＋辰", _shin),
    ("uni7D66", 0x7D66, "給：糸＋合", _kyu),
    ("uni6839", 0x6839, "根：木＋艮", _ne),
    ("uni5C31", 0x5C31, "就：京＋尤", _shuu),
    ("uni8CA9", 0x8CA9, "販：貝＋反", _han),
    ("uni5712", 0x5712, "園：囗＋袁", _en),
    ("uni7570", 0x7570, "異：田＋共", _i),
    ("uni8F9E", 0x8F9E, "辞：舌＋辛", _ji),
    ("uni5C06", 0x5C06, "将：丬＋爫＋寸", _sho),
]


def build() -> list[Glyph]:
    """按清单顺序建出 24 个字形（每个字形在此处完成全部笔画）。"""
    glyphs = []
    for name, code, note, fn in _SPECS:
        g = Glyph(name, advance=1000, unicode=code, note=note)
        fn(g)
        glyphs.append(g)
    return glyphs


def target_ufo() -> Path:
    return FONT_SRC / "masters" / "hkposter-joyo-w2-s3-008.ufo"


if __name__ == "__main__":
    write_ufo(target_ufo(), build())
    print(f"[recipe] 已写出 {target_ufo()}")
