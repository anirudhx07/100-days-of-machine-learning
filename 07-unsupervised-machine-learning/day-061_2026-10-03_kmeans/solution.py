"""Day 061: Kmeans

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-03. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X, _ = make_blobs(n_samples=400, centers=4, cluster_std=0.75, random_state=42)
for k in [2, 3, 4, 5, 6]:
    model = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X)
    print("k=", k, "inertia=", round(model.inertia_, 1), "silhouette=", round(silhouette_score(X, model.labels_), 3))
