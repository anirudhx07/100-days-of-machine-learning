"""Day 071: Confusion Matrix

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-13. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

y_true = [1, 0, 1, 1, 0, 0, 1, 0]
y_pred = [1, 0, 0, 1, 0, 1, 1, 0]
cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
print("Rows=true [0,1], columns=predicted [0,1]:\n", cm)
ConfusionMatrixDisplay(cm, display_labels=["Negative", "Positive"]).plot()
plt.tight_layout()
plt.show()
