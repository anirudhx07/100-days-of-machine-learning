"""Day 089: Introduction To CNN

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-31. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np

image = np.array([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]], dtype=float)
edge_filter = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=float)
feature_map = np.zeros((3, 3))
for row in range(3):
    for col in range(3):
        region = image[row:row+3, col:col+3]
        feature_map[row, col] = np.sum(region * edge_filter)
print("Input image:\n", image)
print("Convolution feature map:\n", feature_map)
