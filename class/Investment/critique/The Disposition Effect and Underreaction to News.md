
### Abstract

Disposition effect: tendency of investors to ride losses and realize gains
- underreaction to news
- leading to return predictability

Data: Mutual fund holdings to construct a new measure of reference purchasing prices for individual stocks

Finding:
- Post-announcement price drift is most severe whenever capital gains and the news event have the same sign. 
- The magnitude of the drift depends on the capital gains (losses) experienced by the stock holders on the event date.
- An event-driven strategy based on this effect yields monthly alphas of over 200 basis points.

![](resource/Pasted%20image%2020240518233619.png)

### Conclusion

1. Disposition effect can induce underreaction to news, leading to return predictability and post-announcement price drift.
2. The price pattern depends on both information content of the news and the investor's reference price relative to the current price.
	1. Bad news: travels slowly among stocks trading at large capital losses, in turn leading to a negative price drift
	2. Good news: travels slowly among stocks trading at large capital gains, in turn leading to a positive price drift.
	3. Reference price: $RP_t = \phi^{-1} \sum_{n=0}^t V_{t,t-n} P_{t-n}$
		1. $V_{t,t-n}$: the number of shares purchased at date $t - n$ that are still held by the original purchasers at date $t$
		2. $\phi$: a normalizing constant such that $\phi = \sum_{n=0}^t V_{t,-n}$
		3. $P_t$: the stock price at the end of month $t$.


3. New method to compute a measure of the aggregate basis for individual stocks that relies on holdings data
	1. mutual funds holdings -> construct a measure of reference prices for individual stocks.
	2. gain and loss -> construct a test of stock price underreaction to news.
4. Results: Stocks with large unrealized capital gains have higher subsequent returns (because investors initially underreact to news announcements)
	1. thereby generating a predictable price drift
	2. Post-event predictability is most severe where the disposition effect predicts the largest underreaction
5. Post-event risk-adjusted returns can be achieved by using a sort on the capital gains overhang, suggesting that such a variable predicts the gradual market response to new information.
	1. Capital gains overhang: $g_t = \cfrac{P_t-RP_t}{P_t}$

