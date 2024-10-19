
# Distribution
1. Binomial: $R \thicksim B(N,p)$
  - $P(R=r) = _NC_rp^r(1-p)^{N-r}$
2. Geometric: $R \thicksim G(p)$
  - $P(N=n) = p(1-p)^{n-1}$
3. Pascal: $N \thicksim P(r,p)$
  - $P(N=n) = _{n-1}C_{r-1}p^r(1-p)^{n-r}$
4. Normal distribution: 
- $f(X) = \cfrac{1}{\sqrt{2\pi}\sigma} \cdot e^{\cfrac{-(X-\mu)^2}{2\sigma^2}}$
- $Z = \cfrac{X-\mu}{\sigma}$
5. Chi-square:

# Central Limit Theorem
- 원래 모집단의 분포에 관계없이 $\bar{X}의 분포는 표본크기(N)이 커짐에 따라 정규분포에 접근
- 이 때 평균은 $\mu$, 분산은 $\sigma^2/N$
