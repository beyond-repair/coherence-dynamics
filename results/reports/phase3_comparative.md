# Phase 3 Comparative Report — Schur Complement vs Continuum Spectral Density

**Date:** 2026-10-28  
**Status:** Discriminating comparison completed. No universal constant found. Scaling-function dependence recorded.

## Exact structural results

### Multi-field Gaussian (Schur complement)

For a quadratic Euclidean action partitioned into retained and unresolved blocks,
\[
K_{\mathrm{eff}}(k) = A(k) - C(k)\, B(k)^{-1}\, C(k)^\dagger.
\]
This is exact. It reduces to the single unresolved field when \(B\) and \(C\) are scalars.

**Property that survives arbitrary overall rescaling of the coupling matrix \(C \to \lambda C\):**
The logarithmic derivative
\[
\mathcal{I}(k) = \frac{d\ln|\Sigma|}{d\ln k}
\]
(using the trace of \(\Sigma\) as a scalar proxy) is independent of \(\lambda\).  
Reason: \(\Sigma \propto \lambda^2\), and the constant factor cancels under the logarithmic derivative.  
This is a property of the logarithmic derivative, not evidence of cross-model universality.

**Property that does not survive:**
The functional form of \(\mathcal{I}(k)\) depends on the eigenvalues of \(B(k)\) (i.e., the mass spectrum of the unresolved fields). Changing the relative entries of \(B\) changes \(\mathcal{I}(k)\).

### Continuum of unresolved modes

\[
\Sigma(k) = \int_0^\infty \frac{\rho(s)}{k^2 + s}\, ds
\]
(under the stated integrability assumptions).

**Numerical observation:**
For power-law-exponential densities \(\rho(s) \propto s^\alpha e^{-s/s_0}\),
\(\mathcal{I}(k)\) at fixed \(k\) changes when \(\alpha\) changes.  
Example (k=1): \(\mathcal{I}\approx -1.35\) (\(\alpha=0\)) versus \(\mathcal{I}\approx -0.95\) (\(\alpha=1\)).

Thus a change in the spectral density \(\rho\) changes the logarithmic slope. No constant value of \(\mathcal{I}\) is shared.

## What survives

| Property | Survives overall coupling rescaling? | Survives change of spectral density / mass spectrum? | Notes |
|----------|--------------------------------------|------------------------------------------------------|-------|
| Exact Schur form | Yes (structural) | N/A | Exact for Gaussian quadratic |
| \(\mathcal{I}(k)\) independent of overall \(\lambda\) | Yes | No | Artifact of log derivative |
| Specific numerical value of \(\mathcal{I}\) | No | No | Model-dependent |
| High-k power \(\Sigma\sim 1/k^2\) | Yes (for finite-rank or rapidly decaying \(\rho\)) | Depends on tail of \(\rho\) | Asymptotic, not a constant |

## Universal scaling function?

No universal scaling function for \(\mathcal{I}(k)\) has been identified that is independent of the unresolved spectrum.  
The single-field case \(\mathcal{I}(k) = -2k^2/(k^2+m^2)\) is recovered only when \(\rho\) is a delta function (or the Schur block is rank-1 with a single mass).  
Different \(\rho\) produce different functions of \(k/m_{\mathrm{char}}\).

## Falsification

- Candidate “\(\mathcal{I}(k)\) is a universal constant”: **FAILED** (Gate D).  
- Candidate “\(\mathcal{I}(k)\) is a universal scaling function independent of unresolved spectrum”: **FAILED** for the class of Gaussian quadratic models and continuum spectral densities tested.  
- The independence from overall coupling strength is retained as a correct but narrow mathematical observation about the logarithmic derivative.

No definitions were modified after the tests.

## Next

The spectral-to-continuum mapping remains deferred.  
A more promising direction is to identify an asymptotic regime (e.g., high-momentum tail or critical scaling) in which a specific functional form becomes independent of microscopic details, and to state the precise class of \(\rho\) for which that holds.
