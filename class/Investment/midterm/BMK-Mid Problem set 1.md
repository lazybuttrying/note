# 강의노트 3: Portfolio Theory and Asset Allocation

## Ch. 5(Risk, Return, and Historical Record): CFA문제 #3, 4, 5, 6

![](https://lh7-us.googleusercontent.com/65M15ig8H3UmIPsyAqxzoStXs8FYf6eOTUijtM5QKAnRckoLgkXs5S_NF4n9gnh_sHYsP62tkG2IhRuuYsal-NyJWT0nd96sgPCl-CV37MRpsldqyH2C1QdQNPvDt3RbHiM9bjXeNXaZuFfnoHfggj4)
### 3)
$E(R_X) = (0.2 \times [-20\%]) + (0.5 \times 18\%) + (0.3 \times 50\%) = 20\%$
$E(R_Y) = (0.2 \times [-15\%]) + (0.5 \times 20\%) + (0.3 \times 10\%) = 10\%$
### 4)
$\sigma_X^2 = (0.2 \times [-0.20 - 0.20]^2) + (0.5 \times [0.18 - 0.20]^2) + (0.3 \times [0.5 - 0.20]^2) = 0.0592$
$\sigma_X = 24.33\%$

$\sigma_Y^2 = (0.2 \times [-0.15 - 0.10]^2) + (0.5 \times [0.20 - 0.10]^2) + (0.3 \times [0.10 - 0.10]^2) = 0.0175$
$\sigma_Y = 13.23\%$
### 5)
$E(r) = (0.9 \times 20\%) + (0.1 \times 10\%) = 19\%$
$\therefore \$1900$
### 6) 
$0.5\cdot0.3=0.15$
## Ch. 6(Risk Aversion and Capital Allocation): #13, 14, 15, 16, 17, 18, 19

> In 13th BMK, expected rate of return is 18->12%, T-bill rate is 8->2%.
> 	> Question 17: 16% -> 10%
> 	> Question 18: 18% -> 12%

![](https://lh7-us.googleusercontent.com/wA4J-M5El80TYRjMezobqcnbib83Dn_05-T4U8BihLOpkNzF1Bq-_766i5J2KB0Lo_-o-PbkIS4hGz6kY_tAi-Hrkz_it7HwmTDUIu4Ec7Z35hJlucmqFMiIbOMLzq6WLHQaS2pyu-qXkjkCvYRnMeE)

### 13)
$E(R)=0.7\cdot0.12+0.3*0.02=0.09$
$\sigma = 0.7\cdot0.28=0.196$
### 14)
- T-bill: $20\%$
- A: $0.7*0.25=17.5\%$
- B: $0.7*0.32=22.4\%$
- C: $0.7*0.43=30.1\%$ 
### 15)
- My sharpe ratio: $S=\cfrac{0.12-0.02}{0.28}=0.3571$
- Client's Sharpe ratio $S=\cfrac{0.09-0.02}{0.196}=0.3571$
### 16)
![](resource/Pasted%20image%2020240415142822.png)
### 17)
- a) $0.10 = 0.02+w(0.12-0.02)$
	- $\therefore w =0.8$
- b)
	- T-bill: $20\%$
	- A: $0.8*0.25=20\%$
	- B: $0.8*0.32=25.6\%$
	- C: $0.8*0.43=34.4\%$ 
- c) $\sigma_C = 0.8\sigma_P=0.224$
### 18)
- a) $y=\cfrac{0.12}{0.28}=0.4286$
- b) $0.02+0.1\cdot0.4286=0.0629$
### 19) 
- a) $y=\cfrac{E(R_P)-R_f}{A\sigma^2_P}=\cfrac{0.12-0.02}{3.5\cdot0.28^2}=\cfrac{0.10}{0.2744}=0.3644$
- b) 
	- $E(R_C)=0.02+0.10\cdot0.3644=0.05644$
	- $\sigma_C=0.3644\cdot0.28=0.0158032$

## Ch. 7(Optimal Risky Portfolios): #4, 5, 6, 7, 8, 9, 10, 11, 12

