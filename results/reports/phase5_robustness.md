# Phase 5 — Finite-Scale Robustness

**Date:** 2026-10-28  
**Status:** Phase 5 initial result  
**Physical interpretation:** none

## Frozen baselines

Gaussian single-field, Schur-complement multi-field, and continuum Stieltjes representations remain regression tests from prior phases. Their asymptotic statements (Phase 4B closed) are unchanged.

## Structural inequality from positivity

Assume \(\rho(s)\ge 0\), not identically zero, and \(k>0\). Then
\[
\Sigma(k)=\int_0^\infty\frac{\rho(s)}{k^2+s}\,ds>0
\]
and
\[
-2 < \mathcal{I}(k) \le 0.
\]

**Proof sketch.**  
Differentiation under the integral (justified by dominated convergence for integrable tails, or by direct inspection for compact support) gives
\[
k\frac{d\Sigma}{dk}=-2k^2\int\frac{\rho(s)}{(k^2+s)^2}\,ds<0,
\]
so \(\mathcal{I}(k)=(k/\Sigma)\,d\Sigma/dk<0\).  
Moreover
\[
\mathcal{I}(k)+2=2\frac{\int\rho(s)\,s/(k^2+s)^2\,ds}{\Sigma(k)}>0,
\]
hence \(\mathcal{I}(k)>-2\).

The inequalities are strict for any density that is not a pure delta function at \(s=0\). Equality \(\mathcal{I}=-2\) is reached only in the limit \(k\to\infty\) when \(M_0<\infty\) (Phase 4A/4B).

## What the bound is and is not

- It is an exact structural consequence of \(\rho\ge 0\) at every finite \(k\).
- It is independent of the overall multiplicative strength of \(\rho\) (the scale cancels in the logarithmic derivative).
- It is independent of the number of unresolved fields when the unresolved sector is Gaussian and positive-definite (the induced \(\Sigma\) remains a positive combination of resolvents).
- It does **not** constrain the value of \(\mathcal{I}\) more tightly than the open interval \((-2,0]\) without further assumptions on \(\rho\).
- It fails as soon as \(\rho\) is allowed to change sign: the proof uses non-negativity at every step. Signed measures are adversarial counter-examples to the inequality.

## Numerical support

Sweeps over exponential, compact, and two-mass (narrow Gaussian) densities at \(k\in\{0.5,1,2,5\}\) confirm \(-2<I(k)\le 0\). Overall rescaling of \(\rho\) leaves \(I\) unchanged to numerical precision. Approach to \(-2\) from above is observed as \(k\) increases for finite-moment densities.

## Verdict

Positivity of the spectral density imposes the nontrivial finite-scale bound
\[
-2<\mathcal{I}(k)\le 0.
\]
This is a model-class theorem for nonnegative spectral measures (or positive-semidefinite unresolved blocks), not a universal constant, and not a statement about any particular physical system. Phase 4B remains closed. No gravitational mapping is introduced.
