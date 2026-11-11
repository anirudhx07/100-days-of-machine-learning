"""Day 011: Linear Algebra

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-14. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

A = np.array([[1, 2], [3, 4]], dtype=float)
B = np.array([[5, 6], [7, 8]], dtype=float)
print("A shape:", A.shape)
print("A + B:\n", A + B)
print("A @ B:\n", A @ B)
print("Transpose:\n", A.T)
