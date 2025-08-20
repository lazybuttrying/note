# A. Normalized Rank

Transform to 0~1 scale (0.50=midean) to mitigate the effect of outliers
$$\text{normalized rank}_i = \cfrac{\text{rank}(x_i) - 0.5}{n}$$


---

# B. Extension of Difference‑in‑Differences 
## 1. Difference‑in‑Differences 

> When $\beta$ is statistically significant, the treatment caused a change in the treated group after time $T$.

For a panel of units $i$ over time $t$, estimate:
$y_{it} = \alpha + \delta\,\mathrm{Treated}_i + \gamma\,\mathrm{Post}_t + \beta\,( \mathrm{Treated}_i \times \mathrm{Post}_t ) + \varepsilon_{it}$
- $y_{it}$: outcome for unit $i$ at time $t$
- $\mathrm{Treated}_i\in\{0,1\}$: indicator that unit $i$ is in the treatment group
- $\mathrm{Post}_t\in\{0,1\}$: indicator that time $t$ is after the true treatment date $T$
- $\beta$: the true treatment effect
- $\varepsilon_{it}$: error term

## 2-1. Placebo Regression = Add False Treatment

> The model picks up a strong effect only at the real treatment date, and no effect (or a near-zero effect) at the placebo date.

Use the same model but replace $\mathrm{Post}_t$ with a “fake” post indicator at a placebo date $T_0 < T$:$y_{it} = \alpha^* + \delta^*\,\mathrm{Treated}_i + \gamma^*\,\mathrm{PlaceboPost}_t + \beta^*\,(\mathrm{Treated}_i \times \mathrm{PlaceboPost}_t) + \varepsilon_{it}^*$
- $\mathrm{PlaceboPost}_t = \mathbf{1}\{t \ge T_0\}$
- $\beta^*$: the placebo treatment effect
- Validation Check: $\beta \gg 0 \ \text{and}\  \beta^* \approx 0$


## 2-2. Mean of DiD (Two-Period, Two-Group)

> Subtracting **removes time** trends → **pure treatment effect**

Define four group–period averages:
$$\begin{aligned} \bar Y_{1,\text{post}} &= \frac1{N_{1,\text{post}}}\sum_{i:\,\mathrm{Treated}i=1}\sum{t\ge T} y_{it},\\ \bar Y_{1,\text{pre}} &= \frac1{N_{1,\text{pre}}}\sum_{i:\,\mathrm{Treated}i=1}\sum{t< T} y_{it},\\ \bar Y_{0,\text{post}} &= \frac1{N_{0,\text{post}}}\sum_{i:\,\mathrm{Treated}i=0}\sum{t\ge T} y_{it},\\ \bar Y_{0,\text{pre}} &= \frac1{N_{0,\text{pre}}}\sum_{i:\,\mathrm{Treated}i=0}\sum{t< T} y_{it}. \end{aligned}$$
Then the **mean DiD** estimator is 
	$\text{DID} \;=\; \bigl(\bar Y_{1,\text{post}} - \bar Y_{1,\text{pre}}\bigr) \;-\; \bigl(\bar Y_{0,\text{post}} - \bar Y_{0,\text{pre}}\bigr)$
1. $\bar Y_{1,\text{post}} - \bar Y_{1,\text{pre}}$ = change in treated group
2. $\bar Y_{0,\text{post}} - \bar Y_{0,\text{pre}}$ = background change in control

Under equal weighting (no covariates beyond group and time dummies), 
whether you compute the four means or run the regression, 
you get the same average treatment‐on‐the‐treated effect.
$$\hat\beta_{\text{OLS}} \;=\; \text{DID}$$
