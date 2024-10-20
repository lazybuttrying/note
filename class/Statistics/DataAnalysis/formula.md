# Representative Value
- mode (bimodal)
  - $b(g)=\Sigma y_i$, where $y= 0(g=x_i) or 1$
- midpoint [half between max & min]
  - $b(g)=\max |x_i-g|$
  - $=\frac{\max+\min}{2}$
- median [center in sort]
  - $b(g)=\cfrac{\Sigma |x_i-g|}{N}$
- mean
  - $b(g)=\cfrac{\Sigma (x_i-g)^2}{N}$

---

# Distribution
independent 하기에 곱셈으로 나타낼 수 있다
- Binomial: $R \thicksim B(N,p)$, 성공 횟수
  - $P(R=r) = _NC_rp^r(1-p)^{N-r}$
  - Mean=$np$, Var=$np(1-p)$
- Geometric: $R \thicksim G(p)$, 시행 횟수 (성공 -1)
  - $P(N=n) = p(1-p)^{n-1}$
- Pascal: $N \thicksim P(r,p)$
  - $P(N=n) = _{n-1}C_{r-1}p^r(1-p)^{n-r}$
- Normal distribution: 
  - $f(X) = \cfrac{1}{\sqrt{2\pi}\sigma} \cdot e^{\cfrac{-(X-\mu)^2}{2\sigma^2}}$
  - $P(X>x_i) = P(Z>\cfrac{x-\mu}{\sigma})$
  - $Z = \cfrac{X-\mu}{\sigma}$
-  Chi-square:
  - !!! $x \geq 0$, $v=df$
  - 평균 $v$, 분산 $2v$
  - !!! $\Sigma Z^2 \thicksim \chi^2(n-1)$ : 자유도 감소!


![](https://postfiles.pstatic.net/20130822_287/af472_1377135179337F6CsW_JPEG/%C7%A5%C1%D8%C1%A4%B1%D4%BA%D0%C6%F7%C7%A5_-_2.jpg?type=w2)


# Sampling Distribution
Assume: independence
- $\mu_{\bar{X}} = E(\bar{X})= \frac{1}{N} N\mu =\mu$
- $\sigma^2_{\bar{X}} = Var(\bar{X}) = \frac{1}{N^2}N\sigma^2 = \cfrac{\sigma^2}{N}$

# Central Limit Theorem
- 원래 모집단의 분포에 관계없이 $\bar{X}$의 분포는 표본크기(N)이 커짐에 따라 정규분포에 접근
- 이 때 평균은 $\mu$, 분산은 $\sigma^2/N$


---

# Point Estimate
- $\hat{\mu} = \bar{X}$ estimator
- $\hat{\mu} = 23$ estimate

- $SE(\hat{\mu}) = SD(\bar{X})= \frac{\sigma}{\sqrt{N}}$

# Unbiased Estimator
- $E(S^2)=\frac{n-1}{n} \sigma^2$: biased
- $S^2_{n-1} = s^2 = \cfrac{n}{n-1}S^2=\cfrac{\Sigma (X_i - \bar{X})^2}{n-1}$

- $E(S^2_{n-1}) = \sigma^2$


# Confidence Interval
- 가능한 구간을 작게 해줘야 의미있는 정보 = 허용할 에러 최소화
- $[\bar{X}-1.96\frac{\sigma}{\sqrt{N}}, \bar{X}+1.96\frac{\sigma}{\sqrt{N}}]$
  - 1.96: 95%, 2.54: 99%
- 옳은 해석: 여러 신뢰구간 중 95%의 신뢰구간은 해당 평균을 포함한다

# t-Distribution
- $E(X)=0$, $Var(X)=\frac{\nu}{\nu-2}$
- $t=\cfrac{Z}{\sqrt{V/\nu}}$
  - $Z=\cfrac{X-\mu}{\sigma}$
  - $V=(n-1)\cfrac{s^2}{\sigma^2}$
    - $\sqrt{V/\nu}=s/\sigma$
- $t = \cfrac{X-\mu}{s}$


- ex) n=100, sample mean=120, sd of sample=10. 이 평균은 정상집단($\mu=100$)보다 통계적으로 유의미하게 높은가?
  - $H_0: \mu = 100$
  - $H_0: \cfrac{\bar{X}-\mu_{\bar{X}}}{s_{\bar{X}}} \thicksim t(99)$, where df=100-1
  
  - $P(\bar{X}>120)=P(t>\cfrac{120-100}{1})=P(t>20)=.0000$
    - $s_{\bar{X}} = 10/\sqrt{100}=1$
  - < 0.05 이므로 기각?
    - 영재학급의 평균공격성 점수는 정상집단보다 높다

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbv1S6M%2FbtsBFIom9iW%2FiXTeKPYBQtnJlPjQABKYy0%2Fimg.png)

