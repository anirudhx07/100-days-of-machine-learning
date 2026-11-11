"""Day 024: NumPy Mathematics

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-27. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

values = np.array([10.0, 20.0, 30.0, 40.0])
normalized = (values - values.min()) / (values.max() - values.min())
print("Normalized:", normalized)
print("Square roots:", np.sqrt(values))
print("Broadcasting:\n", np.array([[1], [2], [3]]) + np.array([10, 20]))
