# Phase 4B — Refined Asymptotic Boundary via Regular Variation

**Date:** 2026-10-28  
**Correction:** 2026-10-28 (exponent ranges audited)

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

## Corrected regular-variation classification

Assume \(\rho\ge 0\), locally integrable, and
\[
\rho(s)\sim s^{-\alpha}L(s),\qquad s\to\infty,
\]
with \(L\) slowly varying. The Stieltjes-transform asymptotic
\[
\Sigma(k)\sim c\,k^{-2\alpha}L(k^2)
\]
(and therefore \(\mathcal{I}(k)\to-2\alpha\)) applies in the non-integrable range under standard Tauberian conditions (monotone density or regular variation with index in \((-1,0)\) after the change of variables, etc.). It does **not** override the finite-moment theorem when the tail is integrable.

| Tail exponent \(\alpha\) | Total weight \(M_0\) | Leading limit of \(\mathcal{I}\) | Notes |
|--------------------------|----------------------|----------------------------------|-------|
| \(\alpha<1\) | Divergent | \(-2\alpha\) | Under regular-variation / Tauberian conditions on the Stieltjes transform |
| \(\alpha=1\) | May be finite or divergent depending on \(L\) | Typically \(-2\) | Rate controlled by the integrated tail of \(L\); see exact example |
| \(\alpha>1\) | Finite | \(-2\) | Finite-moment theorem applies; power-law formula does not override |
| \(\alpha\le 0\) | Generally divergent | Separate analysis required | Do not extrapolate the \(-2\alpha\) formula automatically |

**Important:** When \(\alpha>1\) the tail is integrable at infinity, so \(M_0<\infty\) (assuming local integrability) and the finite-moment theorem forces \(\mathcal{I}\to-2\). The power-dependent limit belongs only to the non-integrable range \(\alpha<1\).

## Behavior of the normalized correction \(\mathcal{J}\)

\(\mathcal{J}(k)\) is finite in the limit only when the first moment converges (or under a stronger integrated-tail condition). Divergence of \(M_1\) does not follow automatically from the leading limit of \(\mathcal{I}\); it depends on the detailed tail. On the borderline \(\alpha=1\) with \(L\equiv 1\), \(\mathcal{J}\to\infty\) as shown by the exact example. For other slowly-varying factors the rate must be derived separately.

## What forces \(\mathcal{I}\to-2\)

Sufficient conditions:
1. \(M_0<\infty\) (includes all \(\alpha>1\)).
2. Regular variation of index \(-1\) under conditions that make the Stieltjes transform produce a logarithmic factor (includes the exact example).

The original failed-universality claims for \(\mathcal{I}\) and \(\mathcal{J}\) as constants independent of all spectra remain failed. This correction is a refinement of the sufficient conditions, not a reinterpretation of those failures.
