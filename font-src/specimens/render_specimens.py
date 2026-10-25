"""render_specimens — HK Poster Heavy Wave 0 样张生成器（参数化）。

本脚本只做「样张层」的事：把已构建的字体渲染成设计评审用的 PNG。
霓虹 / 描边 / 配色效果只存在于本脚本的输出里，**字体轮廓本身不含任何特效**
（见 font-src/CONTRACT.md §8「霓虹/描边/金属/旧化纹理进入字体轮廓」为失败项）。

用法
----
    # 一次生成全部标准样张（黑白 48/96/192 + 效果组 + 英文标题行）
    python font-src/specimens/render_specimens.py --all --outdir font-src/specimens

    # 单张、任意参数（改 --text/--size/--fg/--bg 即可重跑）
    python font-src/specimens/render_specimens.py \
        --font font-src/dist/HKPoster-Heavy.ttf \
        --text "港影龍義" --size 96 --fg "#000000" --bg "#FFFFFF" \
        --out font-src/specimens/custom.png

缺字策略（docs/06 §4）
---------------------
脚本逐字读取字体 cmap：字体里**没有**的字符一律用系统回退字体渲染，
并以洋红色字形 + 洋红虚线下划线标出，页脚列出全部缺字字符。
绝不拿系统字体冒充自有字体。缺字清单随每次运行重新计算，
集成方用合并后的完整字体重跑本脚本即可得到「零缺字」的最终样张。
"""

from __future__ import annotations

import argparse
import hashlib
import os
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

if hasattr(sys, "stdout") and sys.stdout.reconfigure:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = Path(__file__).resolve().parent
FONT_SRC = HERE.parent

# ---------------------------------------------------------------------------
# 样张内容（契约 §5：specimens lane 必须覆盖的字符集）
# ---------------------------------------------------------------------------

# 单字：12 个高信息量代表汉字（cjk-core 6 个 + cjk-dense 6 个）
SINGLE_CHARS = "港影城火夜風龍義警愛無道"

# 双字
DOUBLE_WORDS = ["龍城", "夜行", "風暴"]

# 四字
FOUR_WORDS = ["英雄本色", "旺角風雲", "霓虹之夜", "黑夜追擊"]

# 英文标题行
LATIN_TITLES = ["CITY OF SHADOWS", "LAST BULLET", "1997", "HONG KONG"]

# 日文：假名（平 + 片）与日文标题行（Wave 1 起）
KANA_HIRAGANA = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"
KANA_KATAKANA = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
KANA_VOICED = "がぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ"
KANA_TITLES = ["ひらがな カタカナ", "东京 夜行", "ゲーム タイトル", "映画 タイトル 1997"]

# 缺字标记色（洋红：在白底、黑底、红字、黄字四种底色上都可辨）
FALLBACK_COLOR = "#E0249B"

# ---------------------------------------------------------------------------
# 配色预设
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Preset:
    name: str
    label: str
    fg: str
    bg: str
    stroke_fg: str | None = None
    stroke_width: float = 0.0  # 单位：em


PRESET_MONO = Preset("mono", "单色黑白 Mono B/W", "#000000", "#FFFFFF")
PRESET_EFFECT_RED = Preset("effect-red", "效果组·红字黑底", "#F0262C", "#000000")
PRESET_EFFECT_YELLOW = Preset(
    "effect-yellow", "效果组·黄字红边", "#FFD400", "#000000", "#E01B24", 0.035
)


# ---------------------------------------------------------------------------
# 字体载入
# ---------------------------------------------------------------------------


def _font_dir() -> Path:
    root = os.environ.get("WINDIR", r"C:\Windows")
    return Path(root) / "Fonts"


def _first_existing(names: list[str]) -> Path | None:
    for name in names:
        candidate = _font_dir() / name
        if candidate.exists():
            return candidate
    return None


def _truetype(path: Path, size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size, index=index)


@dataclass
class FontBundle:
    """样张用到的所有字体实例。"""

    main: ImageFont.FreeTypeFont
    ui: ImageFont.FreeTypeFont
    ui_small: ImageFont.FreeTypeFont
    fb_cjk: ImageFont.FreeTypeFont
    fb_latin: ImageFont.FreeTypeFont
    ascent_px: float
    descent_px: float
    em_px: float


