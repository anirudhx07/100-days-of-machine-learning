"""Day 055: KNN

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-27. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)
for k in [1, 5, 15]:
    model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=k)).fit(Xtr, ytr)
    print("k=", k, "accuracy=", round(accuracy_score(yte, model.predict(Xte)), 3))
