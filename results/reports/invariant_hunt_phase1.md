# Invariant Hunt — Phase 1–2 Report

**Date:** 2026-10-28  
**Repository:** beyond-repair/coherence-dynamics

## Exact mathematical results

1. **Gaussian elimination** (Euclidean quadratic action):
   \[
   K_{\mathrm{eff}}(k) = K_\phi(k) - \frac{g^2}{K_\chi(k)}
   \]
   Exact when both fields are free and the mixing is bilinear.

2. **Two-field massive case:**
   \[
   \Sigma(k) = \frac{g^2}{k^2 + m_\chi^2}, \qquad
   K_{\mathrm{eff}}(k) = k^2 + m_\phi^2 - \Sigma(k)
   \]

3. **Candidate logarithmic derivative:**
   \[
   \mathcal{I}(k) = \frac{d\ln|\Sigma|}{d\ln k} = -\frac{2k^2}{k^2 + m_\chi^2}
   \]
   Closed form; independent of \(g\); depends on \(m_\chi/k\).

4. **Stability:** \(K_{\mathrm{eff}}(0) > 0\) is required for the quadratic model to be positive definite at vanishing momentum.

5. **Expansions:**
   - Low \(k\): \(K_{\mathrm{eff}}(0) = m_\phi^2 - g^2/m_\chi^2\), second derivative \(2 + 2g^2/m_\chi^4\).
   - High \(k\): \(\Sigma(k) \sim g^2/k^2\).

## Model-dependent findings

- \(\mathcal{I}(k)\) is an exact property of this particular kernel, not a structural invariant of all effective responses.
- Dimensionless ratios \(\Sigma(k)/k^2\) inherit the same mass-ratio dependence.
- Positivity depends on the relative size of \(g\), \(m_\phi\), and \(m_\chi\).

## Asymptotic / numerical evidence

- \(\mathcal{I}(k) \to -2\) as \(k/m_\chi \to \infty\) (power-law tail of the bubble).
- \(\mathcal{I}(k) \to 0\) as \(k \to 0\).
- Numerical tests confirm the analytic expression to machine precision.

## Unresolved

- Whether any other candidate (spectral moments, RG invariants, geometry ratios) survives across distinct models.
- Causal real-time continuation of the Euclidean result.
- Mapping from graph-resolvent quantities to continuum self-energies.
- Existence of a nontrivial invariant that is independent of microscopic parameters within a stated class.

## Physical predictions

None. No covariant theory, no observable, and no comparison to data have been performed. The historical Ware Constant is not used.

## Next

Phase 3: implement at least two additional models (free field, multi-field, or continuum spectral density) and apply Gates C–D.  
Phase 4: compute resolvent and moment ratios on the existing gasket laboratory and record which quantities are exact graph identities.
