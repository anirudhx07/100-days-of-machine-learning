"""Day 044: Unsupervised Learning

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-16. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X, _ = make_blobs(n_samples=250, centers=3, cluster_std=0.8, random_state=42)
model = KMeans(n_clusters=3, n_init=10, random_state=42)
labels = model.fit_predict(X)
print("Cluster counts:", {int(k): int(v) for k, v in zip(*__import__("numpy").unique(labels, return_counts=True))})
print("Centroids:\n", model.cluster_centers_)
