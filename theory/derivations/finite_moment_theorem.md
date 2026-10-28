# Finite-Moment Theorem and Spectral-Tail Classification

**Date:** 2026-10-28  
**Phase:** 4A

## 1. Finite-moment theorem

Let \(\rho(s)\ge 0\) and assume the zeroth moment is finite:
\[
M_0 := \int_0^\infty \rho(s)\,ds < \infty.
\]
Define
\[
\Sigma(k) = \int_0^\infty \frac{\rho(s)}{k^2 + s}\,ds.
\]

**Leading asymptotic.** For \(k\to\infty\),
\[
\Sigma(k) = \frac{M_0}{k^2} \Bigl(1 + O\bigl(\tfrac{M_1}{M_0 k^2}\bigr)\Bigr)
\]
whenever the first moment \(M_1 = \int s\rho(s)\,ds\) is also finite.  
In all cases with only \(M_0<\infty\),
\[
k^2\Sigma(k)\to M_0.
\]
**Proof sketch.** Write
\[
k^2\Sigma(k) - M_0 = -\int_0^\infty \rho(s)\frac{s}{k^2+s}\,ds.
\]
The integrand is dominated by \(\rho(s)\) and tends pointwise to 0. By the dominated-convergence theorem the integral tends to 0. Hence \(k^2\Sigma(k)\to M_0\).

**Logarithmic derivative.** Differentiating the asymptotic form (or by direct differentiation under the integral under mild conditions) yields
\[
\mathcal{I}(k) = \frac{d\ln\Sigma}{d\ln k} \to -2
\]
as \(k\to\infty\).

The leading limit \(\mathcal{I}(k)\to-2\) therefore holds for every nonnegative density with finite total spectral weight \(M_0\). It does **not** require a specific tail exponent.

## 2. Spectral-tail classification

| Class | Example | \(M_0\) | Leading \(\Sigma(k)\) | \(\mathcal{I}(k)\to\) | Notes |
|-------|---------|--------|-----------------------|----------------------|-------|
| Compact support | uniform on \([0,s_c]\) | finite | \(M_0/k^2\) | \(-2\) | Exponentially small corrections |
| Exponential decay | \(e^{-s/s_0}\) | finite | \(M_0/k^2\) | \(-2\) | Power-series corrections in \(1/k^2\) |
| Power-law, finite \(M_0\) | \(s^\alpha e^{-s}\), \(\alpha>-1\) | finite | \(M_0/k^2\) | \(-2\) | Subleading depends on moments |
| Power-law, divergent \(M_0\) | \(1/(1+s)\) | divergent | \(\sim (\ln k)/k^2\) | \(\to-2\) still, but slowly | Logarithmic correction |
| Discrete (delta) | \(\delta(s-m^2)\) | finite | \(1/(k^2+m^2)\) | \(-2k^2/(k^2+m^2)\to-2\) | Exact single-field case |
| Mixture | discrete + continuous | depends | superposition | \(\to-2\) if total \(M_0<\infty\) | Leading universal; coefficients additive |

**Counterexample to a universal constant:** any density with \(M_0=\infty\) can produce a slower approach or a different subleading term, but the pure power \(\Sigma\sim c/k^2\) with \(c\) independent of the tail shape already fails when \(M_0\) diverges.

**Logarithmic corrections:** for \(\rho(s)\sim 1/s\) the integral produces \(\Sigma(k)\sim (\ln k)/k^2\), so
\[
\mathcal{I}(k) = -2 + \frac{1}{\ln k} + \cdots.
\]
The limit is still \(-2\), but the rate is only logarithmic.

## 3. Normalized correction \(\mathcal{J}(k)\)

\[
\mathcal{J}(k) := k^2\bigl[\mathcal{I}(k)+2\bigr].
\]
When \(M_0\) and \(M_1\) are finite,
\[
\mathcal{J}(k)\to \frac{M_1}{M_0}
\]
(up to a conventional factor of order 1 that depends on the precise differentiation).  
The limiting value depends on the first moment ratio and is therefore **spectrum-dependent**. It is not universal.

## 4. Boundary between universal and spectrum-dependent behavior

- **Universal (under \(M_0<\infty\)):** the leading power \(\Sigma\sim M_0/k^2\) and the limit \(\mathcal{I}\to-2\).
- **Spectrum-dependent:** the value of \(M_0\), all subleading coefficients, the rate of approach, and the limit of \(\mathcal{J}(k)\).
- **Outside the finite-moment class:** the leading coefficient itself may diverge or acquire logarithms; the pure \(1/k^2\) scaling with a finite prefactor ceases to hold.

This classification is the result of the phase. No new physical law is claimed.
