"""Day 092: Dataset Collection

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-11-03. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import pandas as pd
from sklearn.datasets import load_iris
from pathlib import Path

data = load_iris(as_frame=True)
df = data.frame
df["target_name"] = df["target"].map(dict(enumerate(data.target_names)))
output = Path("iris_dataset.csv")
df.to_csv(output, index=False)
print("Saved:", output.resolve())
print("Rows/columns:", df.shape)
print("Target distribution:\n", df["target_name"].value_counts())
