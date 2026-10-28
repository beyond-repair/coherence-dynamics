"""Exact and numerical checks for the Phase 4B borderline density."""
import numpy as np


def exact_Sigma(x: float) -> float:
    """Σ(x) = ln(1+x)/x for ρ(s)=1/(1+s)."""
    return np.log1p(x) / x


def exact_I(x: float) -> float:
    """I(x) = -2 + 2x / ((1+x) ln(1+x))."""
    return -2.0 + 2.0 * x / ((1.0 + x) * np.log1p(x))


def exact_J(x: float) -> float:
    """J(x) = 2 x² / ((1+x) ln(1+x))."""
    return 2.0 * x**2 / ((1.0 + x) * np.log1p(x))


def test_exact_borderline_limit():
    for x in (10.0, 100.0, 1000.0):
        I = exact_I(x)
        assert abs(I + 2.0) < 1.0  # approaches
        assert exact_J(x) > exact_J(x / 10)  # diverging


def test_exact_matches_derivative_definition():
    x = 5.0
    # Numerical d ln Σ / d ln k where x = k², so factor 2
    eps = 1e-6
    s1 = exact_Sigma(x)
    s2 = exact_Sigma(x * (1 + eps))
    I_num = 2.0 * np.log(s2 / s1) / np.log(1 + eps)
    assert abs(I_num - exact_I(x)) < 1e-4
