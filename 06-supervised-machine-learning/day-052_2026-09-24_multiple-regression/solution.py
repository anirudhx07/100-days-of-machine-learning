"""Day 052: Multiple Regression

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-24. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X, y = make_regression(n_samples=400, n_features=4, noise=20, random_state=7)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=7)
model = LinearRegression().fit(Xtr, ytr)
print("Coefficients:", model.coef_.round(2))
print("Intercept:", round(model.intercept_, 2))
print("Test R2:", round(r2_score(yte, model.predict(Xte)), 3))
