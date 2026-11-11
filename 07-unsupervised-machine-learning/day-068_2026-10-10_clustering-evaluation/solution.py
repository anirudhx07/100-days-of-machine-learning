"""Day 068: Clustering Evaluation

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-10. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.9, random_state=5)
X_scaled = StandardScaler().fit_transform(X)
labels = KMeans(n_clusters=4, n_init=10, random_state=5).fit_predict(X_scaled)
print("Silhouette score:", round(silhouette_score(X_scaled, labels), 3))
