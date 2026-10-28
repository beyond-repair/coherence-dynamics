"""Diagnostics for numerical and physical consistency."""
from __future__ import annotations

import numpy as np


def check_positive_definite(M: np.ndarray, tol: float = 1e-10) -> bool:
    """Return True if the smallest eigenvalue is greater than tol."""
    w = np.linalg.eigvalsh(M)
    return bool(w.min() > tol)


def conservation_residual(div_T: np.ndarray) -> float:
    """L2 residual of a divergence (placeholder for stress-energy checks)."""
    return float(np.linalg.norm(div_T))