![](resource/https://lh7-us.googleusercontent.com/-qtMRPjAeWSXCxgRGGIG8hVsgjcEXoKEUxwvG9ROoEj9_4O_PpXd_Ft3KDWJDkHFRoXhIbPoH5iiuoIuz8Qs6oDIXaBMUUXvmCCWCokOID6Vrxo9aB33f75vsB7pcL6xyxQF_Evz_Aj8xRAjG4hMgzI)
![](resource/Pasted%20image%2020240415175148.png)

### 4) 
- $Cov(R_S, R_B) = \rho\sigma_S\sigma_B=0.0045$ 
- $w_S = \cfrac{\sigma^2_B - Cov(R_S, R_B)}{\sigma^2_S + \sigma^2_B - 2Cov(R_S,R_B)}$
	- $=\cfrac{15^2 - 45}{30^2 + 15^2 - 2 \cdot 45}=\cfrac{180}{1035}$
	- $\therefore  \ =0.173913...$
- $w_B = 1 - w_S = 0.8261...$
- $E(R_{MV}) = (0.174 \cdot 0.20) + (0.8261 \cdot 0.12) = 0.1339$
- $\sigma_{MV}=\left [w_S^2\sigma^2_S+w_B^2\sigma^2_B + 2 w_Sw_BCov(R_S, R_B)\right ]^{1/2}$
	- $0.1739^2\cdot900+0.8261^2\cdot225+2\cdot0.1739\cdot0.8261\cdot45$
	- $=27.217089 + 153.54927225+12.9292911=193.69565245$
	- $\sqrt{193.69565245} = 13.917...$
### 5) 
| Proportion in Stock | Proportion in Bond | Expected Return | Standard Deviation | ETC    |
| ------------------- | ------------------ | --------------- | ------------------ | ------ |
| 0.00%               | 100.00%            | 12.00%          | 15.00%             |        |
| ==17.39%==          | ==82.61%==         | ==13.39%==      | ==13.92%==         | ==MV== |
| 20.00%              | 80.00%             | 13.60%          | 13.94%             |        |
| 40.00%              | 60.00%             | 15.20%          | 15.70%             |        |
| 60.00%              | 40.00%             | 16.80%          | 19.53%             |        |
| 80.00%              | 20.00%             | 18.40%          | 24.48%             |        |
| 100.00%             | 0.00%              | 20.00%          | 30.00%             |        |
### 6) 
- Expected Return is approximately 15.6%
- Standard Deviation is approximately 16.5%

![](resource/Pasted%20image%2020240414194832.png)
### 7)
- $w_S = \cfrac{ (E[R_S] - R_f) \sigma_B^2 - (E[R_B] - R_f) \times \text{Cov}(R_S, R_B) }{ (E[R_S] - R_f) \sigma_B^2 + (E[R_B] - R_f) \sigma_S^2 - (E[R_S] - R_f + E[R_B] - R_f) \times \text{Cov}(R_S, R_B) }$
	- $= \cfrac{ (.20 - .08) \times 225 - (.12 - .08) \times 45 }{ (.20 - .08) \times 225 + (.12 - .08) \times 900 - (.20 - .08 + .12 - .08) \times 45 } \approx 0.4516$
- $w_B = 1 - 0.4516 = 0.5484$
- $E[r_p] = (0.4516 \times 0.20) + (0.5484 \times 0.12) \approx 0.1561$
- $\sigma_P = \sqrt{0.4516^2\cdot900 + 0.5484^2\cdot225+2\cdot0.4516\cdot0.5484\cdot45} \approx 16.54\%$
### 8)
Sharpe Ratio: $\cfrac{E(R_P)-R_f}{\sigma_P} \approx \cfrac{0.1561-0.08}{0.1654}=0.4603$
### 9)
- a) $E[R_c] = R_f + \frac{E[R_P] - R_f}{\sigma_P} \sigma_c$
	- $0.14 = 0.08 + 0.4603\cdot\sigma_c$
	- $\sigma_c = 0.1303$
- b)  $E[R_c] = (1 - w) R_f + w E[R_P] = R_f + w  (E[R_P] - R_f)$
	- $0.14= 0.08+w(0.1561-0.08)$
	- T-bill: 0.2119
	- Risky funds: 0.7881
		- Stock: 0.7881 x 0.4516 = 0.3559
		- Bond: 0.7884 x 0.5484 = 0.4322
### 10)
- $0.14=0.20 \cdot w+ 0.12 \cdot (1-w) = 0.12 + 0.08 w$ 
- Stock 25%, Bond 75%
- $\sigma_p = \sqrt{ (0.25^2 \times 900) + (0.75^2 \times 225) + [2 \times 0.25 \times 0.75 \times 45]} \approx 14.13\%$

