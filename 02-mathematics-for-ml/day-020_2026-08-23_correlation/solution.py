"""Day 020: Correlation

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-23. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

study_hours = np.array([1, 2, 3, 4, 5, 6], dtype=float)
scores = np.array([48, 52, 61, 67, 72, 85], dtype=float)
print("Covariance matrix:\n", np.cov(study_hours, scores))
print("Correlation matrix:\n", np.corrcoef(study_hours, scores))
