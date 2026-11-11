"""Day 073: F1 Score

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-15. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.metrics import f1_score, precision_score, recall_score

y_true = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
y_pred = [1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1_manual = 2 * precision * recall / (precision + recall)
print("Precision:", precision, "Recall:", recall)
print("Manual F1:", f1_manual, "scikit-learn F1:", f1_score(y_true, y_pred))
