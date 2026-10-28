"""Numerical precision and tolerance helpers."""
from __future__ import annotations

import numpy as np

DEFAULT_RTOL = 1e-8
DEFAULT_ATOL = 1e-10


def is_close(a: float, b: float, rtol: float = DEFAULT_RTOL, atol: float = DEFAULT_ATOL) -> bool:
    return bool(np.isclose(a, b, rtol=rtol, atol=atol))
