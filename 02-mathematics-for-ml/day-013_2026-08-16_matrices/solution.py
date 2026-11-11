"""Day 013: Matrices

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-16. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

M = np.arange(1, 10).reshape(3, 3)
print("Matrix:\n", M)
print("Center:", M[1, 1])
print("First row:", M[0, :])
print("Last column:", M[:, -1])
print("Shape:", M.shape, "Dimensions:", M.ndim)