![](resource/Pasted%20image%2020240415175201.png)
### 11)
- a) Yes. Because of diversification. Gold has a low or negative correlation with stocks. By including gold, an investor can potentially reduce the portfolio's overall volatility. ![](resource/Pasted%20image%2020240415180943.png)
- b) Nobody holds gold. The bundle of stocks and gold becomes a line, not curve. Gold and stocks move perfectly together; Diversification benefit of holding gold with stocks disappears. ![](resource/Pasted%20image%2020240415181356.png)
- c) The set of assumptions does not represent an equilibrium for the security market, if the correlation coefficient is 1 and gold is riskier and less profitable than stocks.
	- In efficient market, gold would need to either offer a higher expected return to justify its higher risk compared to stocks or have a lower correlation with stocks to offer diversification benefits.


![](resource/Pasted%20image%2020240415175211.png)
### 12)
- In equilibrium, expected return of portfolio will be the risk-free rate, because stock A and B are perfectly negatively correlated.
- $\sigma_P = |w\sigma_A-(1-w)\sigma_B|$
	- $0 = 5w-10(1-w)$
	- $w=0.6667$
- $E(R) = 0.6667\cdot10+0.3333\cdot15=11.67\%$
- Risk rate is 11.67%


## Ch. 8(Index Models): #9, 10, 11, 12, 13, 14, 17

![](https://lh7-us.googleusercontent.com/kNXmefeyN0cgq7o6gdInmI1hB7uV-EcnlGOkeWDg60Jvw6mpiIL_TSaUlWltRQHSXpUT9-2gJhM3tDqwedUMk44l4ksr7M4C_Vs6wPLEeN2DY2v-OTU3gU2-OweROVl_GczjvOu06Mfe7CCZVA8AigM)

### 9)
$R_i^2=\cfrac{\beta_i^2\sigma_M^2}{\sigma_i^2}$
- $\sigma_A^2 = \cfrac{\beta_A^2\sigma^2_M}{R_A^2} = \cfrac{0.7^2\cdot0.20^2}{0.20}=0.098$
	- $\sigma_A = 0.3130$
- $\sigma_B^2 = \cfrac{\beta_B^2\sigma^2_M}{R_B^2} = \cfrac{1.2^2\cdot0.20^2}{0.12}=0.48$
	- $\sigma_B = 0.6926$
### 10)
- A
	- Systematic risk: $\beta_A^2 \cdot \sigma_M^2 = 0.70^2\cdot0.20^2=0.0196$
	- Firm-specific risk: $\text{Total Risk}-\text{Systematic Risk}=0.0784$
- B
	- Systematic risk: $\beta_B^2 \cdot \sigma_M^2 = 1.2^2\cdot0.20^2=0.0576$
	- Firm-specific risk: $\text{Total Risk}-\text{Systematic Risk}=0.4224$
### 11)
- $Cov(R_A, R_B) = \beta_{A}\beta_{B} \sigma^2_M = 0.70 \times 1.20 \times 0.04 = 0.0336$
- $\rho_{A,B} = \cfrac{Cov(R_A, R_B)}{\sigma_A \sigma_B} = \cfrac{0.0336}{0.3130 \times 0.6928} = 0.1549$
### 12)
- $\rho_{A,M} = \sqrt{R_A^2}$, $\rho_{B,M} = \sqrt{R_B^2}$ 
	- $\rho_{A,M} = \cfrac{Cov(R_A, R_M)}{\sigma_A \sigma_M} =\cfrac{\beta_A\sigma_M^2}{\sigma_A\sigma_M}$, where $\beta_M=1$
	- $R_A = \cfrac{\beta_A \sigma_M}{\sigma_A}$
- $Cov(R_A, R_M) = \rho_{A,M} \sigma_A \sigma_M = 0.20^{1/2} \times 0.3130 \times 0.20 = 0.0280$
- $Cov(R_B, R_M) = \rho_{B,M} \sigma_B \sigma_M = 0.12^{1/2} \times 0.6928 \times 0.20 = 0.0480$
### 13) Change in Proportion: 60% in A, 40% in B
- 9)
	- $\sigma_P^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2w_Aw_B\rho_{A,B}\sigma_A\sigma_B$
		- $=\left(  (0.6^2 \cdot 0.0980) + (0.4^2 \cdot 0.48) + [2 \cdot 0.4 \cdot 0.6 \cdot 0.3130 \cdot 0.6926 \cdot 0.1549]  \right)^{1/2}$
		- $=0.03528+0.0768+0.01611=0.1282$
	- $\sigma_P=0.1282^{1/2}=0.3580$
