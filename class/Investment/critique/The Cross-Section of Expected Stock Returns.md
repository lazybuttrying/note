[The Disposition Effect and Underreaction to News](The%20Disposition%20Effect%20and%20Underreaction%20to%20News.md)

CAPM의 한계를 명시하고 size factor와 BE/ME factor를 도입하였다. CAPM은 market beta로 주식 수익률을 제대로 설명할 수 있다고 이야기하지만 실은 그렇지 않음을 이 논문에서 소개한다. 그러나 market beta가 제거해도 될 factor로 고려하지도 않는다. 대신 size factor를 효과적으로 드러내기 위해 beta 산식에 차이를 두었다. 
본 논문에서는 pre-ranking beta와 post-ranking beta로 구분지었다. pre-ranking beta는 개별주식에 대해서 계산하며 post-ranking beta는 각 포트폴리오에 대해 계산한 결과다. 그 결과 pre-ranking beta 방식이 size effect와 구분된 market effect를 설명할 수 있었다.

Fama-MacBeth Regression을 이용하여 횡단면 분석을 진행했다.
그리고 CAPM의 한계를 극복하기 위해 두 가지 요인을 중점적으로 다뤘다.

1. **Size Factor**: Size factor는 주식의 시가총액(크기)이 예상 수익률에 미치는 영향을 분석한다. 소형주일 수록 수익률이 높다는 것을 실증적으로 증명해냈다.
    
2. **BE/ME Factor (Book-to-Market Equity Factor)**: BE/ME factor는 주식의 가치(BE)와 시장가치(ME)의 비율을 나타내며, 이를 통해 가치 주식과 성장 주식의 차이를 반영한다. 이 요인을 도입하여 주식 수익률의 변동성을 설명하고자 하였다. 논문에서는 BE/ME factor를 활용하여 주식의 가치와 시장의 상황에 따른 수익률을 분석하고, 이를 통해 추가적인 설명력을 확보하였다. BE/ME가 높을 수록 수익률이 높다는 점을 실증적으로 증명해냈다.

평균 수익률을 설명하는데 market leverage와 book leverage 간의 서로 반대되는 역할은 BE/ME에 의해 잘 포착된다. Log 산식의 성질에 의해서 증명할 수 있으며 이에 맞게 회귀 결과 기울기의 절댓값은 비슷하나 방향만 다른 결과를 확인해냈다. E/P와 평균수익률의 관계는 size와 BE/ME 조합에 의해 흡수되는 것 또한 위와 유사한 방식으로 확인해냈다.

결론에는 두 factor가 포트폴리오의 수익률뿐만 아니라 다양한 경기 변화를 측정하는 경제 변수들 간의 관계를 조사한다면 둘에 의해 포착되는 economical risk의 근원을 도출하는데 도움이 될 것이라는 질문을 제시한다. 즉 여러 economical factor에 대한 노출도가 size와 BE/ME의 역할을 설명할 수 있는지 실험해볼 수 있다. 비슷한 맥락에서 distress factor에 대해 실험해볼 수 있다.

사실 주가가 합리적이라면, BE/ME는 회사에 대한 상대적 전망의 지표가 될 수 있다. 저BE/ME 회사는 지속적으로 좋은 성과를 낼 것이고 고BE/ME 회사는 계속 부진할 것이다. 그러나 이 전망이 시장이 과잉 반응한 결과일 수 있음을 유의해야 한다. 과잉 반응인지 확인하고 싶다면 횡단면 분석을 통해 타 회사와 비교하면 된다.

그러므로 자산가격 결정이 합리적이라면, size와 BE/ME는 위험의 대용치가 될 수 있다. 자산가격 결정이 비합리적이라 하여도, 대안 투자 전략의 포트폴리오 성과를 평가하고 기대수익률을 측정하는데 사용될 수 있다. 하지만 주가가 비합리적이라면, 이러한 결과가 지속될 지 의심이 된다.