def load_bundle(font_path: Path, size: int) -> FontBundle:
    tt = TTFont(str(font_path), fontNumber=0, lazy=True)
    upm = tt["head"].unitsPerEm
    hhea = tt["hhea"]
    ascent_px = hhea.ascent * size / upm
    descent_px = abs(hhea.descent) * size / upm
    em_px = (hhea.ascent - hhea.descent) * size / upm
    tt.close()

    main = _truetype(font_path, size)

    ui_path = _first_existing(["msyh.ttc", "msyhbd.ttc", "segoeui.ttf", "arial.ttf"])
    ui_bold_path = _first_existing(["msyhbd.ttc", "segoeuib.ttf", "arialbd.ttf"])
    ui = _truetype(ui_path, max(11, int(size * 0.16))) if ui_path else ImageFont.load_default()
    ui_bold = (
        _truetype(ui_bold_path, max(13, int(size * 0.22)))
        if ui_bold_path
        else ui
    )
    ui_small = _truetype(ui_path, max(10, int(size * 0.135))) if ui_path else ImageFont.load_default()

    fb_cjk_path = _first_existing(["msyh.ttc", "NotoSansSC-VF.ttf", "simhei.ttf"])
    fb_latin_path = _first_existing(["segoeui.ttf", "arial.ttf"])
    fb_cjk = _truetype(fb_cjk_path, size) if fb_cjk_path else ui
    fb_latin = _truetype(fb_latin_path, size) if fb_latin_path else ui

    bundle = FontBundle(
        main=main,
        ui=ui_bold,
        ui_small=ui_small,
        fb_cjk=fb_cjk,
        fb_latin=fb_latin,
        ascent_px=ascent_px,
        descent_px=descent_px,
        em_px=em_px,
    )
    return bundle


# ---------------------------------------------------------------------------
# 覆盖检测
# ---------------------------------------------------------------------------


def font_coverage(font_path: Path) -> set[int]:
    tt = TTFont(str(font_path), fontNumber=0, lazy=True)
    cmap = tt.getBestCmap() or {}
    coverage = set(cmap.keys())
    tt.close()
    return coverage


def is_cjk(ch: str) -> bool:
    return unicodedata.east_asian_width(ch) in ("W", "F")


def is_blank(ch: str) -> bool:
    return ch.isspace()


# ---------------------------------------------------------------------------
# 排版上下文
# ---------------------------------------------------------------------------


@dataclass
class Specimen:
    font_path: Path
    size: int
    fg: str
    bg: str
    columns: int
    tracking: float  # 单位：em
    stroke_fg: str | None
    stroke_width: float  # 单位：em
    coverage: set[int]
    bundle: FontBundle
    fallback_font: Path | None = None
    title: str = ""

    def has_glyph(self, ch: str) -> bool:
        if is_blank(ch):
            return True  # 空白不参与缺字判定
        return ord(ch) in self.coverage

    def font_for(self, ch: str):
        """返回 (字体实例, 是否缺字回退)。"""
        if self.has_glyph(ch):
            return self.bundle.main, False
        if self.fallback_font is not None:
            return _truetype(self.fallback_font, self.size), True
        if is_cjk(ch):
            return self.bundle.fb_cjk, True
        return self.bundle.fb_latin, True


# ---------------------------------------------------------------------------
# 绘制小工具
# ---------------------------------------------------------------------------


def dashed_line(draw, x0, y0, x1, y1, color, dash=6, width=1) -> None:
    length = x1 - x0
    if length <= 0:
        return
    pos = 0.0
    while pos < length:
        seg = min(float(dash), length - pos)
        draw.line([x0 + pos, y0, x0 + pos + seg, y1], fill=color, width=width)
        pos += dash * 2


def dashed_rect(draw, box, color, dash=6, width=1) -> None:
    x0, y0, x1, y1 = box
    dashed_line(draw, x0, y0, x1, y0, color, dash, width)
    dashed_line(draw, x0, y1, x1, y1, color, dash, width)
    dashed_line(draw, x0, y0, x0, y1, color, dash, width)
    dashed_line(draw, x1, y0, x1, y1, color, dash, width)


def runs_of(spec: Specimen, text: str) -> list[tuple[str, ImageFont.FreeTypeFont, bool]]:
    """把文字切成 (片段, 字体, 是否缺字) 的连续段。

    同一段用同一字体整段绘制 —— 保留字体自身的 kerning（GSUB/GPOS）。
    """
    runs: list[tuple[str, ImageFont.FreeTypeFont, bool]] = []
    for ch in text:
        font, missing = spec.font_for(ch)
        if runs and runs[-1][1] is font and runs[-1][2] == missing:
            runs[-1] = (runs[-1][0] + ch, font, missing)
        else:
            runs.append((ch, font, missing))
    return runs


