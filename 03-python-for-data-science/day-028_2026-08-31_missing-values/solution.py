"""Day 028: Missing Values

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-31. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import pandas as pd

df = pd.DataFrame({"age": [20, None, 22, 21, None], "score": [80, 90, None, 70, 85]})
print("Missing counts:\n", df.isna().sum())
filled = df.copy()
filled["age"] = filled["age"].fillna(filled["age"].median())
filled["score"] = filled["score"].fillna(filled["score"].median())
print("Median-imputed:\n", filled)