- 10)
	- $\beta_P = (0.6 \times 0.7) + (0.4 \times 1.2) = 0.90$
	- Systematic risk: $\beta_P^2 \cdot \sigma_M^2 = 0.90^2\cdot0.20^2=0.0324$
	- Firm-specific risk: $\text{Total Risk}-\text{Systematic Risk}=0.0958$
- 12) No change in covaraince between each stock and market
	- $Cov(R_P, R_M) = \beta_P \sigma_M^2 = 0.90 \times 0.20^2 = 0.036$
		- $\beta_P = \cfrac{Cov(R_P, R_M)}{\sigma_M^2}$
	- $Cov(R_A, R_M) = \rho_{A,M} \sigma_A \sigma_M = 0.20^{1/2} \times 0.3130 \times 0.20 = 0.0280$
	- $Cov(R_B, R_M) = \rho_{B,M} \sigma_B \sigma_M = 0.12^{1/2} \times 0.6928 \times 0.20 = 0.0480$
### 14)
- $Var(\text{T-bill})=0$, $Cov(\text{T-bill}, \text{Any Asset})=0$
- $\sigma_O^2=w_P^2 \sigma_P^2 + w_M^2 \sigma_M^2 + 2w_Pw_MCov(R_P, R_M)$
	- $=0.5^2\cdot0.1282+0.3^2\cdot0.2^2+2\cdot0.5\cdot0.3\cdot 0.036$
	- $=0.0320+0.0036+0.0108=0.0464$
- $\sigma_O = 0.2155$
- $\beta_O = (0.5 \times 0.9) + (0.3 \times 1) + (0.2 \times 0) = 0.75$
- Systematic risk: $\beta_O^2 \cdot \sigma_M^2 = 0.75^2\cdot0.20^2=0.0225$
- Firm-specific risk: $\text{Total Risk}-\text{Systematic Risk}=0.0239$
- $Cov(R_O, R_M) = \beta_O \sigma_M^2 = 0.75 \times 0.20^2 = 0.03$