def measure_row(draw, spec: Specimen, text: str) -> float:
    total = 0.0
    tracking_px = spec.tracking * spec.size
    runs = runs_of(spec, text)
    for index, (segment, font, _missing) in enumerate(runs):
        total += draw.textlength(segment, font=font)
        if index < len(runs) - 1:
            total += tracking_px
    return total


def draw_row(
    draw,
    spec: Specimen,
    x: float,
    baseline: float,
    text: str,
    fg: str,
    mark_missing: bool = True,
) -> tuple[float, list[tuple[float, float]]]:
    """在基线 baseline 处绘制一行文字，返回 (结束 x, 缺字片段的 (x0, x1) 列表)。"""
    tracking_px = spec.tracking * spec.size
    stroke_w = max(1, int(round(spec.stroke_width * spec.size))) if spec.stroke_fg else 0
    missing_spans: list[tuple[float, float]] = []
    cursor = x
    for segment, font, missing in runs_of(spec, text):
        if spec.tracking == 0.0:
            width = draw.textlength(segment, font=font)
            draw.text(
                (cursor, baseline),
                segment,
                font=font,
                fill=FALLBACK_COLOR if missing else fg,
                anchor="ls",
                stroke_width=stroke_w,
                stroke_fill=spec.stroke_fg,
            )
            cursor += width
        else:
            # 非零字距时逐字绘制（此时不套用字体自身 kerning）
            for ch in segment:
                width = draw.textlength(ch, font=font)
                draw.text(
                    (cursor, baseline),
                    ch,
                    font=font,
                    fill=FALLBACK_COLOR if missing else fg,
                    anchor="ls",
                    stroke_width=stroke_w,
                    stroke_fill=spec.stroke_fg,
                )
                cursor += width + tracking_px
            cursor -= tracking_px
        if missing and mark_missing:
            missing_spans.append((cursor - draw.textlength(segment, font=font), cursor))
        cursor += tracking_px if spec.tracking == 0.0 and len(segment) else 0.0
    return cursor, missing_spans


# ---------------------------------------------------------------------------
# 样张内容区块
# ---------------------------------------------------------------------------


@dataclass
class Block:
    title: str
    kind: str  # "grid" | "lines"
    items: list[str]
    cell: float = 0.0
    line_height: float = 0.0


def punctuation_of(coverage: set[int]) -> list[str]:
    """取 cmap 中的标点字形（用于展示字体里真正已有的字形）。"""
    chars = []
    for cp in sorted(coverage):
        ch = chr(cp)
        if unicodedata.category(ch).startswith("P"):
            chars.append(ch)
    return chars


def build_blocks(spec: Specimen, preset_name: str, custom_text: str | None) -> list[Block]:
    size = spec.size
    blocks: list[Block] = []

    if custom_text is not None:
        items = [line for line in custom_text.split("\n") if line != ""]
        blocks.append(
            Block(
                title="自定义文本 Custom text",
                kind="lines",
                items=items,
                line_height=spec.bundle.em_px,
            )
        )
        return blocks

    if preset_name == "latin":
        blocks.append(
            Block(
                title="D · 英文标题行 English titles",
                kind="lines",
                items=list(LATIN_TITLES),
                line_height=spec.bundle.em_px,
            )
        )
        return blocks

    if preset_name == "kana":
        blocks.append(
            Block(
                title="F · 平假名 Hiragana",
                kind="grid",
                items=list(KANA_HIRAGANA),
                cell=size * 1.0,
            )
        )
        blocks.append(
            Block(
                title="G · 片假名 Katakana",
                kind="grid",
                items=list(KANA_KATAKANA),
                cell=size * 1.0,
            )
        )
        blocks.append(
            Block(
                title="H · 带浊音假名 Voiced kana",
                kind="grid",
                items=list(KANA_VOICED),
                cell=size * 1.0,
            )
        )
        blocks.append(
            Block(
                title="I · 日文标题行 Japanese titles",
                kind="lines",
                items=list(KANA_TITLES),
                line_height=spec.bundle.em_px,
            )
        )
        return blocks

    blocks.append(
        Block(
            title="A · 单字 Single characters",
            kind="grid",
            items=list(SINGLE_CHARS),
            cell=size * 1.15,
        )
    )
    blocks.append(
        Block(
            title="B · 双字 Double characters",
            kind="lines",
            items=list(DOUBLE_WORDS),
            line_height=spec.bundle.em_px,
        )
    )
    blocks.append(
        Block(
            title="C · 四字 Four characters",
            kind="lines",
            items=list(FOUR_WORDS),
            line_height=spec.bundle.em_px,
        )
    )
    blocks.append(
        Block(
            title="D · 英文标题行 English titles",
            kind="lines",
            items=list(LATIN_TITLES),
            line_height=spec.bundle.em_px,
        )
    )

    puncts = punctuation_of(spec.coverage)
    if puncts:
        blocks.append(
            Block(
                title="E · 字体内已有的标点字形 Punctuation (present in font)",
                kind="grid",
                items=puncts,
                cell=size * 1.05,
            )
        )
    return blocks


