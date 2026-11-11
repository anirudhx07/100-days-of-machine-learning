"""Day 039: Exploratory Data Analysis

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-09-11. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import pandas as pd
from sklearn.datasets import load_iris

data = load_iris(as_frame=True)
df = data.frame
df["species"] = df["target"].map(dict(enumerate(data.target_names)))
print("Shape:", df.shape)
print("Dtypes:\n", df.dtypes)
print("Missing values:\n", df.isna().sum())
print("Numeric summary:\n", df.describe())
print("Species counts:\n", df["species"].value_counts())
