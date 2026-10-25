"""平台级 ST —— Windows GDI 真实加载与光栅化（替换检测）。

被 run_tests.py 调用；也可单独运行：
    python font-src/tests/test_platform_load.py --font font-src/dist/HKPoster-Heavy.ttf

判定要点
--------
GDI 的 CreateFontW 在找不到字体名时会**静默替换**成系统字体，外部看不出来。
因此本测试不看 GetTextFaceW（Windows 上不保证返回），而是比对
「GDI 实测文本宽度」与「字体自身 hmtx 算出的宽度」：
两者一致才说明用的确实是我们的字体。
"""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
FONT_SRC = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

TEST_TEXT = "HK"
TEST_SIZE = 96


def expected_width_px(font_path: Path, text: str, size: int):
    """按 cmap + hmtx 算出这段文字应有的像素宽度（逐字形取整）。"""
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


def gdi_render(font_path: Path, face_name: str, text: str, out_png: Path, size: int):
    import ctypes
    from ctypes import wintypes

    gdi32 = ctypes.WinDLL("gdi32", use_last_error=True)
    user32 = ctypes.WinDLL("user32", use_last_error=True)

    gdi32.CreateFontW.restype = wintypes.HGDIOBJ
    gdi32.CreateFontW.argtypes = [ctypes.c_int] * 13 + [ctypes.c_wchar_p]
    gdi32.SelectObject.restype = wintypes.HGDIOBJ
    gdi32.SelectObject.argtypes = [ctypes.c_void_p, wintypes.HGDIOBJ]
    gdi32.GetTextExtentPoint32W.restype = ctypes.c_int
    gdi32.GetTextExtentPoint32W.argtypes = [
        ctypes.c_void_p,
        ctypes.c_wchar_p,
        ctypes.c_int,
        ctypes.POINTER(wintypes.SIZE),
    ]
    gdi32.AddFontResourceExW.restype = ctypes.c_int
    gdi32.AddFontResourceExW.argtypes = [ctypes.c_wchar_p, ctypes.c_uint, ctypes.c_void_p]
    gdi32.GetDIBits.restype = ctypes.c_int
    gdi32.GetDIBits.argtypes = [
        ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int,
        ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint,
    ]
    gdi32.CreateCompatibleDC.restype = ctypes.c_void_p
    gdi32.CreateCompatibleDC.argtypes = [ctypes.c_void_p]
    gdi32.CreateCompatibleBitmap.restype = ctypes.c_void_p
    gdi32.CreateCompatibleBitmap.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    gdi32.DeleteObject.restype = ctypes.c_int
    gdi32.DeleteObject.argtypes = [ctypes.c_void_p]
    gdi32.DeleteDC.restype = ctypes.c_int
    gdi32.DeleteDC.argtypes = [ctypes.c_void_p]
    gdi32.SetBkMode.restype = ctypes.c_int
    gdi32.SetBkMode.argtypes = [ctypes.c_void_p, ctypes.c_int]
    gdi32.SetTextColor.restype = ctypes.c_uint
    gdi32.SetTextColor.argtypes = [ctypes.c_void_p, ctypes.c_uint]
    gdi32.TextOutW.restype = ctypes.c_int
    gdi32.TextOutW.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_wchar_p, ctypes.c_int
    ]
    user32.GetDC.restype = ctypes.c_void_p
    user32.GetDC.argtypes = [ctypes.c_void_p]
    user32.ReleaseDC.restype = ctypes.c_int
    user32.ReleaseDC.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    user32.FillRect.restype = ctypes.c_int
    user32.FillRect.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong]

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

    class RECT(ctypes.Structure):
        _fields_ = [
            ("left", ctypes.c_long),
            ("top", ctypes.c_long),
            ("right", ctypes.c_long),
            ("bottom", ctypes.c_long),
        ]

    added = gdi32.AddFontResourceExW(ctypes.c_wchar_p(str(font_path)), 0x10, None)
    if added <= 0:
        return {"loaded": False, "error": f"AddFontResourceExW 返回 {added}"}

    hdc = user32.GetDC(None)
    try:
        handle = gdi32.CreateFontW(
            -size, 0, 0, 0, 400, 0, 0, 0, 1, 0, 0, 0, 0, ctypes.c_wchar_p(face_name)
        )
        if not handle:
            return {"loaded": False, "error": "CreateFontW 失败"}
        old = gdi32.SelectObject(hdc, handle)

        extent = wintypes.SIZE()
        gdi32.GetTextExtentPoint32W(
            hdc, ctypes.c_wchar_p(text), len(text), ctypes.byref(extent)
        )
        width = max(extent.cx + size, size * 2)
        height = size * 3

        mem_dc = gdi32.CreateCompatibleDC(hdc)
        bitmap = gdi32.CreateCompatibleBitmap(hdc, width, height)
        gdi32.SelectObject(mem_dc, bitmap)
        user32.FillRect(
            mem_dc, ctypes.byref(RECT(0, 0, width, height)), ctypes.c_ulong(0x00FFFFFF)
        )
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
        ink = sum(
            1
            for index in range(0, width * height * 4, 4)
            if raw[index : index + 3] != b"\xff\xff\xff"
        )

        gdi32.DeleteObject(bitmap)
        gdi32.DeleteDC(mem_dc)
        gdi32.SelectObject(hdc, old)
        gdi32.DeleteObject(handle)

        return {
            "loaded": True,
            "fonts_added": int(added),
            "text_extent": [int(extent.cx), int(extent.cy)],
            "dib_scanlines": int(copied),
            "ink_pixels": int(ink),
            "png": str(out_png),
        }
    finally:
        user32.ReleaseDC(None, hdc)


def run(context) -> list[dict]:
    from fontTools.ttLib import TTFont

    results: list[dict] = []
    font_path = Path(context["font"])
    font = TTFont(str(font_path))
    full_name = font["name"].getDebugName(4) or font["name"].getDebugName(1) or ""

    png_path = FONT_SRC / "reports" / "st-platform-render.png"
    detail = gdi_render(font_path, full_name, TEST_TEXT, png_path, TEST_SIZE)
    if not detail.get("loaded"):
        results.append(
            {"name": "GDI 真实加载", "status": "FAIL", "detail": detail.get("error", "")}
        )
        return results

    results.append(
        {
            "name": "GDI 真实加载",
            "status": "PASS",
            "detail": f"AddFontResourceExW 注册 {detail['fonts_added']} 个字体，face={full_name!r}",
        }
    )

    exact, rounded = expected_width_px(font_path, TEST_TEXT, TEST_SIZE)
    measured = detail["text_extent"][0]
    tolerance = max(2.0, rounded * 0.02)
    results.append(
        {
            "name": "GDI 未静默替换字体",
            "status": "PASS" if abs(measured - rounded) <= tolerance else "FAIL",
            "detail": (
                f"GDI 实测 {measured}px，字体 hmtx 应为 {rounded}px（容差 {tolerance:.1f}px）"
            ),
        }
    )

    results.append(
        {
            "name": "GDI 光栅化出墨",
            "status": "PASS" if detail["ink_pixels"] > 0 else "FAIL",
            "detail": f"墨迹 {detail['ink_pixels']} 像素，证据 {detail['png']}",
        }
    )

    return results


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--font", default=str(FONT_SRC / "dist" / "HKPoster-Heavy.ttf"))
    args = parser.parse_args()
    outcomes = run({"font": Path(args.font), "sources": []})
    for item in outcomes:
        print(f"  {item['status']:<4} {item['name']}: {item['detail']}")
    raise SystemExit(1 if any(i["status"] == "FAIL" for i in outcomes) else 0)
