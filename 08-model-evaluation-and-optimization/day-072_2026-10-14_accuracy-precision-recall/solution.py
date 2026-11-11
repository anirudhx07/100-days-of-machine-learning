"""Day 072: Accuracy Precision Recall

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-14. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.metrics import accuracy_score, precision_score, recall_score

y_true = [1, 1, 1, 0, 0, 0, 0, 1]
y_pred = [1, 1, 0, 1, 0, 0, 0, 1]
TP = sum(a == 1 and b == 1 for a, b in zip(y_true, y_pred))
TN = sum(a == 0 and b == 0 for a, b in zip(y_true, y_pred))
FP = sum(a == 0 and b == 1 for a, b in zip(y_true, y_pred))
FN = sum(a == 1 and b == 0 for a, b in zip(y_true, y_pred))
print("TP/TN/FP/FN:", TP, TN, FP, FN)
print("Accuracy:", accuracy_score(y_true, y_pred), "Precision:", precision_score(y_true, y_pred), "Recall:", recall_score(y_true, y_pred))
