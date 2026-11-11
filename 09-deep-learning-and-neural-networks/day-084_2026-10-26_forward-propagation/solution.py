"""Day 084: Forward Propagation

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-26. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.array([[0.2, 0.4], [0.7, 0.1]])
W1 = np.array([[0.3, -0.2], [0.4, 0.1]])
b1 = np.array([0.0, 0.1])
W2 = np.array([[0.5], [-0.3]])
b2 = np.array([0.05])
hidden = sigmoid(X @ W1 + b1)
output = sigmoid(hidden @ W2 + b2)
print("Hidden layer:\n", hidden)
print("Predicted probabilities:\n", output)
