import matplotlib.pyplot as plt
import numpy as np

#%%
# Set up the Edgeworth box
total_endowment = np.array([2, 2])  # Each good's total supply

# Create a grid for allocations
x = np.linspace(0.01, 1.99, 50)
y = np.linspace(0.01, 1.99, 50)
X, Y = np.meshgrid(x, y)

# Cobb-Douglas utility functions (A: α=0.3, B: α=0.7)
U_A = (X)**0.3 * (Y)**0.7
U_B = (total_endowment[0] - X)**0.7 * (total_endowment[1] - Y)**0.3


# Compute marginal rates of substitution for both A and B
# MRS_A = (dU/dx1) / (dU/dx2) = (0.3/x1) / (0.7/x2) = (0.3/0.7) * (x2/x1)
# MRS_B = (0.7/x1') / (0.3/x2') = (0.7/0.3) * (x2'/x1') where x1' = 2 - x1, x2' = 2 - x2

MRS_A = (0.3 / 0.7) * (Y / X)
MRS_B = (0.7 / 0.3) * ((total_endowment[1] - Y) / (total_endowment[0] - X))

# Find where MRS_A ≈ MRS_B (contract curve)
diff = np.abs(MRS_A - MRS_B)
contract_curve_mask = diff < 0.05

# Set an initial endowment point (example: A starts with (1.2, 0.8))
endowment_A = np.array([1.2, 0.8])
endowment_B = total_endowment - endowment_A

# Compute MRS at endowment for both consumers
MRS_A_e = (0.3 / 0.7) * (endowment_A[1] / endowment_A[0])
MRS_B_e = (0.7 / 0.3) * (endowment_B[1] / endowment_B[0])

# We'll use A's MRS at endowment as the price ratio: p1/p2 = MRS_A_e
price_slope = -MRS_A_e

# Create budget line passing through A's endowment with slope = -price ratio
x_vals = np.linspace(0, 2, 100)
budget_line = endowment_A[1] + price_slope * (x_vals - endowment_A[0])

# Re-plot Edgeworth box with contract curve and budget line
fig, ax = plt.subplots(figsize=(8, 8))
ax.contour(X, Y, U_A, colors='blue', linestyles='dotted', levels=10)
ax.contour(X, Y, U_B, colors='red', linestyles='dashed', levels=10)
ax.plot([0, 2, 2, 0, 0], [0, 0, 2, 2, 0], 'k-')

# Contract curve
ax.scatter(X[contract_curve_mask], Y[contract_curve_mask], color='green', s=20, label='Contract Curve')

# Endowment point
ax.plot(endowment_A[0], endowment_A[1], 'ko', label='Initial Endowment (A)', markersize=20, marker="x")

# Budget line
ax.plot(x_vals, budget_line, 'purple', label='Price Line (Budget Line)', linestyle='-.')

# Labels
ax.set_title('Edgeworth Box with Contract Curve, Endowment, and Price Line\nIndifference Curves for A (blue) and B (red) with Cobb-Douglas')
ax.set_xlabel("Good 1 for A")
ax.set_ylabel("Good 2 for A")
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.show()



#%%
# Define a simple production possibility frontier (PPF)
# Let's assume y = 2 - x^2 (nonlinear decreasing)
x_prod = np.linspace(0, np.sqrt(2), 100)
y_prod = 2 - x_prod**2  # PPF: good 2 as function of good 1

# Indifference curve for Robinson Crusoe (Cobb-Douglas α = 0.5)
# u = x^0.5 * y^0.5 → y = u^2 / x
u_level = 1  # chosen utility level
x_util = np.linspace(0.1, np.sqrt(2), 100)
y_util = (u_level**2) / x_util

# Plot
plt.figure(figsize=(8, 6))
plt.plot(x_prod, y_prod, label='Production Possibility Frontier (PPF)', color='green')
plt.plot(x_util, y_util, label='Indifference Curve (Utility = 1)', color='blue', linestyle='--')

# Equilibrium point where utility curve is tangent to PPF
# For Cobb-Douglas, optimal occurs when MRS = MRT
x_eq = 1
y_eq = 1  # Since x * y = 1 → y = 1 when x = 1
plt.plot(x_eq, y_eq, 'ro', label='Equilibrium (Production = Consumption)')

# Labels
plt.title("Robinson Crusoe Economy: Production & Consumption Equilibrium")
plt.xlabel("Good 1")
plt.ylabel("Good 2")
plt.legend()
plt.grid(True)
plt.xlim(0, 1.6)
plt.ylim(0, 2.2)
plt.tight_layout()
plt.show()
