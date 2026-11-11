"""Day 076: Hyperparameter Tuning

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-18. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier

X, y = load_iris(return_X_y=True)
search = GridSearchCV(DecisionTreeClassifier(random_state=42), {"max_depth": [1, 2, 3, 4, None], "min_samples_leaf": [1, 2, 4]}, cv=StratifiedKFold(5, shuffle=True, random_state=42), scoring="accuracy")
search.fit(X, y)
print("Best params:", search.best_params_)
print("Best CV accuracy:", round(search.best_score_, 3))
