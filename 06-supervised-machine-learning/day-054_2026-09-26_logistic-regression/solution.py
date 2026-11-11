"""Day 054: Logistic Regression

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-26. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000)).fit(Xtr, ytr)
probabilities = model.predict_proba(Xte)[:, 1]
predictions = (probabilities >= 0.5).astype(int)
print(classification_report(yte, predictions))
print("First 5 probabilities:", probabilities[:5].round(3))
