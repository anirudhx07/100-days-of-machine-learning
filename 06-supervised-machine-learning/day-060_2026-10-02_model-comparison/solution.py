"""Day 060: Model Comparison

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-02. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)
models = {"Logistic": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)), "KNN": make_pipeline(StandardScaler(), KNeighborsClassifier()), "Forest": RandomForestClassifier(n_estimators=150, random_state=42)}
for name, model in models.items():
    model.fit(Xtr, ytr)
    pred = model.predict(Xte)
    print(name, "accuracy", round(accuracy_score(yte, pred), 3), "macro-F1", round(f1_score(yte, pred, average="macro"), 3))
