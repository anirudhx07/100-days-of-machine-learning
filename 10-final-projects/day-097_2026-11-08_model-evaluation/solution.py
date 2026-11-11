"""Day 097: Model Evaluation

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-11-08. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
model = RandomForestClassifier(n_estimators=200, random_state=42).fit(Xtr, ytr)
print(classification_report(yte, model.predict(Xte), target_names=load_breast_cancer().target_names))
print("Confusion matrix:\n", confusion_matrix(yte, model.predict(Xte)))
print("ROC AUC:", round(roc_auc_score(yte, model.predict_proba(Xte)[:, 1]), 3))
