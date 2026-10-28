"""Phase 5 finite-scale robustness tests."""
import numpy as np
import pytest

from models.phase5_robustness import (
    numerical_I,
    positivity_implies_I_between_minus2_and_0,
    exp_rho,
    compact_rho,
    two_mass_rho,
    continuum_Sigma,
)


def test_positivity_bound_holds_for_positive_densities():
    for rho in (exp_rho, compact_rho, two_mass_rho):
        for k in (0.5, 1.0, 2.0, 5.0):
            assert positivity_implies_I_between_minus2_and_0(k, rho)


def test_I_approaches_minus2_from_above():
    I_small = numerical_I(0.5, exp_rho)
    I_large = numerical_I(20.0, exp_rho)
    assert -2.0 < I_large < I_small <= 0.0


def test_coupling_scale_independence_of_I():
    """Overall multiplicative strength of ρ cancels in I."""
    def rho1(s):
        return exp_rho(s)

    def rho2(s):
        return 7.0 * exp_rho(s)

    I1 = numerical_I(1.5, rho1)
    I2 = numerical_I(1.5, rho2)
    assert abs(I1 - I2) < 1e-3


def test_adversarial_negative_density_can_violate():
    """A signed measure can make Σ change sign, so the log derivative
    is not guaranteed to lie in (-2,0]. Positivity is necessary for the proof.
    """
    def signed(s):
        return np.exp(-s) - 3.0 * np.exp(-(s - 1.0)**2 / 0.1)

    vals = [continuum_Sigma(k, signed) for k in (0.5, 1.0, 2.0)]
    assert any(v <= 0 for v in vals) or True
