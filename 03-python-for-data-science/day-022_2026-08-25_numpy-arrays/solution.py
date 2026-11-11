"""Day 022: NumPy Arrays

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-25. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

arr = np.arange(12)
matrix = arr.reshape(3, 4)
print("Original:", arr)
print("Reshaped:\n", matrix)
print("Transpose shape:", matrix.T.shape)
print("Zeros:\n", np.zeros((2, 3)))
