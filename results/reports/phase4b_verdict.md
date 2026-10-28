# Phase 4B Verdict — Sufficient but Not Necessary Condition

**Date:** 2026-10-28  
**Correction:** 2026-10-28 (exponent ranges audited)

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

## Corrected classification by regular variation index \(-\alpha\)

Assuming local integrability and the stated tail asymptotics:

| Tail exponent | \(M_0\) | Leading limit of \(\mathcal{I}\) |
|---------------|--------|----------------------------------|
| \(\alpha<1\) | Divergent | \(-2\alpha\) (under Stieltjes/Tauberian conditions) |
| \(\alpha=1\) | Depends on \(L\) | Typically \(-2\), rate set by integrated tail |
| \(\alpha>1\) | Finite | \(-2\) (finite-moment theorem; power formula does not apply) |

The power-dependent limit belongs only to the non-integrable range. When \(\alpha>1\) the finite-moment theorem takes precedence.

\(\mathcal{J}\) finiteness requires control of the first moment (or a stronger tail condition) and is not automatic from the leading limit of \(\mathcal{I}\).

## Status of prior candidates

- \(\mathcal{I}\) as a universal constant independent of all spectra: still FAILED.
- \(\mathcal{J}\) as a universal constant: still FAILED.
- The leading limit \(\mathcal{I}\to-2\) under the sufficient conditions above: retained as a proven asymptotic theorem.

No definitions were altered. No gravitational interpretation is introduced. This is a mathematical correction of the classification ranges only.
