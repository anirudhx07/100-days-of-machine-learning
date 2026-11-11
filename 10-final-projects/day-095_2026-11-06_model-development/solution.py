"""Day 095: Model Development

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-11-06. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xval, ytr, yval = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
candidates = {"logistic": make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000)), "random_forest": RandomForestClassifier(n_estimators=200, random_state=42)}
for name, model in candidates.items():
    model.fit(Xtr, ytr)
    print(name, "validation accuracy:", round(model.score(Xval, yval), 3))
