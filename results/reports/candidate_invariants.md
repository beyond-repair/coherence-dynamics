# Candidate Invariants — Phase 2 Catalog

**Date:** 2026-10-28  
**Status:** Definitions only. No universality claimed.

## Gaussian two-field baseline (exact)

\[
\Sigma(k) = \frac{g^2}{k^2 + m_\chi^2}, \qquad
K_{\mathrm{eff}}(k) = k^2 + m_\phi^2 - \Sigma(k)
\]

### Candidate \(\mathcal{I}(k)\)

\[
\mathcal{I}(k) \equiv \frac{d \ln |\Sigma(k)|}{d \ln k} = -\frac{2 k^2}{k^2 + m_\chi^2}
\]

- **Definition:** Logarithmic derivative of the absolute induced self-energy with respect to momentum scale.
- **Domain:** \(k > 0\), \(m_\chi > 0\), Euclidean.
- **Assumptions:** Exact Gaussian elimination; free massive \(\chi\); no higher vertices.
- **Invariance type:** Exact for this model; **not** universal.
- **Counterexample:** Any model whose \(\Sigma(k)\) is not of the form \(c / (k^2 + m^2)\). The single free field has \(\Sigma = 0\). Multiple fields or a continuum spectrum change the functional form. \(\mathcal{I}(k)\) depends on \(m_\chi / k\) and approaches \(-2\) only asymptotically.
- **Parameter dependence:** Independent of \(g\) and \(m_\phi\); depends on \(m_\chi\).
- **Limits:** \(\mathcal{I}(0) = 0\), \(\mathcal{I}(\infty) = -2\).

## Other candidate classes (not yet computed)

| Class | Definition sketch | Status | Notes |
|-------|-------------------|--------|-------|
| Ratio \(\Sigma / K_0\) | \(\Sigma(k)/k^2\) | Defined | Dimensionless; model-dependent |
| Spectral moments | \(\int \rho(\lambda) \lambda^n d\lambda\) | Spectral lab only | Graph identities exist; continuum mapping open |
| RG fixed-point quantities | \(\beta(g^*)=0\), \(\gamma^*\) | Not implemented | Requires explicit RG |
| Heat-trace ratios | \(\mathrm{Tr}\,e^{-tL}\) asymptotics | Spectral lab | Exact for finite graphs; asymptotic for continuum |
| Geometry ratios | \(\lambda_{\max}\), \(\mathrm{Tr}\,L / E\) | Reproduced | Stable under refinement for free gasket; not a physical coupling |

**Rule:** Do not call a quantity universal merely because it is dimensionless.

## Falsification gates (applied to \(\mathcal{I}\))

- **Gate A (dimensional):** Passes (dimensionless).
- **Gate B (analytic reproducibility):** Passes (closed form derived and tested).
- **Gate C (parameter robustness):** Fails universality (depends on \(m_\chi\)).
- **Gate D (model robustness):** Fails (counterexample: free field, or different spectrum).
- **Gate H (predictive value):** The form is a re-expression of the input kernel; no new constraint.

**Conclusion for this candidate:** Exact mathematical result for one model; not a universal invariant.
