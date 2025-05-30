---
marp: true
theme: default
paginate: true
header: "Investors' appetite for money-like assets: The MMF industry after the 2014 regulatory reform"

size: 16:9
math: mathjax
---

# Investors' appetite for money-like assets:

# The MMF industry after the 2014 regulatory reform

## Marco Cipriani, Gabriele La Spada

Federal Reserve Bank of New York Research Group

JFE 2021 (Received February 2019)

---

## Outline

- Background
- Motivation
- Contribution & Key Methodology
- Result
  1. Premium for money-likeness
  2. Elasticity of Substitution b/w Prime & Gov MMF

<!-- - Methodology
- Data (skip)
- Results -->


---

## Background 1: Nonexistent Risk Free, But...

- Exists via combination of a market of people willing to buy the risk asset
- Distribute raw commodity $\implies$ Distribute Risk of the Commodity 

![bg right w:600](resource/image-1.png)


<!-- By "Money without boundaries: How Blockchain Will Facilitate the Decentralization of Money" by Thomas J. Anderson, Piliar 2 - The Credit Theory of Money, 2021 -->

---

## Background 2: MMF(Money Market Fund)

![bg right w:600](resource/image.png)

- Pegged to $1 per share, MMFs are a type of mutual fund that invests in short-term, low-risk securities

---

## Background 3: 2014 SEC Regulatory Reform

##### Enhanced Disclosure Requirements


- The reform mandated liquidity fees and redemption gates for prime MMF (not gov MMF), additionally floating NAV only for ***institutional prime MMFs***
  - ***Floating NAV***: Round to the nearest 1/1000 of a cent for the asset value of the fund, instead of at a $1.00 stable share price
  - ***Gate***: fine liquidity fees or suspending redemptions temporarily when fund's weekly liquid assets fall below a certain threshold

- https://www.sec.gov/newsroom/press-releases/2014-143

---

## Motivation from title

- ***money-like asset*** = MMF is not risk free. It has non-zero volatility like asset
- 2014 ***regulatory reform*** = for adverse selection b/w inst and retail investors
- ***Investors' appetite***:  = Premium of money-likeness for risk aversion

![h:400](resource/image-8.png)

---

## Contribution

- Define feature of money-like assets, information ***in***sensitivity
- Estimate the premium for money-likeness even assets supplied by the private sector
  - By exploiting an exogenous change (SEC Reform)

## Methodology 
1. Difference-in-Difference
2. Two Stage Least Squared Regression
  a. Two instruments for the time-varying endogenous relative price 

---

## Result 1: Premium for Money-Likeness

![ w:450](resource/image-7.png)


- $y_{ijkt}$: W.Avg Net Yield of MMF
  - $k \in \{prime(1), \ government(0) \}$

  - $j \in \{inst, \ retail\}$ : Share classes

  - $i$: Family = Same investment bank

  - $t$: Month
    - $1_{t \geq Nov. \ 2015}$: ***started to react***  
    - $1_{t \geq Oct. \ 2016}$: the ***regulation onward***


![bg right:35% w:430](resource/image-2.png)

---

## Result 1+: Value of Info. Insensitivity in Fee and Gross Yield

Increase in Net-Yield spread 
- $\impliedby$  Decrease in Fee 
- $\impliedby$  Increase in Gross-yield spread or both

![w:700](resource/image-3.png)

---

## Result 2: Elasticity of Substitution b/w Prime & Gov MMF

MMF Investor's Relative Demand for Prime vs Gov MMF

![w:450](resource/image-4.png)

- $q$: TNA(total net asset) of the Funds 
  - from diff of yield $\Delta y$: 
    - treat MMF share as zero coupon bond \$1 face value,  $p=\cfrac{1}{1+y}$
- $p$: W.Avg Prices
  - Log form means $Spread_{it}$

---

## Result 2: Elasticity of Substitution b/w Prime & Gov MMF
2SLS
  - 1st stage
    - The share of prime MMFs in the family
    - The share of government MMFs in the family interacted with a dummy for the post-October 2016 period

  - 2nd
    - Spread
    - The additional spread after October 2016

  - Use familiy specialization in prime MMFs from a pre-sample period
    - MMF Specialization: how concentrated an MMF family's business 



---

## Result 2: Elasticity of Substitution b/w Prime & Gov MMF


![h:450](resource/image-5.png)

---



![h:550](resource/image-6.png)

---

# Fin.
