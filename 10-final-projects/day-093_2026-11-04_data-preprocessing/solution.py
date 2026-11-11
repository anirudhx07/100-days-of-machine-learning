"""Day 093: Data Preprocessing

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-11-04. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

data = load_iris(as_frame=True)
df = data.frame.copy()
df["size_group"] = pd.cut(df["sepal length (cm)"], bins=3, labels=["short", "medium", "long"])
X = df.drop(columns="target"); y = df["target"]
numeric = X.select_dtypes(include="number").columns
categorical = X.select_dtypes(exclude="number").columns
transformer = ColumnTransformer([("num", make_pipeline(SimpleImputer(strategy="median"), StandardScaler()), numeric), ("cat", make_pipeline(SimpleImputer(strategy="most_frequent"), OneHotEncoder(handle_unknown="ignore")), categorical)])
Xt = transformer.fit_transform(X)
print("Original features:", X.shape[1], "Transformed shape:", Xt.shape)
