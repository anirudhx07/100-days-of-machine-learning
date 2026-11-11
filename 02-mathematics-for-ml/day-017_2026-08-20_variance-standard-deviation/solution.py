"""Day 017: Variance Standard Deviation

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-20. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

data = np.array([4, 5, 6, 7, 8], dtype=float)
print("Mean:", data.mean())
print("Population variance:", data.var(ddof=0))
print("Sample variance:", data.var(ddof=1))
print("Population std:", data.std(ddof=0))
print("Sample std:", data.std(ddof=1))
