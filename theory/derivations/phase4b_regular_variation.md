# Phase 4B — Refined Asymptotic Boundary via Regular Variation

**Date:** 2026-10-28

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

## Regular variation

A nonnegative measurable function \(L\) is slowly varying if
\[
\frac{L(\lambda t)}{L(t)}\to 1\qquad(t\to\infty)\quad\text{for every }\lambda>0.
\]
Consider densities of the form
\[
\rho(s)\sim s^{-\alpha}L(s),\qquad s\to\infty,
\]
with \(L\) slowly varying.

- If \(\alpha>1\), then \(M_0<\infty\) and the Phase 4A theorem applies: \(\mathcal{I}\to-2\).
- If \(\alpha=1\) and \(L\) is slowly varying (e.g., \(L\equiv 1\) or \(L=\ln\)), then \(M_0=\infty\) but \(\mathcal{I}\to-2\) still holds, with a rate controlled by \(L\).
- If \(\alpha<1\), the leading decay of \(\Sigma\) is slower than \(1/k^2\) and \(\mathcal{I}\to-2\alpha\) (or a related value determined by the Tauberian theorem for the resolvent).

**Tauberian reminder (Karamata / monotone density).**  
Under regular variation of index \(-\alpha\) with \(\alpha\in(0,2)\),
\[
\Sigma(k)\sim c\,k^{-2\alpha}L(k^2)
\]
(with an explicit constant \(c\) depending on \(\alpha\)). Consequently
\[
\mathcal{I}(k)\to-2\alpha.
\]
Only the case \(\alpha=1\) (including slowly-varying factors) yields the limit \(-2\).

## What forces \(\mathcal{I}\to-2\)

Sufficient conditions (any one):
1. \(M_0<\infty\).
2. \(\rho\) regularly varying with index \(-1\) (including slowly-varying multipliers).

Conditions that produce a different limit:
- Regular variation with index \(-\alpha\), \(\alpha\neq 1\): limit \(-2\alpha\).

The normalized correction \(\mathcal{J}\) remains finite only inside the stricter class \(M_1<\infty\); it diverges on the borderline \(\alpha=1\).

## Numerical checks

Representative densities confirm:
- Exponential / compact: rapid approach to \(-2\).
- \(\rho=1/(1+s)\): \(\mathcal{I}(x)+2\sim 2/\ln x\), \(\mathcal{J}\to\infty\).
- Pure power \(\rho(s)=s^{-1.5}\) (finite \(M_0\)): consistent with \(-2\).
- Pure power \(\rho(s)=s^{-0.5}\) (cut off in the ultraviolet for integrability): limit consistent with \(-1\).

All prior candidate definitions remain unchanged. The broader classification is a new theorem, not a reinterpretation of the failed universality claim.
