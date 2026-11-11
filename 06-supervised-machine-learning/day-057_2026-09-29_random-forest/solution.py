"""Day 057: Random Forest

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-29. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)
models = {"Tree": DecisionTreeClassifier(random_state=42), "Forest": RandomForestClassifier(n_estimators=200, random_state=42)}
for name, model in models.items():
    model.fit(Xtr, ytr)
    print(name, "test accuracy:", round(model.score(Xte, yte), 3))
