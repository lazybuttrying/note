- Beta: 주가 지수 혹은 특정 지수를 추종하는 운용 방식
- Alpha: 벤치마크인 지수 대비 초과 수익을 얻기 위한 운용 방식
- Smartbeta: 과거에 Alpha라 불리던 것들이 금융 발전으로 최근에는 Beta화된 것
	- 금융의 발전과 여러 연구를 통해, 이러한 초과 수익이 배당, 소형주, 가치, 성장 등 특정한 팩터에 의해 발생하며, 사전에 정해진 규칙을 통해 이러한 팩터에 대한 노출이 투명하게 운용될 수 있음이 밝혀짐
	- 특정 factor에 portfolio를 노출시키는 전략
	- Market Capitalization Weighted Index(시가총액가중방식지수)를 이기는 것이 목표
# 1. Stock Selection Strategy

## 1) Birth of Factor

Factor는 "수익률"을 설명하기 위해 만들어낸 지표
### a. Market Factor: CAPM
- CAPM by William Sharpe, expanded from Portfolio Selection of Markowitz
- Beta of CAPM: $\beta=\cfrac{\text{cov}(x,y)}{\sigma^2_x}$ 
	- 여기서 x축을 시장 수익률(m), y축을 개별 주식의 수익률(i)로 변경 시 $\beta =\cfrac{\rho(i,m) \times \sigma_m \times \sigma_i}{\sigma^2_m} = \rho(i,m) \times \cfrac{\sigma_i}{\sigma_m}$
	- 즉, Beta = 개별 주식과 시장 수익률 간의 상관관계 X 개별 주식과 시장 수익률의 변동성 비율
- CAPM: $R_i = R_f + \beta_i \times [R_m - R_f]$
	- 개별 주식의 기대 수익률 = 국고채 등의 무위험 수익률 + (개별주식의 Beta X 시장 프리미엄)
	- 시장 프리미엄: 무위험 수익률 대비 시장의 초과 수익률
	- 따라서 베타값이 크면 클수록 개별 주식의 기대 수익률은 높으며, 시장베타는 주식 수익률에 관한 공통적 특성을 찾은 최초의 팩터
### b. Extension of Factor: 3 factor model of Fama-French 
- 소형주 효과: Small Minus Big (SMB) 대형주 대비 소형주의 초과 수익률
	- 매월 소형주 수익률과 대형주 수익률 차이의 누계
- 가치주 효과: High Minus Low (HML) 시장가치 대비 장부가치(BM: Book to market) 비율이 낮은 주식 대비 BM 비율이 높은 주식의 초과 수익
	- 가치주(High BM) 수익률과 성장주(Low BM) 수익률 차이의 누계
	- BM = PBR 역수
- 3 Factor Model
	- $R_i = R_f + \beta_i \times [R_m - R_f] + \beta_{\text{SMB}} \times \text{SMB} + \beta_{\text{HML}} \times \text{HML}$
		- $\beta_i = \beta_{\text{MKT}} = \text{종합주가지수(KOSPI) 월간 수익률} - \text{콜금리 월 환산 수익}$
		- $\beta_{\text{SMB}} = \cfrac{\text{Small Value}+\text{Small Neutral}+\text{Small Growth}}{3}$ $- \cfrac{\text{Big Value}+\text{Big Neutral}+\text{Big Growth}}{3}$
		- $\beta_{\text{HML}} = \cfrac{\text{Small Value}+\text{Big Value}}{2} - \cfrac{\text{Small Growth}+\text{Big Growth}}{2}$


## c. Row Risk Factor
- High Risk, High Return에 대비비되는 저변동성(Low Volatility) 이상현상(Anomaly)
	- Lottery Effect of Behavioral Finance?
