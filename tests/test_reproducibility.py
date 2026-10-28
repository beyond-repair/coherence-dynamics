"""Reproducibility checks."""
from numerics.reproducibility import set_seed
import numpy as np


def test_seed_determinism():
    set_seed(42)
    a = np.random.rand(5)
    set_seed(42)
    b = np.random.rand(5)
    assert np.allclose(a, b)
