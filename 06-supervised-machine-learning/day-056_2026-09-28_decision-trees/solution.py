"""Day 056: Decision Trees

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-28. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)
for depth in [1, 2, 3, None]:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42).fit(Xtr, ytr)
    print("depth=", depth, "train=", round(tree.score(Xtr, ytr), 3), "test=", round(accuracy_score(yte, tree.predict(Xte)), 3))
