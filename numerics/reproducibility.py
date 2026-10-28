"""Reproducibility utilities (seeds, manifests)."""
from __future__ import annotations

import json
from pathlib import Path


def set_seed(seed: int = 0) -> None:
    """Set NumPy random seed for deterministic runs."""
    import numpy as np
    np.random.seed(seed)


def write_manifest(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        json.dump(data, f, indent=2, sort_keys=True)
