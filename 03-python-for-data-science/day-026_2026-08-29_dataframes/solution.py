"""Day 026: Dataframes

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-29. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import pandas as pd

df = pd.DataFrame({"name": ["Asha", "Kabir", "Mira", "Dev"], "score": [91, 72, 85, 64], "city": ["Agra", "Delhi", "Agra", "Noida"]})
print(df.head())
print("Shape:", df.shape)
print("Dtypes:\n", df.dtypes)
print("High-scoring students:\n", df[(df["score"] >= 80) & (df["city"] == "Agra")])
