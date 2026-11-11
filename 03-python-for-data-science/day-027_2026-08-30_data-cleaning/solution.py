"""Day 027: Data Cleaning

Reference solution for the 100 Days of Machine Learning learning plan.
Scheduled date in folder: 2026-08-30. This file is populated now; it does not
assert that this work was completed on the scheduled date.
"""

import pandas as pd

df = pd.DataFrame({"name": [" Asha ", "kabir", "Asha "], "city": ["agra", "DELHI", "agra"], "score": [91, 72, 91]})
df["name"] = df["name"].str.strip().str.title()
df["city"] = df["city"].str.strip().str.title()
df = df.drop_duplicates()
print(df)
