# Coherence Dynamics

**Mathematical physics research repository**

Investigate whether coarse-graining, physical correlations, and unresolved degrees of freedom can produce a derived effective response with observable consequences, while preserving established physics in tested regimes.

**Do not assume the hypothesis is correct.** Build the mathematics necessary to test it.

## Core Principle

Derive first. Calculate second. Compare with observation third.

No universal numerical constant, new force, modified gravity, or informational source of energy is assumed a priori. All physical effects must emerge from explicitly defined equations.

## Status

**Stage A — Audit and formalization (in progress).**

This is a research foundation, not a completed theory. Ware Constant (W ≈ 0.08) appears only as historical context from prior repositories and is not a parameter, target, or acceptance criterion here.

CI: GitHub Actions runs `pytest` on push/PR to main (see `.github/workflows/ci.yml`).

## Quick Start

```bash
git clone https://github.com/beyond-repair/coherence-dynamics.git
cd coherence-dynamics
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[test]"
pytest -q
```

## Structure

- `docs/` — Research charter, foundations, assumptions, limitations, roadmap.
- `theory/` — Notation, microscopic models, effective actions, derivations.
- `spectral/` — Graph Laplacian, gasket construction, heat trace, convergence (mathematical laboratory).
- `numerics/` — Precision, diagnostics, reproducibility.
- `experiments/` — Baseline, falsification, holdout.
- `tests/` — Analytic identities, conservation, spectral, convergence, reproducibility.
- `research_log/` — Decisions, failed candidates, provenance.
- `.github/workflows/` — CI for tests.

## Provenance

Prior work in the beyond-repair organization (coherence-drive, m2-renormalization-law, finite-gasket-spectral-derivatives, sierpinski-geometry-045, informational-flux-identity, -ware-constant-derivation, ware-constant-phenomenology) is inventoried in `research_log/provenance.md`. Results are reused only with explicit assumptions, verification status, and relationship recorded. No unsupported claims are imported.

## Evidence Labels

- ESTABLISHED: Supported by accepted theory and relevant evidence within its domain.
- DERIVED: Follows mathematically from stated assumptions.
- REPRODUCED: Independently reproduced computationally.
- SUPPORTED: Consistent with specified evidence but not uniquely established.
- HYPOTHESIS: A proposed mechanism awaiting decisive testing.
- FAILED: Violates a predefined mathematical or empirical criterion.
- UNRESOLVED: Evidence is insufficient or conflicting.

## Next Steps

See `docs/research_roadmap.md`.

---

**Atomic Dream Labs / beyond-repair** · 2026-10-29
