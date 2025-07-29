신경망의 출력값 $\hat{y}$ 가 주어졌을 때,  각 입력값 $x_i$ 가 $\hat{y}$에 **얼마나 영향을 주는지**를 계산하고 싶습니다.

## 🔢 핵심 수식: 입력값 × 민감도(미분)

$$

\text{importance}_i = x_i \cdot \frac{\partial \hat{y}}{\partial x_i}


$$

$$

\boxed{\text{중요도} = \text{입력값} \times \text{출력의 변화율 (미분)}}


$$

- $x_i$ : 입력 벡터의 i번째 값
- $\frac{\partial \hat{y}}{\partial x_i}$ : 출력값이 $x_i$의 변화에 얼마나 민감한지를 나타내는 미분값
- 전체 식은 **입력값의 크기**와 **출력 변화율**을 곱한 것 → 중요도

## 📌 왜 이걸 쓰나요?

##### 예시 1: 입력은 크지만 영향 없음

- $x_i = 100$
- $\frac{\partial \hat{y}}{\partial x_i} = 0$
  → 중요도 = $100 \cdot 0 = 0$

##### 예시 2: 입력은 작지만 민감함

- $x_i = 0.1$
- $\cfrac{\partial \hat{y}}{\partial x_i} = 50$
  → 중요도 = $0.1 \cdot 50 = 5$

##### 예시 3: 입력도 크고 민감함

- $x_i = 2.0$
- $\cfrac{\partial \hat{y}}{\partial x_i} = 3.0$
  → 중요도 = $2.0 \cdot 3.0 = 6.0$

## 🎯 bias는 무시

#### 이유 1: bias는 상수입니다

$$\hat{y} = w_1 x_1 + w_2 x_2 + b$$

- 이때 $b$는 **모든 입력과 무관하게** 일정한 영향을 줍니다.
- 즉, 특정 feature가 더 중요하다고 말해주는 지표가 아닙니다.

#### 이유 2: 미분하면 bias는 사라집니다

- 위 식에서 미분해보면,  $b$는 상수이므로 미분하면 0이 되어, 중요도 계산에 영향 없습니다.
  $$
  \frac{\partial \hat{y}}{\partial x_1} = w_1, \quad \frac{\partial \hat{y}}{\partial x_2} = w_2
  $$

---

# 🎓 MLP Feature Importance — Matrix-based Proof

## 🏗️ 네트워크 구조 (2층 MLP 예시)

$$

\begin{align*}

\mathbf{h}_1 &= \phi_1(\mathbf{W}_1 \mathbf{x}) \\

\mathbf{h}_2 &= \phi_2(\mathbf{W}_2 \mathbf{h}_1) \\

\hat{y} &= \mathbf{W}_3 \mathbf{h}_2

\end{align*}


$$

입력층 → 은닉층 1 → 은닉층 2 → 출력층

- $\mathbf{W}_1 \in \mathbb{R}^{d_1 \times n}$
- $\mathbf{W}_2 \in \mathbb{R}^{d_2 \times d_1}$
- $\mathbf{W}_3 \in \mathbb{R}^{1 \times d_2}$
- bias 항은 무시

## ⚙️ 목표: $\frac{\partial \hat{y}}{\partial \mathbf{x}}$

체인 룰(Chain Rule)에 의해:

$$
\frac{\partial \hat{y}}{\partial \mathbf{x}} =

\frac{\partial \hat{y}}{\partial \mathbf{h}_2} \cdot

\frac{\partial \mathbf{h}_2}{\partial \mathbf{h}_1} \cdot

\frac{\partial \mathbf{h}_1}{\partial \mathbf{x}}
$$

## 🔢 Derivatives of each Layer

1. Output Layer: $\hat{y} = \mathbf{W}_3 \mathbf{h}_2 \Rightarrow\cfrac{\partial \hat{y}}{\partial \mathbf{h}_2} = \mathbf{W}_3$
2. Second Hidden Layer: $\cfrac{\partial \mathbf{h}_2}{\partial \mathbf{h}_1} =\text{diag}(\phi_2'(\mathbf{z}_2)) \cdot \mathbf{W}_2$
   1. $\mathbf{h}_2 = \phi_2(\mathbf{W}_2 \mathbf{h}_1)$
   2. Let $\mathbf{z}_2 = \mathbf{W}_2 \mathbf{h}_1$, then $\cfrac{\partial \phi_2(\mathbf{z}_2)}{\partial \mathbf{z}_2} = \text{diag} (\phi_2'(\mathbf{z}_2))$
3. First Hidden Layer: $\mathbf{h}_1 = \phi_1(\mathbf{W}_1 \mathbf{x}) \Rightarrow \cfrac{\partial \mathbf{h}_1}{\partial \mathbf{x}} = \text{diag}(\phi_1'(\mathbf{z}_1)) \cdot \mathbf{W}_1$

$$

\therefore \cfrac{\partial \hat{y}}{\partial \mathbf{x}} =

\mathbf{W}_3 \cdot \text{diag}(\phi_2') \cdot \mathbf{W}_2 \cdot \text{diag}(\phi_1') \cdot \mathbf{W}_1


$$

## 🎯 Feature-wise importance

$$

\text{importance}_i = x_i \cdot \frac{\partial \hat{y}}{\partial x_i}


$$

벡터 형태로 표현하면 ($\odot$는 element-wise 곱):

$$

\text{importance} = \mathbf{x} \odot \left( \frac{\partial \hat{y}}{\partial \mathbf{x}} \right)


$$
