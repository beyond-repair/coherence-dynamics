"""Phase 4A: asymptotic analysis of continuum self-energy.

Σ(k) = ∫_0^∞ ρ(s) / (k² + s) ds

Leading finite-moment theorem and normalized correction J(k).
"""
from __future__ import annotations

from typing import Callable

import numpy as np
from scipy.integrate import quad


def continuum_self_energy(
    k: float,
    rho: Callable[[float], float],
    s_max: float | None = None,
    epsabs: float = 1e-14,
) -> float:
    k2 = max(float(k)**2, 1e-30)
    if s_max is None:
        s_max = 100.0

    def integrand(s):
        return rho(s) / (k2 + s)

    val, _ = quad(integrand, 0.0, s_max, epsabs=epsabs, limit=5000)
    return float(val)


def numerical_I(k: float, rho: Callable[[float], float], eps: float = 1e-4) -> float:
    s1 = continuum_self_energy(k, rho)
    s2 = continuum_self_energy(k * (1.0 + eps), rho)
    if s1 <= 0 or s2 <= 0:
        return float("nan")
    return float(np.log(s2 / s1) / np.log(1.0 + eps))


def numerical_J(k: float, rho: Callable[[float], float]) -> float:
    return float(k**2 * (numerical_I(k, rho) + 2.0))


def spectral_moment_0(rho: Callable[[float], float], s_max: float = 100.0) -> float:
    val, _ = quad(rho, 0.0, s_max, epsabs=1e-14, limit=5000)
    return float(val)


def compact_rho(s: float, s_cut: float = 1.0) -> float:
    return 1.0 / s_cut if 0 <= s <= s_cut else 0.0


def exponential_rho(s: float, s0: float = 1.0) -> float:
    return np.exp(-s / s0) if s >= 0 else 0.0


def power_finite_rho(s: float, alpha: float = -0.5) -> float:
    if s <= 0:
        return 0.0
    return s**alpha * np.exp(-s)


def power_divergent_rho(s: float) -> float:
    """ρ(s) = 1/(1+s) — logarithmically divergent M0."""
    return 1.0 / (1.0 + s) if s >= 0 else 0.0
