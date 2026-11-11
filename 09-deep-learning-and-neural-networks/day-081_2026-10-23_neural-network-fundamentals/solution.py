"""Day 081: Neural Network Fundamentals

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-23. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

x = np.array([2.0, -1.0])
weights = np.array([[0.5, 1.0], [-0.25, 0.75]])
bias = np.array([0.1, -0.2])
pre_activation = x @ weights + bias
activation = np.maximum(0, pre_activation)
print("Weighted sum:", pre_activation)
print("ReLU output:", activation)
