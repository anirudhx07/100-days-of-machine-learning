"""Day 049: Cross Validation

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-21. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
scores = cross_val_score(model, X, y, cv=cv, scoring="accuracy")
print("Fold scores:", scores.round(3))
print("Mean ± std:", round(scores.mean(), 3), "±", round(scores.std(), 3))
