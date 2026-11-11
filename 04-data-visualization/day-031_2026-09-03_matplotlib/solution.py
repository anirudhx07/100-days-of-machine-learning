"""Day 031: Matplotlib

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-03. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 4, 8, 7]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, y, marker="o", label="Observed value")
ax.set(title="A first Matplotlib plot", xlabel="Observation", ylabel="Value")
ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
plt.show()
