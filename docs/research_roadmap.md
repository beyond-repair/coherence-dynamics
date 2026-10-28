# Research Roadmap

## Stage A — Audit and formalization (current)

- Document existing mathematical work and limitations (see `research_log/provenance.md`).
- Write precise research question (see `docs/research_charter.md`).
- Select one concrete microscopic model.

## Stage B — Baseline reproduction

- Reproduce established spectral results (graph Laplacian, eigenvalues, positivity bounds) using known equations.
- Add analytic checks and numerical regression tests.
- Reproduce standard effective-action identities where applicable.

## Stage C — Effective-action derivation

- Derive the effective description for the selected model.
- Record every approximation, regulator, counterterm, and assumption.

## Stage D — Consistency and falsification

- Test symmetries, conservation identities, stability, convergence, and limiting behavior.
- Reject candidates that fail necessary conditions.

## Stage E — Observable prediction

- Select one observable with reliable data and a clear baseline.
- Derive the prediction before inspecting held-out data.

## Stage F — Independent validation

- Fixed parameters, reproducible inputs, uncertainty estimates, transparent scoring.
- Compare against a baseline of comparable complexity.

## Stage G — Cross-scale extension

Only after a specific mechanism succeeds at one scale. Do not require every candidate to explain proton structure, galaxy dynamics, and lensing.

## Prioritized Next Steps

1. Complete provenance ledger.
2. Implement and test gasket Laplacian baseline (reproduce λ_max = 6, Tr L, positivity).
3. Select and fully specify one microscopic model (or document why none yet).
4. Attempt one controlled effective correction derivation.
5. Report what was actually derived versus what remains conjectural.
