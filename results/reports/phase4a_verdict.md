# Phase 4A Verdict — Asymptotic Universality Boundary

**Date:** 2026-10-28

## Proven asymptotic results

- If \(M_0=\int\rho<\infty\), then \(k^2\Sigma(k)\to M_0\) and \(\mathcal{I}(k)\to-2\) (dominated convergence).
- The limit is independent of the tail exponent provided the zeroth moment remains finite.
- For the single-mass (delta) spectrum the approach is exact: \(\mathcal{I}(k)=-2k^2/(k^2+m^2)\).

## Results requiring additional assumptions

- Subleading expansion \(\Sigma=M_0/k^2-M_1/k^4+\cdots\) requires \(M_1<\infty\).
- The normalized correction \(\mathcal{J}(k)=k^2[\mathcal{I}(k)+2]\) approaches a moment ratio only when \(M_1<\infty\). That ratio is spectrum-dependent.

## Numerical evidence

- Compact, exponential, and soft power-law densities: \(\mathcal{I}(30)\) within 0.1 of \(-2\).
- \(\rho(s)=1/(1+s)\) (divergent \(M_0\)): slower approach; \(\mathcal{I}\) remains visibly above \(-2\) at moderate \(k\).
- Truncation and quadrature errors controlled; finite-range plateaus are not treated as proofs.

## Counterexamples

- Any density with divergent \(M_0\) fails to produce a finite limiting coefficient \(M_0\).
- \(\mathcal{J}(\infty)\) depends on \(M_1/M_0\) and is therefore not universal.

## Open hypotheses

- Precise rate of approach for borderline densities (logarithmic divergence).
- Whether higher-order normalized corrections admit a useful classification.

## Verdict

The precise boundary is the finiteness of the total spectral weight \(M_0\).  
Under that condition the leading asymptotic \(\Sigma\sim M_0/k^2\) and \(\mathcal{I}\to-2\) are universal.  
Everything else (prefactor, corrections, \(\mathcal{J}\)) remains spectrum-dependent.  

No gravitational interpretation and no spectral-to-continuum mapping are introduced in this phase.
