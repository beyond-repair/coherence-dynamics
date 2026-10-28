"""Continuum of unresolved modes: induced self-energy as spectral integral.

Σ(k) = ∫_0^∞ ρ(s) / (k² + s) ds

Assumptions for the integral to be well-defined:
- ρ(s) ≥ 0
- ∫ ρ(s)/(1+s) ds < ∞  (sufficient for finiteness at finite k)
"""
from __future__ import annotations

from typing import Callable

import numpy as np
from scipy.integrate import quad


def continuum_self_energy(
    k: float,
    rho: Callable[[float], float],
    s_max: float | None = None,
    epsabs: float = 1e-10,
) -> float:
    """Numerical integral Σ(k) = ∫ ρ(s)/(k²+s) ds from 0 to s_max.

    If s_max is None, uses a large but finite cutoff chosen for exponential tails.
    """
    k2 = max(k**2, 1e-30)
    if s_max is None:
        s_max = 100.0 * (1.0 + k2)  # adaptive but safe for the example densities

    def integrand(s):
        return rho(s) / (k2 + s)

    val, err = quad(integrand, 0.0, s_max, epsabs=epsabs, limit=1000)
    return float(val)


def power_law_rho(s: float, alpha: float, s0: float = 1.0) -> float:
    """Example spectral density ρ(s) = s^alpha * exp(-s/s0).
    Un-normalized; overall strength is a separate scale.
    """
    if s <= 0:
        return 0.0
    return s**alpha * np.exp(-s / s0)
