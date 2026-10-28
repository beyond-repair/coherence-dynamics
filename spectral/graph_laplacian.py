"""Graph Laplacian construction and spectral quantities.

Reproduces baseline results from prior gasket work.
A positivity bound is not a unique physical prediction.
"""
from __future__ import annotations

from typing import List, Tuple

import numpy as np

from .gasket_construction import build_gasket, Edge


def combinatorial_laplacian(n: int, edges: List[Edge]) -> np.ndarray:
    """Free combinatorial Laplacian L = D - A."""
    L = np.zeros((n, n), dtype=float)
    for i, j in edges:
        L[i, i] += 1.0
        L[j, j] += 1.0
        L[i, j] -= 1.0
        L[j, i] -= 1.0
    return L


def graph_spectrum(level: int) -> dict:
    """Compute basic spectral invariants for the free gasket Laplacian."""
    P, E, C = build_gasket(level)
    L = combinatorial_laplacian(len(P), E)
    w = np.linalg.eigvalsh(L)
    return {
        "level": level,
        "N": int(len(P)),
        "E": int(len(E)),
        "lambda_max": float(w.max()),
        "TrL": float(np.trace(L)),
        "n_zero": int(np.sum(np.abs(w) < 1e-10)),
        "eigenvalues": w,
    }


def kernel_matrix(omega2: float, W: float, L: np.ndarray) -> np.ndarray:
    """K = ω² I - W L."""
    return omega2 * np.eye(L.shape[0]) - W * L


def positivity_bound(lambda_max: float, omega2: float = 1.0) -> float:
    """Upper bound on W for positive-definiteness of K (when λ_max > 0)."""
    if lambda_max <= 0:
        return float("inf")
    return omega2 / lambda_max
