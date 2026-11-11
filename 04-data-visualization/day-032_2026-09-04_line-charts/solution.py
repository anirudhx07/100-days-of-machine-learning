"""Day 032: Line Charts

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-04. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [12, 15, 13, 19, 24]
fig, ax = plt.subplots()
ax.plot(months, revenue, marker="o")
max_index = revenue.index(max(revenue))
ax.annotate("Peak", (months[max_index], revenue[max_index]), xytext=(-20, 10), textcoords="offset points")
ax.set(title="Monthly revenue trend", xlabel="Month", ylabel="Revenue (₹ thousands)")
fig.tight_layout()
plt.show()
