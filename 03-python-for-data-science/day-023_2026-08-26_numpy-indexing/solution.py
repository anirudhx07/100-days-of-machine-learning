"""Day 023: NumPy Indexing

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-26. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

arr = np.array([3, -2, 7, 0, 9, -5, 4])
print("First item:", arr[0])
print("Every second item:", arr[::2])
print("Positive values:", arr[arr > 0])
arr[arr < 0] = 0
print("After replacing negatives:", arr)
