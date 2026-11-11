"""Day 014: Matrix Operations

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-17. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])  # (2, 3)
B = np.array([[1, 2], [3, 4], [5, 6]])  # (3, 2)
print("Matrix product shape:", (A @ B).shape)
print(A @ B)
print("Element-wise product is only valid for matching/broadcastable shapes:")
C = np.array([[10, 10, 10], [20, 20, 20]])
print(A * C)
