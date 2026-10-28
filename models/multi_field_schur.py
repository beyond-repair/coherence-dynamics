"""Multi-field Gaussian model: exact Schur complement after integrating out unresolved fields.

For quadratic Euclidean action with blocks
    [ A(k)    C(k) ]
    [ C†(k)   B(k) ]

the effective kernel for the retained fields is the Schur complement
    K_eff(k) = A(k) - C(k) B(k)^{-1} C(k)†

This reduces to the single-field case when B is scalar and C = g.
"""
from __future__ import annotations

import numpy as np


def schur_complement(
    A: np.ndarray,
    B: np.ndarray,
    C: np.ndarray,
) -> np.ndarray:
    """Exact effective kernel K_eff = A - C @ inv(B) @ C.T.conj()

    A, B square; C has shape (n_retained, n_unresolved).
    """
    B_inv = np.linalg.inv(B)
    return A - C @ B_inv @ C.conj().T


def multi_field_self_energy(C: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Induced self-energy matrix Σ = C B^{-1} C†."""
    return C @ np.linalg.inv(B) @ C.conj().T


def two_field_reduction(k: float, m_phi: float, g: float, m_chi: float) -> float:
    """Verify reduction to the single unresolved field case."""
    A = np.array([[k**2 + m_phi**2]])
    B = np.array([[k**2 + m_chi**2]])
    C = np.array([[g]])
    K = schur_complement(A, B, C)
    return float(K[0, 0])
