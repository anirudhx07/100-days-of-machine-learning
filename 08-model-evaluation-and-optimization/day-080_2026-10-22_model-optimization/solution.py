"""Day 080: Model Optimization

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-22. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
import time

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=42)
baseline = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000))
t0 = time.perf_counter(); baseline.fit(Xtr, ytr); baseline_time = time.perf_counter() - t0
search = GridSearchCV(make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000)), {"logisticregression__C": [0.01, 0.1, 1, 10]}, cv=5, scoring="f1")
t0 = time.perf_counter(); search.fit(Xtr, ytr); tuned_time = time.perf_counter() - t0
print("Baseline F1:", round(f1_score(yte, baseline.predict(Xte)), 3), "seconds:", round(baseline_time, 3))
print("Tuned F1:", round(f1_score(yte, search.predict(Xte)), 3), "seconds:", round(tuned_time, 3), "params:", search.best_params_)
