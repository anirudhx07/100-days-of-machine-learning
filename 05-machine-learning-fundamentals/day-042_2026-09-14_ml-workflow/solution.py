"""Day 042: ML Workflow

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-14. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
print(classification_report(y_test, model.predict(X_test)))
