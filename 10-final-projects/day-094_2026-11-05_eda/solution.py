"""Day 094: EDA

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-11-05. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer(as_frame=True)
df = data.frame
print("Shape:", df.shape)
print("Missing values:", int(df.isna().sum().sum()))
print("Class counts:\n", data.target_names[0], int((df.target == 0).sum()), data.target_names[1], int((df.target == 1).sum()))
print(df.describe().T[["mean", "std", "min", "max"]].head(10))
df.iloc[:, :5].hist(figsize=(10, 6)); plt.tight_layout(); plt.show()
