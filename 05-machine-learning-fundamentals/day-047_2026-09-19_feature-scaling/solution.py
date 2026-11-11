"""Day 047: Feature Scaling

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-19. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler, MinMaxScaler

X, _ = load_wine(return_X_y=True)
standard = StandardScaler().fit_transform(X)
minmax = MinMaxScaler().fit_transform(X)
print("Original first feature std:", X[:, 0].std().round(3))
print("Standardized mean/std:", standard[:, 0].mean().round(3), standard[:, 0].std().round(3))
print("Min-max range:", minmax[:, 0].min().round(3), minmax[:, 0].max().round(3))
