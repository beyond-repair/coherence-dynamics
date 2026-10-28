"""Sierpiński gasket graph construction.

Reproduced from beyond-repair/sierpinski-geometry-045/gasket_graph.py
for use as a controlled mathematical laboratory.

Provenance: see research_log/provenance.md.
No physical force or selected constant is derived here.
"""
from __future__ import annotations

import math
from typing import Dict, List, Tuple

import numpy as np

Edge = Tuple[int, int]


def _key(p: np.ndarray, nd: int = 10) -> Tuple[float, float]:
    return (round(float(p[0]), nd), round(float(p[1]), nd))


def build_gasket(level: int) -> Tuple[np.ndarray, List[Edge], np.ndarray]:
    """Build the level-n Sierpiński gasket graph.

    Returns positions, edges, corner indices.
    N(0)=3, N(1)=6, N(2)=15, N(3)=42, ... ; E(n)=3**(n+1).
    """
    if level < 0:
        raise ValueError("level >= 0")
    c0 = np.array([0.0, 0.0])
    c1 = np.array([1.0, 0.0])
    c2 = np.array([0.5, math.sqrt(3.0) / 2.0])
    pos_map: Dict[Tuple[float, float], int] = {}
    positions: List[np.ndarray] = []
    edges: set[Edge] = set()

    def vid(p: np.ndarray) -> int:
        k = _key(p)
        if k not in pos_map:
            pos_map[k] = len(positions)
            positions.append(p.copy())
        return pos_map[k]

    def rec(a, b, c, d):
        if d == 0:
            ia, ib, ic = vid(a), vid(b), vid(c)
            for i, j in ((ia, ib), (ib, ic), (ic, ia)):
                if i != j:
                    edges.add((min(i, j), max(i, j)))
            return
        rec(a, 0.5 * (a + b), 0.5 * (c + a), d - 1)
        rec(0.5 * (a + b), b, 0.5 * (b + c), d - 1)
        rec(0.5 * (c + a), 0.5 * (b + c), c, d - 1)

    rec(c0, c1, c2, level)
    P = np.vstack(positions)
    corners = np.array([pos_map[_key(c0)], pos_map[_key(c1)], pos_map[_key(c2)]], dtype=int)
    return P, sorted(edges), corners
