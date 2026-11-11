"""Day 088: Build Neural Network

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-30. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X, y = load_digits(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)
models = {"Logistic baseline": make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000)), "MLP": make_pipeline(StandardScaler(), MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, early_stopping=True, random_state=42))}
for name, model in models.items():
    model.fit(Xtr, ytr)
    print(name, "test accuracy:", round(model.score(Xte, yte), 3))
