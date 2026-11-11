"""Day 035: Scatter Plots

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-07. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(4)
study_hours = rng.uniform(1, 8, 40)
scores = 35 + 7 * study_hours + rng.normal(0, 8, 40)
fig, ax = plt.subplots()
ax.scatter(study_hours, scores, alpha=0.75)
ax.set(title="Study hours and exam score", xlabel="Study hours", ylabel="Exam score")
fig.tight_layout()
plt.show()
