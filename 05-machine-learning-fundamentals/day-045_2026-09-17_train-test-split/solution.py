"""Day 045: Train Test Split

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-17. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from collections import Counter

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print("Train size:", len(X_train), "Test size:", len(X_test))
print("Train classes:", Counter(y_train))
print("Test classes:", Counter(y_test))
