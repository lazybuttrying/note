
[The Cross-Section of Expected Stock Returns](The%20Cross-Section%20of%20Expected%20Stock%20Returns.md)

**기술 연결과 예측 가능한 수익: 요약**

기업 간 기술적 근접성이 미래 주식 수익률을 예측할 수 있는지 알아본다. 미국 특허 정보와 주식 수익률 데이터를 통합한 데이터셋을 사용하여 주목할 만한 상관관계를 발견했다. 기술적으로 밀접하게 연결된 기업들은 유사한 주식 수익률 패턴을 보였다

**용어 설명**
- tech-peer: 기술 간 유사도가 높은 회사들

**포트폴리오 전략**
- 회사 $i$의 $t$월에 대하여 유사한 기술을 공유하는 회사들로 구성된 시가총액 가중평균 수익률
- $\text{TECHRET}_{it} = \cfrac{\sum_{j \neq i} \text{TECH}_{ijt} \cdot \text{RET}_{jt}}{\sum_{j \neq i} \text{TECH}_{ijt}}$
- $\text{TECH}_{ijt} = \cfrac{(T_{it} T_{jt}^T)}{\sqrt{(T_{it} T_{it}^T)} \sqrt{(T_{jt}T_{jt}^T)}}$
- $T_{it} = (T_{it1}, T_{it2}, \ldots, T_{it427})$

**변수 설명**
- $TECHRET_{it}$: 유사한 기술을 가진 회사들의 수익률
- $RET_{jt}$: 회사 $j$의 $t$월의 수익률
- $TECH_{ijt}$: $t$ 시점에서 회사 $i$, $j$가 기술적 근접도 
	- called 'technology proximity score
	- 같은 산업 코드로 분류되지 않아도 기술적 근접도는 높게 나올 수 있다.
- $T_{it}$: 회사 $i$의 특허에 대한 비례적 점유율

**Technology momentum**
- 전월에 tech-peers가 최고 실적이 보이면 long
- 전월에 tech-peers가 최저 실적이 보이면 short
- 이러한 전략으로 구한 월별 수익률이 알파를 보였다.

**함의점**
- Intensity: **높은 기술 집약도**를 가진 회사일 수록 수익률 예측력이 높다
	- 높은 R&D 지출, 지난 5년 간 특허 수여 개수
	- => technology momentum은 기술 혁신을 반영한다
- Specificity: 기술 특이성이 큰 회사들 사이에서 technology momentum이 크다
	- 산업 집중도가 높은 기술 분류에 속한 특허를 가진 회사들
	- => 기술 관련 뉴스가 더 구체적인 산업에서의 응용에 관한 내용일 수록 정보 확산 속도가 느리다.
- Overlooked and No arbitrage: 투자자들에게 간과된 회사일 수록 그리고 차익거래 비용이 클 수록 수익률 예측력이 높다
	- overlook: 소형주, 소수의 애널리스트, 적은 소유권, 약한 미디어 커버리지
	- arbitrage cost: 높은 고유 수익률 변동성
	- => 아래와 같은 상황에서 관찰 중인 회사의 부진한 가격 반응이 일어났다
		-  더 강력하고 구체적인 기술적 비전을 갖고 있을 때
		- 투자자로부터 이목을 끌지 못할 때
		- 차익거래가 어려울 때