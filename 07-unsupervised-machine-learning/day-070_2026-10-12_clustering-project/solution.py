"""Day 070: Clustering Project

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-12. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X, _ = make_blobs(n_samples=500, centers=4, cluster_std=1.0, random_state=42)
pipeline = make_pipeline(StandardScaler(), KMeans(n_clusters=4, n_init=10, random_state=42))
labels = pipeline.fit_predict(X)
scaled = pipeline.named_steps["standardscaler"].transform(X)
print("Silhouette:", round(silhouette_score(scaled, labels), 3))
print("Segment sizes:\n", pd.Series(labels).value_counts().sort_index())
