"""Conservation and symmetry checks (placeholders until models are specified)."""
import numpy as np

from numerics.diagnostics import conservation_residual


def test_zero_divergence_residual():
    zero = np.zeros(3)
    assert conservation_residual(zero) == 0.0
