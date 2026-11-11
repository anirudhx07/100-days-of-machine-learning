"""Day 064: PCA

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-06. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X, _ = load_wine(return_X_y=True)
X_scaled = StandardScaler().fit_transform(X)
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)
print("Reduced shape:", X_2d.shape)
print("Explained variance:", pca.explained_variance_ratio_.round(3))
print("Total explained:", round(pca.explained_variance_ratio_.sum(), 3))
