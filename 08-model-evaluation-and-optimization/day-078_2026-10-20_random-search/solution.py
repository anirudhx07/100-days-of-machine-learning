"""Day 078: Random Search

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-20. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from scipy.stats import loguniform
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

X, y = load_breast_cancer(return_X_y=True)
pipe = make_pipeline(StandardScaler(), SVC())
params = {"svc__C": loguniform(0.01, 100), "svc__gamma": loguniform(0.0001, 1), "svc__kernel": ["rbf"]}
search = RandomizedSearchCV(pipe, params, n_iter=20, cv=StratifiedKFold(5, shuffle=True, random_state=42), scoring="accuracy", random_state=42)
search.fit(X, y)
print("Best parameters:", search.best_params_)
print("Best CV score:", round(search.best_score_, 3))