- 대부분의 기관투자자들이 시가총액가중평균지수를 기준으로 평가 받기에, 벤치마크와의 추적 오차 문제로 인해 low beta 주식을 매수하지 않고, 단기적으로 벤치마크 대비 높은 성과를 얻기 위해 high volatility stock에 투자하는 경향이 있다. 이러한 투자자들의 행태로 인해 고변동성 주식은 고평가가 되고, 저변동성 주식은 저평가가 되어, 장기적으로 저변동성 주식의 수익률이 고변동성 주식 대비 높게 된다는 설명이다.
- 더불어 주식의 상승과 하락에 대한 비대칭성으로 인해 장기적으로 수익률의 격차가 벌어진다. 시장 하락 시 저변동성 주식은 고변동성 주식 대비 하락폭이 훨씬 작고, 시장 상승 시 고변동성 주식 대비 상승폭이 작기는 하지만 이 차이는 그리 크지 않다. 따라서 시장이 상승과 하락을 반복함에 따라 저변동성과 고변동성 주식의 수익률 차이가 점점 벌어지게 된다.
- Volatility Drag: 수익과 손해의 비대칭성, 대략 $\cfrac{1}{2} \sigma^2$ 정도
	- 산술평균과 기하평균의 차이 -> 결국 복리효과로 인해 변동성이 작을 수록 유리한 효과
		- 그래서 레버리지 상품 장기투자하면 망하는 거
	- ex) 상승 10% 후 하락 10%
		- $\cfrac{(+10\%-10\%)}{2} > [(1+10\%) \times (1-10\%)]^{\cfrac{1}{2}} - 1$ ![](resource/Pasted%20image%2020240315114725.png)

#### c-a. Idiosyncratic Volatility
- Idiosyncratic Return of Residual Return (기업의 고유수익): 기업의 과거 일별 혹은 월별 수익률을 대상으로 Fama-French 3 factor model을 이용하여 회귀분석을 실시한 후, 각각의 팩터로 설명되지 않는 잔차 $\varepsilon$. 
- Idiosyncratic Volatility(고유변동성)
	- $\begin{bmatrix} r_1 \\ r_2  \\ r_3 \\ \vdots \\ r_n \end{bmatrix} = \beta_i \begin{bmatrix} R_{m,1} - R_{f,1} \\ R_{m,2} - R_{f,2}  \\ R_{m,3} - R_{f,3} \\ \vdots \\ R_{m,n} - R_{f,n} \end{bmatrix} + \beta_{\text{SMB}} \begin{bmatrix} R_{\text{SMB},1} \\ R_{\text{SMB},2}  \\ R_{\text{SMB},3} \\ \vdots \\ R_{\text{SMB},n} \end{bmatrix} + \beta_{\text{HML}} \begin{bmatrix} R_{\text{HML},1} \\ R_{\text{HML},2}  \\ R_{\text{HML},3} \\ \vdots \\ R_{\text{HML},n} \end{bmatrix}+ \begin{bmatrix} \varepsilon_1 \\ \varepsilon_2  \\ \varepsilon_3 \\ \vdots \\ \varepsilon_n \end{bmatrix}$


### d. Momentum Factor from Behavior Economics
- Stock price follows random walk
	- 주가의 기대수익률은 0이며 예측 불가능
	- $P_{t+1} = P_t + \varepsilon_{t+1}$, where $\varepsilon$ is a random number
	- $E(P_{t+1} - P_t) = E(\varepsilon_{t+1}) = 0$
- Momentum: 물체가 한 방향으로 지속적으로 변동하려는 경향, 
	- 주식에서는 주가 혹은 이익이 추세로써, 상승 추세의 주식은 지속적으로 상승하고 하락 추세의 주식은 지속적으로 하락하는 현상
	- 투자자들은 자신에 대한 과잉신뢰(Overconfidence)로 인해 자신의 판단을 지지하는 정보에 대해서 과잉반응(Overrecation)을, 자신의 판단을 부정하는 정보에 대해서는 과소반응(Underreaction)하는 경향 => 이러한 투자자들의 비합리성으로 인해 Earnings Momentum과 Price Momentum이 생겨난다고 본다.
#### d-1. Earning Momentum

> 주가는 이익을 "느리게" 반영한다 => 주가는 실적발표에 대해 굉장히 과소반응

