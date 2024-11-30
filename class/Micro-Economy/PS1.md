
- $\succeq$ is completeness
	- Since $c$ satisfies finite nonemptiness, either $x \in c(\{x,y\})$ or $y \in c(\{x,y\})$
	- hence either $x \succeq_c y$ or $y \succeq_c x$
- Transitivity
	- Suppose $x \succeq_c y$ and $y \succeq_c z$. It implies that $x \in c(\{x,y,z\})$
	- Indeed, suppose to the contrary that this is not so, that is $x \notin c(\{x,y,z\})$
	- It cannot be that $y \in c(\{x,y,z\})$, for it were, then $x \notin c(\{x,y\})$ by choice coherence
		- Take $A=\{x,y,z\}$ and $B=\{x,y\}$; then $x,y \in A \cap B$, $y \in c(A)$, $x \notin c(A)$ 
		- hence choice coherence implies that $x \notin c(B)$, contrary to our original hypothesis
- +) Reflexivity: For any alternative $x \in X$, $x \sim x$ (weak preference over itself).
- if $\succeq$ is complete and transitive, then $NBT(x)$ is nonempty for all $x$. 
	- In particular, $x \in NBT(x)$.
	- Moreover, $x \succeq y$ if and only if $NBT(y) \subseteq NBT(x)$.
	- If $x \succ y$ then $NBT(y)$ is a proper subset of $NBT(x)$.

- Properties of a utility function
	- Completeness: $\forall x, y \in X$, either $x \succeq y$ or $y \succeq x$
	- Transitivity: If $x \succeq y$ and $y \succeq z$, then $x \succeq z$
	- Continuity: any sequence $\forall x_n$, converging to an alternatives $x$, if $x_n \succeq y$, $\forall n$, then $x \succeq y$ 

---

1. ==Prove that if $\succeq$ is rational (complete and transitive), then== 
	1. ==$\succ$ is both irreflexive ($x \succ x$ never holds) and transitive (if $x \succ y$ and $y\succ z$, then $x \succ z$);==
		1. Irreflexivity
			1. By completeness of preference $\succeq$, $\forall x \in X$(for any x in choice set X) we know that $x\succeq x$ or $x \preceq x$.
			2. Assume $x \succ x$, than $x \nsucceq x$
			3. So, $\forall x \in X$, $x \nsucceq x$
			4. Thus, $\succ$ is irreflexive
		2. Transitivity
			1. Suppose $x \succ y$ and $y \succ z$,  $\forall x,y,z \in X$
			2. it means $x \succeq y$ and $y \nsucceq x$. it also means $y \succeq z$ and $z \nsucceq y$
			3. i) Show $x \succeq z$
				1. by transitivity of preference $\succeq$, if $x \succeq y$ and $y \succeq z$, then $x \succeq z$
			4. ii) Show $z \nsucceq x$
				1. Assume to the contrary, $z \succeq x$
				2. By transitivitity $\succeq$, since $x \succeq y$, then $z \succeq y$, 
				3. So there is contradiction. $\therefore z \nsucceq x$
			5. By i) and ii), we can see $x \succ z$
	2. ==$∼$ is reflexive ($x ∼ x$, $\forall x$), transitive (if $x ∼ y$ and $y ∼ z$, then $x ∼ z$) and symmetric (if $x ∼ y$ then $y ∼ x$)==
		1. Reflexivity
			1. By completeness of $\succeq$, $\forall x \in X$, then $x \succeq x$ or $x \preceq x$ hold. So, $x\sim x$
		2. Transitivity
			1. Supoose $x \sim y$ and $y \sim z$, $\forall x,y,z \in X$
			2. It implies either $x \succeq y$ and $y \succeq x$. By the same way, $y \succeq z$ and $z \succeq y$
			3. i) Show $x \succeq z$
				1. By transitivity of $\succeq$, if $x \succeq y$ and $y \succeq z$ then $x \succeq z$
			4. ii) Show $z \succeq x$
				1. By transitivity of $\succeq$, if $y \succeq x$ and $z \succeq y$, then $z \succeq x$
			5. By i) and ii), $x \sim z$. transitivity also holds.
		4. Symmetry
			1. Assume $x \sim y$, $\forall x,y \in X$
			3. It means either $x \succeq y$ and $y \succeq x$. By the same way, $y \succeq x$ and $x \succeq y$
			4. In either case, we have $y \sim x$, satisfying symmetry
			5. Therefore, $\sim$ is symmetric
	3. ==if $x \succ y \succeq z$ then $x \succ z$==
		1. It means $x \succeq y$, $y \nsucceq x$, $y \succeq z$
		2. a) Show $x \succeq z$
			1. By transitivity of $\succeq$, if $x \succeq y$ and $y \succeq z$, then $x \succeq z$
		3. b) Show $z \nsucceq x$: Assume to the contrary
			1. Suppose $z \succeq x$.
			2. By transitivity of $\succeq$ , since we know that $y \succeq z$, thus $y \succeq x$ 
			3. This is contradiction
		4. By a) and b), we can see $x \succ z$

