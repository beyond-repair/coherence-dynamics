"""Regression tests for spectral baseline."""
import pytest
import numpy as np

from spectral.graph_laplacian import graph_spectrum, positivity_bound
from spectral.gasket_construction import build_gasket


def test_level2_invariants():
    spec = graph_spectrum(2)
    assert spec["N"] == 15
    assert spec["E"] == 27
    assert abs(spec["lambda_max"] - 6.0) < 1e-8
    assert abs(spec["TrL"] - 54.0) < 1e-8
    assert spec["n_zero"] == 1  # connected graph, one zero mode


def test_level3_invariants():
    spec = graph_spectrum(3)
    assert spec["N"] == 42
    assert spec["E"] == 81
    assert abs(spec["lambda_max"] - 6.0) < 1e-8
    assert abs(spec["TrL"] - 162.0) < 1e-8


def test_positivity_bound():
    # For ω^{2}=1, λ_max=6 → W < 1/6
    bound = positivity_bound(6.0, omega2=1.0)
    assert abs(bound - 1.0 / 6.0) < 1e-12


def test_kernel_positive_definite_below_bound():
    from spectral.graph_laplacian import combinatorial_laplacian, kernel_matrix
    from numerics.diagnostics import check_positive_definite
    P, E, _ = build_gasket(2)
    L = combinatorial_laplacian(len(P), E)
    K = kernel_matrix(1.0, 0.1, L)  # 0.1 < 1/6
    assert check_positive_definite(K)
