"""Day 059: SVM

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-01. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)
for kernel in ["linear", "rbf"]:
    model = make_pipeline(StandardScaler(), SVC(kernel=kernel, C=1.0)).fit(Xtr, ytr)
    print(kernel, "test accuracy:", round(model.score(Xte, yte), 3))
