"""Day 043: Supervised Learning

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-15. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import make_regression, make_classification
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, accuracy_score

Xr, yr = make_regression(n_samples=200, n_features=3, noise=15, random_state=4)
Xtr, Xte, ytr, yte = train_test_split(Xr, yr, random_state=4)
reg = LinearRegression().fit(Xtr, ytr)
print("Regression R2:", round(r2_score(yte, reg.predict(Xte)), 3))

Xc, yc = make_classification(n_samples=200, n_features=5, random_state=4)
Xtr, Xte, ytr, yte = train_test_split(Xc, yc, random_state=4)
clf = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
print("Classification accuracy:", round(accuracy_score(yte, clf.predict(Xte)), 3))