---


# Hypothesis Test

0. 등분산성 검정 $H_0: \cfrac{\sigma_1^2}{\sigma_2^2}=1$

1. Set Hypothesis
- if $H_0: \mu = \mu_0$
- One-tailed test
  - then $H_1: \mu > \mu_0$ 
  - then $H_1: \mu < \mu_0$
- Two-tailed test
  - then $H_1: \mu \neq \mu_0$ 

2. Rejection Area on significance level
- if $H_1: \mu > \mu_0$ 
  - Reject R: $\cfrac{\bar{X}-\mu}{\sigma-\sqrt{n}}=Z > z_{\alpha/2}$ 오른쪽
- if $H_1: \mu < \mu_0$ 
  - Reject R: $\cfrac{\bar{X}-\mu}{\sigma-\sqrt{n}}=Z < - z_{\alpha/2}$ 왼쪽
- if $H_1: \mu \neq \mu_0$ 
  - Reject R: $|\cfrac{\bar{X}-\mu}{\sigma-\sqrt{n}}| = |Z| > z_{\alpha/2}$ 양쪽

![](https://wikidocs.net/images/page/163986/test07.png)


3. Decision
- One-tailed test: if alpha > p-value, Reject $H_0$
- Two-tailed test: if $\cfrac{\alpha}{2}$ > p-value, Reject $H_0$
- 그럼 (0.05 or 0.025), (0.01 or 0.005) 보다 작으면 reject


# Compare means of two groups
Assume: Independence
- $Var(\bar{X}_1-\bar{X}_2) = Var(\bar{X}_1) + Var(\bar{X}_2)$
  - $=\frac{\sigma^2_1}{n_1}+\frac{\sigma^2_2}{n_2}$
- 서로 분산이 동일하다면 ($\sigma^2_1=\sigma^2_2$), $=\sigma(\frac{1}{n_1}+\frac{1}{n_2})$
- 모수를 모른다면,
  - $\hat{\sigma}_{\bar{X_1}-\bar{X_2}}=\frac{s^2_1}{n_1}+\frac{s^2_2}{n_2} = s^2_{pool}(\frac{1}{n_1}+\frac{1}{n_2})$
    
    - $s^2_{pool} = \cfrac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}$

    - $s^2 = \cfrac{\Sigma(X_i - \bar{X})^2}{n-1}$에서 $\Sigma(X_i - \bar{X})^2$를 추출하여 위의 식 전개에 사용


ex1) $n_1=n_2=100$, $\mu_{\bar{X}_m}=120$, $\mu_{\bar{X}_f}=100$, $s_{\bar{X}_m}=10$, $s_{\bar{X}_f}=9$
- 두 집단은  평균이 동일한 분포에서 나왔는지 검증하라
- $H_0: \mu_{\bar{X}_m}-\mu_{\bar{X}_f} = 0$
- $t=\cfrac{(120-100) - 0}{\sqrt{\cfrac{(100-1)\cdot 10^2 +(100-1)\cdot 9^2}{100+100-2}}\sqrt{\frac{1}{100}+\frac{1}{100}}}$

- $P(t>7.433)=0.000$으로 Reject. 두 집단의 공격성 평균점수가 통계적으로 유의미하게 차이 남


---


# Hypothesis Test on Ratio

# Hypothesis test on Correlation
- $H_0: \rho=0$ 즉, $r$이 평균이 $\rho=0$이고 표준편차가 $SD_r$인 t분포에 접근한다
- $SD_r = \sqrt{\cfrac{1-r^2}{n-2}}$ 
  - df: $n-2$ from $y=ax+b$
  - $t(n-2)= \cfrac{r-\rho}{SD_r}$


---



  - 가설검증은 영가설 기각 여부만 논할 뿐. t-test라면 두 평균의 차이 여부만 볼 뿐, 그 차이가 얼마나 큰 지, 다시 연구를 하면 반복 검증이 가능한지 등에 대한 정보는 제공하지 않음. 이럴 때는 effect size와 power
  - 평균의 차이에 대한 effect size $d=\cfrac{|\mu_1-\mu_2|}{\sigma}$
  - 이 때의 estimator of $\sigma$는 $\hat{\sigma} = \sqrt{\cfrac{s_1^2+s_2^2}{2}}$
  




