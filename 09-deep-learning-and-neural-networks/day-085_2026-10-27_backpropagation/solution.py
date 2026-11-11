"""Day 085: Backpropagation

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-27. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

rng = np.random.default_rng(1)
X = np.array([[0,0], [0,1], [1,0], [1,1]], dtype=float)
y = np.array([[0], [1], [1], [0]], dtype=float)
W1 = rng.normal(0, 1, (2, 4)); b1 = np.zeros((1, 4))
W2 = rng.normal(0, 1, (4, 1)); b2 = np.zeros((1, 1))
def sigmoid(z): return 1 / (1 + np.exp(-z))
for epoch in range(8000):
    z1 = X @ W1 + b1; a1 = sigmoid(z1)
    z2 = a1 @ W2 + b2; yhat = sigmoid(z2)
    loss = np.mean((yhat - y) ** 2)
    dz2 = (2 / len(X)) * (yhat - y) * yhat * (1 - yhat)
    dW2 = a1.T @ dz2; db2 = dz2.sum(axis=0, keepdims=True)
    dz1 = (dz2 @ W2.T) * a1 * (1 - a1)
    dW1 = X.T @ dz1; db1 = dz1.sum(axis=0, keepdims=True)
    W2 -= 1.0 * dW2; b2 -= 1.0 * db2; W1 -= 1.0 * dW1; b1 -= 1.0 * db1
    if epoch % 2000 == 0: print("epoch", epoch, "loss", round(float(loss), 5))
print("XOR predictions:\n", (yhat > 0.5).astype(int))
