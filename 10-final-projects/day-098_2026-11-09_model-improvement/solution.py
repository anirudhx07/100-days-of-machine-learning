"""Day 098: Model Improvement

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-11-09. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
baseline = RandomForestClassifier(n_estimators=200, random_state=42).fit(Xtr, ytr)
search = GridSearchCV(RandomForestClassifier(random_state=42), {"n_estimators": [100, 200], "max_depth": [None, 5, 10], "min_samples_leaf": [1, 2]}, cv=StratifiedKFold(5, shuffle=True, random_state=42), scoring="f1", n_jobs=-1).fit(Xtr, ytr)
print("Baseline test F1:", round(f1_score(yte, baseline.predict(Xte)), 3))
print("Tuned test F1:", round(f1_score(yte, search.predict(Xte)), 3), "params:", search.best_params_)