2. 
	1. ==Show that if $f : \mathbb{R} \rightarrow \mathbb{R}$ is a strictly increasing function and $u : X \rightarrow \mathbb{R}$ is a utility function representing the preference relation $\succeq$, then the function $v : X \rightarrow \mathbb{R}$ defined by $v(x) = f(u(x))$ is also a utility function representing $\succeq$;==
		1. We need show that function $v(x) = f(u(x))$ also represents preference $\succeq$
		2. We know that $\forall x,y \in X$. 
		3. It means "$x \succeq y \leftrightarrow u(x) \geq u(y)$", and "$u(x) \geq u(y) \leftrightarrow f(u(x)) \geq f(u(y))$"
		4. $u(x) \geq u(y)$ implies $u(x) > u(y)$ or $u(x) = u(y)$
		5. Similarly, $f(u(x)) \geq f(u(y))$ implies $f(u(x)) > f(u(y))$ or $f(u(x))=f(u(y))$
		6. i) Show $u(x) >u(y) \leftrightarrow f(u(x)) > f(u(y))$
			1. For this direction $\hookrightarrow$, it holds because $f$ is strictly increasing function
			2. For opposite direction $\hookleftarrow$, assume to the contrary
				2. $u(x) \leq u(y) \leftrightarrow u(x) < u(y)$ or $u(x)=u(y)$
				3. If $u(x) < u(y)$, then $f(u(x))< f(u(y))$ -> contradiction
				4. If $u(x) = u(y)$, then $f(u(x)) = f(u(y))$ -> contradiction
			3.  $\therefore u(x) >u(y)$
		7. ii) $u(x) = u(y) \leftrightarrow f(u(x)) = f(u(y))$
			1. For this direction $\hookrightarrow$, it holds because $f$ is function
			2. For opposite direction $\hookleftarrow$, assume to the contrary
				1. $u(x) \neq u(y)$, so without loss of generality, assume that $u(x) >u(y)$
				2. Since $f$ is strictly increasing function, we can see that $f(u(x)) > f(u(y))$ which is contradiction $f(u(x)) = f(u(y))$
		8. By proposition i) and ii), $u(x) \geq u(y) \leftrightarrow f(u(x)) \geq f(u(y))$
		9. Thus, function $v(x)=f(u(x))$ can also represent $\succeq$ since $u$ implies $\succeq$
		
		
	2. ==Consider a preference relation $\succeq$ and a function $u : X \rightarrow \mathbb{R}$. Show that if $u(x) = u(y)$ implies $x ∼ y$ and if $u(x) > u(y)$ implies $x \succ y$ then $u(\cdot)$ is a utility function representing $\succeq$==
		1. What have to prove?
			2. If $u(x) = u(y)$, then $x \sim y$. Also if $u(x) > u(y)$, then $x \succ y$
			3. Then, utility function $u$ represents $\succeq$
		2. We need to show that $x \succeq y$ implies $x\succ y$ or $x \sim y$
		3. First, $x \succ y$ implies $(x \succeq y) \cap (y \nsucceq x)$
		4. Second, $x \sim y$ implies $(x \succeq y) \cap (y \succeq x)$
		5. Then $(x\succ y) \cup (x \sim y) = (x \succeq y)((y \nsucceq x) \cup (y \nsucceq x)) = (x \succeq y)$
		6. So we show that $x \succeq y$ implies $x \succ y$ or $x \sim y$
		7. It also implies $u(x)>u(y)$ or $u(x)=u(y)$
		8. It also implies $u(x) \geq u(y)$
		9. Thus, $u$ represents $\succeq$