# ---------------------------------------------------------------------------
# 样张渲染
# ---------------------------------------------------------------------------


def render_specimen(spec: Specimen, blocks: list[Block], meta_lines: list[str]) -> Image.Image:
    bundle = spec.bundle
    size = spec.size
    pad = max(18, int(size * 0.45))
    gap = size * 0.55
    title_h = size * 0.55
    ui = bundle.ui
    ui_small = bundle.ui_small

    dummy = ImageDraw.Draw(Image.new("RGB", (1, 1)))

    # ---- 测量 ----
    content_w = 0.0
    for block in blocks:
        if block.kind == "grid":
            block_w = block.cell * spec.columns
        else:
            block_w = max((measure_row(dummy, spec, item) for item in block.items), default=0.0)
        content_w = max(content_w, block_w)

    header_h = 0.0
    for line in meta_lines:
        header_h += ui_small.size * 1.35
    header_h += ui.size * 1.5

    body_h = 0.0
    for block in blocks:
        body_h += title_h
        if block.kind == "grid":
            rows = (len(block.items) + spec.columns - 1) // spec.columns
            body_h += rows * size * 1.35
        else:
            body_h += len(block.items) * (block.line_height + size * 0.18)
        body_h += gap

    footer_lines = footer_text(spec, blocks)
    footer_h = 0.0
    for line in footer_lines:
        footer_h += ui_small.size * 1.42

    width = int(content_w + pad * 2)
    height = int(pad + header_h + body_h + footer_h + pad)

    image = Image.new("RGB", (width, height), spec.bg)
    draw = ImageDraw.Draw(image)

    y = float(pad)

    # ---- 页眉 ----
    draw.text((pad, y), spec.title, font=ui, fill=spec.fg)
    y += ui.size * 1.5
    for line in meta_lines:
        draw.text((pad, y), line, font=ui_small, fill="#555555" if spec.bg == "#FFFFFF" else "#BBBBBB")
        y += ui_small.size * 1.35
    rule_y = y + size * 0.12
    draw.line([pad, rule_y, width - pad, rule_y], fill="#999999" if spec.bg == "#FFFFFF" else "#666666")
    y = rule_y + size * 0.3

    # ---- 正文区块 ----
    for block in blocks:
        missing_in_block = [
            ch for item in block.items for ch in item if not spec.has_glyph(ch)
        ]
        title = f"{block.title} — {len(block.items)} 项 / 缺字 {len(set(missing_in_block))}"
        draw.text((pad, y), title, font=ui_small, fill="#444444" if spec.bg == "#FFFFFF" else "#CCCCCC")
        y += title_h

        if block.kind == "grid":
            cell = block.cell
            cell_h = size * 1.35
            for index, item in enumerate(block.items):
                row, column = divmod(index, spec.columns)
                cx = pad + column * cell
                cy = y + row * cell_h
                missing = not spec.has_glyph(item)
                border = FALLBACK_COLOR if missing else ("#DDDDDD" if spec.bg == "#FFFFFF" else "#3A3A3A")
                if missing:
                    dashed_rect(draw, (cx + 1, cy + 1, cx + cell - 1, cy + cell_h - 1), FALLBACK_COLOR)
                else:
                    draw.rectangle([cx + 1, cy + 1, cx + cell - 1, cy + cell_h - 1], outline=border)
                font, _ = spec.font_for(item)
                char_w = draw.textlength(item, font=font)
                tx = cx + (cell - char_w) / 2
                baseline = cy + (cell_h - bundle.em_px) / 2 + bundle.ascent_px
                draw.text(
                    (tx, baseline),
                    item,
                    font=font,
                    fill=FALLBACK_COLOR if missing else spec.fg,
                    anchor="ls",
                    stroke_width=max(1, int(round(spec.stroke_width * size))) if spec.stroke_fg else 0,
                    stroke_fill=spec.stroke_fg,
                )
            rows = (len(block.items) + spec.columns - 1) // spec.columns
            y += rows * cell_h
        else:
            for item in block.items:
                baseline = y + bundle.ascent_px
                _end, spans = draw_row(draw, spec, pad, baseline, item, spec.fg)
                for x0, x1 in spans:
                    underline_y = baseline + bundle.descent_px * 0.55
                    dashed_line(draw, x0, underline_y, x1, underline_y, FALLBACK_COLOR, dash=5)
                y += block.line_height + size * 0.18
        y += gap

    # ---- 页脚 ----
    y += size * 0.1
    rule_y = y
    draw.line([pad, rule_y, width - pad, rule_y], fill="#999999" if spec.bg == "#FFFFFF" else "#666666")
    y += size * 0.22
    for line in footer_lines:
        draw.text((pad, y), line, font=ui_small, fill="#555555" if spec.bg == "#FFFFFF" else "#BBBBBB")
        y += ui_small.size * 1.42

    return image


