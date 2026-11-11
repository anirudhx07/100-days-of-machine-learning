"""Day 033: Bar Charts

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-05. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import matplotlib.pyplot as plt

products = ["Laptop", "Phone", "Tablet", "Watch"]
units = [35, 80, 24, 52]
fig, ax = plt.subplots()
ax.bar(products, units)
ax.set(title="Units sold by product", xlabel="Product", ylabel="Units")
ax.set_ylim(0, max(units) * 1.15)
fig.tight_layout()
plt.show()
