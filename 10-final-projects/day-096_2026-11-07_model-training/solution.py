"""Day 096: Model Training

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-11-07. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import time

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
for trees in [50, 150, 300]:
    model = RandomForestClassifier(n_estimators=trees, random_state=42, n_jobs=-1)
    start = time.perf_counter(); model.fit(Xtr, ytr); duration = time.perf_counter() - start
    print("trees:", trees, "F1:", round(f1_score(yte, model.predict(Xte)), 3), "train seconds:", round(duration, 3))
