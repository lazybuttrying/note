[Cross Section](Cross%20Section.md)
- intercept = return on a standard portfolio (the weights on stocks sum to 1) in which weighted averages of the explanatory variables are 0 

In case of panel data, esitmates the betas and risk premium for any risk factors that are expected to determine asset p
각 자산에 대해 M개의 팩터를 독립변수(risk factor), N개의 자산 포트폴리오의 수익률을 종속변수로 하는 회귀모형 적합
=> 이는 각 자산의 beta exposure를 결정함
![](resource/Pasted%20image%2020240319130127.png)

Step1에서 구한 회귀계수(β)를 독립변수, 각 시점의 포트폴리오 수익률(Ri,t)을 종속변수로 하는 회귀모형 적합
![](resource/Pasted%20image%2020240319130135.png)

즉, [Step1]은 N개의 자산에 대해 각각 회귀모델을 적합시키는 것이고, [Step2]는 T개의 시점에 대해 각각 회귀모델을 적합시키는 것이다.
[Step2]의 결과로 나오는 회귀계수 행렬 λ을 시간축 t에 대해 평균을 취한 각 팩터의 계수값을 각 팩터에 대한 최종적인 회귀계수 추정값으로 사용한다.


https://youtube.com/watch?v=tjfbomhN_kw


https://www.youtube.com/watch?v=O0dOlr_XbdM&list=PLAXSVuGaw0KxTEN_cy-RCuEzzRdnF_xtx&index=5 


https://www.youtube.com/watch?v=T7Dmp8a7IU0&list=PL6Y8SvWdPo08HEFH0aysLYoYkcWxptKXs