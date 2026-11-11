"""Day 065: Dimensionality Reduction

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-07. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X, y = load_digits(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)
for components in [10, 20, 40]:
    pipe_scale = StandardScaler()
    Xtr_s = pipe_scale.fit_transform(Xtr); Xte_s = pipe_scale.transform(Xte)
    pca = PCA(n_components=components, random_state=42)
    Xtr_p = pca.fit_transform(Xtr_s); Xte_p = pca.transform(Xte_s)
    model = LogisticRegression(max_iter=3000).fit(Xtr_p, ytr)
    print(components, "variance:", round(pca.explained_variance_ratio_.sum(), 3), "accuracy:", round(model.score(Xte_p, yte), 3))