![](https://lh7-us.googleusercontent.com/n0UDzgxmVGhNZVWBc9sdCmMkRn0-omBBXAuDc7gd5rvFumNwT7e2lLlA01LKTXm78tKlvVCljSpPvvRBknedumrZ7I8YlhTndYpgbAPSHdkIiLnL_2Xh-sALkGAK0Vv3usJWrXy3w8VZXks8Vv6M0dU)
### 17)
Risk free rate is T-bills' expected return: $R_f = 8\%$
Market's return is the expected return of passive equity portfolio: $E(R_M)=16\%$
##### 17-a)
- Expected excess return: $R_i-R_f$
- Alpha values: $E(R_i) -  (R_f + \beta_i [E(R_M)-R_f])$
- residual variance: $\sigma(\varepsilon_i)^2$

|     | Expected excess return | Alpha values                                 | Residual Variance |
| --- | ---------------------- | -------------------------------------------- | ----------------- |
| A   | 20% - 8% = 12%         | $20\% - (8\% + 1.3 × [16\% - 8\%]) = 1.6\%$  | $0.58^2=0.3364$   |
| B   | 18% - 8% = 10%         | $18\% - (8\% + 1.8 × [16\% - 8\%]) = -4.4\%$ | $0.71^2=0.5041$   |
| C   | 17% - 8% = 9%          | $17\% - (8\% + 0.7 × [16\% - 8\%]) = 3.4\%$  | $0.60^2=0.36$     |
| D   | 12% - 8% = 4%          | $12\% - (8\% + 1.0 × [16\% - 8\%]) = -4\%$   | $0.55^2=0.3025$   |

##### 17-b) Use Treynor-Black model
**For an actively managed portfolio A, comprising four assets A, B, C and D**

|       | $\cfrac{\alpha_i}{\sigma(\varepsilon_i)^2}$ | $w_i= \cfrac{\alpha_i}{\sigma(\varepsilon_i)^2} / \text{Total}$ |
| ----- | ------------------------------------------- | --------------------------------------------------------------- |
| A     | 1.6% / 0.3364 = 0.0476                      | 0.0476 / (-0.0775) = -0.6136                                    |
| B     | -4.4% / 0.5041 = -0.0873                    | -0.0873 / (-0.0775) = 1.1261                                    |
| C     | 3.4% / 0.36 = 0.0944                        | 0.0944 / (-0.0775) = -1.2185                                    |
| D     | -4% / 0.3025 =0.1322                        | 0.1322 / (-0.0775) = 1.7060                                     |
| Total | -0.0775                                     | 1                                                               |

-  Portfolio A's alpha is $\alpha = \Sigma_i w_i \alpha_i$
$\alpha_A = (−0.6142 \times 1.6) + (1.1265 \times [− 4.4]) + (-1.2181 \times 3.4) + (1.7058 \times [− 4.0])= −0.169$
- Portfolio A's beta is $\beta = \Sigma_iw_i\beta_i$
$\beta_A = (−0.6142 \times 1.3) + (1.1265 \times 1.8) + (-1.2181 \times 0.70) + (1.7058 \times 1) = 2.0824$
- Portfolio's residual variance is $\sigma(\varepsilon)^2 = \Sigma_iw_i^2\sigma(\varepsilon)^2$
$\sigma(\varepsilon)^2  = ([-0.6142]^2 \times 0.3364) + ([1.1265]^2 \times 0.5041) + ([-1.2181]^2 \times 0.3600) + ([1.7058]^2 \times 0.3025)$
$=0.1269+0.6397+0.5342+0.8802=2.1809$
$\therefore \sigma(\varepsilon)=1.4768$


- Initial position in the portfolio A
$w_A^0 = \cfrac{\frac{\alpha_A}{\sigma(\varepsilon_A)^2}}{\frac{E(R_M)-R_f}{\sigma_m^2}} = \cfrac{\frac{-0.169}{2.1809}}{\frac{0.08}{0.23^2}}=-0.0513$ 
- Adjusted (for beta) position in A
$w_A^* =\cfrac{w_A^0}{1+(1-\beta_A)w_A^0}=\cfrac{-0.0513}{1+(1-2.08)(-0.0513)}=-0.0486$
$w^*_M=1-w^*_A=1.0486$

- Optimal risky portfolio P
$\beta_P = w^*_M +w^*_A\beta_A=1.0486+(-0.0486)(2.0824)=0.9474$
$E(R_P)=\beta_P E(R_M)+w^*_A\alpha_A= 0.9474\times0.16 +(-0.0486)\times(-0.169)=0.1598$

### c)
- Information ratio: $\cfrac{\alpha}{\sigma(\varepsilon)}=\cfrac{0.169}{1.4768}=-0.1145$
- Market's sharpe ratio:  $S_M=\cfrac{0.08}{0.23}=0.3478$
- Sharpe ratio increases by active management with added ability to pick stocks
$S_P^2 = S_M^2 + \frac{\alpha_A^2}{\sigma(\varepsilon_A)^2}= 0.3478^2+(-0.1145)^2=0.1341$
$S_P = 0.3662$

#### d)
$S_P-S_M=0.0184$

### e) 

- $\beta_P = w_M + (w_A \times \beta_A) = 1.0486 + (-0.0486) \times 2.08 = 0.9474$
- $E(R_P) = w_A \alpha_P + \beta_P [E(R_M)-R_f] = ([-0.0486] \times [-16.90\%]) + (0.9474 \times 8\%) = 8.40\%$
- $\sigma^2_P = \beta^2_P \sigma^2_M + \sigma^2(\varepsilon_P) = (0.9474^2 \times 0.23^2) + ([-0.04856]^2 \times 2.1809) = 0.0526$
- $\sigma_P = 0.2294$

By $A=2.8$ and $y=\cfrac{E(R_P)}{A\times \sigma_P^2}$
- Optimal position in this portfolio: $y_P = \cfrac{0.084}{2.8 \times 0.0526} = 0.5671$
- Optimal position with a passive strategy: $y_M = \cfrac{0.08}{2.8 \times 0.23^2} = 0.5401$
- The difference is $0.5671-0.5401 = 0.027$

Whole position

| A       | $y_P\times w_A^*w_A$ | 0.0169  |
| ------- | -------------------- | ------- |
| B       | $y_P\times w_A^*w_B$ | -0.0310 |
| C       | $y_P\times w_A^*w_C$ | 0.0336  |
| D       | $y_P\times w_A^*w_D$ | -0.0470 |
| T-Bills | $1-y_P$              | 0.4329  |
| Market  | $y_P \times w_M^*$   | 0.5947  |

---
# 강의노트 4: Asset Pricing Models and Market Efficiency

## Ch. 9(Capital Asset Pricing Model): #17, 18, 19; CFA문제 #12 

![](https://lh7-us.googleusercontent.com/HKZBR-g6MCPDtUcHvj2HyTgb4ZsbCUroSxG7jGoXn0CJiz6ySjPop6YBEaAIzX8v2wFBL6VLn883Ufaq9xfNgPkfbTID8oW6c1jyeDA7NMk4udcuPL_DV71eD0jHP5y0z-PZufM1RhrcM2kgzUxGMxw)


### 17)
- $E(R_i) = R_f + \beta(E(R_i)-R_f) =0.06 + 1.2(0.16-0.06)=0.18$
- $0.18=\cfrac{P_1-P_0+D_0}{P_0}=\cfrac{P_1-50+6}{50}$
- $P_1=53$
### 18) 
- $0.06+0.5 \times (0.16-0.06) = 0.11$
- $0.06+1 \times (0.16-0.06) = 0.16$
- $\text{Present Value} = \cfrac{\text{Cash Flow}}{\text{Discount rate}}$
	- $PV_{\beta=0.5} = \cfrac{1000}{0.11} =9,090.909090909091$
	- $PV_{\beta=1} = \cfrac{1000}{0.16} = 6250$
- $9,090.909090909091-6250=2840.909090909091$
### 19)
- $0.06+ \beta \times (0.16-0.06) = 0.04$
- $\beta = -0.2$

![](https://lh7-us.googleusercontent.com/FKXQj62C78d-kxmIl7Yjex03y5aEPKQ4gKz00qf5OpFrsFBiCW8VI75lBFi4EsTTJitxDYOaUL_d-hpJjyHiVASE83nV3yXZs3VcxfhFs-xcK7iVZBsAAT5PAcBqEgFnwp1R6yITv7Zv-kSGs3gkxjo)

### 12)
- a)
	- Stock X
		- Expected Return: $0.05 + 0.8(0.14-0.05)=0.122$
		- Alpha: $0.14-0.122=0.018$
	- Stock Y
		- Expected Return: $0.05 + 1.5(0.14-0.05)=0.185$
		- Alpha: $0.17-0.185=-0.015$
- b) 
	- i) Stock X because it's beta is more close to market index's beta than stock Y. Market index has only systematic risk. It's unsystematic risk goes zero due to diversification. 
	- ii) Stock Y because it has higher expected return and lower standard deviation than stock X. (Low Volatility Effect) Additionally, stock Y has bigger sharpe ratio than stock X. It means that stock Y is better investment target.
		- X: $\cfrac{0.14-0.05}{0.36}=0.25$ < Y:$\cfrac{0.17-0.05}{0.25}=0.48$
