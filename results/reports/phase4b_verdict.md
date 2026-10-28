# Phase 4B Verdict — Closed

**Date:** 2026-10-28  
**Final scope correction:** 2026-10-28  
**Status:** Phase 4B closed

## Refined statement

Finite total spectral weight \(M_0\) is a **sufficient** condition for the universal leading slope \(\mathcal{I}(k)\to-2\).  
It is not necessary.

## Exact borderline result

For \(\rho(s)=1/(1+s)\):
\[
\Sigma(x)=\frac{\ln(1+x)}{x},\qquad
\mathcal{I}(x)\to-2,\qquad
\mathcal{J}(x)\to\infty.
\]

## Final theorem (closure)

Let \(\rho\) be locally integrable and nontrivial, with \(\rho(s)\sim s^{-\alpha}L(s)\) as \(s\to\infty\), where \(L\) is positive and slowly varying. For the ordinary Stieltjes integral to converge at infinity under this power-law model, require \(\alpha>0\).

- For \(0<\alpha<1\), under applicable regular-variation conditions, \(\Sigma(k)\) has leading behavior proportional to \(k^{-2\alpha}L(k^2)\), giving \(\mathcal{I}(k)\to-2\alpha\).
- For \(\alpha>1\), the tail is integrable; if the full spectral density has finite, nonzero \(M_0\), then \(\mathcal{I}(k)\to-2\).
- For \(\alpha=1\), classify according to the integrated slowly varying tail and whether \(M_0\) is finite. Do not assert a universal convergence rate without further assumptions.

The behavior of \(\mathcal{J}(k)\) requires a separate asymptotic analysis.

## Status of prior candidates

- \(\mathcal{I}\) as a universal constant independent of all spectra: still FAILED.
- \(\mathcal{J}\) as a universal constant: still FAILED.
- The leading limit \(\mathcal{I}\to-2\) under the sufficient conditions above: retained as a proven asymptotic theorem.

No definitions were altered. No gravitational interpretation is introduced.  
General slowly-varying rates at \(\alpha=1\) are a bounded follow-up, not a blocker.  
Phase 4B is closed.
