"""Tests for multi-field Schur complement and continuum spectral density."""
import numpy as np
import pytest

from models.multi_field_schur import schur_complement, two_field_reduction
from models.continuum_spectral import continuum_self_energy, power_law_rho


def test_schur_reduces_to_single_field():
    k, m_phi, g, m_chi = 1.5, 1.0, 0.7, 1.2
    K = two_field_reduction(k, m_phi, g, m_chi)
    expected = k**2 + m_phi**2 - g**2 / (k**2 + m_chi**2)
    assert abs(K - expected) < 1e-10


def test_schur_matrix_positive_when_blocks_positive():
    # Diagonal positive definite blocks, modest coupling
    A = np.diag([2.0, 3.0])
    B = np.diag([4.0, 5.0])
    C = 0.1 * np.ones((2, 2))
    K = schur_complement(A, B, C)
    w = np.linalg.eigvalsh(K)
    assert np.all(w > 0)


def test_continuum_integral_finite():
    def rho(s):
        return power_law_rho(s, alpha=0.5, s0=1.0)

    Sigma = continuum_self_energy(1.0, rho, s_max=100.0)
    assert np.isfinite(Sigma)
    assert Sigma > 0


def test_continuum_scaling_with_strength():
    def rho1(s):
        return power_law_rho(s, 0.0)

    def rho2(s):
        return 3.0 * power_law_rho(s, 0.0)

    s1 = continuum_self_energy(1.0, rho1)
    s2 = continuum_self_energy(1.0, rho2)
    assert abs(s2 / s1 - 3.0) < 1e-6
