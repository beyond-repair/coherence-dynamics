"""Convergence across levels."""
from spectral.convergence import level_convergence
from spectral.graph_laplacian import graph_spectrum


def test_lambda_max_stabilizes():
    def lam_max(n):
        return graph_spectrum(n)["lambda_max"]

    result = level_convergence(lam_max, [2, 3, 4])
    # For n≥2, λ_max = 6 exactly (within numerical tolerance)
    for v in result["values"]:
        assert abs(v - 6.0) < 1e-6
