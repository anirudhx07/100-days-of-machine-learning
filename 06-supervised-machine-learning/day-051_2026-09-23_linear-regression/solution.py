"""Day 051: Linear Regression

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-23. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

X, y = make_regression(n_samples=300, n_features=1, noise=18, random_state=42)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42)
model = LinearRegression().fit(Xtr, ytr)
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_[0])
print("Test MAE:", mean_absolute_error(yte, model.predict(Xte)))