- PEAD: Post Earnings Announcement Drift (= SUE effect: Standardized Unexpected Earnings Effect)
	- 어닝 서프라이즈의 표준화
	- t 시점의 개별 주식 i의 SUE effect:  $\text{SUE}_{i,t} = \cfrac{e_{i,q}-e_{i,q-4}}{\sigma_{i,t}}$
		- $e_{i,q}$: 최근 발표된 기업의 분기 주당순이익 Quartely EPS
		- $e_{i,q-4}$: 4분기 전의 분기 주당 순이익
		- $e_{i,q} -e_{i,q-4}$: 비기대이익 (과거 대비 현재 주당순이익의 상승폭)
		- $\sigma_{i,t}$: 과거 8분기 동안 비기대이익의 표준편차
- 누적 초과 수익률  CAR or ABR (CAR: Cumulative Abnormal Return)
	- 이익 발표일 기준 2일 전부터 1일 후까지, 동일가중지수 대비 개별주식의 초과 수익률의 합
	- t시점에서 $\text{ABR}_{i,t} = \displaystyle\sum^{+1}_{j=-2}(r_{i,j} - r_{m,j})$
		- $r_{i,j}$: j일 주식의 수익률 (j=0은 최근의 이익 발표)
		- $r_{m,j}$: j일 동일가중지수의 수익률
- 이익 수정 Earning Revision: $\text{REV6}_{i,t} = \displaystyle\sum^5_{j=0}\cfrac{f_{i,t-j}-f_{i,t-j-1}}{p_{i,t-j-1}}$
	- 추정 평균의 증감을 전월 주가로 나타낸 값
	- $f_{i,t}$: t시점 FY1의 개별 기업 이익에 대한 애널리스트들의 추정치의 평균
	- $f_{i,t-j}-f_{i,t-j-1}$: 전월 대비 추정 평균의 증감
		- 애널리스트들이 추정치를 수정하지 않는 월의 경우 해당 값은 0이 되어 REV의 변동성이 심해진다. 이를 예방하고자 과거 6개월 REV의 moving average를 사용
	- $p_{i,t-j-1}$: 전월 주가
- 이익 모멘텀의 단점
	- 이익 발표 시점이 회사마다 다르기에, 특정 시점에 리밸런싱하면서 관찰 시 실적 발표 후 포트폴리오 편입 시까지 시차가 존재하여 어닝 서프라이즈로 인한 초기 주가 상승 효과를 누릴 수 없음
	- 애널리스트 추정치는 대형주 위주로 제약됨

#### d-2. Price momentum
> 달리는 말에 올라타라

- 자기회귀모형(autoregressive model)에 기반함: $r_{i,t} = E(r_{i,t})+\phi r_{i,t-1} + \varepsilon_{i,t}$
- 크게 단기, 중기, 장기로 나뉨 -> Return Reversal 현상이 관찰됨
	- 보통 중기 모멘텀을 사용: 과거 3~12개월 수익률이 높았던 종목이 향후에도 지속적으로 상승한다 (=trend following)
- 단기 모멘텀
	- 최근 한 주 혹은 1개월 수익률과 차기 수익률의 관계인 $\phi$가 음수로서, 과거의 단기 수익률이 높을/낮을 경우 차월 수익률이 낮은/높은 현상
- 장기 모멘텀 
	- 과거 3~5년 수익률이 낮았던 종목으로 구성된 loser portfolio가 수익률이 높았던 종목으로 구성된 winner portfolio 대비 향후 성과가 높은 형상

> +) Carhart's 4 factor mode: add Momentum factor
> $R_i = R_f + \beta_i \times [R_m - R_f] + \beta_{\text{SMB}} \times \text{SMB} + \beta_{\text{HML}} \times \text{HML} + \beta_{\text{UMD}} \times \text{UMD}$ 
> where $UMD$ is "UP Minus Down" (=cross sectional momentum), 
> 과거 수익률이 높은 종목이 낮은 종목 대비 우월한 성과를 보이더라

