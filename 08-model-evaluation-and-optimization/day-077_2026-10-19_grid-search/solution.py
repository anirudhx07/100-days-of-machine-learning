"""Day 077: Grid Search

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-19. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

X, y = load_iris(return_X_y=True)
pipe = make_pipeline(StandardScaler(), SVC())
param_grid = {"svc__C": [0.1, 1, 10], "svc__kernel": ["linear", "rbf"]}
search = GridSearchCV(pipe, param_grid, cv=StratifiedKFold(5, shuffle=True, random_state=42), scoring="accuracy")
search.fit(X, y)
print("Best parameters:", search.best_params_)
print("Best CV score:", round(search.best_score_, 3))
