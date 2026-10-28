# Phase 4B — Refined Asymptotic Boundary via Regular Variation

**Date:** 2026-10-28  
**Final scope correction:** 2026-10-28  
**Status:** Phase 4B closed

## Correction to the Phase 4A boundary statement

Finite total spectral weight \(M_0<\infty\) is a **sufficient** condition for
\[
k^2\Sigma(k)\to M_0,\qquad\mathcal{I}(k)\to-2.
\]
It is **not necessary**.

| Statement | Verdict |
|-----------|---------|
| Finite \(M_0\) implies \(\mathcal{I}\to-2\) | Proven (dominated convergence) |
| Finite \(M_0\) is necessary for \(\mathcal{I}\to-2\) | False |
| Finite \(M_0\) and \(M_1\) give finite \(\mathcal{J}(\infty)\) | Yes (spectrum-dependent value) |
| \(\mathcal{J}(\infty)\) is spectrum-independent | False |

## Exact borderline example

For \(\rho(s)=1/(1+s)\) (logarithmically divergent \(M_0\)):
\[
\Sigma(x)=\frac{\ln(1+x)}{x},
\]
\[
\mathcal{I}(x)=-2+\frac{2x}{(1+x)\ln(1+x)}\longrightarrow-2,
\]
\[
\mathcal{J}(x)=x\bigl[\mathcal{I}(x)+2\bigr]=\frac{2x^2}{(1+x)\ln(1+x)}\longrightarrow\infty.
\]
The leading slope still tends to \(-2\), but the approach is only logarithmic and the normalized correction diverges.

## Final theorem statement (Phase 4B closure)

Let \(\rho\) be locally integrable and nontrivial, with
\[
\rho(s)\sim s^{-\alpha}L(s)\qquad(s\to\infty),
\]
where \(L\) is positive and slowly varying. For the ordinary Stieltjes integral to converge at infinity under this power-law model, require \(\alpha>0\).

- For \(0<\alpha<1\), under the applicable regular-variation conditions, \(\Sigma(k)\) has leading behavior proportional to \(k^{-2\alpha}L(k^2)\), giving \(\mathcal{I}(k)\to-2\alpha\).
- For \(\alpha>1\), the tail is integrable; if the full spectral density has finite, nonzero \(M_0\), then \(\mathcal{I}(k)\to-2\).
- For \(\alpha=1\), classify according to the integrated slowly varying tail and whether \(M_0\) is finite. Do not assert a universal convergence rate without further assumptions.

The behavior of \(\mathcal{J}(k)\) requires a separate asymptotic analysis and is not determined by the leading limit of \(\mathcal{I}\) alone.

This statement avoids claiming that the Stieltjes integral exists for every \(\alpha\), including nonpositive exponents. The power-dependent limit is confined to the open interval \((0,1)\). The finite-moment theorem retains precedence whenever \(M_0<\infty\).

## What forces \(\mathcal{I}\to-2\)

Sufficient conditions:
1. \(M_0<\infty\) (includes all integrable tails \(\alpha>1\)).
2. The borderline \(\alpha=1\) under conditions that produce a logarithmic factor in the Stieltjes transform (exact example included).

The original failed-universality claims for \(\mathcal{I}\) and \(\mathcal{J}\) as constants independent of all spectra remain failed. General slowly-varying rates at \(\alpha=1\) are recorded as a bounded follow-up, not a blocker for closure of this phase.