- Dual Momentum: 시계열 모멘텀 x 횡단면 모멘텀
	- Time series Momemtum: 과거 누적 수익률을 기준으로 수익률이 0보다 크면 Winner portfolio, 0보다 작으면 Loser portfolio로 구분
		- 0을 절대적 기준으로 나눈다고 하여 Absolute Momentum이라고도 함
	- Cross Sectional Momentum: 과거 누적 수익률이 높은 순서대로 분위수를 나누어, 기존의 테스트와 같이 분위수별 수익률을 구함
	- Dual momentum
		- cross sectional momentum 기준 Top 30%를 Winner portfolio로, Bottom 30%를 loser portfolio로
		- -> 근데 cross sectinonal momentum보다 별로임...

> Momentum 기법 자체가 Regime Switching(시장이 급격히 바뀌는) 구간에서 크게 손실을 본다는 단점.

- 고유수익 모멘텀 = residual momentum
	- 3 factor model의 회귀분석에서도 설명되지 않는 residual $\varepsilon_i$(잔차)가 존재함. 이 잔차를 기업의 고유수익으로 정의해보자
		- $R_i = R_f + \beta_i \times [R_m - R_f] + \beta_{\text{SMB}} \times \text{SMB} + \beta_{\text{HML}} \times \text{HML} + \varepsilon_i$
	- regime switching도 잘 버텨낸 factor :)

