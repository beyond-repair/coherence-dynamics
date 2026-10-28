"""Tests for Phase 4A (improved numerics)."""
import numpy as np
import pytest

from models.asymptotics import (
    continuum_self_energy,
    numerical_I,
    numerical_J,
    spectral_moment_0,
    compact_rho,
    exponential_rho,
    power_finite_rho,
    power_divergent_rho,
)


def test_finite_moment_I_approaches_minus_2():
    for rho in (compact_rho, exponential_rho, lambda s: power_finite_rho(s)):
        I = numerical_I(30.0, rho)
        assert abs(I + 2.0) < 0.1, f"I(30)={I}"


def test_sigma_k2_approaches_M0():
    rho = exponential_rho
    M0 = spectral_moment_0(rho)
    k = 20.0
    Sigma = continuum_self_energy(k, rho)
    rel = abs(Sigma * k**2 - M0) / M0
    assert rel < 0.1


def test_divergent_M0_does_not_approach_minus_2():
    I = numerical_I(10.0, power_divergent_rho)
    assert I > -1.8  # not yet at -2; for 1/(1+s) the approach is logarithmic


def test_J_finite_for_exponential():
    J = numerical_J(10.0, exponential_rho)
    assert np.isfinite(J)
