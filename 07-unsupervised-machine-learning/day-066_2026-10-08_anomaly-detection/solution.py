"""Day 066: Anomaly Detection

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-08. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import make_blobs
from sklearn.ensemble import IsolationForest
import numpy as np

X, _ = make_blobs(n_samples=300, centers=1, cluster_std=0.7, random_state=42)
rng = np.random.default_rng(42)
outliers = rng.uniform(low=-8, high=8, size=(12, 2))
data = np.vstack([X, outliers])
model = IsolationForest(contamination=0.04, random_state=42).fit(data)
pred = model.predict(data)  # -1 = flagged anomaly, 1 = inlier
print("Flagged:", int(np.sum(pred == -1)), "of", len(data))
print("First flagged indices:", np.where(pred == -1)[0][:15])