### e. High Dividend Yield Factor
- 금융 상품의 가격은 미래 현금흐름의 현재 가치의 합으로 표현된다. 주식의 경우 미래의 현금흐름을 무엇으로 정의할 것인가 자체가 불분명하다
- 배당할인모형(Gorden's Dividend Discount Model)은 주주의 입장을 대변하기 위해 미래현금흐름을 배당으로 정의한다.
	- $P = \cfrac{D_1}{r-g} = \cfrac{D_0 \times (1+g)}{r-g}$
		- 주식의 적정 가치는 현재 배당금 대비 $g$로 성장하는 등비수열의 합
		- $g$: 배당성장률 = $\text{ROE} \times (1-b)$
			- $b=\text{배당 성향}$, $1-b=사내유보비율 \ retention \ ratio$
	- 이 식을 수익률(할인률)에 대해 정리하면 다음과 같다
	- $r = \cfrac{D_0 \times (1+g)}{P_0} +g$
- 단순 주가 상승뿐만 아니라 이를 통한 현금 수익까지 고려한 총 수익에 초점을 둔다면 고배당주 장기투자일 수록 총수익 증진 효과는 늘어난다
	- Total Return Factor: $r_{t+1} = \cfrac{P_{t+1} + D_{t+1}}{P_t} - 1$
- 배당 성향 payout ratio $b=\cfrac{주당배당이익(DPS)}{주당순이익(EPS)}$를 추가해보자
	- $r=\cfrac{D_0 + D_0 \times g + P_0 \times g}{P_0} = \cfrac{D_0 + g(D_0+P_0)}{P_0} = \cfrac{D_0}{P_0} + \cfrac{(D_0+P_0)[\text{ROE} \times (1-b)]}{P_0}$
	- 배당을 많이 주는 고배당 포트폴리오의 수익률이 다소 높더라
	- 

### f. Quality Factor
- 소형주의 경우 애널리스트가 분석 보고서를 작성하거나 기관이 매매를 하는 경우가 드물다. 종목에 대한 정보가 대형주에 비해 매우 부족하여 정보가 불확실한 효율적인 형태로 남아 있고 유동성이 떨어지므로 financial risk가 높다. 이러한 소형주만의 systematic risk가 risk premium으로 반영되어 더 높은 수익률을 보인다.
	- 현재는 QMJ를 통제한다면 소형주 효과는 여전히 유효하다
		- QML(Quality Minus Junk): 퀄리티 효과, Quality Stock이 Junk Stock 대비 높은 수
		- 단순히 기대감만으로 주가가 오르는 게 아니라 실적으로 증명할 수 있는 기업 (재무제표의 안정성과 꾸준한 이익창출 능력 => ROE 높고 부채비율과 이익 변동성이 낮아야)

- F-score
	- 저PBR(=High BM) 중 회계적으로 우량한 종목군(7,8,9)일 수록 비우량한 종목군(1,2,3)보다 월등한 수익을 보임

| 지표     | 항목            | 설명                  | 점수                                |
| ------ | ------------- | ------------------- | --------------------------------- |
| 수익성    | ROA           | 당기순이익/총자산           | if ROA>0, then 1, else 0          |
|        | CFO           | 영업활동현금흐름/총자산        | if CFO>0, then 1, else 0          |
|        | ROA 변화량       | 전년 대비 ROA 증가량       | if ROA변화량>0, then 1, else 0       |
|        | Accrual       | 금년의 CFO-ROA         | if Accrual>0, then 1, else 0      |
| 재무 성과  | Leverage 변화량  | 전년 대비 장기부채/총자산 감소량  | if Leverage변화량<0, then 1, else 0  |
|        | Liquidity 변화량 | 전년 대비 유동자산/유동부채 증가량 | if Liquidity변화량>0, then 1, else 0 |
|        | EQ_Offer      | 금년도 신주 발행 여부        | if EQ_Offer<=0, then 1, else 0    |
| 운영 효율성 | Margin 변화량    | 전년 대비 매출총이익/총매출 증가량 | if Margin변화량>0, then 1, else 0    |
|        | Turn 변화량      | 전년 대비 총매출/총자산 증가량   | if Turn변화량>0, then 1, else 0      |

- QMJ: Quality Minus Junk
	- $\text{Quality} = z(\text{Profitability}+\text{Growth}+\text{Safety}+\text{Payout})$
	- 각 항목별 순위를 매긴 후, 매겨진 순위를 바탕으로 각 종목별 Z-score를 계산한다. 그 후, 지표별로 Z-Score를 합한 후, 합한 값들을 바탕으로 최종 Z-score를 구한다. 즉,  4개 항목의 Z-Score 합계가 최종 우량성이다.
	- 연구 결과, 우량한 기업일 수록 장부가 대비 시장가가 높아 상대적으로 주식 가격이 높았다.
	- 우량주를 매수하고 불량주를 공매도 하는 QMJ 전략은 유의미한 수익을 거두어 HML factor와 별도로 Quality factor는 수익률과 높은 연관이 있다.

| 지표  | 항목       | 설명                                          |
| --- | -------- | ------------------------------------------- |
| 수익성 | GPOA     | 매출총이익/자산                                    |
|     | ROE      | 순이익/자본                                      |
|     | ROA      | 순이익/자산                                      |
|     | CFOA     | (순이익+감가상각비-운전자본변화량-CAPEX)/자산                |
|     | GMAR     | 매출총이익/매출액                                   |
|     | ACC      | \-(운전자본변화량+감가상각비)/자산                        |
| 성장성 | GPOA 변화량 | (t기의 매출총이익 - t-5기의 매출총이익) / t-5기의 자산        |
|     | ROE 변화량  | (t기의 순이익 - t-5기의 순이익) / t-5기의 자본            |
|     | ROA 변화량  | t기의 순이익 - t-5기의 순이익) / t-5기의 자산             |
|     | CFOA 변화량 | t기의 Cash Flow - t-5기의 Cash Flow) / t-5기의 자산 |
|     | GMAR 변화량 | (t기의 매출총이익 - t-5기의 매출총이익) / t-5기의 매출액       |
|     | ACC 변화량  | (t기의 발생액 - t-5기의 발생액) / t-5기의 자산            |
| 안전성 | BaB      | 베타                                          |
|     | IVOL     | 기업의 고유 변동성                                  |
|     | LEV      | (장기부채+단기부채+소수주주지분+우선주)/자산                   |
|     | O        | Ohlson's O-Score                            |
|     | Z        | Altman's Z-Score                            |
|     | EVOL     | 60 분기 ROE의 변동성 or 5년 ROE의 변동성               |
| 지불금 | EISS     | 연간 발행 주식 수의 변화                              |
|     | DISS     | 연간 부채의 변화                                   |
|     | NPOP     | (순이익-장부 가치의 변화)의 합 / 수익의 5년 합계              |


### g. Value Factor
- Value effect: 내재가치(fundamental value) 대비 낮은 가격의 주식(저PBR, 저PER 등)이 내재 가치 대비 비싼 주식보다 수익률이 높은 현상
- BLEND portfolio
	- $\text{BLEND} = z(Rank(\text{PER}))+z(Rank(\text{PBR}))+z(Rank(\text{PCR}))+z(Rank(\text{PSR}))$
	- 이전의 QMJ 방법론과 같이 개별 지표의 랭킹을 바탕으로 지표별 Z-score를 구하고, 그들의 최종 합을 최종 value로 판단한다.
