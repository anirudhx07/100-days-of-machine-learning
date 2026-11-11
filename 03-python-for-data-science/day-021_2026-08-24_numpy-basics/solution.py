"""Day 021: NumPy Basics

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-24. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

values = [2, 4, 6, 8]
arr = np.array(values)
print("Array:", arr)
print("dtype:", arr.dtype, "shape:", arr.shape, "size:", arr.size, "ndim:", arr.ndim)
print("Doubled:", arr * 2)
