"""Day 034: Histograms

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-06. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(10)
exam_scores = rng.normal(loc=72, scale=12, size=500)
fig, ax = plt.subplots()
ax.hist(exam_scores, bins=10, edgecolor="black", alpha=0.8)
ax.set(title="Distribution of exam scores", xlabel="Score", ylabel="Number of students")
fig.tight_layout()
plt.show()