## Ch. 10(Arbitrage Pricing Theory): #5, 10; CFA문제 #1, 2, 7, 8 

![](https://lh7-us.googleusercontent.com/154Oz-f9B2bP1MVUVgojqWnkjj1CbtuymKoq3_Od4cDQSTV6mnL3va_vhSQcAFwbzHHNQgxQgTMfSfNF4k-btN6NxtE9ugQDsb68ibffE2cGYbQb79zD_rmOVswHUbymKx5eVZOStGi2gMuyacqCjwg)
### 5) 
Ratio of risk premium to beta
- A: $\cfrac{0.12-0.06}{1.2}=0.05$
- E: $\cfrac{0.08- 0.06}{0.6}=0.0333$ is lower than A
It means that an arbitrage opportunity exists. Create a new portfolio G which has the identical beta with E, 0.6.
- If new portfolio is combined  in equal-weight between A and F
	- Expected return: $0.5\cdot0.12+0.5\cdot0.06=0.09$
	- Beta: $0.5\cdot1.2+0.5\cdot0=0.6$  through $\beta_A+\beta_F=0$
- $E(R_{new})-E(R_E)=0.09-0.08=0.01$ is the profit for the arbitrage
Therefore, go long on portfolio G and go short on portfolio E


![](https://lh7-us.googleusercontent.com/beycvQa2eZfkGoSoBSq9yNERZvmdRZDdK-zYhuF69qX4KSMivtwYe7YXuoZYz653nrgIOObpimOhwQGxUftTzQ2dholH4LJfH1bM5WR6545r3jqJ-ekQYSBHU78wWGezds_pr5ALc6bsj_XP9jW-V-U)![](https://lh7-us.googleusercontent.com/8Kw9cNQrF9Gw2WUUGimOJHHEGEWCCOc71FyIammkA1bvRcDekYYa_4bsRtpMBEyEF1jCZfoQ3VmCFoTeYfTZ5JyIJ6Ys4d0ELoL-9tS6_Sf94x4Su8RmnvM0RskpU9iV0gjh6G11Cdpg-fdm4mtMTxQ)
### 10) 
- a) $0.06+1.2\cdot0.06 +0.5\cdot0.08+0.3\cdot0.03=0.06+0.072+0.04+0.009$
	- $\therefore 0.452$
- b) $1.2(0.04-0.05)+0.5(0.06-0.03)+0.3(0-0.02)=-0.12+0.015-0.006=0.111$
	- $\therefore 0.452-0.111=0.341$

