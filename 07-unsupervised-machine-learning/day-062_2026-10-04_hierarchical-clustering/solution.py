"""Day 062: Hierarchical Clustering

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-04. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
import numpy as np

X, _ = make_blobs(n_samples=120, centers=3, random_state=42)
for linkage in ["ward", "average", "complete"]:
    labels = AgglomerativeClustering(n_clusters=3, linkage=linkage).fit_predict(X)
    print(linkage, "cluster sizes:", np.bincount(labels))