def footer_text(spec: Specimen, blocks: list[Block]) -> list[str]:
    lines = []
    lines.append(
        "缺字图例：洋红色字形 + 洋红虚线下划线 = 当前字体 cmap 中没有该字符，显示为系统回退字体"
        "（非本字体字形）"
    )
    for block in blocks:
        missing = sorted({ch for item in block.items for ch in item if not spec.has_glyph(ch)})
        if missing:
            lines.append(f"缺字 · {block.title.split(' — ')[0]}：{''.join(missing)}")
    total_missing = sorted(
        {ch for block in blocks for item in block.items for ch in item if not spec.has_glyph(ch)}
    )
    lines.append(
        f"合计缺字 {len(total_missing)} 个：{''.join(total_missing) if total_missing else '（无）'}"
    )
    return lines


# ---------------------------------------------------------------------------
# 单张样张
# ---------------------------------------------------------------------------


def build_one(
    font_path: Path,
    out_path: Path,
    size: int,
    fg: str,
    bg: str,
    columns: int,
    preset: Preset,
    text: str | None = None,
    tracking: float = 0.0,
    stroke_fg: str | None = None,
    stroke_width: float = 0.0,
    title: str | None = None,
) -> tuple[Path, list[str]]:
    coverage = font_coverage(font_path)
    bundle = load_bundle(font_path, size)
    spec = Specimen(
        font_path=font_path,
        size=size,
        fg=fg,
        bg=bg,
        columns=max(1, columns),
        tracking=tracking,
        stroke_fg=stroke_fg,
        stroke_width=stroke_width,
        coverage=coverage,
        bundle=bundle,
        title=title or f"HK Poster Heavy — Wave 0 样张 Specimen · {preset.label}",
    )
    blocks = build_blocks(spec, preset.name, text)

    sample_chars = {ch for block in blocks for item in block.items for ch in item if not is_blank(ch)}
    missing_chars = sorted(ch for ch in sample_chars if not spec.has_glyph(ch))
    sha = hashlib.sha256(font_path.read_bytes()).hexdigest()[:12]
    meta_lines = [
        f"font: {font_path.name} · sha256 {sha} · cmap {len(coverage)} 字符 · "
        f"样张内容 {len(sample_chars)} 字符 / 其中缺字 {len(missing_chars)}",
        f"size: {size} px · fg {fg} · bg {bg} · columns {spec.columns} · "
        f"tracking {tracking} em · 线距 {bundle.em_px:.1f} px (字体 hhea ascent 880 / descent -120)",
        "页眉/页脚/图例使用系统 UI 字体（微软雅黑）；只有样张内容用被测字体渲染。",
    ]
    if spec.stroke_fg:
        meta_lines.append(
            f"样张层特效：描边 {spec.stroke_fg}，描边宽 {stroke_width} em（仅存在于 PNG，不写入字体轮廓）"
        )

    image = render_specimen(spec, blocks, meta_lines)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(out_path)
    return out_path, missing_chars


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="渲染 HK Poster Heavy 样张 PNG（参数化）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--font",
        default=str(FONT_SRC / "dist" / "HKPoster-Heavy.ttf"),
        help="被测字体路径（TTF/OTF/WOFF2）",
    )
    parser.add_argument("--text", default=None, help="自定义样张文字（\\n 分行）；给出后覆盖预设内容")
    parser.add_argument("--size", type=int, default=96, help="正文字号 px")
    parser.add_argument("--out", default=None, help="输出 PNG 路径")
    parser.add_argument("--outdir", default=str(HERE), help="--all 模式的输出目录")
    parser.add_argument("--fg", default=None, help="前景色（默认取预设）")
    parser.add_argument("--bg", default=None, help="背景色（默认取预设）")
    parser.add_argument("--columns", type=int, default=6, help="网格每行格数 / 自定义文本每行字符数")
    parser.add_argument(
        "--preset",
        default="mono",
        choices=["mono", "effect-red", "effect-yellow", "latin"],
        help="样张预设",
    )
    parser.add_argument("--tracking", type=float, default=0.0, help="字距，单位 em（0 = 保留字体自身 kerning）")
    parser.add_argument("--stroke-fg", default=None, help="描边色（覆盖预设）")
    parser.add_argument("--stroke-width", type=float, default=None, help="描边宽，单位 em")
    parser.add_argument("--title", default=None, help="页眉标题")
    parser.add_argument("--all", action="store_true", help="生成全部标准样张")
    return parser.parse_args(argv)


