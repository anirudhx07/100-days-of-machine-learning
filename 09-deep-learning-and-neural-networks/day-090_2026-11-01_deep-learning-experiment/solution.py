"""Day 090: Deep Learning Experiment

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-11-01. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import warnings
from sklearn.exceptions import ConvergenceWarning

X, y = load_digits(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)
for seed in [7, 21]:
    model = make_pipeline(StandardScaler(), MLPClassifier(hidden_layer_sizes=(64,), max_iter=400, early_stopping=True, random_state=seed))
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always", ConvergenceWarning)
        model.fit(Xtr, ytr)
    print("seed:", seed, "accuracy:", round(model.score(Xte, yte), 3), "convergence warnings:", sum(issubclass(w.category, ConvergenceWarning) for w in caught))
