"""Phase 5: finite-scale robustness and positivity bounds.

No physical interpretation. Definitions of I and J remain those of prior phases.
"""
from __future__ import annotations

from typing import Callable

import numpy as np
from scipy.integrate import quad


def continuum_Sigma(k: float, rho: Callable[[float], float], s_max: float = 200.0) -> float:
    k2 = max(k**2, 1e-30)

    def integrand(s):
        return rho(s) / (k2 + s)

    val, _ = quad(integrand, 0.0, s_max, epsabs=1e-12, limit=2000)
    return float(val)


def numerical_I(k: float, rho: Callable[[float], float], eps: float = 1e-4) -> float:
    """I(k) = d ln Σ / d ln k (consistent with prior phases)."""
    s1 = continuum_Sigma(k, rho)
    s2 = continuum_Sigma(k * (1 + eps), rho)
    if s1 <= 0 or s2 <= 0:
        return float("nan")
    return float(np.log(s2 / s1) / np.log(1 + eps))


def positivity_implies_I_between_minus2_and_0(k: float, rho: Callable[[float], float]) -> bool:
    """For ρ≥0 and Σ>0, -2 < I(k) ≤ 0 at finite k>0."""
    I = numerical_I(k, rho)
    return bool(-2.0 < I <= 0.0)


def exp_rho(s: float) -> float:
    return np.exp(-s) if s >= 0 else 0.0


def compact_rho(s: float) -> float:
    return 1.0 if 0 <= s <= 1.0 else 0.0


def two_mass_rho(s: float) -> float:
    return (
        np.exp(-((s - 0.5) ** 2) / 0.01) + 0.3 * np.exp(-((s - 2.0) ** 2) / 0.01)
    ) / np.sqrt(2 * np.pi * 0.01)