![](https://lh7-us.googleusercontent.com/M7DkHtTSL57bAOGIFSHe83xDJse9gaaz0MATDuWFPdsL9s6asSxPeGhHAorsYVoSPJF9tjyU8_wdtf8SZ1NLSqx-f8gwtm699oQQYewQz6m4UGd2uX4fbwWMMKhMS31WzBzcFJRt7SjpniVbGcOlRvo)![](https://lh7-us.googleusercontent.com/geCDSR2N-7ZAoaw-iNoLXPq3K8oVqNbfuFB_56txPxi2HI3FptcNE3G-OtK5BhEaATydqwIVsKyUsVQUOl1PWklYHhc4faZMpBT5vnHf6I636BKWu4fVXBDb53m07ttt9Me9AAe0DmgWCA3mU9utnNU)
### 1) 
- a) Incorrect: Only CAPM requires a mean-variance efficient market portfolio
- b) Incorrect: Only CAPM assumes normally distributed security returns
- c) Correct: One-factor APT is equivalent to the CAPM with a market portfolio
### 2)
Answer is b. 
- We can derive expected return of market from X
	- $0.16 = 0.08 + 1(E(R_M)-0.08)$
	- $E(R_M)=0.16$
- Expected Return is overpriced compared to value from calculation
	- $E(R_Y) = 0.08+0.25(0.16-0.08)=0.10$
- Therefore, it offers an arbitrage opportunity

![](https://lh7-us.googleusercontent.com/tZ2C9Lo43x_OqDx3bgpuv2zNPqppasYVJlsxTmNOrIj1nQSeizq8Fb-Bl1Bra7AZ2PZnqnB7PCQuhmcIjVjaifCUch8BgwZBJ3RTq8Rw5UShnGE3l664XBGRHjZFSUID4SBYFgempHQbm5qWqiLGlSM)
### 7)
The answer is d
- a) APT does indeed take into account multiple factors but CAPM does not.
- b) Measurement of the risk-free rate of return is not specific to APT; Both APT and CAPM use the risk-free rate in their calculations.
- c) While variability of coefficients is an important aspect, it is not a distinguishing feature over CAPM, since CAPM's beta is also variable over time.
- d) The most significant feature that differentiates APT from CAPM is the use of multiple factors to explain returns, as opposed to CAPM's single market index. APT's framework allows for the inclusion of several macroeconomic, fundamental, or statistical factors, each affecting the asset's return differently and providing a more nuanced view of an asset's risk profile.
### 8)
The answer is d
- a) CAPM assumes that markets are in equilibrium, whereas APT does not necessarily require that markets are in equilibrium to be applicable.
- b) APT uses risk premiums based on multiple factors that could be macroeconomic in nature, not necessarily just "micro" variables.
- c) While APT is based on multiple factors, it does not specify the exact number of factors; rather, it leaves the number and nature of these factors to be determined empirically.
- d) One of the key distinctions of APT is that it does not require the restrictive assumptions concerning the market portfolio that CAPM does. CAPM relies on the concept of a market portfolio and assumes all investors will hold a combination of the risk-free asset and the market portfolio. On the other hand, APT does not require any specific assumptions about the composition of the market portfolio or that such a portfolio is even held by all investors.