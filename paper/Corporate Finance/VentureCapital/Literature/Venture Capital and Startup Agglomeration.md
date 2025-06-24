---
title: Venture Capital and Startup Agglomeration
authors:
  - Michael Ewens
  - Jun Chen
year: 2023
publication: Journal of Finance
institution: Columbia Business School, University of Illinois Chicago
tags:
  - VC
  - agglomeration
  - banking
doi: https://doi.org/10.31235/osf.io/8tpux
created: 2024-06-06
---
## Summary

- Startup financing constraints can be partially explained by venture capitalist constraints
- Volcker Rule restricted the set of limited partners that could invest in VC
- This change had different impacts by states in the U.S.
- **Findings**: VC funds shrink, fundraising probabilities fall, startups absorb these VC financing constraints.
- https://github.com/michaelewens/Banks-In-VC 


## 🧭 Research Overview
- **Research Question**:  
  How does the supply of venture capital (VC), particularly through banks, shape the geographic clustering of high-growth startups?

- **Hypothesis**:  
  Reductions in local VC capital — especially via regulatory constraints like the Volcker Rule — lead to fewer local startups and greater migration to capital-rich regions.

- **Motivation**:  
  U.S. innovation and startups are geographically concentrated. Understanding whether capital availability, rather than startup quality or ecosystem effects, explains this clustering has policy implications for regional inequality.

---

## 📊 Data & Methodology
- **Data Source(s)**:  
  Call Reports (bank VC revenue), FR Y-9C (bank holding co.), VentureSource, Pitchbook, Form D (SEC), Preqin (LP investment)

- **Sample**:  
  U.S. VC funds and startups (2010–2018), 1,617 VC funds and 11,048 startups

- **Methodology**:
  - Natural experiment: Volcker Rule (banks barred from VC funds)
  - Difference-in-differences regressions
  - State-level variation in bank exposure to VC pre-Volcker
  - Treatment variable: “Bank Expo” (bank VC activity / # of funds)

---

## 📈 Key Findings
- VC fundraising dropped 9–11% in states more exposed to the Volcker Rule.
- VC funds became 22% smaller in those states.
- Startup first-round valuations declined ~9% and raised ~7% less capital.
- Startups were more likely to relocate to VC hubs (CA, MA, NY) — not to other non-hub states.
- Migration increased by ~30% in high-exposure states post-rule.
- LPs (banks, pensions) show strong home bias; capital didn’t flow freely across regions.

---

## 🧠 Theoretical Framework
- No formal structural model, but closely follows capital supply–demand framing.
- Heavily motivated by home bias, capital constraints, and VC-locality interaction theories.

---

## 🎯 Contribution to Literature
- Provides causal evidence linking **venture capital supply** to **startup clustering**.
- Highlights unintended regional impacts of the **Volcker Rule**.
- Adds to the literature on **financial intermediation**, **startup migration**, and **policy-induced market frictions**.

---

## ⚖️ Strengths and Weaknesses
- **Strengths**:
  - Exploits exogenous policy shock with strong heterogeneity
  - Rich datasets combine financing, valuation, and migration
  - Robust to pre-trend checks and alternative specifications

- **Limitations**:
  - Focus on VC-backed startups; generalizability to broader entrepreneurship unclear
  - Doesn’t fully isolate demand vs. supply side startup relocation motives
  - Migration reasons (e.g. tax, talent pool) may also influence results

---

## 🔗 Related Works
- Builds on:
  - Hochberg & Rauh (2013), Samila & Sorenson (2011)
  - Kerr & Nanda (2009), Gompers & Lerner (2000)
  - Ewens & Farre-Mensa (2020), González-Uribe (2020)

- Contrasts with:
  - Location-neutral capital access assumptions in startup ecosystem policies

---

## 💡 Notes & Future Questions
- Could LP home bias be reduced through federal pooling or policy mandates?
- Are similar clustering effects seen in countries with centralized VC systems?
- Could other shocks (e.g., COVID-19, remote work) reverse this capital centralization?
- Does founder background (wealth, mobility) moderate the migration response?

---

## 📚 Citation
Chen, J. & Ewens, M. (2023). *Venture Capital and Startup Agglomeration*. Journal of Finance (forthcoming).