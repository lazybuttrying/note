---
title: Trading and Arbitrage in Cryptocurrency Markets
authors:
  - Igor Makarov
  - Antoinette Schoar
year: 2020
publication: Journal of Financial Economics
institution: London School of Economics, MIT Sloan
doi: https://doi.org/10.1016/j.jfineco.2019.06.011
tags:
  - cryptocurrency
  - bitcoin
  - arbitrage
  - price-impact
  - capital-control
created: 2025-08-01
---

## 🧭 Summary  

 Cross-country capital control leads to the arbitrage oppurtunity in cryptocurrency markets
 1. Price deviations across countries co-move
 2. Countries with higher bitcoin premia over the US bitcoin price see widening arbitrage deviations when bitcoin appreciates

---

## 🧠 Stream of Literature
- Research on **cryptocurrencies** in finance and economics
	- potential real effects of cryptocurrencies: payments, transaction mechanism
	- valuation model of digital currencies
- **Limits of arbitrage**
	- Deviations from one price (ex-Siamese twin)
	- Market Segmenation (by Capital Controls)
- Positive relation btw **asset prices and net order flow** in 'traditional' markets

---

## 🎯 Contribution

##### Geographical Classification of Crypto Exchanges
- China: OkCoin, Huobi, BTCC
- Japan: bitFlyer, Zaif, and Quoine
- Korean: Bithumb
- US: Coinbase, Kraken, Bitstamp,and Gemini
- Europe: Kraken, Coinbase, and Bitstamp

---

## 📊 Data & Methodology  
##### Data
- Source: Kaiko, Bitcoincharts.com
- Duration: 2017-01 ~ 2018-03
- Type: Price & Order book
- Frequency: 5 min, 1 hour, daily
- etc)  Daily ForEx rate
##### Methodology
- **Arbitrage Index** 
	- volume-weighted price of bitcoin per minute for each exchange and averaged at the daily level.
	- For a given minute the maximum price across all exchanges is divided by the minimum price in that minute.
	- (Outliers are removed by replacing any price movement of more than 10% between two adjacent transactions.)
- **Price Ratio**
	-  calculated based on the volume-weighted price per minute across all the exchanges in a region and averaged at the daily level.
	- A big fraction of the large arbitrage spreads for the overall market are driven by **price** **differences** across regions (persistent over long time periods)
- **Arbitrage Profit**
	- include only price differences > 2% btw exchanges 
	- calculated at the second level and then aggregated to the daily level
		- For each second, the aggregate amount of low priced volume(= sold in a high price region) - the sell-initiated volume in the region(= that has the highest price in a given second.)
- **Correlation** matrix of arbitrage indexes
	- to show co-movement of price deviations and ..
		- buying pressure: Hodrick-Prescott filter for smoothing log BTC price
		- Capital Controls
- **Capital Controls Index**
	- 0: if at least one of the countries is totally open
	- 1: if both countries have very high level of capital controls
- **Price impact** $\lambda$:  aggregation of price impact per unit (signed volume) **flow**
	- Decompose order flow & returns
	- Extract common factors
	- Price-flow regression: $r^*_t = \lambda\,s^*_t + \varepsilon_t$
- **Idiosyncratic** price pressure and returns
	- Vector Auto-regression
	- $\hat s_{it}\;=\;\gamma_i\,\hat p_{i,t-1}\;+\;b_{1i}\,\hat s_{i,t-1}\;+\;b_{2i}\,\hat s_{i,t-2}\;+\;b_{3i}\,\hat s_{i,t-3}\;+\;\varepsilon_{it}$
	- $\hat p_{it}\;=\;\lambda_i\,\hat s_{i,t}\;+\;a_{1i}\,\hat p_{i,t-1}\;+\;a_{2i}\,\hat p_{i,t-2}\;+\;a_{3i}\,\hat p_{i,t-3}\;+\;\varepsilon_{it}$

---

## Discussion
##### Implementation of arbitrages strategies
1. Mimic of short 
	1. Motive: Some exchanges do not allow for short selling
	2. Todo: negative position in BTC by trading on margin
	3. Limits: Convergence risk
2. Positive balance of BTC on both exchanges
	1. Limits: exposed to BTC price fluctuations
##### Constraints to Arbitrage
1. Lower transaction cost (fee) -> X
2. Governance Risk of cryptocurrency exchanges -> ?
3. Cross-border capital controls -> O
	1. especialy, binding for retail investors
	2. arbitrage capital is stucked by the noise traders
		1. who are driving up the price in certain markets or lose heart when negative information comes out

---

## 💡 Notes 

- While regulations in some countries make **cross-border transfers in fiat currencies** difficult for retail investors, **large institutions** should be able to **avoid these constraints**
- This **market segmentation** allows us to measure differences in **pricing behavior** across markets ->**marginal investors** who price cryptocurrencies in countries **with less developed capital markets value cryptocurrencies more highly**, possibly **because they have a higher convenience yield for bitcoin.**
