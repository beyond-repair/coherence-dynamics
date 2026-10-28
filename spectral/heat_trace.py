"""Heat-trace and spectral-zeta utilities (where well-defined).

Implemented for finite graphs. Continuum limits are labeled as such.
"""
from __future__ import annotations

import numpy as np


def heat_trace(eigenvalues: np.ndarray, t: float) -> float:
    """Tr exp(-t L) for the combinatorial Laplacian eigenvalues."""
    if t < 0:
        raise ValueError("t >= 0")
    return float(np.sum(np.exp(-t * eigenvalues)))


def spectral_zeta_approx(eigenvalues: np.ndarray, s: float, exclude_zero: bool = True) -> float:
    """Approximate spectral zeta ζ(s) = sum λ^{-s} (nonzero)."""
    ev = eigenvalues[eigenvalues > 1e-12] if exclude_zero else eigenvalues
    if s <= 0 and len(ev) == 0:
        return 0.0
    return float(np.sum(ev ** (-s)))
