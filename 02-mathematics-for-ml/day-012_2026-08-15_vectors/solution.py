"""Day 012: Vectors

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-15. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

a = np.array([2, 3, 4])
b = np.array([1, 0, -1])
manual_dot = sum(x * y for x, y in zip(a, b))
print("Manual dot product:", manual_dot)
print("NumPy dot product:", np.dot(a, b))
print("Magnitude of a:", np.linalg.norm(a))
