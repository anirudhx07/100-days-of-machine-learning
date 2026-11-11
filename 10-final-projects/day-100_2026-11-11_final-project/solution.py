"""Day 100: Final Project

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-11-11. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from pathlib import Path
import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, stratify=data.target, random_state=42)
model = make_pipeline(SimpleImputer(strategy="median"), StandardScaler(), LogisticRegression(max_iter=3000))
model.fit(X_train, y_train)
probabilities = model.predict_proba(X_test)[:, 1]
predictions = model.predict(X_test)
print(classification_report(y_test, predictions, target_names=data.target_names))
print("ROC AUC:", round(roc_auc_score(y_test, probabilities), 3))
Path("artifacts").mkdir(exist_ok=True)
joblib.dump(model, "artifacts/breast_cancer_pipeline.joblib")
loaded = joblib.load("artifacts/breast_cancer_pipeline.joblib")
print("Reloaded model prediction:", data.target_names[loaded.predict(X_test[:1])[0]])