3. ==Show that if $X$ is finite and $\succeq$ is a rational preference relation on $X$, then there is a utility function $u : X \rightarrow \mathbb{R}$ that represents $\succeq$==
	1. Define $u(x) = \text{the number of elements of }NBT(x)$ for all $x, y \in X$
	2. Since $X$ is finite set, subset of X is also finite.
	3. So we can see that $u(x)$ is well defined $\forall x \in X$. It means that $u(x)$ has finite number. So we can compare the number of utility function
	4. Now we will show that $x \succeq y \leftrightarrow NBT(y) \subseteq NBT(x) \leftrightarrow u(x) \geq u(y)$
		1. i) Show $x \succeq y \leftrightarrow NBT(y) \subseteq NBT(x)$
			1. For this direction $\hookrightarrow$,  
				1. $\forall z \in NBT(y)$ implies $y \succeq z$ and $x \succeq z$ because of transitivity of $\succeq$
				2. $\forall z \in NBT(y)$,  also $z \in NBT(x)$. we can show that $NBT(y) \subseteq NBT(x)$
			2. For opposite direction $\hookleftarrow$, 
				1. By the completeness of $\succeq$, $y \succeq y$. therefore $y \in NBT(y)$
				2. Since $y \in NBT(y)$ and $NBT(y) \subseteq NBT(x)$, then $y \in NBT(x)$
				3. Therefore, $x \succeq y$
		2. ii) Show $u(x) \geq u(y) \leftrightarrow NBT(y) \subseteq NBT(x)$
			1. For this direction $\hookrightarrow$,  
				1. By the completeness of $\succeq$, it is either $x \succeq y$ or $y \succeq x$
				2. Therefore, it is either $NBT(y) \subseteq NBT(x)$ or $NBT(x) \subseteq NBT(y)$
				3. Since $u(x) \geq u(y)$, it should be $NBT(y) \subseteq NBT(x)$
			2. For opposite direction $\hookleftarrow$, 
				1. Since X is finite set, so any subset should also be finite
				2. Therefore, $u(x)$ should also be finite $\forall x \in X$
				3. Then, since we assume $NBT(y) \subseteq NBT(x)$ holds, it is trivial the number of $NBT(X)$ has no less thant the number of $NBT(y)$
				4. Therefore $u(x) \geq u(y)$ holds.
				5. Because $u$ is real value function. So $u(x)$ and $u(y)$ can be ordered
		3. Therefore $x \succeq y \leftrightarrow u(x) \geq u(y)$  
	

