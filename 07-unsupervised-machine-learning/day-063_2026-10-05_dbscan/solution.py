"""Day 063: Dbscan

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-05. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import numpy as np

X, _ = make_moons(n_samples=400, noise=0.08, random_state=42)
X_scaled = StandardScaler().fit_transform(X)
for eps in [0.15, 0.25, 0.4]:
    labels = DBSCAN(eps=eps, min_samples=5).fit_predict(X_scaled)
    print("eps:", eps, "clusters:", len(set(labels) - {-1}), "noise:", int(np.sum(labels == -1)))
