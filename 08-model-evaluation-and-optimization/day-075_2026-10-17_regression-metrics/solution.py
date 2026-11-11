"""Day 075: Regression Metrics

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-10-17. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

X, y = make_regression(n_samples=250, n_features=3, noise=25, random_state=42)
Xtr, Xte, ytr, yte = train_test_split(X, y, random_state=42)
model = LinearRegression().fit(Xtr, ytr); pred = model.predict(Xte)
print("MAE:", mean_absolute_error(yte, pred))
print("MSE:", mean_squared_error(yte, pred))
print("RMSE:", np.sqrt(mean_squared_error(yte, pred)))
print("R2:", r2_score(yte, pred))
