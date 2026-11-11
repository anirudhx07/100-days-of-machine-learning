"""Day 074: Roc Auc

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-16. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

X, y = make_classification(n_samples=600, n_features=10, weights=[0.65, 0.35], random_state=42)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=42)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(Xtr, ytr)
prob = model.predict_proba(Xte)[:, 1]
fpr, tpr, _ = roc_curve(yte, prob)
auc = roc_auc_score(yte, prob)
plt.plot(fpr, tpr, label=f"Logistic regression AUC={auc:.3f}")
plt.plot([0, 1], [0, 1], linestyle="--", label="Random baseline")
plt.xlabel("False-positive rate"); plt.ylabel("True-positive rate"); plt.legend(); plt.tight_layout(); plt.show()
