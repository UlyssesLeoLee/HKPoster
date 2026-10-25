"""verify_font — 成品字体的 IT / ST 检查。

用法
----
    python font-src/scripts/verify_font.py --font font-src/dist/HKPoster-Heavy.ttf
    python font-src/scripts/verify_font.py --font font-src/dist/HKPoster-Heavy.ttf --sources font-src/masters

IT（集成）
  * 必需表齐备（TrueType: head/hhea/hmtx/maxp/cmap/name/OS/2/post/glyf/loca）
  * 每个源字形的 Unicode 都能在 cmap 中查到
  * 用 uharfbuzz 真实排版样张串，确认没有 .notdef 兜底

ST（系统）
  * Windows GDI：AddFontResourceExW 真实加载 → CreateFontW/SelectObject →
    GetTextFaceW 读回实际使用的字体名（防止静默替换成系统字体）→
    SetDIBitsToDevice 真实光栅化并落 PNG 证据

退出码：0 = PASS，1 = FAIL
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
FONT_SRC = SCRIPT_DIR.parent
REPO_ROOT = FONT_SRC.parent
sys.path.insert(0, str(SCRIPT_DIR))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

TTF_REQUIRED = {"head", "hhea", "hmtx", "maxp", "cmap", "name", "OS/2", "post", "glyf", "loca"}
OTF_REQUIRED = {"head", "hhea", "hmtx", "maxp", "cmap", "name", "OS/2", "post", "CFF "}


def rel_path(path: Path) -> str:
    """仓库内路径转相对 POSIX 风格；仓库外则原样返回。"""
    try:
        return str(path.relative_to(REPO_ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def source_unicodes(sources: list[Path]) -> dict[int, str]:
    from ufoLib2 import Font

    mapping: dict[int, str] = {}
    for source in sources:
        font = Font.open(str(source))
        for name in font.keys():
            for codepoint in font[name].unicodes:
                mapping[codepoint] = name
    return mapping


def check_tables(font) -> tuple[list[str], list[str]]:
    present = set(font.keys())
    required = TTF_REQUIRED if "glyf" in present else OTF_REQUIRED
    missing = sorted(required - present)
    extra = sorted(present - required)
    return missing, extra


def check_cmap(font, expected: dict[int, str]) -> tuple[list[str], int]:
    from fontTools.ttLib import TTFont

    failures: list[str] = []
    cmap = font.getBestCmap() or {}
    for codepoint, name in sorted(expected.items()):
        if codepoint not in cmap:
            failures.append(f"cmap 缺少 U+{codepoint:04X}（{name}）")
    return failures, len(cmap)


def check_shaping(font_path: Path, cmap) -> tuple[list[str], list[dict]]:
    import uharfbuzz as hb

    failures: list[str] = []
    samples: list[dict] = []
    blob = hb.Blob.from_file_path(str(font_path))
    face = hb.Face(blob)
    font = hb.Font(face)

    notdef = 0
    strings = [
        "HK Poster Heavy",
        "1997",
        "CITY OF SHADOWS",
        "龍城風暴",
        "霓虹之夜",
    ]
    for text in strings:
        if not all(ord(ch) in cmap for ch in text):
            continue
        buffer = hb.Buffer()
        buffer.add_str(text)
        buffer.guess_segment_properties()
        hb.shape(font, buffer)
        infos = buffer.glyph_infos
        positions = buffer.glyph_positions
        names = [font.get_glyph_name(i.codepoint) for i in infos]
        used_notdef = any(i.codepoint == notdef for i in infos)
        samples.append(
            {
                "text": text,
                "glyphs": names,
                "advances": [p.x_advance for p in positions],
                "notdef_used": used_notdef,
            }
        )
        if used_notdef:
            failures.append(f"排版出现 .notdef 兜底：{text}")
        if not names:
            failures.append(f"排版结果为空：{text}")
    return failures, samples


def expected_width_px(font_path: Path, text: str, size: int) -> tuple[float, float]:
    """按字体自身 cmap+hmtx 算出这段文字应有的像素宽度。

    返回 (精确值, 逐字形取整后的和)。GDI 会把每个字形的推进宽度取整到
    整像素，所以取整后的和才是应当与 GDI 实测值对齐的值。
    """
    from fontTools.ttLib import TTFont

    font = TTFont(str(font_path), lazy=True)
    cmap = font.getBestCmap() or {}
    hmtx = font["hmtx"]
    upm = font["head"].unitsPerEm
    exact = 0.0
    rounded = 0.0
    for char in text:
        glyph_name = cmap.get(ord(char))
        if not glyph_name:
            continue
        advance = hmtx[glyph_name][0]
        exact += advance * size / upm
        rounded += round(advance * size / upm)
    return exact, rounded


def gdi_load_and_render(font_path: Path, face_name: str, text: str, out_png: Path, size: int):
    """Windows GDI 真实加载 + 光栅化。返回 (ok, 详情 dict)。"""
    import ctypes
    from ctypes import wintypes

    gdi32 = ctypes.WinDLL("gdi32", use_last_error=True)
    user32 = ctypes.WinDLL("user32", use_last_error=True)

    # 显式声明签名：ctypes 默认不校验参数个数，CreateFontW 少传一个参数
    # 会让 lfFaceName 读到错位的值，表现为 GDI 静默替换成系统字体。
    gdi32.CreateFontW.restype = wintypes.HGDIOBJ
    gdi32.CreateFontW.argtypes = [
        ctypes.c_int,   # nHeight（负值 = 字符高度）
        ctypes.c_int,   # nWidth
        ctypes.c_int,   # nEscapement
        ctypes.c_int,   # nOrientation
        ctypes.c_int,   # nWeight
        ctypes.c_int,   # bItalic
        ctypes.c_int,   # bUnderline
        ctypes.c_int,   # bStrikeOut
        ctypes.c_int,   # iCharSet (1 = DEFAULT_CHARSET)
        ctypes.c_int,   # iOutPrecision
        ctypes.c_int,   # iClipPrecision
        ctypes.c_int,   # iQuality
        ctypes.c_int,   # lfPitchAndFamily
        ctypes.c_wchar_p,  # lfFaceName
    ]
    gdi32.SelectObject.restype = wintypes.HGDIOBJ
    gdi32.SelectObject.argtypes = [ctypes.c_void_p, wintypes.HGDIOBJ]
    gdi32.GetTextFaceW.restype = ctypes.c_int
    gdi32.GetTextFaceW.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_int]
    gdi32.GetTextExtentPoint32W.restype = ctypes.c_int
    gdi32.GetTextExtentPoint32W.argtypes = [
        ctypes.c_void_p,
        ctypes.c_wchar_p,
        ctypes.c_int,
        ctypes.POINTER(wintypes.SIZE),
    ]
    gdi32.AddFontResourceExW.restype = ctypes.c_int
    gdi32.AddFontResourceExW.argtypes = [ctypes.c_wchar_p, ctypes.c_uint, ctypes.c_void_p]
    user32.GetDC.restype = ctypes.c_void_p
    user32.GetDC.argtypes = [ctypes.c_void_p]
    user32.ReleaseDC.restype = ctypes.c_int
    user32.ReleaseDC.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    user32.FillRect.restype = ctypes.c_int
    user32.FillRect.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong]
    gdi32.DeleteObject.restype = ctypes.c_int
    gdi32.DeleteObject.argtypes = [ctypes.c_void_p]
    gdi32.DeleteDC.restype = ctypes.c_int
    gdi32.DeleteDC.argtypes = [ctypes.c_void_p]
    gdi32.CreateCompatibleDC.restype = ctypes.c_void_p
    gdi32.CreateCompatibleDC.argtypes = [ctypes.c_void_p]
    gdi32.CreateCompatibleBitmap.restype = ctypes.c_void_p
    gdi32.CreateCompatibleBitmap.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    gdi32.SetBkMode.restype = ctypes.c_int
    gdi32.SetBkMode.argtypes = [ctypes.c_void_p, ctypes.c_int]
    gdi32.SetTextColor.restype = ctypes.c_uint
    gdi32.SetTextColor.argtypes = [ctypes.c_void_p, ctypes.c_uint]
    gdi32.TextOutW.restype = ctypes.c_int
    gdi32.TextOutW.argtypes = [
        ctypes.c_void_p,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_wchar_p,
        ctypes.c_int,
    ]
    gdi32.GetDIBits.restype = ctypes.c_int
    gdi32.GetDIBits.argtypes = [
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_uint,
        ctypes.c_uint,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_uint,
    ]
    gdi32.SetDIBitsToDevice.restype = ctypes.c_int
    gdi32.SetDIBitsToDevice.argtypes = [
        ctypes.c_void_p,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_uint,
        ctypes.c_uint,
        ctypes.c_int,
        ctypes.c_int,
        ctypes.c_uint,
        ctypes.c_uint,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_uint,
    ]

    added = gdi32.AddFontResourceExW(ctypes.c_wchar_p(str(font_path)), 0x10, None)
    if added <= 0:
        return False, {"error": f"AddFontResourceExW 返回 {added}", "loaded": False}

    class BITMAPINFOHEADER(ctypes.Structure):
        _fields_ = [
            ("biSize", wintypes.DWORD),
            ("biWidth", ctypes.c_long),
            ("biHeight", ctypes.c_long),
            ("biPlanes", wintypes.WORD),
            ("biBitCount", wintypes.WORD),
            ("biCompression", wintypes.DWORD),
            ("biSizeImage", wintypes.DWORD),
            ("biXPelsPerMeter", ctypes.c_long),
            ("biYPelsPerMeter", ctypes.c_long),
            ("biClrUsed", wintypes.DWORD),
            ("biClrImportant", wintypes.DWORD),
        ]

    class BITMAPINFO(ctypes.Structure):
        _fields_ = [("bmiHeader", BITMAPINFOHEADER), ("bmiColors", wintypes.DWORD * 3)]

    hdc = user32.GetDC(None)
    try:
        handle = gdi32.CreateFontW(
            -size, 0, 0, 0, 400, 0, 0, 0, 1, 0, 0, 0, 0, ctypes.c_wchar_p(face_name)
        )
        if not handle:
            return False, {"error": "CreateFontW 失败", "loaded": False}
        old = gdi32.SelectObject(hdc, handle)
        face_buf = ctypes.create_unicode_buffer(64)
        face_n = gdi32.GetTextFaceW(hdc, ctypes.cast(face_buf, ctypes.c_wchar_p), 64)
        face_used = face_buf.value if face_n > 0 else ""

        extent = wintypes.SIZE()
        gdi32.GetTextExtentPoint32W(
            hdc, ctypes.c_wchar_p(text), len(text), ctypes.byref(extent)
        )
        width = max(extent.cx + size, size * 2)
        height = size * 3

        mem_dc = gdi32.CreateCompatibleDC(hdc)
        bitmap = gdi32.CreateCompatibleBitmap(hdc, width, height)
        gdi32.SelectObject(mem_dc, bitmap)

        class RECT(ctypes.Structure):
            _fields_ = [
                ("left", ctypes.c_long),
                ("top", ctypes.c_long),
                ("right", ctypes.c_long),
                ("bottom", ctypes.c_long),
            ]

        white = ctypes.c_ulong(0x00FFFFFF)
        user32.FillRect(mem_dc, ctypes.byref(RECT(0, 0, width, height)), white)
        gdi32.SetBkMode(mem_dc, 1)
        gdi32.SetTextColor(mem_dc, 0x00000000)
        gdi32.TextOutW(mem_dc, 8, 8, ctypes.c_wchar_p(text), len(text))

        header = BITMAPINFOHEADER()
        header.biSize = ctypes.sizeof(BITMAPINFOHEADER)
        header.biWidth = width
        header.biHeight = -height
        header.biPlanes = 1
        header.biBitCount = 32
        header.biCompression = 0
        info = BITMAPINFO()
        info.bmiHeader = header
        buffer = ctypes.create_string_buffer(width * height * 4)
        copied = gdi32.GetDIBits(mem_dc, bitmap, 0, height, buffer, ctypes.byref(info), 0)

        from PIL import Image

        image = Image.frombuffer(
            "RGBA", (width, height), buffer, "raw", "BGRA", 0, 1
        ).convert("RGB")
        out_png.parent.mkdir(parents=True, exist_ok=True)
        image.save(out_png)
        raw = bytes(buffer)
        ink_pixels = sum(
            1
            for index in range(0, width * height * 4, 4)
            if raw[index : index + 3] != b"\xff\xff\xff"
        )

        gdi32.DeleteObject(bitmap)
        gdi32.DeleteDC(mem_dc)
        gdi32.SelectObject(hdc, old)
        gdi32.DeleteObject(handle)

        # 替换检测：GDI 量到的宽度必须与字体自身 hmtx 的推进宽度一致。
        # 若 GDI 静默换用系统字体（宋体/Times 等），宽度必然对不上。
        expected_px, expected_rounded = expected_width_px(font_path, text, size)
        tolerance = max(2.0, expected_rounded * 0.02)
        extent_matches = abs(extent.cx - expected_rounded) <= tolerance

        return True, {
            "loaded": True,
            "fonts_added": int(added),
            "requested_face": face_name,
            "face_used_by_gdi": face_used or "(GetTextFaceW 未返回，Windows 不保证该值)",
            "gdi_text_extent": [int(extent.cx), int(extent.cy)],
            "expected_text_extent_px": [round(expected_px, 2), round(expected_rounded, 2)],
            "extent_matches_font_metrics": bool(extent_matches),
            "extent_tolerance_px": round(tolerance, 2),
            "dib_scanlines_copied": int(copied),
            "ink_pixels": int(ink_pixels),
            "png": str(out_png),
        }
    finally:
        user32.ReleaseDC(None, hdc)


def main() -> int:
    parser = argparse.ArgumentParser(description="成品字体 IT/ST 检查")
    parser.add_argument("--font", default=str(FONT_SRC / "dist" / "HKPoster-Heavy.ttf"))
    parser.add_argument("--sources", nargs="*", default=None)
    parser.add_argument("--json", default=None)
    parser.add_argument("--png", default=None, help="GDI 渲染证据 PNG")
    args = parser.parse_args()

    from fontTools.ttLib import TTFont

    font_path = Path(args.font).resolve()
    if not font_path.exists():
        print(f"[verify_font] 找不到字体文件：{font_path}")
        return 1

    sources = (
        [Path(p).resolve() for p in args.sources]
        if args.sources
        else sorted((FONT_SRC / "masters").glob("*.ufo"))
    )
    expected = source_unicodes(sources)

    failures: list[str] = []
    notes: list[str] = []

    font = TTFont(str(font_path))
    missing, extra = check_tables(font)
    if missing:
        failures.append(f"缺少必需表：{missing}")

    cmap_failures, cmap_count = check_cmap(font, expected)
    failures.extend(cmap_failures)

    name_table = font["name"]
    family = name_table.getDebugName(1) or ""
    subfamily = name_table.getDebugName(2) or ""
    full_name = name_table.getDebugName(4) or ""
    version = name_table.getDebugName(5) or ""

    shaping_failures, samples = check_shaping(font_path, font.getBestCmap() or {})
    failures.extend(shaping_failures)

    has_gpos = "GPOS" in font
    has_gsub = "GSUB" in font
    if not has_gpos:
        notes.append("GPOS 不存在（Latin kerning 尚未接入，见 docs/04）")

    png_path = (
        Path(args.png).resolve()
        if args.png
        else FONT_SRC / "reports" / "st-gdi-render.png"
    )
    # ST 测试串只能用字体自身已有的字符：缺字时 GDI 会用系统字体补齐，
    # 那时宽度对不上 hmtx，无法证明"用的是我们的字体"。
    cmap_all = font.getBestCmap() or {}
    test_chars = [
        chr(cp) for cp in sorted(cmap_all) if cp > 0x20 and chr(cp).strip()
    ][:8]
    st_text = "".join(test_chars) or " "
    st_ok, st_detail = gdi_load_and_render(
        font_path, full_name or family, st_text, png_path, 96
    )
    if not st_ok:
        failures.append(f"GDI 加载失败：{st_detail.get('error')}")
    elif not st_detail.get("extent_matches_font_metrics"):
        failures.append(
            f"GDI 疑似静默替换字体：GDI 实测宽度 {st_detail['gdi_text_extent'][0]}px，"
            f"字体自身 hmtx 应为 {st_detail['expected_text_extent_px'][1]}px"
        )
    elif not st_detail.get("ink_pixels"):
        failures.append("GDI 渲染没有任何墨迹（可能未真正使用该字体）")

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "font": rel_path(font_path),
        "name_table": {
            "family": family,
            "subfamily": subfamily,
            "full_name": full_name,
            "version": version,
        },
        "tables": sorted(font.keys()),
        "missing_required_tables": missing,
        "extra_tables": extra,
        "cmap_entries": cmap_count,
        "source_unicode_count": len(expected),
        "has_gpos": has_gpos,
        "has_gsub": has_gsub,
        "shaping_samples": samples,
        "st": st_detail,
        "st_test_string": st_text,
        "failures": failures,
        "notes": notes,
    }
    report_path = (
        Path(args.json).resolve() if args.json else FONT_SRC / "reports" / "verify.json"
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[verify_font] 字体：{report['font']}")
    print(f"[verify_font] 名称：{full_name} / {version}")
    print(f"[verify_font] 表：{len(report['tables'])} 个；cmap {cmap_count} 项")
    print(f"[verify_font] GPOS={'有' if has_gpos else '无'}  GSUB={'有' if has_gsub else '无'}")
    if st_ok:
        print(
            f"[verify_font] ST：GDI 加载 {st_detail['fonts_added']} 个字体，"
            f"实测宽度 {st_detail['gdi_text_extent'][0]}px / 字体 hmtx 应为 "
            f"{st_detail['expected_text_extent_px'][1]}px，"
            f"墨迹 {st_detail['ink_pixels']} px，证据 {st_detail['png']}"
        )
    for failure in failures:
        print(f"  FAIL  {failure}")
    for note in notes:
        print(f"  NOTE  {note}")
    print(f"[verify_font] {'PASS' if not failures else 'FAIL'}（FAIL {len(failures)}）")
    print(f"[verify_font] 报告：{report_path}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
