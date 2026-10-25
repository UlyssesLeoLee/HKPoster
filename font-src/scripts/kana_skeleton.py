"""骨架中心线提取 —— 把「笔画粗细」从「字形对不对」里剥出去。

为什么需要它
------------
直接对归一化位图求 IoU，粗细差异会被当成走形：同一副骨架，
细笔画版和粗笔画版 IoU 可能只有 0.4。本项目假名比参照轻，
于是 191 个字里 174 个被判 FAIL —— 这种告警没有分辨力。

为什么不用 Zhang-Suen 细化
--------------------------
实测：Zhang-Suen 把 10px 宽的矩形环细化到 **20px**（正确结果应是周长 ~320px 的闭合环），
在细结构上会**断裂**（经典缺陷：2~3px 宽的环会被整体删空）。
用它做中心线，指标变成"这个字的墨迹够不够粗"，还是同一个毛病。

改用 **距离变换脊线**
--------------------
1. 距离变换 EDT（两遍 chamfer，3-4 邻域，纯 numpy，不依赖 scipy）；
2. 取局部极大脊线作为中心线 —— 这是**子集选择**，不会像腐蚀那样把细结构删断；
3. 中心线各膨胀 2px 取容差后求 IoU。

效果（见本文件底部自测）：
* 粗细不同但骨架相同 → 0.9 以上（对粗细不敏感）
* 横线 vs 竖线 → 极低（对走向敏感）
"""

from __future__ import annotations

import numpy as np

_BIG = 1e9


def distance_transform(mask: np.ndarray) -> np.ndarray:
    """两遍 chamfer(3-4) 距离变换：每个墨点到最近背景点的距离。

    ⚠️ 水平方向不能写成 ``np.minimum.accumulate(d)`` —— 那是把**像素值**
    往前传（遇到背景 0 就一路变 0），不是「到最近背景点的索引距离」。
    正确做法是按**索引**算：左扫取最近背景的列号，右扫取右边最近背景的列号。
    """
    h, w = mask.shape
    idx = np.arange(w)
    is_bg = ~mask

    # 水平：到同行最近背景像素的**索引距离**
    last_bg = np.maximum.accumulate(np.where(is_bg, idx, -1), axis=1)
    left = idx - last_bg
    next_bg = np.minimum.accumulate(np.where(is_bg, idx, w)[:, ::-1], axis=1)[:, ::-1]
    right = next_bg - idx
    d = np.minimum(left, right).astype(np.float64)

    # 整行都是墨迹时，水平方向没有背景可依 —— 交给垂直遍处理
    no_bg_row = ~is_bg.any(axis=1)
    if no_bg_row.any():
        d[no_bg_row, :] = _BIG

    # 垂直两遍（含对角）
    for i in range(1, h):
        cur = d[i]
        prev = d[i - 1]
        np.minimum(cur, prev + 3, out=cur)
        cur[1:] = np.minimum(cur[1:], prev[:-1] + 4)
        cur[:-1] = np.minimum(cur[:-1], prev[1:] + 4)
    for i in range(h - 2, -1, -1):
        cur = d[i]
        nxt = d[i + 1]
        np.minimum(cur, nxt + 3, out=cur)
        cur[1:] = np.minimum(cur[1:], nxt[:-1] + 4)
        cur[:-1] = np.minimum(cur[:-1], nxt[1:] + 4)
    return d


def ridge(mask: np.ndarray) -> np.ndarray:
    """距离变换的局部极大脊线 = 笔画中心线。"""
    if not mask.any():
        return np.zeros_like(mask, dtype=bool)
    d = distance_transform(mask)
    pad = np.pad(d, 1, constant_values=-1.0)
    stack = np.stack(
        [
            pad[0:-2, 1:-1], pad[0:-2, 2:], pad[1:-1, 2:], pad[2:, 2:],
            pad[2:, 1:-1], pad[2:, 0:-2], pad[1:-1, 0:-2], pad[0:-2, 0:-2],
        ]
    )
    return mask & (d >= stack.max(axis=0)) & (d > 0)


def dilate(mask: np.ndarray, radius: int = 2) -> np.ndarray:
    out = mask.copy()
    for _ in range(radius):
        p = np.pad(out, 1)
        out = (
            p[:-2, 1:-1] | p[:-2, 2:] | p[1:-1, 2:] | p[2:, 2:]
            | p[2:, 1:-1] | p[2:, :-2] | p[1:-1, :-2] | p[:-2, :-2] | out
        )
    return out


def skeleton_iou(mask_a: np.ndarray, mask_b: np.ndarray, tolerance: int = 2) -> float:
    """中心线 + 容差膨胀后的 IoU。对粗细不敏感，对走向/位置敏感。"""
    if not mask_a.any() and not mask_b.any():
        return 1.0
    if not mask_a.any() or not mask_b.any():
        return 0.0
    sa = dilate(ridge(mask_a), tolerance)
    sb = dilate(ridge(mask_b), tolerance)
    inter = np.count_nonzero(sa & sb)
    union = np.count_nonzero(sa | sb)
    return float(inter / union) if union else 0.0


if __name__ == "__main__":
    # 1) 自比
    a = np.zeros((64, 64), bool)
    a[30:34, 10:54] = True
    print("自比 =", round(skeleton_iou(a, a), 3))

    # 2) 粗细不同但骨架相同 → 应接近 1
    b = np.zeros((64, 64), bool)
    b[28:36, 10:54] = True
    print("粗细不同(骨架同) =", round(skeleton_iou(a, b), 3))

    # 3) 横线 vs 竖线 → 应极低
    c = np.zeros((64, 64), bool)
    c[10:54, 30:34] = True
    print("横线 vs 竖线 =", round(skeleton_iou(a, c), 3))

    # 4) 直 vs 折 → 应明显低于自比
    d = np.zeros((64, 64), bool)
    d[30:34, 10:54] = True
    d[14:34, 50:54] = True
    print("直 vs 折 =", round(skeleton_iou(a, d), 3))

    # 5) 矩形环：脊线必须保住整圈（Zhang-Suen 在这里会断）
    ring = np.zeros((96, 96), bool)
    ring[6:86, 6:86] = True
    ring[16:76, 16:76] = False
    print("矩形环 脊线像素 =", int(ridge(ring).sum()), "(周长约 320)")

    # 6) 环 vs 同心小环 → 骨架位置不同，应低
    ring2 = np.zeros((96, 96), bool)
    ring2[26:66, 26:66] = True
    ring2[36:56, 36:56] = False
    print("大环 vs 小环 =", round(skeleton_iou(ring, ring2), 3))