4. ==Consider a choice problem with choice set $X = \{x, y, z\}$. For every choice structure determine if it satisfies choice coherence. Make sure to justify your answer. Consider the following choice structures $(\mathcal{A}' , C(\cdot))$ where:== 
	1. ==$\mathcal{A}' = \{\{x, y\}, \{y, z\}, \{x, z\}, \{x\}, \{y\}, \{z\}\}$ and $C(\{x, y\}) = \{x\}$, $C(\{y, z\}) = \{y\}$, $C(\{x, z\}) = \{z\}$, $C(\{x\}) = \{x\}$, $C(\{y\}) = \{y\}$, $C(\{z\}) = \{z\}$.== 
		1. There exists at most one element in every possible intersection of $\forall A,B \in \mathcal{A}'$
		2. So choice coherence satisfies.
	2. ==$\mathcal{A}' = \{\{x, y, z\}, \{x, y\}, \{y, z\}, \{x, z\}, \{x\}, \{y\}, \{z\}\}$ and $C(\{x, y, z\}) = \{x\}$, $C(\{x, y\}) = \{x\}$, $C(\{y, z\}) = \{z\}$, $C(\{x, z\}) = \{z\}$, $C(\{x\}) = \{x\}$, $C(\{y\}) = \{y\}$, $C(\{z\}) = \{z\}$.== 
		1. Let choice set $A=\{x,y,z\}$ and $B=\{x,z\}$ and $A\cap B=\{x,z\}$
		2. Then,  $x \in C(A)$ while $z \notin C(A)$
		3. $A\cap B=\{x,z\}$ implies $z \notin C(B)$
		4. For given choice structure, $z \in C(B)$. Thus, choice structure in B doesn't satisfy choice coherence
	3. ==$\mathcal{A}' = \{\{x, y, z\}, \{x, y\}, \{y, z\}, \{x, z\}, \{x\}, \{y\}, \{z\}\}$ and $C(\{x, y, z\}) = \{x\}$, $C(\{x, y\}) = \{x\}$, $C(\{y, z\}) = \{y\}$, $C(\{x, z\}) = \{x\}$, $C(\{x\}) = \{x\}$, $C(\{y\}) = \{y\}$, $C(\{z\}) = \{z\}$.== 
		1. Let choice set $A=\{x,y,z\}$ and $B=\{x,y\}$ and $A\cap B=\{x,y\}$
			1. Since $x \in C(A)$ and $y \notin C(A)$, it also need to be $y \notin C(B)$ which is same as given choice structure
		2. See $A=\{x,y\}$ and $B=\{x,y,z\}$. Same as a previous line.
		3. Let $A=\{x,y,z\}$ and $B=\{x,z\}$. Than $A \cap B = \{x,z\}$
			1. Then since $x \in C(A)$ and $z \notin C(A)$. 
			2. However $z \notin C(B)$. Thus, this choice coherence holds.
		5. Let's look vise versa of previous line: See $A=\{x,z\}$ and $B=\{x,y,z\}$
		6. See $A=\{y,z\}$ and $B=\{x,y,z\}$ -> $A\cap B = \{y,z\}$
		7. Since $y \in C(A)$ and $z \notin C(A)$, it needs to be $z \notin C(B)$
		8. 이렇게 모든 intersection을 확인해야 함...
		9. Thus, choice structure C satisfies the choice coherence in every possible cases

5. ==Show that if $X$ is finite, then any rational preference relation generates a nonempty choice rule; that is, $C(B) \neq \emptyset$ for any $B \subset X$ with $B \neq \emptyset$.==
	1. Let's define choice function $C_{\succeq}(A) = \{x \in A: x \succeq y \ for \ all \ y \in A \}$ 
	2. Let's consider finite and nonempty set choice set $B \subset X$
		1. (i) if the number of B is 1 ($B=\{x\}$), (single element)
			1. then $C_{\succeq}(B) = \{x\}$ since the preference relationship is complete. Therefore $x \succeq x$
			2. Thus, $C_{\succeq}(B)$ is nonempty when the number of B is 1
		2. (ii) Assume that $C_{\succeq}(A)$ is nonempty for all size of sets $n-1$
			1. Let $B$ has $n$ elements
			2. $B'=B \backslash \{x_0\}$ : it means $B'$ is a set $B$ excluded $x_0$ ($\forall x_0 \notin B$)
			3. Size of set $B'$ is $n-1$ ($\#B'=n-1$),
				1. We assume that for all size of sets $n-1$, the choice function is nonempty.
				2. So there exists $\forall x' \in B'$ that satisfies $x' \succeq y$ for all $y \in B'$
			4. By the completeness of the preference relationship, it is either $x' \succeq x_0$ or $x_0 \succeq x'$ hold
				1. 1) If $x' \succeq x_0$ holds, then $x' \succeq y$ for all $y \in B$
					1. Thus it implies $x' \in C_{\succeq}(B)$
				2. 2) If $x_0 \succeq x'$, 
					1. then $x_0 \succeq x_0$ by completeness of $\succeq$
					2. then $x_0 \succeq y$ for all $y \in B'$ by the transitivity of $\succeq$ 
					3. because: $\because x' \succeq y, \forall y \in B'$ 
					4. Since$x_0 \succeq x'$ by assumption 2)
					5. By the transitivity, $x_0 \succeq y, \forall y \in B'$
					6. Thus we can see that $x_0 \in C_{\succeq}(B)$
	3. So we show that for finite set $A$ we assume that $C_{\succeq}(A)$ is nonempty set for all size of sets $n-1$. Then it is also true $C_{\succeq}(A)$ is non empty set for all size of sets $n$. 
	4. By the mathematical induction, we show that the nonemptyness of choice function holds all sets of sizes. It means for arbitrary size, nonemptyness holds in hoice function 