- 가치투자는 동일 조건의 타 주식 대비 가격이 낮은 혹은 많이 하락한 주식을 매수하는 역행(contraian) 투자의 성격을 가지고 있는 반면에 모멘텀  투자는 가격이 지속적으로 상승하는 주식에 투자하는 방법. 둘은 서로 반대의 성격을 가졌다.

### h. Multi Factor

- factor를 조합하는 방법들: Mix, Integrate, Sequential
	- Mix: 서로 다른 팩터에 각각 투자
	- Integrate: 각 종목의 팩터에 대한 순위를 계산하여 합산된 점수를 통해 포트폴리오를 구성
	- Sequential: Screening. 먼저 A 팩터 기준 상위 n%로 투자 유니버스를 걸러낸 후, 그 중 B 팩터 기준 상위 종목을 선택
# 2. Allocation Strategy

### a. Equal Weight Allocation: EW
= 유니버스 내의 종목 수를 n이라고 할 때, 각 종목들의 비중을 1/n으로 정하는 방법

- 변동성 또는 상관관계에 대한 추정치를 전혀 필요로 하지 않으므로, 일반적인 배분 전략들이 기대 수익이나 위험에 대한 추정치를 사용함으로써 발생하는 추정 오차가 전혀 없다.
	- => 단, 인덱스와의 괴리가 심해지기에, 동일비중 전략의 벤치마크를 시가총액가중방식지수로 정하는 경우 추적 오차를 설정할 때 유의해야 함

- 시가총액이 작은 종목은 overweight, 큰 종목은 underweight 투자 
	- => 쏠림 없이 분산이 잘 이루어진 포트폴리오를 구성
	- => 시가총액 작은 종목들의 비중이 많아 펀드의 규모를 크게 확대하긴 어려움: 소형주에 price impact가 크게 가해져서 
	- 
- 만일 개별 종목들의 기대 수익과 변동성이 동일하고 종목 간 상관관계가 모두 같다면, EW는 MVO(평균-분산-최적화 모형)의 optimal solution이 된다.

- EW의 핵심 원리
	- Mean Reversion: 평균으로의 회귀 & BLASH: Buy Low and Sell High
	- Outperform 시 비중 축소, Underperform 시 비중 확대
	- 단, 유니버스의 내 종목들의 fundamental에 문제가 없어야만 함!

### b. Risk-based Allocation
- 포트폴리오의 위험이란, 수익률의 변동성 $\sigma_p$
	- 자산이 2개고 그 비중의 합이 1($w_1 + w_2 =1$)이라면 $\sigma_p = \sqrt{w_1^2\sigma_1^2 +w_2^2\sigma_2^2 + 2w_1w_2\sigma_{12}}$
- 한계위험 기여도: MRC, Marginal Risk Contribution
	- 특정 종목의 비중을 한 단위 늘렸을 때 증가하는 포트폴리오의 위험(변동성) (=편미분)
	- $\text{MRC}_i=\cfrac{\partial \sigma_P}{\partial w_i} \ or \ \cfrac{\partial \sigma (w)}{\partial w_i}$
		- $\sigma_p \ or \ \sigma(w)$: 포트폴리오의 변동성
		- $w_i$: i번째 종목의 비중 
- 위험 기여도: RC, Risk Contribution
	- $i\text{번째 종목의 Risk Contribution} = w_i \times \cfrac{\partial \sigma _p}{\partial w_i}$
	- MRC가 작더라도 전체 포트폴리오에서 차지하는 비중 $w_i$가 크면, 해당 종목으로 인해 RC가 커질 수 있다.
