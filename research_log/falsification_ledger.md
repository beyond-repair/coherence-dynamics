# Falsification Ledger

**Date:** 2026-10-28

## Rejected candidates

### \(\mathcal{I}(k) = d\ln|\Sigma|/d\ln k\) as universal invariant

- **Model tested:** Gaussian two-field (exact).
- **Result:** \(\mathcal{I}(k) = -2k^2/(k^2+m_\chi^2)\).
- **Gates failed:** C (depends on \(m_\chi\)), D (counterexample: free field \(\Sigma=0\); different spectral density changes functional form).
- **Status:** FAILED as universal claim. Retained as exact model-specific result.
- **Counterexample domain:** Any theory whose induced self-energy is not proportional to \(1/(k^2+m^2)\).

### \(\mathcal{I}(k)\) as universal scaling function independent of unresolved spectrum

- **Models tested:** Multi-field Schur complement; continuum spectral densities with different power-law exponents.
- **Result:** Overall coupling rescaling drops out of \(\mathcal{I}\) (log-derivative artifact). Change of mass spectrum or of \(\rho(s)\) changes the value and functional form of \(\mathcal{I}(k)\).
- **Gates failed:** D (model robustness).
- **Status:** FAILED for the tested Gaussian and continuum classes. No retrospective redefinition.

### \(\mathcal{J}(k)=k^2[\mathcal{I}(k)+2]\) as universal constant

- **Result of Phase 4A:** When \(M_1<\infty\), \(\mathcal{J}(\infty)\) equals a moment ratio \(M_1/M_0\) (up to convention). The value depends on the density.
- **Status:** FAILED as universal. The leading limit \(\mathcal{I}\to-2\) under finite \(M_0\) is retained as a proven asymptotic result.

## Established asymptotic results (not claims of new physics)

- If \(M_0=\int\rho<\infty\), then \(k^2\Sigma(k)\to M_0\) and \(\mathcal{I}(k)\to-2\) (sufficient condition).
- Phase 4B refinement: finite \(M_0\) is not necessary. Densities regularly varying of index \(-1\) (including \(\rho(s)=1/(1+s)\)) still satisfy \(\mathcal{I}\to-2\), with logarithmic approach rate; \(\mathcal{J}\) diverges in the exact example.
- **Corrected range (2026-10-28):** the power-dependent limit \(\mathcal{I}\to-2\alpha\) applies only for non-integrable tails \(\alpha<1\) under Tauberian conditions. For \(\alpha>1\) the finite-moment theorem forces \(\mathcal{I}\to-2\). The earlier blanket statement for all \(\alpha\neq 1\) is withdrawn.
- Subleading coefficients, approach rates, and \(\mathcal{J}\) remain spectrum-dependent and require separate tail conditions.

## Open candidates

- Precise approach rates for general slowly-varying factors at \(\alpha=1\).
- Higher-order normalized corrections.
- Spectral moment ratios on finite graphs (exact identities; continuum limit open).
- RG fixed-point exponents (not yet computed).

No retrospective redefinition of any failed candidate has been performed. The correction concerns only the statement of the regular-variation classification.
