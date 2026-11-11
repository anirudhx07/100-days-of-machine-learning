"""Day 053: Polynomial Regression

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-25. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

rng = np.random.default_rng(3)
X = np.linspace(-3, 3, 120).reshape(-1, 1)
y = 2 + 1.5 * X.ravel() - 0.8 * X.ravel()**2 + rng.normal(0, 1.5, 120)
for degree in [1, 2, 5, 12]:
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression()).fit(X, y)
    print("Degree", degree, "MSE", round(mean_squared_error(y, model.predict(X)), 2))
