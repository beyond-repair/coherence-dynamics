"""Gaussian two-field model: exact effective response after integrating out χ.

Baseline for the Invariant Hunt. Euclidean quadratic action only.
No physical interpretation or target constants.

Action (Euclidean):
    S = (1/2) ∫ φ K_φ φ + (1/2) ∫ χ K_χ χ + g ∫ φ χ

Exact Gaussian elimination yields:
    K_eff(k) = K_φ(k) - g² / K_χ(k)
    Σ(k) = g² / K_χ(k)

For free massive fields:
    K_φ(k) = k² + m_φ²
    K_χ(k) = k² + m_χ²
    K_eff(k) = k² + m_φ² - g² / (k² + m_χ²)
"""
from __future__ import annotations

from typing import Tuple

import numpy as np


def K_phi(k: np.ndarray | float, m_phi: float) -> np.ndarray | float:
    """Bare retained-field kernel."""
    return k**2 + m_phi**2


def K_chi(k: np.ndarray | float, m_chi: float) -> np.ndarray | float:
    """Unresolved-field kernel."""
    return k**2 + m_chi**2


def self_energy(k: np.ndarray | float, g: float, m_chi: float) -> np.ndarray | float:
    """Induced self-energy Σ(k) = g² / K_χ(k). Exact for Gaussian model."""
    return g**2 / K_chi(k, m_chi)


def K_eff(k: np.ndarray | float, m_phi: float, g: float, m_chi: float) -> np.ndarray | float:
    """Effective kernel after exact Gaussian elimination."""
    return K_phi(k, m_phi) - self_energy(k, g, m_chi)


def positivity_condition(m_phi: float, g: float, m_chi: float, k_min: float = 0.0) -> bool:
    """Check K_eff(k) > 0 for k >= k_min (stability of quadratic model)."""
    if m_chi <= 0 or m_phi <= 0:
        return False
    # Minimum occurs at k=0 for this form when g is not too large
    return K_eff(k_min, m_phi, g, m_chi) > 0


def low_momentum_expansion(m_phi: float, g: float, m_chi: float, order: int = 2) -> dict:
    """Taylor expansion of K_eff around k=0.

    K_eff(0) = m_φ² - g²/m_χ²
    d²K_eff/dk² |_{0} = 2 + 2 g² / m_χ⁴   (leading)
    """
    K0 = m_phi**2 - g**2 / m_chi**2
    # Second derivative at zero (analytic)
    d2 = 2.0 + 2.0 * g**2 / m_chi**4
    return {
        "K_eff(0)": K0,
        "d2K_eff/dk2(0)": d2,
        "mass_eff_squared": K0,  # for the quadratic model
        "order": order,
    }


def high_momentum_expansion(m_phi: float, g: float, m_chi: float) -> dict:
    """Asymptotic expansion for large k.

    K_eff(k) ~ k² + m_φ² - g²/k² + O(1/k⁴)
    """
    return {
        "leading": "k**2",
        "constant": m_phi**2,
        "1/k2_coeff": -g**2,
        "note": "Σ(k) ~ g²/k² for large k",
    }


def dimensionless_response(k: np.ndarray | float, g: float, m_chi: float) -> np.ndarray | float:
    """Σ(k) / k²  (dimensionless when k has momentum units)."""
    k = np.asarray(k, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        return self_energy(k, g, m_chi) / np.maximum(k**2, 1e-30)


def log_derivative_invariant(k: np.ndarray | float, g: float, m_chi: float) -> np.ndarray | float:
    """Candidate I(k) = d ln|Σ(k)| / d ln k.

    For this model Σ(k) = g² / (k² + m_χ²),
    I(k) = -2 k² / (k² + m_χ²).
    Exact, model-dependent, not universal.
    """
    k2 = np.asarray(k, dtype=float) ** 2
    return -2.0 * k2 / (k2 + m_chi**2)


def analytic_I_limit(k: float, m_chi: float) -> float:
    """Analytic expression for the candidate invariant."""
    return -2.0 * k**2 / (k**2 + m_chi**2)


def parameter_dependence() -> dict:
    """Explicit dependence classification."""
    return {
        "depends_on_g": ["Σ(k)", "K_eff(k)", "dimensionless_response"],
        "depends_on_m_phi": ["K_eff(k)", "positivity", "low-momentum constant"],
        "depends_on_m_chi": ["Σ(k)", "K_eff(k)", "I(k)", "all expansions"],
        "structure_only": [
            "form of Gaussian elimination K_eff = K_φ - g²/K_χ",
            "I(k) = -2 k²/(k²+m_χ²) for this kernel",
            "high-k Σ ~ g²/k²",
        ],
    }
