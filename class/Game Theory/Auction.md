
### 2nd Bid Auction

$\widehat{b_{-i}}$ = highest bid among remains

a) $\widehat{b_{-i}} < \widehat{b_{i}(v_i)} < v_i$
- i wins & pays $\widehat{b_{-i}}$
- i's surplus = $v_j-\widehat{b_{-i}}$

b) $\widehat{b_{i}}(v_i) < \widehat{b_{-i}} < v_i$
- i loses & i's surplus = 0
- if $b^{*}_i$ is played, i wins => i's surplus = $v_i-\widehat{b_{-i}}>0$

b) $\widehat{b_{i}}(v_i) < v_i< \widehat{b_{-i}}$
- i loses & i's surplus = 0
- if $b^{*}_i$ is played, i loses => i's surplus = 0

> Weak Dominance -> true value를 쓰는 게 best 


-  Resource Allocation
	- 공공재를 놓을 것이냐
	- truth telling
		- in terms of maximization of social welfare
		- 예타(예비 타당성 조사)
		- 각자의 true valuation을 내놓기
	- truth valuation을 내놓도록 유인 
		- 위에서 안 그랬을 때 손해보는 상황
	- V-C-G mechanism
		- $y_i = C- \Sigma_{i\neq i}u_j$ 여러분의 i값만 빼고 덧셈
		- $y_i>0$일 때 전철을 놓게 만들어야 하니, truth telling 유도됨
		- 증명 꼭 해보기
		- 2가지 전략이 가능하고 각각 3가지 경우가 가능하다
			- 그대로, 부풀려, 에누리
			- 같거나 손해본다는 결론


  

=== VCG Auction Mechanism ===

The VCG (Vickrey-Clarke-Groves) mechanism ensures truthful bidding and efficiency.

In a single-item auction, the highest bidder wins but pays the second-highest bid.

The mechanism follows the formula: 

 $y_i = C - Σ_{j}\eq i} u_j$ (excluding i's value from the sum).

A project is undertaken if y_i > 0, ensuring truth-telling as the dominant strategy.

  

Received bids:
Alice: 100
Bob: 150
Charlie: 130

  

Sorted bidders (highest to lowest bid):
Bob: 150
Charlie: 130
Alice: 100

  

Winner: Bob with bid: 150
Payment required (second highest bid): 130

  

=== Proof of VCG Mechanism ===

1. The mechanism ensures incentive compatibility: Each bidder maximizes utility by bidding truthfully.

2. The highest bidder wins the auction.

3. The winning bidder pays the opportunity cost imposed on other bidders, which is the second-highest bid.

4. This ensures that bidders are not incentivized to manipulate their bids.

  

Two strategic choices exist, each with three possible cases:

  

Case 1: The bidder wins
   - Bob bids truthfully: Pays the second-highest bid (130) and maximizes utility.
     - Utility calculation: u = 150 - 130.
   - Bob overbids: Still wins but pays the same amount (130), no incentive to overbid.
     - Since bid (150) > second-highest bid (130), payment remains the same.
   - Bob underbids: May lose the auction, risking lower utility.
     - If bid < second-highest bid (130), the bidder loses and gets utility = 0.

  

Case 2: The bidder loses
   - Charlie bids truthfully: Does not win and pays nothing.
     - Utility = 0 since no payment is made.
   - Charlie overbids: If it does not exceed Bob's bid (150), still loses and pays nothing.
     - If bid (130) < highest bid (150), utility = 0.
   - Charlie underbids: Still loses and pays nothing.
     - If bid (130) < highest bid (150), utility = 0.
   - Alice bids truthfully: Does not win and pays nothing.
     - Utility = 0 since no payment is made.
   - Alice overbids: If it does not exceed Bob's bid (150), still loses and pays nothing.
     - If bid (100) < highest bid (150), utility = 0.
   - Alice underbids: Still loses and pays nothing.
     - If bid (100) < highest bid (150), utility = 0.

  

Conclusion: The optimal strategy is to bid truthfully, as any deviation results in the same or worse outcome.

  

Final proof: Bob wins by bidding 150, but only pays 130.

This ensures truthful bidding as overbidding does not reduce cost, and underbidding may lead to losing.

{'winner': 'Bob', 'payment': 130}
```