- 위험균형: RP, Risk Parity (=ERC: Equal Risk Contribution)
	- 개별 종목이 전체 위험(변동성)에 기여하는 정도를 같게 해주는 배분 전략
	- EW는 동일 비중이나 RP는 동일 위험 배분으로 다름
	- $\sigma(w) = w_1 \times \cfrac{\partial \sigma(w)}{w_1} + w_2 \times \cfrac{\partial \sigma(w)}{w_2} + \ ... \ + w_n \times \cfrac{\partial \sigma(w)}{w_n}$
		- = $\displaystyle\sum^n_{i=1} [w_i \times \cfrac{\partial \sigma(w)}{w_1i}] = \displaystyle\sum^n_{i=1} \text{RC}_i$
		- 즉, 포트폴리오의 변동성 = 개별 종목들의 위험 기여도의 합
	- 어느 정목이 큰 위험을 초래할지 사전적으로 알 수 없기에, RP전략에서는 모든 종목의 위험기여도를 $\cfrac{\sigma(w)}{n}$로 동일하게 만든다
		- $w_i \times \cfrac{\partial \sigma_P}{\partial w_i} = w_j \times \cfrac{\partial \sigma_P}{\partial w_j} = \cfrac{\sigma(w)}{n}, \ \forall i,j$
	- Risk Budgeting: 특정 종목의 위험 기여도를 좀 더 크거나 작게 하고 싶다면 
		- $w_i \times \cfrac{\partial \sigma_P}{\partial w_i} = b_i \times \sigma(w)$, where $b_i = \cfrac{1}{n}, \forall i, ... , n$, and $\displaystyle\sum^n_i{w_i}=1, \displaystyle\sum^n_i{b_i}=1$
	- 결국 최적해는
		- $w_1 = \cfrac{\sigma_2}{\sigma_1+\sigma_2}, \ w_2 = \cfrac{\sigma_1}{\sigma_1+\sigma_2},$

- 변동성 균형: VP, Volatility Parity
	- RP에서 모든 상관관계가 동일하다고 가정
	- 결국 최적해는, 
		- $w_i = \cfrac{1/\sigma_i}{\displaystyle\sum^n_{j=1} 1/\sigma_j}$:  개별 종목의 비중은 개별 변동성의 역수에 비례한다
	- 변동성이 큰 종목에는 작은 비중을, 변동성이 작은 종목에는 많은 비중을 부여하여, 저변동성 효과와도 관련 있다.
	
- 최소 변동성: MV, Minimum Volatility
	- = 투자기회선 efficient line의 가장 왼쪽에 위치한, 즉 위험이 가장 작은 포트폴리오
	- $w_{MV} = \cfrac{\Omega^{-1}e}{e^T\Omega^{-1}e}$, $\sigma^2_P(w_mv) = \cfrac{1}{e^T\Omega^{-1}e}$
	- 종목들이 비중이 한 단위 증가했을 때, 포트폴리오의 위험(변동성)이 증가하는 정도가 모든 종목에서 같을 때 최적해가 구해진다.
		- 특정 종목의 MRC가 다른 종목보다 작으면 해당 종목의 비중을 늘리고, 다른 종목보다 크면 해당 종목의 비중을 줄여, 모든 종목의 MRC가 같아지도록 비중을 조절한다. 이 균형점이 바로 최소 변동성을 가지는 포트폴리오이다.
- 최대 분산 포트폴리오: MDP, Most Diversified Portfolio
	- 분산 비율 DP(Diversification Ratio)
		- $DR(w)= \cfrac{\Sigma w_i \sigma_i}{\sigma_P}=\cfrac{w^T \sigma}{\sqrt{w^T \Omega w}}$, 분모는 포트폴리오의 변동성, 분자는 개별 변동성의 가중평균
		- $\Sigma w_i \sigma_i > \sigma_p$이면 $DR(w) > 1$
	- MDP는 분산 비율을 최대화하는 전략으로 상관관계가 작거나 혹은 음수인 종목들 위주로 포트폴리오를 구성
		- 종목들 간의 상관관계가 낮을 수록 포트폴리오의 분산 효과는 커지게 되며, 포트폴리오 전체의 변동성은 작아진다. 이는 곧 분산 비율을 크게 한다
	- $\max DR(w) = \max \cfrac{\Sigma w_i \sigma_i}{\sigma_p}$, where $\Sigma w_i = 1$ 