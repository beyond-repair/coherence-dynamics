"""Tests for the Gaussian two-field baseline and candidate invariant."""
import numpy as np
import pytest

from models.gaussian_two_field import (
    K_eff,
    self_energy,
    positivity_condition,
    low_momentum_expansion,
    log_derivative_invariant,
    analytic_I_limit,
    dimensionless_response,
)


def test_exact_elimination():
    k = np.array([0.0, 0.5, 1.0, 2.0])
    m_phi, g, m_chi = 1.0, 0.5, 1.2
    Sigma = self_energy(k, g, m_chi)
    K = K_eff(k, m_phi, g, m_chi)
    expected = k**2 + m_phi**2 - g**2 / (k**2 + m_chi**2)
    assert np.allclose(K, expected)
    assert np.allclose(Sigma, g**2 / (k**2 + m_chi**2))


def test_positivity():
    # Stable case
    assert positivity_condition(1.0, 0.3, 1.0)
    # Unstable at k=0
    assert not positivity_condition(0.1, 1.0, 0.5)


def test_low_momentum():
    exp = low_momentum_expansion(1.0, 0.4, 1.5)
    assert abs(exp["K_eff(0)"] - (1.0 - 0.16 / 2.25)) < 1e-12
    assert abs(exp["d2K_eff/dk2(0)"] - (2.0 + 2.0 * 0.16 / 1.5**4)) < 1e-12


def test_invariant_analytic():
    k = np.linspace(0.1, 5.0, 20)
    m_chi = 1.0
    I_num = log_derivative_invariant(k, 0.5, m_chi)
    I_ana = analytic_I_limit(k, m_chi)
    assert np.allclose(I_num, I_ana)
    # Limits
    assert abs(analytic_I_limit(0.0, 1.0)) < 1e-12
    assert abs(analytic_I_limit(1e6, 1.0) + 2.0) < 1e-6


def test_invariant_parameter_dependence():
    k = 1.0
    I1 = log_derivative_invariant(k, 0.1, 1.0)
    I2 = log_derivative_invariant(k, 10.0, 1.0)
    # Independent of g
    assert abs(I1 - I2) < 1e-12
    # Depends on m_chi
    I3 = log_derivative_invariant(k, 0.1, 2.0)
    assert abs(I1 - I3) > 0.1


def test_dimensionless_response_scaling():
    k = np.array([0.1, 1.0, 10.0])
    r = dimensionless_response(k, 1.0, 1.0)
    assert r.shape == k.shape
    assert np.all(np.isfinite(r))