PRESETS = {
    "mono": PRESET_MONO,
    "effect-red": PRESET_EFFECT_RED,
    "effect-yellow": PRESET_EFFECT_YELLOW,
    "latin": Preset("latin", "英文标题行 English titles", "#000000", "#FFFFFF"),
    "kana": Preset("kana", "日文样张 Japanese (kana + titles)", "#000000", "#FFFFFF"),
}

ALL_JOBS = [
    # (文件名, 预设, 字号, 附加参数)
    ("specimen-48.png", "mono", 48, {}),
    ("specimen-96.png", "mono", 96, {}),
    ("specimen-192.png", "mono", 192, {}),
    ("specimen-effect-red.png", "effect-red", 96, {}),
    ("specimen-effect-yellow.png", "effect-yellow", 96, {}),
    ("specimen-latin.png", "latin", 120, {"tracking": 0.0}),
    ("specimen-kana.png", "kana", 96, {}),
]


def run_all(args: argparse.Namespace) -> int:
    font_path = Path(args.font).resolve()
    if not font_path.exists():
        print(f"[specimens] 找不到字体：{font_path}")
        return 1
    outdir = Path(args.outdir).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    for filename, preset_name, size, extra in ALL_JOBS:
        preset = PRESETS[preset_name]
        fg = args.fg or preset.fg
        bg = args.bg or preset.bg
        stroke_fg = args.stroke_fg if args.stroke_fg is not None else preset.stroke_fg
        stroke_width = (
            args.stroke_width if args.stroke_width is not None else preset.stroke_width
        )
        out_path = outdir / filename
        path, missing = build_one(
            font_path=font_path,
            out_path=out_path,
            size=size,
            fg=fg,
            bg=bg,
            columns=args.columns,
            preset=preset,
            text=args.text,
            tracking=extra.get("tracking", args.tracking),
            stroke_fg=stroke_fg,
            stroke_width=stroke_width,
        )
        print(f"[specimens] {path.name}  {size}px  缺字 {len(missing)} 个")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.all:
        return run_all(args)

    font_path = Path(args.font).resolve()
    if not font_path.exists():
        print(f"[specimens] 找不到字体：{font_path}")
        return 1
    preset = PRESETS[args.preset]
    fg = args.fg or preset.fg
    bg = args.bg or preset.bg
    stroke_fg = args.stroke_fg if args.stroke_fg is not None else preset.stroke_fg
    stroke_width = args.stroke_width if args.stroke_width is not None else preset.stroke_width
    out_path = Path(args.out).resolve() if args.out else (HERE / "specimen-custom.png")

    path, missing = build_one(
        font_path=font_path,
        out_path=out_path,
        size=args.size,
        fg=fg,
        bg=bg,
        columns=args.columns,
        preset=preset,
        text=args.text,
        tracking=args.tracking,
        stroke_fg=stroke_fg,
        stroke_width=stroke_width,
        title=args.title,
    )
    with Image.open(path) as img:
        dims = img.size
    print(f"[specimens] {path}  {dims[0]}×{dims[1]} px  缺字 {len(missing)} 个：{''.join(missing)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
