"""Day 079: Pipelines

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-21. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

X, y = load_breast_cancer(return_X_y=True)
# The pipeline ensures preprocessing is learned inside each training fold.
pipe = make_pipeline(SimpleImputer(strategy="median"), StandardScaler(), LogisticRegression(max_iter=3000))
scores = cross_val_score(pipe, X, y, cv=StratifiedKFold(5, shuffle=True, random_state=42))
print("CV scores:", scores.round(3), "mean:", round(scores.mean(), 3))
