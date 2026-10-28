"""Tests for analytic identities (spectral sums)."""
import numpy as np

from spectral.graph_laplacian import graph_spectrum


def test_trace_equals_twice_edges():
    # Tr L = 2 E for combinatorial Laplacian
    for n in (2, 3):
        spec = graph_spectrum(n)
        assert abs(spec["TrL"] - 2 * spec["E"]) < 1e-8
