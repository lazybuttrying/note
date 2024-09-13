# 1. Technological Links and Predictable Returns

- Technological affinity for market price discovery and firms' stock returns
### 1. Data and Variables
![](resource/Pasted%20image%2020240528122920.png)
### 2. Underlying Mechanisms
- Technology-related channels: 경기침체 영향 커서 가치 평가 어려움![](resource/Pasted%20image%2020240528123529.png)
- Investors' limited attention:  기술 정보는 이해하기 어려워서 주가 반영 지연됨 (행동재무) ![](resource/Pasted%20image%2020240528123643.png)




# 2. Prospect Theory and Stock Returns: An Empirical Test

### 1. Prospect Theory
- w는 cdf
![](resource/Pasted%20image%2020240528120452.png)
### 2. TK Variable
- Low TK Portfolio has more return than High TK Portfolio
- 모두 동등 가중치 (1/60)이지만 Prospect theory function을 거치면 양극단에서 가중치가 overweight된다. 
	- skewness라서 Mean Variance Optimzation을 적용할 수 없음
- 그러나 실상은 극단값이 일어날 확률은 매우 적음
- 그래서 수익률이 감소

![](resource/Pasted%20image%2020240528120413.png)
- TK is less powerful when we skip a month
![](resource/Pasted%20image%2020240528122242.png)

### 3. 부논문
- Prospect theory also explain an anomaly



# 3. The Disposition Effect and Underreaction to News
- Disposition effect can generate stock price "underreaction" to news and, in turn, return predictability and post-announcement price drift
![](resource/Pasted%20image%2020240528132309.png)
### 1. Capital Gains Overhang

$g_t = \cfrac{P_t-RP_t}{P_t}$: measure the unrealized capital gains and losses
- Reference Price: $RP_t=\Phi^{-1} \displaystyle\sum^t_{n=0} V_{t,t-n}P_{t-n}$: use time series of net purchases by mutual fund managers and their cost basis in a particular stock to compute a weighted average reference price
- ![](resource/Pasted%20image%2020240528135111.png)

### 2. Overhang Spread (L/S Portfolio)
- Positive Overhang Spread: Same sign on earning surprise and capital gains overhang
- Negative Overhang Spread: Different sign on earning surprise and capital gains overhang
![](resource/Pasted%20image%2020240528135323.png)

### 3. Conclusion
- Disposition Effect로 인하여 Underreaction to News
	- Disposition effect is amplified when the news and the CGO have the same sign, and when the CGO is larger in either direction.
	- Disposition effect is apparent in institutional investors.
- Alternative Hypothesis
	- CGO reflects... 
		- not only the disposition effect 
		- but also other important factors in predicting stock returns
			- loyal holders, disagreement about a stock, small and liquid stock
- None of the factor loadings is significant for the long-short overhang spread, which is consistent with returns being driven by underreaction to the initial news content, rather than reflecting systematic risk

### 4. 부논문

'IVOL puzzle 이 unrealised loss 구간에서 나타난다' 를 설명하는 그래프입니다.
A주식이 B주식보다 변동성이 큰 주식입니다. 다른 조건들은 통제되었습니다.
- **이익 영역에서의 효용 (A+ vs B+):**
	- A+와 B+의 기대 효용은 각각 $𝑈ˉ𝐴+=0.5[𝑈(𝐴1)+𝑈(𝐴2)]$와  $UˉB+=0.5[U(B1)+U(B2)]$입니다.​​
	- 효용 함수가 이익 영역에서 오목하므로, $UˉB+$ > $UˉA+$.
	- 이는 투자자가 변동성이 적은 주식(B+)을 선호함을 의미합니다.
- **손실 영역에서의 효용 (A- vs B-):**
	- A-와 B-의 기대 효용은 각각 $UˉA−=0.5[U(−A1)+U(−A2)]$와 $UˉB−=0.5[U(−B1)+U(−B2)]$입니다.​ 
	- 효용 함수가 손실 영역에서 볼록하므로, $UˉA−$ > $U^-𝐵-$.
	- 이는 투자자가 변동성이 큰 주식(A-)을 선호함을 의미합니다.

![](resource/Pasted%20image%2020240528140014.png)


**Figure 1 depicts a simple setting to illustrate how Prospect Theory risk preferences lead to a demand for high-volatility stocks in the domain of losses.**



# 4. Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers

- 주요 사항
	- High BTM 그룹에 투자한 투자자 수익률이 높다
	- 실현 수익률은 왼쪽으로 치우쳐졌다. (left skewed)
	- 예측한 승리자 그룹 long 과 패배자 그룹 short(long-short strategy)전략이 23% 수익률을 보였다
	- small & financially distressed firm을 통한 수익과 historical financial performance의 관계
	- 그리고 나머지 사진

- binary data
	- 이중에서 ROA*, CFO* 가 상관관계가 높았음. 그러나 aggregate한 F_SCORE가 더 상관계수가 높았음!
	- 변수마다 financially distressed를 의미할 수 있는 임의의 임계치를 설정하고 이에 따라 binary로 0, 1 표기되는 값들.
![](resource/Pasted%20image%2020240606235409.png)
- Findings
	- High BM 포트폴리오보다 High F_SCORE 포트폴리오 비교하니 0.075의 1% 수준에서 유의미한 값이 산출됨
	- 2번 quantiles
	- Long high Short Low F_SCORE 포트폴리오 전략도 0.230 으로 1% 유의수준에서 유의미한 값이 산출됨.
![](resource/Pasted%20image%2020240607001418.png)

