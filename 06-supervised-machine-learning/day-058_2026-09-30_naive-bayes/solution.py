"""Day 058: Naive Bayes

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-30. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)
model = GaussianNB().fit(Xtr, ytr)
print(classification_report(yte, model.predict(Xte)))
