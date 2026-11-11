"""Day 082: Perceptron

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-24. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([0, 0, 0, 1])  # AND is linearly separable
weights = np.zeros(2); bias = 0.0; learning_rate = 0.1
for epoch in range(10):
    errors = 0
    for features, target in zip(X, y):
        prediction = int(features @ weights + bias >= 0.5)
        update = learning_rate * (target - prediction)
        weights += update * features; bias += update
        errors += int(update != 0)
    print(f"epoch={epoch + 1}, errors={errors}")
print("Predictions:", (X @ weights + bias >= 0.5).astype(int))
