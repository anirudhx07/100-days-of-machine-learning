"""Day 050: Overfitting Underfitting

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-22. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import make_moons
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = make_moons(n_samples=500, noise=0.25, random_state=42)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
for degree in [1, 2, 5, 12]:
    model = make_pipeline(PolynomialFeatures(degree), LogisticRegression(max_iter=2000))
    model.fit(Xtr, ytr)
    print(degree, "train:", round(accuracy_score(ytr, model.predict(Xtr)), 3), "test:", round(accuracy_score(yte, model.predict(Xte)), 3))
