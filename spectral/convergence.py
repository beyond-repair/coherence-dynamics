"""Convergence across graph levels.

Reports differences; does not claim continuum limits unless supported.
"""
from __future__ import annotations

from typing import Callable

import numpy as np

from .graph_laplacian import graph_spectrum


def level_convergence(quantity: Callable[[int], float], levels: list[int]) -> dict:
    """Compute quantity at successive levels and relative changes."""
    values = [quantity(n) for n in levels]
    rel = []
    for i in range(1, len(values)):
        if values[i - 1] == 0:
            rel.append(float("nan"))
        else:
            rel.append(abs(values[i] - values[i - 1]) / abs(values[i - 1]))
    return {"levels": levels, "values": values, "relative_changes": rel}
