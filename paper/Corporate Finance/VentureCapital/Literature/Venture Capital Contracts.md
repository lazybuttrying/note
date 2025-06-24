---
title: Venture Capital Contracts
authors:
  - Michael Ewens
  - Alexander S. Gorbenko
  - Arthur Korteweg
year: 2022-01-01
publication: Journal of Financial Economics
institution: Caltech, UCL, USC Marshall
tags:
  - VC
  - bargaining-power
doi: N/A
created: 2020-05-05
---

## Summary

- The role of contracts in venture capital (VC) value creation and matching with entrepreneurs is unknown

- estimate the impact of contract terms on startup outcomes and the split of value between the entrepreneur and investor
 
- **Findings**: Venture capital contracts shift value from entrepreneur to VC. Any analysis of contracting must incorporate the complex matching between VC and entrepreneur.
- https://michaelewens.com/wp-content/uploads/2021/03/VCContr-general.pdf


## 🧭 Research Overview
- **Research Question**:  
  How do VC contract terms affect startup success and the distribution of value between VCs and entrepreneurs?

- **Hypothesis**:  
  There exists an internal optimal equity share that maximizes firm value, but bargaining leads to more investor-friendly terms.

- **Motivation**:  
  VC contracts are complex, and their impact on outcomes and value distribution is not well quantified. Prior models often assume efficient contracts, ignoring real-world bargaining power and selection effects.

---

## 📊 Data & Methodology
- **Data Source(s)**:  
  First-round VC contracts (2002–2015) from VentureSource, PitchBook, VC Experts, filings from Delaware & California

- **Sample**:  
  ~1,695–2,581 contracts, focusing on early-stage (seed/Series A) deals with known terms

- **Methodology**:
  - Empirical: Analysis of contract terms (equity share, participation, pay-to-play, board seats) and outcomes (IPO/acquisition > 2×)
  - Structural: Dynamic search and matching model with endogenous contracts and selection
  - Estimation: Generalized Method of Moments (GMM), calibrated to data moments

---

## 📈 Key Findings
- An internal **optimal equity share** (~15%) maximizes firm value; beyond this, higher VC ownership **reduces value**.
- In practice, VCs hold ~40% ownership, shifting more value toward themselves.
- **Participation rights** and **VC board seats** reduce firm value but benefit VCs.
- **Pay-to-play clauses** increase firm value and shift value toward entrepreneurs.
- Better VCs offer more investor-friendly terms, but also create more value.
- **Search frictions** amplify VC bargaining power. Reducing frictions benefits VCs but can reduce startup value.
- **Selection into deals** (match quality) is a major driver of outcomes—endogeneity must be accounted for.

---

## 🧠 Theoretical Framework
- **Dynamic search and matching model**:
  - Agents meet randomly and negotiate contracts.
  - VCs make take-it-or-leave-it offers.
  - Contracts affect both startup value and value split.
- Captures bargaining, search frictions, and endogenous matching.
- Equilibrium contracts reflect trade-offs between cash flow and control rights.

---

## 🎯 Contribution to Literature
- First paper to empirically quantify how individual VC contract terms affect startup **value and value split** using a structural model.
- Adds realism by incorporating **VC bargaining power**, agent heterogeneity, and selection into matches.
- Shows that **inefficient contracting** (VC-friendly terms) can persist due to market frictions and agent differences.

---

## ⚖️ Strengths and Weaknesses
- **Strengths**:
  - Rich contract-level data
  - Structural model allows causal interpretation
  - Addresses selection/endogeneity explicitly
  - Counterfactual simulations are policy-relevant

- **Limitations**:
  - Reduced-form value functions; specific mechanisms (e.g., effort, monitoring) not fully identified
  - Focused on intensive margin (existing deals), not extensive margin (who enters the market)
  - External validity may be limited to early-stage VC-backed startups

---

## 🔗 Related Works
- Builds on:
  - Kaplan & Strömberg (2003), Sørensen (2007), Hall & Woodward (2010)
  - Matvos (2013), Gornall & Strebulaev (2020)
  - Shimer & Smith (2000), Adachi (2007) for matching theory

- Contrasts with:
  - Models assuming perfectly competitive, homogeneous investors
  - Theoretical models lacking selection dynamics

---

## 💡 Notes & Future Questions
- Should policy incentivize more entrepreneur-friendly terms?
- Would centralized VC markets or platforms reduce inefficiencies?
- Can smart contract tech (e.g., blockchains) reduce information asymmetries or frictions?

---

## 📚 Citation
Ewens, M., Gorbenko, A. S., & Korteweg, A. (2020). *Venture Capital Contracts*. Working Paper.
